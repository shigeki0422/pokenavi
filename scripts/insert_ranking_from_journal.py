"""
ランキングonly軽量投入スクリプト
pokemon_usageのみ投入（技/持ち物/EV等は投入しない）

GATE1: 同日同名重複 → 下位rankをスキップ
GATE_DELTA: 基準日との順位差が閾値超え → ハードブロック（フォーム誤認の可能性）
"""
import json, sqlite3, glob
from pathlib import Path

DB = Path(__file__).parent / "pokenavi.db"

WF_DIR = "/Users/shigeki/.claude/projects/-Users-shigeki-work/5c9e5884-44f0-4cfa-ae54-b0230dd188ae/subagents/workflows/wf_709c6a18-015"

CRAWLED_DATE = "2026-06-27"
SEASON = "M-3"
RULE = "single"
SOURCE = "champions_detail"

# 基準日との順位差がこれを超えるとハードブロック
DELTA_THRESHOLD = 80

OCR_POKEMON = {
    "トクロッグ": "ドクロッグ",
    "ウインティ": "ヒスイウインディ",
    "ザザンドラ": "サザンドラ",
    "プロスター": "ブロスター",
    "ベンダラー": "ペンドラー",
    "プリジュラス": "ブリジュラス",
    "バリッパー": "ペリッパー",
    "シャンテラ": "シャンデラ",
    "フーティン": "フーディン",
    "ソロアーク": "ゾロアーク",
    "クラベル": "クチート",
    "グラート": "クチート",
    "バンドラー": "ペンドラー",
    "フーティイン": "フーディン",
    "プリムオン": "ブリムオン",
    "エンベルト": "エンペルト",
    "ウルピアル": "ワルビアル",
    "ウルビアル": "ワルビアル",
    "パイパニラ": "バイバニラ",
    "ズルクスキン": "ズルズキン",
    "テスバーン": "デスバーン",
    "テスパーン": "デスバーン",
    "サムハダー": "サメハダー",
    "サダイハダー": "サメハダー",
    "オーロング": "オーロンゲ",
    "ジバルドン": "シビルドン",
    "ポルード": "ホルード",
    "ボットデス": "ポットデス",
    "ドデカバン": "ドデカバシ",
    "ビビコン": "ビビヨン",
    "ガイオガエン": "ガオガエン",
    "ダルッブル": "タルップル",
    "バンギリス": "バサギリ",
    "ラプレシア": "ラフレシア",
    "ワインティ": "ヒスイウインディ",
    "ブジーロン": "ジジーロン",
    "ジャランガ": "ジャラランガ",
    "ライチウ": "ライチュウ",
    "ライチウウ": "ライチュウ",
    "コノヤザル": "コノヨザル",
    "コノヤル": "コノヨザル",
    "ジュナイバー": "ジュナイパー",
    "フリジュラス": "ブリジュラス",
    "フリガロン": "ブリガロン",
    "シャラランガ": "ジャラランガ",
    "ベリッバー": "ペリッパー",
    "ベリッパー": "ペリッパー",
    "ベンドラー": "ペンドラー",
    "ドテカバシ": "ドデカバシ",
    "ドラバルト": "ドラパルト",
    "カメノテス": "ガメノデス",
    "パシャーモ": "バシャーモ",
    "ジュベッタ": "ジュペッタ",
    "ズルスキン": "ズルズキン",
    "バロリーム": "ペロリーム",
    "ビジョット": "ピジョット",
    "ボウルツ": "ポワルン",
    "マボイツツ": "マホイップ",
    "ファンロトム": "ロトム",
    "デリーニャ": "ランクルス",
    "バリコンオル": "バリコオル",
    "パリコンオル": "バリコオル",
    "アブレーヌ": "アシレーヌ",
    "パイバニラ": "バイバニラ",
    "カイエンジン": "カエンジシ",
    "ロープシン": "ローブシン",
    "ワインディ": "ヒスイウインディ",
    "イツカネズミ": "イッカネズミ",
    "ラブレシア": "ラフレシア",
    "ガルビアル": "ガブリアス",
    "グレッフィ": "クレッフィ",
    "エアニュート": "エンニュート",
    "ブジンロン": "ジジーロン",
    "ドナイドン": "ドサイドン",
    "マッキョ": "マッギョ",
    "ダルップル": "タルップル",
    "グレバース": "クレベース",
    "トリテプス": "トリデプス",
    "フラエッテ": "フラエッテ(永遠)",
    "ミミツキ": "ミミッキュ",
    "ミミツキュ": "ミミッキュ",
    "ラムバルド": "ラムパルド",
    "テンリュウ": "デンリュウ",
    "フーテイン": "フーディン",
    "ベンダー": "ペンドラー",
    "ピビヨン": "ビビヨン",
    "テスカーン": "デスカーン",
    "テテンネ": "デデンネ",
    "ボルード": "ホルード",
    "ボットレス": "ポットデス",
    "スビアー": "スピアー",
    "グレペース": "クレベース",
    "マボイップ": "マホイップ",
    "トデカバン": "ドデカバシ",
    "パロリーム": "ペロリーム",
    "ツンバアー": "ツンベアー",
    "デリーン": "チリーン",
    "ゲンダロス": "ケンタロス",
    "メデュエゴン": "メタモン",
    "フルップル": "タルップル",
    "イダイトウ": "イダイトウ(オス)",
    "ドタイトス": "ドダイトス",
    "パリッパー": "ペリッパー",
    "ジビルドン": "シビルドン",
    "バンギリ": "バサギリ",
    "カエンジン": "カエンジシ",
    "ラングルス": "ランクルス",
    "ジャジャンゴ": "ジャラランガ",
    "カイレキー": "カイリキー",
    "マッキヨ": "マッギョ",
    "マボイツブ": "マホイップ",
    "ルガルガン": "ルガルガン(たそがれ)",
    "ササンドラ": "サザンドラ",
    "ビビコン": "ビビヨン",
    "ガメノテス": "ガメノデス",
    "マツギョ": "マッギョ",
    "ウインデイ": "ウインディ",
    "ドヒドイア": "ドヒドイデ",
    "テカヌチャン": "デカヌチャン",
    "トリテブス": "トリデプス",
    "ウインテイ": "ウインディ",
    # haiku軽量OCR追加補正
    "ラクラージ": "ラグラージ",
    "バーバニラ": "バイバニラ",
    "ハリバーリー": "ハラバリー",
    "パンキラス": "バンギラス",
    "ドドドイア": "ドヒドイデ",
    "オーニスクメ": "オニシズクモ",
    "ジュガイン": "ジュカイン",
    "バウギリ": "バサギリ",
    "グレシャルマ": "グレンアルマ",
    "スルルスキン": "ズルズキン",
    "ガノンテス": "ガメノデス",
    "イヨヤイド": "イダイトウ",
    "テラヌスチャン": "デカヌチャン",
    "ボスコドラ": "ボスゴドラ",
    "デスバーシ": "デスバーン",
    "デスカーニ": "デスカーン",
    "ラッキルス": "ランクルス",
    "テルタリス": "チルタリス",
    "ジョウナイバー": "ジュナイパー",
    "ハチマロール": "ハガネール",
    "テリーン": "チリーン",
    "ミガルゲ": "ミカルゲ",
    "オーゴーリ": "オニゴーリ",
    "カニッツオロチ": "カミツオロチ",
    "パリコオル": "バリコオル",
    "パワーダ": "バクーダ",
}

