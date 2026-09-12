"""Step4 最終ゲート：リーク条件・フレッシュシード実対戦(MCTSプレイ)で honest 比較。
条件: greedyロールアウト選出 / 旧分類器選出 / noisy-oracle(既存wvのargmax=honest化される) / P2 / heuristic / 固定最良。
選出が同じ条件はdedupして対戦を節約。env: KEV(30) GA_SIMS(120)
"""
import os, json, statistics, numpy as np
os.environ["LEARNED_SELECTION"] = "1"
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("GA_SIMS", "120")
import multiprocessing as mp
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.ai import _effective_speed
from simulator.battle import BattleField
from _v3_label import _battle_3v3
# シーズンは V3_SEASON で切替（既定M-3＝従来と同一）。M-6コーパス生成でM-6を渡すため。
SEASON = os.environ.get("V3_SEASON", os.environ.get("POOL_SEASON", "M-3"))
_f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]; field = BattleField()
from engine_dispatch import call as _rust_call, ENGINE as _ENGINE
# m2_parties.json は同ファイル内の分析関数(opp_leak/party/main)専用。提案経路が使う
# _greedy_3v3 / _mcts_3v3 は参照しないので、import時に無い＝落ちる、では困る（M-6運用では不要）。
class _LazyM2(list):
    def _load(self):
        if not len(self):
            import json as _j
            self.extend(e["party"] for e in _j.load(open("m2_parties.json")))
        return self
    def __getitem__(self, i): return list.__getitem__(self._load(), i)
    def __len__(self):
        try: return list.__len__(self._load())
        except Exception: return 0
m2 = _LazyM2()
SIMS = int(os.environ.get("GA_SIMS", "120"))

def _mcts_3v3(args):
    """両者3匹固定・両者MCTSプレイ（本番同等）"""
    pa, sa, pb, sb, seed = args
    if _ENGINE == "rust":   # R5: ネイティブ実装（失敗時は自動でPython経路へ）
        _rv = _rust_call("mcts_3v3", list(pa), list(sa), list(pb), list(sb), seed, SIMS, SEASON)
        if _rv is not None:
            return _rv
    import random as _r
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    from train_az2 import _net_ai
    net = _f1._W["net"]; _r.seed(seed); f = BF()
    A = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pa]
    B = [bfs(pps(s), L, season=SEASON, randomize=True) for s in pb]
    def order(P, sub):
        mons = [P[i] for i in sub]; ld = max(range(3), key=lambda j: espd(mons[j], f))
        return [mons[ld]] + [mons[j] for j in range(3) if j != ld]
    s1 = BattleSide(order(A, sa), viewer_label="P1", source6=A); s2 = BattleSide(order(B, sb), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    _mc = os.environ.get("MCTS_CACHE", "0") == "1"; _me = os.environ.get("MCTS_EARLY", "0") == "1"
    a1 = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True, mcts_cache=_mc)
    a2 = _net_ai(net, L, 0, 12, seed ^ 0x5bd1e995, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True, mcts_cache=_mc)
    # mcts_early は _net_ai の引数ではなく SearchAI の属性（_ai_bench.py と同じ流儀）。
    # 引数で渡すと TypeError になり Python 経路が丸ごと落ちるため属性で設定する。既定off。
    if _me:
        a1.mcts_early = True; a2.mcts_early = True
    def ai1(m, o, ff): return certain_ko_override(a1(m, o, ff), m, o, ff)
    def ai2(m, o, ff): return certain_ko_override(a2(m, o, ff), m, o, ff)
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
def p2_pick(mi, oi):
    import random as _r
    from simulator.learned_selection import learned_select_party
    _r.seed(777 + mi * 131 + oi); A = party(mi)[0]; B = party(oi)[0]; idx = {id(m): j for j, m in enumerate(A)}
    return tuple(sorted(idx[id(m)] for m in learned_select_party(A, B, L, n=3, temperature=0.0, rng=_r)))
