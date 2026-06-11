"""
DBからポケモン・技データを読み込むデータアクセス層
"""
import sqlite3
from dataclasses import dataclass, field
from typing import Optional

DB_PATH = "/Users/shigeki/work/pokenavi/scripts/pokenavi.db"

# 性格補正テーブル: 上げる/(下げる) → (上昇ステータス, 低下ステータス)
NATURE_MODS = {
    "いじっぱり": ("attack",     "sp_attack"),
    "ゆうかん":   ("attack",     "speed"),
    "やんちゃ":   ("attack",     "sp_defense"),
    "さみしがり": ("attack",     "defense"),
    "わんぱく":   ("defense",    "sp_attack"),
    "のうてんき": ("defense",    "sp_defense"),
    "のんき":     ("defense",    "speed"),
    "ずぶとい":   ("defense",    "attack"),
    "おくびょう": ("speed",      "attack"),
    "せっかち":   ("speed",      "defense"),
    "ようき":     ("speed",      "sp_attack"),
    "むじゃき":   ("speed",      "sp_defense"),
    "ひかえめ":   ("sp_attack",  "attack"),
    "おっとり":   ("sp_attack",  "defense"),
    "うっかりや": ("sp_attack",  "sp_defense"),
    "れいせい":   ("sp_attack",  "speed"),
    "おだやか":   ("sp_defense", "attack"),
    "おとなしい": ("sp_defense", "defense"),
    "しんちょう": ("sp_defense", "sp_attack"),
    "なまいき":   ("sp_defense", "speed"),
}
# 注: 五性(まじめ等)は補正なし

# タイプ相性表: TYPE_CHART[攻撃タイプ][防御タイプ] = 倍率
_types = ["ノーマル","かくとう","ひこう","どく","じめん","いわ","むし","ゴースト",
          "はがね","ほのお","みず","くさ","でんき","エスパー","こおり","ドラゴン","あく","フェアリー"]

# 0=無効, 0.5=半減, 1=等倍, 2=弱点
_chart_raw = {
    "ノーマル":  {"ゴースト":0, "はがね":0.5, "いわ":0.5},
    "かくとう":  {"ノーマル":2,"いわ":2,"はがね":2,"こおり":2,"あく":2,
                  "どく":0.5,"むし":0.5,"ひこう":0.5,"エスパー":0.5,"フェアリー":0.5,"ゴースト":0},
    "ひこう":    {"かくとう":2,"むし":2,"くさ":2,"いわ":0.5,"はがね":0.5,"でんき":0.5},
    "どく":      {"くさ":2,"フェアリー":2,"どく":0.5,"じめん":0.5,"いわ":0.5,"ゴースト":0.5,"はがね":0},
    "じめん":    {"どく":2,"いわ":2,"はがね":2,"ほのお":2,"でんき":2,
                  "むし":0.5,"くさ":0.5,"ひこう":0},
    "いわ":      {"ひこう":2,"むし":2,"ほのお":2,"こおり":2,
                  "かくとう":0.5,"じめん":0.5,"はがね":0.5},
    "むし":      {"くさ":2,"エスパー":2,"あく":2,
                  "かくとう":0.5,"ひこう":0.5,"どく":0.5,"ゴースト":0.5,"はがね":0.5,"ほのお":0.5,"フェアリー":0.5},
    "ゴースト":  {"ゴースト":2,"エスパー":2,"ノーマル":0,"あく":0.5},
    "はがね":    {"こおり":2,"いわ":2,"フェアリー":2,
                  "ほのお":0.5,"みず":0.5,"でんき":0.5,"はがね":0.5},
    "ほのお":    {"むし":2,"くさ":2,"こおり":2,"はがね":2,
                  "ほのお":0.5,"みず":0.5,"いわ":0.5,"ドラゴン":0.5},
    "みず":      {"ほのお":2,"じめん":2,"いわ":2,
                  "みず":0.5,"くさ":0.5,"ドラゴン":0.5},
    "くさ":      {"みず":2,"じめん":2,"いわ":2,
                  "ひこう":0.5,"どく":0.5,"むし":0.5,"はがね":0.5,"ほのお":0.5,"くさ":0.5,"ドラゴン":0.5},
    "でんき":    {"みず":2,"ひこう":2,"でんき":0.5,"くさ":0.5,"ドラゴン":0.5,"じめん":0},
    "エスパー":  {"かくとう":2,"どく":2,"エスパー":0.5,"はがね":0.5,"あく":0},
    "こおり":    {"ひこう":2,"じめん":2,"くさ":2,"ドラゴン":2,
                  "みず":0.5,"こおり":0.5,"はがね":0.5,"ほのお":0.5},
    "ドラゴン":  {"ドラゴン":2,"はがね":0.5,"フェアリー":0},
    "あく":      {"ゴースト":2,"エスパー":2,"かくとう":0.5,"あく":0.5,"フェアリー":0.5},
    "フェアリー":{"かくとう":2,"ドラゴン":2,"あく":2,"どく":0.5,"はがね":0.5,"ほのお":0.5},
}

