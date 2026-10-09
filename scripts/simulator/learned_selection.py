"""学習選出（MCTS教師で学習したValMLP選出評価器）。本番の選出（select_party の drop-in 置換）。
モデル: simulator/selector_m6e.json（M-6、2026-10-09 採用。入力 megaform_ohko1＝メガ石持ちをメガ後の形で表し一撃必殺の期待値を追加。m6d 比 51.2% z+2.11。sel_mega_1009）。
旧: selector_m6d.json（2026-10-06 採用。retrain_1005 ft3e4_c1・相手の仮定 learnedK8 が既定。SEL_OPP_ASSUME=heur で旧既定）。旧: selector_m6b.json（2026-09-30）。教師＝本番AI（Rust MCTS@400・JOINT_BUILD既定ON）で、自分の候補
（3体＋先頭、メガ1体ルール内）を相手の選出をサンプリングして戦わせた勝率（段階1＋段階2b、1599対面）。入力は現行の既定特徴量（1037次元）。
A/B（Rust MCTS@400・3プール各4000戦）: vs 相性ベースの規則的な選出 52.1〜52.7%（z=+2.7〜+3.5）、同ベースライン vs 旧 selector_m6 は有意差なし。
既定で有効。LEARNED_SELECTION=0 でヒューリスティック選出（ai.select_party）。SELECTOR_PATH で別のモデル。
モデルが無い・入力次元が現行の特徴量と合わないときはヒューリスティックに落ちる（旧 selector_m2/m3 は905次元で現行では動かない）。
"""
import os
import json
import math
import random
import sys
from itertools import combinations

import numpy as np

_MODEL = None
_LOADED = False
_PATH = os.environ.get("SELECTOR_PATH") or os.path.join(os.path.dirname(__file__), "selector_m6e.json")


def _load():
    global _MODEL, _LOADED
    if _LOADED:
        return _MODEL
    _LOADED = True
    if os.environ.get("LEARNED_SELECTION", "1") == "0" or not os.path.exists(_PATH):
        _MODEL = None
        return None
    with open(_PATH) as f:
        d = json.load(f)
    from .features import feature_dim, SEL_FEAT_V2, SEL_EXTRA_V2
    W1 = np.asarray(d["W1"], float)
    feat = d.get("feat")
    if feat not in (None, SEL_FEAT_V2):
        print(f"[learned_selection] {_PATH}: 入力の形式 {feat} は未対応 → ヒューリスティック選出", file=sys.stderr, flush=True)
        _MODEL = None
        return None
    want = feature_dim() + (SEL_EXTRA_V2 if feat == SEL_FEAT_V2 else 0)
    if W1.shape[1] != want:
        print(f"[learned_selection] {_PATH}: 入力{W1.shape[1]}次元 ≠ 現行の特徴量{want}次元 → ヒューリスティック選出",
              file=sys.stderr, flush=True)
        _MODEL = None
        return None
    act = d.get("act", "tanh")
    if act not in ("tanh", "relu") or "U" in d:
        print(f"[learned_selection] {_PATH}: 活性化 {act}・入力の追加（U）は未対応 → ヒューリスティック選出", file=sys.stderr, flush=True)
        _MODEL = None
        return None
    _MODEL = {"W1": W1, "b1": np.asarray(d["b1"], float),
              "W2": np.asarray(d["W2"], float), "b2": float(d["b2"]), "act": act, "v2": feat == SEL_FEAT_V2}
    return _MODEL


def _predict(model, X):
    X = np.asarray(X, float)
    Z = X @ model["W1"].T + model["b1"]
    H = np.maximum(Z, 0.0) if model.get("act") == "relu" else np.tanh(Z)
    return 1.0 / (1.0 + np.exp(-(H @ model["W2"] + model["b2"])))


