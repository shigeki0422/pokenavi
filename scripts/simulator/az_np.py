"""numpy版 方策＋価値ネット（大規模・高速学習用）。

状態特徴 → (方策prior, 価値)。隠れ2層＋任意で3層目(hidden3)に対応＝大型化可能。
PVMCTSAI/SearchAI からは evaluate(x, legal_idx)→(prior_dict, value) として使える。
"""
import json
from pathlib import Path

import numpy as np

from .alphazero import ACTION_DIM

AZNP_PATH = Path(__file__).resolve().parent.parent / "az_net_np.json"


class PVNetNP:
    def __init__(self, dim: int, hidden: int = 128, hidden2: int = 64, hidden3: int = 0, seed: int = 0):
        self.dim, self.hidden, self.hidden2, self.hidden3 = dim, hidden, hidden2, hidden3
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0, (1.0 / dim) ** 0.5, (hidden, dim)); self.b1 = np.zeros(hidden)
        self.W2 = rng.normal(0, (1.0 / hidden) ** 0.5, (hidden2, hidden)); self.b2 = np.zeros(hidden2)
        top = hidden2
        if hidden3:
            self.W3 = rng.normal(0, (1.0 / hidden2) ** 0.5, (hidden3, hidden2)); self.b3 = np.zeros(hidden3)
            top = hidden3
        self.Wv = rng.normal(0, (1.0 / top) ** 0.5, top); self.bv = 0.0
        self.Wp = rng.normal(0, (1.0 / top) ** 0.5, (ACTION_DIM, top)); self.bp = np.zeros(ACTION_DIM)

    def _top(self, X):
        """入力 → 最終隠れ層の活性（H1,H2[,H3] を計算し最上位を返す）。学習用に全活性も返す。"""
        H1 = np.tanh(X @ self.W1.T + self.b1)
        H2 = np.tanh(H1 @ self.W2.T + self.b2)
        if self.hidden3:
            H3 = np.tanh(H2 @ self.W3.T + self.b3)
            return H1, H2, H3, H3
        return H1, H2, None, H2

    def _forward(self, X):
        *_, top = self._top(X)
        v = 1.0 / (1.0 + np.exp(-(top @ self.Wv + self.bv)))
        logits = top @ self.Wp.T + self.bp
        return top, v, logits

    def evaluate(self, x, legal_idx):
        X = np.asarray(x, dtype=float).reshape(1, -1)
        _, v, logits = self._forward(X)
        lg = logits[0][legal_idx]; lg = lg - lg.max()
        e = np.exp(lg); p = e / (e.sum() or 1.0)
        return {a: float(pi) for a, pi in zip(legal_idx, p)}, float(v[0])

    def _step(self, xb, yb, mb, target, lr_ep, l2, value_weight=1.0):
        """1バッチの前向き＋逆伝播＋更新（2 or 3隠れ層）。value_weight=0で方策のみ学習。"""
        B = len(xb)
        H1, H2, H3, top = self._top(xb)
        v = 1.0 / (1.0 + np.exp(-(top @ self.Wv + self.bv)))
        logits = np.where(mb > 0, top @ self.Wp.T + self.bp, -1e9)
        logits -= logits.max(1, keepdims=True)
        e = np.exp(logits) * mb
        P = e / (e.sum(1, keepdims=True) + 1e-12)
        gv = value_weight * (v - yb) / B
        gp = (P - target) * mb / B
        dWv = top.T @ gv; dbv = gv.sum()
        dWp = gp.T @ top; dbp = gp.sum(0)
        dtop = np.outer(gv, self.Wv) + gp @ self.Wp
        if self.hidden3:
            dpre3 = dtop * (1.0 - H3 * H3)
            dW3 = dpre3.T @ H2; db3 = dpre3.sum(0)
            dH2 = dpre3 @ self.W3
        else:
            dH2 = dtop
        dpre2 = dH2 * (1.0 - H2 * H2)
        dW2 = dpre2.T @ H1; db2 = dpre2.sum(0)
        dH1 = dpre2 @ self.W2
        dpre1 = dH1 * (1.0 - H1 * H1)
        dW1 = dpre1.T @ xb; db1 = dpre1.sum(0)
        self.Wv -= lr_ep * (dWv + l2 * self.Wv); self.bv -= lr_ep * dbv
        self.Wp -= lr_ep * (dWp + l2 * self.Wp); self.bp -= lr_ep * dbp
        if self.hidden3:
            self.W3 -= lr_ep * (dW3 + l2 * self.W3); self.b3 -= lr_ep * db3
        self.W2 -= lr_ep * (dW2 + l2 * self.W2); self.b2 -= lr_ep * db2
        self.W1 -= lr_ep * (dW1 + l2 * self.W1); self.b1 -= lr_ep * db1

    def train(self, X, A, M, Y, epochs=30, lr=0.05, l2=1e-5, batch=256, seed=0, verbose=False):
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

    def train_pi(self, X, PI, M, Y, epochs=20, lr=0.05, l2=1e-5, batch=256, seed=0, verbose=False, value_weight=1.0):
        """方策ターゲットが分布 PI（MCTS訪問分布）の学習。value_weight=0で方策のみ。"""
        X = np.asarray(X, float); PI = np.asarray(PI, float); M = np.asarray(M, float); Y = np.asarray(Y, float)
        N = len(X); rng = np.random.default_rng(seed)
        for ep in range(epochs):
            lr_ep = lr / (1.0 + 0.1 * ep)
            perm = rng.permutation(N)
            for s in range(0, N, batch):
                bi = perm[s:s + batch]
                self._step(X[bi], Y[bi], M[bi], PI[bi], lr_ep, l2, value_weight)
            if verbose:
                print(f"  epoch {ep+1}/{epochs}  val_acc={self.value_acc(X,Y):.3f}", flush=True)

    def value_acc(self, X, Y):
        _, v, _ = self._forward(np.asarray(X, float))
        return float(((v >= 0.5) == (np.asarray(Y) >= 0.5)).mean())

    def policy_acc(self, X, A, M):
        _, _, logits = self._forward(np.asarray(X, float))
        logits = np.where(np.asarray(M) > 0, logits, -1e9)
        return float((logits.argmax(1) == np.asarray(A)).mean())

    def save(self, path=AZNP_PATH):
        d = {"dim": self.dim, "hidden": self.hidden, "hidden2": self.hidden2, "hidden3": self.hidden3,
             "W1": self.W1.tolist(), "b1": self.b1.tolist(),
             "W2": self.W2.tolist(), "b2": self.b2.tolist(),
             "Wv": self.Wv.tolist(), "bv": float(self.bv),
             "Wp": self.Wp.tolist(), "bp": self.bp.tolist()}
        if self.hidden3:
            d["W3"] = self.W3.tolist(); d["b3"] = self.b3.tolist()
        Path(path).write_text(json.dumps(d), encoding="utf-8")

    @classmethod
    def load(cls, path=AZNP_PATH):
        if not Path(path).exists():
            return None
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        net = cls(d["dim"], d["hidden"], d.get("hidden2", 64), d.get("hidden3", 0))
        net.W1 = np.array(d["W1"]); net.b1 = np.array(d["b1"])
        net.W2 = np.array(d["W2"]); net.b2 = np.array(d["b2"])
        net.Wv = np.array(d["Wv"]); net.bv = d["bv"]
        net.Wp = np.array(d["Wp"]); net.bp = np.array(d["bp"])
        if d.get("hidden3"):
            net.W3 = np.array(d["W3"]); net.b3 = np.array(d["b3"])
        return net
