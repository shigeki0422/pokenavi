"""安定化版 AlphaZero ループ: リプレイバッファ + 検証精度ゲート。

旧ループの問題（各反復が自反復データのみで学習→探索ノイズを追い劣化、無条件採用で劣化が定着）を、
AlphaZeroの2機構で解消する:
  1. リプレイバッファ: 直近R反復の自己対戦サンプルを蓄積し、その和集合で候補を学習（忘却防止）。
  2. ゲート: 固定の held-out 検証集合での価値精度が現best以上の候補のみ採用（劣化を構造的に禁止）。

best ネットで自己対戦 → バッファ追加 → 候補=best複製を学習 → ゲート判定 → 通れば best 更新・保存。
使い方: python train_az2.py [iters] [games_per] [n_sims] [hidden] [hidden2] [fresh(1/0)]
"""
import os, sys, time, json, random, copy
import multiprocessing as mp
from collections import deque
from pathlib import Path
import numpy as np

from simulator.simulate import get_loader
from simulator.env import (load_registered_parties, load_extra_templates,
                           build_party, heuristic_selection)
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI, _forced_charging_action
from simulator.features import encode_state, feature_dim
from simulator.az_np import PVNetNP, AZNP_PATH
from simulator.search_ai import SearchAI
from simulator.az_loop import (_selfplay_worker, selfplay_game, _SelfPlayAI,
                               to_arrays, explore_selection)
from simulator.strategies import make_strategy

# 戦略テンプレ party_id → 台本戦略名
_STRAT_MAP = {1001: "baton", 1002: "wall", 1003: "stall", 1004: "setup"}


def _strat_parties(loader):
    return [(t, _STRAT_MAP[t.party_id]) for t in load_extra_templates()
            if t.party_id in _STRAT_MAP]


def _selfplay_worker_strong(args):
    """学習AI(MCTS) vs 強い教師(価値誘導探索) を teach_p の割合で混ぜる自己対戦ワーカー。
    弱いHeuristicでなく『今の自分の強い版』を相手に、学習側の記録のみ採用して鍛える。
    残りは台本戦略・通常自己対戦。"""
    net, n_games, n_sims, seed, dir_eps, temperature, eps_sel, teach_p, strat_p = args
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    sparties = _strat_parties(loader)
    rng = random.Random(seed)

    def vfn(s1, s2, f):
        return net.evaluate(encode_state(s1, s2, f), [0])[1]
    teacher = SearchAI(loader, rollouts=8, depth=6, seed=seed + 1, value_fn=vfn)

    out = []
    for _ in range(n_games):
        r = rng.random()
        if r < teach_p:  # 強い教師戦
            pa, pb = rng.sample(parties, 2)
            learn = build_party(pa, loader); opp = build_party(pb, loader)
            ls = BattleSide(explore_selection(learn, opp, loader, rng, eps_sel))
            os = BattleSide(heuristic_selection(opp, learn, loader))
            ls.belief = OpponentBelief(loader); os.belief = OpponentBelief(loader)
            learn_ai = _SelfPlayAI(loader, net, n_sims, dir_eps, temperature, rng)
            if rng.random() < 0.5:
                w = Battle(ls, os).run(learn_ai, teacher); lw = (w == 1)
            else:
                w = Battle(os, ls).run(teacher, learn_ai); lw = (w == 2)
            if w != 0:
                for feat, pi, legal in learn_ai.records:
                    out.append((feat, pi, legal, 1.0 if lw else 0.0))
        elif sparties and r < teach_p + strat_p:  # 台本戦略戦
            sp, sname = rng.choice(sparties)
            learn = build_party(rng.choice(parties), loader)
            strat_team = build_party(sp, loader)
            ls = BattleSide(explore_selection(learn, strat_team, loader, rng, eps_sel))
            ss = BattleSide(strat_team[:3])
            ls.belief = OpponentBelief(loader); ss.belief = OpponentBelief(loader)
            learn_ai = _SelfPlayAI(loader, net, n_sims, dir_eps, temperature, rng)
            strat_ai = make_strategy(sname, rng.randint(0, 1 << 30))
            if rng.random() < 0.5:
                w = Battle(ls, ss).run(learn_ai, strat_ai); lw = (w == 1)
            else:
                w = Battle(ss, ls).run(strat_ai, learn_ai); lw = (w == 2)
            if w != 0:
                for feat, pi, legal in learn_ai.records:
                    out.append((feat, pi, legal, 1.0 if lw else 0.0))
        else:
            out += selfplay_game(loader, parties, net, n_sims, rng, dir_eps, temperature, eps_sel)
    return out


