"""選出ガイドの相手集団（guide_pool_m6.json）を作る。使用率＋同居率の生成器（_coevo_groups.gen_party＝_pop_gen の使用率Zipf＋同居率、
系統はシーズン固定版の系統の割合）で NP 党を引き、型は系統の中から重みで引く（instantiate）。提案と同じ判定 plausible を通したものだけ。
シーズンを替えたら作り直す。
使い方: venv/bin/python _guide_opps.py [OUT=guide_pool_m6.json]   env: NP(3000) SEED(0)
"""
import json
import os
import random
import sys
from collections import Counter

import pool_versions as _PV

os.environ.setdefault("GROUPS", _PV.path("type_groups", _PV.pointer("season")))
import _coevo_groups as C


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "guide_pool_m6.json"
    C.load()
    rng = random.Random(int(os.environ.get("SEED", "0")))
    pop = []
    while len(pop) < int(os.environ.get("NP", "3000")):
        specs = C.instantiate(C.gen_party(rng), rng)
        if C.plausible(specs):
            pop.append({"party": specs})
    json.dump(pop, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    sp = Counter(x.split("@")[0] for p in pop for x in p["party"])
    print(f"{len(pop)}党 → {out}  種{len(sp)}  上位: " + " ".join(f"{n}{c}" for n, c in sp.most_common(10)))


if __name__ == "__main__":
    main()
