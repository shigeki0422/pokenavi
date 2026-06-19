"""MCTS選出(select_mcts)が雨コア/Xを同時選出するか＝ネットがシナジーを選出に反映するか。
ヒューリスティック(0%)と対比。"""
import os,sys,random
os.environ.setdefault("OMP_NUM_THREADS","1")
from multiprocessing import Pool
import _pop_gen as G
SEASON="M-3"; _W={}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS","1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"]=get_loader(); _W["D"]=G.load(season=SEASON); net=PVNetNP.load()
    _W["sel"]=_net_ai(net,_W["L"],0,12,0,mcts=True,mcts_sims=int(os.environ.get("SELSIMS","120")),mcts_select="regret",mcts_fast=True)
def forced(D,name,item,ab):
    mv=sorted(D["moves"].get(name,{}),key=D["moves"][name].get,reverse=True)[:4] if D["moves"].get(name) else []
    nat=max(D["natures"].get(name,{"":1}),key=D["natures"].get(name,{"":1}).get) if D["natures"].get(name) else None
    ev=D["evs"].get(name,[(None,1)])[0][0]
    return G._spec(name,item,nat,mv,ev,ab)
def usf(D,name):
    return forced(D,name,max(D["items"].get(name,{"":1}),key=D["items"].get(name,{"":1}).get) if D["items"].get(name) else None,
                  max(D["abil"].get(name,{"":1}),key=D["abil"].get(name,{"":1}).get) if D["abil"].get(name) else None)
def _job(args):
    seed,core_specs,core_names,n=args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts, select_valuenet
    from simulator.az_np import PVNetNP
    L=_W["L"]; D=_W["D"]; rng=random.Random(seed); ai=_W["sel"]; net=PVNetNP.load()
    def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]
    def fill(core):
        t=list(core); pool=[p for p,_ in D["usage"][:80] if p not in core_names]; rng.shuffle(pool)
        for p in pool:
            if len(t)>=6: break
            it=max(D["items"].get(p,{"":1}),key=D["items"].get(p,{"":1}).get) if D["items"].get(p) else None
            if it and "ナイト" in it: continue
            t.append(usf(D,p))
        return t[:6]
    hb=mb=vb=0
    for _ in range(n):
        T=team(fill(core_specs)); O=team(G.gen_party(D,rng))
        hn=[p.name for p in select_party(T,O,L,n=3,temperature=0.0,rng=rng)]
        mn=[p.name for p in select_mcts(T,O,L,ai,n=3,rng=rng)]
        vn=[p.name for p in select_valuenet(T,O,L,net,n=3,rng=rng)]
        ok=lambda names: all(cn in names for cn in core_names)
        hb+=ok(hn); mb+=ok(mn); vb+=ok(vn)
    return hb,mb,vb,n
def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 24; workers=8; per=max(1,N//workers)
    D=G.load(season=SEASON)
    rain=([forced(D,"ペリッパー","しめったいわ","あめふらし"),forced(D,"ラグラージ","ラグラージナイト","げきりゅう")],{"ペリッパー","ラグラージ"})
    for label,(core,names) in [("雨コア",rain)]:
        with Pool(workers,initializer=_winit) as p:
            res=p.map(_job,[(300+k,core,names,per) for k in range(workers)])
        hb=sum(r[0] for r in res); mb=sum(r[1] for r in res); vb=sum(r[2] for r in res); n=sum(r[3] for r in res)
        print(f"=== {label} 同時選出率 (N={n}) ===")
        print(f"ヒューリスティック: {hb/n*100:.0f}% / 価値ネット選出(T1): {vb/n*100:.0f}% / MCTS選出(T2): {mb/n*100:.0f}%")
if __name__=="__main__": main()
