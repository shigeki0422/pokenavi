"""
クロール画像をOCR前に事前クロップする
中央パネル（青ダイアログ）のみ、ヘッダー込み・下背景除去:
(2400x1080) → crop(960x965)
"""

import os
import sys
from pathlib import Path
from PIL import Image

CROP_BOX = (720, 0, 1680, 965)

def crop_dir(detail_dir: str, overwrite: bool = False):
    d = Path(detail_dir)
    for png in sorted(d.glob("*.png")):
        out = d / f"_c_{png.name}"
        if out.exists() and not overwrite:
            continue
        img = Image.open(png).crop(CROP_BOX)
        img.save(str(out))

def crop_all(crawl_dir: str, overwrite: bool = False):
    base = Path(crawl_dir) / "detail"
    dirs = sorted(base.iterdir())
    for i, d in enumerate(dirs, 1):
        if d.is_dir():
            crop_dir(str(d), overwrite)
        if i % 20 == 0:
            print(f"  {i}/{len(dirs)}", flush=True)
    print(f"完了: {len(dirs)}件")

if __name__ == "__main__":
    crawl_dir = sys.argv[1] if len(sys.argv) > 1 else None
    if not crawl_dir:
        from datetime import date
        crawl_dir = f"/Users/shigeki/work/pokenavi/crawl_data/champ_crawl_{date.today().isoformat()}"
    print(f"クロップ: {crawl_dir}")
    overwrite = "--overwrite" in sys.argv
    crop_all(crawl_dir, overwrite)
