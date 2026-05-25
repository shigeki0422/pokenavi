#!/usr/bin/env python3
"""
ポケモン情報ページ（src/content/pokemon/）を自動生成するスクリプト
DBデータを参照し、ガブリアスページと同形式で生成する
"""

import sqlite3
import re
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "pokenavi.db"
OUT_DIR = Path(__file__).parent.parent / "src/content/pokemon"

# ---- 防御タイプ相性チャート（Gen 6+）----
# DEFENSE[守備タイプ] = {攻撃タイプ: 倍率}
DEFENSE = {
    "ノーマル":   {"かくとう": 2, "ゴースト": 0},
    "かくとう":   {"ひこう": 2, "エスパー": 2, "フェアリー": 2,
                   "いわ": 0.5, "むし": 0.5, "あく": 0.5},
    "ひこう":     {"でんき": 2, "こおり": 2, "いわ": 2,
                   "かくとう": 0.5, "むし": 0.5, "くさ": 0.5, "じめん": 0},
    "どく":       {"じめん": 2, "エスパー": 2,
                   "くさ": 0.5, "かくとう": 0.5, "どく": 0.5, "むし": 0.5, "フェアリー": 0.5},
    "じめん":     {"みず": 2, "くさ": 2, "こおり": 2,
                   "どく": 0.5, "いわ": 0.5, "でんき": 0},
    "いわ":       {"みず": 2, "くさ": 2, "かくとう": 2, "じめん": 2, "はがね": 2,
                   "ノーマル": 0.5, "ひこう": 0.5, "どく": 0.5, "ほのお": 0.5},
    "むし":       {"ほのお": 2, "ひこう": 2, "いわ": 2,
                   "かくとう": 0.5, "くさ": 0.5, "じめん": 0.5},
    "ゴースト":   {"ゴースト": 2, "あく": 2,
                   "どく": 0.5, "むし": 0.5, "ノーマル": 0, "かくとう": 0},
    "はがね":     {"ほのお": 2, "かくとう": 2, "じめん": 2,
                   "ノーマル": 0.5, "くさ": 0.5, "こおり": 0.5, "どく": 0,
                   "ひこう": 0.5, "エスパー": 0.5, "むし": 0.5, "いわ": 0.5,
                   "ドラゴン": 0.5, "はがね": 0.5, "フェアリー": 0.5},
    "ほのお":     {"みず": 2, "じめん": 2, "いわ": 2,
                   "ほのお": 0.5, "くさ": 0.5, "こおり": 0.5, "むし": 0.5,
                   "はがね": 0.5, "フェアリー": 0.5},
    "みず":       {"でんき": 2, "くさ": 2,
                   "ほのお": 0.5, "みず": 0.5, "こおり": 0.5, "はがね": 0.5},
    "くさ":       {"ほのお": 2, "こおり": 2, "どく": 2, "ひこう": 2, "むし": 2,
                   "みず": 0.5, "でんき": 0.5, "くさ": 0.5, "じめん": 0.5},
    "でんき":     {"じめん": 2,
                   "でんき": 0.5, "ひこう": 0.5, "はがね": 0.5},
    "エスパー":   {"むし": 2, "ゴースト": 2, "あく": 2,
                   "かくとう": 0.5, "エスパー": 0.5},
    "こおり":     {"ほのお": 2, "かくとう": 2, "いわ": 2, "はがね": 2,
                   "みず": 0.5, "こおり": 0.5},
    "ドラゴン":   {"こおり": 2, "ドラゴン": 2, "フェアリー": 2,
                   "ほのお": 0.5, "みず": 0.5, "でんき": 0.5, "くさ": 0.5},
    "あく":       {"かくとう": 2, "むし": 2, "フェアリー": 2,
                   "ゴースト": 0.5, "あく": 0.5, "エスパー": 0},
    "フェアリー": {"どく": 2, "はがね": 2,
                   "かくとう": 0.5, "むし": 0.5, "あく": 0.5, "ドラゴン": 0},
}

ALL_TYPES = ["ノーマル","かくとう","ひこう","どく","じめん","いわ","むし","ゴースト",
             "はがね","ほのお","みず","くさ","でんき","エスパー","こおり",
             "ドラゴン","あく","フェアリー"]

TYPE_NUM = {
    "ノーマル":"00","かくとう":"01","ひこう":"02","どく":"03","じめん":"04",
    "いわ":"05","むし":"06","ゴースト":"07","はがね":"08","ほのお":"09",
    "みず":"10","くさ":"11","でんき":"12","エスパー":"13","こおり":"14",
    "ドラゴン":"15","あく":"16","フェアリー":"17",
}
TYPE_SLUG = {
    "ノーマル":"normal","かくとう":"fighting","ひこう":"flying","どく":"poison",
    "じめん":"ground","いわ":"rock","むし":"bug","ゴースト":"ghost","はがね":"steel",
    "ほのお":"fire","みず":"water","くさ":"grass","でんき":"electric","エスパー":"psychic",
    "こおり":"ice","ドラゴン":"dragon","あく":"dark","フェアリー":"fairy",
}

def type_effectiveness(types: list) -> dict:
    """与えられたタイプリスト（1〜2種）に対する全タイプの効果倍率を返す"""
    result = {}
    for atk in ALL_TYPES:
        mult = 1.0
        for t in types:
            mult *= DEFENSE.get(t, {}).get(atk, 1.0)
        if mult != 1.0:
            result[atk] = mult
    return result

