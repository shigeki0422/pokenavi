"""対戦プール（gen_pop_m6.json 等）の各ポケモンの型を、型プールから引き直す。

対戦プールの型は素朴なマージナル抽出で作られており、実際の使用率と大きくずれていた
（技の最大誤差が中央値39.4pt・最大83.1pt）。学習も評価もこの集団に対して行っているので、
型推定の改善が勝率に出ない原因になりうる。パーティ構成（誰と誰が同居するか）は
同居率から作られた現行のものを維持し、各ポケモンの型だけ差し替える。

env: POOL(gen_pop_m6.json) TYPES(_local/ai_work/type_pool_M-6.json) OUT SEED(1)
"""
import collections
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pool_versions as PV  # noqa: E402
POOL = os.environ.get("POOL", os.path.join(HERE, "gen_pop_m6.json"))
TYPES = os.environ.get("TYPES") or PV.path("type_pool", PV.pointer("season"))
OUT = os.environ.get("OUT", os.path.join(HERE, "gen_pop_m6_new.json"))
SEED = int(os.environ.get("SEED", "1"))

sys.path.insert(0, HERE)


def spec_of(sp, b):
    return "%s@%s:%s:%s:%s:%s" % (sp, b["item"], b["nature"], "|".join(b["moves"]),
                                  "/".join(str(x) for x in b["ev"]), b["ability"])


def main():
    types = {r["species"]: r["builds"] for r in json.load(open(TYPES))}
    parties = json.load(open(POOL))
    rng = random.Random(SEED)
    miss = collections.Counter()
    out = []
    for p in parties:
        names = [s.split("@")[0] for s in p["party"]]
        for _try in range(200):     # 同じ持ち物を避けられない引き方になったら、パーティごと引き直す
            new, used, dup = draw(names, p, types, rng, miss)
            if not dup:
                break
        out.append({"party": new, "label": p.get("label", "")})
    with open(OUT, "w") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"{OUT}: {len(out)}党" + (f"  型プールに無い種 {dict(miss)}" if miss else ""))


def draw(names, p, types, rng, miss):
    new, dup = [], False
    # 型プールに無い種は元の型のまま使うので、その持ち物を先に数える
    used = {p["party"][i].split("@")[1].split(":")[0] for i, nm in enumerate(names) if nm not in types}
    for i, nm in enumerate(names):
            cand = types.get(nm)
            if not cand:
                miss[nm] += 1
                new.append(p["party"][i])       # 型プールに無い種は元のまま
                continue
            # 同じ持ち物はパーティに1つ（上位構築410党で重複1件）。メガ石の数は制限しない
            # （上位構築はメガ石2個が84%。1個に絞ると2匹目のメガ種の持ち物が型プールとずれた）
            pick = [b for b in cand if b["item"] not in used]
            if not pick:
                pick, dup = cand, True
            w = [b["weight"] for b in pick]
            b = rng.choices(pick, weights=w)[0]
            used.add(b["item"])
            new.append(spec_of(nm, b))
    return new, used, dup


if __name__ == "__main__":
    main()
