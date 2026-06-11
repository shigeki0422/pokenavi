"""行動方策（Phase 2: 決定化ロールアウト探索）。

毎ターン、開示情報＋belief（非開示情報の推定）から相手構成をK通りサンプリング（決定化）し、
各候補行動について短いロールアウトで勝率を見積もり、勝率最大（＝負ける確率最小）の行動を選ぶ。

- 相手の非開示情報（EV/性格・持ち物・特性・未開示技）は belief からサンプリングして具体化。
  観測可能な状態（現在HP割合・ランク変化・状態異常・場・メガ）はクローン元から保持する。
- 自分側は既知なのでそのまま。ロールアウトの行動は高速な rollout_ai（既定 HeuristicAI）。
- K個の決定化世界を全候補で共通利用（common random numbers）して候補間の分散を抑える。
"""
import copy
import random
from typing import List, Optional

from .battle import Action, Battle, BattleSide, BattleField, is_trapped
from .data import DataLoader, NATURE_MODS
from .pokemon import calc_hp, calc_stat
from .belief import OpponentBelief
from .ai import (HeuristicAI, _forced_charging_action, _filter_valid_by_lock,
                 _filter_by_pp, _get_struggle, should_mega_evolve,
                 _hazard_value, HAZARD_MOVES)


class _ForcedFirst:
    """ロールアウト初手だけ指定行動、以降は fallback に委譲。"""
    def __init__(self, action: Action, fallback):
        self.action = action
        self.fallback = fallback
        self.used = False

    def __call__(self, my_side, opp_side, field):
        if not self.used:
            self.used = True
            return self.action
        return self.fallback(my_side, opp_side, field)


