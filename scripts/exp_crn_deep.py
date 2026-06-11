"""CRN（共通乱数法）比較: deep net vs v6 net vs heuristic（同一相手・同一対戦乱数）。"""
import random
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.az_np import PVNetNP
from train_az2 import _net_ai

loader = get_loader()
parties = load_registered_parties(loader, complete_only=True)
v6 = PVNetNP.load("az_net_np.json")
deep = PVNetNP.load("az_net_deep.json")
rng = random.Random(555)


def play(ai_factory, pair, seed):
    random.seed(seed)
    pa, pb = pair
    s1 = BattleSide(heuristic_selection(build_party(pa, loader), build_party(pb, loader), loader))
    s2 = BattleSide(heuristic_selection(build_party(pb, loader), build_party(pa, loader), loader))
    s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
    return Battle(s1, s2).run(ai_factory(), HeuristicAI()) == 1


N, M = 24, 4
dw = vw = hw = nb = 0
for i in range(N):
    pair = rng.sample(parties, 2)
    for k in range(M):
        bs = 500000 + i * 1000 + k
        dw += play(lambda: _net_ai(deep, loader, 48, 12, bs), pair, bs)
        vw += play(lambda: _net_ai(v6, loader, 48, 12, bs), pair, bs)
        hw += play(lambda: HeuristicAI(), pair, bs)
        nb += 1
    print(f"  {i+1}/{N}: deep {dw/nb:.1%} / v6 {vw/nb:.1%} / heur {hw/nb:.1%}", flush=True)
print(f"CRN比較 N={N} M={M}: deep {dw/nb:.1%} / v6 {vw/nb:.1%} / heur {hw/nb:.1%}  "
      f"(deep-v6 {(dw-vw)/nb*100:+.1f}pt, deep-heur {(dw-hw)/nb*100:+.1f}pt)", flush=True)
