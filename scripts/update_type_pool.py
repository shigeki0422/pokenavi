"""週次: 最新の使用率で型プール → 系統表を作り、ページ用の版として積み上げ、想定型と 1v1 のデータを同時に作り直す。

  1. 型プール: シーズン中に使用率に出た全種（_gen_type_pool.generate_one。詳細データの最新日、圏外に落ちた種はその種の最新日）。
     シーズン中の詳細データが無い種は、詳細のある直近のシーズンで作る（season を記録）。
     技が4つに満たず生成器が作れない種（メタモン）は、技・持ち物・性格・努力値の周辺分布の積で作る。
  2. 系統表: scripts/arch_groups.py
  3. _local/ai_work/pools/<シーズン>/<日付>/ に type_pool.json・type_groups.json・meta.json を書く（既にあれば止める。上書きしない）
  4. scripts/pool_versions.json の page を新しい版へ向け、gen_builder_data.py → gen_archetype_data.py を流す（archNo を揃えるため必ず両方）
  5. チェックと前の page 版との差分レポート（scripts/pool_checks.py）を版のフォルダの report.md に書く。
     プールと系統表のエラーなら 4 の前に止める（ポインタも生成物も変えない）。出力の整合のエラーならポインタを戻して生成物を作り直す。終了コード1

env: POOL_SEASON（既定: DB の最新シーズン） VERSION（既定: <シーズン>/<今日>） JOBS（並列数） NO_PAGE=1（ポインタと生成物を変えない）
"""
import collections
import datetime
import json
import multiprocessing
import os
import re
import sqlite3
import subprocess
import sys
import time
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DB = os.path.join(HERE, "pokenavi.db")
sys.path.insert(0, HERE)
import pool_versions as PV  # noqa: E402


def _seasons():
    con = sqlite3.connect(DB)
    rows = [r[0] for r in con.execute("select distinct season from pokemon_usage")]
    con.close()
    return sorted(rows, key=lambda s: int(re.match(r"M-(\d+)$", s).group(1)) if re.match(r"M-(\d+)$", s) else -1,
                  reverse=True)


SEASON = os.environ.get("POOL_SEASON") or _seasons()[0]
os.environ["SEASON"] = SEASON
os.environ.setdefault("N", "0")
import _gen_type_pool as G  # noqa: E402


def _init():
    G.con = sqlite3.connect(DB)


def _gen(args):
    sp, seed = args
    return G.generate_one(sp, seed)


def simple_builds(sp):
    return G.simple_builds(sp)


def form_fixes(pool):
    """DB のフォルム誤登録を補正する（_gen_type_pool.form_fix。例: ルガルガン(昼) の かたいツメ 100% → ルガルガン(たそがれ)）。
    補正先の種がすでにあるときは、詳細データの新しい方を残す。戻り値 {元の種: 補正先}"""
    fixed = {}
    by = {r["species"]: r for r in pool}
    for r in list(pool):
        to = G.form_fix(r["species"])
        if not to:
            continue
        src = r["species"]
        old = by.get(to)
        if old is not None:
            if (G.latest("pokemon_moves", src) or "") < (G.latest("pokemon_moves", to) or ""):
                pool.remove(r)
                continue
            pool.remove(old)
        G.rename_species(r, to)
        by[to] = r
        fixed[src] = to
    return fixed


def targets():
    """シーズン中に使用率に出た全種。最新日の順位順 → 圏外に落ちた種（最後に出た日の新しい順・最高順位順）"""
    con = G.con
    d = con.execute("select max(crawled_date) from pokemon_usage where season=?", (SEASON,)).fetchone()[0]
    rows = con.execute(
        "select pokemon, max(crawled_date), min(rank), min(case when crawled_date=? then rank end) "
        "from pokemon_usage where season=? group by pokemon", (d, SEASON)).fetchall()
    rows.sort(key=lambda r: (r[3] is None, r[3] or 0, [-ord(c) for c in r[1]], r[2]))
    return [r[0] for r in rows], d


def detail_season(sp):
    """その種の詳細データ（技）がある直近のシーズン"""
    have = {r[0] for r in G.con.execute("select distinct season from pokemon_moves where pokemon=?", (sp,))}
    return next((s for s in _seasons() if s in have), None)


def git_info():
    def run(*a):
        try:
            return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        except OSError:
            return ""
    files = ["scripts/_gen_type_pool.py", "scripts/arch_groups.py", "scripts/update_type_pool.py"]
    return {"commit": run("rev-parse", "HEAD"), "dirty": run("status", "--porcelain", *files).splitlines()}


