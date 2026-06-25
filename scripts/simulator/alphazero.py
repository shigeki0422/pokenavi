"""AlphaZero的な 方策＋価値ネット と PUCT-MCTS（pure Python・コンパクト版）。

- 二頭ネット PolicyValueNet: 状態特徴 → (方策prior over 行動, 価値=P(side1勝利))。
- 行動語彙(固定12次元): 技4枠×{通常,メガ}=8, 控え交代3枠, わるあがき1。
- PUCT-MCTS: 自分の意思決定ノードの木を張り、方策priorで選択を導き、価値ネットで葉を評価。
  相手は決定化（隠れ情報をbeliefからサンプル）して固定方策で環境として扱う（imperfect-info対応）。

完全なAlphaZeroの構造（policyをMCTSのpriorに、valueを葉評価に）を小規模で実現する。
"""
import copy
import math
import random
from typing import List, Optional

from .battle import Action, Battle, BattleSide, BattleField, is_trapped
from .features import encode_state, feature_dim
from .ai import (HeuristicAI, _filter_valid_by_lock, _filter_by_pp, _get_struggle,
                 _forced_charging_action)

ACTION_DIM = 12  # move0-3(no mega), move0-3(mega), switch slot0-2, struggle


class NetGreedyAI:
    """探索内の相手モデル: 相手手をネットの方策priorで選ぶ（中級＝ネット級の相手）。
    HeuristicAI（初級）相手の読みでは中級手筋に対処できないため、相手も賢い前提で読む。"""
    def __init__(self, net, temperature: float = 0.0, seed: int = 0):
        self.net = net
        self.temperature = temperature   # 0=argmax(決定的) / >0=方策priorから温度付きサンプリング
        self._rng = random.Random(seed)
        self._fallback = HeuristicAI()

    def __call__(self, my_side, opp_side, field):
        me = my_side.active
        if not me.is_alive:
            return Action(type="pass")
        forced = _forced_charging_action(me)
        if forced:
            return forced
        legal = legal_actions_indexed(my_side, opp_side, field)
        if not legal:
            return self._fallback(my_side, opp_side, field)
        try:
            prior, _ = self.net.evaluate(encode_state(my_side, opp_side, field),
                                         [ix for _, ix in legal])
        except Exception:
            return self._fallback(my_side, opp_side, field)
        if not prior:
            return legal[0][0]
        if self.temperature and self.temperature > 0:   # 温度付き: 重み w = p^(1/T)
            T = self.temperature
            acts = [(act, max(prior.get(ix, 0.0), 1e-9) ** (1.0 / T)) for act, ix in legal]
            tot = sum(w for _, w in acts)
            if tot > 0:
                r = self._rng.random() * tot
                for act, w in acts:
                    r -= w
                    if r <= 0:
                        return act
                return acts[-1][0]
        best = max(prior, key=prior.get)
        for act, ix in legal:
            if ix == best:
                return act
        return legal[0][0]


def legal_actions_indexed(my_side, opp_side, field):
    """(Action, action_index) の合法手リスト。SearchAI と整合した列挙。"""
    me = my_side.active
    can_mega = (me.mega_data is not None and not me.mega_evolved and not my_side.mega_used)
    valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
    valid = _filter_valid_by_lock(valid, me)
    pp_valid = _filter_by_pp(valid, me)
    out = []
    if not pp_valid:
        out.append((Action(type="move", move=_get_struggle(), move_idx=-1), 11))
    else:
        for i, mv in pp_valid:
            out.append((Action(type="move", move=mv, move_idx=i, do_mega=False), i))
            if can_mega:
                out.append((Action(type="move", move=mv, move_idx=i, do_mega=True), 4 + i))
    if not is_trapped(me, opp_side.active):
        for j, p in enumerate(my_side.party):
            if j != my_side.active_idx and p.is_alive and j < 3:
                out.append((Action(type="switch", switch_to=j), 8 + j))
    return out


