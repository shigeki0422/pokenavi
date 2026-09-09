"""OCR用に_c_*.pngを縮小する（ヘッダー除去＋0.6倍）。abilityのみヘッダーを残す。"""
import sys
from pathlib import Path
from PIL import Image

SCALE = 0.6
BODY_BOX = (0, 190, 960, 965)

def shrink_dir(d: Path):
    for png in sorted(d.glob("_c_*.png")):
        out = d / f"_s_{png.name[3:]}"
        if out.exists():
            continue
        im = Image.open(png)
        if not png.name.startswith("_c_ability"):
            im = im.crop(BODY_BOX)
        im.resize((int(im.width * SCALE), int(im.height * SCALE)), Image.LANCZOS).save(out)

if __name__ == "__main__":
    base = Path(sys.argv[1]) / "detail"
    dirs = sorted(p for p in base.iterdir() if p.is_dir())
    for i, d in enumerate(dirs, 1):
        shrink_dir(d)
        if i % 40 == 0:
            print(f"  {i}/{len(dirs)}", flush=True)
    print(f"完了: {len(dirs)}件")
