"""使用率シグナルで死に遺伝子を狙い撃ちする共進化。
各構築をガントレット(サンプル対戦)で評価しつつ「選出率/技使用/メガ実行」を測定し、
死にメンバー・死に技・メガ機会損失を狙って変異→同一相手で再評価し勝率が落ちなければ採用(山登り)。
軸固定なし(テーマ消滅可)。高速化のためNetGreedyで対戦。最終検証は別途MCTS総当たりで行う。
"""
import os, sys, json, random, time, re
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G
import _coevo as C

SEASON = "M-3"
POOL_FILE = "func1_themed_M-3.json"
OUT_FILE = "func1_themed_M-3.json"           # 進化後を同ファイルへ上書き（総当たり再実行が読む）
GENS = int(os.environ.get("GENS", "6"))
OPP_N = int(os.environ.get("OPP_N", "24"))   # 1構築あたりの評価対戦数
NPROC = int(os.environ.get("NPROC", "12"))
SETUP = {"つるぎのまい","りゅうのまい","わるだくみ","ちょうのまい","めいそう","てっぺき","からをやぶる",
         "こうそくいどう","ロックカット","ビルドアップ","コスモパワー","とぐろをまく","アシッドボム"}
CHOICE = {"こだわりスカーフ","こだわりハチマキ","こだわりメガネ"}
PIVOT_TRICK = {"とんぼがえり","ボルトチェンジ","クイックターン","トリック","すりかえ"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["NG"] = NetGreedyAI

def _eval(args):
    """subject を opp_specs 各1戦。勝ち数・選出回数・技使用・メガ実行を返す(captureはbaseのみ)。"""
    sub_specs, opp_specs_list, seed, capture = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; net = _W["net"]; NG = _W["NG"]; rng = random.Random(seed)
    _ng = NG(net)
    def AI(my, opp, f): return certain_ko_override(_ng(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    names = [s.split("@")[0].split(":")[0] for s in sub_specs]
    sel = {nm: 0 for nm in names}; muse = {}; mega = 0; wins = 0; n = 0
    for opp in opp_specs_list:
        try:
            PA = team(sub_specs); PB = team(opp)
            sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            b = Battle(s1, s2); w = b.run(AI, AI); n += 1
            if w == 1: wins += 1
            if not capture: continue
            sanames = [p.name for p in sa]
            for nm in sanames:
                if nm in sel: sel[nm] += 1
            if any(getattr(p, "mega_evolved", False) for p in sa): mega += 1
            for l in b.logs:
                for nm in sanames:
                    key = nm + " の "
                    if key in l:
                        seg = l.split(key, 1)[1]
                        muse[nm] = muse.get(nm, set()); muse[nm].add(seg.split()[0] if seg else "")
        except Exception:
            n += 1
    muse = {k: list(v) for k, v in muse.items()}
    return {"wins": wins, "n": n, "sel": sel, "muse": muse, "mega": mega}

def mega_usage_rate(D, species):
    d = D["items"].get(species, {})
    tot = sum(d.values()) or 1.0
    return sum(v for k, v in d.items() if k in D["megastones"]) / tot

def species_stone(D, species):
    dex = D.get("dex", {}).get(species)
    for st, sdex in D.get("mega_stone_dex", {}).items():
        if sdex == dex and st in D["items"].get(species, {}): return st
    return None

def _coherent_mon(D, m, weather, rng):
    mv, nat, ev = G.coherent_set(D, m["name"], m["item"], m["moves"], m["nature"], m["ev"], weather=weather)
    m["moves"] = mv; m["nature"] = nat; m["ev"] = ev; return m

def variants(D, specs, stat, rng, freq=None, npop=1):
    """gene統計から狙い撃ち変異候補を最大3つ作る。freq=母集団の種別出現数（多様性保護用）。"""
    freq = freq or {}
    cap = float(os.environ.get("FREQ_CAP", "0.40")) * npop   # この数を超える種＝過密
    over = lambda nm: freq.get(nm, 0) > cap
    mons = [C.parse_my(s) for s in specs]
    names = [m["name"] for m in mons]
    weather = set()
    for m in mons:
        for a in [m["ability"]] + (m["moves"] or []):
            if a in G._WSET: weather.add(G._WSET[a])
    sel = stat["sel"]; battles = max(1, stat["n"]); muse = stat["muse"]
    srate = {nm: sel.get(nm, 0) / battles for nm in names}
    out = []
    only_mega = os.environ.get("ONLY_MEGA") == "1"
    # V1: 置換候補＝①低選出(<0.30) ②高メガ依存(>=85%)で石なし(ミスキャスト) ③過密種(多様性のため入替提案)
    #   非メガでも強い種/載せ替え不可な核は、置換すると勝率が落ちるので山登りが棄却して残す
    repl_cands = [i for i in range(6) if srate.get(names[i], 0) < 0.30
                  or (mega_usage_rate(D, names[i]) >= 0.85 and mons[i]["item"] not in D["megastones"])
                  or over(names[i])]
    if not only_mega and repl_cands:
        # 過密種を優先的に外す（同点なら低選出）
        worst = min(repl_cands, key=lambda i: (not over(names[i]), srate.get(names[i], 0)))
        keep_top = [names[i] for i in range(6) if i != worst and srate.get(names[i], 0) >= 0.5]
        cw = {}
        for kt in keep_top:
            for pt, rk in D["partners"].get(kt, []): cw[pt] = cw.get(pt, 0) + 1.0 / rk
        for p, w in {p: 1.0 / rk for p, rk in D["usage"]}.items(): cw[p] = cw.get(p, 0) + 0.15 * w
        dexset = {D["dex"].get(n, n) for i, n in enumerate(names) if i != worst}
        # 置換先：非メガでも機能(メガ率<85%)・過密種は除外・低頻度ほど優先（多様性）
        cw = {p: w * (1.0 - min(1.0, freq.get(p, 0) / max(1.0, cap)))
              for p, w in cw.items() if D["dex"].get(p, p) not in dexset and p not in names
              and mega_usage_rate(D, p) < 0.85 and not over(p)}
        ns = G._wchoice(cw, rng)
        if ns:
            nm = _coherent_mon(D, C._gen_mon(ns, rng), weather, rng)
            v = [dict(x) for x in mons]; v[worst] = nm
            out.append(("ミスキャスト置換:" + names[worst] + "→" + ns, [C.to_spec(x) for x in C.repair(v, rng)]))
    # V2: メガ石の最適配置。メガ可能種(石が使用率に存在)のうち、選出率が高い個体に石を載せる。
    # 石数(≤2)は維持しつつ、低選出の石持ち→高選出の石無しへ載せ替え＝選出されるのにメガできない損失を解消。
    holders = [i for i in range(6) if mons[i]["item"] in D["megastones"]]
    capable = [i for i in range(6) if species_stone(D, names[i]) and mega_usage_rate(D, names[i]) >= 0.5]
    if capable:
        nstone = max(1, len(holders))               # 最低1メガは維持
        desired = sorted(capable, key=lambda i: srate.get(names[i], 0), reverse=True)[:nstone]
        cur = set(holders); des = set(desired)
        promote = [i for i in des - cur if srate.get(names[i], 0) >= 0.30]
        demote = sorted(cur - des, key=lambda i: srate.get(names[i], 0))   # 低選出から外す
        if promote and (not holders or demote or len(holders) < 2):
            v = [dict(x) for x in mons]
            used = {v[k]["item"] for k in range(6) if v[k]["item"] and v[k]["item"] not in D["megastones"]}
            for i in demote[:len(promote)]:          # 載せ替え分だけ降格
                v[i] = dict(v[i]); v[i]["item"] = G.fallback_item(D, names[i], used); used.add(v[i]["item"])
                v[i] = _coherent_mon(D, v[i], weather, rng)
            for i in promote:
                st = species_stone(D, names[i]); v[i] = dict(v[i]); v[i]["item"] = st
                v[i] = _coherent_mon(D, v[i], weather, rng)
            tag = "メガ石再配置→" + "/".join(names[i] for i in promote)
            out.append((tag, [C.to_spec(x) for x in C.repair(v, rng)]))
    # V3: 死に技修正（攻撃技の未使用 / こだわり下の積み・変化技）
    mcat = D["move_cat"]
    v = [dict(x) for x in mons]; changed = False
    for i, m in enumerate(mons):
        if only_mega: break
        if srate.get(names[i], 0) < 0.30: continue
        used = set(muse.get(names[i], []))
        choice = m["item"] in CHOICE and not (set(m["moves"]) & {"トリック", "すりかえ"})
        drop = []
        for mv in m["moves"]:
            if not mv: continue
            # こだわり下の積み・変化技は使用有無に関係なく構造的に死に＝必ず落とす
            if choice and (mv in SETUP or (mcat.get(mv) == "status" and mv not in PIVOT_TRICK)):
                drop.append(mv); continue
            if mv in used: continue
            if mcat.get(mv) in ("physical", "special") and mv not in G._ROLE_ATK:   # 未使用の攻撃技
                drop.append(mv)
        if drop:
            keep = [mv for mv in m["moves"] if mv not in drop]
            want = "physical" if G.species_orient(D, names[i], m["item"]) == "phys" else "special"
            have_t = {D["move_type"].get(x) for x in keep if mcat.get(x) in ("physical", "special")}
            for cand in D["learn_atk"].get((names[i], want), []):
                if len(keep) >= 4: break
                if cand in keep or cand in m["moves"]: continue
                if D["move_type"].get(cand) in have_t: continue
                keep.append(cand); have_t.add(D["move_type"].get(cand))
            while len(keep) < 4:                       # 足りなければ使用率次点で埋める
                nxt = next((u for u in sorted(D["moves"].get(names[i], {}), key=D["moves"][names[i]].get, reverse=True)
                            if u not in keep), None)
                if not nxt: break
                keep.append(nxt)
            v[i] = dict(v[i]); v[i]["moves"] = keep[:4]; changed = True
    if changed:
        out.append(("死に技修正", [C.to_spec(x) for x in C.repair(v, rng)]))
    return out

def main():
    global D
    D = G.load(season=SEASON); C.D = D
    pool = [list(p["specs"]) for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"]]
    themes = [p.get("theme", "") for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"]]
    npop = len(pool); rng = random.Random(0)
    print(f"母集団{npop} / {GENS}世代 / 評価{OPP_N}戦 / NetGreedy ×{NPROC}", flush=True)
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as pool_proc:
        for g in range(GENS):
            t0 = time.time()
            samples = [random.sample([k for k in range(npop) if k != i], min(OPP_N, npop - 1)) for i in range(npop)]
            base_args = [(pool[i], [pool[k] for k in samples[i]], 100 + g * 99991 + i, True) for i in range(npop)]
            base = pool_proc.map(_eval, base_args)
            base_wr = [r["wins"] / max(1, r["n"]) for r in base]
            from collections import Counter                  # 母集団の種別出現数（多様性保護）
            freq = Counter(s.split("@")[0].split(":")[0] for sp in pool for s in sp)
            # 各構築の変異候補を作り、同一サンプルで評価
            cand_jobs = []; cand_meta = []
            for i in range(npop):
                for tag, vspecs in variants(D, pool[i], base[i], rng, freq, npop):
                    cand_meta.append((i, tag, vspecs))
                    cand_jobs.append((vspecs, [pool[k] for k in samples[i]], 100 + g * 99991 + i, False))
            cres = pool_proc.map(_eval, cand_jobs) if cand_jobs else []
            best = {}
            for (i, tag, vspecs), r in zip(cand_meta, cres):
                wr = r["wins"] / max(1, r["n"])
                if wr >= base_wr[i] and (i not in best or wr > best[i][0]):
                    best[i] = (wr, tag, vspecs)
            adopted = 0
            for i, (wr, tag, vspecs) in best.items():
                if wr >= base_wr[i]:
                    pool[i] = vspecs; adopted += 1
            mean = sum(base_wr) / npop
            print(f"[gen{g}] baseWR平均={mean*100:.1f}% 変異候補={len(cand_jobs)} 採用={adopted} {time.time()-t0:.0f}s", flush=True)
    # 保存（themeラベルは維持、specsのみ更新）
    obj = json.load(open(POOL_FILE, encoding="utf-8"))
    for i, p in enumerate(obj["parties"]): p["specs"] = pool[i]
    obj["evolved"] = True
    json.dump(obj, open(OUT_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"進化後母集団を {OUT_FILE} に保存", flush=True)

if __name__ == "__main__":
    main()
