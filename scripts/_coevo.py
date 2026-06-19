"""共進化プロトタイプ（M-3共進化の試作 Step2-4）。
生成器(_pop_gen)で初期集団→自己対戦でElo付与→QDアーカイブ(アーキタイプ別保持で多様性維持)
→進化(突然変異/交叉/新規注入で下位置換)を繰り返し、強く多様なパーティ集団を発見できるか検証。
評価器(対戦AI)はNetGreedyAIで固定（パーティ構築エンジンの有効性を切り分け）。
"""
import sys, os, random, math, time, json
from collections import defaultdict
from multiprocessing import Pool
import _pop_gen as G

D = None  # 各プロセスで load

# ---- spec(自分の形式) ⇄ 構造化 mon ----
def parse_my(spec):
    name = spec; item = None
    if "@" in spec:
        name, rest = spec.split("@", 1); parts = rest.split(":"); item = parts[0] or None; fields = parts[1:]
    else:
        parts = spec.split(":"); name = parts[0]; fields = parts[1:]
    nat = fields[0] if len(fields) > 0 and fields[0] else None
    mv = fields[1].split("|") if len(fields) > 1 and fields[1] else []
    ev = None
    if len(fields) > 2 and fields[2]:
        try: ev = tuple(int(x) for x in fields[2].split("/"))
        except ValueError: ev = None
    ab = fields[3] if len(fields) > 3 and fields[3] else None
    return {"name": name, "item": item, "nature": nat, "moves": mv, "ev": ev, "ability": ab}

def to_spec(m):
    return G._spec(m["name"], m["item"], m["nature"], m["moves"], m["ev"], m["ability"])

def _gen_mon(p, rng):
    item = G._wchoice(D["items"].get(p, {}), rng)
    nat = G._wchoice(D["natures"].get(p, {}), rng)
    ab = G._wchoice(D["abil"].get(p, {}), rng)
    mv = G._wsample_dict(D["moves"].get(p, {}), 4, rng)
    ep = D["evs"].get(p, []); ev = None
    if ep:
        i = G._wchoice({i: w for i, (sp, w) in enumerate(ep)}, rng)
        if i is not None: ev = ep[i][0]
    return {"name": G.canon(p), "item": item, "nature": nat, "moves": mv, "ev": ev, "ability": ab}

def _fresh_species(rng, exclude):
    uw = {p: 1.0 / rk for p, rk in D["usage"] if p not in exclude}
    return G._wchoice(uw, rng)

def repair(mons, rng):
    # 1) 種族重複除去（図鑑番号ベース＝リージョン違い同種も同居不可）
    dexmap = D.get("dex", {})
    def dx(nm): return dexmap.get(nm, nm)
    seen = set()
    for m in mons:
        if dx(m["name"]) in seen:
            ns = _fresh_species(rng, seen | {x["name"] for x in mons})
            if ns: m.clear(); m.update(_gen_mon(ns, rng))
        seen.add(dx(m["name"]))
    # 2) 持ち物重複除去
    used = set()
    for m in mons:
        if m["item"] and m["item"] in used:
            alt = {k: v for k, v in D["items"].get(m["name"], {}).items() if k not in used}
            m["item"] = G._wchoice(alt, rng) if alt else None
        if m["item"]: used.add(m["item"])
    # 3) メガ 1〜2
    megas = [i for i, m in enumerate(mons) if m["item"] in D["megastones"]]
    while len(megas) > 2:
        i = megas.pop(); m = mons[i]
        if m["item"]: used.discard(m["item"])
        alt = {k: v for k, v in D["items"].get(m["name"], {}).items() if k not in used and k not in D["megastones"]}
        m["item"] = G._wchoice(alt, rng) if alt else None
        if m["item"]: used.add(m["item"])
    if not megas:
        for m in mons:
            stones = {k: D["items"][m["name"]][k] for k in D["items"].get(m["name"], {})
                      if k in D["megastones"] and k not in used}
            if stones:
                if m["item"]: used.discard(m["item"])
                m["item"] = G._wchoice(stones, rng); used.add(m["item"]); break
    return mons

