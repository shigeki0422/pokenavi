"""
journal.jsonlからM-3詳細データ（技/持ち物/特性/性格/EV/パートナー）をDB投入
OCR補正マッピング適用済み、マスター照合、INSERT OR IGNORE
"""
import json, sqlite3, glob
from datetime import datetime, timezone
from pathlib import Path

DB = Path(__file__).parent / "pokenavi.db"

WF_DIRS = [
    "/Users/shigeki/.claude/projects/-Users-shigeki-work/5c9e5884-44f0-4cfa-ae54-b0230dd188ae/subagents/workflows/wf_935ad6a9-410",
]

OCR_MOVES = {
    "てていこうせん": "てっていこうせん",
    "ここえるかぜ": "こごえるかぜ",
    "かいでんば": "かいでんぱ",
    "ウエーブタックル": "ウェーブタックル",
    "ウエザーボール": "ウェザーボール",
    "もろはのすつき": "もろはのずつき",
    "しねんのすつき": "しねんのずつき",
    "しねんのすずき": "しねんのずつき",
    "めさめるダンス": "めざめるダンス",
    "こうこうせい": "こうごうせい",
    "サンダータイプ": "サンダーダイブ",
    "フレイズキック": "ブレイズキック",
    "じこくづき": "じごくづき",
    "しこくづき": "じごくづき",
    "かんせきぶうじ": "がんせきふうじ",
    "ボルターガイスト": "ポルターガイスト",
    "ほうふう": "ぼうふう",
    "バラボラチャージ": "パラボラチャージ",
    "どくばりセンポン": "どくばりセンボン",
    "どくばりせんぽん": "どくばりセンボン",
    "すてぜりふ": "すてゼリフ",
    "あきのひざし": "あさのひざし",
    "しびれこな": "しびれごな",
    "ばくおんば": "ばくおんぱ",
    "とんぼかえり": "とんぼがえり",
    "みかわり": "みがわり",
    "ふううち": "ふいうち",
    "ふううち": "ふいうち",
    "ふういうち": "ふいうち",
    "ふういち": "ふいうち",
    "パレットパンチ": "バレットパンチ",
    "ねっぽう": "ねっぷう",
    "しごくづき": "じごくづき",
    "じこづくじ": "じごくづき",
    "しゅうでん": "じゅうでん",
    "へドロばくだん": "ヘドロばくだん",
    "へドロウェーブ": "ヘドロウェーブ",
    "ていていこうせん": "てっていこうせん",
    "ボルダーガイスト": "ポルターガイスト",
    "かむしゃら": "がむしゃら",
    "はめのひかり": "はめつのひかり",
    "したばた": "じたばた",
    "3ほんのや": "3ぼんのや",
    "ねっきのだいち": "ねっさのだいち",
    "どわすれ": "ドわすれ",
    "エネルギーボール": "エナジーボール",
    "オーラベール": "オーロラベール",
}
OCR_ITEMS = {
    "ヨブのみ": "ヨプのみ",
    "フーティナイト": "フーディナイト",
    "ジバルドナイト": "シビルドナイト",
    "ヤチエのみ": "ヤチェのみ",
    "バンドラナイト": "ペンドラナイト",
    "ピアーのみ": "ビアーのみ",
    "ユキノオート": "ユキノオナイト",
    "ビジョットナイト": "ピジョットナイト",
}
OCR_ABILITIES = {
    "すなかくれ": "すながくれ",
    "ふしぎなろこ": "ふしぎなうろこ",
    "どしよく": "どしょく",
    "ちからすく": "ちからずく",
    "かんじょう": "がんじょう",
    "はんずう": "はんすう",
    "ほうおん": "ほのおのからだ",
    "ほうじん": "ほうし",
    "てのこぶし": "てつのこぶし",
    "よりよくそ": "ようりょくそ",
}
OCR_NATURES = {
    "すぶとい": "ずぶとい", "すばとい": "ずぶとい", "すぼとい": "ずぶとい", "ずぼとい": "ずぶとい",
    "おくびよう": "おくびょう", "いっぱり": "いじっぱり", "のてんき": "のうてんき", "すばやい": "おくびょう",
}
OCR_POKEMON = {
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
    # パートナー名の誤読
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
    # 新規追加 (rank 151-232)
    "バロリーム": "ペロリーム",
    "ビジョット": "ピジョット",
    "ボウルツ": "ポワルン",
    "マボイツツ": "マホイップ",
    "ファンロトム": "ロトム",
    "デリーニャ": "ランクルス",
    "バリコンオル": "バリコオル",
    "パリコンオル": "バリコオル",
    "アブレーヌ": "アブソル",
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
    # パートナー追加補正
    "ミミツキ": "ミミッキュ",
    "ミミツキュ": "ミミッキュ",
    "ラムバルド": "ラムパルド",
    "テンリュウ": "デンリュウ",
    "フーテイン": "フーディン",
    "ベンダー": "ペンドラー",
    "ピビヨン": "ビビヨン",
    "テスカーン": "デスカーン",
    "テテンネ": "デデンネ",
}

