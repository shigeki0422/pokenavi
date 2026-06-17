"""MCTS(PUCT/DUCT) vs 現行d2(全幅expectiminimax) の対戦検証。
選出はヒューリスティック固定で両者揃え、対戦中の方策の強さだけを比較する。
生成パーティ(M-3基準)で実施。引数: sims c_puct 戦数 gpp。
"""
import sys, os, random, math
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-2"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); net = PVNetNP.load()
    sims = int(os.environ["MCTS_SIMS"]); cp = float(os.environ["MCTS_CPUCT"])
    sel = os.environ.get("MCTS_SELECT", "duct")
    _W["L"] = L
    mc = _net_ai(net, L, 0, 50, 0, mcts=True, mcts_sims=sims, c_puct=cp, mcts_select=sel)
    if "MCTS_ETA" in os.environ:
        mc.exp3_eta = float(os.environ["MCTS_ETA"])
    if "MCTS_GAMMA" in os.environ:
        mc.exp3_gamma = float(os.environ["MCTS_GAMMA"])
    _W["mcts"] = mc
    _W["d2"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]

def _ab(args):
    seed, parties, gpp = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; mc = _W["mcts"]; d2 = _W["d2"]; rng = random.Random(seed)
    vw = vl = dr = 0
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i + 1]
        for g in range(gpp):
            fa, fb = _team(a), _team(b)
            mc_on1 = (g % 2 == 0)   # mctsがside1かside2か交互
            s1sel = select_party(fa, fb, L, n=3, temperature=0.0, rng=rng)
            s2sel = select_party(fb, fa, L, n=3, temperature=0.0, rng=rng)
            s1 = BattleSide(list(s1sel)); s2 = BattleSide(list(s2sel))
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            ai1, ai2 = (mc, d2) if mc_on1 else (d2, mc)
            w = Battle(s1, s2).run(ai1, ai2)
            if w == 0: dr += 1
            elif (w == 1) == mc_on1: vw += 1
            else: vl += 1
    return vw, vl, dr

def main():
    sims = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    cp = float(sys.argv[2]) if len(sys.argv) > 2 else 1.5
    abN = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    gpp = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    sel = sys.argv[5] if len(sys.argv) > 5 else "duct"
    workers = 12
    os.environ["MCTS_SIMS"] = str(sims); os.environ["MCTS_CPUCT"] = str(cp)
    os.environ["MCTS_SELECT"] = sel
    import time
    D = G.load(season=SEASON)
    ev = [G.gen_party(D, random.Random(9000)) for _ in range(abN + workers)]
    chunks = [ev[k::workers] for k in range(workers)]
    t0 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_ab, [(8000 + k, ch, gpp) for k, ch in enumerate(chunks)])
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0
    z = (vw - dec * .5) / math.sqrt(dec * .25) if dec else 0
    pv = math.erfc(abs(z) / math.sqrt(2)) if dec else 1
    verdict = ("有意に優位＝MCTSが現行d2超え" if pv < 0.05 and wr > 0.5
               else ("有意に劣位" if pv < 0.05 else "有意差なし"))
    print(f"\n=== MCTS[{sel}](sims={sims},c_puct={cp}) vs 現行d2(k4,det8)  生成パーティ {dec+dr}戦 {time.time()-t0:.0f}秒 ===", flush=True)
    print(f"MCTS: {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  {verdict}", flush=True)

if __name__ == "__main__":
    main()
