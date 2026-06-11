"""
ダメージ計算モジュール
SV/チャンピオンズ準拠のダメージ式
"""
import math
import random
import re
from typing import TYPE_CHECKING, Optional
from .data import get_type_effectiveness, MoveData


def _is_secondary_effect(eff: str) -> bool:
    """ちからずく(Sheer Force)が強化する「追加効果」を持つ技か。
    確率追加効果(の確率で…)・確定の相手能力ダウン・確定の自己能力アップが対象。
    自己能力ダウン(反動)・反動/ドレイン/条件威力のみの技は対象外。"""
    if not eff:
        return False
    if "の確率で" in eff:
        return True
    if re.search(r"相手の[^。]{0,8}を[1-3]段階下げる", eff):
        return True
    if re.search(r"自分の[^。]{0,8}を[1-3]段階上げる", eff):
        return True
    return False


_SECONDARY_MOVES = None
# 探索のロールアウト中だけ設定する固定ダメージロール（0.0=最低〜1.0=最高）。Noneで通常乱数。
_ROLL_OVERRIDE = None


def _secondary_effect_moves() -> set:
    """move_master.effect_text から追加効果を持つ技名集合を構築（初回のみDB参照・キャッシュ）。"""
    global _SECONDARY_MOVES
    if _SECONDARY_MOVES is None:
        import sqlite3
        from pathlib import Path
        db = Path(__file__).resolve().parent.parent / "pokenavi.db"
        s = set()
        try:
            con = sqlite3.connect(str(db))
            for n, eff in con.execute("SELECT name_jp, effect_text FROM move_master"):
                if _is_secondary_effect(eff or ""):
                    s.add(n)
            con.close()
        except Exception:
            pass
        _SECONDARY_MOVES = s
    return _SECONDARY_MOVES
from .pokemon import ACC_EVA_STAGE

if TYPE_CHECKING:
    from .pokemon import BattlePokemon
    from .battle import BattleField


SKIN_ABILITIES = {
    "フェアリースキン": "フェアリー",
    "フリーズスキン":   "こおり",
    "エレキスキン":     "でんき",
    "スカイスキン":     "ひこう",
    "ドラゴンスキン":   "ドラゴン",
}

BALL_BOMB_MOVES = {
    "きあいだま", "タネばくだん", "エレキボール", "エナジーボール",
    "フォーカスブラスト", "シャドーボール", "ヘドロばくだん", "ロックブラスト",
    "タマゴばくだん", "ウェザーボール", "アシッドボム", "アイスボール",
    "どろばくだん", "マグネットボム", "ポレンパフ", "ジャイロボール",
    "かふんだんご", "がんせきほう", "くちばしキャノン", "でんじほう",
    "はどうだん", "みずあめボム", "タネマシンガン",
}

SOUND_MOVES = {
    "むしのさざめき", "バークアウト", "ハイパーボイス",
    "なきごえ", "うたう", "ちょうおんぱ", "きんぞくおん",
    "ほえる", "スケイルノイズ", "すてゼリフ",
    "いびき", "いやしのすず", "いやなおと", "うたかたのアリア",
    "おたけび", "さわぐ", "とおぼえ", "ばくおんぱ",
    "ぶきみなじゅもん", "ほろびのうた", "みわくのボイス", "りんしょう",
    "サイコノイズ", "ソウルビート", "ドラゴンエール", "フレアソング",
}

PUNCH_MOVES = {"アームハンマー", "スカイアッパー", "アイスハンマー", "ぶちかまし"}

# DB上 power=NULL だがダメージ計算を経由しない技（battle.pyで直接処理）
BYPASS_DAMAGE_CALC = {
    "じわれ", "ぜったいれいど", "つのドリル", "ハサミギロチン",  # OHKO
    "カウンター", "ミラーコート", "メタルバースト",              # カウンター系
    "がむしゃら", "いかりのまえば", "ちきゅうなげ",              # 直接ダメ
    "いのちがけ",   # 相手HP-自分HPのダメージ
    "ナイトヘッド",  # Lv固定50ダメージ
    "はきだす",      # たくわえる回数依存
    "ふくろだたき",  # 味方数依存
}


def effective_weather(field, poke=None):
    """実効天候を返す。
    - メガソーラー持ちは常に "sunny"（ノーてんきより優先）。
    - 場にノーてんきがいる（field._weather_negated）なら天候効果なし（None）。
    - それ以外は実際の field.weather。
    天候依存の効果はすべてこの関数を経由して天候を取得する。
    """
    if poke is not None and getattr(poke, "ability", "") == "メガソーラー":
        return "sunny"
    if getattr(field, "_weather_negated", False):
        return None
    return field.weather