def _mega_plus_random(party6, rng, n=3):
    """メガ1体＋非メガをランダムでn-1体（メガ+受け+攻め補完の現実的な選出）。メガ無しなら全ランダム。
    交代が機能する多様な対面を作るための選出（攻撃偏重を避ける）。"""
    rng = rng or random
    if len(party6) <= n:
        return list(party6)
    megas = [p for p in party6 if getattr(p, "mega_data", None) is not None]
    sel = [rng.choice(megas)] if megas else []
    pool = [p for p in party6 if p not in sel and getattr(p, "mega_data", None) is None]
    rng.shuffle(pool)
    sel += pool[:n - len(sel)]
    if len(sel) < n:
        rest = [p for p in party6 if p not in sel]
        rng.shuffle(rest); sel += rest[:n - len(sel)]
    return sel[:n]


def _opp_assumptions(party6, opp6, loader, n, rng):
    """相手の選出の仮定: ヒューリスティック選出の温度0＋温度1×2（select_party を3回呼ぶのと同じ結果・乱数）"""
    from .ai import select_party_multi
    return select_party_multi(opp6, party6, loader, n=min(n, len(opp6)), temperatures=(0.0, 1.0, 1.0), rng=rng)


def _candidates(party6, n):
    """候補（3体＋先頭の並び、添字）。メガ1体ルール: メガ石持ちがいれば「ちょうど1体」（MIN_MEGA/MAX_MEGA で緩められる）"""
    avail_mega = sum(1 for p in party6 if getattr(p, "mega_data", None) is not None)
    _target = 1 if avail_mega >= 1 else 0
    _max_mega = int(os.environ.get("MAX_MEGA", str(_target)))
    _min_mega = int(os.environ.get("MIN_MEGA", str(_target)))
    out = []
    for combo in combinations(range(len(party6)), n):
        nmega = sum(1 for i in combo if getattr(party6[i], "mega_data", None) is not None)
        if nmega < _min_mega or nmega > _max_mega:
            continue
        for li in range(n):
            out.append([combo[li]] + [combo[j] for j in range(n) if j != li])
    return out


def _encode_ref(order, osel, v2=False):
    """元の実装の状態ベクトル（毎回その場で encode_state）。calc_damage の副作用（半減きのみの消費・かるわざ等）を
    次の候補へ持ち越さないよう、符号化の前後で関係する個体を巻き戻す。
    v2（入力 megaform_ohko1）: メガ石持ちはメガ後の複製で符号化し、末尾に一撃必殺の期待値18次元"""
    from .battle import BattleSide, BattleField
    from .features import encode_state, sel_mega_view, sel_extra
    from .ai import _state_snapshot, _state_restore
    snap = _state_snapshot(list(order) + list(osel))
    try:
        if v2:
            order = [sel_mega_view(p) for p in order]; osel = [sel_mega_view(p) for p in osel]
            ex = sel_extra(order, osel)
        s1 = BattleSide(list(order)); s2 = BattleSide(list(osel)); s1.field_idx = 0; s2.field_idx = 1
        x = encode_state(s1, s2, BattleField())
        return x + ex if v2 else x
    finally:
        _state_restore(snap)


