#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PokeAPIから各ポケモンの重さ(kg)を取得してpokemon_base_statsに保存する
"""
import sqlite3
import urllib.request
import json
import time

DB = "scripts/pokenavi.db"
POKEAPI = "https://pokeapi.co/api/v2/pokemon/"

conn = sqlite3.connect(DB)
cursor = conn.cursor()

# weight_kg カラムを追加（既存なら無視）
try:
    cursor.execute("ALTER TABLE pokemon_base_stats ADD COLUMN weight_kg REAL")
    conn.commit()
    print("weight_kgカラムを追加")
except Exception:
    print("weight_kgカラムは既存")

cursor.execute("""
    SELECT pokemon_name, pokeapi_name, dex_number, form_index
    FROM pokemon_base_stats
    WHERE weight_kg IS NULL
    ORDER BY dex_number
""")
rows = cursor.fetchall()
print(f"取得対象: {len(rows)}件")

updated = 0
failed = []

for name_jp, pokeapi_name, dex, form_idx in rows:
    # pokeapi_nameは図鑑番号またはslugnameのどちらか
    if pokeapi_name:
        url = POKEAPI + str(pokeapi_name).lower().strip()
    else:
        url = POKEAPI + str(dex)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "pokenavi/1.0"})
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        weight_hecto = data.get("weight", 500)  # hectograms
        weight_kg = weight_hecto / 10.0

        cursor.execute(
            "UPDATE pokemon_base_stats SET weight_kg=? WHERE pokemon_name=? AND dex_number=? AND form_index=?",
            (weight_kg, name_jp, dex, form_idx)
        )
        updated += 1
        print(f"  ✓ {name_jp}: {weight_kg}kg (api={pokeapi_name or dex})")
    except Exception as e:
        failed.append((name_jp, str(e)))
        print(f"  ✗ {name_jp}: {e}")

    time.sleep(0.1)

conn.commit()
conn.close()

print(f"\n完了: {updated}件更新 / {len(failed)}件失敗")
if failed:
    print("失敗リスト:")
    for n, e in failed:
        print(f"  {n}: {e}")
