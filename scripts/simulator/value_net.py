"""学習価値関数（pure Python の小型MLP）。

自己対戦の (状態特徴, 最終勝敗) を教師に、状態から side1 の勝率を予測する評価関数を学習する。
隠れ層により天候×タイプ等の相互作用＝長期的戦略の価値を自分で学習できる（コンボの手書き不要）。
numpy 非依存（純Python・SGD）。重みは JSON で保存。
"""
import json
import math
import random
from pathlib import Path
from typing import List, Optional

WEIGHTS_PATH = Path(__file__).resolve().parent.parent / "value_net.json"


def make_value_fn(net: "ValueNet"):
    """ValueNet → SearchAI 用の value_fn(side1, side2, field)→P(side1勝利)。"""
    from .features import encode_state
    return lambda s1, s2, field: net.predict(encode_state(s1, s2, field))


def _sigmoid(z: float) -> float:
    if z < -60:
        return 0.0
    if z > 60:
        return 1.0
    return 1.0 / (1.0 + math.exp(-z))


class ValueNet:
    def __init__(self, dim: int, hidden: int = 24, seed: int = 0):
        self.dim = dim
        self.hidden = hidden
        rng = random.Random(seed)
        s1 = (1.0 / dim) ** 0.5
        s2 = (1.0 / hidden) ** 0.5
        self.W1 = [[rng.uniform(-s1, s1) for _ in range(dim)] for _ in range(hidden)]
        self.b1 = [0.0] * hidden
        self.W2 = [rng.uniform(-s2, s2) for _ in range(hidden)]
        self.b2 = 0.0

    def _forward(self, x: List[float]):
        h = []
        for j in range(self.hidden):
            z = self.b1[j]
            wj = self.W1[j]
            for i in range(self.dim):
                z += wj[i] * x[i]
            h.append(math.tanh(z))
        o = self.b2 + sum(self.W2[j] * h[j] for j in range(self.hidden))
        return h, _sigmoid(o)

    def predict(self, x: List[float]) -> float:
        return self._forward(x)[1]

    def train(self, samples, epochs: int = 20, lr: float = 0.05, l2: float = 1e-5,
              seed: int = 0, verbose: bool = False):
        rng = random.Random(seed)
        idx = list(range(len(samples)))
        for ep in range(epochs):
            lr_ep = lr / (1.0 + 0.15 * ep)   # 学習率減衰（収束安定化）
            rng.shuffle(idx)
            for k in idx:
                x, y = samples[k]
                h, p = self._forward(x)
                g = p - y                      # dL/do (BCE + sigmoid)
                # 出力層
                for j in range(self.hidden):
                    self.W2[j] -= lr_ep * (g * h[j] + l2 * self.W2[j])
                self.b2 -= lr_ep * g
                # 隠れ層
                for j in range(self.hidden):
                    dpre = g * self.W2[j] * (1.0 - h[j] * h[j])
                    wj = self.W1[j]
                    for i in range(self.dim):
                        wj[i] -= lr_ep * (dpre * x[i] + l2 * wj[i])
                    self.b1[j] -= lr_ep * dpre
            if verbose:
                print(f"  epoch {ep+1}/{epochs}  logloss={self.logloss(samples):.4f}", flush=True)

    def logloss(self, samples) -> float:
        s = 0.0
        for x, y in samples:
            p = self.predict(x)
            p = min(1 - 1e-9, max(1e-9, p))
            s += -(y * math.log(p) + (1 - y) * math.log(1 - p))
        return s / max(1, len(samples))

    def accuracy(self, samples) -> float:
        c = sum(1 for x, y in samples if (self.predict(x) >= 0.5) == (y >= 0.5))
        return c / max(1, len(samples))

    def save(self, path: Path = WEIGHTS_PATH):
        Path(path).write_text(json.dumps({
            "dim": self.dim, "hidden": self.hidden,
            "W1": self.W1, "b1": self.b1, "W2": self.W2, "b2": self.b2,
        }), encoding="utf-8")

    @classmethod
    def load(cls, path: Path = WEIGHTS_PATH) -> Optional["ValueNet"]:
        if not Path(path).exists():
            return None
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        net = cls(d["dim"], d["hidden"])
        net.W1, net.b1, net.W2, net.b2 = d["W1"], d["b1"], d["W2"], d["b2"]
        return net
