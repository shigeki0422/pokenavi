"""罰する相手(対面的=GreedyAI: 交代せず常に最大期待ダメージの攻撃)に対し、
ピボット強制@400(うまく活用) と 素@400(活用しない) の勝率を比較。
対面的相手はピボットの天敵対象（無傷で受けを出され殴り続ける）なので、ピボットが活きるなら差が出るはず。
差が出る→学習信号あり。出ない→ピボット強化の再学習は無意味。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "200")); NPROC = int(os.environ.get("NPROC", "12"))
NET_PATH = os.environ.get("NET_PATH", "az_net_np.json")
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.ai import GreedyAI
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; net = PVNetNP.load(NET_PATH)
    _W["w"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["pun"] = GreedyAI()

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
    ospd = _effective_speed(o, f)
    for j, b in enumerate(my.party):
        if j == my.active_idx or not b.is_alive: continue
        in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
        hp = b.hp / max(1, b.max_hp); need = 1 if _effective_speed(b, f) > ospd else 2
        if in_f < my_in and out_f >= 0.5 and hp > in_f * need:
            return Action(type="move", move=me.moves[piv_idx], move_idx=piv_idx)
    return a

def _job(args):
    pa, pb, seed, mode, test_is_s1 = args   # mode: "force" or "base", 被験側=test
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; wai = _W["w"]; pun = _W["pun"]; rng = random.Random(seed)
    def base(my, opp, f): return certain_ko_override(wai(my, opp, f), my, opp, f)
    def force(my, opp, f): return _force_pivot(certain_ko_override(wai(my, opp, f), my, opp, f), my, opp, f)
    def punish(my, opp, f): return certain_ko_override(pun(my, opp, f), my, opp, f)
    test = force if mode == "force" else base
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        ai1 = test if test_is_s1 else punish
        ai2 = punish if test_is_s1 else test
        w = Battle(s1, s2).run(ai1, ai2)
        if w == 0: return (mode, 0)
        return (mode, 1 if ((w == 1) == test_is_s1) else -1)
    except Exception:
        return (mode, 0)

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = []
    for mode in ("force", "base"):
        for k in range(N):
            a, b = rng.sample(range(n), 2)
            jobs.append((parties[a], parties[b], rng.randrange(10**6), mode, k % 2 == 0))
    print(f"NET={NET_PATH} / 対面的相手(GreedyAI) に対し ピボット強制@{SIMS} vs 素@{SIMS} / 各{N}戦", flush=True)
    res = {"force": [0, 0, 0], "base": [0, 0, 0]}   # [win,lose,draw]
    t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for mode, r in p.map(_job, jobs):
            if r == 1: res[mode][0] += 1
            elif r == -1: res[mode][1] += 1
            else: res[mode][2] += 1
    print(f"完了 {time.time()-t0:.0f}s")
    for mode in ("force", "base"):
        wn, ls, dr = res[mode]; dec = wn + ls
        nm = "ピボット活用@400" if mode == "force" else "素(活用せず)@400"
        print(f"  {nm} vs 対面的相手: {wn}勝 {ls}敗 {dr}分 / 勝率 {wn*100/max(1,dec):.1f}%")

if __name__ == "__main__":
    main()