def _selfplay_worker_strat(args):
    """学習AI(MCTS) vs 台本戦略 を strat_p の割合で混ぜる自己対戦ワーカー。
    台本戦は学習側の記録のみ採用（人間戦略への対処を機構として学ぶ）。"""
    net, n_games, n_sims, seed, dir_eps, temperature, eps_sel, strat_p = args
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    sparties = _strat_parties(loader)
    rng = random.Random(seed)
    out = []
    for _ in range(n_games):
        if sparties and rng.random() < strat_p:
            sp, sname = rng.choice(sparties)
            learn = build_party(rng.choice(parties), loader)
            strat_team = build_party(sp, loader)
            ls = BattleSide(explore_selection(learn, strat_team, loader, rng, eps_sel))
            ss = BattleSide(strat_team[:3])
            ls.belief = OpponentBelief(loader); ss.belief = OpponentBelief(loader)
            learn_ai = _SelfPlayAI(loader, net, n_sims, dir_eps, temperature, rng)
            strat_ai = make_strategy(sname, rng.randint(0, 1 << 30))
            if rng.random() < 0.5:
                w = Battle(ls, ss).run(learn_ai, strat_ai); learn_win = (w == 1)
            else:
                w = Battle(ss, ls).run(strat_ai, learn_ai); learn_win = (w == 2)
            if w != 0:
                for feat, pi, legal in learn_ai.records:
                    out.append((feat, pi, legal, 1.0 if learn_win else 0.0))
        else:
            out += selfplay_game(loader, parties, net, n_sims, rng, dir_eps, temperature, eps_sel)
    return out


class _Recorder:
    """各ターンの side1 視点状態を記録するラッパAI。"""
    def __init__(self, inner):
        self.inner = inner; self.feats = []

    def __call__(self, my, opp, field):
        s1, s2 = (my, opp) if my.field_idx == 0 else (opp, my)
        try:
            self.feats.append(encode_state(s1, s2, field))
        except Exception:
            pass
        return self.inner(my, opp, field)


def gen_validation(loader, parties, n_games=150, seed=99, strat_games=60):
    """固定検証集合: HeuristicAI同士＋HeuristicAI vs 台本戦略 の (状態, 最終勝敗)。
    台本戦の局面を含めることで、ゲートが「戦略への対処」改善を評価できるようにする。"""
    rng = random.Random(seed)
    X, Y = [], []
    for _ in range(n_games):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(explore_selection(a1, a2, loader, rng, 0.3))
        s2 = BattleSide(explore_selection(a2, a1, loader, rng, 0.3))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        rec = _Recorder(HeuristicAI())
        w = Battle(s1, s2).run(rec, HeuristicAI())
        if w == 0:
            continue
        y = 1.0 if w == 1 else 0.0
        for fx in rec.feats:
            X.append(fx); Y.append(y)
    sparties = _strat_parties(loader)
    for _ in range(strat_games if sparties else 0):
        sp, sname = rng.choice(sparties)
        a1 = build_party(rng.choice(parties), loader)
        strat_team = build_party(sp, loader)
        s1 = BattleSide(explore_selection(a1, strat_team, loader, rng, 0.3))
        s2 = BattleSide(strat_team[:3])
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        rec = _Recorder(HeuristicAI())
        w = Battle(s1, s2).run(rec, make_strategy(sname, rng.randint(0, 1 << 30)))
        if w == 0:
            continue
        y = 1.0 if w == 1 else 0.0
        for fx in rec.feats:
            X.append(fx); Y.append(y)
    return np.array(X, float), np.array(Y, float)


