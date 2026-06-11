"""AI強度の常設CRNベンチマーク（評価ノイズに騙されないための標準判定）。

  python benchmark.py <net.json> [n_general] [n_strat]

出力：
  ① 総合力: net vs HeuristicAI（共通乱数法・同一相手/乱数）
  ② 戦略対応: net / Heuristic vs 戦略AI群（積み/壁/受け/バトン）

注意: net の次元は現 features.py と一致している必要がある（features と net は同世代で）。
"""
import sys, random
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.az_np import PVNetNP
from simulator.strategies import make_strategy
from train_az2 import _net_ai
from train_league import _strat_parties


def run(net_path, n_general=30, n_strat=8, rollouts=48, depth=12, seed=2024):
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load(net_path)
    print(f"=== ベンチマーク: {net_path} (dim={net.dim}, rollouts={rollouts}) ===", flush=True)
    rng = random.Random(seed)

    # ① 総合力（CRN）
    def play_h(actor, pair, s):
        random.seed(s)
        pa, pb = pair
        s1 = BattleSide(heuristic_selection(build_party(pa, loader), build_party(pb, loader), loader))
        s2 = BattleSide(heuristic_selection(build_party(pb, loader), build_party(pa, loader), loader))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        return Battle(s1, s2).run(actor(), HeuristicAI()) == 1
    nw = hw = nb = 0
    for i in range(n_general):
        pair = rng.sample(parties, 2)
        for k in range(4):
            bs = 500000 + i * 1000 + k
            nw += play_h(lambda: _net_ai(net, loader, rollouts, depth, bs), pair, bs)
            hw += play_h(lambda: HeuristicAI(), pair, bs)
            nb += 1
    g_net, g_heur = nw / nb, hw / nb
    print(f"① 総合 vsHeuristic(CRN N={n_general}): net {g_net:.1%} / heur {g_heur:.1%}  (差 {(g_net-g_heur)*100:+.1f}pt)", flush=True)

    # ② 戦略対応（CRN）
    def play_s(actor, st_tpl, st_name, my_tpl, s):
        random.seed(s)
        my6 = build_party(my_tpl, loader); st = build_party(st_tpl, loader)
        s1 = BattleSide(heuristic_selection(my6, st, loader)); s2 = BattleSide(st[:3])
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        return Battle(s1, s2).run(actor(), make_strategy(st_name, s)) == 1
    strat_list = _strat_parties(loader)
    tnet = theur = 0
    for st_tpl, sname in strat_list:
        ns = hs = nb2 = 0
        for i in range(n_strat):
            my_tpl = rng.choice(parties)
            for k in range(3):
                bs = 700000 + i * 1000 + k
                ns += play_s(lambda: _net_ai(net, loader, rollouts, depth, bs), st_tpl, sname, my_tpl, bs)
                hs += play_s(lambda: HeuristicAI(), st_tpl, sname, my_tpl, bs)
                nb2 += 1
        print(f"  [{sname}] net {ns/nb2:.0%} / heur {hs/nb2:.0%}  (差 {(ns-hs)/nb2*100:+.0f}pt)", flush=True)
        tnet += ns / nb2; theur += hs / nb2
    s_net, s_heur = tnet / len(strat_list), theur / len(strat_list)
    print(f"② 戦略AI総合: net {s_net:.1%} / heur {s_heur:.1%}  (差 {(s_net-s_heur)*100:+.1f}pt)", flush=True)
    print(f"[まとめ] {net_path}: 総合 {(g_net-g_heur)*100:+.1f}pt / 戦略 {(s_net-s_heur)*100:+.1f}pt vs Heuristic", flush=True)
    return {"general": g_net - g_heur, "strategy": s_net - s_heur}


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "az_net_np.json"
    ng = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    nst = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    run(path, ng, nst)
