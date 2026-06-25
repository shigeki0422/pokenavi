"""
AI行動決定モジュール
usage_rate重み付き確率選択 + ダメージ期待値計算の2軸
"""
import copy
import math
import os
import random
from typing import List, Optional
from .battle import Action, BattleSide, BattleField, crit_chance
from .pokemon import BattlePokemon
from .data import get_type_effectiveness, DataLoader
from .damage import calc_damage
from .items import get_speed_item_multiplier

HAZARD_MOVES = {"ステルスロック", "まきびし", "スパイク", "どくびし"}
_AVG_HP = 170  # 設置技価値計算用 平均HP概算


def _hazard_value(move_name: str, my_side: BattleSide, opp_side: BattleSide,
                  field: BattleField) -> float:
    """
    設置技の残りゲーム価値を返す。
    相手の残りポケモン数・すでに設置済みかどうかで増減する。
    相手が1匹しかいない場合は0（交代が発生しないので無価値）。
    """
    opp_remaining = sum(1 for p in opp_side.party if p.is_alive)
    if opp_remaining <= 1:
        return 0.0

    # 全員が少なくとも1回は入場すると仮定（すでに場に出ているポケモンも交代後に再入場しうる）
    # ターン数が早いほど多くのポケモンに効果が発生するため、opp_remaining全体を使う
    entries_remaining = opp_remaining
    opp_idx = getattr(opp_side, 'field_idx', 1)

    if move_name == "ステルスロック":
        if (opp_side.stealth_rock_set
                or getattr(opp_side, '_stealth_rock_pending', False)
                or field.stealth_rock[opp_idx]):
            return 0.0
        return entries_remaining * _AVG_HP * 0.125

    if move_name in ("まきびし", "スパイク"):
        layers = field.spikes[opp_idx]
        if layers >= 3:
            return 0.0
        dmg_by_layer = [0.125, 1 / 6, 0.25]
        next_dmg = dmg_by_layer[min(layers, 2)]
        return entries_remaining * _AVG_HP * next_dmg

    if move_name == "どくびし":
        layers = field.toxic_spikes[opp_idx]
        if layers >= 2:
            return 0.0
        return entries_remaining * _AVG_HP * 0.09

    return 0.0


def expected_damage(attacker: BattlePokemon, defender: BattlePokemon,
                    move, field: BattleField) -> float:
    """ダメージ期待値（命中率考慮）"""
    if move is None or move.category == "status" or move.power is None:
        return 0.0
    acc = (move.accuracy or 100) / 100
    eff = get_type_effectiveness(move.type, defender.type1, defender.type2)
    if eff == 0:
        return 0.0
    dmg = calc_damage(attacker, defender, move, field, critical=False, random_roll=0.5)
    # 急所期待値（トリックフラワー等の必中急所はpc=1.0でcalc_damage(critical=True)になる）
    pc = crit_chance(attacker, move, defender)
    if pc > 0:
        dmg_crit = calc_damage(attacker, defender, move, field, critical=True, random_roll=0.5)
        dmg = dmg * (1 - pc) + dmg_crit * pc
    # へんげんじざい/リベロ: 技使用時にその技タイプへ変化するため全攻撃技がタイプ一致。
    # 選出評価ではタイプ変化前のため、非一致技にSTAB(1.5)を補正（実戦のcalc_damageは
    # 技前に変化済みで二重計上にならない＝ここは選出スコア専用）。
    if attacker.ability in ("へんげんじざい", "リベロ") \
            and move.type not in (attacker.type1, attacker.type2):
        dmg *= 1.5
    return dmg * acc


def _best_expected_damage(poke: BattlePokemon, opp: BattlePokemon,
                          field: BattleField) -> float:
    return max(
        (expected_damage(poke, opp, mv, field) for mv in poke.moves if mv),
        default=0.0,
    )


def _is_likely_threatened(me: BattlePokemon, opp: BattlePokemon,
                           known_move_names: List[str]) -> bool:
    """現在のポケモンが相手から弱点を突かれそうか判定"""
    for mv in opp.moves:
        if mv and mv.name_jp in known_move_names:
            if get_type_effectiveness(mv.type, me.type1, me.type2) >= 2.0:
                return True
    for t in [opp.type1, opp.type2]:
        if t and get_type_effectiveness(t, me.type1, me.type2) >= 2.0:
            return True
    return False