CRAWLED_DATE = "2026-06-18"

def ev_spread(ev):
    parts = []
    for key, label in [("h","H"),("a","A"),("b","B"),("c","C"),("d","D"),("s","S")]:
        v = ev.get(key, 0)
        if v:
            parts.append(f"{label}{v}")
    return "-".join(parts) if parts else "無振り"

def extract_structured_outputs(jsonl_path):
    results = []
    with open(jsonl_path) as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = d.get("message", {})
            content = msg.get("content", [])
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") == "StructuredOutput":
                    inp = c.get("input", {})
                    if "rank" in inp and "pokemon" in inp:
                        results.append(inp)
    return results

def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")

    move_master = set(r[0] for r in conn.execute("SELECT name_jp FROM move_master"))
    item_master = set(r[0] for r in conn.execute("SELECT name_jp FROM item_master"))
    ability_master = set(r[0] for r in conn.execute("SELECT name_jp FROM ability_master"))
    pokemon_master = set(r[0] for r in conn.execute("SELECT pokemon_name FROM pokemon_base_stats"))

    now = datetime.now(timezone.utc).isoformat()

    # 重複を避けるため最新のrank→dataをキープ（後のWFが正しい）
    all_data = {}
    for wf_dir in WF_DIRS:
        for jsonl in sorted(glob.glob(f"{wf_dir}/*.jsonl")):
            for rec in extract_structured_outputs(jsonl):
                rank = rec["rank"]
                if rank not in all_data:
                    all_data[rank] = rec

    print(f"Journal から取得: {len(all_data)} ランク")
    total_ranks = max(all_data.keys()) if all_data else 0
    missing_ranks = [r for r in range(1, total_ranks + 1) if r not in all_data]
    if missing_ranks:
        print(f"  ⚠ 欠落ランク: {missing_ranks}")

    # pokemon_usage 投入（journalのrank+pokemon名から）
    usage_inserted = 0
    for rank in sorted(all_data.keys()):
        rec = all_data[rank]
        pokemon_raw = rec["pokemon"]
        pokemon = OCR_POKEMON.get(pokemon_raw, pokemon_raw)
        if pokemon in pokemon_master:
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_usage(season,rule,rank,pokemon,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?)",
                ("M-3","single",rank,pokemon,"champions_adb",CRAWLED_DATE,now)
            )
            usage_inserted += conn.execute("SELECT changes()").fetchone()[0]
    conn.commit()
    print(f"pokemon_usage: {usage_inserted}件投入")

    # rankからpokemon_usageの正式名を引くルックアップ（フォーム違い対応）
    rank_to_pokemon = {}
    for row in conn.execute(
        "SELECT rank, pokemon FROM pokemon_usage WHERE season='M-3' AND rule='single' AND crawled_date=?",
        (CRAWLED_DATE,)
    ):
        rank_to_pokemon[row[0]] = row[1]

    move_unknown = set()
    item_unknown = set()
    ability_unknown = set()
    partner_unknown = set()
    inserted = {t: 0 for t in ["moves","items","abilities","natures","evs","partners"]}
    skipped_pokemon = []

    for rank in sorted(all_data.keys()):
        rec = all_data[rank]
        pokemon_raw = rec["pokemon"]
        pokemon = OCR_POKEMON.get(pokemon_raw, pokemon_raw)

        # フォーム付きポケモン（イダイトウ(オス/メス)等）はusageテーブルから正式名を取得
        if pokemon not in pokemon_master and rank in rank_to_pokemon:
            usage_name = rank_to_pokemon[rank]
            if usage_name in pokemon_master:
                pokemon = usage_name

        if pokemon not in pokemon_master:
            skipped_pokemon.append((rank, pokemon_raw, pokemon))
            continue

        for i, m in enumerate(rec.get("moves", []), 1):
            name = OCR_MOVES.get(m["name"], m["name"])
            if name not in move_master:
                move_unknown.add(name)
                continue
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_moves(season,rule,pokemon,rank,move,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,name,m["rate"],"champions_adb",CRAWLED_DATE,now)
            )
            inserted["moves"] += conn.execute("SELECT changes()").fetchone()[0]

        for i, it in enumerate(rec.get("items", []), 1):
            name = OCR_ITEMS.get(it["name"], it["name"])
            if name not in item_master:
                item_unknown.add(name)
                continue
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_items(season,rule,pokemon,rank,item,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,name,it["rate"],"champions_adb",CRAWLED_DATE,now)
            )
            inserted["items"] += conn.execute("SELECT changes()").fetchone()[0]

        for i, ab in enumerate(rec.get("abilities", []), 1):
            name = OCR_ABILITIES.get(ab["name"], ab["name"])
            if name not in ability_master:
                ability_unknown.add(name)
                continue
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_abilities(season,rule,pokemon,rank,ability,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,name,ab["rate"],"champions_adb",CRAWLED_DATE,now)
            )
            inserted["abilities"] += conn.execute("SELECT changes()").fetchone()[0]

        for i, na in enumerate(rec.get("natures", []), 1):
            nat = OCR_NATURES.get(na["name"], na["name"])
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_natures(season,rule,pokemon,rank,nature,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,nat,na["rate"],"champions_adb",CRAWLED_DATE,now)
            )
            inserted["natures"] += conn.execute("SELECT changes()").fetchone()[0]

        for i, ev in enumerate(rec.get("evs", []), 1):
            spread = ev_spread(ev)
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_evs(season,rule,pokemon,rank,ev_spread,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,spread,
                 ev.get("h",0),ev.get("a",0),ev.get("b",0),ev.get("c",0),ev.get("d",0),ev.get("s",0),
                 ev["rate"],"champions_adb",CRAWLED_DATE,now)
            )
            inserted["evs"] += conn.execute("SELECT changes()").fetchone()[0]

        for i, pt in enumerate(rec.get("partners", []), 1):
            pname = OCR_POKEMON.get(pt["name"], pt["name"])
            if pname not in pokemon_master:
                partner_unknown.add(pt["name"])
                continue
            conn.execute(
                "INSERT OR IGNORE INTO pokemon_partners(season,rule,pokemon,rank,partner,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?)",
                ("M-3","single",pokemon,i,pname,"champions_adb",CRAWLED_DATE,now)
            )
            inserted["partners"] += conn.execute("SELECT changes()").fetchone()[0]

    conn.commit()
    conn.close()

    print("\n=== 投入結果 ===")
    for t, n in inserted.items():
        print(f"  {t}: {n}件")

    if skipped_pokemon:
        print(f"\n⚠ ポケモンマスター不一致（スキップ）:")
        for rank, raw, fixed in skipped_pokemon:
            print(f"  rank={rank}: {raw} → {fixed}")

    if move_unknown:
        print(f"\n⚠ 技マスター不一致（スキップ）: {sorted(move_unknown)}")
    if item_unknown:
        print(f"\n⚠ 持ち物マスター不一致（スキップ）: {sorted(item_unknown)}")
    if ability_unknown:
        print(f"\n⚠ 特性マスター不一致（スキップ）: {sorted(ability_unknown)}")
    if partner_unknown:
        print(f"\n⚠ パートナー不一致（スキップ）: {sorted(partner_unknown)}")

if __name__ == "__main__":
    main()