# ---- 技→タイプ マッピング ----
MOVE_TYPE = {
    "じしん": "じめん", "だいちのちから": "じめん", "マッドショット": "じめん",
    "ステルスロック": "いわ", "いわなだれ": "いわ", "がんせきふうじ": "いわ",
    "ストーンエッジ": "いわ", "パワージェム": "いわ", "ロックカット": "いわ",
    "りゅうせいぐん": "ドラゴン", "げきりん": "ドラゴン", "ドラゴンテール": "ドラゴン",
    "ドラゴンクロー": "ドラゴン", "りゅうのまい": "ドラゴン", "りゅうのはどう": "ドラゴン",
    "スケイルショット": "ドラゴン", "ドラゴンアロー": "ドラゴン",
    "どくづき": "どく", "ヘドロウェーブ": "どく", "ヘドロばくだん": "どく",
    "どくどく": "どく", "ニードルガード": "どく", "キラースピン": "どく",
    "つるぎのまい": "ノーマル", "ほえる": "ノーマル", "ふきとばし": "ノーマル",
    "みがわり": "ノーマル", "がむしゃら": "ノーマル", "なまける": "ノーマル",
    "しんそく": "ノーマル", "ハイパーボイス": "ノーマル", "ねこだまし": "ノーマル",
    "まもる": "ノーマル", "ギガインパクト": "ノーマル", "メガトンキック": "ノーマル",
    "あくび": "ノーマル", "じこさいせい": "ノーマル", "こうそくスピン": "ノーマル",
    "あさのひざし": "ノーマル", "いたみわけ": "ノーマル", "アンコール": "ノーマル",
    "ほのおのキバ": "ほのお", "フレアドライブ": "ほのお", "かえんほうしゃ": "ほのお",
    "オーバーヒート": "ほのお", "ニトロチャージ": "ほのお", "おにび": "ほのお",
    "だいもんじ": "ほのお", "ほのおのまい": "ほのお", "マジカルフレイム": "ほのお",
    "ムーンフォース": "フェアリー", "じゃれつく": "フェアリー", "ドレインキッス": "フェアリー",
    "マジカルシャイン": "フェアリー", "ミストフィールド": "フェアリー",
    "あまえる": "フェアリー", "フェアリーウィンド": "フェアリー",
    "はめつのひかり": "フェアリー",
    "うたかたのアリア": "みず", "アクアジェット": "みず", "クイックターン": "みず",
    "なみのり": "みず", "たきのぼり": "みず", "ウェーブタックル": "みず",
    "アクアブレイク": "みず", "アクアテール": "みず", "すいりゅうれんだ": "みず",
    "アイススピナー": "こおり", "こおりのキバ": "こおり", "ゆきなだれ": "こおり",
    "トリプルアクセル": "こおり", "こごえるかぜ": "こおり", "れいとうビーム": "こおり",
    "れいとうパンチ": "こおり",
    "１０まんボルト": "でんき", "かみなりパンチ": "でんき", "エレクトロビーム": "でんき",
    "ワイルドボルト": "でんき", "でんじは": "でんき",
    "インファイト": "かくとう", "はどうだん": "かくとう", "しんくうは": "かくとう",
    "バレットパンチ": "はがね", "コメットパンチ": "はがね",
    "マッハパンチ": "かくとう", "けたぐり": "かくとう", "とびひざげり": "かくとう",
    "ビルドアップ": "かくとう", "ボディプレス": "かくとう", "せいなるつるぎ": "かくとう",
    "ドレインパンチ": "かくとう",
    "かげうち": "ゴースト", "シャドーボール": "ゴースト", "ポルターガイスト": "ゴースト",
    "みちづれ": "ゴースト", "たたりめ": "ゴースト", "シャドークロー": "ゴースト",
    "おはかまいり": "ゴースト", "のろい": "ゴースト",
    "かみくだく": "あく", "はたきおとす": "あく", "ふいうち": "あく",
    "イカサマ": "あく", "ちょうはつ": "あく", "あくのはどう": "あく",
    "やけっぱち": "あく", "どろぼう": "あく",
    "アイアンヘッド": "はがね", "ラスターカノン": "はがね", "てっぺき": "はがね",
    "キングシールド": "はがね", "ジャイロボール": "はがね",
    "ソーラービーム": "くさ", "ギガドレイン": "くさ", "パワーウィップ": "くさ",
    "こうごうせい": "くさ", "エナジーボール": "くさ", "グラスフィールド": "くさ",
    "トリックフラワー": "くさ",
    "エアスラッシュ": "ひこう", "ブレイブバード": "ひこう", "はねやすめ": "ひこう",
    "きりばらい": "ひこう", "ダブルウイング": "ひこう",
    "とんぼがえり": "むし", "かえりうち": "むし", "ちょうのまい": "むし",
    "むしのさざめき": "むし", "むしくい": "むし",
    "めいそう": "エスパー", "サイコキネシス": "エスパー", "サイコノイズ": "エスパー",
    "しねんのずつき": "エスパー", "サイコカッター": "エスパー", "アシストパワー": "エスパー",
    "こうそくいどう": "エスパー", "ねむる": "エスパー", "トリックルーム": "エスパー",
    "トリック": "エスパー", "ミラーコート": "エスパー",
    "おいかぜ": "ひこう", "ぼうふう": "ひこう", "アクロバット": "ひこう",
    "フェザーダンス": "ひこう",
    "おきみやげ": "あく", "つじぎり": "あく", "わるだくみ": "あく",
    "しっとのほのお": "あく", "じごくづき": "あく", "ドゲザン": "あく",
    "からげんき": "ノーマル", "からをやぶる": "ノーマル", "こわいかお": "ノーマル",
    "すてみタックル": "ノーマル", "つきのひかり": "ノーマル", "でんこうせっか": "ノーマル",
    "ねがいごと": "ノーマル", "のしかかり": "ノーマル", "はかいこうせん": "ノーマル",
    "バトンタッチ": "ノーマル", "ハサミギロチン": "ノーマル", "ウェザーボール": "ノーマル",
    "かわらわり": "かくとう", "きあいだま": "かくとう", "ばかぢから": "かくとう",
    "みきり": "かくとう",
    "きゅうけつ": "むし", "とびかかる": "むし", "とびつく": "むし",
    "ねばねばネット": "むし",
    "くさむすび": "くさ", "くさわけ": "くさ", "ねむりごな": "くさ",
    "やどりぎのタネ": "くさ", "リーフストーム": "くさ", "リーフブレード": "くさ",
    "コットンガード": "くさ",
    "こおりのつぶて": "こおり", "ぜったいれいど": "こおり", "つららおとし": "こおり",
    "つららばり": "こおり", "ふぶき": "こおり", "フリーズドライ": "こおり",
    "オーロラベール": "こおり",
    "げんしのちから": "いわ", "ロックブラスト": "いわ",
    "さいみんじゅつ": "エスパー", "じんつうりき": "エスパー", "ふういん": "エスパー",
    "サイコショック": "エスパー", "コスモパワー": "エスパー", "ルミナコリジョン": "エスパー",
    "しおふき": "みず", "みずしゅりけん": "みず", "みずのはどう": "みず",
    "みずびたし": "みず", "ハイドロポンプ": "みず",
    "じわれ": "じめん", "ドリルライナー": "じめん",
    "ほうでん": "でんき", "パラボラチャージ": "でんき", "ボルトチェンジ": "でんき",
    "ほのおのうず": "ほのお", "ほのおのパンチ": "ほのお", "フレアソング": "ほのお",
    "ヒートスタンプ": "ほのお", "むねんのつるぎ": "ほのお",
    "みわくのボイス": "フェアリー",
    "メタルバースト": "はがね",
    "アシッドボム": "どく", "フェイタルクロー": "どく",
}

# ---- 性格 効果 ----
NATURE_EFFECTS = {
    "ようき": ("S↑", "C↓"), "いじっぱり": ("A↑", "C↓"), "おくびょう": ("S↑", "A↓"),
    "ひかえめ": ("C↑", "A↓"), "わんぱく": ("B↑", "C↓"), "しんちょう": ("D↑", "C↓"),
    "なまいき": ("D↑", "S↓"), "ずぶとい": ("B↑", "A↓"), "むじゃき": ("S↑", "D↓"),
    "うっかりや": ("C↑", "D↓"), "さみしがり": ("A↑", "B↓"), "やんちゃ": ("C↑", "D↓"),
    "おっとり": ("C↑", "S↓"), "れいせい": ("C↑", "S↓"), "おだやか": ("D↑", "A↓"),
    "ゆうかん": ("A↑", "S↓"), "のうてんき": ("C↑", "B↓"), "てれや": ("A↑", "C↓"),
    "ひねくれ": ("D↑", "B↓"), "うるさい": ("S↑", "D↓"),
}