class _FastEncoder:
    """対面内で使い回す部品（各個体の特徴ブロック・全対面の与ダメ割合・実効速度）から、候補×相手の仮定の状態ベクトルを
    組み立てる。_encode_ref と完全に同じ値（test_all 26l と _local の照合で確認）。前提: 選出時点の個体（無傷・能力変化なし）。"""

    def __init__(self, party6, opp_sels, v2=False):
        from .battle import BattleSide, BattleField
        from . import features as FT
        self.FT = FT
        self.v2 = v2
        self.views = {}
        self.field = BattleField()
        self.dside = BattleSide([])            # 既定の陣営（画面・おいかぜ等なし）
        self.block = {}
        self.frac = {}
        self.spd = {}
        self._const = None

    def _pristine(self, pokes, fn):
        from .ai import _state_snapshot, _state_restore
        snap = _state_snapshot(pokes)
        try:
            return fn()
        finally:
            _state_restore(snap)

    def _v(self, p):
        if not self.v2:
            return p
        k = id(p)
        if k not in self.views:
            self.views[k] = (p, self.FT.sel_mega_view(p))
        return self.views[k][1]

    def _blk(self, p):
        k = id(p)
        if k not in self.block:
            p = self._v(p)
            self.block[k] = self._pristine([p], lambda: self.FT._poke_block(p, self.dside, False))
        return self.block[k]

    def _fr(self, a, d):
        k = (id(a), id(d))
        if k not in self.frac:
            a, d = self._v(a), self._v(d)
            self.frac[k] = self._pristine([a, d], lambda: self.FT._expected_frac(a, d, self.field, self.dside))
        return self.frac[k]

    def _sp(self, p):
        k = id(p)
        if k not in self.spd:
            p = self._v(p)
            self.spd[k] = self._pristine([p], lambda: self.FT._real_speed(p, self.dside, self.field))
        return self.spd[k]

    def _side(self, trio):
        FT = self.FT
        f = []
        for p in trio:
            f += self._blk(p)
        act = trio[0]
        f += [max(-1.0, min(1.0, getattr(act, s, 0) / 6.0)) for s in FT._STAGES]
        alive = [p for p in trio if p.is_alive]
        f.append(len(alive) / 3.0)
        f.append(sum(p.hp / p.max_hp for p in alive if p.max_hp) / 3.0)
        return f

    def encode(self, order, osel):
        FT = self.FT
        if self._const is None:        # 陣営・場の既定値だけで決まる後半（開示・天候・設置・画面など）
            ref = _encode_ref(order, osel)
            lo = 2 * FT._PER_SIDE + FT._MATRIX + FT._SPEEDMAT
            self._const = ref[lo:-2]
        f = self._side(order) + self._side(osel)
        for a in order:
            for d in osel:
                f.append(self._fr(a, d))
        for a in osel:
            for d in order:
                f.append(self._fr(a, d))
        s1s = [self._sp(p) for p in order]; s2s = [self._sp(p) for p in osel]
        for i in range(3):
            for j in range(3):
                f.append(0.0 if (s1s[i] < 0 or s2s[j] < 0) else (1.0 if s1s[i] >= s2s[j] else 0.0))
        f += self._const
        a1, a2 = self._v(order[0]), self._v(osel[0])
        e1, e2 = a1.get_effective_speed(), a2.get_effective_speed()
        f.append(1.0 if e1 >= e2 else 0.0)
        f.append(max(-1.0, min(1.0, (e1 - e2) / 200.0)))
        if self.v2:
            f += self.FT.sel_extra([self._v(p) for p in order], [self._v(p) for p in osel])
        return f


# calc_damage が消費する半減きのみ（damage.py）。1回の符号化の中で消費が次の対面の計算へ持ち越される（元の実装の挙動）ので、
# これを持つ個体がいる対面は部品の使い回しができない＝元の実装で計算する
_CONSUMED_BERRIES = frozenset((
    "オッカのみ", "イトケのみ", "ソクノのみ", "リンドのみ", "ヤチェのみ", "ヨプのみ", "ビアーのみ", "シュカのみ", "バコウのみ",
    "ウタンのみ", "タンガのみ", "ヨロギのみ", "カシブのみ", "ハバンのみ", "ナモのみ", "リリバのみ", "ロゼルのみ", "ホズのみ"))


# ダメージ計算がグローバル乱数を消費する技（_live_rust.RNG_MOVES と同じ）。これを持つ個体がいる対面は、符号化のたびに乱数を
# 消費する元の実装でしか同じ結果にならない（高速版は計算を使い回して消費回数が減る・Rust 版は乱数を持たない＝panic していた）
_RNG_MOVES = frozenset(("きまぐレーザー",))


def _has_rng_move(pokes):
    return any(m is not None and m.name_jp in _RNG_MOVES for p in pokes for m in (p.moves or []))


def _fast_ok(party6, opp6):
    """_FastEncoder の前提（無傷・能力変化なし・状態異常なし・未メガ・半減きのみ無し・乱数を消費する技無し）を満たすか。
    満たさなければ元の実装で"""
    from .features import _STAGES
    if _has_rng_move(list(party6) + list(opp6)):
        return False
    for p in list(party6) + list(opp6):
        if (not p.is_alive or p.hp != p.max_hp or p.status or p.mega_evolved or p.item in _CONSUMED_BERRIES
                or any(getattr(p, s, 0) for s in _STAGES)):
            return False
    return True


