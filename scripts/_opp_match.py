"""相手モデル改善(opp_mix<1.0) vs 現状(純maximin) の直接対戦。
両者とも d2/k4/同一ネット。new側のみ opp_mix を下げる。selection中立・側交互。
"""
import sys, os, random, time, math
from multiprocessing import Pool

def _play_batch(args):
    seed0, n_games, mix = args
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.env import load_registered_parties, build_party
    from simulator.ai import select_party
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); net = PVNetNP.load()
    parties = load_registered_parties(L, complete_only=True)

    def mk_old():
        return _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=16)
    def mk_new():
        a = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=16)
        a.opp_mix = mix
        return a

    nw = nl = draw = 0
    for g in range(n_games):
        random.seed(seed0 + g)
        pa, pb = random.sample(parties, 2)
        P1 = build_party(pa, L); P2 = build_party(pb, L)
        sel1 = select_party(P1, P2, L, n=min(3, len(P1)), temperature=0.4, rng=random)
        sel2 = select_party(P2, P1, L, n=min(3, len(P2)), temperature=0.4, rng=random)
        s1 = BattleSide(sel1); s2 = BattleSide(sel2)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        new_on_s1 = (g % 2 == 0)
        ai1 = mk_new() if new_on_s1 else mk_old()
        ai2 = mk_old() if new_on_s1 else mk_new()
        w = Battle(s1, s2).run(ai1, ai2)
        if w == 0:
            draw += 1
        else:
            new_won = (w == 1) == new_on_s1
            if new_won: nw += 1
            else: nl += 1
    return nw, nl, draw

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    mix = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
    seed_base = int(sys.argv[4]) if len(sys.argv) > 4 else 2000000
    per = max(1, N // W)
    args = [(seed_base + i * 100000, per, mix) for i in range(W)]
    print(f"設定: new=相手モデル改善(opp_mix={mix}) vs old=純maximin  両者d2/k4  seed_base={seed_base}")
    t0 = time.time()
    with Pool(W) as p:
        res = p.map(_play_batch, args)
    dt = time.time() - t0
    nw = sum(r[0] for r in res); nl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = nw + nl
    wr = nw / dec if dec else 0.0
    if dec:
        z = (nw - dec * 0.5) / math.sqrt(dec * 0.25)
        from math import erfc
        pval = erfc(abs(z) / math.sqrt(2))
    else:
        z = 0.0; pval = 1.0
    print(f"\n=== 相手モデル改善(opp_mix={mix}) vs 現状 : {per*W}試合 / {dt:.0f}秒 ===")
    print(f"new: {nw}勝 {nl}敗 {dr}分（決着{dec}）")
    print(f"new勝率(決着のみ): {wr*100:.1f}%   z={z:+.2f}  p={pval:.4f}  {'有意(p<0.05)' if pval<0.05 else '有意差なし'}")

if __name__ == "__main__":
    main()
