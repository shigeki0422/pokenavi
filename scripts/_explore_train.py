"""本番対局コーパス＋探索あり対局コーパスを混ぜた価値・方策の学習（_value_scale_train.py の複数コーパス版）。

CORPORA="名前=ディレクトリ[:対局数上限],..."（上限0/省略=全部）。検証は各コーパスの TEST 印の対局（訓練に入らない）と、
探索コーパスの TEST のうち選出率の低い種が出る局面（RM|RO）・抽選ターンの局面（XW）・抽選が無い局面（本番に近い）を別に出す。
best-epoch は訓練対局の3%（全コーパス合算）の検証 Brier で選ぶ。
PHASE: base / head / joint（_value_scale_train.py と同じ）。env: EPOCHS LR OUT VW TRAIN_SEED RESULTS BASE TAG
"""
import glob
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from simulator.az_np import PVNetNP
from _value_scale_train import metrics

CORPORA = os.environ["CORPORA"]
PHASE = os.environ.get("PHASE", "joint")
EPOCHS = int(os.environ.get("EPOCHS", "8"))
LR = float(os.environ.get("LR", "3e-4"))
OUT = os.environ.get("OUT", "")
VW = float(os.environ.get("VW", "1.0"))
BASE = os.environ.get("BASE", os.path.join(HERE, "az_net_np.json"))
SEED = int(os.environ.get("TRAIN_SEED", "1"))
RESULTS = os.environ.get("RESULTS", "")
TAG = os.environ.get("TAG", "")
EVAL_ONLY = os.environ.get("EVAL_NET", "")
PROD_RARE = os.environ.get("PROD_RARE", os.path.join(os.path.dirname(HERE), "_local", "ai_work", "explore_1003", "prod_test_rare.npz"))
KEYS = ("X", "Y", "PI", "M", "G", "TEST", "ME")
XKEYS = ("XW", "RM", "RO")


def load(d, cap):
    fs = sorted(glob.glob(os.path.join(d, "shards", "w*_c*.npz")))
    parts = {k: [] for k in KEYS + XKEYS}
    for f in fs:
        z = np.load(f)
        n = len(z["Y"])
        for k in KEYS:
            parts[k].append(z[k])
        for k in XKEYS:
            parts[k].append(z[k] if k in z.files else np.zeros(n, np.int8))
    D = {k: np.concatenate(v) for k, v in parts.items()}
    if not D["RM"].any() and os.path.exists(PROD_RARE):
        r = np.load(PROD_RARE)
        look = {int(g): (int(a), int(b)) for g, a, b in zip(r["G"], r["R1"], r["R2"])}
        rr = [look.get(int(g)) for g in D["G"]]
        D["RM"] = np.array([0 if x is None else x[me] for x, me in zip(rr, D["ME"])], np.int8)
        D["RO"] = np.array([0 if x is None else x[1 - me] for x, me in zip(rr, D["ME"])], np.int8)
    if cap:
        tr_g = np.unique(D["G"][D["TEST"] == 0])
        rng = np.random.default_rng(777)
        keep = set(rng.choice(tr_g, size=min(cap, len(tr_g)), replace=False).tolist())
        m = (D["TEST"] == 1) | np.isin(D["G"], np.fromiter(keep, np.int64))
        D = {k: v[m] for k, v in D.items()}
    return D


def sub(D, m):
    return D["X"][m], D["Y"][m], D["PI"][m], D["M"][m].astype(np.float64)


def evaluate(net, tests):
    out = {}
    for name, (X, Y, PI, M) in tests.items():
        if len(Y) == 0:
            continue
        m = metrics(net, X, Y, PI, M)
        out[name] = {k: round(v, 4) for k, v in m.items() if k in ("acc", "brier", "logloss", "ece", "extreme", "pol_top1")}
        out[name]["n"] = int(len(Y))
    return out


def _slot():
    import fcntl
    n = int(os.environ.get("TRAIN_SLOTS", "3"))
    d = os.path.join(os.path.dirname(HERE), "_local", "ai_work", "explore_1003", "locks")
    os.makedirs(d, exist_ok=True)
    while True:
        for i in range(n):
            f = open(os.path.join(d, f"slot{i}"), "w")
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return f
            except OSError:
                f.close()
        time.sleep(2)


