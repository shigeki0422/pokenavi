"""
アイコンテンプレートマッチングでポケモン名を識別してpokemon_usageに投入
RANK_OVERRIDESで上書き可能（パンプジン・フォーム違い等）
"""
import sqlite3, cv2, numpy as np
from pathlib import Path
from datetime import datetime, timezone

DB = Path(__file__).parent / "pokenavi.db"
CROP = (240, 10, 390, 135)

TEMPLATE_DATE = "2026-06-29"
TEMPLATE_DIR  = Path(f"/tmp/champ_crawl_{TEMPLATE_DATE}/detail")

SEASON = "M-3"
RULE   = "single"
MATCH_THRESHOLD = 0.80  # 通常フォーマット用
MATCH_THRESHOLD_GRAY = 0.20  # 横長フォーマット(6/28〜)用

# 処理対象日とRANK_OVERRIDES
TARGETS = {
    "2026-06-21": {
        # パンプジン等フォーム違い、アイコン低スコア箇所を実行後に追記
    },
    "2026-06-23": {
        196: "レントラー",
        200: "ツンベアー",
    },
    "2026-06-24": {
        200: "レントラー",
    },
    "2026-06-28": {
        200: "レントラー",
    },
    "2026-06-29": {
    },
    "2026-06-30": {
    },
    "2026-07-01": {
        199: "アーボック",
        200: "ゴロンダ",
    },
    "2026-07-02": {
        199: "アーボック",
    },
}

CRAWLED_DATE = "2026-07-02"  # ← 実行時に変更


REF_SIZE = (960, 965)  # 6/25の基準サイズ (w, h)

# 画像サイズごとのCROP座標 (x1, y1, x2, y2)
CROP_BY_SIZE = {
    (960, 965):   (240, 10, 390, 135),   # 通常サイズ
    (480, 482):   (240, 10, 390, 135),   # 半サイズ（リサイズ後に使用）
    (2400, 1080): (940, 5, 1075, 130),   # 6/28〜の横長フォーマット
}

def crop_icon(img_path):
    img = cv2.imread(str(img_path))
    if img is None:
        return None
    h, w = img.shape[:2]
    crop_coords = CROP_BY_SIZE.get((w, h))
    if crop_coords is None:
        # 未知サイズは基準サイズにリサイズ
        img = cv2.resize(img, REF_SIZE)
        crop_coords = CROP
    x1, y1, x2, y2 = crop_coords
    return img[y1:y2, x1:x2]


def build_templates(conn):
    rows = conn.execute(
        "SELECT rank, pokemon FROM pokemon_usage WHERE crawled_date=? AND season=? AND rule=? ORDER BY rank",
        (TEMPLATE_DATE, SEASON, RULE)
    ).fetchall()
    templates = {}
    for rank, pokemon in rows:
        img_path = TEMPLATE_DIR / f"{rank:03d}" / "_c_ability_00.png"
        if not img_path.exists():
            continue
        icon = crop_icon(img_path)
        if icon is not None:
            templates[pokemon] = icon
    return templates


def match_icon(icon, templates, use_gray=False):
    if use_gray and len(icon.shape) == 3:
        icon = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)

    best_name, best_score = None, 0.0
    for pokemon, template in templates.items():
        t = template
        if use_gray and len(t.shape) == 3:
            t = cv2.cvtColor(t, cv2.COLOR_BGR2GRAY)
        if t.shape != icon.shape:
            t = cv2.resize(t, (icon.shape[1], icon.shape[0]))
        res = cv2.matchTemplate(icon, t, cv2.TM_CCOEFF_NORMED)
        score = float(res.max())
        if score > best_score:
            best_score = score
            best_name = pokemon
    return best_name, best_score


import datetime as _datetime

LARGE_FORMAT_SINCE = _datetime.date(2026, 6, 28)

