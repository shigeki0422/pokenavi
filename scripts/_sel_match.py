"""選出ロジックA/B：価値ネット選出(T1) vs 現行ヒューリスティック選出。
対戦AI(d2)は両者同一にし、選出だけ変えて勝率比較。側交互でバイアス排除。
雨/バトン/メタモンを含むパーティで差が出るほど、価値ネット選出の優位＝ネット改善で自動成長を支持。
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
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load()
    _W["dai"] = _net_ai(_W["net"], _W["L"], 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def _batch(args):
    seed, parties, gpp = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    from _selnet import select_valuenet
    L = _W["L"]; net = _W["net"]; dai = _W["dai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    vw = vl = dr = 0
    for idx in range(len(parties) - 1):
        a, b = parties[idx], parties[idx + 1]
        for g in range(gpp):
            try:
                PA = team(a); PB = team(b)
                vnet_on_1 = (g % 2 == 0)   # 価値ネット選出をどちら側に
                if vnet_on_1:
                    s1sel = select_valuenet(PA, PB, L, net, n=3, rng=rng)
                    s2sel = select_party(PB, PA, L, n=3, temperature=0.0, rng=rng)
                else:
                    s1sel = select_party(PA, PB, L, n=3, temperature=0.0, rng=rng)
                    s2sel = select_valuenet(PB, PA, L, net, n=3, rng=rng)
                s1 = BattleSide(s1sel); s2 = BattleSide(s2sel)
                s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
                w = Battle(s1, s2).run(dai, dai)
            except Exception:
                w = 0
            if w == 0: dr += 1
            elif (w == 1) == vnet_on_1: vw += 1
            else: vl += 1
    return vw, vl, dr

def main():
    nparties = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    D = G.load(season=SEASON); rng = random.Random(0)
    parties = [G.gen_party(D, rng) for _ in range(nparties)]
    chunks = [parties[k::workers] for k in range(workers)]
    args = [(200 + k, ch, gpp) for k, ch in enumerate(chunks)]
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_batch, args)
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0.0
    z = (vw - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0.0
    from math import erfc; pv = erfc(abs(z) / math.sqrt(2)) if dec else 1.0
    print(f"\n=== 価値ネット選出 vs 現行ヒューリスティック選出（対戦AIは同一d2・{dec+dr}戦）===")
    print(f"価値ネット選出: {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  "
          f"{'有意に優位(p<0.05)' if pv<0.05 and wr>0.5 else ('有意に劣位' if pv<0.05 else '有意差なし')}")

if __name__ == "__main__":
    main()
