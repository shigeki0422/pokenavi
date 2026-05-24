"""
champs.pokedb.tokyo クローラー
- ポケモン使用率ランキング（全213体）
- 各ポケモンの技・持ち物・特性・性格・努力値・同居ポケモン採用率
"""
import re
import time
import json
import sqlite3
from datetime import datetime, timezone, timedelta

import requests
from bs4 import BeautifulSoup

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from db import get_conn, today

BASE = "https://champs.pokedb.tokyo"
JST = timezone(timedelta(hours=9))
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; pokenavi-bot/1.0)"}
DELAY = 1.5


def now_jst():
    return datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")


def fetch(url: str):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        r.encoding = "utf-8"
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return None


def parse_rate(text: str):
    m = re.search(r"[\d.]+", text or "")
    return float(m.group()) if m else None


def get_data_date_from_list_page(season: str, rule: int) -> str:
    """リストページの「更新日 YYYY/M/D HH:MM」から YYYY-MM-DD を返す"""
    url = f"{BASE}/pokemon/list?rule={rule}&season={season.replace('M-', '')}"
    soup = fetch(url)
    if not soup:
        return today()
    text = soup.get_text("\n")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for i, line in enumerate(lines):
        if line == "更新日" and i + 1 < len(lines):
            m = re.match(r"(\d{4})/(\d{1,2})/(\d{1,2})", lines[i + 1])
            if m:
                return f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return today()


def crawl_pokemon_list(season: str, rule: int) -> list:
    """ランキング一覧から全ポケモンとIDを取得"""
    rule_str = "single" if rule == 0 else "double"
    url = f"{BASE}/pokemon/list?rule={rule}&season={season.replace('M-', '')}"
    soup = fetch(url)
    if not soup:
        return []

    pokemons = []
    for rank, a in enumerate(soup.select("a[href*='/pokemon/show/']"), 1):
        href = a["href"]
        m = re.search(r"/pokemon/show/(\d{4}-\d{2})", href)
        if not m:
            continue
        pokemon_id = m.group(1)
        name = a.get_text(strip=True)
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


def save_usage_ranking(season: str, rule_str: str, pokemons: list,
                       conn: sqlite3.Connection, crawled_date: str):
    at = now_jst()
    rows = [(season, rule_str, p["rank"], p["pokemon"], p["pokemon_id"],
             None, "pokedb", crawled_date, at) for p in pokemons]
    conn.executemany("""
        INSERT OR REPLACE INTO pokemon_usage
            (season, rule, rank, pokemon, pokemon_id, usage_rate, source, crawled_date, crawled_at)
        VALUES (?,?,?,?,?,?,?,?,?)
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
            if i + 2 < len(lines) and lines[i+2] == "%" and re.fullmatch(r"[\d.]+", lines[i+1]):
                rank += 1
                results.append((rank, line, float(lines[i+1])))
                i += 3
                continue
            if line in ("特性", "持ち物", "能力補正", "能力ポイント", "一緒に使用"):
                break

        elif pattern == "table":
            if re.fullmatch(r"\d+", line) and i + 2 < len(lines):
                candidate_name = lines[i+1]
                candidate_rate = lines[i+2]
                m = re.fullmatch(r"([\d.]+)%", candidate_rate)
                if m and candidate_name and not re.fullmatch(r"[\d.]+", candidate_name):
                    rank += 1
                    results.append((rank, candidate_name, float(m.group(1))))
                    i += 4
                    continue
            if line in ("技", "能力補正", "能力ポイント", "一緒に使用") and rank > 0:
                break

        elif pattern == "nature":
            if re.fullmatch(r"\d+", line) and i + 1 < len(lines):
                nature_name = lines[i+1]
                j = i + 2
                while j < len(lines) and lines[j] != ")":
                    j += 1
                j += 1
                if j < len(lines):
                    m = re.fullmatch(r"([\d.]+)%", lines[j])
                    if m:
                        rank += 1
                        results.append((rank, nature_name, float(m.group(1))))
                        i = j + 2
                        continue
            if line in ("持ち物", "能力ポイント", "一緒に使用") and rank > 0:
                break

        i += 1

    return results


def parse_ev_section(lines: list, start_idx: int) -> list:
    """
    能力ポイントセクションから個別EV振り行を解析。
    合算サマリー行（後に '+', '余り' が続く）は除外し、
    個別行のみ (rank, label, rate, {H,A,B,C,D,S}) で返す。
    """
    STAT_LETTERS = {"H", "A", "B", "C", "D", "S"}
    results = []
    i = start_idx

    while i < len(lines):
        line = lines[i]

        if line == "一緒に使用":
            break
        if re.fullmatch(r"\d+", line) or line in ("合算", "個別", "+", "余り"):
            i += 1
            continue
        if "件を合算" in line or "残りを表示" in line:
            i += 1
            continue

        if i + 1 >= len(lines):
            break
        rate_m = re.fullmatch(r"([\d.]+)%", lines[i + 1])
        if not rate_m:
            i += 1
            continue

        label = line
        rate = float(rate_m.group(1))
        stats = {"H": 0, "A": 0, "B": 0, "C": 0, "D": 0, "S": 0}

        j = i + 2
        while j + 1 < len(lines):
            if lines[j] in STAT_LETTERS and re.fullmatch(r"\d+", lines[j + 1]):
                stats[lines[j]] = int(lines[j + 1])
                j += 2
            else:
                break

        # 合算サマリー行は '+', '余り' が続く → スキップ
        if j < len(lines) and lines[j] == "+":
            i = j
            continue

        results.append((len(results) + 1, label, rate, stats))
        if len(results) >= 16:
            break
        i = j

    return results


def _save_item_trends(season: str, rule_str: str, name: str,
                      soup, conn: sqlite3.Connection, at: str):
    """pokemonShowTrend から持ち物の日別使用率をバックフィル"""
    trend_el = soup.select_one("section[x-data*='pokemonShowTrend']")
    if not trend_el:
        return
    m = re.search(r"pokemonShowTrend\((\{.*\})\)\s*$",
                  trend_el.get("x-data", ""), re.DOTALL)
    if not m:
        return
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError:
        return

    items_trend = data.get("items", {})      # {item_key: [{date, rate}, ...]}
    item_details = data.get("itemDetails", {})  # {item_key: {name, ...}}

    if not items_trend:
        return

    # 日付ごとに rate でソートしてランクを付ける
    # まず全日付を収集
    all_dates = set()
    for series in items_trend.values():
        for entry in series:
            all_dates.add(entry["date"])

    rows = []
    for date in sorted(all_dates):
        # この日の各アイテムの rate を収集
        day_items = []
        for item_key, series in items_trend.items():
            rate = next((e["rate"] for e in series if e["date"] == date), None)
            if rate is None:
                continue
            item_name = item_details.get(item_key, {}).get("name") if item_details else None
            if not item_name:
                continue
            day_items.append((rate, item_name))

        # rate 降順でランク付け
        day_items.sort(key=lambda x: x[0], reverse=True)
        for rank, (rate, item_name) in enumerate(day_items, 1):
            rows.append((season, rule_str, name, rank, item_name, rate,
                         "pokedb", date, at))

    if rows:
        conn.executemany("""
            INSERT OR IGNORE INTO pokemon_items
                (season, rule, pokemon, rank, item, usage_rate, source, crawled_date, crawled_at)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, rows)


