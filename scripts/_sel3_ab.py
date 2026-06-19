"""同一2メガ構築(X+リザードン)で選出3方式をメタ相手に大標本A/B。
切り分け: heur=ヒューリスティック(1メガ寄せ) / mcts1=MCTS選出max_mega1 / mcts2=MCTS選出max_mega2。
heur≈mcts1>mcts2 なら「2メガがsimで弱い」。heur>both なら「MCTS@100選出が下手」。"""
import sys, os, random, math
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
from _xfix import build_coherent

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
SEL_SIMS = int(os.environ.get("SEL_SIMS", "100"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    net = PVNetNP.load()
    _W["play"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["sel"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SEL_SIMS, mcts_select="regret", mcts_fast=True)
    _W["team"] = build_coherent(G.load(season=SEASON))

def _job(args):
    seed, opp_specs, method = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts
    L = _W["L"]; play = _W["play"]; sel_ai = _W["sel"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = d = both = 0
    for k in range(2):
        T = team(_W["team"]); O = team(opp_specs)
        if method == "heur":
            sa = select_party(T, O, L, n=3, temperature=0.0, rng=rng)
        else:
            sa = select_mcts(T, O, L, sel_ai, n=3, rng=rng, topk=8, max_mega=(1 if method == "mcts1" else 2))
        both += 1 if sum(1 for p in sa if getattr(p, "mega_data", None) is not None) >= 2 else 0
        sb = select_party(O, T, L, n=3, temperature=0.0, rng=rng)
        ton1 = (k == 0)
        s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        try: r = Battle(s1, s2).run(play, play)
        except Exception: r = 0
        if r == 0: d += 1
        elif (r == 1) == ton1: w += 1
        else: l += 1
    return method, w, l, d, both

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    D = G.load(season=SEASON); rng = random.Random(3)
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    import time; t0 = time.time()
    jobs = []
    for m in ("heur", "mcts1", "mcts2"):
        for i in range(gn): jobs.append((700 + i, gauntlet[i], m))
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    agg = {}
    for m, w, l, d, both in res:
        a = agg.setdefault(m, [0, 0, 0, 0]); a[0] += w; a[1] += l; a[2] += d; a[3] += both
    print(f"=== 選出3方式 (X+リザ・vs メタ{gn}・各2戦・MCTS@{SIMS}・{time.time()-t0:.0f}秒) ===")
    for m, name in (("heur", "ヒューリスティック(1メガ寄せ)"), ("mcts1", "MCTS選出 max_mega=1"), ("mcts2", "MCTS選出 max_mega=2")):
        w, l, d, both = agg[m]; dec = w + l; wr = w / dec if dec else 0; tot = w + l + d
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        print(f"{name:<24}: {w}-{l}-{d} → {wr*100:.1f}% (z={z:+.2f}) / 2メガ選出率 {both/tot*100:.0f}%")

if __name__ == "__main__":
    main()
