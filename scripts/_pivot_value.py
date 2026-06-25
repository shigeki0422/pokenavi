"""不利対面でピボット持ちの局面ごとに、本番MCTS(regret)が各行動に与えるQ値(=自分の勝率推定)を抽出。
ピボット技 / 攻撃技 / ハード交代 のQを並べ、価値ネットがピボットで作る盤面をどう評価しているか直接見る。
NET_PATH で評価ネット指定。
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

def _root_stats(ai, my, opp, f):
    cands = ai._candidate_actions(my, opp, f)
    if not cands or len(cands) <= 1:
        return None
    root, root_my, _ = ai._build_mcts_root(my, opp, f, cands)
    meN = root["N"][0]; meW = root["W"][0]
    rows = []
    for a in root_my:
        ix = ai._action_index(a)
        n = meN.get(ix, 0)
        q = (meW.get(ix, 0.0) / n) if n else 0.0
        rows.append((a, n, q))
    return rows

def _classify(a):
    t = getattr(a, "type", None)
    if t == "switch":
        return "switch"
    if t == "move" and a.move and a.move.name_jp in PIVOT:
        return "pivot"
    if t == "move":
        return "attack"
    return "other"

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    from simulator.features import _expected_frac
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    # acc: [n局面, sumQ_pivot, sumQ_bestattack, sumQ_bestswitch, pivot最良かつ選択, pivot最良だが非選択]
    acc = [0, 0.0, 0.0, 0.0, 0, 0]
    examples = []
    from simulator.ai import certain_ko_override
    def wrap(my, opp, f):
        me = my.active; o = opp.active
        has_pivot = me is not None and me.is_alive and any(mv and mv.name_jp in PIVOT for mv in me.moves)
        rows = None
        if has_pivot and o is not None and o.is_alive:
            my_in = _expected_frac(o, me, f, my)
            if my_in >= 0.45:
                rows = _root_stats(ai0, my, opp, f)
        if rows:
            chosen = max(rows, key=lambda r: r[1] + r[2])[0]
            piv = [(n, q, a) for a, n, q in rows if _classify(a) == "pivot"]
            atk = [(n, q, a) for a, n, q in rows if _classify(a) == "attack"]
            sw  = [(n, q, a) for a, n, q in rows if _classify(a) == "switch"]
            if piv:
                acc[0] += 1
                qpiv = max(q for _, q, _ in piv)
                qatk = max((q for _, q, _ in atk), default=0.0)
                qsw  = max((q for _, q, _ in sw), default=0.0)
                acc[1] += qpiv; acc[2] += qatk; acc[3] += qsw
                qbest = max(q for _, _, q in rows)
                piv_is_best = (qpiv >= qbest - 1e-9)
                if piv_is_best and _classify(chosen) == "pivot":
                    acc[4] += 1
                elif piv_is_best:
                    acc[5] += 1
                    if len(examples) < 8:
                        pmv = max(piv, key=lambda r: r[1])[2].move.name_jp
                        examples.append((me.name, o.name, round(my_in, 2), pmv,
                                         round(qpiv, 3), round(qatk, 3), round(qsw, 3),
                                         _classify(chosen)))
            return certain_ko_override(chosen, my, opp, f)
        return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
    except Exception:
        pass
    return acc, examples

def chosen_action(ai, my, opp, f, rows):
    from simulator.ai import certain_ko_override
    return certain_ko_override(ai(my, opp, f), my, opp, f)

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6)) for a, b in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"NET={NET_PATH} / M-1テンプレ {N}戦 MCTS@{SIMS}", flush=True)
    T = [0, 0.0, 0.0, 0.0, 0, 0]; allex = []
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for acc, ex in p.map(_job, jobs):
            for k in range(6): T[k] += acc[k]
            allex += ex
    nloc, sp, sa, ss, pb_sel, pb_no = T
    d = max(1, nloc)
    print(f"\n不利対面×ピボット持ちの局面 {nloc}")
    print(f"  平均Q(ピボット)   : {sp/d:.3f}")
    print(f"  平均Q(最良の攻撃) : {sa/d:.3f}")
    print(f"  平均Q(最良ハード交代): {ss/d:.3f}")
    print(f"  （Q=自分の勝率推定[0-1]。高いほど良いと評価）")
    pb = pb_sel + pb_no
    print(f"\nピボットが最良Qの局面 {pb} / うち実際にピボット選択 {pb_sel} / 非選択 {pb_no}")
    if pb: print(f"  ピボット最良なのに選ばない率: {pb_no*100//max(1,pb)}%")
    print("\n【ピボットが最良Qなのに選ばれなかった例】 自分 vs 相手(被{被}) ピボット技 / Q(piv)/Q(atk)/Q(sw) → 実際")
    for c in allex:
        print(f"  {c[0]} vs {c[1]} (被{c[2]}) {c[3]} / {c[4]}/{c[5]}/{c[6]} → 実際:{c[7]}")

if __name__ == "__main__":
    main()
