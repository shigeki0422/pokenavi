"""選出ポリシーの蒸留（A）。

B（nash_select_net＝学習ネット基準のオンザフライ選出ナッシュ）を教師に、
「自分6＋相手6の個体特徴 → 各自個体の選出確率・先頭確率」を予測する高速MLPを学習する。
特徴ベースなので任意パーティに汎化（party_id不要）。

使い方:
  python train_selection_policy.py gen [n_pairs] [workers]   # 教師データ生成 → selpolicy_data.jsonl
  python train_selection_policy.py train                     # データで学習 → selpolicy_net.json
  python train_selection_policy.py eval [n]                  # 蒸留選出 vs ヒューリスティック選出
"""
import os, sys, json, copy, random
import multiprocessing as mp
from pathlib import Path
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import select_party
from simulator.alphazero import NetGreedyAI
from simulator.selection import nash_select_net, candidate_selections, selection_to_party
from simulator.az_np import PVNetNP
from simulator.features import TYPES, _TI

DATA = Path(__file__).resolve().parent / "selpolicy_data.jsonl"
NET = Path(__file__).resolve().parent / "selpolicy_net.json"

# 設置/積み/回復/優先度/状態 を判定する技集合（features.py と同等の代表例）
from simulator.features import _M_SETUP, _M_RECOVER, _M_HAZARD, _M_STATUS


def poke_feat(p):
    """選出用の個体特徴（コンパクト）: タイプ18 + 全6実数値 + 能力フラグ5。"""
    tv = [0.0] * len(TYPES)
    for t in (p.type1, p.type2):
        if t in _TI:
            tv[_TI[t]] = 1.0
    stats = [p.max_hp / 250.0, p.attack / 300.0, p.defense / 300.0,
             p.sp_attack / 300.0, p.sp_defense / 300.0, p.speed / 300.0]
    setup = recover = hazard = pri = status = 0.0
    for mv in (p.moves or []):
        if not mv:
            continue
        if mv.power and mv.category != "status" and mv.priority and mv.priority > 0:
            pri = 1.0
        if mv.name_jp in _M_SETUP: setup = 1.0
        if mv.name_jp in _M_RECOVER: recover = 1.0
        if mv.name_jp in _M_HAZARD: hazard = 1.0
        if mv.name_jp in _M_STATUS: status = 1.0
    return tv + stats + [setup, recover, hazard, pri, status]


PF = len(TYPES) + 6 + 5   # =29 per poke
IN_DIM = 12 * PF          # my6 + opp6
IN_DIM_MM = IN_DIM + 12 * 3   # +マッチアップ3/個体（与ダメ最大・被ダメ最大・抜ける相手数）


def sample_features(my6, opp6):
    f = []
    for p in (my6 + opp6):
        f += poke_feat(p)
    return f


def matchup_features(my6, opp6):
    """各個体について相手集合との相性3次元（与ダメ最大・被ダメ最大・抜ける相手割合）。
    選出は本質的に相性勝負なので、個体特徴に加えてこの相互作用を与える。"""
    from simulator.features import _expected_frac
    from simulator.battle import BattleField
    fld = BattleField()
    out = []
    for side, other in ((my6, opp6), (opp6, my6)):
        for p in side:
            dealt = max([_expected_frac(p, o, fld) for o in other] or [0.0])
            taken = max([_expected_frac(o, p, fld) for o in other] or [0.0])
            try:
                faster = sum(1 for o in other if p.get_effective_speed() >= o.get_effective_speed()) / max(1, len(other))
            except Exception:
                faster = 0.0
            out += [min(1.5, dealt), min(1.5, taken), faster]
    return out


def sample_features_mm(my6, opp6):
    return sample_features(my6, opp6) + matchup_features(my6, opp6)


def _random_party(parties, loader, rng):
    """登録テンプレから6体をランダムに混ぜた“任意パーティ”を作る（汎化用）。"""
    pool = []
    for tpl in rng.sample(parties, min(6, len(parties))):
        pool += build_party(tpl, loader)
    rng.shuffle(pool)
    return pool[:6]


