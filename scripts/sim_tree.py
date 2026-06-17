"""tree d2（探索あり・強いAI）で対戦を並列実行する共通ランナー。

総当たり・実戦敗因・単一シミュレーションを、弱いNetGreedyAIでなく tree d2 で回すため、
1戦ずつをワーカープロセスに分散する（tree d2 は1戦十数秒のため逐次では総当たりが非現実的）。
fork方式：親プロセスでロード済みのネット/ローダーを子が継承する（再import・再ロード不要）。
"""
import os
import random
import multiprocessing as mp

_W = {}


def _ensure_loaded(season, det):
    """親プロセスでネット/ローダーを一度だけロード（forkで子に継承される）。"""
    if "net" not in _W:
        from simulator.simulate import get_loader
        from simulator.az_np import PVNetNP
        _W["loader"] = get_loader()
        _W["net"] = PVNetNP.load()
    _W["season"] = season
    _W["det"] = det


def _run_one(args):
    specs1, specs2, sel_temp, seed = args
    random.seed(seed)
    from simulator.pokemon import build_from_spec
    from simulator.learned_selection import learned_select_party as select_party  # MCTS教師の学習選出(無効時はheuristic自動フォールバック)
    from simulator.battle import Battle, BattleSide
    from simulator.belief import OpponentBelief
    from train_az2 import _net_ai
    L = _W["loader"]; net = _W["net"]; season = _W["season"]; det = _W["det"]
    ai1 = _net_ai(net, L, 0, 12, seed, tree=True, tree_depth=2, tree_k=3, tree_det=det)
    ai2 = _net_ai(net, L, 0, 12, seed ^ 0x5bd1e995, tree=True, tree_depth=2, tree_k=3, tree_det=det)
    A = [build_from_spec(sp, L, season=season, randomize=True) for sp in specs1]
    B = [build_from_spec(sp, L, season=season, randomize=True) for sp in specs2]
    s1 = BattleSide(select_party(A, B, L, n=min(3, len(A)), temperature=sel_temp))
    s2 = BattleSide(select_party(B, A, L, n=min(3, len(B)), temperature=sel_temp))
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    w = Battle(s1, s2).run(ai1, ai2)
    opp_alive = []
    for p in s2.party:
        if p.is_alive:
            boosts = (getattr(p, "stage_attack", 0) + getattr(p, "stage_sp_attack", 0)
                      + getattr(p, "stage_speed", 0) + getattr(p, "stage_defense", 0)
                      + getattr(p, "stage_sp_defense", 0))
            opp_alive.append((p.name, boosts))
    own_dead = [p.name for p in s1.party if not p.is_alive]
    return {"w": w, "sel1": [p.name for p in s1.party], "sel2": [p.name for p in s2.party],
            "opp_alive": opp_alive, "own_dead": own_dead}


def parallel_battles(specs1_parsed, specs2_parsed, n, season="M-2", det=8,
                     sel_temp=0.6, base_seed=7000):
    """n戦を tree d2 で並列実行（fork）し、各戦の結果dictのリストを返す。"""
    _ensure_loaded(season, det)
    workers = min(n, max(1, (os.cpu_count() or 2) - 2))
    args = [(specs1_parsed, specs2_parsed, sel_temp, base_seed + i) for i in range(n)]
    ctx = mp.get_context("fork")
    with ctx.Pool(workers) as pool:
        return pool.map(_run_one, args)
