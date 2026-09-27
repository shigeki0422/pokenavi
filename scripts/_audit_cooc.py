"""型プールが生成した技の共起行列を検証する。

使用率（周辺分布）だけでは分からなかった「どの技とどの技が一緒に使われるか」を、
制約と層構造から復元できているかを見る。実型（templates）がある種は実測の共起と比較し、
無い種は不自然な共起（同タイプ火力の重複・物理特殊の混在）を探す。

env: TYPES SEASON(M-6) SP(カンマ区切りで種を指定)
"""
import collections
import itertools
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pool_versions as PV  # noqa: E402
from _gen_type_pool import MV, _plain, con  # noqa: E402

TYPES = os.environ.get("TYPES") or PV.path("type_pool", PV.pointer("season"))


def cooc(builds, wkey=None):
    """P(b|a) の行列と、各技の周辺。"""
    mar = collections.Counter()
    joint = collections.Counter()
    z = 0.0
    for b in builds:
        w = b["weight"] if wkey else 1.0
        mv = b["moves"] if wkey else b
        z += w
        for m in mv:
            mar[m] += w
        for x, y in itertools.permutations(set(mv), 2):
            joint[(x, y)] += w
    return mar, joint, z or 1.0


def main():
    d = {r["species"]: r for r in json.load(open(TYPES))}
    real = collections.defaultdict(list)
    season = os.environ.get("SEASON", "")
    if os.environ.get("REAL") == "md":
        # M-4 は templates に無く、上位構築の md だけが残っている
        from _gen_type_pool import md_builds
        for sp, rows in md_builds().items():
            for r in rows:
                real[sp].append(tuple(r["moves"]))
    else:
        for sp, lab, *mv in con.execute(
                "select pokemon,label,move1,move2,move3,move4 from templates"):
            if season and not lab.startswith(season):
                continue
            real[sp].append(tuple(mv))

    sel = [x for x in os.environ.get("SP", "").split(",") if x]
    MINN = int(os.environ.get("MINN", "15"))
    targets = sel or [sp for sp in real if len(real[sp]) >= MINN]

    print("■ 実型がある種：生成した共起 P(b|a) と実測の比較")
    # 実型が10〜20件だと実測側の P(b|a) 自体がぶれる。完璧な生成器でも残る誤差を
    # 実型のブートストラップで見積もり、「標本誤差」列に出す
    print(f'{"種":12s} {"実型":>4s} {"対の数":>5s} {"平均絶対誤差":>10s} {"標本誤差":>7s} {"最大誤差の対":>34s}')
    rng = random.Random(0)
    agg, noise = [], []
    for sp in targets:
        if sp not in d or len(real.get(sp, [])) < MINN:
            continue
        pm, pj, pz = cooc(d[sp]["builds"], wkey=True)
        rm, rj, rz = cooc(real[sp])
        pairs = [(a, b) for a, b in itertools.permutations(rm, 2)
                 if rm[a] / rz > 0.15 and pm.get(a, 0) / pz > 0.15]
        if not pairs:
            continue
        err = []
        for a, b in pairs:
            p = pj.get((a, b), 0.0) / max(pm.get(a, 0.0), 1e-9)
            r = rj.get((a, b), 0.0) / max(rm.get(a, 0.0), 1e-9)
            err.append((abs(p - r), a, b, p, r))
        err.sort(reverse=True)
        mae = sum(e[0] for e in err) / len(err)
        bs = []
        for _ in range(200):
            bm, bj, _z = cooc([rng.choice(real[sp]) for _ in real[sp]])
            d_ = [abs(bj.get((a, b), 0.0) / bm[a] - rj.get((a, b), 0.0) / rm[a])
                  for a, b in pairs if bm.get(a)]
            if d_:
                bs.append(sum(d_) / len(d_))
        nz = sum(bs) / len(bs) if bs else 0.0
        agg.append(mae)
        noise.append(nz)
        e = err[0]
        print(f'{sp:12s} {len(real[sp]):4d} {len(pairs):5d} {mae*100:9.1f}pt {nz*100:6.1f}pt   '
              f'{e[1]}→{e[2]} 生成{e[3]*100:.0f}% 実測{e[4]*100:.0f}%')
    if agg:
        print(f'\n  平均絶対誤差の中央値: {sorted(agg)[len(agg)//2]*100:.1f}pt'
              f'   標本誤差の中央値: {sorted(noise)[len(noise)//2]*100:.1f}pt')

    print("\n■ 全198種：共起の中で不自然なもの（重みつき）")
    bad = collections.Counter()
    ex = collections.defaultdict(list)
    tot = 0.0
    for sp, r in d.items():
        z = sum(b["weight"] for b in r["builds"]) or 1.0
        for b in r["builds"]:
            w = b["weight"] / z / len(d)
            tot += w
            pl = [m for m in b["moves"] if m in MV and _plain(m)]
            ph = [m for m in pl if MV[m]["cat"] == "physical"]
            spc = [m for m in pl if MV[m]["cat"] == "special"]
            if ph and spc:
                bad["主力に物理と特殊が混在"] += w
                if len(ex["主力に物理と特殊が混在"]) < 3 and b["weight"] / z > 0.01:
                    ex["主力に物理と特殊が混在"].append(
                        f"{sp} {b['weight']/z*100:.1f}% {b['nature']} "
                        f"{'|'.join(b['moves'])}")
            ty = collections.Counter(MV[m]["type"] for m in pl)
            if any(v >= 2 for v in ty.values()):
                bad["同タイプの主力を2本以上"] += w
                if len(ex["同タイプの主力を2本以上"]) < 3 and b["weight"] / z > 0.01:
                    ex["同タイプの主力を2本以上"].append(
                        f"{sp} {b['weight']/z*100:.1f}% {'|'.join(b['moves'])}")
    for k, v in bad.most_common():
        print(f"  {v/tot*100:6.2f}%  {k}")
        for e in ex[k]:
            print(f"            {e}")


if __name__ == "__main__":
    main()