def action_to_index(action) -> Optional[int]:
    """Action → 固定行動インデックス（記録/学習用）。pass等は None。"""
    if action.type == "switch":
        return 8 + action.switch_to if action.switch_to < 3 else None
    if action.type == "move":
        if action.move_idx == -1:
            return 11  # わるあがき
        if 0 <= action.move_idx < 4:
            return action.move_idx + (4 if action.do_mega else 0)
    return None


def _softmax(zs):
    m = max(zs)
    es = [math.exp(z - m) for z in zs]
    s = sum(es) or 1.0
    return [e / s for e in es]


class PolicyValueNet:
    """共有1隠れ層 → 価値(1, sigmoid) ＋ 方策(ACTION_DIM logits, softmax)。pure Python・SGD。"""

    def __init__(self, dim: int, hidden: int = 32, seed: int = 0):
        self.dim, self.hidden = dim, hidden
        rng = random.Random(seed)
        s1 = (1.0 / dim) ** 0.5
        sh = (1.0 / hidden) ** 0.5
        self.W1 = [[rng.uniform(-s1, s1) for _ in range(dim)] for _ in range(hidden)]
        self.b1 = [0.0] * hidden
        self.Wv = [rng.uniform(-sh, sh) for _ in range(hidden)]
        self.bv = 0.0
        self.Wp = [[rng.uniform(-sh, sh) for _ in range(hidden)] for _ in range(ACTION_DIM)]
        self.bp = [0.0] * ACTION_DIM

    def _hidden(self, x):
        h = []
        for j in range(self.hidden):
            z = self.b1[j]
            wj = self.W1[j]
            for i in range(self.dim):
                z += wj[i] * x[i]
            h.append(math.tanh(z))
        return h

    def evaluate(self, x, legal_idx):
        """→ (legal_idx上の方策prior dict, 価値[0,1])。"""
        h = self._hidden(x)
        ov = self.bv + sum(self.Wv[j] * h[j] for j in range(self.hidden))
        v = 1.0 / (1.0 + math.exp(-max(-60, min(60, ov))))
        logits = [self.bp[a] + sum(self.Wp[a][j] * h[j] for j in range(self.hidden)) for a in legal_idx]
        probs = _softmax(logits)
        return {a: p for a, p in zip(legal_idx, probs)}, v

    def train(self, samples, epochs: int = 12, lr: float = 0.05, l2: float = 1e-5,
              seed: int = 0, verbose: bool = False):
        """samples: (x, action_index, legal_idx_list, outcome)。価値=BCE, 方策=交差エントロピー。"""
        rng = random.Random(seed)
        idx = list(range(len(samples)))
        for ep in range(epochs):
            lr_ep = lr / (1.0 + 0.15 * ep)
            rng.shuffle(idx)
            for k in idx:
                x, a_taken, legal, y = samples[k]
                h = self._hidden(x)
                ov = self.bv + sum(self.Wv[j] * h[j] for j in range(self.hidden))
                v = 1.0 / (1.0 + math.exp(-max(-60, min(60, ov))))
                logits = {a: self.bp[a] + sum(self.Wp[a][j] * h[j] for j in range(self.hidden)) for a in legal}
                probs = dict(zip(legal, _softmax([logits[a] for a in legal])))
                # 勾配（隠れ層へ逆伝播する誤差を蓄積）
                dh = [0.0] * self.hidden
                gv = v - y
                for j in range(self.hidden):
                    dh[j] += gv * self.Wv[j]
                    self.Wv[j] -= lr_ep * (gv * h[j] + l2 * self.Wv[j])
                self.bv -= lr_ep * gv
                for a in legal:
                    gp = probs[a] - (1.0 if a == a_taken else 0.0)
                    for j in range(self.hidden):
                        dh[j] += gp * self.Wp[a][j]
                        self.Wp[a][j] -= lr_ep * (gp * h[j] + l2 * self.Wp[a][j])
                    self.bp[a] -= lr_ep * gp
                for j in range(self.hidden):
                    dpre = dh[j] * (1.0 - h[j] * h[j])
                    wj = self.W1[j]
                    for i in range(self.dim):
                        wj[i] -= lr_ep * (dpre * x[i] + l2 * wj[i])
                    self.b1[j] -= lr_ep * dpre
            if verbose:
                print(f"  epoch {ep+1}/{epochs}", flush=True)

    def policy_top1_acc(self, samples) -> float:
        c = 0
        for x, a_taken, legal, y in samples:
            pri, _ = self.evaluate(x, legal)
            if max(pri, key=pri.get) == a_taken:
                c += 1
        return c / max(1, len(samples))

    def value_acc(self, samples) -> float:
        c = 0
        for x, a_taken, legal, y in samples:
            _, v = self.evaluate(x, legal)
            c += (v >= 0.5) == (y >= 0.5)
        return c / max(1, len(samples))

    def save(self, path):
        import json
        from pathlib import Path
        Path(path).write_text(json.dumps({
            "dim": self.dim, "hidden": self.hidden, "W1": self.W1, "b1": self.b1,
            "Wv": self.Wv, "bv": self.bv, "Wp": self.Wp, "bp": self.bp}), encoding="utf-8")

    @classmethod
    def load(cls, path):
        import json
        from pathlib import Path
        if not Path(path).exists():
            return None
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        net = cls(d["dim"], d["hidden"])
        net.W1, net.b1 = d["W1"], d["b1"]
        net.Wv, net.bv, net.Wp, net.bp = d["Wv"], d["bv"], d["Wp"], d["bp"]
        return net


