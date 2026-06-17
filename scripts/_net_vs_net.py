"""2つのネットファイルを直接対戦させる。
netA(新・学習)を d3@k2+メガ畳み込みで、netB(現行)を d2@k4 で対局。selection中立・側交互・2メガ回避。
"""
import sys, os, random, time, math
from multiprocessing import Pool

def _play_batch(args):
    seed0, n_games, pathA, pathB, dA, kA, colA = args
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.env import load_registered_parties, build_party
    from simulator.ai import select_party
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader()
    netA = PVNetNP.load(pathA); netB = PVNetNP.load(pathB)
    parties = load_registered_parties(L, complete_only=True)

    def mkA():  # 新ネット: 戦術は引数（既定 d3@k2+畳み込み。純粋なネット比較なら d2/k4/colA=0）
        a = _net_ai(netA, L, 0, 12, 0, tree=True, tree_depth=dA, tree_k=kA, tree_det=16)
        if colA: a.collapse_mega = True
        return a
    def mkB():  # 現行ネット: d2@k4
        return _net_ai(netB, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=16)

    aw = al = draw = 0
    for g in range(n_games):
        random.seed(seed0 + g)
        pa, pb = random.sample(parties, 2)
        P1 = build_party(pa, L); P2 = build_party(pb, L)
        sel1 = select_party(P1, P2, L, n=min(3, len(P1)), temperature=0.4, rng=random)
        sel2 = select_party(P2, P1, L, n=min(3, len(P2)), temperature=0.4, rng=random)
        s1 = BattleSide(sel1); s2 = BattleSide(sel2)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        A_on_s1 = (g % 2 == 0)
        ai1 = mkA() if A_on_s1 else mkB()
        ai2 = mkB() if A_on_s1 else mkA()
        w = Battle(s1, s2).run(ai1, ai2)
        if w == 0: draw += 1
        else:
            A_won = (w == 1) == A_on_s1
            if A_won: aw += 1
            else: al += 1
    return aw, al, draw

def main():
    N = int(sys.argv[1]); W = int(sys.argv[2]); pathA = sys.argv[3]; pathB = sys.argv[4]
    dA = int(sys.argv[5]) if len(sys.argv) > 5 else 3
    kA = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    colA = int(sys.argv[7]) if len(sys.argv) > 7 else 1
    per = max(1, N // W)
    args = [(3000000 + i * 100000, per, pathA, pathB, dA, kA, colA) for i in range(W)]
    print(f"netA(新,d{dA}/k{kA}/collapse{colA})={pathA}  vs  netB(現行,d2@k4)={pathB}")
    t0 = time.time()
    with Pool(W) as p:
        res = p.map(_play_batch, args)
    dt = time.time() - t0
    aw = sum(r[0] for r in res); al = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = aw + al; wr = aw / dec if dec else 0.0
    if dec:
        z = (aw - dec * 0.5) / math.sqrt(dec * 0.25)
        from math import erfc; pval = erfc(abs(z) / math.sqrt(2))
    else:
        z = 0.0; pval = 1.0
    print(f"\n=== 新ネット vs 現行ネット : {per*W}試合 / {dt:.0f}秒 ===")
    print(f"新: {aw}勝 {al}敗 {dr}分（決着{dec}）")
    print(f"新勝率(決着のみ): {wr*100:.1f}%   z={z:+.2f}  p={pval:.4f}  {'有意(p<0.05)' if pval<0.05 else '有意差なし'}")

if __name__ == "__main__":
    main()
