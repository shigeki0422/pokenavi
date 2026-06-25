"""確認A/B：学習選出(selector_m3) vs ランダムmega1、同一エンジン(MCTS@400・905ネット)。
本番で「学習選出を使うべき(ランダムmega1より勝つ)」を直接検証する。"""
import sys, os, random, math, pickle
import numpy as np
from multiprocessing import Pool
import _pop_gen as G
from _selector import _rand_sel_specs  # noqa
import _selector3 as S3
from simulator.learned_selection import _mega_plus_random

SEASON = os.environ.get("SEASON", "M-3")
S3.SEASON = SEASON

def _ab(args):
    seed, parties, gpp, mpath = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    L = S3._W["L"]; mc = S3._W["mc"]; rng = random.Random(seed)
    with open(mpath, "rb") as fh: sel = pickle.load(fh)
    vw = vl = dr = 0
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i + 1]
        for g in range(gpp):
            PA = S3._team(a); PB = S3._team(b)
            learn_on1 = (g % 2 == 0)
            if learn_on1:
                s1sel = S3._select_with(sel, PA, PB, rng); s2sel = _mega_plus_random(PB, rng, 3)
            else:
                s1sel = _mega_plus_random(PA, rng, 3); s2sel = S3._select_with(sel, PB, PA, rng)
            s1 = BattleSide(s1sel); s2 = BattleSide(s2sel)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            w = Battle(s1, s2).run(mc, mc)
            if w == 0: dr += 1
            elif (w == 1) == learn_on1: vw += 1
            else: vl += 1
    return vw, vl, dr

def main():
    abN = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    sims = int(sys.argv[3]) if len(sys.argv) > 3 else 400
    mpath = sys.argv[4] if len(sys.argv) > 4 else "/tmp/selector3.pkl"
    workers = 12
    os.environ["SEL_SIMS"] = str(sims)
    import time
    D = G.load(season=SEASON)
    ev = [G.gen_party(D, random.Random(9000 + k)) for k in range(abN + workers)]
    chunks = [ev[k::workers] for k in range(workers)]
    t1 = time.time()
    with Pool(workers, initializer=S3._winit) as pool:
        res = pool.map(_ab, [(8000 + k, ch, gpp, mpath) for k, ch in enumerate(chunks)])
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0
    z = (vw - dec*.5)/math.sqrt(dec*.25) if dec else 0
    from math import erfc; pv = erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"=== 確認A/B: 学習選出(selector_m3) vs ランダムmega1（同一MCTS@{sims}・{dec+dr}戦・{time.time()-t1:.0f}秒）===", flush=True)
    print(f"学習選出: {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  "
          f"{'有意に優位＝本番は学習選出を使うべき' if pv<0.05 and wr>0.5 else ('有意に劣位' if pv<0.05 else '有意差なし')}", flush=True)

if __name__ == "__main__":
    main()
