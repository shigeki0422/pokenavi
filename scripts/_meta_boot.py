"""使用率ブートストラップ(自己整合メタ発見)の試作。
フラット初期分布→生成→自己対戦Elo→勝率で使用率を逆算→生成器に戻す、を反復。
M-2で(1)収束(ΔL1減衰)と(2)実M-2使用率との順位相関 を検証する。
収束＆相関が出れば、M-3新ポケ投入(高め初期率・技均一)のコールドスタートに使える。
"""
import sys, os, random, math
from collections import defaultdict
from multiprocessing import Pool
import _pop_gen as G
import _coevo as C

SEASON = "M-2"

def make_D(base, species_freq):
    """シミュレート種族使用率(freq)を rank化して D["usage"] に注入。他(partners/items/moves/mega)はbase。"""
    D = dict(base)
    ranked = sorted(species_freq, key=lambda p: -species_freq[p])
    D["usage"] = [(p, i + 1) for i, p in enumerate(ranked)]
    return D

def spearman(x, y):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i]); rk = [0] * len(v)
        for r, i in enumerate(order): rk[i] = r
        return rk
    rx, ry = rank(x), rank(y); n = len(x)
    mx = sum(rx) / n; my = sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sx = math.sqrt(sum((r - mx) ** 2 for r in rx)); sy = math.sqrt(sum((r - my) ** 2 for r in ry))
    return cov / (sx * sy) if sx and sy else 0.0

def main():
    rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    pool_size = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    games_per = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    alpha = 0.5      # 更新平滑(レプリケータ)
    workers = 12
    import time
    base = G.load(season=SEASON)
    real_rank = {p: rk for p, rk in base["usage"]}
    species = list(real_rank.keys())
    freq = {p: 1.0 / len(species) for p in species}   # フラット初期
    floor = 0.1 / len(species)
    pool = Pool(workers, initializer=C._winit, initargs=(SEASON,))
    prev = None
    for r in range(rounds):
        t0 = time.time()
        D = make_D(base, freq)
        parties = [G.gen_party(D, random.Random(r * 1000 + i)) for i in range(pool_size)]
        elo = [1500.0] * pool_size
        rng = random.Random(r * 13 + 1)
        pairs = []
        for i in range(pool_size):
            for _ in range(games_per):
                j = rng.randrange(pool_size)
                if j != i: pairs.append((i, j))
        chunks = [pairs[k::workers] for k in range(workers)]
        args = [(r * 97 + k, ch, parties, SEASON) for k, ch in enumerate(chunks)]
        for res in pool.map(C._play_pairs, args):
            for i, j, w in res: C._elo_update(elo, i, j, w)
        # 勝率(Elo)重みで種族の限界使用率を逆算
        newf = defaultdict(float)
        for idx, party in enumerate(parties):
            w = max(0.1, elo[idx] - 1400.0)
            for nm in set(C.parse_my(s)["name"] for s in party):
                newf[nm] += w
        tot = sum(newf.values()) or 1.0
        nf = {p: (newf.get(p, 0.0) / tot) * 0.9 + floor for p in species}
        s = sum(nf.values()); nf = {p: v / s for p, v in nf.items()}
        freq = {p: alpha * nf[p] + (1 - alpha) * freq[p] for p in species}
        s = sum(freq.values()); freq = {p: v / s for p, v in freq.items()}
        l1 = sum(abs(freq[p] - prev[p]) for p in species) if prev else float('nan')
        prev = dict(freq)
        sp = spearman([freq[p] for p in species], [-real_rank[p] for p in species])
        top = sorted(species, key=lambda p: -freq[p])[:8]
        print(f"round{r}: ΔL1={l1:.4f} 実使用率との順位相関={sp:.3f} {time.time()-t0:.0f}s | top: {', '.join(top[:6])}", flush=True)
    pool.close(); pool.join()
    # 実使用率TOP15 と シミュTOP15 の重なり
    sim_top = set(sorted(species, key=lambda p: -freq[p])[:15])
    real_top = set(sorted(species, key=lambda p: real_rank[p])[:15])
    print(f"\nTOP15一致: {len(sim_top & real_top)}/15  共通: {', '.join(sorted(sim_top & real_top))}", flush=True)

if __name__ == "__main__":
    main()
