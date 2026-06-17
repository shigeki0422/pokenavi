"""診断A＋深さ遷移：開幕局面での選出評価が、先読み深さ d でどれだけ実勝率に相関するか。
各局面で d0(静的価値)/d1(1手先読み)/d2(2手先読み) の推定値と、d2フル対戦の実勝率を比較。
低depthで相関が立てば、その深さの浅いシミュレーションを選出に使えばよい。
"""
import sys, os, random, math
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-2"
_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); net = PVNetNP.load()
    _W["L"] = L; _W["net"] = net
    _W["d1"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=1, tree_k=4, tree_det=8)
    _W["d2"] = _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def _rand_sel(mons, rng):
    for _ in range(20):
        idx = rng.sample(range(len(mons)), 3); sel = [mons[i] for i in idx]
        if sum(1 for p in sel if getattr(p, "mega_data", None) is not None) <= 1: return sel
    return [mons[i] for i in rng.sample(range(len(mons)), 3)]

def _batch(args):
    seed, parties, K = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    L = _W["L"]; net = _W["net"]; d1 = _W["d1"]; d2 = _W["d2"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    out = []
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i + 1]
        Af = team(a); Bf = team(b)
        selA = _rand_sel(Af, rng); selB = _rand_sel(Bf, rng)
        sA = [a[Af.index(p)] for p in selA]; sB = [b[Bf.index(p)] for p in selB]
        try:
            s1 = BattleSide(team(sA)); s2 = BattleSide(team(sB)); s1.field_idx = 0; s2.field_idx = 1
            s1.belief = OpponentBelief(L); f = BattleField()
            e0 = float(net.evaluate(encode_state(s1, s2, f), [0])[1])
            sc1 = d1.score_actions_tree(s1, s2, f); e1 = max(v for _, v in sc1) if sc1 else e0
            sc2 = d2.score_actions_tree(s1, s2, f); e2 = max(v for _, v in sc2) if sc2 else e0
        except Exception:
            continue
        w1 = dec = 0
        for g in range(K):
            t1 = BattleSide(team(sA)); t2 = BattleSide(team(sB))
            t1.belief = OpponentBelief(L); t2.belief = OpponentBelief(L)
            w = Battle(t1, t2).run(d2, d2)
            if w == 0: continue
            dec += 1; w1 += (w == 1)
        if dec >= 1: out.append((e0, e1, e2, w1 / dec))
    return out

def _pearson(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return cov/(sx*sy) if sx and sy else 0.0

def main():
    nmatch = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    workers = 12
    D = G.load(season=SEASON); rng = random.Random(0)
    parties = [G.gen_party(D, rng) for _ in range(nmatch + workers)]
    chunks = [parties[k::workers] for k in range(workers)]
    args = [(400 + k, ch, K) for k, ch in enumerate(chunks)]
    data = []
    with Pool(workers, initializer=_winit) as pool:
        for r in pool.map(_batch, args): data += r
    act = [d[3] for d in data]; n = len(data)
    print(f"\n=== 選出評価の深さ遷移: 推定 vs 実勝率（{n}局面・各最大{K}戦）===")
    for di, name in [(0, "d0 静的価値"), (1, "d1 1手先読み"), (2, "d2 2手先読み")]:
        est = [d[di] for d in data]
        r = _pearson(est, act)
        # キャリブレーション乖離(平均絶対誤差)
        mae = sum(abs(e - a) for e, a in zip(est, act)) / n
        print(f"  {name}: Pearson r = {r:.3f}   平均絶対誤差(予測-実) = {mae:.3f}   "
              f"{'信頼できる(r>=0.7)' if r >= 0.7 else ('そこそこ(0.5-0.7)' if r >= 0.5 else '不十分(<0.5)')}")
    print("\n→ 選出には『r が十分立つ最小の深さ』のシミュレーションを使えばよい。")

if __name__ == "__main__":
    main()
