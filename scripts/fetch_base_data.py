#!/usr/bin/env python3
"""
PokeAPIからポケモン種族値・技データを取得してDBに格納する。
テーブル: pokemon_base_stats, pokemon_mega_stats, move_master
"""
import sqlite3
import requests
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

DB_PATH = "pokenavi.db"
BASE_URL = "https://pokeapi.co/api/v2"
MAX_WORKERS = 15

TYPE_JP = {
    "normal": "ノーマル", "fighting": "かくとう", "flying": "ひこう",
    "poison": "どく", "ground": "じめん", "rock": "いわ",
    "bug": "むし", "ghost": "ゴースト", "steel": "はがね",
    "fire": "ほのお", "water": "みず", "grass": "くさ",
    "electric": "でんき", "psychic": "エスパー", "ice": "こおり",
    "dragon": "ドラゴン", "dark": "あく", "fairy": "フェアリー",
}

# pokemon_idなしの特殊フォーム: JP名 → (dex番号, PokeAPI名)
FORM_OVERRIDES = {
    "アローラキュウコン":       (38,  "ninetales-alola"),
    "アローラライチュウ":       (26,  "raichu-alola"),
    "ウォッシュロトム":         (479, "rotom-wash"),
    "カットロトム":             (479, "rotom-mow"),
    "ヒートロトム":             (479, "rotom-heat"),
    "フロストロトム":           (479, "rotom-frost"),
    "スピンロトム":             (479, "rotom-fan"),
    "ガラルマッギョ":           (618, "stunfisk-galar"),
    "ガラルヤドキング":         (199, "slowking-galar"),
    "ガラルヤドラン":           (80,  "slowbro-galar"),
    "ヒスイウインディ":         (59,  "arcanine-hisui"),
    "ヒスイクレベース":         (713, "avalugg-hisui"),
    "ヒスイジュナイパー":       (724, "decidueye-hisui"),
    "ヒスイゾロアーク":         (571, "zoroark-hisui"),
    "ヒスイダイケンキ":         (503, "samurott-hisui"),
    "ヒスイヌメルゴン":         (704, "goodra-hisui"),
    "ヒスイバクフーン":         (157, "typhlosion-hisui"),
    "イダイトウ(メス)":         (902, "basculegion-female"),
    "パルデアケンタロス(闘)":   (128, "tauros-paldea-combat-breed"),
    "パルデアケンタロス(炎)":   (128, "tauros-paldea-blaze-breed"),
    "パルデアケンタロス(水)":   (128, "tauros-paldea-aqua-breed"),
    "ルガルガン(夜)":           (745, "lycanroc-midnight"),
    "ルガルガン(黄昏)":         (745, "lycanroc-dusk"),
    "ニャオニクス(メス)":       (678, "meowstic-female"),
    "パンプジン(おおだま)":     (711, "gourgeist-large"),
    "パンプジン(ちゅうだま)":   (711, "gourgeist-average"),
    "パンプジン(ギガだま)":     (711, "gourgeist-super"),
    "フラエッテ(永遠)":         (670, "floette-eternal"),
}

