"""デプロイAI基準（価値誘導探索）で真の0% matchupを特定し、そこで勝ち筋を発掘・学習する。

train_curriculum.py はスクリーニングがHeuristicAIで、デプロイAI(価値誘導)が既に勝てる
matchupを誤って標的にしていた。本版は:
 1. HeuristicAIで候補を高速抽出（弱AI0%は強AI0%の上位集合なので候補生成に使う）
 2. 候補を「デプロイ相当の価値誘導AI（+方策prior）」で確認し、真の0%(≤thr)だけ残す
 3. 真の0%で、不利側を高探索＋選出多様化、相手を価値誘導AIにして勝ち筋を発掘
 4. 発掘を価値＋方策に学習（アンカー＋検証ゲート）
使い方: python train_curriculum2.py [confirm_cap] [explore_games] [thr%]
"""
import os, sys, copy, random
import multiprocessing as mp
import numpy as np

from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.search_ai import SearchAI
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.features import encode_state, feature_dim
from simulator.alphazero import legal_actions_indexed
from simulator.az_loop import _SelfPlayAI, _selfplay_worker, to_arrays, explore_selection
import train_az2 as T


def _vg(net, rollouts, depth, seed):
    """デプロイ相当の価値誘導＋方策prior探索AI（軽量設定可）。"""
    def vfn(s1, s2, f): return net.evaluate(encode_state(s1, s2, f), [0])[1]
    def pfn(s1, s2, f):
        L = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
        return net.evaluate(encode_state(s1, s2, f), L)[0] if L else {}
    return SearchAI(get_loader(), rollouts=rollouts, depth=depth, seed=seed,
                    value_fn=vfn, policy_fn=pfn, policy_weight=0.15)


def _heur_screen_worker(args):
    pairs, n, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    heur = HeuristicAI(); out = []
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


def _confirm_worker(args):
    """候補を価値誘導AI同士で確認（A=不利側=価値誘導, B=価値誘導）。Aの勝率を返す。"""
    net, pairs, n, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    heur_sel = heuristic_selection; out = []
    for k, (ai, bi) in enumerate(pairs):
        sc_a = _vg(net, 6, 4, seed + k); sc_b = _vg(net, 6, 4, seed + k + 777)
        aw = tot = 0
        for i in range(n):
            a1 = build_party(parties[ai], loader); a2 = build_party(parties[bi], loader)
            s1 = BattleSide(heur_sel(a1, a2, loader)); s2 = BattleSide(heur_sel(a2, a1, loader))
            s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
            w = Battle(s1, s2).run(sc_a, sc_b)
            if w != 0:
                tot += 1; aw += (w == 1)
        out.append((ai, bi, aw / max(1, tot)))
    return out


def _explore_worker(args):
    """真の0%で不利側A=高探索MCTS＋選出多様化、相手B=価値誘導AI。Aの勝ち筋を発掘。"""
    net, ai_idx, bi_idx, n_games, seed = args
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    rng = random.Random(seed); pa, pb = parties[ai_idx], parties[bi_idx]
    sc_b = _vg(net, 6, 4, seed + 333)
    alls = []; nwin = 0
    for _ in range(n_games):
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(explore_selection(a1, a2, loader, rng, 0.7))
        s2 = BattleSide(heuristic_selection(a2, a1, loader))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        ai_a = _SelfPlayAI(loader, net, 24, 0.4, 1.3, rng)
        w = Battle(s1, s2).run(ai_a, sc_b)
        if w == 0:
            continue
        won = (w == 1); nwin += won
        for feat, pi, legal in ai_a.records:
            alls.append((feat, pi, legal, 1.0 if won else 0.0))
    return {"pair": (ai_idx, bi_idx), "nwin": nwin, "ngame": n_games, "alls": alls}


