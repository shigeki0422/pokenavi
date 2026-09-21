"""numpy版 方策＋価値ネット（大規模・高速学習用）。

状態特徴 → (方策prior, 価値)。隠れ2層＋任意で3層目(hidden3)に対応＝大型化可能。
PVMCTSAI/SearchAI からは evaluate(x, legal_idx)→(prior_dict, value) として使える。
"""
import json
import os
from pathlib import Path

import numpy as np

from .alphazero import ACTION_DIM

# 既定は本番ネット。env AZNP_PATH で差し替えられる＝同じベンチで2つのネットを比較できる
# （ブランダーベンチ等は PVNetNP.load() を引数なしで呼ぶため、これが無いと比較できない）。
# 価値ヘッドのビン数。0=従来のスカラー(sigmoid)。両方の重みを読めるので切替は非破壊。
VALUE_BINS = int(os.environ.get("VALUE_BINS", "0"))
AZNP_PATH = Path(os.environ.get("AZNP_PATH")
                 or (Path(__file__).resolve().parent.parent / "az_net_np.json"))


class PVNetNP:
    def __init__(self, dim: int, hidden: int = 128, hidden2: int = 64, hidden3: int = 0, seed: int = 0,
                 act: str = "tanh", norm: bool = False):
        self.dim, self.hidden, self.hidden2, self.hidden3 = dim, hidden, hidden2, hidden3
        # act="relu"+norm=True+Adam で初めて訓練データに適合できる（tanh素SGDは2000件すら暗記できない）。
        # 既定は tanh/正規化なし＝既存ネットと完全に同一の前向き計算。
        self.act = act
        self.mu = np.zeros(dim) if norm else None
        self.sd = np.ones(dim) if norm else None
        self._adam = None
        self.opt = "sgd"      # "adam" で Adam（train/train_pi の optimizer= で切替）
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0, (1.0 / dim) ** 0.5, (hidden, dim)); self.b1 = np.zeros(hidden)
        self.W2 = rng.normal(0, (1.0 / hidden) ** 0.5, (hidden2, hidden)); self.b2 = np.zeros(hidden2)
        top = hidden2
        if hidden3:
            self.W3 = rng.normal(0, (1.0 / hidden2) ** 0.5, (hidden3, hidden2)); self.b3 = np.zeros(hidden3)
            top = hidden3
        # 価値ヘッド: 既定はスカラー(sigmoid)。VALUE_BINS>0 で two-hot 分類ヘッドにする。
        # スカラー回帰は最終勝敗0/1に対する平均を当てにいくので、勝率0.5付近の局面で
        # 勾配が潰れて「差がつかない」。分布で持つと接戦の局面でも形の違いを学習できる
        # （Metamon が最終段の性能向上を得た手法）。
        self.vbins = VALUE_BINS
        if self.vbins:
            self.Wv = rng.normal(0, (1.0 / top) ** 0.5, (self.vbins, top))
            self.bv = np.zeros(self.vbins)
            # ビン中心: [0,1] を等分した中点
            self.vcent = (np.arange(self.vbins) + 0.5) / self.vbins
        else:
            self.Wv = rng.normal(0, (1.0 / top) ** 0.5, top); self.bv = 0.0
        self.Wp = rng.normal(0, (1.0 / top) ** 0.5, (ACTION_DIM, top)); self.bp = np.zeros(ACTION_DIM)

    def _f(self, z):
        return np.maximum(z, 0.0) if self.act == "relu" else np.tanh(z)

    def _dfz(self, H):
        """活性の出力Hから微分を返す（tanh: 1-H^2 / relu: H>0）。"""
        return (H > 0).astype(float) if self.act == "relu" else (1.0 - H * H)

    def _nz(self, X):
        return X if self.mu is None else (X - self.mu) / self.sd

    def _top(self, X):
        """入力 → 最終隠れ層の活性（H1,H2[,H3] を計算し最上位を返す）。学習用に全活性も返す。"""
        X = self._nz(X)
        H1 = self._f(X @ self.W1.T + self.b1)
        H2 = self._f(H1 @ self.W2.T + self.b2)
        if self.hidden3:
            H3 = self._f(H2 @ self.W3.T + self.b3)
            return H1, H2, H3, H3
        return H1, H2, None, H2

    def _top_raw(self, Xn):
        """_top の正規化済み入力版（_step が二重正規化しないため）。"""
        H1 = self._f(Xn @ self.W1.T + self.b1)
        H2 = self._f(H1 @ self.W2.T + self.b2)
        if self.hidden3:
            H3 = self._f(H2 @ self.W3.T + self.b3)
            return H1, H2, H3, H3
        return H1, H2, None, H2

    def _value_from_top(self, top):
        """top表現 → 価値。two-hot のときは softmax の期待値を返す（下流はスカラーのまま）。"""
        if not self.vbins:
            return 1.0 / (1.0 + np.exp(-(top @ self.Wv + self.bv)))
        z = top @ self.Wv.T + self.bv
        z = z - z.max(axis=-1, keepdims=True)
        e = np.exp(z)
        pr = e / (e.sum(axis=-1, keepdims=True) + 1e-12)
        return pr @ self.vcent

    def _forward(self, X):
        *_, top = self._top(X)
        v = self._value_from_top(top)
        logits = top @ self.Wp.T + self.bp
        return top, v, logits

    def _two_hot(self, y):
        """スカラー目標 y∈[0,1] を隣接2ビンに線形配分した分布にする。"""
        n = self.vbins
        pos = np.clip(np.asarray(y, float) * n - 0.5, 0.0, n - 1.0)
        lo = np.floor(pos).astype(int); hi = np.minimum(lo + 1, n - 1)
        frac = pos - lo
        t = np.zeros((len(pos), n))
        idx = np.arange(len(pos))
        t[idx, lo] += 1.0 - frac
        t[idx, hi] += frac
        return t

    def evaluate(self, x, legal_idx):
        X = np.asarray(x, dtype=float).reshape(1, -1)
        _, v, logits = self._forward(X)
        lg = logits[0][legal_idx]; lg = lg - lg.max()
        e = np.exp(lg); p = e / (e.sum() or 1.0)
        return {a: float(pi) for a, pi in zip(legal_idx, p)}, float(v[0])

    def _step(self, xb, yb, mb, target, lr_ep, l2, value_weight=1.0):
        """1バッチの前向き＋逆伝播＋更新（2 or 3隠れ層）。value_weight=0で方策のみ学習。
        value_weight はサンプルごとの配列でもよい（価値だけ一部サンプルで学習する＝
        同一対局の局面が共有する勝敗ラベルの相関を、方策の学習量を落とさずに断てる）。"""
        B = len(xb)
        xb = self._nz(xb)
        H1, H2, H3, top = self._top_raw(xb)
        if self.vbins:
            zv = top @ self.Wv.T + self.bv
            zv = zv - zv.max(axis=1, keepdims=True)
            ev = np.exp(zv)
            pv = ev / (ev.sum(axis=1, keepdims=True) + 1e-12)
            v = pv @ self.vcent
        else:
            v = 1.0 / (1.0 + np.exp(-(top @ self.Wv + self.bv)))
        logits = np.where(mb > 0, top @ self.Wp.T + self.bp, -1e9)
        logits -= logits.max(1, keepdims=True)
        e = np.exp(logits) * mb
        P = e / (e.sum(1, keepdims=True) + 1e-12)
        # 合法手マスクが全0のサンプル（探索木の内部ノード＝方策ターゲットが無い）は
        # 方策の勾配を流さない。価値だけ学習する。
        gp = (P - target) * mb / B
        dWp = gp.T @ top; dbp = gp.sum(0)
        if self.vbins:
            # 交差エントロピー: 勾配は (予測分布 - two-hot目標)
            gv = value_weight * (pv - self._two_hot(yb)) / B
            dWv = gv.T @ top; dbv = gv.sum(0)
            dtop = gv @ self.Wv + gp @ self.Wp
        else:
            gv = value_weight * (v - yb) / B
            dWv = top.T @ gv; dbv = gv.sum()
            dtop = np.outer(gv, self.Wv) + gp @ self.Wp
        if self.hidden3:
            dpre3 = dtop * self._dfz(H3)
            dW3 = dpre3.T @ H2; db3 = dpre3.sum(0)
            dH2 = dpre3 @ self.W3
        else:
            dH2 = dtop
        dpre2 = dH2 * self._dfz(H2)
        dW2 = dpre2.T @ H1; db2 = dpre2.sum(0)
        dH1 = dpre2 @ self.W2
        dpre1 = dH1 * self._dfz(H1)
        dW1 = dpre1.T @ xb; db1 = dpre1.sum(0)
        grads = [("Wv", dWv + l2 * self.Wv), ("bv", dbv),
                 ("Wp", dWp + l2 * self.Wp), ("bp", dbp),
                 ("W2", dW2 + l2 * self.W2), ("b2", db2),
                 ("W1", dW1 + l2 * self.W1), ("b1", db1)]
        if self.hidden3:
            grads += [("W3", dW3 + l2 * self.W3), ("b3", db3)]
        if self.opt != "adam":
            for k, g in grads:
                setattr(self, k, getattr(self, k) - lr_ep * g)
            return
        if self._adam is None:
            self._adam = {"t": 0, "m": {}, "v": {}}
        st = self._adam; st["t"] += 1; t = st["t"]
        for k, g in grads:
            m = st["m"].get(k, 0.0) * 0.9 + 0.1 * g
            v = st["v"].get(k, 0.0) * 0.999 + 0.001 * g * g
            st["m"][k] = m; st["v"][k] = v
            mh = m / (1.0 - 0.9 ** t); vh = v / (1.0 - 0.999 ** t)
            setattr(self, k, getattr(self, k) - lr_ep * mh / (np.sqrt(vh) + 1e-8))

    def fit_norm(self, X):
        """入力正規化の統計を訓練データから決める（norm=True で作ったネットのみ有効）。"""
        if self.mu is None:
            return
        X = np.asarray(X, float)
        self.mu = X.mean(0); self.sd = X.std(0) + 1e-6

    def train(self, X, A, M, Y, epochs=30, lr=0.05, l2=1e-5, batch=256, seed=0, verbose=False,
              optimizer=None):
        if optimizer:
            self.opt = optimizer
        X = np.asarray(X, float); A = np.asarray(A, int); M = np.asarray(M, float); Y = np.asarray(Y, float)
        N = len(X); rng = np.random.default_rng(seed)
        onehot = np.zeros((N, ACTION_DIM)); onehot[np.arange(N), A] = 1.0
        for ep in range(epochs):
            lr_ep = lr / (1.0 + 0.1 * ep)
            perm = rng.permutation(N)
            for s in range(0, N, batch):
                bi = perm[s:s + batch]
                self._step(X[bi], Y[bi], M[bi], onehot[bi], lr_ep, l2)
            if verbose:
                print(f"  epoch {ep+1}/{epochs}  val_acc={self.value_acc(X,Y):.3f}", flush=True)

    def train_pi(self, X, PI, M, Y, epochs=20, lr=0.05, l2=1e-5, batch=256, seed=0, verbose=False,
                 value_weight=1.0, optimizer=None):
        """方策ターゲットが分布 PI（MCTS訪問分布）の学習。value_weight=0で方策のみ。"""
        if optimizer:
            self.opt = optimizer
        X = np.asarray(X, float); PI = np.asarray(PI, float); M = np.asarray(M, float); Y = np.asarray(Y, float)
        N = len(X); rng = np.random.default_rng(seed)
        for ep in range(epochs):
            lr_ep = lr / (1.0 + 0.1 * ep)
            perm = rng.permutation(N)
            for s in range(0, N, batch):
                bi = perm[s:s + batch]
                vw = value_weight[bi] if isinstance(value_weight, np.ndarray) else value_weight
                self._step(X[bi], Y[bi], M[bi], PI[bi], lr_ep, l2, vw)
            if verbose:
                print(f"  epoch {ep+1}/{epochs}  val_acc={self.value_acc(X,Y):.3f}", flush=True)

    def value_acc(self, X, Y):
        _, v, _ = self._forward(np.asarray(X, float))
        return float(((v >= 0.5) == (np.asarray(Y) >= 0.5)).mean())

    def policy_acc(self, X, A, M):
        _, _, logits = self._forward(np.asarray(X, float))
        logits = np.where(np.asarray(M) > 0, logits, -1e9)
        return float((logits.argmax(1) == np.asarray(A)).mean())

    def fold_norm(self):
        """入力正規化を第1層に畳み込む（W1/σ, b1 - W1·(μ/σ)）。以後 mu/sd は不要になる。
        第1層は線形なので出力は等価。入力のゼロがゼロのまま残るので、Rust 側の
        ゼロスキップ最適化（rows8_sparse）がそのまま使える。"""
        if self.mu is None:
            return self
        self.b1 = self.b1 - self.W1 @ (self.mu / self.sd)
        self.W1 = self.W1 / self.sd
        self.mu = None; self.sd = None
        return self

    def save(self, path=AZNP_PATH):
        d = {"dim": self.dim, "hidden": self.hidden, "hidden2": self.hidden2, "hidden3": self.hidden3,
             "W1": self.W1.tolist(), "b1": self.b1.tolist(),
             "W2": self.W2.tolist(), "b2": self.b2.tolist(),
             "vbins": self.vbins,
             "Wv": self.Wv.tolist(),
             "bv": (self.bv.tolist() if self.vbins else float(self.bv)),
             "Wp": self.Wp.tolist(), "bp": self.bp.tolist()}
        if self.act != "tanh":
            d["act"] = self.act
        if self.mu is not None:
            d["mu"] = self.mu.tolist(); d["sd"] = self.sd.tolist()
        if self.hidden3:
            d["W3"] = self.W3.tolist(); d["b3"] = self.b3.tolist()
        Path(path).write_text(json.dumps(d), encoding="utf-8")

    @classmethod
    def load(cls, path=AZNP_PATH):
        if not Path(path).exists():
            return None
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        net = cls(d["dim"], d["hidden"], d.get("hidden2", 64), d.get("hidden3", 0),
                  act=d.get("act", "tanh"), norm=("mu" in d))
        if "mu" in d:
            net.mu = np.array(d["mu"]); net.sd = np.array(d["sd"])
        net.W1 = np.array(d["W1"]); net.b1 = np.array(d["b1"])
        net.W2 = np.array(d["W2"]); net.b2 = np.array(d["b2"])
        # 価値ヘッドの形はファイル側に従う（env VALUE_BINS で作られた net と混ざらないように）
        net.vbins = int(d.get("vbins", 0) or 0)
        net.Wv = np.array(d["Wv"])
        net.bv = np.array(d["bv"]) if net.vbins else d["bv"]
        if net.vbins:
            net.vcent = (np.arange(net.vbins) + 0.5) / net.vbins
        net.Wp = np.array(d["Wp"]); net.bp = np.array(d["bp"])
        if d.get("hidden3"):
            net.W3 = np.array(d["W3"]); net.b3 = np.array(d["b3"])
        return net
