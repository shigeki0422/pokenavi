"""d3(メガ畳み込み, k2) vs 現状d2(k4) の直接対戦で有意に勝つか検証。
両者とも同じ学習済みネットを使用（再学習なし）。selection は深さ非依存なので中立。
"""
import sys, os, random, time, math
from multiprocessing import Pool

def _play_batch(args):
    seed0, n_games, d3_depth, d3_k = args
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

    def mk_d2():  # 現状: d2, k4, メガ倍化(従来)
        return _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=16)
    def mk_d3():  # 新: メガ畳み込み, 深さ/k は引数
        a = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=d3_depth, tree_k=d3_k, tree_det=16)
        a.collapse_mega = True
        return a

    d3_w = d3_l = draw = 0
    for g in range(n_games):
        random.seed(seed0 + g)
        pa, pb = random.sample(parties, 2)
        P1 = build_party(pa, L); P2 = build_party(pb, L)
        sel1 = select_party(P1, P2, L, n=min(3, len(P1)), temperature=0.4, rng=random)
        sel2 = select_party(P2, P1, L, n=min(3, len(P2)), temperature=0.4, rng=random)
        s1 = BattleSide(sel1); s2 = BattleSide(sel2)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        d3_on_s1 = (g % 2 == 0)  # 側のバイアス除去で交互
        ai1 = mk_d3() if d3_on_s1 else mk_d2()
        ai2 = mk_d2() if d3_on_s1 else mk_d3()
        w = Battle(s1, s2).run(ai1, ai2)
        if w == 0:
            draw += 1
        else:
            d3_won = (w == 1) == d3_on_s1
            if d3_won: d3_w += 1
            else: d3_l += 1
    return d3_w, d3_l, draw

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 240
    W = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    d3_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    d3_k = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    seed_base = int(sys.argv[5]) if len(sys.argv) > 5 else 1000
    per = max(1, N // W)
    args = [(seed_base + i * 100000, per, d3_depth, d3_k) for i in range(W)]
    print(f"設定: d3=depth{d3_depth}/k{d3_k}(畳み込み) vs d2=depth2/k4  seed_base={seed_base}")
    t0 = time.time()
    with Pool(W) as p:
        res = p.map(_play_batch, args)
    dt = time.time() - t0
    d3w = sum(r[0] for r in res); d3l = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = d3w + d3l
    wr = d3w / dec if dec else 0.0
    # 両側二項検定 p値（正規近似）
    if dec:
        z = (d3w - dec * 0.5) / math.sqrt(dec * 0.25)
        from math import erfc
        pval = erfc(abs(z) / math.sqrt(2))
    else:
        z = 0.0; pval = 1.0
    print(f"\n=== d3(畳み込み,depth{d3_depth}/k{d3_k}) vs 現状d2(k4) : {per*W}試合 / {dt:.0f}秒 ===")
    print(f"d3: {d3w}勝 {d3l}敗 {dr}分（決着{dec}）")
    print(f"d3勝率(決着のみ): {wr*100:.1f}%   z={z:+.2f}  p={pval:.4f}  {'有意(p<0.05)' if pval<0.05 else '有意差なし'}")

if __name__ == "__main__":
    main()
