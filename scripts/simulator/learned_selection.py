"""学習選出（MCTS教師で学習したValMLP選出評価器）。本番記録系の select_party の drop-in 置換。
A/B 実MCTS@1600・2000戦で 55.9%(z=+5.23, p<0.0001) とヒューリスティック選出を有意に上回ることを確認済み。
モデル: simulator/selector_m2.json（_selector3.py 由来）。
有効化: 環境変数 LEARNED_SELECTION=1 を明示した時のみ（既定OFF＝heuristicフォールバック）。
フル検証が済むまで本番(auto_update)に出さないため opt-in にしている。検証後に auto_update.sh で =1 を設定して本番投入。
"""
import os
import json
import math
import random
from itertools import combinations

import numpy as np

_MODEL = None
_LOADED = False
_PATH = os.path.join(os.path.dirname(__file__), "selector_m2.json")


def _load():
    global _MODEL, _LOADED
    if _LOADED:
        return _MODEL
    _LOADED = True
    if os.environ.get("LEARNED_SELECTION", "0") != "1" or not os.path.exists(_PATH):
        _MODEL = None   # 既定OFF。検証完了後 LEARNED_SELECTION=1 で本番有効化
        return None
    with open(_PATH) as f:
        d = json.load(f)
    _MODEL = {"W1": np.asarray(d["W1"], float), "b1": np.asarray(d["b1"], float),
              "W2": np.asarray(d["W2"], float), "b2": float(d["b2"])}
    return _MODEL


def _predict(model, X):
    X = np.asarray(X, float)
    H = np.tanh(X @ model["W1"].T + model["b1"])
    return 1.0 / (1.0 + np.exp(-(H @ model["W2"] + model["b2"])))


def learned_select_party(party6, opp6, loader, n=3, temperature=0.0, rng=None):
    """学習選出。temperature=0 で最良の3体(リード順)、>0 で softmax(score/temp) サンプリング。
    select_party と同一シグネチャ。モデル未ロード/3体以下は heuristic にフォールバック。
    SELECT_MODE=mcts のときはMCTS選出(探索ベース・ヒューリスティック比+6〜9pt)へ委譲する。"""
    from .ai import select_party
    if os.environ.get("SELECT_MODE") == "mcts":
        from .mcts_selection import mcts_select_party
        return mcts_select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    model = _load()
    if model is None or len(party6) <= n:
        return select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    from .battle import BattleSide, BattleField
    from .features import encode_state
    rng = rng or random

    # 相手選出のサンプル（候補スコア推定用）: heuristic best + 温度ありサンプル2つ
    opp_sels = [select_party(opp6, party6, loader, n=min(n, len(opp6)), temperature=0.0, rng=rng)]
    for _ in range(2):
        opp_sels.append(select_party(opp6, party6, loader, n=min(n, len(opp6)), temperature=1.0, rng=rng))

    _max_mega = int(os.environ.get("MAX_MEGA", "2"))   # メガ石2枚保持は合法(進化は1戦1体)。2メガ選出は基本的に強い
    cands = []  # (ordered_selection, score)
    for combo in combinations(range(len(party6)), n):
        sub = [party6[i] for i in combo]
        if sum(1 for p in sub if getattr(p, "mega_data", None) is not None) > _max_mega:
            continue
        for li in range(n):
            order = [sub[li]] + [sub[j] for j in range(n) if j != li]
            xs = []
            for osel in opp_sels:
                s1 = BattleSide(order); s2 = BattleSide(list(osel)); s1.field_idx = 0; s2.field_idx = 1
                xs.append(encode_state(s1, s2, BattleField()))
            cands.append((order, float(np.mean(_predict(model, xs)))))
    if not cands:
        return select_party(party6, opp6, loader, n=n, temperature=temperature, rng=rng)
    if temperature <= 0:
        return max(cands, key=lambda x: x[1])[0]
    # スコアは[0,1]で差が小さいため、標準化(z-score)してから温度ソフトマックス
    # （実証済みの「決定的最良」に近い＝最良中心＋たまに変化、を保つ。生スコア/温度だとほぼ一様になる）
    s = np.array([sc for _, sc in cands]); sd = s.std()
    z = (s - s.mean()) / sd if sd > 1e-9 else s * 0.0
    ws = np.exp((z - z.max()) / max(1e-6, temperature))
    tot = ws.sum(); r = rng.random() * tot; acc = 0.0
    for (order, _), w in zip(cands, ws):
        acc += float(w)
        if r <= acc:
            return order
    return cands[-1][0]
