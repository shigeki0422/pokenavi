"""
アイコンテンプレートマッチングでポケモン名を識別してpokemon_usageに投入
RANK_OVERRIDESで上書き可能（パンプジン・フォーム違い等）
"""
import sqlite3, cv2, numpy as np
from pathlib import Path
from datetime import datetime, timezone

DB = Path(__file__).parent / "pokenavi.db"
CROP = (240, 10, 390, 135)

TEMPLATE_DATE = None  # build_templates() 内で自動決定

SEASON = "M-5"
RULE   = "single"
MATCH_THRESHOLD = 0.80  # 通常フォーマット用
MATCH_THRESHOLD_GRAY = 0.20  # 横長フォーマット(6/28〜)用

# _c_move_00.pngからメインアイコンを切り出す座標
# MAIN_ICON_BOX(980,5,1070,110) - CROP_BOX.x1(720)
ICON_BOX = (260, 5, 350, 110)
ICON_SIZE = (64, 64)

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
    "2026-07-03": {
        57: "ヒスイゾロアーク",
        92: "ガラルヤドキング",
        162: "ヤドキング",
        163: "ゾロアーク",
        174: "ニャオニクス(オス)",
        195: "トリデプス",
        197: "アーボック",
        198: "ブースター",
    },
    "2026-07-04": {
        117: "ウェーニバル",
        130: "ヒスイジュナイパー",
        171: "タイレーツ",
        175: "ニャオニクス(オス)",
        178: "エンブオー",
        179: "クレベース",
        183: "マホイップ",
        184: "リーフィア",
        185: "サダイジャ",
        186: "ケンタロス:水",
        187: "ロズレイド",
        189: "エモンガ",
        190: "ガチゴラス",
        193: "バクーダ",
        194: "トリデプス",
        195: "ヒスイクレベース",
        196: "アーボック",
        197: "ドクロッグ",
        198: "ブースター",
        199: "ゴロンダ",
        200: "フラージェス",
    },
}

CRAWLED_DATE = "2026-08-22"  # ← 実行時に変更

TARGETS["2026-07-09"] = {
    124: "ケンタロス:炎",
    182: "パンプジン(ギガだましゅ)",
}

TARGETS["2026-07-10"] = {
    124: "ケンタロス:炎",
}

TARGETS["2026-07-11"] = {
    122: "ケンタロス:炎",
}

TARGETS["2026-07-12"] = {
    118: "ケンタロス:炎",
}

TARGETS["2026-07-13"] = {
    118: "ケンタロス:炎",
}

TARGETS["2026-07-14"] = {
    1: "ガブリアス",
    122: "ケンタロス:炎",
    200: "ケンタロス",
}

TARGETS["2026-07-15"] = {
    123: "ケンタロス:炎",
    200: "ケンタロス",
}

TARGETS["2026-07-16"] = {
    1: "ガブリアス",
    122: "ケンタロス:炎",
}

TARGETS["2026-07-17"] = {
    122: "ケンタロス:炎",
}


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


def extract_main_icon(rank_dir: Path) -> np.ndarray | None:
    """アイコン画像からメインポケモンアイコンを切り出して64x64にリサイズ"""
    for fname in ["_c_move_00.png", "move_00.png", "_c_ability_00.png", "ability_00.png"]:
        img_path = rank_dir / fname
        if img_path.exists():
            break
    else:
        img_path = rank_dir / "_c_move_00.png"
    icon = crop_icon(img_path)
    if icon is None:
        return None
    return cv2.resize(icon, ICON_SIZE)


REF_DIR = Path(__file__).parent / "icon_refs"

def build_templates(conn):
    # 直前の投入済み日付をDBから自動取得
    row = conn.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule=? AND crawled_date<?",
        (SEASON, RULE, CRAWLED_DATE)
    ).fetchone()
    template_date = row[0] if row and row[0] else None
    if template_date is None:
        print("⚠ テンプレート用の直前データなし")
        return {}
    template_dir = Path(f"/Users/shigeki/work/pokenavi/crawl_data/champ_crawl_{template_date}/detail")
    print(f"テンプレート日付: {template_date}")

    rows = conn.execute(
        "SELECT rank, pokemon FROM pokemon_usage WHERE crawled_date=? AND season=? AND rule=? ORDER BY rank",
        (template_date, SEASON, RULE)
    ).fetchall()
    templates = {}
    for rank, pokemon in rows:
        for fname in ["move_00.png", "_c_move_00.png", "_c_ability_00.png"]:
            img_path = template_dir / f"{rank:03d}" / fname
            if img_path.exists():
                break
        else:
            continue
        icon = crop_icon(img_path)
        if icon is not None:
            templates[pokemon] = cv2.resize(icon, ICON_SIZE)
    return templates


