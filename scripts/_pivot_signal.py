"""学習信号の確認：不利対面で『良い着地が存在するなら必ずピボット』を強制する側 vs 何もしない素の側。
同一ネット同士をM-1テンプレで対戦させ、ピボット強制が勝率を上げるか測る。
上がる→価値ネットに学ばせるべき信号が存在。上がらない→M-1ではピボットの旨味が薄い。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "300")); NPROC = int(os.environ.get("NPROC", "12"))
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

def _force_pivot(a, my, opp, f):
    from simulator.battle import is_trapped
    from simulator.ai import Action, _effective_speed
    from simulator.features import _expected_frac
    me = my.active; o = opp.active
    if me is None or o is None or not me.is_alive or not o.is_alive: return a
    if getattr(a, "type", None) == "switch" or is_trapped(me, o): return a
    my_in = _expected_frac(o, me, f, my)
    if my_in < 0.45: return a
    piv_idx = None
    for i, mv in enumerate(me.moves):
        if mv and mv.name_jp in PIVOT and me.pp[i] > 0:
            if me.choice_locked_move and me.choice_locked_move != mv.name_jp: continue
            piv_idx = i; break
    if piv_idx is None: return a
    ospd = _effective_speed(o, f); good = False
    for j, b in enumerate(my.party):
        if j == my.active_idx or not b.is_alive: continue
        in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
        hp = b.hp / max(1, b.max_hp); need = 1 if _effective_speed(b, f) > ospd else 2
        if in_f < my_in and out_f >= 0.5 and hp > in_f * need:
            good = True; break
    if good:
        return Action(type="move", move=me.moves[piv_idx], move_idx=piv_idx)
    return a

def _job(args):
    pa, pb, seed, force_is_s1 = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def base(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def force(my, opp, f): return _force_pivot(certain_ko_override(ai0(my, opp, f), my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        ai1 = force if force_is_s1 else base
        ai2 = base if force_is_s1 else force
        w = Battle(s1, s2).run(ai1, ai2)
        if w == 0: return 0
        return 1 if ((w == 1) == force_is_s1) else -1
    except Exception:
        return 0

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6), k % 2 == 0)
            for k in range(N) for a, b in [rng.sample(range(n), 2)]]
    print(f"NET={NET_PATH} / ピボット強制 vs 素 / M-1 {N}戦 MCTS@{SIMS}", flush=True)
    fw = bw = dr = 0; t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r in p.map(_job, jobs):
            if r == 1: fw += 1
            elif r == -1: bw += 1
            else: dr += 1
    dec = fw + bw
    print(f"完了 {time.time()-t0:.0f}s")
    print(f"ピボット強制 {fw}勝 / 素 {bw}勝 / 引分 {dr}")
    print(f"ピボット強制の勝率（決着のみ）: {fw*100/max(1,dec):.1f}%")

if __name__ == "__main__":
    main()
