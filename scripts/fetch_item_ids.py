"""pokedb のポケモン詳細ページから 持ち物名→item_key の対応を収集する。

ページ内に {"rank":1,"item_key":769,"name":"ボーマンダナイト",...} の形で
埋め込まれているため、これを集めれば item-sprite.css の座標を引ける。

  python3 scripts/fetch_item_ids.py [season] [出力json]
"""
import json, re, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from download_assets import BASE_PDB, HEADERS_PDB, fetch_binary

season = sys.argv[1] if len(sys.argv) > 1 else "6"
out = Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/item_ids.json")

lst = fetch_binary(f"{BASE_PDB}/pokemon/list", HEADERS_PDB).decode("utf-8", "replace")
pids = sorted(set(re.findall(r'/pokemon/show/(\d{4}-\d{2})', lst)))
print(f"ポケモン {len(pids)}件")

mapping = {}
for i, pid in enumerate(pids, 1):
    d = fetch_binary(f"{BASE_PDB}/pokemon/show/{pid}?season={season}&rule=0", HEADERS_PDB)
    if d:
        raw = d.decode("utf-8", "replace").replace("&quot;", '"')
        for key, name in re.findall(r'"item_key":(\d+),"name":"([^"]*)"', raw):
            if name:
                mapping.setdefault(name, int(key))
    if i % 25 == 0:
        print(f"  {i}/{len(pids)}  収集 {len(mapping)}種", flush=True)
    time.sleep(0.4)

out.write_text(json.dumps(mapping, ensure_ascii=False, indent=1))
print(f"完了: {len(mapping)}種 → {out}")
