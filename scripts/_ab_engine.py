"""エンジン設定A/B：同一ネット・同一選出で、行動決定ロジックだけ変えて上位環境構築で対戦。
ベースライン=訪問数ベース(visit)。比較=Qベース(qsel)/下方ガード(guard)/併用(guard+qsel)。
各比較は「対象設定(side1) vs visit(side2)」を上位73構築のペアで対戦し勝率を測る。
"""
import sys, os, random, math, json, glob
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ["LEARNED_SELECTION"] = "1"
from multiprocessing import Pool

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
K = int(os.environ.get("AB_K", "8"))
MARGIN = float(os.environ.get("AB_MARGIN", "0.10"))
TEAMS = [json.load(open(p, encoding="utf-8"))["subject_party"]
         for p in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "f1_cache.learnsel1", "*.json")))]
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load()

def _mkai(mode, seed):
    from train_az2 import _net_ai
    ai = _net_ai(_W["net"], _W["L"], 0, 12, seed, mcts=True, mcts_sims=SIMS,
                 mcts_select="regret", mcts_fast=True)
    ai.qselect = ("qsel" in mode)
    ai.downside_guard = ("guard" in mode)
    ai.downside_k = K; ai.downside_margin = MARGIN
    return ai

def _team(sp):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    return [build_from_spec(parse_pokemon_spec(s), _W["L"], season=SEASON, randomize=False) for s in sp]

def _sel(party6, opp6, rng):
    from simulator.learned_selection import learned_select_party
    return learned_select_party(party6, opp6, _W["L"], n=3, temperature=0.3, rng=rng)

def _games(args):
    seed, mode, pairs, gpp = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    L = _W["L"]; rng = random.Random(seed)
    vw = vl = dr = 0
    for a, b in pairs:
        for g in range(gpp):
            PA = _team(a); PB = _team(b)
            xon1 = (g % 2 == 0)   # 対象設定が side1 か
            sa = _sel(PA, PB, rng); sb = _sel(PB, PA, rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            ai_x = _mkai(mode, seed + g); ai_v = _mkai("visit", seed + g + 7)
            w = Battle(s1, s2).run(ai_x if xon1 else ai_v, ai_v if xon1 else ai_x)
            if w == 0: dr += 1
            elif (w == 1) == xon1: vw += 1
            else: vl += 1
    return vw, vl, dr

def run_cmp(mode, abN, gpp, workers=12):
    import time
    rng = random.Random(0)
    idx = list(range(len(TEAMS)))
    pairs = [(TEAMS[rng.choice(idx)], TEAMS[rng.choice(idx)]) for _ in range(abN)]
    chunks = [pairs[k::workers] for k in range(workers)]
    t0 = time.time()
    with Pool(workers, initializer=_winit) as pool:
        res = pool.map(_games, [(900 + k, mode, ch, gpp) for k, ch in enumerate(chunks)])
    vw = sum(r[0] for r in res); vl = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = vw + vl; wr = vw / dec if dec else 0
    z = (vw - dec*.5)/math.sqrt(dec*.25) if dec else 0
    from math import erfc; pv = erfc(abs(z)/math.sqrt(2)) if dec else 1
    tag = {"qsel":"Qベース","guard":"下方ガード","guard+qsel":"ガード+Q"}.get(mode, mode)
    print(f"[{tag} vs 訪問数ベース] {vw}勝 {vl}敗 {dr}分 → 勝率{wr*100:.1f}%  z={z:+.2f} p={pv:.4f}  "
          f"({dec+dr}戦 {time.time()-t0:.0f}s K={K} margin={MARGIN})", flush=True)

def main():
    abN = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    gpp = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    modes = os.environ.get("AB_MODES", "qsel,guard,guard+qsel").split(",")
    print(f"=== エンジン設定A/B (上位{len(TEAMS)}構築・MCTS@{SIMS}・各{abN}ペア×{gpp}・K={K} margin={MARGIN}) ===", flush=True)
    for mode in modes:
        run_cmp(mode.strip(), abN, gpp)

if __name__ == "__main__":
    main()
