"""「不利→有利（受けに引く）交代」は+EVか？ A/B。
被験側に賢い交代ヒューリスティックを入れる：現役が不利対面(被ダメ大)で、控えに相手の攻撃を
より受けつつ殴り返せる個体がいれば交代。これが勝率を上げるなら、交代自体は+EVで、ネットは
「交代先（有利対面）の評価」ができていないだけ＝直すべきはそこ、と確定する。
"""
import os, json, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "300")); NPROC = int(os.environ.get("NPROC", "12"))
MARGIN = float(os.environ.get("MARGIN", "0.5"))   # 交代で対面優位がこれ以上改善するなら引く
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _smart(act, my, opp, f):
    from simulator.features import _expected_frac
    from simulator.battle import is_trapped
    from simulator.ai import Action
    me = my.active; o = opp.active
    if me is None or o is None or not me.is_alive or not o.is_alive: return act
    if getattr(act, "type", None) == "switch": return act     # 既に交代ならそのまま
    if is_trapped(me, o): return act
    my_in = _expected_frac(o, me, f, my)                        # 自分が受ける期待割合
    my_out = _expected_frac(me, o, f, opp)                      # 自分が与える期待割合
    if my_in < 0.45: return act                                 # 危険でない＝居座る
    cur = my_out - my_in
    best = None; bestscore = cur
    for j, p in enumerate(my.party):
        if j == my.active_idx or not p.is_alive: continue
        b_in = _expected_frac(o, p, f, my); b_out = _expected_frac(p, o, f, opp)
        sc = b_out - b_in
        if sc > bestscore + MARGIN:
            bestscore = sc; best = j
    if best is not None:
        return Action(type="switch", switch_to=best)
    return act

def _job(args):
    pa, pb, seed, smart = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def base(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def A1(my, opp, f):
        a = base(my, opp, f)
        return _smart(a, my, opp, f) if smart else a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        w = Battle(s1, s2).run(A1, base)               # s1=被験側
        return 1 if w == 1 else 0
    except Exception:
        return None

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(7)
    base_jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"賢い交代A/B {N}戦×2アーム MCTS@{SIMS} (margin={MARGIN})", flush=True)
    res = {}
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for smart in (False, True):
            jobs = [(a, b, s, smart) for (a, b, s) in base_jobs]
            t0 = time.time(); wins = tot = 0
            for w in p.map(_job, jobs):
                if w is None: continue
                tot += 1; wins += w
            res[smart] = (wins, tot)
            print(f"{'賢い交代' if smart else '通常'}: {wins}/{tot} = {wins/max(1,tot)*100:.1f}%  [{time.time()-t0:.0f}s]", flush=True)
    a = res[False][0]/max(1,res[False][1]); b = res[True][0]/max(1,res[True][1])
    print(f"\n通常 {a*100:.1f}% → 賢い交代 {b*100:.1f}%  差 {(b-a)*100:+.1f}pt")

if __name__ == "__main__":
    main()
