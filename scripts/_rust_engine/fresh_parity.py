"""記録コーパスを使わない Python↔Rust パリティ検証。

記録済みケースは「記録時点の Python の期待値」なので、仕様を意図的に変えると
エンジンが正しくてもゲートが赤くなる（case_stamp.py の docstring 参照）。
そのときに「両実装が新しい仕様で一致しているか」を直接確かめるための検証。

同じ (パーティ, 選出, シード) を ENGINE=python と ENGINE=rust で走らせ、勝敗を突き合わせる。
greedy_3v3 / mcts_3v3 の両方を対象にできる。

**mcts は正しいオラクルにならない**。R4-G3 の記録ゲートは Rust の逐次 forward に
合わせて Python 側を seqnet（逐次順オラクル）＋ sorted belief に正規化して比較している。
この検証は本番構成の numpy ネットをそのまま使うため、値の最終ビット差（max|Δ|=8.9e-16）が
接戦の MCTS 判断をまれに反転させ、フィルタの有無に関係なく 2割前後ずれる（実測: やまあらし党
7/40、無フィルタ 8/40 ＝ 同率）。ネットを通さない greedy が意味のある検証対象。

env: N(120) SIMS(120) POOL_SEASON(M-6) PARTIES(suggest_cache.json) FN(greedy|mcts|both)
     FILTER(技名や特性名。含むパーティだけを対象にする) SELFCHECK(1=Python自己再現も測る)
"""
import os, sys, json, random, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1")

SEASON = os.environ.get("POOL_SEASON", "M-6")
PARTIES = os.environ.get("PARTIES", "suggest_cache.json")
N = int(os.environ.get("N", "120"))
SIMS = int(os.environ.get("SIMS", "120"))
FN = os.environ.get("FN", "greedy")
FILTER = os.environ.get("FILTER") or None


def _run(engine, fn, jobs):
    """子プロセスで ENGINE を固定して実行（engine_dispatch は import 時に ENGINE を読む）。"""
    import subprocess
    code = (
        "import os,sys,json\n"
        "os.environ['OMP_NUM_THREADS']='1'\n"
        f"os.environ['ENGINE']={engine!r}\n"
        f"os.environ['POOL_SEASON']={SEASON!r}\n"
        f"os.environ.setdefault('GA_SIMS',{str(SIMS)!r})\n"
        "jobs=json.load(sys.stdin)\n"
        + ("from _v3_rollout import _greedy_3v3 as F\n" if fn == "greedy"
           else "from _v3_final import _mcts_3v3 as F\n")
        + "print(json.dumps([F(tuple(j)) for j in jobs]))\n")
    # PYTHONHASHSEED はプロセス跨ぎで belief.py の集合順を変え、Python側が非決定的になる
    env = dict(os.environ, PYTHONHASHSEED="0")
    p = subprocess.run([sys.executable, "-c", code], input=json.dumps(jobs),
                       capture_output=True, text=True, env=env,
                       cwd=os.path.dirname(os.path.abspath(__file__)) + "/..")
    if p.returncode != 0:
        raise RuntimeError(p.stderr[-800:])
    return json.loads(p.stdout.strip().splitlines()[-1])


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
    import _m6_pool
    P = _m6_pool.load_parties(PARTIES)
    if FILTER:
        P = [sp for sp in P if any(FILTER in s for s in sp)]
    if len(P) < 2:
        sys.exit(f"対象パーティが足りない（FILTER={FILTER} で {len(P)}党）")
    rng = random.Random(20260914)
    jobs = []
    for i in range(N):
        a, b = rng.sample(range(len(P)), 2)
        sa = sorted(rng.sample(range(6), 3)); sb = sorted(rng.sample(range(6), 3))
        jobs.append([P[a], sa, P[b], sb, rng.randrange(1, 2 ** 31 - 1)])
    print(f"■ fresh parity: season={SEASON} {len(P)}党 {N}戦 sims={SIMS} "
          f"filter={FILTER or 'なし'}", flush=True)
    ok = True
    for f in (("greedy", "mcts") if FN == "both" else (FN,)):
        py = _run("python", f, jobs)
        if os.environ.get("SELFCHECK") == "1":
            py2 = _run("python", f, jobs)
            nb = sum(1 for x, y in zip(py, py2) if x != y)
            print(f"  {f:6s}: Python自己再現 {len(py)-nb}/{len(py)}" + ("" if not nb else "  ✗非決定的"), flush=True)
        ru = _run("rust", f, jobs)
        bad = [i for i, (x, y) in enumerate(zip(py, ru)) if x != y]
        print(f"  {f:6s}: 一致 {len(py)-len(bad)}/{len(py)}" +
              (f"  ✗ 乖離 {len(bad)}件 index={bad[:8]}" if bad else "  ✓"), flush=True)
        ok = ok and not bad
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
