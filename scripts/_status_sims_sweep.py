"""sims数を振って設置/状態異常技の使用率が改善するか検証。
改善する→探索深度の問題（simsを上げれば解決）。横ばい→ネット評価が設置価値を学べていない（学習の問題）。
"""
import os, json, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"
N = int(os.environ.get("N", "80"))
NPROC = int(os.environ.get("NPROC", "12"))
SIMS_LIST = [250, 400, 800, 1600, 3200]
WATCH = ["ステルスロック", "どくびし", "おにび", "つるぎのまい"]
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=_W["sims"],
                       mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def AI(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    held = {k: 0 for k in WATCH}; used = {k: 0 for k in WATCH}
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        b = Battle(s1, s2); b.run(AI, AI)
        for side in (sa, sb):
            for mon in side:
                for mv in mon.moves:
                    if mv and mv.name_jp in held: held[mv.name_jp] += 1
        for l in b.logs:
            for k in WATCH:
                if ("【" + k + "】を確認") in l: used[k] += 1
    except Exception:
        pass
    return held, used

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(3)
    jobs = []
    for _ in range(N):
        i, j = rng.sample(range(n), 2)
        jobs.append((pool[i], pool[j], rng.randrange(10 ** 6)))
    print(f"各sims {N}戦 / 設置・状態異常技の使用率\n")
    print(f"{'sims':>6} | " + " | ".join(f"{k}" for k in WATCH))
    for sims in SIMS_LIST:
        _W["sims"] = sims
        held = {k: 0 for k in WATCH}; used = {k: 0 for k in WATCH}
        t0 = time.time()
        with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
            for h, u in p.imap_unordered(_job, jobs, chunksize=4):
                for k in WATCH: held[k] += h[k]; used[k] += u[k]
        cells = []
        for k in WATCH:
            r = used[k] / held[k] if held[k] else 0
            cells.append(f"{r:.2f}({used[k]}/{held[k]})")
        print(f"{sims:>6} | " + " | ".join(cells) + f"  [{time.time()-t0:.0f}s]", flush=True)

if __name__ == "__main__":
    main()
