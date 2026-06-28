#!/usr/bin/env python3
"""
blog/*.md のフロントマターに updatedDate を追加する（未設定の記事のみ）。
初期値は pubDate と同じ日付。
"""
import re
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "src/content/blog"

UPDATED_RE = re.compile(r"^updatedDate:", re.MULTILINE)
PUB_RE = re.compile(r"^pubDate:\s*'([^']+)'", re.MULTILINE)

added = skipped = 0

for md_path in sorted(CONTENT_DIR.glob("*.md")):
    text = md_path.read_text(encoding="utf-8")

    if UPDATED_RE.search(text):
        skipped += 1
        continue

    m = PUB_RE.search(text)
    if not m:
        skipped += 1
        continue

    pub_date = m.group(1)
    new_text = text.replace(
        f"pubDate: '{pub_date}'",
        f"updatedDate: '{pub_date}'\npubDate: '{pub_date}'",
        1,
    )

    if new_text != text:
        md_path.write_text(new_text, encoding="utf-8")
        added += 1

print(f"added={added}  skipped={skipped}")