# メガ進化: メガストーン名 → (基本dex, PokeAPI名, JP名)
MEGA_STONE_MAP = {
    "フシギバナイト":   (3,   "venusaur-mega",      "メガフシギバナ"),
    "リザードナイトＸ": (6,   "charizard-mega-x",   "メガリザードンX"),
    "リザードナイトＹ": (6,   "charizard-mega-y",   "メガリザードンY"),
    "カメックスナイト": (9,   "blastoise-mega",     "メガカメックス"),
    "スピアーナイト":   (15,  "beedrill-mega",      "メガスピアー"),
    "ピジョットナイト": (18,  "pidgeot-mega",       "メガピジョット"),
    "ゲンガナイト":     (94,  "gengar-mega",        "メガゲンガー"),
    "ガルーラナイト":   (115, "kangaskhan-mega",    "メガガルーラ"),
    "ギャラドスナイト": (130, "gyarados-mega",      "メガギャラドス"),
    "ハッサムナイト":   (212, "scizor-mega",        "メガハッサム"),
    "ヘラクロスナイト": (214, "heracross-mega",     "メガヘラクロス"),
    "ヘルガナイト":     (229, "houndoom-mega",      "メガヘルガー"),
    "バンギラスナイト": (248, "tyranitar-mega",     "メガバンギラス"),
    "デンリュウナイト": (181, "ampharos-mega",      "メガデンリュウ"),
    "ハガネールナイト": (208, "steelix-mega",       "メガハガネール"),
    "チャーレムナイト": (308, "medicham-mega",      "メガチャーレム"),
    "ライボルトナイト": (310, "manectric-mega",     "メガライボルト"),
    "バクーダナイト":   (323, "camerupt-mega",      "メガバクーダ"),
    "チルタリスナイト": (334, "altaria-mega",       "メガチルタリス"),
    "サーナイトナイト": (282, "gardevoir-mega",     "メガサーナイト"),
    "エルレイドナイト": (475, "gallade-mega",       "メガエルレイド"),
    "サメハダナイト":   (319, "sharpedo-mega",      "メガサメハダー"),
    "ヤミラミナイト":   (302, "sableye-mega",       "メガヤミラミ"),
    "ボスゴドラナイト": (306, "aggron-mega",        "メガボスゴドラ"),
    "フーディナイト":   (65,  "alakazam-mega",      "メガフーディン"),
    "ガブリアスナイト": (445, "garchomp-mega",      "メガガブリアス"),
    "ルカリオナイト":   (448, "lucario-mega",       "メガルカリオ"),
    "アブソルナイト":   (359, "absol-mega",         "メガアブソル"),
    "ユキノオナイト":   (460, "abomasnow-mega",     "メガユキノオ"),
    "ジュペッタナイト": (354, "banette-mega",       "メガジュペッタ"),
    "ミミロップナイト": (428, "lopunny-mega",       "メガミミロップ"),
    "プテラナイト":     (142, "aerodactyl-mega",    "メガプテラ"),
    "ヤドランナイト":   (80,  "slowbro-mega",       "メガヤドラン"),
    "ピクシナイト":     (36,  None, "メガピクシー"),       # Champions独自
    "スターミナイト":   (121, None, "メガスターミー"),     # Champions独自
    "カイリュナイト":   (149, None, "メガカイリュー"),     # Champions独自
    "エアームドナイト": (227, None, "メガエアームド"),     # Champions独自
    "ウツボットナイト": (71,  None, "メガウツボット"),     # Champions独自
    "フラエッテナイト": (670, None, "メガフラエッテ"),     # Champions独自
    "ゲッコウガナイト": (658, None, "メガゲッコウガ"),     # Champions独自
    "ドリュウズナイト": (530, None, "メガドリュウズ"),     # Champions独自
    "メガニウムナイト": (154, None, "メガメガニウム"),     # Champions独自
    "オーダイルナイト": (160, None, "メガオーダイル"),     # Champions独自
    "ブリガロナイト":   (652, None, "メガブリガロン"),     # Champions独自
    "マフォクシナイト": (655, None, "メガマフォクシー"),   # Champions独自
    "ニャオニクスナイト":(678, None, "メガニャオニクス"),  # Champions独自
    "ルチャブルナイト": (701, None, "メガルチャブル"),     # Champions独自
    "キラフロルナイト": (1001,None, "メガキラフロル"),     # Champions独自
    "スコヴィラナイト": (1006,None, "メガスコヴィラン"),   # Champions独自
    "シャンデラナイト": (609, None, "メガシャンデラ"),     # Champions独自
    "ジジーロナイト":   (683, None, "メガジジーロン"),     # Champions独自
    "チリーンナイト":   (358, None, "メガチリーン"),       # Champions独自
    "タブンネナイト":   (531, None, "メガタブンネ"),       # Champions独自
    "オニゴーリナイト": (361, None, "メガオニゴーリ"),     # Champions独自
    "ユキメノコナイト": (478, None, "メガユキメノコ"),     # Champions独自
    "ケケンカニナイト": (768, None, "メガケケンカニ"),     # Champions独自
    "ゴルーグナイト":   (623, None, "メガゴルーグ"),       # Champions独自
    "エンブオナイト":   (500, None, "メガエンブオー"),     # Champions独自
    "バクフーンナイト": (157, None, "メガバクフーン"),     # Champions独自 (エンブオーと区別)
}


