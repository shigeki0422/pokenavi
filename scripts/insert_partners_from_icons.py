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

# _c_partner_*.png (960x965) での各行アイコンBOX (x1, y1, x2, y2)
# 実測値：各行中心x≈306、y間隔≈125px
# 5行 × 2ページ = 最大10パートナー
PARTNER_ROWS = [
    (266, 331, 346, 411),   # 1位
    (265, 456, 345, 536),   # 2位
    (266, 581, 346, 661),   # 3位
    (266, 706, 346, 786),   # 4位
    (266, 831, 346, 911),   # 5位
]


def build_templates():
    """icon_refs/ からテンプレート辞書を構築（insert_ranking_from_icons.pyと同じ）"""
    templates = {}
    for p in sorted(REF_DIR.glob("*.png")):
        img = cv2.imread(str(p))
        if img is not None:
            templates[p.stem] = cv2.resize(img, ICON_SIZE)
    print(f"テンプレート: {len(templates)}件")
    return templates


def match_icon(icon, templates):
    """最もスコアが高いポケモン名とスコアを返す"""
    best_name, best_score = None, -1.0
    icon_r = cv2.resize(icon, ICON_SIZE)
    for name, tmpl in templates.items():
        res = cv2.matchTemplate(icon_r, tmpl, cv2.TM_CCOEFF_NORMED)
        score = float(res.max())
        if score > best_score:
            best_score = score
            best_name = name
    return best_name, best_score


def extract_partner_icons(img_path: Path) -> list:
    """_c_partner_*.png から各行のアイコンを切り出して返す（最大5件）"""
    img = cv2.imread(str(img_path))
    if img is None:
        return []
    h, w = img.shape[:2]
    if (w, h) != (960, 965):
        print(f"  警告: 想定外サイズ {w}x{h} ({img_path.name})")
        return []
    return [img[y1:y2, x1:x2] for x1, y1, x2, y2 in PARTNER_ROWS]


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
            icons = extract_partner_icons(img_path)
            for icon in icons:
                name, score = match_icon(icon, templates)
                if score < 0.4:
                    low_score.append((rank, pokemon, page, score, name))
                partners.append((name, score))

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
        print(f"\n低スコア要確認 ({len(low_score)}件):")
        for rank, pokemon, page, score, name in low_score[:20]:
            print(f"  rank={rank} ({pokemon}) page={page}: score={score:.3f} → {name}")


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
