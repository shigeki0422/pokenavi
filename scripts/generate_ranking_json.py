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

dates_db = [r[0] for r in conn.execute(
    "SELECT DISTINCT crawled_date FROM pokemon_usage WHERE season=? AND rule='single' ORDER BY crawled_date",
    (SEASON,)
)]
# クロール失敗日も日付軸には含める（データなし＝折れ線は直線で繋がる）
MISSING_DATES = ["2026-06-21", "2026-06-26"]
dates = sorted(set(dates_db) | set(MISSING_DATES))

rows = conn.execute(
    "SELECT pokemon, pokemon_id, crawled_date, rank, usage_rate FROM pokemon_usage WHERE season=? AND rule='single' ORDER BY crawled_date, rank",
    (SEASON,)
).fetchall()

# 全日付に登場したポケモンをユニオンで収集
# (pokemon, date) → {rank, rate}
all_map = {}
for name, pid, date, rank, rate in rows:
    key = (name, date)
    if key not in all_map or rank < all_map[key]["rank"]:
        all_map[key] = {"rank": rank, "rate": rate}

# 全期間に登場したポケモンのユニーク集合
all_pokemon = sorted(set(name for name, date in all_map), key=lambda n: (
    all_map.get((n, dates[-1]), {}).get("rank", 9999),  # 最新日順位優先
    min(all_map[(n, d)]["rank"] for d in dates if (n, d) in all_map)  # 次点: 最小順位
))

poke_list = []
for name in all_pokemon:
    entry = {"name": name, "id": id_map.get(name), "dates": {}}
    for d in dates:
        if (name, d) in all_map:
            entry["dates"][d] = all_map[(name, d)]
    poke_list.append(entry)

OUT_PATH.write_text(json.dumps({"dates": dates, "pokemon": poke_list}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"完了: {len(poke_list)}件, 最新日={dates[-1]}")
