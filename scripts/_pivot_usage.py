"""ピボット持ちポケモンが『不利対面』でピボットを使う割合を計測（M-1テンプレ）。
単なる回数でなく、ピボット技を持つ個体が、不利対面(被ダメ大)に立った時にピボットで引く条件付き割合。
NET_PATH で評価ネット指定。
"""
import os, json, glob, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "150")); NPROC = int(os.environ.get("NPROC", "12"))
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

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    # counts: [pivot保持で行動した回数, うち不利, うち不利でピボット使用, 不利でハード交代, 不利で攻撃]
    c = [0, 0, 0, 0, 0]
    def wrap(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        me = my.active; o = opp.active
        has_pivot = me is not None and any(mv and mv.name_jp in PIVOT for mv in me.moves)
        if has_pivot and o is not None and o.is_alive and me.is_alive:
            c[0] += 1
            my_in = _expected_frac(o, me, f, my)
            if my_in >= 0.45:                          # 不利対面（被ダメ大）
                c[1] += 1
                t = getattr(a, "type", None)
                if t == "move" and a.move and a.move.name_jp in PIVOT: c[2] += 1
                elif t == "switch": c[3] += 1
                else: c[4] += 1
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception: pass
    return c

def main():
    parties = [json.load(open(f))["subject_party"] for f in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6)) for a, b in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"NET={NET_PATH} / M-1テンプレ {N}戦 MCTS@{SIMS}", flush=True)
    T = [0, 0, 0, 0, 0]
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for c in p.map(_job, jobs):
            for k in range(5): T[k] += c[k]
    tot, unf, piv, hard, atk = T
    print(f"\nピボット持ちの行動 {tot} / うち不利対面 {unf}")
    print(f"不利対面でのピボット持ちの選択内訳（n={unf}）:")
    print(f"  ピボットで引く : {piv} ({piv*100//max(1,unf)}%)")
    print(f"  ハード交代     : {hard} ({hard*100//max(1,unf)}%)")
    print(f"  居座って攻撃等 : {atk} ({atk*100//max(1,unf)}%)")
    print(f"\n＝不利対面で何らか引く率（ピボット＋ハード）: {(piv+hard)*100//max(1,unf)}%")

if __name__ == "__main__":
    main()