def _effective_move_type(attacker: "BattlePokemon", move: MoveData,
                         field: "BattleField") -> str:
    """スキン系特性・ウェザーボール・レイジングブルによるタイプ上書き"""
    t = move.type
    ab = attacker.ability
    if t == "ノーマル" and ab in SKIN_ABILITIES:
        return SKIN_ABILITIES[ab]
    # うるおいボイス: 音技がみずタイプになる
    if ab == "うるおいボイス" and move.name_jp in SOUND_MOVES:
        return "みず"
    if move.name_jp == "ウェザーボール":
        WEATHER_TYPE = {
            "sunny": "ほのお", "rain": "みず",
            "sandstorm": "いわ", "hail": "こおり",
        }
        eff_w = effective_weather(field, attacker) or ""
        return WEATHER_TYPE.get(eff_w, "ノーマル")
    if move.name_jp == "レイジングブル":
        # 使用者のtype2があればそのタイプ、なければtype1（かくとう）、どちらでもなければノーマル
        if attacker.type2:
            return attacker.type2
        if attacker.type1 == "かくとう":
            return "かくとう"
        return "ノーマル"
    if move.name_jp == "だいちのはどう":
        # 接地時、フィールドの種類でタイプが変わる
        grounded = not ("ひこう" in (attacker.type1, attacker.type2)
                        or ab == "ふゆう" or getattr(attacker, "magnet_rise", False))
        if grounded:
            if getattr(field, "grassy_terrain", False):
                return "くさ"
            if getattr(field, "electric_terrain", False):
                return "でんき"
            if getattr(field, "psychic_terrain", False):
                return "エスパー"
            if getattr(field, "misty_terrain", False):
                return "フェアリー"
    return t


