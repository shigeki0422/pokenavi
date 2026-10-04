"""パーティ診断（ローカル版・2026-10-02）。提案APIの /diagnose・/diag_battle・/improve の中身。
相手集団は _select_guide と同じ（guide_pool_m6.json）。選出率・条件ルール・苦手/得意は /guide の集計（貪欲8戦×3000党）のまま。
有利度（全体・順位・代表相手・改善案）は Rust guide_rows_mcts（同じ選出で対戦を両者 MCTS@SIMS）の勝率をそのまま使う
（貪欲の差は本番AIの差をほぼ予測しない。根拠 _local/ai_work/diag_validation_20261002.md）。
全体の有利度は _diag_ref.py が事前計算（diag_adv_m6.json・参照分布 diag_ref_m6.json）。無い党はサーバが貪欲の値を概算で返し、裏で同じ計算を回す。
並列は呼び出し側のプールを受け取る（サーバは _get_pool()、事前計算は自前の Pool）。
"""
import json
import math
from array import array
import os
from collections import Counter

import _select_guide as SG

_DIR = os.path.dirname(os.path.abspath(__file__))
REF_FILE = os.path.join(_DIR, os.environ.get("DIAG_REF", "diag_ref_m6.json"))
ADV_FILE = os.path.join(_DIR, os.environ.get("DIAG_ADV", "diag_adv_m6.json"))
SIMS = int(os.environ.get("DIAG_SIMS", "64"))
MC_NC = 20
ADV_OPPS, ADV_K, OPP_K = 200, 4, 16
N_OPPS, IMPROVE_OPPS, IMPROVE_K, PER_SLOT, D_MIN, Z_MIN, FIX_MIN_N = 9, 300, 4, 2, 0.03, 2.0, 30
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


def party_key(specs):
    return "\n".join(sorted(specs))


def is_stone(spec):
    return spec.split("@", 1)[1].split(":")[0].endswith(("ナイト", "ナイトX", "ナイトY", "ナイトZ", "ナイトＸ", "ナイトＹ", "ナイトＺ"))


def mrows_at(a):
    """(specs, opps, season, seed, k) → 相手ごとに (自分の選出, MCTS@SIMS の k 戦の勝率) か None"""
    specs, opps, season, seed, k = a
    import pokenavi_engine as E
    from simulator.learned_selection import _PATH
    return [(my, w) if my else None for my, w in E.guide_rows_mcts(list(specs), opps, season, k, seed, _PATH, SIMS)]


def mrows_at_i(a):
    return a[0], mrows_at(a[1])


def mchunk_jobs(specs, opps, season, k, nc=MC_NC):
    """相手 i::nc・シード 1+100003·i（パーティによらず同じ相手に同じシード＝党どうしを対にできる）"""
    return [(list(specs), opps[i::nc], season, 1 + 100_003 * i, k) for i in range(nc)]


def mean_se(xs):
    m = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / max(1, len(xs) - 1))
    return m, sd / math.sqrt(len(xs))


def run_jobs(imap, jobs, progress=None):
    """imap＝プールの imap_unordered。mrows_at を並列に回して jobs の順に返す。progress(済み, 全体)"""
    out = [None] * len(jobs)
    for n, (i, r) in enumerate(imap(mrows_at_i, list(enumerate(jobs))), 1):
        out[i] = r
        if progress:
            progress(n, len(jobs))
    return out


def mcts_adv(specs, imap, opps, season, k, progress=None):
    """全体の有利度＝相手ごとの勝率の平均（MCTS@SIMS をそのまま。MCTS@400 との差は党平均で約1pt＝較正しない）"""
    al = merge(run_jobs(imap, mchunk_jobs(specs, opps, season, k), progress), MC_NC, len(opps))
    m, se = mean_se([r[1] for r in al if r])
    return {"adv": round(m, 4), "se": round(se, 4), "n_opp": len(opps), "k": k, "sims": SIMS}


_LIVE = {}


def _load_live(path):
    """事前計算の途中でも読めるよう、更新されていたら読み直す（書く側は os.replace で置き換える）"""
    try:
        mt = os.path.getmtime(path)
    except OSError:
        return None
    c = _LIVE.get(path)
    if not c or c[0] != mt:
        try:
            c = (mt, json.load(open(path, encoding="utf-8")))
        except (OSError, ValueError):
            return c[1] if c else None
        _LIVE[path] = c
    return c[1]


