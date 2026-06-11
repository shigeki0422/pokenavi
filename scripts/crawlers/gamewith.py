"""
gamewith.jp/pokemon-champions クローラー
- 使用率ランキング（div._pkm span._name から全213体取得）
- 個別ページはJavaScriptレンダリングが必要なためスキップ
  → 技/持ち物/特性/性格/努力値は pokedb.py で取得
"""
import re
import time
import sqlite3
from datetime import datetime, timezone, timedelta

import requests
from bs4 import BeautifulSoup

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from db import get_conn, today

BASE        = "https://gamewith.jp"
RANKING_URL = f"{BASE}/pokemon-champions/555373"
DOUBLE_URL  = f"{BASE}/pokemon-champions/558230"
JST = timezone(timedelta(hours=9))
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0 Safari/537.36"
}
DELAY = 2.0


def now_jst():
    return datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")


def fetch(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        r.encoding = "utf-8"
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return None


def get_season_from_page(soup: BeautifulSoup) -> str:
    text = soup.get_text()
    m = re.search(r"シーズン(M-\d+)", text)
    return m.group(1) if m else "unknown"


def get_data_date_from_page(soup: BeautifulSoup) -> str:
    """「集計日：M/D(曜)」から YYYY-MM-DD を返す。見つからなければ今日の日付"""
    text = soup.get_text()
    m = re.search(r"集計日[：:]\s*(\d{1,2})/(\d{1,2})", text)
    if m:
        month, day = int(m.group(1)), int(m.group(2))
        year = datetime.now(JST).year
        # 月が未来になる場合は前年とみなす（年をまたぐケース対応）
        if month > datetime.now(JST).month:
            year -= 1
        return f"{year:04d}-{month:02d}-{day:02d}"
    return today()


def crawl_ranking(rule_str: str = "single") -> tuple:
    """ランキングページから全ポケモンの順位・名前・図鑑番号を取得"""
    url = RANKING_URL if rule_str == "single" else DOUBLE_URL
    soup = fetch(url)
    if not soup:
        return "unknown", []

    season = get_season_from_page(soup)
    data_date = get_data_date_from_page(soup)
    pokemons = []

    for div in soup.select("div._pkm"):
        rank = div.get("data-rank")
        if not rank:
            continue
        name_el = div.select_one("span._name")
        if not name_el:
            continue
        name = name_el.get_text(strip=True)
        if not name:
            continue

        # 図鑑番号を画像URLから抽出（例: gacha/445.png → 445）
        img = div.select_one("img[data-original]")
        dex_no = None
        if img:
            m = re.search(r"/gacha/(\d+)\.png", img.get("data-original", ""))
            if m:
                dex_no = m.group(1)

        pokemons.append({
            "rank": int(rank),
            "pokemon": name,
            "pokemon_id": dex_no,  # 図鑑番号をIDとして保存
        })

    pokemons.sort(key=lambda p: p["rank"])
    print(f"  {rule_str} {len(pokemons)}体を取得 (シーズン: {season}, 集計日: {data_date})")
    return season, data_date, pokemons


def crawl_season(rules: list = ["single"], limit=None):
    conn = get_conn()
    crawled_date = today()

    for rule_str in rules:
        print(f"\n=== gamewith: {rule_str} ===")
        season, data_date, pokemons = crawl_ranking(rule_str)
        if not pokemons:
            continue

        targets = pokemons[:limit] if limit else pokemons

        at = now_jst()
        conn.executemany("""
            INSERT OR REPLACE INTO pokemon_usage
                (season, rule, rank, pokemon, pokemon_id, usage_rate, source, crawled_date, crawled_at)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, [(season, rule_str, p["rank"], p["pokemon"], p["pokemon_id"],
               None, "gamewith", data_date, at)
              for p in targets])
        conn.commit()

        print(f"  完了: {len(targets)}体")
        print(f"  ※ 個別ページ（技/持ち物等）はJSレンダリング必須のためスキップ → pokedb で補完")

    conn.close()


if __name__ == "__main__":
    crawl_season(rules=["single"])
