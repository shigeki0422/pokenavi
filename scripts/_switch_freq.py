"""AIの自発交代頻度を測る。設置が過小評価される原因が「AIが交代しない」かを切り分ける。
各対戦で AIが返した行動の move/switch を数え、1試合あたりの自発交代数・交代率を集計。
実戦シングルは概ね1試合に数回の交代がある。極端に少なければエンジン忠実度の問題(b)。
"""
import os, json, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "150"))
NPROC = int(os.environ.get("NPROC", "12"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    cnt = {"move": 0, "switch": 0}
    def AI(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        t = getattr(a, "type", None)
        if t in cnt: cnt[t] += 1
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        b = Battle(s1, s2); b.run(AI, AI)
        return cnt["move"], cnt["switch"], b.turn
    except Exception:
        return 0, 0, 0

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(11)
    jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"{N}戦 MCTS@{SIMS} で自発交代頻度を測定", flush=True)
    M = S = T = games = 0
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for mv, sw, turns in p.map(_job, jobs):
            if turns == 0: continue
            M += mv; S += sw; T += turns; games += 1
    print(f"\n試合数 {games} / 平均ターン {T/games:.1f}")
    print(f"両者合計の自発交代 {S}（1試合あたり {S/games:.2f}）/ 攻撃・技 {M}")
    print(f"行動に占める交代率 {S/max(1,M+S)*100:.1f}%")
    print(f"片側1試合あたりの自発交代 約{S/games/2:.2f}回")

if __name__ == "__main__":
    main()
