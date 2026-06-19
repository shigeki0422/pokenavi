"""シナジー選出 A/B（探索検証版）。3方式をシナジー構築で比較:
 h=ヒューリスティック選出 / m=MCTS選出(探索) / s=MCTS選出+シナジー候補注入。
ルールベース検出器がシナジー組成候補を出し、MCTS探索が良し悪しを検証して採否を決める。
学習ヘッド(ノイジー)に判定を任せず、探索に任せるのが狙い。選出評価=@SEL_SIMS, プレイ=@PLAY_SIMS。"""
import sys, os, random, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
from _calib_train import _detect_synergy, _assemble, _stat_total

SEASON = "M-3"
PLAY_SIMS = int(os.environ.get("PLAY_SIMS", "400"))
SEL_SIMS = int(os.environ.get("SEL_SIMS", "100"))
POOL_FILE = f"/tmp/coevo_parties_{SEASON}.json"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load()
    _W["play"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=PLAY_SIMS, mcts_select="regret", mcts_fast=True)
    _W["sel"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SEL_SIMS, mcts_select="regret", mcts_fast=True)

def _syn_orders(T, rng):
    pairs = _detect_synergy(T)
    orders = []
    for tr in pairs:
        sel3 = _assemble(T, tr, rng)
        if len(sel3) == 3:
            orders.append(sel3)                      # enablerが先発
            orders.append([sel3[1], sel3[0], sel3[2]])  # abuserが先発
    return orders[:4]

def _job(args):
    seed, test_specs, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts
    L = _W["L"]; play = _W["play"]; sel_ai = _W["sel"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    res = {"h": [0, 0, 0, 0], "f": [0, 0, 0, 0], "s": [0, 0, 0, 0]}
    for opp in gauntlet:
        for k in range(K):
            T = team(test_specs); O = team(opp)
            so = _syn_orders(T, rng)
            sels = {"h": select_party(T, O, L, n=3, temperature=0.3, rng=rng),
                    "f": so[0] if so else select_party(T, O, L, n=3, temperature=0.3, rng=rng),
                    "s": select_mcts(T, O, L, sel_ai, n=3, rng=rng, topk=4, extra_orders=so)}
            for tag, sa in sels.items():
                res[tag][3] += 1 if _detect_synergy(sa) else 0
                sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
                ton1 = (k % 2 == 0)
                s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
                s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
                try:
                    w = Battle(s1, s2).run(play, play)
                except Exception:
                    w = 0
                if w == 0: res[tag][2] += 1
                elif (w == 1) == ton1: res[tag][0] += 1
                else: res[tag][1] += 1
    return res

def main():
    nteams = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    import time
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader(); D = G.load(season=SEASON); rng = random.Random(0)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    pool = [p["specs"] for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"]]
    kind = os.environ.get("KIND")   # 例 KIND=rain で特定シナジーのみテスト
    def ok(sp):
        prs = _detect_synergy(team(sp))
        return bool(prs) and (kind is None or any(k == kind for k, _, _ in prs))
    tests = [sp for sp in pool if ok(sp)][:nteams]
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"シナジー構築 {len(tests)} / ガントレット {gn} / K={K} / 選出@{SEL_SIMS} プレイ@{PLAY_SIMS}", flush=True)
    jobs = [(3000 + i, tests[i], gauntlet, K) for i in range(len(tests))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        rs = p.map(_job, jobs)
    agg = {"h": [0, 0, 0, 0], "f": [0, 0, 0, 0], "s": [0, 0, 0, 0]}
    for r in rs:
        for tag in agg:
            for i in range(4): agg[tag][i] += r[tag][i]
    print(f"\n=== シナジー選出A/B (プレイMCTS@{PLAY_SIMS}・{time.time()-t0:.0f}秒) ===", flush=True)
    for tag, name in (("h", "ヒューリスティック"), ("f", "シナジー強制組成"), ("s", "MCTS選出+シナジー注入")):
        w, l, d, asm = agg[tag]; dec = w + l; wr = w / dec if dec else 0; tot = w + l + d
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        from math import erfc; pv = erfc(abs(z) / math.sqrt(2)) if dec else 1
        print(f"{name:<22}: {w}勝 {l}敗 {d}分 → {wr*100:.1f}% (p={pv:.3f}) / コア組成率 {asm/tot*100:.0f}%", flush=True)

if __name__ == "__main__":
    main()
