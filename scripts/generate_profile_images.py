import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ACCENT      = (35,  55, 255)
ACCENT_SOFT = (210, 215, 255)   # 淡いアクセント
GRAY_DARK   = (34,  41,  57)
GRAY        = (96, 115, 159)
GRAY_MID    = (180, 190, 210)
GRAY_LIGHT  = (229, 233, 240)
BG          = (250, 251, 254)   # ごく薄い青白

font_paths = [
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    "/System/Library/Fonts/Arial Bold.ttf",
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

def rounded_bar(draw, x0, y0, x1, y1, r, fill):
    draw.rectangle([x0 + r, y0, x1 - r, y1], fill=fill)
    draw.rectangle([x0, y0 + r, x1, y1], fill=fill)
    draw.ellipse([x0, y0, x0 + r*2, y0 + r*2], fill=fill)
    draw.ellipse([x1 - r*2, y0, x1, y0 + r*2], fill=fill)

def dot_grid(draw, x0, y0, x1, y1, step, r, color):
    x = x0
    while x <= x1:
        y = y0
        while y <= y1:
            draw.ellipse([x-r, y-r, x+r, y+r], fill=color)
            y += step
        x += step

# ================================================================
# Profile icon  400×400（×3 超解像レンダリング）
# ================================================================
S, SC = 400, 3
SS = S * SC

img = Image.new("RGB", (SS, SS), BG)
d   = ImageDraw.Draw(img)

cx, cy = SS // 2, SS // 2

# ── ドットグリッド（薄め）
dot_grid(d, 30*SC, 30*SC, SS - 30*SC, SS - 30*SC,
         step=28*SC, r=2*SC, color=GRAY_LIGHT)

# ── バーチャート（5本・洗練比率）
bar_pcts  = [55, 80, 100, 68, 40]
bar_w     = 34 * SC
gap       = 14 * SC
total     = len(bar_pcts) * bar_w + (len(bar_pcts) - 1) * gap
bx0       = cx - total // 2
base_y    = cy + 38 * SC
max_h     = 108 * SC

for i, pct in enumerate(bar_pcts):
    bx = bx0 + i * (bar_w + gap)
    bh = int(max_h * pct / 100)

    if pct == 100:                       # ハイライトバー
        # 背景グロー
        glow = Image.new("RGBA", (SS, SS), (0,0,0,0))
        gd   = ImageDraw.Draw(glow)
        gd.ellipse([bx - 22*SC, base_y - bh - 22*SC,
                    bx + bar_w + 22*SC, base_y + 16*SC],
                   fill=(*ACCENT, 35))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=20*SC))
        img  = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
        d    = ImageDraw.Draw(img)
        col  = ACCENT
    else:
        t   = (pct - 35) / 65
        col = tuple(int(GRAY_LIGHT[j] + (GRAY_MID[j] - GRAY_LIGHT[j]) * t) for j in range(3))

    rounded_bar(d, bx, base_y - bh, bx + bar_w, base_y, 7*SC, col)

# ── ベースライン（細め）
d.rectangle([bx0, base_y + 6*SC, bx0 + total, base_y + 8*SC], fill=GRAY_MID)

# ── 小さな "DATA" ラベル（アクセント色、小文字上部）
font_label = load_font(18 * SC)
label = "DATA ANALYSIS"
lb    = d.textbbox((0,0), label, font=font_label)
lw    = lb[2] - lb[0]
d.text(((SS - lw) / 2, cy - max_h - 30*SC), label, font=font_label, fill=ACCENT)

# ── メインテキスト（レタースペーシング風に各文字描画）
font_main = load_font(60 * SC)
text      = "ポケナビ"
bbox      = d.textbbox((0,0), text, font=font_main)
tw        = bbox[2] - bbox[0]
d.text(((SS - tw) / 2, base_y + 16*SC), text, font=font_main, fill=GRAY_DARK)

img.resize((S, S), Image.LANCZOS).save("public/profile-icon.png")
print("Saved: public/profile-icon.png")

