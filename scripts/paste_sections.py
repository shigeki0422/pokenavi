#!/usr/bin/env python3
"""記事内の生成ブロック（gate:rows）を render_sections.py の最新出力で機械的に置き換える。

使い方: python3 scripts/paste_sections.py <slug>
  1. render_sections.py を実行して _local/article_facts/<slug>.sections.md を作り直す
  2. 記事内の既存の gate:rows ブロックを id ごとに置き換える（文章は触らない）
  3. まだ記事に無いブロックは、id と貼る位置を表示する（最初の1回だけ手で置く）
2026-10-27：書き手が生成器の更新のたびに手で貼り直してトークンを使っていたため、貼り直しを機械化した。
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"<!-- gate:rows start id=(\S+)[^\n]*-->.*?<!-- gate:rows end id=\1 -->", re.S)


def main():
    slug = sys.argv[1]
    facts = ROOT / "_local" / "article_facts" / f"{slug}.json"
    out = ROOT / "_local" / "article_facts" / f"{slug}.sections.md"
    subprocess.run([sys.executable, str(ROOT / "scripts" / "render_sections.py"), "--facts", str(facts), "--out", str(out)],
                   check=True, capture_output=True)
    new = {m.group(1): m.group(0) for m in BLOCK.finditer(out.read_text(encoding="utf-8"))}
    p = ROOT / "src" / "content" / "blog" / f"{slug}.md"
    t = p.read_text(encoding="utf-8")
    seen = []
    t = BLOCK.sub(lambda m: (seen.append(m.group(1)), new.get(m.group(1), m.group(0)))[1], t)
    p.write_text(t, encoding="utf-8")
    missing = [b for b in new if b not in seen and new[b].count("\n") > 1]
    print(f"[paste_sections] 置き換え: {seen}")
    if missing:
        print(f"[paste_sections] 記事に無いブロック（{out} の「貼る位置」に従って一度だけ貼る）: {missing}")


if __name__ == "__main__":
    main()
