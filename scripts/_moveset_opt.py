"""技構成オプティマイザ: 合法技プールから候補を絞り、4技の組合せをMCTS実勝率で評価して最良を学習。
物理/特殊を強制せず候補に混ぜる(=メガライチュウXの混合型 ボルテッカー+きあいだま+くさむすび 等を発見可能)。
使用率に型が無いoff-usage軸(メガX系)の「勝てる技構成」を、ヒューリスティックでなく実戦で最適化する。
対象ポケを与えたチーム(POOL_FILEのテーマ)内で、その個体の技だけ最適化し、メタgauntletと対戦評価。
"""
import sys, os, random, math, json, itertools, sqlite3
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G

SEASON = os.environ.get("COEVO_SEASON", "M-3")
SIMS = int(os.environ.get("MCTS_SIMS", "250"))
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")
_W = {}

UTIL = ["ねこだまし", "でんこうせっか", "しんそく", "バレットパンチ", "アクアジェット", "つるぎのまい", "りゅうのまい",
        "わるだくみ", "ちょうのまい", "アンコール", "ボルトチェンジ", "とんぼがえり", "クイックターン",
        "みがわり", "まもる", "でんじは", "おにび", "ステルスロック", "オーロラベール", "リフレクター",
        "ニトロチャージ", "めいそう", "てっぺき", "リフレッシュ"]
# 攻撃カテゴリだが主目的が攻撃でない技(交代/素早さ等)＝同タイプ重複判定から除外
_ROLE_ATK = {"ボルトチェンジ", "とんぼがえり", "クイックターン", "ニトロチャージ", "でんこうせっか",
             "しんそく", "バレットパンチ", "アクアジェット", "ねこだまし"}
_TRAP = {"ギガインパクト", "はかいこうせん", "ブラストバーン", "ハイドロカノン", "ハードプラント",
         "すてみタックル", "とっしん", "メガトンキック", "メガトンパンチ", "ばくれつパンチ",
         "ロケットずつき", "はなびらのまい", "ぶんまわす"}
# 常時2ターン溜め(天候でも即時化しない・1v1で隙が大きい)＝候補から常時除外
_ALWAYS_CHARGE = {"あなをほる", "そらをとぶ", "ダイビング", "ゴッドバード", "とびはねる", "メテオビーム", "ゴーストダイブ"}

def candidate_moves(species, eff_types, orient, k_atk=6, k_util=2, weather=None):
    weather = weather or set()
    c = sqlite3.connect(DB)
    rows = c.execute("""SELECT m.name_jp,m.type,m.category,m.power,m.accuracy FROM pokemon_learnsets ls
        JOIN move_master m ON m.name_jp=ls.move_jp WHERE ls.pokemon_name=?""", (species,)).fetchall()
    c.close()
    atk = []; util = []
    seen_type = {}
    for nm, tp, cat, pw, ac in rows:
        if nm in UTIL: util.append((nm, UTIL.index(nm)))
        if cat not in ("physical", "special") or nm in _TRAP or nm in _ROLE_ATK or nm in UTIL: continue
        if nm in _ALWAYS_CHARGE: continue                                          # 常時溜め技は除外
        if nm in ("ソーラービーム", "ソーラーブレード") and "sun" not in weather: continue   # 晴れ無しの溜めソーラーは除外
        if nm == "エレクトロビーム" and "rain" not in weather: continue              # 雨無しの溜めエレキは除外
        if ac is not None and ac < 60: continue          # 命中50の博打技(でんじほう等)は除外、70は許容
        p = pw if pw is not None else 70                  # 変動威力(くさむすび等)は公称70で候補化
        stab = 1.5 if tp in eff_types else 1.0
        om = 1.3 if ((cat == "physical" and orient == "phys") or (cat == "special" and orient == "spec")) else 1.0
        atk.append((p * stab * om, nm, tp))               # 向き一致(物理メガ→物理技)を優先＝フレアドライブ>オーバーヒート
    atk.sort(reverse=True)
    picks = []                                            # 純攻撃は1タイプ最良のみ＝タイプ多様性を確保
    for eff, nm, tp in atk:
        if tp in seen_type: continue
        picks.append(nm); seen_type[tp] = 1
        if len(picks) >= k_atk: break
    util.sort(key=lambda x: x[1])                         # 役割技(ピボット/先制/変化/素早さ)は別枠で追加
    short = []
    for nm in picks + [n for n, _ in util][:k_util]:
        if nm not in short: short.append(nm)
    return short

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _spec_set_moves(spec, moves):
    name, _, rest = spec.partition(":")  # name@item
    f = rest.split(":")  # nature, moves, ev, ability (rstripped)
    nature = f[0] if len(f) > 0 else ""
    ev = f[2] if len(f) > 2 else ""
    ability = f[3] if len(f) > 3 else ""
    s = name + ":" + nature + ":" + "|".join(moves) + ":" + ev + ":" + ability
    return s.rstrip(":")

