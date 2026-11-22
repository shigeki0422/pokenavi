#!/usr/bin/env python3
"""
素早さ実数値ページ用JSON生成（環境で実際に使われている型のS実数値）
出力: src/data/speed.json
"""

import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DB_PATH = Path(__file__).parent / "pokenavi.db"
ARCH_PATH = ROOT / "src/data/archetypes.json"
OUT_PATH = ROOT / "src/data/speed.json"
IMGDIR = ROOT / "public/images/pokemon"
POKEMON_DIR = ROOT / "src/content/pokemon"

# scripts/simulator/pokemon.py calc_stat() と同じ（Lv50・IV31・EVは32スケールでev*2）
NATURE_UP_S = {"おくびょう", "せっかち", "ようき", "むじゃき"}
NATURE_DOWN_S = {"ゆうかん", "のんき", "れいせい", "なまいき"}


def calc_speed(base, ev, mod):
    return int((int((base * 2 + 31 + ev * 2) * 50 / 100) + 5) * mod)


def nature_mod(nature):
    if nature in NATURE_UP_S:
        return 1.1
    if nature in NATURE_DOWN_S:
        return 0.9
    return 1.0


def ev_s(ev_str):
    m = re.search(r"\bS(\d+)", ev_str or "")
    return int(m.group(1)) if m else 0


def load_page_slugs():
    by_name = {}
    for p in sorted(POKEMON_DIR.glob("*.md")):
        fm = p.read_text(encoding="utf-8").split("---", 2)
        if len(fm) < 3:
            continue
        name = re.search(r"^pokemonName:\s*'([^']+)'", fm[1], re.M)
        draft = re.search(r"^draft:\s*(\w+)", fm[1], re.M)
        if name and (not draft or draft.group(1) != "true"):
            by_name.setdefault(name.group(1), p.stem)
    return by_name


def main():
    arch = json.loads(ARCH_PATH.read_text(encoding="utf-8"))
    season = arch.get("_version", {}).get("season") if isinstance(arch.get("_version"), dict) else None

    con = sqlite3.connect(DB_PATH)
    base = {}
    for name, dex, form, t1, t2, spd in con.execute(
        "SELECT pokemon_name, dex_number, form_index, type1, type2, speed FROM pokemon_base_stats"
    ):
        base[f"{dex:04d}-{form:02d}"] = {"name": name, "types": [t for t in (t1, t2) if t], "speed": spd}

    mega = {}
    for mname, bname, stone, dex, t1, t2, spd in con.execute(
        "SELECT mega_name_jp, base_pokemon_jp, mega_stone, base_dex, type1, type2, speed FROM pokemon_mega_stats"
    ):
        mega[stone] = {"name": mname, "base": bname, "types": [t for t in (t1, t2) if t], "speed": spd, "dex": dex}

    seasons = [r[0] for r in con.execute("SELECT DISTINCT season FROM pokemon_usage")]
    latest = sorted(seasons, key=lambda s: (1, int(m.group(1))) if (m := re.match(r"M-(\d+)$", s or "")) else (0, 0))[-1]
    season = season or latest
    rank = {}
    for name, r in con.execute(
        "SELECT pokemon, MIN(rank) FROM pokemon_usage WHERE season=? AND rule='single' GROUP BY pokemon", (latest,)
    ):
        rank[name] = r
    con.close()

    slugs = load_page_slugs()
    mons = []
    for key, entry in arch.items():
        if key == "_version" or not isinstance(entry, dict):
            continue
        b = base.get(key)
        if not b:
            continue
        # 型を「素の姿」と「メガ」に分け、メガ側は mega_stone から種族値を引く
        forms = {}
        for grp in entry.get("groups", []):
            # sets の p は「その系統の中での割合」。全体比は 系統の割合 × p / 100。
            # また sets は系統ごとの上位3型だけなので、合計は100%にならない。
            gshare = grp.get("share", 0) or 0
            for st in grp.get("sets", []):
                stone = st.get("item", "")
                mg = mega.get(stone)
                fkey = stone if mg else ""
                f = forms.setdefault(fkey, {
                    "label": mg["name"] if mg else b["name"],
                    "icon": key,
                    "types": mg["types"] if mg else b["types"],
                    "baseSpeed": mg["speed"] if mg else b["speed"],
                    "lines": [],
                })
                nat = st.get("nature", "")
                spd = calc_speed(f["baseSpeed"], ev_s(st.get("ev", "")), nature_mod(nat))
                f["lines"].append({
                    "nature": nat,
                    "evS": ev_s(st.get("ev", "")),
                    "item": stone,
                    "speed": spd,
                    # こだわりスカーフは実効1.5倍（items.py get_speed_item_multiplier）
                    "eff": spd * 3 // 2 if stone == "こだわりスカーフ" else spd,
                    "share": round(gshare * (st.get("p", 0) or 0) / 100, 1),
                    "arch": grp.get("name", ""),
                })
        out_forms = []
        for f in forms.values():
            bs = f["baseSpeed"]
            # 同じ (性格補正, S) の型は実数値が同じなので採用率を合算する
            agg = {}
            for ln in f["lines"]:
                k = (ln["eff"], ln["item"] == "こだわりスカーフ")
                a = agg.setdefault(k, {**ln, "share": 0.0, "archs": []})
                a["share"] += ln["share"]
                if ln["arch"] and ln["arch"] not in a["archs"]:
                    a["archs"].append(ln["arch"])
            lines = sorted(agg.values(), key=lambda x: -x["share"])
            for ln in lines:
                ln.pop("arch", None)
                ln["share"] = round(ln["share"], 1)
            f["lines"] = lines
            f["ref"] = {
                "max": calc_speed(bs, 32, 1.1),
                "semi": calc_speed(bs, 32, 1.0),
                "none": calc_speed(bs, 0, 1.0),
                "maxScarf": calc_speed(bs, 32, 1.1) * 3 // 2,
            }
            out_forms.append(f)
        out_forms.sort(key=lambda f: -f["baseSpeed"])
        if not out_forms:
            continue
        mons.append({
            "key": key,
            "name": b["name"],
            "slug": slugs.get(b["name"]),
            "rank": rank.get(b["name"]),
            "forms": out_forms,
        })

    mons.sort(key=lambda m: (m["rank"] or 999))
    OUT_PATH.write_text(json.dumps({"season": season, "mons": mons}, ensure_ascii=False, indent=2), encoding="utf-8")
    forms_n = sum(len(m["forms"]) for m in mons)
    print(f"{season}: mons={len(mons)} forms={forms_n} (メガ {sum(1 for m in mons for f in m['forms'] if f['label'].startswith('メガ'))})")


if __name__ == "__main__":
    main()