def _matchup_score(p: BattlePokemon, opp: BattlePokemon) -> int:
    """ポケモン対相手の相性スコア（攻撃+防御の合計）"""
    has_se = any(
        get_type_effectiveness(mv.type, opp.type1, opp.type2) >= 2.0
        for mv in p.moves if mv and mv.category != "status" and mv.power
    )
    opp_stab_max = max(
        (get_type_effectiveness(t, p.type1, p.type2) for t in [opp.type1, opp.type2] if t),
        default=1.0
    )
    score = 0
    if has_se:
        score += 2
    if opp_stab_max <= 0.5:
        score += 2
    elif opp_stab_max <= 1.0:
        score += 1
    return score


def _best_switch_target(my_side: BattleSide, opp_side: BattleSide,
                        field: BattleField) -> Optional[int]:
    """脅威下で相性改善できる控えがいれば交代先インデックスを返す"""
    me = my_side.active
    opp = opp_side.active

    if me.locked_move or me.bound_count > 0 or getattr(me, '_switched_this_turn', False):
        return None

    benched = [(i, p) for i, p in enumerate(my_side.party)
               if p.is_alive and i != my_side.active_idx]
    if not benched:
        return None

    known_moves = my_side.opp_view.known_moves_of(opp.name)
    if not _is_likely_threatened(me, opp, known_moves):
        return None

    current_score = _matchup_score(me, opp)
    best_idx, best_score, best_hp_ratio = None, current_score, 0.0
    for i, p in benched:
        s = _matchup_score(p, opp)
        hp_ratio = p.hp / (p.max_hp or 1)
        if s > best_score or (s == best_score and s > current_score and hp_ratio > best_hp_ratio):
            best_score, best_idx, best_hp_ratio = s, i, hp_ratio

    return best_idx


def _effective_speed(poke: BattlePokemon, field: BattleField) -> int:
    spd = math.floor(poke.get_effective_speed() * get_speed_item_multiplier(poke.item))
    if field.weather == "rain" and poke.ability == "すいすい":
        spd *= 2
    if field.weather == "sunny" and poke.ability == "ようりょくそ":
        spd *= 2
    if field.weather in ("sandstorm", "hail") and poke.ability == "すながくれ":
        spd = math.floor(spd * 1.5)
    return spd


def _goes_first(me: BattlePokemon, opp: BattlePokemon,
                my_move_priority: int, field: BattleField) -> bool:
    """自分が指定優先度の技を使った時に先制できるか推定"""
    opp_max_priority = max((mv.priority for mv in opp.moves if mv), default=0)
    if my_move_priority != opp_max_priority:
        return my_move_priority > opp_max_priority
    my_spd = _effective_speed(me, field)
    opp_spd = _effective_speed(opp, field)
    return (my_spd >= opp_spd) if not field.trick_room else (my_spd <= opp_spd)


def _can_ko(attacker: BattlePokemon, defender: BattlePokemon,
            move, field: BattleField) -> bool:
    """この技で相手をKOできるか（期待値50%ロールで判定）"""
    if move is None or not move.power or move.category == "status":
        return False
    eff = get_type_effectiveness(move.type, defender.type1, defender.type2)
    if eff == 0:
        return False
    dmg = calc_damage(attacker, defender, move, field, critical=False, random_roll=0.5)
    return dmg >= defender.hp


def _opp_priority_threatens(me: BattlePokemon, opp: BattlePokemon,
                              field: BattleField) -> bool:
    """相手の先制技でKOされる可能性があるか（全技を参照=メタ知識）"""
    for mv in opp.moves:
        if mv and mv.priority > 0 and mv.power:
            dmg = calc_damage(opp, me, mv, field, critical=False, random_roll=1.0)
            if dmg >= me.hp:
                return True
    return False


