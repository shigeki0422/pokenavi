"""レギュレーションM-C（2026/9/9〜）で解禁された分の静的データをDB投入。

対象（gamewith の個別ページで公開済みのもののみ）:
  通常種 4: ゴリランダー / セグレイブ / グソクムシャ / ボーマンダ
  メガ  4: メガボーマンダ / メガアブソルZ / メガガブリアスZ / メガルカリオZ

本編実在種は PokeAPI と照合済み（M-3で「名前を知らない＝独自種」と誤判定した教訓）。
メガボーマンダは gamewith の値と PokeAPI が完全一致することを確認済み。
Z系メガは Champions 独自なので gamewith の個別ページが唯一の出典。

9/9 正式公開で通常種25（フォルム込み）＋メガグソクムシャ・メガセグレイブを追加投入。
この2メガの特性は gamewith の個別ページが「9/9に判明予定」のまま・特性ページの所持一覧にも
未掲載で、一覧ページ(574460)の記載しか根拠が無かったため、ユーザー確認を取って確定させた
（かたいツメ / ねつこうかん）。ねつこうかんは環境初出なので実装＋テストも追加している。
"""
import os
import sqlite3

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pokenavi.db")

# 9/9 正式公開分（通常種25・フォルム込み）。名前・タイプ・種族値・重さは PokeAPI で照合。
# 和名も /pokemon-species の ja-Hrkt と一致することを確認している（M-3で「知らない名前＝独自種」と
# 誤判定した教訓。フォルムのスラッグは species の varieties から取得: toxtricity-amped /
# squawkabilly-green-plumage など、推測では 404 になる）。
# (名前, dex, form_index, pokeapi_name, type1, type2, H,A,B,C,D,S, 重さkg)
BASE2 = [
    ('プクリン', 40, 0, 'wigglytuff', 'ノーマル', 'フェアリー', 140, 70, 45, 85, 50, 45, 12.0),
    ('ペルシアン', 53, 0, 'persian', 'ノーマル', None, 65, 70, 60, 65, 65, 115, 32.0),
    ('アローラペルシアン', 53, 99, 'persian-alola', 'あく', None, 65, 60, 60, 75, 65, 115, 33.0),
    ('カモネギ', 83, 0, 'farfetchd', 'ノーマル', 'ひこう', 52, 90, 55, 58, 62, 60, 15.0),
    ('バリヤード', 122, 0, 'mr-mime', 'エスパー', 'フェアリー', 40, 45, 65, 100, 120, 90, 54.5),
    ('マルノーム', 317, 0, 'swalot', 'どく', None, 100, 73, 83, 73, 83, 55, 80.0),
    ('ゴーゴート', 673, 0, 'gogoat', 'くさ', None, 123, 100, 62, 97, 81, 68, 91.0),
    ('エースバーン', 815, 0, 'cinderace', 'ほのお', None, 80, 116, 75, 65, 75, 119, 33.0),
    ('インテレオン', 818, 0, 'inteleon', 'みず', None, 70, 85, 65, 125, 65, 120, 45.2),
    ('フォクスライ', 828, 0, 'thievul', 'あく', None, 70, 58, 58, 87, 92, 90, 19.9),
    ('ストリンダー(ハイ)', 849, 0, 'toxtricity-amped', 'でんき', 'どく', 75, 98, 70, 114, 70, 75, 40.0),
    ('ストリンダー(ロー)', 849, 1, 'toxtricity-low-key', 'でんき', 'どく', 75, 98, 70, 114, 70, 75, 40.0),
    ('オトスパス', 853, 0, 'grapploct', 'かくとう', None, 80, 118, 90, 70, 80, 42, 39.0),
    ('ニャイキング', 863, 0, 'perrserker', 'はがね', None, 70, 110, 100, 50, 60, 50, 28.0),
    ('ネギガナイト', 865, 0, 'sirfetchd', 'かくとう', None, 62, 135, 95, 68, 82, 65, 117.0),
    ('バチンウニ', 871, 0, 'pincurchin', 'でんき', None, 48, 101, 95, 91, 85, 15, 1.0),
    ('イエッサン(オス)', 876, 0, 'indeedee-male', 'エスパー', 'ノーマル', 60, 65, 55, 105, 95, 95, 28.0),
    ('イエッサン(メス)', 876, 1, 'indeedee-female', 'エスパー', 'ノーマル', 70, 55, 65, 95, 105, 85, 28.0),
    ('パーモット', 923, 0, 'pawmot', 'でんき', 'かくとう', 70, 115, 70, 70, 60, 105, 41.0),
    ('オリーヴァ', 930, 0, 'arboliva', 'くさ', 'ノーマル', 78, 69, 90, 125, 109, 39, 48.2),
    ('イキリンコ(グリーン)', 931, 0, 'squawkabilly-green-plumage', 'ノーマル', 'ひこう', 82, 96, 51, 45, 51, 92, 2.4),
    ('イキリンコ(ブルー)', 931, 1, 'squawkabilly-blue-plumage', 'ノーマル', 'ひこう', 82, 96, 51, 45, 51, 92, 2.4),
    ('イキリンコ(イエロー)', 931, 2, 'squawkabilly-yellow-plumage', 'ノーマル', 'ひこう', 82, 96, 51, 45, 51, 92, 2.4),
    ('イキリンコ(ホワイト)', 931, 3, 'squawkabilly-white-plumage', 'ノーマル', 'ひこう', 82, 96, 51, 45, 51, 92, 2.4),
    ('マフィティフ', 943, 0, 'mabosstiff', 'あく', None, 80, 120, 90, 60, 70, 85, 61.0),
]

