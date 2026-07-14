#!/usr/bin/env python3
"""
パートナー（同じチームのポケモン）をアイコンマッチングで取得してDBに投入する。
OCRの誤読・リージョンフォーム誤認を防ぐため、insert_ranking_from_icons.pyと同じ
テンプレートマッチングロジックを使う。

使い方:
  python insert_partners_from_icons.py 2026-07-13

実行すると指定日のOCRパートナーデータを削除してアイコンマッチング結果で上書きする。
"""

import sys
import sqlite3
import cv2
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).parent / "pokenavi.db"
CRAWL_BASE = Path(__file__).parent.parent / "crawl_data"
REF_DIR = Path(__file__).parent / "icon_refs"

SEASON = "M-4"
RULE = "single"
SOURCE = "champions_adb"

ICON_SIZE = (80, 80)

# _c_partner_*.png (960x965) 各行アイコンのtop-y（page=0実測値）
# page=0とpage=1で最大+15pxのずれがある
# → 各行を [top_y-10, top_y+100] (110px) で切り出せばpage=1のずれも吸収できる
# x範囲: page=0実測266、±10pxで 256〜366
ROW_TOP_Y = [331, 456, 583, 708, 834]  # page=0での各行アイコンtop-y
ROW_Y_SLACK = 10   # top_y上方向の余裕px（window = top_y-SLACK 〜 top_y+80+SLACK+15）
ROW_X1, ROW_X2 = 256, 366  # アイコンx範囲（80px + 余裕）


def build_templates():
    """icon_refs/ からテンプレート辞書を構築（insert_ranking_from_icons.pyと同じ）"""
    templates = {}
    for p in sorted(REF_DIR.glob("*.png")):
        img = cv2.imread(str(p))
        if img is not None:
            templates[p.stem] = cv2.resize(img, ICON_SIZE)
    print(f"テンプレート: {len(templates)}件")
    return templates


def identify_partners_from_image(img_path: Path, templates: dict) -> list:
    """行ごとの局所ROIでパートナーを識別する（最大5件、順位=行番号）

    Returns: [(name, score), ...]  行順（1位〜5位）
    """
    img = cv2.imread(str(img_path))
    if img is None:
        return []
    h, w = img.shape[:2]
    if (w, h) != (960, 965):
        print(f"  警告: 想定外サイズ {w}x{h} ({img_path.name})")
        return []

    results = []
    for top_y in ROW_TOP_Y:
        y1 = max(0, top_y - ROW_Y_SLACK)
        y2 = min(h, top_y + ICON_SIZE[1] + ROW_Y_SLACK + 15)  # +15でpage=1のずれを吸収
        roi = img[y1:y2, ROW_X1:ROW_X2]

        best_name, best_score = None, -1.0
        for name, tmpl in templates.items():
            res = cv2.matchTemplate(roi, tmpl, cv2.TM_CCOEFF_NORMED)
            score = float(res.max())
            if score > best_score:
                best_score = score
                best_name = name
        results.append((best_name, best_score))

    return results


def process_day(crawled_date: str, templates: dict, conn: sqlite3.Connection):
    crawl_dir = CRAWL_BASE / f"champ_crawl_{crawled_date}"
    detail_dir = crawl_dir / "detail"
    if not detail_dir.exists():
        print(f"ERROR: {detail_dir} が存在しない")
        return

    # 当日のpokemon_usageから順位→ポケモン名マップ
    rank_map = {r[0]: r[1] for r in conn.execute(
        "SELECT rank, pokemon FROM pokemon_usage WHERE season=? AND rule=? AND crawled_date=?",
        (SEASON, RULE, crawled_date)
    )}
    if not rank_map:
        print(f"ERROR: pokemon_usage に {crawled_date} のデータがない")
        return

    now = datetime.now(timezone.utc).isoformat()

    # 既存のOCRパートナーデータを削除
    deleted = conn.execute(
        "DELETE FROM pokemon_partners WHERE season=? AND rule=? AND crawled_date=? AND source=?",
        (SEASON, RULE, crawled_date, SOURCE)
    ).rowcount
    print(f"既存削除: {deleted}件")

    low_score = []
    inserted = 0

    for rank_str in sorted(detail_dir.iterdir(), key=lambda p: p.name):
        if not rank_str.is_dir():
            continue
        try:
            rank = int(rank_str.name)
        except ValueError:
            continue
        pokemon = rank_map.get(rank)
        if not pokemon:
            continue

        partners = []
        for page in range(2):  # partner_00, partner_01
            img_path = rank_str / f"_c_partner_{page:02d}.png"
            if not img_path.exists():
                break
            results = identify_partners_from_image(img_path, templates)
            if len(results) < 5:
                low_score.append((rank, pokemon, page, len(results)))
            partners.extend(results)

        for pos, (name, score) in enumerate(partners, 1):
            if name is None:
                continue
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_partners"
                "(season,rule,pokemon,rank,partner,source,crawled_date,crawled_at)"
                " VALUES(?,?,?,?,?,?,?,?)",
                (SEASON, RULE, pokemon, pos, name, SOURCE, crawled_date, now)
            )
            inserted += conn.execute("SELECT changes()").fetchone()[0]

    conn.commit()
    print(f"投入: {inserted}件")

    if low_score:
        print(f"\n識別数不足 ({len(low_score)}件):")
        for rank, pokemon, page, cnt in low_score[:20]:
            print(f"  rank={rank} ({pokemon}) page={page}: {cnt}件のみ識別")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python insert_partners_from_icons.py YYYY-MM-DD")
        sys.exit(1)

    crawled_date = sys.argv[1]
    conn = sqlite3.connect(DB_PATH)
    templates = build_templates()

    print(f"\n=== {crawled_date} パートナーアイコンマッチング ===")
    process_day(crawled_date, templates, conn)
    conn.close()
