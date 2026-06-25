"""速度・残HP・生存を考慮した改良交代ヒューリスティックの検証。
交代先が『攻撃機会を得るまで生き残れるか』で判定：速いなら1発、遅いなら2発耐えられること。
naive版(対面のみ)が有利と誤判定した交代のうち、改良版が「生存不可＝活かせない」と棄却する例も示す。
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
    from simulator.battle import BattleSide, Battle, is_trapped
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override, Action, _effective_speed
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    accepted = []; rejected = []
    def evalbench(my, opp, f):
        """(改良判定の最良交代先 or None, naiveなら有利だが生存不可で棄却した例list)"""
        me = my.active; o = opp.active
        rej = []
        if me is None or o is None or not me.is_alive or not o.is_alive: return None, rej
        if is_trapped(me, o): return None, rej
        my_in = _expected_frac(o, me, f, my)
        if my_in < 0.45: return None, rej                         # 危険でない
        if _expected_frac(me, o, f, opp) >= 1.0 and _effective_speed(me, f) > _effective_speed(o, f):
            return None, rej                                      # 自分が先制でKOできる→交代不要
        ospd = _effective_speed(o, f); best = None; bestgain = 0.0
        for j, b in enumerate(my.party):
            if j == my.active_idx or not b.is_alive: continue
            in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
            hp = b.hp / max(1, b.max_hp); faster = _effective_speed(b, f) > ospd
            need = 1 if faster else 2                              # 攻撃機会までに耐える必要のある発数
            survives = hp > in_f * need
            naive_fav = (in_f <= my_in - 0.2 and out_f >= 0.8)    # 旧基準では有利
            if naive_fav and survives and out_f - in_f > bestgain:
                bestgain = out_f - in_f; best = (j, b.name, round(in_f, 2), round(out_f, 2), hp, faster)
            elif naive_fav and not survives:                      # 旧基準=有利だが生存不可→棄却
                rej.append((me.name, o.name, b.name, round(in_f, 2), round(out_f, 2),
                            round(hp, 2), "速い" if faster else "遅い", need))
        return best, rej
    def wrap(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        if getattr(a, "type", None) == "switch": return a
        best, rej = evalbench(my, opp, f)
        rejected.extend(rej)
        if best is not None:
            j, nm, inf, outf, hp, faster = best
            accepted.append((my.active.name, opp.active.name, round(_expected_frac(opp.active, my.active, f, my), 2),
                             nm, inf, outf, round(hp, 2), "速い" if faster else "遅い"))
            return Action(type="switch", switch_to=j)
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception: pass
    return accepted, rejected

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(20)
    jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"{N}戦 MCTS@{SIMS} 改良交代（速度・残HP・生存考慮）", flush=True)
    A = []; R = []
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for a, r in p.map(_job, jobs): A += a; R += r
    print(f"\n=== 改良版が採用した交代（生存し攻撃機会あり）: {len(A)}件 ===")
    for c in A[:15]:
        print(f"  {c[0]}(被{c[2]}) vs {c[1]} → {c[3]} 残HP{int(c[6]*100)}%・{c[7]}・交代後 被{c[4]}/与{c[5]}")
    print(f"\n=== 旧基準では有利だが『攻撃前に落ちる』ので棄却した交代: {len(R)}件 ===")
    for c in R[:15]:
        print(f"  {c[0]} vs {c[1]} → {c[2]} (交代被{c[3]}×{c[7]}発, 残HP{int(c[5]*100)}%, {c[6]}) ＝活かせず棄却")

if __name__ == "__main__":
    main()
