"""
Tier1メガ進化記事 ヒーロー画像一括生成
720x360px RGB PNG - フラエッテスクリプトと同仕様
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT  = Path(__file__).parent.parent
ICONS = ROOT / "public" / "images" / "pokemon"
OUT   = ROOT / "src" / "assets"

W, H = 720, 360
ROW_H     = 72
ICON_SIZE = 48

# ---- 共通パレット ----
DIAMOND    = (255, 255, 255)
ROW_WHITE  = (255, 255, 255)
ROW_SHADOW = (200, 200, 210)
RANK_DARK  = (60,  60,  70)
NAME_DARK  = (40,  40,  50)
META_GRAY  = (140, 120, 140)
BADGE_TXT  = (255, 255, 255)

# ---- 記事ごとの設定 ----
ARTICLES = [
    # ── ガブリアス ──
    dict(
        out      = "hero-garchomp-m2.png",
        bg_top   = (210, 235, 255),
        bg_bot   = (195, 215, 250),
        badge_bg = (60, 140, 90),
        row_hi   = (60, 175, 100),
        shadow_hi= (30, 130, 65),
        left_lines = ["#1  ガブリアス", "使用率 No.1 / M-2", "タスキ型 37.5%"],
        entries  = [
            dict(rank=1, name="ガブリアス",   id="0445-00", hi=True),
            dict(rank=2, name="ブリジュラス", id="1018-00", hi=False),
            dict(rank=3, name="マスカーニャ", id="0908-00", hi=False),
            dict(rank=4, name="アシレーヌ",   id="0730-00", hi=False),
        ],
    ),
    # ── メガリザードンX ──
    dict(
        out      = "hero-charizard-x-m2.png",
        bg_top   = (255, 220, 205),
        bg_bot   = (240, 200, 185),
        badge_bg = (190, 50, 30),
        row_hi   = (210, 65, 40),
        shadow_hi= (160, 30, 15),
        left_lines = ["#5  リザードン", "メガX / ほのお・ドラゴン", "メガ石採用率 37.2%"],
        entries  = [
            dict(rank=4, name="アシレーヌ",   id="0730-00", hi=False),
            dict(rank=5, name="リザードン",   id="0006-00", hi=True),
            dict(rank=6, name="アーマーガア", id="0823-00", hi=False),
            dict(rank=7, name="イダイトウ(オス)", id="0902-00", hi=False),
        ],
    ),
    # ── メガリザードンY ──
    dict(
        out      = "hero-charizard-y-m2.png",
        bg_top   = (255, 235, 195),
        bg_bot   = (250, 215, 165),
        badge_bg = (220, 120, 20),
        row_hi   = (235, 140, 30),
        shadow_hi= (185, 90, 10),
        left_lines = ["#5  リザードン", "メガY / ほのお・ひこう", "メガ石採用率 61.4%"],
        entries  = [
            dict(rank=4, name="アシレーヌ",   id="0730-00", hi=False),
            dict(rank=5, name="リザードン",   id="0006-00", hi=True),
            dict(rank=6, name="アーマーガア", id="0823-00", hi=False),
            dict(rank=7, name="イダイトウ(オス)", id="0902-00", hi=False),
        ],
    ),
    # ── メガルカリオ ──
    dict(
        out      = "hero-lucario-m2.png",
        bg_top   = (205, 225, 255),
        bg_bot   = (185, 210, 250),
        badge_bg = (60, 100, 195),
        row_hi   = (75, 120, 215),
        shadow_hi= (40, 75, 165),
        left_lines = ["#9  ルカリオ", "メガ石採用率 97.7%", "ようき AS型 57.8%"],
        entries  = [
            dict(rank=9,  name="ルカリオ",      id="0448-00", hi=True),
            dict(rank=10, name="ギャラドス",    id="0130-00", hi=False),
            dict(rank=11, name="フラエッテ(永遠)", id="0670-05", hi=False),
            dict(rank=12, name="ゲンガー",      id="0094-00", hi=False),
        ],
    ),
    # ── メガギャラドス ──
    dict(
        out      = "hero-gyarados-m2.png",
        bg_top   = (195, 220, 255),
        bg_bot   = (170, 200, 245),
        badge_bg = (35, 80, 180),
        row_hi   = (50, 100, 200),
        shadow_hi= (20, 60, 150),
        left_lines = ["#10 ギャラドス", "メガ石採用率 64.6%", "みず/あくタイプ"],
        entries  = [
            dict(rank=9,  name="ルカリオ",      id="0448-00", hi=False),
            dict(rank=10, name="ギャラドス",    id="0130-00", hi=True),
            dict(rank=11, name="フラエッテ(永遠)", id="0670-05", hi=False),
            dict(rank=12, name="ゲンガー",      id="0094-00", hi=False),
        ],
    ),
    # ── メガゲンガー ──
    dict(
        out      = "hero-gengar-m2.png",
        bg_top   = (230, 210, 255),
        bg_bot   = (215, 190, 250),
        badge_bg = (110, 50, 175),
        row_hi   = (130, 70, 200),
        shadow_hi= (80, 25, 140),
        left_lines = ["#12 ゲンガー", "メガ石採用率 83.3%", "かげふみ型"],
        entries  = [
            dict(rank=11, name="フラエッテ(永遠)", id="0670-05", hi=False),
            dict(rank=12, name="ゲンガー",      id="0094-00", hi=True),
            dict(rank=13, name="キラフロル",    id="0970-00", hi=False),
            dict(rank=14, name="ミミロップ",    id="0428-00", hi=False),
        ],
    ),
    # ── メガキラフロル ──
    dict(
        out      = "hero-kiraflosure-m2.png",
        bg_top   = (245, 220, 255),
        bg_bot   = (225, 200, 240),
        badge_bg = (130, 80, 155),
        row_hi   = (150, 95, 175),
        shadow_hi= (100, 55, 125),
        left_lines = ["#13 キラフロル", "メガ石採用率 53.3%", "おくびょうCS型"],
        entries  = [
            dict(rank=12, name="ゲンガー",   id="0094-00", hi=False),
            dict(rank=13, name="キラフロル", id="0970-00", hi=True),
            dict(rank=14, name="ミミロップ", id="0428-00", hi=False),
            dict(rank=15, name="ハッサム",   id="0212-00", hi=False),
        ],
    ),
    # ── メガミミロップ ──
    dict(
        out      = "hero-lopunny-m2.png",
        bg_top   = (255, 220, 235),
        bg_bot   = (250, 200, 220),
        badge_bg = (195, 80, 120),
        row_hi   = (215, 100, 140),
        shadow_hi= (165, 55, 90),
        left_lines = ["#14 ミミロップ", "メガ石採用率 96.4%", "ようきAS型 70.2%"],
        entries  = [
            dict(rank=13, name="キラフロル", id="0970-00", hi=False),
            dict(rank=14, name="ミミロップ", id="0428-00", hi=True),
            dict(rank=15, name="ハッサム",   id="0212-00", hi=False),
            dict(rank=16, name="ギルガルド", id="0681-00", hi=False),
        ],
    ),
    # ── メガハッサム ──
    dict(
        out      = "hero-scizor-m2.png",
        bg_top   = (210, 245, 215),
        bg_bot   = (190, 235, 195),
        badge_bg = (45, 130, 70),
        row_hi   = (60, 155, 85),
        shadow_hi= (25, 100, 45),
        left_lines = ["#15 ハッサム", "メガ石採用率 78.3%", "いじっぱりHA型"],
        entries  = [
            dict(rank=14, name="ミミロップ", id="0428-00", hi=False),
            dict(rank=15, name="ハッサム",   id="0212-00", hi=True),
            dict(rank=16, name="ギルガルド", id="0681-00", hi=False),
            dict(rank=17, name="カイリュー", id="0149-00", hi=False),
        ],
    ),
    # ── メガカイリュー ──
    dict(
        out      = "hero-dragonite-m2.png",
        bg_top   = (215, 230, 255),
        bg_bot   = (200, 220, 250),
        badge_bg = (70, 110, 200),
        row_hi   = (85, 130, 220),
        shadow_hi= (45, 80, 165),
        left_lines = ["#17 カイリュー", "メガ石採用率 80.8%", "ひかえめCS型 35.0%"],
        entries  = [
            dict(rank=16, name="ギルガルド", id="0681-00", hi=False),
            dict(rank=17, name="カイリュー", id="0149-00", hi=True),
            dict(rank=18, name="ウルガモス", id="0637-00", hi=False),
            dict(rank=19, name="ミミッキュ", id="0778-00", hi=False),
        ],
    ),
    # ── メガムクホーク ──
    dict(
        out      = "hero-staraptor-m3.png",
        bg_top   = (220, 230, 255),
        bg_bot   = (205, 215, 245),
        badge_bg = (60, 90, 180),
        row_hi   = (75, 110, 200),
        shadow_hi= (40, 70, 150),
        left_lines = ["#6  ムクホーク", "使用率 M-3 6位", "ようきAS型 76.1%"],
        entries  = [
            dict(rank=5, name="ミミッキュ",   id="0778-00", hi=False),
            dict(rank=6, name="ムクホーク",   id="0398-00", hi=True),
            dict(rank=8, name="アーマーガア", id="0823-00", hi=False),
            dict(rank=9, name="リザードン",   id="0006-00", hi=False),
        ],
    ),
    # ── メガスターミー ──
    dict(
        out      = "hero-starmie-m2.png",
        bg_top   = (195, 235, 250),
        bg_bot   = (200, 215, 245),
        badge_bg = (50, 155, 185),
        row_hi   = (65, 175, 205),
        shadow_hi= (30, 120, 155),
        left_lines = ["#20 スターミー", "メガ石採用率 97.8%", "いじっぱりAS型 61.9%"],
        entries  = [
            dict(rank=18, name="ウルガモス", id="0637-00", hi=False),
            dict(rank=19, name="ミミッキュ", id="0778-00", hi=False),
            dict(rank=20, name="スターミー", id="0121-00", hi=True),
            dict(rank=21, name="サザンドラ", id="0635-00", hi=False),
        ],
    ),
]


def load_icon(pokemon_id: str, size: int):
    path = ICONS / f"pokemon-{pokemon_id}.webp"
    if not path.exists():
        print(f"  [WARN] アイコン不在: {path.name}")
        return None
    img = Image.open(path).convert("RGBA").resize((size, size), Image.LANCZOS)
    return img


def draw_gradient(draw, w, h, top, bot):
    for y in range(h):
        t = y / h
        r = int(top[0] + (bot[0] - top[0]) * t)
        g = int(top[1] + (bot[1] - top[1]) * t)
        b = int(top[2] + (bot[2] - top[2]) * t)
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
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" if bold
        else "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode MS.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def generate(cfg: dict):
    canvas = Image.new("RGB", (W, H))
    draw   = ImageDraw.Draw(canvas)
    draw_gradient(draw, W, H, cfg["bg_top"], cfg["bg_bot"])

    rgba = canvas.convert("RGBA")
    draw_diamonds(rgba, W, H)
    canvas = rgba.convert("RGB")
    draw   = ImageDraw.Draw(canvas)

    LX, LY = 22, 20

    # シーズン M-2 バッジ
    bw, bh = 145, 38
    draw.rounded_rectangle([LX, LY, LX+bw, LY+bh], radius=19, fill=cfg["badge_bg"])
    draw.text((LX+14, LY+9), "シーズン M-2",
              font=get_font(18, bold=True), fill=BADGE_TXT)

    # 日付
    draw.text((LX+2, LY+48), "2026/05/13 〜 06/17",
              font=get_font(12), fill=META_GRAY)

    # シングルバトル タグ
    ty = LY + 72
    draw.rounded_rectangle([LX, ty, LX+118, ty+26],
                            radius=13, outline=(200, 160, 190), width=1,
                            fill=(255, 255, 255))
    draw.text((LX+18, ty+6), "シングルバトル",
              font=get_font(13), fill=(120, 80, 110))

    # 左パネル テキスト情報
    draw.text((LX, LY+118), "使用率ランキング",
              font=get_font(11), fill=META_GRAY)
    y_info = LY + 134
    fonts_info = [get_font(12, bold=True), get_font(11), get_font(11)]
    colors_info = [cfg["row_hi"], META_GRAY, META_GRAY]
    for i, line in enumerate(cfg["left_lines"][:3]):
        f = fonts_info[i] if i < len(fonts_info) else get_font(11)
        c = colors_info[i] if i < len(colors_info) else META_GRAY
        draw.text((LX, y_info), line, font=f, fill=c)
        y_info += 18

    # ---- 右パネル ----
    RX    = 200
    ROW_W = W - RX - 18

    font_rank   = get_font(28, bold=True)
    font_name   = get_font(17)
    font_name_h = get_font(18, bold=True)

    for i, entry in enumerate(cfg["entries"]):
        ry   = 16 + i * (ROW_H + 6)
        is_hi = entry["hi"]

        shadow_c = cfg["shadow_hi"] if is_hi else (200, 200, 210)
        row_c    = cfg["row_hi"]    if is_hi else ROW_WHITE

        draw.rounded_rectangle([RX,   ry+3, RX+ROW_W, ry+ROW_H+3],
                                radius=14, fill=shadow_c)
        draw.rounded_rectangle([RX,   ry,   RX+ROW_W, ry+ROW_H],
                                radius=14, fill=row_c)

        # 三角マーカー
        if is_hi:
            ax = RX - 12
            ay = ry + ROW_H // 2
            draw.polygon([(ax, ay-9), (ax+11, ay), (ax, ay+9)],
                         fill=cfg["row_hi"])

        # 順位
        rank_c = (255, 255, 255) if is_hi else RANK_DARK
        draw.text((RX+14, ry + ROW_H//2 - 18), str(entry["rank"]),
                  font=font_rank, fill=rank_c)

        # アイコン
        ix = RX + 62
        iy = ry + (ROW_H - ICON_SIZE) // 2
        icon = load_icon(entry["id"], ICON_SIZE)
        if icon:
            canvas.paste(icon, (ix, iy), icon)

        # 名前
        name_c = (255, 255, 255) if is_hi else NAME_DARK
        nfont  = font_name_h if is_hi else font_name
        draw.text((ix + ICON_SIZE + 10, ry + ROW_H//2 - 11),
                  entry["name"], font=nfont, fill=name_c)

        # ハイライト行: 右端にミニアイコン
        if is_hi:
            mk = load_icon(entry["id"], 32)
            if mk:
                canvas.paste(mk, (RX + ROW_W - 42, ry + (ROW_H - 32)//2), mk)

    path = OUT / cfg["out"]
    canvas.save(path, "PNG")
    print(f"  saved: {path.name}")


if __name__ == "__main__":
    print(f"生成開始 ({len(ARTICLES)} 枚)...")
    for cfg in ARTICLES:
        generate(cfg)
    print("完了")
