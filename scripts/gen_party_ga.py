"""M-3環境パーティをGAで生成・進化。
プール＝build_pool_M-3の型のみ／種は順位重み（型数中立）／1パーティ6種別・ちょうど2メガ。
適合度＝集団内サンプリング総当たりの勝率（価値ネット＋MCTS、選出は学習選出）。
出力: gen_pop.json（最終世代の全パーティ＋適合度）。ゲート1で確認用。

env: POP(300) K(15・1個体あたり対戦相手数) GA_SIMS(300) GENS(10) ELITE(0.2) MUT(0.3) FRESH(0.1)
"""
import os, json, random, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1

SEASON = os.environ.get("POOL_SEASON", "M-3")
POP = int(os.environ.get("POP", "300"))
K = int(os.environ.get("K", "15"))
SIMS = int(os.environ.get("GA_SIMS", "300"))
GENS = int(os.environ.get("GENS", "10"))
ELITE = float(os.environ.get("ELITE", "0.2"))
MUT = float(os.environ.get("MUT", "0.3"))
FRESH = float(os.environ.get("FRESH", "0.1"))


def _play_winner(args):
    p1, p2, seed = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.ai import certain_ko_override
    from train_az2 import _net_ai
    L = _f1._W["loader"]; net = _f1._W["net"]
    _r.seed(seed)
    P1 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in p1]
    P2 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in p2]
    sel1 = learned_select_party(P1, P2, L, n=3, temperature=0.3)
    sel2 = learned_select_party(P2, P1, L, n=3, temperature=0.3)
    s1 = BattleSide(sel1, viewer_label="P1", source6=P1)
    s2 = BattleSide(sel2, viewer_label="P2", source6=P2)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(net, L, 0, 12, seed ^ 1540483477, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True)
    def ai1(my, opp, f): return certain_ko_override(a1(my, opp, f), my, opp, f)
    def ai2(my, opp, f): return certain_ko_override(a2(my, opp, f), my, opp, f)
    return Battle(s1, s2, BattleField()).run(ai1, ai2)
