"""
バトルフィールドとターン処理エンジン
"""
import copy
import math
import os
import random
from dataclasses import dataclass, field
from typing import Optional, List, Tuple
from .pokemon import BattlePokemon
from .data import MoveData, get_type_effectiveness
from .damage import calc_damage, check_hit, _effective_move_type, is_contact_move, effective_weather
from .abilities import (
    entry_ability, on_after_hit, on_ko, on_switch_out,
    end_of_turn_ability, on_stat_lowered, MOLD_BREAKER_ABILITIES,
    _rough_skin_recoil, on_defender_ko,
)
from .items import (
    apply_sturdy, try_cure_berry, try_white_herb,
    apply_hp_berry, on_item_consumed, has_quick_claw_trigger,
    is_choice_item, get_speed_item_multiplier,
    try_mental_herb, try_leppa_berry,
)


# おうごんのからだ が無効化する「相手に向けた変化技」（自己強化・天候・設置・画面等は対象外）
_GAG_BLOCK = frozenset({
    "でんじは", "おにび", "どくどく", "どくのこな", "しびれごな", "ねむりごな", "キノコのほうし",
    "さいみんじゅつ", "あくび", "へびにらみ", "ちょうおんぱ", "あやしいひかり", "いばる", "おだてる",
    "ちょうはつ", "アンコール", "かなしばり", "いちゃもん", "やどりぎのタネ", "メロメロ", "くろいまなざし",
    "なきごえ", "にらみつける", "あまえる", "すなかけ", "フラッシュ", "あまいかおり", "うそなき",
    "ひっくりかえす", "ワンダールーム", "トリック", "すりかえ", "なかよくする", "このゆびとまれ",
    "とおせんぼう", "くすぐる", "テクスチャー2",
})


def _is_megastone(item: Optional[str]) -> bool:
    """メガストーン（〜ナイト/ナイトＸ/ナイトＹ）かどうか判定。道具奪取・交換・はたき落としは失敗。"""
    return item is not None and (item.endswith("ナイト")
                                 or item.endswith("ナイトＸ") or item.endswith("ナイトＹ")
                                 or item.endswith("ナイトX") or item.endswith("ナイトY"))


def is_trapped(poke, opponent) -> bool:
    """poke が交代・逃走できない状態か。
    かげふみ：ゴーストタイプ以外の相手を交代不可にする（ゴースト/ふゆうは無関係に効かない）。
    その他、トラップ技(trapped)・バインドでも交代不可。"""
    if opponent is not None and getattr(opponent, "is_alive", False) \
            and opponent.ability == "かげふみ" and "ゴースト" not in (poke.type1, poke.type2):
        return True
    return getattr(poke, "trapped", False) or getattr(poke, "_bound_turns", 0) > 0
from .opponent_view import OpponentView

MAX_TURNS = 30  # 30ターンを超えたら引き分け（長い受け合いの打ち切り）

STAT_JP = {
    "stage_attack": "こうげき",
    "stage_defense": "ぼうぎょ",
    "stage_sp_attack": "とくこう",
    "stage_sp_defense": "とくぼう",
    "stage_speed": "すばやさ",
    "stage_accuracy": "めいちゅう",
    "stage_evasion": "かいひ",
}


@dataclass
class BattleField:
    weather: Optional[str] = None        # sunny/rain/sandstorm/hail
    weather_count: int = 0
    trick_room: bool = False
    trick_room_count: int = 0
    stealth_rock: List[bool] = field(default_factory=lambda: [False, False])  # [p1, p2]
    spikes: List[int] = field(default_factory=lambda: [0, 0])
    toxic_spikes: List[int] = field(default_factory=lambda: [0, 0])  # どくびし層数
    sticky_web: List[bool] = field(default_factory=lambda: [False, False])  # ねばねばネット
    misty_terrain: bool = False
    misty_terrain_count: int = 0
    electric_terrain: bool = False
    electric_terrain_count: int = 0
    psychic_terrain: bool = False
    psychic_terrain_count: int = 0
    gravity: int = 0           # じゅうりょく残りターン
    magic_room: int = 0        # マジックルーム残りターン
    wonder_room: int = 0       # ワンダールーム残りターン
    grassy_terrain: bool = False
    grassy_terrain_count: int = 0


@dataclass
class Action:
    """1ターンの行動"""
    type: str          # "move" / "switch" / "mega" / "pass"
    move: Optional[MoveData] = None
    move_idx: int = 0
    switch_to: int = -1
    do_mega: bool = False


class BattleSide:
    def __init__(self, party: List[BattlePokemon], viewer_label: str = "",
                 source6: "Optional[List[BattlePokemon]]" = None):
        self.party = party
        # 見せ合いで公開する候補（隠れ選出時の6体ソース）。未指定なら選出=候補（従来＝選出公開）。
        self.source6 = source6 if source6 is not None else party
        self.active_idx = 0
        self.fainted = []
        self.stealth_rock_set = False
        self.mega_used = False
        self.opp_view = OpponentView(viewer_label)
        self.belief = None  # OpponentBelief（任意）。学習側が付与すると被ダメージ割合からEV/性格を推定
        self.field_idx: int = 0  # フィールド内のインデックス (0=P1, 1=P2)、Battle.__init__で設定
        self.reflect = False
        self.reflect_count = 0
        self.light_screen = False
        self.light_screen_count = 0
        self.aurora_veil = False
        self.aurora_veil_count = 0
        self.tailwind = False
        self.tailwind_count = 0
        self.wish_hp = 0
        self.wish_count = 0
        self.healing_wish = False
        self.safeguard = 0  # しんぴのまもり残りターン
        self.future_sight_count = 0   # みらいよち発動までの残りターン
        self.future_sight_dmg = 0
        self.future_sight_name = ""

    @property
    def active(self) -> BattlePokemon:
        return self.party[self.active_idx]

    def has_alive(self) -> bool:
        return any(p.is_alive for p in self.party)

    def next_alive_idx(self) -> Optional[int]:
        for i, p in enumerate(self.party):
            if p.is_alive and i != self.active_idx:
                return i
        return None

    def switch_to(self, idx: int, logs: Optional[List[str]] = None, field=None):
        prev = self.active
        # 引っ込む時の特性処理
        if logs is not None:
            on_switch_out(prev, logs, field)
        if getattr(prev, '_transformed', False):
            backup = prev._transform_backup  # type: ignore
            prev.attack     = backup["attack"]
            prev.defense    = backup["defense"]
            prev.sp_attack  = backup["sp_attack"]
            prev.sp_defense = backup["sp_defense"]
            prev.speed      = backup["speed"]
            prev.ability    = backup["ability"]
            prev.moves      = backup["moves"]
            prev.pp         = backup["pp"]
            prev._transformed = False  # type: ignore
            prev._transform_backup = None  # type: ignore
        prev._illusion_name = None  # type: ignore
        prev.stage_attack = prev.stage_defense = 0
        prev.stage_sp_attack = prev.stage_sp_defense = 0
        prev.stage_speed = prev.stage_accuracy = prev.stage_evasion = 0
        prev.type1 = prev.base_type1
        prev.type2 = prev.base_type2
        prev.confused = False
        prev.yawn_count = 0
        prev.flinched = False
        prev.protecting = False
        prev.enduring = False
        prev.grounded = False
        prev.used_moves = set()
        prev.ate_berry = False
        prev.protect_consecutive = 0
        prev.locked_move = None
        prev.choice_locked_move = None
        prev.disabled_move = None
        prev.disabled_turns = 0
        prev.lock_count = 0
        prev.charging_move = None
        prev.bound_count = 0
        prev.throat_chop_count = 0
        prev._substitute_hp = 0  # type: ignore
        prev._electromorphosis_charged = False  # type: ignore
        prev._gyaku_triggered = False  # type: ignore
        prev._protean_used = False  # type: ignore
        prev._barrier_done = False  # type: ignore
        prev._info_done = False  # type: ignore
        prev.recharge = False
        prev.crit_stage = 0
        prev.perish_count = 0
        prev.destiny_bond = False
        prev.cursed = False
        prev.charged = False
        self.active_idx = idx
        # バトンタッチのランク引き継ぎ
        baton = getattr(prev, '_baton_stages', None)
        if baton:
            for attr, val in baton.items():
                setattr(self.active, attr, max(-6, min(6, val)))
            prev._baton_stages = None  # type: ignore
        self.active.turns_out = 0
        self.active.times_hit = 0
        self.active._switched_this_turn = True  # type: ignore
        self.active.fainted_allies = sum(1 for p in self.party if not p.is_alive)


def _priority(action: Action, poke: BattlePokemon, field: "BattleField | None" = None) -> int:
    if action.type == "switch":
        return 6
    if action.type == "mega":
        return 7
    if action.move is None:
        return 0
    base = action.move.priority
    # グラススライダー: グラスフィールド時に優先度+1（地面のポケモンのみ）
    if action.move.name_jp == "グラススライダー" and field is not None and field.grassy_terrain:
        if not (poke.ability == "ふゆう" or "ひこう" in (poke.type1, poke.type2)
                or getattr(poke, "magnet_rise", False)):
            base += 1
    # はやてのつばさ: HP満タン時、ひこう技の優先度+1
    if poke.ability == "はやてのつばさ" and action.move.type == "ひこう" and poke.hp == poke.max_hp:
        base += 1
    # いたずらごころ: 変化技の優先度+1（技タイプを問わない。あく相手への無効は命中処理側）
    if poke.ability == "いたずらごころ" and action.move.category == "status":
        base += 1
    # せんせいのツメ
    if has_quick_claw_trigger(poke.item):
        base += 1
    return base


def _speed_order(
    side1: BattleSide, action1: Action,
    side2: BattleSide, action2: Action,
    field: BattleField,
) -> bool:
    """True: side1が先攻"""
    p1, p2 = side1.active, side2.active
    pri1 = _priority(action1, p1, field)
    pri2 = _priority(action2, p2, field)
    if pri1 != pri2:
        return pri1 > pri2

    # あとだし: 同じ優先度の中で最後に行動する
    _stall1 = p1.ability == "あとだし"; _stall2 = p2.ability == "あとだし"
    if _stall1 != _stall2:
        return _stall2  # 相手があとだし→自分が先攻
    # クイックドロウ: 30%で同じ優先度の中で最初に行動する
    _qd1 = p1.ability == "クイックドロウ" and random.random() < 0.30
    _qd2 = p2.ability == "クイックドロウ" and random.random() < 0.30
    if _qd1 and not _qd2:
        return True
    if _qd2 and not _qd1:
        return False

    spd1 = p1.get_effective_speed()
    spd2 = p2.get_effective_speed()

    # ノーてんき：当事者から無効化フラグを最新化
    field._weather_negated = "ノーてんき" in (p1.ability, p2.ability)
    # 実効天候（ノーてんきで無効・メガソーラー優先、per-poke）
    _w1 = effective_weather(field, p1)
    _w2 = effective_weather(field, p2)

    # こだわりスカーフ（ぶきようは道具無効）
    spd1 = math.floor(spd1 * (get_speed_item_multiplier(p1.item) if p1.ability != "ぶきよう" else 1.0))
    spd2 = math.floor(spd2 * (get_speed_item_multiplier(p2.item) if p2.ability != "ぶきよう" else 1.0))

    # おいかぜ
    if side1.tailwind: spd1 *= 2
    if side2.tailwind: spd2 *= 2

    # 天候速度補正（各自の実効天候で判定）
    if _w1 == "rain" and p1.ability == "すいすい": spd1 *= 2
    if _w2 == "rain" and p2.ability == "すいすい": spd2 *= 2
    if _w1 == "sunny" and p1.ability == "ようりょくそ": spd1 *= 2
    if _w2 == "sunny" and p2.ability == "ようりょくそ": spd2 *= 2
    if _w1 == "sandstorm" and p1.ability == "すなかき": spd1 *= 2
    if _w2 == "sandstorm" and p2.ability == "すなかき": spd2 *= 2
    if _w1 == "hail" and p1.ability == "ゆきかき": spd1 *= 2
    if _w2 == "hail" and p2.ability == "ゆきかき": spd2 *= 2
    # エレキフィールド: サーフテール
    if getattr(field, "electric_terrain", False):
        if p1.ability == "サーフテール": spd1 *= 2
        if p2.ability == "サーフテール": spd2 *= 2
    # はやあし: 状態異常時 素早さ1.5倍（まひの速度低下も無視）
    if p1.ability == "はやあし" and p1.status is not None: spd1 = int(spd1 * 1.5)
    if p2.ability == "はやあし" and p2.status is not None: spd2 = int(spd2 * 1.5)

    if spd1 == spd2:
        return random.random() < 0.5

    return (spd1 > spd2) if not field.trick_room else (spd1 < spd2)


def _entry_effects(poke: BattlePokemon, side_idx: int, field: BattleField,
                   opponent: BattlePokemon, logs: Optional[List[str]] = None,
                   party: Optional[List[BattlePokemon]] = None):
    """場に出たときの効果"""
    if logs is None:
        logs = []
    poke.turns_out = 0
    poke.times_hit = 0
    # _switched_this_turn は switch_to が True にし end_of_turn が False に戻す（=交代したターン中だけTrue）。
    # ここで False に上書きすると switch_to の直後に打ち消され、はりこみ/ねこだまし判定が壊れる（出さない）。
    poke._pivot_out = False           # type: ignore
    poke._force_switch = False        # type: ignore

    immune_to_ground = ("ひこう" in (poke.type1, poke.type2) or poke.ability in ("ふゆう", "うなぎのぼり"))

    # ステルスロック（マジックガード無効）
    if field.stealth_rock[side_idx] and poke.ability != "マジックガード":
        eff = get_type_effectiveness("いわ", poke.type1, poke.type2)
        dmg = max(1, math.floor(poke.max_hp * eff / 8))
        poke.take_damage(dmg)
        if dmg > 0:
            logs.append(f"{poke.name} はステルスロックの効果を受けた！({dmg})")

    # スパイクス（ひこう免疫・マジックガード無効）
    if field.spikes[side_idx] and not immune_to_ground and poke.ability != "マジックガード":
        rate = {1: 1/8, 2: 1/6, 3: 1/4}[field.spikes[side_idx]]
        dmg = max(1, math.floor(poke.max_hp * rate))
        poke.take_damage(dmg)
        logs.append(f"{poke.name} は まきびし のダメージを受けた！({dmg})")

    # どくびし（ひこう・はがね・どく免疫）
    if field.toxic_spikes[side_idx] and not immune_to_ground and poke.ability != "マジックガード":
        if "どく" in (poke.type1, poke.type2):
            field.toxic_spikes[side_idx] = 0
            logs.append(f"{poke.name} が どくびし を吸収した！")
        elif "はがね" not in (poke.type1, poke.type2):
            layers = field.toxic_spikes[side_idx]
            status = "badpoison" if layers >= 2 else "poison"
            if poke.apply_status(status):
                logs.append(f"{poke.name} は どくびし で {'もうどく' if status == 'badpoison' else 'どく'} になった！")

    # ねばねばネット（ひこう・ふゆう免疫）
    if field.sticky_web[side_idx] and not immune_to_ground:
        old_s = poke.stage_speed
        poke.stage_speed = max(-6, poke.stage_speed - 1)
        if poke.stage_speed != old_s:
            logs.append(f"{poke.name} は ねばねばネット で すばやさ が下がった！")

    # がんじょう: 設置物で倒れない
    if poke.ability == "がんじょう" and not poke.is_alive:
        poke.hp = 1
        poke.is_alive = True

    # いやしのねがい（前のポケモンが使用済みなら全回復）
    # BattleSideは渡されないため、Battle._do_action から別途処理
    # イリュージョン: 場に出たとき最後尾の生存ポケモンに化ける
    if poke.ability == "イリュージョン" and party:
        disguise = next(
            (p for p in reversed(party) if p.is_alive and p is not poke), None
        )
        if disguise:
            poke._illusion_name = disguise.name  # type: ignore

    # 特性による入場効果（abilities.pyへ委譲）
    entry_logs = entry_ability(poke, opponent, field)
    logs.extend(entry_logs)


def _best_faint_switch(side: BattleSide, opp: BattlePokemon, field=None) -> Optional[int]:
    """倒れた後の最適交代先インデックスを返す（相手に最も有利な控えを選択）。
    反撃KO（相手より速く、現在HPを最大打点で削り切れる控え）が居れば最優先する。"""
    benched = [(i, p) for i, p in enumerate(side.party)
               if p.is_alive and i != side.active_idx]
    if not benched:
        return None
    fld = field if field is not None else BattleField()

    def _eff_spd(p: BattlePokemon) -> float:
        s = float(p.speed)
        if getattr(p, "item", None) == "こだわりスカーフ":
            s *= 1.5
        if p.status == "paralysis" and p.ability != "はやあし":
            s *= 0.5
        if field is not None:
            w = effective_weather(fld, p); ab = getattr(p, "ability", None)
            if (ab == "すいすい" and w == "rain") or (ab == "すなかき" and w == "sandstorm") \
               or (ab == "ようりょくそ" and w == "sunny") or (ab == "ゆきかき" and w in ("hail", "snow")):
                s *= 2
        return s

    def _can_revenge(p: BattlePokemon) -> bool:
        # 相手より速く、最大打点で相手の現在HPを削り切れる（HPの減った相手を先制で倒す）
        if _eff_spd(p) <= _eff_spd(opp):
            return False
        # ばけのかわ未破壊なら1発目は通らないので反撃KOは成立しない
        if opp.ability == "ばけのかわ" and not getattr(opp, "_disguise_broken", False):
            return False
        best = 0.0
        for mv in p.moves:
            if mv and mv.category != "status" and (mv.power or 0) > 0:
                try:
                    # 第6引数は正規化ロール。最低ロールは 0.0（0.85 は実効0.9775＝ほぼ最高値）
                    best = max(best, calc_damage(p, opp, mv, fld, False, 0.0))
                except Exception:
                    pass
        return best >= opp.hp

    def score(p: BattlePokemon) -> float:
        has_se = any(
            get_type_effectiveness(mv.type, opp.type1, opp.type2) >= 2.0
            for mv in p.moves if mv and mv.category != "status" and mv.power
        )
        opp_max_eff = max(
            (get_type_effectiveness(t, p.type1, p.type2) for t in [opp.type1, opp.type2] if t),
            default=1.0
        )
        s = 0.0
        if has_se:
            s += 2
        if opp_max_eff <= 0.5:
            s += 2
        elif opp_max_eff <= 1.0:
            s += 1
        elif opp_max_eff >= 2.0:
            s -= 2
        rev = 100000 if _can_revenge(p) else 0   # 反撃KOは最優先
        return rev + s * 1000 + p.hp / max(1, p.max_hp) * 10

    return max(benched, key=lambda x: score(x[1]))[0]


def _choose_pivot_target(side: BattleSide, opp: BattlePokemon, is_baton: bool = False) -> Optional[int]:
    """ピボット技（とんぼがえり/バトンタッチ等）の交代先を選ぶ。
    バトン: 積みを活かせるエース（攻撃実数値が高い・メガ）を優先。
    通常ピボット: 相手に有利な控え（_best_faint_switch）。"""
    benched = [(i, p) for i, p in enumerate(side.party)
               if p.is_alive and i != side.active_idx]
    if not benched:
        return None
    if is_baton:
        def bscore(p: BattlePokemon) -> float:
            v = float(max(p.attack, p.sp_attack))
            if p.mega_data is not None:
                v *= 1.2
            return v
        return max(benched, key=lambda x: bscore(x[1]))[0]
    return _best_faint_switch(side, opp)


def _aegislash_to_blade(poke: BattlePokemon, logs: List[str]) -> None:
    if getattr(poke, '_in_blade_forme', False):
        return
    poke._shield_atk   = poke.attack      # type: ignore
    poke._shield_def   = poke.defense     # type: ignore
    poke._shield_spatk = poke.sp_attack   # type: ignore
    poke._shield_spdef = poke.sp_defense  # type: ignore
    # ブレードフォルム種族値(Atk=150,Def=50,SpAtk=150,SpDef=50)で再計算
    from .pokemon import calc_stat, NATURE_MODS
    ev = getattr(poke, 'evs', {}) or {}
    nature_up, nature_dn = NATURE_MODS.get(getattr(poke, 'nature', ''), (None, None))
    def _nat(key: str) -> float:
        return 1.1 if nature_up == key else (0.9 if nature_dn == key else 1.0)
    poke.attack     = calc_stat(150, ev.get('A', 0), 31, _nat('attack'))
    poke.defense    = calc_stat(50,  ev.get('B', 0), 31, _nat('defense'))
    poke.sp_attack  = calc_stat(150, ev.get('C', 0), 31, _nat('sp_attack'))
    poke.sp_defense = calc_stat(50,  ev.get('D', 0), 31, _nat('sp_defense'))
    if poke.ability == 'はりきり':
        poke.attack = math.floor(poke.attack * 1.5)
    poke._in_blade_forme = True           # type: ignore
    logs.append(f"{poke.name} は ブレードフォルム に変化した！")


def _aegislash_to_shield(poke: BattlePokemon, logs: List[str]) -> None:
    if not getattr(poke, '_in_blade_forme', False):
        return
    poke.attack     = poke._shield_atk    # type: ignore
    poke.defense    = poke._shield_def    # type: ignore
    poke.sp_attack  = poke._shield_spatk  # type: ignore
    poke.sp_defense = poke._shield_spdef  # type: ignore
    poke._in_blade_forme = False          # type: ignore
    logs.append(f"{poke.name} は シールドフォルム に変化した！")


