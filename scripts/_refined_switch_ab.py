"""生存考慮版の交代ヒューリスティック vs 現行ネット のA/B（勝率影響）。
不利対面で、控えが『速いなら1発/遅いなら2発』耐えて攻撃機会を得られる有利対面があれば交代。
活かせない（攻撃前に落ちる）なら交代しない＝死に出し優先。
"""
import os, json, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "300")); NPROC = int(os.environ.get("NPROC", "12"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed, refined = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, is_trapped
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override, Action, _effective_speed
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def base(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def refined_switch(a, my, opp, f):
        me = my.active; o = opp.active
        if me is None or o is None or not me.is_alive or not o.is_alive: return a
        if getattr(a, "type", None) == "switch" or is_trapped(me, o): return a
        my_in = _expected_frac(o, me, f, my)
        if my_in < 0.45: return a
        if _expected_frac(me, o, f, opp) >= 1.0 and _effective_speed(me, f) > _effective_speed(o, f): return a
        ospd = _effective_speed(o, f); best = None; bg = 0.0
        for j, b in enumerate(my.party):
            if j == my.active_idx or not b.is_alive: continue
            in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
            hp = b.hp / max(1, b.max_hp); need = 1 if _effective_speed(b, f) > ospd else 2
            if in_f <= my_in - 0.2 and out_f >= 0.8 and hp > in_f * need and out_f - in_f > bg:
                bg = out_f - in_f; best = j
        return Action(type="switch", switch_to=best) if best is not None else a
    def A1(my, opp, f):
        a = base(my, opp, f)
        return refined_switch(a, my, opp, f) if refined else a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        w = Battle(s1, s2).run(A1, base)
        return 1 if w == 1 else 0
    except Exception:
        return None

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(7)
    base_jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"生存考慮版交代 A/B {N}戦×2アーム MCTS@{SIMS}", flush=True)
    res = {}
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for refined in (False, True):
            jobs = [(a, b, s, refined) for (a, b, s) in base_jobs]
            t0 = time.time(); wins = tot = 0
            for w in p.map(_job, jobs):
                if w is None: continue
                tot += 1; wins += w
            res[refined] = (wins, tot)
            print(f"{'生存考慮版交代' if refined else '通常(現行ネット)'}: {wins}/{tot} = {wins/max(1,tot)*100:.1f}%  [{time.time()-t0:.0f}s]", flush=True)
    a = res[False][0]/max(1,res[False][1]); b = res[True][0]/max(1,res[True][1])
    print(f"\n通常 {a*100:.1f}% → 生存考慮版 {b*100:.1f}%  差 {(b-a)*100:+.1f}pt")

if __name__ == "__main__":
    main()