def calc_damage(
    attacker: "BattlePokemon",
    defender: "BattlePokemon",
    move: MoveData,
    field: "BattleField",
    critical: bool = False,
    random_roll: Optional[float] = None,
) -> int:
    """
    ダメージ計算。戻り値はダメージ量。
    random_roll: None=乱数あり, 0.0~1.0=固定(0.0=最低, 1.0=最高)
    """
    from .abilities import (
        check_move_immunity, should_ignore_ability,
        get_pinch_multiplier, get_sharpness_multiplier, scrappy_override,
        MOLD_BREAKER_ABILITIES,
    )
    from .items import get_type_boost, get_crit_stage_bonus

    if move.category == "status":
        return 0

    # ノーてんき：場の天候無効化フラグを当事者から最新化（Battle外の直接呼び出しでも正しく判定）
    field._weather_negated = "ノーてんき" in (attacker.ability, defender.ability)

    level = 50
    eff_type = _effective_move_type(attacker, move, field)
    power = _effective_power(attacker, defender, move, field, eff_type)
    if not power:
        return 0

    # 無効チェック（ふゆう・もらいび等）
    # かたやぶり系は特性無視
    ignore_ab = should_ignore_ability(attacker)
    if not ignore_ab:
        if check_move_immunity(defender, eff_type, move.name_jp):
            # スクラッピー上書き
            if not scrappy_override(attacker, eff_type, defender):
                return 0
        # タイプ無効もここで弾く（ゴースト・ノーマル等）
    else:
        # かたやぶりでもタイプ無効は残る（ふゆうは無視できるが、どくタイプのノーマル無効は無視できない）
        pass

    # てんねん: 相手のランク変化を無視（自分のランク変化は有効、速度は無関係）
    # 攻撃側がてんねん → 相手の防御・特防ランク変化を無視
    # 防御側がてんねん → 相手の攻撃・特攻ランク変化を無視
    atk_ignores_def_stage = not ignore_ab and attacker.ability == "てんねん"
    def_ignores_atk_stage = not ignore_ab and defender.ability == "てんねん"

    # シェルアームズ：物理/特殊のうちダメージが大きくなる方を選ぶ
    _cat = move.category
    if move.name_jp == "シェルアームズ":
        _phys = attacker.get_effective_stat("attack") / max(1, defender.get_effective_stat("defense"))
        _spec = attacker.get_effective_stat("sp_attack") / max(1, defender.get_effective_stat("sp_defense"))
        _cat = "physical" if _phys > _spec else "special"

    # 攻撃・防御実数値
    if _cat == "physical":
        if def_ignores_atk_stage:
            atk = attacker.attack  # 攻撃側の攻撃ランク変化を無視
        elif critical:
            atk = max(attacker.get_effective_stat("attack"), attacker.attack)
        else:
            atk = attacker.get_effective_stat("attack")

        if atk_ignores_def_stage:
            dfs = defender.defense  # 防御側の防御ランク変化を無視
        elif critical:
            dfs = min(defender.get_effective_stat("defense"), defender.defense)
        else:
            dfs = defender.get_effective_stat("defense")
        # 雪: 氷タイプの防御×1.5
        if effective_weather(field, defender) == "hail" and "こおり" in (defender.type1, defender.type2):
            dfs = math.floor(dfs * 1.5)
    else:
        if def_ignores_atk_stage:
            atk = attacker.sp_attack  # 攻撃側の特攻ランク変化を無視
        elif critical:
            atk = max(attacker.get_effective_stat("sp_attack"), attacker.sp_attack)
        else:
            atk = attacker.get_effective_stat("sp_attack")

        if atk_ignores_def_stage:
            dfs = defender.sp_defense  # 防御側の特防ランク変化を無視
        elif critical:
            dfs = min(defender.get_effective_stat("sp_defense"), defender.sp_defense)
        else:
            dfs = defender.get_effective_stat("sp_defense")
        # 砂嵐: 岩タイプの特防×1.5
        if effective_weather(field, defender) == "sandstorm" and "いわ" in (defender.type1, defender.type2):
            dfs = math.floor(dfs * 1.5)

    # ボディプレス（自身のBをAとして使う）
    if move.name_jp == "ボディプレス":
        atk = attacker.get_effective_stat("defense") if not critical else max(
            attacker.get_effective_stat("defense"), attacker.defense)

    # イカサマ（相手のAを参照）
    if move.name_jp == "イカサマ":
        atk = defender.get_effective_stat("attack") if not critical else max(
            defender.get_effective_stat("attack"), defender.attack)

    # サイコショック / サイコブレイク / シークレットソード（特殊技だが相手のBで計算）
    if move.name_jp in ("サイコショック", "サイコブレイク", "シークレットソード"):
        dfs = defender.get_effective_stat("defense") if not critical else min(
            defender.get_effective_stat("defense"), defender.defense)

    # せいなるつるぎ / DDラリアット（相手の防御ランク変化を無視＝素の防御で計算）
    if move.name_jp in ("せいなるつるぎ", "DDラリアット"):
        dfs = defender.defense if not critical else min(defender.get_effective_stat("defense"), defender.defense)

    # ふしぎなうろこ（状態異常時、防御実数値が1.5倍。防御参照技＝物理・サイコショック系のみ。特殊技には効かない）
    _uses_defense = (_cat == "physical") or move.name_jp in (
        "サイコショック", "サイコブレイク", "シークレットソード", "せいなるつるぎ", "DDラリアット")
    if defender.ability == "ふしぎなうろこ" and defender.status is not None and _uses_defense:
        dfs = math.floor(dfs * 1.5)

    # ちからもち / ヨガパワー（物理攻撃×2）
    if move.category == "physical" and attacker.ability in ("ちからもち", "ヨガパワー"):
        atk = atk * 2

    # こんじょう（状態異常時 攻撃×1.5、やけどの攻撃半減も無効）
    if move.category == "physical" and attacker.ability == "こんじょう" and attacker.status is not None:
        atk = math.floor(atk * 1.5)

    # やけど補正（こんじょう持ち・からげんきは免除）
    if attacker.status == "burn" and move.category == "physical":
        if attacker.ability not in ("こんじょう",) and move.name_jp != "からげんき":
            atk = math.floor(atk * 0.5)

    # 基本ダメージ式
    dmg = math.floor(math.floor(math.floor(2 * level / 5 + 2) * power * atk / dfs) / 50) + 2

    # 急所（スナイパーは2.25倍）
    if critical:
        dmg = math.floor(dmg * (2.25 if attacker.ability == "スナイパー" else 1.5))

    # 天候補正（メガソーラー特性は常に晴れ扱い／ノーてんきは天候効果を無効化）
    eff_weather = effective_weather(field, attacker)
    if eff_weather == "sunny":
        if eff_type == "ほのお":
            dmg = math.floor(dmg * 1.5)
        elif eff_type == "みず":
            dmg = math.floor(dmg * 0.5)
    elif eff_weather == "rain":
        if eff_type == "みず":
            dmg = math.floor(dmg * 1.5)
        elif eff_type == "ほのお":
            dmg = math.floor(dmg * 0.5)

    # じゅうでん（電気技×2）
    if getattr(attacker, 'charged', False) and eff_type == "でんき":
        dmg = math.floor(dmg * 2.0)
        attacker.charged = False

    # フィールド威力補正（地に足がついているポケモンのみ）
    grounded = not ("ひこう" in (attacker.type1, attacker.type2) or attacker.ability == "ふゆう")
    if grounded:
        if field.electric_terrain and eff_type == "でんき":
            dmg = math.floor(dmg * 1.3)
        elif field.psychic_terrain and eff_type == "エスパー":
            dmg = math.floor(dmg * 1.3)
        elif field.misty_terrain and eff_type == "ドラゴン":
            dmg = math.floor(dmg * 0.5)
        elif getattr(field, "grassy_terrain", False) and eff_type == "くさ":
            dmg = math.floor(dmg * 1.3)
    # グラスフィールド：じしん/じならし/マグニチュードは威力半減（地に足の有無を問わない）
    if getattr(field, "grassy_terrain", False) and move.name_jp in ("じしん", "じならし", "マグニチュード"):
        dmg = math.floor(dmg * 0.5)

    # 乱数（_ROLL_OVERRIDE設定時は乱数指定なしの呼び出しを固定ロールに置換＝探索のリスク回避用）
    if random_roll is None and _ROLL_OVERRIDE is not None:
        random_roll = _ROLL_OVERRIDE
    if random_roll is None:
        roll = random.choice([85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]) / 100
    else:
        roll = 0.85 + random_roll * 0.15
    dmg = math.floor(dmg * roll)

    # タイプ一致補正（スキン系は元タイプ≠ノーマルになるので自然にSTABが付く）
    stab_type = eff_type
    if stab_type in (attacker.type1, attacker.type2):
        if attacker.ability == "てきおうりょく":
            dmg = math.floor(dmg * 2.0)
        else:
            dmg = math.floor(dmg * 1.5)
    # スキン系: ノーマル技をタイプ変換 → 1.2倍ボーナス
    if move.type == "ノーマル" and attacker.ability in SKIN_ABILITIES:
        dmg = math.floor(dmg * 1.2)
    # フェアリーオーラ: 場にいる間、全員のフェアリー技の威力1.33倍（攻撃側・防御側どちらが持っていても）
    if eff_type == "フェアリー" and "フェアリーオーラ" in (attacker.ability, defender.ability):
        dmg = math.floor(dmg * 1.33)

    # タイプ相性
    effectiveness = get_type_effectiveness(eff_type, defender.type1, defender.type2)
    # フライングプレス：かくとう×ひこうの複合相性（両タイプの相性を掛け合わせる）
    if move.name_jp == "フライングプレス":
        if effectiveness == 0:
            pass  # かくとうが無効なら複合も無効
        else:
            flying_eff = get_type_effectiveness("ひこう", defender.type1, defender.type2)
            effectiveness *= flying_eff
    # うちおとす接地中：じめん技がひこうタイプにも当たる（ひこうの無効を解除）
    if eff_type == "じめん" and getattr(defender, "grounded", False) and "ひこう" in (defender.type1, defender.type2):
        effectiveness = 1.0
        for t in (defender.type1, defender.type2):
            if t and t != "ひこう":
                effectiveness *= get_type_effectiveness(eff_type, t, None)
    # スクラッピー：ゴーストへのノーマル/かくとう
    if effectiveness == 0 and scrappy_override(attacker, eff_type, defender):
        effectiveness = 1.0
    # フリーズドライ：みずタイプに必ず効果バツグン（こおり→みずの0.5倍を上書き）
    if move.name_jp == "フリーズドライ" and "みず" in (defender.type1, defender.type2):
        effectiveness = max(effectiveness, 2.0)
    dmg = math.floor(dmg * effectiveness)
    if dmg == 0:
        return 0

    # 持ち物補正（攻撃側）。ぶきよう持ちは道具効果を発揮しない
    if attacker.ability != "ぶきよう":
        dmg = _apply_attacker_item(dmg, attacker, move, effectiveness)

    # 持ち物補正（防御側）
    if defender.ability != "ぶきよう":
        dmg = _apply_defender_item(dmg, defender, move, effectiveness)

    # 特性補正（攻撃側）
    dmg = _apply_attacker_ability(dmg, attacker, defender, move, field, critical, ignore_ab)

    # 特性補正（防御側）
    if not ignore_ab:
        dmg = _apply_defender_ability(dmg, attacker, defender, move, field)

    # 低HP時ブースト（もうか・げきりゅう・しんりょく）
    pinch = get_pinch_multiplier(attacker, move.type)
    if pinch > 1.0:
        dmg = math.floor(dmg * pinch)

    # きれあじ
    sharp = get_sharpness_multiplier(attacker, move.name_jp)
    if sharp > 1.0:
        dmg = math.floor(dmg * sharp)

    # タイプ強化アイテム（ぶきようは無効）
    type_boost = get_type_boost(attacker.item, move.type, attacker.name) if attacker.ability != "ぶきよう" else 1.0
    if type_boost > 1.0:
        dmg = math.floor(dmg * type_boost)

    # もらいび発動中のほのお技強化
    if eff_type == "ほのお" and getattr(attacker, "_flash_fire_active", False):
        dmg = math.floor(dmg * 1.5)

    # でんきにかえるチャージ中のでんき技強化（使用後リセット）
    if eff_type == "でんき" and getattr(attacker, "_electromorphosis_charged", False):
        dmg = math.floor(dmg * 1.5)
        attacker._electromorphosis_charged = False  # type: ignore

    return max(1, dmg) if effectiveness > 0 else 0


