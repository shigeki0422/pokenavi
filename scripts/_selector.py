"""選出評価器の試作(b)：開幕局面に特化した値モデルを (encode_state, 実対戦outcome) で学習。
d0(汎用価値ネットの開幕評価, r=0.23)より高い相関を狙う。学習は対戦AIの出力(勝敗)から→AI改善で自動成長。
phase1 データ生成(並列・d2 det4) → phase2 MLP学習 → phase3 相関評価(vs 実勝率)。
"""
import sys, os, random, math
import numpy as np
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-2"

class ValMLP:
    def __init__(self, dim, hidden=128, seed=0):
        rng = np.random.default_rng(seed)
        self.W1 = rng.normal(0, (1/dim)**.5, (hidden, dim)); self.b1 = np.zeros(hidden)
        self.W2 = rng.normal(0, (1/hidden)**.5, hidden); self.b2 = 0.0
    def predict(self, X):
        X = np.asarray(X, float); H = np.tanh(X @ self.W1.T + self.b1)
        return 1/(1+np.exp(-(H @ self.W2 + self.b2)))
    def fit(self, X, Y, epochs=50, lr=0.05, l2=1e-5, batch=256, seed=0, val=None):
        X = np.asarray(X, float); Y = np.asarray(Y, float); n = len(X); rng = np.random.default_rng(seed)
        for ep in range(epochs):
            idx = rng.permutation(n)
            for s in range(0, n, batch):
                bi = idx[s:s+batch]; xb = X[bi]; yb = Y[bi]; B = len(bi)
                H = np.tanh(xb @ self.W1.T + self.b1); v = 1/(1+np.exp(-(H @ self.W2 + self.b2)))
                gv = (v - yb) / B
                gW2 = H.T @ gv; gb2 = gv.sum(); dH = np.outer(gv, self.W2) * (1 - H**2)
                gW1 = dH.T @ xb; gb1 = dH.sum(0)
                self.W2 -= lr*(gW2 + l2*self.W2); self.b2 -= lr*gb2
                self.W1 -= lr*(gW1 + l2*self.W1); self.b1 -= lr*gb1
        return self

_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); net = PVNetNP.load()
    _W["L"] = L; _W["net"] = net
    _W["dai"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=4)

def _rand_sel_specs(specs, mons, rng):
    for _ in range(20):
        idx = rng.sample(range(len(mons)), 3)
        if sum(1 for i in idx if getattr(mons[i], "mega_data", None) is not None) <= 1:
            return [specs[i] for i in idx]
    idx = rng.sample(range(len(mons)), 3); return [specs[i] for i in idx]

def _gen(args):
    seed, parties, per = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    L = _W["L"]; dai = _W["dai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    out = []
    for _ in range(per):
        a, b = rng.sample(parties, 2)
        sa = _rand_sel_specs(a, team(a), rng); sb = _rand_sel_specs(b, team(b), rng)
        s1 = BattleSide(team(sa)); s2 = BattleSide(team(sb)); s1.field_idx = 0; s2.field_idx = 1
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        X = encode_state(s1, s2, BattleField())
        t1 = BattleSide(team(sa)); t2 = BattleSide(team(sb)); t1.belief = OpponentBelief(L); t2.belief = OpponentBelief(L)
        w = Battle(t1, t2).run(dai, dai)
        if w == 0: continue
        out.append((X, 1.0 if w == 1 else 0.0))
    return out

def _eval_batch(args):  # 相関評価用: (selector予測, 実勝率) を返す
    seed, parties, K, wpath = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    import pickle
    L = _W["L"]; dai = _W["dai"]; rng = random.Random(seed)
    with open(wpath, "rb") as fh: sel = pickle.load(fh)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    out = []
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i+1]
        sa = _rand_sel_specs(a, team(a), rng); sb = _rand_sel_specs(b, team(b), rng)
        s1 = BattleSide(team(sa)); s2 = BattleSide(team(sb)); s1.field_idx = 0; s2.field_idx = 1
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        pred = float(sel.predict([encode_state(s1, s2, BattleField())])[0])
        w1 = dec = 0
        for g in range(K):
            t1 = BattleSide(team(sa)); t2 = BattleSide(team(sb)); t1.belief = OpponentBelief(L); t2.belief = OpponentBelief(L)
            w = Battle(t1, t2).run(dai, dai)
            if w == 0: continue
            dec += 1; w1 += (w == 1)
        if dec: out.append((pred, w1/dec))
    return out

def _pearson(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return cov/(sx*sy) if sx and sy else 0.0

def main():
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    neval = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    workers = 12
    import time, pickle
    D = G.load(season=SEASON); rng = random.Random(0)
    parties = [G.gen_party(D, rng) for _ in range(400)]
    t0 = time.time()
    per = max(1, nsamp // workers)
    args = [(700 + k, parties, per) for k in range(workers)]
    data = []
    with Pool(workers, initializer=_winit) as pool:
        for r in pool.map(_gen, args): data += r
    print(f"phase1 データ生成: {len(data)}サンプル {time.time()-t0:.0f}秒", flush=True)
    X = [d[0] for d in data]; Y = [d[1] for d in data]
    ntr = int(len(X)*0.9)
    sel = ValMLP(len(X[0]), hidden=128).fit(X[:ntr], Y[:ntr], epochs=60)
    # val acc
    pv = sel.predict(X[ntr:]); ya = np.asarray(Y[ntr:])
    acc = float(((pv >= 0.5) == (ya >= 0.5)).mean())
    print(f"phase2 学習完了: val勝敗的中率 {acc*100:.1f}% (n={len(ya)})", flush=True)
    with open("/tmp/selector.pkl", "wb") as fh: pickle.dump(sel, fh)
    # phase3 相関評価
    ev_parties = [G.gen_party(D, random.Random(9000)) for _ in range(neval + workers)]
    chunks = [ev_parties[k::workers] for k in range(workers)]
    eargs = [(8000+k, ch, K, "/tmp/selector.pkl") for k, ch in enumerate(chunks)]
    pairs = []
    with Pool(workers, initializer=_winit) as pool:
        for r in pool.map(_eval_batch, eargs): pairs += r
    preds = [p for p, _ in pairs]; act = [a for _, a in pairs]
    r = _pearson(preds, act); mae = sum(abs(p-a) for p, a in zip(preds, act))/len(pairs)
    print(f"\n=== 選出評価器 vs 実勝率（{len(pairs)}局面・各最大{K}戦）===", flush=True)
    print(f"  学習選出評価器: Pearson r = {r:.3f}  MAE = {mae:.3f}", flush=True)
    print(f"  （比較: 汎用ネットd0={'0.234'}  d2={'0.377'}）", flush=True)
    print(f"  → {'d0/d2より改善＝学習選出評価器が有効' if r>0.40 else 'd2並み/未満'}", flush=True)

if __name__ == "__main__":
    main()
