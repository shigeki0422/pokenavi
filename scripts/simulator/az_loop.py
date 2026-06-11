"""完全自律 AlphaZero ループ（pure Python + numpyネット・小規模デモ）。

- 自己対戦は MCTS 自身が方策（Dirichletノイズ＋温度で探索）。
- 学習ターゲットは MCTS の訪問分布π（方策）＋最終勝敗（価値）＝本来のAlphaZero。
- 選出にもε探索を入れ、ペリッパー始動など普段選ばれない構築も試す（雨等の自力発見を狙う）。
- これを反復（自己対戦→学習→自己対戦…）し、方策・価値を共進化させる。

オーバーサンプリングに頼らず、探索だけで雨シナジー等が学習されるかを検証する基盤。
使い方: python -m simulator.az_loop [iters] [games_per] [n_sims]
"""
import copy
import random
import sys
from itertools import combinations

import numpy as np

from .simulate import get_loader
from .env import load_registered_parties, build_party, heuristic_selection
from .battle import Battle, BattleSide, BattleField
from .ai import HeuristicAI, _forced_charging_action
from .belief import OpponentBelief
from .features import encode_state, feature_dim
from .battle import Action
from .alphazero import legal_actions_indexed, mcts_search, ACTION_DIM
from .az_np import PVNetNP, AZNP_PATH
from .search_ai import SearchAI
from .train_az_np import rain_probe


def explore_selection(party6, opp6, loader, rng, eps=0.15, k=6):
    """多様性のある選出: 有望top-k候補から一様サンプル（妥当だが多様なマッチアップ）。
    小確率epsで完全ランダム（真の探索）。決定的選出（毎回同じ3体）による学習分布の偏りを防ぐ。"""
    from .selection import candidate_selections
    if len(party6) <= 3:
        return list(party6)
    if rng.random() < eps:
        idxs = rng.sample(range(len(party6)), 3)
        rng.shuffle(idxs)
        return [party6[i] for i in idxs]
    cands = candidate_selections(party6, opp6, k)
    if not cands:
        return heuristic_selection(party6, opp6, loader)
    sel = rng.choice(cands)
    return [party6[i] for i in sel if i < len(party6)]


class _SelfPlayAI:
    """MCTS自己対戦AI: 探索付きで指し、(状態, 訪問分布π, 合法手) を記録する。"""
    def __init__(self, loader, net, n_sims, dir_eps, temperature, rng, season="M-2"):
        self.net = net; self.n_sims = n_sims
        self.dir_eps = dir_eps; self.temperature = temperature; self.rng = rng
        # 探索内の相手モデルをネット化（中級＝ネット級の相手前提で読む）。HeuristicAI(初級)では弱い相手しか経験できない。
        from .alphazero import NetGreedyAI
        self.opp_ai = NetGreedyAI(net); self._fallback = HeuristicAI()
        self._det = SearchAI(loader, season=season, seed=rng.randint(0, 1 << 30))
        self.records = []  # (features, pi_dict, legal_idxs)

    def __call__(self, my_side, opp_side, field):
        me = my_side.active
        if not me.is_alive:
            return Action(type="pass")
        forced = _forced_charging_action(me)
        if forced:
            return forced
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self._det.loader, self._det.season)
        belief.observe_disclosure(my_side.opp_view)
        my_is_s1 = (my_side.field_idx == 0)
        legal = [ix for _, ix in legal_actions_indexed(my_side, opp_side, field)]
        s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
        cs1, cs2, cfield = copy.deepcopy((s1, s2, field))
        copp = cs2 if my_is_s1 else cs1
        cfg = self._det._sample_opp_config(opp_side, belief)
        for poke, c in zip(copp.party, cfg):
            if c is not None:
                self._det._determinize(poke, c)
        feat = encode_state(my_side, opp_side, field)
        b = Battle(cs1, cs2, cfield)
        act, pi = mcts_search(b, my_is_s1, self.net, self.opp_ai, n_sims=self.n_sims,
                              dir_eps=self.dir_eps, temperature=self.temperature,
                              return_pi=True, rng=self.rng)
        if act is None:
            return self._fallback(my_side, opp_side, field)
        if pi and len(legal) > 1:
            self.records.append((feat, pi, legal))
        return act


def selfplay_game(loader, parties, net, n_sims, rng, dir_eps=0.25, temperature=1.0, eps_sel=0.35):
    pa, pb = rng.sample(parties, 2)
    a1 = build_party(pa, loader); a2 = build_party(pb, loader)
    s1 = BattleSide(explore_selection(a1, a2, loader, rng, eps_sel))
    s2 = BattleSide(explore_selection(a2, a1, loader, rng, eps_sel))
    s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
    ai1 = _SelfPlayAI(loader, net, n_sims, dir_eps, temperature, rng)
    ai2 = _SelfPlayAI(loader, net, n_sims, dir_eps, temperature, rng)
    w = Battle(s1, s2).run(ai1, ai2)
    samples = []
    if w != 0:
        for feat, pi, legal in ai1.records:
            samples.append((feat, pi, legal, 1.0 if w == 1 else 0.0))
        for feat, pi, legal in ai2.records:
            samples.append((feat, pi, legal, 1.0 if w == 2 else 0.0))
    return samples


