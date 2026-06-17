"""選出評価器(b改)：ユーザー提案 k=1・決定的フルゲーム・プレイアウトでラベル生成。
固定ダメージロール＋固定seedで「互いが(narrow)最善を打ち続けた結着」を低分散の1本で得る。
→ K戦平均のノイズを排除＋終盤シナジーも結論に反映＋k=1で高速。学習し、最終はA/B(実d2対戦)でヒューリスティック超えを判定。
"""
import sys, os, random, math, pickle
import numpy as np
from multiprocessing import Pool
import _pop_gen as G
from _selector import ValMLP, _rand_sel_specs

SEASON = "M-2"
ROLL = 0.85          # 固定ロール(分散低減・tree_rollと同値)
BSEED = 12345        # 対戦の固定seed(決定化)

_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); net = PVNetNP.load()
    _W["L"] = L; _W["net"] = net
    _W["k1"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=1, tree_det=1)   # k=1 narrow
    _W["d2"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)   # 実戦(A/B用)

def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]

def _det_playout(sa, sb):
    """d2(デプロイAI)・固定ロール・固定seedの決定的フルゲーム。戻り: 1(side1勝)/0(side2)/None(分)
    ラベルとデプロイ戦略を一致させる(アライン)＋固定ロール/seedで低分散。"""
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    import simulator.damage as _dmg
    L = _W["L"]; d2 = _W["d2"]
    t1 = BattleSide(_team(sa)); t2 = BattleSide(_team(sb)); t1.belief = OpponentBelief(L); t2.belief = OpponentBelief(L)
    prev = _dmg._ROLL_OVERRIDE; _dmg._ROLL_OVERRIDE = ROLL; random.seed(BSEED)
    try:
        w = Battle(t1, t2).run(d2, d2)
    finally:
        _dmg._ROLL_OVERRIDE = prev
    return None if w == 0 else (1.0 if w == 1 else 0.0)

def _gen(args):
    seed, parties, per = args
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    L = _W["L"]; rng = random.Random(seed)
    out = []
    for _ in range(per):
        a, b = rng.sample(parties, 2)
        sa = _rand_sel_specs(a, _team(a), rng); sb = _rand_sel_specs(b, _team(b), rng)
        s1 = BattleSide(_team(sa)); s2 = BattleSide(_team(sb)); s1.field_idx = 0; s2.field_idx = 1
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        X = encode_state(s1, s2, BattleField())
        y = _det_playout(sa, sb)
        if y is not None: out.append((X, y))
    return out

def _select_with(selmodel, full, opp_full, rng, opp_samples=3):
    """学習選出評価器で3体選出（候補×相手選出サンプルの平均予測で最良）"""
    from itertools import combinations
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    from simulator.ai import select_party
    L = _W["L"]
    opp_sels = [select_party(opp_full, full, L, n=min(3, len(opp_full)), temperature=0.0, rng=rng)]
    for _ in range(opp_samples - 1):
        opp_sels.append(select_party(opp_full, full, L, n=min(3, len(opp_full)), temperature=1.0, rng=rng))
    best = None; bestv = -1
    for combo in combinations(range(len(full)), 3):
        sub = [full[i] for i in combo]
        if sum(1 for p in sub if getattr(p, "mega_data", None) is not None) > 1: continue
        for li in range(3):
            order = [sub[li]] + [sub[j] for j in range(3) if j != li]
            xs = []
            for os_ in opp_sels:
                s1 = BattleSide(order); s2 = BattleSide(list(os_)); s1.field_idx = 0; s2.field_idx = 1
                xs.append(encode_state(s1, s2, BattleField()))
            v = float(np.mean(selmodel.predict(xs)))
            if v > bestv: bestv = v; best = order
    return best

def _ab(args):
    seed, parties, gpp, mpath = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; d2 = _W["d2"]; rng = random.Random(seed)
    with open(mpath, "rb") as fh: sel = pickle.load(fh)
    vw = vl = dr = 0
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i + 1]
        for g in range(gpp):
            PA = _team(a); PB = _team(b)
            von1 = (g % 2 == 0)
            if von1:
                s1sel = _select_with(sel, PA, PB, rng); s2sel = select_party(PB, PA, L, n=3, temperature=0.0, rng=rng)
            else:
                s1sel = select_party(PA, PB, L, n=3, temperature=0.0, rng=rng); s2sel = _select_with(sel, PB, PA, rng)
            s1 = BattleSide(s1sel); s2 = BattleSide(s2sel); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            w = Battle(s1, s2).run(d2, d2)
            if w == 0: dr += 1
            elif (w == 1) == von1: vw += 1
            else: vl += 1
    return vw, vl, dr

def main():
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    abN = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    gpp = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    workers = 12
    import time
    D = G.load(season=SEASON); rng = random.Random(0)
    parties = [G.gen_party(D, rng) for _ in range(400)]
    t0 = time.time(); per = max(1, nsamp // workers)
    with Pool(workers, initializer=_winit) as pool:
        data = []
        for r in pool.map(_gen, [(700 + k, parties, per) for k in range(workers)]): data += r
    print(f"phase1 d2決定的ラベル生成: {len(data)}サンプル {time.time()-t0:.0f}秒 (勝率{np.mean([d[1] for d in data]):.2f})", flush=True)
    X = [d[0] for d in data]; Y = [d[1] for d in data]; ntr = int(len(X) * 0.9)
    sel = ValMLP(len(X[0]), hidden=256).fit(X[:ntr], Y[:ntr], epochs=100)
    pv = sel.predict(X[ntr:]); ya = np.asarray(Y[ntr:])
    acc = float(((pv >= 0.5) == (ya >= 0.5)).mean())
    print(f"phase2 学習完了: 決定ラベルval的中率 {acc*100:.1f}% (n={len(ya)})", flush=True)
    with open("/tmp/selector2.pkl", "wb") as fh: pickle.dump(sel, fh)
    # phase3 A/B: 学習選出 vs ヒューリスティック（実d2対戦）
    ev = [G.gen_party(D, random.Random(9000)) for _ in range(abN + workers)]
    chunks = [ev[k::workers] for k in range(workers)]
    t1 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_ab, [(8000 + k, ch, gpp, "/tmp/selector2.pkl") for k, ch in enumerate(chunks)])
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0; z = (vw - dec*.5)/math.sqrt(dec*.25) if dec else 0
    from math import erfc; pv2 = erfc(abs(z)/math.sqrt(2)) if dec else 1
    print(f"\n=== A/B: 学習選出(d2決定的ラベル) vs 現行ヒューリスティック（実d2・{dec+dr}戦・{time.time()-t1:.0f}秒）===", flush=True)
    print(f"学習選出: {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv2:.4f}  "
          f"{'有意に優位＝学習選出が現行超え' if pv2<0.05 and wr>0.5 else ('有意に劣位' if pv2<0.05 else '有意差なし')}", flush=True)

if __name__ == "__main__":
    main()
