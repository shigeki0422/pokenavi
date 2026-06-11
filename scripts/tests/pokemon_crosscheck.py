#!/usr/bin/env python3
"""DBのポケモン種族値・タイプを PokeAPI（canonical）と照合する。

- base_stats の各行について PokeAPI スラッグを解決し、type と base stats を比較。
- スラッグ解決: pokeapi_name が英字スラッグならそれを使用。数値/空なら dex（標準形）→ /pokemon/{dex}。
  代表的な別形は ALT_SLUG で補完。解決できない別形は「要手動確認」として報告。
- 取得結果は scripts/.pokeapi_cache.json にキャッシュ（再実行で再取得しない）。
- Champions固有（独自メガ・PokeAPI非収録フォルム）は照合対象外（gamewith/PDFで別途確認）。

出力: タイプ不一致 / 種族値不一致 / 未照合（要手動）。不一致0が目標。
"""
import json
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "pokenavi.db"
CACHE = ROOT / ".pokeapi_cache.json"
ABCACHE = ROOT / ".pokeapi_ability_cache.json"
UA = {"User-Agent": "pokenavi-bot/1.0"}

EN2JP_TYPE = {
    "normal": "ノーマル", "fire": "ほのお", "water": "みず", "electric": "でんき",
    "grass": "くさ", "ice": "こおり", "fighting": "かくとう", "poison": "どく",
    "ground": "じめん", "flying": "ひこう", "psychic": "エスパー", "bug": "むし",
    "rock": "いわ", "ghost": "ゴースト", "dragon": "ドラゴン", "dark": "あく",
    "steel": "はがね", "fairy": "フェアリー",
}
# pokeapi_name が壊れている代表的別形のスラッグ補完
ALT_SLUG = {
    "ルガルガン(昼)": "lycanroc-midday", "ルガルガン(たそがれ)": "lycanroc-dusk",
    "ルガルガン(夜)": "lycanroc-midnight", "ルガルガン(まよなか)": "lycanroc-midnight",
    "ケンタロス:炎": "tauros-paldea-blaze-breed", "ケンタロス:水": "tauros-paldea-aqua-breed",
    "ケンタロス:格": "tauros-paldea-combat-breed",
    "ヒートロトム": "rotom-heat", "フロストロトム": "rotom-frost",
    "スピンロトム": "rotom-fan", "カットロトム": "rotom-mow",
    "パンプジン(ギガだましゅ)": "gourgeist-super", "パンプジン(おおだましゅ)": "gourgeist-large",
    "パンプジン(こだましゅ)": "gourgeist-small", "パンプジン(ちゅうだましゅ)": "gourgeist-average",
    "イダイトウ(メス)": "basculegion-female", "イダイトウ(オス)": "basculegion-male",
    "ビビヨン": "vivillon",
}


def load_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return {}


def fetch(slug, cache):
    if slug in cache and "abilities" in cache[slug]:
        return cache[slug]
    req = urllib.request.Request(f"https://pokeapi.co/api/v2/pokemon/{slug}", headers=UA)
    d = json.load(urllib.request.urlopen(req, timeout=25))
    out = {
        "name": d.get("name"),
        "types": [EN2JP_TYPE.get(t["type"]["name"]) for t in sorted(d["types"], key=lambda x: x["slot"])],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in d["stats"]},
        "abilities": [a["ability"]["name"] for a in d.get("abilities", [])],
    }
    cache[slug] = out
    CACHE.write_text(json.dumps(cache, ensure_ascii=False))
    time.sleep(0.3)
    return out


def slug_for(name, dex, form_index, pokeapi_name):
    if name in ALT_SLUG:
        return ALT_SLUG[name]
    if pokeapi_name and any(ch.isalpha() and ch.isascii() for ch in pokeapi_name):
        return pokeapi_name
    if form_index == 0:
        return str(dex)
    return None  # 別形でスラッグ不明


