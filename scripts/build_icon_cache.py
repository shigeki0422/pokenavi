"""
過去のクロールデータからicon_cacheを一括構築する
初回1回だけ実行すればよい
"""
import sqlite3, cv2
from pathlib import Path
from insert_ranking_from_icons import (
    DB, SEASON, RULE, ICON_CACHE_DIR,
    extract_main_icon, _save_cache
)

conn = sqlite3.connect(DB)
rows = conn.execute(
    "SELECT crawled_date, rank, pokemon FROM pokemon_usage WHERE season=? AND rule=? ORDER BY crawled_date",
    (SEASON, RULE)
).fetchall()
conn.close()

ICON_CACHE_DIR.mkdir(exist_ok=True)
updated = {}  # pokemon -> 最新日付

for date, rank, pokemon in rows:
    rank_dir = Path(f"/Users/shigeki/work/pokenavi/crawl_data/champ_crawl_{date}/detail/{rank:03d}")
    icon = extract_main_icon(rank_dir)
    if icon is not None:
        updated[pokemon] = (date, icon)

saved = 0
for pokemon, (date, icon) in updated.items():
    _save_cache(pokemon, icon)
    saved += 1

print(f"icon_cache: {saved}件保存 (最新日付のみ)")