def main():
    overrides = TARGETS.get(CRAWLED_DATE, {})
    target_dir = Path(f"/tmp/champ_crawl_{CRAWLED_DATE}/detail")
    use_gray = _datetime.date.fromisoformat(CRAWLED_DATE) >= LARGE_FORMAT_SINCE
    match_threshold = MATCH_THRESHOLD_GRAY if use_gray else MATCH_THRESHOLD

    conn = sqlite3.connect(DB)
    pokemon_master = set(r[0] for r in conn.execute("SELECT pokemon_name FROM pokemon_base_stats"))

    print(f"=== {CRAWLED_DATE} テンプレート構築 ===")
    templates = build_templates(conn)
    print(f"テンプレート: {len(templates)}件")

    print(f"\n=== {CRAWLED_DATE} アイコンマッチング ===")
    matched = {}
    no_image = []
    low_score = []

    for rank in range(1, 201):
        rank_dir = target_dir / f"{rank:03d}"
        img_path = rank_dir / "_c_ability_00.png"
        if not img_path.exists():
            img_path = rank_dir / "ability_00.png"
        if not img_path.exists():
            no_image.append(rank)
            continue

        # RANK_OVERRIDESが設定されていればマッチングをスキップ
        if rank in overrides:
            matched[rank] = (overrides[rank], 1.0, "override")
            continue

        icon = crop_icon(img_path)
        if icon is None:
            no_image.append(rank)
            continue

        name, score = match_icon(icon, templates, use_gray=use_gray)
        matched[rank] = (name, score, "match")
        if score < match_threshold:
            low_score.append((rank, name, score))

    # 画像なし
    if no_image:
        print(f"🚨 画像なし: rank={no_image}")

    # 低スコア
    if low_score:
        print(f"\n⚠ 類似度低 (<{MATCH_THRESHOLD}): {len(low_score)}件")
        for rank, name, score in sorted(low_score, key=lambda x: x[2]):
            print(f"  rank={rank:3d} → {name} (score={score:.3f})")
            print(f"    画像: {target_dir}/{rank:03d}/_c_ability_00.png")

    # 重複チェック
    seen = {}
    dupes = []
    master_miss = []
    candidates = []

    for rank in sorted(matched):
        name, score, method = matched[rank]
        if name not in pokemon_master:
            master_miss.append((rank, name))
            continue
        if name in seen:
            dupes.append((rank, name, seen[name]))
        else:
            seen[name] = rank
            candidates.append((rank, name))

    if master_miss:
        print(f"\n🚨 マスター不一致: {[(r, n) for r, n in master_miss]}")

    if dupes:
        print(f"\n🚨 重複あり: {len(dupes)}件")
        for rank, name, first in dupes:
            print(f"  rank={rank} {name} (rank={first}と重複)")
            print(f"    画像: {target_dir}/{rank:03d}/_c_ability_00.png")
            print(f"    画像: {target_dir}/{first:03d}/_c_ability_00.png")
        print(f"\n🚫 投入中止: RANK_OVERRIDES_BY_DATE[\"{CRAWLED_DATE}\"]に追加して再実行")
        conn.close()
        return

    if len(candidates) < 200:
        print(f"\n🚫 投入中止: {len(candidates)}件（200件必須）")
        conn.close()
        return

    # POKEMON_DATAからpokemon_idを引く
    from generate_pokemon_pages import POKEMON_DATA
    id_map = {name: data.get("id") for name, data in POKEMON_DATA.items()}

    print(f"\n✅ 重複なし・200件確認 → 投入開始")
    now = datetime.now(timezone.utc).isoformat()
    inserted = 0
    for rank, name in candidates:
        pid = id_map.get(name)
        conn.execute(
            "INSERT OR IGNORE INTO pokemon_usage(season,rule,rank,pokemon,pokemon_id,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?)",
            (SEASON, RULE, rank, name, pid, "champions_adb", CRAWLED_DATE, now)
        )
        inserted += conn.execute("SELECT changes()").fetchone()[0]
    conn.commit()
    conn.close()
    print(f"pokemon_usage: {inserted}件投入")


if __name__ == "__main__":
    main()