def _priority_ko_action(me: BattlePokemon, opp: BattlePokemon,
                        valid, field: BattleField, do_mega: bool) -> Optional[Action]:
    """先制技でKOできるなら最善のActionを返す"""
    candidates = [
        (i, mv) for i, mv in valid
        if mv.priority > 0 and mv.power
        and _goes_first(me, opp, mv.priority, field)
        and _can_ko(me, opp, mv, field)
    ]
    if not candidates:
        return None
    best_i, best_mv = max(candidates, key=lambda x: expected_damage(me, opp, x[1], field))
    return Action(type="move", move=best_mv, move_idx=best_i, do_mega=do_mega)


def certain_ko_override(act, my_side: BattleSide, opp_side: BattleSide, field: BattleField):
    """確定KO安全弁：先制（または優先度）で最低ロールでもOHKOできる攻撃技があれば、それを最優先。
    任意AI(MCTS/ネット)の出力 act を受け、確実に倒せる手を逃している場合のみ上書きする。
    積み・変化技で自滅する誤選択や、弱い攻撃技を選ぶミス(例トリックフラワー<はたきおとす)を防ぐ。"""
    me = my_side.active; opp = opp_side.active
    if me is None or opp is None or not me.is_alive or not opp.is_alive:
        return act
    if _forced_charging_action(me):                 # 溜め中などは介入しない
        return act
    full = opp.hp == opp.max_hp
    if full and (opp.ability in ("マルチスケイル", "ファントムガード")
                 or opp.item == "きあいのタスキ" or opp.ability == "がんじょう"):
        return act                                  # 満タンで耐える系は確定KO不成立→介入しない
    valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
    valid = _filter_by_pp(_filter_valid_by_lock(valid, me), me)
    best = None; bestd = -1
    for i, mv in valid:
        if not mv.power or mv.category == "status":
            continue
        if get_type_effectiveness(mv.type, opp.type1, opp.type2) == 0:
            continue
        if not _goes_first(me, opp, mv.priority, field):
            continue
        d = calc_damage(me, opp, mv, field, critical=False, random_roll=0.85)   # 最低ロールでKO=確定
        if d >= opp.hp and d > bestd:
            bestd = d; best = (i, mv)
    if best is None:
        return act
    if act and getattr(act, "type", None) == "move" and act.move is best[1]:
        return act                                  # 既に同じ手を選んでいる
    return Action(type="move", move=best[1], move_idx=best[0],
                  do_mega=bool(act and getattr(act, "do_mega", False)))


# 崩し（壁対策）用の積み技
SETUP_MOVES = {
    "つるぎのまい", "りゅうのまい", "ちょうのまい", "めいそう", "わるだくみ",
    "からをやぶる", "てっぺき", "ビルドアップ", "ロックカット", "こうそくいどう",
    "せいちょう", "とぐろをまく", "コットンガード", "はらだいこ",
}


def _poison_immune(opp: BattlePokemon) -> bool:
    """どくどくが無効/逆効果か（はがね・どくタイプ、めんえき等、ポイズンヒール）。"""
    if "どく" in (opp.type1, opp.type2) or "はがね" in (opp.type1, opp.type2):
        return True
    return opp.ability in ("めんえき", "きよめのしお", "マジックガード", "ポイズンヒール")


def _wall_break_action(me: BattlePokemon, opp: BattlePokemon, valid,
                       field: BattleField, do_mega: bool) -> Optional[Action]:
    """相手を有効打で崩せない（壁）時の崩し手段。どくどく＞ちょうはつ＞安全な積み。"""
    bounces = (opp.ability == "マジックミラー")  # 変化技を跳ね返す
    # 1. どくどく：受けをじわじわ枯らす（最有力）
    for i, mv in valid:
        if (mv.name_jp == "どくどく" and opp.status is None
                and not _poison_immune(opp) and not bounces):
            return Action(type="move", move=mv, move_idx=i)
    # 2. ちょうはつ：回復/積み/設置などの変化技を封じる
    opp_has_utility = any(m and m.category == "status" for m in opp.moves)
    if opp_has_utility and not bounces:
        for i, mv in valid:
            if mv.name_jp == "ちょうはつ" and opp.taunt_count == 0:
                return Action(type="move", move=mv, move_idx=i)
    # 3. 積み：相手の打点が低く安全なら起点化
    opp_best = max((expected_damage(opp, me, m, field) for m in opp.moves if m and m.power),
                   default=0.0)
    my_stages = (me.stage_attack + me.stage_sp_attack + me.stage_speed
                 + me.stage_defense + me.stage_sp_defense)
    if opp_best < me.hp * 0.4 and my_stages < 6:
        for i, mv in valid:
            if mv.name_jp in SETUP_MOVES:
                return Action(type="move", move=mv, move_idx=i, do_mega=do_mega)
    return None


