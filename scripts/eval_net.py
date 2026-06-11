"""現ネットの厳密評価（サンプル増で勝率の分散を抑える）。"""
import random
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.search_ai import SearchAI
from simulator.features import encode_state
from simulator.az_np import PVNetNP

if __name__ == "__main__":
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load()
    def vfn(s1, s2, f): return net.evaluate(encode_state(s1, s2, f), [0])[1]
    heur = HeuristicAI(); rng = random.Random(123)
    N = 50; win = lose = 0
    for i in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader)); s2 = BattleSide(heuristic_selection(a2, a1, loader))
        sc = SearchAI(loader, rollouts=12, depth=6, seed=2000 + i, value_fn=vfn)
        if i % 2 == 0:
            s1.belief = OpponentBelief(loader); w = Battle(s1, s2).run(sc, heur); win += (w == 1); lose += (w == 2)
        else:
            s2.belief = OpponentBelief(loader); w = Battle(s1, s2).run(heur, sc); win += (w == 2); lose += (w == 1)
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{N}: {win}勝{lose}敗", flush=True)
    tot = win + lose
    print(f"\n現ネット(84dim,256x128,継続16反復) vs Heuristic: {win}勝{lose}敗 ({win/max(1,tot):.0%}) N={tot}")