def _execute_move(
    attacker_side: BattleSide, defender_side: BattleSide,
    action: Action, field: BattleField,
    opp_action: Optional[Action] = None,
) -> List[str]:
    logs = []
    attacker = attacker_side.active
    defender = defender_side.active
    move = action.move

    if move is None:
        return logs

    attacker.flinched = False
    attacker.last_used_move = move.name_jp
    attacker._last_move_obj = move  # type: ignore  # まねっこ用：直前技のMoveData
    if move.name_jp != "とっておき":
        attacker.used_moves.add(move.name_jp)

    # 技の選択を相手に公開（結果に関わらず）
    logs.extend(defender_side.opp_view.on_move(attacker.name, move.name_jp))

    # リチャージ（ギガインパクト・ブラストバーン等の次ターン行動不能）
    if getattr(attacker, 'recharge', False):
        attacker.recharge = False
        logs.append(f"{attacker.name} は動けない！")
        return logs

    # ねごと（ねむり中に別技を選んで使う）
    if move.name_jp == "ねごと":
        if attacker.status != "sleep":
            logs.append(f"{attacker.name} の ねごと は失敗した！（ねむり状態でない）")
            return logs
        usable = [m for m in attacker.moves if m and m.category != "status"]
        if not usable:
            logs.append(f"{attacker.name} の ねごと は失敗した！")
            return logs
        selected = random.choice(usable)
        logs.append(f"{attacker.name} は ねごと で {selected.name_jp} を使った！")
        saved_status, saved_count = attacker.status, attacker.sleep_count
        attacker.status = None
        fake_action = Action(type="move", move=selected)
        logs.extend(_execute_move(attacker_side, defender_side, fake_action, field, opp_action))
        if attacker.status is None:
            attacker.status = saved_status
            attacker.sleep_count = saved_count
        return logs

    # ちょうはつ中は変化技失敗
    if move.category == "status" and attacker.taunt_count > 0:
        logs.append(f"{attacker.name} は ちょうはつ 中で {move.name_jp} が使えない！")
        attacker.taunt_count = max(0, attacker.taunt_count - 1)
        return logs

    # じごくづき中は音技失敗
    from .damage import SOUND_MOVES as _SOUND_MOVES_CHECK
    if attacker.throat_chop_count > 0 and move.name_jp in _SOUND_MOVES_CHECK:
        logs.append(f"{attacker.name} は じごくづき 状態で {move.name_jp} が使えない！")
        return logs

    # アンコール中は指定技のみ
    if attacker.encore_count > 0 and attacker.locked_move:
        if move.name_jp != attacker.locked_move:
            # AIが違う技を選んだ場合、locked_moveに差し替え（簡易）
            from .data import DataLoader
            pass  # AIが正しいmoveを選ぶことを期待
        attacker.encore_count -= 1
        if attacker.encore_count == 0:
            attacker.locked_move = None

    # ふういん・のろわれボディによる封じチェック
    if attacker.disabled_move and move.name_jp == attacker.disabled_move:
        logs.append(f"{attacker.name} の {move.name_jp} は封じられている！")
        return logs

    # まひ行動不能チェック (25%)
    if attacker.status == "paralysis" and random.random() < 0.25:
        logs.append(f"{attacker.name} はからだがしびれて うごけない！")
        return logs

    # ねむりチェック
    if attacker.status == "sleep":
        # はやおき: 2倍の早さで目覚める（カウントを2減らす）
        attacker.sleep_count -= 2 if attacker.ability == "はやおき" else 1
        if attacker.sleep_count > 0:
            # いびき・ねごとはねむり中でも使える
            if move.name_jp in ("いびき", "ねごと"):
                logs.append(f"{attacker.name} はねむりながら {move.name_jp} を使った！")
            else:
                attacker.charging_move = None   # 眠ると溜め技(ソーラービーム等)は解除される
                logs.append(f"{attacker.name} はねむっている…")
                return logs
        else:
            attacker.status = None
            logs.append(f"{attacker.name} は目を覚ました！")

    # こおりチェック (20% で解除)
    if attacker.status == "freeze":
        # 解凍техн: 使うと自分のこおりを治して行動できる（もえつきる/ねっとう/ねっさのだいち等）
        THAW_MOVES = {"もえつきる", "ねっとう", "ねっさのだいち", "せいなるほのお"}
        if move.name_jp in THAW_MOVES:
            attacker.status = None
            logs.append(f"{attacker.name} は {move.name_jp} でこおりがとけた！")
        elif random.random() < 0.2:
            attacker.status = None
            logs.append(f"{attacker.name} のこおりがとけた！")
        else:
            logs.append(f"{attacker.name} はこおっている！")
            return logs

    # こんらんチェック
    if attacker.confused:
        if random.random() < 0.33:
            logs.append(f"{attacker.name} はこんらんして自分を傷つけた！")
            self_dmg = max(1, math.floor(
                (math.floor(math.floor(2 * 50 / 5 + 2) * 40 * attacker.attack / attacker.defense) / 50) + 2
            ))
            attacker.take_damage(self_dmg)
            return logs

    # まもる / キングシールド / ニードルガード / こらえる
    # 連続成功回数 n 回後の成功率 = (1/3)^n
    if move.name_jp in ("まもる", "キングシールド", "ニードルガード", "みきり", "こらえる", "トーチカ"):
        n = attacker.protect_consecutive
        success_rate = (1 / 3) ** n
        if n > 0 and random.random() >= success_rate:
            logs.append(f"{attacker.name} の{move.name_jp} は失敗した！")
            attacker.protect_consecutive += 1
            return logs
        # こらえるは攻撃を通すがHP1で耐える（まもる系の全無効とは別挙動）
        if move.name_jp == "こらえる":
            attacker.enduring = True
            attacker.protect_consecutive += 1
            logs.append(f"{attacker.name} は こらえる 構えをした！")
            return logs
        attacker.protecting = True
        attacker._protect_move = move.name_jp  # type: ignore
        attacker.protect_consecutive += 1
        logs.append(f"{attacker.name} は身を守っている！")
        if move.name_jp == "キングシールド" and attacker.ability == "バトルスイッチ":
            _aegislash_to_shield(attacker, logs)
        return logs
    else:
        attacker.protect_consecutive = 0

    # スクリーン技
    if move.name_jp == "リフレクター":
        if not attacker_side.reflect:
            attacker_side.reflect = True
            attacker_side.reflect_count = 8 if attacker.item == "ひかりのねんど" else 5
            logs.append(f"リフレクター が張られた！")
        else:
            logs.append(f"リフレクター はすでに効果中！")
        return logs
    if move.name_jp == "ひかりのかべ":
        if not attacker_side.light_screen:
            attacker_side.light_screen = True
            attacker_side.light_screen_count = 8 if attacker.item == "ひかりのねんど" else 5
            logs.append(f"ひかりのかべ が張られた！")
        else:
            logs.append(f"ひかりのかべ はすでに効果中！")
        return logs
    if move.name_jp == "オーロラベール":
        if effective_weather(field, attacker) != "hail":
            logs.append("しかし オーロラベール は失敗した！（ゆき状態でない）")
            return logs
        if not attacker_side.aurora_veil:
            attacker_side.aurora_veil = True
            attacker_side.aurora_veil_count = 8 if attacker.item == "ひかりのねんど" else 5
            logs.append(f"オーロラベール が張られた！")
        else:
            logs.append(f"オーロラベール はすでに効果中！")
        return logs

    # おいかぜ（自分側の素早さ2倍/3ターン）
    if move.name_jp == "おいかぜ":
        if not attacker_side.tailwind:
            attacker_side.tailwind = True
            attacker_side.tailwind_count = 3
            logs.append(f"おいかぜ が吹き始めた！（3ターン）")
        else:
            logs.append(f"おいかぜ はすでに効果中！")
        return logs

    # まきびし設置（最大3層）
    if move.name_jp == "まきびし":
        opp_idx = defender_side.field_idx
        if field.spikes[opp_idx] < 3:
            field.spikes[opp_idx] += 1
            logs.append(f"まきびしが まき散らされた！（{field.spikes[opp_idx]}層）")
        else:
            logs.append(f"まきびしはこれ以上まけない！")
        return logs

    # ステルスロック設置（未設置時のみ）
    if move.name_jp == "ステルスロック":
        if not getattr(defender_side, 'stealth_rock_set', False) and \
           not getattr(defender_side, '_stealth_rock_pending', False):
            defender_side._stealth_rock_pending = True  # type: ignore
            logs.append(f"ステルスロックを まき散らした！")
        else:
            logs.append(f"ステルスロックはすでに設置されている！")
        return logs

    # トリックルーム
    if move.name_jp == "トリックルーム":
        if field.trick_room:
            field.trick_room = False
            field.trick_room_count = 0
            logs.append("トリックルーム が解除された！")
        else:
            field.trick_room = True
            field.trick_room_count = 5
            logs.append("トリックルーム が発動した！")
        return logs

    # あまごい・にほんばれ等（天候岩を持っていれば持続8ターン）
    def _wturns(rock):
        return 8 if attacker.item == rock else 5
    if move.name_jp == "あまごい":
        field.weather = "rain"; field.weather_count = _wturns("しめったいわ")
        logs.append("雨が降り出した！"); return logs
    if move.name_jp == "にほんばれ":
        field.weather = "sunny"; field.weather_count = _wturns("あついいわ")
        logs.append("日差しが強くなった！"); return logs
    if move.name_jp == "すなあらし":
        field.weather = "sandstorm"; field.weather_count = _wturns("さらさらいわ")
        logs.append("砂嵐が吹き始めた！"); return logs
    if move.name_jp == "あられ":
        field.weather = "hail"; field.weather_count = _wturns("つめたいいわ")
        logs.append("あられが降り始めた！"); return logs
    if move.name_jp == "ゆきげしき":
        field.weather = "hail"; field.weather_count = _wturns("つめたいいわ")
        logs.append("雪が降り始めた！"); return logs

    if move.name_jp == "さむいギャグ":
        field.weather = "hail"; field.weather_count = _wturns("つめたいいわ")
        logs.append("さむいギャグ！ 雪が降り始めた！")
        attacker._pivot_out = True  # type: ignore
        return logs

    # 状態異常技
    if move.category == "status":
        # いたずらごころ：あくタイプの相手には変化技が無効（技タイプを問わない）
        if attacker.ability == "いたずらごころ":
            if "あく" in (defender.type1, defender.type2):
                logs.append(f"{defender.name} は あく タイプなので {move.name_jp} は効かない！")
                return logs
        logs.append(f"{attacker.name} は {move.name_jp} を使った！")
        if not check_hit(attacker, defender, move, field):
            if defender.protecting:
                logs.append(f"{attacker.name} の {move.name_jp} は {defender.name} に防がれた！")
            else:
                logs.append(f"{attacker.name} の {move.name_jp} は外れた！")
            return logs
        # おうごんのからだ: 相手に向けた変化技を無効化（自己強化/天候/設置/画面は対象外）
        if defender.ability == "おうごんのからだ" and move.name_jp in _GAG_BLOCK:
            logs.append(f"{defender.name} の おうごんのからだ！ {move.name_jp} は効かない！")
            return logs
        logs += _apply_status_move(attacker, defender, move, field, attacker_side, defender_side)
        return logs

    # ── 特殊技の前処理 ──────────────────────────────────────

    # ねこだまし：場に出た最初のターンのみ使用可（turns_out > 0 は失敗）
    if move.name_jp in ("ねこだまし", "であいがしら") and attacker.turns_out > 0:
        logs.append(f"{attacker.name} の {move.name_jp} は失敗した！（2ターン目以降）")
        return logs

    # ふいうち：相手が今ターン攻撃技を使わない場合は失敗
    if move.name_jp == "ふいうち":
        opp_is_attacking = (
            opp_action is not None
            and opp_action.type == "move"
            and opp_action.move is not None
            and opp_action.move.category != "status"
        )
        if not opp_is_attacking:
            logs.append(f"{attacker.name} の ふいうち は失敗した！")
            return logs

    # ぼうおん: 音技を無効（status技を含む）
    from .damage import SOUND_MOVES
    if move.name_jp in SOUND_MOVES and defender.ability == "ぼうおん":
        logs.append(f"{defender.name} の ぼうおん で {move.name_jp} が効かない！")
        return logs


    # ポルターガイスト：相手が持ち物なしで失敗
    if move.name_jp == "ポルターガイスト" and defender.item is None:
        logs.append(f"{attacker.name} の ポルターガイスト は失敗した！（持ち物なし）")
        return logs

    # なげつける：持ち物なしで失敗。使用後にアイテム消費＆特殊効果
    if move.name_jp == "なげつける":
        if attacker.item is None:
            logs.append(f"{attacker.name} の なげつける は失敗した！（持ち物なし）")
            return logs
        attacker._last_flung_item = attacker.item  # type: ignore
        attacker.item = None

    # じょおうのいげん/テイルアーマー：相手の先制技（優先度+）を受け付けない
    if move.priority > 0 and defender.ability in ("じょおうのいげん", "テイルアーマー"):
        logs.append(f"{defender.name} の {defender.ability}！ 先制技は効かない！")
        return logs

    # しめりけ：場に「しめりけ」がいると爆発技は使えない
    if move.name_jp in ("だいばくはつ", "じばく", "ミストバースト") and "しめりけ" in (attacker.ability, defender.ability):
        logs.append(f"{attacker.name} は {move.name_jp} を使おうとしたが、しめりけ で出せなかった！")
        return logs

    # バトルスイッチ（ギルガルド）：攻撃技使用前にブレードフォルムへ
    if attacker.ability == "バトルスイッチ" and move.category != "status":
        _aegislash_to_blade(attacker, logs)

    # へんげんじざい：技使用前にその技のタイプへ変化。登場するたび1回だけ（交代でリセット）
    if attacker.ability == "へんげんじざい" and not getattr(attacker, "_protean_used", False):
        new_type = move.type
        if attacker.type1 != new_type or attacker.type2 is not None:
            attacker.type1 = new_type
            attacker.type2 = None
            attacker._protean_used = True  # type: ignore
            logs.append(f"{attacker.name} の へんげんじざい で {new_type} タイプになった！")

    # フリーズドライ：みず弱点に2倍（タイプ上書き処理は後で行う）
    # → effective_type_override フラグで処理

    # ── 一撃必殺技 ────────────────────────────────────────
    OHKO_MOVES = {"ぜったいれいど", "ハサミギロチン", "つのドリル", "じわれ"}
    if move.name_jp in OHKO_MOVES:
        if move.name_jp == "ぜったいれいど" and "こおり" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        if move.name_jp == "じわれ" and "ひこう" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        if move.name_jp in ("つのドリル", "ハサミギロチン") and "ゴースト" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        if not check_hit(attacker, defender, move, field):
            logs.append(f"{attacker.name} の {move.name_jp} は外れた！")
            return logs
        if defender.item == "きあいのタスキ" and defender.hp == defender.max_hp:
            defender.item = None
            on_item_consumed(defender, logs)
            logs.append(f"{defender.name} のきあいのタスキ で耐えた！")
            defender.hp = 1
        elif defender.ability == "がんじょう" and defender.hp == defender.max_hp:
            logs.append(f"{defender.name} の がんじょう で耐えた！")
            defender.hp = 1
        elif defender.item == "きあいのハチマキ" and random.random() < 0.10:
            logs.append(f"{defender.name} の きあいのハチマキ で耐えた！")
            defender.hp = 1
        else:
            overkill = defender.hp
            defender.hp = 0
            defender.is_alive = False
            logs.append(f"一撃必殺！ {defender.name} は倒れた！")
            on_defender_ko(attacker, defender, overkill, logs)
            on_ko(attacker, logs)
        return logs

    # ── 溜め技（2ターン攻撃） ────────────────────────────
    TWO_TURN_MOVES = {"ソーラービーム", "ソーラーブレード", "あなをほる", "そらをとぶ", "ダイビング", "エレクトロビーム", "ゴッドバード", "とびはねる", "メテオビーム", "ゴーストダイブ"}
    if move.name_jp in TWO_TURN_MOVES:
        # ソーラービーム/ブレードは晴れ中即時発動、エレクトロビームは雨中即時発動
        instant = (move.name_jp in ("ソーラービーム", "ソーラーブレード")
                   and effective_weather(field, attacker) == "sunny")
        instant = instant or (move.name_jp == "エレクトロビーム" and effective_weather(field, attacker) == "rain")
        if not instant:
            if attacker.charging_move is None:
                attacker.charging_move = move.name_jp
                charge_msg = {
                    "ソーラービーム":    "エネルギーを溜めている！",
                    "ソーラーブレード": "エネルギーを溜めている！",
                    "あなをほる":        "地面に潜った！",
                    "そらをとぶ":        "空高く飛び上がった！",
                    "ダイビング":        "水中に潜った！",
                    "エレクトロビーム": "エネルギーをチャージした！",
                    "ゴッドバード":      "ゴッドバードの準備をしている！",
                    "とびはねる":        "空高く飛び上がった！",
                    "メテオビーム":      "エネルギーを溜めている！",
                }.get(move.name_jp, "ためている！")
                logs.append(f"{attacker.name} は {charge_msg}")
                if move.name_jp in ("エレクトロビーム", "メテオビーム"):
                    attacker.stage_sp_attack = min(6, attacker.stage_sp_attack + 1)
                    logs.append(f"{attacker.name} の とくこう が上がった！")
                return logs
            else:
                attacker.charging_move = None  # 攻撃ターン：溜め解除して続行
        if instant and move.name_jp == "エレクトロビーム":
            attacker.stage_sp_attack = min(6, attacker.stage_sp_attack + 1)
            logs.append(f"{attacker.name} の とくこう が上がった！")

    # くちばしキャノンが自分で行動する＝もう被弾準備は不要（解除）
    if move.name_jp == "くちばしキャノン":
        attacker._beak_primed = False

    # フェイント・ゴーストダイブ：まもるを解除して攻撃
    if move.name_jp in ("フェイント", "ゴーストダイブ") and defender.protecting:
        defender.protecting = False
        logs.append(f"{defender.name} の まもり が解除された！")

    # ふかしのこぶし／かんつうドリル：接触技は相手の守りを無視し、本来の1/4ダメージを与える
    # （守り以外の効果は発動。両特性とも同一の効果）
    attacker._pierce_quarter = False  # type: ignore
    if defender.protecting and is_contact_move(move) and attacker.ability in ("ふかしのこぶし", "かんつうドリル"):
        defender.protecting = False
        attacker._pierce_quarter = True  # type: ignore
        logs.append(f"{attacker.name} の {attacker.ability}！ 守りを無視して攻撃した！")

    # きあいパンチ：行動前に技ダメージを受けていると失敗（優先度-3で後攻のため成立しやすい）
    if move.name_jp == "きあいパンチ" and getattr(attacker, '_took_damage_this_turn', False):
        logs.append(f"{attacker.name} は きあいパンチ に集中できなかった！")
        return logs

    # もえつきる：自分がほのおタイプでないと失敗
    if move.name_jp == "もえつきる" and "ほのお" not in (attacker.type1, attacker.type2):
        logs.append(f"{attacker.name} の もえつきる は失敗した！（ほのおタイプではない）")
        return logs

    # ゲップ：戦闘中にきのみを食べていないと失敗
    if move.name_jp == "ゲップ" and not getattr(attacker, 'ate_berry', False):
        logs.append(f"{attacker.name} の ゲップ は失敗した！（きのみを食べていない）")
        return logs

    # いびき・ねごと：自分がねむり状態でないと失敗
    if move.name_jp in ("いびき", "ねごと") and attacker.status != "sleep":
        logs.append(f"{attacker.name} の {move.name_jp} は失敗した！（ねむっていない）")
        return logs

    # デカハンマー：2ターン連続では使えない
    if move.name_jp == "デカハンマー":
        if attacker._deka_last:
            attacker._deka_last = False
            logs.append(f"{attacker.name} の デカハンマー は失敗した！（連続使用不可）")
            return logs
        attacker._deka_last = True
    else:
        attacker._deka_last = False

    # とっておき：他に覚えている技を全て使っていないと失敗
    if move.name_jp == "とっておき":
        others = {m.name_jp for m in attacker.moves if m and m.name_jp != "とっておき"}
        if not others or not others.issubset(attacker.used_moves):
            logs.append(f"{attacker.name} の とっておき は失敗した！（他の技を使い切っていない）")
            return logs

    # はやてがえし：相手が先制技（優先度+）を選んでいないと失敗
    if move.name_jp == "はやてがえし":
        opp_pri = (opp_action.move.priority
                   if opp_action and opp_action.type == "move" and opp_action.move else 0)
        if opp_pri <= 0:
            logs.append(f"{attacker.name} の はやてがえし は失敗した！（相手が先制技を使っていない）")
            return logs

    # アイアンローラー：場にフィールドがないと失敗
    if move.name_jp == "アイアンローラー" and field is not None:
        if not (field.grassy_terrain or field.electric_terrain
                or field.psychic_terrain or field.misty_terrain):
            logs.append(f"{attacker.name} の アイアンローラー は失敗した！（フィールドがない）")
            return logs

    # みらいよち：相手の場に予約し、2ターン後に発動（ダメージは使用時のステータスで先に算出）
    if move.name_jp == "みらいよち":
        if defender_side.future_sight_count > 0:
            logs.append(f"{attacker.name} の みらいよち は失敗した！")
            return logs
        # random_roll は正規化値（実ロール = 0.85 + x*0.15）。平均ロール0.925は 0.5 を渡す。
        # 0.925 を渡すと実効0.98875＝ほぼ最高値になる。
        defender_side.future_sight_dmg = calc_damage(attacker, defender, move, field, random_roll=0.5)
        defender_side.future_sight_count = 2
        defender_side.future_sight_name = attacker.name
        logs.append(f"{attacker.name} は みらいよち を放った！")
        return logs

    # ダメージ技
    if not check_hit(attacker, defender, move, field):
        if defender.protecting:
            logs.append(f"{attacker.name} の {move.name_jp} は {defender.name} に防がれた！")
            _pmove = getattr(defender, '_protect_move', None)
            # キングシールド：接触技で攻撃してきた相手の攻撃-1
            if _pmove == "キングシールド" and is_contact_move(move) and attacker.ability != "えんかく":
                if attacker.ability not in ("かたやぶり", "ターボブレイズ", "テラボルテージ"):
                    old_a = attacker.stage_attack
                    attacker.stage_attack = max(-6, attacker.stage_attack - 1)
                    if attacker.stage_attack != old_a:
                        logs.append(f"{defender.name} の キングシールド！ {attacker.name} の攻撃が下がった！")
            # トーチカ：接触技で攻撃してきた相手をどく
            if _pmove == "トーチカ" and is_contact_move(move) and attacker.ability != "えんかく":
                if defender.is_alive and attacker.is_alive:
                    if attacker.apply_status("poison"):
                        logs.append(f"{defender.name} の トーチカ！ {attacker.name} は どく になった！")
            # ニードルガード：接触技で攻撃してきた相手に最大HP1/8ダメージ
            if _pmove == "ニードルガード" and is_contact_move(move) and attacker.ability != "えんかく" and attacker.is_alive:
                nd = max(1, attacker.max_hp // 8)
                attacker.take_damage(nd)
                logs.append(f"{defender.name} の ニードルガード！ {attacker.name} に {nd} のダメージ！")
        else:
            logs.append(f"{attacker.name} の {move.name_jp} は外れた！")
            attacker._move_failed_this_turn = True  # じだんだ/やけっぱち：技を外した（ターン終了時に繰り越す）
            # とびひざげり・とびげり・かかとおとし・サンダーダイブは外れると最大HP1/2ダメ
            if move.name_jp in ("とびひざげり", "とびげり", "かかとおとし", "サンダーダイブ"):
                recoil = max(1, attacker.max_hp // 2)
                attacker.take_damage(recoil)
                logs.append(f"{attacker.name} は激しく地面に叩きつけられた！({recoil})")
        return logs

    # タイプ無効（スキン系・ウェザーボール等の実効タイプで判定）
    _eff_type = _effective_move_type(attacker, move, field)
    eff = get_type_effectiveness(_eff_type, defender.type1, defender.type2)
    # フリーズドライ：みずタイプに2倍（通常こおりはみずに0.5倍）
    if move.name_jp == "フリーズドライ" and "みず" in (defender.type1, defender.type2):
        eff = max(eff, 2.0)  # みず弱点を優先
    if eff == 0:
        logs.append(f"{move.name_jp} は {defender.name} に効かない…")
        return logs

    # ばけのかわ（ミミッキュ）：初回ダメージ無効（ピボット技は交代フラグだけ立てて続行）
    if defender.ability == "ばけのかわ" and not getattr(defender, '_disguise_broken', False):
        defender._disguise_broken = True  # type: ignore
        dmg_penalty = max(1, math.floor(defender.max_hp / 8))
        defender.take_damage(dmg_penalty)
        logs.append(f"{defender.name} の ばけのかわ が破れた！({dmg_penalty})")
        PIVOT_MOVES = {"ボルトチェンジ", "とんぼがえり", "クイックターン"}
        if move.name_jp in PIVOT_MOVES and attacker.is_alive:
            attacker._pivot_out = True  # type: ignore
        return logs

    # カウンター / ミラーコート / メタルバースト / ほうふく
    if move.name_jp in ("カウンター", "ミラーコート", "メタルバースト", "ほうふく"):
        if move.name_jp == "カウンター":
            base = getattr(attacker, '_last_physical_dmg_received', 0)
            ret_dmg = base * 2
        elif move.name_jp == "ミラーコート":
            base = getattr(attacker, '_last_special_dmg_received', 0)
            ret_dmg = base * 2
        else:  # メタルバースト・ほうふく：物理+特殊合算×1.5
            base = (getattr(attacker, '_last_physical_dmg_received', 0)
                    + getattr(attacker, '_last_special_dmg_received', 0))
            ret_dmg = math.floor(base * 1.5)
        if ret_dmg <= 0:
            logs.append(f"{attacker.name} の {move.name_jp} は失敗した！")
            return logs
        if defender.item == "きあいのタスキ" and defender.hp == defender.max_hp and ret_dmg >= defender.hp:
            ret_dmg = defender.hp - 1
            defender.item = None
            on_item_consumed(defender, logs)
            logs.append(f"{defender.name} のきあいのタスキ で耐えた！")
            logs.extend(attacker_side.opp_view.on_item(defender.name, "きあいのタスキ", "タスキ発動"))
        if defender.ability == "がんじょう" and defender.hp == defender.max_hp and ret_dmg >= defender.hp:
            ret_dmg = defender.hp - 1
            logs.append(f"{defender.name} の がんじょう で耐えた！")
        if defender.item == "きあいのハチマキ" and ret_dmg >= defender.hp and random.random() < 0.10:
            ret_dmg = defender.hp - 1
            logs.append(f"{defender.name} の きあいのハチマキ で耐えた！")
        defender.take_damage(ret_dmg)
        logs.append(f"{attacker.name} の {move.name_jp} → {defender.name} に {ret_dmg}ダメ")
        if not defender.is_alive:
            on_defender_ko(attacker, defender, ret_dmg, logs)
            on_ko(attacker, logs)
        return logs

    # 急所判定
    critical = _check_critical(attacker, move, defender)

    # ヒット数（連続技）
    hits = _calc_hits(move, attacker)

    # スクリーン補正（急所・かたやぶり・すりぬけ・スクリーン破壊技は無視）
    _SCREEN_BREAKERS = {"かわらわり", "レイジングブル", "サイコファング"}
    screen_mult = 1.0
    if (not critical
            and attacker.ability not in ("かたやぶり","ターボブレイズ","テラボルテージ","すりぬけ")
            and move.name_jp not in _SCREEN_BREAKERS):
        if move.category == "physical" and (defender_side.reflect or defender_side.aurora_veil):
            screen_mult = 0.5
        elif move.category == "special" and (defender_side.light_screen or defender_side.aurora_veil):
            screen_mult = 0.5

    total_dmg = 0
    rough_skin_logs: List[str] = []  # さめはだ/てつのとげはダメージログの後にまとめて出力
    for _hit_i in range(hits):
        if not defender.is_alive:
            break
        attacker._multi_hit_index = _hit_i  # type: ignore
        dmg = calc_damage(attacker, defender, move, field, critical)
        if screen_mult < 1.0:
            dmg = max(1, math.floor(dmg * screen_mult))
        # かんつうドリル：守りを貫通した攻撃は本来の1/4ダメージ
        if getattr(attacker, "_pierce_quarter", False):
            dmg = max(1, dmg // 4)

        # みがわり: ダメージを身代わりが吸収
        sub_hp = getattr(defender, '_substitute_hp', 0)
        if sub_hp > 0 and move.name_jp not in ("ぼうふう", "ハイパーボイス"):  # 音技は貫通
            if dmg >= sub_hp:
                defender._substitute_hp = 0  # type: ignore
                logs.append(f"{defender.name} の みがわり が壊れた！")
            else:
                defender._substitute_hp = sub_hp - dmg  # type: ignore
                logs.append(f"{attacker.name} の {move.name_jp} → みがわり に {dmg} ダメ")
            total_dmg += dmg
            continue

        # タスキ
        if defender.item == "きあいのタスキ" and defender.hp == defender.max_hp and dmg >= defender.hp:
            dmg = defender.hp - 1
            defender.item = None
            on_item_consumed(defender, logs)
            logs.append(f"{defender.name} のきあいのタスキ で耐えた！")
            logs.extend(attacker_side.opp_view.on_item(defender.name, "きあいのタスキ", "タスキ発動"))

        # がんじょう（HP満タン時1耐え）
        if defender.ability == "がんじょう" and defender.hp == defender.max_hp and dmg >= defender.hp:
            dmg = defender.hp - 1
            logs.append(f"{defender.name} の がんじょう で耐えた！")
            logs.extend(attacker_side.opp_view.on_ability(defender.name, "がんじょう"))

        # きあいのハチマキ（HP不問・10%で1耐え・消費しない）
        if defender.item == "きあいのハチマキ" and dmg >= defender.hp and random.random() < 0.10:
            dmg = defender.hp - 1
            logs.append(f"{defender.name} の きあいのハチマキ で耐えた！")
            logs.extend(attacker_side.opp_view.on_item(defender.name, "きあいのハチマキ", "ハチマキ発動"))

        defender.take_damage(dmg)
        total_dmg += dmg
        if dmg > 0:
            defender._took_damage_this_turn = True  # type: ignore

        # イリュージョン解除（ダメージを受けたとき）
        if getattr(defender, '_illusion_name', None):
            logs.append(f"イリュージョンが解けた！{defender._illusion_name} の正体は {defender.name} だった！")
            defender._illusion_name = None  # type: ignore

        if move.category == "physical":
            defender._last_physical_dmg_received = getattr(defender, '_last_physical_dmg_received', 0) + dmg  # type: ignore
        elif move.category == "special":
            defender._last_special_dmg_received = getattr(defender, '_last_special_dmg_received', 0) + dmg  # type: ignore

        # いのちのたま反動
        if attacker.item == "いのちのたま" and move.category != "status":
            recoil = max(1, math.floor(attacker.max_hp / 10))
            attacker.take_damage(recoil)
            logs.extend(defender_side.opp_view.on_item(attacker.name, "いのちのたま", "反動ダメから判明"))

        # さめはだ/てつのとげ: バッファに収集（ダメージログの後に出力）
        _rough_skin_recoil(attacker, defender, move, rough_skin_logs)

        # くちばしキャノン：弾技を使う前(=このターンまだ行動前)に接触技で被弾→攻撃側やけど
        if getattr(defender, '_beak_primed', False) and is_contact_move(move) and attacker.is_alive:
            if attacker.apply_status("burn"):
                logs.append(f"{defender.name} の くちばしキャノン！ {attacker.name} は やけど した！")

        # ついばむ/むしくい：相手のきのみを食べて効果を得る
        if move.name_jp in ("ついばむ", "むしくい") and attacker.is_alive \
                and defender.item and defender.item.endswith("のみ"):
            _berry = defender.item
            defender.item = None
            attacker.ate_berry = True
            logs.append(f"{attacker.name} は {defender.name} の {_berry} を食べた！")
            if _berry == "オボンのみ":
                _h = attacker.max_hp // 4
                attacker.hp = min(attacker.max_hp, attacker.hp + _h)
                logs.append(f"{attacker.name} は HPが {_h} 回復した！")
            elif _berry == "オレンのみ":
                attacker.hp = min(attacker.max_hp, attacker.hp + 10)
                logs.append(f"{attacker.name} は HPが 10 回復した！")
            elif _berry in ("ラムのみ", "カゴのみ"):
                attacker.status = None
                attacker.bad_poison_count = 0
                attacker.sleep_count = 0
                attacker.confused = False
            elif _berry == "モモンのみ" and attacker.status in ("poison", "badpoison"):
                attacker.status = None
                attacker.bad_poison_count = 0
            elif _berry == "チーゴのみ" and attacker.status == "burn":
                attacker.status = None
            else:
                _QB = {"カムラのみ": "speed", "サルのみ": "sp_attack",
                       "リュガのみ": "defense", "タラプのみ": "sp_defense"}
                if _berry in _QB:
                    _s = _QB[_berry]
                    setattr(attacker, f"stage_{_s}", min(6, getattr(attacker, f"stage_{_s}", 0) + 1))

        # 被弾後特性効果（くだけるよろい・せいでんき等）
        if defender.is_alive:
            on_after_hit(attacker, defender, move, logs)

        # ポイズンタッチ（攻撃側特性：接触技で30%毒）
        if defender.is_alive and attacker.ability == "ポイズンタッチ" and is_contact_move(move):
            if random.random() < 0.30:
                ok = defender.apply_status("poison")
                if ok:
                    logs.append(f"{attacker.name} の ポイズンタッチ！ {defender.name} がどくになった！")
                    from .items import try_cure_berry
                    try_cure_berry(defender, logs)

        # じゃくてんほけん（ばつぐんダメ受けで攻撃・特攻+2、倒れても発動）
        if defender.item == "じゃくてんほけん":
            eff_check = get_type_effectiveness(_eff_type, defender.type1, defender.type2)
            if eff_check >= 2.0:
                defender.stage_attack = min(6, defender.stage_attack + 2)
                defender.stage_sp_attack = min(6, defender.stage_sp_attack + 2)
                defender.item = None
                logs.append(f"{defender.name} の じゃくてんほけん が発動！")

        # 倒した時の特性
        if not defender.is_alive:
            on_defender_ko(attacker, defender, dmg, logs)
            on_ko(attacker, logs)

    if hits > 1:
        logs.append(f"{attacker.name} の {move.name_jp} → {defender.name} に {total_dmg}ダメ ({hits}回)")
    else:
        logs.append(f"{attacker.name} の {move.name_jp} → {defender.name} に {total_dmg}ダメ")

    if critical:
        logs.append("急所に当たった！")
        # いかりのつぼ：急所を受けると攻撃が最大（6段階）になる
        if defender.is_alive and defender.ability == "いかりのつぼ":
            defender.stage_attack = 6
            logs.append(f"{defender.name} の いかりのつぼ！ 攻撃が最大まで上がった！")
    if eff > 1.0:
        logs.append("こうかはばつぐんだ！")
    elif eff < 1.0:
        logs.append("こうかはいまひとつ…")

    # だいばくはつ・じばく：攻撃後に自分はひんしになる
    if move.name_jp in ("だいばくはつ", "じばく") and attacker.is_alive:
        attacker.take_damage(attacker.hp)
        attacker.is_alive = False
        logs.append(f"{attacker.name} は爆発して倒れた！")

    # みちづれ：倒された場合に相手も道連れ
    if not defender.is_alive and defender.destiny_bond and attacker.is_alive:
        attacker.take_damage(attacker.hp)
        attacker.is_alive = False
        logs.append(f"{attacker.name} は みちづれ に巻き込まれた！")

    # かいがらのすず（与えたダメージの1/8回復）
    if attacker.item == "かいがらのすず" and total_dmg > 0 and attacker.is_alive:
        heal = max(1, math.floor(total_dmg / 8))
        attacker.hp = min(attacker.max_hp, attacker.hp + heal)
        logs.append(f"{attacker.name} の かいがらのすず で {heal}HP 回復した！")

    # HP吸収技（ダメージログの後に回復を表示）
    DRAIN_RATES = {
        "ギガドレイン": 0.5, "メガドレイン": 0.5, "すいとる": 0.5,
        "ドレインパンチ": 0.5, "ドレインキッス": 0.75, "きゅうけつ": 0.5,
        "パラボラチャージ": 0.5, "むねんのつるぎ": 0.5, "ウッドホーン": 0.5,
        "シャカシャカほう": 0.5,
    }
    if move.name_jp in DRAIN_RATES and total_dmg > 0 and attacker.is_alive:
        heal = max(1, math.floor(total_dmg * DRAIN_RATES[move.name_jp]))
        if attacker.item == "おおきなねっこ":
            heal = math.floor(heal * 1.3)
        attacker.hp = min(attacker.max_hp, attacker.hp + heal)
        logs.append(f"{attacker.name} は {heal}HP 吸収した！")

    # さめはだ/てつのとげ（ダメージ・効果テキストの後）
    logs.extend(rough_skin_logs)

    # のろわれボディ（ダメージ処理後）
    if defender.is_alive and defender.ability == "のろわれボディ" and random.random() < 0.30:
        if attacker.disabled_move is None:
            attacker.disabled_move = move.name_jp
            attacker.disabled_turns = 3
            logs.append(f"{defender.name} の のろわれボディ！ {attacker.name} の {move.name_jp} が封じられた！")

    # すなはき：技のダメージを受けると5ターン砂嵐
    if defender.ability == "すなはき" and total_dmg > 0 and field.weather != "sandstorm":
        field.weather = "sandstorm"; field.weather_count = 5
        logs.append(f"{defender.name} の すなはき！ すなあらしが５ターン続く！")

    # どくげしょう：物理技のダメージを受けると相手の場をどくびし状態にする
    if defender.ability == "どくげしょう" and move.category == "physical" and total_dmg > 0:
        if field.toxic_spikes[attacker_side.field_idx] < 2:
            field.toxic_spikes[attacker_side.field_idx] += 1
            logs.append(f"{defender.name} の どくげしょう！ {attacker.name} の足元にどくびしがまかれた！")

    # ── 技個別効果（ダメージ後） ────────────────────────────

    # はたきおとす：持ち物消去（damage.py では1.5xで計算済み）（メガストーンは失敗）
    if move.name_jp == "はたきおとす" and defender.is_alive and defender.item:
        if _is_megastone(defender.item):
            logs.append(f"{defender.name} の {defender.item} は叩き落とせなかった！")
        elif defender.ability == "ねんちゃく":
            logs.append(f"{defender.name} は ねんちゃく で道具を落とさなかった！")
        else:
            logs.append(f"{defender.name} の {defender.item} が叩き落とされた！")
            logs.extend(attacker_side.opp_view.on_item(defender.name, defender.item, "はたきおとした"))
            defender.item = None

    # いかりのまえば：相手の現HP50%ダメ（ダメ計算バイパス）・ゴーストタイプ無効
    if move.name_jp == "いかりのまえば" and defender.is_alive:
        if "ゴースト" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        fang_dmg = max(1, defender.hp // 2)
        if defender.item == "きあいのタスキ" and defender.hp == defender.max_hp and fang_dmg >= defender.hp:
            fang_dmg = defender.hp - 1
            defender.item = None
            on_item_consumed(defender, logs)
            logs.append(f"{defender.name} のきあいのタスキ で耐えた！")
        if defender.ability == "がんじょう" and defender.hp == defender.max_hp and fang_dmg >= defender.hp:
            fang_dmg = defender.hp - 1
        if defender.item == "きあいのハチマキ" and fang_dmg >= defender.hp and random.random() < 0.10:
            fang_dmg = defender.hp - 1
            logs.append(f"{defender.name} の きあいのハチマキ で耐えた！")
        defender.take_damage(fang_dmg)
        total_dmg += fang_dmg
        logs.append(f"いかりのまえば で {fang_dmg} ダメ！")

    # ちきゅうなげ：Lv50固定ダメ・ゴーストタイプ無効
    if move.name_jp == "ちきゅうなげ" and defender.is_alive:
        if "ゴースト" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        dmg = 50
        defender.take_damage(dmg)
        total_dmg += dmg
        logs.append(f"ちきゅうなげ で {dmg} ダメ！")

    # ナイトヘッド：Lv50固定ダメ・ノーマル/エスパー無効考慮（ゴースト技なのでノーマル無効）
    if move.name_jp == "ナイトヘッド" and defender.is_alive:
        if "ノーマル" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        dmg = 50
        defender.take_damage(dmg)
        total_dmg += dmg
        logs.append(f"ナイトヘッド で {dmg} ダメ！")

    # いのちがけ：自分のHP分のダメージを与えて自分はひんしになる
    if move.name_jp == "いのちがけ" and defender.is_alive:
        dmg = attacker.hp
        defender.take_damage(dmg)
        total_dmg += dmg
        attacker.take_damage(attacker.hp)
        attacker.is_alive = False
        logs.append(f"いのちがけ で {dmg} ダメ！ {attacker.name} は倒れた！")

    # はきだす：たくわえ回数で威力100/200/300、使用後たくわえ消費
    if move.name_jp == "はきだす" and defender.is_alive:
        if attacker.stockpile_count <= 0:
            logs.append(f"{attacker.name} の はきだす は失敗した！")
            return logs
        power = {1: 100, 2: 200, 3: 300}[attacker.stockpile_count]
        spit = type(move)(**{**move.__dict__, 'power': power})
        sd = calc_damage(attacker, defender, spit, field)
        defender.take_damage(sd)
        total_dmg += sd
        for st in ("stage_defense", "stage_sp_defense"):
            v = getattr(attacker, st, 0)
            setattr(attacker, st, max(-6, v - attacker.stockpile_count))
        attacker.stockpile_count = 0
        logs.append(f"はきだす で {sd} ダメ！")

    # ふくろだたき：手持ちの戦えるポケモン数だけ攻撃（簡易: 数×基礎ダメージ）
    if move.name_jp == "ふくろだたき" and defender.is_alive and attacker_side is not None:
        hits = sum(1 for p in attacker_side.party if p.is_alive and p.status is None)
        hits = max(1, hits)
        base = max(1, attacker.attack // 10)
        fukuro_dmg = base * hits
        defender.take_damage(fukuro_dmg)
        total_dmg += fukuro_dmg
        logs.append(f"ふくろだたき で {hits}回攻撃！ {fukuro_dmg} ダメ！")

    # がむしゃら：相手HPを自分HPに揃える（追加ダメとして処理）・ゴーストタイプ無効
    if move.name_jp == "がむしゃら" and defender.is_alive:
        if "ゴースト" in (defender.type1, defender.type2):
            logs.append(f"{move.name_jp} は {defender.name} に効かない…")
            return logs
        target_hp = attacker.hp
        if defender.hp > target_hp:
            extra = defender.hp - target_hp
            defender.take_damage(extra)
            total_dmg += extra
            logs.append(f"がむしゃら で {extra} 追加ダメ！")

    # すてゼリフ：相手の攻撃・特攻-1 + ピボット
    if move.name_jp == "すてゼリフ" and defender.is_alive:
        for stat in ("stage_attack", "stage_sp_attack"):
            if defender.ability not in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
                old_val = getattr(defender, stat)
                new_val = max(-6, old_val - 1)
                setattr(defender, stat, new_val)
                if new_val != old_val:
                    logs.append(f"{defender.name} の {STAT_JP.get(stat, stat)} が下がった！")
        if attacker.is_alive:
            attacker._pivot_out = True  # type: ignore

    # ピボット技：自分が生存中にひっこむ
    PIVOT_MOVES = {"ボルトチェンジ", "とんぼがえり", "クイックターン"}
    if move.name_jp in PIVOT_MOVES and attacker.is_alive:
        attacker._pivot_out = True  # type: ignore

    # 強制交代技：相手をランダムに交代させる
    FORCE_SWITCH_MOVES = {"ドラゴンテール", "ほえる", "ふきとばし", "ともえなげ"}
    if move.name_jp in FORCE_SWITCH_MOVES and defender.is_alive:
        defender._force_switch = True  # type: ignore

    # 開示情報：相手HPの残り割合と、この技による被ダメージ割合を記録
    # （実数HPは不可視。割合からダメージ計算で相手のEV/性格を逆算する用）
    if total_dmg > 0:
        logs.extend(attacker_side.opp_view.on_hp_change(
            defender.name, defender.hp, defender.max_hp,
            total_dmg, move.name_jp, attacker.name))
        # 推定器(任意): 観測した被ダメージ割合からEV/性格をベイズ更新
        # （攻撃側・場は観測時点の実値。再現不可な特殊ケースは belief 側で安全にスキップ）
        if attacker_side.belief is not None:
            attacker_side.belief.observe_damage(
                defender.name, attacker, move,
                round(total_dmg / defender.max_hp, 3), field)

    # ひけん・ちえなみ / がんせきアックス：倒しても設置（ヒット時100%）
    if total_dmg > 0:
        if move.name_jp == "ひけん・ちえなみ":
            idx = defender_side.field_idx
            if field.spikes[idx] < 3:
                field.spikes[idx] += 1
                logs.append(f"まきびしが まき散らされた！（{field.spikes[idx]}層）")
        elif move.name_jp == "がんせきアックス":
            idx = defender_side.field_idx
            if not field.stealth_rock[idx]:
                field.stealth_rock[idx] = True
                logs.append(f"ステルスロックが まき散らされた！")

    # リチャージ技（ギガインパクト・ブラストバーン）
    RECHARGE_MOVES = {"ギガインパクト", "ブラストバーン", "はかいこうせん",
                      "ハイドロカノン", "ハードプラント", "がんせきほう"}
    if move.name_jp in RECHARGE_MOVES and attacker.is_alive:
        attacker.recharge = True

    # うちおとす：命中後に相手を接地状態にし、でんじふゆう/空中状態を解除
    if move.name_jp == "うちおとす" and total_dmg > 0 and defender.is_alive:
        defender.grounded = True
        defender.magnet_rise = False
        if getattr(defender, 'charging_move', None) in ("そらをとぶ", "とびはねる"):
            defender.charging_move = None
        logs.append(f"{defender.name} は地面に落とされた！")

    # クリアスモッグ：命中後に相手のランク変化リセット
    if move.name_jp == "クリアスモッグ" and total_dmg > 0 and defender.is_alive:
        for attr in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed"):
            setattr(defender, attr, 0)
        logs.append(f"{defender.name} の能力変化がリセットされた！")

    # こうそくスピン/キラースピン：バインド状態・やどりぎのタネ解除
    if move.name_jp in ("こうそくスピン", "キラースピン") and total_dmg > 0 and attacker.is_alive:
        if attacker.bound_count > 0:
            attacker.bound_count = 0
            logs.append(f"{attacker.name} の バインド が解けた！")
        if attacker.seeded:
            attacker.seeded = False
            logs.append(f"{attacker.name} の やどりぎのタネ が解けた！")

    # こうそくスピン：ハザード除去 + 素早さ+1
    if move.name_jp == "こうそくスピン" and total_dmg > 0 and attacker.is_alive and field is not None:
        my_idx = attacker_side.field_idx
        removed = []
        if field.stealth_rock[my_idx]:
            field.stealth_rock[my_idx] = False
            removed.append("ステルスロック")
        if field.spikes[my_idx] > 0:
            field.spikes[my_idx] = 0
            removed.append("まきびし")
        if field.toxic_spikes[my_idx] > 0:
            field.toxic_spikes[my_idx] = 0
            removed.append("どくびし")
        if removed:
            logs.append(f"{attacker.name} の こうそくスピン で {'/'.join(removed)} が吹き飛んだ！")
        old_spd = attacker.stage_speed
        attacker.stage_speed = min(6, attacker.stage_speed + 1)
        if attacker.stage_speed != old_spd:
            logs.append(f"{attacker.name} の すばやさ が上がった！")

    # キラースピン：相手をどく + 自分のバインド/やどりぎ解除（バインド解除は上の共通処理で実施済み）
    if move.name_jp == "キラースピン" and total_dmg > 0 and defender.is_alive:
        if defender.apply_status("poison"):
            logs.append(f"{defender.name} は どく になった！")
            from .items import try_cure_berry as _tcb_ks
            _tcb_ks(defender, logs)

    # フィールド解除（アイススピナー/アイアンローラー）：命中時に場のフィールドを消す
    if move.name_jp in ("アイススピナー", "アイアンローラー") and total_dmg > 0 and field is not None:
        cleared = False
        for fa, fc in [("electric_terrain","electric_terrain_count"),
                       ("psychic_terrain","psychic_terrain_count"),
                       ("misty_terrain","misty_terrain_count"),
                       ("grassy_terrain","grassy_terrain_count")]:
            if getattr(field, fa, False):
                setattr(field, fa, False); setattr(field, fc, 0); cleared = True
        if cleared:
            logs.append(f"{attacker.name} は フィールド を解除した！")

    # 道具奪取（どろぼう/ほしがる）：自分が道具を持たない時、相手の道具を奪う（メガストーンは失敗）
    if move.name_jp in ("どろぼう", "ほしがる") and total_dmg > 0 and attacker.is_alive:
        if attacker.item is None and defender.item is not None:
            if _is_megastone(defender.item) or defender.ability == "ねんちゃく":
                logs.append(f"{defender.name} の {defender.item} は奪えなかった！")
            else:
                attacker.item = defender.item
                logs.append(f"{attacker.name} は {defender.name} の {attacker.item} を奪った！")
                defender.item = None

    # マジシャン：技でダメージを与えると相手の道具を奪う（自分が道具未所持時）
    if attacker.ability == "マジシャン" and total_dmg > 0 and attacker.is_alive \
            and attacker.item is None and defender.item is not None \
            and not _is_megastone(defender.item) and defender.ability != "ねんちゃく":
        attacker.item = defender.item
        defender.item = None
        logs.append(f"{attacker.name} の マジシャン！ {defender.name} の {attacker.item} を奪った！")

    # わるいてぐせ：接触技を受けると相手の道具を盗む（自分が道具未所持時）
    if defender.ability == "わるいてぐせ" and is_contact_move(move) and attacker.ability != "えんかく" and defender.is_alive \
            and defender.item is None and attacker.item is not None \
            and not _is_megastone(attacker.item) and attacker.ability != "ねんちゃく":
        defender.item = attacker.item
        attacker.item = None
        logs.append(f"{defender.name} の わるいてぐせ！ {attacker.name} の {defender.item} を盗んだ！")

    # スクリーン破壊技（レイジングブル/かわらわり/サイコファング）：命中時に相手のスクリーンを壊す
    if move.name_jp in ("レイジングブル", "かわらわり", "サイコファング") and total_dmg > 0 and defender_side is not None:
        screen_removed = []
        if defender_side.reflect:
            defender_side.reflect = False
            defender_side.reflect_count = 0
            screen_removed.append("リフレクター")
        if defender_side.light_screen:
            defender_side.light_screen = False
            defender_side.light_screen_count = 0
            screen_removed.append("ひかりのかべ")
        if defender_side.aurora_veil:
            defender_side.aurora_veil = False
            defender_side.aurora_veil_count = 0
            screen_removed.append("オーロラベール")
        if screen_removed:
            logs.append(f"{attacker.name} の {move.name_jp} で {'/'.join(screen_removed)} が壊れた！")

    # 追加効果（自己能力変化はKO時も発動、defender効果は関数内でガード済み）
    _apply_secondary(attacker, defender, move, total_dmg, logs, field, defender_side)

    # 反動ダメ（すてみ系）
    _apply_recoil(attacker, defender, move, total_dmg, logs)

    # おやこあい（単発技のみ2回目を25%で追撃）：本体ヒットを完全に処理・記録した後に追撃を適用する
    if attacker.ability == "おやこあい" and hits == 1 and total_dmg > 0 and defender.is_alive:
        pb_dmg = max(1, math.floor(total_dmg * 0.25))
        if defender.item == "きあいのタスキ" and defender.hp == defender.max_hp and pb_dmg >= defender.hp:
            pb_dmg = defender.hp - 1
            defender.item = None
            on_item_consumed(defender, logs)
            logs.append(f"{defender.name} のきあいのタスキ で耐えた！（おやこあい2発目）")
        if defender.ability == "がんじょう" and defender.hp == defender.max_hp and pb_dmg >= defender.hp:
            pb_dmg = defender.hp - 1
        if defender.item == "きあいのハチマキ" and pb_dmg >= defender.hp and random.random() < 0.10:
            pb_dmg = defender.hp - 1
            logs.append(f"{defender.name} の きあいのハチマキ で耐えた！")
        defender.take_damage(pb_dmg)
        logs.append(f"おやこあい 追撃！ {pb_dmg}ダメ")
        pb_rough: List[str] = []
        if defender.is_alive:
            on_after_hit(attacker, defender, move, logs)
            _apply_secondary(attacker, defender, move, pb_dmg, logs, field, defender_side)
        _rough_skin_recoil(attacker, defender, move, pb_rough)
        logs.extend(pb_rough)
        _apply_recoil(attacker, defender, move, pb_dmg, logs)
        if not defender.is_alive:
            on_defender_ko(attacker, defender, pb_dmg, logs)
            on_ko(attacker, logs)

    return logs


def _apply_status_move(attacker: BattlePokemon, defender: BattlePokemon,
                       move: MoveData, field: "BattleField" = None,
                       attacker_side: "BattleSide" = None,
                       defender_side: "BattleSide" = None) -> List[str]:
    logs = []
    n = move.name_jp

    # マジックミラー：OPPONENT_DEBUFFS外で個別処理される対人変化技も跳ね返す
    # （ちょうはつ/アンコール/やどりぎのタネ。OPPONENT_DEBUFFS系は下流で跳ね返す）
    if n in ("ちょうはつ", "アンコール", "やどりぎのタネ") and defender.ability == "マジックミラー":
        logs.append(f"{defender.name} の マジックミラー で {n} を跳ね返した！")
        if attacker.ability != "マジックミラー":
            logs += _apply_status_move(defender, attacker, move, field, defender_side, attacker_side)
        return logs

    # ひっくりかえす（相手の能力ランク変化を全て逆転）
    if n == "ひっくりかえす":
        if defender.ability == "マジックミラー" and attacker.ability != "マジックミラー":
            logs.append(f"{defender.name} の マジックミラー で ひっくりかえす を跳ね返した！")
            return logs + _apply_status_move(defender, attacker, move, field, defender_side, attacker_side)
        _stg = ("stage_attack", "stage_defense", "stage_sp_attack", "stage_sp_defense",
                "stage_speed", "stage_accuracy", "stage_evasion")
        changed = False
        for s in _stg:
            v = getattr(defender, s, 0)
            if v != 0:
                setattr(defender, s, -v); changed = True
        logs.append(f"{defender.name} の 能力変化が逆転した！" if changed
                    else f"しかし {defender.name} の 能力に変化がなかった！")
        return logs

    # みがわり（HP1/4消費してみがわりを作る）
    if n == "みがわり":
        cost = attacker.max_hp // 4
        if attacker.hp <= cost:
            logs.append(f"{attacker.name} は HP が足りなくて みがわり を作れない！")
        elif getattr(attacker, '_substitute_hp', 0) > 0:
            logs.append(f"{attacker.name} には すでに みがわり がある！")
        else:
            attacker.hp -= cost
            attacker._substitute_hp = cost  # type: ignore
            logs.append(f"{attacker.name} は みがわり を作った！（HP -{cost}）")
        return logs

    # すてゼリフ（相手の攻撃・特攻-1してピボット）
    if n == "すてゼリフ":
        logs.append(f"{attacker.name} は すてゼリフ を使った！")
        if defender.ability not in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
            for stat in ("stage_attack", "stage_sp_attack"):
                old_val = getattr(defender, stat, 0)
                new_val = max(-6, old_val - 1)
                setattr(defender, stat, new_val)
                if new_val != old_val:
                    logs.append(f"{defender.name} の {STAT_JP.get(stat, stat)} が下がった！")
        attacker._pivot_out = True  # type: ignore
        return logs

    # たくわえる（防御・特防+1、たくわえカウント+1、最大3）
    if n == "たくわえる":
        if attacker.stockpile_count >= 3:
            logs.append(f"{attacker.name} は これ以上 たくわえられない！")
            return logs
        attacker.stockpile_count += 1
        for st in ("stage_defense", "stage_sp_defense"):
            v = getattr(attacker, st, 0)
            if v < 6:
                setattr(attacker, st, v + 1)
        logs.append(f"{attacker.name} は たくわえた！（{attacker.stockpile_count}）")
        return logs

    # のみこむ（たくわえ消費してHP回復：1回1/4, 2回1/2, 3回全回復）
    if n == "のみこむ":
        if attacker.stockpile_count <= 0:
            logs.append(f"{attacker.name} の のみこむ は失敗した！")
            return logs
        ratio = {1: 1/4, 2: 1/2, 3: 1.0}[attacker.stockpile_count]
        heal = attacker.max_hp if ratio >= 1.0 else max(1, math.floor(attacker.max_hp * ratio))
        attacker.hp = min(attacker.max_hp, attacker.hp + heal)
        # たくわえで上げた防御・特防を戻す
        for st in ("stage_defense", "stage_sp_defense"):
            v = getattr(attacker, st, 0)
            setattr(attacker, st, max(-6, v - attacker.stockpile_count))
        attacker.stockpile_count = 0
        logs.append(f"{attacker.name} は のみこんで回復した！")
        return logs

    # ── 回復技 ──────────────────────────────────────────────
    RECOVER_MOVES = {"なまける","じこさいせい","あさのひざし","こうごうせい","つきのひかり",
                     "はねやすめ","タマゴうみ","ミルクのみ"}
    if n in RECOVER_MOVES:
        if attacker.heal_block_count > 0:
            logs.append(f"{attacker.name} は かいふくふうじ で回復できない！")
            return logs
        WEATHER_HEAL_MOVES = {"あさのひざし", "こうごうせい", "つきのひかり"}
        if n in WEATHER_HEAL_MOVES:
            eff_w = effective_weather(field, attacker)
            if eff_w == "sunny":
                heal = attacker.max_hp * 2 // 3
            elif eff_w in ("rain", "sandstorm", "hail"):
                heal = attacker.max_hp // 4
            else:
                heal = attacker.max_hp // 2
        else:
            heal = attacker.max_hp // 2
        attacker.hp = min(attacker.max_hp, attacker.hp + heal)
        logs.append(f"{attacker.name} は体力を回復した！")
        # はねやすめ：このターン中はひこうタイプが消える（じめん技などが通る）
        if n == "はねやすめ" and "ひこう" in (attacker.type1, attacker.type2):
            attacker._roost_types = (attacker.type1, attacker.type2)  # type: ignore
            rem = [t for t in (attacker.type1, attacker.type2) if t and t != "ひこう"]
            attacker.type1 = rem[0] if rem else "ノーマル"
            attacker.type2 = rem[1] if len(rem) > 1 else None
        return logs

    # ねむる：全回復+ねむり（HP満タン・かいふくふうじで失敗）
    if n == "ねむる":
        if attacker.heal_block_count > 0:
            logs.append(f"{attacker.name} は かいふくふうじ で ねむる に失敗した！")
            return logs
        if attacker.hp >= attacker.max_hp:
            logs.append(f"{attacker.name} の ねむる は失敗した！（HP満タン）")
            return logs
        attacker.hp = attacker.max_hp
        attacker.status = "sleep"
        attacker.sleep_count = 2
        attacker.bad_poison_count = 0
        logs.append(f"{attacker.name} はねむって体力を回復した！")
        return logs

    # はらだいこ：HP半分消費してA最大（残りHPが足りないと失敗）
    if n == "はらだいこ":
        if attacker.hp <= attacker.max_hp // 2:
            logs.append(f"{attacker.name} の はらだいこ は失敗した！（HP不足）")
            return logs
        attacker.hp = max(1, attacker.hp - attacker.max_hp // 2)
        attacker.stage_attack = 6
        logs.append(f"{attacker.name} の はらだいこ！ こうげきが最大になった！")
        return logs

    # いたみわけ
    if n == "いたみわけ":
        avg = (attacker.hp + defender.hp) // 2
        attacker.hp = min(attacker.max_hp, avg)
        defender.hp = min(defender.max_hp, avg)
        if defender.hp <= 0:
            defender.hp = 0
            defender.is_alive = False
        logs.append(f"いたみわけ！ お互いのHPが均等になった")
        return logs

    # やどりぎのタネ
    if n == "やどりぎのタネ":
        if "くさ" in (defender.type1, defender.type2):
            logs.append(f"{defender.name} には効かない！")
        else:
            defender.seeded = True
            logs.append(f"{defender.name} に やどりぎのタネ が刺さった！")
        return logs

    # あくび（次ターンねむり）
    if n == "あくび":
        if defender.status is None and not defender.yawn_count:
            if defender.ability not in ("ふみん", "やるき"):
                defender.yawn_count = 2
                logs.append(f"{defender.name} は あくび をした！")
        return logs

    # アンコール
    if n == "アンコール":
        if defender.ability == "アロマベール":
            logs.append(f"{defender.name} は アロマベール で アンコール を防いだ！")
        elif defender.last_used_move and not defender.encore_count:
            defender.encore_count = 3
            defender.locked_move = defender.last_used_move
            logs.append(f"{defender.name} は {defender.last_used_move} を繰り返すことになった！")
        return logs

    # ちょうはつ
    if n == "ちょうはつ":
        if defender.ability == "アロマベール":
            logs.append(f"{defender.name} は アロマベール で ちょうはつ を防いだ！")
        elif not defender.taunt_count:
            defender.taunt_count = 3
            logs.append(f"{defender.name} は ちょうはつ 状態になった！")
        return logs

    # ── 能力変化（自分）────────────────────────────────────
    # きあいだめ（急所ランク+2）
    if n == "きあいだめ":
        attacker.crit_stage = min(3, getattr(attacker, 'crit_stage', 0) + 2)
        logs.append(f"{attacker.name} は きあいだめ した！急所に当たりやすくなった！")
        return logs

    # ドラゴンエール（味方の急所ランク：ドラゴンタイプ+2、それ以外+1）
    if n == "ドラゴンエール":
        bonus = 2 if "ドラゴン" in (attacker.type1, attacker.type2) else 1
        attacker.crit_stage = min(3, getattr(attacker, 'crit_stage', 0) + bonus)
        logs.append(f"{attacker.name} は ドラゴンエール！急所に当たりやすくなった！")
        return logs

    SELF_BOOSTS = {
        "つるぎのまい":   [("stage_attack", 2)],
        "わるだくみ":     [("stage_sp_attack", 2)],
        "りゅうのまい":   [("stage_attack", 1), ("stage_speed", 1)],
        "からをやぶる":   [("stage_attack", 2), ("stage_sp_attack", 2), ("stage_speed", 2),
                           ("stage_defense", -1), ("stage_sp_defense", -1)],
        "めいそう":       [("stage_sp_attack", 1), ("stage_sp_defense", 1)],
        "ちょうのまい":   [("stage_sp_attack", 1), ("stage_sp_defense", 1), ("stage_speed", 1)],
        "はいすいのじん": [("stage_attack", 1), ("stage_defense", 1), ("stage_sp_attack", 1),
                           ("stage_sp_defense", 1), ("stage_speed", 1)],
        "コスモパワー":   [("stage_defense", 1), ("stage_sp_defense", 1)],
        "てっぺき":       [("stage_defense", 2)],
        "ビルドアップ":   [("stage_attack", 1), ("stage_defense", 1)],
        "こうそくいどう": [("stage_speed", 2)],
        "ロックカット":   [("stage_speed", 2)],
        "ドわすれ":       [("stage_sp_defense", 2)],
        "コットンガード": [("stage_defense", 3)],
        "とぐろをまく":   [("stage_attack", 1), ("stage_defense", 1), ("stage_accuracy", 1)],
        "ちいさくなる":   [("stage_evasion", 2)],
        "とける":         [("stage_defense", 2)],
        "たてこもる":     [("stage_defense", 2)],
        "かげぶんしん":   [("stage_evasion", 1)],
    }
    # せいちょう：通常は攻撃・特攻+1、にほんばれ中は+2
    if n == "せいちょう":
        amt = 2 if (field and effective_weather(field, attacker) == "sunny") else 1
        for st in ("stage_attack", "stage_sp_attack"):
            v = getattr(attacker, st, 0)
            setattr(attacker, st, min(6, v + amt))
        logs.append(f"{attacker.name} の 攻撃・特攻 が上がった！")
        return logs

    if n == "はいすいのじん" and attacker.trapped:
        logs.append(f"{attacker.name} は はいすいのじん を使えない！")
        return logs

    if n in SELF_BOOSTS:
        for attr, delta in SELF_BOOSTS[n]:
            _d = -delta if attacker.ability == "あまのじゃく" else delta
            val = getattr(attacker, attr, 0)
            new_val = max(-6, min(6, val + _d))
            setattr(attacker, attr, new_val)
            direction = "上がった" if _d > 0 else "下がった"
            if new_val != val:
                logs.append(f"{attacker.name} の {STAT_JP.get(attr, attr)} が{direction}！")
                # びんじょう：相手の能力上昇をコピー
                if _d > 0 and defender.is_alive and defender.ability == "びんじょう":
                    _ov = getattr(defender, attr, 0)
                    setattr(defender, attr, min(6, _ov + _d))
                    if getattr(defender, attr, 0) != _ov:
                        logs.append(f"{defender.name} の びんじょう！ {STAT_JP.get(attr, attr)} が上がった！")
        if n == "ちいさくなる":
            attacker.minimized = True  # のしかかり等の被弾2倍状態
        if n == "はいすいのじん":
            attacker.trapped = True  # 全能力上昇の代償に交代・逃げ不可
        return logs

    # ── 能力変化（相手）+ 状態異常（status技）────────────────
    STATUS_JP_NAMES = {
        "paralysis": "まひ", "burn": "やけど", "poison": "どく",
        "badpoison": "もうどく", "sleep": "ねむり", "freeze": "こおり",
    }
    # 自己状態付与（単純フラグ）
    SELF_STATE = {
        "ねをはる": "rooted", "アクアリング": "aqua_ring",
        "でんじふゆう": "magnet_rise", "ロックオン": "lock_on", "ふういん": "_sealed",
    }
    if n in SELF_STATE:
        setattr(attacker, SELF_STATE[n], True)
        logs.append(f"{attacker.name} は {n} の状態になった！")
        return logs

    # とおぼえ：自分（と味方）の攻撃+1
    if n == "とおぼえ":
        attacker.stage_attack = min(6, attacker.stage_attack + 1)
        logs.append(f"{attacker.name} の こうげき が上がった！")
        return logs

    # つぼをつく：自分のいずれかの能力ランダム+2
    if n == "つぼをつく":
        stat = random.choice(["stage_attack","stage_defense","stage_sp_attack",
                              "stage_sp_defense","stage_speed","stage_accuracy","stage_evasion"])
        setattr(attacker, stat, min(6, getattr(attacker, stat, 0) + 2))
        logs.append(f"{attacker.name} の {STAT_JP.get(stat, stat)} がぐーんと上がった！")
        return logs

    # じゅうりょく/マジックルーム/ワンダールーム：場の状態（簡易フラグ）
    GLOBAL_ROOM = {"じゅうりょく": "gravity", "マジックルーム": "magic_room",
                   "ワンダールーム": "wonder_room"}
    if n in GLOBAL_ROOM and field is not None:
        setattr(field, GLOBAL_ROOM[n], 5)
        logs.append(f"{n} 状態になった！")
        return logs

    # しんぴのまもり：味方の場（5T状態異常無効）
    if n == "しんぴのまもり" and attacker_side is not None:
        attacker_side.safeguard = 5
        logs.append(f"{attacker.name} の チームは しんぴのまもり に包まれた！")
        return logs

    # ミラータイプ：自分のタイプを相手と同じに
    if n == "ミラータイプ":
        attacker.type1, attacker.type2 = defender.type1, defender.type2
        logs.append(f"{attacker.name} は {defender.name} と同じタイプになった！")
        return logs

    # なかまづくり/なりきり/スキルスワップ：特性操作
    if n == "なかまづくり":
        defender.ability = attacker.ability
        logs.append(f"{defender.name} の とくせい が {attacker.ability} になった！")
        return logs
    if n == "なりきり":
        attacker.ability = defender.ability
        logs.append(f"{attacker.name} は {defender.name} の とくせい をコピーした！")
        return logs
    if n == "スキルスワップ":
        attacker.ability, defender.ability = defender.ability, attacker.ability
        logs.append(f"{attacker.name} と {defender.name} の とくせい が入れ替わった！")
        return logs

    # じこあんじ：相手の能力変化を自分にコピー
    if n == "じこあんじ":
        for st in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                   "stage_speed","stage_accuracy","stage_evasion"):
            setattr(attacker, st, getattr(defender, st, 0))
        logs.append(f"{attacker.name} は {defender.name} の能力変化をコピーした！")
        return logs

    # スピードスワップ/パワースワップ/ガードスワップ：能力変化やステータス入替
    if n == "スピードスワップ":
        attacker.speed, defender.speed = defender.speed, attacker.speed
        logs.append(f"{attacker.name} と {defender.name} の すばやさ が入れ替わった！")
        return logs
    if n == "パワースワップ":
        for st in ("stage_attack","stage_sp_attack"):
            a = getattr(attacker, st, 0); d = getattr(defender, st, 0)
            setattr(attacker, st, d); setattr(defender, st, a)
        logs.append(f"{attacker.name} と {defender.name} の 攻撃系ランク が入れ替わった！")
        return logs
    if n == "ガードスワップ":
        for st in ("stage_defense","stage_sp_defense"):
            a = getattr(attacker, st, 0); d = getattr(defender, st, 0)
            setattr(attacker, st, d); setattr(defender, st, a)
        logs.append(f"{attacker.name} と {defender.name} の 防御系ランク が入れ替わった！")
        return logs
    # パワートリック：自分の攻撃と防御の実数値を入れ替える
    if n == "パワートリック":
        attacker.attack, attacker.defense = attacker.defense, attacker.attack
        logs.append(f"{attacker.name} は こうげき と ぼうぎょ を入れ替えた！")
        return logs
    # ガードシェア/パワーシェア：両者の実数値を合算して半分ずつ
    if n == "ガードシェア":
        for st in ("defense", "sp_defense"):
            avg = (getattr(attacker, st) + getattr(defender, st)) // 2
            setattr(attacker, st, avg); setattr(defender, st, avg)
        logs.append(f"{attacker.name} と {defender.name} の防御を分け合った！")
        return logs
    if n == "パワーシェア":
        for st in ("attack", "sp_attack"):
            avg = (getattr(attacker, st) + getattr(defender, st)) // 2
            setattr(attacker, st, avg); setattr(defender, st, avg)
        logs.append(f"{attacker.name} と {defender.name} の攻撃を分け合った！")
        return logs
    # すりかえ：道具を入れ替える（どちらかがメガストーンを持つ場合は失敗）
    if n == "すりかえ":
        if _is_megastone(attacker.item) or _is_megastone(defender.item):
            logs.append(f"{attacker.name} の すりかえ は失敗した！（メガストーン）")
            return logs
        attacker.item, defender.item = defender.item, attacker.item
        logs.append(f"{attacker.name} と {defender.name} は道具を入れ替えた！")
        return logs
    # グラスフィールド
    if n == "グラスフィールド" and field is not None:
        field.grassy_terrain = True
        field.grassy_terrain_count = 5
        logs.append("足元に草が生い茂った！")
        return logs
    # リサイクル：消費した道具を復元
    if n == "リサイクル":
        consumed = getattr(attacker, '_last_consumed_item', None)
        if attacker.item is None and consumed:
            attacker.item = consumed
            attacker._last_consumed_item = None  # type: ignore
            logs.append(f"{attacker.name} は {attacker.item} を拾った！")
        else:
            logs.append(f"{attacker.name} の リサイクル は失敗した！")
        return logs
    # まねっこ／さいはい：直前に相手が使った技をコピーして使う（_last_move_obj を優先利用）
    if n in ("まねっこ", "さいはい"):
        copy_mv = getattr(defender, "_last_move_obj", None)
        if copy_mv is None:  # フォールバック：相手のmovesから名前一致で取得
            copy_mv = next((m for m in defender.moves if m and m.name_jp == defender.last_used_move), None)
        _UNCOPYABLE = {"まねっこ", "さいはい", "オウムがえし", "ものまね", "スケッチ", "へんしん", "わるあがき"}
        if copy_mv is not None and copy_mv.name_jp not in _UNCOPYABLE:
            logs.append(f"{attacker.name} は {copy_mv.name_jp} をコピーした！")
            logs += _execute_move(attacker_side, defender_side,
                                  Action(type="move", move=copy_mv), field)
        else:
            logs.append(f"{attacker.name} の {n} は失敗した！")
        return logs
    # ねごと：ねむり中のみ、自分の技からランダムに使用
    if n == "ねごと":
        if attacker.status == "sleep":
            cands = [m for m in attacker.moves if m and m.name_jp != "ねごと"]
            if cands:
                chosen = random.choice(cands)
                logs.append(f"{attacker.name} は ねごと で {chosen.name_jp} を使った！")
                logs += _execute_move(attacker_side, defender_side,
                                      Action(type="move", move=chosen), field)
            else:
                logs.append(f"{attacker.name} の ねごと は失敗した！")
        else:
            logs.append(f"{attacker.name} は ねむっていないので ねごと は失敗した！")
        return logs
    # そうでん：相手の次の技をでんきタイプにする（簡易フラグ）
    if n == "そうでん":
        defender._electrified = True  # type: ignore
        logs.append(f"{defender.name} は そうでん された！")
        return logs

    OPPONENT_DEBUFFS: dict = {
        "いかりのこな":   [],
        "どくどく":       [("status", "badpoison")],
        "でんじは":       [("status", "paralysis")],
        "おにび":         [("status", "burn")],
        "ねむりごな":     [("status", "sleep")],
        "さいみんじゅつ": [("status", "sleep")],
        "うたう":         [("status", "sleep")],
        "あやしいひかり": [("confused", True)],
        "ちょうおんぱ":   [("confused", True)],
        "へびにらみ":     [("status", "paralysis")],
        "しびれごな":     [("status", "paralysis")],
        "わたほうし":     [("stage_speed", -2)],
        "フェザーダンス": [("stage_attack", -2)],
        "かいでんぱ":     [("stage_sp_attack", -2)],
        "こわいかお":     [("stage_speed", -2)],
        "つぶらなひとみ": [("stage_attack", -1)],
        "どくのいと":     [("status", "poison"), ("stage_speed", -2)],
        "あまえる":       [("stage_attack", -2)],
        "いとをはく":     [("stage_speed", -2)],
        "いやなおと":     [("stage_defense", -2)],
        "うそなき":       [("stage_sp_defense", -2)],
        "あまいかおり":   [("stage_evasion", -2)],
        "きんぞくおん":   [("stage_sp_defense", -2)],
        "てんしのキッス": [("confused", True)],
        "どくのこな":     [("status", "poison")],
        "おたけび":       [("stage_attack", -1), ("stage_sp_attack", -1)],
        "くすぐる":       [("stage_attack", -1), ("stage_defense", -1)],
        "なみだめ":       [("stage_attack", -1), ("stage_sp_attack", -1)],
        "いばる":         [("stage_attack", 2), ("confused", True)],
        "おだてる":       [("stage_sp_attack", 1), ("confused", True)],
        "メロメロ":       [("infatuation", True)],
        "いちゃもん":     [("torment", True)],
        "くろいまなざし": [("trapped", True)],
        "とおせんぼう":   [("trapped", True)],
        "かげぬい":       [("trapped", True)],
        "いえき":         [("ability_suppressed", True)],
        "シンプルビーム": [("ability_change", "たんじゅん")],
        "なやみのタネ":   [("ability_change", "ふみん")],
        "ハロウィン":     [("type_add", "ゴースト")],
        "もりののろい":   [("type_add", "くさ")],
        "うらみ":         [("pp_reduce", 4)],
        "ぶきみなじゅもん":[("pp_reduce", 3)],
        "デコレーション": [("stage_attack", 2), ("stage_sp_attack", 2)],
        "ハバネロエキス": [("stage_defense", -2), ("stage_attack", 2)],
        "まほうのこな":   [("type_set", "エスパー")],
    }

    # メロメロは性別判定が必要だが本シミュレータは性別を持たないため常に失敗扱い
    if n == "メロメロ":
        logs.append(f"{attacker.name} の メロメロ は失敗した！")
        return logs

    # でんじは：じめんタイプには無効（でんきわざの無効）
    if n == "でんじは" and "じめん" in (defender.type1, defender.type2):
        logs.append(f"{defender.name} には でんじは が効かない！")
        return logs

    # 粉・胞子技：くさタイプ・ぼうじん・ぼうじんゴーグルには無効
    _POWDER = {"ねむりごな", "しびれごな", "どくのこな", "キノコのほうし", "わたほうし", "いかりのこな", "まほうのこな"}
    if n in _POWDER and ("くさ" in (defender.type1, defender.type2)
                         or defender.ability == "ぼうじん"
                         or defender.item == "ぼうじんゴーグル"):
        logs.append(f"{defender.name} には {n} が効かない！（草/防塵）")
        return logs

    if n in OPPONENT_DEBUFFS:
        if defender.ability == "マジックミラー":
            logs.append(f"{defender.name} の マジックミラー で {n} を跳ね返した！")
            # 攻撃側を対象に同じ変化技を適用（跳ね返し）。相手もマジックミラーなら無限反射を防ぐため適用しない
            if attacker.ability != "マジックミラー":
                logs += _apply_status_move(defender, attacker, move, field, defender_side, attacker_side)
            return logs

        _sg = defender_side is not None and getattr(defender_side, 'safeguard', 0) > 0
        for attr, val in OPPONENT_DEBUFFS[n]:
            if attr == "status":
                if _sg:
                    logs.append(f"{defender.name} は しんぴのまもり で状態異常を防いだ！")
                    continue
                if val == "sleep" and defender.ability in ("ふみん", "やるき", "スイートベール"):
                    logs.append(f"{defender.name} の {defender.ability} でねむりを防いだ！")
                    continue
                if defender.ability == "リーフガード" and effective_weather(field, defender) == "sunny":
                    logs.append(f"{defender.name} は リーフガード で状態異常を防いだ！")
                    continue
                ok = defender.apply_status(val, corrosion=(attacker.ability == "ふしょく"))
                if ok:
                    if val == "sleep":
                        defender.sleep_count = random.randint(1, 3)
                    logs.append(f"{defender.name} は {STATUS_JP_NAMES.get(val, val)} になった！")
                    try_cure_berry(defender, logs)
                    # シンクロ：状態異常を相手にも伝染（変化技経由）
                    if defender.ability == "シンクロ" and val in ("poison", "badpoison", "paralysis", "burn") and attacker.is_alive:
                        if attacker.apply_status(val):
                            logs.append(f"{defender.name} の シンクロ！ {attacker.name} にも伝染った！")
                else:
                    logs.append(f"しかし {defender.name} には効かなかった…")
            elif attr == "confused":
                if _sg:
                    logs.append(f"{defender.name} は しんぴのまもり でこんらんを防いだ！")
                elif defender.ability == "マイペース":
                    logs.append(f"{defender.name} の マイペース でこんらんを防いだ！")
                else:
                    defender.confused = True
                    logs.append(f"{defender.name} はこんらんした！")
                    try_cure_berry(defender, logs)
            elif attr.startswith("stage_"):
                # あまのじゃく：対象(defender)自身への能力変化は逆転
                _val = -val if defender.ability == "あまのじゃく" else val
                if _val < 0 and defender.ability in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
                    logs.append(f"{defender.name} の {defender.ability} で能力が下がらなかった！")
                    continue
                old_v = getattr(defender, attr, 0)
                new_v = max(-6, min(6, old_v + _val))
                setattr(defender, attr, new_v)
                if new_v != old_v:
                    direction = "下がった" if _val < 0 else "上がった"
                    logs.append(f"{defender.name} の {STAT_JP.get(attr, attr)} が{direction}！")
                    if _val < 0:
                        from .abilities import on_stat_lowered
                        on_stat_lowered(defender, logs)
            elif attr == "infatuation":
                defender.infatuation = True
                logs.append(f"{defender.name} は メロメロ になった！")
            elif attr == "torment":
                defender.torment = True
                logs.append(f"{defender.name} は いちゃもん 状態になった！")
            elif attr == "trapped":
                defender.trapped = True
                logs.append(f"{defender.name} は逃げられなくなった！")
            elif attr == "ability_suppressed":
                defender.ability_suppressed = True
                logs.append(f"{defender.name} の とくせい が消えた！")
            elif attr == "ability_change":
                defender.ability = val
                logs.append(f"{defender.name} の とくせい が {val} になった！")
            elif attr == "type_add":
                if val not in (defender.type1, defender.type2):
                    if defender.type2 is None:
                        defender.type2 = val
                    else:
                        defender.type1 = val
                    logs.append(f"{defender.name} は {val} タイプが追加された！")
            elif attr == "type_set":
                defender.type1 = val; defender.type2 = None
                logs.append(f"{defender.name} は {val} タイプになった！")
            elif attr == "pp_reduce":
                if defender.last_used_move:
                    for i, mv in enumerate(defender.moves):
                        if mv and mv.name_jp == defender.last_used_move and i < len(defender.pp):
                            defender.pp[i] = max(0, defender.pp[i] - val)
                            logs.append(f"{defender.name} の {mv.name_jp} の PP が {val} 減った！")
                            break
        return logs

    # ── 強制交代（ほえる / ふきとばし）──────────────────────
    if n in ("ほえる", "ふきとばし"):
        blocked = False
        if defender.ability == "マジックミラー":
            logs.append(f"{defender.name} の マジックミラー で {n} を跳ね返した！")
            blocked = True
            # 跳ね返し：攻撃側が追い払われる（相手もマジックミラーなら無効）
            if attacker.ability != "マジックミラー":
                attacker._force_switch = True  # type: ignore
                logs.append(f"{attacker.name} は 跳ね返されて追い払われた！")
        elif defender.ability == "おうごんのからだ":
            logs.append(f"{defender.name} の おうごんのからだ で防いだ！")
            blocked = True
        elif defender.ability == "きゅうばん":
            logs.append(f"{defender.name} の きゅうばん で踏ん張った！")
            blocked = True
        elif n == "ほえる" and defender.ability == "ぼうおん":
            logs.append(f"{defender.name} の ぼうおん で防いだ！")
            blocked = True
        elif n == "ふきとばし" and defender.ability == "かぜのり":
            logs.append(f"{defender.name} の かぜのり で受け流した！")
            blocked = True
        if not blocked:
            for attr in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                         "stage_speed","stage_accuracy","stage_evasion"):
                setattr(defender, attr, 0)
            defender._force_switch = True  # type: ignore
            logs.append(f"{defender.name} は 追い払われた！")
        return logs

    # くろいきり（両者の能力変化リセット）
    if n == "くろいきり":
        for p in [attacker, defender]:
            for attr in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                         "stage_speed","stage_accuracy","stage_evasion"):
                setattr(p, attr, 0)
        logs.append("くろいきり で全ての能力変化がリセットされた！")
        return logs

    # みちづれ：連続使用は失敗（_destiny_bond_last_turn で前ターン使用を記録）
    if n == "みちづれ":
        if getattr(attacker, '_destiny_bond_last_turn', False):
            logs.append(f"{attacker.name} の みちづれ は失敗した！（連続使用）")
            return logs
        attacker.destiny_bond = True
        attacker._destiny_bond_last_turn = True  # type: ignore
        logs.append(f"{attacker.name} は みちづれ にした！")
        return logs

    # ほろびのうた
    if n == "ほろびのうた":
        for p in [attacker, defender]:
            if p.perish_count == 0:
                p.perish_count = 3
                logs.append(f"{p.name} は ほろびのうた を聞いた！")
        return logs

    # ねがいごと
    if n == "ねがいごと" and attacker_side is not None:
        if attacker_side.wish_count == 0:
            attacker_side.wish_hp = attacker.max_hp // 2
            attacker_side.wish_count = 2
            logs.append(f"{attacker.name} は ねがいごと をした！")
        return logs

    # いやしのねがい（自身が倒れ次のポケモンを全回復）
    if n == "いやしのねがい" and attacker_side is not None:
        attacker_side.healing_wish = True
        attacker.take_damage(attacker.hp)
        attacker.is_alive = False
        logs.append(f"{attacker.name} は いやしのねがい を使って倒れた！")
        return logs

    # おきみやげ（相手A・C -2後に自倒）
    if n == "おきみやげ":
        for stat in ("stage_attack", "stage_sp_attack"):
            if defender.ability not in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
                old_v = getattr(defender, stat, 0)
                new_v = max(-6, old_v - 2)
                setattr(defender, stat, new_v)
                if new_v != old_v:
                    logs.append(f"{defender.name} の {STAT_JP.get(stat, stat)} が下がった！")
        attacker.take_damage(attacker.hp)
        attacker.is_alive = False
        logs.append(f"{attacker.name} は おきみやげ を使って倒れた！")
        return logs

    # どくびし
    if n == "どくびし" and defender_side is not None and field is not None:
        idx = defender_side.field_idx
        if field.toxic_spikes[idx] < 2:
            field.toxic_spikes[idx] += 1
            logs.append(f"どくびし が まき散らされた！（{field.toxic_spikes[idx]}層）")
        return logs

    # ねばねばネット
    if n == "ねばねばネット" and defender_side is not None and field is not None:
        idx = defender_side.field_idx
        if not field.sticky_web[idx]:
            field.sticky_web[idx] = True
            logs.append("ねばねばネット が張られた！")
        return logs

    # きりばらい（相手の回避率-1 + 両サイドのハザード・スクリーン解除）
    if n == "きりばらい" and field is not None:
        if defender.ability not in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
            old_ev = defender.stage_evasion
            defender.stage_evasion = max(-6, defender.stage_evasion - 1)
            if defender.stage_evasion != old_ev:
                logs.append(f"{defender.name} の かいひりつ が下がった！")
        for side in ([attacker_side, defender_side] if attacker_side and defender_side else []):
            idx = side.field_idx
            field.spikes[idx] = 0
            field.toxic_spikes[idx] = 0
            field.sticky_web[idx] = False
            field.stealth_rock[idx] = False
            side.reflect = False
            side.light_screen = False
            side.aurora_veil = False
        logs.append(f"{attacker.name} の きりばらい で場が綺麗になった！")
        return logs

    # おかたづけ（両サイドハザード解除＋A・S +1）
    if n == "おかたづけ" and field is not None:
        for side in ([attacker_side, defender_side] if attacker_side and defender_side else []):
            idx = side.field_idx
            field.spikes[idx] = 0
            field.toxic_spikes[idx] = 0
            field.sticky_web[idx] = False
        attacker.stage_attack = min(6, attacker.stage_attack + 1)
        attacker.stage_speed = min(6, attacker.stage_speed + 1)
        logs.append(f"{attacker.name} の おかたづけ！こうげきとすばやさが上がった！")
        return logs

    # みずびたし（みずタイプに変更）
    if n == "みずびたし":
        defender.type1 = "みず"
        defender.type2 = None
        logs.append(f"{defender.name} は みずびたし で みず タイプになった！")
        return logs

    # のろい
    if n == "のろい":
        if "ゴースト" in (attacker.type1, attacker.type2):
            cost = max(1, attacker.max_hp // 4)
            attacker.take_damage(cost)
            defender.cursed = True
            logs.append(f"{attacker.name} は のろい で {defender.name} に呪いをかけた！")
        else:
            attacker.stage_attack = min(6, attacker.stage_attack + 1)
            attacker.stage_defense = min(6, attacker.stage_defense + 1)
            attacker.stage_speed = max(-6, attacker.stage_speed - 1)
            logs.append(f"{attacker.name} は のろい！こうげきとぼうぎょが上がり、すばやさが下がった！")
        return logs

    # バトンタッチ
    if n == "バトンタッチ":
        attacker._baton_stages = {
            a: getattr(attacker, a, 0)
            for a in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                      "stage_speed","stage_accuracy","stage_evasion")
        }  # type: ignore
        attacker._pivot_out = True  # type: ignore
        logs.append(f"{attacker.name} は バトンタッチ！")
        return logs

    # トリック（アイテム交換）：どちらかがメガストーンを持つ場合は失敗
    if n == "トリック":
        if _is_megastone(attacker.item) or _is_megastone(defender.item):
            logs.append(f"{attacker.name} の トリック は失敗した！（メガストーン）")
            return logs
        attacker.item, defender.item = defender.item, attacker.item
        logs.append(f"トリック！ {attacker.name} と {defender.name} のアイテムが入れ替わった！")
        return logs

    # ミストフィールド
    if n == "ミストフィールド" and field is not None:
        field.misty_terrain = True
        field.misty_terrain_count = 5
        logs.append("ミストフィールドが広がった！")
        return logs

    # エレキフィールド
    if n == "エレキフィールド" and field is not None:
        field.electric_terrain = True
        field.electric_terrain_count = 5
        logs.append("エレキフィールドが広がった！")
        return logs

    # サイコフィールド
    if n == "サイコフィールド" and field is not None:
        field.psychic_terrain = True
        field.psychic_terrain_count = 5
        logs.append("サイコフィールドが広がった！")
        return logs

    # じゅうでん（次の電気技威力×2 + とくぼう+1）
    if n == "じゅうでん":
        attacker.charged = True
        attacker.stage_sp_defense = min(6, attacker.stage_sp_defense + 1)
        logs.append(f"{attacker.name} は じゅうでん した！とくぼうが上がった！")
        return logs

    # しっぽきり（みがわり作成＋ピボット）
    if n == "しっぽきり":
        cost = attacker.max_hp // 2
        sub_hp = attacker.max_hp // 4
        if attacker.hp > cost and getattr(attacker, '_substitute_hp', 0) == 0:
            attacker.hp -= cost
            attacker._substitute_hp = sub_hp  # type: ignore
            attacker._pivot_out = True  # type: ignore
            logs.append(f"{attacker.name} は しっぽきり！みがわりを残して交代！")
        else:
            logs.append(f"{attacker.name} の しっぽきり は失敗した！")
        return logs

    # ちからをすいとる（相手の攻撃実数値分回復＋相手のこうげき-1）
    if n == "ちからをすいとる":
        heal = defender.get_effective_stat("attack")
        attacker.hp = min(attacker.max_hp, attacker.hp + heal)
        if defender.ability not in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
            old_v = defender.stage_attack
            defender.stage_attack = max(-6, defender.stage_attack - 1)
            if defender.stage_attack != old_v:
                logs.append(f"{defender.name} の こうげき が下がった！")
        logs.append(f"{attacker.name} は {heal}HP を吸収した！")
        return logs

    # パワースワップ（A・C ランク交換）
    if n == "パワースワップ":
        attacker.stage_attack, defender.stage_attack = defender.stage_attack, attacker.stage_attack
        attacker.stage_sp_attack, defender.stage_sp_attack = defender.stage_sp_attack, attacker.stage_sp_attack
        logs.append(f"{attacker.name} の パワースワップ！こうげき・とくこうが入れ替わった！")
        return logs

    # ほおばる（きのみ食べ＋ぼうぎょ+2）
    if n == "ほおばる":
        if attacker.item and attacker.item.endswith("のみ"):
            logs.append(f"{attacker.name} は {attacker.item} を食べた！")
            attacker.item = None
            attacker.ate_berry = True
            attacker.stage_defense = min(6, attacker.stage_defense + 2)
            logs.append(f"{attacker.name} の ぼうぎょ が上がった！")
        else:
            logs.append(f"{attacker.name} の ほおばる は失敗した！（きのみなし）")
        return logs

    # リサイクル（前回消費アイテム回収）
    if n == "リサイクル":
        last_item = getattr(attacker, '_last_item', None)
        if last_item and attacker.item is None:
            attacker.item = last_item
            attacker._last_item = None  # type: ignore
            logs.append(f"{attacker.name} は {attacker.item} を リサイクル した！")
        else:
            logs.append(f"{attacker.name} の リサイクル は失敗した！")
        return logs

    # かなしばり（相手の最後に使った技を封じる）
    if n == "かなしばり":
        if defender.last_used_move and not defender.disabled_move:
            defender.disabled_move = defender.last_used_move
            defender.disabled_turns = 4
            logs.append(f"{defender.name} の {defender.disabled_move} が かなしばり された！")
        return logs

    # ふういん（共通技の封印）
    if n == "ふういん":
        logs.append(f"{attacker.name} は ふういん した！")
        return logs

    # でんじふゆう（3ターン地面無効）
    if n == "でんじふゆう":
        attacker._levitate_turns = 3  # type: ignore
        logs.append(f"{attacker.name} は でんじふゆう ！地面技を3ターン無効化！")
        return logs

    # ソウルビート（全能力+1・HP1/3消費）
    if n == "ソウルビート":
        cost = max(1, attacker.max_hp // 3)
        if attacker.hp > cost:
            attacker.hp -= cost
            for attr in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed"):
                setattr(attacker, attr, min(6, getattr(attacker, attr, 0) + 1))
            logs.append(f"{attacker.name} の ソウルビート！全能力が上がった！")
        else:
            logs.append(f"{attacker.name} の ソウルビート は失敗した！")
        return logs

    # へんしん（相手をコピー）
    if n == "へんしん":
        if getattr(attacker, '_transformed', False):
            logs.append(f"{attacker.name} は すでに へんしん している！")
            return logs
        attacker._transform_backup = {  # type: ignore
            "attack":     attacker.attack,
            "defense":    attacker.defense,
            "sp_attack":  attacker.sp_attack,
            "sp_defense": attacker.sp_defense,
            "speed":      attacker.speed,
            "ability":    attacker.ability,
            "moves":      list(attacker.moves),
            "pp":         list(attacker.pp),
        }
        attacker.attack      = defender.attack
        attacker.defense     = defender.defense
        attacker.sp_attack   = defender.sp_attack
        attacker.sp_defense  = defender.sp_defense
        attacker.speed       = defender.speed
        attacker.ability     = defender.ability
        attacker.type1       = defender.type1
        attacker.type2       = defender.type2
        attacker.moves       = list(defender.moves)
        attacker.pp          = [min(5, m.pp if m else 5) for m in defender.moves]
        attacker.stage_attack    = defender.stage_attack
        attacker.stage_defense   = defender.stage_defense
        attacker.stage_sp_attack = defender.stage_sp_attack
        attacker.stage_sp_defense = defender.stage_sp_defense
        attacker.stage_speed     = defender.stage_speed
        attacker.stage_accuracy  = defender.stage_accuracy
        attacker.stage_evasion   = defender.stage_evasion
        attacker._transformed    = True  # type: ignore
        logs.append(f"{attacker.name} は {defender.name} に へんしん した！")
        return logs

    # コーチング / さいはい（ダブル専用）
    if n in ("コーチング", "さいはい"):
        logs.append(f"{n}（ダブルバトル専用・無効）")
        return logs

    logs.append(f"{n} が発動")
    return logs


HIGH_CRIT_MOVES = {
    "きょうふのつるぎ","からじしボム","スラッシュ","カタストロフィ",
    "シャドークロー","ナイトスラッシュ","クロスポイズン","サイコカッター","リーフブレード",
    "3ぼんのや","ストーンエッジ","ブレイズキック",
    "クラブハンマー","クロスチョップ","つじぎり","ドリルライナー",
    "アクアカッター","エアカッター","ゴッドバード",
}
_CRIT_THRESHOLDS = {0: 1/24, 1: 1/8, 2: 1/2, 3: 1.0}


def crit_chance(attacker: BattlePokemon, move: MoveData,
                defender: Optional[BattlePokemon] = None) -> float:
    """急所確率（0.0〜1.0）。必中急所(トリックフラワー/ひとでなしvs毒)は1.0。
    ダメージ期待値の計算（選出評価・相性表）からも参照する。"""
    if defender is not None and defender.ability in ("シェルアーマー", "カブトアーマー"):
        return 0.0
    if attacker.ability == "ひとでなし" and defender is not None \
            and defender.status in ("poison", "badpoison"):
        return 1.0
    if move.name_jp == "トリックフラワー":
        return 1.0
    stage = 0
    if move.name_jp in HIGH_CRIT_MOVES:
        stage = 1
    if attacker.ability in ("きょううん",):
        stage += 1
    from .items import get_crit_stage_bonus
    stage += get_crit_stage_bonus(attacker.item)
    stage += getattr(attacker, 'crit_stage', 0)
    return _CRIT_THRESHOLDS.get(min(stage, 3), 1.0)


def _check_critical(attacker: BattlePokemon, move: MoveData,
                    defender: Optional[BattlePokemon] = None) -> bool:
    return random.random() < crit_chance(attacker, move, defender)


MULTI_HIT_2 = {
    "ダブルキック", "にどげり", "ダブルウイング", "ドラゴンアロー",
    "スパークリングアリア", "ダブルパンツァー", "ツインビーム", "ダブルアタック",
}
MULTI_HIT_3 = {"トリプルアクセル"}
MULTI_HIT_RANDOM_25 = {
    "スケイルショット", "みずしゅりけん", "ロックブラスト",
    "タネマシンガン", "つららばり", "ミサイルばり",
    "ボーンラッシュ", "あわ", "スイープビンタ",
}


def _calc_hits(move: MoveData, attacker=None) -> int:
    n = move.name_jp
    skill_link = attacker is not None and getattr(attacker, 'ability', '') == "スキルリンク"

    if n in MULTI_HIT_2:
        return 2
    if n in MULTI_HIT_3:
        return 3
    if n in MULTI_HIT_RANDOM_25:
        if skill_link:
            return 5
        return random.choices([2, 3, 4, 5], weights=[3, 3, 1, 1])[0]
    # ネズミざん：1〜10回連続（途中で外れると終わる＝各継続を確率判定）。スキルリンクで必ず10回
    if n == "ネズミざん":
        if skill_link:
            return 10
        hits = 1
        while hits < 10 and random.random() < 0.90:
            hits += 1
        return hits
    return 1


def _apply_secondary(attacker, defender, move, dmg, logs, field=None, defender_side=None):
    """追加効果（状態異常・ひるみ・能力変化）"""
    n = move.name_jp

    if not defender.is_alive:
        # 自己能力変化（りゅうせいぐん等）は倒した時も発動
        SELF_EFFECTS_KO: dict[str, list[tuple[str, int, float]]] = {
            "インファイト":     [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
            "クローズコンバット": [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
            "ばかぢから":       [("stage_attack", -1, 1.0), ("stage_defense", -1, 1.0)],
            "りゅうせいぐん":   [("stage_sp_attack", -2, 1.0)],
            "リーフストーム":   [("stage_sp_attack", -2, 1.0)],
            "オーバーヒート":   [("stage_sp_attack", -2, 1.0)],
            "サイコブースト":   [("stage_sp_attack", -2, 1.0)],
            "ゴールドラッシュ": [("stage_sp_attack", -2, 1.0)],
            "アームハンマー":   [("stage_speed", -1, 1.0)],
            "アーマーキャノン": [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
            "とどめばり":       [("stage_attack", 3, 1.0)],
        }
        if n in SELF_EFFECTS_KO:
            for stat, delta, prob in SELF_EFFECTS_KO[n]:
                if random.random() < prob:
                    old_val = getattr(attacker, stat, 0)
                    new_val = max(-6, min(6, old_val + delta))
                    setattr(attacker, stat, new_val)
                    if new_val != old_val:
                        logs.append(f"{attacker.name} の {STAT_JP.get(stat, stat)} が{'下がった' if delta < 0 else '上がった'}！")
        return

    # ふんどのこぶし用: 攻撃技で被弾した回数を加算（防御側は生存中）
    if dmg > 0:
        defender.times_hit += 1

    # ちからずく: 追加効果（状態異常・ひるみ・相手への能力変化）をキャンセル
    # ただし自分自身の確定能力変化（インファイト等）は後段で発動
    force_no_secondary = (attacker.ability == "ちからずく" or defender.ability == "りんぷん")

    # じごくづき（2ターン音技封じ）
    if n == "じごくづき" and dmg > 0 and defender.is_alive:
        defender.throat_chop_count = 2
        logs.append(f"{defender.name} は じごくづき 状態になった！")

    # バインド（4-5ターン、毎ターン1/8ダメ、交代不可）
    _BIND_MOVES = {
        "まきつく", "しめつける", "まとわりつく", "ほのおのうず",
        "うずしお", "すなじごく", "トラバサミ",
    }
    if n in _BIND_MOVES and dmg > 0 and defender.is_alive and not defender.bound_count:
        defender.bound_count = random.randint(4, 5)
        logs.append(f"{defender.name} は バインド 状態になった！")

    # ── なげつける特殊効果 ──────────────────────────────
    if n == "なげつける" and defender.is_alive and not force_no_secondary:
        flung = getattr(attacker, '_last_flung_item', None)
        FLING_STATUS: dict[str, tuple[str, str]] = {
            "どくバリ": ("poison",    "どく"),
            "もうどくだま": ("badpoison", "もうどく"),
        }
        if flung in FLING_STATUS:
            st, st_jp = FLING_STATUS[flung]
            ok = defender.apply_status(st)
            if ok:
                logs.append(f"なげつけた {flung} で {defender.name} が {st_jp} になった！")
                from .items import try_cure_berry
                try_cure_berry(defender, logs)

    # ── 状態異常追加効果 ──────────────────────────────
    STATUS_EFFECTS: dict[str, tuple[str, float]] = {
        # 麻痺
        "10まんボルト": ("paralysis", 0.10), "かみなり": ("paralysis", 0.30),
        "ボルテッカー":  ("paralysis", 0.10), "でんきショック": ("paralysis", 0.10),
        "スパーク":      ("paralysis", 0.30), "りゅうのいぶき": ("paralysis", 0.30),
        "ほうでん": ("paralysis", 0.30),
        "かみなりのキバ": ("paralysis", 0.10), "かみなりパンチ": ("paralysis", 0.10),
        "ほっぺすりすり": ("paralysis", 1.00),
        "でんじほう":    ("paralysis", 1.00),
        "のしかかり":    ("paralysis", 0.30),
        "とびはねる":    ("paralysis", 0.30),
        # やけど
        "かえんほうしゃ": ("burn", 0.10), "フレアドライブ": ("burn", 0.10),
        "だいもんじ":     ("burn", 0.10), "かえんぐるま":   ("burn", 0.10),
        "ねっとう":       ("burn", 0.30),
        "ほのおのキバ":   ("burn", 0.10), "ほのおのパンチ":  ("burn", 0.10),
        "ブレイズキック": ("burn", 0.10),
        "ふんえん":       ("burn", 0.30), "ねっぷう": ("burn", 0.10),
        "ねっさのだいち": ("burn", 0.30), "ひゃっきやこう": ("burn", 0.30),
        "れんごく":       ("burn", 1.00),
        "シャカシャカほう": ("burn", 0.20),
        # こおり
        "れいとうビーム": ("freeze", 0.10), "ふぶき": ("freeze", 0.10),
        "アイスビーム":   ("freeze", 0.10),
        "こおりのキバ":   ("freeze", 0.10), "れいとうパンチ": ("freeze", 0.10),
        # どく
        "どくづき": ("poison", 0.30), "クロスポイズン": ("poison", 0.10),
        "どくどくのキバ": ("badpoison", 0.50),
        "ヘドロばくだん": ("poison", 0.30), "ヘドロウェーブ": ("poison", 0.10),
        "ダストシュート": ("poison", 0.30), "シェルアームズ": ("poison", 0.20),
        "どくばりセンボン": ("poison", 0.50),
        # こんらん
        "ウォーターパルス": ("confused", 0.20), "みずのはどう": ("confused", 0.20),
        "ダイナミックフル": ("confused", 0.10), "ぼうふう":     ("confused", 0.30),
        "ばくれつパンチ":   ("confused", 1.00), "かかとおとし": ("confused", 0.30),
    }
    _sg_sec = defender_side is not None and getattr(defender_side, 'safeguard', 0) > 0
    if n in STATUS_EFFECTS and not force_no_secondary and not _sg_sec:
        effect, prob = STATUS_EFFECTS[n]
        if effect == "freeze" and field is not None and effective_weather(field, defender) == "sunny":
            pass
        elif random.random() < prob:
            if effect == "confused":
                if defender.ability not in ("マイペース",):
                    defender.confused = True
                    logs.append(f"{defender.name} はこんらんした！")
                    from .items import try_cure_berry
                    try_cure_berry(defender, logs)
            else:
                EFFECT_NAMES = {"paralysis":"まひ","burn":"やけど","freeze":"こおり","poison":"どく"}
                ok = defender.apply_status(effect)
                if ok:
                    logs.append(f"{defender.name} は {EFFECT_NAMES.get(effect, effect)} になった！")
                    from .items import try_cure_berry
                    try_cure_berry(defender, logs)

    # トライアタック: まひ/やけど/こおりいずれか20%
    if n == "トライアタック" and not force_no_secondary and random.random() < 0.20:
        effect = random.choice(["paralysis", "burn", "freeze"])
        if not (effect == "freeze" and field is not None and effective_weather(field, defender) == "sunny"):
            EFFECT_NAMES_TRI = {"paralysis":"まひ","burn":"やけど","freeze":"こおり"}
            ok = defender.apply_status(effect)
            if ok:
                logs.append(f"{defender.name} は {EFFECT_NAMES_TRI[effect]} になった！")
                from .items import try_cure_berry as _tcb_tri
                _tcb_tri(defender, logs)

    # しっとのほのお/みわくのボイス: 相手の能力が上がっている場合のみ状態異常
    if n in ("しっとのほのお", "みわくのボイス") and not force_no_secondary:
        _stages = ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense",
                   "stage_speed","stage_accuracy","stage_evasion")
        if any(getattr(defender, s, 0) > 0 for s in _stages):
            if n == "みわくのボイス":
                if defender.ability not in ("マイペース",):
                    defender.confused = True
                    logs.append(f"{defender.name} はこんらんした！")
                    from .items import try_cure_berry as _tcb_v
                    _tcb_v(defender, logs)
            else:
                if defender.apply_status("burn"):
                    logs.append(f"{defender.name} はやけどを負った！")
                    from .items import try_cure_berry as _tcb_j
                    _tcb_j(defender, logs)

    # りんぷん: 追加効果をブロック
    if defender.ability == "りんぷん":
        return

    # ── 防御側能力ダウン ──────────────────────────────
    DEF_DOWNS: dict[str, tuple[str, int, float]] = {
        "かみくだく":    ("stage_defense",    -1, 0.20),
        "クラッシュクロー": ("stage_defense",  -1, 0.50),
        "バークアウト":  ("stage_sp_attack",  -1, 1.00),
        "こごえるかぜ":  ("stage_speed",       -1, 1.00),
        "がんせきふうじ": ("stage_speed",      -1, 1.00),
        "じならし":      ("stage_speed",       -1, 1.00),
        "バブルこうせん": ("stage_speed",      -1, 0.10),
        "バブルだま":    ("stage_speed",        -1, 0.10),
        "キャタストロフィ": ("stage_defense",  -1, 0.20),
        "マッドショット":  ("stage_speed",     -1, 1.00),
        "アクアブレイク": ("stage_defense",    -1, 0.20),
        "ワタシらしく":  ("stage_sp_attack",   -1, 1.00),
        "ルミナコリジョン": ("stage_sp_defense",-2, 1.00),
        "マジカルフレイム": ("stage_sp_attack", -1, 1.00),
        "エレキネット":  ("stage_speed",       -1, 1.00),
        "シャドーボール": ("stage_sp_defense", -1, 0.20),
        "サイコキネシス": ("stage_sp_defense", -1, 0.10),
        "エナジーボール": ("stage_sp_defense", -1, 0.10),
        "むしのさざめき": ("stage_sp_defense", -1, 0.10),
        "じゃれつく":    ("stage_attack",      -1, 0.10),
        "ムーンフォース": ("stage_sp_attack",  -1, 0.30),
        "ナイトバースト": ("stage_accuracy",   -1, 0.40),
        "だくりゅう":    ("stage_accuracy",   -1, 1.00),
        "どろかけ":      ("stage_accuracy",   -1, 1.00),
        "アイアンテール": ("stage_defense",   -1, 0.30),
        "トロピカルキック": ("stage_attack",  -1, 1.00),
        "はいよるいちげき": ("stage_sp_attack", -1, 1.00),
        "ひやみず":      ("stage_attack",     -1, 1.00),
        "むしのていこう": ("stage_sp_attack",  -1, 1.00),
        "Gのちから":    ("stage_defense",     -1, 1.00),
        "とびつく":      ("stage_speed",       -1, 1.00),
        "りんごさん":    ("stage_sp_defense",  -1, 1.00),
        "きあいだま":    ("stage_sp_defense",  -1, 0.10),
        "アシッドボム":  ("stage_sp_defense",  -2, 1.00),
        "シェルブレード": ("stage_defense",    -1, 0.50),
        "3ぼんのや":    ("stage_defense",    -1, 0.50),
        "だいちのちから": ("stage_sp_defense", -1, 0.10),
        "とびかかる":    ("stage_attack",      -1, 1.00),
        "ラスターカノン": ("stage_sp_defense", -1, 0.10),
        "ほのおのムチ":   ("stage_defense",    -1, 1.00),
        "ブレイククロー": ("stage_defense",    -1, 0.50),
        "ローキック":     ("stage_speed",      -1, 1.00),
        "ワイドブレイカー":("stage_attack",    -1, 1.00),
        "ソウルクラッシュ": ("stage_sp_attack", -1, 1.00),
    }
    if n in DEF_DOWNS and not force_no_secondary:
        stat, delta, prob = DEF_DOWNS[n]
        # あまのじゃく：対象(defender)自身への能力変化は逆転（起因が相手の技でも対象基準で反転）
        if defender.ability == "あまのじゃく":
            delta = -delta
        # 能力下落防止チェック（逆転後の符号で判定）
        if delta < 0:
            if defender.ability == "ミラーアーマー" and random.random() < prob:
                # 能力低下を相手（攻撃側）に跳ね返す
                _ov = getattr(attacker, stat, 0); setattr(attacker, stat, max(-6, _ov + delta))
                if getattr(attacker, stat, 0) != _ov:
                    logs.append(f"{defender.name} の ミラーアーマー！ {attacker.name} の {STAT_JP.get(stat, stat)} が下がった！")
                return
            if defender.ability in ("クリアボディ", "しろいけむり", "かがくへんかガス"):
                logs.append(f"{defender.name} の {defender.ability} で能力が下がらなかった！")
                return
            if stat == "stage_defense" and defender.ability == "はとむね":
                logs.append(f"{defender.name} の はとむね で防御が下がらなかった！")
                return
            if stat == "stage_attack" and defender.ability == "かいりきバサミ":
                logs.append(f"{defender.name} の かいりきバサミ で攻撃が下がらなかった！")
                return
            if stat in ("stage_accuracy",) and defender.ability in ("するどいめ", "はっこう"):
                logs.append(f"{defender.name} の {defender.ability} で命中率が下がらなかった！")
                return
        if random.random() < prob:
            old_val = getattr(defender, stat, 0)
            new_val = max(-6, min(6, old_val + delta))
            setattr(defender, stat, new_val)
            if new_val != old_val:
                logs.append(f"{defender.name} の {STAT_JP.get(stat, stat)} が{'下がった' if delta < 0 else '上がった'}！")
                from .abilities import on_stat_lowered
                if delta < 0:
                    on_stat_lowered(defender, logs)

    # ── 攻撃側自己能力変化 ──────────────────────────────
    SELF_EFFECTS: dict[str, list[tuple[str, int, float]]] = {
        "インファイト":   [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
        "クローズコンバット": [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
        "ばかぢから":    [("stage_attack", -1, 1.0), ("stage_defense", -1, 1.0)],
        "りゅうせいぐん": [("stage_sp_attack", -2, 1.0)],
        "リーフストーム": [("stage_sp_attack", -2, 1.0)],
        "オーバーヒート": [("stage_sp_attack", -2, 1.0)],
        "サイコブースト": [("stage_sp_attack", -2, 1.0)],
        "ゴールドラッシュ": [("stage_sp_attack", -2, 1.0)],
        "だいばくはつ":   [],  # 倒れる（別処理）
        "じばく":         [],
        "フレアソング":   [("stage_sp_attack", 1, 1.0)],
        "ほのおのまい":  [("stage_sp_attack", 1, 0.50)],
        "チャージビーム": [("stage_sp_attack", 1, 0.70)],
        "ニトロチャージ": [("stage_speed", 1, 1.0)],
        "アクアステップ": [("stage_speed", 1, 1.0)],
        "くさわけ":      [("stage_speed", 1, 1.0)],
        "コメットパンチ": [("stage_attack", 1, 0.20)],
        "アームハンマー": [("stage_speed", -1, 1.0)],
        "アーマーキャノン": [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
        "オーラぐるま":    [("stage_speed", 1, 1.0)],
        "バリアーラッシュ":[("stage_defense", 1, 1.0)],
        "はがねのつばさ":  [("stage_defense", 1, 0.10)],
        "ぶちかまし":      [("stage_defense", -1, 1.0), ("stage_sp_defense", -1, 1.0)],
        "アイスハンマー":  [("stage_speed", -1, 1.0)],
        "スケイルノイズ":  [("stage_defense", -1, 1.0)],
        "スケイルショット":[("stage_defense", -1, 1.0), ("stage_speed", 1, 1.0)],
    }
    # げんしのちから/シルバーウィンド等：10%で全能力1段階上昇（一括判定）
    if n == "げんしのちから" and not force_no_secondary and random.random() < 0.10:
        for st in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed"):
            v = getattr(attacker, st, 0)
            if v < 6:
                setattr(attacker, st, v + 1)
        logs.append(f"{attacker.name} の能力が上がった！")
    if n in SELF_EFFECTS:
        for stat, delta, prob in SELF_EFFECTS[n]:
            if random.random() < prob:
                # あまのじゃく：能力変化を反転
                _d = -delta if attacker.ability == "あまのじゃく" else delta
                old_val = getattr(attacker, stat, 0)
                new_val = max(-6, min(6, old_val + _d))
                setattr(attacker, stat, new_val)
                if new_val != old_val:
                    logs.append(f"{attacker.name} の {STAT_JP.get(stat, stat)} が{'下がった' if _d < 0 else '上がった'}！")
                    from .abilities import on_stat_lowered
                    if _d < 0:
                        on_stat_lowered(attacker, logs)
                    # びんじょう：相手の能力が上がると自分も同じだけ上がる
                    if _d > 0 and defender.is_alive and defender.ability == "びんじょう":
                        _ov = getattr(defender, stat, 0)
                        setattr(defender, stat, min(6, _ov + _d))
                        if getattr(defender, stat, 0) != _ov:
                            logs.append(f"{defender.name} の びんじょう！ {STAT_JP.get(stat, stat)} が上がった！")

    # ぶきみなじゅもん（攻撃技）：命中後に相手の最後の技のPPを3減らす
    if n == "ぶきみなじゅもん" and defender.is_alive and defender.last_used_move:
        for i, mv in enumerate(defender.moves):
            if mv and mv.name_jp == defender.last_used_move and i < len(defender.pp):
                defender.pp[i] = max(0, defender.pp[i] - 3)
                logs.append(f"{defender.name} の {mv.name_jp} の PP が 3 減った！")
                break

    # ── ひるみ ──────────────────────────────
    FLINCH_MOVES: dict[str, float] = {
        "エアスラッシュ": 0.30, "アイアンヘッド": 0.20, "3ぼんのや": 0.30,
        "がんせきおとし": 0.30, "いわなだれ": 0.30,
        "ほのおのキバ": 0.10, "かみなりのキバ": 0.10, "こおりのキバ": 0.10,
        "ウォーターフォール": 0.20, "たきのぼり": 0.20,
        "あくのはどう": 0.20,
        "かみつく": 0.30, "しねんのずつき": 0.20,
        "ねこだまし": 1.00,
        "スピードスター": 0.0,
        "いびき": 0.30, "じんつうりき": 0.10,
        "つららおとし": 0.30, "ひょうざんおろし": 0.30,
        "ゴッドバード": 0.30, "ドラゴンダイブ": 0.20,
        "はやてがえし": 1.00,
    }
    if n in FLINCH_MOVES and FLINCH_MOVES[n] > 0 and not force_no_secondary:
        if random.random() < FLINCH_MOVES[n]:
            if defender.ability not in ("せいしんりょく", "どんかん"):
                defender.flinched = True
                logs.append(f"{defender.name} はひるんだ！")

    # フェイタルクロー：30%でどく/まひ/ねむりいずれか
    if n == "フェイタルクロー" and defender.is_alive and not force_no_secondary:
        if random.random() < 0.30:
            candidates = ["poison", "paralysis", "sleep"]
            chosen = random.choice(candidates)
            ok = defender.apply_status(chosen)
            if ok:
                STATUS_JP = {"poison":"どく","paralysis":"まひ","sleep":"ねむり"}
                if chosen == "sleep":
                    defender.sleep_count = random.randint(1, 3)
                logs.append(f"{defender.name} は {STATUS_JP.get(chosen, chosen)} になった！")
                from .items import try_cure_berry
                try_cure_berry(defender, logs)

    # かげぬい（ダメージ技）：命中時に相手をにげられない状態に
    if n == "かげぬい" and dmg > 0 and defender.is_alive:
        defender.trapped = True
        logs.append(f"{defender.name} は逃げられなくなった！")

    # こおり治癒：ねっとう/ねっさのだいち=相手のこおりを治す、自分のこおりも治す
    if n in ("ねっとう", "ねっさのだいち"):
        if defender.is_alive and defender.status == "freeze":
            defender.status = None
            logs.append(f"{defender.name} の こおり が治った！")
    if n in ("ねっとう", "もえつきる", "ねっさのだいち"):
        if attacker.status == "freeze":
            attacker.status = None
            logs.append(f"{attacker.name} の こおり が治った！")
    # もえつきる：攻撃後に自分のほのおタイプが消える
    if n == "もえつきる" and "ほのお" in (attacker.type1, attacker.type2):
        rem = [t for t in (attacker.type1, attacker.type2) if t and t != "ほのお"]
        attacker.type1 = rem[0] if rem else "ノーマル"
        attacker.type2 = rem[1] if len(rem) > 1 else None
        logs.append(f"{attacker.name} は ほのお タイプでなくなった！")

    # しおづけ：ソルトキュア状態（ターン終了時に継続ダメ）
    if n == "しおづけ" and defender.is_alive and not force_no_secondary:
        if not getattr(defender, '_salted', False):
            defender._salted = True  # type: ignore
            logs.append(f"{defender.name} は しおづけ にされた！")

    # みずあめボム：3ターンあめまみれ（素早さ低下）
    if n == "みずあめボム" and defender.is_alive and not force_no_secondary:
        defender.syrup_count = 3
        logs.append(f"{defender.name} は あめまみれ になった！")

    # サイコノイズ：2ターンかいふくふうじ
    if n == "サイコノイズ" and defender.is_alive and not force_no_secondary:
        defender.heal_block_count = 2
        logs.append(f"{defender.name} は かいふくふうじ 状態になった！")

    # うたかたのアリア：相手のやけどを治す（ダメージ技の追加効果）
    if n == "うたかたのアリア" and defender.is_alive and defender.status == "burn":
        defender.status = None
        logs.append(f"{defender.name} の やけど が うたかたのアリア で治った！")

    # ミストバースト：使用後に自分が気絶
    if n == "ミストバースト" and attacker.is_alive:
        attacker.hp = 0
        attacker.is_alive = False
        logs.append(f"{attacker.name} は ミストバースト の反動で倒れた！")

    # げきりん・あばれる・はなびらのまい・だいふんげき：2〜3ターンロック後にこんらん
    RAGE_MOVES = {"げきりん", "あばれる", "はなびらのまい", "だいふんげき"}
    if n in RAGE_MOVES:
        if not attacker.locked_move:
            attacker.locked_move = n
            attacker.lock_count = random.randint(2, 3)
        else:
            attacker.lock_count -= 1
            if attacker.lock_count <= 0:
                attacker.locked_move = None
                attacker.lock_count = 0
                if attacker.ability != "マイペース":
                    attacker.confused = True
                    logs.append(f"{attacker.name} は疲れてこんらんした！")
                    from .items import try_cure_berry as _tcb
                    _tcb(attacker, logs)

    # さわぐ：2〜3ターン連続使用ロック（あばれる類似だが終了後こんらんしない）
    if n == "さわぐ":
        if not attacker.locked_move:
            attacker.locked_move = n
            attacker.lock_count = random.randint(2, 3)
        else:
            attacker.lock_count -= 1
            if attacker.lock_count <= 0:
                attacker.locked_move = None
                attacker.lock_count = 0

    # last_used_moveを記録（ふいうち・アンコール用）
    attacker.last_used_move = n


def _apply_recoil(attacker, defender, move, dmg, logs):
    # いしあたま/ロックヘッド: 反動を受けない（わるあがき除く）
    if attacker.ability in ("いしあたま", "ロックヘッド") and move.name_jp != "わるあがき":
        return
    # わるあがき：与ダメの1/4を自傷
    if move.name_jp == "わるあがき":
        recoil = max(1, math.floor(attacker.max_hp / 4))
        attacker.take_damage(recoil)
        logs.append(f"{attacker.name} は わるあがき の反動を受けた！({recoil})")
        return

    # 最大HPの半分を反動として受ける技
    max_hp_half_recoil = {"てっていこうせん"}
    # ダメージの割合を反動として受ける技
    recoil_moves = {
        "すてみタックル":  1/3,
        "フレアドライブ":  1/3,
        "ボルテッカー":    1/3,
        "ウェーブタックル":1/3,
        "ブレイブバード":  1/3,
        "ウッドハンマー":  1/3,
        "もろはのずつき":  1/2,
        "ワイルドボルト":  1/4,
        "はめつのひかり":  1/2,
    }
    if attacker.ability in ("ロックヘッド", "マジックガード"):
        return
    if move.name_jp in max_hp_half_recoil:
        recoil = max(1, attacker.max_hp // 2)
        attacker.take_damage(recoil)
        logs.append(f"{attacker.name} は反動を受けた！({recoil})")
    elif move.name_jp in recoil_moves:
        recoil = max(1, math.floor(dmg * recoil_moves[move.name_jp]))
        attacker.take_damage(recoil)
        logs.append(f"{attacker.name} は反動を受けた！({recoil})")


class Battle:
    def __init__(self, side1: BattleSide, side2: BattleSide, field: Optional[BattleField] = None):
        self.side1 = side1
        self.side2 = side2
        self.field = field or BattleField()
        self.turn = 0
        self.logs: List[str] = []
        side1.field_idx = 0
        side2.field_idx = 1

    def clone(self) -> "Battle":
        """現在の対戦状態を独立に複製する（決定化ロールアウト用・MCTS探索専用）。
        belief は Noneガード済みで探索中は読まないので複製しない。opp_view は開示情報の
        特徴量化（v5）で参照するため複製する（各クローン独立に保つ）。"""
        s1b, s2b = self.side1.belief, self.side2.belief
        self.side1.belief = self.side2.belief = None
        try:
            c = copy.deepcopy(self)
        finally:
            self.side1.belief, self.side2.belief = s1b, s2b
        return c

    def resume(self, ai1, ai2, verbose=False, max_turns=None) -> int:
        """途中状態（clone後など）から対戦を継続する。見せ合い・初手入場処理は再実行しない。
        max_turns: このターン数で打ち切る（ロールアウトの深さ制限用、Noneなら通常のMAX_TURNS）。"""
        return self._turn_loop(ai1, ai2, verbose, max_turns)

    def run(self, ai1, ai2, verbose=False, on_turn=None) -> int:
        """
        バトルを実行。戻り値: 1=side1勝利, 2=side2勝利, 0=引き分け(最大ターン超過)
        ai: BattleSide, BattleField → Action を返す callable
        on_turn: 各ターン完了時に on_turn(self) を呼ぶフック（記録/リプレイ用）。
        """
        # 対戦前の見せ合い：互いに相手の候補（種族・タイプ）を確認する。
        # 隠れ選出時(HIDDEN_SELECTION=1)は6体ソースを公開し、どの3体を選出したかは場に出るまで不明。
        # フラグOFF時は従来通り選出パーティ(=3体)を公開＝本番不変。
        # 実戦の瀕死交代は、各サイドのAIが持つ choose_faint_switch（価値ベースの交代選択）を使う。
        # シミュ内(_advance_turn→resume)は run を通らないため未設定＝従来の高速ヒューリスティック。
        self._faint_chooser1 = getattr(ai1, "choose_faint_switch", None)
        self._faint_chooser2 = getattr(ai2, "choose_faint_switch", None)
        _hidden = os.environ.get("HIDDEN_SELECTION") != "0"   # 既定ON。HIDDEN_SELECTION=0で従来(選出公開)
        _pv1 = self.side2.source6 if (_hidden and len(self.side2.source6) > len(self.side2.party)) else self.side2.party
        _pv2 = self.side1.source6 if (_hidden and len(self.side1.source6) > len(self.side1.party)) else self.side1.party
        self.logs.extend(self.side1.opp_view.team_preview(_pv1))
        self.logs.extend(self.side2.opp_view.team_preview(_pv2))

        # 入場時効果
        _entry_effects(self.side1.active, 0, self.field, self.side2.active, self.logs, self.side1.party)
        _entry_effects(self.side2.active, 1, self.field, self.side1.active, self.logs, self.side2.party)

        return self._turn_loop(ai1, ai2, verbose, on_turn=on_turn)

    def _turn_loop(self, ai1, ai2, verbose=False, max_turns=None, on_turn=None) -> int:
        limit = MAX_TURNS if max_turns is None else min(max_turns, MAX_TURNS)
        while self.turn < limit:
            self.turn += 1

            if not self.side1.has_alive():
                return 2
            if not self.side2.has_alive():
                return 1

            # バリアフリー: 登場した側がいれば両者のスクリーンを解除（1回の登場につき1度）
            for _bf_side in (self.side1, self.side2):
                if _bf_side.active.ability == "バリアフリー" and not getattr(_bf_side.active, "_barrier_done", False):
                    _bf_side.active._barrier_done = True  # type: ignore
                    for _scr in (self.side1, self.side2):
                        if _scr.reflect or _scr.light_screen or _scr.aurora_veil:
                            _scr.reflect = _scr.light_screen = _scr.aurora_veil = False
                            _scr.reflect_count = _scr.light_screen_count = _scr.aurora_veil_count = 0
                    self.logs.append(f"{_bf_side.active.name} の バリアフリー！ 場のかべが解除された！")

            # ノーてんき：場の天候無効化フラグを更新（メガソーラーは effective_weather 側で優先）
            self.field._weather_negated = "ノーてんき" in (self.side1.active.ability, self.side2.active.ability)

            # 情報系特性（おみとおし/きけんよち）：登場時に強制で相手情報を開示
            self._info_abilities_on_entry()

            action1 = ai1(self.side1, self.side2, self.field)
            action2 = ai2(self.side2, self.side1, self.field)
            # 行動を選んだ本体を記録（先攻で倒され交代した場合、後攻の行動権を失わせるため）
            chooser1, chooser2 = self.side1.active, self.side2.active

            # メガ進化（行動前）
            for _side, _action in [(self.side1, action1), (self.side2, action2)]:
                poke = _side.active
                if _action.do_mega and not poke.mega_evolved and not _side.mega_used:
                    poke.do_mega_evolve()
                    _side.mega_used = True
                    self.logs.append(f"{poke.name} はメガ進化した！")
                    _opp_side = self.side2 if _side is self.side1 else self.side1
                    self.logs.extend(entry_ability(poke, _opp_side.active, self.field,
                                                   weather_duration=MAX_TURNS))

            # くちばしキャノン準備 ＆ このターンの被弾フラグをリセット
            for _sd, _ac in ((self.side1, action1), (self.side2, action2)):
                _mv = getattr(_ac, 'move', None)
                _sd.active._beak_primed = bool(_mv and _mv.name_jp == "くちばしキャノン")
                _sd.active._took_damage_this_turn = False

            # 先攻/後攻決定
            p1_first = _speed_order(self.side1, action1, self.side2, action2, self.field)

            first_side,  first_action,  first_opp  = (
                (self.side1, action1, self.side2) if p1_first
                else (self.side2, action2, self.side1)
            )
            second_side, second_action, second_opp = (
                (self.side2, action2, self.side1) if p1_first
                else (self.side1, action1, self.side2)
            )
            second_chooser = chooser1 if second_side is self.side1 else chooser2

            # 先攻行動（自滅瀕死の交代はターン終了まで保留）
            self._do_action(first_side, first_opp, first_action,
                            ai2 if p1_first else ai1, opp_action=second_action,
                            defer_self_faint=True)
            if not first_opp.has_alive():
                if on_turn:
                    on_turn(self)
                break

            # 後攻行動
            if second_side.active is not second_chooser:
                # 行動者が先攻で倒されて交代済み → このターンは行動権を失う
                pass
            elif not second_opp.active.is_alive:
                # 先攻が自滅(反動/自爆)で退場し場が空 → 後攻技は対象不在で失敗（瀕死交代はターン終了時）
                self.logs.append(f"{second_side.active.name} は こうげきしようとしたが 相手がいない！")
            elif second_side.active.flinched:
                self.logs.append(f"{second_side.active.name} はひるんで動けない！")
                if second_side.active.ability == "ふくつのこころ":
                    second_side.active.stage_speed = min(6, second_side.active.stage_speed + 1)
                    self.logs.append(f"{second_side.active.name} の ふくつのこころ！ 素早さが上がった！")
                second_side.active.flinched = False
            else:
                second_side.active._acts_second = True  # type: ignore
                self._do_action(second_side, second_opp, second_action,
                                ai1 if p1_first else ai2, opp_action=first_action)
                if second_side.active.is_alive:
                    second_side.active._acts_second = False  # type: ignore
            if not second_opp.has_alive():
                if on_turn:
                    on_turn(self)
                break

            # ターン終了処理
            self._end_of_turn()
            if on_turn:
                on_turn(self)
            if verbose:
                print(f"T{self.turn}: {self.side1.active} vs {self.side2.active}")

        if not self.side1.has_alive():
            return 2
        if not self.side2.has_alive():
            return 1
        return 0

    def _do_action(self, my_side: BattleSide, opp_side: BattleSide,
                   action: Action, opp_ai, opp_action: Optional[Action] = None,
                   defer_self_faint: bool = False):
        if action.type == "switch":
            idx = action.switch_to
            if 0 <= idx < len(my_side.party) and my_side.party[idx].is_alive:
                prev_name = my_side.active.name
                self.logs.append(f"{prev_name} は引っ込んだ！")
                my_side.switch_to(idx, self.logs, self.field)
                self.logs.append(f"{my_side.active.name} が出てきた！")
                _entry_effects(my_side.active, my_side.field_idx,
                                self.field, opp_side.active, self.logs, my_side.party)
                self._apply_healing_wish(my_side)
                self.logs.extend(opp_side.opp_view.on_enter(my_side.active))
                self._faint_switch(my_side, opp_side)
            return

        if action.type == "move" and action.move is not None:
            logs = _execute_move(my_side, opp_side, action, self.field, opp_action)
            self.logs.extend(logs)

            # PP消費（わるあがきはmove_idx=-1なのでスキップ）
            attacker = my_side.active
            if action.move_idx is not None and 0 <= action.move_idx < len(attacker.pp):
                # プレッシャー: 相手の技を受けると追加で1減る（攻撃技が相手を対象にした場合）
                _pp_cost = 1
                if (action.move is not None and action.move.category != "status"
                        and opp_side.active.is_alive and opp_side.active.ability == "プレッシャー"):
                    _pp_cost = 2
                attacker.pp[action.move_idx] = max(0, attacker.pp[action.move_idx] - _pp_cost)

            # こだわりアイテム: 技を使ったらその技に縛る（変化技も含む）
            if is_choice_item(attacker.item):
                if attacker.choice_locked_move is None:
                    attacker.choice_locked_move = action.move.name_jp

            # ステルスロックのペンディングフラグを適用
            if getattr(opp_side, '_stealth_rock_pending', False):
                opp_side._stealth_rock_pending = False  # type: ignore
                opp_side.stealth_rock_set = True
                self.field.stealth_rock[opp_side.field_idx] = True

            # 倒れた場合の交代（ハザードで連続倒れも対応）
            self._faint_switch(opp_side, my_side)
            # 先攻が自滅(反動/自爆)した時の交代はターン終了時まで保留（後攻技を空振りさせるため）。
            # 保留分は _end_of_turn 末尾の _faint_switch が回収する。
            if not defer_self_faint:
                self._faint_switch(my_side, opp_side)

            # ピボット技（ボルトチェンジ・とんぼがえり・バトンタッチ等）：生存中に引っ込む
            # 交代先は戦略的に選ぶ（バトンは積みエースへ、通常は有利な受け先へ）
            if my_side.active.is_alive and getattr(my_side.active, '_pivot_out', False):
                if not getattr(my_side, '_manual_switch', False):
                    my_side.active._pivot_out = False  # type: ignore
                    _is_baton = (action.move is not None and action.move.name_jp == "バトンタッチ")
                    next_idx = _choose_pivot_target(my_side, opp_side.active, _is_baton)
                    if next_idx is not None:
                        my_side.switch_to(next_idx, self.logs, self.field)
                        self.logs.append(f"{my_side.active.name} が出てきた！")
                        _entry_effects(my_side.active,
                                       my_side.field_idx,
                                       self.field, opp_side.active, self.logs, my_side.party)
                        self._apply_healing_wish(my_side)
                        self.logs.extend(opp_side.opp_view.on_enter(my_side.active))
                        self._faint_switch(my_side, opp_side)

            # 強制交代技（ドラゴンテール等）：相手をランダム交代
            if opp_side.active.is_alive and getattr(opp_side.active, '_force_switch', False):
                opp_side.active._force_switch = False  # type: ignore
                benched = [i for i, p in enumerate(opp_side.party)
                           if p.is_alive and i != opp_side.active_idx]
                if benched:
                    new_idx = random.choice(benched)
                    self.logs.append(f"{opp_side.active.name} は強制交代させられた！")
                    opp_side.switch_to(new_idx, self.logs, self.field)
                    _entry_effects(opp_side.active,
                                   opp_side.field_idx,
                                   self.field, my_side.active, self.logs, opp_side.party)
                    self.logs.extend(my_side.opp_view.on_enter(opp_side.active))
                    self._faint_switch(opp_side, my_side)

    def _apply_healing_wish(self, side: BattleSide):
        if side.healing_wish and side.active.is_alive:
            side.active.hp = side.active.max_hp
            side.active.status = None
            side.healing_wish = False
            self.logs.append(f"{side.active.name} は いやしのねがい で全快した！")

    def _faint_switch(self, fainted_side: BattleSide, opp_side: BattleSide):
        """倒れたポケモンの交代。ハザードで連続倒れしても全員処理する。"""
        if getattr(fainted_side, '_manual_switch', False):
            return  # 手動バトル: P1の交代はプレイヤーが選択
        chooser = (getattr(self, "_faint_chooser1", None) if fainted_side is self.side1
                   else getattr(self, "_faint_chooser2", None))
        while not fainted_side.active.is_alive and fainted_side.has_alive():
            self.logs.append(f"{fainted_side.active.name} は倒れた！")
            alive_bench = sum(1 for i, p in enumerate(fainted_side.party)
                              if p.is_alive and i != fainted_side.active_idx)
            if chooser is not None and alive_bench >= 2:   # 実戦：価値ベースで繰り出し選択
                next_idx = chooser(fainted_side, opp_side, self.field)
                if next_idx is None:
                    next_idx = _best_faint_switch(fainted_side, opp_side.active, self.field)
            else:
                next_idx = _best_faint_switch(fainted_side, opp_side.active, self.field)
            if next_idx is None:
                break
            fainted_side.switch_to(next_idx, self.logs, self.field)
            self.logs.append(f"{fainted_side.active.name} が登場した！")
            # 相打ちで相手側がマニュアル交代待ち中なら登場時効果を保留
            opp_awaiting = (
                not opp_side.active.is_alive
                and opp_side.has_alive()
                and getattr(opp_side, '_manual_switch', False)
            )
            if opp_awaiting:
                fainted_side._entry_effects_pending = True  # type: ignore
            else:
                _entry_effects(fainted_side.active, fainted_side.field_idx,
                               self.field, opp_side.active, self.logs, fainted_side.party)
                self.logs.extend(opp_side.opp_view.on_enter(fainted_side.active))

    def _info_abilities_on_entry(self):
        """おみとおし/きけんよち：登場時に相手情報を強制開示し、開示情報(opp_view)へ記録する。
        1回の登場につき1度（_info_doneフラグ、交代でリセット）。"""
        for my_side, opp_side in ((self.side1, self.side2), (self.side2, self.side1)):
            me = my_side.active
            opp = opp_side.active
            if not me.is_alive or getattr(me, "_info_done", False):
                continue
            if me.ability not in ("おみとおし", "きけんよち", "よちむ"):
                continue
            me._info_done = True  # type: ignore
            # おみとおし：相手の持ち物を開示
            if me.ability == "おみとおし" and opp.item:
                self.logs.extend(my_side.opp_view.on_item(opp.name, opp.item, "おみとおし"))
            # きけんよち：相手が効果抜群/一撃必殺の技を持つか判定し開示
            if me.ability == "きけんよち":
                from .damage import get_type_effectiveness, BYPASS_DAMAGE_CALC
                _ohko = {"じわれ", "つのドリル", "ハサミギロチン", "ぜったいれいど"}
                threat = False
                for mv in opp.moves:
                    if mv is None or mv.category == "status":
                        continue
                    if mv.name_jp in _ohko:
                        threat = True
                        break
                    eff = get_type_effectiveness(mv.type, me.type1, me.type2)
                    if eff > 1.0:
                        threat = True
                        break
                if threat:
                    self.logs.extend(my_side.opp_view.on_anticipation(opp.name))

    def _end_of_turn(self):
        # ひるみはそのターン限り＝次ターンへ持ち越さない（後攻が当てたひるみは無意味）
        self.side1.active.flinched = False
        self.side2.active.flinched = False
        # ノーてんき無効化フラグを最新化（とんぼがえり等の交代後にも対応）
        self.field._weather_negated = "ノーてんき" in (self.side1.active.ability, self.side2.active.ability)
        # 天候カウントを先に更新（終了ターンはダメージなし）
        if self.field.weather and self.field.weather_count > 0:
            self.field.weather_count -= 1
            if self.field.weather_count == 0:
                self.field.weather = None
                self.logs.append("天候がおわった！")

        # 天候ダメ・アイテム・状態異常
        for side, side_idx in [(self.side1, 0), (self.side2, 1)]:
            p = side.active
            if not p.is_alive:
                continue

            # 天候ダメ（ノーてんきが場にいると無効・effective_weatherで判定）
            if effective_weather(self.field, p) == "sandstorm":
                if p.type1 not in ("いわ","はがね","じめん") and \
                   (p.type2 is None or p.type2 not in ("いわ","はがね","じめん")) and \
                   p.ability not in ("すなかき","すながくれ","すなのちから","ぼうじん","マジックガード"):
                    dmg = max(1, p.max_hp // 16)
                    p.take_damage(dmg)
                    self.logs.append(f"{p.name} は すなあらし のダメージを受けた！({dmg})")
            # ゆき（旧あられ）: ターンダメージなし

            opp_side = self.side2 if side is self.side1 else self.side1

            # 状態異常・持ち物（個別に処理してログを出す）
            if p.ability != "マジックガード":
                # やけど
                if p.status == "burn":
                    dmg = max(1, p.max_hp // 16)
                    p.take_damage(dmg)
                    self.logs.append(f"{p.name} は やけど のダメージを受けた！({dmg})")
                # どく・もうどく
                elif p.status in ("poison", "badpoison"):
                    if p.ability == "ポイズンヒール":
                        heal = max(1, p.max_hp // 8)
                        p.hp = min(p.max_hp, p.hp + heal)
                        self.logs.append(f"{p.name} の ポイズンヒール で回復！(+{heal})")
                    elif p.status == "poison":
                        dmg = max(1, p.max_hp // 8)
                        p.take_damage(dmg)
                        self.logs.append(f"{p.name} は どく のダメージを受けた！({dmg})")
                    else:
                        p.bad_poison_count += 1
                        dmg = max(1, p.max_hp * p.bad_poison_count // 16)
                        p.take_damage(dmg)
                        self.logs.append(f"{p.name} は もうどく のダメージを受けた！({dmg})")

            if not p.is_alive:
                continue

            # ねをはる/アクアリング：ターン終了時HP1/16回復
            if (getattr(p, 'rooted', False) or getattr(p, 'aqua_ring', False)) and p.is_alive:
                heal = max(1, p.max_hp // 16)
                old_hp = p.hp
                p.hp = min(p.max_hp, p.hp + heal)
                if p.hp > old_hp:
                    src = "ねをはる" if getattr(p, 'rooted', False) else "アクアリング"
                    self.logs.append(f"{p.name} は {src} で HPが {p.hp - old_hp} 回復した！")

            # 持ち物回復・ダメージ（たべのこし等）
            if p.item == "たべのこし":
                heal = max(1, p.max_hp // 16)
                old_hp = p.hp
                p.hp = min(p.max_hp, p.hp + heal)
                if p.hp > old_hp:
                    self.logs.append(f"{p.name} の たべのこし で HPが {p.hp - old_hp} 回復した！")
                    self.logs.extend(opp_side.opp_view.on_item(p.name, "たべのこし", "ターン終了回復"))
            elif p.item == "くろいヘドロ":
                if "どく" in (p.type1, p.type2):
                    heal = max(1, p.max_hp // 16)
                    old_hp = p.hp
                    p.hp = min(p.max_hp, p.hp + heal)
                    if p.hp > old_hp:
                        self.logs.append(f"{p.name} の くろいヘドロ で HPが {p.hp - old_hp} 回復した！")
                        self.logs.extend(opp_side.opp_view.on_item(p.name, "くろいヘドロ", "ターン終了回復"))
                else:
                    dmg = max(1, p.max_hp // 16)
                    p.take_damage(dmg)
                    self.logs.append(f"{p.name} は くろいヘドロ のダメージを受けた！({dmg})")

            # きんちょうかん：相手がいるとこのポケモンはきのみを食べられない
            _berry_blocked = opp_side.active.is_alive and opp_side.active.ability == "きんちょうかん"

            # オボンのみ (HP半分以下)
            if not _berry_blocked and p.item == "オボンのみ" and p.hp <= p.max_hp // 2:
                heal = p.max_hp // 4
                p.hp = min(p.max_hp, p.hp + heal)
                p._last_berry = "オボンのみ"  # type: ignore
                p.item = None
                p.ate_berry = True
                on_item_consumed(p, [])
                self.logs.append(f"{p.name} の オボンのみ が発動！ HPが {heal} 回復した！")
                self.logs.extend(opp_side.opp_view.on_item(p.name, "オボンのみ", "HP回復から判明"))

            # オレンのみ (HP半分以下で10回復・固定値)
            if not _berry_blocked and p.item == "オレンのみ" and p.hp <= p.max_hp // 2:
                heal = 10
                p.hp = min(p.max_hp, p.hp + heal)
                p._last_berry = "オレンのみ"  # type: ignore
                p.item = None
                p.ate_berry = True
                on_item_consumed(p, [])
                self.logs.append(f"{p.name} の オレンのみ が発動！ HPが {heal} 回復した！")
                self.logs.extend(opp_side.opp_view.on_item(p.name, "オレンのみ", "HP回復から判明"))

            # ラムのみ・カゴのみ・モモンのみ・チーゴのみ
            if not _berry_blocked:
                try_cure_berry(p, self.logs)

            # しろいハーブ・メンタルハーブ
            try_white_herb(p, self.logs)
            try_mental_herb(p, self.logs)
            try_leppa_berry(p, self.logs)

            # ステータスきのみ（HP1/4以下で能力上昇）
            if not _berry_blocked:
                apply_hp_berry(p, self.logs)

            # かそく等のターン終了特性
            end_of_turn_ability(p, self.field, self.logs)

            # やどりぎのタネ吸収
            opp = (self.side2 if side is self.side1 else self.side1).active
            if p.seeded and p.is_alive:
                drain = max(1, p.max_hp // 8)
                p.take_damage(drain)
                self.logs.append(f"{p.name} は やどりぎのタネ で {drain} のダメージを受けた！")
                if opp.is_alive:
                    opp.hp = min(opp.max_hp, opp.hp + drain)
                    self.logs.append(f"{opp.name} は やどりぎのタネ で {drain} 回復した！")

            # しおづけ（ソルトキュア継続ダメ）はがね/みずは1/8、それ以外は1/16
            if getattr(p, '_salted', False) and p.is_alive:
                is_water_steel = "みず" in (p.type1, p.type2) or "はがね" in (p.type1, p.type2)
                rate = 1/8 if is_water_steel else 1/16
                dmg = max(1, math.floor(p.max_hp * rate))
                p.take_damage(dmg)
                self.logs.append(f"{p.name} は しおづけ のダメージを受けた！({dmg})")

            # あくびカウント（0になったらねむり）
            if p.yawn_count > 0:
                p.yawn_count -= 1
                if p.yawn_count == 0 and p.status is None:
                    if p.ability not in ("ふみん", "やるき"):
                        p.status = "sleep"
                        p.sleep_count = random.randint(1, 3)
                        self.logs.append(f"{p.name} は ねむって しまった！")

            # バインド継続ダメ・カウントダウン
            if p.bound_count > 0 and p.is_alive:
                bind_dmg = max(1, p.max_hp // 8)
                p.take_damage(bind_dmg)
                self.logs.append(f"{p.name} は バインド のダメージを受けた！({bind_dmg})")
                p.bound_count -= 1
                if p.bound_count == 0:
                    self.logs.append(f"{p.name} の バインド が解けた！")

            # じごくづきカウントダウン
            if p.throat_chop_count > 0:
                p.throat_chop_count -= 1

            # ちょうはつ・アンコール・封じカウント
            if p.taunt_count > 0:
                p.taunt_count -= 1
            if p.encore_count > 0:
                p.encore_count -= 1
                if p.encore_count == 0:
                    p.locked_move = None
            if p.disabled_turns > 0:
                p.disabled_turns -= 1
                if p.disabled_turns == 0:
                    p.disabled_move = None

            # まもる解除
            p.protecting = False
            p.enduring = False
            # みちづれ連続失敗フラグ：今ターンみちづれを使っていなければリセット
            if p.last_used_move != "みちづれ":
                p._destiny_bond_last_turn = False  # type: ignore
            # はねやすめのタイプ消失を復元
            if getattr(p, '_roost_types', None):
                p.type1, p.type2 = p._roost_types  # type: ignore
                p._roost_types = None  # type: ignore

            if p.syrup_count > 0:
                p.syrup_count -= 1
            if p.heal_block_count > 0:
                p.heal_block_count -= 1
            # じだんだ/やけっぱち：今ターンの技失敗を「前ターン失敗」へ繰り越す
            p._move_failed_last = getattr(p, '_move_failed_this_turn', False)  # type: ignore
            p._move_failed_this_turn = False  # type: ignore

            # 交代で出たターンは「場に出て行動できたターン」に数えない（次の行動ターンが最初＝
            # ねこだまし/であいがしらが交代後の初手で打てる。1ターン目限定バグの修正）。
            if getattr(p, '_switched_this_turn', False):
                p._switched_this_turn = False  # type: ignore
            else:
                p.turns_out += 1

        # ものひろい：両者のきのみ処理後、道具未所持なら相手が消費したきのみを拾う
        for _ms, _os in ((self.side1, self.side2), (self.side2, self.side1)):
            _mp = _ms.active
            if _mp.is_alive and _mp.ability == "ものひろい" and _mp.item is None \
                    and getattr(_os.active, "_last_berry", None):
                _mp.item = _os.active._last_berry  # type: ignore
                _os.active._last_berry = None  # type: ignore
                self.logs.append(f"{_mp.name} の ものひろい！ {_mp.item} を拾った！")

        # トリルカウント
        if self.field.trick_room and self.field.trick_room_count > 0:
            self.field.trick_room_count -= 1
            if self.field.trick_room_count == 0:
                self.field.trick_room = False

        # フィールドカウント
        for fname in ("misty_terrain", "electric_terrain", "psychic_terrain"):
            count_attr = fname + "_count"
            if getattr(self.field, fname, False):
                cnt = getattr(self.field, count_attr, 0) - 1
                setattr(self.field, count_attr, cnt)
                if cnt <= 0:
                    setattr(self.field, fname, False)
                    setattr(self.field, count_attr, 0)
                    self.logs.append(f"{fname.replace('_terrain','')} フィールドが終わった！")

        # ねがいごと（ウィッシュ回復）
        for side in [self.side1, self.side2]:
            if side.wish_count > 0:
                side.wish_count -= 1
                if side.wish_count == 0 and side.active.is_alive:
                    heal = min(side.wish_hp, side.active.max_hp - side.active.hp)
                    side.active.hp += heal
                    self.logs.append(f"{side.active.name} の ねがいごと が叶った！（+{heal}HP）")

        # みらいよち発動
        for side in [self.side1, self.side2]:
            if side.future_sight_count > 0:
                side.future_sight_count -= 1
                if side.future_sight_count == 0 and side.active.is_alive:
                    fs = side.future_sight_dmg
                    side.active.take_damage(fs)
                    self.logs.append(f"{side.active.name} は みらいよち の攻撃を受けた！({fs})")
                    if not side.active.is_alive:
                        self.logs.append(f"{side.active.name} は倒れた！")

        # ほろびのうた・のろい
        for side, opp_side in [(self.side1, self.side2), (self.side2, self.side1)]:
            p = side.active
            if not p.is_alive:
                continue
            if p.perish_count > 0:
                p.perish_count -= 1
                self.logs.append(f"{p.name} の ほろびのうた カウント：{p.perish_count}")
                if p.perish_count == 0:
                    p.take_damage(p.hp)
                    p.is_alive = False
                    self.logs.append(f"{p.name} は ほろびのうた で倒れた！")
            if p.cursed and p.is_alive:
                dmg = max(1, p.max_hp // 4)
                p.take_damage(dmg)
                self.logs.append(f"{p.name} は のろい のダメージを受けた！({dmg})")

        # スクリーン・おいかぜカウント
        for side in [self.side1, self.side2]:
            if side.reflect_count > 0:
                side.reflect_count -= 1
                if side.reflect_count == 0:
                    side.reflect = False
                    self.logs.append("リフレクター の効果が切れた！")
            if side.light_screen_count > 0:
                side.light_screen_count -= 1
                if side.light_screen_count == 0:
                    side.light_screen = False
                    self.logs.append("ひかりのかべ の効果が切れた！")
            if side.aurora_veil_count > 0:
                side.aurora_veil_count -= 1
                if side.aurora_veil_count == 0:
                    side.aurora_veil = False
                    self.logs.append("オーロラベール の効果が切れた！")
            if side.tailwind_count > 0:
                side.tailwind_count -= 1
                if side.tailwind_count == 0:
                    side.tailwind = False
                    self.logs.append("おいかぜ の効果が切れた！")

        # カウンター系トラッカーをリセット（次ターン用）
        for side in [self.side1, self.side2]:
            p = side.active
            p._last_physical_dmg_received = 0  # type: ignore
            p._last_special_dmg_received = 0   # type: ignore

        # ターン終了時に倒れたポケモンの交代（毒・やけど等によるKO）
        self._faint_switch(self.side1, self.side2)
        self._faint_switch(self.side2, self.side1)
