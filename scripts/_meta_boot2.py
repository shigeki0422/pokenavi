"""使用率ブートストラップ 全次元版：種族・同居・持ち物・技・特性・性格・EV配分 を一括逆算。
各次元を「合法候補上で均一」から初期化→生成→自己対戦Elo→勝率で全次元の使用率を逆算→反復。
M-2で各分布が収束＆実使用率と一致するか検証（種族ρ/TOP15・他次元はtop一致率）。
固定（逆算しない）：種族値・タイプ・learnset・メガ定義（＝合法性であって使用率でない）。
"""
import sys, os, random, math
from collections import defaultdict
from multiprocessing import Pool
import _pop_gen as G
import _coevo as C

SEASON = "M-2"

def uniform_from(real_dim):
    """real_dim={p:{opt:rate}} or {p:[(opt,rate)]} の候補集合を均一weightで初期化。"""
    out = {}
    for p, d in real_dim.items():
        opts = [o for o, _ in d] if isinstance(d, list) else list(d.keys())
        if opts: out[p] = {o: 1.0 for o in opts}
    return out

def make_D(base, sp_freq, partner_f, item_f, move_f, nat_f, abil_f, ev_f):
    D = dict(base)
    D["usage"] = [(p, i + 1) for i, p in enumerate(sorted(sp_freq, key=lambda p: -sp_freq[p]))]
    D["partners"] = {p: sorted(d.items(), key=lambda kv: -kv[1])
                     for p, d in ((p, {q: w for q, w in pf.items()}) for p, pf in partner_f.items())}
    D["partners"] = {p: [(q, i + 1) for i, (q, _) in enumerate(lst)] for p, lst in D["partners"].items()}
    D["items"] = {p: dict(d) for p, d in item_f.items()}
    D["moves"] = {p: dict(d) for p, d in move_f.items()}
    D["natures"] = {p: dict(d) for p, d in nat_f.items()}
    D["abil"] = {p: dict(d) for p, d in abil_f.items()}
    D["evs"] = {p: sorted(d.items(), key=lambda kv: -kv[1]) for p, d in ev_f.items()}
    return D

def blend_dim(sim, new, alpha, floor_frac=0.1):
    """{p:{opt:w}} を レプリケータ更新(平滑+合法候補にフロア)。simの候補集合を維持。"""
    out = {}
    for p, simd in sim.items():
        nd = new.get(p, {})
        tot = sum(nd.values()) or 1.0
        opts = simd.keys()
        fl = floor_frac / max(1, len(opts))
        merged = {}
        for o in opts:
            nv = (nd.get(o, 0.0) / tot) * (1 - floor_frac) + fl
            merged[o] = alpha * nv + (1 - alpha) * simd[o]
        s = sum(merged.values()) or 1.0
        out[p] = {o: v / s for o, v in merged.items()}
    return out

def top1_match(sim, real):
    """各pでargmaxが実使用率のargmaxと一致する率。"""
    ok = n = 0
    for p, simd in sim.items():
        rd = real.get(p)
        if not rd: continue
        rdd = dict(rd) if not isinstance(rd, list) else {o: w for o, w in rd}
        if not rdd or not simd: continue
        n += 1
        if max(simd, key=simd.get) == max(rdd, key=rdd.get): ok += 1
    return ok / n if n else 0.0

def topk_overlap(sim, real, k=4):
    tot = n = 0.0
    for p, simd in sim.items():
        rd = real.get(p)
        if not rd: continue
        rdd = dict(rd)
        st = set(sorted(simd, key=simd.get, reverse=True)[:k])
        rt = set(sorted(rdd, key=rdd.get, reverse=True)[:k])
        if rt: tot += len(st & rt) / len(rt); n += 1
    return tot / n if n else 0.0

def spearman(x, y):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i]); rk = [0] * len(v)
        for r, i in enumerate(order): rk[i] = r
        return rk
    rx, ry = rank(x), rank(y); n = len(x); mx = sum(rx) / n; my = sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sx = math.sqrt(sum((r - mx) ** 2 for r in rx)); sy = math.sqrt(sum((r - my) ** 2 for r in ry))
    return cov / (sx * sy) if sx and sy else 0.0