def _job(args):
    seed, idx, team_specs, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = 0
    for gi, opp in enumerate(gauntlet):
        for k in range(K):
            T = team(team_specs); O = team(opp)
            core = [T[0]]; rest = T[1:]                 # 対象個体(slot0)を必ず選出に入れる
            fs = select_party(rest, O, L, n=2, temperature=0.3, rng=rng)
            sa = (core + fs)[:3]
            sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
            aon1 = ((gi + k) % 2 == 0)
            s1 = BattleSide(sa if aon1 else sb); s2 = BattleSide(sb if aon1 else sa)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try: r = Battle(s1, s2).run(ai, ai)
            except Exception: r = 0
            if r == 0: continue
            if (r == 1) == aon1: w += 1
            else: l += 1
    return idx, w, l

def main():
    theme = sys.argv[1] if len(sys.argv) > 1 else "メガ軸:ライチュウ(X)"
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    import time
    D = G.load(season=SEASON); rng = random.Random(0)
    pool = json.load(open(f"func1_pool_{SEASON}.json", encoding="utf-8"))["parties"]
    party = next((p for p in pool if p.get("theme") == theme), None)
    if party is None:
        print(f"テーマ {theme} が母集団に無い"); return
    specs = list(party["specs"])
    axis = specs[0]
    species = axis.split("@")[0].split(":")[0]
    item = axis.split("@")[1].split(":")[0] if "@" in axis else None
    orient = G.mega_orient(D, item)
    eff = D.get("mega_by_stone", {}).get(item)
    # メガ後タイプはmega_statsから
    c = sqlite3.connect(DB)
    mt = c.execute("SELECT type1,type2 FROM pokemon_mega_stats WHERE mega_stone=?", (item,)).fetchone()
    c.close()
    eff_types = set(t for t in (mt or ()) if t)
    _WSET = {"あめふらし": "rain", "あまごい": "rain", "ひでり": "sun", "にほんばれ": "sun", "すなおこし": "sand", "ゆきふらし": "snow"}
    weather = set()                                       # チームの天候源(特性/技)
    for s in specs:
        for a in [s.split(":")[-1]] + (s.split(":")[2].split("|") if ":" in s else []):
            if a in _WSET: weather.add(_WSET[a])
    short = candidate_moves(species, eff_types, orient, weather=weather)
    cc = sqlite3.connect(DB)
    mcat = {r[0]: r[1] for r in cc.execute("SELECT name_jp,category FROM move_master")}
    mtype = {r[0]: r[1] for r in cc.execute("SELECT name_jp,type FROM move_master")}
    cc.close()
    # 排除する重複: 純攻撃技の同タイプ重複(オーバーヒート+フレアドライブ等)＋ピボット2枚＋積み2枚。
    # 先制技/交代技/変化技/素早さ技(_ROLE_ATK)や壁は同タイプでも役割が違い共存正当なので除外しない。
    _REDUN = [{"ボルトチェンジ", "とんぼがえり", "クイックターン"},
              {"つるぎのまい", "りゅうのまい", "わるだくみ", "ちょうのまい", "めいそう", "てっぺき"}]
    force = [m for m in os.environ.get("FORCE_MOVES", "").split(",") if m]   # ドメイン固定技(例きあいだま)
    for fm in force:
        if fm not in short: short.append(fm)
    def ok(combo):
        cs = set(combo)
        if any(fm not in cs for fm in force): return False
        if any(len(cs & g) > 1 for g in _REDUN): return False
        tcnt = {}
        for m in combo:
            if mcat.get(m) not in ("physical", "special") or m in _ROLE_ATK: continue
            t = mtype.get(m); tcnt[t] = tcnt.get(t, 0) + 1
        return all(v <= 1 for v in tcnt.values())
    combos = [c for c in itertools.combinations(short, 4) if ok(c)]
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"対象: {species}@{item} (メガ後{'/'.join(eff_types)} 向き={orient}) / 候補技{len(short)}: {short}")
    print(f"組合せ {len(combos)} を vs メタ{gn}×{K}戦 MCTS@{SIMS} で評価\n", flush=True)
    t0 = time.time()
    jobs = []
    for i, combo in enumerate(combos):
        ns = list(specs); ns[0] = _spec_set_moves(axis, list(combo))
        jobs.append((900 + i, i, ns, gauntlet, K))
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    rows = []
    for idx, w, l in res:
        wr = w / (w + l) if w + l else 0
        rows.append((wr, w, l, combos[idx]))
    rows.sort(reverse=True)
    print(f"\n=== {species}@{item} 技構成 最適化結果 (上位) {time.time()-t0:.0f}秒 ===")
    for wr, w, l, combo in rows[:8]:
        print(f"  {wr*100:5.1f}% ({w}-{l})  {' / '.join(combo)}")
    # 最良をファイルに保存(テーマ別・適用用)
    OUT = "/tmp/moveset_opts.json"
    db = {}
    if os.path.exists(OUT):
        db = json.load(open(OUT, encoding="utf-8"))
    db[theme] = {"species": species, "item": item, "moves": list(rows[0][3]), "winrate": rows[0][0]}
    json.dump(db, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"最良を {OUT} に保存", flush=True)

if __name__ == "__main__":
    main()