def heur_pick(mi, oi):
    import random as _r
    from simulator.ai import select_party
    _r.seed(777 + mi * 131 + oi); A = party(mi)[0]; B = party(oi)[0]; idx = {id(m): j for j, m in enumerate(A)}
    return tuple(sorted(idx[id(m)] for m in select_party(A, B, L, n=3, temperature=0.0, rng=_r)))

if __name__ == "__main__":
    det = json.load(open("v3leak_detail.json"))
    GW = json.load(open("v3_greedy_wr.json"))
    KEV = int(os.environ.get("KEV", "30"))
    # 党ごとの固定最良（全相手平均のargmax）
    per_party = {}
    for gi, d in enumerate(det): per_party.setdefault(d["mi"], []).append(d)
    fixed_S = {}
    for mi, ds in per_party.items():
        opts = [tuple(s) for s in ds[0]["opts"]]
        fixed_S[mi] = max(opts, key=lambda S: statistics.mean(
            dict(zip([tuple(x) for x in dd["opts"]], dd["wr"])).get(S, 0.0) for dd in ds))
    # 各グループの選出
    conds = ["greedy", "clf", "noisy_oracle", "p2", "heur", "fixed"]
    picks = {}
    for gi, d in enumerate(det):
        mi, oi = d["mi"], d["oi"]; opts = [tuple(s) for s in d["opts"]]
        gsc = [GW.get(f"{gi}|{'_'.join(map(str,s))}", [0, 1]) for s in opts]
        gwr = [a[0] / max(1, a[1]) for a in gsc]
        picks[(gi, "greedy")] = opts[int(np.argmax(gwr))]
        picks[(gi, "clf")] = opts[int(np.argmax(d["score"]))]
        picks[(gi, "noisy_oracle")] = opts[int(np.argmax(d["wr"]))]
        picks[(gi, "p2")] = p2_pick(mi, oi); picks[(gi, "heur")] = heur_pick(mi, oi)
        picks[(gi, "fixed")] = fixed_S[mi]
    # dedup対戦
    need = {}
    for gi, d in enumerate(det):
        for c in conds:
            need.setdefault((gi, picks[(gi, c)]), []).append(c)
    jobs, meta = [], []
    for (gi, s), _ in need.items():
        d = det[gi]; ob = opp_leak(d["mi"], d["oi"])
        for k in range(KEV):
            seed = (77_000_000 + gi * 1000003 + hash(s) % 10000 * 7 + k) & 0x7fffffff  # フレッシュ帯
            jobs.append((m2[d["mi"]], s, m2[d["oi"]], ob, seed)); meta.append((gi, s))
    print(f"フレッシュ実対戦 {len(jobs)}戦（{len(need)}ユニーク選出×K{KEV}, MCTSプレイ）…", flush=True)
    pool = mp.get_context("fork").Pool(max(1, (os.cpu_count() or 2) - 1))
    res = pool.map(_mcts_3v3, jobs, chunksize=4); pool.close()
    W = {}
    for (gi, s), r in zip(meta, res):
        a = W.setdefault((gi, s), [0, 0]); a[1] += 1 if r in (1, 2) else 0; a[0] += 1 if r == 1 else 0
    print(f"\n■ 最終ゲート：リーク条件・フレッシュ実対戦（{len(det)}グループ×K{KEV}）", flush=True)
    for c, lbl in [("noisy_oracle", "oracle(honest化)"), ("greedy", "greedyロールアウト選出"), ("clf", "旧分類器選出"),
                   ("fixed", "固定最良"), ("p2", "P2"), ("heur", "heuristic")]:
        vals = [W[(gi, picks[(gi, c)])][0] / max(1, W[(gi, picks[(gi, c)])][1]) for gi in range(len(det))]
        print(f"  {lbl:22} {statistics.mean(vals)*100:.1f}%", flush=True)
