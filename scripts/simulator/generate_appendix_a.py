#!/usr/bin/env python3
import sqlite3
import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from simulator.damage import (
    _NON_CONTACT_PHYSICAL,
    SOUND_MOVES,
    BALL_BOMB_MOVES,
    PUNCH_MOVES,
    BYPASS_DAMAGE_CALC,
)
from simulator.abilities import SLICING_MOVES

def get_move_flags(move_name):
    flags = []

    if move_name not in _NON_CONTACT_PHYSICAL:
        cursor.execute("SELECT power, category FROM move_master WHERE name_jp = ?", (move_name,))
        row = cursor.fetchone()
        if row and row[1] == "physical":
            flags.append("接")

    if "パンチ" in move_name or move_name in PUNCH_MOVES:
        flags.append("パ")

    if move_name in SOUND_MOVES:
        flags.append("音")

    if move_name in BALL_BOMB_MOVES:
        flags.append("弾")

    if move_name in SLICING_MOVES:
        flags.append("切")

    if move_name in (
        "かみつく","かみくだく","かみなりのキバ","ほのおのキバ","こおりのキバ",
        "どくどくのキバ","サイコファング",
    ):
        flags.append("噛")

    if move_name in ("はどうだん","みずのはどう","あくのはどう","りゅうのはどう","いやしのはどう","だいちのはどう"):
        flags.append("波")

    if move_name in (
        "こごえるかぜ","ぼうふう","ふぶき","ねっぷう","ふきとばし",
        "おいかぜ","すなあらし","はなふぶき","エアカッター",
    ):
        flags.append("風")

    return " ".join(flags) if flags else ""

def get_effect_desc(move_name, cursor):
    cursor.execute("SELECT effect_text FROM move_master WHERE name_jp = ?", (move_name,))
    row = cursor.fetchone()
    return (row[0] or "") if row else ""

def format_table_row(name, type_, power, accuracy, priority, pp, flags, effect):
    power_str = str(power) if power else "可変" if name in BYPASS_DAMAGE_CALC else "—"
    accuracy_str = str(accuracy) if accuracy else "—"
    priority_str = str(priority) if priority and priority != 0 else ""

    return (
        f"| {name} | {type_} | {power_str} | {accuracy_str} | {pp} | "
        f"{priority_str} | {flags} | {effect} |"
    )

conn = sqlite3.connect("scripts/pokenavi.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name_jp, type, category, power, accuracy, priority, pp FROM move_master ORDER BY id"
)

physical_moves = []
special_moves = []
status_moves = []

for name_jp, type_, category, power, accuracy, priority, pp in cursor.fetchall():
    flags = get_move_flags(name_jp)
    effect = get_effect_desc(name_jp, cursor)

    row = format_table_row(name_jp, type_, power, accuracy, priority, pp, flags, effect)

    if category == "physical":
        physical_moves.append(row)
    elif category == "special":
        special_moves.append(row)
    elif category == "status":
        status_moves.append(row)

conn.close()

header = "| 技名 | タイプ | 威力 | 命中 | PP | 優先 | フラグ | 主要効果・備考 |"
sep    = "|------|--------|------|------|----|----|--------|------|"

output = f"""### 物理技

{header}
{sep}
{chr(10).join(physical_moves)}

### 特殊技

{header}
{sep}
{chr(10).join(special_moves)}

### 変化技

{header}
{sep}
{chr(10).join(status_moves)}
"""

print(output)

with open("scripts/simulator/appendix_a.md", "w", encoding="utf-8") as f:
    f.write(output)

print(f"\n✅ Generated appendix_a.md", file=sys.stderr)
