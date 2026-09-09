"""OCR結果(JSON)から pokemon_usage を投入する。

新シーズン初日など、icon_cache に無いポケモンが多くアイコン照合
(insert_ranking_from_icons.py)が使えない場合に用いる。
ヘッダーの図鑑番号(dex)と名前がマスターで整合することを確認してから投入する。

  python3 scripts/insert_ranking_from_ocr.py <ocr_json_dir> <season> <crawled_date> <max_rank>
"""
import json, sqlite3, sys
from datetime import datetime, timezone
from pathlib import Path

src = Path(sys.argv[1])
season, date, max_rank = sys.argv[2], sys.argv[3], int(sys.argv[4])
conn = sqlite3.connect(Path(__file__).parent / "pokenavi.db")

dex_names = {}
for name, dex in conn.execute("SELECT pokemon_name, dex_number FROM pokemon_base_stats"):
    dex_names.setdefault(dex, set()).add(name)

rows, errors, seen = [], [], {}
for r in range(1, max_rank + 1):
    f = src / f"{r:03d}.json"
    if not f.exists():
        errors.append(f"rank={r}: JSONなし"); continue
    d = json.loads(f.read_text())
    name, dex = d["pokemon"], d.get("dex")
    cands = dex_names.get(dex, set())
    if not cands:
        errors.append(f"rank={r}: No.{dex} がマスターに無い ({name})")
    elif name not in cands:
        errors.append(f"rank={r}: '{name}' が No.{dex} の名前({sorted(cands)})と不一致")
    if name in seen:
        errors.append(f"rank={r}: '{name}' が rank={seen[name]} と重複")
    seen[name] = r
    rows.append((r, name))

if errors:
    print(f"🚫 投入中止: {len(errors)}件の問題")
    for e in errors:
        print("  ", e)
    sys.exit(1)

now = datetime.now(timezone.utc).isoformat()
n = 0
for rank, name in rows:
    conn.execute(
        "INSERT OR IGNORE INTO pokemon_usage(season,rule,rank,pokemon,source,crawled_date,crawled_at)"
        " VALUES(?,?,?,?,?,?,?)",
        (season, "single", rank, name, "champions_adb", date, now))
    n += conn.execute("SELECT changes()").fetchone()[0]
conn.commit()
print(f"✅ {len(rows)}件ユニーク確認 → pokemon_usage: {n}件投入")
