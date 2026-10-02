"""パーティ提案の選出ガイド（相手集団の統計版・2026-10-02）。
相手＝M-6 の使用率＋同居率の生成器で引いた NP 党（guide_pool_m6.json、`_guide_opps.py sample` が作る）。相手ごとに
自分の学習選出（温度0、先頭＝リード）と、それ vs 相手の選出（相手側の学習選出の値から温度1で抽選）を Rust 貪欲AIで GK 戦（先後交互）し、
貪欲の勝率 g を MCTS@400 の勝率へ線形較正（CAL_A + CAL_B·g）した値を有利度とする（Rust `guide_rows`）。
集計（summarize）: 全体の有利度・各ポケモンの選出率/先発率・多い3体・相手にいる種ごとの選出の変化（条件ルール）と有利度の差（苦手/得意）。
少数の相手では1対面ごとの選出・勝率の揺れがそのまま出るので、相手を数千党にして統計にする。根拠（2集団 s4/s5 各3000党・提案40党）:
  条件ルール（z≥6・差≥25pt）はもう一方の集団でも有意・同じ向きが 97%、苦手/得意（z≥6・差≥2.5pt）は 98%、最多の3体は 40/40 一致、
  全体の有利度の差は最大0.8pt。1000党だとルールが 1/3 しか出ない。
較正は旧版（よくある構築10個×提案40党の800対面、真値＝推奨3体の MCTS@400 16戦）の当てはめ。
"""
import json
import math
import os
from collections import defaultdict

POOL_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.environ.get("GUIDE_POOL", "guide_pool_m6.json"))
GK = int(os.environ.get("GUIDE_GK", "8"))
CAL_A, CAL_B = 0.371, 0.409
Z_MIN, D_RULE, D_FOE, MIN_N = 6.0, 0.25, 0.025, 30


def load_pool(path=POOL_FILE):
    return [o["party"] for o in json.load(open(path, encoding="utf-8"))]


def rows(specs, opps, season, k=GK, seed=1):
    """相手ごとに (自分の選出の添字の並び, 相手の種名, 貪欲の勝率)。選べなかった相手は除く"""
    import pokenavi_engine as E
    from simulator.learned_selection import _PATH
    r = E.guide_rows(list(specs), opps, season, k, seed, _PATH)
    return [(my, [x.split("@")[0] for x in o], g) for (my, g), o in zip(r, opps) if my]


def summarize(names, rows, min_n=MIN_N, z_min=Z_MIN, d_rule=D_RULE, d_foe=D_FOE):
    N = len(rows)
    adv = [CAL_A + CAL_B * g for _, _, g in rows]
    mean = sum(adv) / N
    sd = math.sqrt(sum((a - mean) ** 2 for a in adv) / max(1, N - 1))
    pick = [{names[i] for i in my} for my, _, _ in rows]
    members = [{"name": n, "sel": round(sum(n in p for p in pick) / N, 3),
                "lead": round(sum(names[my[0]] == n for my, _, _ in rows) / N, 3)} for n in names]
    tri = defaultdict(list)
    for (my, _, _), a in zip(rows, adv):
        tri[tuple(sorted(names[i] for i in my))].append(a)
    trios = [{"my": list(t), "share": round(len(v) / N, 3), "adv": round(sum(v) / len(v), 3)}
             for t, v in sorted(tri.items(), key=lambda x: -len(x[1]))[:3]]
    present = defaultdict(list)
    for r, (_, on, _) in enumerate(rows):
        for s in set(on):
            present[s].append(r)
    tot_m = {m: sum(m in p for p in pick) for m in names}
    tot_a = sum(adv)
    rules, foes = {}, []
    for s, idx in present.items():
        n1 = len(idx)
        if n1 < min_n or N - n1 < min_n:
            continue
        for m in names:
            c1 = sum(m in pick[r] for r in idx)
            p1, p0, pp = c1 / n1, (tot_m[m] - c1) / (N - n1), tot_m[m] / N
            z = abs(p1 - p0) / math.sqrt(max(1e-9, pp * (1 - pp) * (1 / n1 + 1 / (N - n1))))
            if abs(p1 - p0) >= d_rule and z >= z_min:
                rules.setdefault(s, {"opp": s, "share": round(n1 / N, 3), "add": [], "drop": []})[
                    "add" if p1 > p0 else "drop"].append({"mon": m, "with": round(p1, 3), "without": round(p0, 3)})
        s1 = sum(adv[r] for r in idx)
        m1, m0 = s1 / n1, (tot_a - s1) / (N - n1)
        se = sd * math.sqrt(1 / n1 + 1 / (N - n1))
        if se > 0 and abs(m1 - m0) >= d_foe and abs(m1 - m0) / se >= z_min:
            foes.append({"opp": s, "share": round(n1 / N, 3), "adv": round(m1, 3), "diff": round(m1 - m0, 3)})
    gap = lambda r: max(abs(x["with"] - x["without"]) for x in r["add"] + r["drop"])
    rules = sorted(rules.values(), key=lambda r: -gap(r) * r["share"] ** 0.5)
    foes.sort(key=lambda x: x["diff"])
    return {"n": N, "adv": round(mean, 3), "members": members, "trios": trios, "rules": rules[:6],
            "weak": [x for x in foes if x["diff"] < 0][:4], "strong": [x for x in foes[::-1] if x["diff"] > 0][:3]}


def guide(specs, opps, season, k=GK, seed=1):
    return summarize([x.split("@")[0] for x in specs], rows(specs, opps, season, k, seed))
