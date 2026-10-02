"""選出ガイド（_select_guide.py）の検証。提案キャッシュの党 NP 個 × 相手集団（guide_pool_m6.json）の先頭 NO 党。
  (a) 推奨選出の質: 推奨（学習選出・温度0）vs 簡易ルール（ai.select_party・温度0）を、同じ相手の選出（相手側の学習選出を温度 OPP_T で抽選）・
      同じシードで Rust MCTS@400 対戦（先後入れ替え、SEL_KEEP_ORDER=1）。選出が同じ対面は対戦しない（差0）
  (b) 有利度の候補と、推奨選出の大量対戦の勝率（K 戦）の相関: sel（学習選出のスコア）・sym（sel と 1−相手の最良スコアの平均）・
      val（価値ネットの対戦開始時評価。推奨 vs 相手の想定選出）・adv（_select_guide.rows の貪欲勝率を較正した値＝本番の有利度の1対面分）・
      greedy（貪欲AIで GK 戦。相手の選出を真値の対戦と共有するので相関は水増しされる＝参考。既定0で省略）
使い方: venv/bin/python _select_guide_eval.py OUT.json   env: NP(40) NO(10) K(16) KA(4) GK(0) SIMS(400) OPP_T(1.0) W(12) SEED(0)
"""
import json
import math
import os
import random
import sys
import time

os.environ.setdefault("POOL_SEASON", "M-6")
os.environ.setdefault("USAGE_SEASON", "M-6")
os.environ.setdefault("ENGINE", "rust")
os.environ["SEL_KEEP_ORDER"] = "1"
import multiprocessing as mp

import numpy as np

SEASON = "M-6"


def _play(args):
    key, pa, sa, pb, sb, seed, sims, a_first = args
    import pokenavi_engine as E
    if sims == 0:
        r = E.greedy_3v3(pa, sa, pb, sb, seed, SEASON) if a_first else E.greedy_3v3(pb, sb, pa, sa, seed, SEASON)
    else:
        r = E.mcts_3v3(pa, sa, pb, sb, seed, sims, SEASON) if a_first else E.mcts_3v3(pb, sb, pa, sa, seed, sims, SEASON)
    win = (r == 1) if a_first else (r == 2)
    lose = (r == 2) if a_first else (r == 1)
    return key, 1 if win else -1 if lose else 0


def _wr(rs):
    w = sum(1 for x in rs if x > 0); l = sum(1 for x in rs if x < 0)
    return (w + 0.5 * (len(rs) - w - l)) / len(rs) if rs else 0.5


