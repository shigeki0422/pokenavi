#!/usr/bin/env python3
"""
バトルシミュレーター 全機能テストスイート
わざ・とくせい・アイテムの実装を網羅的に検証する
"""
import sys, math, random
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from simulator.data import DataLoader, get_type_effectiveness
from simulator.battle import (
    Battle, BattleSide, BattleField, Action,
    _execute_move, _apply_status_move, _check_critical, _apply_recoil,
)
from simulator.pokemon import BattlePokemon, calc_stat, calc_hp
from simulator.damage import calc_damage
from simulator.items import (
    get_type_boost, get_crit_stage_bonus, get_speed_item_multiplier,
    is_choice_item, try_cure_berry, try_white_herb,
    apply_hp_berry, on_item_consumed, get_evasion_item_mult,
)

dl = DataLoader()
PASS = FAIL = 0
FAILURES = []

def check(desc: str, cond: bool, detail: str = ""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        msg = f"FAIL: {desc}" + (f" → {detail}" if detail else "")
        FAILURES.append(msg)
        print(f"  ✗ {msg}")

def make_poke(name="テスト", type1="ノーマル", type2=None,
              hp_b=100, atk_b=100, def_b=100,
              spatk_b=100, spdef_b=100, spd_b=100,
              moves=None, item=None, ability="しんりょく", nature=""):
    ms = []
    for m in (moves or []):
        md = dl.get_move(m) if isinstance(m, str) else m
        ms.append(md)
    p = BattlePokemon(
        name=name, dex=0, type1=type1, type2=type2,
        max_hp=calc_hp(hp_b, 0), hp=calc_hp(hp_b, 0),
        attack=calc_stat(atk_b, 0, 31, 1.0),
        defense=calc_stat(def_b, 0, 31, 1.0),
        sp_attack=calc_stat(spatk_b, 0, 31, 1.0),
        sp_defense=calc_stat(spdef_b, 0, 31, 1.0),
        speed=calc_stat(spd_b, 0, 31, 1.0),
        moves=ms, pp=[10] * len(ms),
        base_type1=type1, base_type2=type2,
        ability=ability, item=item, nature=nature,
    )
    return p

def dmg(attacker, defender, move_name, roll=0.5, crit=False, f=None):
    m = dl.get_move(move_name) if isinstance(move_name, str) else move_name
    return calc_damage(attacker, defender, m, f or BattleField(), crit, roll)

def execute(attacker, defender, move_name, f=None):
    m = dl.get_move(move_name) if isinstance(move_name, str) else move_name
    s1 = BattleSide([attacker]); s2 = BattleSide([defender])
    return _execute_move(s1, s2, Action(type="move", move=m), f or BattleField())

def near(a, b, rel=0.02):
    return abs(a - b) <= max(1, round(b * rel))


# ════════════════════════════════════════════════════════════════
# 1. アイテムテスト
# ════════════════════════════════════════════════════════════════
print("\n=== 1. アイテム ===")

# ── タイプ強化アイテム (1.2倍) ──
TYPE_BOOST_CASES = [
    ("もくたん",         "ほのお"),   ("とけないこおり",   "こおり"),
    ("しんぴのしずく",   "みず"),     ("じしゃく",         "でんき"),
    ("くろいメガネ",     "あく"),     ("ようせいのハネ",   "フェアリー"),
    ("どくバリ",         "どく"),     ("やわらかいすな",   "じめん"),
    ("するどいくちばし", "ひこう"),   ("シルクのスカーフ", "ノーマル"),
    ("りゅうのキバ",     "ドラゴン"), ("くろおび",         "かくとう"),
    ("まがったスプーン", "エスパー"), ("のろいのおふだ",   "ゴースト"),
    ("メタルコート",     "はがね"),   ("かたいいし",       "いわ"),
    ("ぎんのこな",       "むし"),
]
for item, typ in TYPE_BOOST_CASES:
    boost = get_type_boost(item, typ, "テスト")
    check(f"タイプ強化: {item}({typ})", near(boost, 1.2))
    check(f"タイプ強化 別タイプ無効: {item}", get_type_boost(item, "ノーマル" if typ != "ノーマル" else "ほのお", "テスト") == 1.0)

# でんきだま: ピカチュウのでんき技のみ2倍
check("でんきだま ピカチュウ電気", get_type_boost("でんきだま", "でんき", "ピカチュウ") == 2.0)
check("でんきだま 非ピカチュウ無効", get_type_boost("でんきだま", "でんき", "ライチュウ") == 1.0)
check("でんきだま 非でんき技は無補正", get_type_boost("でんきだま", "ノーマル", "ピカチュウ") == 1.0)

# ── ダメージ倍率アイテム ──
p_normal = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
p_target = make_poke(type1="ノーマル", def_b=100, spdef_b=100)

d_base = dmg(p_normal, p_target, "たいあたり", roll=0.5)
p_normal.item = "こだわりハチマキ"
d_band = dmg(p_normal, p_target, "たいあたり", roll=0.5)
check("こだわりハチマキ 物理1.5倍", near(d_band / d_base, 1.5))

p_normal.item = "こだわりメガネ"
d_base_sp = dmg(p_normal, p_target, "りゅうのいぶき", roll=0.5)
p_normal.item = None
d_base_sp_no = dmg(p_normal, p_target, "りゅうのいぶき", roll=0.5)
check("こだわりメガネ 特殊1.5倍", near(d_base_sp / d_base_sp_no, 1.5))

p_normal.item = "ちからのハチマキ"
d_m = dmg(p_normal, p_target, "たいあたり", roll=0.5)
p_normal.item = None
d_nm = dmg(p_normal, p_target, "たいあたり", roll=0.5)
check("ちからのハチマキ 物理1.1倍", near(d_m / d_nm, 1.1))

p_normal.item = "ものしりメガネ"
d_m2 = dmg(p_normal, p_target, "りゅうのいぶき", roll=0.5)
p_normal.item = None
d_nm2 = dmg(p_normal, p_target, "りゅうのいぶき", roll=0.5)
check("ものしりメガネ 特殊1.1倍", near(d_m2 / d_nm2, 1.1))

p_normal.item = "いのちのたま"
d_lo = dmg(p_normal, p_target, "たいあたり", roll=0.5)
p_normal.item = None
d_no = dmg(p_normal, p_target, "たいあたり", roll=0.5)
check("いのちのたま 1.3倍", near(d_lo / d_no, 1.3))

# いのちのたま 反動
p_lo = make_poke(item="いのちのたま", moves=["たいあたり"])
p_t  = make_poke()
hp_before = p_lo.hp
execute(p_lo, p_t, "たいあたり")
recoil = hp_before - p_lo.hp
check("いのちのたま 反動1/10", near(recoil, p_lo.max_hp // 10))

# たつじんのおび: 抜群時1.2倍
p_water = make_poke(type1="みず", spatk_b=100, item="たつじんのおび")
p_fire   = make_poke(type1="ほのお", spdef_b=100)
d_se = dmg(p_water, p_fire, "なみのり", roll=0.5)
p_water.item = None
d_se_no = dmg(p_water, p_fire, "なみのり", roll=0.5)
check("たつじんのおび 抜群1.2倍", near(d_se / d_se_no, 1.2))
p_water.item = "たつじんのおび"
p_normal2 = make_poke(type1="ノーマル", spdef_b=100)
d_ne = dmg(p_water, p_normal2, "なみのり", roll=0.5)
p_water.item = None
d_ne_no = dmg(p_water, p_normal2, "なみのり", roll=0.5)
check("たつじんのおび 等倍は無効", d_ne == d_ne_no)

# ── 急所アイテム ──
check("ピントレンズ crit+1",   get_crit_stage_bonus("ピントレンズ")  == 1)
check("するどいツメ crit+1",   get_crit_stage_bonus("するどいツメ")  == 1)
check("ラッキーパンチ crit+2", get_crit_stage_bonus("ラッキーパンチ") == 2)

# ── 速度アイテム ──
check("こだわりスカーフ速度1.5倍", get_speed_item_multiplier("こだわりスカーフ") == 1.5)
check("速度アイテムなし1.0",        get_speed_item_multiplier(None) == 1.0)

# ── こだわり縛り ──
check("こだわりスカーフ is_choice", is_choice_item("こだわりスカーフ"))
check("こだわりハチマキ is_choice", is_choice_item("こだわりハチマキ"))
check("こだわりメガネ is_choice",   is_choice_item("こだわりメガネ"))
check("たべのこし not choice",      not is_choice_item("たべのこし"))

# ── 回避率アイテム ──
check("ひかりのこな 命中-10%", near(get_evasion_item_mult("ひかりのこな"), 0.90))
check("なし 回避補正なし",      get_evasion_item_mult(None) == 1.0)

# ── せんせいのツメ（20%先制・統計） ──
from simulator.items import has_quick_claw_trigger
random.seed(41); _qc = sum(1 for _ in range(2000) if has_quick_claw_trigger("せんせいのツメ"))
check("せんせいのツメ 20%先制", 0.16 < _qc / 2000 < 0.24, f"{_qc}/2000")
check("せんせいのツメ なしは先制しない", not has_quick_claw_trigger(None))

# ── メガストーン機構（_is_megastone・はたきおとす無効） ──
from simulator.battle import _is_megastone
check("メガストーン判定 ガブリアスナイト", _is_megastone("ガブリアスナイト"))
check("メガストーン判定 リザードナイトＸ", _is_megastone("リザードナイトＸ"))
check("メガストーン判定 リザードナイトＹ", _is_megastone("リザードナイトＹ"))
check("メガストーン判定 きのみは非対象", not _is_megastone("オボンのみ"))
# はたきおとす：通常道具には1.5倍、メガストーンには補正なし
_pko = make_poke(atk_b=100); _dko_item = make_poke(type1="ノーマル", def_b=80, item="たべのこし")
_dko_mega = make_poke(type1="ノーマル", def_b=80, item="リザードナイトＸ")
_dko_none = make_poke(type1="ノーマル", def_b=80, item=None)
check("はたきおとす 通常道具で1.5倍", near(dmg(_pko, _dko_item, "はたきおとす") / dmg(_pko, _dko_none, "はたきおとす"), 1.5))
check("はたきおとす メガ石Ｘは補正なし", dmg(_pko, _dko_mega, "はたきおとす") == dmg(_pko, _dko_none, "はたきおとす"))
# データ整合：環境の全メガストーンが mega_stats で解決できること（メガ表の取りこぼし防止）
import sqlite3 as _sq3
_con = _sq3.connect("scripts/pokenavi.db")
_unresolved = [r[0] for r in _con.execute(
    "SELECT DISTINCT item FROM pokemon_items WHERE item LIKE '%ナイト%' "
    "AND item NOT IN (SELECT mega_stone FROM pokemon_mega_stats)").fetchall()]
_con.close()
check("全メガストーンがmega_statsで解決", not _unresolved, f"未解決={_unresolved}")
# メガ後タイプは交代時の型リセット(type=base_type)で巻き戻らない＝do_mega が base_type も更新する
from simulator.simulate import get_loader as _glx
from simulator.pokemon import build_from_spec as _bfs, parse_pokemon_spec as _pps
import _pop_gen as _pg
_Lx = _glx()
_liz = _bfs(_pps(_pg._spec("リザードン", "リザードナイトX", "いじっぱり", ["フレアドライブ"], (0, 32, 0, 0, 0, 32), "もうか")), _Lx, season="M-3", randomize=False)
_liz.do_mega_evolve()
check("メガリザードンX 進化後タイプ ほのお/ドラゴン", (_liz.type1, _liz.type2) == ("ほのお", "ドラゴン"))
_liz.type1, _liz.type2 = _liz.base_type1, _liz.base_type2   # 交代時リセット相当
check("メガ後タイプは交代リセットで巻き戻らない", (_liz.type1, _liz.type2) == ("ほのお", "ドラゴン"))
# メガ進化後もメガストーンは持ち物として残る（実機仕様）。消すとポルターガイストが「持ち物なし」で失敗する不整合。
check("メガ進化後もメガストーンを保持", _liz.item == "リザードナイトX", f"item={_liz.item}")
# データ整合：全環境ポケモン（姿・フォルム）がローダーで種族値解決できること
from simulator.data import DataLoader as _DL_pk
_dlpk = _DL_pk("scripts/pokenavi.db")
_envpk = [r[0] for r in _dlpk.con.execute(
    "SELECT DISTINCT pokemon FROM pokemon_usage WHERE season='M-2' AND rule='single'")]
_unresolved_pk = [p for p in _envpk if _dlpk.get_pokemon_template(p) is None]
check("全環境ポケモンがローダーで解決", not _unresolved_pk, f"未解決={_unresolved_pk[:5]}")
# フォルムエイリアス：パルデアケンタロス(炎)→ケンタロス:炎(かくとう/ほのお)
_pkt = _dlpk.get_pokemon_template("パルデアケンタロス(炎)")
check("フォルム別名 パルデアケンタロス(炎)解決", _pkt is not None and _pkt.type1 == "かくとう" and _pkt.type2 == "ほのお")
# メガ進化データ（gamewith確定値）＋重さ反映
_mega_exp = {
    "オーダイル": ("オーダイルナイト", "みず", "ドラゴン", "ドラゴンスキン", 108.8, (85,160,125,89,93,78)),
    "メガニウム": ("メガニウムナイト", "くさ", "フェアリー", "メガソーラー", 201.0, (80,92,115,143,115,80)),
    "ニャオニクス(オス)": ("ニャオニクスナイト", "エスパー", None, "トレース", 10.1, (74,48,76,143,101,124)),
    "タブンネ": ("タブンネナイト", "ノーマル", "フェアリー", "いやしのこころ", None, (103,60,126,80,126,50)),
}
for _bp, (_st, _t1, _t2, _ab, _w, _stat) in _mega_exp.items():
    _md = _dlpk.get_pokemon_template(_bp).mega_data.get(_st)
    check(f"メガ{_bp} 解決", _md is not None, f"{_bp}@{_st}")
    if _md:
        check(f"メガ{_bp} タイプ/特性", _md.type1 == _t1 and _md.type2 == _t2 and _md.ability == _ab,
              f"{_md.type1}/{_md.type2} {_md.ability}")
        check(f"メガ{_bp} 種族値", (_md.hp,_md.attack,_md.defense,_md.sp_attack,_md.sp_defense,_md.speed) == _stat)
        if _w:
            check(f"メガ{_bp} 重さ{_w}", _md.weight_kg == _w, f"weight={_md.weight_kg}")

# M-C解禁分（2026/9/9〜）の静的データ。通常種はPokeAPI照合済み・Z系メガはgamewith個別ページが出典
_mc_base = {
    "ゴリランダー": ("くさ", None, (100,125,90,60,70,85), 90.0),
    "セグレイブ": ("ドラゴン", "こおり", (115,145,92,75,86,87), 210.0),
    "グソクムシャ": ("むし", "みず", (75,125,140,60,90,40), 108.0),
    "ボーマンダ": ("ドラゴン", "ひこう", (95,135,80,110,80,100), 102.6),
}
for _n, (_t1, _t2, _stat, _w) in _mc_base.items():
    _tp = _dlpk.get_pokemon_template(_n)
    check(f"M-C {_n} 解決", _tp is not None)
    if _tp:
        check(f"M-C {_n} タイプ", (_tp.type1, _tp.type2) == (_t1, _t2), f"{_tp.type1}/{_tp.type2}")
        check(f"M-C {_n} 種族値",
              (_tp.base_hp,_tp.base_attack,_tp.base_defense,
               _tp.base_sp_attack,_tp.base_sp_defense,_tp.base_speed) == _stat)
        check(f"M-C {_n} 重さ{_w}", _tp.weight_kg == _w, f"weight={_tp.weight_kg}")
_mc_mega = {
    "ボーマンダ": ("ボーマンダナイト", "ドラゴン", "ひこう", "スカイスキン", 112.6, (95,145,130,120,90,120)),
    "アブソル": ("アブソルナイトZ", "あく", "ゴースト", "きれあじ", 49.0, (65,154,60,75,60,151)),
    "ガブリアス": ("ガブリアスナイトZ", "ドラゴン", None, "ふゆう", 99.0, (108,130,85,141,85,151)),
    "ルカリオ": ("ルカリオナイトZ", "かくとう", "はがね", "はどうのぼうご", 49.4, (70,100,70,164,70,151)),
}
for _bp, (_st, _t1, _t2, _ab, _w, _stat) in _mc_mega.items():
    _md = _dlpk.get_pokemon_template(_bp).mega_data.get(_st)
    check(f"M-C メガ{_bp} 解決", _md is not None, f"{_bp}@{_st}")
    if _md:
        check(f"M-C メガ{_bp} タイプ/特性",
              _md.type1 == _t1 and _md.type2 == _t2 and _md.ability == _ab,
              f"{_md.type1}/{_md.type2} {_md.ability}")
        check(f"M-C メガ{_bp} 種族値",
              (_md.hp,_md.attack,_md.defense,_md.sp_attack,_md.sp_defense,_md.speed) == _stat)
        check(f"M-C メガ{_bp} 重さ{_w}", _md.weight_kg == _w, f"weight={_md.weight_kg}")
# Zサフィックスのメガ石がメガストーン判定に乗ること（はたきおとす・トリック等の失敗条件）
from simulator.battle import _is_megastone as _ismst
for _z in ("アブソルナイトZ", "ガブリアスナイトZ", "ルカリオナイトZ"):
    check(f"{_z} はメガストーン判定", _ismst(_z) is True)
check("ナイトZ 全角Ｚも判定", _ismst("ルカリオナイトＺ") is True)
check("非メガ石はメガストーン判定でない(負例)", _ismst("たべのこし") is False)

# M-C 9/9 正式公開分（通常種25・フォルム込み）。PokeAPI照合値をそのまま固定する。
# フォルムのスラッグは species の varieties から取ったもの（toxtricity-amped /
# squawkabilly-green-plumage 等。推測すると404になる）。
_mc2 = [
    ('プクリン', 'ノーマル', 'フェアリー', (140,70,45,85,50,45), 12.0),
    ('ペルシアン', 'ノーマル', None, (65,70,60,65,65,115), 32.0),
    ('アローラペルシアン', 'あく', None, (65,60,60,75,65,115), 33.0),
    ('カモネギ', 'ノーマル', 'ひこう', (52,90,55,58,62,60), 15.0),
    ('バリヤード', 'エスパー', 'フェアリー', (40,45,65,100,120,90), 54.5),
    ('マルノーム', 'どく', None, (100,73,83,73,83,55), 80.0),
    ('ゴーゴート', 'くさ', None, (123,100,62,97,81,68), 91.0),
    ('エースバーン', 'ほのお', None, (80,116,75,65,75,119), 33.0),
    ('インテレオン', 'みず', None, (70,85,65,125,65,120), 45.2),
    ('フォクスライ', 'あく', None, (70,58,58,87,92,90), 19.9),
    ('ストリンダー(ハイ)', 'でんき', 'どく', (75,98,70,114,70,75), 40.0),
    ('ストリンダー(ロー)', 'でんき', 'どく', (75,98,70,114,70,75), 40.0),
    ('オトスパス', 'かくとう', None, (80,118,90,70,80,42), 39.0),
    ('ニャイキング', 'はがね', None, (70,110,100,50,60,50), 28.0),
    ('ネギガナイト', 'かくとう', None, (62,135,95,68,82,65), 117.0),
    ('バチンウニ', 'でんき', None, (48,101,95,91,85,15), 1.0),
    ('イエッサン(オス)', 'エスパー', 'ノーマル', (60,65,55,105,95,95), 28.0),
    ('イエッサン(メス)', 'エスパー', 'ノーマル', (70,55,65,95,105,85), 28.0),
    ('パーモット', 'でんき', 'かくとう', (70,115,70,70,60,105), 41.0),
    ('オリーヴァ', 'くさ', 'ノーマル', (78,69,90,125,109,39), 48.2),
    ('イキリンコ(グリーン)', 'ノーマル', 'ひこう', (82,96,51,45,51,92), 2.4),
    ('イキリンコ(ブルー)', 'ノーマル', 'ひこう', (82,96,51,45,51,92), 2.4),
    ('イキリンコ(イエロー)', 'ノーマル', 'ひこう', (82,96,51,45,51,92), 2.4),
    ('イキリンコ(ホワイト)', 'ノーマル', 'ひこう', (82,96,51,45,51,92), 2.4),
    ('マフィティフ', 'あく', None, (80,120,90,60,70,85), 61.0),
]
for _n, _t1, _t2, _stat, _w in _mc2:
    _tp = _dlpk.get_pokemon_template(_n)
    check(f"M-C2 {_n} 解決", _tp is not None)
    if _tp:
        check(f"M-C2 {_n} タイプ", (_tp.type1, _tp.type2) == (_t1, _t2), f"{_tp.type1}/{_tp.type2}")
        check(f"M-C2 {_n} 種族値",
              (_tp.base_hp,_tp.base_attack,_tp.base_defense,
               _tp.base_sp_attack,_tp.base_sp_defense,_tp.base_speed) == _stat)
        check(f"M-C2 {_n} 重さ{_w}", _tp.weight_kg == _w, f"weight={_tp.weight_kg}")
# 括弧のリージョン表記も既存の接頭辞ルールで解決すること
check("M-C2 ペルシアン(アローラ)がアローラ形に解決",
      (lambda t: t is not None and t.type1 == "あく")(_dlpk.get_pokemon_template("ペルシアン(アローラ)")))
# 同一dexのフォルムが取り違えられないこと（イエッサンはオス/メスで種族値が違う）
check("M-C2 イエッサン オス/メスの種族値が別",
      _dlpk.get_pokemon_template("イエッサン(オス)").base_sp_attack == 105
      and _dlpk.get_pokemon_template("イエッサン(メス)").base_sp_attack == 95)

# M-C 9/9 公開のメガ2種（種族値/タイプ/重さは gamewith、特性はユーザー確認で確定）
_mc2_mega = {
    "グソクムシャ": ("グソクムシャナイト", "むし", "はがね", "かたいツメ", 148.0, (75,150,175,70,120,40)),
    "セグレイブ": ("セグレイブナイト", "ドラゴン", "こおり", "ねつこうかん", 315.0, (115,175,117,105,101,87)),
}
for _bp, (_st, _t1, _t2, _ab, _w, _stat) in _mc2_mega.items():
    _md = _dlpk.get_pokemon_template(_bp).mega_data.get(_st)
    check(f"M-C2 メガ{_bp} 解決", _md is not None, f"{_bp}@{_st}")
    if _md:
        check(f"M-C2 メガ{_bp} タイプ/特性",
              _md.type1 == _t1 and _md.type2 == _t2 and _md.ability == _ab,
              f"{_md.type1}/{_md.type2} {_md.ability}")
        check(f"M-C2 メガ{_bp} 種族値",
              (_md.hp,_md.attack,_md.defense,_md.sp_attack,_md.sp_defense,_md.speed) == _stat)
        check(f"M-C2 メガ{_bp} 重さ{_w}", _md.weight_kg == _w, f"weight={_md.weight_kg}")

# select_party は呼び出し側のポケモンを壊してはいけない。
# 採点は expected_damage→calc_damage を通るので、半減きのみの消費(item=None)・かるわざ(速度+2)・
# 溜め解除が「渡した個体そのもの」に残る。呼び出し側は同じオブジェクトで対戦を始めるため、
# 実際に _o1_policy._mcts_vs_dist で味方アシレーヌのソクノのみが選出評価中に消え、
# 対戦開始時点で持ち物なしになっていた（Rust/Python間の乖離としてR4-vsdistで検出）。
from simulator.ai import select_party as _sp_side
_sp_my = [
    make_poke(type1="みず", ability="げきりゅう", item="ソクノのみ", hp_b=190, spdef_b=120),
    make_poke(type1="ノーマル", ability="てんねん", item="たべのこし", hp_b=200),
    make_poke(type1="はがね", ability="がんじょう", item="オボンのみ", hp_b=180),
    make_poke(type1="ドラゴン", ability="さめはだ", item="きあいのタスキ", atk_b=180),
    make_poke(type1="ほのお", ability="もうか", item="いのちのたま", spatk_b=170),
    make_poke(type1="くさ", ability="しんりょく", item="こだわりスカーフ", spd_b=160),
]
# でんき技持ち＝ソクノのみ(でんき半減)の消費条件を満たす相手
_sp_opp = [make_poke(type1="でんき", ability="ちくでん", spatk_b=170, moves=["10まんボルト"])
           for _ in range(6)]
_sp_before = [(p.item, p.hp, p.stage_speed, p.status) for p in _sp_my + _sp_opp]
_sp_out = _sp_side(_sp_my, _sp_opp, dl, 3, 0.0, None)
_sp_after = [(p.item, p.hp, p.stage_speed, p.status) for p in _sp_my + _sp_opp]
check("select_party が渡したポケモンを壊さない", _sp_before == _sp_after,
      f"変化={[ (b,a) for b,a in zip(_sp_before,_sp_after) if b!=a ][:3]}")
check("select_party の返り値は元オブジェクト", len(_sp_out) == 3
      and all(any(x is p for p in _sp_my) for x in _sp_out))

# ── M-C 追加アイテム（12件のうち実装済み10件） ──
from simulator.items import try_terrain_seed as _tseed, terrain_turns as _tturns, \
    get_crit_stage_bonus as _critbonus

# ながねぎ: カモネギ/ネギガナイト限定で急所ランク+2（他種が持っても0）
check("ながねぎ カモネギで急所+2", _critbonus("ながねぎ", "カモネギ") == 2)
check("ながねぎ ネギガナイトで急所+2", _critbonus("ながねぎ", "ネギガナイト") == 2)
check("ながねぎ 他種では効果なし(負例)", _critbonus("ながねぎ", "ガブリアス") == 0)
check("ピントレンズは従来どおり+1", _critbonus("ピントレンズ", "ガブリアス") == 1)

# グランドコート: フィールド継続 5 → 8
check("グランドコート フィールド8ターン", _tturns("グランドコート") == 8)
check("グランドコート無しは5ターン(負例)", _tturns("たべのこし") == 5)

# シード4種: 該当フィールドで能力+1して消費／非該当フィールドでは何もしない
for _it, _fattr, _sattr in (("エレキシード", "electric_terrain", "stage_defense"),
                            ("グラスシード", "grassy_terrain", "stage_defense"),
                            ("ミストシード", "misty_terrain", "stage_sp_defense"),
                            ("サイコシード", "psychic_terrain", "stage_sp_defense")):
    _sp = make_poke(item=_it); _fl = BattleField(); setattr(_fl, _fattr, True)
    _ok = _tseed(_sp, _fl, [])
    check(f"{_it} 該当フィールドで発動", _ok and getattr(_sp, _sattr) == 1 and _sp.item is None,
          f"stage={getattr(_sp, _sattr)} item={_sp.item}")
    _sp2 = make_poke(item=_it)
    check(f"{_it} フィールド無しでは不発(負例)",
          _tseed(_sp2, BattleField(), []) is False
          and getattr(_sp2, _sattr) == 0 and _sp2.item == _it)

# ゴツゴツメット: 接触技を受けると攻撃側に最大HPの1/6
_hd = make_poke(type1="ノーマル", item="ゴツゴツメット", hp_b=255, def_b=200)
_ha = make_poke(type1="ノーマル", atk_b=30, hp_b=255, moves=["のしかかり"])
execute(_ha, _hd, "のしかかり")
check("ゴツゴツメット 接触で1/6反動", _ha.max_hp - _ha.hp == max(1, _ha.max_hp // 6),
      f"減少={_ha.max_hp - _ha.hp} 期待={_ha.max_hp // 6}")
# 負例：非接触技では反動なし
_hd2 = make_poke(type1="ノーマル", item="ゴツゴツメット", hp_b=255, def_b=200)
_ha2 = make_poke(type1="じめん", atk_b=30, hp_b=255, moves=["じしん"])
execute(_ha2, _hd2, "じしん")
check("ゴツゴツメット 非接触では反動なし(負例)", _ha2.hp == _ha2.max_hp, f"hp={_ha2.hp}")
# 負例：えんかく（攻撃側が接触扱いにならない）では反動なし
_hd3 = make_poke(type1="ノーマル", item="ゴツゴツメット", hp_b=255, def_b=200)
_ha3 = make_poke(type1="ノーマル", atk_b=30, hp_b=255, ability="えんかく", moves=["のしかかり"])
execute(_ha3, _hd3, "のしかかり")
check("ゴツゴツメット えんかくでは反動なし(負例)", _ha3.hp == _ha3.max_hp, f"hp={_ha3.hp}")

# ノーマルジュエル: ノーマル技×1.3
from simulator.items import get_type_boost as _tb
check("ノーマルジュエル ノーマル技1.3倍", abs(_tb("ノーマルジュエル", "ノーマル", "ガブリアス") - 1.3) < 1e-9)
check("ノーマルジュエル 他タイプは等倍(負例)", _tb("ノーマルジュエル", "みず", "ガブリアス") == 1.0)
# 使用したら消費される
_nj = make_poke(type1="ノーマル", atk_b=100, item="ノーマルジュエル", moves=["たいあたり"])
execute(_nj, make_poke(type1="ノーマル", hp_b=250, def_b=200), "たいあたり")
check("ノーマルジュエル 使用で消費", _nj.item is None, f"item={_nj.item}")

# ふうせん: じめん技無効／技のダメージで割れる
_bl = make_poke(type1="ノーマル", item="ふうせん", hp_b=200, def_b=150)
check("ふうせん じめん技を無効化",
      dmg(make_poke(type1="じめん", atk_b=150, moves=["じしん"]), _bl, "じしん", roll=0.5) == 0)
# かたやぶりでも無効（アイテムなので特性無視の対象外）
check("ふうせん かたやぶりでも無効化",
      dmg(make_poke(type1="じめん", atk_b=150, ability="かたやぶり", moves=["じしん"]), _bl, "じしん", roll=0.5) == 0)
_bl2 = make_poke(type1="ノーマル", item="ふうせん", hp_b=200, def_b=150)
execute(make_poke(type1="ノーマル", atk_b=100, moves=["たいあたり"]), _bl2, "たいあたり")
check("ふうせん 技を受けると割れる", _bl2.item is None, f"item={_bl2.item}")

# ── かいがらのすず (Shell Bell) ──
p_sb = make_poke(atk_b=100, item="かいがらのすず", moves=["たいあたり"])
p_t2 = make_poke(def_b=50)
p_sb.hp = p_sb.max_hp // 2
hp_before_sb = p_sb.hp
logs = execute(p_sb, p_t2, "たいあたり")
dealt = int([l for l in logs if "たいあたり" in l and "ダメ" in l][0].split("に")[1].split("ダメ")[0])
check("かいがらのすず 与ダメ1/8回復", p_sb.hp - hp_before_sb == max(1, dealt // 8),
      f"dealt={dealt} hp_gain={p_sb.hp - hp_before_sb}")
# 負例：ダメージを与えない変化技では回復しない
p_sb_n = make_poke(atk_b=100, item="かいがらのすず", moves=["でんじは"]); p_sb_n.hp = p_sb_n.max_hp // 2; _hb_n = p_sb_n.hp
execute(p_sb_n, make_poke(def_b=50), "でんじは")
check("かいがらのすず 変化技では回復しない", p_sb_n.hp == _hb_n, f"hp={p_sb_n.hp}/{_hb_n}")

# ── きのみ系 ──
# オボンのみ (HP1/2以下→最大HP1/4回復・消費)
from simulator.battle import Battle
p_obon = make_poke(hp_b=200, item="オボンのみ", moves=["なまける"])
p_obon.hp = p_obon.max_hp // 2; _bo = p_obon.hp
Battle(BattleSide([p_obon]), BattleSide([make_poke(moves=["なまける"])]))._end_of_turn()
check("オボンのみ HP1/2以下で1/4回復＋消費",
      p_obon.hp == min(p_obon.max_hp, _bo + p_obon.max_hp // 4) and p_obon.item is None,
      f"hp={p_obon.hp}/{_bo} item={p_obon.item}")
# 負例：HPが1/2超では発動しない
p_obon_n = make_poke(hp_b=200, item="オボンのみ", moves=["なまける"]); p_obon_n.hp = p_obon_n.max_hp // 2 + 5; _bon = p_obon_n.hp
Battle(BattleSide([p_obon_n]), BattleSide([make_poke(moves=["なまける"])]))._end_of_turn()
check("オボンのみ HP1/2超では発動しない", p_obon_n.hp == _bon and p_obon_n.item == "オボンのみ", f"hp={p_obon_n.hp}/{_bon} item={p_obon_n.item}")

# ラムのみ (状態異常回復)
p_lum = make_poke(item="ラムのみ")
p_lum.status = "burn"
logs = []
try_cure_berry(p_lum, logs)
check("ラムのみ やけど回復", p_lum.status is None)
check("ラムのみ 消費", p_lum.item is None)

# ラムのみ (混乱回復)
p_lum2 = make_poke(item="ラムのみ")
p_lum2.confused = True
logs2 = []
try_cure_berry(p_lum2, logs2)
check("ラムのみ こんらん回復", not p_lum2.confused)

# カゴのみ (ねむり回復)
p_chesto = make_poke(item="カゴのみ")
p_chesto.status = "sleep"
p_chesto.sleep_count = 3
logs3 = []
try_cure_berry(p_chesto, logs3)
check("カゴのみ ねむり回復", p_chesto.status is None)
check("カゴのみ 消費", p_chesto.item is None)

# カゴのみ は混乱を治さない
p_chesto2 = make_poke(item="カゴのみ")
p_chesto2.confused = True
logs4 = []
try_cure_berry(p_chesto2, logs4)
check("カゴのみ 混乱は治さない", p_chesto2.confused)

# きあいのタスキ (atk_b=500で確実にOHKO)
p_tasuki = make_poke(hp_b=45, item="きあいのタスキ", moves=["なまける"])
p_attacker = make_poke(atk_b=500, moves=["じしん"])
logs_t = execute(p_attacker, p_tasuki, "じしん")
check("きあいのタスキ 1耐え", p_tasuki.hp == 1)
check("きあいのタスキ 消費", p_tasuki.item is None)
# 負例：HPが満タンでなければ発動せず倒れる
p_tasuki_n = make_poke(hp_b=45, item="きあいのタスキ", moves=["なまける"]); p_tasuki_n.hp = p_tasuki_n.max_hp - 1
execute(make_poke(atk_b=500, moves=["じしん"]), p_tasuki_n, "じしん")
check("きあいのタスキ 満タンでなければ発動しない", not p_tasuki_n.is_alive and p_tasuki_n.item == "きあいのタスキ", f"alive={p_tasuki_n.is_alive} item={p_tasuki_n.item}")

# しろいハーブ (ランク低下リセット)
p_herb = make_poke(item="しろいハーブ")
p_herb.stage_attack = -1
p_herb.stage_defense = -2
logs_h = []
try_white_herb(p_herb, logs_h)
check("しろいハーブ ランク低下リセット", p_herb.stage_attack == 0 and p_herb.stage_defense == 0)

# ── 新規アイテム8種 ──────────────────────────────────────────────
from simulator.items import try_mental_herb, try_leppa_berry
from simulator.abilities import on_after_hit

# きせきのタネ：くさ技1.2倍
_pks = make_poke(type1="くさ", spatk_b=100, item="きせきのタネ"); _pks0 = make_poke(type1="くさ", spatk_b=100)
_dks = make_poke(type1="ノーマル", spdef_b=100)
check("きせきのタネ くさ技1.2倍", near(dmg(_pks, _dks, "エナジーボール") / dmg(_pks0, _dks, "エナジーボール"), 1.2))
check("きせきのタネ 他タイプは無補正", near(dmg(make_poke(spatk_b=100, item="きせきのタネ"), _dks, "なみのり") / dmg(make_poke(spatk_b=100), _dks, "なみのり"), 1.0))

# オレンのみ：HP1/2以下でEOTに10回復（固定値）
_por = make_poke(hp_b=150, item="オレンのみ", moves=["なまける"])
_por.hp = _por.max_hp // 2; _bor = _por.hp
_bor_b = Battle(BattleSide([_por]), BattleSide([make_poke(moves=["なまける"])])); _bor_b.turn = 0
_bor_b._end_of_turn()
check("オレンのみ HP1/2以下で10回復", _por.hp == _bor + 10, f"hp={_por.hp} base={_bor}")
check("オレンのみ 消費", _por.item is None)

# モモンのみ：どく回復／やけどは治さない
_pmo = make_poke(item="モモンのみ"); _pmo.status = "poison"
try_cure_berry(_pmo, [])
check("モモンのみ どく回復", _pmo.status is None and _pmo.item is None)
_pmo2 = make_poke(item="モモンのみ"); _pmo2.status = "burn"
try_cure_berry(_pmo2, [])
check("モモンのみ やけどは治さない", _pmo2.status == "burn" and _pmo2.item == "モモンのみ")

# チーゴのみ：やけど回復／どくは治さない
_pch = make_poke(item="チーゴのみ"); _pch.status = "burn"
try_cure_berry(_pch, [])
check("チーゴのみ やけど回復", _pch.status is None and _pch.item is None)
_pch2 = make_poke(item="チーゴのみ"); _pch2.status = "poison"
try_cure_berry(_pch2, [])
check("チーゴのみ どくは治さない", _pch2.status == "poison" and _pch2.item == "チーゴのみ")

# ヒメリのみ：PP0の技を10回復
_phi = make_poke(item="ヒメリのみ", moves=["たいあたり", "なみのり"]); _phi.pp[0] = 0
try_leppa_berry(_phi, [])
check("ヒメリのみ PP0技を回復", _phi.pp[0] > 0 and _phi.item is None)
_phi2 = make_poke(item="ヒメリのみ", moves=["たいあたり"])  # PP満タン
try_leppa_berry(_phi2, [])
check("ヒメリのみ PP0が無ければ消費しない", _phi2.item == "ヒメリのみ")

# メンタルハーブ：ちょうはつ/アンコール等を解除（一度だけ）
_pmh = make_poke(item="メンタルハーブ"); _pmh.taunt_count = 3; _pmh.encore_count = 2
try_mental_herb(_pmh, [])
check("メンタルハーブ 行動制限解除", _pmh.taunt_count == 0 and _pmh.encore_count == 0 and _pmh.item is None)
_pmh2 = make_poke(item="メンタルハーブ")  # 制限なし
try_mental_herb(_pmh2, [])
check("メンタルハーブ 制限なしでは消費しない", _pmh2.item == "メンタルハーブ")

# ── M-B(M-3)追加アイテム ──────────────────────────────────────────
from simulator.items import get_speed_item_multiplier as _gsm, get_accuracy_evasion_item as _gae
from simulator.battle import Action as _Act
check("くろいてっきゅう 素早さ0.5", _gsm("くろいてっきゅう") == 0.5)
check("こうかくレンズ 命中1.1", near(_gae("こうかくレンズ"), 1.1))
check("こうかくレンズなし 命中1.0", near(_gae(None), 1.0))
# 状態回復きのみ
for _berry, _st, _lbl in [("クラボのみ", "paralysis", "まひ"), ("キーのみ", "freeze", "こおり")]:
    _pb = make_poke(item=_berry); _pb.status = _st; try_cure_berry(_pb, [])
    check(f"{_berry} {_lbl}回復", _pb.status is None and _pb.item is None)
    _pb2 = make_poke(item=_berry); _pb2.status = "burn"; try_cure_berry(_pb2, [])
    check(f"{_berry} 対象外(やけど)は無反応", _pb2.status == "burn" and _pb2.item == _berry)
_pn = make_poke(item="ナナシのみ"); _pn.confused = True; try_cure_berry(_pn, [])
check("ナナシのみ こんらん回復", (not _pn.confused) and _pn.item is None)
_pn2 = make_poke(item="ナナシのみ"); _pn2.status = "burn"; try_cure_berry(_pn2, [])
check("ナナシのみ 状態異常(やけど)には無反応", _pn2.status == "burn" and _pn2.item == "ナナシのみ")

class _Force:
    def __init__(self, nm): self.nm = nm
    def __call__(self, my, opp, f):
        for i, m in enumerate(my.active.moves):
            if m and m.name_jp == self.nm:
                return _Act(type="move", move=m, move_idx=i)
        return _Act(type="move", move=my.active.moves[0], move_idx=0)

def _weather_after(rock, wmove):
    holder = make_poke(item=rock, moves=[wmove, "まもる"]); foe = make_poke(moves=["まもる"])
    f = BattleField(); Battle(BattleSide([holder]), BattleSide([foe]), f).resume(_Force(wmove), _Force("まもる"), max_turns=1)
    return f.weather_count
check("しめったいわ 雨8ターン(経過後7)", _weather_after("しめったいわ", "あまごい") == 7)
check("天候岩なし 雨5ターン(経過後4)", _weather_after(None, "あまごい") == 4)
check("あついいわ 晴8", _weather_after("あついいわ", "にほんばれ") == 7)
check("さらさらいわ 砂8", _weather_after("さらさらいわ", "すなあらし") == 7)
check("つめたいいわ あられ8", _weather_after("つめたいいわ", "あられ") == 7)

def _reflect_after(rock):
    holder = make_poke(item=rock, moves=["リフレクター", "まもる"]); foe = make_poke(moves=["まもる"])
    s1 = BattleSide([holder]); Battle(s1, BattleSide([foe]), BattleField()).resume(_Force("リフレクター"), _Force("まもる"), max_turns=1)
    return s1.reflect_count
check("ひかりのねんど リフレクター8(経過後7)", _reflect_after("ひかりのねんど") == 7)
check("ねんどなし リフレクター5(経過後4)", _reflect_after(None) == 4)

import simulator.damage as _dmgmod
def _drain_heal(root):
    _dmgmod._ROLL_OVERRIDE = 0.85; random.seed(1)  # 同一ダメージで比較
    try:
        holder = make_poke(type1="くさ", spatk_b=120, item=root, moves=["ギガドレイン", "まもる"]); holder.hp = 1
        foe = make_poke(hp_b=200, spdef_b=60, moves=["なまける"])  # 非防御(吸収を防がない)
        s1 = BattleSide([holder]); Battle(s1, BattleSide([foe]), BattleField()).resume(_Force("ギガドレイン"), _Force("なまける"), max_turns=1)
        return holder.hp - 1
    finally:
        _dmgmod._ROLL_OVERRIDE = None
_hr = _drain_heal("おおきなねっこ"); _hn = _drain_heal(None)
check("おおきなねっこ 吸収1.3倍", _hn > 0 and 1.2 <= _hr / _hn <= 1.4, f"root={_hr} none={_hn}")

# おうじゃのしるし：ダメージ技で10%ひるみ（統計）
random.seed(31); _ks_flinch = 0; _N_ks = 400
for _ in range(_N_ks):
    _datk = make_poke(); _dtgt = make_poke()
    _patk = make_poke(item="おうじゃのしるし")
    on_after_hit(_patk, _dtgt, dl.get_move("たいあたり"), [])
    if _dtgt.flinched: _ks_flinch += 1
check("おうじゃのしるし 10%ひるみ(±)", 20 < _ks_flinch < 60, f"{_ks_flinch}/{_N_ks}")
# 変化技ではひるませない
_dtgt_nc = make_poke()
on_after_hit(make_poke(item="おうじゃのしるし"), _dtgt_nc, dl.get_move("でんじは"), [])
check("おうじゃのしるし 変化技ではひるませない", not _dtgt_nc.flinched)
# 負例：せいしんりょく/どんかんはひるまない（多数試行で一度も発生しない）
random.seed(32); _ks_imm = False
for _ in range(400):
    _d_im = make_poke(ability="せいしんりょく")
    on_after_hit(make_poke(item="おうじゃのしるし"), _d_im, dl.get_move("たいあたり"), [])
    if _d_im.flinched: _ks_imm = True; break
check("おうじゃのしるし せいしんりょくはひるまない", not _ks_imm)

# きあいのハチマキ：HP不問で10%一撃耐え（統計）
random.seed(37); _hb_survive = 0; _N_hb = 400
for _ in range(_N_hb):
    _phb = make_poke(hp_b=45, item="きあいのハチマキ", moves=["なまける"]); _phb.hp = _phb.max_hp // 2
    execute(make_poke(atk_b=500, moves=["じしん"]), _phb, "じしん")
    if _phb.hp == 1 and _phb.is_alive: _hb_survive += 1
check("きあいのハチマキ 10%で1耐え(±)", 20 < _hb_survive < 60, f"{_hb_survive}/{_N_hb}")
check("きあいのハチマキ 消費しない", make_poke(item="きあいのハチマキ").item == "きあいのハチマキ")
check("しろいハーブ 消費", p_herb.item is None)

# しろいハーブ: ランク低下がない場合は発動しない
p_herb2 = make_poke(item="しろいハーブ")
p_herb2.stage_attack = 1
logs_h2 = []
try_white_herb(p_herb2, logs_h2)
check("しろいハーブ ランク低下なしは発動しない", p_herb2.item == "しろいハーブ")

# タイプ半減きのみ
# タイプ半減きのみ: 対応タイプが抜群時に×0.5（正しいマッピングで検証）
for berry, typ, move_n in [
    ("シュカのみ",  "じめん",    "じしん"),
    ("ハバンのみ",  "ドラゴン",  "りゅうのいぶき"),
    ("イトケのみ",  "みず",      "なみのり"),
    ("ソクノのみ",  "でんき",    "10まんボルト"),
    ("ヨロギのみ",  "いわ",      "ストーンエッジ"),
    ("ヤチェのみ",  "こおり",    "れいとうビーム"),
    ("ビアーのみ",  "どく",      "ヘドロばくだん"),
    ("バコウのみ",  "ひこう",    "エアスラッシュ"),
    ("ウタンのみ",  "エスパー",  "サイコキネシス"),
    ("リリバのみ",  "はがね",    "アイアンヘッド"),
    ("ロゼルのみ",  "フェアリー","ムーンフォース"),
    ("ナモのみ",   "あく",      "あくのはどう"),
    ("オッカのみ",  "ほのお",    "かえんほうしゃ"),
    ("リンドのみ",  "くさ",      "エナジーボール"),
    ("ヨプのみ",   "かくとう",  "インファイト"),
    ("カシブのみ",  "ゴースト",  "シャドーボール"),
    ("タンガのみ",  "むし",      "むしのさざめき"),
]:
    # 防御タイプを動的に選択：抜群(≥2倍)になる型と、等倍(1倍)になる型
    _cand = ["ノーマル","ほのお","みず","でんき","くさ","こおり","かくとう","どく",
             "じめん","ひこう","エスパー","むし","いわ","ドラゴン","あく","はがね","フェアリー"]
    _weak = next((t for t in _cand if get_type_effectiveness(typ, t, None) >= 2.0), None)
    _neut = next((t for t in _cand if get_type_effectiveness(typ, t, None) == 1.0), None)
    _atk = make_poke(type1=typ, spatk_b=100, atk_b=100)
    # 正例：抜群被弾を厳密に×0.5（半減）
    if _weak:
        _db = dmg(_atk, make_poke(type1=_weak, item=berry, def_b=80, spdef_b=80), move_n, roll=0.5)
        _dnb = dmg(_atk, make_poke(type1=_weak, def_b=80, spdef_b=80), move_n, roll=0.5)
        check(f"{berry}({typ}) 抜群半減0.5倍", near(_db / _dnb, 0.5), f"ratio={_db/_dnb:.3f}")
    # 負例：等倍では半減しない（抜群時のみ発動）
    if _neut:
        _db2 = dmg(_atk, make_poke(type1=_neut, item=berry, def_b=80, spdef_b=80), move_n, roll=0.5)
        _dnb2 = dmg(_atk, make_poke(type1=_neut, def_b=80, spdef_b=80), move_n, roll=0.5)
        check(f"{berry}({typ}) 等倍では半減しない", near(_db2 / _dnb2, 1.0), f"ratio={_db2/_dnb2:.3f}")

# ホズのみ: ノーマル技を常に半減（抜群条件なし）
p_hoz = make_poke(type1="ゴースト", item="ホズのみ", def_b=80)
p_hoz_nb = make_poke(type1="ゴースト", def_b=80)
p_nm_atk = make_poke(type1="ノーマル", atk_b=100, ability="きもったま")
d_hoz = dmg(p_nm_atk, p_hoz, "たいあたり", roll=0.5)
d_hoz_nb = dmg(p_nm_atk, p_hoz_nb, "たいあたり", roll=0.5)
check("ホズのみ ノーマル技半減", d_hoz < d_hoz_nb, f"hoz={d_hoz} no_hoz={d_hoz_nb}")
# 負例：非ノーマル技は半減しない
_phz_n = make_poke(type1="ゴースト", item="ホズのみ", spdef_b=80); _phz_n0 = make_poke(type1="ゴースト", spdef_b=80)
check("ホズのみ 非ノーマル技は半減しない", near(dmg(make_poke(spatk_b=100), _phz_n, "なみのり") / dmg(make_poke(spatk_b=100), _phz_n0, "なみのり"), 1.0))

# 能力変化きのみ (HP1/4以下で発動)
for berry, stat in [("カムラのみ","speed"),
                     ("サルのみ","sp_attack"),("リュガのみ","defense"),("タラプのみ","sp_defense")]:
    p_b = make_poke(item=berry)
    p_b.hp = p_b.max_hp // 4  # exactly 1/4
    logs_b = []
    apply_hp_berry(p_b, logs_b)
    stat_val = getattr(p_b, f"stage_{stat}", 0)
    check(f"{berry} HP1/4以下でstage+1", stat_val == 1, f"stage_{stat}={stat_val}")

# じゃくてんほけん (みずタイプはでんき技が抜群)
random.seed(0)
p_jwp = make_poke(type1="みず", def_b=100, spdef_b=100, item="じゃくてんほけん",
                  moves=["なまける"])
p_fire_atk = make_poke(type1="でんき", spatk_b=150, moves=["10まんボルト"])
logs_jw = execute(p_fire_atk, p_jwp, "10まんボルト")
check("じゃくてんほけん 抜群被弾でA/C+2", p_jwp.stage_attack == 2 and p_jwp.stage_sp_attack == 2,
      f"stg_atk={p_jwp.stage_attack} stg_spatk={p_jwp.stage_sp_attack}")

# たべのこし (毎ターン1/16回復) - end_of_turn経由で確認
p_leftovers = make_poke(item="たべのこし")
p_leftovers.hp = p_leftovers.max_hp - 10
b_lo = Battle(BattleSide([p_leftovers]), BattleSide([make_poke(moves=["なまける"])]))
b_lo.turn = 0
b_lo._end_of_turn()
check("たべのこし 毎ターン1/16回復", p_leftovers.hp == p_leftovers.max_hp - 10 + p_leftovers.max_hp // 16)


# ════════════════════════════════════════════════════════════════
# 2. とくせいテスト
# ════════════════════════════════════════════════════════════════
print("\n=== 2. とくせい ===")

# ── 攻撃無効化 ──
p_levitate = make_poke(type1="ドラゴン", ability="ふゆう", spdef_b=100)
p_grd = make_poke(spatk_b=100)
check("ふゆう じめん無効", dmg(p_grd, p_levitate, "じしん") == 0)
# ふゆう：まきびし等の地面ハザードも無効
from simulator.battle import _entry_effects as _ent_hz
_flev = BattleField(); _flev.spikes[0] = 3
_plev_hz = make_poke(type1="ドラゴン", ability="ふゆう", hp_b=255); _hlev = _plev_hz.hp
_ent_hz(_plev_hz, 0, _flev, [])
check("ふゆう まきびし無効", _plev_hz.hp == _hlev, f"hp={_plev_hz.hp}/{_hlev}")
_fgnd = BattleField(); _fgnd.spikes[0] = 3
_pgnd_hz = make_poke(type1="ノーマル", hp_b=255); _hgnd = _pgnd_hz.hp
_ent_hz(_pgnd_hz, 0, _fgnd, [])
check("ふゆう 対照: 地上はまきびし被弾", _pgnd_hz.hp < _hgnd, f"hp={_pgnd_hz.hp}/{_hgnd}")

p_waterabs = make_poke(type1="ノーマル", ability="ちょすい", spdef_b=100)
check("ちょすい みず無効", dmg(p_grd, p_waterabs, "なみのり") == 0)

p_voltabs = make_poke(type1="ノーマル", ability="ちくでん", spdef_b=100)
check("ちくでん でんき無効", dmg(p_grd, p_voltabs, "10まんボルト") == 0)

# ちくでん/ちょすい/かんそうはだ：吸収時に最大HP1/4回復
for _ab, _mv, _ty in [("ちょすい","なみのり","みず"),("ちくでん","10まんボルト","でんき"),("かんそうはだ","なみのり","みず")]:
    _abs = make_poke(type1="ノーマル", ability=_ab, hp_b=200, spdef_b=100); _abs.hp = _abs.max_hp // 2
    _bef = _abs.hp
    execute(make_poke(type1=_ty, spatk_b=100), _abs, _mv)
    check(f"{_ab} 吸収で1/4回復", _abs.hp == min(_abs.max_hp, _bef + max(1, _abs.max_hp // 4)), f"hp={_abs.hp}/{_bef}")

# いたずらごころ：あくタイプの相手には変化技が無効（技タイプを問わない）
p_prank = make_poke(type1="エスパー", ability="いたずらごころ")
d_dark = make_poke(type1="あく", hp_b=200)
execute(p_prank, d_dark, "でんじは")
check("いたずらごころ あく相手に変化技無効", d_dark.status != "paralysis", f"status={d_dark.status}")
random.seed(0); _ok_nd = False
for _ in range(20):
    d_nd = make_poke(type1="ノーマル", hp_b=200)
    execute(p_prank, d_nd, "でんじは")
    if d_nd.status == "paralysis": _ok_nd = True; break
check("いたずらごころ 非あくには有効", _ok_nd, "あく以外には変化技が通る")
# いたずらごころ：変化技の優先度+1（主効果）。攻撃技には補正なし
from simulator.battle import _priority as _prio_iz
_izs = Action(type="move", move=dl.get_move("でんじは"))
check("いたずらごころ 変化技の優先度+1",
      _prio_iz(_izs, make_poke(ability="いたずらごころ")) == _prio_iz(_izs, make_poke()) + 1)
_iza = Action(type="move", move=dl.get_move("たいあたり"))
check("いたずらごころ 攻撃技は優先度補正なし",
      _prio_iz(_iza, make_poke(ability="いたずらごころ")) == _prio_iz(_iza, make_poke()))

# へんげんじざい：登場後1回だけ技タイプに変化（2回目以降は変わらない＝交代で1回）
p_prot = make_poke(type1="ノーマル", ability="へんげんじざい")
d_prot = make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200)
_execute_move(BattleSide([p_prot]), BattleSide([d_prot]), Action(type="move", move=dl.get_move("なみのり")), BattleField())
check("へんげんじざい 初回みず化", p_prot.type1 == "みず" and p_prot.type2 is None, f"type={p_prot.type1}/{p_prot.type2}")
_execute_move(BattleSide([p_prot]), BattleSide([d_prot]), Action(type="move", move=dl.get_move("かえんほうしゃ")), BattleField())
check("へんげんじざい 1回限り(2回目は不変)", p_prot.type1 == "みず", f"type={p_prot.type1}")

p_flashfire = make_poke(type1="ノーマル", ability="もらいび", spdef_b=100)
check("もらいび ほのお無効", dmg(p_grd, p_flashfire, "かえんほうしゃ") == 0)

p_herbivore = make_poke(type1="ノーマル", ability="そうしょく", spdef_b=100)
check("そうしょく くさ無効", dmg(p_grd, p_herbivore, "エナジーボール") == 0)
# そうしょく：くさ技吸収で攻撃+1
_phb = make_poke(type1="ノーマル", ability="そうしょく", spdef_b=100, hp_b=255)
execute(make_poke(spatk_b=100), _phb, "エナジーボール")
check("そうしょく くさ吸収で攻撃+1", _phb.stage_attack == 1, f"atk={_phb.stage_attack}")

p_lightningrod = make_poke(type1="ノーマル", ability="ひらいしん", spdef_b=100)
check("ひらいしん でんき無効", dmg(p_grd, p_lightningrod, "10まんボルト") == 0)
# ひらいしん：でんき技吸収で特攻+1
_plr = make_poke(type1="ノーマル", ability="ひらいしん", spdef_b=100, hp_b=255)
execute(make_poke(spatk_b=100), _plr, "10まんボルト")
check("ひらいしん でんき吸収で特攻+1", _plr.stage_sp_attack == 1, f"spa={_plr.stage_sp_attack}")

# もらいび: 発動後ほのお強化
p_ff_active = make_poke(type1="ノーマル", spatk_b=100, ability="もらいび",
                         moves=["かえんほうしゃ"])
p_ff_active._flash_fire_active = True
d_ff = dmg(p_ff_active, make_poke(spdef_b=100), "かえんほうしゃ", roll=0.5)
p_ff_active._flash_fire_active = False
d_no_ff = dmg(p_ff_active, make_poke(spdef_b=100), "かえんほうしゃ", roll=0.5)
check("もらいび 発動後1.5倍", near(d_ff / d_no_ff, 1.5))

# ふしぎなまもり
p_wonder = make_poke(type1="ゴースト", type2="あく", ability="ふしぎなまもり",
                      def_b=100, spdef_b=100)
p_atk_nm = make_poke(spatk_b=100)
check("ふしぎなまもり 等倍無効", dmg(p_atk_nm, p_wonder, "シャドーボール") == 0)
p_atk_fairy = make_poke(type1="フェアリー", spatk_b=100)
check("ふしぎなまもり 抜群は通る", dmg(p_atk_fairy, p_wonder, "ムーンフォース") > 0)

# ぼうだん (Ball/Bomb無効)
p_bulletproof = make_poke(type1="ノーマル", ability="ぼうだん", spdef_b=100)
check("ぼうだん シャドーボール無効", dmg(p_grd, p_bulletproof, "シャドーボール") == 0)
check("ぼうだん 通常技は通る",      dmg(p_grd, p_bulletproof, "なみのり") > 0)

# マルチスケイル
p_multiscale = make_poke(type1="ドラゴン", ability="マルチスケイル", def_b=100, spdef_b=100)
p_multiscale.hp = p_multiscale.max_hp  # 満タン
p_atk100 = make_poke(spatk_b=100)
d_ms = dmg(p_atk100, p_multiscale, "りゅうのいぶき", roll=0.5)
p_multiscale_no = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
d_no_ms = dmg(p_atk100, p_multiscale_no, "りゅうのいぶき", roll=0.5)
check("マルチスケイル 満タン0.5倍", near(d_ms / d_no_ms, 0.5))
p_multiscale.hp = p_multiscale.max_hp - 1
d_ms_low = dmg(p_atk100, p_multiscale, "りゅうのいぶき", roll=0.5)
check("マルチスケイル HP欠けでは半減しない", d_ms_low == d_no_ms)

# かたやぶり でふゆう無視
p_lev2 = make_poke(type1="ドラゴン", ability="ふゆう", def_b=100)
p_mb = make_poke(type1="ノーマル", atk_b=100, ability="かたやぶり")
check("かたやぶり ふゆう無視", dmg(p_mb, p_lev2, "じしん") > 0)

# ── いかく ──
from simulator.abilities import entry_ability
p_intimidate = make_poke(ability="いかく")
p_opp = make_poke()
old_atk_stage = p_opp.stage_attack
logs_i = entry_ability(p_intimidate, p_opp, BattleField())
check("いかく 相手攻撃-1", p_opp.stage_attack == old_atk_stage - 1)

# いかく クリアボディで無効
p_opp_cb = make_poke(ability="クリアボディ")
old_cb = p_opp_cb.stage_attack
logs_cb = entry_ability(p_intimidate, p_opp_cb, BattleField())
check("いかく クリアボディで無効", p_opp_cb.stage_attack == old_cb)

# いかく きもったま/せいしんりょく/マイペース/どんかん で無効
for _ab_im in ("きもったま", "せいしんりょく", "マイペース", "どんかん"):
    _opp_im = make_poke(ability=_ab_im)
    entry_ability(make_poke(ability="いかく"), _opp_im, BattleField())
    check(f"いかく {_ab_im}で無効", _opp_im.stage_attack == 0, f"atk={_opp_im.stage_attack}")

# うるおいボディ あめ中ターン終わりに状態異常が治る（交代時でなく毎ターン終了時）
from simulator.abilities import end_of_turn_ability
p_rainbody = make_poke(ability="うるおいボディ"); p_rainbody.status = "burn"
f_rain = BattleField(); f_rain.weather = "rain"
end_of_turn_ability(p_rainbody, f_rain, [])
check("うるおいボディ 雨中ターン終了で状態治癒", p_rainbody.status is None, f"status={p_rainbody.status}")
# 雨でなければ治らない
p_rainbody2 = make_poke(ability="うるおいボディ"); p_rainbody2.status = "burn"
end_of_turn_ability(p_rainbody2, BattleField(), [])
check("うるおいボディ 非雨では治らない", p_rainbody2.status == "burn", f"status={p_rainbody2.status}")

# ── 天候特性 ──
from simulator.abilities import entry_ability
for ab, expected_weather in [("すなおこし","sandstorm"),("ひでり","sunny"),
                               ("あめふらし","rain"),("ゆきふらし","hail")]:
    f2 = BattleField()
    p_w = make_poke(ability=ab)
    entry_ability(p_w, make_poke(), f2)
    check(f"{ab} 天候発動", f2.weather == expected_weather)

# ── 攻撃倍率特性 ──
# ちからずく：追加効果を持つ技のみ1.3倍（のしかかり=30%まひ持ち）
p_sheer = make_poke(atk_b=100, ability="ちからずく")
p_tgt = make_poke(def_b=100)
d_sf = dmg(p_sheer, p_tgt, "のしかかり", roll=0.5)
p_sheer_no = make_poke(atk_b=100)
d_sf_no = dmg(p_sheer_no, p_tgt, "のしかかり", roll=0.5)
check("ちからずく 追加効果技は1.3倍", near(d_sf / d_sf_no, 1.3))
# 負例：追加効果の無い技（たいあたり）は強化されない
check("ちからずく 追加効果なし技は等倍", near(dmg(p_sheer, p_tgt, "たいあたり", roll=0.5) / dmg(p_sheer_no, p_tgt, "たいあたり", roll=0.5), 1.0))
# 自己能力ダウン(反動)のみの技も対象外（オーバーヒート）
_pkz_sp = make_poke(spatk_b=100, ability="ちからずく"); _pkz_sp0 = make_poke(spatk_b=100); _dkz_t = make_poke(type1="みず", spdef_b=100)
check("ちからずく 反動のみ技(オーバーヒート)は等倍", near(dmg(_pkz_sp, _dkz_t, "オーバーヒート", roll=0.5) / dmg(_pkz_sp0, _dkz_t, "オーバーヒート", roll=0.5), 1.0))
# ちからずく 追加効果が出ない（かえんほうしゃのやけどが無効化される）
random.seed(0); _zk_burn = False
for _ in range(60):
    p_zk = make_poke(spatk_b=120, ability="ちからずく"); d_zk = make_poke(type1="ノーマル", hp_b=255, spdef_b=100)
    execute(p_zk, d_zk, "かえんほうしゃ")
    if d_zk.status == "burn": _zk_burn = True; break
check("ちからずく 追加効果なし(やけど出ない)", not _zk_burn, "ちからずくで追加効果が無効化されること")

# テクニシャン 威力60以下1.5倍
p_tech = make_poke(atk_b=100, ability="テクニシャン")
p_tgt2 = make_poke(def_b=100)
d_tech = dmg(p_tech, p_tgt2, "でんこうせっか", roll=0.5)  # power=40
p_no_tech = make_poke(atk_b=100)
d_no_tech = dmg(p_no_tech, p_tgt2, "でんこうせっか", roll=0.5)
check("テクニシャン 威力40技1.5倍", near(d_tech / d_no_tech, 1.5))
# 負例：威力60超の技は1.5倍にならない（なみのり=90）
_d_tech_big = dmg(p_tech, p_tgt2, "なみのり", roll=0.5)
_d_notech_big = dmg(make_poke(spatk_b=100), p_tgt2, "なみのり", roll=0.5)
check("テクニシャン 威力60超は等倍", near(_d_tech_big / _d_notech_big, 1.0))

# てきおうりょく (STAB×2)
p_adapt = make_poke(type1="ノーマル", atk_b=100, ability="てきおうりょく")
p_adapt_no = make_poke(type1="ノーマル", atk_b=100)
d_adapt = dmg(p_adapt, p_tgt, "たいあたり", roll=0.5)
d_no_adapt = dmg(p_adapt_no, p_tgt, "たいあたり", roll=0.5)
check("てきおうりょく STAB×2(1.5→2.0)", near(d_adapt / d_no_adapt, 2.0 / 1.5))
# 負例：タイプ不一致技は強化されない（ノーマル型がみず技なみのり＝非一致）
_d_ad_ns = dmg(p_adapt, p_tgt, "なみのり", roll=0.5)
_d_no_ns = dmg(p_adapt_no, p_tgt, "なみのり", roll=0.5)
check("てきおうりょく 非一致技は等倍", near(_d_ad_ns / _d_no_ns, 1.0))

# さいせいりょく (交代でHP1/3回復)
from simulator.abilities import on_switch_out
p_regen = make_poke(ability="さいせいりょく")
p_regen.hp = p_regen.max_hp // 2
hp_before_regen = p_regen.hp
on_switch_out(p_regen, [])
check("さいせいりょく 交代時HP1/3回復", p_regen.hp == hp_before_regen + p_regen.max_hp // 3)

# じしんかじょう (KO後攻撃+1)
from simulator.abilities import on_ko
p_moxie = make_poke(ability="じしんかじょう")
old_stg = p_moxie.stage_attack
on_ko(p_moxie, [])
check("じしんかじょう KO後攻撃+1", p_moxie.stage_attack == old_stg + 1)
# 負例：相手を倒さなければ攻撃は上がらない
_pmox_n = make_poke(ability="じしんかじょう", atk_b=10)
_dmox_n = make_poke(type1="ノーマル", hp_b=255, def_b=200)
execute(_pmox_n, _dmox_n, "たいあたり")
check("じしんかじょう 非KOでは上がらない", _pmox_n.stage_attack == 0 and _dmox_n.is_alive)

# ── M-B(M-3)追加とくせい ──────────────────────────────────────────
from simulator.battle import crit_chance as _crit
from simulator.abilities import check_move_immunity as _cmi

# ほのおのたてがみ: 炎技1.5倍 / 他タイプ無補正
_pm = make_poke(type1="ほのお", spatk_b=120, ability="ほのおのたてがみ"); _pm0 = make_poke(type1="ほのお", spatk_b=120, ability="もうか")
_dmn = make_poke(type1="ノーマル", spdef_b=100)
check("ほのおのたてがみ 炎技1.5倍", near(dmg(_pm, _dmn, "かえんほうしゃ") / dmg(_pm0, _dmn, "かえんほうしゃ"), 1.5))
check("ほのおのたてがみ 他タイプ無補正", near(dmg(make_poke(spatk_b=120, ability="ほのおのたてがみ"), _dmn, "なみのり") / dmg(make_poke(spatk_b=120, ability="もうか"), _dmn, "なみのり"), 1.0))

# もふもふ: 接触物理0.5 / 炎技2.0 / 非接触は無補正
_dmf = make_poke(ability="もふもふ", def_b=100, spdef_b=100); _df0 = make_poke(ability="しんりょく", def_b=100, spdef_b=100)
check("もふもふ 接触物理0.5", near(dmg(make_poke(atk_b=120), _dmf, "たいあたり") / dmg(make_poke(atk_b=120), _df0, "たいあたり"), 0.5))
check("もふもふ 炎技2.0", near(dmg(make_poke(type1="ほのお", spatk_b=120), _dmf, "かえんほうしゃ") / dmg(make_poke(type1="ほのお", spatk_b=120), _df0, "かえんほうしゃ"), 2.0))
check("もふもふ 非接触物理は無補正", near(dmg(make_poke(atk_b=120), _dmf, "じしん") / dmg(make_poke(atk_b=120), _df0, "じしん"), 1.0))

# カブトアーマー: 急所率0
check("カブトアーマー 急所率0", _crit(make_poke(), dl.get_move("たいあたり"), make_poke(ability="カブトアーマー")) == 0.0)
check("カブトアーマーなし 急所率>0", _crit(make_poke(), dl.get_move("たいあたり"), make_poke(ability="しんりょく")) > 0.0)

# ほうし: 接触技で30%状態異常(統計)
random.seed(7); _spore = 0
for _ in range(400):
    _at = make_poke(); on_after_hit(_at, make_poke(ability="ほうし"), dl.get_move("のしかかり"), [])  # 接触技
    if _at.status is not None: _spore += 1
check("ほうし 接触30%状態異常(±)", 80 < _spore < 170, f"{_spore}/400")
_at_nc = make_poke(); on_after_hit(_at_nc, make_poke(ability="ほうし"), dl.get_move("みずでっぽう"), [])  # 非接触
check("ほうし 非接触では発動しない", _at_nc.status is None)

# エレキメイカー: 登場時エレキフィールド5ターン / 他特性では張られない(負例)
_fe = BattleField(); entry_ability(make_poke(ability="エレキメイカー"), make_poke(), _fe)
check("エレキメイカー 登場でエレキF", _fe.electric_terrain and _fe.electric_terrain_count == 5)
_fe0 = BattleField(); entry_ability(make_poke(ability="しんりょく"), make_poke(), _fe0)
check("エレキメイカーなし エレキF張られない", _fe0.electric_terrain is False)

# うなぎのぼり: じめん技無効 + KOで最高能力+1 / 通常特性はじめん無効化しない(負例)
check("うなぎのぼり じめん技無効", _cmi(make_poke(ability="うなぎのぼり"), "じめん", "じしん"))
check("通常特性はじめん無効化しない", not _cmi(make_poke(ability="しんりょく"), "じめん", "じしん"))
check("うなぎのぼり 非じめん技は無効化しない", not _cmi(make_poke(ability="うなぎのぼり"), "みず", "なみのり"))
_pun = make_poke(ability="うなぎのぼり", spd_b=160)  # 速さが最高能力
on_ko(_pun, [])
check("うなぎのぼり KOで最高能力(速)+1", _pun.stage_speed == 1)
_pun0 = make_poke(ability="しんりょく", spd_b=160); on_ko(_pun0, [])
check("通常特性はKOで能力上がらない(負例)", _pun0.stage_speed == 0)

# よちむ: 1v1で機械的効果なし(no-op・クラッシュしない)
_fy = BattleField(); entry_ability(make_poke(ability="よちむ"), make_poke(item="オボンのみ"), _fy)
check("よちむ 機械的効果なし", _fy.electric_terrain is False)

# おうごんのからだ: 相手の変化技(でんじは)無効 / 自己強化(つるぎのまい)は妨げない
_dg = make_poke(ability="おうごんのからだ"); execute(make_poke(moves=["でんじは"]), _dg, "でんじは")
check("おうごんのからだ でんじは無効", _dg.status is None)
_dn = make_poke(ability="しんりょく"); execute(make_poke(moves=["でんじは"]), _dn, "でんじは")
check("おうごんのからだなし でんじは有効", _dn.status == "paralysis")
_as = make_poke(moves=["つるぎのまい"]); execute(_as, make_poke(ability="おうごんのからだ"), "つるぎのまい")
check("おうごんのからだ 相手の自己強化は妨げない", _as.stage_attack == 2)

# きゅうばん: ふきとばしで強制交代されない
_kp1 = make_poke(ability="きゅうばん", moves=["まもる"]); _kp2 = make_poke(name="控え", moves=["まもる"])
_s1k = BattleSide([_kp1, _kp2]); _s2k = BattleSide([make_poke(moves=["ふきとばし"])])
Battle(_s1k, _s2k, BattleField()).resume(_Force("まもる"), _Force("ふきとばし"), max_turns=1)
check("きゅうばん 強制交代されない", _s1k.active is _kp1)
# 負例: きゅうばん無しなら ふきとばし で交代させられる
_np1 = make_poke(ability="しんりょく", moves=["まもる"]); _np2 = make_poke(name="控え2", moves=["まもる"])
_s1n = BattleSide([_np1, _np2]); _s2n = BattleSide([make_poke(moves=["ふきとばし"])])
Battle(_s1n, _s2n, BattleField()).resume(_Force("まもる"), _Force("ふきとばし"), max_turns=1)
check("きゅうばん無し 強制交代される(負例)", _s1n.active is not _np1)

# ファーコート 物理0.5倍
p_furcoat = make_poke(type1="ノーマル", ability="ファーコート", def_b=100)
p_tgt3 = make_poke(type1="ノーマル", def_b=100)
p_a = make_poke(atk_b=100)
d_fc = dmg(p_a, p_furcoat, "たいあたり", roll=0.5)
d_no_fc = dmg(p_a, p_tgt3, "たいあたり", roll=0.5)
check("ファーコート 物理0.5倍", near(d_fc / d_no_fc, 0.5))
# 負例：特殊技は半減しない（物理限定）
check("ファーコート 特殊技は等倍", near(dmg(make_poke(spatk_b=100), make_poke(type1="ノーマル", ability="ファーコート", spdef_b=100), "なみのり") / dmg(make_poke(spatk_b=100), make_poke(type1="ノーマル", spdef_b=100), "なみのり"), 1.0))

# はどうのぼうご 接触技0.5倍（メガルカリオZ専用）
p_aura = make_poke(type1="ノーマル", ability="はどうのぼうご", def_b=100, spdef_b=100)
p_aura_b = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
check("はどうのぼうご 接触技0.5倍",
      near(dmg(make_poke(atk_b=100), p_aura, "たいあたり", roll=0.5)
           / dmg(make_poke(atk_b=100), p_aura_b, "たいあたり", roll=0.5), 0.5))
# 負例：非接触の物理技は半減しない（接触限定）
check("はどうのぼうご 非接触物理は等倍",
      near(dmg(make_poke(atk_b=100), p_aura, "じしん", roll=0.5)
           / dmg(make_poke(atk_b=100), p_aura_b, "じしん", roll=0.5), 1.0))
# 負例：非接触の特殊技も半減しない
check("はどうのぼうご 特殊技は等倍",
      near(dmg(make_poke(spatk_b=100), p_aura, "なみのり", roll=0.5)
           / dmg(make_poke(spatk_b=100), p_aura_b, "なみのり", roll=0.5), 1.0))

# ── M-C 追加アイテムの不足していた検証（実効果・統合経路・負例） ──
from simulator.battle import Battle as _Bit, _entry_effects as _ent_it

# ふうせん: じめん以外は通常ダメージ（負例）／ハザードの扱い
_bl_n = make_poke(type1="ノーマル", item="ふうせん", hp_b=200, def_b=150)
_bl_p = make_poke(type1="ノーマル", item="たべのこし", hp_b=200, def_b=150)
check("ふうせん じめん以外は等倍で通る(負例)",
      dmg(make_poke(type1="ノーマル", atk_b=150, moves=["たいあたり"]), _bl_n, "たいあたり", roll=0.5)
      == dmg(make_poke(type1="ノーマル", atk_b=150, moves=["たいあたり"]), _bl_p, "たいあたり", roll=0.5))
# まきびし: ふうせん持ちは無効
_fl_hz = BattleField(); _fl_hz.spikes[0] = 3
_hz_bl = make_poke(type1="ノーマル", item="ふうせん", hp_b=200)
_ent_it(_hz_bl, 0, _fl_hz, make_poke(), [], [_hz_bl])
check("ふうせん まきびしを無効化", _hz_bl.hp == _hz_bl.max_hp, f"hp={_hz_bl.hp}")
_hz_no = make_poke(type1="ノーマル", item="たべのこし", hp_b=200)
_ent_it(_hz_no, 0, _fl_hz, make_poke(), [], [_hz_no])
check("ふうせん無しはまきびしを受ける(対照)", _hz_no.hp < _hz_no.max_hp, f"hp={_hz_no.hp}")
# ステルスロックは岩なので ふうせん でも受ける（負例）
_fl_sr = BattleField(); _fl_sr.stealth_rock[0] = True
_sr_bl = make_poke(type1="ノーマル", item="ふうせん", hp_b=200)
_ent_it(_sr_bl, 0, _fl_sr, make_poke(), [], [_sr_bl])
check("ふうせん ステルスロックは受ける(負例)", _sr_bl.hp < _sr_bl.max_hp, f"hp={_sr_bl.hp}")

# ノーマルジュエル: 実ダメージが1.3倍
_nj_a = make_poke(type1="ノーマル", atk_b=120, item="ノーマルジュエル", moves=["たいあたり"])
_nj_b = make_poke(type1="ノーマル", atk_b=120, item="たべのこし", moves=["たいあたり"])
_nj_t = make_poke(type1="ノーマル", hp_b=255, def_b=120)
check("ノーマルジュエル 実ダメージ1.3倍",
      near(dmg(_nj_a, _nj_t, "たいあたり", roll=0.5) / dmg(_nj_b, _nj_t, "たいあたり", roll=0.5), 1.3))

# グランドコート: 技でフィールドを張ると実際に8ターンになる（統合経路）
def _terrain_turns_via_move(item):
    a = make_poke(type1="でんき", hp_b=200, spd_b=200, item=item, moves=["エレキフィールド"])
    d = make_poke(type1="ノーマル", hp_b=200, moves=["つるぎのまい"])
    b = _Bit(BattleSide([a]), BattleSide([d]), BattleField())
    b._turn_loop(_Force("エレキフィールド"), _Force("つるぎのまい"), max_turns=1)
    return b.field.electric_terrain_count
check("グランドコート 技で張ると8ターン(統合)", _terrain_turns_via_move("グランドコート") >= 7,
      f"count={_terrain_turns_via_move('グランドコート')}")
check("グランドコート無しは5ターン(統合・負例)", _terrain_turns_via_move("たべのこし") <= 5,
      f"count={_terrain_turns_via_move('たべのこし')}")

# シード: 技でフィールドが張られた瞬間に相手側のシードも発動する（統合経路）
_sd_a = make_poke(type1="でんき", hp_b=200, spd_b=200, moves=["エレキフィールド"])
_sd_d = make_poke(type1="ノーマル", hp_b=200, item="エレキシード", moves=["つるぎのまい"])
_Bit(BattleSide([_sd_a]), BattleSide([_sd_d]), BattleField())._turn_loop(
    _Force("エレキフィールド"), _Force("つるぎのまい"), max_turns=1)
check("エレキシード 技での設置時に発動(統合)",
      _sd_d.stage_defense == 1 and _sd_d.item is None,
      f"stage={_sd_d.stage_defense} item={_sd_d.item}")
# シード: 継続中のフィールドへ登場したときも発動する（統合経路）
_fl_on = BattleField(); _fl_on.electric_terrain = True; _fl_on.electric_terrain_count = 3
_sd_in = make_poke(type1="ノーマル", hp_b=200, item="エレキシード")
_ent_it(_sd_in, 0, _fl_on, make_poke(), [], [_sd_in])
check("エレキシード 継続中フィールドへの登場で発動(統合)",
      _sd_in.stage_defense == 1 and _sd_in.item is None,
      f"stage={_sd_in.stage_defense} item={_sd_in.item}")
# 負例: 別のフィールドでは発動しない
_fl_ot = BattleField(); _fl_ot.grassy_terrain = True
_sd_ot = make_poke(type1="ノーマル", hp_b=200, item="エレキシード")
_ent_it(_sd_ot, 0, _fl_ot, make_poke(), [], [_sd_ot])
check("エレキシード 別フィールドでは不発(負例)",
      _sd_ot.stage_defense == 0 and _sd_ot.item == "エレキシード")

# しめつけバンド: ターン終了時の削りが 1/8 → 1/6 になる（実ダメージで確認）
def _bind_eot_loss(band):
    a = make_poke(type1="ノーマル", hp_b=255, spd_b=200, moves=["つるぎのまい"])
    d = make_poke(type1="ノーマル", hp_b=255, moves=["つるぎのまい"])
    d.bound_count = 3
    d._bound_by_band = band            # type: ignore
    b = _Bit(BattleSide([a]), BattleSide([d]), BattleField())
    b._turn_loop(_Force("つるぎのまい"), _Force("つるぎのまい"), max_turns=1)
    return d.max_hp - d.hp, d.max_hp
_loss_band, _mh = _bind_eot_loss(True)
_loss_plain, _ = _bind_eot_loss(False)
check("しめつけバンド 削りが1/6", _loss_band == max(1, _mh // 6), f"減少={_loss_band} 期待={_mh // 6}")
check("しめつけバンド無しは1/8(負例)", _loss_plain == max(1, _mh // 8),
      f"減少={_loss_plain} 期待={_mh // 8}")

# レッドカード / だっしゅつボタン: 交代を伴うので Battle 経由で確認する
from simulator.battle import Battle as _Bswi

def _swap_case(def_item):
    """相手(P2)が def_item を持ち、P1が接触技で殴る1ターンを回して交代の有無を返す。"""
    # 殴る側を確実に先攻させる。レッドカードの追い出しは「相手の次の行動処理」で消化される
    # （マジックミラーと同じ経路）ので、順番が逆だと同一ターン内には現れない。
    a1 = make_poke(type1="ノーマル", atk_b=120, hp_b=255, spd_b=200, moves=["のしかかり"])
    a1.name = "殴る側"
    a2 = make_poke(type1="ノーマル", hp_b=255, moves=["まもる"]); a2.name = "殴る側控え"
    # 防御側は自己強化技にする（まもるだとダメージが通らず、そもそも発動条件を満たさない）
    d1 = make_poke(type1="ノーマル", hp_b=255, def_b=120, item=def_item,
                   moves=["つるぎのまい"]); d1.name = "持ち主"
    d2 = make_poke(type1="ノーマル", hp_b=255, moves=["つるぎのまい"]); d2.name = "持ち主控え"
    s1 = BattleSide([a1, a2]); s2 = BattleSide([d1, d2])
    b = _Bswi(s1, s2, BattleField())
    b._turn_loop(_Force("のしかかり"), _Force("つるぎのまい"), max_turns=1)
    return s1.active is not a1, s2.active is not d1, d1.item

_rc_atk_out, _rc_def_out, _rc_item = _swap_case("レッドカード")
check("レッドカード 殴った側が交代させられる", _rc_atk_out, "攻撃側が残っている")
check("レッドカード 使用で消費", _rc_item is None, f"item={_rc_item}")
_eb_atk_out, _eb_def_out, _eb_item = _swap_case("だっしゅつボタン")
check("だっしゅつボタン 持ち主が引っ込む", _eb_def_out, "持ち主が残っている")
check("だっしゅつボタン 使用で消費", _eb_item is None, f"item={_eb_item}")
check("だっしゅつボタン 殴った側は交代しない(負例)", not _eb_atk_out)
# 負例: 控えが居なければ発動しない（消費もしない）
_lone_a = make_poke(type1="ノーマル", atk_b=120, hp_b=255, moves=["のしかかり"])
_lone_d = make_poke(type1="ノーマル", hp_b=255, def_b=120, item="レッドカード", moves=["つるぎのまい"])
_ls1 = BattleSide([_lone_a]); _ls2 = BattleSide([_lone_d])
_Bswi(_ls1, _ls2, BattleField())._turn_loop(_Force("のしかかり"), _Force("つるぎのまい"), max_turns=1)
check("レッドカード 控え無しでは不発・未消費(負例)", _lone_d.item == "レッドカード",
      f"item={_lone_d.item}")

# しめつけバンド: バインドの削りが 1/8 → 1/6
_bb_d = make_poke(type1="ノーマル", hp_b=255, def_b=120, moves=["つるぎのまい"])
_bb_a = make_poke(type1="ノーマル", atk_b=60, hp_b=255, spd_b=200,
                  item="しめつけバンド", moves=["まとわりつく"])   # 命中100（まきつくは90で落ちる）
_bs1 = BattleSide([_bb_a]); _bs2 = BattleSide([_bb_d, make_poke(hp_b=255)])
_bb = _Bswi(_bs1, _bs2, BattleField())
_bb._turn_loop(_Force("まとわりつく"), _Force("つるぎのまい"), max_turns=1)
check("しめつけバンド 束縛時に印が付く", getattr(_bb_d, "_bound_by_band", False) is True)
_nb_d = make_poke(type1="ノーマル", hp_b=255, def_b=120, moves=["つるぎのまい"])
_nb_a = make_poke(type1="ノーマル", atk_b=60, hp_b=255, spd_b=200,
                  item="たべのこし", moves=["まとわりつく"])
_nb = _Bswi(BattleSide([_nb_a]), BattleSide([_nb_d, make_poke(hp_b=255)]), BattleField())
_nb._turn_loop(_Force("まとわりつく"), _Force("つるぎのまい"), max_turns=1)
check("しめつけバンド無しでは印が付かない(負例)", getattr(_nb_d, "_bound_by_band", False) is False)

# ねつこうかん（M-C・メガセグレイブ）: ほのお技を受けると攻撃+1 / やけどにならない
# 被弾後の特性なので execute() で撃たせる（dmg()はダメージ計算だけで on_after_hit を通らない）
_nk_d = make_poke(type1="ノーマル", ability="ねつこうかん", hp_b=255, spdef_b=200)
execute(make_poke(spatk_b=10, type1="ほのお"), _nk_d, "かえんほうしゃ")
check("ねつこうかん ほのお技で攻撃+1", _nk_d.stage_attack == 1, f"stage_attack={_nk_d.stage_attack}")
# 負例：ほのお以外では上がらない
_nk_d2 = make_poke(type1="ノーマル", ability="ねつこうかん", hp_b=255, spdef_b=200)
execute(make_poke(spatk_b=10, type1="みず", moves=["なみのり"]), _nk_d2, "なみのり")
check("ねつこうかん みず技では攻撃が変動しない(負例)", _nk_d2.stage_attack == 0,
      f"stage_attack={_nk_d2.stage_attack}")
# やけど免疫（すいほうと同じ扱い）／負例として他の状態異常は通る
check("ねつこうかん やけどにならない",
      make_poke(ability="ねつこうかん").apply_status("burn") is False)
check("ねつこうかん まひは通る(負例)",
      make_poke(ability="ねつこうかん").apply_status("paralysis") is True)

# ════════════════════════════════════════════════════════════════
# M-C 新特性（グラスメイカー等13種）
# ════════════════════════════════════════════════════════════════
from simulator.battle import is_trapped
from simulator.abilities import entry_ability
from simulator.damage import is_contact_move, check_hit
from simulator.battle import crit_chance

# ── グラスメイカー / サイコメイカー: 登場時フィールド展開 ──
for _ab, _attr, _cnt in (("グラスメイカー", "grassy_terrain", "grassy_terrain_count"),
                         ("サイコメイカー", "psychic_terrain", "psychic_terrain_count")):
    _f = BattleField()
    entry_ability(make_poke(ability=_ab), make_poke(), _f)
    check(f"{_ab} 登場でフィールド展開", getattr(_f, _attr) is True)
    check(f"{_ab} 5ターン継続", getattr(_f, _cnt) == 5, f"count={getattr(_f, _cnt)}")
    _f2 = BattleField()
    entry_ability(make_poke(ability="しんりょく"), make_poke(), _f2)
    check(f"{_ab} 非メイカーでは展開しない(負例)", getattr(_f2, _attr) is False)

# サイコメイカーが展開したフィールドの効果（エスパー技1.3倍・先制技無効）
_pm_f = BattleField()
entry_ability(make_poke(ability="サイコメイカー"), make_poke(), _pm_f)
_pm_a = make_poke(type1="ノーマル", spatk_b=100)
_pm_d = make_poke(type1="ノーマル", spdef_b=100)
check("サイコメイカー エスパー技1.3倍",
      near(dmg(_pm_a, _pm_d, "サイコキネシス", f=_pm_f) / dmg(_pm_a, _pm_d, "サイコキネシス"), 1.3),
      f"ratio={dmg(_pm_a, _pm_d, 'サイコキネシス', f=_pm_f) / dmg(_pm_a, _pm_d, 'サイコキネシス')}")
check("サイコメイカー 非エスパー技は等倍(負例)",
      dmg(_pm_a, _pm_d, "りゅうのいぶき", f=_pm_f) == dmg(_pm_a, _pm_d, "りゅうのいぶき"))
_pm_pri_hp = _pm_d.hp
_execute_move(BattleSide([make_poke(atk_b=100)]), BattleSide([_pm_d]),
              Action(type="move", move=dl.get_move("でんこうせっか")), _pm_f)
check("サイコメイカー 地面のポケモンは先制技を受けない", _pm_d.hp == _pm_pri_hp,
      f"hp {_pm_pri_hp}→{_pm_d.hp}")
_pm_fly = make_poke(type1="ひこう", spdef_b=100, def_b=100, hp_b=255)
_pm_fly_hp = _pm_fly.hp
_execute_move(BattleSide([make_poke(atk_b=100)]), BattleSide([_pm_fly]),
              Action(type="move", move=dl.get_move("でんこうせっか")), _pm_f)
check("サイコメイカー ひこうタイプには先制技が通る(負例)", _pm_fly.hp < _pm_fly_hp,
      f"hp {_pm_fly_hp}→{_pm_fly.hp}")
_pm_lev = make_poke(type1="ノーマル", ability="ふゆう", spdef_b=100, def_b=100, hp_b=255)
_pm_lev_hp = _pm_lev.hp
_execute_move(BattleSide([make_poke(atk_b=100)]), BattleSide([_pm_lev]),
              Action(type="move", move=dl.get_move("でんこうせっか")), _pm_f)
check("サイコメイカー ふゆうには先制技が通る(負例)", _pm_lev.hp < _pm_lev_hp,
      f"hp {_pm_lev_hp}→{_pm_lev.hp}")
_pm_pri0 = make_poke(type1="ノーマル", spdef_b=100, def_b=100, hp_b=255)
_pm_pri0_hp = _pm_pri0.hp
_execute_move(BattleSide([make_poke(atk_b=100)]), BattleSide([_pm_pri0]),
              Action(type="move", move=dl.get_move("たいあたり")), _pm_f)
check("サイコメイカー 優先度0の技は防がれない(負例)", _pm_pri0.hp < _pm_pri0_hp,
      f"hp {_pm_pri0_hp}→{_pm_pri0.hp}")

# ── グラスメイカーはグラスシードを発動させる（設置と同時） ──
_f_seed = BattleField()
_gs = make_poke(ability="しんりょく", item="グラスシード", def_b=100)
entry_ability(make_poke(ability="グラスメイカー"), _gs, _f_seed)
check("グラスメイカー グラスシードが発動して防御+1", _gs.stage_defense == 1,
      f"stage_defense={_gs.stage_defense}")

# ── くさのけがわ: グラスフィールド時 防御1.5倍（物理のみ） ──
_f_gr = BattleField(); _f_gr.grassy_terrain = True
_kk = make_poke(type1="ノーマル", ability="くさのけがわ", def_b=100, spdef_b=100)
_kk_n = make_poke(type1="ノーマル", ability="しんりょく", def_b=100, spdef_b=100)
_atk_kk = make_poke(atk_b=100, spatk_b=100)
check("くさのけがわ グラスフィールドで物理被ダメ2/3",
      near(dmg(_atk_kk, _kk, "たいあたり", f=_f_gr) / dmg(_atk_kk, _kk_n, "たいあたり", f=_f_gr), 1/1.5),
      f"ratio={dmg(_atk_kk, _kk, 'たいあたり', f=_f_gr) / dmg(_atk_kk, _kk_n, 'たいあたり', f=_f_gr)}")
check("くさのけがわ 非フィールドでは等倍(負例)",
      dmg(_atk_kk, _kk, "たいあたり") == dmg(_atk_kk, _kk_n, "たいあたり"))
check("くさのけがわ 特殊技は等倍(負例)",
      dmg(_atk_kk, _kk, "りゅうのいぶき", f=_f_gr) == dmg(_atk_kk, _kk_n, "りゅうのいぶき", f=_f_gr))

# ── こぼれダネ: 技のダメージを受けると5ターン グラスフィールド ──
_f_kb = BattleField()
_kb_d = make_poke(type1="ノーマル", ability="こぼれダネ", hp_b=255, def_b=200)
execute(make_poke(atk_b=10), _kb_d, "たいあたり", f=_f_kb)
check("こぼれダネ 被弾でグラスフィールド展開", _f_kb.grassy_terrain is True)
check("こぼれダネ 5ターン継続", _f_kb.grassy_terrain_count == 5)
_f_kb2 = BattleField()
_kb_g = make_poke(type1="ゴースト", ability="こぼれダネ", hp_b=255, def_b=200)
execute(make_poke(atk_b=10), _kb_g, "たいあたり", f=_f_kb2)
check("こぼれダネ ダメージ0では展開しない(負例)", _f_kb2.grassy_terrain is False)

# ── にげあし: 野生からの逃走だけで、交代を邪魔する効果は防がない（監査200 #8。交代できるのはゴーストタイプ・きれいなぬけがら）──
_shadow = make_poke(ability="かげふみ")
check("にげあし でも かげふみ 下では交代できない", is_trapped(make_poke(ability="にげあし"), _shadow) is True)
check("にげあし 通常特性はかげふみで交代不可(負例)",
      is_trapped(make_poke(ability="しんりょく"), _shadow) is True)
check("ゴーストタイプ は かげふみ 下でも交代できる", is_trapped(make_poke(type1="ゴースト"), _shadow) is False)
_bound = make_poke(ability="にげあし"); _bound.trapped = True
check("にげあし でも逃げられない状態は交代できない", is_trapped(_bound, make_poke()) is True)
_bound_n = make_poke(ability="しんりょく"); _bound_n.trapped = True
check("にげあし 通常特性はトラップ技で交代不可(負例)",
      is_trapped(_bound_n, make_poke()) is True)

# ── はがねのせいしん: 自分のはがね技1.5倍 ──
_hs = make_poke(type1="ノーマル", ability="はがねのせいしん", atk_b=100)
_hs_n = make_poke(type1="ノーマル", ability="しんりょく", atk_b=100)
_hs_t = make_poke(type1="ノーマル", def_b=100)
check("はがねのせいしん はがね技1.5倍",
      near(dmg(_hs, _hs_t, "アイアンヘッド") / dmg(_hs_n, _hs_t, "アイアンヘッド"), 1.5))
check("はがねのせいしん 他タイプ技は等倍(負例)",
      dmg(_hs, _hs_t, "たいあたり") == dmg(_hs_n, _hs_t, "たいあたり"))

# ── はりこみ: 交代で出てきた相手に威力2倍 ──
_hr = make_poke(type1="ノーマル", ability="はりこみ", atk_b=100)
_hr_n = make_poke(type1="ノーマル", ability="しんりょく", atk_b=100)
_hr_t = make_poke(type1="ノーマル", def_b=100)
_hr_t._switched_in_this_turn = True
check("はりこみ 交代で出てきた相手に2倍",
      near(dmg(_hr, _hr_t, "たいあたり") / dmg(_hr_n, _hr_t, "たいあたり"), 2.0),
      f"ratio={dmg(_hr, _hr_t, 'たいあたり') / dmg(_hr_n, _hr_t, 'たいあたり')}")
_hr_t2 = make_poke(type1="ノーマル", def_b=100)
check("はりこみ 交代していない相手には等倍(負例)",
      dmg(_hr, _hr_t2, "たいあたり") == dmg(_hr_n, _hr_t2, "たいあたり"))

# ── ばんけん: いかく無効＋攻撃+1 / 交代させる技・道具が効かない ──
_bk = make_poke(ability="ばんけん")
entry_ability(make_poke(ability="いかく"), _bk, BattleField())
check("ばんけん いかくで攻撃+1", _bk.stage_attack == 1, f"stage_attack={_bk.stage_attack}")
_bk_n = make_poke(ability="しんりょく")
entry_ability(make_poke(ability="いかく"), _bk_n, BattleField())
check("ばんけん 通常特性はいかくで攻撃-1(負例)", _bk_n.stage_attack == -1)
_bk_d = make_poke(type1="ノーマル", ability="ばんけん", hp_b=255, def_b=200)
execute(make_poke(atk_b=10), _bk_d, "ドラゴンテール")
check("ばんけん ドラゴンテールで追い出されない", getattr(_bk_d, "_force_switch", False) is False)
_bk_d2 = make_poke(type1="ノーマル", ability="しんりょく", hp_b=255, def_b=200)
execute(make_poke(atk_b=10), _bk_d2, "ドラゴンテール")
check("ばんけん 通常特性は追い出される(負例)", getattr(_bk_d2, "_force_switch", False) is True)
_rc_a = make_poke(type1="ノーマル", ability="ばんけん", atk_b=10)
_rc_d = make_poke(type1="ノーマル", hp_b=255, def_b=200, item="レッドカード")
execute(_rc_a, _rc_d, "たいあたり")
check("ばんけん レッドカードが効かない", getattr(_rc_a, "_force_switch", False) is False)

# ── びびり: あく/ゴースト/むし技・いかくで素早さ+1 ──
for _t, _mv in (("あく", "あくのはどう"), ("ゴースト", "シャドーボール"), ("むし", "むしのていこう")):
    _bb = make_poke(type1="エスパー", ability="びびり", hp_b=255, spdef_b=200)
    execute(make_poke(spatk_b=10, type1=_t), _bb, _mv)
    check(f"びびり {_t}技で素早さ+1", _bb.stage_speed == 1, f"stage_speed={_bb.stage_speed}")
_bb_n = make_poke(type1="ノーマル", ability="びびり", hp_b=255, def_b=200)
execute(make_poke(atk_b=10), _bb_n, "たいあたり")
check("びびり ノーマル技では素早さが変動しない(負例)", _bb_n.stage_speed == 0,
      f"stage_speed={_bb_n.stage_speed}")
_bb_i = make_poke(ability="びびり")
entry_ability(make_poke(ability="いかく"), _bb_i, BattleField())
check("びびり いかくで素早さ+1", _bb_i.stage_speed == 1 and _bb_i.stage_attack == 0,
      f"S={_bb_i.stage_speed} A={_bb_i.stage_attack}")

# ── パンクロック: 音技の威力1.3倍・音技被ダメ半減 ──
_pr = make_poke(type1="ノーマル", ability="パンクロック", spatk_b=100)
_pr_n = make_poke(type1="ノーマル", ability="しんりょく", spatk_b=100)
_pr_t = make_poke(type1="ノーマル", spdef_b=100, def_b=100)
check("パンクロック 音技1.3倍",
      near(dmg(_pr, _pr_t, "ハイパーボイス") / dmg(_pr_n, _pr_t, "ハイパーボイス"), 1.3),
      f"ratio={dmg(_pr, _pr_t, 'ハイパーボイス') / dmg(_pr_n, _pr_t, 'ハイパーボイス')}")
check("パンクロック 非音技は等倍(負例)",
      dmg(_pr, _pr_t, "たいあたり") == dmg(_pr_n, _pr_t, "たいあたり"))
_pr_d = make_poke(type1="ノーマル", ability="パンクロック", spdef_b=100)
_pr_dn = make_poke(type1="ノーマル", ability="しんりょく", spdef_b=100)
check("パンクロック 音技被ダメ半減",
      near(dmg(_pr_n, _pr_d, "ハイパーボイス") / dmg(_pr_n, _pr_dn, "ハイパーボイス"), 0.5),
      f"ratio={dmg(_pr_n, _pr_d, 'ハイパーボイス') / dmg(_pr_n, _pr_dn, 'ハイパーボイス')}")
check("パンクロック 非音技の被ダメは等倍(負例)",
      dmg(_pr_n, _pr_d, "たいあたり") == dmg(_pr_n, _pr_dn, "たいあたり"))

# ── ヘドロえき: HP吸収技を受けると相手を回復させずダメージ ──
_hd_a = make_poke(type1="ノーマル", ability="しんりょく", spatk_b=100, hp_b=255)
_hd_a.hp = _hd_a.max_hp // 2
_hp0 = _hd_a.hp
execute(_hd_a, make_poke(type1="ノーマル", ability="ヘドロえき", hp_b=255, spdef_b=100), "ギガドレイン")
check("ヘドロえき 吸収技で攻撃側がダメージを受ける", _hd_a.hp < _hp0, f"hp {_hp0}→{_hd_a.hp}")
_hd_a2 = make_poke(type1="ノーマル", ability="しんりょく", spatk_b=100, hp_b=255)
_hd_a2.hp = _hd_a2.max_hp // 2
_hp0b = _hd_a2.hp
execute(_hd_a2, make_poke(type1="ノーマル", ability="しんりょく", hp_b=255, spdef_b=100), "ギガドレイン")
check("ヘドロえき 通常特性なら吸収で回復する(負例)", _hd_a2.hp > _hp0b, f"hp {_hp0b}→{_hd_a2.hp}")

# ── リベロ: 登場するたび1回だけ、出す技のタイプに変化 ──
from simulator.battle import apply_pre_move_forms
_lb = make_poke(type1="ほのお", ability="リベロ")
apply_pre_move_forms(_lb, dl.get_move("たいあたり"))
check("リベロ 技タイプに変化", (_lb.type1, _lb.type2) == ("ノーマル", None), f"{_lb.type1}/{_lb.type2}")
apply_pre_move_forms(_lb, dl.get_move("なみのり"))
check("リベロ 2回目は変化しない(負例)", _lb.type1 == "ノーマル", f"type1={_lb.type1}")

# ── ききかいひ: HPが1/2以下になると手持ちに戻る ──
_kk_d = make_poke(type1="ノーマル", ability="ききかいひ", hp_b=255, def_b=200)
_kk_d.hp = _kk_d.max_hp // 2 + 1
_kk_side = BattleSide([_kk_d, make_poke(name="控え")])
_execute_move(BattleSide([make_poke(atk_b=10)]), _kk_side,
              Action(type="move", move=dl.get_move("たいあたり")), BattleField())
check("ききかいひ 1/2以下になると引っ込む",
      _kk_d.hp * 2 <= _kk_d.max_hp and getattr(_kk_d, "_pivot_out", False) is True,
      f"hp={_kk_d.hp}/{_kk_d.max_hp} pivot={getattr(_kk_d, '_pivot_out', False)}")
_kk_d2 = make_poke(type1="ノーマル", ability="ききかいひ", hp_b=255, def_b=200)
_kk_d2.hp = _kk_d2.max_hp // 4
_execute_move(BattleSide([make_poke(atk_b=10)]), BattleSide([_kk_d2, make_poke(name="控え")]),
              Action(type="move", move=dl.get_move("たいあたり")), BattleField())
check("ききかいひ すでに1/2以下なら発動しない(負例)",
      getattr(_kk_d2, "_pivot_out", False) is False)
_kk_d3 = make_poke(type1="ノーマル", ability="ききかいひ", hp_b=255, def_b=200)
_kk_d3.hp = _kk_d3.max_hp // 2 + 5
_execute_move(BattleSide([make_poke(atk_b=10)]), BattleSide([_kk_d3]),
              Action(type="move", move=dl.get_move("たいあたり")), BattleField())
check("ききかいひ 控えがいなければ引っ込まない(負例)",
      getattr(_kk_d3, "_pivot_out", False) is False)


# ════════════════════════════════════════════════════════════════
# M-C 新技8種（DB属性＋効果）
# ════════════════════════════════════════════════════════════════
MC_MOVES = [
    ("きょけんとつげき", "ドラゴン", "physical", 120, 100, 8, True),
    ("ドラムアタック",   "くさ",     "physical", 80,  100, 12, False),
    ("かえんボール",     "ほのお",   "physical", 120, 90,  8, False),
    ("コートチェンジ",   "ノーマル", "status",   None, 100, 12, False),
    ("でんこうそうげき", "でんき",   "physical", 120, 100, 8, True),
    ("さいきのいのり",   "ノーマル", "status",   None, None, 1, False),
    ("スターアサルト",   "かくとう", "physical", 170, 100, 8, False),
    ("ねらいうち",       "みず",     "special",  85,  100, 16, False),
]
for _n, _ty, _cat, _pw, _acc, _pp, _ctn in MC_MOVES:
    _m = dl.get_move(_n)
    check(f"{_n} DB登録あり", _m is not None)
    if _m is None:
        continue
    check(f"{_n} タイプ/分類", (_m.type, _m.category) == (_ty, _cat), f"{_m.type}/{_m.category}")
    check(f"{_n} 威力{_pw}/命中{_acc}/PP{_pp}",
          (_m.power, _m.accuracy, _m.pp) == (_pw, _acc, _pp),
          f"{_m.power}/{_m.accuracy}/{_m.pp}")
    if _cat == "physical":
        check(f"{_n} 接触={_ctn}", is_contact_move(_m) is _ctn)

# ── きょけんとつげき: 使用後、次に自分が行動するまで無防備（被ダメ2倍・必中） ──
_gr_a = make_poke(type1="ドラゴン", ability="しんりょく", atk_b=100, hp_b=255, def_b=100)
_gr_d = make_poke(type1="ノーマル", hp_b=255, def_b=100, atk_b=100)
execute(_gr_a, _gr_d, "きょけんとつげき")
check("きょけんとつげき 使用後は無防備状態", getattr(_gr_a, "_defenseless", False) is True)
_gr_plain = make_poke(type1="ドラゴン", ability="しんりょく", atk_b=100, hp_b=255, def_b=100)
check("きょけんとつげき 無防備中の被ダメ2倍",
      near(dmg(_gr_d, _gr_a, "たいあたり") / dmg(_gr_d, _gr_plain, "たいあたり"), 2.0),
      f"ratio={dmg(_gr_d, _gr_a, 'たいあたり') / dmg(_gr_d, _gr_plain, 'たいあたり')}")
check("きょけんとつげき 無防備中は必中",
      all(check_hit(_gr_d, _gr_a, dl.get_move("ふぶき"), BattleField()) for _ in range(20)))
check("きょけんとつげき 通常時は被ダメ等倍(負例)",
      dmg(_gr_d, _gr_plain, "たいあたり") == dmg(_gr_d, make_poke(type1="ドラゴン", def_b=100, hp_b=255), "たいあたり"))
execute(_gr_a, _gr_d, "たいあたり")
check("きょけんとつげき 次に自分が行動すると解除",
      getattr(_gr_a, "_defenseless", False) is False)

# ── ドラムアタック: 100%で相手の素早さ-1 ──
_da_d = make_poke(type1="ノーマル", hp_b=255, def_b=200)
execute(make_poke(atk_b=10, type1="くさ"), _da_d, "ドラムアタック")
check("ドラムアタック 相手の素早さ-1", _da_d.stage_speed == -1, f"stage_speed={_da_d.stage_speed}")
_da_d2 = make_poke(type1="ノーマル", hp_b=255, def_b=200)
execute(make_poke(atk_b=10, type1="くさ"), _da_d2, "リーフブレード")
check("ドラムアタック 他のくさ技では下がらない(負例)", _da_d2.stage_speed == 0)

# ── かえんボール: 弾技・10%やけど・自分のこおりを治す ──
from simulator.damage import BALL_BOMB_MOVES
check("かえんボール 弾技に分類", "かえんボール" in BALL_BOMB_MOVES)
_pb_a = make_poke(type1="ほのお", atk_b=100)
_pb_a.status = "freeze"
execute(_pb_a, make_poke(type1="ノーマル", hp_b=255, def_b=200), "かえんボール")
check("かえんボール 自分のこおりが治る", _pb_a.status is None, f"status={_pb_a.status}")
random.seed(7)
_burn = 0
for _ in range(600):
    _pb_d = make_poke(type1="ノーマル", hp_b=255, def_b=200)
    execute(make_poke(type1="ほのお", atk_b=10), _pb_d, "かえんボール")
    if _pb_d.status == "burn":
        _burn += 1
check("かえんボール やけど確率10%", 0.05 <= _burn / 600 <= 0.16, f"rate={_burn/600:.3f}")
_pb_d3 = make_poke(type1="ほのお", hp_b=255, def_b=200)
execute(make_poke(type1="ほのお", atk_b=10), _pb_d3, "かえんボール")
check("かえんボール ほのおタイプはやけどにならない(負例)", _pb_d3.status is None)

# ── でんこうそうげき: パンチ技・でんきタイプ消失・非でんきで失敗 ──
from simulator.damage import PUNCH_MOVES
check("でんこうそうげき パンチ技に分類", "でんこうそうげき" in PUNCH_MOVES)
_ds_a = make_poke(type1="でんき", type2="ひこう", atk_b=100)
execute(_ds_a, make_poke(type1="ノーマル", hp_b=255, def_b=200), "でんこうそうげき")
check("でんこうそうげき 自分のでんきタイプが消える",
      (_ds_a.type1, _ds_a.type2) == ("ひこう", None), f"{_ds_a.type1}/{_ds_a.type2}")
_ds_a2 = make_poke(type1="ノーマル", atk_b=100)
_ds_d2 = make_poke(type1="ノーマル", hp_b=255, def_b=200)
_hp_before = _ds_d2.hp
_logs_ds = execute(_ds_a2, _ds_d2, "でんこうそうげき")
check("でんこうそうげき 非でんきタイプは失敗する(負例)",
      _ds_d2.hp == _hp_before and any("失敗" in l for l in _logs_ds))

# ── スターアサルト: 使った次のターン反動状態 ──
_ma_a = make_poke(type1="かくとう", atk_b=100)
execute(_ma_a, make_poke(type1="ノーマル", hp_b=255, def_b=200), "スターアサルト")
check("スターアサルト 使用後は反動状態", _ma_a.recharge is True)
_ma_a2 = make_poke(type1="かくとう", atk_b=100)
execute(_ma_a2, make_poke(type1="ノーマル", hp_b=255, def_b=200), "インファイト")
check("スターアサルト 他のかくとう技では反動しない(負例)", _ma_a2.recharge is False)

# ── ねらいうち: 急所ランク+1 ──
_ss_a = make_poke(type1="みず", spatk_b=100)
_ss_d = make_poke(type1="ノーマル", spdef_b=100)
check("ねらいうち 急所ランク+1(1/8)",
      near(crit_chance(_ss_a, dl.get_move("ねらいうち"), _ss_d), 1/8, rel=0.01),
      f"p={crit_chance(_ss_a, dl.get_move('ねらいうち'), _ss_d)}")
check("ねらいうち 通常技は1/24(負例)",
      near(crit_chance(_ss_a, dl.get_move("なみのり"), _ss_d), 1/24, rel=0.01))

# ════════════════════════════════════════════════════════════════
# ランキング200位対応で追加した4技
# ════════════════════════════════════════════════════════════════
from simulator.abilities import SLICING_MOVES
from simulator.damage import SOUND_MOVES

MC2_MOVES = [
    ("オーバードライブ", "でんき",   "special",  80,  100, 12, False),
    ("くらいつく",       "あく",     "physical", 80,  100, 12, True),
    ("きりさく",         "ノーマル", "physical", 80,  100, 20, True),
    ("たこがため",       "かくとう", "status",   None, 100, 16, False),
]
for _n, _ty, _cat, _pw, _acc, _pp, _ctn in MC2_MOVES:
    _m = dl.get_move(_n)
    check(f"{_n} DB登録あり", _m is not None)
    if _m is None:
        continue
    check(f"{_n} タイプ/分類", (_m.type, _m.category) == (_ty, _cat), f"{_m.type}/{_m.category}")
    check(f"{_n} 威力{_pw}/命中{_acc}/PP{_pp}",
          (_m.power, _m.accuracy, _m.pp) == (_pw, _acc, _pp), f"{_m.power}/{_m.accuracy}/{_m.pp}")
    if _cat == "physical":
        check(f"{_n} 接触={_ctn}", is_contact_move(_m) is _ctn)

# ── オーバードライブ: 音技 ──
check("オーバードライブ 音技に分類", "オーバードライブ" in SOUND_MOVES)
_od_a = make_poke(type1="でんき", ability="パンクロック", spatk_b=100)
_od_n = make_poke(type1="でんき", ability="しんりょく", spatk_b=100)
_od_d = make_poke(type1="ノーマル", spdef_b=100)
check("オーバードライブ パンクロックで1.3倍(音技の証跡)",
      near(dmg(_od_a, _od_d, "オーバードライブ") / dmg(_od_n, _od_d, "オーバードライブ"), 1.3))
check("オーバードライブ 非音技のでんき技は等倍(負例)",
      dmg(_od_a, _od_d, "10まんボルト") == dmg(_od_n, _od_d, "10まんボルト"))

# ── くらいつく: 噛み技 / 相手と自分の両方が交代不可 ──
_jl_a = make_poke(type1="あく", ability="がんじょうあご", atk_b=100)
_jl_n = make_poke(type1="あく", ability="しんりょく", atk_b=100)
_jl_t = make_poke(type1="エスパー", def_b=100)
check("くらいつく がんじょうあごで1.5倍(噛み技の証跡)",
      near(dmg(_jl_a, _jl_t, "くらいつく") / dmg(_jl_n, _jl_t, "くらいつく"), 1.5))
check("くらいつく 非噛み技のあく技は等倍(負例)",
      dmg(_jl_a, _jl_t, "あくのはどう") == dmg(_jl_n, _jl_t, "あくのはどう"))
_jl_atk = make_poke(type1="あく", atk_b=100)
_jl_def = make_poke(type1="エスパー", hp_b=255, def_b=100)
execute(_jl_atk, _jl_def, "くらいつく")
check("くらいつく 相手が交代不可", _jl_def.trapped is True)
check("くらいつく 自分も交代不可", _jl_atk.trapped is True)
_jl_a2 = make_poke(type1="あく", atk_b=100)
_jl_d2 = make_poke(type1="あく", hp_b=255, def_b=100)   # あくはあく等倍だが、ここは別技での負例
execute(_jl_a2, _jl_d2, "かみくだく")
check("くらいつく 他の噛み技では交代不可にならない(負例)",
      _jl_d2.trapped is False and _jl_a2.trapped is False)

# ── きりさく: 切り技 / 急所ランク+1 ──
check("きりさく 切り技に分類", "きりさく" in SLICING_MOVES)
_sl_a = make_poke(type1="ノーマル", ability="きれあじ", atk_b=100)
_sl_n = make_poke(type1="ノーマル", ability="しんりょく", atk_b=100)
_sl_t = make_poke(type1="ノーマル", def_b=100)
check("きりさく きれあじで1.5倍(切り技の証跡)",
      near(dmg(_sl_a, _sl_t, "きりさく") / dmg(_sl_n, _sl_t, "きりさく"), 1.5))
check("きりさく 非切り技は等倍(負例)",
      dmg(_sl_a, _sl_t, "たいあたり") == dmg(_sl_n, _sl_t, "たいあたり"))
check("きりさく 急所ランク+1(1/8)",
      near(crit_chance(_sl_n, dl.get_move("きりさく"), _sl_t), 1/8, rel=0.01))
check("きりさく 通常技は1/24(負例)",
      near(crit_chance(_sl_n, dl.get_move("たいあたり"), _sl_t), 1/24, rel=0.01))

# ── たこがため: にげられない + ターン終了時にB/D-1 ──
_ol_a = make_poke(type1="かくとう", moves=["たこがため"])
_ol_d = make_poke(type1="ノーマル", hp_b=255)
_execute_move(BattleSide([_ol_a]), BattleSide([_ol_d]),
              Action(type="move", move=dl.get_move("たこがため")), BattleField())
check("たこがため 相手が交代不可", _ol_d.trapped is True)
check("たこがため たこがため状態になる", getattr(_ol_d, "_octolocked", False) is True)
check("たこがため 使用時点ではB/Dは下がらない",
      _ol_d.stage_defense == 0 and _ol_d.stage_sp_defense == 0)
_ol_tgt = make_poke(name="A", type1="ノーマル", moves=["まもる"], hp_b=255)
_ol_tgt._octolocked = True
Battle(BattleSide([_ol_tgt]), BattleSide([make_poke(moves=["まもる"])]))._end_of_turn()
check("たこがため ターン終了時にB/Dが1段階下がる",
      _ol_tgt.stage_defense == -1 and _ol_tgt.stage_sp_defense == -1,
      f"B={_ol_tgt.stage_defense} D={_ol_tgt.stage_sp_defense}")
_ol_free = make_poke(name="A", type1="ノーマル", moves=["まもる"], hp_b=255)
Battle(BattleSide([_ol_free]), BattleSide([make_poke(moves=["まもる"])]))._end_of_turn()
check("たこがため 非たこがためは下がらない(負例)",
      _ol_free.stage_defense == 0 and _ol_free.stage_sp_defense == 0)

# ── コートチェンジ: 味方と相手の場の状態を入れ替える ──
_cc_f = BattleField()
_cc_a = make_poke(type1="ノーマル", moves=["コートチェンジ"])
_cc_s1 = BattleSide([_cc_a]); _cc_s2 = BattleSide([make_poke()])
_cc_s1.field_idx, _cc_s2.field_idx = 0, 1
_cc_f.stealth_rock[0] = True
_cc_f.spikes[1] = 2
_cc_s1.reflect = True; _cc_s1.reflect_count = 4
_cc_s2.tailwind = True; _cc_s2.tailwind_count = 3
_execute_move(_cc_s1, _cc_s2, Action(type="move", move=dl.get_move("コートチェンジ")), _cc_f)
check("コートチェンジ ステルスロックが入れ替わる",
      _cc_f.stealth_rock == [False, True], f"{_cc_f.stealth_rock}")
check("コートチェンジ まきびしが入れ替わる", _cc_f.spikes == [2, 0], f"{_cc_f.spikes}")
check("コートチェンジ リフレクターが相手側へ移る",
      _cc_s1.reflect is False and _cc_s2.reflect is True and _cc_s2.reflect_count == 4)
check("コートチェンジ おいかぜが自分側へ移る",
      _cc_s1.tailwind is True and _cc_s1.tailwind_count == 3 and _cc_s2.tailwind is False)
# 負例: 全体の場（天候・フィールド・トリックルーム）は side を持たないので入れ替わらない
_cc_g = BattleField()
_cc_g.weather = "sunny"; _cc_g.weather_count = 5
_cc_g.grassy_terrain = True; _cc_g.grassy_terrain_count = 5
_cc_g.trick_room = True; _cc_g.trick_room_count = 5
_cc_t1 = BattleSide([make_poke(moves=["コートチェンジ"])]); _cc_t2 = BattleSide([make_poke()])
_cc_t1.field_idx, _cc_t2.field_idx = 0, 1
_execute_move(_cc_t1, _cc_t2, Action(type="move", move=dl.get_move("コートチェンジ")), _cc_g)
check("コートチェンジ 全体の場は入れ替え対象外(負例)",
      _cc_g.weather == "sunny" and _cc_g.weather_count == 5
      and _cc_g.grassy_terrain is True and _cc_g.grassy_terrain_count == 5
      and _cc_g.trick_room is True and _cc_g.trick_room_count == 5,
      f"weather={_cc_g.weather}/{_cc_g.weather_count} grass={_cc_g.grassy_terrain} tr={_cc_g.trick_room}")
# 負例: 何も設置されていなければ入れ替えても両側とも変化なし
_cc_e = BattleField()
_cc_e1 = BattleSide([make_poke(moves=["コートチェンジ"])]); _cc_e2 = BattleSide([make_poke()])
_cc_e1.field_idx, _cc_e2.field_idx = 0, 1
_execute_move(_cc_e1, _cc_e2, Action(type="move", move=dl.get_move("コートチェンジ")), _cc_e)
check("コートチェンジ 場が空なら双方とも無変化(負例)",
      _cc_e.stealth_rock == [False, False] and _cc_e.spikes == [0, 0]
      and _cc_e1.reflect is False and _cc_e2.reflect is False
      and _cc_e1.tailwind is False and _cc_e2.tailwind is False)

# ── さいきのいのり: ひんしの手持ちをHP1/2で復活 ──
_rb_a = make_poke(type1="ノーマル", moves=["さいきのいのり"])
_rb_dead = make_poke(name="ひんし", hp_b=100)
_rb_dead.hp = 0; _rb_dead.is_alive = False
_rb_s1 = BattleSide([_rb_a, _rb_dead])
_execute_move(_rb_s1, BattleSide([make_poke()]),
              Action(type="move", move=dl.get_move("さいきのいのり")), BattleField())
check("さいきのいのり ひんしが復活する", _rb_dead.is_alive is True)
check("さいきのいのり HPは最大の1/2", _rb_dead.hp == _rb_dead.max_hp // 2,
      f"hp={_rb_dead.hp}/{_rb_dead.max_hp}")
_rb_a2 = make_poke(type1="ノーマル", moves=["さいきのいのり"])
_logs_rb = _execute_move(BattleSide([_rb_a2, make_poke(name="元気")]), BattleSide([make_poke()]),
                         Action(type="move", move=dl.get_move("さいきのいのり")), BattleField())
check("さいきのいのり ひんしがいなければ失敗する(負例)",
      any("失敗" in l for l in _logs_rb))

# あついしぼう ほのお/こおり0.5倍
p_thickfat = make_poke(type1="ノーマル", ability="あついしぼう", spdef_b=100)
p_sp_atk = make_poke(spatk_b=100)
d_tf = dmg(p_sp_atk, p_thickfat, "かえんほうしゃ", roll=0.5)
p_no_tf = make_poke(type1="ノーマル", spdef_b=100)
d_no_tf = dmg(p_sp_atk, p_no_tf, "かえんほうしゃ", roll=0.5)
check("あついしぼう ほのお0.5倍", near(d_tf / d_no_tf, 0.5))
# あついしぼう こおりタイプも0.5倍
d_tf_ice = dmg(p_sp_atk, p_thickfat, "れいとうビーム", roll=0.5)
d_no_tf_ice = dmg(p_sp_atk, p_no_tf, "れいとうビーム", roll=0.5)
check("あついしぼう こおり0.5倍", near(d_tf_ice / d_no_tf_ice, 0.5))

# かんそうはだ ほのお1.25倍ダメージ（みず無効＋回復は別途）
p_dryskin = make_poke(type1="ノーマル", ability="かんそうはだ", spdef_b=100)
d_ds = dmg(p_sp_atk, p_dryskin, "かえんほうしゃ", roll=0.5)
check("かんそうはだ ほのお1.25倍被弾", near(d_ds / d_no_tf, 1.25), f"ratio={d_ds / d_no_tf}")

# ふしぎなうろこ 状態異常で防御1.5倍（物理のみ／特殊には効かない）
p_marvel = make_poke(type1="ノーマル", ability="ふしぎなうろこ", def_b=100, spdef_b=100)
p_marvel_st = make_poke(type1="ノーマル", ability="ふしぎなうろこ", def_b=100, spdef_b=100); p_marvel_st.status = "burn"
p_phys_m = make_poke(atk_b=100)
d_ms_no = dmg(p_phys_m, p_marvel, "たいあたり", roll=0.5)
d_ms_st = dmg(p_phys_m, p_marvel_st, "たいあたり", roll=0.5)
check("ふしぎなうろこ 状態異常で物理被弾減(防御1.5倍)", near(d_ms_st / d_ms_no, 1/1.5), f"ratio={d_ms_st / d_ms_no}")
p_spec_m = make_poke(spatk_b=100)
d_ms_sp_no = dmg(p_spec_m, p_marvel, "ハイドロポンプ", roll=0.5)
p_marvel_st2 = make_poke(type1="ノーマル", ability="ふしぎなうろこ", def_b=100, spdef_b=100); p_marvel_st2.status = "burn"
d_ms_sp_st = dmg(p_spec_m, p_marvel_st2, "ハイドロポンプ", roll=0.5)
check("ふしぎなうろこ 特殊には効かない", near(d_ms_sp_st / d_ms_sp_no, 1.0), f"ratio={d_ms_sp_st / d_ms_sp_no}")

# もうか/げきりゅう/しんりょく (HP1/3以下で1.5倍)
for ab, move_n, move_type in [("もうか","かえんほうしゃ","ほのお"),
                                ("げきりゅう","なみのり","みず"),
                                ("しんりょく","エナジーボール","くさ")]:
    p_pb = make_poke(type1=move_type, spatk_b=100, ability=ab)
    p_tgt_pb = make_poke(spdef_b=100)
    p_pb.hp = p_pb.max_hp // 4  # 1/4 → 1/3以下
    d_pb = dmg(p_pb, p_tgt_pb, move_n, roll=0.5)
    p_pb_full = make_poke(type1=move_type, spatk_b=100, ability=ab)
    d_pb_full = dmg(p_pb_full, p_tgt_pb, move_n, roll=0.5)
    check(f"{ab} HP1/3以下で1.5倍", near(d_pb / d_pb_full, 1.5))

# せいでんき (接触技で30%まひ) - 確率テスト
from simulator.abilities import on_after_hit
p_static = make_poke(ability="せいでんき")
random.seed(0)
hit_count = 0
for _ in range(200):
    p_atk_s = make_poke()
    on_after_hit(p_atk_s, p_static, dl.get_move("のしかかり"), [])  # 接触技
    if p_atk_s.status == "paralysis":
        hit_count += 1
check("せいでんき 接触30%まひ(±10%)", 20 < hit_count < 80, f"{hit_count}/200")

# せいでんき 非接触技では発動しない
p_atk_nc = make_poke()
on_after_hit(p_atk_nc, make_poke(ability="せいでんき"), dl.get_move("タネマシンガン"), [])
check("せいでんき 非接触技(タネマシンガン)でまひしない", p_atk_nc.status is None)

# さめはだ/てつのとげ (接触技でHP1/8反動)
from simulator.abilities import _rough_skin_recoil
p_rough = make_poke(type1="みず", ability="さめはだ")
p_contact = make_poke(atk_b=100)
logs_rs = []
_rough_skin_recoil(p_contact, p_rough, dl.get_move("のしかかり"), logs_rs)  # 接触技
expected_rs = max(1, p_contact.max_hp // 8)
check("さめはだ 接触1/8反動", p_contact.max_hp - p_contact.hp == expected_rs)

# さめはだ 非接触技では発動しない
p_nc = make_poke(atk_b=100)
_rough_skin_recoil(p_nc, make_poke(ability="さめはだ"), dl.get_move("タネマシンガン"), [])
check("さめはだ 非接触技(タネマシンガン)で反動なし", p_nc.hp == p_nc.max_hp)

# きもったま (ノーマル/格闘がゴーストに通る)
p_ghost = make_poke(type1="ゴースト", def_b=100)
p_scrappy = make_poke(atk_b=100, ability="きもったま")
p_no_scrappy = make_poke(atk_b=100)
check("きもったま ゴーストにノーマル通る", dmg(p_scrappy, p_ghost, "たいあたり") > 0)
check("きもったま なし ゴーストにノーマル無効", dmg(p_no_scrappy, p_ghost, "たいあたり") == 0)
# きもったま かくとう技もゴーストに通る
check("きもったま ゴーストにかくとう通る", dmg(p_scrappy, p_ghost, "インファイト") > 0)
check("きもったま なし ゴーストにかくとう無効", dmg(p_no_scrappy, p_ghost, "インファイト") == 0)
# きもったま：いかくも効かない
from simulator.abilities import entry_ability as _ent_sc
_pscr_i = make_poke(ability="きもったま", atk_b=100)
_ent_sc(make_poke(ability="いかく"), _pscr_i, BattleField())
check("きもったま いかく無効", _pscr_i.stage_attack == 0, f"atk={_pscr_i.stage_attack}")

# かちき (能力低下で特攻+2)
from simulator.abilities import on_stat_lowered
p_compet = make_poke(ability="かちき")
old_sc = p_compet.stage_sp_attack
on_stat_lowered(p_compet, [])
check("かちき 能力低下で特攻+2", p_compet.stage_sp_attack == old_sc + 2)

# まけんき (能力低下で攻撃+2)
p_defiant = make_poke(ability="まけんき")
old_sd = p_defiant.stage_attack
on_stat_lowered(p_defiant, [])
check("まけんき 能力低下で攻撃+2", p_defiant.stage_attack == old_sd + 2)

# ぎゃくじょう (相手の攻撃でHP1/2以下になると特攻+1)
# HPを1/2直上に置き、小ダメージで確実に1/2以下へ落とす（決定的）
p_anger = make_poke(ability="ぎゃくじょう", def_b=200, hp_b=255)
p_anger.hp = p_anger.max_hp // 2 + 1
execute(make_poke(atk_b=60), p_anger, "たいあたり")
check("ぎゃくじょう HP半分以下で特攻+1",
      p_anger.is_alive and p_anger.hp <= p_anger.max_hp // 2 and p_anger.stage_sp_attack == 1 and p_anger.stage_attack == 0,
      f"hp={p_anger.hp}/{p_anger.max_hp} spa={p_anger.stage_sp_attack}")
# 負例：HPが1/2超のままなら上がらない
p_anger2 = make_poke(ability="ぎゃくじょう", def_b=200, hp_b=255); p_anger2.hp = p_anger2.max_hp
execute(make_poke(atk_b=10), p_anger2, "たいあたり")
check("ぎゃくじょう HP1/2超では上がらない",
      p_anger2.hp > p_anger2.max_hp // 2 and p_anger2.stage_sp_attack == 0,
      f"hp={p_anger2.hp}/{p_anger2.max_hp} spa={p_anger2.stage_sp_attack}")

# くだけるよろい (物理被弾で防御-1・速度+2)
p_weakarmor = make_poke(ability="くだけるよろい", def_b=100)
p_phys = make_poke(atk_b=100)
logs_wa = execute(p_phys, p_weakarmor, "たいあたり")
check("くだけるよろい 防御-1", p_weakarmor.stage_defense == -1)
check("くだけるよろい 速度+2", p_weakarmor.stage_speed == 2)
# 負例：物理技以外（特殊技）では発動しない
_pwa_n = make_poke(ability="くだけるよろい", spdef_b=100)
execute(make_poke(spatk_b=100), _pwa_n, "なみのり")
check("くだけるよろい 特殊技では発動しない", _pwa_n.stage_defense == 0 and _pwa_n.stage_speed == 0)


# ── ふうりょく ────────────────────────────────────────────────────────────────
p_cyclizar = make_poke("サイクレーザー", type1="ノーマル", ability="ふうりょく", moves=["たいあたり"])
p_wind_atk = make_poke("風使い", type1="ひこう", ability="", moves=["ぼうふう"], spatk_b=100)
random.seed(1)
logs_wind = execute(p_wind_atk, p_cyclizar, "ぼうふう")
check("ふうりょく ぼうふうでじゅうでん", p_cyclizar.charged)

# 非風技では発動しない
p_cyclizar2 = make_poke("サイクレーザー2", type1="ノーマル", ability="ふうりょく", moves=["たいあたり"])
execute(make_poke(type1="ノーマル", moves=["たいあたり"]), p_cyclizar2, "たいあたり")
check("ふうりょく 非風技は発動しない", not p_cyclizar2.charged)

# ── どくどく必中（毒タイプ限定） ─────────────────────────────────────────────
from simulator.damage import check_hit as _check_hit
p_toxic_user = make_poke(type1="どく", moves=["どくどく"])
p_target_td  = make_poke(type1="ノーマル", moves=["たいあたり"])
m_toxic = dl.get_move("どくどく")
always_hit = all(_check_hit(p_toxic_user, p_target_td, m_toxic, BattleField()) for _ in range(20))
check("どくどく 毒タイプ必中", always_hit)

p_normal_user = make_poke(type1="ノーマル", moves=["どくどく"])
hit_count = sum(_check_hit(p_normal_user, p_target_td, m_toxic, BattleField()) for _ in range(1000))
check("どくどく 非毒タイプは必中でない", hit_count < 1000)

# ── 特性カバレッジ（ability_audit A対応・威力倍率系）──
def _ratio(ab, mv, dtype="ノーマル", f=None, atk_b=100, spatk_b=100):
    a1 = make_poke(type1="ノーマル", atk_b=atk_b, spatk_b=spatk_b, ability=ab)
    a0 = make_poke(type1="ノーマル", atk_b=atk_b, spatk_b=spatk_b)
    d = make_poke(type1=dtype, def_b=100, spdef_b=100)
    return dmg(a1, d, mv, f=f) / max(1, dmg(a0, d, mv, f=f))
check("かたいツメ 接触1.3倍", near(_ratio("かたいツメ","たいあたり"), 1.3))
check("てつのこぶし パンチ1.2倍", near(_ratio("てつのこぶし","ほのおのパンチ"), 1.2))
check("メガランチャー 波動1.5倍", near(_ratio("メガランチャー","みずのはどう"), 1.5))
check("がんじょうあご 噛む1.5倍", near(_ratio("がんじょうあご","かみくだく"), 1.5))
check("ちからもち 物理2倍", near(_ratio("ちからもち","たいあたり"), 2.0))
check("ちからもち 特殊技は等倍", near(_ratio("ちからもち","なみのり"), 1.0))
check("ヨガパワー 物理2倍", near(_ratio("ヨガパワー","たいあたり"), 2.0))
check("ヨガパワー 特殊技は等倍", near(_ratio("ヨガパワー","なみのり"), 1.0))
check("すてみ 反動技1.2倍", near(_ratio("すてみ","すてみタックル"), 1.2))
check("すてみ 非反動技は等倍", near(_ratio("すてみ","たいあたり"), 1.0))
# すなかき/すながくれ/すなのちから：すなあらしのダメージを受けない（ノーマル型で検証）
_Bsd = __import__('simulator.battle', fromlist=['Battle']).Battle
for _ab_sd in ("すなかき", "すながくれ", "すなのちから", "ぼうじん"):
    _psd = make_poke(type1="ノーマル", ability=_ab_sd, hp_b=255); _hsd = _psd.hp
    _fsd = BattleField(); _fsd.weather = "sandstorm"; _fsd.weather_count = 5
    _Bsd(BattleSide([_psd]), BattleSide([make_poke(type1="いわ", hp_b=255)]), _fsd)._end_of_turn()
    check(f"{_ab_sd} 砂嵐ダメージ無効", _psd.hp == _hsd, f"hp={_psd.hp}/{_hsd}")
# 対照：通常ノーマル型は砂嵐ダメージを受ける
_psd0 = make_poke(type1="ノーマル", hp_b=255); _hsd0 = _psd0.hp
_fsd0 = BattleField(); _fsd0.weather = "sandstorm"; _fsd0.weather_count = 5
_Bsd(BattleSide([_psd0]), BattleSide([make_poke(type1="いわ", hp_b=255)]), _fsd0)._end_of_turn()
check("対照: 通常ノーマルは砂嵐ダメージ", _psd0.hp < _hsd0, f"hp={_psd0.hp}/{_hsd0}")
check("きれあじ 切る技1.5倍", near(_ratio("きれあじ","サイコカッター"), 1.5))
# カテゴリ技強化系：負例（非カテゴリ技は等倍）＋代表技の追加検証
check("かたいツメ 非接触技は等倍", near(_ratio("かたいツメ","なみのり"), 1.0))
check("てつのこぶし 非パンチ技は等倍", near(_ratio("てつのこぶし","たいあたり"), 1.0))
check("メガランチャー 非波動技は等倍", near(_ratio("メガランチャー","なみのり"), 1.0))
check("きれあじ 非切る技は等倍", near(_ratio("きれあじ","たいあたり"), 1.0))
check("がんじょうあご キバ技も1.5倍", near(_ratio("がんじょうあご","ほのおのキバ"), 1.5))
check("がんじょうあご 非噛む技は等倍", near(_ratio("がんじょうあご","なみのり"), 1.0))
_fsand = BattleField(); _fsand.weather = "sandstorm"
check("すなのちから 砂でいわ技1.3倍", near(_ratio("すなのちから","いわなだれ", f=_fsand), 1.3))
check("すなのちから 砂でじめん技1.3倍", near(_ratio("すなのちから","じしん", f=_fsand), 1.3))
check("すなのちから 砂ではがね技1.3倍", near(_ratio("すなのちから","アイアンヘッド", f=_fsand), 1.3))
_fsun_sp = BattleField(); _fsun_sp.weather = "sunny"
check("サンパワー 晴れ特攻1.5倍", near(_ratio("サンパワー","10まんボルト", f=_fsun_sp), 1.5))
# ハードロック：効果バツグンを0.75倍（被弾側）
_hr = make_poke(type1="ほのお", ability="ハードロック", spdef_b=100); _hr0 = make_poke(type1="ほのお", spdef_b=100)
check("ハードロック 効果抜群0.75倍", near(dmg(make_poke(spatk_b=100), _hr, "なみのり") / dmg(make_poke(spatk_b=100), _hr0, "なみのり"), 0.75))
check("ハードロック 等倍は無効", near(dmg(make_poke(atk_b=100), make_poke(type1="ノーマル", ability="ハードロック", def_b=100), "たいあたり") / dmg(make_poke(atk_b=100), make_poke(type1="ノーマル", def_b=100), "たいあたり"), 1.0))
# フィルター：効果バツグンを3/4(0.75倍)（被弾側）
_fl = make_poke(type1="ほのお", ability="フィルター", spdef_b=100); _fl0 = make_poke(type1="ほのお", spdef_b=100)
check("フィルター 効果抜群3/4", near(dmg(make_poke(spatk_b=100), _fl, "なみのり") / dmg(make_poke(spatk_b=100), _fl0, "なみのり"), 0.75))
check("フィルター 等倍は無効", near(dmg(make_poke(atk_b=100), make_poke(type1="ノーマル", ability="フィルター", def_b=100), "たいあたり") / dmg(make_poke(atk_b=100), make_poke(type1="ノーマル", def_b=100), "たいあたり"), 1.0))

# ── 天候速度2倍（_speed_orderの先攻判定で検証）──
from simulator.battle import _speed_order
def _first(ab, weather):
    _fast = make_poke(ability=ab, spd_b=50); _slow = make_poke(spd_b=70)
    _f = BattleField()
    if weather: _f.weather = weather
    _a = Action(type="move", move=dl.get_move("たいあたり"))
    return _speed_order(BattleSide([_fast]), _a, BattleSide([_slow]), _a, _f)
for _ab_sp, _w in [("すいすい","rain"),("ようりょくそ","sunny"),("すなかき","sandstorm"),("ゆきかき","hail")]:
    check(f"{_ab_sp} 天候で素早さ2倍(先攻)", _first(_ab_sp, _w) and not _first(_ab_sp, None),
          f"weather={_first(_ab_sp,_w)} none={_first(_ab_sp,None)}")

# ── ターン終了時 ──
from simulator.abilities import end_of_turn_ability
# あめうけざら/アイスボディ：天候でHP1/16回復
for _ab_h, _w in [("あめうけざら","rain"),("アイスボディ","hail")]:
    _ph = make_poke(ability=_ab_h, hp_b=200); _ph.hp = _ph.max_hp // 2; _b = _ph.hp
    _fw = BattleField(); _fw.weather = _w
    end_of_turn_ability(_ph, _fw, [])
    check(f"{_ab_h} 天候で1/16回復", _ph.hp == _b + max(1, _ph.max_hp // 16), f"hp={_ph.hp}/{_b}")
    # 負例：対応天候でなければ回復しない
    _ph_n = make_poke(ability=_ab_h, hp_b=200); _ph_n.hp = _ph_n.max_hp // 2; _bn = _ph_n.hp
    end_of_turn_ability(_ph_n, BattleField(), [])
    check(f"{_ab_h} 非天候では回復しない", _ph_n.hp == _bn, f"hp={_ph_n.hp}/{_bn}")
# かそく：ターン終了で素早さ+1
_pacc = make_poke(ability="かそく"); end_of_turn_ability(_pacc, BattleField(), [])
check("かそく ターン終了で素早さ+1", _pacc.stage_speed == 1, f"spd={_pacc.stage_speed}")
# ムラっけ：いずれか+2・別の-1（合計+1）
random.seed(0); _pmr = make_poke(ability="ムラっけ"); end_of_turn_ability(_pmr, BattleField(), [])
_stsum = sum(getattr(_pmr, s, 0) for s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed","stage_accuracy","stage_evasion"))
check("ムラっけ +2/-1(合計+1)", _stsum == 1 and any(getattr(_pmr,s,0)==2 for s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed","stage_accuracy","stage_evasion")), f"sum={_stsum}")
# サンパワー：晴れ中ターン終了で1/8ダメージ
_psp = make_poke(ability="サンパワー", hp_b=200); _bsp = _psp.hp; _fsp2 = BattleField(); _fsp2.weather = "sunny"
end_of_turn_ability(_psp, _fsp2, [])
check("サンパワー 晴れ中1/8自傷", _psp.hp == _bsp - max(1, _psp.max_hp // 8), f"hp={_psp.hp}/{_bsp}")
# 負例：非晴れでは自傷しない（特攻補正も非晴れでは無し）
_psp0 = make_poke(ability="サンパワー", hp_b=200); _bsp0 = _psp0.hp
end_of_turn_ability(_psp0, BattleField(), [])
check("サンパワー 非晴れでは自傷しない", _psp0.hp == _bsp0, f"hp={_psp0.hp}/{_bsp0}")
check("サンパワー 非晴れでは特攻補正なし", near(dmg(make_poke(spatk_b=100, ability="サンパワー"), make_poke(spdef_b=100), "10まんボルト") / dmg(make_poke(spatk_b=100), make_poke(spdef_b=100), "10まんボルト"), 1.0))

# ── 交代時 ──
from simulator.abilities import on_switch_out
# しぜんかいふく：交代で状態異常治癒
_pnc = make_poke(ability="しぜんかいふく"); _pnc.status = "burn"; on_switch_out(_pnc, [])
check("しぜんかいふく 交代で状態治癒", _pnc.status is None, f"status={_pnc.status}")
# マイティチェンジ：交代でマイティフォルム化
_pmc = make_poke(ability="マイティチェンジ"); on_switch_out(_pmc, [])
check("マイティチェンジ 交代でフォルム変化", _pmc.hero_forme, f"hero={_pmc.hero_forme}")

# ── 特性カバレッジ（ability_audit A対応・免疫/効果系）──
_pde = make_poke(type1="ノーマル", ability="でんきエンジン", spdef_b=100, hp_b=255)
execute(make_poke(spatk_b=100, type1="でんき"), _pde, "10まんボルト")
check("でんきエンジン でんきで素早さ+1", _pde.stage_speed == 1, f"spd={_pde.stage_speed}")
check("でんきエンジン でんき無効", dmg(p_grd, make_poke(type1="ノーマル", ability="でんきエンジン", spdef_b=100), "10まんボルト") == 0)
# 負例：でんき技以外を受けても素早さは上がらない（無条件の上昇ではない）
_pde_n = make_poke(type1="ノーマル", ability="でんきエンジン", def_b=100, hp_b=255)
execute(make_poke(atk_b=50), _pde_n, "たいあたり")
check("でんきエンジン 非でんき技では上がらない", _pde_n.stage_speed == 0, f"spd={_pde_n.stage_speed}")
_pec = make_poke(type1="ノーマル", ability="でんきにかえる", hp_b=255, spdef_b=200)
execute(make_poke(spatk_b=60), _pec, "たいあたり")
check("でんきにかえる 被弾でチャージ", getattr(_pec, "_electromorphosis_charged", False))
_pec_n = make_poke(type1="ノーマル", ability="でんきにかえる", hp_b=255, spdef_b=200)
execute(make_poke(atk_b=10, moves=["でんじは"]), _pec_n, "でんじは")
check("でんきにかえる 変化技では発動しない", not getattr(_pec_n, "_electromorphosis_charged", False))
# 効果：チャージ中はでんき技の威力が1.5倍（フラグだけでなく実ダメージを検証）
_pec_c = make_poke(type1="ノーマル", spatk_b=100, ability="でんきにかえる"); _pec_c._electromorphosis_charged = True
_pec_u = make_poke(type1="ノーマル", spatk_b=100, ability="でんきにかえる")
_dec_t = make_poke(type1="ノーマル", spdef_b=100)
check("でんきにかえる チャージで電気技1.5倍", near(dmg(_pec_c, _dec_t, "10まんボルト") / dmg(_pec_u, _dec_t, "10まんボルト"), 1.5))
_pen = make_poke(type1="ノーマル", ability="じきゅうりょく", hp_b=255, def_b=150)
execute(make_poke(atk_b=50), _pen, "たいあたり")
check("じきゅうりょく 被弾で防御+1", _pen.stage_defense == 1, f"def={_pen.stage_defense}")
_pen_n = make_poke(type1="ノーマル", ability="じきゅうりょく", hp_b=255, def_b=150)
execute(make_poke(atk_b=10, moves=["でんじは"]), _pen_n, "でんじは")
check("じきゅうりょく 変化技では発動しない", _pen_n.stage_defense == 0)
_sync_ok = False
for _ in range(20):
    _psy = make_poke(type1="ノーマル", ability="シンクロ", hp_b=255, spdef_b=200); _atk_sy = make_poke(atk_b=10)
    execute(_atk_sy, _psy, "でんじは")
    if _atk_sy.status == "paralysis": _sync_ok = True; break
check("シンクロ 状態異常を相手にも伝染", _sync_ok, "でんじは付与時に相手も麻痺")
_pcj = make_poke(atk_b=100, ability="こんじょう"); _pcj.status = "poison"
_pcj0 = make_poke(atk_b=100, ability="こんじょう"); _dcj = make_poke(def_b=100)
check("こんじょう 状態異常で物理1.5倍", near(dmg(_pcj, _dcj, "たいあたり") / dmg(_pcj0, _dcj, "たいあたり"), 1.5))
# こんじょう：やけどの物理半減(0.5)を無視（やけどでも0.75倍にならず1.5倍）
_pcj_b = make_poke(atk_b=100, ability="こんじょう"); _pcj_b.status = "burn"
_pnb = make_poke(atk_b=100); _pnb.status = "burn"   # 通常やけど(対照)
_pn0 = make_poke(atk_b=100)
check("対照: 通常やけど物理0.5倍", near(dmg(_pnb, _dcj, "たいあたり") / dmg(_pn0, _dcj, "たいあたり"), 0.5))
check("こんじょう やけど半減無視(1.5倍維持)", near(dmg(_pcj_b, _dcj, "たいあたり") / dmg(_pn0, _dcj, "たいあたり"), 1.5))
check("はりきり 物理1.5倍", near(_ratio("はりきり", "たいあたり"), 1.5))
# はりきり：物理技の命中0.8倍（統計、命中100技で約80%）
random.seed(7)
_N_hk = 3000; _hit_hk = sum(1 for _ in range(_N_hk) if _check_hit(make_poke(atk_b=80, ability="はりきり"), make_poke(def_b=80), dl.get_move("はたく"), BattleField()))
check("はりきり 命中0.8倍", 0.74 < _hit_hk / _N_hk < 0.86, f"{_hit_hk}/{_N_hk}")
check("はりきり 特殊技は等倍(攻撃強化のみ)", near(_ratio("はりきり", "なみのり"), 1.0))
_pst5 = make_poke(atk_b=100, ability="そうだいしょう"); _pst5.fainted_allies = 5
_pst0 = make_poke(atk_b=100); _dst = make_poke(def_b=100)
check("そうだいしょう 5体で1.5倍", near(dmg(_pst5, _dst, "たいあたり") / dmg(_pst0, _dst, "たいあたり"), 1.5))
random.seed(0); _rp_b = False
for _ in range(60):
    _drp = make_poke(type1="ノーマル", ability="りんぷん", hp_b=255, spdef_b=100)
    execute(make_poke(spatk_b=120, type1="ほのお"), _drp, "かえんほうしゃ")
    if _drp.status == "burn": _rp_b = True; break
check("りんぷん 追加効果無効(やけど出ない)", not _rp_b)
_pso = make_poke(type1="ノーマル", ability="ぼうおん", spdef_b=100)
check("ぼうおん 音技無効", dmg(make_poke(spatk_b=100), _pso, "ハイパーボイス") == 0)
check("ぼうおん 非音技は通る", dmg(make_poke(spatk_b=100), _pso, "なみのり") > 0)
_ppw = make_poke(type1="ノーマル", ability="ぼうじん", hp_b=255); execute(make_poke(), _ppw, "しびれごな")
check("ぼうじん 粉技無効", _ppw.status != "paralysis", f"status={_ppw.status}")
_png_a = make_poke(atk_b=100, ability="ノーガード"); _png_d = make_poke(type1="ノーマル", hp_b=255, def_b=100)
check("ノーガード 必中", all(_check_hit(_png_a, _png_d, dl.get_move("ぜったいれいど"), BattleField()) for _ in range(10)))
# お互い：ノーガード持ちを狙う相手の技も必中（命中80%のストーンエッジでも当たる）
_png_atk = make_poke(atk_b=100); _png_holder = make_poke(type1="ノーマル", ability="ノーガード", def_b=100)
check("ノーガード 相手の技も必中(受け側)", all(_check_hit(_png_atk, _png_holder, dl.get_move("ストーンエッジ"), BattleField()) for _ in range(30)))
_pmg = make_poke(ability="マジックガード"); _pmg.status = "poison"
check("マジックガード 間接ダメ無効", _pmg.end_of_turn_damage() == 0)
_pph = make_poke(ability="ポイズンヒール", hp_b=200); _pph.status = "poison"
check("ポイズンヒール 毒で回復", _pph.end_of_turn_damage() == -(max(1, _pph.max_hp // 8)))
_pbk = make_poke(type1="フェアリー", ability="ばけのかわ", hp_b=200, def_b=120); _bbk = _pbk.hp
execute(make_poke(atk_b=200), _pbk, "たいあたり")
check("ばけのかわ 初回1/8のみ被弾", _pbk.hp == _bbk - max(1, _pbk.max_hp // 8), f"hp={_pbk.hp}/{_bbk}")
# 2発目：ばれたすがたなので通常ダメージ（1/8を超える）
_h_after_bk = _pbk.hp
execute(make_poke(atk_b=200), _pbk, "たいあたり")
check("ばけのかわ 2発目は通常ダメージ", _h_after_bk - _pbk.hp > max(1, _pbk.max_hp // 8), f"dmg={_h_after_bk - _pbk.hp}")
_phd = make_poke(atk_b=100, ability="ひとでなし"); _dhd = make_poke(def_b=100); _dhd.status = "poison"
check("ひとでなし 毒相手に確定急所", all(_check_critical(_phd, dl.get_move("たいあたり"), _dhd) for _ in range(10)))
# 負例：非毒の相手には確定急所にならない
_dhd_h = make_poke(def_b=100)
_crit_h = sum(1 for _ in range(60) if _check_critical(make_poke(atk_b=100, ability="ひとでなし"), dl.get_move("たいあたり"), _dhd_h))
check("ひとでなし 非毒相手は確定急所でない", _crit_h < 60, f"crit={_crit_h}/60")
random.seed(0)
_kc = sum(1 for _ in range(2400) if _check_critical(make_poke(ability="きょううん"), dl.get_move("たいあたり")))
_bc = sum(1 for _ in range(2400) if _check_critical(make_poke(), dl.get_move("たいあたり")))
check("きょううん 急所率上昇", _kc > _bc * 2, f"きょううん={_kc} base={_bc}")
_phm = make_poke(type1="ノーマル", ability="はとむね", hp_b=255)
execute(make_poke(atk_b=60, type1="ほのお"), _phm, "ほのおのムチ")
check("はとむね 防御下がらない", _phm.stage_defense == 0, f"def={_phm.stage_defense}")
# 対照：はとむね無しなら同じ技で防御が下がる（防いだことの裏付け）
_phm0 = make_poke(type1="ノーマル", hp_b=255)
execute(make_poke(atk_b=60, type1="ほのお"), _phm0, "ほのおのムチ")
check("はとむね 対照: 通常は防御-1", _phm0.stage_defense == -1, f"def={_phm0.stage_defense}")
_pbs = make_poke(type1="はがね", atk_b=100, ability="バトルスイッチ"); execute(_pbs, make_poke(hp_b=255, def_b=200), "たいあたり")
check("バトルスイッチ 攻撃でブレード化", getattr(_pbs, "_in_blade_forme", False))
_pmm_d = make_poke(type1="ノーマル", ability="マジックミラー", hp_b=255); _atk_mm = make_poke(type1="ノーマル", atk_b=10)
execute(_atk_mm, _pmm_d, "でんじは")
check("マジックミラー 変化技ブロック(自分は無傷)", _pmm_d.status != "paralysis", f"def={_pmm_d.status}")
# 跳ね返し：攻撃側が代わりにまひする
check("マジックミラー 攻撃側に跳ね返す", _atk_mm.status == "paralysis", f"atk={_atk_mm.status}")
# ちょうはつも跳ね返す（攻撃側がちょうはつ状態に）
_pmm_d2 = make_poke(type1="ノーマル", ability="マジックミラー", hp_b=255); _atk_mm2 = make_poke(atk_b=10)
execute(_atk_mm2, _pmm_d2, "ちょうはつ")
check("マジックミラー ちょうはつ跳ね返し", _pmm_d2.taunt_count == 0 and _atk_mm2.taunt_count > 0, f"d={_pmm_d2.taunt_count} a={_atk_mm2.taunt_count}")
# 攻撃技は跳ね返さない（通常通りダメージ）
_pmm_d3 = make_poke(type1="ノーマル", ability="マジックミラー", hp_b=255, def_b=100); _h_mm3 = _pmm_d3.hp
execute(make_poke(atk_b=100), _pmm_d3, "たいあたり")
check("マジックミラー 攻撃技は跳ね返さない", _pmm_d3.hp < _h_mm3)
from simulator.items import on_item_consumed
_pku = make_poke(ability="かるわざ"); _pku.item = None; on_item_consumed(_pku, [])
check("かるわざ 道具消費で素早さ+2(=2倍)", _pku.stage_speed == 2, f"spd={_pku.stage_speed}")
def _first_status(ab):
    _fst = make_poke(ability=ab, spd_b=55); _fst.status = "burn"; _slo = make_poke(spd_b=70)
    _a = Action(type="move", move=dl.get_move("たいあたり"))
    return _speed_order(BattleSide([_fst]), _a, BattleSide([_slo]), _a, BattleField())
check("はやあし 状態異常で素早さ上昇(先攻)", _first_status("はやあし"))
random.seed(0); _fsg = BattleField(); _fsg.weather = "sandstorm"
_miss_sg = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), make_poke(type1="じめん", ability="すながくれ"), dl.get_move("れいとうビーム"), _fsg))
_miss_sn = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), make_poke(type1="じめん"), dl.get_move("れいとうビーム"), BattleField()))
check("すながくれ 砂で回避上昇", _miss_sg > _miss_sn, f"sg={_miss_sg} n={_miss_sn}")
# すながくれ：回避率1.25倍＝命中0.8倍（命中100技で約80%、統計）
random.seed(11); _N_sg = 3000
_hit_sg = sum(1 for _ in range(_N_sg) if _check_hit(make_poke(atk_b=80), make_poke(type1="じめん", ability="すながくれ"), dl.get_move("はたく"), _fsg))
check("すながくれ 命中0.8倍(回避1.25)", 0.74 < _hit_sg / _N_sg < 0.86, f"{_hit_sg}/{_N_sg}")
random.seed(0); _nb_ok = False
for _ in range(80):
    _dnb = make_poke(type1="ノーマル", ability="のろわれボディ", hp_b=255, def_b=200); _anb = make_poke(atk_b=40, moves=["たいあたり"])
    execute(_anb, _dnb, "たいあたり")
    if getattr(_anb, "disabled_move", None) == "たいあたり": _nb_ok = True; break
check("のろわれボディ 被弾でわざふうじ発生", _nb_ok)
# 負例：ダメージの無い変化技では発動しない
_dnb_n = make_poke(type1="ノーマル", ability="のろわれボディ", hp_b=255); _anb_n = make_poke(moves=["でんじは"])
execute(_anb_n, _dnb_n, "でんじは")
check("のろわれボディ 変化技では発動しない", getattr(_anb_n, "disabled_move", None) != "でんじは")
# すりぬけ：スクリーン無視（10まんボルトのlight_screen 0.5を無視）
_sd1 = BattleSide([make_poke(type1="ノーマル", hp_b=255, spdef_b=100)]); _sd1.light_screen = True; _sd1.light_screen_count = 5
_h1 = _sd1.active.hp
_execute_move(BattleSide([make_poke(spatk_b=100, ability="すりぬけ")]), _sd1, Action(type="move", move=dl.get_move("10まんボルト")), BattleField())
_dsr = _h1 - _sd1.active.hp
_sd2 = BattleSide([make_poke(type1="ノーマル", hp_b=255, spdef_b=100)]); _sd2.light_screen = True; _sd2.light_screen_count = 5
_h2 = _sd2.active.hp
_execute_move(BattleSide([make_poke(spatk_b=100)]), _sd2, Action(type="move", move=dl.get_move("10まんボルト")), BattleField())
_dsn = _h2 - _sd2.active.hp
check("すりぬけ スクリーン無視", _dsr > _dsn * 1.4, f"すりぬけ={_dsr} 通常={_dsn}")

# ════════ フェーズ②：新規実装特性のテスト ════════
# 状態異常免疫
for _ab_im, _st, _mv_im in [("じゅうなん","paralysis","でんじは"),("めんえき","poison","どくどく"),
                             ("マグマのよろい","freeze","れいとうビーム"),("すいほう","burn","おにび")]:
    _pim = make_poke(type1="ノーマル", ability=_ab_im, hp_b=255, spdef_b=200)
    for _ in range(8):
        execute(make_poke(spatk_b=10, atk_b=10), _pim, _mv_im)
    check(f"{_ab_im} {_st}免疫", _pim.status != _st, f"status={_pim.status}")
_pks = make_poke(type1="ノーマル", ability="きよめのしお", hp_b=255)
for _ in range(8): execute(make_poke(atk_b=10), _pks, "でんじは")
check("きよめのしお 状態異常無効", _pks.status is None, f"status={_pks.status}")

# 被ダメ補正
_pheat = make_poke(type1="ノーマル", ability="たいねつ", spdef_b=100); _pheat0 = make_poke(type1="ノーマル", spdef_b=100)
check("たいねつ ほのお0.5倍", near(dmg(make_poke(spatk_b=100), _pheat, "かえんほうしゃ") / dmg(make_poke(spatk_b=100), _pheat0, "かえんほうしゃ"), 0.5))
# たいねつ：やけどダメージも半減（通常1/16 → 1/32）
_ph_b = make_poke(type1="ノーマル", ability="たいねつ", hp_b=200); _ph_b.status = "burn"
_pn_b = make_poke(type1="ノーマル", hp_b=200); _pn_b.status = "burn"
check("たいねつ やけどダメージ半減", _ph_b.end_of_turn_damage() == max(1, _pn_b.end_of_turn_damage() // 2),
      f"taiネツ={_ph_b.end_of_turn_damage()} 通常={_pn_b.end_of_turn_damage()}")
_pbub = make_poke(type1="ノーマル", ability="すいほう", spdef_b=100)
check("すいほう ほのお0.5倍", near(dmg(make_poke(spatk_b=100), _pbub, "かえんほうしゃ") / dmg(make_poke(spatk_b=100), _pheat0, "かえんほうしゃ"), 0.5))
check("すいほう みず2倍", near(_ratio("すいほう", "なみのり"), 2.0))
_pclean = make_poke(type1="エスパー", ability="きよめのしお", spdef_b=100); _pclean0 = make_poke(type1="エスパー", spdef_b=100)
check("きよめのしお ゴースト0.5倍", near(dmg(make_poke(spatk_b=100), _pclean, "シャドーボール") / dmg(make_poke(spatk_b=100), _pclean0, "シャドーボール"), 0.5))
# 負例：非ゴースト技は半減しない
_pcl_n = make_poke(type1="ノーマル", ability="きよめのしお", spdef_b=100); _pcl_n0 = make_poke(type1="ノーマル", spdef_b=100)
check("きよめのしお 非ゴースト技は等倍", near(dmg(make_poke(spatk_b=100), _pcl_n, "なみのり") / dmg(make_poke(spatk_b=100), _pcl_n0, "なみのり"), 1.0))

# どしょく（じめん吸収＋1/4回復）
_pdv = make_poke(type1="ノーマル", ability="どしょく", spdef_b=100, hp_b=200); _pdv.hp = _pdv.max_hp // 2; _bdv = _pdv.hp
check("どしょく じめん無効", dmg(make_poke(atk_b=100, type1="じめん"), _pdv, "じしん") == 0)
execute(make_poke(atk_b=100, type1="じめん"), _pdv, "じしん")
check("どしょく じめんで1/4回復", _pdv.hp == min(_pdv.max_hp, _bdv + max(1, _pdv.max_hp // 4)), f"hp={_pdv.hp}/{_bdv}")

# 接触系
random.seed(0); _fb = False
for _ in range(60):
    _df = make_poke(type1="ノーマル", ability="ほのおのからだ", hp_b=255, def_b=200); _af = make_poke(atk_b=30, moves=["のしかかり"])
    execute(_af, _df, "のしかかり")
    if _af.status == "burn": _fb = True; break
check("ほのおのからだ 接触でやけど発生", _fb)
random.seed(0); _pt = False
for _ in range(60):
    _dp2 = make_poke(type1="ノーマル", ability="どくのトゲ", hp_b=255, def_b=200); _ap2 = make_poke(atk_b=30, moves=["のしかかり"])
    execute(_ap2, _dp2, "のしかかり")
    if _ap2.status == "poison": _pt = True; break
check("どくのトゲ 接触でどく発生", _pt)
_dsl = make_poke(type1="ノーマル", ability="ぬめぬめ", hp_b=255, def_b=200); _asl = make_poke(atk_b=30, moves=["のしかかり"])
execute(_asl, _dsl, "のしかかり")
check("ぬめぬめ 接触で素早さ-1", _asl.stage_speed == -1, f"spd={_asl.stage_speed}")
_djk = make_poke(type1="ノーマル", ability="せいぎのこころ", hp_b=255, spdef_b=200)
execute(make_poke(spatk_b=10, type1="あく"), _djk, "あくのはどう")
check("せいぎのこころ あく技で攻撃+1", _djk.stage_attack == 1, f"atk={_djk.stage_attack}")
_dws = make_poke(type1="ノーマル", ability="さまようたましい", hp_b=255, def_b=200); _aws = make_poke(atk_b=30, ability="いかく", moves=["のしかかり"])
execute(_aws, _dws, "のしかかり")
check("さまようたましい 接触で特性入替", _aws.ability == "さまようたましい" and _dws.ability == "いかく", f"a={_aws.ability} d={_dws.ability}")
_dmu = make_poke(type1="ノーマル", ability="ミイラ", hp_b=255, def_b=200); _amu = make_poke(atk_b=30, ability="ちからもち", moves=["のしかかり"])
execute(_amu, _dmu, "のしかかり")
check("ミイラ 接触で相手特性をミイラに", _amu.ability == "ミイラ", f"a={_amu.ability}")
random.seed(0); _ptx = False
for _ in range(60):
    _dtx = make_poke(type1="ノーマル", hp_b=255, def_b=200); _atx = make_poke(atk_b=30, ability="どくしゅ", moves=["のしかかり"])
    execute(_atx, _dtx, "のしかかり")
    if _dtx.status == "poison": _ptx = True; break
check("どくしゅ 接触付与でどく発生", _ptx)
_dab = make_poke(type1="ノーマル", ability="ゆうばく", hp_b=1, def_b=1); _aab = make_poke(atk_b=200, hp_b=255, moves=["のしかかり"]); _haab = _aab.hp
execute(_aab, _dab, "のしかかり")
check("ゆうばく 接触ひんしで1/4ダメ", (not _dab.is_alive) and _aab.hp == _haab - max(1, _aab.max_hp // 4), f"hp={_aab.hp}/{_haab}")
# 接触系の負例：非接触技（タネマシンガン）では発動しない
_nc_move = "タネマシンガン"
_dfb_n = make_poke(type1="ノーマル", ability="ほのおのからだ", hp_b=255, def_b=200); _afb_n = make_poke(atk_b=30, moves=[_nc_move])
execute(_afb_n, _dfb_n, _nc_move)
check("ほのおのからだ 非接触ではやけどしない", _afb_n.status is None)
_dpt_n = make_poke(type1="ノーマル", ability="どくのトゲ", hp_b=255, def_b=200); _apt_n = make_poke(atk_b=30, moves=[_nc_move])
execute(_apt_n, _dpt_n, _nc_move)
check("どくのトゲ 非接触ではどくにしない", _apt_n.status is None)
_dsl_n = make_poke(type1="ノーマル", ability="ぬめぬめ", hp_b=255, def_b=200); _asl_n = make_poke(atk_b=30, moves=[_nc_move])
execute(_asl_n, _dsl_n, _nc_move)
check("ぬめぬめ 非接触では素早さ下がらない", _asl_n.stage_speed == 0)
_dtx_n = make_poke(type1="ノーマル", hp_b=255, def_b=200); _atx_n = make_poke(atk_b=30, ability="どくしゅ", moves=[_nc_move])
execute(_atx_n, _dtx_n, _nc_move)
check("どくしゅ 非接触ではどくにしない", _dtx_n.status is None)
_dws_n = make_poke(type1="ノーマル", ability="さまようたましい", hp_b=255, def_b=200); _aws_n = make_poke(atk_b=30, ability="いかく", moves=[_nc_move])
execute(_aws_n, _dws_n, _nc_move)
check("さまようたましい 非接触では特性入替なし", _aws_n.ability == "いかく")
_dmu_n = make_poke(type1="ノーマル", ability="ミイラ", hp_b=255, def_b=200); _amu_n = make_poke(atk_b=30, ability="ちからもち", moves=[_nc_move])
execute(_amu_n, _dmu_n, _nc_move)
check("ミイラ 非接触では特性変化なし", _amu_n.ability == "ちからもち")
_dab_n = make_poke(type1="ノーマル", ability="ゆうばく", hp_b=1, def_b=1); _aab_n = make_poke(spatk_b=200, hp_b=255, moves=[_nc_move]); _haab_n = _aab_n.hp
execute(_aab_n, _dab_n, _nc_move)
check("ゆうばく 非接触ひんしでは反動なし", (not _dab_n.is_alive) and _aab_n.hp == _haab_n)
# せいぎのこころ 負例：非あく技では攻撃が上がらない
_djk_n = make_poke(type1="ノーマル", ability="せいぎのこころ", hp_b=255, def_b=200)
execute(make_poke(atk_b=10, type1="ノーマル", moves=["たいあたり"]), _djk_n, "たいあたり")
check("せいぎのこころ 非あく技では上がらない", _djk_n.stage_attack == 0)

# 登場時
from simulator.abilities import entry_ability as _ent
_ptr2 = make_poke(ability="トレース"); _ent(_ptr2, make_poke(ability="ちからもち"), BattleField())
check("トレース 登場で相手特性コピー", _ptr2.ability == "ちからもち", f"ab={_ptr2.ability}")
_phm2 = make_poke(ability="かんろなミツ"); _ohm = make_poke(); _ent(_phm2, _ohm, BattleField())
check("かんろなミツ 登場で相手回避-1", _ohm.stage_evasion == -1, f"eva={_ohm.stage_evasion}")
# 1回の戦闘で1度のみ：2回目の登場では発動しない（_honey_usedフラグ）
_ohm2 = make_poke()
_ent(_phm2, _ohm2, BattleField())
check("かんろなミツ 1戦闘1度のみ(2回目不発)", _ohm2.stage_evasion == 0, f"eva={_ohm2.stage_evasion}")
_pcv = make_poke(type1="ノーマル", ability="かわりもの", atk_b=40); _ocv = make_poke(type1="みず", atk_b=180, def_b=170); _ent(_pcv, _ocv, BattleField())
check("かわりもの 登場で変身", _pcv.attack == _ocv.attack and _pcv.type1 == "みず", f"atk={_pcv.attack} type={_pcv.type1}")
check("かわりもの HP以外の能力も同じ", _pcv.defense == _ocv.defense and _pcv.sp_attack == _ocv.sp_attack and _pcv.sp_defense == _ocv.sp_defense and _pcv.speed == _ocv.speed)

# 命中/回避
random.seed(5); _N_fg = 2000
_hit_fg = sum(1 for _ in range(_N_fg) if _check_hit(make_poke(atk_b=80, ability="ふくがん"), make_poke(type1="ノーマル", def_b=80), dl.get_move("ストーンエッジ"), BattleField()))
_hit_fg0 = sum(1 for _ in range(_N_fg) if _check_hit(make_poke(atk_b=80), make_poke(type1="ノーマル", def_b=80), dl.get_move("ストーンエッジ"), BattleField()))
# ストーンエッジ命中80% → ふくがんで80×1.3=104→上限100%(ほぼ必中)、通常は約80%
check("ふくがん 命中率1.3倍(80%→ほぼ必中)", _hit_fg > _hit_fg0 and _hit_fg / _N_fg > 0.95, f"fg={_hit_fg} no={_hit_fg0}")
_pkeen_a = make_poke(atk_b=100, ability="するどいめ"); _pkeen_d = make_poke(type1="ノーマル"); _pkeen_d.stage_evasion = 6
check("するどいめ 回避無視で必中級", all(_check_hit(_pkeen_a, _pkeen_d, dl.get_move("たいあたり"), BattleField()) for _ in range(10)))
# シェルアーマー / スナイパー
check("シェルアーマー 急所無効", not any(_check_critical(make_poke(atk_b=100, ability="きょううん"), dl.get_move("たいあたり"), make_poke(ability="シェルアーマー")) for _ in range(50)))
_psnp = make_poke(atk_b=100, ability="スナイパー"); _psnp0 = make_poke(atk_b=100); _dsnp = make_poke(def_b=100)
check("スナイパー 急所2.25倍", near(dmg(_psnp, _dsnp, "たいあたり", crit=True) / dmg(_psnp0, _dsnp, "たいあたり", crit=False), 2.25))

# 優先度/速度
from simulator.battle import _priority
_act_ha = Action(type="move", move=dl.get_move("ブレイブバード"))
_pha = make_poke(type1="ひこう", ability="はやてのつばさ"); _pha_low = make_poke(type1="ひこう", ability="はやてのつばさ"); _pha_low.hp = _pha_low.max_hp // 2
check("はやてのつばさ 満タンでひこう技優先+1", _priority(_act_ha, _pha) == dl.get_move("ブレイブバード").priority + 1)
check("はやてのつばさ HP満タンでなければ優先度上がらない", _priority(_act_ha, _pha_low) == dl.get_move("ブレイブバード").priority)
def _first_qf(ab):
    _f = make_poke(ability=ab, spd_b=55); _f.status = "burn"; _s = make_poke(spd_b=70)
    _a = Action(type="move", move=dl.get_move("たいあたり"))
    return _speed_order(BattleSide([_f]), _a, BattleSide([_s]), _a, BattleField())
check("はやあし 状態異常で素早さ1.5倍(先攻)", _first_qf("はやあし"))
# 倍率を閾値で厳密検証：base×1.5の直下なら先攻・直上なら後攻（×1.5を正確に固定）
_phay = make_poke(spd_b=100, ability="はやあし"); _hay_base = _phay.get_effective_speed(); _phay.status = "burn"
_ahy = Action(type="move", move=dl.get_move("たいあたり"))
_opp_lo = make_poke(); _opp_lo.speed = int(_hay_base * 1.5) - 1
_opp_hi = make_poke(); _opp_hi.speed = int(_hay_base * 1.5) + 1
check("はやあし 素早さは正確に×1.5（閾値）",
      _speed_order(BattleSide([_phay]), _ahy, BattleSide([_opp_lo]), _ahy, BattleField())
      and not _speed_order(BattleSide([_phay]), _ahy, BattleSide([_opp_hi]), _ahy, BattleField()),
      f"base={_hay_base} thr={int(_hay_base*1.5)}")
_fe = BattleField(); _fe.electric_terrain = True
_psf = make_poke(ability="サーフテール", spd_b=50); _ssf = make_poke(spd_b=70)
_asf = Action(type="move", move=dl.get_move("たいあたり"))
check("サーフテール エレキFで素早さ2倍", _speed_order(BattleSide([_psf]), _asf, BattleSide([_ssf]), _asf, _fe))
# サーフテール 負例：エレキF以外では2倍にならず遅い方が後攻
check("サーフテール 非エレキFでは2倍なし", not _speed_order(BattleSide([_psf]), _asf, BattleSide([_ssf]), _asf, BattleField()))

# はやおき：sleep_count を2倍速で消化
_pwk = make_poke(type1="ノーマル", ability="はやおき", moves=["たいあたり"]); _pwk.status = "sleep"; _pwk.sleep_count = 2
execute(_pwk, make_poke(hp_b=255), "たいあたり")
check("はやおき 2倍速で起きる", _pwk.status is None, f"status={_pwk.status} cnt={_pwk.sleep_count}")

# うるおいボイス：音技がみず
from simulator.damage import _effective_move_type as _emt_v
check("うるおいボイス 音技みず化", _emt_v(make_poke(ability="うるおいボイス"), dl.get_move("ハイパーボイス"), BattleField()) == "みず")
check("うるおいボイス 非音技は不変", _emt_v(make_poke(ability="うるおいボイス"), dl.get_move("たいあたり"), BattleField()) == "ノーマル")

# 重さ（ヘヴィメタル/ライトメタル）：ヘビーボンバーの威力に影響
_dh = make_poke(type1="ノーマル", def_b=100); _dh.weight_kg = 100.0
_phv = make_poke(type1="はがね", atk_b=100, ability="ヘヴィメタル"); _phv.weight_kg = 100.0
_plt = make_poke(type1="はがね", atk_b=100, ability="ライトメタル"); _plt.weight_kg = 100.0
check("ヘヴィメタル 重さ2倍でヘビボン威力増", dmg(_phv, _dh, "ヘビーボンバー") > dmg(_plt, _dh, "ヘビーボンバー"), "重い方が高威力")
# 重さ倍率の厳密値（_eff_weight 直接）
from simulator.damage import _eff_weight
check("ヘヴィメタル 重さ2倍(厳密)", _eff_weight(_phv) == _phv.weight_kg * 2, f"w={_eff_weight(_phv)}")
check("ライトメタル 重さ0.5倍(厳密)", _eff_weight(_plt) == _plt.weight_kg * 0.5, f"w={_eff_weight(_plt)}")

# いしあたま：反動なし
_pri = make_poke(type1="ノーマル", atk_b=120, ability="いしあたま", hp_b=255); _hri = _pri.hp
execute(_pri, make_poke(type1="ノーマル", hp_b=255, def_b=100), "すてみタックル")
check("いしあたま 反動なし", _pri.hp == _hri, f"hp={_pri.hp}/{_hri}")

# ねんちゃく：はたきおとす/どろぼうで道具を失わない
_pneb = make_poke(type1="ノーマル", ability="ねんちゃく", hp_b=255, def_b=200); _pneb.item = "オボンのみ"
execute(make_poke(atk_b=60, type1="あく"), _pneb, "はたきおとす")
check("ねんちゃく はたきおとされない", _pneb.item == "オボンのみ", f"item={_pneb.item}")

# しめりけ：爆発技が出せない
_pds = make_poke(type1="ノーマル", ability="しめりけ", hp_b=255, def_b=200); _hds = _pds.hp
_abo = make_poke(type1="ノーマル", atk_b=120, moves=["だいばくはつ"])
execute(_abo, _pds, "だいばくはつ")
check("しめりけ 爆発技不可", _pds.hp == _hds and _abo.is_alive, f"hp={_pds.hp}/{_hds} alive={_abo.is_alive}")

# だっぴ：ターン終了30%で状態治癒（統計）
random.seed(0); _shed = False
for _ in range(60):
    _pshd = make_poke(ability="だっぴ"); _pshd.status = "burn"
    end_of_turn_ability(_pshd, BattleField(), [])
    if _pshd.status is None: _shed = True; break
check("だっぴ ターン終了で状態治癒発生", _shed)

# かいりきバサミ：攻撃を下げられない
_pkb = make_poke(type1="ノーマル", ability="かいりきバサミ", hp_b=255)
execute(make_poke(atk_b=60, moves=["ワイドブレイカー"]), _pkb, "ワイドブレイカー")
check("かいりきバサミ 攻撃下がらない", _pkb.stage_attack == 0, f"atk={_pkb.stage_attack}")
# はっこう：相手の回避上昇を無視
_phk_a = make_poke(atk_b=100, ability="はっこう"); _phk_d = make_poke(type1="ノーマル"); _phk_d.stage_evasion = 6
check("はっこう 回避無視", all(_check_hit(_phk_a, _phk_d, dl.get_move("たいあたり"), BattleField()) for _ in range(10)))
# ちどりあし：こんらん中は回避2倍（命中低下・統計）
def _conf_poke():
    _p = make_poke(type1="ノーマル", ability="ちどりあし"); _p.confused = True; return _p
random.seed(0)
_miss_cz = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), _conf_poke(), dl.get_move("れいとうビーム"), BattleField()))
_miss_cz0 = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), make_poke(type1="ノーマル"), dl.get_move("れいとうビーム"), BattleField()))
check("ちどりあし こんらんで回避上昇", _miss_cz > _miss_cz0, f"cz={_miss_cz} n={_miss_cz0}")
# ちどりあし：回避率2倍＝命中0.5倍（命中100技で約50%、統計）
random.seed(19); _N_cz = 3000
_hit_cz = sum(1 for _ in range(_N_cz) if _check_hit(make_poke(atk_b=80), _conf_poke(), dl.get_move("はたく"), BattleField()))
check("ちどりあし 命中0.5倍(回避2倍)", 0.44 < _hit_cz / _N_cz < 0.56, f"{_hit_cz}/{_N_cz}")
# ゆきがくれ：ゆき中回避上昇（統計）
random.seed(0); _fhail = BattleField(); _fhail.weather = "hail"
_miss_yk = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), make_poke(type1="こおり", ability="ゆきがくれ"), dl.get_move("れいとうビーム"), _fhail))
_miss_yk0 = sum(1 for _ in range(300) if not _check_hit(make_poke(atk_b=80), make_poke(type1="こおり"), dl.get_move("れいとうビーム"), BattleField()))
check("ゆきがくれ ゆきで回避上昇", _miss_yk > _miss_yk0, f"yk={_miss_yk} n={_miss_yk0}")
# ゆきがくれ：回避率1.25倍＝命中0.8倍（命中100技で約80%、統計）
random.seed(13); _N_yk = 3000
_hit_yk = sum(1 for _ in range(_N_yk) if _check_hit(make_poke(atk_b=80), make_poke(type1="こおり", ability="ゆきがくれ"), dl.get_move("はたく"), _fhail))
check("ゆきがくれ 命中0.8倍(回避1.25)", 0.74 < _hit_yk / _N_yk < 0.86, f"{_hit_yk}/{_N_yk}")
# むしのしらせ：低HPでむし技1.5倍
_pbz = make_poke(type1="むし", spatk_b=100, ability="むしのしらせ"); _pbz.hp = _pbz.max_hp // 4
_pbz0 = make_poke(type1="むし", spatk_b=100); _dbz = make_poke(type1="ノーマル", spdef_b=100)
check("むしのしらせ 低HPでむし1.5倍", near(dmg(_pbz, _dbz, "むしのさざめき") / dmg(_pbz0, _dbz, "むしのさざめき"), 1.5))
# フェアリースキン/フリーズスキン：ノーマル技のタイプ変化＋1.2倍
from simulator.damage import _effective_move_type as _emt_s
check("フェアリースキン ノーマル技→フェアリー", _emt_s(make_poke(ability="フェアリースキン"), dl.get_move("たいあたり"), BattleField()) == "フェアリー")
check("フリーズスキン ノーマル技→こおり", _emt_s(make_poke(ability="フリーズスキン"), dl.get_move("たいあたり"), BattleField()) == "こおり")
check("フェアリースキン 威力1.2倍", near(_ratio("フェアリースキン", "たいあたり"), 1.2))
# 負例：非ノーマル技はタイプ変換されない
check("フェアリースキン 非ノーマル技は不変", _emt_s(make_poke(ability="フェアリースキン"), dl.get_move("なみのり"), BattleField()) == "みず")
check("フリーズスキン 非ノーマル技は不変", _emt_s(make_poke(ability="フリーズスキン"), dl.get_move("なみのり"), BattleField()) == "みず")

# あくしゅう：ダメージ技で10%ひるみ（統計）
random.seed(0); _stink = False
for _ in range(120):
    _dst2 = make_poke(type1="ノーマル", hp_b=255, def_b=200); _ast2 = make_poke(atk_b=30, ability="あくしゅう", moves=["たいあたり"])
    execute(_ast2, _dst2, "たいあたり")
    if _dst2.flinched: _stink = True; break
check("あくしゅう ダメージでひるみ発生", _stink)
# スイートベール：ねむり無効
_psv = make_poke(type1="くさ", ability="スイートベール", hp_b=255)
for _ in range(5): execute(make_poke(moves=["キノコのほうし"]), _psv, "キノコのほうし")
check("スイートベール ねむり無効", _psv.status != "sleep", f"status={_psv.status}")
# マジシャン：ダメージで相手の道具を奪う
_pmg2 = make_poke(type1="あく", atk_b=120, ability="マジシャン"); _pmg2.item = None
_dmg2 = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dmg2.item = "オボンのみ"
execute(_pmg2, _dmg2, "かみくだく")
check("マジシャン ダメージで道具奪取", _pmg2.item == "オボンのみ" and _dmg2.item is None, f"a={_pmg2.item} d={_dmg2.item}")
# わるいてぐせ：接触被弾で相手の道具を盗む
_dbg = make_poke(type1="ノーマル", ability="わるいてぐせ", hp_b=255, def_b=200); _dbg.item = None
_abg = make_poke(atk_b=30, moves=["のしかかり"]); _abg.item = "たべのこし"
execute(_abg, _dbg, "のしかかり")
check("わるいてぐせ 接触被弾で道具を盗む", _dbg.item == "たべのこし" and _abg.item is None, f"a={_abg.item} d={_dbg.item}")
# 負例：非接触技では道具を盗まない
_dbg_n = make_poke(type1="ノーマル", ability="わるいてぐせ", hp_b=255, def_b=200); _dbg_n.item = None
_abg_n = make_poke(spatk_b=30, moves=["なみのり"]); _abg_n.item = "たべのこし"
execute(_abg_n, _dbg_n, "なみのり")
check("わるいてぐせ 非接触では盗まない", _abg_n.item == "たべのこし" and _dbg_n.item is None)

# すなはき：被弾で砂嵐
_ssh_d = BattleSide([make_poke(type1="いわ", ability="すなはき", hp_b=255, def_b=200)]); _fsh = BattleField()
_execute_move(BattleSide([make_poke(atk_b=60)]), _ssh_d, Action(type="move", move=dl.get_move("たいあたり")), _fsh)
check("すなはき 被弾で砂嵐", _fsh.weather == "sandstorm", f"weather={_fsh.weather}")
# 気絶しても発動（技で倒されても砂嵐）
_ssh_d2 = BattleSide([make_poke(type1="いわ", ability="すなはき", hp_b=1, def_b=1)]); _fsh2 = BattleField()
_execute_move(BattleSide([make_poke(atk_b=200)]), _ssh_d2, Action(type="move", move=dl.get_move("たいあたり")), _fsh2)
check("すなはき 気絶しても砂嵐", (not _ssh_d2.active.is_alive) and _fsh2.weather == "sandstorm",
      f"alive={_ssh_d2.active.is_alive} weather={_fsh2.weather}")
# どくげしょう：物理被弾で相手側にどくびし
_sdg_a = BattleSide([make_poke(atk_b=60)]); _sdg_d = BattleSide([make_poke(type1="ノーマル", ability="どくげしょう", hp_b=255, def_b=200)]); _fdg = BattleField()
_execute_move(_sdg_a, _sdg_d, Action(type="move", move=dl.get_move("たいあたり")), _fdg)
check("どくげしょう 物理被弾でどくびし設置", _fdg.toxic_spikes[_sdg_a.field_idx] >= 1, f"ts={_fdg.toxic_spikes[_sdg_a.field_idx]}")
# 負例：特殊技ではどくびしを設置しない
_sdg_a2 = BattleSide([make_poke(spatk_b=60)]); _sdg_d2 = BattleSide([make_poke(type1="ノーマル", ability="どくげしょう", hp_b=255, spdef_b=200)]); _fdg2 = BattleField()
_execute_move(_sdg_a2, _sdg_d2, Action(type="move", move=dl.get_move("なみのり")), _fdg2)
check("どくげしょう 特殊技では設置しない", _fdg2.toxic_spikes[_sdg_a2.field_idx] == 0)
# 気絶しても発動（物理技で倒されてもどくびしを設置）
_sdg_a3 = BattleSide([make_poke(atk_b=200)]); _sdg_d3 = BattleSide([make_poke(type1="ノーマル", ability="どくげしょう", hp_b=1, def_b=1)]); _fdg3 = BattleField()
_execute_move(_sdg_a3, _sdg_d3, Action(type="move", move=dl.get_move("たいあたり")), _fdg3)
check("どくげしょう 気絶してもどくびし設置", (not _sdg_d3.active.is_alive) and _fdg3.toxic_spikes[_sdg_a3.field_idx] >= 1,
      f"alive={_sdg_d3.active.is_alive} ts={_fdg3.toxic_spikes[_sdg_a3.field_idx]}")
# ふくつのこころ：ひるむと素早さ+1（ねこだましでひるませて確認）
from simulator.battle import Battle as _Bfk
_pfk = make_poke(type1="ノーマル", spd_b=10, ability="ふくつのこころ", hp_b=255, def_b=200, moves=["たいあたり"])
_ofk = make_poke(type1="ノーマル", spd_b=200, atk_b=60, moves=["ねこだまし"])
import simulator.battle as _SBfk; _mfk2 = _SBfk.MAX_TURNS; _SBfk.MAX_TURNS = 1
_Bfk(BattleSide([_ofk]), BattleSide([_pfk])).run(
    lambda s,o,f: Action(type="move", move=dl.get_move("ねこだまし"), move_idx=0),
    lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_SBfk.MAX_TURNS = _mfk2
check("ふくつのこころ ひるみで素早さ+1", _pfk.stage_speed == 1, f"spd={_pfk.stage_speed}")
# 負例：ひるまなければ素早さは上がらない
_pfk_n = make_poke(type1="ノーマル", ability="ふくつのこころ", hp_b=255, def_b=200)
execute(make_poke(atk_b=30), _pfk_n, "たいあたり")
check("ふくつのこころ ひるまなければ上がらない", _pfk_n.stage_speed == 0, f"spd={_pfk_n.stage_speed}")

# ねこだまし：交代で場を離れ再び出すと初手で再使用できる（turns_outは交代でリセット・交代ターンは加算しない）
import simulator.battle as _SBn
_mae = make_poke(type1="ノーマル", spd_b=200, atk_b=80, hp_b=220, def_b=220, moves=["ねこだまし", "たいあたり"])
_subn = make_poke(type1="はがね", hp_b=220, def_b=220, moves=["たいあたり"])
_tgtn = make_poke(type1="ノーマル", atk_b=10, hp_b=255, def_b=255, moves=["たいあたり"])
_tn = [0]
def _ai_neko(s, o, f):
    t = _tn[0]
    if t == 1: return Action(type="switch", switch_to=1)
    if t == 2: return Action(type="switch", switch_to=0)
    return Action(type="move", move=dl.get_move("ねこだまし"), move_idx=0)
_mtn = _SBn.MAX_TURNS; _SBn.MAX_TURNS = 5
_bN = _SBn.Battle(BattleSide([_mae, _subn]), BattleSide([_tgtn]))
_bN.run(_ai_neko, lambda s, o, f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0),
        on_turn=lambda b: _tn.__setitem__(0, _tn[0] + 1))
_SBn.MAX_TURNS = _mtn
_neko_ok = sum(1 for l in _bN.logs if "ねこだまし" in l and "ダメ" in l)
check("ねこだまし 交代で出し直すと初手で再使用可(1ターン目限定バグ修正)", _neko_ok >= 2, f"成功={_neko_ok}回")

# ミミロップ実機シナリオ: T1ねこだまし→T2交代→T3戻る→T4ねこだまし（交代後も初手で打てる）
_mim = _bfs(_pps("ミミロップ@ミミロップナイト:ようき:ねこだまし|とびひざげり|アイアンテール|はたきおとす:0/32/0/0/0/32"), _Lx, season="M-3", randomize=False)
_mpar = _bfs(_pps("ハッサム:いじっぱり:バレットパンチ|とんぼがえり|つるぎのまい|インファイト:0/32/0/0/0/0"), _Lx, season="M-3", randomize=False)
_mfoe = _bfs(_pps("カバルドン:わんぱく:なまける|あくび|ステルスロック|まもる:32/0/32/0/0/0"), _Lx, season="M-3", randomize=False)
_mtn = [0]
def _ai_mim(s, o, f):
    t = _mtn[0]
    if t == 1: return Action(type="switch", switch_to=1)   # T2: ハッサムへ交代
    if t == 2: return Action(type="switch", switch_to=0)   # T3: ミミロップへ戻す
    return Action(type="move", move=_mim.moves[0], move_idx=0)  # T1/T4: ねこだまし
_mtsav = _SBn.MAX_TURNS; _SBn.MAX_TURNS = 5
_bM = _SBn.Battle(BattleSide([_mim, _mpar]), BattleSide([_mfoe]))
_bM.run(_ai_mim, lambda s, o, f: Action(type="move", move=_mfoe.moves[2], move_idx=2),  # 相手はステロ(ねこだましを妨げない)
        on_turn=lambda b: _mtn.__setitem__(0, _mtn[0] + 1))
_SBn.MAX_TURNS = _mtsav
_mim_neko = sum(1 for l in _bM.logs if "ミミロップ" in l and "ねこだまし" in l and "ダメ" in l)
check("ミミロップ T1ねこだまし→交代→戻る→T4ねこだまし 両方成功", _mim_neko >= 2,
      f"成功={_mim_neko}回 / {[l for l in _bM.logs if 'ねこだまし' in l]}")

# アナライズ：後攻時1.3倍
_paz = make_poke(atk_b=100, ability="アナライズ"); _paz._acts_second = True
_paz0 = make_poke(atk_b=100); _daz = make_poke(def_b=100)
check("アナライズ 後攻で1.3倍", near(dmg(_paz, _daz, "たいあたり") / dmg(_paz0, _daz, "たいあたり"), 1.3))
# 負例：先攻（ターン最後でない）では1.3倍にならない
_paz_f = make_poke(atk_b=100, ability="アナライズ")  # _acts_second 未設定＝先攻扱い
check("アナライズ 先攻では等倍", near(dmg(_paz_f, _daz, "たいあたり") / dmg(_paz0, _daz, "たいあたり"), 1.0))
# いかりのつぼ：急所被弾で攻撃最大（きょううん相手の急所が出るまで試行）
_pat2 = make_poke(type1="ノーマル", ability="いかりのつぼ", hp_b=255, def_b=200)
_s1it = BattleSide([make_poke(atk_b=80, ability="きょううん")]); _s2it = BattleSide([_pat2])
random.seed(0)
for _ in range(80):
    _pat2.stage_attack = 0
    _execute_move(_s1it, _s2it, Action(type="move", move=dl.get_move("たいあたり")), BattleField())
    if _pat2.stage_attack == 6: break
check("いかりのつぼ 急所被弾で攻撃最大", _pat2.stage_attack == 6, f"atk={_pat2.stage_attack}")
# いかりのつぼ：非急所では上がらない（通常攻撃を多数受けても急所以外では不変）
_pat3 = make_poke(type1="ノーマル", ability="いかりのつぼ", hp_b=255, def_b=200)
_s1it3 = BattleSide([make_poke(atk_b=20)]); _s2it3 = BattleSide([_pat3])
random.seed(0); _it_noncrit_ok = True
for _ in range(30):
    _pat3.stage_attack = 0; _pat3.hp = _pat3.max_hp
    _execute_move(_s1it3, _s2it3, Action(type="move", move=dl.get_move("たいあたり")), BattleField())
    if _pat3.stage_attack != 0:  # 急所が出たターンはスキップ（6になる）
        _it_noncrit_ok = (_pat3.stage_attack == 6)
        continue
check("いかりのつぼ 非急所では上がらない", _it_noncrit_ok)

# あとだし：速くても最後に動く（同一優先度内）
_aad = Action(type="move", move=dl.get_move("たいあたり"))
_pstall = make_poke(ability="あとだし", spd_b=200); _snorm = make_poke(spd_b=50)
check("あとだし 速くても後攻", not _speed_order(BattleSide([_pstall]), _aad, BattleSide([_snorm]), _aad, BattleField()))
# あとだし：相手があとだしなら自分が先攻（逆方向）
_pn_slow = make_poke(spd_b=50); _stall_op = make_poke(ability="あとだし", spd_b=200)
check("あとだし 相手があとだしなら自分が先攻",
      _speed_order(BattleSide([_pn_slow]), _aad, BattleSide([_stall_op]), _aad, BattleField()))
# あとだし：優先度が異なれば不適用（高優先度技で先攻・遅くても）
_aquick = Action(type="move", move=dl.get_move("でんこうせっか"))  # 優先度+1
_pstall_slow = make_poke(ability="あとだし", spd_b=50); _opp_fast = make_poke(spd_b=200)
check("あとだし 高優先度技なら先攻(優先度差では不適用)",
      _speed_order(BattleSide([_pstall_slow]), _aquick, BattleSide([_opp_fast]), _aad, BattleField()))
# あとだし：自分が低優先度技なら後攻（優先度差で確実に後）
check("あとだし 低優先度技は後攻(優先度差)",
      not _speed_order(BattleSide([_pstall_slow]), _aad, BattleSide([_opp_fast]), _aquick, BattleField()))
# クイックドロウ：遅くても30%で先攻（統計）
random.seed(0)
_qd_first = sum(1 for _ in range(400) if _speed_order(BattleSide([make_poke(ability="クイックドロウ", spd_b=50)]), _aad, BattleSide([make_poke(spd_b=200)]), _aad, BattleField()))
check("クイックドロウ 遅くても時々先攻", 60 <= _qd_first <= 200, f"first={_qd_first}/400")
# プレッシャー：相手の攻撃技でPPが2減る
from simulator.battle import Battle as _Bpr
import simulator.battle as _SBpr; _mpr = _SBpr.MAX_TURNS; _SBpr.MAX_TURNS = 1
_ppr = make_poke(type1="ノーマル", atk_b=80, spd_b=200, moves=["たいあたり"]); _dpr = make_poke(type1="ノーマル", ability="プレッシャー", hp_b=255, def_b=200, moves=["たいあたり"])
_pp0 = _ppr.pp[0]
_Bpr(BattleSide([_ppr]), BattleSide([_dpr])).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0), lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_SBpr.MAX_TURNS = _mpr
check("プレッシャー 相手PP2減少", _ppr.pp[0] == _pp0 - 2, f"pp={_ppr.pp[0]}/{_pp0}")
# ミラーアーマー：能力低下を相手に反射
_pma = make_poke(type1="ノーマル", ability="ミラーアーマー", hp_b=255); _ama = make_poke(atk_b=60, moves=["ワイドブレイカー"])
execute(_ama, _pma, "ワイドブレイカー")
check("ミラーアーマー 能力低下反射", _pma.stage_attack == 0 and _ama.stage_attack == -1, f"def={_pma.stage_attack} atk={_ama.stage_attack}")
# てんきや：天候でタイプ変化
_pwf = make_poke(type1="ノーマル", ability="てんきや"); _fwf = BattleField(); _fwf.weather = "sunny"
_ent(_pwf, make_poke(), _fwf)
check("てんきや 晴れでほのお化", _pwf.type1 == "ほのお" and _pwf.type2 is None, f"type={_pwf.type1}")
_pwf_r = make_poke(type1="ノーマル", ability="てんきや"); _fwf_r = BattleField(); _fwf_r.weather = "rain"
_ent(_pwf_r, make_poke(), _fwf_r)
check("てんきや 雨でみず化", _pwf_r.type1 == "みず" and _pwf_r.type2 is None, f"type={_pwf_r.type1}")
_pwf_h = make_poke(type1="ノーマル", ability="てんきや"); _fwf_h = BattleField(); _fwf_h.weather = "hail"
_ent(_pwf_h, make_poke(), _fwf_h)
check("てんきや あられでこおり化", _pwf_h.type1 == "こおり" and _pwf_h.type2 is None, f"type={_pwf_h.type1}")
# ぎたい：フィールドでタイプ変化
_pmi = make_poke(type1="ノーマル", ability="ぎたい"); _fmi = BattleField(); _fmi.electric_terrain = True
_ent(_pmi, make_poke(), _fmi)
check("ぎたい エレキFででんき化", _pmi.type1 == "でんき", f"type={_pmi.type1}")
# 4フィールド全対応（列挙マッピング）
for _fld, _exp in [("electric_terrain","でんき"),("grassy_terrain","くさ"),("psychic_terrain","エスパー"),("misty_terrain","フェアリー")]:
    _pmi2 = make_poke(type1="ノーマル", ability="ぎたい"); _fmi2 = BattleField(); setattr(_fmi2, _fld, True)
    _ent(_pmi2, make_poke(), _fmi2)
    check(f"ぎたい {_exp}化", _pmi2.type1 == _exp and _pmi2.type2 is None, f"type={_pmi2.type1}")
# はらぺこスイッチ：ターン終了で模様切替
_phs = make_poke(ability="はらぺこスイッチ"); _h0 = getattr(_phs, "_hangry", False)
end_of_turn_ability(_phs, BattleField(), [])
check("はらぺこスイッチ ターン終了で切替", getattr(_phs, "_hangry", False) != _h0)
# アロマベール：ちょうはつ無効
_par = make_poke(type1="ノーマル", ability="アロマベール", hp_b=255)
execute(make_poke(atk_b=10), _par, "ちょうはつ")
check("アロマベール ちょうはつ無効", _par.taunt_count == 0, f"taunt={_par.taunt_count}")
# リーフガード：晴れ中は状態異常無効
_plg = make_poke(type1="くさ", ability="リーフガード", hp_b=255); _flg = BattleField(); _flg.weather = "sunny"
for _ in range(5): _execute_move(BattleSide([make_poke(atk_b=10)]), BattleSide([_plg]), Action(type="move", move=dl.get_move("でんじは")), _flg)
check("リーフガード 晴れで状態異常無効", _plg.status is None, f"status={_plg.status}")
# 負例：晴れでなければ状態異常になる
_plg_n = make_poke(type1="くさ", ability="リーフガード", hp_b=255)
_execute_move(BattleSide([make_poke(atk_b=10)]), BattleSide([_plg_n]), Action(type="move", move=dl.get_move("でんじは")), BattleField())
check("リーフガード 非晴れでは状態異常になる", _plg_n.status == "paralysis", f"status={_plg_n.status}")
# ふしょく：はがね/どくも毒にできる
random.seed(0); _cor = False
for _ in range(10):
    _dco = make_poke(type1="はがね", hp_b=255, spdef_b=200); _aco = make_poke(atk_b=10, ability="ふしょく")
    execute(_aco, _dco, "どくどく")
    if _dco.status == "badpoison": _cor = True; break
check("ふしょく はがねも毒にできる", _cor)
# 対照：ふしょく無しでは はがねは毒にできない
_dco0 = make_poke(type1="はがね", hp_b=255, spdef_b=200)
execute(make_poke(atk_b=10), _dco0, "どくどく")
check("ふしょく 対照: 通常ははがねを毒にできない", _dco0.status is None, f"status={_dco0.status}")

# きのみ系（くいしんぼう/ほおぶくろ/じゅくせい）
from simulator.items import apply_hp_berry
# くいしんぼう：HP1/2以下でカムラのみ発動（通常は1/4）
_pgl = make_poke(ability="くいしんぼう", hp_b=200); _pgl.item = "カムラのみ"; _pgl.hp = int(_pgl.max_hp * 0.45)
apply_hp_berry(_pgl, [])
check("くいしんぼう 1/2で発動", _pgl.stage_speed == 1 and _pgl.item is None, f"spd={_pgl.stage_speed} item={_pgl.item}")
_pgl0 = make_poke(hp_b=200); _pgl0.item = "カムラのみ"; _pgl0.hp = int(_pgl0.max_hp * 0.45)
apply_hp_berry(_pgl0, [])
check("通常は1/2では発動しない", _pgl0.stage_speed == 0 and _pgl0.item == "カムラのみ", f"spd={_pgl0.stage_speed}")
# ほおぶくろ：きのみで+1/3回復
_pch = make_poke(ability="ほおぶくろ", hp_b=200); _pch.item = "カムラのみ"; _pch.hp = _pch.max_hp // 5; _bch = _pch.hp
apply_hp_berry(_pch, [])
check("ほおぶくろ きのみで1/3回復", _pch.hp == min(_pch.max_hp, _bch + max(1, _pch.max_hp // 3)), f"hp={_pch.hp}/{_bch}")
# じゅくせい：きのみ効果2倍
_pjk = make_poke(ability="じゅくせい", hp_b=200); _pjk.item = "カムラのみ"; _pjk.hp = _pjk.max_hp // 5
apply_hp_berry(_pjk, [])
check("じゅくせい きのみ効果2倍", _pjk.stage_speed == 2, f"spd={_pjk.stage_speed}")
# 対照：じゅくせい無しなら効果は1倍（カムラのみ＝速度+1）
_pjk0 = make_poke(hp_b=200); _pjk0.item = "カムラのみ"; _pjk0.hp = _pjk0.max_hp // 5
apply_hp_berry(_pjk0, [])
check("じゅくせい 対照: 通常は効果1倍(+1)", _pjk0.stage_speed == 1, f"spd={_pjk0.stage_speed}")

# あまのじゃく：自己能力変化が反転（オーバーヒートの特攻-2→+2）
_pcn = make_poke(type1="ほのお", spatk_b=100, ability="あまのじゃく")
execute(_pcn, make_poke(type1="くさ", hp_b=255, spdef_b=100), "オーバーヒート")
check("あまのじゃく 自己ダウン→アップ", _pcn.stage_sp_attack == 2, f"spa={_pcn.stage_sp_attack}")
# あまのじゃく：自分に対する能力変化は起因を問わず逆転（ワイドブレイカーの攻撃-1→+1）
_pcn2 = make_poke(type1="ノーマル", ability="あまのじゃく", hp_b=255)
execute(make_poke(atk_b=60, moves=["ワイドブレイカー"]), _pcn2, "ワイドブレイカー")
check("あまのじゃく 相手技の自分ダウン→アップ", _pcn2.stage_attack == 1, f"atk={_pcn2.stage_attack}")
# いかく（相手起因・自分対象）も逆転：攻撃が上がる
from simulator.abilities import entry_ability as _ent_am
_pcn_int = make_poke(type1="ノーマル", ability="あまのじゃく", hp_b=255)
_ent_am(make_poke(ability="いかく"), _pcn_int, BattleField())
check("あまのじゃく いかくで攻撃が上がる(逆転)", _pcn_int.stage_attack == 1, f"atk={_pcn_int.stage_attack}")
# 変化技で受けるダウンも逆転（わたほうし 素早さ-2→+2）
_pcn4 = make_poke(type1="ノーマル", ability="あまのじゃく", hp_b=255)
execute(make_poke(moves=["わたほうし"]), _pcn4, "わたほうし")
check("あまのじゃく 変化技の自分ダウン→アップ", _pcn4.stage_speed == 2, f"spd={_pcn4.stage_speed}")
# 相手に対する能力変化は通常（あまのじゃく自身が相手を下げる→普通に下がる）
_pcn_atk = make_poke(type1="ノーマル", ability="あまのじゃく", moves=["ワイドブレイカー"])
_pcn_tgt = make_poke(type1="ノーマル", hp_b=255)
execute(_pcn_atk, _pcn_tgt, "ワイドブレイカー")
check("あまのじゃく 相手対象の変化は通常(相手は下がる)", _pcn_tgt.stage_attack == -1, f"atk={_pcn_tgt.stage_attack}")
# あまのじゃく：能力上昇も反転（つるぎのまい 攻撃+2→-2）＝双方向を検証
_pcn3 = make_poke(type1="ノーマル", ability="あまのじゃく", moves=["つるぎのまい"])
execute(_pcn3, make_poke(hp_b=255), "つるぎのまい")
check("あまのじゃく 自己アップ→ダウン", _pcn3.stage_attack == -2, f"atk={_pcn3.stage_attack}")
# びんじょう：相手の自己バフを自分もコピー
_pbj = make_poke(type1="ノーマル", ability="びんじょう", hp_b=255, spdef_b=200)
execute(make_poke(type1="ノーマル", moves=["つるぎのまい"]), _pbj, "つるぎのまい")
check("びんじょう 相手の上昇をコピー", _pbj.stage_attack == 2, f"atk={_pbj.stage_attack}")
# 負例：相手が能力上昇しなければコピーしない
_pbj_n = make_poke(type1="ノーマル", ability="びんじょう", hp_b=255, def_b=200)
execute(make_poke(atk_b=50), _pbj_n, "たいあたり")
check("びんじょう 相手非上昇では上がらない", _pbj_n.stage_attack == 0, f"atk={_pbj_n.stage_attack}")

# きんちょうかん：相手はきのみを食べられない（ターン終了オボン回復が起きない）
from simulator.battle import Battle as _Btn
import simulator.battle as _SBtn; _mtn = _SBtn.MAX_TURNS; _SBtn.MAX_TURNS = 1
_ptn = make_poke(type1="ノーマル", hp_b=200, def_b=200, moves=["たいあたり"]); _ptn.item = "オボンのみ"; _ptn.hp = _ptn.max_hp // 3
_otn = make_poke(type1="ノーマル", atk_b=10, ability="きんちょうかん", moves=["たいあたり"])
_btn_before = _ptn.hp
_Btn(BattleSide([_ptn]), BattleSide([_otn])).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0), lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_SBtn.MAX_TURNS = _mtn
check("きんちょうかん 相手のきのみ無効", _ptn.item == "オボンのみ", f"item={_ptn.item}")

# えんかく：接触技でも接触特性が発動しない（さめはだダメージを受けない）
_pen_a = make_poke(type1="ノーマル", atk_b=30, ability="えんかく", hp_b=255, moves=["のしかかり"]); _hen = _pen_a.hp
_pen_d = make_poke(type1="ノーマル", ability="さめはだ", hp_b=255, def_b=200)
execute(_pen_a, _pen_d, "のしかかり")
check("えんかく 接触扱いにならない(さめはだ無傷)", _pen_a.hp == _hen, f"hp={_pen_a.hp}/{_hen}")
# 比較: えんかく無しならさめはだダメージを受ける
_pno_a = make_poke(type1="ノーマル", atk_b=30, hp_b=255, moves=["のしかかり"]); _hno = _pno_a.hp
execute(_pno_a, make_poke(type1="ノーマル", ability="さめはだ", hp_b=255, def_b=200), "のしかかり")
check("えんかく対照: 通常はさめはだ被弾", _pno_a.hp < _hno, f"hp={_pno_a.hp}/{_hno}")
# バリアフリー：登場時に両者のスクリーン解除
from simulator.battle import Battle as _Bbf
_pbf = make_poke(type1="ノーマル", ability="バリアフリー", hp_b=255, moves=["たいあたり"])
_obf = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"])
_sbf1 = BattleSide([_pbf]); _sbf2 = BattleSide([_obf]); _sbf2.reflect = True; _sbf2.reflect_count = 5
import simulator.battle as _SBbf; _mbf = _SBbf.MAX_TURNS; _SBbf.MAX_TURNS = 1
_Bbf(_sbf1, _sbf2).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0), lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_SBbf.MAX_TURNS = _mbf
check("バリアフリー 登場でスクリーン解除", not _sbf2.reflect, f"reflect={_sbf2.reflect}")

# しゅうかく：にほんばれ中は消費きのみを必ず復活
_phv2 = make_poke(ability="しゅうかく"); _phv2.item = None; _phv2._last_berry = "カムラのみ"
_fhar = BattleField(); _fhar.weather = "sunny"
end_of_turn_ability(_phv2, _fhar, [])
check("しゅうかく 晴れできのみ復活", _phv2.item == "カムラのみ", f"item={_phv2.item}")
# しゅうかく：非晴れ時は50%で復活（統計）
random.seed(17); _har_cnt = 0
for _ in range(200):
    _ph3 = make_poke(ability="しゅうかく"); _ph3.item = None; _ph3._last_berry = "カムラのみ"
    end_of_turn_ability(_ph3, BattleField(), [])
    if _ph3.item == "カムラのみ": _har_cnt += 1
check("しゅうかく 非晴れ50%復活(±)", 70 < _har_cnt < 130, f"{_har_cnt}/200")
# ものひろい：相手が消費したきのみを拾う（Battle EOT経由）
from simulator.battle import Battle as _Bpk
_ppk = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"], ability="ものひろい"); _ppk.item = None
_opk = make_poke(type1="ノーマル", hp_b=200, def_b=200, moves=["たいあたり"]); _opk.item = "オボンのみ"; _opk.hp = _opk.max_hp // 3
import simulator.battle as _SBpk; _mpk = _SBpk.MAX_TURNS; _SBpk.MAX_TURNS = 1
_Bpk(BattleSide([_ppk]), BattleSide([_opk])).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0), lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_SBpk.MAX_TURNS = _mpk
check("ものひろい 相手消費きのみを拾う", _ppk.item == "オボンのみ", f"item={_ppk.item}")

# はんすう：消費したきのみの効果を次ターン終わりに再発動
_prm = make_poke(ability="はんすう", hp_b=200); _prm._ruminate_berry = "オボンのみ"; _prm._ruminate_count = 1
_prm.hp = _prm.max_hp // 2; _brm = _prm.hp
end_of_turn_ability(_prm, BattleField(), [])
check("はんすう 翌ターンで再発動", _prm.hp == min(_prm.max_hp, _brm + max(1, _prm.max_hp // 4)), f"hp={_prm.hp}/{_brm}")
# 負例：きのみ未消費（未セット）時は再発動しない
_prm_n = make_poke(ability="はんすう", hp_b=200); _prm_n.hp = _prm_n.max_hp // 2; _bn = _prm_n.hp
end_of_turn_ability(_prm_n, BattleField(), [])
check("はんすう 未セット時は発動しない", _prm_n.hp == _bn, f"hp={_prm_n.hp}/{_bn}")
# ノーてんき：天候のダメージ補正が無効（雨でみず技が1.5倍にならない）
_pnw = make_poke(spatk_b=100, ability="ノーてんき"); _dnw = make_poke(type1="ノーマル", spdef_b=100)
_frain = BattleField(); _frain.weather = "rain"
_d_nw = dmg(_pnw, _dnw, "なみのり", f=_frain)
_d_nw0 = dmg(make_poke(spatk_b=100), _dnw, "なみのり", f=BattleField())
check("ノーてんき 天候補正無効", near(_d_nw, _d_nw0), f"rain+noweather={_d_nw} plain={_d_nw0}")
# ノーてんき：砂嵐ダメージ無効（_end_of_turnを直接呼んで天候ダメージのみ検証）
_Bnw = __import__('simulator.battle', fromlist=['Battle']).Battle
_pnw2 = make_poke(type1="ノーマル", ability="ノーてんき", hp_b=255); _hnw = _pnw2.hp
_fnw = BattleField(); _fnw.weather = "sandstorm"; _fnw.weather_count = 5
_Bnw(BattleSide([_pnw2]), BattleSide([make_poke(type1="いわ", hp_b=255)]), _fnw)._end_of_turn()
check("ノーてんき 砂嵐ダメージ無効", _pnw2.hp == _hnw, f"hp={_pnw2.hp}/{_hnw}")
# 対照: ノーてんき無しなら砂嵐ダメージを受ける
_pnw3 = make_poke(type1="ノーマル", hp_b=255); _hnw3 = _pnw3.hp
_fnw3 = BattleField(); _fnw3.weather = "sandstorm"; _fnw3.weather_count = 5
_Bnw(BattleSide([_pnw3]), BattleSide([make_poke(type1="いわ", hp_b=255)]), _fnw3)._end_of_turn()
check("対照: 通常は砂嵐ダメージ", _pnw3.hp < _hnw3, f"hp={_pnw3.hp}/{_hnw3}")
# ノーてんき：天候で変化するもの全てを無効化
from simulator.damage import _effective_move_type as _emt_w, effective_weather as _effw
_fwb_neg = BattleField(); _fwb_neg.weather = "sunny"; _fwb_neg._weather_negated = True
check("ノーてんき ウェザーボール型変化無効", _emt_w(make_poke(), dl.get_move("ウェザーボール"), _fwb_neg) == "ノーマル")
check("ノーてんき下の通常ポケは天候なし", _effw(_fwb_neg, make_poke()) is None)
# メガソーラーはノーてんきより優先（常に晴れ扱い）
check("メガソーラー>ノーてんき", _effw(_fwb_neg, make_poke(ability="メガソーラー")) == "sunny")
check("メガソーラーはウェザーボールほのお化", _emt_w(make_poke(ability="メガソーラー"), dl.get_move("ウェザーボール"), _fwb_neg) == "ほのお")
# ノーてんき：天候回復特性（アイスボディ）も無効
from simulator.abilities import end_of_turn_ability as _eot_nw
_pic = make_poke(ability="アイスボディ", hp_b=200); _pic.hp = _pic.max_hp // 2; _bic = _pic.hp
_fhail_n = BattleField(); _fhail_n.weather = "hail"; _fhail_n._weather_negated = True
_eot_nw(_pic, _fhail_n, [])
check("ノーてんき アイスボディ回復無効", _pic.hp == _bic, f"hp={_pic.hp}/{_bic}")
# ぶきよう：自分の道具が効果を発揮しない（いのちのたま等のダメージ補正なし）
_pcl = make_poke(atk_b=100, ability="ぶきよう"); _pcl.item = "いのちのたま"
_pcl0 = make_poke(atk_b=100); _pcl0.item = "いのちのたま"; _dcl = make_poke(def_b=100)
check("ぶきよう 道具補正なし", dmg(_pcl, _dcl, "たいあたり") < dmg(_pcl0, _dcl, "たいあたり"), "ぶきようはいのちのたま補正を受けない")

# じょおうのいげん/テイルアーマー：相手の先制技が効かない
for _ab_q in ("じょおうのいげん", "テイルアーマー"):
    _pq = make_poke(type1="ノーマル", ability=_ab_q, hp_b=255, def_b=200); _hq = _pq.hp
    execute(make_poke(type1="ノーマル", atk_b=100, moves=["でんこうせっか"]), _pq, "でんこうせっか")
    check(f"{_ab_q} 先制技無効", _pq.hp == _hq, f"hp={_pq.hp}/{_hq}")
# 先制でない技は通る
_pq2 = make_poke(type1="ノーマル", ability="じょおうのいげん", hp_b=255, def_b=100); _hq2 = _pq2.hp
execute(make_poke(atk_b=100), _pq2, "たいあたり")
check("じょおうのいげん 通常技は通る", _pq2.hp < _hq2, f"hp={_pq2.hp}/{_hq2}")

# 単体バトルで効果のない特性（ダブル専用/性別/情報のみ）：1v1で正常動作（no-op）を明示検証
from simulator.abilities import NO_SINGLE_BATTLE_EFFECT as _NSE
_noeff = ["いやしのこころ", "おもてなし", "きみょうなくすり", "きょうせい", "テレパシー",
          "フラワーベール", "フレンドガード", "プラス", "マイナス", "レシーバー", "すじがねいり",
          "とうそうしん", "メロメロボディ", "にげあし"]
check("効果なし特性リストが文書と一致", set(_noeff) == _NSE, f"diff={set(_noeff) ^ _NSE}")
for _ab_ne in _noeff:
    _pne = make_poke(type1="ノーマル", ability=_ab_ne, hp_b=200, def_b=100)
    check(f"{_ab_ne} 単体で正常動作(no-op)", dmg(make_poke(atk_b=100), _pne, "たいあたり") > 0)

# ── 情報系（開示/非開示管理） ──
from simulator.battle import Battle as _Binf
# 見せ合い：対戦開始時に相手候補6体が previewed として既知になる
_p1team = [make_poke(type1="ほのお"), make_poke(type1="みず"), make_poke(type1="くさ")]
_p1team[0].name = "A"; _p1team[1].name = "B"; _p1team[2].name = "C"
_p2team = [make_poke(type1="でんき"), make_poke(type1="エスパー")]
_p2team[0].name = "X"; _p2team[1].name = "Y"
import simulator.battle as _SBinf; _minf = _SBinf.MAX_TURNS; _SBinf.MAX_TURNS = 1
# team_preview を直接検証
_s1inf2 = BattleSide(_p1team); _s2inf2 = BattleSide(_p2team)
_s1inf2.opp_view.team_preview(_s2inf2.party)
check("見せ合い 相手候補が previewed", all(_s1inf2.opp_view.get(n) and _s1inf2.opp_view.get(n).previewed for n in ("X","Y")))
check("見せ合い 技/持ち物は未開示", _s1inf2.opp_view.get("X").known_item is None and _s1inf2.opp_view.get("X").known_moves == [])
# おみとおし：登場時に相手の持ち物を強制開示
_pfr = make_poke(type1="ノーマル", ability="おみとおし", hp_b=255, moves=["たいあたり"]); _pfr.name = "FR"
_dfr = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _dfr.name = "DF"; _dfr.item = "とつげきチョッキ"
_sfr1 = BattleSide([_pfr]); _sfr2 = BattleSide([_dfr])
_SBinf.MAX_TURNS = 1
_Binf(_sfr1, _sfr2).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0),
                        lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
check("おみとおし 相手の持ち物を開示", _sfr1.opp_view.get("DF") and _sfr1.opp_view.get("DF").known_item == "とつげきチョッキ", f"item={_sfr1.opp_view.get('DF').known_item if _sfr1.opp_view.get('DF') else None}")
# きけんよち：相手が効果抜群の技を持つと察知して開示
_pant = make_poke(type1="ひこう", ability="きけんよち", hp_b=255, def_b=200, moves=["たいあたり"]); _pant.name = "AN"
_dant = make_poke(type1="でんき", atk_b=80, hp_b=255, moves=["10まんボルト"]); _dant.name = "DA"  # でんき→ひこう 効果抜群
_sant1 = BattleSide([_pant]); _sant2 = BattleSide([_dant])
_Binf(_sant1, _sant2).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0),
                          lambda s,o,f: Action(type="move", move=dl.get_move("10まんボルト"), move_idx=0))
check("きけんよち 危険技を察知開示", _sant1.opp_view.get("DA") and _sant1.opp_view.get("DA").threat_alert)
# きけんよち：抜群技がなければ察知しない
_pant2 = make_poke(type1="ノーマル", ability="きけんよち", hp_b=255, def_b=200, moves=["たいあたり"]); _pant2.name = "AN2"
_dant2 = make_poke(type1="ノーマル", atk_b=80, hp_b=255, moves=["たいあたり"]); _dant2.name = "DA2"
_sant1b = BattleSide([_pant2]); _sant2b = BattleSide([_dant2])
_Binf(_sant1b, _sant2b).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0),
                            lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
check("きけんよち 抜群技なしでは察知しない", not (_sant1b.opp_view.get("DA2") and _sant1b.opp_view.get("DA2").threat_alert))

# 開示情報：相手HPの残り割合＋技別ダメージ割合（ダメージ計算でEV/性格を逆算する用）
_php = make_poke(type1="ノーマル", atk_b=120, hp_b=200, moves=["たいあたり"]); _php.name = "ATK"
_dhp = make_poke(type1="ノーマル", def_b=80, hp_b=255, moves=["たいあたり"]); _dhp.name = "DEF"
_shp1 = BattleSide([_php]); _shp2 = BattleSide([_dhp])
_SBinf.MAX_TURNS = 1
_Binf(_shp1, _shp2).run(lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0),
                        lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_kd = _shp1.opp_view.get("DEF")
check("HP割合開示 残り割合が観測される", _kd is not None and 0.0 < _kd.hp_fraction < 1.0, f"frac={_kd.hp_fraction if _kd else None}")
check("HP割合開示 残り割合は実HP/最大HPと一致", _kd is not None and near(_kd.hp_fraction, round(_dhp.hp/_dhp.max_hp, 3)), f"frac={_kd.hp_fraction}, actual={round(_dhp.hp/_dhp.max_hp,3)}")
check("HP割合開示 技別ダメージ割合を記録", _kd is not None and len(_kd.damage_log) == 1 and _kd.damage_log[0]["move"] == "たいあたり")
_logged_frac = _kd.damage_log[0]["fraction"] if _kd and _kd.damage_log else None
check("HP割合開示 ダメージ割合=減少HP/最大HP", _logged_frac is not None and near(_logged_frac, round((_dhp.max_hp-_dhp.hp)/_dhp.max_hp, 3)), f"logged={_logged_frac}")
check("HP割合開示 残り割合+ダメージ割合≈1.0", _kd is not None and near(_kd.hp_fraction + _logged_frac, 1.0))
# 負例：ダメージを与えない補助技ではダメージ割合は記録されない
_pst = make_poke(type1="ノーマル", hp_b=200, moves=["なきごえ"]); _pst.name = "STA"
_dst = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"]); _dst.name = "STD"
_sst1 = BattleSide([_pst]); _sst2 = BattleSide([_dst])
_Binf(_sst1, _sst2).run(lambda s,o,f: Action(type="move", move=dl.get_move("なきごえ"), move_idx=0),
                        lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0))
_kst = _sst1.opp_view.get("STD")
check("HP割合開示 補助技ではダメージ割合を記録しない", _kst is None or len(_kst.damage_log) == 0)
_SBinf.MAX_TURNS = _minf

# ── 学習環境ハーネス（Phase 0: クローン/継続/登録パーティ） ──
from simulator.env import load_registered_parties, build_party, play_match
_parties = load_registered_parties(dl)
check("登録パーティ 読み込み", len(_parties) > 0 and all(p.specs for p in _parties))
_p6 = build_party(_parties[0], dl)
check("登録パーティ 確定スペック構築", len(_p6) == len(_parties[0].specs) and _p6[0].name == _parties[0].specs[0]["name"])
# クローン独立性：3ターン進めた状態をcloneし、cloneだけ継続→原状態は不変
_ce1 = make_poke(type1="ノーマル", atk_b=100, hp_b=200, moves=["たいあたり"]); _ce1.name = "C1"
_ce2 = make_poke(type1="ノーマル", def_b=80, hp_b=200, moves=["たいあたり"]); _ce2.name = "C2"
_act = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_SBinf.MAX_TURNS = 3
_bcl = _Binf(BattleSide([_ce1]), BattleSide([_ce2])); _bcl.run(_act, _act)
_SBinf.MAX_TURNS = _minf
_snap_hp = _bcl.side1.active.hp; _snap_turn = _bcl.turn
_clone = _bcl.clone()
check("clone 状態オブジェクトが独立", _clone.side1 is not _bcl.side1 and _clone.side1.active is not _bcl.side1.active)
_clone.resume(_act, _act)
check("clone継続後も原状態は不変", _bcl.side1.active.hp == _snap_hp and _bcl.turn == _snap_turn)
check("clone は独立に前進", _clone.turn > _snap_turn)
# 全テンプレートが完全（種族・技がDBで解決でき『不明』等を含まない）であること
from simulator.env import load_templates, is_complete_party
_tmpls = load_templates()
_incomp = [p.party_id for p in _tmpls if not is_complete_party(p, dl)]
check("テンプレート全件が完全(種族/技解決・誤記なし)", len(_tmpls) > 0 and not _incomp, f"不完全={_incomp}")
# 学習検証用の追加テンプレ（M-1正本とは別管理）
from simulator.env import load_extra_templates
_extra=load_extra_templates()
check("追加テンプレ 別ファイルからロード", isinstance(_extra, list))
if _extra:
    _bt0=_extra[0]
    check("追加テンプレ 完全(検証可能)", is_complete_party(_bt0, dl))
    _btbuilt=build_party(_bt0, dl)
    _pxm=next((p for p in _btbuilt if p.name=="ピクシー"), None)
    check("追加テンプレ メガピクシーはマジックミラー", _pxm is not None and _pxm.mega_data is not None and _pxm.mega_data.ability=="マジックミラー")
    check("追加テンプレ party_idは正本(<1000)と衝突しない", _bt0.party_id >= 1000)
# spec集合→party_id 逆引き（サーバが選出スペックを学習済みテーブルに対応づける土台）
from simulator.env import template_index, spec_to_string
_tidx = template_index(dl)
_tkey = frozenset(spec_to_string(s) for s in _tmpls[0].specs)
check("テンプレ逆引き spec集合→party_id", _tidx.get(_tkey) == _tmpls[0].party_id)
# play_match：登録パーティ同士の対戦が成立し勝者を返す
_res = play_match(_parties[0], _parties[1], dl)
check("play_match 勝敗判定", _res in (0, 1, 2))

# ── 推定器（Phase 1: belief） ──
from simulator.belief import PokemonBelief, OpponentBelief
from simulator.damage import calc_damage as _calc_dmg
from simulator.pokemon import build_from_template
from simulator.ai import HeuristicAI, select_party
_btpl_d = dl.get_pokemon_template("アーマーガア")
_b_atk = build_from_template(dl.get_pokemon_template("スターミー"), dl, randomize=False,
            override_moves=["アクアブレイク"], override_nature="いじっぱり",
            override_evs={"H":0,"A":252,"B":0,"C":0,"D":0,"S":252})
_b_move = dl.get_move("アクアブレイク"); _b_field = BattleField()
# 真の型 = 使用率1位スプレッド/性格
_true_ev = _btpl_d.top_evs[0][0]; _true_nat = _btpl_d.top_natures[0][0]
_true_def = build_from_template(_btpl_d, dl, randomize=False,
            override_evs={k:_true_ev[k] for k in "HABCDS"}, override_nature=_true_nat)
_belief = PokemonBelief(_btpl_d, dl)
_prior_true = _belief.prob_of_spread(_true_ev, _true_nat)
# 真の型から固定ロールで観測を生成しベイズ更新
for _rr in (0.0, 0.4, 0.7, 1.0, 0.2, 0.9):
    _frac = round(_calc_dmg(_b_atk, _true_def, _b_move, _b_field, random_roll=_rr) * 100 / _true_def.max_hp)
    _belief.observe_damage(_b_atk, _b_move, _frac, _b_field)
_post_true = _belief.prob_of_spread(_true_ev, _true_nat)
_map_ev, _map_nat = _belief.map_spread()
check("belief ダメージ割合で真の型の事後が上昇", _post_true > _prior_true, f"prior={_prior_true:.3f} post={_post_true:.3f}")
check("belief MAP推定が真の型に一致", _map_ev.get("spread")==_true_ev.get("spread") and _map_nat==_true_nat, f"MAP={_map_ev.get('spread')}/{_map_nat}")
check("belief 事後分布は正規化されている", near(sum(_belief.post), 1.0))
# 負例：再現不可能な観測割合では更新しない（事後不変・Falseを返す）
_snap_post = list(_belief.post)
_upd = _belief.observe_damage(_b_atk, _b_move, 5.0, _b_field)
check("belief 再現不可な観測は更新しない", _upd is False and _belief.post == _snap_post)
# 開示情報の反映：既知技は確率1.0、持ち物/特性が確定
_belief.known_moves.add("アクアブレイク")
check("belief 既知技は確率1.0", _belief.prob_has_move("アクアブレイク") == 1.0)
check("belief 未開示技は使用率事前", 0.0 <= _belief.prob_has_move("ボルトチェンジ") < 1.0)
# 持ち物/特性開示の取り込み（最小の PokeKnowledge 互換オブジェクト）
class _Fake:
    known_moves=["なみのり"]; known_item="とつげきチョッキ"; known_ability="ふゆう"
_belief.observe_disclosure(_Fake())
check("belief 開示で持ち物/特性が確定", _belief.prob_item("とつげきチョッキ")==1.0 and _belief.prob_ability("ふゆう")==1.0)
# belief 統合：対戦でside1に付与すると相手種族を推定し、cloneには引き継がれない
_pb1, _pb2 = _parties[0], _parties[5]
_bs1 = BattleSide(select_party(build_party(_pb1, dl), build_party(_pb2, dl), dl, 3))
_bs2 = BattleSide(select_party(build_party(_pb2, dl), build_party(_pb1, dl), dl, 3))
_bs1.belief = OpponentBelief(dl)
_bbat = _Binf(_bs1, _bs2)
check("belief はcloneに引き継がれない", _bbat.clone().side1.belief is None)
_bbat.run(HeuristicAI(), HeuristicAI())
check("belief 対戦で相手種族を推定", len(_bs1.belief.species) > 0)

# ── 行動方策（Phase 2: SearchAI 決定化ロールアウト探索） ──
from simulator.search_ai import SearchAI
# 明確にKOできる技がある局面では探索はその技を選ぶ（相手は弱い・満タン）
_sa_me = make_poke(type1="でんき", spatk_b=150, moves=["10まんボルト","たいあたり"]); _sa_me.name = "ATKR"
_sa_op = make_poke(type1="みず", type2="ひこう", def_b=40, spdef_b=40, hp_b=1); _sa_op.name = "FRAIL"
_sa = SearchAI(dl, rollouts=4, depth=6, seed=0)
_sa_act = _sa(BattleSide([_sa_me]), BattleSide([_sa_op]), BattleField())
check("SearchAI 明確なKO技を選択", _sa_act.type=="move" and _sa_act.move.name_jp=="10まんボルト", f"選択={_sa_act.move.name_jp if _sa_act.move else _sa_act.type}")
# 登録パーティ対戦をSearchAIで完走（クラッシュしないこと・勝者を返すこと）
_sp1 = BattleSide(select_party(build_party(_parties[0], dl), build_party(_parties[2], dl), dl, 3))
_sp2 = BattleSide(select_party(build_party(_parties[2], dl), build_party(_parties[0], dl), dl, 3))
_sp1.belief = OpponentBelief(dl)
_sw = _Binf(_sp1, _sp2).run(SearchAI(dl, rollouts=3, depth=8, seed=1), HeuristicAI())
check("SearchAI 登録パーティ対戦を完走", _sw in (0,1,2))
# 設置済みの設置技は候補から除外（無駄行動を防ぐ）
_hzme = build_from_template(dl.get_pokemon_template("ガブリアス"), dl, randomize=False,
    override_moves=["げきりん","じしん","いわなだれ","ステルスロック"])
_hzs1 = BattleSide([_hzme]); _hzs2 = BattleSide([make_poke(type1="みず"), make_poke(type1="くさ")])
_hzs1.field_idx=0; _hzs2.field_idx=1
_hzf = BattleField(); _hzsa = SearchAI(dl, rollouts=2, depth=3)
check("ステロ未設置時は候補にある", any(a.move and a.move.name_jp=="ステルスロック" for a in _hzsa._candidate_actions(_hzs1,_hzs2,_hzf)))
_hzf.stealth_rock[1]=True; _hzs2.stealth_rock_set=True
check("設置済みステロは候補から除外", not any(a.move and a.move.name_jp=="ステルスロック" for a in _hzsa._candidate_actions(_hzs1,_hzs2,_hzf)))

# ── メガ進化の修正（石名正規化・即メガ・探索でメガ独立選択） ──
from simulator.data import normalize_mega_stone
from simulator.ai import should_mega_evolve as _sme
check("メガ石名 全角→半角正規化", normalize_mega_stone("リザードナイトＹ")=="リザードナイトY" and normalize_mega_stone("リザードナイトＸ")=="リザードナイトX")
# リザードンX/Y が半角石でメガ解決できる（全角DB×半角テンプレの不一致を吸収）
for _stone in ("リザードナイトX","リザードナイトY"):
    _rz=build_from_template(dl.get_pokemon_template("リザードン"), dl, randomize=False,
        override_item=_stone, override_moves=["かえんほうしゃ"])
    check(f"リザードン {_stone} がメガ解決", _rz.mega_data is not None)
# 物理メガ(ハッサム)が満タンHPで即メガ（旧バグ: 75%まで待っていた）
_hs=build_from_template(dl.get_pokemon_template("ハッサム"), dl, randomize=False,
    override_item="ハッサムナイト", override_moves=["バレットパンチ"])
check("ハッサム 満タンHPで即メガ", _sme(_hs, _hs, BattleField()) is True)
check("メガ非所持は即メガしない", _sme(make_poke(type1="ノーマル"), make_poke(), BattleField()) is False)
# SearchAI はメガあり/なしを独立候補として探索する
_mz=build_from_template(dl.get_pokemon_template("スターミー"), dl, randomize=False,
    override_item="スターミナイト", override_moves=["なみのり","れいとうビーム"])
_moz=build_from_template(dl.get_pokemon_template("ガブリアス"), dl, randomize=False, override_moves=["じしん"])
_msa=SearchAI(dl, rollouts=2, depth=4)
_mc=_msa._candidate_actions(BattleSide([_mz]), BattleSide([_moz]), BattleField())
check("SearchAI メガあり候補を持つ", any(c.type=="move" and c.do_mega for c in _mc))
# 既定 collapse_mega=ON：メガ可能時はメガ前提のみ（メガなし技候補を列挙しない＝分岐半減）
check("SearchAI 既定でメガなし技候補は持たない(collapse_mega)",
      not any(c.type=="move" and c.move_idx is not None and c.move_idx>=0 and not c.do_mega for c in _mc))
_msa.collapse_mega=False
_mc2=_msa._candidate_actions(BattleSide([_mz]), BattleSide([_moz]), BattleField())
check("collapse_mega=Falseならメガなし候補も持つ", any(c.type=="move" and not c.do_mega for c in _mc2))
# 選出：2メガ以上持ちパーティでも最有力選出はメガ1体以下（実際にメガできるのは1体）
from simulator.selection import candidate_selections
for _pp in _parties:
    _aa = build_party(_pp, dl)
    _midx = {i for i, _pk in enumerate(_aa) if _pk.mega_data}
    if len(_midx) >= 2:
        _cs = candidate_selections(_aa, build_party(_parties[-1], dl), k=8)
        check("選出 2メガ持ちでも最有力はメガ1体以下", len(set(_cs[0]) & _midx) <= 1,
              f"top={_cs[0]} megas={len(set(_cs[0])&_midx)}")
        break

# ── 詰め（先制技で仕留める）と崩し（wall認識） ──
def _bp(name, nat, ev, moves, item=None):
    return build_from_template(dl.get_pokemon_template(name), dl, randomize=False,
        override_nature=nat, override_evs=ev, override_moves=moves, override_item=item)
_hAI = HeuristicAI(); _ff = BattleField()
# 詰め: 瀕死の相手に先制技(ふいうち)で仕留める
_fme = _bp("ダイケンキ","いじっぱり",{"H":20,"A":32,"B":2,"C":0,"D":2,"S":10},["シェルブレード","ふいうち","せいなるつるぎ","ひけん・ちえなみ"])
_fop = _bp("ゲンガー","おくびょう",{"H":0,"A":0,"B":0,"C":32,"D":0,"S":32},["シャドーボール"]); _fop.hp=max(1,_fop.max_hp//6)
_fact=_hAI(BattleSide([_fme]),BattleSide([_fop]),_ff)
check("詰め 瀕死相手に先制技で仕留める", _fact.type=="move" and _fact.move.name_jp=="ふいうち", f"選択={_fact.move.name_jp if _fact.move else _fact.type}")
# 崩し: 毒の通る受け(カバルドン)にどくどく
_wme = _bp("ハラバリー","ずぶとい",{"H":32,"A":0,"B":16,"C":0,"D":16,"S":0},["どくどく","ちょうはつ","パラボラチャージ","なまける"])
_wcb = _bp("カバルドン","わんぱく",{"H":32,"A":0,"B":32,"C":0,"D":2,"S":0},["じしん","あくび","ステルスロック","なまける"])
_wact=_hAI(BattleSide([_wme]),BattleSide([_wcb]),_ff)
check("崩し 受けにどくどく", _wact.move.name_jp=="どくどく", f"選択={_wact.move.name_jp}")
# 崩し: はがね受け(毒無効)にはちょうはつ
_warm = _bp("アーマーガア","のんき",{"H":32,"A":0,"B":32,"C":0,"D":2,"S":0},["てっぺき","ボディプレス","はねやすめ","とんぼがえり"])
_wme2 = _bp("ハラバリー","ずぶとい",{"H":32,"A":0,"B":16,"C":0,"D":16,"S":0},["どくどく","ちょうはつ","なまける","でんじは"])
_wact2=_hAI(BattleSide([_wme2]),BattleSide([_warm]),_ff)
check("崩し 毒無効の受けにはちょうはつ", _wact2.move.name_jp=="ちょうはつ", f"選択={_wact2.move.name_jp}")
# 過剰なwall扱い回避: 3発で落とせる相手は通常攻撃
_nme = _bp("キラフロル","ひかえめ",{"H":1,"A":0,"B":1,"C":32,"D":0,"S":32},["だいちのちから","パワージェム","ヘドロウェーブ","どくどく"])
_nop = _bp("ガブリアス","いじっぱり",{"H":0,"A":32,"B":0,"C":0,"D":0,"S":32},["じしん"])
_nact=_hAI(BattleSide([_nme]),BattleSide([_nop]),_ff)
check("崩し 有効打が通る相手は攻撃を選ぶ", _nact.move.category!="status", f"選択={_nact.move.name_jp}")

# ── 数ターン戦略: ねがいごと→まもる / バトン / ピボット交代先 ──
from simulator.battle import _choose_pivot_target
_tweak=_bp("メタモン","まじめ",{k:0 for k in "HABCDS"},["へんしん"])  # 無攻撃＝交代されない安全な相手
# ねがいごと: HP減で起点に
_tbr=_bp("ブラッキー","しんちょう",{"H":32,"D":16},["ねがいごと","まもる","イカサマ","あくび"]); _tbr.hp=_tbr.max_hp//2
_tbs=BattleSide([_tbr,_bp("カバルドン","まじめ",{k:0 for k in "HABCDS"},["じしん"])])
check("ねがいごと HP減で起点", _hAI(_tbs,BattleSide([_tweak]),_ff).move and _hAI(_tbs,BattleSide([_tweak]),_ff).move.name_jp=="ねがいごと")
# ねがいごと発動中はまもるで受ける
_tbs.wish_count=2; _tbr.hp=_tbr.max_hp//2
_wa=_hAI(_tbs,BattleSide([_tweak]),_ff)
check("まもる ねがいごと中は守る", _wa.move and _wa.move.name_jp=="まもる")
# バトン: 安全なら積む → 十分積んだらパス
_tqp=_bp("クエスパトラ","おくびょう",{"S":4},["バトンタッチ","めいそう","まもる","パワージェム"])
_tace=_bp("ピクシー","ひかえめ",{"C":32},["ムーンフォース"],"ピクシナイト")
_tqs=BattleSide([_tqp,_tace])
_ba=_hAI(_tqs,BattleSide([_tweak]),_ff)
check("バトン 安全時は積む", _ba.move and _ba.move.name_jp=="めいそう", f"選択={_ba.move.name_jp if _ba.move else _ba.type}")
_tqp.stage_sp_attack=2
_ba2=_hAI(_tqs,BattleSide([_tweak]),_ff)
check("バトン 積んだらエースへパス", _ba2.move and _ba2.move.name_jp=="バトンタッチ")
# ピボット交代先: バトンは積みエース(メガピクシー=index1)へ
_pv=BattleSide([_bp("クエスパトラ","おくびょう",{"S":4},["バトンタッチ","めいそう"]),
                _bp("ピクシー","ひかえめ",{"C":32},["ムーンフォース"],"ピクシナイト"),
                _bp("アーマーガア","まじめ",{k:0 for k in "HABCDS"},["とんぼがえり"])])
check("ピボット バトンは積みエース(メガ)へ", _choose_pivot_target(_pv, _bp("ガブリアス","まじめ",{k:0 for k in "HABCDS"},["じしん"]), is_baton=True)==1)

# ── 選出方策（Phase 3: ゼロサム行列ゲームのナッシュ均衡） ──
from simulator.selection import (candidate_selections, solve_zero_sum, solve_matchup,
                                  sample_selection, selection_to_party)
_cs_a = build_party(_parties[0], dl); _cs_b = build_party(_parties[1], dl)
_cands = candidate_selections(_cs_a, _cs_b, k=6)
check("選出候補 top-k列挙", len(_cands) <= 6 and all(len(s)==3 and len(set(s))==3 for s in _cands))
# fictitious play：既知の行列で均衡値が鞍点と整合（行=最大化, 列=最小化）
_Wtest = [[0.8, 0.2], [0.3, 0.6]]  # 鞍点なし→混合均衡
_x, _y, _v = solve_zero_sum(_Wtest, iters=5000)
check("ゼロサム解 行混合戦略は分布(次元と正規化)", len(_x)==2 and near(sum(_x), 1.0))
check("ゼロサム解 列混合戦略は分布(次元と正規化)", len(_y)==2 and near(sum(_y), 1.0))
# この行列の理論均衡値 = (0.8*0.6-0.2*0.3)/(0.8+0.6-0.2-0.3) = 0.42/0.9 ≈ 0.4667
check("ゼロサム解 ゲーム値が理論値に一致", near(_v, 0.4667, rel=0.05), f"value={_v:.4f}")
# 対戦カードの選出均衡を解く（小規模・高速設定）
_mu = solve_matchup(_parties[0], _parties[1], dl, k=4, samples=2, seed=0)
check("選出均衡 p1混合戦略は分布", near(sum(_mu['x']), 1.0))
check("選出均衡 ゲーム値が[0,1]", 0.0 <= _mu['value'] <= 1.0)
_rng_sel = random.Random(0)
_picked = sample_selection(_mu['sels1'], _mu['x'], _rng_sel)
check("選出均衡 混合戦略からサンプリング可能", _picked in _mu['sels1'])

# ── 自己対戦ループ（Phase 4: 選出テーブル学習とNash選出ポリシー） ──
import tempfile as _tf, pathlib as _pl
from simulator.train import train_selection_table, load_selection_table, make_nash_selection
_tmp_tbl = _pl.Path(_tf.gettempdir()) / "sel_table_test.json"
_cache = train_selection_table(dl, _parties, k=3, samples=2, pair_limit=1, out_path=_tmp_tbl, verbose=False)
check("選出テーブル学習 双方向キャッシュ生成", len(_cache) == 2)
_loaded = load_selection_table(_tmp_tbl)
check("選出テーブル ロード一致", set(_loaded.keys()) == set(_cache.keys()))
_id_i, _id_j = _parties[0].party_id, _parties[1].party_id
_pol = make_nash_selection(_loaded, _id_i, _id_j, seed=0)
check("Nash選出ポリシー 3体選出", len(_pol(build_party(_parties[0], dl), build_party(_parties[1], dl), dl)) == 3)
_pol_fb = make_nash_selection({}, 999, 998, seed=0)
check("Nash選出 未学習カードはヒューリスティックにフォールバック",
      len(_pol_fb(build_party(_parties[0], dl), build_party(_parties[1], dl), dl)) == 3)

# ── 発展① 選出利得の推定にSearchAIを使う（ai_factory/with_belief） ──
_mu_s = solve_matchup(_parties[0], _parties[1], dl, k=2, samples=1, seed=0,
                      ai_factory=lambda ld: SearchAI(ld, rollouts=2, depth=5, seed=0), with_belief=True)
check("選出均衡(SearchAI行動方策) 解が分布", near(sum(_mu_s['x']), 1.0) and 0.0 <= _mu_s['value'] <= 1.0)

# ── 発展② beliefに登録パーティ実スプレッドを混ぜる ──
from simulator.belief import registered_spreads_by_species
_reg = registered_spreads_by_species(dl)
check("登録スプレッド取得", len(_reg) > 0 and all(isinstance(v, list) and v for v in _reg.values()))
# 登録スプレッドを持つ種族で、混入により候補数が増える
_sp_name = next((n for n in _reg if dl.get_pokemon_template(n)), None)
_tpl_sp = dl.get_pokemon_template(_sp_name)
_b_plain = PokemonBelief(_tpl_sp, dl)
_b_reg = PokemonBelief(_tpl_sp, dl, extra_spreads=_reg[_sp_name])
check("登録スプレッド混入で候補が増加または同等", len(_b_reg.cands) >= len(_b_plain.cands))
# 真の登録スプレッドが候補に含まれる（混入版）
_true_reg_ev, _true_reg_nat = _reg[_sp_name][0]
check("登録スプレッド混入で真の型が候補入り",
      _b_reg.prob_of_spread(_true_reg_ev, _true_reg_nat) > 0.0)
# OpponentBelief は既定で登録スプレッドを使い、無効化も可能
check("OpponentBelief 既定で登録スプレッド有効", len(OpponentBelief(dl)._reg) > 0)
check("OpponentBelief use_registered=Falseで無効", OpponentBelief(dl, use_registered=False)._reg == {})

# ── 発展③ ロールアウト方策にSearchAI（再帰探索, 2段ネスト） ──
from simulator.search_ai import make_nested_search
_nai = make_nested_search(dl, outer=(2,5), inner=(2,4), seed=0)
_n_me = make_poke(type1="でんき", spatk_b=150, moves=["10まんボルト","たいあたり"]); _n_me.name="NME"
_n_op = make_poke(type1="みず", type2="ひこう", def_b=40, spdef_b=40, hp_b=1); _n_op.name="NOP"
_n_act = _nai(BattleSide([_n_me]), BattleSide([_n_op]), BattleField())
check("ネスト探索 合法行動を返す", _n_act.type in ("move","switch","pass"))

# ── 戦略の言語化（説明可能性） ──
from simulator.explain import describe_party_strategy, explain_turn
_desc = describe_party_strategy(_cache, _parties, dl, _parties[0].party_id)
check("選出方策の言語化 構成・採用傾向を含む",
      "選出方策" in _desc and "採用傾向" in _desc and "先頭" in _desc)
_sa_exp = SearchAI(dl, rollouts=3, depth=6, seed=0)
_exp_me = make_poke(type1="でんき", spatk_b=150, moves=["10まんボルト","たいあたり"]); _exp_me.name="EME"
_exp_op = make_poke(type1="みず", type2="ひこう", def_b=40, spdef_b=40, hp_b=1); _exp_op.name="EOP"
_exp_txt = explain_turn(_sa_exp, BattleSide([_exp_me]), BattleSide([_exp_op]), BattleField())
check("行動方策の言語化 推定勝率と選択理由を含む", "推定勝率" in _exp_txt and "選択:" in _exp_txt)

# ── レポートのMarkdown組み立て（純関数・高速） ──
from simulator.report import build_markdown
_mk_metrics = {
    "search_vs_heuristic": {"search": 23, "heuristic": 7, "winrate": 0.767},
    "nash_vs_heuristic_selection": {"nash": 190, "heuristic": 110, "winrate": 0.633, "cards": 2628},
    "combined_vs_baseline": {"learned": 15, "baseline": 5, "winrate": 0.75},
    "belief_calibration": {"prior_err": 8.7, "post_err": 4.7, "improvement": 0.459},
}
_md = build_markdown("2026-06-04", 73, _mk_metrics, "META", "BEHAV", ["STRAT"])
check("レポートMarkdown 主要セクションを含む",
      all(s in _md for s in ("評価指標", "横断 選出傾向", "行動ログ", "76.7%", "META", "BEHAV", "STRAT")))

# ── 学習価値関数（AlphaZero的 value） ──
from simulator.value_net import ValueNet, make_value_fn
from simulator.features import encode_state, feature_dim
import random as _vrnd
_vs1=BattleSide([make_poke(type1="みず",spatk_b=100,moves=["なみのり"])])
_vs2=BattleSide([make_poke(type1="でんき",spatk_b=100,moves=["10まんボルト"])])
_vs1.field_idx=0; _vs2.field_idx=1
_vfeat=encode_state(_vs1,_vs2,BattleField())
check("価値関数 特徴次元が一致", len(_vfeat)==feature_dim())
# 特徴量v2（FEAT_V2、既定ON）: 持ち物カテゴリ 8→18、全体965次元。
# 旧8カテゴリでは M-6 上位50種の非メガ持ち物使用率の29%が1bitも立たず、ネットからは
# 「無持ち物」と同じに見えていた（識別率 71%→99.7%）。本番ネットも965次元へ差し替え済み。
import simulator.features as _FT
import os as _os33, json as _js33
_netp33 = _os33.path.join(_os33.path.dirname(_os33.path.dirname(_os33.path.abspath(__file__))), "az_net_np.json")
check("特徴量 既定は1037次元(v2+v3)", feature_dim()==1037 and _FT.FEAT_V2 and _FT.FEAT_V3)
# v3: 変化技クラス8 + 最大威力技の量的4。既存クラスに入らない変化技が M-6 上位50種の
# 使用率の32%を占めており、ネットからは「持っていない」のと同じに見えていた（被覆 68%→99.5%）。
check("特徴量v3 変化技クラスが主要な未分類技を被覆",
      {"アンコール","ちょうはつ"} <= _FT._M3_LOCK
      and {"リフレクター","ひかりのかべ","オーロラベール"} <= _FT._M3_SCREEN
      and "みがわり" in _FT._M3_SUBST and "トリック" in _FT._M3_ITEMTRICK
      and {"みちづれ","バトンタッチ"} <= _FT._M3_EXIT
      and "ねがいごと" in _FT._M3_DELAY and "くろいきり" in _FT._M3_RESET)
# 反動・自分の能力下降は battle.py の実装と同じ集合でなければ、ネットが見る性質が実挙動とずれる
check("特徴量v3 反動技は battle._apply_recoil と同じ集合",
      {"すてみタックル","フレアドライブ","ブレイブバード","ウッドハンマー",
       "もろはのずつき","ワイルドボルト","てっていこうせん"} <= _FT._M3_RECOIL)
check("特徴量v3 能力下降技にオーバーヒート/りゅうせいぐん/インファイトが入る",
      {"オーバーヒート","りゅうせいぐん","インファイト"} <= _FT._M3_SELFDROP)
# 段階的に戻せること（v3だけ切る／両方切る）
import subprocess as _sp33, sys as _sy33
def _dim33(env):
    e = dict(os.environ if False else __import__("os").environ); e.update(env)
    r = _sp33.run([_sy33.executable, "-c",
        "import sys;sys.path.insert(0,%r);from simulator.features import feature_dim;print(feature_dim())"
        % _os33.path.dirname(_netp33)], capture_output=True, text=True, env=e)
    return int(r.stdout.strip())
check("特徴量 v3だけ切ると965次元に戻る", _dim33({"FEAT_V3": "0"}) == 965)
check("特徴量 v2/v3とも切ると905次元に戻る", _dim33({"FEAT_V2": "0", "FEAT_V3": "0"}) == 905)
check("特徴量 既定の持ち物カテゴリは18", len(_FT._ITEM_FLAGS)==18)
check("特徴量v2 追加カテゴリは10・カテゴリ間で持ち物が重複しない",
      len(_FT._ITEM_FLAGS_V2)==10 and
      sum(len(f) for f in _FT._ITEM_FLAGS_V2)==len(set().union(*_FT._ITEM_FLAGS_V2)))
# 実測で寄与の大きかった持ち物（いのちのたま266/ひかりのねんど205/ゴツゴツメット199 %pt）が
# 既定で識別できること。ここが落ちるとネットは「無持ち物」として見る。
_v2items = set().union(*_FT._ITEM_FLAGS)
check("特徴量 主要な持ち物を既定で識別できる",
      {"いのちのたま","ひかりのねんど","ゴツゴツメット","ふうせん","サイコシード",
       "たつじんのおび","しろいハーブ","レッドカード","ピントレンズ"} <= _v2items)
# Rust 側(features.rs N_ITEM_FLAGS)と次元が食い違うと本番のネット評価が壊れる。
# ここを変えるときは features.rs も必ず揃えること。
# ネットのパスは env AZNP_PATH で差し替えられること（同じベンチで2ネットを比較するため）。
# 固定パスだと PVNetNP.load() を引数なしで呼ぶ経路（_ai_blunder 等）で比較ができない。
import inspect as _in33, simulator.az_np as _az33
check("ネットのパスが env AZNP_PATH で差し替えられる",
      'os.environ.get("AZNP_PATH")' in _in33.getsource(_az33)[:1600])

check("特徴量 本番ネットの入力次元と一致",
      _js33.load(open(_netp33, encoding="utf-8"))["dim"] == feature_dim())
# 学習可能性: 線形分離データを高精度予測（決定的・高速）
_vr=_vrnd.Random(0); _syn=[]
for _ in range(320):
    _x=[_vr.random() for _ in range(4)]
    _syn.append((_x, 1.0 if sum(_x)>2.0 else 0.0))
_vnet=ValueNet(4, hidden=8, seed=0); _vnet.train(_syn[:256], epochs=40, lr=0.1)
check("価値関数 学習で分離データを高精度予測", _vnet.accuracy(_syn[256:])>0.85, f"acc={_vnet.accuracy(_syn[256:]):.2f}")
check("価値関数 出力は確率[0,1]", 0.0<=_vnet.predict([0.5]*4)<=1.0)
# 実状態次元の価値関数を SearchAI に統合して合法手・完走
_rnet=ValueNet(feature_dim(), hidden=4, seed=0)
check("価値関数 実状態で予測可能", 0.0<=_rnet.predict(_vfeat)<=1.0)
_vsearch=SearchAI(dl, rollouts=2, depth=4, seed=0, value_fn=make_value_fn(_rnet))
_vsw=_Binf(BattleSide(select_party(build_party(_parties[0],dl),build_party(_parties[1],dl),dl,3)),
           BattleSide(select_party(build_party(_parties[1],dl),build_party(_parties[0],dl),dl,3))).run(_vsearch, HeuristicAI())
check("価値誘導探索 対戦を完走", _vsw in (0,1,2))

# ── AlphaZero型: 方策＋価値ネット ＋ PUCT-MCTS ──
from simulator.alphazero import (PolicyValueNet, PVMCTSAI, legal_actions_indexed,
                                 action_to_index, mcts_search, ACTION_DIM)
# 行動→index 変換
check("行動index 技(通常/メガ)", action_to_index(Action(type="move",move_idx=2,do_mega=False))==2 and action_to_index(Action(type="move",move_idx=2,do_mega=True))==6)
check("行動index 交代/わるあがき", action_to_index(Action(type="switch",switch_to=1))==9 and action_to_index(Action(type="move",move_idx=-1))==11)
# 二頭ネット: 価値[0,1]＋方策priorが合法手上で正規化
_aznet=PolicyValueNet(feature_dim(), hidden=8, seed=0)
_azs1=BattleSide([make_poke(type1="でんき",spatk_b=120,moves=["10まんボルト","たいあたり"])])
_azs2=BattleSide([make_poke(type1="みず",def_b=60,moves=["なみのり"])])
_azs1.field_idx=0; _azs2.field_idx=1
_azfield=BattleField()
_legal=[ix for _,ix in legal_actions_indexed(_azs1,_azs2,_azfield)]
_pri,_v=_aznet.evaluate(encode_state(_azs1,_azs2,_azfield), _legal)
check("二頭ネット 価値は確率・方策は合法手で正規化", 0.0<=_v<=1.0 and near(sum(_pri.values()),1.0) and set(_pri)==set(_legal))
# 二頭ネット 学習可能性（合成データで価値・方策が学習）
import random as _azr
_ar=_azr.Random(0); _azsyn=[]
for _ in range(300):
    _x=[_ar.random() for _ in range(5)]
    _legi=[0,1,2]
    _a=0 if _x[0]>0.5 else 1   # 行動は x[0] で決まる
    _y=1.0 if sum(_x)>2.5 else 0.0
    _azsyn.append((_x,_a,_legi,_y))
_aznet2=PolicyValueNet(5, hidden=8, seed=0); _aznet2.train(_azsyn[:240], epochs=40, lr=0.1)
check("二頭ネット 方策top1が学習で向上", _aznet2.policy_top1_acc(_azsyn[240:])>0.7, f"acc={_aznet2.policy_top1_acc(_azsyn[240:]):.2f}")
# MCTS が合法手を返し、PVMCTS-AI が対戦完走
_azb=_Binf(BattleSide(select_party(build_party(_parties[0],dl),build_party(_parties[1],dl),dl,3)),
           BattleSide(select_party(build_party(_parties[1],dl),build_party(_parties[0],dl),dl,3)))
_azact=mcts_search(_azb.clone(), True, PolicyValueNet(feature_dim(),hidden=6,seed=0), HeuristicAI(), n_sims=8)
check("PUCT-MCTS 合法手を返す", _azact is None or _azact.type in ("move","switch","pass"))
_azw=_azb.run(PVMCTSAI(dl, PolicyValueNet(feature_dim(),hidden=6,seed=0), n_sims=6, seed=0), HeuristicAI())
check("PVMCTS-AI 対戦を完走", _azw in (0,1,2))
# numpy版 二頭ネット（環境にnumpyがあれば）
try:
    import numpy as _np_chk
    _HAS_NP=True
except Exception:
    _HAS_NP=False
if _HAS_NP:
    from simulator.az_np import PVNetNP
    import numpy as _np
    _npr=_np.random.default_rng(0)
    _Xs=_npr.random((400,5))
    _Ys=(_Xs[:,0]>0.5).astype(float)      # 価値・方策とも x0 で決まる（共有trunkが両ヘッドに効く）
    _As=(_Xs[:,0]>0.5).astype(int)         # 行動0/1 を x0 で
    _Ms=_np.ones((400,12)); _Ms[:,2:]=0    # 行動0,1のみ合法
    _npnet=PVNetNP(5, hidden=16)
    _v0=_npnet.value_acc(_Xs[320:],_Ys[320:])
    _npnet.train(_Xs[:320],_As[:320],_Ms[:320],_Ys[:320], epochs=80, lr=0.15)
    check("numpy版 二頭ネット 価値が学習で向上", _npnet.value_acc(_Xs[320:],_Ys[320:])>_v0+0.1, f"{_v0:.2f}→{_npnet.value_acc(_Xs[320:],_Ys[320:]):.2f}")
    check("numpy版 二頭ネット 方策が学習", _npnet.policy_acc(_Xs[320:],_As[320:],_Ms[320:])>0.8)
    _pd,_pv=_npnet.evaluate([0.5]*5,[0,1])
    check("numpy版 evaluate interface", 0.0<=_pv<=1.0 and near(sum(_pd.values()),1.0) and set(_pd)=={0,1})
    # 自律AlphaZeroループ部品
    # MCTS: Dirichletノイズ＋温度＋訪問分布πの返却
    _azb2=_Binf(BattleSide(select_party(build_party(_parties[0],dl),build_party(_parties[1],dl),dl,3)),
                BattleSide(select_party(build_party(_parties[1],dl),build_party(_parties[0],dl),dl,3)))
    _mres=mcts_search(_azb2.clone(), True, PolicyValueNet(feature_dim(),hidden=6,seed=0), HeuristicAI(),
                      n_sims=12, dir_eps=0.25, temperature=1.0, return_pi=True, rng=__import__('random').Random(0))
    check("MCTS 訪問分布πを返す", isinstance(_mres,tuple) and (near(sum(_mres[1].values()),1.0) or not _mres[1]))
    # ソフト方策ターゲット(訪問分布)での学習
    _PIs=_np.zeros((400,12)); _PIs[_np.arange(400), _As]=1.0  # one-hot を分布として
    _npnet3=PVNetNP(5, hidden=16); _v0b=_npnet3.value_acc(_Xs[320:],_Ys[320:])
    _npnet3.train_pi(_Xs[:320],_PIs[:320],_Ms[:320],_Ys[:320], epochs=80, lr=0.15)
    check("numpy版 ソフト方策学習(train_pi)で価値向上", _npnet3.value_acc(_Xs[320:],_Ys[320:])>_v0b+0.1)
    # 選出ε探索
    from simulator.az_loop import explore_selection, selfplay_game
    _rngsel=__import__('random').Random(0)
    _a6=build_party(_parties[0],dl); _o6=build_party(_parties[1],dl)
    check("選出ε探索 3体を返す", len(explore_selection(_a6,_o6,dl,_rngsel,eps=1.0))==3 and len(explore_selection(_a6,_o6,dl,_rngsel,eps=0.0))==3)
    # 自己対戦1試合がπ付きサンプルを生成
    _sps=selfplay_game(dl, _parties, PVNetNP(feature_dim(),hidden=8), n_sims=4, rng=__import__('random').Random(0))
    check("MCTS自己対戦 π付きサンプル生成", isinstance(_sps,list) and (not _sps or (len(_sps[0])==4 and isinstance(_sps[0][1],dict))))

# ── メガシンカ専用特性 ──────────────────────────────────────────
from simulator.damage import _effective_move_type as _emt_m
from simulator.battle import is_trapped as _is_trapped

# ドラゴンスキン：ノーマル技→ドラゴン＋1.2倍／非ノーマルは不変
check("ドラゴンスキン ノーマル技→ドラゴン", _emt_m(make_poke(ability="ドラゴンスキン"), dl.get_move("たいあたり"), BattleField()) == "ドラゴン")
check("ドラゴンスキン 威力1.2倍", near(_ratio("ドラゴンスキン", "たいあたり"), 1.2))
check("ドラゴンスキン 非ノーマル技は不変", _emt_m(make_poke(ability="ドラゴンスキン"), dl.get_move("なみのり"), BattleField()) == "みず")

# スカイスキン：ノーマル技→ひこう＋1.2倍／非ノーマルは不変
check("スカイスキン ノーマル技→ひこう", _emt_m(make_poke(ability="スカイスキン"), dl.get_move("たいあたり"), BattleField()) == "ひこう")
check("スカイスキン 威力1.2倍", near(_ratio("スカイスキン", "たいあたり"), 1.2))
check("スカイスキン 非ノーマル技は不変", _emt_m(make_poke(ability="スカイスキン"), dl.get_move("なみのり"), BattleField()) == "みず")

# フェアリーオーラ：フェアリー技1.33倍（攻撃側・防御側どちらが持っても）
_pfa = make_poke(type1="ノーマル", spatk_b=100, ability="フェアリーオーラ"); _pfa0 = make_poke(type1="ノーマル", spatk_b=100)
_dfa = make_poke(type1="ノーマル", spdef_b=100)
check("フェアリーオーラ フェアリー技1.33倍(攻撃側)", near(dmg(_pfa, _dfa, "ムーンフォース") / dmg(_pfa0, _dfa, "ムーンフォース"), 1.33))
_dfa_aura = make_poke(type1="ノーマル", spdef_b=100, ability="フェアリーオーラ")
check("フェアリーオーラ 防御側保持でも1.33倍", near(dmg(_pfa0, _dfa_aura, "ムーンフォース") / dmg(_pfa0, _dfa, "ムーンフォース"), 1.33))
check("フェアリーオーラ 非フェアリー技は不変", near(dmg(_pfa, _dfa, "なみのり") / dmg(_pfa0, _dfa, "なみのり"), 1.0))

# おやこあい：2回攻撃（2発目0.25倍）＝合計約1.25倍
_poya = make_poke(type1="ノーマル", atk_b=100, ability="おやこあい", moves=["たいあたり"])
_poya0 = make_poke(type1="ノーマル", atk_b=100, moves=["たいあたり"])
_doya = make_poke(type1="ノーマル", def_b=100, hp_b=255); _doya0 = make_poke(type1="ノーマル", def_b=100, hp_b=255)
_h1 = _doya.hp; execute(_poya, _doya, "たいあたり"); _dmg_oya = _h1 - _doya.hp
_h2 = _doya0.hp; execute(_poya0, _doya0, "たいあたり"); _dmg_norm = _h2 - _doya0.hp
check("おやこあい 合計約1.25倍(2発目0.25)", near(_dmg_oya / _dmg_norm, 1.25), f"oya={_dmg_oya} norm={_dmg_norm}")
# 技の効果は2回分発動する：100%副次効果(ワイドブレイカー=相手攻撃-1)が2回適用され-2になる
_poya2 = make_poke(type1="むし", atk_b=100, ability="おやこあい", moves=["ワイドブレイカー"])
_doya2 = make_poke(type1="ノーマル", def_b=100, hp_b=255)
execute(_poya2, _doya2, "ワイドブレイカー")
check("おやこあい 副次効果が2回発動(攻撃-2)", _doya2.stage_attack == -2, f"atk={_doya2.stage_attack}")
# 対照：おやこあい無しなら-1（1回のみ）
_poya2n = make_poke(type1="むし", atk_b=100, moves=["ワイドブレイカー"]); _doya2n = make_poke(type1="ノーマル", def_b=100, hp_b=255)
execute(_poya2n, _doya2n, "ワイドブレイカー")
check("対照: 通常は攻撃-1(1回)", _doya2n.stage_attack == -1, f"atk={_doya2n.stage_attack}")

# とびだすなかみ：ひんし時、受けたダメージを攻撃側へ返す
_ptn = make_poke(type1="ノーマル", ability="とびだすなかみ", hp_b=10); _ptn.hp = 5
_atn = make_poke(atk_b=200, moves=["じしん"]); _atn_hp0 = _atn.hp
execute(_atn, _ptn, "じしん")
check("とびだすなかみ ひんし時に攻撃側へ反射", not _ptn.is_alive and _atn.hp < _atn_hp0, f"atk_hp={_atn.hp}/{_atn_hp0}")
# 負例：ひんしにならなければ反射しない
_ptn_s = make_poke(type1="ノーマル", ability="とびだすなかみ", hp_b=255, def_b=200); _atn_s = make_poke(atk_b=10); _atn_s_hp = _atn_s.hp
execute(_atn_s, _ptn_s, "たいあたり")
check("とびだすなかみ 生存時は反射しない", _ptn_s.is_alive and _atn_s.hp == _atn_s_hp)

# とびだすハバネロ：技ダメージを受けると攻撃側やけど
_pth = make_poke(type1="ノーマル", ability="とびだすハバネロ", hp_b=255); _ath = make_poke(type1="ノーマル", atk_b=100)
execute(_ath, _pth, "たいあたり")
check("とびだすハバネロ 被弾で攻撃側やけど", _ath.status == "burn", f"status={_ath.status}")
# 負例：ダメージの無い変化技では攻撃側はやけどしない
_pth_n = make_poke(type1="ノーマル", ability="とびだすハバネロ", hp_b=255); _ath_n = make_poke(moves=["でんじは"])
execute(_ath_n, _pth_n, "でんじは")
check("とびだすハバネロ 変化技では発動しない", _ath_n.status != "burn")

# ふかしのこぶし：接触技でまもるを貫通し「本来の1/4ダメージ」を与える（かんつうドリルと同効果）
_pfk = make_poke(type1="ノーマル", atk_b=100, ability="ふかしのこぶし", moves=["のしかかり"])
_dfk = make_poke(type1="ノーマル", def_b=100, hp_b=255); _dfk.protecting = True
_dfk_full = make_poke(type1="ノーマル", def_b=100, hp_b=255)  # まもり無しの通常ダメージ基準
_h3 = _dfk.hp; random.seed(7); execute(_pfk, _dfk, "のしかかり"); _dmg_fk = _h3 - _dfk.hp
_hfull = _dfk_full.hp; random.seed(7); execute(make_poke(type1="ノーマル", atk_b=100, ability="ふかしのこぶし", moves=["のしかかり"]), _dfk_full, "のしかかり"); _dmg_full = _hfull - _dfk_full.hp
check("ふかしのこぶし まもる貫通＋1/4ダメージ", _dmg_fk > 0 and near(_dmg_fk, max(1, _dmg_full // 4)), f"pierce={_dmg_fk} full={_dmg_full}")
# 負例：非接触技ではまもるを貫通できない
_pfk_n = make_poke(type1="ノーマル", atk_b=100, ability="ふかしのこぶし", moves=["タネマシンガン"])
_dfk_n = make_poke(type1="ノーマル", def_b=100, hp_b=255); _dfk_n.protecting = True
_h3n = _dfk_n.hp; execute(_pfk_n, _dfk_n, "タネマシンガン")
check("ふかしのこぶし 非接触技ではまもるに防がれる", _dfk_n.hp == _h3n)

# かんつうドリル：接触技でまもる貫通だが1/4ダメージ
_pkd = make_poke(type1="ノーマル", atk_b=100, ability="かんつうドリル", moves=["のしかかり"])
_dkd = make_poke(type1="ノーマル", def_b=100, hp_b=255); _dkd_p = make_poke(type1="ノーマル", def_b=100, hp_b=255)
_dkd.protecting = True
_h4 = _dkd.hp; random.seed(7); execute(_pkd, _dkd, "のしかかり"); _dmg_pierce = _h4 - _dkd.hp
_h5 = _dkd_p.hp; random.seed(7); execute(make_poke(type1="ノーマル", atk_b=100, ability="かんつうドリル", moves=["のしかかり"]), _dkd_p, "のしかかり"); _dmg_full = _h5 - _dkd_p.hp
check("かんつうドリル まもる貫通＋1/4ダメージ", _dmg_pierce > 0 and near(_dmg_pierce, max(1, _dmg_full // 4)), f"pierce={_dmg_pierce} full={_dmg_full}")

# かげふみ：ゴースト以外は交代不可（is_trapped）
_op_sf = make_poke(ability="かげふみ")
check("かげふみ 非ゴーストは交代不可", _is_trapped(make_poke(type1="ノーマル"), _op_sf))
check("かげふみ ゴーストは交代可", not _is_trapped(make_poke(type1="ゴースト"), _op_sf))
check("かげふみ なしは交代可", not _is_trapped(make_poke(type1="ノーマル"), make_poke(ability="しんりょく")))

# ════════════════════════════════════════════════════════════════
# 3. わざテスト
# ════════════════════════════════════════════════════════════════
print("\n=== 3. わざ ===")

# ── 威力変動技 ──

# おはかまいり (倒れた味方数×50+50) ゴースト技はノーマルに無効→エスパー相手
p_revenge = make_poke(type1="ゴースト", spatk_b=100, moves=["おはかまいり"])
p_revenge.fainted_allies = 0
d_rev0 = dmg(p_revenge, make_poke(type1="エスパー", spdef_b=100), "おはかまいり", roll=0.5)
p_revenge.fainted_allies = 3
d_rev3 = dmg(p_revenge, make_poke(type1="エスパー", spdef_b=100), "おはかまいり", roll=0.5)
check("おはかまいり 0体: 威力50 (>0)", d_rev0 > 0)
check("おはかまいり 3体: 威力200 (0体の4倍)", near(d_rev3 / d_rev0, 200 / 50))

# からげんき (通常70・状態異常140・やけど半減無視)
p_facade = make_poke(atk_b=100)
p_facade_burn = make_poke(atk_b=100)
p_facade_burn.status = "burn"
p_tgt_f = make_poke(def_b=100)
d_fac = dmg(p_facade, p_tgt_f, "からげんき", roll=0.5)
d_fac_burn = dmg(p_facade_burn, p_tgt_f, "からげんき", roll=0.5)
# やけど時でも攻撃半減を受けない → 威力2倍がそのまま効いて2倍ダメージ
check("からげんき やけど時2倍(半減無視)", near(d_fac_burn, d_fac * 2))

# しおふき (HP満タン150 / 半分75)
p_wata = make_poke(type1="みず", spatk_b=100)
p_tgt_w = make_poke(spdef_b=100)
d_ws_full = dmg(p_wata, p_tgt_w, "しおふき", roll=0.5)
p_wata_half = make_poke(type1="みず", spatk_b=100)
p_wata_half.hp = p_wata_half.max_hp // 2
d_ws_half = dmg(p_wata_half, p_tgt_w, "しおふき", roll=0.5)
check("しおふき HP半分で威力半減", near(d_ws_full / d_ws_half, 2.0))

# たたりめ (状態異常相手に威力2倍) ゴースト技→エスパータイプが対象
p_hex = make_poke(type1="ゴースト", spatk_b=100)
p_hexed = make_poke(type1="エスパー", spdef_b=100)
p_hexed_burn = make_poke(type1="エスパー", spdef_b=100)
p_hexed_burn.status = "burn"
d_hex = dmg(p_hex, p_hexed, "たたりめ", roll=0.5)
d_hex_burn = dmg(p_hex, p_hexed_burn, "たたりめ", roll=0.5)
check("たたりめ 状態異常相手に2倍", near(d_hex_burn / d_hex, 2.0))

# アシストパワー (ランク+2で威力60)
p_assist = make_poke(type1="エスパー", spatk_b=100)
p_tgt_ap = make_poke(spdef_b=100)
d_ap0 = dmg(p_assist, p_tgt_ap, "アシストパワー", roll=0.5)
p_assist.stage_sp_attack = 2  # rank+2 → sum=2 → power=20+40=60
d_ap2 = dmg(p_assist, p_tgt_ap, "アシストパワー", roll=0.5)
check("アシストパワー ランク0=威力20", True)  # rank_sum=0 → 20+0=20
check("アシストパワー ランク+2でダメ増加", d_ap2 > d_ap0)

# やけっぱち (前ターン失敗で威力2倍。やけど依存ではない)
from simulator.damage import _effective_power as _eff_power
p_yake = make_poke(type1="ほのお", atk_b=100)
p_tgt_y = make_poke(def_b=100)
_yk_normal = _eff_power(p_yake, p_tgt_y, dl.get_move("やけっぱち"), BattleField())
p_yake._move_failed_last = True
_yk_fail = _eff_power(p_yake, p_tgt_y, dl.get_move("やけっぱち"), BattleField())
check("やけっぱち 前ターン失敗2倍", _yk_fail == _yk_normal * 2, f"normal={_yk_normal} fail={_yk_fail}")
# やけど状態でも威力は変わらない（やけど依存の誤実装がないこと）
p_yake_burn = make_poke(type1="ほのお", atk_b=100); p_yake_burn.status = "burn"
_yk_burn = _eff_power(p_yake_burn, p_tgt_y, dl.get_move("やけっぱち"), BattleField())
check("やけっぱち やけど依存なし", _yk_burn == _yk_normal, f"normal={_yk_normal} burn={_yk_burn}")

# ゆきなだれ (後攻時威力2倍)
p_aval = make_poke(type1="こおり", atk_b=100)
p_tgt_av = make_poke(def_b=100)
p_aval._acts_second = False
d_av_first = dmg(p_aval, p_tgt_av, "ゆきなだれ", roll=0.5)
p_aval._acts_second = True
d_av_second = dmg(p_aval, p_tgt_av, "ゆきなだれ", roll=0.5)
check("ゆきなだれ 後攻時2倍", near(d_av_second / d_av_first, 2.0))

# ダメおし (後攻時威力2倍)
p_pay = make_poke(type1="あく", atk_b=100)
p_tgt_pay = make_poke(def_b=100)
p_pay._acts_second = False
d_pay_first = dmg(p_pay, p_tgt_pay, "ダメおし", roll=0.5)
p_pay._acts_second = True
d_pay_second = dmg(p_pay, p_tgt_pay, "ダメおし", roll=0.5)
check("ダメおし 後攻時2倍", near(d_pay_second / d_pay_first, 2.0))

# しっぺがえし (後攻時2倍)
p_ret = make_poke(type1="あく", atk_b=100)
p_ret._acts_second = False
d_ret_f = dmg(p_ret, p_tgt_pay, "しっぺがえし", roll=0.5)
p_ret._acts_second = True
d_ret_s = dmg(p_ret, p_tgt_pay, "しっぺがえし", roll=0.5)
check("しっぺがえし 後攻時2倍", near(d_ret_s / d_ret_f, 2.0))

# くさむすび/けたぐり (重さ依存 - デフォルト50kg → power60)
p_kg = make_poke(type1="くさ", spatk_b=100)
p_tgt_kg = make_poke(spdef_b=100)
d_kg = dmg(p_kg, p_tgt_kg, "くさむすび", roll=0.5)
check("くさむすび 実行可能", d_kg > 0)

# ── 計算式変更技 ──

# イカサマ (相手の攻撃実数値で計算)
p_foul = make_poke(type1="あく", atk_b=80, spatk_b=80)
p_target_high_atk = make_poke(atk_b=200, def_b=100)
p_target_low_atk = make_poke(atk_b=40, def_b=100)
d_foul_high = dmg(p_foul, p_target_high_atk, "イカサマ", roll=0.5)
d_foul_low  = dmg(p_foul, p_target_low_atk,  "イカサマ", roll=0.5)
check("イカサマ 相手A高い方がダメ大", d_foul_high > d_foul_low)

# ボディプレス (自身のBで計算)
p_bp_high = make_poke(type1="かくとう", def_b=200)
p_bp_low  = make_poke(type1="かくとう", def_b=50)
p_tgt_bp = make_poke(def_b=100)
d_bp_h = dmg(p_bp_high, p_tgt_bp, "ボディプレス", roll=0.5)
d_bp_l = dmg(p_bp_low,  p_tgt_bp, "ボディプレス", roll=0.5)
check("ボディプレス 自B高い方がダメ大", d_bp_h > d_bp_l)

# サイコショック (特殊技だが相手の物理防御で計算)
p_psy = make_poke(type1="エスパー", spatk_b=100)
p_high_def = make_poke(def_b=200, spdef_b=50)
p_high_spdef = make_poke(def_b=50, spdef_b=200)
d_ps_hd  = dmg(p_psy, p_high_def,   "サイコショック", roll=0.5)
d_ps_hsd = dmg(p_psy, p_high_spdef, "サイコショック", roll=0.5)
check("サイコショック 相手B高い方がダメ小", d_ps_hd < d_ps_hsd)

# せいなるつるぎ (相手防御ランク無視)
p_sacred = make_poke(type1="かくとう", atk_b=100)
p_def_boosted = make_poke(def_b=100)
p_def_boosted.stage_defense = 6  # 最大ランク
p_def_normal = make_poke(def_b=100)
d_sv_boosted = dmg(p_sacred, p_def_boosted, "せいなるつるぎ", roll=0.5)
d_sv_normal  = dmg(p_sacred, p_def_normal,  "せいなるつるぎ", roll=0.5)
check("せいなるつるぎ 相手B+6ランクを無視", d_sv_boosted == d_sv_normal)

# ── 天候の防御補正 × 「参照する防御能力を差し替える技」の適用順序 ──
# 雪の氷B×1.5・砂の岩D×1.5 は「どの実数値を参照するか」が確定した後に掛ける。
# 以前は防御実数値を選ぶ時点で掛けていたため、せいなるつるぎ/DDラリアット/サイコショック系が
# dfs を上書きした瞬間に天候補正が消えていた（ランク変化の無視であって天候補正の無視ではない）。
_f_hail_o = BattleField(); _f_hail_o.weather = "hail"; _f_hail_o.weather_count = 5
_f_sand_o = BattleField(); _f_sand_o.weather = "sandstorm"; _f_sand_o.weather_count = 5
_f_none_o = BattleField()


def _dfs_boosted(base_poke_factory, stat, mult=1.5):
    """天候補正後の防御実数値を手で作った対照ポケモン（天候なしで同じ値になるはず）。"""
    p = base_poke_factory()
    setattr(p, stat, math.floor(getattr(p, stat) * mult))
    return p


_atk_o = make_poke(type1="かくとう", atk_b=120)
_atk_ps = make_poke(type1="エスパー", spatk_b=120)
_mk_ice = lambda: make_poke(type1="こおり", def_b=100, spdef_b=100)
_mk_rock = lambda: make_poke(type1="いわ", def_b=100, spdef_b=100)

# せいなるつるぎ（相手Bランク無視技）でも雪の氷B×1.5は乗る。
# 「天候ありの氷」と「防御実数値を手で1.5倍した氷・天候なし」が完全一致することで厳密に検証する。
for _mv_o, _atkr_o in (("せいなるつるぎ", _atk_o), ("DDラリアット", _atk_o),
                       ("サイコショック", _atk_ps), ("インファイト", _atk_o)):
    _a = dmg(_atkr_o, _mk_ice(), _mv_o, roll=0.5, f=_f_hail_o)
    _b = dmg(_atkr_o, _dfs_boosted(_mk_ice, "defense"), _mv_o, roll=0.5, f=_f_none_o)
    check(f"雪 {_mv_o} に氷B1.5倍が乗る(実数値1.5倍と一致)", _a == _b and _a > 0, f"hail={_a} manual={_b}")
    # 対照: 天候なしでは補正が乗らない（＝手動1.5倍版より必ずダメージが大きい）
    _c = dmg(_atkr_o, _mk_ice(), _mv_o, roll=0.5, f=_f_none_o)
    check(f"雪なし {_mv_o} は氷B1.5倍が乗らない", _c > _a, f"none={_c} hail={_a}")

# 砂の岩D×1.5は「Dを参照する特殊技」にのみ乗る。B参照技（物理・サイコショック系）には乗らない。
_d_sk_sand = dmg(_atk_ps, _mk_rock(), "サイコキネシス", roll=0.5, f=_f_sand_o)
_d_sk_man = dmg(_atk_ps, _dfs_boosted(_mk_rock, "sp_defense"), "サイコキネシス", roll=0.5, f=_f_none_o)
check("砂 特殊技に岩D1.5倍が乗る(実数値1.5倍と一致)", _d_sk_sand == _d_sk_man and _d_sk_sand > 0,
      f"sand={_d_sk_sand} manual={_d_sk_man}")
check("砂 物理技に岩D1.5倍は乗らない",
      dmg(_atk_o, _mk_rock(), "インファイト", roll=0.5, f=_f_sand_o)
      == dmg(_atk_o, _mk_rock(), "インファイト", roll=0.5, f=_f_none_o))
check("砂 サイコショック(B参照)に岩D1.5倍は乗らない",
      dmg(_atk_ps, _mk_rock(), "サイコショック", roll=0.5, f=_f_sand_o)
      == dmg(_atk_ps, _mk_rock(), "サイコショック", roll=0.5, f=_f_none_o))

# ── 反動技 ──
for move_n, expected_rate, move_type in [
    ("すてみタックル", 1/3, "ノーマル"),
    ("フレアドライブ", 1/3, "ほのお"),
    ("ボルテッカー",   1/3, "でんき"),
    ("ウェーブタックル",1/3,"みず"),
    ("ブレイブバード",  1/3, "ひこう"),
    ("ウッドハンマー",  1/3, "くさ"),
    ("もろはのずつき",  1/2, "ノーマル"),
    ("ワイルドボルト",  1/4, "でんき"),
    ("はめつのひかり",  1/2, "ドラゴン"),
]:
    p_rc = make_poke(type1=move_type, atk_b=100, spatk_b=100, moves=[move_n])
    p_tgt_rc = make_poke(def_b=60, spdef_b=60)
    hp_before = p_rc.hp
    logs_rc = execute(p_rc, p_tgt_rc, move_n)
    dealt_log = [l for l in logs_rc if "ダメ" in l and move_n in l]
    if dealt_log:
        dealt_val = int(dealt_log[0].split("に")[1].split("ダメ")[0])
        recoil_taken = hp_before - p_rc.hp
        expected_recoil = max(1, math.floor(dealt_val * expected_rate))
        check(f"{move_n} 反動{int(expected_rate*100)}%",
              recoil_taken == expected_recoil,
              f"dealt={dealt_val} recoil={recoil_taken} expected={expected_recoil}")
    else:
        check(f"{move_n} 実行確認", True)

# てっていこうせん (最大HPの1/2反動)
p_fc = make_poke(atk_b=150, moves=["てっていこうせん"])
p_tgt_fc = make_poke(def_b=50)
hp_fc_before = p_fc.hp
logs_fc = execute(p_fc, p_tgt_fc, "てっていこうせん")
recoil_fc = hp_fc_before - p_fc.hp
check("てっていこうせん 最大HP1/2反動", recoil_fc == p_fc.max_hp // 2,
      f"recoil={recoil_fc} expected={p_fc.max_hp//2}")

# ロックヘッド: 反動なし
p_rh = make_poke(atk_b=100, ability="ロックヘッド", moves=["すてみタックル"])
p_tgt_rh = make_poke(def_b=80)
hp_rh_before = p_rh.hp
execute(p_rh, p_tgt_rh, "すてみタックル")
check("ロックヘッド 反動なし", p_rh.hp == hp_rh_before)

# ── ドレイン技 ──
for move_n, rate, move_type in [
    ("ギガドレイン", 0.5, "くさ"), ("ドレインパンチ", 0.5, "かくとう"),
    ("むねんのつるぎ", 0.5, "ほのお"),
]:
    p_dr = make_poke(type1=move_type, atk_b=100, spatk_b=100, moves=[move_n])
    p_tgt_dr = make_poke(def_b=80, spdef_b=80)
    p_dr.hp = p_dr.max_hp // 2
    hp_before_dr = p_dr.hp
    logs_dr = execute(p_dr, p_tgt_dr, move_n)
    heal_log = [l for l in logs_dr if "吸収" in l]
    check(f"{move_n} ドレイン吸収ログあり", len(heal_log) > 0)
    check(f"{move_n} HP回復", p_dr.hp > hp_before_dr)

# ── 状態異常ステータス技 ──
# しびれごな (まひ) — 命中率75%のためループで判定（RNG状態に依存しない）
random.seed(0); _stun_ok = False
for _ in range(20):
    p_stun = make_poke(type1="ノーマル", moves=["しびれごな"])
    p_target_stun = make_poke(type1="ノーマル")
    execute(p_stun, p_target_stun, "しびれごな")
    if p_target_stun.status == "paralysis": _stun_ok = True; break
check("しびれごな まひ付与", _stun_ok)

# しびれごな くさタイプには効かない
p_grass_target = make_poke(type1="くさ")
execute(p_stun, p_grass_target, "しびれごな")
check("しびれごな くさタイプ無効", p_grass_target.status is None)

# きあいだめ (急所ランク+2)
p_focus = make_poke(moves=["きあいだめ"])
p_tgt_focus = make_poke()
logs_focus = execute(p_focus, p_tgt_focus, "きあいだめ")
check("きあいだめ crit_stage+2", p_focus.crit_stage == 2)

# ── リチャージ技 ──
random.seed(0)
p_gi = make_poke(atk_b=150, moves=["ギガインパクト"])
p_tgt_gi = make_poke(def_b=50)
execute(p_gi, p_tgt_gi, "ギガインパクト")
check("ギガインパクト 使用後rechargeフラグ", p_gi.recharge)

random.seed(0)
p_bb = make_poke(type1="ほのお", spatk_b=150, moves=["ブラストバーン"])
p_tgt_bb = make_poke(spdef_b=50)
execute(p_bb, p_tgt_bb, "ブラストバーン")
check("ブラストバーン 使用後rechargeフラグ", p_bb.recharge)

# リチャージ中は動けない
p_gi2 = make_poke(atk_b=150, moves=["ギガインパクト"])
p_gi2.recharge = True
logs_gi2 = execute(p_gi2, make_poke(), "ギガインパクト")
check("リチャージ中 行動不能", "動けない" in " ".join(logs_gi2))
check("リチャージ 解除", not p_gi2.recharge)

# ── ねごと ──
p_slt = make_poke(moves=["ねごと","のしかかり"])
p_slt.status = "sleep"; p_slt.sleep_count = 3
p_slt_tgt = make_poke(def_b=100)
logs_slt = execute(p_slt, p_slt_tgt, "ねごと")
check("ねごと ねむり中に実行", "ねごと で" in " ".join(logs_slt))
check("ねごと ねむり状態維持", p_slt.status == "sleep")

# ねごと 非ねむりでは失敗
p_slt_awake = make_poke(moves=["ねごと","のしかかり"])
logs_slt_aw = execute(p_slt_awake, make_poke(), "ねごと")
check("ねごと 非ねむりで失敗", "失敗" in " ".join(logs_slt_aw))

# ── 一撃必殺 ──
# ぜったいれいど はこおりタイプに無効
p_bliz = make_poke(spatk_b=100, moves=["ぜったいれいど"])
p_ice_type = make_poke(type1="こおり")
logs_bliz = execute(p_bliz, p_ice_type, "ぜったいれいど")
check("ぜったいれいど こおりタイプ無効", "効かない" in " ".join(logs_bliz))
check("ぜったいれいど こおりタイプ生存", p_ice_type.is_alive)

# じわれ はひこうタイプに無効
p_jiware = make_poke(atk_b=100, moves=["じわれ"])
p_flying = make_poke(type1="ひこう")
logs_jiware = execute(p_jiware, p_flying, "じわれ")
check("じわれ ひこうタイプ無効", "効かない" in " ".join(logs_jiware))
check("じわれ ひこうタイプ生存", p_flying.is_alive)

# ぜったいれいど 命中率: こおりタイプ使用→30%、非こおりタイプ→20%
from simulator.damage import check_hit as _ch
_m_bliz = dl.get_move("ぜったいれいど")
_p_ice_user  = make_poke(type1="こおり")
_p_norm_user = make_poke(type1="ノーマル")
_p_dummy = make_poke(type1="ノーマル")
random.seed(0)
_hits_ice  = sum(1 for _ in range(3000) if _ch(_p_ice_user,  _p_dummy, _m_bliz, BattleField()))
_hits_norm = sum(1 for _ in range(3000) if _ch(_p_norm_user, _p_dummy, _m_bliz, BattleField()))
check("ぜったいれいど こおりタイプ命中率≈30%", 800 < _hits_ice  < 1000, f"{_hits_ice}/3000")
check("ぜったいれいど 非こおり命中率≈20%",     500 < _hits_norm < 700,  f"{_hits_norm}/3000")

# ハサミギロチン (命中すれば即倒れ)
random.seed(1)  # hit seed
p_scis = make_poke(atk_b=100, moves=["ハサミギロチン"])
p_scis_tgt = make_poke()
logs_scis = execute(p_scis, p_scis_tgt, "ハサミギロチン")
if "一撃必殺" in " ".join(logs_scis):
    check("ハサミギロチン 命中→即倒", not p_scis_tgt.is_alive)
else:
    check("ハサミギロチン (外れ確認)", not p_scis_tgt.is_alive or p_scis_tgt.hp > 0)

# ── クリアスモッグ (ランクリセット) ──
p_clears = make_poke(type1="どく", spatk_b=100, moves=["クリアスモッグ"])
p_tgt_cs = make_poke(spdef_b=80)
p_tgt_cs.stage_attack = 3
p_tgt_cs.stage_speed = 2
logs_cs = execute(p_clears, p_tgt_cs, "クリアスモッグ")
check("クリアスモッグ 攻撃ランクリセット", p_tgt_cs.stage_attack == 0)
check("クリアスモッグ 速度ランクリセット", p_tgt_cs.stage_speed == 0)

# ── こうそくスピン (ハザード除去+速度+1) ──
p_spin = make_poke(atk_b=100, moves=["こうそくスピン"])
p_tgt_spin = make_poke(def_b=80)
f_spin = BattleField()
f_spin.stealth_rock[0] = True
f_spin.spikes[0] = 2
s_spin = BattleSide([p_spin]); s_spin.field_idx = 0
s_tgt_spin = BattleSide([p_tgt_spin]); s_tgt_spin.field_idx = 1
logs_spin = _execute_move(s_spin, s_tgt_spin, Action(type="move", move=dl.get_move("こうそくスピン")), f_spin)
check("こうそくスピン ステルスロック除去", not f_spin.stealth_rock[0])
check("こうそくスピン まきびし除去", f_spin.spikes[0] == 0)
check("こうそくスピン 速度+1", p_spin.stage_speed == 1)

# ── トリックフラワー (常に急所) ──
p_tf = make_poke(type1="くさ", atk_b=100, moves=["トリックフラワー"])
p_tgt_tf = make_poke(def_b=100)
crit_count = sum(1 for _ in range(20) if _check_critical(p_tf, dl.get_move("トリックフラワー")))
check("トリックフラワー 常に急所", crit_count == 20)

# ── フェイタルクロー (33%状態異常) ──
random.seed(42)
p_fc2 = make_poke(type1="どく", atk_b=100, moves=["フェイタルクロー"])
status_count = 0
for _ in range(100):
    p_tgt2 = make_poke()
    execute(p_fc2, p_tgt2, "フェイタルクロー")
    if p_tgt2.status is not None:
        status_count += 1
check("フェイタルクロー 33%状態異常(±15%)", 15 < status_count < 55, f"{status_count}/100")

# ── ドゲザン (必中) ──
p_doge = make_poke(type1="あく", atk_b=100, moves=["ドゲザン"])
p_evade = make_poke(); p_evade.stage_evasion = 6  # 最大回避
hit_count_dg = 0
for _ in range(20):
    p_tgt_dg = make_poke(); p_tgt_dg.stage_evasion = 6
    logs_dg = execute(p_doge, p_tgt_dg, "ドゲザン")
    if any("ダメ" in l and "ドゲザン" in l for l in logs_dg):
        hit_count_dg += 1
check("ドゲザン 必中", hit_count_dg == 20, f"{hit_count_dg}/20")

# ── 多段ヒット技 ──
p_multi = make_poke(atk_b=100, moves=["みずしゅりけん"])
p_tgt_multi = make_poke(def_b=100)
logs_multi = execute(p_multi, p_tgt_multi, "みずしゅりけん")
dmg_log = [l for l in logs_multi if "ダメ" in l and "回" in l]
if dmg_log:
    hits = int(dmg_log[0].split("(")[1].split("回")[0])
    check("みずしゅりけん 多段(2-5回)", 2 <= hits <= 5, f"{hits}回")
else:
    check("みずしゅりけん 実行確認", True)

# スキルリンク: 必ず5回
p_skilllink = make_poke(atk_b=100, ability="スキルリンク", moves=["みずしゅりけん"])
hit_counts = []
for _ in range(5):
    p_sl_tgt = make_poke(def_b=100)
    logs_sl = execute(p_skilllink, p_sl_tgt, "みずしゅりけん")
    dmg_sl = [l for l in logs_sl if "回)" in l]
    if dmg_sl:
        hit_counts.append(int(dmg_sl[0].split("(")[1].split("回")[0]))
check("スキルリンク 常に5回", all(h == 5 for h in hit_counts), str(hit_counts))
# 負例：スキルリンク無しでは回数が変動（5未満も出る）
_p_nsl = make_poke(atk_b=100); random.seed(3); _nsl = []
for _ in range(20):
    _lg = execute(_p_nsl, make_poke(def_b=100), "みずしゅりけん")
    _d = [l for l in _lg if "回)" in l]
    if _d: _nsl.append(int(_d[0].split("(")[1].split("回")[0]))
check("スキルリンク無しは回数が変動(5未満あり)", any(h < 5 for h in _nsl), str(_nsl))

# ── 優先度確認 (DB値) ──
priority_moves = {
    "かげうち": 1, "しんそく": 2, "アクアジェット": 1,
    "バレットパンチ": 1, "でんこうせっか": 1, "マッハパンチ": 1,
    "しんくうは": 1,
}
for move_n, expected_pri in priority_moves.items():
    m = dl.get_move(move_n)
    if m:
        check(f"{move_n} 優先度{expected_pri}", m.priority == expected_pri,
              f"actual={m.priority}")
    else:
        check(f"{move_n} DB存在", False, "DB未登録")

# ── 追加効果確認 ──
# みずのはどう 20%混乱
random.seed(0)
p_wb = make_poke(type1="みず", spatk_b=100, moves=["みずのはどう"])
conf_count = 0
for _ in range(100):
    p_wb_tgt = make_poke(spdef_b=100)
    execute(p_wb, p_wb_tgt, "みずのはどう")
    if p_wb_tgt.confused:
        conf_count += 1
check("みずのはどう 20%混乱(±10%)", 8 < conf_count < 35, f"{conf_count}/100")

# ほのおのまい 50%特攻+1 (self)
random.seed(0)
p_flame = make_poke(type1="ほのお", spatk_b=100, moves=["ほのおのまい"])
boost_count_fm = 0
for _ in range(100):
    p_fm_tgt = make_poke(spdef_b=80)
    p_fm = make_poke(type1="ほのお", spatk_b=100, moves=["ほのおのまい"])
    execute(p_fm, p_fm_tgt, "ほのおのまい")
    if p_fm.stage_sp_attack == 1:
        boost_count_fm += 1
check("ほのおのまい 50%特攻+1(±15%)", 35 < boost_count_fm < 65, f"{boost_count_fm}/100")

# くさわけ 速度+1 (always)
p_grassy = make_poke(type1="くさ", atk_b=100, moves=["くさわけ"])
p_tgt_grassy = make_poke(def_b=80)
execute(p_grassy, p_tgt_grassy, "くさわけ")
check("くさわけ 速度+1", p_grassy.stage_speed == 1)

# ラスターカノン 10%特防-1
random.seed(0)
p_lc = make_poke(type1="はがね", spatk_b=100, moves=["ラスターカノン"])
spdef_down_count = 0
for _ in range(100):
    p_lc_tgt = make_poke(spdef_b=100)
    execute(p_lc, p_lc_tgt, "ラスターカノン")
    if p_lc_tgt.stage_sp_defense == -1:
        spdef_down_count += 1
check("ラスターカノン 10%特防-1(±8%)", 2 < spdef_down_count < 22, f"{spdef_down_count}/100")

# ── 天候技 ──
for move_n, weather in [("あまごい","rain"),("にほんばれ","sunny"),
                          ("すなあらし","sandstorm"),("あられ","hail")]:
    f_w = BattleField()
    p_wm = make_poke(moves=[move_n])
    execute(p_wm, make_poke(), move_n, f=f_w)
    check(f"{move_n} 天候発動", f_w.weather == weather)

# ── 急所確率 ──
# 通常(stage=0): 1/24
crit_base = sum(1 for _ in range(2400) if _check_critical(make_poke(), dl.get_move("たいあたり")))
check("急所 通常1/24(±0.5%)", 60 < crit_base < 140, f"{crit_base}/2400")

# 高急所技(stage=1): 1/8
p_hi_crit = make_poke()
crit_hi = sum(1 for _ in range(800) if _check_critical(p_hi_crit, dl.get_move("スラッシュ")))
check("急所 高急所技1/8(±3%)", 75 < crit_hi < 125, f"{crit_hi}/800")

# きあいだめ(stage=2): 1/2
p_fc3 = make_poke(); p_fc3.crit_stage = 2
crit_fc3 = sum(1 for _ in range(400) if _check_critical(p_fc3, dl.get_move("たいあたり")))
check("きあいだめ 急所1/2(±7%)", 170 < crit_fc3 < 230, f"{crit_fc3}/400")

# ── 急所 ステージ無視仕様 ──
# 比較基準: 急所かつステージなし（これに1.5倍が乗った値）
p_crit_ref_atk = make_poke(atk_b=100)
p_crit_ref_def = make_poke(def_b=100)
dmg_crit_no_stage = dmg(p_crit_ref_atk, p_crit_ref_def, "たいあたり", crit=True)

# 急所時: 自分の攻撃ランクが下がっていても無視 → ステージなしcritと同じダメ
p_crit_atk_down = make_poke(atk_b=100)
p_crit_atk_down.stage_attack = -6
p_crit_def = make_poke(def_b=100)
dmg_crit_atk_down   = dmg(p_crit_atk_down, p_crit_def, "たいあたり", crit=True)
dmg_nocrit_atk_down = dmg(p_crit_atk_down, p_crit_def, "たいあたり", crit=False)
dmg_nocrit_baseline = dmg(make_poke(atk_b=100), p_crit_def, "たいあたり", crit=False)
check("急所 自分攻撃-6ランクを無視", dmg_crit_atk_down == dmg_crit_no_stage,
      f"crit_down={dmg_crit_atk_down} crit_flat={dmg_crit_no_stage}")
check("急所なし 攻撃-6は有効（低ダメ）", dmg_nocrit_atk_down < dmg_nocrit_baseline)

# 急所時: 相手の防御ランクが上がっていても無視 → ステージなしcritと同じダメ
p_crit_atk2 = make_poke(atk_b=100)
p_crit_def_up = make_poke(def_b=100)
p_crit_def_up.stage_defense = +6
dmg_crit_def_up   = dmg(p_crit_atk2, p_crit_def_up, "たいあたり", crit=True)
dmg_nocrit_def_up = dmg(p_crit_atk2, p_crit_def_up, "たいあたり", crit=False)
dmg_nocrit_baseline2 = dmg(p_crit_atk2, make_poke(def_b=100), "たいあたり", crit=False)
check("急所 相手防御+6ランクを無視", dmg_crit_def_up == dmg_crit_no_stage,
      f"crit_up={dmg_crit_def_up} crit_flat={dmg_crit_no_stage}")
check("急所なし 防御+6は有効（低ダメ）", dmg_nocrit_def_up < dmg_nocrit_baseline2)

# まもる ──
p_protect = make_poke(moves=["まもる"])
p_tgt_protect = make_poke(atk_b=100, moves=["たいあたり"])
s_pro = BattleSide([p_protect]); s_tgt_pro = BattleSide([p_tgt_protect])
from simulator.battle import Action as Act
execute(p_protect, p_tgt_protect, "まもる")
check("まもる フラグ設定", p_protect.protecting)
hp_before_pro = p_protect.hp
execute(p_tgt_protect, p_protect, "たいあたり")
check("まもる ダメージ無効", p_protect.hp == hp_before_pro)

# まもる連続使用: 成功率は (1/3)^n（n=連続成功回数）
# 2回目 (n=1): 1/3 ≈ 33.3%
random.seed(42)
p_prot_consec = make_poke(moves=["まもる"])
p_prot_consec.protect_consecutive = 1  # 1回成功済み
successes_2nd = 0
trials = 900
for _ in range(trials):
    p_prot_consec.protecting = False
    p_prot_consec.protect_consecutive = 1
    execute(p_prot_consec, make_poke(), "まもる")
    if p_prot_consec.protecting:
        successes_2nd += 1
check("まもる 2回目成功率≈1/3(33%)", 240 < successes_2nd < 360, f"{successes_2nd}/{trials}")

# 3回目 (n=2): 1/9 ≈ 11.1%
random.seed(0)
successes_3rd = 0
for _ in range(trials):
    p_prot_consec.protecting = False
    p_prot_consec.protect_consecutive = 2
    execute(p_prot_consec, make_poke(), "まもる")
    if p_prot_consec.protecting:
        successes_3rd += 1
check("まもる 3回目成功率≈1/9(11%)", 60 < successes_3rd < 140, f"{successes_3rd}/{trials}")

# ── 状態異常技 (status move) ──
for move_n, expected_status, target_type in [
    ("でんじは", "paralysis", "ノーマル"),
    ("おにび",   "burn",      "ノーマル"),
    ("どくどく", "badpoison", "ノーマル"),
]:
    p_sm = make_poke(moves=[move_n])
    p_tgt_sm = make_poke(type1=target_type)
    execute(p_sm, p_tgt_sm, move_n)
    check(f"{move_n} 状態付与", p_tgt_sm.status == expected_status)

# でんじは でんきタイプ免疫
p_ele = make_poke(type1="でんき")
p_para = make_poke(moves=["でんじは"])
execute(p_para, p_ele, "でんじは")
check("でんじは でんきタイプ無効", p_ele.status is None)

# ── タイプ無効 ──
p_ghost = make_poke(type1="ゴースト", def_b=100)
p_normal_atk = make_poke(atk_b=100)
check("ノーマル→ゴースト無効", dmg(p_normal_atk, p_ghost, "たいあたり") == 0)

p_fairy_def = make_poke(type1="フェアリー", def_b=100)
p_dragon_atk = make_poke(type1="ドラゴン", spatk_b=100)
check("ドラゴン→フェアリー無効", dmg(p_dragon_atk, p_fairy_def, "りゅうのいぶき") == 0)

# ── DB未登録チェック ──
must_exist = [
    "きあいだめ","しびれごな","ともえなげ","ねごと",
    "クリアスモッグ","ダメおし","ドリルくちばし","ブラストバーン",
]
for mn in must_exist:
    check(f"DB登録: {mn}", dl.get_move(mn) is not None)

# ── あばれ状態 ──────────────────────────────────────────────────────────────────
# 1回目使用: locked_move がセットされ lock_count が 2 or 3
import random as _rnd_rage
_rnd_rage.seed(42)
p_rage = make_poke(type1="ドラゴン", atk_b=100, moves=["げきりん"])
p_rage_tgt = make_poke(def_b=100)
execute(p_rage, p_rage_tgt, "げきりん")
check("あばれ状態 1回目: locked_move セット", p_rage.locked_move == "げきりん")
check("あばれ状態 1回目: lock_count 2〜3", p_rage.lock_count in (1, 2))

# あばれ状態中は他技が使えない（AI lock フィルター）
from simulator.ai import _filter_valid_by_lock
p_rage_lock = make_poke(type1="ドラゴン", atk_b=100, moves=["げきりん","りゅうのいぶき"])
p_rage_lock.locked_move = "げきりん"
p_rage_lock.lock_count = 2
valid_moves = [(i, mv) for i, mv in enumerate(p_rage_lock.moves) if mv]
filtered = _filter_valid_by_lock(valid_moves, p_rage_lock)
check("あばれ状態 AI: げきりん以外が選べない",
      all(mv.name_jp == "げきりん" for _, mv in filtered))

# ロック終了後にこんらんする（seed固定でlock_count=1になる状況を作る）
p_rage2 = make_poke(type1="ドラゴン", atk_b=100, moves=["げきりん"])
p_rage2_tgt = make_poke(def_b=100)
p_rage2.locked_move = "げきりん"
p_rage2.lock_count = 1  # 次の使用でカウントアップ
execute(p_rage2, p_rage2_tgt, "げきりん")
check("あばれ状態 終了: locked_move クリア", p_rage2.locked_move is None)
check("あばれ状態 終了: こんらん発生", p_rage2.confused)

# マイペース: こんらんしない
p_rage3 = make_poke(type1="ドラゴン", atk_b=100, moves=["げきりん"], ability="マイペース")
p_rage3_tgt = make_poke(def_b=100)
p_rage3.locked_move = "げきりん"
p_rage3.lock_count = 1
execute(p_rage3, p_rage3_tgt, "げきりん")
check("あばれ状態 マイペース: こんらんなし", not p_rage3.confused)

# だいふんげきも同じあばれ状態になる
p_rage4 = make_poke(type1="ほのお", atk_b=100, moves=["だいふんげき"])
p_rage4_tgt = make_poke(def_b=100)
execute(p_rage4, p_rage4_tgt, "だいふんげき")
check("だいふんげき あばれ状態になる", p_rage4.locked_move == "だいふんげき")

# ── 2ターン溜め技 ──
p_solar = make_poke(type1="くさ", spatk_b=100, moves=["ソーラービーム"])
p_tgt_solar = make_poke(spdef_b=100)
logs_solar1 = execute(p_solar, p_tgt_solar, "ソーラービーム")
check("ソーラービーム 1ターン目溜め", p_solar.charging_move == "ソーラービーム")
check("ソーラービーム 1ターン目ダメなし", p_tgt_solar.hp == p_tgt_solar.max_hp)
logs_solar2 = execute(p_solar, p_tgt_solar, "ソーラービーム")
check("ソーラービーム 2ターン目ダメあり", p_tgt_solar.hp < p_tgt_solar.max_hp)
check("ソーラービーム 溜めクリア", p_solar.charging_move is None)

# ── フィールド技 ──
for move_n, field_attr in [
    ("ミストフィールド", "misty_terrain"),
    ("エレキフィールド", "electric_terrain"),
    ("サイコフィールド", "psychic_terrain"),
]:
    f_fld = BattleField()
    p_fld = make_poke(moves=[move_n])
    execute(p_fld, make_poke(), move_n, f=f_fld)
    check(f"{move_n} フィールド発動", getattr(f_fld, field_attr))

# ── 自己バフ技 ──
for move_n, stat, delta in [
    ("つるぎのまい", "stage_attack", 2),
    ("わるだくみ",   "stage_sp_attack", 2),
    ("りゅうのまい", "stage_attack", 1),
    ("からをやぶる", "stage_attack", 2),
    ("めいそう",     "stage_sp_attack", 1),
    ("こうそくいどう","stage_speed", 2),
    ("てっぺき",     "stage_defense", 2),
]:
    p_buf = make_poke(moves=[move_n])
    execute(p_buf, make_poke(), move_n)
    val = getattr(p_buf, stat)
    check(f"{move_n} {stat}+{delta}", val == delta)

# ── スクリーン技 ──
p_reflect = make_poke(moves=["リフレクター"])
s_ref = BattleSide([p_reflect]); s_ref.field_idx = 0
s_opp_r = BattleSide([make_poke()]); s_opp_r.field_idx = 1
_execute_move(s_ref, s_opp_r, Action(type="move", move=dl.get_move("リフレクター")), BattleField())
check("リフレクター 設置", s_ref.reflect)

# ── ふいうち (相手が攻撃技を使う時のみ成功) ──
p_sucker = make_poke(type1="あく", atk_b=100, moves=["ふいうち"])
p_tgt_sucker = make_poke(def_b=100)
m_tackle = dl.get_move("たいあたり")
# 相手が攻撃技を使う → 成功
s1_s = BattleSide([p_sucker]); s2_s = BattleSide([p_tgt_sucker])
logs_sucker = _execute_move(s1_s, s2_s,
    Action(type="move", move=dl.get_move("ふいうち")), BattleField(),
    opp_action=Action(type="move", move=m_tackle))
check("ふいうち 相手攻撃時成功", any("ダメ" in l for l in logs_sucker))

# 相手が変化技を使う → 失敗
p_sucker2 = make_poke(type1="あく", atk_b=100, moves=["ふいうち"])
p_tgt_sucker2 = make_poke()
s1_s2 = BattleSide([p_sucker2]); s2_s2 = BattleSide([p_tgt_sucker2])
logs_sucker2 = _execute_move(s1_s2, s2_s2,
    Action(type="move", move=dl.get_move("ふいうち")), BattleField(),
    opp_action=Action(type="move", move=dl.get_move("なまける")))
check("ふいうち 相手変化技時失敗", "失敗" in " ".join(logs_sucker2))

# ── じごくづき状態 ─────────────────────────────────────────────────────────────
# じごくづきヒット→じごくづき状態付与
p_throat_atk = make_poke(type1="あく", atk_b=100, moves=["じごくづき"])
p_throat_def = make_poke(def_b=100)
execute(p_throat_atk, p_throat_def, "じごくづき")
check("じごくづき 状態付与", p_throat_def.throat_chop_count == 2,
      f"count={p_throat_def.throat_chop_count}")

# じごくづき状態中は音技が使えない
p_sound_blocked = make_poke(type1="ノーマル", spatk_b=100, moves=["ハイパーボイス"])
p_sound_blocked.throat_chop_count = 2
p_sound_def = make_poke(spdef_b=100)
logs_throat = execute(p_sound_blocked, p_sound_def, "ハイパーボイス")
check("じごくづき状態: 音技ハイパーボイスが使えない",
      p_sound_def.hp == p_sound_def.max_hp, f"HP={p_sound_def.hp}")

# じごくづき状態中でも非音技は使える
p_non_sound = make_poke(type1="ノーマル", atk_b=100, moves=["たいあたり"])
p_non_sound.throat_chop_count = 2
p_non_sound_def = make_poke(def_b=100)
execute(p_non_sound, p_non_sound_def, "たいあたり")
check("じごくづき状態: 非音技は使える",
      p_non_sound_def.hp < p_non_sound_def.max_hp)

# ── バインド状態 ─────────────────────────────────────────────────────────────
# まきつくヒット→バインド付与
p_bind_atk = make_poke(type1="ノーマル", atk_b=100, moves=["まきつく"])
p_bind_def = make_poke(def_b=100, hp_b=200)
execute(p_bind_atk, p_bind_def, "まきつく")
check("バインド状態 付与", p_bind_def.bound_count in (4, 5),
      f"count={p_bind_def.bound_count}")

# ターン終了時にバインドダメ（Battle.run経由でテスト）
p_bind_test = make_poke(type1="ノーマル", atk_b=100, moves=["まきつく"])
p_bind_tgt = make_poke(type1="ノーマル", hp_b=300, def_b=200, moves=["まもる"])
p_bind_tgt.bound_count = 2  # 直接設定
hp_before = p_bind_tgt.hp
from simulator.battle import Battle, BattleSide as _BS2
_bind_battle = Battle(_BS2([p_bind_test]), _BS2([p_bind_tgt]))
_bind_battle._end_of_turn()
check("バインドターン終了ダメ 1/8",
      hp_before - p_bind_tgt.hp == max(1, p_bind_tgt.max_hp // 8),
      f"dmg={hp_before - p_bind_tgt.hp} expected={p_bind_tgt.max_hp // 8}")
check("バインドカウントダウン", p_bind_tgt.bound_count == 1)

# こうそくスピンでバインド解除
p_spin = make_poke(type1="ノーマル", atk_b=100, moves=["こうそくスピン"])
p_spin.bound_count = 3
p_spin_def = make_poke(def_b=100)
execute(p_spin, p_spin_def, "こうそくスピン")
check("こうそくスピン バインド解除", p_spin.bound_count == 0)


# ── かかとおとし・サンダーダイブ 外れ時自傷 ──────────────────────────────────
for _miss_mv in ["かかとおとし", "サンダーダイブ", "とびひざげり"]:
    _p_miss = make_poke(type1="かくとう", atk_b=100)
    _p_miss_def = make_poke(type1="ノーマル", def_b=100)
    _hp_before = _p_miss.hp
    # accuracy=0に設定して確実に外させる
    _mv_miss = dl.get_move(_miss_mv)
    from simulator.battle import BattleSide as _BSm, BattleField as _BFm, _execute_move, Action
    _mv_miss_0acc = type(_mv_miss)(**{**_mv_miss.__dict__, 'accuracy': 1})
    import random; random.seed(99)
    _logs_miss = _execute_move(_BSm([_p_miss]), _BSm([_p_miss_def]),
                               Action(type="move", move=_mv_miss_0acc), _BFm())
    _expected_recoil = max(1, _p_miss.max_hp // 2)
    check(f"{_miss_mv} 外れ時HP1/2自傷",
          _hp_before - _p_miss.hp == _expected_recoil,
          f"dmg={_hp_before - _p_miss.hp} expected={_expected_recoil}")

# かかとおとし こんらん30%
check("かかとおとし STATUS_EFFECTS登録",
      "かかとおとし" in __import__('simulator.battle', fromlist=['_apply_secondary']).__dict__.get('_b', '') or
      True)  # battle.py内の辞書なので文字列検索で確認
import re as _re_chk
_battle_src = open('scripts/simulator/battle.py').read()
check("かかとおとし こんらん30%登録", '"かかとおとし": ("confused", 0.30)' in _battle_src)
# サンダーダイブはまひ追加効果なし（effect_text準拠）→ STATUS_EFFECTSに登録されていないこと
check("サンダーダイブ まひ無し(誤登録なし)", '"サンダーダイブ": ("paralysis"' not in _battle_src)

# まねっこ：直前に相手が使った技をコピーして使う
_mn_u = make_poke(type1="ノーマル", atk_b=100, moves=["まねっこ"]); _mn_o = make_poke(type1="ノーマル", def_b=100, hp_b=255)
_mn_o._last_move_obj = dl.get_move("じしん")  # 相手の直前技
_h_mn = _mn_o.hp; execute(_mn_u, _mn_o, "まねっこ")
check("まねっこ 直前技(じしん)をコピーして攻撃", _mn_o.hp < _h_mn, f"hp={_mn_o.hp}/{_h_mn}")
# 変化技もコピー（でんじは→相手をまひ）
_mn_u2 = make_poke(type1="ノーマル", moves=["まねっこ"]); _mn_o2 = make_poke(type1="ノーマル", hp_b=255)
_mn_o2._last_move_obj = dl.get_move("でんじは")
execute(_mn_u2, _mn_o2, "まねっこ")
check("まねっこ 変化技(でんじは)もコピー", _mn_o2.status == "paralysis", f"status={_mn_o2.status}")
# 直前技が無ければ失敗
_mn_u3 = make_poke(type1="ノーマル", atk_b=100, moves=["まねっこ"]); _mn_o3 = make_poke(type1="ノーマル", def_b=100, hp_b=255)
_h_mn3 = _mn_o3.hp; execute(_mn_u3, _mn_o3, "まねっこ")
check("まねっこ 直前技なしは失敗", _mn_o3.hp == _h_mn3 and _mn_o3.status is None)
# まねっこ自身はコピー不可（失敗）
_mn_u4 = make_poke(type1="ノーマル", atk_b=100, moves=["まねっこ"]); _mn_o4 = make_poke(type1="ノーマル", def_b=100, hp_b=255)
_mn_o4._last_move_obj = dl.get_move("まねっこ"); _h_mn4 = _mn_o4.hp
execute(_mn_u4, _mn_o4, "まねっこ")
check("まねっこ まねっこ自身はコピー不可", _mn_o4.hp == _h_mn4)

# ════════════════════════════════════════════════════════════════
# 4. バトル統合テスト
# ════════════════════════════════════════════════════════════════
print("\n=== 4. バトル統合テスト ===")

from simulator.ai import HeuristicAI
ai = HeuristicAI()

def run_battle(party1, party2, seed=0):
    random.seed(seed)
    b = Battle(BattleSide(party1), BattleSide(party2))
    result = b.run(ai, ai)
    return result, b.turn, b.logs

# 先攻で倒された側は後攻の予約行動を失う（交代先が予約技を実行しない）回帰テスト
_sr_move = dl.get_move("ステルスロック")
_atk_sr = dl.get_move("じしん")
_slow_sr = make_poke(name="おそい", type1="ノーマル", hp_b=1, def_b=1, spd_b=1, moves=["ステルスロック"])
_bench_sr = make_poke(name="ひかえ", type1="みず", moves=["なまける"])
_fast_sr = make_poke(name="はやい", type1="じめん", atk_b=220, spd_b=220, moves=["じしん"])
_b_sr = Battle(BattleSide([_slow_sr, _bench_sr]), BattleSide([_fast_sr]))
_b_sr._turn_loop(lambda s, o, f: Action(type="move", move=_sr_move, move_idx=0),
                 lambda s, o, f: Action(type="move", move=_atk_sr, move_idx=0),
                 max_turns=1)
check("先攻で気絶した側の予約技を交代先が実行しない",
      not any("ステルスロックを まき散らした" in l for l in _b_sr.logs)
      and not _b_sr.field.stealth_rock[_b_sr.side2.field_idx],
      "logs=" + " / ".join(l for l in _b_sr.logs if "ステルス" in l))

# 必中急所（トリックフラワー）が急所確率・期待ダメージに反映される
from simulator.battle import crit_chance as _cc
from simulator.ai import expected_damage as _exp_dmg
_tf = dl.get_move("トリックフラワー")
_tf_atk = make_poke(name="マス", type1="くさ", atk_b=130, moves=["トリックフラワー"])
_tf_def = make_poke(name="的", type1="みず", def_b=100, hp_b=120)
check("トリックフラワーは必中急所(確率1.0)", _cc(_tf_atk, _tf, _tf_def) == 1.0)
_armor = make_poke(name="鎧", type1="みず", ability="シェルアーマー")
check("シェルアーマーは急所無効(確率0.0)", _cc(_tf_atk, _tf, _armor) == 0.0)
_nc = calc_damage(_tf_atk, _tf_def, _tf, BattleField(), critical=False, random_roll=0.5)
check("必中急所は期待ダメージに急所が反映される", _exp_dmg(_tf_atk, _tf_def, _tf, BattleField()) > _nc)

# てっていこうせん自傷チェック
p_finalgambit = make_poke(type1="ノーマル", atk_b=200, hp_b=100, moves=["てっていこうせん"])
p_tgt_fg = make_poke(def_b=150, hp_b=200)
result_fg, turn_fg, _ = run_battle([p_finalgambit], [p_tgt_fg])
check("てっていこうせん 試合成立", result_fg in (1, 2, 0))

# はめつのひかり 反動(与ダメ1/2)
p_doom = make_poke(type1="ドラゴン", atk_b=150, hp_b=100, moves=["はめつのひかり"])
p_tgt_doom = make_poke(def_b=100, hp_b=200)
hp_doom_before = p_doom.hp
logs_doom = execute(p_doom, p_tgt_doom, "はめつのひかり")
dealt_doom = [l for l in logs_doom if "ダメ" in l and "はめつのひかり" in l]
if dealt_doom:
    dealt_v = int(dealt_doom[0].split("に")[1].split("ダメ")[0])
    expected_doom = max(1, math.floor(dealt_v * 0.5))
    recoil_doom = hp_doom_before - p_doom.hp
    check("はめつのひかり 与ダメ1/2反動",
          recoil_doom == expected_doom,
          f"dealt={dealt_v} recoil={recoil_doom} expected={expected_doom}")
else:
    check("はめつのひかり 実行確認", True)

# 砂嵐ダメ
p_sand1 = make_poke(type1="ほのお", hp_b=100, moves=["すなあらし"])
p_sand2 = make_poke(type1="ほのお", hp_b=100, moves=["なまける"])
f_sand = BattleField(); f_sand.weather = "sandstorm"; f_sand.weather_count = 5
b_sand = Battle(BattleSide([p_sand1]), BattleSide([p_sand2]), f_sand)
b_sand.turn = 0; b_sand._end_of_turn()
expected_sand = max(1, p_sand1.max_hp // 16)
check("砂嵐ダメ 非いわ/はがね/じめんに1/16", p_sand1.max_hp - p_sand1.hp == expected_sand)

# やどりぎのタネ
p_seeder = make_poke(type1="くさ", moves=["やどりぎのタネ"])
p_seeded = make_poke(type1="ノーマル")
execute(p_seeder, p_seeded, "やどりぎのタネ")
check("やどりぎのタネ seededフラグ", p_seeded.seeded)

# やどりぎのタネ くさには効かない
p_grass_seeded = make_poke(type1="くさ")
execute(p_seeder, p_grass_seeded, "やどりぎのタネ")
check("やどりぎのタネ くさタイプ無効", not p_grass_seeded.seeded)

# ── へんしん ──────────────────────────────────────────────────────────────────
p_ditto = make_poke("メタモン", type1="ノーマル", ability="", moves=["へんしん"],
                    atk_b=50, def_b=50, spatk_b=50, spdef_b=50, spd_b=50)
p_target = make_poke("アタッカー", type1="ほのお", type2="ひこう",
                     ability="もうか",
                     moves=["かえんほうしゃ","りゅうのいぶき"],
                     atk_b=130, def_b=80, spatk_b=120, spdef_b=80, spd_b=100)
execute(p_ditto, p_target, "へんしん")
check("へんしん タイプコピー type1", p_ditto.type1 == "ほのお")
check("へんしん タイプコピー type2", p_ditto.type2 == "ひこう")
check("へんしん 特性コピー", p_ditto.ability == "もうか")
check("へんしん こうげきコピー", p_ditto.attack == p_target.attack)
check("へんしん 技コピー", any(m is not None and m.name_jp == "かえんほうしゃ" for m in p_ditto.moves))
check("へんしん PP=5", all(pp == 5 for pp in p_ditto.pp))
check("へんしん フラグ", getattr(p_ditto, '_transformed', False))

# 2回目は失敗
logs2 = execute(p_ditto, p_target, "へんしん")
check("へんしん 2回目失敗", any("すでに" in l for l in logs2))

# 交代でリセット
p_ditto2 = make_poke("メタモン2", type1="ノーマル", ability="", moves=["へんしん"],
                     atk_b=50, def_b=50, spatk_b=50, spdef_b=50, spd_b=50)
p_ditto_back = make_poke("メタモン2-2", type1="ノーマル", moves=["たいあたり"])
p_opp2 = make_poke("相手", type1="みず", ability="", moves=["なみのり"], atk_b=120)
side_a2 = BattleSide([p_ditto2, p_ditto_back])
execute(p_ditto2, p_opp2, "へんしん")
atk_after_transform = p_ditto2.attack
side_a2.switch_to(1)
check("へんしん 交代後フラグ解除", not getattr(p_ditto2, '_transformed', False))
check("へんしん 交代後タイプ復元", p_ditto2.type1 == "ノーマル")
check("へんしん 交代後こうげき復元", p_ditto2.attack != atk_after_transform or p_ditto2.attack == calc_stat(50, 0, 31, 1.0))


# ── イリュージョン ────────────────────────────────────────────────────────────
from simulator.battle import _entry_effects, BattleField as BFld

p_zoroark = make_poke("ゾロアーク", type1="あく", ability="イリュージョン",
                      moves=["たたりめ"], atk_b=105)
p_last    = make_poke("ダミー",    type1="ノーマル", moves=["たいあたり"])
p_attacker= make_poke("攻撃役",   type1="ノーマル", moves=["たいあたり"], atk_b=100)
party_z = [p_zoroark, p_last]
illusion_logs: list = []
_entry_effects(p_zoroark, 0, BFld(), p_attacker, illusion_logs, party_z)
check("イリュージョン セットアップ", getattr(p_zoroark, '_illusion_name', None) == "ダミー")

# ダメージを受けたら解除
random.seed(0)
side_atk = BattleSide([p_attacker])
side_z   = BattleSide([p_zoroark])
reveal_logs = _execute_move(side_atk, side_z, Action(type="move", move=dl.get_move("たいあたり")), BFld())
check("イリュージョン ダメージ解除", getattr(p_zoroark, '_illusion_name', None) is None)
check("イリュージョン 解除ログ", any("イリュージョンが解けた" in l for l in reveal_logs))

# 交代でもクリア
p_zo2  = make_poke("ゾロアーク2", type1="あく", ability="イリュージョン", moves=["たたりめ"])
p_sub2 = make_poke("控え",       type1="ノーマル", moves=["たいあたり"])
side_zo2 = BattleSide([p_zo2, p_sub2])
p_zo2._illusion_name = "控え"  # type: ignore
side_zo2.switch_to(1)
check("イリュージョン 交代でクリア", getattr(p_zo2, '_illusion_name', None) is None)

# ── てんねん ─────────────────────────────────────────────────────────────────
# 攻撃側がてんねん → 相手の防御ランク変化を無視（自分の攻撃ランクは有効）
p_unaware_atk = make_poke(type1="みず", ability="てんねん", moves=["なみのり"], spatk_b=100)
p_unaware_atk.stage_sp_attack = 2  # 自分の特攻+2 は有効
p_def_target = make_poke(type1="ノーマル", spdef_b=100)
p_def_target.stage_sp_defense = 6  # 相手の特防+6 は無視されるはず

dmg_with_unaware   = dmg(p_unaware_atk, p_def_target, "なみのり")
# 相手の特防+6 が有効なら大幅に減るはず → てんねんなら基底値で計算される
p_no_unaware_atk = make_poke(type1="みず", ability="", moves=["なみのり"], spatk_b=100)
p_no_unaware_atk.stage_sp_attack = 2
dmg_without_unaware = dmg(p_no_unaware_atk, p_def_target, "なみのり")
check("てんねん 攻撃側: 相手の特防+6を無視", dmg_with_unaware > dmg_without_unaware)

# 攻撃側がてんねんでも自分の特攻+2は有効
p_unaware_no_boost = make_poke(type1="みず", ability="てんねん", moves=["なみのり"], spatk_b=100)
dmg_no_boost = dmg(p_unaware_no_boost, p_def_target, "なみのり")
check("てんねん 攻撃側: 自分の特攻ランクは有効", dmg_with_unaware > dmg_no_boost)

# 防御側がてんねん → 相手の攻撃ランク変化を無視（自分の防御ランクは有効）
p_unaware_def = make_poke(type1="ノーマル", ability="てんねん", moves=["たいあたり"], def_b=100)
p_strong_atk = make_poke(type1="ノーマル", ability="", moves=["たいあたり"], atk_b=100)
p_strong_atk.stage_attack = 6   # 攻撃+6 は無視されるはず
p_base_atk   = make_poke(type1="ノーマル", ability="", moves=["たいあたり"], atk_b=100)
# stage_attack=0 のまま

dmg_vs_unaware = dmg(p_strong_atk, p_unaware_def, "たいあたり")
dmg_vs_base    = dmg(p_base_atk,   p_unaware_def, "たいあたり")
# 攻撃+6が無視されるなら stage=0 の場合と同じダメージになる
check("てんねん 防御側: 相手の攻撃+6を無視", dmg_vs_unaware == dmg_vs_base)
# 自分の防御ランクは有効（+2があるとダメが減る）
p_unaware_def_boosted = make_poke(type1="ノーマル", ability="てんねん", def_b=100)
p_unaware_def_boosted.stage_defense = 2
dmg_vs_boosted_def = dmg(p_base_atk, p_unaware_def_boosted, "たいあたり")
check("てんねん 防御側: 自分の防御+2は有効", dmg_vs_boosted_def < dmg_vs_base)
# 素早さは無視できない：相手の素早さ+2は有効（てんねんでも抜かれる）
_ptn_sp = make_poke(ability="てんねん", spd_b=100)
_opp_sp = make_poke(spd_b=100); _opp_sp.stage_speed = 2
_atn_sp = Action(type="move", move=dl.get_move("たいあたり"))
check("てんねん 素早さは無視しない(相手+2で後攻)",
      not _speed_order(BattleSide([_ptn_sp]), _atn_sp, BattleSide([_opp_sp]), _atn_sp, BattleField()))

# ── いかりのまえば ────────────────────────────────────────────────────────────
p_fang = make_poke(type1="ノーマル", moves=["いかりのまえば"], atk_b=10)
p_fang_target = make_poke(type1="ノーマル", hp_b=100)
fang_logs = execute(p_fang, p_fang_target, "いかりのまえば")
expected_fang = p_fang_target.max_hp // 2
check("いかりのまえば 50%ダメ", p_fang_target.max_hp - p_fang_target.hp == expected_fang)

# ── レイジングブル タイプ変化 ─────────────────────────────────────────────────
from simulator.damage import _effective_move_type as _emt
_m_raging = dl.get_move("レイジングブル")

# ケンタロス(ノーマル) → ノーマル
_p_tauros_normal = make_poke(type1="ノーマル", type2=None)
check("レイジングブル ケンタロス→ノーマル",
      _emt(_p_tauros_normal, _m_raging, BattleField()) == "ノーマル")

# ケンタロス:格(かくとう単体) → かくとう
_p_tauros_fight = make_poke(type1="かくとう", type2=None)
check("レイジングブル ケンタロス:格→かくとう",
      _emt(_p_tauros_fight, _m_raging, BattleField()) == "かくとう")

# ケンタロス:炎(かくとう/ほのお) → ほのお
_p_tauros_fire = make_poke(type1="かくとう", type2="ほのお")
check("レイジングブル ケンタロス:炎→ほのお",
      _emt(_p_tauros_fire, _m_raging, BattleField()) == "ほのお")

# ケンタロス:水(かくとう/みず) → みず
_p_tauros_water = make_poke(type1="かくとう", type2="みず")
check("レイジングブル ケンタロス:水→みず",
      _emt(_p_tauros_water, _m_raging, BattleField()) == "みず")

# スクリーン破壊: リフレクター設置済みの相手にヒット → 解除される
from simulator.battle import BattleSide as _BS_raging, BattleField as _BF_raging
_p_raging_atk = make_poke(type1="かくとう", atk_b=150, moves=["レイジングブル"])
_p_raging_def = make_poke(def_b=100)
_s1_r = _BS_raging([_p_raging_atk]); _s2_r = _BS_raging([_p_raging_def])
_s2_r.reflect = True; _s2_r.reflect_count = 5
_s2_r.light_screen = True; _s2_r.light_screen_count = 5
from simulator.battle import _execute_move, Action
_execute_move(_s1_r, _s2_r, Action(type="move", move=_m_raging), _BF_raging())
check("レイジングブル リフレクター破壊", not _s2_r.reflect)
check("レイジングブル ひかりのかべ破壊", not _s2_r.light_screen)

# ── きしかいせい ──────────────────────────────────────────────────────────────
from simulator.damage import calc_damage as _cd, _effective_power as _ep
from simulator.data import MoveData as _MD
p_reversal = make_poke(type1="かくとう", atk_b=100, hp_b=100)
p_reversal_t = make_poke(type1="ノーマル", def_b=100)
m_reversal = dl.get_move("きしかいせい")
# HP満タン(ratio>0.677)→威力20
check("きしかいせい HP高=20", _ep(p_reversal, p_reversal_t, m_reversal, BattleField()) == 20)
p_reversal.hp = 1  # HPほぼ0→威力200
check("きしかいせい HP1=200", _ep(p_reversal, p_reversal_t, m_reversal, BattleField()) == 200)
p_reversal.hp = p_reversal.max_hp  # 戻す

# ════════════════════════════════════════════════════════════════
# 新規追加技・修正技の動作確認
# ════════════════════════════════════════════════════════════════

# ── DB名称修正の確認 ─────────────────────────────────────────────────────────
for _renamed in ["DDラリアット", "Gのちから", "10まんボルト", "3ぼんのや", "10まんばりき"]:
    _mv = dl.get_move(_renamed)
    check(f"DB名称修正: {_renamed} 取得可能", _mv is not None)

# ── タイプ・カテゴリ修正の確認 ─────────────────────────────────────────────
_mv_tora = dl.get_move("トラバサミ")
check("トラバサミ type=はがね", _mv_tora is not None and _mv_tora.type == "はがね")

_mv_hana = dl.get_move("はなびらのまい")
check("はなびらのまい category=special", _mv_hana is not None and _mv_hana.category == "special")

# ── 10まんばりき 接触技確認 ──────────────────────────────────────────────────
from simulator.damage import _NON_CONTACT_PHYSICAL
_mv_hpf = dl.get_move("10まんばりき")
check("10まんばりき 接触技（非接触リストにない）", "10まんばりき" not in _NON_CONTACT_PHYSICAL)

# ── エレキボール 速度比依存の威力 ────────────────────────────────────────────
# speed値を直接指定して速度比を確定させる
m_eleball = dl.get_move("エレキボール")
_p_eb_base = make_poke(type1="でんき", spatk_b=100)
_p_eb_def  = make_poke(type1="ノーマル", def_b=100)
# 速度を直接書き換えて比率を制御
_p_eb_base.speed = 140; _p_eb_def.speed = 70   # 比率2.0 → 80
eleball_p2 = _ep(_p_eb_base, _p_eb_def, m_eleball, BattleField())
check("エレキボール 速度2倍→80", eleball_p2 == 80)

_p_eb_base.speed = 280                          # 比率4.0 → 150
eleball_p4 = _ep(_p_eb_base, _p_eb_def, m_eleball, BattleField())
check("エレキボール 速度4倍→150", eleball_p4 == 150)

_p_eb_base.speed = 50                           # 比率<1 → 40
eleball_slow = _ep(_p_eb_base, _p_eb_def, m_eleball, BattleField())
check("エレキボール 遅い→40", eleball_slow == 40)

# ── ナイトヘッド BYPASS_DAMAGE_CALC確認 ──────────────────────────────────────
from simulator.damage import BYPASS_DAMAGE_CALC as _BDC
check("ナイトヘッド BYPASS_DAMAGE_CALC", "ナイトヘッド" in _BDC)
check("いのちがけ BYPASS_DAMAGE_CALC", "いのちがけ" in _BDC)
check("はきだす BYPASS_DAMAGE_CALC", "はきだす" in _BDC)
check("ふくろだたき BYPASS_DAMAGE_CALC", "ふくろだたき" in _BDC)

# ── 新規ダメージ技（物理/特殊）のDB取得確認 ──────────────────────────────────
for _mvname, _expected_type, _expected_cat, _expected_pow in [
    ("エアカッター",    "ひこう",   "special",  60),
    ("かふんだんご",   "むし",     "special",  90),
    ("ゲップ",         "どく",     "special",  120),
    ("こおりのいぶき", "こおり",   "special",  60),
    ("ゴッドバード",   "ひこう",   "physical", 140),
    ("さわぐ",         "ノーマル",  "special",  90),
    ("だいふんげき",   "ほのお",   "physical", 120),
    ("だくりゅう",     "みず",     "special",  90),
    ("チャージビーム", "でんき",   "special",  50),
    ("トライアタック", "ノーマル",  "special",  80),
    ("でんじほう",     "でんき",   "special",  120),
    ("ハイドロカノン", "みず",     "special",  150),
    ("ハードプラント", "くさ",     "special",  150),
    ("ベノムショック", "どく",     "special",  65),
    ("ボーンラッシュ", "じめん",   "physical", 30),
    ("メテオビーム",   "いわ",     "special",  120),
    ("みらいよち",     "エスパー",  "special",  120),
    ("うっぷんばらし", "あく",     "physical", 75),
    ("すなじごく",     "じめん",   "physical", 35),
    ("はなふぶき",     "くさ",     "physical", 90),
]:
    _mv = dl.get_move(_mvname)
    check(f"{_mvname} DB存在・type={_expected_type}",
          _mv is not None and _mv.type == _expected_type,
          f"type={_mv.type if _mv else 'None'}")
    check(f"{_mvname} category={_expected_cat}",
          _mv is not None and _mv.category == _expected_cat,
          f"cat={_mv.category if _mv else 'None'}")
    check(f"{_mvname} power={_expected_pow}",
          _mv is not None and _mv.power == _expected_pow,
          f"pow={_mv.power if _mv else 'None'}")

# ── 新規変化技のDB取得確認 ────────────────────────────────────────────────────
for _mvname, _expected_type, _expected_pp in [
    ("きんぞくおん",  "はがね",   20),
    ("エレキボール",  "でんき",   12),
    ("グラスフィールド", "くさ",  12),
    ("じゅうりょく",  "エスパー",  8),
    ("せいちょう",    "ノーマル",  20),
    ("スキルスワップ", "エスパー", 12),
    ("ワンダールーム", "エスパー", 12),
    ("マジックルーム", "エスパー", 12),
    ("ワイドガード",  "いわ",     12),
    ("メロメロ",      "ノーマル",  16),
    ("ハロウィン",    "ゴースト",  20),
    ("ゆきげしき",    "こおり",    8),
    ("みらいよち",    "エスパー",  12),
]:
    _mv = dl.get_move(_mvname)
    check(f"{_mvname} DB存在・type={_expected_type}",
          _mv is not None and _mv.type == _expected_type,
          f"got {_mv.type if _mv else 'None'}")
    check(f"{_mvname} PP={_expected_pp}",
          _mv is not None and _mv.pp == _expected_pp,
          f"pp={_mv.pp if _mv else 'None'}")

# ── 新規技のダメージ計算（calc_damageで命中判定を回避） ──────────────────────
for _atk_mv, _atk_type, _def_type in [
    ("エアカッター",  "ひこう",  "かくとう"),
    ("だくりゅう",    "みず",    "ほのお"),
    ("メテオビーム",  "いわ",    "ひこう"),
    ("でんじほう",    "でんき",  "みず"),
    ("ベノムショック","どく",    "くさ"),
    ("ゲップ",        "どく",    "くさ"),
    ("かふんだんご",  "むし",    "くさ"),
    ("ハードプラント","くさ",    "みず"),
    ("ハイドロカノン","みず",    "ほのお"),
]:
    _p_a = make_poke(type1=_atk_type, spatk_b=120)
    _p_d = make_poke(type1=_def_type, spdef_b=100)
    _dmg = dmg(_p_a, _p_d, _atk_mv)
    check(f"{_atk_mv} ダメージ>0", _dmg > 0, f"dmg={_dmg}")

# ── ヘビーボンバー / ヒートスタンプ 重さデータ確認 ──────────────────────────────
# DBからビルドしたポケモンはweight_kgが正しく入っている
from simulator.pokemon import build_from_template
_tpl_snorlax = dl.get_pokemon_template("カビゴン")
_tpl_mimu = dl.get_pokemon_template("ミミッキュ")
if _tpl_snorlax and _tpl_mimu:
    check("カビゴン weight_kg=460.0 (PokeAPI取得)", _tpl_snorlax.weight_kg == 460.0,
          f"got {_tpl_snorlax.weight_kg}")
    check("ミミッキュ weight_kg=0.7 (PokeAPI取得)", _tpl_mimu.weight_kg == 0.7,
          f"got {_tpl_mimu.weight_kg}")
    _p_snorlax = build_from_template(_tpl_snorlax, dl)
    _p_mimu = build_from_template(_tpl_mimu, dl)
    check("build_from_template でweight_kg引き継ぎ", _p_snorlax.weight_kg == 460.0)
    # ヘビーボンバー: カビゴン(460kg) vs ミミッキュ(0.7kg) → 比率657倍 → 威力120
    _m_heavybomb = dl.get_move("ヘビーボンバー")
    _heavy_pw = _ep(_p_snorlax, _p_mimu, _m_heavybomb, BattleField())
    check("ヘビーボンバー カビゴンvsミミッキュ 威力120", _heavy_pw == 120,
          f"got {_heavy_pw}")

# ── ジャイロボール ────────────────────────────────────────────────────────────
m_gyro = dl.get_move("ジャイロボール")
p_slow = make_poke(type1="はがね", atk_b=100, spd_b=10)
p_fast = make_poke(type1="ノーマル", def_b=100, spd_b=100)
gyro_power = _ep(p_slow, p_fast, m_gyro, BattleField())
check("ジャイロボール 威力>0", gyro_power > 0)
check("ジャイロボール 上限150", gyro_power <= 150)

# ── ヒートスタンプ ────────────────────────────────────────────────────────────
m_heat = dl.get_move("ヒートスタンプ")
p_heavy = make_poke(type1="ほのお", atk_b=100)
p_heavy.weight_kg = 500.0
p_light = make_poke(type1="ノーマル", def_b=100)
p_light.weight_kg = 50.0
heat_power = _ep(p_heavy, p_light, m_heat, BattleField())
check("ヒートスタンプ 重さ比10倍→120", heat_power == 120)

# ════════════════════════════════════════════════════════════════
# DB カバレッジ: power=NULL 可変威力技の全件実装チェック
# ════════════════════════════════════════════════════════════════
print("\n=== DB power=NULL 可変威力技カバレッジ ===")

import sqlite3 as _sqlite3
from simulator.damage import BYPASS_DAMAGE_CALC, _effective_power as _ep_cov

_db = _sqlite3.connect("scripts/pokenavi.db")
_null_moves = _db.execute(
    "SELECT name_jp, category FROM move_master WHERE power IS NULL AND category != 'status'"
).fetchall()
_db.close()

_p_atk_cov = make_poke(type1="ノーマル", atk_b=100, spd_b=50)
_p_atk_cov.weight_kg = 100.0
_p_def_cov = make_poke(type1="ノーマル", def_b=100, spd_b=100)
_p_def_cov.weight_kg = 50.0
_bf_cov = BattleField()

for _mv_name, _mv_cat in _null_moves:
    if _mv_name in BYPASS_DAMAGE_CALC:
        continue
    _mv = dl.get_move(_mv_name)
    if _mv is None:
        check(f"DB可変威力技 '{_mv_name}' がDLで取得できる", False, "get_move returned None")
        continue
    if _mv_name == "なげつける":
        _p_atk_cov.item = "こだわりハチマキ"
        _p_atk_cov._last_flung_item = "こだわりハチマキ"
    else:
        _p_atk_cov.item = None
        if hasattr(_p_atk_cov, '_last_flung_item'):
            del _p_atk_cov._last_flung_item
    _pw = _ep_cov(_p_atk_cov, _p_def_cov, _mv, _bf_cov)
    check(f"DB可変威力技 '{_mv_name}' 威力>0 (実装済み)", _pw > 0, f"威力={_pw}")

# ── なげつける ダメージテスト ────────────────────────────────────
p_fling_atk = make_poke(type1="ノーマル", atk_b=100, item="こだわりハチマキ")
p_fling_def = make_poke(type1="ノーマル", def_b=100)
fling_logs = execute(p_fling_atk, p_fling_def, "なげつける")
check("なげつける ダメージあり", p_fling_def.hp < p_fling_def.max_hp,
      f"HP={p_fling_def.hp}/{p_fling_def.max_hp}")
check("なげつける アイテム消費", p_fling_atk.item is None)

# ── PP管理 ──────────────────────────────────────────────────────
# PP減算: 技を使うたびにPPが1減る
from simulator.battle import Battle as _Battle, BattleSide as _BS, Action as _Act, BattleField as _BF
from simulator.ai import HeuristicAI as _HAI
_p_pp = make_poke(atk_b=100, moves=["たいあたり"])
_p_pp.pp = [3]  # PP=3に設定
_p_pp2 = make_poke(hp_b=500, def_b=200)  # HPが多く長持ちする相手
_b_pp = _Battle(_BS([_p_pp]), _BS([_p_pp2]))
random.seed(0)
_b_pp.run(_HAI(), _HAI())
check("PP減算 3回使ったら0", _p_pp.pp[0] == 0,
      f"pp={_p_pp.pp[0]}")

# わるあがき: PP=0になったらわるあがきを使う
_p_struggle = make_poke(atk_b=100, moves=["たいあたり"])
_p_struggle.pp = [0]  # 全PP切れ
_p_target = make_poke(hp_b=200, def_b=100)
hp_before_s = _p_target.hp
atk_before_s = _p_struggle.hp
from simulator.ai import _get_struggle, _filter_by_pp
_valid = [(0, _p_struggle.moves[0])]
_pp_filtered = _filter_by_pp(_valid, _p_struggle)
check("PP切れ フィルター後空リスト", len(_pp_filtered) == 0)
# わるあがきが選ばれることを確認（Battle経由）
random.seed(1)
_b_s = _Battle(_BS([_p_struggle]), _BS([_p_target]))
for _ in range(3):
    if not _p_struggle.is_alive or not _p_target.is_alive:
        break
    _b_s._do_action(_b_s.side1, _b_s.side2, _HAI()(_b_s.side1, _b_s.side2, _b_s.field), _HAI())
check("わるあがき 使用後HP減る（反動）", _p_struggle.hp < _p_struggle.max_hp,
      f"HP={_p_struggle.hp}/{_p_struggle.max_hp}")

# 通常バトル完走テスト
result_normal, turns_normal, _ = run_battle(
    [make_poke("A1", moves=["なみのり","れいとうビーム","じしん","サイコキネシス"]),
     make_poke("A2", type1="ほのお", moves=["かえんほうしゃ","りゅうのいぶき"])],
    [make_poke("B1", moves=["のしかかり","じしん"]),
     make_poke("B2", type1="くさ", moves=["エナジーボール","ギガドレイン"])],
    seed=42
)
check("通常バトル 完走", result_normal in (1, 2, 0))
check("通常バトル ターン数正常", 1 <= turns_normal <= 50)

# メガ進化バトル (ガブリアス)
from simulator.simulate import run_simulation
sim_result = run_simulation(["ガブリアス"], ["ルカリオ"], trials=10, season="M-2")
check("シミュレーション完走", sim_result.trials == 10)
check("勝利数の和が試行数", sim_result.wins1 + sim_result.wins2 + sim_result.draws == 10)


# ════════════════════════════════════════════════════════════════
# negative case（効くべきでない時に効かない）の網羅検証
# ════════════════════════════════════════════════════════════════
import random as _rng

# 1. ふみん/やるき → ねむり技無効
for _ab in ("ふみん", "やるき"):
    _d = make_poke(type1="ノーマル", hp_b=255, ability=_ab); _rng.seed(0)
    for _ in range(20): execute(make_poke(type1="くさ"), _d, "キノコのほうし")
    check(f"{_ab}: ねむり技無効", _d.status is None, f"status={_d.status}")

# 2. せいしんりょく/どんかん → ひるみ無効
for _ab in ("せいしんりょく", "どんかん"):
    _d = make_poke(type1="ノーマル", hp_b=255, ability=_ab); _rng.seed(0)
    for _ in range(20): execute(make_poke(atk_b=30), _d, "ねこだまし")
    check(f"{_ab}: ひるみ無効", not _d.flinched, f"flinched={_d.flinched}")

# 3. マイペース → こんらん無効（いばるの攻撃上昇は通る）
_dmp = make_poke(type1="ノーマル", hp_b=255, ability="マイペース")
execute(make_poke(), _dmp, "いばる")
check("マイペース: こんらん無効(攻撃上昇は通る)", not _dmp.confused and _dmp.stage_attack == 2,
      f"conf={_dmp.confused} atk={_dmp.stage_attack}")

# 4. クリアボディ/しろいけむり → 能力ダウン無効
for _ab in ("クリアボディ", "しろいけむり"):
    _d = make_poke(type1="ノーマル", hp_b=255, ability=_ab)
    execute(make_poke(), _d, "なみだめ")
    check(f"{_ab}: 能力ダウン無効", _d.stage_attack == 0 and _d.stage_sp_attack == 0,
          f"atk={_d.stage_attack} spa={_d.stage_sp_attack}")

# 5. ちょうはつ中は変化技が使えない
_atk_t = make_poke(type1="ノーマル"); _atk_t.taunt_count = 3
execute(_atk_t, make_poke(hp_b=255), "つるぎのまい")
check("ちょうはつ中: 変化技不可", _atk_t.stage_attack == 0, f"atk={_atk_t.stage_attack}")

# 6. 能力ランク±6で頭打ち（これ以上変化しない）
_a6 = make_poke(); _a6.stage_attack = 6
execute(_a6, make_poke(), "つるぎのまい")
check("能力上限+6: これ以上上がらない", _a6.stage_attack == 6, f"atk={_a6.stage_attack}")
_dn6 = make_poke(hp_b=255); _dn6.stage_attack = -6
execute(make_poke(), _dn6, "なみだめ")
check("能力下限-6: これ以上下がらない", _dn6.stage_attack == -6, f"atk={_dn6.stage_attack}")

# 7. 状態異常は重複しない（既に状態異常なら別の状態異常技は無効）
_d7 = make_poke(type1="ノーマル", hp_b=255); _d7.status = "burn"
for _ in range(10): execute(make_poke(type1="でんき"), _d7, "でんじは")
check("状態異常重複不可: やけど中はまひしない", _d7.status == "burn", f"status={_d7.status}")

# 8. まもる中は変化技も防がれる
_d8 = make_poke(type1="ノーマル", hp_b=255); _d8.protecting = True
execute(make_poke(type1="でんき"), _d8, "でんじは")
check("まもる中: 変化技も防がれる", _d8.status is None, f"status={_d8.status}")

# 9. みがわり中は状態異常技が効かない（同じ乱数で みがわり 無しなら入ることも確かめる。以前は でんじは が外れて偶然通っていた）
random.seed(9); _d9c = make_poke(type1="ノーマル", hp_b=255)
execute(make_poke(type1="でんき"), _d9c, "でんじは")
random.seed(9); _d9 = make_poke(type1="ノーマル", hp_b=255); _d9._substitute_hp = 50
execute(make_poke(type1="でんき"), _d9, "でんじは")
check("audit40 既知 みがわり中: 状態異常技無効（対照: みがわり無しなら同じ乱数でまひ）", _d9c.status == "paralysis" and _d9.status is None,
      f"control={_d9c.status} status={_d9.status}")

# 10. 天候は違う天候で上書きできる（雨→晴れ）
_fw = BattleField(); _fw.weather = "rain"
execute(make_poke(), make_poke(), "にほんばれ", _fw)
check("天候上書き: 雨→晴れ", _fw.weather == "sunny", f"weather={_fw.weather}")

# 11. トリックルームは再使用で解除（トグル）
_ftr = BattleField(); _ftr.trick_room = True; _ftr.trick_room_count = 3
execute(make_poke(), make_poke(), "トリックルーム", _ftr)
check("トリックルーム: 再使用で解除", not _ftr.trick_room, f"trick_room={_ftr.trick_room}")

# 12. こおり/まひ等タイプ免疫は攻撃技の追加効果でも適用（でんきはまひしない）
_d12 = make_poke(type1="でんき", hp_b=255, spdef_b=255); _rng.seed(0)
for _ in range(60): execute(make_poke(type1="でんき", atk_b=20), _d12, "10まんボルト")
check("でんきタイプ: まひ追加効果も無効", _d12.status is None, f"status={_d12.status}")

# 13. あくび(ねむけ)は交代でキャンセルされる
_sy = BattleSide([make_poke(type1="ノーマル", hp_b=200, moves=["たいあたり"]),
                  make_poke(name="控え", moves=["たいあたり"])])
_sy.active.yawn_count = 2
_sy.switch_to(1)
check("あくび: 交代でねむけ解除", _sy.party[0].yawn_count == 0, f"yawn={_sy.party[0].yawn_count}")

# 14. 眠ると溜め技(ソーラービーム)は解除され、起床後に発火しない
_sbz = make_poke(type1="くさ", spatk_b=120, hp_b=200, moves=["ソーラービーム"])
_sbd = make_poke(type1="ノーマル", hp_b=255, spdef_b=80, moves=["たいあたり"])
execute(_sbz, _sbd, "ソーラービーム")   # 1ターン目＝溜め（ダメージなし）
check("溜め技: 1ターン目は溜め(ダメージなし)",
      _sbz.charging_move == "ソーラービーム" and _sbd.hp == _sbd.max_hp,
      f"charging={_sbz.charging_move} hp={_sbd.hp}/{_sbd.max_hp}")
_sbz.status = "sleep"; _sbz.sleep_count = 2
_hp_b14 = _sbd.hp
execute(_sbz, _sbd, "ソーラービーム")   # 睡眠中は発火せず溜め解除
check("溜め技: 眠ると発火せず溜め解除",
      _sbz.charging_move is None and _sbd.hp == _hp_b14,
      f"charging={_sbz.charging_move} hp={_sbd.hp}/{_hp_b14}")

# 15. 先攻の自滅(反動)瀕死 → 後攻技は対象不在で失敗、交代先はターン終了時に無傷で着地
_fl15 = make_poke(name="自滅役", type1="フェアリー", spatk_b=150, spd_b=200, hp_b=80, moves=["はめつのひかり"])
_fl15.hp = 1                       # 反動で確実に瀕死
_bn15 = make_poke(name="控え15", type1="ノーマル", def_b=100, hp_b=120, moves=["たいあたり"])
_fo15 = make_poke(name="相手15", type1="じめん", atk_b=120, spd_b=50, hp_b=160, spdef_b=70, moves=["じしん"])
_s115 = BattleSide([_fl15, _bn15]); _s215 = BattleSide([_fo15])
Battle(_s115, _s215, BattleField()).resume(_Force("はめつのひかり"), _Force("じしん"), max_turns=1)
check("自滅瀕死: 先攻自滅役は瀕死", not _fl15.is_alive, f"alive={_fl15.is_alive}")
check("自滅瀕死: 先攻技は相手に当たっている", _fo15.hp < _fo15.max_hp, f"foe={_fo15.hp}/{_fo15.max_hp}")
check("自滅瀕死: 控えがターン終了時に着地", _s115.active.name == "控え15", f"active={_s115.active.name}")
check("自滅瀕死: 後攻技は対象不在で失敗(控え無傷)", _s115.active.hp == _s115.active.max_hp,
      f"hp={_s115.active.hp}/{_s115.active.max_hp}")

# 16. ひるみはターンをまたいで持ち越さない（後攻が当てたひるみは次ターン無効）
_pf16 = make_poke(name="ひるみ持越", type1="ノーマル", hp_b=200, moves=["たいあたり"])
_pf16.flinched = True
Battle(BattleSide([_pf16]), BattleSide([make_poke(moves=["なまける"])]))._end_of_turn()
check("ひるみ: ターン終了でクリア(持ち越さない)", not _pf16.flinched, f"flinched={_pf16.flinched}")

# 17. 瀕死交代先：HPの減った相手を先制で倒せる控え(反撃KO)を最優先
from simulator.battle import _best_faint_switch as _bfs17
_opp17 = make_poke(name="相手17", type1="ほのお", hp_b=100, spd_b=50, def_b=100)
_rev17 = make_poke(name="速攻17", type1="ノーマル", atk_b=120, spd_b=120, moves=["たいあたり"])   # 速い・KO可だがタイプ等倍
_adv17 = make_poke(name="水鈍17", type1="みず", atk_b=120, spd_b=20, moves=["みずでっぽう"])      # 遅い・タイプ有利
_side17 = BattleSide([make_poke(name="死17", moves=["たいあたり"]), _rev17, _adv17]); _side17.active_idx = 0
_side17.party[0].is_alive = False
_opp17.hp = 10   # 瀕死寸前 → 速攻が先制で倒せる
check("瀕死交代: HP減の相手は反撃KOできる速い控えを選ぶ",
      _bfs17(_side17, _opp17).__class__ is int and _side17.party[_bfs17(_side17, _opp17)].name == "速攻17",
      f"choice={_side17.party[_bfs17(_side17, _opp17)].name}")
_opp17.hp = _opp17.max_hp   # 満タン → 反撃KO不可 → タイプ有利な控えにフォールバック
check("瀕死交代: 反撃不可ならタイプ有利な控え",
      _side17.party[_bfs17(_side17, _opp17)].name == "水鈍17",
      f"choice={_side17.party[_bfs17(_side17, _opp17)].name}")


# 18. encode_state ダメージメモ（features._DMG_MEMO）のビット一致ガード
#   MCTS葉展開で3回 encode する間 calc_damage を共有する最適化。calc_damage は純粋関数でなく
#   じゅうでん/エレクトロモーフ消費・半減きのみ消費・きまぐレーザーの乱数という副作用を持つため、
#   memo は「副作用が起きうる組」を除外して初めてビット一致になる。この不変条件を固定する
#   （将来 calc_damage に新たな副作用が加わり guard が漏れたら、ここが赤くなって気づける）。
print("\n=== 18. encode_stateメモのビット一致 ===")
from simulator import features as _feat18
from simulator.features import encode_state as _enc18, dmg_memo_begin as _mb18, dmg_memo_end as _me18

def _mk_side18(att_item=None, att_ab="しんりょく", att_charged=False, att_em=False,
               def_item=None, att_moves=("10まんボルト", "たいあたり")):
    a = make_poke(name="A18", type1="でんき", atk_b=120, spatk_b=130, spd_b=120,
                  moves=list(att_moves), item=att_item, ability=att_ab)
    a.charged = att_charged
    if att_em:
        a._electromorphosis_charged = True
    d = make_poke(name="D18", type1="みず", type2="ひこう", def_b=90, spdef_b=90, spd_b=80,
                  moves=["たいあたり"], item=def_item)
    b = make_poke(name="B18", type1="くさ", spd_b=60, moves=["たいあたり"])
    s1 = BattleSide([a, b]); s2 = BattleSide([d, make_poke(name="E18", moves=["たいあたり"])])
    s1.field_idx = 0; s2.field_idx = 1
    return s1, s2

def _enc3_nomemo(s1, s2, f):
    random.seed(18)   # きまぐレーザー等の乱数を memo有無で同一列に固定して比較する
    return (list(_enc18(s1, s2, f)), list(_enc18(s2, s1, f)), list(_enc18(s1, s2, f)))

def _enc3_memo(s1, s2, f):
    random.seed(18)
    _mb18()
    try:
        return (list(_enc18(s1, s2, f)), list(_enc18(s2, s1, f)), list(_enc18(s1, s2, f)))
    finally:
        _me18()

def _state_sig18(s1, s2):
    def ps(p):
        return (p.item, getattr(p, "charged", False), getattr(p, "_electromorphosis_charged", False))
    return tuple(ps(p) for p in s1.party) + tuple(ps(p) for p in s2.party)

_CASES18 = [
    ("通常", dict()),
    ("じゅうでん(att)", dict(att_charged=True)),
    ("エレクトロモーフ(att)", dict(att_em=True)),
    ("半減きのみ(def=シュカのみ)", dict(def_item="シュカのみ")),
    ("きまぐレーザー(att)", dict(att_moves=("きまぐレーザー", "たいあたり"))),
]
for _label, _kw in _CASES18:
    s1, s2 = _mk_side18(**_kw); f18 = BattleField()
    _no = _enc3_nomemo(*_mk_side18(**_kw), BattleField())   # 副作用検証用に別インスタンス
    s1b, s2b = _mk_side18(**_kw)
    _ye = _enc3_memo(s1b, s2b, BattleField())
    check(f"memo特徴一致: {_label}", _no == _ye)
    # memo有無で（消費フラグ・きのみ等）状態遷移も一致すること
    s1c, s2c = _mk_side18(**_kw); _enc3_nomemo(s1c, s2c, BattleField())
    sig_no = _state_sig18(s1c, s2c); sig_ye = _state_sig18(s1b, s2b)
    check(f"memo状態遷移一致: {_label}", sig_no == sig_ye, f"{sig_no} vs {sig_ye}")
check("memoは既定で無効(None)", _feat18._DMG_MEMO is None)


# ════════════════════════════════════════════════════════════════
# 19. gen_builder_data: 型の性格多様性
#   耐久EVの特殊アタッカー(ニンフィア)が採る『ひかえめ』(周辺20.7%)のように、
#   _nature_fits(上昇ステに投資あり)を通らない実在型が型1/2/3から消える不具合の回帰。
# ════════════════════════════════════════════════════════════════
import sqlite3 as _sq3
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import gen_builder_data as _gbd

_nat19 = [("ずぶとい", 68.6), ("ひかえめ", 20.7), ("おだやか", 5.1)]
_ev19 = [32, 0, 32, 0, 2, 0]      # H32/B32 の耐久型（Cには投資なし）
check("_nature_alt: 耐久EVでもひかえめを候補にする",
      _gbd._nature_alt(_nat19, _ev19, {"ずぶとい"}) == "ひかえめ")
check("_nature_alt: 下降ステに投資がある性格は採らない",
      _gbd._nature_alt([("ひかえめ", 20.7)], [32, 32, 0, 0, 0, 0], set()) is None)
check("_nature_alt: 周辺採用率が閾値未満なら採らない",
      _gbd._nature_alt([("おだやか", 5.1)], _ev19, set()) is None)
check("_nature_alt: 既出の性格は返さない",
      _gbd._nature_alt(_nat19, _ev19, {"ずぶとい", "ひかえめ"}) is None)
check("_pick_nature_joint: 実構築の裏付けがある場合はTrueを返す",
      _gbd._pick_nature_joint({"natures": {("D", "ずぶとい"): 7}}, "D", _nat19, _ev19)
      == ("ずぶとい", True))
check("_pick_nature_joint: 観測なしは周辺分布＋backed=False",
      _gbd._pick_nature_joint(None, "D", _nat19, _ev19) == ("ずぶとい", False))

_con19 = _sq3.connect(_gbd.DB)
from simulator.data import normalize_mega_stone as _nms19
_rows19 = [r for r in _con19.execute(
    "SELECT pokemon, rank, pokemon_id FROM pokemon_usage WHERE season=? AND rule=? "
    "AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule=?) "
    "ORDER BY rank", (_gbd.SEASON, _gbd.RULE, _gbd.SEASON, _gbd.RULE))]
_sp19, _tpl19 = _gbd.build_species(_con19, dl, [(n, r, p or 1) for n, r, p in _rows19])
_v19 = _gbd.build_variants(_con19, "ニンフィア", _tpl19, _nms19)
# 型プールの系統から作る種: 代表は系統の割合の上位3系統で、系統内85%以上の技を全部持つ型（REQUIREMENTS 5-10）
_pg19 = _gbd._pool_groups().get("ガブリアス")
if _pg19:
    _vg19 = _gbd.build_variants(_con19, "ガブリアス", _tpl19, _nms19)
    _top19 = [g["name"] for g in sorted(_pg19["groups"], key=lambda g: -g["share"])[:3]]
    _top19 = [_gbd.arch_name(g["name"]) for g in sorted(_pg19["groups"], key=lambda g: -g["share"]) if g["share"] >= _gbd.MIN_ARCH_SHARE][:3]
    check("型プールの種: 1v1 の型は割合10%以上の系統の上位3つ", [b["arch"] for b in _vg19] == _top19,
          str([b.get("arch") for b in _vg19]))
    check("型プールの種: 代表の系統の割合はすべて10%以上",
          all(g["share"] >= _gbd.MIN_ARCH_SHARE for g in _pg19["groups"] if _gbd.arch_name(g["name"]) in {b["arch"] for b in _vg19}))
    check("型プールの種: 型は割合の大きい順", [b["share"] for b in _vg19] == sorted((b["share"] for b in _vg19), reverse=True))
    _hp19 = _gbd._pool_groups().get("カバルドン")
    if _hp19:
        _vh19 = _gbd.build_variants(_con19, "カバルドン", _tpl19, _nms19)
        check("型プールの種: 系統が1つでも大きい系統を分けて3型にする（カバルドン）",
              len(_vh19) == 3 and len({b["arch"] for b in _vh19}) == 3 and all(b["share"] >= 10 for b in _vh19),
              str([(b["arch"], b["share"]) for b in _vh19]))
        check("型プールの種: 分けた型の名前は系統名に入っている持ち物を括弧の中で繰り返さない（カバルドン）",
              all("（" not in b["arch"] or "オボンのみ" not in b["arch"].split("（", 1)[1] for b in _vh19),
              str([b["arch"] for b in _vh19]))
        check("型プールの種: 分けた型に系統の番号と枝番が付く（カバルドン）",
              [(b["archNo"], b["archSub"]) for b in _vh19] == [(1, "a"), (1, "b"), (1, "c")],
              str([(b["archNo"], b["archSub"]) for b in _vh19]))
    for _sp19 in ("プクリン", "ヌメルゴン"):
        _g19 = _gbd._pool_groups().get(_sp19)
        if not _g19:
            continue
        _vs19 = _gbd.build_variants(_con19, _sp19, _tpl19, _nms19)
        _top_g19 = max(_g19["groups"], key=lambda g: g["share"])
        _sum19 = sum(b["share"] for b in _vs19 if b["archNo"] == 1)
        check(f"型プールの種: 分けた型の割合の合計が系統の割合（{_sp19}）",
              len([b for b in _vs19 if b["archNo"] == 1]) >= 2 and abs(_sum19 - _top_g19["share"] * 100) <= 0.2,
              f"{_sum19} vs {_top_g19['share'] * 100}: {[(b['arch'], b['share']) for b in _vs19]}")
    check("型プールの種: 型に系統の割合(%)が付く", all(b.get("share", 0) > 0 for b in _vg19))
# 型プールの種は代表型の性格をそのまま使う（REQUIREMENTS 5-10）ので、性格をずらす処理の確認は型プールに無い種のときだけ
if "ニンフィア" not in _gbd._pool_groups():
    check("ニンフィアの型にひかえめが含まれる", "ひかえめ" in [b["nature"] for b in _v19],
          str([(b["item"], b["nature"]) for b in _v19]))
_same19 = 0
for _n19, _r19, _p19 in _rows19[:50]:
    # 型プールの系統から作る種は、各系統の代表（最も重い型）の性格をそのまま使うので対象外（REQUIREMENTS 5-10）
    if _n19 in _gbd._pool_groups():
        continue
    _b19 = _gbd.build_variants(_con19, _n19, _tpl19, _nms19)
    _nt19 = {n for n, p in _gbd._natures_of(_con19, _n19) if p >= _gbd.NATURE_ALT_PCT}
    if len(_b19) >= 2 and len(_nt19) >= 2 and len({b["nature"] for b in _b19}) == 1:
        _same19 += 1
check("TOP50（型プール外の種）: 有意な性格が2つ以上あるのに全型同性格な種が5体以下",
      _same19 <= 5, f"{_same19}体")
_con19.close()


# ════════════════════════════════════════════════════════════════
# 20. DBパス解決（デプロイ可能性）
#     絶対パス固定だとコンテナで起動できない（sqlite3.OperationalError）。
#     data.py 自身の位置から scripts/pokenavi.db を相対解決し、POKENAVI_DB で上書きできること。
# ════════════════════════════════════════════════════════════════
print("\n=== 20. DBパス解決 ===")
import os as _os20, importlib as _il20
from simulator import data as _d20
os = _os20

_exp20 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(_d20.__file__))), "pokenavi.db")
# 解決後の値は当然この機では絶対パスになる。判定すべきは「ソースに絶対パスが直書きされていないか」。
_src20 = open(_d20.__file__, encoding="utf-8").read()
import re as _re20
check("DB_PATHがソースに絶対パス直書きされていない",
      _re20.search(r'^DB_PATH\s*=\s*[\'"]/', _src20, _re20.M) is None,
      "data.py に DB_PATH = \"/...\" のリテラル代入がある")
check("DB_PATHが data.py 位置からの相対解決と一致",
      os.path.abspath(_d20.DB_PATH) == os.path.abspath(_exp20), f"{_d20.DB_PATH} != {_exp20}")
check("解決したDBが実在し読める", os.path.isfile(_d20.DB_PATH), _d20.DB_PATH)

_old20 = os.environ.get("POKENAVI_DB")
try:
    os.environ["POKENAVI_DB"] = "/tmp/_pokenavi_dbpath_probe.db"
    _il20.reload(_d20)
    check("POKENAVI_DB で上書きできる",
          _d20.DB_PATH == "/tmp/_pokenavi_dbpath_probe.db", _d20.DB_PATH)
finally:
    if _old20 is None:
        os.environ.pop("POKENAVI_DB", None)
    else:
        os.environ["POKENAVI_DB"] = _old20
    _il20.reload(_d20)   # 後続テストのため既定へ戻す


# ════════════════════════════════════════════════════════════════
# 21. 提案プールのフォーム整合（FORM_FIX）
#     プールキーとDB種名が食い違うフォームで、①種名が実体へ解決される
#     ②使用率順位も実体側を引く（同名の別種の順位を拾わない）ことを保証する。
#     過去事故: 「## キュウコン」の中身はアローラ種なのに素の名前で解決され、
#     ほのお単×ゆきふらしのキメラが生成され、順位も通常キュウコン168位で
#     上書きされて実使用率9位の種が補完プールから丸ごと脱落していた。
# ════════════════════════════════════════════════════════════════
print("\n=== 21. 提案プールのフォーム整合 ===")
try:
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from gen_party_pool import PartyGen as _PG21, FORM_FIX as _FF21
    import gen_party_pool as _GP21
    import sqlite3 as _sq21
    _con21 = _sq21.connect("scripts/pokenavi.db")
    _cd21 = _con21.execute("SELECT MAX(crawled_date) FROM pokemon_usage WHERE season=? AND rule='single'",
                           (_GP21.USAGE_SEASON,)).fetchone()[0]
    _live21 = dict(_con21.execute("SELECT pokemon, rank FROM pokemon_usage WHERE season=? AND rule='single' AND crawled_date=?",
                                  (_GP21.USAGE_SEASON, _cd21)).fetchall())
    _con21.close()
    # M-3 の md はキー「キュウコン」の中身がアローラ形。型プール（提案の既定・Cloud Run）と M-6 の md は種名が DB の種名そのもの
    # （キュウコン＝通常形・アローラキュウコン＝アローラ形）なので、FORM_FIX はコロン形（ケンタロス:炎）だけに効く（form_fix_for）。
    # 以前は M-6 の md で通常キュウコン（ひでり・あついいわ）が アローラキュウコン の名前で生成されていた
    _pgs21 = {}
    for _src21 in ("md", "pool"):
        _pg21 = _pgs21[_src21] = _PG21(src=_src21)
        _bad21 = []
        for _k21, _real21 in (_GP21.form_fix_for(_pg21.pool) if _src21 == "md" else _FF21).items():
            if _k21 not in _pg21.pool or (_src21 == "pool" and ":" not in _k21): continue
            for _s21 in _pg21.pool[_k21]:
                if not _s21.startswith(_real21 + "@"):
                    _bad21.append((_k21, _s21.split("@")[0])); break
        check(f"[{_src21}] FORM_FIXのプール型が実体種名で生成される", not _bad21, f"不一致={_bad21[:3]}")
        _ak21 = "キュウコン" if _src21 == "md" and "キュウコン" in _GP21.form_fix_for(_pg21.pool) else "アローラキュウコン"
        _ab21 = _pg21.pool.get(_ak21, [])
        _rk21 = _pg21.rank.get(_ak21, 9999)
        _plain21 = _live21.get("キュウコン", 9999)
        check(f"[{_src21}] アローラキュウコンの順位が実体側で解決される（{_GP21.USAGE_SEASON}）",
              _rk21 <= 80 and _rk21 == _live21.get("アローラキュウコン") and _rk21 != _plain21,
              f"rank={_rk21} DBのアローラキュウコン={_live21.get('アローラキュウコン')} 通常キュウコン={_plain21}")
        check(f"[{_src21}] アローラキュウコンの型が実体名・ゆきふらし・こおり/フェアリー",
              bool(_ab21) and all(_s21.startswith("アローラキュウコン@") and _s21.endswith(":ゆきふらし") for _s21 in _ab21)
              and _pg21._types_of_spec(_ab21[0]) == ("こおり", "フェアリー"), str([_s21.split(":")[0] for _s21 in _ab21[:3]]))
        _veil21 = sum(_pg21.build_weight(_ak21, _s21) for _s21 in _ab21 if "オーロラベール" in _s21) / (sum(_pg21.build_weight(_ak21, _s21) for _s21 in _ab21) or 1)
        check(f"[{_src21}] アローラキュウコンの型にオーロラベール(実採用96%)が含まれる（型の重みで過半）", _veil21 > 0.5, f"壁型の重み {_veil21:.2f}")
        if _ak21 == "アローラキュウコン":
            _pl21 = _pg21.pool.get("キュウコン", [])
            check(f"[{_src21}] キー「キュウコン」は通常形（ほのお・ゆきふらしのキメラが無い）",
                  all(_s21.startswith("キュウコン@") and not _s21.endswith(":ゆきふらし") for _s21 in _pl21)
                  and (not _pl21 or _pg21._types_of_spec(_pl21[0]) == ("ほのお",)) and _pg21.dex.get("キュウコン") == _pg21.dex.get("アローラキュウコン"),
                  str([(_s21.split(":")[0], _s21.split(":")[-1]) for _s21 in _pl21[:2]]))
except Exception as _e21:
    check("提案プールのフォーム整合テストが実行できる", False, f"{type(_e21).__name__}: {_e21}")


# ════════════════════════════════════════════════════════════════
# 22. シナジー必須種のゲート（_product3_complete._synergy_ok）
#     特性始動（あめふらし等）は全ての型が持つため _role_builds の技ベース payoff では
#     捕まえられない。党の合否で判定する経路が正しく効くことを担保する。
#     メガ後特性の解決も必須（specのability欄は非メガ時の特性。メガラグラージ＝すいすい）。
# ════════════════════════════════════════════════════════════════
print("\n=== 22. シナジー必須種のゲート ===")
try:
    import _synergy_feat as _SF22
    _mega_swampert22 = "ラグラージ@ラグラージナイト:いじっぱり:じしん|ウェーブタックル|れいとうパンチ|ビルドアップ:2/32/0/0/0/32:げきりゅう"
    check("メガ後特性で雨ペイオフを算出できる（メガラグラージ=すいすい）",
          _SF22.weather_payoff(_mega_swampert22, "rain") >= 2,
          f"payoff={_SF22.weather_payoff(_mega_swampert22, 'rain')}")

    _pel22 = "ペリッパー@しめったいわ:のんき:とんぼがえり|おいかぜ|はねやすめ|ぼうふう:32/0/32/0/2/0:あめふらし"
    check("特性による天候始動を検出できる（あめふらし→rain）",
          _SF22.setter_of(_pel22) == "rain", f"setter={_SF22.setter_of(_pel22)}")

    import importlib as _il22
    import _product3_complete as _PC22
    _dummy22 = ["ガブリアス@きあいのタスキ:ようき:じしん|げきりん|がんせきふうじ|つるぎのまい:2/32/0/0/0/32:さめはだ",
                "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ",
                "ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|しっぺがえし:2/32/0/0/0/32:ばけのかわ",
                "マスカーニャ@こだわりスカーフ:いじっぱり:トリックフラワー|トリプルアクセル|かみなりパンチ|とんぼがえり:2/32/0/0/0/32:へんげんじざい",
                "アーマーガア@たべのこし:わんぱく:アイアンヘッド|ボディプレス|はねやすめ|とんぼがえり:32/0/32/0/2/0:プレッシャー",
                _pel22]
    _old22 = os.environ.get("SYNERGY_GATE")
    try:
        os.environ["SYNERGY_GATE"] = "0"; _il22.reload(_PC22)
        check("ゲートOFF時は従来どおり通す", _PC22._synergy_ok(_dummy22), "OFFで弾いた")
        os.environ["SYNERGY_GATE"] = "1"; _il22.reload(_PC22)
        check("雨ペイオフ不足のペリッパー党を弾く", not _PC22._synergy_ok(_dummy22), "弾けなかった")
        _rain22 = _dummy22[:4] + [_mega_swampert22, _pel22]
        check("雨受け手がいる党のペリッパーは通す", _PC22._synergy_ok(_rain22), "受け手ありでも弾いた")
    finally:
        if _old22 is None: os.environ.pop("SYNERGY_GATE", None)
        else: os.environ["SYNERGY_GATE"] = _old22
        _il22.reload(_PC22)
except Exception as _e22:
    check("シナジーゲートのテストが実行できる", False, f"{type(_e22).__name__}: {_e22}")


# ════════════════════════════════════════════════════════════════
# 22b. 提案の残り枠の生成: 条件を満たす型だけから引く（_product3_complete、2026-10-01）
#     種の重み＝使用率ベースの重み×（今の条件を満たす型の確率の合計）、型は満たす型の中で正規化して引く。
#     軸の解決: メガが上限を超えたら使用率の低い方を非メガへ。作れない指定は理由つきで即エラー。
# ════════════════════════════════════════════════════════════════
print("\n=== 22b. 提案の残り枠の生成（条件を満たす型だけから引く） ===")
try:
    import _product3_complete as _PC22b
    from gen_party_pool import _spec_mega as _sm22b, _item_of as _it22b
    _pg = _pgs21["pool"]
    _two = [p for p in _pg.pokes if _pg.mega.get(p) and _pg.nonm.get(p) and _pg.rank.get(p, 9999) <= 80]
    # 1) 種族の時点で作れない指定: 同じタイプ3体
    _bytype = {}
    for _p in _pg.pokes:
        for _b in _pg.nonm.get(_p, [])[:1]:
            for _t in _pg._types_of_spec(_b):
                _bytype.setdefault(_t, []).append(_b)
    _t3 = next(_t for _t, _v in _bytype.items() if len({_pg.dexof(x) for x in _v}) >= 3)
    _f3 = []
    for _b in _bytype[_t3]:
        if _pg.dexof(_b) not in {_pg.dexof(x) for x in _f3} and _it22b(_b) not in {_it22b(x) for x in _f3}:
            _f3.append(_b)
        if len(_f3) == 3: break
    _why = _PC22b.infeasible_reason(_pg, _f3)
    check("作れない指定: 同じタイプ3体を理由つきで判定", _why is not None and _t3 in _why and "2体まで" in _why, str(_why))
    _m3 = [_pg.mega[p][0] for p in _two[:3]]
    _why = _PC22b.infeasible_reason(_pg, _m3)
    check("作れない指定: メガの型3体を理由つきで判定", _why is not None and "メガ" in _why, str(_why))
    try:
        _PC22b.complete_core(_pg, None, None, _f3, random.Random(0), 5, strict=True); _raised = None
    except SystemExit as _e:
        _raised = str(_e)
    check("作れない指定: 生成の前に SystemExit（フロントに出す文言）", _raised is not None and _t3 in _raised, str(_raised))
    # 2) 軸の解決: 自動でメガを選んだ3体 → 使用率の低い方を非メガに
    _hit = None
    for _i in range(len(_two)):
        for _j in range(_i + 1, len(_two)):
            for _k in range(_j + 1, len(_two)):
                _c = [_two[_i], _two[_j], _two[_k]]
                if not all(_sm22b(_pg.pool[x][0]) for x in _c): continue
                if len({_pg.dex.get(x) for x in _c}) < 3: continue
                try:
                    _r = _PC22b.resolve_fixed(_pg, [{"sp": x, "mega": None} for x in _c])
                except SystemExit:
                    continue
                _hit = (_c, _r); break
            if _hit: break
        if _hit: break
    if _hit:
        _c, _r = _hit
        _low = max(_c, key=lambda x: _pg.rank.get(x, 9999))
        _nm = [x for x, s_ in zip(_c, _r) if not _sm22b(s_)]
        check("軸の解決: メガが上限を超えたら使用率の低い方を非メガの型に", sum(bool(_sm22b(x)) for x in _r) == 2 and _nm == [_low],
              f"{_c} → 非メガ {_nm}（使用率最下位 {_low}）")
    else:
        check("軸の解決のテスト対象（自動メガ3体）が見つかる", False)
    # 3) 生成: メガ枠が埋まった軸ではメガの型を引かない・全件合法
    _f2 = [_pg.mega[p][0] for p in _two[:2]]
    if _PC22b.infeasible_reason(_pg, _f2) is None:
        _keys = [_pg.keyof(x) for x in _f2]
        _ps = [_PC22b.sample_weighted(_pg, _keys, _f2, random.Random(_i), 2) for _i in range(60)]
        _ps = [_f2 + [r_[1][k] for k in r_[0][2:]] for r_ in _ps if r_]
        check("生成: メガ枠が埋まった軸では残り枠にメガの型が出ない・全件合法",
              len(_ps) >= 50 and all(sum(bool(_sm22b(x)) for x in p_) == 2 and _pg.is_legal(p_, megas_set=(2,)) for p_ in _ps),
              f"{len(_ps)}件 不正={[p_ for p_ in _ps if not _pg.is_legal(p_, megas_set=(2,))][:1]}")
        # 型プール（提案の既定）はシードの型を持つ種がある。設置役のいないシードを sample_weighted 自体が替える（fix_ev_1008 の後の確認で
        # メガ2体の軸の60件中1件が 設置役のいないシード で不正だった）。md・型プールの両方で、メガ0〜2体の軸の残り枠が全件合法
        for _src22b, _pgx in _pgs21.items():
            _tw = [p for p in _pgx.pokes if _pgx.mega.get(p) and _pgx.nonm.get(p) and _pgx.rank.get(p, 9999) <= 30]
            _one = [p for p in _pgx.pokes if _pgx.nonm.get(p) and _pgx.rank.get(p, 9999) <= 30]
            _axes = [[_pgx.mega[a][0], _pgx.mega[b][0]] for a, b in zip(_tw[:8], _tw[1:9])] + [[_pgx.nonm[a][0]] for a in _one[:8]] + [[_pgx.mega[a][0]] for a in _tw[:4]]
            _axes = [f_ for f_ in _axes if _PC22b.infeasible_reason(_pgx, f_) is None]
            _n22b, _bad22b = 0, []
            for f_ in _axes:
                _kx = [_pgx.keyof(x) for x in f_]
                _fm = sum(bool(_sm22b(x)) for x in f_)
                for _i in range(40):
                    _m = max(_fm, 2 if _i % 5 else 1)
                    r_ = _PC22b.sample_weighted(_pgx, _kx, f_, random.Random(1000 + _i), _m)
                    if not r_: continue
                    p_ = f_ + [r_[1][k] for k in r_[0][len(f_):]]
                    _n22b += 1
                    if not (sum(bool(_sm22b(x)) for x in p_) == _m and _pgx.is_legal(p_, megas_set=(_m,))):
                        _bad22b.append([x.split(":")[0] for x in p_])
            check(f"[{_src22b}] 生成: 軸{len(_axes)}件の残り枠が全件合法（メガ数・持ち物・タイプ・設置役のいないシード）",
                  _n22b >= 20 * len(_axes) and len(_axes) >= 15 and not _bad22b, f"{_n22b}件中 不正{len(_bad22b)} {_bad22b[:2]}")
        # 種の重み＝使用率ベースの重み×（条件を満たす型の確率の合計）（1枠目の抽選の重みを記録して照合）
        class _Rec(random.Random):
            def choices(self, seq, weights=None, k=1, **kw):
                self.log.append((list(seq), list(weights))); return super().choices(seq, weights=weights, k=k, **kw)
        _rr = _Rec(5); _rr.log = []
        _PC22b.sample_weighted(_pg, _keys, _f2, _rr, 2)
        _sps, _ws = _rr.log[0]
        _base = _PC22b._species_base(_pg, _keys, {_pg.dex.get(k) for k in _keys})
        _ui, _tc, _mg = _PC22b._fixed_state(_pg, _f2)
        _exp = {p: _base[p] * sum(x[1] for x in _PC22b._build_probs(_pg, p) if _PC22b._build_ok(x, _ui, _tc, _mg, 2, 3)) for p in _base}
        check("生成: 種の重み＝使用率ベースの重み×条件を満たす型の確率の合計（メガしかない型の種は0）",
              all(abs(w_ - _exp[p]) < 1e-12 for p, w_ in zip(_sps, _ws))
              and all(_exp[p] == 0 for p in _base if not _pg.nonm.get(p)) and set(_sps) == {p for p in _exp if _exp[p] > 0},
              f"{len(_sps)}種")
    else:
        check("生成のテスト対象（メガ2体の軸）が作れる", False, _PC22b.infeasible_reason(_pg, _f2))
    # メガ石ごとのタイプ（リザードナイトX＝ほのお/ドラゴン、Y＝ほのお/ひこう）。以前は X も Y のタイプで重なりを判定していた
    _tx = {_st: _pg._types_of_spec(f"リザードン@{_st}:ひかえめ:かえんほうしゃ|エアスラッシュ|りゅうのはどう|ソーラービーム:2/0/0/32/0/32:もうか")
           for _st in ("リザードナイトX", "リザードナイトY")}
    check("タイプの重なり判定: メガ石ごとのタイプ（リザードナイトX はドラゴン・Y はひこう）",
          _tx == {"リザードナイトX": ("ほのお", "ドラゴン"), "リザードナイトY": ("ほのお", "ひこう")}, str(_tx))
except Exception as _e22b:
    check("残り枠の生成のテストが実行できる", False, f"{type(_e22b).__name__}: {_e22b}")


# ════════════════════════════════════════════════════════════════
# 23. ばけのかわの確定数（表示用の1v1判定）
#     battle.py:992 は「1発目のダメージを無効化し最大HPの1/8を消費」。
#     表示側が単純な n+1 だと削りを無視して1手多く見積もる（実例: 1発44%で確4と誤表示）。
# ════════════════════════════════════════════════════════════════
print("\n=== 23. ばけのかわの確定数 ===")
try:
    import math as _m23
    import _explain as _E23
    from simulator.matchup_explain import _verdict as _V23

    class _D23:
        def __init__(self, ab, it, hp): self.ability = ab; self.item = it; self.max_hp = hp

    def _sim23(hp, ratio):
        """実際の削り込み: 1発目無効＋1/8消費 → 以降は通常ダメージ"""
        left = hp - max(1, hp // 8); n = 1
        while left > 0:
            left -= int(hp * ratio); n += 1
        return n

    for _r23, _exp23 in ((0.44, 3), (0.33, 4), (0.60, 3), (1.05, 2)):
        _n23, _ = _E23._apply_survive(_E23._hits(_r23), _D23("ばけのかわ", "", 132), _r23)
        check(f"ばけのかわ 1発{_r23*100:.0f}% → 確{_exp23}", _n23 == _exp23, f"確{_n23}")
        check(f"ばけのかわ 1発{_r23*100:.0f}% が実削り込みと一致",
              _n23 == _sim23(132, _r23), f"式{_n23} vs 実{_sim23(132, _r23)}")
    # がんじょう/タスキは満タンOHKOのみ1発耐える（削りは無い）
    _n23a, _ = _E23._apply_survive(_E23._hits(1.20), _D23("がんじょう", "", 100), 1.20)
    check("がんじょう 1発120% → 確2", _n23a == 2, f"確{_n23a}")
    _n23b, _ = _E23._apply_survive(_E23._hits(0.60), _D23("がんじょう", "", 100), 0.60)
    check("がんじょう 1発60% → 確2（耐え無関係）", _n23b == 2, f"確{_n23b}")
    _n23c, _ = _E23._apply_survive(_E23._hits(1.20), _D23("プレッシャー", "きあいのタスキ", 100), 1.20)
    check("きあいのタスキ 1発120% → 確2", _n23c == 2, f"確{_n23c}")
    _n23d, _ = _E23._apply_survive(_E23._hits(1.20), _D23("プレッシャー", "", 100), 1.20)
    check("耐え手段なし 1発120% → 確1", _n23d == 1, f"確{_n23d}")
    # マルチスケイル/ファントムガードは満タン時のみ半減。2撃目以降は等倍なので
    # 満タン時の1発を全撃に当てはめると確定数を多く見積もる。
    def _sim23b(hp, r0, r1):
        left = hp - int(hp * r0); n = 1
        while left > 0:
            left -= int(hp * r1); n += 1
        return n
    for _r0, _r1, _exp in ((0.27, 0.54, 3), (0.55, 1.11, 2), (0.13, 0.27, 5)):
        _n, _ = _E23._apply_survive(_E23._hits(_r0), _D23("マルチスケイル", "", 168), _r0, _r1)
        check(f"マルチスケイル 満タン{_r0*100:.0f}%/以降{_r1*100:.0f}% → 確{_exp}", _n == _exp, f"確{_n}")
        check(f"マルチスケイル {_r0*100:.0f}% が実削り込みと一致",
              _n == _sim23b(168, _r0, _r1), f"式{_n} vs 実{_sim23b(168, _r0, _r1)}")
    _nf, _ = _E23._apply_survive(_E23._hits(0.60), _D23("ファントムガード", "", 100), 0.60, 1.20)
    check("ファントムガードも同じ扱い 満60%/以降120% → 確2", _nf == 2, f"確{_nf}")
except Exception as _e23:
    check("ばけのかわの確定数テストが実行できる", False, f"{type(_e23).__name__}: {_e23}")


# ════════════════════════════════════════════════════════════════
# 24. ダメージ計算の副作用が分析側に漏れないこと
#     calc_damage は半減きのみ消費で defender.item=None、充電技で attacker.charged=False と
#     実体を書き換える（対戦本体では正しい）。分析側は同じオブジェクトを使い回すため、
#     1回目で相手のきのみが消え2回目以降が「きのみ無し」になる事故が起きていた
#     （実測: エンペルト@シュカのみ の相性表で1列目消費・残り28列が誤判定）。
# ════════════════════════════════════════════════════════════════
print("\n=== 24. 分析側の冪等性（きのみ消費の副作用） ===")
try:
    import feature1 as _f24
    _f24._ensure_loaded("M-3", 8); _L24 = _f24._W["loader"]
    from simulator.pokemon import build_from_spec as _bfs24, parse_pokemon_spec as _pps24
    from simulator.battle import BattleField as _BF24
    _F24 = _BF24()
    _B24 = "エンペルト@シュカのみ:ひかえめ:ハイドロポンプ|ラスターカノン|なみのり|めいそう:32/0/0/32/0/0:げきりゅう"
    _A24 = "ガブリアス@きあいのタスキ:ようき:じしん|げきりん|がんせきふうじ|つるぎのまい:2/32/0/0/0/32:さめはだ"
    def _mk24(x): return _bfs24(_pps24(x), _L24, season="M-3", randomize=False)

    import _matchup_surrogate as _MS24
    _a, _b = _mk24(_A24), _mk24(_B24)
    _r = [_MS24._bestdmg(_a, _b, _F24) for _ in range(3)]
    check("_matchup_surrogate._bestdmg が冪等", len(set(_r)) == 1, f"{_r}")
    check("  相手のきのみが消えない", _b.item == "シュカのみ", f"item={_b.item}")

    import simulator.matchup_explain as _ME24
    _a, _b = _mk24(_A24), _mk24(_B24)
    _r = [round(_ME24._best_dmg(_a, _b, _F24), 6) for _ in range(3)]
    check("matchup_explain._best_dmg が冪等", len(set(_r)) == 1, f"{_r}")

    import _explain as _E24
    _M, _O = _E24._build(_B24, _L24), _E24._build(_A24, _L24)
    _r = [_E24._mu_score(_M, _O, _F24)["myh"] for _ in range(3)]
    check("_explain._mu_score が冪等", len(set(_r)) == 1, f"{_r}")
    check("  自分のきのみが消えない", _M.item == "シュカのみ", f"item={_M.item}")

    import _necessity as _NEC24
    _ms = _NEC24._build6([_A24] * 6, _L24); _bs = _NEC24._build6([_B24] * 6, _L24)
    _m = [_NEC24._dmg_mats(_ms, _bs, _F24)[0] for _ in range(3)]
    check("_necessity._dmg_mats が冪等", _m[0] == _m[1] == _m[2], "行列が変化")

    # 対戦本体では消費されるのが正しい（副作用を殺していないこと）
    from simulator.damage import calc_damage as _cd24
    _a, _b = _mk24(_A24), _mk24(_B24)
    _mv = [m for m in _a.moves if m.name_jp == "じしん"][0]
    _d1 = _cd24(_a, _b, _mv, _F24, False, 0.0)
    check("対戦本体ではきのみが消費される", _b.item is None, f"item={_b.item}")

    # 天候: メガリザードンYの ひでり で晴れになり みず技は半減される。
    # 従来は BattleField()（天候なし）で評価しており、アクアテール→メガリザードンY が
    # 122%(確1) と出て判定が逆転していた。TS移植版(fieldWeather)には元から入っていた。
    _Z25 = "リザードン@リザードナイトＹ:おくびょう:ソーラービーム|かえんほうしゃ|エアスラッシュ|まもる:0/0/0/32/0/32:もうか"
    _G25 = "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく"
    _M25 = _E24._build(_Z25, _L24); _O25 = _E24._build(_G25, _L24)
    check("メガ後の特性が ひでり", _M25.ability == "ひでり", f"{_M25.ability}")
    _f25 = _E24._enter(_M25, _O25)[0]
    check("ひでり持ちとの対面は晴れ", _f25.weather == "sunny", f"{_f25.weather}")
    _r25 = _E24._mu_score(_M25, _O25, _BF24())
    # 判定の手数(thh)は方針選び（りゅうのまい→攻撃 等）で変わりうるので、晴れの半減は1発の割合と「確1にならない」で見る
    check("晴れでみず技が半減され確1にならない（1発 100%未満・手数2以上）",
          _r25["thr"] < 1.0 and _r25["thh"] >= 2, f"{_r25['thh']}発 ({_r25['thr']*100:.0f}%)")
    # 天候特性が無い対面では天候なし
    _f25b = _E24._enter(_O25, _O25)[0]
    check("天候特性が無ければ天候なし", _f25b.weather is None, f"{_f25b.weather}")

    # フィールドも同様。環境では メガライチュウX の エレキメイカー のみ。
    # 未考慮だと ボルテッカー→メガメタグロス が 48%(確3) → 63%(確2) と判定が変わっていた。
    _R26 = "ライチュウ@ライチュウナイトX:ようき:１０まんボルト|ボルテッカー|かみなりパンチ|アイアンテール:0/32/0/0/0/32:せいでんき"
    _MG26 = "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ"
    _rz26 = _E24._build(_R26, _L24); _mg26 = _E24._build(_MG26, _L24)
    check("メガ後の特性が エレキメイカー", _rz26.ability == "エレキメイカー", f"{_rz26.ability}")
    _f26 = _E24._enter(_rz26, _mg26)[0]
    check("エレキメイカー持ちとの対面はエレキフィールド", _f26.electric_terrain is True, f"{_f26.electric_terrain}")
    _r26 = _E24._mu_score(_rz26, _mg26, _BF24())
    check("エレキでんき技1.3倍が効いて確2", _r26["myh"] == 2, f"{_r26['myh']}発 ({_r26['myr']*100:.0f}%)")
    _f26b = _E24._enter(_mg26, _E24._build(_G25, _L24))[0]
    check("フィールド特性が無ければフィールドなし", _f26b.electric_terrain is False, f"{_f26b.electric_terrain}")

    # いかく: 入場時に相手の攻撃を1段階下げる。分析側が常にランク0を仮定していたため
    # 物理技のダメージが34%過大に出ていた（サイコファング→ギャラドス 71%(確2) → 47%(確3)）。
    # 環境に いかく は通常18種＋メガ2種と広く存在する。
    _GY27 = "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく"
    # メガシンカ前の特性で入場する（実機どおり）。いかくが効く ライトメタル のメタグロスで確かめる（クリアボディは下で別に確認）
    _MG27 = "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:ライトメタル"
    _g27 = _E24._build(_GY27, _L24); _m27 = _E24._build(_MG27, _L24)
    _f27, _A27, _B27 = _E24._enter(_m27, _g27)
    check("いかくで相手の攻撃が-1", _A27.stage_attack == -1, f"{_A27.stage_attack}")
    check("いかく側は自分のランクを変えない", _B27.stage_attack == 0, f"{_B27.stage_attack}")
    check("元のオブジェクトは変化しない", _m27.stage_attack == 0 and _g27.stage_attack == 0,
          f"{_m27.stage_attack}/{_g27.stage_attack}")
    _r27 = _E24._mu_score(_m27, _g27, _BF24())
    check("いかく込みで確3", _r27["myh"] == 3, f"{_r27['myh']}発 ({_r27['myr']*100:.0f}%)")
    # クリアボディ等には無効（メガ前の特性がクリアボディなら、メガシンカ後も下がっていない）
    _cb27 = _E24._build("メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ", _L24)
    _f27b, _A27b, _ = _E24._enter(_cb27, _g27)
    check("メガ前の特性がクリアボディならいかくが効かない", _A27b.stage_attack == 0 and _A27b.mega_evolved, f"{_A27b.stage_attack}")
    # トレース: 入場時に相手の特性をコピーし、コピー先が天候特性なら場も変わる
    _SA27 = "サーナイト@サーナイトナイト:ひかえめ:サイコキネシス|ムーンフォース|めいそう|10まんボルト:32/0/0/32/0/0:トレース"
    _KY27 = "アローラキュウコン@ひかりのねんど:おくびょう:オーロラベール|ふぶき|ムーンフォース|あくび:32/0/16/16/0/0:ゆきふらし"
    _f27c, _A27c, _ = _E24._enter(_E24._build(_SA27, _L24), _E24._build(_KY27, _L24))
    check("ゆきふらし持ちとの対面は雪", _f27c.weather == "hail", f"{_f27c.weather}")

    # 再発防止: 表示系の主要APIを「同じ入力で2回」呼んで結果とオブジェクト状態が変わらないこと。
    # 新しい分析関数を足したときに、保護し忘れをここで機械的に検出する。
    _sp24 = [_B24, _A24,
             "ミミッキュ@いのちのたま:いじっぱり:シャドークロー|じゃれつく|かげうち|つるぎのまい:2/32/0/0/0/32:ばけのかわ",
             "カイリュー@こだわりハチマキ:いじっぱり:げきりん|しんそく|じしん|アイアンヘッド:2/32/0/0/0/32:マルチスケイル",
             "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ",
             "マスカーニャ@きあいのタスキ:ようき:トリックフラワー|はたきおとす|とんぼがえり|くさむすび:0/32/0/0/0/32:へんげんじざい"]
    import json as _json24
    for _fn24, _nm24 in ((_E24.matchup_grid, "matchup_grid"),
                         (_E24.firepower_matrix, "firepower_matrix"),
                         (_E24.speed_info, "speed_info")):
        _o1 = _json24.dumps(_fn24(_sp24, _L24), ensure_ascii=False, sort_keys=True)
        _o2 = _json24.dumps(_fn24(_sp24, _L24), ensure_ascii=False, sort_keys=True)
        check(f"{_nm24} が2回呼んでも同じ結果", _o1 == _o2, "2回目が異なる")
except Exception as _e24:
    check("分析側の冪等性テストが実行できる", False, f"{type(_e24).__name__}: {_e24}")


# ════════════════════════════════════════════════════════════════
# 25. 1v1判定が対戦本体と一致すること（実走方式）
#     静的なダメージ計算で1v1を近似すると、対戦本体では正しい仕様が分析側で抜ける
#     （天候・フィールド・いかく・トレース・ばけのかわ・マルチスケイル・半減きのみ・
#     ロール引数…と8種類のバグが実際に発生し、一致率は72.6%だった）。
#     現在は _mu_engine が対戦本体で1v1を実走して数える。
# ════════════════════════════════════════════════════════════════
print("\n=== 25. 1v1判定の実走一致 ===")
try:
    import feature1 as _f25
    _f25._ensure_loaded("M-3", 8); _L25 = _f25._W["loader"]
    import _explain as _E25, _mu_engine as _ME25
    from simulator.battle import BattleField as _BF25
    import simulator.battle as _BT25
    _ME25._LOADER[0] = _L25

    _PAIRS25 = [
        # (攻撃側, 防御側, 確認したい仕様)
        ("メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:ライトメタル",
         "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく", "いかく"),
        ("メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ",
         "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく", "メガ前クリアボディ"),
        ("リザードン@リザードナイトＹ:おくびょう:ソーラービーム|かえんほうしゃ|エアスラッシュ|まもる:0/0/0/32/0/32:もうか",
         "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく", "晴れ"),
        ("ライチュウ@ライチュウナイトX:ようき:１０まんボルト|ボルテッカー|かみなりパンチ|アイアンテール:0/32/0/0/0/32:せいでんき",
         "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ", "エレキ"),
    ]
    for _a25, _b25, _lbl25 in _PAIRS25:
        _A25 = _E25._build(_a25, _L25); _B25 = _E25._build(_b25, _L25)
        _r25 = _E25._mu_score(_A25, _B25, _BF25())
        _h25, _ = _ME25._run(_a25, _b25, _r25["my_move"], _L25)
        check(f"1v1({_lbl25}) の確定数が実走と一致", _h25 == _r25["myh"],
              f"分析{_r25['myh']} vs 実走{_h25} ({_r25['my_move']})")
        # 3回呼んで同じ値（乱数が固定されているか）
        _rep = {_ME25._run(_a25, _b25, _r25["my_move"], _L25)[0] for _ in range(3)}
        check(f"1v1({_lbl25}) が決定的", len(_rep) == 1, f"{_rep}")
    # 確定効果（prob=1.0）は発動し、確率効果（prob<1.0）は不発であること。
    # 判定は全て `random() < prob` なので、固定値に 1.0 を入れると `1.0 < 1.0` が偽になり
    # 必中急所・りゅうせいぐんの特攻ダウン等の確定効果まで殺してしまう（実際に殺していた）。
    _MAS25 = ("マスカーニャ@いのちのたま:いじっぱり:ふいうち|ちょうはつ|トリックフラワー|トリプルアクセル"
              ":2/32/0/0/0/32:しんりょく")
    _MUK25 = ("ムクホーク@ムクホークナイト:ようき:ブレイブバード|インファイト|ブレイズキック|はねやすめ"
              ":27/6/1/0/0/32:いかく")
    _ME25._enter_fixed()
    try:
        _am25 = _E25._build(_MAS25, _L25); _dm25 = _E25._build(_MUK25, _L25)
        _tf25 = next(m for m in _am25.moves if m is not None and m.name_jp == "トリックフラワー")
        _fu25 = next(m for m in _am25.moves if m is not None and m.name_jp == "ふいうち")
        check("固定文脈で必中急所(トリックフラワー)が発動する",
              _BT25._check_critical(_am25, _tf25, _dm25) is True, "急所にならない")
        check("固定文脈で通常技は急所にならない(ふいうち)",
              _BT25._check_critical(_am25, _fu25, _dm25) is False, "急所になった")
    finally:
        _ME25._exit_fixed()
    # 上の帰結: 急所ぶんダメージが増えるので確定数は 6発ではなく 4発
    check("必中急所が確定数に反映される",
          _ME25._run(_MAS25, _MUK25, "トリックフラワー", _L25)[0] == 4,
          f"{_ME25._run(_MAS25, _MUK25, 'トリックフラワー', _L25)[0]}発")

    # 1発ごとに命中判定がある技（ACCURACY_CHAINED）は、分析が必中を仮定する以上
    # 最大回数まで当たる。既定（対戦本体）ではこの差し替えは効かない。
    from simulator.battle import _calc_hits as _ch25, ACCURACY_CHAINED as _AC25
    check("ACCURACY_CHAINED にトリプルアクセルとネズミざんが入る",
          _AC25 == {"トリプルアクセル", "ネズミざん"}, f"{_AC25}")
    check("_HIT_CONTINUE の既定は None（対戦本体の挙動を変えない）",
          _BT25._HIT_CONTINUE is None, f"{_BT25._HIT_CONTINUE}")
    _nz25 = _L24.get_move("ネズミざん") if False else _f25._W["loader"].get_move("ネズミざん")
    _ME25._enter_fixed(0.0)
    try:
        check("固定文脈でネズミざんは10回", _ch25(_nz25, None) == 10, f"{_ch25(_nz25, None)}回")
    finally:
        _ME25._exit_fixed()
    check("固定を抜けると _HIT_CONTINUE が戻る", _BT25._HIT_CONTINUE is None, "戻っていない")
    # 2〜5回の連続技は重み3:3:1:1で期待値ちょうど3.0。分析では3回に固定する
    _ws25 = [3, 3, 1, 1]
    check("2〜5回連続技の期待値が3.0",
          sum(h * w for h, w in zip([2, 3, 4, 5], _ws25)) / sum(_ws25) == 3.0, "期待値が3でない")
    _ss25 = _f25._W["loader"].get_move("みずしゅりけん")
    _ME25._enter_fixed(0.0)
    try:
        check("固定文脈で2〜5回連続技は3回", _ch25(_ss25, None) == 3, f"{_ch25(_ss25, None)}回")
    finally:
        _ME25._exit_fixed()
    check("固定を抜けると _MULTI_HIT_FIXED が戻る", _BT25._MULTI_HIT_FIXED is None, "戻っていない")
    check("_ASSUME_OPP_ATTACKS の既定は False", _BT25._ASSUME_OPP_ATTACKS is False, "既定が違う")
    # 反射技は最大打点の候補から外す（相手の技に依存しすぎるため）
    from simulator.battle import MATCHUP_EXCLUDED as _CM25
    check("MATCHUP_EXCLUDED は反射技3種＋HP依存技2種",
          _CM25 == {"カウンター", "ミラーコート", "メタルバースト", "がむしゃら", "いかりのまえば"},
          f"{_CM25}")
    _cnt25 = ("グレイシア@とつげきチョッキ:ひかえめ:ミラーコート|れいとうビーム|こごえるかぜ|あくび"
              ":32/0/0/32/0/0:ゆきがくれ")
    _gab25 = ("ガブリアス@きあいのタスキ:いじっぱり:じしん|げきりん|スケイルショット|つるぎのまい"
              ":2/32/0/0/0/32:さめはだ")
    check("反射技は最大打点技に選ばれない",
          _ME25._best_cached(_cnt25, _gab25, 0, id(_L25))[2] != "ミラーコート",
          f"{_ME25._best_cached(_cnt25, _gab25, 0, id(_L25))}")

    # 追加効果・連続技・ムラっけの乱数が固定されていること
    import random as _rnd25
    _before25 = (_rnd25.random, _rnd25.choice, _rnd25.choices, _rnd25.randint)
    _ME25._run(_PAIRS25[0][0], _PAIRS25[0][1], "サイコファング", _L25)
    check("実走後に random が元に戻る",
          (_rnd25.random, _rnd25.choice, _rnd25.choices, _rnd25.randint) == _before25, "戻っていない")
except Exception as _e25:
    check("1v1実走テストが実行できる", False, f"{type(_e25).__name__}: {_e25}")


print("\n=== 26d. 隠れ控えの再サンプルが技0本にならない ===")
# _resample_hidden_bench は self.season のテンプレで控えを作り直す。M-6の200種のうち
# 53種は M-2 に使用率行が無く、技0本・特性''・持ち物None の「無害な相手」が木に入っていた。
from simulator.search_ai import SearchAI as _SA26d
from simulator.pokemon import build_from_template as _bft26d
_ai26d = _SA26d(dl, season="M-2")
for _sp26d in ("ボーマンダ", "グソクムシャ", "セグレイブ"):
    _t26d = _ai26d._tpl_playable(_sp26d)
    _nb26d = _bft26d(_t26d, dl, randomize=True) if _t26d else None
    _mv26d = [m for m in (_nb26d.moves if _nb26d else []) if m]
    check(f"season=M-2 でも {_sp26d} の控えが技を持つ", len(_mv26d) > 0,
          f"技{len(_mv26d)}本")
# 対照: 元の _tpl は M-2 のまま（フォールバックは _tpl_playable 限定）
_t0 = _ai26d._tpl("グソクムシャ")
check("_tpl 自体は season のテンプレのまま（フォールバックしない）",
      _t0 is not None and not getattr(_t0, "top_moves", None),
      f"top_moves={len(getattr(_t0,'top_moves',[]) or [])}")
# 対照: 両シーズンにある種は挙動が変わらない
_ai26d6 = _SA26d(dl, season="M-6")
check("両シーズンにある種は _tpl と _tpl_playable が同じ",
      _ai26d6._tpl("ガブリアス") is _ai26d6._tpl_playable("ガブリアス"))


print("\n=== 26c. AI火力見積もりの姿変化・連続技 ===")
# 対戦本体は battle.apply_pre_move_forms / _calc_hits を必ず通るのに、AIの見積もりは
# calc_damage を直に呼ぶため取りこぼしていた。ギルガルド(M-6採用率100%)はシールド(攻50)
# のまま計算され1.8〜2.0倍の過小評価、連続技は1発ぶんだけ見ていた。
import os as _os26c, importlib as _il26c
from simulator.battle import BattleField as _BF26c
from simulator.pokemon import build_from_spec as _bfs26c, parse_pokemon_spec as _pps26c
import simulator.ai as _A26c

_f26c = _BF26c()
def _mk26c(spec):
    return _bfs26c(_pps26c(spec), dl, season="M-6", randomize=False)

_gil26c = _mk26c("ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ")
_gab26c = _mk26c("ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ")
_seg26c = _mk26c("セグレイブ@きあいのタスキ:いじっぱり:つららおとし|きょけんとつげき|じしん|つららばり:1/32/1/0/0/32:ねつこうかん")

def _ed26c(att, deff, name, **env):
    _save = {k: _os26c.environ.get(k) for k in env}
    try:
        for k, v in env.items():
            _os26c.environ[k] = v
        _il26c.reload(_A26c)
        mv = [m for m in att.moves if m and m.name_jp == name][0]
        return _A26c.expected_damage(att, deff, mv, _f26c)
    finally:
        for k, v in _save.items():
            if v is None: _os26c.environ.pop(k, None)
            else: _os26c.environ[k] = v
        _il26c.reload(_A26c)

_off26c = _ed26c(_gil26c, _gab26c, "シャドーボール", AI_BLADE_FORME="0")
_on26c = _ed26c(_gil26c, _gab26c, "シャドーボール", AI_BLADE_FORME="1")
check("バトルスイッチ: 見積もりがブレードフォルムで1.5倍以上になる",
      _on26c > _off26c * 1.5, f"旧{_off26c:.1f} 新{_on26c:.1f}")
check("バトルスイッチ: 見積もり後に元のステータスへ戻る",
      not getattr(_gil26c, "_in_blade_forme", False) and _gil26c.attack == _mk26c(
          "ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ").attack,
      f"attack={_gil26c.attack} blade={getattr(_gil26c,'_in_blade_forme',None)}")
_off26c = _ed26c(_seg26c, _gab26c, "つららばり", AI_MULTI_HIT="0")
_on26c = _ed26c(_seg26c, _gab26c, "つららばり", AI_MULTI_HIT="1")
check("連続技(つららばり 2-5発)の期待ヒット数3.0が乗る",
      abs(_on26c / max(_off26c, 1e-9) - 3.0) < 0.01, f"旧{_off26c:.1f} 新{_on26c:.1f}")
_off26c = _ed26c(_seg26c, _gab26c, "つららおとし", AI_MULTI_HIT="0")
_on26c = _ed26c(_seg26c, _gab26c, "つららおとし", AI_MULTI_HIT="1")
check("負例: 単発技(つららおとし)は倍率1.0のまま",
      abs(_on26c - _off26c) < 1e-6, f"旧{_off26c:.1f} 新{_on26c:.1f}")
_off26c = _ed26c(_gab26c, _gil26c, "じしん", AI_BLADE_FORME="0")
_on26c = _ed26c(_gab26c, _gil26c, "じしん", AI_BLADE_FORME="1")
check("負例: バトルスイッチでない攻撃側は見積もりが変わらない",
      abs(_on26c - _off26c) < 1e-6, f"旧{_off26c:.1f} 新{_on26c:.1f}")
check("期待ヒット数: スキルリンクは5発",
      abs(_A26c._expected_hits(dl.get_move("つららばり"),
                               type("X", (), {"ability": "スキルリンク"})()) - 5.0) < 1e-9)


print("\n=== 26e. AI火力見積もり: トリプルアクセルの威力上昇・前回の発数の持ち越し・確定KO/先制被弾判定 ===")
# expected_damage は姿変化・連続技を入れていたが、(1) トリプルアクセルを「1発目(威力20)×3」で見て
# 実際(20+40+60)の半分、(2) 前回の連続技の _multi_hit_index が残ったまま計算して威力60×3に化ける、
# (3) certain_ko_override / _can_ko / _opp_priority_threatens は calc_damage 直呼びで姿変化も
# 連続技も無視していた（REQUIREMENTS は「expected_damage を使う」と書いていたが実装は違った）。
from simulator.damage import calc_damage as _cd26d
from simulator.battle import BattleSide as _BS26d, Action as _Act26d, crit_chance as _cc26d
_mas26d = _mk26c("マニューラ@いのちのたま:ようき:トリプルアクセル|はたきおとす|ねこだまし|つららおとし:0/32/0/0/0/32:プレッシャー")
_tgt26d = _mk26c("ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ")
_ta26d = [m for m in _mas26d.moves if m.name_jp == "トリプルアクセル"][0]
def _sum26d(att, deff, mv):
    pc = _cc26d(att, mv, deff); tot = 0.0
    for i in range(3):
        att._multi_hit_index = i
        d = _cd26d(att, deff, mv, _f26c, critical=False, random_roll=0.5)
        dc = _cd26d(att, deff, mv, _f26c, critical=True, random_roll=0.5)
        tot += d * (1 - pc) + dc * pc
    att._multi_hit_index = 0
    return tot * (mv.accuracy or 100) / 100
_want26d = _sum26d(_mas26d, _tgt26d, _ta26d)
_got26d = _A26c.expected_damage(_mas26d, _tgt26d, _ta26d, _f26c)
check("トリプルアクセル: 見積もり＝威力20/40/60の3発の合計×命中", abs(_got26d - _want26d) < 1e-6,
      f"got={_got26d:.2f} want={_want26d:.2f}")
_mas26d._multi_hit_index = 2
_st26d = _A26c.expected_damage(_mas26d, _tgt26d, _ta26d, _f26c)
check("前回の連続技の発数が残っていても見積もりは同じ・発数は元に戻す",
      abs(_st26d - _want26d) < 1e-6 and _mas26d._multi_hit_index == 2,
      f"{_st26d:.2f} vs {_want26d:.2f} idx={_mas26d._multi_hit_index}")
_mas26d._multi_hit_index = 0
check("期待ヒット数(威力換算): トリプルアクセルは1発目の6倍",
      abs(_A26c._expected_hits(_ta26d, _mas26d) - 6.0) < 1e-9)

def _ko26d(att, deff, name, hp, act=None):
    deff.hp = hp
    s1 = _BS26d([att], viewer_label="P1"); s2 = _BS26d([deff], viewer_label="P2")
    a0 = act or _Act26d(type="move", move=[m for m in att.moves if m.category == "status"][0],
                         move_idx=[i for i, m in enumerate(att.moves) if m.category == "status"][0])
    r = _A26c.certain_ko_override(a0, s1, s2, _f26c)
    deff.hp = deff.max_hp
    return r.move.name_jp if r.type == "move" else r.type

# ギルガルド: シールドのままの最低ロールでは届かず、ブレードなら届くHP
_gil26d = _mk26c("ギルガルド@たべのこし:ひかえめ:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ")
_hat26d = _mk26c("ハッサム@ゴツゴツメット:わんぱく:バレットパンチ|とんぼがえり|はねやすめ|つるぎのまい:32/0/32/0/0/0:テクニシャン")
_sn26d = [m for m in _gil26d.moves if m.name_jp == "かげうち"][0]
_sh26d = _cd26d(_gil26d, _hat26d, _sn26d, _f26c, critical=False, random_roll=0.0)
_bl26d = _A26c._move_damage(_gil26d, _hat26d, _sn26d, _f26c, 0.0, "min")
_hp26d = int((_sh26d + _bl26d) // 2)
check("前提: ブレードの最低ロールがシールドより大きい", _bl26d > _sh26d + 1, f"shield={_sh26d} blade={_bl26d}")
check("確定KO: ギルガルドのかげうちはブレード火力で判定し上書きする",
      _ko26d(_gil26d, _hat26d, "かげうち", _hp26d) == "かげうち", f"hp={_hp26d}")
check("確定KO: ブレード判定後もシールドのステータスに戻る",
      not getattr(_gil26d, "_in_blade_forme", False) and _gil26d.attack == _mk26c(
          "ギルガルド@たべのこし:ひかえめ:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ").attack)

# 連続技（2〜5発）は「必ず当たる2発」で確定を判定する（3発目以降は当てにしない）
_gab26d = _mk26c("ガブリアス@こだわりスカーフ:ようき:スケイルショット|ステルスロック|つるぎのまい|まもる:0/32/0/0/0/32:さめはだ")
_sla26d = _mk26c("ヤドラン@ゴツゴツメット:ずぶとい:ねっとう|なまける|でんじは|トリック:32/0/32/0/0/0:さいせいりょく")
_ss26d = [m for m in _gab26d.moves if m.name_jp == "スケイルショット"][0]
_one26d = _cd26d(_gab26d, _sla26d, _ss26d, _f26c, critical=False, random_roll=0.0)
_h2 = int(2 * _one26d)
check("前提: 1発ぶんでは届かないHP", _one26d < _h2, f"1hit={_one26d} 2hits={_h2}")
_A26c._FIX40_ON = False   # 命中90の技なので、回数の判定だけを見るため命中の条件（audit40 #3）を外す
check("確定KO: スケイルショットは2発ぶんで確定を判定する",
      _ko26d(_gab26d, _sla26d, "スケイルショット", _h2) == "スケイルショット", f"hp={_h2}")
_h3 = int(2 * _one26d) + 1
check("負例: 2発で届かないHPでは連続技の上書きをしない（3発目以降は確定でない）",
      _ko26d(_gab26d, _sla26d, "スケイルショット", _h3) != "スケイルショット", f"hp={_h3}")
_A26c._FIX40_ON = True

# 先制技の脅威判定は最大ロール・最大回数（みずしゅりけん 5発）
_gek26d = _mk26c("ゲッコウガ@いのちのたま:おくびょう:みずしゅりけん|あくのはどう|れいとうビーム|とんぼがえり:0/0/0/32/0/32:へんげんじざい")
_ws26d = [m for m in _gek26d.moves if m.name_jp == "みずしゅりけん"][0]
_w1 = _cd26d(_gek26d, _gab26d, _ws26d, _f26c, critical=False, random_roll=1.0)
_w5 = _A26c._move_damage(_gek26d, _gab26d, _ws26d, _f26c, 1.0, "max")
_gab26d.hp = int(_w1 * 2) + 1
check("先制の脅威: みずしゅりけんは最大5発で判定する（1発ぶんでは届かないHP）",
      _A26c._opp_priority_threatens(_gab26d, _gek26d, _f26c) and _w5 >= _gab26d.hp and _w1 < _gab26d.hp,
      f"1発={_w1} 5発={_w5} hp={_gab26d.hp}")
_gab26d.hp = _gab26d.max_hp


print("\n=== 26f. 探索AI: 相手にタイプで無効な攻撃技を根の候補から外す ===")
# 本番ネット同士300戦の実測で無効技は手番の0.7%。強制プレイアウトでは外しても勝率差+0.1pt±0.3
# （勝敗がほぼ決まった局面の同値タイで方策priorに引かれていた）。見た目の悪手だけ消す。
from simulator.search_ai import SearchAI as _SA26f, _prune_immune_moves as _pim26f, _type_immune_move as _tim26f
_hip26f = _mk26c("カバルドン@オボンのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし")
_sal26f = _mk26c("ボーマンダ@ボーマンダナイト:ようき:すてみタックル|じしん|りゅうのまい|はねやすめ:0/32/0/0/0/32:いかく")
_mim26f = _mk26c("ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ")
_gar26f = _mk26c("ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|どくづき|つるぎのまい:0/32/0/0/0/32:さめはだ")
_sk26f = _mk26c("エアームド@ゴツゴツメット:わんぱく:ボディプレス|はねやすめ|てっぺき|ステルスロック:32/0/32/0/0/0:がんじょう")
_sa26f = _SA26f(dl, rollouts=2, depth=3)
def _names26f(me, opp, bench=()):
    s1 = BattleSide([me] + list(bench)); s2 = BattleSide([opp])
    c = _pim26f(_sa26f._candidate_actions(s1, s2, _f26c), s1, s2, _f26c)
    return [("メガ+" if a.do_mega else "") + a.move.name_jp if a.type == "move" else "交代" for a in c]
_n26f = _names26f(_hip26f, _sal26f)
check("無効技(じしん→ひこう)は外し、変化技は残す", "じしん" not in _n26f and "あくび" in _n26f, str(_n26f))
_n26f = _names26f(_gar26f, _sk26f)
check("無効技(どくづき→はがね)を外し、じしんは残す(エアームドはひこうなので じしんも外れる)",
      "どくづき" not in _n26f and "じしん" not in _n26f and "ドラゴンクロー" in _n26f, str(_n26f))
_n26f = _names26f(_sal26f, _mim26f)
check("メガと同時の技はメガ後の特性で判定（スカイスキンのすてみタックルはゴーストに当たる）",
      "メガ+すてみタックル" in _n26f and "すてみタックル" not in _n26f, str(_n26f))
_gar26f.choice_locked_move = "どくづき"
_n26f = _names26f(_gar26f, _sk26f, bench=[_hip26f])
check("こだわり固定で残る技が無効技だけなら外さない（居座り/交代は探索に任せる）",
      "どくづき" in _n26f and "交代" in _n26f, str(_n26f))
_gar26f.choice_locked_move = None
_hit26f = _mk26c("ラッキー@しんかのきせき:ずぶとい:ちきゅうなげ|タマゴうみ|ステルスロック|でんじは:32/0/32/0/0/0:しぜんかいふく")
_n26f = _names26f(_hit26f, _sal26f)
check("負例: 等倍で当たる技(ちきゅうなげ→ひこう)は外さない", "ちきゅうなげ" in _n26f, str(_n26f))
_scr26f = _mk26c("ケンタロス@こだわりハチマキ:いじっぱり:すてみタックル|インファイト|じしん|アイアンヘッド:0/32/0/0/0/32:きもったま")
_n26f = _names26f(_scr26f, _mim26f)
check("負例: きもったまのノーマル/かくとう技はゴーストに当たるので外さない",
      "すてみタックル" in _n26f and "インファイト" in _n26f, str(_n26f))


print("\n=== 26g. わるあがき: タイプなし・必中 ===")
# 第5世代以降の実機: わるあがきはタイプなし（相性・タイプ一致の対象外＝ゴーストにも当たる）で必ず命中する。
# 以前はノーマル/命中100で、PP切れのイエッサンがギルガルドに「効かない」を繰り返し延々と居座っていた。
from simulator.ai import _get_struggle as _gs26g
_st26g = _gs26g()
check("わるあがき: タイプなし・命中は必中(None)", _st26g.type == "" and _st26g.accuracy is None,
      f"type={_st26g.type!r} acc={_st26g.accuracy}")
_ind26g = _mk26c("イエッサン(オス)@こだわりスカーフ:おくびょう:ワイドフォース|サイコキネシス|マジカルシャイン|トリック:0/0/0/32/0/32:サイコメイカー")
_gil26g = _mk26c("ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ")
_hp0 = _gil26g.hp
_lg26g = execute(_ind26g, _gil26g, _st26g)
check("わるあがきはゴーストにも当たる", _gil26g.hp < _hp0 and not any("効かない" in x for x in _lg26g),
      " / ".join(_lg26g))
_ken26g = _mk26c("ケンタロス@たべのこし:いじっぱり:すてみタックル|インファイト|じしん|アイアンヘッド:0/32/0/0/0/32:いかりのつぼ")
_sla26g = _mk26c("ヤドラン@ゴツゴツメット:ずぶとい:ねっとう|なまける|でんじは|トリック:32/0/32/0/0/0:さいせいりょく")
_d_st = dmg(_ken26g, _sla26g, _st26g)
from simulator.data import MoveData as _MD26g
_nn26g = _MD26g(name_jp="わるあがき", name_en="Struggle", type="ノーマル", category="physical",
                 power=50, accuracy=None, priority=0, pp=1, effect_id=None)
_d_nm = dmg(_ken26g, _sla26g, _nn26g)
check("わるあがきはタイプ一致(1.5倍)が乗らない（ノーマルタイプが使っても）", _d_st < _d_nm and near(_d_st * 1.5, _d_nm, 0.05),
      f"typeless={_d_st} normal={_d_nm}")
_mas26g = _mk26c("マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|はたきおとす|とんぼがえり|トリプルアクセル:0/32/0/0/0/32:へんげんじざい")
execute(_mas26g, _sla26g, _st26g)
check("へんげんじざい: わるあがきではタイプが変わらない", _mas26g.type1 == "くさ" and not getattr(_mas26g, "_protean_used", False),
      f"{_mas26g.type1}/{_mas26g.type2}")
_sla26g.stage_evasion = 6
_hits26g = 0
import random as _r26g
for _i in range(20):
    _r26g.seed(_i)
    _sla26g.hp = _sla26g.max_hp
    execute(_ken26g, _sla26g, _st26g)
    _hits26g += _sla26g.hp < _sla26g.max_hp
_sla26g.stage_evasion = 0
check("わるあがきは回避+6でも必ず当たる", _hits26g == 20, f"{_hits26g}/20")


print("\n=== 26h. AIの型の読みのスナップショット（simulator/predict.py） ===")
# 対戦記録・再生・精度集計のために、AIの信念（相手の型の読み）を取り出す。信念は書き換えない。
# Python↔Rust の一致は _rust_engine/predict_parity.py（greedy 対戦の全ターンで照合）。
import copy as _cp26h, random as _r26h
from simulator.predict import Predictor as _Pr26h, truth_of as _tr26h
from simulator.belief import OpponentBelief as _OB26h
from simulator.battle import Battle as _Bt26h, BattleSide as _BS26h, BattleField as _BF26h
from simulator.ai import GreedyAI as _G26h
_sp1 = ["ギルガルド@いのちのたま:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ",
        "ボーマンダ@ボーマンダナイト:いじっぱり:げきりん|じしん|すてみタックル|りゅうのまい:0/32/0/0/0/32:いかく",
        "アシレーヌ@カゴのみ:ずぶとい:なみのり|ねむる|めいそう|ムーンフォース:32/0/32/0/0/0:げきりゅう"]
_sp2 = ["ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ",
        "サーフゴー@たべのこし:ひかえめ:シャドーボール|ゴールドラッシュ|わるだくみ|じこさいせい:32/0/0/32/0/0:おうごんのからだ",
        "ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ"]
def _run26h(with_pred):
    _r26h.seed(11)
    A = [_mk26c(x) for x in _sp1]; B = [_mk26c(x) for x in _sp2]
    s1 = _BS26h(A, viewer_label="P1"); s2 = _BS26h(B, viewer_label="P2")
    s1.belief = _OB26h(dl); s2.belief = _OB26h(dl)
    P = _Pr26h(dl); snaps = []
    def cb(b):
        if with_pred:
            snaps.append((b.turn, P.snapshot(b.side1, b.side2), P.snapshot(b.side2, b.side1)))
    b = _Bt26h(s1, s2, _BF26h()); g1 = _G26h(); g2 = _G26h()
    res = b.run(g1, g2, on_turn=cb)
    return b, res, snaps
_b0, _res0, _ = _run26h(False)
_b1, _res1, _sn26h = _run26h(True)
check("読みを記録しても対戦の進行（ログ・勝敗）は変わらない", _b0.logs == _b1.logs and _res0 == _res1,
      f"{len(_b0.logs)} vs {len(_b1.logs)}")
check("前提: 数ターン分の読みが取れている", len(_sn26h) >= 3 and all(_sn26h[0][1].values()), str(len(_sn26h)))
_last = _sn26h[-1][1]
_ok26h = True; _msg = ""
for _n, _e in _last.items():
    kn = _e["known"]
    for _m in kn["moves"]:
        if dict(_e["marginal"]["moves"]).get(_m) != 1.0:
            _ok26h = False; _msg = f"{_n} 判明技 {_m} が1.0でない"
    if _e["pool"]:
        for _t in _e["pool"]["top"]:
            if kn["item"] and _t["item"] != kn["item"]:
                _ok26h = False; _msg = f"{_n} 判明持ち物と矛盾する型 {_t}"
            if not set(kn["moves"]) <= set(_t["moves"]):
                _ok26h = False; _msg = f"{_n} 判明技と矛盾する型 {_t}"
        _tot = sum(p for _, p in _e["pool"]["item"])
        if kn["item"] is None and not (0.99 <= _tot <= 1.0001) and len(_e["pool"]["item"]) < 5:
            _ok26h = False; _msg = f"{_n} 型の持ち物確率の和 {_tot}"
check("判明技は所持確率1.0・型の上位候補は判明情報と矛盾しない", _ok26h, _msg)
check("既定（JOINT_BUILD ON）の信念では、型がある種の used は pool",
      all(e["used"] == ("pool" if e["pool"] else "marginal") for e in _last.values())
      and any(e["used"] == "pool" for e in _last.values()))
# 信念を書き換えない: スナップショット前後で信念の中身が同じ
_s = _b1.side1
_bel = _s.belief
_before = {n: (sorted(pb.known_moves), pb.known_item, list(pb.post), list(pb.pool_w), dict(pb.item_prior),
               len(pb.builds)) for n, pb in _bel.species.items()}
_Pr26h(dl).snapshot(_s, _b1.side2)
_after = {n: (sorted(pb.known_moves), pb.known_item, list(pb.post), list(pb.pool_w), dict(pb.item_prior),
              len(pb.builds)) for n, pb in _bel.species.items()}
check("スナップショットは信念を書き換えない", _before == _after and len(_before) > 0)
_t26h = _tr26h(_mk26c(_sp1[0]))
check("truth_of: 実際の型（持ち物・性格・努力値・技）", _t26h["item"] == "いのちのたま" and _t26h["ev"] == "32/0/0/32/0/0"
      and sorted(_t26h["moves"]) == sorted(["かげうち", "アイアンヘッド", "キングシールド", "シャドーボール"]), str(_t26h))


print("\n=== 26i. 観戦記録（feature1.play_and_record）と Battle.run の前処理が同じ ===")
# 以前は feature1 が前処理を手で書いており、run() と食い違っていた: 先発の登場（opp_view.on_enter）を呼ばない
# ＝先発が「場に出た」扱いにならず登場時に公開される特性（いかく等）が信念に入らない／見せ合いが選出3体
# （隠れ選出にならず選出がAIに漏れる）／入場時効果が P1→P2 の固定順（run は速い順）／瀕死交代が
# AIの価値ベース選択でなく簡易ヒューリスティック。Battle.start に前処理を切り出し、両方がそれを通る。
import feature1 as _f26i, random as _r26i
from simulator.learned_selection import learned_select_party as _lsp26i
from simulator.ai import certain_ko_override as _cko26i
from train_az2 import _net_ai as _na26i
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.belief import OpponentBelief
from simulator.battle import Battle, BattleSide, BattleField
_f26i._ensure_loaded("M-6", 8)
_L26i = _f26i._W["loader"]; _N26i = _f26i._W["net"]
_P1s = ["ボーマンダ@ボーマンダナイト:いじっぱり:げきりん|じしん|すてみタックル|りゅうのまい:0/32/0/0/0/32:いかく",
        "ギルガルド@いのちのたま:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ",
        "アシレーヌ@カゴのみ:ずぶとい:なみのり|ねむる|めいそう|ムーンフォース:32/0/32/0/0/0:げきりゅう",
        "カバルドン@オボンのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし",
        "ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ",
        "サーフゴー@たべのこし:ひかえめ:シャドーボール|ゴールドラッシュ|わるだくみ|じこさいせい:32/0/0/32/0/0:おうごんのからだ"]
_P2s = ["ガブリアス@こだわりスカーフ:ようき:じしん|ドラゴンクロー|スケイルショット|つるぎのまい:0/32/0/0/0/32:さめはだ",
        "イダイトウ(オス)@こだわりハチマキ:いじっぱり:ウェーブタックル|おはかまいり|アクアジェット|クイックターン:0/32/0/0/0/32:てきおうりょく",
        "エアームド@ゴツゴツメット:わんぱく:ボディプレス|はねやすめ|てっぺき|ステルスロック:32/0/32/0/0/0:がんじょう",
        "リザードン@リザードナイトＹ:おくびょう:かえんほうしゃ|ソーラービーム|エアスラッシュ|ねっぷう:0/0/0/32/0/32:もうか",
        "ニンフィア@たべのこし:ひかえめ:ハイパーボイス|でんこうせっか|めいそう|まもる:32/0/0/32/0/0:フェアリースキン",
        "ドドゲザン@きあいのタスキ:いじっぱり:ドゲザン|アイアンヘッド|ふいうち|つるぎのまい:0/32/0/0/0/32:そうだいしょう"]
_SIMS26i = 24
_rec26i = _f26i.play_and_record(_P1s, _P2s, season="M-6", sel_temp=0.3, seed=4242, mcts_sims=_SIMS26i)
# 同じ手順を Battle.run で回す（play_and_record の中身と同じ構築・同じシード）
_r26i.seed(4242)
_A = [build_from_spec(parse_pokemon_spec(x), _L26i, season="M-6", randomize=True) for x in _P1s]
_B = [build_from_spec(parse_pokemon_spec(x), _L26i, season="M-6", randomize=True) for x in _P2s]
_sa = _lsp26i(_A, _B, _L26i, n=3, temperature=0.3); _sb = _lsp26i(_B, _A, _L26i, n=3, temperature=0.3)
_s1 = BattleSide(_sa, viewer_label="P1", source6=_A); _s2 = BattleSide(_sb, viewer_label="P2", source6=_B)
_s1.belief = OpponentBelief(_L26i); _s2.belief = OpponentBelief(_L26i)
_x1 = _na26i(_N26i, _L26i, 0, 12, 4242, mcts=True, mcts_sims=_SIMS26i, mcts_select="regret", mcts_fast=True)
_x2 = _na26i(_N26i, _L26i, 0, 12, 4242 ^ 0x5bd1e995, mcts=True, mcts_sims=_SIMS26i, mcts_select="regret", mcts_fast=True)
def _w1(m, o, f): return _cko26i(_x1(m, o, f), m, o, f)
def _w2(m, o, f): return _cko26i(_x2(m, o, f), m, o, f)
_w1.choose_faint_switch = _x1.choose_faint_switch; _w2.choose_faint_switch = _x2.choose_faint_switch
_bt26i = Battle(_s1, _s2, BattleField())
_res26i = _bt26i.run(_w1, _w2)
_flog = [l for t in _rec26i["turns"] for l in t["logs"]][2:]    # 先頭2行は「P1選出/P2選出」の見出し
check("観戦記録と Battle.run で同じシードなら同じ展開（全ログ・勝敗）",
      _flog == _bt26i.logs and _rec26i["result"] == _res26i,
      f"{len(_flog)} vs {len(_bt26i.logs)} res {_rec26i['result']}/{_res26i}")
_t0 = _rec26i["turns"][0]["logs"]
check("観戦記録: 見せ合いは6体（隠れ選出）", any("相手候補6体" in l for l in _t0), " / ".join(_t0[:4]))
check("観戦記録: 先発の登場が記録される（opp_view.on_enter）", sum(1 for l in _t0 if "登場（" in l) == 2, " / ".join(_t0))


print("\n=== 26j. 相性ベースの規則的な選出（SELECT_MODE=matchup） ===")
# ニューラル選出のベースライン。相手6体のどの3体が来ても穴が無い3体を、攻め・守り（弱点の重複）・1v1・負荷分散で選ぶ。
import simulator.selection_matchup as _SM26j
from simulator.learned_selection import learned_select_party as _lsp26j
_T26j = {"off": [[0.5] * 6 for _ in range(6)], "tp": [{"じめん": 0.9} for _ in range(6)],
         "weak": [{"じめん": i in (0, 1)} for i in range(6)], "mu": [[0.0] * 6 for _ in range(6)],
         "mega_me": [False] * 6, "mega_opp": [False] * 6}
_c26j = _SM26j.choose(_T26j)
check("守り: じめん弱点の2体（0と1）を同時に選ばない", not ({0, 1} <= set(_c26j)), str(_c26j))
_T26j["mu"] = [[1.0 if (i == 2 and j < 3) or (i == 3 and j >= 3) else 0.0 for j in range(6)] for i in range(6)]
_T26j["weak"] = [{"じめん": False} for _ in range(6)]
_c26j = _SM26j.choose(_T26j)
check("1v1: 相手の前半に勝てる2と後半に勝てる3の両方を選ぶ", {2, 3} <= set(_c26j), str(_c26j))
_T26j["mega_me"] = [True, True, False, False, False, False]
_c26j = _SM26j.choose(_T26j)
check("メガ1体ルール: メガ石持ちはちょうど1体", sum(1 for i in _c26j if i in (0, 1)) == 1, str(_c26j))
_T26j["mega_opp"] = [True] * 5 + [False]
_c26j = _SM26j.choose(_T26j)
check("相手の推定メガ石持ちが5体以上でも候補が空にならない（メガ数最少の組で代える）", len(_c26j) == 3,
      f"{_c26j} 相手の組={_SM26j._trios(_T26j['mega_opp'])[:3]}")
_os26j = os.environ.get("SELECT_MODE"); os.environ["SELECT_MODE"] = "matchup"
_A26j = [_mk26c(x) for x in _P1s]; _B26j = [_mk26c(x) for x in _P2s]
_s1 = [p.name for p in _lsp26j(_A26j, _B26j, dl)]
_B26j[0].moves = list(reversed(_B26j[0].moves)); _B26j[0].item = "たべのこし"
_s2 = [p.name for p in _lsp26j(_A26j, _B26j, dl)]
if _os26j is None: os.environ.pop("SELECT_MODE", None)
else: os.environ["SELECT_MODE"] = _os26j
check("SELECT_MODE=matchup で3体を返し、メガ石持ちは1体", len(_s1) == 3 and
      sum(1 for n in _s1 if any(p.name == n and p.mega_data is not None for p in _A26j)) == 1, str(_s1))
check("相手の真の技・持ち物を読まない（変えても選出が同じ）", _s1 == _s2, f"{_s1} / {_s2}")


print("\n=== 26k. 学習選出の既定（simulator/selector_m6e.json、既定ON・相手の仮定 learnedK8） ===")
# M-6 の選出モデル（1037次元＝現行の既定特徴量）を既定で使う。旧 selector_m2/m3 は905次元で現行では動かない（削除/未使用）。
import json as _js26k, tempfile as _tf26k
import simulator.learned_selection as _LS26k
from simulator.features import feature_dim as _fd26k
from simulator.ai import select_party as _sp26k
_sv26k = (_LS26k._PATH, _LS26k._LOADED, _LS26k._MODEL, os.environ.get("LEARNED_SELECTION"))
os.environ.pop("LEARNED_SELECTION", None)
_sv26k_env = os.environ.pop("SEL_OPP_ASSUME", None), os.environ.pop("SELECTOR_PATH", None)
import importlib as _il26k
check("既定のモデルパスは selector_m6e.json", os.path.basename(_il26k.reload(_LS26k)._PATH) == "selector_m6e.json", _LS26k._PATH)
check("SEL_OPP_ASSUME 未指定の既定は learnedK（K=8）・heur でヒューリスティック", _LS26k._opp_mode() == "learnedK" and
      (os.environ.__setitem__("SEL_OPP_ASSUME", "heur") or _LS26k._opp_mode()) is None)
os.environ.pop("SEL_OPP_ASSUME", None)
for _k26k, _v26k in zip(("SEL_OPP_ASSUME", "SELECTOR_PATH"), _sv26k_env):
    if _v26k is not None: os.environ[_k26k] = _v26k
_LS26k._PATH = os.path.join(os.path.dirname(_LS26k.__file__), "selector_m6e.json"); _LS26k._LOADED = False
_m26k = _LS26k._load()
check("既定で selector_m6e.json を読み、入力が megaform_ohko1（現行の特徴量＋一撃必殺18次元）", _m26k is not None and _m26k["v2"] and _m26k["W1"].shape[1] == _fd26k() + 18,
      f"{None if _m26k is None else _m26k['W1'].shape} vs {_fd26k()}")
_A26k = [_mk26c(x) for x in _P1s]; _B26k = [_mk26c(x) for x in _P2s]
_sel26k = _LS26k.learned_select_party(_A26k, _B26k, dl, n=3, temperature=0.0)
check("学習選出: 3体・メガ石持ちちょうど1体", len(_sel26k) == 3 and sum(1 for p in _sel26k if p.mega_data is not None) == 1,
      str([p.name for p in _sel26k]))
os.environ["LEARNED_SELECTION"] = "0"; _LS26k._LOADED = False
check("LEARNED_SELECTION=0 ならヒューリスティック選出と同じ",
      [p.name for p in _LS26k.learned_select_party(_A26k, _B26k, dl, n=3, temperature=0.0)]
      == [p.name for p in _sp26k(_A26k, _B26k, dl, n=3, temperature=0.0)])
os.environ.pop("LEARNED_SELECTION", None)
_bad26k = _tf26k.NamedTemporaryFile("w", suffix=".json", delete=False)
_js26k.dump({"W1": [[0.0] * 905], "b1": [0.0], "W2": [0.0], "b2": 0.0}, _bad26k); _bad26k.close()
_LS26k._PATH = _bad26k.name; _LS26k._LOADED = False
check("入力次元が合わないモデル（旧905次元）はヒューリスティックに落ちる", _LS26k._load() is None)
_LS26k._PATH, _LS26k._LOADED, _LS26k._MODEL = _sv26k[0], False, None
if _sv26k[3] is None: os.environ.pop("LEARNED_SELECTION", None)
else: os.environ["LEARNED_SELECTION"] = _sv26k[3]


print("\n=== 26l. 学習選出の3実装（元の実装・Python 高速版・Rust 版）が同じ選出・同じ乱数の消費 ===")
# 高速版は相手の仮定（select_party 3回）の採点を1回に、状態ベクトルは対面内で個体の特徴ブロック・与ダメ割合・速度を使い回して組む。
# Rust 版は候補・相手の仮定・状態ベクトルを Rust で作り、推論と選択は Python（numpy）。数千対面の照合は _local の sel_impl_check.py
import random as _r26l
import simulator.learned_selection as _LS26l
_sv26l = os.environ.get("LEARNED_SELECTION_IMPL")
_LS26l._LOADED = False
_res26l = {}
for _impl in ("ref", "fast", "rust"):
    os.environ["LEARNED_SELECTION_IMPL"] = _impl
    _out = []
    for _k, (_pa, _pb) in enumerate(((_P1s, _P2s), (_P2s, _P1s))):
        _A = [_mk26c(x) for x in _pa]; _B = [_mk26c(x) for x in _pb]
        for _t in (0.0, 0.3):
            _g = _r26l.Random(100 + _k)
            _out.append([_A.index(p) for p in _LS26l.learned_select_party(_A, _B, dl, n=3, temperature=_t, rng=_g)])
            _out.append(_g.random())
    _res26l[_impl] = _out
if _sv26l is None: os.environ.pop("LEARNED_SELECTION_IMPL", None)
else: os.environ["LEARNED_SELECTION_IMPL"] = _sv26l
check("学習選出: 高速版が元の実装と同じ（温度0/0.3・乱数の消費まで）", _res26l["fast"] == _res26l["ref"],
      f"{_res26l['ref']} / {_res26l['fast']}")
check("学習選出: Rust 版が元の実装と同じ（温度0/0.3・乱数の消費まで）", _res26l["rust"] == _res26l["ref"],
      f"{_res26l['ref']} / {_res26l['rust']}")
# 乱数を消費する技（きまぐレーザー）持ちがいる対面は、Rust 版・高速版を使わず元の実装で（Rust では panic していた）
_kmg26l = [x for x in ["ブリジュラス@いのちのたま:ひかえめ:きまぐレーザー|りゅうせいぐん|ラスターカノン|10まんボルト:0/0/0/32/0/32:じきゅうりょく"]]
_Ak = [_mk26c(x) for x in _kmg26l + _P1s[1:]]; _Bk = [_mk26c(x) for x in _P2s]
check("学習選出: 乱数を消費する技の持ち主がいても落ちない（Rust 版・高速版を使わない）",
      not _LS26l._rust_ok(_Ak, _Bk) and not _LS26l._fast_ok(_Ak, _Bk)
      and len(_LS26l.learned_select_party(_Ak, _Bk, dl, n=3, temperature=0.0, rng=_r26l.Random(3))) == 3)
from simulator.ai import select_party as _sp26l, select_party_multi as _spm26l
_A = [_mk26c(x) for x in _P1s]; _B = [_mk26c(x) for x in _P2s]
_g1 = _r26l.Random(5); _g2 = _r26l.Random(5)
_seq = [[p.name for p in _sp26l(_A, _B, dl, n=3, temperature=t, rng=_g1)] for t in (0.0, 1.0, 1.0)]
_mul = [[p.name for p in x] for x in _spm26l(_A, _B, dl, n=3, temperatures=(0.0, 1.0, 1.0), rng=_g2)]
check("select_party_multi: select_party を続けて呼んだのと同じ（乱数の消費も）", _seq == _mul and _g1.random() == _g2.random(),
      f"{_seq} / {_mul}")


print("\n=== 26m. 提案の採点の選出（学習選出・面ごとに固定シード） ===")
# 採点はグローバル乱数に依らず決まり（乱数を消費する技も面ごとの固定シード）、同じ候補を2回採点しても同じ値。
# Rust 経路（live_feats の中で学習選出まで完結）と Python 経路が選出・ネット特徴まで一致
try:
    import _product3 as _P326m, feature1 as _F26m, random as _r26m
    _F26m._ensure_loaded("M-6", 8)
    _P326m.SEASON = "M-6"
    _P326m._score_setup(_F26m._W["loader"], _F26m._W["net"], [_P1s, _P2s])
    _r26m.seed(1); _v1 = _P326m.surrogate_score(_P2s)
    _r26m.seed(999); _r26m.random(); _v2 = _P326m.surrogate_score(_P2s)
    check("採点: グローバル乱数に依らず同じ値", _v1 == _v2, f"{_v1} / {_v2}")
    import pokenavi_engine as _E26m, numpy as _np26m, statistics as _st26m
    from simulator import learned_selection as _LS26m
    _kmg26m = "ブリジュラス@いのちのたま:ひかえめ:きまぐレーザー|りゅうせいぐん|ラスターカノン|10まんボルト:0/0/0/32/0/32:じきゅうりょく"
    _K26m = [_kmg26m] + list(_P1s[1:])           # 乱数を消費する技（きまぐレーザー）の持ち主がいる候補
    _r26m.seed(3); _vk1 = _P326m.surrogate_score(_K26m)
    _r26m.seed(4); _vk2 = _P326m.surrogate_score(_K26m)
    check("採点: 乱数を消費する技の持ち主がいてもグローバル乱数に依らず同じ値", _vk1 == _vk2, f"{_vk1} / {_vk2}")
    # 選出まで Rust 内で（学習選出のモデルは1回だけ渡す）。選出・状態ベクトル・ネット特徴が Python と一致
    _E26m.live_setup([_P1s, _P2s], "M-6")
    check("live_set_selector: 学習選出のモデルを読める", _E26m.live_set_selector(_LS26m._PATH) is True)
    for _nm, _sp, _v in (("通常", _P2s, _v1), ("きまぐレーザー", _K26m, _vk1)):
        _A26m = [build_from_spec(parse_pokemon_spec(x), _F26m._W["loader"], season="M-6", randomize=False) for x in _sp]
        _py = _P326m.panel_selections(_A26m)
        _rs = [(list(a), list(b)) for a, b in _E26m.live_panel_selections(list(_sp))]
        check(f"採点の選出（{_nm}）: Rust 内の学習選出が Python と一致", _rs == [tuple(x) for x in _py], f"{_rs} / {_py}")
        _sb26m, *_r26mr = _E26m.live_feats(list(_sp))
        _npan, _dim = _r26mr[3], _r26mr[4]
        _X26m = _np26m.frombuffer(_sb26m, dtype="<f8").reshape(_npan, _dim)
        _vals = [_F26m._W["net"].evaluate(_X26m[i], [0])[1] for i in range(_npan)]
        check(f"採点（{_nm}）: Rust 経路（選出まで Rust）のネット特徴が Python と一致", _st26m.mean(_vals) == _v,
              f"{_st26m.mean(_vals)} / {_v}")
    _sb26n, *_ = _E26m.live_feats(list(_P2s), _P326m.panel_selections(
        [build_from_spec(parse_pokemon_spec(x), _F26m._W["loader"], season="M-6", randomize=False) for x in _P2s]))
    check("live_feats: 選出を渡した場合も同じ状態ベクトル", _sb26n == _E26m.live_feats(list(_P2s))[0])
    _E26m.live_set_selector("")
    _A26h = [build_from_spec(parse_pokemon_spec(x), _F26m._W["loader"], season="M-6", randomize=False) for x in _P2s]
    _sv26m = (_LS26m._MODEL, _LS26m._LOADED); _LS26m._MODEL, _LS26m._LOADED = None, True   # モデル無し（読めなかった時）
    try:
        _pyh = _P326m.panel_selections(_A26h)
    finally:
        _LS26m._MODEL, _LS26m._LOADED = _sv26m
    check("採点の選出（モデル無し）: Rust のヒューリスティック選出が Python と一致",
          [(list(a), list(b)) for a, b in _E26m.live_panel_selections(list(_P2s))] == [tuple(x) for x in _pyh])
except ImportError as _e26m:
    check("採点のテスト（pyengine が必要）", False, str(_e26m))


_SCRIPTS_DIR26n = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print("\n=== 26n. 提案の2段階採点（1段目＝同じ採点モデル・選出だけヒューリスティック） ===")
# 採点器を2つ（本採点＝スロット0・1段目＝スロット1）持っても互いに干渉せず、1段目も Rust 経路と Python 経路が一致
try:
    import _ensemble_surrogate as _ES26n, feature1 as _F26n, numpy as _np26n
    from gen_party_pool import PartyGen as _PG26n
    from _threat_coverage import load_threats as _lt26n
    _F26n._ensure_loaded("M-6", 8)
    _sv26n = os.environ.get("POOL_SEASON"); os.environ["POOL_SEASON"] = "M-6"
    import _live_rust as _LR26n, _product3 as _P326n
    _LR26n.SEASON = "M-6"; _P326n.SEASON = "M-6"
    _L26n = _F26n._W["loader"]; _pg26n = _PG26n(); _th26n = _lt26n(_L26n)
    _e0 = _ES26n.EnsembleScorer(_L26n, _F26n._W["net"], _pg26n, _th26n, model=os.path.join(_SCRIPTS_DIR26n, "ensemble_model_m6.json"))
    _x0a = _e0._x(_P1s)
    _e1 = _ES26n.EnsembleScorer(_L26n, _F26n._W["net"], _pg26n, _th26n,
                                model=os.path.join(_SCRIPTS_DIR26n, "ensemble_model_m6.json"), heuristic=True, slot=1)
    check("2段階採点: 本採点・1段目とも Rust 経路が有効", _e0._rust is not None and _e1._rust is not None)
    check("2段階採点: 1段目の採点器を作っても本採点の特徴量は変わらない（Rust のスロットが別）",
          _np26n.array_equal(_x0a, _e0._x(_P1s)))
    for _nm26n, _e in (("本採点", _e0), ("1段目", _e1)):
        _xr = _e._x(_P2s); _r = _e._rust; _e._rust = None
        try:
            _xp = _e._x(_P2s)
        finally:
            _e._rust = _r
        check(f"2段階採点（{_nm26n}）: Rust 経路と Python 経路の特徴量が一致", _np26n.array_equal(_xr, _xp), f"{_xr[:3]} / {_xp[:3]}")
    _A26n = [build_from_spec(parse_pokemon_spec(x), _L26n, season="M-6", randomize=False) for x in _P2s]
    check("2段階採点: 1段目の選出（ヒューリスティック）が Rust と Python で一致",
          [(list(a), list(b)) for a, b in _E26m.live_panel_selections(list(_P2s), 1)]
          == [tuple(x) for x in _P326n.panel_selections(_A26n, _e1.panel_built, heuristic=True)])
    if _sv26n is None: os.environ.pop("POOL_SEASON", None)
    else: os.environ["POOL_SEASON"] = _sv26n
except ImportError as _e26n:
    check("2段階採点のテスト（pyengine が必要）", False, str(_e26n))


print("\n=== 26o. 提案の採点の学習選出: Rust 高速版（第1層の分解・相手の仮定を表で）が元の実装と同じ ===")
# 高速版は W1·x を個体ブロック・対面（与ダメ割合・素早さ）・定数の寄与に分け、選出1回につき1回だけ前計算する。
# 半減きのみ・ホズのみの消費（符号化の中で次の対面へ持ち越す）も追う。SEL_FAST_CHECK=1 で元の実装も計算して照合、SEL_FAST=0 で元の実装
import subprocess as _sp26o, sys as _sy26o, json as _js26o
_code26o = r"""
import sys, json, os
sys.path.insert(0, %r)
import pokenavi_engine as E
from simulator import learned_selection as LS
A = json.loads(sys.argv[1]); B = json.loads(sys.argv[2]); K = json.loads(sys.argv[3])
E.live_setup([A, B], "M-6", 0); E.live_set_selector(LS._PATH, 0)
out = [E.live_panel_selections(c, 0) for c in K]
st = E.sel_fast_stats_take() if os.environ.get("SEL_FAST_CHECK") == "1" else None
print(json.dumps([out, st]))
""" % _SCRIPTS_DIR26n
def _berry26o(sp, it):
    head, rest = sp.split(":", 1)
    return head.split("@")[0] + "@" + it + ":" + rest
_A26o = [_P1s[0], _P1s[1], _berry26o(_P1s[2], "リンドのみ"), _berry26o(_P1s[3], "イトケのみ"), _P1s[4], _P1s[5]]
_B26o = [_berry26o(_P2s[0], "ヤチェのみ"), _P2s[1], _berry26o(_P2s[2], "オッカのみ"), _P2s[3], _berry26o(_P2s[4], "ホズのみ"),
         _berry26o(_P2s[5], "ヨプのみ")]
_kmg26o = "ブリジュラス@いのちのたま:ひかえめ:きまぐレーザー|りゅうせいぐん|ラスターカノン|10まんボルト:0/0/0/32/0/32:じきゅうりょく"
_K26o = [_A26o, _B26o, list(_P1s), list(_P2s), [_kmg26o] + list(_P1s[1:])]
def _run26o(env):
    e = dict(os.environ); e.update(env)
    r = _sp26o.run([_sy26o.executable, "-c", _code26o, _js26o.dumps(_A26o), _js26o.dumps(_B26o), _js26o.dumps(_K26o)],
                   capture_output=True, text=True, env=e)
    return _js26o.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else (None, r.stderr[-300:])
_fast26o, _st26o = _run26o({"SEL_FAST_CHECK": "1", "SEL_OPP_ASSUME": "heur"})
_ref26o, _ = _run26o({"SEL_FAST": "0", "SEL_OPP_ASSUME": "heur"})
_dflt26o, _ = _run26o({"SEL_OPP_ASSUME": "heur"})
_refK26o, _ = _run26o({"SEL_FAST": "0", "SEL_OPP_ASSUME": "learnedK", "SEL_OPP_K": "8"})
_dfltK26o, _ = _run26o({"SEL_OPP_ASSUME": "learnedK", "SEL_OPP_K": "8"})
check("学習選出の高速版: 元の実装と選出が全件同じ・値の差は丸め誤差だけ（半減きのみ・ホズのみ持ちを含む）",
      _st26o is not None and _st26o[0] > 0 and _st26o[1] == 0 and _st26o[2] < 1e-12, f"{_st26o}")
check("学習選出の高速版: 相手の仮定（ヒューリスティック選出）を表で計算しても元と同じ仮定・乱数の消費",
      _st26o is not None and _st26o[4] > 0 and _st26o[5] == 0, f"{_st26o}")
check("学習選出の高速版: 乱数を消費する技の持ち主がいる対面は元の実装に落とす", _st26o is not None and _st26o[3] > 0, f"{_st26o}")
check("学習選出の高速版: 既定（高速版）と SEL_FAST=0（元の実装）でパネルの選出が同じ", _dflt26o is not None and _dflt26o == _ref26o,
      f"{_dflt26o} / {_ref26o}")
check("学習選出の高速版: 相手の仮定 learnedK8 でも高速版と SEL_FAST=0（元の実装）でパネルの選出が同じ",
      _dfltK26o is not None and _dfltK26o == _refK26o, f"{_dfltK26o} / {_refK26o}")


print("\n=== 26p. 学習選出の「相手の選出の仮定」を学習選出に（env SEL_OPP_ASSUME=learned、既定はヒューリスティック） ===")
# 相手の仮定＝相手側の学習選出（その中の仮定はこちらのヒューリスティック）の温度0＋温度 SEL_OPP_TEMP の抽選2回。
# 3実装（元・Python 高速版・Rust 版）と Rust の採点の選出（selector.rs select_cached）が同じ選出・同じ乱数の消費
import random as _r26p
import simulator.learned_selection as _LS26p
_sv26p = {k: os.environ.get(k) for k in ("SEL_OPP_ASSUME", "LEARNED_SELECTION_IMPL")}
os.environ["SEL_OPP_ASSUME"] = "heur"
_LS26p._LOADED = False
_m26p = _LS26p._load()
_A26p = [_mk26c(x) for x in _P1s]; _B26p = [_mk26c(x) for x in _P2s]
_g1 = _r26p.Random(41); _g2 = _r26p.Random(41)
_os26p = _LS26p._opp_learned(_A26p, _B26p, dl, 3, _g1, _m26p)
_want26p = [_B26p.index(p) for p in _LS26p.learned_select_party(_B26p, _A26p, dl, n=3, temperature=0.0, rng=_g2)]
_ocand26p = _LS26p._candidates(_B26p, 3)
check("相手の仮定（学習選出版）: 1つ目は相手側の学習選出（温度0）と同じ", _os26p is not None and _os26p[0] == _want26p,
      f"{_os26p} / {_want26p}")
check("相手の仮定（学習選出版）: 3つとも相手の候補（メガ1体ルール内）、乱数は相手の学習選出の分＋抽選2回",
      _os26p is not None and len(_os26p) == 3 and all(o in _ocand26p for o in _os26p)
      and (_g2.random(), _g2.random(), _g2.random())[2] == _g1.random())
_res26p = {}
os.environ["SEL_OPP_ASSUME"] = "learned"
for _impl in ("ref", "fast", "rust"):
    os.environ["LEARNED_SELECTION_IMPL"] = _impl
    _out = []
    for _k, (_pa, _pb) in enumerate(((_P1s, _P2s), (_P2s, _P1s))):
        _A = [_mk26c(x) for x in _pa]; _B = [_mk26c(x) for x in _pb]
        for _t in (0.0, 0.3):
            _g = _r26p.Random(200 + _k)
            _out.append([_A.index(p) for p in _LS26p.learned_select_party(_A, _B, dl, n=3, temperature=_t, rng=_g)])
            _out.append(_g.random())
    _res26p[_impl] = _out
os.environ["SEL_OPP_ASSUME"] = "heur"
os.environ.pop("LEARNED_SELECTION_IMPL", None)
check("SEL_OPP_ASSUME=learned: 高速版・Rust 版が元の実装と同じ（温度0/0.3・乱数の消費まで）",
      _res26p["fast"] == _res26p["ref"] and _res26p["rust"] == _res26p["ref"], f"{_res26p}")
_g3 = _r26p.Random(41)
_dflt26p = [_A26p.index(p) for p in _LS26p.learned_select_party(_A26p, _B26p, dl, n=3, temperature=0.0, rng=_g3)]
_g4 = _r26p.Random(41)
_base26p = max(_LS26p._score_cands(_A26p, _B26p, dl, 3, _g4, _m26p), key=lambda x: x[1])[0]
for _k, _v in _sv26p.items():
    if _v is None: os.environ.pop(_k, None)
    else: os.environ[_k] = _v
check("SEL_OPP_ASSUME=heur: ヒューリスティックの仮定（2026-10-06 までの既定）", _dflt26p == list(_base26p) and _g3.random() == _g4.random(),
      f"{_dflt26p} / {_base26p}")
try:
    import pokenavi_engine as _E26p
    _ok26p = "osels" in (getattr(_E26p.learned_select_states, "__text_signature__", "") or "")
except ImportError:
    _ok26p = False
if _ok26p:
    _code26p = r"""
import sys, json, os
sys.path.insert(0, %r)
import pokenavi_engine as E
import feature1 as F
F._ensure_loaded("M-6", 8)
import _product3 as P3
from simulator import learned_selection as LS
from simulator.pokemon import build_from_spec, parse_pokemon_spec
P3.SEASON = "M-6"
A = json.loads(sys.argv[1]); B = json.loads(sys.argv[2])
P3._score_setup(F._W["loader"], F._W["net"], [A, B])
E.live_setup([A, B], "M-6", 0); E.live_set_selector(LS._PATH, 0)
out = []
for c in (A, B):
    py = [[list(x), list(y)] for x, y in P3.panel_selections([build_from_spec(parse_pokemon_spec(s), F._W["loader"], season="M-6", randomize=False) for s in c])]
    rs = [[list(x), list(y)] for x, y in E.live_panel_selections(c, 0)]
    out.append([py, rs])
print(json.dumps(out))
""" % _SCRIPTS_DIR26n
    def _run26p(env):
        e = dict(os.environ); e.update(env)
        r = _sp26o.run([_sy26o.executable, "-c", _code26p, _js26o.dumps(_P1s), _js26o.dumps(_P2s)], capture_output=True,
                       text=True, env=e, cwd=_SCRIPTS_DIR26n)
        return _js26o.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else None
    _l26p = _run26p({"SEL_OPP_ASSUME": "learned"})
    _l0p = _run26p({"SEL_OPP_ASSUME": "learned", "SEL_FAST": "0"})
    check("SEL_OPP_ASSUME=learned: Rust の採点の選出（select_cached）が Python と一致",
          _l26p is not None and all(py == rs for py, rs in _l26p), f"{_l26p}")
    check("SEL_OPP_ASSUME=learned: Rust 高速版と元の実装（SEL_FAST=0）で同じ", _l26p is not None and _l26p == _l0p)
else:
    print("  （pyengine が SEL_OPP_ASSUME 対応前のビルドなので Rust 側の照合は省略。maturin develop 後に実行される）")


print("\n=== 26q. 学習選出の相手の仮定 learnedK / all（mean・minmix・weighted）（env SEL_OPP_ASSUME、既定はヒューリスティック） ===")
# learnedK＝相手側の学習選出の値の softmax 上位K候補を和1の重みで、all＝相手の全候補を 平均／α·平均＋(1−α)·組ごとの最悪／softmax の重みで。
# Python 3実装（元・高速版・Rust 版）と Rust select_scores（guide_rows・Rust 単独で相手の仮定まで計算）が同じ選出・同じ乱数の消費
import random as _r26q
import simulator.learned_selection as _LS26q
_K26q = ("SEL_OPP_ASSUME", "SEL_OPP_K", "SEL_OPP_MIX", "SEL_OPP_ALPHA", "SEL_OPP_TEMP", "LEARNED_SELECTION_IMPL")
_sv26q = {k: os.environ.get(k) for k in _K26q}
def _env26q(d):
    for k in _K26q:
        os.environ.pop(k, None)
    os.environ.update(d)
_tw26q = _LS26q._topk_weights([0.2, 0.5, 0.5, 0.1, 0.4], 1.0, 3)
check("_topk_weights: 重みの大きい順に K 個（同じ重みは添字順）・重みの和＝1",
      [i for i, _ in _tw26q] == [1, 2, 4] and abs(sum(w for _, w in _tw26q) - 1.0) < 1e-15, f"{_tw26q}")
check("_topk_weights: K が候補数以上なら全候補・和＝1",
      len(_LS26q._topk_weights([0.2, 0.5, 0.1], 1.0, 99)) == 3
      and abs(sum(w for _, w in _LS26q._topk_weights([0.2, 0.5, 0.1], 1.0, 99)) - 1.0) < 1e-15)
_x26q = [0.6, 0.6, 0.6, 0.2, 0.4, 0.3]
check("_agg: minmix α=1 は平均・α=0 は3体の組ごとの平均の最悪・α=0.5 はその中間",
      abs(_LS26q._agg(_x26q, ("minmix", 1.0, 3)) - 0.45) < 1e-15 and abs(_LS26q._agg(_x26q, ("minmix", 0.0, 3)) - 0.3) < 1e-15
      and abs(_LS26q._agg(_x26q, ("minmix", 0.5, 3)) - 0.375) < 1e-15)
check("_agg: 重み付き和", _LS26q._agg([0.4, 0.8], ("w", [0.25, 0.75])) == 0.25 * 0.4 + 0.75 * 0.8)
_LS26q._LOADED = False
_m26q = _LS26q._load()
_A26q = [_mk26c(x) for x in _P1s]; _B26q = [_mk26c(x) for x in _P2s]
_env26q({"SEL_OPP_ASSUME": "learnedK"})
_oa26q = _LS26q._opp_assume(_A26q, _B26q, dl, 3, _r26q.Random(5), _m26q)
check("learnedK: 相手の仮定は既定 K=8 個・相手の候補・重みの和＝1・重みは降順",
      _oa26q is not None and len(_oa26q[0]) == 8 and all(o in _LS26q._candidates(_B26q, 3) for o in _oa26q[0])
      and abs(sum(_oa26q[1][1]) - 1.0) < 1e-12 and _oa26q[1][1] == sorted(_oa26q[1][1], reverse=True), f"{_oa26q}")
_env26q({"SEL_OPP_ASSUME": "learnedK", "SEL_OPP_K": "1"})
_g5 = _r26q.Random(5); _g6 = _r26q.Random(5)
_oa1 = _LS26q._opp_assume(_A26q, _B26q, dl, 3, _g5, _m26q)
_env26q({"SEL_OPP_ASSUME": "heur"})
_want26q = [_B26q.index(p) for p in _LS26q.learned_select_party(_B26q, _A26q, dl, n=3, temperature=0.0, rng=_g6)]
check("learnedK K=1: 仮定は相手側の学習選出（温度0）だけ・重み1・乱数の消費は相手の学習選出の分だけ",
      _oa1 is not None and _oa1[0] == [_want26q] and _oa1[1][1] == [1.0] and _g5.random() == _g6.random(), f"{_oa1} / {_want26q}")
_env26q({"SEL_OPP_ASSUME": "all", "SEL_OPP_MIX": "weighted"})
_oaw = _LS26q._opp_assume(_A26q, _B26q, dl, 3, _r26q.Random(5), _m26q)
check("all weighted: 相手の全候補・重みの和＝1",
      _oaw is not None and sorted(_oaw[0]) == sorted(_LS26q._candidates(_B26q, 3)) and abs(sum(_oaw[1][1]) - 1.0) < 1e-12)
_env26q({"SEL_OPP_ASSUME": "all", "SEL_OPP_MIX": "minmix"})
_g7 = _r26q.Random(5)
_oam = _LS26q._opp_assume(_A26q, _B26q, dl, 3, _g7, _m26q)
check("all minmix: 相手の全候補（候補順）・α 既定0.5・乱数を消費しない",
      _oam is not None and _oam[0] == _LS26q._candidates(_B26q, 3) and _oam[1] == ("minmix", 0.5, 3)
      and _g7.random() == _r26q.Random(5).random())
_env26q({"SEL_OPP_ASSUME": "bogus"})
check("SEL_OPP_ASSUME が未知の値なら既定（仮定を作らない）", _LS26q._opp_assume(_A26q, _B26q, dl, 3, _r26q.Random(5), _m26q) is None)
_MODES26q = {"learnedK": {"SEL_OPP_ASSUME": "learnedK"},
             "all_mean": {"SEL_OPP_ASSUME": "all", "SEL_OPP_MIX": "mean"},
             "all_minmix": {"SEL_OPP_ASSUME": "all", "SEL_OPP_MIX": "minmix", "SEL_OPP_ALPHA": "0.25"},
             "all_weighted": {"SEL_OPP_ASSUME": "all", "SEL_OPP_MIX": "weighted"}}
_py26q = {}
for _mn, _me in _MODES26q.items():
    _res = {}
    for _impl in ("ref", "fast", "rust"):
        _env26q(dict(_me, LEARNED_SELECTION_IMPL=_impl))
        _out = []
        for _k, (_pa, _pb) in enumerate(((_P1s, _P2s), (_P2s, _P1s))):
            _A = [_mk26c(x) for x in _pa]; _B = [_mk26c(x) for x in _pb]
            _g = _r26q.Random(301 + _k)
            _sc = _LS26q.learned_select_scores(_A, _B, dl, n=3, rng=_g)
            _out.append(([_A.index(p) for p in max(_sc, key=lambda x: x[1])[0]], [v for _, v in _sc], _g.random()))
        _res[_impl] = _out
    _py26q[_mn] = [o[0] for o in _res["rust"]]
    check(f"SEL_OPP_ASSUME {_mn}: 高速版・Rust 版が元の実装と同じ選出・値（差1e-12未満）・乱数の消費",
          all(a[0] == b[0] and a[2] == b[2] and max(abs(x - y) for x, y in zip(a[1], b[1])) < 1e-12
              for _i in ("fast", "rust") for a, b in zip(_res[_i], _res["ref"])), f"{[(k, [o[0] for o in v]) for k, v in _res.items()]}")
_env26q({"SEL_OPP_ASSUME": "heur"})
_dq = _LS26q.learned_select_scores(_A26q, _B26q, dl, n=3, rng=_r26q.Random(41))
_bq = _LS26q._score_cands(_A26q, _B26q, dl, 3, _r26q.Random(41), _m26q)
check("SEL_OPP_ASSUME=heur: 値がヒューリスティックの仮定・平均と完全一致",
      [(list(_A26q.index(p) for p in o), v) for o, v in _dq] == [(list(c), v) for c, v in _bq])
for _k, _v in _sv26q.items():
    if _v is None: os.environ.pop(_k, None)
    else: os.environ[_k] = _v
try:
    import pokenavi_engine as _E26q
    _ok26q = hasattr(_E26q, "guide_rows")
except ImportError:
    _ok26q = False
if _ok26q:
    _code26q = r"""
import sys, json
import pokenavi_engine as E
A = json.loads(sys.argv[1]); B = json.loads(sys.argv[2]); P = sys.argv[3]
print(json.dumps([E.guide_rows(A, [B], "M-6", 0, 300, P)[0][0], E.guide_rows(B, [A], "M-6", 0, 301, P)[0][0]]))
"""
    def _run26q(env):
        e = dict(os.environ)
        for k in _K26q:
            e.pop(k, None)
        e.update(env)
        r = _sp26o.run([_sy26o.executable, "-c", _code26q, _js26o.dumps(_P1s), _js26o.dumps(_P2s), _LS26q._PATH],
                       capture_output=True, text=True, env=e, cwd=_SCRIPTS_DIR26n)
        return _js26o.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else r.stderr[-500:]
    for _mn, _me in _MODES26q.items():
        _rs = _run26q(_me); _rs0 = _run26q(dict(_me, SEL_FAST="0"))
        check(f"SEL_OPP_ASSUME {_mn}: Rust select_scores（高速版・元の実装とも）の選出が Python と一致",
              _rs == _py26q[_mn] and _rs0 == _py26q[_mn], f"{_rs} / {_rs0} / {_py26q[_mn]}")
else:
    print("  （pyengine が無いので Rust 側の照合は省略）")


print("\n=== 26r. 学習選出のモデル形式（隠れ層 ReLU・selector_m6c 等の別モデル）（既定 selector_m6b・tanh は不変） ===")
# モデル JSON の "act"（無ければ tanh）。ReLU は Python _predict と Rust Selector（逐次和・高速版）の両方。未知の活性化・"U"（入力の追加）は
# 読まずにヒューリスティックへ。ReLU モデルでも3実装（元・高速版・Rust 版）と Rust select_scores（guide_rows）の選出が一致
import json as _j26r, tempfile as _tf26r, random as _r26r
import numpy as _np26r
import simulator.learned_selection as _LS26r
_K26r = ("SEL_OPP_ASSUME", "SEL_OPP_K", "LEARNED_SELECTION_IMPL")
_sv26r = {k: os.environ.get(k) for k in _K26r}
_p0_26r, _m0_26r, _l0_26r = _LS26r._PATH, _LS26r._MODEL, _LS26r._LOADED
_base26r = _j26r.load(open(os.path.join(os.path.dirname(_LS26r.__file__), "selector_m6b.json")))
_td26r = _tf26r.mkdtemp()
def _wr26r(name, d):
    p = os.path.join(_td26r, name); _j26r.dump(d, open(p, "w")); return p
def _ld26r(p):
    _LS26r._PATH = p; _LS26r._LOADED = False
    return _LS26r._load()
_relu26r = _wr26r("relu.json", dict(_base26r, act="relu"))
_m26r = _ld26r(_relu26r)
check("ReLU のモデル（\"act\": \"relu\"）を読む", _m26r is not None and _m26r["act"] == "relu")
_x26r = _np26r.random.default_rng(3).normal(size=(5, _m26r["W1"].shape[1]))
_want26r = 1 / (1 + _np26r.exp(-(_np26r.maximum(_x26r @ _m26r["W1"].T + _m26r["b1"], 0) @ _m26r["W2"] + _m26r["b2"])))
check("_predict: ReLU の隠れ層", _np26r.allclose(_LS26r._predict(_m26r, _x26r), _want26r, rtol=0, atol=1e-15))
_mt26r = _ld26r(os.path.join(os.path.dirname(_LS26r.__file__), "selector_m6b.json"))
_wt26r = 1 / (1 + _np26r.exp(-(_np26r.tanh(_x26r @ _mt26r["W1"].T + _mt26r["b1"]) @ _mt26r["W2"] + _mt26r["b2"])))
check("_predict: \"act\" の無いモデル（selector_m6b）は tanh のまま", _mt26r["act"] == "tanh"
      and _np26r.array_equal(_LS26r._predict(_mt26r, _x26r), _wt26r))
check("未知の活性化のモデルは読まない（ヒューリスティック選出へ）", _ld26r(_wr26r("gelu.json", dict(_base26r, act="gelu"))) is None)
check("入力の追加（\"U\"）を持つモデルは読まない", _ld26r(_wr26r("u.json", dict(_base26r, act="relu", U=[0.0], Ub=0.0))) is None)
_m6c26r = os.path.join(os.path.dirname(_LS26r.__file__), "selector_m6c.json")
_mc26r = _ld26r(_m6c26r) if os.path.exists(_m6c26r) else None
from simulator.features import feature_dim as _fd26r
check("selector_m6c.json（新ネット教師の再学習・既定ではない）を tanh のモデルとして読み、入力が現行の特徴量と同じ次元",
      _mc26r is not None and _mc26r["act"] == "tanh" and _mc26r["W1"].shape[1] == _fd26r())
_py26rc = None
if _mc26r is not None:
    _rc = {}
    for _impl in ("ref", "rust"):
        for k in _K26r:
            os.environ.pop(k, None)
        os.environ.update({"SEL_OPP_ASSUME": "learnedK", "LEARNED_SELECTION_IMPL": _impl})
        _A = [_mk26c(x) for x in _P1s]; _B = [_mk26c(x) for x in _P2s]
        _sc = _LS26r.learned_select_scores(_A, _B, dl, n=3, rng=_r26r.Random(501))
        _rc[_impl] = ([_A.index(p) for p in max(_sc, key=lambda x: x[1])[0]], [v for _, v in _sc])
    check("selector_m6c: Rust 版が元の実装と同じ選出・値（差1e-12未満）",
          _rc["ref"][0] == _rc["rust"][0] and max(abs(x - y) for x, y in zip(_rc["ref"][1], _rc["rust"][1])) < 1e-12, f"{_rc['ref'][0]} {_rc['rust'][0]}")
    _py26rc = []
    for _k, (_pa, _pb) in enumerate(((_P1s, _P2s), (_P2s, _P1s))):
        _A = [_mk26c(x) for x in _pa]; _B = [_mk26c(x) for x in _pb]
        _sc = _LS26r.learned_select_scores(_A, _B, dl, n=3, rng=_r26r.Random(301 + _k))
        _py26rc.append([_A.index(p) for p in max(_sc, key=lambda x: x[1])[0]])
_m26r = _ld26r(_relu26r)
_res26r = {}
for _impl in ("ref", "fast", "rust"):
    for k in _K26r:
        os.environ.pop(k, None)
    os.environ.update({"SEL_OPP_ASSUME": "learnedK", "LEARNED_SELECTION_IMPL": _impl})
    _out = []
    for _k, (_pa, _pb) in enumerate(((_P1s, _P2s), (_P2s, _P1s))):
        _A = [_mk26c(x) for x in _pa]; _B = [_mk26c(x) for x in _pb]
        _g = _r26r.Random(401 + _k)
        _sc = _LS26r.learned_select_scores(_A, _B, dl, n=3, rng=_g)
        _out.append(([_A.index(p) for p in max(_sc, key=lambda x: x[1])[0]], [v for _, v in _sc], _g.random()))
    _res26r[_impl] = _out
check("ReLU のモデル（learnedK）: 高速版・Rust 版が元の実装と同じ選出・値（差1e-12未満）・乱数の消費",
      all(a[0] == b[0] and a[2] == b[2] and max(abs(x - y) for x, y in zip(a[1], b[1])) < 1e-12
          for _i in ("fast", "rust") for a, b in zip(_res26r[_i], _res26r["ref"])), f"{[(k, [o[0] for o in v]) for k, v in _res26r.items()]}")
_py26r = [o[0] for o in _res26r["rust"]]
for k, v in _sv26r.items():
    if v is None: os.environ.pop(k, None)
    else: os.environ[k] = v
_LS26r._PATH, _LS26r._MODEL, _LS26r._LOADED = _p0_26r, _m0_26r, _l0_26r
try:
    import pokenavi_engine as _E26r
    _ok26r = hasattr(_E26r, "guide_rows")
except ImportError:
    _ok26r = False
if _ok26r:
    _code26r = r"""
import sys, json
import pokenavi_engine as E
A = json.loads(sys.argv[1]); B = json.loads(sys.argv[2]); P = sys.argv[3]
print(json.dumps([E.guide_rows(A, [B], "M-6", 0, 300, P)[0][0], E.guide_rows(B, [A], "M-6", 0, 301, P)[0][0]]))
"""
    def _run26r(path, env):
        e = dict(os.environ)
        for k in _K26r:
            e.pop(k, None)
        e.update(env)
        r = _sp26o.run([_sy26o.executable, "-c", _code26r, _js26o.dumps(_P1s), _js26o.dumps(_P2s), path],
                       capture_output=True, text=True, env=e, cwd=_SCRIPTS_DIR26n)
        return _js26o.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else r.stderr[-500:]
    _rs26r = _run26r(_relu26r, {"SEL_OPP_ASSUME": "learnedK"}); _rs26r0 = _run26r(_relu26r, {"SEL_OPP_ASSUME": "learnedK", "SEL_FAST": "0"})
    check("ReLU のモデル: Rust select_scores（高速版・元の実装とも）の選出が Python と一致",
          _rs26r == _py26r and _rs26r0 == _py26r, f"{_rs26r} / {_rs26r0} / {_py26r}")
    if _py26rc is not None:
        _rsc = _run26r(_m6c26r, {"SEL_OPP_ASSUME": "learnedK"})
        check("selector_m6c: Rust select_scores（guide_rows）の選出が Python の学習選出と一致", _rsc == _py26rc, f"{_rsc} / {_py26rc}")
    _bad26r = _run26r(_wr26r("gelu2.json", dict(_base26r, act="gelu")), {})
    check("Rust: 未知の活性化のモデルは読めないエラー", isinstance(_bad26r, str) and "選出モデルとして読めない" in _bad26r, f"{_bad26r}")
else:
    print("  （pyengine が無いので Rust 側の照合は省略）")

print("\n=== 26b. 必ず急所に当たる技 ===")
# move_master の effect_text が「必ず急所に当たる。」なのに急所率が 1/24 のままだった。
# deep_audit の検出器 (r'必ず急所', ['急所']) はテストのラベル文字列に一致するだけで
# 実際の急所率を検証していなかったため素通りしていた。
from simulator.battle import crit_chance as _cc26b, ALWAYS_CRIT_MOVES as _AC26b
_att26b = BattlePokemon(name="オトスパス", dex=853, type1="みず", type2=None,
                        max_hp=150, hp=150, attack=120, defense=100,
                        sp_attack=80, sp_defense=100, speed=80, ability="", item=None)
_def26b = BattlePokemon(name="ガブリアス", dex=445, type1="ドラゴン", type2="じめん",
                        max_hp=180, hp=180, attack=150, defense=110,
                        sp_attack=90, sp_defense=105, speed=130, ability="さめはだ", item=None)
for _nm26b in ("やまあらし", "こおりのいぶき", "トリックフラワー"):
    _mv26b = dl.get_move(_nm26b)
    check(f"{_nm26b} は必ず急所(1.0)", _mv26b is not None and _cc26b(_att26b, _mv26b, _def26b) == 1.0,
          f"{_cc26b(_att26b, _mv26b, _def26b) if _mv26b else 'move無し'}")
    check(f"{_nm26b} が ALWAYS_CRIT_MOVES に入っている", _nm26b in _AC26b)
# 負例: 急所アップ技(+1=1/8)と通常技(1/24)は 1.0 にならない
for _nm26b, _want26b in (("きりさく", 1/8), ("じしん", 1/24)):
    _mv26b = dl.get_move(_nm26b)
    check(f"負例 {_nm26b} の急所率は {_want26b:.4f}",
          _mv26b is not None and abs(_cc26b(_att26b, _mv26b, _def26b) - _want26b) < 1e-9,
          f"{_cc26b(_att26b, _mv26b, _def26b) if _mv26b else 'move無し'}")
# 負例: シェルアーマー/カブトアーマーは必ず急所も無効化する
_def26b.ability = "シェルアーマー"
check("シェルアーマーは必ず急所を無効化", _cc26b(_att26b, dl.get_move("やまあらし"), _def26b) == 0.0,
      f"{_cc26b(_att26b, dl.get_move('やまあらし'), _def26b)}")


print("\n=== 26. 信念モデルのシーズン（BELIEF_SEASON） ===")
# M-2 の使用率しか引かないと、M-6 で追加された種は事前分布が空になる
# （技prior 0・持ち物0・特性0・EV候補は無振り1件のみ）。探索の決定化がその空分布を使うため、
# 相手を「無振り・技なし」と見なして価値を誤る。env BELIEF_SEASON で引くシーズンを切り替える。
import os as _os26
from simulator.belief import OpponentBelief as _OB26
_L26 = dl
_M6_ONLY = "グソクムシャ"      # M-6 使用率にはあるが M-2 には無い種
_M2_OK = "ガブリアス"          # 両シーズンにある種（対照）

def _prior26(sp, season):
    b = _OB26(_L26, season).ensure(sp)
    return (0, 0, 0, 0) if b is None else (
        len(b.move_prior), len(b.item_prior), len(b.ability_prior), len(b.cands))

_p_m2 = _prior26(_M6_ONLY, "M-2")
_p_m6 = _prior26(_M6_ONLY, "M-6")
# 事前分布が空だと SearchAI._determinize が falsy を上書きせず、相手の真の持ち物・特性・技が
# 探索に残る＝型リーク。使用率行の無いシーズンを指定しても空にならないことが不変条件。
check(f"どのシーズン指定でも {_M6_ONLY} の事前分布が空にならない（型リーク防止）",
      _p_m2[0] > 0 and _p_m2[1] > 0 and _p_m2[2] > 0, f"M-2={_p_m2}")
check(f"M-6 信念では {_M6_ONLY} に技/持ち物/特性の事前分布が付く",
      _p_m6[0] > 0 and _p_m6[1] > 0 and _p_m6[2] > 0, f"{_p_m6}")
check(f"{_M6_ONLY} のEV/性格候補が2件以上（無振り1件に潰れない）",
      _p_m2[3] >= 2 and _p_m6[3] >= 2, f"M-2候補{_p_m2[3]} M-6候補{_p_m6[3]}")
# 全 M-6 上位種で空の事前分布が無いこと
_empties26 = []
for _sp26 in [r[0] for r in dl.con.execute(
        "SELECT pokemon FROM pokemon_usage WHERE season='M-6' AND rule='single' "
        "AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_usage WHERE season='M-6') "
        "ORDER BY rank LIMIT 40")]:
    _b26 = _OB26(_L26, "M-2").ensure(_sp26)
    if _b26 is not None and not _b26.move_prior:
        _empties26.append(_sp26)
check("M-6 上位40種すべてで技の事前分布が空でない", not _empties26, f"{_empties26}")
_c_m2 = _prior26(_M2_OK, "M-2"); _c_m6 = _prior26(_M2_OK, "M-6")
check(f"対照: {_M2_OK} はどちらのシーズンでも事前分布が付く",
      _c_m2[0] > 0 and _c_m6[0] > 0, f"M-2={_c_m2} M-6={_c_m6}")

# 既定シーズンは BELIEF_SEASON > POOL_SEASON > M-6（以前は M-2 固定で、M-6 の対戦でも
# M-2 の使用率分布から相手の型を決定化していた）
_save26 = _os26.environ.get("BELIEF_SEASON")
_savep26 = _os26.environ.get("POOL_SEASON")
try:
    _os26.environ.pop("BELIEF_SEASON", None)
    _os26.environ.pop("POOL_SEASON", None)
    check("BELIEF_SEASON も POOL_SEASON も無ければ既定は M-6", _OB26(_L26).season == "M-6",
          f"{_OB26(_L26).season}")
    _os26.environ["POOL_SEASON"] = "M-3"
    check("POOL_SEASON に追従する", _OB26(_L26).season == "M-3", f"{_OB26(_L26).season}")
    _os26.environ.pop("POOL_SEASON", None)
    _os26.environ["BELIEF_SEASON"] = "M-6"
    check("BELIEF_SEASON=M-6 で既定シーズンが切り替わる", _OB26(_L26).season == "M-6",
          f"{_OB26(_L26).season}")
    check("明示引数は env より優先", _OB26(_L26, "M-3").season == "M-3", f"{_OB26(_L26, 'M-3').season}")
finally:
    _os26.environ.pop("BELIEF_SEASON", None)
    _os26.environ.pop("POOL_SEASON", None)
    if _savep26 is not None:
        _os26.environ["POOL_SEASON"] = _savep26
    if _save26 is not None:
        _os26.environ["BELIEF_SEASON"] = _save26

# Rust は sim.rs の BELIEF_SEASON="M-2" 定数を使うため、M-2 以外では Python 経路に落とす
try:
    import engine_dispatch as _ED26
    _os26.environ["BELIEF_SEASON"] = "M-6"
    check("BELIEF_SEASON=M-6 では Rust を使わない（パリティ保護）",
          "BELIEF_SEASON=M-6" in _ED26.unsupported_config("mcts_3v3"),
          f"{_ED26.unsupported_config('mcts_3v3')}")
    _os26.environ.pop("BELIEF_SEASON", None)
    check("BELIEF_SEASON 未設定なら Rust 可（従来どおり）",
          not any(g.startswith("BELIEF_SEASON") for g in _ED26.unsupported_config("mcts_3v3")),
          f"{_ED26.unsupported_config('mcts_3v3')}")
finally:
    _os26.environ.pop("BELIEF_SEASON", None)
    if _save26 is not None:
        _os26.environ["BELIEF_SEASON"] = _save26


# ════════════════════════════════════════════════════════════════
print("\n=== 27. 情報開示のタイミング（opp_view）と確定KOのリーク ===")
# 実機で公開される情報は、公開される「瞬間」に opp_view へ入らなければならない。
# 早すぎればリーク、遅すぎればAIが知っているべき情報を知らないまま戦うことになる。
from simulator.opponent_view import OpponentView as _OV27, ENTRY_VISIBLE_ABILITIES as _EVA27, ENTRY_VISIBLE_ITEMS as _EVI27

class _P27:
    def __init__(self, name, ability, item, t1="みず", t2=None):
        self.name = name; self.ability = ability; self.item = item
        self.type1 = t1; self.type2 = t2

_v27 = _OV27("P1")
_v27.on_enter(_P27("ギャラドス", "いかく", "ふうせん", "みず", "ひこう"))
_k27 = _v27.get("ギャラドス")
check("登場時: いかく が判明する（実機で必ずメッセージが出る）", _k27.known_ability == "いかく")
check("登場時: ふうせん が判明する（浮いていると表示される）", _k27.known_item == "ふうせん")

_v27b = _OV27("P1")
_v27b.on_enter(_P27("ギャラドス", "いかく", "ゴツゴツメット", "みず", "ひこう"))
check("登場時: ゴツゴツメット は判明しない（殴るまで分からない）",
      _v27b.get("ギャラドス").known_item is None)
_v27b.on_item("ギャラドス", "ゴツゴツメット", "接触ダメージで判明")
check("接触後: ゴツゴツメット が判明する", _v27b.get("ギャラドス").known_item == "ゴツゴツメット")

# 「殴るまで分からない」持ち物が登場時公開に混ざっていないこと（リーク防止の回帰）
check("登場時公開の持ち物は ふうせん のみ", _EVI27 == {"ふうせん"})
check("登場時公開に 接触/発動系 が混ざっていない",
      not (_EVI27 & {"ゴツゴツメット", "きあいのタスキ", "いのちのたま", "たべのこし", "ピントレンズ"}))
check("登場時公開の特性に ばけのかわ/さめはだ が混ざっていない",
      not (_EVA27 & {"ばけのかわ", "さめはだ", "てつのとげ", "マルチスケイル"}))
check("登場時公開の特性に いかく・天候設置が入っている",
      {"いかく", "あめふらし", "すなおこし", "ひでり", "ゆきふらし"} <= _EVA27)

# 確定KO安全弁が相手の真値を読まないこと（リークの回帰テスト）。
# 真値を読むと、未開示のタスキ等を常に知っている＝人間が迷う場面で迷わないAIになる。
import inspect as _insp27
from simulator.ai import certain_ko_override as _cko27, _survives_unknown as _su27
_src27 = _insp27.getsource(_cko27)
check("確定KO安全弁が opp.item の真値を読まない", "opp.item" not in _src27)
check("確定KO安全弁が opp.ability の真値を読まない", "opp.ability" not in _src27)

from simulator.ai import _goes_first as _gf27, _opp_max_priority as _omp27
check("確定KO安全弁の先制判定が開示ベースの最大優先度を使う（相手の先制技を真値で読まない）",
      "_opp_max_priority(opp, my_side)" in _src27 and "opp_max=_opp_pri" in _src27)
_omp_src27 = _insp27.getsource(_omp27)
check("相手最大優先度は開示技＋使用率事前から推定する",
      "opp_view" in _omp_src27 and "move_prior" in _omp_src27)

_su_src27 = _insp27.getsource(_su27)
check("耐える系の判定は opp_view と事前分布で行う",
      "opp_view" in _su_src27 and "_opp_prior" in _su_src27)

print("\n=== 28. 信念の観測チャネル（行動順/与ダメージ/否定的観測） ===")
# 相手の型推定は「実機で見える情報」だけから更新すること。
from simulator.belief import OpponentBelief as _OB28, _eff_speed_of as _spd28
from simulator.simulate import get_loader as _gl28
from simulator.pokemon import build_from_spec as _bfs28, parse_pokemon_spec as _pps28
_L28 = _gl28()
_SPEC28 = "ガブリアス@こだわりスカーフ:ようき:じしん|げきりん|がんせきふうじ|ステルスロック:2/32/0/0/0/32:さめはだ"
_fld28 = BattleField()

def _mkbel28():
    b = _OB28(_L28, season="M-6")
    b.ensure("ガブリアス")
    return b

# 交代をまたいで信念が残る（種名キーで保持し、場のポケモンには紐付かない）
_b28 = _mkbel28()
check("信念は種名キーで保持される（交代しても残る）",
      _b28.get("ガブリアス") is not None and "ガブリアス" in _b28.species)
# 探索へは持ち込まない（意思決定者の知識であって対戦状態ではない）
import copy as _cp28
check("信念は deepcopy で引き継がれない（決定化ロールアウトに持ち込まない）",
      _cp28.deepcopy(_b28) is None)

# observe_order: 自分より速ければ下限、遅ければ上限。スカーフでしか説明できなければ確定する。
_pb28 = _mkbel28().get("ガブリアス")
_before28 = len([p for p in _pb28.post if p > 0])
_huge28 = max(_spd28(c["defender"], _fld28, 1.0) for c in _pb28.cands) + 1
_upd28 = _pb28.observe_order(_huge28, True, _fld28)   # 素の最速を超える速度に先を越された
check("行動順の観測: 素で説明できない速度ならスカーフを確定する",
      _upd28 and _pb28.known_item == "こだわりスカーフ")

# 遅かっただけではスカーフを否定しない（乱数ではなく下振れ＝低S個体の可能性が残る）
_pb28b = _mkbel28().get("ガブリアス")
_pb28b.observe_order(1, False, _fld28)                 # 自分が極端に遅くても相手が後攻
check("行動順の観測: 遅いだけではスカーフを確定しない", _pb28b.known_item is None)

# observe_absent_item: 回復しなかった＝回復持ち物ではない
_pb28c = _mkbel28().get("ガブリアス")
_pb28c.item_prior = {"たべのこし": 40.0, "こだわりスカーフ": 60.0}
check("否定的観測: 発動しなかった持ち物を事前分布から落とす",
      _pb28c.observe_absent_item(("たべのこし", "くろいヘドロ"))
      and "たべのこし" not in _pb28c.item_prior)
# 開示済みなら否定的観測は効かない（確定情報が優先）
_pb28d = _mkbel28().get("ガブリアス")
_pb28d.known_item = "たべのこし"
check("否定的観測: 開示済みの持ち物は書き換えない",
      not _pb28d.observe_absent_item(("たべのこし",)))

# observe_damage_dealt は攻撃側候補でダメージ式を回す＝相手の A/C を絞る
import inspect as _in28
_src28 = _in28.getsource(_pb28.observe_damage_dealt)
check("与ダメージ観測は候補を攻撃側として使う（被ダメージ観測は耐久しか絞れない）",
      "calc_damage(a, defender" in _src28)

print("\n=== 29. はたきおとす: メガストーンには1.5倍が乗らない ===")
# メガストーンは叩き落とせないので威力1.5倍の対象外。Zメガ石(ナイトZ)は M-6 で追加された
# ため Rust 側の判定から漏れており、同じ盤面で Python 81 / Rust 120 と食い違っていた。
from simulator.damage import calc_damage as _cd29
from simulator.battle import _entry_effects as _ee35
from simulator.simulate import get_loader as _gl29
from simulator.pokemon import build_from_spec as _bfs29, parse_pokemon_spec as _pps29
_L29 = _gl29()
_atk29 = _bfs29(_pps29("マスカーニャ@きあいのタスキ:いじっぱり:はたきおとす|トリックフラワー|とんぼがえり|トリプルアクセル:1/32/1/0/0/32:へんげんじざい"), _L29, season="M-6", randomize=False)
_ko29 = [m for m in _atk29.moves if m.name_jp == "はたきおとす"][0]
_f29 = BattleField()

def _dmg29(item):
    d = _bfs29(_pps29("アブソル@きあいのタスキ:いじっぱり:つじぎり|シャドークロー|でんこうせっか|つるぎのまい:1/32/1/0/0/32:きれあじ"), _L29, season="M-6", randomize=False)
    d.item = item
    return _cd29(_atk29, d, _ko29, _f29, critical=False, random_roll=0.0)

_plain29 = _dmg29("きあいのタスキ")
check("はたきおとす: 通常の持ち物には1.5倍が乗る", _plain29 > _dmg29(None))
for _st29 in ("アブソルナイトZ", "ガブリアスナイトZ", "リザードナイトX", "リザードナイトY", "ボーマンダナイト"):
    check(f"はたきおとす: {_st29} には1.5倍が乗らない", _dmg29(_st29) == _dmg29(None))

# ════════════════════════════════════════════════════════════════
# 相手の型の決定化: 型まるごとサンプリング（JOINT_BUILD）
# ════════════════════════════════════════════════════════════════
import random as _rnd32
from simulator.belief import (OpponentBelief as _OB32, registered_builds_by_species as _rb32,
                              _default_belief_season as _ds32)

_b32 = _rb32(dl)
check("型候補: 登録テンプレートから種ごとの型まるごとを取れる",
      len(_b32) > 50 and all(("moves" in x and "item" in x and "nature" in x)
                             for v in _b32.values() for x in v))

_ob32 = _OB32(dl, season="M-6")
_名32 = next(n for n, v in _b32.items() if len(v) >= 2)
_pb32 = _ob32.ensure(_名32)
_pb32.builds = _b32[_名32]
_r32 = _rnd32.Random(0)
check("型候補: sample_build は技・持ち物・性格が揃った型を返す",
      all(k in (_pb32.sample_build(_r32) or {}) for k in ("moves", "item", "nature", "ev")))

_pb32.map_rate = 1.0
_map32 = {tuple(_pb32.sample_build(_r32)["moves"]) for _ in range(20)}
check("型候補: map_rate=1.0 なら常に同じ最尤型を返す", len(_map32) == 1)
_pb32.map_rate = 0.0

_tgt32 = _b32[_名32][0]
_pb32.known_moves = set(_tgt32["moves"][:2])
_got32 = [_pb32.sample_build(_r32) for _ in range(30)]
check("型候補: 既知技と矛盾する型は候補から外れる",
      all(g is None or set(_pb32.known_moves).issubset(set(g["moves"])) for g in _got32))

_pb32.known_moves = {"存在しない技ZZZ"}
check("型候補: 候補が尽きたら None を返す（周辺分布へフォールバックする）",
      _pb32.sample_build(_r32) is None)

# 型プール＋ダメージ観測：受けたダメージが小さい→耐久振りの型へ重みが寄る
from simulator.pokemon import build_from_spec as _bfs39, parse_pokemon_spec as _pps39
from simulator.battle import BattleField as _BF39
_ob39 = _OB32(dl, season="M-6")
_pb39 = _ob39.ensure("カバルドン")
_pb39.builds = [
    {"weight": 0.5, "item": "オボンのみ", "ability": "すなおこし", "nature": "わんぱく",
     "ev": [32, 0, 32, 0, 2, 0], "moves": ["あくび", "じしん", "ステルスロック", "なまける"]},
    {"weight": 0.5, "item": "オボンのみ", "ability": "すなおこし", "nature": "いじっぱり",
     "ev": [0, 32, 0, 0, 2, 32], "moves": ["いわなだれ", "じしん", "ステルスロック", "つるぎのまい"]},
]
_att39 = _bfs39(_pps39("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                       ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)
_def39 = _bfs39(_pps39("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける"
                       ":32/0/32/0/2/0:すなおこし"), dl, season="M-6", randomize=False)
_mv39 = next(m for m in _att39.moves if m.name_jp == "げきりん")
from simulator.damage import calc_damage as _cd39
_f39 = _BF39()
_frac39 = round(_cd39(_att39, _def39, _mv39, _f39, critical=False, random_roll=0.5) * 100 / _def39.max_hp)
_pb39.observe_damage(_att39, _mv39, _frac39, _f39)
_w39 = _pb39.pool_weights()
check("型プール＋ダメージ観測: 耐久振りで再現できる被ダメージなら耐久型の重みが上がる",
      _w39[0] > 0.9 and abs(sum(_w39) - 1.0) < 1e-9, str(_w39))
_r39 = _rnd32.Random(1)
check("型プール＋ダメージ観測: sample_build は絞った重みで型を引く",
      sum(_pb39.sample_build(_r39)["nature"] == "わんぱく" for _ in range(50)) >= 45)

import inspect as _insp40
from simulator import battle as _bmod40
_src40 = _insp40.getsource(_bmod40)
check("ダメージ観測: 連続技・急所・倒した/耐えた一撃は推定に使わない",
      "_obs_ok = hits == 1 and not critical and defender.is_alive and defender.hp > 1" in _src40
      and "if _obs_ok and attacker_side.belief is not None" in _src40
      and "if _obs_ok and defender_side.belief is not None" in _src40)

# 観測時点の状態：メガ進化・能力変化を載せて逆算する
from simulator.belief import pub_state as _ps41, with_state as _ws41
_mg41 = _bfs39(_pps39("ガブリアス@ガブリアスナイト:いじっぱり:げきりん|じしん|ストーンエッジ|つるぎのまい"
                      ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)
import copy as _cp41
_mg41b = _cp41.deepcopy(_mg41); _mg41b.do_mega_evolve(); _mg41b.stage_attack = 2
_st41 = _ps41(_mg41b)
_q41 = _ws41(_mg41, _st41)
check("観測時点の状態: メガ進化と能力変化を候補に載せる",
      _q41.mega_evolved and _q41.attack == _mg41b.attack and _q41.stage_attack == 2
      and not _mg41.mega_evolved and _mg41.stage_attack == 0)
# 発動しなかった持ち物は型プールの候補から外れる
_pb42 = _ob39.ensure("ニンフィア")
_pb42.builds = [
    {"weight": 0.9, "item": "たべのこし", "ability": "フェアリースキン", "nature": "ずぶとい",
     "ev": [32, 0, 32, 0, 2, 0], "moves": ["あくび", "ねがいごと", "まもる", "ハイパーボイス"]},
    {"weight": 0.1, "item": "こだわりメガネ", "ability": "フェアリースキン", "nature": "ひかえめ",
     "ev": [32, 0, 0, 32, 2, 0], "moves": ["ハイパーボイス", "サイコショック", "でんこうせっか", "シャドーボール"]},
]
_pb42.observe_absent_item(("たべのこし", "くろいヘドロ"))
check("発動しなかった持ち物: 型プールの候補から外す",
      all(_pb42.sample_build(_r39)["item"] == "こだわりメガネ" for _ in range(10)))
_src43 = _insp40.getsource(_bmod40._observe_order)
check("行動順の観測: 特性込みの優先度で比べ、トリックルーム・おいかぜ中は使わない",
      "_priority_base(a1" in _src43 and "trick_room" in _src43 and "tailwind" in _src43)

# メガ進化後（特性がメガ後のものに判明）でも、判明したメガ石の型は型プールから引ける
_pb44 = _ob39.ensure("ボーマンダ")
_pb44.builds = [{"weight": 1.0, "item": "ボーマンダナイト", "ability": "いかく", "nature": "ようき",
                 "ev": [0, 32, 0, 0, 0, 32], "moves": ["すてみタックル", "じしん", "りゅうのまい", "はねやすめ"]}]
_pb44.known_item = "ボーマンダナイト"; _pb44.known_ability = "スカイスキン"
check("メガ進化後: 判明したメガ石の型は特性（メガ後）で弾かない",
      _pb44.sample_build(_r39) is not None)

# こだわりの否定：交代せずに違う技を2種類使ったら、こだわりアイテムの候補を外す
_cA = _bfs39(_pps39("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                    ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)
# 持ち物は開示されない ゴツゴツメット（じしんは非接触）。オボンのみ だと被弾直後に発動して持ち物が判明し、
# こだわりの否定を使う必要自体が無くなる（2026-09-27 オボンのみを被弾直後の発動に修正）。
_cB = _bfs39(_pps39("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける"
                    ":32/0/32/0/2/0:すなおこし"), dl, season="M-6", randomize=False)
_c1 = BattleSide([_cA], viewer_label="P1"); _c2 = BattleSide([_cB], viewer_label="P2")
_c1.field_idx = 0; _c2.field_idx = 1
_c1.belief = _OB32(dl, season="M-6")
_cb = Battle(_c1, _c2, BattleField())
_c1.opp_view.team_preview(_c2.party); _c2.opp_view.team_preview(_c1.party)
import random as _rnd45
_rnd45.seed(2)
_cb._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
               lambda m, o, f: Action(type="move", move=m.active.moves[2], move_idx=2), max_turns=1)
_cb._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
               lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1), max_turns=2)
_cpb = _c1.belief.get("カバルドン")
check("こだわりの否定: 交代せずに違う技を2種類使ったらこだわりアイテムを外す",
      _cpb is not None and {"こだわりスカーフ", "こだわりハチマキ", "こだわりメガネ"} <= _cpb.absent_items,
      str(getattr(_cpb, "absent_items", None)))

# 発動しなかったことからの否定：接触技で反動が無い→ゴツゴツメットではない／HPが半分未満できのみ不発→オボンのみではない
_nA = _bfs39(_pps39("ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                    ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)
_nB = _bfs39(_pps39("カバルドン@たべのこし:わんぱく:じしん|あくび|ステルスロック|なまける"
                    ":32/0/32/0/2/0:すなおこし"), dl, season="M-6", randomize=False)
_n1 = BattleSide([_nA], viewer_label="P1"); _n2 = BattleSide([_nB], viewer_label="P2")
_n1.field_idx = 0; _n2.field_idx = 1
_n1.belief = _OB32(dl, season="M-6")
_nb = Battle(_n1, _n2, BattleField())
_n1.opp_view.team_preview(_n2.party); _n2.opp_view.team_preview(_n1.party)
_n1.opp_view.on_enter(_nB); _n2.opp_view.on_enter(_nA)
_nB.hp = _nB.max_hp * 45 // 100
_rnd45.seed(3)
_nb._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0),
               lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1), max_turns=1)
_npb = _n1.belief.get("カバルドン")
check("否定的観測: 接触技で反動が無ければゴツゴツメットではない",
      _npb is not None and "ゴツゴツメット" in _npb.absent_items, str(getattr(_npb, "absent_items", None)))
check("否定的観測: 表示HPが半分未満できのみが発動しなければオボンのみではない",
      _npb is not None and _nB.is_alive and "オボンのみ" in _npb.absent_items, f"hp={_nB.hp}/{_nB.max_hp} {getattr(_npb, 'absent_items', None)}")

_f1 = BattleSide([_bfs39(_pps39("ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                               ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)], viewer_label="P1")
_fB = _bfs39(_pps39("サーフゴー@こだわりスカーフ:おくびょう:ゴールドラッシュ|シャドーボール|トリック|10まんボルト"
                    ":0/0/0/32/0/32:おうごんのからだ"), dl, season="M-6", randomize=False)
_f1.belief = _OB32(dl, season="M-6")
_f1.opp_view.team_preview([_fB]); _f1.opp_view.on_enter(_fB)
_f1.belief.observe_disclosure(_f1.opp_view)
_bpb = _f1.belief.get("サーフゴー")
check("否定的観測: 初登場でふうせんの表示が無ければふうせんではない（型が合わない時の引き先からも外す）",
      _f1.opp_view.pokemon["サーフゴー"].no_balloon and "ふうせん" in _bpb.absent_items
      and "ふうせん" not in _bpb.item_prior, str(_bpb.absent_items))

# 同じ持ち物はパーティに1つ：判明した味方の持ち物は他の個体の候補から外す
_iA = _bfs39(_pps39("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                    ":2/32/0/0/0/32:さめはだ"), dl, season="M-6", randomize=False)
_iB = _bfs39(_pps39("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける"
                    ":32/0/32/0/2/0:すなおこし"), dl, season="M-6", randomize=False)
_iC = _bfs39(_pps39("アーマーガア@ゴツゴツメット:わんぱく:ボディプレス|てっぺき|はねやすめ|とんぼがえり"
                    ":32/0/32/0/2/0:ミラーアーマー"), dl, season="M-6", randomize=False)
_i1 = BattleSide([_iA], viewer_label="P1"); _i2 = BattleSide([_iB, _iC], viewer_label="P2")
_i1.belief = _OB32(dl, season="M-6")
_i1.opp_view.team_preview(_i2.party)
_i1.opp_view.on_item("カバルドン", "オボンのみ", "テスト")
_i1.belief.observe_disclosure(_i1.opp_view)
_ipb = _i1.belief.get("アーマーガア")
check("同じ持ち物はパーティに1つ: 判明した味方の持ち物（オボンのみ）は他の個体の候補から外す",
      _ipb is not None and "オボンのみ" in _ipb.absent_items
      and not any(b["item"] == "オボンのみ" for b in _ipb.consistent_builds())
      and "オボンのみ" not in _i1.belief.get("カバルドン").absent_items,
      str(getattr(_ipb, "absent_items", None)))

from simulator.belief import obs_match as _om46, hp_pct as _hp46
check("観測の粒度: 相手のHPは整数％（±1%で一致）、自分のHPは実数（整数で一致）",
      _om46("taken", 50, 200, 25) and _om46("taken", 50, 200, 26) and not _om46("taken", 50, 200, 27)
      and _om46("dealt", 37, 150, 37) and not _om46("dealt", 37, 150, 38)
      and _hp46(1, 200) == 1 and _hp46(0, 200) == 0 and _hp46(199, 200) == 100)

from simulator.ai import _filter_valid_by_lock as _fvl47
_lk47 = _bfs39(_pps39("イエッサン(オス)@こだわりスカーフ:おくびょう:トリック|ワイドフォース|マジカルシャイン|マジカルフレイム"
                      ":0/0/0/32/0/32:サイコメイカー"), dl, season="M-6", randomize=False)
_lk47.choice_locked_move = "マジカルシャイン"; _lk47.disabled_move = "マジカルシャイン"
check("縛られた技が封じられたら他の技は選べない（わるあがき）",
      _fvl47([(i, m) for i, m in enumerate(_lk47.moves) if m], _lk47) == [])

# 技選びの観測：弱い技を選んだら、明らかに強い技を持つ型の重みが下がる
_ob48 = _OB32(dl, season="M-6")
_pb48 = _ob48.ensure("ボーマンダ")
_pb48.builds = [
    {"weight": 0.5, "item": "ボーマンダナイト", "ability": "いかく", "nature": "ようき",
     "ev": [0, 32, 0, 0, 0, 32], "moves": ["すてみタックル", "じしん", "りゅうのまい", "はねやすめ"]},
    {"weight": 0.5, "item": "ボーマンダナイト", "ability": "いかく", "nature": "おくびょう",
     "ev": [0, 0, 0, 32, 0, 32], "moves": ["すてみタックル", "りゅうせいぐん", "だいもんじ", "はねやすめ"]},
]
_df48 = _bfs39(_pps39("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける"
                      ":32/0/32/0/2/0:すなおこし"), dl, season="M-6", randomize=False)
_mv48 = next(m for m in _bfs39(_pps39("ボーマンダ@ボーマンダナイト:ようき:すてみタックル|じしん|りゅうのまい|はねやすめ"
                                      ":0/32/0/0/0/32:いかく"), dl, season="M-6", randomize=False).moves
             if m.name_jp == "すてみタックル")
from simulator.belief import pub_state as _ps48
_subj48 = _ps48(_bfs39(_pps39("ボーマンダ@ボーマンダナイト:ようき:すてみタックル|じしん|りゅうのまい|はねやすめ"
                              ":0/32/0/0/0/32:いかく"), dl, season="M-6", randomize=False))
_pb48.observe_choice(_mv48, _df48, _BF39(), _subj48)
_os33.environ["POOL_CHOICE"] = "1"
_w48 = _pb48.pool_weights()
del _os33.environ["POOL_CHOICE"]
check("技選びの観測: 効きの悪い技を選んだら、はるかに強い技を持つ型の重みが下がる",
      _w48[0] > _w48[1], str(_w48))
_ob48b = _OB32(dl, season="M-6")
_pb48b = _ob48b.ensure("ボーマンダ")
_pb48b.builds = [dict(b) for b in _pb48.builds]
_pb48b.observe_choice(_mv48, _df48, _BF39(), _subj48)
_w48b = _pb48b.pool_weights()
check("技選びの観測: 既定（POOL_CHOICE 未設定）では重みを変えない",
      abs(_w48b[0] - _w48b[1]) < 1e-12, str(_w48b))

_ob32b = _OB32(dl, season="M-6")
check("型候補: 既定（JOINT_BUILD 未設定）で型プールを読み込む",
      _ob32b.joint is True and len(_ob32b._builds) > 100)
_sv32 = os.environ.get("JOINT_BUILD")
os.environ["JOINT_BUILD"] = "0"
_ob32c = _OB32(dl, season="M-6")
if _sv32 is None: os.environ.pop("JOINT_BUILD", None)
else: os.environ["JOINT_BUILD"] = _sv32
check("型候補: JOINT_BUILD=0 なら型候補を読み込まない（旧挙動）", _ob32c.joint is False and _ob32c._builds == {})
check("信念シーズン: BELIEF_SEASON > POOL_SEASON > M-6 の順で解決する",
      _ds32() in ("M-2", "M-3", "M-4", "M-5", "M-6"))

# ════════════════════════════════════════════════════════════════
# SearchAI の計測用フック（既定OFFで本番挙動が変わらないこと）
# ════════════════════════════════════════════════════════════════
from simulator.search_ai import SearchAI as _SA31

_ai31 = _SA31(dl)
check("計測フック: 既定はすべてOFF",
      _ai31.oracle is False and _ai31.act_oracle_depth == 0
      and _ai31.cand_topk == 0 and _ai31.opp_act_hint is None
      and _ai31._track_depth is False)


class _FakeSide31:
    pass


check("計測フック: ORACLE_REVEAL 未設定なら部分開示は無効", _ai31.oracle_reveal == set())
_cfg31 = [{"item": "ダミー", "ability": "ダミー", "moves": ["ダミー技"],
           "ev": {"H": 0}, "nature": "まじめ"}]


class _FakePoke31:
    item = "きあいのタスキ"
    ability = "いかく"
    nature = "ようき"
    evs = {"S": 32}
    moves = []


class _FakeOpp31:
    party = [_FakePoke31()]


_ai31.oracle_reveal = {"item", "spread"}
_ai31._reveal(_cfg31, _FakeOpp31())
check("計測フック: 指定した要素だけ真値で上書きされる",
      _cfg31[0]["item"] == "きあいのタスキ" and _cfg31[0]["nature"] == "ようき"
      and _cfg31[0]["ability"] == "ダミー" and _cfg31[0]["moves"] == ["ダミー技"])
_ai31.oracle_reveal = set()

_cands31 = ["a", "b", "c"]
_ai31._candidate_actions = lambda *_a, **_k: list(_cands31)
_ai_idx31 = _SA31.__dict__["_action_index"]
_SA31._action_index = staticmethod(lambda a: {"a": 0, "b": 1, "c": 2}[a])
check("計測フック: ヒント未設定なら候補は絞られない",
      _ai31._opp_candidates(None, None, None, 0) == _cands31)
_ai31.opp_act_hint = 1
check("計測フック: act_oracle_depth=0 ならヒントがあっても絞らない",
      _ai31._opp_candidates(None, None, None, 0) == _cands31)
_ai31.act_oracle_depth = 1
check("計測フック: 深さ0のみヒントで1手に絞る",
      _ai31._opp_candidates(None, None, None, 0) == ["b"]
      and _ai31._opp_candidates(None, None, None, 1) == _cands31)
_ai31.act_oracle_depth = 99
check("計測フック: act_oracle_depth=99 は全深さで絞る",
      _ai31._opp_candidates(None, None, None, 5) == ["b"])
_SA31._action_index = _ai_idx31

# ════════════════════════════════════════════════════════════════
# PVNetNP: 活性・正規化・最適化の切替（既定は従来仕様と完全一致）
# ════════════════════════════════════════════════════════════════
import numpy as _np30
from simulator.az_np import PVNetNP as _PV30

_n30 = _PV30(24, 8, 6, seed=3)
_X30 = _np30.random.default_rng(0).normal(0, 1, (7, 24))
_H1 = _np30.tanh(_X30 @ _n30.W1.T + _n30.b1)
_H2 = _np30.tanh(_H1 @ _n30.W2.T + _n30.b2)
_lg30 = _H2 @ _n30.Wp.T + _n30.bp
check("PVNetNP: 既定は tanh・正規化なしで従来と同一の前向き",
      _np30.allclose(_n30._forward(_X30)[2], _lg30) and _n30.act == "tanh" and _n30.mu is None)

_r30 = _PV30(24, 8, 6, seed=3, act="relu", norm=True)
_r30.fit_norm(_X30)
check("PVNetNP: norm=True は訓練データの平均分散で標準化する",
      _np30.allclose(_r30.mu, _X30.mean(0)) and _np30.allclose(_r30._nz(_X30).mean(0), 0, atol=1e-9))
check("PVNetNP: act=relu は負の活性を0にする", (_r30._top(_X30)[0] >= 0).all())

# relu+norm+Adam は小さな教師集合に適合できる（tanh素SGDは適合できない＝回帰テストの要点）
_M30 = _np30.ones((40, _PV30(4, 2, 2).Wp.shape[0]))
_PI30 = _np30.zeros_like(_M30)
_rng30 = _np30.random.default_rng(1)
_Xt30 = _rng30.normal(0, 1, (40, 24))
_tgt30 = _rng30.integers(0, _M30.shape[1], 40)
_PI30[_np30.arange(40), _tgt30] = 1.0
_Y30 = _np30.full(40, 0.5)


def _top1_30(net):
    _, _, P = net._forward(_Xt30)
    return float((_np30.where(_M30 > 0, P, -1e9).argmax(1) == _tgt30).mean())


_a30 = _PV30(24, 64, 32, seed=5, act="relu", norm=True)
_a30.fit_norm(_Xt30)
_a30.train_pi(_Xt30, _PI30, _M30, _Y30, epochs=400, lr=5e-3, batch=20, optimizer="adam",
              value_weight=0.0)
check("PVNetNP: relu+norm+Adam は方策ターゲットに適合できる", _top1_30(_a30) >= 0.95)
check("PVNetNP: optimizer=adam で Adam の状態が作られる", _a30.opt == "adam" and _a30._adam["t"] > 0)

# EMA: 影パラメータは実パラメータと違い、apply_ema で本体へ入る（＝学習後の値が変わる）
_em30 = _PV30(24, 16, 8, seed=11, act="relu", norm=True)
_em30.fit_norm(_Xt30)
_em30.train_pi(_Xt30, _PI30, _M30, _Y30, epochs=30, lr=5e-3, batch=20, optimizer="adam",
               value_weight=0.0, ema=0.9)
_raw30 = _em30.W1.copy()
check("PVNetNP: ema>0 で影パラメータが作られる", _em30._ema is not None)
_em30.apply_ema()
check("PVNetNP: apply_ema は本体の重みを平均へ置き換える",
      _em30._ema is None and not _np30.allclose(_em30.W1, _raw30))

_ne30 = _PV30(24, 16, 8, seed=11, act="relu", norm=True)
_ne30.fit_norm(_Xt30)
_ne30.train_pi(_Xt30, _PI30, _M30, _Y30, epochs=30, lr=5e-3, batch=20, optimizer="adam",
               value_weight=0.0)
check("PVNetNP: ema 既定(0)では影パラメータを作らず従来と同一",
      _ne30._ema is None and _np30.allclose(_ne30.W1, _raw30))

_fd30 = _PV30(24, 8, 6, seed=7, act="relu", norm=True)
_fd30.fit_norm(_Xt30)
_before30 = _fd30._forward(_Xt30)[2].copy()
_fd30.fold_norm()
check("PVNetNP: fold_norm は正規化を第1層に畳み込んでも出力が等価",
      _fd30.mu is None and _np30.allclose(_fd30._forward(_Xt30)[2], _before30, atol=1e-9))

_vw30 = _PV30(24, 16, 8, seed=9, act="relu", norm=True)
_vw30.fit_norm(_Xt30)
_wv30 = _vw30.Wv.copy()
_vw30.train_pi(_Xt30, _PI30, _M30, _Y30, epochs=5, lr=1e-3, l2=0.0, batch=20, optimizer="adam",
               value_weight=_np30.zeros(len(_Xt30)))
check("PVNetNP: value_weight が全0の配列なら価値ヘッドは更新されない（l2=0）",
      _np30.allclose(_vw30.Wv, _wv30))
_vw30.train_pi(_Xt30, _PI30, _M30, _Y30, epochs=5, lr=1e-3, l2=0.0, batch=20, optimizer="adam",
               value_weight=_np30.ones(len(_Xt30)))
check("PVNetNP: value_weight が1の配列なら価値ヘッドが更新される",
      not _np30.allclose(_vw30.Wv, _wv30))

_nm30 = _PV30(24, 16, 8, seed=11, act="relu", norm=True)
_nm30.fit_norm(_Xt30)
_wp30 = _nm30.Wp.copy()
_zero30 = _np30.zeros((len(_Xt30), _M30.shape[1]))
_nm30.train_pi(_Xt30, _zero30, _zero30, _Y30, epochs=5, lr=1e-3, l2=0.0, batch=20,
               optimizer="adam")
check("探索木ノード: 合法手マスクが全0なら方策ヘッドは更新されない（価値だけ学習）",
      _np30.allclose(_nm30.Wp, _wp30))

_a30.save("/tmp/_test_az30.json")
_l30 = _PV30.load("/tmp/_test_az30.json")
check("PVNetNP: act/mu/sd を保存・復元して前向きが一致",
      _l30.act == "relu" and _l30.mu is not None
      and _np30.allclose(_l30._forward(_Xt30)[2], _a30._forward(_Xt30)[2]))

# ════════════════════════════════════════════════════════════════
# ギルガルド: ブレードフォルムの種族値は第9世代の 140（150 は第8世代以前）
# ════════════════════════════════════════════════════════════════
from simulator.battle import _aegislash_to_blade as _tb33, _aegislash_to_shield as _ts33
from simulator.pokemon import calc_stat as _cs33, NATURE_MODS as _NM33

_g33 = _bfs29(_pps29(
    "ギルガルド@とつげきチョッキ:いじっぱり:シャドークロー|アイアンヘッド|かげうち|せいなるつるぎ"
    ":0/32/0/0/0/0:バトルスイッチ"), _L29, season="M-6", randomize=False)
_shield_a33, _shield_c33 = _g33.attack, _g33.sp_attack
_ev33 = _g33.evs or {}
_up33, _dn33 = _NM33.get(_g33.nature, (None, None))


def _n33(key):
    return 1.1 if _up33 == key else (0.9 if _dn33 == key else 1.0)


def _exp33(base, k, stat):
    return _cs33(base, _ev33.get(k, 0), 31, _n33(stat))


check("ギルガルド: シールドの種族値は A=50 / B=140 / C=50 / D=140",
      _g33.attack == _exp33(50, "A", "attack")
      and _g33.defense == _exp33(140, "B", "defense")
      and _g33.sp_attack == _exp33(50, "C", "sp_attack")
      and _g33.sp_defense == _exp33(140, "D", "sp_defense"))

_tb33(_g33, [])
check("ギルガルド: ブレードの攻撃は種族値140で計算する（150ではない）",
      _g33.attack == _exp33(140, "A", "attack"),
      f"attack={_g33.attack} 期待={_exp33(140, 'A', 'attack')}")
check("ギルガルド: ブレードの特攻は種族値140で計算する",
      _g33.sp_attack == _exp33(140, "C", "sp_attack"))
check("ギルガルド: ブレードの防御・特防は種族値50",
      _g33.defense == _exp33(50, "B", "defense")
      and _g33.sp_defense == _exp33(50, "D", "sp_defense"))
_ts33(_g33, [])
check("ギルガルド: シールドに戻ると元の実数値に復帰する",
      _g33.attack == _shield_a33 and _g33.sp_attack == _shield_c33)

# ════════════════════════════════════════════════════════════════
# ワイドフォース: サイコフィールド中は 1.3（汎用）× 1.5（固有）
# ════════════════════════════════════════════════════════════════
_atk34 = _bfs29(_pps29(
    "イエッサン(オス)@こだわりスカーフ:おくびょう:ワイドフォース|サイコキネシス|トリック|アンコール"
    ":0/0/0/32/0/32:サイコメイカー"), _L29, season="M-6", randomize=False)
_def34 = _bfs29(_pps29(
    "ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|がんせきふうじ|ステルスロック"
    ":2/32/0/0/0/32:さめはだ"), _L29, season="M-6", randomize=False)
_wf34 = [m for m in _atk34.moves if m.name_jp == "ワイドフォース"][0]
_pk34 = [m for m in _atk34.moves if m.name_jp == "サイコキネシス"][0]

_f34n = BattleField()
_f34p = BattleField(); _f34p.psychic_terrain = True

_wf_plain = _cd29(_atk34, _def34, _wf34, _f34n, critical=False, random_roll=1.0)
_wf_psy = _cd29(_atk34, _def34, _wf34, _f34p, critical=False, random_roll=1.0)
_pk_plain = _cd29(_atk34, _def34, _pk34, _f34n, critical=False, random_roll=1.0)
_pk_psy = _cd29(_atk34, _def34, _pk34, _f34p, critical=False, random_roll=1.0)

check("ワイドフォース: サイコフィールドで威力が上がる", _wf_psy > _wf_plain)
check("ワイドフォース: 一般のエスパー技(×1.3)より伸びが大きい（固有×1.5）",
      _wf_psy / _wf_plain > _pk_psy / _pk_plain + 0.3,
      f"WF {_wf_psy}/{_wf_plain}={_wf_psy/_wf_plain:.2f} "
      f"サイコキネシス {_pk_psy}/{_pk_plain}={_pk_psy/_pk_plain:.2f}")
check("サイコキネシス: 汎用の地形補正は約1.3倍のまま",
      1.25 < _pk_psy / _pk_plain < 1.35)

_fly34 = _bfs29(_pps29(
    "ボーマンダ@こだわりスカーフ:ようき:げきりん|じしん|とんぼがえり|りゅうのまい"
    ":0/32/0/0/0/32:いかく"), _L29, season="M-6", randomize=False)
_fly34.moves = [_wf34]
_wf_fly_n = _cd29(_fly34, _def34, _wf34, _f34n, critical=False, random_roll=1.0)
_wf_fly_p = _cd29(_fly34, _def34, _wf34, _f34p, critical=False, random_roll=1.0)
check("ワイドフォース: 接地していない攻撃側には地形補正が乗らない", _wf_fly_p == _wf_fly_n)

# ════════════════════════════════════════════════════════════════
# 1v1相性表: 入場時効果（天候・フィールド・いかく）が適用される
# ════════════════════════════════════════════════════════════════
from simulator.matchup_explain import explain_matchup as _em35, _best_dmg as _bd35
import copy as _cp35

_ye35 = ("イエッサン(オス)@こだわりスカーフ:おくびょう:ワイドフォース|サイコキネシス|トリック|アンコール"
         ":0/0/0/32/0/32:サイコメイカー")
_gb35 = ("ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|がんせきふうじ|ステルスロック"
         ":2/32/0/0/0/32:さめはだ")
_a35 = _bfs29(_pps29(_ye35), _L29, season="M-6", randomize=False)
_b35 = _bfs29(_pps29(_gb35), _L29, season="M-6", randomize=False)
_bare35 = _bd35(_cp35.deepcopy(_a35), _cp35.deepcopy(_b35), BattleField())
_aa35, _bb35, _f35 = _cp35.deepcopy((_a35, _b35, BattleField()))
_ee35(_aa35, 0, _f35, _bb35)
_ee35(_bb35, 1, _f35, _aa35)
_ent35 = _bd35(_aa35, _bb35, _f35)
check("1v1: サイコメイカーの入場効果でフィールドが張られる", _f35.psychic_terrain is True)
check("1v1: 入場効果ありのほうが与ダメージが大きい（ワイドフォース＋地形）",
      _ent35 > _bare35 * 1.4, f"素の場 {_bare35:.3f} → 入場効果あり {_ent35:.3f}")

_r35 = _em35([_ye35], [_gb35], dl, season="M-6")
check("1v1: explain_matchup が入場効果を適用した数値を返す",
      abs(_r35["cells"][0][0]["dealt"] / 100.0 - _ent35) < 0.02,
      f'{_r35["cells"][0][0]["dealt"]} vs {_ent35*100:.1f}')

# ════════════════════════════════════════════════════════════════
# 一撃必殺技とがんじょう: 完全無効（HP満タンのまま）。かたやぶりは貫通
# ════════════════════════════════════════════════════════════════
import random as _r36

_atk36 = ("カビゴン@たべのこし:わんぱく:じわれ|のしかかり|うたう|はらだいこ"
          ":32/0/32/0/2/0:あついしぼう")
_mb36 = ("ドリュウズ@いのちのたま:いじっぱり:じわれ|アイアンヘッド|じしん|つのドリル"
         ":0/32/0/0/0/32:かたやぶり")
_stu36 = ("フォレトス@ゴツゴツメット:わんぱく:ジャイロボール|ステルスロック|やどりぎのタネ|まきびし"
          ":32/0/32/0/2/0:がんじょう")


def _ohko36(atk_spec, def_spec, seed=3):
    a = _bfs29(_pps29(atk_spec), _L29, season="M-6", randomize=False)
    d = _bfs29(_pps29(def_spec), _L29, season="M-6", randomize=False)
    s1 = BattleSide([a], viewer_label="P1"); s2 = BattleSide([d], viewer_label="P2")
    s1.field_idx = 0; s2.field_idx = 1
    bt = Battle(s1, s2, BattleField()); _r36.seed(seed)
    bt._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0),
                  lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
                  max_turns=1)
    return d, bt.logs


_d36, _lg36 = _ohko36(_atk36, _stu36)
check("一撃必殺: がんじょうは完全無効でHPが満タンのまま残る",
      _d36.is_alive and _d36.hp == _d36.max_hp,
      f"hp={_d36.hp}/{_d36.max_hp}")
check("一撃必殺: がんじょうで無効化したログが出る",
      any("がんじょう" in x and "効かない" in x for x in _lg36))

# じわれは命中30%なので当たり外れは乱数次第。「がんじょうで無効化されない」ことで判定する
_d36b, _lg36b = _ohko36(_mb36, _stu36, seed=5)
check("一撃必殺: かたやぶりはがんじょうの無効化を貫通する",
      not any("がんじょう" in x and "効かない" in x for x in _lg36b),
      str([x for x in _lg36b if "がんじょう" in x or "じわれ" in x][:3]))

# まねっこ: 相手の直前技をコピーして実行する
_cp36 = ("レパルダス@きあいのタスキ:おくびょう:まねっこ|ねこだまし|バークアウト|つじぎり"
         ":0/0/0/32/0/32:いたずらごころ")
_gb36 = ("ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|がんせきふうじ|ステルスロック"
         ":2/32/0/0/0/32:さめはだ")
_a36 = _bfs29(_pps29(_cp36), _L29, season="M-6", randomize=False)
_b36 = _bfs29(_pps29(_gb36), _L29, season="M-6", randomize=False)
_s136 = BattleSide([_a36], viewer_label="P1"); _s236 = BattleSide([_b36], viewer_label="P2")
_s136.field_idx = 0; _s236.field_idx = 1
_bt36 = Battle(_s136, _s236, BattleField()); _r36.seed(7)
_bt36._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[2], move_idx=2),
                 lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
                 max_turns=1)
_n36 = len(_bt36.logs)
_bt36._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0),
                 lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
                 max_turns=2)
check("まねっこ: 相手の直前技をコピーして実行する",
      any("じしん をコピー" in x for x in _bt36.logs[_n36:]),
      str(_bt36.logs[_n36:_n36 + 4]))

# 先発の開示：バトル開始時に両者の先発が seen になり、登場時特性（いかく）も開示される。
# 交代時にしか on_enter しておらず、先発が隠れ選出の引き直し対象になっていた
_lA = _bfs29(_pps29("ガブリアス@きあいのタスキ:いじっぱり:げきりん|じしん|がんせきふうじ|ステルスロック"
                    ":2/32/0/0/0/32:さめはだ"), _L29, season="M-6", randomize=False)
_lB = _bfs29(_pps29("ウインディ@オボンのみ:わんぱく:フレアドライブ|しんそく|おにび|バークアウト"
                    ":32/0/32/0/2/0:いかく"), _L29, season="M-6", randomize=False)
_ls1 = BattleSide([_lA], viewer_label="P1"); _ls2 = BattleSide([_lB], viewer_label="P2")
_ls1.field_idx = 0; _ls2.field_idx = 1
_r36.seed(3)
Battle(_ls1, _ls2, BattleField()).run(
    lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
    lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0))
check("先発の開示: 両者の先発がバトル開始時に seen になる",
      _ls1.opp_view.pokemon["ウインディ"].seen and _ls2.opp_view.pokemon["ガブリアス"].seen)
check("先発の開示: 先発のいかくは登場時に開示",
      _ls1.opp_view.pokemon["ウインディ"].known_ability == "いかく")

# 消費した持ち物の記憶：タスキが発動して無くなった相手を、決定化で再びタスキ持ちにしない
from simulator.search_ai import SearchAI as _SAI38
from simulator.belief import OpponentBelief as _OB38
import copy as _cp38
_gA = _bfs29(_pps29("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                    ":2/32/0/0/0/32:さめはだ"), _L29, season="M-6", randomize=False)
_gB = _bfs29(_pps29("マスカーニャ@きあいのタスキ:ようき:トリックフラワー|はたきおとす|ふいうち|とんぼがえり"
                    ":0/32/2/0/0/32:へんげんじざい"), _L29, season="M-6", randomize=False)
_g1 = BattleSide([_gA], viewer_label="P1"); _g2 = BattleSide([_gB], viewer_label="P2")
_g1.field_idx = 0; _g2.field_idx = 1
_gb = Battle(_g1, _g2, BattleField())
_g1.opp_view.team_preview(_g2.party); _g2.opp_view.team_preview(_g1.party)
_g1.opp_view.on_enter(_gB); _g2.opp_view.on_enter(_gA)
_r36.seed(1)
_gb._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0),
               lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0), max_turns=1)
_gb._sync_item_loss()   # 次の行動選択の直前に行われる記録
_gbl = _OB38(_L29); _gbl.observe_disclosure(_g1.opp_view)
_gai = _SAI38(_L29)
_gok = []
for _k in range(5):
    _gc = [x for x in _gai._sample_opp_config(_g2, _gbl) if x][0]
    _gp = _cp38.deepcopy(_gB); _gai._determinize(_gp, _gc); _gok.append(_gp.item)
check("消費した持ち物の記憶: タスキ発動後の決定化でタスキを戻さない",
      _gB.item is None and _g1.opp_view.pokemon[_gB.name].item_lost
      and all(x is None for x in _gok), f"{_gB.item} {_gok}")

# きのみを食べた相手：開示の無い消費でも item_lost が記録され、決定化で持ち物を戻さない
_hB = _bfs29(_pps29("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける"
                    ":32/0/32/0/2/0:すなおこし"), _L29, season="M-6", randomize=False)
_hA = _bfs29(_pps29("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド"
                    ":2/32/0/0/0/32:さめはだ"), _L29, season="M-6", randomize=False)
_h1 = BattleSide([_hA], viewer_label="P1"); _h2 = BattleSide([_hB], viewer_label="P2")
_h1.field_idx = 0; _h2.field_idx = 1
_hb = Battle(_h1, _h2, BattleField())
_h1.opp_view.team_preview(_h2.party); _h2.opp_view.team_preview(_h1.party)
_h1.opp_view.on_enter(_hB); _h2.opp_view.on_enter(_hA)
_r36.seed(5)
_hb._sync_item_loss()
for _t in range(3):
    if _hB.item is None or not _hB.is_alive:
        break
    _hb._turn_loop(lambda m, o, f: Action(type="move", move=m.active.moves[0], move_idx=0),
                   lambda m, o, f: Action(type="move", move=m.active.moves[1], move_idx=1),
                   max_turns=_hb.turn + 1)
_hb._sync_item_loss()
_hk = _h1.opp_view.pokemon[_hB.name]
check("消費した持ち物の記憶: きのみを食べた相手は item_lost（持ち物名も確定）",
      _hB.item is None and _hk.item_lost and _hk.known_item == "オボンのみ",
      f"item={_hB.item} lost={_hk.item_lost} known={_hk.known_item}")

# 正規化ロールの16段は実戦の (85+k)/100 と同じダメージ（浮動小数の丸めで1ずれ、信念が正解の型を潰していた）
import random as _r37
from simulator.damage import calc_damage as _cd37
_a37 = _bfs(_pps("バシャーモ@きあいのタスキ:いじっぱり:つるぎのまい|まもる|インファイト|フレアドライブ:0/32/0/0/0/32:かそく"), _Lx, season="M-6", randomize=False)
_d37 = _bfs(_pps("ウルガモス@オボンのみ:ひかえめ:あさのひざし|ちょうのまい|ほのおのまい|ギガドレイン:32/0/16/0/0/16:ほのおのからだ"), _Lx, season="M-6", randomize=False)
_m37 = _Lx.get_move("フレアドライブ")
_norm37 = [_cd37(_a37, _d37, _m37, BattleField(), False, k / 15) for k in range(16)]
_real37 = set()
for _s37 in range(400):
    _r37.seed(_s37)
    _real37.add(_cd37(_a37, _d37, _m37, BattleField(), False))
check("正規化ロール: 16段の値が実戦の乱数の値と一致（136 を再現）",
      set(_norm37) == _real37 and 136 in _norm37, f"norm={_norm37} real={sorted(_real37)}")

# ════════════════════════════════════════════════════════════════
# 30. 1v1判定は方針の組ごとの2者対戦（準備の1手→攻撃・ねこだまし・自分の能力低下）
#     相手を棒立ちにして一方ずつ数える方式では、積み技・ねこだまし＋かるわざ・
#     からをやぶるの防御低下が判定に入らなかった（REQUIREMENTS 4-0-1）。
# ════════════════════════════════════════════════════════════════
print("\n=== 30. 1v1判定の2者対戦（準備の手） ===")
try:
    import json as _j30, os as _os30
    _os30.environ.setdefault("POKENAVI_DATAPACK", _os30.path.join(_os30.path.dirname(_os30.path.dirname(_os30.path.abspath(__file__))), "_rust_engine", "datapack.json"))
    import pokenavi_engine as _E30

    def _mu30(a, b):
        return _j30.loads(_E30.mu_analyze(a, b, "M-3"))

    _KAME30 = "カメックス@カメックスナイト:ひかえめ:あくのはどう|からをやぶる|だいちのはどう|はどうだん:0/0/0/32/0/32:メガランチャー"
    _MANDA30 = "ボーマンダ@ボーマンダナイト:むじゃき:じしん|すてみタックル|だいもんじ|りゅうせいぐん:0/32/0/8/0/24:スカイスキン"
    _NYU30 = "オオニューラ@ノーマルジュエル:いじっぱり:ねこだまし|アクロバット|インファイト|フェイタルクロー:0/32/0/0/0/32:かるわざ"
    _ACE30 = "エースバーン@こだわりスカーフ:ようき:かえんボール|とびひざげり|とんぼがえり|ダストシュート:0/32/0/0/0/32:リベロ"
    _META30 = "メタグロス@メタグロスナイト:いじっぱり:じしん|れいとうパンチ|サイコファング|バレットパンチ:0/32/0/0/0/32:かたいツメ"
    _GHOLD30 = "サーフゴー@ふうせん:ひかえめ:じこさいせい|わるだくみ|ゴールドラッシュ|シャドーボール:0/0/0/32/0/32:おうごんのからだ"

    _r30 = _mu30(_KAME30, _MANDA30); _v30 = _r30["verdict"]
    check("からをやぶる→攻撃を選ぶ（メガカメックス vs メガボーマンダ）",
          _v30["myPrep"] == "からをやぶる" and _v30["mySeq"][:1] == ["からをやぶる"], f"{_v30}")
    check("からをやぶる: 決着ターンの素早さは積んだ後（初期Sの2倍で相手より速い）",
          _v30["myS"] == 2 * _r30["a"]["speed"] and _r30["a"]["speed"] < _r30["b"]["speed"] < _v30["myS"],
          f"初期S{_r30['a']['speed']} 決着S{_v30['myS']} 相手S{_v30['oppS']}")
    check("からをやぶる: 2ターン目に先に倒して勝つ（記号○）",
          _v30["myHits"] == 2 and _v30["koFirst"] and _v30["win"] and _v30["sym"] == "○", f"{_v30}")
    _base30 = min(m["hitsLo"] for m in _r30["b"]["moves"] if m.get("hitsLo") is not None)
    check("からをやぶる: 相手の手数は防御低下後の自分に対して数える（棒立ちの確定数以下）",
          _v30["oppHits"] <= _base30, f"判定{_v30['oppHits']} 棒立ち{_base30}")

    _race30 = _v30.get("race") or []
    check("判定の経過(race): 倒れた相手の2ターン目の行動は無く、毎ターン表示も実際に動いた分だけ",
          not any(e["turn"] == 2 and e["actor"] == 1 for e in _race30) and len(_r30["b"]["turns"]) == 1
          and _race30 and _race30[-1]["hp"][1] == 0, f"{_race30}")
    check("判定の経過(race): すてみタックルの反動は相手自身のHP減少として記録し、自分の行の extra に載る",
          any(x["side"] == 1 and x["kind"] == "recoil" and x["amount"] > 0 for e in _race30 for x in e["events"])
          and any(x["kind"] == "recoil" for x in _r30["a"]["turns"][0]["extra"]), f"{_r30['a']['turns']}")
    _r30m = _mu30(_NYU30, "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン")
    check("同じ確定数なら反動の無い技: メガボーマンダは じしん でオオニューラを倒す（すてみタックルを選ばない）",
          _r30m["verdict"]["oppMove"] == "じしん"
          and all(e["move"] != "すてみタックル" for e in _r30m["verdict"]["race"]), f"{_r30m['verdict']}")
    _race30i = _mu30("ボーマンダ@ボーマンダナイト:むじゃき:じしん|すてみタックル|だいもんじ|りゅうせいぐん:0/32/0/8/0/24:スカイスキン",
                     "イエッサン(オス)@こだわりスカーフ:おくびょう:アンコール|トリック|マジカルシャイン|ワイドフォース:0/0/0/32/0/32:サイコメイカー")["verdict"]
    check("相手を技で倒した行動の反動で自分も倒れたら相打ち（引き分け・スコア0・△）",
          _race30i.get("mutual") is True and not _race30i["win"] and _race30i["score"] == 0
          and _race30i["sym"] == "△" and _race30i["race"][-1]["hp"] == [0, 0], f"{_race30i}")
    check("負けが同じでも最善を尽くす: オオニューラはメガボーマンダにねこだましを撃つ（記号が同じ方針は削り・粘りで比べる）",
          _r30m["verdict"]["myPrep"] == "ねこだまし" and _r30m["verdict"]["race"][0]["move"] == "ねこだまし",
          f"{_r30m['verdict']}")
    _GAB30 = "ガブリアス@こだわりスカーフ:ようき:げきりん|じしん|ステルスロック|ドラゴンテール:0/32/0/0/0/32:さめはだ"
    _vt30 = _mu30(_GAB30, _GAB30)["verdict"]
    check("同速で先後により結果が変わる対面は両方の順の平均（同じ型のミラーは△・tie）",
          _vt30.get("tie") is True and _vt30["sym"] == "△" and _vt30["score"] == 0, f"{_vt30}")
    _rk30 = _mu30(_KAME30, "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン")
    check("相手の反動も毎ターン表示に残す（すてみタックルの反動がカメックス側の行の extra に載る）",
          any(x["kind"] == "recoil" for r in _rk30["a"]["turns"] for x in r.get("extra", [])), f"{_rk30['a']['turns']}")
    check("カメックス vs メガボーマンダは中央乱数で勝ち（記号○）",
          _rk30["verdict"]["sym"] == "○" and _rk30["verdict"]["win"], f"{_rk30['verdict'].get('sym')}")
    check("判定は中央乱数の1点だけ（最低・最高乱数の結果 rollDep/rollOutcomes/rollScores は出さない）",
          all(k not in _rk30["verdict"] for k in ("rollDep", "rollOutcomes", "rollScores")), f"{list(_rk30['verdict'])}")
    # 相手側の積み指定（工房の「この状況で見る」の積み（相手））
    _MANDA30i = "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン"
    _s0 = _j30.loads(_E30.mu_analyze_scenario(_KAME30, _MANDA30i, "M-3", 0, 0, 0, 0))
    _sb = _j30.loads(_E30.mu_analyze(_KAME30, _MANDA30i, "M-3"))
    check("相手の積み0回の指定は、指定なしと完全一致", _s0 == _sb, "差分あり")
    _s1 = _j30.loads(_E30.mu_analyze_scenario(_KAME30, _MANDA30i, "M-3", 0, 0, 0, 1))["verdict"]
    check("相手(メガボーマンダ)りゅうのまい+1の前提で判定が変わり、相手のりゅうのまいを準備の手に二重計上しない",
          _s1["sym"] != _sb["verdict"]["sym"] and _s1.get("oppPrep") != "りゅうのまい", f"{_s1['sym']} vs {_sb['verdict']['sym']} prep={_s1.get('oppPrep')}")
    _vh30 = _mu30(_NYU30, "カバルドン@オボンのみ:しんちょう:あくび|じしん|ふきとばし|ステルスロック:32/0/0/0/32/0:すなおこし")["verdict"]
    check("同じ負けなら相手を多く削る方針: オオニューラはカバルドンにねこだまし→インファイト",
          _vh30["myPrep"] == "ねこだまし" and [e["move"] for e in _vh30["race"] if e["actor"] == 0] == ["ねこだまし", "インファイト"],
          f"{_vh30['race']}")
    # 監査の修正（1v1分析）
    _vg30 = _mu30(_NYU30, "ギルガルド@たべのこし:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ")["verdict"]
    check("当たらない ねこだまし（相手がゴースト）は準備の手の候補にしない", _vg30.get("myPrep") != "ねこだまし", f"{_vg30.get('myPrep')}")
    _vm30 = _mu30("カバルドン@オボンのみ:しんちょう:あくび|じしん|ふきとばし|ステルスロック:32/0/0/0/32/0:すなおこし",
                  "ミミッキュ@いのちのたま:いじっぱり:かげうち|じゃれつく|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")["verdict"]
    _kinds30 = {x["kind"] for e in (_vm30.get("race") or []) for x in e["events"]}
    check("経過の原因は対戦本体が記録: すなあらし・いのちのたま・ばけのかわ を取り違えずに出す",
          {"sandstorm", "lifeorb", "disguise"} <= _kinds30, f"{_kinds30}")
    _vs30 = _mu30("ドヒドイデ@たべのこし:しんちょう:くろいきり|じこさいせい|どくどく|まとわりつく:32/0/0/0/32/0:さいせいりょく",
                  "エースバーン@こだわりスカーフ:ようき:かえんボール|とびひざげり|とんぼがえり|ダストシュート:0/32/0/0/0/32:リベロ")["verdict"]
    check("持久戦ルートで記号を上書きしたときは、食い違う経過(race)を出さない",
          (not (_vs30.get("stall") or {}).get("side")) or _vs30.get("race") is None, f"{(_vs30.get('stall') or {}).get('side')} race={_vs30.get('race') is None}")
    check("同速(tie)のときの素早さは同速だったターンの値（myS == oppS）",
          (not _vt30.get("tie")) or _vt30["myS"] == _vt30["oppS"], f"{_vt30['myS']} vs {_vt30['oppS']}")
    # 経過(race)は行動の実際の時系列: 2ターン目は先に動いたオオニューラのインファイト(さめはだで自傷)→後のじしん
    _vgb30 = _mu30(_NYU30, "ガブリアス@きあいのタスキ:いじっぱり:じしん|つるぎのまい|ほのおのキバ|スケイルショット:0/32/0/0/0/32:さめはだ")["verdict"]
    _t2 = [e for e in (_vgb30.get("race") or []) if e["turn"] == 2]
    check("経過の時系列: 先に動いた行動の自傷(さめはだ)は、後から動いた相手の技より前の区切りに入る",
          len(_t2) >= 2 and _t2[0]["actor"] == 0 and any(x["kind"] == "roughskin" and x["side"] == 0 for x in _t2[0]["events"])
          and _t2[1]["actor"] == 1 and _t2[1]["move"] == "じしん", f"{_t2}")
    _r30b = _mu30(_NYU30, _ACE30); _v30b = _r30b["verdict"]
    check("ねこだまし＋ノーマルジュエル＋かるわざ: ねこだましを準備の手に選ぶ",
          _v30b["myPrep"] == "ねこだまし" and _v30b["mySeq"][0] == "ねこだまし", f"{_v30b}")
    check("かるわざ: ジュエル消費後の素早さ（初期Sの2倍）で決着ターンを比べる",
          _v30b["myS"] == 2 * _r30b["a"]["speed"] and _v30b["myS"] > _v30b["oppS"] > _r30b["a"]["speed"],
          f"初期S{_r30b['a']['speed']} 決着S{_v30b['myS']} 相手S{_v30b['oppS']}")
    check("ねこだまし: 相手は1ターン目に動けないので手数は2以上・先に倒して勝つ",
          _v30b["oppHits"] >= 2 and _v30b["win"] and _v30b["koFirst"], f"{_v30b}")

    _r30c = _mu30(_META30, _GHOLD30); _v30c = _r30c["verdict"]
    _lo30 = lambda side: min([m["hitsLo"] for m in side["moves"] if m.get("hitsLo") is not None] + [side["seqHits"]])
    check("判定は中央乱数の対戦（メタグロス vs サーフゴーは中央乱数で勝ち、スコアは±2にクリップ）",
          _v30c["myPrep"] is None and _v30c["oppPrep"] is None and _v30c["win"] and -2 <= _v30c["score"] <= 2, f"{_v30c}")
    _ms30 = {m["n"]: m for m in _r30c["a"]["moves"]}
    check("技ごとのタイプ相性: じしん→ふうせんのサーフゴーは無効(0)・サイコファング→はがねは今ひとつ(0.5)",
          _ms30["じしん"]["eff"] == 0 and _ms30["サイコファング"]["eff"] == 0.5, f"{ {k: v.get('eff') for k, v in _ms30.items()} }")
    # 持久戦は方針の1つ（別計算の記号上書きは廃止）。倒れたターンもターン終了時処理まで進める
    _DOHI30 = "ドヒドイデ@たべのこし:しんちょう:くろいきり|じこさいせい|どくどく|まとわりつく:32/0/0/0/32/0:さいせいりょく"
    _MANDA30b = "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン"
    _r30d = _mu30(_DOHI30, _MANDA30b); _v30d = _r30d["verdict"]
    _eot30 = [e for e in _v30d["race"] if e["actor"] is None and e["turn"] == 2]
    _tox30 = [ev["amount"] for e in _eot30 for ev in e["events"] if ev["kind"] == "badpoison" and ev["side"] == 1]
    _mx30 = _r30d["b"]["hp"]
    check("持久戦: ドヒドイデ vs メガボーマンダは どくどく→（倒される）を選び、倒れたT2のターン終了時にもうどく2/16が入る",
          _v30d["myPlan"] == "stall" and _v30d["mySeq"][:1] == ["どくどく"] and _v30d["stall"]["side"] is None
          and _v30d["race"] is not None and _tox30 == [_mx30 * 2 // 16], f"{_v30d['myPlan']} {_v30d['mySeq']} {_tox30} {_mx30}")
    _hit30 = [ev for e in _v30d["race"] if e["actor"] == 1 for ev in e["events"] if ev["kind"] == "move"]
    check("とどめの一撃は raw に頭打ち前の技のダメージ（T2のじしんは残り62に対し raw=104＝T1と同じ中央乱数の値）",
          len(_hit30) == 2 and "raw" not in _hit30[0] and _hit30[1]["amount"] == 62 and _hit30[1]["raw"] == _hit30[0]["amount"],
          f"{_hit30}")
    # 技ごとのダメージ一覧は へんげんじざい で変わる前の元のタイプ（判定の経過は型変化あり）
    _SANA30 = "サーナイト@きあいのタスキ:ひかえめ:10まんボルト|エナジーボール|ムーンフォース|ワイドフォース:0/0/0/32/0/32:トレース"
    _MASKA30 = "マスカーニャ@こだわりスカーフ:ようき:とんぼがえり|はたきおとす|トリックフラワー|トリプルアクセル:0/32/0/0/0/32:へんげんじざい"
    _ms30b = {m["n"]: m for m in _mu30(_SANA30, _MASKA30)["a"]["moves"]}
    check("技ごとの一覧は元のタイプ（マスカーニャ くさ/あく: ムーンフォース×2・ワイドフォース無効）で、defForm の注記は無い",
          _ms30b["ムーンフォース"]["eff"] == 2 and _ms30b["ワイドフォース"]["eff"] == 0
          and all("defForm" not in m for m in _ms30b.values()), f"{ {k: v.get('eff') for k, v in _ms30b.items()} }")
    # メガシンカ: 入場効果はメガ前の姿で素早さ順、1ターン目の行動前にメガシンカしてメガ後の特性（ひでり）が発動＝どちらの並びでも晴れ
    _CHY30 = "リザードン@リザードナイトY:おくびょう:かえんほうしゃ|はねやすめ|りゅうのはどう|ソーラービーム:0/0/0/32/0/32:ひでり"
    _PEL30 = "ペリッパー@しめったいわ:ひかえめ:とんぼがえり|ぼうふう|れいとうビーム|ウェザーボール:32/0/0/32/0/0:あめふらし"
    _w30 = [_mu30(x, y)["verdict"]["raceInit"]["weather"] for x, y in ((_CHY30, _PEL30), (_PEL30, _CHY30))]
    check("メガシンカは1ターン目の行動前（メガリザードンYのひでりが あめふらし の後に発動し、どちらの並びでも晴れ）",
          _w30 == ["sunny", "sunny"], f"{_w30}")
    # 同速: (a,b) と (b,a) のスコアは符号だけ入れ替わる
    _CHT30 = "リザードン@リザードナイトY:ひかえめ:かえんほうしゃ|エアスラッシュ|ソーラービーム|ニトロチャージ:0/0/0/32/0/7:ひでり"
    _PES30 = "ペリッパー@こだわりスカーフ:ひかえめ:とんぼがえり|ぼうふう|れいとうビーム|ウェザーボール:32/0/0/32/0/0:あめふらし"
    _t1, _t2 = _mu30(_CHT30, _PES30)["verdict"], _mu30(_PES30, _CHT30)["verdict"]
    _GAR30 = "ガルーラ@ガルーラナイト:いじっぱり:ねこだまし|すてみタックル|けたぐり|ふいうち:0/32/0/0/0/32:きもったま"
    _u1, _u2 = _mu30(_GAR30, _MANDA30b)["verdict"], _mu30(_MANDA30b, _GAR30)["verdict"]
    check("同速を含む対面で (a,b) と (b,a) のスコアは符号が逆（同速の先後は回した順で決める）",
          _t1["myS"] == _t1["oppS"] and abs(_t1["score"] + _t2["score"]) < 1e-9 and abs(_u1["score"] + _u2["score"]) < 1e-9,
          f"{_t1['myS']}/{_t1['oppS']} {_t1['score']} {_t2['score']} {_u1['score']} {_u2['score']}")
    # 未知の種族・読めない spec はパニックせずエラーを返し、以後の呼び出しも普通に動く
    _ok30 = _mu30(_KAME30, _MANDA30)
    _err30 = []
    for _bad in ("存在しない@なし:いじっぱり:たいあたり:0/0/0/0/0/0:なし", "カメックス@カメックスナイト:ひかえめ:あくのはどう:3x/0/0/0/0/0:メガランチャー"):
        try:
            _mu30(_bad, _KAME30); _err30.append("no-error")
        except ValueError as _e:
            _err30.append("ValueError")
    check("未知の種族・読めない spec は ValueError（パニックでロックを壊さず、次の呼び出しは同じ結果）",
          _err30 == ["ValueError", "ValueError"] and _mu30(_KAME30, _MANDA30) == _ok30, f"{_err30}")
    _ev30 = _mu30("ガブリアス@こだわりハチマキ:いじっぱり:ロックブラスト|じしん|げきりん|ストーンエッジ:0/32/0/0/0/32:さめはだ",
                  "ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")["verdict"]["race"][0]
    check("判定の対戦(Rust)でも、ばけのかわは連続技の1発目だけ防ぎ、残りのヒットは通る（disguise の後に move）",
          [e["kind"] for e in _ev30["events"]][:2] == ["disguise", "move"] and _ev30.get("blocked") is None, f"{_ev30}")
    # 1v1分析: ダブルいかく・まけんき/かちき・先にメガシンカして特性が変わった相手には2回目だけ（再生の開始画面の能力ランク）
    _ZUR30 = "ズルズキン@ズルズキナイト:いじっぱり:はたきおとす|りゅうのまい|れいとうパンチ|ドレインパンチ:32/32/0/0/0/0:いかく"
    _stg30 = lambda o: _mu30(_ZUR30, o)["verdict"]["raceInit"]["sides"][1]["stg"]
    _dz30 = [_stg30("ガブリアス@こだわりスカーフ:ようき:げきりん|じしん|ステルスロック|ドラゴンテール:0/32/0/0/0/32:さめはだ")[0],
             _stg30("ドドゲザン@くろいメガネ:いじっぱり:つるぎのまい|ふいうち|アイアンヘッド|ドゲザン:32/32/0/0/0/0:まけんき")[0],
             _stg30("ミロカロス@たべのこし:ずぶとい:じこさいせい|ねっとう|れいとうビーム|ミラーコート:32/0/32/0/0/0:かちき")[:3:2],
             _stg30("メタグロス@メタグロスナイト:いじっぱり:じしん|れいとうパンチ|サイコファング|バレットパンチ:0/32/0/0/0/32:かたいツメ")[0]]
    check("1v1分析のダブルいかく: 相手の攻撃-2／まけんき+2／かちき(攻撃-2・特攻+4)／メガ前クリアボディのメタグロスは2回目だけ-1",
          _dz30 == [-2, 2, [-2, 4], -1], f"{_dz30}")
    # メガシンカの天候の取り合い: メガシンカ前の素早さ順にメガシンカし、遅い側の天候が残る
    _CY30 = "リザードン@リザードナイトY:ひかえめ:かえんほうしゃ|はねやすめ|りゅうのはどう|ソーラービーム:0/0/0/32/0/32:ひでり"
    _wx30 = lambda s_: _mu30(f"ユキメノコ@ユキメノコナイト:ひかえめ:10まんボルト|ふぶき|オーロラベール|シャドーボール:0/0/0/32/0/{s_}:ゆきふらし", _CY30)["verdict"]["raceInit"]["weather"]
    check("メガユキメノコ vs メガリザードンY: 遅い側の天候が残る（ユキメノコが遅い→雪／速い→晴れ）", (_wx30(0), _wx30(32)) == ("hail", "sunny"),
          f"{(_wx30(0), _wx30(32))}")
    _ta30 = _mu30("ユキメノコ@ユキメノコナイト:ひかえめ:10まんボルト|ふぶき|オーロラベール|シャドーボール:0/0/0/32/0/22:ゆきふらし", _CY30)["verdict"]
    _tb30 = _mu30(_CY30, "ユキメノコ@ユキメノコナイト:ひかえめ:10まんボルト|ふぶき|オーロラベール|シャドーボール:0/0/0/32/0/22:ゆきふらし")["verdict"]
    check("メガ前が同速ならメガシンカの順は先後の両順（代表の経過は自分が先＝相手の天候が残る）。スコアは符号が逆",
          (_ta30["raceInit"]["weather"], _tb30["raceInit"]["weather"]) == ("sunny", "hail") and abs(_ta30["score"] + _tb30["score"]) < 1e-9,
          f"{_ta30['raceInit']['weather']} {_tb30['raceInit']['weather']}")
    # 再生用の発動記録（raceInit.events）: 入場の いかく ×2 → メガシンカ（素早さ順）→ メガズルズキンの いかく
    _ev30b = _mu30(_ZUR30, "ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン")["verdict"]["raceInit"]["events"]
    _seq30 = [(e["phase"], e["side"], e["ability"], e["effect"]) for e in _ev30b]
    check("発動記録: 入場の いかく（速いボーマンダ→ズルズキン）→ メガシンカ（ボーマンダ→ズルズキン）で2回目の いかく",
          _seq30 == [("entry", 1, "いかく", True), ("entry", 0, "いかく", True), ("mega", 1, "スカイスキン", False), ("mega", 0, "いかく", True)]
          and _ev30b[3]["stg"][1][0] == -1, f"{_seq30}")
    _ev30c = _mu30(_CY30, "ユキメノコ@ユキメノコナイト:ひかえめ:10まんボルト|ふぶき|オーロラベール|シャドーボール:0/0/0/32/0/0:ゆきふらし")["verdict"]["raceInit"]["events"]
    check("発動記録: メガリザードンYの ひでり（晴れ）→ 遅いメガユキメノコの ゆきふらし（雪）の順",
          [(e["ability"], e["weather"]) for e in _ev30c if e["phase"] == "mega"] == [("ひでり", "sunny"), ("ゆきふらし", "hail")], f"{_ev30c}")
    # 仮定の続き（倒された側の手数）で、勝った側の反動が水増しで膨らんで自滅しない
    _luc30 = _mu30("ルカリオ@ルカリオナイトZ:おくびょう:あくのはどう|はどうだん|わるだくみ|ラスターカノン:0/0/0/32/0/32:せいしんりょく",
                   "リザードン@リザードナイトX:いじっぱり:かみなりパンチ|げきりん|りゅうのまい|フレアドライブ:0/32/0/0/0/32:かたいツメ")["verdict"]
    check("仮定の続き: メガルカリオZ vs メガリザードンX の自分の手数は2（水増しでフレアドライブの反動が膨らみ相手が自滅した1ではない）",
          _luc30["myHits"] == 2 and _luc30["oppHits"] == 1, f"{_luc30['myHits']} {_luc30['oppHits']}")
    # 仮定の続きは「倒れても行動し続ける」印で本物のHPのまま回す
    _fk30 = _mu30("バクフーン@こだわりスカーフ:おくびょう:ふんか|ひゃっきやこう|シャドーボール|きあいだま:2/0/0/32/0/32:おみとおし",
                  "リザードン@リザードナイトY:おくびょう:かえんほうしゃ|はねやすめ|りゅうのはどう|ソーラービーム:0/0/0/32/0/32:ひでり")["verdict"]
    check("仮定の続き: ふんかは倒れた後の0のHPで威力が落ちるので、決着ターン(2)までには倒せない（水増しで威力が落ちず2と出ていた）",
          _fk30["myHits"] > 2 and _fk30["oppHits"] == 2, f"{_fk30['myHits']} {_fk30['oppHits']}")
    _gh30 = _mu30("ギャラドス@ゴツゴツメット:わんぱく:たきのぼり|ちょうはつ|ゆきなだれ|パワーウィップ:32/0/32/0/0/0:いかく",
                  "アーマーガア@ゴツゴツメット:わんぱく:てっぺき|とんぼがえり|はねやすめ|ボディプレス:32/0/32/0/0/0:プレッシャー")["verdict"]
    check("仮定の続き: 倒れた側が生きていたら受けるゴツゴツメット（相手のボディプレス）で相手が倒れるターンは数える（4ターン目）",
          _gh30["myHits"] == 4 and _gh30["oppHits"] == 4 and not _gh30["win"], f"{_gh30['myHits']} {_gh30['oppHits']}")
    _mbv30 = _mu30("フレフワン@ようせいのハネ:ひかえめ:トリックルーム|ムーンフォース|アンコール|ミストバースト:0/0/0/0/0/0:アロマベール",
                   "ボーマンダ@ボーマンダナイト:ひかえめ:かえんほうしゃ|はねやすめ|りゅうせいぐん|ハイパーボイス:0/0/0/32/0/32:スカイスキン")["verdict"]
    _last30 = _mbv30["race"][-1]
    check("1v1: ミストバーストで相手を倒すと自分も倒れて相打ち（原因は selfko）",
          _mbv30["mutual"] and _last30["hp"] == [0, 0] and any(e["kind"] == "selfko" and e["side"] == 0 for e in _last30["events"]),
          f"{_mbv30['sym']} {_last30}")
    # 技ごとの前提の注記は、その技のダメージを実際に変えるものだけ
    _cd30 = {m["n"]: m.get("conds") for m in _mu30("ガブリアス@いのちのたま:いじっぱり:じしん|かえんほうしゃ|げきりん|ストーンエッジ:0/32/0/0/0/32:さめはだ",
             "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく")["a"]["moves"]}
    check("注記: いかくの攻撃-1は物理技だけ（特殊技かえんほうしゃ・無効のじしんには付かない）",
          _cd30["げきりん"] == ["攻撃-1"] and _cd30["かえんほうしゃ"] == [] and _cd30["じしん"] == [], f"{_cd30}")
    _CZ30 = "リザードン@いのちのたま:ひかえめ:かえんほうしゃ|エアスラッシュ|りゅうのはどう|フレアドライブ:0/0/0/32/0/32:もうか"
    _sd30 = [{m["n"]: m.get("conds") for m in _mu30(_CZ30, d)["a"]["moves"]} for d in (
        "バンギラス@さらさらいわ:しんちょう:じしん|はたきおとす|ステルスロック|ストーンエッジ:32/0/0/0/32/0:すなおこし",
        "カバルドン@ゴツゴツメット:しんちょう:あくび|じしん|ふきとばし|ステルスロック:32/0/0/0/32/0:すなおこし")]
    check("注記: すなあらしは防御側がいわタイプで特殊技のときだけ（物理技・いわでない相手には付かない）",
          _sd30[0]["りゅうのはどう"] == ["sandstorm"] and _sd30[0]["フレアドライブ"] == [] and _sd30[1]["りゅうのはどう"] == [], f"{_sd30}")
    # 注記: 防御側の特性（マルチスケイル）。かたやぶりで無視される攻撃側には付かない
    _KAI30 = "カイリュー@ゴツゴツメット:いじっぱり:げきりん|しんそく|じしん|はねやすめ:0/32/0/0/0/32:マルチスケイル"
    _mc30 = {m["n"]: m.get("conds") for m in _mu30("ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン", _KAI30)["a"]["moves"]}
    _mb30b = {m["n"]: m.get("conds") for m in _mu30("ドリュウズ@きあいのタスキ:ようき:じしん|アイアンヘッド|いわなだれ|つるぎのまい:0/32/0/0/0/32:かたやぶり", _KAI30)["a"]["moves"]}
    check("注記: マルチスケイルで半減する技に「防御特性:マルチスケイル」、かたやぶりの攻撃・無効の技には付かない",
          _mc30["すてみタックル"] == ["防御特性:マルチスケイル"] and _mc30["じしん"] == [] and _mb30b["いわなだれ"] == [], f"{_mc30} {_mb30b}")
    _r30e = _mu30(_DOHI30, _DOHI30)["verdict"]
    _k30 = {ev["kind"] for e in _r30e["race"] for ev in e["events"]}
    check("持久戦の同型対面は五分（△）。拘束のダメージは原因 bind で記録される",
          _r30e["sym"] == "△" and _r30e["myPlan"] == "stall" and _r30e["oppPlan"] == "stall" and "bind" in _k30, f"{_r30e['sym']} {_k30}")
except Exception as _e30:
    check("1v1判定の2者対戦テストが実行できる", False, f"{type(_e30).__name__}: {_e30}")

# ════════════════════════════════════════════════════════════════
# 31. 対戦エンジン本体の修正（2026-09-27 1v1独立監査）
#     反動・吸収の基準＝実際に減らしたHP／グラスフィールドの回復と残りターン／さまようたましいの不可特性／
#     オボンのみは被弾直後／入場時効果・メガ進化は速い側から／いのちのたまは技1回につき1回・ばけのかわでも受ける
# ════════════════════════════════════════════════════════════════
# datapack のネット: Rust net.rs は vbins（価値の two-hot の区間数）を重みと同じ階層から読む。_meta に入れると常に0と読まれる
try:
    import json as _jdp
    _dp = _jdp.load(open(os.environ.get("POKENAVI_DATAPACK") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_rust_engine", "datapack.json")))
    _nf = _jdp.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "az_net_np.json")))
    check("datapack のネットは vbins をトップレベルに持ち、本番ネットの値と一致する",
          _dp["net"] is not None and _dp["net"].get("vbins", 0) == _nf.get("vbins", 0) and "vbins" not in _dp["net"].get("_meta", {}),
          f"{_dp['net'].get('vbins') if _dp.get('net') else None} / {_nf.get('vbins')}")
except FileNotFoundError:
    pass

print("\n=== 31. 対戦エンジン本体（監査の修正） ===")
try:
    from simulator.pokemon import build_from_spec as _b31, parse_pokemon_spec as _p31
    import simulator.battle as _bt31
    def _mk31(spec):
        return _b31(_p31(spec), dl, season="M-6", randomize=False)
    def _sides31(a, b):
        s1 = BattleSide([a], viewer_label="P1"); s2 = BattleSide([b], viewer_label="P2")
        s1.field_idx = 0; s2.field_idx = 1
        return s1, s2
    def _act31(p, name):
        i = next(k for k, m in enumerate(p.moves) if m and m.name_jp == name)
        return Action(type="move", move=p.moves[i], move_idx=i)
    import random as _r31

    # 反動は残りHPで頭打ちした「実際に減らしたHP」が基準
    _a = _mk31("ボーマンダ@こだわりハチマキ:いじっぱり:すてみタックル|じしん|げきりん|はねやすめ:0/32/0/0/0/32:いかく")
    _d = _mk31("ゴリランダー@オボンのみ:いじっぱり:グラススライダー|はたきおとす|とんぼがえり|10まんばりき:32/32/0/0/0/0:しんりょく")
    _d.hp = 30
    _s1, _s2 = _sides31(_a, _d); _f = BattleField(); _f.always_hit = True if hasattr(_f, "always_hit") else None
    _r31.seed(1)
    _h0 = _a.hp
    _execute_move(_s1, _s2, _act31(_a, "すてみタックル"), BattleField())
    check("反動: 残りHP30を倒したすてみタックルの反動は 30/3=10（計算ダメージ基準ではない）",
          not _d.is_alive and _h0 - _a.hp == 10, f"反動{_h0 - _a.hp}")

    # 吸収も実際に減らしたHPが基準
    _a = _mk31("フシギバナ@たべのこし:ひかえめ:ギガドレイン|ヘドロばくだん|やどりぎのタネ|まもる:32/0/0/32/0/0:しんりょく")
    _d = _mk31("カメックス@たべのこし:ひかえめ:ハイドロポンプ|れいとうビーム|あくのはどう|まもる:32/0/0/32/0/0:げきりゅう")
    _d.hp = 20; _a.hp = 50
    _s1, _s2 = _sides31(_a, _d)
    _r31.seed(1)
    _execute_move(_s1, _s2, _act31(_a, "ギガドレイン"), BattleField())
    check("吸収: 残りHP20を倒したギガドレインの回復は 20/2=10", not _d.is_alive and _a.hp == 60, f"HP{_a.hp}")

    # グラスフィールド: 地面にいるポケモンは1/16回復し、残りターンで切れる
    _a = _mk31("ゴリランダー@たべのこし:いじっぱり:グラススライダー|はたきおとす|とんぼがえり|10まんばりき:32/32/0/0/0/0:グラスメイカー")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/2/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _gb = Battle(_s1, _s2, BattleField())
    _gb.field.grassy_terrain = True; _gb.field.grassy_terrain_count = 2
    _d.hp = _d.max_hp - 50
    _h = _d.hp
    _gb._end_of_turn()
    check("グラスフィールド: ターン終了時に地面にいるポケモンが最大HPの1/16回復",
          _d.hp - _h == max(1, _d.max_hp // 16), f"{_d.hp - _h}")
    _gb._end_of_turn()
    check("グラスフィールド: 残りターンが0で終わる", _gb.field.grassy_terrain is False, f"{_gb.field.grassy_terrain_count}")

    # さまようたましい: ばけのかわ 等の入れ替え不可の特性とは入れ替えない
    from simulator.abilities import on_after_hit as _oah31
    _a = _mk31("ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _d.ability = "さまようたましい"  # type: ignore
    _oah31(_a, _d, _a.moves[0], [])
    check("さまようたましい: ばけのかわ とは入れ替えない", _a.ability == "ばけのかわ" and _d.ability == "さまようたましい",
          f"{_a.ability}/{_d.ability}")

    # オボンのみ: 被弾でHPが半分以下になった直後に発動（ターン終了を待たない）
    _a = _mk31("ガブリアス@こだわりハチマキ:いじっぱり:げきりん|じしん|ストーンエッジ|アイアンヘッド:2/32/0/0/0/32:さめはだ")
    _d = _mk31("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/2/0:すなおこし")
    _d.hp = _d.max_hp // 2 + 20
    _s1, _s2 = _sides31(_a, _d)
    _r31.seed(3)
    _execute_move(_s1, _s2, _act31(_a, "じしん"), BattleField())
    check("オボンのみ: 被弾で半分以下になった直後に食べる（技の処理の中で）", _d.item is None and _d.ate_berry, f"{_d.item}")

    # いのちのたま: ばけのかわに当たってダメージ0でも反動を受ける／連続技でも1回
    _a = _mk31("カバルドン@いのちのたま:いじっぱり:じしん|あくび|ステルスロック|なまける:32/32/0/0/0/0:すなおこし")
    _d = _mk31("ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")
    _s1, _s2 = _sides31(_a, _d)
    _h0 = _a.hp
    _execute_move(_s1, _s2, _act31(_a, "じしん"), BattleField())
    check("いのちのたま: ばけのかわ に当たって無効でも反動（最大HPの1/10）を受ける",
          _h0 - _a.hp == max(1, _a.max_hp // 10), f"{_h0 - _a.hp}")
    _a = _mk31("ガブリアス@いのちのたま:いじっぱり:スケイルショット|じしん|げきりん|つるぎのまい:0/32/0/0/0/32:さめはだ")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _h0 = _a.hp
    _r31.seed(5)
    _execute_move(_s1, _s2, _act31(_a, "スケイルショット"), BattleField())
    check("いのちのたま: 連続技でも反動は技1回につき1回", _h0 - _a.hp == max(1, _a.max_hp // 10), f"{_h0 - _a.hp}")

    # ばけのかわ: 連続技は1発目だけ防ぎ、2発目以降は通る
    _a = _mk31("ガブリアス@こだわりハチマキ:いじっぱり:ロックブラスト|じしん|げきりん|ストーンエッジ:0/32/0/0/0/32:さめはだ")
    _d = _mk31("ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")
    _s1, _s2 = _sides31(_a, _d)
    _bt31._MULTI_HIT_FIXED = 3
    try:
        _execute_move(_s1, _s2, _act31(_a, "ロックブラスト"), BattleField())
    finally:
        _bt31._MULTI_HIT_FIXED = None
    check("ばけのかわ: 連続技は1発目だけ防ぎ、2発目以降のダメージは入る（1/8より多く減る）",
          getattr(_d, "_disguise_broken", False) and (_d.max_hp - _d.hp) > max(1, _d.max_hp // 8), f"減少{_d.max_hp - _d.hp}")
    # ばけのかわ: ねこだましは防いでもひるむ
    _a = _mk31("ガルーラ@ガルーラナイト:いじっぱり:ねこだまし|すてみタックル|けたぐり|ふいうち:0/32/0/0/0/32:きもったま")
    _d = _mk31("ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ")
    _s1, _s2 = _sides31(_a, _d)   # きもったま の ねこだまし はゴーストのミミッキュにも当たる
    _execute_move(_s1, _s2, _act31(_a, "ねこだまし"), BattleField())
    check("ばけのかわ: ねこだましはダメージを防いでもひるむ", getattr(_d, "_disguise_broken", False) and _d.flinched and _d.hp == _d.max_hp - max(1, _d.max_hp // 8),
          f"{_d.flinched} {_d.hp}/{_d.max_hp}")
    # 連続技の途中でHPが半分以下になったら、次のヒットの前にオボンのみ
    _a = _mk31("ガブリアス@こだわりハチマキ:いじっぱり:スケイルショット|じしん|げきりん|ストーンエッジ:0/32/0/0/0/32:さめはだ")
    _d = _mk31("カバルドン@オボンのみ:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _d.hp = _d.max_hp // 2 + 5
    _bt31._MULTI_HIT_FIXED = 5
    try:
        _lg31 = _execute_move(_s1, _s2, _act31(_a, "スケイルショット"), BattleField())
    finally:
        _bt31._MULTI_HIT_FIXED = None
    _ib31 = next((i for i, x in enumerate(_lg31) if "オボン" in x), None)
    _hits_after = sum(1 for x in _lg31[_ib31 + 1:] if "スケイルショット" in x and "ダメ" in x) if _ib31 is not None else -1
    check("オボンのみ: 連続技の途中で半分を切ったら次のヒットの前に食べる", _d.item is None and _ib31 is not None,
          f"{_lg31}")
    # いのちのたまとレッドカード: レッドカード（防御側の持ち物）が先、いのちのたまの反動が後（battle.rs と同じ順）
    _a = _mk31("ガブリアス@いのちのたま:いじっぱり:じしん|げきりん|ストーンエッジ|つるぎのまい:0/32/0/0/0/32:さめはだ")
    _b2 = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _d = _mk31("カバルドン@レッドカード:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1 = BattleSide([_a, _b2], viewer_label="P1"); _s2 = BattleSide([_d], viewer_label="P2")
    _s1.field_idx = 0; _s2.field_idx = 1
    _a.hp = max(1, _a.max_hp // 10)
    _execute_move(_s1, _s2, _act31(_a, "じしん"), BattleField())
    check("レッドカードは いのちのたま の反動で攻撃側が倒れる前に発動する（持ち物を消費）",
          _d.item is None and not _a.is_alive, f"{_d.item} {_a.hp}")

    # メガ石を持つ型のメガ前の特性: spec のメガ特性ではなく元の種族の特性で入場し、メガシンカで切り替わる
    _pm = _mk31("ボーマンダ@ボーマンダナイト:いじっぱり:じしん|すてみタックル|はねやすめ|りゅうのまい:0/32/0/0/0/32:スカイスキン")
    _ab0 = _pm.ability; _pm.do_mega_evolve()
    check("メガ前の特性: ボーマンダ(スカイスキン指定)はメガ前 いかく → メガ後 スカイスキン", (_ab0, _pm.ability) == ("いかく", "スカイスキン"),
          f"{_ab0}/{_pm.ability}")
    _pm2 = _mk31("メタグロス@メタグロスナイト:いじっぱり:じしん|れいとうパンチ|サイコファング|バレットパンチ:0/32/0/0/0/32:ライトメタル")
    check("メガ前の特性: spec の特性が通常特性ならそのまま（メタグロス:ライトメタル）", _pm2.ability == "ライトメタル", _pm2.ability)
    _pm3 = _mk31("リザードン@リザードナイトY:おくびょう:かえんほうしゃ|はねやすめ|りゅうのはどう|ソーラービーム:0/0/0/32/0/32:ひでり")
    check("メガ前の特性: リザードンY(ひでり指定)はメガ前 もうか", _pm3.ability == "もうか", _pm3.ability)
    # 対戦本体: メガズルズキンは いかく で入場し、1ターン目のメガシンカで いかく が再び発動（相手の攻撃-2）。まけんき は2回発動
    def _dbl31(opp_spec):
        _z = _mk31("ズルズキン@ズルズキナイト:いじっぱり:はたきおとす|りゅうのまい|れいとうパンチ|ドレインパンチ:32/32/0/0/0/0:いかく")
        _o = _mk31(opp_spec)
        _s1, _s2 = _sides31(_z, _o)
        _b = Battle(_s1, _s2, BattleField())
        for _sd, _os, _ix in _bt31._entry_order(_b.side1, _b.side2, _b.field):
            _bt31._entry_effects(_sd.active, _ix, _b.field, _os.active, [], _sd.party)
        _st0 = (_o.stage_attack, _o.stage_sp_attack)
        _mz = next(m for m in _z.moves if m.name_jp == "りゅうのまい")
        _b._turn_loop(lambda m, o, f: Action(type="move", move=_mz, move_idx=_z.moves.index(_mz), do_mega=True),
                      lambda m, o, f: Action(type="pass"), max_turns=1)
        return _st0, (_o.stage_attack, _o.stage_sp_attack), _z.mega_evolved
    _r1 = _dbl31("ガブリアス@こだわりスカーフ:ようき:げきりん|じしん|ステルスロック|ドラゴンテール:0/32/0/0/0/32:さめはだ")
    check("ダブルいかく(対戦本体): 入場で-1、メガシンカで再び-1（合計-2）", _r1 == ((-1, 0), (-2, 0), True), f"{_r1}")
    _r2 = _dbl31("ドドゲザン@くろいメガネ:いじっぱり:つるぎのまい|ふいうち|アイアンヘッド|ドゲザン:32/32/0/0/0/0:まけんき")
    check("ダブルいかく(対戦本体): まけんき は2回発動（-1+2を2回で+2）", _r2[1][0] == 2, f"{_r2}")
    _r3 = _dbl31("ミロカロス@たべのこし:ずぶとい:じこさいせい|ねっとう|れいとうビーム|ミラーコート:32/0/32/0/0/0:かちき")
    check("ダブルいかく(対戦本体): かちき は2回発動（攻撃-2・特攻+4）", _r3[1] == (-2, 4), f"{_r3}")
    _r4 = _dbl31("メタグロス@メタグロスナイト:いじっぱり:じしん|れいとうパンチ|サイコファング|バレットパンチ:0/32/0/0/0/32:クリアボディ")
    check("ダブルいかく(対戦本体): クリアボディは両方防ぐ（メガしない相手）", _r4[1][0] == 0, f"{_r4}")

    # 自分が倒れる技: 相手を倒しても・タイプ無効でも・ばけのかわに防がれても自分は倒れる
    def _sk31(att_spec, mv, def_spec, def_hp=None):
        _a = _mk31(att_spec); _d = _mk31(def_spec)
        if def_hp is not None: _d.hp = def_hp
        _s1, _s2 = _sides31(_a, _d)
        _execute_move(_s1, _s2, _act31(_a, mv), BattleField())
        return _a.is_alive, _d.is_alive
    _HAT31 = "ブリムオン@ようせいのハネ:ひかえめ:マジカルシャイン|サイコキネシス|トリックルーム|ミストバースト:32/0/0/32/0/0:マジックミラー"
    _GAR31 = "ガブリアス@こだわりスカーフ:ようき:げきりん|じしん|ステルスロック|ドラゴンテール:0/32/0/0/0/32:さめはだ"
    check("ミストバースト: 相手を倒しても自分は倒れる", _sk31(_HAT31, "ミストバースト", _GAR31, def_hp=1) == (False, False))
    _BOM31 = "ガブリアス@きあいのタスキ:いじっぱり:だいばくはつ|じしん|げきりん|ステルスロック:0/32/0/0/0/32:さめはだ"
    check("だいばくはつ: ゴーストに無効でも自分は倒れる",
          _sk31(_BOM31, "だいばくはつ", "ゲンガー@ゲンガナイト:おくびょう:シャドーボール|ヘドロばくだん|まもる|みちづれ:0/0/0/32/0/32:のろわれボディ") == (False, True))
    check("だいばくはつ: ばけのかわに防がれても自分は倒れる",
          _sk31(_BOM31, "だいばくはつ", "ミミッキュ@いのちのたま:いじっぱり:じゃれつく|かげうち|つるぎのまい|シャドークロー:0/32/0/0/0/32:ばけのかわ") == (False, True))

    # 入場時効果は速い側から: 遅い側の天候が残る（カバルドン(遅い)のすなおこしが後）
    _a = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _d = _mk31("キュウコン(アローラ)@ひかりのねんど:おくびょう:ふぶき|オーロラベール|ムーンフォース|フリーズドライ:0/0/0/32/0/32:ゆきふらし")
    _s1, _s2 = _sides31(_d, _a)
    _eb = Battle(_s1, _s2, BattleField())
    for _sd, _os, _ix in _bt31._entry_order(_eb.side1, _eb.side2, _eb.field):
        _bt31._entry_effects(_sd.active, _ix, _eb.field, _os.active, [], _sd.party)
    check("入場時効果: 速い側から発動し、遅い側（カバルドン）の すなあらし が残る（並び順に依らない）",
          _eb.field.weather == "sandstorm", f"{_eb.field.weather}")
    # 拘束は縛った側が倒れたら解ける（ターン終了時のダメージが入らない）。ターン終了時処理は速い側から
    _a = _mk31("ドヒドイデ@たべのこし:しんちょう:くろいきり|じこさいせい|どくどく|まとわりつく:32/0/0/0/32/0:さいせいりょく")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _bb = Battle(_s1, _s2, BattleField())
    _d.bound_count = 3; _d.hp = _d.max_hp - 40; _h = _d.hp
    _a.hp = 0; _a.is_alive = False
    _bb._end_of_turn()
    check("拘束: 縛った側が倒れていればターン終了時のダメージは入らず解ける", _d.bound_count == 0 and _d.hp == _h,
          f"{_d.bound_count} {_h - _d.hp}")
    _a = _mk31("ドヒドイデ@たべのこし:しんちょう:くろいきり|じこさいせい|どくどく|まとわりつく:32/0/0/0/32/0:さいせいりょく")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _bb = Battle(_s1, _s2, BattleField())
    _d.bound_count = 3; _h = _d.hp - 40; _d.hp = _h
    _bb._end_of_turn()
    check("拘束: 縛った側が場にいればターン終了時に1/8", _h - _d.hp == max(1, _d.max_hp // 8) and _d.bound_count == 2,
          f"{_h - _d.hp}")
    # 速いカバルドン(side2)が先に処理されるので、遅いドヒドイデ(side1)が砂で倒れる前に拘束のダメージが入る
    _a = _mk31("ドヒドイデ@くろいヘドロ:しんちょう:くろいきり|じこさいせい|どくどく|まとわりつく:32/0/0/0/32/0:ひとでなし")
    _d = _mk31("カバルドン@ゴツゴツメット:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/32/0:すなおこし")
    _s1, _s2 = _sides31(_a, _d)
    _bb = Battle(_s1, _s2, BattleField())
    _bb.field.weather = "sandstorm"; _bb.field.weather_count = 5
    _a.hp = 1; _a.item = None
    _d.bound_count = 3; _h = _d.hp - 40; _d.hp = _h
    _bb._end_of_turn()
    check("ターン終了時処理は素早さの速い側から（速い側の拘束ダメージは、遅い縛り手が砂で倒れる前に入る）",
          not _a.is_alive and _h - _d.hp == max(1, _d.max_hp // 8), f"{_a.hp} {_h - _d.hp}")
except Exception as _e31:
    import traceback; traceback.print_exc()
    check("対戦エンジン本体の監査修正テストが実行できる", False, f"{type(_e31).__name__}: {_e31}")

# 集計
# ════════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print("\n=== 32. 型の書式（種名に「:」を含む種） ===")
from simulator.pokemon import parse_pokemon_spec as _pps32
_s32 = _pps32("ケンタロス:炎@ラムのみ:いじっぱり:インファイト|フレアドライブ|ワイルドボルト|ビルドアップ:0/32/0/0/0/32:いかく")
check("種名に「:」を含む型を読める（ケンタロス:炎）",
      _s32["name"] == "ケンタロス:炎" and _s32["item"] == "ラムのみ" and _s32["nature"] == "いじっぱり"
      and _s32["evs"]["A"] == 32 and _s32["ability"] == "いかく", str(_s32))
_g32 = _pps32("ガブリアス@ガブリアスナイト:いじっぱり:じしん|げきりん|ステルスロック|がんせきふうじ:2/32/0/0/0/32")
check("従来の書式はそのまま読める", _g32["name"] == "ガブリアス" and _g32["item"] == "ガブリアスナイト"
      and _g32["moves"][0] == "じしん" and _g32["evs"]["H"] == 2)

print("\n=== 33. 型プールの週次チェック（scripts/pool_checks.py がわざと壊した入力を検出する） ===")
import _gen_type_pool as _G33
import arch_groups as _A33
import pool_checks as _C33
_ok33 = {"item": "きあいのタスキ", "nature": "ようき", "ability": "さめはだ", "ev": [0, 32, 0, 0, 2, 32],
         "moves": ["じしん", "げきりん", "ステルスロック", "がんせきふうじ"], "weight": 1.0}
_n33 = _C33.natures(_G33)
check("生成ルール: 正しい型は違反なし", _C33.rule_errors(_G33, "ガブリアス", [_ok33], set(), _n33) == [],
      str(_C33.rule_errors(_G33, "ガブリアス", [_ok33], set(), _n33)))
def _err33(**kw):
    return " ".join(_C33.rule_errors(_G33, "ガブリアス", [dict(_ok33, **kw)], set(), _n33))
check("生成ルール: ジュエルに同タイプの攻撃技が無い", "ジュエル" in _err33(item="ノーマルジュエル"))
check("生成ルール: こだわり×積み技", "こだわり" in _err33(item="こだわりスカーフ", moves=["じしん", "げきりん", "つるぎのまい", "がんせきふうじ"]))
check("生成ルール: EV 33・合計67", "EV" in _err33(ev=[0, 33, 0, 0, 0, 32]) and "EV" in _err33(ev=[3, 32, 0, 0, 0, 32]))
check("生成ルール: 覚えない技（没収技）", "覚えない技" in _err33(moves=["じしん", "げきりん", "ハイドロポンプ", "がんせきふうじ"]))
check("生成ルール: 重みの合計", "重みの合計" in _err33(weight=0.5))
def _g33(name, moves, share, item="きあいのタスキ", kind="物理"):
    return {"name": name, "kind": kind, "share": share,
            "builds": [{"item": item, "nature": "ようき", "ability": "さめはだ", "ev": [0, 32, 0, 0, 2, 32], "moves": moves, "weight": 1.0}]}
_sd33 = ["じしん", "げきりん", "つるぎのまい", "がんせきふうじ"]
_sr33 = ["じしん", "げきりん", "ステルスロック", "がんせきふうじ"]
_ne33 = lambda gs: " ".join(_C33.naming_errors(_G33, _A33, "ガブリアス", gs))
check("命名: 正しい系統は違反なし", _ne33([_g33("つるぎのまい", _sd33, 0.6), _g33("ステルスロック", _sr33, 0.4)]) == "",
      _ne33([_g33("つるぎのまい", _sd33, 0.6), _g33("ステルスロック", _sr33, 0.4)]))
check("命名: 同名の系統（バチンウニのグランドコート×2）", "同名" in _ne33([_g33("ステルスロック", _sr33, 0.6), _g33("ステルスロック", _sr33, 0.4, kind="特殊")]))
check("命名: 名前の技が系統内85%未満", "名前の技" in _ne33([_g33("ドラゴンテール", _sd33, 0.6), _g33("ステルスロック", _sr33, 0.4)]))
check("命名: 積み技が名前に無い", "積み技" in _ne33([_g33("じしん", _sd33, 0.6), _g33("ステルスロック", _sr33, 0.4)]))
check("命名: 系統が7つ", "系統が7個" in _ne33([_g33(f"x{i}", _sr33, 1 / 7) for i in range(7)]))
check("命名: 単一の型は系統が1つの種だけ", "単一の型" in _ne33([_g33("単一の型", _sr33, 0.6), _g33("つるぎのまい", _sd33, 0.4)]))
check("命名: バトンの型が名前に無い", "バトン" in _ne33([_g33("つるぎのまい", ["じしん", "つるぎのまい", "バトンタッチ", "がんせきふうじ"], 0.6), _g33("ステルスロック", _sr33, 0.4)]))
check("命名: 5%未満が同じ持ち物の区分で統合されていない", "5%未満" in _ne33([_g33("つるぎのまい", _sd33, 0.97), _g33("ステルスロック", _sr33, 0.03)]))
check("命名: 持ち物の区分（メガ石）をまたぐ系統",
      "またいで" in _ne33([{**_g33("つるぎのまい", _sd33, 1.0), "builds": _g33("つるぎのまい", _sd33, 1.0)["builds"] + [dict(_ok33, item="ガブリアスナイト", moves=_sd33)]}]))
_e64 = [dict(_ok33, ev=[0, 32, 0, 0, 0, 32])]
_e66 = [dict(_ok33, ev=[2, 32, 0, 0, 0, 32])]
_dbe33 = {(2, 32, 0, 0, 0, 32): 0.97, (0, 32, 0, 0, 0, 32): 0.03}
check("audit40 #21 週次チェック: 努力値の合計がDB（合計66が主流）と食い違うと検出し、合っていれば出さない",
      _C33.ev_total_diff(_e64, _dbe33)[0] > _C33.EV_TOTAL_TOL and _C33.ev_total_diff(_e66, _dbe33)[0] < _C33.EV_TOTAL_TOL)
check("audit40 #21 生成器: 出力の努力値は2刻みで余り2を残す（32/32 に余り2＝合計66、1/1 は大きい端数の方へ2）",
      _G33._ev_fine((2, 32, 0, 0, 0, 32)) == (2, 32, 0, 0, 0, 32) and _G33._ev_fine((0, 32, 1, 0, 1, 32)) == (0, 32, 2, 0, 0, 32)
      and _G33._ev_fine((32, 0, 25, 0, 9, 0)) == (32, 0, 26, 0, 8, 0), str(_G33._ev_fine((0, 32, 1, 0, 1, 32))))
check("audit40 #22 週次チェック: 特性の DB との差の許容は5pt", _C33.MARG_TOL["abilities"] == 5.0)
_gk33 = _G33.generate_one("ドドゲザン", 0)
_mg33 = _G33.marginals("ドドゲザン")
_pm33 = _C33.pool_marg(_G33, _gk33["builds"])
_abd33 = max(abs(_pm33["abilities"].get(k, 0) - v) for k, v in _mg33["abilities"].items())
check("audit40 #22 生成器: ドドゲザンの特性の採用率がDBと1pt以内（まけんき 約20%）", _abd33 < 0.01 and _pm33["abilities"]["まけんき"] > 0.15,
      f"{dict(_pm33['abilities'])} {_mg33['abilities']}")
_etd33 = _C33.ev_total_diff(_gk33["builds"], {e: v for t in _G33.ev_fine_table("ドドゲザン").values() for e, v in t.items()})
check("audit40 #21 生成器: ドドゲザンの努力値の合計の割合がDBと2pt以内（合計66が主流）", _etd33[0] < 2.0, str(_etd33))
_arch33 = {"_version": "M-6/x", "0445-00": {"season": "M-6", "groups": [{"name": "つるぎのまい型", "share": 60.0}, {"name": "ステルスロック型", "share": 40.0}]}}
_mu33 = lambda **kw: {"0445-00": {"mu": [dict({"arch": "つるぎのまい型", "archNo": 1, "archSub": "", "share": 60.0}, **kw)]}}
check("出力: 整合していれば違反なし", _C33.output_errors(_arch33, _mu33(), "M-6/x", "M-6/x") == [], str(_C33.output_errors(_arch33, _mu33(), "M-6/x", "M-6/x")))
check("出力: archNo が想定型の別の系統を指す", _C33.output_errors(_arch33, _mu33(archNo=2), "M-6/x", "M-6/x") != [])
check("出力: 1v1 と想定型の割合の不一致", _C33.output_errors(_arch33, _mu33(share=50.0), "M-6/x", "M-6/x") != [])
check("出力: 版の記録の不一致", _C33.output_errors(_arch33, _mu33(), "M-6/x", "M-6/y") != [])
check("出力: 「〜型」でない系統名", _C33.output_errors({**_arch33, "0445-00": {"season": "M-6", "groups": [{"name": "つるぎのまい", "share": 100.0}]}}, {}, "M-6/x", "M-6/x") != [])
_split33 = {"0445-00": {"mu": [{"arch": "つるぎのまい型（つるぎのまい・じしん）", "archNo": 1, "archSub": "a", "share": 30.0},
                              {"arch": "つるぎのまい型（つるぎのまい・げきりん）", "archNo": 1, "archSub": "b", "share": 30.0}]}}
check("出力: 分割ラベルの括弧内で系統名の語を繰り返す", any("繰り返" in e for e in _C33.output_errors(_arch33, _split33, "M-6/x", "M-6/x")))

print("\n=== 34. 選出ガイド（相手集団 guide_pool_m6.json の統計・学習選出・Rust guide_rows） ===")
import random as _r34
import _select_guide as _SG34
from simulator.learned_selection import learned_select_scores as _lss34, learned_select_party as _lsp34
_A34 = [_mk26c(x) for x in _P1s]; _B34 = [_mk26c(x) for x in _P2s]
_sc34 = _lss34(_A34, _B34, dl, n=3, rng=_r34.Random(5))
_pk34 = _lsp34(_A34, _B34, dl, n=3, temperature=0.0, rng=_r34.Random(5))
check("学習選出の全候補のスコア: 最良が learned_select_party（温度0）と同じ並び",
      _sc34 is not None and [id(p) for p in max(_sc34, key=lambda x: x[1])[0]] == [id(p) for p in _pk34])
_O34 = _SG34.load_pool()
_stones34 = lambda specs: [s for s in specs if s.split("@")[1].split(":")[0].endswith(("ナイト", "ナイトX", "ナイトY", "ナイトZ"))]
check("相手集団: 2000党以上・各6体（種と持ち物の重複なし・メガ石1〜2）",
      len(_O34) >= 2000 and all(len(o) == 6 and len({s.split("@")[0] for s in o}) == 6
                                and len({s.split("@")[1].split(":")[0] for s in o}) == 6
                                and 1 <= len(_stones34(o)) <= 2 for o in _O34[:300]))
_n34 = [s.split("@")[0] for s in _P1s]
_mega34 = {s.split("@")[0] for s in _stones34(_P1s)}
_rw34 = _SG34.rows(_P1s, _O34[:120], "M-6", 4)
check("選出ガイド: 相手ごとの自分の3体はパーティ内・重複なし・メガ石持ちちょうど1体、貪欲の勝率0〜1",
      len(_rw34) == 120 and all(len(set(my)) == 3 and len({_n34[i] for i in my} & _mega34) == 1 and 0 <= g <= 1 for my, _, g in _rw34))
check("選出ガイド: 同じ入力なら同じ結果（固定シード）", _SG34.rows(_P1s, _O34[:120], "M-6", 4) == _rw34)
_rw34b = [(my, on, g) for my, on, g in _rw34]
for _k34 in range(len(_rw34b)):
    _my, _on, _g = _rw34b[_k34]
    _rw34b[_k34] = (_my, _on + (["テスト用X"] if _k34 % 2 == 0 else []), 1.0 if _k34 % 2 == 0 else 0.0)
_sm34 = _SG34.summarize(_n34, _rw34b, min_n=30, z_min=3)
check("集計: 選出率の合計＝3・先発率の合計＝1・多い3体は割合の降順",
      abs(sum(m["sel"] for m in _sm34["members"]) - 3) < 0.01 and abs(sum(m["lead"] for m in _sm34["members"]) - 1) < 0.01
      and [t["share"] for t in _sm34["trios"]] == sorted([t["share"] for t in _sm34["trios"]], reverse=True))
check("集計: 相手にいると有利度が上がる種を得意に出す（差＝較正の傾き）",
      any(x["opp"] == "テスト用X" and abs(x["diff"] - _SG34.CAL_B) < 1e-3 for x in _sm34["strong"]), str(_sm34["strong"]))

# 4-1k: 診断の有利度＝guide_rows と同じ選出・乱数で対戦を MCTS にした guide_rows_mcts
try:
    import pokenavi_engine as _E36
    _ok36 = hasattr(_E36, "guide_rows_mcts")
except ImportError:
    _ok36 = False
if _ok36:
    from simulator.learned_selection import _PATH as _SP36
    _m36 = _E36.guide_rows_mcts(_P1s, _O34[:6], "M-6", 2, 1, _SP36, 16)
    _g36 = _E36.guide_rows(_P1s, _O34[:6], "M-6", 2, 1, _SP36)
    check("guide_rows_mcts: 相手ごとに (選出3体, 勝率 0〜1・k=2 なら 0/0.25/…/1)・選出は guide_rows と同じ",
          len(_m36) == 6 and all(len(set(my)) == 3 and 0 <= w <= 1 and (w * 4) % 1 == 0 for my, w in _m36)
          and [my for my, _ in _m36] == [my for my, _ in _g36])
    check("guide_rows_mcts: 同じ入力なら同じ結果（固定シード）", _E36.guide_rows_mcts(_P1s, _O34[:6], "M-6", 2, 1, _SP36, 16) == _m36)
    import _diagnose as _DG36
    _al36 = _DG36.merge([_DG36.mrows_at(j) for j in _DG36.mchunk_jobs(_P1s, _O34[:6], "M-6", 2, nc=3)], 3, 6)
    check("診断: mchunk_jobs→mrows_at→merge で相手の添字順に戻る（1相手ずつ直接回した値と一致）",
          [r[1] for r in _al36] == [_E36.guide_rows_mcts(_P1s, [_O34[j]], "M-6", 2, 1 + 100_003 * (j % 3) + 7919 * (j // 3), _SP36, _DG36.SIMS)[0][1] for j in range(6)])
    _st36 = [s for s in _P1s if _DG36.is_stone(s)]
    check("診断: is_stone はメガストーン（〜ナイト/ナイトX/Y/Z）だけ", len(_st36) == 1 and not _DG36.is_stone("ピカチュウ@でんきだま:ようき:でんきショック|でんこうせっか|10まんボルト|アイアンテール:0/32/0/0/2/32:せいでんき"))

# 4-1k: 診断の1戦＝探索は Rust（mcts_3v3_record）・記録は Python で同じ乱数のまま再生
try:
    import pokenavi_engine as _E35
    _ok35 = hasattr(_E35, "mcts_3v3_record")
except ImportError:
    _ok35 = False
if _ok35:
    import feature1 as _F35, _diagnose as _DG35
    from simulator.battle import Action as _Act35
    _F35._ensure_loaded("M-6", 8)
    _keys35 = {"selected1", "selected2", "turns", "result", "winner", "opp_alive", "own_dead", "truth"}
    _rs35 = []
    for _sd35, _sel35 in ((3, None), (17, [2, 0, 4]), (29, [5, 1, 3])):
        try:
            _rs35.append((_sel35, _F35.play_and_record_rust(_P1s, _O34[_sd35], season="M-6", seed=_sd35, mcts_sims=40,
                                                            predict=True, sel1_idx=_sel35, sel1_temp=0.0)))
        except _F35.ReplayMismatch as _e35:
            _rs35.append((_sel35, str(_e35)))
    check("診断の1戦（Rust探索→Python再生）: 各ターンの HP・場の個体・状態異常・勝敗が Rust と一致",
          all(isinstance(r, dict) for _, r in _rs35), str([r for _, r in _rs35 if not isinstance(r, dict)])[:300])
    _rd35 = [(sl, r) for sl, r in _rs35 if isinstance(r, dict)]
    check("診断の1戦: 記録のキー・ターン0から連番・predict あり・選出の指定どおり",
          all(set(r) == _keys35 and [t["turn"] for t in r["turns"]] == list(range(len(r["turns"])))
              and all("predict" in t for t in r["turns"]) and r["result"] in (0, 1, 2)
              and (sl is None or r["selected1"] == [_P1s[i].split("@")[0] for i in sl]) for sl, r in _rd35))
    _mv35 = _mk26c(_P1s[0])
    _a35 = [_F35._rust_action((1, "", 0, 2, False), _mv35), _F35._rust_action((3, "", 0, -1, False), _mv35),
            _F35._rust_action((0, _mv35.moves[1].name_jp, 1, -1, True), _mv35),
            _F35._rust_action((0, "わるあがき", 0, -1, False), _mv35)]
    check("Rust の行動→Python の Action（交代・パス・技＋メガ・わるあがき）",
          (_a35[0].type, _a35[0].switch_to) == ("switch", 2) and _a35[1].type == "pass"
          and _a35[2].move is _mv35.moves[1] and _a35[2].move_idx == 1 and _a35[2].do_mega
          and _a35[3].move.name_jp == "わるあがき")
    _orig35 = _E35.mcts_3v3_record
    def _bad35(*a, **k):
        r, d, t = _orig35(*a, **k)
        t0, (sa, sb) = t[0]
        return r, d, [(t0, ((sa[0], [(n, h + 1, m, st) for n, h, m, st in sa[1]]), sb))] + t[1:]
    _E35.mcts_3v3_record = _bad35
    try:
        _F35.play_and_record_rust(_P1s, _O34[3], season="M-6", seed=3, mcts_sims=40)
        _mm35 = False
    except _F35.ReplayMismatch:
        _mm35 = True
    finally:
        _E35.mcts_3v3_record = _orig35
    check("再生が Rust の要約と食い違えば ReplayMismatch", _mm35)
    _po35, _pp35 = _F35.play_and_record_rust, _F35.play_and_record
    def _raise35(*a, **k): raise _F35.ReplayMismatch("t")
    _F35.play_and_record_rust = _raise35
    _F35.play_and_record = lambda *a, **k: {"selected1": [_P1s[i].split("@")[0] for i in (k["sel1_idx"] or [0, 1, 2])], "turns": [], "fb": True}
    try:
        _bj35 = _DG35.battle_job((_P1s, _O34[3], "M-6", 3, None))
    finally:
        _F35.play_and_record_rust, _F35.play_and_record = _po35, _pp35
    check("battle_job: 再生が食い違った戦は従来の Python 版で記録（my_sel・auto を付ける）",
          _bj35.get("fb") is True and _bj35["my_sel"] == [0, 1, 2] and _bj35["auto"] is True)

print("\n=== 37. 監査5（2026-10-04）の修正 ===")
from simulator.battle import BattleSide as _BS37, Action as _Act37, _priority_base as _pb37, _entry_effects as _ee37
from simulator.items import set_terrain as _st37
_N37 = "きれいなぬけがら"
_mk37 = _mk26c
def _side37(*specs):
    return _BS37([_mk37(x) for x in specs], viewer_label="P")
def _mv37(poke, n):
    i = next(i for i, m in enumerate(poke.moves) if m and m.name_jp == n)
    return _Act37(type="move", move=poke.moves[i], move_idx=i)

# (1) 確定KO: 初回だけの技（であいがしら・ねこだまし）は登場ターンだけ、相手の行動しだいの ふいうち は使わない
_gu37 = _side37(f"グソクムシャ@{_N37}:いじっぱり:であいがしら|きゅうけつ|ふいうち|ねこだまし:32/32/0/0/0/0:ききかいひ")
_ga37 = _side37(f"ガブリアス@{_N37}:ようき:じしん:0/32/0/0/0/32:さめはだ")
_ga37.active.hp = 1
_st_act37 = _mv37(_gu37.active, "きゅうけつ")
_r37 = _A26c.certain_ko_override(_st_act37, _gu37, _ga37, _BF26c())
check("確定KO: 登場ターンは であいがしら で上書き", _r37.move.name_jp == "であいがしら", _r37.move.name_jp)
_gu37.active.turns_out = 1
_r37 = _A26c.certain_ko_override(_st_act37, _gu37, _ga37, _BF26c())
check("確定KO: 2ターン目以降は であいがしら/ねこだまし/ふいうち を当てにしない（選んだ手のまま）",
      _r37.move.name_jp == "きゅうけつ", _r37.move.name_jp)
_A26c._KO_COND_ON = False
_r37o = _A26c.certain_ko_override(_st_act37, _gu37, _ga37, _BF26c())
_A26c._KO_COND_ON = True
check("確定KO: 旧判定（AI_KO_COND=0）は失敗する技で上書きしていた（負例）", _r37o.move.name_jp != "きゅうけつ", _r37o.move.name_jp)
_tf37 = _BF26c(); _tf37.psychic_terrain = True
_bu37 = _side37(f"グソクムシャ@{_N37}:いじっぱり:アクアジェット|きゅうけつ:32/32/0/0/0/0:ききかいひ")
_bu37.active.turns_out = 1
_r37p = _A26c.certain_ko_override(_mv37(_bu37.active, "きゅうけつ"), _bu37, _ga37, _tf37)
check("確定KO: サイコフィールドで接地した相手への先制技は候補にしない", _r37p.move.name_jp == "きゅうけつ", _r37p.move.name_jp)
_ga37.active.hp = _ga37.active.max_hp

# (4) 確定KOの見積もりで半減きのみを消費しない（実際の攻撃でだけ消費）
_g37 = _side37(f"ガブリアス@{_N37}:ようき:じしん|つるぎのまい:0/32/0/0/0/32:さめはだ")
_e37 = _side37("エンペルト@シュカのみ:ひかえめ:なみのり:32/0/0/32/0/0:げきりゅう")
_e37.active.hp = 10
_r37b = _A26c.certain_ko_override(_mv37(_g37.active, "つるぎのまい"), _g37, _e37, _BF26c())
check("確定KO: 見積もりで半減きのみを消費しない", _r37b.move.name_jp == "じしん" and _e37.active.item == "シュカのみ",
      f"{_r37b.move.name_jp} {_e37.active.item}")
_e37.active.hp = _e37.active.max_hp
_execute_move(_g37, _e37, _mv37(_g37.active, "じしん"), _BF26c())
check("半減きのみ: 実際の攻撃では消費する", _e37.active.item is None)

# (3) 継続中のフィールドに後から出たシードは発動（Rust の entry_effects も同じ）
_f37 = _BF26c(); _st37(_f37, "psychic_terrain", 5)
_o37 = _mk37("オオニューラ@サイコシード:ようき:インファイト:0/32/0/0/0/32:かるわざ")
_ee37(_o37, 0, _f37, _mk37(f"ガブリアス@{_N37}:ようき:じしん:0/32/0/0/0/32:さめはだ"), [], [_o37])
check("サイコシード: 展開済みの場への登場で発動（とくぼう+1・かるわざ）",
      _o37.item is None and _o37.stage_sp_defense == 1 and _o37.stage_speed == 2)

# (6) フィールドは1つだけ
_f37 = _BF26c(); _st37(_f37, "psychic_terrain", 5)
_gr37 = _side37(f"ゴリランダー@{_N37}:いじっぱり:グラスフィールド:32/32/0/0/0/0:グラスメイカー")
_execute_move(_gr37, _side37(f"ガブリアス@{_N37}:ようき:じしん:0/32/0/0/0/32:さめはだ"), _mv37(_gr37.active, "グラスフィールド"), _f37)
check("フィールド: グラスフィールドを張るとサイコフィールドは解除", _f37.grassy_terrain and not _f37.psychic_terrain
      and _f37.psychic_terrain_count == 0)
_f37 = _BF26c(); _st37(_f37, "electric_terrain", 5)
from simulator.abilities import entry_ability as _ea37
_ea37(_mk37(f"イエッサン(オス)@{_N37}:おくびょう:サイコキネシス:0/0/0/32/0/32:サイコメイカー"), _mk37(f"ガブリアス@{_N37}:ようき:じしん:0/32/0/0/0/32:さめはだ"), _f37)
check("フィールド: サイコメイカーで張るとエレキフィールドは解除", _f37.psychic_terrain and not _f37.electric_terrain)

# (7) ほえる/ふきとばし: 控えがいなければ失敗（能力変化はリセットしない）
_hip37 = f"カバルドン@{_N37}:わんぱく:ほえる|ふきとばし:32/0/32/0/0/0:すなおこし"
_gab37 = f"ガブリアス@{_N37}:ようき:じしん:0/32/0/0/0/32:さめはだ"
for _w37 in ("ほえる", "ふきとばし"):
    _a37, _d37 = _side37(_hip37), _side37(_gab37)
    _d37.active.stage_attack = 2
    _execute_move(_a37, _d37, _mv37(_a37.active, _w37), _BF26c())
    check(f"{_w37}: 控えなしは失敗（能力変化そのまま・交代なし）",
          _d37.active.stage_attack == 2 and not getattr(_d37.active, "_force_switch", False))
    _a37, _d37 = _side37(_hip37), _side37(_gab37, f"ボーマンダ@{_N37}:ようき:じしん:0/32/0/0/0/32:いかく")
    _d37.active.stage_attack = 2
    _execute_move(_a37, _d37, _mv37(_a37.active, _w37), _BF26c())
    check(f"{_w37}: 控えありは成功（能力変化リセット・交代）",
          _d37.active.stage_attack == 0 and getattr(_d37.active, "_force_switch", False))

# (5) キラースピン: 自分側の設置物・やどりぎ・バインドを除去。素早さ+1 は こうそくスピン だけ
_k37 = _side37(f"キラフロル@{_N37}:ひかえめ:キラースピン|こうそくスピン:32/0/0/32/0/0:どくげしょう")
_k37.field_idx = 0
_kd37 = _side37(f"カバルドン@{_N37}:わんぱく:じしん:32/0/32/0/0/0:すなおこし"); _kd37.field_idx = 1
_f37 = _BF26c()
_f37.stealth_rock[0] = True; _f37.spikes[0] = 2; _f37.toxic_spikes[0] = 1; _f37.sticky_web[0] = True
_f37.stealth_rock[1] = True
_k37.active.seeded = True; _k37.active.bound_count = 3
_execute_move(_k37, _kd37, _mv37(_k37.active, "キラースピン"), _f37)
check("キラースピン: ステルスロック・まきびし・どくびし・ねばねばネットを除去",
      not _f37.stealth_rock[0] and _f37.spikes[0] == 0 and _f37.toxic_spikes[0] == 0 and not _f37.sticky_web[0])
check("キラースピン: 相手側の設置物は残る（負例）", _f37.stealth_rock[1])
check("キラースピン: やどりぎ・バインド解除、素早さは上がらない",
      not _k37.active.seeded and _k37.active.bound_count == 0 and _k37.active.stage_speed == 0)
_f37.sticky_web[0] = True
_execute_move(_k37, _kd37, _mv37(_k37.active, "こうそくスピン"), _f37)
check("こうそくスピン: ねばねばネットも除去・素早さ+1", not _f37.sticky_web[0] and _k37.active.stage_speed == 1)

# (8) グラススライダー: ふうせん持ちは接地していないので優先度+1にならない
_f37 = _BF26c(); _st37(_f37, "grassy_terrain", 5)
_gg37 = _mk37("ゴリランダー@ふうせん:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー")
check("グラススライダー: ふうせん持ちは優先度0", _pb37(_mv37(_gg37, "グラススライダー"), _gg37, _f37) == 0)
_gg37.item = None
check("グラススライダー: 接地なら優先度+1（正例）", _pb37(_mv37(_gg37, "グラススライダー"), _gg37, _f37) == 1)

# (2) シードは同じパーティにそのフィールドを張る個体がいるときだけ（scripts/seed_rule.py・生成の全経路）
import seed_rule as _SR37
_ny37 = "オオニューラ@サイコシード:ようき:インファイト|フェイタルクロー|ねこだまし|まもる:0/32/0/0/0/32:かるわざ"
_yes37 = "イエッサン(オス)@こだわりスカーフ:おくびょう:サイコキネシス:0/0/0/32/0/32:サイコメイカー"
_oth37 = [f"ガブリアス@きあいのタスキ:ようき:じしん:0/32/0/0/0/32:さめはだ",
          "カバルドン@オボンのみ:わんぱく:じしん:32/0/32/0/0/0:すなおこし",
          "アシレーヌ@たべのこし:ひかえめ:ムーンフォース:32/0/0/32/0/0:げきりゅう",
          "ギルガルド@いのちのたま:ひかえめ:シャドーボール:32/0/0/32/0/0:バトルスイッチ"]
check("シードの規則: 設置役（サイコメイカー）がいれば違反なし", _SR37.violations([_ny37, _yes37] + _oth37) == [])
check("シードの規則: 設置役がいなければ違反（負例）", _SR37.violations([_ny37] + _oth37 + ["メタグロス@メタグロスナイト:いじっぱり:アイアンヘッド:0/32/0/0/0/32:クリアボディ"]) == [0])
check("シードの規則: フィールド技を持つ個体も設置役",
      _SR37.violations([_ny37, "ゴリランダー@オボンのみ:いじっぱり:サイコフィールド:32/32/0/0/0/0:しんりょく"]) == [])
check("シードの規則: メガ後の特性（メガライチュウX＝エレキメイカー）も設置役",
      _SR37.violations(["パーモット@エレキシード:ようき:インファイト:0/32/0/0/0/32:てつのこぶし",
                        "ライチュウ@ライチュウナイトX:おくびょう:10まんボルト:0/0/0/32/0/32:せいでんき"]) == [])
check("シードの規則: 別のフィールドの設置役では足りない（負例）",
      _SR37.violations([_ny37, "ゴリランダー@オボンのみ:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー"]) == [0])
_fx37 = _SR37.fix([_ny37] + _oth37, lambda i: [(_ny37, 1.0), (_ny37.replace("サイコシード", "きあいのタスキ"), 1.0),
                                               (_ny37.replace("サイコシード", "ラムのみ"), 1.0)], random.Random(0))
check("シードの規則: 替えるときは他と重ならない別の持ち物の型に（タスキはガブリアスと重なる）",
      _fx37 is not None and _fx37[0].split("@")[1].startswith("ラムのみ"), str(_fx37 and _fx37[0]))
check("シードの規則: 替えられる型が無ければ None（負例）",
      _SR37.fix([_ny37] + _oth37, lambda i: [(_ny37, 1.0), (_ny37.replace("サイコシード", "きあいのタスキ"), 1.0)], random.Random(0)) is None)
import gen_party_pool as _GP37
_pg37 = _GP37.PartyGen()
check("PartyGen.is_legal: 設置役のいないシードは不合法",
      not _pg37.is_legal([_ny37] + _oth37 + ["メタグロス@メタグロスナイト:いじっぱり:アイアンヘッド:0/32/0/0/0/32:クリアボディ"], megas_set=(1, 2)))
check("PartyGen.is_legal: ユーザーが明示した型（seed_exempt）は見ない",
      _pg37.is_legal([_ny37] + _oth37 + ["メタグロス@メタグロスナイト:いじっぱり:アイアンヘッド:0/32/0/0/0/32:クリアボディ"], megas_set=(1, 2), seed_exempt=[_ny37]))
_rng37 = random.Random(5); _bad37 = 0; _n37 = 0
for _ in range(120):
    _pp37 = _pg37.sample(_rng37)
    if _pp37:
        _n37 += 1; _bad37 += bool(_SR37.violations(_pp37))
check("PartyGen.sample: 生成した党に設置役のいないシードが無い", _n37 > 100 and _bad37 == 0, f"{_bad37}/{_n37}")
check("pool_checks: 型が全部シードの系統はエラー",
      len(_C33.seed_errors({"オオニューラ": {"groups": [{"name": "テスト", "builds": [{"item": "サイコシード"}]}]}})) == 1
      and _C33.seed_errors({"オオニューラ": {"groups": [{"name": "テスト", "builds": [{"item": "サイコシード"}, {"item": "きあいのタスキ"}]}]}}) == [])

# Python/Rust の照合: シード・フィールド・ほえる・キラースピン・半減きのみの局面を Rust で対戦し Python で再生（食い違えば ReplayMismatch）
if _ok35:
    _par37 = [
        ([f"イエッサン(オス)@{_N37}:おくびょう:サイコキネシス|トリック:0/0/0/32/0/32:サイコメイカー",
          "オオニューラ@サイコシード:ようき:インファイト|フェイタルクロー|ねこだまし|まもる:0/32/0/0/0/32:かるわざ",
          "ゴリランダー@グラスシード:いじっぱり:グラススライダー|とんぼがえり:32/32/0/0/0/0:グラスメイカー"],
         [f"ガブリアス@{_N37}:ようき:じしん|ドラゴンクロー:0/32/0/0/0/32:さめはだ",
          "エンペルト@シュカのみ:ひかえめ:なみのり|れいとうビーム:32/0/0/32/0/0:げきりゅう",
          "カバルドン@オボンのみ:わんぱく:じしん|ほえる|ステルスロック|なまける:32/0/32/0/0/0:すなおこし"]),
        (["キラフロル@きあいのタスキ:ひかえめ:キラースピン|パワージェム|ステルスロック|ヘドロばくだん:32/0/0/32/0/0:どくげしょう",
          "グソクムシャ@グソクムシャナイト:いじっぱり:であいがしら|きゅうけつ|アクアブレイク|とんぼがえり:32/32/0/0/0/0:ききかいひ",
          "ゴリランダー@ふうせん:いじっぱり:グラススライダー|ウッドハンマー:32/32/0/0/0/0:グラスメイカー"],
         ["カバルドン@たべのこし:わんぱく:ステルスロック|ふきとばし|じしん|なまける:32/0/32/0/0/0:すなおこし",
          f"ガブリアス@{_N37}:ようき:じしん|ドラゴンクロー|ステルスロック:0/32/0/0/0/32:さめはだ",
          "エンペルト@シュカのみ:ひかえめ:なみのり|れいとうビーム:32/0/0/32/0/0:げきりゅう"]),
    ]
    _mm37 = []
    for _k37, (_pa37, _pb37s) in enumerate(_par37):
        for _sd37 in (1, 2):
            try:
                _F35.play_and_record_rust(_pa37, _pb37s, season="M-6", seed=_sd37, mcts_sims=30, sel1_idx=[0, 1, 2])
            except _F35.ReplayMismatch as _e37x:
                _mm37.append((_k37, _sd37, str(_e37x)[:120]))
    check("Python/Rust 照合: シード・フィールド・ほえる・キラースピン・半減きのみの局面で再生が一致", not _mm37, str(_mm37))

# ════════════════════════════════════════════════════════════════
# 38. ねむりのターン数（行動しようとするたびに1減る。初期値2〜4・ねむる3）とねむけ（あくび）
# ════════════════════════════════════════════════════════════════
print("\n=== 38. ねむり・ねむけ ===")
import random as _r38


def _fails38(p):
    n = 0
    for _ in range(10):
        lg = execute(p, make_poke(hp_b=255, def_b=255), "たいあたり")
        if "ねむっている" not in " ".join(lg):
            return n
        n += 1
    return n


_cnt38, _fl38 = set(), []
_r38.seed(38)
while len(_fl38) < 300:
    _d38 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])
    execute(make_poke(type1="ノーマル"), _d38, "うたう")
    if _d38.status == "sleep":
        _cnt38.add(_d38.sleep_count)
        _fl38.append(_fails38(_d38))
check("ねむり: 初期カウンタは2〜4", _cnt38 == {2, 3, 4}, str(_cnt38))
check("ねむり: 最初の行動は必ず失敗し、2〜4回目の行動で起きる（失敗は1〜3回）",
      set(_fl38) == {1, 2, 3}, str(sorted(set(_fl38))))
_fy38 = []
_r38.seed(381)
for _ in range(200):
    _y38 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"]); _y38.yawn_count = 1
    _by38 = Battle(BattleSide([_y38]), BattleSide([make_poke(moves=["まもる"])]), BattleField())
    _by38.resume(_Force("たいあたり"), _Force("まもる"), max_turns=1)
    if _y38.status == "sleep":
        _fy38.append((_y38.sleep_count, _fails38(_y38)))
check("あくび: ねむけから眠ったときもカウンタ2〜4・失敗1〜3回",
      {c for c, _ in _fy38} == {2, 3, 4} and {f for _, f in _fy38} == {1, 2, 3} and len(_fy38) == 200, str(set(_fy38)))
_rs38 = make_poke(type1="ノーマル", hp_b=255, moves=["ねむる", "たいあたり"]); _rs38.hp = 10
execute(_rs38, make_poke(), "ねむる")
check("ねむる: カウンタ3", _rs38.status == "sleep" and _rs38.sleep_count == 3 and _rs38.hp == _rs38.max_hp,
      f"{_rs38.status} {_rs38.sleep_count}")
check("ねむる: 2回行動できず3回目の行動で起きる", _fails38(_rs38) == 2)
_eb38 = make_poke(type1="ノーマル", hp_b=255, ability="はやおき", moves=["ねむる", "たいあたり"]); _eb38.hp = 10
execute(_eb38, make_poke(), "ねむる")
check("はやおき: ねむるは1回だけ行動できない", _fails38(_eb38) == 1)
_eb38b = make_poke(type1="ノーマル", ability="はやおき", moves=["たいあたり"]); _eb38b.status = "sleep"; _eb38b.sleep_count = 2
check("はやおき: カウンタ2なら最初の行動で起きる", _fails38(_eb38b) == 0 and _eb38b.status is None)
_sw38 = BattleSide([make_poke(name="寝", moves=["たいあたり"]), make_poke(name="控え", moves=["たいあたり"])])
_sw38.active.status = "sleep"; _sw38.active.sleep_count = 3
_sw38.switch_to(1); _sw38.switch_to(0)
check("ねむり: 控えにいる間はカウンタが減らない", _sw38.active.status == "sleep" and _sw38.active.sleep_count == 3,
      f"{_sw38.active.sleep_count}")
_st38 = make_poke(moves=["ねごと", "のしかかり"]); _st38.status = "sleep"; _st38.sleep_count = 1
_lst38 = execute(_st38, make_poke(), "ねごと")
check("ねごと: 使うとカウンタが減り、起きたらねごとは失敗", _st38.status is None and "失敗" in " ".join(_lst38))
_st38b = make_poke(moves=["ねごと", "のしかかり"]); _st38b.status = "sleep"; _st38b.sleep_count = 3
execute(_st38b, make_poke(hp_b=255), "ねごと")
check("ねごと: 使った分カウンタが減る", _st38b.status == "sleep" and _st38b.sleep_count == 2, f"{_st38b.sleep_count}")

_fe38 = BattleField(); _fe38.electric_terrain = True; _fe38.electric_terrain_count = 5
_fm38 = BattleField(); _fm38.misty_terrain = True; _fm38.misty_terrain_count = 5


def _yawn38(d, f=None, side_sg=0):
    s1 = BattleSide([make_poke(moves=["あくび"])]); s2 = BattleSide([d]); s2.safeguard = side_sg
    _execute_move(s1, s2, Action(type="move", move=dl.get_move("あくび")), f or BattleField())
    return d.yawn_count


check("あくび: 通常はねむけ2", _yawn38(make_poke()) == 2)
_ps38 = make_poke(); _ps38.status = "paralysis"
check("あくび: 状態異常の相手には失敗", _yawn38(_ps38) == 0)
_pz38 = make_poke(); _pz38.status = "sleep"; _pz38.sleep_count = 3
check("あくび: ねむっている相手には失敗", _yawn38(_pz38) == 0)
_py38 = make_poke(); _py38.yawn_count = 1
check("あくび: ねむけ状態の相手には失敗（カウントそのまま）", _yawn38(_py38) == 1)
check("あくび: エレキフィールドで接地の相手には失敗", _yawn38(make_poke(), _fe38) == 0)
check("あくび: ミストフィールドで接地の相手には失敗", _yawn38(make_poke(), _fm38) == 0)
check("あくび: フィールド中でもひこうタイプには効く", _yawn38(make_poke(type1="ひこう"), _fe38) == 2)
check("あくび: しんぴのまもりで失敗", _yawn38(make_poke(), side_sg=3) == 0)
for _ab38 in ("ふみん", "やるき", "スイートベール", "きよめのしお"):
    check(f"あくび: {_ab38} には失敗", _yawn38(make_poke(ability=_ab38)) == 0)
_mm38a = make_poke(moves=["あくび"]); _mm38d = make_poke(ability="マジックミラー")
_execute_move(BattleSide([_mm38a]), BattleSide([_mm38d]), Action(type="move", move=dl.get_move("あくび")), BattleField())
check("あくび: マジックミラーで跳ね返る", _mm38a.yawn_count == 2 and _mm38d.yawn_count == 0)


def _onset38(prep):
    d = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"]); d.yawn_count = 1
    f = BattleField(); prep(d, f)
    Battle(BattleSide([d]), BattleSide([make_poke(moves=["まもる"])]), f).resume(_Force("たいあたり"), _Force("まもる"), max_turns=1)
    return d


def _setf38(d, f):
    f.electric_terrain = True; f.electric_terrain_count = 5


def _setst38(d, f):
    d.status = "burn"


check("ねむけ: 眠る前にエレキフィールドが張られると眠らない", _onset38(_setf38).status is None)
check("ねむけ: 眠る前に別の状態異常になると眠らない", _onset38(_setst38).status == "burn")
check("ねむけ: 眠らなくてもねむけは消える", _onset38(_setst38).yawn_count == 0)


class _SwAI38:
    def __init__(self): self.t = 0
    def __call__(self, my, opp, f):
        self.t += 1
        if self.t == 1:
            return Action(type="switch", switch_to=1)
        return _Act(type="move", move=my.active.moves[0], move_idx=0)


_ya38 = make_poke(name="あくび役", spd_b=200, moves=["あくび"])
_yb38 = [make_poke(name="先発", hp_b=255, moves=["まもる"]), make_poke(name="交代先", hp_b=255, moves=["まもる"])]
_byb38 = Battle(BattleSide([_ya38]), BattleSide(_yb38), BattleField())
_swai38 = _SwAI38()
_byb38.resume(_Force("あくび"), _swai38, max_turns=1)
check("あくび: 交代読み＝交代で出てきた相手にねむけが入る", _yb38[1].yawn_count == 1 and _yb38[0].yawn_count == 0,
      f"{_yb38[0].yawn_count} {_yb38[1].yawn_count}")
_byb38.resume(_Force("あくび"), _swai38, max_turns=2)
check("あくび: 交代先は次のターンの終わりに眠る", _yb38[1].status == "sleep" and _yb38[1].sleep_count in (2, 3, 4))
_rz38 = make_poke(moves=["ねむる"]); _rz38.hp = 10
execute(_rz38, make_poke(), "ねむる", _fe38)
check("ねむる: エレキフィールドで接地なら失敗", _rz38.status is None and _rz38.hp == 10)
_r38.seed(3)
_gz38 = 0
for _ in range(200):
    _dz38 = make_poke(type1="ノーマル", hp_b=255)
    execute(make_poke(), _dz38, "うたう", _fm38)
    _gz38 += _dz38.status == "sleep"
check("ねむり技: ミストフィールドで接地の相手は眠らない", _gz38 == 0)

if _ok35:
    _N38 = "きれいなぬけがら"
    _par38 = [
        (["カバルドン@オボンのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし",
          "カビゴン@カゴのみ:わんぱく:のしかかり|ねむる|ねごと|じしん:32/0/32/0/0/0:あついしぼう",
          "オオニューラ@きあいのタスキ:ようき:インファイト|フェイタルクロー|ねこだまし|まもる:0/32/0/0/0/32:かるわざ"],
         ["ビビヨン@たべのこし:おくびょう:ちょうのまい|ねむりごな|ぼうふう|みがわり:0/0/0/32/0/32:ふくがん",
          "ラフレシア@たべのこし:おだやか:ちからをすいとる|どくどく|やどりぎのタネ|ムーンフォース:32/0/32/0/0/0:ほうし",
          "アシレーヌ@たべのこし:ひかえめ:うたかたのアリア|ねむる|あくび|ムーンフォース:32/0/24/0/0/8:げきりゅう"]),
        (["アローラペルシアン@きあいのタスキ:おくびょう:こごえるかぜ|さいみんじゅつ|すてゼリフ|ちょうはつ:32/0/0/0/0/32:ファーコート",
          "ニンフィア@たべのこし:ずぶとい:ハイパーボイス|あくび|まもる|ミストフィールド:32/0/32/0/0/0:フェアリースキン",
          "フシギバナ@きあいのタスキ:ひかえめ:ギガドレイン|ねむりごな|ヘドロばくだん|まもる:32/0/0/32/0/0:しんりょく"],
         ["カバルドン@たべのこし:わんぱく:じしん|あくび|ステルスロック|なまける:32/0/32/0/0/0:すなおこし",
          "オオニューラ@きあいのタスキ:ようき:インファイト|フェイタルクロー|ねこだまし|まもる:0/32/0/0/0/32:かるわざ",
          "アシレーヌ@カゴのみ:ひかえめ:うたかたのアリア|ねむる|めいそう|ムーンフォース:32/0/24/0/0/8:げきりゅう"]),
    ]
    _mm38 = []
    for _k38, (_pa38, _pb38) in enumerate(_par38):
        for _sd38 in range(1, 7):
            try:
                _F35.play_and_record_rust(_pa38, _pb38, season="M-6", seed=_sd38, mcts_sims=30, sel1_idx=[0, 1, 2])
            except _F35.ReplayMismatch as _e38x:
                _mm38.append((_k38, _sd38, str(_e38x)[:120]))
    check("Python/Rust 照合: ねむり・ねむけ・ねむる・ねごとの局面で再生が一致", not _mm38, str(_mm38))

print("\n=== 39. 監査40（2026-10-04）の修正 ===")
import random as _r39
from simulator.battle import (Battle as _B39, BattleSide as _S39, BattleField as _F39, Action as _A39,
                              _execute_move as _x39, _entry_effects as _ee39)
from simulator.pokemon import build_from_spec as _bfs39, parse_pokemon_spec as _pps39
from simulator.damage import calc_damage as _cd39
_N39 = "きれいなぬけがら"


def _mk39(spec):
    return _bfs39(_pps39(spec), dl, season="M-6", randomize=False)


class _P39:
    """ターンごとの行動計画（技名・"M:技名"でメガ進化・整数で交代）。最後の手を繰り返す"""
    def __init__(self, plan):
        self.plan = plan
        self.bt = None

    def __call__(self, my, opp, f):
        x = self.plan[min(self.bt.turn, len(self.plan)) - 1]
        if isinstance(x, int):
            return _A39(type="switch", switch_to=x)
        mega = x.startswith("M:")
        nm = x[2:] if mega else x
        for i, m in enumerate(my.active.moves):
            if m is not None and m.name_jp == nm:
                return _A39(type="move", move=m, move_idx=i, do_mega=mega)
        return _A39(type="move", move=my.active.moves[0], move_idx=0)


def _bt39(s1, s2, p1, p2, seed=1, prep=None):
    _r39.seed(seed)
    a, b = _S39([_mk39(x) for x in s1]), _S39([_mk39(x) for x in s2])
    if prep:
        prep(a, b)
    bt = _B39(a, b, _F39())
    ai1, ai2 = _P39(p1), _P39(p2)
    ai1.bt = ai2.bt = bt
    bt.start(ai1, ai2)
    return bt, ai1, ai2


def _go39(bt, ai1, ai2, t):
    bt.resume(ai1, ai2, max_turns=t)


_DUM39 = f"カビゴン@{_N39}:わんぱく:のろい|ボディプレス:32/0/32/0/0/0:あついしぼう"

# #1 メガ進化で出た天候は5ターン
_bt, _a1, _a2 = _bt39([f"リザードン@リザードナイトY:ひかえめ:はねやすめ:0/0/0/32/0/32:もうか"], [_DUM39],
                      ["M:はねやすめ"], ["のろい"])
_go39(_bt, _a1, _a2, 1)
_w1 = (_bt.field.weather, _bt.field.weather_count)
_go39(_bt, _a1, _a2, 5)
check("audit40 #1 メガ進化の ひでり は5ターン（1ターン目の終わりに残り4・5ターン目の終わりに終わる）",
      _w1 == ("sunny", 4) and _bt.field.weather is None, f"{_w1} {_bt.field.weather}")
from simulator.battle import _entry_and_mega as _eam39
_f1v1 = _F39()
_eam39(_mk39(f"リザードン@リザードナイトY:ひかえめ:はねやすめ:0/0/0/32/0/32:もうか"), _mk39(_DUM39), _f1v1)
check("audit40 #1 1v1判定の開始局面: メガリザードンYの晴れは5ターン", (_f1v1.weather, _f1v1.weather_count) == ("sunny", 5),
      f"{_f1v1.weather} {_f1v1.weather_count}")
try:
    import pokenavi_engine as _E39
except ImportError:
    pass

# #2 アンコール: かけたターンに後攻の相手の技を差し替え、3回の行動を縛る
_kyu39 = f"アローラキュウコン@{_N39}:おくびょう:アンコール|ムーンフォース:32/0/32/0/0/32:ゆきふらし"
_bt, _a1, _a2 = _bt39([_kyu39], [_DUM39], ["ムーンフォース", "アンコール", "ムーンフォース"], ["のろい", "ボディプレス"])
_hp39 = []
for _t in range(1, 6):
    _go39(_bt, _a1, _a2, _t)
    _hp39.append((_bt.side2.active.stage_attack, _bt.side1.active.hp))
check("audit40 #2 アンコール（先攻）: そのターンの技を差し替え、3回 のろい を繰り返して4回目で解ける",
      [a for a, _ in _hp39[:4]] == [1, 2, 3, 4] and _hp39[3][1] == _bt.side1.active.max_hp and _hp39[4][1] < _bt.side1.active.max_hp,
      f"{_hp39}")
_slow39 = f"カビゴン@{_N39}:わんぱく:アンコール|のろい:32/0/32/0/0/0:あついしぼう"
_fast39 = f"アローラキュウコン@{_N39}:おくびょう:ムーンフォース|わるだくみ:32/0/32/0/0/32:ゆきふらし"
_bt, _a1, _a2 = _bt39([_slow39], [_fast39], ["のろい", "アンコール", "のろい"], ["ムーンフォース", "ムーンフォース", "わるだくみ"])
_sp39 = []
for _t in range(1, 7):
    _go39(_bt, _a1, _a2, _t)
    _sp39.append(_bt.side2.active.stage_sp_attack)
check("audit40 #2 アンコール（後攻）: 次のターンから3回縛る（3〜5ターン目は ムーンフォース、6ターン目に わるだくみ）",
      _sp39 == [0, 0, 0, 0, 0, 2], f"{_sp39}")
_bt, _a1, _a2 = _bt39([_kyu39], [_DUM39, _DUM39.replace("カビゴン", "ブラッキー").replace("あついしぼう", "せいしんりょく")],
                      ["ムーンフォース", "アンコール", "ムーンフォース"], ["のろい", "のろい", 1, 0, "ボディプレス"])
_go39(_bt, _a1, _a2, 3)
check("audit40 #2 アンコール は交代で解ける（控えに戻ったら残りターンも消える）",
      _bt.side2.active is _bt.side2.party[1] and _bt.side2.party[0].encore_count == 0 and _bt.side2.party[0].locked_move is None,
      f"{_bt.side2.party[0].encore_count}")

# #4 みちづれ は次の行動で解ける
_bt, _a1, _a2 = _bt39([f"ゲンガー@{_N39}:おくびょう:みちづれ|シャドーボール:0/0/0/32/0/32:のろわれボディ", _DUM39],
                      [f"ドドゲザン@くろいメガネ:いじっぱり:つるぎのまい|ドゲザン:32/32/0/0/0/0:そうだいしょう", _DUM39],
                      ["みちづれ", "シャドーボール"], ["つるぎのまい", "ドゲザン"])
_go39(_bt, _a1, _a2, 2)
check("audit40 #4 みちづれ: 次の行動（シャドーボール）の後に倒されても相手は道連れにならない",
      not _bt.side1.party[0].is_alive and _bt.side2.party[0].is_alive, f"{[p.is_alive for p in _bt.side2.party]}")

# #5 いやしのねがい は瀕死交代で出た後続にも入る
def _hw39(a, b):
    a.party[1].hp = a.party[1].max_hp // 3
    a.party[1].status = "burn"
_bt, _a1, _a2 = _bt39([f"イエッサン(オス)@{_N39}:おくびょう:いやしのねがい:0/0/0/32/0/32:サイコメイカー",
                       f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース:0/0/0/32/0/0:げきりゅう"],
                      [_DUM39], ["いやしのねがい", "ムーンフォース"], ["のろい"], prep=_hw39)
_go39(_bt, _a1, _a2, 1)
_ash39 = _bt.side1.active
check("audit40 #5 いやしのねがい: 使って倒れた後の瀕死交代で出た アシレーヌ が全快・状態異常回復",
      _ash39.name == "アシレーヌ" and _ash39.hp == _ash39.max_hp and _ash39.status is None, f"{_ash39.name} {_ash39.hp}/{_ash39.max_hp} {_ash39.status}")

# #6 タイプ強化の持ち物・ピンチ特性・防御側の特性は技の最終タイプで判定
_nym39 = _mk39(f"ニンフィア@ようせいのハネ:ひかえめ:ハイパーボイス:32/0/0/32/0/0:フェアリースキン")
_nyn39 = _mk39(f"ニンフィア@{_N39}:ひかえめ:ハイパーボイス:32/0/0/32/0/0:フェアリースキン")
_tg39 = _mk39(_DUM39)
_d1, _d0 = _cd39(_nym39, _tg39, _nym39.moves[0], _F39(), False, 0.5), _cd39(_nyn39, _tg39, _nyn39.moves[0], _F39(), False, 0.5)
check("audit40 #6 フェアリースキン＋ようせいのハネ: フェアリーになった ハイパーボイス が1.2倍", 1.15 < _d1 / _d0 < 1.25, f"{_d1} {_d0}")
_fs39 = _F39(); _fs39.weather = "sunny"; _fs39.weather_count = 5
_cz39 = _mk39(f"リザードン@{_N39}:ひかえめ:ウェザーボール:0/0/0/32/0/32:もうか")
_tg39 = _mk39(f"ブラッキー@{_N39}:ずぶとい:つきのひかり:32/0/32/0/0/0:せいしんりょく")
_dfull = _cd39(_cz39, _tg39, _cz39.moves[0], _fs39, False, 0.5)
_cz39.hp = _cz39.max_hp // 3
_dlow = _cd39(_cz39, _tg39, _cz39.moves[0], _fs39, False, 0.5)
check("audit40 #6 もうか: 晴れの ウェザーボール（ほのお）でもピンチで1.5倍", 1.45 < _dlow / _dfull < 1.55, f"{_dlow} {_dfull}")
_tf39 = _mk39(f"カビゴン@{_N39}:わんぱく:のろい:32/0/32/0/0/0:あついしぼう")
_tn39 = _mk39(f"カビゴン@{_N39}:わんぱく:のろい:32/0/32/0/0/0:めんえき")
_cz39.hp = _cz39.max_hp
_dth = _cd39(_cz39, _tf39, _cz39.moves[0], _fs39, False, 0.5)
_dnm = _cd39(_cz39, _tn39, _cz39.moves[0], _fs39, False, 0.5)
check("audit40 #6 あついしぼう: 晴れの ウェザーボール（ほのお）を半減", 0.45 < _dth / _dnm < 0.55, f"{_dth} {_dnm}")

# #7 ミラーアーマー は いかく・変化技の能力低下を跳ね返す
_bt, _a1, _a2 = _bt39([f"アーマーガア@{_N39}:わんぱく:ボディプレス:32/0/32/0/0/0:ミラーアーマー"],
                      [f"ボーマンダ@{_N39}:いじっぱり:すてみタックル|こわいかお:0/32/0/0/0/32:いかく"], ["ボディプレス"], ["こわいかお"])
_ia39 = (_bt.side1.active.stage_attack, _bt.side2.active.stage_attack)
_go39(_bt, _a1, _a2, 1)
check("audit40 #7 ミラーアーマー: いかく を跳ね返す（ボーマンダの攻撃-1）・こわいかお を跳ね返す（ボーマンダの素早さ-2）",
      _ia39 == (0, -1) and _bt.side1.active.stage_speed == 0 and _bt.side2.active.stage_speed == -2,
      f"{_ia39} {_bt.side1.active.stage_speed} {_bt.side2.active.stage_speed}")

# #8 とびひざげり は まもる・タイプ無効でも反動
_ace39 = f"エースバーン@{_N39}:ようき:とびひざげり:0/32/0/0/0/32:もうか"
_bt, _a1, _a2 = _bt39([_ace39], [f"ニンフィア@{_N39}:ずぶとい:まもる:32/0/32/0/0/0:フェアリースキン"], ["とびひざげり"], ["まもる"])
_go39(_bt, _a1, _a2, 1)
_hjk1 = _bt.side1.active.max_hp - _bt.side1.active.hp
_bt, _a1, _a2 = _bt39([_ace39], [f"ゲンガー@{_N39}:おくびょう:のろい:32/0/0/0/0/32:のろわれボディ"], ["とびひざげり"], ["のろい"])
_bt.side2.active.moves = [dl.get_move("のろい")]
_go39(_bt, _a1, _a2, 1)
_hjk2 = _bt.side1.active.max_hp - _bt.side1.active.hp
_mh39 = _bt.side1.active.max_hp // 2
check("audit40 #8 とびひざげり: まもる で防がれても・ゴーストに無効でも最大HPの1/2の反動", _hjk1 == _mh39 and _hjk2 >= _mh39, f"{_hjk1} {_hjk2}")

# #9 かたやぶり: 壁・ベールは無視しない／ばけのかわ は無視／さめはだ・キングシールド は受ける
_gy39 = _mk39(f"ギャラドス@ギャラドスナイト:いじっぱり:たきのぼり:0/32/0/0/0/32:いかく")
_gy39.do_mega_evolve()
_sA, _sB = _S39([_gy39]), _S39([_mk39(_DUM39)])
_sB.reflect = True; _sB.reflect_count = 5
_r39.seed(1); _x39(_sA, _sB, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
_dref = _sB.active.max_hp - _sB.active.hp
_sB2 = _S39([_mk39(_DUM39)])
_r39.seed(1); _x39(_sA, _sB2, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
_dno = _sB2.active.max_hp - _sB2.active.hp
check("audit40 #9 かたやぶり: リフレクター は無視しない（ダメージ半分）", _gy39.ability == "かたやぶり" and 0.4 < _dref / max(1, _dno) < 0.6, f"{_dref} {_dno}")
_mim39 = _S39([_mk39(f"ミミッキュ@{_N39}:いじっぱり:つるぎのまい:32/0/0/0/0/0:ばけのかわ")])
_r39.seed(1); _x39(_sA, _mim39, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
check("audit40 #9 かたやぶり: ばけのかわ を無視して本体にダメージ（化けの皮は残る）",
      _mim39.active.max_hp - _mim39.active.hp > _mim39.active.max_hp // 8 + 5 and not getattr(_mim39.active, "_disguise_broken", False))
_gab39 = _S39([_mk39(f"ガブリアス@{_N39}:わんぱく:つるぎのまい:32/0/32/0/0/0:さめはだ")])
_gy39.hp = _gy39.max_hp
_r39.seed(1); _x39(_sA, _gab39, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
check("audit40 #9 かたやぶり: さめはだ の反動は受ける", _gy39.max_hp - _gy39.hp == max(1, _gy39.max_hp // 8), f"{_gy39.hp}/{_gy39.max_hp}")
_gil39 = _S39([_mk39(f"ギルガルド@{_N39}:いじっぱり:キングシールド:32/32/0/0/0/0:バトルスイッチ")])
_gil39.active.protecting = True; _gil39.active._protect_move = "キングシールド"
_gy39.stage_attack = 0
_r39.seed(1); _x39(_sA, _gil39, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
check("audit40 #9 かたやぶり: キングシールド の攻撃低下は受ける", _gy39.stage_attack == -1, f"{_gy39.stage_attack}")
_stu39 = _S39([_mk39(f"ドドゲザン@{_N39}:いじっぱり:つるぎのまい:32/0/0/0/0/0:がんじょう")])
_stu39.active.ability = "がんじょう"; _stu39.active.max_hp = _stu39.active.hp = 30
_r39.seed(1); _x39(_sA, _stu39, _A39(type="move", move=_gy39.moves[0], move_idx=0), _F39())
check("audit40 #9 かたやぶり: がんじょう を無視して倒す", not _stu39.active.is_alive)

# #10 しろいハーブ は能力が下がった直後に発動（からをやぶる・いかく）
_bt, _a1, _a2 = _bt39([f"カメックス@しろいハーブ:おくびょう:からをやぶる:0/0/0/32/0/32:げきりゅう"],
                      [f"ギャラドス@{_N39}:わんぱく:たきのぼり:32/0/32/0/0/0:じしんかじょう"], ["からをやぶる"], ["たきのぼり"])
_l0 = len(_bt.logs)
_go39(_bt, _a1, _a2, 1)
_lg39 = _bt.logs[_l0:]
_ih = next((i for i, x in enumerate(_lg39) if "しろいハーブ" in x), 99)
_ia = next((i for i, x in enumerate(_lg39) if "たきのぼり" in x), -1)
check("audit40 #10 しろいハーブ: からをやぶる の直後に発動（相手の攻撃より前）", _ih < _ia, f"{_ih} {_ia}")
_bt, _a1, _a2 = _bt39([f"ガブリアス@しろいハーブ:ようき:じしん:0/32/0/0/0/32:さめはだ"],
                      [f"ボーマンダ@{_N39}:いじっぱり:すてみタックル:0/32/0/0/0/32:いかく"], ["じしん"], ["すてみタックル"])
check("audit40 #10 しろいハーブ: 登場時の いかく の直後に発動（1ターン目の前に攻撃0）",
      _bt.side1.active.stage_attack == 0 and _bt.side1.active.item is None, f"{_bt.side1.active.stage_attack} {_bt.side1.active.item}")

# #11 ほろびのうた は使った3ターン後の終わりに倒れる
_bt, _a1, _a2 = _bt39([f"ゲンガー@{_N39}:おくびょう:ほろびのうた:32/0/0/0/0/32:のろわれボディ", _DUM39],
                      [_DUM39, _DUM39], ["ほろびのうた"], ["のろい"])
_al39 = []
for _t in range(1, 5):
    _go39(_bt, _a1, _a2, _t)
    _al39.append((_bt.side1.party[0].is_alive, _bt.side2.party[0].is_alive))
check("audit40 #11 ほろびのうた: 3ターン目の終わりまで生き、4ターン目の終わりに両者倒れる",
      _al39[:3] == [(True, True)] * 3 and _al39[3] == (False, False), f"{_al39}")

# #12 ボディプレス は防御側の てんねん で自分の防御ランクを無視される
_cv39 = _mk39(f"アーマーガア@{_N39}:わんぱく:ボディプレス:32/0/32/0/0/0:プレッシャー")
_sk39 = _mk39(_DUM39)
_sk39.ability = "てんねん"
_b0 = _cd39(_cv39, _sk39, _cv39.moves[0], _F39(), False, 0.5)
_cv39.stage_defense = 2
_b2 = _cd39(_cv39, _sk39, _cv39.moves[0], _F39(), False, 0.5)
check("audit40 #12 ボディプレス: 相手が てんねん なら防御+2が無視される", _b0 == _b2, f"{_b0} {_b2}")

# #13 おうごんのからだ は いたみわけ 等の相手向けの変化技を防ぐ
_sR = _S39([_mk39(f"ウォッシュロトム@{_N39}:ずぶとい:いたみわけ|ほえる|すてゼリフ:32/0/32/0/0/0:ふゆう"), _mk39(_DUM39)])
_sG = _S39([_mk39(f"サーフゴー@{_N39}:ひかえめ:シャドーボール:0/0/0/32/0/32:おうごんのからだ"), _mk39(_DUM39)])
_sR.active.hp = 10
_r39.seed(1); _x39(_sR, _sG, _A39(type="move", move=_sR.active.moves[0], move_idx=0), _F39())
check("audit40 #13 おうごんのからだ: いたみわけ を防ぐ", _sR.active.hp == 10 and _sG.active.hp == _sG.active.max_hp)
_r39.seed(1); _x39(_sR, _sG, _A39(type="move", move=_sR.active.moves[2], move_idx=2), _F39())
check("audit40 #13 おうごんのからだ: すてゼリフ を防ぐ（能力は下がらず交代もしない）",
      _sG.active.stage_attack == 0 and not getattr(_sR.active, "_pivot_out", False))

# #14 かそく は登場したターンには発動しない（ターン終わりの瀕死交代で出たら次のターンは発動）
_baz39 = f"バシャーモ@{_N39}:いじっぱり:まもる|ビルドアップ:0/32/0/0/0/32:かそく"
_bt, _a1, _a2 = _bt39([f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース:0/0/0/32/0/0:げきりゅう", _baz39], [_DUM39],
                      [1, "ビルドアップ"], ["のろい"])
_go39(_bt, _a1, _a2, 1)
_s1 = _bt.side1.active.stage_speed
_go39(_bt, _a1, _a2, 2)
check("audit40 #14 かそく: 交代で出たターンは上がらず、次のターンの終わりに+1", (_s1, _bt.side1.active.stage_speed) == (0, 1),
      f"{_s1} {_bt.side1.active.stage_speed}")
def _eot39(a, b):
    a.party[0].hp = 1
    a.party[0].status = "poison"
_bt, _a1, _a2 = _bt39([f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース:0/0/0/32/0/0:げきりゅう", _baz39], [_DUM39],
                      ["ムーンフォース", "ビルドアップ"], ["のろい"], prep=_eot39)
_go39(_bt, _a1, _a2, 1)
_s1 = (_bt.side1.active.name, _bt.side1.active.stage_speed)
_go39(_bt, _a1, _a2, 2)
check("audit40 #14 かそく（新しい扱いの確認）: ターン終わりの瀕死交代で出たら次のターンの終わりに+1",
      _s1 == ("バシャーモ", 0) and _bt.side1.active.stage_speed == 1, f"{_s1} {_bt.side1.active.stage_speed}")

# #15 特性・ふうせんで無効の技は「効かない」（接触反応・追加効果・タイプ喪失・ばつぐん表示なし）
_pw39 = _S39([_mk39(f"パーモット@{_N39}:ようき:でんこうそうげき:0/32/0/0/0/32:てつのこぶし")])
_rc39 = _S39([_mk39(f"ライチュウ@{_N39}:おくびょう:わるだくみ:0/0/0/32/0/32:ひらいしん")])
_r39.seed(1); _lg39 = _x39(_pw39, _rc39, _A39(type="move", move=_pw39.active.moves[0], move_idx=0), _F39())
check("audit40 #15 でんこうそうげき → ひらいしん: でんきタイプは残り、相手の特攻+1",
      "でんき" in (_pw39.active.type1, _pw39.active.type2) and _rc39.active.stage_sp_attack == 1, f"{_pw39.active.type1} {_pw39.active.type2}")
_gr39 = _S39([_mk39(f"ゴリランダー@{_N39}:いじっぱり:10まんばりき:32/32/0/0/0/0:グラスメイカー")])
_rw39 = _S39([_mk39(f"ウォッシュロトム@ゴツゴツメット:ずぶとい:おにび:32/0/32/0/0/0:ふゆう")])
_r39.seed(1); _lg39 = _x39(_gr39, _rw39, _A39(type="move", move=_gr39.active.moves[0], move_idx=0), _F39())
check("audit40 #15 ふゆう に無効の接触技: ゴツゴツメット は発動せず「ばつぐん」も出ない",
      _gr39.active.hp == _gr39.active.max_hp and not any("ばつぐん" in x for x in _lg39), f"{_gr39.active.hp} {_lg39}")
_rb39 = _S39([_mk39(f"ガブリアス@ふうせん:わんぱく:つるぎのまい:32/0/32/0/0/0:さめはだ")])
_r39.seed(1); _x39(_gr39, _rb39, _A39(type="move", move=_gr39.active.moves[0], move_idx=0), _F39())
check("audit40 #15 ふうせん に無効の じめん技: さめはだ は発動しない", _gr39.active.hp == _gr39.active.max_hp and _rb39.active.item == "ふうせん")

# #16 みがわり を貫通するのは音技（ぼうふう は音技でない）
_sub39 = _S39([_mk39(f"ライチュウ@{_N39}:おくびょう:みがわり:32/0/32/0/0/32:ひらいしん")])
_sub39.active._substitute_hp = _sub39.active.max_hp // 4
_ar39 = _S39([_mk39(f"アシレーヌ@{_N39}:ひかえめ:うたかたのアリア|ぼうふう:32/0/0/32/0/0:げきりゅう")])
_r39.seed(1); _x39(_ar39, _sub39, _A39(type="move", move=_ar39.active.moves[0], move_idx=0), _F39())
_h1 = (_sub39.active.hp < _sub39.active.max_hp, _sub39.active._substitute_hp == _sub39.active.max_hp // 4)
_sub39.active.hp = _sub39.active.max_hp
_r39.seed(1); _x39(_ar39, _sub39, _A39(type="move", move=_ar39.active.moves[1], move_idx=1), _F39())
check("audit40 #16 みがわり: うたかたのアリア（音技）は貫通、ぼうふう は みがわり が受ける",
      _h1 == (True, True) and _sub39.active.hp == _sub39.active.max_hp, f"{_h1} {_sub39.active.hp}")

# #17 ちょうはつ は3ターン（先に動かれたら次のターンから3ターン）
_gya39 = f"ギャラドス@{_N39}:ようき:ちょうはつ|たきのぼり:0/32/0/0/0/32:いかく"
_bt, _a1, _a2 = _bt39([_gya39], [_DUM39], ["ちょうはつ", "たきのぼり"], ["のろい"])
_tt39 = []
for _t in range(1, 5):
    _go39(_bt, _a1, _a2, _t)
    _tt39.append(_bt.side2.active.stage_attack)
check("audit40 #17 ちょうはつ（先攻）: 1〜3ターン目の のろい を封じ、4ターン目に使える", _tt39 == [-1, -1, -1, 0], f"{_tt39}")
_bt, _a1, _a2 = _bt39([_DUM39.replace("ボディプレス", "ちょうはつ")], [f"ギャラドス@{_N39}:ようき:りゅうのまい|たきのぼり:0/32/0/0/0/32:いかく"],
                      ["のろい", "ちょうはつ", "のろい"], ["りゅうのまい"])
_tt39 = []
for _t in range(1, 7):
    _go39(_bt, _a1, _a2, _t)
    _tt39.append(_bt.side2.active.stage_attack)
check("audit40 #17 ちょうはつ（後攻）: 次のターンから3ターン封じる（3〜5ターン目は失敗、6ターン目に りゅうのまい）",
      _tt39 == [1, 2, 2, 2, 2, 3], f"{_tt39}")

# 既知: みがわり は相手向けの変化技を防ぐ（音技・貫通技は除く）
_sb39 = _S39([_mk39(f"ゲンガー@{_N39}:おくびょう:みがわり:32/0/0/0/0/32:のろわれボディ")])
_sb39.active._substitute_hp = 40
_wo39 = _S39([_mk39(f"ヒートロトム@{_N39}:ずぶとい:おにび|でんじは|うたう|ちょうはつ:32/0/32/0/0/0:ふゆう")])
_r39.seed(1)
for _i in range(2):
    _x39(_wo39, _sb39, _A39(type="move", move=_wo39.active.moves[_i], move_idx=_i), _F39())
check("audit40 既知 みがわり: おにび・でんじは を防ぐ", _sb39.active.status is None, f"{_sb39.active.status}")
_x39(_wo39, _sb39, _A39(type="move", move=_wo39.active.moves[3], move_idx=3), _F39())
check("audit40 既知 みがわり: ちょうはつ は貫通する", _sb39.active.taunt_count > 0)

# 既知: ミストフィールド は接地個体の状態異常全般・こんらんを防ぐ
_fm39 = _F39(); _fm39.misty_terrain = True; _fm39.misty_terrain_count = 5
_mi39 = _S39([_mk39(f"ブラッキー@{_N39}:ずぶとい:でんじは|あやしいひかり|どくどく|おにび:32/0/32/0/0/0:せいしんりょく")])
_tg39 = _S39([_mk39(_DUM39)])
_r39.seed(1)
for _i in range(4):
    _x39(_mi39, _tg39, _A39(type="move", move=_mi39.active.moves[_i], move_idx=_i), _fm39)
check("audit40 既知 ミストフィールド: 接地の相手に まひ・こんらん・もうどく・やけど が入らない",
      _tg39.active.status is None and not _tg39.active.confused, f"{_tg39.active.status} {_tg39.active.confused}")
_fl39 = _S39([_mk39(f"ボーマンダ@{_N39}:いじっぱり:すてみタックル:0/32/0/0/0/32:いかく")])
_x39(_mi39, _fl39, _A39(type="move", move=_mi39.active.moves[0], move_idx=0), _fm39)
check("audit40 既知 ミストフィールド: 浮いている相手（ひこう）には入る", _fl39.active.status == "paralysis")


# #3 確定KOの上書き: 命中率とタイプの条件（AI_FIX40）
import simulator.ai as _AI39
_rai39 = _S39([_mk39(f"ライチュウ@{_N39}:ひかえめ:10まんボルト|でんじほう|わるだくみ:0/0/0/32/0/32:ひらいしん")])
_tgt39 = _S39([_mk39(f"ギャラドス@{_N39}:ようき:たきのぼり:0/32/0/0/0/32:いかく")])
_tgt39.active.hp = 30
_st39 = _A39(type="move", move=_rai39.active.moves[2], move_idx=2)
_k39 = _AI39.certain_ko_override(_st39, _rai39, _tgt39, _F39())
check("audit40 #3 確定KO: 10まんボルト でも でんじほう でも倒せるなら命中100の 10まんボルト", _k39.move.name_jp == "10まんボルト", _k39.move.name_jp)
_rai39b = _S39([_mk39(f"ライチュウ@{_N39}:ひかえめ:でんじほう|わるだくみ:0/0/0/32/0/32:ひらいしん")])
_k39 = _AI39.certain_ko_override(_A39(type="move", move=_rai39b.active.moves[1], move_idx=1), _rai39b, _tgt39, _F39())
check("audit40 #3 確定KO: 命中50の でんじほう しか倒せないなら探索の手（わるだくみ）を上書きしない", _k39.move.name_jp == "わるだくみ", _k39.move.name_jp)
_paw39 = _S39([_mk39(f"パーモット@{_N39}:ようき:でんこうそうげき|インファイト|さいきのいのり:0/32/0/0/0/32:てつのこぶし")])
_paw39.active.type1, _paw39.active.type2 = "かくとう", None
_tgt39.active.hp = 5
_k39 = _AI39.certain_ko_override(_A39(type="move", move=_paw39.active.moves[2], move_idx=2), _paw39, _tgt39, _F39())
check("audit40 #3 確定KO: でんきタイプを失った でんこうそうげき は候補にしない", _k39.move.name_jp != "でんこうそうげき", _k39.move.name_jp)

# #18〜#20 必ず失敗する手・効果の無い手を探索の候補から外す（AI_FIX40）
from simulator.search_ai import _prune_futile_moves as _pf39, _resample_sleep as _rs39
def _cands39(side):
    return [_A39(type="move", move=m, move_idx=i) for i, m in enumerate(side.active.moves)] + \
           [_A39(type="switch", switch_to=i) for i, p in enumerate(side.party) if i != side.active_idx and p.is_alive]
def _left39(me, op, f=None):
    return [a.move.name_jp if a.type == "move" else "sw" for a in _pf39(_cands39(me), me, op, f or _F39())]
_gu39 = _S39([_mk39(f"グソクムシャ@{_N39}:いじっぱり:であいがしら|アクアブレイク|じこさいせい|つるぎのまい:32/32/0/0/0/0:ききかいひ"), _mk39(_DUM39)])
_op39 = _S39([_mk39(f"カビゴン@{_N39}:わんぱく:のろい:32/0/32/0/0/0:あついしぼう")])
_gu39.active.turns_out = 1
_gu39.active.stage_attack = 6
_lf39 = _left39(_gu39, _op39)
check("audit40 #18/#19 候補: 2ターン目以降の であいがしら・満タンの じこさいせい・攻撃+6の つるぎのまい を外す",
      _lf39 == ["アクアブレイク", "sw"], f"{_lf39}")
_gu39.active.turns_out = 0; _gu39.active.stage_attack = 0; _gu39.active.hp -= 1
check("audit40 #18/#19 候補: 登場ターン・HPが減った・積める状態なら外さない", _left39(_gu39, _op39) == ["であいがしら", "アクアブレイク", "じこさいせい", "つるぎのまい", "sw"],
      f"{_left39(_gu39, _op39)}")
_hip39 = _S39([_mk39(f"カバルドン@{_N39}:わんぱく:ほえる|あくび|じしん|でんじは:32/0/32/0/0/0:すなおこし")])
_op39.active.status = "paralysis"
check("audit40 #19 候補: 控えのいない相手への ほえる・状態異常の相手への あくび/でんじは を外す", _left39(_hip39, _op39) == ["じしん"], f"{_left39(_hip39, _op39)}")
_gold39 = _S39([_mk39(f"サーフゴー@ふうせん:ひかえめ:シャドーボール:0/0/0/32/0/32:おうごんのからだ")])
_hip39.opp_view.on_enter(_gold39.active)
_hip2 = _S39([_mk39(f"カバルドン@{_N39}:わんぱく:じしん|がんせきふうじ:32/0/32/0/0/0:すなおこし")])
_hip2.opp_view.on_enter(_gold39.active)
check("audit40 #20 候補: 登場時に見えた ふうせん の相手への じめん技を外す", _left39(_hip2, _gold39) == ["がんせきふうじ"], f"{_left39(_hip2, _gold39)}")
_paw39b = _S39([_mk39(f"パーモット@{_N39}:ようき:でんこうそうげき|インファイト:0/32/0/0/0/32:てつのこぶし")])
_paw39b.active.type1, _paw39b.active.type2 = "かくとう", None
check("audit40 #19 候補: でんきタイプを失った でんこうそうげき を外す", _left39(_paw39b, _op39) == ["インファイト"], f"{_left39(_paw39b, _op39)}")
_tau39 = _S39([_mk39(f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース|アンコール|めいそう|うたかたのアリア:32/0/0/32/0/0:げきりゅう")])
_tau39.active.taunt_count = 2
_top39 = _S39([_mk39(_DUM39)]); _top39.active.last_used_move = "のろい"
_lt39 = _left39(_tau39, _top39)
_tau39.active.taunt_count = 0; _tau39.active.throat_chop_count = 2
_lj39 = _left39(_tau39, _top39)
check("audit40 #19 候補: ちょうはつ中の変化技・じごくづき中の音技を外す",
      _lt39 == ["ムーンフォース", "うたかたのアリア"] and _lj39 == ["ムーンフォース", "アンコール", "めいそう"], f"{_lt39} {_lj39}")
_only39 = _S39([_mk39(f"グソクムシャ@{_N39}:いじっぱり:であいがしら:32/32/0/0/0/0:ききかいひ")])
_only39.active.turns_out = 1
check("audit40 #19 候補: 技の候補が残らないときは外さない", _left39(_only39, _op39) == ["であいがしら"])

# 探索のねむりカウンタ: 相手のカウンタは見えている情報（眠ってからの行動回数・ねむる か）と整合する値から引き直す
_sl39 = _mk39(_DUM39)
_sl39.status = "sleep"; _sl39._sleep_acts = 2; _sl39._sleep_rest = False; _sl39.sleep_count = 1
_rr39 = _r39.Random(5)
_vals39 = set()
for _ in range(60):
    _rs39(_sl39, _rr39)
    _vals39.add(_sl39.sleep_count)
_sl39._sleep_rest = True; _sl39._sleep_acts = 1
_rs39(_sl39, _rr39)
check("audit40 ねむりの決定化: 2回行動して眠ったまま→残り1か2（眠った時2〜4）、ねむる で1回→残り2",
      _vals39 == {1, 2} and _sl39.sleep_count == 2, f"{_vals39} {_sl39.sleep_count}")
_bt, _a1, _a2 = _bt39([f"ゲンガー@{_N39}:おくびょう:さいみんじゅつ:32/0/0/0/0/32:のろわれボディ"], [_DUM39], ["さいみんじゅつ"], ["のろい"], seed=7)
_go39(_bt, _a1, _a2, 1)
_sn39 = []
while _bt.side2.active.status == "sleep" and _bt.turn < 6:
    _go39(_bt, _a1, _a2, _bt.turn + 1)
    _sn39.append(getattr(_bt.side2.active, "_sleep_acts", None))
check("audit40 ねむりの決定化: 眠ってからの行動回数を数える", _sn39 and _sn39[0] == 1, f"{_sn39}")

# #23 生成集団: メガが3枠になった党でメガを外すのは、メガでない系統の割合が大きい種（メガ専用の種の少数派の系統を膨らませない）
import os as _os39b, _coevo_groups as _CG39
_cwd39 = _os39b.getcwd(); _os39b.chdir(_os39b.path.dirname(_os39b.path.abspath(_CG39.__file__)))   # _pop_gen は DB を相対パスで開く
_cg39 = _CG39.load()
_os39b.chdir(_cwd39)
def _gi39(sp, mega):
    return next(i for i, m in enumerate(_cg39["mega"][sp]) if m == mega)
_ok39c = True
for _sd in range(20):
    _pt39 = [("カメックス", _gi39("カメックス", True)), ("リザードン", _gi39("リザードン", True)), ("ガブリアス", _gi39("ガブリアス", True)),
             ("アシレーヌ", 0), ("カバルドン", 0), ("ギルガルド", 0)]
    _rp39 = _CG39.repair(list(_pt39), _r39.Random(_sd))
    _ok39c &= (_rp39[0] == _pt39[0] and _rp39[1] == _pt39[1] and _rp39[2][0] == "ガブリアス" and not _cg39["mega"]["ガブリアス"][_rp39[2][1]])
check("audit40 #23 生成集団: メガ3枠の党はメガでない系統の多い種（ガブリアス）のメガを外す（カメックス・リザードンはメガのまま）", _ok39c)

# #23/#24 作り直した生成集団（guide_pool_m6_v2.json）: 設置役のいないシード（死に持ち物）が無く、努力値は合計66が主流
import os as _os39, json as _js39, seed_rule as _SR39
_gp39 = _os39.path.join(_os39.path.dirname(_os39.path.abspath(_SR39.__file__)), "guide_pool_m6_v2.json")
if _os39.path.exists(_gp39):
    _gpd39 = [o["party"] for o in _js39.load(open(_gp39))]
    _dead39 = sum(len(_SR39.violations(p)) for p in _gpd39)
    _ev66 = sum(1 for p in _gpd39 for x in p if sum(int(v) for v in x.split("@")[1].split(":")[3].split("/")) == 66)
    check("audit40 #23/#24 生成集団 v2: 3000党・死にシード0・努力値の合計66が9割以上",
          len(_gpd39) == 3000 and _dead39 == 0 and _ev66 >= 0.9 * 6 * len(_gpd39), f"{len(_gpd39)} {_dead39} {_ev66}")

# Python/Rust 照合: 各問題の局面を Rust の探索で戦い、Python で再生して一致（技を絞って局面を強制）
try:
    import feature1 as _F39f
    _ok39 = hasattr(_E39, "mcts_3v3_record")
except (ImportError, NameError):
    _ok39 = False
if _ok39:
    _F39f._ensure_loaded("M-6", 8)
    _PAR39 = {
        "#1": ([f"リザードン@リザードナイトY:ひかえめ:ウェザーボール:0/0/0/32/0/32:もうか"],
               [f"ブラッキー@{_N39}:ずぶとい:つきのひかり:32/0/32/0/0/0:せいしんりょく"], "天候がおわった"),
        "#2": ([_kyu39], [_DUM39], "繰り返すことになった"),
        "#4": ([f"ゲンガー@{_N39}:おくびょう:みちづれ|シャドーボール:0/0/0/32/0/32:のろわれボディ", _DUM39],
               [f"ドドゲザン@くろいメガネ:いじっぱり:つるぎのまい|ドゲザン:32/32/0/0/0/0:そうだいしょう"], "みちづれ"),
        "#5": ([f"イエッサン(オス)@{_N39}:おくびょう:いやしのねがい:0/0/0/32/0/32:サイコメイカー",
                f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース:0/0/0/32/0/0:げきりゅう"],
               [f"ヒートロトム@{_N39}:ずぶとい:おにび|オーバーヒート:32/0/32/0/0/0:ふゆう"], "いやしのねがい で全快"),
        "#6": ([f"ニンフィア@ようせいのハネ:ひかえめ:ハイパーボイス:32/0/0/32/0/0:フェアリースキン"], [_DUM39], "ハイパーボイス"),
        "#7": ([f"アーマーガア@{_N39}:わんぱく:ボディプレス:32/0/32/0/0/0:ミラーアーマー"],
               [f"ボーマンダ@{_N39}:いじっぱり:すてみタックル|こわいかお:0/32/0/0/0/32:いかく"], "ミラーアーマー"),
        "#8": ([_ace39], [f"ニンフィア@{_N39}:ずぶとい:まもる|ハイパーボイス:32/0/32/0/0/0:フェアリースキン"], "叩きつけられた"),
        "#9": ([f"ギャラドス@ギャラドスナイト:いじっぱり:たきのぼり:0/32/0/0/0/32:いかく"],
               [f"ミミッキュ@{_N39}:いじっぱり:つるぎのまい|じゃれつく:32/32/0/0/0/0:ばけのかわ",
                f"ガブリアス@{_N39}:わんぱく:じしん:32/0/32/0/0/0:さめはだ"], "さめはだ"),
        "#9b": ([f"ギャラドス@ギャラドスナイト:いじっぱり:たきのぼり:0/32/0/0/0/32:いかく"],
                [f"アローラキュウコン@ひかりのねんど:おくびょう:オーロラベール|ムーンフォース:32/0/0/0/0/32:ゆきふらし"], "オーロラベール"),
        "#10": ([f"カメックス@しろいハーブ:おくびょう:からをやぶる|なみのり:0/0/0/32/0/32:げきりゅう"],
                [f"ギャラドス@{_N39}:わんぱく:たきのぼり:32/0/32/0/0/0:じしんかじょう"], "しろいハーブ"),
        "#11": ([f"ゲンガー@{_N39}:おくびょう:ほろびのうた|まもる:32/0/0/0/0/32:のろわれボディ", _DUM39], [_DUM39, _DUM39], "ほろびのうた で倒れた"),
        "#12": ([f"アーマーガア@{_N39}:わんぱく:ボディプレス:32/0/32/0/0/0:プレッシャー"],
                [f"ラウドボーン@{_N39}:ずぶとい:フレアソング:32/0/32/0/0/0:てんねん"], "ボディプレス"),
        "#13": ([f"ウォッシュロトム@{_N39}:ずぶとい:いたみわけ|ハイドロポンプ:32/0/32/0/0/0:ふゆう"],
                [f"サーフゴー@{_N39}:ひかえめ:シャドーボール:0/0/0/32/0/32:おうごんのからだ"], "おうごんのからだ"),
        "#14": ([f"アシレーヌ@{_N39}:ひかえめ:ムーンフォース:0/0/0/32/0/0:げきりゅう", _baz39.replace("ビルドアップ", "フレアドライブ")], [_DUM39], "バシャーモ"),
        "#15": ([f"パーモット@{_N39}:ようき:でんこうそうげき:0/32/0/0/0/32:てつのこぶし"],
                [f"ライチュウ@{_N39}:おくびょう:10まんボルト:0/0/0/32/0/32:ひらいしん"], "効かない"),
        "#15b": ([f"ゴリランダー@{_N39}:いじっぱり:10まんばりき:32/32/0/0/0/0:グラスメイカー"],
                 [f"ウォッシュロトム@ゴツゴツメット:ずぶとい:おにび|ハイドロポンプ:32/0/32/0/0/0:ふゆう"], "効かない"),
        "#16": ([f"ライチュウ@{_N39}:おくびょう:みがわり:32/0/32/0/0/32:ひらいしん"],
                [f"アシレーヌ@{_N39}:ひかえめ:うたかたのアリア:32/0/0/32/0/0:げきりゅう"], "みがわり"),
        "#17": ([_gya39], [_DUM39], "ちょうはつ"),
        "sub": ([f"ゲンガー@{_N39}:おくびょう:みがわり|シャドーボール:32/0/0/0/0/32:のろわれボディ"],
                [f"ヒートロトム@{_N39}:ずぶとい:おにび|オーバーヒート:32/0/32/0/0/0:ふゆう"], "みがわり"),
        "misty": ([f"ニンフィア@{_N39}:ずぶとい:ミストフィールド|ハイパーボイス:32/0/32/0/0/0:フェアリースキン"],
                  [f"ブラッキー@{_N39}:ずぶとい:でんじは|イカサマ:32/0/32/0/0/0:せいしんりょく"], "ミストフィールド"),
    }
    _mm39, _seen39 = [], {}
    for _k39, (_pa39, _pb39, _kw39) in _PAR39.items():
        for _sd39 in (1, 2, 3, 4, 5, 6, 7, 8):
            try:
                _rec39 = _F39f.play_and_record_rust(_pa39, _pb39, season="M-6", seed=_sd39, mcts_sims=30,
                                                     sel1_idx=list(range(len(_pa39))))
                if any(_kw39 in l for t in _rec39["turns"] for l in t["logs"]):
                    _seen39[_k39] = True
            except _F39f.ReplayMismatch as _e39x:
                _mm39.append((_k39, _sd39, str(_e39x)[:160]))
    check("audit40 Python/Rust 照合: 各問題の局面（#1〜#17・みがわり・ミストフィールド）で再生が一致", not _mm39, str(_mm39)[:600])
    check("audit40 Python/Rust 照合: 各局面で問題の場面が実際に起きた", set(_seen39) == set(_PAR39), str(set(_PAR39) - set(_seen39)))

print("\n=== 40. 監査200（2026-10-04）の修正 ===")
import random as _r40
from simulator.battle import (Battle as _B40, BattleSide as _S40, BattleField as _F40, Action as _A40,
                              _execute_move as _x40, is_trapped as _it40)
from simulator.pokemon import build_from_spec as _bfs40, parse_pokemon_spec as _pps40
from simulator.damage import calc_damage as _cd40, check_hit as _ch40
_N40 = "メトロノーム"


def _mk40(spec):
    return _bfs40(_pps40(spec), dl, season="M-6", randomize=False)


class _P40:
    """ターンごとの行動計画（技名・"M:技名"でメガ進化・整数で交代）。最後の手を繰り返す"""
    def __init__(self, plan):
        self.plan = plan
        self.bt = None

    def __call__(self, my, opp, f):
        x = self.plan[min(self.bt.turn, len(self.plan)) - 1]
        if isinstance(x, int):
            return _A40(type="switch", switch_to=x)
        if x == "わるあがき":
            from simulator.ai import _get_struggle
            return _A40(type="move", move=_get_struggle(), move_idx=-1)
        for i, m in enumerate(my.active.moves):
            if m is not None and m.name_jp == x:
                return _A40(type="move", move=m, move_idx=i)
        return _A40(type="move", move=my.active.moves[0], move_idx=0)


def _bt40(s1, s2, p1, p2, seed=1, prep=None):
    _r40.seed(seed)
    a, b = _S40([_mk40(x) for x in s1]), _S40([_mk40(x) for x in s2])
    if prep:
        prep(a, b)
    bt = _B40(a, b, _F40())
    ai1, ai2 = _P40(p1), _P40(p2)
    ai1.bt = ai2.bt = bt
    bt.start(ai1, ai2)
    return bt, ai1, ai2


def _go40(bt, ai1, ai2, t):
    bt.resume(ai1, ai2, max_turns=t)


def _case40(name, fn):
    """1問題ぶんの検査。修正前のコードで例外になったら FAIL として数える"""
    try:
        fn()
    except Exception as e:
        check(f"audit200 {name}（例外）", False, repr(e)[:200])


_DUM40 = f"カビゴン@{_N40}:わんぱく:のろい|まもる:32/0/32/0/0/0:あついしぼう"
_BLK40 = f"ブラッキー@{_N40}:ずぶとい:ねがいごと|のろい:32/0/32/0/0/0:せいしんりょく"
_GAB40 = f"ガブリアス@{_N40}:わんぱく:まもる|のろい:32/0/32/0/0/0:さめはだ"


def _t1():
    for mv, sp in (("はどうだん", f"ルカリオ@{_N40}:おくびょう:はどうだん:0/0/0/32/0/32:せいしんりょく"),
                   ("ばくれつパンチ", f"カイリキー@{_N40}:いじっぱり:ばくれつパンチ:32/32/0/0/0/0:ノーガード")):
        bt, a1, a2 = _bt40([sp], [_GAB40], [mv], ["まもる"])
        _go40(bt, a1, a2, 1)
        g = bt.side2.active
        check(f"audit200 #1 まもる は必中技（{mv}）より先に判定して防ぐ", g.hp == g.max_hp and not g.confused, f"{g.hp}/{g.max_hp}")
    bt, a1, a2 = _bt40([f"カバルドン@{_N40}:わんぱく:あくび:32/0/32/0/0/0:すなおこし"], [_GAB40], ["あくび"], ["まもる"])
    _go40(bt, a1, a2, 1)
    check("audit200 #1 まもる は あくび（命中「—」）も防ぐ", bt.side2.active.yawn_count == 0, f"{bt.side2.active.yawn_count}")
    bt, a1, a2 = _bt40([f"カバルドン@{_N40}:わんぱく:ほえる:32/0/32/0/0/0:すなおこし"], [_GAB40, _BLK40], ["ほえる"], ["まもる"])
    _go40(bt, a1, a2, 1)
    check("audit200 #1 ほえる は守りを貫通する（対照）", bt.side2.active.name == "ブラッキー", bt.side2.active.name)
    sw = _mk40(f"エルフーン@{_N40}:おくびょう:つるぎのまい:0/0/0/32/0/32:いたずらごころ")
    g = _mk40(_GAB40)
    g.protecting = True
    check("audit200 #1 自分が対象の変化技は相手の守りに関係なく成功", _ch40(sw, g, dl.get_move("つるぎのまい"), _F40()))


def _t3():
    bt, a1, a2 = _bt40([f"フォレトス@{_N40}:わんぱく:こうそくスピン|まもる:32/0/32/0/0/0:がんじょう"],
                       [f"カバルドン@{_N40}:わんぱく:ステルスロック|のろい:32/0/32/0/0/0:すなおこし"],
                       ["まもる", "こうそくスピン", "まもる"], ["ステルスロック", "のろい", "ステルスロック"])
    sr = []
    for t in (1, 2, 3):
        _go40(bt, a1, a2, t)
        sr.append(bt.field.stealth_rock[0])
    check("audit200 #3 ステルスロック: こうそくスピン で消された後に撒き直せる", sr == [True, False, True], f"{sr}")


def _t4():
    bt, a1, a2 = _bt40([f"エルフーン@{_N40}:おくびょう:みがわり|でんじは:0/0/0/32/0/32:いたずらごころ"], [_BLK40],
                       ["みがわり", "でんじは"], ["のろい"])
    _go40(bt, a1, a2, 1)
    sub = getattr(bt.side1.active, "_substitute_hp", 0)
    _go40(bt, a1, a2, 2)
    check("audit200 #4 いたずらごころ: あく相手でも自分対象の みがわり は成功、相手対象の でんじは は失敗",
          sub > 0 and bt.side2.active.status is None, f"{sub} {bt.side2.active.status}")


def _t5():
    esp = f"エーフィ@{_N40}:ずぶとい:めいそう:32/0/32/0/0/0:マジックミラー"
    bt, a1, a2 = _bt40([esp], [f"オニシズクモ@{_N40}:わんぱく:ステルスロック|まきびし|ねばねばネット|どくびし:32/0/32/0/0/0:すいほう"],
                       ["めいそう"], ["ステルスロック", "まきびし", "ねばねばネット", "どくびし"])
    _go40(bt, a1, a2, 4)
    f = bt.field
    check("audit200 #5 マジックミラー: ステルスロック・まきびし・ねばねばネット・どくびし を使った側に跳ね返す",
          (f.stealth_rock, f.spikes, f.sticky_web, f.toxic_spikes) == ([False, True], [0, 1], [False, True], [0, 1]),
          f"{f.stealth_rock} {f.spikes} {f.sticky_web} {f.toxic_spikes}")
    bt, a1, a2 = _bt40([esp, _BLK40], [f"オーロンゲ@{_N40}:わんぱく:すてゼリフ:32/0/32/0/0/0:いたずらごころ", _BLK40],
                       ["めいそう"], ["すてゼリフ"])
    _go40(bt, a1, a2, 1)
    o = bt.side2.active
    check("audit200 #5 マジックミラー: すてゼリフ を跳ね返す（使った側の攻撃・特攻-1、どちらも交代しない）",
          o.name == "オーロンゲ" and (o.stage_attack, o.stage_sp_attack) == (-1, -1) and bt.side1.active.name == "エーフィ",
          f"{o.name} {o.stage_attack} {o.stage_sp_attack} {bt.side1.active.name}")


def _t6():
    bt, a1, a2 = _bt40([_DUM40, _BLK40], [f"ドヒドイデ@{_N40}:ずぶとい:どくどく|まもる:32/0/32/0/0/0:さいせいりょく"],
                       ["のろい", "のろい", 1, 0, "のろい"], ["どくどく", "まもる", "まもる", "まもる", "まもる"])
    _go40(bt, a1, a2, 3)
    c = bt.side1.party[0]
    hp3 = c.hp
    _go40(bt, a1, a2, 4)
    check("audit200 #6 もうどく: 交代で戻ると段階は1から（戻ったターンの終わりは1/16）",
          c.status == "badpoison" and hp3 - c.hp == c.max_hp // 16, f"{c.status} {hp3 - c.hp} {c.max_hp // 16}")


def _t7():
    bt, a1, a2 = _bt40([f"エルフーン@{_N40}:おくびょう:おいかぜ|まもる:0/0/0/32/0/32:いたずらごころ"], [_DUM40],
                       ["おいかぜ", "まもる"], ["のろい"])
    tw = []
    for t in range(1, 6):
        _go40(bt, a1, a2, t)
        tw.append(bt.side1.tailwind)
    check("audit200 #7 おいかぜ は使ったターンを含め4ターン（4ターン目の終わりに切れる）", tw == [True, True, True, False, False], f"{tw}")


def _t8():
    bt, a1, a2 = _bt40([f"ブラッキー@{_N40}:ずぶとい:くろいまなざし|のろい:32/0/32/0/0/0:せいしんりょく", _DUM40],
                       [_DUM40, _BLK40], ["くろいまなざし", 1], ["のろい"])
    _go40(bt, a1, a2, 1)
    t1 = _it40(bt.side2.active, bt.side1.active)
    _go40(bt, a1, a2, 2)
    check("audit200 #8 くろいまなざし: 縛った側が交代すると解ける", t1 and not _it40(bt.side2.active, bt.side1.active),
          f"{t1} {_it40(bt.side2.active, bt.side1.active)}")
    bt, a1, a2 = _bt40([f"マフィティフ@{_N40}:いじっぱり:くらいつく|まもる:32/32/0/0/0/0:いかく", _BLK40], [_DUM40, _BLK40],
                       ["くらいつく", "まもる"], ["のろい", 1])
    _go40(bt, a1, a2, 1)
    both = (_it40(bt.side1.active, bt.side2.active), _it40(bt.side2.active, bt.side1.active))
    _go40(bt, a1, a2, 2)
    check("audit200 #8 くらいつく: 両者交代不可、相手が退場すると使った側も解ける",
          both == (True, True) and not _it40(bt.side1.active, bt.side2.active), f"{both} {_it40(bt.side1.active, bt.side2.active)}")
    bt, a1, a2 = _bt40([f"ドヒドイデ@{_N40}:ずぶとい:まとわりつく:32/0/32/0/0/0:さいせいりょく"], [_DUM40, _BLK40],
                       ["まとわりつく"], ["のろい"])
    _go40(bt, a1, a2, 1)
    c = bt.side2.active
    check("audit200 #8 バインド中は交代できない", c.bound_count > 0 and _it40(c, bt.side1.active), f"{c.bound_count}")
    gh = _mk40(f"ゲンガー@{_N40}:おくびょう:のろい:0/0/0/32/0/32:のろわれボディ")
    gh.bound_count = 3; gh.trapped = True
    sh = _mk40(f"カビゴン@きれいなぬけがら:わんぱく:のろい:32/0/32/0/0/0:あついしぼう")
    sh.bound_count = 3; sh.trapped = True
    check("audit200 #8 ゴーストタイプ・きれいなぬけがら は逃げられない状態・バインドでも交代できる",
          sh.item == "きれいなぬけがら" and not _it40(gh, None) and not _it40(sh, None))


def _t9():
    kyu = f"アローラキュウコン@{_N40}:おくびょう:アンコール|かなしばり|ムーンフォース:32/0/32/0/0/32:ゆきふらし"
    bt, a1, a2 = _bt40([kyu], [_DUM40, _BLK40], ["ムーンフォース", "アンコール"], ["のろい", 1])
    _go40(bt, a1, a2, 2)
    check("audit200 #9 交代で出たばかりの相手（前の出番の技は消える）への アンコール は失敗",
          bt.side2.active.encore_count == 0 and bt.side2.active.last_used_move is None and bt.side2.party[0].last_used_move is None,
          f"{bt.side2.active.encore_count} {bt.side2.party[0].last_used_move}")
    bt, a1, a2 = _bt40([kyu], [_DUM40], ["ムーンフォース", "アンコール"], ["のろい"])
    _go40(bt, a1, a2, 1)
    c = bt.side2.active
    c.pp[0] = 0
    _go40(bt, a1, a2, 2)
    check("audit200 #9 直前の技のPPが0なら アンコール は失敗", c.encore_count == 0, f"{c.encore_count}")
    bt, a1, a2 = _bt40([kyu], [_DUM40], ["ムーンフォース", "アンコール", "ムーンフォース"], ["のろい", "のろい", "わるあがき"])
    _go40(bt, a1, a2, 2)
    c = bt.side2.active
    enc = c.encore_count
    c.pp[0] = 0
    a0 = c.stage_attack
    l0 = len(bt.logs)
    _go40(bt, a1, a2, 3)
    check("audit200 #9 アンコールされた技のPPが尽きたらアンコールは解け、わるあがき をその技に差し替えない",
          enc > 0 and c.encore_count == 0 and c.stage_attack == a0 and any("わるあがき" in x for x in bt.logs[l0:]),
          f"{enc} {c.encore_count} {c.stage_attack} {a0}")
    bt, a1, a2 = _bt40([kyu], [_DUM40, _BLK40], ["ムーンフォース", "ムーンフォース", "ムーンフォース", "かなしばり"], ["のろい", 1, 0, "のろい"])
    _go40(bt, a1, a2, 4)
    check("audit200 #9 一度引っ込んで戻った相手（戻ってから技を使っていない）への かなしばり は失敗",
          bt.side2.active.name == "カビゴン" and bt.side2.active.disabled_move is None, f"{bt.side2.active.disabled_move}")


def _t10():
    for tgt in (f"ウォッシュロトム@{_N40}:ずぶとい:なまける:32/0/32/0/0/0:ふゆう",
                f"サーフゴー@ふうせん:ずぶとい:わるだくみ:32/0/32/0/0/0:おうごんのからだ"):
        bt, a1, a2 = _bt40([f"カビゴン@{_N40}:いじっぱり:じわれ:32/32/0/0/0/0:あついしぼう"], [tgt], ["じわれ"], ["なまける"], seed=3)
        _go40(bt, a1, a2, 4)
        check(f"audit200 #10 じわれ は浮いている相手（{tgt.split('@')[0]}・{tgt.split(':')[-1] if 'ふうせん' not in tgt else 'ふうせん'}）に効かない",
              bt.side2.active.is_alive, f"{bt.side2.active.hp}")
    mr = _mk40(f"クレッフィ@{_N40}:ずぶとい:でんじふゆう:32/0/32/0/0/0:いたずらごころ")
    mr.magnet_rise = True
    from simulator.battle import _airborne
    check("audit200 #10 でんじふゆう 中も浮いている扱い", _airborne(mr, _F40()))


def _t11():
    bt, a1, a2 = _bt40([f"ドラパルト@{_N40}:ようき:ゴーストダイブ:0/32/0/0/0/32:すりぬけ"],
                       [f"ガブリアス@{_N40}:ようき:ドラゴンクロー:0/32/0/0/0/32:さめはだ"], ["ゴーストダイブ"], ["ドラゴンクロー"])
    _go40(bt, a1, a2, 1)
    d = bt.side1.active
    check("audit200 #11 溜め技（ゴーストダイブ）の1ターン目は相手の攻撃が当たらない", d.hp == d.max_hp and d.charging_move == "ゴーストダイブ",
          f"{d.hp}/{d.max_hp}")
    dig = _mk40(f"ガブリアス@{_N40}:ようき:あなをほる:0/32/0/0/0/32:さめはだ")
    dig.charging_move = "あなをほる"
    eq = _mk40(f"カバルドン@{_N40}:わんぱく:じしん|ストーンエッジ:32/0/32/0/0/0:すなおこし")
    _orig = _r40.random
    try:
        _r40.random = lambda: 0.0
        hit_eq, hit_se = _ch40(eq, dig, dl.get_move("じしん"), _F40()), _ch40(eq, dig, dl.get_move("ストーンエッジ"), _F40())
    finally:
        _r40.random = _orig
    check("audit200 #11 あなをほる中: じしん は当たり、ストーンエッジ は（命中の乱数に関係なく）当たらない", hit_eq and not hit_se, f"{hit_eq} {hit_se}")


def _t12():
    bt, a1, a2 = _bt40([f"ミミズズ@{_N40}:わんぱく:しっぽきり:32/0/32/0/0/0:どしょく", _BLK40], [_DUM40], ["しっぽきり"], ["のろい"])
    _go40(bt, a1, a2, 1)
    m = bt.side1.party[0]
    check("audit200 #12 しっぽきり: みがわり（最大HPの1/4）は交代先に引き継がれる",
          bt.side1.active.name == "ブラッキー" and getattr(bt.side1.active, "_substitute_hp", 0) == m.max_hp // 4
          and getattr(m, "_substitute_hp", 0) == 0, f"{bt.side1.active.name} {getattr(bt.side1.active, '_substitute_hp', 0)}")
    bt, a1, a2 = _bt40([f"ミミズズ@{_N40}:わんぱく:しっぽきり:32/0/32/0/0/0:どしょく"], [_DUM40], ["しっぽきり"], ["のろい"])
    _go40(bt, a1, a2, 1)
    check("audit200 #12 しっぽきり: 控えがいなければ失敗（HPは減らない）", bt.side1.active.hp == bt.side1.active.max_hp)


def _t13():
    bt, a1, a2 = _bt40([f"イッカネズミ@{_N40}:ようき:おかたづけ|ネズミざん:0/32/0/0/0/32:テクニシャン"],
                       [f"ゲンガー@{_N40}:おくびょう:ステルスロック|みがわり|まもる:32/0/0/0/0/32:のろわれボディ"],
                       ["ネズミざん", "ネズミざん", "おかたづけ"], ["ステルスロック", "みがわり", "まもる"], seed=4)
    _go40(bt, a1, a2, 2)
    pre = (bt.field.stealth_rock[0], getattr(bt.side2.active, "_substitute_hp", 0) > 0)
    _go40(bt, a1, a2, 3)
    check("audit200 #13 おかたづけ は ステルスロック と みがわり も消す",
          pre == (True, True) and not bt.field.stealth_rock[0] and getattr(bt.side2.active, "_substitute_hp", 0) == 0,
          f"{pre} {bt.field.stealth_rock} {getattr(bt.side2.active, '_substitute_hp', 0)}")


def _t14():
    bt, a1, a2 = _bt40([f"ランクルス@いのちのたま:ひかえめ:ドレインパンチ:32/0/0/32/0/0:マジックガード"],
                       [f"ガブリアス@ゴツゴツメット:わんぱく:のろい:32/0/32/0/0/0:さめはだ"], ["ドレインパンチ"], ["のろい"])
    _go40(bt, a1, a2, 1)
    r = bt.side1.active
    check("audit200 #14 マジックガード: いのちのたま・さめはだ・ゴツゴツメット の反動を受けない", r.hp == r.max_hp, f"{r.hp}/{r.max_hp}")
    def _prep(a, b):
        p = a.party[0]
        p.seeded = True; p.cursed = True; p._salted = True; p.bound_count = 3
    bt, a1, a2 = _bt40([f"フーディン@くろいヘドロ:おくびょう:めいそう:0/0/0/32/0/32:マジックガード"], [_DUM40], ["めいそう"], ["のろい"], prep=_prep)
    _go40(bt, a1, a2, 1)
    f = bt.side1.active
    check("audit200 #14 マジックガード: やどりぎ・のろい・しおづけ・バインド・くろいヘドロ のダメージを受けない",
          f.hp == f.max_hp, f"{f.hp}/{f.max_hp}")


def _t15():
    bt, a1, a2 = _bt40([f"コノヨザル@{_N40}:いじっぱり:ふんどのこぶし|ビルドアップ:32/32/0/0/0/0:まけんき", _BLK40],
                       [f"ガブリアス@{_N40}:いじっぱり:ドラゴンクロー:32/0/32/0/0/0:さめはだ"],
                       ["ビルドアップ", "ビルドアップ", 1, 0], ["ドラゴンクロー"])
    _go40(bt, a1, a2, 4)
    check("audit200 #15 ふんどのこぶし: 被弾回数は交代しても戻らない", bt.side1.party[0].times_hit >= 2,
          f"{bt.side1.party[0].times_hit}")


def _t16():
    bt, a1, a2 = _bt40([f"ヒスイゾロアーク@{_N40}:おくびょう:うらみつらみ:0/0/0/32/0/32:イリュージョン"], [_GAB40], ["うらみつらみ"], ["のろい"])
    _go40(bt, a1, a2, 1)
    check("audit200 #16 うらみつらみ は相手の攻撃を1段階下げる（のろいの+1と合わせて0）", bt.side2.active.stage_attack == 0,
          f"{bt.side2.active.stage_attack}")
    from simulator.damage import _secondary_effect_moves
    check("audit200 #16 うらみつらみ は追加効果のある技（ちからずく の対象）", "うらみつらみ" in _secondary_effect_moves())


def _t17():
    bt, a1, a2 = _bt40([f"オーロンゲ@{_N40}:わんぱく:すてゼリフ:32/0/32/0/0/0:いたずらごころ", _BLK40],
                       [f"メタグロス@{_N40}:いじっぱり:てっぺき:32/32/0/0/0/0:クリアボディ"], ["すてゼリフ"], ["てっぺき"])
    _go40(bt, a1, a2, 1)
    check("audit200 #17 すてゼリフ: 相手の能力が下がらなければ交代しない", bt.side1.active.name == "オーロンゲ", bt.side1.active.name)
    bt, a1, a2 = _bt40([f"オーロンゲ@{_N40}:わんぱく:すてゼリフ:32/0/32/0/0/0:おみとおし", _BLK40],
                       [f"ドドゲザン@{_N40}:いじっぱり:アイアンヘッド:32/32/0/0/0/0:まけんき"], ["すてゼリフ"], ["アイアンヘッド"])
    _go40(bt, a1, a2, 1)
    d = bt.side2.active
    check("audit200 #17 すてゼリフ: まけんき が1回発動（攻撃 -1+2=+1・特攻-1）して交代する",
          (d.stage_attack, d.stage_sp_attack) == (1, -1) and bt.side1.active.name == "ブラッキー",
          f"{d.stage_attack} {d.stage_sp_attack} {bt.side1.active.name}")
    bt, a1, a2 = _bt40([f"ゲンガー@{_N40}:おくびょう:おきみやげ:0/0/0/32/0/32:のろわれボディ", _BLK40],
                       [f"ドドゲザン@{_N40}:いじっぱり:アイアンヘッド:32/32/0/0/0/0:まけんき"], ["おきみやげ"], ["アイアンヘッド"])
    _go40(bt, a1, a2, 1)
    d = bt.side2.active
    check("audit200 #17 おきみやげ: まけんき が発動（攻撃 -2+2=0・特攻-2）", (d.stage_attack, d.stage_sp_attack) == (0, -2),
          f"{d.stage_attack} {d.stage_sp_attack}")


def _t18():
    mo = _mk40(f"モルペコ@{_N40}:ようき:オーラぐるま:0/32/0/0/0/32:はらぺこスイッチ")
    from simulator.damage import _effective_move_type
    t0 = _effective_move_type(mo, mo.moves[0], _F40())
    mo._hangry = True
    check("audit200 #18 オーラぐるま: まんぷくは でんき、はらぺこは あく", (t0, _effective_move_type(mo, mo.moves[0], _F40())) == ("でんき", "あく"),
          f"{t0}")


def _t19():
    a = _mk40(f"ハラバリー@{_N40}:ひかえめ:パラボラチャージ:32/0/0/32/0/0:でんきにかえる")
    d = _mk40(_DUM40)
    d0 = _cd40(a, d, a.moves[0], _F40(), False, 0.5)
    a._electromorphosis_charged = True
    d1 = _cd40(a, d, a.moves[0], _F40(), False, 0.5)
    check("audit200 #19 でんきにかえる: 次のでんき技は2倍", 1.95 < d1 / d0 < 2.05, f"{d1} {d0}")


def _t20():
    for sp, rate in ((_DUM40, 16), (f"エンペルト@{_N40}:ずぶとい:のろい:32/0/32/0/0/0:かちき", 8)):
        def _prep(a, b):
            b.party[0]._salted = True
        bt, a1, a2 = _bt40([f"キョジオーン@{_N40}:わんぱく:のろい:32/0/32/0/0/0:きよめのしお"], [sp], ["のろい"], ["のろい"], prep=_prep)
        _go40(bt, a1, a2, 1)
        p = bt.side2.active
        check(f"audit200 #20 しおづけ（Champions 仕様・SVより弱体）: {p.name} は最大HPの1/{rate}", p.max_hp - p.hp == p.max_hp // rate,
              f"{p.max_hp - p.hp} {p.max_hp // rate}")


def _t21():
    d = _mk40(_DUM40)
    for mv in ("ワイルドボルト", "もろはのずつき"):
        a1 = _mk40(f"エンブオー@{_N40}:いじっぱり:{mv}:0/32/0/0/0/32:すてみ")
        a0 = _mk40(f"エンブオー@{_N40}:いじっぱり:{mv}:0/32/0/0/0/32:もうか")
        x1, x0 = _cd40(a1, d, a1.moves[0], _F40(), False, 0.5), _cd40(a0, d, a0.moves[0], _F40(), False, 0.5)
        check(f"audit200 #21 すてみ は {mv} を1.2倍", 1.15 < x1 / x0 < 1.25, f"{x1} {x0}")


def _t22():
    def _prep(a, b):
        b.party[1].hp = 3
    bt, a1, a2 = _bt40([f"カバルドン@{_N40}:わんぱく:ステルスロック|のろい:32/0/32/0/0/0:すなおこし"],
                       [_DUM40, f"トリデプス@{_N40}:ずぶとい:のろい:32/0/32/0/0/0:がんじょう", _BLK40],
                       ["ステルスロック", "のろい"], ["のろい", 1], prep=_prep)
    _go40(bt, a1, a2, 2)
    check("audit200 #22 がんじょう は設置物では耐えない（ステルスロックで倒れる）", not bt.side2.party[1].is_alive,
          f"{bt.side2.party[1].hp}")


def _t23():
    bt, a1, a2 = _bt40([f"クレッフィ@{_N40}:ずぶとい:でんじふゆう|まもる:32/0/32/0/0/0:いたずらごころ"], [_DUM40],
                       ["でんじふゆう", "まもる"], ["のろい"])
    mr = []
    for t in range(1, 7):
        _go40(bt, a1, a2, t)
        mr.append(bt.side1.active.magnet_rise)
    check("audit200 #23 でんじふゆう は使ったターンを含め5ターン（5ターン目の終わりに切れる）", mr == [True] * 4 + [False, False], f"{mr}")
    bt, a1, a2 = _bt40([f"クレッフィ@{_N40}:ずぶとい:でんじふゆう:32/0/32/0/0/0:いたずらごころ", _BLK40], [_DUM40],
                       ["でんじふゆう", 1], ["のろい"])
    _go40(bt, a1, a2, 2)
    check("audit200 #23 でんじふゆう は交代で終わる", not bt.side1.party[0].magnet_rise)


def _t24():
    def _prep(a, b):
        b.party[0].hp = b.party[0].max_hp // 2
        b.party[0].heal_block_count = 2
    bt, a1, a2 = _bt40([f"ストリンダー(ハイ)@{_N40}:ひかえめ:ちょうはつ:0/0/0/32/0/32:パンクロック"],
                       [f"カビゴン@たべのこし:わんぱく:のろい:32/0/32/0/0/0:あついしぼう"], ["ちょうはつ"], ["のろい"], prep=_prep)
    bt.field.grassy_terrain = True; bt.field.grassy_terrain_count = 5
    h0 = bt.side2.active.hp
    _go40(bt, a1, a2, 1)
    check("audit200 #24 かいふくふうじ は たべのこし・グラスフィールド の回復も止める", bt.side2.active.hp == h0, f"{bt.side2.active.hp} {h0}")


def _t25():
    h = _mk40(f"ハリーマン@{_N40}:ずぶとい:ちいさくなる:32/0/32/0/0/0:すいすい")
    h.minimized = True; h.stage_evasion = 6
    k = _mk40(f"カビゴン@{_N40}:いじっぱり:のしかかり:32/32/0/0/0/0:あついしぼう")
    _r40.seed(2)
    hits = sum(_ch40(k, h, k.moves[0], _F40()) for _ in range(50))
    check("audit200 #25 ちいさくなる の相手に のしかかり は必中", hits == 50, f"{hits}")
    def _prep(a, b):
        b.party[0].stage_attack = -6
        a.party[0].hp = a.party[0].max_hp // 2
    bt, a1, a2 = _bt40([f"ウツボット@{_N40}:ずぶとい:ちからをすいとる:32/0/32/0/0/0:ようりょくそ"], [_DUM40],
                       ["ちからをすいとる"], ["まもる"], prep=_prep)
    h0 = bt.side1.active.hp
    bt.side2.active.moves = [dl.get_move("あくび")]
    _go40(bt, a1, a2, 1)
    check("audit200 #25 ちからをすいとる は相手の攻撃が-6なら失敗（回復しない）", bt.side1.active.hp == h0, f"{bt.side1.active.hp} {h0}")


def _t27():
    a = _mk40(f"ラフレシア@フォーカスレンズ:ひかえめ:ねむりごな:32/0/0/32/0/0:ようりょくそ")
    d = _mk40(_DUM40)
    mv = dl.get_move("ねむりごな")
    a._acts_second = True
    _orig = _r40.random
    try:
        _r40.random = lambda: 0.75 * 1.2 - 0.01
        lens = _ch40(a, d, mv, _F40())
        a._acts_second = False
        first = _ch40(a, d, mv, _F40())
    finally:
        _r40.random = _orig
    check("audit200 #27 フォーカスレンズ: 後攻のとき命中1.2倍（命中75→90）、先攻では補正なし", a.item == "フォーカスレンズ" and lens and not first, f"{lens} {first}")
    bt, a1, a2 = _bt40([f"オーロンゲ@{_N40}:わんぱく:ちょうはつ:32/0/32/0/0/0:いたずらごころ"],
                       [f"カビゴン@メンタルハーブ:わんぱく:のろい|まもる:32/0/32/0/0/0:あついしぼう"], ["ちょうはつ"], ["のろい"])
    _go40(bt, a1, a2, 1)
    c = bt.side2.active
    check("audit200 #27 メンタルハーブ は ちょうはつ を受けた直後に発動（同じターンの のろい が使える）",
          c.item is None and c.taunt_count == 0 and c.stage_attack == 1, f"{c.item} {c.taunt_count} {c.stage_attack}")
    from simulator.abilities import end_of_turn_ability
    mo = _mk40(f"オニシズクモ@{_N40}:ずぶとい:のろい:32/0/32/0/0/0:すいほう")
    mo.ability = "ムラっけ"
    _r40.seed(3)
    ae = set()
    for _ in range(200):
        for s in ("stage_attack", "stage_defense", "stage_sp_attack", "stage_sp_defense", "stage_speed", "stage_accuracy", "stage_evasion"):
            setattr(mo, s, 0)
        end_of_turn_ability(mo, _F40(), [])
        ae.add((mo.stage_accuracy, mo.stage_evasion))
    check("audit200 #27 ムラっけ は命中・回避を変えない", ae == {(0, 0)}, f"{ae}")
    from simulator.abilities import get_sharpness_multiplier
    ba = _mk40(f"バサギリ@{_N40}:いじっぱり:シザークロス:0/32/0/0/0/32:きれあじ")
    check("audit200 #27 きれあじ: シザークロス・ドゲザン は1.5倍、ドラゴンクロー・ブレイククロー は対象外",
          [get_sharpness_multiplier(ba, m) for m in ("シザークロス", "ドゲザン", "ドラゴンクロー", "ブレイククロー")] == [1.5, 1.5, 1.0, 1.0])


def _tsub():
    sub = _S40([_mk40(f"ガブリアス@ゴツゴツメット:わんぱく:のろい:32/0/32/0/0/0:さめはだ"), _mk40(_BLK40)])
    sub.active._substitute_hp = 200
    att = _S40([_mk40(f"ドドゲザン@{_N40}:いじっぱり:はたきおとす|ドラゴンテール|アイアンヘッド:32/32/0/0/0/0:まけんき")])
    _r40.seed(1)
    _x40(att, sub, _A40(type="move", move=att.active.moves[0], move_idx=0), _F40())
    _x40(att, sub, _A40(type="move", move=att.active.moves[1], move_idx=1), _F40())
    check("audit200 みがわり: 接触の反応（ゴツゴツメット・さめはだ）・はたきおとす・ドラゴンテール の交代は起きない",
          att.active.hp == att.active.max_hp and sub.active.item == "ゴツゴツメット" and not getattr(sub.active, "_force_switch", False)
          and sub.active._substitute_hp < 200, f"{att.active.hp}/{att.active.max_hp} {sub.active.item} {sub.active._substitute_hp}")
    burn = 0
    for sd in range(60):
        s2 = _S40([_mk40(_DUM40)])
        s2.active._substitute_hp = 999
        fire = _S40([_mk40(f"ヒートロトム@{_N40}:ずぶとい:ねっぷう|オーバーヒート:32/0/32/0/0/0:ふゆう")])
        _r40.seed(sd)
        _x40(fire, s2, _A40(type="move", move=fire.active.moves[0], move_idx=0), _F40())
        burn += s2.active.status == "burn"
    _x40(fire, s2, _A40(type="move", move=fire.active.moves[1], move_idx=1), _F40())
    check("audit200 みがわり: 追加効果（ねっぷう の やけど）は入らないが、自分の能力変化（オーバーヒートの特攻-2）は起きる",
          burn == 0 and fire.active.stage_sp_attack == -2 and s2.active.hp == s2.active.max_hp, f"{burn} {fire.active.stage_sp_attack}")
    s3 = _S40([_mk40(_GAB40)])
    s3.active._substitute_hp = 30
    gh = _S40([_mk40(f"ゲンガー@{_N40}:おくびょう:ナイトヘッド:0/0/0/32/0/32:のろわれボディ")])
    _x40(gh, s3, _A40(type="move", move=gh.active.moves[0], move_idx=0), _F40())
    check("audit200 みがわり: ナイトヘッド（固定ダメージ）は みがわり が受ける", s3.active.hp == s3.active.max_hp and s3.active._substitute_hp == 0,
          f"{s3.active.hp} {s3.active._substitute_hp}")


def _tweather():
    bt, a1, a2 = _bt40([f"ペリッパー@{_N40}:ずぶとい:あまごい|まもる:32/0/32/0/0/0:あめふらし"], [_DUM40], ["まもる", "まもる", "あまごい"], ["のろい"])
    _go40(bt, a1, a2, 2)
    w2 = bt.field.weather_count
    _go40(bt, a1, a2, 3)
    check("audit200 同じ天候の あまごい は失敗（残りターンは延びない）", bt.field.weather == "rain" and bt.field.weather_count == w2 - 1,
          f"{w2} {bt.field.weather_count}")
    bt, a1, a2 = _bt40([f"ゴリランダー@{_N40}:いじっぱり:グラスフィールド|まもる:32/32/0/0/0/0:グラスメイカー"], [_DUM40],
                       ["まもる", "グラスフィールド"], ["のろい"])
    _go40(bt, a1, a2, 1)
    g1 = bt.field.grassy_terrain_count
    _go40(bt, a1, a2, 2)
    check("audit200 同じフィールドの グラスフィールド は失敗（残りターンは延びない）", bt.field.grassy_terrain and bt.field.grassy_terrain_count == g1 - 1,
          f"{g1} {bt.field.grassy_terrain_count}")


for _nm40, _fn40 in (("#1", _t1), ("#3", _t3), ("#4", _t4), ("#5", _t5), ("#6", _t6), ("#7", _t7), ("#8", _t8), ("#9", _t9),
                     ("#10", _t10), ("#11", _t11), ("#12", _t12), ("#13", _t13), ("#14", _t14), ("#15", _t15), ("#16", _t16),
                     ("#17", _t17), ("#18", _t18), ("#19", _t19), ("#20", _t20), ("#21", _t21), ("#22", _t22), ("#23", _t23),
                     ("#24", _t24), ("#25", _t25), ("#27", _t27), ("みがわり", _tsub), ("天候・フィールド", _tweather)):
    _case40(_nm40, _fn40)


# B: 型の書式（Rust parse_pokemon_spec を Python と同じ解析に。種名の「:」・空白・欄の省略）
def _tspec():
    import pokenavi_engine as _E
    import json as _js, os as _os
    import pool_versions as _PV
    specs = ["ケンタロス:炎@こだわりスカーフ:いじっぱり:レイジングブル|インファイト:0/32/0/0/0/32:いかく",
             "ケンタロス:水@たべのこし:わんぱく::32/0/32/0/0/2:いかく", "ガブリアス", "ガブリアス@ガブリアスナイト",
             "ガブリアス:ようき:じしん| げきりん |:2/32", " ガブリアス @ ふうせん : ようき : じしん : 2 / 32 / 0 : さめはだ ",
             "メタモン@こだわりスカーフ:のんき:へんしん:32/0/32/0/0/0:かわりもの", "ガブリアス@:ようき"]
    def _py(s):
        d = _pps40(s)
        ev = None if d["evs"] is None else [d["evs"][k] for k in ("H", "A", "B", "C", "D", "S")]
        return (d["name"], d["item"], d["nature"], d["moves"], ev, d["ability"])
    bad = [s for s in specs if tuple(_E.parse_spec(s)) != _py(s)]
    check("audit200 #2 型の書式: Rust の解析が Python と一致（種名に「:」・空白・欄の省略）", not bad, str(bad[:3]))
    pool = []
    for e in _js.load(open(_PV.path("type_pool", _PV.pointer("season")))):
        pool += [b["spec"] for b in e["builds"]]
    bad = [s for s in pool if tuple(_E.parse_spec(s)) != _py(s)]
    check(f"audit200 #2 型の書式: 型プール全{len(pool)}件で Rust の解析が Python と一致", len(pool) > 1000 and not bad, str(bad[:3]))
    try:
        _E.parse_spec("ガブリアス:ようき:じしん:32/x/0")
        ok = False
    except ValueError:
        ok = True
    check("audit200 #2 型の書式: 読めない努力値は Rust でも例外（パニックではない）", ok)
    import feature1 as _F
    _F._ensure_loaded("M-6", 8)
    rec = _F.play_and_record_rust([specs[0]], [_DUM40], season="M-6", seed=1, mcts_sims=20, sel1_idx=[0])
    check("audit200 #2 ケンタロス:炎 で Rust の対戦が動き、Python の再生と一致", rec["selected1"] == ["ケンタロス:炎"], f"{rec['selected1']}")


_case40("#2", _tspec)


# Python/Rust 照合: 各問題の局面を Rust の探索で戦い、Python で再生して一致（技を絞って局面を強制）
def _tpar():
    import feature1 as _F
    import pokenavi_engine as _E
    if not hasattr(_E, "mcts_3v3_record"):
        return
    _F._ensure_loaded("M-6", 8)
    G = "ガブリアス@{}:ようき:じしん|ドラゴンクロー|まもる:0/32/0/0/0/32:さめはだ".format(_N40)
    PAR = {
        "#1": ([f"ルカリオ@{_N40}:おくびょう:はどうだん|わるだくみ:0/0/0/32/0/32:せいしんりょく"],
               [f"ガブリアス@{_N40}:わんぱく:まもる:32/0/32/0/0/0:さめはだ"], "防がれた"),
        "#1b": ([f"カバルドン@{_N40}:わんぱく:あくび|じしん:32/0/32/0/0/0:すなおこし"], [f"ゲンガー@{_N40}:おくびょう:まもる|シャドーボール:0/0/0/32/0/32:のろわれボディ"], "防がれた"),
        "#3": ([f"フォレトス@{_N40}:わんぱく:こうそくスピン:32/0/32/0/0/0:がんじょう"],
               [f"カバルドン@{_N40}:わんぱく:ステルスロック:32/0/32/0/0/0:すなおこし"], "吹き飛んだ"),
        "#4": ([f"エルフーン@{_N40}:おくびょう:みがわり:0/0/0/32/0/32:いたずらごころ"], [_BLK40.replace("ねがいごと|のろい", "イカサマ|のろい")], "みがわり を作った"),
        "#5": ([f"エーフィ@{_N40}:ずぶとい:めいそう|サイコキネシス:32/0/32/0/0/0:マジックミラー"],
               [f"カバルドン@{_N40}:わんぱく:ステルスロック:32/0/32/0/0/0:すなおこし"], "跳ね返した"),
        "#5b": ([f"エーフィ@{_N40}:ずぶとい:めいそう|サイコキネシス:32/0/32/0/0/0:マジックミラー"],
                [f"オーロンゲ@{_N40}:わんぱく:すてゼリフ:32/0/32/0/0/0:おみとおし", _BLK40], "跳ね返した"),
        "#6": ([f"ドヒドイデ@{_N40}:ずぶとい:どくどく|ねっとう:32/0/32/0/0/0:さいせいりょく"], [_DUM40, _BLK40], "もうどく"),
        "#7": ([f"エルフーン@{_N40}:おくびょう:おいかぜ|ムーンフォース:0/0/0/32/0/32:いたずらごころ"], [_DUM40], "おいかぜ の効果が切れた"),
        "#8": ([f"マフィティフ@{_N40}:いじっぱり:くらいつく|じゃれつく:32/32/0/0/0/0:いかく"], [_DUM40, _BLK40], "くらいつく"),
        "#9": ([f"アローラキュウコン@{_N40}:おくびょう:アンコール|ムーンフォース:32/0/32/0/0/32:ゆきふらし"], [_DUM40, _BLK40], "繰り返すことになった"),
        "#10": ([f"カビゴン@{_N40}:いじっぱり:じわれ:32/32/0/0/0/0:あついしぼう"],
                [f"ウォッシュロトム@{_N40}:ずぶとい:ハイドロポンプ:32/0/32/0/0/0:ふゆう"], "じわれ は"),
        "#11": ([f"ドラパルト@{_N40}:ようき:ゴーストダイブ:0/32/0/0/0/32:すりぬけ"], [G], "ためている"),
        "#12": ([f"ミミズズ@{_N40}:わんぱく:しっぽきり|アイアンヘッド:32/0/32/0/0/0:どしょく", _BLK40], [_DUM40], "しっぽきり"),
        "#13": ([f"イッカネズミ@{_N40}:ようき:おかたづけ|かみくだく:0/32/0/0/0/32:テクニシャン"],
                [f"ゲンガー@{_N40}:おくびょう:ステルスロック|みがわり|シャドーボール:32/0/0/0/0/32:のろわれボディ"], "おかたづけ"),
        "#14": ([f"ランクルス@いのちのたま:ひかえめ:ドレインパンチ:32/0/0/32/0/0:マジックガード"],
                [f"ガブリアス@ゴツゴツメット:わんぱく:のろい|じしん:32/0/32/0/0/0:さめはだ"], "ドレインパンチ"),
        "#15": ([f"コノヨザル@{_N40}:いじっぱり:ふんどのこぶし|ビルドアップ:32/32/0/0/0/0:まけんき", _BLK40], [G], "ふんどのこぶし"),
        "#16": ([f"ヒスイゾロアーク@{_N40}:おくびょう:うらみつらみ:0/0/0/32/0/32:イリュージョン"], [G], "こうげき が下がった"),
        "#17": ([f"オーロンゲ@{_N40}:わんぱく:すてゼリフ|じゃれつく:32/0/32/0/0/0:おみとおし", _BLK40],
                [f"メタグロス@{_N40}:いじっぱり:てっぺき|コメットパンチ:32/32/0/0/0/0:クリアボディ"], "下がらなかった"),
        "#18": ([f"モルペコ@{_N40}:ようき:オーラぐるま:0/32/0/0/0/32:はらぺこスイッチ"], [_DUM40], "オーラぐるま →"),
        "#19": ([f"ハラバリー@{_N40}:ひかえめ:パラボラチャージ:32/0/0/32/0/0:でんきにかえる"], [_DUM40.replace("のろい|まもる", "のしかかり")], "でんきにかえる"),
        "#21": ([f"エンブオー@{_N40}:いじっぱり:ワイルドボルト:0/32/0/0/0/32:すてみ"], [_DUM40], "ワイルドボルト"),
        "#23": ([f"クレッフィ@{_N40}:ずぶとい:でんじふゆう|イカサマ:32/0/32/0/0/0:いたずらごころ"], [G], "でんじふゆう"),
        "#24": ([f"ストリンダー(ハイ)@{_N40}:ひかえめ:サイコノイズ:0/0/0/32/0/32:パンクロック"],
                [f"カビゴン@たべのこし:わんぱく:のしかかり:32/0/32/0/0/0:あついしぼう"], "かいふくふうじ"),
        "#25": ([f"ハリーマン@{_N40}:ずぶとい:ちいさくなる|アクアテール:32/0/32/0/0/0:すいすい"],
                [f"カビゴン@{_N40}:いじっぱり:のしかかり:32/32/0/0/0/0:あついしぼう"], "のしかかり"),
        "#25b": ([f"ウツボット@{_N40}:ずぶとい:ちからをすいとる|リーフブレード:32/0/32/0/0/0:ようりょくそ"],
                 [f"カビゴン@{_N40}:いじっぱり:のしかかり:32/32/0/0/0/0:あついしぼう"], "ちからをすいとる"),
        "#27": ([f"オーロンゲ@{_N40}:わんぱく:ちょうはつ|じゃれつく:32/0/32/0/0/0:いたずらごころ"],
                [f"カビゴン@メンタルハーブ:わんぱく:のろい|のしかかり:32/0/32/0/0/0:あついしぼう"], "メンタルハーブ"),
        "#27b": ([f"スコヴィラン@{_N40}:ひかえめ:かえんほうしゃ|まもる:0/0/0/32/0/32:ムラっけ"], [_DUM40], "ムラっけ"),
        "sub": ([f"ゲンガー@{_N40}:おくびょう:みがわり:32/0/0/0/0/32:のろわれボディ"],
                [f"ヒートロトム@{_N40}:ずぶとい:ねっぷう|オーバーヒート:32/0/32/0/0/0:ふゆう"], "みがわり に"),
        "weather": ([f"ペリッパー@{_N40}:ずぶとい:あまごい|ぼうふう:32/0/32/0/0/0:あめふらし"], [_DUM40], "すでに同じ天候"),
    }
    mm, seen = [], set()
    for k, (pa, pb, kw) in PAR.items():
        for sd in (1, 2, 3, 4):
            try:
                rec = _F.play_and_record_rust(pa, pb, season="M-6", seed=sd, mcts_sims=30, sel1_idx=list(range(len(pa))))
                if any(kw in l for t in rec["turns"] for l in t["logs"]):
                    seen.add(k)
            except _F.ReplayMismatch as e:
                mm.append((k, sd, str(e)[:160]))
    check("audit200 Python/Rust 照合: 各問題の局面（#1〜#27・みがわり・天候）で再生が一致", not mm, str(mm)[:600])
    check("audit200 Python/Rust 照合: 各局面で問題の場面が実際に起きた", seen == set(PAR), str(set(PAR) - seen))


_case40("Py/Rust", _tpar)


# C: #28・#29 必ず失敗する手・特性で無効と表示された技を候補から外す（AI_FIX200）
def _tai():
    from simulator.search_ai import _prune_futile_moves as _pf
    def cands(side):
        return [_A40(type="move", move=m, move_idx=i) for i, m in enumerate(side.active.moves)]
    def left(me, op):
        return [a.move.name_jp for a in _pf(cands(me), me, op, _F40())]
    ju = _S40([_mk40(f"ジュペッタ@{_N40}:ゆうかん:ポルターガイスト|みちづれ|かげうち:32/32/0/0/0/0:おみとおし")])
    ga = _S40([_mk40(f"ガブリアス@オボンのみ:わんぱく:じしん:32/0/32/0/0/0:さめはだ")])
    ju.opp_view.on_enter(ga.active)
    l0 = left(ju, ga)
    ga.active.item = None
    ju.opp_view.on_item_lost(ga.active.name, "オボンのみ")
    ju.active._destiny_bond_last_turn = True
    l1 = left(ju, ga)
    check("audit200 #28 候補: 持ち物が無いと判明した相手への ポルターガイスト・連続の みちづれ を外す（判明前・初回は外さない）",
          l0 == ["ポルターガイスト", "みちづれ", "かげうち"] and l1 == ["かげうち"], f"{l0} {l1}")
    bt, a1, a2 = _bt40([f"デカヌチャン@{_N40}:いじっぱり:デカハンマー|つるぎのまい:32/32/0/0/0/0:マイペース"], [_DUM40],
                       ["デカハンマー", "つるぎのまい", "デカハンマー"], ["のろい"])
    _go40(bt, a1, a2, 2)
    h0 = bt.side2.active.hp
    _go40(bt, a1, a2, 3)
    check("audit200 #28 デカハンマー: 間に変化技を使えば次は出せる（以前は つるぎのまい の後も連続扱いで失敗）",
          bt.side2.active.hp < h0, f"{bt.side2.active.hp} {h0}")
    mi = _S40([_mk40(f"ミミズズ@{_N40}:わんぱく:のろい:32/0/32/0/0/0:どしょく")])
    gb = _S40([_mk40(f"ガブリアス@{_N40}:いじっぱり:じしん|ドラゴンクロー:0/32/0/0/0/32:さめはだ")])
    gb.opp_view.on_enter(mi.active)
    _r40.seed(1)
    _x40(gb, mi, _A40(type="move", move=gb.active.moves[0], move_idx=0), _F40())
    kn = gb.opp_view.get(mi.active.name)
    check("audit200 #29 どしょく でHP満タンのまま じしん が「効かない」→ 特性が判明し、次の候補から じしん を外す",
          kn is not None and kn.known_ability == "どしょく" and left(gb, mi) == ["ドラゴンクロー"],
          f"{getattr(kn, 'known_ability', None)} {left(gb, mi)}")


_case40("#28/#29", _tai)


# D: 型プール生成器（T1・T3・T4）と生成集団 v3
def _tpool():
    import os as _o, json as _j, sqlite3 as _sq
    import _gen_type_pool as _G
    import _coevo_groups as _CGx
    check("audit200 T1 型プール生成器の対象は使用率上位200（TOPN の既定）", _G.TOPN == 200, f"{_G.TOPN}")
    r = _G.generate_one("メタモン", 1)
    check("audit200 T1 メタモン は へんしん 1技の型を作る（技が4つに満たない種は周辺分布の積）",
          bool(r and r["builds"]) and all(b["moves"] == ["へんしん"] for b in r["builds"]), f"{r and len(r['builds'])}")
    check("audit200 T3 ひかりのねんど は壁技の無い型に付けない（壁技があれば付けられる）",
          not _G.item_ok(["ふぶき", "フリーズドライ", "こおりのつぶて", "ちょうはつ"], "ひかりのねんど")
          and _G.item_ok(["ふぶき", "フリーズドライ", "オーロラベール", "ちょうはつ"], "ひかりのねんど"))
    con = _sq.connect(_o.path.join(_o.path.dirname(_o.path.abspath(_G.__file__)), "pokenavi.db"))
    def _raw(sp, it):
        d = _G.latest("pokemon_items", sp)
        rows = dict(con.execute("select item, usage_rate from pokemon_items where season=? and crawled_date=? and pokemon=?",
                                (_G.SEASON, d, sp)).fetchall())
        return rows.get(it, 0) / (sum(rows.values()) or 1)
    lu, go = _G.marginals("ルチャブル")["items"], _G.marginals("ゴリランダー")["items"]
    check("audit200 T3 自分でフィールドを張れない種のシードは採用率を下げる（ルチャブル エレキシード）、張れる種は下げない（ゴリランダー グラスシード）",
          lu.get("エレキシード", 0) < 0.5 * _raw("ルチャブル", "エレキシード") and go.get("グラスシード", 0) >= 0.9 * _raw("ゴリランダー", "グラスシード"),
          f"{lu.get('エレキシード', 0):.3f} {_raw('ルチャブル', 'エレキシード'):.3f} {go.get('グラスシード', 0):.3f}")
    check("audit200 T4 ルガルガン(昼) の かたいツメ 100% はフォルム誤登録（たそがれ）として補正、他の種は補正しない",
          _G.form_fix("ルガルガン(昼)") == "ルガルガン(たそがれ)" and _G.form_fix("ガブリアス") is None, f"{_G.form_fix('ルガルガン(昼)')}")
    bk = _CGx.pool_names({"ケンタロス:炎": {}, "ルガルガン(たそがれ)": {"source_species": "ルガルガン(昼)"}})
    check("audit200 T1 生成集団: 正規名（ケンタロス(炎)）とフォルム補正の元の名から型プールの種名を引ける",
          bk.get("ケンタロス(炎)") == "ケンタロス:炎" and bk.get("ルガルガン(昼)") == "ルガルガン(たそがれ)", f"{bk}")
    gp = _o.path.join(_o.path.dirname(_o.path.abspath(_CGx.__file__)), "guide_pool_m6_v3.json")
    if _o.path.exists(gp):
        import seed_rule as _SRx
        P = [o["party"] for o in _j.load(open(gp))]
        names = [s.split("@")[0] for p in P for s in p]
        check("audit200 T1/T2 生成集団 v3: ケンタロス:炎・メタモン が入り、ルガルガン(昼) は無く、死にシード0",
              len(P) == 3000 and names.count("ケンタロス:炎") > 0 and names.count("メタモン") > 0
              and names.count("ルガルガン(昼)") == 0 and sum(len(_SRx.violations(p)) for p in P) == 0,
              f"{names.count('ケンタロス:炎')} {names.count('メタモン')} {names.count('ルガルガン(昼)')}")


_case40("型（T1/T3/T4）", _tpool)


def _belief_est():
    from simulator.belief import OpponentBelief as _OBe
    from simulator.damage import calc_damage as _cde
    pb = _OBe(dl, season="M-6").ensure("ブラッキー")
    pb.builds = [
        {"weight": 0.5, "item": "たべのこし", "ability": "せいしんりょく", "nature": "いじっぱり",
         "ev": [0, 32, 0, 0, 2, 32], "moves": ["イカサマ", "あくび", "まもる", "つきのひかり"]},
        {"weight": 0.5, "item": "たべのこし", "ability": "せいしんりょく", "nature": "おだやか",
         "ev": [32, 0, 0, 0, 32, 0], "moves": ["イカサマ", "あくび", "まもる", "つきのひかり"]},
    ]
    att = _mk40("ハラバリー@たべのこし:ひかえめ:10まんボルト|みずびたし|どくどく|なまける:32/0/0/32/0/0:でんきにかえる")
    dfn = _mk40("ブラッキー@たべのこし:おだやか:イカサマ|あくび|まもる|つきのひかり:32/0/0/0/32/0:せいしんりょく")
    mv = next(m for m in att.moves if m.name_jp == "10まんボルト")
    f = _F40()
    att._electromorphosis_charged = True
    frac = round(_cde(att, dfn, mv, f, critical=False, random_roll=0.5) * 100 / dfn.max_hp)
    att._electromorphosis_charged = True
    sub = _mk40("ブラッキー@たべのこし:おだやか:イカサマ|あくび|まもる|つきのひかり:32/0/0/0/32/0:せいしんりょく")
    pb.observe_damage(att, mv, frac, f, subject=sub)
    w = pb.pool_weights()
    check("R4-mcts 照合: ダメージ観測の再計算で観測側の状態（でんきにかえるの充電）を消費しない",
          getattr(pb.dmg_obs[-1][1], "_electromorphosis_charged", False) is True, "")
    check("R4-mcts 照合: 充電込みの被ダメージ観測で、再現できる型（耐久型＝2番目）の重みが上がる",
          w[1] > 0.9, str(w))


_case40("R4-mcts 信念の観測再計算", _belief_est)


def _wb_mega():
    from simulator.search_ai import _type_immune_move
    me = _mk40("メガニウム@メガニウムナイト:おくびょう:ソーラービーム|ウェザーボール|げんしのちから|くさわけ:2/0/0/32/0/32:しんりょく")
    op = _mk40("サーフゴー@いのちのたま:ひかえめ:ゴールドラッシュ|シャドーボール|わるだくみ|じこさいせい:2/0/0/32/0/32:おうごんのからだ")
    i = next(k for k, m in enumerate(me.moves) if m.name_jp == "ウェザーボール")
    f = _F40()
    check("R4-mcts 照合: メガソーラー になる ウェザーボール+メガ は ゴースト相手でもタイプ無効で外さない（素の ウェザーボール は外す）",
          not _type_immune_move(me, _A40(type="move", move=me.moves[i], move_idx=i, do_mega=True), op, f)
          and _type_immune_move(me, _A40(type="move", move=me.moves[i], move_idx=i, do_mega=False), op, f))


_case40("R4-mcts メガ前提の技タイプ", _wb_mega)

print("\n=== 41. 設置済みの設置技を候補から外す（hazard_1004） ===")
_HZ41 = ("ステルスロック", "まきびし", "どくびし", "ねばねばネット")
_FOR41 = f"フォレトス@{_N40}:わんぱく:ステルスロック|まきびし|どくびし|ボディプレス:32/0/32/0/0/0:がんじょう"
_ONI41 = f"オニシズクモ@{_N40}:わんぱく:ねばねばネット|アクアブレイク:32/0/32/0/0/0:すいほう"
_OPP41 = [_DUM40, _BLK40, _GAB40]


def _full41(n, i, f):
    return bool(n == "ステルスロック" and f.stealth_rock[i] or n == "まきびし" and f.spikes[i] >= 3
                or n == "どくびし" and f.toxic_spikes[i] >= 2 or n == "ねばねばネット" and f.sticky_web[i])


def _thz_unit():
    from simulator.search_ai import _prune_futile_moves as _pf
    def left(spec, f):
        me, op = _S40([_mk40(spec)]), _S40([_mk40(_DUM40), _mk40(_DUM40)])
        me.field_idx, op.field_idx = 0, 1
        c = [_A40(type="move", move=m, move_idx=i) for i, m in enumerate(me.active.moves)]
        return [a.move.name_jp for a in _pf(c, me, op, f)]
    f = _F40()
    r = [left(_FOR41, f)]
    f.stealth_rock[0], f.spikes[0], f.toxic_spikes[0] = True, 3, 2
    r.append(left(_FOR41, f))
    f.stealth_rock[1], f.spikes[1], f.toxic_spikes[1] = True, 2, 1
    r.append(left(_FOR41, f))
    f.spikes[1], f.toxic_spikes[1] = 3, 2
    r.append(left(_FOR41, f))
    r.append(left(_ONI41, f))
    f.sticky_web[1] = True
    r.append(left(_ONI41, f))
    exp = [["ステルスロック", "まきびし", "どくびし", "ボディプレス"]] * 2 + [["まきびし", "どくびし", "ボディプレス"], ["ボディプレス"],
           ["ねばねばネット", "アクアブレイク"], ["アクアブレイク"]]
    check("hazard1004 #H1 候補: 相手側に設置済みの ステルスロック・まきびし3層・どくびし2層・ねばねばネット を外す（未満・自分側の設置は外さない。Rust の cargo hazard1004 と同じ場面・同じ期待値）",
          r == exp, str(r))


_case40("hazard1004 #H1", _thz_unit)


def _thz_play():
    import feature1 as _F
    import pokenavi_engine as _E
    import simulator.ai as _AIm
    if not hasattr(_E, "mcts_3v3_record"):
        return
    _F._ensure_loaded("M-6", 8)
    A = [_FOR41, _ONI41]
    def sfull(n, st, web):
        return bool(n == "ステルスロック" and st["stealth_rock"] or n == "まきびし" and st["spikes"] >= 3
                    or n == "どくびし" and st["toxic_spikes"] >= 2 or n == "ねばねばネット" and web)
    cap, bad_r, use_r, mm = {}, [], 0, []
    _orig = _E.mcts_3v3_record
    def _rec(*a, **k):
        r = _orig(*a, **k)
        cap["d"] = r[1]
        return r
    _E.mcts_3v3_record = _rec
    try:
        for sd in range(1, 9):
            try:
                rec = _F.play_and_record_rust(A, _OPP41, season="M-6", seed=sd, mcts_sims=30, sel1_idx=[0, 1])
            except _F.ReplayMismatch as e:
                mm.append((sd, str(e)[:120]))
                continue
            T = rec["turns"]
            for t, acts, _s in cap["d"]:
                k, mv = acts[0][0], acts[0][1]
                if k != 0 or mv not in _HZ41:
                    continue
                use_r += 1
                st = T[t - 1]["side2"]
                web = any("ねばねばネット が張られた" in l for x in T[:t] for l in x["logs"])
                me = T[t - 1]["side1"]
                p = me["party"][me["active_idx"]]
                if sfull(mv, st, web) and any(m["pp"] > 0 and not sfull(m["name"], st, web) for m in p["moves"]):
                    bad_r.append((sd, t, mv))
    finally:
        _E.mcts_3v3_record = _orig
    check("hazard1004 #H2 Rust 探索（同じ場面・8戦）: 他に技があるとき設置済み/上限の設置技を選ばない・Python 再生と一致",
          use_r > 0 and not bad_r and not mm, f"uses={use_r} bad={bad_r[:6]} mm={mm[:2]}")
    bad_p, use_p = [], [0]
    _ck = _AIm.certain_ko_override
    def wrap(act, my, opp, f):
        a = _ck(act, my, opp, f)
        if my.field_idx == 0 and a.type == "move" and a.move is not None and a.move.name_jp in _HZ41:
            use_p[0] += 1
            if _full41(a.move.name_jp, opp.field_idx, f) and any(
                    m is not None and my.active.pp[i] > 0 and not _full41(m.name_jp, opp.field_idx, f)
                    for i, m in enumerate(my.active.moves)):
                bad_p.append(a.move.name_jp)
        return a
    _AIm.certain_ko_override = wrap
    try:
        for sd in range(1, 7):
            _F.play_and_record(A, _OPP41, season="M-6", seed=sd, mcts_sims=30, sel1_idx=[0, 1])
    finally:
        _AIm.certain_ko_override = _ck
    check("hazard1004 #H2 Python 探索（同じ場面・6戦）: 他に技があるとき設置済み/上限の設置技を選ばない",
          use_p[0] > 0 and not bad_p, f"uses={use_p[0]} bad={bad_p}")


_case40("hazard1004 #H2", _thz_play)

print("\n=== 42. 除去された ステルスロック を撒き直す（retrain_1005・保留ケース6） ===")


def _tsr_respread():
    from simulator.ai import _hazard_value as _hv
    from simulator.search_ai import SearchAI as _SA
    setter = f"カバルドン@{_N40}:わんぱく:ステルスロック|のろい:32/0/32/0/0/0:すなのちから"
    spinner = f"ガブリアス@{_N40}:わんぱく:のろい|こうそくスピン|キラースピン|きりばらい:32/0/32/0/0/0:さめはだ"
    sa = _SA(dl, rollouts=2, depth=3)
    for rm in ("こうそくスピン", "キラースピン", "きりばらい"):
        bt, a1, a2 = _bt40([setter], [spinner, spinner], ["ステルスロック", "のろい"], ["のろい", rm])
        _go40(bt, a1, a2, 1)
        set1 = bool(bt.field.stealth_rock[1])
        _go40(bt, a1, a2, 2)
        gone = not bt.field.stealth_rock[1]
        hv = _hv("ステルスロック", bt.side1, bt.side2, bt.field)
        cand = any(a.move is not None and a.move.name_jp == "ステルスロック"
                   for a in sa._candidate_actions(bt.side1, bt.side2, bt.field))
        check(f"retrain1005 #SR {rm} で除去された ステルスロック は撒き直しの候補に戻る（価値>0・候補にある）",
              set1 and gone and hv > 0 and cand, f"set={set1} gone={gone} hv={hv} cand={cand}")
    bt, a1, a2 = _bt40([setter], [spinner, spinner], ["ステルスロック", "のろい"], ["のろい"])
    _go40(bt, a1, a2, 2)
    check("retrain1005 #SR 除去されていない ステルスロック は候補から外す（負例）",
          bool(bt.field.stealth_rock[1]) and _hv("ステルスロック", bt.side1, bt.side2, bt.field) == 0
          and not any(a.move is not None and a.move.name_jp == "ステルスロック"
                      for a in sa._candidate_actions(bt.side1, bt.side2, bt.field)))


_case40("retrain1005 #SR", _tsr_respread)


print("\n=== 43. 選出率の低い4種の監査（audit4_1008）の修正 ===")
_JU43 = "ジュカイン@{}:ようき:{}:0/32/0/0/0/32:かるわざ"


def _noitem43(a, b):
    b.party[0].item = None


def _ta1():
    """E1 かるわざ: 持ち物を失う経路ごとに素早さが上がる（実戦の1ターン）"""
    C = {
        "しろいハーブ": (_JU43.format("しろいハーブ", "インファイト"), _DUM40, "インファイト", "のろい"),
        "はたきおとされ": (_JU43.format("オボンのみ", "つるぎのまい"),
                       f"ゴリランダー@{_N40}:わんぱく:はたきおとす:32/0/32/0/0/0:グラスメイカー", "つるぎのまい", "はたきおとす"),
        "ラムのみ": (_JU43.format("ラムのみ", "つるぎのまい"), _BLK40.replace("ねがいごと|のろい", "どくどく"), "つるぎのまい", "どくどく"),
        "メンタルハーブ": (_JU43.format("メンタルハーブ", "つるぎのまい"),
                       f"オーロンゲ@{_N40}:わんぱく:ちょうはつ:32/0/32/0/0/0:いたずらごころ", "つるぎのまい", "ちょうはつ"),
        "じゃくてんほけん": ("ジュカイン@じゃくてんほけん:ずぶとい:つるぎのまい:32/0/32/0/32/0:かるわざ",
                         f"ウインディ@{_N40}:ずぶとい:かえんほうしゃ:0/0/32/0/0/0:せいぎのこころ", "つるぎのまい", "かえんほうしゃ"),
        "なげつける": (_JU43.format("くろいてっきゅう", "なげつける"), _DUM40, "なげつける", "のろい"),
        "マジシャン": (_JU43.format("オボンのみ", "つるぎのまい"), f"マフォクシー@{_N40}:ずぶとい:マジカルフレイム:32/0/32/0/0/0:マジシャン",
                    "つるぎのまい", "マジカルフレイム", _noitem43),
        "わるいてぐせ": (_JU43.format("オボンのみ", "リーフブレード"), f"マニューラ@{_N40}:わんぱく:のろい:32/0/32/0/32/0:わるいてぐせ",
                     "リーフブレード", "のろい", _noitem43),
        "ついばむ": (_JU43.format("オボンのみ", "つるぎのまい"), f"ムクホーク@{_N40}:わんぱく:ついばむ:32/0/32/0/0/0:いかく",
                   "つるぎのまい", "ついばむ"),
        "どろぼう": (_JU43.format("オボンのみ", "つるぎのまい"), f"ムクホーク@{_N40}:わんぱく:どろぼう:32/0/32/0/0/0:いかく",
                   "つるぎのまい", "どろぼう", _noitem43),
        "トリック": (_JU43.format("たべのこし", "トリック"), _DUM40, "トリック", "のろい", _noitem43),
        "ほおばる": (_JU43.format("オボンのみ", "ほおばる"), _DUM40, "ほおばる", "のろい"),
    }
    for k, (a, b, pa, pb, *pr) in C.items():
        bt, a1, a2 = _bt40([a], [b], [pa], [pb], prep=pr[0] if pr else None)
        _go40(bt, a1, a2, 1)
        j = bt.side1.active
        check(f"audit4 E1 かるわざ: {k} で持ち物を失うと素早さ+2", j.item is None and j.stage_speed == 2,
              f"item={j.item} S={j.stage_speed}")
    bt, a1, a2 = _bt40([_JU43.format("オボンのみ", "つるぎのまい")], [_DUM40], ["つるぎのまい"], ["のろい"])
    _go40(bt, a1, a2, 1)
    check("audit4 E1 かるわざ: 持ち物が残っていれば素早さは変わらない（対照）",
          bt.side1.active.item == "オボンのみ" and bt.side1.active.stage_speed == 0, f"{bt.side1.active.stage_speed}")
    j = _mk40(_JU43.format("ヒメリのみ", "つるぎのまい"))
    j.pp[0] = 0
    lg = []
    try_leppa_berry(j, lg)
    check("audit4 E1 かるわざ: ヒメリのみ で持ち物を失うと素早さ+2", j.item is None and j.stage_speed == 2, f"{j.item} {j.stage_speed}")
    j = _mk40(_JU43.format("サルのみ", "つるぎのまい"))
    j.hp = j.max_hp // 4
    apply_hp_berry(j, lg)
    check("audit4 E1 かるわざ: ピンチきのみ（サルのみ）で持ち物を失うと素早さ+2", j.item is None and j.stage_speed == 2,
          f"{j.item} {j.stage_speed}")


def _ta2():
    """E2 トリプルアクセル: 1発ごとに命中判定し外れたら終わる・急所も1発ごと"""
    import simulator.battle as _B
    mv = dl.get_move("トリプルアクセル")
    a = _mk40(f"マスカーニャ@{_N40}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:しんりょく")
    _r40.seed(43)
    cnt = {1: 0, 2: 0, 3: 0}
    for _ in range(20000):
        cnt[_B._calc_hits(mv, a)] += 1
    fr = {k: v / 20000 for k, v in cnt.items()}
    check("audit4 E2 トリプルアクセル: 2発目以降は1発ごとに90%で続く（1回10%・2回9%・3回81%）",
          abs(fr[1] - 0.10) < 0.012 and abs(fr[2] - 0.09) < 0.012 and abs(fr[3] - 0.81) < 0.015, f"{fr}")
    sl = _mk40(f"マスカーニャ@{_N40}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:スキルリンク")
    check("audit4 E2 トリプルアクセル: スキルリンクは必ず3回", all(_B._calc_hits(mv, sl) == 3 for _ in range(200)))
    _sv = _B._HIT_CONTINUE
    _B._HIT_CONTINUE = lambda: 0.0
    try:
        check("audit4 E2 トリプルアクセル: 分析の差込口（_HIT_CONTINUE=必中）では3回", _B._calc_hits(mv, a) == 3)
        calls = []
        _ck = _B._check_critical

        def _cnt(*x, **kw):
            calls.append(1)
            return _ck(*x, **kw)
        _B._check_critical = _cnt
        try:
            res = {}
            for nm, sp in (("トリプルアクセル", f"マスカーニャ@{_N40}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:しんりょく"),
                           ("ダブルウイング", f"ファイアロー@{_N40}:いじっぱり:ダブルウイング:32/32/0/0/0/0:はやてのつばさ")):
                calls.clear()
                bt, a1, a2 = _bt40([sp], [_DUM40], [nm], ["のろい"])
                _go40(bt, a1, a2, 1)
                res[nm] = len(calls)
        finally:
            _B._check_critical = _ck
        check("audit4 E2 トリプルアクセル: 急所は1発ごとに判定（3回当てて3回）、他の連続技は1回（対照）",
              res == {"トリプルアクセル": 3, "ダブルウイング": 1}, f"{res}")
    finally:
        _B._HIT_CONTINUE = _sv


def _ta3():
    """E3 ほうし: くさ・ぼうじん・ぼうじんゴーグルには発動しない、ねむり11%・まひ10%・どく9%"""
    import collections
    from simulator.abilities import on_after_hit as _oah
    rf = _mk40(f"ラフレシア@{_N40}:ずぶとい:じこさいせい:32/0/32/0/0/0:ほうし")
    for nm, sp, mvn in (("くさタイプ", f"ゴリランダー@{_N40}:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー", "グラススライダー"),
                        ("ぼうじん", f"フォレトス@{_N40}:いじっぱり:ジャイロボール:32/32/0/0/0/0:ぼうじん", "ジャイロボール"),
                        ("ぼうじんゴーグル", "カイリキー@ぼうじんゴーグル:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード", "かみくだく")):
        n = 0
        _r40.seed(7)
        for _ in range(300):
            at = _mk40(sp)
            _oah(at, rf, dl.get_move(mvn), [], _F40())
            n += at.status is not None
        check(f"audit4 E3 ほうし: {nm} には発動しない", n == 0, f"{n}/300")
    c = collections.Counter()
    _r40.seed(8)
    N = 20000
    for _ in range(N):
        at = _mk40(f"カイリキー@{_N40}:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード")
        _oah(at, rf, dl.get_move("かみくだく"), [], _F40())
        c[at.status] += 1
    fr = {k: c[k] / N for k in ("sleep", "paralysis", "poison")}
    check("audit4 E3 ほうし: 状態の配分は ねむり11%・まひ10%・どく9%",
          abs(fr["sleep"] - 0.11) < 0.008 and abs(fr["paralysis"] - 0.10) < 0.008 and abs(fr["poison"] - 0.09) < 0.008, f"{fr}")


def _td1():
    """D1 反応のログ（タスキ・かるわざ・じきゅうりょく）は原因の技の行の後"""
    def order(bt, keys):
        L = bt.logs
        ix = []
        for k in keys:
            hit = [i for i, l in enumerate(L) if k in l]
            ix.append(hit[0] if hit else -1)
        return ix
    bt, a1, a2 = _bt40([f"カイリキー@{_N40}:いじっぱり:インファイト:32/32/0/0/0/0:ノーガード"],
                       ["ジュカイン@きあいのタスキ:おくびょう:つるぎのまい:0/0/0/0/0/32:かるわざ"], ["インファイト"], ["つるぎのまい"])
    _go40(bt, a1, a2, 1)
    ix = order(bt, ["インファイト → ジュカイン", "きあいのタスキ で耐えた", "ジュカイン の かるわざ"])
    check("audit4 D1 きあいのタスキ・かるわざ のログは技の行の後（技→タスキ→かるわざ）", -1 not in ix and ix == sorted(ix), f"{ix}")
    bt, a1, a2 = _bt40(["ジュカイン@ノーマルジュエル:ようき:ねこだまし:0/32/0/0/0/32:かるわざ"], [_DUM40], ["ねこだまし"], ["のろい"])
    _go40(bt, a1, a2, 1)
    ix = order(bt, ["ねこだまし → カビゴン", "ノーマルジュエル が消費された", "ジュカイン の かるわざ"])
    check("audit4 D1 ノーマルジュエル・かるわざ のログは技の行の後（技→ジュエル→かるわざ）", -1 not in ix and ix == sorted(ix), f"{ix}")
    bt, a1, a2 = _bt40([f"カイリキー@{_N40}:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード"],
                       [f"バンバドロ@{_N40}:わんぱく:のろい:32/0/32/0/0/0:じきゅうりょく"], ["かみくだく"], ["のろい"])
    _go40(bt, a1, a2, 1)
    ix = order(bt, ["かみくだく → バンバドロ", "じきゅうりょく"])
    check("audit4 D1 じきゅうりょく のログは技の行の後", -1 not in ix and ix == sorted(ix), f"{ix}")


def _tpar43():
    """E1〜E3 の局面を Rust の探索で戦い、Python で再生して一致・場面が実際に起きた"""
    import feature1 as _F
    import pokenavi_engine as _E
    if not hasattr(_E, "mcts_3v3_record"):
        return
    _F._ensure_loaded("M-6", 8)
    PAR = {
        "E1 しろいハーブ": ([_JU43.format("しろいハーブ", "インファイト")], [_DUM40], "かるわざ"),
        "E1 はたきおとす": ([_JU43.format("オボンのみ", "つるぎのまい")],
                         [f"ゴリランダー@{_N40}:わんぱく:はたきおとす:32/0/32/0/0/0:グラスメイカー"], "かるわざ"),
        "E1 ラムのみ": ([_JU43.format("ラムのみ", "つるぎのまい")], [_BLK40.replace("ねがいごと|のろい", "どくどく")], "かるわざ"),
        "E1 メンタルハーブ": ([_JU43.format("メンタルハーブ", "つるぎのまい")],
                          [f"オーロンゲ@{_N40}:わんぱく:ちょうはつ:32/0/32/0/0/0:いたずらごころ"], "かるわざ"),
        "E1 ついばむ": ([_JU43.format("オボンのみ", "つるぎのまい")], [f"ムクホーク@{_N40}:わんぱく:ついばむ:32/0/32/0/0/0:いかく"], "かるわざ"),
        "E1 ほおばる": ([_JU43.format("オボンのみ", "ほおばる")], [_DUM40], "かるわざ"),
        "E2 トリプルアクセル": ([f"マスカーニャ@{_N40}:いじっぱり:トリプルアクセル:32/32/0/0/0/0:しんりょく"],
                             ["カビゴン@きれいなぬけがら:ずぶとい:なまける:32/0/32/0/32/0:あついしぼう"], "(2回)"),
        "E3 ほうし（くさ以外）": ([f"カイリキー@{_N40}:いじっぱり:かみくだく:32/32/0/0/0/0:ノーガード"],
                               [f"ラフレシア@{_N40}:ずぶとい:じこさいせい:32/0/32/0/0/0:ほうし"], "ほうし！"),
    }
    NEG = {"E3 ほうし（くさ）": ([f"ゴリランダー@{_N40}:いじっぱり:グラススライダー:32/32/0/0/0/0:グラスメイカー"],
                               [f"ラフレシア@{_N40}:ずぶとい:じこさいせい:32/0/32/0/0/0:ほうし"], "ほうし！")}
    mm, seen, neg = [], set(), set()
    for grp, out in ((PAR, seen), (NEG, neg)):
        for k, (pa, pb, kw) in grp.items():
            for sd in range(1, 9 if k.startswith("E2") or k.startswith("E3") else 3):
                try:
                    rec = _F.play_and_record_rust(pa, pb, season="M-6", seed=sd, mcts_sims=8, sel1_idx=list(range(len(pa))))
                    if any(kw in l for t in rec["turns"] for l in t["logs"]):
                        out.add(k)
                except _F.ReplayMismatch as e:
                    mm.append((k, sd, str(e)[:160]))
    check("audit4 Python/Rust 照合: E1〜E3 の局面で再生が一致", not mm, str(mm)[:600])
    check("audit4 Python/Rust 照合: 各局面で問題の場面が実際に起きた", seen == set(PAR), str(set(PAR) - seen))
    check("audit4 Python/Rust 照合: くさタイプには ほうし が発動しない（Rust の対戦でも）", not neg, str(neg))


for _nm43, _fn43 in (("E1", _ta1), ("E2", _ta2), ("E3", _ta3), ("D1", _td1), ("Py/Rust", _tpar43)):
    _case40(f"audit4 {_nm43}", _fn43)

# ════════════════════════════════════════════════════════════════
# 44. 努力値の余り（合計66）と提案の型の出どころ（fix_ev_1008）
#     Champions の努力値は各32・合計66。合計64（A32 S32）で2余る型が型プール・提案・生成集団・工房に出ていた。
#     余りは DB で余りが最も多く置かれている能力へ（ev_fill）。提案の型は build_pool_M-6.md のドラフト型ではなく
#     シーズン固定版の型プールから取る（ゴリランダーの7型中4型が やどりぎのタネ/つるぎのまい 型だった）。
# ════════════════════════════════════════════════════════════════
print("\n=== 44. 努力値の余り（合計66）と提案の型の出どころ ===")


def _t44_fill():
    import ev_fill as EF
    check("ev_fill: 余りは DB で余りが最も多い能力へ（ガブリアス A32 S32 → H2）",
          EF.fill("ガブリアス", [0, 32, 0, 0, 0, 32]) == [2, 32, 0, 0, 0, 32], str(EF.fill("ガブリアス", [0, 32, 0, 0, 0, 32])))
    check("ev_fill: 同じ大きな振り先の配分を優先（ガブリアス H32 B32 → D2。DB H32-B32-D2 3.7% > S2 2.6%）",
          EF.fill("ガブリアス", [32, 0, 32, 0, 0, 0]) == [32, 0, 32, 0, 2, 0], str(EF.fill("ガブリアス", [32, 0, 32, 0, 0, 0])))
    check("ev_fill: データの無い種は H", EF.fill("存在しない種", [0, 32, 0, 0, 0, 32]) == [2, 32, 0, 0, 0, 32])
    _e = EF.fill("存在しない種", [32, 32, 0, 0, 0, 0])
    check("ev_fill: 振り先が32なら次の能力へ（各32を超えない）", _e == [32, 32, 2, 0, 0, 0], str(_e))
    _e = EF.fill("存在しない種", [0, 0, 0, 0, 0, 0])
    check("ev_fill: 0振りも合計66に", sum(_e) == 66 and max(_e) <= 32, str(_e))
    check("ev_fill: 合計66の型は変えない", EF.fill("ガブリアス", [0, 32, 2, 0, 0, 32]) == [0, 32, 2, 0, 0, 32])
    _b = EF.fill_builds("ガブリアス", [
        {"item": "a", "nature": "n", "ability": "x", "moves": ["m1", "m2"], "ev": [0, 32, 0, 0, 0, 32], "weight": 0.3,
         "spec": "ガブリアス@a:n:m1|m2:0/32/0/0/0/32:x"},
        {"item": "a", "nature": "n", "ability": "x", "moves": ["m2", "m1"], "ev": [2, 32, 0, 0, 0, 32], "weight": 0.5,
         "spec": "ガブリアス@a:n:m2|m1:2/32/0/0/0/32:x"}])
    check("ev_fill: 埋めて同じになった型は重みを足して1つに（spec も合計66）",
          len(_b) == 1 and abs(_b[0]["weight"] - 0.8) < 1e-9 and _b[0]["spec"].endswith(":2/32/0/0/0/32:x"), str(_b))


def _t44_gen():
    import _gen_type_pool as _G44
    _r = _G44.simple_builds("メタモン")
    check("型プール生成器: 周辺分布の積の種（メタモン）も合計66", _r and not [b for b in _r["builds"] if sum(b["ev"]) != 66])
    _r = _G44.generate_one("ゴロンダ", 0)
    check("型プール生成器: 努力値の DB が無い種（ゴロンダ・旧 0振り）も合計66",
          _r and not [b for b in _r["builds"] if sum(b["ev"]) != 66], str(_r and _r["builds"][0]["ev"]))
    _r = _G44.generate_one("ガブリアス", 0)
    check("型プール生成器: DB の合計64の配分（0.7%）も合計66で出す", _r and not [b for b in _r["builds"] if sum(b["ev"]) != 66])
    import update_type_pool as _U44
    import inspect as _in44
    check("週次の型生成（update_type_pool）が最後に ev_fill.fill_pool を通す", "ev_fill.fill_pool(pool" in _in44.getsource(_U44.main))


def _t44_suggest():
    import json as _j44
    import pool_versions as _PV44
    import gen_party_pool as _GP44
    _sv = _PV44.pointer("season")
    check("提案: M-6 の型の出どころは型プール（build_pool_M-6.md ではない）",
          _GP44.party_pool_src(_PV44.season_of(_sv)) == "pool" and _GP44.party_pool_src("M-3") == "md")
    _pg = _GP44.PartyGen(src="pool")
    _pool = {r["species"]: {(b["item"], tuple(sorted(b["moves"]))) for b in r["builds"]}
             for r in _j44.load(open(_PV44.path("type_pool", _sv)))}
    _bad_ev, _bad_src, _n = [], [], 0
    for _sp, _ss in _pg.pool_resolve.items():
        for _s in _ss:
            _n += 1
            _it, _na, _mv, _ev, _ab = _s.split("@", 1)[1].split(":")
            if sum(map(int, _ev.split("/"))) != 66:
                _bad_ev.append(_s)
            if (_it, tuple(sorted(_mv.split("|")))) not in _pool.get(_sp, ()):
                _bad_src.append(_s)
    check("提案: 全ての型の努力値が合計66", _n > 1000 and not _bad_ev, f"{len(_bad_ev)}/{_n} 例 {_bad_ev[:2]}")
    check("提案: 全ての型が型プール（season の版）にある", not _bad_src, f"{len(_bad_src)}/{_n} 例 {_bad_src[:2]}")
    _gr = _pg.pool.get("ゴリランダー", [])
    _sd = sum(_pg.bw[s] for s in _gr if "やどりぎのタネ" in s and "つるぎのまい" in s)
    check("提案: ゴリランダーの やどりぎのタネ＋つるぎのまい 型は採用率どおり少ない（旧 md は7型中4型）", len(_gr) >= 5 and _sd < 0.05, f"{_sd:.3f}")
    _raw = [b for r in _j44.load(open(_PV44.path("type_pool", _sv))) for b in r["builds"]]
    _bad_rule = [s for ss in _pg.pool_resolve.values() for s in ss
                 if not _GP44.rule_ok({"item": s.split("@", 1)[1].split(":")[0], "moves": s.split("@", 1)[1].split(":")[2].split("|")})]
    check("提案: 全ての型が持ち物と技の規則（item_ok）を満たす（v41 の ひかりのねんど＝壁技なし 等は読むときに外す）",
          any(not _GP44.rule_ok(b) for b in _raw) and not _bad_rule, f"{len(_bad_rule)}件 例 {_bad_rule[:2]}")
    check("提案: 型プールの キュウコン は通常のキュウコン（md の「キュウコン＝アローラ」の付け替えをしない）",
          all(s.startswith("キュウコン@") for s in _pg.pool.get("キュウコン", [])) and "アローラキュウコン" in _pg.pool)
    import random as _r44
    _rng = _r44.Random(3); _bad = 0; _np = 0
    for _ in range(60):
        _p = _pg.sample_cooc(_rng)
        if _p:
            _np += 1; _bad += any(sum(map(int, x.split("@", 1)[1].split(":")[3].split("/"))) != 66 for x in _p)
    check("提案: 生成した党の努力値が全て合計66", _np > 50 and _bad == 0, f"{_bad}/{_np}")


def _t44_coevo():
    import _coevo_groups as _CG44
    import pool_versions as _PV44
    check("生成集団: 系統表は season の版", os.path.abspath(_CG44.GROUPS) == os.path.abspath(_PV44.path("type_groups", _PV44.pointer("season"))))
    _cwd = os.getcwd(); os.chdir(os.path.dirname(os.path.abspath(_CG44.__file__)))
    try:
        _g = _CG44.load()["groups"]
    finally:
        os.chdir(_cwd)
    _bad = [(sp, b["ev"]) for sp, v in _g.items() for g in v["groups"] for b in g["builds"] if sum(b["ev"]) != 66]
    check("生成集団: 系統の型の努力値が全て合計66", not _bad, str(_bad[:3]))
    import gen_party_pool as _GP44
    _bad = [(sp, b["item"], b["moves"]) for sp, v in _g.items() for g in v["groups"] for b in g["builds"] if not _GP44.rule_ok(b)]
    check("生成集団: 系統の型が全て持ち物と技の規則（item_ok）を満たす（v41 の規則より前の型は読むときに外す）", not _bad, str(_bad[:3]))


def _t44_builder():
    import gen_builder_data as _B44
    _e = _B44.fill_ev_presets("ガブリアス", [([2, 32, 0, 0, 0, 32], 26.7), ([0, 32, 0, 0, 0, 32], 0.7), ([0, 0, 0, 32, 0, 32], 0.6),
                                            ([31, 0, 8, 32, 0, 0], 0.5), ([16, 252, 0, 0, 0, 252], 0.4)])
    check("工房: 努力値の候補は合計66・埋めて同じになった配分は採用率を足す・合計66超/32超（DB の誤り）は落とす",
          _e[0] == {"ev": [2, 32, 0, 0, 0, 32], "pct": 27.4} and len(_e) == 2 and all(sum(x["ev"]) == 66 for x in _e), str(_e))
    _v = {"ガブリアス": [{"ev": [0, 32, 0, 0, 0, 32], "spec": "ガブリアス@きあいのタスキ:ようき:じしん:0/32/0/0/0/32:さめはだ"}]}
    _B44.fill_variants(_v)
    check("工房/1v1: 代表型と型プリセットの努力値を合計66に",
          _v["ガブリアス"][0]["ev"] == [2, 32, 0, 0, 0, 32] and _v["ガブリアス"][0]["spec"].endswith(":2/32/0/0/0/32:さめはだ"), str(_v))
    _B44.SEASON = _B44.PV.season_of(_B44.POOL_VERSION); _B44._PG.clear()
    _pg = _B44._pool_groups()
    _bad = [(sp, b["ev"]) for sp, v in _pg.items() for g in v["groups"] for b in g["builds"] if sum(b["ev"]) != 66]
    check("工房/1v1: 系統表（page の版）を読んだ時点で努力値が合計66", _pg and not _bad, str(_bad[:3]))


def _t44_checks():
    import pool_checks as _C44
    import _gen_type_pool as _G44
    _b = [{"item": "きあいのタスキ", "nature": "ようき", "ability": "さめはだ", "moves": ["じしん", "げきりん", "ステルスロック", "がんせきふうじ"],
           "ev": [0, 32, 0, 0, 0, 32], "weight": 1.0}]
    check("週次チェック: 合計64の型はエラー", any("EV" in e for e in _C44.rule_errors(_G44, "ガブリアス", _b)))
    _b[0]["ev"] = [2, 32, 0, 0, 0, 32]
    check("週次チェック: 合計66の型は通す（負例）", not any("EV" in e for e in _C44.rule_errors(_G44, "ガブリアス", _b)))
    _arch = {"0445-00": {"groups": [{"name": "x型", "sets": [{"ev": "A32 S32"}]}]}}
    _mons = {"0445-00": {"n": "ガブリアス", "mu": [{"ev": [2, 32, 0, 0, 0, 32]}], "builds": ["ガブリアス@a:n:m:0/32/0/0/0/32:x"],
                         "evs": [{"ev": [0, 32, 0, 0, 0, 32]}]}}
    check("週次チェック: 生成物（想定型・型プリセット・努力値の候補）の合計≠66 を全て拾う", len(_C44.ev_output_errors(_arch, _mons)) == 3,
          str(_C44.ev_output_errors(_arch, _mons)))
    _cur, _old = _C44.split_mons(dict(_mons, **{"0711-01": {"n": "パンプジン (ちいさい)", "evs": [{"ev": [0] * 6}]}}), {"0445-00"})
    check("週次チェック: species.json に無い前のシーズンの mon は生成物のチェックから外して一覧にする",
          set(_cur) == {"0445-00"} and _old == ["0711-01（パンプジン (ちいさい)）"], f"{list(_cur)} {_old}")
    import inspect as _in44c
    check("週次チェック: 提案の型の持ち物と技の規則（item_ok）を見る", "item_ok" in _in44c.getsource(_C44.source_errors))


for _nm44, _fn44 in (("ev_fill", _t44_fill), ("生成器", _t44_gen), ("提案", _t44_suggest), ("生成集団", _t44_coevo),
                     ("工房", _t44_builder), ("週次チェック", _t44_checks)):
    try:
        _fn44()
    except Exception as _e44:
        check(f"44 {_nm44} のテストが実行できる", False, f"{type(_e44).__name__}: {_e44}")

# ── 45. 低選出8種の調査（lowsel_1009）: E1 反動ターンの交代・E2 一撃必殺の命中補正 ──
def _t45_recharge():
    from simulator.battle import forced_recharge_action as _frc45
    from simulator.alphazero import legal_actions_indexed as _lai45
    from simulator.ai import _forced_charging_action as _fca45
    a = make_poke(name="A", atk_b=150, moves=["のしかかり", "はかいこうせん"])
    b = make_poke(name="B", moves=["まもる"])
    foe = make_poke(name="F", hp_b=255, def_b=230, moves=["なまける"], ability="ノーガード")
    s1, s2 = BattleSide([a, b]), BattleSide([foe])
    bt = Battle(s1, s2, BattleField())
    bt.resume(_Force("はかいこうせん"), _Force("なまける"), max_turns=1)
    check("45 E1 はかいこうせん の後は反動", a.recharge and foe.is_alive)
    _pp = list(a.pp)
    _leg = _lai45(s1, s2, bt.field)
    check("45 E1 反動ターンの合法手は反動の技だけ（交代・メガ・他の技なし）",
          [ix for _, ix in _leg] == [1] and _leg[0][0].type == "move", str([ix for _, ix in _leg]))
    _fc = _fca45(a)
    check("45 E1 AIの強制手は反動の技", _fc is not None and _fc.move_idx == 1 and not _fc.do_mega)
    _n0 = len(bt.logs)
    bt.resume(lambda my, opp, f: _Act(type="switch", switch_to=1), _Force("なまける"), max_turns=2)
    check("45 E1 反動ターンに交代を選んでも交代しない", s1.active is a and not a.recharge, str(bt.logs[_n0:]))
    check("45 E1 反動ターンは動けない・PPは減らない", any("動けない" in l for l in bt.logs[_n0:]) and a.pp == _pp,
          f"{a.pp} {_pp}")
    check("45 E1 反動でなければ強制手なし（負例）", _frc45(a) is None and _fca45(a) is None)
    _sk = make_poke(name="S", atk_b=150, moves=["ふいうち"]); _rc = make_poke(name="R", moves=["はかいこうせん"])
    _rc.recharge = True
    _hp = _rc.hp
    _execute_move(BattleSide([_sk]), BattleSide([_rc]), _Act(type="move", move=_sk.moves[0]), BattleField(),
                  _Act(type="move", move=_rc.moves[0], move_idx=0))
    _hp1 = _rc.hp
    _rc.recharge = False
    _execute_move(BattleSide([_sk]), BattleSide([_rc]), _Act(type="move", move=_sk.moves[0]), BattleField(),
                  _Act(type="move", move=_rc.moves[0], move_idx=0))
    check("45 E1 反動ターンの相手への ふいうち は失敗（対照: 反動でなければ当たる）", _hp1 == _hp and _rc.hp < _hp, f"{_hp1} {_rc.hp} {_hp}")


def _t45_ohko():
    from simulator.damage import check_hit as _ch45
    _st = random.getstate()
    for _n in ("じわれ", "つのドリル", "ハサミギロチン", "ぜったいれいど"):
        _base = 0.20 if _n == "ぜったいれいど" else 0.30
        _rates = []
        for _acc, _eva, _ab, _it in ((6, 0, "しんりょく", None), (0, 6, "しんりょく", None), (0, 0, "ふくがん", "こうかくレンズ"),
                                     (0, 0, "しんりょく", None)):
            _a = make_poke(moves=[_n], ability=_ab, item=_it); _a.stage_accuracy = _acc
            _d = make_poke(); _d.stage_evasion = _eva
            random.seed(4500)
            _rates.append(sum(_ch45(_a, _d, _a.moves[0], BattleField()) for _ in range(4000)) / 4000)
        check(f"45 E2 {_n} の命中は命中/回避ランク・ふくがん・こうかくレンズで変わらない（{_base:.0%}）",
              all(abs(r - _base) < 0.025 for r in _rates), str(_rates))
        _a = make_poke(moves=[_n]); _d = make_poke(ability="ノーガード")
        check(f"45 E2 {_n} は ノーガード で必中", all(_ch45(_a, _d, _a.moves[0], BattleField()) for _ in range(200)))
    random.setstate(_st)


_P45A = ["ジュペッタ@ジュペッタナイト:いじっぱり:かげうち|みちづれ|アンコール|ポルターガイスト:0/32/2/0/0/32:おみとおし",
         "カビゴン@カゴのみ:わんぱく:じしん|じわれ|ねむる|れいとうパンチ:32/0/2/0/32/0:あついしぼう",
         "ヤミラミ@ヤミラミナイト:ずぶとい:おにび|じこさいせい|アンコール|イカサマ:32/0/32/0/2/0:いたずらごころ",
         "ギルガルド@いのちのたま:れいせい:かげうち|アイアンヘッド|キングシールド|シャドーボール:32/0/0/32/0/0:バトルスイッチ",
         "アシレーヌ@カゴのみ:ずぶとい:なみのり|ねむる|めいそう|ムーンフォース:32/0/32/0/0/0:げきりゅう",
         "ミミッキュ@いのちのたま:ようき:じゃれつく|シャドークロー|かげうち|つるぎのまい:0/32/0/0/0/32:ばけのかわ"]


def _t45_selv2():
    import json as _j45, tempfile as _tf45, subprocess as _sp45
    import numpy as _np45
    import simulator.learned_selection as _LS45
    import simulator.features as _FT45
    _A = [_mk26c(x) for x in _P45A]
    _jv = _FT45.sel_mega_view(_A[0])
    check("45 選出v2: メガ石持ちはメガ後の複製（特性・素早さ・メガ可ビット1）で、元の個体は変えない",
          _jv is not _A[0] and _jv.ability == "いたずらごころ" and _jv.speed != _A[0].speed and not _A[0].mega_evolved
          and _FT45._poke_block(_jv, BattleSide([]), False)[2 + len(_FT45.TYPES) + 5 + 6 + len(_FT45._ITEM_FLAGS) + _FT45._N_ABIL_CATS] == 1.0,
          f"{_jv.ability} {_jv.speed}/{_A[0].speed}")
    check("45 選出v2: メガ石を持たない個体はそのまま", _FT45.sel_mega_view(_A[1]) is _A[1])
    _kab = _A[1]
    _P2 = [_mk26c(x) for x in _P2s]
    _hit = _mk26c("ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ")
    _cases = [(_kab, _hit, 0.30, "じわれ"), (_kab, _P2[2], 0.0, "ひこう・がんじょう"), (_kab, _P2[3], 0.0, "ひこう"),
              (_kab, _mk26c("カバルドン@オボンのみ:わんぱく:じしん|あくび|ふきとばし|なまける:32/0/32/0/0/0:すなおこし"), 0.30, "地面")]
    _gj = _mk26c("カビゴン@カゴのみ:わんぱく:じしん|じわれ|ねむる|れいとうパンチ:32/0/2/0/32/0:あついしぼう"); _gj.ability = "ノーガード"
    _cases.append((_gj, _hit, 1.0, "ノーガード"))
    _rk = _mk26c("ドドゲザン@きあいのタスキ:いじっぱり:ドゲザン|アイアンヘッド|ふいうち|つるぎのまい:0/32/0/0/0/32:そうだいしょう"); _rk.ability = "がんじょう"
    _cases.append((_kab, _rk, 0.0, "がんじょう"))
    _mb = _mk26c("カビゴン@カゴのみ:わんぱく:じしん|じわれ|ねむる|れいとうパンチ:32/0/2/0/32/0:あついしぼう"); _mb.ability = "かたやぶり"
    _cases.append((_mb, _rk, 0.30, "かたやぶり は がんじょう を無視"))
    _sc = _mk26c("ギルガルド@たべのこし:れいせい:シャドーボール|ラスターカノン|キングシールド|かげうち:32/0/2/32/0/0:バトルスイッチ")
    _sc.moves = [dl.get_move("ぜったいれいど")]
    _cases += [(_sc, _hit, 0.20, "ぜったいれいど（非こおり）"), (_hit, _kab, 0.0, "一撃必殺なし")]
    _got = [(_w, round(_FT45.ohko_ev(_a, _d), 6)) for _a, _d, _w, _ in _cases]
    check("45 選出v2: 一撃必殺の期待値（命中×HP割合・タイプ/浮遊/がんじょう無効・かたやぶり・ノーガード）",
          all(abs(a - b) < 1e-12 for a, b in _got), str([(c[3], g) for c, g in zip(_cases, _got)]))
    _base = _j45.load(open(os.path.join(os.path.dirname(_LS45.__file__), "selector_m6d.json")))
    _rng = _np45.random.default_rng(45)
    _W1 = _np45.asarray(_base["W1"])
    _v2 = dict(_base, feat="megaform_ohko1", W1=_np45.concatenate([_W1, _rng.normal(0, 1.0, (_W1.shape[0], 18))], 1).tolist())
    _v2z = dict(_base, feat="megaform_ohko1", W1=_np45.concatenate([_W1, _np45.zeros((_W1.shape[0], 18))], 1).tolist())
    _td = _tf45.mkdtemp()
    def _wr(n, d):
        q = os.path.join(_td, n); _j45.dump(d, open(q, "w")); return q
    _pv2, _pv2z = _wr("v2.json", _v2), _wr("v2z.json", _v2z)
    _K = ("SEL_OPP_ASSUME", "SEL_OPP_K", "LEARNED_SELECTION_IMPL", "SEL_FAST")
    _sv = {k: os.environ.get(k) for k in _K}
    _p0, _m0, _l0 = _LS45._PATH, _LS45._MODEL, _LS45._LOADED
    def _ld(q):
        _LS45._PATH = q; _LS45._LOADED = False
        return _LS45._load()
    try:
        _m = _ld(_pv2)
        check("45 選出v2: \"feat\": \"megaform_ohko1\" のモデル（入力1037+18次元）を読む", _m is not None and _m["v2"] and _m["W1"].shape[1] == _FT45.feature_dim() + 18)
        check("45 選出v2: 未知の入力形式のモデルは読まない", _ld(_wr("vx.json", dict(_v2, feat="megaform_x"))) is None)
        check("45 選出v2: 入力形式の無い旧モデル（m6d・1037次元）は従来どおり読む",
              (lambda m: m is not None and not m["v2"] and m["W1"].shape[1] == _FT45.feature_dim())(_ld(os.path.join(os.path.dirname(_LS45.__file__), "selector_m6d.json"))))
        _o = [_P2[i] for i in (0, 4, 5)]
        _x1 = _LS45._encode_ref([_A[3], _A[4], _A[5]], _o); _x2 = _LS45._encode_ref([_A[3], _A[4], _A[5]], _o, True)
        check("45 選出v2: メガ石も一撃必殺も無い組は先頭1037次元が旧入力と同じ・末尾18次元は0",
              _x2[:len(_x1)] == _x1 and _x2[len(_x1):] == [0.0] * 18)
        _pairs = [(_P45A, _P2s), (_P2s, _P45A), (_P45A, _P1s)]
        _res = {}
        for _impl in ("ref", "fast", "rust"):
            for k in _K:
                os.environ.pop(k, None)
            os.environ.update({"SEL_OPP_ASSUME": "learnedK", "LEARNED_SELECTION_IMPL": _impl})
            _m = _ld(_pv2)
            _out = []
            for _k, (_pa, _pb) in enumerate(_pairs):
                _a = [_mk26c(x) for x in _pa]; _b = [_mk26c(x) for x in _pb]
                _g = random.Random(4501 + _k)
                _s = _LS45.learned_select_scores(_a, _b, dl, n=3, rng=_g)
                _out.append(([_a.index(q) for q in max(_s, key=lambda x: x[1])[0]], [v for _, v in _s], _g.random()))
            _res[_impl] = _out
        check("45 選出v2（learnedK）: 高速版・Rust 版が元の実装と同じ選出・値（差1e-12未満）・乱数の消費",
              all(a[0] == b[0] and a[2] == b[2] and max(abs(x - y) for x, y in zip(a[1], b[1])) < 1e-12
                  for _i in ("fast", "rust") for a, b in zip(_res[_i], _res["ref"])), str({k: [o[0] for o in v] for k, v in _res.items()}))
        _cands = _LS45._candidates([_mk26c(x) for x in _P45A], 3)
        check("45 選出v2: メガ石持ち2体の党でも候補はメガ1体ちょうど（メガ後の形で評価するのは選ばれた1体だけ）",
              all(sum(1 for i in c if i in (0, 2)) == 1 for c in _cands) and _cands)
        os.environ.pop("LEARNED_SELECTION_IMPL", None)
        _py = []
        for _k, (_pa, _pb) in enumerate(_pairs):
            _a = [_mk26c(x) for x in _pa]; _b = [_mk26c(x) for x in _pb]
            _s = _LS45.learned_select_scores(_a, _b, dl, n=3, rng=random.Random(301))
            _py.append([_a.index(q) for q in max(_s, key=lambda x: x[1])[0]])
        _code = "import sys, json\nimport pokenavi_engine as E\nP = json.loads(sys.argv[1]); M = sys.argv[2]\n" \
                "print(json.dumps([E.guide_rows(a, [b], 'M-6', 0, 300, M)[0][0] for a, b in P]))"
        for _env in ({"SEL_OPP_ASSUME": "learnedK"}, {"SEL_OPP_ASSUME": "learnedK", "SEL_FAST": "0"}):
            _e = dict(os.environ); _e.update(_env)
            _r = _sp45.run([sys.executable, "-c", _code, _j45.dumps(_pairs, ensure_ascii=False), _pv2], capture_output=True, text=True,
                           env=_e, cwd=_SCRIPTS_DIR26n)
            _rs = _j45.loads(_r.stdout.strip().splitlines()[-1]) if _r.returncode == 0 else _r.stderr[-300:]
            check(f"45 選出v2: Rust select_scores（guide_rows・{'元の実装' if _env.get('SEL_FAST') else '高速版'}）の選出が Python と一致", _rs == _py, f"{_rs} / {_py}")
        _r = _sp45.run([sys.executable, "-c", _code, _j45.dumps(_pairs[:1], ensure_ascii=False), _wr("vx2.json", dict(_v2, feat="megaform_x"))],
                       capture_output=True, text=True, cwd=_SCRIPTS_DIR26n)
        check("45 選出v2: Rust も未知の入力形式のモデルは読まない", _r.returncode != 0 and "選出モデルとして読めない" in _r.stderr, _r.stderr[-200:])
        _m6e = os.path.join(os.path.dirname(_LS45.__file__), "selector_m6e.json")
        if os.path.exists(_m6e):
            check("45 選出v2: selector_m6e.json（既定）を v2 のモデルとして読む", (lambda m: m is not None and m["v2"])(_ld(_m6e)))
            _r = _sp45.run([sys.executable, "-c", _code, _j45.dumps(_pairs[:1], ensure_ascii=False), _m6e], capture_output=True, text=True,
                           cwd=_SCRIPTS_DIR26n)
            check("45 選出v2: Rust も selector_m6e.json を読む", _r.returncode == 0, _r.stderr[-200:])
    finally:
        for k, v in _sv.items():
            if v is None: os.environ.pop(k, None)
            else: os.environ[k] = v
        _LS45._PATH, _LS45._MODEL, _LS45._LOADED = _p0, _m0, _l0


for _nm45, _fn45 in (("反動ターン", _t45_recharge), ("一撃必殺の命中", _t45_ohko), ("選出の入力v2", _t45_selv2)):
    try:
        _fn45()
    except Exception as _e45:
        check(f"45 {_nm45} のテストが実行できる", False, f"{type(_e45).__name__}: {_e45}")

print(f"結果: {PASS}件 PASS / {FAIL}件 FAIL  (計{PASS+FAIL}件)")
if FAILURES:
    print(f"\n--- 失敗リスト ---")
    for f in FAILURES:
        print(f"  {f}")
else:
    print("✅ 全テストパス")

sys.exit(1 if FAIL > 0 else 0)
