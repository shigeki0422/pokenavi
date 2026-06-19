"""校正ヘッド選出 vs ヒューリスティック選出 A/B。
テストチーム=シナジー対を持つ実構築(進化集団から抽出)。相手=usage生成ガントレット。
同一チーム・同一相手で2方式が選出し、両者MCTS@400でプレイ。実勝率とコア組成率を比較。
校正ヘッドがシナジーを組めて勝率が上がれば、選出器としての価値が実証される。"""
import sys, os, random, math, json, pickle
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
from _calib_train import _detect_synergy

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
POOL_FILE = f"/tmp/coevo_parties_{SEASON}.json"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.search_ai import SearchAI
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load()
    _W["ai"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["det"] = SearchAI(L, season=SEASON, seed=999)
    _W["head"] = pickle.load(open("/tmp/calib_head.pkl", "rb"))

def _has_syn(mons):
    return len(_detect_synergy(mons)) > 0

def _job(args):
    seed, test_specs, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_calib
    L = _W["L"]; ai = _W["ai"]; head = _W["head"]; det = _W["det"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    res = {"h": [0, 0, 0, 0], "c": [0, 0, 0, 0]}   # [win, loss, draw, assembled]
    for opp in gauntlet:
        for k in range(K):
            T = team(test_specs); O = team(opp)
            sels = {"h": select_party(T, O, L, n=3, temperature=0.3, rng=rng),
                    "c": select_calib(T, O, L, head, n=3, rng=rng, det=det, opp_samples=2)}
            for tag, sa in sels.items():
                res[tag][3] += 1 if _has_syn(sa) else 0
                sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
                ton1 = (k % 2 == 0)
                s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
                s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
                try:
                    w = Battle(s1, s2).run(ai, ai)
                except Exception:
                    w = 0
                if w == 0: res[tag][2] += 1
                elif (w == 1) == ton1: res[tag][0] += 1
                else: res[tag][1] += 1
    return res

def main():
    nteams = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    import time
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader(); D = G.load(season=SEASON); rng = random.Random(0)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    pool = [p["specs"] for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"]]
    tests = [sp for sp in pool if _has_syn(team(sp))][:nteams]
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"シナジー対を持つテスト構築 {len(tests)} / ガントレット {gn} / K={K} / MCTS@{SIMS}", flush=True)
    jobs = [(3000 + i, tests[i], gauntlet, K) for i in range(len(tests))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        rs = p.map(_job, jobs)
    agg = {"h": [0, 0, 0, 0], "c": [0, 0, 0, 0]}
    for r in rs:
        for tag in ("h", "c"):
            for i in range(4): agg[tag][i] += r[tag][i]
    print(f"\n=== 選出A/B (シナジー構築・両者MCTS@{SIMS}・{time.time()-t0:.0f}秒) ===", flush=True)
    for tag, name in (("h", "ヒューリスティック選出"), ("c", "校正ヘッド選出")):
        w, l, d, asm = agg[tag]; dec = w + l; wr = w / dec if dec else 0; tot = w + l + d
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        from math import erfc; pv = erfc(abs(z) / math.sqrt(2)) if dec else 1
        print(f"{name}: {w}勝 {l}敗 {d}分 → {wr*100:.1f}% (p={pv:.3f}) / コア組成率 {asm/tot*100:.0f}%", flush=True)

if __name__ == "__main__":
    main()
