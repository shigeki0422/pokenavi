"""現行モデル自身の交代 と 賢い交代ヒューリスティックが追加した交代 を分離列挙。
各決定で base(現行AI) と smart(base+賢い交代) を両方計算し、
 - base が交代 → 現行モデルが既に出来ている交代
 - base は技だが smart が交代 → 賢い交代で新たに発生した交代
を対面情報付きで記録する。対戦は smart で進める（現実的に継続）。
"""
import os, json, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120")); NPROC = int(os.environ.get("NPROC", "12"))
MARGIN = float(os.environ.get("MARGIN", "0.5"))
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
    from simulator.battle import BattleSide, Battle, is_trapped
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override, Action
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    model_sw = []; smart_sw = []
    def ctx(me, o, nu, f, my, opp):
        return (me.name, o.name, nu.name,
                round(_expected_frac(o, me, f, my), 2), round(_expected_frac(me, o, f, opp), 2),
                round(_expected_frac(o, nu, f, my), 2), round(_expected_frac(nu, o, f, opp), 2))
    def smart(a, my, opp, f):
        me = my.active; o = opp.active
        if me is None or o is None or not me.is_alive or not o.is_alive: return a
        if getattr(a, "type", None) == "switch" or is_trapped(me, o): return a
        my_in = _expected_frac(o, me, f, my)
        if my_in < 0.45: return a
        cur = _expected_frac(me, o, f, opp) - my_in; best = None; bs = cur
        for j, p in enumerate(my.party):
            if j == my.active_idx or not p.is_alive: continue
            sc = _expected_frac(p, o, f, opp) - _expected_frac(o, p, f, my)
            if sc > bs + MARGIN: bs = sc; best = j
        return Action(type="switch", switch_to=best) if best is not None else a
    def wrap(my, opp, f):
        ab = certain_ko_override(ai0(my, opp, f), my, opp, f)
        if getattr(ab, "type", None) == "switch" and ab.switch_to is not None:
            nu = my.party[ab.switch_to]
            if my.active and opp.active and nu and opp.active.is_alive:
                try: model_sw.append(ctx(my.active, opp.active, nu, f, my, opp))
                except Exception: pass
            return ab
        asm = smart(ab, my, opp, f)
        if getattr(asm, "type", None) == "switch" and asm.switch_to is not None:
            nu = my.party[asm.switch_to]
            if my.active and opp.active and nu and opp.active.is_alive:
                try: smart_sw.append(ctx(my.active, opp.active, nu, f, my, opp))
                except Exception: pass
        return asm
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception: pass
    return model_sw, smart_sw

def fmt(c): return f"{c[0]} vs {c[1]} (被{c[3]}/与{c[4]}) → {c[2]} (被{c[5]}/与{c[6]})"

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(20)
    jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"{N}戦 MCTS@{SIMS}", flush=True)
    M = []; S = []
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for m, s in p.map(_job, jobs): M += m; S += s
    print(f"\n=== ① 現行モデルが既に行った交代: {len(M)}件 ===")
    for c in M[:20]: print("  " + fmt(c))
    print(f"\n=== ② 賢い交代ヒューリスティックが新たに発生させた交代: {len(S)}件 ===")
    for c in S[:20]: print("  " + fmt(c))

if __name__ == "__main__":
    main()
