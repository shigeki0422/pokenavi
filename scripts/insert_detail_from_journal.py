"""
journal.jsonlからM-3詳細データ（技/持ち物/特性/性格/EV/パートナー）をDB投入
OCR補正マッピング適用済み、マスター照合、INSERT OR IGNORE
"""
import json, sqlite3, glob
from datetime import datetime, timezone
from pathlib import Path

DB = Path(__file__).parent / "pokenavi.db"

WF_DIRS = [
    "/Users/shigeki/.claude/projects/-Users-shigeki-work/5c9e5884-44f0-4cfa-ae54-b0230dd188ae/subagents/workflows/wf_02d68588-c0c",
]

OCR_MOVES = {
    "けきりん": "げきりん",
    "しんぐうは": "しんくうは",
    "かみしゃら": "がむしゃら",
    "じゆうでん": "じゅうでん",
    "どくぱりセンボン": "どくばりセンボン",
    "はいずいのじん": "はいすいのじん",
    "もらはのすつき": "もろはのずつき",
    "タネマシガン": "タネマシンガン",
    "ゴーストタイプ": "ゴーストダイブ",
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
    "ヘドろばくだん": "ヘドロばくだん",
    "サンダーダイプ": "サンダーダイブ",
    "ドラゴンタイプ": "ドラゴンダイブ",
    "とびざげり": "とびひざげり",
    "むねのつるぎ": "むねんのつるぎ",
    "かわりみ": "みがわり",
    "ひやっきやこう": "ひゃっきやこう",
    "でаいがしら": "であいがしら",
    "かんせきふうじ": "がんせきふうじ",
    "こうごせい": "こうごうせい",
    "ダブルウィング": "ダブルウイング",
    "しこうさいせい": "じこさいせい",
    "でいあがしら": "であいがしら",
    "でいがしら": "であいがしら",
    "ドグザン": "ドゲザン",
    "プレイバード": "ブレイブバード",
    "シェルアームズ": "シェルブレード",
    "クロスボイズン": "クロスポイズン",
    "コトンガード": "コットンガード",
    "ふちかまし": "ぶちかまし",
    "かげふんしん": "かげぶんしん",
    "つらら おとし": "つららおとし",
    "サンダータイブ": "サンダーダイブ",
}
OCR_ITEMS = {
    "のりのおふだ": "のろいのおふだ",
    "ジュベッタナイト": "ジュペッタナイト",
    "ユキノオーナイト": "ユキノオナイト",
    "こうがくレンズ": "こうかくレンズ",
    "ビントレンズ": "ピントレンズ",
    "ボスゴドライト": "ボスゴドナイト",
    "ヨブのみ": "ヨプのみ",
    "フーティナイト": "フーディナイト",
    "ジバルドナイト": "シビルドナイト",
    "ヤチエのみ": "ヤチェのみ",
    "バンドラナイト": "ペンドラナイト",
    "ピアーのみ": "ビアーのみ",
    "ユキノオート": "ユキノオナイト",
    "ビジョットナイト": "ピジョットナイト",
    "かいからのすず": "かいがらのすず",
    "シャンテラナイト": "シャンデラナイト",
    "スビアナイト": "スピアナイト",
    "しんびのしずく": "しんぴのしずく",
    "たじゅんのおび": "たつじんのおび",
    "たじんのおび": "たつじんのおび",
    "サーナイナイト": "サーナイトナイト",
    "カイリユナイト": "カイリュナイト",
    "テンリュウナイト": "デンリュウナイト",
    "パワーダナイト": "バクーダナイト",
    "ミミッキュナイト": "ミミロップナイト",
    "ちくたん": "もくたん",
}
OCR_ABILITIES = {
    "ちょうすい": "ちょすい",
    "ふしよく": "ふしょく",
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
    "じょうおうのいげん": "じょおうのいげん",
    "じゆうなん": "じゅうなん",
    "いたすらごころ": "いたずらごころ",
    "かんじょうあご": "がんじょうあご",
    "どくけしょう": "どくのトゲ",
    "ゆきかくれ": "ゆきがくれ",
    "よりょくそ": "ようりょくそ",
    "メロメロボティ": "メロメロボディ",
    "きようせい": "きょうせい",
    "ボイゾンヒール": "ポイズンヒール",
    "ボイズンヒール": "ポイズンヒール",
}
OCR_NATURES = {
    "すぶとい": "ずぶとい", "すばとい": "ずぶとい", "すぼとい": "ずぶとい", "ずぼとい": "ずぶとい",
    "おくびよう": "おくびょう", "いっぱり": "いじっぱり", "のてんき": "のうてんき", "すばやい": "おくびょう",
}
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
    "ジュベッタ": "ジュペッタ",
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
    "ジャジャンゴ": "ジャラランガ",
    "ササンドラ": "サザンドラ",
    "オーロング": "オーロンゲ",
    "ビビコン": "ビビヨン",
    "グレペース": "クレベース",
    "ガメノテス": "ガメノデス",
    "マツギョ": "マッギョ",
    "ウインデイ": "ウインディ",
    "ドヒドイア": "ドヒドイデ",
    "テカヌチャン": "デカヌチャン",
}

