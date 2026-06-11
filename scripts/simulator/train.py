"""自己対戦ループ（Phase 4: 選出戦略テーブルの学習）。

登録パーティ対ごとに、AI同士の自己対戦（数千〜数万試合）で選出利得行列を推定し、
ゼロサムゲームのナッシュ均衡（混合選出戦略）を解いてテーブル化・キャッシュする。
これが「相手パーティ構成→どの3体をどの先頭で選出するか」の学習成果物。

戦闘中の行動方策（SearchAI）は belief により対戦ごとにオンラインで適応するため、
ここで重み学習は行わない（選出のメタ戦略のみを学習・固定する）。
"""
import json
import random
from itertools import combinations
from pathlib import Path
from typing import List, Optional

from .data import DataLoader
from .ai import HeuristicAI
from .env import RegisteredParty, load_registered_parties, heuristic_selection
from .selection import solve_matchup, sample_selection, selection_to_party

CACHE_PATH = Path(__file__).resolve().parent.parent / "selection_table.json"


def train_selection_table(loader: DataLoader, parties: List[RegisteredParty],
                          ai=None, k: int = 8, samples: int = 8,
                          pair_limit: Optional[int] = None, season: str = "M-2",
                          out_path: Path = CACHE_PATH, verbose: bool = True) -> dict:
    """各パーティ対の選出ナッシュ均衡を解き、(my_id, opp_id)→混合選出戦略 をキャッシュ。

    戻り値はキャッシュ dict。総自己対戦数も報告する。
    """
    ai = ai or HeuristicAI()
    cache: dict = {}
    total_battles = 0
    ids = [p.party_id for p in parties]
    by_id = {p.party_id: p for p in parties}
    pairs = list(combinations(ids, 2))
    if pair_limit:
        pairs = pairs[:pair_limit]

    for n, (i, j) in enumerate(pairs):
        res = solve_matchup(by_id[i], by_id[j], loader, ai=ai, k=k,
                            samples=samples, season=season, seed=n)
        cache[f"{i}-{j}"] = {"sels": [list(s) for s in res["sels1"]], "mix": res["x"]}
        cache[f"{j}-{i}"] = {"sels": [list(s) for s in res["sels2"]], "mix": res["y"]}
        total_battles += len(res["sels1"]) * len(res["sels2"]) * samples
        if verbose and (n + 1) % 5 == 0:
            print(f"  {n+1}/{len(pairs)} 対戦カード解析済 (累計 {total_battles} 自己対戦)")

    out_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    if verbose:
        print(f"選出戦略テーブル保存: {out_path}  ({len(pairs)}カード / 計 {total_battles} 自己対戦)")
    return cache


def _solve_one(args):
    """1カードの選出ナッシュを解くワーカー（プロセス毎に自前の loader を生成）。"""
    i, j, k, samples, season, seed = args
    from .simulate import get_loader
    from .env import load_registered_parties
    loader = get_loader()
    by_id = {p.party_id: p for p in load_registered_parties(loader, complete_only=True, season=season)}
    res = solve_matchup(by_id[i], by_id[j], loader, k=k, samples=samples, season=season, seed=seed)
    return (i, j, [list(s) for s in res["sels1"]], res["x"],
            [list(s) for s in res["sels2"]], res["y"], len(res["sels1"]) * len(res["sels2"]) * samples)


def train_selection_table_parallel(parties: List[RegisteredParty], k: int = 8, samples: int = 8,
                                   workers: Optional[int] = None, season: str = "M-2",
                                   out_path: Path = CACHE_PATH, verbose: bool = True) -> dict:
    """全カードの選出ナッシュをマルチプロセスで並列に解いてキャッシュする（読み取り専用DBで安全）。"""
    import multiprocessing as mp
    import os
    ids = [p.party_id for p in parties]
    pairs = list(combinations(ids, 2))
    args = [(i, j, k, samples, season, n) for n, (i, j) in enumerate(pairs)]
    workers = workers or max(1, (os.cpu_count() or 2) - 1)
    cache: dict = {}
    total = 0
    ctx = mp.get_context("spawn")
    with ctx.Pool(workers) as pool:
        for n, (i, j, s1, x, s2, y, b) in enumerate(pool.imap_unordered(_solve_one, args)):
            cache[f"{i}-{j}"] = {"sels": s1, "mix": x}
            cache[f"{j}-{i}"] = {"sels": s2, "mix": y}
            total += b
            if verbose and (n + 1) % 50 == 0:
                print(f"  {n+1}/{len(pairs)} カード解析済 (累計 {total} 自己対戦)", flush=True)
    out_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    if verbose:
        print(f"選出戦略テーブル保存: {out_path}  ({len(pairs)}カード / 計 {total} 自己対戦 / {workers}並列)")
    return cache


def load_selection_table(path: Path = CACHE_PATH) -> dict:
    if not Path(path).exists():
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def make_nash_selection(cache: dict, my_id: int, opp_id: int, seed: int = 0):
    """キャッシュから (my_id, opp_id) の混合選出戦略を引く SelectionPolicy を返す。
    未学習カードはヒューリスティック選出にフォールバック。"""
    rng = random.Random(seed)
    entry = cache.get(f"{my_id}-{opp_id}")

    def policy(my6, opp6, loader):
        if entry is None:
            return heuristic_selection(my6, opp6, loader)
        sels = [tuple(s) for s in entry["sels"]]
        sel = sample_selection(sels, entry["mix"], rng)
        return selection_to_party(my6, sel)

    return policy


if __name__ == "__main__":
    import sys
    from .simulate import get_loader
    loader = get_loader()
    parties = load_registered_parties(loader, complete_only=True)
    print(f"使用可能な登録パーティ: {len(parties)}", flush=True)
    if len(sys.argv) > 1 and sys.argv[1] == "full":
        # 全カードを並列で先計算（python -m simulator.train full [workers] [n_parties]）
        workers = int(sys.argv[2]) if len(sys.argv) > 2 else None
        if len(sys.argv) > 3:
            parties = parties[:int(sys.argv[3])]
        train_selection_table_parallel(parties, workers=workers)
    else:
        limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
        train_selection_table(loader, parties, pair_limit=limit)