def mutate(specs, rng):
    mons = [parse_my(s) for s in specs]
    if rng.random() < 0.5:                       # 種族入替（探索の主軸）
        i = rng.randrange(6); ns = _fresh_species(rng, {m["name"] for m in mons})
        if ns: mons[i] = _gen_mon(ns, rng)
    else:                                         # 持ち物/技/EVの微変異
        i = rng.randrange(6); mons[i] = _gen_mon(mons[i]["name"], rng)
    return [to_spec(m) for m in repair(mons, rng)]

def crossover(s1, s2, rng):
    m1 = [parse_my(s) for s in s1]; m2 = [parse_my(s) for s in s2]
    idx = set(rng.sample(range(6), 3))
    child = [dict(m1[i]) if i in idx else dict(m2[i]) for i in range(6)]
    return [to_spec(m) for m in repair(child, rng)]

# ---- 対戦（ワーカー） ----
_W = {}
def _winit(season):
    global D
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    D = G.load(season=season)
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["NG"] = NetGreedyAI

def _play_pairs(args):
    seed, pairs, pop_specs, season = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; net = _W["net"]; NG = _W["NG"]; rng = random.Random(seed)
    def team(specs): return [build_from_spec(parse_pokemon_spec(s), L, season=season, randomize=False) for s in specs]
    out = []
    for (i, j) in pairs:
        try:
            PA = team(pop_specs[i]); PB = team(pop_specs[j])
            sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            w = Battle(s1, s2).run(NG(net), NG(net))
        except Exception:
            w = 0
        out.append((i, j, w))
    return out

def _elo_update(elo, i, j, w, K=24):
    ra, rb = elo[i], elo[j]
    ea = 1.0 / (1.0 + 10 ** ((rb - ra) / 400))
    sa = 0.5 if w == 0 else (1.0 if w == 1 else 0.0)
    elo[i] = ra + K * (sa - ea); elo[j] = rb + K * ((1 - sa) - (1 - ea))

def niche(specs):
    txt = " ".join(specs)
    mons = [parse_my(s) for s in specs]
    rain = ("あまごい" in txt) or ("あめふらし" in txt)
    baton = "バトンタッチ" in txt
    ditto = any(m["name"].startswith("メタモン") for m in mons)
    hazard = ("ステルスロック" in txt) or ("まきびし" in txt)
    nmega = sum(1 for m in mons if m["item"] in D["megastones"])
    return (rain, baton, ditto, hazard, min(nmega, 2))

