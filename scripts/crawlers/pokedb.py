"""
champs.pokedb.tokyo クローラー
- ポケモン使用率ランキング（全213体）
- 各ポケモンの技・持ち物・特性・性格・努力値・同居ポケモン採用率
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

BASE = "https://champs.pokedb.tokyo"
JST = timezone(timedelta(hours=9))
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; pokenavi-bot/1.0)"}
DELAY = 1.5  # サーバー負荷軽減


def now_jst():
    return datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")


def fetch(url: str) -> None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        r.encoding = "utf-8"
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return None


def parse_rate(text: str) -> None:
    """'52.4%' → 52.4"""
    m = re.search(r"[\d.]+", text or "")
    return float(m.group()) if m else None


def crawl_pokemon_list(season: str, rule: int) -> list[dict]:
    """ランキング一覧から全ポケモンとIDを取得"""
    rule_str = "single" if rule == 0 else "double"
    url = f"{BASE}/pokemon/list?rule={rule}&season={season.replace('M-', '')}"
    soup = fetch(url)
    if not soup:
        return []

    pokemons = []
    # 各ポケモンへのリンク: /pokemon/show/XXXX-XX
    for rank, a in enumerate(soup.select("a[href*='/pokemon/show/']"), 1):
        href = a["href"]
        m = re.search(r"/pokemon/show/(\d{4}-\d{2})", href)
        if not m:
            continue
        pokemon_id = m.group(1)
        name = a.get_text(strip=True)
        # 数字・矢印などを除去
        name = re.sub(r"^\d+", "", name).strip()
        if name:
            pokemons.append({
                "rank": rank,
                "pokemon": name,
                "pokemon_id": pokemon_id,
                "url": f"{BASE}/pokemon/show/{pokemon_id}?season={season.replace('M-', '')}&rule={rule}"
            })
    print(f"  {rule_str} {len(pokemons)}体を取得")
    return pokemons


def save_usage_ranking(season: str, rule_str: str, pokemons: list[dict], conn: sqlite3.Connection):
    at = now_jst()
    rows = [(season, rule_str, p["rank"], p["pokemon"], p["pokemon_id"],
             None, "pokedb", at) for p in pokemons]
    conn.executemany("""
        INSERT OR REPLACE INTO pokemon_usage
            (season, rule, rank, pokemon, pokemon_id, usage_rate, source, crawled_at)
        VALUES (?,?,?,?,?,?,?,?)
    """, rows)
    conn.commit()


def parse_pokedb_page(lines: list, section_header: str, pattern: str) -> list:
    """
    pattern='move'  : header → (name, number, '%') × N
    pattern='table' : header → (rank, name, 'XX.X%', 'XX.X%') × N
    pattern='nature': header → (rank, name, '(', ..., ')', 'XX.X%', 'XX.X%') × N
    pattern='ev'    : header → '合算'/'個別', (rank, label, 'XX.X%', ...) × N
    """
    results = []
    start = None
    for i, line in enumerate(lines):
        if line == section_header:
            start = i + 1
            break
    if start is None:
        return results

    rank = 0
    i = start
    while i < len(lines) and len(results) < 10:
        line = lines[i]

        if pattern == "move":
            # name / number / '%' の3行セット
            if i + 2 < len(lines) and lines[i+2] == "%" and re.fullmatch(r"[\d.]+", lines[i+1]):
                rank += 1
                results.append((rank, line, float(lines[i+1])))
                i += 3
                continue
            # 別セクション開始を検知
            if line in ("特性", "持ち物", "能力補正", "能力ポイント", "一緒に使用"):
                break

        elif pattern == "table":
            # rank(数字) / name / 'XX%' / 'XX%' の4行セット
            if re.fullmatch(r"\d+", line) and i + 2 < len(lines):
                candidate_name = lines[i+1]
                candidate_rate = lines[i+2]
                m = re.fullmatch(r"([\d.]+)%", candidate_rate)
                if m and candidate_name and not re.fullmatch(r"[\d.]+", candidate_name):
                    rank += 1
                    results.append((rank, candidate_name, float(m.group(1))))
                    i += 4  # 重複行もスキップ
                    continue
            if line in ("技", "能力補正", "能力ポイント", "一緒に使用") and rank > 0:
                break

        elif pattern == "nature":
            # rank / name / '(' / ... / ')' / 'XX%' / 'XX%'
            if re.fullmatch(r"\d+", line) and i + 1 < len(lines):
                nature_name = lines[i+1]
                # ')' の後の XX% を探す
                j = i + 2
                while j < len(lines) and lines[j] != ")":
                    j += 1
                j += 1  # ')' の次
                if j < len(lines):
                    m = re.fullmatch(r"([\d.]+)%", lines[j])
                    if m:
                        rank += 1
                        results.append((rank, nature_name, float(m.group(1))))
                        i = j + 2
                        continue
            if line in ("持ち物", "能力ポイント", "一緒に使用") and rank > 0:
                break

        elif pattern == "ev":
            # '合算'/'個別' をスキップ → rank / label / 'XX%' の3行
            if line in ("合算", "個別"):
                i += 1
                continue
            if re.fullmatch(r"\d+", line) and i + 2 < len(lines):
                label = lines[i+1]
                rate_line = lines[i+2]
                m = re.fullmatch(r"([\d.]+)%", rate_line)
                if m and label:
                    rank += 1
                    results.append((rank, label, float(m.group(1))))
                    i += 3
                    continue
            if line == "一緒に使用" and rank > 0:
                break

        i += 1

    return results


def crawl_pokemon_detail(season: str, rule: int, pokemon: dict, conn: sqlite3.Connection):
    """個別ページから技・持ち物・特性・性格・努力値・同居ポケモンを取得"""
    rule_str = "single" if rule == 0 else "double"
    url = pokemon["url"]
    name = pokemon["pokemon"]
    soup = fetch(url)
    at = now_jst()

    if not soup:
        conn.execute(
            "INSERT INTO crawl_log (crawled_at,source,url,season,rule,pokemon,status,message) VALUES(?,?,?,?,?,?,?,?)",
            (at, "pokedb", url, season, rule_str, name, "error", "fetch failed")
        )
        conn.commit()
        return

    lines = [l.strip() for l in soup.get_text("\n").split("\n") if l.strip()]

    moves     = parse_pokedb_page(lines, "技",      "move")
    abilities = parse_pokedb_page(lines, "特性",    "table")
    natures   = parse_pokedb_page(lines, "能力補正", "nature")
    items     = parse_pokedb_page(lines, "持ち物",  "table")
    evs       = parse_pokedb_page(lines, "能力ポイント", "ev")

    def bulk_insert(table: str, col: str, data: list):
        if not data:
            return
        conn.executemany(f"""
            INSERT OR REPLACE INTO {table}
                (season, rule, pokemon, rank, {col}, usage_rate, source, crawled_at)
            VALUES (?,?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r, label, rate, "pokedb", at)
              for r, label, rate in data])

    bulk_insert("pokemon_moves",     "move",      moves)
    bulk_insert("pokemon_items",     "item",      items)
    bulk_insert("pokemon_abilities", "ability",   abilities)
    bulk_insert("pokemon_natures",   "nature",    natures)
    bulk_insert("pokemon_evs",       "ev_spread", evs)

    # 同居ポケモン（ランキング一覧リンクを除いた個別ページへのリンク）
    partners, seen = [], {name}
    for a in soup.select("a[href*='/pokemon/show/']"):
        partner = re.sub(r"^\d+", "", a.get_text(strip=True)).strip()
        if partner and partner not in seen and len(partner) <= 15:
            seen.add(partner)
            partners.append(partner)
        if len(partners) >= 10:
            break
    if partners:
        conn.executemany("""
            INSERT OR REPLACE INTO pokemon_partners
                (season, rule, pokemon, rank, partner, source, crawled_at)
            VALUES (?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r+1, p, "pokedb", at)
              for r, p in enumerate(partners)])

    conn.execute(
        "INSERT INTO crawl_log (crawled_at,source,url,season,rule,pokemon,status) VALUES(?,?,?,?,?,?,?)",
        (at, "pokedb", url, season, rule_str, name, "success")
    )
    conn.commit()


def crawl_season(season: str = "M-2", rules: list = [0, 1], limit=None):
    """シーズン全体をクロール"""
    conn = get_conn()

    for rule in rules:
        rule_str = "single" if rule == 0 else "double"
        print(f"\n=== pokedb: {season} {rule_str} ===")

        pokemons = crawl_pokemon_list(season, rule)
        if not pokemons:
            continue

        save_usage_ranking(season, rule_str, pokemons, conn)

        targets = pokemons[:limit] if limit else pokemons
        for i, p in enumerate(targets, 1):
            print(f"  [{i:3}/{len(targets)}] {p['pokemon']}", end="\r")
            crawl_pokemon_detail(season, rule, p, conn)
            time.sleep(DELAY)

        print(f"\n  完了: {len(targets)}体")

    conn.close()


if __name__ == "__main__":
    crawl_season(season="M-2", rules=[0], limit=30)
