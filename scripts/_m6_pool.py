"""AI の学習・評価で使うパーティ集合の供給元（1箇所）。

提案キャッシュ(suggest_cache.json)は222軸1,110党あるが、使用率下位の軸まで含めると
製品が実際に相手にしないオフメタ対面で AI を測ることになる。既定では使用率上位の軸だけを使う。

env:
  PARTIES        供給元json（既定 suggest_cache.json）。提案キャッシュ / [{"party":[…]}…] /
                 共進化の出力 {"parties":[{"specs":[…]}…]} のいずれも読む
  MAX_CORE_RANK  軸(コア種)の使用率順位の上限。既定50。0で無制限
  POOL_SEASON    順位を引くシーズン（既定 M-6）
"""
import json
import os
import sqlite3

_DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")


def core_ranks(season=None):
    """{種名: 使用率順位}（最新クロール日）。"""
    season = season or os.environ.get("POOL_SEASON", "M-6")
    con = sqlite3.connect(_DB)
    d = con.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=?",
                    (season,)).fetchone()[0]
    rows = con.execute(
        "SELECT pokemon, rank FROM pokemon_usage "
        "WHERE season=? AND rule='single' AND crawled_date=?", (season, d)).fetchall()
    con.close()
    return {n: r for n, r in rows}


def _core_of(key):
    """提案キャッシュのキーから軸の種名を取り出す。おまかせ（コア指定なし）は None。"""
    try:
        core = json.loads(key)[0]
    except Exception:
        return None
    if not core:
        return None
    c = core[0]
    return (c["sp"] if isinstance(c, dict) else str(c).split("@")[0])


def load_parties(path=None, max_core_rank=None, season=None):
    """6体パーティのspec列。同一6体構成は1つに畳む。"""
    path = path or os.environ.get("PARTIES", "suggest_cache.json")
    if max_core_rank is None:
        max_core_rank = int(os.environ.get("MAX_CORE_RANK", "50"))
    d = json.load(open(path, encoding="utf-8"))
    out = []
    if isinstance(d, dict) and "parties" in d:              # 共進化の出力
        out = [list(x["specs"]) for x in d["parties"] if len(x.get("specs", [])) == 6]
    elif isinstance(d, dict):                               # 提案キャッシュ
        ranks = core_ranks(season) if max_core_rank else {}
        for k in sorted(d):
            if max_core_rank:
                sp = _core_of(k)
                # おまかせ軸は常に採用（特定の種に紐づかないため）
                if sp is not None and ranks.get(sp, 9999) > max_core_rank:
                    continue
            for r in d[k].get("results", []):
                sp6 = r.get("specs")
                if sp6 and len(sp6) == 6:
                    out.append(list(sp6))
    else:
        for e in d:
            sp6 = e["party"] if isinstance(e, dict) else e
            if sp6 and len(sp6) == 6:
                out.append(list(sp6))
    seen, uniq = set(), []
    for sp6 in out:
        k = tuple(sorted(sp6))
        if k not in seen:
            seen.add(k)
            uniq.append(sp6)
    return uniq


def describe(path=None, max_core_rank=None):
    n = len(load_parties(path, max_core_rank))
    lim = max_core_rank if max_core_rank is not None else int(os.environ.get("MAX_CORE_RANK", "50"))
    return f"{n}党（軸は使用率{lim}位以内）" if lim else f"{n}党（全軸）"
