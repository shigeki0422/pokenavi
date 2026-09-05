"""1v1判定を対戦本体で実走して求める。

従来 `_explain._mu_score` はダメージ計算だけを使った静的評価だったため、
「対戦本体では正しい仕様が分析側では抜ける」バグが繰り返し発生した
（天候・フィールド・いかく・トレース・ばけのかわの削り・マルチスケイルの初撃限定・
半減きのみの消費・ロール引数の取り違え…）。実測でも静的評価と実走の一致率は72.6%だった。

ここでは 1v1 を対戦本体で実際に走らせて確定数を数える。追加効果・自己ランク低下・
反動・回復・特性の発動など、engine が実装している全てが自動的に反映される。

確定数の定義（最低乱数・急所なし・必中）に合わせるため:
  - damage._ROLL_OVERRIDE = 0.0 で全ダメージを最低ロールに固定
  - check_hit を常に True（命中率のブレを排除）
  - 攻撃側は同じ技を撃ち続け、防御側は行動しない（片側の火力だけを測る）
"""
import math
import os
import random as _rnd
from functools import lru_cache

import simulator.damage as _DMG
import simulator.battle as _BT
from simulator.battle import BattleField, BattleSide, Battle, Action
from simulator.pokemon import build_from_spec, parse_pokemon_spec

_NEXT_BELOW_ONE = math.nextafter(1.0, 0.0)

SEASON = "M-3"
CAP = int(os.environ.get("MU_ENGINE_CAP", "12"))   # これ以上かかる技は「圏外」扱い（表示上5以上は同じ）


def _build(spec, L):
    p = build_from_spec(parse_pokemon_spec(spec), L, season=SEASON, randomize=False)
    if p.mega_data is not None:
        p.do_mega_evolve()
    return p


class _Fixed:
    """常に同じ技を撃つAI。"""
    def __init__(self, name): self.name = name

    def __call__(self, my, opp, field):
        me = my.active
        for i, mv in enumerate(me.moves):
            if mv is not None and mv.name_jp == self.name:
                return Action(type="move", move=mv, move_idx=i)
        return Action(type="pass")


def _pass(my, opp, field):
    return Action(type="pass")


def _run(spec_0, spec_1, move_name, L, roll=0.0, att=0):
    """並び (spec_0, spec_1) の対面で、att 側が move_name を撃ち続けて
    もう一方を倒すまでのターン数と、1発目の被ダメ割合。

    攻撃側を常に先に入場させると、両者が天候特性を持つ対面（キュウコン vs ペリッパー等）で
    「後から出た側の天候が勝つ」規則により、評価する向きで場が変わってしまう。
    場は対面ごとに1つなので、並びは固定して攻撃側だけを指定する。
    確定数の前提（最低乱数・必中）はこの関数自身が確立する。外側の文脈に依存させると
    lru_cache が「乱数あり」で計算した値を保持してしまう（実際に汚染を確認した）。
    roll は正規化値（0.0=最低乱数 / 1.0=最高乱数）。既定は確定数の定義どおり最低乱数。"""
    _enter_fixed(roll)
    try:
        return _run_inner(spec_0, spec_1, move_name, L, att)
    finally:
        _exit_fixed()


def _run_inner(spec_0, spec_1, move_name, L, att=0):
    """並び (spec_0, spec_1) で入場させ、att 側だけが move_name を撃ち続ける。
    入場順は場（天候・フィールド）の成立に効くので、攻撃側がどちらでも変えない。"""
    P = [_build(spec_0, L), _build(spec_1, L)]
    D = P[1 - att]                      # 倒す相手
    hp0 = D.max_hp
    s1 = BattleSide([P[0]], viewer_label="P1", source6=[P[0]])
    s2 = BattleSide([P[1]], viewer_label="P2", source6=[P[1]])
    b = Battle(s1, s2, BattleField())
    first = {"dmg": None}
    n = {"t": 0}
    ai = _Fixed(move_name)

    def attacker(my, opp, field):
        n["t"] += 1
        if first["dmg"] is None and n["t"] == 2:
            first["dmg"] = hp0 - D.hp        # 1ターン目終了後の減少量
        return ai(my, opp, field)

    # run() は max_turns を取らないので、_turn_loop に渡すため入場効果だけ run と同じ手順で実行する
    b._faint_chooser1 = None; b._faint_chooser2 = None
    from simulator.battle import _entry_effects as _ee
    _ee(P[0], 0, b.field, P[1], b.logs, [P[0]])
    _ee(P[1], 1, b.field, P[0], b.logs, [P[1]])
    ai1, ai2 = (attacker, _pass) if att == 0 else (_pass, attacker)
    b._turn_loop(ai1, ai2, max_turns=CAP)
    if first["dmg"] is None:
        first["dmg"] = hp0 - D.hp
    hits = n["t"] if not D.is_alive else 999
    return hits, max(0.0, first["dmg"] / max(1, hp0))


