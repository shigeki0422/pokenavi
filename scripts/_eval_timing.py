"""d2 と MCTS(regret) の1戦あたり実時間を計測し、同一時間でのsim数を出す。"""
import os, time, random
os.environ.setdefault("OMP_NUM_THREADS","1")
SEASON="M-3"
import _pop_gen as G
from simulator.simulate import get_loader
from simulator.az_np import PVNetNP
from simulator.battle import BattleSide, Battle
from simulator.belief import OpponentBelief
from simulator.ai import select_party
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from train_az2 import _net_ai
L=get_loader(); net=PVNetNP.load()
D=G.load(season=SEASON); rng=random.Random(7)
pool=[G.gen_party(D,rng) for _ in range(30)]
def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]
def run_n(mk, n=8, seed0=100):
    rng=random.Random(seed0); t=0.0; done=0
    for g in range(n):
        a,b=rng.sample(pool,2); A=team(a); B=team(b)
        sa=select_party(A,B,L,n=3,temperature=0.3,rng=rng); sb=select_party(B,A,L,n=3,temperature=0.3,rng=rng)
        s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
        ai1=mk(); ai2=mk()
        t0=time.time(); Battle(s1,s2).run(ai1,ai2); t+=time.time()-t0; done+=1
    return t/done
d2=lambda: _net_ai(net,L,0,12,0,tree=True,tree_depth=2,tree_k=4,tree_det=8)
print("計測中(各8戦)...", flush=True)
td2=run_n(d2)
print(f"d2: {td2:.2f}秒/戦", flush=True)
for sims in (400,1200):
    mk=lambda s=sims: _net_ai(net,L,0,12,0,mcts=True,mcts_sims=s,mcts_select="regret",mcts_fast=True)
    tm=run_n(mk)
    print(f"MCTS regret@{sims}: {tm:.2f}秒/戦  (d2比 ×{tm/td2:.1f})", flush=True)
