"""AIの「相手の型の読み」（simulator/predict.py ↔ Rust predict.rs）が Python と Rust で一致するか。
greedy 対戦に両側の信念を付けて走らせ、各ターン終了時の両AIの読みを突き合わせる（belief_parity.py と同じ作り）。
数値は小数4桁に丸めた値を 2e-4 の許容で比べる（丸め境界の差だけを許す）。
env: N(40) PARTIES(ab_pool_new.json) POOL_SEASON(M-6) JOINT_BUILD(既定1。0/1: used の判定と信念の型プール)
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
    os.environ["BELIEF_PROBE"] = "1"; os.environ["PREDICT_PROBE"] = "1"
    import pokenavi_engine as E
    for pa, sa, pb, sb, seed in jobs:
        E.greedy_3v3(pa, sa, pb, sb, seed, S)
        out.append([[t, json.loads(a), json.loads(b)] for t, a, b in E.predict_probe_take()])
else:
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec as bfs, parse_pokemon_spec as pps
    from simulator.ai import GreedyAI, certain_ko_override, _effective_speed as espd
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField as BF
    from simulator.predict import Predictor
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
        g1 = GreedyAI(); g2 = GreedyAI(); P = Predictor(L); rows = []
        def cb(b):
            rows.append([b.turn, P.snapshot(b.side1, b.side2), P.snapshot(b.side2, b.side1)])
        Battle(s1, s2, BF()).run(lambda m, o, ff: certain_ko_override(g1(m, o, ff), m, o, ff),
                                 lambda m, o, ff: certain_ko_override(g2(m, o, ff), m, o, ff), on_turn=cb)
        out.append(json.loads(json.dumps(rows, ensure_ascii=False)))
print(json.dumps(out, ensure_ascii=False))
'''
    env = dict(os.environ, ENGINE=engine, PYTHONHASHSEED="0")
    p = subprocess.run([sys.executable, "-c", code], input=json.dumps(jobs), capture_output=True,
                       text=True, env=env, cwd=os.path.dirname(HERE))
    if p.returncode != 0:
        raise RuntimeError(p.stderr[-1500:])
    return json.loads(p.stdout.strip().splitlines()[-1])


def diff(a, b, path="") -> str:
    """最初の食い違いの場所。数値は 2e-4 まで同じとみなす。"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool):
        return "" if abs(a - b) <= 2e-4 else f"{path}: {a} vs {b}"
    if type(a) != type(b):
        return f"{path}: 型 {type(a).__name__} vs {type(b).__name__} ({a!r} / {b!r})"
    if isinstance(a, dict):
        if set(a) != set(b):     # Rust の serde_json はキー順を保たない（JSON のオブジェクトとして比べる）
            return f"{path}: キー {sorted(a)} vs {sorted(b)}"
        for k in a:
            d = diff(a[k], b[k], f"{path}.{k}")
            if d:
                return d
        return ""
    if isinstance(a, list):
        if len(a) != len(b):
            return f"{path}: 長さ {len(a)} vs {len(b)} ({a} / {b})"
        for i, (x, y) in enumerate(zip(a, b)):
            d = diff(x, y, f"{path}[{i}]")
            if d:
                return d
        return ""
    return "" if a == b else f"{path}: {a!r} vs {b!r}"


def main():
    sys.path.insert(0, os.path.dirname(HERE))
    import _m6_pool
    P = _m6_pool.load_parties(os.environ.get("PARTIES", "ab_pool_new.json"))
    rng = random.Random(20260928)
    jobs = []
    for _ in range(N):
        a, b = rng.sample(range(len(P)), 2)
        jobs.append([P[a], sorted(rng.sample(range(6), 3)), P[b], sorted(rng.sample(range(6), 3)),
                     rng.randrange(1, 2 ** 31 - 1)])
    py, ru = _child("python", jobs), _child("rust", jobs)
    bad = 0; nt = 0
    for gi, (a, b) in enumerate(zip(py, ru)):
        nt += len(a)
        d = diff(a, b, f"対戦{gi}")
        if d:
            bad += 1
            if bad <= 8:
                print("  ✗ " + d[:400])
    print(f"■ 読みのパリティ JOINT_BUILD={os.environ.get('JOINT_BUILD', '1')} {N}戦 {nt}ターン: 一致 {N - bad}/{N}"
          + ("  ✓" if not bad else ""))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
