"""『不利→有利の交代が自明なのに交代しない』見逃しケースを抽出（M-1テンプレ上）。
各決定で、生存考慮の良い交代先(survivableで殴り返せる有利対面)が存在するのに、
AIがその交代を選ばなかった場合を記録。AIの実際の行動（技/ピボット/別交代）も併記。
NET_PATH 環境変数で評価ネットを指定。
"""
import os, json, glob, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120")); NPROC = int(os.environ.get("NPROC", "12"))
NET_PATH = os.environ.get("NET_PATH", "az_net_np.json")
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(NET_PATH), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _best_switch(my, opp, f):
    from simulator.battle import is_trapped
    from simulator.ai import _effective_speed
    from simulator.features import _expected_frac
    me = my.active; o = opp.active
    if me is None or o is None or not me.is_alive or not o.is_alive: return None
    if is_trapped(me, o): return None
    my_in = _expected_frac(o, me, f, my)
    if my_in < 0.45: return None
    if _expected_frac(me, o, f, opp) >= 1.0 and _effective_speed(me, f) > _effective_speed(o, f): return None
    ospd = _effective_speed(o, f); best = None; bg = 0.0; info = None
    for j, b in enumerate(my.party):
        if j == my.active_idx or not b.is_alive: continue
        in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
        hp = b.hp / max(1, b.max_hp); need = 1 if _effective_speed(b, f) > ospd else 2
        if in_f <= my_in - 0.2 and out_f >= 0.8 and hp > in_f * need and out_f - in_f > bg:
            bg = out_f - in_f; best = j; info = (b.name, round(my_in, 2), round(_expected_frac(me, o, f, opp), 2), round(in_f, 2), round(out_f, 2))
    return (best, info) if best is not None else None

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    missed = []; opp_count = [0, 0]   # [自明交代局面数, うち見逃し]
    def wrap(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        bs = _best_switch(my, opp, f)
        if bs is not None:
            j, info = bs; opp_count[0] += 1
            took = (getattr(a, "type", None) == "switch" and a.switch_to == j)
            if not took:
                opp_count[1] += 1
                if getattr(a, "type", None) == "switch":
                    act_s = "別交代→" + my.party[a.switch_to].name
                elif a.move and a.move.name_jp in PIVOT:
                    act_s = "ピボット:" + a.move.name_jp
                elif a.move:
                    act_s = "技:" + a.move.name_jp
                else:
                    act_s = str(getattr(a, "type", "?"))
                nm, myin, myout, inf, outf = info
                missed.append((my.active.name, opp.active.name, myin, myout, nm, inf, outf, act_s))
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception: pass
    return missed, opp_count

def main():
    parties = [json.load(open(f))["subject_party"] for f in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6)) for a, b in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"NET={NET_PATH} / M-1テンプレ {N}戦 MCTS@{SIMS}", flush=True)
    allm = []; tot = 0; miss = 0
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for m, c in p.map(_job, jobs):
            allm += m; tot += c[0]; miss += c[1]
    print(f"自明な不利→有利交代の局面 {tot} / 交代せず見逃し {miss} ({miss*100//max(1,tot)}%)\n")
    print("【見逃し例】 交代元 vs 相手(被{被}/与{与}) → 本来の交代先(被{被}/与{与}) ／ AIの実際の行動")
    for c in allm[:14]:
        print(f"  {c[0]} vs {c[1]} (被{c[2]}/与{c[3]}) → {c[4]} (被{c[5]}/与{c[6]})  ／ 実際: {c[7]}")

if __name__ == "__main__":
    main()