def _rust_ok(party6, opp6):
    """Rust 版は選出時点の個体（spec から組み直せる状態）が前提。半減きのみは元の実装と同じ順で消費するので可"""
    from .features import _STAGES
    if _has_rng_move(list(party6) + list(opp6)):
        return False
    return all(p.is_alive and p.hp == p.max_hp and not p.status and not p.mega_evolved
               and not any(getattr(p, s, 0) for s in _STAGES) for p in list(party6) + list(opp6))


def _rust_states(party6, opp6, n, rng, osels=None, v2=False):
    """Rust 版（pokenavi_engine.learned_select_states）: 候補・相手の仮定・状態ベクトルを Rust で作る。
    相手の仮定の温度つきサンプリングは Python の乱数状態を渡して Rust で進め、終わった状態を書き戻す（乱数の消費も Python と同じ）。
    使えなければ None（Python 版へ）。"""
    if os.environ.get("ENGINE", "rust").lower() != "rust" or os.environ.get("LEARNED_SELECTION_RUST", "1") == "0":
        return None
    try:
        import engine_dispatch as _ED
        m = _ED.rust()
    except Exception:
        return None
    if m is None or not hasattr(m, "learned_select_states"):
        return None
    from .selection_matchup import spec_of
    try:
        st = rng.getstate()
        avail_mega = sum(1 for p in party6 if getattr(p, "mega_data", None) is not None)
        _t = 1 if avail_mega >= 1 else 0
        r = m.learned_select_states([spec_of(p) for p in party6], [spec_of(p) for p in opp6],
                                    os.environ.get("POOL_SEASON", "M-6"), n,
                                    int(os.environ.get("MIN_MEGA", str(_t))), int(os.environ.get("MAX_MEGA", str(_t))),
                                    list(st[1]), osels, **({"megaform": True} if v2 else {}))
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:           # Rust の panic は PyO3 では BaseException（PanicException）。Python 版へ落とす
        return None
    cands, osels, xb, dim, newst = r
    rng.setstate((st[0], tuple(newst), st[2]))
    X = np.frombuffer(xb, dtype="<f8").reshape(len(cands), len(osels), dim)
    return cands, osels, X


def _agg(p, agg):
    """相手の仮定ごとの予測 p から候補の値（Rust selector::Agg と同じ定義・同じ和の順）。
    agg: None＝平均 / ("w", 重み)＝重み付き和 / ("minmix", α, g)＝α·平均＋(1−α)·（g 個ずつの平均の最小）"""
    if agg is None:
        return float(np.mean(p))
    if agg[0] == "w":
        acc = 0.0
        for w, x in zip(agg[1], p):
            acc += w * float(x)
        return acc
    a, g = agg[1], agg[2]
    tot = 0.0
    for x in p:
        tot += float(x)
    mn = math.inf
    for i in range(0, len(p), g):
        t = 0.0
        for x in p[i:i + g]:
            t += float(x)
        mn = min(mn, t / len(p[i:i + g]))
    return a * (tot / len(p)) + (1.0 - a) * mn


