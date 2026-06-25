import os, json, glob, random
os.environ.setdefault("OMP_NUM_THREADS","1")
from simulator.simulate import get_loader
from simulator.az_np import PVNetNP
from simulator.ai import GreedyAI, select_party, certain_ko_override
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.battle import BattleSide, Battle
from simulator.belief import OpponentBelief
from train_az2 import _net_ai

L=get_loader(); net=PVNetNP.load("az_net_np.json")
wai=_net_ai(net,L,0,12,0,mcts=True,mcts_sims=400,mcts_select="regret",mcts_fast=True)
g=GreedyAI()
parties=[json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
rng=random.Random(1)
SEASON="M-3"
def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]

vol=[0]  # GreedyAIが返したswitch行動数
def gwrap(my,opp,f):
    a=certain_ko_override(g(my,opp,f),my,opp,f)
    if getattr(a,"type",None)=="switch": vol[0]+=1
    return a
def nwrap(my,opp,f):
    return certain_ko_override(wai(my,opp,f),my,opp,f)

import re
forced_faint=[0]; greedy_active_changes=[0]
for k in range(30):
    a,b=rng.sample(range(len(parties)),2)
    PA=team(parties[a]); PB=team(parties[b])
    sa=select_party(PA,PB,L,n=3,temperature=0.3,rng=rng)
    sb=select_party(PB,PA,L,n=3,temperature=0.3,rng=rng)
    s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
    # Greedy = s2
    bt=Battle(s1,s2)
    w=bt.run(nwrap,gwrap)
    # ログからGreedy側(s2)の交代起因を数える: 「引っ込んだ」=自発/ピボット, 倒れ由来は別行で
    for ln in bt.logs:
        if "倒れた" in ln: pass
print("Greedyが返した自発switch行動 総数:", vol[0], "/ 30戦")