# ---- アイテムアイコン ----
ITEM_PNG = {
    "きあいのタスキ": "item-0275-tasuki.png",
    "こだわりスカーフ": "item-0287-scarf.png",
    "オボンのみ": "item-0158-obon.png",
    "ラムのみ": "item-0157-ram.png",
    "ヤチェのみ": "item-0188-yache.png",
    "ハバンのみ": "item-0197-haban.png",
    "ガブリアスナイト": "item-0683-garchompite.png",
}
ITEM_SPRITE = {
    "たべのこし": (-288, -192), "ひかりのこな": (-384, -168), "やわらかいすな": (-360, -192),
    "こだわりメガネ": (-216, -264), "こだわりはちまき": (-192, -264),
    "いのちのたま": (0, -192), "とつげきチョッキ": (-456, -216), "ゴツゴツメット": (-456, -192),
    "じゃくてんほけん": (-24, -240), "クリアチャーム": (-120, -192),
    "メガフシギバナイト": (-192, -384), "メガリザードナイト": (-216, -384),
    "メガリザードナイトY": (-240, -384), "メガギャラドスナイト": (-312, -408),
    "メガルカリオナイト": (-336, -408), "メガミミロップナイト": (-360, -408),
    "メガハッサムナイト": (-384, -408), "メガゲンガーナイト": (-408, -408),
    "メガカイリューナイト": (-432, -408),
    "メガブリジュラスナイト": None,
}

# ---- メガシンカデータ ----
MEGA_DATA = {
    "リザードン": [
        {"name": "メガリザードンX", "types": ["ほのお", "ドラゴン"],
         "stats": [78, 130, 111, 130, 85, 100], "ability": "かたいつめ"},
        {"name": "メガリザードンY", "types": ["ほのお", "ひこう"],
         "stats": [78, 104, 78, 159, 115, 100], "ability": "ひでり"},
    ],
    "ルカリオ": [
        {"name": "メガルカリオ", "types": ["かくとう", "はがね"],
         "stats": [70, 145, 88, 140, 70, 112], "ability": "てきおうりょく"},
    ],
    "ゲンガー": [
        {"name": "メガゲンガー", "types": ["ゴースト", "どく"],
         "stats": [60, 65, 80, 170, 95, 130], "ability": "かげふみ"},
    ],
    "ギャラドス": [
        {"name": "メガギャラドス", "types": ["みず", "あく"],
         "stats": [95, 155, 109, 70, 130, 81], "ability": "かたやぶり"},
    ],
    "ミミロップ": [
        {"name": "メガミミロップ", "types": ["ノーマル", "かくとう"],
         "stats": [65, 136, 94, 54, 96, 135], "ability": "こんじょう"},
    ],
    "ハッサム": [
        {"name": "メガハッサム", "types": ["むし", "はがね"],
         "stats": [70, 150, 140, 65, 100, 75], "ability": "テクニシャン"},
    ],
    "フシギバナ": [
        {"name": "メガフシギバナ", "types": ["くさ", "どく"],
         "stats": [80, 100, 123, 122, 120, 80], "ability": "あついしぼう"},
    ],
    "カメックス": [
        {"name": "メガカメックス", "types": ["みず"],
         "stats": [79, 103, 120, 135, 115, 78], "ability": "メガランチャー"},
    ],
    "ガルーラ": [
        {"name": "メガガルーラ", "types": ["ノーマル"],
         "stats": [105, 125, 100, 60, 100, 100], "ability": "おやこあい"},
    ],
    "バンギラス": [
        {"name": "メガバンギラス", "types": ["いわ", "あく"],
         "stats": [100, 164, 150, 95, 120, 71], "ability": "すなおこし"},
    ],
    "エルレイド": [
        {"name": "メガエルレイド", "types": ["エスパー", "かくとう"],
         "stats": [68, 165, 95, 65, 115, 110], "ability": "かたやぶり"},
    ],
}

