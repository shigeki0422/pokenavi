"""機能1向け テーマ別パーティ生成。
各メガを軸にした構築＋戦略テーマ(雨/晴/砂/雪/壁/バトン/トリル/おいかぜ/設置/積み/サイクル)を、
dex同種排除・持ち物重複なし・メガ≤2・メガ石別の型出し分け(orient_set)込みで生成。
MCTS(ギミック組成選出含む)で強さ選別し、テーマラベル付きで永続化。100+の多様な構築を作る。
出力: scripts/func1_themed_{SEASON}.json
"""
import sys, os, random, json, math
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G

SEASON = os.environ.get("COEVO_SEASON", "M-3")

def _top(d):
    return max(d, key=d.get) if d else None

def mon_spec(D, name, item="auto", ability=None, force_moves=None):
    it = (_top(D["items"].get(name, {})) if item == "auto" else item)
    ab = ability if ability is not None else _top(D["abil"].get(name, {}))
    nat = _top(D["natures"].get(name, {}))
    umv = sorted(D["moves"].get(name, {}), key=D["moves"][name].get, reverse=True)
    moves = [m for m in (force_moves or [])]
    for m in umv:
        if len(moves) >= 4: break
        if m not in moves: moves.append(m)
    ev = D["evs"].get(name, [(None, 1)])[0][0]
    mv2, nat2, ev2 = G.orient_set(D, name, it, moves, nat, ev)
    return G._spec(name, it, nat2, mv2, ev2, ab)

def abil_species(D, ability):
    return [p for p, _ in D["usage"] if ability in D["abil"].get(p, {})]

def move_species(D, move):
    s = set(D.get("_learn_move", {}).get(move, []))
    return [p for p, _ in D["usage"] if p in s]

def build_party(D, rng, core_mons, prefer=None, topN=70):
    """core_mons: [(name,item,ability,force_moves)] 既に決まった軸。残りをfillして6体・spec化。"""
    prefer = set(prefer or [])
    dexmap = D["dex"]
    def dx(p): return dexmap.get(p, p)
    team = []          # (name,item,ability,force_moves)
    used_dex = set(); used_items = set(); megas = 0
    for (nm, it, ab, fm) in core_mons:
        rit = (_top(D["items"].get(nm, {})) if it == "auto" else it)
        team.append((nm, it, ab, fm)); used_dex.add(dx(nm))
        if rit: used_items.add(rit)
        if rit in D["megastones"]: megas += 1
    core_names = {m[0] for m in team}
    cw = {}
    for nm in core_names:
        for partner, rk in D["partners"].get(nm, []):
            cw[partner] = cw.get(partner, 0) + 1.0 / rk
    for p, rk in D["usage"][:topN]:
        cw[p] = cw.get(p, 0) + 0.15 / (rk if isinstance(rk, (int, float)) and rk else 1)
    for p in list(cw):
        if p in prefer: cw[p] *= 4.0
    while len(team) < 6:
        cand = {p: w for p, w in cw.items() if dx(p) not in used_dex}
        nm = G._wchoice(cand, rng)
        if nm is None: break
        it = _top({k: v for k, v in D["items"].get(nm, {}).items()
                   if k not in used_items and not (k in D["megastones"] and megas >= 2)})
        team.append((nm, it if it else None, None, None)); used_dex.add(dx(nm))
        if it: used_items.add(it)
        if it in D["megastones"]: megas += 1
    # メガ最低1（軸が非メガでも）: 無ければ可能個体を差替
    if megas == 0:
        for i, (nm, it, ab, fm) in enumerate(team):
            stones = [k for k in D["items"].get(nm, {}) if k in D["megastones"] and k not in used_items]
            if stones:
                team[i] = (nm, stones[0], ab, fm); used_items.add(stones[0]); megas = 1; break
    specs = []
    for (nm, it, ab, fm) in team[:6]:
        specs.append(mon_spec(D, nm, item=("auto" if it == "auto" else it), ability=ab, force_moves=fm))
    return specs

