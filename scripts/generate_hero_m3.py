"""M-3記事のヒーロー画像を生成（720x360px）"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sqlite3, re

ROOT   = Path(__file__).parent.parent
ICONS  = ROOT / "public" / "images" / "pokemon"
OUT    = ROOT / "src" / "assets"
BLOG   = ROOT / "src" / "content" / "blog"
DB     = ROOT / "scripts" / "pokenavi.db"
SEASON = "M-3"

W, H      = 720, 360
ROW_H     = 72
ICON_SIZE = 48

ROW_WHITE = (255, 255, 255)
RANK_DARK = (60, 60, 70)
NAME_DARK = (40, 40, 50)
META_GRAY = (140, 120, 140)
BADGE_TXT = (255, 255, 255)

TYPE_PALETTE = {
    "ノーマル":   dict(bg_top=(230,230,230), bg_bot=(210,210,210), badge_bg=(120,120,120), row_hi=(130,130,140), shadow_hi=(90,90,100)),
    "ほのお":     dict(bg_top=(255,220,180), bg_bot=(250,190,140), badge_bg=(200,80,30),  row_hi=(220,90,40),  shadow_hi=(170,55,15)),
    "みず":       dict(bg_top=(200,230,255), bg_bot=(170,210,250), badge_bg=(40,120,200), row_hi=(50,140,220), shadow_hi=(25,90,165)),
    "でんき":     dict(bg_top=(255,245,180), bg_bot=(250,235,140), badge_bg=(200,160,20), row_hi=(220,175,25), shadow_hi=(170,125,10)),
    "くさ":       dict(bg_top=(200,240,200), bg_bot=(170,225,170), badge_bg=(60,150,60),  row_hi=(70,170,70),  shadow_hi=(40,115,40)),
    "こおり":     dict(bg_top=(210,245,255), bg_bot=(180,235,252), badge_bg=(60,180,210), row_hi=(70,195,230), shadow_hi=(40,140,175)),
    "かくとう":   dict(bg_top=(240,210,200), bg_bot=(225,185,170), badge_bg=(180,60,60),  row_hi=(200,70,70),  shadow_hi=(145,40,40)),
    "どく":       dict(bg_top=(230,200,240), bg_bot=(210,175,230), badge_bg=(140,60,180), row_hi=(155,70,200), shadow_hi=(105,40,140)),
    "じめん":     dict(bg_top=(240,225,180), bg_bot=(225,208,155), badge_bg=(170,130,40), row_hi=(185,145,50), shadow_hi=(130,95,25)),
    "ひこう":     dict(bg_top=(210,225,255), bg_bot=(185,205,252), badge_bg=(90,120,200), row_hi=(100,135,220), shadow_hi=(65,90,165)),
    "エスパー":   dict(bg_top=(255,210,225), bg_bot=(252,185,210), badge_bg=(210,60,120), row_hi=(230,70,135), shadow_hi=(165,40,90)),
    "むし":       dict(bg_top=(215,235,180), bg_bot=(195,220,155), badge_bg=(115,155,20), row_hi=(125,170,25), shadow_hi=(85,120,10)),
    "いわ":       dict(bg_top=(225,215,190), bg_bot=(210,198,168), badge_bg=(155,130,60), row_hi=(170,145,70), shadow_hi=(120,100,40)),
    "ゴースト":   dict(bg_top=(200,190,230), bg_bot=(175,165,215), badge_bg=(90,70,160),  row_hi=(100,80,180), shadow_hi=(65,50,125)),
    "ドラゴン":   dict(bg_top=(195,210,255), bg_bot=(165,185,250), badge_bg=(60,80,210),  row_hi=(70,90,230),  shadow_hi=(40,60,170)),
    "あく":       dict(bg_top=(200,190,200), bg_bot=(175,165,178), badge_bg=(80,60,80),   row_hi=(90,70,90),   shadow_hi=(55,40,58)),
    "はがね":     dict(bg_top=(215,225,235), bg_bot=(195,208,220), badge_bg=(110,130,155),row_hi=(120,145,170),shadow_hi=(80,100,125)),
    "フェアリー": dict(bg_top=(255,215,235), bg_bot=(252,195,222), badge_bg=(210,100,155),row_hi=(230,110,170),shadow_hi=(165,70,120)),
}

# 記事スラッグ → DBポケモン名（名前差異の吸収）
SLUG_TO_DBNAME = {
    "raichu-y": "ライチュウ",
}

def get_font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" if bold else "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def load_icon(pid, size):
    if not pid:
        return None
    p = ICONS / f"pokemon-{pid}.webp"
    if not p.exists():
        return None
    img = Image.open(p).convert("RGBA")
    return img.resize((size, size), Image.LANCZOS)

def draw_gradient(draw, w, h, top, bot):
    for y in range(h):
        r = int(top[0] + (bot[0] - top[0]) * y / h)
        g = int(top[1] + (bot[1] - top[1]) * y / h)
        b = int(top[2] + (bot[2] - top[2]) * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def draw_diamonds(img, w, h):
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    size = 28
    for row in range(-1, h // size + 2):
        for col in range(-1, w // size + 2):
            cx = col * size + (size // 2 if row % 2 else 0)
            cy = row * size
            pts = [(cx, cy - size//2), (cx + size//2, cy), (cx, cy + size//2), (cx - size//2, cy)]
            d.polygon(pts, fill=(255, 255, 255, 12))
    img.alpha_composite(overlay)

def generate(cfg):
    canvas = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(canvas)
    draw_gradient(draw, W, H, cfg["bg_top"], cfg["bg_bot"])
    rgba = canvas.convert("RGBA")
    draw_diamonds(rgba, W, H)
    canvas = rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    LX, LY = 22, 20
    bw, bh = 145, 38
    draw.rounded_rectangle([LX, LY, LX + bw, LY + bh], radius=19, fill=cfg["badge_bg"])
    draw.text((LX + 14, LY + 9), "シーズン M-3", font=get_font(18, bold=True), fill=BADGE_TXT)
    draw.text((LX + 2, LY + 48), "2026/06/18 〜", font=get_font(12), fill=META_GRAY)

    ty = LY + 72
    draw.rounded_rectangle([LX, ty, LX + 118, ty + 26], radius=13, outline=(200, 160, 190), width=1, fill=(255, 255, 255))
    draw.text((LX + 18, ty + 6), "シングルバトル", font=get_font(13), fill=(120, 80, 110))

    draw.text((LX, LY + 118), "使用率ランキング", font=get_font(11), fill=META_GRAY)
    y_info = LY + 134
    fonts_info = [get_font(12, bold=True), get_font(11), get_font(11)]
    colors_info = [cfg["row_hi"], META_GRAY, META_GRAY]
    for i, line in enumerate(cfg["left_lines"][:3]):
        draw.text((LX, y_info), line, font=fonts_info[i], fill=colors_info[i])
        y_info += 18

    RX = 200
    ROW_W = W - RX - 18
    font_rank  = get_font(28, bold=True)
    font_name  = get_font(17)
    font_name_h = get_font(18, bold=True)

    for i, entry in enumerate(cfg["entries"]):
        ry = 16 + i * (ROW_H + 6)
        is_hi = entry["hi"]
        shadow_c = cfg["shadow_hi"] if is_hi else (200, 200, 210)
        row_c    = cfg["row_hi"]    if is_hi else ROW_WHITE
        draw.rounded_rectangle([RX, ry + 3, RX + ROW_W, ry + ROW_H + 3], radius=14, fill=shadow_c)
        draw.rounded_rectangle([RX, ry,     RX + ROW_W, ry + ROW_H],     radius=14, fill=row_c)
        if is_hi:
            ax, ay = RX - 12, ry + ROW_H // 2
            draw.polygon([(ax, ay - 9), (ax + 11, ay), (ax, ay + 9)], fill=cfg["row_hi"])
        rank_c = (255, 255, 255) if is_hi else RANK_DARK
        draw.text((RX + 14, ry + ROW_H // 2 - 18), str(entry["rank"]), font=font_rank, fill=rank_c)
        ix, iy = RX + 62, ry + (ROW_H - ICON_SIZE) // 2
        icon = load_icon(entry["id"], ICON_SIZE)
        if icon:
            canvas.paste(icon, (ix, iy), icon)
        name_c = (255, 255, 255) if is_hi else NAME_DARK
        nfont  = font_name_h if is_hi else font_name
        draw.text((ix + ICON_SIZE + 10, ry + ROW_H // 2 - 11), entry["name"], font=nfont, fill=name_c)
        if is_hi:
            mk = load_icon(entry["id"], 32)
            if mk:
                canvas.paste(mk, (RX + ROW_W - 42, ry + (ROW_H - 32) // 2), mk)

    path = OUT / cfg["out"]
    canvas.save(path, "PNG")
    return path.name


def main():
    conn = sqlite3.connect(str(DB))
    cur  = conn.cursor()

    dexmap = {}
    for r in cur.execute("SELECT pokemon_name, dex_number, form_index FROM pokemon_base_stats"):
        dexmap[r[0]] = f"{int(r[1]):04d}-{int(r[2]):02d}"

    latest = cur.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single'", (SEASON,)
    ).fetchone()[0]

    usage_map = {}
    for r in cur.execute(
        "SELECT pokemon, rank FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=?",
        (SEASON, latest)
    ):
        usage_map[r[0]] = r[1]

    generated, skipped = [], []

    for md_file in sorted(BLOG.glob("*-analysis-m3.md")):
        slug = md_file.stem.replace("-analysis-m3", "")
        text = md_file.read_text()

        m = re.search(r"title:\s*['\"]?【ポケモンチャンピオンズ】([^考]+?)考察", text)
        if not m:
            skipped.append(f"{slug}: title parse failed"); continue
        raw = m.group(1).strip()
        raw = re.sub(r"^[\(（]メガ[\)）]", "", raw).strip()
        if not any(raw.startswith(p) for p in ["メガニウム", "メガヤンマ"]):
            raw = re.sub(r"^メガ", "", raw)
        raw = raw.replace("（", "(").replace("）", ")")

        db_name = SLUG_TO_DBNAME.get(slug, raw)
        rank    = usage_map.get(db_name)
        if not rank:
            skipped.append(f"{slug}: '{db_name}' not in usage_map"); continue

        type_row = cur.execute(
            "SELECT type1, type2 FROM pokemon_base_stats WHERE pokemon_name=? LIMIT 1", (db_name,)
        ).fetchone()
        type1 = type_row[0] if type_row else None
        type2 = type_row[1] if type_row else None
        palette = TYPE_PALETTE.get(type1) or TYPE_PALETTE.get(type2) or TYPE_PALETTE["ノーマル"]

        start = max(1, rank - 1)
        rows = cur.execute(
            "SELECT rank, pokemon FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=? AND rank BETWEEN ? AND ? ORDER BY rank LIMIT 4",
            (SEASON, latest, start, start + 3)
        ).fetchall()
        entries = []
        for r in rows:
            name = r[1].replace(":永遠", "(永遠)").replace(" (", "(")
            pid  = dexmap.get(r[1]) or dexmap.get(r[1].split("(")[0].strip())
            entries.append(dict(rank=r[0], name=name, id=pid, hi=(r[0] == rank)))

        if not entries:
            skipped.append(f"{slug}: no entries"); continue

        mega_row = cur.execute(
            "SELECT usage_rate FROM pokemon_items WHERE season=? AND rule='single' AND pokemon=? AND item LIKE '%ナイト%' ORDER BY usage_rate DESC LIMIT 1",
            (SEASON, db_name)
        ).fetchone()
        mega_rate = float(mega_row[0]) if mega_row and mega_row[0] else None

        type_text = type1 + ("/" + type2 if type2 else "") if type1 else ""
        line1 = f"#{rank}  {raw}"
        line2 = f"{type_text}タイプ" if type_text else "M-3 シーズン"
        line3 = f"メガ石採用率 {mega_rate:.1f}%" if mega_rate and mega_rate > 5 else "M-3 シーズン考察"

        cfg = dict(out=f"hero-{slug}-m3.png", **palette, left_lines=[line1, line2, line3], entries=entries)
        try:
            saved = generate(cfg)
            generated.append(saved)
        except Exception as e:
            skipped.append(f"{slug}: {e}")

    conn.close()
    print(f"\n=== 生成完了 {len(generated)} 件 ===")
    for s in generated: print(" ", s)
    if skipped:
        print(f"\n=== スキップ {len(skipped)} 件 ===")
        for s in skipped: print(" ", s)


if __name__ == "__main__":
    main()
