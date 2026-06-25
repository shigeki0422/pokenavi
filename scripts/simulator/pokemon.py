"""
実戦に出るポケモンインスタンス（HP・ステータス・状態管理）
"""
import copy
import math
import random
from dataclasses import dataclass, field
from typing import Optional, List
from .data import PokemonTemplate, MoveData, MegaData, NATURE_MODS, DataLoader

STAT_STAGE_MULT = {
    -6: 2/8, -5: 2/7, -4: 2/6, -3: 2/5, -2: 2/4, -1: 2/3,
     0: 1.0,
     1: 3/2,  2: 4/2,  3: 5/2,  4: 6/2,  5: 7/2,  6: 8/2,
}
ACC_EVA_STAGE = {
    -6: 3/9, -5: 3/8, -4: 3/7, -3: 3/6, -2: 3/5, -1: 3/4,
     0: 1.0,
     1: 4/3,  2: 5/3,  3: 6/3,  4: 7/3,  5: 8/3,  6: 9/3,
}


def calc_stat(base: int, ev: int, iv: int, nature_mod: float, level: int = 50) -> int:
    return math.floor((math.floor((base * 2 + iv + ev * 2) * level / 100) + 5) * nature_mod)


def calc_hp(base: int, ev: int, iv: int = 31, level: int = 50) -> int:
    return math.floor((base * 2 + iv + ev * 2) * level / 100) + level + 10