def _score_cands(party6, opp6, loader, n, rng, model, osel_idx=None, agg=None):
    """候補（添字の並び）と値（相手の仮定ごとの予測を agg で集めたもの。既定は平均）[(添字, 値)]。osel_idx: 相手の仮定
    （相手6体の添字の並び）を渡す（None ならヒューリスティック選出 温度0,1,1＝_opp_assumptions）"""
    impl = os.environ.get("LEARNED_SELECTION_IMPL", "auto")
    v2 = bool(model.get("v2"))
    if impl in ("auto", "rust") and _rust_ok(party6, opp6):
        r = _rust_states(party6, opp6, n, rng, osel_idx, v2)
        if r is not None:
            ci, oi, X = r
            if agg is None:
                return [(list(c), float(np.mean(_predict(model, X[k])))) for k, c in enumerate(ci)]
            P = _predict(model, X.reshape(-1, X.shape[2])).reshape(X.shape[0], X.shape[1])
            return [(list(c), _agg(P[k], agg)) for k, c in enumerate(ci)]
    if osel_idx is None:
        opp_sels = _opp_assumptions(party6, opp6, loader, n, rng)
    else:
        opp_sels = [[opp6[i] for i in o] for o in osel_idx]
    if impl in ("auto", "fast", "rust") and _fast_ok(party6, opp6):
        enc = _FastEncoder(party6, opp_sels, v2).encode
    else:
        enc = lambda order, osel: _encode_ref(order, osel, v2)
    out = []
    for c in _candidates(party6, n):
        order = [party6[i] for i in c]
        xs = [enc(order, osel) for osel in opp_sels]
        out.append((c, _agg(_predict(model, xs), agg)))
    return out


def _opp_learned(party6, opp6, loader, n, rng, model):
    """相手の選出の仮定を学習選出そのものに（env SEL_OPP_ASSUME=learned。既定はヒューリスティック 温度0,1,1）:
    相手側の学習選出（その中の仮定は既定どおりこちらのヒューリスティック選出）の温度0の最良＋温度 SEL_OPP_TEMP（既定1.0）の
    抽選2回。返り値は相手6体の添字の並び×3。相手が選ぶ余地が無い・候補が無いときは None（既定の仮定へ）"""
    nb = min(n, len(opp6))
    if len(opp6) <= nb:
        return None
    oc = _score_cands(opp6, party6, loader, nb, rng, model)
    if not oc:
        return None
    t = float(os.environ.get("SEL_OPP_TEMP", "1.0"))
    best = max(oc, key=lambda x: x[1])[0]
    return [list(best), list(_softmax_pick(oc, t, rng)), list(_softmax_pick(oc, t, rng))]


def _topk_weights(vals, temperature, k):
    """_softmax_pick と同じ重みの大きい順に k 個（同じ重みは添字の小さい方が先）と、和で割った重み（Rust selector::topk_weights）"""
    s = np.array(vals, float); sd = s.std()
    z = (s - s.mean()) / sd if sd > 1e-9 else s * 0.0
    ws = [float(w) for w in np.exp((z - z.max()) / max(1e-6, temperature))]
    order = sorted(range(len(ws)), key=lambda i: (-ws[i], i))[:max(1, k)]
    tot = 0.0
    for i in order:
        tot += ws[i]
    return [(i, ws[i] / tot) for i in order]


def _opp_mode():
    m = os.environ.get("SEL_OPP_ASSUME", "learnedK")
    return m if m in ("learned", "learnedK", "all") else None


def _opp_assume(party6, opp6, loader, n, rng, model):
    """相手の選出の仮定と集め方（env SEL_OPP_ASSUME。Rust selector::opp_sets と同じ定義。未指定は learnedK＝既定（2026-10-06〜）、heur 等それ以外は None＝ヒューリスティック 温度0,1,1・平均）
      learned  … _opp_learned（3通り・平均）
      learnedK … 相手側の学習選出の値の softmax（温度 SEL_OPP_TEMP）の上位 SEL_OPP_K（既定8）候補を、和を1にした重みで
      all      … 相手の全候補（3体＋先頭・メガ1体ルール内）。SEL_OPP_MIX=mean（既定）/ minmix（SEL_OPP_ALPHA（既定0.5）·平均＋
                  (1−α)·3体の組ごとの平均の最悪）/ weighted（全候補を softmax の重みで）
    返り値: (相手6体の添字の並びのリスト, agg)"""
    mode = _opp_mode()
    if mode is None:
        return None
    if mode == "learned":
        o = _opp_learned(party6, opp6, loader, n, rng, model)
        return (o, None) if o is not None else None
    nb = min(n, len(opp6))
    if len(opp6) <= nb:
        return None
    mix = os.environ.get("SEL_OPP_MIX", "mean")
    if mode == "all" and mix != "weighted":
        oc = _candidates(opp6, nb)
        if not oc:
            return None
        a = float(os.environ.get("SEL_OPP_ALPHA", "0.5")) if mix == "minmix" else 1.0
        return oc, ("minmix", a, nb)
    oc = _score_cands(opp6, party6, loader, nb, rng, model)
    if not oc:
        return None
    k = int(os.environ.get("SEL_OPP_K", "8")) if mode == "learnedK" else len(oc)
    tw = _topk_weights([v for _, v in oc], float(os.environ.get("SEL_OPP_TEMP", "1.0")), k)
    return [list(oc[i][0]) for i, _ in tw], ("w", [w for _, w in tw])