# ---- 各ポケモンの静的データ ----
POKEMON_DATA = {
    "ブリジュラス": {
        "file": "baxcalibur", "dex": 1018, "id": "1018-00",
        "types": ["ドラゴン", "はがね"],
        "stats": [90, 105, 130, 125, 65, 85],
    },
    "マスカーニャ": {
        "file": "meowscarada", "dex": 908, "id": "0908-00",
        "types": ["くさ", "あく"],
        "stats": [76, 110, 70, 70, 70, 123],
    },
    "アシレーヌ": {
        "file": "primarina", "dex": 730, "id": "0730-00",
        "types": ["みず", "フェアリー"],
        "stats": [80, 74, 74, 126, 116, 60],
    },
    "リザードン": {
        "file": "charizard", "dex": 6, "id": "0006-00",
        "types": ["ほのお", "ひこう"],
        "stats": [78, 84, 78, 109, 85, 100],
    },
    "アーマーガア": {
        "file": "corviknight", "dex": 823, "id": "0823-00",
        "types": ["はがね", "ひこう"],
        "stats": [98, 87, 105, 53, 85, 72],
    },
    "イダイトウ (オス)": {
        "file": "basculegion", "dex": 902, "id": "0902-00",
        "types": ["みず", "ゴースト"],
        "stats": [120, 112, 65, 80, 75, 78],
    },
    "カバルドン": {
        "file": "hippowdon", "dex": 450, "id": "0450-00",
        "types": ["じめん"],
        "stats": [108, 112, 118, 68, 72, 47],
    },
    "ルカリオ": {
        "file": "lucario", "dex": 448, "id": "0448-00",
        "types": ["かくとう", "はがね"],
        "stats": [70, 110, 70, 115, 70, 90],
    },
    "ゲンガー": {
        "file": "gengar", "dex": 94, "id": "0094-00",
        "types": ["ゴースト", "どく"],
        "stats": [60, 65, 60, 130, 75, 110],
        "analysis": ["gengar-analysis-m2"],
    },
    "ギャラドス": {
        "file": "gyarados", "dex": 130, "id": "0130-00",
        "types": ["みず", "ひこう"],
        "stats": [95, 125, 79, 60, 100, 81],
        "analysis": ["gyarados-analysis-m2"],
    },
    "ギルガルド": {
        "file": "aegislash", "dex": 681, "id": "0681-00",
        "types": ["はがね", "ゴースト"],
        "stats": [60, 50, 150, 50, 150, 60],
    },
    "フラエッテ:永遠": {
        "file": "floette-eternal", "dex": 670, "id": "0670-05",
        "display_name": "フラエッテ（永遠）",
        "types": ["フェアリー"],
        "stats": [74, 65, 67, 125, 128, 92],
        "analysis": ["florette-analysis-m2"],
    },
    "キラフロル": {
        "file": "glimmora", "dex": 970, "id": "0970-00",
        "types": ["いわ", "どく"],
        "stats": [83, 55, 90, 125, 90, 81],
    },
    "ミミロップ": {
        "file": "lopunny", "dex": 428, "id": "0428-00",
        "types": ["ノーマル"],
        "stats": [65, 76, 84, 54, 96, 105],
    },
    "カイリュー": {
        "file": "dragonite", "dex": 149, "id": "0149-00",
        "types": ["ドラゴン", "ひこう"],
        "stats": [91, 134, 95, 100, 100, 80],
        "analysis": ["dragonite-analysis-m2"],
    },
    "ハッサム": {
        "file": "scizor", "dex": 212, "id": "0212-00",
        "types": ["むし", "はがね"],
        "stats": [70, 130, 100, 55, 80, 65],
    },
    "ウルガモス": {
        "file": "volcarona", "dex": 637, "id": "0637-00",
        "types": ["ほのお", "むし"],
        "stats": [85, 60, 65, 135, 105, 100],
    },
    "ミミッキュ": {
        "file": "mimikyu", "dex": 778, "id": "0778-00",
        "types": ["ゴースト", "フェアリー"],
        "stats": [55, 90, 80, 50, 105, 96],
    },
    "スターミー": {
        "file": "starmie", "dex": 121, "id": "0121-00",
        "types": ["みず", "エスパー"],
        "stats": [60, 75, 85, 100, 85, 115],
        "analysis": ["starmie-analysis-m2"],
    },
    "サザンドラ": {
        "file": "hydreigon", "dex": 635, "id": "0635-00",
        "types": ["あく", "ドラゴン"],
        "stats": [92, 105, 90, 125, 90, 98],
    },
    "ウォッシュロトム": {
        "file": "rotom-wash", "dex": 479, "id": "0479-02",
        "types": ["みず", "でんき"],
        "stats": [50, 65, 107, 105, 107, 86],
    },
    "ダイケンキ (ヒスイ)": {
        "file": "samurott-hisui", "dex": 503, "id": "0503-01",
        "display_name": "ダイケンキ（ヒスイ）",
        "types": ["みず", "あく"],
        "stats": [110, 135, 70, 65, 80, 55],
    },
    "ドドゲザン": {
        "file": "kingambit", "dex": 983, "id": "0983-00",
        "types": ["あく", "はがね"],
        "stats": [100, 135, 120, 60, 85, 50],
    },
    "マフォクシー": {
        "file": "delphox", "dex": 655, "id": "0655-00",
        "types": ["ほのお", "エスパー"],
        "stats": [75, 69, 72, 114, 100, 104],
    },
    "ラウドボーン": {
        "file": "skeledirge", "dex": 911, "id": "0911-00",
        "types": ["ほのお", "ゴースト"],
        "stats": [104, 75, 100, 110, 75, 66],
    },
    "ソウブレイズ": {
        "file": "ceruledge", "dex": 937, "id": "0937-00",
        "types": ["ほのお", "ゴースト"],
        "stats": [75, 125, 80, 60, 80, 85],
    },
    "ゲッコウガ": {
        "file": "greninja", "dex": 658, "id": "0658-00",
        "types": ["みず", "あく"],
        "stats": [72, 95, 67, 103, 71, 122],
    },
    "フシギバナ": {
        "file": "venusaur", "dex": 3, "id": "0003-00",
        "types": ["くさ", "どく"],
        "stats": [80, 82, 83, 100, 100, 80],
    },
    "ブラッキー": {
        "file": "umbreon", "dex": 197, "id": "0197-00",
        "types": ["あく"],
        "stats": [95, 65, 110, 60, 130, 65],
    },
    "ハラバリー": {
        "file": "bellibolt", "dex": 939, "id": "0939-00",
        "types": ["でんき"],
        "stats": [109, 64, 67, 91, 67, 43],
    },
    "カメックス": {
        "file": "blastoise", "dex": 9, "id": "0009-00",
        "types": ["みず"],
        "stats": [79, 83, 100, 85, 105, 78],
    },
    "ガルーラ": {
        "file": "kangaskhan", "dex": 115, "id": "0115-00",
        "types": ["ノーマル"],
        "stats": [105, 95, 80, 40, 80, 90],
    },
    "オオニューラ": {
        "file": "sneasler", "dex": 903, "id": "0903-00",
        "types": ["どく", "かくとう"],
        "stats": [80, 130, 60, 40, 65, 120],
    },
    "クエスパトラ": {
        "file": "espathra", "dex": 956, "id": "0956-00",
        "types": ["エスパー"],
        "stats": [95, 60, 60, 101, 60, 105],
    },
    "ピクシー": {
        "file": "clefable", "dex": 36, "id": "0036-00",
        "types": ["フェアリー"],
        "stats": [95, 70, 73, 85, 90, 60],
    },
    "メガニウム": {
        "file": "meganium", "dex": 154, "id": "0154-00",
        "types": ["くさ"],
        "stats": [80, 82, 100, 83, 100, 80],
    },
    "ゾロアーク (ヒスイ)": {
        "file": "zoroark-hisui", "dex": 571, "id": "0571-01",
        "display_name": "ゾロアーク（ヒスイ）",
        "types": ["ノーマル", "ゴースト"],
        "stats": [55, 100, 60, 100, 60, 105],
    },
    "バンギラス": {
        "file": "tyranitar", "dex": 248, "id": "0248-00",
        "types": ["いわ", "あく"],
        "stats": [100, 134, 110, 95, 100, 61],
    },
    "オニシズクモ": {
        "file": "araquanid", "dex": 752, "id": "0752-00",
        "types": ["みず", "むし"],
        "stats": [68, 70, 92, 50, 132, 42],
    },
    "ニンフィア": {
        "file": "sylveon", "dex": 700, "id": "0700-00",
        "types": ["フェアリー"],
        "stats": [95, 65, 65, 110, 130, 60],
    },
    "ペリッパー": {
        "file": "pelipper", "dex": 279, "id": "0279-00",
        "types": ["みず", "ひこう"],
        "stats": [60, 50, 100, 85, 70, 65],
    },
    "エルフーン": {
        "file": "whimsicott", "dex": 547, "id": "0547-00",
        "types": ["くさ", "フェアリー"],
        "stats": [60, 67, 85, 77, 75, 116],
    },
    "マンムー": {
        "file": "mamoswine", "dex": 473, "id": "0473-00",
        "types": ["こおり", "じめん"],
        "stats": [110, 130, 80, 70, 60, 80],
    },
    "カビゴン": {
        "file": "snorlax", "dex": 143, "id": "0143-00",
        "types": ["ノーマル"],
        "stats": [160, 110, 65, 65, 110, 30],
    },
    "エアームド": {
        "file": "skarmory", "dex": 227, "id": "0227-00",
        "types": ["はがね", "ひこう"],
        "stats": [65, 80, 140, 40, 70, 70],
    },
    "スコヴィラン": {
        "file": "scovillain", "dex": 952, "id": "0952-00",
        "types": ["くさ", "ほのお"],
        "stats": [65, 108, 65, 108, 65, 75],
    },
    "エルレイド": {
        "file": "gallade", "dex": 475, "id": "0475-00",
        "types": ["エスパー", "かくとう"],
        "stats": [68, 125, 65, 65, 115, 80],
    },
    "ヒートロトム": {
        "file": "rotom-heat", "dex": 479, "id": "0479-01",
        "types": ["ほのお", "でんき"],
        "stats": [50, 65, 107, 105, 107, 86],
    },
    "バイバニラ": {
        "file": "vanilluxe", "dex": 584, "id": "0584-00",
        "types": ["こおり"],
        "stats": [71, 95, 85, 110, 95, 79],
    },
}

STAT_NAMES = ["HP", "こうげき", "ぼうぎょ", "とくこう", "とくぼう", "すばやさ"]
STAT_COLORS = [
    "linear-gradient(90deg,#60a5fa,#3b82f6)",
    "linear-gradient(90deg,#f97316,#dc2626)",
    "linear-gradient(90deg,#60a5fa,#3b82f6)",
    "linear-gradient(90deg,#c084fc,#7c3aed)",
    "linear-gradient(90deg,#60a5fa,#3b82f6)",
    "linear-gradient(90deg,#34d399,#059669)",
]

