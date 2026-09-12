"""ステップ2再定式化 ②：両者の3匹をgiven（固定）にした3v3を多数対戦しラベル化。
相手選出の変動を排除＝ノイズ減＋3v3は勝率が極端に振れ信号大。matchup_featsで学習可能かの土台データ。
出力 v3_labels.json。env: NM(1200) K(6) GA_SIMS(120)
"""
import os, json, random, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "120")
import multiprocessing as mp
import feature1 as _f1
_f1._ensure_loaded(os.environ.get("POOL_SEASON", "M-3"), 8)
SEASON = os.environ.get("POOL_SEASON", "M-3"); SIMS = int(os.environ.get("GA_SIMS", "120"))
SUBSETS = list(itertools.combinations(range(6), 3))

def _valid(specs):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = _f1._W["loader"]
    P = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    av = sum(1 for m in P if getattr(m, "mega_data", None) is not None)
    tgt = 1 if av >= 1 else 0
    return [S for S in SUBSETS if sum(1 for i in S if getattr(P[i], "mega_data", None) is not None) == tgt]

def _battle_3v3(args):
    """両者の3匹を固定(sA,sB)して対戦。lead=各々最速。"""
    pa, sa, pb, sb, seed = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import certain_ko_override, _effective_speed
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    from train_az2 import _net_ai
    L = _f1._W["loader"]; net = _f1._W["net"]; field = BattleField(); _r.seed(seed)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    def order(P, sub):
        mons = [P[i] for i in sub]; ld = max(range(3), key=lambda j: _effective_speed(mons[j], field))
        return [mons[ld]] + [mons[j] for j in range(3) if j != ld]
    s1 = BattleSide(order(A, sa), viewer_label="P1", source6=A); s2 = BattleSide(order(B, sb), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    a2 = _net_ai(net, L, 0, 12, seed ^ 0x5bd1e995, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    def ai1(m, o, f): return certain_ko_override(a1(m, o, f), m, o, f)
    def ai2(m, o, f): return certain_ko_override(a2(m, o, f), m, o, f)
    return Battle(s1, s2, BattleField()).run(ai1, ai2)

if __name__ == "__main__":
    m2 = [e["party"] for e in json.load(open("m2_parties.json"))]
    NM = int(os.environ.get("NM", "1200")); K = int(os.environ.get("K", "6"))
    rng = random.Random(20)
    valid = {}
    def vget(i):
        if i not in valid: valid[i] = _valid(m2[i])
        return valid[i]
    # 多様な3v3マッチアップをサンプル
    matchups = []
    for _ in range(NM):
        ai = rng.randrange(len(m2)); bi = rng.randrange(len(m2))
        while bi == ai: bi = rng.randrange(len(m2))
        sA = rng.choice(vget(ai)); sB = rng.choice(vget(bi))
        matchups.append((ai, sA, bi, sB))
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 1))
    out = {"m2_ref": True, "rows": []}
    BATCH = 100
    for start in range(0, NM, BATCH):
        chunk = matchups[start:start + BATCH]
        jobs = []
        for mi, (ai, sA, bi, sB) in enumerate(chunk):
            for k in range(K):
                seed = (400 + (start + mi) * 7919 + k) & 0x7fffffff
                jobs.append((m2[ai], tuple(sA), m2[bi], tuple(sB), seed))
        res = pool.map(_battle_3v3, jobs, chunksize=4)
        for mi, (ai, sA, bi, sB) in enumerate(chunk):
            rr = res[mi * K:(mi + 1) * K]
            w = sum(1 for r in rr if r == 1); d = sum(1 for r in rr if r in (1, 2))
            out["rows"].append({"ai": ai, "sA": list(sA), "bi": bi, "sB": list(sB), "w": w, "d": d})
        json.dump(out, open("v3_labels.json", "w"))
        print(f"[{min(start+BATCH,NM)}/{NM}] 3v3ラベル化", flush=True)
    pool.close()
    print("■ 3v3ラベル生成完了 v3_labels.json", flush=True)