def get_type_effectiveness(atk_type: str, def_type1: str, def_type2: Optional[str]) -> float:
    chart = _chart_raw.get(atk_type, {})
    e1 = chart.get(def_type1, 1.0)
    e2 = chart.get(def_type2, 1.0) if def_type2 else 1.0
    return e1 * e2


@dataclass
class MoveData:
    name_jp: str
    name_en: str
    type: str
    category: str      # physical / special / status
    power: Optional[int]
    accuracy: Optional[int]
    priority: int
    pp: Optional[int]
    effect_id: Optional[int]

    def __deepcopy__(self, memo):
        return self  # 不変な技定義は共有（MCTSクローンのdeepcopyを省き大幅高速化）


@dataclass
class PokemonTemplate:
    """DBから取得したポケモンの雛形（実戦に出す前のテンプレート）"""
    name: str
    dex: int
    type1: str
    type2: Optional[str]
    base_hp: int
    base_attack: int
    base_defense: int
    base_sp_attack: int
    base_sp_defense: int
    base_speed: int
    # 採用率上位の型
    top_moves: list       # [(move_name, usage_rate), ...]
    top_items: list       # [(item_name, usage_rate), ...]
    top_abilities: list   # [(ability_name, usage_rate), ...]
    top_natures: list     # [(nature_name, usage_rate), ...]
    top_evs: list         # [(ev_dict, usage_rate), ...]  ev_dict has "spread" key
    # メガ情報: {石名: MegaData}（複数石対応、石なし=空dict）
    mega_data: dict = field(default_factory=dict)
    weight_kg: float = 50.0


@dataclass
class MegaData:
    mega_name: str
    type1: str
    type2: Optional[str]
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    ability: Optional[str]
    mega_stone: str
    weight_kg: Optional[float] = None

    def __deepcopy__(self, memo):
        return self  # 不変なメガ定義は共有（MCTSクローン高速化）


def normalize_mega_stone(name: Optional[str]) -> Optional[str]:
    """メガ石名の全角Ｘ/Ｙを半角X/Yに統一（リザードナイトＸ↔X 等の表記ゆれ吸収）。"""
    if not name:
        return name
    return name.replace("Ｘ", "X").replace("Ｙ", "Y")


