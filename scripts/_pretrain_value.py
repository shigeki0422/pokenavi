"""価値ヘッドをランダム方策コーパスで事前学習する。

方策ヘッドは触らない（ランダムな行動は方策の教師にならない）。W1/W2 は共有なので
価値の学習が表現層も改善するが、方策が壊れないよう value_weight を使い分ける:
  PHASE=value  価値のみ学習（方策ターゲットを与えず、方策勾配は流さない）

学習後、方策ヘッドは元のネットのものへ戻す（表現層の変化に方策ヘッドが追随して
いないと方策が壊れるため、戻すのではなく「方策も微調整する」のが本筋だが、
まずは価値の効果を切り分けて測るためにこの形にする）。

env: IN(az_net_np.json) OUT(az_net_valpre.json) CORPUS(/tmp/rnd) EPOCHS(15)
     VALUE_BINS(32) KEEP_POLICY(1=方策ヘッドを元に戻す)
"""
import os, sys, json
import numpy as np

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
IN = os.environ.get("IN", os.path.join(D, "az_net_np.json"))
OUT = os.environ.get("OUT", os.path.join(D, "az_net_valpre.json"))
CORPUS = os.environ.get("CORPUS", "/tmp/rnd")
EPOCHS = int(os.environ.get("EPOCHS", "15"))
KEEP_POLICY = os.environ.get("KEEP_POLICY", "1") == "1"
PHASE = os.environ.get("PHASE", "all")   # head=表現層を凍結し価値ヘッド(Wv,bv)だけ学習
                                         # joint=価値を大量コーパスで学習した後、方策をMCTSπで再学習
PI_CORPUS = os.environ.get("PI_CORPUS", "")   # _PI/_M を持つ方策ターゲットのコーパス接頭辞
PI_EPOCHS = int(os.environ.get("PI_EPOCHS", "20"))

from simulator.az_np import PVNetNP, ACTION_DIM


def main():
    X = np.load(CORPUS + "_X.npy"); Y = np.load(CORPUS + "_Y.npy")
    net = PVNetNP.load(IN)
    if net is None:
        sys.exit(f"ネットが読めない: {IN}")
    if net.dim != X.shape[1]:
        sys.exit(f"次元不一致: net={net.dim} corpus={X.shape[1]}（FEAT_V2/V3 を揃えること）")
    print(f"コーパス {len(X)}件 / ネット dim={net.dim} vbins={net.vbins}", flush=True)
    Wp0, bp0 = net.Wp.copy(), net.bp.copy()
    n = len(X); nte = max(1, int(n * 0.1)); ntr = n - nte

    def acc(a, b):
        _, v, _ = net._forward(X[a:b]); v = np.asarray(v).ravel()
        return float(((v >= 0.5) == (Y[a:b] >= 0.5)).mean()), float(((v - Y[a:b]) ** 2).mean())

    a0, b0 = acc(ntr, n)
    if PHASE == "head":
        # 表現層(W1/W2/W3)を凍結し、その出力 top の上で価値ヘッドだけをロジスティック回帰で学習。
        # 方策ヘッドは表現が動かないので一切壊れない。
        T = net._top(X[:ntr])[-1]
        Wv = net.Wv.copy(); bv = float(net.bv)
        rng = np.random.default_rng(0); B = 256
        for ep in range(EPOCHS):
            lr = 0.05 / (1.0 + 0.1 * ep)
            for s0 in range(0, ntr, B):
                bi = rng.permutation(ntr)[s0:s0 + B] if s0 == 0 else slice(s0, s0 + B)
                t = T[bi]; y = Y[:ntr][bi]
                v = 1.0 / (1.0 + np.exp(-(t @ Wv + bv)))
                g = (v - y) / len(y)
                Wv -= lr * (t.T @ g + 1e-5 * Wv); bv -= lr * g.sum()
        net.Wv, net.bv = Wv, bv
    else:
        A = np.zeros(ntr, dtype=int); M = np.ones((ntr, ACTION_DIM))
        net.train(X[:ntr], A, M, Y[:ntr], epochs=EPOCHS, lr=0.05, batch=256, seed=0)
    a1, b1 = acc(ntr, n)
    if PHASE == "joint" and PI_CORPUS:
        # 表現層が動いた分、方策ヘッドを MCTS の訪問分布で学習し直す（元に戻さない）。
        Xp = np.load(PI_CORPUS + "_X.npy"); PIp = np.load(PI_CORPUS + "_PI.npy")
        Mp = np.load(PI_CORPUS + "_M.npy"); Yp = np.load(PI_CORPUS + "_Y.npy")
        npt = max(1, int(len(Xp) * 0.1)); ntrp = len(Xp) - npt

        def ptop1(a, b):
            _, _, P = net._forward(Xp[a:b])
            P = np.asarray(P)
            P = np.where(Mp[a:b] > 0, P, -1e9)
            return float((P.argmax(1) == PIp[a:b].argmax(1)).mean())

        p0 = ptop1(ntrp, len(Xp))
        net.train_pi(Xp[:ntrp], PIp[:ntrp], Mp[:ntrp], Yp[:ntrp],
                     epochs=PI_EPOCHS, lr=0.05, batch=256, seed=0)
        p1 = ptop1(ntrp, len(Xp))
        print(f"方策: MCTSの手の top-1 的中 {p0*100:.1f}% → {p1*100:.1f}%  (n={npt})", flush=True)
    elif KEEP_POLICY:
        net.Wp, net.bp = Wp0, bp0
    net.save(OUT)
    print(f"価値: 的中 {a0*100:.1f}% → {a1*100:.1f}%   Brier {b0:.4f} → {b1:.4f}", flush=True)
    for tp in [t for t in os.environ.get("TEST", "").split(",") if t]:
        Xt = np.load(tp + "_X.npy"); Yt = np.load(tp + "_Y.npy")
        _, vt, _ = net._forward(Xt); vt = np.asarray(vt).ravel()
        ac = float(((vt >= 0.5) == (Yt >= 0.5)).mean()); br = float(((vt - Yt) ** 2).mean())
        print(f"  [test] {os.path.basename(tp):14s} n={len(Xt):6d}  的中 {ac*100:.1f}%  Brier {br:.4f}", flush=True)
    print(f"保存: {OUT}" + ("（方策ヘッドは元のまま）" if KEEP_POLICY else ""), flush=True)


if __name__ == "__main__":
    main()
