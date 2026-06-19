"""機能2 採用候補トップNを、独立(別seed)大標本で再検証。多重比較の上振れを除いた確定勝率。"""
import sys, os, random, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
from _func2_pipeline import _winit, _job, _species

SEASON = os.environ.get("COEVO_SEASON", "M-3")

def main():
    topn = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    import time
    full = json.load(open(f"func2_teams_{SEASON}.json", encoding="utf-8"))
    teams = full["teams"][:topn]
    D = G.load(season=SEASON); rng = random.Random(9999)        # 別seed=独立ガントレット
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"確定検証: 採用上位{len(teams)} vs 独立メタ{gn}・各{gn*K}戦・MCTS@400", flush=True)
    jobs = [(9000 + i, teams[i]["specs"], gauntlet, K) for i in range(len(teams))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    print(f"\n=== 確定勝率（独立大標本・{time.time()-t0:.0f}秒）===", flush=True)
    out = []
    for cand, w, l, d in res:
        dec = w + l; wr = w / dec if dec else 0
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        pv = math.erfc(abs(z) / math.sqrt(2)) if dec else 1
        out.append((wr, z, pv, w, l, d, cand))
    # 確定勝率をJSONへ書き戻す（specsで突合）
    bykey = {tuple(_species(o[6])): o for o in out}
    for t in full["teams"]:
        o = bykey.get(tuple(t["species"]))
        if o:
            t["confirmed_wr"], t["confirmed_z"], t["confirmed_p"] = o[0], o[1], o[2]
    json.dump(full, open(f"func2_teams_{SEASON}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    out.sort(reverse=True)
    for wr, z, pv, w, l, d, cand in out:
        sig = "★有意" if pv < 0.05 and wr > 0.5 else ""
        print(f"{wr*100:5.1f}% (z={z:+.2f} p={pv:.3f}{sig}) {w}-{l}-{d}  {' / '.join(_species(cand))}", flush=True)
    print("（確定勝率を func2_teams_*.json に書き戻し）", flush=True)

if __name__ == "__main__":
    main()
