import random, time
from simulator.simulate import get_loader
from simulator.env import load_registered_parties, build_party, heuristic_selection
from simulator.battle import Battle, BattleSide
from simulator.belief import OpponentBelief
from simulator.ai import HeuristicAI
from simulator.az_np import PVNetNP
from train_az2 import _net_ai
loader=get_loader(); parties=load_registered_parties(loader,complete_only=True); net=PVNetNP.load()
def mk_d2(s): return _net_ai(net,loader,0,12,s,tree=True,tree_depth=2,tree_k=3,tree_det=20)
def mk_d3(s): return _net_ai(net,loader,0,12,s,tree=True,tree_depth=3,tree_k=3,tree_det=10)
def mk_plain(s): return _net_ai(net,loader,48,12,s)
def duel(mkA,mkB,N,tag,base=400000):
    rng=random.Random(2024); aw=bw=0; t0=time.time()
    for i in range(N):
        pa,pb=rng.sample(parties,2)
        s1=BattleSide(heuristic_selection(build_party(pa,loader),build_party(pb,loader),loader))
        s2=BattleSide(heuristic_selection(build_party(pb,loader),build_party(pa,loader),loader))
        s1.belief=OpponentBelief(loader); s2.belief=OpponentBelief(loader); seed=base+i
        if i%2==0: w=Battle(s1,s2).run(mkA(seed),mkB(seed)); aw+=(w==1); bw+=(w==2)
        else:      w=Battle(s1,s2).run(mkB(seed),mkA(seed)); aw+=(w==2); bw+=(w==1)
    print(f"① {tag}: {aw}-{bw} = {aw/max(1,aw+bw):.0%}  ({time.time()-t0:.0f}秒)",flush=True)
def play(actor,pair,s):
    random.seed(s); pa,pb=pair
    s1=BattleSide(heuristic_selection(build_party(pa,loader),build_party(pb,loader),loader))
    s2=BattleSide(heuristic_selection(build_party(pb,loader),build_party(pa,loader),loader))
    s1.belief=OpponentBelief(loader); s2.belief=OpponentBelief(loader)
    return Battle(s1,s2).run(actor(),HeuristicAI())==1

duel(mk_d2,mk_plain,40,"tree(d2) vs plain  [確定N=40]")
# ② d2 大きめペアCRN
rng=random.Random(777); d2=pw=hw=nb=0
for i in range(30):
    pair=rng.sample(parties,2)
    for k in range(3):
        bs=600000+i*1000+k
        d2+=play(lambda:mk_d2(bs),pair,bs); pw+=play(lambda:mk_plain(bs),pair,bs); hw+=play(lambda:HeuristicAI(),pair,bs); nb+=1
print(f"② ペアCRN N=30 vs Heuristic(同一カード):",flush=True)
print(f"  tree d2 : {d2/nb:.1%} (差 {(d2-hw)/nb*100:+.1f}pt) => vs plain {(d2-pw)/nb*100:+.1f}pt",flush=True)
print(f"  plain   : {pw/nb:.1%} (差 {(pw-hw)/nb*100:+.1f}pt)",flush=True)
# ③ d3 傾向（小N）
duel(mk_d3,mk_plain,14,"tree(d3) vs plain  [傾向N=14]",base=420000)