def should_mega_evolve(me: BattlePokemon, opp: BattlePokemon,
                       field: BattleField) -> bool:
    """メガ進化すべきかを判断する。

    メガ進化はターンを消費せず、種族値・特性・タイプが基本的に強化されるため、
    石を持っているなら原則として即メガが最善（熟練プレイヤーの定石）。
    例外的な「メガしない方が良い」局面は探索側(SearchAI)が独立に判断する。
    """
    if me.mega_data is None or me.mega_evolved:
        return False
    return True


def _forced_charging_action(me: BattlePokemon) -> Optional[Action]:
    """溜め中の場合、同じ技を強制継続するActionを返す"""
    if not me.charging_move:
        return None
    for i, mv in enumerate(me.moves):
        if mv and mv.name_jp == me.charging_move:
            return Action(type="move", move=mv, move_idx=i, do_mega=False)
    me.charging_move = None
    return None


def _filter_valid_by_lock(valid: list, me: BattlePokemon) -> list:
    """こだわり縛り・アンコール・あばれ状態・のろわれボディによる技制限を適用"""
    if me.disabled_move:
        valid = [(i, mv) for i, mv in valid if mv.name_jp != me.disabled_move]
    # あばれ状態(lock_count>0)・アンコール・こだわり縛りの優先順で固定技を決定
    lock = (
        me.choice_locked_move
        or (me.locked_move if (me.encore_count > 0 or me.lock_count > 0) else None)
    )
    if lock:
        locked = [(i, mv) for i, mv in valid if mv.name_jp == lock]
        return locked if locked else valid
    return valid if valid else [(i, mv) for i, mv in enumerate(me.moves) if mv]


def _filter_by_pp(valid: list, me: BattlePokemon) -> list:
    """PP>0の技のみ返す。全PP切れならわるあがき用に空リストを返す"""
    pp_valid = [(i, mv) for i, mv in valid if i < len(me.pp) and me.pp[i] > 0]
    return pp_valid


_STRUGGLE_MOVE = None

def _get_struggle():
    global _STRUGGLE_MOVE
    if _STRUGGLE_MOVE is None:
        from .data import MoveData
        _STRUGGLE_MOVE = MoveData(
            name_jp="わるあがき", name_en="Struggle",
            type="ノーマル", category="physical",
            power=50, accuracy=100, priority=0, pp=1, effect_id=None,
        )
    return _STRUGGLE_MOVE


class GreedyAI:
    """ばつぐん技優先、なければダメージ期待値最大の技を選ぶ。交代は考慮しない。"""

    def __call__(self, my_side: BattleSide, opp_side: BattleSide,
                 field: BattleField) -> Action:
        me = my_side.active
        opp = opp_side.active

        if not me.is_alive:
            return Action(type="pass")

        forced = _forced_charging_action(me)
        if forced:
            return forced

        do_mega = should_mega_evolve(me, opp, field) and not my_side.mega_used

        valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
        if not valid:
            return Action(type="pass")

        valid = _filter_valid_by_lock(valid, me)
        pp_valid = _filter_by_pp(valid, me)
        if not pp_valid:
            return Action(type="move", move=_get_struggle(), move_idx=-1, do_mega=do_mega)
        valid = pp_valid

        supereff = [
            (i, mv) for i, mv in valid
            if mv.category != "status" and mv.power
            and get_type_effectiveness(mv.type, opp.type1, opp.type2) >= 2.0
        ]
        if supereff:
            best_i, best_mv = max(supereff, key=lambda x: expected_damage(me, opp, x[1], field))
            return Action(type="move", move=best_mv, move_idx=best_i, do_mega=do_mega)

        dmg_moves = [(i, mv) for i, mv in valid if mv.category != "status" and mv.power]
        if dmg_moves:
            best_i, best_mv = max(dmg_moves, key=lambda x: expected_damage(me, opp, x[1], field))
            return Action(type="move", move=best_mv, move_idx=best_i, do_mega=do_mega)

        return Action(type="move", move=valid[0][1], move_idx=valid[0][0], do_mega=do_mega)