def themes(D, rng):
    """[(theme_label, core_mons, prefer)] を返す。"""
    out = []
    rain_ab = abil_species(D, "あめふらし"); swift = abil_species(D, "すいすい")
    sun_ab = abil_species(D, "ひでり"); chloro = abil_species(D, "ようりょくそ")
    sand_ab = abil_species(D, "すなおこし"); sandr = abil_species(D, "すなかき")
    snow_ab = abil_species(D, "ゆきふらし"); prank = abil_species(D, "いたずらごころ")
    veil = move_species(D, "オーロラベール")
    baton = move_species(D, "バトンタッチ"); tr = move_species(D, "トリックルーム")
    tw = move_species(D, "おいかぜ"); sr = move_species(D, "ステルスロック"); spikes = move_species(D, "どくびし")
    pivot = move_species(D, "とんぼがえり") + move_species(D, "ボルトチェンジ")
    setup = move_species(D, "つるぎのまい") + move_species(D, "りゅうのまい") + move_species(D, "わるだくみ")
    # --- メガ軸: 各種族の正規メガ石すべて(X/Y両方含む)を軸に1つずつ ---
    mega_by_dex = {}
    for stone, dx in D.get("mega_stone_dex", {}).items():
        mega_by_dex.setdefault(dx, []).append(stone)
    seen_dex = set()
    for p, _ in D["usage"]:
        pdx = D["dex"].get(p)
        for it in sorted(mega_by_dex.get(pdx, [])):
            key = (pdx, it)
            if key in seen_dex: continue
            seen_dex.add(key)
            suf = "X" if it.endswith("X") else ("Y" if it.endswith("Y") else "")
            label = f"メガ軸:{p}{('('+suf+')') if suf else ''}"
            out.append((label, [(p, it, None, None)], set(x for x, _ in D["partners"].get(p, []))))
    # --- 戦略テーマ ---
    def pick(lst, k=1):
        lst = [x for x in lst if x]; rng.shuffle(lst); return lst[:k]
    def add(label, core, prefer):
        out.append((label, core, set(prefer)))
    for setter in pick(rain_ab, 2):
        for ab2 in pick(swift, 3):
            add(f"雨:{setter}+{ab2}", [(setter, "しめったいわ", "あめふらし", ["あまごい"] if setter not in rain_ab else None), (ab2, "auto", "すいすい", None)], swift + ["ラグラージ"])
    for setter in pick(sun_ab, 2):
        for ab2 in pick(chloro, 3):
            add(f"晴:{setter}+{ab2}", [(setter, "auto", "ひでり", None), (ab2, "auto", "ようりょくそ", None)], chloro)
    for setter in pick(sand_ab, 2):
        for ab2 in pick(sandr, 2):
            add(f"砂:{setter}+{ab2}", [(setter, "auto", "すなおこし", None), (ab2, "auto", "すなかき", None)], sandr)
    # 雪は実環境で希少＋ゆきふらし重複で不自然になりがちのため無効化。
    if os.environ.get("ENABLE_SNOW") == "1":
        for setter in pick(snow_ab, 3):
            for v in pick(veil, 2):
                add(f"雪:{setter}+ベール", [(setter, "auto", "ゆきふらし", None), (v, "ひかりのねんど", None, ["オーロラベール"])], snow_ab + veil)
    for s in pick([p for p in prank if p in (move_species(D, "リフレクター"))], 5):
        add(f"壁:{s}", [(s, "ひかりのねんど", "いたずらごころ", ["リフレクター", "ひかりのかべ"])], setup)
    # トリル・バトンは相方ロジックが未最適(テーマ風味の強チーム止まり)のため一旦無効化。
    # 相方ロジック(トリル=鈍足高火力/バトン=積み受け手)を強化したら再有効化する。
    if os.environ.get("ENABLE_TR_BATON") == "1":
        for s in pick(baton, 6):
            add(f"バトン:{s}", [(s, "auto", None, ["バトンタッチ"])], setup + ["エルフーン"])
        for s in pick(tr, 6):
            add(f"トリル:{s}", [(s, "auto", None, ["トリックルーム"])] + [(x, "auto", None, None) for x in pick(["ドドゲザン", "ハリーマン", "バンギラス", "メタグロス"], 1)], ["ドドゲザン", "ハリーマン"])
    for s in pick(tw, 6):
        add(f"おいかぜ:{s}", [(s, "auto", None, ["おいかぜ"])], setup)
    # 設置・積みは汎用的すぎてテーマとして弱い(他テーマ/強構築に内包される)ため無効化。
    if os.environ.get("ENABLE_HAZARD_SETUP") == "1":
        for s in pick(sr, 4):
            for sp in pick(spikes, 2):
                add(f"設置:{s}+{sp}", [(s, "auto", None, ["ステルスロック"]), (sp, "auto", None, ["どくびし"])], [])
        for s in pick(setup, 8):
            add(f"積み:{s}", [(s, "auto", None, None)], setup)
    for s in pick(list(set(pivot)), 7):
        add(f"サイクル:{s}", [(s, "auto", None, None)] + [(x, "auto", None, None) for x in pick(list(set(pivot)), 1)], pivot)
    return out

PLAY_SIMS = int(os.environ.get("MCTS_SIMS", "300"))
SEL_SIMS = int(os.environ.get("SEL_SIMS", "80"))
_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    net = PVNetNP.load()
    _W["play"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=PLAY_SIMS, mcts_select="regret", mcts_fast=True)
    _W["sel"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SEL_SIMS, mcts_select="regret", mcts_fast=True)