@dataclass
class BattlePokemon:
    """バトル中のポケモン状態"""
    name: str
    dex: int
    type1: str
    type2: Optional[str]

    # 実数値
    max_hp: int
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

    # 採用技 (MoveData or None)
    moves: List[Optional[MoveData]] = field(default_factory=list)
    pp: List[int] = field(default_factory=list)

    # 元タイプ（交代時リセット用）
    base_type1: str = ""
    base_type2: Optional[str] = None

    # 持ち物・特性
    item: Optional[str] = None
    ability: str = ""

    # 能力変化ランク
    stage_attack: int = 0
    stage_defense: int = 0
    stage_sp_attack: int = 0
    stage_sp_defense: int = 0
    stage_speed: int = 0
    stage_accuracy: int = 0
    stage_evasion: int = 0

    # 状態異常
    status: Optional[str] = None        # burn/paralysis/sleep/freeze/poison/badpoison
    bad_poison_count: int = 0           # どくどくのカウント
    sleep_count: int = 0                # ねむりのターン数
    confused: bool = False
    flinched: bool = False

    # 性格・努力値（ログ表示用）
    nature: str = ""
    evs: dict = field(default_factory=dict)

    # バトル中フラグ
    is_alive: bool = True
    mega_evolved: bool = False
    mega_data: Optional[MegaData] = None
    hero_forme: bool = False

    # 保護系
    protecting: bool = False
    protect_consecutive: int = 0        # 連続まもる成功回数（成功率 (1/3)^n）
    enduring: bool = False              # こらえる：このターンKO級ダメージでもHP1で耐える
    ate_berry: bool = False             # ゲップ：戦闘中にきのみを食べたか
    used_moves: set = field(default_factory=set)  # とっておき：使用済み技名
    grounded: bool = False              # うちおとす：接地状態（ひこう/ふゆう/でんじふゆうのじめん無効を解除）
    syrup_count: int = 0                # あめまみれ：残りターン（素早さ低下）
    heal_block_count: int = 0           # かいふくふうじ：残りターン（回復不可）
    _deka_last: bool = False            # デカハンマー：直前にデカハンマーを使ったか

    # ちょっかい系
    locked_move: Optional[str] = None   # アンコール縛り
    choice_locked_move: Optional[str] = None  # こだわりアイテム縛り
    disabled_move: Optional[str] = None  # のろわれボディ等による封じ
    disabled_turns: int = 0              # 封じの残りターン
    lock_count: int = 0                 # あばれる等の連続ターン
    recharge: bool = False              # りゅうせいぐん等の反動ターン
    charging_move: Optional[str] = None  # ソーラービーム等の溜めターン管理

    # フィールド状態
    seeded: bool = False                # やどりぎのタネ
    yawn_count: int = 0                 # あくびカウント(1=次ターンねむり)
    encore_count: int = 0              # アンコール残りターン
    taunt_count: int = 0               # ちょうはつ残りターン
    bound_count: int = 0               # バインド残りターン（4-5ターン）
    throat_chop_count: int = 0         # じごくづき残りターン（2ターン、音技封じ）
    stockpile_count: int = 0           # たくわえる回数（最大3、のみこむ/はきだすで消費）
    infatuation: bool = False          # メロメロ状態
    torment: bool = False              # いちゃもん（連続同技不可）
    trapped: bool = False              # にげられない（くろいまなざし等）
    times_hit: int = 0                 # 場に出てから攻撃技で受けた回数（ふんどのこぶし用）
    ability_suppressed: bool = False   # とくせいなし（いえき）
    rooted: bool = False               # ねをはる
    aqua_ring: bool = False            # アクアリング
    magnet_rise: bool = False          # でんじふゆう
    lock_on: bool = False              # ロックオン（次ターン必中）
    _move_failed_last: bool = False    # 前ターン技失敗（じだんだ/やけっぱち威力2倍用）
    minimized: bool = False            # ちいさくなる状態（のしかかり等で被弾2倍）
    last_used_move: Optional[str] = None  # ふいうち判定用・アンコール用

    # 場に出たターン
    turns_out: int = 0

    # 味方の累計倒れ数（おはかまいり・そうだいしょう用）
    fainted_allies: int = 0

    # 特殊状態フラグ
    perish_count: int = 0            # ほろびのうた（3→2→1→0で倒れる）
    destiny_bond: bool = False       # みちづれ
    cursed: bool = False             # のろい（ゴーストが呪いをかけた）
    charged: bool = False            # じゅうでん（次の電気技×2）
    crit_stage: int = 0              # きあいだめ等による急所ランク加算

    def __deepcopy__(self, memo):
        """高速クローン: 可変コンテナ(list/dict/set)だけ複製し、不変(スカラ/文字列/
        MoveData/MegaData)は共有。スカラは再代入で更新されるためクローン間で独立。
        汎用なので可変フィールドの列挙漏れによる共有バグが起きない。"""
        new = self.__class__.__new__(self.__class__)
        memo[id(self)] = new
        nd = new.__dict__
        for k, v in self.__dict__.items():
            nd[k] = copy.deepcopy(v, memo) if type(v) in (list, dict, set) else v
        return new

    def get_effective_stat(self, stat_name: str) -> int:
        base = getattr(self, stat_name)
        stage = getattr(self, f"stage_{stat_name}", 0)
        return max(1, math.floor(base * STAT_STAGE_MULT[max(-6, min(6, stage))]))

    def get_effective_speed(self) -> int:
        spd = self.get_effective_stat("speed")
        if self.status == "paralysis" and self.ability != "はやあし":
            spd = math.floor(spd * 0.5)
        if self.syrup_count > 0:
            spd = math.floor(spd * 0.5)
        return spd

    def apply_status(self, status: str, corrosion: bool = False) -> bool:
        """状態異常を付与。成功でTrue。corrosion=True（ふしょく）ははがね/どくの毒免疫を貫通。"""
        if self.status is not None:
            return False
        # 特性による状態異常免疫
        _ab = self.ability
        if _ab == "きよめのしお":
            return False  # 全状態異常にならない
        if _ab == "じゅうなん" and status == "paralysis":
            return False
        if _ab == "めんえき" and status in ("poison", "badpoison"):
            return False
        if _ab == "マグマのよろい" and status == "freeze":
            return False
        if _ab == "すいほう" and status == "burn":
            return False
        if _ab in ("ふみん", "やるき", "スイートベール") and status == "sleep":
            return False
        if status == "burn" and "ほのお" in (self.type1, self.type2):
            return False
        if status in ("poison", "badpoison") and not corrosion and (
            "どく" in (self.type1, self.type2) or "はがね" in (self.type1, self.type2)
        ):
            return False
        if status == "paralysis" and "でんき" in (self.type1, self.type2):
            return False
        if status in ("freeze",) and "こおり" in (self.type1, self.type2):
            return False
        self.status = status
        return True

    def end_of_turn_damage(self) -> int:
        """ターン終了時のダメージ（毒・やけど・たべのこし等）。正=ダメ、負=回復"""
        if self.ability == "マジックガード":
            return 0
        dmg = 0
        if self.status == "burn":
            _burn = max(1, self.max_hp // 16)
            if self.ability == "たいねつ":
                _burn = max(1, _burn // 2)
            dmg += _burn
        elif self.status in ("poison", "badpoison"):
            if self.ability == "ポイズンヒール":
                return -(max(1, self.max_hp // 8))
            if self.status == "poison":
                dmg += max(1, self.max_hp // 8)
            else:
                self.bad_poison_count += 1
                dmg += max(1, self.max_hp * self.bad_poison_count // 16)

        if self.item == "たべのこし":
            dmg -= max(1, self.max_hp // 16)
        elif self.item == "くろいヘドロ" and "どく" in (self.type1, self.type2):
            dmg -= max(1, self.max_hp // 16)
        elif self.item == "くろいヘドロ":
            dmg += max(1, self.max_hp // 16)

        return dmg

    def do_mega_evolve(self):
        if self.mega_evolved or self.mega_data is None:
            return
        md = self.mega_data
        evs = getattr(self, 'evs', {}) or {}
        up, dn = NATURE_MODS.get(self.nature, (None, None))
        def nat(key):
            return 1.1 if up == key else (0.9 if dn == key else 1.0)

        hp_ratio = self.hp / self.max_hp
        self.max_hp = calc_hp(md.hp, evs.get('H', 0))
        self.hp = max(1, math.floor(self.max_hp * hp_ratio))
        self.attack     = calc_stat(md.attack,     evs.get('A', 0), 31, nat('attack'))
        self.defense    = calc_stat(md.defense,    evs.get('B', 0), 31, nat('defense'))
        self.sp_attack  = calc_stat(md.sp_attack,  evs.get('C', 0), 31, nat('sp_attack'))
        self.sp_defense = calc_stat(md.sp_defense, evs.get('D', 0), 31, nat('sp_defense'))
        self.speed      = calc_stat(md.speed,      evs.get('S', 0), 31, nat('speed'))
        self.type1 = md.type1
        self.type2 = md.type2
        self.base_type1 = md.type1   # メガ後タイプを基本タイプにも反映(交代時の型リセットで巻き戻らないように)
        self.base_type2 = md.type2
        if md.ability:
            self.ability = md.ability
        if getattr(md, "weight_kg", None):
            self.weight_kg = md.weight_kg
        # メガストーンはメガ進化後も持ち物として残る（実機仕様）。消去するとポルターガイストが
        # 「持ち物なし」で失敗する等の不整合。はたきおとす/トリック/なげつける等は _is_megastone で
        # メガストーンを保護済みなので剥奪・1.5倍補正は乗らない。効果アイテムでもないのでEOT効果も出ない。
        self.mega_evolved = True

    def take_damage(self, dmg: int):
        if self.enduring and dmg >= self.hp and self.hp > 0:
            self.hp = 1
            return
        self.hp = max(0, self.hp - dmg)
        if self.hp == 0:
            self.is_alive = False
            # タスキ処理はダメージ計算側で行う

    def __repr__(self):
        return f"{self.name}({self.hp}/{self.max_hp})"


def build_from_template(tpl: PokemonTemplate, loader: DataLoader,
                        randomize: bool = True,
                        override_item: Optional[str] = None,
                        override_nature: Optional[str] = None,
                        override_ability: Optional[str] = None,
                        override_evs: Optional[dict] = None,
                        override_moves: Optional[List[str]] = None) -> "BattlePokemon":
    """
    PokemonTemplateからBattlePokemonを生成。
    override_* が指定された場合はDBランダムより優先する。
    randomize=True: 使用率を確率として型を確率的にサンプリング
    randomize=False: 使用率1位の型を使用
    """
    def weighted_choice(items):
        if not items:
            return None
        if not randomize:
            return items[0][0]
        total = sum(r for _, r in items)
        if total == 0:
            return items[0][0]
        r = random.random() * total
        for name, rate in items:
            r -= rate
            if r <= 0:
                return name
        return items[-1][0]

    nature  = override_nature  if override_nature  is not None else (weighted_choice(tpl.top_natures) or "まじめ")
    item    = override_item    if override_item    is not None else weighted_choice(tpl.top_items)
    ability = override_ability if override_ability is not None else (weighted_choice(tpl.top_abilities) or "")

    # 努力値
    if override_evs is not None:
        ev_entry = override_evs
    else:
        ev_entry = weighted_choice([(ev, rate) for ev, rate in tpl.top_evs]) if tpl.top_evs else None
    if ev_entry is None:
        ev_entry = {"H": 0, "A": 0, "B": 0, "C": 0, "D": 0, "S": 0}

    # 性格補正
    nature_up, nature_dn = NATURE_MODS.get(nature, (None, None))
    def nat_mod(stat_key):
        if nature_up == stat_key:
            return 1.1
        if nature_dn == stat_key:
            return 0.9
        return 1.0

    max_hp     = calc_hp(tpl.base_hp, ev_entry.get("H", 0))
    atk_val    = calc_stat(tpl.base_attack,     ev_entry.get("A", 0), 31, nat_mod("attack"))
    def_val    = calc_stat(tpl.base_defense,    ev_entry.get("B", 0), 31, nat_mod("defense"))
    spatk_val  = calc_stat(tpl.base_sp_attack,  ev_entry.get("C", 0), 31, nat_mod("sp_attack"))
    spdef_val  = calc_stat(tpl.base_sp_defense, ev_entry.get("D", 0), 31, nat_mod("sp_defense"))
    speed_val  = calc_stat(tpl.base_speed,      ev_entry.get("S", 0), 31, nat_mod("speed"))

    # 技4枠
    if override_moves is not None:
        selected_moves = [loader.get_move(m) for m in override_moves]
        selected_moves = [m for m in selected_moves if m is not None]
    else:
        move_pool = list(tpl.top_moves)
        selected_moves = []
        for _ in range(min(4, len(move_pool))):
            total = sum(r for _, r in move_pool)
            if total == 0:
                break
            if not randomize:
                chosen = move_pool[0][0]
            else:
                r = random.random() * total
                chosen = move_pool[-1][0]
                for name, rate in move_pool:
                    r -= rate
                    if r <= 0:
                        chosen = name
                        break
            move_pool = [(n, r) for n, r in move_pool if n != chosen]
            selected_moves.append(loader.get_move(chosen))

    pp_list = [(m.pp or 5) for m in selected_moves]

    # メガデータをアイテムから解決（石名で引く。全角/半角X・Yを正規化）
    from .data import normalize_mega_stone
    mega_data = tpl.mega_data.get(normalize_mega_stone(item)) if item else None
    if mega_data is None and item:
        mega_data = tpl.mega_data.get(item)

    poke = BattlePokemon(
        name=tpl.name, dex=tpl.dex,
        type1=tpl.type1, type2=tpl.type2,
        base_type1=tpl.type1, base_type2=tpl.type2,
        max_hp=max_hp, hp=max_hp,
        attack=atk_val, defense=def_val,
        sp_attack=spatk_val, sp_defense=spdef_val, speed=speed_val,
        moves=selected_moves, pp=pp_list,
        item=item, ability=ability,
        nature=nature,
        evs=ev_entry,
        mega_data=mega_data,
    )
    poke.weight_kg = tpl.weight_kg

    # はりきり補正（攻撃実数値に織り込む）
    if ability == "はりきり":
        poke.attack = math.floor(poke.attack * 1.5)

    return poke


def parse_pokemon_spec(spec_str: str) -> dict:
    """
    書式: ポケモン名[@持ち物][:性格][:技1|技2|技3|技4][:H/A/B/C/D/S]
    省略フィールドは None（DBランダム）。
    例:
      ガブリアス
      ガブリアス@ガブリアスナイト
      ガブリアス@ガブリアスナイト:いじっぱり
      ガブリアス@ガブリアスナイト:いじっぱり:じしん|げきりん|ステルスロック|がんせきふうじ
      ガブリアス@ガブリアスナイト:いじっぱり:じしん|げきりん|ステルスロック|がんせきふうじ:2/32/0/0/0/32
    """
    spec_str = spec_str.strip()

    # 持ち物を @ で分離
    item = None
    if "@" in spec_str:
        spec_str, item_part = spec_str.split("@", 1)
        item = item_part.split(":")[0].strip() or None
        rest = item_part[len(item or ""):]
        spec_str = spec_str + rest

    parts = spec_str.split(":")
    name = parts[0].strip()

    nature = None
    moves = None
    evs = None

    if len(parts) >= 2 and parts[1].strip():
        nature = parts[1].strip()

    if len(parts) >= 3 and parts[2].strip():
        raw = parts[2].strip()
        moves = [m.strip() for m in raw.split("|") if m.strip()]

    ability = None

    if len(parts) >= 4 and parts[3].strip():
        raw = parts[3].strip()
        vals = [int(v) for v in raw.split("/")]
        keys = ["H", "A", "B", "C", "D", "S"]
        evs = {k: vals[i] if i < len(vals) else 0 for i, k in enumerate(keys)}

    if len(parts) >= 5 and parts[4].strip():
        ability = parts[4].strip()

    return {
        "name": name,
        "item": item,
        "nature": nature,
        "moves": moves,
        "evs": evs,
        "ability": ability,
    }


def build_from_spec(spec: dict, loader: "DataLoader",
                    season: str = "M-2", randomize: bool = True) -> "BattlePokemon":
    """parse_pokemon_spec の結果から BattlePokemon を生成"""
    tpl = loader.get_pokemon_template(spec["name"], season)
    if tpl is None:
        raise ValueError(f"ポケモン '{spec['name']}' が見つかりません (season={season})")
    return build_from_template(
        tpl, loader, randomize=randomize,
        override_item=spec.get("item"),
        override_nature=spec.get("nature"),
        override_ability=spec.get("ability"),
        override_evs=spec.get("evs"),
        override_moves=spec.get("moves"),
    )
