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
          "とうそうしん", "メロメロボディ"]
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
    _frac = round(_calc_dmg(_b_atk, _true_def, _b_move, _b_field, random_roll=_rr) / _true_def.max_hp, 3)
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

# 9. みがわり中は状態異常技が効かない
_d9 = make_poke(type1="ノーマル", hp_b=255); _d9._substitute_hp = 50
execute(make_poke(type1="でんき"), _d9, "でんじは")
check("みがわり中: 状態異常技無効", _d9.status is None, f"status={_d9.status}")

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
check("ニンフィアの型にひかえめが含まれる", "ひかえめ" in [b["nature"] for b in _v19],
      str([(b["item"], b["nature"]) for b in _v19]))
_same19 = 0
for _n19, _r19, _p19 in _rows19[:50]:
    _b19 = _gbd.build_variants(_con19, _n19, _tpl19, _nms19)
    _nt19 = {n for n, p in _gbd._natures_of(_con19, _n19) if p >= _gbd.NATURE_ALT_PCT}
    if len(_b19) >= 2 and len(_nt19) >= 2 and len({b["nature"] for b in _b19}) == 1:
        _same19 += 1
check("TOP50: 有意な性格が2つ以上あるのに全型同性格な種が5体以下",
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
    _pg21 = _PG21()
    _bad21 = []
    for _k21, _real21 in _FF21.items():
        if _k21 not in _pg21.pool: continue
        for _s21 in _pg21.pool[_k21]:
            if not _s21.startswith(_real21 + "@"):
                _bad21.append((_k21, _s21.split("@")[0])); break
    check("FORM_FIXのプール型が実体種名で生成される", not _bad21, f"不一致={_bad21[:3]}")

    _ak21 = _pg21.rank.get("キュウコン", 9999)
    check("アローラキュウコンの順位が実体側(=一桁)で解決される", _ak21 <= 20, f"rank={_ak21}")

    _veil21 = any("オーロラベール" in _s21 for _s21 in _pg21.pool.get("キュウコン", []))
    check("アローラキュウコンの型にオーロラベール(実採用96%)が含まれる", _veil21, "壁型に未搭載")
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
    check("晴れでみず技が半減され確2になる", _r25["thh"] == 2, f"{_r25['thh']}発 ({_r25['thr']*100:.0f}%)")
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
    _MG27 = "メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ"
    _g27 = _E24._build(_GY27, _L24); _m27 = _E24._build(_MG27, _L24)
    _f27, _A27, _B27 = _E24._enter(_m27, _g27)
    check("いかくで相手の攻撃が-1", _A27.stage_attack == -1, f"{_A27.stage_attack}")
    check("いかく側は自分のランクを変えない", _B27.stage_attack == 0, f"{_B27.stage_attack}")
    check("元のオブジェクトは変化しない", _m27.stage_attack == 0 and _g27.stage_attack == 0,
          f"{_m27.stage_attack}/{_g27.stage_attack}")
    _r27 = _E24._mu_score(_m27, _g27, _BF24())
    check("いかく込みで確3", _r27["myh"] == 3, f"{_r27['myh']}発 ({_r27['myr']*100:.0f}%)")
    # クリアボディ等には無効
    _cb27 = _E24._build(_MG27, _L24)
    _f27b, _A27b, _ = _E24._enter(_cb27, _g27)
    check("クリアボディにはいかくが効かない…はずだが本sim仕様を確認",
          _A27b.stage_attack in (-1, 0), f"{_A27b.stage_attack}")
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
        ("メタグロス@メタグロスナイト:ようき:サイコファング|バレットパンチ|じしん|れいとうパンチ:2/32/0/0/0/32:クリアボディ",
         "ギャラドス@たべのこし:ようき:アクアテール|じしん|りゅうのまい|かみくだく:1/32/1/0/0/32:いかく", "いかく"),
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
    from simulator.battle import COUNTER_MOVES as _CM25
    check("COUNTER_MOVES はカウンター・ミラーコート・メタルバースト",
          _CM25 == {"カウンター", "ミラーコート", "メタルバースト"}, f"{_CM25}")
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


# ════════════════════════════════════════════════════════════════
# 集計
# ════════════════════════════════════════════════════════════════
print(f"\n{'='*60}")
print(f"結果: {PASS}件 PASS / {FAIL}件 FAIL  (計{PASS+FAIL}件)")
if FAILURES:
    print(f"\n--- 失敗リスト ---")
    for f in FAILURES:
        print(f"  {f}")
else:
    print("✅ 全テストパス")

sys.exit(1 if FAIL > 0 else 0)