# ── PUCT-MCTS ──────────────────────────────────────────────────────────
class _Node:
    __slots__ = ("P", "N", "W", "children", "expanded", "acts")

    def __init__(self):
        self.P = {}; self.N = {}; self.W = {}; self.children = {}
        self.expanded = False; self.acts = {}


def _terminal_value(b, my_is_s1) -> float:
    if not b.side1.has_alive():
        return 0.0 if my_is_s1 else 1.0
    if not b.side2.has_alive():
        return 1.0 if my_is_s1 else 0.0
    return 0.5


def _puct(node, c_puct):
    sN = sum(node.N.values())
    best, bv = None, -1e9
    import math as _m
    for a in node.N:
        q = (node.W[a] / node.N[a]) if node.N[a] > 0 else 0.0
        u = c_puct * node.P.get(a, 0.0) * _m.sqrt(sN + 1) / (1 + node.N[a])
        if q + u > bv:
            bv = q + u; best = a
    return best


class _ForcedFirst:
    def __init__(self, action, fallback):
        self.action = action; self.fallback = fallback; self.used = False

    def __call__(self, my, opp, field):
        if not self.used:
            self.used = True
            return self.action
        return self.fallback(my, opp, field)


def _step_one_turn(b, my_action, opp_ai, my_is_s1):
    my_ai = _ForcedFirst(my_action, opp_ai)
    if my_is_s1:
        b.resume(my_ai, opp_ai, max_turns=b.turn + 1)
    else:
        b.resume(opp_ai, my_ai, max_turns=b.turn + 1)