_NON_CONTACT_PHYSICAL = {
    "じしん", "マグニチュード", "いわなだれ", "ストーンエッジ", "ロックブラスト",
    "がんせきふうじ",
    "どくびし", "まきびし", "ステルスロック", "ほのおのせんぷうき",
    "だいばくはつ", "じばく", "ボーンラッシュ",
    "ほねブーメラン", "しっぽをふる", "すなかけ",
    "3ぼんのや", "タネマシンガン",
    "うちおとす", "おはかまいり", "かげぬい",
    "がんせきほう", "くちばしキャノン", "こおりのつぶて", "しおづけ",
    "じさくづき", "じならし", "たいあたり", "つららおとし", "つららばり",
    "ひょうざんおろし", "アクアカッター", "オーラぐるま", "サイコカッター",
    "スケイルショット", "スラッシュ", "タネばくだん", "ダストシュート",
    "デカハンマー", "トリックフラワー", "ドラゴンアロー", "フェイント",
    "ポルターガイスト", "ミサイルばり", "Gのちから",
    "うっぷんばらし", "すなじごく", "だいふんげき", "はなふぶき",
    "ふくろだたき", "ゴッドバード",
    "じわれ", "なげつける", "メタルバースト",
}


_SPECIAL_CONTACT_MOVES = {
    "くさむすび", "まとわりつく", "はなびらのまい",
}


