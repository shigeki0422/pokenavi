#!/usr/bin/env python3
"""テストの「恒真（常にパス）アサーション」を検出するlint。

check(label, condition, ...) の condition が構文上ほぼ常に真になる危険パターンを洗い出す。
恒真テストは「緑なのに何も検証していない」最悪の盲点（ふくがんの in (True, False) 型）。
0件を保つ。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 手書き(test_all)＋自動生成(test_move_effects)の両方を走査
SRC = []
for _f in ("test_all.py", "test_move_effects.py"):
    p = ROOT / "tests" / _f
    if p.exists():
        SRC += p.read_text(encoding="utf-8").splitlines()

# (パターン, 説明)。check(...) 行のうち条件部に現れたら恒真の疑い。
PATTERNS = [
    (r"in \((True, False|False, True)\)", "bool ∈ {True,False} は常に真"),
    (r"in \[(True, False|False, True)\]", "bool ∈ [True,False] は常に真"),
    (r"in \{(True, False|False, True)\}", "bool ∈ {True,False} は常に真"),
    (r"\bor True\b", "`or True` で常に真"),
    (r"\bTrue or\b", "`True or` で常に真"),
    (r">=\s*0\b", "`>= 0`（カウント等は常に真の可能性）"),
    (r">\s*-1\b", "`> -1` は常に真の可能性"),
    (r"!=\s*None\s+or\s+.*==\s*None", "is/!= None の網羅で常に真"),
]


def main():
    hits = []
    for i, ln in enumerate(SRC, 1):
        s = ln.strip()
        if not s.startswith("check("):
            continue
        # ラベル（最初の文字列引数）を除いた条件部を対象にする
        m = re.match(r'check\(\s*f?"(?:[^"\\]|\\.)*"\s*,(.*)', s)
        cond = m.group(1) if m else s
        for pat, desc in PATTERNS:
            if re.search(pat, cond):
                hits.append((i, desc, s[:100]))
                break

    print(f"=== テスト恒真アサーション lint（check {sum(1 for l in SRC if l.strip().startswith('check('))}件走査）===\n")
    print(f"【恒真の疑い: {len(hits)}件】")
    for ln, desc, txt in hits:
        print(f"  L{ln} [{desc}]\n      {txt}")
    return len(hits)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
