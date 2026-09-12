"""Product3クイック提案エンジン＋検証。
covered_sample候補 → 価値ネットのターン0パネル評価で強い順にランキング（対戦ゼロ）。
検証: サロゲート上位 vs 下位、および vs QD最終 を実戦で比較（上位が強ければサロゲート有効）。
env NCAND(300) PANEL(24) TOPN(60) K(12) SIMS(300) OUT(候補json)
"""
import os, sys, json, random, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", os.environ.get("SIMS", "300"))
import multiprocessing as mp
import feature1 as _f1
from gen_party_ga import _play_winner
from gen_party_pool import PartyGen
from _threat_coverage import load_threats, covered_sample

# M-3固定だとM-6運用でnet-t0とeval_vs_builtが旧環境のテンプレートで計算される。
SEASON = os.environ.get("POOL_SEASON", "M-3")
NCAND = int(os.environ.get("NCAND", "300"))
PANELN = int(os.environ.get("PANEL", "24"))
TOPN = int(os.environ.get("TOPN", "60"))
K = int(os.environ.get("K", "12"))

_W = {}
def _score_setup(L, net, panel_specs):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    _W["L"] = L; _W["net"] = net
    _W["panel"] = [[build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp] for sp in panel_specs]

def surrogate_score(specs):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    L = _W["L"]; net = _W["net"]
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    vals = []
    for B in _W["panel"]:
        sa = learned_select_party(A, B, L, n=3, temperature=0.0)
        sb = learned_select_party(B, A, L, n=3, temperature=0.0)
        s1 = BattleSide(sa, source6=A); s2 = BattleSide(sb, source6=B)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        vals.append(net.evaluate(encode_state(s1, s2, BattleField()), [0])[1])
    return statistics.mean(vals)

def eval_vs_built(specs, opp_built):
    """自分specs vs 相手(構築済み)。価値ネットの想定有利度と、学習選出が選ぶ自分の3体を返す。"""
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    L = _W["L"]; net = _W["net"]
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    names = [s.split("@")[0] for s in specs]
    sa = learned_select_party(A, opp_built, L, n=3, temperature=0.0)   # 貪欲＝各相手に最適な選出3体
    sb = learned_select_party(opp_built, A, L, n=3, temperature=0.0)
    s1 = BattleSide(sa, source6=A); s2 = BattleSide(sb, source6=opp_built)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    v = net.evaluate(encode_state(s1, s2, BattleField()), [0])[1]
    pick = []
    for m in sa:
        try: pick.append(names[A.index(m)])
        except ValueError: pass
    return float(v), pick

def wr_vs(cands, opps, seedbase):
    jobs = []; owner = []
    rng = random.Random(seedbase)
    for i, p in enumerate(cands):
        for k in range(K):
            jobs.append((p, rng.choice(opps), (seedbase + i * 131 + k * 7) & 0x7fffffff)); owner.append(i)
    workers = max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(workers) as pool:
        res = pool.map(_play_winner, jobs, chunksize=4)
    w = sum(1 for r in res if r == 1); dec = sum(1 for r in res if r in (1, 2))
    return w / dec if dec else 0.5

def main():
    _f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]; net = _f1._W["net"]
    pg = PartyGen(); th = load_threats(L); rng = random.Random(0)
    final = [e["party"] for e in json.load(open("gen_pop_step1.json"))]
    panel = [final[i] for i in rng.sample(range(len(final)), PANELN)]
    _score_setup(L, net, panel)
    # 候補生成＋スコアリング
    cands = []
    while len(cands) < NCAND:
        p = covered_sample(pg, L, th, rng, tries=6)
        if p: cands.append(p)
    scored = sorted(((surrogate_score(p), p) for p in cands), key=lambda x: -x[0])
    print(f"候補{len(scored)}体をサロゲート評価。スコア範囲 {scored[-1][0]:.3f}〜{scored[0][0]:.3f}", flush=True)
    top = [p for _, p in scored[:TOPN]]
    bot = [p for _, p in scored[-TOPN:]]
    out = os.environ.get("OUT")
    if out:
        json.dump([{"party": p, "score": round(s, 4)} for s, p in scored], open(out, "w"), ensure_ascii=False)
    # 検証
    print("検証中（上位/下位 × QD最終）...", flush=True)
    top_f = wr_vs(top, final, 1000)
    bot_f = wr_vs(bot, final, 5000)
    tvb = wr_vs(top, bot, 9000)
    print(f"\n■ サロゲート検証（K={K}戦/体, SIMS={os.environ.get('GA_SIMS')}）")
    print(f"  サロゲート上位{TOPN} vs QD最終: {top_f*100:.1f}%   (無選抜covered_sample=46%)")
    print(f"  サロゲート下位{TOPN} vs QD最終: {bot_f*100:.1f}%")
    print(f"  上位 vs 下位 直接対決: {tvb*100:.1f}%  (>55%ならサロゲートが強さを識別)")

if __name__ == "__main__":
    main()