def is_contact_move(move) -> bool:
    """接触技かどうかを返す"""
    if move is None:
        return False
    name = move.name_jp or ""
    if name in _SPECIAL_CONTACT_MOVES:
        return True
    if move.category != "physical":
        return False
    return name not in _NON_CONTACT_PHYSICAL


def _eff_weight(poke) -> float:
    w = getattr(poke, 'weight_kg', 50.0)
    ab = getattr(poke, 'ability', '')
    if ab == "ヘヴィメタル":
        return w * 2
    if ab == "ライトメタル":
        return w * 0.5
    return w


def _weight_power(kg: float) -> int:
    if kg <= 10.0: return 20
    if kg <= 25.0: return 40
    if kg <= 50.0: return 60
    if kg <= 100.0: return 80
    if kg <= 200.0: return 100
    return 120


def _effective_power(attacker, defender, move, field, eff_type: str = "") -> int:
    power = move.power or 0
    if not eff_type:
        eff_type = move.type

    if move.name_jp == "おはかまいり":
        power = 50 + 50 * min(5, attacker.fainted_allies)
    elif move.name_jp == "ふんどのこぶし":
        power = 1 + (50 if attacker.status else 0)
    elif move.name_jp == "からげんき":
        power = 70 if not attacker.status else 140
    elif move.name_jp == "スケイルショット":
        power = 25
    elif move.name_jp in ("ダブルキック", "にどげり"):
        power = 30
    elif move.name_jp == "トリプルアクセル":
        power = 20 * (getattr(attacker, '_multi_hit_index', 0) + 1)
    elif move.name_jp == "はたきおとす":
        _it = defender.item
        _is_mega = _it is not None and (_it.endswith("ナイト")
                                        or _it.endswith("ナイトＸ") or _it.endswith("ナイトＹ"))
        if _it is not None and not _is_mega:
            power = math.floor(power * 1.5)
    elif move.name_jp == "たたりめ":
        if defender.status is not None:
            power = power * 2
    elif move.name_jp == "ひゃっきやこう":
        if defender.status is not None:
            power = power * 2
    elif move.name_jp == "ベノムショック":
        if defender.status in ("poison", "badpoison"):
            power = power * 2
    elif move.name_jp == "ライジングボルト":
        if field.electric_terrain and not ("ひこう" in (defender.type1, defender.type2)
                                            or defender.ability == "ふゆう"):
            power = power * 2
    elif move.name_jp == "しっぺがえし":
        if getattr(attacker, '_acts_second', False):
            power = power * 2
    elif move.name_jp == "アクロバット":
        if attacker.item is None:
            power = power * 2
    elif move.name_jp == "きまぐレーザー":
        if random.random() < 0.30:
            power = power * 2
    elif move.name_jp == "Gのちから":
        if getattr(field, "gravity", 0) > 0:
            power = math.floor(power * 1.5)
    elif move.name_jp == "ミストバースト":
        _grounded = not ("ひこう" in (attacker.type1, attacker.type2)
                         or attacker.ability == "ふゆう" or getattr(attacker, "magnet_rise", False))
        if getattr(field, "misty_terrain", False) and _grounded:
            power = math.floor(power * 1.5)
    elif move.name_jp == "ウェザーボール":
        power = 100 if effective_weather(field, attacker) else 50
    elif move.name_jp in ("くさむすび", "けたぐり"):
        power = _weight_power(_eff_weight(defender))
    elif move.name_jp in ("しおふき", "ふんか"):
        power = max(1, math.floor(150 * attacker.hp / attacker.max_hp))
    elif move.name_jp in ("アシストパワー", "つけあがる"):
        rank_sum = sum(max(0, getattr(attacker, s, 0))
                       for s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed"))
        power = 20 + 20 * rank_sum
    elif move.name_jp == "ダメおし":
        if getattr(attacker, '_acts_second', False):
            power = power * 2
    elif move.name_jp == "きしかいせい":
        ratio = attacker.hp / attacker.max_hp if attacker.max_hp > 0 else 1.0
        if ratio > 0.677:   power = 20
        elif ratio > 0.354: power = 40
        elif ratio > 0.208: power = 80
        elif ratio > 0.104: power = 100
        elif ratio > 0.031: power = 150
        else:               power = 200
    elif move.name_jp == "ジャイロボール":
        atk_spd = max(1, attacker.get_effective_speed())
        def_spd = max(1, defender.get_effective_speed())
        power = min(150, max(1, math.floor(25 * def_spd / atk_spd)))
    elif move.name_jp in ("ヒートスタンプ", "ヘビーボンバー"):
        w_atk = _eff_weight(attacker)
        w_def = _eff_weight(defender)
        ratio_w = w_atk / max(0.1, w_def)
        if ratio_w >= 5:   power = 120
        elif ratio_w >= 4: power = 100
        elif ratio_w >= 3: power = 80
        elif ratio_w >= 2: power = 60
        else:              power = 40
    elif move.name_jp == "じたばた":
        # 自分のHP比で威力変動（きしかいせいと同じ式）
        ratio = attacker.hp / attacker.max_hp if attacker.max_hp > 0 else 1.0
        if ratio > 0.677:   power = 20
        elif ratio > 0.354: power = 40
        elif ratio > 0.208: power = 80
        elif ratio > 0.104: power = 100
        elif ratio > 0.031: power = 150
        else:               power = 200
    elif move.name_jp == "ハードプレス":
        # 相手のHP比で威力変動（最大100）
        ratio = defender.hp / defender.max_hp if defender.max_hp > 0 else 1.0
        power = max(1, math.floor(100 * ratio))
    elif move.name_jp == "エレキボール":
        # 自分の素早さ/相手の素早さの比で威力変動（40-150）
        atk_spd = max(1, attacker.speed)
        def_spd = max(1, defender.speed)
        ratio_s = atk_spd / def_spd
        if ratio_s >= 4: power = 150
        elif ratio_s >= 3: power = 120
        elif ratio_s >= 2: power = 80
        elif ratio_s >= 1: power = 60
        else: power = 40
    # ちきゅうなげはbattle.pyでLv固定ダメとして処理（BYPASS_DAMAGE_CALC）
    elif move.name_jp == "なげつける":
        FLING_POWER: dict[str, int] = {
            "こだわりハチマキ": 130,
            "こだわりメガネ":    90, "こだわりスカーフ":  90,
            "ゴツゴツメット":    80, "くろおび":          80,
            "きあいのタスキ":    60, "じゅうなんチョッキ": 60,
            "いのちのたま":      30, "くろいヘドロ":       30,
            "メタルコート":      30, "シルクのスカーフ":   20,
            "たべのこし":        20, "どくバリ":           50,
        }
        flung_item = getattr(attacker, '_last_flung_item', None) or attacker.item
        power = FLING_POWER.get(flung_item or "", 10) if flung_item else 0

    # DB上 power=NULL で未処理のまま power=0 になった技を検出する安全網
    if move.power is None and power == 0 and move.name_jp not in BYPASS_DAMAGE_CALC:
        raise NotImplementedError(f"可変威力技 '{move.name_jp}' の威力計算が未実装")

    # ソーラービーム/ブレード：晴れ以外の天候は威力半減
    if move.name_jp in ("ソーラービーム", "ソーラーブレード"):
        if effective_weather(field, attacker) in ("rain", "hail", "sandstorm"):
            power = power // 2

    # じめん技 + ひこうタイプ（うちおとす接地中は無効化されない）
    if eff_type == "じめん":
        if "ひこう" in (defender.type1, defender.type2) and not getattr(defender, "grounded", False):
            return 0
        # ふゆう は check_move_immunity で処理済み

    # 砂嵐中 砂の力
    if effective_weather(field, attacker) == "sandstorm" and attacker.ability == "すなのちから":
        if eff_type in ("いわ", "じめん", "はがね"):
            power = math.floor(power * 1.3)

    # だいちのはどう：接地中かつフィールドが展開されていれば威力2倍
    if move.name_jp == "だいちのはどう":
        _grounded_dh = not ("ひこう" in (attacker.type1, attacker.type2)
                            or attacker.ability == "ふゆう" or getattr(attacker, "magnet_rise", False))
        if _grounded_dh and any(getattr(field, _t, False) for _t in
                                ("grassy_terrain", "electric_terrain", "psychic_terrain", "misty_terrain")):
            power = power * 2

    # じだんだ/やけっぱち：前のターン技が失敗していれば威力2倍
    if move.name_jp in ("じだんだ", "やけっぱち") and getattr(attacker, "_move_failed_last", False):
        power = power * 2

    # ゆきなだれ/リベンジ：このターン相手から技ダメージを受けていれば威力2倍
    if move.name_jp in ("ゆきなだれ", "リベンジ") and getattr(attacker, "_took_damage_this_turn", False):
        power = power * 2

    # うっぷんばらし：自分の能力ランクが1つでも下がっていれば威力2倍
    if move.name_jp == "うっぷんばらし":
        if any(getattr(attacker, s, 0) < 0 for s in
               ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                "stage_speed","stage_accuracy","stage_evasion")):
            power = power * 2

    # ちいさくなる状態の相手に2倍（のしかかり等）
    MINIMIZE_2X = {"のしかかり", "ドラゴンダイブ", "ヘビーボンバー", "ヒートスタンプ",
                   "フライングプレス", "サンダーダイブ"}
    if move.name_jp in MINIMIZE_2X and getattr(defender, "minimized", False):
        power = power * 2

    # 半無敵状態の相手に2倍（なみのり/うずしお→水中、じしん/マグニチュード→地中）
    dcharge = getattr(defender, "charging_move", None)
    if dcharge == "ダイビング" and move.name_jp in ("なみのり", "うずしお"):
        power = power * 2
    elif dcharge == "あなをほる" and move.name_jp in ("じしん", "マグニチュード"):
        power = power * 2

    return power


