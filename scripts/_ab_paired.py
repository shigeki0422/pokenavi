"""2ネットの対ペア A/B（本番経路 Rust IS-MCTS・pokenavi_engine.mcts_3v3_ab）。
同じ (パーティA, パーティB, 選出, シード) を先後入れ替えて2戦する（ネットAがAを持つ回とBを持つ回）＝パーティと乱数の有利不利が相殺される。
選出は学習選出（温度 SEL_TEMP、既定0.6＝本番の事前計算と同じ）。SELECT=random で6体から3体を無作為（従来の A/B と同じ）。
パーティは評価用の集合（訓練コーパスに使っていないもの）: 提案キャッシュ上位軸・eval_evo・ab_pool_new_v1pool。
env: NET_A NET_B(既定 az_net_np.json) PAIRS(1000) SIMS(400) W(10) AB_SEED(777) SELECT(learned) SEL_TEMP(0.6) DUMP
"""
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")
import multiprocessing as mp

SEASON = "M-6"
NET_A = os.environ["NET_A"]
NET_B = os.environ.get("NET_B", os.path.join(HERE, "az_net_np.json"))
PAIRS = int(os.environ.get("PAIRS", "1000"))
SIMS = int(os.environ.get("SIMS", "400"))
W = int(os.environ.get("W", "10"))
AB_SEED = int(os.environ.get("AB_SEED", "777"))
SELECT = os.environ.get("SELECT", "learned")
SEL_TEMP = float(os.environ.get("SEL_TEMP", "0.6"))
AW = os.path.join(os.path.dirname(HERE), "_local", "ai_work")


def pools():
    import _m6_pool
    P = [list(p) for p in _m6_pool.load_parties()]
    for f in ("eval_evo_M-6.json", "ab_pool_new_v1pool.json"):
        P += [list(e["party"]) for e in json.load(open(os.path.join(AW, f))) if len(e["party"]) == 6]
    seen, out = set(), []
    for p in P:
        k = tuple(sorted(p))
        if k not in seen:
            seen.add(k); out.append(p)
    return out


_L = {}


def _sel(pa, pb, seed):
    rng = random.Random(seed)
    if SELECT == "random":
        return rng.sample(range(6), 3), rng.sample(range(6), 3)
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    if "L" not in _L:
        from simulator.simulate import get_loader
        _L["L"] = get_loader()
    L = _L["L"]
    random.seed(seed)
    P1 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    P2 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    s1 = learned_select_party(P1, P2, L, n=3, temperature=SEL_TEMP)
    s2 = learned_select_party(P2, P1, L, n=3, temperature=SEL_TEMP)
    return ([next(i for i, q in enumerate(P1) if q is p) for p in s1],
            [next(i for i, q in enumerate(P2) if q is p) for p in s2])


def play(job):
    import pokenavi_engine as E
    pa, pb, seed = job
    sa, sb = _sel(pa, pb, seed)
    r1 = E.mcts_3v3_ab(pa, sa, pb, sb, seed, SIMS, NET_A, NET_B, SEASON, SIMS)
    r2 = E.mcts_3v3_ab(pa, sa, pb, sb, seed, SIMS, NET_B, NET_A, SEASON, SIMS)
    a1 = 0 if r1 == 0 else (1 if r1 == 1 else -1)
    a2 = 0 if r2 == 0 else (1 if r2 == 2 else -1)
    return a1, a2


def main():
    P = pools()
    rng = random.Random(AB_SEED)
    jobs = []
    for i in range(PAIRS):
        a, b = rng.sample(range(len(P)), 2)
        jobs.append((P[a], P[b], AB_SEED * 100000 + i * 7717))
    print(f"■ {os.path.basename(NET_A)} vs {os.path.basename(NET_B)}  sims={SIMS}  {PAIRS}組×先後  選出={SELECT}"
          f"{'' if SELECT == 'random' else f'(温度{SEL_TEMP})'}  パーティ{len(P)}党  AB_SEED={AB_SEED}", flush=True)
    with mp.get_context("fork").Pool(W) as pool:
        out = pool.map(play, jobs, chunksize=4)
    res = [x for pr in out for x in pr]
    win = sum(1 for x in res if x > 0); lose = sum(1 for x in res if x < 0); draw = sum(1 for x in res if x == 0)
    dec = win + lose; wr = win / dec if dec else 0.0
    z = (win - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0.0
    pair_score = [sum(pr) for pr in out]
    n = len(pair_score); mu = sum(pair_score) / n
    sd = math.sqrt(sum((s - mu) ** 2 for s in pair_score) / max(n - 1, 1))
    zp = mu / (sd / math.sqrt(n)) if sd > 0 else 0.0
    sweep = sum(1 for s in pair_score if s == 2); lost = sum(1 for s in pair_score if s == -2)
    print(f"A: {win}勝 {lose}敗 {draw}分 → 勝率{wr*100:.2f}%  z={z:+.2f}  p={math.erfc(abs(z)/math.sqrt(2)):.4f}  "
          f"ペア単位z={zp:+.2f}（ペア: A2勝 {sweep} / 1勝1敗 {len(out)-sweep-lost} / A2敗 {lost}）", flush=True)
    if os.environ.get("DUMP"):
        with open(os.environ["DUMP"], "w") as f:
            json.dump({"net_a": NET_A, "net_b": NET_B, "win": win, "lose": lose, "draw": draw, "z": z,
                       "pairs": [[j[2], o[0], o[1]] for j, o in zip(jobs, out)]}, f)


if __name__ == "__main__":
    main()
