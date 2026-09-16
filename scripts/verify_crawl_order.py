"""クロール画像のフォルダ番号とヘッダーの「N位」表示のずれを検出する。

画面遷移が間に合わないと同じ画面を2度撮り、以降が1つずつずれて最後の順位が
欠落する（2026-09-16に156位以降で発生）。アイコン照合では「重複」としか
出ず、ずれ始めも特定できないため、投入前にこれを通す。

順位表示の領域を二値化して隣接フォルダ間で比較する。画面遷移中のコマは
全体が暗くなるため、生の輝度差では判定できない（二値化が必要）。

  python3 scripts/verify_crawl_order.py <crawl_dir> [max_rank]
"""
import sys
from pathlib import Path

import cv2
import numpy as np

crawl = Path(sys.argv[1])
max_rank = int(sys.argv[2]) if len(sys.argv) > 2 else 200
base = crawl / "detail"

BOX_FULL = (690, 20, 1010, 95)   # 2400x1080 の「N位」表示（下端の暗帯は避ける）
BOX_CROP = (0, 20, 290, 95)      # _c_ は左に720ずれる
THRESHOLD = 0.93                 # 実測: 同一表示0.98 / 別表示0.60〜0.73


def rank_mask(rank: int):
    d = base / f"{rank:03d}"
    for name, box in (("move_00.png", BOX_FULL), ("ability_00.png", BOX_FULL),
                      ("_c_move_00.png", BOX_CROP), ("_c_ability_00.png", BOX_CROP)):
        p = d / name
        if not p.exists():
            continue
        g = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE)
        if g is None:
            continue
        x1, y1, x2, y2 = box
        if g.shape[1] < x2 or g.shape[0] < y2:
            continue
        s = g[y1:y2, x1:x2]
        return (s < s.mean() - 20).astype(np.uint8)
    return None


masks = {r: rank_mask(r) for r in range(1, max_rank + 1)}
missing = [r for r, m in masks.items() if m is None]

shifted = []
for r in range(2, max_rank + 1):
    a, c = masks.get(r - 1), masks.get(r)
    if a is None or c is None or a.shape != c.shape:
        continue
    iou = (a & c).sum() / max((a | c).sum(), 1)
    if iou >= THRESHOLD:
        shifted.append((r, round(float(iou), 3)))

print(f"検査 {max_rank}件 / 画像なし {len(missing)}件 / ずれ {len(shifted)}件")
if missing:
    print("  画像なし:", missing[:20])
for r, iou in shifted:
    print(f"  🚨 rank={r} が直前と同じ順位表示 (一致率{iou}) "
          f"→ ここから後ろが1つずれ、最後の順位が欠落している可能性")
if shifted:
    print("  → 取り直しを推奨。該当フォルダの move_00.png でヘッダーを確認すること")

sys.exit(1 if (missing or shifted) else 0)
