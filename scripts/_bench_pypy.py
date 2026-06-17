"""CPython vs PyPy ベンチ（同一ワークロード）。バトルエンジン純Python部のJIT効果を測る。
使い方: ./venv/bin/python _bench_pypy.py / ./venv_pypy/bin/python _bench_pypy.py
"""
import sys, time, random
import _pop_gen as G
from simulator.simulate import get_loader
from simulator.az_np import PVNetNP
from train_az2 import _net_ai
from simulator.battle import BattleSide, Battle, BattleField
from simulator.belief import OpponentBelief
from simulator.ai import select_party
from simulator.pokemon import build_from_spec, parse_pokemon_spec

print(f"== interpreter: {sys.implementation.name} {sys.version.split()[0]} ==", flush=True)
L = get_loader(); net = PVNetNP.load()
D = G.load(season="M-2"); rng = random.Random(7)
parties = [G.gen_party(D, rng) for _ in range(8)]
def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season="M-2", randomize=False) for s in sp]
def mkstate(a, b):
    s1 = BattleSide(list(select_party(team(a), team(b), L, n=3, temperature=0.0, rng=rng)))
    s2 = BattleSide(list(select_party(team(b), team(a), L, n=3, temperature=0.0, rng=rng)))
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L); s1.field_idx = 0; s2.field_idx = 1
    return s1, s2, BattleField()

# --- d2 フルバトル ---
d2 = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)
# warmup (JITトレース)
for k in range(2):
    s1 = BattleSide(list(select_party(team(parties[0]), team(parties[1]), L, n=3, temperature=0.0, rng=rng)))
    s2 = BattleSide(list(select_party(team(parties[1]), team(parties[0]), L, n=3, temperature=0.0, rng=rng)))
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    Battle(s1, s2).run(d2, d2)
t = time.time(); nb = 4
for k in range(nb):
    s1 = BattleSide(list(select_party(team(parties[k % 8]), team(parties[(k+3) % 8]), L, n=3, temperature=0.0, rng=rng)))
    s2 = BattleSide(list(select_party(team(parties[(k+3) % 8]), team(parties[k % 8]), L, n=3, temperature=0.0, rng=rng)))
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    Battle(s1, s2).run(d2, d2)
print(f"d2 フルバトル: {(time.time()-t)/nb:.2f}s/戦 (warm)", flush=True)

# --- MCTS-regret@1600 1手 ---
mc = _net_ai(net, L, 0, 50, 0, mcts=True, mcts_sims=1600, c_puct=1.5, mcts_select="regret")
st = mkstate(parties[0], parties[1]); mc(*st)  # warmup
t = time.time(); nm = 4
for k in range(nm):
    mc(*mkstate(parties[k % 8], parties[(k+3) % 8]))
print(f"MCTS-regret@1600: {(time.time()-t)/nm:.3f}s/手 (warm)", flush=True)
