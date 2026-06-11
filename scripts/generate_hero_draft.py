"""
ドラフト39記事のhero画像を、公開済みメガ進化記事と同じフォーマット
（720x360px・使用率ランキング表）で一括生成。

使い方: /usr/bin/python3 scripts/generate_hero_draft.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sqlite3
import re

ROOT = Path(__file__).parent.parent
ICONS = ROOT / "public" / "images" / "pokemon"
OUT = ROOT / "src" / "assets"
BLOG = ROOT / "src" / "content" / "blog"
DB = ROOT / "scripts" / "pokenavi.db"

W, H = 720, 360
ROW_H = 72
ICON_SIZE = 48

# 共通色
ROW_WHITE = (255, 255, 255)
RANK_DARK = (60, 60, 70)
NAME_DARK = (40, 40, 50)
META_GRAY = (140, 120, 140)
BADGE_TXT = (255, 255, 255)


# タイプ→カラーパレット
TYPE_PALETTE = {
    "ノーマル":   dict(bg_top=(245, 240, 220), bg_bot=(235, 225, 200), badge_bg=(160, 145, 110), row_hi=(180, 160, 120), shadow_hi=(130, 115, 80)),
    "ほのお":     dict(bg_top=(255, 220, 195), bg_bot=(245, 200, 170), badge_bg=(200, 70, 30),  row_hi=(220, 90, 40),  shadow_hi=(165, 45, 15)),
    "みず":       dict(bg_top=(195, 220, 255), bg_bot=(175, 205, 245), badge_bg=(40, 95, 195),  row_hi=(60, 120, 215), shadow_hi=(25, 70, 155)),
    "でんき":     dict(bg_top=(255, 245, 195), bg_bot=(250, 230, 165), badge_bg=(210, 170, 30), row_hi=(230, 190, 50), shadow_hi=(170, 130, 10)),
    "くさ":       dict(bg_top=(215, 245, 205), bg_bot=(195, 235, 185), badge_bg=(60, 145, 70),  row_hi=(80, 170, 90),  shadow_hi=(40, 110, 50)),
    "こおり":     dict(bg_top=(210, 240, 245), bg_bot=(190, 225, 235), badge_bg=(80, 165, 195), row_hi=(100, 185, 215),shadow_hi=(50, 130, 165)),
    "かくとう":   dict(bg_top=(255, 215, 200), bg_bot=(245, 200, 185), badge_bg=(180, 60, 40),  row_hi=(200, 80, 60),  shadow_hi=(140, 30, 15)),
    "どく":       dict(bg_top=(235, 215, 245), bg_bot=(220, 200, 235), badge_bg=(125, 70, 165), row_hi=(145, 90, 185), shadow_hi=(95, 45, 130)),
    "じめん":     dict(bg_top=(240, 225, 195), bg_bot=(225, 210, 175), badge_bg=(170, 130, 50), row_hi=(190, 150, 70), shadow_hi=(135, 95, 25)),
    "ひこう":     dict(bg_top=(220, 230, 255), bg_bot=(200, 215, 250), badge_bg=(95, 130, 200), row_hi=(115, 150, 220),shadow_hi=(65, 100, 165)),
    "エスパー":   dict(bg_top=(255, 220, 235), bg_bot=(250, 200, 220), badge_bg=(210, 85, 130), row_hi=(230, 105, 150),shadow_hi=(175, 55, 95)),
    "むし":       dict(bg_top=(220, 240, 195), bg_bot=(205, 230, 180), badge_bg=(110, 145, 55), row_hi=(130, 170, 75), shadow_hi=(80, 110, 30)),
    "いわ":       dict(bg_top=(235, 225, 195), bg_bot=(220, 210, 180), badge_bg=(150, 130, 75), row_hi=(170, 150, 95), shadow_hi=(115, 95, 45)),
    "ゴースト":   dict(bg_top=(220, 210, 240), bg_bot=(200, 190, 230), badge_bg=(95, 75, 145),  row_hi=(115, 95, 165), shadow_hi=(65, 50, 110)),
    "ドラゴン":   dict(bg_top=(215, 215, 250), bg_bot=(200, 200, 245), badge_bg=(85, 80, 195),  row_hi=(105, 100, 215),shadow_hi=(60, 55, 155)),
    "あく":       dict(bg_top=(220, 210, 200), bg_bot=(200, 190, 180), badge_bg=(95, 70, 55),   row_hi=(115, 90, 75),  shadow_hi=(65, 45, 30)),
    "はがね":     dict(bg_top=(220, 230, 235), bg_bot=(200, 215, 220), badge_bg=(115, 130, 145),row_hi=(135, 150, 165),shadow_hi=(80, 95, 110)),
    "フェアリー": dict(bg_top=(255, 220, 240), bg_bot=(250, 200, 225), badge_bg=(215, 95, 155), row_hi=(235, 115, 175),shadow_hi=(180, 65, 120)),
}


def get_font(size, bold=False):
    paths = [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc" if bold else "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


def load_icon(pokemon_id, size):
    path = ICONS / f"pokemon-{pokemon_id}.webp"
    if not path.exists():
        return None
    return Image.open(path).convert("RGBA").resize((size, size), Image.LANCZOS)


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


def extract_pokemon_name(text):
    """記事のtitleからポケモン名（メガ・括弧除く正規名）を抽出"""
    m = re.search(r"title:\s*['\"]?【ポケモンチャンピオンズ】([^考]+?)考察", text)
    if not m:
        return None
    name = m.group(1).strip()
    # 「（メガ）」プレフィックスを先に除去（メガニウムを誤って「ニウム」にしない）
    name = re.sub(r"^[\(（]メガ[\)）]", "", name).strip()
    # 「メガ」プレフィックスを除去するが、「メガニウム」「メガヤンマ」等の固有名は保護
    PROTECT = ["メガニウム", "メガヤンマ"]
    if not any(name.startswith(p) for p in PROTECT):
        name = re.sub(r"^メガ", "", name)
    # 全角括弧→半角括弧
    name = name.replace("（", "(").replace("）", ")")
    # 括弧前後のスペース正規化
    name = re.sub(r"\s*\(\s*", "(", name)
    return name.strip()


def fetch_pokemon_data(conn, name_jp):
    """DBから該当ポケモンの順位・タイプ・pokemon_id・メガ石採用率を取得"""
    cur = conn.cursor()
    # 括弧表記の正規化（「ヒスイ」「オス」など）
    # name_jp は半角括弧前提
    base = re.sub(r"\(.+?\)", "", name_jp).strip()
    suffix_m = re.search(r"\((.+?)\)", name_jp)
    suffix = suffix_m.group(1) if suffix_m else None

    candidates = [name_jp]
    if suffix:
        # DB登録パターン：「base (suffix)」「base(suffix)」
        candidates += [f"{base} ({suffix})", f"{base}({suffix})", base]
    else:
        candidates += [f"{name_jp} (オス)", f"{name_jp}(オス)",
                       f"{name_jp}:永遠", f"{name_jp} (永遠)",
                       f"{name_jp} (ヒスイ)", f"{name_jp}(ヒスイ)",
                       f"{name_jp} (アローラ)", f"{name_jp}(アローラ)"]
    row = None
    used_name = None
    for c in candidates:
        cur.execute("""
            SELECT rank, pokemon_id, pokemon FROM pokemon_usage
            WHERE season='M-2' AND rule='single' AND pokemon=?
              AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-2' AND rule='single')
            LIMIT 1
        """, (c,))
        row = cur.fetchone()
        if row and row[1]:
            used_name = c
            break
    if not row or not row[1]:
        return None

    rank, pid, dbname = row
    # タイプ
    type_candidates = [name_jp]
    if suffix:
        type_candidates += [suffix + base, base]
    for tc in type_candidates:
        cur.execute("""
            SELECT type1, type2 FROM pokemon_base_stats
            WHERE pokemon_name=? LIMIT 1
        """, (tc,))
        type_row = cur.fetchone()
        if type_row:
            break
    type1 = type_row[0] if type_row else None
    type2 = type_row[1] if type_row else None

    return dict(rank=rank, pokemon_id=pid, db_name=used_name, type1=type1, type2=type2)


def fetch_around(conn, rank):
    """指定順位の前後を含む4体を取得（ハイライト＝指定rank）"""
    cur = conn.cursor()
    # rank-1, rank, rank+1, rank+2 を基本（先頭/末尾調整）
    start = max(1, rank - 1)
    cur.execute("""
        SELECT rank, pokemon, pokemon_id FROM pokemon_usage
        WHERE season='M-2' AND rule='single' AND pokemon_id IS NOT NULL AND pokemon_id != ''
          AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-2' AND rule='single')
          AND rank BETWEEN ? AND ?
        ORDER BY rank
        LIMIT 4
    """, (start, start + 3))
    rows = cur.fetchall()
    return [dict(rank=r[0], name=clean_display_name(r[1]), id=r[2], hi=(r[0] == rank)) for r in rows]


def clean_display_name(name):
    """画像表示用にポケモン名を整形（フラエッテ:永遠 → フラエッテ(永遠) 等）"""
    name = name.replace(":永遠", "(永遠)")
    name = name.replace(" (", "(")
    return name


def fetch_mega_rate(conn, db_name):
    """対象ポケモンのメガ石採用率を取得（メガ進化対応の場合）"""
    cur = conn.cursor()
    cur.execute("""
        SELECT item, usage_rate FROM pokemon_items
        WHERE season='M-2' AND rule='single' AND pokemon=?
          AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_items WHERE season='M-2' AND rule='single' AND pokemon=?)
          AND item LIKE '%ナイト%'
        ORDER BY usage_rate DESC LIMIT 1
    """, (db_name, db_name))
    row = cur.fetchone()
    if row and row[1] is not None:
        return row[0], float(row[1])
    return None, None


def generate(cfg):
    canvas = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(canvas)
    draw_gradient(draw, W, H, cfg["bg_top"], cfg["bg_bot"])

    rgba = canvas.convert("RGBA")
    draw_diamonds(rgba, W, H)
    canvas = rgba.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    LX, LY = 22, 20

    # シーズン M-2 バッジ
    bw, bh = 145, 38
    draw.rounded_rectangle([LX, LY, LX + bw, LY + bh], radius=19, fill=cfg["badge_bg"])
    draw.text((LX + 14, LY + 9), "シーズン M-2", font=get_font(18, bold=True), fill=BADGE_TXT)

    # 日付
    draw.text((LX + 2, LY + 48), "2026/05/13 〜 06/17", font=get_font(12), fill=META_GRAY)

    # シングルバトル タグ
    ty = LY + 72
    draw.rounded_rectangle([LX, ty, LX + 118, ty + 26],
                           radius=13, outline=(200, 160, 190), width=1, fill=(255, 255, 255))
    draw.text((LX + 18, ty + 6), "シングルバトル", font=get_font(13), fill=(120, 80, 110))

    # 左パネル
    draw.text((LX, LY + 118), "使用率ランキング", font=get_font(11), fill=META_GRAY)
    y_info = LY + 134
    fonts_info = [get_font(12, bold=True), get_font(11), get_font(11)]
    colors_info = [cfg["row_hi"], META_GRAY, META_GRAY]
    for i, line in enumerate(cfg["left_lines"][:3]):
        f = fonts_info[i] if i < len(fonts_info) else get_font(11)
        c = colors_info[i] if i < len(colors_info) else META_GRAY
        draw.text((LX, y_info), line, font=f, fill=c)
        y_info += 18

    # 右パネル
    RX = 200
    ROW_W = W - RX - 18

    font_rank = get_font(28, bold=True)
    font_name = get_font(17)
    font_name_h = get_font(18, bold=True)

    for i, entry in enumerate(cfg["entries"]):
        ry = 16 + i * (ROW_H + 6)
        is_hi = entry["hi"]
        shadow_c = cfg["shadow_hi"] if is_hi else (200, 200, 210)
        row_c = cfg["row_hi"] if is_hi else ROW_WHITE
        draw.rounded_rectangle([RX, ry + 3, RX + ROW_W, ry + ROW_H + 3], radius=14, fill=shadow_c)
        draw.rounded_rectangle([RX, ry, RX + ROW_W, ry + ROW_H], radius=14, fill=row_c)

        if is_hi:
            ax = RX - 12
            ay = ry + ROW_H // 2
            draw.polygon([(ax, ay - 9), (ax + 11, ay), (ax, ay + 9)], fill=cfg["row_hi"])

        rank_c = (255, 255, 255) if is_hi else RANK_DARK
        draw.text((RX + 14, ry + ROW_H // 2 - 18), str(entry["rank"]), font=font_rank, fill=rank_c)

        ix = RX + 62
        iy = ry + (ROW_H - ICON_SIZE) // 2
        icon = load_icon(entry["id"], ICON_SIZE)
        if icon:
            canvas.paste(icon, (ix, iy), icon)

        name_c = (255, 255, 255) if is_hi else NAME_DARK
        nfont = font_name_h if is_hi else font_name
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
    generated = []
    skipped = []

    for md_file in sorted(BLOG.glob("*-analysis-m2.md")):
        text = md_file.read_text()
        if "draft: true" not in text:
            continue
        slug = md_file.stem.replace("-analysis-m2", "")
        name = extract_pokemon_name(text)
        if not name:
            skipped.append(f"{slug}: name extract failed")
            continue
        data = fetch_pokemon_data(conn, name)
        if not data:
            skipped.append(f"{slug}: db lookup failed for '{name}'")
            continue

        rank = data["rank"]
        type1 = data["type1"]
        type2 = data["type2"]

        # タイプ→パレット
        palette = TYPE_PALETTE.get(type1) or TYPE_PALETTE.get(type2) or TYPE_PALETTE["ノーマル"]

        # 左パネルテキスト
        if type1:
            type_text = type1 + ("/" + type2 if type2 else "")
        else:
            type_text = ""
        mega_item, mega_rate = fetch_mega_rate(conn, data["db_name"])

        line1 = f"#{rank}  {clean_display_name(data['db_name'])}"
        line2 = f"{type_text}タイプ" if type_text else "M-2 シーズン"
        if mega_rate and mega_rate > 5:
            line3 = f"メガ石採用率 {mega_rate:.1f}%"
        else:
            line3 = "M-2 シーズン考察"

        # 周辺ランキング
        entries = fetch_around(conn, rank)
        if not entries:
            skipped.append(f"{slug}: around fetch failed")
            continue

        cfg = dict(
            out=f"hero-{slug}-m2.png",
            **palette,
            left_lines=[line1, line2, line3],
            entries=entries,
        )
        try:
            saved = generate(cfg)
            generated.append(saved)
        except Exception as e:
            skipped.append(f"{slug}: generate error {e}")

    conn.close()
    print(f"\n=== 生成完了 {len(generated)} 件 ===")
    for s in generated:
        print(f"  {s}")
    if skipped:
        print(f"\n=== スキップ {len(skipped)} 件 ===")
        for s in skipped:
            print(f"  {s}")


if __name__ == "__main__":
    main()