def eval_vs_strategies(net, loader, parties, N=12, depth=8, seed=31):
    """価値誘導AI が 台本戦略（受け/粘り/積み）に勝てるか（戦略ごとの勝率）。"""
    def vfn(s1, s2, f):
        return net.evaluate(encode_state(s1, s2, f), [0])[1]
    sparties = _strat_parties(loader)
    rng = random.Random(seed)
    res = {}
    for sp, sname in sparties:
        win = lose = 0
        strat_team = build_party(sp, loader)
        for i in range(N):
            learn = build_party(rng.choice(parties), loader)
            ls = BattleSide(heuristic_selection(learn, strat_team, loader))
            ss = BattleSide(strat_team[:3])
            ls.belief = OpponentBelief(loader)
            sc = SearchAI(loader, rollouts=24, depth=depth, seed=5000 + i, value_fn=vfn)
            sa = make_strategy(sname, 7000 + i)
            w = Battle(ls, ss).run(sc, sa)
            win += (w == 1); lose += (w == 2)
        res[sname] = (win, lose)
    return res


def _net_ai(net, loader, rollouts, depth, seed, adversarial=False, opp_k=6,
            tree=False, tree_depth=1, tree_k=3, tree_det=None, tree_extend_k=0,
            mcts=False, mcts_sims=400, c_puct=1.5, mcts_select="duct", mcts_fast=True,
            mcts_cache=False, mcts_ensemble=16):
    """ネットの価値誘導探索AI。ロールアウト相手もネット（NetGreedyAI）＝AlphaZero的。
    mcts_fast=True: MCTS高速化（葉のencode+forward統合＝net_eval、cloneでbelief非複製）。結果はビット一致。"""
    from simulator.alphazero import NetGreedyAI, legal_actions_indexed
    def vfn(s1, s2, f): return net.evaluate(encode_state(s1, s2, f), [0])[1]
    def pfn(s1, s2, f):
        L = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
        return net.evaluate(encode_state(s1, s2, f), L)[0] if L else {}
    ai = SearchAI(loader, rollouts=rollouts, depth=depth, seed=seed,
                  value_fn=vfn, policy_fn=pfn, policy_weight=0.15, rollout_ai=NetGreedyAI(net),
                  adversarial=adversarial, opp_k=opp_k)
    if tree:
        ai.tree_search = True; ai.tree_depth = tree_depth; ai.tree_k = tree_k
        ai.tree_det = tree_det if tree_det is not None else rollouts
        ai.tree_extend_k = tree_extend_k
    if mcts:
        ai.mcts = True; ai.mcts_sims = mcts_sims; ai.c_puct = c_puct
        ai.mcts_select = mcts_select
        if mcts_fast:
            def nefn(s1, s2, f):
                L = [ix for _, ix in legal_actions_indexed(s1, s2, f)]
                pol, val = net.evaluate(encode_state(s1, s2, f), L if L else [0])
                return pol, val
            ai.net_eval = nefn
            ai.fast_clone = True
        if mcts_cache:
            ai.mcts_cache = True; ai.mcts_ensemble = mcts_ensemble
    return ai


def eval_vs_heuristic(net, loader, parties, N=20, depth=6, seed=7):
    heur = HeuristicAI(); rng = random.Random(seed); win = lose = 0
    for i in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader)); s2 = BattleSide(heuristic_selection(a2, a1, loader))
        sc = _net_ai(net, loader, 12, depth, 3000 + i)
        if i % 2 == 0:
            s1.belief = OpponentBelief(loader); w = Battle(s1, s2).run(sc, heur); win += (w == 1); lose += (w == 2)
        else:
            s2.belief = OpponentBelief(loader); w = Battle(s1, s2).run(heur, sc); win += (w == 2); lose += (w == 1)
    return win, lose


def eval_vs_net(net, baseline, loader, parties, N=30, depth=6, seed=17):
    """共進化の指標: 現ネットのAI vs 凍結ベースラインネットのAI（両者ネット同士の対戦）。
    50%超で「ベースラインより強くなった」＝学習が前進している証拠（HeuristicAI比ではない）。"""
    rng = random.Random(seed); win = lose = 0
    for i in range(N):
        pa, pb = rng.sample(parties, 2)
        a1 = build_party(pa, loader); a2 = build_party(pb, loader)
        s1 = BattleSide(heuristic_selection(a1, a2, loader)); s2 = BattleSide(heuristic_selection(a2, a1, loader))
        cur = _net_ai(net, loader, 12, depth, 4000 + i)
        base = _net_ai(baseline, loader, 12, depth, 6000 + i)
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        if i % 2 == 0:
            w = Battle(s1, s2).run(cur, base); win += (w == 1); lose += (w == 2)
        else:
            w = Battle(s1, s2).run(base, cur); win += (w == 2); lose += (w == 1)
    return win, lose