def _apply_attacker_item(dmg, attacker, move, effectiveness) -> int:
    item = attacker.item
    if item == "いのちのたま":
        dmg = math.floor(dmg * 1.3)
    elif item == "こだわりハチマキ" and move.category == "physical":
        dmg = math.floor(dmg * 1.5)
    elif item == "こだわりメガネ" and move.category == "special":
        dmg = math.floor(dmg * 1.5)
    elif item == "ちからのハチマキ" and move.category == "physical":
        dmg = math.floor(dmg * 1.1)
    elif item == "ものしりメガネ" and move.category == "special":
        dmg = math.floor(dmg * 1.1)
    elif item == "たつじんのおび" and effectiveness > 1.0:
        dmg = math.floor(dmg * 1.2)
    return dmg


def _apply_defender_item(dmg, defender, move, effectiveness) -> int:
    item = defender.item
    if item is None:
        return dmg

    # ひかりのこな：命中率補正（check_hit で処理）

    # タイプ半減きのみ（抜群時×0.5）
    berry_resist = {
        "オッカのみ":  "ほのお",
        "イトケのみ":  "みず",
        "ソクノのみ":  "でんき",
        "リンドのみ":  "くさ",
        "ヤチェのみ":  "こおり",
        "ヨプのみ":   "かくとう",
        "ビアーのみ":  "どく",
        "シュカのみ":  "じめん",
        "バコウのみ":  "ひこう",
        "ウタンのみ":  "エスパー",
        "タンガのみ":  "むし",
        "ヨロギのみ":  "いわ",
        "カシブのみ":  "ゴースト",
        "ハバンのみ":  "ドラゴン",
        "ナモのみ":   "あく",
        "リリバのみ":  "はがね",
        "ロゼルのみ":  "フェアリー",
    }
    # ホズのみ: ノーマル技を常に半減（抜群条件なし）
    if item == "ホズのみ" and move.type == "ノーマル" and effectiveness > 0:
        dmg = math.floor(dmg * 0.5)
        defender.item = None
        from .items import on_item_consumed
        on_item_consumed(defender, [])
    elif item in berry_resist and effectiveness >= 2.0:
        if move.type == berry_resist[item]:
            dmg = math.floor(dmg * 0.5)
            defender.item = None
            from .items import on_item_consumed
            on_item_consumed(defender, [])

    return dmg