def get_json(url, retries=3):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        except Exception as e:
            if i == retries - 1:
                print(f"  ERROR {url}: {e}")
                return None
            time.sleep(1)


def parse_pokemon_id(pid):
    """'0445-00' or '445' or '006' → (dex_number, form_index)"""
    if not pid:
        return None, None
    pid = pid.strip()
    if "-" in pid:
        parts = pid.split("-")
        return int(parts[0]), int(parts[1])
    else:
        return int(pid), 0


def extract_stats(data):
    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
    return {
        "hp":         stats.get("hp", 0),
        "attack":     stats.get("attack", 0),
        "defense":    stats.get("defense", 0),
        "sp_attack":  stats.get("special-attack", 0),
        "sp_defense": stats.get("special-defense", 0),
        "speed":      stats.get("speed", 0),
    }


def extract_types(data):
    types = sorted(data["types"], key=lambda t: t["slot"])
    type1 = TYPE_JP.get(types[0]["type"]["name"], types[0]["type"]["name"])
    type2 = TYPE_JP.get(types[1]["type"]["name"], types[1]["type"]["name"]) if len(types) > 1 else None
    return type1, type2


def fetch_pokemon_stats(pokeapi_name):
    url = f"{BASE_URL}/pokemon/{pokeapi_name}"
    return get_json(url)


def fetch_move(move_en_name):
    url = f"{BASE_URL}/move/{move_en_name}"
    return get_json(url)


def get_jp_name(names_list):
    for n in names_list:
        if n["language"]["name"] in ("ja-Hrkt", "ja"):
            return n["name"]
    return None


