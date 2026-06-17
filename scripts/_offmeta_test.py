"""現行ネットは「実メタ外ポケモン」を操縦できるか検証。
同一パーティのミラー戦で NetGreedy vs Heuristic を行い、ネットの操縦エッジ(対Heuristic勝率)が
選出3体中の実メタ外個体数で変わるかを見る。同一チーム対戦なのでパーティ強弱の交絡は排除される。
エッジが実メタ外で縮むなら「汎化はするが新規個体には弱い＝M-3で伸び代大」が確定。
"""
import sys, os, random, math
from collections import defaultdict
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-2"
_W = {}
def _winit(meta):
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["meta"] = meta

def _batch(args):
    seed, parties, gpp = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, HeuristicAI
    from train_az2 import _net_ai
    L = _W["L"]; net = _W["net"]; meta = _W["meta"]; rng = random.Random(seed)
    dai = _net_ai(net, L, 0, 12, seed, tree=True, tree_depth=2, tree_k=4, tree_det=8)  # 実戦戦術=d2探索
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    res = defaultdict(lambda: [0, 0])  # offcount -> [netwins, decisive]
    for specs in parties:
        full = team(specs)
        sel = select_party(full, full, L, n=3, temperature=0.3, rng=rng)
        sel_specs = [specs[full.index(p)] for p in sel]
        offc = sum(1 for p in sel if G.canon(p.name) not in meta)
        for g in range(gpp):
            a = team(sel_specs); b = team(sel_specs)             # 同一3体をミラー
            s1 = BattleSide(a); s2 = BattleSide(b); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            net_s1 = (g % 2 == 0)
            ai1 = dai if net_s1 else HeuristicAI()
            ai2 = HeuristicAI() if net_s1 else dai
            w = Battle(s1, s2).run(ai1, ai2)
            if w == 0: continue
            res[offc][1] += 1
            if (w == 1) == net_s1: res[offc][0] += 1
    return dict(res)

def main():
    nparties = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    workers = 12
    from simulator.simulate import get_loader
    from simulator.env import load_registered_parties
    L = get_loader(); D = G.load(season=SEASON); rng = random.Random(0)
    meta = set()
    for p in load_registered_parties(L, complete_only=True):
        for s in p.specs: meta.add(G.canon(s.get("name")))
    parties = [G.gen_party(D, rng) for _ in range(nparties)]
    chunks = [parties[k::workers] for k in range(workers)]
    args = [(100 + k, ch, gpp) for k, ch in enumerate(chunks)]
    agg = defaultdict(lambda: [0, 0])
    with Pool(workers, initializer=_winit, initargs=(meta,)) as pool:
        for d in pool.map(_batch, args):
            for oc, (w, dec) in d.items():
                agg[oc][0] += w; agg[oc][1] += dec
    print(f"実メタ{len(meta)}種 / 生成{nparties}パーティ・各{gpp}ミラー戦")
    print("選出3体中の実メタ外数 → ネットの操縦エッジ(対Heuristic勝率):")
    # off=0 と off>=2 をまとめて比較
    buckets = {"0(全実メタ)": [0,0], "1": [0,0], "2+": [0,0]}
    for oc, (w, dec) in sorted(agg.items()):
        key = "0(全実メタ)" if oc == 0 else ("1" if oc == 1 else "2+")
        buckets[key][0] += w; buckets[key][1] += dec
        wr = w/dec*100 if dec else 0
        print(f"  off={oc}: {w}/{dec}勝 = {wr:.1f}%  (決着{dec})")
    for k, (w, dec) in buckets.items():
        wr = w/dec*100 if dec else 0
        print(f"  実メタ外{k}: ネット勝率 {wr:.1f}%  (決着{dec})")
    # off=0 vs off>=1 で比較
    w0, n0 = buckets["0(全実メタ)"]
    w1, n1 = buckets["1"][0] + buckets["2+"][0], buckets["1"][1] + buckets["2+"][1]
    print("\n=== off=0 vs off>=1 比較 ===")
    if n0 and n1:
        p0, p1 = w0/n0, w1/n1
        se = math.sqrt(p0*(1-p0)/n0 + p1*(1-p1)/n1)
        z = (p0-p1)/se if se else 0
        from math import erfc; pv = erfc(abs(z)/math.sqrt(2))
        print(f"  全実メタ: {p0*100:.1f}% (決着{n0})   実メタ外含む(>=1): {p1*100:.1f}% (決着{n1})")
        print(f"  差 = {(p0-p1)*100:+.1f}pt  z={z:.2f} p={pv:.4f}")
        print(f"  → {'有意にエッジ縮小＝ネットは新規個体に弱い(M-3伸び代大)' if pv<0.05 and p0>p1 else ('有意に逆' if pv<0.05 else '有意差なし')}")

if __name__ == "__main__":
    main()