ABILITY_DESC = {
    "さめはだ": "直接攻撃を受けると相手に最大HPの1/8のダメージ",
    "すながくれ": "砂嵐のとき回避率が1.25倍になる",
    "がんじょうあご": "かみつく技の威力が1.5倍になる",
    "りんぷん": "相手のもちものや特性の効果を受けない",
    "ちからずく": "追加効果がある技の威力が1.3倍になるが追加効果はなくなる",
    "テクニシャン": "威力60以下の技の威力が1.5倍になる",
    "てきおうりょく": "タイプ一致技の補正が2倍になる",
    "ふゆう": "じめんタイプの技を受けない",
    "マジックガード": "直接ダメージ以外のダメージを受けない",
    "のろわれボディ": "接触技を受けると30%の確率で相手の技をかなしばりにする",
    "いかく": "登場時に相手全体のこうげきを1段階下げる",
    "じゅうなん": "まひ状態にならない。まひのすばやさ低下も受けない",
    "せいしんりょく": "ひるみ状態にならない。いかくを受けない",
    "しんがん": "必中になる",
    "ひでり": "登場時に天気をにほんばれにする（5ターン）",
    "あめふらし": "登場時に天気をあめにする（5ターン）",
    "すなおこし": "登場時に天気をすなあらしにする（5ターン）",
    "ゆきふらし": "登場時に天気をゆきにする（5ターン）",
    "はやあし": "状態異常のときすばやさが1.5倍になる",
    "どんかん": "いかく・おだやか・ちょうはつ・いじわるなどの変化技を受けない",
    "ナイーブ": "いたみわけ・ほろびのうた・ちょうはつなどが効かない",
    "かたやぶり": "相手の特性を無視して攻撃できる",
    "しょうりのほし": "自分の技が必ずあたる",
    "ふしぎなうろこ": "状態異常のとき防御が1.5倍になる",
    "ちくでん": "でんきタイプの技を受けるとHPが回復する",
    "よびみず": "みずタイプの技を引き寄せ、HPが回復する",
    "もらいび": "ほのおタイプの技を受けると無効化し、自分のほのお技が強化される",
    "ほのおのからだ": "接触技を受けると30%の確率で相手をやけど状態にする",
    "すなかき": "砂嵐のときすばやさが2倍になる",
    "あくしゅう": "攻撃時10%の確率で相手をひるませる",
    "ちょすい": "みずタイプの技を受けるとHPが回復する",
    "ライトメタル": "自分の重さが半分になる",
    "ヘヴィメタル": "自分の重さが2倍になる",
    "はりきり": "こうげきが1.5倍になるが命中率が0.8倍になる",
    "いたずらごころ": "変化技が先制で出せる（優先度+1）",
    "オーバーコート": "天気ダメージ・まきびし・どくびし・ほうし系の技を受けない",
    "ポイズンヒール": "どく状態のときターン終了時にHPが回復する",
    "マジックミラー": "相手の変化技を跳ね返す",
    "フィルター": "効果抜群の技のダメージを0.75倍に抑える",
    "クリアボディ": "能力を下げる効果を受けない",
    "なまけ": "1ターンおきにしか行動できない",
    "しぜんかいふく": "控えに戻ると状態異常が回復する",
    "かんそうはだ": "ほのおタイプの技で受けるダメージが1.25倍になる。みずタイプの技でHPが回復",
    "ものひろい": "バトル後にどうぐを入手できる",
    "うのミサイル": "特定の技の追加効果で2〜5回攻撃する",
    "ふゆう": "じめんタイプの技を受けない",
    "ミイラ": "接触技を使った相手の特性をミイラにする",
    "へんげんじざい": "使った技のタイプになる",
    "リミットシールド": "HPが半分を下回ると発動する（詳細はゲームで確認）",
    "ねつこうかん": "ほのおタイプの技を受けるとやけど状態になり、そのターン以降ほのお技が強化される",
    "どくのくさり": "接触技を使ったとき相手をどく状態にする",
    "サンドパワー": "砂嵐のときいわ・じめん・はがねタイプの技の威力が1.5倍になる",
    "かたいつめ": "接触技の威力が1.3倍になる",
    "かげふみ": "相手のポケモンを逃げられなくする",
    "こんじょう": "状態異常のときこうげきが1.5倍になる",
    "あめうけざら": "雨のとき毎ターンHPが最大HPの1/16回復する",
    "おみとおし": "登場時に相手のもちものを把握する",
    "かそく": "毎ターン終了時にすばやさが1段階上がる",
    "かるわざ": "もちものを失うとすばやさが2倍になる",
    "がんじょう": "HP満タンのとき一撃では倒れない。一撃必殺技も無効",
    "きもったま": "ゴーストタイプにノーマル・かくとうの技が当たる。いかくを受けない",
    "きれあじ": "切る技（スラッシュ系）の威力が1.5倍になる",
    "きんちょうかん": "相手のきのみを使えなくする",
    "くいしんぼう": "HP半分以下になるとすぐにきのみを食べる",
    "くだけるよろい": "物理攻撃を受けるとぼうぎょが1段階下がりすばやさが2段階上がる",
    "げきりゅう": "HPが1/3以下になるとみずタイプの技の威力が1.5倍になる",
    "しめりけ": "じばく・だいばくはつなどの自爆技を封じる",
    "しんりょく": "HPが1/3以下になるとくさタイプの技の威力が1.5倍になる",
    "すいほう": "みずタイプの技の威力が2倍になりほのおタイプの技のダメージを半減する",
    "すりぬけ": "相手の壁（リフレクター・光のかべ等）の効果を無視して攻撃できる",
    "するどいめ": "命中率が下がらない",
    "せいぎのこころ": "あくタイプの技を受けるとこうげきが1段階上がる",
    "せいでんき": "接触技を受けると30%の確率で相手をまひ状態にする",
    "そうだいしょう": "控えに倒されたポケモンの数に応じてこうげき・とくこうが上がる（1体ごとに10%、最大50%）",
    "てんねん": "相手の能力ランク上昇を無視して攻撃・防御できる",
    "でんきにかえる": "攻撃を受けた次のターン、でんきタイプの技の威力が2倍になる",
    "どくしゅ": "接触技を使ったとき30%の確率で相手をどく状態にする",
    "はやおき": "ねむり状態のとき通常より早く目覚める",
    "びんじょう": "相手がステータスを上昇させると同じステータスを1段階上げる",
    "ふくつのこころ": "ひるんだときすばやさが2段階上がる",
    "ふみん": "ねむり状態にならない",
    "まけんき": "こうげきが下げられると逆にこうげきが2段階上がる",
    "めんえき": "どく・ねむりなど状態異常にならない",
    "もうか": "HPが1/3以下になるとほのおタイプの技の威力が1.5倍になる",
    "ゆきがくれ": "ゆきのとき回避率が1.25倍になる",
    "ようりょくそ": "にほんばれのときすばやさが2倍になる",
    "アイスボディ": "ゆきのとき毎ターンHPが少しずつ回復する",
    "シンクロ": "状態異常になると相手にも同じ状態異常を与える",
    "フェアリースキン": "ノーマルタイプの技がフェアリータイプになり威力が1.2倍になる",
    "プレッシャー": "相手の技のPPを1ターンに2倍消費させる",
    "マジシャン": "攻撃したとき相手のもちものを奪う",
    "メガランチャー": "はどう系の技（みずのはどう・はどうだん等）の威力が1.5倍になる",
    "おやこあい": "技が2回ヒットする（2回目は威力の25%）",
    "ムラっけ": "ターン終了時にランダムで1つのステータスが2段階上昇し別の1つが1段階下降する",
    "メロメロボディ": "接触技を受けると30%の確率で相手をメロメロ状態にする",
    "リーフガード": "にほんばれのとき状態異常にならない",
}


