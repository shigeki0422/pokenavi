"""sims A/B：同一エンジン(guardq)で sims=800(対象) vs 400(基準) を上位構築で対戦。"""
import sys, os, random, math, json, glob
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ["LEARNED_SELECTION"] = "1"
from multiprocessing import Pool
SEASON="M-3"
TEAMS=[json.load(open(p,encoding="utf-8"))["subject_party"] for p in sorted(glob.glob(os.path.join(os.path.dirname(__file__),"f1_cache.learnsel1","*.json")))]
_W={}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS","1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    _W["L"]=get_loader(); _W["net"]=PVNetNP.load()
def _ai(sims, seed):
    from train_az2 import _net_ai
    return _net_ai(_W["net"], _W["L"], 0, 12, seed, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]
def _sel(a,b,rng):
    from simulator.learned_selection import learned_select_party
    return learned_select_party(a,b,_W["L"],n=3,temperature=0.3,rng=rng)
def _games(args):
    seed,pairs,gpp=args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    L=_W["L"]; rng=random.Random(seed); vw=vl=dr=0
    for a,b in pairs:
        for g in range(gpp):
            PA=_team(a); PB=_team(b); xon1=(g%2==0)
            s1=BattleSide(_sel(PA,PB,rng)); s2=BattleSide(_sel(PB,PA,rng))
            s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
            ax=_ai(800,seed+g); ay=_ai(400,seed+g+7)
            w=Battle(s1,s2).run(ax if xon1 else ay, ay if xon1 else ax)
            if w==0: dr+=1
            elif (w==1)==xon1: vw+=1
            else: vl+=1
    return vw,vl,dr
def main():
    abN=int(sys.argv[1]) if len(sys.argv)>1 else 200; gpp=int(sys.argv[2]) if len(sys.argv)>2 else 2; workers=12
    import time
    rng=random.Random(0); idx=list(range(len(TEAMS)))
    pairs=[(TEAMS[rng.choice(idx)],TEAMS[rng.choice(idx)]) for _ in range(abN)]
    chunks=[pairs[k::workers] for k in range(workers)]
    t0=time.time()
    with Pool(workers, initializer=_winit) as pool:
        res=pool.map(_games,[(900+k,ch,gpp) for k,ch in enumerate(chunks)])
    vw=sum(r[0] for r in res); vl=sum(r[1] for r in res); dr=sum(r[2] for r in res)
    dec=vw+vl; wr=vw/dec if dec else 0; z=(vw-dec*.5)/math.sqrt(dec*.25) if dec else 0
    from math import erfc; pv=erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"[MCTS@800 vs @400] {vw}勝 {vl}敗 {dr}分 → @800勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f} ({dec+dr}戦 {time.time()-t0:.0f}s)",flush=True)
if __name__=="__main__": main()