def crawl_pokemon_detail(season: str, rule: int, pokemon: dict,
                         conn: sqlite3.Connection, crawled_date: str):
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

    moves     = parse_pokedb_page(lines, "技",       "move")
    abilities = parse_pokedb_page(lines, "特性",     "table")
    natures   = parse_pokedb_page(lines, "能力補正", "nature")
    items     = parse_pokedb_page(lines, "持ち物",   "table")

    ev_start = None
    for idx, l in enumerate(lines):
        if l == "能力ポイント":
            ev_start = idx + 1
            break
    evs = parse_ev_section(lines, ev_start) if ev_start is not None else []

    def bulk_insert(table: str, col: str, data: list):
        if not data:
            return
        conn.executemany(f"""
            INSERT OR REPLACE INTO {table}
                (season, rule, pokemon, rank, {col}, usage_rate, source, crawled_date, crawled_at)
            VALUES (?,?,?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r, label, rate, "pokedb", crawled_date, at)
              for r, label, rate in data])

    bulk_insert("pokemon_moves",     "move",      moves)
    bulk_insert("pokemon_items",     "item",      items)
    bulk_insert("pokemon_abilities", "ability",   abilities)
    bulk_insert("pokemon_natures",   "nature",    natures)

    if evs:
        conn.executemany("""
            INSERT OR REPLACE INTO pokemon_evs
                (season, rule, pokemon, rank, ev_spread,
                 ev_h, ev_a, ev_b, ev_c, ev_d, ev_s,
                 usage_rate, source, crawled_date, crawled_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r, label,
               s["H"], s["A"], s["B"], s["C"], s["D"], s["S"],
               rate, "pokedb", crawled_date, at)
              for r, label, rate, s in evs])

    # 持ち物の日別トレンドデータ（pokemonShowTrend）をバックフィル
    _save_item_trends(season, rule_str, name, soup, conn, at)

    # 同居ポケモン
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
                (season, rule, pokemon, rank, partner, source, crawled_date, crawled_at)
            VALUES (?,?,?,?,?,?,?,?)
        """, [(season, rule_str, name, r+1, p, "pokedb", crawled_date, at)
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

        # 更新日をリストページから取得（1回だけ）
        data_date = get_data_date_from_list_page(season, rule)
        print(f"\n=== pokedb: {season} {rule_str} (集計日: {data_date}) ===")

        pokemons = crawl_pokemon_list(season, rule)
        if not pokemons:
            continue

        save_usage_ranking(season, rule_str, pokemons, conn, data_date)

        targets = pokemons[:limit] if limit else pokemons
        for i, p in enumerate(targets, 1):
            print(f"  [{i:3}/{len(targets)}] {p['pokemon']}", end="\r")
            crawl_pokemon_detail(season, rule, p, conn, data_date)
            time.sleep(DELAY)

        print(f"\n  完了: {len(targets)}体")

    conn.close()


if __name__ == "__main__":
    crawl_season(season="M-2", rules=[0], limit=30)
