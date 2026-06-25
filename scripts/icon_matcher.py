"""
ポケモンアイコン参照画像比較モジュール
- build_refs(): crawlデータから参照アイコンを切り出してsave
- match_icon(img): 最も近い参照アイコンを返す
"""

import os
import math
from pathlib import Path
from PIL import Image

REF_DIR = Path(__file__).parent / "icon_refs"
ICON_SIZE = (64, 64)

# move_00.pngからメインポケモンアイコンを切り出す座標
MAIN_ICON_BOX = (980, 5, 1070, 110)

# partner_N.pngからパートナーアイコンを切り出す座標
# (x1, y_centers_per_page, x2, half_height)
PARTNER_ICON_X1 = 940
PARTNER_ICON_X2 = 1110
PARTNER_ICON_HALF_H = 65
PARTNER_ICON_Y_CENTERS = [385, 500, 622, 767, 867]


def _mse(img_a: Image.Image, img_b: Image.Image) -> float:
    a = img_a.resize(ICON_SIZE).convert("RGB")
    b = img_b.resize(ICON_SIZE).convert("RGB")
    pa, pb = list(a.getdata()), list(b.getdata())
    total = sum(
        (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
        for (r1,g1,b1),(r2,g2,b2) in zip(pa, pb)
    )
    return total / (ICON_SIZE[0] * ICON_SIZE[1] * 3)


def extract_main_icon(move_img_path: str) -> Image.Image:
    """move_00.pngからメインポケモンアイコンを切り出す"""
    return Image.open(move_img_path).crop(MAIN_ICON_BOX)


def extract_partner_icons(partner_img_path: str) -> list[Image.Image]:
    """partner_N.pngからパートナーアイコン5枚を切り出す"""
    img = Image.open(partner_img_path)
    icons = []
    for yc in PARTNER_ICON_Y_CENTERS:
        box = (PARTNER_ICON_X1, yc - PARTNER_ICON_HALF_H,
               PARTNER_ICON_X2, yc + PARTNER_ICON_HALF_H)
        icons.append(img.crop(box))
    return icons


def build_refs(crawl_dir: str, rank_to_pokemon: dict[int, str]):
    """
    確定済みのrank→pokemon名マッピングから参照アイコンを構築
    crawl_dir: /tmp/champ_crawl_YYYY-MM-DD
    rank_to_pokemon: {rank: pokemon_name}
    """
    REF_DIR.mkdir(exist_ok=True)
    saved = 0
    for rank, pokemon in rank_to_pokemon.items():
        move_path = f"{crawl_dir}/detail/{rank:03d}/move_00.png"
        if not os.path.exists(move_path):
            continue
        ref_path = REF_DIR / f"{pokemon}.png"
        if ref_path.exists():
            continue
        try:
            icon = extract_main_icon(move_path)
            icon.resize(ICON_SIZE).save(str(ref_path))
            saved += 1
        except Exception as e:
            print(f"  ⚠ rank={rank} {pokemon}: {e}")
    print(f"参照アイコン保存: {saved}件 → {REF_DIR}")


def load_refs() -> dict[str, Image.Image]:
    """参照アイコンをすべてロード"""
    refs = {}
    for p in REF_DIR.glob("*.png"):
        refs[p.stem] = Image.open(str(p)).convert("RGB")
    return refs


def match_icon(icon: Image.Image, refs: dict[str, Image.Image] | None = None,
               top_n: int = 3) -> list[tuple[str, float]]:
    """
    アイコン画像と参照セットを比較し、MSEが小さい順にtop_n件返す
    returns: [(pokemon_name, mse), ...]
    """
    if refs is None:
        refs = load_refs()
    scores = []
    for name, ref in refs.items():
        score = _mse(icon.convert("RGB"), ref)
        scores.append((name, score))
    scores.sort(key=lambda x: x[1])
    return scores[:top_n]


def identify_partner(partner_img_path: str, slot: int,
                     refs: dict[str, Image.Image] | None = None,
                     threshold: float = 2000) -> tuple[str | None, float]:
    """
    partner_N.pngのslot番目（0-4）のアイコンを識別
    threshold以下のMSEなら一致とみなす
    returns: (pokemon_name or None, mse)
    """
    icons = extract_partner_icons(partner_img_path)
    if slot >= len(icons):
        return None, float("inf")
    candidates = match_icon(icons[slot], refs, top_n=1)
    if not candidates:
        return None, float("inf")
    name, mse = candidates[0]
    return (name if mse <= threshold else None), mse


if __name__ == "__main__":
    import sqlite3, sys
    from pathlib import Path

    DB = Path(__file__).parent / "pokenavi.db"
    CRAWL_DATE = "2026-06-19"
    CRAWL_DIR = f"/tmp/champ_crawl_{CRAWL_DATE}"

    conn = sqlite3.connect(DB)
    rank_to_pokemon = {
        r[0]: r[1] for r in conn.execute(
            "SELECT rank, pokemon FROM pokemon_usage WHERE crawled_date=? AND rank <= 200",
            (CRAWL_DATE,)
        ).fetchall()
    }
    conn.close()

    build_refs(CRAWL_DIR, rank_to_pokemon)

    # テスト: 参照アイコン同士で自己一致確認
    refs = load_refs()
    print(f"\n参照アイコン総数: {len(refs)}")
    print("\n=== 自己一致テスト（上位3件）===")
    test_cases = list(refs.items())[:5]
    for name, img in test_cases:
        results = match_icon(img, refs)
        top = results[0]
        ok = "✓" if top[0] == name else f"✗ (got {top[0]})"
        print(f"  {name}: MSE={top[1]:.0f} {ok}")
