"""相性ベースの規則的な選出（SELECT_MODE=matchup）。ニューラル選出のベースライン。
考え方: 相手6体のうちどの3体が来ても穴が無い3体を選ぶ。4項目の重み付き和を、相手が来うる3体（メガ1体ルール）ごとに計算し、
平均と最悪の混合が最大の3体を選ぶ。先頭は相手6体への1v1の勝ち数（同数は攻めの通り）で決める。
- 攻め off: 相手の各ポケモンに、自分の3体の技で通る最大の相性（抜群1・等倍0.5・半減0.25・無効0）
- 守り dfp: 相手が持っていそうな攻撃技のタイプ（型プールの型の重み＝そのタイプの攻撃技を持つ確率）ごとに、
            自分の3体のうち抜群を取られる数が2以上なら (数−1)×確率 を減点
- 1v1 mu: 自分の各ポケモン×相手の各ポケモンの1v1判定（Rust の1v1エンジン analysis、相手は型プールの最多の型）で勝てるか
- 負荷分散 load: 相手の各ポケモンに勝てる自分のポケモンの数（2体で満点）
相手の技・持ち物は真値を読まない（種族→型プール。見せ合いで分かる情報だけ）。
重みは env SELECT_MU_W="off,dfp,mu,load,alpha"（alpha＝平均の割合、残りが最悪）で変えられる。
"""
import os
from itertools import combinations
from typing import Dict, List, Optional

_DEF_W = (1.0, 1.0, 1.0, 1.0, 0.5)
_MU_CACHE: Dict[tuple, float] = {}


def _weights():
    s = os.environ.get("SELECT_MU_W")
    if not s:
        return _DEF_W
    v = [float(x) for x in s.split(",")]
    return tuple(v + list(_DEF_W[len(v):]))


def _is_mega(p) -> bool:
    return getattr(p, "mega_data", None) is not None


def _types(p):
    md = getattr(p, "mega_data", None)
    if md is not None and not p.mega_evolved:
        return md.type1, md.type2          # メガ石持ちは場に出ればメガ進化する
    return p.type1, p.type2


def spec_of(p) -> str:
    ev = getattr(p, "evs", {}) or {}
    moves = "|".join(m.name_jp for m in p.moves if m)
    return (f"{p.name}@{p.item or ''}:{p.nature}:{moves}:"
            + "/".join(str(ev.get(k, 0)) for k in "HABCDS") + f":{p.ability}")


def _pool_build(name):
    from .belief import pool_builds_by_species
    arr = pool_builds_by_species().get(name) or []
    return max(arr, key=lambda b: b["weight"]) if arr else None


def opp_move_type_probs(name, loader) -> Dict[str, float]:
    """相手の種族が持っていそうな攻撃技のタイプ → そのタイプの攻撃技を1つ以上持つ確率（型プールの型の重みで）。
    型プールに無い種は使用率（技の採用率）から"""
    from .belief import pool_builds_by_species
    arr = pool_builds_by_species().get(name) or []
    out: Dict[str, float] = {}
    if arr:
        tot = sum(b["weight"] for b in arr) or 1.0
        for b in arr:
            ts = set()
            for mn in b["moves"]:
                md = loader.get_move(mn)
                if md is not None and md.category != "status" and (md.power or 0) > 0:
                    ts.add(md.type)
            for t in ts:
                out[t] = out.get(t, 0.0) + b["weight"] / tot
        return out
    tpl = loader.get_pokemon_template(name, os.environ.get("POOL_SEASON", "M-6"))
    for mn, r in (getattr(tpl, "top_moves", None) or []):
        md = loader.get_move(mn)
        if md is not None and md.category != "status" and (md.power or 0) > 0:
            out[md.type] = max(out.get(md.type, 0.0), min(1.0, r / 100.0))
    return out


def _opp_spec(o) -> Optional[str]:
    b = _pool_build(o.name)
    if b is None:
        return None
    return (f"{o.name}@{b['item']}:{b['nature']}:{'|'.join(b['moves'])}:"
            + "/".join(str(x) for x in b["ev"]) + f":{b.get('ability', '')}")