@lru_cache(maxsize=200000)
def _best_cached(spec_0, spec_1, att, _lid):
    """並び (spec_0, spec_1) の対面における att 側の最大打点技と、その確定数・被ダメ割合。
    「1発の火力」ではなく「同じ技を撃ち続けて何発で倒せるか」で選ぶ（りゅうせいぐん等、
    使用後に自分のランクが下がる技は1発目が最大でも実際は遅い）。"""
    L = _LOADER[0]
    A = _build(spec_0 if att == 0 else spec_1, L)
    best = (999, 0.0, "—")
    for mv in A.moves:
        if mv is None or mv.category == "status" or not (mv.power or 0):
            continue
        # 相手依存で評価が歪む技（反射技・HP依存技）は最大打点の候補から外す
        if mv.name_jp in _BT.MATCHUP_EXCLUDED:
            continue
        h, r = _run(spec_0, spec_1, mv.name_jp, L, 0.0, att)
        if (h, -r) < (best[0], -best[1]):
            best = (h, r, mv.name_jp)
    return best


_LOADER = [None]
_STATE = {"depth": 0}


def _enter_fixed(roll=0.0):
    """確定数の前提を固定する。
    最低乱数・必中に加え、追加効果（アクアブレイクの防御ダウン等）と急所を発動させない。
    確定数は「保証値」なので、運良く追加効果が乗った場合の発数を出してはいけない。
    固定しないと対戦本体が乱数を引いて呼ぶたび結果が変わる（実際に11%の不一致として出た）。"""
    if _STATE["depth"] == 0:
        _STATE["roll"] = getattr(_DMG, "_ROLL_OVERRIDE", None)
        _STATE["hit"] = _BT.check_hit
        _STATE["rand"] = _rnd.random
        _STATE["randint"] = _rnd.randint
        _STATE["choice"] = _rnd.choice
        _STATE["choices"] = _rnd.choices
        _DMG._ROLL_OVERRIDE = roll
        _BT.check_hit = lambda *a, **k: True
        # 1発ごとの命中判定も必中扱い。外れて止まる技（ネズミざん）は最大回数まで当たる。
        # そうしないと「1発しか当たらない前提」になり、イッカネズミの主力技が圏外になる。
        _STATE["hitcont"] = _BT._HIT_CONTINUE
        _BT._HIT_CONTINUE = lambda: 0.0
        # 2〜5回の連続技は重み3:3:1:1で期待値がちょうど3.0。最小の2回だと過小、
        # 最大の5回だと過大なので期待値で固定する（スキルリンクは先に5回で決まる）。
        _STATE["mhits"] = _BT._MULTI_HIT_FIXED
        _BT._MULTI_HIT_FIXED = 3
        # 1v1判定は互いに攻撃し合う対面なので、ふいうちも通る前提で評価する。
        _STATE["oppatk"] = _BT._ASSUME_OPP_ATTACKS
        _BT._ASSUME_OPP_ATTACKS = True
        # 1.0 ちょうど未満の最大値。判定は全て `random() < prob` なので、
        # prob<1 の追加効果は不発、prob=1 の確定効果（必中急所・りゅうせいぐんの特攻ダウン等）
        # だけが発動する。1.0 を入れると `1.0 < 1.0` が偽になり確定効果まで殺す（実際に殺していた）
        _rnd.random = lambda: _NEXT_BELOW_ONE
        _rnd.randint = lambda a, b: a        # 連続技は最小回数
        # ムラっけ等の random.choice も固定する。固定しないと呼ぶたび確定数が変わり、
        # 表示とキャッシュが不安定になる（実際に8件の不一致として出た）。
        _rnd.choice = lambda seq: list(seq)[0]
        # 連続技の回数（つららばり等）は random.choices。確定数は保証値なので最小回数にする
        _rnd.choices = lambda pop, weights=None, k=1, **kw: [list(pop)[0]] * k
    _STATE["depth"] += 1


def _exit_fixed():
    _STATE["depth"] -= 1
    if _STATE["depth"] == 0:
        _DMG._ROLL_OVERRIDE = _STATE["roll"]
        _BT.check_hit = _STATE["hit"]
        _BT._HIT_CONTINUE = _STATE["hitcont"]
        _BT._MULTI_HIT_FIXED = _STATE["mhits"]
        _BT._ASSUME_OPP_ATTACKS = _STATE["oppatk"]
        _rnd.random = _STATE["rand"]
        _rnd.randint = _STATE["randint"]
        _rnd.choice = _STATE["choice"]
        _rnd.choices = _STATE["choices"]