# (名前, dex, pokeapi_name, type1, type2, H,A,B,C,D,S, 重さkg)  ※PokeAPI照合済み
BASE = [
    ("ゴリランダー",   812, "rillaboom",   "くさ",     None,     100, 125,  90,  60,  70,  85,  90.0),
    ("セグレイブ",     998, "baxcalibur",  "ドラゴン", "こおり", 115, 145,  92,  75,  86,  87, 210.0),
    ("グソクムシャ",   768, "golisopod",   "むし",     "みず",    75, 125, 140,  60,  90,  40, 108.0),
    ("ボーマンダ",     373, "salamence",   "ドラゴン", "ひこう",  95, 135,  80, 110,  80, 100, 102.6),
]

# (メガ名, ベース種, メガストーン, base_dex, pokeapi_name, type1, type2, H,A,B,C,D,S, 特性, 重さkg)
MEGA = [
    # 本編実在。gamewith と PokeAPI が完全一致
    ("メガボーマンダ", "ボーマンダ", "ボーマンダナイト", 373, "salamence-mega",
     "ドラゴン", "ひこう", 95, 145, 130, 120, 90, 120, "スカイスキン", 112.6),
    # 以下は Champions 独自（PokeAPI に無い）。出典=gamewith 個別ページ
    ("メガアブソルZ", "アブソル", "アブソルナイトZ", 359, None,
     "あく", "ゴースト", 65, 154, 60, 75, 60, 151, "きれあじ", 49.0),
    ("メガガブリアスZ", "ガブリアス", "ガブリアスナイトZ", 445, None,
     "ドラゴン", None, 108, 130, 85, 141, 85, 151, "ふゆう", 99.0),
    ("メガルカリオZ", "ルカリオ", "ルカリオナイトZ", 448, None,
     "かくとう", "はがね", 70, 100, 70, 164, 70, 151, "はどうのぼうご", 49.4),
    # 種族値・タイプ・重さは gamewith（一覧546494／個別575003・575000）。特性はユーザー確認済み
    ("メガグソクムシャ", "グソクムシャ", "グソクムシャナイト", 768, None,
     "むし", "はがね", 75, 150, 175, 70, 120, 40, "かたいツメ", 148.0),
    ("メガセグレイブ", "セグレイブ", "セグレイブナイト", 998, None,
     "ドラゴン", "こおり", 115, 175, 117, 105, 101, 87, "ねつこうかん", 315.0),
]

# 新規特性。効果文は gamewith の記載どおり
ABILITIES = [
    ("はどうのぼうご", "接触技で受けるダメージが半減する。"),
    ("ねつこうかん", "ほのおタイプの技のダメージを受けると攻撃が1段階上がる。やけど状態にならない。"),
    ("ききかいひ", "HPが1/2以下になると手持ちに戻る。"),
    ("くさのけがわ", "グラスフィールド状態の時、防御が1.5倍になる。"),
    ("こぼれダネ", "技のダメージを受けた時から5ターンの間、全体の場をグラスフィールド状態にする。"),
    ("にげあし", "交代を邪魔する効果を無視して、手持ちの他のポケモンと交代することができる。"),
    ("はがねのせいしん", "自分と味方のはがねタイプの技の威力が1.5倍になる。"),
    ("はりこみ", "交代で出てきた相手に攻撃する時、技の威力が2倍になる。"),
    ("ばんけん", "いかくが効かず攻撃が1段階上がる。相手を入れ替えさせる技や道具が効かない。"),
    ("びびり", "あく、ゴースト、むしタイプの技のダメージやいかくを受けた時、素早さが1段階上がる。"),
    ("グラスメイカー", "登場した時から5ターンの間、全体の場をグラスフィールド状態にする。"),
    ("サイコメイカー", "登場した時から5ターンの間、全体の場をサイコフィールド状態にする。地面にいるすべてのポケモンは、相手の先制技を受けなくなり、またエスパータイプの技の威力が1.3倍になる。"),
    ("パンクロック", "音の技の威力が1.3倍になり、音の技で受けるダメージが半減する。"),
    ("ヘドロえき", "HPを吸い取る技を受けた時、相手を回復させずその分のダメージを与える。"),
    ("リベロ", "登場するたび1回だけ自分が出す技と同じタイプに変化する。"),
]