def match_icon(icon, templates, use_gray=False):
    best_name, best_score = None, 0.0
    for pokemon, template in templates.items():
        t = template
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
    target_dir = Path(f"/Users/shigeki/work/pokenavi/crawl_data/champ_crawl_{CRAWLED_DATE}/detail")

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

        # RANK_OVERRIDESが設定されていればマッチングをスキップ
        if rank in overrides:
            matched[rank] = (overrides[rank], 1.0, "override")
            continue

        icon = extract_main_icon(rank_dir)
        if icon is None:
            no_image.append(rank)
            continue

        name, score = match_icon(icon, templates)
        matched[rank] = (name, score, "match")
        if score < MATCH_THRESHOLD:
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



TARGETS["2026-07-30"] = {
    35: "ウルガモス",
    36: "ミミロップ",
    37: "メガニウム",
    38: "オーロンゲ",
    39: "ニンフィア",
    40: "フシギバナ",
    41: "クチート",
    42: "ドリュウズ",
    43: "ソウブレイズ",
    44: "ペリッパー",
    45: "エルフーン",
    46: "ドヒドイデ",
    47: "バンギラス",
    48: "ピクシー",
    49: "スコヴィラン",
    50: "カメックス",
    51: "オオニューラ",
    52: "クエスパトラ",
    53: "フラエッテ(永遠)",
    54: "ドラミドロ",
    55: "イッカネズミ",
    56: "バイバニラ",
    57: "ヒートロトム",
    58: "カビゴン",
    59: "マンムー",
    60: "コノヨザル",
    61: "ジュカイン",
    62: "ヒスイゾロアーク",
    63: "ミロカロス",
    64: "オニシズクモ",
    65: "ペンドラー",
    66: "ヤミラミ",
    67: "ヒスイヌメルゴン",
    68: "マリルリ",
    69: "ヤバソチャ",
    70: "メタモン",
    71: "ガルーラ",
    72: "ビビヨン",
    73: "ヤドラン",
    74: "バサギリ",
    75: "ジャローダ",
    76: "ジュペッタ",
    77: "エアームド",
    78: "ブリムオン",
    79: "サーナイト",
    80: "エルレイド",
    81: "ユキメノコ",
    82: "エンペルト",
    83: "ガオガエン",
    84: "ハリーマン",
    85: "ミミズズ",
    86: "グレンアルマ",
    87: "ラフレシア",
    88: "シャンデラ",
    89: "エーフィ",
    90: "ウツボット",
    91: "ハカドッグ",
    92: "ローブシン",
    93: "ズルズキン",
    94: "グライオン",
    95: "ドデカバシ",
    96: "ポットデス",
    97: "ホルード",
    98: "カエンジシ",
    99: "ヒスイウインディ",
    100: "ガラルヤドキング",
    101: "シビルドン",
    102: "ヘラクロス",
    103: "デカヌチャン",
    104: "イルカマン",
    105: "シャワーズ",
    106: "ランクルス",
    107: "プテラ",
    108: "サメハダー",
    109: "ボスゴドラ",
    110: "ブリガロン",
    111: "ウェーニバル",
    112: "ガラルヤドラン",
    113: "エレザード",
    114: "ユキノオー",
    115: "マニューラ",
    116: "カイロス",
    117: "ファイアロー",
    118: "ヒスイジュナイパー",
    119: "エンニュート",
    120: "イダイトウ(メス)",
    121: "オーダイル",
    122: "コータス",
    123: "フーディン",
    124: "カラマネロ",
    125: "ヒスイバクフーン",
    126: "チルタリス",
    127: "スピアー",
    128: "ルガルガン(たそがれ)",
    129: "ゴウカザル",
    130: "デスバーン",
    131: "ケンタロス:炎",
    132: "サンダース",
    133: "ルチャブル",
    134: "チリーン",
    135: "ウインディ",
    136: "バンバドロ",
    137: "グレイシア",
    138: "オニゴーリ",
    139: "ミカルゲ",
    140: "デスカーン",
    141: "ニョロトノ",
    142: "ドダイトス",
    143: "ジャラランガ",
    144: "カットロトム",
    145: "ワルビアル",
    146: "ブロスター",
    147: "ガメノデス",
    148: "ケケンカニ",
    149: "ピジョット",
    150: "クレッフィ",
    151: "アリアドス",
    152: "キョジオーン",
    153: "アマージョ",
    154: "オンバーン",
    155: "キュウコン",
    156: "チャーレム",
    157: "ハガネール",
    158: "カイリキー",
    159: "デンリュウ",
    160: "モルペコ",
    161: "ヘルガー",
    162: "ムシャーナ",
    163: "ペロリーム",
    164: "ゴルーグ",
    165: "フォレトス",
    166: "ヌメルゴン",
    167: "オーロット",
    168: "ヤドキング",
    169: "カミツオロチ",
    170: "ゾロアーク",
    171: "ジュナイパー",
    172: "アブソル",
    173: "サダイジャ",
    174: "ピカチュウ",
    175: "ロズレイド",
    176: "リキキリン",
    177: "ジジーロン",
    178: "ドサイドン",
    179: "マホイップ",
    180: "リーフィア",
    181: "アーボック",
    182: "ケンタロス:水",
    183: "タブンネ",
    184: "タイレーツ",
    185: "クレベース",
    186: "アマルルガ",
    187: "エモンガ",
    188: "フラージェス",
    189: "ニャオニクス(オス)",
    190: "バクーダ",
    191: "レパルダス",
    192: "ガチゴラス",
    193: "ライボルト",
    194: "バリコオル",
    195: "ゴロンダ",
    196: "バクフーン",
    197: "トリデプス",
    198: "マッギョ",
    199: "ブースター",
    200: "ドクロッグ",
}


