#!/usr/bin/env python3
"""記事の体裁・構成ルール違反を機械的に検出するCLI（実体は article_style.py）。

使い方:
  python3 scripts/article_style_check.py src/content/blog/garchomp-analysis-m7.md
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from article_style import check_all, allowed  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    args = ap.parse_args()
    text = open(args.path, encoding="utf-8").read()
    lines = text.split("\n")

    findings = check_all(text)
    if not findings:
        print("体裁・構成の既知パターンでの検出なし。")
        return
    print(f"=== {args.path}: {len(findings)}件の検出 ===\n")
    for f in findings:
        mark = ""
        if "style" in allowed(lines[f.line - 1] if 0 < f.line <= len(lines) else ""):
            mark = " (gate:allow)"
        print(f"L{f.line}: [{f.kind}] {f.detail}{mark}")


if __name__ == "__main__":
    main()
