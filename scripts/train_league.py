"""長時間リーグ自己対戦（AlphaZero/AlphaStar的・共進化）。

- 学習者(best)が、リーグプール（現best＋過去の採用チェックポイント）から選ばれた相手と対戦。
  → 共進化の循環（A>B>C>A）を防ぎ、多様な競争相手で頑健に強くなる。
- 学習者のみMCTSで記録、相手は採用ネットの方策(NetGreedyAI＝競争力ある相手)で高速に。
- 各反復: 自己対戦→学習→アリーナ(候補 vs 現best, ネット対ネット)→勝ち越せば昇格しプールに追加。
- 一晩規模: iter上限 or 時間上限まで連続。採用毎にbest保存＋定期チェックポイント。
使い方: nohup python train_league.py [iters] [games_per] [n_sims] [max_hours] &
"""
import os, sys, json, copy, random, time
import multiprocessing as mp
from collections import deque
from pathlib import Path
import numpy as np

from simulator.simulate import get_loader
from simulator.env import (load_registered_parties, load_extra_templates,
                           build_party, heuristic_selection)
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.features import feature_dim
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.alphazero import NetGreedyAI, PVMCTSAI
from simulator.az_loop import _SelfPlayAI, explore_selection, to_arrays
from simulator.strategies import make_strategy
import train_az2 as T

_STRAT_MAP = {1001: "baton", 1002: "wall", 1003: "stall", 1004: "setup"}
CKPT_DIR = Path(__file__).resolve().parent / "reports" / "checkpoints"
ARENA_N = 200   # アリーナ対戦数（#1ノイズ対策で24→200）


def _strat_parties(loader):
    return [(t, _STRAT_MAP[t.party_id]) for t in load_extra_templates() if t.party_id in _STRAT_MAP]


def _league_worker(args):
    """学習者=MCTS(記録)、相手=リーグ(過去/現best)のネット方策 or 戦略exploiter。"""
    learner, pool, n_games, n_sims, seed, strat_p = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    sparties = _strat_parties(loader); rng = random.Random(seed)
    out = []
    for _ in range(n_games):
        pa, pb = rng.sample(parties, 2)
        learn_team = build_party(pa, loader); opp_team = build_party(pb, loader)
        ls = BattleSide(explore_selection(learn_team, opp_team, loader, rng))   # 多様な選出
        ls.belief = OpponentBelief(loader)
        learner_ai = _SelfPlayAI(loader, learner, n_sims, 0.25, 1.0, rng)
        if sparties and rng.random() < strat_p:               # exploiter（戦略相手・OOD補完）
            sp, sname = rng.choice(sparties); st = build_party(sp, loader)
            os_ = BattleSide(st[:3]); opp_ai = make_strategy(sname, rng.randint(0, 1 << 30))
        else:                                                 # リーグ相手（過去/現best）も探索AI(MCTS)＝対称的自己対戦
            os_ = BattleSide(explore_selection(opp_team, learn_team, loader, rng))  # 相手も多様な選出
            opp_ai = PVMCTSAI(loader, rng.choice(pool), n_sims=n_sims, seed=seed ^ 0x5bd1e995)
        os_.belief = OpponentBelief(loader)
        if rng.random() < 0.5:
            w = Battle(ls, os_).run(learner_ai, opp_ai); lw = (w == 1)
        else:
            w = Battle(os_, ls).run(opp_ai, learner_ai); lw = (w == 2)
        if w != 0:
            for feat, pi, legal in learner_ai.records:
                out.append((feat, pi, legal, 1.0 if lw else 0.0))
    return out


def _arena_worker(args):
    """アリーナを並列化（候補 vs 現best, 探索AI同士）。N分割スライスを1ワーカーが担当。"""
    cand, base, n, depth, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    return T.eval_vs_net(cand, base, loader, parties, N=n, depth=depth, seed=seed)