def main():
    t0 = time.time()
    version = os.environ.get("VERSION") or f"{SEASON}/{datetime.date.today().isoformat()}"
    out_dir = PV.version_dir(version)
    if os.path.exists(out_dir):
        sys.exit(f"{out_dir} は既にあります（版は上書きしない）。VERSION=<シーズン>/<別名> で別の版にしてください")
    sps, usage_date = targets()
    cur = [sp for sp in sps if detail_season(sp) == SEASON]
    other = {sp: detail_season(sp) for sp in sps if detail_season(sp) not in (SEASON,)}
    jobs = int(os.environ.get("JOBS") or max(1, (os.cpu_count() or 2) - 2))
    with multiprocessing.get_context("spawn").Pool(jobs, initializer=_init) as p:
        # 乱数の種は種名から決める（順位の並びで変わると、使用率が同じでも特性などの割り振りが週ごとに揺れる）
        res = p.map(_gen, [(sp, zlib.crc32(sp.encode())) for sp in cur], chunksize=1)
    pool, simple, none = [], [], []
    for sp, r in zip(cur, res):
        if not r or not r["builds"]:
            r = simple_builds(sp)
            if not r:
                none.append(sp)
        if r:
            if r.get("simple"):
                simple.append(sp)
            pool.append(r)
    form_fixed = form_fixes(pool)
    t_pool = time.time() - t0
    # 詳細データが今シーズンに無い種は、詳細のある直近のシーズンで作る（別プロセス: 生成器はシーズンを import 時に読む）
    fallback = {}
    for s in sorted({s for s in other.values() if s}):
        spl = [sp for sp, x in other.items() if x == s]
        os.makedirs(PV.POOLS, exist_ok=True)
        tmp = os.path.join(PV.POOLS, f".tmp_{os.getpid()}_{s}.json")
        env = dict(os.environ, SEASON=s, SPECIES=",".join(spl), OUT=tmp, N=os.environ["N"])
        subprocess.run([sys.executable, os.path.join(HERE, "_gen_type_pool.py")], env=env, check=True,
                       stderr=subprocess.DEVNULL)
        for r in json.load(open(tmp)):
            r["season"] = s
            pool.append(r)
            fallback[r["species"]] = s
        os.remove(tmp)
    none += [sp for sp, s in other.items() if sp not in fallback]
    import ev_fill
    ev_fill.fill_pool(pool, SEASON)
    t_fb = time.time() - t0 - t_pool

    import arch_groups as A
    groups = {}
    for r in pool:
        _, gtab = A.group_species(r["species"], r["builds"])
        groups[r["species"]] = {"rank": None, "groups": gtab}
        if r.get("season"):
            groups[r["species"]]["season"] = r["season"]
        if r.get("source_species"):
            groups[r["species"]]["source_species"] = r["source_species"]
    for sp, rk in G.con.execute("select pokemon, rank from pokemon_usage where season=? and crawled_date=?",
                                (SEASON, usage_date)):
        sp = form_fixed.get(sp, sp)
        if sp in groups:
            groups[sp]["rank"] = rk
    t_grp = time.time() - t0 - t_pool - t_fb

    os.makedirs(out_dir)
    with open(os.path.join(out_dir, "type_pool.json"), "w") as f:
        json.dump(pool, f, ensure_ascii=False, indent=1, default=float)
    with open(os.path.join(out_dir, "type_groups.json"), "w") as f:
        json.dump(groups, f, ensure_ascii=False, default=float)
    params = {k: getattr(G, k) for k in dir(G) if k.isupper() and isinstance(getattr(G, k), (int, float, str, bool))}
    meta = {
        "version": version, "season": SEASON, "created": datetime.datetime.now().isoformat(timespec="seconds"),
        "usage_rank_date": usage_date, "detail_date": G.latest("pokemon_moves", None),
        "species": len(pool),
        "older_detail_date": {sp: G.latest("pokemon_moves", sp) for sp in cur
                              if G.latest("pokemon_moves", sp) != G.latest("pokemon_moves", None)},
        "fallback_season": fallback, "simple_product": simple, "not_generated": none, "form_fixed": form_fixed,
        "params": params, "git": git_info(), "jobs": jobs,
        "seconds": {"pool": round(t_pool), "fallback": round(t_fb), "groups": round(t_grp)},
    }
    with open(os.path.join(out_dir, "meta.json"), "w") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print(f"{out_dir}: {len(pool)}種（型プール {t_pool:.0f}s・前シーズン {t_fb:.0f}s・系統 {t_grp:.0f}s）"
          + (f"  前シーズンで作成 {fallback}" if fallback else "") + (f"  周辺分布の積 {simple}" if simple else "")
          + (f"  作れず {none}" if none else "") + (f"  フォルム補正 {form_fixed}" if form_fixed else ""))
    import pool_checks as C
    prev = PV.pointer("page")
    rep = os.path.join(out_dir, "report.md")

    def finish(stage):
        t = time.time()
        E, W, L = C.run(prev, version, stage)
        meta["seconds"]["checks_" + stage] = round(time.time() - t)
        meta["seconds"]["total"] = round(time.time() - t0)
        with open(os.path.join(out_dir, "meta.json"), "w") as f:
            json.dump(meta, f, ensure_ascii=False, indent=1)
        with open(rep, "w") as f:
            f.write("\n".join(L) + "\n")
        print(f"チェック（{stage}）: エラー {len(E)}件・警告 {len(W)}件  → {rep}")
        for a, b, c in E[:30]:
            print(f"  ERROR [{a}] {b} {c}")
        for k, v in collections.Counter(w[0] for w in W).most_common():
            print(f"  WARN  {k}: {v}件")
        return E

    if finish("pool"):
        sys.exit(f"エラーがあるのでページ用の版は {prev} のまま（生成物も変えていない）")
    if os.environ.get("NO_PAGE") == "1":
        return
    py = sys.executable

    def pages():
        subprocess.run([py, os.path.join(HERE, "gen_builder_data.py")], cwd=ROOT, check=True)
        subprocess.run([py, os.path.join(HERE, "gen_archetype_data.py")], cwd=ROOT, check=True)
    PV.set_pointer("page", version)
    t1 = time.time()
    pages()
    meta["seconds"]["pages"] = round(time.time() - t1)
    if finish("all"):
        PV.set_pointer("page", prev)
        pages()
        sys.exit(f"出力の整合にエラーがあるのでページ用の版を {prev} に戻し、生成物も作り直した")
    print(f"page: {prev} → {version}  合計 {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
