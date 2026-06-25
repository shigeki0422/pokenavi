"""実戦でAIが自発交代したケースを、交代前後の対面（与/被 期待ダメージ）付きで抽出・分類。
不利対面(被ダメ大・与ダメ小)から有利対面(被ダメ小・与ダメ大)への交代が実際に起きているか具体例で見る。
"""
import os, json, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120")); NPROC = int(os.environ.get("NPROC", "12"))
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
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    cases = []
    def wrap(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        if getattr(a, "type", None) == "switch" and a.switch_to is not None:
            me = my.active; o = opp.active; nu = my.party[a.switch_to]
            if me and o and nu and o.is_alive:
                try:
                    cases.append((me.name, o.name, nu.name,
                                  round(_expected_frac(o, me, f, my), 2), round(_expected_frac(me, o, f, opp), 2),
                                  round(_expected_frac(o, nu, f, my), 2), round(_expected_frac(nu, o, f, opp), 2)))
                except Exception: pass
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception: pass
    return cases

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(20)
    jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"{N}戦 MCTS@{SIMS} で自発交代ケースを抽出", flush=True)
    allc = []
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for cs in p.map(_job, jobs): allc += cs
    # 分類: 交代前(被in_old,与out_old) → 交代後(被in_new,与out_new)
    unf_to_fav = [c for c in allc if c[3] >= 0.45 and c[5] <= c[3] - 0.2 and c[6] >= c[4]]
    print(f"\n自発交代 計{len(allc)}件 / うち『不利→有利』判定 {len(unf_to_fav)}件\n")
    print("【不利→有利 交代の実例】 形式: 交代元@相手(被{被ダメ}/与{与ダメ}) → 交代先(被{被}/与{与})")
    for c in unf_to_fav[:12]:
        print(f"  {c[0]} vs {c[1]} (被{c[3]}/与{c[4]}) → {c[2]} (被{c[5]}/与{c[6]})")
    print("\n【その他の自発交代（不利→有利でない）例】")
    others = [c for c in allc if c not in unf_to_fav]
    for c in others[:8]:
        print(f"  {c[0]} vs {c[1]} (被{c[3]}/与{c[4]}) → {c[2]} (被{c[5]}/与{c[6]})")

if __name__ == "__main__":
    main()