class DataLoader:
    def __init__(self, db_path=DB_PATH):
        self.con = sqlite3.connect(db_path, check_same_thread=False)
        self.con.row_factory = sqlite3.Row
        self._move_cache: dict[str, MoveData] = {}

    def get_move(self, name_jp: str) -> Optional[MoveData]:
        if name_jp in self._move_cache:
            return self._move_cache[name_jp]
        row = self.con.execute(
            "SELECT * FROM move_master WHERE name_jp=?", (name_jp,)
        ).fetchone()
        if not row:
            return None
        m = MoveData(
            name_jp=row["name_jp"], name_en=row["name_en"],
            type=row["type"], category=row["category"],
            power=row["power"], accuracy=row["accuracy"],
            priority=row["priority"], pp=row["pp"],
            effect_id=row["effect_id"],
        )
        self._move_cache[name_jp] = m
        return m

    # 使用率DB名 → base_stats格納名 のエイリアス（接頭辞ルールで拾えない表記違い）
    FORM_ALIASES = {
        "フラエッテ:永遠": "フラエッテ(永遠)",
        "パルデアケンタロス(炎)": "ケンタロス:炎",
        "パルデアケンタロス(水)": "ケンタロス:水",
        "パルデアケンタロス(闘)": "ケンタロス:格",
        # ルガルガン：使用率名 → 正しい種族値を持つ行（PokeAPI照合で確定）
        "ルガルガン(黄昏)": "ルガルガン(たそがれ)",
        "ルガルガン(まひる)": "ルガルガン(昼)",
        "ルガルガン(まよなか)": "ルガルガン(夜)",
    }

    def get_pokemon_template(self, pokemon_name: str, season: str = "M-2") -> Optional[PokemonTemplate]:
        # スペースあり括弧 → スペースなし括弧に正規化
        pokemon_name = pokemon_name.replace(" (", "(")
        # フォルム名エイリアス（接頭辞ルール外の表記違いを明示変換）
        pokemon_name = self.FORM_ALIASES.get(pokemon_name, pokemon_name)

        # リージョン括弧表記 → 接頭語表記に変換して正しい種族値を取得
        base = None
        for prefix in ("ガラル", "アローラ", "ヒスイ", "パルデア"):
            if pokemon_name.endswith(f"({prefix})"):
                alt = f"{prefix}{pokemon_name[:-len(prefix)-2]}"
                base = self.con.execute(
                    "SELECT * FROM pokemon_base_stats WHERE pokemon_name=?", (alt,)
                ).fetchone()
                break

        if not base:
            base = self.con.execute("""
                SELECT * FROM pokemon_base_stats WHERE pokemon_name=?
            """, (pokemon_name,)).fetchone()

        # フォールバック: 部分一致（フォーム表記ゆれ対策）
        if not base:
            base = self.con.execute("""
                SELECT * FROM pokemon_base_stats WHERE pokemon_name LIKE ?
            """, (f"%{pokemon_name.split('(')[0]}%",)).fetchone()
        if not base:
            return None

        # 使用率DBのポケモン名を解決（スペースなし括弧 → スペースあり括弧 or 接頭語）
        usage_name = pokemon_name
        for prefix in ("ガラル", "アローラ", "ヒスイ", "パルデア"):
            if pokemon_name.endswith(f"({prefix})"):
                base_part = pokemon_name[:-len(prefix)-2]
                # スペースあり括弧表記で試行（moves/items等のDB形式）
                spaced = f"{base_part} ({prefix})"
                found = self.con.execute(
                    "SELECT 1 FROM pokemon_moves WHERE rule='single' AND pokemon=? LIMIT 1", (spaced,)
                ).fetchone()
                if found:
                    usage_name = spaced
                else:
                    # 接頭語表記で試行
                    prefixed = f"{prefix}{base_part}"
                    found2 = self.con.execute(
                        "SELECT 1 FROM pokemon_moves WHERE rule='single' AND pokemon=? LIMIT 1", (prefixed,)
                    ).fetchone()
                    if found2:
                        usage_name = prefixed
                break

        cd = f"(SELECT MAX(crawled_date) FROM pokemon_moves WHERE season=? AND rule='single' AND pokemon=?)"
        moves = self.con.execute(f"""
            SELECT move, usage_rate FROM pokemon_moves
            WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
            ORDER BY rank LIMIT 12
        """, (season, usage_name, season, usage_name)).fetchall()

        items = self.con.execute(f"""
            SELECT item, usage_rate FROM pokemon_items
            WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
            ORDER BY rank LIMIT 5
        """, (season, usage_name, season, usage_name)).fetchall()

        abilities = self.con.execute(f"""
            SELECT ability, usage_rate FROM pokemon_abilities
            WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
            ORDER BY rank LIMIT 3
        """, (season, usage_name, season, usage_name)).fetchall()

        natures = self.con.execute(f"""
            SELECT nature, usage_rate FROM pokemon_natures
            WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
            ORDER BY rank LIMIT 3
        """, (season, usage_name, season, usage_name)).fetchall()

        evs = self.con.execute(f"""
            SELECT ev_spread, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate FROM pokemon_evs
            WHERE season=? AND rule='single' AND pokemon=? AND crawled_date={cd}
            ORDER BY rank LIMIT 3
        """, (season, usage_name, season, usage_name)).fetchall()

        # アイテムプール内のメガ石を全て解決して辞書化
        mega_data_map: dict = {}
        for item_row in items:
            stone = item_row["item"]
            if "ナイト" not in stone:
                continue
            stone = normalize_mega_stone(stone)
            if stone in mega_data_map:
                continue
            mega_row = self.con.execute(
                "SELECT * FROM pokemon_mega_stats WHERE mega_stone=? OR mega_stone=?",
                (stone, item_row["item"])
            ).fetchone()
            if mega_row:
                mega_data_map[stone] = MegaData(
                    mega_name=mega_row["mega_name_jp"],
                    type1=mega_row["type1"], type2=mega_row["type2"],
                    hp=mega_row["hp"], attack=mega_row["attack"],
                    defense=mega_row["defense"], sp_attack=mega_row["sp_attack"],
                    sp_defense=mega_row["sp_defense"], speed=mega_row["speed"],
                    ability=mega_row["ability"], mega_stone=stone,
                    weight_kg=(mega_row["weight_kg"] if "weight_kg" in mega_row.keys() else None),
                )

        # 使用率に出ない自分のメガ石も解決（base_dex一致で全メガを利用可能に）
        for mrow in self.con.execute(
                "SELECT * FROM pokemon_mega_stats WHERE base_dex=?", (base["dex_number"],)).fetchall():
            st = normalize_mega_stone(mrow["mega_stone"])
            if st in mega_data_map:
                continue
            mega_data_map[st] = MegaData(
                mega_name=mrow["mega_name_jp"], type1=mrow["type1"], type2=mrow["type2"],
                hp=mrow["hp"], attack=mrow["attack"], defense=mrow["defense"],
                sp_attack=mrow["sp_attack"], sp_defense=mrow["sp_defense"], speed=mrow["speed"],
                ability=mrow["ability"], mega_stone=st,
                weight_kg=(mrow["weight_kg"] if "weight_kg" in mrow.keys() else None),
            )

        return PokemonTemplate(
            name=pokemon_name,
            dex=base["dex_number"],
            type1=base["type1"], type2=base["type2"],
            base_hp=base["hp"], base_attack=base["attack"],
            base_defense=base["defense"], base_sp_attack=base["sp_attack"],
            base_sp_defense=base["sp_defense"], base_speed=base["speed"],
            weight_kg=float(base["weight_kg"] or 50.0),
            top_moves=[(r["move"], r["usage_rate"]) for r in moves],
            top_items=[(r["item"], r["usage_rate"]) for r in items],
            top_abilities=[(r["ability"], r["usage_rate"]) for r in abilities],
            top_natures=[(r["nature"], r["usage_rate"]) for r in natures],
            top_evs=[({
                "H": r["ev_h"], "A": r["ev_a"], "B": r["ev_b"],
                "C": r["ev_c"], "D": r["ev_d"], "S": r["ev_s"],
                "spread": r["ev_spread"],
            }, r["usage_rate"]) for r in evs],
            mega_data=mega_data_map,
        )
