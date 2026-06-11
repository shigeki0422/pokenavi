"""大規模自己対戦ドライバ。既存ネットから継続学習し、各反復でチェックポイント保存。
使い方: python train_run.py [iters] [games_per] [n_sims]
"""
import os, sys, time, json, random, copy
import multiprocessing as mp
from pathlib import Path
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.features import encode_state, feature_dim
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.search_ai import SearchAI
from simulator.az_loop import _selfplay_worker, to_arrays
from simulator.train_az_np import rain_probe


def eval_strength(net, loader, parties, N=20, depth=6, seed=7):
    """価値誘導 SearchAI vs HeuristicAI の勝率（AI=価値誘導）。"""
    def vfn(s1, s2, f):
        return net.evaluate(encode_state(s1, s2, f), [0])[1]
    heur = HeuristicAI()
    rng = random.Random(seed)
    win = lose = 0
    for i in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        sc = SearchAI(loader, rollouts=12, depth=depth, seed=1000 + i, value_fn=vfn)
        if i % 2 == 0:
            s1.belief = OpponentBelief(loader); w = Battle(s1, s2).run(sc, heur)
            win += (w == 1); lose += (w == 2)
        else:
            s2.belief = OpponentBelief(loader); w = Battle(s1, s2).run(heur, sc)
            win += (w == 2); lose += (w == 1)
    return win, lose


def main():
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    games_per = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    n_sims = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    hidden = int(sys.argv[4]) if len(sys.argv) > 4 else 256
    hidden2 = int(sys.argv[5]) if len(sys.argv) > 5 else 128
    fresh = (len(sys.argv) > 6 and sys.argv[6] == "1")
    workers = max(1, (os.cpu_count() or 2) - 1)
    seed = 0

    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    existing = None if fresh else PVNetNP.load()
    if existing is not None and existing.dim == feature_dim():
        net = existing
        mode = f"継続学習 net({net.hidden}x{net.hidden2})"
    else:
        net = PVNetNP(feature_dim(), hidden=hidden, hidden2=hidden2, seed=seed)
        mode = f"ゼロ学習 net({hidden}x{hidden2})"
    print(f"開始: 新アーキ {mode} dim={feature_dim()}  "
          f"iters={iters} games/iter={games_per} n_sims={n_sims} workers={workers}", flush=True)

    w0, l0 = eval_strength(net, loader, parties, N=20)
    print(f"[開始時] 価値誘導AI vs Heuristic: {w0}勝{l0}敗 ({w0/max(1,w0+l0):.0%})", flush=True)

    ctx = mp.get_context("spawn")
    history = []
    out = Path("reports") / "az_history_big.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    t_all = time.time()
    for it in range(iters):
        t0 = time.time()
        per = max(1, games_per // workers)
        args = [(net, per, n_sims, seed + it * 1000 + wk, 0.25, 1.0, 0.35) for wk in range(workers)]
        samples = []
        with ctx.Pool(workers) as pool:
            for res in pool.map(_selfplay_worker, args):
                samples += res
        X, PI, M, Y = to_arrays(samples)
        net.train_pi(X, PI, M, Y, epochs=20, lr=0.06, batch=256)
        net.save()  # チェックポイント
        d, pos = rain_probe(net, loader)
        rec = {"iter": it + 1, "games": per * workers, "samples": len(samples),
               "value_acc": float(net.value_acc(X, Y)), "rain_delta": float(d),
               "sec": round(time.time() - t0, 1)}
        history.append(rec)
        out.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[反復{it+1}/{iters}] {per*workers}試合 サンプル{len(samples)} "
              f"価値精度{rec['value_acc']:.1%} 雨Δ{d:+.4f} {rec['sec']:.0f}秒 "
              f"(累計{(time.time()-t_all)/60:.0f}分)", flush=True)

    w1, l1 = eval_strength(net, loader, parties, N=30)
    print(f"[終了時] 価値誘導AI vs Heuristic: {w1}勝{l1}敗 ({w1/max(1,w1+l1):.0%})", flush=True)
    print(f"保存: {AZNP_PATH}  履歴: {out}", flush=True)


if __name__ == "__main__":
    main()