def v1(p, o, season="M-6") -> float:
    """自分 p と相手 o の1v1（1=勝ち・0.5=相打ち扱い・0=負け）。相手は型プールの最多の型"""
    import json
    sa, sb = spec_of(p), _opp_spec(o)
    if sb is None:
        return 0.5
    key = (sa, sb)
    if key not in _MU_CACHE:
        try:
            import pokenavi_engine as E
            v = json.loads(E.mu_analyze(sa, sb, season))["verdict"]
            _MU_CACHE[key] = 1.0 if v.get("win") else (0.5 if v.get("score", -1) == 0 else 0.0)
        except Exception:
            _MU_CACHE[key] = 0.5              # 判定できない組（エンジン無し等）は中立
    return _MU_CACHE[key]


def tables(party6, opp6, loader):
    """選出の評価に使う表（自分6×相手6）。精度集計・重みの調整からも再利用する"""
    from .data import get_type_effectiveness
    off = [[0.0] * len(opp6) for _ in party6]
    for i, p in enumerate(party6):
        for j, o in enumerate(opp6):
            t1, t2 = o.type1, o.type2           # 相手のタイプは見せ合いで分かる素のタイプ
            best = 0.0
            for m in p.moves:
                if m and m.category != "status" and (m.power or 0) > 0:
                    best = max(best, get_type_effectiveness(m.type, t1, t2))
            off[i][j] = min(best, 2.0) / 2.0
    tp = [opp_move_type_probs(o.name, loader) for o in opp6]
    weak = [{t: get_type_effectiveness(t, *_types(p)) >= 2.0 for d in tp for t in d} for p in party6]
    mu = [[v1(p, o) for o in opp6] for p in party6]
    # 相手がメガ石を持っているかは見せ合いでは分からないので、型プールの最多の型の持ち物で見る（真値を読まない）
    def _opp_mega(o):
        b = _pool_build(o.name)
        return bool(b) and b["item"].rstrip("XYZＸＹＺ").endswith("ナイト")
    return {"off": off, "tp": tp, "weak": weak, "mu": mu,
            "mega_me": [_is_mega(p) for p in party6], "mega_opp": [_opp_mega(o) for o in opp6]}


def _trios(flags):
    allc = list(combinations(range(len(flags)), 3))
    if not any(flags):
        return allc
    one = [c for c in allc if sum(flags[i] for i in c) == 1]
    # メガ石持ちが5体以上で「ちょうど1体」を作れないパーティは、メガ数が最少の組で代える
    return one or [c for c in allc if sum(flags[i] for i in c) == min(sum(flags[i] for i in x) for x in allc)]


def trio_score(T, S, O, w=None) -> float:
    """自分の3体 S（添字）の、相手の3体 O に対する評価"""
    a, b, c, d, _ = w or _weights()
    off = sum(max(T["off"][i][j] for i in S) for j in O) / len(O)
    dfp = 0.0
    for j in O:
        for t, p in T["tp"][j].items():
            k = sum(1 for i in S if T["weak"][i].get(t))
            if k >= 2:
                dfp += (k - 1) * p
    dfp /= len(O)
    mu = sum(max(T["mu"][i][j] for i in S) for j in O) / len(O)
    load = sum(min(sum(1 for i in S if T["mu"][i][j] >= 1.0), 2) / 2.0 for j in O) / len(O)
    return a * off - b * dfp + c * mu + d * load


def choose(T, w=None):
    """(3体の添字の並び＝先頭が最初) を返す"""
    w = w or _weights()
    alpha = w[4]
    opp_trios = _trios(T["mega_opp"])
    best, bs = None, -1e18
    for S in _trios(T["mega_me"]):
        v = [trio_score(T, S, O, w) for O in opp_trios]
        s = alpha * sum(v) / len(v) + (1 - alpha) * min(v)
        if s > bs + 1e-12:
            bs, best = s, S
    lead = max(best, key=lambda i: (sum(T["mu"][i]), sum(T["off"][i]), -best.index(i)))
    return [lead] + [i for i in best if i != lead]


def matchup_select_party(party6: List, opp6: List, loader, n: int = 3, temperature: float = 0.0, rng=None) -> List:
    if len(party6) <= n:
        return list(party6)
    T = tables(party6, opp6, loader)
    return [party6[i] for i in choose(T)]
