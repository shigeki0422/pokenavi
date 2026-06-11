"""戦略台本付き対戦相手（自己対戦プールに混ぜ、学習AIに人間戦略への対処を学ばせる）。

HeuristicAI同士の自己対戦には「受け・積み全抜き・粘り」が現れず、価値ネットがこれらの
人間戦略を分布外（OOD）として評価・対処できない。本モジュールの台本AIを相手に対戦させる
ことで、機構（学習）として対処を獲得させる。各台本は該当技が無ければHeuristicにフォールバック。
"""
import random

from .battle import Action, BattleSide, BattleField
from .ai import (HeuristicAI, should_mega_evolve, _forced_charging_action,
                 _filter_valid_by_lock, _filter_by_pp, _get_struggle)

SETUP_MOVES = {  # 技名 → 主に上げる能力（積み全抜き判定用）
    "つるぎのまい": "atk", "りゅうのまい": "atk", "ビルドアップ": "atk", "もりののろい": "atk",
    "めいそう": "spa", "わるだくみ": "spa", "ロックカット": "spd_spe",
    "からをやぶる": "all", "りゅうせいぐん": None,
}
RECOVERY_MOVES = ["はねやすめ", "なまける", "こうごうせい", "じこさいせい", "タマゴうみ",
                  "つきのひかり", "あさのひざし", "ねがいごと", "ミルクのみ"]
DEFENSE_SETUP = ["てっぺき", "とける", "めいそう", "ビルドアップ"]
STALL_MOVES = ["どくどく", "あくび", "まもる", "みがわり"]
WALL_ATTACKS = ["ボディプレス", "イカサマ", "ジャイロボール", "ナイトヘッド", "ちきゅうなげ"]


def _legal_moves(me):
    valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
    valid = _filter_valid_by_lock(valid, me)
    return _filter_by_pp(valid, me)


def _find(pp_valid, names):
    for nm in names:
        for i, mv in pp_valid:
            if mv.name_jp == nm:
                return i, mv
    return None


class _ScriptedBase:
    def __init__(self, seed=0):
        self._fallback = HeuristicAI()
        self._rng = random.Random(seed)
        self._last = None

    def _setup(self, my_side, opp_side, field):
        me = my_side.active
        if not me.is_alive:
            return self._fallback(my_side, opp_side, field), None, None, None
        forced = _forced_charging_action(me)
        if forced:
            return forced, None, None, None
        do_mega = should_mega_evolve(me, opp_side.active, field) and not my_side.mega_used
        pp_valid = _legal_moves(me)
        if not pp_valid:
            return Action(type="move", move=_get_struggle(), move_idx=-1, do_mega=do_mega), None, None, None
        return None, me, do_mega, pp_valid

    def _act(self, i, mv, do_mega):
        self._last = mv.name_jp
        return Action(type="move", move=mv, move_idx=i, do_mega=do_mega)


class SetupSweeperAI(_ScriptedBase):
    """高HPのうちに積み技で積み、その後最大火力で全抜きを狙う。"""
    def __call__(self, my_side, opp_side, field):
        done, me, do_mega, pp_valid = self._setup(my_side, opp_side, field)
        if done is not None:
            return done
        hp = me.hp / me.max_hp if me.max_hp else 0
        total_boost = me.stage_attack + me.stage_sp_attack + me.stage_speed
        if hp >= 0.55 and total_boost < 4:
            setup = [nm for nm in SETUP_MOVES if SETUP_MOVES[nm] is not None]
            hit = _find(pp_valid, setup)
            if hit:
                return self._act(hit[0], hit[1], do_mega)
        return self._fallback(my_side, opp_side, field)


class WallAI(_ScriptedBase):
    """硬く受け、回復で粘り、ボディプレス/イカサマ等で削る。"""
    def __call__(self, my_side, opp_side, field):
        done, me, do_mega, pp_valid = self._setup(my_side, opp_side, field)
        if done is not None:
            return done
        hp = me.hp / me.max_hp if me.max_hp else 0
        if hp < 0.55:
            hit = _find(pp_valid, RECOVERY_MOVES)
            if hit:
                return self._act(hit[0], hit[1], do_mega)
        if me.stage_defense < 2 and hp > 0.6:
            hit = _find(pp_valid, DEFENSE_SETUP)
            if hit:
                return self._act(hit[0], hit[1], do_mega)
        hit = _find(pp_valid, WALL_ATTACKS)
        if hit:
            return self._act(hit[0], hit[1], do_mega)
        return self._fallback(my_side, opp_side, field)


class StallAI(_ScriptedBase):
    """どくどく/あくび/まもる/ねがいごとで粘り、削り切る。"""
    def __call__(self, my_side, opp_side, field):
        done, me, do_mega, pp_valid = self._setup(my_side, opp_side, field)
        if done is not None:
            return done
        opp = opp_side.active
        hp = me.hp / me.max_hp if me.max_hp else 0
        if opp.status is None:
            hit = _find(pp_valid, ["どくどく"])
            if hit and self._rng.random() < 0.7:
                return self._act(hit[0], hit[1], do_mega)
        if hp < 0.5:
            hit = _find(pp_valid, RECOVERY_MOVES)
            if hit:
                return self._act(hit[0], hit[1], do_mega)
        if self._last not in ("まもる", "みがわり"):
            hit = _find(pp_valid, ["まもる", "みがわり"])
            if hit and self._rng.random() < 0.5:
                return self._act(hit[0], hit[1], do_mega)
        hit = _find(pp_valid, ["イカサマ", "ナイトヘッド", "ちきゅうなげ"])
        if hit:
            return self._act(hit[0], hit[1], do_mega)
        return self._fallback(my_side, opp_side, field)


class BatonSweepAI(_ScriptedBase):
    """積み（からをやぶる/めいそう/まもる積み）→バトンタッチでエースに繋ぎ全抜き。"""
    def __call__(self, my_side, opp_side, field):
        done, me, do_mega, pp_valid = self._setup(my_side, opp_side, field)
        if done is not None:
            return done
        total_boost = (me.stage_attack + me.stage_sp_attack + me.stage_speed
                       + me.stage_defense + me.stage_sp_defense)
        baton = _find(pp_valid, ["バトンタッチ"])
        # 十分積んだ or 危険ならバトンで繋ぐ
        if baton and (total_boost >= 3 or (me.hp / me.max_hp if me.max_hp else 0) < 0.5):
            return self._act(baton[0], baton[1], do_mega)
        # まだ積めるなら積む
        if total_boost < 4:
            setup = [nm for nm in SETUP_MOVES if SETUP_MOVES[nm] is not None]
            hit = _find(pp_valid, setup + ["まもる"])
            if hit:
                return self._act(hit[0], hit[1], do_mega)
        return self._fallback(my_side, opp_side, field)


def make_strategy(name, seed=0):
    return {"setup": SetupSweeperAI, "wall": WallAI, "stall": StallAI,
            "baton": BatonSweepAI}[name](seed)


STRATEGY_NAMES = ["setup", "wall", "stall", "baton"]