def main():
    confirm_cap = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    explore_games = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    thr = (float(sys.argv[3]) if len(sys.argv) > 3 else 5.0) / 100.0
    workers = max(1, (os.cpu_count() or 2) - 1)
    ctx = mp.get_context("spawn")
    loader = get_loader(); parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP.load()
    if net is None or net.dim != feature_dim():
        print("ネット未整合。"); return
    N = len(parties); rng = random.Random(0)

    # 1. HeuristicAIで候補抽出（弱AIで負け気味＝価値誘導でも難所の可能性）
    pairs = []
    for ai in range(N):
        for bi in rng.sample([x for x in range(N) if x != ai], min(8, N - 1)):
            pairs.append((ai, bi))
    print(f"候補スクリーニング(HeuristicAI): {len(pairs)}ペア...", flush=True)
    chunks = [pairs[i::workers] for i in range(workers)]
    with ctx.Pool(workers) as pool:
        screened = [x for res in pool.map(_heur_screen_worker, [(c, 8, 100 + i) for i, c in enumerate(chunks)]) for x in res]
    cand = sorted([s for s in screened if s[2] <= 0.12], key=lambda x: x[2])[:confirm_cap]
    print(f"候補(HeuristicAI勝率≤12%): {len(cand)}件 → 価値誘導AIで真の0%を確認...", flush=True)

    # 2. デプロイ相当の価値誘導AIで確認
    cpairs = [(a, b) for a, b, _ in cand]
    cchunks = [cpairs[i::workers] for i in range(workers)]
    with ctx.Pool(workers) as pool:
        confirmed = [x for res in pool.map(_confirm_worker, [(net, c, 6, 200 + i) for i, c in enumerate(cchunks)]) for x in res]
    true0 = sorted([c for c in confirmed if c[2] <= thr], key=lambda x: x[2])
    print(f"真の0%(価値誘導AI勝率≤{thr:.0%}): {len(true0)}件", flush=True)
    for ai, bi, wr in true0[:16]:
        print(f"  #{parties[ai].party_id} vs #{parties[bi].party_id}: 価値誘導A勝率{wr:.0%}", flush=True)
    true0 = true0[:12]
    if not true0:
        print("真の0%なし（デプロイAIは全候補で勝てている）。"); return

    # 3. 真の0%で勝ち筋発掘（相手＝価値誘導AI）
    print(f"\n真の0% {len(true0)}件で各{explore_games}戦の探索...", flush=True)
    ex_args = [(net, ai, bi, explore_games, 500 + i) for i, (ai, bi, _) in enumerate(true0)]
    curric = []; total_win = 0
    with ctx.Pool(workers) as pool:
        for res in pool.map(_explore_worker, ex_args):
            ai, bi = res["pair"]
            print(f"  #{parties[ai].party_id} vs #{parties[bi].party_id}: 勝ち発掘 {res['nwin']}/{res['ngame']}", flush=True)
            curric += res["alls"]; total_win += res["nwin"]
    print(f"探索完了: 勝ち発掘 計{total_win}試合, サンプル{len(curric)}手", flush=True)
    if total_win == 0:
        print("勝ち筋を発掘できず。探索量を増やすか、不利側も価値誘導にする必要あり。"); return

    # 4. 学習（アンカー＋カリキュラム、検証ゲート）
    Xv, Yv = T.gen_validation(loader, parties, n_games=120, strat_games=40)
    base_acc = net.value_acc(Xv, Yv)
    per = max(1, 800 // workers)
    with ctx.Pool(workers) as pool:
        anchor = [x for res in pool.map(_selfplay_worker, [(net, per, 24, 700 + w, 0.25, 1.0, 0.35) for w in range(workers)]) for x in res]
    Xa, PIa, Ma, Ya = to_arrays(anchor)
    cand_net = copy.deepcopy(net)
    # 価値ヘッドは完全凍結（全段階 value_weight=0）。方策だけ更新＝価値較正を一切壊さない。
    # 段階1: アンカー方策で正則化（汎用の良手を忘れない）
    cand_net.train_pi(Xa, PIa, Ma, Ya, epochs=6, lr=0.03, batch=256, value_weight=0.0)
    # 段階2: 発掘した勝ち筋を方策に注入（0%局面での勝ち手順を方策へ）
    wins = [s for s in curric if s[3] == 1.0]
    Xc, PIc, Mc, Yc = to_arrays(wins)
    cand_net.train_pi(Xc, PIc, Mc, Yc, epochs=10, lr=0.03, batch=64, value_weight=0.0)
    print(f"学習: アンカー{len(anchor)}+勝ち筋{len(wins)}手 すべて方策のみ(価値凍結)", flush=True)
    cand_acc = cand_net.value_acc(Xv, Yv)
    # 方策のみ更新なので価値はほぼ不変。共有層の僅かなドリフト分(≤1.2%)は許容。
    print(f"検証精度: {base_acc:.1%} → {cand_acc:.1%}（価値凍結）", flush=True)
    if cand_acc >= base_acc - 0.012:
        cand_net.save()
        print(f"採用・保存: {AZNP_PATH}（真の0%難所の勝ち筋を方策に反映）", flush=True)
    else:
        print("棄却（検証低下）。据え置き。", flush=True)


if __name__ == "__main__":
    main()
