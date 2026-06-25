"""交代先選択の勝率A/B：同一ネットで『ダメージ考慮版』vs『タイプ相性版』を直接対戦。
side._pivot_mode で側ごとに方式を切替（dmg / type）。M-1テンプレ、先後入替で公平化。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "200")); NPROC = int(os.environ.get("NPROC", "12"))
NET_PATH = os.environ.get("NET_PATH", "az_net_np.json")
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(NET_PATH), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed, dmg_is_s1 = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def ai(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        s1._pivot_mode = "dmg" if dmg_is_s1 else "type"
        s2._pivot_mode = "type" if dmg_is_s1 else "dmg"
        w = Battle(s1, s2).run(ai, ai)
        if w == 0: return 0          # 引分
        dmg_won = (w == 1) == dmg_is_s1
        return 1 if dmg_won else -1
    except Exception:
        return 0

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = []
    for k in range(N):
        a, b = rng.sample(range(n), 2)
        jobs.append((parties[a], parties[b], rng.randrange(10**6), k % 2 == 0))
    print(f"NET={NET_PATH} / 交代先A/B ダメージ版 vs タイプ版 / M-1 {N}戦 MCTS@{SIMS}", flush=True)
    dmg_w = typ_w = draw = 0; t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r in p.map(_job, jobs):
            if r == 1: dmg_w += 1
            elif r == -1: typ_w += 1
            else: draw += 1
    dec = dmg_w + typ_w
    print(f"完了 {time.time()-t0:.0f}s")
    print(f"ダメージ版 {dmg_w}勝 / タイプ版 {typ_w}勝 / 引分 {draw}")
    print(f"ダメージ版の勝率（決着のみ）: {dmg_w*100/max(1,dec):.1f}%")

if __name__ == "__main__":
    main()