TARGETS["2026-08-06"] = {
    166: "ナゲツケサル",
    197: "パンプジン(ちゅうだましゅ)",
}


TARGETS["2026-08-07"] = {
    60: "ヒスイゾロアーク",
    61: "エルレイド",
    62: "ヒートロトム",
    63: "コノヨザル",
    64: "ユキメノコ",
    65: "メタモン",
    66: "イッカネズミ",
    67: "ミロカロス",
    68: "ジュペッタ",
    69: "ヤドラン",
    70: "ミミズズ",
    71: "ヒスイヌメルゴン",
    72: "エンペルト",
    73: "オニシズクモ",
    74: "ビビヨン",
    75: "バサギリ",
    76: "ヤミラミ",
    77: "マリルリ",
    78: "サーナイト",
    79: "ジュカイン",
    80: "ジャローダ",
    81: "エアームド",
    82: "ドラミドロ",
    83: "ハリーマン",
    84: "ローブシン",
    85: "ホルード",
    86: "ブリムオン",
    87: "ガラルヤドキング",
    88: "ヤバソチャ",
    89: "ポットデス",
    90: "シャンデラ",
    91: "カエンジシ",
    92: "ヒスイウインディ",
    93: "ドデカバシ",
    94: "カイロス",
    95: "ガオガエン",
    96: "ランクルス",
    97: "ブリガロン",
    98: "ヘラクロス",
    99: "コータス",
    100: "エーフィ",
    101: "ハカドッグ",
    102: "グレンアルマ",
    103: "イルカマン",
    104: "イダイトウ(メス)",
    105: "ズルズキン",
    106: "デカヌチャン",
    107: "ボスゴドラ",
    108: "ユキノオー",
    109: "ラフレシア",
    110: "グライオン",
    111: "サメハダー",
    112: "シャワーズ",
    113: "ウェーニバル",
    114: "チルタリス",
    115: "ケンタロス:炎",
    116: "オーダイル",
    117: "エレザード",
    118: "マニューラ",
    119: "プテラ",
    120: "ヒスイジュナイパー",
    121: "ゴウカザル",
    122: "ルガルガン(たそがれ)",
    123: "ヤドキング",
    124: "シビルドン",
    125: "オニゴーリ",
    126: "スピアー",
    127: "オンバーン",
    128: "ワルビアル",
    129: "エンニュート",
    130: "ピジョット",
    131: "ウインディ",
    132: "カラマネロ",
    133: "ファイアロー",
    134: "チャーレム",
    135: "バンバドロ",
    136: "ニョロトノ",
    137: "フーディン",
    138: "ガラルヤドラン",
    139: "アリアドス",
    140: "タブンネ",
    141: "ケケンカニ",
    142: "ドダイトス",
    143: "ペロリーム",
    144: "グレイシア",
    145: "ムシャーナ",
    146: "ジャラランガ",
    147: "ルチャブル",
    148: "ヘルガー",
    149: "カイリキー",
    150: "キュウコン",
    151: "クレッフィ",
    152: "サンダース",
    153: "サダイジャ",
    154: "デスバーン",
    155: "ガメノデス",
    156: "カットロトム",
    157: "キョジオーン",
    158: "ブロスター",
    159: "オーロット",
    160: "ドサイドン",
    161: "デスカーン",
    162: "アマージョ",
    163: "バリコオル",
    164: "チリーン",
    165: "モルペコ",
    166: "アーボック",
    167: "ハガネール",
    168: "アブソル",
    169: "ケンタロス:水",
    170: "フォレトス",
    171: "リーフィア",
    172: "ピカチュウ",
    173: "レパルダス",
    174: "アマルルガ",
    175: "パンプジン(ギガだましゅ)",
    176: "ジュナイパー",
    177: "デデンネ",
    178: "ミカルゲ",
    179: "ゾロアーク",
    180: "フロストロトム",
    181: "ヒスイバクフーン",
    182: "デンリュウ",
    183: "ゴルーグ",
    184: "ロズレイド",
    185: "ヤナッキー",
    186: "ライボルト",
    187: "トリデプス",
    188: "マホイップ",
    189: "タイレーツ",
    190: "ダストダス",
    191: "バクーダ",
    192: "クレベース",
    193: "ラムパルド",
    194: "ジジーロン",
    195: "ゴロンダ",
    196: "ヌメルゴン",
    197: "ポワルン",
    198: "カミツオロチ",
    199: "ニャオニクス(メス)",
    200: "ナゲツケサル",
}