class RandomAI:
    """使用率に比例した確率で技を選ぶ（実際のプレイヤー分布を近似）"""

    def __call__(self, my_side: BattleSide, opp_side: BattleSide,
                 field: BattleField) -> Action:
        me = my_side.active
        opp = opp_side.active
        if not me.is_alive:
            return Action(type="pass")

        forced = _forced_charging_action(me)
        if forced:
            return forced

        do_mega = should_mega_evolve(me, opp, field) and not my_side.mega_used

        valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
        if not valid:
            return Action(type="pass")

        valid = _filter_valid_by_lock(valid, me)
        pp_valid = _filter_by_pp(valid, me)
        if not pp_valid:
            return Action(type="move", move=_get_struggle(), move_idx=-1, do_mega=do_mega)
        valid = pp_valid

        idx, move = random.choice(valid)
        return Action(type="move", move=move, move_idx=idx, do_mega=do_mega)


class HeuristicAI:
    """
    ばつぐん技優先 + タイプ相性ベースの交代判断。
    alpha は後方互換のため残すが使用しない。
    """

    def __init__(self, alpha: float = 0.7, enable_tactics: bool = True,
                 finish_priority: Optional[bool] = None, wall_break: Optional[bool] = None):
        self.alpha = alpha
        self.enable_tactics = enable_tactics  # 数ターン戦略(ねがいごと/バトン等)の総合フラグ
        # 詰め(先制仕留め)・崩し(wall認識)を個別制御。未指定は enable_tactics に従う
        self.finish_priority = enable_tactics if finish_priority is None else finish_priority
        self.wall_break = enable_tactics if wall_break is None else wall_break

    def __call__(self, my_side: BattleSide, opp_side: BattleSide,
                 field: BattleField) -> Action:
        me = my_side.active
        opp = opp_side.active
        if not me.is_alive:
            return Action(type="pass")

        forced = _forced_charging_action(me)
        if forced:
            return forced

        do_mega = should_mega_evolve(me, opp, field) and not my_side.mega_used

        valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
        if not valid:
            return Action(type="pass")

        valid = _filter_valid_by_lock(valid, me)
        pp_valid = _filter_by_pp(valid, me)
        if not pp_valid:
            return Action(type="move", move=_get_struggle(), move_idx=-1, do_mega=do_mega)
        valid = pp_valid

        # 交代判断（相性が悪いなら交代。かげふみ等で交代不可なら不可）
        from .battle import is_trapped
        switch_idx = None if is_trapped(me, opp) else _best_switch_target(my_side, opp_side, field)
        if switch_idx is not None:
            return Action(type="switch", switch_to=switch_idx)

        # ── 数ターン戦略（居座る時のコンボ）: ねがいごと→まもる / バトン構築 ──
        if self.enable_tactics:
            mv_names = {mv.name_jp for _, mv in valid}
            can_ko_now = any(_can_ko(me, opp, mv, field)
                             for _, mv in valid if mv.power and mv.category != "status")
            opp_best = max((expected_damage(opp, me, m, field)
                            for m in opp.moves if m and m.power), default=0.0)
            # 直前にねがいごと発動済み → まもるで安全に回復を受ける（初回まもるは必ず成功）
            if (my_side.wish_count > 0 and "まもる" in mv_names
                    and me.protect_consecutive == 0 and not can_ko_now):
                for i, mv in valid:
                    if mv.name_jp == "まもる":
                        return Action(type="move", move=mv, move_idx=i)
            # HP減＋ねがいごと未発動かつ今KOされない → ねがいごと（疑似回復の起点）
            if (my_side.wish_count == 0 and me.hp < me.max_hp * 0.6 and "ねがいごと" in mv_names
                    and not can_ko_now and opp_best < me.hp):
                for i, mv in valid:
                    if mv.name_jp == "ねがいごと":
                        return Action(type="move", move=mv, move_idx=i)
            # バトン構築: 積み技/かそくで能力上昇、十分積んだ/危険なら エースへバトンタッチ
            if "バトンタッチ" in mv_names and not can_ko_now:
                bench = any(p.is_alive for j, p in enumerate(my_side.party) if j != my_side.active_idx)
                if bench:
                    boosts = max(0, me.stage_attack) + max(0, me.stage_sp_attack) + max(0, me.stage_speed)
                    setup_here = [(i, mv) for i, mv in valid if mv.name_jp in SETUP_MOVES]
                    if boosts >= 2 or opp_best >= me.hp * 0.5:
                        for i, mv in valid:
                            if mv.name_jp == "バトンタッチ":
                                return Action(type="move", move=mv, move_idx=i)
                    if opp_best < me.hp * 0.45 and boosts < 4 and setup_here:
                        i, mv = setup_here[0]
                        return Action(type="move", move=mv, move_idx=i, do_mega=do_mega)
                    if (opp_best < me.hp * 0.45 and me.ability == "かそく"
                            and me.stage_speed < 3 and me.protect_consecutive == 0
                            and "まもる" in mv_names):
                        for i, mv in valid:
                            if mv.name_jp == "まもる":
                                return Action(type="move", move=mv, move_idx=i)

        # ── 先制技 KO 判定 ────────────────────────────────────────────
        # 条件A: 後攻になる通常行動 → 相手にKOされる → 先制技でKOできる
        my_spd = _effective_speed(me, field)
        opp_spd = _effective_speed(opp, field)
        i_go_second = (my_spd < opp_spd) if not field.trick_room else (my_spd > opp_spd)
        opp_normal_ko = any(
            _can_ko(opp, me, mv, field)
            for mv in opp.moves if mv and mv.power and mv.category != "status"
        )
        if i_go_second and opp_normal_ko:
            act = _priority_ko_action(me, opp, valid, field, do_mega)
            if act:
                return act

        # 条件B: 相手の先制技でKOされそう → 自分の先制技で返す
        if _opp_priority_threatens(me, opp, field):
            act = _priority_ko_action(me, opp, valid, field, do_mega)
            if act:
                return act

        # 条件C（詰め）: 先制技で確実に仕留められるなら相手に行動させず倒す
        if self.finish_priority:
            act = _priority_ko_action(me, opp, valid, field, do_mega)
            if act:
                return act

        # ── 通常の技選択 ─────────────────────────────────────────────

        # 設置技の価値評価
        hazard_candidates = [
            (i, mv) for i, mv in valid
            if mv.category == "status" and mv.name_jp in HAZARD_MOVES
        ]
        dmg_moves = [(i, mv) for i, mv in valid if mv.category != "status" and mv.power]
        if hazard_candidates:
            # このターンに相手をKOできるかチェック
            can_ko_now = any(_can_ko(me, opp, mv, field) for _, mv in dmg_moves)
            # KOできない場合 → 価値がある設置技を最優先
            if not can_ko_now:
                best_hazard = max(
                    hazard_candidates,
                    key=lambda x: _hazard_value(x[1].name_jp, my_side, opp_side, field)
                )
                if _hazard_value(best_hazard[1].name_jp, my_side, opp_side, field) > 0:
                    return Action(type="move", move=best_hazard[1], move_idx=best_hazard[0], do_mega=False)
            else:
                # KOできる → 設置技の価値がダメ期待値より明確に高い場合のみ
                best_dmg = max(
                    (expected_damage(me, opp, mv, field) for _, mv in dmg_moves),
                    default=0.0
                )
                for i, mv in hazard_candidates:
                    if _hazard_value(mv.name_jp, my_side, opp_side, field) > best_dmg * 1.5:
                        return Action(type="move", move=mv, move_idx=i, do_mega=False)

        # ── 壁認識: 有効打で崩せない（3発でも落とせない）なら崩し手段へ ──
        best_dmg = max((expected_damage(me, opp, mv, field) for _, mv in dmg_moves), default=0.0)
        if self.wall_break and best_dmg * 3 < opp.hp:
            wact = _wall_break_action(me, opp, valid, field, do_mega)
            if wact:
                return wact

        # ばつぐん技（ダメージ技）があれば最優先
        supereff = [
            (i, mv) for i, mv in dmg_moves
            if get_type_effectiveness(mv.type, opp.type1, opp.type2) >= 2.0
        ]
        if supereff:
            best_i, best_mv = max(supereff, key=lambda x: expected_damage(me, opp, x[1], field))
            return Action(type="move", move=best_mv, move_idx=best_i, do_mega=do_mega)

        # ダメージ技から期待値最大を選択
        if dmg_moves:
            best_i, best_mv = max(dmg_moves, key=lambda x: expected_damage(me, opp, x[1], field))
            return Action(type="move", move=best_mv, move_idx=best_i, do_mega=do_mega)

        # 変化技のみの場合はそのまま使う
        return Action(type="move", move=valid[0][1], move_idx=valid[0][0], do_mega=do_mega)