# ================================================================
# Header  1500×500（×2）
# ================================================================
W, H, SC2 = 1500, 500, 2
WS, HS    = W * SC2, H * SC2

hdr = Image.new("RGB", (WS, HS), BG)
d2  = ImageDraw.Draw(hdr)

# ── 微グラデーション（上が少し白め）
for y in range(HS):
    t  = y / HS
    bg = tuple(int(255 + (v - 255) * (0.02 + 0.05 * t)) for v in BG)
    d2.line([(0, y), (WS, y)], fill=bg)

# ── ドットグリッド（右半分のみ、薄め）
dot_grid(d2, WS//2, 20*SC2, WS - 20*SC2, HS - 20*SC2,
         step=36*SC2, r=2*SC2, color=GRAY_LIGHT)

# ── 上部アクセントライン（細め・2px相当）
d2.rectangle([(0, 0), (WS, 4*SC2)], fill=ACCENT)

# ── 左縦バー
d2.rectangle([(76*SC2, 65*SC2), (86*SC2, (H-65)*SC2)], fill=ACCENT)

# ── 小ラベル "POKEMON CHAMPIONS DATA ANALYSIS"
font_en  = load_font(20 * SC2)
en_label = "POKEMON CHAMPIONS  ·  DATA ANALYSIS"
d2.text((110*SC2, 68*SC2), en_label, font=font_en, fill=GRAY)

# ── メインタイトル
font_title = load_font(155 * SC2)
d2.text((106*SC2, 96*SC2), "ポケナビ", font=font_title, fill=GRAY_DARK)

# タイトル下の細いアクセントライン
title_bbox = d2.textbbox((0,0), "ポケナビ", font=font_title)
title_w    = title_bbox[2] - title_bbox[0]
d2.rectangle([(108*SC2, 280*SC2),
              (108*SC2 + title_w, 284*SC2)], fill=ACCENT)

# ── タグライン
font_tag = load_font(38 * SC2)
d2.text((110*SC2, 298*SC2),
        "使用率・採用率・メタ考察を定期配信",
        font=font_tag, fill=GRAY)

# ── URL（小）
font_url = load_font(28 * SC2)
d2.text((112*SC2, 380*SC2), "pokenavi.jp", font=font_url, fill=GRAY_MID)

# ── 右側バーチャート（8本、洗練比率）
bar_data2 = [105, 195, 80, 170, 260, 130, 75, 195]
bw2       = 46 * SC2
gap2      = 16 * SC2
rx0       = WS - len(bar_data2) * (bw2 + gap2) - 70*SC2
by2       = HS - 60*SC2

for i, bh in enumerate(bar_data2):
    bh_s = bh * SC2 // 2
    bx2  = rx0 + i * (bw2 + gap2)
    if i == 4:      # 最大バーだけアクセント
        # グロー
        glow2 = Image.new("RGBA", (WS, HS), (0,0,0,0))
        gd2   = ImageDraw.Draw(glow2)
        gd2.ellipse([bx2 - 20*SC2, by2 - bh_s - 20*SC2,
                     bx2 + bw2 + 20*SC2, by2 + 10*SC2],
                    fill=(*ACCENT, 30))
        glow2 = glow2.filter(ImageFilter.GaussianBlur(radius=22*SC2))
        hdr   = Image.alpha_composite(hdr.convert("RGBA"), glow2).convert("RGB")
        d2    = ImageDraw.Draw(hdr)
        col2  = ACCENT
    else:
        t2   = bh / 260
        col2 = tuple(int(GRAY_LIGHT[j] + (GRAY_MID[j] - GRAY_LIGHT[j]) * t2 * 0.85) for j in range(3))
    rounded_bar(d2, bx2, by2 - bh_s, bx2 + bw2, by2, 7*SC2, col2)

# ベースライン
d2.rectangle([rx0 - 2, by2 + 4*SC2,
              rx0 + len(bar_data2)*(bw2+gap2), by2 + 7*SC2], fill=GRAY_LIGHT)

hdr.resize((W, H), Image.LANCZOS).save("public/profile-header.png")
print("Saved: public/profile-header.png")
