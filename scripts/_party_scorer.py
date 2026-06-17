"""機能2蒸留 マイルストーン1：パーティ強さスコアラー。
固定gauntlet(usage重みの生成パーティ群=メタ)への勝率をラベルに、パーティ特徴→勝率をMLP学習。
これが効けば穴埋め最適化/改善提案を ms 級でできる（実対戦バッチ20-40分を蒸留）。
phase1 ラベル生成(NetGreedy・並列) → phase2 学習 → phase3 相関検証(held-out)。
"""
import sys, os, random, math, pickle
import numpy as np
from multiprocessing import Pool
import _pop_gen as G
from _selector import ValMLP

SEASON = "M-2"
GN = 16  # gauntlet(固定メタ)サイズ

def _gauntlet(D):
    return [G.gen_party(D, random.Random(50000 + k)) for k in range(GN)]

# ---- パーティ特徴量（順不同・固定長） ----
_F = {}
def encode_party(mons):
    from simulator.features import (TYPES, _TI, _M_SETUP, _M_RECOVER, _M_HAZARD, _M_PIVOT, _M_STATUS)
    from simulator.data import get_type_effectiveness
    per = []
    for p in mons:
        f = [p.max_hp/200, p.attack/200, p.defense/200, p.sp_attack/200, p.sp_defense/200, p.speed/200]
        tv = [0.0]*18
        for t in (p.type1, p.type2):
            if t in _TI: tv[_TI[t]] = 1.0
        f += tv
        oc = [0.0]*18
        for mv in p.moves:
            if mv and mv.power and mv.category != "status" and mv.type in _TI:
                oc[_TI[mv.type]] = max(oc[_TI[mv.type]], min(1.5, mv.power/120))
        f += oc
        names = {mv.name_jp for mv in p.moves if mv}
        has_pri = any(mv and mv.priority and mv.priority > 0 for mv in p.moves)
        f += [1.0 if has_pri else 0.0,
              1.0 if (names & _M_SETUP) else 0.0,
              1.0 if (names & _M_RECOVER) else 0.0,
              1.0 if (names & _M_HAZARD) else 0.0,
              1.0 if (names & _M_PIVOT) else 0.0,
              1.0 if (names & _M_STATUS) else 0.0,
              1.0 if p.mega_data is not None else 0.0]
        per.append(f)
    A = np.array(per)
    agg = list(A.mean(0)) + list(A.max(0))
    speeds = sorted([p.speed for p in mons], reverse=True)
    agg += [s/200 for s in speeds[:6]] + [0.0]*(6-len(speeds[:6]))
    agg += [sum(1 for p in mons if p.mega_data is not None)/2.0]
    dl = [0.0]*18
    for at in TYPES:
        c = sum(1 for p in mons if get_type_effectiveness(at, p.type1, p.type2) > 1.0)
        dl[_TI[at]] = c/6.0
    agg += dl
    return agg

_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["NG"] = NetGreedyAI

def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]

def _winrate_vs_gauntlet(cand_specs, gauntlet, rng, K=4):
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; net = _W["net"]; NG = _W["NG"]
    wins = dec = 0
    for opp in gauntlet:
        for _ in range(K):
            PA = _team(cand_specs); PB = _team(opp)
            sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try:
                w = Battle(s1, s2).run(NG(net), NG(net))
            except Exception:
                w = 0
            if w != 0:
                dec += 1; wins += (w == 1)
    return wins/dec if dec else 0.5

def _gen(args):
    seed, cands, gauntlet = args
    rng = random.Random(seed)
    out = []
    for sp in cands:
        y = _winrate_vs_gauntlet(sp, gauntlet, rng)
        x = encode_party(_team(sp))
        out.append((x, y))
    return out

def _pearson(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return cov/(sx*sy) if sx and sy else 0.0

def main():
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    workers = 12
    import time
    D = G.load(season=SEASON); rng = random.Random(0)
    gauntlet = _gauntlet(D)
    cands = [G.gen_party(D, rng) for _ in range(nsamp)]
    per = max(1, nsamp//workers)
    chunks = [cands[k*per:(k+1)*per] for k in range(workers)]
    t0 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        data = []
        for r in pool.map(_gen, [(700+k, ch, gauntlet) for k, ch in enumerate(chunks)]): data += r
    X = [d[0] for d in data]; Y = [d[1] for d in data]
    print(f"phase1 ラベル生成: {len(data)}パーティ {time.time()-t0:.0f}秒 (勝率分布 mean={np.mean(Y):.3f} sd={np.std(Y):.3f})", flush=True)
    ntr = int(len(X)*0.9)
    sc = ValMLP(len(X[0]), hidden=128).fit(X[:ntr], Y[:ntr], epochs=80)
    pv = sc.predict(X[ntr:]); ya = np.asarray(Y[ntr:])
    r = _pearson(list(pv), list(ya)); mae = float(np.mean(np.abs(pv-ya)))
    print(f"phase2/3 学習完了: held-out Pearson r={r:.3f} MAE={mae:.3f} (n={len(ya)})", flush=True)
    with open("/tmp/party_scorer.pkl", "wb") as fh: pickle.dump(sc, fh)
    print(f"  → {'有望(r>0.4)＝パーティ強さを予測できる' if r>0.4 else 'r低＝特徴量/ラベル要改善'}", flush=True)

if __name__ == "__main__":
    main()
