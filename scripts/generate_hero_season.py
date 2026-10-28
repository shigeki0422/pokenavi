"""シーズン考察記事の hero 画像（720x360・使用率ランキング表）を DB から生成する。

使い方: python3 scripts/generate_hero_season.py M-7 リザードン charizard [--start 2026/10/07]
出力: src/assets/hero-<slug_base>-<season小文字>.png（例 hero-charizard-m7.png）
"""
import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_hero_images import generate  # noqa: E402
from generate_hero_draft import TYPE_PALETTE, clean_display_name  # noqa: E402

DB = Path(__file__).parent / "pokenavi.db"
SEASON_START = {"M-7": "2026/10/07"}


def latest(cur, season, upto="9999"):
    return cur.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date<=?",
                       (season, upto)).fetchone()[0]


def detail_date(cur, season, name):
    """本文の数値（article_facts.py）と同じ日のデータを使う。使用率は毎日クロールされるので、最新日だと本文の順位と
    食い違う（2026-10-28 ヒスイゾロアーク：本文73位・画像74位）。"""
    return cur.execute("SELECT MAX(crawled_date) FROM pokemon_moves WHERE season=? AND rule='single' AND pokemon=?",
                       (season, name)).fetchone()[0] or "9999"


def rank_of(cur, season, name, upto="9999"):
    d = latest(cur, season, upto)
    r = cur.execute("SELECT rank, pokemon_id FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=? AND pokemon=?",
                    (season, d, name)).fetchone()
    return r


def types_of(cur, name):
    base = re.sub(r"\(.+?\)", "", name).strip()
    for c in (name, base):
        r = cur.execute("SELECT type1, type2 FROM pokemon_base_stats WHERE pokemon_name=? LIMIT 1", (c,)).fetchone()
        if r:
            return [t for t in r if t]
    sys.exit(f"タイプが DB に無い: {name}")


def mega_stone(cur, season, name, upto="9999"):
    r = cur.execute("""SELECT item, usage_rate FROM pokemon_items WHERE season=? AND rule='single' AND pokemon=?
                       AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_items WHERE season=? AND rule='single' AND pokemon=? AND crawled_date<=?)
                       AND item LIKE '%ナイト%' ORDER BY usage_rate DESC LIMIT 1""", (season, name, season, name, upto)).fetchone()
    return (r[0], float(r[1])) if r and r[1] is not None and float(r[1]) >= 20 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season")
    ap.add_argument("pokemon")
    ap.add_argument("slug_base")
    ap.add_argument("--start", default=None)
    a = ap.parse_args()
    cur = sqlite3.connect(DB).cursor()
    # 事実ファイルがあればその detail_date（spec で日付を固定した公開済み記事は最新クロール日と違う）
    fp = Path(__file__).parent.parent / "_local" / "article_facts" / f"{a.slug_base}-analysis-m{a.season.split('-')[1]}.json"
    dd = (json.loads(fp.read_text(encoding="utf-8"))["sources"]["detail_date"] if fp.exists()
          else detail_date(cur, a.season, a.pokemon))
    now = rank_of(cur, a.season, a.pokemon, dd)
    if not now:
        sys.exit(f"{a.season} の使用率に {a.pokemon} が無い")
    rank = now[0]
    n = int(a.season.split("-")[1])
    prev = rank_of(cur, f"M-{n - 1}", a.pokemon)
    types = types_of(cur, a.pokemon)
    cfg = dict(TYPE_PALETTE[types[0]])
    cfg["out"] = f"hero-{a.slug_base}-m{n}.png"
    cfg["badge_label"] = f"シーズン {a.season}"
    cfg["date_range"] = f"{a.start or SEASON_START.get(a.season, '')} 〜"
    stone = mega_stone(cur, a.season, a.pokemon, dd)
    cfg["left_lines"] = [
        f"#{rank}  {clean_display_name(a.pokemon)}",
        f"使用率 {a.season} {rank}位" + (f"（M-{n - 1}:{prev[0]}位）" if prev else ""),
        f"{stone[0]} {stone[1]:.1f}%" if stone else "/".join(types),
    ]
    d = latest(cur, a.season, dd)
    start = max(1, rank - 1)
    rows = cur.execute("""SELECT rank, pokemon, pokemon_id FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=?
                          AND pokemon_id IS NOT NULL AND pokemon_id != '' AND rank BETWEEN ? AND ? ORDER BY rank LIMIT 4""",
                       (a.season, d, start, start + 3)).fetchall()
    cfg["entries"] = [{"rank": r, "id": pid, "name": clean_display_name(p), "hi": r == rank} for r, p, pid in rows]
    generate(cfg)
    print(f"src/assets/{cfg['out']}")


if __name__ == "__main__":
    main()