def mcts_search(root_battle, my_is_s1, net, opp_ai, n_sims=30, c_puct=1.4, depth_cap=10,
                dir_eps=0.0, dir_alpha=0.3, temperature=0.0, return_pi=False, rng=None,
                switch_boost=0.0):
    """PUCT-MCTS。dir_eps>0 で根にDirichletノイズ（探索）、temperature>0 で訪問数比例サンプリング。
    switch_boost>0 で根の交代手(8-10)のpriorを底上げ＝交代探索を強める（positional学習用）。
    return_pi=True で (action, 訪問分布dict over ACTION_DIM) を返す（AlphaZero学習ターゲット用）。"""
    rng = rng or random
    root = _Node()
    for _ in range(n_sims):
        b = root_battle.clone()
        node = root
        path = []
        depth = 0
        while node.expanded:
            if not b.side1.has_alive() or not b.side2.has_alive():
                break
            a = _puct(node, c_puct)
            if a is None:
                break
            path.append((node, a))
            _step_one_turn(b, node.acts[a], opp_ai, my_is_s1)
            node = node.children.setdefault(a, _Node())
            depth += 1
            if depth >= depth_cap:
                break
        # 評価
        if not b.side1.has_alive() or not b.side2.has_alive():
            v = _terminal_value(b, my_is_s1)
        else:
            my_side, opp_side = (b.side1, b.side2) if my_is_s1 else (b.side2, b.side1)
            legal = legal_actions_indexed(my_side, opp_side, b.field)
            idxs = [ix for _, ix in legal]
            # 手番側(my_side)視点で符号化（ネットは actor をスロット1で学習済み）。
            # 価値・方策とも my_side のものになり、side2手番時の視点ズレ（潜在バグ）を解消。
            pri, v = net.evaluate(encode_state(my_side, opp_side, b.field), idxs)
            if not node.expanded and depth < depth_cap and idxs:
                node.P = pri
                node.acts = {ix: act for act, ix in legal}
                for ix in idxs:
                    node.N[ix] = 0; node.W[ix] = 0.0
                node.expanded = True
                # 根にDirichletノイズを混ぜて探索を促す（AlphaZero）
                if node is root and dir_eps > 0 and len(idxs) > 1:
                    noise = [rng.gammavariate(dir_alpha, 1.0) for _ in idxs]
                    ns = sum(noise) or 1.0
                    for ix, nz in zip(idxs, noise):
                        node.P[ix] = (1 - dir_eps) * node.P[ix] + dir_eps * (nz / ns)
                # 交代手のprior底上げ＝交代探索を強める（交代の過小評価を破る）
                if node is root and switch_boost > 0 and len(idxs) > 1:
                    sw = [ix for ix in idxs if 8 <= ix <= 10]
                    if sw and len(sw) < len(idxs):
                        for ix in sw:
                            node.P[ix] = node.P.get(ix, 0.0) + switch_boost
                        tot = sum(node.P.get(ix, 0.0) for ix in idxs) or 1.0
                        for ix in idxs:
                            node.P[ix] = node.P.get(ix, 0.0) / tot
        for nd, a in path:
            nd.N[a] += 1; nd.W[a] += v
    if not root.expanded or not root.N:
        return (None, {}) if return_pi else None
    total = sum(root.N.values()) or 1
    pi = {a: root.N[a] / total for a in root.N}
    if temperature and temperature > 0:
        weights = [root.N[a] ** (1.0 / temperature) for a in root.N]
        acts = list(root.N)
        wsum = sum(weights) or 1.0
        r = rng.random() * wsum
        best = acts[-1]
        for a, w in zip(acts, weights):
            r -= w
            if r <= 0:
                best = a; break
    else:
        best = max(root.N, key=lambda a: root.N[a])
    action = root.acts[best]
    return (action, pi) if return_pi else action


class PVMCTSAI:
    """方策＋価値ネットを用いた PUCT-MCTS の行動方策（AlphaZero型）。"""

    def __init__(self, loader, net, n_sims=30, season="M-2", opp_ai=None, seed=0):
        from .search_ai import SearchAI
        self.net = net
        self.n_sims = n_sims
        # 探索内の相手モデルは既定でネット（NetGreedyAI）＝AlphaZero的な賢い相手前提
        self.opp_ai = opp_ai or NetGreedyAI(net)
        self._fallback = HeuristicAI()
        self._det = SearchAI(loader, season=season, seed=seed)  # 決定化ヘルパーを借用

    def __call__(self, my_side, opp_side, field):
        from .ai import _forced_charging_action
        from .belief import OpponentBelief
        me = my_side.active
        if not me.is_alive:
            return Action(type="pass")
        forced = _forced_charging_action(me)
        if forced:
            return forced
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self._det.loader, self._det.season)
        belief.observe_disclosure(my_side.opp_view)
        my_is_s1 = (my_side.field_idx == 0)
        s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
        cs1, cs2, cfield = copy.deepcopy((s1, s2, field))
        copp = cs2 if my_is_s1 else cs1
        cfg = self._det._sample_opp_config(opp_side, belief)
        for poke, c in zip(copp.party, cfg):
            if c is not None:
                self._det._determinize(poke, c)
        b = Battle(cs1, cs2, cfield)
        act = mcts_search(b, my_is_s1, self.net, self.opp_ai, n_sims=self.n_sims)
        return act or self._fallback(my_side, opp_side, field)
