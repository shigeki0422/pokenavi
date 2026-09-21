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
ARCH = os.environ.get("ARCH", "512x256")   # PHASE=fresh の隠れ層
LR = float(os.environ.get("LR", "1e-3"))
# 方策ヘッドは勝率にほぼ寄与しない（実測: 新方策+本番価値=50.6%）。胴体を共有しているので、
# 価値の重みを上げると同じ容量とデータを価値の学習に振り向けられる。
VALUE_WEIGHT = float(os.environ.get("VALUE_WEIGHT", "1.0"))

from simulator.az_np import PVNetNP, ACTION_DIM


def _lambda_return(G, Y, Q, lam):
    """λ収益: 同じ手番側の n 手先の探索評価 Q を混ぜ、終端は最終勝敗 Y に接続する。

    λ=0 なら Q そのもの（1ステップのブートストラップ＝探索の結論の丸写し・自己回帰）、
    λ=1 なら最終勝敗そのもの（分散大・同一対局で共有）。中間は「決着に近い局面ほど 0/1 に寄る」
    RL の標準的な価値になり、局面ごとに値が変わるので相関も切れる。

    記録は対局内で時系列順。Y はその手番側が最終的に勝ったかなので、**手番側の識別子**として使える
    （勝者側の記録は Y=1、敗者側は Y=0）。同じ Y を持つ記録を辿れば同一視点の系列になる。
    """
    out = np.array(Y, dtype=float)
    order = np.argsort(G, kind="stable")
    gs = G[order]
    for seg in np.split(order, np.flatnonzero(np.diff(gs)) + 1):
        for side in (0.0, 1.0):
            idx = seg[Y[seg] == side]
            if len(idx) == 0:
                continue
            q = Q[idx]
            # 後ろから: g_k = (1-λ)·Q(k+1) + λ·g_{k+1}、終端は最終勝敗
            g = float(side)
            for k in range(len(idx) - 1, -1, -1):
                out[idx[k]] = (1.0 - lam) * q[k] + lam * g if k < len(idx) - 1 else \
                    (1.0 - lam) * q[k] + lam * float(side)
                g = out[idx[k]]
    return out


_VALUE_W: list = []   # VALUE_PER_GAME 使用時のサンプルごとの価値重み（訓練コーパス分のみ）


def _load_pi(prefixes):
    """カンマ区切りの複数コーパスを連結して (X, PI, M, Y) を返す。
    VALUE_TARGET=q で価値ターゲットを探索の根の価値 Q にする（最終勝敗と違い局面ごとに値が変わる＝
    同一対局内の相関が切れる）。mix:0.5 で Y と Q の加重平均。PER_GAME_PICK=k で対局ごとに k 件へ間引く。"""
    parts = [p for p in prefixes.split(",") if p]

    def cat(suf):
        return np.concatenate([np.load(p + suf) for p in parts])

    X, PI, M, Y = cat("_X.npy"), cat("_PI.npy"), cat("_M.npy"), cat("_Y.npy")
    tgt = os.environ.get("VALUE_TARGET", "y")
    if tgt != "y":
        Q = cat("_Q.npy")
        if tgt == "q":
            Y = Q
        elif tgt.startswith("mix:"):
            w = float(tgt.split(":", 1)[1])
            Y = (1.0 - w) * Y + w * Q
        elif tgt.startswith("lam:"):
            Y = _lambda_return(cat("_G.npy"), Y, Q, float(tgt.split(":", 1)[1]))
    vk = int(os.environ.get("VALUE_PER_GAME", "0") or 0)
    if vk:
        G = cat("_G.npy")
        rng = np.random.default_rng(11)
        w = np.zeros(len(X))
        order = np.argsort(G, kind="stable"); gs = G[order]
        ng = 0
        for seg in np.split(order, np.flatnonzero(np.diff(gs)) + 1):
            ng += 1
            pick = seg if len(seg) <= vk else rng.choice(seg, vk, replace=False)
            w[pick] = 1.0
        # 学習量を保つため、選ばれた局面の重みを (全件/選択件) 倍にする
        w *= len(X) / max(w.sum(), 1.0)
        _VALUE_W.append(w)
        print(f"価値は1対局{vk}局面のみ学習: {int((w>0).sum())}/{len(X)}件（対局数 {ng}）", flush=True)
    k = int(os.environ.get("PER_GAME_PICK", "0") or 0)
    if k:
        G = cat("_G.npy")
        rng = np.random.default_rng(7)
        keep = []
        order = np.argsort(G, kind="stable")
        gs = G[order]
        bounds = np.flatnonzero(np.diff(gs)) + 1
        for seg in np.split(order, bounds):
            keep.append(seg if len(seg) <= k else rng.choice(seg, k, replace=False))
        idx = np.sort(np.concatenate(keep))
        X, PI, M, Y = X[idx], PI[idx], M[idx], Y[idx]
        print(f"対局ごとに最大{k}件へ間引き: {len(G)} → {len(X)}件（対局数 {len(np.unique(G))}）", flush=True)
    return X, PI, M, Y