def mu_engine(spec_a, spec_b, L):
    """(myh, myr, my_move, thh, thr, th_move) を対戦本体の実走で返す。"""
    _LOADER[0] = L
    # 場は対面ごとに1つなので、並びを固定して攻撃側だけを切り替える
    ah, ar, am = _best_cached(spec_a, spec_b, 0, id(L))
    bh, br, bm = _best_cached(spec_a, spec_b, 1, id(L))
    return ah, ar, am, bh, br, bm


def _run_one(spec_0, spec_1, move_name, L, roll=0.0, att=0):
    """対戦本体に1回だけ技を撃たせ、(与ダメ, 防御側生存, 残HP) を返す。
    engine の analysis::executed_damage と対応。表示には「実際に与えた分」ではなく
    技の威力を使うが、防御側が生き残る場合はこの値が正しい
    （じきゅうりょくのように連続技の合間に相手の特性が挟まる場合、本体の値だけが合う）。"""
    _enter_fixed(roll)
    try:
        P = [_build(spec_0, L), _build(spec_1, L)]
        D = P[1 - att]
        s1 = BattleSide([P[0]], viewer_label="P1", source6=[P[0]])
        s2 = BattleSide([P[1]], viewer_label="P2", source6=[P[1]])
        b = Battle(s1, s2, BattleField())
        from simulator.battle import _entry_effects as _ee, _execute_move as _em
        _ee(P[0], 0, b.field, P[1], b.logs, [P[0]])
        _ee(P[1], 1, b.field, P[0], b.logs, [P[1]])
        A = P[att]
        mv = next((m for m in A.moves if m is not None and m.name_jp == move_name), None)
        if mv is None:
            return 0, True, D.hp
        act = Action(type="move", move=mv, move_idx=A.moves.index(mv))
        opp_mv = next((m for m in D.moves if m is not None), None)
        opp_act = Action(type="move", move=opp_mv, move_idx=0)
        out = []
        _em((s1, s2)[att], (s1, s2)[1 - att], act, b.field, opp_act, out)
        return (out[0] if out else 0), D.is_alive, D.hp
    finally:
        _exit_fixed()


def _hit_damage_loop(spec_0, spec_1, mv_name, L, roll, att, n_hits):
    """技の威力ぶんのダメージ（全ヒット合計）。相手が倒れても止めない。
    対戦本体は倒れるとヒットループを止めるので、表示用の威力はこちらで出す。"""
    from simulator.battle import apply_pre_move_forms, _check_critical
    from simulator.damage import calc_damage
    P = [_build(spec_0, L), _build(spec_1, L)]
    A, D = P[att], P[1 - att]
    f = BattleField()
    from simulator.battle import _entry_effects as _ee
    _ee(P[0], 0, f, P[1], [], [P[0]])
    _ee(P[1], 1, f, P[0], [], [P[1]])
    mv = next((m for m in A.moves if m is not None and m.name_jp == mv_name), None)
    if mv is None:
        return 0
    apply_pre_move_forms(A, mv)
    crit = _check_critical(A, mv, D)
    total = 0
    for hit_i in range(max(1, n_hits)):
        A._multi_hit_index = hit_i
        d = calc_damage(A, D, mv, f, crit, roll)
        total += d
        D.hp = max(1, D.hp - d)      # マルチスケイル等を2発目以降に持ち越さない
    return total


def move_damage(spec_0, spec_1, mv_name, L, roll=0.0, att=0):
    """表示するダメージ。engine の analysis::move_damage と対応。

    防御側が生き残り、切り詰め（きあいのタスキ・がんじょう）も起きていないなら、
    対戦本体に実際に撃たせた値をそのまま使う。連続技の合間に相手の特性が挟まる場合
    （じきゅうりょくで2発目の防御が上がる等）は本体の値だけが正しい。
    倒れる場合は本体がヒットループを止めるので、そのときだけ威力を自前で出す。
    """
    ex, alive, hp = _run_one(spec_0, spec_1, mv_name, L, roll, att)
    if ex > 0 and alive and hp > 1:
        return ex
    _enter_fixed(roll)
    try:
        from simulator.battle import _calc_hits
        A = _build(spec_0 if att == 0 else spec_1, L)
        mv = next((m for m in A.moves if m is not None and m.name_jp == mv_name), None)
        n = max(1, _calc_hits(mv, A)) if mv is not None else 1
    finally:
        _exit_fixed()
    _enter_fixed(roll)
    try:
        d = _hit_damage_loop(spec_0, spec_1, mv_name, L, roll, att, n)
    finally:
        _exit_fixed()
    if d == 0 and mv is not None and not (mv.power or 0):
        # がむしゃら等、威力がDBに無く対戦本体の中でHPから決まる技
        return ex
    return d
