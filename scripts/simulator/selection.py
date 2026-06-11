"""選出方策（Phase 3: ゼロサム行列ゲームのナッシュ均衡）。

相手パーティ（見せ合いの6体）に対し、自分の6体からどの3体を選び、どれを先頭にするかを学習する。
両者の選出選択は同時手番のゼロサムゲーム。選出空間（C(6,3)×先頭=60通り）はヒューリスティックで
有望な top-k に絞り、利得行列 W[i][j]=P(自分が勝つ) をモンテカルロ推定して fictitious play で
混合戦略ナッシュ均衡を解く（外部依存なし）。
"""
import copy
import random
from itertools import combinations
from typing import List, Tuple

from .battle import Battle, BattleSide, BattleField
from .ai import HeuristicAI, expected_damage, HAZARD_MOVES, _AVG_HP
from .data import get_type_effectiveness
from .env import RegisteredParty, build_party
from .belief import OpponentBelief

Selection = Tuple[int, int, int]  # (先頭, 2番手, 3番手) の party インデックス


def _scoring_form(p):
    """メガ石持ちはメガ後のステータス/タイプで評価する（選出価値の過小評価を防ぐ）。"""
    if getattr(p, "mega_data", None) is not None and not p.mega_evolved:
        m = copy.deepcopy(p)
        try:
            m.do_mega_evolve()
            return m
        except Exception:
            return p
    return p


_WEATHER_ABILITY = {"あめふらし": "rain", "すなおこし": "sand", "ひでり": "sun", "ゆきふらし": "snow"}
_WEATHER_MOVE = {"あまごい": "rain", "すなあらし": "sand", "にほんばれ": "sun", "あられ": "snow", "ゆきげしき": "snow"}
_SETUP = {"つるぎのまい", "りゅうのまい", "ちょうのまい", "めいそう", "わるだくみ", "からをやぶる",
          "てっぺき", "ビルドアップ", "ロックカット", "こうそくいどう", "せいちょう", "とぐろをまく", "はらだいこ"}


def _moves_of(p):
    return {m.name_jp for m in p.moves if m}


def _sets_weather(p):
    if p.ability in _WEATHER_ABILITY:
        return _WEATHER_ABILITY[p.ability]
    for m in _moves_of(p) & set(_WEATHER_MOVE):
        return _WEATHER_MOVE[m]
    return None


def _abuses_weather(p, w):
    t = (p.type1, p.type2)
    mv = _moves_of(p)
    if w == "rain":
        return ("みず" in t or p.ability in ("すいすい", "かんそうはだ", "あめうけざら")
                or "エレクトロビーム" in mv or any(m and m.type == "みず" and m.power for m in p.moves))
    if w == "sun":
        return ("ほのお" in t or p.ability in ("ようりょくそ", "サンパワー")
                or any(m and m.type == "ほのお" and m.power for m in p.moves))
    if w == "sand":
        return p.ability in ("すなかき", "すながくれ", "すなのちから") or "いわ" in t
    if w == "snow":
        return p.ability in ("ゆきかき", "ゆきがくれ", "アイスボディ") or "こおり" in t
    return False


def _baton_recipient_value(p):
    v = float(max(p.attack, p.sp_attack))
    if p.mega_data is not None:
        v *= 1.2
        if p.mega_data.ability == "マジックミラー":   # ふきとばし等の積みリセットを無効化
            v *= 1.4
    return v


def _synergy_bonus(trio_pokes):
    """数ターン戦略のシナジー加点：天候(設置役+活用役)、バトン(積み役+受けエース)。"""
    bonus = 0.0
    # 天候シナジー
    for p in trio_pokes:
        w = _sets_weather(p)
        if w and any(_abuses_weather(q, w) for q in trio_pokes if q is not p):
            bonus += _AVG_HP * 0.6
            break
    # バトンシナジー：積み役(バトンタッチ＋積み技/かそく) ＋ 受けエース
    passers = [p for p in trio_pokes
               if "バトンタッチ" in _moves_of(p) and (p.ability == "かそく" or _moves_of(p) & _SETUP)]
    if passers:
        recips = [p for p in trio_pokes if "バトンタッチ" not in _moves_of(p)]
        if recips:
            best = max(_baton_recipient_value(p) for p in recips)
            bonus += _AVG_HP * 0.5 * min(2.0, best / 150.0)  # 強い受け先(メガピクシー等)ほど高い
    return bonus


