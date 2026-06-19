"""MEGA_PENALTY(ヒューリスティック選出の2体目メガ減点)の適正値をA/B。
2メガ構築(X+リザードン)をヒューリスティック選出でメタと対戦。env MEGA_PENALTY別に
勝率と2メガ選出率を比較。2メガが強いなら減点小の方が勝率↑のはず。"""
import sys, os, random, math
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
import _calib_probe as CP
from _xfix import build_coherent

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["team"] = build_coherent(G.load(season=SEASON))

def _job(args):
    seed, opp_specs, penalty = args
    os.environ["MEGA_PENALTY"] = str(penalty)
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = d = both = 0
    for k in range(2):
        T = team(_W["team"]); O = team(opp_specs)
        sa = select_party(T, O, L, n=3, temperature=0.0, rng=rng)
        both += 1 if sum(1 for p in sa if getattr(p, "mega_data", None) is not None) >= 2 else 0
        sb = select_party(O, T, L, n=3, temperature=0.0, rng=rng)
        ton1 = (k == 0)
        s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        try: r = Battle(s1, s2).run(ai, ai)
        except Exception: r = 0
        if r == 0: d += 1
        elif (r == 1) == ton1: w += 1
        else: l += 1
    return penalty, w, l, d, both

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    D = G.load(season=SEASON); rng = random.Random(3)
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    import time; t0 = time.time()
    jobs = []
    for pen in (50.0, 15.0, 0.0):
        for i in range(gn): jobs.append((700 + i, gauntlet[i], pen))
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    agg = {}
    for pen, w, l, d, both in res:
        a = agg.setdefault(pen, [0, 0, 0, 0]); a[0] += w; a[1] += l; a[2] += d; a[3] += both
    print(f"=== MEGA_PENALTY別 ヒューリスティック選出(2メガ構築X+リザ) vs メタ ({time.time()-t0:.0f}秒) ===")
    for pen in (50.0, 15.0, 0.0):
        w, l, d, both = agg[pen]; dec = w + l; wr = w / dec if dec else 0; tot = w + l + d
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        print(f"MEGA_PENALTY={pen:>4}: {w}-{l}-{d} → {wr*100:.1f}% (z={z:+.2f}) / 2メガ選出率 {both/tot*100:.0f}%")

if __name__ == "__main__":
    main()
