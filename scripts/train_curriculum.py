"""0%（AIが負け切る）matchupに探索を集中して勝ち筋を発掘・学習するカリキュラム。

着想: シミュで勝率0%でも実際は勝ち筋が存在する（人間は勝てる）。そういう難所こそ
価値・方策が最も誤っており学習価値が高い。AlphaZeroが難所に探索を集中するのと同じ。

手順:
 1. 全構築ペアを高速スクリーニング（HeuristicAI）し「片側がほぼ勝てない(≤thr)」matchupを抽出
 2. その matchup で不利側を「選出多様化＋高探索(Dirichlet/温度/選出ε大)」で自己対戦し、
    不利側の勝ち試合を発掘・記録（稀少な勝ちを複製して重み付け）
 3. 発掘データを価値＋方策に学習（自己対戦アンカー＋検証精度ゲートで劣化禁止）
使い方: python train_curriculum.py [screen_opp] [explore_games] [thr%]
"""
import os, sys, copy, random, time
import multiprocessing as mp
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.features import feature_dim
from simulator.az_loop import _SelfPlayAI, _selfplay_worker, to_arrays, explore_selection
import train_az2 as T


def _screen_worker(args):
    pairs, n, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    rng = random.Random(seed); heur = HeuristicAI(); out = []
    for ai, bi in pairs:
        aw = tot = 0
        for _ in range(n):
            a1 = build_party(parties[ai], loader); a2 = build_party(parties[bi], loader)
            s1 = BattleSide(heuristic_selection(a1, a2, loader)); s2 = BattleSide(heuristic_selection(a2, a1, loader))
            s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
            w = Battle(s1, s2).run(heur, heur)
            if w != 0:
                tot += 1; aw += (w == 1)
        out.append((ai, bi, aw / max(1, tot)))
    return out


def _explore_worker(args):
    net, ai_idx, bi_idx, n_games, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    rng = random.Random(seed); heur = HeuristicAI()
    pa, pb = parties[ai_idx], parties[bi_idx]
    alls = []; nwin = 0
    for _ in range(n_games):
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(explore_selection(a1, a2, loader, rng, 0.7))  # 不利側: 選出を強く多様化
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        ai_a = _SelfPlayAI(loader, net, 20, 0.4, 1.3, rng)           # 高探索MCTS
        w = Battle(s1, s2).run(ai_a, heur)
        if w == 0:
            continue
        won = (w == 1); nwin += won
        for feat, pi, legal in ai_a.records:
            alls.append((feat, pi, legal, 1.0 if won else 0.0))
    return {"pair": (ai_idx, bi_idx), "nwin": nwin, "ngame": n_games, "alls": alls}


def main():
    screen_opp = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    explore_games = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    thr = (float(sys.argv[3]) if len(sys.argv) > 3 else 8.0) / 100.0
    workers = max(1, (os.cpu_count() or 2) - 1)
    ctx = mp.get_context("spawn")
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load()
    if net is None or net.dim != feature_dim():
        print("ネット未整合。先に通常学習が必要。"); return
    N = len(parties); rng = random.Random(0)

    # 1. スクリーニング: 各構築A vs ランダム相手B（HeuristicAI）で A の勝率
    pairs = []
    for ai in range(N):
        for bi in rng.sample([x for x in range(N) if x != ai], min(screen_opp, N - 1)):
            pairs.append((ai, bi))
    print(f"スクリーニング: {len(pairs)}ペア（HeuristicAI×10戦）...", flush=True)
    chunks = [pairs[i::workers] for i in range(workers)]
    args = [(c, 10, 100 + i) for i, c in enumerate(chunks)]
    screened = []
    with ctx.Pool(workers) as pool:
        for res in pool.map(_screen_worker, args):
            screened += res
    hard = sorted([s for s in screened if s[2] <= thr], key=lambda x: x[2])
    print(f"難所(勝率≤{thr:.0%})検出: {len(hard)}件", flush=True)
    hard = hard[:16]
    for ai, bi, wr in hard[:16]:
        print(f"  #{parties[ai].party_id} vs #{parties[bi].party_id}: A勝率{wr:.0%}", flush=True)
    if not hard:
        print("難所なし。終了。"); return

    # 2. 難所で高探索自己対戦 → 不利側の勝ち筋を発掘
    print(f"\n難所{len(hard)}件で各{explore_games}戦の探索的自己対戦...", flush=True)
    ex_args = [(net, ai, bi, explore_games, 500 + i) for i, (ai, bi, _) in enumerate(hard)]
    curric = []; total_win = 0
    with ctx.Pool(workers) as pool:
        for res in pool.map(_explore_worker, ex_args):
            ai, bi = res["pair"]
            print(f"  #{parties[ai].party_id} vs #{parties[bi].party_id}: 勝ち発掘 {res['nwin']}/{res['ngame']}", flush=True)
            curric += res["alls"]; total_win += res["nwin"]
    print(f"探索完了: 勝ち発掘 計{total_win}試合, サンプル{len(curric)}手", flush=True)
    if total_win == 0:
        print("勝ち筋を発掘できず（探索不足）。試合数/探索を増やして再試行を推奨。"); return

    # 3. 学習: カリキュラム + アンカー自己対戦、検証精度ゲート
    Xv, Yv = T.gen_validation(loader, parties, n_games=120, strat_games=40)
    base_acc = net.value_acc(Xv, Yv)
    per = max(1, 800 // workers)
    a_args = [(net, per, 24, 700 + w, 0.25, 1.0, 0.35) for w in range(workers)]
    anchor = []
    with ctx.Pool(workers) as pool:
        for res in pool.map(_selfplay_worker, a_args):
            anchor += res
    Xa, PIa, Ma, Ya = to_arrays(anchor)
    Xc, PIc, Mc, Yc = to_arrays(curric)
    # 発掘勝ち手を重み付け（難所の勝ち筋を強調）
    wins_idx = [i for i, s in enumerate(curric) if s[3] == 1.0]
    rep = max(1, len(anchor) // max(1, len(curric)))
    X = np.concatenate([Xa, Xc] + [Xc[wins_idx]] * rep)
    PI = np.concatenate([PIa, PIc] + [PIc[wins_idx]] * rep)
    M = np.concatenate([Ma, Mc] + [Mc[wins_idx]] * rep)
    Y = np.concatenate([Ya, Yc] + [Yc[wins_idx]] * rep)
    print(f"学習: アンカー{len(anchor)} + カリキュラム{len(curric)}(勝ち{len(wins_idx)}×{rep+1})", flush=True)
    cand = copy.deepcopy(net)
    cand.train_pi(X, PI, M, Y, epochs=12, lr=0.04, batch=256)
    cand_acc = cand.value_acc(Xv, Yv)
    print(f"検証精度: {base_acc:.1%} → {cand_acc:.1%}", flush=True)
    if cand_acc >= base_acc - 0.005:
        cand.save()
        print(f"採用・保存: {AZNP_PATH}（0%難所の勝ち筋を反映）", flush=True)
    else:
        print(f"棄却（検証低下）。据え置き。", flush=True)


if __name__ == "__main__":
    main()
