#!/usr/bin/env python3
"""
構築まとめページ用JSON生成（同居率ベースの軸の組み合わせ）
出力: src/data/builds.json
"""

import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent.parent
DB_PATH = Path(__file__).parent / "pokenavi.db"
OUT_PATH = ROOT / "src/data/builds.json"
IMGDIR = ROOT / "public/images/pokemon"
POKEMON_DIR = ROOT / "src/content/pokemon"
NAME_MAP_TS = ROOT / "src/data/ranking-name-map.ts"
SPECIES_JSON = ROOT / "public/suggest-data/species.json"

ALIASES = {
    "フラエッテ(永遠)": "0670-05",
    "アローラキュウコン": "0038-01", "ライチュウ(アローラ)": "0026-01",
    "アローラライチュウ": "0026-01", "アローラペルシアン": "0053-01",
    "ガラルヤドキング": "0199-01", "ガラルヤドラン": "0080-02",
    "マッギョ(ガラル)": "0618-01",
    "ヒスイダイケンキ": "0503-01", "ヒスイゾロアーク": "0571-01",
    "ヒスイウインディ": "0059-01", "ヒスイバクフーン": "0157-01",
    "ヒスイクレベース": "0713-01", "ヒスイジュナイパー": "0724-01",
    "ヒスイヌメルゴン": "0706-01",
    "ルガルガン(たそがれ)": "0745-02", "ルガルガン(まよなか)": "0745-01",
    "ウォッシュロトム": "0479-02", "ヒートロトム": "0479-01",
    "カットロトム": "0479-05", "フロストロトム": "0479-03",
    "スピンロトム": "0479-04",
    "イダイトウ(オス)": "0902-00", "イダイトウ(メス)": "0902-01",
    "ニャオニクス(オス)": "0678-00", "ニャオニクス(メス)": "0678-01",
    "ケンタロス:炎": "0128-02", "ケンタロス:水": "0128-03", "ケンタロス:格": "0128-01",
    "ビビヨン": "0666-18",
}

CLASSIC_RANK = 15
CLASSIC_N = 12
SIGNATURE_RANK = 60
SIGNATURE_MIN_SCORE = 25
SIGNATURE_N = 8
TRIO_RANK = 30
TRIO_N = 8
CORE_N = 20
CORE_PARTNERS = 5


def latest_season(con, table):
    rows = [r[0] for r in con.execute(f"SELECT DISTINCT season FROM {table}")]
    def key(s):
        m = re.match(r"M-(\d+)$", s or "")
        return (1, int(m.group(1))) if m else (0, 0)
    return sorted(rows, key=key)[-1]


def load_name_map():
    text = NAME_MAP_TS.read_text(encoding="utf-8")
    return dict(re.findall(r"'([^']+)':\s*'([^']+)'", text))


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


def load_suggest():
    """軸から簡単構築のスラッグ(party-suggest/[slug].astro と同じ規則)。
    非メガのページが無い種は、実際に使われているメガの枠へ案内する。"""
    species = json.loads(SPECIES_JSON.read_text(encoding="utf-8"))
    mega_count = {}
    for s in species:
        if s["mega"]:
            mega_count[s["sp"]] = mega_count.get(s["sp"], 0) + 1
    out = {}
    for s in species:
        sp = s["sp"]
        if s["mega"]:
            variant = None
            if mega_count.get(sp, 0) > 1:
                m = re.search(r"([XYZ])$", s["label"])
                variant = m.group(1).lower() if m else None
            suffix = f"mega-{{slug}}-{variant}" if variant else "mega-{slug}"
        else:
            suffix = "{slug}"
        out.setdefault(sp, []).append({"label": s["label"], "pattern": suffix, "mega": bool(s["mega"])})
    return out


