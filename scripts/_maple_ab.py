"""Phase 5 ゲート: MAPLE式（k状態を1本の木で共有）vs PIMC（決定化ごとに別木・根で合算）。

現行本番は PIMC（`mcts_cache` 経路）。MAPLE 論文(arXiv:2605.24139)が strategy fusion として
名指しした型で、決定化ごとに別の最適戦略が立ちそれを平均するので情報集合として一貫しない
手が選ばれる。MAPLE は k 状態で1本の木を共有し、葉で policy/value を平均する。

総ネット評価数を揃えて比較する:
  PIMC  = E木 × (sims/E)           = sims 回
  MAPLE = (sims/k) 展開 × k 状態   = sims 回

env: N(対戦数=300) SIMS(400) K(5) E(16) POOL_SEASON/BELIEF_SEASON/MAX_CORE_RANK
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
import _m6_pool

SEASON = os.environ.get("POOL_SEASON", "M-6")
SIMS = int(os.environ.get("SIMS", "400"))
K = int(os.environ.get("K", "5"))
E = int(os.environ.get("E", "16"))
_f1._ensure_loaded(SEASON, 8)


def _mk(net, L, seed, maple):
    from train_az2 import _net_ai
    ai = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True, mcts_ensemble=E)
    if maple:
        ai.maple_k = K          # _build_mcts_root が maple_k>0 で MAPLE 経路へ分岐
    else:
        ai.maple_k = 0
    return ai


def _battle(args):
    pa, pb, seed, a_first = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, certain_ko_override
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    L = _f1._W["loader"]; net = _f1._W["net"]; _r.seed(seed)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    s1 = BattleSide(select_party(A, B, L, n=3, temperature=0.3, rng=_r), viewer_label="P1", source6=A)
    s2 = BattleSide(select_party(B, A, L, n=3, temperature=0.3, rng=_r), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    # a_first=True なら P1 が MAPLE。先後の有利を相殺するため呼び出し側で交互にする
    ai1 = _mk(net, L, seed, a_first)
    ai2 = _mk(net, L, seed ^ 0x5bd1e995, not a_first)
    res = Battle(s1, s2, BattleField()).run(
        lambda m, o, f: certain_ko_override(ai1(m, o, f), m, o, f),
        lambda m, o, f: certain_ko_override(ai2(m, o, f), m, o, f))
    if res == 0:
        return 0
    maple_won = (res == 1) == a_first
    return 1 if maple_won else -1


def main():
    N = int(os.environ.get("N", "300"))
    P = _m6_pool.load_parties()
    rng = random.Random(31337)
    jobs = []
    for i in range(N):
        a, b = rng.sample(range(len(P)), 2)
        jobs.append((P[a], P[b], 60000 + i * 7717, i % 2 == 0))
    print(f"■ MAPLE(k={K}) vs PIMC(E={E})  sims={SIMS} 総ネット評価は同数  {N}戦  {_m6_pool.describe()}",
          flush=True)
    w = int(os.environ.get("AB_WORKERS", "0")) or max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(w) as pool:
        out = pool.map(_battle, jobs, chunksize=1)
    win = sum(1 for x in out if x > 0); lose = sum(1 for x in out if x < 0)
    draw = sum(1 for x in out if x == 0)
    dec = win + lose
    wr = win / dec if dec else 0.0
    z = (win - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0.0
    pv = math.erfc(abs(z) / math.sqrt(2)) if dec else 1.0
    print(f"MAPLE: {win}勝 {lose}敗 {draw}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}"
          + ("  有意" if pv < 0.05 else "  有意差なし"), flush=True)


if __name__ == "__main__":
    main()