# デフォルトAI
DEFAULT_AI = HeuristicAI(alpha=0.7)


def _temp_sample_indices(scores: List[float], n: int, temperature: float, rng) -> List[int]:
    """スコアを標準化し softmax(z/T) で n 個を非復元サンプリング（温度付き選出）。"""
    m = sum(scores) / len(scores)
    sd = (sum((s - m) ** 2 for s in scores) / len(scores)) ** 0.5 or 1.0
    z = [(s - m) / sd for s in scores]
    pool = list(range(len(scores))); chosen = []
    for _ in range(min(n, len(pool))):
        ws = [math.exp(z[i] / max(1e-6, temperature)) for i in pool]
        tot = sum(ws); r = rng.random() * tot
        for k, i in enumerate(pool):
            r -= ws[k]
            if r <= 0:
                chosen.append(pool.pop(k)); break
        else:
            chosen.append(pool.pop())
    return chosen


def select_party(party6: List[BattlePokemon], opp6: List[BattlePokemon],
                 loader: DataLoader, n: int = 3,
                 temperature: float = 0.0, rng=None) -> List[BattlePokemon]:
    """
    6匹から3匹選出するAI。
    - 各相手に対する最善技ダメージ期待値の合計でベーススコアを計算
    - 設置技持ちにはゲーム価値ボーナス（相手6匹×将来の交代数を想定）
    - タイプ重複ペナルティ
    - 選出後、リード（先頭）は設置技持ち or 多数相手に有利なポケモンを優先
    temperature>0 で選出をスコアの softmax から確率的にサンプル（多様性付与）。0で従来の決定的選出。
    """
    if len(party6) <= n:
        return _order_by_lead(list(party6), opp6, temperature, rng or random)

    dummy_field = BattleField()

    def _poke_score(poke: BattlePokemon, as_mega: bool = False) -> float:
        # 相手6体それぞれとの1v1優劣を合計する。
        # 各対面で「上から確一」「ダメージレースの優劣」「素早さ」を評価し、
        # サブウェポンの抜群（へんげんじざい等のSTABはexpected_damage側で補正）と
        # スカーフ等の素早さ（上から動けるか）を反映する。
        # as_mega=True かつメガ石持ちなら、メガ後の姿（種族値・特性・タイプ）で採点する。
        p = poke
        if as_mega and getattr(poke, "mega_data", None) is not None and not poke.mega_evolved:
            p = copy.deepcopy(poke); p.do_mega_evolve()
        my_hp = max(1.0, p.max_hp)
        my_spd = _effective_speed(p, dummy_field)
        val = 0.0
        for opp in opp6:
            opp_hp = max(1.0, opp.max_hp)
            my_best = _best_expected_damage(p, opp, dummy_field)
            opp_best = _best_expected_damage(opp, p, dummy_field)
            faster = my_spd >= _effective_speed(opp, dummy_field)
            my_ko = my_best >= opp_hp
            opp_ko = opp_best >= my_hp
            if my_ko and faster:
                mv = 2.0                       # 上から確一＝最良の対面
            elif my_ko and not opp_ko:
                mv = 1.3                       # 確一を持ち、相手の一撃は耐える
            elif opp_ko and not faster and not my_ko:
                mv = -1.5                       # 上から一撃で落とされる不利対面
            else:
                mr = min(my_best / opp_hp, 1.5)
                orr = min(opp_best / my_hp, 1.5)
                mv = (mr - orr) + (0.3 if faster else -0.3)  # ダメージレース＋先制の優劣
            val += mv
        # 設置技ボーナス（後続の起点作り価値）
        if any(mv and mv.name_jp in HAZARD_MOVES and mv.category == "status"
               for mv in p.moves):
            val += 2.0
        return val

    # メガは1試合1体のみ進化可。メガ石持ちのうち最も得な1体だけメガ後で評価し、
    # 2体目以降のメガ石持ちには減点を与える（メガできない＝素の姿で戦う前提のコスト）。
    # 2メガ選出は相手次第でどちらをメガするか選べる柔軟性が強いので、減点は控えめにする。
    # env MEGA_PENALTY で調整可（既定50。検証では下げても2メガ選出はほぼ増えず勝率も改善せず＝元値維持）。
    MEGA_PENALTY = float(os.environ.get("MEGA_PENALTY", "50"))
    _mega_caps = [mp for mp in party6
                  if getattr(mp, "mega_data", None) is not None and not mp.mega_evolved]
    _mbest = max(_mega_caps, key=lambda mp: _poke_score(mp, as_mega=True)) if _mega_caps else None

    def _eff_score(poke: BattlePokemon) -> float:
        is_cap = getattr(poke, "mega_data", None) is not None and not poke.mega_evolved
        if poke is _mbest:
            return _poke_score(poke, as_mega=True)                       # メガする1体＝メガ後評価
        if is_cap:
            return _poke_score(poke, as_mega=False) - MEGA_PENALTY       # 2体目以降のメガ石持ち
        return _poke_score(poke, as_mega=False)                          # 非メガ＝素評価

    if temperature and temperature > 0:   # 温度付きサンプリング選出
        scores = [_eff_score(p) for p in party6]
        idx = _temp_sample_indices(scores, n, temperature, rng or random)
        return _order_by_lead([party6[i] for i in idx], opp6, temperature, rng or random)

    indexed = sorted(enumerate(party6), key=lambda x: _eff_score(x[1]), reverse=True)

    selected: List[BattlePokemon] = []
    seen_type_pairs: List[tuple] = []
    for _, poke in indexed:
        if len(selected) >= n:
            break
        tp = (poke.type1, poke.type2)
        if seen_type_pairs.count(tp) >= 2:
            continue
        selected.append(poke)
        seen_type_pairs.append(tp)

    for _, poke in indexed:
        if len(selected) >= n:
            break
        if poke not in selected:
            selected.append(poke)

    return _order_by_lead(selected[:n], opp6)