def generate_mega_section(pokemon_name: str, base_types: list, base_stats: list) -> str:
    mega_list = MEGA_DATA.get(pokemon_name)
    if not mega_list:
        return ""

    def cells_html(type_list):
        if not type_list:
            return '<td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px;color:#aaa">—</div></td>'
        icons = "".join(type_icon_html(t, 36) for t in type_list)
        return f'<td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px;flex-wrap:wrap">{icons}</div></td>'

    blocks = []
    for mega in mega_list:
        name = mega["name"]
        types = mega["types"]
        stats = mega["stats"]
        ability = mega["ability"]
        total = sum(stats)

        type_icons = "".join(
            f'<img src="/images/types/type-{TYPE_NUM[t]}-{TYPE_SLUG[t]}.png" alt="{t}" style="width:36px;height:36px;vertical-align:middle" />'
            for t in types
        )
        ability_desc = ABILITY_DESC.get(ability, "—")

        stat_lines = []
        for i in range(6):
            val = stats[i]
            delta = val - base_stats[i]
            pct = min(int(val / 180 * 100), 100)
            if val >= 120:
                s_color = "#059669" if i == 5 else "#dc2626"
                val_str = f'<strong style="color:{s_color}">{val}</strong>'
            else:
                val_str = str(val)
            if delta > 0:
                delta_html = f'<span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+{delta}</span>'
            elif delta < 0:
                delta_html = f'<span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">{delta}</span>'
            else:
                delta_html = '<span style="width:40px"></span>'
            stat_lines.append(
                f'  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">\n'
                f'    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">{STAT_NAMES[i]}</span>\n'
                f'    <div style="flex:1;background:#eee;border-radius:4px;height:12px">\n'
                f'      <div style="width:{pct}%;background:{STAT_COLORS[i]};height:12px;border-radius:4px"></div>\n'
                f'    </div>\n'
                f'    <span style="width:32px;text-align:right">{val_str}</span>{delta_html}\n'
                f'  </div>'
            )
        stat_bars = "\n".join(stat_lines)

        type_changed = types != base_types
        type_section = ""
        if type_changed:
            eff = type_effectiveness(types)
            x4   = [t for t in ALL_TYPES if eff.get(t) == 4]
            x2   = [t for t in ALL_TYPES if eff.get(t) == 2]
            x025 = [t for t in ALL_TYPES if eff.get(t) == 0.25]
            x05  = [t for t in ALL_TYPES if eff.get(t) == 0.5]
            x0   = [t for t in ALL_TYPES if eff.get(t) == 0]
            has_x025 = bool(x025)
            x025_col = '<th style="padding:8px 12px;border:1px solid #cbd5e1">×¼ 耐性</th>' if has_x025 else ""
            x025_td  = cells_html(x025) if has_x025 else ""
            type_section = f"""
<p style="font-size:0.85rem;font-weight:600;margin:14px 0 6px">タイプ相性（メガシンカ後）</p>
<div style="overflow-x:auto;margin:6px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.85em;text-align:center">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×4 弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×2 弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×½ 耐性</th>
  {x025_col}
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×0 無効</th>
</tr></thead>
<tbody><tr>
  {cells_html(x4)}
  {cells_html(x2)}
  {cells_html(x05)}
  {x025_td}
  {cells_html(x0)}
</tr></tbody>
</table>
</div>"""

        blocks.append(f"""
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px 20px;margin:12px 0">

### {name}

<div style="display:flex;align-items:center;gap:6px;margin:4px 0 10px">{type_icons}</div>

**特性：{ability}** — {ability_desc}

<div style="max-width:380px;margin:10px 0;font-size:0.9em">
{stat_bars}
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">{total}</span><span style="width:40px"></span>
  </div>
</div>
{type_section}
</div>""")

    return f"""
## メガシンカ
{"".join(blocks)}

---"""


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def latest(conn, table, pokemon, field="season='M-2' AND rule='single'"):
    row = conn.execute(
        f"SELECT MAX(crawled_date) FROM {table} WHERE {field} AND pokemon=?", (pokemon,)
    ).fetchone()
    return row[0] if row else None


def query_db(conn, table, pokemon, col, alias=None):
    date = latest(conn, table, pokemon)
    if not date:
        return []
    rows = conn.execute(
        f"SELECT * FROM {table} WHERE season='M-2' AND rule='single' AND pokemon=? AND crawled_date=? ORDER BY rank LIMIT 10",
        (pokemon, date)
    ).fetchall()
    return rows


def item_icon_html(item_name: str) -> str:
    if item_name in ITEM_PNG:
        return f'<img src="/images/items/{ITEM_PNG[item_name]}" alt="{item_name}" style="width:24px;height:24px">'
    if item_name in ITEM_SPRITE and ITEM_SPRITE[item_name]:
        x, y = ITEM_SPRITE[item_name]
        return (f'<span style="display:inline-block;width:24px;height:24px;'
                f'background-image:url(\'/images/items/item-sprite.png\');'
                f'background-size:480px 648px;background-position:{x}px {y}px;'
                f'flex-shrink:0"></span>')
    return ""


def type_icon_html(t: str, size: int = 20) -> str:
    num = TYPE_NUM.get(t, "00")
    slug = TYPE_SLUG.get(t, "normal")
    return f'<img src="/images/types/type-{num}-{slug}.png" alt="{t}" style="width:{size}px;height:{size}px">'


def stat_bar_html(label: str, value: int, color: str, bold=False, s_color=None) -> str:
    pct = min(int(value / 180 * 100), 100)
    val_span = f'<strong style="color:{s_color}">{value}</strong>' if s_color else (f'<strong>{value}</strong>' if bold else str(value))
    return f'''  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">{label}</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:{pct}%;background:{color};height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">{val_span}</span>
  </div>'''


