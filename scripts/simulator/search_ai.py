"""行動方策（Phase 2: 決定化ロールアウト探索）。

毎ターン、開示情報＋belief（非開示情報の推定）から相手構成をK通りサンプリング（決定化）し、
各候補行動について短いロールアウトで勝率を見積もり、勝率最大（＝負ける確率最小）の行動を選ぶ。

- 相手の非開示情報（EV/性格・持ち物・特性・未開示技）は belief からサンプリングして具体化。
  観測可能な状態（現在HP割合・ランク変化・状態異常・場・メガ）はクローン元から保持する。
- 自分側は既知なのでそのまま。ロールアウトの行動は高速な rollout_ai（既定 HeuristicAI）。
- K個の決定化世界を全候補で共通利用（common random numbers）して候補間の分散を抑える。

探索の質に関する既知の保留ケース（d2の限界に起因する違和感のある手）は
`deferred_ai_cases.md` に記録。深化(d3)/相手モデル/価値ネット再学習の合否判定に使う。
"""
import copy
import math
import random
from typing import List, Optional

from .battle import Action, Battle, BattleSide, BattleField, is_trapped
from .data import DataLoader, NATURE_MODS, get_type_effectiveness
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
                 roll_pessimism=None, policy_fn=None, policy_weight=0.15,
                 adversarial: bool = False, opp_k: int = 6,
                 tree_search: bool = False, tree_depth: int = 1, tree_k: int = 3,
                 tree_det: int = None, tree_extend_k: int = 0):
        self.loader = loader
        self.K = rollouts
        self.depth = depth
        self.season = season
        # adversarial=True: 現手番を「同時手番ゼロ和ゲーム」として解く。
        #   自分の候補×相手の候補のペイオフ行列をロールアウトで作り、相手は最善応手(ナッシュ)を取る前提。
        #   ＝「相手は固定方策」を仮定する従来1手に対し、相手の択(読み合い)を評価に入れる。
        self.adversarial = adversarial
        self.opp_k = opp_k   # 相手候補手の上限（計算量抑制。priorで上位に絞る）
        # tree_search=True: 深さ限定 expectiminimax。各手番(自分手×相手手)を解決し、
        #   結果状態を価値ネットで直接採点（ロールアウトを排す）。priorで上位tree_kに枝刈り、
        #   各手番をゼロ和で解く(=maximin)。tree_depth=展開する手番(ターン)数。
        self.tree_search = tree_search
        self.tree_depth = tree_depth
        self.tree_k = tree_k
        self.se_bonus = 0.15               # 枝刈り順位での抜群技ボーナス(2倍=+0.15/4倍=+0.30)
        self.mega_tiebreak_eps = 0.05      # 同一技の素/メガが拮抗時にメガを採る閾値
        self.dominance_eps = 0.05          # 均衡値がこの差以内の手は最悪応手で優劣判定（リスク回避）
        self._last_worst = {}              # 直近の手ごと最悪応手値
        self.tree_det = tree_det if tree_det is not None else max(1, rollouts)   # 決定化数
        self.tree_roll = 0.85              # 解決時の固定ダメージロール(分散低減)
        # tree_extend_k>0: 選択的深化。tree_depthで全候補を評価後、上位tree_extend_k手だけを
        #   tree_depth+1 で精査（d3相当を高速化）。0で無効。
        self.tree_extend_k = tree_extend_k
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
        # mcts=True: 全幅expectiminimaxの代わりに IS-MCTS + Decoupled PUCT(DUCT) で探索。
        #   コストが固定幅 k^(2d-1) でなくシミュ本数 mcts_sims に線形化し、深さは有望ラインに沿って
        #   選択的に伸びる。葉は価値ネット、priorは方策ネット（＝本物のPUCT/AlphaZero）。
        #   同時手番は両者独立PUCT、確率(相手隠れ情報)はシミュ毎の決定化で平均(IS-MCTS)。
        self.mcts = False
        self.mcts_sims = 400
        self.c_puct = 1.5
        self.mcts_fpu = 0.5          # 未訪問手の初期Q(first-play urgency)
        self.mcts_p_floor = 1e-3     # prior未定義手の最小prior
        self.mcts_max_depth = 60     # 1シミュの最大実ターン降下数
        # 各ノードの手の選び方。"duct"=独立PUCT(純粋戦略に収束)、
        #   "regret"=regret-matching / "exp3"=Exp3（いずれも混合ナッシュ均衡に収束＝同時手番に正しい）。
        self.mcts_select = "duct"
        self.rm_prior_mix = 0.25     # regret-matching: 方策priorとの混合率(ネット知識のウォームスタート)
        self.exp3_eta = 0.05         # Exp3: 学習率
        self.exp3_gamma = 0.1        # Exp3: 一様探索率(最小確率 gamma/K を保証)
        # net_eval(s1,s2,f)->(policy_dict, value): encode_state+ネットforwardを1回で方策と価値の両方を返す統合関数。
        #   設定すると葉展開での value_fn/policy_fn の重複encode+forwardを排除（同一side順はメモ化）。
        #   未設定(None)なら従来どおり value_fn/policy_fn を個別に呼ぶ（既存挙動・デフォルト）。
        self.net_eval = None
        # fast_clone=True: MCTSの状態複製で belief を deepcopy しない（共有/分離）。
        #   beliefは根での相手構成サンプリングに使うのみでシミュ降下中は参照されないため安全（ビット一致）。
        self.fast_clone = False
        # mcts_cache=True: 各ノードに解決後の状態をキャッシュし、降下時の再解決・再cloneを排除（~2x）。
        #   1手内では相手構成を固定（IS-MCTSの逐次再決定化を廃す）代わりに mcts_ensemble 個の
        #   決定化ツリーで平均化して隠れ情報のロバスト性を保つ。挙動が変わるので強さは要A/B検証。
        self.mcts_cache = False
        self.mcts_ensemble = 16

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
        if self.mcts:
            return self._mcts_choose(my_side, opp_side, field, cands)
        if self.tree_search:
            scored = self.score_actions_tree(my_side, opp_side, field)
        elif self.adversarial:
            scored = self.score_actions_adversarial(my_side, opp_side, field)
        else:
            scored = self.score_actions(my_side, opp_side, field)
        best_a, best_v = max(scored, key=lambda x: x[1])
        # ②ドミナンス除去（リスク回避）：均衡値が最良からEPS内の手の中で、最悪応手値が最大の手を選ぶ。
        # ＝同等の上振れなら下振れの小さい手を採る。上振れが明確に大きい手（正当な読み）は残る
        # （EPSを超える差は対象外）。worst が無い手は均衡値で代替。
        worst = getattr(self, "_last_worst", None) or {}
        if self.tree_search and worst:
            near = [(a, v) for a, v in scored if v >= best_v - self.dominance_eps]
            if len(near) > 1:
                best_a, best_v = max(near, key=lambda av: worst.get(self._action_index(av[0]), av[1]))
        # メガ優越のタイブレーク：最良が「素の技」で同一技の「メガ版」が拮抗(EPS内)ならメガ版を採る。
        if (best_a.type == "move" and best_a.move_idx is not None and best_a.move_idx >= 0
                and not getattr(best_a, "do_mega", False)):
            for a, v in scored:
                if (a.type == "move" and a.move_idx == best_a.move_idx
                        and getattr(a, "do_mega", False) and v >= best_v - self.mega_tiebreak_eps):
                    return a
        return best_a

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

    def score_actions_adversarial(self, my_side, opp_side, field):
        """現手番を同時手番ゼロ和ゲームとして解く。各自分手の「相手最善応手に対する価値」を返す。

        各決定化(相手構成サンプル)ごとに:
          ペイオフ行列 M[i][j] = 自分手i・相手手j を同時に打って depth ターン進めた評価
          → solve_zero_sum で相手の混合最善戦略 y を解き、各自分手の vs-y 価値を accumulate。
        K個の決定化で平均して返す（隠れ情報の不確実性を平均）。
        """
        from .selection import solve_zero_sum
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self.loader, self.season)
        belief.observe_disclosure(my_side.opp_view)
        my_cands = self._candidate_actions(my_side, opp_side, field)
        if len(my_cands) <= 1:
            return [(my_cands[0], 1.0)] if my_cands else []
        my_is_s1 = (my_side.field_idx == 0)
        priors = {}
        if self.policy_fn is not None:
            try:
                priors = self.policy_fn(my_side, opp_side, field) or {}
            except Exception:
                priors = {}
        agg = [0.0] * len(my_cands); nconf = 0
        for _ in range(self.K):
            cfg = self._sample_opp_config(opp_side, belief)
            s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
            bs1, bs2, bfield = copy.deepcopy((s1, s2, field))
            dopp = bs2 if my_is_s1 else bs1; dme = bs1 if my_is_s1 else bs2
            for poke, c in zip(dopp.party, cfg):
                if c is not None:
                    self._determinize(poke, c)
            opp_cands = self._candidate_actions(dopp, dme, bfield)
            if not opp_cands:
                continue
            opp_cands = self._limit_opp(opp_cands, dopp, dme, bfield)
            M = [[self._eval_joint(bs1, bs2, bfield, my_cands[i], opp_cands[j], my_is_s1)
                  for j in range(len(opp_cands))] for i in range(len(my_cands))]
            _x, y, _v = solve_zero_sum(M, iters=1500)
            for i in range(len(my_cands)):
                agg[i] += sum(M[i][j] * y[j] for j in range(len(opp_cands)))
            nconf += 1
        if nconf == 0:
            return self.score_actions(my_side, opp_side, field)
        out = []
        for i, act in enumerate(my_cands):
            sc = agg[i] / nconf
            if priors:
                sc += self.policy_weight * priors.get(self._action_index(act), 0.0)
            out.append((act, sc))
        return out

    def _limit_opp(self, opp_cands, dopp, dme, field):
        """相手候補手を opp_k 件に制限（計算量抑制）。policy_fn があれば上位、無ければ先頭。"""
        if len(opp_cands) <= self.opp_k:
            return opp_cands
        if self.policy_fn is not None:
            try:
                pr = self.policy_fn(dopp, dme, field) or {}
                opp_cands = sorted(opp_cands, key=lambda a: -pr.get(self._action_index(a), 0.0))
            except Exception:
                pass
        return opp_cands[:self.opp_k]

    def _eval_joint(self, bs1, bs2, bfield, my_act, opp_act, my_is_s1):
        """自分手・相手手を同時に強制し depth ターン進めて評価（決定化済み状態から）。"""
        cs1, cs2, cfield = copy.deepcopy((bs1, bs2, bfield))
        if my_is_s1:
            a1 = _ForcedFirst(my_act, self.rollout_ai); a2 = _ForcedFirst(opp_act, self.rollout_ai)
        else:
            a1 = _ForcedFirst(opp_act, self.rollout_ai); a2 = _ForcedFirst(my_act, self.rollout_ai)
        b = Battle(cs1, cs2, cfield)
        winner = b.resume(a1, a2, max_turns=self.depth)
        return self._score(b, winner, my_is_s1)

    # ── 深さ限定 expectiminimax（葉＝価値ネット直接採点） ──────────────
    def score_actions_tree(self, my_side, opp_side, field):
        """各自分手の「相手最善応手に対する、深さtree_depthの木の価値」を返す。

        tree_extend_k>0 なら選択的深化：まず tree_depth で全候補を評価し、上位 tree_extend_k 手だけを
        tree_depth+1 で精査（深い読みが要る“最善手の見極め”だけ深くする＝d3相当を高速化）。
        """
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self.loader, self.season)
        belief.observe_disclosure(my_side.opp_view)
        my_cands = self._candidate_actions(my_side, opp_side, field)
        if len(my_cands) <= 1:
            return [(my_cands[0], 1.0)] if my_cands else []
        res = self._tree_scores_pass(my_side, opp_side, field, belief, None, self.tree_depth)
        if res is None:
            self._last_worst = {}
            return self.score_actions(my_side, opp_side, field)
        scores, worst = res
        self._last_worst = worst   # 手ごとの最悪応手値（②ドミナンス除去で参照）
        if self.tree_extend_k and len(my_cands) > self.tree_extend_k:
            top = sorted(my_cands, key=lambda a: -scores.get(self._action_index(a), -1.0))[:self.tree_extend_k]
            restrict = {self._action_index(a) for a in top}
            deep = self._tree_scores_pass(my_side, opp_side, field, belief, restrict, self.tree_depth + 1)
            if deep:   # 深化した上位手のみを候補に（浅い手より弱いことが確定済み）
                dscores, dworst = deep
                self._last_worst = dworst
                return [(a, dscores[self._action_index(a)]) for a in top if self._action_index(a) in dscores]
        return [(a, scores[self._action_index(a)]) for a in my_cands if self._action_index(a) in scores]

    def _tree_scores_pass(self, my_side, opp_side, field, belief, restrict, depth):
        """tree_det 個の決定化で木を解き、{行動index: 平均価値} を返す。
        restrict=None で自分の全候補、集合指定でその行動indexのみを行（自分手）に使う。"""
        from .selection import solve_zero_sum
        my_is_s1 = (my_side.field_idx == 0)
        agg = {}; wst = {}; cnt = 0
        for _ in range(self.tree_det):
            cfg = self._sample_opp_config(opp_side, belief)
            s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
            bs1, bs2, bfield = copy.deepcopy((s1, s2, field))
            dopp = bs2 if my_is_s1 else bs1; dme = bs1 if my_is_s1 else bs2
            for poke, c in zip(dopp.party, cfg):
                if c is not None:
                    self._determinize(poke, c)
            opp_cands = self._topk_actions(dopp, dme, bfield, self.tree_k)
            all_mine = self._candidate_actions(dme, dopp, bfield)
            mine = [a for a in all_mine if self._action_index(a) in restrict] if restrict is not None else all_mine
            if not opp_cands or not mine:
                continue
            M = [[self._tree_value(bs1, bs2, bfield, a_my, a_op, my_is_s1, depth - 1)
                  for a_op in opp_cands] for a_my in mine]
            _x, y, _v = solve_zero_sum(M, iters=1500)
            y = self._opp_blend(y, opp_cands, dopp, dme, bfield)
            for i, a in enumerate(mine):
                ix = self._action_index(a)
                agg[ix] = agg.get(ix, 0.0) + sum(M[i][j] * y[j] for j in range(len(opp_cands)))
                wst[ix] = wst.get(ix, 0.0) + (min(M[i]) if M[i] else 0.0)   # この手の最悪応手値
            cnt += 1
        if cnt == 0:
            return None
        return ({ix: v / cnt for ix, v in agg.items()},
                {ix: w / cnt for ix, w in wst.items()})

    def _opp_blend(self, y, opp_cands, side, opp, field):
        """相手の混合戦略 y（maximin均衡）を、相手の方策prior（≒人間的に自然な手）とブレンド。
        opp_mix=1.0 で純maximin（従来）、<1.0 で「低確率の相手交代の過大評価」を是正。
        y_blend = b*y + (1-b)*prior。"""
        b = getattr(self, "opp_mix", 1.0)
        if b >= 1.0 or self.policy_fn is None or not opp_cands:
            return y
        try:
            pr = self.policy_fn(side, opp, field) or {}
        except Exception:
            return y
        p = [max(0.0, pr.get(self._action_index(a), 0.0)) for a in opp_cands]
        s = sum(p)
        if s <= 0:
            return y
        p = [pi / s for pi in p]
        return [b * y[j] + (1.0 - b) * p[j] for j in range(len(opp_cands))]

    def _topk_actions(self, side, opp, field, k):
        """side の候補手を上位 k 件に枝刈り。
        ベースは方策prior（≒採用率）。さらに相手対面に抜群を取れる攻撃技は加点して順位を上げ、
        サブウェポン（アイススピナー等）の見落としを防ぐ。低採用率の技まで過剰には警戒しない
        （加点は抜群技のみ・採用率の重みはbeliefサンプリングと方策priorが担保）。"""
        cands = self._candidate_actions(side, opp, field)
        if len(cands) <= k:
            return cands
        pr = {}
        if self.policy_fn is not None:
            try:
                pr = self.policy_fn(side, opp, field) or {}
            except Exception:
                pr = {}
        tgt = opp.active
        tgt_alive = tgt is not None and getattr(tgt, "is_alive", False)

        def _score(a):
            s = pr.get(self._action_index(a), 0.0)
            mv = getattr(a, "move", None)
            if tgt_alive and mv and mv.power and mv.category != "status":
                eff = get_type_effectiveness(mv.type, tgt.type1, tgt.type2)
                if eff >= 4.0:
                    s += self.se_bonus * 2
                elif eff >= 2.0:
                    s += self.se_bonus
            return s
        return sorted(cands, key=lambda a: -_score(a))[:k]

    def _tree_value(self, bs1, bs2, bfield, my_act, opp_act, my_is_s1, depth):
        """自分手・相手手を1ターン解決し、子状態を深さdepthで再帰評価（葉＝価値ネット）。"""
        from .selection import solve_zero_sum
        from . import damage as _dmg
        cs1, cs2, cfield = copy.deepcopy((bs1, bs2, bfield))
        if my_is_s1:
            a1 = _ForcedFirst(my_act, self.rollout_ai); a2 = _ForcedFirst(opp_act, self.rollout_ai)
        else:
            a1 = _ForcedFirst(opp_act, self.rollout_ai); a2 = _ForcedFirst(my_act, self.rollout_ai)
        b = Battle(cs1, cs2, cfield)
        _prev = _dmg._ROLL_OVERRIDE; _dmg._ROLL_OVERRIDE = self.tree_roll
        try:
            winner = b.resume(a1, a2, max_turns=1)   # 1ターンだけ解決
        finally:
            _dmg._ROLL_OVERRIDE = _prev
        if winner != 0:
            return self._score(b, winner, my_is_s1)
        if depth <= 0:
            return self._leaf_value(b, my_is_s1)
        # さらに1ターン展開（同時手番ゼロ和）
        me_sub = b.side1 if my_is_s1 else b.side2
        op_sub = b.side2 if my_is_s1 else b.side1
        my_next = self._topk_actions(me_sub, op_sub, b.field, self.tree_k)
        op_next = self._topk_actions(op_sub, me_sub, b.field, self.tree_k)
        if not my_next or not op_next:
            return self._leaf_value(b, my_is_s1)
        M = [[self._tree_value(b.side1, b.side2, b.field, am, ao, my_is_s1, depth - 1)
              for ao in op_next] for am in my_next]
        _x, yv, val = solve_zero_sum(M, iters=1000)
        yb = self._opp_blend(yv, op_next, op_sub, me_sub, b.field)
        if yb is not yv:   # ブレンド時は「ブレンド相手への最善応手」を局面価値とする
            val = max(sum(M[i][j] * yb[j] for j in range(len(op_next))) for i in range(len(my_next)))
        return val

    # ── IS-MCTS + Decoupled PUCT（深さの指数爆発を回避する選択的探索） ──────
    def _mcts_choose(self, my_side, opp_side, field, cands) -> Action:
        """mcts_sims 回のシミュレーションで根の手を選ぶ。最多訪問手を採用（AlphaZero流）。"""
        scored = self.score_actions_mcts(my_side, opp_side, field, cands)
        self._last_worst = {}
        best_a, best_v = max(scored, key=lambda x: x[1])   # x[1]=訪問数（同点はQでタイブレーク済）
        # メガ優越タイブレーク：最良が素技で同一技のメガ版が拮抗(訪問近い)ならメガ版
        if (best_a.type == "move" and best_a.move_idx is not None and best_a.move_idx >= 0
                and not getattr(best_a, "do_mega", False)):
            for a, v in scored:
                if (a.type == "move" and a.move_idx == best_a.move_idx
                        and getattr(a, "do_mega", False) and v >= best_v * 0.9):
                    return a
        return best_a

    def _clone_state(self, s1, s2, field):
        """MCTSシミュ用の独立コピー。fast_clone時は belief を deepcopy せず分離（シミュ中不使用）。"""
        if not self.fast_clone:
            return copy.deepcopy((s1, s2, field))
        b1, b2 = getattr(s1, "belief", None), getattr(s2, "belief", None)
        s1.belief = None; s2.belief = None
        try:
            cs1, cs2, cf = copy.deepcopy((s1, s2, field))
        finally:
            s1.belief = b1; s2.belief = b2
        return cs1, cs2, cf

    def _build_mcts_root(self, my_side, opp_side, field, cands):
        """mcts_sims回シミュして根ノードを構築し (root, root_my, my_is_s1) を返す。"""
        if self.mcts_cache:
            return self._build_mcts_root_cached(my_side, opp_side, field, cands)
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self.loader, self.season)
        belief.observe_disclosure(my_side.opp_view)
        my_is_s1 = (my_side.field_idx == 0)
        root_my = cands if cands is not None else self._candidate_actions(my_side, opp_side, field)
        root = self._new_node()
        if len(root_my) <= 1:
            return root, root_my, my_is_s1
        for t in range(self.mcts_sims):
            s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
            cs1, cs2, cfield = self._clone_state(s1, s2, field)
            cfg = self._sample_opp_config(opp_side, belief)
            dopp = cs2 if my_is_s1 else cs1
            for poke, c in zip(dopp.party, cfg):
                if c is not None:
                    self._determinize(poke, c)
            self._mcts_simulate(root, cs1, cs2, cfield, my_is_s1)
        return root, root_my, my_is_s1

    def _build_mcts_root_cached(self, my_side, opp_side, field, cands):
        """状態キャッシュ版：mcts_ensemble個の決定化ツリー(各 sims/E)で探索し、根の訪問を集約。
        各ツリーはノードに解決後状態を持ち、降下時の再解決・再cloneを排除する。
        戻り値は擬似root {"N":[集約,{}], "W":[集約,{}]}（下流は root["N"][0]/["W"][0] を読む）。"""
        belief = my_side.belief if my_side.belief is not None else OpponentBelief(self.loader, self.season)
        belief.observe_disclosure(my_side.opp_view)
        my_is_s1 = (my_side.field_idx == 0)
        root_my = cands if cands is not None else self._candidate_actions(my_side, opp_side, field)
        aggN = {}; aggW = {}
        if len(root_my) <= 1:
            return {"N": [aggN, {}], "W": [aggW, {}]}, root_my, my_is_s1
        E = max(1, self.mcts_ensemble)
        per = max(1, self.mcts_sims // E)
        for _e in range(E):
            s1, s2 = (my_side, opp_side) if my_is_s1 else (opp_side, my_side)
            cs1, cs2, cfield = self._clone_state(s1, s2, field)
            cfg = self._sample_opp_config(opp_side, belief)
            dopp = cs2 if my_is_s1 else cs1
            for poke, c in zip(dopp.party, cfg):
                if c is not None:
                    self._determinize(poke, c)
            root = self._new_node(); root["state"] = (cs1, cs2, cfield)
            self._expand_state_node(root, my_is_s1)
            for _t in range(per):
                self._mcts_simulate_cached(root, my_is_s1)
            for ix, n in root["N"][0].items():
                aggN[ix] = aggN.get(ix, 0) + n
                aggW[ix] = aggW.get(ix, 0.0) + root["W"][0].get(ix, 0.0)
        return {"N": [aggN, {}], "W": [aggW, {}]}, root_my, my_is_s1

    def _expand_state_node(self, node, my_is_s1):
        """node["state"] から両者priorを設定し、葉価値(自分視点)を返す。net_eval優先。"""
        cs1, cs2, cfield = node["state"]
        if self.net_eval is not None:
            return self._expand_with_value(node, cs1, cs2, cfield, my_is_s1)
        self._expand_node(node, cs1, cs2, cfield, my_is_s1)
        return self._mcts_leaf_value(cs1, cs2, cfield, my_is_s1)

    def _leaf_value_state(self, node, my_is_s1):
        cs1, cs2, cfield = node["state"]
        return self._mcts_leaf_value(cs1, cs2, cfield, my_is_s1)

    def _mcts_simulate_cached(self, root, my_is_s1):
        """状態キャッシュ降下：子は状態を保持。新規葉のみ1ターン解決(親状態をclone)。"""
        node = root; path = []; v = None; depth = 0
        while True:
            cs1, cs2, cfield = node["state"]
            me_s = cs1 if my_is_s1 else cs2
            op_s = cs2 if my_is_s1 else cs1
            my_cands = self._candidate_actions(me_s, op_s, cfield)
            opp_cands = self._candidate_actions(op_s, me_s, cfield)
            if not my_cands or not opp_cands:
                v = self._leaf_value_state(node, my_is_s1); break
            idx_me, a_me, sg_me = self._select(node, 0, my_cands)
            idx_op, a_op, sg_op = self._select(node, 1, opp_cands)
            path.append((node, idx_me, idx_op, sg_me, sg_op))
            key = (idx_me, idx_op)
            child = node["children"].get(key)
            if child is None:
                ccs1, ccs2, ccfield = self._clone_state(cs1, cs2, cfield)
                winner = self._advance_turn(ccs1, ccs2, ccfield, a_me, a_op, my_is_s1)
                child = self._new_node(); child["state"] = (ccs1, ccs2, ccfield)
                node["children"][key] = child
                if winner != 0:
                    child["terminal"] = True
                    child["v_me"] = 1.0 if ((winner == 1) == my_is_s1) else 0.0
                    v = child["v_me"]
                else:
                    v = self._expand_state_node(child, my_is_s1)
                break
            if child.get("terminal"):
                v = child["v_me"]; break
            node = child; depth += 1
            if depth >= self.mcts_max_depth:
                v = self._leaf_value_state(node, my_is_s1); break
        exp3 = (self.mcts_select == "exp3")
        for (nd, im, io, sm, so) in path:
            nd["total"] += 1
            nd["N"][0][im] = nd["N"][0].get(im, 0) + 1
            nd["W"][0][im] = nd["W"][0].get(im, 0.0) + v
            nd["N"][1][io] = nd["N"][1].get(io, 0) + 1
            nd["W"][1][io] = nd["W"][1].get(io, 0.0) + (1.0 - v)
            if exp3:
                nd["S"][0][im] = nd["S"][0].get(im, 0.0) + v / max(sm, 1e-9)
                nd["S"][1][io] = nd["S"][1].get(io, 0.0) + (1.0 - v) / max(so, 1e-9)

    def score_actions_mcts(self, my_side, opp_side, field, cands=None):
        """根の各自分手の (Action, 訪問数+Q) を返す。可視化/選択共用。"""
        root, root_my, _ = self._build_mcts_root(my_side, opp_side, field, cands)
        if len(root_my) <= 1:
            return [(root_my[0], 1.0)] if root_my else []
        meN = root["N"][0]; meW = root["W"][0]
        out = []
        for a in root_my:
            ix = self._action_index(a)
            n = meN.get(ix, 0)
            q = (meW.get(ix, 0.0) / n) if n else 0.0
            out.append((a, n + q))   # 訪問数が主、Qで微小タイブレーク
        return out

    def mcts_policy(self, my_side, opp_side, field, temperature=1.0):
        """学習用：根の訪問分布πを {action_index: 確率} で返す。戻り (best_action, pi)。
        新MCTS(同時手番DUCT/regret)を教師信号に使うためのフック。"""
        cands = self._candidate_actions(my_side, opp_side, field)
        if not cands:
            return None, {}
        if len(cands) == 1:
            return cands[0], {self._action_index(cands[0]): 1.0}
        root, root_my, _ = self._build_mcts_root(my_side, opp_side, field, cands)
        meN = root["N"][0]
        counts = [(self._action_index(a), meN.get(self._action_index(a), 0)) for a in root_my]
        tot = sum(n for _, n in counts)
        if tot <= 0:
            return root_my[0], {ix: 1.0 / len(counts) for ix, _ in counts}
        if temperature and temperature > 0 and temperature != 1.0:
            w = [(ix, (n / tot) ** (1.0 / temperature)) for ix, n in counts]
            z = sum(x for _, x in w) or 1.0
            pi = {ix: x / z for ix, x in w}
        else:
            pi = {ix: n / tot for ix, n in counts}
        best = max(root_my, key=lambda a: meN.get(self._action_index(a), 0))
        return best, pi

    @staticmethod
    def _new_node():
        # R=累積後悔(regret-matching用), S=累積推定報酬(Exp3用)。side毎に[me,opp]。
        return {"N": [{}, {}], "W": [{}, {}], "P": [{}, {}],
                "R": [{}, {}], "S": [{}, {}],
                "children": {}, "total": 0, "expanded": False}

    def _policy_dict(self, side, opp, field):
        if self.policy_fn is None:
            return {}
        try:
            return self.policy_fn(side, opp, field) or {}
        except Exception:
            return {}

    def _expand_node(self, node, cs1, cs2, cfield, my_is_s1):
        me_s = cs1 if my_is_s1 else cs2
        op_s = cs2 if my_is_s1 else cs1
        node["P"][0] = self._policy_dict(me_s, op_s, cfield)
        node["P"][1] = self._policy_dict(op_s, me_s, cfield)
        node["expanded"] = True

    def _select(self, node, side, cands):
        """side(0=自分,1=相手)の手を選び (idx, action, 選択確率) を返す。
        mcts_select で選択則を切替: duct=独立PUCT / regret=regret-matching / exp3=Exp3。"""
        mode = self.mcts_select
        if mode == "duct":
            ix, a = self._duct_select(node, side, cands)
            return ix, a, 1.0
        P = node["P"][side]; N = node["N"][side]; W = node["W"][side]
        # 各候補の (idx, action, Q, prior)
        items = []
        for a in cands:
            ix = self._action_index(a)
            n = N.get(ix, 0)
            q = (W.get(ix, 0.0) / n) if n else self.mcts_fpu
            p = max(P.get(ix, self.mcts_p_floor), self.mcts_p_floor)
            items.append((ix, a, q, p))
        psum = sum(p for _, _, _, p in items) or 1.0
        if mode == "regret":
            R = node["R"][side]
            pos = {ix: max(0.0, R.get(ix, 0.0)) for ix, _, _, _ in items}
            Z = sum(pos.values())
            if Z > 0:
                sig = {ix: pos[ix] / Z for ix, _, _, _ in items}
            else:
                sig = {ix: 1.0 / len(items) for ix, _, _, _ in items}
            lam = self.rm_prior_mix
            sig = {ix: (1 - lam) * sig[ix] + lam * (p / psum) for ix, _, _, p in items}
            V = sum(sig[ix] * q for ix, _, q, _ in items)   # 現戦略の期待値
            for ix, _, q, _ in items:                        # 後悔を累積: r(a)=Q(a)-V
                R[ix] = R.get(ix, 0.0) + (q - V)
        else:  # exp3
            S = node["S"][side]; eta = self.exp3_eta
            logits = {}
            for ix, _, _, p in items:
                if ix not in S:                              # priorでウォームスタート(eta*S=log p)
                    S[ix] = (1.0 / eta) * math.log(max(p / psum, self.mcts_p_floor))
                logits[ix] = eta * S[ix]
            m = max(logits.values())
            ex = {ix: math.exp(logits[ix] - m) for ix in logits}
            Z = sum(ex.values()); g = self.exp3_gamma; K = len(items)
            sig = {ix: (1 - g) * ex[ix] / Z + g / K for ix in ex}
        ix, a = self._sample(items, sig)
        return ix, a, sig[ix]

    def _sample(self, items, sig):
        r = self._rng.random(); acc = 0.0
        for ix, a, _, _ in items:
            acc += sig[ix]
            if r <= acc:
                return ix, a
        ix, a, _, _ = items[-1]
        return ix, a

    def _duct_select(self, node, side, cands):
        """side(0=自分,1=相手)の手を独立PUCTで選ぶ。Q + c_puct*P*sqrt(ΣN)/(1+N)。"""
        P = node["P"][side]; N = node["N"][side]; W = node["W"][side]
        sq = math.sqrt(max(1, node["total"]))
        best = None; bix = None; bs = -1e18
        for a in cands:
            ix = self._action_index(a)
            n = N.get(ix, 0)
            q = (W.get(ix, 0.0) / n) if n else self.mcts_fpu
            p = P.get(ix, self.mcts_p_floor)
            s = q + self.c_puct * p * sq / (1 + n)
            if s > bs:
                bs = s; best = a; bix = ix
        return bix, best

    def _mcts_leaf_value(self, cs1, cs2, cfield, my_is_s1):
        if self.net_eval is not None:
            _, v1 = self.net_eval(cs1, cs2, cfield)
            return v1 if my_is_s1 else (1.0 - v1)
        if self.value_fn is not None:
            v1 = self.value_fn(cs1, cs2, cfield)
            return v1 if my_is_s1 else (1.0 - v1)
        a = sum(p.hp for p in cs1.party) / max(1, sum(p.max_hp for p in cs1.party))
        d = sum(p.hp for p in cs2.party) / max(1, sum(p.max_hp for p in cs2.party))
        v1 = max(0.0, min(1.0, 0.5 + 0.5 * (a - d)))
        return v1 if my_is_s1 else (1.0 - v1)

    def _advance_turn(self, cs1, cs2, cfield, a_me, a_op, my_is_s1):
        """決定化済み状態を1ターン分その場で進める（固定ロール）。戻り: winner(0=継続)。"""
        from . import damage as _dmg
        if my_is_s1:
            a1 = _ForcedFirst(a_me, self.rollout_ai); a2 = _ForcedFirst(a_op, self.rollout_ai)
        else:
            a1 = _ForcedFirst(a_op, self.rollout_ai); a2 = _ForcedFirst(a_me, self.rollout_ai)
        b = Battle(cs1, cs2, cfield)
        _prev = _dmg._ROLL_OVERRIDE; _dmg._ROLL_OVERRIDE = self.tree_roll
        try:
            return b.resume(a1, a2, max_turns=1)
        finally:
            _dmg._ROLL_OVERRIDE = _prev

    def _expand_with_value(self, node, cs1, cs2, cfield, my_is_s1):
        """net_eval使用時: 1状態のencode+ネットforwardをメモ化し、両者prior設定＋葉価値を返す。
        value_fn/policy_fnを個別に呼ぶ従来路の重複encode（3回→2回）を排除。結果はビット一致。"""
        memo = {}
        def ev(A, B):
            k = (id(A), id(B))
            r = memo.get(k)
            if r is None:
                r = self.net_eval(A, B, cfield)   # (policy_dict, value=P(A勝))
                memo[k] = r
            return r
        me_s = cs1 if my_is_s1 else cs2
        op_s = cs2 if my_is_s1 else cs1
        pol_me, _ = ev(me_s, op_s)
        pol_op, _ = ev(op_s, me_s)
        node["P"][0] = pol_me or {}
        node["P"][1] = pol_op or {}
        node["expanded"] = True
        _, v1 = ev(cs1, cs2)   # side1視点の価値（どちらの視点でも上の2呼びのいずれかとメモ共有）
        return v1 if my_is_s1 else (1.0 - v1)

    def _mcts_simulate(self, root, cs1, cs2, cfield, my_is_s1):
        if not root["expanded"]:
            if self.net_eval is not None:
                self._expand_with_value(root, cs1, cs2, cfield, my_is_s1)
            else:
                self._expand_node(root, cs1, cs2, cfield, my_is_s1)
        node = root
        path = []   # [(node, idx_me, idx_op)]
        depth = 0
        v = None
        while True:
            me_s = cs1 if my_is_s1 else cs2
            op_s = cs2 if my_is_s1 else cs1
            my_cands = self._candidate_actions(me_s, op_s, cfield)
            opp_cands = self._candidate_actions(op_s, me_s, cfield)
            if not my_cands or not opp_cands:
                v = self._mcts_leaf_value(cs1, cs2, cfield, my_is_s1); break
            idx_me, a_me, sg_me = self._select(node, 0, my_cands)
            idx_op, a_op, sg_op = self._select(node, 1, opp_cands)
            path.append((node, idx_me, idx_op, sg_me, sg_op))
            winner = self._advance_turn(cs1, cs2, cfield, a_me, a_op, my_is_s1)
            depth += 1
            if winner != 0:
                v = 1.0 if ((winner == 1) == my_is_s1) else 0.0
                break
            key = (idx_me, idx_op)
            child = node["children"].get(key)
            if child is None:
                child = self._new_node()
                node["children"][key] = child
                if self.net_eval is not None:
                    v = self._expand_with_value(child, cs1, cs2, cfield, my_is_s1)
                else:
                    self._expand_node(child, cs1, cs2, cfield, my_is_s1)
                    v = self._mcts_leaf_value(cs1, cs2, cfield, my_is_s1)
                break
            node = child
            if depth >= self.mcts_max_depth:
                v = self._mcts_leaf_value(cs1, cs2, cfield, my_is_s1); break
        exp3 = (self.mcts_select == "exp3")
        for (nd, im, io, sm, so) in path:
            nd["total"] += 1
            nd["N"][0][im] = nd["N"][0].get(im, 0) + 1
            nd["W"][0][im] = nd["W"][0].get(im, 0.0) + v
            nd["N"][1][io] = nd["N"][1].get(io, 0) + 1
            nd["W"][1][io] = nd["W"][1].get(io, 0.0) + (1.0 - v)
            if exp3:   # 重要度重み付き推定報酬を累積: S(a)+=報酬/選択確率
                nd["S"][0][im] = nd["S"][0].get(im, 0.0) + v / max(sm, 1e-9)
                nd["S"][1][io] = nd["S"][1].get(io, 0.0) + (1.0 - v) / max(so, 1e-9)

    def _leaf_value(self, b, my_is_s1):
        """葉の状態を価値ネットで採点（無ければHP割合）。my視点のP(勝利)。"""
        if self.value_fn is not None:
            v1 = self.value_fn(b.side1, b.side2, b.field)
            return v1 if my_is_s1 else (1.0 - v1)
        return self._score(b, 0, my_is_s1)

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
        # collapse_mega=True: メガ石持ちは常にメガ前提（メガ無し重複を列挙しない＝分岐半減）
        can_mega = (me.mega_data is not None and not me.mega_evolved and not my_side.mega_used)
        mega_flags = (([True] if getattr(self, "collapse_mega", False) else [True, False])
                      if can_mega else [False])
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
