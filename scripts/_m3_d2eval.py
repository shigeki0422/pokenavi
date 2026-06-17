"""学習M-3ネット vs 現行ネットを d2(強評価器)で A/B。NetGreedyゲートの測定限界を排除。"""
import sys, os, random, math
from multiprocessing import Pool
import _pop_gen as G
SEASON="M-3"
_W={}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS","1")
    from simulator.simulate import get_loader
    _W["L"]=get_loader()
def _batch(args):
    seed, pool, n, pathA, pathB = args
    from simulator.az_np import PVNetNP
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from train_az2 import _net_ai
    L=_W["L"]; nA=PVNetNP.load(pathA); nB=PVNetNP.load(pathB); rng=random.Random(seed)
    aiA=_net_ai(nA,L,0,12,0,tree=True,tree_depth=2,tree_k=4,tree_det=8)
    aiB=_net_ai(nB,L,0,12,0,tree=True,tree_depth=2,tree_k=4,tree_det=8)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]
    aw=al=dr=0
    for g in range(n):
        a,b=rng.sample(pool,2)
        try:
            A=team(a); B=team(b)
            sa=select_party(A,B,L,n=3,temperature=0.3,rng=rng); sb=select_party(B,A,L,n=3,temperature=0.3,rng=rng)
            s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
            Aon1=(g%2==0)
            w=Battle(s1,s2).run(aiA if Aon1 else aiB, aiB if Aon1 else aiA)
            if w==0: dr+=1
            elif (w==1)==Aon1: aw+=1
            else: al+=1
        except Exception: dr+=1
    return aw,al,dr
def main():
    N=int(sys.argv[1]) if len(sys.argv)>1 else 300
    workers=12
    D=G.load(season=SEASON); rng=random.Random(0)
    pool=[G.gen_party(D,rng) for _ in range(150)]
    per=max(1,N//workers)
    args=[(7000+k*131, pool, per, "az_net_coevo_M-3.json", "../scripts/simulator/az_net_np.json") for k in range(workers)]
    # 現行ネットはPVNetNP.load()既定パスを使う
    args=[(7000+k*131, pool, per, "az_net_coevo_M-3.json", None) for k in range(workers)]
    # Noneは既定(現行)を意味させる→_batch側で対応
    with Pool(workers, initializer=_winit) as p:
        res=p.map(_batch2, args)
    aw=sum(r[0] for r in res); al=sum(r[1] for r in res); dr=sum(r[2] for r in res)
    dec=aw+al; wr=aw/dec if dec else 0; z=(aw-dec*0.5)/math.sqrt(dec*0.25) if dec else 0
    from math import erfc; pv=erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"d2評価: 学習M-3ネット {aw}勝 {al}敗 {dr}分 → {wr*100:.1f}% p={pv:.4f} "
          f"{'有意に強化' if pv<0.05 and wr>0.5 else ('有意に弱化' if pv<0.05 else '有意差なし')}")
def _batch2(args):
    seed,pool,n,pathA,_=args
    from simulator.az_np import PVNetNP
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from train_az2 import _net_ai
    L=_W["L"]; nA=PVNetNP.load(pathA); nB=PVNetNP.load(); rng=random.Random(seed)
    aiA=_net_ai(nA,L,0,12,0,tree=True,tree_depth=2,tree_k=4,tree_det=8)
    aiB=_net_ai(nB,L,0,12,0,tree=True,tree_depth=2,tree_k=4,tree_det=8)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s),L,season=SEASON,randomize=False) for s in sp]
    aw=al=dr=0
    for g in range(n):
        a,b=rng.sample(pool,2)
        try:
            A=team(a); B=team(b)
            sa=select_party(A,B,L,n=3,temperature=0.3,rng=rng); sb=select_party(B,A,L,n=3,temperature=0.3,rng=rng)
            s1=BattleSide(sa); s2=BattleSide(sb); s1.belief=OpponentBelief(L); s2.belief=OpponentBelief(L)
            Aon1=(g%2==0)
            w=Battle(s1,s2).run(aiA if Aon1 else aiB, aiB if Aon1 else aiA)
            if w==0: dr+=1
            elif (w==1)==Aon1: aw+=1
            else: al+=1
        except Exception: dr+=1
    return aw,al,dr
if __name__=="__main__": main()
