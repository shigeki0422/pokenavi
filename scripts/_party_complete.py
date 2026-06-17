"""機能2蒸留 マイルストーン2：穴埋め最適化＋A/B検証。
部分パーティ(3体)を (a)scorer貪欲補完 (b)usage-baseline補完 で6体に埋め、両者を対戦させて
scorer補完がbaselineに勝つかを検証する。勝てば「学習スコアラーで提案が成立(ms級)」。
"""
import sys, os, random, math, pickle
import numpy as np
from multiprocessing import Pool
import _pop_gen as G
import _coevo as C
from _party_scorer import encode_party

SEASON = "M-2"
_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load(); _W["NG"] = NetGreedyAI
    C.D = G.load(season=SEASON)            # _coevo の構築機構が使うグローバル
    _W["D"] = C.D
    with open("/tmp/party_scorer.pkl", "rb") as fh: _W["sc"] = pickle.load(fh)
    _W["mode"] = os.environ.get("BATTLE_AI", "ng")
    if _W["mode"] == "d2":
        from train_az2 import _net_ai
        _W["d2"] = _net_ai(_W["net"], _W["L"], 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]

def _score(specs):
    return float(_W["sc"].predict([encode_party(_team(specs))])[0])

def complete_scorer(base_specs, rng, add=3, topN=50):
    """scorer貪欲補完：候補種(usage上位)から、パーティスコアを最大化する1体を順に追加。"""
    cur = [C.parse_my(s) for s in base_specs]
    cand = [p for p, _ in _W["D"]["usage"][:topN]]
    for _ in range(add):
        used = {m["name"] for m in cur}
        best = None; bestv = -1.0
        for spname in cand:
            if G.canon(spname) in used:
                continue
            mon = C._gen_mon(spname, rng)
            trial = C.repair([dict(m) for m in cur] + [mon], rng)
            v = _score([C.to_spec(m) for m in trial])
            if v > bestv:
                bestv = v; best = mon
        if best is None:
            ns = C._fresh_species(rng, used); best = C._gen_mon(ns, rng) if ns else None
        if best is not None:
            cur.append(best)
    return [C.to_spec(m) for m in C.repair(cur, rng)]

def complete_baseline(base_specs, rng, add=3):
    """usage-baseline補完：usage重みでランダムに種を足す（素朴な人気ポケ提案相当）。"""
    cur = [C.parse_my(s) for s in base_specs]
    for _ in range(add):
        used = {m["name"] for m in cur}
        ns = C._fresh_species(rng, used)
        if ns: cur.append(C._gen_mon(ns, rng))
    return [C.to_spec(m) for m in C.repair(cur, rng)]

def _ab(args):
    seed, bases, gpp = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; net = _W["net"]; NG = _W["NG"]; rng = random.Random(seed)
    sw = sl = dr = 0
    for base in bases:
        ps = complete_scorer(base, rng)      # scorer補完
        pb = complete_baseline(base, rng)    # baseline補完
        for g in range(gpp):
            son1 = (g % 2 == 0)
            A = _team(ps) if son1 else _team(pb)
            B = _team(pb) if son1 else _team(ps)
            sa = select_party(A, B, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            ai1, ai2 = (_W["d2"], _W["d2"]) if _W.get("mode") == "d2" else (NG(net), NG(net))
            try:
                w = Battle(s1, s2).run(ai1, ai2)
            except Exception:
                w = 0
            if w == 0: dr += 1
            elif (w == 1) == son1: sw += 1
            else: sl += 1
    return sw, sl, dr

def main():
    nbase = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    workers = 12
    import time
    D = G.load(season=SEASON); rng = random.Random(123)
    bases = [G.gen_party(D, rng)[:3] for _ in range(nbase)]   # 3体の部分パーティ
    per = max(1, nbase // workers)
    chunks = [bases[k*per:(k+1)*per] for k in range(workers)]
    t0 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_ab, [(900 + k, ch, gpp) for k, ch in enumerate(chunks)])
    sw = sum(r[0] for r in res); sl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = sw + sl; wr = sw/dec if dec else 0
    z = (sw - dec*.5)/math.sqrt(dec*.25) if dec else 0
    pv = math.erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"\n=== A/B: scorer補完 vs usage-baseline補完（{dec+dr}戦・{time.time()-t0:.0f}秒）===", flush=True)
    print(f"scorer補完: {sw}勝 {sl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  "
          f"{'有意に優位＝学習スコアラーで穴埋め提案が成立' if pv<0.05 and wr>0.5 else ('有意に劣位' if pv<0.05 else '有意差なし')}", flush=True)

if __name__ == "__main__":
    main()