def create_tables(con):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS pokemon_base_stats (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_name TEXT NOT NULL,
        dex_number   INTEGER NOT NULL,
        form_index   INTEGER NOT NULL DEFAULT 0,
        pokeapi_name TEXT,
        type1        TEXT NOT NULL,
        type2        TEXT,
        hp           INTEGER NOT NULL,
        attack       INTEGER NOT NULL,
        defense      INTEGER NOT NULL,
        sp_attack    INTEGER NOT NULL,
        sp_defense   INTEGER NOT NULL,
        speed        INTEGER NOT NULL,
        UNIQUE(dex_number, form_index)
    );

    CREATE TABLE IF NOT EXISTS pokemon_mega_stats (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        mega_name_jp    TEXT NOT NULL UNIQUE,
        base_pokemon_jp TEXT NOT NULL,
        mega_stone      TEXT NOT NULL,
        base_dex        INTEGER NOT NULL,
        pokeapi_name    TEXT,
        type1           TEXT NOT NULL,
        type2           TEXT,
        hp              INTEGER NOT NULL,
        attack          INTEGER NOT NULL,
        defense         INTEGER NOT NULL,
        sp_attack       INTEGER NOT NULL,
        sp_defense      INTEGER NOT NULL,
        speed           INTEGER NOT NULL,
        ability         TEXT
    );

    CREATE TABLE IF NOT EXISTS move_master (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name_jp     TEXT NOT NULL UNIQUE,
        name_en     TEXT,
        type        TEXT NOT NULL,
        category    TEXT NOT NULL,
        power       INTEGER,
        accuracy    INTEGER,
        priority    INTEGER NOT NULL DEFAULT 0,
        pp          INTEGER,
        effect_id   INTEGER
    );
    """)
    con.commit()


def fetch_all_base_stats(con):
    print("=== ポケモン種族値を取得 ===")
    cur = con.cursor()

    # pokemon_idありのポケモン
    rows = cur.execute("""
        SELECT DISTINCT pokemon, pokemon_id FROM pokemon_usage
        WHERE rule='single' AND pokemon_id IS NOT NULL AND pokemon_id != ''
    """).fetchall()

    # pokemon_idなしのフォームを追加
    form_targets = []
    for jp_name, (dex, api_name) in FORM_OVERRIDES.items():
        form_targets.append((jp_name, dex, api_name))

    def process_row(pokemon_name, dex, form, api_name):
        existing = cur.execute(
            "SELECT 1 FROM pokemon_base_stats WHERE dex_number=? AND form_index=?",
            (dex, form)
        ).fetchone()
        if existing:
            return None, "skip"

        data = fetch_pokemon_stats(api_name)
        if not data:
            return pokemon_name, "error"

        s = extract_stats(data)
        t1, t2 = extract_types(data)
        return (pokemon_name, dex, form, api_name, t1, t2,
                s["hp"], s["attack"], s["defense"],
                s["sp_attack"], s["sp_defense"], s["speed"]), "ok"

    targets = []
    seen_dex_form = set()
    for pname, pid in rows:
        dex, form = parse_pokemon_id(pid)
        if dex is None:
            continue
        if (dex, form) in seen_dex_form:
            continue
        seen_dex_form.add((dex, form))
        targets.append((pname, dex, form, f"{dex}"))

    for jp_name, dex, api_name in form_targets:
        form = 99  # フォームオーバーライドは仮のform_index
        if (dex, form) not in seen_dex_form:
            seen_dex_form.add((dex, form))
            targets.append((jp_name, dex, form, api_name))

    print(f"対象: {len(targets)}匹")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(fetch_pokemon_stats, api_name): (pname, dex, form, api_name)
            for pname, dex, form, api_name in targets
        }
        ok = err = skip = 0
        for future in as_completed(futures):
            pname, dex, form, api_name = futures[future]
            try:
                data = future.result()
            except Exception as e:
                print(f"  ERR {pname}: {e}")
                err += 1
                continue

            if data is None:
                print(f"  404 {pname} ({api_name})")
                err += 1
                continue

            s = extract_stats(data)
            t1, t2 = extract_types(data)
            try:
                con.execute("""
                    INSERT OR IGNORE INTO pokemon_base_stats
                    (pokemon_name, dex_number, form_index, pokeapi_name,
                     type1, type2, hp, attack, defense, sp_attack, sp_defense, speed)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """, (pname, dex, form, api_name,
                      t1, t2, s["hp"], s["attack"], s["defense"],
                      s["sp_attack"], s["sp_defense"], s["speed"]))
                ok += 1
            except Exception as e:
                print(f"  DB ERR {pname}: {e}")
                err += 1

    con.commit()
    print(f"  取得: {ok}匹, エラー: {err}匹")


def fetch_all_mega_stats(con):
    print("=== メガ進化種族値を取得 ===")

    # ベースポケモンのJP名を逆引きするためにDBを使う
    cur = con.cursor()
    mega_stone_to_base = {}
    for stone, (dex, *_) in MEGA_STONE_MAP.items():
        row = cur.execute(
            "SELECT pokemon_name FROM pokemon_base_stats WHERE dex_number=? LIMIT 1", (dex,)
        ).fetchone()
        mega_stone_to_base[stone] = row[0] if row else f"dex{dex}"

    targets = [(stone, dex, api_name, mega_jp)
               for stone, (dex, api_name, mega_jp) in MEGA_STONE_MAP.items()
               if api_name is not None]

    print(f"PokeAPIで取得: {len(targets)}件, Champions独自(スキップ): "
          f"{sum(1 for _,_,a,_ in [(s,d,a,j) for s,(d,a,j) in MEGA_STONE_MAP.items()] if a is None)}件")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(fetch_pokemon_stats, api_name): (stone, dex, api_name, mega_jp)
            for stone, dex, api_name, mega_jp in targets
        }
        ok = err = 0
        for future in as_completed(futures):
            stone, dex, api_name, mega_jp = futures[future]
            try:
                data = future.result()
            except Exception as e:
                print(f"  ERR {mega_jp}: {e}")
                err += 1
                continue

            if data is None:
                print(f"  404 {mega_jp} ({api_name})")
                err += 1
                continue

            s = extract_stats(data)
            t1, t2 = extract_types(data)

            ability = None
            if data.get("abilities"):
                ab = next((a for a in data["abilities"] if not a["is_hidden"]), data["abilities"][0])
                ability = ab["ability"]["name"]

            base_jp = mega_stone_to_base.get(stone, "")
            try:
                con.execute("""
                    INSERT OR REPLACE INTO pokemon_mega_stats
                    (mega_name_jp, base_pokemon_jp, mega_stone, base_dex, pokeapi_name,
                     type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, ability)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, (mega_jp, base_jp, stone, dex, api_name,
                      t1, t2, s["hp"], s["attack"], s["defense"],
                      s["sp_attack"], s["sp_defense"], s["speed"], ability))
                ok += 1
            except Exception as e:
                print(f"  DB ERR {mega_jp}: {e}")
                err += 1

    con.commit()
    print(f"  取得: {ok}件, エラー: {err}件")