def learned_select_party(party6, opp6, loader, n=3, temperature=0.0, rng=None):
    """学習選出。temperature=0 で最良の3体(リード順)、>0 で softmax(score/temp) サンプリング。
    select_party と同一シグネチャ。モデル未ロード/3体以下は heuristic にフォールバック。
    SELECT_MODE=mcts のときはMCTS選出へ、=mega1 のとき現実的選出(メガ1+多様控え)へ委譲する。
    計算は Rust 版（ENGINE=rust かつ pokenavi_engine がある時）→ Python 高速版（部品の使い回し）→ 元の実装、の順に使える方で。
    どれも同じ選出・同じ乱数の消費（LEARNED_SELECTION_IMPL=ref/fast/rust で固定できる。照合用）。"""
    from .ai import select_party
    if os.environ.get("SELECT_MODE") == "mega1":   # 現実的選出（交代が機能する多様な対面）
        return _mega_plus_random(party6, rng, n)
    if os.environ.get("SELECT_MODE") == "matchup":   # 相性ベースの規則的な選出（ベースライン）
        from .selection_matchup import matchup_select_party
        return matchup_select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    if os.environ.get("SELECT_MODE") == "mcts":
        from .mcts_selection import mcts_select_party
        return mcts_select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    model = _load()
    if model is None or len(party6) <= n:
        return select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    rng = rng or random
    osel_idx, agg = _opp_assume(party6, opp6, loader, n, rng, model) or (None, None)
    cands = [([party6[i] for i in c], sc) for c, sc in _score_cands(party6, opp6, loader, n, rng, model, osel_idx, agg)]
    if not cands:
        return select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    if temperature <= 0:
        return max(cands, key=lambda x: x[1])[0]
    return _softmax_pick(cands, temperature, rng)


def _softmax_pick(cands, temperature, rng):
    """[(x, スコア)] から1つ引く（乱数1回）。スコアは[0,1]で差が小さいため、標準化(z-score)してから温度ソフトマックス
    （実証済みの「決定的最良」に近い＝最良中心＋たまに変化、を保つ。生スコア/温度だとほぼ一様になる）"""
    s = np.array([sc for _, sc in cands]); sd = s.std()
    z = (s - s.mean()) / sd if sd > 1e-9 else s * 0.0
    ws = np.exp((z - z.max()) / max(1e-6, temperature))
    tot = ws.sum(); r = rng.random() * tot; acc = 0.0
    for (order, _), w in zip(cands, ws):
        acc += float(w)
        if r <= acc:
            return order
    return cands[-1][0]


def learned_select_scores(party6, opp6, loader, n=3, rng=None):
    """学習選出の全候補 [(3体の並び（先頭＝リード）, スコア)]。スコア＝相手の選出の仮定に対する予測勝率の平均。
    モデルが無い・3体以下なら None（呼び出し側でヒューリスティックへ）。learned_select_party と同じ計算・同じ乱数の消費"""
    model = _load()
    if model is None or len(party6) <= n:
        return None
    rng = rng or random
    osel_idx, agg = _opp_assume(party6, opp6, loader, n, rng, model) or (None, None)
    return [([party6[i] for i in c], sc) for c, sc in _score_cands(party6, opp6, loader, n, rng, model, osel_idx, agg)] or None