def ability_jp(slug, abcache):
    """PokeAPI英語特性スラッグ → 日本語名（/ability/{slug} の ja-Hrkt）。"""
    if slug in abcache:
        return abcache[slug]
    try:
        req = urllib.request.Request(f"https://pokeapi.co/api/v2/ability/{slug}", headers=UA)
        d = json.load(urllib.request.urlopen(req, timeout=25))
        jp = next((n["name"] for n in d["names"] if n["language"]["name"] in ("ja-Hrkt", "ja")), None)
        time.sleep(0.3)
    except Exception:
        jp = None
    abcache[slug] = jp
    ABCACHE.write_text(json.dumps(abcache, ensure_ascii=False))
    return jp


def check_abilities():
    """環境ポケモンの使用特性が PokeAPI の正規特性集合に含まれるか照合。
    含まれない＝データ誤り or Champions固有変更（後者はgamewith要確認）。"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("pa", ROOT / "tests" / "pokemon_audit.py")
    pa = importlib.util.module_from_spec(spec); spec.loader.exec_module(pa)
    from simulator.data import DataLoader
    dl = DataLoader(str(DB))
    c = sqlite3.connect(DB)
    env = [r[0] for r in c.execute(
        "SELECT DISTINCT pokemon FROM pokemon_usage WHERE season='M-2' AND rule='single'")]
    used = {}
    for pk, ab in c.execute(
            "SELECT DISTINCT pokemon, ability FROM pokemon_abilities WHERE season='M-2' AND rule='single'"):
        used.setdefault(pk, set()).add(ab)
    c.close()
    cache, abcache = load_cache(), (json.loads(ABCACHE.read_text()) if ABCACHE.exists() else {})

    # 使用名 → base_stats の正規スラッグ（ローダーと同じ解決：別名→リージョン接頭辞→exact/部分）
    c2 = sqlite3.connect(DB)

    def resolve_slug(pk):
        name = DataLoader.FORM_ALIASES.get(pk.replace(" (", "("), pk.replace(" (", "("))
        for prefix in ("ガラル", "アローラ", "ヒスイ", "パルデア"):
            if name.endswith(f"({prefix})"):
                name = f"{prefix}{name[:-len(prefix)-2]}"; break
        row = c2.execute("SELECT pokeapi_name, dex_number FROM pokemon_base_stats WHERE pokemon_name=?", (name,)).fetchone()
        if not row:
            row = c2.execute("SELECT pokeapi_name, dex_number FROM pokemon_base_stats WHERE pokemon_name LIKE ?",
                             (f"%{name.split('(')[0]}%",)).fetchone()
        if not row:
            return None
        pname, dex = row
        return pname if (pname and any(ch.isalpha() and ch.isascii() for ch in pname)) else str(dex)

    illegal, unresolved = [], []
    for pk in env:
        slug = resolve_slug(pk)
        if slug is None:
            unresolved.append(pk); continue
        try:
            api = fetch(slug, cache)
        except Exception:
            unresolved.append(pk); continue
        legal_jp = {ability_jp(s, abcache) for s in api.get("abilities", [])}
        legal_jp.discard(None)
        for ab in used.get(pk, ()):
            if ab not in legal_jp:
                illegal.append(f"{pk}: 使用特性'{ab}' がPokeAPI正規外 (正規={sorted(legal_jp)})")

    print(f"=== 特性 PokeAPI照合（環境{len(env)}種）===\n")
    print(f"【使用特性がPokeAPI正規外（データ誤り or Champions固有）: {len(illegal)}件】")
    for it in illegal[:80]:
        print(f"   {it}")
    print(f"\n【特性照合のためのスラッグ未解決: {len(unresolved)}件】 {unresolved[:10]}")
    return len(illegal)


def check_megas():
    """mega_stats を PokeAPI と照合。実在第6世代メガ＝値検証、PokeAPI非収録＝Champions独自として報告。"""
    c = sqlite3.connect(DB)
    base_api = {r[0]: r[1] for r in c.execute(
        "SELECT dex_number, pokeapi_name FROM pokemon_base_stats WHERE form_index=0")}
    megas = c.execute("SELECT mega_name_jp, base_dex, type1, type2, hp, attack, defense, "
                      "sp_attack, sp_defense, speed FROM pokemon_mega_stats").fetchall()
    c.close()
    cache = load_cache()
    STAT_KEYS = ["hp", "attack", "defense", "special-attack", "special-defense", "speed"]
    confirmed, type_mm, stat_mm, champions_orig, errors = [], [], [], [], []
    for (nm, dex, t1, t2, *st) in megas:
        try:
            bn = fetch(str(dex), cache)["name"]  # dexからベース種のスラッグ名を取得
        except Exception as e:
            errors.append(f"{nm}: base {type(e).__name__}"); continue
        slug = f"{bn}-mega-x" if nm.endswith("X") else f"{bn}-mega-y" if nm.endswith("Y") else f"{bn}-mega"
        try:
            api = fetch(slug, cache)
        except Exception:
            champions_orig.append(nm); continue  # PokeAPI非収録＝Champions独自
        db_types = [x for x in (t1, t2) if x]
        if db_types != [x for x in api["types"] if x]:
            type_mm.append(f"{nm}: DB={db_types} API={api['types']}")
        api_st = [api["stats"][k] for k in STAT_KEYS]
        if st != api_st:
            stat_mm.append(f"{nm}: DB={st} API={api_st}")
        if db_types == api["types"] and st == api_st:
            confirmed.append(nm)
    print(f"=== メガ PokeAPI照合（{len(megas)}件）===\n")
    print(f"【第6世代メガ・値一致(確認済): {len(confirmed)}件】")
    for title, items in [("メガ タイプ不一致", type_mm), ("メガ 種族値不一致(推定値の誤り)", stat_mm),
                         ("Champions独自メガ(PokeAPI非収録・gamewith要確認)", champions_orig)]:
        print(f"\n【{title}: {len(items)}件】")
        for it in items[:80]:
            print(f"   {it}")
    return len(type_mm) + len(stat_mm)


def main(limit=None, only_forms=False):
    c = sqlite3.connect(DB)
    rows = c.execute("SELECT pokemon_name, dex_number, form_index, pokeapi_name, "
                     "type1, type2, hp, attack, defense, sp_attack, sp_defense, speed "
                     "FROM pokemon_base_stats ORDER BY form_index DESC, dex_number").fetchall()
    c.close()
    if only_forms:
        rows = [r for r in rows if r[2] > 0]
    if limit:
        rows = rows[:limit]

    cache = load_cache()
    type_mismatch, stat_mismatch, unverified, errors = [], [], [], []
    STAT_KEYS = ["hp", "attack", "defense", "special-attack", "special-defense", "speed"]
    for (nm, dex, fi, pname, t1, t2, *st) in rows:
        slug = slug_for(nm, dex, fi, pname)
        if slug is None:
            unverified.append(nm)
            continue
        try:
            api = fetch(slug, cache)
        except Exception as e:
            errors.append(f"{nm}({slug}): {type(e).__name__}")
            continue
        db_types = [x for x in (t1, t2) if x]
        if db_types != [x for x in api["types"] if x]:
            type_mismatch.append(f"{nm}: DB={db_types} API={api['types']}")
        api_st = [api["stats"][k] for k in STAT_KEYS]
        if st != api_st:
            stat_mismatch.append(f"{nm}: DB={st} API={api_st}")

    print(f"=== PokeAPI照合（{len(rows)}姿）===\n")
    for title, items in [("タイプ不一致", type_mismatch), ("種族値不一致", stat_mismatch),
                         ("未照合(別形でスラッグ不明・要手動)", unverified), ("取得エラー", errors)]:
        print(f"【{title}: {len(items)}件】")
        for it in items[:60]:
            print(f"   {it}")
        print()
    return len(type_mismatch) + len(stat_mismatch)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mega" in args:
        sys.exit(1 if check_megas() else 0)
    if "--abilities" in args:
        sys.exit(1 if check_abilities() else 0)
    only_forms = "--forms" in args
    lim = next((int(a) for a in args if a.isdigit()), None)
    sys.exit(1 if main(limit=lim, only_forms=only_forms) else 0)
