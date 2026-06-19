"""893ネット(MCTS@400) vs HeuristicAI を M-3 で。絶対強さの確認。"""
import os,sys,random,math
os.environ.setdefault("OMP_NUM_THREADS","1")
from multiprocessing import Pool
import _pop_gen as G
SEASON="M-3"; _W={}
NET=sys.argv[2] if len(sys.argv)>2 else "az_net_coevo_M-3.json"
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS","1")
    from simulator.simulate import get_loader
    _W["L"]=get_loader(); _W["D"]=G.load(season=SEASON)
def _batch(args):
    seed,n=args
    from simulator.az_np import PVNetNP
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, HeuristicAI
    from train_az2 import _net_ai
    L=_W["L"]; rng=random.Random(seed)
    net=PVNetNP.load(NET)
    nai=_net_ai(net,L,0,12,0,mcts=True,mcts_sims=400,mcts_select="regret",mcts_fast=True)
    hai=HeuristicAI()
    pool=[G.gen_party(_W["D"],rng) for _ in range(40)]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]
    nw=nl=dr=0
    for g in range(n):
        a,b=rng.sample(pool,2); A=team(a); B=team(b)
        sa=select_party(A,B,L,n=3,temperature=0.3,rng=rng); sb=select_party(B,A,L,n=3,temperature=0.3,rng=rng)
        s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
        non1=(g%2==0)
        try: w=Battle(s1,s2).run(nai if non1 else hai, hai if non1 else nai)
        except Exception: w=0
        if w==0: dr+=1
        elif (w==1)==non1: nw+=1
        else: nl+=1
    return nw,nl,dr
def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 360; workers=12; per=max(1,N//workers)
    with Pool(workers,initializer=_winit) as p:
        res=p.map(_batch,[(800+k*53,per) for k in range(workers)])
    nw=sum(r[0] for r in res); nl=sum(r[1] for r in res); dr=sum(r[2] for r in res)
    dec=nw+nl; wr=nw/dec if dec else 0; z=(nw-dec*.5)/math.sqrt(dec*.25) if dec else 0
    pv=math.erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"=== {NET}(MCTS@400) vs Heuristic・{dec+dr}戦 ===")
    print(f"ネット: {nw}勝 {nl}敗 {dr}分 → {wr*100:.1f}% p={pv:.4f}")
if __name__=="__main__": main()