def _gen_worker(args):
    n, seed, use_random = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load()
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        if use_random:
            my6 = _random_party(parties, loader, rng); opp6 = _random_party(parties, loader, rng)
        else:
            pa, pb = rng.sample(parties, 2)
            my6 = build_party(pa, loader); opp6 = build_party(pb, loader)
        if len(my6) < 4 or len(opp6) < 3:
            continue
        sel, sels1, x, value = nash_select_net(my6, opp6, loader, net, k=6, samples=20,
                                               seed=seed, return_mix=True)
        if not sels1:
            continue
        incl = [0.0] * len(my6); lead = [0.0] * len(my6)
        for s, px in zip(sels1, x):
            for pos, idx in enumerate(s):
                if idx < len(my6):
                    incl[idx] += px
                    if pos == 0:
                        lead[idx] += px
        rows.append({"feat": sample_features(my6, opp6),
                     "feat_mm": sample_features_mm(my6, opp6),
                     "incl": incl + [0.0] * (6 - len(incl)),
                     "lead": lead + [0.0] * (6 - len(lead))})
    return rows


def gen(n_pairs=120, workers=None):
    workers = workers or max(1, (os.cpu_count() or 2) - 1)
    per = max(1, n_pairs // workers)
    # 半分はランダムパーティ（汎化）、半分は登録パーティ
    args = [(per, 1000 + w, (w % 2 == 0)) for w in range(workers)]
    ctx = mp.get_context("spawn")
    rows = []
    with ctx.Pool(workers) as pool:
        for res in pool.map(_gen_worker, args):
            rows += res
    # 追記モード（夜間バッチを重ねて蓄積）
    with open(DATA, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    total = sum(1 for _ in open(DATA, encoding="utf-8"))
    print(f"教師データ生成: +{len(rows)}件 追記 / 累計{total}件 → {DATA}", flush=True)


class SelNet:
    """入力(12体特徴) → 各自個体6の (選出スコア, 先頭スコア)。"""
    def __init__(self, dim, hidden=128, seed=0):
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0, (1/dim)**0.5, (hidden, dim)); self.b1 = np.zeros(hidden)
        self.Wi = rng.normal(0, (1/hidden)**0.5, (6, hidden)); self.bi = np.zeros(6)
        self.Wl = rng.normal(0, (1/hidden)**0.5, (6, hidden)); self.bl = np.zeros(6)
        self.dim, self.hidden = dim, hidden

    def _fwd(self, X):
        H = np.tanh(X @ self.W1.T + self.b1)
        incl = 1/(1+np.exp(-(H @ self.Wi.T + self.bi)))
        lead_logit = H @ self.Wl.T + self.bl
        return H, incl, lead_logit

    def predict(self, x):
        H, incl, ll = self._fwd(np.asarray(x, float).reshape(1, -1))
        return incl[0], ll[0]

    def train(self, X, INCL, LEAD, epochs=120, lr=0.05, batch=128, seed=0):
        X = np.asarray(X, float); INCL = np.asarray(INCL, float); LEAD = np.asarray(LEAD, float)
        N = len(X); rng = np.random.default_rng(seed)
        for ep in range(epochs):
            lr_e = lr / (1 + 0.05 * ep)
            for s in range(0, N, batch):
                bi = rng.permutation(N)[s:s+batch]
                xb, ib, lb = X[bi], INCL[bi], LEAD[bi]; B = len(bi)
                H, incl, ll = self._fwd(xb)
                gi = (incl - ib) / B
                e = np.exp(ll - ll.max(1, keepdims=True)); P = e / e.sum(1, keepdims=True)
                gl = (P - lb) / B
                dWi = gi.T @ H; dbi = gi.sum(0); dWl = gl.T @ H; dbl = gl.sum(0)
                dH = gi @ self.Wi + gl @ self.Wl
                dpre = dH * (1 - H*H)
                dW1 = dpre.T @ xb; db1 = dpre.sum(0)
                self.Wi -= lr_e*dWi; self.bi -= lr_e*dbi
                self.Wl -= lr_e*dWl; self.bl -= lr_e*dbl
                self.W1 -= lr_e*dW1; self.b1 -= lr_e*db1

    def save(self, path=NET):
        Path(path).write_text(json.dumps({"dim": self.dim, "hidden": self.hidden,
            "W1": self.W1.tolist(), "b1": self.b1.tolist(), "Wi": self.Wi.tolist(),
            "bi": self.bi.tolist(), "Wl": self.Wl.tolist(), "bl": self.bl.tolist()}), encoding="utf-8")

    @classmethod
    def load(cls, path=NET):
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        n = cls(d["dim"], d["hidden"]); n.W1=np.array(d["W1"]); n.b1=np.array(d["b1"])
        n.Wi=np.array(d["Wi"]); n.bi=np.array(d["bi"]); n.Wl=np.array(d["Wl"]); n.bl=np.array(d["bl"])
        return n


NET_MM = Path(__file__).resolve().parent / "selpolicy_net_mm.json"


def policy_select(model, my6, opp6, mm=False):
    """蒸留モデルで3体選出（top3＋先頭）。任意パーティ対応。mm=Trueでマッチアップ特徴版。"""
    feat = sample_features_mm(my6, opp6) if mm else sample_features(my6, opp6)
    incl, ll = model.predict(feat)
    n = len(my6)
    order = sorted(range(n), key=lambda i: incl[i], reverse=True)[:3]
    lead = max(order, key=lambda i: ll[i])
    sel = [lead] + [i for i in order if i != lead]
    return selection_to_party(my6, sel)


def train(mm=False):
    key = "feat_mm" if mm else "feat"
    rows = [json.loads(l) for l in open(DATA, encoding="utf-8")]
    rows = [r for r in rows if key in r]
    X = [r[key] for r in rows]; INCL = [r["incl"] for r in rows]; LEAD = [r["lead"] for r in rows]
    dim = IN_DIM_MM if mm else IN_DIM
    m = SelNet(dim, 128, seed=0)
    m.train(X, INCL, LEAD, epochs=150)
    m.save(NET_MM if mm else NET)
    print(f"選出ポリシー学習完了({'mm' if mm else 'v1'}): {len(rows)}件 → {NET_MM if mm else NET}", flush=True)


def evaluate(n=8, mm=False):
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load(); model = SelNet.load(NET_MM if mm else NET); rng = random.Random(999)
    def winrate(my3, opp3, M=50, seed=0):
        w = 0
        for k in range(M):
            s1 = BattleSide([copy.deepcopy(p) for p in my3]); s2 = BattleSide([copy.deepcopy(p) for p in opp3])
            s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
            if Battle(s1, s2).run(NetGreedyAI(net), NetGreedyAI(net)) == 1: w += 1
        return w / M
    pt = ht = 0
    for i in range(n):
        random.seed(7000 + i)   # パーティ生成を再現可能に（v1/v2/heuristicを同一パーティで比較）
        my6 = _random_party(parties, loader, rng); opp6 = _random_party(parties, loader, rng)
        opp_h = select_party(opp6, my6, loader)
        wh = winrate(select_party(my6, opp6, loader), opp_h, seed=i)
        wp = winrate(policy_select(model, my6, opp6, mm=mm), opp_h, seed=i)
        ht += wh; pt += wp
        print(f"対{i+1}: ヒュ選出 {wh:.0%} / 蒸留選出({'mm' if mm else 'v1'}) {wp:.0%}", flush=True)
    print(f"平均(ランダムパーティ): ヒューリスティック {ht/n:.1%} → 蒸留({'mm' if mm else 'v1'}) {pt/n:.1%}", flush=True)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "gen"
    if cmd == "gen":
        gen(int(sys.argv[2]) if len(sys.argv) > 2 else 120,
            int(sys.argv[3]) if len(sys.argv) > 3 else None)
    elif cmd == "train":
        train()
    elif cmd == "train_mm":
        train(mm=True)
    elif cmd == "eval":
        evaluate(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
    elif cmd == "eval_mm":
        evaluate(int(sys.argv[2]) if len(sys.argv) > 2 else 8, mm=True)