def generate_page(pokemon_name: str, usage_rank: int) -> str:
    pdata = POKEMON_DATA[pokemon_name]
    display_name = pdata.get("display_name", pokemon_name)
    file_id = pdata["id"]
    types = pdata["types"]
    stats = pdata["stats"]  # H A B C D S
    total = sum(stats)
    analysis_slugs = pdata.get("analysis", [])

    conn = get_conn()

    # 集計日
    date = latest(conn, "pokemon_moves", pokemon_name) or "2026-05-24"

    # 各データ取得
    moves = query_db(conn, "pokemon_moves", pokemon_name, "move")
    items = query_db(conn, "pokemon_items", pokemon_name, "item")
    abilities = query_db(conn, "pokemon_abilities", pokemon_name, "ability")
    natures = query_db(conn, "pokemon_natures", pokemon_name, "nature")

    ev_date = latest(conn, "pokemon_evs", pokemon_name)
    evs = conn.execute(
        "SELECT rank, ev_spread, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s, usage_rate "
        "FROM pokemon_evs WHERE season='M-2' AND rule='single' AND pokemon=? AND crawled_date=? ORDER BY rank LIMIT 10",
        (pokemon_name, ev_date)
    ).fetchall() if ev_date else []

    # チームメイト
    partner_date = latest(conn, "pokemon_partners", pokemon_name)
    usage_date = conn.execute(
        "SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-2' AND rule='single'"
    ).fetchone()[0]
    partners = conn.execute(
        """SELECT p.rank, p.partner, u.pokemon_id
           FROM pokemon_partners p
           LEFT JOIN pokemon_usage u
             ON u.pokemon=p.partner AND u.season=p.season AND u.rule=p.rule
             AND u.crawled_date=?
           WHERE p.pokemon=? AND p.season='M-2' AND p.rule='single' AND p.crawled_date=?
           ORDER BY p.rank""",
        (usage_date, pokemon_name, partner_date)
    ).fetchall() if partner_date else []

    conn.close()

    # タイプ相性計算
    eff = type_effectiveness(types)
    x4  = [t for t in ALL_TYPES if eff.get(t) == 4]
    x2  = [t for t in ALL_TYPES if eff.get(t) == 2]
    x025 = [t for t in ALL_TYPES if eff.get(t) == 0.25]
    x05 = [t for t in ALL_TYPES if eff.get(t) == 0.5]
    x0  = [t for t in ALL_TYPES if eff.get(t) == 0]
    has_x025 = bool(x025)

    # ---- フロントマター ----
    type_str = "/".join(types)
    rank_str = f"{usage_rank}位"
    desc = f"ポケモンチャンピオンズ M-2シーズンの{display_name}基礎データ。種族値・タイプ相性・特性と、技・持ち物・性格・チームメイトの使用率TOP10を掲載。使用率{rank_str}。"
    id_form = pdata["id"].split("-")[1]
    image_form_line = f"\nimageForm: '{id_form}'" if id_form != "00" else ""
    front = f"""---
title: '{display_name} | ポケモンチャンピオンズ 使用率・基礎データ M-2'
description: '{desc}'
pokemonName: '{display_name}'
dexNumber: {pdata['dex']}{image_form_line}
pubDate: '2026-05-24'
draft: true
{f"analysisSlug: '{analysis_slugs[0]}'" if len(analysis_slugs) == 1 else ""}
---"""

    # ---- ヘッダー ----
    type_icons = "".join(
        f'\n      <img src="/images/types/type-{TYPE_NUM[t]}-{TYPE_SLUG[t]}.png" alt="{t}" style="width:40px;height:40px;vertical-align:middle" />'
        for t in types
    )
    header = f"""
<div style="display:flex;align-items:center;gap:16px;margin:0 0 24px">
  <img src="/images/pokemon/pokemon-{file_id}.webp" alt="{display_name}" style="width:96px;height:96px" />
  <div>
    <h1 style="margin:0 0 6px;font-size:1.6rem">{display_name}</h1>
    <div style="display:flex;align-items:center;gap:6px;margin-bottom:6px">{type_icons}
    </div>
    <div style="font-size:0.85rem;color:#555">
      全国図鑑 <strong>No.{pdata['dex']}</strong>　／　M-2 使用率 <strong style="color:#dc2626">{rank_str}</strong>
    </div>
    <div style="font-size:0.78rem;color:#999;margin-top:4px">データ集計日：{date}</div>
  </div>
</div>

---"""

    # ---- 種族値 ----
    stat_bars = "\n".join(
        stat_bar_html(
            STAT_NAMES[i], stats[i], STAT_COLORS[i],
            bold=(stats[i] >= 120),
            s_color="#059669" if i == 5 else ("#dc2626" if stats[i] >= 120 else None)
        )
        for i in range(6)
    )
    section_stats = f"""
## 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
{stat_bars}
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">{total}</span>
  </div>
</div>

---"""

    # ---- タイプ相性 ----
    def cells_html(type_list):
        if not type_list:
            return '<td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px;color:#aaa">—</div></td>'
        icons = "".join(type_icon_html(t, 36) for t in type_list)
        return f'<td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px;flex-wrap:wrap">{icons}</div></td>'

    x025_col = f'<th style="padding:8px 12px;border:1px solid #cbd5e1">×¼ 耐性</th>' if has_x025 else ""
    x025_td = cells_html(x025) if has_x025 else ""
    section_type = f"""
## タイプ相性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×4 弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×2 弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×½ 耐性</th>
  {x025_col}
  <th style="padding:8px 12px;border:1px solid #cbd5e1">×0 無効</th>
</tr>
</thead>
<tbody>
<tr>
  {cells_html(x4)}
  {cells_html(x2)}
  {cells_html(x05)}
  {x025_td}
  {cells_html(x0)}
</tr>
</tbody>
</table>
</div>

---"""

    # ---- 特性 ----
    ability_rows = ""
    for i, row in enumerate(abilities):
        ab = row["ability"]
        rate = row["usage_rate"]
        desc_text = ABILITY_DESC.get(ab, "—")
        bg = ' style="background:#fef9c3"' if i == 0 else (' style="background:#fafafa"' if i % 2 == 0 else "")
        bold_open = "<font-weight:bold>" if i == 0 else ""
        ability_rows += f'''<tr{bg}>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;{'font-weight:bold' if i==0 else ''}">{ab}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#555">{desc_text}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{rate}%</td>
</tr>
'''
    section_ability = f"""
## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;width:30%">特性名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;width:80px">採用率</th>
</tr>
</thead>
<tbody>
{ability_rows}</tbody>
</table>
</div>

---"""

    # ---- 使用率データ ----
    def table_header(cols):
        ths = "".join(f'<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:{a};{w}">{n}</th>'
                      for n, a, w in cols)
        return f'<tr style="background:#f1f5f9">{ths}</tr>'

    # 技テーブル
    move_rows = ""
    for i, row in enumerate(moves):
        mv = row["move"]
        rate = row["usage_rate"]
        bg = ' style="background:#fef9c3"' if i == 0 else (' style="background:#fafafa"' if i % 2 == 0 else "")
        mt = MOVE_TYPE.get(mv)
        icon = f'{type_icon_html(mt)} ' if mt else ""
        move_rows += f'''<tr{bg}>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{i+1}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;{'font-weight:bold' if i==0 else ''}"><div style="display:flex;align-items:center;gap:6px">{icon}{mv}</div></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{rate}%</td>
</tr>
'''

    # 持ち物テーブル
    item_rows = ""
    for i, row in enumerate(items):
        it = row["item"]
        rate = row["usage_rate"]
        bg = ' style="background:#fef9c3"' if i == 0 else (' style="background:#fafafa"' if i % 2 == 0 else "")
        icon = item_icon_html(it)
        icon_wrap = f'<div style="display:flex;align-items:center;gap:6px">{icon}{it}</div>' if icon else it
        item_rows += f'''<tr{bg}>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{i+1}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;{'font-weight:bold' if i==0 else ''}">{icon_wrap}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{rate}%</td>
</tr>
'''

    # 性格テーブル
    nature_rows = ""
    for i, row in enumerate(natures):
        nat = row["nature"]
        rate = row["usage_rate"]
        bg = ' style="background:#fef9c3"' if i == 0 else (' style="background:#fafafa"' if i % 2 == 0 else "")
        eff_str = ""
        if nat in NATURE_EFFECTS:
            up, dn = NATURE_EFFECTS[nat]
            eff_str = f' <small style="color:#666">（{up} {dn}）</small>'
        nature_rows += f'''<tr{bg}>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{i+1}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;{'font-weight:bold' if i==0 else ''}">{nat}{eff_str}</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{rate}%</td>
</tr>
'''

    # EVテーブル
    def ev_cell(val):
        if val == 0:
            return f'<td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;color:#aaa">0</td>'
        bold = "<strong>" if val == 32 else ""
        bold_end = "</strong>" if val == 32 else ""
        return f'<td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">{bold}{val}{bold_end}</td>'

    ev_rows = ""
    for i, row in enumerate(evs):
        bg = ' style="background:#fef9c3"' if i == 0 else (' style="background:#fafafa"' if i % 2 == 0 else "")
        ev_rows += f'''<tr{bg}>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{i+1}</td>
  {ev_cell(row["ev_h"])}{ev_cell(row["ev_a"])}{ev_cell(row["ev_b"])}{ev_cell(row["ev_c"])}{ev_cell(row["ev_d"])}{ev_cell(row["ev_s"])}
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;{'font-weight:bold' if i==0 else ''}">{row["usage_rate"]}%</td>
</tr>
'''

    section_data = f"""
## 使用率データ（M-2シーズン）

### 技

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;width:44px">順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr></thead>
<tbody>
{move_rows}</tbody>
</table>
</div>

### 持ち物

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;width:44px">順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr></thead>
<tbody>
{item_rows}</tbody>
</table>
</div>

### 性格

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;width:44px">順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr></thead>
<tbody>
{nature_rows}</tbody>
</table>
</div>

### ステータス振り

<p style="font-size:0.8em;color:#666;margin:4px 0 8px">H=HP A=こうげき B=ぼうぎょ C=とくこう D=とくぼう S=すばやさ　最大値=32</p>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center;width:36px">順位</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">H</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">A</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">B</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">C</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">D</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">S</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr></thead>
<tbody>
{ev_rows}</tbody>
</table>
</div>"""

    # ---- チームメイト ----
    partner_cards = ""
    for row in partners:
        partner = row["partner"]
        pid = row["pokemon_id"]
        rank = row["rank"]
        if pid:
            partner_cards += f'''  <div style="text-align:center;padding:8px;border:1px solid #e2e8f0;border-radius:8px">
    <img src="/images/pokemon/pokemon-{pid}.webp" alt="{partner}" style="width:56px;height:56px;display:block;margin:0 auto 4px">
    <div style="font-size:0.72rem;font-weight:bold">{partner}</div>
    <div style="font-size:0.68rem;color:#888">{rank}位</div>
  </div>
'''
        else:
            partner_cards += f'''  <div style="text-align:center;padding:8px;border:1px solid #e2e8f0;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:88px">
    <div style="font-size:0.72rem;font-weight:bold">{partner}</div>
    <div style="font-size:0.68rem;color:#888">{rank}位</div>
  </div>
'''
    section_partners = f"""

### チームメイト（同居率 TOP10）

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(90px,1fr));gap:10px;margin:12px 0">
{partner_cards}</div>

---"""

    # ---- 考察記事 ----
    section_analysis = ""
    if analysis_slugs:
        cards = ""
        for slug in analysis_slugs:
            # 記事タイトルをslugから推定
            title_map = {
                "charizard-x-analysis-m2": "【ポケモンチャンピオンズ】リザードン（メガリザードンX）考察 M-2",
                "charizard-y-analysis-m2": "【ポケモンチャンピオンズ】リザードン（メガリザードンY）考察 M-2",
                "lucario-analysis-m2": "【ポケモンチャンピオンズ】ルカリオ考察 M-2 使用率9位",
                "gengar-analysis-m2": "【ポケモンチャンピオンズ】ゲンガー考察 M-2 使用率10位",
                "gyarados-analysis-m2": "【ポケモンチャンピオンズ】ギャラドス考察 M-2 使用率11位",
                "florette-analysis-m2": "【ポケモンチャンピオンズ】フラエッテ（永遠）考察 M-2",
                "kiraflosure-analysis-m2": "【ポケモンチャンピオンズ】キラフロル考察 M-2 使用率14位",
                "lopunny-analysis-m2": "【ポケモンチャンピオンズ】ミミロップ考察 M-2 S135高速",
                "dragonite-analysis-m2": "【ポケモンチャンピオンズ】カイリュー考察 M-2 使用率16位",
                "scizor-analysis-m2": "【ポケモンチャンピオンズ】ハッサム考察 M-2 使用率17位",
                "starmie-analysis-m2": "【ポケモンチャンピオンズ】スターミー考察 M-2 使用率20位",
                "garchomp-analysis-m2": "【ポケモンチャンピオンズ】ガブリアス考察 M-2 使用率1位",
            }
            title = title_map.get(slug, f"【ポケモンチャンピオンズ】{display_name}考察 M-2")
            cards += f'''<a href="/blog/{slug}/" style="display:flex;align-items:center;gap:12px;padding:16px;border:1px solid #e2e8f0;border-radius:8px;text-decoration:none;background:#f8fafc;transition:box-shadow 0.2s;margin-bottom:8px" onmouseover="this.style.boxShadow='0 4px 12px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow=''">
  <img src="/images/pokemon/pokemon-{file_id}.webp" alt="{display_name}" style="width:56px;height:56px;flex-shrink:0">
  <div>
    <div style="font-size:0.75rem;color:#0369a1;font-weight:700;margin-bottom:2px">考察記事</div>
    <div style="font-size:0.95rem;font-weight:bold;color:#1e293b">{title}</div>
  </div>
</a>
'''
        section_analysis = f"""
## 考察記事

{cards}"""

    section_mega = generate_mega_section(pokemon_name, types, stats)

    parts = [front, header, section_stats, section_type, section_ability]
    if section_mega:
        parts.append(section_mega)
    parts += [section_data, section_partners, section_analysis]
    return "\n".join(parts)


