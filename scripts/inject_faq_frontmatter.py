#!/usr/bin/env python3
"""
pokemon/*.md のフロントマターに faq セクションを追加/更新する。
M-3データ優先、なければM-2にフォールバック。
updatedDate も同時に今日の日付で更新する。
"""
import sqlite3
import re
from datetime import date
from pathlib import Path

DB = Path(__file__).parent / "pokenavi.db"
CONTENT_DIR = Path(__file__).parent.parent / "src/content/pokemon"

conn = sqlite3.connect(DB)

DATE_M3 = conn.execute("SELECT MAX(crawled_date) FROM pokemon_moves WHERE season='M-3' AND rule='single'").fetchone()[0]
DATE_M2 = conn.execute("SELECT MAX(crawled_date) FROM pokemon_moves WHERE season='M-2' AND rule='single'").fetchone()[0]


def fetch_usage(table, col, pokemon, season, date, limit=4):
    return conn.execute(
        f"SELECT {col}, usage_rate FROM {table} WHERE season=? AND rule='single' AND pokemon=? AND crawled_date=? ORDER BY usage_rate DESC LIMIT ?",
        (season, pokemon, date, limit)
    ).fetchall()


def get_faq_data(pokemon_name):
    for season, date in [("M-3", DATE_M3), ("M-2", DATE_M2)]:
        moves = fetch_usage("pokemon_moves", "move", pokemon_name, season, date, 4)
        if not moves:
            continue
        items = fetch_usage("pokemon_items", "item", pokemon_name, season, date, 3)
        abil  = fetch_usage("pokemon_abilities", "ability", pokemon_name, season, date, 1)
        nats  = fetch_usage("pokemon_natures", "nature", pokemon_name, season, date, 2)
        if not items or not abil or not nats:
            continue
        return {
            "season": season,
            "moves": moves,
            "items": items,
            "ability": abil[0],
            "natures": nats,
        }
    return None


def fmt_pct(v):
    return round(float(v), 1)


def build_faq_yaml(data):
    season = data["season"]
    moves  = data["moves"]
    items  = data["items"]
    ability, abil_pct = data["ability"]
    nats = data["natures"]

    move_names = [m[0] for m in moves]
    move_pcts  = [fmt_pct(m[1]) for m in moves]
    item_names = [it[0] for it in items]
    item_pcts  = [fmt_pct(it[1]) for it in items]

    lines = [
        "faq:",
        f"  season: '{season}'",
        f"  topMoves: {move_names}",
        f"  topMovePct: {move_pcts}",
        f"  topItems: {item_names}",
        f"  topItemPct: {item_pcts}",
        f"  topAbility: '{ability}'",
        f"  topAbilityPct: {fmt_pct(abil_pct)}",
        f"  topNature: '{nats[0][0]}'",
        f"  topNaturePct: {fmt_pct(nats[0][1])}",
    ]
    if len(nats) >= 2:
        lines.append(f"  topNature2: '{nats[1][0]}'")
        lines.append(f"  topNaturePct2: {fmt_pct(nats[1][1])}")
    return "\n".join(lines)


FAQ_RE = re.compile(r"\nfaq:\n(?:  [^\n]*\n)*", re.MULTILINE)
UPDATED_DATE_RE = re.compile(r"^updatedDate:.*$", re.MULTILINE)
TODAY = date.today().isoformat()

updated = skipped = no_data = 0

for md_path in sorted(CONTENT_DIR.glob("*.md")):
    text = md_path.read_text(encoding="utf-8")

    m = re.search(r"^pokemonName:\s*'([^']+)'", text, re.MULTILINE)
    if not m:
        skipped += 1
        continue
    pokemon_name = m.group(1)

    data = get_faq_data(pokemon_name)
    if not data:
        no_data += 1
        continue

    faq_yaml = build_faq_yaml(data)

    # faq ブロックを置換、なければ closing --- の直前に挿入
    if FAQ_RE.search(text):
        new_text = FAQ_RE.sub("\n" + faq_yaml + "\n", text)
    else:
        new_text = text.replace("\n---\n", f"\n{faq_yaml}\n---\n", 1)

    # updatedDate を今日の日付で更新/追加
    if UPDATED_DATE_RE.search(new_text):
        new_text = UPDATED_DATE_RE.sub(f"updatedDate: '{TODAY}'", new_text)
    else:
        new_text = new_text.replace("\npubDate:", f"\nupdatedDate: '{TODAY}'\npubDate:", 1)

    if new_text != text:
        md_path.write_text(new_text, encoding="utf-8")
        updated += 1

conn.close()
print(f"updated={updated}  skipped={skipped}  no_data={no_data}")
