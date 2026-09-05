"""TS の 1v1 判定（engine/wasm 経由）が Python(正本) と一致することの検証。

`_mu_engine` の数値そのものは `_rust_engine/verify_wasm.mjs` が突き合わせている。
こちらが見るのは TS 側の繋ぎ込み——ResolvedBuild から spec を組む処理、
採用率プール(最大10技)の扱い、最大打点技の選び方——が正本と同じ結果になるか。

実行:
    cd pokenavi && scripts/venv/bin/python scripts/tests/test_ts_engine.py
env: NPAIR(400)
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", "1")


def ts_output() -> list:
    out = os.path.join(tempfile.mkdtemp(), "eng.mjs")
    subprocess.run(
        ["npx", "esbuild", "scripts/tests/ts_engine_check.ts", "--bundle",
         "--platform=node", "--format=esm", f"--outfile={out}", "--log-level=warning"],
        cwd=ROOT, check=True,
    )
    r = subprocess.run(["node", out], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(r.stdout)


def check_named(named, bad):
    """報告のあった表示バグの回帰確認。
    カバルドンのじしん→ミミッキュ が「18〜18% 確3」と出ていた。18% の正体は
    ばけのかわの身代わり(HPの1/8=16) ＋ すなあらしの削り(1/16=8) で、技のダメージではない。
    乱数に依らない値なので下限と上限も同じになっていた。"""
    d = (named or {}).get("kabaVsMimi")
    if not d:
        bad.append("カバルドンのじしん→ミミッキュ が取得できない")
        return
    hp = named["mimiHp"]
    if d["dmgLo"] == d["dmgHi"]:
        bad.append(f"じしんの与ダメに乱数幅が無い: {d['dmgLo']}〜{d['dmgHi']}")
    if d["dmgLo"] <= hp // 8 + hp // 16:
        bad.append(f"じしんの与ダメが小さすぎる（1ターンのHP減少を表示している疑い）: {d['dmgLo']}")
    if d["hits"] and d["hits"] > 1 and not d["reason"]:
        bad.append("ばけのかわで発数が増えているのに要因が注記されていない")


def main() -> int:
    payload = ts_output()
    recs = payload["pairs"]
    os.chdir(os.path.join(ROOT, "scripts"))
    import feature1 as _f1

    _f1._ensure_loaded("M-3", 8)
    L = _f1._W["loader"]
    import _explain as E
    import _mu_engine as ME
    from simulator.ai import _effective_speed

    ME._LOADER[0] = L

    bad: list[str] = []
    check_named(payload.get("named"), bad)
    for r in recs:
        sa, sb = r["specA"], r["specB"]
        ah, _ar, am = ME._best_cached(sa, sb, 0, id(L))
        bh, _br, bm = ME._best_cached(sa, sb, 1, id(L))
        field, A, B = E._enter(E._build(sa, L), E._build(sb, L))
        aspd, bspd = _effective_speed(A, field), _effective_speed(B, field)
        tag = f"{sa.split('@')[0]} vs {sb.split('@')[0]}"
        if r["myHits"] != ah:
            bad.append(f"{tag}: 自分の確定数 py={ah} ts={r['myHits']}")
        if r["oppHits"] != bh:
            bad.append(f"{tag}: 相手の確定数 py={bh} ts={r['oppHits']}")
        if r["myMove"] != am:
            bad.append(f"{tag}: 自分の最大打点技 py={am} ts={r['myMove']}")
        if r["oppMove"] != bm:
            bad.append(f"{tag}: 相手の最大打点技 py={bm} ts={r['oppMove']}")
        if r["myS"] != aspd:
            bad.append(f"{tag}: 自分の実効素早さ py={aspd} ts={r['myS']}")
        if r["oppS"] != bspd:
            bad.append(f"{tag}: 相手の実効素早さ py={bspd} ts={r['oppS']}")

    print(f"\n=== TS(engine経由) vs Python(正本) ===")
    print(f"  一致 {len(recs) - len({b.split(':')[0] for b in bad})}/{len(recs)} 対面 "
          f"/ 不一致 {len(bad)}項目")
    for b in bad[:20]:
        print(f"      {b}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