TARGET_POKEMON_ALL = [
    ("ブリジュラス", 2), ("マスカーニャ", 3), ("アシレーヌ", 4), ("リザードン", 5),
    ("アーマーガア", 6), ("イダイトウ (オス)", 7), ("カバルドン", 8), ("ルカリオ", 9),
    ("ゲンガー", 10), ("ギャラドス", 11), ("ギルガルド", 12), ("フラエッテ:永遠", 13),
    ("キラフロル", 14), ("ミミロップ", 15), ("カイリュー", 16), ("ハッサム", 17),
    ("ウルガモス", 18), ("ミミッキュ", 19), ("スターミー", 20),
    ("サザンドラ", 21), ("ウォッシュロトム", 22), ("ダイケンキ (ヒスイ)", 23),
    ("ドドゲザン", 24), ("マフォクシー", 25), ("ラウドボーン", 26), ("ソウブレイズ", 27),
    ("ゲッコウガ", 28), ("フシギバナ", 29), ("ブラッキー", 30), ("ハラバリー", 31),
    ("カメックス", 32), ("ガルーラ", 33), ("オオニューラ", 34), ("クエスパトラ", 35),
    ("ピクシー", 36), ("メガニウム", 37), ("ゾロアーク (ヒスイ)", 38), ("バンギラス", 39),
    ("オニシズクモ", 40), ("ニンフィア", 41), ("ペリッパー", 42), ("エルフーン", 43),
    ("マンムー", 44), ("カビゴン", 45), ("エアームド", 46), ("スコヴィラン", 47),
    ("エルレイド", 48), ("ヒートロトム", 49), ("バイバニラ", 50),
]
TARGET_POKEMON = TARGET_POKEMON_ALL

if __name__ == "__main__":
    import sys
    targets = TARGET_POKEMON
    if len(sys.argv) > 1:
        names = set(sys.argv[1:])
        targets = [(p, r) for p, r in TARGET_POKEMON_ALL if p in names or POKEMON_DATA.get(p, {}).get("file", "") in names]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for pokemon, rank in targets:
        pdata = POKEMON_DATA[pokemon]
        filename = OUT_DIR / f"{pdata['file']}.md"
        print(f"  生成: {filename.name} ({pokemon} 使用率{rank}位)")
        content = generate_page(pokemon, rank)
        filename.write_text(content, encoding="utf-8")
    print(f"\n完了: {len(targets)}件")
