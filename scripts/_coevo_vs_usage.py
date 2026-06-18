"""共進化Top構築 vs usage生成構築 を MCTS基準でA/B。AI機械が人気ベースラインを超えるか。"""
import os, sys, random, math, json
os.environ.setdefault("OMP_NUM_THREADS","1")
from multiprocessing import Pool
import _pop_gen as G
SEASON="M-3"
_W={}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS","1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"]=get_loader(); _W["net"]=PVNetNP.load()
    sims=int(os.environ.get("MCTS_SIMS","400"))
    _W["ai"]=_net_ai(_W["net"],_W["L"],0,12,0,mcts=True,mcts_sims=sims,mcts_select="regret",mcts_fast=True)
    _W["coevo"]=[p["specs"] for p in json.load(open("/tmp/coevo_parties_M-3.json",encoding="utf-8"))["parties"][:20]]
    _W["D"]=G.load(season=SEASON)
def team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s),_W["L"],season=SEASON,randomize=False) for s in sp]
def _ab(args):
    seed,n=args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    rng=random.Random(seed); L=_W["L"]; ai=_W["ai"]
    cw=cl=dr=0
    for g in range(n):
        ce=rng.choice(_W["coevo"])                  # 共進化Top20から
        us=G.gen_party(_W["D"],rng)                 # usage生成
        A=team(ce) if g%2==0 else team(us)
        B=team(us) if g%2==0 else team(ce)
        sa=select_party(A,B,L,n=3,temperature=0.3,rng=rng); sb=select_party(B,A,L,n=3,temperature=0.3,rng=rng)
        s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
        ceon1=(g%2==0)
        try: w=Battle(s1,s2).run(ai,ai)
        except Exception: w=0
        if w==0: dr+=1
        elif (w==1)==ceon1: cw+=1
        else: cl+=1
    return cw,cl,dr
def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 480; workers=12
    per=max(1,N//workers)
    with Pool(workers,initializer=_winit) as p:
        res=p.map(_ab,[(300+k*97,per) for k in range(workers)])
    cw=sum(r[0] for r in res); cl=sum(r[1] for r in res); dr=sum(r[2] for r in res)
    dec=cw+cl; wr=cw/dec if dec else 0; z=(cw-dec*.5)/math.sqrt(dec*.25) if dec else 0
    pv=math.erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"=== 共進化Top構築 vs usage生成構築（MCTS基準・{dec+dr}戦）===")
    print(f"共進化: {cw}勝 {cl}敗 {dr}分 → {wr*100:.1f}% z={z:+.2f} p={pv:.4f} "
          f"{'有意に優位＝AIが選んだ強チーム提示に価値あり' if pv<0.05 and wr>0.5 else ('有意に劣位' if pv<0.05 else '有意差なし＝人気チーム提示で十分')}")
if __name__=="__main__": main()
