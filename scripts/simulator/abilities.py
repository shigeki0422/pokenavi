"""
特性効果の定義
各タイミング別に関数を提供:
  entry_ability(poke, opponent, field)        場に出た時
  on_physical_hit(attacker, defender, move)   物理技で被弾時
  on_ko(attacker, field)                      相手を倒した時
  end_of_turn_ability(poke, field)            ターン終了時
  on_switch_out(poke)                         交代で引っ込む時
  on_stat_drop(poke, stat)                    能力が下げられた時
"""
import math
import random
from typing import Optional, TYPE_CHECKING
from .damage import is_contact_move, effective_weather

if TYPE_CHECKING:
    from .pokemon import BattlePokemon
    from .battle import BattleField


# ── てんきや/ぎたい：天候・フィールドでタイプが変わる ──────────────────────────

def _apply_forme_type(poke: "BattlePokemon", field: "BattleField", logs: list) -> None:
    ab = poke.ability
    new_t = None
    if ab == "てんきや":
        new_t = {"sunny": "ほのお", "rain": "みず", "hail": "こおり"}.get(effective_weather(field, poke), poke.base_type1)
    elif ab == "ぎたい":
        if getattr(field, "electric_terrain", False):  new_t = "でんき"
        elif getattr(field, "grassy_terrain", False):  new_t = "くさ"
        elif getattr(field, "psychic_terrain", False): new_t = "エスパー"
        elif getattr(field, "misty_terrain", False):   new_t = "フェアリー"
        else: new_t = poke.base_type1
    if new_t is not None and (poke.type1 != new_t or poke.type2 is not None):
        poke.type1 = new_t
        poke.type2 = None
        logs.append(f"{poke.name} の {ab}！ {new_t} タイプになった！")


# ── 場に出た時 ──────────────────────────────────────────────────────────────

def entry_ability(poke: "BattlePokemon", opponent: "BattlePokemon",
                  field: "BattleField", weather_duration: int = 5) -> list[str]:
    logs = []
    ab = poke.ability

    # 天候系
    WEATHER_MAP = {
        "すなおこし": "sandstorm", "ひでり": "sunny",
        "あめふらし": "rain",      "ゆきふらし": "hail",
    }
    if ab in WEATHER_MAP and field.weather != WEATHER_MAP[ab]:
        field.weather = WEATHER_MAP[ab]
        field.weather_count = weather_duration
        logs.append(f"{poke.name} の {ab}！")

    # いかく
    if ab == "いかく":
        if opponent.ability in ("クリアボディ", "しろいけむり", "かがくへんかガス",
                                "マイペース", "どんかん", "きもったま", "せいしんりょく"):
            logs.append(f"{poke.name} の いかく は {opponent.name} に効かなかった！")
        elif opponent.ability == "あまのじゃく":
            # 対象自身への能力変化なので逆転（攻撃が上がる）
            opponent.stage_attack = min(6, opponent.stage_attack + 1)
            logs.append(f"{poke.name} の いかく！ しかし {opponent.name} の あまのじゃく で攻撃が上がった！")
        else:
            opponent.stage_attack = max(-6, opponent.stage_attack - 1)
            logs.append(f"{poke.name} の いかく！ {opponent.name} の攻撃が下がった！")

    # ダウンロード
    if ab == "ダウンロード":
        if opponent.defense <= opponent.sp_defense:
            poke.stage_attack = min(6, poke.stage_attack + 1)
            logs.append(f"{poke.name} の ダウンロード：攻撃が上がった！")
        else:
            poke.stage_sp_attack = min(6, poke.stage_sp_attack + 1)
            logs.append(f"{poke.name} の ダウンロード：特攻が上がった！")

    # てんきや/ぎたい（登場時に天候・フィールドでタイプ変化）
    if ab in ("てんきや", "ぎたい"):
        _apply_forme_type(poke, field, logs)

    # トレース（登場時に相手の特性をコピー）
    if ab == "トレース":
        _UNCOPYABLE = {"トレース", "かわりもの", "イリュージョン", "ばけのかわ", "かがくへんかガス"}
        if opponent.ability and opponent.ability not in _UNCOPYABLE:
            poke.ability = opponent.ability  # type: ignore
            logs.append(f"{poke.name} は トレース！ {opponent.name} の {opponent.ability} になった！")

    # かんろなミツ（登場時に相手の回避率-1。1戦闘1回）
    if ab == "かんろなミツ" and not getattr(poke, "_honey_used", False):
        poke._honey_used = True  # type: ignore
        if opponent.ability not in ("クリアボディ", "しろいけむり", "かいりきバサミ"):
            opponent.stage_evasion = max(-6, opponent.stage_evasion - 1)
            logs.append(f"{poke.name} の かんろなミツ！ {opponent.name} の回避率が下がった！")

    # かわりもの（登場時に目の前の相手に変身。HP以外コピー、PP5、ランクもコピー）
    if ab == "かわりもの" and not getattr(poke, "_transformed", False):
        poke._transform_backup = {  # type: ignore
            "attack": poke.attack, "defense": poke.defense, "sp_attack": poke.sp_attack,
            "sp_defense": poke.sp_defense, "speed": poke.speed, "ability": poke.ability,
            "moves": list(poke.moves), "pp": list(poke.pp),
        }
        poke.attack, poke.defense = opponent.attack, opponent.defense
        poke.sp_attack, poke.sp_defense = opponent.sp_attack, opponent.sp_defense
        poke.speed = opponent.speed
        poke.ability = opponent.ability
        poke.type1, poke.type2 = opponent.type1, opponent.type2
        poke.moves = list(opponent.moves)
        poke.pp = [min(5, m.pp if m else 5) for m in opponent.moves]
        for _s in ("stage_attack", "stage_defense", "stage_sp_attack", "stage_sp_defense",
                   "stage_speed", "stage_accuracy", "stage_evasion"):
            setattr(poke, _s, getattr(opponent, _s, 0))
        poke._transformed = True  # type: ignore
        logs.append(f"{poke.name} は かわりもの！ {opponent.name} に変身した！")

    return logs