def cached_adv(specs):
    d = _load_live(ADV_FILE)
    return (d or {}).get("adv", {}).get(party_key(specs))


def remeasure_job(a):
    """代表相手1党に MCTS@SIMS を OPP_K 戦"""
    specs, opp, season, oid = a
    import pokenavi_engine as E
    from simulator.learned_selection import _PATH
    my, w = E.guide_rows_mcts(list(specs), [opp], season, OPP_K, 7 + 7919 * oid, _PATH, SIMS)[0]
    return w if my else None


def remeasure_jobs(specs, pool, opps, season):
    """表示する相手だけ MCTS@SIMS×OPP_K 戦で測り直す（貪欲の相手別の値は本番AIと r≈0.5）。結果は apply_remeasure で入れる"""
    return [(list(specs), pool[o["id"]], season, o["id"]) for o in opps]


def apply_remeasure(opps, ws):
    for o, w in zip(opps, ws):
        o["adv"] = None if w is None else round(w, 3)
        o["k"] = OPP_K
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


def improve_cands(specs, cand_fn):
    """各枠を cand_fn(残り5体)（/complete と同じ補完の上位）の候補で入れ替え。同じ種は除き各枠 PER_SLOT 件"""
    cands = []
    for i in range(6):
        rest = specs[:i] + specs[i + 1:]
        got = [sp for sp in cand_fn(rest) if _name(sp) != _name(specs[i])]
        cands += [(i, sp) for sp in got[:PER_SLOT]]
    return cands


def improve(specs, cands, imap, opps, season, progress=None):
    """cands＝improve_cands の (枠, spec)。候補の党と元の党を同じ相手・同じシードで MCTS@SIMS×IMPROVE_K 戦し、相手ごとの差の平均と標準誤差で z。
    diff≥D_MIN かつ z≥Z_MIN だけを差の大きい順に返す。mega2＝残り5体にメガ石があるのにメガ石の候補（選出ではメガは1体だけ）"""
    specs = list(specs)
    parties = [specs] + [specs[:i] + [sp] + specs[i + 1:] for i, sp in cands]
    n = len(opps)
    jobs = [j for p in parties for j in mchunk_jobs(p, opps, season, IMPROVE_K)]
    parts = run_jobs(imap, jobs, progress)
    al = [merge(parts[k * MC_NC:(k + 1) * MC_NC], MC_NC, n) for k in range(len(parties))]
    base = al[0]
    onames = [{_name(x) for x in o} for o in opps]
    out = []
    for (i, sp), ca in zip(cands, al[1:]):
        idx = [j for j in range(n) if base[j] and ca[j]]
        d = [ca[j][1] - base[j][1] for j in idx]
        m, se = mean_se(d)
        z = m / se if se > 0 else 0.0
        if m < D_MIN or z < Z_MIN:
            continue
        by = {}
        for j, x in zip(idx, d):
            for s in onames[j]:
                by.setdefault(s, []).append(x)
        fixes = sorted(((s, sum(v) / len(v)) for s, v in by.items() if len(v) >= FIX_MIN_N), key=lambda x: -x[1])[:3]
        rest = specs[:i] + specs[i + 1:]
        out.append({"slot": i, "out": _name(specs[i]), "in": _name(sp), "spec": sp,
                    "adv": round(mean_se([r[1] for r in ca if r])[0], 3), "diff": round(m, 3), "se": round(se, 3), "z": round(z, 1),
                    "mega2": is_stone(sp) and any(is_stone(x) for x in rest),
                    "fixes": [{"opp": s, "diff": round(v, 3)} for s, v in fixes if v > 0]})
    out.sort(key=lambda x: -x["diff"])
    return {"base": round(mean_se([r[1] for r in base if r])[0], 3), "n_opp": n, "k": IMPROVE_K, "sims": SIMS,
            "n_cand": len(cands), "tried": [{"slot": i, "out": _name(specs[i]), "in": _name(sp)} for i, sp in cands], "cands": out}
