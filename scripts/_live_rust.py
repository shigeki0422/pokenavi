"""ライブ提案経路（/suggest・/complete のスコアリング）の Rust 経路グルー。

`ENGINE=rust` かつ `pokenavi_engine` が有効なときだけ使う。無効なら None を返し、
呼び出し側（_ensemble_surrogate.EnsembleScorer）は従来の純Python経路をそのまま通る。

**ビット一致の設計**: Rust は「集約の手前の中間量」だけを返す。
  - パネル各面の encode_state(905)  → net forward と statistics.mean は Python(numpy) がやる
  - 6x6 の _bestdmg 行列（int）      → matchup_feats の集約は Python がやる
丸め順が絡む演算（BLAS gemv・statistics.mean の厳密平均）を Python 側に残すため、
Rust とPythonで丸め順が食い違う余地が原理的に無い。
"""
import os
import statistics

import numpy as np

import engine_dispatch as _ED

# シーズン固定はM-6運用で誤採点になる（M-6のパーティをM-3データで計算し、
# Python経路と平均scoreが0.104ずれていた）。POOL_SEASON連動にする。既定M-3＝従来と同一。
SEASON = os.environ.get("POOL_SEASON", "M-3")

# ダメージ計算がグローバル random を消費する技（Python側が非決定的になる）。
# 該当する構築は Rust に渡さず Python 経路で採点する（＝従来どおりの挙動を保つ）。
RNG_MOVES = ("きまぐレーザー",)

# 計測用（パリティゲートが「本当にRust経路を通ったか」を検証するために使う）
STATS = {"rust": 0, "needs_python": 0}
ERRORS = []


class NeedsPython(Exception):
    """この候補は Rust では扱えない（Python 経路で採点する。Rustは無効化しない）"""


def needs_python(specs):
    return any(mv in s for s in specs for mv in RNG_MOVES)

# Rust 版が実装していない env（有効なら Python 経路へ）
_GUARD = [
    ("LEARNED_SELECTION", {None, "0"}),
    ("SELECT_MODE", {None}),
    ("MEGA_PENALTY", {None, "50", "50.0"}),
    ("MAX_MEGA", {None}),
    ("MIN_MEGA", {None}),
]


def unsupported():
    return [f"{k}={os.environ.get(k)}" for k, ok in _GUARD if os.environ.get(k) not in ok]


def setup(panel_specs):
    """パネルを Rust 側に構築。使えるなら module を、使えないなら None を返す。"""
    bad = unsupported()
    if bad:
        _ED._warn("cfg:live", f"live: 未対応コンフィグ [{', '.join(bad)}]")
        return None
    m = _ED.rust()
    if m is None or not hasattr(m, "live_setup"):
        if m is not None:
            _ED._warn("live:old", "pokenavi_engine に live_setup が無い（旧ビルド）")
        return None
    if any(needs_python(sp) for sp in panel_specs):
        _ED._warn("live:panel_rng", "パネルに乱数消費技が含まれる → Python経路")
        return None
    try:
        m.live_setup([list(sp) for sp in panel_specs], SEASON)
    except BaseException as e:
        _ED._warn("live:setup", f"live_setup 失敗: {e}")
        return None
    return m


def _matchup_feats_from(spd_a, hp_a, spd_b, hp_b, dAB, dBA):
    """_matchup_surrogate.matchup_feats と同じ12特徴を、事前計算済み行列から組む。
    元関数とは独立実装（パリティゲートで突き合わせるため意図的にコードを共有しない）。"""
    nA = len(hp_a)
    nB = len(hp_b)
    offB = [max(dAB[i][j] for i in range(nA)) / hp_b[j] for j in range(nB)]
    offA = [max(dBA[j][i] for j in range(nB)) / hp_a[i] for i in range(nA)]
    a_ohko = sum(1 for x in offB if x >= 1.0) / nB
    b_ohko = sum(1 for x in offA if x >= 1.0) / nA
    a_2hko = sum(1 for x in offB if x >= 0.5) / nB
    b_2hko = sum(1 for x in offA if x >= 0.5) / nA
    a_moff = statistics.mean(min(x, 1.5) for x in offB)
    b_moff = statistics.mean(min(x, 1.5) for x in offA)
    a_rev = 0
    for j in range(nB):
        if any(spd_a[i] > spd_b[j] and dAB[i][j] >= hp_b[j] for i in range(nA)):
            a_rev += 1
    a_rev /= nB
    b_rev = 0
    for i in range(nA):
        if any(spd_b[j] > spd_a[i] and dBA[j][i] >= hp_a[i] for j in range(nB)):
            b_rev += 1
    b_rev /= nA
    a_faster = statistics.mean(1.0 if max(spd_a) > spd_b[j] else 0.0 for j in range(nB))
    spd_adv = (max(spd_a) - max(spd_b)) / 200.0
    return [a_ohko, b_ohko, a_2hko, b_2hko, a_moff, b_moff, a_faster, a_rev, b_rev, spd_adv,
            a_ohko - b_ohko, b_2hko - a_2hko]


def feats(m, specs, net, panel_spd, panel_hp):
    """ネットt0パネル特徴(1) + リッチ特徴(12) を返す。construction特徴はPython側で足す。"""
    if needs_python(specs):
        STATS["needs_python"] += 1
        raise NeedsPython(specs)
    sb, mb, spd_a, hp_a, npanel, dim, na, nb = m.live_feats(list(specs))
    X = np.frombuffer(sb, dtype="<f8").reshape(npanel, dim)
    ns = statistics.mean(net.evaluate(X[i], [0])[1] for i in range(npanel))
    D = np.frombuffer(mb, dtype="<i8").reshape(npanel, 2, na * nb).tolist()
    fs = []
    for pi in range(npanel):
        dab = [D[pi][0][i * nb:(i + 1) * nb] for i in range(na)]
        dba = [D[pi][1][j * na:(j + 1) * na] for j in range(nb)]
        fs.append(_matchup_feats_from(spd_a, hp_a, panel_spd[pi], panel_hp[pi], dab, dba))
    rich = [statistics.mean(c) for c in zip(*fs)]
    STATS["rust"] += 1
    return [ns] + list(rich)
