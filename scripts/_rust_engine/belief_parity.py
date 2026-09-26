"""信念（相手の型の推定）の更新が Python と Rust で 1:1 か、同じ対戦を流して突き合わせる。
MCTS の fresh parity は numpy/逐次の数値差で約2割ずれる既知ドリフトがあり、信念の不一致を
見分けられない。greedy 対戦に両側の信念を付けて走らせ、終局後の P1 の信念を直接比べる。
比べるもの: EV/性格候補の事後分布・型プールの重み・判明技・判明持ち物・持ち物喪失・発動しなかった持ち物
env: N(40) PARTIES(ab_pool_new.json) POOL_SEASON(M-6)
"""
import json, os, random, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
N = int(os.environ.get("N", "40"))


def _child(engine, jobs):
    code = r'''
import os, sys, json, random as _r
sys.path.insert(0, ".")
os.environ["OMP_NUM_THREADS"] = "1"
jobs = json.load(sys.stdin)
S = os.environ.get("POOL_SEASON", "M-6")
out = []
if os.environ["ENGINE"] == "rust":
    os.environ["BELIEF_PROBE"] = "1"
    import pokenavi_engine as E
    for pa, sa, pb, sb, seed in jobs:
        E.greedy_3v3(pa, sa, pb, sb, seed, S)
        out.append([[n, post, pw, km, ki, lost, sorted(ab)] for n, post, pw, km, ki, lost, ab in E.belief_probe_take()])
else:
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import GreedyAI, certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    L = get_loader()
    for pa, sa, pb, sb, seed in jobs:
        _r.seed(seed); f = BF()
        A = [bfs(pps(s), L, season=S, randomize=True) for s in pa]
        B = [bfs(pps(s), L, season=S, randomize=True) for s in pb]
        def order(P, sub):
            mons = [P[i] for i in sub]; ld = max(range(3), key=lambda j: espd(mons[j], f))
            return [mons[ld]] + [mons[j] for j in range(3) if j != ld]
        s1 = BattleSide(order(A, sa), viewer_label="P1", source6=A); s2 = BattleSide(order(B, sb), viewer_label="P2", source6=B)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        g1 = GreedyAI(); g2 = GreedyAI()
        Battle(s1, s2, BF()).run(lambda m, o, ff: certain_ko_override(g1(m, o, ff), m, o, ff),
                                 lambda m, o, ff: certain_ko_override(g2(m, o, ff), m, o, ff))
        rows = []
        from simulator.belief import pool_builds_by_species
        pool = pool_builds_by_species()
        for n, pb_ in s1.belief.species.items():
            if not pb_.builds and n in pool:
                pb_.builds = pool[n]
            pw = list(pb_.pool_weights()) if pb_.builds else []
            rows.append([n, list(pb_.post), pw, sorted(pb_.known_moves), pb_.known_item,
                         bool(pb_.item_lost), sorted(pb_.absent_items)])
        out.append(rows)
print(json.dumps(out, ensure_ascii=False))
'''
    env = dict(os.environ, ENGINE=engine, PYTHONHASHSEED="0")
    p = subprocess.run([sys.executable, "-c", code], input=json.dumps(jobs), capture_output=True,
                       text=True, env=env, cwd=os.path.dirname(HERE))
    if p.returncode != 0:
        raise RuntimeError(p.stderr[-1500:])
    return json.loads(p.stdout.strip().splitlines()[-1])


def main():
    sys.path.insert(0, os.path.dirname(HERE))
    import _m6_pool
    P = _m6_pool.load_parties(os.environ.get("PARTIES", "ab_pool_new.json"))
    rng = random.Random(20260925)
    jobs = []
    for _ in range(N):
        a, b = rng.sample(range(len(P)), 2)
        jobs.append([P[a], sorted(rng.sample(range(6), 3)), P[b], sorted(rng.sample(range(6), 3)),
                     rng.randrange(1, 2 ** 31 - 1)])
    py, ru = _child("python", jobs), _child("rust", jobs)
    bad = 0
    for gi, (a, b) in enumerate(zip(py, ru)):
        msg = None
        if [r[0] for r in a] != [r[0] for r in b]:
            msg = f"種の並び {[r[0] for r in a]} vs {[r[0] for r in b]}"
        else:
            for x, y in zip(a, b):
                for k, lab in ((1, "EV/性格の事後"), (2, "型プール重み")):
                    if len(x[k]) != len(y[k]) or any(abs(p - q) > 1e-9 for p, q in zip(x[k], y[k])):
                        d = max((abs(p - q) for p, q in zip(x[k], y[k])), default=-1)
                        msg = f"{x[0]} {lab} 長さ{len(x[k])}/{len(y[k])} 最大差{d:.3g}"
                        break
                if msg:
                    break
                for k, lab in ((3, "判明技"), (4, "判明持ち物"), (5, "持ち物喪失"), (6, "発動しなかった持ち物")):
                    if x[k] != y[k]:
                        msg = f"{x[0]} {lab} {x[k]} vs {y[k]}"
                        break
                if msg:
                    break
        if msg:
            bad += 1
            if bad <= 8:
                print(f"  ✗ 対戦{gi}: {msg}")
    print(f"■ 信念パリティ {N}戦: 一致 {N - bad}/{N}" + ("  ✓" if not bad else ""))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