TARGETS["2026-08-08"] = {
    169: "エンブオー",
    200: "ジュナイパー",
}


TARGETS["2026-08-09"] = {
    169: "エンブオー",
    200: "ジュナイパー",
}

TARGETS["2026-08-10"] = {
    128: "オンバーン",
    129: "エンニュート",
    130: "オニゴーリ",
    131: "キュウコン",
    132: "チルタリス",
    133: "ピジョット",
    134: "カットロトム",
    135: "ジャラランガ",
    136: "ニョロトノ",
    137: "ルチャブル",
    138: "カラマネロ",
    139: "ウインディ",
    140: "ケケンカニ",
    141: "ワルビアル",
    142: "ヒスイバクフーン",
    143: "チリーン",
    144: "ドダイトス",
    145: "アリアドス",
    146: "デスバーン",
    147: "チャーレム",
    148: "グレイシア",
    149: "バンバドロ",
    150: "サンダース",
    151: "アマージョ",
    152: "ブロスター",
    153: "デンリュウ",
    154: "ハガネール",
    155: "ミカルゲ",
    156: "カイリキー",
    157: "ペロリーム",
    158: "デスカーン",
    159: "ガメノデス",
    160: "ムシャーナ",
    161: "ヘルガー",
    162: "クレッフィ",
    163: "ピカチュウ",
    164: "タブンネ",
    165: "フォレトス",
    166: "ロズレイド",
    167: "アーボック",
    168: "モルペコ",
    169: "クレベース",
    170: "キョジオーン",
    171: "エンブオー",
    172: "ドサイドン",
    173: "オーロット",
    174: "アブソル",
    175: "リーフィア",
    176: "ケンタロス:水",
    177: "ヌメルゴン",
    178: "ゴルーグ",
    179: "ゾロアーク",
    180: "カミツオロチ",
    181: "サダイジャ",
    182: "ライボルト",
    183: "ゴロンダ",
    184: "リキキリン",
    185: "ドクロッグ",
    186: "レパルダス",
    187: "バリコオル",
    188: "バクフーン",
    189: "マホイップ",
    190: "アマルルガ",
    191: "フラージェス",
    192: "ヒスイクレベース",
    193: "タイレーツ",
    194: "ジジーロン",
    195: "エモンガ",
    196: "マッギョ",
    197: "パンプジン(ギガだましゅ)",
    198: "ブースター",
    199: "ニャオニクス(オス)",
    200: "バクーダ",
}

TARGETS["2026-08-11"] = {}
TARGETS["2026-08-12"] = {}
TARGETS["2026-08-13"] = {
    200: "マツギヨ",
}
TARGETS["2026-08-15"] = {
    195: "ガチゴラス",
    200: "パンプジン(ギガだましゅ)",
}
TARGETS["2026-08-16"] = {}
TARGETS["2026-08-17"] = {}
TARGETS["2026-08-18"] = {}
TARGETS["2026-08-19"] = {
    200: "ツンベアー",
}

TARGETS["2026-08-20"] = {
    199: "ツンベアー",
}

TARGETS["2026-08-21"] = {
    199: "ツンベアー",
}

TARGETS["2026-08-22"] = {}

if __name__ == "__main__":
    main()
