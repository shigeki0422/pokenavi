#!/usr/bin/env python3
"""
M-3使用率ランキングJSON生成
出力: src/data/ranking.json
"""

import sqlite3
import json
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "pokenavi.db"
OUT_PATH = Path(__file__).parent.parent / "src/data/ranking.json"
IMGDIR = Path(__file__).parent.parent / "public/images/pokemon"
SEASON = "M-3"
LIMIT = 200

ALIASES = {
    "フラエッテ(永遠)": "0670-05",
    "アローラキュウコン": "0038-01", "ライチュウ(アローラ)": "0026-01",
    "ガラルヤドキング": "0199-01", "ガラルヤドラン": "0080-02",
    "マッギョ(ガラル)": "0618-01",
    "ヒスイダイケンキ": "0503-01", "ヒスイゾロアーク": "0571-01",
    "ヒスイウインディ": "0059-01", "ヒスイバクフーン": "0157-01",
    "ヒスイクレベース": "0713-01", "ヒスイジュナイパー": "0724-01",
    "ヒスイヌメルゴン": "0706-01",
    "ルガルガン(たそがれ)": "0745-02", "ルガルガン(まよなか)": "0745-01",
    "ウォッシュロトム": "0479-02", "ヒートロトム": "0479-01",
    "カットロトム": "0479-04", "フロストロトム": "0479-03",
    "スピンロトム": "0479-05",
    "イダイトウ(オス)": "0902-00", "イダイトウ(メス)": "0902-01",
    "ニャオニクス(オス)": "0678-00", "ニャオニクス(メス)": "0678-01",
    "ケンタロス:炎": "0128-02", "ケンタロス:水": "0128-03", "ケンタロス:格": "0128-01",
    "ビビヨン": "0666-18",
}

conn = sqlite3.connect(DB_PATH)

# pokemon_name → 画像ID マップ構築
id_map = {}
for name, dex, form in conn.execute("SELECT pokemon_name, dex_number, form_index FROM pokemon_base_stats"):
    iid = f"{dex:04d}-{form:02d}"
    if (IMGDIR / f"pokemon-{iid}.webp").exists():
        id_map.setdefault(name, iid)
for k, v in ALIASES.items():
    if (IMGDIR / f"pokemon-{v}.webp").exists():
        id_map[k] = v

dates = [r[0] for r in conn.execute(
    "SELECT DISTINCT crawled_date FROM pokemon_usage WHERE season=? AND rule='single' ORDER BY crawled_date",
    (SEASON,)
)]

rows = conn.execute(
    "SELECT pokemon, pokemon_id, crawled_date, rank, usage_rate FROM pokemon_usage WHERE season=? AND rule='single' ORDER BY crawled_date, rank",
    (SEASON,)
).fetchall()

# 最新日のrank順エントリをキーにする（同名ポケモンが複数rankに存在する場合も全件表示）
latest = dates[-1]
latest_rows = [(name, pid, rank, rate) for name, pid, date, rank, rate in rows
               if date == latest and rank <= LIMIT]
latest_rows.sort(key=lambda r: r[2])

# 過去日付のデータ: (pokemon, date) → rank。同名が複数ある場合は最小rankを採用
past_map = {}
for name, pid, date, rank, rate in rows:
    if date == latest:
        continue
    key = (name, date)
    if key not in past_map or rank < past_map[key]["rank"]:
        past_map[key] = {"rank": rank, "rate": rate}

poke_list = []
for name, pid, rank, rate in latest_rows:
    entry = {"name": name, "id": id_map.get(name), "dates": {latest: {"rank": rank, "rate": rate}}}
    for d in dates[:-1]:
        if (name, d) in past_map:
            entry["dates"][d] = past_map[(name, d)]
    poke_list.append(entry)

OUT_PATH.write_text(json.dumps({"dates": dates, "pokemon": poke_list}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"完了: {len(poke_list)}件, 最新日={latest}")
