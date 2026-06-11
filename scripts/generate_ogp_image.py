import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = "public/og-image.png"

BG_TOP = (15, 23, 42)
BG_BOT = (26, 35, 60)
ACCENT = (99, 179, 237)
WHITE = (255, 255, 255)
GRAY = (180, 195, 220)

img = Image.new("RGB", (W, H), BG_TOP)
draw = ImageDraw.Draw(img)

for y in range(H):
    r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * y / H)
    g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * y / H)
    b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * y / H)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

for i in range(8):
    x = 80 + i * 150
    draw.ellipse([(x - 120, -120), (x + 120, 120)], fill=(30, 50, 90))

font_paths = [
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    "/System/Library/Fonts/Supplemental/Hiragino Sans GB W3.otf",
    "/System/Library/Fonts/Arial.ttf",
]

def load_font(size):
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()

font_title = load_font(110)
font_tagline = load_font(44)
font_url = load_font(36)

draw.line([(80, 200), (W - 80, 200)], fill=ACCENT, width=3)

title = "ポケナビ"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) / 2, 230), title, font=font_title, fill=WHITE)

tagline = "ポケモンチャンピオンズ × データ分析"
bbox2 = draw.textbbox((0, 0), tagline, font=font_tagline)
tw2 = bbox2[2] - bbox2[0]
draw.text(((W - tw2) / 2, 400), tagline, font=font_tagline, fill=ACCENT)

desc = "使用率・採用率・メタ考察を定期配信"
bbox3 = draw.textbbox((0, 0), desc, font=font_tagline)
tw3 = bbox3[2] - bbox3[0]
draw.text(((W - tw3) / 2, 465), desc, font=font_tagline, fill=GRAY)

draw.line([(80, 540), (W - 80, 540)], fill=ACCENT, width=2)

url = "pokenavi.jp"
bbox4 = draw.textbbox((0, 0), url, font=font_url)
tw4 = bbox4[2] - bbox4[0]
draw.text(((W - tw4) / 2, 560), url, font=font_url, fill=GRAY)

img.save(OUT)
print(f"Saved: {OUT} ({W}x{H})")