class SearchAI:
    def __init__(self, loader: DataLoader, rollouts: int = 16, depth: int = 50,
                 season: str = "M-2", rollout_ai=None, seed: int = 0, value_fn=None,
                 roll_pessimism=None, policy_fn=None, policy_weight=0.15):
        self.loader = loader
        self.K = rollouts
        self.depth = depth
        self.season = season
        # ロールアウト相手は呼び出し側が指定（netを持つ箇所は NetGreedyAI(net) を渡す＝
        # 読みの相手も賢い前提＝AlphaZero的）。未指定時のみ HeuristicAI にフォールバック。
        self.rollout_ai = rollout_ai or HeuristicAI()
        self._fallback = HeuristicAI()
        self._rng = random.Random(seed)
        self._tpl_cache: dict = {}
        # 学習価値関数 value_fn(side1, side2, field)→P(side1勝利)。
        # 設定すると打ち切り葉を学習価値で評価し、短い深さで長期戦略を見積もる（AlphaZero的）。
        self.value_fn = value_fn
        # ロールアウト中の固定ダメージロール(0最低〜1最高)。高め=「不利な乱数を仮定」する
        # リスク回避探索（パラノイド）。技名ハードコードでない一般原理。Noneで通常乱数。
        self.roll_pessimism = roll_pessimism
        # 学習方策prior policy_fn(side1,side2,field)→{行動index: prior}。
        # スコアに policy_weight*prior を加算し、人間の手筋（模倣方策）へソフトに寄せる（PUCT的）。
        self.policy_fn = policy_fn
        self.policy_weight = policy_weight

    # ── 公開API（AIコールバック） ──────────────────────────────────
    def __call__(self, my_side: BattleSide, opp_side: BattleSide, field: BattleField) -> Action:
        me = my_side.active
        if not me.is_alive:
            return Action(type="pass")
        forced = _forced_charging_action(me)
        if forced:
            return forced

        cands = self._candidate_actions(my_side, opp_side, field)
        if len(cands) <= 1:
            return cands[0] if cands else self._fallback(my_side, opp_side, field)
        scored = self.score_actions(my_side, opp_side, field)
        return max(scored, key=lambda x: x[1])[0]

    def score_actions(self, my_side, opp_side, field):
        """各候補行動の推定勝率を返す [(Action, score), ...]（説明・可視化用）。"""
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self.loader, self.season)
        belief.observe_disclosure(my_side.opp_view)
        cands = self._candidate_actions(my_side, opp_side, field)
        if not cands:
            return []
        my_is_s1 = (my_side.field_idx == 0)
        configs = [self._sample_opp_config(opp_side, belief) for _ in range(self.K)]
        priors = {}
        if self.policy_fn is not None:
            try:
                priors = self.policy_fn(my_side, opp_side, field) or {}
            except Exception:
                priors = {}
        scored = []
        for act in cands:
            total = sum(self._evaluate(my_side, opp_side, field, act, cfg, my_is_s1)
                        for cfg in configs)
            score = total / len(configs)
            if priors:
                score += self.policy_weight * priors.get(self._action_index(act), 0.0)
            scored.append((act, score))
        return scored

    @staticmethod
    def _action_index(act) -> int:
        """legal_actions_indexed と整合: move=idx[+4でメガ] / switch=8+slot / struggle=11。"""
        if act.type == "switch":
            return 8 + act.switch_to
        if act.move_idx is not None and act.move_idx >= 0:
            return act.move_idx + (4 if getattr(act, "do_mega", False) else 0)
        return 11

    # ── 候補行動 ─────────────────────────────────────────────────
    def _candidate_actions(self, my_side, opp_side, field) -> List[Action]:
        me = my_side.active
        # メガ可能なら「メガする/しない」を独立した選択肢として探索（勝率で比較）
        can_mega = (me.mega_data is not None and not me.mega_evolved and not my_side.mega_used)
        mega_flags = [True, False] if can_mega else [False]
        valid = [(i, mv) for i, mv in enumerate(me.moves) if mv is not None]
        valid = _filter_valid_by_lock(valid, me)
        pp_valid = _filter_by_pp(valid, me)
        # 価値0の設置技（既に設置済み/相手残り1体）は無駄行動なので候補から除外
        move_cands = [(i, mv) for i, mv in pp_valid
                      if not (mv.category == "status" and mv.name_jp in HAZARD_MOVES
                              and _hazard_value(mv.name_jp, my_side, opp_side, field) <= 0)]
        if not move_cands:
            move_cands = pp_valid  # 全て除外されたら元に戻す（手が無くなるのを防ぐ）
        out: List[Action] = []
        if not pp_valid:
            for dm in mega_flags:
                out.append(Action(type="move", move=_get_struggle(), move_idx=-1, do_mega=dm))
        else:
            for i, mv in move_cands:
                for dm in mega_flags:
                    out.append(Action(type="move", move=mv, move_idx=i, do_mega=dm))
        if not is_trapped(me, opp_side.active):
            for i, p in enumerate(my_side.party):
                if i != my_side.active_idx and p.is_alive:
                    out.append(Action(type="switch", switch_to=i))
        return out

    # ── 相手構成のサンプリングと適用（決定化） ────────────────────
    def _tpl(self, name):
        if name not in self._tpl_cache:
            self._tpl_cache[name] = self.loader.get_pokemon_template(name, self.season)
        return self._tpl_cache[name]

    def _sample_opp_config(self, opp_side, belief) -> List[Optional[dict]]:
        cfg = []
        for p in opp_side.party:
            pb = belief.ensure(p.name)
            if pb is None:
                cfg.append(None)
                continue
            ev, nat = pb.sample_spread(self._rng)
            cfg.append({
                "ev": ev, "nature": nat,
                "item": pb.sample_item(self._rng),
                "ability": pb.sample_ability(self._rng),
                "moves": pb.sample_moves(self._rng),
            })
        return cfg

    def _determinize(self, poke, c: dict) -> None:
        tpl = self._tpl(poke.name)
        if tpl is None:
            return
        # メガ/へんしん中は観測される形態のステータスを保持（再サンプルしない）
        if not poke.mega_evolved and not getattr(poke, "_transformed", False):
            ev, nat = c["ev"], c["nature"]
            up, dn = NATURE_MODS.get(nat, (None, None))
            def nm(k):
                return 1.1 if up == k else (0.9 if dn == k else 1.0)
            frac = (poke.hp / poke.max_hp) if poke.max_hp else 1.0
            poke.max_hp = calc_hp(tpl.base_hp, ev.get("H", 0))
            poke.attack = calc_stat(tpl.base_attack, ev.get("A", 0), 31, nm("attack"))
            poke.defense = calc_stat(tpl.base_defense, ev.get("B", 0), 31, nm("defense"))
            poke.sp_attack = calc_stat(tpl.base_sp_attack, ev.get("C", 0), 31, nm("sp_attack"))
            poke.sp_defense = calc_stat(tpl.base_sp_defense, ev.get("D", 0), 31, nm("sp_defense"))
            poke.speed = calc_stat(tpl.base_speed, ev.get("S", 0), 31, nm("speed"))
            poke.nature, poke.evs = nat, ev
            poke.hp = max(1, round(frac * poke.max_hp)) if poke.is_alive else 0
        if c.get("item") is not None:
            poke.item = c["item"]
        if c.get("ability"):
            poke.ability = c["ability"]
        mvs = [self.loader.get_move(m) for m in c.get("moves", [])]
        mvs = [m for m in mvs if m is not None]
        if mvs:
            poke.moves = mvs
            poke.pp = [(m.pp or 5) for m in mvs]
            names = {m.name_jp for m in mvs}
            for attr in ("last_used_move", "choice_locked_move", "locked_move",
                         "disabled_move", "charging_move"):
                if getattr(poke, attr, None) is not None and getattr(poke, attr) not in names:
                    setattr(poke, attr, None)

    # ── ロールアウト評価 ──────────────────────────────────────────
    def _evaluate(self, my_side, opp_side, field, action, cfg, my_is_s1) -> float:
        s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
        cs1, cs2, cfield = copy.deepcopy((s1, s2, field))
        copp = cs2 if my_is_s1 else cs1
        for poke, c in zip(copp.party, cfg):
            if c is not None:
                self._determinize(poke, c)
        b = Battle(cs1, cs2, cfield)
        my_ai = _ForcedFirst(action, self.rollout_ai)
        if self.roll_pessimism is not None:
            from . import damage as _dmg
            _prev = _dmg._ROLL_OVERRIDE
            _dmg._ROLL_OVERRIDE = self.roll_pessimism
            try:
                if my_is_s1:
                    winner = b.resume(my_ai, self.rollout_ai, max_turns=self.depth)
                else:
                    winner = b.resume(self.rollout_ai, my_ai, max_turns=self.depth)
            finally:
                _dmg._ROLL_OVERRIDE = _prev
        elif my_is_s1:
            winner = b.resume(my_ai, self.rollout_ai, max_turns=self.depth)
        else:
            winner = b.resume(self.rollout_ai, my_ai, max_turns=self.depth)
        return self._score(b, winner, my_is_s1)

    def _score(self, b, winner, my_is_s1) -> float:
        if winner == 1:
            return 1.0 if my_is_s1 else 0.0
        if winner == 2:
            return 0.0 if my_is_s1 else 1.0
        # 打ち切り → 学習価値関数があればそれで葉を評価（長期的価値）
        if self.value_fn is not None:
            v1 = self.value_fn(b.side1, b.side2, b.field)  # P(side1勝利)
            return v1 if my_is_s1 else (1.0 - v1)
        # 価値関数が無ければ 残HP割合の差 ＋ 設置技の残存価値（ゲーム終了までのリターン）
        my_s = b.side1 if my_is_s1 else b.side2
        op_s = b.side2 if my_is_s1 else b.side1
        a = sum(p.hp for p in my_s.party) / max(1, sum(p.max_hp for p in my_s.party))
        d = sum(p.hp for p in op_s.party) / max(1, sum(p.max_hp for p in op_s.party))
        haz = self._hazard_credit(b.field, op_s) - self._hazard_credit(b.field, my_s)
        return max(0.0, min(1.0, 0.5 + 0.5 * (a - d) + haz))

    @staticmethod
    def _hazard_credit(field, side) -> float:
        """そのサイドに設置された設置技の残存価値（今後の交代で効く）。控えが居る時のみ。"""
        if sum(1 for p in side.party if p.is_alive) <= 1:
            return 0.0
        idx = side.field_idx
        v = 0.0
        if field.stealth_rock[idx]:
            v += 0.03
        v += 0.02 * field.spikes[idx]
        v += 0.02 * field.toxic_spikes[idx]
        return v


def make_nested_search(loader: DataLoader, season: str = "M-2",
                       outer=(12, 40), inner=(2, 8), seed: int = 0) -> "SearchAI":
    """再帰探索（2段ネスト）の SearchAI を構築する。

    外側 SearchAI のロールアウト方策に、予算を絞った内側 SearchAI を用いる
    （内側のロールアウトは HeuristicAI ＝ 再帰は2段で打ち止め）。ロールアウト中の
    両者がより賢く打つ前提で評価するため精度が上がりうるが、計算量は大幅増（opt-in）。
    outer/inner = (rollouts, depth)。
    """
    inner_ai = SearchAI(loader, rollouts=inner[0], depth=inner[1], season=season,
                        rollout_ai=HeuristicAI(), seed=seed + 1)
    return SearchAI(loader, rollouts=outer[0], depth=outer[1], season=season,
                    rollout_ai=inner_ai, seed=seed)