def fetch_all_moves(con):
    print("=== 技データを取得 ===")
    cur = con.cursor()

    db_moves = set(r[0] for r in cur.execute(
        "SELECT DISTINCT move FROM pokemon_moves WHERE rule='single'"
    ).fetchall())
    print(f"DB内の技: {len(db_moves)}種")

    print("PokeAPI全技リスト取得中...")
    all_moves_data = get_json(f"{BASE_URL}/move?limit=2000")
    if not all_moves_data:
        print("ERROR: 技リスト取得失敗")
        return
    all_moves_en = [m["name"] for m in all_moves_data["results"]]
    print(f"PokeAPI全技: {len(all_moves_en)}種")

    def fetch_and_match(move_en):
        data = fetch_move(move_en)
        if not data:
            return None
        jp_name = get_jp_name(data.get("names", []))
        if jp_name not in db_moves:
            return None
        damage_class = data.get("damage_class", {}).get("name", "status")
        move_type = TYPE_JP.get(
            data.get("type", {}).get("name", ""), data.get("type", {}).get("name", "")
        )
        return {
            "name_jp":  jp_name,
            "name_en":  move_en,
            "type":     move_type,
            "category": damage_class,
            "power":    data.get("power"),
            "accuracy": data.get("accuracy"),
            "priority": data.get("priority", 0),
            "pp":       data.get("pp"),
            "effect_id": data["id"],
        }

    found = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(fetch_and_match, en): en for en in all_moves_en}
        for i, future in enumerate(as_completed(futures), 1):
            if i % 100 == 0:
                print(f"  進捗: {i}/{len(all_moves_en)} (マッチ済み: {found})")
            result = future.result()
            if result is None:
                continue
            try:
                con.execute("""
                    INSERT OR IGNORE INTO move_master
                    (name_jp, name_en, type, category, power, accuracy, priority, pp, effect_id)
                    VALUES (:name_jp,:name_en,:type,:category,:power,:accuracy,:priority,:pp,:effect_id)
                """, result)
                found += 1
            except Exception as e:
                print(f"  DB ERR {result.get('name_jp')}: {e}")

    con.commit()
    missing = db_moves - set(
        r[0] for r in cur.execute("SELECT name_jp FROM move_master").fetchall()
    )
    print(f"  マッチ: {found}種")
    if missing:
        print(f"  未マッチ({len(missing)}種): {sorted(missing)[:20]}")


def main():
    con = sqlite3.connect(DB_PATH)
    create_tables(con)
    fetch_all_base_stats(con)
    fetch_all_mega_stats(con)
    fetch_all_moves(con)
    con.close()
    print("=== 完了 ===")


if __name__ == "__main__":
    main()