def main():
    con = sqlite3.connect(DB_PATH)
    season = latest_season(con, "pokemon_partners")
    date = con.execute(
        "SELECT MAX(crawled_date) FROM pokemon_partners WHERE season=? AND rule='single'", (season,)
    ).fetchone()[0]

    usage = {}
    for name, rank in con.execute(
        "SELECT pokemon, MIN(rank) FROM pokemon_usage WHERE season=? AND rule='single' GROUP BY pokemon", (season,)
    ):
        usage[name] = rank

    partners = {}
    for mon, rank, partner in con.execute(
        "SELECT pokemon, rank, partner FROM pokemon_partners WHERE season=? AND rule='single'", (season,)
    ):
        partners.setdefault(mon, {})[partner] = rank

    icon_map = {}
    for name, dex, form in con.execute("SELECT pokemon_name, dex_number, form_index FROM pokemon_base_stats"):
        iid = f"{dex:04d}-{form:02d}"
        if (IMGDIR / f"pokemon-{iid}.webp").exists():
            icon_map.setdefault(name, iid)
    for k, v in ALIASES.items():
        if (IMGDIR / f"pokemon-{v}.webp").exists():
            icon_map[k] = v
    con.close()

    name_map = load_name_map()
    page_slugs = load_page_slugs()
    suggest = load_suggest()

    def mon(name):
        slug = page_slugs.get(name_map.get(name, name)) or page_slugs.get(name)
        # 軸から簡単構築のページは pokemonName の完全一致でしか生成されないため、
        # 表記ゆれ対応表を通した名前で組み立てるとリンク先が404になる。
        suggest_slug = page_slugs.get(name)
        entries = suggest.get(name, [])
        entry = next((e for e in entries if not e["mega"]), entries[0] if entries else None)
        return {
            "name": name,
            "icon": icon_map.get(name),
            "rank": usage.get(name),
            "slug": slug,
            "suggest": entry["pattern"].format(slug=suggest_slug) if entry and suggest_slug else None,
            "suggestLabel": entry["label"] if entry and suggest_slug else None,
        }

    def mutual(a, b):
        ra = partners.get(a, {}).get(b)
        rb = partners.get(b, {}).get(a)
        return (ra, rb) if ra and rb else (None, None)

    pairs = []
    for a in partners:
        for b in partners[a]:
            if a >= b:
                continue
            ra, rb = mutual(a, b)
            if not ra:
                continue
            ua, ub = usage.get(a, 999), usage.get(b, 999)
            pairs.append({"a": a, "b": b, "ra": ra, "rb": rb, "ua": ua, "ub": ub,
                          "tie": ra + rb, "spec": (ub - ra) + (ua - rb)})

    classic = sorted(
        (p for p in pairs if p["ua"] <= CLASSIC_RANK and p["ub"] <= CLASSIC_RANK),
        key=lambda p: (p["tie"], p["ua"] + p["ub"]),
    )[:CLASSIC_N]

    signature = sorted(
        (p for p in pairs if p["ua"] <= SIGNATURE_RANK and p["ub"] <= SIGNATURE_RANK
         and p["ra"] <= 5 and p["rb"] <= 5 and p["spec"] >= SIGNATURE_MIN_SCORE),
        key=lambda p: -p["spec"],
    )[:SIGNATURE_N]

    top = [m for m, _ in sorted(usage.items(), key=lambda x: x[1]) if m in partners]
    trio_pool = [m for m in top if usage[m] <= TRIO_RANK]
    trios = []
    for i, a in enumerate(trio_pool):
        for j in range(i + 1, len(trio_pool)):
            b = trio_pool[j]
            if not mutual(a, b)[0]:
                continue
            for k in range(j + 1, len(trio_pool)):
                c = trio_pool[k]
                if not mutual(a, c)[0] or not mutual(b, c)[0]:
                    continue
                score = sum(sum(mutual(x, y)) for x, y in ((a, b), (a, c), (b, c)))
                trios.append({"mons": [a, b, c], "score": score})
    trios.sort(key=lambda t: (t["score"], sum(usage[m] for m in t["mons"])))
    trios = trios[:TRIO_N]

    by_core = []
    for m in top[:CORE_N]:
        ps = sorted(partners[m].items(), key=lambda x: x[1])[:CORE_PARTNERS]
        by_core.append({"core": mon(m), "partners": [mon(p) for p, _ in ps]})

    out = {
        "season": season,
        "date": date,
        "classic": [{"a": mon(p["a"]), "b": mon(p["b"]), "ra": p["ra"], "rb": p["rb"]} for p in classic],
        "signature": [{"a": mon(p["a"]), "b": mon(p["b"]), "ra": p["ra"], "rb": p["rb"]} for p in signature],
        "trios": [{"mons": [mon(m) for m in t["mons"]]} for t in trios],
        "byCore": by_core,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{season} ({date}): classic={len(out['classic'])} signature={len(out['signature'])} "
          f"trios={len(out['trios'])} byCore={len(out['byCore'])}")


if __name__ == "__main__":
    main()