def run(pop_size=64, gens=10, games_per=30, workers=12, season="M-2", seed=0, log=print):
    global D
    D = G.load(season=season)
    rng = random.Random(seed)
    pop = [[s for s in G.gen_party(D, rng)] for _ in range(pop_size)]
    gen0 = [list(p) for p in pop]                       # 検証用に初期集団を保存
    elo = [1500.0] * pop_size
    pool = Pool(workers, initializer=_winit, initargs=(season,))
    hist = []
    for g in range(gens):
        t0 = time.time()
        pairs = []
        for i in range(pop_size):
            for _ in range(games_per):
                j = rng.randrange(pop_size)
                if j != i: pairs.append((i, j))
        chunks = [pairs[k::workers] for k in range(workers)]
        args = [(seed + g * 1000 + k, ch, pop, season) for k, ch in enumerate(chunks)]
        for res in pool.map(_play_pairs, args):
            for i, j, w in res: _elo_update(elo, i, j, w)
        order = sorted(range(pop_size), key=lambda i: -elo[i])
        niches = defaultdict(list)
        for i in order: niches[niche(pop[i])].append(i)
        # QDエリート: 各ニッチ上位1 + 全体上位で survivors を pop_size*0.6 に
        survivors = []
        for nb, idxs in niches.items(): survivors.append(idxs[0])
        for i in order:
            if len(survivors) >= int(pop_size * 0.6): break
            if i not in survivors: survivors.append(i)
        surv_set = set(survivors); mean_elo = sum(elo[i] for i in survivors) / len(survivors)
        hist.append({"gen": g, "max_elo": max(elo), "mean_surv": mean_elo,
                     "niches": len(niches), "sec": round(time.time() - t0, 1)})
        log(f"[gen{g}] maxElo={max(elo):.0f} survMean={mean_elo:.0f} ニッチ数={len(niches)} "
            f"対戦{len(pairs)} {hist[-1]['sec']:.0f}秒")
        if g == gens - 1: break
        # 次世代: survivors保持 + 残りを子で置換（突然変異/交叉/新規）
        newpop = [list(pop[i]) for i in survivors]; newelo = [elo[i] for i in survivors]
        topw = {i: max(1.0, elo[i] - 1400) for i in survivors}
        while len(newpop) < pop_size:
            r = rng.random()
            if r < 0.5:
                p = G._wchoice(topw, rng); child = mutate(pop[p], rng)
            elif r < 0.85:
                a = G._wchoice(topw, rng); b = G._wchoice(topw, rng); child = crossover(pop[a], pop[b], rng)
            else:
                child = G.gen_party(D, rng)
            newpop.append(child); newelo.append(mean_elo)
        pop = newpop; elo = newelo
    # ---- 検証: 最終集団 vs 初期集団 のクロス対戦 ----
    log("最終集団 vs 初期集団 クロス対戦で強化を検証中...")
    cross = [(a, b) for a in range(pop_size) for b in range(pop_size)]
    random.Random(seed).shuffle(cross); cross = cross[:1500]
    combined = pop + gen0  # 0..pop-1=最終, pop..2pop-1=初期
    cpairs = [(a, pop_size + b) for (a, b) in cross]
    chunks = [cpairs[k::workers] for k in range(workers)]
    args = [(seed + 99000 + k, ch, combined, season) for k, ch in enumerate(chunks)]
    fw = fl = fd = 0
    for res in pool.map(_play_pairs, args):
        for i, j, w in res:
            if w == 0: fd += 1
            elif w == 1: fw += 1
            else: fl += 1
    pool.close(); pool.join()
    dec = fw + fl; wr = fw / dec if dec else 0.0
    z = (fw - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0.0
    from math import erfc; pval = erfc(abs(z) / math.sqrt(2)) if dec else 1.0
    log(f"\n=== 検証: 最終集団 vs 初期集団 {len(cpairs)}戦 ===")
    log(f"最終集団: {fw}勝 {fl}敗 {fd}分 → 勝率{wr*100:.1f}%  p={pval:.4f}  {'有意に強化(p<0.05)' if pval<0.05 and wr>0.5 else ('有意に弱化' if pval<0.05 else '有意差なし')}")
    # 強パーティ Top3 を表示
    order = sorted(range(pop_size), key=lambda i: -elo[i])
    log("\n--- 発見された強パーティ Top3（Elo順）---")
    for r in order[:3]:
        names = [parse_my(s)["name"] for s in pop[r]]
        log(f"  Elo{elo[r]:.0f}: {' / '.join(names)}")
    log(f"\n最終ニッチ多様性: {len(set(niche(p) for p in pop))} 種類")
    out = f"/tmp/coevo_parties_{season}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"season": season, "winrate_vs_init": wr, "pval": pval,
                   "parties": [{"elo": elo[i], "specs": pop[i],
                                "names": [parse_my(s)["name"] for s in pop[i]]}
                               for i in order]}, f, ensure_ascii=False, indent=1)
    log(f"最終集団を {out} に保存（Elo順）")
    return hist

if __name__ == "__main__":
    ps = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    gp = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    season = sys.argv[4] if len(sys.argv) > 4 else os.environ.get("COEVO_SEASON", "M-2")
    run(pop_size=ps, gens=gn, games_per=gp, season=season)