CRAWLED_DATE = "2026-06-26"

# ランク番号で確定したフォーム名（OCR_POKEMONより優先）、日付別に管理
#
# 【設定ルール — 必ず守ること】
# RANK_OVERRIDESに追加する前に、そのrankの _c_ability_00.png を開いて以下5点を画像で確認する:
#   1. No.（図鑑番号）
#   2. ポケモン名テキスト
#   3. スプライット色
#   4. タイプアイコン（個数・種類）
#   5. 特性名（1位）
# 確認した根拠を # コメントに必ず書く。テキスト情報だけで判断した場合は設定しない。
#
RANK_OVERRIDES_BY_DATE = {
    "2026-06-19": {
        19: "アローラキュウコン",
        25: "ウォッシュロトム",
        50: "ヒートロトム",
        89: "ヒスイヌメルゴン",
        95: "カットロトム",
        105: "イダイトウ(メス)",
        116: "ヒスイバクフーン",
        129: "ガラルヤドラン",
        146: "ヌメルゴン",
        155: "ヒスイゾロアーク",
        160: "ガラルヤドキング",
        165: "ニャオニクス(オス)",
        195: "スピンロトム",
    },
    "2026-06-24": {
        23: "サーフゴー",          # OCR=ロトム（No.1000 はがね/ゴースト おうごんのからだ）
        35: "ミミロップ",          # OCR=ミミッキュ（No.428 ノーマル じゅうなん）
        49: "ヒートロトム",        # OCR=ロトム（でんき/ほのお）
        88: "ポットデス",          # OCR=ヌメルゴン（No.855 ゴースト のろわれボディ）
        89: "イツカネズミ",        # OCR=ヤドキング（No.925 ノーマル テクニシャン）
        103: "ハリーマン",         # OCR=イダイトウ(オス)（No.904 どく/エスパー いかく）
        106: "ボスゴドラ",         # OCR=ロトム（No.306 はがね/いわ がんじょう）
        116: "マニューラ",         # OCR=ヤドラン（No.461 あく/こおり プレッシャー）
        150: "ヌメルゴン",         # OCR=ヌメルゴン（正解、rank=88誤読でスキップされた）
        159: "アマルルガ",         # OCR=ヤドキング（No.699 いわ/こおり ゆきふらし）
        162: "オンバーン",         # OCR=ゾロアーク（No.715 ひこう/ドラゴン おみとおし）
        167: "チャーレム",         # OCR=ニャオニクス（No.308 かくとう/エスパー ヨガパワー）
        169: "ニャオニクス(オス)", # OCR=キュウコン（No.678 エスパー 青スプライット）
        181: "リキキリン",         # OCR=ケンタロス（No.981 ノーマル/エスパー テイルアーマー）
        188: "エモンガ",           # OCR=バクフーン（No.587 でんき/ひこう でんきエンジン）
        190: "マホイップ",         # OCR=パンプジン（No.869 フェアリー アロマベール）
        192: "フロストロトム",     # OCR=ロトム（でんき/こおり）
        198: "ブースター",         # OCR=クレベース（No.136 ほのお もらいび）
    },
    "2026-06-25": {
        13: "アローラキュウコン",    # No.38 こおり/フェアリー、ゆきふらし99.6%
        21: "ウォッシュロトム",      # No.479 でんき/みず、ふゆう
        50: "ヒートロトム",          # No.479 でんき/ほのお、ふゆう
        59: "ヒスイゾロアーク",      # No.571 ノーマル/ゴースト、白スプライット
        86: "ヒスイヌメルゴン",      # No.706 はがね/ドラゴン、シェルアーマー39%
        91: "ガラルヤドキング",      # No.199 エスパー/どく、きみょうなくすり0.4%
        95: "ヒスイウインディ",      # No.59 ほのお/ノーマル、黒スプライット、いしあたま92.1%
        103: "イダイトウ(メス)",     # No.902 みず/ゴースト、てきおうりょく87.1%
        108: "カットロトム",         # No.479 でんき/くさ、ふゆう
        117: "ガラルヤドラン",       # No.80 クイックドロウ87.4%
        123: "ヒスイバクフーン",     # No.157 ほのお/ゴースト、おみとおし72.1%
        126: "ケンタロス:炎",        # No.128 かくとう/ほのお
        170: "ニャオニクス(オス)",   # No.678 エスパー、青スプライット、いたずらごころ92%
        183: "ケンタロス:水",        # No.128 かくとう/みず
        191: "スピンロトム",         # No.479 でんき/ひこう
        192: "パンプジン(ちゅうだましゅ)",  # No.711 ゴースト/くさ、ふみん52.6%
        196: "ヒスイクレベース",     # No.713 こおり/ノーマル、がんじょう91%
        200: "ニャオニクス(メス)",   # No.678 エスパー、白スプライット、かちき82%
    },
    "2026-06-27": {
        11: "アローラキュウコン",    # No.38 こおり/フェアリー
        15: "イダイトウ(オス)",      # No.901 みず/かくとう、赤スプライット
        19: "ウォッシュロトム",      # No.479 でんき/みず
        49: "ヒートロトム",          # No.479 でんき/ほのお
        58: "ヒスイゾロアーク",      # No.571 ノーマル/ゴースト
        96: "ヒスイウインディ",      # No.59 ほのお/ノーマル（OCR=ウインテイ）、いしあたま91.9%
        113: "カットロトム",         # No.479 でんき/くさ
        114: "ウインディ",           # No.59 ほのお（OCR=ウインテイ）、いかく96.4%
        117: "ガラルヤドラン",       # No.80 エスパー/はがね、クイックドロウ88.1%
        125: "ヒスイバクフーン",     # No.157 ほのお/ゴースト
        126: "ケンタロス:炎",        # No.128 かくとう/ほのお
        137: "ルガルガン(昼)",       # No.745 ノーマル、かたいツメ100%
        172: "ニャオニクス(オス)",   # No.678 エスパー、青スプライット、いたずらごころ91.4%
        184: "ケンタロス:水",        # No.128 かくとう/みず
        191: "フロストロトム",       # No.479 でんき/こおり
        194: "パンプジン(ちゅうだましゅ)", # No.711 ゴースト/くさ、ふみん53.0%
        196: "ヒスイクレベース",     # No.713 こおり/ノーマル
    },
    "2026-06-26": {
        61: "ガラルヤドキング",      # No.199 みず/エスパー, スプライット紫（さいせいりょくは通常ヤドキングの特性表示バグ）
        143: "ヤドキング",            # No.199 ピンクスプライット, 通常形
        20: "ウォッシュロトム",      # No.479 でんき/みず, ふゆう100%
        35: "ヒートロトム",          # No.479 でんき/ほのお, ふゆう100%
        56: "アローラキュウコン",    # No.38 こおり/フェアリー, ゆきふらし99.1%
        59: "ヒスイヌメルゴン",      # No.706 はがね/ドラゴン（OCR=フェアリー/ドラゴン誤読）, シェルアーマー31.6%
        62: "ヒスイゾロアーク",      # No.571 ノーマル/ゴースト, イリュージョン100%
        73: "ヒスイウインディ",      # No.59 ほのお/ノーマル（OCR=ウインデイ）, いしあたま90.9%
        89: "ウインディ",            # No.59 ほのお単（OCR=ウインデイ）, いかく96.2%
        105: "ガラルヤドラン",       # No.80 みず/はがね（OCR=みず/エスパー誤読）, クイックドロウ87.5%
        113: "ルガルガン(昼)",       # No.745 いわ, かたいツメ100%
        119: "ケンタロス:炎",        # No.128 かくとう/ほのお, いかく91.4%
        123: "カットロトム",         # No.479 でんき/くさ, ふゆう100%
        158: "ヒスイクレベース",     # No.713 こおり/ノーマル, がんじょう94.7%
        161: "ケンタロス:水",        # No.128 かくとう/みず, いかく86.8%
        162: "フロストロトム",       # No.479 でんき/こおり, ふゆう100%
        163: "ニャオニクス(オス)",   # No.678 エスパー, いたずらごころ89%
        169: "トリデプス",            # OCR=トリテブス
        179: "アローラライチュウ",   # No.26 でんき/エスパー, サーフテール100%
        181: "パンプジン(ちゅうだましゅ)", # No.711 ゴースト/くさ, ふみん52.2%
        182: "ライチュウ",           # No.26 でんき, ひらいしん61.9%（rank=179はアローラ形）
        183: "ニャオニクス(メス)",   # No.678 エスパー, かちき79.3%
        185: "ルガルガン(まよなか)", # No.745 いわ, すなかき43.3%
        191: "スピンロトム",         # No.479 でんき/ひこう, ふゆう100%
        198: "ルガルガン(たそがれ)", # No.745 いわ, ノーガード79.8%
        100: "イダイトウ(メス)",     # みず/ゴースト, てきおうりょく91.8%（rank=10オスと別種）
        106: "ヒスイバクフーン",     # ほのお/ゴースト, おみとおし73.0%
        117: "ヒスイジュナイパー",   # くさ/かくとう, きもったま98.1%
        168: "バクフーン",           # ほのお, もらいび68.9%（rank=106ヒスイと別種）
        172: "マッギョ",             # じめん/でんき, せいでんき86.7%
        178: "ジュナイパー",         # くさ/ゴースト, えんかく73.1%（rank=117ヒスイと別種）
        189: "ガラルマッギョ",       # じめん/みず, ぎたい100%（rank=172通常と別種）
    },
    "2026-06-22": {
        17: "アローラキュウコン",   # OCR=キュウコン（ゆきふらし+オーロラベール）
        23: "ウォッシュロトム",     # OCR=ロトム（ハイドロポンプ採用）
        62: "ヒスイゾロアーク",     # OCR=ゾロアーク（白スプライト）
        88: "ヒスイヌメルゴン",     # OCR=ヌメルゴン（白スプライト+ラスターカノン）
        96: "ヒスイウインディ",     # OCR=ウインディ（黒スプライト+いしあたま92.7%）
        35: "ミミロップ",           # OCR=ミミッキュ（No.428 メガミミロップ）
        49: "ヒートロトム",         # OCR=ロトム（オーバーヒート+ふゆう）
        89: "ガラルヤドキング",     # OCR=ヤドキング（紫スプライト・エスパータイプアイコン）
        103: "イダイトウ(メス)",    # OCR=イダイトウ
        106: "カットロトム",        # OCR=ロトム（リーフストーム+ふゆう）
        116: "ガラルヤドラン",      # OCR=ヤドラン（クイックドロウ87.8%）
        # 129: クレッフィ（OCR=グレッフィ→OCR_POKEMONで自動補正済み）
        # 155: ジジーロンはOCR正解のためオーバーライド不要
        # 160: サンダース（OCR正解。ちくでん94.1%で確認済み。ガラルヤドキングは誤り）
        165: "ニャオニクス(オス)",  # OCR=カミツオロチ
        167: "ニャオニクス(メス)",  # OCR=ニャオニクス
        181: "ケンタロス:水",       # OCR=ケンタロス
        188: "ヒスイバクフーン",    # OCR=バクフーン（シャドーボール採用）
        190: "パンプジン(ギガだましゅ)", # OCR=パンプジン
        192: "フロストロトム",      # OCR=ロトム
        195: "スピンロトム",        # OCR=ドクロッグ
        198: "ヒスイクレベース",    # OCR=グレペース（rank=186がクレベース）
    },
}
RANK_OVERRIDES = RANK_OVERRIDES_BY_DATE.get(CRAWLED_DATE, {})

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
                all_data[rank] = rec  # 後のWFで上書き（後が正しい）

    MAX_RANK = 200

    print(f"Journal から取得: {len(all_data)} ランク")

    # GATE0: journalに存在しないrank（OCRデータ欠落）を検出
    gate0_missing = [r for r in range(1, MAX_RANK + 1) if r not in all_data]
    if gate0_missing:
        print(f"🚨 [GATE0] Journalにデータなし（OCR欠落）: rank={gate0_missing}")
        print("  → クロール画像を再OCRするか手動登録が必要")

    # GATE1: 200匹ユニーク必須（重複・マスター不一致があれば全件投入中止）
    pokemon_to_first_rank = {}
    candidates = []
    gate1_errors = []
    master_miss_ranks = []
    for rank in sorted(all_data.keys()):
        if rank > MAX_RANK:
            continue
        rec = all_data[rank]
        pokemon_raw = rec["pokemon"]
        pokemon = RANK_OVERRIDES.get(rank) or OCR_POKEMON.get(pokemon_raw, pokemon_raw)
        if pokemon not in pokemon_master:
            master_miss_ranks.append((rank, pokemon_raw, pokemon))
            continue
        if pokemon in pokemon_to_first_rank:
            first = pokemon_to_first_rank[pokemon]
            crawl_dir = f"/tmp/champ_crawl_{CRAWLED_DATE}"
            gate1_errors.append((rank, pokemon, first))
            print(f"🚨 [GATE1] 重複ポケモン: {pokemon} が rank={first} と rank={rank} に存在")
            print(f"   画像を開いてNo./名前/スプライット色/タイプアイコンを確認すること（テキスト判断禁止）:")
            print(f"     rank={first:3d}: {crawl_dir}/detail/{str(first).zfill(3)}/_c_ability_00.png")
            print(f"     rank={rank:3d}: {crawl_dir}/detail/{str(rank).zfill(3)}/_c_ability_00.png")
            print(f"   別種なら RANK_OVERRIDES_BY_DATE['{CRAWLED_DATE}'][{rank}] に正しい名前を設定して再実行。")
        else:
            pokemon_to_first_rank[pokemon] = rank
            candidates.append((rank, pokemon, rec))

    if master_miss_ranks:
        print(f"🚨 [GATE_MISS] ポケモンマスター不一致（要対処）:")
        for rank, raw, fixed in master_miss_ranks:
            print(f"  rank={rank}: OCR='{raw}' → 補正後='{fixed}' ← RANK_OVERRIDESかOCR_POKEMONに追加必要")

    if len(candidates) < MAX_RANK or gate1_errors or master_miss_ranks:
        conn.close()
        print(f"\n🚫 投入中止: {len(candidates)}件（{MAX_RANK}件必須・重複{len(gate1_errors)}件・マスター不一致{len(master_miss_ranks)}件）")
        return

    # pokemon_usage 投入
    usage_inserted = 0
    for rank, pokemon, rec in candidates:
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

    candidate_ranks = {rank for rank, _, _ in candidates}
    for rank in sorted(all_data.keys()):
        if rank not in candidate_ranks:
            continue
        rec = all_data[rank]
        pokemon_raw = rec["pokemon"]
        pokemon = RANK_OVERRIDES.get(rank) or OCR_POKEMON.get(pokemon_raw, pokemon_raw)

        # フォーム付きポケモン（イダイトウ(オス/メス)等）はusageテーブルから正式名を取得
        if pokemon not in pokemon_master and rank in rank_to_pokemon:
            usage_name = rank_to_pokemon[rank]
            if usage_name in pokemon_master:
                pokemon = usage_name

        if pokemon not in pokemon_master:
            skipped_pokemon.append((rank, pokemon_raw, pokemon))
            continue

        # ゲート3: 黒画像/OCR失敗チェック（技が0件の場合はアラート）
        moves_raw = rec.get("moves", [])
        if not moves_raw:
            print(f"⚠ [GATE3] rank={rank} {pokemon}: 技データが0件（黒画像またはOCR失敗の可能性） → 詳細データをスキップ")
            skipped_pokemon.append((rank, pokemon_raw, f"{pokemon}（技0件）"))
            continue

        # ゲート2: 技リスト内重複チェック
        move_names_corrected = [OCR_MOVES.get(m["name"], m["name"]) for m in moves_raw]
        seen_moves_gate = set()
        for mn in move_names_corrected:
            if mn in move_master:
                if mn in seen_moves_gate:
                    print(f"⚠ [GATE2] rank={rank} {pokemon}: 技リスト内重複 '{mn}' → OCR_MOVESの補正が必要")
                seen_moves_gate.add(mn)

        # ゲート2: 持ち物リスト内重複チェック
        item_names_corrected = [OCR_ITEMS.get(it["name"], it["name"]) for it in rec.get("items", [])]
        seen_items_gate = set()
        for itn in item_names_corrected:
            if itn in item_master:
                if itn in seen_items_gate:
                    print(f"⚠ [GATE2] rank={rank} {pokemon}: 持ち物リスト内重複 '{itn}' → OCR_ITEMSの補正が必要")
                seen_items_gate.add(itn)

        # ゲート2: パートナーリスト内重複チェック
        partner_names_corrected = [OCR_POKEMON.get(pt["name"], pt["name"]) for pt in rec.get("partners", [])]
        seen_partners_gate = set()
        for ptn in partner_names_corrected:
            if ptn in pokemon_master:
                if ptn in seen_partners_gate:
                    print(f"⚠ [GATE2] rank={rank} {pokemon}: パートナーリスト内重複 '{ptn}' → OCR_POKEMONの補正が必要")
                seen_partners_gate.add(ptn)

        moves = rec.get("moves", [])
        if moves:
            top_move_rate = moves[0].get("rate", 0)
            if top_move_rate < 10:
                print(f"  [GATE_RATE1] {pokemon} rank={rank}: 技1位={top_move_rate}%<10% スキップ")
            else:
                for i, m in enumerate(moves, 1):
                    name = OCR_MOVES.get(m["name"], m["name"])
                    if name not in move_master:
                        move_unknown.add(name)
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO pokemon_moves(season,rule,pokemon,rank,move,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                        ("M-3","single",pokemon,i,name,m["rate"],"champions_adb",CRAWLED_DATE,now)
                    )
                    inserted["moves"] += conn.execute("SELECT changes()").fetchone()[0]

        items = rec.get("items", [])
        if items:
            top_item_rate = items[0].get("rate", 0)
            items_sum = sum(it.get("rate", 0) for it in items)
            if top_item_rate < 10:
                print(f"  [GATE_RATE1] {pokemon} rank={rank}: 持ち物1位={top_item_rate}%<10% スキップ")
            elif items_sum < 70:
                print(f"  [GATE_RATE_SUM] {pokemon} rank={rank}: 持ち物合計={items_sum:.1f}%<70% スキップ")
            else:
                for i, it in enumerate(items, 1):
                    name = OCR_ITEMS.get(it["name"], it["name"])
                    if name not in item_master:
                        item_unknown.add(name)
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO pokemon_items(season,rule,pokemon,rank,item,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                        ("M-3","single",pokemon,i,name,it["rate"],"champions_adb",CRAWLED_DATE,now)
                    )
                    inserted["items"] += conn.execute("SELECT changes()").fetchone()[0]

        abilities = rec.get("abilities", [])
        if abilities:
            top_ab_rate = abilities[0].get("rate", 0)
            ab_sum = sum(ab.get("rate", 0) for ab in abilities)
            if top_ab_rate < 10:
                print(f"  [GATE_RATE1] {pokemon} rank={rank}: 特性1位={top_ab_rate}%<10% スキップ")
            elif ab_sum < 70:
                print(f"  [GATE_RATE_SUM] {pokemon} rank={rank}: 特性合計={ab_sum:.1f}%<70% スキップ")
            else:
                for i, ab in enumerate(abilities, 1):
                    name = OCR_ABILITIES.get(ab["name"], ab["name"])
                    if name not in ability_master:
                        ability_unknown.add(name)
                        continue
                    conn.execute(
                        "INSERT OR IGNORE INTO pokemon_abilities(season,rule,pokemon,rank,ability,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                        ("M-3","single",pokemon,i,name,ab["rate"],"champions_adb",CRAWLED_DATE,now)
                    )
                    inserted["abilities"] += conn.execute("SELECT changes()").fetchone()[0]

        natures = rec.get("natures", [])
        if natures:
            top_na_rate = natures[0].get("rate", 0)
            na_sum = sum(na.get("rate", 0) for na in natures)
            if top_na_rate < 10:
                print(f"  [GATE_RATE1] {pokemon} rank={rank}: 性格1位={top_na_rate}%<10% スキップ")
            elif na_sum < 70:
                print(f"  [GATE_RATE_SUM] {pokemon} rank={rank}: 性格合計={na_sum:.1f}%<70% スキップ")
            else:
                for i, na in enumerate(natures, 1):
                    nat = OCR_NATURES.get(na["name"], na["name"])
                    conn.execute(
                        "INSERT OR IGNORE INTO pokemon_natures(season,rule,pokemon,rank,nature,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?)",
                        ("M-3","single",pokemon,i,nat,na["rate"],"champions_adb",CRAWLED_DATE,now)
                    )
                    inserted["natures"] += conn.execute("SELECT changes()").fetchone()[0]

        evs = rec.get("evs", [])
        ev_violations = []
        if evs:
            top_ev_rate = evs[0].get("rate", 0)
            ev_rate_sum = sum(ev.get("rate", 0) for ev in evs[:10])
            if top_ev_rate < 5:
                print(f"  [GATE_RATE1] {pokemon} rank={rank}: EV1位={top_ev_rate}%<5% スキップ")
            elif ev_rate_sum < 30:
                print(f"  [GATE_RATE_SUM] {pokemon} rank={rank}: EV合計(top10)={ev_rate_sum:.1f}%<30% スキップ")
            elif ev_rate_sum > 100:
                print(f"  [GATE_RATE_SUM] {pokemon} rank={rank}: EV合計(top10)={ev_rate_sum:.1f}%>100% スキップ")
            else:
                for i, ev in enumerate(evs, 1):
                    h,a,b,c,d,s = ev.get("h",0),ev.get("a",0),ev.get("b",0),ev.get("c",0),ev.get("d",0),ev.get("s",0)
                    vals = [h,a,b,c,d,s]
                    total = sum(vals)
                    if max(vals) > 32 or total > 66:
                        ev_violations.append((i, vals, f"max={max(vals)}>32 or sum={total}>66"))
                        continue
                    if total < 64:
                        ev_violations.append((i, vals, f"sum={total}<64"))
                        continue
                    spread = ev_spread(ev)
                    conn.execute(
                        "INSERT OR IGNORE INTO pokemon_evs(season,rule,pokemon,rank,ev_spread,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s,usage_rate,source,crawled_date,crawled_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        ("M-3","single",pokemon,i,spread,h,a,b,c,d,s,
                         ev["rate"],"champions_adb",CRAWLED_DATE,now)
                    )
                    inserted["evs"] += conn.execute("SELECT changes()").fetchone()[0]
        if ev_violations:
            print(f"  [GATE_EV] {pokemon} rank={rank}: {len(ev_violations)}件スキップ → {ev_violations[:2]}")

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

    # GATE4: usage投入後のランク欠落チェック
    db_ranks = set(r[0] for r in conn.execute(
        "SELECT rank FROM pokemon_usage WHERE season='M-3' AND rule='single' AND crawled_date=? AND rank<=?",
        (CRAWLED_DATE, MAX_RANK)
    ))
    gate4_missing = [r for r in range(1, MAX_RANK + 1) if r not in db_ranks]
    db_over = [r[0] for r in conn.execute(
        "SELECT rank FROM pokemon_usage WHERE season='M-3' AND rule='single' AND crawled_date=? AND rank>?",
        (CRAWLED_DATE, MAX_RANK)
    )]
    print(f"\n=== GATE4: 使用率ランキング完全性チェック ===")
    if gate4_missing:
        print(f"🚨 欠落rank: {gate4_missing}")
    else:
        print(f"✓ rank 1-{MAX_RANK} 全件あり")
    if db_over:
        print(f"🚨 {MAX_RANK}超のrank存在（要削除）: {db_over}")

    # GATE5: 詳細データの欠落チェック
    print(f"\n=== GATE5: 詳細データ完全性チェック ===")
    gate5_issues = []
    for row in conn.execute(
        "SELECT rank, pokemon FROM pokemon_usage WHERE season='M-3' AND rule='single' AND crawled_date=? AND rank<=? ORDER BY rank",
        (CRAWLED_DATE, MAX_RANK)
    ):
        rank_u, poke = row[0], row[1]
        n_moves = conn.execute("SELECT count(*) FROM pokemon_moves WHERE season='M-3' AND rule='single' AND pokemon=? AND crawled_date=?", (poke, CRAWLED_DATE)).fetchone()[0]
        n_items = conn.execute("SELECT count(*) FROM pokemon_items WHERE season='M-3' AND rule='single' AND pokemon=? AND crawled_date=?", (poke, CRAWLED_DATE)).fetchone()[0]
        n_ab    = conn.execute("SELECT count(*) FROM pokemon_abilities WHERE season='M-3' AND rule='single' AND pokemon=? AND crawled_date=?", (poke, CRAWLED_DATE)).fetchone()[0]
        n_nat   = conn.execute("SELECT count(*) FROM pokemon_natures WHERE season='M-3' AND rule='single' AND pokemon=? AND crawled_date=?", (poke, CRAWLED_DATE)).fetchone()[0]
        issues = []
        if n_moves == 0: issues.append("技0件")
        if n_items == 0: issues.append("持ち物0件")
        if n_ab == 0:    issues.append("特性0件")
        if n_nat == 0:   issues.append("性格0件")
        if issues:
            gate5_issues.append((rank_u, poke, issues))
    if gate5_issues:
        print(f"🚨 詳細データ不足 ({len(gate5_issues)}件):")
        for rank_u, poke, issues in gate5_issues:
            print(f"  rank={rank_u} {poke}: {', '.join(issues)}")
    else:
        print(f"✓ 全ポケモンの詳細データあり")

    conn.close()

if __name__ == "__main__":
    main()
