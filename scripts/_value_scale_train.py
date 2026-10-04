"""対局数を変えた価値ヘッドの学習曲線（_gen_value_corpus_big.py のコーパス）。

検証は対局単位で分けた TEST 印の対局（訓練と同じ対局の局面は入らない）。訓練対局の 3% を best-epoch 選択用に取り分ける。
PHASE:
  base   本番ネットをそのまま評価（基準）
  head   本番ネットの表現（W1/W2）を凍結し価値ヘッド（Wv,bv）だけ Adam で学習。方策は不変
  joint  本番ネットから全層を価値（最終勝敗）＋方策（根の訪問分布）で同時に微調整（Adam）
  fresh  ReLU＋入力正規化の新規ネットを価値＋方策で学習（保存時に正規化を W1 に畳み込む＝Rust で読める）
env: CORPUS  NGAMES(訓練対局数の上限・0=全部)  PHASE  EPOCHS  LR  OUT  ARCH(fresh: 256x128)  VW(価値の重み 1.0)
     USE_PER_GAME(1 or 2: 1対局から使う局面数)  BASE(本番ネット)  TRAIN_SEED(1)  RESULTS(結果を1行JSONで追記)
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

CORPUS = os.environ.get("CORPUS", os.path.join(os.path.dirname(HERE), "_local", "ai_work", "valcorpus_20261002"))
NGAMES = int(os.environ.get("NGAMES", "0"))
PHASE = os.environ.get("PHASE", "head")
EPOCHS = int(os.environ.get("EPOCHS", "10"))
LR = float(os.environ.get("LR", "3e-4"))
OUT = os.environ.get("OUT", "")
ARCH = os.environ.get("ARCH", "256x128")
VW = float(os.environ.get("VW", "1.0"))
USE_PER_GAME = int(os.environ.get("USE_PER_GAME", "2"))
BASE = os.environ.get("BASE", os.path.join(HERE, "az_net_np.json"))
SEED = int(os.environ.get("TRAIN_SEED", "1"))
RESULTS = os.environ.get("RESULTS", "")
MAX_SHARDS = int(os.environ.get("MAX_SHARDS", "0"))


def load():
    fs = sorted(glob.glob(os.path.join(CORPUS, "shards", "w*_c*.npz")))
    if MAX_SHARDS:
        fs = fs[:MAX_SHARDS]
    parts = {k: [] for k in ("X", "Y", "PI", "M", "G", "T", "TEST")}
    games = 0
    for f in fs:
        d = np.load(f)
        games += int(d["META"][0])
        for k in parts:
            parts[k].append(d[k])
    D = {k: np.concatenate(v) for k, v in parts.items()}
    return D, games, len(fs)


def metrics(net, X, Y, PI, M):
    out_v = []; out_p = []
    for s in range(0, len(X), 20000):
        _, v, lg = net._forward(X[s:s + 20000].astype(np.float64))
        out_v.append(np.asarray(v).ravel()); out_p.append(np.asarray(lg))
    v = np.concatenate(out_v); lg = np.concatenate(out_p)
    vc = np.clip(v, 1e-6, 1 - 1e-6)
    acc = float(((v >= 0.5) == (Y >= 0.5)).mean())
    brier = float(((v - Y) ** 2).mean())
    ll = float(-(Y * np.log(vc) + (1 - Y) * np.log(1 - vc)).mean())
    bins = np.clip((v * 10).astype(int), 0, 9)
    ece = float(sum(abs(v[bins == b].mean() - Y[bins == b].mean()) * (bins == b).mean() for b in range(10) if (bins == b).any()))
    ext = float(((v < 0.1) | (v > 0.9)).mean())
    lgm = np.where(M > 0, lg, -1e9)
    multi = M.sum(1) > 1
    top1 = float((lgm.argmax(1) == PI.argmax(1))[multi].mean())
    return {"acc": acc, "brier": brier, "logloss": ll, "ece": ece, "extreme": ext, "pol_top1": top1}


def main():
    t0 = time.time()
    D, games_total, nsh = load()
    G = D["G"]
    te = D["TEST"] == 1
    if USE_PER_GAME == 1:
        first = np.ones(len(G), bool)
        first[1:] = G[1:] != G[:-1]
        keep_tr = first
    else:
        keep_tr = np.ones(len(G), bool)
    tr_games = np.unique(G[~te])
    rng = np.random.default_rng(12345)
    rng.shuffle(tr_games)
    nval = max(200, int(len(tr_games) * 0.03))
    val_g = set(tr_games[:nval].tolist())
    pool_g = tr_games[nval:]
    if NGAMES and NGAMES < len(pool_g):
        pool_g = np.sort(pool_g[:NGAMES])
    use_g = np.zeros(len(G), bool)
    use_g[np.isin(G, pool_g)] = True
    va = np.isin(G, np.fromiter(val_g, np.int64))
    tr = use_g & keep_tr & ~te & ~va
    Xte, Yte, PIte, Mte = D["X"][te], D["Y"][te], D["PI"][te], D["M"][te].astype(np.float64)
    Xva, Yva, PIva, Mva = D["X"][va], D["Y"][va], D["PI"][va], D["M"][va].astype(np.float64)
    ntr_games = len(np.unique(G[tr]))
    print(f"シャード{nsh} 全対局{games_total} / 訓練 {tr.sum()}局面・{ntr_games}対局 / 検証(選択) {va.sum()} / "
          f"TEST {te.sum()}局面・{len(np.unique(G[te]))}対局  PHASE={PHASE}", flush=True)
    base = PVNetNP.load(BASE)
    if PHASE == "base":
        m = metrics(base, Xte, Yte, PIte, Mte)
        print("TEST", json.dumps(m), flush=True)
        _rec({"phase": "base", "games": 0, **m})
        return
    X = D["X"][tr].astype(np.float64); Y = D["Y"][tr].astype(np.float64)
    PI = D["PI"][tr].astype(np.float64); M = D["M"][tr].astype(np.float64)
    del D
    if PHASE == "fresh":
        h1, h2 = (int(v) for v in ARCH.split("x"))
        net = PVNetNP(X.shape[1], hidden=h1, hidden2=h2, seed=SEED, act="relu", norm=True)
        net.fit_norm(X)
    else:
        net = PVNetNP.load(BASE)
    keys = ("W1", "b1", "W2", "b2", "Wv", "bv", "Wp", "bp")
    snap = lambda: {k: (getattr(net, k).copy() if hasattr(getattr(net, k), "copy") else getattr(net, k)) for k in keys}
    best = (metrics(net, Xva, Yva, PIva, Mva)["brier"] if PHASE != "fresh" else 9.0, snap(), 0)
    print(f"  ep0 検証Brier {best[0]:.4f}", flush=True)
    if PHASE == "head":
        T = net._top(X)[-1]; Tva = net._top(Xva.astype(np.float64))[-1]
        Wv = np.array(net.Wv, float); bv = float(net.bv)
        st = {"m": np.zeros_like(Wv), "v": np.zeros_like(Wv), "mb": 0.0, "vb": 0.0, "t": 0}
        r = np.random.default_rng(SEED)
        for ep in range(EPOCHS):
            lr = LR * (0.5 ** (ep / max(EPOCHS / 3.0, 1.0)))
            perm = r.permutation(len(T))
            for s in range(0, len(T), 256):
                bi = perm[s:s + 256]
                v = 1.0 / (1.0 + np.exp(-(T[bi] @ Wv + bv)))
                g = (v - Y[bi]) / len(bi)
                gw = T[bi].T @ g + 1e-5 * Wv; gb = g.sum()
                st["t"] += 1; t = st["t"]
                st["m"] = 0.9 * st["m"] + 0.1 * gw; st["v"] = 0.999 * st["v"] + 0.001 * gw * gw
                st["mb"] = 0.9 * st["mb"] + 0.1 * gb; st["vb"] = 0.999 * st["vb"] + 0.001 * gb * gb
                c1 = 1 - 0.9 ** t; c2 = 1 - 0.999 ** t
                Wv -= lr * (st["m"] / c1) / (np.sqrt(st["v"] / c2) + 1e-8)
                bv -= lr * (st["mb"] / c1) / (np.sqrt(st["vb"] / c2) + 1e-8)
            vv = 1.0 / (1.0 + np.exp(-(Tva @ Wv + bv)))
            b = float(((vv - Yva) ** 2).mean())
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
            print(f"  ep{ep+1} 検証Brier {m['brier']:.4f} 的中 {m['acc']*100:.1f}% 方策top1 {m['pol_top1']*100:.1f}%", flush=True)
            if m["brier"] < best[0]:
                best = (m["brier"], snap(), ep + 1)
    for k, v in best[1].items():
        setattr(net, k, v)
    if PHASE == "fresh":
        net.fold_norm()
    m = metrics(net, Xte, Yte, PIte, Mte)
    print(f"TEST best_ep={best[2]}", json.dumps(m), f"{time.time()-t0:.0f}s", flush=True)
    if OUT:
        net._adam = None
        net.save(OUT)
        print(f"保存: {OUT}", flush=True)
    _rec({"phase": PHASE, "games": int(ntr_games), "samples": int(tr.sum()), "best_ep": best[2],
          "lr": LR, "epochs": EPOCHS, "vw": VW, "per_game": USE_PER_GAME, "out": OUT, **m})


def _rec(d):
    if RESULTS:
        with open(RESULTS, "a") as f:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