# ランク番号で確定したフォーム名（日付別）
RANK_OVERRIDES_BY_DATE = {
    "2026-06-27": {
        11: "アローラキュウコン",
        6: "ライチュウ",
        138: "ドダイトス",
        92: "ガラルヤドキング",
        160: "ヤドキング",
        15: "イダイトウ(オス)",
        19: "ウォッシュロトム",
        49: "ヒートロトム",
        58: "ヒスイゾロアーク",
        96: "ヒスイウインディ",
        113: "カットロトム",
        114: "ウインディ",
        117: "ガラルヤドラン",
        14: "アシレーヌ",
        26: "クチート",
        33: "ダイケンキ",
        43: "フシギバナ",
        44: "カメックス",
        80: "ズルズキン",
        86: "ヒスイヌメルゴン",
        94: "ドデカバシ",
        110: "プテラ",
        118: "コータス",
        125: "ヒスイバクフーン",
        126: "ケンタロス:炎",
        137: "ルガルガン(昼)",
        143: "ケケンカニ",
        172: "ニャオニクス(オス)",
        183: "サダイジャ",
        184: "ケンタロス:水",
        104: "イダイトウ(メス)",
        190: "バクフーン",
        191: "フロストロトム",
        194: "パンプジン(ちゅうだましゅ)",
        196: "ヒスイクレベース",
        200: "レントラー",
    },
}


def load_ocr_results(wf_dir):
    results = {}
    for f in sorted(glob.glob(f"{wf_dir}/*.jsonl")):
        with open(f) as fp:
            for line in fp:
                try:
                    d = json.loads(line)
                    if d.get("type") == "assistant":
                        for block in d.get("message", {}).get("content", []) or []:
                            if (isinstance(block, dict)
                                    and block.get("type") == "tool_use"
                                    and block.get("name") == "StructuredOutput"):
                                inp = block.get("input", {})
                                if "rank" in inp and "pokemon" in inp:
                                    results[inp["rank"]] = inp
                except Exception:
                    pass
    return results


def apply_corrections(rank, raw_name, overrides):
    if rank in overrides:
        return overrides[rank]
    return OCR_POKEMON.get(raw_name, raw_name)


def load_reference(conn, ref_date):
    cur = conn.execute(
        "SELECT pokemon, rank FROM pokemon_usage WHERE crawled_date=? AND season=? AND rule=?",
        (ref_date, SEASON, RULE)
    )
    return {row[0]: row[1] for row in cur.fetchall()}


def get_reference_date(conn):
    cur = conn.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE crawled_date<? AND season=? AND rule=?",
        (CRAWLED_DATE, SEASON, RULE)
    )
    row = cur.fetchone()
    return row[0] if row else None