def _fresh():
    """Adam+ReLU+入力正規化で新規ネットを学習する（既存ネットは tanh/素SGD なので転移できない）。"""
    X, PI, M, Y = _load_pi(PI_CORPUS)
    ntr_cap = int(os.environ.get("NTRAIN", "0") or 0)
    if ntr_cap and ntr_cap < len(X):
        # SUBSAMPLE=random: 全体から一様抽出＝1対局あたり平均1局面になり、局面間の相関が切れる。
        # 既定（先頭から連続）は同じ対局の局面が固まって入る＝AlphaGo が過学習した条件。
        if os.environ.get("SUBSAMPLE") == "random":
            ix = np.random.default_rng(12345).choice(len(X), ntr_cap, replace=False)
            ix.sort()
        else:
            ix = np.arange(ntr_cap)
        X, PI, M, Y = X[ix], PI[ix], M[ix], Y[ix]
    h1, h2 = (int(v) for v in ARCH.split("x"))
    rng = np.random.default_rng(0)
    perm = rng.permutation(len(X))
    X, PI, M, Y = X[perm], PI[perm], M[perm], Y[perm]
    # 同一対戦の局面は価値ラベルを共有するので、ランダム分割だとリークして価値精度が水増しされる。
    # PI_TEST に別生成のコーパスを渡して評価する。
    PI_TEST = os.environ.get("PI_TEST", "")
    if PI_TEST:
        Xv, PIv, Mv, Yv = _load_pi(PI_TEST)
        nte_cap = int(os.environ.get("NTEST", "0") or 0)
        if nte_cap and nte_cap < len(Xv):
            Xv, PIv, Mv, Yv = Xv[:nte_cap], PIv[:nte_cap], Mv[:nte_cap], Yv[:nte_cap]
        ntr = len(X)
        X = np.concatenate([X, Xv]); PI = np.concatenate([PI, PIv])
        M = np.concatenate([M, Mv]); Y = np.concatenate([Y, Yv])
        nte = len(Xv)
    else:
        nte = max(1, int(len(X) * 0.1)); ntr = len(X) - nte
    net = PVNetNP(X.shape[1], hidden=h1, hidden2=h2, seed=1, act="relu", norm=True)
    net.fit_norm(X[:ntr])
    _VW = None
    if _VALUE_W:
        # 訓練コーパスの読み込み時に作った重みを、シャッフル後の並びに合わせる
        w = np.concatenate([_VALUE_W[0], np.zeros(len(X) - len(_VALUE_W[0]))])
        _VW = w[perm][:ntr]
    print(f"fresh {h1}x{h2} relu+norm+adam  訓練{ntr}件 / 検証{nte}件"
          + ("（別コーパス）" if PI_TEST else "（同一コーパスの1割・価値はリークあり）"), flush=True)

    def stat(a, b):
        _, v, P = net._forward(X[a:b]); v = np.asarray(v).ravel()
        P = np.where(M[a:b] > 0, np.asarray(P), -1e9)
        return (float((P.argmax(1) == PI[a:b].argmax(1)).mean()),
                float(((v >= 0.5) == (Y[a:b] >= 0.5)).mean()))

    best = (0.0, None)
    for ep in range(PI_EPOCHS):
        lr = LR * (0.5 ** (ep / max(PI_EPOCHS / 3.0, 1.0)))
        net.train_pi(X[:ntr], PI[:ntr], M[:ntr], Y[:ntr], epochs=1, lr=lr, batch=128,
                     seed=ep, optimizer="adam",
                     value_weight=_VW if _VW is not None else VALUE_WEIGHT)
        if (ep + 1) % 5 == 0 or ep == PI_EPOCHS - 1:
            p1, a1 = stat(ntr, ntr + nte)
            ptr, _ = stat(0, min(ntr, 5000))
            print(f"  ep{ep+1:3d} 訓練top1 {ptr*100:5.1f}%  検証top1 {p1*100:5.1f}%  価値 {a1*100:5.1f}%", flush=True)
            if p1 > best[0]:
                best = (p1, {k: (getattr(net, k).copy() if hasattr(getattr(net, k), "copy") else getattr(net, k))
                             for k in ("W1", "b1", "W2", "b2", "Wv", "bv", "Wp", "bp")})
    if best[1]:
        for k, v in best[1].items():
            setattr(net, k, v)
    net.save(OUT)
    print(f"保存: {OUT}  検証best top1 {best[0]*100:.1f}%", flush=True)


def main():
    if PHASE == "fresh":
        return _fresh()
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