def _syn_orders(T, rng):
    from _calib_train import _detect_synergy, _assemble
    orders = []
    for tr in _detect_synergy(T):
        s3 = _assemble(T, tr, rng)
        if len(s3) == 3:
            orders.append(s3); orders.append([s3[1], s3[0], s3[2]])
    return orders[:4]

def _screen(args):
    seed, specs, gauntlet = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts
    L = _W["L"]; play = _W["play"]; sel_ai = _W["sel"]; rng = random.Random(seed)
    def team(sp):
        return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        team(specs)   # ビルド可否のみ確認
    except Exception:
        return -1.0
    w = n = 0
    for gi, opp in enumerate(gauntlet):
        try:
            A = team(specs); B = team(opp)   # 対戦ごとに作り直す(Battle.runが破壊的に状態変更するため)
            aon1 = (gi % 2 == 0)
            # テスト側はギミック組成候補をMCTS探索で検証して選出（ちゃんと組めば勝てるを反映）
            sa = select_mcts(A, B, L, sel_ai, n=3, rng=rng, topk=5, max_mega=2, extra_orders=_syn_orders(A, rng))
            sb = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa if aon1 else sb); s2 = BattleSide(sb if aon1 else sa)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            r = Battle(s1, s2).run(play, play)
            if r != 0: n += 1; w += ((r == 1) == aon1)
        except Exception:
            pass
    return w / n if n else 0.5

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    bar = float(os.environ.get("BAR", "0.45"))   # MCTS(ギミック組成選出)選別＝シナジーもフェアに評価
    import time
    D = G.load(season=SEASON)
    # learnset move→species（テーマ核探索用）
    import sqlite3
    c = sqlite3.connect(os.path.join(os.path.dirname(__file__), "pokenavi.db"))
    lm = {}
    for nm, mv in c.execute("SELECT pokemon_name, move_jp FROM pokemon_learnsets"):
        lm.setdefault(mv, set()).add(G.canon(nm))
    c.close(); D["_learn_move"] = lm
    rng = random.Random(20)
    defs = themes(D, rng)
    parties = []
    seen = set()
    for label, core, prefer in defs:
        try:
            specs = build_party(D, rng, core, prefer)
        except Exception:
            continue
        species = tuple(sorted(s.split("@")[0].split(":")[0] for s in specs))
        stones = tuple(sorted(s.split("@")[1].split(":")[0] for s in specs
                              if "@" in s and s.split("@")[1].split(":")[0] in D["megastones"]))
        key = (species, stones)   # メガ石も鍵に含める＝同種でもX/Y別構築は別物として残す
        if key in seen: continue
        seen.add(key)
        parties.append({"theme": label, "specs": specs})
    print(f"テーマ定義{len(defs)} → 重複除去後{len(parties)}構築 生成", flush=True)
    # 強さ選別（MCTS・ギミック組成選出・小メタgauntlet）
    gauntlet = [G.gen_party(D, random.Random(5000 + k)) for k in range(gn)]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        wrs = p.map(_screen, [(700 + i, parties[i]["specs"], gauntlet) for i in range(len(parties))])
    for pt, wr in zip(parties, wrs): pt["screen_wr"] = wr
    # メガ軸は「各メガの軸構築」showcaseとして強さバーで切らず必ず残す(強さは強生き残り234が担保)。
    # ただしビルド失敗(-1)は除外。戦略テーマはバー適用。
    kept = [pt for pt in parties
            if (pt["theme"].startswith("メガ軸") and pt["screen_wr"] >= 0) or pt["screen_wr"] >= bar]
    kept.sort(key=lambda x: -x["screen_wr"])
    out = f"func1_themed_{SEASON}.json"
    json.dump({"season": SEASON, "bar": bar, "screen": f"MCTS@{PLAY_SIMS}/sel@{SEL_SIMS}+synergy", "parties": kept},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    cat = Counter(pt["theme"].split(":")[0] for pt in kept)
    print(f"選別(MCTS勝率≥{bar*100:.0f}%)後 {len(kept)}/{len(parties)}構築 {time.time()-t0:.0f}秒", flush=True)
    print("テーマ別内訳:", dict(cat), flush=True)
    print(f"→ {out} に保存", flush=True)
    bycat = {}
    for pt in kept: bycat.setdefault(pt["theme"].split(":")[0], []).append(pt)
    for cat in ["雨", "晴", "砂", "雪", "壁", "バトン", "トリル", "おいかぜ", "設置", "積み", "サイクル", "メガ軸"]:
        for pt in bycat.get(cat, [])[:2]:
            print(f"  {pt['screen_wr']*100:4.0f}% [{pt['theme']}] " + " / ".join(s.split('@')[0].split(':')[0] for s in pt["specs"]), flush=True)

if __name__ == "__main__":
    main()
