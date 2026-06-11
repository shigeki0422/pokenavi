"""
PokeAPIからSVレアセット（SV覚え技一覧）を取得し pokemon_learnsets テーブルに保存。
"""
import sys
import time
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

sys.path.append(str(Path(__file__).parent))
from db import get_conn

BASE_URL = "https://pokeapi.co/api/v2"
HEADERS = {"User-Agent": "pokenavi-bot/1.0"}
VERSION_GROUPS = ["scarlet-violet", "sword-shield", "brilliant-diamond-shining-pearl", "ultra-sun-ultra-moon"]
DB_PATH = Path(__file__).parent / "pokenavi.db"


def get_json(url: str, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                time.sleep(2)
        except Exception as e:
            print(f"  [ERROR] {url}: {e}")
            return None
    return None


def ensure_table():
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_learnsets (
            pokemon_name TEXT NOT NULL,
            move_jp      TEXT NOT NULL,
            PRIMARY KEY (pokemon_name, move_jp)
        )
    """)
    con.commit()
    con.close()


def build_en_to_jp() -> dict:
    con = sqlite3.connect(DB_PATH)
    rows = con.execute("SELECT name_en, name_jp FROM move_master WHERE name_en IS NOT NULL").fetchall()
    con.close()
    return {row[0]: row[1] for row in rows}


def fetch_sv_moves(pokeapi_key: str):
    data = get_json(f"{BASE_URL}/pokemon/{pokeapi_key}")
    if not data:
        return []
    # 優先度順にバージョングループを試す
    for vg in VERSION_GROUPS:
        result = []
        for m in data["moves"]:
            if any(vgd["version_group"]["name"] == vg for vgd in m["version_group_details"]):
                result.append(m["move"]["name"])
        if result:
            return result
    return []


def fetch_jp_name_from_api(en_name: str):
    data = get_json(f"{BASE_URL}/move/{en_name}")
    if not data:
        return None
    for name_entry in data.get("names", []):
        if name_entry["language"]["name"] == "ja-Hrkt":
            return name_entry["name"]
    return None


def process_pokemon(pokemon_name: str, pokeapi_key: str, en_to_jp: dict):
    """各スレッドで独立したDB接続を使う"""
    en_moves = fetch_sv_moves(pokeapi_key)
    if not en_moves:
        return pokemon_name, 0

    jp_moves = []
    for en in en_moves:
        jp = en_to_jp.get(en)
        if not jp:
            jp = fetch_jp_name_from_api(en)
            if jp:
                en_to_jp[en] = jp
        if jp:
            jp_moves.append(jp)

    if jp_moves:
        con = sqlite3.connect(DB_PATH)
        try:
            con.executemany(
                "INSERT OR REPLACE INTO pokemon_learnsets (pokemon_name, move_jp) VALUES (?,?)",
                [(pokemon_name, mv) for mv in jp_moves]
            )
            con.commit()
        finally:
            con.close()

    return pokemon_name, len(jp_moves)


def main():
    ensure_table()
    en_to_jp = build_en_to_jp()

    con = sqlite3.connect(DB_PATH)
    rows = con.execute("""
        SELECT DISTINCT pokemon_name, pokeapi_name, dex_number, form_index
        FROM pokemon_base_stats
        ORDER BY dex_number, form_index
    """).fetchall()
    done = set(r[0] for r in con.execute("SELECT DISTINCT pokemon_name FROM pokemon_learnsets").fetchall())
    con.close()

    # フォルム違いは同じレアセットとして代表のpokeapi_keyを使う
    dex_to_key = {}
    name_to_key = {}
    for poke_name, api_name, dex, form_idx in rows:
        key = str(api_name) if api_name else str(dex)
        name_to_key[poke_name] = key
        if dex not in dex_to_key:
            dex_to_key[dex] = key
    for poke_name, api_name, dex, form_idx in rows:
        if form_idx != 0:
            name_to_key[poke_name] = dex_to_key.get(dex, str(api_name))

    targets = [(name, key) for name, key in name_to_key.items() if name not in done]
    print(f"取得対象: {len(targets)}体 (スキップ: {len(done)}体)")

    results = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(process_pokemon, name, key, en_to_jp): name
                   for name, key in targets}
        for i, f in enumerate(as_completed(futures), 1):
            name, count = f.result()
            results.append((name, count))
            print(f"  [{i:3}/{len(targets)}] {name}: {count}技", end="\r")

    ok = sum(1 for _, c in results if c > 0)
    zero = [(n, c) for n, c in results if c == 0]
    print(f"\n完了: {ok}体成功, {len(zero)}体0技")
    if zero:
        print("  0技のポケモン:", [n for n, _ in zero[:10]])


if __name__ == "__main__":
    main()