def main():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    pool_size = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    games_per = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    alpha = 0.5; workers = 12
    import time
    base = G.load(season=SEASON)
    real_rank = {p: rk for p, rk in base["usage"]}
    species = list(real_rank.keys())
    # 実分布(検証用) — EVはリスト→dict化
    real_ev = {p: {tuple(sp) if isinstance(sp, (list, tuple)) else sp: w for sp, w in lst} for p, lst in base["evs"].items()}
    # 初期: 全次元 均一
    sp_freq = {p: 1.0 / len(species) for p in species}
    item_f = uniform_from(base["items"]); move_f = uniform_from(base["moves"])
    nat_f = uniform_from(base["natures"]); abil_f = uniform_from(base["abil"])
    ev_f = {p: {sp: 1.0 for sp in d} for p, d in real_ev.items()}
    partner_f = {p: {q: 1.0 for q in dict(base["partners"].get(p, {}))} for p in species}
    floor = 0.1 / len(species)
    pool = Pool(workers, initializer=C._winit, initargs=(SEASON,))
    prev = None
    for r in range(rounds):
        t0 = time.time()
        D = make_D(base, sp_freq, partner_f, item_f, move_f, nat_f, abil_f, ev_f)
        parties = [G.gen_party(D, random.Random(r * 1000 + i)) for i in range(pool_size)]
        elo = [1500.0] * pool_size
        rng = random.Random(r * 13 + 1); pairs = []
        for i in range(pool_size):
            for _ in range(games_per):
                j = rng.randrange(pool_size)
                if j != i: pairs.append((i, j))
        chunks = [pairs[k::workers] for k in range(workers)]
        for res in pool.map(C._play_pairs, [(r * 97 + k, ch, parties, SEASON) for k, ch in enumerate(chunks)]):
            for i, j, w in res: C._elo_update(elo, i, j, w)
        # 逆算
        nsp = defaultdict(float); nit = defaultdict(lambda: defaultdict(float))
        nmv = defaultdict(lambda: defaultdict(float)); nna = defaultdict(lambda: defaultdict(float))
        nab = defaultdict(lambda: defaultdict(float)); nev = defaultdict(lambda: defaultdict(float))
        npa = defaultdict(lambda: defaultdict(float))
        for idx, party in enumerate(parties):
            w = max(0.1, elo[idx] - 1400.0)
            mons = [C.parse_my(s) for s in party]
            names = [m["name"] for m in mons]
            for m in mons:
                p = m["name"]; nsp[p] += w
                if m["item"]: nit[p][m["item"]] += w
                if m["nature"]: nna[p][m["nature"]] += w
                if m["ability"]: nab[p][m["ability"]] += w
                if m["ev"]: nev[p][tuple(m["ev"])] += w
                for mv in (m["moves"] or []): nmv[p][mv] += w
            for a in range(len(names)):
                for b in range(len(names)):
                    if a != b: npa[names[a]][names[b]] += w
        # 種族(rank)更新
        tot = sum(nsp.values()) or 1.0
        nf = {p: (nsp.get(p, 0.0) / tot) * 0.9 + floor for p in species}
        s = sum(nf.values()); nf = {p: v / s for p, v in nf.items()}
        sp_freq = {p: alpha * nf[p] + (1 - alpha) * sp_freq[p] for p in species}
        s = sum(sp_freq.values()); sp_freq = {p: v / s for p, v in sp_freq.items()}
        # 各次元更新
        item_f = blend_dim(item_f, nit, alpha); move_f = blend_dim(move_f, nmv, alpha)
        nat_f = blend_dim(nat_f, nna, alpha); abil_f = blend_dim(abil_f, nab, alpha)
        ev_f = blend_dim(ev_f, nev, alpha)
        partner_f = blend_dim(partner_f, npa, alpha)
        # メトリクス
        l1 = sum(abs(sp_freq[p] - prev[p]) for p in species) if prev else float('nan')
        prev = dict(sp_freq)
        sp_rho = spearman([sp_freq[p] for p in species], [-real_rank[p] for p in species])
        m_it = top1_match(item_f, base["items"]); m_na = top1_match(nat_f, base["natures"])
        m_ab = top1_match(abil_f, base["abil"]); m_ev = top1_match(ev_f, real_ev)
        ov_mv = topk_overlap(move_f, base["moves"], 4); ov_pa = topk_overlap(partner_f, {p: dict(base["partners"].get(p, {})) for p in species}, 3)
        print(f"r{r}: 種族ρ={sp_rho:.2f} ΔL1={l1:.3f} | 持物top1={m_it:.2f} 性格top1={m_na:.2f} 特性top1={m_ab:.2f} EVtop1={m_ev:.2f} 技top4重複={ov_mv:.2f} 同居top3重複={ov_pa:.2f} {time.time()-t0:.0f}s", flush=True)
    pool.close(); pool.join()
    sim_top = set(sorted(species, key=lambda p: -sp_freq[p])[:15])
    real_top = set(sorted(species, key=lambda p: real_rank[p])[:15])
    print(f"\n種族TOP15一致: {len(sim_top & real_top)}/15", flush=True)

if __name__ == "__main__":
    main()