def candidate_selections(party6, opp6, k: int = 10) -> List[Selection]:
    """ヒューリスティックで有望な選出 top-k を列挙する（先頭=index0）。"""
    n = len(party6)
    if n <= 3:
        return [tuple(range(n)) + tuple([0] * (3 - n))][:1] if n else []
    field = BattleField()

    def dmg_score(p):
        s = sum(max((expected_damage(p, o, mv, field) for mv in p.moves if mv), default=0.0)
                for o in opp6)
        if any(mv and mv.name_jp in HAZARD_MOVES and mv.category == "status" for mv in p.moves):
            s += len(opp6) * _AVG_HP * 0.125 * 2
        return s

    def lscore(p):
        hz = any(mv and mv.name_jp in HAZARD_MOVES and mv.category == "status" for mv in p.moves)
        se = sum(1 for o in opp6 if any(
            get_type_effectiveness(mv.type, o.type1, o.type2) >= 2.0
            for mv in p.moves if mv and mv.category != "status" and mv.power))
        return (100 if hz else 0) + se

    # 各ポケの素点と「メガ化による加点」。1サイドはメガ1体のみなので、
    # トリオの得点は素点合計＋トリオ内で最良の単一メガ加点だけ（2メガを過大評価しない）。
    ps_base = [dmg_score(p) for p in party6]
    mega_gain = []
    for i, p in enumerate(party6):
        mf = _scoring_form(p)
        mega_gain.append(max(0.0, dmg_score(mf) - ps_base[i]) if mf is not p else 0.0)
    ls = [lscore(p) for p in party6]

    sels = []
    for trio in combinations(range(n), 3):
        base = sum(ps_base[i] for i in trio)
        megas_in = [i for i in trio if mega_gain[i] > 0]
        bonus = max((mega_gain[i] for i in megas_in), default=0.0)  # 実際にメガできるのは1体
        forgone = sum(mega_gain[i] for i in megas_in) - bonus       # 2体目以降が逃したメガ価値
        # メガ石を2枚以上選んでも1体しかメガできず、残りは素のフォルム＝構造的に損。
        # 逃したメガ価値＋スロットの機会損失をフラット減点して、基本1メガに寄せる。
        n_mega = sum(1 for i in trio if party6[i].mega_data is not None)
        extra_mega_penalty = forgone + _AVG_HP * 0.4 * max(0, n_mega - 1)
        synergy = _synergy_bonus([party6[i] for i in trio])         # 天候/バトン等の数ターン戦略
        for lead in trio:
            rest = [i for i in trio if i != lead]
            sels.append(((lead, rest[0], rest[1]), base + bonus - extra_mega_penalty + synergy + ls[lead]))
    sels.sort(key=lambda x: x[1], reverse=True)
    return [s for s, _ in sels[:k]]


def selection_to_party(party6, sel: Selection):
    return [party6[i] for i in sel]


def payoff_matrix(p1: RegisteredParty, p2: RegisteredParty, sels1, sels2,
                  loader, ai=None, samples: int = 6, season: str = "M-2",
                  seed: int = 0, ai_factory=None, with_belief: bool = False):
    """W[i][j] = sels1[i] 対 sels2[j] での p1 勝率（samples 試合の平均）。

    ai_factory(loader)→AI を渡すと行動方策を差し替え可能（例: SearchAI）。
    with_belief=True で両サイドに OpponentBelief を付与（SearchAI のEV/性格推定を有効化）。
    """
    battle_ai = ai_factory(loader) if ai_factory is not None else (ai or HeuristicAI())
    random.seed(seed)
    W = [[0.0] * len(sels2) for _ in sels1]
    for i, si in enumerate(sels1):
        for j, sj in enumerate(sels2):
            wins = 0
            for _ in range(samples):
                a1 = build_party(p1, loader, season)
                a2 = build_party(p2, loader, season)
                s1 = BattleSide(selection_to_party(a1, si))
                s2 = BattleSide(selection_to_party(a2, sj))
                if with_belief:
                    s1.belief = OpponentBelief(loader, season)
                    s2.belief = OpponentBelief(loader, season)
                if Battle(s1, s2).run(battle_ai, battle_ai) == 1:
                    wins += 1
            W[i][j] = wins / samples
    return W


