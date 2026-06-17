import os, time
for k in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"): os.environ[k]="1"
import multiprocessing as mp
from simulator.simulate import get_loader
from simulator.env import load_registered_parties
from simulator.pokemon import parse_pokemon_spec
import sim_tree
def timed_one(args):
    t=time.time(); r=sim_tree._run_one(args); return time.time()-t, r["w"]
if __name__=="__main__":
    loader=get_loader(); ps=load_registered_parties(loader,complete_only=True)
    s1=[parse_pokemon_spec(s["name"]) for s in ps[0].specs]; s2=[parse_pokemon_spec(s["name"]) for s in ps[1].specs]
    sim_tree._ensure_loaded("M-2",16)
    args=[(s1,s2,0.6,7000+i) for i in range(10)]
    # 逐次
    t=time.time(); seq=[timed_one(a) for a in args]; seqwall=time.time()-t
    print(f"逐次: wall {seqwall:.0f}秒  各戦 {[round(x[0]) for x in seq]}",flush=True)
    # 並列(fork, 10ワーカー)
    ctx=mp.get_context("fork")
    t=time.time()
    with ctx.Pool(10) as pool: par=pool.map(timed_one, args)
    parwall=time.time()-t
    print(f"並列: wall {parwall:.0f}秒  各戦 {[round(x[0]) for x in par]}",flush=True)
    print(f"→ 並列の各戦時間が逐次より大きく伸びていれば競合、伸びてなければスケジューリング/ばらつき",flush=True)
