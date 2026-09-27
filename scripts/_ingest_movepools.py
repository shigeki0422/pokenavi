"""pokemon_learnsets（ポケモンごとの覚える技）を gamewith の習得技一覧から作り直す。

正本は gamewith のポケモン一覧ページ（全ポケモンの習得技IDと技マスタがページ内に埋め込まれている）。
PokeAPI のチャンピオンズ版より、パッチ反映・地方フォルムの分離・収録種数の点で正確だったため。
（使用率データを足す方式は、過去のクロールで地方フォルムが通常フォルム名で保存された日があり、
  キュウコンがオーロラベールを覚える等の誤りを持ち込んだので廃止した）

- move_master に無い技（チャンピオンズにはあるが未登録）は入れずに報告する。
- REMOVED はパッチでの没収の保険。gamewith 側が未反映だった場合に備える。
- move_master.name_en が空の技は PokeAPI の和名から補完する（ページの英語表示用）。

使い方: python3 scripts/_ingest_movepools.py [--dry]
"""
import html
import importlib.util
import json
import re
import sqlite3
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "pokenavi.db"
MOVE_NAMES_CACHE = ROOT / ".pokeapi_move_names.json"
GW_LIST_URL = "https://gamewith.jp/pokemon-champions/546414"
GW_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Referer": "https://gamewith.jp/",
}
UA = {"User-Agent": "pokenavi-bot/1.0"}

REMOVED = {
    "ニョロトノ": {"はたく"},                          # M-6
    "ブリジュラス": {"ミラーコート", "メタルバースト"},  # M-6
}

# POKEMON_DATA のキー → gamewith 側の名前（正規化で一致しないもの）
GW_NAME = {
    "イキリンコ(グリーン)": "イキリンコ(グリーンフェザー)",
    "イキリンコ(ブルー)": "イキリンコ(ブルーフェザー)",
    "イキリンコ(イエロー)": "イキリンコ(イエローフェザー)",
    "イキリンコ(ホワイト)": "イキリンコ(ホワイトフェザー)",
    "ギルガルド": "ギルガルド(シールドフォルム)",
    "フラエッテ(永遠)": "フラエッテ(えいえんのはな)",
    "イルカマン": "イルカマン(マイティ)",
    "ケンタロス:格": "パルデアケンタロス(かくとう)",
    "ケンタロス:炎": "パルデアケンタロス(ほのお)",
    "ケンタロス:水": "パルデアケンタロス(みず)",
    "ルガルガン(昼)": "ルガルガン(まひる)",
    "カエンジシ": "カエンジシ(オスのすがた)",
}

# 旧表記のキー。consumer(sim_server 等)がこの名前で引くので正規キーと同じ中身にする。
ALIASES = {
    "イダイトウ (オス)": "イダイトウ(オス)",
    "イダイトウ (メス)": "イダイトウ(メス)",
    "ルガルガン (たそがれ)": "ルガルガン(たそがれ)",
    "ルガルガン (まよなか)": "ルガルガン(まよなか)",
    "ルガルガン(夜)": "ルガルガン(まよなか)",
    "フラエッテ:永遠": "フラエッテ(永遠)",
}

REGIONS = ("アローラ", "ガラル", "ヒスイ", "パルデア")


def norm(name: str) -> str:
    n = name.replace("（", "(").replace("）", ")").replace(" ", "").replace(":", "(")
    if "(" in n and not n.endswith(")"):
        n += ")"
    m = re.match(r"^(.+?)\((.+)\)$", n)
    if m:
        base, sfx = m.groups()
        return sfx + base if sfx in REGIONS else f"{base}({sfx})"
    return n


def get_json(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except Exception:
            if i == 2:
                return None
            time.sleep(2)


def load_move_names() -> dict:
    if MOVE_NAMES_CACHE.exists():
        return json.loads(MOVE_NAMES_CACHE.read_text(encoding="utf-8"))
    lst = get_json("https://pokeapi.co/api/v2/move?limit=2000")["results"]
    ja2slug = {}
    for m in lst:
        d = get_json(m["url"])
        for n in (d or {}).get("names", []):
            if n["language"]["name"] in ("ja-Hrkt", "ja"):
                ja2slug.setdefault(n["name"], d["name"])
        time.sleep(0.03)
    MOVE_NAMES_CACHE.write_text(json.dumps(ja2slug, ensure_ascii=False), encoding="utf-8")
    return ja2slug


def load_gamewith() -> dict:
    """{gamewith上のポケモン名: {技名,...}}"""
    req = urllib.request.Request(GW_LIST_URL, headers=GW_HEADERS)
    s = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    moves = {i: html.unescape(n) for i, n in re.findall(r"\{id:'(\d+)',n:'([^']+)',t:'", s)}
    recs = re.findall(r"\{id:'\d+',idx:\d+,aid:'\d*',no:'\d+',n:'([^']+)',[^}]*?mvs:'([^']*)'", s)
    if not moves or not recs:
        sys.exit("gamewith のページ構造が変わっている（技マスタ or ポケモン一覧を抽出できない）")
    return {html.unescape(n): {moves[x] for x in mvs.split(",") if x in moves} for n, mvs in recs}


def load_pokemon_data() -> dict:
    spec = importlib.util.spec_from_file_location("gp", ROOT / "generate_pokemon_pages.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.POKEMON_DATA


def main():
    dry = "--dry" in sys.argv
    c = sqlite3.connect(DB)

    ja2slug = load_move_names()
    filled = [(ja2slug[jp], jp) for jp, en in c.execute("SELECT name_jp, name_en FROM move_master").fetchall()
              if not en and ja2slug.get(jp)]
    if not dry:
        c.executemany("UPDATE move_master SET name_en=? WHERE name_jp=?", filled)
    print(f"name_en 補完: {len(filled)}技")

    master = {r[0] for r in c.execute("SELECT name_jp FROM move_master")}
    gw = load_gamewith()
    gw_by_norm = {norm(k): k for k in gw}
    print(f"gamewith: {len(gw)}体")

    new, not_found, not_in_master = {}, [], {}
    for name in load_pokemon_data():
        key = GW_NAME.get(name) or gw_by_norm.get(norm(name))
        if key not in gw:
            not_found.append(name)
            continue
        for mv in gw[key] - master:
            not_in_master.setdefault(mv, []).append(name)
        new[name] = (gw[key] & master) - REMOVED.get(name, set())
    for alias, canon in ALIASES.items():
        if canon in new:
            new[alias] = new[canon]

    before = {}
    for pk, mv in c.execute("SELECT pokemon_name, move_jp FROM pokemon_learnsets"):
        before.setdefault(pk, set()).add(mv)
    added = sum(len(v - before.get(k, set())) for k, v in new.items())
    removed = sum(len(before.get(k, set()) - v) for k, v in new.items())

    if not dry:
        for name, moves in new.items():
            c.execute("DELETE FROM pokemon_learnsets WHERE pokemon_name=?", (name,))
            c.executemany("INSERT INTO pokemon_learnsets(pokemon_name, move_jp) VALUES(?,?)",
                          [(name, m) for m in sorted(moves)])
        c.commit()
    tag = "[DRY] " if dry else ""
    print(f"{tag}作り直し: {len(new)}種 / 追加{added}件 / 削除{removed}件")
    if not_found:
        print(f"{tag}[WARN] gamewith に対応するポケモンが無い: {not_found}")
    if not_in_master:
        print(f"{tag}[WARN] move_master に無いため入れなかった技: "
              + ", ".join(f"{m}({'・'.join(v)})" for m, v in sorted(not_in_master.items())))
    c.close()


if __name__ == "__main__":
    main()
