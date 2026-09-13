"""R4追加ゲート: mcts_vs_dist（select_party temp0.3 込み）の Python/Rust パリティ。

他のゲートと違い記録ケースを使わない。同じ入力で Python(正本) と Rust(pokenavi_engine)
をその場で両方走らせ、勝敗結果を突き合わせる。select_party を内部で呼ぶのは
mcts_vs_dist だけで、選出の乱数消費まで含めた一致はここでしか見られない。

呼ぶのは cargo の gate バイナリではなく venv に入った .so なので、run_gates.sh は
直前に必ず maturin develop で作り直すこと（古い .so が「Rustの乖離」に化ける）。

使い方: scripts/ を cwd にして  venv/bin/python _rust_engine/gate_r4_vsdist.py
env:
  VD_N       検査ケース数（既定 40）
  VD_SEASON  対象シーズン（既定 POOL_SEASON、無ければ M-3）
  VD_SIMS    MCTSシミュレーション数（既定 GA_SIMS=120）
  VD_SRC     パーティ供給元 jsonl/json。既定は suggest_cache.json の提案パーティ
  VD_SHOW    不一致の表示件数（既定 10）
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
os.chdir(ROOT)

SEASON = os.environ.get("VD_SEASON") or os.environ.get("POOL_SEASON") or "M-3"
os.environ["POOL_SEASON"] = SEASON
os.environ.setdefault("OMP_NUM_THREADS", "1")
SIMS = int(os.environ.get("VD_SIMS") or os.environ.get("GA_SIMS", "120"))
os.environ["GA_SIMS"] = str(SIMS)


def _parties():
    """6体パーティのspec列を集める。決定的に並べてからシードで抽出する。"""
    src = os.environ.get("VD_SRC") or os.path.join(ROOT, "suggest_cache.json")
    cache = json.load(open(src, encoding="utf-8"))
    out = []
    for key in sorted(cache):
        for r in cache[key]["results"]:
            sp = r.get("specs")
            if sp and len(sp) == 6:
                out.append(list(sp))
    return out


def main():
    n = int(os.environ.get("VD_N", "40"))
    show = int(os.environ.get("VD_SHOW", "10"))

    import engine_dispatch as ED
    if ED.rust() is None:
        sys.exit("gate_r4_vsdist: Rustエンジンが無効。"
                 " maturin develop で pokenavi_engine を入れ、ENGINE=rust で実行せよ")

    import _o1_policy as P
    if P.SEASON != SEASON:
        sys.exit(f"gate_r4_vsdist: _o1_policy が別シーズンで読み込まれている"
                 f" ({P.SEASON} != {SEASON})")

    pool = _parties()
    if len(pool) < 2:
        sys.exit(f"gate_r4_vsdist: パーティが足りない ({len(pool)}件)")
    rng = random.Random(4_040_000)
    cases = []
    for i in range(n):
        pa = pool[rng.randrange(len(pool))]
        pb = pool[rng.randrange(len(pool))]
        sa = sorted(rng.sample(range(6), 3))
        seed = rng.randrange(1, 0x7fffffff)
        cases.append((pa, sa, pb, seed))

    print(f"gate_r4_vsdist: season={SEASON} sims={SIMS} cases={n}", flush=True)
    bad = 0
    shown = 0
    for i, (pa, sa, pb, seed) in enumerate(cases):
        rv = ED.call("mcts_vs_dist", list(pa), list(sa), list(pb), seed, SIMS, SEASON)
        if rv is None:
            sys.exit("gate_r4_vsdist: Rust呼び出しが None を返した"
                     "（未対応コンフィグ＝env ガードに引っかかっている）。"
                     f" unsupported={ED.unsupported_config('mcts_vs_dist')}")
        saved = P._ENGINE
        P._ENGINE = "python"
        try:
            pv = P._mcts_vs_dist((pa, sa, pb, seed))
        finally:
            P._ENGINE = saved
        if rv != pv:
            bad += 1
            if shown < show:
                shown += 1
                print(f"  ✗ case{i} seed={seed} rust={rv} python={pv}")
                print(f"      A={[s.split('@')[0] for s in pa]} sel={sa}")
                print(f"      B={[s.split('@')[0] for s in pb]}")
        if (i + 1) % 10 == 0:
            print(f"  {i + 1}/{n} 乖離{bad}", flush=True)
    if bad:
        sys.exit(f"gate_r4_vsdist: 乖離 {bad}/{n} 件")
    print(f"gate_r4_vsdist: OK 乖離0 ({n}件)")


if __name__ == "__main__":
    main()
