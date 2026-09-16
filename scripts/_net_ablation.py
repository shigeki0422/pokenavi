"""ネットの寄与量を測る: 学習済みネット vs ランダム初期化ネット（同一アーキ・同sims）。

特徴量(v2/v3)も探索の集約(MAPLE)も効かなかった。どちらも「葉の評価関数」を良くする施策で、
効かないなら **そもそも葉の評価がボトルネックでない** 可能性がある。MCTS は実エンジンを
回すので、@400 の探索が届く範囲は評価関数が悪くても正しく判断できてしまう。

ランダム初期化ネットに対する勝率が小さければ、ネットの改善に投資しても伸びない。
大きければ、評価関数は効いており改善余地が残っている。

env: N(対戦数) SIMS(400) NET_B(比較相手。既定=ランダム初期化)
"""
import os, sys, math, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
import _m6_pool

SEASON = os.environ.get("POOL_SEASON", "M-6")
SIMS = int(os.environ.get("SIMS", "400"))
_f1._ensure_loaded(SEASON, 8)
NET_B = os.environ.get("NET_B")   # 未指定ならランダム初期化


def _battle(args):
    pa, pb, seed, a_first = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, certain_ko_override
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.az_np import PVNetNP
    from simulator.features import feature_dim
    from train_az2 import _net_ai
    L = _f1._W["loader"]; netA = _f1._W["net"]; _r.seed(seed)
    if NET_B:
        netB = PVNetNP.load(NET_B)
    else:
        netB = PVNetNP(feature_dim(), hidden=netA.hidden, hidden2=netA.hidden2, seed=12345)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    s1 = BattleSide(select_party(A, B, L, n=3, temperature=0.3, rng=_r), viewer_label="P1", source6=A)
    s2 = BattleSide(select_party(B, A, L, n=3, temperature=0.3, rng=_r), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    n1 = netA if a_first else netB
    n2 = netB if a_first else netA
    ai1 = _net_ai(n1, L, 0, 12, seed, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    ai2 = _net_ai(n2, L, 0, 12, seed ^ 0x5bd1e995, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    res = Battle(s1, s2, BattleField()).run(
        lambda m, o, f: certain_ko_override(ai1(m, o, f), m, o, f),
        lambda m, o, f: certain_ko_override(ai2(m, o, f), m, o, f))
    if res == 0:
        return 0
    return 1 if ((res == 1) == a_first) else -1


def main():
    N = int(os.environ.get("N", "200"))
    P = _m6_pool.load_parties()
    rng = random.Random(24680)
    jobs = [(P[a], P[b], 80000 + i * 7717, i % 2 == 0)
            for i, (a, b) in enumerate(rng.sample(range(len(P)), 2) for _ in range(N))]
    label = NET_B or "ランダム初期化ネット"
    print(f"■ 学習済みネット vs {label}  sims={SIMS}  {N}戦  {_m6_pool.describe()}", flush=True)
    w = int(os.environ.get("AB_WORKERS", "0")) or max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(w) as pool:
        out = pool.map(_battle, jobs, chunksize=1)
    win = sum(1 for x in out if x > 0); lose = sum(1 for x in out if x < 0); draw = sum(1 for x in out if x == 0)
    dec = win + lose; wr = win / dec if dec else 0
    z = (win - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0
    print(f"学習済み: {win}勝 {lose}敗 {draw}分 → 勝率{wr*100:.1f}%  z={z:+.2f} "
          f"p={math.erfc(abs(z)/math.sqrt(2)):.4f}", flush=True)


if __name__ == "__main__":
    main()