def main():
    _lock = _slot()
    t0 = time.time()
    Ds = {}
    for spec in CORPORA.split(","):
        name, rest = spec.split("=")
        d, _, cap = rest.partition(":")
        Ds[name] = load(d, int(cap or 0))
    tests = {}
    tr_parts = {k: [] for k in KEYS}
    for name, D in Ds.items():
        te = D["TEST"] == 1
        tests[f"{name}"] = sub(D, te)
        if D["RM"].any():
            tests[f"{name}_rare"] = sub(D, te & ((D["RM"] == 1) | (D["RO"] == 1)))
        if D["XW"].any():
            tests[f"{name}_xw"] = sub(D, te & (D["XW"] == 1))
            tests[f"{name}_noxw"] = sub(D, te & (D["XW"] == 0))
        for k in KEYS:
            tr_parts[k].append(D[k][~te])
    T = {k: np.concatenate(v) for k, v in tr_parts.items()}
    del Ds
    G = T["G"]
    ug = np.unique(G)
    rng = np.random.default_rng(12345)
    rng.shuffle(ug)
    nval = max(200, int(len(ug) * 0.03))
    va = np.isin(G, ug[:nval])
    tr = ~va
    Xva, Yva, PIva, Mva = T["X"][va], T["Y"][va], T["PI"][va], T["M"][va].astype(np.float64)
    print(f"[{TAG}] 訓練 {tr.sum()}局面・{len(ug)-nval}対局 / 選択用 {va.sum()} / TEST " +
          " ".join(f"{k}:{len(v[1])}" for k, v in tests.items()) + f"  PHASE={PHASE}", flush=True)
    base = PVNetNP.load(EVAL_ONLY or BASE)
    if PHASE == "base":
        r = evaluate(base, tests)
        print("TEST", json.dumps(r, ensure_ascii=False), flush=True)
        _rec({"tag": TAG, "phase": "base", "net": EVAL_ONLY or BASE, "test": r})
        return
    X = T["X"][tr].astype(np.float64); Y = T["Y"][tr].astype(np.float64)
    PI = T["PI"][tr].astype(np.float64); M = T["M"][tr].astype(np.float64)
    del T
    net = PVNetNP.load(BASE)
    keys = ("W1", "b1", "W2", "b2", "Wv", "bv", "Wp", "bp")
    snap = lambda: {k: (getattr(net, k).copy() if hasattr(getattr(net, k), "copy") else getattr(net, k)) for k in keys}
    best = (metrics(net, Xva, Yva, PIva, Mva)["brier"], snap(), 0)
    curve = [{"ep": 0, "val_brier": best[0]}]
    print(f"  ep0 検証Brier {best[0]:.4f}", flush=True)
    if PHASE == "head":
        Tt = net._top(X)[-1]; Tva = net._top(Xva.astype(np.float64))[-1]
        Wv = np.array(net.Wv, float); bv = float(net.bv)
        st = {"m": np.zeros_like(Wv), "v": np.zeros_like(Wv), "mb": 0.0, "vb": 0.0, "t": 0}
        r = np.random.default_rng(SEED)
        for ep in range(EPOCHS):
            lr = LR * (0.5 ** (ep / max(EPOCHS / 3.0, 1.0)))
            perm = r.permutation(len(Tt))
            for s in range(0, len(Tt), 256):
                bi = perm[s:s + 256]
                v = 1.0 / (1.0 + np.exp(-(Tt[bi] @ Wv + bv)))
                g = (v - Y[bi]) / len(bi)
                gw = Tt[bi].T @ g + 1e-5 * Wv; gb = g.sum()
                st["t"] += 1; t = st["t"]
                st["m"] = 0.9 * st["m"] + 0.1 * gw; st["v"] = 0.999 * st["v"] + 0.001 * gw * gw
                st["mb"] = 0.9 * st["mb"] + 0.1 * gb; st["vb"] = 0.999 * st["vb"] + 0.001 * gb * gb
                c1 = 1 - 0.9 ** t; c2 = 1 - 0.999 ** t
                Wv -= lr * (st["m"] / c1) / (np.sqrt(st["v"] / c2) + 1e-8)
                bv -= lr * (st["mb"] / c1) / (np.sqrt(st["vb"] / c2) + 1e-8)
            vv = 1.0 / (1.0 + np.exp(-(Tva @ Wv + bv)))
            b = float(((vv - Yva) ** 2).mean())
            curve.append({"ep": ep + 1, "val_brier": b})
            print(f"  ep{ep+1} 検証Brier {b:.4f}", flush=True)
            if b < best[0]:
                net.Wv, net.bv = Wv.copy(), bv
                best = (b, snap(), ep + 1)
    else:
        for ep in range(EPOCHS):
            lr = LR * (0.5 ** (ep / max(EPOCHS / 3.0, 1.0)))
            net.train_pi(X, PI, M, Y, epochs=1, lr=lr, batch=256, seed=SEED * 1000 + ep,
                         optimizer="adam", l2=1e-5, value_weight=VW)
            m = metrics(net, Xva, Yva, PIva, Mva)
            curve.append({"ep": ep + 1, "val_brier": m["brier"], "val_acc": m["acc"], "val_top1": m["pol_top1"]})
            print(f"  ep{ep+1} 検証Brier {m['brier']:.4f} 的中 {m['acc']*100:.1f}% 方策top1 {m['pol_top1']*100:.1f}%  {time.time()-t0:.0f}s", flush=True)
            if m["brier"] < best[0]:
                best = (m["brier"], snap(), ep + 1)
    for k, v in best[1].items():
        setattr(net, k, v)
    r = evaluate(net, tests)
    print(f"TEST best_ep={best[2]}", json.dumps(r, ensure_ascii=False), f"{time.time()-t0:.0f}s", flush=True)
    if OUT:
        net._adam = None
        net.save(OUT)
        print(f"保存: {OUT}", flush=True)
    _rec({"tag": TAG, "phase": PHASE, "corpora": CORPORA, "train_games": int(len(ug) - nval), "samples": int(tr.sum()),
          "best_ep": best[2], "lr": LR, "epochs": EPOCHS, "out": OUT, "curve": curve, "test": r})


def _rec(d):
    if RESULTS:
        with open(RESULTS, "a") as f:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
