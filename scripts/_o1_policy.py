"""①Step2: ペイオフ行列(greedy K50)＋ポリシー算出。
グループごとに my選出×oppB を greedy K50 → EV-top3/maximin/Nash → EV-top3は2段目(MCTS K30, 相手temp0.3)で精査。
出力 o1_picks.json。env: K1(50) K2(30) GA_SIMS(120)

※ 2026-09-13 復元: git未追跡のまま git clean で消失し、__pycache__ のバイトコードから
   _mcts_vs_dist とモジュールヘッダを復元した。__main__ のバッチ本体は入力3点
   （v3leak_detail.json / o1_dist.json / m2_parties.json）がすべて失われており
   復元しても動かないため再現していない。現在の利用者は R4 パリティゲート
   （_rust_engine/gate_r4_vsdist.py）で、必要なのは _mcts_vs_dist だけ。
"""
import os, json, statistics
import numpy as np
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "120")
import multiprocessing as mp
import feature1 as _f1
SEASON = os.environ.get("POOL_SEASON", "M-3")
_f1._ensure_loaded(SEASON, 8)
SIMS = int(os.environ.get("GA_SIMS", "120"))
from engine_dispatch import call as _rust_call, ENGINE as _ENGINE
from _v3_rollout import _greedy_3v3
from simulator.selection import solve_zero_sum
L = _f1._W["loader"]


class _LazyM2(list):
    """m2_parties.json は消失している。import 時に読むと全利用者が落ちるので参照時まで遅延する。"""
    def _load(self):
        if not len(self):
            self.extend(e["party"] for e in json.load(open("m2_parties.json")))
        return self
    def __iter__(self): return list.__iter__(self._load())
    def __len__(self):
        try: list.__len__(self._load())
        except FileNotFoundError: pass
        return list.__len__(self)
    def __getitem__(self, i): return list.__getitem__(self._load(), i)


m2 = _LazyM2()


def _mcts_vs_dist(args):
    """subjectの3匹固定、相手は見せ合いからtemp0.3で選出（真の分布）、MCTSプレイ。"""
    pa, sa, pb, seed = args
    if _ENGINE == "rust":
        _rv = _rust_call("mcts_vs_dist", list(pa), list(sa), list(pb), seed, SIMS, SEASON)
        if _rv is not None:
            return _rv
    import random as _r
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import select_party, certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    from train_az2 import _net_ai
    net = _f1._W["net"]; _r.seed(seed); f = BF()
    A = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pa]
    B = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pb]
    mons = [A[i] for i in sa]
    ld = max(range(3), key=lambda j: espd(mons[j], f))
    sel1 = [mons[ld]] + [mons[j] for j in range(3) if j != ld]
    sel2 = select_party(B, A, L, n=3, temperature=0.3, rng=_r)
    s1 = BattleSide(sel1, viewer_label="P1", source6=A)
    s2 = BattleSide(sel2, viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(net, L, 0, 12, seed ^ 1540483477, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True)
    def ai1(m, o, ff): return certain_ko_override(a1(m, o, ff), m, o, ff)
    def ai2(m, o, ff): return certain_ko_override(a2(m, o, ff), m, o, ff)
    return Battle(s1, s2, BF()).run(ai1, ai2)