def _apply_attacker_ability(dmg, attacker, defender, move, field, critical,
                             ignore_defender_ab=False) -> int:
    ab = attacker.ability
    if ab == "ちからずく" and move.category != "status" and move.name_jp in _secondary_effect_moves():
        dmg = math.floor(dmg * 1.3)
    elif ab in ("かたいツメ", "かたいつめ") and move.category == "physical" and (move.name_jp or "") not in _NON_CONTACT_PHYSICAL:
        dmg = math.floor(dmg * 1.3)
    elif ab == "てつのこぶし" and (
        "パンチ" in (move.name_jp or "") or move.name_jp in PUNCH_MOVES
    ):
        dmg = math.floor(dmg * 1.2)
    elif ab == "テクニシャン" and move.power is not None and move.power <= 60:
        dmg = math.floor(dmg * 1.5)
    elif ab == "ねつぼうそう" and move.category == "special" and attacker.status == "burn":
        dmg = math.floor(dmg * 1.5)
    elif ab == "すてみ" and move.name_jp in (
        # 反動技 ＋ 外し時クラッシュ技（とびひざげり/とびげり）のみ。
        # じゃれつく・とびはねる は反動が無いため対象外（誤適用バグ修正）。
        "すてみタックル","フレアドライブ","ボルテッカー","ウェーブタックル",
        "ダブルエッジ","ブレイブバード","ウッドハンマー",
        "とびひざげり","とびげり",
    ):
        dmg = math.floor(dmg * 1.2)
    elif ab == "がんじょうあご" and move.name_jp in (
        "かみつく","かみくだく","かみなりのキバ","ほのおのキバ","こおりのキバ",
        "どくどくのキバ","サイコファング",
    ):
        dmg = math.floor(dmg * 1.5)
    elif ab == "メガランチャー" and move.name_jp in (
        "はどうだん","みずのはどう","あくのはどう","りゅうのはどう","いやしのはどう",
        "だいちのはどう",
    ):
        dmg = math.floor(dmg * 1.5)
    elif ab == "すいほう" and move.type == "みず":
        dmg = math.floor(dmg * 2)
    elif ab == "アナライズ" and getattr(attacker, "_acts_second", False):
        dmg = math.floor(dmg * 1.3)
    elif ab == "サンパワー" and move.category == "special" and effective_weather(field, attacker) == "sunny":
        dmg = math.floor(dmg * 1.5)
    elif ab == "はりこみ" and getattr(defender, "_switched_this_turn", False):
        dmg = math.floor(dmg * 2.0)
    elif ab == "はがねのせいしん" and move.type == "はがね":
        dmg = math.floor(dmg * 1.5)
    elif ab == "そうだいしょう":
        boost = 1.0 + 0.1 * min(5, attacker.fainted_allies)
        dmg = math.floor(dmg * boost)
    return dmg


