"""パーティ診断（ローカル版・2026-10-02）。提案APIの /diagnose・/diag_battle・/improve の中身。
相手集団・有利度の定義は _select_guide と同じ（guide_pool_m6.json・Rust guide_rows の貪欲勝率を CAL_A/CAL_B で較正）。
並列は呼び出し側の永続プールの map を受け取る（サーバは _get_pool()、参照分布の生成は自前の Pool）。
"""
import json
import math
from array import array
import os
from collections import Counter

import _select_guide as SG

REF_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.environ.get("DIAG_REF", "diag_ref_m6.json"))
OPP_GK = 64
N_OPPS, IMPROVE_OPPS, PER_SLOT, Z_MIN, MAX_CANDS, FIX_MIN_N = 9, 1000, 4, 2.0, 6, 30
PRED_TOP = 3


def _name(spec):
    return spec.split("@")[0]


def adv_of(g):
    return SG.CAL_A + SG.CAL_B * g


def rows_at(a):
    """(specs, opps, season, seed) → 相手ごとに (自分の選出, 貪欲勝率)。選べなかった相手は None（添字をそろえるため除かない）"""
    specs, opps, season, seed = a
    import pokenavi_engine as E
    from simulator.learned_selection import _PATH
    return [(my, g) if my else None for my, g in E.guide_rows(list(specs), opps, season, SG.GK, seed, _PATH)]


def chunk_jobs(specs, opps, season, nc):
    """サーバの guide() と同じ分け方・シード（相手 i::nc、シード 1+100003·i）"""
    return [(list(specs), opps[i::nc], season, 1 + 100_003 * i) for i in range(nc)]


def merge(parts, nc, n):
    """chunk_jobs の結果を相手の添字順に戻す"""
    out = [None] * n
    for i, part in enumerate(parts):
        for jj, r in enumerate(part):
            out[i + jj * nc] = r
    return out


def overall_adv(aligned):
    a = [adv_of(r[1]) for r in aligned if r]
    return sum(a) / len(a)


def g_array(aligned):
    return array("d", (r[1] if r else math.nan for r in aligned))


def load_ref(path=REF_FILE):
    try:
        return json.load(open(path, encoding="utf-8"))
    except FileNotFoundError:
        return None


def rank(adv, ref):
    if not ref:
        return None
    xs = ref["adv"]
    return {"pct": round((sum(x > adv for x in xs) + 1) / (len(xs) + 1), 3), "ref_n": len(xs)}


_NAMES = {}


def _pool_names(pool):
    k = id(pool)
    if k not in _NAMES:
        names = [[_name(x) for x in p] for p in pool]
        _NAMES[k] = (names, Counter(s for ns in names for s in set(ns)))
    return _NAMES[k]