def solve_zero_sum(W, iters: int = 20000):
    """行プレイヤー最大化・列プレイヤー最小化のゼロサム行列ゲームを
    fictitious play で解く。戻り値 (行混合戦略, 列混合戦略, ゲーム値)。"""
    n, m = len(W), len(W[0])
    row_cnt = [0] * n
    col_cnt = [0] * m
    row_pay = [0.0] * m   # 行が bi を選んだ累積 → 列が見る各列の累積利得
    col_pay = [0.0] * n   # 列が cj を選んだ累積 → 行が見る各行の累積利得
    cj = 0
    for _ in range(iters):
        for i in range(n):
            col_pay[i] += W[i][cj]
        bi = max(range(n), key=lambda i: col_pay[i])
        row_cnt[bi] += 1
        for j in range(m):
            row_pay[j] += W[bi][j]
        cj = min(range(m), key=lambda j: row_pay[j])
        col_cnt[cj] += 1
    x = [c / iters for c in row_cnt]
    y = [c / iters for c in col_cnt]
    value = sum(x[i] * W[i][j] * y[j] for i in range(n) for j in range(m))
    return x, y, value


def solve_matchup(p1: RegisteredParty, p2: RegisteredParty, loader,
                  ai=None, k: int = 8, samples: int = 6, season: str = "M-2",
                  seed: int = 0, ai_factory=None, with_belief: bool = False):
    """1対戦カードの選出ナッシュ均衡を解く。
    戻り値 dict: sels1/x(p1混合戦略)/sels2/y(p2混合戦略)/value(p1から見たゲーム値)。
    ai_factory/with_belief で行動方策（例: SearchAI＋belief）を差し替え可能。"""
    a1 = build_party(p1, loader, season)
    a2 = build_party(p2, loader, season)
    sels1 = candidate_selections(a1, a2, k)
    sels2 = candidate_selections(a2, a1, k)
    W = payoff_matrix(p1, p2, sels1, sels2, loader, ai, samples, season, seed,
                      ai_factory=ai_factory, with_belief=with_belief)
    x, y, value = solve_zero_sum(W)
    return {"sels1": sels1, "x": x, "sels2": sels2, "y": y, "value": value, "W": W}


def sample_selection(sels: List[Selection], mix: List[float], rng: random.Random) -> Selection:
    r = rng.random() * (sum(mix) or 1.0)
    for s, p in zip(sels, mix):
        r -= p
        if r <= 0:
            return s
    return sels[-1]


def nash_select_net(my6, opp6, loader, net, k: int = 8, samples: int = 16,
                    seed: int = 0, return_mix: bool = False):
    """学習ネット(NetGreedyAI)基準で選出ナッシュを解く。任意パーティ対応（built party を受け取る）。

    payoff は NetGreedyAI(net) 同士の対戦勝率（探索なしで高速）。各対戦で個体を複製し汚染を防ぐ。
    返り値: 選んだ3体（return_mix=True なら (sel, sels1, mix, value)）。
    """
    from .alphazero import NetGreedyAI
    rng = random.Random(seed)
    sels1 = candidate_selections(my6, opp6, k)
    sels2 = candidate_selections(opp6, my6, k)
    if not sels1:
        sel = tuple(range(min(3, len(my6))))
        return (sel, sels1, [], 0.0) if return_mix else list(my6[:3])
    W = [[0.0] * len(sels2) for _ in sels1]
    for i, si in enumerate(sels1):
        for j, sj in enumerate(sels2):
            wins = 0
            for _ in range(samples):
                s1 = BattleSide([copy.deepcopy(my6[t]) for t in si])
                s2 = BattleSide([copy.deepcopy(opp6[t]) for t in sj])
                s1.belief = OpponentBelief(loader)
                s2.belief = OpponentBelief(loader)
                if Battle(s1, s2).run(NetGreedyAI(net), NetGreedyAI(net)) == 1:
                    wins += 1
            W[i][j] = wins / samples
    x, y, value = solve_zero_sum(W)
    sel = sample_selection(sels1, x, rng)
    if return_mix:
        return sel, sels1, x, value
    return selection_to_party(my6, sel)