def _order_by_lead(party: List[BattlePokemon], opp6: List[BattlePokemon],
                   temperature: float = 0.0, rng=None) -> List[BattlePokemon]:
    """
    選出済みパーティの中からリード（先頭）を選んで並び替える。
    評価: 設置技（起点作り）＋相手の多数にばつぐんを出せるか。
    temperature>0 なら lead スコアの softmax から確率的にサンプル（リードを多様化）。
    """
    if not party or len(party) == 1:
        return party

    def _lead_score(poke: BattlePokemon) -> float:
        has_hazard = any(
            mv and mv.name_jp in HAZARD_MOVES and mv.category == "status"
            for mv in poke.moves
        )
        se_count = sum(
            1 for opp in opp6
            if any(
                get_type_effectiveness(mv.type, opp.type1, opp.type2) >= 2.0
                for mv in poke.moves
                if mv and mv.category != "status" and mv.power
            )
        )
        # 設置技は起点作りとして優位だが、温度で他のリードにもばらけるよう緩めの重み。
        return (2.0 if has_hazard else 0.0) + se_count

    scores = [_lead_score(p) for p in party]
    if temperature and temperature > 0:
        r = rng or random
        m = sum(scores) / len(scores)
        sd = (sum((s - m) ** 2 for s in scores) / len(scores)) ** 0.5 or 1.0
        ws = [math.exp(((s - m) / sd) / max(1e-6, temperature)) for s in scores]
        tot = sum(ws); pick = r.random() * tot; lead_i = len(ws) - 1
        acc = 0.0
        for i, w in enumerate(ws):
            acc += w
            if pick <= acc:
                lead_i = i
                break
    else:
        lead_i = max(range(len(party)), key=lambda i: scores[i])

    if lead_i != 0:
        party[0], party[lead_i] = party[lead_i], party[0]
    return party