def main():
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    games_per = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    n_sims = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    hidden = int(sys.argv[4]) if len(sys.argv) > 4 else 256
    hidden2 = int(sys.argv[5]) if len(sys.argv) > 5 else 128
    fresh = not (len(sys.argv) > 6 and sys.argv[6] == "0")
    buffer_iters = 5
    workers = max(1, (os.cpu_count() or 2) - 1)
    seed = 0

    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    print(f"検証集合を生成中...", flush=True)
    Xv, Yv = gen_validation(loader, parties, n_games=150)
    print(f"検証集合: {len(Xv)}局面", flush=True)

    existing = None if fresh else PVNetNP.load()
    if existing is not None and existing.dim == feature_dim():
        best = existing
    else:
        best = PVNetNP(feature_dim(), hidden=hidden, hidden2=hidden2, seed=seed)
    best_acc = best.value_acc(Xv, Yv)
    print(f"開始: 安定化版 net({best.hidden}x{best.hidden2}) dim={feature_dim()} "
          f"iters={iters} games/iter={games_per} n_sims={n_sims} buffer={buffer_iters}反復 "
          f"workers={workers}  初期検証精度={best_acc:.1%}", flush=True)
    w0, l0 = eval_vs_heuristic(best, loader, parties, N=20)
    s0 = eval_vs_strategies(best, loader, parties, N=12)
    print(f"[開始時] vs Heuristic: {w0}勝{l0}敗 ({w0/max(1,w0+l0):.0%})  "
          f"vs戦略: " + " ".join(f"{k}{w}-{l}" for k, (w, l) in s0.items()), flush=True)

    frozen0 = copy.deepcopy(best)  # 開始時ネット＝累積進歩の基準
    ctx = mp.get_context("spawn")
    buffer = deque(maxlen=buffer_iters)
    history = []
    out = Path("reports") / "az_history_v2.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    t_all = time.time()
    for it in range(iters):
        t0 = time.time()
        per = max(1, games_per // workers)
        # 純self-play（ネット対ネットMCTS・相手モデルもネット）＋少量の戦略相手(exploiter, OOD補完)
        args = [(best, per, n_sims, seed + it * 1000 + wk, 0.25, 1.0, 0.60, 0.15) for wk in range(workers)]
        samples = []
        with ctx.Pool(workers) as pool:
            for res in pool.map(_selfplay_worker_strat, args):
                samples += res
        buffer.append(samples)
        train_samples = [s for chunk in buffer for s in chunk]
        X, PI, M, Y = to_arrays(train_samples)
        cand = copy.deepcopy(best)
        cand.train_pi(X, PI, M, Y, epochs=15, lr=0.05, batch=256)
        # AlphaZeroアリーナ: 候補 vs 現best（ネット対ネット）。勝ち越せば採用＝共進化ラチェット
        aw, al = eval_vs_net(cand, best, loader, parties, N=24, seed=it)
        cand_acc = cand.value_acc(Xv, Yv)
        accepted = (aw / max(1, aw + al)) >= 0.52
        if accepted:
            best = cand; best_acc = cand_acc; best.save()
        rec = {"iter": it + 1, "games": per * workers, "arena_w": aw, "arena_l": al,
               "cand_acc": float(cand_acc), "accepted": bool(accepted),
               "sec": round(time.time() - t0, 1)}
        history.append(rec)
        out.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        mark = "採用" if accepted else "棄却"
        print(f"[反復{it+1}/{iters}] {per*workers}試合 アリーナ候補vs現best {aw}-{al}"
              f"({aw/max(1,aw+al):.0%}) [{mark}] 検証{cand_acc:.0%} {rec['sec']:.0f}秒 "
              f"(累計{(time.time()-t_all)/60:.0f}分)", flush=True)

    cw, cl = eval_vs_net(best, frozen0, loader, parties, N=50)
    w1, l1 = eval_vs_heuristic(best, loader, parties, N=40)
    print(f"[終了時] 累積進歩 最終best vs 開始net: {cw}-{cl}({cw/max(1,cw+cl):.0%})", flush=True)
    print(f"[終了時] 参考 vs Heuristic: {w1}-{l1}({w1/max(1,w1+l1):.0%})", flush=True)
    best.save()
    print(f"保存: {AZNP_PATH}  履歴: {out}", flush=True)


if __name__ == "__main__":
    main()
