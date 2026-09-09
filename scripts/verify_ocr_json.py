"""OCR結果(JSON)を投入前に検証する。

検証は2系統:
  A) アイコン照合済みランキングとの突き合わせ（前シーズンの続きで icon_cache が効く日）
  B) ヘッダーの図鑑番号(dex)とマスターの突き合わせ（新シーズン初日など、
     icon_cache に無いポケモンが多くアイコン照合が使えない日）

サブエージェントは同じランクに別のポケモンを報告することがあるため必ず通す。

  python3 scripts/verify_ocr_json.py <ocr_json_dir> <season> <crawled_date> [max_rank]
"""
import json, sqlite3, sys
from pathlib import Path

src = Path(sys.argv[1])
season, date = sys.argv[2], sys.argv[3]
max_rank = int(sys.argv[4]) if len(sys.argv) > 4 else 200

conn = sqlite3.connect(Path(__file__).parent / "pokenavi.db")
ranking = {r[0]: r[1] for r in conn.execute(
    "SELECT rank,pokemon FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=?",
    (season, date))}
# 図鑑番号 → その番号を持つ正式名（フォーム違いを含む）
dex_names = {}
for name, dex in conn.execute("SELECT pokemon_name, dex_number FROM pokemon_base_stats"):
    dex_names.setdefault(dex, set()).add(name)
master = {n for s in dex_names.values() for n in s}

files = sorted(src.glob("*.json"))
missing = [r for r in range(1, max_rank + 1) if not (src / f"{r:03d}.json").exists()]
bad, empty, form, seen = [], [], [], {}

for f in files:
    d = json.loads(f.read_text())
    r, p, dex = d["rank"], d["pokemon"], d.get("dex")
    if r != int(f.stem):
        bad.append((r, f"ファイル名{f.stem}とrank不一致", "")); continue
    if r in seen:
        bad.append((r, p, f"rank重複（{seen[r]}）"))
    seen[r] = p

    exp = ranking.get(r)
    if exp:  # A) アイコン照合の結果が正
        if p != exp:
            (form if (p in exp or exp in p) else bad).append((r, p, exp))
    elif dex is not None:  # B) 図鑑番号で検証
        cands = dex_names.get(dex)
        if not cands:
            bad.append((r, p, f"No.{dex} がマスターに無い"))
        elif p not in cands:
            # 同じ図鑑番号の別フォーム名なら上書き候補、そうでなければ誤読
            (form if len(cands) >= 1 else bad).append((r, p, f"No.{dex}→{sorted(cands)}"))
    elif p not in master:
        bad.append((r, p, "マスターに無い（dexも無し）"))

    n = {k: len(d.get(k, [])) for k in ("moves", "items", "abilities", "natures", "partners", "evs")}
    if not all(n[k] for k in ("moves", "items", "abilities", "natures", "partners", "evs")):
        empty.append((r, p, n))

dup_names = {v for k, v in seen.items() if list(seen.values()).count(v) > 1}

print(f"JSON {len(files)}件 / 未処理 {len(missing)}件 / 要確認 {len(bad)}件 / 空 {len(empty)}件 / フォーム差 {len(form)}件")
if missing:
    print("  未処理:", missing)
for r, p, e in bad:
    print(f"  🚨 rank={r:3d} OCR={p} … {e}")
for r, p, n in empty:
    print(f"  🚨 空   rank={r:3d} {p} {n}")
if dup_names:
    print(f"  ⚠ 同名が複数ランクに出現（フォーム違いの可能性）: {sorted(dup_names)}")
if form:
    print("\n  フォーム要確認（ability画像でNo./タイプを目視のうえ確定）:")
    for r, p, e in sorted(form):
        print(f"    {r}: OCR={p}  {e}")

sys.exit(1 if (missing or bad or empty) else 0)
