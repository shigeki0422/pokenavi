"""
gamewith.jp/pokemon-champions クローラー
- 使用率ランキング（/555373）
- 各ポケモン詳細（技・持ち物・特性・性格・能力ポイント・同居ポケモン）
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
from db import get_conn

BASE       = "https://gamewith.jp"
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


def fetch(url: str) -> None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        r.encoding = "utf-8"
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return None


def parse_rate(text: str) -> None:
    m = re.search(r"[\d.]+", text or "")
    return float(m.group()) if m else None


def get_season_from_page(soup: BeautifulSoup) -> str:
    """ページ内のシーズン表記を取得（例: シーズンM-2）"""
    text = soup.get_text()
    m = re.search(r"シーズン(M-\d+)", text)
    return m.group(1) if m else "unknown"


def crawl_ranking(rule_str: str = "single") -> tuple[str, list[dict]]:
    """ランキングページからポケモン一覧とURLを取得"""
    url = RANKING_URL if rule_str == "single" else DOUBLE_URL
    soup = fetch(url)
    if not soup:
        return "unknown", []

    season = get_season_from_page(soup)
    pokemons = []
    seen = set()

    for a in soup.select("a[href*='/pokemon-champions/']"):
        href = a.get("href", "")
        # ランキング・記事ページ以外を除外
        if not re.search(r"/pokemon-champions/\d+$", href):
            continue
        article_id = re.search(r"/(\d+)$", href).group(1)
        if article_id in ("555373", "558230", "546413"):  # ランキングページ自身を除外
            continue
        name = a.get_text(strip=True)
        name = re.sub(r"\s+", "", name)
        if not name or name in seen or len(name) > 15:
            continue
        seen.add(name)
        pokemons.append({
            "pokemon": name,
            "url": BASE + href if href.startswith("/") else href
        })

    # 順位を付与
    for i, p in enumerate(pokemons, 1):
        p["rank"] = i

    print(f"  {rule_str} {len(pokemons)}体を取得 (シーズン: {season})")
    return season, pokemons


def crawl_pokemon_detail(season: str, rule_str: str, pokemon: dict, conn: sqlite3.Connection):
    """個別ページから詳細データを取得してDBに保存"""
    name = pokemon["pokemon"]
    url  = pokemon["url"]
    soup = fetch(url)
    at   = now_jst()

    if not soup:
        conn.execute(
            "INSERT INTO crawl_log (crawled_at,source,url,season,rule,pokemon,status,message) VALUES(?,?,?,?,?,?,?,?)",
            (at, "gamewith", url, season, rule_str, name, "error", "fetch failed")
        )
        conn.commit()
        return

    full_text = soup.get_text("\n")
    lines = full_text.split("\n")

    def extract_section(keyword: str) -> list[tuple[int, str, float]]:
        """キーワード以降の行から (rank, label, rate) を抽出"""
        rows, in_section, rank = [], False, 0
        for line in lines:
            line = line.strip()
            if keyword in line and not in_section:
                in_section = True
                continue
            if in_section:
                m = re.search(r"([\d.]+)%", line)
                if m:
                    label = re.sub(r"[\d.]+%", "", line).strip()
                    label = re.sub(r"^\d+\s*位?\s*", "", label).strip()
                    if label and 1 <= len(label) <= 25:
                        rank += 1
                        rows.append((rank, label, float(m.group(1))))
                elif rank >= 3:
                    break
        return rows[:10]

    # シングル / ダブルのセクションを判定して抽出
    section_prefix = "シングル" if rule_str == "single" else "ダブル"

    moves     = extract_section(f"{section_prefix}バトル") or extract_section("わざ")
    items     = extract_section("持ち物")
    abilities = extract_section("特性")
    natures   = extract_section("性格")
    evs       = extract_section("能力ポイント")

    def bulk_insert(table: str, col: str, data: list[tuple]):
        if not data:
            return
        conn.executemany(f"""
            INSERT OR REPLACE INTO {table}
                (season, rule, pokemon, rank, {col}, usage_rate, source, crawled_at)
            VALUES (?,?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r, label, rate, "gamewith", at)
              for r, label, rate in data])

    bulk_insert("pokemon_moves",     "move",      moves)
    bulk_insert("pokemon_items",     "item",      items)
    bulk_insert("pokemon_abilities", "ability",   abilities)
    bulk_insert("pokemon_natures",   "nature",    natures)
    bulk_insert("pokemon_evs",       "ev_spread", evs)

    # 同居ポケモン
    partner_links = soup.select(f"a[href*='/pokemon-champions/']")
    partners, seen = [], {name}
    for a in partner_links:
        pname = a.get_text(strip=True)
        pname = re.sub(r"\s+", "", pname)
        if pname and pname not in seen and len(pname) <= 15:
            seen.add(pname)
            partners.append(pname)
        if len(partners) >= 10:
            break
    if partners:
        conn.executemany("""
            INSERT OR REPLACE INTO pokemon_partners
                (season, rule, pokemon, rank, partner, source, crawled_at)
            VALUES (?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r+1, p, "gamewith", at)
              for r, p in enumerate(partners)])

    conn.execute(
        "INSERT INTO crawl_log (crawled_at,source,url,season,rule,pokemon,status) VALUES(?,?,?,?,?,?,?)",
        (at, "gamewith", url, season, rule_str, name, "success")
    )
    conn.commit()


def crawl_season(rules: list = ["single"], limit=None):
    conn = get_conn()

    for rule_str in rules:
        print(f"\n=== gamewith: {rule_str} ===")
        season, pokemons = crawl_ranking(rule_str)
        if not pokemons:
            continue

        # 使用率ランキングを保存
        at = now_jst()
        conn.executemany("""
            INSERT OR REPLACE INTO pokemon_usage
                (season, rule, rank, pokemon, pokemon_id, usage_rate, source, crawled_at)
            VALUES (?,?,?,?,?,?,?,?)
        """, [(season, rule_str, p["rank"], p["pokemon"], None, None, "gamewith", at)
              for p in pokemons])
        conn.commit()

        targets = pokemons[:limit] if limit else pokemons
        for i, p in enumerate(targets, 1):
            print(f"  [{i:3}/{len(targets)}] {p['pokemon']}", end="\r")
            crawl_pokemon_detail(season, rule_str, p, conn)
            time.sleep(DELAY)

        print(f"\n  完了: {len(targets)}体")

    conn.close()


if __name__ == "__main__":
    crawl_season(rules=["single"], limit=20)
