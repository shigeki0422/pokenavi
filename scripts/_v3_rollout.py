"""Step3: プレイアウト推定器の診断。held-outグループの全選出をGreedyAI高速ロールアウトで対戦し、
greedy勝率 ↔ 真のMCTS勝率(v3leak_detail) のwithin-group相関を測る。0.5-0.6超なら推定器として採用。
env: KR(24) NG(48)
"""
import os, json, statistics, numpy as np
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "1")
import multiprocessing as mp
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.ai import _effective_speed
from simulator.battle import BattleField
_f1._ensure_loaded("M-3", 8); L = _f1._W["loader"]; field = BattleField(); SEASON = "M-3"
m2 = [e["party"] for e in json.load(open("m2_parties.json"))]

def _greedy_3v3(args):
    """両者3匹固定・両者GreedyAIプレイの高速対戦"""
    pa, sa, pb, sb, seed = args
    import random as _r
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import GreedyAI, certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    _r.seed(seed); f = BF()
    A = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pa]
    B = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pb]
    def order(P, sub):
        mons = [P[i] for i in sub]; ld = max(range(3), key=lambda j: espd(mons[j], f))
        return [mons[ld]] + [mons[j] for j in range(3) if j != ld]
    s1 = BattleSide(order(A, sa), viewer_label="P1", source6=A); s2 = BattleSide(order(B, sb), viewer_label="P2", source6=B)
    # beliefはGreedyAIから一切読まれない（読むのはSearchAIの根の決定化のみ）が、observe_damageが
    # 被弾ごとに候補×16ロールのcalc_damageを回すため実行時間の94%を占める。結果に影響しないので既定で作らない。
    # 例外＝calc_damage内で乱数を消費する技（きまぐレーザー）を含む場合のみ、乱数列を保つため従来通り作る。
    if any("きまぐレーザー" in s for s in pa) or any("きまぐレーザー" in s for s in pb):
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    g1 = GreedyAI(); g2 = GreedyAI()
    def ai1(m, o, ff): return certain_ko_override(g1(m, o, ff), m, o, ff)
    def ai2(m, o, ff): return certain_ko_override(g2(m, o, ff), m, o, ff)
    return Battle(s1, s2, BF()).run(ai1, ai2)

cache = {}
def party(i):
    if i not in cache:
        P = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in m2[i]]
        cache[i] = (P, {id(x): _effective_speed(x, field) for x in P})
    return cache[i]
def opp_leak(mi, oi):
    import random as _r
    from simulator.ai import select_party
    _r.seed(202 + mi * 53 + oi); B = party(oi)[0]; A = party(mi)[0]; idx = {id(m): j for j, m in enumerate(B)}
    return tuple(sorted(idx[id(m)] for m in select_party(B, A, L, n=3, temperature=0.0, rng=_r)))

if __name__ == "__main__":
    det = json.load(open("v3leak_detail.json"))
    KR = int(os.environ.get("KR", "24")); NG = int(os.environ.get("NG", "48"))
    det = det[:NG]
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 1))
    jobs, meta = [], []
    for gi, d in enumerate(det):
        mi, oi = d["mi"], d["oi"]; ob = opp_leak(mi, oi)
        for s in d["opts"]:
            for k in range(KR):
                seed = (60000 + gi * 7919 + hash(tuple(s)) % 1000 * 3 + k) & 0x7fffffff
                jobs.append((m2[mi], tuple(s), m2[oi], tuple(ob), seed)); meta.append((gi, tuple(s)))
    print(f"greedyロールアウト {len(jobs)}戦…", flush=True)
    res = pool.map(_greedy_3v3, jobs, chunksize=8); pool.close()
    gw = {}
    for (gi, s), r in zip(meta, res):
        a = gw.setdefault((gi, s), [0, 0]); a[1] += 1 if r in (1, 2) else 0; a[0] += 1 if r == 1 else 0
    json.dump({f"{gi}|{'_'.join(map(str,s))}": v for (gi, s), v in gw.items()}, open("v3_greedy_wr.json", "w"))
    rc, t1, gaps = [], [], []
    for gi, d in enumerate(det):
        opts = [tuple(s) for s in d["opts"]]; wv = d["wr"]
        if len(set(wv)) <= 1: continue
        sc = [gw[(gi, s)][0] / max(1, gw[(gi, s)][1]) for s in opts]
        rs = np.argsort(np.argsort(sc)); rw = np.argsort(np.argsort(wv))
        rc.append(np.corrcoef(rs, rw)[0, 1])
        t1.append(1.0 if int(np.argmax(sc)) == int(np.argmax(wv)) else 0.0)
        gaps.append(max(wv) - wv[int(np.argmax(sc))])
    print(f"\n■ greedyロールアウト推定器（{len(rc)}グループ, 各選出K{KR}）", flush=True)
    print(f"  基準: 旧分類器 順位相関+0.333 / argmax17% / regret22.5pt", flush=True)
    print(f"  順位相関(平均) = {statistics.mean(rc):+.3f}", flush=True)
    print(f"  argmax一致    = {statistics.mean(t1)*100:.0f}%", flush=True)
    print(f"  regret        = {statistics.mean(gaps)*100:.1f}pt", flush=True)