def _apply_defender_ability(dmg, attacker, defender, move, field) -> int:
    ab = defender.ability
    if ab == "マルチスケイル" and defender.hp == defender.max_hp:
        dmg = math.floor(dmg * 0.5)
    elif ab == "ファーコート" and move.category == "physical":
        dmg = math.floor(dmg * 0.5)
    elif ab == "あついしぼう" and move.type in ("ほのお", "こおり"):
        dmg = math.floor(dmg * 0.5)
    elif ab == "かんそうはだ" and move.type == "ほのお":
        dmg = math.floor(dmg * 1.25)
    elif ab in ("たいねつ", "すいほう") and move.type == "ほのお":
        dmg = math.floor(dmg * 0.5)
    elif ab == "きよめのしお" and move.type == "ゴースト":
        dmg = math.floor(dmg * 0.5)
    elif ab == "もふもふ":
        if move.category == "physical":
            dmg = math.floor(dmg * 0.5)
        if move.type == "ほのお":
            dmg = math.floor(dmg * 2)
    elif ab in ("フィルター", "ハードロック", "プリズムアーマー"):
        from .data import get_type_effectiveness
        eff = get_type_effectiveness(move.type, defender.type1, defender.type2)
        if eff > 1.0:
            dmg = math.floor(dmg * 0.75)
    return dmg


def check_hit(attacker, defender, move, field) -> bool:
    """命中判定"""
    from .items import get_evasion_item_mult
    field._weather_negated = "ノーてんき" in (attacker.ability, defender.ability)
    if move.accuracy is None:
        return True
    # ロックオン：直前にロックオンした相手には必中
    if getattr(attacker, "lock_on", False):
        return True
    # ノーガード: 両者必中
    if attacker.ability == "ノーガード" or defender.ability == "ノーガード":
        return True
    # どくどく: 毒タイプが使うと必中
    if move.name_jp == "どくどく" and "どく" in (attacker.type1, attacker.type2):
        return True
    # なみだめ: 相手の回避率・まもる等を無視して必中（accuracy=Noneだが念のため）
    if move.name_jp == "なみだめ":
        return True
    # くさタイプは粉・胞子技に免疫
    POWDER_MOVES = {"しびれごな", "ねむりごな", "どくのこな", "キノコのほうし", "わたほうし", "ちょうのこな"}
    if move.name_jp in POWDER_MOVES and "くさ" in (defender.type1, defender.type2):
        return False
    # ぜったいれいど: こおりタイプが使うと30%、非こおりタイプは20%
    if move.name_jp == "ぜったいれいど":
        acc = 0.30 if "こおり" in (attacker.type1, attacker.type2) else 0.20
        return random.random() < acc
    if effective_weather(field, attacker) == "rain" and move.name_jp in ("かみなり", "ぼうふう"):
        return True  # 雨中必中
    if effective_weather(field, attacker) == "sunny" and move.name_jp in ("かみなり", "ぼうふう"):
        return random.random() < 0.5  # 晴れ中は命中率50%
    if effective_weather(field, attacker) == "hail" and move.name_jp == "ふぶき":
        return True  # 雪中ふぶき必中
    if effective_weather(field, defender) == "sandstorm" and defender.ability == "すながくれ":
        hit_rate = (move.accuracy or 100) / 100 * 0.8
        acc_stage = attacker.stage_accuracy - defender.stage_evasion
        acc_mult = ACC_EVA_STAGE[max(-6, min(6, acc_stage))]
        hit_rate *= acc_mult
        hit_rate *= get_evasion_item_mult(defender.item)
        if defender.protecting and move.name_jp not in ("フェイント", "ゴーストダイブ"):
            return False
        return random.random() < hit_rate

    # するどいめ/はっこう: 相手の回避率の変化を無視
    _eva = 0 if attacker.ability in ("するどいめ", "はっこう") else defender.stage_evasion
    acc_stage = attacker.stage_accuracy - _eva
    acc_mult = ACC_EVA_STAGE[max(-6, min(6, acc_stage))]
    hit_rate = move.accuracy * acc_mult / 100

    # ふくがん: 命中率1.3倍
    if attacker.ability == "ふくがん":
        hit_rate *= 1.3
    # ゆきがくれ: ゆき中は回避率1.25倍（命中0.8倍）
    if effective_weather(field, defender) == "hail" and defender.ability == "ゆきがくれ":
        hit_rate *= 0.8
    # ちどりあし: こんらん中は回避率2倍（命中0.5倍）
    if defender.confused and defender.ability == "ちどりあし":
        hit_rate *= 0.5

    # はりきり: 物理技の命中率-20%
    if attacker.ability == "はりきり" and move.category == "physical":
        hit_rate *= 0.8

    # ひかりのこな補正
    hit_rate *= get_evasion_item_mult(defender.item)

    # まもるで無効（フェイント・ゴーストダイブはまもるを貫通）
    if defender.protecting and move.name_jp not in ("フェイント", "ゴーストダイブ"):
        return False

    return random.random() < hit_rate
