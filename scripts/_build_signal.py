"""型(持物/技/性格/EV)の良し悪しが勝率に出るか＝評価器別の信号強度を測る。
各種族で「実メタ良型」vs「ランダム悪型」のテストパーティ(=該当種+固定2体)を gauntlet と対戦。
NetGreedy(弱) と d2(強) で 勝率差(良型-悪型) を比較。d2で差が大きくNetGreedyで~0なら
「型最適化には強評価が必要」＝共進化の評価器をd2/MCTSに上げれば型も最適化できる、と確認できる。
"""
import sys, os, random, math
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-2"
SPECIES = ["ガブリアス", "リザードン", "マスカーニャ", "アシレーヌ", "ギャラドス", "ルカリオ"]
FIXED = ["カバルドン", "ブリジュラス"]  # テスト種に添える固定2体(良型)
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    from train_az2 import _net_ai
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["NG"] = NetGreedyAI
    _W["D"] = G.load(season=SEASON)
    _W["d2"] = _net_ai(_W["net"], _W["L"], 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def good_spec(p, rng):
    D = _W["D"]
    item = max(D["items"].get(p, {"":1}), key=D["items"].get(p, {"":1}).get) if D["items"].get(p) else None
    nat = max(D["natures"].get(p, {"":1}), key=D["natures"].get(p, {"":1}).get) if D["natures"].get(p) else None
    mv = sorted(D["moves"].get(p, {}), key=D["moves"][p].get, reverse=True)[:4] if D["moves"].get(p) else []
    ev = D["evs"].get(p, [(None, 1)])[0][0]
    return G._spec(p, item, nat, mv, ev, None)

def bad_spec(p, rng):
    D = _W["D"]
    items = list(D["items"].get(p, {}).keys()); nats = list(D["natures"].get(p, {}).keys())
    mvs = list(D["moves"].get(p, {}).keys()); evs = [e for e, _ in D["evs"].get(p, [])]
    item = rng.choice(items) if items else None
    nat = rng.choice(nats) if nats else None
    mv = rng.sample(mvs, min(4, len(mvs))) if mvs else []
    ev = rng.choice(evs) if evs else None
    return G._spec(p, item, nat, mv, ev, None)

def _team(specs):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in specs]

def _winrate(test_specs, gauntlet, ai_key, K, rng):
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; net = _W["net"]
    if ai_key == "ng":
        mk = lambda: _W["NG"](net)
    else:
        d2 = _W["d2"]; mk = lambda: d2
    w = d = 0
    for opp in gauntlet:
        for g in range(K):
            A = _team(test_specs); B = _team(opp)
            sa = select_party(A, B, L, n=3, temperature=0.0, rng=rng); sb = select_party(B, A, L, n=3, temperature=0.0, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try:
                r = Battle(s1, s2).run(mk(), mk())
            except Exception:
                r = 0
            if r != 0: d += 1; w += (r == 1)
    return w / d if d else 0.5

def _job(args):
    seed, sp, ai_key, gauntlet, K = args
    rng = random.Random(seed)
    fixed = [good_spec(FIXED[0], rng), good_spec(FIXED[1], rng)]
    good = [good_spec(sp, rng)] + fixed
    bad = [bad_spec(sp, rng)] + fixed
    wg = _winrate(good, gauntlet, ai_key, K, rng)
    wb = _winrate(bad, gauntlet, ai_key, K, rng)
    return sp, ai_key, wg, wb

def main():
    ng_K = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    d2_K = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    gn = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    workers = 12
    import time
    D = G.load(season=SEASON)
    gauntlet = [G.gen_party(D, random.Random(50000 + k)) for k in range(gn)]
    jobs = []
    for i, sp in enumerate(SPECIES):
        jobs.append((1000 + i, sp, "ng", gauntlet, ng_K))
        jobs.append((2000 + i, sp, "d2", gauntlet, d2_K))
    t0 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_job, jobs)
    agg = {}
    for sp, ai, wg, wb in res:
        agg.setdefault(sp, {})[ai] = (wg, wb)
    print(f"\n=== 型の良し悪しの勝率差（良型 vs ランダム悪型）{time.time()-t0:.0f}s ===")
    print(f"{'種族':<12} {'NetGreedy良/悪/差':<22} {'d2良/悪/差':<22}")
    ng_gaps = []; d2_gaps = []
    for sp in SPECIES:
        ng = agg[sp]["ng"]; d2 = agg[sp]["d2"]
        ng_gap = ng[0] - ng[1]; d2_gap = d2[0] - d2[1]
        ng_gaps.append(ng_gap); d2_gaps.append(d2_gap)
        print(f"{sp:<12} {ng[0]*100:4.0f}/{ng[1]*100:4.0f}/{ng_gap*100:+5.1f}        {d2[0]*100:4.0f}/{d2[1]*100:4.0f}/{d2_gap*100:+5.1f}")
    print(f"\n平均ギャップ(良型-悪型): NetGreedy={sum(ng_gaps)/len(ng_gaps)*100:+.1f}pt  d2={sum(d2_gaps)/len(d2_gaps)*100:+.1f}pt")
    print("→ d2の方が大きければ「型最適化には強評価が必要(共進化の評価器をd2/MCTSに上げる)」が裏付け")

if __name__ == "__main__":
    main()
