"""v7のgoal-aligned評価（現features=v7=665）。
 ①v7 vs ヒューリスティック（CRN・総合力） ②v7/ヒューリスティック vs 戦略AI群（戦略対応度）。"""
import random
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.az_np import PVNetNP
from simulator.strategies import make_strategy
from train_az2 import _net_ai
from train_league import _strat_parties

loader = get_loader()
parties = load_registered_parties(loader, complete_only=True)
v7 = PVNetNP.load("az_net_v7.json")
strat_list = _strat_parties(loader)
rng = random.Random(2024)

# ① v7 vs ヒューリスティック（CRN・通常マッチ）
def play_heur(net_factory, pair, seed):
    random.seed(seed)
    pa, pb = pair
    s1 = BattleSide(heuristic_selection(build_party(pa, loader), build_party(pb, loader), loader))
    s2 = BattleSide(heuristic_selection(build_party(pb, loader), build_party(pa, loader), loader))
    s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
    return Battle(s1, s2).run(net_factory(), HeuristicAI()) == 1

Ng, Mg = 30, 4
v7w = hw = nb = 0
for i in range(Ng):
    pair = rng.sample(parties, 2)
    for k in range(Mg):
        bs = 500000 + i * 1000 + k
        v7w += play_heur(lambda: _net_ai(v7, loader, 48, 12, bs), pair, bs)
        hw += play_heur(lambda: HeuristicAI(), pair, bs)
        nb += 1
print(f"① 総合 vsヒューリスティック(CRN N={Ng}): v7 {v7w/nb:.1%} / heur {hw/nb:.1%}  (v7-heur {(v7w-hw)/nb*100:+.1f}pt) ※v6は以前+8pt", flush=True)

# ② v7/ヒューリスティック vs 戦略AI群（CRN・共通乱数）
def play_strat(actor_factory, strat_tpl, strat_name, my_tpl, seed):
    random.seed(seed)
    my6 = build_party(my_tpl, loader); st = build_party(strat_tpl, loader)
    s1 = BattleSide(heuristic_selection(my6, st, loader))
    s2 = BattleSide(st[:3])
    s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
    return Battle(s1, s2).run(actor_factory(), make_strategy(strat_name, seed)) == 1

N, M = 8, 3
tv7 = th = 0
for strat_tpl, sname in strat_list:
    v7s = hs = nb2 = 0
    for i in range(N):
        my_tpl = rng.choice(parties)
        for k in range(M):
            bs = 700000 + i * 1000 + k
            v7s += play_strat(lambda: _net_ai(v7, loader, 48, 12, bs), strat_tpl, sname, my_tpl, bs)
            hs += play_strat(lambda: HeuristicAI(), strat_tpl, sname, my_tpl, bs)
            nb2 += 1
    print(f"  [{sname}] v7 {v7s/nb2:.0%} / heur {hs/nb2:.0%}  (v7-heur {(v7s-hs)/nb2*100:+.0f}pt)", flush=True)
    tv7 += v7s / nb2; th += hs / nb2
print(f"② 戦略AI総合 vs戦略: v7 {tv7/len(strat_list):.1%} / heur {th/len(strat_list):.1%}  (v7-heur {(tv7-th)/len(strat_list)*100:+.1f}pt)", flush=True)
