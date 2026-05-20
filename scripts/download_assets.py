"""
ポケナビ 画像アセットダウンローダー
- ポケモンアイコン: gamewith gacha/{dex_no}.png
- タイプスプライト: pokedb S3 type-sprite.png + CSS
- 持ち物スプライト: pokedb S3 item-sprite.png + CSS
"""
import re
import sys
import time
import sqlite3
from pathlib import Path

import requests

sys.path.append(str(Path(__file__).parent))
from db import get_conn

HEADERS_GW = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/124.0 Safari/537.36",
    "Referer": "https://gamewith.jp/",
}
HEADERS_PDB = {
    "User-Agent": "Mozilla/5.0 (compatible; pokenavi-bot/1.0)",
    "Referer": "https://champs.pokedb.tokyo/",
}

BASE_GW_IMG = "https://img.gamewith.jp/article_tools/pokemon-champions/gacha"
BASE_PDB_S3 = "https://s3-ap-northeast-1.amazonaws.com/pokedb.tokyo/champs/assets"
BASE_PDB    = "https://champs.pokedb.tokyo"

DELAY = 0.5

PROJECT_ROOT = Path(__file__).parent.parent
PUBLIC = PROJECT_ROOT / "public"


def fetch_binary(url: str, headers: dict):
    try:
        r = requests.get(url, headers=headers, timeout=20)
        r.raise_for_status()
        return r.content
    except Exception as e:
        print(f"  [ERROR] {url} → {e}")
        return None


def download_pokemon_icons():
    """gamewith から全ポケモンアイコンをダウンロード"""
    dest = PUBLIC / "images" / "pokemon"
    dest.mkdir(parents=True, exist_ok=True)

    conn = get_conn()
    rows = conn.execute("""
        SELECT DISTINCT pokemon_id, pokemon
        FROM pokemon_usage
        WHERE rule='single' AND source='gamewith'
        ORDER BY rank
    """).fetchall()
    conn.close()

    print(f"\n=== ポケモンアイコン: {len(rows)}体 ===")
    ok = skip = fail = 0
    for pokemon_id, name in rows:
        if not pokemon_id:
            print(f"  [SKIP] {name} — pokemon_id なし")
            skip += 1
            continue

        out = dest / f"{pokemon_id}.png"
        if out.exists():
            skip += 1
            continue

        url = f"{BASE_GW_IMG}/{pokemon_id}.png"
        data = fetch_binary(url, HEADERS_GW)
        if data:
            out.write_bytes(data)
            ok += 1
            print(f"  [{ok+skip+fail}/{len(rows)}] {name} ({pokemon_id}) ✓", end="\r")
        else:
            fail += 1
        time.sleep(DELAY)

    print(f"\n  完了: {ok}件DL, {skip}件スキップ, {fail}件失敗")


def download_pokemon_icons_from_db():
    """pokedb の pokemon_id (XXXX-YY 形式) をもとに pokedb S3 から webp をダウンロード"""
    dest = PUBLIC / "images" / "pokemon"
    dest.mkdir(parents=True, exist_ok=True)

    conn = get_conn()
    rows = conn.execute("""
        SELECT DISTINCT pokemon_id, pokemon
        FROM pokemon_usage
        WHERE rule='single' AND source='pokedb'
        ORDER BY rank
    """).fetchall()
    conn.close()

    print(f"\n=== ポケモンアイコン (pokedb webp): {len(rows)}体 ===")
    ok = skip = fail = 0
    for pokemon_id, name in rows:
        if not pokemon_id:
            skip += 1
            continue

        out = dest / f"pokemon-{pokemon_id}.webp"
        if out.exists():
            skip += 1
            continue

        url = f"{BASE_PDB_S3}/pokemon/icons_128/pokemon-{pokemon_id}.webp"
        data = fetch_binary(url, HEADERS_PDB)
        if data:
            out.write_bytes(data)
            ok += 1
            print(f"  [{ok+skip+fail}/{len(rows)}] {name} ({pokemon_id}) ✓", end="\r")
        else:
            fail += 1
        time.sleep(DELAY)

    print(f"\n  完了: {ok}件DL, {skip}件スキップ, {fail}件失敗")


def download_type_sprite():
    """タイプスプライト PNG と CSS をダウンロード"""
    dest = PUBLIC / "images" / "types"
    dest.mkdir(parents=True, exist_ok=True)

    # PNG
    out_png = dest / "type-sprite.png"
    if not out_png.exists():
        url = f"{BASE_PDB_S3}/icons/type/type-sprite.png"
        data = fetch_binary(url, HEADERS_PDB)
        if data:
            out_png.write_bytes(data)
            print(f"  type-sprite.png ✓ ({len(data):,} bytes)")
        else:
            print("  type-sprite.png 失敗")
    else:
        print("  type-sprite.png スキップ（既存）")

    # CSS
    out_css = dest / "type-sprite.css"
    if not out_css.exists():
        url = f"{BASE_PDB}/css/type-sprite.css"
        data = fetch_binary(url, HEADERS_PDB)
        if data:
            out_css.write_bytes(data)
            print(f"  type-sprite.css ✓ ({len(data):,} bytes)")
        else:
            print("  type-sprite.css 失敗")
    else:
        print("  type-sprite.css スキップ（既存）")


def download_item_sprite():
    """持ち物スプライト PNG と CSS をダウンロード"""
    dest = PUBLIC / "images" / "items"
    dest.mkdir(parents=True, exist_ok=True)

    out_png = dest / "item-sprite.png"
    if not out_png.exists():
        url = f"{BASE_PDB_S3}/icons/item/item-sprite.png"
        data = fetch_binary(url, HEADERS_PDB)
        if data:
            out_png.write_bytes(data)
            print(f"  item-sprite.png ✓ ({len(data):,} bytes)")
        else:
            print("  item-sprite.png 失敗")
    else:
        print("  item-sprite.png スキップ（既存）")

    out_css = dest / "item-sprite.css"
    if not out_css.exists():
        url = f"{BASE_PDB}/css/item-sprite.css"
        data = fetch_binary(url, HEADERS_PDB)
        if data:
            out_css.write_bytes(data)
            print(f"  item-sprite.css ✓ ({len(data):,} bytes)")
        else:
            print("  item-sprite.css 失敗")
    else:
        print("  item-sprite.css スキップ（既存）")


if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"

    print("=== ポケナビ 画像アセットダウンローダー ===")

    if mode in ("all", "pokemon-gw"):
        download_pokemon_icons()

    if mode in ("all", "pokemon-pdb"):
        download_pokemon_icons_from_db()

    if mode in ("all", "types"):
        print("\n=== タイプスプライト ===")
        download_type_sprite()

    if mode in ("all", "items"):
        print("\n=== 持ち物スプライト ===")
        download_item_sprite()

    print("\n完了")
