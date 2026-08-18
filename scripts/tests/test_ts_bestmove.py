"""bestMove(src/scripts/party-builder/damage.ts)の技選定基準の検証。

「1発目のダメージが最大の技」ではなく「その技を撃ち続けた時の確定数が最小の技」を
選ぶこと（りゅうせいぐん等の自己ランク低下技で1発目基準が誤る問題の回帰テスト）。

実行:
    cd pokenavi && scripts/venv/bin/python scripts/tests/test_ts_bestmove.py
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main() -> int:
    out = os.path.join(tempfile.mkdtemp(), "bm.mjs")
    subprocess.run(
        ["npx", "esbuild", "scripts/tests/ts_bestmove_check.ts", "--bundle",
         "--platform=node", "--format=esm", f"--outfile={out}", "--log-level=warning"],
        cwd=ROOT, check=True,
    )
    res = json.loads(subprocess.run(["node", out], cwd=ROOT, check=True, capture_output=True, text=True).stdout)
    ng = [r for r in res if not r["ok"]]
    for r in ng:
        print(f"  FAIL: {r['name']} → {r['detail']}")
    print(f"結果: {len(res) - len(ng)}件 PASS / {len(ng)}件 FAIL  (計{len(res)}件)")
    return 1 if ng else 0


if __name__ == "__main__":
    sys.exit(main())