def pick_opps(pool, gs, weak, n=N_OPPS):
    """苦手な種ごとにその種を含む代表的な相手を1つ、残りはよくある相手。代表度＝相手集団での種の出現数の和
    （既に選んだ相手と同じ種は半分ずつ割り引いて、似た党が並ばないようにする）"""
    names, freq = _pool_names(pool)
    chosen, used = [], Counter()

    def take(js, why, focus):
        js = [j for j in js if not math.isnan(gs[j]) and j not in chosen]
        if not js:
            return
        j = max(js, key=lambda j: sum(freq[s] * 0.5 ** used[s] for s in names[j]))
        chosen.append(j)
        used.update(names[j])
        out.append({"id": j, "names": names[j], "why": why, "focus": focus, "adv": round(adv_of(gs[j]), 3)})

    out = []
    for w in weak[:n // 2]:
        take([j for j, ns in enumerate(names) if w["opp"] in ns], "weak", w["opp"])
    while len(out) < n:
        k = len(out)
        take(range(len(pool)), "meta", None)
        if len(out) == k:
            break
    return out


def remeasure(specs, parties, opps, season, seed=7):
    """表示する相手だけ貪欲 OPP_GK 戦で測り直す（集計用の8戦では1党ごとの値は揺れが大きく、0/8＝37%が並ぶ）"""
    import pokenavi_engine as E
    from simulator.learned_selection import _PATH
    r = E.guide_rows(list(specs), parties, season, OPP_GK, seed, _PATH)
    for o, (my, g) in zip(opps, r):
        if my:
            o["adv"] = round(adv_of(g), 3)
    return opps


def _trim_predict(rec):
    for t in rec.get("turns", ()):
        for side in (t.get("predict") or {}).values():
            for ent in side.values():
                pool = ent.get("pool")
                if pool:
                    pool["top"] = pool["top"][:PRED_TOP]
                    pool["item"] = pool["item"][:PRED_TOP]
                ent["marginal"]["item"] = ent["marginal"]["item"][:PRED_TOP]
    return rec


def battle_job(a):
    """プールのワーカーで1戦（MCTS@400・型の読みつき）。my_sel=None なら自分も学習選出（温度0）、相手は常に学習選出。
    探索は Rust（mcts_3v3_record）・記録は Python で同じ乱数のまま再生。再生が食い違った戦だけ従来の Python 版で記録する"""
    specs, opp, season, seed, my_sel = a
    import feature1 as F1
    kw = dict(season=season, seed=seed, predict=True, sel1_idx=my_sel, sel1_temp=0.0)
    try:
        rec = F1.play_and_record_rust(list(specs), list(opp), **kw)
    except (F1.ReplayMismatch, ImportError, AttributeError):
        rec = F1.play_and_record(list(specs), list(opp), **kw)
    names = [_name(x) for x in specs]
    rec["my_sel"] = list(my_sel) if my_sel is not None else [names.index(n) for n in rec["selected1"]]
    rec["auto"] = my_sel is None
    return _trim_predict(rec)


def improve(specs, cand_fn, pmap, opps, season, nc):
    """各枠を cand_fn(残り5体) の候補で入れ替え、相手 opps に対する有利度を base と同じシードで比べる（相手ごとの差の平均と標準誤差で z）"""
    specs = list(specs)
    cands = []
    for i in range(6):
        rest = specs[:i] + specs[i + 1:]
        got = [sp for sp in cand_fn(rest) if _name(sp) != _name(specs[i])]
        cands += [(i, sp) for sp in got[:PER_SLOT]]
    parties = [specs] + [specs[:i] + [sp] + specs[i + 1:] for i, sp in cands]
    n = len(opps)
    parts = pmap(rows_at, [j for p in parties for j in chunk_jobs(p, opps, season, nc)])
    al = [merge(parts[k * nc:(k + 1) * nc], nc, n) for k in range(len(parties))]
    base = al[0]
    onames = [{_name(x) for x in o} for o in opps]
    out = []
    for (i, sp), ca in zip(cands, al[1:]):
        idx = [j for j in range(n) if base[j] and ca[j]]
        d = [adv_of(ca[j][1]) - adv_of(base[j][1]) for j in idx]
        m = sum(d) / len(d)
        sd = math.sqrt(sum((x - m) ** 2 for x in d) / max(1, len(d) - 1))
        z = m / (sd / math.sqrt(len(d))) if sd > 0 else 0.0
        if z < Z_MIN:
            continue
        by = {}
        for j, x in zip(idx, d):
            for s in onames[j]:
                by.setdefault(s, []).append(x)
        fixes = sorted(((s, sum(v) / len(v)) for s, v in by.items() if len(v) >= FIX_MIN_N), key=lambda x: -x[1])[:3]
        out.append({"slot": i, "out": _name(specs[i]), "in": _name(sp), "spec": sp,
                    "adv": round(overall_adv(ca), 3), "diff": round(m, 3), "z": round(z, 1),
                    "fixes": [{"opp": s, "diff": round(v, 3)} for s, v in fixes if v > 0]})
    out.sort(key=lambda x: -x["diff"])
    return {"base": round(overall_adv(base), 3), "n_opp": n, "n_cand": len(cands), "cands": out[:MAX_CANDS]}
