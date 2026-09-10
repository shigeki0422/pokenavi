"""OCR結果の目視照合用に、ヘッダー帯（順位・図鑑番号・名前・アイコン）を
20件ずつ縦に連結した一覧画像を作る。

サブエージェントは同じランクに別のポケモンを報告することがあるため、
投入前にこの画像で全件を目視確認する。

  python3 scripts/make_header_sheets.py <crawl_dir> <out_dir> [max_rank]
"""
import sys
from pathlib import Path
from PIL import Image

crawl = Path(sys.argv[1])
out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
max_rank = int(sys.argv[3]) if len(sys.argv) > 3 else 200

BOX = (620, 5, 1400, 110)
SCALE = 0.62
PER = 20
W, H = BOX[2]-BOX[0], BOX[3]-BOX[1]

for g in range((max_rank + PER - 1) // PER):
    ranks = [r for r in range(g*PER+1, g*PER+PER+1) if r <= max_rank]
    canvas = Image.new("RGB", (W, H*len(ranks)), "white")
    for i, r in enumerate(ranks):
        p = crawl / "detail" / f"{r:03d}" / "ability_00.png"
        if p.exists():
            canvas.paste(Image.open(p).crop(BOX), (0, i*H))
    canvas = canvas.resize((int(W*SCALE), int(H*len(ranks)*SCALE)), Image.LANCZOS)
    f = out / f"headers_{g+1:02d}.png"
    canvas.save(f)
    print(f"{f.name}  rank {ranks[0]}〜{ranks[-1]}")
