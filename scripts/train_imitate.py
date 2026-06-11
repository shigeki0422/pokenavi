"""模倣学習: 手動対戦で記録した人間(あなた)の手を教師にネットをファインチューン。

sim_server が imitation_data.jsonl に記録した (局面特徴x, 行動index a, 合法マスクm, 勝敗y) を、
ワンホット方策＋価値ターゲットとして学習。自己対戦サンプルをアンカーに混ぜて忘却を防ぎ、
固定検証集合の価値精度が下がらない場合のみ採用（劣化を構造的に禁止）。
使い方: python train_imitate.py
"""
import os, sys, json, copy, random
import multiprocessing as mp
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.features import feature_dim
from simulator.alphazero import ACTION_DIM
from simulator.az_loop import _selfplay_worker, to_arrays
import train_az2 as T

IMIT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "imitation_data.jsonl")


def load_imitation():
    if not os.path.exists(IMIT_PATH):
        return None
    recs = []
    with open(IMIT_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    return recs or None


def imit_arrays(recs):
    n = len(recs)
    X = np.array([r["x"] for r in recs], float)
    PI = np.zeros((n, ACTION_DIM)); M = np.zeros((n, ACTION_DIM)); Y = np.zeros(n)
    for k, r in enumerate(recs):
        for ix in r["m"]:
            M[k, ix] = 1.0
        PI[k, r["a"]] = 1.0          # 人間の選んだ手をワンホット方策ターゲット
        Y[k] = r["y"]
    return X, PI, M, Y


def main():
    recs = load_imitation()
    if not recs:
        print(f"模倣データがありません: {IMIT_PATH}\n手動対戦をプレイすると自動で記録されます。")
        return
    print(f"模倣データ: {len(recs)}手（あなたの意思決定）", flush=True)

    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load()
    if net is None or net.dim != feature_dim():
        print("ネット未整合。先に通常学習が必要です。"); return

    # 検証集合（戦略含む）と現在精度
    Xv, Yv = T.gen_validation(loader, parties, n_games=100, strat_games=40)
    base_acc = net.value_acc(Xv, Yv)
    print(f"検証精度(現): {base_acc:.1%}", flush=True)

    # アンカー用 自己対戦サンプル（忘却防止）
    workers = max(1, (os.cpu_count() or 2) - 1)
    ctx = mp.get_context("spawn")
    args = [(net, max(1, 600 // workers), 24, w, 0.25, 1.0, 0.35) for w in range(workers)]
    anchor = []
    with ctx.Pool(workers) as pool:
        for res in pool.map(_selfplay_worker, args):
            anchor += res
    Xa, PIa, Ma, Ya = to_arrays(anchor)
    cand = copy.deepcopy(net)
    # 段階1: アンカー自己対戦で価値＋方策を通常学習（価値較正を保つ）
    cand.train_pi(Xa, PIa, Ma, Ya, epochs=10, lr=0.04, batch=256)

    # 段階2: 勝ち試合の手だけを「方策のみ」注入（value_weight=0で価値を歪めない）
    wins = [r for r in recs if r["y"] == 1.0]
    if wins:
        Xi, PIi, Mi, Yi = imit_arrays(wins)
        cand.train_pi(Xi, PIi, Mi, Yi, epochs=8, lr=0.03, batch=64, value_weight=0.0)
    print(f"学習: アンカー{len(anchor)}手(価値+方策) + 勝ち模倣{len(wins)}手(方策のみ)", flush=True)

    cand_acc = cand.value_acc(Xv, Yv)
    # 模倣方策が実際に反映されたか（勝ち局面で人間の手が最上位prior）
    from simulator.alphazero import ACTION_DIM
    hit = 0
    for r in wins:
        prior, _ = cand.evaluate(r["x"], r["m"])
        if prior and max(prior, key=prior.get) == r["a"]:
            hit += 1
    pol = hit / max(1, len(wins))
    print(f"検証精度(候補): {cand_acc:.1%}  模倣方策一致率: {pol:.0%}", flush=True)

    if cand_acc >= base_acc - 0.005:
        cand.save()
        print(f"採用・保存: {AZNP_PATH}（あなたの手筋を方策に反映）", flush=True)
    else:
        print(f"棄却（検証精度が低下: {base_acc:.1%}→{cand_acc:.1%}）。ネットは据え置き。", flush=True)


if __name__ == "__main__":
    main()
