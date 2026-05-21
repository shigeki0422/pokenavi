"""
メガフラエッテ記事のヒーロー画像生成
720x360px, RGB PNG
"""
from PIL import Image, ImageDraw, ImageFont
import math
from pathlib import Path

ROOT = Path(__file__).parent.parent
ICONS = ROOT / "public" / "images" / "pokemon"
OUT   = ROOT / "src" / "assets" / "hero-florette-m2.png"

W, H = 720, 360

# ---- 色定義 ----
BG_TOP    = (252, 220, 240)   # ピンク上
BG_BOT    = (240, 224, 255)   # ラベンダー下
DIAMOND   = (255, 255, 255)
ROW_WHITE = (255, 255, 255)
ROW_PINK  = (242, 100, 160)
BADGE_BG  = (224, 80, 140)
BADGE_TXT = (255, 255, 255)
RANK_PINK = (242, 100, 160)
RANK_DARK = (60, 60, 70)
NAME_DARK = (40, 40, 50)
META_GRAY = (140, 120, 140)
ARROW     = (242, 100, 160)

# ---- ランキングデータ ----
ENTRIES = [
    {"rank": 10, "name": "ギャラドス",    "id": "0130-00", "highlight": False},
    {"rank": 11, "name": "フラエッテ(永遠)", "id": "0670-05", "highlight": True},
    {"rank": 12, "name": "ゲンガー",      "id": "0094-00", "highlight": False},
    {"rank": 13, "name": "キラフロル",    "id": "0970-00", "highlight": False},
]

def load_icon(pokemon_id: str, size: int):
    path = ICONS / f"pokemon-{pokemon_id}.webp"
    if not path.exists():
        print(f"  [WARN] アイコン不在: {path.name}")
        return None
    img = Image.open(path).convert("RGBA").resize((size, size), Image.LANCZOS)
    return img

def draw_gradient(draw, w, h):
    for y in range(h):
        t = y / h
        r = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
        g = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
        b = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def draw_diamonds(canvas, w, h):
    size = 28
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for row in range(-1, h // size + 2):
        for col in range(-1, w // size + 2):
            cx = col * size + (size // 2 if row % 2 else 0)
            cy = row * size
            pts = [(cx, cy - size // 2), (cx + size // 2, cy),
                   (cx, cy + size // 2), (cx - size // 2, cy)]
            d.polygon(pts, outline=(255, 255, 255, 35))
    canvas.paste(overlay, (0, 0), overlay)

def get_font(size: int, bold=False):
    candidates = [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" if bold else "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode MS.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

def main():
    # ベースキャンバス
    canvas = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(canvas)
    draw_gradient(draw, W, H)

    rgba = canvas.convert("RGBA")
    draw_diamonds(rgba, W, H)
    canvas = rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # ---- 左パネル ----
    LX, LY = 22, 20

    # シーズン M-2 バッジ
    badge_x, badge_y, badge_w, badge_h = LX, LY, 145, 38
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
                            radius=19, fill=BADGE_BG)
    font_badge = get_font(18, bold=True)
    draw.text((badge_x + 14, badge_y + 9), "シーズン M-2", font=font_badge, fill=BADGE_TXT)

    # 日付
    font_date = get_font(12)
    draw.text((LX + 2, LY + 48), "2026/05/13 〜 06/17", font=font_date, fill=META_GRAY)

    # シングルバトル タグ
    tag_x, tag_y = LX, LY + 72
    draw.rounded_rectangle([tag_x, tag_y, tag_x + 118, tag_y + 26],
                            radius=13, outline=(200, 160, 190), width=1, fill=(255, 255, 255))
    font_tag = get_font(13)
    draw.text((tag_x + 18, tag_y + 6), "シングルバトル", font=font_tag, fill=(120, 80, 110))

    # 使用率ランキング情報
    font_small = get_font(11)
    font_small2 = get_font(12)
    draw.text((LX, LY + 118), "使用率ランキング", font=font_small, fill=META_GRAY)
    draw.text((LX, LY + 134), "#11 フラエッテ(永遠)", font=font_small2, fill=RANK_PINK)
    draw.text((LX, LY + 153), "フラエッテナイト 97.4%", font=font_small, fill=META_GRAY)
    draw.text((LX, LY + 168), "相方: メガギャラドス", font=font_small, fill=META_GRAY)

    # ---- 右パネル（ランキング行） ----
    RX = 200       # 右エリア開始X
    ROW_H = 72     # 1行の高さ
    ROW_W = W - RX - 18
    ICON_SIZE = 48

    font_rank   = get_font(28, bold=True)
    font_rank_h = get_font(28, bold=True)
    font_name   = get_font(17)
    font_name_h = get_font(18, bold=True)

    for i, entry in enumerate(ENTRIES):
        ry = 16 + i * (ROW_H + 6)
        rx = RX
        is_hi = entry["highlight"]

        # 行背景
        row_color = ROW_PINK if is_hi else ROW_WHITE
        shadow_color = (200, 200, 210) if not is_hi else (220, 70, 130)
        draw.rounded_rectangle([rx, ry + 3, rx + ROW_W, ry + ROW_H + 3],
                                radius=14, fill=shadow_color)
        draw.rounded_rectangle([rx, ry, rx + ROW_W, ry + ROW_H],
                                radius=14, fill=row_color)

        # 三角マーカー（ハイライト行のみ）
        if is_hi:
            ax = rx - 12
            ay = ry + ROW_H // 2
            draw.polygon([(ax, ay - 9), (ax + 11, ay), (ax, ay + 9)], fill=ARROW)

        # 順位
        rank_str = str(entry["rank"])
        rank_color = (255, 255, 255) if is_hi else RANK_DARK
        rfont = font_rank_h if is_hi else font_rank
        rank_x = rx + 14
        draw.text((rank_x, ry + ROW_H // 2 - 18), rank_str, font=rfont, fill=rank_color)

        # アイコン
        icon_x = rx + 62
        icon_y = ry + (ROW_H - ICON_SIZE) // 2
        icon = load_icon(entry["id"], ICON_SIZE)
        if icon:
            canvas.paste(icon, (icon_x, icon_y), icon)

        # 名前
        name_color = (255, 255, 255) if is_hi else NAME_DARK
        nfont = font_name_h if is_hi else font_name
        name_x = icon_x + ICON_SIZE + 10
        draw.text((name_x, ry + ROW_H // 2 - 11), entry["name"], font=nfont, fill=name_color)

        # ハイライト行：右端にメガマーク
        if is_hi:
            mark_icon_path = ICONS / "pokemon-0670-05.webp"
            if mark_icon_path.exists():
                mk = Image.open(mark_icon_path).convert("RGBA").resize((28, 28), Image.LANCZOS)
                mk_x = rx + ROW_W - 38
                mk_y = ry + (ROW_H - 28) // 2
                canvas.paste(mk, (mk_x, mk_y), mk)

    canvas.save(OUT, "PNG")
    print(f"✓ 保存: {OUT}")

if __name__ == "__main__":
    main()
