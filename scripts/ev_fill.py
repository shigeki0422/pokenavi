"""努力値の余りを埋める（Champions: 各能力最大32・合計66）。
合計66未満の型は、残りをその種の DB（pokemon_evs・そのシーズンの種の最新日）で余り（1〜6の端数）が最も多く置かれている能力へ配る。
同じ大きな振り先（28以上の能力の組）の配分を優先し、無ければ種全体、データが無ければ H→B→D→S→A→C。各能力32を超えない。
型プール生成器・提案（gen_party_pool）・生成集団（_coevo_groups）・工房/想定型（gen_builder_data・gen_archetype_data）が共有する。"""
import collections
import os
import sqlite3

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")
TOTAL, CAP = 66, 32
DEFAULT_ORDER = (0, 2, 4, 5, 1, 3)
SMALL = 6
_ROWS = {}


def _rows(sp, season):
    k = (season, sp)
    if k not in _ROWS:
        con = sqlite3.connect(DB)
        d = con.execute("select max(crawled_date) from pokemon_evs where season=? and pokemon=?", (season, sp)).fetchone()[0]
        rows = []
        if d:
            for *ev, u in con.execute("select ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate from pokemon_evs "
                                      "where season=? and pokemon=? and crawled_date=?", (season, sp, d)):
                ev = [int(x or 0) for x in ev]
                big = frozenset(i for i in range(6) if ev[i] >= 28)
                rows.append((big, [v if 0 < v <= SMALL else 0 for v in ev], float(u or 0)))
        con.close()
        _ROWS[k] = rows
    return _ROWS[k]


def order(sp, ev, season="M-6"):
    """余りを置く能力の順（添字 0=H … 5=S）"""
    big = frozenset(i for i in range(6) if ev[i] >= 28)
    pat, allr = collections.Counter(), collections.Counter()
    for b, small, u in _rows(sp, season):
        for i, v in enumerate(small):
            if v:
                allr[i] += u * v
                if b == big:
                    pat[i] += u * v
    return sorted(range(6), key=lambda i: (-pat[i], -allr[i], DEFAULT_ORDER.index(i)))


def fill(sp, ev, season="M-6"):
    ev = [int(x) for x in ev]
    rem = TOTAL - sum(ev)
    if rem <= 0:
        return ev
    for i in order(sp, ev, season):
        add = min(CAP - ev[i], rem)
        if add > 0:
            ev[i] += add
            rem -= add
        if rem <= 0:
            break
    return ev


def spec_fields(spec):
    head, rest = spec.split("@", 1)
    return [head] + rest.split(":")


def fill_spec(spec, season="M-6", sp=None):
    head, it, na, mv, ev, ab = spec_fields(spec)
    e = fill(sp or head, [int(x) for x in ev.split("/")], season)
    return f"{head}@{it}:{na}:{mv}:{'/'.join(map(str, e))}:{ab}"


def fill_builds(sp, builds, season="M-6"):
    """型の dict（ev・weight・任意で spec）の努力値を埋め、埋めた結果が同じになった型は重みを足して1つにする"""
    out = {}
    for b in builds:
        nb = dict(b)
        nb["ev"] = fill(sp, b["ev"], season)
        if "spec" in b:
            head = spec_fields(b["spec"])[0]
            nb["spec"] = "%s@%s:%s:%s:%s:%s" % (head, b["item"], b["nature"], "|".join(b["moves"]),
                                                "/".join(map(str, nb["ev"])), b.get("ability", ""))
        k = (b["item"], b["nature"], b.get("ability", ""), tuple(sorted(b["moves"])), tuple(nb["ev"]))
        if k in out:
            out[k]["weight"] = round(out[k]["weight"] + b["weight"], 6)
        else:
            out[k] = nb
    return sorted(out.values(), key=lambda b: -b["weight"])


def fill_pool(pool, season="M-6"):
    """type_pool.json（種ごとの builds の list）。前シーズンで作った種は r["season"] の DB を見る"""
    for r in pool:
        r["builds"] = fill_builds(r.get("source_species") or r["species"], r["builds"], r.get("season") or season)
    return pool


def fill_groups(groups, season="M-6"):
    """type_groups.json（{種: {groups: [{builds}]}}）"""
    for sp, v in groups.items():
        for g in v["groups"]:
            g["builds"] = fill_builds(v.get("source_species") or sp, g["builds"], v.get("season") or season)
    return groups


def short_builds(builds):
    """合計66未満の型（週次チェック・テスト用）"""
    return [b for b in builds if sum(b["ev"]) != TOTAL]
