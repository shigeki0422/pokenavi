"""種族ごとの特性一覧（通常・隠れ）をPokeAPIから取得して pokemon_species_abilities に保存する。

pokemon_abilities は使用率クロール由来のため、一度も使用率に載っていないポケモンの
特性が分からない。ページ生成側のフォールバック用にここで種族の特性そのものを持つ。

キーは generate_pokemon_pages.py の POKEMON_DATA のキー（ページ生成が使う和名）。
PokeAPIのスラッグは pokemon_base_stats.pokeapi_name を dex+form で引いて解決する。
"""
import importlib.util
import json
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "pokenavi.db"
CACHE = ROOT / ".pokeapi_ability_names.json"
UA = {"User-Agent": "pokenavi-bot/1.0"}
DELAY = 0.2


def get_json(url: str, retries: int = 3):
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                return json.load(r)
        except Exception as e:
            if i == retries - 1:
                print(f"  [ERROR] {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2)


def load_pokemon_data():
    spec = importlib.util.spec_from_file_location("gp", ROOT / "generate_pokemon_pages.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.POKEMON_DATA


def main() -> int:
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    con.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_species_abilities (
            pokemon_name TEXT NOT NULL,
            slot         INTEGER NOT NULL,
            ability      TEXT NOT NULL,
            is_hidden    INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (pokemon_name, slot)
        )
    """)

    rows = list(con.execute("SELECT dex_number, form_index, pokeapi_name FROM pokemon_base_stats"))
    by_df = {(r["dex_number"], r["form_index"]): r["pokeapi_name"] for r in rows}
    by_dex = {}
    for r in rows:
        by_dex.setdefault(r["dex_number"], []).append(r["pokeapi_name"])

    names = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}

    def ability_jp(slug: str) -> str:
        if slug in names:
            return names[slug]
        d = get_json(f"https://pokeapi.co/api/v2/ability/{slug}")
        jp = slug
        if d:
            jp = next((n["name"] for n in d["names"] if n["language"]["name"] == "ja-Hrkt"),
                      next((n["name"] for n in d["names"] if n["language"]["name"] == "ja"), slug))
        names[slug] = jp
        time.sleep(DELAY)
        return jp

    data = load_pokemon_data()
    ok = fail = 0
    unknown = []
    known = {r[0] for r in con.execute("SELECT name_jp FROM ability_master")}
    for name, p in data.items():
        dex, form = int(p["dex"]), int(p["id"].split("-")[1])
        slug = by_df.get((dex, form)) or by_df.get((dex, 99))
        if not slug:
            cand = by_dex.get(dex, [])
            slug = cand[0] if len(cand) == 1 else None
        if not slug:
            print(f"  [SKIP] {name}: スラッグ未解決")
            fail += 1
            continue
        d = get_json(f"https://pokeapi.co/api/v2/pokemon/{slug}")
        if not d:
            # 一部のスラッグは404になる(pyroar等)。図鑑番号なら引ける。
            d = get_json(f"https://pokeapi.co/api/v2/pokemon/{dex}")
        if not d:
            fail += 1
            continue
        con.execute("DELETE FROM pokemon_species_abilities WHERE pokemon_name=?", (name,))
        for a in sorted(d["abilities"], key=lambda x: x["slot"]):
            jp = ability_jp(a["ability"]["name"])
            if jp not in known:
                unknown.append((name, jp, a["ability"]["name"]))
            con.execute(
                "INSERT OR REPLACE INTO pokemon_species_abilities(pokemon_name, slot, ability, is_hidden)"
                " VALUES(?,?,?,?)", (name, a["slot"], jp, 1 if a["is_hidden"] else 0))
        ok += 1
        print(f"  [{ok+fail}/{len(data)}] {name} ({slug})", end="\r")
        time.sleep(DELAY)

    con.commit()
    CACHE.write_text(json.dumps(names, ensure_ascii=False, indent=0), encoding="utf-8")
    total = con.execute("SELECT count(*) FROM pokemon_species_abilities").fetchone()[0]
    con.close()
    print(f"\n完了: {ok}体 / 失敗{fail}体 / 行数{total}")
    if unknown:
        print(f"[WARN] ability_master に無い特性 {len(unknown)}件: "
              + ", ".join(f"{n}:{jp}({en})" for n, jp, en in unknown[:20]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