# ── 技で被弾した後 ──────────────────────────────────────────────────────────

def on_after_hit(attacker: "BattlePokemon", defender: "BattlePokemon",
                 move, logs: list) -> None:
    """物理・特殊を問わず被弾後の特性効果"""
    ab = defender.ability

    # くだけるよろい
    if ab == "くだけるよろい" and move.category == "physical":
        defender.stage_defense = max(-6, defender.stage_defense - 1)
        defender.stage_speed   = min(6, defender.stage_speed + 2)
        logs.append(f"{defender.name} の くだけるよろい！ 防御↓ 素早さ↑↑")

    # せいでんき (接触技 → 30%麻痺)
    if ab == "せいでんき" and is_contact_move(move) and attacker.ability != "えんかく":
        if random.random() < 0.30:
            ok = attacker.apply_status("paralysis")
            if ok:
                logs.append(f"{defender.name} の せいでんき！ {attacker.name} が まひ した！")

    # のろわれボディ → battle.py の _execute_move 内で処理

    # ひらいしん（でんき無効 → SpAtk+1 は damage.py で0ダメにした後ここで処理）
    if ab == "ひらいしん" and move.type == "でんき":
        defender.stage_sp_attack = min(6, defender.stage_sp_attack + 1)
        logs.append(f"{defender.name} の ひらいしん！ 特攻が上がった！")

    # ちくでん/ちょすい/かんそうはだ（対応タイプを吸収すると最大HP1/4回復）
    _ABSORB_HEAL = {"ちくでん": "でんき", "ちょすい": "みず", "かんそうはだ": "みず", "どしょく": "じめん"}
    if ab in _ABSORB_HEAL and move.type == _ABSORB_HEAL[ab]:
        if defender.hp < defender.max_hp:
            heal = max(1, defender.max_hp // 4)
            defender.hp = min(defender.max_hp, defender.hp + heal)
            logs.append(f"{defender.name} の {ab}！ HPが {heal} 回復した！")

    # もらいび（ほのお無効 → 次のほのお技強化フラグ）
    if ab == "もらいび" and move.type == "ほのお":
        if not getattr(defender, "_flash_fire_active", False):
            defender._flash_fire_active = True  # type: ignore
            logs.append(f"{defender.name} の もらいび が発動！")

    # でんきエンジン（でんき無効 → Speed+1）
    if ab == "でんきエンジン" and move.type == "でんき":
        defender.stage_speed = min(6, defender.stage_speed + 1)
        logs.append(f"{defender.name} の でんきエンジン！ 素早さが上がった！")

    # そうしょく（くさ無効 → 攻撃+1）
    if ab == "そうしょく" and move.type == "くさ":
        defender.stage_attack = min(6, defender.stage_attack + 1)
        logs.append(f"{defender.name} の そうしょく！ 攻撃が上がった！")

    # でんきにかえる（被弾 → 次のでんき技の威力1.5倍、何度でも再充電可）
    if ab == "でんきにかえる":
        defender._electromorphosis_charged = True  # type: ignore
        logs.append(f"{defender.name} の でんきにかえる！ でんき技がチャージされた！")

    # ふうりょく（風技を受けると じゅうでん 状態になる）
    WIND_MOVES = {
        "こごえるかぜ", "ぼうふう", "ふぶき", "ねっぷう", "ふきとばし",
        "おいかぜ", "すなあらし", "はなふぶき", "エアカッター",
    }
    if ab == "ふうりょく" and move.name_jp in WIND_MOVES:
        defender.charged = True
        logs.append(f"{defender.name} の ふうりょく！ じゅうでん状態になった！")

    # シンクロ（状態異常を受けたら攻撃側にも同じ状態異常）
    if ab == "シンクロ" and defender.is_alive and defender.status in ("poison","badpoison","paralysis","burn"):
        if attacker.is_alive:
            ok = attacker.apply_status(defender.status)
            if ok:
                logs.append(f"{defender.name} の シンクロ！ {attacker.name} にも {defender.status} が伝染った！")

    # ぎゃくじょう（HP半分以下になった時に攻撃+2）
    if ab == "ぎゃくじょう" and defender.is_alive:
        was_above_half = not getattr(defender, '_gyaku_triggered', False)
        if was_above_half and defender.hp <= defender.max_hp // 2:
            defender.stage_sp_attack = min(6, defender.stage_sp_attack + 1)
            defender._gyaku_triggered = True  # type: ignore
            logs.append(f"{defender.name} の ぎゃくじょう！ 特攻が上がった！")

    # ねばりかわ / ながいしっぽ（接触技 → 攻撃側の素早さ-1）
    if ab in ("ねばりかわ", "ながいしっぽ") and is_contact_move(move) and attacker.ability != "えんかく":
        if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
            attacker.stage_speed = max(-6, attacker.stage_speed - 1)
            logs.append(f"{defender.name} の {ab}！ {attacker.name} の素早さが下がった！")

    # じきゅうりょく（被弾 → 防御+1）
    if ab == "じきゅうりょく":
        if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
            defender.stage_defense = min(6, defender.stage_defense + 1)
            logs.append(f"{defender.name} の じきゅうりょく！ 防御が上がった！")

    _mold = attacker.ability in ("かたやぶり", "ターボブレイズ", "テラボルテージ")
    # えんかく: 攻撃側の技は接触扱いにならない
    _contact = is_contact_move(move) and attacker.ability != "えんかく"

    # せいぎのこころ（あく技を受けると攻撃+1）
    if ab == "せいぎのこころ" and move.type == "あく":
        defender.stage_attack = min(6, defender.stage_attack + 1)
        logs.append(f"{defender.name} の せいぎのこころ！ 攻撃が上がった！")

    # 接触技を受けた時の防御側特性（かたやぶり系で無視される）
    if _contact and not _mold and attacker.is_alive:
        if ab == "ほのおのからだ" and random.random() < 0.30:
            if attacker.apply_status("burn"):
                logs.append(f"{defender.name} の ほのおのからだ！ {attacker.name} は やけど した！")
        if ab == "どくのトゲ" and random.random() < 0.30:
            if attacker.apply_status("poison"):
                logs.append(f"{defender.name} の どくのトゲ！ {attacker.name} は どく になった！")
        if ab == "ぬめぬめ":
            attacker.stage_speed = max(-6, attacker.stage_speed - 1)
            logs.append(f"{defender.name} の ぬめぬめ！ {attacker.name} の素早さが下がった！")
        if ab == "ミイラ" and attacker.ability not in ("ミイラ", "かがくへんかガス"):
            attacker.ability = "ミイラ"  # type: ignore
            logs.append(f"{defender.name} の ミイラ！ {attacker.name} の特性が ミイラ になった！")
        elif ab == "さまようたましい" and attacker.ability not in ("かがくへんかガス",):
            attacker.ability, defender.ability = defender.ability, attacker.ability  # type: ignore
            logs.append(f"{defender.name} の さまようたましい！ 特性を入れ替えた！")

    # どくしゅ（攻撃側：接触技を当てると30%でどく）
    if attacker.ability == "どくしゅ" and _contact and defender.is_alive and random.random() < 0.30:
        if defender.apply_status("poison"):
            logs.append(f"{attacker.name} の どくしゅ！ {defender.name} は どく になった！")

    # あくしゅう（攻撃側：ダメージを与えた技で10%ひるみ）
    if attacker.ability == "あくしゅう" and defender.is_alive and move.category != "status" and random.random() < 0.10:
        defender.flinched = True
        logs.append(f"{attacker.name} の あくしゅう！ {defender.name} はひるんだ！")

    # おうじゃのしるし（アイテム：ダメージを与えた技で10%ひるみ）
    if attacker.item == "おうじゃのしるし" and defender.is_alive and move.category != "status" \
            and defender.ability not in ("せいしんりょく", "どんかん") and random.random() < 0.10:
        defender.flinched = True
        logs.append(f"{attacker.name} の おうじゃのしるし！ {defender.name} はひるんだ！")



# ── さめはだ/てつのとげ（防御側が倒れても発動）──────────────────────────────────

def _rough_skin_recoil(attacker: "BattlePokemon", defender: "BattlePokemon",
                       move, logs: list) -> None:
    ab = defender.ability
    _enkaku = attacker.ability == "えんかく"
    if ab in ("さめはだ", "てつのとげ") and is_contact_move(move) and not _enkaku:
        if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
            recoil = max(1, attacker.max_hp // 8)
            attacker.take_damage(recoil)
            logs.append(f"{defender.name} の {ab}！ {attacker.name} に {recoil} のダメージ！")

    # ゆうばく（接触技でひんしにされると相手に最大HP1/4ダメージ）
    if ab == "ゆうばく" and is_contact_move(move) and not _enkaku and not defender.is_alive and attacker.is_alive:
        if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
            recoil = max(1, attacker.max_hp // 4)
            attacker.take_damage(recoil)
            logs.append(f"{defender.name} の ゆうばく！ {attacker.name} に {recoil} のダメージ！")

    # とびだすハバネロ（被弾 → 攻撃側をやけど）
    if ab == "とびだすハバネロ" and move.category != "status":
        if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
            ok = attacker.apply_status("burn")
            if ok:
                logs.append(f"{defender.name} の とびだすハバネロ！ {attacker.name} がやけどを負った！")


def on_defender_ko(attacker: "BattlePokemon", defender: "BattlePokemon",
                   damage: int, logs: list) -> None:
    """防御側が倒された時に発動する特性効果"""
    ab = defender.ability

    # とびだすなかみ（倒された時、受けたダメージ分を攻撃側に返す）
    if ab == "とびだすなかみ" and damage > 0 and attacker.is_alive:
        attacker.take_damage(damage)
        logs.append(f"{defender.name} の とびだすなかみ！ {attacker.name} に {damage} のダメージ！")


# ── 相手を倒した後 ──────────────────────────────────────────────────────────

def on_ko(attacker: "BattlePokemon", logs: list) -> None:
    ab = attacker.ability

    if ab == "じしんかじょう":
        attacker.stage_attack = min(6, attacker.stage_attack + 1)
        logs.append(f"{attacker.name} の じしんかじょう！ 攻撃が上がった！")



# ── ターン終了時 ────────────────────────────────────────────────────────────

def end_of_turn_ability(poke: "BattlePokemon", field: "BattleField", logs: list) -> None:
    ab = poke.ability

    # かそく
    if ab == "かそく":
        poke.stage_speed = min(6, poke.stage_speed + 1)

    # アイスボディ（雹中HP1/16回復）
    if ab == "アイスボディ" and effective_weather(field, poke) == "hail":
        heal = max(1, poke.max_hp // 16)
        poke.hp = min(poke.max_hp, poke.hp + heal)

    # あめうけざら（雨中HP1/16回復）
    if ab == "あめうけざら" and effective_weather(field, poke) == "rain":
        heal = max(1, poke.max_hp // 16)
        poke.hp = min(poke.max_hp, poke.hp + heal)

    # うるおいボディ（雨中ターン終わりに状態異常が治る）
    if ab == "うるおいボディ" and effective_weather(field, poke) == "rain" and poke.status is not None:
        poke.status = None
        poke.bad_poison_count = 0
        logs.append(f"{poke.name} の うるおいボディ！ 状態異常が治った")

    # だっぴ（ターン終わり30%で状態異常が治る）
    if ab == "だっぴ" and poke.status is not None and random.random() < 0.30:
        poke.status = None
        poke.bad_poison_count = 0
        logs.append(f"{poke.name} の だっぴ！ 状態異常が治った")

    # てんきや/ぎたい（ターン終わりに天候・フィールドでタイプ再計算）
    if ab in ("てんきや", "ぎたい"):
        _apply_forme_type(poke, field, logs)

    # はらぺこスイッチ（ターン終わりにまんぷく/はらぺこを切り替え）
    if ab == "はらぺこスイッチ":
        poke._hangry = not getattr(poke, "_hangry", False)  # type: ignore
        logs.append(f"{poke.name} の はらぺこスイッチ！ 模様が変わった！")

    # しゅうかく（ターン終わり、消費したきのみを50%／にほんばれ中は必ず復活）
    if ab == "しゅうかく" and poke.item is None and getattr(poke, "_last_berry", None):
        if effective_weather(field, poke) == "sunny" or random.random() < 0.50:
            poke.item = poke._last_berry  # type: ignore
            logs.append(f"{poke.name} の しゅうかく！ {poke.item} を作り出した！")

    # はんすう（きのみを食べた次のターン終わりに、もう一度その効果を受ける）
    if getattr(poke, "_ruminate_count", 0) > 0:
        poke._ruminate_count -= 1  # type: ignore
        if poke._ruminate_count == 0:
            _berry = getattr(poke, "_ruminate_berry", None)
            poke._ruminate_berry = None  # type: ignore
            _QB = {"カムラのみ": "speed", "サルのみ": "sp_attack", "リュガのみ": "defense", "タラプのみ": "sp_defense"}
            if _berry == "オボンのみ":
                _h = max(1, poke.max_hp // 4); poke.hp = min(poke.max_hp, poke.hp + _h)
                logs.append(f"{poke.name} の はんすう！ {_berry} の効果でHPが {_h} 回復した！")
            elif _berry in _QB:
                _st = _QB[_berry]; setattr(poke, f"stage_{_st}", min(6, getattr(poke, f"stage_{_st}", 0) + 1))
                logs.append(f"{poke.name} の はんすう！ {_berry} の効果が再発動した！")

    # サンパワー（晴れ中1/8ダメ）
    if ab == "サンパワー" and effective_weather(field, poke) == "sunny":
        dmg = max(1, poke.max_hp // 8)
        poke.take_damage(dmg)
        logs.append(f"{poke.name} の サンパワー！ {dmg} のダメージ！")

    # かんそうはだ（晴れダメ・雨回復）
    if ab == "かんそうはだ":
        if effective_weather(field, poke) == "sunny":
            poke.take_damage(max(1, poke.max_hp // 8))
            logs.append(f"{poke.name} は日光でダメージを受けた！")
        elif effective_weather(field, poke) == "rain":
            heal = max(1, poke.max_hp // 8)
            poke.hp = min(poke.max_hp, poke.hp + heal)

    # ムラっけ: ランダムに1ランク上昇 + 1ランク下降
    if ab == "ムラっけ":
        STATS = ["stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed","stage_accuracy","stage_evasion"]
        up_stat = random.choice(STATS)
        old = getattr(poke, up_stat, 0)
        setattr(poke, up_stat, min(6, old + 2))
        down_stat = random.choice([s for s in STATS if s != up_stat])
        old2 = getattr(poke, down_stat, 0)
        setattr(poke, down_stat, max(-6, old2 - 1))
        from .pokemon import STAT_STAGE_MULT
        _STAT_JP = {"stage_attack":"こうげき","stage_defense":"ぼうぎょ","stage_sp_attack":"とくこう","stage_sp_defense":"とくぼう","stage_speed":"すばやさ","stage_accuracy":"めいちゅう","stage_evasion":"かいひ"}
        logs.append(f"{poke.name} の ムラっけ！ {_STAT_JP.get(up_stat,up_stat)}↑↑ {_STAT_JP.get(down_stat,down_stat)}↓")


# ── 交代で引っ込む時 ────────────────────────────────────────────────────────

def on_switch_out(poke: "BattlePokemon", logs: list, field=None) -> None:
    ab = poke.ability

    if ab == "マイティチェンジ" and not poke.hero_forme:
        evs = poke.evs or {}
        up, dn = __import__('simulator.data', fromlist=['NATURE_MODS']).NATURE_MODS.get(poke.nature, (None, None))
        def nat(key):
            return 1.1 if up == key else (0.9 if dn == key else 1.0)
        from simulator.pokemon import calc_stat
        poke.attack     = calc_stat(160, evs.get('A', 0), 31, nat('attack'))
        poke.defense    = calc_stat(97,  evs.get('B', 0), 31, nat('defense'))
        poke.sp_attack  = calc_stat(106, evs.get('C', 0), 31, nat('sp_attack'))
        poke.sp_defense = calc_stat(87,  evs.get('D', 0), 31, nat('sp_defense'))
        poke.speed      = calc_stat(100, evs.get('S', 0), 31, nat('speed'))
        poke.hero_forme = True
        logs.append(f"{poke.name} は マイティフォルムに変化した！")

    if ab == "さいせいりょく":
        heal = poke.max_hp // 3
        poke.hp = min(poke.max_hp, poke.hp + heal)
        logs.append(f"{poke.name} の さいせいりょく！ {heal}回復")

    if ab == "しぜんかいふく" and poke.status is not None:
        poke.status = None
        poke.bad_poison_count = 0
        logs.append(f"{poke.name} の しぜんかいふく！ 状態異常が治った")


# ── 能力が下げられた時 ──────────────────────────────────────────────────────

def on_stat_lowered(poke: "BattlePokemon", logs: list) -> None:
    ab = poke.ability

    if ab == "かちき":
        poke.stage_sp_attack = min(6, poke.stage_sp_attack + 2)
        logs.append(f"{poke.name} の かちき！ 特攻が大きく上がった！")

    if ab == "まけんき":
        poke.stage_attack = min(6, poke.stage_attack + 2)
        logs.append(f"{poke.name} の まけんき！ 攻撃が大きく上がった！")


# ── ダメージ計算内の特殊処理 ───────────────────────────────────────────────

# 攻撃無効チェック（damage.py のcheck_immunityから呼ぶ）
IMMUNITY_ABILITIES = {
    "ふゆう":       {"type": "じめん"},
    "ちくでん":     {"type": "でんき"},
    "ちょすい":     {"type": "みず"},
    "もらいび":     {"type": "ほのお"},
    "ひらいしん":   {"type": "でんき"},
    "でんきエンジン": {"type": "でんき"},
    "こんがりボディ": {"type": "ほのお"},
    "かんそうはだ": {"type": "みず"},   # 回復として扱う
    "そうしょく":   {"type": "くさ"},
    "どしょく":     {"type": "じめん"},
    "ぼうだん":     {},  # 弾技全般
}


def check_move_immunity(defender: "BattlePokemon", move_type: str,
                        move_name: str) -> bool:
    """True: 技が無効（ダメージ0）"""
    ab = defender.ability

    # うちおとす接地中はじめん無効が解除される
    _grounded = getattr(defender, "grounded", False)

    # ふゆう：じめん無効（ただしかたやぶり等で無視される）
    if ab == "ふゆう" and move_type == "じめん" and not _grounded:
        return True

    # でんじふゆう：じめん技を無効化
    if getattr(defender, "magnet_rise", False) and move_type == "じめん" and not _grounded:
        return True

    if ab in ("ちくでん", "ひらいしん", "でんきエンジン") and move_type == "でんき":
        return True

    if ab == "ちょすい" and move_type == "みず":
        return True

    if ab in ("もらいび",) and move_type == "ほのお":
        return True

    if ab == "こんがりボディ" and move_type == "ほのお":
        return True

    if ab == "かんそうはだ" and move_type == "みず":
        return True

    if ab == "そうしょく" and move_type == "くさ":
        return True

    if ab == "どしょく" and move_type == "じめん":
        return True

    if ab == "ふしぎなまもり":
        from .data import get_type_effectiveness
        eff = get_type_effectiveness(move_type, defender.type1, defender.type2)
        return eff <= 1.0

    from .damage import BALL_BOMB_MOVES, SOUND_MOVES
    if ab == "ぼうだん" and move_name in BALL_BOMB_MOVES:
        return True

    if ab == "ぼうおん" and move_name in SOUND_MOVES:
        return True

    return False


# ──かたやぶり系の特性無視 ────────────────────────────────────────────────────

MOLD_BREAKER_ABILITIES = {
    "かたやぶり", "ターボブレイズ", "テラボルテージ",
    "きんぞくおん",  # ガラルマッギョ等
}


# 単体バトル(1v1)・性別なしの本シミュレータでは効果が発生しない特性。
# 「効果が出ない」のが正しい挙動として明示的に no-op 扱いする（gameする目的ではなく仕様の明記）。
NO_SINGLE_BATTLE_EFFECT = {
    # ダブルバトル専用（味方への効果のため1v1では発動しない）
    "いやしのこころ", "おもてなし", "きみょうなくすり", "きょうせい",
    "テレパシー", "フラワーベール", "フレンドガード", "プラス", "マイナス",
    "レシーバー", "すじがねいり",
    # 性別未実装のため発動しない
    "とうそうしん", "メロメロボディ",
}
# 注: おみとおし/きけんよち は情報開示として正式実装（Battle._info_abilities_on_entry）。


def should_ignore_ability(attacker: "BattlePokemon") -> bool:
    return attacker.ability in MOLD_BREAKER_ABILITIES


# ── 低HP時攻撃ブースト ──────────────────────────────────────────────────────

PINCH_ABILITIES = {
    "もうか":    ("ほのお",   1/3),
    "げきりゅう": ("みず",    1/3),
    "しんりょく": ("くさ",    1/3),
    "もうこ":    ("ほのお",   1/3),  # 猛火
    "むしのしらせ": ("むし",  1/3),
}


def get_pinch_multiplier(attacker: "BattlePokemon", move_type: str) -> float:
    ab = attacker.ability
    if ab in PINCH_ABILITIES:
        required_type, threshold = PINCH_ABILITIES[ab]
        if move_type == required_type and attacker.hp <= attacker.max_hp * threshold:
            return 1.5
    return 1.0


# ── きれあじ (Sharpness) ────────────────────────────────────────────────────

SLICING_MOVES = {
    # DBに存在する切る技（ポケモンチャンピオンズ準拠）
    "アクアカッター", "エアスラッシュ", "エアカッター", "がんせきアックス",
    "クロスポイズン", "サイコカッター", "シェルブレード", "シザークロス",
    "シャドークロー", "せいなるつるぎ", "ソーラーブレード", "つじぎり",
    "つばめがえし", "ドゲザン", "ドラゴンクロー", "ネズミざん",
    "ひけん・ちえなみ", "ブレイククロー", "フェイタルクロー",
    "むねんのつるぎ", "リーフブレード",
}


def get_sharpness_multiplier(attacker: "BattlePokemon", move_name: str) -> float:
    if attacker.ability == "きれあじ" and move_name in SLICING_MOVES:
        return 1.5
    return 1.0


# ── スクラッピー（ノーマル・かくとうがゴーストに当たる）───────────────────

def scrappy_override(attacker: "BattlePokemon", move_type: str,
                     defender: "BattlePokemon") -> bool:
    """True: 無効を等倍に上書きする"""
    if attacker.ability == "きもったま":
        if move_type in ("ノーマル", "かくとう") and \
           "ゴースト" in (defender.type1, defender.type2):
            return True
    return False
