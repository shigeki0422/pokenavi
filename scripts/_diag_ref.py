"""パーティ診断の rank 用の参照分布（diag_ref_m6.json）を作る。相手集団と同じ生成器（_guide_opps）で別シードの NP 党を引き、
それぞれの全体有利度を /guide と同じ計算（相手 guide_pool_m6.json 全体・同じ分け方とシード）で求めて保存する。
シーズン・相手集団・較正を替えたら作り直す。
使い方: POOL_SEASON=M-6 USAGE_SEASON=M-6 ENGINE=rust venv/bin/python _diag_ref.py   env: NP(300) SEED(1) PROCS(12) NC(サーバの _WORKERS と同じ既定)
"""
import json
import multiprocessing as mp
import os
import random
import time

import _guide_opps as GO
import _diagnose as DG
import _select_guide as SG

SEASON = os.environ.get("POOL_SEASON", "M-6")


def main():
    np_, seed = int(os.environ.get("NP", "300")), int(os.environ.get("SEED", "1"))
    nc = int(os.environ.get("NC") or 0) or max(2, (os.cpu_count() or 2) - 1)
    GO.C.load()
    rng = random.Random(seed)
    parties = []
    while len(parties) < np_:
        specs = GO.C.instantiate(GO.C.gen_party(rng), rng)
        if GO.C.plausible(specs):
            parties.append(specs)
    opps = SG.load_pool()
    t = time.time()
    with mp.get_context("fork").Pool(int(os.environ.get("PROCS", "12"))) as pool:
        parts = pool.map(DG.rows_at, [j for p in parties for j in DG.chunk_jobs(p, opps, SEASON, nc)], chunksize=1)
    adv = [round(DG.overall_adv(DG.merge(parts[k * nc:(k + 1) * nc], nc, len(opps))), 4) for k in range(len(parties))]
    json.dump({"season": SEASON, "seed": seed, "nc": nc, "n_opp": len(opps), "adv": sorted(adv)},
              open(DG.REF_FILE, "w", encoding="utf-8"))
    s = sorted(adv)
    print(f"{len(adv)}党 {time.time() - t:.0f}s → {os.path.basename(DG.REF_FILE)}  "
          f"p10={s[len(s) // 10]:.3f} 中央={s[len(s) // 2]:.3f} p90={s[len(s) * 9 // 10]:.3f}")


if __name__ == "__main__":
    main()