def to_arrays(samples):
    X = np.array([s[0] for s in samples], float)
    Y = np.array([s[3] for s in samples], float)
    PI = np.zeros((len(samples), ACTION_DIM))
    M = np.zeros((len(samples), ACTION_DIM))
    for k, s in enumerate(samples):
        for ix in s[2]:
            M[k, ix] = 1.0
        for a, p in s[1].items():
            PI[k, a] = p
    return X, PI, M, Y


def run_loop(iters=2, games_per=150, n_sims=16, hidden=96, seed=0, verbose=True, fresh=True):
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    # fresh=True: まっさらから開始（探索だけで創発するかの検証）。Falseで既存netから継続。
    net = PVNetNP(feature_dim(), hidden=hidden, seed=seed) if fresh else (PVNetNP.load() or PVNetNP(feature_dim(), hidden=hidden, seed=seed))
    rng = random.Random(seed)
    for it in range(iters):
        if verbose:
            print(f"[反復 {it+1}/{iters}] MCTS自己対戦 {games_per} 試合（探索あり）...", flush=True)
        samples = []
        for g in range(games_per):
            samples += selfplay_game(loader, parties, net, n_sims, rng)
        X, PI, M, Y = to_arrays(samples)
        if verbose:
            print(f"  サンプル {len(samples)} で学習...", flush=True)
        net.train_pi(X, PI, M, Y, epochs=20, lr=0.06, batch=256)
        d, pos = rain_probe(net, loader)
        if verbose:
            print(f"  価値精度={net.value_acc(X,Y):.1%}  雨プローブΔ={d:+.4f}(正{pos:.0%})", flush=True)
    net.save()
    if verbose:
        print(f"保存: {AZNP_PATH}")
    return net


def _selfplay_worker(args):
    """並列ワーカー: 与えられたネットで n_games 試合の MCTS 自己対戦サンプルを返す。"""
    net, n_games, n_sims, seed, dir_eps, temperature, eps_sel = args
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    rng = random.Random(seed)
    out = []
    for _ in range(n_games):
        out += selfplay_game(loader, parties, net, n_sims, rng, dir_eps, temperature, eps_sel)
    return out


def run_loop_parallel(iters=4, games_per=400, n_sims=24, hidden=128, workers=None,
                      seed=0, fresh=True, verbose=True, log=None):
    """自己対戦をマルチプロセスで並列化した AlphaZero ループ（実用的な大規模化）。"""
    import multiprocessing as mp
    import os
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    net = PVNetNP(feature_dim(), hidden=hidden, seed=seed) if fresh else (PVNetNP.load() or PVNetNP(feature_dim(), hidden=hidden, seed=seed))
    workers = workers or max(1, (os.cpu_count() or 2) - 1)
    ctx = mp.get_context("spawn")
    history = []
    for it in range(iters):
        per = max(1, games_per // workers)
        args = [(net, per, n_sims, seed + it * 1000 + w, 0.25, 1.0, 0.35) for w in range(workers)]
        samples = []
        with ctx.Pool(workers) as pool:
            for res in pool.map(_selfplay_worker, args):
                samples += res
        X, PI, M, Y = to_arrays(samples)
        net.train_pi(X, PI, M, Y, epochs=20, lr=0.06, batch=256)
        d, pos = rain_probe(net, loader)
        rec = {"iter": it + 1, "samples": len(samples), "games": per * workers,
               "value_acc": net.value_acc(X, Y), "rain_delta": d, "rain_pos": pos}
        history.append(rec)
        line = (f"[反復 {it+1}/{iters}] {per*workers}試合/{workers}並列 → サンプル{len(samples)} "
                f"価値精度{rec['value_acc']:.1%} 雨Δ{d:+.4f}(正{pos:.0%})")
        if verbose:
            print(line, flush=True)
        if log:
            log.append(rec)
    net.save()
    return net, history


if __name__ == "__main__":
    import json
    from pathlib import Path
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    games = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    sims = int(sys.argv[3]) if len(sys.argv) > 3 else 24
    _net, _hist = run_loop_parallel(iters=iters, games_per=games, n_sims=sims)
    _out = Path(__file__).resolve().parent.parent / "reports" / "az_history.json"
    _out.parent.mkdir(parents=True, exist_ok=True)
    _out.write_text(json.dumps(_hist, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"履歴保存: {_out}")