# 追加メガストーン（メガ石は endswith 判定で一括処理されるが、item_master には登録が要る）
ITEMS = [(m[2], "対応するポケモンがバトル中にメガシンカできる。", "mega") for m in MEGA]


# 新規技。タイプ/分類/威力/命中/優先度/PP/効果文は gamewith 技一覧(546417)の記載どおり
MOVES = [
    ("きょけんとつげき", "glaive-rush", "ドラゴン", "physical", 120, 100, 0, 8,
     "次に自分が行動するまで、自分は無防備状態になる。"),
    ("ドラムアタック", "drum-beating", "くさ", "physical", 80, 100, 0, 12,
     "相手の素早さを1段階下げる。"),
    ("かえんボール", "pyro-ball", "ほのお", "physical", 120, 90, 0, 8,
     "10%の確率で相手をやけど状態にする。使うと自分のこおり状態をなおす。"),
    ("コートチェンジ", "court-change", "ノーマル", "status", None, 100, 0, 12,
     "味方と相手の場の状態を入れ替える。"),
    ("でんこうそうげき", "double-shock", "でんき", "physical", 120, 100, 0, 8,
     "自分のでんきタイプがなくなる。自分がでんきタイプではない場合、失敗する。"),
    ("さいきのいのり", "revival-blessing", "ノーマル", "status", None, None, 0, 1,
     "手持ちのひんしのポケモンを最大HPの1/2の状態で復活させる。"),
    ("スターアサルト", "meteor-assault", "かくとう", "physical", 170, 100, 0, 8,
     "使った次のターン、自分は反動状態になる。"),
    ("ねらいうち", "snipe-shot", "みず", "special", 85, 100, 0, 16,
     "技を引き受ける特性や技の影響を無視する。きゅうしょアップ+1で攻撃する。"),
]


def main() -> None:
    con = sqlite3.connect(DB)
    cur = con.cursor()
    n = {"base": 0, "mega": 0, "abil": 0, "item": 0, "move": 0}
    for name, dex, fi, api, t1, t2, h, a, b, c, d, s, w in BASE2:
        if cur.execute("SELECT 1 FROM pokemon_base_stats WHERE pokemon_name=?", (name,)).fetchone():
            continue
        cur.execute(
            "INSERT INTO pokemon_base_stats(pokemon_name,dex_number,form_index,pokeapi_name,"
            "type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,weight_kg)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, dex, fi, api, t1, t2, h, a, b, c, d, s, w))
        n["base"] += 1
    for name, dex, api, t1, t2, h, a, b, c, d, s, w in BASE:
        if cur.execute("SELECT 1 FROM pokemon_base_stats WHERE pokemon_name=?", (name,)).fetchone():
            continue
        cur.execute(
            "INSERT INTO pokemon_base_stats(pokemon_name,dex_number,form_index,pokeapi_name,"
            "type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,weight_kg)"
            " VALUES(?,?,0,?,?,?,?,?,?,?,?,?,?)", (name, dex, api, t1, t2, h, a, b, c, d, s, w))
        n["base"] += 1
    for name, base, stone, bdex, api, t1, t2, h, a, b, c, d, s, ab, w in MEGA:
        if cur.execute("SELECT 1 FROM pokemon_mega_stats WHERE mega_name_jp=?", (name,)).fetchone():
            continue
        cur.execute(
            "INSERT INTO pokemon_mega_stats(mega_name_jp,base_pokemon_jp,mega_stone,base_dex,"
            "pokeapi_name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,ability,weight_kg)"
            " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (name, base, stone, bdex, api, t1, t2, h, a, b, c, d, s, ab, w))
        n["mega"] += 1
    for name, eff in ABILITIES:
        if cur.execute("SELECT 1 FROM ability_master WHERE name_jp=?", (name,)).fetchone():
            continue
        cur.execute("INSERT INTO ability_master(name_jp,effect_text,implemented) VALUES(?,?,1)",
                    (name, eff))
        n["abil"] += 1
    for name, eff, cat in ITEMS:
        if cur.execute("SELECT 1 FROM item_master WHERE name_jp=?", (name,)).fetchone():
            continue
        cur.execute("INSERT INTO item_master(name_jp,effect_text,category,implemented) VALUES(?,?,?,1)",
                    (name, eff, cat))
        n["item"] += 1
    for name, en, ty, cat, pw, acc, pri, pp, eff in MOVES:
        if cur.execute("SELECT 1 FROM move_master WHERE name_jp=?", (name,)).fetchone():
            continue
        cur.execute("INSERT INTO move_master(name_jp,name_en,type,category,power,accuracy,"
                    "priority,pp,effect_text) VALUES(?,?,?,?,?,?,?,?,?)",
                    (name, en, ty, cat, pw, acc, pri, pp, eff))
        n["move"] += 1
    con.commit()
    print(f"投入: 種{n['base']} / メガ{n['mega']} / 特性{n['abil']} / 持ち物{n['item']} / 技{n['move']}")


if __name__ == "__main__":
    main()