def main():
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    games_per = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    n_sims = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    max_hours = float(sys.argv[4]) if len(sys.argv) > 4 else 8.0
    mode = sys.argv[5] if len(sys.argv) > 5 else ""
    big = mode == "big"
    fresh_std = mode in ("v3", "v4", "v5", "v6", "v7", "exp24", "exp96")  # 標準サイズnetを現feature_dimでゼロ学習
    strat_p = 0.35 if mode in ("v7", "exp24", "exp96") else 0.15   # 戦略カリキュラム（exp系もv7と同条件で揃える）
    deep = mode == "deep"                            # 現デプロイnetから継続・別ファイル保存
    if big:
        save_path = Path(__file__).resolve().parent / "az_net_big.json"
    elif fresh_std:
        save_path = Path(__file__).resolve().parent / f"az_net_{mode}.json"
    elif deep:
        save_path = Path(__file__).resolve().parent / "az_net_deep.json"
    else:
        save_path = AZNP_PATH
    workers = max(1, (os.cpu_count() or 2) - 1)
    ctx = mp.get_context("spawn")
    CKPT_DIR.mkdir(parents=True, exist_ok=True)

    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    if big:
        best = PVNetNP(feature_dim(), hidden=512, hidden2=384, hidden3=256, seed=0)
        print("大型ネット(512x384x256)をゼロから学習。保存先=別ファイル(デプロイは不変)", flush=True)
    elif fresh_std:
        best = PVNetNP(feature_dim(), hidden=256, hidden2=128, seed=0)
        print(f"{mode}特徴({feature_dim()}次元)・標準net(256x128)をゼロから学習。保存先=az_net_{mode}.json(デプロイは不変)", flush=True)
    else:
        best = PVNetNP.load()
        if best is None or best.dim != feature_dim():
            print("ネット未整合。"); return
    start_net = copy.deepcopy(best)
    pool = deque([copy.deepcopy(best)], maxlen=8)   # リーグプール（凍結スナップショット）
    Xv, Yv = T.gen_validation(loader, parties, n_games=120, strat_games=40)
    print(f"リーグ自己対戦開始: iters={iters} games/iter={games_per} n_sims={n_sims} "
          f"max_hours={max_hours} workers={workers} 初期検証{best.value_acc(Xv,Yv):.1%}", flush=True)

    buffer = deque(maxlen=5)
    hist = []; out_path = Path("reports") / "league_history.json"
    accepts = 0; t_all = time.time()
    for it in range(iters):
        if (time.time() - t_all) > max_hours * 3600:
            print(f"時間上限({max_hours}h)到達。終了。", flush=True); break
        t0 = time.time()
        per = max(1, games_per // workers)
        pool_list = list(pool)
        args = [(best, pool_list, per, n_sims, it * 1000 + w, strat_p) for w in range(workers)]
        samples = []
        with ctx.Pool(workers) as pool_mp:
            for res in pool_mp.map(_league_worker, args):
                samples += res
        buffer.append(samples)
        train_samples = [s for chunk in buffer for s in chunk]
        X, PI, M, Y = to_arrays(train_samples)
        cand = copy.deepcopy(best)
        cand.train_pi(X, PI, M, Y, epochs=12, lr=0.05, batch=256)
        # アリーナ（#1ノイズ対策）: N=200 を並列化。誤昇格率 約27%→約8%。
        per_a = max(1, ARENA_N // workers)
        a_args = [(cand, best, per_a, 4, it * 7919 + w) for w in range(workers)]
        with ctx.Pool(workers) as pool_mp:
            ares = pool_mp.map(_arena_worker, a_args)
        aw = sum(r[0] for r in ares); al = sum(r[1] for r in ares)
        accepted = (aw + al) > 0 and (aw / (aw + al)) >= 0.55
        if accepted:
            best = cand; accepts += 1
            pool.append(copy.deepcopy(best)); best.save(save_path)
        rec = {"iter": it + 1, "arena_w": aw, "arena_l": al, "accepted": bool(accepted),
               "pool": len(pool), "sec": round(time.time() - t0, 1),
               "elapsed_min": round((time.time() - t_all) / 60, 1)}
        hist.append(rec); out_path.write_text(json.dumps(hist, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[反復{it+1}/{iters}] アリーナ{aw}-{al}({aw/max(1,aw+al):.0%}) "
              f"[{'昇格' if accepted else '据置'}] プール{len(pool)} 採用計{accepts} "
              f"{rec['sec']:.0f}秒 累計{rec['elapsed_min']:.0f}分", flush=True)
        if (it + 1) % 10 == 0:
            ckpt = CKPT_DIR / f"league_it{it+1}.json"; best.save(ckpt)
            cw, cl = T.eval_vs_net(best, start_net, loader, parties, N=30, depth=4)
            print(f"  ▷ 中間チェックポイント保存。累積進歩 vs 開始net: {cw}-{cl}({cw/max(1,cw+cl):.0%})", flush=True)

    cw, cl = T.eval_vs_net(best, start_net, loader, parties, N=60, depth=4)
    print(f"[終了] 採用{accepts}回 / 累積進歩 最終best vs 開始net: {cw}-{cl}({cw/max(1,cw+cl):.0%})", flush=True)
    best.save(save_path)
    print(f"保存: {save_path}", flush=True)


if __name__ == "__main__":
    main()
