"""OCR結果(JSON)をアイコン照合済みランキングと突き合わせて検証する。

サブエージェントは同じランクに別のポケモンを報告することがあるため、
insert_detail_from_journal.py に渡す前に必ずこれを通す。

  python3 scripts/verify_ocr_json.py <ocr_json_dir> <season> <crawled_date>
"""
import json, sqlite3, sys, re
from pathlib import Path

src, season, date = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
conn = sqlite3.connect(Path(__file__).parent / "pokenavi.db")
db = {r[0]: r[1] for r in conn.execute(
    "SELECT rank,pokemon FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=?",
    (season, date))}

files = sorted(src.glob("*.json"))
missing = [r for r in range(1, 201) if not (src / f"{r:03d}.json").exists()]
bad, empty, form = [], [], []

for f in files:
    d = json.loads(f.read_text())
    r, p = d["rank"], d["pokemon"]
    if r != int(f.stem):
        bad.append((r, f"ファイル名{f.stem}とrank不一致", ""))
        continue
    exp = db.get(r)
    if exp and p != exp:
        # フォーム違い（部分一致）は上書き候補、それ以外は誤読
        (form if (p in exp or exp in p) else bad).append((r, p, exp))
    n = {k: len(d.get(k, [])) for k in ("moves", "items", "abilities", "natures", "partners", "evs")}
    if not all(n[k] for k in ("moves", "items", "abilities", "natures", "partners", "evs")):
        empty.append((r, p, n))

print(f"JSON {len(files)}件 / 未処理 {len(missing)}件 / 名前誤り {len(bad)}件 / 空 {len(empty)}件 / フォーム差 {len(form)}件")
if missing:
    print("  未処理:", missing)
for r, p, e in bad:
    print(f"  🚨 誤読 rank={r:3d} OCR={p} DB={e} → 該当ランクを再OCRすること")
for r, p, n in empty:
    print(f"  🚨 空   rank={r:3d} {p} {n}")
if form:
    print("\n  RANK_OVERRIDES_BY_DATE 用（アイコン照合の名前を採用）:")
    print(f'    "{date}": {{')
    for r, p, e in sorted(form):
        print(f'        {r}: "{e}",  # OCR={p}')
    print("    },")

sys.exit(1 if (missing or bad or empty) else 0)
