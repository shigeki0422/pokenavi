"""ocr_0909/*.json を insert_detail_from_journal.py が読むjournal形式に変換する"""
import json, sys
from pathlib import Path

src = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

records = []
for f in sorted(src.glob("*.json")):
    records.append(json.loads(f.read_text()))

with (out_dir / "ocr.jsonl").open("w") as w:
    for rec in records:
        w.write(json.dumps({
            "message": {"content": [
                {"type": "tool_use", "name": "StructuredOutput", "input": rec}
            ]}
        }, ensure_ascii=False) + "\n")

print(f"{len(records)}件 → {out_dir}/ocr.jsonl")
