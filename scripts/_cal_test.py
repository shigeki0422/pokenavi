"""診断A：価値ネットのターン0(開幕)評価が実勝率と相関するか。
多数の開幕局面で V=価値ネット予測(P(side1勝)) と、その局面からd2自己対戦した実勝率を比較。
相関が弱い/較正がズレていれば「開幕評価は選出オラクルとして不十分」が確定（T1失敗の原因）。
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
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load()
    _W["dai"] = _net_ai(_W["net"], _W["L"], 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)

def _rand_sel(mons, rng):  # 3体ランダム(≤1メガ)・lead=先頭
    for _ in range(20):
        idx = rng.sample(range(len(mons)), 3)
        sel = [mons[i] for i in idx]
        if sum(1 for p in sel if getattr(p, "mega_data", None) is not None) <= 1:
            return sel
    return [mons[i] for i in rng.sample(range(len(mons)), 3)]

def _batch(args):
    seed, parties, K = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    L = _W["L"]; net = _W["net"]; dai = _W["dai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    out = []  # (V, side1_wins, decisive)
    for i in range(len(parties) - 1):
        a, b = parties[i], parties[i + 1]
        selA_specs = None
        # 選出をspecで固定（毎対戦リビルドのため）
        Af = team(a); Bf = team(b)
        selA = _rand_sel(Af, rng); selB = _rand_sel(Bf, rng)
        selA_specs = [a[Af.index(p)] for p in selA]; selB_specs = [b[Bf.index(p)] for p in selB]
        # V = 価値ネットの開幕評価
        s1 = BattleSide(team(selA_specs)); s2 = BattleSide(team(selB_specs))
        s1.field_idx = 0; s2.field_idx = 1
        V = float(net.evaluate(encode_state(s1, s2, BattleField()), [0])[1])
        # 実対戦K局（d2同士）
        w1 = dec = 0
        for g in range(K):
            t1 = BattleSide(team(selA_specs)); t2 = BattleSide(team(selB_specs))
            t1.belief = OpponentBelief(L); t2.belief = OpponentBelief(L)
            w = Battle(t1, t2).run(dai, dai)
            if w == 0: continue
            dec += 1
            if w == 1: w1 += 1
        if dec >= 1: out.append((V, w1, dec))
    return out

def main():
    nmatch = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    workers = 12
    D = G.load(season=SEASON); rng = random.Random(0)
    parties = [G.gen_party(D, rng) for _ in range(nmatch + workers)]
    chunks = [parties[k::workers] for k in range(workers)]
    args = [(300 + k, ch, K) for k, ch in enumerate(chunks)]
    data = []
    with Pool(workers, initializer=_winit) as pool:
        for r in pool.map(_batch, args): data += r
    # 相関とキャリブレーション
    Vs = [d[0] for d in data]; act = [d[1] / d[2] for d in data]
    n = len(data)
    mv = sum(Vs) / n; ma = sum(act) / n
    cov = sum((v - mv) * (a - ma) for v, a in zip(Vs, act))
    sv = math.sqrt(sum((v - mv) ** 2 for v in Vs)); sa = math.sqrt(sum((a - ma) ** 2 for a in act))
    pear = cov / (sv * sa) if sv and sa else 0.0
    print(f"\n=== 診断A: ターン0価値 V vs 実勝率（{n}局面・各最大{K}戦）===")
    print(f"V範囲: {min(Vs):.2f}〜{max(Vs):.2f}（平均{mv:.2f}）  実勝率平均{ma:.2f}")
    print(f"Pearson相関 r = {pear:.3f}  （高いほど開幕評価が信頼できる。0.7+で良好/0.3未満は不十分）")
    print("\nキャリブレーション（V帯ごとの実勝率）:")
    bins = [(0, .3), (.3, .45), (.45, .55), (.55, .7), (.7, 1.01)]
    for lo, hi in bins:
        sub = [(v, a) for v, a in zip(Vs, act) if lo <= v < hi]
        if sub:
            mvb = sum(v for v, _ in sub) / len(sub); mab = sum(a for _, a in sub) / len(sub)
            print(f"  V∈[{lo:.2f},{hi:.2f}): n={len(sub):>3}  予測平均{mvb:.2f} → 実勝率{mab:.2f}  ({'乖離大' if abs(mvb-mab)>0.15 else 'おおむね一致'})")

if __name__ == "__main__":
    main()