def check_master(conn, name):
    cur = conn.execute(
        "SELECT count(*) FROM pokemon_usage WHERE pokemon=? AND season=? AND rule=?",
        (name, SEASON, RULE)
    )
    return cur.fetchone()[0] > 0


def main():
    ocr = load_ocr_results(WF_DIR)
    print(f"OCR取得: {len(ocr)}件")

    overrides = RANK_OVERRIDES_BY_DATE.get(CRAWLED_DATE, {})

    conn = sqlite3.connect(DB)
    ref_date = get_reference_date(conn)
    print(f"基準日: {ref_date}")
    ref_map = load_reference(conn, ref_date) if ref_date else {}

    inserted = 0
    candidates = []
    skipped_gate1 = []
    skipped_delta = []
    skipped_miss = []
    seen = {}  # pokemon_name → rank

    import datetime
    crawled_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

    for rank in sorted(ocr.keys()):
        raw = ocr[rank]
        raw_name = raw.get("pokemon", "")
        name = apply_corrections(rank, raw_name, overrides)

        # GATE_MISS: マスター不一致
        if not check_master(conn, name):
            skipped_miss.append((rank, name, raw_name))
            continue

        # GATE1: 同日重複 → ハードブロック（フォーム誤認またはOCR誤読）
        if name in seen:
            skipped_gate1.append((rank, name, seen[name]))
            continue
        seen[name] = rank

        # GATE_DELTA: 基準日との順位差（RANK_OVERRIDESで画像確認済みのrankはスキップ）
        if rank not in overrides and name in ref_map:
            delta = abs(rank - ref_map[name])
            if delta > DELTA_THRESHOLD:
                skipped_delta.append((rank, name, ref_map[name], delta))
                continue

        candidates.append((rank, name))

    # 200件未満ならコミットしない
    if len(candidates) < 200:
        conn.close()
        print(f"\n🚫 投入中止: {len(candidates)}件（200件必須）")
    else:
        for rank, name in candidates:
            try:
                conn.execute(
                    """INSERT OR IGNORE INTO pokemon_usage
                       (season, rule, rank, pokemon, pokemon_id, usage_rate, source, crawled_date, crawled_at)
                       VALUES (?, ?, ?, ?, NULL, NULL, ?, ?, ?)""",
                    (SEASON, RULE, rank, name, SOURCE, CRAWLED_DATE, crawled_at)
                )
                if conn.execute("SELECT changes()").fetchone()[0]:
                    inserted += 1
            except Exception as e:
                print(f"  INSERT ERROR rank={rank} {name}: {e}")
        conn.commit()
        conn.close()
        print(f"\npokemon_usage: {inserted}件投入")

    if skipped_gate1:
        print(f"\n🚨 [GATE1] 重複ブロック: {len(skipped_gate1)}件")
        print(f"  ※ フォーム誤認またはOCR誤読。RANK_OVERRIDES_BY_DATE['{CRAWLED_DATE}']で両rankのフォームを明示して再実行。")
        for rank, name, first_rank in skipped_gate1:
            print(f"  rank={rank} {name} (rank={first_rank}と重複)")
            print(f"    画像: /tmp/champ_crawl_{CRAWLED_DATE}/detail/{str(rank).zfill(3)}/_c_ability_00.png")
            print(f"    画像: /tmp/champ_crawl_{CRAWLED_DATE}/detail/{str(first_rank).zfill(3)}/_c_ability_00.png")

    if skipped_delta:
        print(f"\n🚨 [GATE_DELTA] 順位変動大 (>{DELTA_THRESHOLD}位) ハードブロック: {len(skipped_delta)}件")
        print(f"  ※ フォーム誤認の可能性。RANK_OVERRIDES_BY_DATE['{CRAWLED_DATE}']に追加して再実行。")
        for rank, name, ref_rank, delta in sorted(skipped_delta, key=lambda x: -x[3]):
            print(f"  rank={rank} {name} ← 基準日rank={ref_rank} (差={delta})")
            print(f"    画像: /tmp/champ_crawl_{CRAWLED_DATE}/detail/{str(rank).zfill(3)}/_c_ability_00.png")

    if skipped_miss:
        print(f"\n⚠ [GATE_MISS] マスター不一致: {len(skipped_miss)}件")
        for rank, name, raw in skipped_miss:
            print(f"  rank={rank}: OCR='{raw}' → 補正後='{name}'")

    # 完全性チェック
    import sqlite3 as _sq
    conn2 = _sq.connect(DB)
    total = conn2.execute(
        "SELECT count(*) FROM pokemon_usage WHERE crawled_date=? AND season=? AND rule=?",
        (CRAWLED_DATE, SEASON, RULE)
    ).fetchone()[0]
    conn2.close()
    print(f"\n=== DB合計: {total}件 ===")
    missing = sorted(set(range(1, 201)) - set(ocr.keys()))
    if missing:
        print(f"🚨 OCR未取得rank: {missing}")


if __name__ == "__main__":
    main()