def main():
    out = sys.argv[1]
    NP, K, KA, GK = (int(os.environ.get(k, d)) for k, d in (("NP", "40"), ("K", "16"), ("KA", "4"), ("GK", "0")))
    SIMS, OPP_T, W = int(os.environ.get("SIMS", "400")), float(os.environ.get("OPP_T", "1.0")), int(os.environ.get("W", "12"))
    rng = random.Random(int(os.environ.get("SEED", "0")))
    import feature1 as F
    F._ensure_loaded(SEASON, 8)
    L, net = F._W["loader"], F._W["net"]
    import _select_guide as G
    from simulator.ai import select_party
    from simulator.learned_selection import learned_select_party, learned_select_scores
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    opps = [{"label": str(i), "party": p, "built": [build_from_spec(parse_pokemon_spec(x), L, season=SEASON, randomize=False) for x in p]}
            for i, p in enumerate(G.load_pool()[:int(os.environ.get("NO", "10"))])]
    cache = json.load(open("suggest_cache.json", encoding="utf-8"))
    allp = sorted({tuple(r["specs"]) for v in cache.values() for r in v["results"]})
    parties = rng.sample(allp, NP)
    build = lambda specs: [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    idx = lambda P, sel: [next(i for i, p in enumerate(P) if p is m) for m in sel]
    pairs, jobs = [], []
    t0 = time.time()
    for pi, specs in enumerate(parties):
        A = build(list(specs))
        gd = G.rows(list(specs), [o["party"] for o in opps], SEASON)
        for oi, o in enumerate(opps):
            O = o["built"]
            sc = learned_select_scores(A, O, L, n=3, rng=random.Random(1000 + oi))
            rec, s_me = max(sc, key=lambda x: x[1])
            osc = learned_select_scores(O, A, L, n=3, rng=random.Random(2000 + oi))
            opred, s_op = max(osc, key=lambda x: x[1])
            heur = select_party(A, O, L, n=3, temperature=0.0, rng=random.Random(3000 + oi))
            s1 = BattleSide(rec, source6=A); s2 = BattleSide(opred, source6=O)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            val = float(net.evaluate(encode_state(s1, s2, BattleField()), [0])[1])
            ri, hi = idx(A, rec), idx(A, heur)
            kp = len(pairs)
            pairs.append({"p": pi, "o": oi, "rec": ri, "heur": hi, "opred": idx(O, opred),
                          "sel": s_me, "sym": 0.5 * (s_me + 1 - s_op), "val": val, "adv": G.CAL_A + G.CAL_B * gd[oi][2]})
            orng = random.Random(rng.random())
            osamp = [idx(O, learned_select_party(O, A, L, n=3, temperature=OPP_T, rng=orng)) for _ in range(max(K, KA, GK))]
            pa, pb = list(specs), o["party"]
            for g in range(K):
                jobs.append((("t", kp, g), pa, ri, pb, osamp[g], 7_000_000 + kp * 101 + g, SIMS, g % 2 == 0))
            for g in range(GK):
                jobs.append((("g", kp, g), pa, ri, pb, osamp[g], 8_000_000 + kp * 101 + g, 0, g % 2 == 0))
            if hi != ri:
                for g in range(KA):
                    jobs.append((("h", kp, g), pa, hi, pb, osamp[g], 7_000_000 + kp * 101 + g, SIMS, g % 2 == 0))
    print(f"選出 {len(pairs)}対面 {time.time() - t0:.1f}s / 対戦 {len(jobs)}", flush=True)
    res = {}
    with mp.get_context("fork").Pool(W) as pool:
        for n_done, (key, r) in enumerate(pool.imap_unordered(_play, jobs, chunksize=4), 1):
            res[key] = r
            if n_done % 2000 == 0:
                print(f"  {n_done}/{len(jobs)} {time.time() - t0:.0f}s", flush=True)
    col = lambda t, kp, n: [res[(t, kp, g)] for g in range(n) if (t, kp, g) in res]
    for kp, d in enumerate(pairs):
        d["truth_k"] = col("t", kp, K)
        d["truth"] = _wr(d["truth_k"])
        d["greedy"] = _wr(col("g", kp, GK)) if GK else None
        d["heur_k"] = col("h", kp, KA) if d["heur"] != d["rec"] else None
    json.dump({"opps": [o["label"] for o in opps], "parties": [list(p) for p in parties], "pairs": pairs,
               "K": K, "KA": KA, "GK": GK, "SIMS": SIMS, "OPP_T": OPP_T}, open(out, "w"), ensure_ascii=False)
    report(out)


def report(path):
    d = json.load(open(path))
    P = d["pairs"]; KA = d["KA"]
    diff = [x for x in P if x["heur_k"] is not None]
    a = [r for x in diff for r in x["truth_k"][:KA]]; b = [r for x in diff for r in x["heur_k"]]
    wa, wb = _wr(a), _wr(b)
    dlt = [(_wr(x["truth_k"][:KA]) - _wr(x["heur_k"])) for x in diff]
    se = float(np.std(dlt, ddof=1) / math.sqrt(len(dlt))) if len(dlt) > 1 else 0
    print(f"(a) 選出が違う対面 {len(diff)}/{len(P)}（{len(diff) / len(P) * 100:.0f}%）: 推奨 {wa * 100:.1f}% vs 簡易ルール {wb * 100:.1f}%"
          f"  差 {(wa - wb) * 100:+.1f}pt（対面単位SE {se * 100:.1f}pt, z={(wa - wb) / se if se else 0:+.2f}）"
          f" → 全対面換算 {(wa - wb) * len(diff) / len(P) * 100:+.1f}pt")
    y = np.array([x["truth"] for x in P])
    k = len(P[0]["truth_k"])
    noise = float(np.mean(y * (1 - y)) / k)
    rel = max(1e-9, 1 - noise / float(np.var(y)))
    print(f"(b) 真値＝推奨選出の MCTS@{d['SIMS']} {k}戦の勝率: 平均{y.mean() * 100:.1f}% SD{y.std() * 100:.1f}pt 信頼性{rel:.2f}")
    for f in ("sel", "sym", "val", "adv", "greedy"):
        if P[0].get(f) is None:
            continue
        x = np.array([p[f] for p in P])
        if f == "adv":
            b = np.polyfit(x, y, 1)
            print(f"   adv の較正: 真値 ≈ {b[1]:.3f} + {b[0]:.3f}×adv（1:1 なら 0 + 1）、平均 adv {x.mean() * 100:.1f}% vs 真値 {y.mean() * 100:.1f}%")
        r = float(np.corrcoef(x, y)[0, 1])
        print(f"   {f:7s} r={r:+.3f}（測定誤差補正 {r / math.sqrt(rel):+.3f}） 範囲 {x.min():.3f}〜{x.max():.3f}")


if __name__ == "__main__":
    if sys.argv[1] == "report":
        report(sys.argv[2])
    else:
        main()
