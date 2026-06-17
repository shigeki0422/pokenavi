#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全技仕様テスト（generate_move_tests.pyで自動生成）"""
import sys, random
sys.path.insert(0, 'scripts')

from simulator.data import DataLoader
from simulator.battle import BattleSide, Action, BattleField, _execute_move, Battle, _priority
from simulator.pokemon import BattlePokemon, calc_hp, calc_stat
from simulator.damage import calc_damage, _effective_power as _ep

dl = DataLoader('scripts/pokenavi.db')

PASS = 0; FAIL = 0; FAILURES = []

def check(label, cond, note=''):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        FAILURES.append(f'FAIL: {label}' + (f' → {note}' if note else ''))

def make_poke(type1='ノーマル', type2=None, hp_b=100, atk_b=100, def_b=100,
              spatk_b=100, spdef_b=100, spd_b=100, moves=None, item=None, ability=''):
    ms = [dl.get_move(m) for m in (moves or []) if dl.get_move(m)]
    p = BattlePokemon(
        name='test', dex=0, type1=type1, type2=type2,
        base_type1=type1, base_type2=type2,
        max_hp=calc_hp(hp_b,0), hp=calc_hp(hp_b,0),
        attack=calc_stat(atk_b,0,31,1.0), defense=calc_stat(def_b,0,31,1.0),
        sp_attack=calc_stat(spatk_b,0,31,1.0), sp_defense=calc_stat(spdef_b,0,31,1.0),
        speed=calc_stat(spd_b,0,31,1.0), moves=ms, pp=[20]*len(ms),
        item=item, ability=ability, nature='',
    )
    return p

def execute(atk, df, mv_name, field=None):
    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name
    s1 = BattleSide([atk]); s2 = BattleSide([df])
    return _execute_move(s1, s2, Action(type='move', move=mv), field or BattleField())

def execute_ctx(atk, df, mv_name, field=None):
    '''field/side状態を参照するため s1,s2,field を返す'''
    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name
    s1 = BattleSide([atk]); s2 = BattleSide([df]); f = field or BattleField()
    _execute_move(s1, s2, Action(type='move', move=mv), f)
    return s1, s2, f

def dmg(atk, df, mv_name):
    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name
    return calc_damage(atk, df, mv, BattleField(), random_roll=1.0)  # 比率比較を安定させる固定ロール

_SNAP_SKIP = {'moves','name','dex','max_hp','base_type1','base_type2','mega_data','evs',
    'opp_view','last_used_move','turns_out','protect_consecutive','_last_flung_item'}
def _snap_obj(o):
    d = {}
    for k, v in vars(o).items():
        if k in _SNAP_SKIP: continue
        if isinstance(v, list): v = tuple(v)
        if isinstance(v, dict): v = tuple(sorted(v.items())) if v else ()
        try: hash(v)
        except Exception: v = str(v)
        d[k] = v
    return d
def snap_poke(p): return _snap_obj(p)
def snap_field(f): return _snap_obj(f)
def snap_side(s): return _snap_obj(s)
def any_change(before, after):
    # 新規キー出現も変化とみなす（setattrで増えた状態フラグを検出）
    keys = set(before) | set(after)
    return any(before.get(k) != after.get(k) for k in keys)

# 1v1シミュで副作用が観測できない技（味方対象・位置入替・ダブル専用ガード）
DOUBLE_ONLY_SMOKE = {
    'アロマミスト','コーチング','てだすけ','サイドチェンジ','ファストガード',
    'ワイドガード','このゆびとまれ','じばそうさ','いやしのねがい','いのちのしずく',
    'いやしのすず','フェアリーロック','りんしょう','さきおくり','おさきにどうぞ',
    'いかりのこな','いやしのはどう','おちゃかい','ふしょくガス','フラフラダンス',
}

def side_effect_check(label, mv_name, atk_type, accuracy_known, smoke=False):
    '''status技を実行し、何らかの観測可能変化が起きるか（命中までリトライ）。
       smoke=Trueなら例外を投げず実行できればOK。'''
    import random as _r
    _r.seed(0)
    mv = dl.get_move(mv_name)
    if mv is None:
        check(label, False, 'move not found'); return
    for _ in range(40):
        # 攻撃側と防御側を非対称に（入替/コピー技が観測できるよう型/特性/速度/値を変える）
        atk = make_poke(type1=atk_type, hp_b=200, spd_b=50, ability='ちからもち')
        df = make_poke(type1='ドラゴン', hp_b=200, spd_b=150, ability='ふゆう')
        atk.hp = 150  # 回復技用に余地
        # 前提条件依存技のための汎用セットアップ（道具・ランク・前技・状態・たくわえ）
        atk.item = 'オボンのみ'; df.item = 'たべのこし'
        atk._last_consumed_item = 'オボンのみ'
        atk.stockpile_count = 2
        df.stage_attack = 2; df.stage_defense = 2; df.stage_sp_attack = 2
        atk.stage_attack = 1
        df.last_used_move = 'たいあたり'; atk.last_used_move = 'たいあたり'
        df.moves = [dl.get_move('たいあたり')]; df.pp = [10]
        s1 = BattleSide([atk, make_poke()]); s2 = BattleSide([df, make_poke()]); f = BattleField()
        b_a, b_d = snap_poke(atk), snap_poke(df)
        b_f, b_s1, b_s2 = snap_field(f), snap_side(s1), snap_side(s2)
        try:
            _execute_move(s1, s2, Action(type='move', move=mv), f)
        except Exception as e:
            check(label, False, f'例外: {e}'); return
        changed = (any_change(b_a, snap_poke(atk)) or any_change(b_d, snap_poke(df))
                   or any_change(b_f, snap_field(f)) or any_change(b_s1, snap_side(s1))
                   or any_change(b_s2, snap_side(s2)))
        if changed:
            check(label, True); return
    if smoke:
        check(label, True)  # 例外なく実行完了（観測困難技）
    else:
        check(label, False, '副作用が観測されない（未実装の疑い）')


# ── ほのおのパンチ ──
check("DB: ほのおのパンチ 取得可能", dl.get_move("ほのおのパンチ") is not None)
_mv_ほのおのパンチ = dl.get_move("ほのおのパンチ")
if _mv_ほのおのパンチ:
    _pa_ほのおのパンチ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ほのおのパンチ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ほのおのパンチ = dmg(_pa_ほのおのパンチ, _pd_ほのおのパンチ, "ほのおのパンチ")
    check("ダメージ計算: ほのおのパンチ", _d_ほのおのパンチ > 0, f"dmg={_d_ほのおのパンチ}")
# ほのおのパンチ: やけど10%
_mv_s_ほのおのパンチ = dl.get_move("ほのおのパンチ")
if _mv_s_ほのおのパンチ:
    random.seed(0); _hit_ほのおのパンチ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ほのおのパンチ")
        _hit_ほのおのパンチ += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): ほのおのパンチ", 9 <= _hit_ほのおのパンチ <= 66, f"count={_hit_ほのおのパンチ}/300")
    random.seed(1); _immok_ほのおのパンチ = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ほのおのパンチ")
        if _pdi.status == "burn": _immok_ほのおのパンチ = False; break
    check("やけど免疫(ほのお型には無効): ほのおのパンチ", _immok_ほのおのパンチ, "免疫タイプに状態異常が付与されないこと")

# ── かみなりパンチ ──
check("DB: かみなりパンチ 取得可能", dl.get_move("かみなりパンチ") is not None)
_mv_かみなりパンチ = dl.get_move("かみなりパンチ")
if _mv_かみなりパンチ:
    _pa_かみなりパンチ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_かみなりパンチ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_かみなりパンチ = dmg(_pa_かみなりパンチ, _pd_かみなりパンチ, "かみなりパンチ")
    check("ダメージ計算: かみなりパンチ", _d_かみなりパンチ > 0, f"dmg={_d_かみなりパンチ}")
# かみなりパンチ: まひ10%
_mv_s_かみなりパンチ = dl.get_move("かみなりパンチ")
if _mv_s_かみなりパンチ:
    random.seed(0); _hit_かみなりパンチ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "かみなりパンチ")
        _hit_かみなりパンチ += int((_pd2.status == "paralysis"))
    check("追加効果(まひ10%): かみなりパンチ", 9 <= _hit_かみなりパンチ <= 66, f"count={_hit_かみなりパンチ}/300")
    random.seed(1); _immok_かみなりパンチ = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "かみなりパンチ")
        if _pdi.status == "paralysis": _immok_かみなりパンチ = False; break
    check("まひ免疫(でんき型には無効): かみなりパンチ", _immok_かみなりパンチ, "免疫タイプに状態異常が付与されないこと")

# ── れいとうパンチ ──
check("DB: れいとうパンチ 取得可能", dl.get_move("れいとうパンチ") is not None)
_mv_れいとうパンチ = dl.get_move("れいとうパンチ")
if _mv_れいとうパンチ:
    _pa_れいとうパンチ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_れいとうパンチ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_れいとうパンチ = dmg(_pa_れいとうパンチ, _pd_れいとうパンチ, "れいとうパンチ")
    check("ダメージ計算: れいとうパンチ", _d_れいとうパンチ > 0, f"dmg={_d_れいとうパンチ}")
# れいとうパンチ: こおり10%
_mv_s_れいとうパンチ = dl.get_move("れいとうパンチ")
if _mv_s_れいとうパンチ:
    random.seed(0); _hit_れいとうパンチ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "れいとうパンチ")
        _hit_れいとうパンチ += int((_pd2.status == "freeze"))
    check("追加効果(こおり10%): れいとうパンチ", 9 <= _hit_れいとうパンチ <= 66, f"count={_hit_れいとうパンチ}/300")
    random.seed(1); _immok_れいとうパンチ = True
    for _ in range(60):
        _pai = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pdi = make_poke(type1="こおり", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "れいとうパンチ")
        if _pdi.status == "freeze": _immok_れいとうパンチ = False; break
    check("こおり免疫(こおり型には無効): れいとうパンチ", _immok_れいとうパンチ, "免疫タイプに状態異常が付与されないこと")

# ── ハサミギロチン ──
check("DB: ハサミギロチン 取得可能", dl.get_move("ハサミギロチン") is not None)
# ハサミギロチン: 一撃必殺
_mv_oh_ハサミギロチン = dl.get_move("ハサミギロチン")
if _mv_oh_ハサミギロチン:
    random.seed(0); _ko_ハサミギロチン = False
    for _ in range(60):
        _pa_oh = make_poke(type1="ノーマル"); _pd_oh = make_poke(type1="ノーマル", hp_b=200)
        execute(_pa_oh, _pd_oh, "ハサミギロチン")
        if not _pd_oh.is_alive: _ko_ハサミギロチン = True; break
    check("一撃必殺: ハサミギロチン", _ko_ハサミギロチン)
# ハサミギロチン: 命中時に相手を必ずひんし（HP量に依存しない）
random.seed(0); _ohko_ok = False
for _ in range(60):
    _pa_oh = make_poke(type1="ノーマル"); _pd_oh = make_poke(type1="ノーマル", hp_b=255)
    execute(_pa_oh, _pd_oh, "ハサミギロチン")
    if not _pd_oh.is_alive: _ohko_ok = True; break
check("一撃必殺(フルHP): ハサミギロチン", _ohko_ok, "60試行内に一撃必殺が発生すること")
# 命中率30%統計（200試行で40〜100回ヒット）
random.seed(1); _ohko_count = 0
for _ in range(200):
    _pa_s = make_poke(type1="ノーマル"); _pd_s = make_poke(type1="ノーマル", hp_b=255)
    execute(_pa_s, _pd_s, "ハサミギロチン"); _ohko_count += (0 if _pd_s.is_alive else 1)
check("命中率約30%: ハサミギロチン", 20 <= _ohko_count <= 100, f"hits={_ohko_count}/200")

# ── つるぎのまい ──
check("DB: つるぎのまい 取得可能", dl.get_move("つるぎのまい") is not None)
# つるぎのまい: 自分攻撃+2
_mv_sb_つるぎのまい_attack = dl.get_move("つるぎのまい")
if _mv_sb_つるぎのまい_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "つるぎのまい")
    check("自分攻撃+2: つるぎのまい", _pa_sb.stage_attack == 2, f"1回適用={_pa_sb.stage_attack} 期待=+2")
# つるぎのまい: 自分攻撃+2
_mvss_つるぎのまい_attack = dl.get_move("つるぎのまい")
if _mvss_つるぎのまい_attack:
    random.seed(0); _got_つるぎのまい_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="ノーマル", atk_b=60, spatk_b=60); _pds = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "つるぎのまい")
        if _pas.stage_attack != 0: _got_つるぎのまい_attack = _pas.stage_attack; break
    check("自分攻撃+2: つるぎのまい", _got_つるぎのまい_attack == 2, f"1回適用={_got_つるぎのまい_attack} 期待=2")

# ── ふきとばし ──
check("DB: ふきとばし 取得可能", dl.get_move("ふきとばし") is not None)
# ふきとばし: 優先度-6
_mv_pr_ふきとばし = dl.get_move("ふきとばし")
if _mv_pr_ふきとばし and _mv_pr_ふきとばし.priority == -6:
    check("優先度-6: ふきとばし", _mv_pr_ふきとばし.priority == -6)
elif _mv_pr_ふきとばし:
    check("優先度-6: ふきとばし", _mv_pr_ふきとばし.priority == -6, f"DB優先度={_mv_pr_ふきとばし.priority} 仕様=-6")
# ふきとばし: 控えがいれば相手をランダム交代させる／控えがいなければ交代しない
from simulator.battle import Battle as _Bfsw
import simulator.battle as _SBfsw; _mx_fsw = _SBfsw.MAX_TURNS; _SBfsw.MAX_TURNS = 1
import copy as _cpfs; _mvfs = _cpfs.copy(dl.get_move("ふきとばし")); _mvfs.accuracy = 100
_actfsw = lambda s,o,f: Action(type="move", move=_mvfs, move_idx=0)
_actwk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_pfsw = make_poke(type1="ノーマル", atk_b=120, spd_b=200, moves=["ふきとばし"])
_df0 = make_poke(type1="ノーマル", hp_b=255, def_b=200, spd_b=10, moves=["たいあたり"]); _df1 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])
_sdef = BattleSide([_df0, _df1])
_Bfsw(BattleSide([_pfsw]), _sdef).run(_actfsw, _actwk)
check("控え有りで強制交代: ふきとばし", _sdef.active is not _df0, f"active_idx={_sdef.active_idx}")
_pfsw2 = make_poke(type1="ノーマル", atk_b=120, spd_b=200, moves=["ふきとばし"])
_dsolo = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _ssolo = BattleSide([_dsolo])
_Bfsw(BattleSide([_pfsw2]), _ssolo).run(_actfsw, _actwk)
check("控えなしでは交代しない: ふきとばし", _ssolo.active is _dsolo, "1体なら強制交代は発生しない")
_SBfsw.MAX_TURNS = _mx_fsw

# ── メガトンキック ──
check("DB: メガトンキック 取得可能", dl.get_move("メガトンキック") is not None)
_mv_メガトンキック = dl.get_move("メガトンキック")
if _mv_メガトンキック:
    _pa_メガトンキック = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_メガトンキック = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_メガトンキック = dmg(_pa_メガトンキック, _pd_メガトンキック, "メガトンキック")
    check("ダメージ計算: メガトンキック", _d_メガトンキック > 0, f"dmg={_d_メガトンキック}")

# ── つのドリル ──
check("DB: つのドリル 取得可能", dl.get_move("つのドリル") is not None)
# つのドリル: 一撃必殺
_mv_oh_つのドリル = dl.get_move("つのドリル")
if _mv_oh_つのドリル:
    random.seed(0); _ko_つのドリル = False
    for _ in range(60):
        _pa_oh = make_poke(type1="ノーマル"); _pd_oh = make_poke(type1="ノーマル", hp_b=200)
        execute(_pa_oh, _pd_oh, "つのドリル")
        if not _pd_oh.is_alive: _ko_つのドリル = True; break
    check("一撃必殺: つのドリル", _ko_つのドリル)

# ── のしかかり ──
check("DB: のしかかり 取得可能", dl.get_move("のしかかり") is not None)
_mv_のしかかり = dl.get_move("のしかかり")
if _mv_のしかかり:
    _pa_のしかかり = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_のしかかり = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_のしかかり = dmg(_pa_のしかかり, _pd_のしかかり, "のしかかり")
    check("ダメージ計算: のしかかり", _d_のしかかり > 0, f"dmg={_d_のしかかり}")
# のしかかり: まひ30%
_mv_s_のしかかり = dl.get_move("のしかかり")
if _mv_s_のしかかり:
    random.seed(0); _hit_のしかかり = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "のしかかり")
        _hit_のしかかり += int((_pd2.status == "paralysis"))
    check("追加効果(まひ30%): のしかかり", 27 <= _hit_のしかかり <= 168, f"count={_hit_のしかかり}/300")
    random.seed(1); _immok_のしかかり = True
    for _ in range(60):
        _pai = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "のしかかり")
        if _pdi.status == "paralysis": _immok_のしかかり = False; break
    check("まひ免疫(でんき型には無効): のしかかり", _immok_のしかかり, "免疫タイプに状態異常が付与されないこと")
# のしかかり: ちいさくなる状態の相手に威力2倍
_pm = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
_dm0 = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
_dm1 = make_poke(type1="ノーマル", def_b=100, spdef_b=100); _dm1.minimized = True
_pm_n = _ep(_pm, _dm0, dl.get_move("のしかかり"), BattleField())
_pm_m = _ep(_pm, _dm1, dl.get_move("のしかかり"), BattleField())
check("ちいさくなる2倍: のしかかり", _pm_m == _pm_n * 2, f"normal={_pm_n} mini={_pm_m}")

# ── まきつく ──
check("DB: まきつく 取得可能", dl.get_move("まきつく") is not None)
_mv_まきつく = dl.get_move("まきつく")
if _mv_まきつく:
    _pa_まきつく = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_まきつく = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_まきつく = dmg(_pa_まきつく, _pd_まきつく, "まきつく")
    check("ダメージ計算: まきつく", _d_まきつく > 0, f"dmg={_d_まきつく}")
# まきつく: バインド
_mv_bd_まきつく = dl.get_move("まきつく")
if _mv_bd_まきつく:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="ノーマル", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="ノーマル", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "まきつく")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: まきつく", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── あばれる ──
check("DB: あばれる 取得可能", dl.get_move("あばれる") is not None)
_mv_あばれる = dl.get_move("あばれる")
if _mv_あばれる:
    _pa_あばれる = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_あばれる = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_あばれる = dmg(_pa_あばれる, _pd_あばれる, "あばれる")
    check("ダメージ計算: あばれる", _d_あばれる > 0, f"dmg={_d_あばれる}")
# あばれる: あばれ状態
_mv_rg_あばれる = dl.get_move("あばれる")
if _mv_rg_あばれる:
    _pa_rg = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pd_rg = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
    execute(_pa_rg, _pd_rg, "あばれる")
    check("あばれ状態: あばれる", _pa_rg.locked_move == "あばれる")

# ── ミサイルばり ──
check("DB: ミサイルばり 取得可能", dl.get_move("ミサイルばり") is not None)
_mv_ミサイルばり = dl.get_move("ミサイルばり")
if _mv_ミサイルばり:
    _pa_ミサイルばり = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_ミサイルばり = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ミサイルばり = dmg(_pa_ミサイルばり, _pd_ミサイルばり, "ミサイルばり")
    check("ダメージ計算: ミサイルばり", _d_ミサイルばり > 0, f"dmg={_d_ミサイルばり}")
# ミサイルばり: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ミサイルばり = dl.get_move("ミサイルばり")
if _mvmh_ミサイルばり:
    _pam = make_poke(type1="むし", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ミサイルばり = calc_damage(_pam, make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200), _mvmh_ミサイルばり, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ミサイルばり = 0
    for _ in range(20):
        _pdm = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ミサイルばり"); _multi_ミサイルばり = _pdm.max_hp - _pdm.hp
        if _multi_ミサイルばり > _single_ミサイルばり: break
    check("多段ヒット発生(複数回): ミサイルばり", _multi_ミサイルばり > _single_ミサイルばり, f"single={_single_ミサイルばり} multi={_multi_ミサイルばり}")

# ── かみつく ──
check("DB: かみつく 取得可能", dl.get_move("かみつく") is not None)
_mv_かみつく = dl.get_move("かみつく")
if _mv_かみつく:
    _pa_かみつく = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_かみつく = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_かみつく = dmg(_pa_かみつく, _pd_かみつく, "かみつく")
    check("ダメージ計算: かみつく", _d_かみつく > 0, f"dmg={_d_かみつく}")
# かみつく: ひるみ30%
_mv_f_かみつく = dl.get_move("かみつく")
if _mv_f_かみつく:
    random.seed(1); _fh_かみつく = 0
    for _ in range(300):
        _pa3 = make_poke(type1="あく", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="エスパー", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "かみつく"); _fh_かみつく += int(_pd3.flinched)
    check("ひるみ(30%): かみつく", 27 <= _fh_かみつく <= 168, f"count={_fh_かみつく}/300")

# ── すてみタックル ──
check("DB: すてみタックル 取得可能", dl.get_move("すてみタックル") is not None)
_mv_すてみタックル = dl.get_move("すてみタックル")
if _mv_すてみタックル:
    _pa_すてみタックル = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_すてみタックル = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_すてみタックル = dmg(_pa_すてみタックル, _pd_すてみタックル, "すてみタックル")
    check("ダメージ計算: すてみタックル", _d_すてみタックル > 0, f"dmg={_d_すてみタックル}")
# すてみタックル: 反動（与ダメの1/3）
_mvrc_すてみタックル = dl.get_move("すてみタックル")
if _mvrc_すてみタックル:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="ノーマル", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "すてみタックル")
        _rc_dealt_すてみタックル = _hpdr - _pdr.hp; _rc_rcv_すてみタックル = _par.max_hp - _par.hp
        if _rc_dealt_すてみタックル > 0: break
    _rc_exp_すてみタックル = max(1, _rc_dealt_すてみタックル // 3)
    check("反動ダメージ(1/3): すてみタックル", abs(_rc_rcv_すてみタックル - _rc_exp_すてみタックル) <= 2, f"dealt={_rc_dealt_すてみタックル} recoil={_rc_rcv_すてみタックル} 期待={_rc_exp_すてみタックル}")

# ── ほえる ──
check("DB: ほえる 取得可能", dl.get_move("ほえる") is not None)
# ほえる: 優先度-6
_mv_pr_ほえる = dl.get_move("ほえる")
if _mv_pr_ほえる and _mv_pr_ほえる.priority == -6:
    check("優先度-6: ほえる", _mv_pr_ほえる.priority == -6)
elif _mv_pr_ほえる:
    check("優先度-6: ほえる", _mv_pr_ほえる.priority == -6, f"DB優先度={_mv_pr_ほえる.priority} 仕様=-6")
# ほえる: 控えがいれば相手をランダム交代させる／控えがいなければ交代しない
from simulator.battle import Battle as _Bfsw
import simulator.battle as _SBfsw; _mx_fsw = _SBfsw.MAX_TURNS; _SBfsw.MAX_TURNS = 1
import copy as _cpfs; _mvfs = _cpfs.copy(dl.get_move("ほえる")); _mvfs.accuracy = 100
_actfsw = lambda s,o,f: Action(type="move", move=_mvfs, move_idx=0)
_actwk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_pfsw = make_poke(type1="ノーマル", atk_b=120, spd_b=200, moves=["ほえる"])
_df0 = make_poke(type1="ノーマル", hp_b=255, def_b=200, spd_b=10, moves=["たいあたり"]); _df1 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])
_sdef = BattleSide([_df0, _df1])
_Bfsw(BattleSide([_pfsw]), _sdef).run(_actfsw, _actwk)
check("控え有りで強制交代: ほえる", _sdef.active is not _df0, f"active_idx={_sdef.active_idx}")
_pfsw2 = make_poke(type1="ノーマル", atk_b=120, spd_b=200, moves=["ほえる"])
_dsolo = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _ssolo = BattleSide([_dsolo])
_Bfsw(BattleSide([_pfsw2]), _ssolo).run(_actfsw, _actwk)
check("控えなしでは交代しない: ほえる", _ssolo.active is _dsolo, "1体なら強制交代は発生しない")
_SBfsw.MAX_TURNS = _mx_fsw

# ── かなしばり ──
check("DB: かなしばり 取得可能", dl.get_move("かなしばり") is not None)
# かなしばり: 相手の最後の技を封じる
_pkn = make_poke(); _dkn = make_poke(moves=["たいあたり"]); _dkn.last_used_move = "たいあたり"
execute(_pkn, _dkn, "かなしばり")
check("かなしばり わざ封じ: かなしばり", _dkn.disabled_move == "たいあたり")

# ── かえんほうしゃ ──
check("DB: かえんほうしゃ 取得可能", dl.get_move("かえんほうしゃ") is not None)
_mv_かえんほうしゃ = dl.get_move("かえんほうしゃ")
if _mv_かえんほうしゃ:
    _pa_かえんほうしゃ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_かえんほうしゃ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_かえんほうしゃ = dmg(_pa_かえんほうしゃ, _pd_かえんほうしゃ, "かえんほうしゃ")
    check("ダメージ計算: かえんほうしゃ", _d_かえんほうしゃ > 0, f"dmg={_d_かえんほうしゃ}")
# かえんほうしゃ: やけど10%
_mv_s_かえんほうしゃ = dl.get_move("かえんほうしゃ")
if _mv_s_かえんほうしゃ:
    random.seed(0); _hit_かえんほうしゃ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "かえんほうしゃ")
        _hit_かえんほうしゃ += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): かえんほうしゃ", 9 <= _hit_かえんほうしゃ <= 66, f"count={_hit_かえんほうしゃ}/300")
    random.seed(1); _immok_かえんほうしゃ = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "かえんほうしゃ")
        if _pdi.status == "burn": _immok_かえんほうしゃ = False; break
    check("やけど免疫(ほのお型には無効): かえんほうしゃ", _immok_かえんほうしゃ, "免疫タイプに状態異常が付与されないこと")

# ── ハイドロポンプ ──
check("DB: ハイドロポンプ 取得可能", dl.get_move("ハイドロポンプ") is not None)
_mv_ハイドロポンプ = dl.get_move("ハイドロポンプ")
if _mv_ハイドロポンプ:
    _pa_ハイドロポンプ = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ハイドロポンプ = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ハイドロポンプ = dmg(_pa_ハイドロポンプ, _pd_ハイドロポンプ, "ハイドロポンプ")
    check("ダメージ計算: ハイドロポンプ", _d_ハイドロポンプ > 0, f"dmg={_d_ハイドロポンプ}")

# ── ふぶき ──
check("DB: ふぶき 取得可能", dl.get_move("ふぶき") is not None)
_mv_ふぶき = dl.get_move("ふぶき")
if _mv_ふぶき:
    _pa_ふぶき = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_ふぶき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ふぶき = dmg(_pa_ふぶき, _pd_ふぶき, "ふぶき")
    check("ダメージ計算: ふぶき", _d_ふぶき > 0, f"dmg={_d_ふぶき}")
# ふぶき: こおり10%
_mv_s_ふぶき = dl.get_move("ふぶき")
if _mv_s_ふぶき:
    random.seed(0); _hit_ふぶき = 0
    for _ in range(300):
        _pa2 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ふぶき")
        _hit_ふぶき += int((_pd2.status == "freeze"))
    check("追加効果(こおり10%): ふぶき", 9 <= _hit_ふぶき <= 66, f"count={_hit_ふぶき}/300")
    random.seed(1); _immok_ふぶき = True
    for _ in range(60):
        _pai = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pdi = make_poke(type1="こおり", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ふぶき")
        if _pdi.status == "freeze": _immok_ふぶき = False; break
    check("こおり免疫(こおり型には無効): ふぶき", _immok_ふぶき, "免疫タイプに状態異常が付与されないこと")
# ふぶき: ゆき状態で必中
_mvwh_ふぶき = dl.get_move("ふぶき")
if _mvwh_ふぶき:
    random.seed(0); _wh_all_ふぶき = True
    for _ in range(30):
        _pawh = make_poke(type1="こおり", atk_b=100, spatk_b=100); _pdwh = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
        _fwh = BattleField(); _fwh.weather = "hail"
        _hpwh = _pdwh.hp
        _execute_move(BattleSide([_pawh]), BattleSide([_pdwh]), Action(type="move", move=_mvwh_ふぶき), _fwh)
        if _pdwh.hp == _hpwh: _wh_all_ふぶき = False; break
    check("ゆき状態で必中: ふぶき", _wh_all_ふぶき)

# ── れいとうビーム ──
check("DB: れいとうビーム 取得可能", dl.get_move("れいとうビーム") is not None)
_mv_れいとうビ_ム = dl.get_move("れいとうビーム")
if _mv_れいとうビ_ム:
    _pa_れいとうビ_ム = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_れいとうビ_ム = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_れいとうビ_ム = dmg(_pa_れいとうビ_ム, _pd_れいとうビ_ム, "れいとうビーム")
    check("ダメージ計算: れいとうビーム", _d_れいとうビ_ム > 0, f"dmg={_d_れいとうビ_ム}")
# れいとうビーム: こおり10%
_mv_s_れいとうビ_ム = dl.get_move("れいとうビーム")
if _mv_s_れいとうビ_ム:
    random.seed(0); _hit_れいとうビ_ム = 0
    for _ in range(300):
        _pa2 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "れいとうビーム")
        _hit_れいとうビ_ム += int((_pd2.status == "freeze"))
    check("追加効果(こおり10%): れいとうビーム", 9 <= _hit_れいとうビ_ム <= 66, f"count={_hit_れいとうビ_ム}/300")
    random.seed(1); _immok_れいとうビ_ム = True
    for _ in range(60):
        _pai = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pdi = make_poke(type1="こおり", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "れいとうビーム")
        if _pdi.status == "freeze": _immok_れいとうビ_ム = False; break
    check("こおり免疫(こおり型には無効): れいとうビーム", _immok_れいとうビ_ム, "免疫タイプに状態異常が付与されないこと")

# ── なみのり ──
check("DB: なみのり 取得可能", dl.get_move("なみのり") is not None)
_mv_なみのり = dl.get_move("なみのり")
if _mv_なみのり:
    _pa_なみのり = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_なみのり = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_なみのり = dmg(_pa_なみのり, _pd_なみのり, "なみのり")
    check("ダメージ計算: なみのり", _d_なみのり > 0, f"dmg={_d_なみのり}")
# なみのり: 水中(ダイビング溜め中)の相手に2倍
_pwv = make_poke(type1="みず", spatk_b=100, atk_b=100); _dwv = make_poke(type1="ノーマル", spdef_b=100, def_b=100)
_n0 = _ep(_pwv, _dwv, dl.get_move("なみのり"), BattleField())
_dwv.charging_move = "ダイビング"; _n1 = _ep(_pwv, _dwv, dl.get_move("なみのり"), BattleField())
check("なみのり 水中2倍: なみのり", _n1 == _n0 * 2, f"normal={_n0} dive={_n1}")

# ── はかいこうせん ──
check("DB: はかいこうせん 取得可能", dl.get_move("はかいこうせん") is not None)
_mv_はかいこうせん = dl.get_move("はかいこうせん")
if _mv_はかいこうせん:
    _pa_はかいこうせん = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_はかいこうせん = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_はかいこうせん = dmg(_pa_はかいこうせん, _pd_はかいこうせん, "はかいこうせん")
    check("ダメージ計算: はかいこうせん", _d_はかいこうせん > 0, f"dmg={_d_はかいこうせん}")
# はかいこうせん: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="ノーマル", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "はかいこうせん")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: はかいこうせん", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="ノーマル", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "はかいこうせん")
check("リチャージ中行動不能: はかいこうせん", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── カウンター ──
check("DB: カウンター 取得可能", dl.get_move("カウンター") is not None)
# カウンター: 優先度-5
_mv_pr_カウンタ_ = dl.get_move("カウンター")
if _mv_pr_カウンタ_ and _mv_pr_カウンタ_.priority == -5:
    check("優先度-5: カウンター", _mv_pr_カウンタ_.priority == -5)
elif _mv_pr_カウンタ_:
    check("優先度-5: カウンター", _mv_pr_カウンタ_.priority == -5, f"DB優先度={_mv_pr_カウンタ_.priority} 仕様=-5")
# カウンター: カウンター反射（物理技×2.0）
_mvcnt_カウンタ_ = dl.get_move("カウンター")
if _mvcnt_カウンタ_:
    _pac_cnt = make_poke(type1="かくとう", atk_b=100, spatk_b=100, hp_b=200)
    _pdc_cnt = make_poke(type1="ノーマル" if "かくとう"!="かくとう" else "エスパー", hp_b=255, def_b=100, spdef_b=100)
    _pac_cnt._last_physical_dmg_received = 100
    _exp_cnt = int(100 * 2.0)
    _hpc0 = _pdc_cnt.hp; execute(_pac_cnt, _pdc_cnt, "カウンター")
    check("カウンター反射: カウンター", _hpc0 - _pdc_cnt.hp == _exp_cnt, f"返し={_hpc0 - _pdc_cnt.hp} 期待={_exp_cnt}")
    _pac_cnt2 = make_poke(type1="かくとう", atk_b=100, spatk_b=100); _pdc_cnt2 = make_poke(type1="ノーマル", hp_b=255)
    _hpc20 = _pdc_cnt2.hp; execute(_pac_cnt2, _pdc_cnt2, "カウンター")
    check("カウンター被ダメ0で失敗: カウンター", _pdc_cnt2.hp == _hpc20)
# カウンター: 物理被ダメの2倍を返す。実際に物理技を受けてから使うintegrationも確認
_pac = make_poke(type1="かくとう", hp_b=255, def_b=60)
_attacker_phys = make_poke(type1="ノーマル", atk_b=100, hp_b=255)
_execute_move(BattleSide([_attacker_phys]), BattleSide([_pac]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())
_phys_received = _pac._last_physical_dmg_received
_pdc = make_poke(type1="ノーマル", hp_b=255, def_b=50); _hpc0 = _pdc.hp
execute(_pac, _pdc, "カウンター")
check("物理被ダメ×2返却: カウンター", _hpc0 - _pdc.hp == _phys_received * 2, f"received={_phys_received} returned={_hpc0 - _pdc.hp} expected={_phys_received * 2}")
# 被ダメなしは失敗
_pac2 = make_poke(type1="かくとう"); _pdc2 = make_poke(type1="ノーマル", hp_b=255); _hp2 = _pdc2.hp
execute(_pac2, _pdc2, "カウンター")
check("被ダメ0で失敗: カウンター", _pdc2.hp == _hp2)
# 特殊技を受けただけでは反射しない（物理のみ反応）
_pac3 = make_poke(type1="かくとう", hp_b=255); _pac3._last_special_dmg_received = 100; _pac3._last_physical_dmg_received = 0
_pdc3 = make_poke(type1="ノーマル", hp_b=255); _hp3 = _pdc3.hp
execute(_pac3, _pdc3, "カウンター")
check("特殊被弾では反射しない: カウンター", _pdc3.hp == _hp3, f"hp={_pdc3.hp}/{_hp3}")

# ── やどりぎのタネ ──
check("DB: やどりぎのタネ 取得可能", dl.get_move("やどりぎのタネ") is not None)
# やどりぎのタネ: 付与。くさタイプには無効
_pys = make_poke(type1="くさ"); _dys = make_poke(type1="ノーマル", hp_b=200); execute(_pys, _dys, "やどりぎのタネ")
check("やどりぎ付与: やどりぎのタネ", _dys.seeded, f"seeded={_dys.seeded}")
_dys2 = make_poke(type1="くさ", hp_b=200); execute(_pys, _dys2, "やどりぎのタネ")
check("くさ無効: やどりぎのタネ", not _dys2.seeded, f"seeded={_dys2.seeded}")

# ── けたぐり ──
check("DB: けたぐり 取得可能", dl.get_move("けたぐり") is not None)
# けたぐり: 相手の重さ別の威力テーブル（20/40/60/80/100/120）
_pw_l = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
_kg_ng = []
for _w, _exp in [(5,20),(15,40),(35,60),(75,80),(150,100),(300,120)]:
    _dkg = make_poke(type1="ノーマル"); _dkg.weight_kg = float(_w)
    _got = _ep(_pw_l, _dkg, dl.get_move("けたぐり"), BattleField())
    if _got != _exp: _kg_ng.append(f"{_w}kg:{_got}!={_exp}")
check("重さ別威力テーブル: けたぐり", not _kg_ng, f"NG={_kg_ng}")
# けたぐり: 重さによる威力テーブル（各境界を検証）
_pa_kg = make_poke(type1="かくとう", atk_b=100)
for _w, _exp in [(5,20),(15,40),(35,60),(75,80),(150,100),(300,120)]:
    _d_kg = make_poke(type1="ノーマル"); _d_kg.weight_kg = float(_w)
    _got_kg = _ep(_pa_kg, _d_kg, dl.get_move("けたぐり"), BattleField())
    check(f"重さ{_w}kg→威力{_exp}: けたぐり", _got_kg == _exp, f"w={_w}kg got={_got_kg} exp={_exp}")

# ── ソーラービーム ──
check("DB: ソーラービーム 取得可能", dl.get_move("ソーラービーム") is not None)
_mv_ソ_ラ_ビ_ム = dl.get_move("ソーラービーム")
if _mv_ソ_ラ_ビ_ム:
    _pa_ソ_ラ_ビ_ム = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ソ_ラ_ビ_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_ソ_ラ_ビ_ム = make_poke(type1="くさ", atk_b=100, spatk_b=100); _pd_ソ_ラ_ビ_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
        execute(_pa_ソ_ラ_ビ_ム, _pd_ソ_ラ_ビ_ム, "ソーラービーム"); execute(_pa_ソ_ラ_ビ_ム, _pd_ソ_ラ_ビ_ム, "ソーラービーム")
        if _pd_ソ_ラ_ビ_ム.hp < _pd_ソ_ラ_ビ_ム.max_hp: break
    check("ダメージ計算: ソーラービーム", _pd_ソ_ラ_ビ_ム.hp < _pd_ソ_ラ_ビ_ム.max_hp, f"hp={_pd_ソ_ラ_ビ_ム.hp}")
# ソーラービーム: 2ターン溜め
_mv_2t_ソ_ラ_ビ_ム = dl.get_move("ソーラービーム")
if _mv_2t_ソ_ラ_ビ_ム:
    _pa_2t = make_poke(type1="くさ", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="みず", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "ソーラービーム")
    check("2ターン溜め(1T)ダメなし: ソーラービーム", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: ソーラービーム", _pa_2t.charging_move == "ソーラービーム")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "ソーラービーム")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "ソーラービーム")
    check("2ターン溜め(2T)ダメあり: ソーラービーム", _pd_2t.hp < _hp_before_2t)
# ソーラービーム: にほんばれ状態では溜めず即攻撃（1ターン目でダメージ）
_fwi_ソ_ラ_ビ_ム = BattleField(); _fwi_ソ_ラ_ビ_ム.weather = "sunny"
_pwi_ソ_ラ_ビ_ム = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dwi_ソ_ラ_ビ_ム = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100); _hpwi_ソ_ラ_ビ_ム = _dwi_ソ_ラ_ビ_ム.hp
execute(_pwi_ソ_ラ_ビ_ム, _dwi_ソ_ラ_ビ_ム, "ソーラービーム", _fwi_ソ_ラ_ビ_ム)
check("にほんばれで即発動(1Tダメージ): ソーラービーム", _dwi_ソ_ラ_ビ_ム.hp < _hpwi_ソ_ラ_ビ_ム and _pwi_ソ_ラ_ビ_ム.charging_move is None, f"hp={_dwi_ソ_ラ_ビ_ム.hp}/{_hpwi_ソ_ラ_ビ_ム} charging={_pwi_ソ_ラ_ビ_ム.charging_move}")
# ソーラービーム: 晴れ以外の天候は威力1/2
_psb = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsb = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120)
_fsun = BattleField(); _fsun.weather = "sunny"; _frain = BattleField(); _frain.weather = "rain"
_sb_sun = calc_damage(_psb, _dsb, dl.get_move("ソーラービーム"), _fsun, random_roll=1.0); _sb_rain = calc_damage(_psb, _dsb, dl.get_move("ソーラービーム"), _frain, random_roll=1.0)
check("天候半減: ソーラービーム", _sb_rain < _sb_sun, f"sun={_sb_sun} rain={_sb_rain}")
# 無天候は溜めが必要（1ターン目ダメなし）
_pno = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dno = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpno = _dno.hp
execute(_pno, _dno, "ソーラービーム")
check("無天候は溜め(1Tダメなし): ソーラービーム", _dno.hp == _hpno and _pno.charging_move == "ソーラービーム", f"hp={_dno.hp}/{_hpno} charging={_pno.charging_move}")
# にほんばれ中は溜めず即攻撃（1ターン目でダメージ）
_psn = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsn = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpsn = _dsn.hp
_fsun2 = BattleField(); _fsun2.weather = "sunny"
execute(_psn, _dsn, "ソーラービーム", _fsun2)
check("晴れは即発動(1Tでダメージ): ソーラービーム", _dsn.hp < _hpsn and _psn.charging_move is None, f"hp={_dsn.hp}/{_hpsn} charging={_psn.charging_move}")
# 威力半減の具体値（120→60）
_psx = make_poke(type1="くさ", atk_b=100, spatk_b=100); _dsx = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
_pwr_norm = _ep(_psx, _dsx, dl.get_move("ソーラービーム"), BattleField())
_frx = BattleField(); _frx.weather = "rain"; _pwr_rain = _ep(_psx, _dsx, dl.get_move("ソーラービーム"), _frx)
check("通常威力120: ソーラービーム", _pwr_norm == 120, f"norm={_pwr_norm}")
check("天候半減(60): ソーラービーム", _pwr_rain == 60, f"rain={_pwr_rain}")

# ── ねむりごな ──
check("DB: ねむりごな 取得可能", dl.get_move("ねむりごな") is not None)
# ねむりごな: ねむり付与(変化技)
_mv_si_ねむりごな = dl.get_move("ねむりごな")
if _mv_si_ねむりごな:
    random.seed(0); _ok_ねむりごな = False
    for _ in range(30):
        _pa_si = make_poke(type1="くさ"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "ねむりごな")
        if _pd_si.status == "sleep": _ok_ねむりごな = True; break
    check("ねむり付与: ねむりごな", _ok_ねむりごな)
# ねむりごな: 粉技。くさタイプには無効
_ppw = make_poke(type1="くさ"); random.seed(0); _pw_ok = False
for _ in range(20):
    _dpw = make_poke(type1="ノーマル", hp_b=200); execute(_ppw, _dpw, "ねむりごな")
    if _dpw.status == "sleep": _pw_ok = True; break
check("粉付与: ねむりごな", _pw_ok)
_dpw2 = make_poke(type1="くさ", hp_b=200)
for _ in range(20): execute(_ppw, _dpw2, "ねむりごな")
check("くさ無効: ねむりごな", _dpw2.status is None, f"status={_dpw2.status}")

# ── ほのおのうず ──
check("DB: ほのおのうず 取得可能", dl.get_move("ほのおのうず") is not None)
_mv_ほのおのうず = dl.get_move("ほのおのうず")
if _mv_ほのおのうず:
    _pa_ほのおのうず = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ほのおのうず = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ほのおのうず = dmg(_pa_ほのおのうず, _pd_ほのおのうず, "ほのおのうず")
    check("ダメージ計算: ほのおのうず", _d_ほのおのうず > 0, f"dmg={_d_ほのおのうず}")
# ほのおのうず: バインド
_mv_bd_ほのおのうず = dl.get_move("ほのおのうず")
if _mv_bd_ほのおのうず:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="ほのお", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="くさ", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "ほのおのうず")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: ほのおのうず", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── じわれ ──
check("DB: じわれ 取得可能", dl.get_move("じわれ") is not None)
# じわれ: 一撃必殺
_mv_oh_じわれ = dl.get_move("じわれ")
if _mv_oh_じわれ:
    random.seed(0); _ko_じわれ = False
    for _ in range(60):
        _pa_oh = make_poke(type1="じめん"); _pd_oh = make_poke(type1="ノーマル", hp_b=200)
        execute(_pa_oh, _pd_oh, "じわれ")
        if not _pd_oh.is_alive: _ko_じわれ = True; break
    check("一撃必殺: じわれ", _ko_じわれ)

# ── 10まんボルト ──
check("DB: 10まんボルト 取得可能", dl.get_move("10まんボルト") is not None)
_mv_10まんボルト = dl.get_move("10まんボルト")
if _mv_10まんボルト:
    _pa_10まんボルト = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_10まんボルト = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_10まんボルト = dmg(_pa_10まんボルト, _pd_10まんボルト, "10まんボルト")
    check("ダメージ計算: 10まんボルト", _d_10まんボルト > 0, f"dmg={_d_10まんボルト}")
# 10まんボルト: まひ10%
_mv_s_10まんボルト = dl.get_move("10まんボルト")
if _mv_s_10まんボルト:
    random.seed(0); _hit_10まんボルト = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "10まんボルト")
        _hit_10まんボルト += int((_pd2.status == "paralysis"))
    check("追加効果(まひ10%): 10まんボルト", 9 <= _hit_10まんボルト <= 66, f"count={_hit_10まんボルト}/300")
    random.seed(1); _immok_10まんボルト = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "10まんボルト")
        if _pdi.status == "paralysis": _immok_10まんボルト = False; break
    check("まひ免疫(でんき型には無効): 10まんボルト", _immok_10まんボルト, "免疫タイプに状態異常が付与されないこと")

# ── じしん ──
check("DB: じしん 取得可能", dl.get_move("じしん") is not None)
_mv_じしん = dl.get_move("じしん")
if _mv_じしん:
    _pa_じしん = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_じしん = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_じしん = dmg(_pa_じしん, _pd_じしん, "じしん")
    check("ダメージ計算: じしん", _d_じしん > 0, f"dmg={_d_じしん}")
# じしん: 地中(あなをほる溜め中)の相手に2倍
_pug = make_poke(type1="じめん", atk_b=100); _dug = make_poke(type1="ノーマル", def_b=100)
_g0 = _ep(_pug, _dug, dl.get_move("じしん"), BattleField())
_dug.charging_move = "あなをほる"; _g1 = _ep(_pug, _dug, dl.get_move("じしん"), BattleField())
check("じしん 地中2倍: じしん", _g1 == _g0 * 2, f"normal={_g0} dig={_g1}")
# グラスフィールド状態では威力1/2
_pgf = make_poke(type1="じめん", atk_b=100); _dgf = make_poke(type1="どく", def_b=100)
_d_no = calc_damage(_pgf, _dgf, dl.get_move("じしん"), BattleField(), random_roll=1.0)
_fg1 = BattleField(); _fg1.grassy_terrain = True; _d_gf = calc_damage(_pgf, _dgf, dl.get_move("じしん"), _fg1, random_roll=1.0)
check("じしん グラスF半減: じしん", _d_gf < _d_no, f"no={_d_no} gf={_d_gf}")

# ── かみなり ──
check("DB: かみなり 取得可能", dl.get_move("かみなり") is not None)
_mv_かみなり = dl.get_move("かみなり")
if _mv_かみなり:
    _pa_かみなり = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_かみなり = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_かみなり = dmg(_pa_かみなり, _pd_かみなり, "かみなり")
    check("ダメージ計算: かみなり", _d_かみなり > 0, f"dmg={_d_かみなり}")
# かみなり: まひ30%
_mv_s_かみなり = dl.get_move("かみなり")
if _mv_s_かみなり:
    random.seed(0); _hit_かみなり = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "かみなり")
        _hit_かみなり += int((_pd2.status == "paralysis"))
    check("追加効果(まひ30%): かみなり", 27 <= _hit_かみなり <= 168, f"count={_hit_かみなり}/300")
    random.seed(1); _immok_かみなり = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "かみなり")
        if _pdi.status == "paralysis": _immok_かみなり = False; break
    check("まひ免疫(でんき型には無効): かみなり", _immok_かみなり, "免疫タイプに状態異常が付与されないこと")
# かみなり: あめ状態で必中
_mvwh_かみなり = dl.get_move("かみなり")
if _mvwh_かみなり:
    random.seed(0); _wh_all_かみなり = True
    for _ in range(30):
        _pawh = make_poke(type1="でんき", atk_b=100, spatk_b=100); _pdwh = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100)
        _fwh = BattleField(); _fwh.weather = "rain"
        _hpwh = _pdwh.hp
        _execute_move(BattleSide([_pawh]), BattleSide([_pdwh]), Action(type="move", move=_mvwh_かみなり), _fwh)
        if _pdwh.hp == _hpwh: _wh_all_かみなり = False; break
    check("あめ状態で必中: かみなり", _wh_all_かみなり)
# かみなり: あめ必中・にほんばれ命中低下
_pwa = make_poke(type1="でんき", spatk_b=100); _dwa = make_poke(type1="みず", spdef_b=100)
_fsun_w = BattleField(); _fsun_w.weather = "sunny"; _fnorm_w = BattleField()
from simulator.damage import check_hit as _ch
random.seed(0); _miss_sun = sum(0 if _ch(_pwa, _dwa, dl.get_move("かみなり"), _fsun_w) else 1 for _ in range(200))
random.seed(0); _miss_norm = sum(0 if _ch(_pwa, _dwa, dl.get_move("かみなり"), _fnorm_w) else 1 for _ in range(200))
check("晴れ命中低下: かみなり", _miss_sun > _miss_norm, f"sun_miss={_miss_sun} norm_miss={_miss_norm}")

# ── でんじは ──
check("DB: でんじは 取得可能", dl.get_move("でんじは") is not None)
# でんじは: まひ付与(変化技)
_mv_si_でんじは = dl.get_move("でんじは")
if _mv_si_でんじは:
    random.seed(0); _ok_でんじは = False
    for _ in range(30):
        _pa_si = make_poke(type1="でんき"); _pd_si = make_poke(type1="みず", hp_b=255)
        execute(_pa_si, _pd_si, "でんじは")
        if _pd_si.status == "paralysis": _ok_でんじは = True; break
    check("まひ付与: でんじは", _ok_でんじは)
    random.seed(2); _siimm_でんじは = True
    for _ in range(40):
        _pai2 = make_poke(type1="でんき"); _pdi2 = make_poke(type1="でんき", hp_b=255)
        execute(_pai2, _pdi2, "でんじは")
        if _pdi2.status == "paralysis": _siimm_でんじは = False; break
    check("まひ免疫(でんき型には無効): でんじは", _siimm_でんじは, "免疫タイプに付与されないこと")
# でんじは: まひ付与。じめんタイプには無効
_pdj = make_poke(type1="でんき"); _ddj = make_poke(type1="ノーマル", hp_b=200)
execute(_pdj, _ddj, "でんじは")
check("まひ付与: でんじは", _ddj.status == "paralysis", f"status={_ddj.status}")
_ddj2 = make_poke(type1="じめん", hp_b=200); execute(_pdj, _ddj2, "でんじは")
check("じめん無効: でんじは", _ddj2.status is None, f"status={_ddj2.status}")

# ── あなをほる ──
check("DB: あなをほる 取得可能", dl.get_move("あなをほる") is not None)
_mv_あなをほる = dl.get_move("あなをほる")
if _mv_あなをほる:
    _pa_あなをほる = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_あなをほる = make_poke(type1="でんき", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_あなをほる = make_poke(type1="じめん", atk_b=100, spatk_b=100); _pd_あなをほる = make_poke(type1="でんき", def_b=100, spdef_b=100)
        execute(_pa_あなをほる, _pd_あなをほる, "あなをほる"); execute(_pa_あなをほる, _pd_あなをほる, "あなをほる")
        if _pd_あなをほる.hp < _pd_あなをほる.max_hp: break
    check("ダメージ計算: あなをほる", _pd_あなをほる.hp < _pd_あなをほる.max_hp, f"hp={_pd_あなをほる.hp}")
# あなをほる: 2ターン溜め
_mv_2t_あなをほる = dl.get_move("あなをほる")
if _mv_2t_あなをほる:
    _pa_2t = make_poke(type1="じめん", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "あなをほる")
    check("2ターン溜め(1T)ダメなし: あなをほる", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: あなをほる", _pa_2t.charging_move == "あなをほる")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "あなをほる")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "あなをほる")
    check("2ターン溜め(2T)ダメあり: あなをほる", _pd_2t.hp < _hp_before_2t)

# ── どくどく ──
check("DB: どくどく 取得可能", dl.get_move("どくどく") is not None)
# どくどく: もうどく付与(変化技)
_mv_si_どくどく = dl.get_move("どくどく")
if _mv_si_どくどく:
    random.seed(0); _ok_どくどく = False
    for _ in range(30):
        _pa_si = make_poke(type1="どく"); _pd_si = make_poke(type1="くさ", hp_b=255)
        execute(_pa_si, _pd_si, "どくどく")
        if _pd_si.status == "badpoison": _ok_どくどく = True; break
    check("もうどく付与: どくどく", _ok_どくどく)
    random.seed(2); _siimm_どくどく = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="どく", hp_b=255)
        execute(_pai2, _pdi2, "どくどく")
        if _pdi2.status == "badpoison": _siimm_どくどく = False; break
    check("もうどく免疫(どく型には無効): どくどく", _siimm_どくどく, "免疫タイプに付与されないこと")
    random.seed(2); _siimm_どくどく = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="はがね", hp_b=255)
        execute(_pai2, _pdi2, "どくどく")
        if _pdi2.status == "badpoison": _siimm_どくどく = False; break
    check("もうどく免疫(はがね型には無効): どくどく", _siimm_どくどく, "免疫タイプに付与されないこと")

# ── サイコキネシス ──
check("DB: サイコキネシス 取得可能", dl.get_move("サイコキネシス") is not None)
_mv_サイコキネシス = dl.get_move("サイコキネシス")
if _mv_サイコキネシス:
    _pa_サイコキネシス = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_サイコキネシス = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_サイコキネシス = dmg(_pa_サイコキネシス, _pd_サイコキネシス, "サイコキネシス")
    check("ダメージ計算: サイコキネシス", _d_サイコキネシス > 0, f"dmg={_d_サイコキネシス}")
# サイコキネシス: 相手特防-1
_mv_dd_サイコキネシス = dl.get_move("サイコキネシス")
if _mv_dd_サイコキネシス:
    _pa_dd = make_poke(type1="エスパー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_サイコキネシス = 0; _dd_ok_サイコキネシス = False
    for _ in range(60):
        _pd_dd = make_poke(type1="かくとう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "サイコキネシス")
        if _pd_dd.stage_sp_defense != 0: _dd_val_サイコキネシス = _pd_dd.stage_sp_defense; _dd_ok_サイコキネシス = True; break
    check("相手特防-1: サイコキネシス", _dd_ok_サイコキネシス and _dd_val_サイコキネシス == -1, f"1回適用={_dd_val_サイコキネシス} 期待=-1")

# ── さいみんじゅつ ──
check("DB: さいみんじゅつ 取得可能", dl.get_move("さいみんじゅつ") is not None)
# さいみんじゅつ: ねむり付与(変化技)
_mv_si_さいみんじゅつ = dl.get_move("さいみんじゅつ")
if _mv_si_さいみんじゅつ:
    random.seed(0); _ok_さいみんじゅつ = False
    for _ in range(30):
        _pa_si = make_poke(type1="エスパー"); _pd_si = make_poke(type1="かくとう", hp_b=255)
        execute(_pa_si, _pd_si, "さいみんじゅつ")
        if _pd_si.status == "sleep": _ok_さいみんじゅつ = True; break
    check("ねむり付与: さいみんじゅつ", _ok_さいみんじゅつ)

# ── こうそくいどう ──
check("DB: こうそくいどう 取得可能", dl.get_move("こうそくいどう") is not None)
# こうそくいどう: 自分素早さ+2
_mv_sb_こうそくいどう_speed = dl.get_move("こうそくいどう")
if _mv_sb_こうそくいどう_speed:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "こうそくいどう")
    check("自分素早さ+2: こうそくいどう", _pa_sb.stage_speed == 2, f"1回適用={_pa_sb.stage_speed} 期待=+2")
# こうそくいどう: 自分素早さ+2
_mvss_こうそくいどう_speed = dl.get_move("こうそくいどう")
if _mvss_こうそくいどう_speed:
    random.seed(0); _got_こうそくいどう_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="エスパー", atk_b=60, spatk_b=60); _pds = make_poke(type1="かくとう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "こうそくいどう")
        if _pas.stage_speed != 0: _got_こうそくいどう_speed = _pas.stage_speed; break
    check("自分素早さ+2: こうそくいどう", _got_こうそくいどう_speed == 2, f"1回適用={_got_こうそくいどう_speed} 期待=2")

# ── でんこうせっか ──
check("DB: でんこうせっか 取得可能", dl.get_move("でんこうせっか") is not None)
_mv_でんこうせっか = dl.get_move("でんこうせっか")
if _mv_でんこうせっか:
    _pa_でんこうせっか = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_でんこうせっか = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_でんこうせっか = dmg(_pa_でんこうせっか, _pd_でんこうせっか, "でんこうせっか")
    check("ダメージ計算: でんこうせっか", _d_でんこうせっか > 0, f"dmg={_d_でんこうせっか}")
# でんこうせっか: 優先度1
_mv_pr_でんこうせっか = dl.get_move("でんこうせっか")
if _mv_pr_でんこうせっか and _mv_pr_でんこうせっか.priority == 1:
    check("優先度1: でんこうせっか", _mv_pr_でんこうせっか.priority == 1)
elif _mv_pr_でんこうせっか:
    check("優先度1: でんこうせっか", _mv_pr_でんこうせっか.priority == 1, f"DB優先度={_mv_pr_でんこうせっか.priority} 仕様=1")

# ── じこさいせい ──
check("DB: じこさいせい 取得可能", dl.get_move("じこさいせい") is not None)
# じこさいせい: HP回復（最大HPの約1/2・無天候）
_mv_hp_じこさいせい = dl.get_move("じこさいせい")
if _mv_hp_じこさいせい:
    _pa_hp = make_poke(type1="ノーマル", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "じこさいせい")
    _exp_hp_じこさいせい = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): じこさいせい", abs(_pa_hp.hp - (1 + _exp_hp_じこさいせい)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_じこさいせい}")

# ── ちいさくなる ──
check("DB: ちいさくなる 取得可能", dl.get_move("ちいさくなる") is not None)
# ちいさくなる: 自分回避率+2
_mv_sb_ちいさくなる_evasion = dl.get_move("ちいさくなる")
if _mv_sb_ちいさくなる_evasion:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ちいさくなる")
    check("自分回避率+2: ちいさくなる", _pa_sb.stage_evasion == 2, f"1回適用={_pa_sb.stage_evasion} 期待=+2")
# ちいさくなる: 自分回避率+2
_mvss_ちいさくなる_evasion = dl.get_move("ちいさくなる")
if _mvss_ちいさくなる_evasion:
    random.seed(0); _got_ちいさくなる_evasion = 0
    for _ in range(60):
        _pas = make_poke(type1="ノーマル", atk_b=60, spatk_b=60); _pds = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "ちいさくなる")
        if _pas.stage_evasion != 0: _got_ちいさくなる_evasion = _pas.stage_evasion; break
    check("自分回避率+2: ちいさくなる", _got_ちいさくなる_evasion == 2, f"1回適用={_got_ちいさくなる_evasion} 期待=2")
# ちいさくなる: 回避+2 かつ minimized状態になる（のしかかり等2倍の条件成立）
_pmin = make_poke(type1="ノーマル"); execute(_pmin, make_poke(), "ちいさくなる")
check("回避率+2: ちいさくなる", _pmin.stage_evasion == 2, f"eva={_pmin.stage_evasion}")
check("minimized成立: ちいさくなる", _pmin.minimized, f"minimized={_pmin.minimized}")

# ── かげぶんしん ──
check("DB: かげぶんしん 取得可能", dl.get_move("かげぶんしん") is not None)
# かげぶんしん: 自分回避率+1
_mv_sb_かげぶんしん_evasion = dl.get_move("かげぶんしん")
if _mv_sb_かげぶんしん_evasion:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "かげぶんしん")
    check("自分回避率+1: かげぶんしん", _pa_sb.stage_evasion == 1, f"1回適用={_pa_sb.stage_evasion} 期待=+1")
# かげぶんしん: 自分回避率+1
_mvss_かげぶんしん_evasion = dl.get_move("かげぶんしん")
if _mvss_かげぶんしん_evasion:
    random.seed(0); _got_かげぶんしん_evasion = 0
    for _ in range(60):
        _pas = make_poke(type1="ノーマル", atk_b=60, spatk_b=60); _pds = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "かげぶんしん")
        if _pas.stage_evasion != 0: _got_かげぶんしん_evasion = _pas.stage_evasion; break
    check("自分回避率+1: かげぶんしん", _got_かげぶんしん_evasion == 1, f"1回適用={_got_かげぶんしん_evasion} 期待=1")

# ── ひかりのかべ ──
check("DB: ひかりのかべ 取得可能", dl.get_move("ひかりのかべ") is not None)
# ひかりのかべ: スクリーンlight_screen
_mv_sc_ひかりのかべ = dl.get_move("ひかりのかべ")
if _mv_sc_ひかりのかべ:
    _fsc = BattleField()
    _s1sc, _s2sc, _fsc = execute_ctx(make_poke(type1="エスパー"), make_poke(), "ひかりのかべ", _fsc)
    check("スクリーンlight_screen: ひかりのかべ", _s1sc.light_screen, f"light_screen={_s1sc.light_screen}")

# ── くろいきり ──
check("DB: くろいきり 取得可能", dl.get_move("くろいきり") is not None)
# くろいきり: 両者の能力変化リセット
_pck = make_poke(); _pck.stage_attack = 3; _dck = make_poke(); _dck.stage_defense = 2
execute(_pck, _dck, "くろいきり")
check("くろいきり 能力リセット: くろいきり", _pck.stage_attack == 0 and _dck.stage_defense == 0)

# ── リフレクター ──
check("DB: リフレクター 取得可能", dl.get_move("リフレクター") is not None)
# リフレクター: スクリーンreflect
_mv_sc_リフレクタ_ = dl.get_move("リフレクター")
if _mv_sc_リフレクタ_:
    _fsc = BattleField()
    _s1sc, _s2sc, _fsc = execute_ctx(make_poke(type1="エスパー"), make_poke(), "リフレクター", _fsc)
    check("スクリーンreflect: リフレクター", _s1sc.reflect, f"reflect={_s1sc.reflect}")

# ── じばく ──
check("DB: じばく 取得可能", dl.get_move("じばく") is not None)
_mv_じばく = dl.get_move("じばく")
if _mv_じばく:
    _pa_じばく = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_じばく = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_じばく = dmg(_pa_じばく, _pd_じばく, "じばく")
    check("ダメージ計算: じばく", _d_じばく > 0, f"dmg={_d_じばく}")
# じばく: 自己ひんし
_mvsf_じばく = dl.get_move("じばく")
if _mvsf_じばく:
    _pasf = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pdsf = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
    execute(_pasf, _pdsf, "じばく")
    check("自己ひんし: じばく", not _pasf.is_alive)

# ── だいもんじ ──
check("DB: だいもんじ 取得可能", dl.get_move("だいもんじ") is not None)
_mv_だいもんじ = dl.get_move("だいもんじ")
if _mv_だいもんじ:
    _pa_だいもんじ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_だいもんじ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_だいもんじ = dmg(_pa_だいもんじ, _pd_だいもんじ, "だいもんじ")
    check("ダメージ計算: だいもんじ", _d_だいもんじ > 0, f"dmg={_d_だいもんじ}")
# だいもんじ: やけど10%
_mv_s_だいもんじ = dl.get_move("だいもんじ")
if _mv_s_だいもんじ:
    random.seed(0); _hit_だいもんじ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "だいもんじ")
        _hit_だいもんじ += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): だいもんじ", 9 <= _hit_だいもんじ <= 66, f"count={_hit_だいもんじ}/300")
    random.seed(1); _immok_だいもんじ = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "だいもんじ")
        if _pdi.status == "burn": _immok_だいもんじ = False; break
    check("やけど免疫(ほのお型には無効): だいもんじ", _immok_だいもんじ, "免疫タイプに状態異常が付与されないこと")

# ── たきのぼり ──
check("DB: たきのぼり 取得可能", dl.get_move("たきのぼり") is not None)
_mv_たきのぼり = dl.get_move("たきのぼり")
if _mv_たきのぼり:
    _pa_たきのぼり = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_たきのぼり = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_たきのぼり = dmg(_pa_たきのぼり, _pd_たきのぼり, "たきのぼり")
    check("ダメージ計算: たきのぼり", _d_たきのぼり > 0, f"dmg={_d_たきのぼり}")
# たきのぼり: ひるみ20%
_mv_f_たきのぼり = dl.get_move("たきのぼり")
if _mv_f_たきのぼり:
    random.seed(1); _fh_たきのぼり = 0
    for _ in range(300):
        _pa3 = make_poke(type1="みず", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "たきのぼり"); _fh_たきのぼり += int(_pd3.flinched)
    check("ひるみ(20%): たきのぼり", 18 <= _fh_たきのぼり <= 117, f"count={_fh_たきのぼり}/300")

# ── ドわすれ ──
check("DB: ドわすれ 取得可能", dl.get_move("ドわすれ") is not None)
# ドわすれ: 自分特防+2
_mv_sb_ドわすれ_sp_defense = dl.get_move("ドわすれ")
if _mv_sb_ドわすれ_sp_defense:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ドわすれ")
    check("自分特防+2: ドわすれ", _pa_sb.stage_sp_defense == 2, f"1回適用={_pa_sb.stage_sp_defense} 期待=+2")
# ドわすれ: 自分特防+2
_mvss_ドわすれ_sp_defense = dl.get_move("ドわすれ")
if _mvss_ドわすれ_sp_defense:
    random.seed(0); _got_ドわすれ_sp_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="エスパー", atk_b=60, spatk_b=60); _pds = make_poke(type1="かくとう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "ドわすれ")
        if _pas.stage_sp_defense != 0: _got_ドわすれ_sp_defense = _pas.stage_sp_defense; break
    check("自分特防+2: ドわすれ", _got_ドわすれ_sp_defense == 2, f"1回適用={_got_ドわすれ_sp_defense} 期待=2")

# ── とびひざげり ──
check("DB: とびひざげり 取得可能", dl.get_move("とびひざげり") is not None)
_mv_とびひざげり = dl.get_move("とびひざげり")
if _mv_とびひざげり:
    _pa_とびひざげり = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_とびひざげり = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_とびひざげり = dmg(_pa_とびひざげり, _pd_とびひざげり, "とびひざげり")
    check("ダメージ計算: とびひざげり", _d_とびひざげり > 0, f"dmg={_d_とびひざげり}")
# とびひざげり: 外れ時1/2自傷
_mv_mr_とびひざげり = dl.get_move("とびひざげり")
if _mv_mr_とびひざげり:
    _pa_mr = make_poke(type1="かくとう", atk_b=100)
    import copy as _cp; _mv_miss = _cp.copy(_mv_mr_とびひざげり); _mv_miss.accuracy = 1
    random.seed(99); _s1m = BattleSide([_pa_mr]); _s2m = BattleSide([make_poke()])
    _execute_move(_s1m, _s2m, Action(type="move", move=_mv_miss), BattleField())
    check("外れ時1/2自傷: とびひざげり", _pa_mr.max_hp - _pa_mr.hp == max(1, _pa_mr.max_hp//2), f"dmg={_pa_mr.max_hp - _pa_mr.hp}")

# ── へびにらみ ──
check("DB: へびにらみ 取得可能", dl.get_move("へびにらみ") is not None)
# へびにらみ: まひ付与(変化技)
_mv_si_へびにらみ = dl.get_move("へびにらみ")
if _mv_si_へびにらみ:
    random.seed(0); _ok_へびにらみ = False
    for _ in range(30):
        _pa_si = make_poke(type1="ノーマル"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "へびにらみ")
        if _pd_si.status == "paralysis": _ok_へびにらみ = True; break
    check("まひ付与: へびにらみ", _ok_へびにらみ)
    random.seed(2); _siimm_へびにらみ = True
    for _ in range(40):
        _pai2 = make_poke(type1="ノーマル"); _pdi2 = make_poke(type1="でんき", hp_b=255)
        execute(_pai2, _pdi2, "へびにらみ")
        if _pdi2.status == "paralysis": _siimm_へびにらみ = False; break
    check("まひ免疫(でんき型には無効): へびにらみ", _siimm_へびにらみ, "免疫タイプに付与されないこと")

# ── きゅうけつ ──
check("DB: きゅうけつ 取得可能", dl.get_move("きゅうけつ") is not None)
_mv_きゅうけつ = dl.get_move("きゅうけつ")
if _mv_きゅうけつ:
    _pa_きゅうけつ = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_きゅうけつ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_きゅうけつ = dmg(_pa_きゅうけつ, _pd_きゅうけつ, "きゅうけつ")
    check("ダメージ計算: きゅうけつ", _d_きゅうけつ > 0, f"dmg={_d_きゅうけつ}")
# きゅうけつ: ドレイン（与ダメの1/2回復）
_mv_dr_きゅうけつ = dl.get_move("きゅうけつ")
if _mv_dr_きゅうけつ:
    _pa_dr = make_poke(type1="むし", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_きゅうけつ = False; _dr_dealt_きゅうけつ = 0; _dr_heal_きゅうけつ = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="くさ", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "きゅうけつ")
        _dr_dealt_きゅうけつ = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_きゅうけつ = _pa_dr.hp - 1
        if _dr_dealt_きゅうけつ > 0: _dr_ok_きゅうけつ = abs(_dr_heal_きゅうけつ - max(1, _dr_dealt_きゅうけつ * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): きゅうけつ", _dr_ok_きゅうけつ, f"dealt={_dr_dealt_きゅうけつ} heal={_dr_heal_きゅうけつ}")

# ── へんしん ──
check("DB: へんしん 取得可能", dl.get_move("へんしん") is not None)
# へんしん: 相手のステータス・タイプをコピー
_pt = make_poke(type1="ノーマル", atk_b=40); _dt = make_poke(type1="みず", atk_b=180)
execute(_pt, _dt, "へんしん")
check("変身コピー: へんしん", _pt.attack == _dt.attack and _pt.type1 == "みず", f"atk={_pt.attack}/{_dt.attack} type={_pt.type1}")
# HP以外の全ステータスをコピー・HPは自分のまま
_dt2 = make_poke(type1="みず", atk_b=180, def_b=170, spatk_b=160, spdef_b=150, spd_b=140)
_pt2 = make_poke(type1="ノーマル", atk_b=40, hp_b=200); _hp_keep = _pt2.max_hp
execute(_pt2, _dt2, "へんしん")
check("全ステータスコピー: へんしん", (_pt2.attack,_pt2.defense,_pt2.sp_attack,_pt2.sp_defense,_pt2.speed) == (_dt2.attack,_dt2.defense,_dt2.sp_attack,_dt2.sp_defense,_dt2.speed), f"self={(_pt2.attack,_pt2.defense,_pt2.sp_attack,_pt2.sp_defense,_pt2.speed)} foe={(_dt2.attack,_dt2.defense,_dt2.sp_attack,_dt2.sp_defense,_dt2.speed)}")
check("HPはコピーしない: へんしん", _pt2.max_hp == _hp_keep, f"max_hp={_pt2.max_hp} keep={_hp_keep}")
# 特性・技PP5・状態異常/持ち物の非コピー・交代で元に戻る
_dt3 = make_poke(type1="みず", atk_b=180, spatk_b=160, ability="ちょすい", moves=["たいあたり","なみのり"]); _dt3.status = "burn"; _dt3.item = "オボンのみ"
_sht = BattleSide([make_poke(type1="ノーマル", atk_b=40, ability="てんねん"), make_poke()])
_orig_atk = _sht.active.attack; _orig_ab = _sht.active.ability; _sht.active.item = None
execute(_sht.active, _dt3, "へんしん")
_tf = _sht.active
check("特性コピー: へんしん", _tf.ability == "ちょすい", f"ability={_tf.ability}")
check("技PP5: へんしん", len(_tf.pp) > 0 and all(p == 5 for p in _tf.pp), f"pp={_tf.pp}")
check("状態異常は非コピー: へんしん", _tf.status is None, f"status={_tf.status}")
check("持ち物は非コピー: へんしん", _tf.item is None, f"item={_tf.item}")
_sht.switch_to(1)
check("交代で元に戻る: へんしん", _sht.party[0].attack == _orig_atk and _sht.party[0].ability == _orig_ab and not getattr(_sht.party[0], "_transformed", False), f"atk={_sht.party[0].attack}/{_orig_atk} ab={_sht.party[0].ability}/{_orig_ab}")
# 命中・回避ランクもコピーする
_dt4 = make_poke(type1="みず"); _dt4.stage_accuracy = 2; _dt4.stage_evasion = -1
_pt4 = make_poke(type1="ノーマル"); execute(_pt4, _dt4, "へんしん")
check("命中回避ランクもコピー: へんしん", _pt4.stage_accuracy == 2 and _pt4.stage_evasion == -1, f"acc={_pt4.stage_accuracy} eva={_pt4.stage_evasion}")

# ── クラブハンマー ──
check("DB: クラブハンマー 取得可能", dl.get_move("クラブハンマー") is not None)
_mv_クラブハンマ_ = dl.get_move("クラブハンマー")
if _mv_クラブハンマ_:
    _pa_クラブハンマ_ = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_クラブハンマ_ = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_クラブハンマ_ = dmg(_pa_クラブハンマ_, _pd_クラブハンマ_, "クラブハンマー")
    check("ダメージ計算: クラブハンマー", _d_クラブハンマ_ > 0, f"dmg={_d_クラブハンマ_}")
# クラブハンマー: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_クラブハンマ_
random.seed(0); _hc_crit_クラブハンマ_ = 0; _phc = make_poke(type1="みず")
_mvhc_クラブハンマ_ = dl.get_move("クラブハンマー")
for _ in range(800):
    if _cc_クラブハンマ_(_phc, _mvhc_クラブハンマ_, make_poke(type1="ほのお")): _hc_crit_クラブハンマ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: クラブハンマー", 60 <= _hc_crit_クラブハンマ_ <= 150, f"crit={_hc_crit_クラブハンマ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── とける ──
check("DB: とける 取得可能", dl.get_move("とける") is not None)
# とける: 自分防御+2
_mv_sb_とける_defense = dl.get_move("とける")
if _mv_sb_とける_defense:
    _pa_sb = make_poke(type1="どく"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "とける")
    check("自分防御+2: とける", _pa_sb.stage_defense == 2, f"1回適用={_pa_sb.stage_defense} 期待=+2")
# とける: 自分防御+2
_mvss_とける_defense = dl.get_move("とける")
if _mvss_とける_defense:
    random.seed(0); _got_とける_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="どく", atk_b=60, spatk_b=60); _pds = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "とける")
        if _pas.stage_defense != 0: _got_とける_defense = _pas.stage_defense; break
    check("自分防御+2: とける", _got_とける_defense == 2, f"1回適用={_got_とける_defense} 期待=2")

# ── だいばくはつ ──
check("DB: だいばくはつ 取得可能", dl.get_move("だいばくはつ") is not None)
_mv_だいばくはつ = dl.get_move("だいばくはつ")
if _mv_だいばくはつ:
    _pa_だいばくはつ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_だいばくはつ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_だいばくはつ = dmg(_pa_だいばくはつ, _pd_だいばくはつ, "だいばくはつ")
    check("ダメージ計算: だいばくはつ", _d_だいばくはつ > 0, f"dmg={_d_だいばくはつ}")
# だいばくはつ: 自己ひんし
_mvsf_だいばくはつ = dl.get_move("だいばくはつ")
if _mvsf_だいばくはつ:
    _pasf = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pdsf = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
    execute(_pasf, _pdsf, "だいばくはつ")
    check("自己ひんし: だいばくはつ", not _pasf.is_alive)

# ── いわなだれ ──
check("DB: いわなだれ 取得可能", dl.get_move("いわなだれ") is not None)
_mv_いわなだれ = dl.get_move("いわなだれ")
if _mv_いわなだれ:
    _pa_いわなだれ = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_いわなだれ = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_いわなだれ = dmg(_pa_いわなだれ, _pd_いわなだれ, "いわなだれ")
    check("ダメージ計算: いわなだれ", _d_いわなだれ > 0, f"dmg={_d_いわなだれ}")
# いわなだれ: ひるみ30%
_mv_f_いわなだれ = dl.get_move("いわなだれ")
if _mv_f_いわなだれ:
    random.seed(1); _fh_いわなだれ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="いわ", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="ひこう", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "いわなだれ"); _fh_いわなだれ += int(_pd3.flinched)
    check("ひるみ(30%): いわなだれ", 27 <= _fh_いわなだれ <= 168, f"count={_fh_いわなだれ}/300")

# ── ねむる ──
check("DB: ねむる 取得可能", dl.get_move("ねむる") is not None)
# ねむる: HP回復（最大HPの約1/2・無天候）
_mv_hp_ねむる = dl.get_move("ねむる")
if _mv_hp_ねむる:
    _pa_hp = make_poke(type1="エスパー", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "ねむる")
    _exp_hp_ねむる = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): ねむる", abs(_pa_hp.hp - (1 + _exp_hp_ねむる)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_ねむる}")
# ねむる: HP満タンだと失敗、減っていれば全回復+ねむり
_pnf = make_poke(type1="ノーマル", hp_b=200); execute(_pnf, make_poke(), "ねむる")
check("満タン失敗: ねむる", _pnf.status != "sleep", f"status={_pnf.status}")
_pns = make_poke(type1="ノーマル", hp_b=200); _pns.hp = _pns.max_hp // 2; execute(_pns, make_poke(), "ねむる")
check("ねむる付与: ねむる", _pns.status == "sleep" and _pns.hp == _pns.max_hp, f"status={_pns.status} hp={_pns.hp}")

# ── いかりのまえば ──
check("DB: いかりのまえば 取得可能", dl.get_move("いかりのまえば") is not None)
# いかりのまえば: 相手の残りHPの1/2のダメージ
_pi = make_poke(atk_b=100); _di = make_poke(hp_b=200); _di.hp = 160
execute(_pi, _di, "いかりのまえば")
check("1/2ダメ: いかりのまえば", _di.hp == 80, f"hp={_di.hp}")
# 残りHP1の相手には1ダメージ（最低1保証）
_pi2 = make_poke(atk_b=100); _di2 = make_poke(hp_b=200); _di2.hp = 1
execute(_pi2, _di2, "いかりのまえば")
check("残りHP1で1ダメージ: いかりのまえば", _di2.hp == 0, f"hp={_di2.hp}")

# ── みがわり ──
check("DB: みがわり 取得可能", dl.get_move("みがわり") is not None)
# みがわり: HP1/4消費して身代わり生成
_pm = make_poke(hp_b=200); _hpm = _pm.hp; execute(_pm, make_poke(), "みがわり")
check("みがわり生成: みがわり", getattr(_pm, "_substitute_hp", 0) > 0 and _pm.hp < _hpm, f"sub={getattr(_pm,'_substitute_hp',0)} hp={_pm.hp}/{_hpm}")
# 身代わりが技を肩代わり（本体HPは減らない・身代わりHPが減る）
_pms = make_poke(hp_b=200); execute(_pms, make_poke(), "みがわり"); _sub0 = _pms._substitute_hp; _hpms = _pms.hp
_atkms = make_poke(type1="ノーマル", atk_b=20, moves=["たいあたり"])
_execute_move(BattleSide([_atkms]), BattleSide([_pms]), Action(type="move", move=dl.get_move("たいあたり")), BattleField())
check("みがわり中は本体ダメージなし: みがわり", _pms.hp == _hpms and _pms._substitute_hp < _sub0, f"hp={_pms.hp}/{_hpms} sub={_pms._substitute_hp}/{_sub0}")
# 身代わりHPを超えるダメージで身代わりが消える
_pmb = make_poke(hp_b=200); execute(_pmb, make_poke(), "みがわり")
_atkmb = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])
_execute_move(BattleSide([_atkmb]), BattleSide([_pmb]), Action(type="move", move=dl.get_move("インファイト")), BattleField())
check("大ダメージで身代わり消滅: みがわり", getattr(_pmb, "_substitute_hp", 0) == 0, f"sub={getattr(_pmb,'_substitute_hp',0)}")

# ── どろぼう ──
check("DB: どろぼう 取得可能", dl.get_move("どろぼう") is not None)
_mv_どろぼう = dl.get_move("どろぼう")
if _mv_どろぼう:
    _pa_どろぼう = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_どろぼう = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_どろぼう = dmg(_pa_どろぼう, _pd_どろぼう, "どろぼう")
    check("ダメージ計算: どろぼう", _d_どろぼう > 0, f"dmg={_d_どろぼう}")
# どろぼう: 相手の道具を奪う（自分が道具なし時のみ）
_pst = make_poke(type1="あく", atk_b=120); _pst.item = None
_dst = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst.item = "オボンのみ"
execute(_pst, _dst, "どろぼう")
check("道具奪取: どろぼう", _pst.item == "オボンのみ" and _dst.item is None, f"atk={_pst.item} def={_dst.item}")
# 攻撃者が道具持ちの場合は奪わない
_pst2 = make_poke(type1="あく", atk_b=120, item="こだわりスカーフ"); _dst2 = make_poke(type1="ノーマル", hp_b=255, def_b=100, item="オボンのみ")
execute(_pst2, _dst2, "どろぼう")
check("道具持ちは奪わない: どろぼう", _pst2.item == "こだわりスカーフ" and _dst2.item == "オボンのみ", f"atk={_pst2.item} def={_dst2.item}")
# 相手がメガストーンを持っている場合は奪えない
_pst3 = make_poke(type1="あく", atk_b=120); _pst3.item = None
_dst3 = make_poke(type1="ノーマル", hp_b=255, def_b=100, item="ガブリアスナイト")
execute(_pst3, _dst3, "どろぼう")
check("メガストーンは奪えない: どろぼう", _pst3.item is None and _dst3.item == "ガブリアスナイト", f"atk={_pst3.item} def={_dst3.item}")

# ── のろい ──
check("DB: のろい 取得可能", dl.get_move("のろい") is not None)
# のろい(非ゴースト): 攻+1防+1速-1
_pn = make_poke(type1="ノーマル"); execute(_pn, make_poke(), "のろい")
check("のろい非ゴースト 攻+1: のろい", _pn.stage_attack == 1)
check("のろい非ゴースト 防+1: のろい", _pn.stage_defense == 1)
check("のろい非ゴースト 速-1: のろい", _pn.stage_speed == -1)
_pg = make_poke(type1="ゴースト"); _dg = make_poke()
execute(_pg, _dg, "のろい")
check("のろいゴースト 相手呪い: のろい", getattr(_dg, "cursed", False))

# ── いびき ──
check("DB: いびき 取得可能", dl.get_move("いびき") is not None)
_mv_いびき = dl.get_move("いびき")
if _mv_いびき:
    _pa_いびき = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_いびき = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_いびき = dmg(_pa_いびき, _pd_いびき, "いびき")
    check("ダメージ計算: いびき", _d_いびき > 0, f"dmg={_d_いびき}")
# いびき: 覚醒時は失敗、ねむり中は使えて30%ひるみ
_pib = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _dib = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)
_hpib = _dib.hp; execute(_pib, _dib, "いびき")
check("覚醒時は失敗: いびき", _dib.hp == _hpib, f"hp={_dib.hp}/{_hpib}")
random.seed(2); _ib_fl = 0
for _ in range(300):
    _pib2 = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pib2.status = "sleep"; _pib2.sleep_count = 5
    _dib2 = make_poke(type1="ノーマル", hp_b=255, spdef_b=120, def_b=120)
    execute(_pib2, _dib2, "いびき"); _ib_fl += int(_dib2.flinched)
check("ねむり中使用+30%ひるみ: いびき", 40 <= _ib_fl <= 140, f"flinch={_ib_fl}/300")

# ── わたほうし ──
check("DB: わたほうし 取得可能", dl.get_move("わたほうし") is not None)
# わたほうし: 相手素早さ-2
_mv_dd_わたほうし = dl.get_move("わたほうし")
if _mv_dd_わたほうし:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_わたほうし = 0; _dd_ok_わたほうし = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "わたほうし")
        if _pd_dd.stage_speed != 0: _dd_val_わたほうし = _pd_dd.stage_speed; _dd_ok_わたほうし = True; break
    check("相手素早さ-2: わたほうし", _dd_ok_わたほうし and _dd_val_わたほうし == -2, f"1回適用={_dd_val_わたほうし} 期待=-2")
# わたほうし: 素早さ-2。くさタイプには無効（粉）
_pwt = make_poke(type1="むし"); random.seed(0); _wt_ok = False
for _ in range(20):
    _dwt = make_poke(type1="ノーマル", hp_b=200); execute(_pwt, _dwt, "わたほうし")
    if _dwt.stage_speed == -2: _wt_ok = True; break
check("素早さ-2: わたほうし", _wt_ok)
_dwt2 = make_poke(type1="くさ", hp_b=200); execute(_pwt, _dwt2, "わたほうし")
check("くさ無効: わたほうし", _dwt2.stage_speed == 0, f"spd={_dwt2.stage_speed}")

# ── きしかいせい ──
check("DB: きしかいせい 取得可能", dl.get_move("きしかいせい") is not None)
# きしかいせい: HP比別の威力テーブル（>67.7%→20 ... ≤3.1%→200）
_ph = make_poke(type1="かくとう", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="ノーマル")
_ks_ng = []
for _r, _exp in [(0.80,20),(0.50,40),(0.30,80),(0.15,100),(0.05,150),(0.01,200)]:
    _ph.hp = max(1, int(_ph.max_hp * _r))
    _got = _ep(_ph, _dd, dl.get_move("きしかいせい"), BattleField())
    if _got != _exp: _ks_ng.append(f"r={_r}:{_got}!={_exp}")
check("HP比別威力テーブル: きしかいせい", not _ks_ng, f"NG={_ks_ng}")

# ── マッハパンチ ──
check("DB: マッハパンチ 取得可能", dl.get_move("マッハパンチ") is not None)
_mv_マッハパンチ = dl.get_move("マッハパンチ")
if _mv_マッハパンチ:
    _pa_マッハパンチ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_マッハパンチ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_マッハパンチ = dmg(_pa_マッハパンチ, _pd_マッハパンチ, "マッハパンチ")
    check("ダメージ計算: マッハパンチ", _d_マッハパンチ > 0, f"dmg={_d_マッハパンチ}")
# マッハパンチ: 優先度1
_mv_pr_マッハパンチ = dl.get_move("マッハパンチ")
if _mv_pr_マッハパンチ and _mv_pr_マッハパンチ.priority == 1:
    check("優先度1: マッハパンチ", _mv_pr_マッハパンチ.priority == 1)
elif _mv_pr_マッハパンチ:
    check("優先度1: マッハパンチ", _mv_pr_マッハパンチ.priority == 1, f"DB優先度={_mv_pr_マッハパンチ.priority} 仕様=1")

# ── こわいかお ──
check("DB: こわいかお 取得可能", dl.get_move("こわいかお") is not None)
# こわいかお: 相手素早さ-2
_mv_dd_こわいかお = dl.get_move("こわいかお")
if _mv_dd_こわいかお:
    _pa_dd = make_poke(type1="ノーマル", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_こわいかお = 0; _dd_ok_こわいかお = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "こわいかお")
        if _pd_dd.stage_speed != 0: _dd_val_こわいかお = _pd_dd.stage_speed; _dd_ok_こわいかお = True; break
    check("相手素早さ-2: こわいかお", _dd_ok_こわいかお and _dd_val_こわいかお == -2, f"1回適用={_dd_val_こわいかお} 期待=-2")

# ── まもる ──
check("DB: まもる 取得可能", dl.get_move("まもる") is not None)
# まもる: 優先度4
_mv_pr_まもる = dl.get_move("まもる")
if _mv_pr_まもる and _mv_pr_まもる.priority == 4:
    check("優先度4: まもる", _mv_pr_まもる.priority == 4)
elif _mv_pr_まもる:
    check("優先度4: まもる", _mv_pr_まもる.priority == 4, f"DB優先度={_mv_pr_まもる.priority} 仕様=4")
# まもる: 連続使用で成功率1/3に低下（protect_consecutiveが増える）
_pmm = make_poke(type1="ノーマル"); _s1m = BattleSide([_pmm]); _s2m = BattleSide([make_poke()])
_execute_move(_s1m, _s2m, Action(type="move", move=dl.get_move("まもる")), BattleField())
check("まもる成功: まもる", _pmm.protecting)
random.seed(0); _fail_seen = False
for _ in range(40):
    _pmc = make_poke(type1="ノーマル"); _pmc.protect_consecutive = 1; _s1c = BattleSide([_pmc])
    _execute_move(_s1c, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("まもる")), BattleField())
    if not _pmc.protecting: _fail_seen = True; break
check("連続成功率低下: まもる", _fail_seen)

# ── はらだいこ ──
check("DB: はらだいこ 取得可能", dl.get_move("はらだいこ") is not None)
# はらだいこ: HP不足だと失敗、足りればA最大+HP半減
_phf = make_poke(type1="ノーマル", hp_b=200); _phf.hp = _phf.max_hp // 2; execute(_phf, make_poke(), "はらだいこ")
check("HP不足失敗: はらだいこ", _phf.stage_attack < 6, f"atk_stage={_phf.stage_attack}")
_phs = make_poke(type1="ノーマル", hp_b=200); execute(_phs, make_poke(), "はらだいこ")
check("はらだいこ成功: はらだいこ", _phs.stage_attack == 6 and _phs.hp < _phs.max_hp, f"atk={_phs.stage_attack} hp={_phs.hp}")

# ── まきびし ──
check("DB: まきびし 取得可能", dl.get_move("まきびし") is not None)
# まきびし: ハザードspikes
_mvhz_まきびし = dl.get_move("まきびし")
if _mvhz_まきびし:
    _s1h, _s2h, _fh2 = execute_ctx(make_poke(type1="じめん"), make_poke(), "まきびし")
    _hzval = _fh2.spikes[_s2h.field_idx]
    check("ハザードspikes: まきびし", bool(_hzval), f"val={_hzval}")

# ── ヘドロばくだん ──
check("DB: ヘドロばくだん 取得可能", dl.get_move("ヘドロばくだん") is not None)
_mv_ヘドロばくだん = dl.get_move("ヘドロばくだん")
if _mv_ヘドロばくだん:
    _pa_ヘドロばくだん = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_ヘドロばくだん = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ヘドロばくだん = dmg(_pa_ヘドロばくだん, _pd_ヘドロばくだん, "ヘドロばくだん")
    check("ダメージ計算: ヘドロばくだん", _d_ヘドロばくだん > 0, f"dmg={_d_ヘドロばくだん}")
# ヘドロばくだん: どく30%
_mv_s_ヘドロばくだん = dl.get_move("ヘドロばくだん")
if _mv_s_ヘドロばくだん:
    random.seed(0); _hit_ヘドロばくだん = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ヘドロばくだん")
        _hit_ヘドロばくだん += int((_pd2.status == "poison"))
    check("追加効果(どく30%): ヘドロばくだん", 27 <= _hit_ヘドロばくだん <= 168, f"count={_hit_ヘドロばくだん}/300")
    random.seed(1); _immok_ヘドロばくだん = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ヘドロばくだん")
        if _pdi.status == "poison": _immok_ヘドロばくだん = False; break
    check("どく免疫(どく型には無効): ヘドロばくだん", _immok_ヘドロばくだん, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_ヘドロばくだん = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ヘドロばくだん")
        if _pdi.status == "poison": _immok_ヘドロばくだん = False; break
    check("どく免疫(はがね型には無効): ヘドロばくだん", _immok_ヘドロばくだん, "免疫タイプに状態異常が付与されないこと")

# ── こごえるかぜ ──
check("DB: こごえるかぜ 取得可能", dl.get_move("こごえるかぜ") is not None)
_mv_こごえるかぜ = dl.get_move("こごえるかぜ")
if _mv_こごえるかぜ:
    _pa_こごえるかぜ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_こごえるかぜ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_こごえるかぜ = dmg(_pa_こごえるかぜ, _pd_こごえるかぜ, "こごえるかぜ")
    check("ダメージ計算: こごえるかぜ", _d_こごえるかぜ > 0, f"dmg={_d_こごえるかぜ}")
# こごえるかぜ: 相手素早さ-1
_mv_dd_こごえるかぜ = dl.get_move("こごえるかぜ")
if _mv_dd_こごえるかぜ:
    _pa_dd = make_poke(type1="こおり", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_こごえるかぜ = 0; _dd_ok_こごえるかぜ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "こごえるかぜ")
        if _pd_dd.stage_speed != 0: _dd_val_こごえるかぜ = _pd_dd.stage_speed; _dd_ok_こごえるかぜ = True; break
    check("相手素早さ-1: こごえるかぜ", _dd_ok_こごえるかぜ and _dd_val_こごえるかぜ == -1, f"1回適用={_dd_val_こごえるかぜ} 期待=-1")

# ── みちづれ ──
check("DB: みちづれ 取得可能", dl.get_move("みちづれ") is not None)
# みちづれ: 道連れ付与 + 連続使用は失敗
_pmz = make_poke(type1="ゴースト"); execute(_pmz, make_poke(), "みちづれ")
check("みちづれ付与: みちづれ", _pmz.destiny_bond)
# 連続使用は失敗（前ターン使用フラグが立っている場合）
_pmz2 = make_poke(type1="ゴースト"); _pmz2._destiny_bond_last_turn = True
execute(_pmz2, make_poke(), "みちづれ")
check("連続失敗: みちづれ", not _pmz2.destiny_bond, f"destiny_bond={_pmz2.destiny_bond}")
_pmz2 = make_poke(type1="ゴースト", hp_b=1, def_b=1); _pmz2.destiny_bond = True
_fatk = make_poke(type1="あく", atk_b=255, moves=["かみくだく"])
_execute_move(BattleSide([_fatk]), BattleSide([_pmz2]), Action(type="move", move=dl.get_move("かみくだく")), BattleField())
check("道連れ発動: みちづれ", not _pmz2.is_alive and not _fatk.is_alive, f"自{_pmz2.is_alive} 相{_fatk.is_alive}")

# ── ほろびのうた ──
check("DB: ほろびのうた 取得可能", dl.get_move("ほろびのうた") is not None)
# ほろびのうた: 場の全員をほろび状態に
_ph = make_poke(); _dh = make_poke(); execute(_ph, _dh, "ほろびのうた")
check("ほろび付与: ほろびのうた", _ph.perish_count > 0 and _dh.perish_count > 0, f"自{_ph.perish_count} 相{_dh.perish_count}")

# ── げきりん ──
check("DB: げきりん 取得可能", dl.get_move("げきりん") is not None)
_mv_げきりん = dl.get_move("げきりん")
if _mv_げきりん:
    _pa_げきりん = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_げきりん = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_げきりん = dmg(_pa_げきりん, _pd_げきりん, "げきりん")
    check("ダメージ計算: げきりん", _d_げきりん > 0, f"dmg={_d_げきりん}")
# げきりん: あばれ状態
_mv_rg_げきりん = dl.get_move("げきりん")
if _mv_rg_げきりん:
    _pa_rg = make_poke(type1="ドラゴン", atk_b=30, spatk_b=30); _pd_rg = make_poke(type1="ドラゴン", def_b=255, spdef_b=255, hp_b=255)
    execute(_pa_rg, _pd_rg, "げきりん")
    check("あばれ状態: げきりん", _pa_rg.locked_move == "げきりん")

# ── みきり ──
check("DB: みきり 取得可能", dl.get_move("みきり") is not None)
# みきり: 優先度4
_mv_pr_みきり = dl.get_move("みきり")
if _mv_pr_みきり and _mv_pr_みきり.priority == 4:
    check("優先度4: みきり", _mv_pr_みきり.priority == 4)
elif _mv_pr_みきり:
    check("優先度4: みきり", _mv_pr_みきり.priority == 4, f"DB優先度={_mv_pr_みきり.priority} 仕様=4")
# みきり: まもる状態になり相手の技を防ぐ
_pmk = make_poke(type1="かくとう"); execute(_pmk, make_poke(), "みきり")
check("まもる状態: みきり", _pmk.protecting)
_pmk2 = make_poke(type1="かくとう"); _pmk2.protecting = True; _dmk = make_poke(type1="ノーマル", atk_b=200, hp_b=255)
_hpmk = _pmk2.hp
_execute_move(BattleSide([_dmk]), BattleSide([_pmk2]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())
check("技を防ぐ: みきり", _pmk2.hp == _hpmk, f"hp={_pmk2.hp}/{_hpmk}")

# ── ギガドレイン ──
check("DB: ギガドレイン 取得可能", dl.get_move("ギガドレイン") is not None)
_mv_ギガドレイン = dl.get_move("ギガドレイン")
if _mv_ギガドレイン:
    _pa_ギガドレイン = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ギガドレイン = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ギガドレイン = dmg(_pa_ギガドレイン, _pd_ギガドレイン, "ギガドレイン")
    check("ダメージ計算: ギガドレイン", _d_ギガドレイン > 0, f"dmg={_d_ギガドレイン}")
# ギガドレイン: ドレイン（与ダメの1/2回復）
_mv_dr_ギガドレイン = dl.get_move("ギガドレイン")
if _mv_dr_ギガドレイン:
    _pa_dr = make_poke(type1="くさ", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_ギガドレイン = False; _dr_dealt_ギガドレイン = 0; _dr_heal_ギガドレイン = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="みず", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "ギガドレイン")
        _dr_dealt_ギガドレイン = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_ギガドレイン = _pa_dr.hp - 1
        if _dr_dealt_ギガドレイン > 0: _dr_ok_ギガドレイン = abs(_dr_heal_ギガドレイン - max(1, _dr_dealt_ギガドレイン * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): ギガドレイン", _dr_ok_ギガドレイン, f"dealt={_dr_dealt_ギガドレイン} heal={_dr_heal_ギガドレイン}")

# ── こらえる ──
check("DB: こらえる 取得可能", dl.get_move("こらえる") is not None)
# こらえる: 優先度4
_mv_pr_こらえる = dl.get_move("こらえる")
if _mv_pr_こらえる and _mv_pr_こらえる.priority == 4:
    check("優先度4: こらえる", _mv_pr_こらえる.priority == 4)
elif _mv_pr_こらえる:
    check("優先度4: こらえる", _mv_pr_こらえる.priority == 4, f"DB優先度={_mv_pr_こらえる.priority} 仕様=4")
# こらえる: KO級ダメージでもHP1で耐える（まもる系の全無効とは別）
from simulator.battle import Battle as _Bce
_pce = make_poke(type1="ノーマル", hp_b=1, def_b=1)
_fce = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])
_act_end = lambda s,o,f: Action(type="move", move=dl.get_move("こらえる"), move_idx=0)
_act_atk = lambda s,o,f: Action(type="move", move=dl.get_move("インファイト"), move_idx=0)
_bce = _Bce(BattleSide([_pce]), BattleSide([_fce]))
import simulator.battle as _SBe; _SBemax = _SBe.MAX_TURNS; _SBe.MAX_TURNS = 1; _bce.run(_act_end, _act_atk); _SBe.MAX_TURNS = _SBemax
check("こらえHP1: こらえる", _pce.is_alive and _pce.hp == 1, f"alive={_pce.is_alive} hp={_pce.hp}")
# negative: こらえる無し（通常）なら同じ攻撃で耐えられない
_pce2 = make_poke(type1="ノーマル", hp_b=1, def_b=1)
_fce2 = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])
execute(_fce2, _pce2, "インファイト")
check("こらえる無し時は耐えられない: こらえる", not _pce2.is_alive, f"alive={_pce2.is_alive} hp={_pce2.hp}")

# ── あまえる ──
check("DB: あまえる 取得可能", dl.get_move("あまえる") is not None)
# あまえる: 相手攻撃-2
_mv_dd_あまえる = dl.get_move("あまえる")
if _mv_dd_あまえる:
    _pa_dd = make_poke(type1="フェアリー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_あまえる = 0; _dd_ok_あまえる = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "あまえる")
        if _pd_dd.stage_attack != 0: _dd_val_あまえる = _pd_dd.stage_attack; _dd_ok_あまえる = True; break
    check("相手攻撃-2: あまえる", _dd_ok_あまえる and _dd_val_あまえる == -2, f"1回適用={_dd_val_あまえる} 期待=-2")

# ── いたみわけ ──
check("DB: いたみわけ 取得可能", dl.get_move("いたみわけ") is not None)
# いたみわけ: 互いのHPを合計して半分ずつ
_pp = make_poke(hp_b=200); _pp.hp = 20; _dp = make_poke(hp_b=200); _dp.hp = 180
execute(_pp, _dp, "いたみわけ")
check("HP折半: いたみわけ", abs(_pp.hp - _dp.hp) <= 1, f"自{_pp.hp} 相{_dp.hp}")

# ── ばくれつパンチ ──
check("DB: ばくれつパンチ 取得可能", dl.get_move("ばくれつパンチ") is not None)
_mv_ばくれつパンチ = dl.get_move("ばくれつパンチ")
if _mv_ばくれつパンチ:
    _pa_ばくれつパンチ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ばくれつパンチ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ばくれつパンチ = dmg(_pa_ばくれつパンチ, _pd_ばくれつパンチ, "ばくれつパンチ")
    check("ダメージ計算: ばくれつパンチ", _d_ばくれつパンチ > 0, f"dmg={_d_ばくれつパンチ}")
# ばくれつパンチ: こんらん100%
_mv_s_ばくれつパンチ = dl.get_move("ばくれつパンチ")
if _mv_s_ばくれつパンチ:
    random.seed(0); _hit_ばくれつパンチ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="かくとう", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ばくれつパンチ")
        _hit_ばくれつパンチ += int(_pd2.confused)
    check("追加効果(こんらん100%): ばくれつパンチ", 90 <= _hit_ばくれつパンチ <= 525, f"count={_hit_ばくれつパンチ}/300")

# ── メガホーン ──
check("DB: メガホーン 取得可能", dl.get_move("メガホーン") is not None)
_mv_メガホ_ン = dl.get_move("メガホーン")
if _mv_メガホ_ン:
    _pa_メガホ_ン = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_メガホ_ン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_メガホ_ン = dmg(_pa_メガホ_ン, _pd_メガホ_ン, "メガホーン")
    check("ダメージ計算: メガホーン", _d_メガホ_ン > 0, f"dmg={_d_メガホ_ン}")

# ── アンコール ──
check("DB: アンコール 取得可能", dl.get_move("アンコール") is not None)
# アンコール: 相手をアンコール状態に
_pen = make_poke(); _den = make_poke(moves=["たいあたり"]); _den.last_used_move = "たいあたり"
execute(_pen, _den, "アンコール")
check("アンコール付与: アンコール", _den.encore_count > 0 and _den.locked_move == "たいあたり")

# ── バトンタッチ ──
check("DB: バトンタッチ 取得可能", dl.get_move("バトンタッチ") is not None)
# バトンタッチ: ピボット交代フラグ
_mvpv_バトンタッチ = dl.get_move("バトンタッチ")
if _mvpv_バトンタッチ:
    _pap = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pdp = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_バトンタッチ), BattleField())
    check("ピボット交代フラグ: バトンタッチ", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")
# バトンタッチ: 能力ランクを交代先に引き継ぐ
_sbt = BattleSide([make_poke(type1="ノーマル"), make_poke(type1="みず")])
_sbt.active.stage_attack = 3; _sbt.active.stage_speed = 2
_execute_move(_sbt, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("バトンタッチ")), BattleField())
_sbt.switch_to(1)
check("能力ランク引き継ぎ: バトンタッチ", _sbt.active.stage_attack == 3 and _sbt.active.stage_speed == 2, f"atk={_sbt.active.stage_attack} spd={_sbt.active.stage_speed}")

# ── こうそくスピン ──
check("DB: こうそくスピン 取得可能", dl.get_move("こうそくスピン") is not None)
_mv_こうそくスピン = dl.get_move("こうそくスピン")
if _mv_こうそくスピン:
    _pa_こうそくスピン = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_こうそくスピン = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_こうそくスピン = dmg(_pa_こうそくスピン, _pd_こうそくスピン, "こうそくスピン")
    check("ダメージ計算: こうそくスピン", _d_こうそくスピン > 0, f"dmg={_d_こうそくスピン}")
# こうそくスピン: 自分素早さ+1
_mvss_こうそくスピン_speed = dl.get_move("こうそくスピン")
if _mvss_こうそくスピン_speed:
    random.seed(0); _got_こうそくスピン_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="ノーマル", atk_b=60, spatk_b=60); _pds = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "こうそくスピン")
        if _pas.stage_speed != 0: _got_こうそくスピン_speed = _pas.stage_speed; break
    check("自分素早さ+1: こうそくスピン", _got_こうそくスピン_speed == 1, f"1回適用={_got_こうそくスピン_speed} 期待=1")
# こうそくスピン: 自分のやどりぎ/バインドを解除
_pcs = make_poke(type1="ノーマル", atk_b=100, spd_b=100); _pcs.seeded = True; _dcs = make_poke(hp_b=255, def_b=120)
execute(_pcs, _dcs, "こうそくスピン")
check("バインド/やどりぎ解除: こうそくスピン", not _pcs.seeded, f"seeded={_pcs.seeded}")

# ── アイアンテール ──
check("DB: アイアンテール 取得可能", dl.get_move("アイアンテール") is not None)
_mv_アイアンテ_ル = dl.get_move("アイアンテール")
if _mv_アイアンテ_ル:
    _pa_アイアンテ_ル = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_アイアンテ_ル = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_アイアンテ_ル = dmg(_pa_アイアンテ_ル, _pd_アイアンテ_ル, "アイアンテール")
    check("ダメージ計算: アイアンテール", _d_アイアンテ_ル > 0, f"dmg={_d_アイアンテ_ル}")
# アイアンテール: 相手防御-1
_mv_dd_アイアンテ_ル = dl.get_move("アイアンテール")
if _mv_dd_アイアンテ_ル:
    _pa_dd = make_poke(type1="はがね", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_アイアンテ_ル = 0; _dd_ok_アイアンテ_ル = False
    for _ in range(60):
        _pd_dd = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "アイアンテール")
        if _pd_dd.stage_defense != 0: _dd_val_アイアンテ_ル = _pd_dd.stage_defense; _dd_ok_アイアンテ_ル = True; break
    check("相手防御-1: アイアンテール", _dd_ok_アイアンテ_ル and _dd_val_アイアンテ_ル == -1, f"1回適用={_dd_val_アイアンテ_ル} 期待=-1")

# ── あさのひざし ──
check("DB: あさのひざし 取得可能", dl.get_move("あさのひざし") is not None)
# あさのひざし: HP回復（最大HPの約1/2・無天候）
_mv_hp_あさのひざし = dl.get_move("あさのひざし")
if _mv_hp_あさのひざし:
    _pa_hp = make_poke(type1="ノーマル", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "あさのひざし")
    _exp_hp_あさのひざし = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): あさのひざし", abs(_pa_hp.hp - (1 + _exp_hp_あさのひざし)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_あさのひざし}")
# あさのひざし: 天候別回復を厳密検証 無天候=1/2・晴れ=2/3・悪天候(雨/砂/あられ)=1/4
_hh_ng = []
for _wen, _expfn in [(None, lambda m: m//2), ("sunny", lambda m: m*2//3), ("rain", lambda m: m//4), ("sandstorm", lambda m: m//4)]:
    _phw = make_poke(hp_b=200); _phw.hp = 1; _mhw = _phw.max_hp
    _fwh = BattleField()
    if _wen: _fwh.weather = _wen
    _execute_move(BattleSide([_phw]), BattleSide([make_poke()]), Action(type="move", move=dl.get_move("あさのひざし")), _fwh)
    _exph = min(_mhw, 1 + _expfn(_mhw))
    if _phw.hp != _exph: _hh_ng.append(str(_wen) + ":" + str(_phw.hp) + "!=" + str(_exph))
check("天候別回復(1/2,2/3,1/4)厳密: あさのひざし", not _hh_ng, "NG=" + str(_hh_ng))

# ── こうごうせい ──
check("DB: こうごうせい 取得可能", dl.get_move("こうごうせい") is not None)
# こうごうせい: HP回復（最大HPの約1/2・無天候）
_mv_hp_こうごうせい = dl.get_move("こうごうせい")
if _mv_hp_こうごうせい:
    _pa_hp = make_poke(type1="くさ", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "こうごうせい")
    _exp_hp_こうごうせい = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): こうごうせい", abs(_pa_hp.hp - (1 + _exp_hp_こうごうせい)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_こうごうせい}")
# こうごうせい: 天候別回復を厳密検証 無天候=1/2・晴れ=2/3・悪天候(雨/砂/あられ)=1/4
_hh_ng = []
for _wen, _expfn in [(None, lambda m: m//2), ("sunny", lambda m: m*2//3), ("rain", lambda m: m//4), ("sandstorm", lambda m: m//4)]:
    _phw = make_poke(hp_b=200); _phw.hp = 1; _mhw = _phw.max_hp
    _fwh = BattleField()
    if _wen: _fwh.weather = _wen
    _execute_move(BattleSide([_phw]), BattleSide([make_poke()]), Action(type="move", move=dl.get_move("こうごうせい")), _fwh)
    _exph = min(_mhw, 1 + _expfn(_mhw))
    if _phw.hp != _exph: _hh_ng.append(str(_wen) + ":" + str(_phw.hp) + "!=" + str(_exph))
check("天候別回復(1/2,2/3,1/4)厳密: こうごうせい", not _hh_ng, "NG=" + str(_hh_ng))

# ── クロスチョップ ──
check("DB: クロスチョップ 取得可能", dl.get_move("クロスチョップ") is not None)
_mv_クロスチョップ = dl.get_move("クロスチョップ")
if _mv_クロスチョップ:
    _pa_クロスチョップ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_クロスチョップ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_クロスチョップ = dmg(_pa_クロスチョップ, _pd_クロスチョップ, "クロスチョップ")
    check("ダメージ計算: クロスチョップ", _d_クロスチョップ > 0, f"dmg={_d_クロスチョップ}")
# クロスチョップ: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_クロスチョップ
random.seed(0); _hc_crit_クロスチョップ = 0; _phc = make_poke(type1="かくとう")
_mvhc_クロスチョップ = dl.get_move("クロスチョップ")
for _ in range(800):
    if _cc_クロスチョップ(_phc, _mvhc_クロスチョップ, make_poke(type1="ノーマル")): _hc_crit_クロスチョップ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: クロスチョップ", 60 <= _hc_crit_クロスチョップ <= 150, f"crit={_hc_crit_クロスチョップ}/800 (期待≈100, 通常1/24なら≈33)")

# ── つきのひかり ──
check("DB: つきのひかり 取得可能", dl.get_move("つきのひかり") is not None)
# つきのひかり: HP回復（最大HPの約1/2・無天候）
_mv_hp_つきのひかり = dl.get_move("つきのひかり")
if _mv_hp_つきのひかり:
    _pa_hp = make_poke(type1="フェアリー", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "つきのひかり")
    _exp_hp_つきのひかり = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): つきのひかり", abs(_pa_hp.hp - (1 + _exp_hp_つきのひかり)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_つきのひかり}")
# つきのひかり: 天候別回復を厳密検証 無天候=1/2・晴れ=2/3・悪天候(雨/砂/あられ)=1/4
_hh_ng = []
for _wen, _expfn in [(None, lambda m: m//2), ("sunny", lambda m: m*2//3), ("rain", lambda m: m//4), ("sandstorm", lambda m: m//4)]:
    _phw = make_poke(hp_b=200); _phw.hp = 1; _mhw = _phw.max_hp
    _fwh = BattleField()
    if _wen: _fwh.weather = _wen
    _execute_move(BattleSide([_phw]), BattleSide([make_poke()]), Action(type="move", move=dl.get_move("つきのひかり")), _fwh)
    _exph = min(_mhw, 1 + _expfn(_mhw))
    if _phw.hp != _exph: _hh_ng.append(str(_wen) + ":" + str(_phw.hp) + "!=" + str(_exph))
check("天候別回復(1/2,2/3,1/4)厳密: つきのひかり", not _hh_ng, "NG=" + str(_hh_ng))

# ── あまごい ──
check("DB: あまごい 取得可能", dl.get_move("あまごい") is not None)
# あまごい: 天候rain
_mv_w_あまごい = dl.get_move("あまごい")
if _mv_w_あまごい:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="みず"), make_poke(), "あまごい")
    check("天候rain: あまごい", _fw.weather == "rain", f"weather={_fw.weather}")

# ── かみくだく ──
check("DB: かみくだく 取得可能", dl.get_move("かみくだく") is not None)
_mv_かみくだく = dl.get_move("かみくだく")
if _mv_かみくだく:
    _pa_かみくだく = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_かみくだく = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_かみくだく = dmg(_pa_かみくだく, _pd_かみくだく, "かみくだく")
    check("ダメージ計算: かみくだく", _d_かみくだく > 0, f"dmg={_d_かみくだく}")
# かみくだく: 相手防御-1
_mv_dd_かみくだく = dl.get_move("かみくだく")
if _mv_dd_かみくだく:
    _pa_dd = make_poke(type1="あく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_かみくだく = 0; _dd_ok_かみくだく = False
    for _ in range(60):
        _pd_dd = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "かみくだく")
        if _pd_dd.stage_defense != 0: _dd_val_かみくだく = _pd_dd.stage_defense; _dd_ok_かみくだく = True; break
    check("相手防御-1: かみくだく", _dd_ok_かみくだく and _dd_val_かみくだく == -1, f"1回適用={_dd_val_かみくだく} 期待=-1")

# ── ミラーコート ──
check("DB: ミラーコート 取得可能", dl.get_move("ミラーコート") is not None)
# ミラーコート: 優先度-5
_mv_pr_ミラ_コ_ト = dl.get_move("ミラーコート")
if _mv_pr_ミラ_コ_ト and _mv_pr_ミラ_コ_ト.priority == -5:
    check("優先度-5: ミラーコート", _mv_pr_ミラ_コ_ト.priority == -5)
elif _mv_pr_ミラ_コ_ト:
    check("優先度-5: ミラーコート", _mv_pr_ミラ_コ_ト.priority == -5, f"DB優先度={_mv_pr_ミラ_コ_ト.priority} 仕様=-5")
# ミラーコート: カウンター反射（特殊技×2.0）
_mvcnt_ミラ_コ_ト = dl.get_move("ミラーコート")
if _mvcnt_ミラ_コ_ト:
    _pac_cnt = make_poke(type1="エスパー", atk_b=100, spatk_b=100, hp_b=200)
    _pdc_cnt = make_poke(type1="ノーマル" if "エスパー"!="かくとう" else "エスパー", hp_b=255, def_b=100, spdef_b=100)
    _pac_cnt._last_special_dmg_received = 100
    _exp_cnt = int(100 * 2.0)
    _hpc0 = _pdc_cnt.hp; execute(_pac_cnt, _pdc_cnt, "ミラーコート")
    check("カウンター反射: ミラーコート", _hpc0 - _pdc_cnt.hp == _exp_cnt, f"返し={_hpc0 - _pdc_cnt.hp} 期待={_exp_cnt}")
    _pac_cnt2 = make_poke(type1="エスパー", atk_b=100, spatk_b=100); _pdc_cnt2 = make_poke(type1="ノーマル", hp_b=255)
    _hpc20 = _pdc_cnt2.hp; execute(_pac_cnt2, _pdc_cnt2, "ミラーコート")
    check("カウンター被ダメ0で失敗: ミラーコート", _pdc_cnt2.hp == _hpc20)
# ミラーコート: 特殊被ダメの2倍を返す。実戦で特殊技を受けてから使うintegration
_pmc = make_poke(type1="エスパー", hp_b=255, spdef_b=60)
_atk_spec = make_poke(type1="エスパー", spatk_b=100, hp_b=255)
_execute_move(BattleSide([_atk_spec]), BattleSide([_pmc]), Action(type="move", move=dl.get_move("サイコキネシス")), BattleField())
_spec_received = _pmc._last_special_dmg_received
_dmc = make_poke(type1="ノーマル", hp_b=255, def_b=50); _hpm0 = _dmc.hp
execute(_pmc, _dmc, "ミラーコート")
check("特殊被ダメ×2返却(実戦): ミラーコート", _spec_received > 0 and _hpm0 - _dmc.hp == _spec_received * 2, f"received={_spec_received} returned={_hpm0 - _dmc.hp}")
# 被ダメなしは失敗
_pmc2 = make_poke(type1="エスパー"); _dmc2 = make_poke(type1="ノーマル", hp_b=255); _hpm2 = _dmc2.hp
execute(_pmc2, _dmc2, "ミラーコート")
check("被ダメ0で失敗: ミラーコート", _dmc2.hp == _hpm2)
# 物理技を受けただけでは反射しない（特殊のみ反応）
_pmc3 = make_poke(type1="エスパー", hp_b=255); _pmc3._last_physical_dmg_received = 100; _pmc3._last_special_dmg_received = 0
_dmc3 = make_poke(type1="ノーマル", hp_b=255); _hpm3 = _dmc3.hp
execute(_pmc3, _dmc3, "ミラーコート")
check("物理被弾では反射しない: ミラーコート", _dmc3.hp == _hpm3, f"hp={_dmc3.hp}/{_hpm3}")

# ── しんそく ──
check("DB: しんそく 取得可能", dl.get_move("しんそく") is not None)
_mv_しんそく = dl.get_move("しんそく")
if _mv_しんそく:
    _pa_しんそく = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_しんそく = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_しんそく = dmg(_pa_しんそく, _pd_しんそく, "しんそく")
    check("ダメージ計算: しんそく", _d_しんそく > 0, f"dmg={_d_しんそく}")
# しんそく: 優先度2
_mv_pr_しんそく = dl.get_move("しんそく")
if _mv_pr_しんそく and _mv_pr_しんそく.priority == 2:
    check("優先度2: しんそく", _mv_pr_しんそく.priority == 2)
elif _mv_pr_しんそく:
    check("優先度2: しんそく", _mv_pr_しんそく.priority == 2, f"DB優先度={_mv_pr_しんそく.priority} 仕様=2")

# ── げんしのちから ──
check("DB: げんしのちから 取得可能", dl.get_move("げんしのちから") is not None)
_mv_げんしのちから = dl.get_move("げんしのちから")
if _mv_げんしのちから:
    _pa_げんしのちから = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_げんしのちから = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_げんしのちから = dmg(_pa_げんしのちから, _pd_げんしのちから, "げんしのちから")
    check("ダメージ計算: げんしのちから", _d_げんしのちから > 0, f"dmg={_d_げんしのちから}")
# げんしのちから: 確率自己攻撃+1(10%)
_mvpb_げんしのちから = dl.get_move("げんしのちから")
if _mvpb_げんしのちから:
    random.seed(0); _pb_ok_げんしのちから = False
    for _ in range(200):
        _papb = make_poke(type1="いわ", atk_b=40, spatk_b=40); _pdpb = make_poke(type1="ひこう", hp_b=255, def_b=255, spdef_b=255)
        execute(_papb, _pdpb, "げんしのちから")
        if _papb.stage_attack > 0: _pb_ok_げんしのちから = _papb.stage_attack; break
    check("確率自己攻撃+1: げんしのちから", _pb_ok_げんしのちから == 1, f"1回適用={_pb_ok_げんしのちから} 期待=+1")

# ── シャドーボール ──
check("DB: シャドーボール 取得可能", dl.get_move("シャドーボール") is not None)
_mv_シャド_ボ_ル = dl.get_move("シャドーボール")
if _mv_シャド_ボ_ル:
    _pa_シャド_ボ_ル = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_シャド_ボ_ル = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_シャド_ボ_ル = dmg(_pa_シャド_ボ_ル, _pd_シャド_ボ_ル, "シャドーボール")
    check("ダメージ計算: シャドーボール", _d_シャド_ボ_ル > 0, f"dmg={_d_シャド_ボ_ル}")
# シャドーボール: 相手特防-1
_mv_dd_シャド_ボ_ル = dl.get_move("シャドーボール")
if _mv_dd_シャド_ボ_ル:
    _pa_dd = make_poke(type1="ゴースト", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_シャド_ボ_ル = 0; _dd_ok_シャド_ボ_ル = False
    for _ in range(60):
        _pd_dd = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "シャドーボール")
        if _pd_dd.stage_sp_defense != 0: _dd_val_シャド_ボ_ル = _pd_dd.stage_sp_defense; _dd_ok_シャド_ボ_ル = True; break
    check("相手特防-1: シャドーボール", _dd_ok_シャド_ボ_ル and _dd_val_シャド_ボ_ル == -1, f"1回適用={_dd_val_シャド_ボ_ル} 期待=-1")

# ── うずしお ──
check("DB: うずしお 取得可能", dl.get_move("うずしお") is not None)
_mv_うずしお = dl.get_move("うずしお")
if _mv_うずしお:
    _pa_うずしお = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_うずしお = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_うずしお = dmg(_pa_うずしお, _pd_うずしお, "うずしお")
    check("ダメージ計算: うずしお", _d_うずしお > 0, f"dmg={_d_うずしお}")
# うずしお: バインド
_mv_bd_うずしお = dl.get_move("うずしお")
if _mv_bd_うずしお:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="みず", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="ほのお", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "うずしお")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: うずしお", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")
# うずしお: 水中(ダイビング溜め中)の相手に2倍
_pwv = make_poke(type1="みず", spatk_b=100, atk_b=100); _dwv = make_poke(type1="ノーマル", spdef_b=100, def_b=100)
_n0 = _ep(_pwv, _dwv, dl.get_move("うずしお"), BattleField())
_dwv.charging_move = "ダイビング"; _n1 = _ep(_pwv, _dwv, dl.get_move("うずしお"), BattleField())
check("うずしお 水中2倍: うずしお", _n1 == _n0 * 2, f"normal={_n0} dive={_n1}")

# ── ねこだまし ──
check("DB: ねこだまし 取得可能", dl.get_move("ねこだまし") is not None)
_mv_ねこだまし = dl.get_move("ねこだまし")
if _mv_ねこだまし:
    _pa_ねこだまし = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ねこだまし = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ねこだまし = dmg(_pa_ねこだまし, _pd_ねこだまし, "ねこだまし")
    check("ダメージ計算: ねこだまし", _d_ねこだまし > 0, f"dmg={_d_ねこだまし}")
# ねこだまし: ひるみ(確定)
_mv_f100_ねこだまし = dl.get_move("ねこだまし")
if _mv_f100_ねこだまし:
    random.seed(0); _f100 = False
    for _ in range(20):
        _pa100 = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pd100 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa100, _pd100, "ねこだまし")
        if _pd100.flinched: _f100 = True; break
    check("ひるみ(確定): ねこだまし", _f100)
# ねこだまし: 優先度3
_mv_pr_ねこだまし = dl.get_move("ねこだまし")
if _mv_pr_ねこだまし and _mv_pr_ねこだまし.priority == 3:
    check("優先度3: ねこだまし", _mv_pr_ねこだまし.priority == 3)
elif _mv_pr_ねこだまし:
    check("優先度3: ねこだまし", _mv_pr_ねこだまし.priority == 3, f"DB優先度={_mv_pr_ねこだまし.priority} 仕様=3")
# ねこだまし: 100%ひるみ
random.seed(0); _pnk = make_poke(type1="ノーマル", atk_b=30); _dnk = make_poke(type1="ノーマル", def_b=255, hp_b=255)
execute(_pnk, _dnk, "ねこだまし")
check("ねこだまし ひるみ: ねこだまし", _dnk.flinched)
# 場に出て最初のターンのみ成功（turns_out>0は失敗）
_pnk_l = make_poke(type1="ノーマル", atk_b=120); _dnk_l = make_poke(type1="ノーマル", hp_b=255, def_b=150)
_pnk_l.turns_out = 1; _hpnk_l = _dnk_l.hp; execute(_pnk_l, _dnk_l, "ねこだまし")
check("初手以外で失敗: ねこだまし", _dnk_l.hp == _hpnk_l, f"hp={_dnk_l.hp}/{_hpnk_l}")
_pnk_f = make_poke(type1="ノーマル", atk_b=120); _dnk_f = make_poke(type1="ノーマル", hp_b=255, def_b=150)
_pnk_f.turns_out = 0; _hpnk_f = _dnk_f.hp; execute(_pnk_f, _dnk_f, "ねこだまし")
check("初手で成功: ねこだまし", _dnk_f.hp < _hpnk_f, f"hp={_dnk_f.hp}/{_hpnk_f}")

# ── ねっぷう ──
check("DB: ねっぷう 取得可能", dl.get_move("ねっぷう") is not None)
_mv_ねっぷう = dl.get_move("ねっぷう")
if _mv_ねっぷう:
    _pa_ねっぷう = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ねっぷう = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ねっぷう = dmg(_pa_ねっぷう, _pd_ねっぷう, "ねっぷう")
    check("ダメージ計算: ねっぷう", _d_ねっぷう > 0, f"dmg={_d_ねっぷう}")
# ねっぷう: やけど10%
_mv_s_ねっぷう = dl.get_move("ねっぷう")
if _mv_s_ねっぷう:
    random.seed(0); _hit_ねっぷう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ねっぷう")
        _hit_ねっぷう += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): ねっぷう", 9 <= _hit_ねっぷう <= 66, f"count={_hit_ねっぷう}/300")
    random.seed(1); _immok_ねっぷう = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ねっぷう")
        if _pdi.status == "burn": _immok_ねっぷう = False; break
    check("やけど免疫(ほのお型には無効): ねっぷう", _immok_ねっぷう, "免疫タイプに状態異常が付与されないこと")

# ── おきみやげ ──
check("DB: おきみやげ 取得可能", dl.get_move("おきみやげ") is not None)
# おきみやげ: 自己ひんし
_mvsf_おきみやげ = dl.get_move("おきみやげ")
if _mvsf_おきみやげ:
    _pasf = make_poke(type1="あく", atk_b=100, spatk_b=100); _pdsf = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
    execute(_pasf, _pdsf, "おきみやげ")
    check("自己ひんし: おきみやげ", not _pasf.is_alive)
# おきみやげ: 自己ひんし + 相手の攻撃・特攻を2段階下げる
_posf = make_poke(type1="あく"); _dosf = make_poke(type1="エスパー", hp_b=255)
execute(_posf, _dosf, "おきみやげ")
check("自己ひんし: おきみやげ", not _posf.is_alive)
check("相手攻撃-2: おきみやげ", _dosf.stage_attack == -2, f"atk={_dosf.stage_attack} 期待=-2")
check("相手特攻-2: おきみやげ", _dosf.stage_sp_attack == -2, f"spa={_dosf.stage_sp_attack} 期待=-2")

# ── おにび ──
check("DB: おにび 取得可能", dl.get_move("おにび") is not None)
# おにび: やけど付与(変化技)
_mv_si_おにび = dl.get_move("おにび")
if _mv_si_おにび:
    random.seed(0); _ok_おにび = False
    for _ in range(30):
        _pa_si = make_poke(type1="ほのお"); _pd_si = make_poke(type1="くさ", hp_b=255)
        execute(_pa_si, _pd_si, "おにび")
        if _pd_si.status == "burn": _ok_おにび = True; break
    check("やけど付与: おにび", _ok_おにび)
    random.seed(2); _siimm_おにび = True
    for _ in range(40):
        _pai2 = make_poke(type1="ほのお"); _pdi2 = make_poke(type1="ほのお", hp_b=255)
        execute(_pai2, _pdi2, "おにび")
        if _pdi2.status == "burn": _siimm_おにび = False; break
    check("やけど免疫(ほのお型には無効): おにび", _siimm_おにび, "免疫タイプに付与されないこと")

# ── からげんき ──
check("DB: からげんき 取得可能", dl.get_move("からげんき") is not None)
_mv_からげんき = dl.get_move("からげんき")
if _mv_からげんき:
    _pa_からげんき = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_からげんき = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_からげんき = dmg(_pa_からげんき, _pd_からげんき, "からげんき")
    check("ダメージ計算: からげんき", _d_からげんき > 0, f"dmg={_d_からげんき}")
# からげんき: 状態異常時に威力2倍（等値検証）
_pk = make_poke(type1="ノーマル", atk_b=120); _dk = make_poke(type1="いわ", def_b=120, hp_b=255)
_kn = calc_damage(_pk, _dk, dl.get_move("からげんき"), BattleField(), random_roll=1.0)
_pk.status = "paralysis"; _ks = calc_damage(_pk, _dk, dl.get_move("からげんき"), BattleField(), random_roll=1.0)
check("状態異常で2倍: からげんき", abs(_ks - _kn * 2) <= 1, f"n={_kn} s={_ks} expected={_kn*2}")
# やけど状態でも攻撃半減を受けない（やけど状態のダメージ≈通常状態の2倍）
_pk_burn = make_poke(type1="ノーマル", atk_b=120); _dk2 = make_poke(type1="いわ", def_b=120, hp_b=255)
_pk_burn.status = "burn"
_k_burn = calc_damage(_pk_burn, _dk2, dl.get_move("からげんき"), BattleField(), random_roll=1.0)
check("やけど攻撃半減無視: からげんき", abs(_k_burn - _kn * 2) <= 1, f"burn={_k_burn} normal={_kn} expected={_kn*2}")

# ── じゅうでん ──
check("DB: じゅうでん 取得可能", dl.get_move("じゅうでん") is not None)
# じゅうでん: 自分特防+1
_mv_sb_じゅうでん_sp_defense = dl.get_move("じゅうでん")
if _mv_sb_じゅうでん_sp_defense:
    _pa_sb = make_poke(type1="でんき"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "じゅうでん")
    check("自分特防+1: じゅうでん", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")
# じゅうでん: 自分特防+1
_mvss_じゅうでん_sp_defense = dl.get_move("じゅうでん")
if _mvss_じゅうでん_sp_defense:
    random.seed(0); _got_じゅうでん_sp_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="でんき", atk_b=60, spatk_b=60); _pds = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "じゅうでん")
        if _pas.stage_sp_defense != 0: _got_じゅうでん_sp_defense = _pas.stage_sp_defense; break
    check("自分特防+1: じゅうでん", _got_じゅうでん_sp_defense == 1, f"1回適用={_got_じゅうでん_sp_defense} 期待=1")
# じゅうでん: 使用するとcharged状態になる（条件成立を検証）
_pjd_t = make_poke(type1="でんき"); execute(_pjd_t, make_poke(), "じゅうでん")
check("じゅうでんでcharged成立: じゅうでん", _pjd_t.charged, f"charged={_pjd_t.charged}")
# charged状態だと次のでんき技の威力が2倍
_pjd = make_poke(type1="でんき", spatk_b=120); _djd = make_poke(type1="ノーマル", spdef_b=100)
_djd2 = make_poke(type1="ノーマル", spdef_b=100)
_jd_base = calc_damage(_pjd, _djd, dl.get_move("10まんボルト"), BattleField(), random_roll=1.0)
_pjd.charged = True; _jd_chg = calc_damage(_pjd, _djd2, dl.get_move("10まんボルト"), BattleField(), random_roll=1.0)
check("じゅうでん次でんき2倍: じゅうでん", abs(_jd_chg - _jd_base * 2) <= 2, f"base={_jd_base} chg={_jd_chg}")

# ── ちょうはつ ──
check("DB: ちょうはつ 取得可能", dl.get_move("ちょうはつ") is not None)
# ちょうはつ: 相手をちょうはつ状態に
_pt2 = make_poke(); _dt2 = make_poke(); execute(_pt2, _dt2, "ちょうはつ")
check("ちょうはつ付与: ちょうはつ", _dt2.taunt_count > 0)

# ── トリック ──
check("DB: トリック 取得可能", dl.get_move("トリック") is not None)
# トリック: 道具交換（メガストーンは失敗）
_ptrk = make_poke(type1="エスパー", item="こだわりスカーフ"); _dtrk = make_poke(type1="ノーマル", item="オボンのみ")
execute(_ptrk, _dtrk, "トリック")
check("道具入替: トリック", _ptrk.item == "オボンのみ" and _dtrk.item == "こだわりスカーフ", f"atk={_ptrk.item} def={_dtrk.item}")
# 相手がメガストーンを持つ場合は失敗
_ptrk2 = make_poke(type1="エスパー", item="こだわりスカーフ"); _dtrk2 = make_poke(type1="ノーマル", item="ガブリアスナイト")
execute(_ptrk2, _dtrk2, "トリック")
check("メガストーン交換失敗: トリック", _ptrk2.item == "こだわりスカーフ" and _dtrk2.item == "ガブリアスナイト", f"atk={_ptrk2.item} def={_dtrk2.item}")

# ── ねがいごと ──
check("DB: ねがいごと 取得可能", dl.get_move("ねがいごと") is not None)
# ねがいごと: 2ターン後に自分側の場のポケモンを回復
from simulator.battle import Battle as _Bwi
_pwi = make_poke(type1="ノーマル", hp_b=200); _pwi.hp = 30
_s1w, _, _ = execute_ctx(_pwi, make_poke(), "ねがいごと")
check("ねがいごと予約: ねがいごと", _s1w.wish_count > 0)
_bwi = _Bwi(_s1w, BattleSide([make_poke()])); _hpw0 = _pwi.hp
_bwi._end_of_turn(); _mid_w = _pwi.hp; _bwi._end_of_turn()
check("ねがいごと回復: ねがいごと", _mid_w == _hpw0 and _pwi.hp > _hpw0, f"mid={_mid_w} end={_pwi.hp}/{_hpw0}")

# ── ばかぢから ──
check("DB: ばかぢから 取得可能", dl.get_move("ばかぢから") is not None)
_mv_ばかぢから = dl.get_move("ばかぢから")
if _mv_ばかぢから:
    _pa_ばかぢから = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ばかぢから = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ばかぢから = dmg(_pa_ばかぢから, _pd_ばかぢから, "ばかぢから")
    check("ダメージ計算: ばかぢから", _d_ばかぢから > 0, f"dmg={_d_ばかぢから}")
# ばかぢから: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="かくとう", atk_b=120, spatk_b=120); _dsd = make_poke(type1="ノーマル", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "ばかぢから")
    if _psd.stage_attack < 0: break
check("自分攻撃下降: ばかぢから", _psd.stage_attack < 0, f"stage={_psd.stage_attack}")
check("自分防御下降: ばかぢから", _psd.stage_defense < 0, f"stage={_psd.stage_defense}")

# ── リサイクル ──
check("DB: リサイクル 取得可能", dl.get_move("リサイクル") is not None)
# リサイクル: 消費道具を復元
_prc = make_poke(); _prc.item = None; _prc._last_consumed_item = "オボンのみ"
execute(_prc, make_poke(), "リサイクル")
check("リサイクル 道具復元: リサイクル", _prc.item == "オボンのみ")

# ── あくび ──
check("DB: あくび 取得可能", dl.get_move("あくび") is not None)
# あくび: ねむけ付与(yawn_count)
_pda = make_poke(); execute(make_poke(), _pda, "あくび")
check("ねむけ付与: あくび", _pda.yawn_count == 2, f"yawn={_pda.yawn_count}")

# ── かわらわり ──
check("DB: かわらわり 取得可能", dl.get_move("かわらわり") is not None)
_mv_かわらわり = dl.get_move("かわらわり")
if _mv_かわらわり:
    _pa_かわらわり = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_かわらわり = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_かわらわり = dmg(_pa_かわらわり, _pd_かわらわり, "かわらわり")
    check("ダメージ計算: かわらわり", _d_かわらわり > 0, f"dmg={_d_かわらわり}")
# かわらわり: スクリーン破壊
_mvbrk_かわらわり = dl.get_move("かわらわり")
if _mvbrk_かわらわり:
    random.seed(0); _brk_ok = False
    for _ in range(20):
        _pabrk = make_poke(type1="かくとう", atk_b=120, spatk_b=120); _pdbrk = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
        _s1b = BattleSide([_pabrk]); _s2b = BattleSide([_pdbrk])
        _s2b.reflect = True; _s2b.reflect_count = 5; _s2b.light_screen = True; _s2b.light_screen_count = 5
        _execute_move(_s1b, _s2b, Action(type="move", move=_mvbrk_かわらわり), BattleField())
        if not _s2b.reflect and not _s2b.light_screen: _brk_ok = True; break
    check("スクリーン破壊: かわらわり", _brk_ok)
# かわらわり: スクリーンを無視してダメージ（スクリーン有り≈無しと同等）、かつスクリーンを破壊する
_pakw = make_poke(type1="かくとう", atk_b=150)
# 同じシードで実行してランダムロールを揃える
random.seed(77); _dkw_no = make_poke(type1="ノーマル", def_b=80, hp_b=255)
_execute_move(BattleSide([_pakw]), BattleSide([_dkw_no]), Action(type="move", move=dl.get_move("かわらわり")), BattleField())
_dmg_no_scr = _dkw_no.max_hp - _dkw_no.hp
random.seed(77); _dkw_ref = make_poke(type1="ノーマル", def_b=80, hp_b=255)
_s2_ref = BattleSide([_dkw_ref]); _s2_ref.reflect = True; _s2_ref.reflect_count = 5
_execute_move(BattleSide([_pakw]), _s2_ref, Action(type="move", move=dl.get_move("かわらわり")), BattleField())
_dmg_with_scr = _dkw_ref.max_hp - _dkw_ref.hp
check("スクリーン無視(等ダメ): かわらわり", _dmg_no_scr == _dmg_with_scr, f"no_screen={_dmg_no_scr} with_screen={_dmg_with_scr}")
check("スクリーン破壊: かわらわり", not _s2_ref.reflect, f"reflect={_s2_ref.reflect}")

# ── はたきおとす ──
check("DB: はたきおとす 取得可能", dl.get_move("はたきおとす") is not None)
_mv_はたきおとす = dl.get_move("はたきおとす")
if _mv_はたきおとす:
    _pa_はたきおとす = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_はたきおとす = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_はたきおとす = dmg(_pa_はたきおとす, _pd_はたきおとす, "はたきおとす")
    check("ダメージ計算: はたきおとす", _d_はたきおとす > 0, f"dmg={_d_はたきおとす}")
# はたきおとす: 道具持ちに1.5倍+道具排除
_pko = make_poke(type1="あく", atk_b=100)
_dko_item = make_poke(type1="ノーマル", def_b=100); _dko_item.item = "たべのこし"
_dko_none = make_poke(type1="ノーマル", def_b=100)
_d_item = calc_damage(_pko, _dko_item, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)
_d_none = calc_damage(_pko, _dko_none, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)
check("はたきおとす 道具持ち1.5倍: はたきおとす", _d_item > _d_none, f"item={_d_item} none={_d_none}")
# 威力1.5倍の具体値（65→97）
_pkx = make_poke(type1="あく", atk_b=100); _dkx = make_poke(type1="ノーマル", def_b=100); _dkx.item = None
_ko_base = _ep(_pkx, _dkx, dl.get_move("はたきおとす"), BattleField())
_dkx.item = "オボンのみ"; _ko_item = _ep(_pkx, _dkx, dl.get_move("はたきおとす"), BattleField())
check("道具なし威力65: はたきおとす", _ko_base == 65, f"base={_ko_base}")
check("道具持ち1.5倍具体値(97): はたきおとす", _ko_item == 97, f"item={_ko_item}")
execute(_pko, _dko_item, "はたきおとす")
check("はたきおとす 道具排除: はたきおとす", _dko_item.item is None)
# メガストーンは叩き落とせない＋1.5倍補正もない
_dko_mega = make_poke(type1="ノーマル", def_b=100, item="ガブリアスナイト")
_dko_mega_nodmg = make_poke(type1="ノーマル", def_b=100)  # アイテムなし（基準）
_d_mega = calc_damage(_pko, _dko_mega, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)
_d_mega_base = calc_damage(_pko, _dko_mega_nodmg, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)
execute(_pko, _dko_mega, "はたきおとす")
check("メガストーン消去失敗: はたきおとす", _dko_mega.item == "ガブリアスナイト", f"item={_dko_mega.item}")
check("メガストーン時1.5倍補正なし: はたきおとす", _d_mega == _d_mega_base, f"mega={_d_mega} base={_d_mega_base}")

# ── がむしゃら ──
check("DB: がむしゃら 取得可能", dl.get_move("がむしゃら") is not None)
# がむしゃら: 相手HPを自分HPに揃える。相手HP≦自分HPなら失敗(無傷)
_pgm = make_poke(type1="ノーマル", atk_b=1); _pgm.hp = _pgm.max_hp
_dgm = make_poke(type1="でんき", hp_b=120, def_b=255); _dgm.hp = 10
execute(_pgm, _dgm, "がむしゃら")
check("相手HP以下で失敗: がむしゃら", _dgm.hp == 10, f"hp={_dgm.hp}")
_pgm2 = make_poke(type1="ノーマル", atk_b=1); _pgm2.hp = 20
_dgm2 = make_poke(type1="でんき", hp_b=200, def_b=255)
execute(_pgm2, _dgm2, "がむしゃら")
check("HP揃え(可変ダメージ): がむしゃら", _dgm2.hp == 20, f"hp={_dgm2.hp}")

# ── ふんか ──
check("DB: ふんか 取得可能", dl.get_move("ふんか") is not None)
_mv_ふんか = dl.get_move("ふんか")
if _mv_ふんか:
    _pa_ふんか = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ふんか = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ふんか = dmg(_pa_ふんか, _pd_ふんか, "ふんか")
    check("ダメージ計算: ふんか", _d_ふんか > 0, f"dmg={_d_ふんか}")
# ふんか: 威力=floor(150×現HP/最大HP)。満タン150、半分75
_ph = make_poke(type1="ほのお", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="くさ")
import math as _mfk
_fk_ng = []
for _r in [1.0, 0.5, 0.25]:
    _ph.hp = max(1, int(_ph.max_hp * _r)); _exp = max(1, _mfk.floor(150 * _ph.hp / _ph.max_hp))
    _got = _ep(_ph, _dd, dl.get_move("ふんか"), BattleField())
    if _got != _exp: _fk_ng.append(f"r={_r}:{_got}!={_exp}")
check("HP比威力(150×HP/max): ふんか", not _fk_ng, f"NG={_fk_ng}")

# ── ふういん ──
check("DB: ふういん 取得可能", dl.get_move("ふういん") is not None)
# ふういん: 自分がふういん状態に
_pf = make_poke(); execute(_pf, make_poke(), "ふういん")
check("ふういん付与: ふういん", getattr(_pf, "_sealed", False))

# ── フェザーダンス ──
check("DB: フェザーダンス 取得可能", dl.get_move("フェザーダンス") is not None)
# フェザーダンス: 相手攻撃-2
_mv_dd_フェザ_ダンス = dl.get_move("フェザーダンス")
if _mv_dd_フェザ_ダンス:
    _pa_dd = make_poke(type1="ひこう", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_フェザ_ダンス = 0; _dd_ok_フェザ_ダンス = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "フェザーダンス")
        if _pd_dd.stage_attack != 0: _dd_val_フェザ_ダンス = _pd_dd.stage_attack; _dd_ok_フェザ_ダンス = True; break
    check("相手攻撃-2: フェザーダンス", _dd_ok_フェザ_ダンス and _dd_val_フェザ_ダンス == -2, f"1回適用={_dd_val_フェザ_ダンス} 期待=-2")

# ── ブレイズキック ──
check("DB: ブレイズキック 取得可能", dl.get_move("ブレイズキック") is not None)
_mv_ブレイズキック = dl.get_move("ブレイズキック")
if _mv_ブレイズキック:
    _pa_ブレイズキック = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ブレイズキック = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ブレイズキック = dmg(_pa_ブレイズキック, _pd_ブレイズキック, "ブレイズキック")
    check("ダメージ計算: ブレイズキック", _d_ブレイズキック > 0, f"dmg={_d_ブレイズキック}")
# ブレイズキック: やけど10%
_mv_s_ブレイズキック = dl.get_move("ブレイズキック")
if _mv_s_ブレイズキック:
    random.seed(0); _hit_ブレイズキック = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ブレイズキック")
        _hit_ブレイズキック += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): ブレイズキック", 9 <= _hit_ブレイズキック <= 66, f"count={_hit_ブレイズキック}/300")
    random.seed(1); _immok_ブレイズキック = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ブレイズキック")
        if _pdi.status == "burn": _immok_ブレイズキック = False; break
    check("やけど免疫(ほのお型には無効): ブレイズキック", _immok_ブレイズキック, "免疫タイプに状態異常が付与されないこと")
# ブレイズキック: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_ブレイズキック
random.seed(0); _hc_crit_ブレイズキック = 0; _phc = make_poke(type1="ほのお")
_mvhc_ブレイズキック = dl.get_move("ブレイズキック")
for _ in range(800):
    if _cc_ブレイズキック(_phc, _mvhc_ブレイズキック, make_poke(type1="くさ")): _hc_crit_ブレイズキック += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: ブレイズキック", 60 <= _hc_crit_ブレイズキック <= 150, f"crit={_hc_crit_ブレイズキック}/800 (期待≈100, 通常1/24なら≈33)")

# ── ハイパーボイス ──
check("DB: ハイパーボイス 取得可能", dl.get_move("ハイパーボイス") is not None)
_mv_ハイパ_ボイス = dl.get_move("ハイパーボイス")
if _mv_ハイパ_ボイス:
    _pa_ハイパ_ボイス = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ハイパ_ボイス = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ハイパ_ボイス = dmg(_pa_ハイパ_ボイス, _pd_ハイパ_ボイス, "ハイパーボイス")
    check("ダメージ計算: ハイパーボイス", _d_ハイパ_ボイス > 0, f"dmg={_d_ハイパ_ボイス}")

# ── なまける ──
check("DB: なまける 取得可能", dl.get_move("なまける") is not None)
# なまける: HP回復（最大HPの約1/2・無天候）
_mv_hp_なまける = dl.get_move("なまける")
if _mv_hp_なまける:
    _pa_hp = make_poke(type1="ノーマル", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "なまける")
    _exp_hp_なまける = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): なまける", abs(_pa_hp.hp - (1 + _exp_hp_なまける)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_なまける}")

# ── コメットパンチ ──
check("DB: コメットパンチ 取得可能", dl.get_move("コメットパンチ") is not None)
_mv_コメットパンチ = dl.get_move("コメットパンチ")
if _mv_コメットパンチ:
    _pa_コメットパンチ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_コメットパンチ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_コメットパンチ = dmg(_pa_コメットパンチ, _pd_コメットパンチ, "コメットパンチ")
    check("ダメージ計算: コメットパンチ", _d_コメットパンチ > 0, f"dmg={_d_コメットパンチ}")
# コメットパンチ: 確率自己攻撃+1(20%)
_mvpb_コメットパンチ = dl.get_move("コメットパンチ")
if _mvpb_コメットパンチ:
    random.seed(0); _pb_ok_コメットパンチ = False
    for _ in range(200):
        _papb = make_poke(type1="はがね", atk_b=40, spatk_b=40); _pdpb = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_papb, _pdpb, "コメットパンチ")
        if _papb.stage_attack > 0: _pb_ok_コメットパンチ = _papb.stage_attack; break
    check("確率自己攻撃+1: コメットパンチ", _pb_ok_コメットパンチ == 1, f"1回適用={_pb_ok_コメットパンチ} 期待=+1")

# ── ウェザーボール ──
check("DB: ウェザーボール 取得可能", dl.get_move("ウェザーボール") is not None)
_mv_ウェザ_ボ_ル = dl.get_move("ウェザーボール")
if _mv_ウェザ_ボ_ル:
    _pa_ウェザ_ボ_ル = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ウェザ_ボ_ル = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ウェザ_ボ_ル = dmg(_pa_ウェザ_ボ_ル, _pd_ウェザ_ボ_ル, "ウェザーボール")
    check("ダメージ計算: ウェザーボール", _d_ウェザ_ボ_ル > 0, f"dmg={_d_ウェザ_ボ_ル}")
# ウェザーボール: 天候で威力2倍＆タイプ変化
_pwb = make_poke(type1="ノーマル", spatk_b=100); _dwb = make_poke(type1="ノーマル", spdef_b=100)
_pw_none = _ep(_pwb, _dwb, dl.get_move("ウェザーボール"), BattleField())
_fwb = BattleField(); _fwb.weather = "sunny"
_pw_sun = _ep(_pwb, _dwb, dl.get_move("ウェザーボール"), _fwb)
from simulator.damage import _effective_move_type as _emt2
_typ_sun = _emt2(_pwb, dl.get_move("ウェザーボール"), _fwb)
check("ウェザーボール 天候威力2倍: ウェザーボール", _pw_sun == _pw_none * 2, f"none={_pw_none} sun={_pw_sun}")
# 全天候→タイプの対応を網羅（晴れ:ほのお/雨:みず/あられ:こおり/砂:いわ）
_wb_ng = []
for _w, _ty in [("sunny","ほのお"),("rain","みず"),("hail","こおり"),("sandstorm","いわ"),(None,"ノーマル")]:
    _fwx = BattleField()
    if _w: _fwx.weather = _w
    _gt = _emt2(_pwb, dl.get_move("ウェザーボール"), _fwx)
    if _gt != _ty: _wb_ng.append(str(_w) + ":" + str(_gt) + "!=" + str(_ty))
check("ウェザーボール 全天候タイプ変化: ウェザーボール", not _wb_ng, "NG=" + str(_wb_ng))

# ── がんせきふうじ ──
check("DB: がんせきふうじ 取得可能", dl.get_move("がんせきふうじ") is not None)
_mv_がんせきふうじ = dl.get_move("がんせきふうじ")
if _mv_がんせきふうじ:
    _pa_がんせきふうじ = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_がんせきふうじ = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_がんせきふうじ = dmg(_pa_がんせきふうじ, _pd_がんせきふうじ, "がんせきふうじ")
    check("ダメージ計算: がんせきふうじ", _d_がんせきふうじ > 0, f"dmg={_d_がんせきふうじ}")
# がんせきふうじ: 相手素早さ-1
_mv_dd_がんせきふうじ = dl.get_move("がんせきふうじ")
if _mv_dd_がんせきふうじ:
    _pa_dd = make_poke(type1="いわ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_がんせきふうじ = 0; _dd_ok_がんせきふうじ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ひこう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "がんせきふうじ")
        if _pd_dd.stage_speed != 0: _dd_val_がんせきふうじ = _pd_dd.stage_speed; _dd_ok_がんせきふうじ = True; break
    check("相手素早さ-1: がんせきふうじ", _dd_ok_がんせきふうじ and _dd_val_がんせきふうじ == -1, f"1回適用={_dd_val_がんせきふうじ} 期待=-1")

# ── オーバーヒート ──
check("DB: オーバーヒート 取得可能", dl.get_move("オーバーヒート") is not None)
_mv_オ_バ_ヒ_ト = dl.get_move("オーバーヒート")
if _mv_オ_バ_ヒ_ト:
    _pa_オ_バ_ヒ_ト = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_オ_バ_ヒ_ト = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_オ_バ_ヒ_ト = dmg(_pa_オ_バ_ヒ_ト, _pd_オ_バ_ヒ_ト, "オーバーヒート")
    check("ダメージ計算: オーバーヒート", _d_オ_バ_ヒ_ト > 0, f"dmg={_d_オ_バ_ヒ_ト}")
# オーバーヒート: 自分特攻-2
_mvss_オ_バ_ヒ_ト_sp_attack = dl.get_move("オーバーヒート")
if _mvss_オ_バ_ヒ_ト_sp_attack:
    random.seed(0); _got_オ_バ_ヒ_ト_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="ほのお", atk_b=60, spatk_b=60); _pds = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "オーバーヒート")
        if _pas.stage_sp_attack != 0: _got_オ_バ_ヒ_ト_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻-2: オーバーヒート", _got_オ_バ_ヒ_ト_sp_attack == -2, f"1回適用={_got_オ_バ_ヒ_ト_sp_attack} 期待=-2")
# オーバーヒート: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="ほのお", atk_b=120, spatk_b=120); _dsd = make_poke(type1="くさ", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "オーバーヒート")
    if _psd.stage_sp_attack < 0: break
check("自分特攻下降: オーバーヒート", _psd.stage_sp_attack < 0, f"stage={_psd.stage_sp_attack}")

# ── コスモパワー ──
check("DB: コスモパワー 取得可能", dl.get_move("コスモパワー") is not None)
# コスモパワー: 自分防御+1
_mv_sb_コスモパワ__defense = dl.get_move("コスモパワー")
if _mv_sb_コスモパワ__defense:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "コスモパワー")
    check("自分防御+1: コスモパワー", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")
# コスモパワー: 自分特防+1
_mv_sb_コスモパワ__sp_defense = dl.get_move("コスモパワー")
if _mv_sb_コスモパワ__sp_defense:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "コスモパワー")
    check("自分特防+1: コスモパワー", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")

# ── しおふき ──
check("DB: しおふき 取得可能", dl.get_move("しおふき") is not None)
_mv_しおふき = dl.get_move("しおふき")
if _mv_しおふき:
    _pa_しおふき = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_しおふき = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_しおふき = dmg(_pa_しおふき, _pd_しおふき, "しおふき")
    check("ダメージ計算: しおふき", _d_しおふき > 0, f"dmg={_d_しおふき}")
# しおふき: 威力=floor(150×現HP/最大HP)。満タン150、半分75
_ph = make_poke(type1="みず", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="ほのお")
import math as _mfk
_fk_ng = []
for _r in [1.0, 0.5, 0.25]:
    _ph.hp = max(1, int(_ph.max_hp * _r)); _exp = max(1, _mfk.floor(150 * _ph.hp / _ph.max_hp))
    _got = _ep(_ph, _dd, dl.get_move("しおふき"), BattleField())
    if _got != _exp: _fk_ng.append(f"r={_r}:{_got}!={_exp}")
check("HP比威力(150×HP/max): しおふき", not _fk_ng, f"NG={_fk_ng}")

# ── じんつうりき ──
check("DB: じんつうりき 取得可能", dl.get_move("じんつうりき") is not None)
_mv_じんつうりき = dl.get_move("じんつうりき")
if _mv_じんつうりき:
    _pa_じんつうりき = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_じんつうりき = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_じんつうりき = dmg(_pa_じんつうりき, _pd_じんつうりき, "じんつうりき")
    check("ダメージ計算: じんつうりき", _d_じんつうりき > 0, f"dmg={_d_じんつうりき}")
# じんつうりき: ひるみ10%
_mv_f_じんつうりき = dl.get_move("じんつうりき")
if _mv_f_じんつうりき:
    random.seed(1); _fh_じんつうりき = 0
    for _ in range(300):
        _pa3 = make_poke(type1="エスパー", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="かくとう", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "じんつうりき"); _fh_じんつうりき += int(_pd3.flinched)
    check("ひるみ(10%): じんつうりき", 9 <= _fh_じんつうりき <= 66, f"count={_fh_じんつうりき}/300")

# ── ぜったいれいど ──
check("DB: ぜったいれいど 取得可能", dl.get_move("ぜったいれいど") is not None)
# ぜったいれいど: 一撃必殺
_mv_oh_ぜったいれいど = dl.get_move("ぜったいれいど")
if _mv_oh_ぜったいれいど:
    random.seed(0); _ko_ぜったいれいど = False
    for _ in range(60):
        _pa_oh = make_poke(type1="こおり"); _pd_oh = make_poke(type1="ノーマル", hp_b=200)
        execute(_pa_oh, _pd_oh, "ぜったいれいど")
        if not _pd_oh.is_alive: _ko_ぜったいれいど = True; break
    check("一撃必殺: ぜったいれいど", _ko_ぜったいれいど)

# ── タネマシンガン ──
check("DB: タネマシンガン 取得可能", dl.get_move("タネマシンガン") is not None)
_mv_タネマシンガン = dl.get_move("タネマシンガン")
if _mv_タネマシンガン:
    _pa_タネマシンガン = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_タネマシンガン = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_タネマシンガン = dmg(_pa_タネマシンガン, _pd_タネマシンガン, "タネマシンガン")
    check("ダメージ計算: タネマシンガン", _d_タネマシンガン > 0, f"dmg={_d_タネマシンガン}")
# タネマシンガン: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_タネマシンガン = dl.get_move("タネマシンガン")
if _mvmh_タネマシンガン:
    _pam = make_poke(type1="くさ", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_タネマシンガン = calc_damage(_pam, make_poke(type1="みず", hp_b=255, def_b=200, spdef_b=200), _mvmh_タネマシンガン, BattleField(), random_roll=1.0)
    random.seed(0); _multi_タネマシンガン = 0
    for _ in range(20):
        _pdm = make_poke(type1="みず", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "タネマシンガン"); _multi_タネマシンガン = _pdm.max_hp - _pdm.hp
        if _multi_タネマシンガン > _single_タネマシンガン: break
    check("多段ヒット発生(複数回): タネマシンガン", _multi_タネマシンガン > _single_タネマシンガン, f"single={_single_タネマシンガン} multi={_multi_タネマシンガン}")

# ── つららばり ──
check("DB: つららばり 取得可能", dl.get_move("つららばり") is not None)
_mv_つららばり = dl.get_move("つららばり")
if _mv_つららばり:
    _pa_つららばり = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_つららばり = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_つららばり = dmg(_pa_つららばり, _pd_つららばり, "つららばり")
    check("ダメージ計算: つららばり", _d_つららばり > 0, f"dmg={_d_つららばり}")
# つららばり: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_つららばり = dl.get_move("つららばり")
if _mvmh_つららばり:
    _pam = make_poke(type1="こおり", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_つららばり = calc_damage(_pam, make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200), _mvmh_つららばり, BattleField(), random_roll=1.0)
    random.seed(0); _multi_つららばり = 0
    for _ in range(20):
        _pdm = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "つららばり"); _multi_つららばり = _pdm.max_hp - _pdm.hp
        if _multi_つららばり > _single_つららばり: break
    check("多段ヒット発生(複数回): つららばり", _multi_つららばり > _single_つららばり, f"single={_single_つららばり} multi={_multi_つららばり}")

# ── つばめがえし ──
check("DB: つばめがえし 取得可能", dl.get_move("つばめがえし") is not None)
_mv_つばめがえし = dl.get_move("つばめがえし")
if _mv_つばめがえし:
    _pa_つばめがえし = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_つばめがえし = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_つばめがえし = dmg(_pa_つばめがえし, _pd_つばめがえし, "つばめがえし")
    check("ダメージ計算: つばめがえし", _d_つばめがえし > 0, f"dmg={_d_つばめがえし}")
# つばめがえし: 必中
_mvmust_つばめがえし = dl.get_move("つばめがえし")
if _mvmust_つばめがえし:
    random.seed(0); _hit_all_つばめがえし = True
    for _ in range(30):
        _pah = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pdh = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "つばめがえし")
        if _pdh.hp == _hpb: _hit_all_つばめがえし = False; break
    check("必中: つばめがえし", _hit_all_つばめがえし)

# ── てっぺき ──
check("DB: てっぺき 取得可能", dl.get_move("てっぺき") is not None)
# てっぺき: 自分防御+2
_mv_sb_てっぺき_defense = dl.get_move("てっぺき")
if _mv_sb_てっぺき_defense:
    _pa_sb = make_poke(type1="はがね"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "てっぺき")
    check("自分防御+2: てっぺき", _pa_sb.stage_defense == 2, f"1回適用={_pa_sb.stage_defense} 期待=+2")
# てっぺき: 自分防御+2
_mvss_てっぺき_defense = dl.get_move("てっぺき")
if _mvss_てっぺき_defense:
    random.seed(0); _got_てっぺき_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="はがね", atk_b=60, spatk_b=60); _pds = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "てっぺき")
        if _pas.stage_defense != 0: _got_てっぺき_defense = _pas.stage_defense; break
    check("自分防御+2: てっぺき", _got_てっぺき_defense == 2, f"1回適用={_got_てっぺき_defense} 期待=2")

# ── ドラゴンクロー ──
check("DB: ドラゴンクロー 取得可能", dl.get_move("ドラゴンクロー") is not None)
_mv_ドラゴンクロ_ = dl.get_move("ドラゴンクロー")
if _mv_ドラゴンクロ_:
    _pa_ドラゴンクロ_ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_ドラゴンクロ_ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ドラゴンクロ_ = dmg(_pa_ドラゴンクロ_, _pd_ドラゴンクロ_, "ドラゴンクロー")
    check("ダメージ計算: ドラゴンクロー", _d_ドラゴンクロ_ > 0, f"dmg={_d_ドラゴンクロ_}")

# ── ビルドアップ ──
check("DB: ビルドアップ 取得可能", dl.get_move("ビルドアップ") is not None)
# ビルドアップ: 自分攻撃+1
_mv_sb_ビルドアップ_attack = dl.get_move("ビルドアップ")
if _mv_sb_ビルドアップ_attack:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ビルドアップ")
    check("自分攻撃+1: ビルドアップ", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# ビルドアップ: 自分防御+1
_mv_sb_ビルドアップ_defense = dl.get_move("ビルドアップ")
if _mv_sb_ビルドアップ_defense:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ビルドアップ")
    check("自分防御+1: ビルドアップ", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")

# ── とびはねる ──
check("DB: とびはねる 取得可能", dl.get_move("とびはねる") is not None)
_mv_とびはねる = dl.get_move("とびはねる")
if _mv_とびはねる:
    _pa_とびはねる = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_とびはねる = make_poke(type1="くさ", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_とびはねる = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_とびはねる = make_poke(type1="くさ", def_b=100, spdef_b=100)
        execute(_pa_とびはねる, _pd_とびはねる, "とびはねる"); execute(_pa_とびはねる, _pd_とびはねる, "とびはねる")
        if _pd_とびはねる.hp < _pd_とびはねる.max_hp: break
    check("ダメージ計算: とびはねる", _pd_とびはねる.hp < _pd_とびはねる.max_hp, f"hp={_pd_とびはねる.hp}")
# とびはねる: まひ30%
_mv_s_とびはねる = dl.get_move("とびはねる")
if _mv_s_とびはねる:
    random.seed(0); _hit_とびはねる = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ひこう", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "とびはねる"); execute(_pa2, _pd2, "とびはねる")
        _hit_とびはねる += int((_pd2.status == "paralysis"))
    check("追加効果(まひ30%): とびはねる", 27 <= _hit_とびはねる <= 168, f"count={_hit_とびはねる}/300")
    random.seed(1); _immok_とびはねる = True
    for _ in range(60):
        _pai = make_poke(type1="ひこう", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "とびはねる"); execute(_pai, _pdi, "とびはねる")
        if _pdi.status == "paralysis": _immok_とびはねる = False; break
    check("まひ免疫(でんき型には無効): とびはねる", _immok_とびはねる, "免疫タイプに状態異常が付与されないこと")
# とびはねる: 2ターン溜め
_mv_2t_とびはねる = dl.get_move("とびはねる")
if _mv_2t_とびはねる:
    _pa_2t = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "とびはねる")
    check("2ターン溜め(1T)ダメなし: とびはねる", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: とびはねる", _pa_2t.charging_move == "とびはねる")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "とびはねる")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "とびはねる")
    check("2ターン溜め(2T)ダメあり: とびはねる", _pd_2t.hp < _hp_before_2t)

# ── マッドショット ──
check("DB: マッドショット 取得可能", dl.get_move("マッドショット") is not None)
_mv_マッドショット = dl.get_move("マッドショット")
if _mv_マッドショット:
    _pa_マッドショット = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_マッドショット = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_マッドショット = dmg(_pa_マッドショット, _pd_マッドショット, "マッドショット")
    check("ダメージ計算: マッドショット", _d_マッドショット > 0, f"dmg={_d_マッドショット}")
# マッドショット: 相手素早さ-1
_mv_dd_マッドショット = dl.get_move("マッドショット")
if _mv_dd_マッドショット:
    _pa_dd = make_poke(type1="じめん", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_マッドショット = 0; _dd_ok_マッドショット = False
    for _ in range(60):
        _pd_dd = make_poke(type1="でんき", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "マッドショット")
        if _pd_dd.stage_speed != 0: _dd_val_マッドショット = _pd_dd.stage_speed; _dd_ok_マッドショット = True; break
    check("相手素早さ-1: マッドショット", _dd_ok_マッドショット and _dd_val_マッドショット == -1, f"1回適用={_dd_val_マッドショット} 期待=-1")

# ── ボルテッカー ──
check("DB: ボルテッカー 取得可能", dl.get_move("ボルテッカー") is not None)
_mv_ボルテッカ_ = dl.get_move("ボルテッカー")
if _mv_ボルテッカ_:
    _pa_ボルテッカ_ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ボルテッカ_ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ボルテッカ_ = dmg(_pa_ボルテッカ_, _pd_ボルテッカ_, "ボルテッカー")
    check("ダメージ計算: ボルテッカー", _d_ボルテッカ_ > 0, f"dmg={_d_ボルテッカ_}")
# ボルテッカー: まひ10%
_mv_s_ボルテッカ_ = dl.get_move("ボルテッカー")
if _mv_s_ボルテッカ_:
    random.seed(0); _hit_ボルテッカ_ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ボルテッカー")
        _hit_ボルテッカ_ += int((_pd2.status == "paralysis"))
    check("追加効果(まひ10%): ボルテッカー", 9 <= _hit_ボルテッカ_ <= 66, f"count={_hit_ボルテッカ_}/300")
    random.seed(1); _immok_ボルテッカ_ = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ボルテッカー")
        if _pdi.status == "paralysis": _immok_ボルテッカ_ = False; break
    check("まひ免疫(でんき型には無効): ボルテッカー", _immok_ボルテッカ_, "免疫タイプに状態異常が付与されないこと")
# ボルテッカー: 反動（与ダメの1/3）
_mvrc_ボルテッカ_ = dl.get_move("ボルテッカー")
if _mvrc_ボルテッカ_:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="でんき", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="みず", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "ボルテッカー")
        _rc_dealt_ボルテッカ_ = _hpdr - _pdr.hp; _rc_rcv_ボルテッカ_ = _par.max_hp - _par.hp
        if _rc_dealt_ボルテッカ_ > 0: break
    _rc_exp_ボルテッカ_ = max(1, _rc_dealt_ボルテッカ_ // 3)
    check("反動ダメージ(1/3): ボルテッカー", abs(_rc_rcv_ボルテッカ_ - _rc_exp_ボルテッカ_) <= 2, f"dealt={_rc_dealt_ボルテッカ_} recoil={_rc_rcv_ボルテッカ_} 期待={_rc_exp_ボルテッカ_}")

# ── リーフブレード ──
check("DB: リーフブレード 取得可能", dl.get_move("リーフブレード") is not None)
_mv_リ_フブレ_ド = dl.get_move("リーフブレード")
if _mv_リ_フブレ_ド:
    _pa_リ_フブレ_ド = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_リ_フブレ_ド = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_リ_フブレ_ド = dmg(_pa_リ_フブレ_ド, _pd_リ_フブレ_ド, "リーフブレード")
    check("ダメージ計算: リーフブレード", _d_リ_フブレ_ド > 0, f"dmg={_d_リ_フブレ_ド}")
# リーフブレード: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_リ_フブレ_ド
random.seed(0); _hc_crit_リ_フブレ_ド = 0; _phc = make_poke(type1="くさ")
_mvhc_リ_フブレ_ド = dl.get_move("リーフブレード")
for _ in range(800):
    if _cc_リ_フブレ_ド(_phc, _mvhc_リ_フブレ_ド, make_poke(type1="みず")): _hc_crit_リ_フブレ_ド += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: リーフブレード", 60 <= _hc_crit_リ_フブレ_ド <= 150, f"crit={_hc_crit_リ_フブレ_ド}/800 (期待≈100, 通常1/24なら≈33)")

# ── めいそう ──
check("DB: めいそう 取得可能", dl.get_move("めいそう") is not None)
# めいそう: 自分特攻+1
_mv_sb_めいそう_sp_attack = dl.get_move("めいそう")
if _mv_sb_めいそう_sp_attack:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "めいそう")
    check("自分特攻+1: めいそう", _pa_sb.stage_sp_attack == 1, f"1回適用={_pa_sb.stage_sp_attack} 期待=+1")
# めいそう: 自分特防+1
_mv_sb_めいそう_sp_defense = dl.get_move("めいそう")
if _mv_sb_めいそう_sp_defense:
    _pa_sb = make_poke(type1="エスパー"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "めいそう")
    check("自分特防+1: めいそう", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")

# ── りゅうのまい ──
check("DB: りゅうのまい 取得可能", dl.get_move("りゅうのまい") is not None)
# りゅうのまい: 自分攻撃+1
_mv_sb_りゅうのまい_attack = dl.get_move("りゅうのまい")
if _mv_sb_りゅうのまい_attack:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "りゅうのまい")
    check("自分攻撃+1: りゅうのまい", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# りゅうのまい: 自分素早さ+1
_mv_sb_りゅうのまい_speed = dl.get_move("りゅうのまい")
if _mv_sb_りゅうのまい_speed:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "りゅうのまい")
    check("自分素早さ+1: りゅうのまい", _pa_sb.stage_speed == 1, f"1回適用={_pa_sb.stage_speed} 期待=+1")

# ── ロックブラスト ──
check("DB: ロックブラスト 取得可能", dl.get_move("ロックブラスト") is not None)
_mv_ロックブラスト = dl.get_move("ロックブラスト")
if _mv_ロックブラスト:
    _pa_ロックブラスト = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_ロックブラスト = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_ロックブラスト = dmg(_pa_ロックブラスト, _pd_ロックブラスト, "ロックブラスト")
    check("ダメージ計算: ロックブラスト", _d_ロックブラスト > 0, f"dmg={_d_ロックブラスト}")
# ロックブラスト: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ロックブラスト = dl.get_move("ロックブラスト")
if _mvmh_ロックブラスト:
    _pam = make_poke(type1="いわ", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ロックブラスト = calc_damage(_pam, make_poke(type1="ひこう", hp_b=255, def_b=200, spdef_b=200), _mvmh_ロックブラスト, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ロックブラスト = 0
    for _ in range(20):
        _pdm = make_poke(type1="ひこう", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ロックブラスト"); _multi_ロックブラスト = _pdm.max_hp - _pdm.hp
        if _multi_ロックブラスト > _single_ロックブラスト: break
    check("多段ヒット発生(複数回): ロックブラスト", _multi_ロックブラスト > _single_ロックブラスト, f"single={_single_ロックブラスト} multi={_multi_ロックブラスト}")

# ── みずのはどう ──
check("DB: みずのはどう 取得可能", dl.get_move("みずのはどう") is not None)
_mv_みずのはどう = dl.get_move("みずのはどう")
if _mv_みずのはどう:
    _pa_みずのはどう = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_みずのはどう = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_みずのはどう = dmg(_pa_みずのはどう, _pd_みずのはどう, "みずのはどう")
    check("ダメージ計算: みずのはどう", _d_みずのはどう > 0, f"dmg={_d_みずのはどう}")
# みずのはどう: こんらん20%
_mv_s_みずのはどう = dl.get_move("みずのはどう")
if _mv_s_みずのはどう:
    random.seed(0); _hit_みずのはどう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="みず", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "みずのはどう")
        _hit_みずのはどう += int(_pd2.confused)
    check("追加効果(こんらん20%): みずのはどう", 18 <= _hit_みずのはどう <= 117, f"count={_hit_みずのはどう}/300")

# ── はねやすめ ──
check("DB: はねやすめ 取得可能", dl.get_move("はねやすめ") is not None)
# はねやすめ: HP回復（最大HPの約1/2・無天候）
_mv_hp_はねやすめ = dl.get_move("はねやすめ")
if _mv_hp_はねやすめ:
    _pa_hp = make_poke(type1="ひこう", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()
    execute(_pa_hp, _pd_hp, "はねやすめ")
    _exp_hp_はねやすめ = _pa_hp.max_hp * 1 // 2
    check("HP回復(約1/2): はねやすめ", abs(_pa_hp.hp - (1 + _exp_hp_はねやすめ)) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={_pa_hp.hp} 期待≈{1 + _exp_hp_はねやすめ}")
# はねやすめ: 使用ターン中ひこうタイプ消失（じめん技が通る）
_prs, _, _ = execute_ctx(make_poke(type1="でんき", type2="ひこう", hp_b=200), make_poke(), "はねやすめ")
check("ひこう消失: はねやすめ", "ひこう" not in (_prs.active.type1, _prs.active.type2), f"types={_prs.active.type1}/{_prs.active.type2}")

# ── いやしのねがい ──
check("DB: いやしのねがい 取得可能", dl.get_move("いやしのねがい") is not None)
# いやしのねがい: 自分ひんし+healing_wishフラグ
_piw = make_poke(); _s1iw = BattleSide([_piw, make_poke()]); _s2iw = BattleSide([make_poke()])
_execute_move(_s1iw, _s2iw, Action(type="move", move=dl.get_move("いやしのねがい")), BattleField())
check("いやしのねがい 自分ひんし: いやしのねがい", not _piw.is_alive)
check("いやしのねがい healing_wish: いやしのねがい", _s1iw.healing_wish)

# ── ジャイロボール ──
check("DB: ジャイロボール 取得可能", dl.get_move("ジャイロボール") is not None)
# ジャイロボール: 威力 = min(150, floor(25×相手速度/自速度))。具体値と上限を検証
_pg = make_poke(atk_b=100, spd_b=10); _df = make_poke(spd_b=200, def_b=100); _de = make_poke(spd_b=10, def_b=100)
_gslow = _ep(_pg, _df, dl.get_move("ジャイロボール"), BattleField()); _geq = _ep(_pg, _de, dl.get_move("ジャイロボール"), BattleField())
check("速度比威力: ジャイロボール", _gslow > _geq, f"slow={_gslow} eq={_geq}")
# 具体値: 相手speed=自speedの4倍 → 25×4=100
_pg4 = make_poke(spd_b=10); _df4 = make_poke(spd_b=10); import math as _m
_sa = _pg4.get_effective_speed(); _df4.speed = _sa * 4
_exp_g = min(150, max(1, _m.floor(25 * _df4.get_effective_speed() / _sa)))
_got_g = _ep(_pg4, _df4, dl.get_move("ジャイロボール"), BattleField())
check("威力式(25×相手/自): ジャイロボール", _got_g == _exp_g, f"got={_got_g} exp={_exp_g}")
# 上限150: 相手が極端に速い
_pg_s = make_poke(spd_b=4); _df_f = make_poke(spd_b=255); _df_f.speed = 99999
_got_cap = _ep(_pg_s, _df_f, dl.get_move("ジャイロボール"), BattleField())
check("威力上限150: ジャイロボール", _got_cap == 150, f"got={_got_cap}")

# ── おいかぜ ──
check("DB: おいかぜ 取得可能", dl.get_move("おいかぜ") is not None)
# おいかぜ: 自分側の素早さが2倍（単体でも自分に効果）
from simulator.battle import _speed_order
_s1o, _s2o, _ = execute_ctx(make_poke(type1="ひこう", spd_b=80, moves=["おいかぜ"]), make_poke(spd_b=100), "おいかぜ")
check("おいかぜS2倍: おいかぜ", _s1o.tailwind, f"tailwind={_s1o.tailwind}")

# ── フェイント ──
check("DB: フェイント 取得可能", dl.get_move("フェイント") is not None)
_mv_フェイント = dl.get_move("フェイント")
if _mv_フェイント:
    _pa_フェイント = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_フェイント = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_フェイント = dmg(_pa_フェイント, _pd_フェイント, "フェイント")
    check("ダメージ計算: フェイント", _d_フェイント > 0, f"dmg={_d_フェイント}")
# フェイント: 優先度2
_mv_pr_フェイント = dl.get_move("フェイント")
if _mv_pr_フェイント and _mv_pr_フェイント.priority == 2:
    check("優先度2: フェイント", _mv_pr_フェイント.priority == 2)
elif _mv_pr_フェイント:
    check("優先度2: フェイント", _mv_pr_フェイント.priority == 2, f"DB優先度={_mv_pr_フェイント.priority} 仕様=2")
# フェイント: まもる状態の相手を貫通して攻撃
_pft = make_poke(type1="ノーマル", atk_b=120); _dft = make_poke(type1="ノーマル", hp_b=255, def_b=150)
_dft.protecting = True; _hpft = _dft.hp
_execute_move(BattleSide([_pft]), BattleSide([_dft]), Action(type="move", move=dl.get_move("フェイント")), BattleField())
check("まもる貫通: フェイント", _dft.hp < _hpft and not _dft.protecting, f"hp={_dft.hp}/{_hpft} protect={_dft.protecting}")

# ── メタルバースト ──
check("DB: メタルバースト 取得可能", dl.get_move("メタルバースト") is not None)
# メタルバースト: カウンター反射（物理+特殊×1.5）
_mvcnt_メタルバ_スト = dl.get_move("メタルバースト")
if _mvcnt_メタルバ_スト:
    _pac_cnt = make_poke(type1="はがね", atk_b=100, spatk_b=100, hp_b=200)
    _pdc_cnt = make_poke(type1="ノーマル" if "はがね"!="かくとう" else "エスパー", hp_b=255, def_b=100, spdef_b=100)
    _pac_cnt._last_physical_dmg_received = 100
    _exp_cnt = int(100 * 1.5)
    _hpc0 = _pdc_cnt.hp; execute(_pac_cnt, _pdc_cnt, "メタルバースト")
    check("カウンター反射: メタルバースト", _hpc0 - _pdc_cnt.hp == _exp_cnt, f"返し={_hpc0 - _pdc_cnt.hp} 期待={_exp_cnt}")
    _pac_cnt2 = make_poke(type1="はがね", atk_b=100, spatk_b=100); _pdc_cnt2 = make_poke(type1="ノーマル", hp_b=255)
    _hpc20 = _pdc_cnt2.hp; execute(_pac_cnt2, _pdc_cnt2, "メタルバースト")
    check("カウンター被ダメ0で失敗: メタルバースト", _pdc_cnt2.hp == _hpc20)

# ── とんぼがえり ──
check("DB: とんぼがえり 取得可能", dl.get_move("とんぼがえり") is not None)
_mv_とんぼがえり = dl.get_move("とんぼがえり")
if _mv_とんぼがえり:
    _pa_とんぼがえり = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_とんぼがえり = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_とんぼがえり = dmg(_pa_とんぼがえり, _pd_とんぼがえり, "とんぼがえり")
    check("ダメージ計算: とんぼがえり", _d_とんぼがえり > 0, f"dmg={_d_とんぼがえり}")
# とんぼがえり: ピボット交代フラグ
_mvpv_とんぼがえり = dl.get_move("とんぼがえり")
if _mvpv_とんぼがえり:
    _pap = make_poke(type1="むし", atk_b=100, spatk_b=100); _pdp = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_とんぼがえり), BattleField())
    check("ピボット交代フラグ: とんぼがえり", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")

# ── インファイト ──
check("DB: インファイト 取得可能", dl.get_move("インファイト") is not None)
_mv_インファイト = dl.get_move("インファイト")
if _mv_インファイト:
    _pa_インファイト = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_インファイト = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_インファイト = dmg(_pa_インファイト, _pd_インファイト, "インファイト")
    check("ダメージ計算: インファイト", _d_インファイト > 0, f"dmg={_d_インファイト}")
# インファイト: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="かくとう", atk_b=120, spatk_b=120); _dsd = make_poke(type1="ノーマル", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "インファイト")
    if _psd.stage_defense < 0: break
check("自分防御下降: インファイト", _psd.stage_defense < 0, f"stage={_psd.stage_defense}")
check("自分特防下降: インファイト", _psd.stage_sp_defense < 0, f"stage={_psd.stage_sp_defense}")

# ── しっぺがえし ──
check("DB: しっぺがえし 取得可能", dl.get_move("しっぺがえし") is not None)
_mv_しっぺがえし = dl.get_move("しっぺがえし")
if _mv_しっぺがえし:
    _pa_しっぺがえし = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_しっぺがえし = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_しっぺがえし = dmg(_pa_しっぺがえし, _pd_しっぺがえし, "しっぺがえし")
    check("ダメージ計算: しっぺがえし", _d_しっぺがえし > 0, f"dmg={_d_しっぺがえし}")
# しっぺがえし: _acts_second状態で威力2倍
_ps = make_poke(atk_b=100); _ds = make_poke(def_b=100)
_sa = _ep(_ps, _ds, dl.get_move("しっぺがえし"), BattleField()); _ps._acts_second = True; _sb = _ep(_ps, _ds, dl.get_move("しっぺがえし"), BattleField())
check("後攻2倍: しっぺがえし", _sb == _sa * 2, f"a={_sa} b={_sb}")
# 実戦: 後攻（遅い）で使うと先攻時より大ダメージ＝条件が実機能
from simulator.battle import Battle as _Bsp
import simulator.battle as _SBsp; _msp = _SBsp.MAX_TURNS; _SBsp.MAX_TURNS = 1
_act_sp = lambda s,o,f: Action(type="move", move=dl.get_move("しっぺがえし"), move_idx=0)
_act_wk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_psp_slow = make_poke(type1="あく", atk_b=120, spd_b=10, moves=["しっぺがえし"]); _fsp = make_poke(type1="エスパー", atk_b=10, spd_b=200, hp_b=255, def_b=120, moves=["たいあたり"])
_Bsp(BattleSide([_psp_slow]), BattleSide([_fsp])).run(_act_sp, _act_wk)
_dmg_second = _fsp.max_hp - _fsp.hp
_psp_fast = make_poke(type1="あく", atk_b=120, spd_b=200, moves=["しっぺがえし"]); _fsp2 = make_poke(type1="エスパー", atk_b=10, spd_b=10, hp_b=255, def_b=120, moves=["たいあたり"])
_Bsp(BattleSide([_psp_fast]), BattleSide([_fsp2])).run(_act_sp, _act_wk)
_dmg_first = _fsp2.max_hp - _fsp2.hp; _SBsp.MAX_TURNS = _msp
check("後攻条件が実戦で成立: しっぺがえし", _dmg_second > _dmg_first * 1.4, f"後攻={_dmg_second} 先攻={_dmg_first}")

# ── なげつける ──
check("DB: なげつける 取得可能", dl.get_move("なげつける") is not None)
# なげつける: 持ち物別の威力テーブルを全件検証
_dnt = make_poke(type1="ノーマル", hp_b=255, def_b=120)
_FLING = {"こだわりハチマキ":130,"こだわりメガネ":90,"こだわりスカーフ":90,"ゴツゴツメット":80,"くろおび":80,"きあいのタスキ":60,"じゅうなんチョッキ":60,"どくバリ":50,"いのちのたま":30,"くろいヘドロ":30,"メタルコート":30,"シルクのスカーフ":20,"たべのこし":20}
_nt_ng = []
for _it, _ep_exp in _FLING.items():
    _pnt = make_poke(type1="あく", atk_b=100, item=_it)
    _got_nt = _ep(_pnt, _dnt, dl.get_move("なげつける"), BattleField())
    if _got_nt != _ep_exp: _nt_ng.append(f"{_it}:{_got_nt}!={_ep_exp}")
check("道具別威力テーブル全件: なげつける", not _nt_ng, f"NG={_nt_ng}")
# テーブル外アイテムはデフォルト威力10
_pnt_d = make_poke(type1="あく", atk_b=100, item="オボンのみ")
check("テーブル外デフォルト10: なげつける", _ep(_pnt_d, _dnt, dl.get_move("なげつける"), BattleField()) == 10, f"got={_ep(_pnt_d, _dnt, dl.get_move('なげつける'), BattleField())}")
# 持ち物なしは失敗（相手にダメージが入らない）
_pnt_n = make_poke(type1="あく", atk_b=100); _dnt_n = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpnn = _dnt_n.hp
execute(_pnt_n, _dnt_n, "なげつける")
check("持ち物なしで失敗: なげつける", _dnt_n.hp == _hpnn, f"hp={_dnt_n.hp}/{_hpnn}")
# 使うと持ち物が無くなる
_pnt3 = make_poke(type1="あく", atk_b=100, item="こだわりハチマキ"); execute(_pnt3, make_poke(type1="ノーマル", hp_b=255), "なげつける")
check("道具消費: なげつける", _pnt3.item is None, f"item={_pnt3.item}")

# ── まねっこ ──
check("DB: まねっこ 取得可能", dl.get_move("まねっこ") is not None)
# まねっこ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: まねっこ", "まねっこ", "ノーマル", False, smoke=("まねっこ" in DOUBLE_ONLY_SMOKE))

# ── パワースワップ ──
check("DB: パワースワップ 取得可能", dl.get_move("パワースワップ") is not None)
# パワースワップ: 攻撃・特攻の能力変化を相手と入れ替え（双方向。コピーでなく入替を区別）
_pp = make_poke(); _pp.stage_attack = -1; _pp.stage_sp_attack = 1
_dp = make_poke(); _dp.stage_attack = 3; _dp.stage_sp_attack = 2
execute(_pp, _dp, "パワースワップ")
check("パワースワップ入替(双方向): パワースワップ", _pp.stage_attack == 3 and _pp.stage_sp_attack == 2 and _dp.stage_attack == -1 and _dp.stage_sp_attack == 1, f"自{_pp.stage_attack}/{_pp.stage_sp_attack} 相{_dp.stage_attack}/{_dp.stage_sp_attack}")

# ── ふいうち ──
check("DB: ふいうち 取得可能", dl.get_move("ふいうち") is not None)
_mv_ふいうち = dl.get_move("ふいうち")
if _mv_ふいうち:
    _pa_ふいうち = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ふいうち = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ふいうち = dmg(_pa_ふいうち, _pd_ふいうち, "ふいうち")
    check("ダメージ計算: ふいうち", _d_ふいうち > 0, f"dmg={_d_ふいうち}")
# ふいうち: 優先度1
_mv_pr_ふいうち = dl.get_move("ふいうち")
if _mv_pr_ふいうち and _mv_pr_ふいうち.priority == 1:
    check("優先度1: ふいうち", _mv_pr_ふいうち.priority == 1)
elif _mv_pr_ふいうち:
    check("優先度1: ふいうち", _mv_pr_ふいうち.priority == 1, f"DB優先度={_mv_pr_ふいうち.priority} 仕様=1")
# ふいうち: 相手が攻撃技を選んでいれば成功、変化技/未選択なら失敗
_pfu = make_poke(type1="あく", atk_b=120)
_opp_atk = Action(type="move", move=dl.get_move("のしかかり"))
_opp_sta = Action(type="move", move=dl.get_move("まもる"))
# 相手が攻撃技 → 成功
_dfu1 = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpfu1 = _dfu1.hp
_execute_move(BattleSide([_pfu]), BattleSide([_dfu1]), Action(type="move", move=dl.get_move("ふいうち")), BattleField(), _opp_atk)
check("攻撃技相手に成功: ふいうち", _dfu1.hp < _hpfu1, f"hp={_dfu1.hp}/{_hpfu1}")
# 相手が変化技 → 失敗
_dfu2 = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpfu2 = _dfu2.hp
_execute_move(BattleSide([_pfu]), BattleSide([_dfu2]), Action(type="move", move=dl.get_move("ふいうち")), BattleField(), _opp_sta)
check("変化技相手に失敗: ふいうち", _dfu2.hp == _hpfu2, f"hp={_dfu2.hp}/{_hpfu2}")

# ── どくびし ──
check("DB: どくびし 取得可能", dl.get_move("どくびし") is not None)
# どくびし: ハザードtoxic_spikes
_mvhz_どくびし = dl.get_move("どくびし")
if _mvhz_どくびし:
    _s1h, _s2h, _fh2 = execute_ctx(make_poke(type1="どく"), make_poke(), "どくびし")
    _hzval = _fh2.toxic_spikes[_s2h.field_idx]
    check("ハザードtoxic_spikes: どくびし", bool(_hzval), f"val={_hzval}")

# ── でんじふゆう ──
check("DB: でんじふゆう 取得可能", dl.get_move("でんじふゆう") is not None)
# でんじふゆう: じめん技無効化
_pmr = make_poke(type1="でんき"); execute(_pmr, make_poke(), "でんじふゆう")
check("でんじふゆうフラグ: でんじふゆう", _pmr.magnet_rise)
_atkg = make_poke(type1="じめん", atk_b=120, moves=["じしん"])
_djump = dmg(_atkg, _pmr, "じしん")
check("でんじふゆう じめん無効: でんじふゆう", _djump == 0, f"dmg={_djump}")

# ── フレアドライブ ──
check("DB: フレアドライブ 取得可能", dl.get_move("フレアドライブ") is not None)
_mv_フレアドライブ = dl.get_move("フレアドライブ")
if _mv_フレアドライブ:
    _pa_フレアドライブ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_フレアドライブ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_フレアドライブ = dmg(_pa_フレアドライブ, _pd_フレアドライブ, "フレアドライブ")
    check("ダメージ計算: フレアドライブ", _d_フレアドライブ > 0, f"dmg={_d_フレアドライブ}")
# フレアドライブ: やけど10%
_mv_s_フレアドライブ = dl.get_move("フレアドライブ")
if _mv_s_フレアドライブ:
    random.seed(0); _hit_フレアドライブ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "フレアドライブ")
        _hit_フレアドライブ += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): フレアドライブ", 9 <= _hit_フレアドライブ <= 66, f"count={_hit_フレアドライブ}/300")
    random.seed(1); _immok_フレアドライブ = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "フレアドライブ")
        if _pdi.status == "burn": _immok_フレアドライブ = False; break
    check("やけど免疫(ほのお型には無効): フレアドライブ", _immok_フレアドライブ, "免疫タイプに状態異常が付与されないこと")
# フレアドライブ: 反動（与ダメの1/3）
_mvrc_フレアドライブ = dl.get_move("フレアドライブ")
if _mvrc_フレアドライブ:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="ほのお", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="くさ", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "フレアドライブ")
        _rc_dealt_フレアドライブ = _hpdr - _pdr.hp; _rc_rcv_フレアドライブ = _par.max_hp - _par.hp
        if _rc_dealt_フレアドライブ > 0: break
    _rc_exp_フレアドライブ = max(1, _rc_dealt_フレアドライブ // 3)
    check("反動ダメージ(1/3): フレアドライブ", abs(_rc_rcv_フレアドライブ - _rc_exp_フレアドライブ) <= 2, f"dealt={_rc_dealt_フレアドライブ} recoil={_rc_rcv_フレアドライブ} 期待={_rc_exp_フレアドライブ}")

# ── ロックカット ──
check("DB: ロックカット 取得可能", dl.get_move("ロックカット") is not None)
# ロックカット: 自分素早さ+2
_mv_sb_ロックカット_speed = dl.get_move("ロックカット")
if _mv_sb_ロックカット_speed:
    _pa_sb = make_poke(type1="いわ"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ロックカット")
    check("自分素早さ+2: ロックカット", _pa_sb.stage_speed == 2, f"1回適用={_pa_sb.stage_speed} 期待=+2")
# ロックカット: 自分素早さ+2
_mvss_ロックカット_speed = dl.get_move("ロックカット")
if _mvss_ロックカット_speed:
    random.seed(0); _got_ロックカット_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="いわ", atk_b=60, spatk_b=60); _pds = make_poke(type1="ひこう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "ロックカット")
        if _pas.stage_speed != 0: _got_ロックカット_speed = _pas.stage_speed; break
    check("自分素早さ+2: ロックカット", _got_ロックカット_speed == 2, f"1回適用={_got_ロックカット_speed} 期待=2")

# ── はどうだん ──
check("DB: はどうだん 取得可能", dl.get_move("はどうだん") is not None)
_mv_はどうだん = dl.get_move("はどうだん")
if _mv_はどうだん:
    _pa_はどうだん = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_はどうだん = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_はどうだん = dmg(_pa_はどうだん, _pd_はどうだん, "はどうだん")
    check("ダメージ計算: はどうだん", _d_はどうだん > 0, f"dmg={_d_はどうだん}")
# はどうだん: 必中
_mvmust_はどうだん = dl.get_move("はどうだん")
if _mvmust_はどうだん:
    random.seed(0); _hit_all_はどうだん = True
    for _ in range(30):
        _pah = make_poke(type1="かくとう", atk_b=100, spatk_b=100); _pdh = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "はどうだん")
        if _pdh.hp == _hpb: _hit_all_はどうだん = False; break
    check("必中: はどうだん", _hit_all_はどうだん)

# ── どくづき ──
check("DB: どくづき 取得可能", dl.get_move("どくづき") is not None)
_mv_どくづき = dl.get_move("どくづき")
if _mv_どくづき:
    _pa_どくづき = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_どくづき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_どくづき = dmg(_pa_どくづき, _pd_どくづき, "どくづき")
    check("ダメージ計算: どくづき", _d_どくづき > 0, f"dmg={_d_どくづき}")
# どくづき: どく30%
_mv_s_どくづき = dl.get_move("どくづき")
if _mv_s_どくづき:
    random.seed(0); _hit_どくづき = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "どくづき")
        _hit_どくづき += int((_pd2.status == "poison"))
    check("追加効果(どく30%): どくづき", 27 <= _hit_どくづき <= 168, f"count={_hit_どくづき}/300")
    random.seed(1); _immok_どくづき = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくづき")
        if _pdi.status == "poison": _immok_どくづき = False; break
    check("どく免疫(どく型には無効): どくづき", _immok_どくづき, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_どくづき = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくづき")
        if _pdi.status == "poison": _immok_どくづき = False; break
    check("どく免疫(はがね型には無効): どくづき", _immok_どくづき, "免疫タイプに状態異常が付与されないこと")

# ── あくのはどう ──
check("DB: あくのはどう 取得可能", dl.get_move("あくのはどう") is not None)
_mv_あくのはどう = dl.get_move("あくのはどう")
if _mv_あくのはどう:
    _pa_あくのはどう = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_あくのはどう = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_あくのはどう = dmg(_pa_あくのはどう, _pd_あくのはどう, "あくのはどう")
    check("ダメージ計算: あくのはどう", _d_あくのはどう > 0, f"dmg={_d_あくのはどう}")
# あくのはどう: ひるみ20%
_mv_f_あくのはどう = dl.get_move("あくのはどう")
if _mv_f_あくのはどう:
    random.seed(1); _fh_あくのはどう = 0
    for _ in range(300):
        _pa3 = make_poke(type1="あく", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="エスパー", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "あくのはどう"); _fh_あくのはどう += int(_pd3.flinched)
    check("ひるみ(20%): あくのはどう", 18 <= _fh_あくのはどう <= 117, f"count={_fh_あくのはどう}/300")

# ── タネばくだん ──
check("DB: タネばくだん 取得可能", dl.get_move("タネばくだん") is not None)
_mv_タネばくだん = dl.get_move("タネばくだん")
if _mv_タネばくだん:
    _pa_タネばくだん = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_タネばくだん = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_タネばくだん = dmg(_pa_タネばくだん, _pd_タネばくだん, "タネばくだん")
    check("ダメージ計算: タネばくだん", _d_タネばくだん > 0, f"dmg={_d_タネばくだん}")

# ── つじぎり ──
check("DB: つじぎり 取得可能", dl.get_move("つじぎり") is not None)
_mv_つじぎり = dl.get_move("つじぎり")
if _mv_つじぎり:
    _pa_つじぎり = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_つじぎり = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_つじぎり = dmg(_pa_つじぎり, _pd_つじぎり, "つじぎり")
    check("ダメージ計算: つじぎり", _d_つじぎり > 0, f"dmg={_d_つじぎり}")
# つじぎり: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_つじぎり
random.seed(0); _hc_crit_つじぎり = 0; _phc = make_poke(type1="あく")
_mvhc_つじぎり = dl.get_move("つじぎり")
for _ in range(800):
    if _cc_つじぎり(_phc, _mvhc_つじぎり, make_poke(type1="エスパー")): _hc_crit_つじぎり += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: つじぎり", 60 <= _hc_crit_つじぎり <= 150, f"crit={_hc_crit_つじぎり}/800 (期待≈100, 通常1/24なら≈33)")

# ── アクアテール ──
check("DB: アクアテール 取得可能", dl.get_move("アクアテール") is not None)
_mv_アクアテ_ル = dl.get_move("アクアテール")
if _mv_アクアテ_ル:
    _pa_アクアテ_ル = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_アクアテ_ル = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_アクアテ_ル = dmg(_pa_アクアテ_ル, _pd_アクアテ_ル, "アクアテール")
    check("ダメージ計算: アクアテール", _d_アクアテ_ル > 0, f"dmg={_d_アクアテ_ル}")

# ── シザークロス ──
check("DB: シザークロス 取得可能", dl.get_move("シザークロス") is not None)
_mv_シザ_クロス = dl.get_move("シザークロス")
if _mv_シザ_クロス:
    _pa_シザ_クロス = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_シザ_クロス = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_シザ_クロス = dmg(_pa_シザ_クロス, _pd_シザ_クロス, "シザークロス")
    check("ダメージ計算: シザークロス", _d_シザ_クロス > 0, f"dmg={_d_シザ_クロス}")

# ── エアスラッシュ ──
check("DB: エアスラッシュ 取得可能", dl.get_move("エアスラッシュ") is not None)
_mv_エアスラッシュ = dl.get_move("エアスラッシュ")
if _mv_エアスラッシュ:
    _pa_エアスラッシュ = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_エアスラッシュ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_エアスラッシュ = dmg(_pa_エアスラッシュ, _pd_エアスラッシュ, "エアスラッシュ")
    check("ダメージ計算: エアスラッシュ", _d_エアスラッシュ > 0, f"dmg={_d_エアスラッシュ}")
# エアスラッシュ: ひるみ30%
_mv_f_エアスラッシュ = dl.get_move("エアスラッシュ")
if _mv_f_エアスラッシュ:
    random.seed(1); _fh_エアスラッシュ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="ひこう", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "エアスラッシュ"); _fh_エアスラッシュ += int(_pd3.flinched)
    check("ひるみ(30%): エアスラッシュ", 27 <= _fh_エアスラッシュ <= 168, f"count={_fh_エアスラッシュ}/300")

# ── むしのさざめき ──
check("DB: むしのさざめき 取得可能", dl.get_move("むしのさざめき") is not None)
_mv_むしのさざめき = dl.get_move("むしのさざめき")
if _mv_むしのさざめき:
    _pa_むしのさざめき = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_むしのさざめき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_むしのさざめき = dmg(_pa_むしのさざめき, _pd_むしのさざめき, "むしのさざめき")
    check("ダメージ計算: むしのさざめき", _d_むしのさざめき > 0, f"dmg={_d_むしのさざめき}")
# むしのさざめき: 相手特防-1
_mv_dd_むしのさざめき = dl.get_move("むしのさざめき")
if _mv_dd_むしのさざめき:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_むしのさざめき = 0; _dd_ok_むしのさざめき = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "むしのさざめき")
        if _pd_dd.stage_sp_defense != 0: _dd_val_むしのさざめき = _pd_dd.stage_sp_defense; _dd_ok_むしのさざめき = True; break
    check("相手特防-1: むしのさざめき", _dd_ok_むしのさざめき and _dd_val_むしのさざめき == -1, f"1回適用={_dd_val_むしのさざめき} 期待=-1")

# ── ドラゴンダイブ ──
check("DB: ドラゴンダイブ 取得可能", dl.get_move("ドラゴンダイブ") is not None)
_mv_ドラゴンダイブ = dl.get_move("ドラゴンダイブ")
if _mv_ドラゴンダイブ:
    _pa_ドラゴンダイブ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_ドラゴンダイブ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ドラゴンダイブ = dmg(_pa_ドラゴンダイブ, _pd_ドラゴンダイブ, "ドラゴンダイブ")
    check("ダメージ計算: ドラゴンダイブ", _d_ドラゴンダイブ > 0, f"dmg={_d_ドラゴンダイブ}")
# ドラゴンダイブ: ひるみ20%
_mv_f_ドラゴンダイブ = dl.get_move("ドラゴンダイブ")
if _mv_f_ドラゴンダイブ:
    random.seed(1); _fh_ドラゴンダイブ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="ドラゴン", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="ドラゴン", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "ドラゴンダイブ"); _fh_ドラゴンダイブ += int(_pd3.flinched)
    check("ひるみ(20%): ドラゴンダイブ", 18 <= _fh_ドラゴンダイブ <= 117, f"count={_fh_ドラゴンダイブ}/300")
# ドラゴンダイブ: ちいさくなる状態の相手に威力2倍
_pm = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
_dm0 = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
_dm1 = make_poke(type1="ドラゴン", def_b=100, spdef_b=100); _dm1.minimized = True
_pm_n = _ep(_pm, _dm0, dl.get_move("ドラゴンダイブ"), BattleField())
_pm_m = _ep(_pm, _dm1, dl.get_move("ドラゴンダイブ"), BattleField())
check("ちいさくなる2倍: ドラゴンダイブ", _pm_m == _pm_n * 2, f"normal={_pm_n} mini={_pm_m}")

# ── りゅうのはどう ──
check("DB: りゅうのはどう 取得可能", dl.get_move("りゅうのはどう") is not None)
_mv_りゅうのはどう = dl.get_move("りゅうのはどう")
if _mv_りゅうのはどう:
    _pa_りゅうのはどう = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_りゅうのはどう = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_りゅうのはどう = dmg(_pa_りゅうのはどう, _pd_りゅうのはどう, "りゅうのはどう")
    check("ダメージ計算: りゅうのはどう", _d_りゅうのはどう > 0, f"dmg={_d_りゅうのはどう}")

# ── パワージェム ──
check("DB: パワージェム 取得可能", dl.get_move("パワージェム") is not None)
_mv_パワ_ジェム = dl.get_move("パワージェム")
if _mv_パワ_ジェム:
    _pa_パワ_ジェム = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_パワ_ジェム = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_パワ_ジェム = dmg(_pa_パワ_ジェム, _pd_パワ_ジェム, "パワージェム")
    check("ダメージ計算: パワージェム", _d_パワ_ジェム > 0, f"dmg={_d_パワ_ジェム}")

# ── しんくうは ──
check("DB: しんくうは 取得可能", dl.get_move("しんくうは") is not None)
_mv_しんくうは = dl.get_move("しんくうは")
if _mv_しんくうは:
    _pa_しんくうは = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_しんくうは = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_しんくうは = dmg(_pa_しんくうは, _pd_しんくうは, "しんくうは")
    check("ダメージ計算: しんくうは", _d_しんくうは > 0, f"dmg={_d_しんくうは}")
# しんくうは: 優先度1
_mv_pr_しんくうは = dl.get_move("しんくうは")
if _mv_pr_しんくうは and _mv_pr_しんくうは.priority == 1:
    check("優先度1: しんくうは", _mv_pr_しんくうは.priority == 1)
elif _mv_pr_しんくうは:
    check("優先度1: しんくうは", _mv_pr_しんくうは.priority == 1, f"DB優先度={_mv_pr_しんくうは.priority} 仕様=1")

# ── ドレインパンチ ──
check("DB: ドレインパンチ 取得可能", dl.get_move("ドレインパンチ") is not None)
_mv_ドレインパンチ = dl.get_move("ドレインパンチ")
if _mv_ドレインパンチ:
    _pa_ドレインパンチ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ドレインパンチ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ドレインパンチ = dmg(_pa_ドレインパンチ, _pd_ドレインパンチ, "ドレインパンチ")
    check("ダメージ計算: ドレインパンチ", _d_ドレインパンチ > 0, f"dmg={_d_ドレインパンチ}")
# ドレインパンチ: ドレイン（与ダメの1/2回復）
_mv_dr_ドレインパンチ = dl.get_move("ドレインパンチ")
if _mv_dr_ドレインパンチ:
    _pa_dr = make_poke(type1="かくとう", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_ドレインパンチ = False; _dr_dealt_ドレインパンチ = 0; _dr_heal_ドレインパンチ = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="ノーマル", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "ドレインパンチ")
        _dr_dealt_ドレインパンチ = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_ドレインパンチ = _pa_dr.hp - 1
        if _dr_dealt_ドレインパンチ > 0: _dr_ok_ドレインパンチ = abs(_dr_heal_ドレインパンチ - max(1, _dr_dealt_ドレインパンチ * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): ドレインパンチ", _dr_ok_ドレインパンチ, f"dealt={_dr_dealt_ドレインパンチ} heal={_dr_heal_ドレインパンチ}")

# ── きあいだま ──
check("DB: きあいだま 取得可能", dl.get_move("きあいだま") is not None)
_mv_きあいだま = dl.get_move("きあいだま")
if _mv_きあいだま:
    _pa_きあいだま = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_きあいだま = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_きあいだま = dmg(_pa_きあいだま, _pd_きあいだま, "きあいだま")
    check("ダメージ計算: きあいだま", _d_きあいだま > 0, f"dmg={_d_きあいだま}")
# きあいだま: 相手特防-1
_mv_dd_きあいだま = dl.get_move("きあいだま")
if _mv_dd_きあいだま:
    _pa_dd = make_poke(type1="かくとう", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_きあいだま = 0; _dd_ok_きあいだま = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "きあいだま")
        if _pd_dd.stage_sp_defense != 0: _dd_val_きあいだま = _pd_dd.stage_sp_defense; _dd_ok_きあいだま = True; break
    check("相手特防-1: きあいだま", _dd_ok_きあいだま and _dd_val_きあいだま == -1, f"1回適用={_dd_val_きあいだま} 期待=-1")

# ── エナジーボール ──
check("DB: エナジーボール 取得可能", dl.get_move("エナジーボール") is not None)
_mv_エナジ_ボ_ル = dl.get_move("エナジーボール")
if _mv_エナジ_ボ_ル:
    _pa_エナジ_ボ_ル = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_エナジ_ボ_ル = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_エナジ_ボ_ル = dmg(_pa_エナジ_ボ_ル, _pd_エナジ_ボ_ル, "エナジーボール")
    check("ダメージ計算: エナジーボール", _d_エナジ_ボ_ル > 0, f"dmg={_d_エナジ_ボ_ル}")
# エナジーボール: 相手特防-1
_mv_dd_エナジ_ボ_ル = dl.get_move("エナジーボール")
if _mv_dd_エナジ_ボ_ル:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_エナジ_ボ_ル = 0; _dd_ok_エナジ_ボ_ル = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "エナジーボール")
        if _pd_dd.stage_sp_defense != 0: _dd_val_エナジ_ボ_ル = _pd_dd.stage_sp_defense; _dd_ok_エナジ_ボ_ル = True; break
    check("相手特防-1: エナジーボール", _dd_ok_エナジ_ボ_ル and _dd_val_エナジ_ボ_ル == -1, f"1回適用={_dd_val_エナジ_ボ_ル} 期待=-1")

# ── ブレイブバード ──
check("DB: ブレイブバード 取得可能", dl.get_move("ブレイブバード") is not None)
_mv_ブレイブバ_ド = dl.get_move("ブレイブバード")
if _mv_ブレイブバ_ド:
    _pa_ブレイブバ_ド = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ブレイブバ_ド = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ブレイブバ_ド = dmg(_pa_ブレイブバ_ド, _pd_ブレイブバ_ド, "ブレイブバード")
    check("ダメージ計算: ブレイブバード", _d_ブレイブバ_ド > 0, f"dmg={_d_ブレイブバ_ド}")
# ブレイブバード: 反動（与ダメの1/3）
_mvrc_ブレイブバ_ド = dl.get_move("ブレイブバード")
if _mvrc_ブレイブバ_ド:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="ひこう", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="くさ", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "ブレイブバード")
        _rc_dealt_ブレイブバ_ド = _hpdr - _pdr.hp; _rc_rcv_ブレイブバ_ド = _par.max_hp - _par.hp
        if _rc_dealt_ブレイブバ_ド > 0: break
    _rc_exp_ブレイブバ_ド = max(1, _rc_dealt_ブレイブバ_ド // 3)
    check("反動ダメージ(1/3): ブレイブバード", abs(_rc_rcv_ブレイブバ_ド - _rc_exp_ブレイブバ_ド) <= 2, f"dealt={_rc_dealt_ブレイブバ_ド} recoil={_rc_rcv_ブレイブバ_ド} 期待={_rc_exp_ブレイブバ_ド}")

# ── だいちのちから ──
check("DB: だいちのちから 取得可能", dl.get_move("だいちのちから") is not None)
_mv_だいちのちから = dl.get_move("だいちのちから")
if _mv_だいちのちから:
    _pa_だいちのちから = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_だいちのちから = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_だいちのちから = dmg(_pa_だいちのちから, _pd_だいちのちから, "だいちのちから")
    check("ダメージ計算: だいちのちから", _d_だいちのちから > 0, f"dmg={_d_だいちのちから}")
# だいちのちから: 相手特防-1
_mv_dd_だいちのちから = dl.get_move("だいちのちから")
if _mv_dd_だいちのちから:
    _pa_dd = make_poke(type1="じめん", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_だいちのちから = 0; _dd_ok_だいちのちから = False
    for _ in range(60):
        _pd_dd = make_poke(type1="でんき", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "だいちのちから")
        if _pd_dd.stage_sp_defense != 0: _dd_val_だいちのちから = _pd_dd.stage_sp_defense; _dd_ok_だいちのちから = True; break
    check("相手特防-1: だいちのちから", _dd_ok_だいちのちから and _dd_val_だいちのちから == -1, f"1回適用={_dd_val_だいちのちから} 期待=-1")

# ── バレットパンチ ──
check("DB: バレットパンチ 取得可能", dl.get_move("バレットパンチ") is not None)
_mv_バレットパンチ = dl.get_move("バレットパンチ")
if _mv_バレットパンチ:
    _pa_バレットパンチ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_バレットパンチ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_バレットパンチ = dmg(_pa_バレットパンチ, _pd_バレットパンチ, "バレットパンチ")
    check("ダメージ計算: バレットパンチ", _d_バレットパンチ > 0, f"dmg={_d_バレットパンチ}")
# バレットパンチ: 優先度1
_mv_pr_バレットパンチ = dl.get_move("バレットパンチ")
if _mv_pr_バレットパンチ and _mv_pr_バレットパンチ.priority == 1:
    check("優先度1: バレットパンチ", _mv_pr_バレットパンチ.priority == 1)
elif _mv_pr_バレットパンチ:
    check("優先度1: バレットパンチ", _mv_pr_バレットパンチ.priority == 1, f"DB優先度={_mv_pr_バレットパンチ.priority} 仕様=1")

# ── わるだくみ ──
check("DB: わるだくみ 取得可能", dl.get_move("わるだくみ") is not None)
# わるだくみ: 自分特攻+2
_mv_sb_わるだくみ_sp_attack = dl.get_move("わるだくみ")
if _mv_sb_わるだくみ_sp_attack:
    _pa_sb = make_poke(type1="あく"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "わるだくみ")
    check("自分特攻+2: わるだくみ", _pa_sb.stage_sp_attack == 2, f"1回適用={_pa_sb.stage_sp_attack} 期待=+2")
# わるだくみ: 自分特攻+2
_mvss_わるだくみ_sp_attack = dl.get_move("わるだくみ")
if _mvss_わるだくみ_sp_attack:
    random.seed(0); _got_わるだくみ_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="あく", atk_b=60, spatk_b=60); _pds = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "わるだくみ")
        if _pas.stage_sp_attack != 0: _got_わるだくみ_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻+2: わるだくみ", _got_わるだくみ_sp_attack == 2, f"1回適用={_got_わるだくみ_sp_attack} 期待=2")

# ── すりかえ ──
check("DB: すりかえ 取得可能", dl.get_move("すりかえ") is not None)
# すりかえ: 道具交換（メガストーンは失敗）
_psrk = make_poke(type1="エスパー", item="こだわりメガネ"); _dsrk = make_poke(type1="ノーマル", item="オボンのみ")
execute(_psrk, _dsrk, "すりかえ")
check("道具入替: すりかえ", _psrk.item == "オボンのみ" and _dsrk.item == "こだわりメガネ", f"atk={_psrk.item} def={_dsrk.item}")
# 相手がメガストーンを持つ場合は失敗
_psrk2 = make_poke(type1="エスパー", item="こだわりメガネ"); _dsrk2 = make_poke(type1="ノーマル", item="ガブリアスナイト")
execute(_psrk2, _dsrk2, "すりかえ")
check("メガストーン交換失敗: すりかえ", _psrk2.item == "こだわりメガネ" and _dsrk2.item == "ガブリアスナイト", f"atk={_psrk2.item} def={_dsrk2.item}")

# ── ゆきなだれ ──
check("DB: ゆきなだれ 取得可能", dl.get_move("ゆきなだれ") is not None)
_mv_ゆきなだれ = dl.get_move("ゆきなだれ")
if _mv_ゆきなだれ:
    _pa_ゆきなだれ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_ゆきなだれ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ゆきなだれ = dmg(_pa_ゆきなだれ, _pd_ゆきなだれ, "ゆきなだれ")
    check("ダメージ計算: ゆきなだれ", _d_ゆきなだれ > 0, f"dmg={_d_ゆきなだれ}")
# ゆきなだれ: 優先度-4
_mv_pr_ゆきなだれ = dl.get_move("ゆきなだれ")
if _mv_pr_ゆきなだれ and _mv_pr_ゆきなだれ.priority == -4:
    check("優先度-4: ゆきなだれ", _mv_pr_ゆきなだれ.priority == -4)
elif _mv_pr_ゆきなだれ:
    check("優先度-4: ゆきなだれ", _mv_pr_ゆきなだれ.priority == -4, f"DB優先度={_mv_pr_ゆきなだれ.priority} 仕様=-4")
# ゆきなだれ: 優先度-4。被弾していれば威力2倍（実戦の被弾フラグも検証）
_pcd = make_poke(type1="こおり", atk_b=100, spatk_b=100); _dcd = make_poke(type1="くさ", def_b=100, spdef_b=100)
_p_base = _ep(_pcd, _dcd, dl.get_move("ゆきなだれ"), BattleField())
_pcd._took_damage_this_turn = True
_p_cond = _ep(_pcd, _dcd, dl.get_move("ゆきなだれ"), BattleField())
check("条件成立で威力2倍: ゆきなだれ", _p_cond == _p_base * 2, f"base={_p_base} cond={_p_cond}")
# 実戦: 攻撃技を受けると _took_damage_this_turn が立つ（フラグ自体が機能するか）
_pyk = make_poke(type1="こおり", hp_b=255); _pyk._took_damage_this_turn = False
execute(make_poke(type1="ノーマル", atk_b=120, moves=["のしかかり"]), _pyk, "のしかかり")
check("被弾フラグ実機能: ゆきなだれ", _pyk._took_damage_this_turn, "攻撃を受けたら被弾フラグが立つこと")

# ── こおりのつぶて ──
check("DB: こおりのつぶて 取得可能", dl.get_move("こおりのつぶて") is not None)
_mv_こおりのつぶて = dl.get_move("こおりのつぶて")
if _mv_こおりのつぶて:
    _pa_こおりのつぶて = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_こおりのつぶて = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_こおりのつぶて = dmg(_pa_こおりのつぶて, _pd_こおりのつぶて, "こおりのつぶて")
    check("ダメージ計算: こおりのつぶて", _d_こおりのつぶて > 0, f"dmg={_d_こおりのつぶて}")
# こおりのつぶて: 優先度1
_mv_pr_こおりのつぶて = dl.get_move("こおりのつぶて")
if _mv_pr_こおりのつぶて and _mv_pr_こおりのつぶて.priority == 1:
    check("優先度1: こおりのつぶて", _mv_pr_こおりのつぶて.priority == 1)
elif _mv_pr_こおりのつぶて:
    check("優先度1: こおりのつぶて", _mv_pr_こおりのつぶて.priority == 1, f"DB優先度={_mv_pr_こおりのつぶて.priority} 仕様=1")

# ── ギガインパクト ──
check("DB: ギガインパクト 取得可能", dl.get_move("ギガインパクト") is not None)
_mv_ギガインパクト = dl.get_move("ギガインパクト")
if _mv_ギガインパクト:
    _pa_ギガインパクト = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ギガインパクト = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ギガインパクト = dmg(_pa_ギガインパクト, _pd_ギガインパクト, "ギガインパクト")
    check("ダメージ計算: ギガインパクト", _d_ギガインパクト > 0, f"dmg={_d_ギガインパクト}")
# ギガインパクト: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="ノーマル", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "ギガインパクト")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: ギガインパクト", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="ノーマル", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "ギガインパクト")
check("リチャージ中行動不能: ギガインパクト", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── かみなりのキバ ──
check("DB: かみなりのキバ 取得可能", dl.get_move("かみなりのキバ") is not None)
_mv_かみなりのキバ = dl.get_move("かみなりのキバ")
if _mv_かみなりのキバ:
    _pa_かみなりのキバ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_かみなりのキバ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_かみなりのキバ = dmg(_pa_かみなりのキバ, _pd_かみなりのキバ, "かみなりのキバ")
    check("ダメージ計算: かみなりのキバ", _d_かみなりのキバ > 0, f"dmg={_d_かみなりのキバ}")
# かみなりのキバ: まひ10%
_mv_s_かみなりのキバ = dl.get_move("かみなりのキバ")
if _mv_s_かみなりのキバ:
    random.seed(0); _hit_かみなりのキバ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "かみなりのキバ")
        _hit_かみなりのキバ += int((_pd2.status == "paralysis"))
    check("追加効果(まひ10%): かみなりのキバ", 9 <= _hit_かみなりのキバ <= 66, f"count={_hit_かみなりのキバ}/300")
    random.seed(1); _immok_かみなりのキバ = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "かみなりのキバ")
        if _pdi.status == "paralysis": _immok_かみなりのキバ = False; break
    check("まひ免疫(でんき型には無効): かみなりのキバ", _immok_かみなりのキバ, "免疫タイプに状態異常が付与されないこと")
# かみなりのキバ: ひるみ10%
_mv_f_かみなりのキバ = dl.get_move("かみなりのキバ")
if _mv_f_かみなりのキバ:
    random.seed(1); _fh_かみなりのキバ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "かみなりのキバ"); _fh_かみなりのキバ += int(_pd3.flinched)
    check("ひるみ(10%): かみなりのキバ", 9 <= _fh_かみなりのキバ <= 66, f"count={_fh_かみなりのキバ}/300")

# ── シャドークロー ──
check("DB: シャドークロー 取得可能", dl.get_move("シャドークロー") is not None)
_mv_シャド_クロ_ = dl.get_move("シャドークロー")
if _mv_シャド_クロ_:
    _pa_シャド_クロ_ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_シャド_クロ_ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_シャド_クロ_ = dmg(_pa_シャド_クロ_, _pd_シャド_クロ_, "シャドークロー")
    check("ダメージ計算: シャドークロー", _d_シャド_クロ_ > 0, f"dmg={_d_シャド_クロ_}")
# シャドークロー: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_シャド_クロ_
random.seed(0); _hc_crit_シャド_クロ_ = 0; _phc = make_poke(type1="ゴースト")
_mvhc_シャド_クロ_ = dl.get_move("シャドークロー")
for _ in range(800):
    if _cc_シャド_クロ_(_phc, _mvhc_シャド_クロ_, make_poke(type1="エスパー")): _hc_crit_シャド_クロ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: シャドークロー", 60 <= _hc_crit_シャド_クロ_ <= 150, f"crit={_hc_crit_シャド_クロ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── こおりのキバ ──
check("DB: こおりのキバ 取得可能", dl.get_move("こおりのキバ") is not None)
_mv_こおりのキバ = dl.get_move("こおりのキバ")
if _mv_こおりのキバ:
    _pa_こおりのキバ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_こおりのキバ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_こおりのキバ = dmg(_pa_こおりのキバ, _pd_こおりのキバ, "こおりのキバ")
    check("ダメージ計算: こおりのキバ", _d_こおりのキバ > 0, f"dmg={_d_こおりのキバ}")
# こおりのキバ: こおり10%
_mv_s_こおりのキバ = dl.get_move("こおりのキバ")
if _mv_s_こおりのキバ:
    random.seed(0); _hit_こおりのキバ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "こおりのキバ")
        _hit_こおりのキバ += int((_pd2.status == "freeze"))
    check("追加効果(こおり10%): こおりのキバ", 9 <= _hit_こおりのキバ <= 66, f"count={_hit_こおりのキバ}/300")
    random.seed(1); _immok_こおりのキバ = True
    for _ in range(60):
        _pai = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pdi = make_poke(type1="こおり", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "こおりのキバ")
        if _pdi.status == "freeze": _immok_こおりのキバ = False; break
    check("こおり免疫(こおり型には無効): こおりのキバ", _immok_こおりのキバ, "免疫タイプに状態異常が付与されないこと")
# こおりのキバ: ひるみ10%
_mv_f_こおりのキバ = dl.get_move("こおりのキバ")
if _mv_f_こおりのキバ:
    random.seed(1); _fh_こおりのキバ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "こおりのキバ"); _fh_こおりのキバ += int(_pd3.flinched)
    check("ひるみ(10%): こおりのキバ", 9 <= _fh_こおりのキバ <= 66, f"count={_fh_こおりのキバ}/300")

# ── ほのおのキバ ──
check("DB: ほのおのキバ 取得可能", dl.get_move("ほのおのキバ") is not None)
_mv_ほのおのキバ = dl.get_move("ほのおのキバ")
if _mv_ほのおのキバ:
    _pa_ほのおのキバ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ほのおのキバ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ほのおのキバ = dmg(_pa_ほのおのキバ, _pd_ほのおのキバ, "ほのおのキバ")
    check("ダメージ計算: ほのおのキバ", _d_ほのおのキバ > 0, f"dmg={_d_ほのおのキバ}")
# ほのおのキバ: やけど10%
_mv_s_ほのおのキバ = dl.get_move("ほのおのキバ")
if _mv_s_ほのおのキバ:
    random.seed(0); _hit_ほのおのキバ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ほのおのキバ")
        _hit_ほのおのキバ += int((_pd2.status == "burn"))
    check("追加効果(やけど10%): ほのおのキバ", 9 <= _hit_ほのおのキバ <= 66, f"count={_hit_ほのおのキバ}/300")
    random.seed(1); _immok_ほのおのキバ = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ほのおのキバ")
        if _pdi.status == "burn": _immok_ほのおのキバ = False; break
    check("やけど免疫(ほのお型には無効): ほのおのキバ", _immok_ほのおのキバ, "免疫タイプに状態異常が付与されないこと")
# ほのおのキバ: ひるみ10%
_mv_f_ほのおのキバ = dl.get_move("ほのおのキバ")
if _mv_f_ほのおのキバ:
    random.seed(1); _fh_ほのおのキバ = 0
    for _ in range(300):
        _pa3 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "ほのおのキバ"); _fh_ほのおのキバ += int(_pd3.flinched)
    check("ひるみ(10%): ほのおのキバ", 9 <= _fh_ほのおのキバ <= 66, f"count={_fh_ほのおのキバ}/300")

# ── かげうち ──
check("DB: かげうち 取得可能", dl.get_move("かげうち") is not None)
_mv_かげうち = dl.get_move("かげうち")
if _mv_かげうち:
    _pa_かげうち = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_かげうち = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_かげうち = dmg(_pa_かげうち, _pd_かげうち, "かげうち")
    check("ダメージ計算: かげうち", _d_かげうち > 0, f"dmg={_d_かげうち}")
# かげうち: 優先度1
_mv_pr_かげうち = dl.get_move("かげうち")
if _mv_pr_かげうち and _mv_pr_かげうち.priority == 1:
    check("優先度1: かげうち", _mv_pr_かげうち.priority == 1)
elif _mv_pr_かげうち:
    check("優先度1: かげうち", _mv_pr_かげうち.priority == 1, f"DB優先度={_mv_pr_かげうち.priority} 仕様=1")

# ── サイコカッター ──
check("DB: サイコカッター 取得可能", dl.get_move("サイコカッター") is not None)
_mv_サイコカッタ_ = dl.get_move("サイコカッター")
if _mv_サイコカッタ_:
    _pa_サイコカッタ_ = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_サイコカッタ_ = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_サイコカッタ_ = dmg(_pa_サイコカッタ_, _pd_サイコカッタ_, "サイコカッター")
    check("ダメージ計算: サイコカッター", _d_サイコカッタ_ > 0, f"dmg={_d_サイコカッタ_}")
# サイコカッター: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_サイコカッタ_
random.seed(0); _hc_crit_サイコカッタ_ = 0; _phc = make_poke(type1="エスパー")
_mvhc_サイコカッタ_ = dl.get_move("サイコカッター")
for _ in range(800):
    if _cc_サイコカッタ_(_phc, _mvhc_サイコカッタ_, make_poke(type1="かくとう")): _hc_crit_サイコカッタ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: サイコカッター", 60 <= _hc_crit_サイコカッタ_ <= 150, f"crit={_hc_crit_サイコカッタ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── しねんのずつき ──
check("DB: しねんのずつき 取得可能", dl.get_move("しねんのずつき") is not None)
_mv_しねんのずつき = dl.get_move("しねんのずつき")
if _mv_しねんのずつき:
    _pa_しねんのずつき = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_しねんのずつき = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_しねんのずつき = dmg(_pa_しねんのずつき, _pd_しねんのずつき, "しねんのずつき")
    check("ダメージ計算: しねんのずつき", _d_しねんのずつき > 0, f"dmg={_d_しねんのずつき}")
# しねんのずつき: ひるみ20%
_mv_f_しねんのずつき = dl.get_move("しねんのずつき")
if _mv_f_しねんのずつき:
    random.seed(1); _fh_しねんのずつき = 0
    for _ in range(300):
        _pa3 = make_poke(type1="エスパー", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="かくとう", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "しねんのずつき"); _fh_しねんのずつき += int(_pd3.flinched)
    check("ひるみ(20%): しねんのずつき", 18 <= _fh_しねんのずつき <= 117, f"count={_fh_しねんのずつき}/300")

# ── ラスターカノン ──
check("DB: ラスターカノン 取得可能", dl.get_move("ラスターカノン") is not None)
_mv_ラスタ_カノン = dl.get_move("ラスターカノン")
if _mv_ラスタ_カノン:
    _pa_ラスタ_カノン = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_ラスタ_カノン = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_ラスタ_カノン = dmg(_pa_ラスタ_カノン, _pd_ラスタ_カノン, "ラスターカノン")
    check("ダメージ計算: ラスターカノン", _d_ラスタ_カノン > 0, f"dmg={_d_ラスタ_カノン}")
# ラスターカノン: 相手特防-1
_mv_dd_ラスタ_カノン = dl.get_move("ラスターカノン")
if _mv_dd_ラスタ_カノン:
    _pa_dd = make_poke(type1="はがね", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ラスタ_カノン = 0; _dd_ok_ラスタ_カノン = False
    for _ in range(60):
        _pd_dd = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ラスターカノン")
        if _pd_dd.stage_sp_defense != 0: _dd_val_ラスタ_カノン = _pd_dd.stage_sp_defense; _dd_ok_ラスタ_カノン = True; break
    check("相手特防-1: ラスターカノン", _dd_ok_ラスタ_カノン and _dd_val_ラスタ_カノン == -1, f"1回適用={_dd_val_ラスタ_カノン} 期待=-1")

# ── トリックルーム ──
check("DB: トリックルーム 取得可能", dl.get_move("トリックルーム") is not None)
# トリックルーム: 場の状態セット
_s1rm, _s2rm, _frm = execute_ctx(make_poke(type1="エスパー"), make_poke(), "トリックルーム")
check("トリックルーム 場の状態: トリックルーム", bool(getattr(_frm, "trick_room", 0)))

# ── がんせきほう ──
check("DB: がんせきほう 取得可能", dl.get_move("がんせきほう") is not None)
_mv_がんせきほう = dl.get_move("がんせきほう")
if _mv_がんせきほう:
    _pa_がんせきほう = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_がんせきほう = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_がんせきほう = dmg(_pa_がんせきほう, _pd_がんせきほう, "がんせきほう")
    check("ダメージ計算: がんせきほう", _d_がんせきほう > 0, f"dmg={_d_がんせきほう}")
# がんせきほう: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="いわ", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="ひこう", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "がんせきほう")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: がんせきほう", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="いわ", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="ひこう", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "がんせきほう")
check("リチャージ中行動不能: がんせきほう", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── りゅうせいぐん ──
check("DB: りゅうせいぐん 取得可能", dl.get_move("りゅうせいぐん") is not None)
_mv_りゅうせいぐん = dl.get_move("りゅうせいぐん")
if _mv_りゅうせいぐん:
    _pa_りゅうせいぐん = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_りゅうせいぐん = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_りゅうせいぐん = dmg(_pa_りゅうせいぐん, _pd_りゅうせいぐん, "りゅうせいぐん")
    check("ダメージ計算: りゅうせいぐん", _d_りゅうせいぐん > 0, f"dmg={_d_りゅうせいぐん}")
# りゅうせいぐん: 自分特攻-2
_mvss_りゅうせいぐん_sp_attack = dl.get_move("りゅうせいぐん")
if _mvss_りゅうせいぐん_sp_attack:
    random.seed(0); _got_りゅうせいぐん_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="ドラゴン", atk_b=60, spatk_b=60); _pds = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "りゅうせいぐん")
        if _pas.stage_sp_attack != 0: _got_りゅうせいぐん_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻-2: りゅうせいぐん", _got_りゅうせいぐん_sp_attack == -2, f"1回適用={_got_りゅうせいぐん_sp_attack} 期待=-2")
# りゅうせいぐん: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="ドラゴン", atk_b=120, spatk_b=120); _dsd = make_poke(type1="ドラゴン", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "りゅうせいぐん")
    if _psd.stage_sp_attack < 0: break
check("自分特攻下降: りゅうせいぐん", _psd.stage_sp_attack < 0, f"stage={_psd.stage_sp_attack}")

# ── パワーウィップ ──
check("DB: パワーウィップ 取得可能", dl.get_move("パワーウィップ") is not None)
_mv_パワ_ウィップ = dl.get_move("パワーウィップ")
if _mv_パワ_ウィップ:
    _pa_パワ_ウィップ = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_パワ_ウィップ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_パワ_ウィップ = dmg(_pa_パワ_ウィップ, _pd_パワ_ウィップ, "パワーウィップ")
    check("ダメージ計算: パワーウィップ", _d_パワ_ウィップ > 0, f"dmg={_d_パワ_ウィップ}")

# ── リーフストーム ──
check("DB: リーフストーム 取得可能", dl.get_move("リーフストーム") is not None)
_mv_リ_フスト_ム = dl.get_move("リーフストーム")
if _mv_リ_フスト_ム:
    _pa_リ_フスト_ム = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_リ_フスト_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_リ_フスト_ム = dmg(_pa_リ_フスト_ム, _pd_リ_フスト_ム, "リーフストーム")
    check("ダメージ計算: リーフストーム", _d_リ_フスト_ム > 0, f"dmg={_d_リ_フスト_ム}")
# リーフストーム: 自分特攻-2
_mvss_リ_フスト_ム_sp_attack = dl.get_move("リーフストーム")
if _mvss_リ_フスト_ム_sp_attack:
    random.seed(0); _got_リ_フスト_ム_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="くさ", atk_b=60, spatk_b=60); _pds = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "リーフストーム")
        if _pas.stage_sp_attack != 0: _got_リ_フスト_ム_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻-2: リーフストーム", _got_リ_フスト_ム_sp_attack == -2, f"1回適用={_got_リ_フスト_ム_sp_attack} 期待=-2")
# リーフストーム: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsd = make_poke(type1="みず", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "リーフストーム")
    if _psd.stage_sp_attack < 0: break
check("自分特攻下降: リーフストーム", _psd.stage_sp_attack < 0, f"stage={_psd.stage_sp_attack}")

# ── ふんえん ──
check("DB: ふんえん 取得可能", dl.get_move("ふんえん") is not None)
_mv_ふんえん = dl.get_move("ふんえん")
if _mv_ふんえん:
    _pa_ふんえん = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ふんえん = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ふんえん = dmg(_pa_ふんえん, _pd_ふんえん, "ふんえん")
    check("ダメージ計算: ふんえん", _d_ふんえん > 0, f"dmg={_d_ふんえん}")
# ふんえん: やけど30%
_mv_s_ふんえん = dl.get_move("ふんえん")
if _mv_s_ふんえん:
    random.seed(0); _hit_ふんえん = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ふんえん")
        _hit_ふんえん += int((_pd2.status == "burn"))
    check("追加効果(やけど30%): ふんえん", 27 <= _hit_ふんえん <= 168, f"count={_hit_ふんえん}/300")
    random.seed(1); _immok_ふんえん = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ふんえん")
        if _pdi.status == "burn": _immok_ふんえん = False; break
    check("やけど免疫(ほのお型には無効): ふんえん", _immok_ふんえん, "免疫タイプに状態異常が付与されないこと")

# ── きりばらい ──
check("DB: きりばらい 取得可能", dl.get_move("きりばらい") is not None)
# きりばらい: 相手回避率-1
_mv_dd_きりばらい = dl.get_move("きりばらい")
if _mv_dd_きりばらい:
    _pa_dd = make_poke(type1="ひこう", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_きりばらい = 0; _dd_ok_きりばらい = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "きりばらい")
        if _pd_dd.stage_evasion != 0: _dd_val_きりばらい = _pd_dd.stage_evasion; _dd_ok_きりばらい = True; break
    check("相手回避率-1: きりばらい", _dd_ok_きりばらい and _dd_val_きりばらい == -1, f"1回適用={_dd_val_きりばらい} 期待=-1")

# ── ほうでん ──
check("DB: ほうでん 取得可能", dl.get_move("ほうでん") is not None)
_mv_ほうでん = dl.get_move("ほうでん")
if _mv_ほうでん:
    _pa_ほうでん = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ほうでん = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ほうでん = dmg(_pa_ほうでん, _pd_ほうでん, "ほうでん")
    check("ダメージ計算: ほうでん", _d_ほうでん > 0, f"dmg={_d_ほうでん}")
# ほうでん: まひ30%
_mv_s_ほうでん = dl.get_move("ほうでん")
if _mv_s_ほうでん:
    random.seed(0); _hit_ほうでん = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ほうでん")
        _hit_ほうでん += int((_pd2.status == "paralysis"))
    check("追加効果(まひ30%): ほうでん", 27 <= _hit_ほうでん <= 168, f"count={_hit_ほうでん}/300")
    random.seed(1); _immok_ほうでん = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ほうでん")
        if _pdi.status == "paralysis": _immok_ほうでん = False; break
    check("まひ免疫(でんき型には無効): ほうでん", _immok_ほうでん, "免疫タイプに状態異常が付与されないこと")

# ── ダストシュート ──
check("DB: ダストシュート 取得可能", dl.get_move("ダストシュート") is not None)
_mv_ダストシュ_ト = dl.get_move("ダストシュート")
if _mv_ダストシュ_ト:
    _pa_ダストシュ_ト = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_ダストシュ_ト = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ダストシュ_ト = dmg(_pa_ダストシュ_ト, _pd_ダストシュ_ト, "ダストシュート")
    check("ダメージ計算: ダストシュート", _d_ダストシュ_ト > 0, f"dmg={_d_ダストシュ_ト}")
# ダストシュート: どく30%
_mv_s_ダストシュ_ト = dl.get_move("ダストシュート")
if _mv_s_ダストシュ_ト:
    random.seed(0); _hit_ダストシュ_ト = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ダストシュート")
        _hit_ダストシュ_ト += int((_pd2.status == "poison"))
    check("追加効果(どく30%): ダストシュート", 27 <= _hit_ダストシュ_ト <= 168, f"count={_hit_ダストシュ_ト}/300")
    random.seed(1); _immok_ダストシュ_ト = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ダストシュート")
        if _pdi.status == "poison": _immok_ダストシュ_ト = False; break
    check("どく免疫(どく型には無効): ダストシュート", _immok_ダストシュ_ト, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_ダストシュ_ト = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ダストシュート")
        if _pdi.status == "poison": _immok_ダストシュ_ト = False; break
    check("どく免疫(はがね型には無効): ダストシュート", _immok_ダストシュ_ト, "免疫タイプに状態異常が付与されないこと")

# ── アイアンヘッド ──
check("DB: アイアンヘッド 取得可能", dl.get_move("アイアンヘッド") is not None)
_mv_アイアンヘッド = dl.get_move("アイアンヘッド")
if _mv_アイアンヘッド:
    _pa_アイアンヘッド = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_アイアンヘッド = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_アイアンヘッド = dmg(_pa_アイアンヘッド, _pd_アイアンヘッド, "アイアンヘッド")
    check("ダメージ計算: アイアンヘッド", _d_アイアンヘッド > 0, f"dmg={_d_アイアンヘッド}")
# アイアンヘッド: ひるみ20%
_mv_f_アイアンヘッド = dl.get_move("アイアンヘッド")
if _mv_f_アイアンヘッド:
    random.seed(1); _fh_アイアンヘッド = 0
    for _ in range(300):
        _pa3 = make_poke(type1="はがね", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="こおり", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "アイアンヘッド"); _fh_アイアンヘッド += int(_pd3.flinched)
    check("ひるみ(20%): アイアンヘッド", 18 <= _fh_アイアンヘッド <= 117, f"count={_fh_アイアンヘッド}/300")

# ── ストーンエッジ ──
check("DB: ストーンエッジ 取得可能", dl.get_move("ストーンエッジ") is not None)
_mv_スト_ンエッジ = dl.get_move("ストーンエッジ")
if _mv_スト_ンエッジ:
    _pa_スト_ンエッジ = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_スト_ンエッジ = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_スト_ンエッジ = dmg(_pa_スト_ンエッジ, _pd_スト_ンエッジ, "ストーンエッジ")
    check("ダメージ計算: ストーンエッジ", _d_スト_ンエッジ > 0, f"dmg={_d_スト_ンエッジ}")
# ストーンエッジ: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_スト_ンエッジ
random.seed(0); _hc_crit_スト_ンエッジ = 0; _phc = make_poke(type1="いわ")
_mvhc_スト_ンエッジ = dl.get_move("ストーンエッジ")
for _ in range(800):
    if _cc_スト_ンエッジ(_phc, _mvhc_スト_ンエッジ, make_poke(type1="ひこう")): _hc_crit_スト_ンエッジ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: ストーンエッジ", 60 <= _hc_crit_スト_ンエッジ <= 150, f"crit={_hc_crit_スト_ンエッジ}/800 (期待≈100, 通常1/24なら≈33)")

# ── くさむすび ──
check("DB: くさむすび 取得可能", dl.get_move("くさむすび") is not None)
# くさむすび: 相手の重さ別の威力テーブル（20/40/60/80/100/120）
_pw_l = make_poke(type1="くさ", atk_b=100, spatk_b=100)
_kg_ng = []
for _w, _exp in [(5,20),(15,40),(35,60),(75,80),(150,100),(300,120)]:
    _dkg = make_poke(type1="みず"); _dkg.weight_kg = float(_w)
    _got = _ep(_pw_l, _dkg, dl.get_move("くさむすび"), BattleField())
    if _got != _exp: _kg_ng.append(f"{_w}kg:{_got}!={_exp}")
check("重さ別威力テーブル: くさむすび", not _kg_ng, f"NG={_kg_ng}")

# ── ステルスロック ──
check("DB: ステルスロック 取得可能", dl.get_move("ステルスロック") is not None)
# ステルスロック: ハザードstealth_rock
_mvhz_ステルスロック = dl.get_move("ステルスロック")
if _mvhz_ステルスロック:
    _s1h, _s2h, _fh2 = execute_ctx(make_poke(type1="いわ"), make_poke(), "ステルスロック")
    _hzval = _fh2.stealth_rock[_s2h.field_idx] or getattr(_s2h, "_stealth_rock_pending", False) or _s2h.stealth_rock_set
    check("ハザードstealth_rock: ステルスロック", bool(_hzval), f"val={_hzval}")

# ── むしくい ──
check("DB: むしくい 取得可能", dl.get_move("むしくい") is not None)
_mv_むしくい = dl.get_move("むしくい")
if _mv_むしくい:
    _pa_むしくい = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_むしくい = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_むしくい = dmg(_pa_むしくい, _pd_むしくい, "むしくい")
    check("ダメージ計算: むしくい", _d_むしくい > 0, f"dmg={_d_むしくい}")
# むしくい: 相手のきのみを食べ効果を得る（オボンのみで自分回復）
_ppk = make_poke(type1="むし", atk_b=80); _ppk.hp = _ppk.max_hp // 2
_dpk = make_poke(type1="くさ", hp_b=255, def_b=200, item="オボンのみ")
_hp_ppk = _ppk.hp; execute(_ppk, _dpk, "むしくい")
check("きのみ奪取: むしくい", _dpk.item is None and _ppk.hp > _hp_ppk, f"foeItem={_dpk.item} hp={_ppk.hp}/{_hp_ppk}")
# effect_textに無い余計な追加効果がないこと（きのみ無しの相手に能力変化等が起きない）
_dpk2 = make_poke(type1="くさ", hp_b=255, def_b=200); _rng_noextra = 0
import random as _rnx; _rnx.seed(0)
for _ in range(30): execute(make_poke(type1="むし", atk_b=10), _dpk2, "むしくい")
_stg2 = [getattr(_dpk2, _s, 0) for _s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed")]
check("余計な追加効果なし: むしくい", all(_v == 0 for _v in _stg2) and _dpk2.status is None, f"stages={_stg2} status={_dpk2.status}")

# ── ウッドハンマー ──
check("DB: ウッドハンマー 取得可能", dl.get_move("ウッドハンマー") is not None)
_mv_ウッドハンマ_ = dl.get_move("ウッドハンマー")
if _mv_ウッドハンマ_:
    _pa_ウッドハンマ_ = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ウッドハンマ_ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ウッドハンマ_ = dmg(_pa_ウッドハンマ_, _pd_ウッドハンマ_, "ウッドハンマー")
    check("ダメージ計算: ウッドハンマー", _d_ウッドハンマ_ > 0, f"dmg={_d_ウッドハンマ_}")
# ウッドハンマー: 反動（与ダメの1/3）
_mvrc_ウッドハンマ_ = dl.get_move("ウッドハンマー")
if _mvrc_ウッドハンマ_:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="くさ", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="みず", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "ウッドハンマー")
        _rc_dealt_ウッドハンマ_ = _hpdr - _pdr.hp; _rc_rcv_ウッドハンマ_ = _par.max_hp - _par.hp
        if _rc_dealt_ウッドハンマ_ > 0: break
    _rc_exp_ウッドハンマ_ = max(1, _rc_dealt_ウッドハンマ_ // 3)
    check("反動ダメージ(1/3): ウッドハンマー", abs(_rc_rcv_ウッドハンマ_ - _rc_exp_ウッドハンマ_) <= 2, f"dealt={_rc_dealt_ウッドハンマ_} recoil={_rc_rcv_ウッドハンマ_} 期待={_rc_exp_ウッドハンマ_}")

# ── アクアジェット ──
check("DB: アクアジェット 取得可能", dl.get_move("アクアジェット") is not None)
_mv_アクアジェット = dl.get_move("アクアジェット")
if _mv_アクアジェット:
    _pa_アクアジェット = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_アクアジェット = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_アクアジェット = dmg(_pa_アクアジェット, _pd_アクアジェット, "アクアジェット")
    check("ダメージ計算: アクアジェット", _d_アクアジェット > 0, f"dmg={_d_アクアジェット}")
# アクアジェット: 優先度1
_mv_pr_アクアジェット = dl.get_move("アクアジェット")
if _mv_pr_アクアジェット and _mv_pr_アクアジェット.priority == 1:
    check("優先度1: アクアジェット", _mv_pr_アクアジェット.priority == 1)
elif _mv_pr_アクアジェット:
    check("優先度1: アクアジェット", _mv_pr_アクアジェット.priority == 1, f"DB優先度={_mv_pr_アクアジェット.priority} 仕様=1")

# ── もろはのずつき ──
check("DB: もろはのずつき 取得可能", dl.get_move("もろはのずつき") is not None)
_mv_もろはのずつき = dl.get_move("もろはのずつき")
if _mv_もろはのずつき:
    _pa_もろはのずつき = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_もろはのずつき = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_もろはのずつき = dmg(_pa_もろはのずつき, _pd_もろはのずつき, "もろはのずつき")
    check("ダメージ計算: もろはのずつき", _d_もろはのずつき > 0, f"dmg={_d_もろはのずつき}")
# もろはのずつき: 反動（与ダメの1/2）
_mvrc_もろはのずつき = dl.get_move("もろはのずつき")
if _mvrc_もろはのずつき:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="いわ", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="ひこう", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "もろはのずつき")
        _rc_dealt_もろはのずつき = _hpdr - _pdr.hp; _rc_rcv_もろはのずつき = _par.max_hp - _par.hp
        if _rc_dealt_もろはのずつき > 0: break
    _rc_exp_もろはのずつき = max(1, _rc_dealt_もろはのずつき // 2)
    check("反動ダメージ(1/2): もろはのずつき", abs(_rc_rcv_もろはのずつき - _rc_exp_もろはのずつき) <= 2, f"dealt={_rc_dealt_もろはのずつき} recoil={_rc_rcv_もろはのずつき} 期待={_rc_exp_もろはのずつき}")

# ── サイコショック ──
check("DB: サイコショック 取得可能", dl.get_move("サイコショック") is not None)
_mv_サイコショック = dl.get_move("サイコショック")
if _mv_サイコショック:
    _pa_サイコショック = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_サイコショック = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_サイコショック = dmg(_pa_サイコショック, _pd_サイコショック, "サイコショック")
    check("ダメージ計算: サイコショック", _d_サイコショック > 0, f"dmg={_d_サイコショック}")
# サイコショック: 相手の物理防御でダメージ計算
_pps = make_poke(type1="エスパー", spatk_b=100)
_dps_hb = make_poke(type1="ノーマル", def_b=250, spdef_b=10)
_dps_lb = make_poke(type1="ノーマル", def_b=10, spdef_b=250)
_d_hb = calc_damage(_pps, _dps_hb, dl.get_move("サイコショック"), BattleField(), random_roll=1.0)
_d_lb = calc_damage(_pps, _dps_lb, dl.get_move("サイコショック"), BattleField(), random_roll=1.0)
check("サイコショック 物理防御依存: サイコショック", _d_hb < _d_lb, f"highB={_d_hb} lowB={_d_lb}")

# ── いかりのこな ──
check("DB: いかりのこな 取得可能", dl.get_move("いかりのこな") is not None)
# いかりのこな: 優先度2
_mv_pr_いかりのこな = dl.get_move("いかりのこな")
if _mv_pr_いかりのこな and _mv_pr_いかりのこな.priority == 2:
    check("優先度2: いかりのこな", _mv_pr_いかりのこな.priority == 2)
elif _mv_pr_いかりのこな:
    check("優先度2: いかりのこな", _mv_pr_いかりのこな.priority == 2, f"DB優先度={_mv_pr_いかりのこな.priority} 仕様=2")
# いかりのこな: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: いかりのこな", "いかりのこな", "むし", False, smoke=("いかりのこな" in DOUBLE_ONLY_SMOKE))

# ── うちおとす ──
check("DB: うちおとす 取得可能", dl.get_move("うちおとす") is not None)
_mv_うちおとす = dl.get_move("うちおとす")
if _mv_うちおとす:
    _pa_うちおとす = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_うちおとす = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_うちおとす = dmg(_pa_うちおとす, _pd_うちおとす, "うちおとす")
    check("ダメージ計算: うちおとす", _d_うちおとす > 0, f"dmg={_d_うちおとす}")
# うちおとす: ひこう/ふゆう/でんじふゆうを接地させ、じめん技が当たるようになる
_pud = make_poke(type1="いわ", atk_b=100); _dud = make_poke(type1="ひこう", hp_b=255, def_b=120)
_jground = make_poke(type1="じめん", atk_b=120)
_before = dmg(_jground, _dud, "じしん")
execute(_pud, _dud, "うちおとす")
_after = dmg(_jground, _dud, "じしん")
check("接地化: うちおとす", _before == 0 and _after > 0 and _dud.grounded, f"before={_before} after={_after} grounded={_dud.grounded}")
# でんじふゆうも接地で解除
_dud2 = make_poke(type1="でんき", hp_b=255, def_b=120); _dud2.magnet_rise = True
execute(make_poke(type1="いわ", atk_b=100), _dud2, "うちおとす")
check("でんじふゆう解除: うちおとす", not _dud2.magnet_rise, f"magnet={_dud2.magnet_rise}")

# ── やまあらし ──
check("DB: やまあらし 取得可能", dl.get_move("やまあらし") is not None)
_mv_やまあらし = dl.get_move("やまあらし")
if _mv_やまあらし:
    _pa_やまあらし = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_やまあらし = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_やまあらし = dmg(_pa_やまあらし, _pd_やまあらし, "やまあらし")
    check("ダメージ計算: やまあらし", _d_やまあらし > 0, f"dmg={_d_やまあらし}")
# やまあらし: 必ず急所（高ダメージ）
_mvcr_やまあらし = dl.get_move("やまあらし")
if _mvcr_やまあらし:
    _pac = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _d_crit = dmg(_pac, make_poke(type1="ノーマル", def_b=100, spdef_b=100), "やまあらし")
    check("必ず急所(>0): やまあらし", _d_crit > 0)

# ── ヘドロウェーブ ──
check("DB: ヘドロウェーブ 取得可能", dl.get_move("ヘドロウェーブ") is not None)
_mv_ヘドロウェ_ブ = dl.get_move("ヘドロウェーブ")
if _mv_ヘドロウェ_ブ:
    _pa_ヘドロウェ_ブ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_ヘドロウェ_ブ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ヘドロウェ_ブ = dmg(_pa_ヘドロウェ_ブ, _pd_ヘドロウェ_ブ, "ヘドロウェーブ")
    check("ダメージ計算: ヘドロウェーブ", _d_ヘドロウェ_ブ > 0, f"dmg={_d_ヘドロウェ_ブ}")
# ヘドロウェーブ: どく10%
_mv_s_ヘドロウェ_ブ = dl.get_move("ヘドロウェーブ")
if _mv_s_ヘドロウェ_ブ:
    random.seed(0); _hit_ヘドロウェ_ブ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ヘドロウェーブ")
        _hit_ヘドロウェ_ブ += int((_pd2.status == "poison"))
    check("追加効果(どく10%): ヘドロウェーブ", 9 <= _hit_ヘドロウェ_ブ <= 66, f"count={_hit_ヘドロウェ_ブ}/300")
    random.seed(1); _immok_ヘドロウェ_ブ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ヘドロウェーブ")
        if _pdi.status == "poison": _immok_ヘドロウェ_ブ = False; break
    check("どく免疫(どく型には無効): ヘドロウェーブ", _immok_ヘドロウェ_ブ, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_ヘドロウェ_ブ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ヘドロウェーブ")
        if _pdi.status == "poison": _immok_ヘドロウェ_ブ = False; break
    check("どく免疫(はがね型には無効): ヘドロウェーブ", _immok_ヘドロウェ_ブ, "免疫タイプに状態異常が付与されないこと")

# ── みずびたし ──
check("DB: みずびたし 取得可能", dl.get_move("みずびたし") is not None)
# みずびたし: 相手を純みずタイプに変える（複合タイプでもtype2が消える）
_pmz = make_poke(); _dmz = make_poke(type1="ほのお", type2="ひこう"); execute(_pmz, _dmz, "みずびたし")
check("純みずタイプ化(type2消去): みずびたし", _dmz.type1 == "みず" and _dmz.type2 is None, f"t1={_dmz.type1} t2={_dmz.type2}")

# ── ヘビーボンバー ──
check("DB: ヘビーボンバー 取得可能", dl.get_move("ヘビーボンバー") is not None)
# ヘビーボンバー: 重さ比別の威力テーブル（≥5→120 ... 未満→40）
_pwh = make_poke(type1="はがね", atk_b=100); _pwh.weight_kg = 500.0
_hb_ng = []
for _wd, _exp in [(99,120),(125,100),(166,80),(250,60),(400,40)]:
    _dwh = make_poke(type1="こおり"); _dwh.weight_kg = float(_wd)
    _got = _ep(_pwh, _dwh, dl.get_move("ヘビーボンバー"), BattleField())
    if _got != _exp: _hb_ng.append(f"500/{_wd}kg:{_got}!={_exp}")
check("重さ比別威力テーブル: ヘビーボンバー", not _hb_ng, f"NG={_hb_ng}")
# ちいさくなる状態の相手に威力2倍（重さ比固定: 500/100kg→比5→威力120）
_dmm0 = make_poke(type1="こおり"); _dmm0.weight_kg = 100.0
_dmm1 = make_poke(type1="こおり"); _dmm1.weight_kg = 100.0; _dmm1.minimized = True
_mm_n = _ep(_pwh, _dmm0, dl.get_move("ヘビーボンバー"), BattleField()); _mm_m = _ep(_pwh, _dmm1, dl.get_move("ヘビーボンバー"), BattleField())
check("ちいさくなる2倍: ヘビーボンバー", _mm_m == _mm_n * 2, f"normal={_mm_n} mini={_mm_m}")

# ── ちょうのまい ──
check("DB: ちょうのまい 取得可能", dl.get_move("ちょうのまい") is not None)
# ちょうのまい: 自分特攻+1
_mv_sb_ちょうのまい_sp_attack = dl.get_move("ちょうのまい")
if _mv_sb_ちょうのまい_sp_attack:
    _pa_sb = make_poke(type1="むし"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ちょうのまい")
    check("自分特攻+1: ちょうのまい", _pa_sb.stage_sp_attack == 1, f"1回適用={_pa_sb.stage_sp_attack} 期待=+1")
# ちょうのまい: 自分特防+1
_mv_sb_ちょうのまい_sp_defense = dl.get_move("ちょうのまい")
if _mv_sb_ちょうのまい_sp_defense:
    _pa_sb = make_poke(type1="むし"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ちょうのまい")
    check("自分特防+1: ちょうのまい", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")
# ちょうのまい: 自分素早さ+1
_mv_sb_ちょうのまい_speed = dl.get_move("ちょうのまい")
if _mv_sb_ちょうのまい_speed:
    _pa_sb = make_poke(type1="むし"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ちょうのまい")
    check("自分素早さ+1: ちょうのまい", _pa_sb.stage_speed == 1, f"1回適用={_pa_sb.stage_speed} 期待=+1")

# ── とぐろをまく ──
check("DB: とぐろをまく 取得可能", dl.get_move("とぐろをまく") is not None)
# とぐろをまく: 自分攻撃+1
_mv_sb_とぐろをまく_attack = dl.get_move("とぐろをまく")
if _mv_sb_とぐろをまく_attack:
    _pa_sb = make_poke(type1="どく"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "とぐろをまく")
    check("自分攻撃+1: とぐろをまく", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# とぐろをまく: 自分防御+1
_mv_sb_とぐろをまく_defense = dl.get_move("とぐろをまく")
if _mv_sb_とぐろをまく_defense:
    _pa_sb = make_poke(type1="どく"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "とぐろをまく")
    check("自分防御+1: とぐろをまく", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")
# とぐろをまく: 自分命中率+1
_mv_sb_とぐろをまく_accuracy = dl.get_move("とぐろをまく")
if _mv_sb_とぐろをまく_accuracy:
    _pa_sb = make_poke(type1="どく"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "とぐろをまく")
    check("自分命中率+1: とぐろをまく", _pa_sb.stage_accuracy == 1, f"1回適用={_pa_sb.stage_accuracy} 期待=+1")

# ── ニトロチャージ ──
check("DB: ニトロチャージ 取得可能", dl.get_move("ニトロチャージ") is not None)
_mv_ニトロチャ_ジ = dl.get_move("ニトロチャージ")
if _mv_ニトロチャ_ジ:
    _pa_ニトロチャ_ジ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ニトロチャ_ジ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ニトロチャ_ジ = dmg(_pa_ニトロチャ_ジ, _pd_ニトロチャ_ジ, "ニトロチャージ")
    check("ダメージ計算: ニトロチャージ", _d_ニトロチャ_ジ > 0, f"dmg={_d_ニトロチャ_ジ}")
# ニトロチャージ: 自分素早さ+1
_mvss_ニトロチャ_ジ_speed = dl.get_move("ニトロチャージ")
if _mvss_ニトロチャ_ジ_speed:
    random.seed(0); _got_ニトロチャ_ジ_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="ほのお", atk_b=60, spatk_b=60); _pds = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "ニトロチャージ")
        if _pas.stage_speed != 0: _got_ニトロチャ_ジ_speed = _pas.stage_speed; break
    check("自分素早さ+1: ニトロチャージ", _got_ニトロチャ_ジ_speed == 1, f"1回適用={_got_ニトロチャ_ジ_speed} 期待=1")

# ── イカサマ ──
check("DB: イカサマ 取得可能", dl.get_move("イカサマ") is not None)
_mv_イカサマ = dl.get_move("イカサマ")
if _mv_イカサマ:
    _pa_イカサマ = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_イカサマ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_イカサマ = dmg(_pa_イカサマ, _pd_イカサマ, "イカサマ")
    check("ダメージ計算: イカサマ", _d_イカサマ > 0, f"dmg={_d_イカサマ}")
# イカサマ: 相手の攻撃実数値でダメージ計算（ランク変化も反映）
_pik = make_poke(type1="あく", atk_b=10); _dik_hi = make_poke(type1="エスパー", atk_b=200, def_b=100)
_dik_lo = make_poke(type1="エスパー", atk_b=10, def_b=100)
_d_hi = calc_damage(_pik, _dik_hi, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)
_d_lo = calc_damage(_pik, _dik_lo, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)
check("イカサマ 相手攻撃依存: イカサマ", _d_hi > _d_lo, f"hi={_d_hi} lo={_d_lo}")
# 相手の攻撃ランク+2でもダメージが増える（ランク変化反映）
_dik_buff = make_poke(type1="エスパー", atk_b=100, def_b=100); _dik_buff.stage_attack = 2
_dik_base = make_poke(type1="エスパー", atk_b=100, def_b=100)
_d_buff = calc_damage(_pik, _dik_buff, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)
_d_base = calc_damage(_pik, _dik_base, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)
check("相手攻撃依存(ランク変化): イカサマ", _d_buff > _d_base, f"buff={_d_buff} base={_d_base}")

# ── アシッドボム ──
check("DB: アシッドボム 取得可能", dl.get_move("アシッドボム") is not None)
_mv_アシッドボム = dl.get_move("アシッドボム")
if _mv_アシッドボム:
    _pa_アシッドボム = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_アシッドボム = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_アシッドボム = dmg(_pa_アシッドボム, _pd_アシッドボム, "アシッドボム")
    check("ダメージ計算: アシッドボム", _d_アシッドボム > 0, f"dmg={_d_アシッドボム}")
# アシッドボム: 相手特防-2
_mv_dd_アシッドボム = dl.get_move("アシッドボム")
if _mv_dd_アシッドボム:
    _pa_dd = make_poke(type1="どく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_アシッドボム = 0; _dd_ok_アシッドボム = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "アシッドボム")
        if _pd_dd.stage_sp_defense != 0: _dd_val_アシッドボム = _pd_dd.stage_sp_defense; _dd_ok_アシッドボム = True; break
    check("相手特防-2: アシッドボム", _dd_ok_アシッドボム and _dd_val_アシッドボム == -2, f"1回適用={_dd_val_アシッドボム} 期待=-2")

# ── アシストパワー ──
check("DB: アシストパワー 取得可能", dl.get_move("アシストパワー") is not None)
_mv_アシストパワ_ = dl.get_move("アシストパワー")
if _mv_アシストパワ_:
    _pa_アシストパワ_ = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_アシストパワ_ = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_アシストパワ_ = dmg(_pa_アシストパワ_, _pd_アシストパワ_, "アシストパワー")
    check("ダメージ計算: アシストパワー", _d_アシストパワ_ > 0, f"dmg={_d_アシストパワ_}")
# アシストパワー: 自分のランク合計で威力増（20+20×ランク）
_pap2 = make_poke(type1="エスパー", spatk_b=100, atk_b=100); _dap2 = make_poke(type1="かくとう", def_b=100, spdef_b=100)
_pw_base = _ep(_pap2, _dap2, dl.get_move("アシストパワー"), BattleField())
_pap2.stage_attack = 2; _pap2.stage_speed = 1
_pw_up = _ep(_pap2, _dap2, dl.get_move("アシストパワー"), BattleField())
check("ランクで威力増: アシストパワー", _pw_base == 20 and _pw_up == 20 + 20*3, f"base={_pw_base} up={_pw_up}")

# ── からをやぶる ──
check("DB: からをやぶる 取得可能", dl.get_move("からをやぶる") is not None)
# からをやぶる: 自分攻撃+2
_mv_sb_からをやぶる_attack = dl.get_move("からをやぶる")
if _mv_sb_からをやぶる_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "からをやぶる")
    check("自分攻撃+2: からをやぶる", _pa_sb.stage_attack == 2, f"1回適用={_pa_sb.stage_attack} 期待=+2")
# からをやぶる: 自分特攻+2
_mv_sb_からをやぶる_sp_attack = dl.get_move("からをやぶる")
if _mv_sb_からをやぶる_sp_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "からをやぶる")
    check("自分特攻+2: からをやぶる", _pa_sb.stage_sp_attack == 2, f"1回適用={_pa_sb.stage_sp_attack} 期待=+2")
# からをやぶる: 自分素早さ+2
_mv_sb_からをやぶる_speed = dl.get_move("からをやぶる")
if _mv_sb_からをやぶる_speed:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "からをやぶる")
    check("自分素早さ+2: からをやぶる", _pa_sb.stage_speed == 2, f"1回適用={_pa_sb.stage_speed} 期待=+2")

# ── ねっとう ──
check("DB: ねっとう 取得可能", dl.get_move("ねっとう") is not None)
_mv_ねっとう = dl.get_move("ねっとう")
if _mv_ねっとう:
    _pa_ねっとう = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ねっとう = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ねっとう = dmg(_pa_ねっとう, _pd_ねっとう, "ねっとう")
    check("ダメージ計算: ねっとう", _d_ねっとう > 0, f"dmg={_d_ねっとう}")
# ねっとう: やけど30%
_mv_s_ねっとう = dl.get_move("ねっとう")
if _mv_s_ねっとう:
    random.seed(0); _hit_ねっとう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="みず", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ねっとう")
        _hit_ねっとう += int((_pd2.status == "burn"))
    check("追加効果(やけど30%): ねっとう", 27 <= _hit_ねっとう <= 168, f"count={_hit_ねっとう}/300")
    random.seed(1); _immok_ねっとう = True
    for _ in range(60):
        _pai = make_poke(type1="みず", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ねっとう")
        if _pdi.status == "burn": _immok_ねっとう = False; break
    check("やけど免疫(ほのお型には無効): ねっとう", _immok_ねっとう, "免疫タイプに状態異常が付与されないこと")
# ねっとう: 相手のこおりを治す
_paf2 = make_poke(type1="みず", spatk_b=100, atk_b=100); _pdf2 = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
_pdf2.status = "freeze"; execute(_paf2, _pdf2, "ねっとう")
check("相手こおり治癒: ねっとう", _pdf2.status != "freeze")
# 自分のこおりも治す
_paf3 = make_poke(type1="みず", spatk_b=100, atk_b=100); _paf3.status = "freeze"
execute(_paf3, make_poke(hp_b=255), "ねっとう")
check("自分こおり治癒: ねっとう", _paf3.status != "freeze")

# ── たたりめ ──
check("DB: たたりめ 取得可能", dl.get_move("たたりめ") is not None)
_mv_たたりめ = dl.get_move("たたりめ")
if _mv_たたりめ:
    _pa_たたりめ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_たたりめ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_たたりめ = dmg(_pa_たたりめ, _pd_たたりめ, "たたりめ")
    check("ダメージ計算: たたりめ", _d_たたりめ > 0, f"dmg={_d_たたりめ}")
# たたりめ: 相手状態異常で威力2倍
_pcp = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
_dn1 = make_poke(type1="エスパー", def_b=100, spdef_b=100)
_dn2 = make_poke(type1="エスパー", def_b=100, spdef_b=100); _dn2.status = "burn"
_pn = _ep(_pcp, _dn1, dl.get_move("たたりめ"), BattleField())
_pd = _ep(_pcp, _dn2, dl.get_move("たたりめ"), BattleField())
check("状態異常で威力2倍: たたりめ", _pd == _pn * 2, f"normal={_pn} status={_pd}")

# ── アクロバット ──
check("DB: アクロバット 取得可能", dl.get_move("アクロバット") is not None)
_mv_アクロバット = dl.get_move("アクロバット")
if _mv_アクロバット:
    _pa_アクロバット = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_アクロバット = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_アクロバット = dmg(_pa_アクロバット, _pd_アクロバット, "アクロバット")
    check("ダメージ計算: アクロバット", _d_アクロバット > 0, f"dmg={_d_アクロバット}")
# アクロバット: 道具を持っていないと威力2倍
_pa = make_poke(atk_b=100, item="オボンのみ"); _pa2 = make_poke(atk_b=100); _da = make_poke(def_b=100)
_wi = _ep(_pa, _da, dl.get_move("アクロバット"), BattleField()); _wn = _ep(_pa2, _da, dl.get_move("アクロバット"), BattleField())
check("アクロバット道具なし2倍: アクロバット", _wn == _wi * 2, f"item={_wi} no={_wn}")

# ── ボルトチェンジ ──
check("DB: ボルトチェンジ 取得可能", dl.get_move("ボルトチェンジ") is not None)
_mv_ボルトチェンジ = dl.get_move("ボルトチェンジ")
if _mv_ボルトチェンジ:
    _pa_ボルトチェンジ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ボルトチェンジ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ボルトチェンジ = dmg(_pa_ボルトチェンジ, _pd_ボルトチェンジ, "ボルトチェンジ")
    check("ダメージ計算: ボルトチェンジ", _d_ボルトチェンジ > 0, f"dmg={_d_ボルトチェンジ}")
# ボルトチェンジ: ピボット交代フラグ
_mvpv_ボルトチェンジ = dl.get_move("ボルトチェンジ")
if _mvpv_ボルトチェンジ:
    _pap = make_poke(type1="でんき", atk_b=100, spatk_b=100); _pdp = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_ボルトチェンジ), BattleField())
    check("ピボット交代フラグ: ボルトチェンジ", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")

# ── じならし ──
check("DB: じならし 取得可能", dl.get_move("じならし") is not None)
_mv_じならし = dl.get_move("じならし")
if _mv_じならし:
    _pa_じならし = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_じならし = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_じならし = dmg(_pa_じならし, _pd_じならし, "じならし")
    check("ダメージ計算: じならし", _d_じならし > 0, f"dmg={_d_じならし}")
# じならし: 相手素早さ-1
_mv_dd_じならし = dl.get_move("じならし")
if _mv_dd_じならし:
    _pa_dd = make_poke(type1="じめん", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_じならし = 0; _dd_ok_じならし = False
    for _ in range(60):
        _pd_dd = make_poke(type1="でんき", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "じならし")
        if _pd_dd.stage_speed != 0: _dd_val_じならし = _pd_dd.stage_speed; _dd_ok_じならし = True; break
    check("相手素早さ-1: じならし", _dd_ok_じならし and _dd_val_じならし == -1, f"1回適用={_dd_val_じならし} 期待=-1")
# じならし: グラスフィールド時に威力半減
_pgf = make_poke(type1="じめん", atk_b=100); _dgf = make_poke(type1="どく", def_b=100)
_fg0 = BattleField(); _d_no = calc_damage(_pgf, _dgf, dl.get_move("じならし"), _fg0, random_roll=1.0)
_fg1 = BattleField(); _fg1.grassy_terrain = True
_d_gf = calc_damage(_pgf, _dgf, dl.get_move("じならし"), _fg1, random_roll=1.0)
check("じならし グラスF半減: じならし", _d_gf < _d_no, f"no={_d_no} gf={_d_gf}")

# ── ドラゴンテール ──
check("DB: ドラゴンテール 取得可能", dl.get_move("ドラゴンテール") is not None)
_mv_ドラゴンテ_ル = dl.get_move("ドラゴンテール")
if _mv_ドラゴンテ_ル:
    _pa_ドラゴンテ_ル = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_ドラゴンテ_ル = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ドラゴンテ_ル = dmg(_pa_ドラゴンテ_ル, _pd_ドラゴンテ_ル, "ドラゴンテール")
    check("ダメージ計算: ドラゴンテール", _d_ドラゴンテ_ル > 0, f"dmg={_d_ドラゴンテ_ル}")
# ドラゴンテール: 優先度-6
_mv_pr_ドラゴンテ_ル = dl.get_move("ドラゴンテール")
if _mv_pr_ドラゴンテ_ル and _mv_pr_ドラゴンテ_ル.priority == -6:
    check("優先度-6: ドラゴンテール", _mv_pr_ドラゴンテ_ル.priority == -6)
elif _mv_pr_ドラゴンテ_ル:
    check("優先度-6: ドラゴンテール", _mv_pr_ドラゴンテ_ル.priority == -6, f"DB優先度={_mv_pr_ドラゴンテ_ル.priority} 仕様=-6")
# ドラゴンテール: 控えがいれば相手をランダム交代させる／控えがいなければ交代しない
from simulator.battle import Battle as _Bfsw
import simulator.battle as _SBfsw; _mx_fsw = _SBfsw.MAX_TURNS; _SBfsw.MAX_TURNS = 1
import copy as _cpfs; _mvfs = _cpfs.copy(dl.get_move("ドラゴンテール")); _mvfs.accuracy = 100
_actfsw = lambda s,o,f: Action(type="move", move=_mvfs, move_idx=0)
_actwk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_pfsw = make_poke(type1="ドラゴン", atk_b=120, spd_b=200, moves=["ドラゴンテール"])
_df0 = make_poke(type1="ノーマル", hp_b=255, def_b=200, spd_b=10, moves=["たいあたり"]); _df1 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])
_sdef = BattleSide([_df0, _df1])
_Bfsw(BattleSide([_pfsw]), _sdef).run(_actfsw, _actwk)
check("控え有りで強制交代: ドラゴンテール", _sdef.active is not _df0, f"active_idx={_sdef.active_idx}")
_pfsw2 = make_poke(type1="ドラゴン", atk_b=120, spd_b=200, moves=["ドラゴンテール"])
_dsolo = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _ssolo = BattleSide([_dsolo])
_Bfsw(BattleSide([_pfsw2]), _ssolo).run(_actfsw, _actwk)
check("控えなしでは交代しない: ドラゴンテール", _ssolo.active is _dsolo, "1体なら強制交代は発生しない")
_SBfsw.MAX_TURNS = _mx_fsw

# ── ワイルドボルト ──
check("DB: ワイルドボルト 取得可能", dl.get_move("ワイルドボルト") is not None)
_mv_ワイルドボルト = dl.get_move("ワイルドボルト")
if _mv_ワイルドボルト:
    _pa_ワイルドボルト = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ワイルドボルト = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ワイルドボルト = dmg(_pa_ワイルドボルト, _pd_ワイルドボルト, "ワイルドボルト")
    check("ダメージ計算: ワイルドボルト", _d_ワイルドボルト > 0, f"dmg={_d_ワイルドボルト}")
# ワイルドボルト: 反動（与ダメの1/4）
_mvrc_ワイルドボルト = dl.get_move("ワイルドボルト")
if _mvrc_ワイルドボルト:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="でんき", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="みず", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "ワイルドボルト")
        _rc_dealt_ワイルドボルト = _hpdr - _pdr.hp; _rc_rcv_ワイルドボルト = _par.max_hp - _par.hp
        if _rc_dealt_ワイルドボルト > 0: break
    _rc_exp_ワイルドボルト = max(1, _rc_dealt_ワイルドボルト // 4)
    check("反動ダメージ(1/4): ワイルドボルト", abs(_rc_rcv_ワイルドボルト - _rc_exp_ワイルドボルト) <= 2, f"dealt={_rc_dealt_ワイルドボルト} recoil={_rc_rcv_ワイルドボルト} 期待={_rc_exp_ワイルドボルト}")

# ── ドリルライナー ──
check("DB: ドリルライナー 取得可能", dl.get_move("ドリルライナー") is not None)
_mv_ドリルライナ_ = dl.get_move("ドリルライナー")
if _mv_ドリルライナ_:
    _pa_ドリルライナ_ = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_ドリルライナ_ = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_ドリルライナ_ = dmg(_pa_ドリルライナ_, _pd_ドリルライナ_, "ドリルライナー")
    check("ダメージ計算: ドリルライナー", _d_ドリルライナ_ > 0, f"dmg={_d_ドリルライナ_}")
# ドリルライナー: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_ドリルライナ_
random.seed(0); _hc_crit_ドリルライナ_ = 0; _phc = make_poke(type1="じめん")
_mvhc_ドリルライナ_ = dl.get_move("ドリルライナー")
for _ in range(800):
    if _cc_ドリルライナ_(_phc, _mvhc_ドリルライナ_, make_poke(type1="でんき")): _hc_crit_ドリルライナ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: ドリルライナー", 60 <= _hc_crit_ドリルライナ_ <= 150, f"crit={_hc_crit_ドリルライナ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── シェルブレード ──
check("DB: シェルブレード 取得可能", dl.get_move("シェルブレード") is not None)
_mv_シェルブレ_ド = dl.get_move("シェルブレード")
if _mv_シェルブレ_ド:
    _pa_シェルブレ_ド = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_シェルブレ_ド = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_シェルブレ_ド = dmg(_pa_シェルブレ_ド, _pd_シェルブレ_ド, "シェルブレード")
    check("ダメージ計算: シェルブレード", _d_シェルブレ_ド > 0, f"dmg={_d_シェルブレ_ド}")
# シェルブレード: 相手防御-1
_mv_dd_シェルブレ_ド = dl.get_move("シェルブレード")
if _mv_dd_シェルブレ_ド:
    _pa_dd = make_poke(type1="みず", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_シェルブレ_ド = 0; _dd_ok_シェルブレ_ド = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ほのお", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "シェルブレード")
        if _pd_dd.stage_defense != 0: _dd_val_シェルブレ_ド = _pd_dd.stage_defense; _dd_ok_シェルブレ_ド = True; break
    check("相手防御-1: シェルブレード", _dd_ok_シェルブレ_ド and _dd_val_シェルブレ_ド == -1, f"1回適用={_dd_val_シェルブレ_ド} 期待=-1")

# ── ウッドホーン ──
check("DB: ウッドホーン 取得可能", dl.get_move("ウッドホーン") is not None)
_mv_ウッドホ_ン = dl.get_move("ウッドホーン")
if _mv_ウッドホ_ン:
    _pa_ウッドホ_ン = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ウッドホ_ン = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ウッドホ_ン = dmg(_pa_ウッドホ_ン, _pd_ウッドホ_ン, "ウッドホーン")
    check("ダメージ計算: ウッドホーン", _d_ウッドホ_ン > 0, f"dmg={_d_ウッドホ_ン}")
# ウッドホーン: ドレイン（与ダメの1/2回復）
_mv_dr_ウッドホ_ン = dl.get_move("ウッドホーン")
if _mv_dr_ウッドホ_ン:
    _pa_dr = make_poke(type1="くさ", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_ウッドホ_ン = False; _dr_dealt_ウッドホ_ン = 0; _dr_heal_ウッドホ_ン = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="みず", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "ウッドホーン")
        _dr_dealt_ウッドホ_ン = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_ウッドホ_ン = _pa_dr.hp - 1
        if _dr_dealt_ウッドホ_ン > 0: _dr_ok_ウッドホ_ン = abs(_dr_heal_ウッドホ_ン - max(1, _dr_dealt_ウッドホ_ン * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): ウッドホーン", _dr_ok_ウッドホ_ン, f"dealt={_dr_dealt_ウッドホ_ン} heal={_dr_heal_ウッドホ_ン}")

# ── ヒートスタンプ ──
check("DB: ヒートスタンプ 取得可能", dl.get_move("ヒートスタンプ") is not None)
# ヒートスタンプ: 重さ比別の威力テーブル（≥5→120 ... 未満→40）
_pwh = make_poke(type1="ほのお", atk_b=100); _pwh.weight_kg = 500.0
_hb_ng = []
for _wd, _exp in [(99,120),(125,100),(166,80),(250,60),(400,40)]:
    _dwh = make_poke(type1="くさ"); _dwh.weight_kg = float(_wd)
    _got = _ep(_pwh, _dwh, dl.get_move("ヒートスタンプ"), BattleField())
    if _got != _exp: _hb_ng.append(f"500/{_wd}kg:{_got}!={_exp}")
check("重さ比別威力テーブル: ヒートスタンプ", not _hb_ng, f"NG={_hb_ng}")
# ちいさくなる状態の相手に威力2倍（重さ比固定: 500/100kg→比5→威力120）
_dmm0 = make_poke(type1="くさ"); _dmm0.weight_kg = 100.0
_dmm1 = make_poke(type1="くさ"); _dmm1.weight_kg = 100.0; _dmm1.minimized = True
_mm_n = _ep(_pwh, _dmm0, dl.get_move("ヒートスタンプ"), BattleField()); _mm_m = _ep(_pwh, _dmm1, dl.get_move("ヒートスタンプ"), BattleField())
check("ちいさくなる2倍: ヒートスタンプ", _mm_m == _mm_n * 2, f"normal={_mm_n} mini={_mm_m}")

# ── せいなるつるぎ ──
check("DB: せいなるつるぎ 取得可能", dl.get_move("せいなるつるぎ") is not None)
_mv_せいなるつるぎ = dl.get_move("せいなるつるぎ")
if _mv_せいなるつるぎ:
    _pa_せいなるつるぎ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_せいなるつるぎ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_せいなるつるぎ = dmg(_pa_せいなるつるぎ, _pd_せいなるつるぎ, "せいなるつるぎ")
    check("ダメージ計算: せいなるつるぎ", _d_せいなるつるぎ > 0, f"dmg={_d_せいなるつるぎ}")
# せいなるつるぎ: 相手の防御ランク上昇を無視
_pdd = make_poke(type1="かくとう", atk_b=100)
_ddd = make_poke(type1="ノーマル", def_b=100); _ddd.stage_defense = 6
_dd_ignore = calc_damage(_pdd, _ddd, dl.get_move("せいなるつるぎ"), BattleField(), random_roll=1.0)
_ddn = make_poke(type1="ノーマル", def_b=100)
_dd_normal = calc_damage(_pdd, _ddn, dl.get_move("せいなるつるぎ"), BattleField(), random_roll=1.0)
check("防御ランク上昇無視: せいなるつるぎ", _dd_ignore == _dd_normal, f"ignore={_dd_ignore} normal={_dd_normal}")
# 防御ランク低下も無視（相手が防御-6でも軽減されない＝通常と同ダメージ）
_ddlo = make_poke(type1="ノーマル", def_b=100); _ddlo.stage_defense = -6
_dd_low = calc_damage(_pdd, _ddlo, dl.get_move("せいなるつるぎ"), BattleField(), random_roll=1.0)
check("防御ランク低下も無視: せいなるつるぎ", _dd_low == _dd_normal, f"low={_dd_low} normal={_dd_normal}")

# ── エレキネット ──
check("DB: エレキネット 取得可能", dl.get_move("エレキネット") is not None)
_mv_エレキネット = dl.get_move("エレキネット")
if _mv_エレキネット:
    _pa_エレキネット = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_エレキネット = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_エレキネット = dmg(_pa_エレキネット, _pd_エレキネット, "エレキネット")
    check("ダメージ計算: エレキネット", _d_エレキネット > 0, f"dmg={_d_エレキネット}")
# エレキネット: 相手素早さ-1
_mv_dd_エレキネット = dl.get_move("エレキネット")
if _mv_dd_エレキネット:
    _pa_dd = make_poke(type1="でんき", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_エレキネット = 0; _dd_ok_エレキネット = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "エレキネット")
        if _pd_dd.stage_speed != 0: _dd_val_エレキネット = _pd_dd.stage_speed; _dd_ok_エレキネット = True; break
    check("相手素早さ-1: エレキネット", _dd_ok_エレキネット and _dd_val_エレキネット == -1, f"1回適用={_dd_val_エレキネット} 期待=-1")

# ── コットンガード ──
check("DB: コットンガード 取得可能", dl.get_move("コットンガード") is not None)
# コットンガード: 自分防御+3
_mv_sb_コットンガ_ド_defense = dl.get_move("コットンガード")
if _mv_sb_コットンガ_ド_defense:
    _pa_sb = make_poke(type1="くさ"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "コットンガード")
    check("自分防御+3: コットンガード", _pa_sb.stage_defense == 3, f"1回適用={_pa_sb.stage_defense} 期待=+3")
# コットンガード: 自分防御+3
_mvss_コットンガ_ド_defense = dl.get_move("コットンガード")
if _mvss_コットンガ_ド_defense:
    random.seed(0); _got_コットンガ_ド_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="くさ", atk_b=60, spatk_b=60); _pds = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "コットンガード")
        if _pas.stage_defense != 0: _got_コットンガ_ド_defense = _pas.stage_defense; break
    check("自分防御+3: コットンガード", _got_コットンガ_ド_defense == 3, f"1回適用={_got_コットンガ_ド_defense} 期待=3")

# ── ナイトバースト ──
check("DB: ナイトバースト 取得可能", dl.get_move("ナイトバースト") is not None)
_mv_ナイトバ_スト = dl.get_move("ナイトバースト")
if _mv_ナイトバ_スト:
    _pa_ナイトバ_スト = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ナイトバ_スト = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ナイトバ_スト = dmg(_pa_ナイトバ_スト, _pd_ナイトバ_スト, "ナイトバースト")
    check("ダメージ計算: ナイトバースト", _d_ナイトバ_スト > 0, f"dmg={_d_ナイトバ_スト}")
# ナイトバースト: 相手命中率-1
_mv_dd_ナイトバ_スト = dl.get_move("ナイトバースト")
if _mv_dd_ナイトバ_スト:
    _pa_dd = make_poke(type1="あく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ナイトバ_スト = 0; _dd_ok_ナイトバ_スト = False
    for _ in range(60):
        _pd_dd = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ナイトバースト")
        if _pd_dd.stage_accuracy != 0: _dd_val_ナイトバ_スト = _pd_dd.stage_accuracy; _dd_ok_ナイトバ_スト = True; break
    check("相手命中率-1: ナイトバースト", _dd_ok_ナイトバ_スト and _dd_val_ナイトバ_スト == -1, f"1回適用={_dd_val_ナイトバ_スト} 期待=-1")

# ── ぼうふう ──
check("DB: ぼうふう 取得可能", dl.get_move("ぼうふう") is not None)
_mv_ぼうふう = dl.get_move("ぼうふう")
if _mv_ぼうふう:
    _pa_ぼうふう = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ぼうふう = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ぼうふう = dmg(_pa_ぼうふう, _pd_ぼうふう, "ぼうふう")
    check("ダメージ計算: ぼうふう", _d_ぼうふう > 0, f"dmg={_d_ぼうふう}")
# ぼうふう: こんらん30%
_mv_s_ぼうふう = dl.get_move("ぼうふう")
if _mv_s_ぼうふう:
    random.seed(0); _hit_ぼうふう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ひこう", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ぼうふう")
        _hit_ぼうふう += int(_pd2.confused)
    check("追加効果(こんらん30%): ぼうふう", 27 <= _hit_ぼうふう <= 168, f"count={_hit_ぼうふう}/300")
# ぼうふう: あめ状態で必中
_mvwh_ぼうふう = dl.get_move("ぼうふう")
if _mvwh_ぼうふう:
    random.seed(0); _wh_all_ぼうふう = True
    for _ in range(30):
        _pawh = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pdwh = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
        _fwh = BattleField(); _fwh.weather = "rain"
        _hpwh = _pdwh.hp
        _execute_move(BattleSide([_pawh]), BattleSide([_pdwh]), Action(type="move", move=_mvwh_ぼうふう), _fwh)
        if _pdwh.hp == _hpwh: _wh_all_ぼうふう = False; break
    check("あめ状態で必中: ぼうふう", _wh_all_ぼうふう)
# ぼうふう: あめ必中・にほんばれ命中低下
_pwa = make_poke(type1="ひこう", spatk_b=100); _dwa = make_poke(type1="くさ", spdef_b=100)
_fsun_w = BattleField(); _fsun_w.weather = "sunny"; _fnorm_w = BattleField()
from simulator.damage import check_hit as _ch
random.seed(0); _miss_sun = sum(0 if _ch(_pwa, _dwa, dl.get_move("ぼうふう"), _fsun_w) else 1 for _ in range(200))
random.seed(0); _miss_norm = sum(0 if _ch(_pwa, _dwa, dl.get_move("ぼうふう"), _fnorm_w) else 1 for _ in range(200))
check("晴れ命中低下: ぼうふう", _miss_sun > _miss_norm, f"sun_miss={_miss_sun} norm_miss={_miss_norm}")

# ── ほのおのまい ──
check("DB: ほのおのまい 取得可能", dl.get_move("ほのおのまい") is not None)
_mv_ほのおのまい = dl.get_move("ほのおのまい")
if _mv_ほのおのまい:
    _pa_ほのおのまい = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ほのおのまい = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ほのおのまい = dmg(_pa_ほのおのまい, _pd_ほのおのまい, "ほのおのまい")
    check("ダメージ計算: ほのおのまい", _d_ほのおのまい > 0, f"dmg={_d_ほのおのまい}")
# ほのおのまい: 50%で自分の特攻+1
random.seed(0); _fd_up = False
for _ in range(20):
    _pfd = make_poke(type1="ほのお", spatk_b=100); _dfd = make_poke(type1="くさ", hp_b=255, spdef_b=200)
    execute(_pfd, _dfd, "ほのおのまい")
    if _pfd.stage_sp_attack > 0: _fd_up = True; break
check("自分特攻上昇: ほのおのまい", _fd_up)

# ── つららおとし ──
check("DB: つららおとし 取得可能", dl.get_move("つららおとし") is not None)
_mv_つららおとし = dl.get_move("つららおとし")
if _mv_つららおとし:
    _pa_つららおとし = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_つららおとし = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_つららおとし = dmg(_pa_つららおとし, _pd_つららおとし, "つららおとし")
    check("ダメージ計算: つららおとし", _d_つららおとし > 0, f"dmg={_d_つららおとし}")
# つららおとし: ひるみ30%
_mv_f_つららおとし = dl.get_move("つららおとし")
if _mv_f_つららおとし:
    random.seed(1); _fh_つららおとし = 0
    for _ in range(300):
        _pa3 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "つららおとし"); _fh_つららおとし += int(_pd3.flinched)
    check("ひるみ(30%): つららおとし", 27 <= _fh_つららおとし <= 168, f"count={_fh_つららおとし}/300")

# ── バークアウト ──
check("DB: バークアウト 取得可能", dl.get_move("バークアウト") is not None)
_mv_バ_クアウト = dl.get_move("バークアウト")
if _mv_バ_クアウト:
    _pa_バ_クアウト = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_バ_クアウト = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_バ_クアウト = dmg(_pa_バ_クアウト, _pd_バ_クアウト, "バークアウト")
    check("ダメージ計算: バークアウト", _d_バ_クアウト > 0, f"dmg={_d_バ_クアウト}")
# バークアウト: 相手特攻-1
_mv_dd_バ_クアウト = dl.get_move("バークアウト")
if _mv_dd_バ_クアウト:
    _pa_dd = make_poke(type1="あく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_バ_クアウト = 0; _dd_ok_バ_クアウト = False
    for _ in range(60):
        _pd_dd = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "バークアウト")
        if _pd_dd.stage_sp_attack != 0: _dd_val_バ_クアウト = _pd_dd.stage_sp_attack; _dd_ok_バ_クアウト = True; break
    check("相手特攻-1: バークアウト", _dd_ok_バ_クアウト and _dd_val_バ_クアウト == -1, f"1回適用={_dd_val_バ_クアウト} 期待=-1")

# ── ねばねばネット ──
check("DB: ねばねばネット 取得可能", dl.get_move("ねばねばネット") is not None)
# ねばねばネット: ハザードsticky_web
_mvhz_ねばねばネット = dl.get_move("ねばねばネット")
if _mvhz_ねばねばネット:
    _s1h, _s2h, _fh2 = execute_ctx(make_poke(type1="むし"), make_poke(), "ねばねばネット")
    _hzval = _fh2.sticky_web[_s2h.field_idx]
    check("ハザードsticky_web: ねばねばネット", bool(_hzval), f"val={_hzval}")

# ── ゴーストダイブ ──
check("DB: ゴーストダイブ 取得可能", dl.get_move("ゴーストダイブ") is not None)
_mv_ゴ_ストダイブ = dl.get_move("ゴーストダイブ")
if _mv_ゴ_ストダイブ:
    _pa_ゴ_ストダイブ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_ゴ_ストダイブ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_ゴ_ストダイブ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100); _pd_ゴ_ストダイブ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
        execute(_pa_ゴ_ストダイブ, _pd_ゴ_ストダイブ, "ゴーストダイブ"); execute(_pa_ゴ_ストダイブ, _pd_ゴ_ストダイブ, "ゴーストダイブ")
        if _pd_ゴ_ストダイブ.hp < _pd_ゴ_ストダイブ.max_hp: break
    check("ダメージ計算: ゴーストダイブ", _pd_ゴ_ストダイブ.hp < _pd_ゴ_ストダイブ.max_hp, f"hp={_pd_ゴ_ストダイブ.hp}")
# ゴーストダイブ: 2ターン溜め
_mv_2t_ゴ_ストダイブ = dl.get_move("ゴーストダイブ")
if _mv_2t_ゴ_ストダイブ:
    _pa_2t = make_poke(type1="ゴースト", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "ゴーストダイブ")
    check("2ターン溜め(1T)ダメなし: ゴーストダイブ", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: ゴーストダイブ", _pa_2t.charging_move == "ゴーストダイブ")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "ゴーストダイブ")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "ゴーストダイブ")
    check("2ターン溜め(2T)ダメあり: ゴーストダイブ", _pd_2t.hp < _hp_before_2t)
# ゴーストダイブ: 攻撃ターンにまもるを貫通して命中
_pgd = make_poke(type1="ゴースト", atk_b=120); _dgd = make_poke(type1="エスパー", hp_b=255, def_b=150)
_pgd.charging_move = "ゴーストダイブ"; _dgd.protecting = True; _hpgd = _dgd.hp
_execute_move(BattleSide([_pgd]), BattleSide([_dgd]), Action(type="move", move=dl.get_move("ゴーストダイブ")), BattleField())
check("まもる貫通: ゴーストダイブ", _dgd.hp < _hpgd, f"hp={_dgd.hp}/{_hpgd}")

# ── とどめばり ──
check("DB: とどめばり 取得可能", dl.get_move("とどめばり") is not None)
_mv_とどめばり = dl.get_move("とどめばり")
if _mv_とどめばり:
    _pa_とどめばり = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_とどめばり = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_とどめばり = dmg(_pa_とどめばり, _pd_とどめばり, "とどめばり")
    check("ダメージ計算: とどめばり", _d_とどめばり > 0, f"dmg={_d_とどめばり}")
# とどめばり: 相手を倒すと自分の攻撃+3
_ptd = make_poke(type1="むし", atk_b=220); _dtd = make_poke(type1="あく", hp_b=1, def_b=1)
execute(_ptd, _dtd, "とどめばり")
check("とどめばりKO攻撃+3: とどめばり", (not _dtd.is_alive) and _ptd.stage_attack == 3, f"alive={_dtd.is_alive} atk={_ptd.stage_attack}")
# negative: 倒せなかった場合は攻撃が上がらない
_ptd2 = make_poke(type1="むし", atk_b=10); _dtd2 = make_poke(type1="あく", hp_b=255, def_b=255)
execute(_ptd2, _dtd2, "とどめばり")
check("非KO時は攻撃上昇なし: とどめばり", _dtd2.is_alive and _ptd2.stage_attack == 0, f"alive={_dtd2.is_alive} atk={_ptd2.stage_attack}")

# ── パラボラチャージ ──
check("DB: パラボラチャージ 取得可能", dl.get_move("パラボラチャージ") is not None)
_mv_パラボラチャ_ジ = dl.get_move("パラボラチャージ")
if _mv_パラボラチャ_ジ:
    _pa_パラボラチャ_ジ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_パラボラチャ_ジ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_パラボラチャ_ジ = dmg(_pa_パラボラチャ_ジ, _pd_パラボラチャ_ジ, "パラボラチャージ")
    check("ダメージ計算: パラボラチャージ", _d_パラボラチャ_ジ > 0, f"dmg={_d_パラボラチャ_ジ}")
# パラボラチャージ: ドレイン（与ダメの1/2回復）
_mv_dr_パラボラチャ_ジ = dl.get_move("パラボラチャージ")
if _mv_dr_パラボラチャ_ジ:
    _pa_dr = make_poke(type1="でんき", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_パラボラチャ_ジ = False; _dr_dealt_パラボラチャ_ジ = 0; _dr_heal_パラボラチャ_ジ = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="みず", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "パラボラチャージ")
        _dr_dealt_パラボラチャ_ジ = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_パラボラチャ_ジ = _pa_dr.hp - 1
        if _dr_dealt_パラボラチャ_ジ > 0: _dr_ok_パラボラチャ_ジ = abs(_dr_heal_パラボラチャ_ジ - max(1, _dr_dealt_パラボラチャ_ジ * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): パラボラチャージ", _dr_ok_パラボラチャ_ジ, f"dealt={_dr_dealt_パラボラチャ_ジ} heal={_dr_heal_パラボラチャ_ジ}")

# ── フリーズドライ ──
check("DB: フリーズドライ 取得可能", dl.get_move("フリーズドライ") is not None)
_mv_フリ_ズドライ = dl.get_move("フリーズドライ")
if _mv_フリ_ズドライ:
    _pa_フリ_ズドライ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_フリ_ズドライ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_フリ_ズドライ = dmg(_pa_フリ_ズドライ, _pd_フリ_ズドライ, "フリーズドライ")
    check("ダメージ計算: フリーズドライ", _d_フリ_ズドライ > 0, f"dmg={_d_フリ_ズドライ}")
# フリーズドライ: みずタイプに効果バツグン上書き
_mv_ov_フリ_ズドライ = dl.get_move("フリーズドライ")
if _mv_ov_フリ_ズドライ:
    _pa_ov = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _d_ov_tgt = dmg(_pa_ov, make_poke(type1="みず", def_b=100, spdef_b=100), "フリーズドライ")
    _d_ov_neu = dmg(_pa_ov, make_poke(type1="ノーマル", def_b=100, spdef_b=100), "フリーズドライ")
    check("みず効果バツグン上書き: フリーズドライ", _d_ov_tgt >= _d_ov_neu * 2, f"tgt={_d_ov_tgt} neu={_d_ov_neu}")

# ── すてゼリフ ──
check("DB: すてゼリフ 取得可能", dl.get_move("すてゼリフ") is not None)
# すてゼリフ: ピボット交代フラグ
_mvpv_すてゼリフ = dl.get_move("すてゼリフ")
if _mvpv_すてゼリフ:
    _pap = make_poke(type1="あく", atk_b=100, spatk_b=100); _pdp = make_poke(type1="エスパー", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_すてゼリフ), BattleField())
    check("ピボット交代フラグ: すてゼリフ", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")

# ── ドレインキッス ──
check("DB: ドレインキッス 取得可能", dl.get_move("ドレインキッス") is not None)
_mv_ドレインキッス = dl.get_move("ドレインキッス")
if _mv_ドレインキッス:
    _pa_ドレインキッス = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_ドレインキッス = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ドレインキッス = dmg(_pa_ドレインキッス, _pd_ドレインキッス, "ドレインキッス")
    check("ダメージ計算: ドレインキッス", _d_ドレインキッス > 0, f"dmg={_d_ドレインキッス}")
# ドレインキッス: ドレイン（与ダメの3/4回復）
_mv_dr_ドレインキッス = dl.get_move("ドレインキッス")
if _mv_dr_ドレインキッス:
    _pa_dr = make_poke(type1="フェアリー", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_ドレインキッス = False; _dr_dealt_ドレインキッス = 0; _dr_heal_ドレインキッス = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="ドラゴン", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "ドレインキッス")
        _dr_dealt_ドレインキッス = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_ドレインキッス = _pa_dr.hp - 1
        if _dr_dealt_ドレインキッス > 0: _dr_ok_ドレインキッス = abs(_dr_heal_ドレインキッス - max(1, _dr_dealt_ドレインキッス * 3 // 4)) <= 2; break
    check("ドレイン回復(与ダメ3/4): ドレインキッス", _dr_ok_ドレインキッス, f"dealt={_dr_dealt_ドレインキッス} heal={_dr_heal_ドレインキッス}")

# ── ミストフィールド ──
check("DB: ミストフィールド 取得可能", dl.get_move("ミストフィールド") is not None)
# ミストフィールド: フィールド展開
_mvfl_ミストフィ_ルド = dl.get_move("ミストフィールド")
if _mvfl_ミストフィ_ルド:
    _s1f, _s2f, _ff = execute_ctx(make_poke(type1="フェアリー"), make_poke(), "ミストフィールド")
    check("フィールドmisty_terrain: ミストフィールド", _ff.misty_terrain, f"val={_ff.misty_terrain}")

# ── じゃれつく ──
check("DB: じゃれつく 取得可能", dl.get_move("じゃれつく") is not None)
_mv_じゃれつく = dl.get_move("じゃれつく")
if _mv_じゃれつく:
    _pa_じゃれつく = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_じゃれつく = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_じゃれつく = dmg(_pa_じゃれつく, _pd_じゃれつく, "じゃれつく")
    check("ダメージ計算: じゃれつく", _d_じゃれつく > 0, f"dmg={_d_じゃれつく}")
# じゃれつく: 相手攻撃-1
_mv_dd_じゃれつく = dl.get_move("じゃれつく")
if _mv_dd_じゃれつく:
    _pa_dd = make_poke(type1="フェアリー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_じゃれつく = 0; _dd_ok_じゃれつく = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "じゃれつく")
        if _pd_dd.stage_attack != 0: _dd_val_じゃれつく = _pd_dd.stage_attack; _dd_ok_じゃれつく = True; break
    check("相手攻撃-1: じゃれつく", _dd_ok_じゃれつく and _dd_val_じゃれつく == -1, f"1回適用={_dd_val_じゃれつく} 期待=-1")

# ── ムーンフォース ──
check("DB: ムーンフォース 取得可能", dl.get_move("ムーンフォース") is not None)
_mv_ム_ンフォ_ス = dl.get_move("ムーンフォース")
if _mv_ム_ンフォ_ス:
    _pa_ム_ンフォ_ス = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_ム_ンフォ_ス = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ム_ンフォ_ス = dmg(_pa_ム_ンフォ_ス, _pd_ム_ンフォ_ス, "ムーンフォース")
    check("ダメージ計算: ムーンフォース", _d_ム_ンフォ_ス > 0, f"dmg={_d_ム_ンフォ_ス}")
# ムーンフォース: 相手特攻-1
_mv_dd_ム_ンフォ_ス = dl.get_move("ムーンフォース")
if _mv_dd_ム_ンフォ_ス:
    _pa_dd = make_poke(type1="フェアリー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ム_ンフォ_ス = 0; _dd_ok_ム_ンフォ_ス = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ムーンフォース")
        if _pd_dd.stage_sp_attack != 0: _dd_val_ム_ンフォ_ス = _pd_dd.stage_sp_attack; _dd_ok_ム_ンフォ_ス = True; break
    check("相手特攻-1: ムーンフォース", _dd_ok_ム_ンフォ_ス and _dd_val_ム_ンフォ_ス == -1, f"1回適用={_dd_val_ム_ンフォ_ス} 期待=-1")

# ── ばくおんぱ ──
check("DB: ばくおんぱ 取得可能", dl.get_move("ばくおんぱ") is not None)
_mv_ばくおんぱ = dl.get_move("ばくおんぱ")
if _mv_ばくおんぱ:
    _pa_ばくおんぱ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ばくおんぱ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ばくおんぱ = dmg(_pa_ばくおんぱ, _pd_ばくおんぱ, "ばくおんぱ")
    check("ダメージ計算: ばくおんぱ", _d_ばくおんぱ > 0, f"dmg={_d_ばくおんぱ}")

# ── キングシールド ──
check("DB: キングシールド 取得可能", dl.get_move("キングシールド") is not None)
# キングシールド: 優先度4
_mv_pr_キングシ_ルド = dl.get_move("キングシールド")
if _mv_pr_キングシ_ルド and _mv_pr_キングシ_ルド.priority == 4:
    check("優先度4: キングシールド", _mv_pr_キングシ_ルド.priority == 4)
elif _mv_pr_キングシ_ルド:
    check("優先度4: キングシールド", _mv_pr_キングシ_ルド.priority == 4, f"DB優先度={_mv_pr_キングシ_ルド.priority} 仕様=4")
# キングシールド: 守る状態になる+接触攻撃者の攻撃-1
_pks = make_poke(type1="はがね"); execute(_pks, make_poke(), "キングシールド")
check("キングシールド 守る状態: キングシールド", _pks.protecting)
_atkr = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _pks2 = make_poke(type1="はがね")
_pks2.protecting = True; _pks2._protect_move = "キングシールド"
_s1k = BattleSide([_atkr]); _s2k = BattleSide([_pks2])
_execute_move(_s1k, _s2k, Action(type="move", move=dl.get_move("のしかかり")), BattleField())
check("接触者攻撃-1: キングシールド", _atkr.stage_attack == -1, f"1回適用={_atkr.stage_attack} 期待=-1")
# 使用するとシールドフォルムに戻る（ブレードフォルム→シールド）
from simulator.battle import _aegislash_to_blade as _toblade
_pksf = make_poke(type1="はがね", atk_b=100, ability="バトルスイッチ"); _toblade(_pksf, [])
check("前提ブレードフォルム: キングシールド", _pksf._in_blade_forme)
execute(_pksf, make_poke(), "キングシールド")
check("使用でシールドフォルム化: キングシールド", not _pksf._in_blade_forme, f"blade={_pksf._in_blade_forme}")

# ── マジカルフレイム ──
check("DB: マジカルフレイム 取得可能", dl.get_move("マジカルフレイム") is not None)
_mv_マジカルフレイム = dl.get_move("マジカルフレイム")
if _mv_マジカルフレイム:
    _pa_マジカルフレイム = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_マジカルフレイム = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_マジカルフレイム = dmg(_pa_マジカルフレイム, _pd_マジカルフレイム, "マジカルフレイム")
    check("ダメージ計算: マジカルフレイム", _d_マジカルフレイム > 0, f"dmg={_d_マジカルフレイム}")
# マジカルフレイム: 相手特攻-1
_mv_dd_マジカルフレイム = dl.get_move("マジカルフレイム")
if _mv_dd_マジカルフレイム:
    _pa_dd = make_poke(type1="ほのお", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_マジカルフレイム = 0; _dd_ok_マジカルフレイム = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "マジカルフレイム")
        if _pd_dd.stage_sp_attack != 0: _dd_val_マジカルフレイム = _pd_dd.stage_sp_attack; _dd_ok_マジカルフレイム = True; break
    check("相手特攻-1: マジカルフレイム", _dd_ok_マジカルフレイム and _dd_val_マジカルフレイム == -1, f"1回適用={_dd_val_マジカルフレイム} 期待=-1")

# ── みずしゅりけん ──
check("DB: みずしゅりけん 取得可能", dl.get_move("みずしゅりけん") is not None)
_mv_みずしゅりけん = dl.get_move("みずしゅりけん")
if _mv_みずしゅりけん:
    _pa_みずしゅりけん = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_みずしゅりけん = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_みずしゅりけん = dmg(_pa_みずしゅりけん, _pd_みずしゅりけん, "みずしゅりけん")
    check("ダメージ計算: みずしゅりけん", _d_みずしゅりけん > 0, f"dmg={_d_みずしゅりけん}")
# みずしゅりけん: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_みずしゅりけん = dl.get_move("みずしゅりけん")
if _mvmh_みずしゅりけん:
    _pam = make_poke(type1="みず", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_みずしゅりけん = calc_damage(_pam, make_poke(type1="ほのお", hp_b=255, def_b=200, spdef_b=200), _mvmh_みずしゅりけん, BattleField(), random_roll=1.0)
    random.seed(0); _multi_みずしゅりけん = 0
    for _ in range(20):
        _pdm = make_poke(type1="ほのお", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "みずしゅりけん"); _multi_みずしゅりけん = _pdm.max_hp - _pdm.hp
        if _multi_みずしゅりけん > _single_みずしゅりけん: break
    check("多段ヒット発生(複数回): みずしゅりけん", _multi_みずしゅりけん > _single_みずしゅりけん, f"single={_single_みずしゅりけん} multi={_multi_みずしゅりけん}")

# ── かいでんぱ ──
check("DB: かいでんぱ 取得可能", dl.get_move("かいでんぱ") is not None)
# かいでんぱ: 相手特攻-2
_mv_dd_かいでんぱ = dl.get_move("かいでんぱ")
if _mv_dd_かいでんぱ:
    _pa_dd = make_poke(type1="でんき", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_かいでんぱ = 0; _dd_ok_かいでんぱ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "かいでんぱ")
        if _pd_dd.stage_sp_attack != 0: _dd_val_かいでんぱ = _pd_dd.stage_sp_attack; _dd_ok_かいでんぱ = True; break
    check("相手特攻-2: かいでんぱ", _dd_ok_かいでんぱ and _dd_val_かいでんぱ == -2, f"1回適用={_dd_val_かいでんぱ} 期待=-2")

# ── ニードルガード ──
check("DB: ニードルガード 取得可能", dl.get_move("ニードルガード") is not None)
# ニードルガード: 優先度4
_mv_pr_ニ_ドルガ_ド = dl.get_move("ニードルガード")
if _mv_pr_ニ_ドルガ_ド and _mv_pr_ニ_ドルガ_ド.priority == 4:
    check("優先度4: ニードルガード", _mv_pr_ニ_ドルガ_ド.priority == 4)
elif _mv_pr_ニ_ドルガ_ド:
    check("優先度4: ニードルガード", _mv_pr_ニ_ドルガ_ド.priority == 4, f"DB優先度={_mv_pr_ニ_ドルガ_ド.priority} 仕様=4")
# ニードルガード: 守る成功+接触攻撃者にHP1/8ダメ
_png2 = make_poke(type1="くさ"); execute(_png2, make_poke(), "ニードルガード")
check("ニードルガード 守る状態: ニードルガード", _png2.protecting)
_atk_n = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _png3 = make_poke(type1="くさ")
_png3.protecting = True; _png3._protect_move = "ニードルガード"; _hp_n = _atk_n.hp
_execute_move(BattleSide([_atk_n]), BattleSide([_png3]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())
check("ニードルガード 接触ダメ: ニードルガード", _atk_n.hp < _hp_n, f"hp={_atk_n.hp}")
check("接触ダメは最大HP1/8(具体値): ニードルガード", _atk_n.max_hp - _atk_n.hp == _atk_n.max_hp // 8, f"dmg={_atk_n.max_hp - _atk_n.hp} 期待={_atk_n.max_hp // 8}")

# ── エレキフィールド ──
check("DB: エレキフィールド 取得可能", dl.get_move("エレキフィールド") is not None)
# エレキフィールド: フィールド展開
_mvfl_エレキフィ_ルド = dl.get_move("エレキフィールド")
if _mvfl_エレキフィ_ルド:
    _s1f, _s2f, _ff = execute_ctx(make_poke(type1="でんき"), make_poke(), "エレキフィールド")
    check("フィールドelectric_terrain: エレキフィールド", _ff.electric_terrain, f"val={_ff.electric_terrain}")

# ── マジカルシャイン ──
check("DB: マジカルシャイン 取得可能", dl.get_move("マジカルシャイン") is not None)
_mv_マジカルシャイン = dl.get_move("マジカルシャイン")
if _mv_マジカルシャイン:
    _pa_マジカルシャイン = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_マジカルシャイン = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_マジカルシャイン = dmg(_pa_マジカルシャイン, _pd_マジカルシャイン, "マジカルシャイン")
    check("ダメージ計算: マジカルシャイン", _d_マジカルシャイン > 0, f"dmg={_d_マジカルシャイン}")

# ── つぶらなひとみ ──
check("DB: つぶらなひとみ 取得可能", dl.get_move("つぶらなひとみ") is not None)
# つぶらなひとみ: 相手攻撃-1
_mv_dd_つぶらなひとみ = dl.get_move("つぶらなひとみ")
if _mv_dd_つぶらなひとみ:
    _pa_dd = make_poke(type1="フェアリー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_つぶらなひとみ = 0; _dd_ok_つぶらなひとみ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "つぶらなひとみ")
        if _pd_dd.stage_attack != 0: _dd_val_つぶらなひとみ = _pd_dd.stage_attack; _dd_ok_つぶらなひとみ = True; break
    check("相手攻撃-1: つぶらなひとみ", _dd_ok_つぶらなひとみ and _dd_val_つぶらなひとみ == -1, f"1回適用={_dd_val_つぶらなひとみ} 期待=-1")
# つぶらなひとみ: 優先度1
_mv_pr_つぶらなひとみ = dl.get_move("つぶらなひとみ")
if _mv_pr_つぶらなひとみ and _mv_pr_つぶらなひとみ.priority == 1:
    check("優先度1: つぶらなひとみ", _mv_pr_つぶらなひとみ.priority == 1)
elif _mv_pr_つぶらなひとみ:
    check("優先度1: つぶらなひとみ", _mv_pr_つぶらなひとみ.priority == 1, f"DB優先度={_mv_pr_つぶらなひとみ.priority} 仕様=1")

# ── ほっぺすりすり ──
check("DB: ほっぺすりすり 取得可能", dl.get_move("ほっぺすりすり") is not None)
_mv_ほっぺすりすり = dl.get_move("ほっぺすりすり")
if _mv_ほっぺすりすり:
    _pa_ほっぺすりすり = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ほっぺすりすり = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ほっぺすりすり = dmg(_pa_ほっぺすりすり, _pd_ほっぺすりすり, "ほっぺすりすり")
    check("ダメージ計算: ほっぺすりすり", _d_ほっぺすりすり > 0, f"dmg={_d_ほっぺすりすり}")
# ほっぺすりすり: まひ100%
_mv_s_ほっぺすりすり = dl.get_move("ほっぺすりすり")
if _mv_s_ほっぺすりすり:
    random.seed(0); _hit_ほっぺすりすり = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ほっぺすりすり")
        _hit_ほっぺすりすり += int((_pd2.status == "paralysis"))
    check("追加効果(まひ100%): ほっぺすりすり", 90 <= _hit_ほっぺすりすり <= 525, f"count={_hit_ほっぺすりすり}/300")
    random.seed(1); _immok_ほっぺすりすり = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ほっぺすりすり")
        if _pdi.status == "paralysis": _immok_ほっぺすりすり = False; break
    check("まひ免疫(でんき型には無効): ほっぺすりすり", _immok_ほっぺすりすり, "免疫タイプに状態異常が付与されないこと")

# ── まとわりつく ──
check("DB: まとわりつく 取得可能", dl.get_move("まとわりつく") is not None)
_mv_まとわりつく = dl.get_move("まとわりつく")
if _mv_まとわりつく:
    _pa_まとわりつく = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_まとわりつく = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_まとわりつく = dmg(_pa_まとわりつく, _pd_まとわりつく, "まとわりつく")
    check("ダメージ計算: まとわりつく", _d_まとわりつく > 0, f"dmg={_d_まとわりつく}")
# まとわりつく: バインド
_mv_bd_まとわりつく = dl.get_move("まとわりつく")
if _mv_bd_まとわりつく:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="むし", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="くさ", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "まとわりつく")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: まとわりつく", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── はめつのひかり ──
check("DB: はめつのひかり 取得可能", dl.get_move("はめつのひかり") is not None)
_mv_はめつのひかり = dl.get_move("はめつのひかり")
if _mv_はめつのひかり:
    _pa_はめつのひかり = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_はめつのひかり = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_はめつのひかり = dmg(_pa_はめつのひかり, _pd_はめつのひかり, "はめつのひかり")
    check("ダメージ計算: はめつのひかり", _d_はめつのひかり > 0, f"dmg={_d_はめつのひかり}")
# はめつのひかり: 反動（与ダメの1/2）
_mvrc_はめつのひかり = dl.get_move("はめつのひかり")
if _mvrc_はめつのひかり:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="フェアリー", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="ドラゴン", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "はめつのひかり")
        _rc_dealt_はめつのひかり = _hpdr - _pdr.hp; _rc_rcv_はめつのひかり = _par.max_hp - _par.hp
        if _rc_dealt_はめつのひかり > 0: break
    _rc_exp_はめつのひかり = max(1, _rc_dealt_はめつのひかり // 2)
    check("反動ダメージ(1/2): はめつのひかり", abs(_rc_rcv_はめつのひかり - _rc_exp_はめつのひかり) <= 2, f"dealt={_rc_dealt_はめつのひかり} recoil={_rc_rcv_はめつのひかり} 期待={_rc_exp_はめつのひかり}")

# ── トーチカ ──
check("DB: トーチカ 取得可能", dl.get_move("トーチカ") is not None)
# トーチカ: 優先度4
_mv_pr_ト_チカ = dl.get_move("トーチカ")
if _mv_pr_ト_チカ and _mv_pr_ト_チカ.priority == 4:
    check("優先度4: トーチカ", _mv_pr_ト_チカ.priority == 4)
elif _mv_pr_ト_チカ:
    check("優先度4: トーチカ", _mv_pr_ト_チカ.priority == 4, f"DB優先度={_mv_pr_ト_チカ.priority} 仕様=4")
# トーチカ: 守る成功+接触攻撃者をどく
_pto = make_poke(type1="どく"); execute(_pto, make_poke(), "トーチカ")
check("トーチカ 守る状態: トーチカ", _pto.protecting)
_atk_t = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _pto2 = make_poke(type1="どく")
_pto2.protecting = True; _pto2._protect_move = "トーチカ"
_execute_move(BattleSide([_atk_t]), BattleSide([_pto2]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())
check("トーチカ 接触どく: トーチカ", _atk_t.status == "poison", f"status={_atk_t.status}")

# ── であいがしら ──
check("DB: であいがしら 取得可能", dl.get_move("であいがしら") is not None)
_mv_であいがしら = dl.get_move("であいがしら")
if _mv_であいがしら:
    _pa_であいがしら = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_であいがしら = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_であいがしら = dmg(_pa_であいがしら, _pd_であいがしら, "であいがしら")
    check("ダメージ計算: であいがしら", _d_であいがしら > 0, f"dmg={_d_であいがしら}")
# であいがしら: 優先度2
_mv_pr_であいがしら = dl.get_move("であいがしら")
if _mv_pr_であいがしら and _mv_pr_であいがしら.priority == 2:
    check("優先度2: であいがしら", _mv_pr_であいがしら.priority == 2)
elif _mv_pr_であいがしら:
    check("優先度2: であいがしら", _mv_pr_であいがしら.priority == 2, f"DB優先度={_mv_pr_であいがしら.priority} 仕様=2")
# であいがしら: 場に出て最初のターンのみ成功（turns_out>0は失敗）
_pnk = make_poke(type1="むし", atk_b=120); _dnk = make_poke(type1="くさ", hp_b=255, def_b=150)
_pnk.turns_out = 1; _hpnk = _dnk.hp; execute(_pnk, _dnk, "であいがしら")
check("初手以外で失敗: であいがしら", _dnk.hp == _hpnk, f"hp={_dnk.hp}/{_hpnk}")
_pnk2 = make_poke(type1="むし", atk_b=120); _dnk2 = make_poke(type1="くさ", hp_b=255, def_b=150)
_pnk2.turns_out = 0; _hpnk2 = _dnk2.hp; execute(_pnk2, _dnk2, "であいがしら")
check("初手で成功: であいがしら", _dnk2.hp < _hpnk2, f"hp={_dnk2.hp}/{_hpnk2}")

# ── DDラリアット ──
check("DB: DDラリアット 取得可能", dl.get_move("DDラリアット") is not None)
_mv_DDラリアット = dl.get_move("DDラリアット")
if _mv_DDラリアット:
    _pa_DDラリアット = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_DDラリアット = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_DDラリアット = dmg(_pa_DDラリアット, _pd_DDラリアット, "DDラリアット")
    check("ダメージ計算: DDラリアット", _d_DDラリアット > 0, f"dmg={_d_DDラリアット}")
# DDラリアット: 相手の防御ランク上昇を無視
_pdd = make_poke(type1="あく", atk_b=100)
_ddd = make_poke(type1="ノーマル", def_b=100); _ddd.stage_defense = 6
_dd_ignore = calc_damage(_pdd, _ddd, dl.get_move("DDラリアット"), BattleField(), random_roll=1.0)
_ddn = make_poke(type1="ノーマル", def_b=100)
_dd_normal = calc_damage(_pdd, _ddn, dl.get_move("DDラリアット"), BattleField(), random_roll=1.0)
check("防御ランク上昇無視: DDラリアット", _dd_ignore == _dd_normal, f"ignore={_dd_ignore} normal={_dd_normal}")
# 防御ランク低下も無視（相手が防御-6でも軽減されない＝通常と同ダメージ）
_ddlo = make_poke(type1="ノーマル", def_b=100); _ddlo.stage_defense = -6
_dd_low = calc_damage(_pdd, _ddlo, dl.get_move("DDラリアット"), BattleField(), random_roll=1.0)
check("防御ランク低下も無視: DDラリアット", _dd_low == _dd_normal, f"low={_dd_low} normal={_dd_normal}")

# ── かげぬい ──
check("DB: かげぬい 取得可能", dl.get_move("かげぬい") is not None)
_mv_かげぬい = dl.get_move("かげぬい")
if _mv_かげぬい:
    _pa_かげぬい = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_かげぬい = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_かげぬい = dmg(_pa_かげぬい, _pd_かげぬい, "かげぬい")
    check("ダメージ計算: かげぬい", _d_かげぬい > 0, f"dmg={_d_かげぬい}")
# かげぬい: 相手をにげられない状態に
_ptr = make_poke(type1="ゴースト", atk_b=120); _dtr = make_poke(type1="エスパー", hp_b=255, def_b=100)
execute(_ptr, _dtr, "かげぬい")
check("にげられない付与: かげぬい", _dtr.trapped)

# ── アイスハンマー ──
check("DB: アイスハンマー 取得可能", dl.get_move("アイスハンマー") is not None)
_mv_アイスハンマ_ = dl.get_move("アイスハンマー")
if _mv_アイスハンマ_:
    _pa_アイスハンマ_ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_アイスハンマ_ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_アイスハンマ_ = dmg(_pa_アイスハンマ_, _pd_アイスハンマ_, "アイスハンマー")
    check("ダメージ計算: アイスハンマー", _d_アイスハンマ_ > 0, f"dmg={_d_アイスハンマ_}")
# アイスハンマー: 自分素早さ-1
_mvss_アイスハンマ__speed = dl.get_move("アイスハンマー")
if _mvss_アイスハンマ__speed:
    random.seed(0); _got_アイスハンマ__speed = 0
    for _ in range(60):
        _pas = make_poke(type1="こおり", atk_b=60, spatk_b=60); _pds = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "アイスハンマー")
        if _pas.stage_speed != 0: _got_アイスハンマ__speed = _pas.stage_speed; break
    check("自分素早さ-1: アイスハンマー", _got_アイスハンマ__speed == -1, f"1回適用={_got_アイスハンマ__speed} 期待=-1")

# ── うたかたのアリア ──
check("DB: うたかたのアリア 取得可能", dl.get_move("うたかたのアリア") is not None)
_mv_うたかたのアリア = dl.get_move("うたかたのアリア")
if _mv_うたかたのアリア:
    _pa_うたかたのアリア = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_うたかたのアリア = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_うたかたのアリア = dmg(_pa_うたかたのアリア, _pd_うたかたのアリア, "うたかたのアリア")
    check("ダメージ計算: うたかたのアリア", _d_うたかたのアリア > 0, f"dmg={_d_うたかたのアリア}")
# うたかたのアリア: 相手のやけどを治す
_pu = make_poke(type1="みず", spatk_b=100); _du = make_poke(type1="ノーマル", hp_b=255, spdef_b=200); _du.status = "burn"
execute(_pu, _du, "うたかたのアリア")
check("やけど治癒: うたかたのアリア", _du.status is None, f"status={_du.status}")

# ── ソーラーブレード ──
check("DB: ソーラーブレード 取得可能", dl.get_move("ソーラーブレード") is not None)
_mv_ソ_ラ_ブレ_ド = dl.get_move("ソーラーブレード")
if _mv_ソ_ラ_ブレ_ド:
    _pa_ソ_ラ_ブレ_ド = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ソ_ラ_ブレ_ド = make_poke(type1="みず", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_ソ_ラ_ブレ_ド = make_poke(type1="くさ", atk_b=100, spatk_b=100); _pd_ソ_ラ_ブレ_ド = make_poke(type1="みず", def_b=100, spdef_b=100)
        execute(_pa_ソ_ラ_ブレ_ド, _pd_ソ_ラ_ブレ_ド, "ソーラーブレード"); execute(_pa_ソ_ラ_ブレ_ド, _pd_ソ_ラ_ブレ_ド, "ソーラーブレード")
        if _pd_ソ_ラ_ブレ_ド.hp < _pd_ソ_ラ_ブレ_ド.max_hp: break
    check("ダメージ計算: ソーラーブレード", _pd_ソ_ラ_ブレ_ド.hp < _pd_ソ_ラ_ブレ_ド.max_hp, f"hp={_pd_ソ_ラ_ブレ_ド.hp}")
# ソーラーブレード: 2ターン溜め
_mv_2t_ソ_ラ_ブレ_ド = dl.get_move("ソーラーブレード")
if _mv_2t_ソ_ラ_ブレ_ド:
    _pa_2t = make_poke(type1="くさ", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="みず", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "ソーラーブレード")
    check("2ターン溜め(1T)ダメなし: ソーラーブレード", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: ソーラーブレード", _pa_2t.charging_move == "ソーラーブレード")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "ソーラーブレード")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "ソーラーブレード")
    check("2ターン溜め(2T)ダメあり: ソーラーブレード", _pd_2t.hp < _hp_before_2t)
# ソーラーブレード: にほんばれ状態では溜めず即攻撃（1ターン目でダメージ）
_fwi_ソ_ラ_ブレ_ド = BattleField(); _fwi_ソ_ラ_ブレ_ド.weather = "sunny"
_pwi_ソ_ラ_ブレ_ド = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dwi_ソ_ラ_ブレ_ド = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100); _hpwi_ソ_ラ_ブレ_ド = _dwi_ソ_ラ_ブレ_ド.hp
execute(_pwi_ソ_ラ_ブレ_ド, _dwi_ソ_ラ_ブレ_ド, "ソーラーブレード", _fwi_ソ_ラ_ブレ_ド)
check("にほんばれで即発動(1Tダメージ): ソーラーブレード", _dwi_ソ_ラ_ブレ_ド.hp < _hpwi_ソ_ラ_ブレ_ド and _pwi_ソ_ラ_ブレ_ド.charging_move is None, f"hp={_dwi_ソ_ラ_ブレ_ド.hp}/{_hpwi_ソ_ラ_ブレ_ド} charging={_pwi_ソ_ラ_ブレ_ド.charging_move}")
# ソーラーブレード: 晴れ以外の天候は威力1/2
_psb = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsb = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120)
_fsun = BattleField(); _fsun.weather = "sunny"; _frain = BattleField(); _frain.weather = "rain"
_sb_sun = calc_damage(_psb, _dsb, dl.get_move("ソーラーブレード"), _fsun, random_roll=1.0); _sb_rain = calc_damage(_psb, _dsb, dl.get_move("ソーラーブレード"), _frain, random_roll=1.0)
check("天候半減: ソーラーブレード", _sb_rain < _sb_sun, f"sun={_sb_sun} rain={_sb_rain}")
# 無天候は溜めが必要（1ターン目ダメなし）
_pno = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dno = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpno = _dno.hp
execute(_pno, _dno, "ソーラーブレード")
check("無天候は溜め(1Tダメなし): ソーラーブレード", _dno.hp == _hpno and _pno.charging_move == "ソーラーブレード", f"hp={_dno.hp}/{_hpno} charging={_pno.charging_move}")
# にほんばれ中は溜めず即攻撃（1ターン目でダメージ）
_psn = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsn = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpsn = _dsn.hp
_fsun2 = BattleField(); _fsun2.weather = "sunny"
execute(_psn, _dsn, "ソーラーブレード", _fsun2)
check("晴れは即発動(1Tでダメージ): ソーラーブレード", _dsn.hp < _hpsn and _psn.charging_move is None, f"hp={_dsn.hp}/{_hpsn} charging={_psn.charging_move}")
# 威力半減の具体値（125→62）
_psx = make_poke(type1="くさ", atk_b=100, spatk_b=100); _dsx = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
_pwr_norm = _ep(_psx, _dsx, dl.get_move("ソーラーブレード"), BattleField())
_frx = BattleField(); _frx.weather = "rain"; _pwr_rain = _ep(_psx, _dsx, dl.get_move("ソーラーブレード"), _frx)
check("通常威力125: ソーラーブレード", _pwr_norm == 125, f"norm={_pwr_norm}")
check("天候半減(62): ソーラーブレード", _pwr_rain == 62, f"rain={_pwr_rain}")

# ── ちからをすいとる ──
check("DB: ちからをすいとる 取得可能", dl.get_move("ちからをすいとる") is not None)
# ちからをすいとる: 相手攻撃-1
_mv_dd_ちからをすいとる = dl.get_move("ちからをすいとる")
if _mv_dd_ちからをすいとる:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ちからをすいとる = 0; _dd_ok_ちからをすいとる = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ちからをすいとる")
        if _pd_dd.stage_attack != 0: _dd_val_ちからをすいとる = _pd_dd.stage_attack; _dd_ok_ちからをすいとる = True; break
    check("相手攻撃-1: ちからをすいとる", _dd_ok_ちからをすいとる and _dd_val_ちからをすいとる == -1, f"1回適用={_dd_val_ちからをすいとる} 期待=-1")
# ちからをすいとる: 相手の攻撃実数値分回復 + 相手の攻撃-1
_pcs = make_poke(type1="フェアリー"); _pcs.hp = 1
_dcs = make_poke(type1="ノーマル", atk_b=120, hp_b=255)
_opp_atk = _dcs.attack; execute(_pcs, _dcs, "ちからをすいとる")
check("相手攻撃実数値分回復: ちからをすいとる", abs(_pcs.hp - 1 - _opp_atk) <= 2, f"heal={_pcs.hp-1} opp_atk={_opp_atk}")
check("相手攻撃-1: ちからをすいとる", _dcs.stage_attack == -1, f"atk={_dcs.stage_attack}")

# ── どくのいと ──
check("DB: どくのいと 取得可能", dl.get_move("どくのいと") is not None)
# どくのいと: 相手素早さ-2
_mv_dd_どくのいと = dl.get_move("どくのいと")
if _mv_dd_どくのいと:
    _pa_dd = make_poke(type1="どく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_どくのいと = 0; _dd_ok_どくのいと = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "どくのいと")
        if _pd_dd.stage_speed != 0: _dd_val_どくのいと = _pd_dd.stage_speed; _dd_ok_どくのいと = True; break
    check("相手素早さ-2: どくのいと", _dd_ok_どくのいと and _dd_val_どくのいと == -2, f"1回適用={_dd_val_どくのいと} 期待=-2")
# どくのいと: どく付与(変化技)
_mv_si_どくのいと = dl.get_move("どくのいと")
if _mv_si_どくのいと:
    random.seed(0); _ok_どくのいと = False
    for _ in range(30):
        _pa_si = make_poke(type1="どく"); _pd_si = make_poke(type1="くさ", hp_b=255)
        execute(_pa_si, _pd_si, "どくのいと")
        if _pd_si.status == "poison": _ok_どくのいと = True; break
    check("どく付与: どくのいと", _ok_どくのいと)
    random.seed(2); _siimm_どくのいと = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="どく", hp_b=255)
        execute(_pai2, _pdi2, "どくのいと")
        if _pdi2.status == "poison": _siimm_どくのいと = False; break
    check("どく免疫(どく型には無効): どくのいと", _siimm_どくのいと, "免疫タイプに付与されないこと")
    random.seed(2); _siimm_どくのいと = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="はがね", hp_b=255)
        execute(_pai2, _pdi2, "どくのいと")
        if _pdi2.status == "poison": _siimm_どくのいと = False; break
    check("どく免疫(はがね型には無効): どくのいと", _siimm_どくのいと, "免疫タイプに付与されないこと")

# ── じごくづき ──
check("DB: じごくづき 取得可能", dl.get_move("じごくづき") is not None)
_mv_じごくづき = dl.get_move("じごくづき")
if _mv_じごくづき:
    _pa_じごくづき = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_じごくづき = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_じごくづき = dmg(_pa_じごくづき, _pd_じごくづき, "じごくづき")
    check("ダメージ計算: じごくづき", _d_じごくづき > 0, f"dmg={_d_じごくづき}")
# じごくづき: じごくづき状態
_mv_tc_じごくづき = dl.get_move("じごくづき")
if _mv_tc_じごくづき:
    random.seed(0)
    for _ in range(20):
        _pa_tc = make_poke(type1="あく", atk_b=150, spatk_b=150); _pd_tc = make_poke(type1="エスパー", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_tc, _pd_tc, "じごくづき")
        if _pd_tc.throat_chop_count == 2: break
    check("じごくづき付与: じごくづき", _pd_tc.throat_chop_count == 2)
    # 効果本体: じごくづき中は音技が使えない
    _ptc2 = make_poke(type1="ノーマル", spatk_b=100); _ptc2.throat_chop_count = 2
    _dtc2 = make_poke(type1="あく", hp_b=255, spdef_b=200); _hptc = _dtc2.hp
    execute(_ptc2, _dtc2, "ハイパーボイス")
    check("じごくづき中は音技不可: じごくづき", _dtc2.hp == _hptc, f"hp={_dtc2.hp}/{_hptc}")

# ── とびかかる ──
check("DB: とびかかる 取得可能", dl.get_move("とびかかる") is not None)
_mv_とびかかる = dl.get_move("とびかかる")
if _mv_とびかかる:
    _pa_とびかかる = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_とびかかる = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_とびかかる = dmg(_pa_とびかかる, _pd_とびかかる, "とびかかる")
    check("ダメージ計算: とびかかる", _d_とびかかる > 0, f"dmg={_d_とびかかる}")
# とびかかる: 相手攻撃-1
_mv_dd_とびかかる = dl.get_move("とびかかる")
if _mv_dd_とびかかる:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_とびかかる = 0; _dd_ok_とびかかる = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "とびかかる")
        if _pd_dd.stage_attack != 0: _dd_val_とびかかる = _pd_dd.stage_attack; _dd_ok_とびかかる = True; break
    check("相手攻撃-1: とびかかる", _dd_ok_とびかかる and _dd_val_とびかかる == -1, f"1回適用={_dd_val_とびかかる} 期待=-1")

# ── サイコフィールド ──
check("DB: サイコフィールド 取得可能", dl.get_move("サイコフィールド") is not None)
# サイコフィールド: フィールド展開
_mvfl_サイコフィ_ルド = dl.get_move("サイコフィールド")
if _mvfl_サイコフィ_ルド:
    _s1f, _s2f, _ff = execute_ctx(make_poke(type1="エスパー"), make_poke(), "サイコフィールド")
    check("フィールドpsychic_terrain: サイコフィールド", _ff.psychic_terrain, f"val={_ff.psychic_terrain}")

# ── もえつきる ──
check("DB: もえつきる 取得可能", dl.get_move("もえつきる") is not None)
_mv_もえつきる = dl.get_move("もえつきる")
if _mv_もえつきる:
    _pa_もえつきる = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_もえつきる = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_もえつきる = dmg(_pa_もえつきる, _pd_もえつきる, "もえつきる")
    check("ダメージ計算: もえつきる", _d_もえつきる > 0, f"dmg={_d_もえつきる}")
# もえつきる: 非ほのおは失敗、ほのおなら攻撃後に自分のほのおが消える
_pmf = make_poke(type1="みず", spatk_b=100); _dmf = make_poke(type1="くさ", hp_b=255, spdef_b=150)
_hpm1 = _dmf.hp; execute(_pmf, _dmf, "もえつきる")
check("非ほのお失敗: もえつきる", _dmf.hp == _hpm1, f"hp={_dmf.hp}/{_hpm1}")
_pms = make_poke(type1="ほのお", spatk_b=120); _dms = make_poke(type1="くさ", hp_b=255, spdef_b=150)
execute(_pms, _dms, "もえつきる")
check("ほのおタイプ消失: もえつきる", "ほのお" not in (_pms.type1, _pms.type2), f"types={_pms.type1}/{_pms.type2}")
# 使うと自分のこおり状態を治す
_pmt = make_poke(type1="ほのお", spatk_b=100); _pmt.status = "freeze"
execute(_pmt, make_poke(type1="くさ", hp_b=255), "もえつきる")
check("自分こおり治癒: もえつきる", _pmt.status != "freeze", f"status={_pmt.status}")

# ── つけあがる ──
check("DB: つけあがる 取得可能", dl.get_move("つけあがる") is not None)
_mv_つけあがる = dl.get_move("つけあがる")
if _mv_つけあがる:
    _pa_つけあがる = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_つけあがる = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_つけあがる = dmg(_pa_つけあがる, _pd_つけあがる, "つけあがる")
    check("ダメージ計算: つけあがる", _d_つけあがる > 0, f"dmg={_d_つけあがる}")
# つけあがる: 自分のランク合計で威力増（20+20×ランク）
_pap2 = make_poke(type1="あく", spatk_b=100, atk_b=100); _dap2 = make_poke(type1="エスパー", def_b=100, spdef_b=100)
_pw_base = _ep(_pap2, _dap2, dl.get_move("つけあがる"), BattleField())
_pap2.stage_attack = 2; _pap2.stage_speed = 1
_pw_up = _ep(_pap2, _dap2, dl.get_move("つけあがる"), BattleField())
check("ランクで威力増: つけあがる", _pw_base == 20 and _pw_up == 20 + 20*3, f"base={_pw_base} up={_pw_up}")

# ── さいはい ──
check("DB: さいはい 取得可能", dl.get_move("さいはい") is not None)
# さいはい: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: さいはい", "さいはい", "エスパー", False, smoke=("さいはい" in DOUBLE_ONLY_SMOKE))

# ── トロピカルキック ──
check("DB: トロピカルキック 取得可能", dl.get_move("トロピカルキック") is not None)
_mv_トロピカルキック = dl.get_move("トロピカルキック")
if _mv_トロピカルキック:
    _pa_トロピカルキック = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_トロピカルキック = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_トロピカルキック = dmg(_pa_トロピカルキック, _pd_トロピカルキック, "トロピカルキック")
    check("ダメージ計算: トロピカルキック", _d_トロピカルキック > 0, f"dmg={_d_トロピカルキック}")
# トロピカルキック: 相手攻撃-1
_mv_dd_トロピカルキック = dl.get_move("トロピカルキック")
if _mv_dd_トロピカルキック:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_トロピカルキック = 0; _dd_ok_トロピカルキック = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "トロピカルキック")
        if _pd_dd.stage_attack != 0: _dd_val_トロピカルキック = _pd_dd.stage_attack; _dd_ok_トロピカルキック = True; break
    check("相手攻撃-1: トロピカルキック", _dd_ok_トロピカルキック and _dd_val_トロピカルキック == -1, f"1回適用={_dd_val_トロピカルキック} 期待=-1")

# ── くちばしキャノン ──
check("DB: くちばしキャノン 取得可能", dl.get_move("くちばしキャノン") is not None)
_mv_くちばしキャノン = dl.get_move("くちばしキャノン")
if _mv_くちばしキャノン:
    _pa_くちばしキャノン = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_くちばしキャノン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_くちばしキャノン = dmg(_pa_くちばしキャノン, _pd_くちばしキャノン, "くちばしキャノン")
    check("ダメージ計算: くちばしキャノン", _d_くちばしキャノン > 0, f"dmg={_d_くちばしキャノン}")
# くちばしキャノン: 優先度-3
_mv_pr_くちばしキャノン = dl.get_move("くちばしキャノン")
if _mv_pr_くちばしキャノン and _mv_pr_くちばしキャノン.priority == -3:
    check("優先度-3: くちばしキャノン", _mv_pr_くちばしキャノン.priority == -3)
elif _mv_pr_くちばしキャノン:
    check("優先度-3: くちばしキャノン", _mv_pr_くちばしキャノン.priority == -3, f"DB優先度={_mv_pr_くちばしキャノン.priority} 仕様=-3")
# くちばしキャノン: 使用したそのターンに接触技を受けた相手をやけど（同一ターン内・ターンまたぎ無し）
from simulator.battle import Battle as _Bk
_act_beak = lambda s,o,f: Action(type="move", move=dl.get_move("くちばしキャノン"), move_idx=0)
_act_tackle = lambda s,o,f: Action(type="move", move=dl.get_move("のしかかり"), move_idx=0)
# 同一ターン: 鳥がくちばしキャノン(-3で後攻)、相手が接触技で先制 → 相手やけど
_bird = make_poke(type1="ひこう", hp_b=255, atk_b=10, moves=["くちばしキャノン"])
_foe = make_poke(type1="ノーマル", atk_b=40, hp_b=255, def_b=255, moves=["のしかかり"])
_bk1 = _Bk(BattleSide([_bird]), BattleSide([_foe])); _bk1.run(_act_beak, _act_tackle)
check("くちばしキャノン 被弾やけど: くちばしキャノン", _foe.status == "burn", f"status={_foe.status}")
# ターンまたぎ無し: 鳥が別の技を使ったターンは接触してもやけどしない
_bird2 = make_poke(type1="ひこう", hp_b=255, atk_b=10, moves=["のしかかり"])
_foe2 = make_poke(type1="ノーマル", atk_b=40, hp_b=255, def_b=255, moves=["のしかかり"])
_bk2 = _Bk(BattleSide([_bird2]), BattleSide([_foe2])); _bk2.run(_act_tackle, _act_tackle)
check("くちばしキャノン 非使用ターンはやけど無し: くちばしキャノン", _foe2.status != "burn", f"status={_foe2.status}")

# ── スケイルノイズ ──
check("DB: スケイルノイズ 取得可能", dl.get_move("スケイルノイズ") is not None)
_mv_スケイルノイズ = dl.get_move("スケイルノイズ")
if _mv_スケイルノイズ:
    _pa_スケイルノイズ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_スケイルノイズ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_スケイルノイズ = dmg(_pa_スケイルノイズ, _pd_スケイルノイズ, "スケイルノイズ")
    check("ダメージ計算: スケイルノイズ", _d_スケイルノイズ > 0, f"dmg={_d_スケイルノイズ}")
# スケイルノイズ: 自分防御-1
_mvss_スケイルノイズ_defense = dl.get_move("スケイルノイズ")
if _mvss_スケイルノイズ_defense:
    random.seed(0); _got_スケイルノイズ_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="ドラゴン", atk_b=60, spatk_b=60); _pds = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "スケイルノイズ")
        if _pas.stage_defense != 0: _got_スケイルノイズ_defense = _pas.stage_defense; break
    check("自分防御-1: スケイルノイズ", _got_スケイルノイズ_defense == -1, f"1回適用={_got_スケイルノイズ_defense} 期待=-1")

# ── ぶんまわす ──
check("DB: ぶんまわす 取得可能", dl.get_move("ぶんまわす") is not None)
_mv_ぶんまわす = dl.get_move("ぶんまわす")
if _mv_ぶんまわす:
    _pa_ぶんまわす = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ぶんまわす = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ぶんまわす = dmg(_pa_ぶんまわす, _pd_ぶんまわす, "ぶんまわす")
    check("ダメージ計算: ぶんまわす", _d_ぶんまわす > 0, f"dmg={_d_ぶんまわす}")

# ── オーロラベール ──
check("DB: オーロラベール 取得可能", dl.get_move("オーロラベール") is not None)
# オーロラベール: スクリーンaurora_veil
_mv_sc_オ_ロラベ_ル = dl.get_move("オーロラベール")
if _mv_sc_オ_ロラベ_ル:
    _fsc = BattleField(); _fsc.weather = "hail"
    _s1sc, _s2sc, _fsc = execute_ctx(make_poke(type1="こおり"), make_poke(), "オーロラベール", _fsc)
    check("スクリーンaurora_veil: オーロラベール", _s1sc.aurora_veil, f"aurora_veil={_s1sc.aurora_veil}")
# オーロラベール: ゆき(hail)下でのみ成功し、ゆき以外では失敗
_sav = BattleSide([make_poke(type1="こおり")]); _fav = BattleField(); _fav.weather = "hail"
_execute_move(_sav, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("オーロラベール")), _fav)
check("ゆき下で成功: オーロラベール", _sav.aurora_veil, f"av={_sav.aurora_veil}")
_sav2 = BattleSide([make_poke(type1="こおり")]); _fav2 = BattleField()
_execute_move(_sav2, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("オーロラベール")), _fav2)
check("ゆき以外では失敗(negative): オーロラベール", not _sav2.aurora_veil, f"av={_sav2.aurora_veil}")

# ── サイコファング ──
check("DB: サイコファング 取得可能", dl.get_move("サイコファング") is not None)
_mv_サイコファング = dl.get_move("サイコファング")
if _mv_サイコファング:
    _pa_サイコファング = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_サイコファング = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_サイコファング = dmg(_pa_サイコファング, _pd_サイコファング, "サイコファング")
    check("ダメージ計算: サイコファング", _d_サイコファング > 0, f"dmg={_d_サイコファング}")
# サイコファング: スクリーン破壊
_mvbrk_サイコファング = dl.get_move("サイコファング")
if _mvbrk_サイコファング:
    random.seed(0); _brk_ok = False
    for _ in range(20):
        _pabrk = make_poke(type1="エスパー", atk_b=120, spatk_b=120); _pdbrk = make_poke(type1="かくとう", hp_b=255, def_b=100, spdef_b=100)
        _s1b = BattleSide([_pabrk]); _s2b = BattleSide([_pdbrk])
        _s2b.reflect = True; _s2b.reflect_count = 5; _s2b.light_screen = True; _s2b.light_screen_count = 5
        _execute_move(_s1b, _s2b, Action(type="move", move=_mvbrk_サイコファング), BattleField())
        if not _s2b.reflect and not _s2b.light_screen: _brk_ok = True; break
    check("スクリーン破壊: サイコファング", _brk_ok)

# ── じだんだ ──
check("DB: じだんだ 取得可能", dl.get_move("じだんだ") is not None)
_mv_じだんだ = dl.get_move("じだんだ")
if _mv_じだんだ:
    _pa_じだんだ = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_じだんだ = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_じだんだ = dmg(_pa_じだんだ, _pd_じだんだ, "じだんだ")
    check("ダメージ計算: じだんだ", _d_じだんだ > 0, f"dmg={_d_じだんだ}")
# じだんだ: 前ターン失敗で威力2倍（実効威力で厳密比較）
_mvj = dl.get_move("じだんだ")
_paj = make_poke(type1="じめん", atk_b=100, spatk_b=100); _pdj = make_poke(type1="でんき", def_b=100, spdef_b=100)
_p_normal = _ep(_paj, _pdj, _mvj, BattleField())
_paj._move_failed_last = True
_p_double = _ep(_paj, _pdj, _mvj, BattleField())
check("前ターン失敗2倍: じだんだ", _p_double == _p_normal * 2, f"normal={_p_normal} double={_p_double}")
# 条件成立: 技を外すと _move_failed_this_turn が立つ（実戦arising）
import copy as _cpj; _mvmiss = _cpj.copy(_mvj); _mvmiss.accuracy = 1
random.seed(0); _missset = False
for _ in range(40):
    _pjm = make_poke(type1="じめん", atk_b=100, spatk_b=100); _djm = make_poke(type1="でんき", hp_b=255)
    _execute_move(BattleSide([_pjm]), BattleSide([_djm]), Action(type="move", move=_mvmiss), BattleField())
    if getattr(_pjm, "_move_failed_this_turn", False): _missset = True; break
check("外すと失敗フラグ成立: じだんだ", _missset, "技を外すと_move_failed_this_turnが立つこと")
# ターン終了で前ターン失敗へ繰り越す
from simulator.battle import Battle as _Bjd
_pcarry = make_poke(type1="じめん"); _pcarry._move_failed_this_turn = True
_Bjd(BattleSide([_pcarry]), BattleSide([make_poke()]))._end_of_turn()
check("失敗フラグ繰り越し: じだんだ", _pcarry._move_failed_last, "ターン終了で_move_failed_lastに繰り越すこと")

# ── アクセルロック ──
check("DB: アクセルロック 取得可能", dl.get_move("アクセルロック") is not None)
_mv_アクセルロック = dl.get_move("アクセルロック")
if _mv_アクセルロック:
    _pa_アクセルロック = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_アクセルロック = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_アクセルロック = dmg(_pa_アクセルロック, _pd_アクセルロック, "アクセルロック")
    check("ダメージ計算: アクセルロック", _d_アクセルロック > 0, f"dmg={_d_アクセルロック}")
# アクセルロック: 優先度1
_mv_pr_アクセルロック = dl.get_move("アクセルロック")
if _mv_pr_アクセルロック and _mv_pr_アクセルロック.priority == 1:
    check("優先度1: アクセルロック", _mv_pr_アクセルロック.priority == 1)
elif _mv_pr_アクセルロック:
    check("優先度1: アクセルロック", _mv_pr_アクセルロック.priority == 1, f"DB優先度={_mv_pr_アクセルロック.priority} 仕様=1")

# ── アクアブレイク ──
check("DB: アクアブレイク 取得可能", dl.get_move("アクアブレイク") is not None)
_mv_アクアブレイク = dl.get_move("アクアブレイク")
if _mv_アクアブレイク:
    _pa_アクアブレイク = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_アクアブレイク = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_アクアブレイク = dmg(_pa_アクアブレイク, _pd_アクアブレイク, "アクアブレイク")
    check("ダメージ計算: アクアブレイク", _d_アクアブレイク > 0, f"dmg={_d_アクアブレイク}")
# アクアブレイク: 相手防御-1
_mv_dd_アクアブレイク = dl.get_move("アクアブレイク")
if _mv_dd_アクアブレイク:
    _pa_dd = make_poke(type1="みず", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_アクアブレイク = 0; _dd_ok_アクアブレイク = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ほのお", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "アクアブレイク")
        if _pd_dd.stage_defense != 0: _dd_val_アクアブレイク = _pd_dd.stage_defense; _dd_ok_アクアブレイク = True; break
    check("相手防御-1: アクアブレイク", _dd_ok_アクアブレイク and _dd_val_アクアブレイク == -1, f"1回適用={_dd_val_アクアブレイク} 期待=-1")

# ── ほおばる ──
check("DB: ほおばる 取得可能", dl.get_move("ほおばる") is not None)
# ほおばる: きのみ無しは失敗、有りで防御+2&消費
_pbf = make_poke(type1="ノーマル"); execute(_pbf, make_poke(), "ほおばる")
check("きのみ無し失敗: ほおばる", _pbf.stage_defense == 0)
_pbs = make_poke(type1="ノーマル", item="オボンのみ"); execute(_pbs, make_poke(), "ほおばる")
check("防御2段階上昇(+2): ほおばる", _pbs.stage_defense == 2 and _pbs.item is None and _pbs.ate_berry)

# ── ドラゴンアロー ──
check("DB: ドラゴンアロー 取得可能", dl.get_move("ドラゴンアロー") is not None)
_mv_ドラゴンアロ_ = dl.get_move("ドラゴンアロー")
if _mv_ドラゴンアロ_:
    _pa_ドラゴンアロ_ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_ドラゴンアロ_ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ドラゴンアロ_ = dmg(_pa_ドラゴンアロ_, _pd_ドラゴンアロ_, "ドラゴンアロー")
    check("ダメージ計算: ドラゴンアロー", _d_ドラゴンアロ_ > 0, f"dmg={_d_ドラゴンアロ_}")
# ドラゴンアロー: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ドラゴンアロ_ = dl.get_move("ドラゴンアロー")
if _mvmh_ドラゴンアロ_:
    _pam = make_poke(type1="ドラゴン", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ドラゴンアロ_ = calc_damage(_pam, make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200), _mvmh_ドラゴンアロ_, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ドラゴンアロ_ = 0
    for _ in range(20):
        _pdm = make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ドラゴンアロー"); _multi_ドラゴンアロ_ = _pdm.max_hp - _pdm.hp
        if _multi_ドラゴンアロ_ > _single_ドラゴンアロ_: break
    check("多段ヒット発生(複数回): ドラゴンアロー", _multi_ドラゴンアロ_ > _single_ドラゴンアロ_, f"single={_single_ドラゴンアロ_} multi={_multi_ドラゴンアロ_}")

# ── トラバサミ ──
check("DB: トラバサミ 取得可能", dl.get_move("トラバサミ") is not None)
_mv_トラバサミ = dl.get_move("トラバサミ")
if _mv_トラバサミ:
    _pa_トラバサミ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_トラバサミ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_トラバサミ = dmg(_pa_トラバサミ, _pd_トラバサミ, "トラバサミ")
    check("ダメージ計算: トラバサミ", _d_トラバサミ > 0, f"dmg={_d_トラバサミ}")
# トラバサミ: バインド
_mv_bd_トラバサミ = dl.get_move("トラバサミ")
if _mv_bd_トラバサミ:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="はがね", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="こおり", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "トラバサミ")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: トラバサミ", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── ボディプレス ──
check("DB: ボディプレス 取得可能", dl.get_move("ボディプレス") is not None)
_mv_ボディプレス = dl.get_move("ボディプレス")
if _mv_ボディプレス:
    _pa_ボディプレス = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ボディプレス = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ボディプレス = dmg(_pa_ボディプレス, _pd_ボディプレス, "ボディプレス")
    check("ダメージ計算: ボディプレス", _d_ボディプレス > 0, f"dmg={_d_ボディプレス}")
# ボディプレス: 自分の防御でダメージ計算
_pbp_hi = make_poke(type1="かくとう", atk_b=10, def_b=200); _pbp_lo = make_poke(type1="かくとう", atk_b=10, def_b=10)
_dbp = make_poke(type1="ノーマル", def_b=100)
_d_hi = calc_damage(_pbp_hi, _dbp, dl.get_move("ボディプレス"), BattleField(), random_roll=1.0)
_d_lo = calc_damage(_pbp_lo, _dbp, dl.get_move("ボディプレス"), BattleField(), random_roll=1.0)
check("ボディプレス 自分防御依存: ボディプレス", _d_hi > _d_lo, f"hi={_d_hi} lo={_d_lo}")

# ── ソウルビート ──
check("DB: ソウルビート 取得可能", dl.get_move("ソウルビート") is not None)
# ソウルビート: 自分攻撃+1
_mv_sb_ソウルビ_ト_attack = dl.get_move("ソウルビート")
if _mv_sb_ソウルビ_ト_attack:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ソウルビート")
    check("自分攻撃+1: ソウルビート", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# ソウルビート: 自分防御+1
_mv_sb_ソウルビ_ト_defense = dl.get_move("ソウルビート")
if _mv_sb_ソウルビ_ト_defense:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ソウルビート")
    check("自分防御+1: ソウルビート", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")
# ソウルビート: 自分特攻+1
_mv_sb_ソウルビ_ト_sp_attack = dl.get_move("ソウルビート")
if _mv_sb_ソウルビ_ト_sp_attack:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ソウルビート")
    check("自分特攻+1: ソウルビート", _pa_sb.stage_sp_attack == 1, f"1回適用={_pa_sb.stage_sp_attack} 期待=+1")
# ソウルビート: 自分特防+1
_mv_sb_ソウルビ_ト_sp_defense = dl.get_move("ソウルビート")
if _mv_sb_ソウルビ_ト_sp_defense:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ソウルビート")
    check("自分特防+1: ソウルビート", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")
# ソウルビート: 自分素早さ+1
_mv_sb_ソウルビ_ト_speed = dl.get_move("ソウルビート")
if _mv_sb_ソウルビ_ト_speed:
    _pa_sb = make_poke(type1="ドラゴン"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "ソウルビート")
    check("自分素早さ+1: ソウルビート", _pa_sb.stage_speed == 1, f"1回適用={_pa_sb.stage_speed} 期待=+1")
# ソウルビート: HP不足だと失敗、足りれば全能力+1&HP1/3消費
_psf = make_poke(type1="ドラゴン", hp_b=200); _psf.hp = 1; execute(_psf, make_poke(), "ソウルビート")
check("HP不足失敗: ソウルビート", _psf.stage_attack == 0, f"atk={_psf.stage_attack}")
_pss = make_poke(type1="ドラゴン", hp_b=200); execute(_pss, make_poke(), "ソウルビート")
check("ソウルビート成功: ソウルビート", _pss.stage_attack == 1 and _pss.hp < _pss.max_hp, f"atk={_pss.stage_attack} hp={_pss.hp}")

# ── オーラぐるま ──
check("DB: オーラぐるま 取得可能", dl.get_move("オーラぐるま") is not None)
_mv_オ_ラぐるま = dl.get_move("オーラぐるま")
if _mv_オ_ラぐるま:
    _pa_オ_ラぐるま = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_オ_ラぐるま = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_オ_ラぐるま = dmg(_pa_オ_ラぐるま, _pd_オ_ラぐるま, "オーラぐるま")
    check("ダメージ計算: オーラぐるま", _d_オ_ラぐるま > 0, f"dmg={_d_オ_ラぐるま}")
# オーラぐるま: 自分素早さ+1
_mvss_オ_ラぐるま_speed = dl.get_move("オーラぐるま")
if _mvss_オ_ラぐるま_speed:
    random.seed(0); _got_オ_ラぐるま_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="でんき", atk_b=60, spatk_b=60); _pds = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "オーラぐるま")
        if _pas.stage_speed != 0: _got_オ_ラぐるま_speed = _pas.stage_speed; break
    check("自分素早さ+1: オーラぐるま", _got_オ_ラぐるま_speed == 1, f"1回適用={_got_オ_ラぐるま_speed} 期待=1")

# ── りんごさん ──
check("DB: りんごさん 取得可能", dl.get_move("りんごさん") is not None)
_mv_りんごさん = dl.get_move("りんごさん")
if _mv_りんごさん:
    _pa_りんごさん = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_りんごさん = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_りんごさん = dmg(_pa_りんごさん, _pd_りんごさん, "りんごさん")
    check("ダメージ計算: りんごさん", _d_りんごさん > 0, f"dmg={_d_りんごさん}")
# りんごさん: 相手特防-1
_mv_dd_りんごさん = dl.get_move("りんごさん")
if _mv_dd_りんごさん:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_りんごさん = 0; _dd_ok_りんごさん = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "りんごさん")
        if _pd_dd.stage_sp_defense != 0: _dd_val_りんごさん = _pd_dd.stage_sp_defense; _dd_ok_りんごさん = True; break
    check("相手特防-1: りんごさん", _dd_ok_りんごさん and _dd_val_りんごさん == -1, f"1回適用={_dd_val_りんごさん} 期待=-1")

# ── てっていこうせん ──
check("DB: てっていこうせん 取得可能", dl.get_move("てっていこうせん") is not None)
_mv_てっていこうせん = dl.get_move("てっていこうせん")
if _mv_てっていこうせん:
    _pa_てっていこうせん = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_てっていこうせん = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_てっていこうせん = dmg(_pa_てっていこうせん, _pd_てっていこうせん, "てっていこうせん")
    check("ダメージ計算: てっていこうせん", _d_てっていこうせん > 0, f"dmg={_d_てっていこうせん}")
# てっていこうせん: 最大HP1/2の反動
_ptk2 = make_poke(type1="はがね", spatk_b=120); _dtk2 = make_poke(type1="いわ", hp_b=255, spdef_b=100)
random.seed(0); _hp0 = _ptk2.hp
for _ in range(20):
    _ptk2.hp = _hp0; execute(_ptk2, _dtk2, "てっていこうせん")
    if _ptk2.hp < _hp0: break
check("てっていこうせん 反動: てっていこうせん", _hp0 - _ptk2.hp >= _ptk2.max_hp//2 - 2, f"recoil={_hp0 - _ptk2.hp}")

# ── Gのちから ──
check("DB: Gのちから 取得可能", dl.get_move("Gのちから") is not None)
_mv_Gのちから = dl.get_move("Gのちから")
if _mv_Gのちから:
    _pa_Gのちから = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_Gのちから = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_Gのちから = dmg(_pa_Gのちから, _pd_Gのちから, "Gのちから")
    check("ダメージ計算: Gのちから", _d_Gのちから > 0, f"dmg={_d_Gのちから}")
# Gのちから: 相手防御-1
_mv_dd_Gのちから = dl.get_move("Gのちから")
if _mv_dd_Gのちから:
    _pa_dd = make_poke(type1="くさ", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_Gのちから = 0; _dd_ok_Gのちから = False
    for _ in range(60):
        _pd_dd = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "Gのちから")
        if _pd_dd.stage_defense != 0: _dd_val_Gのちから = _pd_dd.stage_defense; _dd_ok_Gのちから = True; break
    check("相手防御-1: Gのちから", _dd_ok_Gのちから and _dd_val_Gのちから == -1, f"1回適用={_dd_val_Gのちから} 期待=-1")
# Gのちから: じゅうりょく状態で威力1.5倍
_pgc = make_poke(spatk_b=100); _dgc = make_poke(spdef_b=100)
_gn = _ep(_pgc, _dgc, dl.get_move("Gのちから"), BattleField()); _fgv = BattleField(); _fgv.gravity = 1; _gg = _ep(_pgc, _dgc, dl.get_move("Gのちから"), _fgv)
check("じゅうりょく1.5倍: Gのちから", _gg > _gn, f"n={_gn} g={_gg}")
check("通常威力80: Gのちから", _gn == 80, f"n={_gn}")
check("じゅうりょく時1.5倍具体値(120): Gのちから", _gg == 120, f"g={_gg}")

# ── ワイドフォース ──
check("DB: ワイドフォース 取得可能", dl.get_move("ワイドフォース") is not None)
_mv_ワイドフォ_ス = dl.get_move("ワイドフォース")
if _mv_ワイドフォ_ス:
    _pa_ワイドフォ_ス = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_ワイドフォ_ス = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_ワイドフォ_ス = dmg(_pa_ワイドフォ_ス, _pd_ワイドフォ_ス, "ワイドフォース")
    check("ダメージ計算: ワイドフォース", _d_ワイドフォ_ス > 0, f"dmg={_d_ワイドフォ_ス}")
# ワイドフォース: サイコフィールドで威力上昇
_pw = make_poke(type1="エスパー", spatk_b=100); _dw = make_poke(type1="ノーマル", spdef_b=100, hp_b=255)
_wn0 = calc_damage(_pw, _dw, dl.get_move("ワイドフォース"), BattleField(), random_roll=1.0)
_fpt = BattleField(); _fpt.psychic_terrain = True; _wp = calc_damage(_pw, _dw, dl.get_move("ワイドフォース"), _fpt, random_roll=1.0)
check("サイコフィールド威力上昇: ワイドフォース", _wp > _wn0, f"n={_wn0} p={_wp}")

# ── スケイルショット ──
check("DB: スケイルショット 取得可能", dl.get_move("スケイルショット") is not None)
_mv_スケイルショット = dl.get_move("スケイルショット")
if _mv_スケイルショット:
    _pa_スケイルショット = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_スケイルショット = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_スケイルショット = dmg(_pa_スケイルショット, _pd_スケイルショット, "スケイルショット")
    check("ダメージ計算: スケイルショット", _d_スケイルショット > 0, f"dmg={_d_スケイルショット}")
# スケイルショット: 自分防御-1
_mvss_スケイルショット_defense = dl.get_move("スケイルショット")
if _mvss_スケイルショット_defense:
    random.seed(0); _got_スケイルショット_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="ドラゴン", atk_b=60, spatk_b=60); _pds = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "スケイルショット")
        if _pas.stage_defense != 0: _got_スケイルショット_defense = _pas.stage_defense; break
    check("自分防御-1: スケイルショット", _got_スケイルショット_defense == -1, f"1回適用={_got_スケイルショット_defense} 期待=-1")
# スケイルショット: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_スケイルショット = dl.get_move("スケイルショット")
if _mvmh_スケイルショット:
    _pam = make_poke(type1="ドラゴン", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_スケイルショット = calc_damage(_pam, make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200), _mvmh_スケイルショット, BattleField(), random_roll=1.0)
    random.seed(0); _multi_スケイルショット = 0
    for _ in range(20):
        _pdm = make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "スケイルショット"); _multi_スケイルショット = _pdm.max_hp - _pdm.hp
        if _multi_スケイルショット > _single_スケイルショット: break
    check("多段ヒット発生(複数回): スケイルショット", _multi_スケイルショット > _single_スケイルショット, f"single={_single_スケイルショット} multi={_multi_スケイルショット}")
# スケイルショット: 1発あたり威力25（2-5回連続。多段/自己能力変化は別途検証）
_pss2 = make_poke(type1="ドラゴン", atk_b=100); _dss2 = make_poke(type1="ドラゴン", def_b=100)
check("1発威力25: スケイルショット", _ep(_pss2, _dss2, dl.get_move("スケイルショット"), BattleField()) == 25, f"pw={_ep(_pss2, _dss2, dl.get_move('スケイルショット'), BattleField())}")

# ── シェルアームズ ──
check("DB: シェルアームズ 取得可能", dl.get_move("シェルアームズ") is not None)
_mv_シェルア_ムズ = dl.get_move("シェルアームズ")
if _mv_シェルア_ムズ:
    _pa_シェルア_ムズ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_シェルア_ムズ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_シェルア_ムズ = dmg(_pa_シェルア_ムズ, _pd_シェルア_ムズ, "シェルアームズ")
    check("ダメージ計算: シェルアームズ", _d_シェルア_ムズ > 0, f"dmg={_d_シェルア_ムズ}")
# シェルアームズ: どく20%
_mv_s_シェルア_ムズ = dl.get_move("シェルアームズ")
if _mv_s_シェルア_ムズ:
    random.seed(0); _hit_シェルア_ムズ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "シェルアームズ")
        _hit_シェルア_ムズ += int((_pd2.status == "poison"))
    check("追加効果(どく20%): シェルアームズ", 18 <= _hit_シェルア_ムズ <= 117, f"count={_hit_シェルア_ムズ}/300")
    random.seed(1); _immok_シェルア_ムズ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "シェルアームズ")
        if _pdi.status == "poison": _immok_シェルア_ムズ = False; break
    check("どく免疫(どく型には無効): シェルアームズ", _immok_シェルア_ムズ, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_シェルア_ムズ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "シェルアームズ")
        if _pdi.status == "poison": _immok_シェルア_ムズ = False; break
    check("どく免疫(はがね型には無効): シェルアームズ", _immok_シェルア_ムズ, "免疫タイプに状態異常が付与されないこと")
# シェルアームズ: 物理/特殊のうち相手の低い防御を突く
_psh = make_poke(atk_b=150, spatk_b=150); _dlowdef = make_poke(def_b=1, spdef_b=255, hp_b=255); _dhigh = make_poke(def_b=255, spdef_b=255, hp_b=255)
_dmg_low = calc_damage(_psh, _dlowdef, dl.get_move("シェルアームズ"), BattleField(), random_roll=1.0); _dmg_high = calc_damage(_psh, _dhigh, dl.get_move("シェルアームズ"), BattleField(), random_roll=1.0)
check("物理特殊の有利側選択: シェルアームズ", _dmg_low > _dmg_high, f"lowdef={_dmg_low} high={_dmg_high}")

# ── ミストバースト ──
check("DB: ミストバースト 取得可能", dl.get_move("ミストバースト") is not None)
_mv_ミストバ_スト = dl.get_move("ミストバースト")
if _mv_ミストバ_スト:
    _pa_ミストバ_スト = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_ミストバ_スト = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ミストバ_スト = dmg(_pa_ミストバ_スト, _pd_ミストバ_スト, "ミストバースト")
    check("ダメージ計算: ミストバースト", _d_ミストバ_スト > 0, f"dmg={_d_ミストバ_スト}")
# ミストバースト: 自己ひんし
_mvsf_ミストバ_スト = dl.get_move("ミストバースト")
if _mvsf_ミストバ_スト:
    _pasf = make_poke(type1="フェアリー", atk_b=100, spatk_b=100); _pdsf = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
    execute(_pasf, _pdsf, "ミストバースト")
    check("自己ひんし: ミストバースト", not _pasf.is_alive)
# ミストバースト: ミストフィールドで威力上昇
_pmb = make_poke(type1="フェアリー", spatk_b=100); _dmb = make_poke(type1="ノーマル", spdef_b=100, hp_b=255)
_mbn = calc_damage(_pmb, _dmb, dl.get_move("ミストバースト"), BattleField(), random_roll=1.0)
_fmf = BattleField(); _fmf.misty_terrain = True; _mbp = calc_damage(_pmb, _dmb, dl.get_move("ミストバースト"), _fmf, random_roll=1.0)
check("ミストフィールド威力上昇: ミストバースト", _mbp > _mbn, f"n={_mbn} p={_mbp}")
# 威力1.5倍の具体値（100→150）
_mbx = make_poke(type1="フェアリー", spatk_b=100); _dbx = make_poke(type1="ノーマル", spdef_b=100)
_mb_norm = _ep(_mbx, _dbx, dl.get_move("ミストバースト"), BattleField())
_fmx = BattleField(); _fmx.misty_terrain = True; _mb_misty = _ep(_mbx, _dbx, dl.get_move("ミストバースト"), _fmx)
check("通常威力100: ミストバースト", _mb_norm == 100, f"norm={_mb_norm}")
check("ミスト時1.5倍(150): ミストバースト", _mb_misty == 150, f"misty={_mb_misty}")

# ── しっとのほのお ──
check("DB: しっとのほのお 取得可能", dl.get_move("しっとのほのお") is not None)
_mv_しっとのほのお = dl.get_move("しっとのほのお")
if _mv_しっとのほのお:
    _pa_しっとのほのお = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_しっとのほのお = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_しっとのほのお = dmg(_pa_しっとのほのお, _pd_しっとのほのお, "しっとのほのお")
    check("ダメージ計算: しっとのほのお", _d_しっとのほのお > 0, f"dmg={_d_しっとのほのお}")
# しっとのほのお: 相手の能力上昇時のみ状態異常
_psj = make_poke(type1="ほのお", spatk_b=100, atk_b=100)
random.seed(0); _sj_ok = False
for _ in range(20):
    _dsj = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200); _dsj.stage_attack = 2
    execute(_psj, _dsj, "しっとのほのお")
    if _dsj.status == "burn": _sj_ok = True; break
check("能力上昇時の状態異常: しっとのほのお", _sj_ok)
# negative: 相手の能力が上がっていなければ付与されない
random.seed(1); _sj_neg = True
for _ in range(40):
    _dsn = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200)
    execute(_psj, _dsn, "しっとのほのお")
    if _dsn.status == "burn": _sj_neg = False; break
check("能力非上昇時は付与なし: しっとのほのお", _sj_neg, "能力上昇がなければ状態異常は付かない")

# ── ライジングボルト ──
check("DB: ライジングボルト 取得可能", dl.get_move("ライジングボルト") is not None)
_mv_ライジングボルト = dl.get_move("ライジングボルト")
if _mv_ライジングボルト:
    _pa_ライジングボルト = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_ライジングボルト = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ライジングボルト = dmg(_pa_ライジングボルト, _pd_ライジングボルト, "ライジングボルト")
    check("ダメージ計算: ライジングボルト", _d_ライジングボルト > 0, f"dmg={_d_ライジングボルト}")
# ライジングボルト: エレキフィールドで威力2倍
_prb = make_poke(type1="でんき", spatk_b=100); _drb = make_poke(type1="ノーマル", spdef_b=100)
_prn = _ep(_prb, _drb, dl.get_move("ライジングボルト"), BattleField())
_fe = BattleField(); _fe.electric_terrain = True
_prd = _ep(_prb, _drb, dl.get_move("ライジングボルト"), _fe)
check("エレキF威力2倍: ライジングボルト", _prd == _prn * 2, f"normal={_prn} ef={_prd}")

# ── コーチング ──
check("DB: コーチング 取得可能", dl.get_move("コーチング") is not None)
# コーチング: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: コーチング", "コーチング", "かくとう", False, smoke=("コーチング" in DOUBLE_ONLY_SMOKE))

# ── ポルターガイスト ──
check("DB: ポルターガイスト 取得可能", dl.get_move("ポルターガイスト") is not None)
_mv_ポルタ_ガイスト = dl.get_move("ポルターガイスト")
if _mv_ポルタ_ガイスト:
    _pa_ポルタ_ガイスト = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_ポルタ_ガイスト = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ポルタ_ガイスト = dmg(_pa_ポルタ_ガイスト, _pd_ポルタ_ガイスト, "ポルターガイスト")
    check("ダメージ計算: ポルターガイスト", _d_ポルタ_ガイスト > 0, f"dmg={_d_ポルタ_ガイスト}")
# ポルターガイスト: 相手が道具を持っていないと失敗
_ppg = make_poke(type1="ゴースト", atk_b=100); _dpg = make_poke(type1="エスパー", hp_b=255, def_b=120, item=None); _hppg = _dpg.hp
execute(_ppg, _dpg, "ポルターガイスト")
check("ポルターガイスト道具なし失敗: ポルターガイスト", _dpg.hp == _hppg, f"hp={_dpg.hp}/{_hppg}")
# 相手が道具を持っていれば成功（ダメージが通る）
_ppg2 = make_poke(type1="ゴースト", atk_b=120); _dpg2 = make_poke(type1="エスパー", hp_b=255, def_b=120); _dpg2.item = "オボンのみ"; _hppg2 = _dpg2.hp
execute(_ppg2, _dpg2, "ポルターガイスト")
check("道具あり成功: ポルターガイスト", _dpg2.hp < _hppg2, f"hp={_dpg2.hp}/{_hppg2}")

# ── はいよるいちげき ──
check("DB: はいよるいちげき 取得可能", dl.get_move("はいよるいちげき") is not None)
_mv_はいよるいちげき = dl.get_move("はいよるいちげき")
if _mv_はいよるいちげき:
    _pa_はいよるいちげき = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_はいよるいちげき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_はいよるいちげき = dmg(_pa_はいよるいちげき, _pd_はいよるいちげき, "はいよるいちげき")
    check("ダメージ計算: はいよるいちげき", _d_はいよるいちげき > 0, f"dmg={_d_はいよるいちげき}")
# はいよるいちげき: 相手特攻-1
_mv_dd_はいよるいちげき = dl.get_move("はいよるいちげき")
if _mv_dd_はいよるいちげき:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_はいよるいちげき = 0; _dd_ok_はいよるいちげき = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "はいよるいちげき")
        if _pd_dd.stage_sp_attack != 0: _dd_val_はいよるいちげき = _pd_dd.stage_sp_attack; _dd_ok_はいよるいちげき = True; break
    check("相手特攻-1: はいよるいちげき", _dd_ok_はいよるいちげき and _dd_val_はいよるいちげき == -1, f"1回適用={_dd_val_はいよるいちげき} 期待=-1")

# ── トリプルアクセル ──
check("DB: トリプルアクセル 取得可能", dl.get_move("トリプルアクセル") is not None)
_mv_トリプルアクセル = dl.get_move("トリプルアクセル")
if _mv_トリプルアクセル:
    _pa_トリプルアクセル = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_トリプルアクセル = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_トリプルアクセル = dmg(_pa_トリプルアクセル, _pd_トリプルアクセル, "トリプルアクセル")
    check("ダメージ計算: トリプルアクセル", _d_トリプルアクセル > 0, f"dmg={_d_トリプルアクセル}")
# トリプルアクセル: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_トリプルアクセル = dl.get_move("トリプルアクセル")
if _mvmh_トリプルアクセル:
    _pam = make_poke(type1="こおり", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_トリプルアクセル = calc_damage(_pam, make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200), _mvmh_トリプルアクセル, BattleField(), random_roll=1.0)
    random.seed(0); _multi_トリプルアクセル = 0
    for _ in range(20):
        _pdm = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "トリプルアクセル"); _multi_トリプルアクセル = _pdm.max_hp - _pdm.hp
        if _multi_トリプルアクセル > _single_トリプルアクセル: break
    check("多段ヒット発生(複数回): トリプルアクセル", _multi_トリプルアクセル > _single_トリプルアクセル, f"single={_single_トリプルアクセル} multi={_multi_トリプルアクセル}")
# トリプルアクセル: 1回目20/2回目40/3回目60と威力漸増
_pta = make_poke(type1="こおり", atk_b=100); _dta = make_poke(type1="ノーマル", def_b=100)
_pta._multi_hit_index = 0; _ta0 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())
_pta._multi_hit_index = 1; _ta1 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())
_pta._multi_hit_index = 2; _ta2 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())
check("威力漸増: トリプルアクセル", (_ta0, _ta1, _ta2) == (20, 40, 60), f"powers={_ta0},{_ta1},{_ta2}")

# ── クイックターン ──
check("DB: クイックターン 取得可能", dl.get_move("クイックターン") is not None)
_mv_クイックタ_ン = dl.get_move("クイックターン")
if _mv_クイックタ_ン:
    _pa_クイックタ_ン = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_クイックタ_ン = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_クイックタ_ン = dmg(_pa_クイックタ_ン, _pd_クイックタ_ン, "クイックターン")
    check("ダメージ計算: クイックターン", _d_クイックタ_ン > 0, f"dmg={_d_クイックタ_ン}")
# クイックターン: ピボット交代フラグ
_mvpv_クイックタ_ン = dl.get_move("クイックターン")
if _mvpv_クイックタ_ン:
    _pap = make_poke(type1="みず", atk_b=100, spatk_b=100); _pdp = make_poke(type1="ほのお", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_クイックタ_ン), BattleField())
    check("ピボット交代フラグ: クイックターン", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")

# ── ダブルウイング ──
check("DB: ダブルウイング 取得可能", dl.get_move("ダブルウイング") is not None)
_mv_ダブルウイング = dl.get_move("ダブルウイング")
if _mv_ダブルウイング:
    _pa_ダブルウイング = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ダブルウイング = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ダブルウイング = dmg(_pa_ダブルウイング, _pd_ダブルウイング, "ダブルウイング")
    check("ダメージ計算: ダブルウイング", _d_ダブルウイング > 0, f"dmg={_d_ダブルウイング}")
# ダブルウイング: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ダブルウイング = dl.get_move("ダブルウイング")
if _mvmh_ダブルウイング:
    _pam = make_poke(type1="ひこう", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ダブルウイング = calc_damage(_pam, make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200), _mvmh_ダブルウイング, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ダブルウイング = 0
    for _ in range(20):
        _pdm = make_poke(type1="くさ", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ダブルウイング"); _multi_ダブルウイング = _pdm.max_hp - _pdm.hp
        if _multi_ダブルウイング > _single_ダブルウイング: break
    check("多段ヒット発生(複数回): ダブルウイング", _multi_ダブルウイング > _single_ダブルウイング, f"single={_single_ダブルウイング} multi={_multi_ダブルウイング}")

# ── ねっさのだいち ──
check("DB: ねっさのだいち 取得可能", dl.get_move("ねっさのだいち") is not None)
_mv_ねっさのだいち = dl.get_move("ねっさのだいち")
if _mv_ねっさのだいち:
    _pa_ねっさのだいち = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_ねっさのだいち = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_ねっさのだいち = dmg(_pa_ねっさのだいち, _pd_ねっさのだいち, "ねっさのだいち")
    check("ダメージ計算: ねっさのだいち", _d_ねっさのだいち > 0, f"dmg={_d_ねっさのだいち}")
# ねっさのだいち: やけど30%
_mv_s_ねっさのだいち = dl.get_move("ねっさのだいち")
if _mv_s_ねっさのだいち:
    random.seed(0); _hit_ねっさのだいち = 0
    for _ in range(300):
        _pa2 = make_poke(type1="じめん", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ねっさのだいち")
        _hit_ねっさのだいち += int((_pd2.status == "burn"))
    check("追加効果(やけど30%): ねっさのだいち", 27 <= _hit_ねっさのだいち <= 168, f"count={_hit_ねっさのだいち}/300")
    random.seed(1); _immok_ねっさのだいち = True
    for _ in range(60):
        _pai = make_poke(type1="じめん", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ねっさのだいち")
        if _pdi.status == "burn": _immok_ねっさのだいち = False; break
    check("やけど免疫(ほのお型には無効): ねっさのだいち", _immok_ねっさのだいち, "免疫タイプに状態異常が付与されないこと")
# ねっさのだいち: 相手のこおりを治す
_paf2 = make_poke(type1="じめん", spatk_b=100, atk_b=100); _pdf2 = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
_pdf2.status = "freeze"; execute(_paf2, _pdf2, "ねっさのだいち")
check("相手こおり治癒: ねっさのだいち", _pdf2.status != "freeze")
# 自分のこおりも治す
_paf3 = make_poke(type1="じめん", spatk_b=100, atk_b=100); _paf3.status = "freeze"
execute(_paf3, make_poke(hp_b=255), "ねっさのだいち")
check("自分こおり治癒: ねっさのだいち", _paf3.status != "freeze")

# ── フェイタルクロー ──
check("DB: フェイタルクロー 取得可能", dl.get_move("フェイタルクロー") is not None)
_mv_フェイタルクロ_ = dl.get_move("フェイタルクロー")
if _mv_フェイタルクロ_:
    _pa_フェイタルクロ_ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_フェイタルクロ_ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_フェイタルクロ_ = dmg(_pa_フェイタルクロ_, _pd_フェイタルクロ_, "フェイタルクロー")
    check("ダメージ計算: フェイタルクロー", _d_フェイタルクロ_ > 0, f"dmg={_d_フェイタルクロ_}")
# フェイタルクロー: どく30%
_mv_s_フェイタルクロ_ = dl.get_move("フェイタルクロー")
if _mv_s_フェイタルクロ_:
    random.seed(0); _hit_フェイタルクロ_ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "フェイタルクロー")
        _hit_フェイタルクロ_ += int((_pd2.status == "poison"))
    check("追加効果(どく30%): フェイタルクロー", 27 <= _hit_フェイタルクロ_ <= 168, f"count={_hit_フェイタルクロ_}/300")
    random.seed(1); _immok_フェイタルクロ_ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "フェイタルクロー")
        if _pdi.status == "poison": _immok_フェイタルクロ_ = False; break
    check("どく免疫(どく型には無効): フェイタルクロー", _immok_フェイタルクロ_, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_フェイタルクロ_ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "フェイタルクロー")
        if _pdi.status == "poison": _immok_フェイタルクロ_ = False; break
    check("どく免疫(はがね型には無効): フェイタルクロー", _immok_フェイタルクロ_, "免疫タイプに状態異常が付与されないこと")
# フェイタルクロー: どく・まひ・ねむりの「いずれか」→3状態すべてが実際に発生する
_pfc_m = make_poke(type1="どく", atk_b=30)
random.seed(0); _fc_cnt = {"poison":0, "paralysis":0, "sleep":0}
for _ in range(600):
    _dfc = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
    execute(_pfc_m, _dfc, "フェイタルクロー")
    if _dfc.status in _fc_cnt: _fc_cnt[_dfc.status] += 1
check("いずれか3状態すべて発生: フェイタルクロー", all(_v > 0 for _v in _fc_cnt.values()), f"counts={_fc_cnt}")

# ── バリアーラッシュ ──
check("DB: バリアーラッシュ 取得可能", dl.get_move("バリアーラッシュ") is not None)
_mv_バリア_ラッシュ = dl.get_move("バリアーラッシュ")
if _mv_バリア_ラッシュ:
    _pa_バリア_ラッシュ = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_バリア_ラッシュ = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_バリア_ラッシュ = dmg(_pa_バリア_ラッシュ, _pd_バリア_ラッシュ, "バリアーラッシュ")
    check("ダメージ計算: バリアーラッシュ", _d_バリア_ラッシュ > 0, f"dmg={_d_バリア_ラッシュ}")
# バリアーラッシュ: 自分防御+1
_mvss_バリア_ラッシュ_defense = dl.get_move("バリアーラッシュ")
if _mvss_バリア_ラッシュ_defense:
    random.seed(0); _got_バリア_ラッシュ_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="エスパー", atk_b=60, spatk_b=60); _pds = make_poke(type1="かくとう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "バリアーラッシュ")
        if _pas.stage_defense != 0: _got_バリア_ラッシュ_defense = _pas.stage_defense; break
    check("自分防御+1: バリアーラッシュ", _got_バリア_ラッシュ_defense == 1, f"1回適用={_got_バリア_ラッシュ_defense} 期待=1")

# ── がんせきアックス ──
check("DB: がんせきアックス 取得可能", dl.get_move("がんせきアックス") is not None)
_mv_がんせきアックス = dl.get_move("がんせきアックス")
if _mv_がんせきアックス:
    _pa_がんせきアックス = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_がんせきアックス = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_がんせきアックス = dmg(_pa_がんせきアックス, _pd_がんせきアックス, "がんせきアックス")
    check("ダメージ計算: がんせきアックス", _d_がんせきアックス > 0, f"dmg={_d_がんせきアックス}")
# がんせきアックス: ハザード設置(ダメージ技)stealth_rock
_mvhd_がんせきアックス = dl.get_move("がんせきアックス")
if _mvhd_がんせきアックス:
    random.seed(0); _hdval = False
    for _ in range(20):
        _pahd = make_poke(type1="いわ", atk_b=120, spatk_b=120); _pdhd = make_poke(type1="ひこう", hp_b=255, def_b=100, spdef_b=100)
        _s1hd = BattleSide([_pahd]); _s2hd = BattleSide([_pdhd]); _fhd = BattleField()
        _execute_move(_s1hd, _s2hd, Action(type="move", move=_mvhd_がんせきアックス), _fhd)
        _hdval = _fhd.stealth_rock[_s2hd.field_idx] or getattr(_s2hd,"_stealth_rock_pending",False) or _s2hd.stealth_rock_set
        if _hdval: break
    check("ハザード設置stealth_rock: がんせきアックス", bool(_hdval), f"val={_hdval}")

# ── ウェーブタックル ──
check("DB: ウェーブタックル 取得可能", dl.get_move("ウェーブタックル") is not None)
_mv_ウェ_ブタックル = dl.get_move("ウェーブタックル")
if _mv_ウェ_ブタックル:
    _pa_ウェ_ブタックル = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ウェ_ブタックル = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ウェ_ブタックル = dmg(_pa_ウェ_ブタックル, _pd_ウェ_ブタックル, "ウェーブタックル")
    check("ダメージ計算: ウェーブタックル", _d_ウェ_ブタックル > 0, f"dmg={_d_ウェ_ブタックル}")
# ウェーブタックル: 反動（与ダメの1/3）
_mvrc_ウェ_ブタックル = dl.get_move("ウェーブタックル")
if _mvrc_ウェ_ブタックル:
    random.seed(0)
    for _ in range(20):
        _par = make_poke(type1="みず", atk_b=120, spatk_b=120); _par.hp = _par.max_hp
        _pdr = make_poke(type1="ほのお", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp
        execute(_par, _pdr, "ウェーブタックル")
        _rc_dealt_ウェ_ブタックル = _hpdr - _pdr.hp; _rc_rcv_ウェ_ブタックル = _par.max_hp - _par.hp
        if _rc_dealt_ウェ_ブタックル > 0: break
    _rc_exp_ウェ_ブタックル = max(1, _rc_dealt_ウェ_ブタックル // 3)
    check("反動ダメージ(1/3): ウェーブタックル", abs(_rc_rcv_ウェ_ブタックル - _rc_exp_ウェ_ブタックル) <= 2, f"dealt={_rc_dealt_ウェ_ブタックル} recoil={_rc_rcv_ウェ_ブタックル} 期待={_rc_exp_ウェ_ブタックル}")

# ── ひょうざんおろし ──
check("DB: ひょうざんおろし 取得可能", dl.get_move("ひょうざんおろし") is not None)
_mv_ひょうざんおろし = dl.get_move("ひょうざんおろし")
if _mv_ひょうざんおろし:
    _pa_ひょうざんおろし = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_ひょうざんおろし = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ひょうざんおろし = dmg(_pa_ひょうざんおろし, _pd_ひょうざんおろし, "ひょうざんおろし")
    check("ダメージ計算: ひょうざんおろし", _d_ひょうざんおろし > 0, f"dmg={_d_ひょうざんおろし}")
# ひょうざんおろし: ひるみ30%
_mv_f_ひょうざんおろし = dl.get_move("ひょうざんおろし")
if _mv_f_ひょうざんおろし:
    random.seed(1); _fh_ひょうざんおろし = 0
    for _ in range(300):
        _pa3 = make_poke(type1="こおり", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "ひょうざんおろし"); _fh_ひょうざんおろし += int(_pd3.flinched)
    check("ひるみ(30%): ひょうざんおろし", 27 <= _fh_ひょうざんおろし <= 168, f"count={_fh_ひょうざんおろし}/300")

# ── ぶちかまし ──
check("DB: ぶちかまし 取得可能", dl.get_move("ぶちかまし") is not None)
_mv_ぶちかまし = dl.get_move("ぶちかまし")
if _mv_ぶちかまし:
    _pa_ぶちかまし = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_ぶちかまし = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_ぶちかまし = dmg(_pa_ぶちかまし, _pd_ぶちかまし, "ぶちかまし")
    check("ダメージ計算: ぶちかまし", _d_ぶちかまし > 0, f"dmg={_d_ぶちかまし}")
# ぶちかまし: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="じめん", atk_b=120, spatk_b=120); _dsd = make_poke(type1="でんき", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "ぶちかまし")
    if _psd.stage_defense < 0: break
check("自分防御下降: ぶちかまし", _psd.stage_defense < 0, f"stage={_psd.stage_defense}")
check("自分特防下降: ぶちかまし", _psd.stage_sp_defense < 0, f"stage={_psd.stage_sp_defense}")

# ── たてこもる ──
check("DB: たてこもる 取得可能", dl.get_move("たてこもる") is not None)
# たてこもる: 自分防御+2
_mv_sb_たてこもる_defense = dl.get_move("たてこもる")
if _mv_sb_たてこもる_defense:
    _pa_sb = make_poke(type1="はがね"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "たてこもる")
    check("自分防御+2: たてこもる", _pa_sb.stage_defense == 2, f"1回適用={_pa_sb.stage_defense} 期待=+2")
# たてこもる: 自分防御+2
_mvss_たてこもる_defense = dl.get_move("たてこもる")
if _mvss_たてこもる_defense:
    random.seed(0); _got_たてこもる_defense = 0
    for _ in range(60):
        _pas = make_poke(type1="はがね", atk_b=60, spatk_b=60); _pds = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "たてこもる")
        if _pas.stage_defense != 0: _got_たてこもる_defense = _pas.stage_defense; break
    check("自分防御+2: たてこもる", _got_たてこもる_defense == 2, f"1回適用={_got_たてこもる_defense} 期待=2")

# ── うらみつらみ ──
check("DB: うらみつらみ 取得可能", dl.get_move("うらみつらみ") is not None)
_mv_うらみつらみ = dl.get_move("うらみつらみ")
if _mv_うらみつらみ:
    _pa_うらみつらみ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_うらみつらみ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_うらみつらみ = dmg(_pa_うらみつらみ, _pd_うらみつらみ, "うらみつらみ")
    check("ダメージ計算: うらみつらみ", _d_うらみつらみ > 0, f"dmg={_d_うらみつらみ}")

# ── ひゃっきやこう ──
check("DB: ひゃっきやこう 取得可能", dl.get_move("ひゃっきやこう") is not None)
_mv_ひゃっきやこう = dl.get_move("ひゃっきやこう")
if _mv_ひゃっきやこう:
    _pa_ひゃっきやこう = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_ひゃっきやこう = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ひゃっきやこう = dmg(_pa_ひゃっきやこう, _pd_ひゃっきやこう, "ひゃっきやこう")
    check("ダメージ計算: ひゃっきやこう", _d_ひゃっきやこう > 0, f"dmg={_d_ひゃっきやこう}")
# ひゃっきやこう: やけど30%
_mv_s_ひゃっきやこう = dl.get_move("ひゃっきやこう")
if _mv_s_ひゃっきやこう:
    random.seed(0); _hit_ひゃっきやこう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ゴースト", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="エスパー", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "ひゃっきやこう")
        _hit_ひゃっきやこう += int((_pd2.status == "burn"))
    check("追加効果(やけど30%): ひゃっきやこう", 27 <= _hit_ひゃっきやこう <= 168, f"count={_hit_ひゃっきやこう}/300")
    random.seed(1); _immok_ひゃっきやこう = True
    for _ in range(60):
        _pai = make_poke(type1="ゴースト", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "ひゃっきやこう")
        if _pdi.status == "burn": _immok_ひゃっきやこう = False; break
    check("やけど免疫(ほのお型には無効): ひゃっきやこう", _immok_ひゃっきやこう, "免疫タイプに状態異常が付与されないこと")
# ひゃっきやこう: 相手状態異常で威力2倍
_pcp = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
_dn1 = make_poke(type1="エスパー", def_b=100, spdef_b=100)
_dn2 = make_poke(type1="エスパー", def_b=100, spdef_b=100); _dn2.status = "burn"
_pn = _ep(_pcp, _dn1, dl.get_move("ひゃっきやこう"), BattleField())
_pd = _ep(_pcp, _dn2, dl.get_move("ひゃっきやこう"), BattleField())
check("状態異常で威力2倍: ひゃっきやこう", _pd == _pn * 2, f"normal={_pn} status={_pd}")

# ── 3ぼんのや ──
check("DB: 3ぼんのや 取得可能", dl.get_move("3ぼんのや") is not None)
_mv_3ぼんのや = dl.get_move("3ぼんのや")
if _mv_3ぼんのや:
    _pa_3ぼんのや = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_3ぼんのや = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_3ぼんのや = dmg(_pa_3ぼんのや, _pd_3ぼんのや, "3ぼんのや")
    check("ダメージ計算: 3ぼんのや", _d_3ぼんのや > 0, f"dmg={_d_3ぼんのや}")
# 3ぼんのや: ひるみ30%
_mv_f_3ぼんのや = dl.get_move("3ぼんのや")
if _mv_f_3ぼんのや:
    random.seed(1); _fh_3ぼんのや = 0
    for _ in range(300):
        _pa3 = make_poke(type1="かくとう", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "3ぼんのや"); _fh_3ぼんのや += int(_pd3.flinched)
    check("ひるみ(30%): 3ぼんのや", 27 <= _fh_3ぼんのや <= 168, f"count={_fh_3ぼんのや}/300")
# 3ぼんのや: 相手防御-1
_mv_dd_3ぼんのや = dl.get_move("3ぼんのや")
if _mv_dd_3ぼんのや:
    _pa_dd = make_poke(type1="かくとう", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_3ぼんのや = 0; _dd_ok_3ぼんのや = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "3ぼんのや")
        if _pd_dd.stage_defense != 0: _dd_val_3ぼんのや = _pd_dd.stage_defense; _dd_ok_3ぼんのや = True; break
    check("相手防御-1: 3ぼんのや", _dd_ok_3ぼんのや and _dd_val_3ぼんのや == -1, f"1回適用={_dd_val_3ぼんのや} 期待=-1")
# 3ぼんのや: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_3ぼんのや
random.seed(0); _hc_crit_3ぼんのや = 0; _phc = make_poke(type1="かくとう")
_mvhc_3ぼんのや = dl.get_move("3ぼんのや")
for _ in range(800):
    if _cc_3ぼんのや(_phc, _mvhc_3ぼんのや, make_poke(type1="ノーマル")): _hc_crit_3ぼんのや += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: 3ぼんのや", 60 <= _hc_crit_3ぼんのや <= 150, f"crit={_hc_crit_3ぼんのや}/800 (期待≈100, 通常1/24なら≈33)")

# ── ひけん・ちえなみ ──
check("DB: ひけん・ちえなみ 取得可能", dl.get_move("ひけん・ちえなみ") is not None)
_mv_ひけん_ちえなみ = dl.get_move("ひけん・ちえなみ")
if _mv_ひけん_ちえなみ:
    _pa_ひけん_ちえなみ = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ひけん_ちえなみ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ひけん_ちえなみ = dmg(_pa_ひけん_ちえなみ, _pd_ひけん_ちえなみ, "ひけん・ちえなみ")
    check("ダメージ計算: ひけん・ちえなみ", _d_ひけん_ちえなみ > 0, f"dmg={_d_ひけん_ちえなみ}")
# ひけん・ちえなみ: ハザード設置(ダメージ技)spikes
_mvhd_ひけん_ちえなみ = dl.get_move("ひけん・ちえなみ")
if _mvhd_ひけん_ちえなみ:
    random.seed(0); _hdval = False
    for _ in range(20):
        _pahd = make_poke(type1="あく", atk_b=120, spatk_b=120); _pdhd = make_poke(type1="エスパー", hp_b=255, def_b=100, spdef_b=100)
        _s1hd = BattleSide([_pahd]); _s2hd = BattleSide([_pdhd]); _fhd = BattleField()
        _execute_move(_s1hd, _s2hd, Action(type="move", move=_mvhd_ひけん_ちえなみ), _fhd)
        _hdval = _fhd.spikes[_s2hd.field_idx]
        if _hdval: break
    check("ハザード設置spikes: ひけん・ちえなみ", bool(_hdval), f"val={_hdval}")

# ── ルミナコリジョン ──
check("DB: ルミナコリジョン 取得可能", dl.get_move("ルミナコリジョン") is not None)
_mv_ルミナコリジョン = dl.get_move("ルミナコリジョン")
if _mv_ルミナコリジョン:
    _pa_ルミナコリジョン = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_ルミナコリジョン = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_ルミナコリジョン = dmg(_pa_ルミナコリジョン, _pd_ルミナコリジョン, "ルミナコリジョン")
    check("ダメージ計算: ルミナコリジョン", _d_ルミナコリジョン > 0, f"dmg={_d_ルミナコリジョン}")
# ルミナコリジョン: 相手特防-2
_mv_dd_ルミナコリジョン = dl.get_move("ルミナコリジョン")
if _mv_dd_ルミナコリジョン:
    _pa_dd = make_poke(type1="エスパー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ルミナコリジョン = 0; _dd_ok_ルミナコリジョン = False
    for _ in range(60):
        _pd_dd = make_poke(type1="かくとう", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ルミナコリジョン")
        if _pd_dd.stage_sp_defense != 0: _dd_val_ルミナコリジョン = _pd_dd.stage_sp_defense; _dd_ok_ルミナコリジョン = True; break
    check("相手特防-2: ルミナコリジョン", _dd_ok_ルミナコリジョン and _dd_val_ルミナコリジョン == -2, f"1回適用={_dd_val_ルミナコリジョン} 期待=-2")

# ── ジェットパンチ ──
check("DB: ジェットパンチ 取得可能", dl.get_move("ジェットパンチ") is not None)
_mv_ジェットパンチ = dl.get_move("ジェットパンチ")
if _mv_ジェットパンチ:
    _pa_ジェットパンチ = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ジェットパンチ = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ジェットパンチ = dmg(_pa_ジェットパンチ, _pd_ジェットパンチ, "ジェットパンチ")
    check("ダメージ計算: ジェットパンチ", _d_ジェットパンチ > 0, f"dmg={_d_ジェットパンチ}")
# ジェットパンチ: 優先度1
_mv_pr_ジェットパンチ = dl.get_move("ジェットパンチ")
if _mv_pr_ジェットパンチ and _mv_pr_ジェットパンチ.priority == 1:
    check("優先度1: ジェットパンチ", _mv_pr_ジェットパンチ.priority == 1)
elif _mv_pr_ジェットパンチ:
    check("優先度1: ジェットパンチ", _mv_pr_ジェットパンチ.priority == 1, f"DB優先度={_mv_pr_ジェットパンチ.priority} 仕様=1")

# ── おはかまいり ──
check("DB: おはかまいり 取得可能", dl.get_move("おはかまいり") is not None)
_mv_おはかまいり = dl.get_move("おはかまいり")
if _mv_おはかまいり:
    _pa_おはかまいり = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_おはかまいり = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_おはかまいり = dmg(_pa_おはかまいり, _pd_おはかまいり, "おはかまいり")
    check("ダメージ計算: おはかまいり", _d_おはかまいり > 0, f"dmg={_d_おはかまいり}")
# おはかまいり: ひんしの味方が多いほど威力が高い
_po = make_poke(atk_b=100); _do = make_poke(def_b=100)
_o0 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField()); _po.fainted_allies = 3; _o3 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField())
_po.fainted_allies = 5; _o5 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField())
check("ひんし0で威力50: おはかまいり", _o0 == 50, f"0={_o0}")
check("ひんし3で威力200(50+50×3): おはかまいり", _o3 == 200, f"3={_o3}")
check("ひんし上限5で威力300: おはかまいり", _o5 == 300, f"5={_o5}")

# ── アイススピナー ──
check("DB: アイススピナー 取得可能", dl.get_move("アイススピナー") is not None)
_mv_アイススピナ_ = dl.get_move("アイススピナー")
if _mv_アイススピナ_:
    _pa_アイススピナ_ = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_アイススピナ_ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_アイススピナ_ = dmg(_pa_アイススピナ_, _pd_アイススピナ_, "アイススピナー")
    check("ダメージ計算: アイススピナー", _d_アイススピナ_ > 0, f"dmg={_d_アイススピナ_}")
# アイススピナー: フィールド解除
_pfc = make_poke(type1="こおり" if "アイススピナー"=="アイススピナー" else "はがね", atk_b=120)
_dfc = make_poke(type1="ノーマル", hp_b=255, def_b=100)
_s1fc = BattleSide([_pfc]); _s2fc = BattleSide([_dfc]); _ffc = BattleField()
_ffc.electric_terrain = True; _ffc.electric_terrain_count = 5
_execute_move(_s1fc, _s2fc, Action(type="move", move=dl.get_move("アイススピナー")), _ffc)
check("フィールド解除: アイススピナー", not _ffc.electric_terrain)

# ── ネズミざん ──
check("DB: ネズミざん 取得可能", dl.get_move("ネズミざん") is not None)
_mv_ネズミざん = dl.get_move("ネズミざん")
if _mv_ネズミざん:
    _pa_ネズミざん = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ネズミざん = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ネズミざん = dmg(_pa_ネズミざん, _pd_ネズミざん, "ネズミざん")
    check("ダメージ計算: ネズミざん", _d_ネズミざん > 0, f"dmg={_d_ネズミざん}")
# ネズミざん: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ネズミざん = dl.get_move("ネズミざん")
if _mvmh_ネズミざん:
    _pam = make_poke(type1="ノーマル", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ネズミざん = calc_damage(_pam, make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200), _mvmh_ネズミざん, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ネズミざん = 0
    for _ in range(20):
        _pdm = make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ネズミざん"); _multi_ネズミざん = _pdm.max_hp - _pdm.hp
        if _multi_ネズミざん > _single_ネズミざん: break
    check("多段ヒット発生(複数回): ネズミざん", _multi_ネズミざん > _single_ネズミざん, f"single={_single_ネズミざん} multi={_multi_ネズミざん}")

# ── キラースピン ──
check("DB: キラースピン 取得可能", dl.get_move("キラースピン") is not None)
_mv_キラ_スピン = dl.get_move("キラースピン")
if _mv_キラ_スピン:
    _pa_キラ_スピン = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_キラ_スピン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_キラ_スピン = dmg(_pa_キラ_スピン, _pd_キラ_スピン, "キラースピン")
    check("ダメージ計算: キラースピン", _d_キラ_スピン > 0, f"dmg={_d_キラ_スピン}")
# キラースピン: どく100%
_mv_s_キラ_スピン = dl.get_move("キラースピン")
if _mv_s_キラ_スピン:
    random.seed(0); _hit_キラ_スピン = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "キラースピン")
        _hit_キラ_スピン += int((_pd2.status == "poison"))
    check("追加効果(どく100%): キラースピン", 90 <= _hit_キラ_スピン <= 525, f"count={_hit_キラ_スピン}/300")
    random.seed(1); _immok_キラ_スピン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "キラースピン")
        if _pdi.status == "poison": _immok_キラ_スピン = False; break
    check("どく免疫(どく型には無効): キラースピン", _immok_キラ_スピン, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_キラ_スピン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "キラースピン")
        if _pdi.status == "poison": _immok_キラ_スピン = False; break
    check("どく免疫(はがね型には無効): キラースピン", _immok_キラ_スピン, "免疫タイプに状態異常が付与されないこと")
# キラースピン: 自分のやどりぎ/バインドを解除
_pks = make_poke(type1="ノーマル", atk_b=120); _pks.seeded = True; _dks = make_poke(type1="ノーマル", hp_b=255, def_b=120)
execute(_pks, _dks, "キラースピン")
check("バインド解除: キラースピン", not _pks.seeded, f"seeded={_pks.seeded}")

# ── しおづけ ──
check("DB: しおづけ 取得可能", dl.get_move("しおづけ") is not None)
_mv_しおづけ = dl.get_move("しおづけ")
if _mv_しおづけ:
    _pa_しおづけ = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_しおづけ = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _d_しおづけ = dmg(_pa_しおづけ, _pd_しおづけ, "しおづけ")
    check("ダメージ計算: しおづけ", _d_しおづけ > 0, f"dmg={_d_しおづけ}")
# しおづけ: 相手をしおづけ状態にする
_psl = make_poke(atk_b=100); _dsl = make_poke(hp_b=255, def_b=120); execute(_psl, _dsl, "しおづけ")
check("しおづけ付与: しおづけ", getattr(_dsl, "_salted", False))

# ── アクアステップ ──
check("DB: アクアステップ 取得可能", dl.get_move("アクアステップ") is not None)
_mv_アクアステップ = dl.get_move("アクアステップ")
if _mv_アクアステップ:
    _pa_アクアステップ = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_アクアステップ = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_アクアステップ = dmg(_pa_アクアステップ, _pd_アクアステップ, "アクアステップ")
    check("ダメージ計算: アクアステップ", _d_アクアステップ > 0, f"dmg={_d_アクアステップ}")
# アクアステップ: 自分素早さ+1
_mvss_アクアステップ_speed = dl.get_move("アクアステップ")
if _mvss_アクアステップ_speed:
    random.seed(0); _got_アクアステップ_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="みず", atk_b=60, spatk_b=60); _pds = make_poke(type1="ほのお", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "アクアステップ")
        if _pas.stage_speed != 0: _got_アクアステップ_speed = _pas.stage_speed; break
    check("自分素早さ+1: アクアステップ", _got_アクアステップ_speed == 1, f"1回適用={_got_アクアステップ_speed} 期待=1")

# ── フレアソング ──
check("DB: フレアソング 取得可能", dl.get_move("フレアソング") is not None)
_mv_フレアソング = dl.get_move("フレアソング")
if _mv_フレアソング:
    _pa_フレアソング = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_フレアソング = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_フレアソング = dmg(_pa_フレアソング, _pd_フレアソング, "フレアソング")
    check("ダメージ計算: フレアソング", _d_フレアソング > 0, f"dmg={_d_フレアソング}")
# フレアソング: 自分特攻+1
_mvss_フレアソング_sp_attack = dl.get_move("フレアソング")
if _mvss_フレアソング_sp_attack:
    random.seed(0); _got_フレアソング_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="ほのお", atk_b=60, spatk_b=60); _pds = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "フレアソング")
        if _pas.stage_sp_attack != 0: _got_フレアソング_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻+1: フレアソング", _got_フレアソング_sp_attack == 1, f"1回適用={_got_フレアソング_sp_attack} 期待=1")

# ── ドゲザン ──
check("DB: ドゲザン 取得可能", dl.get_move("ドゲザン") is not None)
_mv_ドゲザン = dl.get_move("ドゲザン")
if _mv_ドゲザン:
    _pa_ドゲザン = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ドゲザン = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ドゲザン = dmg(_pa_ドゲザン, _pd_ドゲザン, "ドゲザン")
    check("ダメージ計算: ドゲザン", _d_ドゲザン > 0, f"dmg={_d_ドゲザン}")
# ドゲザン: 必中
_mvmust_ドゲザン = dl.get_move("ドゲザン")
if _mvmust_ドゲザン:
    random.seed(0); _hit_all_ドゲザン = True
    for _ in range(30):
        _pah = make_poke(type1="あく", atk_b=100, spatk_b=100); _pdh = make_poke(type1="エスパー", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "ドゲザン")
        if _pdh.hp == _hpb: _hit_all_ドゲザン = False; break
    check("必中: ドゲザン", _hit_all_ドゲザン)

# ── レイジングブル ──
check("DB: レイジングブル 取得可能", dl.get_move("レイジングブル") is not None)
_mv_レイジングブル = dl.get_move("レイジングブル")
if _mv_レイジングブル:
    _pa_レイジングブル = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_レイジングブル = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_レイジングブル = dmg(_pa_レイジングブル, _pd_レイジングブル, "レイジングブル")
    check("ダメージ計算: レイジングブル", _d_レイジングブル > 0, f"dmg={_d_レイジングブル}")
# レイジングブル: スクリーン破壊
_mvbrk_レイジングブル = dl.get_move("レイジングブル")
if _mvbrk_レイジングブル:
    random.seed(0); _brk_ok = False
    for _ in range(20):
        _pabrk = make_poke(type1="ノーマル", atk_b=120, spatk_b=120); _pdbrk = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
        _s1b = BattleSide([_pabrk]); _s2b = BattleSide([_pdbrk])
        _s2b.reflect = True; _s2b.reflect_count = 5; _s2b.light_screen = True; _s2b.light_screen_count = 5
        _execute_move(_s1b, _s2b, Action(type="move", move=_mvbrk_レイジングブル), BattleField())
        if not _s2b.reflect and not _s2b.light_screen: _brk_ok = True; break
    check("スクリーン破壊: レイジングブル", _brk_ok)
# レイジングブル: 自分のフォルム(type2)で技タイプが変わる
from simulator.damage import _effective_move_type as _emtr
_prb = make_poke(type1="ノーマル", type2="ほのお")
check("フォルム別タイプ: レイジングブル", _emtr(_prb, dl.get_move("レイジングブル"), BattleField()) == "ほのお", f"type={_emtr(_prb, dl.get_move('レイジングブル'), BattleField())}")

# ── トリックフラワー ──
check("DB: トリックフラワー 取得可能", dl.get_move("トリックフラワー") is not None)
_mv_トリックフラワ_ = dl.get_move("トリックフラワー")
if _mv_トリックフラワ_:
    _pa_トリックフラワ_ = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_トリックフラワ_ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_トリックフラワ_ = dmg(_pa_トリックフラワ_, _pd_トリックフラワ_, "トリックフラワー")
    check("ダメージ計算: トリックフラワー", _d_トリックフラワ_ > 0, f"dmg={_d_トリックフラワ_}")
# トリックフラワー: 必中
_mvmust_トリックフラワ_ = dl.get_move("トリックフラワー")
if _mvmust_トリックフラワ_:
    random.seed(0); _hit_all_トリックフラワ_ = True
    for _ in range(30):
        _pah = make_poke(type1="くさ", atk_b=100, spatk_b=100); _pdh = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "トリックフラワー")
        if _pdh.hp == _hpb: _hit_all_トリックフラワ_ = False; break
    check("必中: トリックフラワー", _hit_all_トリックフラワ_)
# トリックフラワー: 必ず急所（高ダメージ）
_mvcr_トリックフラワ_ = dl.get_move("トリックフラワー")
if _mvcr_トリックフラワ_:
    _pac = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _d_crit = dmg(_pac, make_poke(type1="みず", def_b=100, spdef_b=100), "トリックフラワー")
    check("必ず急所(>0): トリックフラワー", _d_crit > 0)

# ── おかたづけ ──
check("DB: おかたづけ 取得可能", dl.get_move("おかたづけ") is not None)
# おかたづけ: 自分攻撃+1
_mv_sb_おかたづけ_attack = dl.get_move("おかたづけ")
if _mv_sb_おかたづけ_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "おかたづけ")
    check("自分攻撃+1: おかたづけ", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# おかたづけ: 自分素早さ+1
_mv_sb_おかたづけ_speed = dl.get_move("おかたづけ")
if _mv_sb_おかたづけ_speed:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "おかたづけ")
    check("自分素早さ+1: おかたづけ", _pa_sb.stage_speed == 1, f"1回適用={_pa_sb.stage_speed} 期待=+1")

# ── さむいギャグ ──
check("DB: さむいギャグ 取得可能", dl.get_move("さむいギャグ") is not None)
# さむいギャグ: 天候hail
_mv_w_さむいギャグ = dl.get_move("さむいギャグ")
if _mv_w_さむいギャグ:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="こおり"), make_poke(), "さむいギャグ")
    check("天候hail: さむいギャグ", _fw.weather == "hail", f"weather={_fw.weather}")
# さむいギャグ: ピボット交代フラグ
_mvpv_さむいギャグ = dl.get_move("さむいギャグ")
if _mvpv_さむいギャグ:
    _pap = make_poke(type1="こおり", atk_b=100, spatk_b=100); _pdp = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_さむいギャグ), BattleField())
    check("ピボット交代フラグ: さむいギャグ", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")

# ── とびつく ──
check("DB: とびつく 取得可能", dl.get_move("とびつく") is not None)
_mv_とびつく = dl.get_move("とびつく")
if _mv_とびつく:
    _pa_とびつく = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_とびつく = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_とびつく = dmg(_pa_とびつく, _pd_とびつく, "とびつく")
    check("ダメージ計算: とびつく", _d_とびつく > 0, f"dmg={_d_とびつく}")
# とびつく: 相手素早さ-1
_mv_dd_とびつく = dl.get_move("とびつく")
if _mv_dd_とびつく:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_とびつく = 0; _dd_ok_とびつく = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "とびつく")
        if _pd_dd.stage_speed != 0: _dd_val_とびつく = _pd_dd.stage_speed; _dd_ok_とびつく = True; break
    check("相手素早さ-1: とびつく", _dd_ok_とびつく and _dd_val_とびつく == -1, f"1回適用={_dd_val_とびつく} 期待=-1")

# ── くさわけ ──
check("DB: くさわけ 取得可能", dl.get_move("くさわけ") is not None)
_mv_くさわけ = dl.get_move("くさわけ")
if _mv_くさわけ:
    _pa_くさわけ = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_くさわけ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_くさわけ = dmg(_pa_くさわけ, _pd_くさわけ, "くさわけ")
    check("ダメージ計算: くさわけ", _d_くさわけ > 0, f"dmg={_d_くさわけ}")
# くさわけ: 自分素早さ+1
_mvss_くさわけ_speed = dl.get_move("くさわけ")
if _mvss_くさわけ_speed:
    random.seed(0); _got_くさわけ_speed = 0
    for _ in range(60):
        _pas = make_poke(type1="くさ", atk_b=60, spatk_b=60); _pds = make_poke(type1="みず", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "くさわけ")
        if _pas.stage_speed != 0: _got_くさわけ_speed = _pas.stage_speed; break
    check("自分素早さ+1: くさわけ", _got_くさわけ_speed == 1, f"1回適用={_got_くさわけ_speed} 期待=1")

# ── ひやみず ──
check("DB: ひやみず 取得可能", dl.get_move("ひやみず") is not None)
_mv_ひやみず = dl.get_move("ひやみず")
if _mv_ひやみず:
    _pa_ひやみず = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ひやみず = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ひやみず = dmg(_pa_ひやみず, _pd_ひやみず, "ひやみず")
    check("ダメージ計算: ひやみず", _d_ひやみず > 0, f"dmg={_d_ひやみず}")
# ひやみず: 相手攻撃-1
_mv_dd_ひやみず = dl.get_move("ひやみず")
if _mv_dd_ひやみず:
    _pa_dd = make_poke(type1="みず", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ひやみず = 0; _dd_ok_ひやみず = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ほのお", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ひやみず")
        if _pd_dd.stage_attack != 0: _dd_val_ひやみず = _pd_dd.stage_attack; _dd_ok_ひやみず = True; break
    check("相手攻撃-1: ひやみず", _dd_ok_ひやみず and _dd_val_ひやみず == -1, f"1回適用={_dd_val_ひやみず} 期待=-1")

# ── しっぽきり ──
check("DB: しっぽきり 取得可能", dl.get_move("しっぽきり") is not None)
# しっぽきり: ピボット交代フラグ
_mvpv_しっぽきり = dl.get_move("しっぽきり")
if _mvpv_しっぽきり:
    _pap = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pdp = make_poke(type1="ノーマル", hp_b=255, def_b=100, spdef_b=100)
    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])
    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_しっぽきり), BattleField())
    check("ピボット交代フラグ: しっぽきり", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")
# しっぽきり: HP1/2を消費してみがわりを残す
_satk = BattleSide([make_poke(hp_b=200), make_poke()]); _satk.active.hp = _satk.active.max_hp; _hpsk = _satk.active.hp
_execute_move(_satk, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("しっぽきり")), BattleField())
check("みがわり生成: しっぽきり", getattr(_satk.party[0], "_substitute_hp", 0) > 0 and _satk.party[0].hp < _hpsk, f"sub={getattr(_satk.party[0],'_substitute_hp',0)}")
# 消費は最大HP1/2・身代わりHPは最大HP1/4（effect_text通り）
_satk_v = BattleSide([make_poke(hp_b=200), make_poke()]); _satk_v.active.hp = _satk_v.active.max_hp; _mhp = _satk_v.active.max_hp
_execute_move(_satk_v, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("しっぽきり")), BattleField())
check("HP消費1/2: しっぽきり", _satk_v.party[0].hp == _mhp - _mhp // 2, f"hp={_satk_v.party[0].hp} 期待={_mhp - _mhp // 2}")
check("身代わりHP1/4: しっぽきり", _satk_v.party[0]._substitute_hp == _mhp // 4, f"sub={_satk_v.party[0]._substitute_hp} 期待={_mhp // 4}")
# 身代わりが技を肩代わり（本体ダメージなし）
_holder = _satk_v.party[0]; _sub_sk = _holder._substitute_hp; _hp_sk = _holder.hp
_atksk = make_poke(type1="ノーマル", atk_b=20, moves=["たいあたり"])
_execute_move(BattleSide([_atksk]), BattleSide([_holder]), Action(type="move", move=dl.get_move("たいあたり")), BattleField())
check("身代わりが肩代わり(本体ダメージなし): しっぽきり", _holder.hp == _hp_sk and getattr(_holder,"_substitute_hp",0) < _sub_sk, f"hp={_holder.hp}/{_hp_sk} sub={getattr(_holder,'_substitute_hp',0)}/{_sub_sk}")

# ── ツインビーム ──
check("DB: ツインビーム 取得可能", dl.get_move("ツインビーム") is not None)
_mv_ツインビ_ム = dl.get_move("ツインビーム")
if _mv_ツインビ_ム:
    _pa_ツインビ_ム = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_ツインビ_ム = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_ツインビ_ム = dmg(_pa_ツインビ_ム, _pd_ツインビ_ム, "ツインビーム")
    check("ダメージ計算: ツインビーム", _d_ツインビ_ム > 0, f"dmg={_d_ツインビ_ム}")
# ツインビーム: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ツインビ_ム = dl.get_move("ツインビーム")
if _mvmh_ツインビ_ム:
    _pam = make_poke(type1="エスパー", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ツインビ_ム = calc_damage(_pam, make_poke(type1="かくとう", hp_b=255, def_b=200, spdef_b=200), _mvmh_ツインビ_ム, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ツインビ_ム = 0
    for _ in range(20):
        _pdm = make_poke(type1="かくとう", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ツインビーム"); _multi_ツインビ_ム = _pdm.max_hp - _pdm.hp
        if _multi_ツインビ_ム > _single_ツインビ_ム: break
    check("多段ヒット発生(複数回): ツインビーム", _multi_ツインビ_ム > _single_ツインビ_ム, f"single={_single_ツインビ_ム} multi={_multi_ツインビ_ム}")

# ── むねんのつるぎ ──
check("DB: むねんのつるぎ 取得可能", dl.get_move("むねんのつるぎ") is not None)
_mv_むねんのつるぎ = dl.get_move("むねんのつるぎ")
if _mv_むねんのつるぎ:
    _pa_むねんのつるぎ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_むねんのつるぎ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_むねんのつるぎ = dmg(_pa_むねんのつるぎ, _pd_むねんのつるぎ, "むねんのつるぎ")
    check("ダメージ計算: むねんのつるぎ", _d_むねんのつるぎ > 0, f"dmg={_d_むねんのつるぎ}")
# むねんのつるぎ: ドレイン（与ダメの1/2回復）
_mv_dr_むねんのつるぎ = dl.get_move("むねんのつるぎ")
if _mv_dr_むねんのつるぎ:
    _pa_dr = make_poke(type1="ほのお", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_むねんのつるぎ = False; _dr_dealt_むねんのつるぎ = 0; _dr_heal_むねんのつるぎ = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="くさ", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "むねんのつるぎ")
        _dr_dealt_むねんのつるぎ = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_むねんのつるぎ = _pa_dr.hp - 1
        if _dr_dealt_むねんのつるぎ > 0: _dr_ok_むねんのつるぎ = abs(_dr_heal_むねんのつるぎ - max(1, _dr_dealt_むねんのつるぎ * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): むねんのつるぎ", _dr_ok_むねんのつるぎ, f"dealt={_dr_dealt_むねんのつるぎ} heal={_dr_heal_むねんのつるぎ}")

# ── アーマーキャノン ──
check("DB: アーマーキャノン 取得可能", dl.get_move("アーマーキャノン") is not None)
_mv_ア_マ_キャノン = dl.get_move("アーマーキャノン")
if _mv_ア_マ_キャノン:
    _pa_ア_マ_キャノン = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ア_マ_キャノン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ア_マ_キャノン = dmg(_pa_ア_マ_キャノン, _pd_ア_マ_キャノン, "アーマーキャノン")
    check("ダメージ計算: アーマーキャノン", _d_ア_マ_キャノン > 0, f"dmg={_d_ア_マ_キャノン}")
# アーマーキャノン: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="ほのお", atk_b=120, spatk_b=120); _dsd = make_poke(type1="くさ", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "アーマーキャノン")
    if _psd.stage_defense < 0: break
check("自分防御下降: アーマーキャノン", _psd.stage_defense < 0, f"stage={_psd.stage_defense}")
check("自分特防下降: アーマーキャノン", _psd.stage_sp_defense < 0, f"stage={_psd.stage_sp_defense}")

# ── デカハンマー ──
check("DB: デカハンマー 取得可能", dl.get_move("デカハンマー") is not None)
_mv_デカハンマ_ = dl.get_move("デカハンマー")
if _mv_デカハンマ_:
    _pa_デカハンマ_ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_デカハンマ_ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_デカハンマ_ = dmg(_pa_デカハンマ_, _pd_デカハンマ_, "デカハンマー")
    check("ダメージ計算: デカハンマー", _d_デカハンマ_ > 0, f"dmg={_d_デカハンマ_}")
# デカハンマー: 2ターン連続では使えない
_pdh = make_poke(type1="はがね", atk_b=120); _ddh = make_poke(type1="フェアリー", hp_b=255, def_b=120)
execute(_pdh, _ddh, "デカハンマー"); _hp_after1 = _ddh.hp; execute(_pdh, _ddh, "デカハンマー")
check("連続不可: デカハンマー", _ddh.hp == _hp_after1, f"2回目hp={_ddh.hp}/{_hp_after1}")

# ── ほうふく ──
check("DB: ほうふく 取得可能", dl.get_move("ほうふく") is not None)
_mv_ほうふく = dl.get_move("ほうふく")
if _mv_ほうふく:
    _pa_ほうふく = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ほうふく = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ほうふく = dmg(_pa_ほうふく, _pd_ほうふく, "ほうふく")
    check("ダメージ計算: ほうふく", _d_ほうふく > 0, f"dmg={_d_ほうふく}")
# ほうふく: カウンター反射（物理+特殊×1.5）
_mvcnt_ほうふく = dl.get_move("ほうふく")
if _mvcnt_ほうふく:
    _pac_cnt = make_poke(type1="あく", atk_b=100, spatk_b=100, hp_b=200)
    _pdc_cnt = make_poke(type1="ノーマル" if "あく"!="かくとう" else "エスパー", hp_b=255, def_b=100, spdef_b=100)
    _pac_cnt._last_physical_dmg_received = 100
    _exp_cnt = int(100 * 1.5)
    _hpc0 = _pdc_cnt.hp; execute(_pac_cnt, _pdc_cnt, "ほうふく")
    check("カウンター反射: ほうふく", _hpc0 - _pdc_cnt.hp == _exp_cnt, f"返し={_hpc0 - _pdc_cnt.hp} 期待={_exp_cnt}")
    _pac_cnt2 = make_poke(type1="あく", atk_b=100, spatk_b=100); _pdc_cnt2 = make_poke(type1="ノーマル", hp_b=255)
    _hpc20 = _pdc_cnt2.hp; execute(_pac_cnt2, _pdc_cnt2, "ほうふく")
    check("カウンター被ダメ0で失敗: ほうふく", _pdc_cnt2.hp == _hpc20)

# ── アクアカッター ──
check("DB: アクアカッター 取得可能", dl.get_move("アクアカッター") is not None)
_mv_アクアカッタ_ = dl.get_move("アクアカッター")
if _mv_アクアカッタ_:
    _pa_アクアカッタ_ = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_アクアカッタ_ = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_アクアカッタ_ = dmg(_pa_アクアカッタ_, _pd_アクアカッタ_, "アクアカッター")
    check("ダメージ計算: アクアカッター", _d_アクアカッタ_ > 0, f"dmg={_d_アクアカッタ_}")
# アクアカッター: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_アクアカッタ_
random.seed(0); _hc_crit_アクアカッタ_ = 0; _phc = make_poke(type1="みず")
_mvhc_アクアカッタ_ = dl.get_move("アクアカッター")
for _ in range(800):
    if _cc_アクアカッタ_(_phc, _mvhc_アクアカッタ_, make_poke(type1="ほのお")): _hc_crit_アクアカッタ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: アクアカッター", 60 <= _hc_crit_アクアカッタ_ <= 150, f"crit={_hc_crit_アクアカッタ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── みずあめボム ──
check("DB: みずあめボム 取得可能", dl.get_move("みずあめボム") is not None)
_mv_みずあめボム = dl.get_move("みずあめボム")
if _mv_みずあめボム:
    _pa_みずあめボム = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_みずあめボム = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_みずあめボム = dmg(_pa_みずあめボム, _pd_みずあめボム, "みずあめボム")
    check("ダメージ計算: みずあめボム", _d_みずあめボム > 0, f"dmg={_d_みずあめボム}")
# みずあめボム: 相手をあめまみれ状態に（素早さ低下）
_psb = make_poke(type1="みず", spatk_b=100); _dsb = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)
random.seed(0)
for _ in range(20):
    execute(_psb, _dsb, "みずあめボム")
    if _dsb.syrup_count == 3: break
check("あめまみれ付与: みずあめボム", _dsb.syrup_count == 3, f"syrup={_dsb.syrup_count}")

# ── シャカシャカほう ──
check("DB: シャカシャカほう 取得可能", dl.get_move("シャカシャカほう") is not None)
_mv_シャカシャカほう = dl.get_move("シャカシャカほう")
if _mv_シャカシャカほう:
    _pa_シャカシャカほう = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_シャカシャカほう = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_シャカシャカほう = dmg(_pa_シャカシャカほう, _pd_シャカシャカほう, "シャカシャカほう")
    check("ダメージ計算: シャカシャカほう", _d_シャカシャカほう > 0, f"dmg={_d_シャカシャカほう}")
# シャカシャカほう: やけど20%
_mv_s_シャカシャカほう = dl.get_move("シャカシャカほう")
if _mv_s_シャカシャカほう:
    random.seed(0); _hit_シャカシャカほう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="くさ", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "シャカシャカほう")
        _hit_シャカシャカほう += int((_pd2.status == "burn"))
    check("追加効果(やけど20%): シャカシャカほう", 18 <= _hit_シャカシャカほう <= 117, f"count={_hit_シャカシャカほう}/300")
    random.seed(1); _immok_シャカシャカほう = True
    for _ in range(60):
        _pai = make_poke(type1="くさ", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "シャカシャカほう")
        if _pdi.status == "burn": _immok_シャカシャカほう = False; break
    check("やけど免疫(ほのお型には無効): シャカシャカほう", _immok_シャカシャカほう, "免疫タイプに状態異常が付与されないこと")
# シャカシャカほう: ドレイン（与ダメの1/2回復）
_mv_dr_シャカシャカほう = dl.get_move("シャカシャカほう")
if _mv_dr_シャカシャカほう:
    _pa_dr = make_poke(type1="くさ", atk_b=150, spatk_b=150, hp_b=200)
    random.seed(0); _dr_ok_シャカシャカほう = False; _dr_dealt_シャカシャカほう = 0; _dr_heal_シャカシャカほう = 0
    for _ in range(20):
        _pa_dr.hp = 1; _pd_dr = make_poke(type1="みず", def_b=50, spdef_b=50, hp_b=255)
        execute(_pa_dr, _pd_dr, "シャカシャカほう")
        _dr_dealt_シャカシャカほう = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_シャカシャカほう = _pa_dr.hp - 1
        if _dr_dealt_シャカシャカほう > 0: _dr_ok_シャカシャカほう = abs(_dr_heal_シャカシャカほう - max(1, _dr_dealt_シャカシャカほう * 1 // 2)) <= 2; break
    check("ドレイン回復(与ダメ1/2): シャカシャカほう", _dr_ok_シャカシャカほう, f"dealt={_dr_dealt_シャカシャカほう} heal={_dr_heal_シャカシャカほう}")

# ── エレクトロビーム ──
check("DB: エレクトロビーム 取得可能", dl.get_move("エレクトロビーム") is not None)
_mv_エレクトロビ_ム = dl.get_move("エレクトロビーム")
if _mv_エレクトロビ_ム:
    _pa_エレクトロビ_ム = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_エレクトロビ_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_エレクトロビ_ム = make_poke(type1="でんき", atk_b=100, spatk_b=100); _pd_エレクトロビ_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
        execute(_pa_エレクトロビ_ム, _pd_エレクトロビ_ム, "エレクトロビーム"); execute(_pa_エレクトロビ_ム, _pd_エレクトロビ_ム, "エレクトロビーム")
        if _pd_エレクトロビ_ム.hp < _pd_エレクトロビ_ム.max_hp: break
    check("ダメージ計算: エレクトロビーム", _pd_エレクトロビ_ム.hp < _pd_エレクトロビ_ム.max_hp, f"hp={_pd_エレクトロビ_ム.hp}")
# エレクトロビーム: 2ターン溜め
_mv_2t_エレクトロビ_ム = dl.get_move("エレクトロビーム")
if _mv_2t_エレクトロビ_ム:
    _pa_2t = make_poke(type1="でんき", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="みず", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "エレクトロビーム")
    check("2ターン溜め(1T)ダメなし: エレクトロビーム", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: エレクトロビーム", _pa_2t.charging_move == "エレクトロビーム")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "エレクトロビーム")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "エレクトロビーム")
    check("2ターン溜め(2T)ダメあり: エレクトロビーム", _pd_2t.hp < _hp_before_2t)
# エレクトロビーム: 溜めターン自己特攻+1
_mvcb_エレクトロビ_ム = dl.get_move("エレクトロビーム")
if _mvcb_エレクトロビ_ム:
    _pacb = make_poke(type1="でんき", atk_b=60, spatk_b=60); _pdcb = make_poke(type1="みず", hp_b=255)
    execute(_pacb, _pdcb, "エレクトロビーム")  # 溜めターン
    check("溜め自己特攻+1: エレクトロビーム", _pacb.stage_sp_attack >= 1, f"stage={_pacb.stage_sp_attack}")
# エレクトロビーム: あめ状態では溜めず即攻撃（1ターン目でダメージ）
_fwi_エレクトロビ_ム = BattleField(); _fwi_エレクトロビ_ム.weather = "rain"
_pwi_エレクトロビ_ム = make_poke(type1="でんき", atk_b=120, spatk_b=120); _dwi_エレクトロビ_ム = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100); _hpwi_エレクトロビ_ム = _dwi_エレクトロビ_ム.hp
execute(_pwi_エレクトロビ_ム, _dwi_エレクトロビ_ム, "エレクトロビーム", _fwi_エレクトロビ_ム)
check("あめで即発動(1Tダメージ): エレクトロビーム", _dwi_エレクトロビ_ム.hp < _hpwi_エレクトロビ_ム and _pwi_エレクトロビ_ム.charging_move is None, f"hp={_dwi_エレクトロビ_ム.hp}/{_hpwi_エレクトロビ_ム} charging={_pwi_エレクトロビ_ム.charging_move}")
check("あめ即攻撃でも自己特攻+1: エレクトロビーム", _pwi_エレクトロビ_ム.stage_sp_attack >= 1, f"stage={_pwi_エレクトロビ_ム.stage_sp_attack}")

# ── きまぐレーザー ──
check("DB: きまぐレーザー 取得可能", dl.get_move("きまぐレーザー") is not None)
_mv_きまぐレ_ザ_ = dl.get_move("きまぐレーザー")
if _mv_きまぐレ_ザ_:
    _pa_きまぐレ_ザ_ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_きまぐレ_ザ_ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_きまぐレ_ザ_ = dmg(_pa_きまぐレ_ザ_, _pd_きまぐレ_ザ_, "きまぐレーザー")
    check("ダメージ計算: きまぐレーザー", _d_きまぐレ_ザ_ > 0, f"dmg={_d_きまぐレ_ザ_}")
# きまぐレーザー: 30%で威力2倍（複数回で2倍が出る）
_pkl = make_poke(spatk_b=100); _dkl = make_poke(def_b=100)
random.seed(0); _kls = [_ep(_pkl, _dkl, dl.get_move("きまぐレーザー"), BattleField()) for _ in range(60)]
_klbase = min(_kls); check("30%威力2倍: きまぐレーザー", max(_kls) == _klbase * 2, f"vals={sorted(set(_kls))}")

# ── やけっぱち ──
check("DB: やけっぱち 取得可能", dl.get_move("やけっぱち") is not None)
_mv_やけっぱち = dl.get_move("やけっぱち")
if _mv_やけっぱち:
    _pa_やけっぱち = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_やけっぱち = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_やけっぱち = dmg(_pa_やけっぱち, _pd_やけっぱち, "やけっぱち")
    check("ダメージ計算: やけっぱち", _d_やけっぱち > 0, f"dmg={_d_やけっぱち}")
# やけっぱち: 前ターン失敗で威力2倍（実効威力で厳密比較）
_mvj = dl.get_move("やけっぱち")
_paj = make_poke(type1="ほのお", atk_b=100, spatk_b=100); _pdj = make_poke(type1="くさ", def_b=100, spdef_b=100)
_p_normal = _ep(_paj, _pdj, _mvj, BattleField())
_paj._move_failed_last = True
_p_double = _ep(_paj, _pdj, _mvj, BattleField())
check("前ターン失敗2倍: やけっぱち", _p_double == _p_normal * 2, f"normal={_p_normal} double={_p_double}")
# 条件成立: 技を外すと _move_failed_this_turn が立つ（実戦arising）
import copy as _cpj; _mvmiss = _cpj.copy(_mvj); _mvmiss.accuracy = 1
random.seed(0); _missset = False
for _ in range(40):
    _pjm = make_poke(type1="ほのお", atk_b=100, spatk_b=100); _djm = make_poke(type1="くさ", hp_b=255)
    _execute_move(BattleSide([_pjm]), BattleSide([_djm]), Action(type="move", move=_mvmiss), BattleField())
    if getattr(_pjm, "_move_failed_this_turn", False): _missset = True; break
check("外すと失敗フラグ成立: やけっぱち", _missset, "技を外すと_move_failed_this_turnが立つこと")
# ターン終了で前ターン失敗へ繰り越す
from simulator.battle import Battle as _Bjd
_pcarry = make_poke(type1="ほのお"); _pcarry._move_failed_this_turn = True
_Bjd(BattleSide([_pcarry]), BattleSide([make_poke()]))._end_of_turn()
check("失敗フラグ繰り越し: やけっぱち", _pcarry._move_failed_last, "ターン終了で_move_failed_lastに繰り越すこと")

# ── サイコノイズ ──
check("DB: サイコノイズ 取得可能", dl.get_move("サイコノイズ") is not None)
_mv_サイコノイズ = dl.get_move("サイコノイズ")
if _mv_サイコノイズ:
    _pa_サイコノイズ = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_サイコノイズ = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_サイコノイズ = dmg(_pa_サイコノイズ, _pd_サイコノイズ, "サイコノイズ")
    check("ダメージ計算: サイコノイズ", _d_サイコノイズ > 0, f"dmg={_d_サイコノイズ}")
# サイコノイズ: 相手をかいふくふうじ状態に
_psn = make_poke(type1="エスパー", spatk_b=100); _dsn = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)
execute(_psn, _dsn, "サイコノイズ")
check("かいふくふうじ付与: サイコノイズ", _dsn.heal_block_count == 2, f"hb={_dsn.heal_block_count}")

# ── サンダーダイブ ──
check("DB: サンダーダイブ 取得可能", dl.get_move("サンダーダイブ") is not None)
_mv_サンダ_ダイブ = dl.get_move("サンダーダイブ")
if _mv_サンダ_ダイブ:
    _pa_サンダ_ダイブ = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_サンダ_ダイブ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_サンダ_ダイブ = dmg(_pa_サンダ_ダイブ, _pd_サンダ_ダイブ, "サンダーダイブ")
    check("ダメージ計算: サンダーダイブ", _d_サンダ_ダイブ > 0, f"dmg={_d_サンダ_ダイブ}")
# サンダーダイブ: 外れ時1/2自傷
_mv_mr_サンダ_ダイブ = dl.get_move("サンダーダイブ")
if _mv_mr_サンダ_ダイブ:
    _pa_mr = make_poke(type1="でんき", atk_b=100)
    import copy as _cp; _mv_miss = _cp.copy(_mv_mr_サンダ_ダイブ); _mv_miss.accuracy = 1
    random.seed(99); _s1m = BattleSide([_pa_mr]); _s2m = BattleSide([make_poke()])
    _execute_move(_s1m, _s2m, Action(type="move", move=_mv_miss), BattleField())
    check("外れ時1/2自傷: サンダーダイブ", _pa_mr.max_hp - _pa_mr.hp == max(1, _pa_mr.max_hp//2), f"dmg={_pa_mr.max_hp - _pa_mr.hp}")
# サンダーダイブ: ちいさくなる状態の相手に威力2倍
_pm = make_poke(type1="でんき", atk_b=100, spatk_b=100)
_dm0 = make_poke(type1="みず", def_b=100, spdef_b=100)
_dm1 = make_poke(type1="みず", def_b=100, spdef_b=100); _dm1.minimized = True
_pm_n = _ep(_pm, _dm0, dl.get_move("サンダーダイブ"), BattleField())
_pm_m = _ep(_pm, _dm1, dl.get_move("サンダーダイブ"), BattleField())
check("ちいさくなる2倍: サンダーダイブ", _pm_m == _pm_n * 2, f"normal={_pm_n} mini={_pm_m}")

# ── みわくのボイス ──
check("DB: みわくのボイス 取得可能", dl.get_move("みわくのボイス") is not None)
_mv_みわくのボイス = dl.get_move("みわくのボイス")
if _mv_みわくのボイス:
    _pa_みわくのボイス = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_みわくのボイス = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_みわくのボイス = dmg(_pa_みわくのボイス, _pd_みわくのボイス, "みわくのボイス")
    check("ダメージ計算: みわくのボイス", _d_みわくのボイス > 0, f"dmg={_d_みわくのボイス}")
# みわくのボイス: 相手の能力上昇時のみ状態異常
_psj = make_poke(type1="フェアリー", spatk_b=100, atk_b=100)
random.seed(0); _sj_ok = False
for _ in range(20):
    _dsj = make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200); _dsj.stage_attack = 2
    execute(_psj, _dsj, "みわくのボイス")
    if _dsj.confused: _sj_ok = True; break
check("能力上昇時の状態異常: みわくのボイス", _sj_ok)
# negative: 相手の能力が上がっていなければ付与されない
random.seed(1); _sj_neg = True
for _ in range(40):
    _dsn = make_poke(type1="ドラゴン", hp_b=255, def_b=200, spdef_b=200)
    execute(_psj, _dsn, "みわくのボイス")
    if _dsn.confused: _sj_neg = False; break
check("能力非上昇時は付与なし: みわくのボイス", _sj_neg, "能力上昇がなければ状態異常は付かない")

# ── はやてがえし ──
check("DB: はやてがえし 取得可能", dl.get_move("はやてがえし") is not None)
_mv_はやてがえし = dl.get_move("はやてがえし")
if _mv_はやてがえし:
    _pa_はやてがえし = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_はやてがえし = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_はやてがえし = dmg(_pa_はやてがえし, _pd_はやてがえし, "はやてがえし")
    check("ダメージ計算: はやてがえし", _d_はやてがえし > 0, f"dmg={_d_はやてがえし}")
# はやてがえし: 優先度3
_mv_pr_はやてがえし = dl.get_move("はやてがえし")
if _mv_pr_はやてがえし and _mv_pr_はやてがえし.priority == 3:
    check("優先度3: はやてがえし", _mv_pr_はやてがえし.priority == 3)
elif _mv_pr_はやてがえし:
    check("優先度3: はやてがえし", _mv_pr_はやてがえし.priority == 3, f"DB優先度={_mv_pr_はやてがえし.priority} 仕様=3")
# はやてがえし: 相手が先制技を選んでいないと失敗、選んでいれば命中しひるませる
_pqg = make_poke(type1="ひこう", atk_b=120)
_opp_quick = Action(type="move", move=dl.get_move("でんこうせっか"))
_opp_slow = Action(type="move", move=dl.get_move("のしかかり"))
# 相手が通常技→失敗（無傷）
_dqg = make_poke(type1="ノーマル", hp_b=255, def_b=200); _hpq1 = _dqg.hp
_execute_move(BattleSide([_pqg]), BattleSide([_dqg]), Action(type="move", move=dl.get_move("はやてがえし")), BattleField(), _opp_slow)
check("先制技なしで失敗: はやてがえし", _dqg.hp == _hpq1, f"hp={_dqg.hp}/{_hpq1}")
# 相手が先制技→成功しひるませる
random.seed(0); _qg_flinch = False
for _ in range(20):
    _dqg2 = make_poke(type1="ノーマル", hp_b=255, def_b=200)
    _execute_move(BattleSide([_pqg]), BattleSide([_dqg2]), Action(type="move", move=dl.get_move("はやてがえし")), BattleField(), _opp_quick)
    if _dqg2.flinched: _qg_flinch = True; break
check("ひるみ(先制技相手): はやてがえし", _qg_flinch)

# ── きあいだめ ──
check("DB: きあいだめ 取得可能", dl.get_move("きあいだめ") is not None)
# きあいだめ: 急所ランク+2
_pkd = make_poke(type1="ノーマル"); execute(_pkd, make_poke(), "きあいだめ")
check("急所ランク+2: きあいだめ", _pkd.crit_stage == 2, f"crit_stage={_pkd.crit_stage}")

# ── しびれごな ──
check("DB: しびれごな 取得可能", dl.get_move("しびれごな") is not None)
# しびれごな: まひ付与(変化技)
_mv_si_しびれごな = dl.get_move("しびれごな")
if _mv_si_しびれごな:
    random.seed(0); _ok_しびれごな = False
    for _ in range(30):
        _pa_si = make_poke(type1="くさ"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "しびれごな")
        if _pd_si.status == "paralysis": _ok_しびれごな = True; break
    check("まひ付与: しびれごな", _ok_しびれごな)
    random.seed(2); _siimm_しびれごな = True
    for _ in range(40):
        _pai2 = make_poke(type1="くさ"); _pdi2 = make_poke(type1="でんき", hp_b=255)
        execute(_pai2, _pdi2, "しびれごな")
        if _pdi2.status == "paralysis": _siimm_しびれごな = False; break
    check("まひ免疫(でんき型には無効): しびれごな", _siimm_しびれごな, "免疫タイプに付与されないこと")
# しびれごな: 粉技。くさタイプには無効
_ppw = make_poke(type1="くさ"); random.seed(0); _pw_ok = False
for _ in range(20):
    _dpw = make_poke(type1="ノーマル", hp_b=200); execute(_ppw, _dpw, "しびれごな")
    if _dpw.status == "paralysis": _pw_ok = True; break
check("粉付与: しびれごな", _pw_ok)
_dpw2 = make_poke(type1="くさ", hp_b=200)
for _ in range(20): execute(_ppw, _dpw2, "しびれごな")
check("くさ無効: しびれごな", _dpw2.status is None, f"status={_dpw2.status}")

# ── ともえなげ ──
check("DB: ともえなげ 取得可能", dl.get_move("ともえなげ") is not None)
_mv_ともえなげ = dl.get_move("ともえなげ")
if _mv_ともえなげ:
    _pa_ともえなげ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ともえなげ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ともえなげ = dmg(_pa_ともえなげ, _pd_ともえなげ, "ともえなげ")
    check("ダメージ計算: ともえなげ", _d_ともえなげ > 0, f"dmg={_d_ともえなげ}")
# ともえなげ: 優先度-6
_mv_pr_ともえなげ = dl.get_move("ともえなげ")
if _mv_pr_ともえなげ and _mv_pr_ともえなげ.priority == -6:
    check("優先度-6: ともえなげ", _mv_pr_ともえなげ.priority == -6)
elif _mv_pr_ともえなげ:
    check("優先度-6: ともえなげ", _mv_pr_ともえなげ.priority == -6, f"DB優先度={_mv_pr_ともえなげ.priority} 仕様=-6")
# ともえなげ: 控えがいれば相手をランダム交代させる／控えがいなければ交代しない
from simulator.battle import Battle as _Bfsw
import simulator.battle as _SBfsw; _mx_fsw = _SBfsw.MAX_TURNS; _SBfsw.MAX_TURNS = 1
import copy as _cpfs; _mvfs = _cpfs.copy(dl.get_move("ともえなげ")); _mvfs.accuracy = 100
_actfsw = lambda s,o,f: Action(type="move", move=_mvfs, move_idx=0)
_actwk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_pfsw = make_poke(type1="かくとう", atk_b=120, spd_b=200, moves=["ともえなげ"])
_df0 = make_poke(type1="ノーマル", hp_b=255, def_b=200, spd_b=10, moves=["たいあたり"]); _df1 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])
_sdef = BattleSide([_df0, _df1])
_Bfsw(BattleSide([_pfsw]), _sdef).run(_actfsw, _actwk)
check("控え有りで強制交代: ともえなげ", _sdef.active is not _df0, f"active_idx={_sdef.active_idx}")
_pfsw2 = make_poke(type1="かくとう", atk_b=120, spd_b=200, moves=["ともえなげ"])
_dsolo = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _ssolo = BattleSide([_dsolo])
_Bfsw(BattleSide([_pfsw2]), _ssolo).run(_actfsw, _actwk)
check("控えなしでは交代しない: ともえなげ", _ssolo.active is _dsolo, "1体なら強制交代は発生しない")
_SBfsw.MAX_TURNS = _mx_fsw

# ── ねごと ──
check("DB: ねごと 取得可能", dl.get_move("ねごと") is not None)
# ねごと: ねむり中に技を使う
_png = make_poke(atk_b=120, moves=["たいあたり"]); _png.status = "sleep"
_dng = make_poke(hp_b=200, def_b=50); _hng = _dng.hp
execute(_png, _dng, "ねごと")
check("ねごと 技発動: ねごと", _dng.hp < _hng, f"hp={_dng.hp}")
# negative: 覚醒(非ねむり)状態では失敗
_png_aw = make_poke(atk_b=120, moves=["たいあたり"]); _dng_aw = make_poke(hp_b=200, def_b=50); _hng_aw = _dng_aw.hp
execute(_png_aw, _dng_aw, "ねごと")
check("覚醒時は失敗: ねごと", _dng_aw.hp == _hng_aw, f"hp={_dng_aw.hp}/{_hng_aw}")

# ── クリアスモッグ ──
check("DB: クリアスモッグ 取得可能", dl.get_move("クリアスモッグ") is not None)
_mv_クリアスモッグ = dl.get_move("クリアスモッグ")
if _mv_クリアスモッグ:
    _pa_クリアスモッグ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_クリアスモッグ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_クリアスモッグ = dmg(_pa_クリアスモッグ, _pd_クリアスモッグ, "クリアスモッグ")
    check("ダメージ計算: クリアスモッグ", _d_クリアスモッグ > 0, f"dmg={_d_クリアスモッグ}")
# クリアスモッグ: 必中
_mvmust_クリアスモッグ = dl.get_move("クリアスモッグ")
if _mvmust_クリアスモッグ:
    random.seed(0); _hit_all_クリアスモッグ = True
    for _ in range(30):
        _pah = make_poke(type1="どく", atk_b=100, spatk_b=100); _pdh = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "クリアスモッグ")
        if _pdh.hp == _hpb: _hit_all_クリアスモッグ = False; break
    check("必中: クリアスモッグ", _hit_all_クリアスモッグ)
# クリアスモッグ: 命中時に相手の能力変化をリセット
_pcl = make_poke(type1="どく", spatk_b=100); _dcl = make_poke(type1="ノーマル", hp_b=255, spdef_b=120); _dcl.stage_attack = 2; _dcl.stage_speed = 3
execute(_pcl, _dcl, "クリアスモッグ")
check("能力リセット: クリアスモッグ", _dcl.stage_attack == 0 and _dcl.stage_speed == 0, f"atk={_dcl.stage_attack} spd={_dcl.stage_speed}")

# ── ダメおし ──
check("DB: ダメおし 取得可能", dl.get_move("ダメおし") is not None)
_mv_ダメおし = dl.get_move("ダメおし")
if _mv_ダメおし:
    _pa_ダメおし = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_ダメおし = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ダメおし = dmg(_pa_ダメおし, _pd_ダメおし, "ダメおし")
    check("ダメージ計算: ダメおし", _d_ダメおし > 0, f"dmg={_d_ダメおし}")
# ダメおし: _acts_second状態（相手が既に行動済み）で威力2倍
_pd = make_poke(atk_b=100); _dd = make_poke(def_b=100)
_da1 = _ep(_pd, _dd, dl.get_move("ダメおし"), BattleField()); _pd._acts_second = True; _da2 = _ep(_pd, _dd, dl.get_move("ダメおし"), BattleField())
check("ダメおし後攻2倍: ダメおし", _da2 == _da1 * 2, f"a={_da1} b={_da2}")
# 実戦: 後攻（遅い）で使うと先攻時より大ダメージ＝条件が実機能
from simulator.battle import Battle as _Bdm
import simulator.battle as _SBdm; _mdm = _SBdm.MAX_TURNS; _SBdm.MAX_TURNS = 1
_act_dm = lambda s,o,f: Action(type="move", move=dl.get_move("ダメおし"), move_idx=0)
_act_wk2 = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)
_pdm_slow = make_poke(type1="あく", atk_b=120, spd_b=10, moves=["ダメおし"]); _fdm = make_poke(type1="エスパー", atk_b=10, spd_b=200, hp_b=255, def_b=120, moves=["たいあたり"])
_Bdm(BattleSide([_pdm_slow]), BattleSide([_fdm])).run(_act_dm, _act_wk2)
_dmg_2nd = _fdm.max_hp - _fdm.hp
_pdm_fast = make_poke(type1="あく", atk_b=120, spd_b=200, moves=["ダメおし"]); _fdm2 = make_poke(type1="エスパー", atk_b=10, spd_b=10, hp_b=255, def_b=120, moves=["たいあたり"])
_Bdm(BattleSide([_pdm_fast]), BattleSide([_fdm2])).run(_act_dm, _act_wk2)
_dmg_1st = _fdm2.max_hp - _fdm2.hp; _SBdm.MAX_TURNS = _mdm
check("後攻条件が実戦で成立: ダメおし", _dmg_2nd > _dmg_1st * 1.4, f"後攻={_dmg_2nd} 先攻={_dmg_1st}")

# ── ドリルくちばし ──
check("DB: ドリルくちばし 取得可能", dl.get_move("ドリルくちばし") is not None)
_mv_ドリルくちばし = dl.get_move("ドリルくちばし")
if _mv_ドリルくちばし:
    _pa_ドリルくちばし = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ドリルくちばし = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ドリルくちばし = dmg(_pa_ドリルくちばし, _pd_ドリルくちばし, "ドリルくちばし")
    check("ダメージ計算: ドリルくちばし", _d_ドリルくちばし > 0, f"dmg={_d_ドリルくちばし}")

# ── ブラストバーン ──
check("DB: ブラストバーン 取得可能", dl.get_move("ブラストバーン") is not None)
_mv_ブラストバ_ン = dl.get_move("ブラストバーン")
if _mv_ブラストバ_ン:
    _pa_ブラストバ_ン = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ブラストバ_ン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ブラストバ_ン = dmg(_pa_ブラストバ_ン, _pd_ブラストバ_ン, "ブラストバーン")
    check("ダメージ計算: ブラストバーン", _d_ブラストバ_ン > 0, f"dmg={_d_ブラストバ_ン}")
# ブラストバーン: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="ほのお", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "ブラストバーン")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: ブラストバーン", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="ほのお", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="くさ", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "ブラストバーン")
check("リチャージ中行動不能: ブラストバーン", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── たいあたり ──
check("DB: たいあたり 取得可能", dl.get_move("たいあたり") is not None)
_mv_たいあたり = dl.get_move("たいあたり")
if _mv_たいあたり:
    _pa_たいあたり = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_たいあたり = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_たいあたり = dmg(_pa_たいあたり, _pd_たいあたり, "たいあたり")
    check("ダメージ計算: たいあたり", _d_たいあたり > 0, f"dmg={_d_たいあたり}")

# ── りゅうのいぶき ──
check("DB: りゅうのいぶき 取得可能", dl.get_move("りゅうのいぶき") is not None)
_mv_りゅうのいぶき = dl.get_move("りゅうのいぶき")
if _mv_りゅうのいぶき:
    _pa_りゅうのいぶき = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_りゅうのいぶき = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_りゅうのいぶき = dmg(_pa_りゅうのいぶき, _pd_りゅうのいぶき, "りゅうのいぶき")
    check("ダメージ計算: りゅうのいぶき", _d_りゅうのいぶき > 0, f"dmg={_d_りゅうのいぶき}")
# りゅうのいぶき: まひ30%
_mv_s_りゅうのいぶき = dl.get_move("りゅうのいぶき")
if _mv_s_りゅうのいぶき:
    random.seed(0); _hit_りゅうのいぶき = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ドラゴン", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ドラゴン", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "りゅうのいぶき")
        _hit_りゅうのいぶき += int((_pd2.status == "paralysis"))
    check("追加効果(まひ30%): りゅうのいぶき", 27 <= _hit_りゅうのいぶき <= 168, f"count={_hit_りゅうのいぶき}/300")
    random.seed(1); _immok_りゅうのいぶき = True
    for _ in range(60):
        _pai = make_poke(type1="ドラゴン", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "りゅうのいぶき")
        if _pdi.status == "paralysis": _immok_りゅうのいぶき = False; break
    check("まひ免疫(でんき型には無効): りゅうのいぶき", _immok_りゅうのいぶき, "免疫タイプに状態異常が付与されないこと")

# ── スラッシュ ──
check("DB: スラッシュ 取得可能", dl.get_move("スラッシュ") is not None)
_mv_スラッシュ = dl.get_move("スラッシュ")
if _mv_スラッシュ:
    _pa_スラッシュ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_スラッシュ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_スラッシュ = dmg(_pa_スラッシュ, _pd_スラッシュ, "スラッシュ")
    check("ダメージ計算: スラッシュ", _d_スラッシュ > 0, f"dmg={_d_スラッシュ}")
# スラッシュ: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_スラッシュ
random.seed(0); _hc_crit_スラッシュ = 0; _phc = make_poke(type1="ノーマル")
_mvhc_スラッシュ = dl.get_move("スラッシュ")
for _ in range(800):
    if _cc_スラッシュ(_phc, _mvhc_スラッシュ, make_poke(type1="ノーマル")): _hc_crit_スラッシュ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: スラッシュ", 60 <= _hc_crit_スラッシュ <= 150, f"crit={_hc_crit_スラッシュ}/800 (期待≈100, 通常1/24なら≈33)")

# ── にほんばれ ──
check("DB: にほんばれ 取得可能", dl.get_move("にほんばれ") is not None)
# にほんばれ: 天候sunny
_mv_w_にほんばれ = dl.get_move("にほんばれ")
if _mv_w_にほんばれ:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="ほのお"), make_poke(), "にほんばれ")
    check("天候sunny: にほんばれ", _fw.weather == "sunny", f"weather={_fw.weather}")

# ── あられ ──
check("DB: あられ 取得可能", dl.get_move("あられ") is not None)
# あられ: 天候hail
_mv_w_あられ = dl.get_move("あられ")
if _mv_w_あられ:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="こおり"), make_poke(), "あられ")
    check("天候hail: あられ", _fw.weather == "hail", f"weather={_fw.weather}")

# ── すなあらし ──
check("DB: すなあらし 取得可能", dl.get_move("すなあらし") is not None)
# すなあらし: 天候sandstorm
_mv_w_すなあらし = dl.get_move("すなあらし")
if _mv_w_すなあらし:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="いわ"), make_poke(), "すなあらし")
    check("天候sandstorm: すなあらし", _fw.weather == "sandstorm", f"weather={_fw.weather}")

# ── 10まんばりき ──
check("DB: 10まんばりき 取得可能", dl.get_move("10まんばりき") is not None)
_mv_10まんばりき = dl.get_move("10まんばりき")
if _mv_10まんばりき:
    _pa_10まんばりき = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_10まんばりき = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_10まんばりき = dmg(_pa_10まんばりき, _pd_10まんばりき, "10まんばりき")
    check("ダメージ計算: 10まんばりき", _d_10まんばりき > 0, f"dmg={_d_10まんばりき}")

# ── アームハンマー ──
check("DB: アームハンマー 取得可能", dl.get_move("アームハンマー") is not None)
_mv_ア_ムハンマ_ = dl.get_move("アームハンマー")
if _mv_ア_ムハンマ_:
    _pa_ア_ムハンマ_ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ア_ムハンマ_ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ア_ムハンマ_ = dmg(_pa_ア_ムハンマ_, _pd_ア_ムハンマ_, "アームハンマー")
    check("ダメージ計算: アームハンマー", _d_ア_ムハンマ_ > 0, f"dmg={_d_ア_ムハンマ_}")
# アームハンマー: 自分素早さ-1
_mvss_ア_ムハンマ__speed = dl.get_move("アームハンマー")
if _mvss_ア_ムハンマ__speed:
    random.seed(0); _got_ア_ムハンマ__speed = 0
    for _ in range(60):
        _pas = make_poke(type1="かくとう", atk_b=60, spatk_b=60); _pds = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "アームハンマー")
        if _pas.stage_speed != 0: _got_ア_ムハンマ__speed = _pas.stage_speed; break
    check("自分素早さ-1: アームハンマー", _got_ア_ムハンマ__speed == -1, f"1回適用={_got_ア_ムハンマ__speed} 期待=-1")
# アームハンマー: 自分の能力下降（命中までリトライ）
random.seed(0); _psd = None
for _ in range(20):
    _psd = make_poke(type1="かくとう", atk_b=120, spatk_b=120); _dsd = make_poke(type1="ノーマル", hp_b=255, def_b=80, spdef_b=80)
    execute(_psd, _dsd, "アームハンマー")
    if _psd.stage_speed < 0: break
check("自分素早さ下降: アームハンマー", _psd.stage_speed < 0, f"stage={_psd.stage_speed}")

# ── アイアンローラー ──
check("DB: アイアンローラー 取得可能", dl.get_move("アイアンローラー") is not None)
_mv_アイアンロ_ラ_ = dl.get_move("アイアンローラー")
if _mv_アイアンロ_ラ_:
    _pa_アイアンロ_ラ_ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_アイアンロ_ラ_ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_アイアンロ_ラ_ = dmg(_pa_アイアンロ_ラ_, _pd_アイアンロ_ラ_, "アイアンローラー")
    check("ダメージ計算: アイアンローラー", _d_アイアンロ_ラ_ > 0, f"dmg={_d_アイアンロ_ラ_}")
# アイアンローラー: フィールド無しは失敗、有りで成功&フィールド解除
_pir = make_poke(type1="はがね", atk_b=120); _dir = make_poke(type1="フェアリー", hp_b=255, def_b=120)
_f_no = BattleField(); _hpi1 = _dir.hp; execute(_pir, _dir, "アイアンローラー", _f_no)
check("フィールド無し失敗: アイアンローラー", _dir.hp == _hpi1, f"hp={_dir.hp}/{_hpi1}")
_pir2 = make_poke(type1="はがね", atk_b=120); _dir2 = make_poke(type1="フェアリー", hp_b=255, def_b=120)
_f_g = BattleField(); _f_g.grassy_terrain = True; _hpi2 = _dir2.hp; execute(_pir2, _dir2, "アイアンローラー", _f_g)
check("フィールド解除(成功時): アイアンローラー", _dir2.hp < _hpi2 and not _f_g.grassy_terrain, f"hp={_dir2.hp}/{_hpi2} field={_f_g.grassy_terrain}")

# ── かかとおとし ──
check("DB: かかとおとし 取得可能", dl.get_move("かかとおとし") is not None)
_mv_かかとおとし = dl.get_move("かかとおとし")
if _mv_かかとおとし:
    _pa_かかとおとし = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_かかとおとし = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_かかとおとし = dmg(_pa_かかとおとし, _pd_かかとおとし, "かかとおとし")
    check("ダメージ計算: かかとおとし", _d_かかとおとし > 0, f"dmg={_d_かかとおとし}")
# かかとおとし: こんらん30%
_mv_s_かかとおとし = dl.get_move("かかとおとし")
if _mv_s_かかとおとし:
    random.seed(0); _hit_かかとおとし = 0
    for _ in range(300):
        _pa2 = make_poke(type1="かくとう", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "かかとおとし")
        _hit_かかとおとし += int(_pd2.confused)
    check("追加効果(こんらん30%): かかとおとし", 27 <= _hit_かかとおとし <= 168, f"count={_hit_かかとおとし}/300")
# かかとおとし: 外れ時1/2自傷
_mv_mr_かかとおとし = dl.get_move("かかとおとし")
if _mv_mr_かかとおとし:
    _pa_mr = make_poke(type1="かくとう", atk_b=100)
    import copy as _cp; _mv_miss = _cp.copy(_mv_mr_かかとおとし); _mv_miss.accuracy = 1
    random.seed(99); _s1m = BattleSide([_pa_mr]); _s2m = BattleSide([make_poke()])
    _execute_move(_s1m, _s2m, Action(type="move", move=_mv_miss), BattleField())
    check("外れ時1/2自傷: かかとおとし", _pa_mr.max_hp - _pa_mr.hp == max(1, _pa_mr.max_hp//2), f"dmg={_pa_mr.max_hp - _pa_mr.hp}")

# ── きあいパンチ ──
check("DB: きあいパンチ 取得可能", dl.get_move("きあいパンチ") is not None)
_mv_きあいパンチ = dl.get_move("きあいパンチ")
if _mv_きあいパンチ:
    _pa_きあいパンチ = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_きあいパンチ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_きあいパンチ = dmg(_pa_きあいパンチ, _pd_きあいパンチ, "きあいパンチ")
    check("ダメージ計算: きあいパンチ", _d_きあいパンチ > 0, f"dmg={_d_きあいパンチ}")
# きあいパンチ: 優先度-3
_mv_pr_きあいパンチ = dl.get_move("きあいパンチ")
if _mv_pr_きあいパンチ and _mv_pr_きあいパンチ.priority == -3:
    check("優先度-3: きあいパンチ", _mv_pr_きあいパンチ.priority == -3)
elif _mv_pr_きあいパンチ:
    check("優先度-3: きあいパンチ", _mv_pr_きあいパンチ.priority == -3, f"DB優先度={_mv_pr_きあいパンチ.priority} 仕様=-3")
# きあいパンチ: 行動前に技ダメージを受けると失敗（-3で後攻）
from simulator.battle import Battle as _Bfp
_pfp = make_poke(type1="かくとう", atk_b=150, hp_b=255, def_b=255, moves=["きあいパンチ"])
_ffp = make_poke(type1="ノーマル", atk_b=80, hp_b=255, def_b=255, moves=["のしかかり"])
_act_fp = lambda s,o,f: Action(type="move", move=dl.get_move("きあいパンチ"), move_idx=0)
_act_hit = lambda s,o,f: Action(type="move", move=dl.get_move("のしかかり"), move_idx=0)
_hp_ffp = _ffp.hp
_bfp = _Bfp(BattleSide([_pfp]), BattleSide([_ffp]))
import simulator.battle as _SB; _SBmax = _SB.MAX_TURNS; _SB.MAX_TURNS = 1; _bfp.run(_act_fp, _act_hit); _SB.MAX_TURNS = _SBmax
check("被弾失敗: きあいパンチ", _ffp.hp == _hp_ffp, f"foeHP={_ffp.hp}/{_hp_ffp}（被弾後きあいパンチ不発なら相手無傷）")

# ── クロスポイズン ──
check("DB: クロスポイズン 取得可能", dl.get_move("クロスポイズン") is not None)
_mv_クロスポイズン = dl.get_move("クロスポイズン")
if _mv_クロスポイズン:
    _pa_クロスポイズン = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_クロスポイズン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_クロスポイズン = dmg(_pa_クロスポイズン, _pd_クロスポイズン, "クロスポイズン")
    check("ダメージ計算: クロスポイズン", _d_クロスポイズン > 0, f"dmg={_d_クロスポイズン}")
# クロスポイズン: どく10%
_mv_s_クロスポイズン = dl.get_move("クロスポイズン")
if _mv_s_クロスポイズン:
    random.seed(0); _hit_クロスポイズン = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "クロスポイズン")
        _hit_クロスポイズン += int((_pd2.status == "poison"))
    check("追加効果(どく10%): クロスポイズン", 9 <= _hit_クロスポイズン <= 66, f"count={_hit_クロスポイズン}/300")
    random.seed(1); _immok_クロスポイズン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "クロスポイズン")
        if _pdi.status == "poison": _immok_クロスポイズン = False; break
    check("どく免疫(どく型には無効): クロスポイズン", _immok_クロスポイズン, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_クロスポイズン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "クロスポイズン")
        if _pdi.status == "poison": _immok_クロスポイズン = False; break
    check("どく免疫(はがね型には無効): クロスポイズン", _immok_クロスポイズン, "免疫タイプに状態異常が付与されないこと")
# クロスポイズン: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_クロスポイズン
random.seed(0); _hc_crit_クロスポイズン = 0; _phc = make_poke(type1="どく")
_mvhc_クロスポイズン = dl.get_move("クロスポイズン")
for _ in range(800):
    if _cc_クロスポイズン(_phc, _mvhc_クロスポイズン, make_poke(type1="くさ")): _hc_crit_クロスポイズン += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: クロスポイズン", 60 <= _hc_crit_クロスポイズン <= 150, f"crit={_hc_crit_クロスポイズン}/800 (期待≈100, 通常1/24なら≈33)")

# ── グラススライダー ──
check("DB: グラススライダー 取得可能", dl.get_move("グラススライダー") is not None)
_mv_グラススライダ_ = dl.get_move("グラススライダー")
if _mv_グラススライダ_:
    _pa_グラススライダ_ = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_グラススライダ_ = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_グラススライダ_ = dmg(_pa_グラススライダ_, _pd_グラススライダ_, "グラススライダー")
    check("ダメージ計算: グラススライダー", _d_グラススライダ_ > 0, f"dmg={_d_グラススライダ_}")
# グラススライダー: グラスフィールド時に優先度+1
_pgs = make_poke(type1="くさ"); _ags = Action(type="move", move=dl.get_move("グラススライダー"))
_fgs0 = BattleField(); _fgs1 = BattleField(); _fgs1.grassy_terrain = True
_pr0 = _priority(_ags, _pgs, _fgs0); _pr1 = _priority(_ags, _pgs, _fgs1)
check("グラスF優先度+1: グラススライダー", _pr1 == _pr0 + 1, f"off={_pr0} on={_pr1}")
check("非グラスFでは通常優先度: グラススライダー", _pr0 == dl.get_move("グラススライダー").priority, f"off={_pr0} db={dl.get_move('グラススライダー').priority}")

# ── しめつける ──
check("DB: しめつける 取得可能", dl.get_move("しめつける") is not None)
_mv_しめつける = dl.get_move("しめつける")
if _mv_しめつける:
    _pa_しめつける = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_しめつける = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_しめつける = dmg(_pa_しめつける, _pd_しめつける, "しめつける")
    check("ダメージ計算: しめつける", _d_しめつける > 0, f"dmg={_d_しめつける}")
# しめつける: バインド
_mv_bd_しめつける = dl.get_move("しめつける")
if _mv_bd_しめつける:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="ノーマル", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="ノーマル", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "しめつける")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: しめつける", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── じさくづき ──
check("DB: じさくづき 取得可能", dl.get_move("じさくづき") is not None)
_mv_じさくづき = dl.get_move("じさくづき")
if _mv_じさくづき:
    _pa_じさくづき = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_じさくづき = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_じさくづき = dmg(_pa_じさくづき, _pd_じさくづき, "じさくづき")
    check("ダメージ計算: じさくづき", _d_じさくづき > 0, f"dmg={_d_じさくづき}")

# ── じたばた ──
check("DB: じたばた 取得可能", dl.get_move("じたばた") is not None)
# じたばた: HP比別の威力テーブル（>67.7%→20 ... ≤3.1%→200）
_ph = make_poke(type1="ノーマル", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="ノーマル")
_ks_ng = []
for _r, _exp in [(0.80,20),(0.50,40),(0.30,80),(0.15,100),(0.05,150),(0.01,200)]:
    _ph.hp = max(1, int(_ph.max_hp * _r))
    _got = _ep(_ph, _dd, dl.get_move("じたばた"), BattleField())
    if _got != _exp: _ks_ng.append(f"r={_r}:{_got}!={_exp}")
check("HP比別威力テーブル: じたばた", not _ks_ng, f"NG={_ks_ng}")

# ── シャドーパンチ ──
check("DB: シャドーパンチ 取得可能", dl.get_move("シャドーパンチ") is not None)
_mv_シャド_パンチ = dl.get_move("シャドーパンチ")
if _mv_シャド_パンチ:
    _pa_シャド_パンチ = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_シャド_パンチ = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_シャド_パンチ = dmg(_pa_シャド_パンチ, _pd_シャド_パンチ, "シャドーパンチ")
    check("ダメージ計算: シャドーパンチ", _d_シャド_パンチ > 0, f"dmg={_d_シャド_パンチ}")
# シャドーパンチ: 必中
_mvmust_シャド_パンチ = dl.get_move("シャドーパンチ")
if _mvmust_シャド_パンチ:
    random.seed(0); _hit_all_シャド_パンチ = True
    for _ in range(30):
        _pah = make_poke(type1="ゴースト", atk_b=100, spatk_b=100); _pdh = make_poke(type1="エスパー", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "シャドーパンチ")
        if _pdh.hp == _hpb: _hit_all_シャド_パンチ = False; break
    check("必中: シャドーパンチ", _hit_all_シャド_パンチ)

# ── スイープビンタ ──
check("DB: スイープビンタ 取得可能", dl.get_move("スイープビンタ") is not None)
_mv_スイ_プビンタ = dl.get_move("スイープビンタ")
if _mv_スイ_プビンタ:
    _pa_スイ_プビンタ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_スイ_プビンタ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_スイ_プビンタ = dmg(_pa_スイ_プビンタ, _pd_スイ_プビンタ, "スイープビンタ")
    check("ダメージ計算: スイープビンタ", _d_スイ_プビンタ > 0, f"dmg={_d_スイ_プビンタ}")
# スイープビンタ: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_スイ_プビンタ = dl.get_move("スイープビンタ")
if _mvmh_スイ_プビンタ:
    _pam = make_poke(type1="ノーマル", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_スイ_プビンタ = calc_damage(_pam, make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200), _mvmh_スイ_プビンタ, BattleField(), random_roll=1.0)
    random.seed(0); _multi_スイ_プビンタ = 0
    for _ in range(20):
        _pdm = make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "スイープビンタ"); _multi_スイ_プビンタ = _pdm.max_hp - _pdm.hp
        if _multi_スイ_プビンタ > _single_スイ_プビンタ: break
    check("多段ヒット発生(複数回): スイープビンタ", _multi_スイ_プビンタ > _single_スイ_プビンタ, f"single={_single_スイ_プビンタ} multi={_multi_スイ_プビンタ}")

# ── スマートホーン ──
check("DB: スマートホーン 取得可能", dl.get_move("スマートホーン") is not None)
_mv_スマ_トホ_ン = dl.get_move("スマートホーン")
if _mv_スマ_トホ_ン:
    _pa_スマ_トホ_ン = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_スマ_トホ_ン = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_スマ_トホ_ン = dmg(_pa_スマ_トホ_ン, _pd_スマ_トホ_ン, "スマートホーン")
    check("ダメージ計算: スマートホーン", _d_スマ_トホ_ン > 0, f"dmg={_d_スマ_トホ_ン}")
# スマートホーン: 必中
_mvmust_スマ_トホ_ン = dl.get_move("スマートホーン")
if _mvmust_スマ_トホ_ン:
    random.seed(0); _hit_all_スマ_トホ_ン = True
    for _ in range(30):
        _pah = make_poke(type1="はがね", atk_b=100, spatk_b=100); _pdh = make_poke(type1="こおり", hp_b=255, def_b=100, spdef_b=100)
        _hpb = _pdh.hp; execute(_pah, _pdh, "スマートホーン")
        if _pdh.hp == _hpb: _hit_all_スマ_トホ_ン = False; break
    check("必中: スマートホーン", _hit_all_スマ_トホ_ン)

# ── そらをとぶ ──
check("DB: そらをとぶ 取得可能", dl.get_move("そらをとぶ") is not None)
_mv_そらをとぶ = dl.get_move("そらをとぶ")
if _mv_そらをとぶ:
    _pa_そらをとぶ = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_そらをとぶ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_そらをとぶ = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_そらをとぶ = make_poke(type1="くさ", def_b=100, spdef_b=100)
        execute(_pa_そらをとぶ, _pd_そらをとぶ, "そらをとぶ"); execute(_pa_そらをとぶ, _pd_そらをとぶ, "そらをとぶ")
        if _pd_そらをとぶ.hp < _pd_そらをとぶ.max_hp: break
    check("ダメージ計算: そらをとぶ", _pd_そらをとぶ.hp < _pd_そらをとぶ.max_hp, f"hp={_pd_そらをとぶ.hp}")
# そらをとぶ: 2ターン溜め
_mv_2t_そらをとぶ = dl.get_move("そらをとぶ")
if _mv_2t_そらをとぶ:
    _pa_2t = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "そらをとぶ")
    check("2ターン溜め(1T)ダメなし: そらをとぶ", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: そらをとぶ", _pa_2t.charging_move == "そらをとぶ")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "そらをとぶ")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "そらをとぶ")
    check("2ターン溜め(2T)ダメあり: そらをとぶ", _pd_2t.hp < _hp_before_2t)

# ── ちきゅうなげ ──
check("DB: ちきゅうなげ 取得可能", dl.get_move("ちきゅうなげ") is not None)
# ちきゅうなげ: 固定50ダメージ
_mvfx_ちきゅうなげ = dl.get_move("ちきゅうなげ")
if _mvfx_ちきゅうなげ:
    _paf = make_poke(type1="かくとう", atk_b=100, spatk_b=100); _pdf = make_poke(type1="ノーマル", hp_b=200, def_b=100, spdef_b=100)
    _hpbf = _pdf.hp; execute(_paf, _pdf, "ちきゅうなげ")
    check("固定50ダメージ: ちきゅうなげ", _hpbf - _pdf.hp == 50, f"dmg={_hpbf - _pdf.hp}")

# ── ついばむ ──
check("DB: ついばむ 取得可能", dl.get_move("ついばむ") is not None)
_mv_ついばむ = dl.get_move("ついばむ")
if _mv_ついばむ:
    _pa_ついばむ = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ついばむ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ついばむ = dmg(_pa_ついばむ, _pd_ついばむ, "ついばむ")
    check("ダメージ計算: ついばむ", _d_ついばむ > 0, f"dmg={_d_ついばむ}")
# ついばむ: 相手のきのみを食べ効果を得る（オボンのみで自分回復）
_ppk = make_poke(type1="ひこう", atk_b=80); _ppk.hp = _ppk.max_hp // 2
_dpk = make_poke(type1="くさ", hp_b=255, def_b=200, item="オボンのみ")
_hp_ppk = _ppk.hp; execute(_ppk, _dpk, "ついばむ")
check("きのみ奪取: ついばむ", _dpk.item is None and _ppk.hp > _hp_ppk, f"foeItem={_dpk.item} hp={_ppk.hp}/{_hp_ppk}")
# effect_textに無い余計な追加効果がないこと（きのみ無しの相手に能力変化等が起きない）
_dpk2 = make_poke(type1="くさ", hp_b=255, def_b=200); _rng_noextra = 0
import random as _rnx; _rnx.seed(0)
for _ in range(30): execute(make_poke(type1="ひこう", atk_b=10), _dpk2, "ついばむ")
_stg2 = [getattr(_dpk2, _s, 0) for _s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed")]
check("余計な追加効果なし: ついばむ", all(_v == 0 for _v in _stg2) and _dpk2.status is None, f"stages={_stg2} status={_dpk2.status}")

# ── とっておき ──
check("DB: とっておき 取得可能", dl.get_move("とっておき") is not None)
_mv_とっておき = dl.get_move("とっておき")
if _mv_とっておき:
    _pa_とっておき = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_とっておき = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_とっておき = dmg(_pa_とっておき, _pd_とっておき, "とっておき")
    check("ダメージ計算: とっておき", _d_とっておき > 0, f"dmg={_d_とっておき}")
# とっておき: 他の技を全て使うまで失敗、使い切れば成功
_ptf = make_poke(type1="ノーマル", atk_b=120, moves=["とっておき","たいあたり"]); _dtf = make_poke(type1="ノーマル", hp_b=255, def_b=200)
_hpt1 = _dtf.hp; execute(_ptf, _dtf, "とっておき")
check("他技未使用で失敗: とっておき", _dtf.hp == _hpt1, f"hp={_dtf.hp}/{_hpt1}")
_ptf.used_moves.add("たいあたり"); _hpt2 = _dtf.hp; execute(_ptf, _dtf, "とっておき")
check("他技使用後に成功: とっておき", _dtf.hp < _hpt2, f"hp={_dtf.hp}/{_hpt2}")

# ── どくどくのキバ ──
check("DB: どくどくのキバ 取得可能", dl.get_move("どくどくのキバ") is not None)
_mv_どくどくのキバ = dl.get_move("どくどくのキバ")
if _mv_どくどくのキバ:
    _pa_どくどくのキバ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_どくどくのキバ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_どくどくのキバ = dmg(_pa_どくどくのキバ, _pd_どくどくのキバ, "どくどくのキバ")
    check("ダメージ計算: どくどくのキバ", _d_どくどくのキバ > 0, f"dmg={_d_どくどくのキバ}")
# どくどくのキバ: もうどく50%
_mv_s_どくどくのキバ = dl.get_move("どくどくのキバ")
if _mv_s_どくどくのキバ:
    random.seed(0); _hit_どくどくのキバ = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "どくどくのキバ")
        _hit_どくどくのキバ += int((_pd2.status == "badpoison"))
    check("追加効果(もうどく50%): どくどくのキバ", 45 <= _hit_どくどくのキバ <= 270, f"count={_hit_どくどくのキバ}/300")
    random.seed(1); _immok_どくどくのキバ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくどくのキバ")
        if _pdi.status == "badpoison": _immok_どくどくのキバ = False; break
    check("もうどく免疫(どく型には無効): どくどくのキバ", _immok_どくどくのキバ, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_どくどくのキバ = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくどくのキバ")
        if _pdi.status == "badpoison": _immok_どくどくのキバ = False; break
    check("もうどく免疫(はがね型には無効): どくどくのキバ", _immok_どくどくのキバ, "免疫タイプに状態異常が付与されないこと")

# ── ダイビング ──
check("DB: ダイビング 取得可能", dl.get_move("ダイビング") is not None)
_mv_ダイビング = dl.get_move("ダイビング")
if _mv_ダイビング:
    _pa_ダイビング = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ダイビング = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_ダイビング = make_poke(type1="みず", atk_b=100, spatk_b=100); _pd_ダイビング = make_poke(type1="ほのお", def_b=100, spdef_b=100)
        execute(_pa_ダイビング, _pd_ダイビング, "ダイビング"); execute(_pa_ダイビング, _pd_ダイビング, "ダイビング")
        if _pd_ダイビング.hp < _pd_ダイビング.max_hp: break
    check("ダメージ計算: ダイビング", _pd_ダイビング.hp < _pd_ダイビング.max_hp, f"hp={_pd_ダイビング.hp}")
# ダイビング: 2ターン溜め
_mv_2t_ダイビング = dl.get_move("ダイビング")
if _mv_2t_ダイビング:
    _pa_2t = make_poke(type1="みず", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "ダイビング")
    check("2ターン溜め(1T)ダメなし: ダイビング", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: ダイビング", _pa_2t.charging_move == "ダイビング")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "ダイビング")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "ダイビング")
    check("2ターン溜め(2T)ダメあり: ダイビング", _pd_2t.hp < _hp_before_2t)

# ── ダブルアタック ──
check("DB: ダブルアタック 取得可能", dl.get_move("ダブルアタック") is not None)
_mv_ダブルアタック = dl.get_move("ダブルアタック")
if _mv_ダブルアタック:
    _pa_ダブルアタック = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ダブルアタック = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ダブルアタック = dmg(_pa_ダブルアタック, _pd_ダブルアタック, "ダブルアタック")
    check("ダメージ計算: ダブルアタック", _d_ダブルアタック > 0, f"dmg={_d_ダブルアタック}")
# ダブルアタック: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ダブルアタック = dl.get_move("ダブルアタック")
if _mvmh_ダブルアタック:
    _pam = make_poke(type1="ノーマル", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ダブルアタック = calc_damage(_pam, make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200), _mvmh_ダブルアタック, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ダブルアタック = 0
    for _ in range(20):
        _pdm = make_poke(type1="ノーマル", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ダブルアタック"); _multi_ダブルアタック = _pdm.max_hp - _pdm.hp
        if _multi_ダブルアタック > _single_ダブルアタック: break
    check("多段ヒット発生(複数回): ダブルアタック", _multi_ダブルアタック > _single_ダブルアタック, f"single={_single_ダブルアタック} multi={_multi_ダブルアタック}")

# ── はがねのつばさ ──
check("DB: はがねのつばさ 取得可能", dl.get_move("はがねのつばさ") is not None)
_mv_はがねのつばさ = dl.get_move("はがねのつばさ")
if _mv_はがねのつばさ:
    _pa_はがねのつばさ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_はがねのつばさ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_はがねのつばさ = dmg(_pa_はがねのつばさ, _pd_はがねのつばさ, "はがねのつばさ")
    check("ダメージ計算: はがねのつばさ", _d_はがねのつばさ > 0, f"dmg={_d_はがねのつばさ}")
# はがねのつばさ: 確率自己防御+1(10%)
_mvpb_はがねのつばさ = dl.get_move("はがねのつばさ")
if _mvpb_はがねのつばさ:
    random.seed(0); _pb_ok_はがねのつばさ = False
    for _ in range(200):
        _papb = make_poke(type1="はがね", atk_b=40, spatk_b=40); _pdpb = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_papb, _pdpb, "はがねのつばさ")
        if _papb.stage_defense > 0: _pb_ok_はがねのつばさ = _papb.stage_defense; break
    check("確率自己防御+1: はがねのつばさ", _pb_ok_はがねのつばさ == 1, f"1回適用={_pb_ok_はがねのつばさ} 期待=+1")

# ── はたく ──
check("DB: はたく 取得可能", dl.get_move("はたく") is not None)
_mv_はたく = dl.get_move("はたく")
if _mv_はたく:
    _pa_はたく = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_はたく = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_はたく = dmg(_pa_はたく, _pd_はたく, "はたく")
    check("ダメージ計算: はたく", _d_はたく > 0, f"dmg={_d_はたく}")

# ── はなびらのまい ──
check("DB: はなびらのまい 取得可能", dl.get_move("はなびらのまい") is not None)
_mv_はなびらのまい = dl.get_move("はなびらのまい")
if _mv_はなびらのまい:
    _pa_はなびらのまい = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_はなびらのまい = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_はなびらのまい = dmg(_pa_はなびらのまい, _pd_はなびらのまい, "はなびらのまい")
    check("ダメージ計算: はなびらのまい", _d_はなびらのまい > 0, f"dmg={_d_はなびらのまい}")
# はなびらのまい: あばれ状態
_mv_rg_はなびらのまい = dl.get_move("はなびらのまい")
if _mv_rg_はなびらのまい:
    _pa_rg = make_poke(type1="くさ", atk_b=30, spatk_b=30); _pd_rg = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
    execute(_pa_rg, _pd_rg, "はなびらのまい")
    check("あばれ状態: はなびらのまい", _pa_rg.locked_move == "はなびらのまい")

# ── ハードプレス ──
check("DB: ハードプレス 取得可能", dl.get_move("ハードプレス") is not None)
# ハードプレス: 威力=max(1,floor(100×相手現HP/最大HP))。具体値を検証
_php = make_poke(atk_b=100); _dhp = make_poke(hp_b=200, def_b=100)
import math as _mhp; _hp_ng = []
for _r in [1.0, 0.5, 0.25]:
    _dhp.hp = max(1, int(_dhp.max_hp * _r)); _exp = max(1, _mhp.floor(100 * _dhp.hp / _dhp.max_hp))
    _got = _ep(_php, _dhp, dl.get_move("ハードプレス"), BattleField())
    if _got != _exp: _hp_ng.append(f"r={_r}:{_got}!={_exp}")
check("相手HP比威力(100×HP/max): ハードプレス", not _hp_ng, f"NG={_hp_ng}")

# ── ほしがる ──
check("DB: ほしがる 取得可能", dl.get_move("ほしがる") is not None)
_mv_ほしがる = dl.get_move("ほしがる")
if _mv_ほしがる:
    _pa_ほしがる = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ほしがる = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ほしがる = dmg(_pa_ほしがる, _pd_ほしがる, "ほしがる")
    check("ダメージ計算: ほしがる", _d_ほしがる > 0, f"dmg={_d_ほしがる}")
# ほしがる: 道具奪取
_pst = make_poke(type1="あく", atk_b=120); _pst.item = None
_dst = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst.item = "オボンのみ"
execute(_pst, _dst, "ほしがる")
check("道具奪取: ほしがる", _pst.item == "オボンのみ" and _dst.item is None)
# negative: 自分が道具を持っている場合は奪わない
_pst2 = make_poke(type1="あく", atk_b=120); _pst2.item = "オボンのみ"
_dst2 = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst2.item = "たべのこし"
execute(_pst2, _dst2, "ほしがる")
check("自分が道具持ちなら奪わない: ほしがる", _pst2.item == "オボンのみ" and _dst2.item == "たべのこし", f"atk={_pst2.item} def={_dst2.item}")

# ── ほのおのムチ ──
check("DB: ほのおのムチ 取得可能", dl.get_move("ほのおのムチ") is not None)
_mv_ほのおのムチ = dl.get_move("ほのおのムチ")
if _mv_ほのおのムチ:
    _pa_ほのおのムチ = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_ほのおのムチ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ほのおのムチ = dmg(_pa_ほのおのムチ, _pd_ほのおのムチ, "ほのおのムチ")
    check("ダメージ計算: ほのおのムチ", _d_ほのおのムチ > 0, f"dmg={_d_ほのおのムチ}")
# ほのおのムチ: 相手防御-1
_mv_dd_ほのおのムチ = dl.get_move("ほのおのムチ")
if _mv_dd_ほのおのムチ:
    _pa_dd = make_poke(type1="ほのお", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ほのおのムチ = 0; _dd_ok_ほのおのムチ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ほのおのムチ")
        if _pd_dd.stage_defense != 0: _dd_val_ほのおのムチ = _pd_dd.stage_defense; _dd_ok_ほのおのムチ = True; break
    check("相手防御-1: ほのおのムチ", _dd_ok_ほのおのムチ and _dd_val_ほのおのムチ == -1, f"1回適用={_dd_val_ほのおのムチ} 期待=-1")

# ── フライングプレス ──
check("DB: フライングプレス 取得可能", dl.get_move("フライングプレス") is not None)
_mv_フライングプレス = dl.get_move("フライングプレス")
if _mv_フライングプレス:
    _pa_フライングプレス = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_フライングプレス = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_フライングプレス = dmg(_pa_フライングプレス, _pd_フライングプレス, "フライングプレス")
    check("ダメージ計算: フライングプレス", _d_フライングプレス > 0, f"dmg={_d_フライングプレス}")
# フライングプレス: かくとう×ひこうの複合相性（両タイプの相性を掛け合わせる）
_pfp = make_poke(type1="かくとう", atk_b=120)
from simulator.data import get_type_effectiveness as _gte
from simulator.damage import _effective_move_type as _emtfp
_fp_base = calc_damage(_pfp, make_poke(type1="ノーマル",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)
_fp_bug = calc_damage(_pfp, make_poke(type1="むし",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)
_fp_fairy = calc_damage(_pfp, make_poke(type1="フェアリー",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)
_fp_ghost = calc_damage(_pfp, make_poke(type1="ゴースト",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)
# vsノーマル: かくとう2×ひこう1=2× / vsむし: かくとう0.5×ひこう2=1× → 等しい
check("複合相性(むし=ノーマル等倍): フライングプレス", abs(_fp_bug - _fp_base/_gte("かくとう","ノーマル",None)) <= 2, f"bug={_fp_bug} expected≈{_fp_base/_gte(chr(12363)+chr(12367)+chr(12392)+chr(12358),chr(12494)+chr(12540)+chr(12510)+chr(12523),None):.0f}")
# vsゴースト: かくとう0×ひこう1=0（無効）
check("複合相性(ゴースト無効): フライングプレス", _fp_ghost == 0, f"ghost={_fp_ghost}")
# ちいさくなる状態の相手に威力2倍
_fpm0 = make_poke(type1="ノーマル", def_b=100); _fpm1 = make_poke(type1="ノーマル", def_b=100); _fpm1.minimized = True
_fp_n = _ep(_pfp, _fpm0, dl.get_move("フライングプレス"), BattleField()); _fp_m = _ep(_pfp, _fpm1, dl.get_move("フライングプレス"), BattleField())
check("ちいさくなる2倍: フライングプレス", _fp_m == _fp_n * 2, f"normal={_fp_n} mini={_fp_m}")

# ── ブレイククロー ──
check("DB: ブレイククロー 取得可能", dl.get_move("ブレイククロー") is not None)
_mv_ブレイククロ_ = dl.get_move("ブレイククロー")
if _mv_ブレイククロ_:
    _pa_ブレイククロ_ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_ブレイククロ_ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ブレイククロ_ = dmg(_pa_ブレイククロ_, _pd_ブレイククロ_, "ブレイククロー")
    check("ダメージ計算: ブレイククロー", _d_ブレイククロ_ > 0, f"dmg={_d_ブレイククロ_}")
# ブレイククロー: 相手防御-1
_mv_dd_ブレイククロ_ = dl.get_move("ブレイククロー")
if _mv_dd_ブレイククロ_:
    _pa_dd = make_poke(type1="ノーマル", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ブレイククロ_ = 0; _dd_ok_ブレイククロ_ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ブレイククロー")
        if _pd_dd.stage_defense != 0: _dd_val_ブレイククロ_ = _pd_dd.stage_defense; _dd_ok_ブレイククロ_ = True; break
    check("相手防御-1: ブレイククロー", _dd_ok_ブレイククロ_ and _dd_val_ブレイククロ_ == -1, f"1回適用={_dd_val_ブレイククロ_} 期待=-1")

# ── ローキック ──
check("DB: ローキック 取得可能", dl.get_move("ローキック") is not None)
_mv_ロ_キック = dl.get_move("ローキック")
if _mv_ロ_キック:
    _pa_ロ_キック = make_poke(type1="かくとう", atk_b=100, spatk_b=100)
    _pd_ロ_キック = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_ロ_キック = dmg(_pa_ロ_キック, _pd_ロ_キック, "ローキック")
    check("ダメージ計算: ローキック", _d_ロ_キック > 0, f"dmg={_d_ロ_キック}")
# ローキック: 相手素早さ-1
_mv_dd_ロ_キック = dl.get_move("ローキック")
if _mv_dd_ロ_キック:
    _pa_dd = make_poke(type1="かくとう", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ロ_キック = 0; _dd_ok_ロ_キック = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ローキック")
        if _pd_dd.stage_speed != 0: _dd_val_ロ_キック = _pd_dd.stage_speed; _dd_ok_ロ_キック = True; break
    check("相手素早さ-1: ローキック", _dd_ok_ロ_キック and _dd_val_ロ_キック == -1, f"1回適用={_dd_val_ロ_キック} 期待=-1")

# ── ワイドブレイカー ──
check("DB: ワイドブレイカー 取得可能", dl.get_move("ワイドブレイカー") is not None)
_mv_ワイドブレイカ_ = dl.get_move("ワイドブレイカー")
if _mv_ワイドブレイカ_:
    _pa_ワイドブレイカ_ = make_poke(type1="ドラゴン", atk_b=100, spatk_b=100)
    _pd_ワイドブレイカ_ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ワイドブレイカ_ = dmg(_pa_ワイドブレイカ_, _pd_ワイドブレイカ_, "ワイドブレイカー")
    check("ダメージ計算: ワイドブレイカー", _d_ワイドブレイカ_ > 0, f"dmg={_d_ワイドブレイカ_}")
# ワイドブレイカー: 相手攻撃-1
_mv_dd_ワイドブレイカ_ = dl.get_move("ワイドブレイカー")
if _mv_dd_ワイドブレイカ_:
    _pa_dd = make_poke(type1="ドラゴン", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ワイドブレイカ_ = 0; _dd_ok_ワイドブレイカ_ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ワイドブレイカー")
        if _pd_dd.stage_attack != 0: _dd_val_ワイドブレイカ_ = _pd_dd.stage_attack; _dd_ok_ワイドブレイカ_ = True; break
    check("相手攻撃-1: ワイドブレイカー", _dd_ok_ワイドブレイカ_ and _dd_val_ワイドブレイカ_ == -1, f"1回適用={_dd_val_ワイドブレイカ_} 期待=-1")

# ── アクアリング ──
check("DB: アクアリング 取得可能", dl.get_move("アクアリング") is not None)
# アクアリング: 毎ターン1/16回復
_prt = make_poke(hp_b=200); _prt.hp = 50; execute(_prt, make_poke(), "アクアリング")
check("アクアリングフラグ: アクアリング", _prt.aqua_ring)
from simulator.battle import Battle as _B
_b = _B(BattleSide([_prt]), BattleSide([make_poke()])); _hp0 = _prt.hp
_b._end_of_turn()
check("アクアリング ターン終了回復: アクアリング", _prt.hp > _hp0, f"hp={_prt.hp}")

# ── あまいかおり ──
check("DB: あまいかおり 取得可能", dl.get_move("あまいかおり") is not None)
# あまいかおり: 相手回避率-2
_mv_dd_あまいかおり = dl.get_move("あまいかおり")
if _mv_dd_あまいかおり:
    _pa_dd = make_poke(type1="ノーマル", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_あまいかおり = 0; _dd_ok_あまいかおり = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "あまいかおり")
        if _pd_dd.stage_evasion != 0: _dd_val_あまいかおり = _pd_dd.stage_evasion; _dd_ok_あまいかおり = True; break
    check("相手回避率-2: あまいかおり", _dd_ok_あまいかおり and _dd_val_あまいかおり == -2, f"1回適用={_dd_val_あまいかおり} 期待=-2")

# ── あやしいひかり ──
check("DB: あやしいひかり 取得可能", dl.get_move("あやしいひかり") is not None)
# あやしいひかり: こんらん付与(変化技)
_mv_si_あやしいひかり = dl.get_move("あやしいひかり")
if _mv_si_あやしいひかり:
    random.seed(0); _ok_あやしいひかり = False
    for _ in range(30):
        _pa_si = make_poke(type1="ゴースト"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "あやしいひかり")
        if _pd_si.confused: _ok_あやしいひかり = True; break
    check("こんらん付与: あやしいひかり", _ok_あやしいひかり)

# ── アロマミスト ──
check("DB: アロマミスト 取得可能", dl.get_move("アロマミスト") is not None)
# アロマミスト: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: アロマミスト", "アロマミスト", "フェアリー", False, smoke=("アロマミスト" in DOUBLE_ONLY_SMOKE))

# ── いえき ──
check("DB: いえき 取得可能", dl.get_move("いえき") is not None)
# いえき: 相手をとくせいなし状態に
_pe = make_poke(); _de = make_poke(ability="いかく"); execute(_pe, _de, "いえき")
check("とくせい無効化: いえき", _de.ability_suppressed, f"sup={_de.ability_suppressed}")

# ── いちゃもん ──
check("DB: いちゃもん 取得可能", dl.get_move("いちゃもん") is not None)
# いちゃもん: 相手を連続不可状態に
_pic = make_poke(); _dic = make_poke(hp_b=200); execute(_pic, _dic, "いちゃもん")
check("連続不可付与: いちゃもん", _dic.torment, f"torment={_dic.torment}")

# ── いとをはく ──
check("DB: いとをはく 取得可能", dl.get_move("いとをはく") is not None)
# いとをはく: 相手素早さ-2
_mv_dd_いとをはく = dl.get_move("いとをはく")
if _mv_dd_いとをはく:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_いとをはく = 0; _dd_ok_いとをはく = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "いとをはく")
        if _pd_dd.stage_speed != 0: _dd_val_いとをはく = _pd_dd.stage_speed; _dd_ok_いとをはく = True; break
    check("相手素早さ-2: いとをはく", _dd_ok_いとをはく and _dd_val_いとをはく == -2, f"1回適用={_dd_val_いとをはく} 期待=-2")

# ── いのちがけ ──
check("DB: いのちがけ 取得可能", dl.get_move("いのちがけ") is not None)
# いのちがけ: 自分はひんしになり残HP分のダメージ
_plg = make_poke(type1="かくとう", atk_b=100); _plg.hp = 80; _dlg = make_poke(type1="ノーマル", hp_b=200, def_b=100)
_hplg = _dlg.hp; execute(_plg, _dlg, "いのちがけ")
check("可変ダメージ(いのちがけ): いのちがけ", not _plg.is_alive and (_hplg - _dlg.hp) == 80, f"自alive={_plg.is_alive} dmg={_hplg - _dlg.hp}")

# ── いのちのしずく ──
check("DB: いのちのしずく 取得可能", dl.get_move("いのちのしずく") is not None)
# いのちのしずく: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: いのちのしずく", "いのちのしずく", "みず", False, smoke=("いのちのしずく" in DOUBLE_ONLY_SMOKE))

# ── いばる ──
check("DB: いばる 取得可能", dl.get_move("いばる") is not None)
# いばる: 相手の攻撃+2&こんらん
_pib = make_poke(); _dib = make_poke(hp_b=200); execute(_pib, _dib, "いばる")
check("攻撃+2こんらん: いばる", _dib.stage_attack == 2 and _dib.confused, f"atk={_dib.stage_attack} conf={_dib.confused}")

# ── いやしのすず ──
check("DB: いやしのすず 取得可能", dl.get_move("いやしのすず") is not None)
# いやしのすず: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: いやしのすず", "いやしのすず", "ノーマル", False, smoke=("いやしのすず" in DOUBLE_ONLY_SMOKE))

# ── いやしのはどう ──
check("DB: いやしのはどう 取得可能", dl.get_move("いやしのはどう") is not None)
# いやしのはどう: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: いやしのはどう", "いやしのはどう", "エスパー", False, smoke=("いやしのはどう" in DOUBLE_ONLY_SMOKE))

# ── いやなおと ──
check("DB: いやなおと 取得可能", dl.get_move("いやなおと") is not None)
# いやなおと: 相手防御-2
_mv_dd_いやなおと = dl.get_move("いやなおと")
if _mv_dd_いやなおと:
    _pa_dd = make_poke(type1="ノーマル", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_いやなおと = 0; _dd_ok_いやなおと = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "いやなおと")
        if _pd_dd.stage_defense != 0: _dd_val_いやなおと = _pd_dd.stage_defense; _dd_ok_いやなおと = True; break
    check("相手防御-2: いやなおと", _dd_ok_いやなおと and _dd_val_いやなおと == -2, f"1回適用={_dd_val_いやなおと} 期待=-2")

# ── うそなき ──
check("DB: うそなき 取得可能", dl.get_move("うそなき") is not None)
# うそなき: 相手特防-2
_mv_dd_うそなき = dl.get_move("うそなき")
if _mv_dd_うそなき:
    _pa_dd = make_poke(type1="あく", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_うそなき = 0; _dd_ok_うそなき = False
    for _ in range(60):
        _pd_dd = make_poke(type1="エスパー", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "うそなき")
        if _pd_dd.stage_sp_defense != 0: _dd_val_うそなき = _pd_dd.stage_sp_defense; _dd_ok_うそなき = True; break
    check("相手特防-2: うそなき", _dd_ok_うそなき and _dd_val_うそなき == -2, f"1回適用={_dd_val_うそなき} 期待=-2")

# ── うたう ──
check("DB: うたう 取得可能", dl.get_move("うたう") is not None)
# うたう: ねむり付与(変化技)
_mv_si_うたう = dl.get_move("うたう")
if _mv_si_うたう:
    random.seed(0); _ok_うたう = False
    for _ in range(30):
        _pa_si = make_poke(type1="ノーマル"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "うたう")
        if _pd_si.status == "sleep": _ok_うたう = True; break
    check("ねむり付与: うたう", _ok_うたう)

# ── うっぷんばらし ──
check("DB: うっぷんばらし 取得可能", dl.get_move("うっぷんばらし") is not None)
_mv_うっぷんばらし = dl.get_move("うっぷんばらし")
if _mv_うっぷんばらし:
    _pa_うっぷんばらし = make_poke(type1="あく", atk_b=100, spatk_b=100)
    _pd_うっぷんばらし = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_うっぷんばらし = dmg(_pa_うっぷんばらし, _pd_うっぷんばらし, "うっぷんばらし")
    check("ダメージ計算: うっぷんばらし", _d_うっぷんばらし > 0, f"dmg={_d_うっぷんばらし}")
# うっぷんばらし: 自分の能力が下がっていれば威力2倍
_pcd = make_poke(type1="あく", atk_b=100, spatk_b=100); _dcd = make_poke(type1="エスパー", def_b=100, spdef_b=100)
_p_base = _ep(_pcd, _dcd, dl.get_move("うっぷんばらし"), BattleField())
_pcd.stage_attack = -1
_p_cond = _ep(_pcd, _dcd, dl.get_move("うっぷんばらし"), BattleField())
check("条件成立で威力2倍: うっぷんばらし", _p_cond == _p_base * 2, f"base={_p_base} cond={_p_cond}")

# ── うらみ ──
check("DB: うらみ 取得可能", dl.get_move("うらみ") is not None)
# うらみ: 相手の最後の技のPPを4減らす
_ppp = make_poke(spatk_b=10, atk_b=10); _dpp = make_poke(moves=["たいあたり"], hp_b=255, def_b=255, spdef_b=255); _dpp.last_used_move = "たいあたり"; _dpp.pp = [20]
execute(_ppp, _dpp, "うらみ")
check("PP減少: うらみ", _dpp.pp[0] == 20 - 4, f"pp={_dpp.pp[0]}")

# ── エアカッター ──
check("DB: エアカッター 取得可能", dl.get_move("エアカッター") is not None)
_mv_エアカッタ_ = dl.get_move("エアカッター")
if _mv_エアカッタ_:
    _pa_エアカッタ_ = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_エアカッタ_ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_エアカッタ_ = dmg(_pa_エアカッタ_, _pd_エアカッタ_, "エアカッター")
    check("ダメージ計算: エアカッター", _d_エアカッタ_ > 0, f"dmg={_d_エアカッタ_}")
# エアカッター: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_エアカッタ_
random.seed(0); _hc_crit_エアカッタ_ = 0; _phc = make_poke(type1="ひこう")
_mvhc_エアカッタ_ = dl.get_move("エアカッター")
for _ in range(800):
    if _cc_エアカッタ_(_phc, _mvhc_エアカッタ_, make_poke(type1="くさ")): _hc_crit_エアカッタ_ += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: エアカッター", 60 <= _hc_crit_エアカッタ_ <= 150, f"crit={_hc_crit_エアカッタ_}/800 (期待≈100, 通常1/24なら≈33)")

# ── エレキボール ──
check("DB: エレキボール 取得可能", dl.get_move("エレキボール") is not None)
# エレキボール: 速度比別の威力テーブル（≥4→150 ≥3→120 ≥2→80 ≥1→60 未満→40）
_peb = make_poke(type1="でんき", spatk_b=100)
_eb_ng = []
for _ratio, _exp in [(4,150),(3,120),(2,80),(1,60),(0.5,40)]:
    _deb = make_poke(type1="ノーマル")
    _peb.speed = 200; _deb.speed = int(200 / _ratio)
    _got = _ep(_peb, _deb, dl.get_move("エレキボール"), BattleField())
    if _got != _exp: _eb_ng.append(f"ratio={_ratio}:{_got}!={_exp}")
check("速度比別威力テーブル: エレキボール", not _eb_ng, f"NG={_eb_ng}")

# ── おさきにどうぞ ──
check("DB: おさきにどうぞ 取得可能", dl.get_move("おさきにどうぞ") is not None)
# おさきにどうぞ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: おさきにどうぞ", "おさきにどうぞ", "ノーマル", False, smoke=("おさきにどうぞ" in DOUBLE_ONLY_SMOKE))

# ── おたけび ──
check("DB: おたけび 取得可能", dl.get_move("おたけび") is not None)
# おたけび: 相手の攻撃・特攻-1
_pok = make_poke(); _dok = make_poke(hp_b=200); execute(_pok, _dok, "おたけび")
check("相手攻撃特攻ダウン: おたけび", _dok.stage_attack == -1 and _dok.stage_sp_attack == -1, f"atk={_dok.stage_attack} spa={_dok.stage_sp_attack}")

# ── おだてる ──
check("DB: おだてる 取得可能", dl.get_move("おだてる") is not None)
# おだてる: 相手の特攻+1&こんらん
_pod = make_poke(); _dod = make_poke(hp_b=200); execute(_pod, _dod, "おだてる")
check("特攻+1こんらん: おだてる", _dod.stage_sp_attack == 1 and _dod.confused, f"spa={_dod.stage_sp_attack} conf={_dod.confused}")

# ── おちゃかい ──
check("DB: おちゃかい 取得可能", dl.get_move("おちゃかい") is not None)
# おちゃかい: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: おちゃかい", "おちゃかい", "ノーマル", False, smoke=("おちゃかい" in DOUBLE_ONLY_SMOKE))

# ── かふんだんご ──
check("DB: かふんだんご 取得可能", dl.get_move("かふんだんご") is not None)
_mv_かふんだんご = dl.get_move("かふんだんご")
if _mv_かふんだんご:
    _pa_かふんだんご = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_かふんだんご = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_かふんだんご = dmg(_pa_かふんだんご, _pd_かふんだんご, "かふんだんご")
    check("ダメージ計算: かふんだんご", _d_かふんだんご > 0, f"dmg={_d_かふんだんご}")

# ── ガードシェア ──
check("DB: ガードシェア 取得可能", dl.get_move("ガードシェア") is not None)
# ガードシェア: 防御・特防を平均化
_pgs = make_poke(def_b=200); _dgs = make_poke(def_b=20)
_exp = (_pgs.defense + _dgs.defense)//2
execute(_pgs, _dgs, "ガードシェア")
check("ガードシェア 防御平均化: ガードシェア", _pgs.defense == _exp and _dgs.defense == _exp)

# ── ガードスワップ ──
check("DB: ガードスワップ 取得可能", dl.get_move("ガードスワップ") is not None)
# ガードスワップ: 防御・特防の能力変化を相手と入れ替え（双方向。コピーでなく入替を区別）
_pg = make_poke(); _pg.stage_defense = -1; _pg.stage_sp_defense = 1
_dg = make_poke(); _dg.stage_defense = 3; _dg.stage_sp_defense = 2
execute(_pg, _dg, "ガードスワップ")
check("ガードスワップ入替(双方向): ガードスワップ", _pg.stage_defense == 3 and _pg.stage_sp_defense == 2 and _dg.stage_defense == -1 and _dg.stage_sp_defense == 1, f"自{_pg.stage_defense}/{_pg.stage_sp_defense} 相{_dg.stage_defense}/{_dg.stage_sp_defense}")

# ── きんぞくおん ──
check("DB: きんぞくおん 取得可能", dl.get_move("きんぞくおん") is not None)
# きんぞくおん: 相手特防-2
_mv_dd_きんぞくおん = dl.get_move("きんぞくおん")
if _mv_dd_きんぞくおん:
    _pa_dd = make_poke(type1="はがね", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_きんぞくおん = 0; _dd_ok_きんぞくおん = False
    for _ in range(60):
        _pd_dd = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "きんぞくおん")
        if _pd_dd.stage_sp_defense != 0: _dd_val_きんぞくおん = _pd_dd.stage_sp_defense; _dd_ok_きんぞくおん = True; break
    check("相手特防-2: きんぞくおん", _dd_ok_きんぞくおん and _dd_val_きんぞくおん == -2, f"1回適用={_dd_val_きんぞくおん} 期待=-2")

# ── くすぐる ──
check("DB: くすぐる 取得可能", dl.get_move("くすぐる") is not None)
# くすぐる: 相手の攻撃・防御-1
_pks = make_poke(); _dks = make_poke(hp_b=200); execute(_pks, _dks, "くすぐる")
check("相手攻撃防御ダウン: くすぐる", _dks.stage_attack == -1 and _dks.stage_defense == -1, f"atk={_dks.stage_attack} def={_dks.stage_defense}")

# ── グラスフィールド ──
check("DB: グラスフィールド 取得可能", dl.get_move("グラスフィールド") is not None)
# グラスフィールド: フィールド展開
side_effect_check("フィールド展開: グラスフィールド", "グラスフィールド", "くさ", True)

# ── くろいまなざし ──
check("DB: くろいまなざし 取得可能", dl.get_move("くろいまなざし") is not None)
# くろいまなざし: 相手をにげられない状態に
_ptr = make_poke(type1="ノーマル", atk_b=120); _dtr = make_poke(type1="ノーマル", hp_b=255, def_b=100)
execute(_ptr, _dtr, "くろいまなざし")
check("にげられない付与: くろいまなざし", _dtr.trapped)

# ── ゲップ ──
check("DB: ゲップ 取得可能", dl.get_move("ゲップ") is not None)
_mv_ゲップ = dl.get_move("ゲップ")
if _mv_ゲップ:
    _pa_ゲップ = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_ゲップ = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ゲップ = dmg(_pa_ゲップ, _pd_ゲップ, "ゲップ")
    check("ダメージ計算: ゲップ", _d_ゲップ > 0, f"dmg={_d_ゲップ}")
# ゲップ: きのみ未食だと失敗、食べていれば成功
_pgf = make_poke(type1="どく", spatk_b=100); _dgf = make_poke(type1="くさ", hp_b=255, spdef_b=120)
_hpd1 = _dgf.hp; execute(_pgf, _dgf, "ゲップ")
check("きのみ未食失敗: ゲップ", _dgf.hp == _hpd1, f"hp={_dgf.hp}/{_hpd1}")
_pgs = make_poke(type1="どく", spatk_b=100); _pgs.ate_berry = True; _dgs = make_poke(type1="くさ", hp_b=255, spdef_b=120)
_hpd2 = _dgs.hp; execute(_pgs, _dgs, "ゲップ")
check("きのみ食後成功: ゲップ", _dgs.hp < _hpd2, f"hp={_dgs.hp}/{_hpd2}")

# ── こおりのいぶき ──
check("DB: こおりのいぶき 取得可能", dl.get_move("こおりのいぶき") is not None)
_mv_こおりのいぶき = dl.get_move("こおりのいぶき")
if _mv_こおりのいぶき:
    _pa_こおりのいぶき = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _pd_こおりのいぶき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_こおりのいぶき = dmg(_pa_こおりのいぶき, _pd_こおりのいぶき, "こおりのいぶき")
    check("ダメージ計算: こおりのいぶき", _d_こおりのいぶき > 0, f"dmg={_d_こおりのいぶき}")
# こおりのいぶき: 必ず急所（高ダメージ）
_mvcr_こおりのいぶき = dl.get_move("こおりのいぶき")
if _mvcr_こおりのいぶき:
    _pac = make_poke(type1="こおり", atk_b=100, spatk_b=100)
    _d_crit = dmg(_pac, make_poke(type1="くさ", def_b=100, spdef_b=100), "こおりのいぶき")
    check("必ず急所(>0): こおりのいぶき", _d_crit > 0)

# ── ゴッドバード ──
check("DB: ゴッドバード 取得可能", dl.get_move("ゴッドバード") is not None)
_mv_ゴッドバ_ド = dl.get_move("ゴッドバード")
if _mv_ゴッドバ_ド:
    _pa_ゴッドバ_ド = make_poke(type1="ひこう", atk_b=100, spatk_b=100)
    _pd_ゴッドバ_ド = make_poke(type1="くさ", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_ゴッドバ_ド = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_ゴッドバ_ド = make_poke(type1="くさ", def_b=100, spdef_b=100)
        execute(_pa_ゴッドバ_ド, _pd_ゴッドバ_ド, "ゴッドバード"); execute(_pa_ゴッドバ_ド, _pd_ゴッドバ_ド, "ゴッドバード")
        if _pd_ゴッドバ_ド.hp < _pd_ゴッドバ_ド.max_hp: break
    check("ダメージ計算: ゴッドバード", _pd_ゴッドバ_ド.hp < _pd_ゴッドバ_ド.max_hp, f"hp={_pd_ゴッドバ_ド.hp}")
# ゴッドバード: ひるみ30%
_mv_f_ゴッドバ_ド = dl.get_move("ゴッドバード")
if _mv_f_ゴッドバ_ド:
    random.seed(1); _fh_ゴッドバ_ド = 0
    for _ in range(300):
        _pa3 = make_poke(type1="ひこう", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa3, _pd3, "ゴッドバード"); _fh_ゴッドバ_ド += int(_pd3.flinched); execute(_pa3, _pd3, "ゴッドバード"); _fh_ゴッドバ_ド += int(_pd3.flinched)
    check("ひるみ(30%): ゴッドバード", 27 <= _fh_ゴッドバ_ド <= 168, f"count={_fh_ゴッドバ_ド}/300")
# ゴッドバード: 2ターン溜め
_mv_2t_ゴッドバ_ド = dl.get_move("ゴッドバード")
if _mv_2t_ゴッドバ_ド:
    _pa_2t = make_poke(type1="ひこう", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "ゴッドバード")
    check("2ターン溜め(1T)ダメなし: ゴッドバード", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: ゴッドバード", _pa_2t.charging_move == "ゴッドバード")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "ゴッドバード")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "ゴッドバード")
    check("2ターン溜め(2T)ダメあり: ゴッドバード", _pd_2t.hp < _hp_before_2t)
# ゴッドバード: 急所ランク+1（急所率が通常技より高い）
from simulator.battle import _check_critical as _cc_ゴッドバ_ド
random.seed(0); _hc_crit_ゴッドバ_ド = 0; _phc = make_poke(type1="ひこう")
_mvhc_ゴッドバ_ド = dl.get_move("ゴッドバード")
for _ in range(800):
    if _cc_ゴッドバ_ド(_phc, _mvhc_ゴッドバ_ド, make_poke(type1="くさ")): _hc_crit_ゴッドバ_ド += 1
# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別
check("急所ランク+1: ゴッドバード", 60 <= _hc_crit_ゴッドバ_ド <= 150, f"crit={_hc_crit_ゴッドバ_ド}/800 (期待≈100, 通常1/24なら≈33)")

# ── このゆびとまれ ──
check("DB: このゆびとまれ 取得可能", dl.get_move("このゆびとまれ") is not None)
# このゆびとまれ: 優先度2
_mv_pr_このゆびとまれ = dl.get_move("このゆびとまれ")
if _mv_pr_このゆびとまれ and _mv_pr_このゆびとまれ.priority == 2:
    check("優先度2: このゆびとまれ", _mv_pr_このゆびとまれ.priority == 2)
elif _mv_pr_このゆびとまれ:
    check("優先度2: このゆびとまれ", _mv_pr_このゆびとまれ.priority == 2, f"DB優先度={_mv_pr_このゆびとまれ.priority} 仕様=2")
# このゆびとまれ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: このゆびとまれ", "このゆびとまれ", "ノーマル", False, smoke=("このゆびとまれ" in DOUBLE_ONLY_SMOKE))

# ── サイドチェンジ ──
check("DB: サイドチェンジ 取得可能", dl.get_move("サイドチェンジ") is not None)
# サイドチェンジ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: サイドチェンジ", "サイドチェンジ", "エスパー", False, smoke=("サイドチェンジ" in DOUBLE_ONLY_SMOKE))

# ── さきおくり ──
check("DB: さきおくり 取得可能", dl.get_move("さきおくり") is not None)
# さきおくり: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: さきおくり", "さきおくり", "あく", True, smoke=("さきおくり" in DOUBLE_ONLY_SMOKE))

# ── さわぐ ──
check("DB: さわぐ 取得可能", dl.get_move("さわぐ") is not None)
_mv_さわぐ = dl.get_move("さわぐ")
if _mv_さわぐ:
    _pa_さわぐ = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_さわぐ = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_さわぐ = dmg(_pa_さわぐ, _pd_さわぐ, "さわぐ")
    check("ダメージ計算: さわぐ", _d_さわぐ > 0, f"dmg={_d_さわぐ}")
# さわぐ: 2〜3ターン連続使用ロック（さわぐ状態）
_psw = make_poke(type1="ノーマル", spatk_b=100); _dsw = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)
execute(_psw, _dsw, "さわぐ")
check("さわぐ状態ロック: さわぐ", _psw.locked_move == "さわぐ" and _psw.lock_count >= 1, f"locked={_psw.locked_move} count={_psw.lock_count}")

# ── じこあんじ ──
check("DB: じこあんじ 取得可能", dl.get_move("じこあんじ") is not None)
# じこあんじ: 相手の能力変化を自分にコピー
_pj = make_poke(); _dj = make_poke(); _dj.stage_attack = 2; _dj.stage_speed = -1
execute(_pj, _dj, "じこあんじ")
check("じこあんじコピー: じこあんじ", _pj.stage_attack == 2 and _pj.stage_speed == -1, f"atk={_pj.stage_attack} spd={_pj.stage_speed}")

# ── じばそうさ ──
check("DB: じばそうさ 取得可能", dl.get_move("じばそうさ") is not None)
# じばそうさ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: じばそうさ", "じばそうさ", "でんき", False, smoke=("じばそうさ" in DOUBLE_ONLY_SMOKE))

# ── じゅうりょく ──
check("DB: じゅうりょく 取得可能", dl.get_move("じゅうりょく") is not None)
# じゅうりょく: 場の状態セット
_s1rm, _s2rm, _frm = execute_ctx(make_poke(type1="エスパー"), make_poke(), "じゅうりょく")
check("じゅうりょく 場の状態: じゅうりょく", bool(getattr(_frm, "gravity", 0)))

# ── しんぴのまもり ──
check("DB: しんぴのまもり 取得可能", dl.get_move("しんぴのまもり") is not None)
# しんぴのまもり: 自分側が状態異常を防ぐ（でんじはを無効化）
_pss = make_poke(type1="ノーマル"); _dss = make_poke(type1="ノーマル", hp_b=200)
_s2ss = BattleSide([_dss]); _s2ss.safeguard = 5
random.seed(0)
for _ in range(10): _execute_move(BattleSide([_pss]), _s2ss, Action(type="move", move=dl.get_move("でんじは")), BattleField())
check("状態異常防御: しんぴのまもり", _dss.status is None, f"status={_dss.status}")

# ── シンプルビーム ──
check("DB: シンプルビーム 取得可能", dl.get_move("シンプルビーム") is not None)
# シンプルビーム: 相手の特性をたんじゅんに
_psb = make_poke(); _dsb = make_poke(ability="いかく"); execute(_psb, _dsb, "シンプルビーム")
check("特性たんじゅん化: シンプルビーム", _dsb.ability == "たんじゅん", f"相{_dsb.ability}")

# ── スキルスワップ ──
check("DB: スキルスワップ 取得可能", dl.get_move("スキルスワップ") is not None)
# スキルスワップ: 特性を相手と入れ替え
_pk = make_poke(ability="いかく"); _dk = make_poke(ability="ちょすい")
execute(_pk, _dk, "スキルスワップ")
check("特性入替: スキルスワップ", _pk.ability == "ちょすい" and _dk.ability == "いかく", f"自{_pk.ability} 相{_dk.ability}")

# ── すなじごく ──
check("DB: すなじごく 取得可能", dl.get_move("すなじごく") is not None)
_mv_すなじごく = dl.get_move("すなじごく")
if _mv_すなじごく:
    _pa_すなじごく = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_すなじごく = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_すなじごく = dmg(_pa_すなじごく, _pd_すなじごく, "すなじごく")
    check("ダメージ計算: すなじごく", _d_すなじごく > 0, f"dmg={_d_すなじごく}")
# すなじごく: バインド
_mv_bd_すなじごく = dl.get_move("すなじごく")
if _mv_bd_すなじごく:
    random.seed(0)
    for _ in range(20):
        _pa_bd = make_poke(type1="じめん", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="でんき", def_b=100, spdef_b=100, hp_b=255)
        execute(_pa_bd, _pd_bd, "すなじごく")
        if _pd_bd.bound_count in (4,5): break
    check("バインド付与: すなじごく", _pd_bd.bound_count in (4,5), f"count={_pd_bd.bound_count}")

# ── スピードスワップ ──
check("DB: スピードスワップ 取得可能", dl.get_move("スピードスワップ") is not None)
# スピードスワップ: 素早さの実数値を相手と入れ替え
_ps = make_poke(spd_b=50); _ds = make_poke(spd_b=200); _spb = _ps.speed; _dspb = _ds.speed
execute(_ps, _ds, "スピードスワップ")
check("素早さ入替: スピードスワップ", _ps.speed == _dspb and _ds.speed == _spb, f"自{_ps.speed} 相{_ds.speed}")

# ── せいちょう ──
check("DB: せいちょう 取得可能", dl.get_move("せいちょう") is not None)
# せいちょう: 自分攻撃+1
_mv_sb_せいちょう_attack = dl.get_move("せいちょう")
if _mv_sb_せいちょう_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "せいちょう")
    check("自分攻撃+1: せいちょう", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# せいちょう: 自分特攻+1
_mv_sb_せいちょう_sp_attack = dl.get_move("せいちょう")
if _mv_sb_せいちょう_sp_attack:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "せいちょう")
    check("自分特攻+1: せいちょう", _pa_sb.stage_sp_attack == 1, f"1回適用={_pa_sb.stage_sp_attack} 期待=+1")
# せいちょう: 通常は攻撃・特攻+1、にほんばれ中は+2
_pg1 = make_poke(type1="ノーマル"); execute(_pg1, make_poke(), "せいちょう")
check("せいちょう通常+1: せいちょう", _pg1.stage_attack == 1, f"atk={_pg1.stage_attack}")
_pg2 = make_poke(type1="ノーマル"); _fsun_g = BattleField(); _fsun_g.weather = "sunny"; execute(_pg2, make_poke(), "せいちょう", _fsun_g)
check("晴れ2段階: せいちょう", _pg2.stage_attack == 2, f"atk={_pg2.stage_attack}")

# ── そうでん ──
check("DB: そうでん 取得可能", dl.get_move("そうでん") is not None)
# そうでん: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: そうでん", "そうでん", "でんき", False, smoke=("そうでん" in DOUBLE_ONLY_SMOKE))

# ── だいちのはどう ──
check("DB: だいちのはどう 取得可能", dl.get_move("だいちのはどう") is not None)
_mv_だいちのはどう = dl.get_move("だいちのはどう")
if _mv_だいちのはどう:
    _pa_だいちのはどう = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_だいちのはどう = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_だいちのはどう = dmg(_pa_だいちのはどう, _pd_だいちのはどう, "だいちのはどう")
    check("ダメージ計算: だいちのはどう", _d_だいちのはどう > 0, f"dmg={_d_だいちのはどう}")
# だいちのはどう: フィールドでタイプが変わる（グラスF→くさ）
_pew = make_poke(type1="ノーマル", spatk_b=120)
_few = BattleField(); _few.grassy_terrain = True
from simulator.damage import _effective_move_type as _emt
check("フィールド型変化: だいちのはどう", _emt(_pew, dl.get_move("だいちのはどう"), _few) == "くさ", f"type={_emt(_pew, dl.get_move('だいちのはどう'), _few)}")
# フィールド効果を受けていると威力2倍（接地時）／フィールド無しは等倍
_pdw = make_poke(type1="じめん", spatk_b=100, atk_b=100); _ddw = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
_dw_n = _ep(_pdw, _ddw, dl.get_move("だいちのはどう"), BattleField())
_fdw = BattleField(); _fdw.grassy_terrain = True; _dw_f = _ep(_pdw, _ddw, dl.get_move("だいちのはどう"), _fdw)
check("フィールドで威力2倍: だいちのはどう", _dw_f == _dw_n * 2, f"no={_dw_n} field={_dw_f}")

# ── だいふんげき ──
check("DB: だいふんげき 取得可能", dl.get_move("だいふんげき") is not None)
_mv_だいふんげき = dl.get_move("だいふんげき")
if _mv_だいふんげき:
    _pa_だいふんげき = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_だいふんげき = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_だいふんげき = dmg(_pa_だいふんげき, _pd_だいふんげき, "だいふんげき")
    check("ダメージ計算: だいふんげき", _d_だいふんげき > 0, f"dmg={_d_だいふんげき}")
# だいふんげき: あばれ状態
_mv_rg_だいふんげき = dl.get_move("だいふんげき")
if _mv_rg_だいふんげき:
    _pa_rg = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd_rg = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
    execute(_pa_rg, _pd_rg, "だいふんげき")
    check("あばれ状態: だいふんげき", _pa_rg.locked_move == "だいふんげき")

# ── だくりゅう ──
check("DB: だくりゅう 取得可能", dl.get_move("だくりゅう") is not None)
_mv_だくりゅう = dl.get_move("だくりゅう")
if _mv_だくりゅう:
    _pa_だくりゅう = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_だくりゅう = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_だくりゅう = dmg(_pa_だくりゅう, _pd_だくりゅう, "だくりゅう")
    check("ダメージ計算: だくりゅう", _d_だくりゅう > 0, f"dmg={_d_だくりゅう}")
# だくりゅう: 相手命中率-1
_mv_dd_だくりゅう = dl.get_move("だくりゅう")
if _mv_dd_だくりゅう:
    _pa_dd = make_poke(type1="みず", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_だくりゅう = 0; _dd_ok_だくりゅう = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ほのお", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "だくりゅう")
        if _pd_dd.stage_accuracy != 0: _dd_val_だくりゅう = _pd_dd.stage_accuracy; _dd_ok_だくりゅう = True; break
    check("相手命中率-1: だくりゅう", _dd_ok_だくりゅう and _dd_val_だくりゅう == -1, f"1回適用={_dd_val_だくりゅう} 期待=-1")

# ── たくわえる ──
check("DB: たくわえる 取得可能", dl.get_move("たくわえる") is not None)
# たくわえる: 自分防御+1
_mv_sb_たくわえる_defense = dl.get_move("たくわえる")
if _mv_sb_たくわえる_defense:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "たくわえる")
    check("自分防御+1: たくわえる", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")
# たくわえる: 自分特防+1
_mv_sb_たくわえる_sp_defense = dl.get_move("たくわえる")
if _mv_sb_たくわえる_sp_defense:
    _pa_sb = make_poke(type1="ノーマル"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "たくわえる")
    check("自分特防+1: たくわえる", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")
# たくわえる: たくわえカウント+1
_ptk = make_poke(); execute(_ptk, make_poke(), "たくわえる")
check("たくわえ+1: たくわえる", _ptk.stockpile_count == 1, f"sc={_ptk.stockpile_count}")

# ── チャージビーム ──
check("DB: チャージビーム 取得可能", dl.get_move("チャージビーム") is not None)
_mv_チャ_ジビ_ム = dl.get_move("チャージビーム")
if _mv_チャ_ジビ_ム:
    _pa_チャ_ジビ_ム = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_チャ_ジビ_ム = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_チャ_ジビ_ム = dmg(_pa_チャ_ジビ_ム, _pd_チャ_ジビ_ム, "チャージビーム")
    check("ダメージ計算: チャージビーム", _d_チャ_ジビ_ム > 0, f"dmg={_d_チャ_ジビ_ム}")
# チャージビーム: 70%で自分の特攻+1
random.seed(0); _cb_up = False
for _ in range(20):
    _pcb = make_poke(type1="でんき", spatk_b=100); _dcb = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)
    execute(_pcb, _dcb, "チャージビーム")
    if _pcb.stage_sp_attack > 0: _cb_up = True; break
check("自分特攻上昇(70%): チャージビーム", _cb_up)

# ── つぼをつく ──
check("DB: つぼをつく 取得可能", dl.get_move("つぼをつく") is not None)
# つぼをつく: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: つぼをつく", "つぼをつく", "ノーマル", False, smoke=("つぼをつく" in DOUBLE_ONLY_SMOKE))

# ── てだすけ ──
check("DB: てだすけ 取得可能", dl.get_move("てだすけ") is not None)
# てだすけ: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: てだすけ", "てだすけ", "ノーマル", False, smoke=("てだすけ" in DOUBLE_ONLY_SMOKE))

# ── てんしのキッス ──
check("DB: てんしのキッス 取得可能", dl.get_move("てんしのキッス") is not None)
# てんしのキッス: こんらん付与(変化技)
_mv_si_てんしのキッス = dl.get_move("てんしのキッス")
if _mv_si_てんしのキッス:
    random.seed(0); _ok_てんしのキッス = False
    for _ in range(30):
        _pa_si = make_poke(type1="フェアリー"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "てんしのキッス")
        if _pd_si.confused: _ok_てんしのキッス = True; break
    check("こんらん付与: てんしのキッス", _ok_てんしのキッス)

# ── とおせんぼう ──
check("DB: とおせんぼう 取得可能", dl.get_move("とおせんぼう") is not None)
# とおせんぼう: 相手をにげられない状態に
_ptr = make_poke(type1="ノーマル", atk_b=120); _dtr = make_poke(type1="ノーマル", hp_b=255, def_b=100)
execute(_ptr, _dtr, "とおせんぼう")
check("にげられない付与: とおせんぼう", _dtr.trapped)

# ── とおぼえ ──
check("DB: とおぼえ 取得可能", dl.get_move("とおぼえ") is not None)
# とおぼえ: 自分の攻撃+1
_pto = make_poke(type1="ノーマル"); execute(_pto, make_poke(), "とおぼえ")
check("攻撃+1: とおぼえ", _pto.stage_attack == 1, f"atk={_pto.stage_attack}")

# ── デコレーション ──
check("DB: デコレーション 取得可能", dl.get_move("デコレーション") is not None)
# デコレーション: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: デコレーション", "デコレーション", "フェアリー", False, smoke=("デコレーション" in DOUBLE_ONLY_SMOKE))

# ── トライアタック ──
check("DB: トライアタック 取得可能", dl.get_move("トライアタック") is not None)
_mv_トライアタック = dl.get_move("トライアタック")
if _mv_トライアタック:
    _pa_トライアタック = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_トライアタック = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_トライアタック = dmg(_pa_トライアタック, _pd_トライアタック, "トライアタック")
    check("ダメージ計算: トライアタック", _d_トライアタック > 0, f"dmg={_d_トライアタック}")
# トライアタック: まひ20%
_mv_s_トライアタック = dl.get_move("トライアタック")
if _mv_s_トライアタック:
    random.seed(0); _hit_トライアタック = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="ノーマル", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "トライアタック")
        _hit_トライアタック += int((_pd2.status == "paralysis"))
    check("追加効果(まひ20%): トライアタック", 18 <= _hit_トライアタック <= 117, f"count={_hit_トライアタック}/300")
    random.seed(1); _immok_トライアタック = True
    for _ in range(60):
        _pai = make_poke(type1="ノーマル", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "トライアタック")
        if _pdi.status == "paralysis": _immok_トライアタック = False; break
    check("まひ免疫(でんき型には無効): トライアタック", _immok_トライアタック, "免疫タイプに状態異常が付与されないこと")
# トライアタック: まひ・やけど・こおりの「いずれか」→3状態すべてが実際に発生する
_pta_m = make_poke(type1="ノーマル", spatk_b=30)
random.seed(0); _ta_cnt = {"paralysis":0, "burn":0, "freeze":0}
for _ in range(900):
    _dta_m = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
    execute(_pta_m, _dta_m, "トライアタック")
    if _dta_m.status in _ta_cnt: _ta_cnt[_dta_m.status] += 1
check("いずれか3状態すべて発生: トライアタック", all(_v > 0 for _v in _ta_cnt.values()), f"counts={_ta_cnt}")

# ── でんじほう ──
check("DB: でんじほう 取得可能", dl.get_move("でんじほう") is not None)
_mv_でんじほう = dl.get_move("でんじほう")
if _mv_でんじほう:
    _pa_でんじほう = make_poke(type1="でんき", atk_b=100, spatk_b=100)
    _pd_でんじほう = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_でんじほう = dmg(_pa_でんじほう, _pd_でんじほう, "でんじほう")
    check("ダメージ計算: でんじほう", _d_でんじほう > 0, f"dmg={_d_でんじほう}")
# でんじほう: まひ100%
_mv_s_でんじほう = dl.get_move("でんじほう")
if _mv_s_でんじほう:
    random.seed(0); _hit_でんじほう = 0
    for _ in range(300):
        _pa2 = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="みず", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "でんじほう")
        _hit_でんじほう += int((_pd2.status == "paralysis"))
    check("追加効果(まひ100%): でんじほう", 90 <= _hit_でんじほう <= 525, f"count={_hit_でんじほう}/300")
    random.seed(1); _immok_でんじほう = True
    for _ in range(60):
        _pai = make_poke(type1="でんき", atk_b=30, spatk_b=30); _pdi = make_poke(type1="でんき", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "でんじほう")
        if _pdi.status == "paralysis": _immok_でんじほう = False; break
    check("まひ免疫(でんき型には無効): でんじほう", _immok_でんじほう, "免疫タイプに状態異常が付与されないこと")

# ── ナイトヘッド ──
check("DB: ナイトヘッド 取得可能", dl.get_move("ナイトヘッド") is not None)
# ナイトヘッド: 固定50ダメージ
_mvfx_ナイトヘッド = dl.get_move("ナイトヘッド")
if _mvfx_ナイトヘッド:
    _paf = make_poke(type1="ゴースト", atk_b=100, spatk_b=100); _pdf = make_poke(type1="エスパー", hp_b=200, def_b=100, spdef_b=100)
    _hpbf = _pdf.hp; execute(_paf, _pdf, "ナイトヘッド")
    check("固定50ダメージ: ナイトヘッド", _hpbf - _pdf.hp == 50, f"dmg={_hpbf - _pdf.hp}")

# ── なかまづくり ──
check("DB: なかまづくり 取得可能", dl.get_move("なかまづくり") is not None)
# なかまづくり: 相手の特性を自分と同じに
_pn = make_poke(ability="いかく"); _dn = make_poke(ability="ちょすい")
execute(_pn, _dn, "なかまづくり")
check("特性コピー(相手): なかまづくり", _dn.ability == "いかく", f"相{_dn.ability}")

# ── どくのこな ──
check("DB: どくのこな 取得可能", dl.get_move("どくのこな") is not None)
# どくのこな: どく付与(変化技)
_mv_si_どくのこな = dl.get_move("どくのこな")
if _mv_si_どくのこな:
    random.seed(0); _ok_どくのこな = False
    for _ in range(30):
        _pa_si = make_poke(type1="どく"); _pd_si = make_poke(type1="ノーマル", hp_b=255)
        execute(_pa_si, _pd_si, "どくのこな")
        if _pd_si.status == "poison": _ok_どくのこな = True; break
    check("どく付与: どくのこな", _ok_どくのこな)
    random.seed(2); _siimm_どくのこな = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="どく", hp_b=255)
        execute(_pai2, _pdi2, "どくのこな")
        if _pdi2.status == "poison": _siimm_どくのこな = False; break
    check("どく免疫(どく型には無効): どくのこな", _siimm_どくのこな, "免疫タイプに付与されないこと")
    random.seed(2); _siimm_どくのこな = True
    for _ in range(40):
        _pai2 = make_poke(type1="どく"); _pdi2 = make_poke(type1="はがね", hp_b=255)
        execute(_pai2, _pdi2, "どくのこな")
        if _pdi2.status == "poison": _siimm_どくのこな = False; break
    check("どく免疫(はがね型には無効): どくのこな", _siimm_どくのこな, "免疫タイプに付与されないこと")
# どくのこな: 粉技。くさタイプには無効
_ppw = make_poke(type1="どく"); random.seed(0); _pw_ok = False
for _ in range(20):
    _dpw = make_poke(type1="ノーマル", hp_b=200); execute(_ppw, _dpw, "どくのこな")
    if _dpw.status == "poison": _pw_ok = True; break
check("粉付与: どくのこな", _pw_ok)
_dpw2 = make_poke(type1="くさ", hp_b=200)
for _ in range(20): execute(_ppw, _dpw2, "どくのこな")
check("くさ無効: どくのこな", _dpw2.status is None, f"status={_dpw2.status}")

# ── なみだめ ──
check("DB: なみだめ 取得可能", dl.get_move("なみだめ") is not None)
# なみだめ: 相手の攻撃・特攻-1 + 回避率を無視して命中（高回避にも当たる）
_pnd = make_poke(); _dnd = make_poke(hp_b=200); execute(_pnd, _dnd, "なみだめ")
check("相手攻撃特攻ダウン: なみだめ", _dnd.stage_attack == -1 and _dnd.stage_sp_attack == -1, f"atk={_dnd.stage_attack} spa={_dnd.stage_sp_attack}")
# 回避無視: stage_evasion=6(最大)でも命中する
random.seed(0); _pnd2 = make_poke(); _dnd2 = make_poke(hp_b=200); _dnd2.stage_evasion = 6
for _ in range(10): execute(_pnd2, _dnd2, "なみだめ")
check("回避無視: なみだめ", _dnd2.stage_attack < 0, f"atk={_dnd2.stage_attack}(回避6でも命中するべき)")

# ── なやみのタネ ──
check("DB: なやみのタネ 取得可能", dl.get_move("なやみのタネ") is not None)
# なやみのタネ: 相手の特性をふみんに
_pny = make_poke(); _dny = make_poke(ability="いかく"); execute(_pny, _dny, "なやみのタネ")
check("特性ふみん化: なやみのタネ", _dny.ability == "ふみん", f"相{_dny.ability}")

# ── ドラゴンエール ──
check("DB: ドラゴンエール 取得可能", dl.get_move("ドラゴンエール") is not None)
# ドラゴンエール: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: ドラゴンエール", "ドラゴンエール", "ドラゴン", False, smoke=("ドラゴンエール" in DOUBLE_ONLY_SMOKE))

# ── なりきり ──
check("DB: なりきり 取得可能", dl.get_move("なりきり") is not None)
# なりきり: 自分の特性を相手と同じに
_pr = make_poke(ability="いかく"); _dr = make_poke(ability="ちょすい")
execute(_pr, _dr, "なりきり")
check("特性コピー(自分): なりきり", _pr.ability == "ちょすい", f"自{_pr.ability}")

# ── どろかけ ──
check("DB: どろかけ 取得可能", dl.get_move("どろかけ") is not None)
_mv_どろかけ = dl.get_move("どろかけ")
if _mv_どろかけ:
    _pa_どろかけ = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_どろかけ = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_どろかけ = dmg(_pa_どろかけ, _pd_どろかけ, "どろかけ")
    check("ダメージ計算: どろかけ", _d_どろかけ > 0, f"dmg={_d_どろかけ}")
# どろかけ: 相手命中率-1
_mv_dd_どろかけ = dl.get_move("どろかけ")
if _mv_dd_どろかけ:
    _pa_dd = make_poke(type1="じめん", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_どろかけ = 0; _dd_ok_どろかけ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="でんき", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "どろかけ")
        if _pd_dd.stage_accuracy != 0: _dd_val_どろかけ = _pd_dd.stage_accuracy; _dd_ok_どろかけ = True; break
    check("相手命中率-1: どろかけ", _dd_ok_どろかけ and _dd_val_どろかけ == -1, f"1回適用={_dd_val_どろかけ} 期待=-1")

# ── のみこむ ──
check("DB: のみこむ 取得可能", dl.get_move("のみこむ") is not None)
# のみこむ: たくわえ消費でHP回復、たくわえ0だと失敗
_pno = make_poke(type1="ノーマル", hp_b=200); _pno.hp = 30; execute(_pno, make_poke(), "のみこむ")
check("たくわえ0で失敗: のみこむ", _pno.hp == 30, f"hp={_pno.hp}")
_pno2 = make_poke(type1="ノーマル", hp_b=200); _pno2.hp = 30; _pno2.stockpile_count = 2; execute(_pno2, make_poke(), "のみこむ")
check("たくわえ消費回復: のみこむ", _pno2.hp > 30 and _pno2.stockpile_count == 0, f"hp={_pno2.hp} sc={_pno2.stockpile_count}")

# ── ねをはる ──
check("DB: ねをはる 取得可能", dl.get_move("ねをはる") is not None)
# ねをはる: 毎ターン1/16回復
_prt = make_poke(hp_b=200); _prt.hp = 50; execute(_prt, make_poke(), "ねをはる")
check("ねをはるフラグ: ねをはる", _prt.rooted)
from simulator.battle import Battle as _B
_b = _B(BattleSide([_prt]), BattleSide([make_poke()])); _hp0 = _prt.hp
_b._end_of_turn()
check("ねをはる ターン終了回復: ねをはる", _prt.hp > _hp0, f"hp={_prt.hp}")

# ── ハイドロカノン ──
check("DB: ハイドロカノン 取得可能", dl.get_move("ハイドロカノン") is not None)
_mv_ハイドロカノン = dl.get_move("ハイドロカノン")
if _mv_ハイドロカノン:
    _pa_ハイドロカノン = make_poke(type1="みず", atk_b=100, spatk_b=100)
    _pd_ハイドロカノン = make_poke(type1="ほのお", def_b=100, spdef_b=100)
    _d_ハイドロカノン = dmg(_pa_ハイドロカノン, _pd_ハイドロカノン, "ハイドロカノン")
    check("ダメージ計算: ハイドロカノン", _d_ハイドロカノン > 0, f"dmg={_d_ハイドロカノン}")
# ハイドロカノン: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="みず", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="ほのお", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "ハイドロカノン")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: ハイドロカノン", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="みず", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="ほのお", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "ハイドロカノン")
check("リチャージ中行動不能: ハイドロカノン", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── はきだす ──
check("DB: はきだす 取得可能", dl.get_move("はきだす") is not None)
# はきだす: たくわえ0だと失敗、たくわえ有りでダメージ
_phk = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _dhk = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)
_hphk = _dhk.hp; execute(_phk, _dhk, "はきだす")
check("たくわえ0で失敗: はきだす", _dhk.hp == _hphk, f"hp={_dhk.hp}/{_hphk}")
_phk2 = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _phk2.stockpile_count = 2; _dhk2 = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)
_hphk2 = _dhk2.hp; execute(_phk2, _dhk2, "はきだす")
check("たくわえ消費攻撃: はきだす", _dhk2.hp < _hphk2 and _phk2.stockpile_count == 0, f"hp={_dhk2.hp}/{_hphk2} sc={_phk2.stockpile_count}")

# ── はなふぶき ──
check("DB: はなふぶき 取得可能", dl.get_move("はなふぶき") is not None)
_mv_はなふぶき = dl.get_move("はなふぶき")
if _mv_はなふぶき:
    _pa_はなふぶき = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_はなふぶき = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_はなふぶき = dmg(_pa_はなふぶき, _pd_はなふぶき, "はなふぶき")
    check("ダメージ計算: はなふぶき", _d_はなふぶき > 0, f"dmg={_d_はなふぶき}")

# ── ハバネロエキス ──
check("DB: ハバネロエキス 取得可能", dl.get_move("ハバネロエキス") is not None)
# ハバネロエキス: 相手の防御-2・攻撃+2
_phb = make_poke(); _dhb = make_poke(hp_b=200); execute(_phb, _dhb, "ハバネロエキス")
check("相手防御-2攻撃+2: ハバネロエキス", _dhb.stage_defense == -2 and _dhb.stage_attack == 2, f"def={_dhb.stage_defense} atk={_dhb.stage_attack}")

# ── ハロウィン ──
check("DB: ハロウィン 取得可能", dl.get_move("ハロウィン") is not None)
# ハロウィン: 相手にゴーストタイプを追加
_pha = make_poke(); _dha = make_poke(type1="ノーマル", type2=None); execute(_pha, _dha, "ハロウィン")
check("タイプ追加(ゴースト): ハロウィン", "ゴースト" in (_dha.type1, _dha.type2), f"type={_dha.type1}/{_dha.type2}")

# ── パワーシェア ──
check("DB: パワーシェア 取得可能", dl.get_move("パワーシェア") is not None)
# パワーシェア: 攻撃・特攻を平均化
_pps = make_poke(atk_b=200); _dps = make_poke(atk_b=20)
_expp = (_pps.attack + _dps.attack)//2
execute(_pps, _dps, "パワーシェア")
check("パワーシェア 攻撃平均化: パワーシェア", _pps.attack == _expp and _dps.attack == _expp)

# ── パワートリック ──
check("DB: パワートリック 取得可能", dl.get_move("パワートリック") is not None)
# パワートリック: 攻撃と防御を入替
_ppt = make_poke(atk_b=120, def_b=40); _a0, _d0 = _ppt.attack, _ppt.defense
execute(_ppt, make_poke(), "パワートリック")
check("パワートリック 攻防入替: パワートリック", _ppt.attack == _d0 and _ppt.defense == _a0)

# ── ハードプラント ──
check("DB: ハードプラント 取得可能", dl.get_move("ハードプラント") is not None)
_mv_ハ_ドプラント = dl.get_move("ハードプラント")
if _mv_ハ_ドプラント:
    _pa_ハ_ドプラント = make_poke(type1="くさ", atk_b=100, spatk_b=100)
    _pd_ハ_ドプラント = make_poke(type1="みず", def_b=100, spdef_b=100)
    _d_ハ_ドプラント = dmg(_pa_ハ_ドプラント, _pd_ハ_ドプラント, "ハードプラント")
    check("ダメージ計算: ハードプラント", _d_ハ_ドプラント > 0, f"dmg={_d_ハ_ドプラント}")
# ハードプラント: 使用後リチャージ付与 + リチャージ中は行動不能
random.seed(0); _rc_ok2 = False
for _ in range(20):
    _prc2 = make_poke(type1="くさ", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100)
    execute(_prc2, _drc2, "ハードプラント")
    if _prc2.recharge: _rc_ok2 = True; break
check("リチャージ付与: ハードプラント", _rc_ok2)
# リチャージ中は行動不能（相手にダメージが通らない）
_prc3 = make_poke(type1="くさ", atk_b=150, spatk_b=150); _prc3.recharge = True
_drc3 = make_poke(type1="みず", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp
execute(_prc3, _drc3, "ハードプラント")
check("リチャージ中行動不能: ハードプラント", _drc3.hp == _hprc3, f"hp={_drc3.hp}/{_hprc3}")

# ── ファストガード ──
check("DB: ファストガード 取得可能", dl.get_move("ファストガード") is not None)
# ファストガード: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: ファストガード", "ファストガード", "かくとう", False, smoke=("ファストガード" in DOUBLE_ONLY_SMOKE))

# ── フェアリーロック ──
check("DB: フェアリーロック 取得可能", dl.get_move("フェアリーロック") is not None)
# フェアリーロック: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: フェアリーロック", "フェアリーロック", "フェアリー", False, smoke=("フェアリーロック" in DOUBLE_ONLY_SMOKE))

# ── ぶきみなじゅもん ──
check("DB: ぶきみなじゅもん 取得可能", dl.get_move("ぶきみなじゅもん") is not None)
_mv_ぶきみなじゅもん = dl.get_move("ぶきみなじゅもん")
if _mv_ぶきみなじゅもん:
    _pa_ぶきみなじゅもん = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_ぶきみなじゅもん = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_ぶきみなじゅもん = dmg(_pa_ぶきみなじゅもん, _pd_ぶきみなじゅもん, "ぶきみなじゅもん")
    check("ダメージ計算: ぶきみなじゅもん", _d_ぶきみなじゅもん > 0, f"dmg={_d_ぶきみなじゅもん}")
# ぶきみなじゅもん: 相手の最後の技のPPを3減らす
_ppp = make_poke(spatk_b=10, atk_b=10); _dpp = make_poke(moves=["たいあたり"], hp_b=255, def_b=255, spdef_b=255); _dpp.last_used_move = "たいあたり"; _dpp.pp = [20]
execute(_ppp, _dpp, "ぶきみなじゅもん")
check("PP減少: ぶきみなじゅもん", _dpp.pp[0] == 20 - 3, f"pp={_dpp.pp[0]}")

# ── ふくろだたき ──
check("DB: ふくろだたき 取得可能", dl.get_move("ふくろだたき") is not None)
# ふくろだたき: 手持ちの数だけ攻撃（1v1でも発動しダメージ）
_pfd = make_poke(type1="あく", atk_b=120); _dfd = make_poke(type1="エスパー", hp_b=255, def_b=120)
_hpfd = _dfd.hp; execute(_pfd, _dfd, "ふくろだたき")
check("ふくろだたき発動: ふくろだたき", _dfd.hp < _hpfd, f"hp={_dfd.hp}/{_hpfd}")

# ── ふしょくガス ──
check("DB: ふしょくガス 取得可能", dl.get_move("ふしょくガス") is not None)
# ふしょくガス: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: ふしょくガス", "ふしょくガス", "どく", True, smoke=("ふしょくガス" in DOUBLE_ONLY_SMOKE))

# ── フラフラダンス ──
check("DB: フラフラダンス 取得可能", dl.get_move("フラフラダンス") is not None)
# フラフラダンス: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: フラフラダンス", "フラフラダンス", "ノーマル", True, smoke=("フラフラダンス" in DOUBLE_ONLY_SMOKE))

# ── ベノムショック ──
check("DB: ベノムショック 取得可能", dl.get_move("ベノムショック") is not None)
_mv_ベノムショック = dl.get_move("ベノムショック")
if _mv_ベノムショック:
    _pa_ベノムショック = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_ベノムショック = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_ベノムショック = dmg(_pa_ベノムショック, _pd_ベノムショック, "ベノムショック")
    check("ダメージ計算: ベノムショック", _d_ベノムショック > 0, f"dmg={_d_ベノムショック}")
# ベノムショック: 相手状態異常で威力2倍
_pcp = make_poke(type1="どく", atk_b=100, spatk_b=100)
_dn1 = make_poke(type1="くさ", def_b=100, spdef_b=100)
_dn2 = make_poke(type1="くさ", def_b=100, spdef_b=100); _dn2.status = "badpoison"
_pn = _ep(_pcp, _dn1, dl.get_move("ベノムショック"), BattleField())
_pd = _ep(_pcp, _dn2, dl.get_move("ベノムショック"), BattleField())
check("状態異常で威力2倍: ベノムショック", _pd == _pn * 2, f"normal={_pn} status={_pd}")

# ── ボーンラッシュ ──
check("DB: ボーンラッシュ 取得可能", dl.get_move("ボーンラッシュ") is not None)
_mv_ボ_ンラッシュ = dl.get_move("ボーンラッシュ")
if _mv_ボ_ンラッシュ:
    _pa_ボ_ンラッシュ = make_poke(type1="じめん", atk_b=100, spatk_b=100)
    _pd_ボ_ンラッシュ = make_poke(type1="でんき", def_b=100, spdef_b=100)
    _d_ボ_ンラッシュ = dmg(_pa_ボ_ンラッシュ, _pd_ボ_ンラッシュ, "ボーンラッシュ")
    check("ダメージ計算: ボーンラッシュ", _d_ボ_ンラッシュ > 0, f"dmg={_d_ボ_ンラッシュ}")
# ボーンラッシュ: 多段ヒット（合計が単発を上回る＝複数回当たっている）
_mvmh_ボ_ンラッシュ = dl.get_move("ボーンラッシュ")
if _mvmh_ボ_ンラッシュ:
    _pam = make_poke(type1="じめん", atk_b=120, spatk_b=120, ability="スキルリンク")
    _single_ボ_ンラッシュ = calc_damage(_pam, make_poke(type1="でんき", hp_b=255, def_b=200, spdef_b=200), _mvmh_ボ_ンラッシュ, BattleField(), random_roll=1.0)
    random.seed(0); _multi_ボ_ンラッシュ = 0
    for _ in range(20):
        _pdm = make_poke(type1="でんき", hp_b=255, def_b=200, spdef_b=200)
        execute(_pam, _pdm, "ボーンラッシュ"); _multi_ボ_ンラッシュ = _pdm.max_hp - _pdm.hp
        if _multi_ボ_ンラッシュ > _single_ボ_ンラッシュ: break
    check("多段ヒット発生(複数回): ボーンラッシュ", _multi_ボ_ンラッシュ > _single_ボ_ンラッシュ, f"single={_single_ボ_ンラッシュ} multi={_multi_ボ_ンラッシュ}")

# ── マジックルーム ──
check("DB: マジックルーム 取得可能", dl.get_move("マジックルーム") is not None)
# マジックルーム: 場の状態セット
_s1rm, _s2rm, _frm = execute_ctx(make_poke(type1="エスパー"), make_poke(), "マジックルーム")
check("マジックルーム 場の状態: マジックルーム", bool(getattr(_frm, "magic_room", 0)))

# ── まほうのこな ──
check("DB: まほうのこな 取得可能", dl.get_move("まほうのこな") is not None)
# まほうのこな: 相手をエスパー化。くさタイプには無効（粉）
_pmp = make_poke(type1="エスパー"); _dmp = make_poke(type1="ノーマル", hp_b=200)
for _ in range(20): execute(_pmp, _dmp, "まほうのこな")
check("エスパータイプ化: まほうのこな", _dmp.type1 == "エスパー", f"type={_dmp.type1}")
_dmp2 = make_poke(type1="くさ", hp_b=200); execute(_pmp, _dmp2, "まほうのこな")
check("くさ無効: まほうのこな", _dmp2.type1 == "くさ", f"type={_dmp2.type1}")

# ── みらいよち ──
check("DB: みらいよち 取得可能", dl.get_move("みらいよち") is not None)
_mv_みらいよち = dl.get_move("みらいよち")
if _mv_みらいよち:
    _pa_みらいよち = make_poke(type1="エスパー", atk_b=100, spatk_b=100)
    _pd_みらいよち = make_poke(type1="かくとう", def_b=100, spdef_b=100)
    _d_みらいよち = dmg(_pa_みらいよち, _pd_みらいよち, "みらいよち")
    check("ダメージ計算: みらいよち", _d_みらいよち > 0, f"dmg={_d_みらいよち}")
# みらいよち: 使用すると予約が立ち（arising・手動セットしない）、満了ターンで発動
from simulator.battle import Battle as _Bfs
_pfs = make_poke(type1="エスパー", spatk_b=150, moves=["みらいよち"])
_ffs = make_poke(type1="ノーマル", hp_b=255, spdef_b=80, moves=["たいあたり"])
_bfs = _Bfs(BattleSide([_pfs]), BattleSide([_ffs])); _s2 = _bfs.side2
# 使用 → 予約成立（future_sight_count が立つことを実機で確認）
_execute_move(_bfs.side1, _bfs.side2, Action(type="move", move=dl.get_move("みらいよち"), move_idx=0), _bfs.field)
check("使用で予約成立(arising): みらいよち", getattr(_s2, "future_sight_count", 0) > 0, f"count={getattr(_s2,'future_sight_count',0)}")
_hp_ffs = _ffs.hp; _n_fs = _s2.future_sight_count
# 予約中ターンは本体ダメージなし、満了ターンで発動
for _ in range(_n_fs - 1): _bfs._end_of_turn()
_mid = _ffs.hp; _bfs._end_of_turn()
check("みらいよち遅延発動: みらいよち", _mid == _hp_ffs and _ffs.hp < _hp_ffs, f"mid={_mid} end={_ffs.hp}/{_hp_ffs}")

# ── ミラータイプ ──
check("DB: ミラータイプ 取得可能", dl.get_move("ミラータイプ") is not None)
# ミラータイプ: 自分のタイプを相手と同じに
_pmt = make_poke(type1="ノーマル"); _dmt = make_poke(type1="みず", type2="ひこう")
execute(_pmt, _dmt, "ミラータイプ")
check("ミラータイプコピー: ミラータイプ", _pmt.type1 == "みず" and _pmt.type2 == "ひこう", f"type={_pmt.type1}/{_pmt.type2}")

# ── むしのていこう ──
check("DB: むしのていこう 取得可能", dl.get_move("むしのていこう") is not None)
_mv_むしのていこう = dl.get_move("むしのていこう")
if _mv_むしのていこう:
    _pa_むしのていこう = make_poke(type1="むし", atk_b=100, spatk_b=100)
    _pd_むしのていこう = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_むしのていこう = dmg(_pa_むしのていこう, _pd_むしのていこう, "むしのていこう")
    check("ダメージ計算: むしのていこう", _d_むしのていこう > 0, f"dmg={_d_むしのていこう}")
# むしのていこう: 相手特攻-1
_mv_dd_むしのていこう = dl.get_move("むしのていこう")
if _mv_dd_むしのていこう:
    _pa_dd = make_poke(type1="むし", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_むしのていこう = 0; _dd_ok_むしのていこう = False
    for _ in range(60):
        _pd_dd = make_poke(type1="くさ", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "むしのていこう")
        if _pd_dd.stage_sp_attack != 0: _dd_val_むしのていこう = _pd_dd.stage_sp_attack; _dd_ok_むしのていこう = True; break
    check("相手特攻-1: むしのていこう", _dd_ok_むしのていこう and _dd_val_むしのていこう == -1, f"1回適用={_dd_val_むしのていこう} 期待=-1")

# ── メテオビーム ──
check("DB: メテオビーム 取得可能", dl.get_move("メテオビーム") is not None)
_mv_メテオビ_ム = dl.get_move("メテオビーム")
if _mv_メテオビ_ム:
    _pa_メテオビ_ム = make_poke(type1="いわ", atk_b=100, spatk_b=100)
    _pd_メテオビ_ム = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    random.seed(0)
    for _ in range(10):
        _pa_メテオビ_ム = make_poke(type1="いわ", atk_b=100, spatk_b=100); _pd_メテオビ_ム = make_poke(type1="ひこう", def_b=100, spdef_b=100)
        execute(_pa_メテオビ_ム, _pd_メテオビ_ム, "メテオビーム"); execute(_pa_メテオビ_ム, _pd_メテオビ_ム, "メテオビーム")
        if _pd_メテオビ_ム.hp < _pd_メテオビ_ム.max_hp: break
    check("ダメージ計算: メテオビーム", _pd_メテオビ_ム.hp < _pd_メテオビ_ム.max_hp, f"hp={_pd_メテオビ_ム.hp}")
# メテオビーム: 2ターン溜め
_mv_2t_メテオビ_ム = dl.get_move("メテオビーム")
if _mv_2t_メテオビ_ム:
    _pa_2t = make_poke(type1="いわ", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="ひこう", def_b=100, spdef_b=100)
    _hp_before_2t = _pd_2t.hp
    execute(_pa_2t, _pd_2t, "メテオビーム")
    check("2ターン溜め(1T)ダメなし: メテオビーム", _pd_2t.hp == _hp_before_2t)
    check("2ターン溜め(1T)charging: メテオビーム", _pa_2t.charging_move == "メテオビーム")
    random.seed(0)
    for _ in range(10):
        execute(_pa_2t, _pd_2t, "メテオビーム")
        if _pd_2t.hp < _hp_before_2t: break
        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "メテオビーム")
    check("2ターン溜め(2T)ダメあり: メテオビーム", _pd_2t.hp < _hp_before_2t)
# メテオビーム: 溜めターン自己特攻+1
_mvcb_メテオビ_ム = dl.get_move("メテオビーム")
if _mvcb_メテオビ_ム:
    _pacb = make_poke(type1="いわ", atk_b=60, spatk_b=60); _pdcb = make_poke(type1="ひこう", hp_b=255)
    execute(_pacb, _pdcb, "メテオビーム")  # 溜めターン
    check("溜め自己特攻+1: メテオビーム", _pacb.stage_sp_attack >= 1, f"stage={_pacb.stage_sp_attack}")

# ── メロメロ ──
check("DB: メロメロ 取得可能", dl.get_move("メロメロ") is not None)
# メロメロ: 性別未実装のため常に失敗（infatuationは付与されない）
_pml = make_poke(type1="ノーマル"); _dml = make_poke(type1="ノーマル", hp_b=200)
execute(_pml, _dml, "メロメロ")
check("メロメロ: メロメロ", not _dml.infatuation, f"infatuation={_dml.infatuation}")

# ── もりののろい ──
check("DB: もりののろい 取得可能", dl.get_move("もりののろい") is not None)
# もりののろい: 相手にくさタイプを追加
_pha = make_poke(); _dha = make_poke(type1="ノーマル", type2=None); execute(_pha, _dha, "もりののろい")
check("タイプ追加(くさ): もりののろい", "くさ" in (_dha.type1, _dha.type2), f"type={_dha.type1}/{_dha.type2}")

# ── ゆきげしき ──
check("DB: ゆきげしき 取得可能", dl.get_move("ゆきげしき") is not None)
# ゆきげしき: 天候hail
_mv_w_ゆきげしき = dl.get_move("ゆきげしき")
if _mv_w_ゆきげしき:
    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="こおり"), make_poke(), "ゆきげしき")
    check("天候hail: ゆきげしき", _fw.weather == "hail", f"weather={_fw.weather}")

# ── りんしょう ──
check("DB: りんしょう 取得可能", dl.get_move("りんしょう") is not None)
_mv_りんしょう = dl.get_move("りんしょう")
if _mv_りんしょう:
    _pa_りんしょう = make_poke(type1="ノーマル", atk_b=100, spatk_b=100)
    _pd_りんしょう = make_poke(type1="ノーマル", def_b=100, spdef_b=100)
    _d_りんしょう = dmg(_pa_りんしょう, _pd_りんしょう, "りんしょう")
    check("ダメージ計算: りんしょう", _d_りんしょう > 0, f"dmg={_d_りんしょう}")

# ── れんごく ──
check("DB: れんごく 取得可能", dl.get_move("れんごく") is not None)
_mv_れんごく = dl.get_move("れんごく")
if _mv_れんごく:
    _pa_れんごく = make_poke(type1="ほのお", atk_b=100, spatk_b=100)
    _pd_れんごく = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_れんごく = dmg(_pa_れんごく, _pd_れんごく, "れんごく")
    check("ダメージ計算: れんごく", _d_れんごく > 0, f"dmg={_d_れんごく}")
# れんごく: やけど100%
_mv_s_れんごく = dl.get_move("れんごく")
if _mv_s_れんごく:
    random.seed(0); _hit_れんごく = 0
    for _ in range(300):
        _pa2 = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "れんごく")
        _hit_れんごく += int((_pd2.status == "burn"))
    check("追加効果(やけど100%): れんごく", 90 <= _hit_れんごく <= 525, f"count={_hit_れんごく}/300")
    random.seed(1); _immok_れんごく = True
    for _ in range(60):
        _pai = make_poke(type1="ほのお", atk_b=30, spatk_b=30); _pdi = make_poke(type1="ほのお", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "れんごく")
        if _pdi.status == "burn": _immok_れんごく = False; break
    check("やけど免疫(ほのお型には無効): れんごく", _immok_れんごく, "免疫タイプに状態異常が付与されないこと")

# ── ロックオン ──
check("DB: ロックオン 取得可能", dl.get_move("ロックオン") is not None)
# ロックオン: 次の技が必中
_plo = make_poke(type1="ノーマル", atk_b=100); execute(_plo, make_poke(), "ロックオン")
check("ロックオンフラグ: ロックオン", _plo.lock_on)
import copy as _cp2; _mvlo = _cp2.copy(dl.get_move("でんじは") or dl.get_move("たいあたり")); _mvlo.accuracy = 1
_dlo = make_poke(type1="ノーマル", hp_b=255); _hplo = _dlo.hp; random.seed(0)
from simulator.damage import check_hit as _ch
check("ロックオン必中: ロックオン", all(_ch(_plo, _dlo, _mvlo, BattleField()) for _ in range(20)))

# ── ワイドガード ──
check("DB: ワイドガード 取得可能", dl.get_move("ワイドガード") is not None)
# ワイドガード: 副作用検証（status技フォールバック）
side_effect_check("副作用発現: ワイドガード", "ワイドガード", "いわ", False, smoke=("ワイドガード" in DOUBLE_ONLY_SMOKE))

# ── ワンダールーム ──
check("DB: ワンダールーム 取得可能", dl.get_move("ワンダールーム") is not None)
# ワンダールーム: 場の状態セット
_s1rm, _s2rm, _frm = execute_ctx(make_poke(type1="エスパー"), make_poke(), "ワンダールーム")
check("ワンダールーム 場の状態: ワンダールーム", bool(getattr(_frm, "wonder_room", 0)))

# ── ゴールドラッシュ ──
check("DB: ゴールドラッシュ 取得可能", dl.get_move("ゴールドラッシュ") is not None)
_mv_ゴ_ルドラッシュ = dl.get_move("ゴールドラッシュ")
if _mv_ゴ_ルドラッシュ:
    _pa_ゴ_ルドラッシュ = make_poke(type1="はがね", atk_b=100, spatk_b=100)
    _pd_ゴ_ルドラッシュ = make_poke(type1="こおり", def_b=100, spdef_b=100)
    _d_ゴ_ルドラッシュ = dmg(_pa_ゴ_ルドラッシュ, _pd_ゴ_ルドラッシュ, "ゴールドラッシュ")
    check("ダメージ計算: ゴールドラッシュ", _d_ゴ_ルドラッシュ > 0, f"dmg={_d_ゴ_ルドラッシュ}")
# ゴールドラッシュ: 自分特攻-1
_mvss_ゴ_ルドラッシュ_sp_attack = dl.get_move("ゴールドラッシュ")
if _mvss_ゴ_ルドラッシュ_sp_attack:
    random.seed(0); _got_ゴ_ルドラッシュ_sp_attack = 0
    for _ in range(60):
        _pas = make_poke(type1="はがね", atk_b=60, spatk_b=60); _pds = make_poke(type1="こおり", hp_b=255, def_b=255, spdef_b=255)
        execute(_pas, _pds, "ゴールドラッシュ")
        if _pas.stage_sp_attack != 0: _got_ゴ_ルドラッシュ_sp_attack = _pas.stage_sp_attack; break
    check("自分特攻-1: ゴールドラッシュ", _got_ゴ_ルドラッシュ_sp_attack == -1, f"1回適用={_got_ゴ_ルドラッシュ_sp_attack} 期待=-1")

# ── ソウルクラッシュ ──
check("DB: ソウルクラッシュ 取得可能", dl.get_move("ソウルクラッシュ") is not None)
_mv_ソウルクラッシュ = dl.get_move("ソウルクラッシュ")
if _mv_ソウルクラッシュ:
    _pa_ソウルクラッシュ = make_poke(type1="フェアリー", atk_b=100, spatk_b=100)
    _pd_ソウルクラッシュ = make_poke(type1="ドラゴン", def_b=100, spdef_b=100)
    _d_ソウルクラッシュ = dmg(_pa_ソウルクラッシュ, _pd_ソウルクラッシュ, "ソウルクラッシュ")
    check("ダメージ計算: ソウルクラッシュ", _d_ソウルクラッシュ > 0, f"dmg={_d_ソウルクラッシュ}")
# ソウルクラッシュ: 相手特攻-1
_mv_dd_ソウルクラッシュ = dl.get_move("ソウルクラッシュ")
if _mv_dd_ソウルクラッシュ:
    _pa_dd = make_poke(type1="フェアリー", atk_b=30, spatk_b=30)
    random.seed(0); _dd_val_ソウルクラッシュ = 0; _dd_ok_ソウルクラッシュ = False
    for _ in range(60):
        _pd_dd = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)
        execute(_pa_dd, _pd_dd, "ソウルクラッシュ")
        if _pd_dd.stage_sp_attack != 0: _dd_val_ソウルクラッシュ = _pd_dd.stage_sp_attack; _dd_ok_ソウルクラッシュ = True; break
    check("相手特攻-1: ソウルクラッシュ", _dd_ok_ソウルクラッシュ and _dd_val_ソウルクラッシュ == -1, f"1回適用={_dd_val_ソウルクラッシュ} 期待=-1")

# ── ふんどのこぶし ──
check("DB: ふんどのこぶし 取得可能", dl.get_move("ふんどのこぶし") is not None)
_mv_ふんどのこぶし = dl.get_move("ふんどのこぶし")
if _mv_ふんどのこぶし:
    _pa_ふんどのこぶし = make_poke(type1="ゴースト", atk_b=100, spatk_b=100)
    _pd_ふんどのこぶし = make_poke(type1="エスパー", def_b=100, spdef_b=100)
    _d_ふんどのこぶし = dmg(_pa_ふんどのこぶし, _pd_ふんどのこぶし, "ふんどのこぶし")
    check("ダメージ計算: ふんどのこぶし", _d_ふんどのこぶし > 0, f"dmg={_d_ふんどのこぶし}")
# ふんどのこぶし: 攻撃技で受けた回数(times_hit)×50 威力上昇(上限350)
_pf = make_poke(type1="ゴースト", atk_b=100); _df = make_poke(def_b=100)
_pf.times_hit = 0; _f0 = _ep(_pf, _df, dl.get_move("ふんどのこぶし"), BattleField())
_pf.times_hit = 3; _f3 = _ep(_pf, _df, dl.get_move("ふんどのこぶし"), BattleField())
_pf.times_hit = 10; _f10 = _ep(_pf, _df, dl.get_move("ふんどのこぶし"), BattleField())
check("被弾0で威力50: ふんどのこぶし", _f0 == 50, f"0={_f0}")
check("被弾3で威力200(50+50×3): ふんどのこぶし", _f3 == 200, f"3={_f3}")
check("被弾上限6で威力350: ふんどのこぶし", _f10 == 350, f"max={_f10}")

# ── はいすいのじん ──
check("DB: はいすいのじん 取得可能", dl.get_move("はいすいのじん") is not None)
# はいすいのじん: 自分攻撃+1
_mv_sb_はいすいのじん_attack = dl.get_move("はいすいのじん")
if _mv_sb_はいすいのじん_attack:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "はいすいのじん")
    check("自分攻撃+1: はいすいのじん", _pa_sb.stage_attack == 1, f"1回適用={_pa_sb.stage_attack} 期待=+1")
# はいすいのじん: 自分防御+1
_mv_sb_はいすいのじん_defense = dl.get_move("はいすいのじん")
if _mv_sb_はいすいのじん_defense:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "はいすいのじん")
    check("自分防御+1: はいすいのじん", _pa_sb.stage_defense == 1, f"1回適用={_pa_sb.stage_defense} 期待=+1")
# はいすいのじん: 自分特攻+1
_mv_sb_はいすいのじん_sp_attack = dl.get_move("はいすいのじん")
if _mv_sb_はいすいのじん_sp_attack:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "はいすいのじん")
    check("自分特攻+1: はいすいのじん", _pa_sb.stage_sp_attack == 1, f"1回適用={_pa_sb.stage_sp_attack} 期待=+1")
# はいすいのじん: 自分特防+1
_mv_sb_はいすいのじん_sp_defense = dl.get_move("はいすいのじん")
if _mv_sb_はいすいのじん_sp_defense:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "はいすいのじん")
    check("自分特防+1: はいすいのじん", _pa_sb.stage_sp_defense == 1, f"1回適用={_pa_sb.stage_sp_defense} 期待=+1")
# はいすいのじん: 自分素早さ+1
_mv_sb_はいすいのじん_speed = dl.get_move("はいすいのじん")
if _mv_sb_はいすいのじん_speed:
    _pa_sb = make_poke(type1="かくとう"); _pd_sb = make_poke()
    execute(_pa_sb, _pd_sb, "はいすいのじん")
    check("自分素早さ+1: はいすいのじん", _pa_sb.stage_speed == 1, f"1回適用={_pa_sb.stage_speed} 期待=+1")
# はいすいのじん: 全能力+1かつ自分が交代不可になる。すでに交代不可なら失敗
_ph = make_poke(type1="かくとう"); execute(_ph, make_poke(), "はいすいのじん")
check("使用後に交代不可: はいすいのじん", _ph.trapped, f"trapped={_ph.trapped}")
_ph2 = make_poke(type1="かくとう"); _ph2.trapped = True; execute(_ph2, make_poke(), "はいすいのじん")
check("すでに交代不可なら失敗(能力上がらない): はいすいのじん", _ph2.stage_attack == 0, f"atk={_ph2.stage_attack}")

# ── どくばりセンボン ──
check("DB: どくばりセンボン 取得可能", dl.get_move("どくばりセンボン") is not None)
_mv_どくばりセンボン = dl.get_move("どくばりセンボン")
if _mv_どくばりセンボン:
    _pa_どくばりセンボン = make_poke(type1="どく", atk_b=100, spatk_b=100)
    _pd_どくばりセンボン = make_poke(type1="くさ", def_b=100, spdef_b=100)
    _d_どくばりセンボン = dmg(_pa_どくばりセンボン, _pd_どくばりセンボン, "どくばりセンボン")
    check("ダメージ計算: どくばりセンボン", _d_どくばりセンボン > 0, f"dmg={_d_どくばりセンボン}")
# どくばりセンボン: どく50%
_mv_s_どくばりセンボン = dl.get_move("どくばりセンボン")
if _mv_s_どくばりセンボン:
    random.seed(0); _hit_どくばりセンボン = 0
    for _ in range(300):
        _pa2 = make_poke(type1="どく", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="くさ", def_b=255, spdef_b=255, hp_b=255)
        execute(_pa2, _pd2, "どくばりセンボン")
        _hit_どくばりセンボン += int((_pd2.status == "poison"))
    check("追加効果(どく50%): どくばりセンボン", 45 <= _hit_どくばりセンボン <= 270, f"count={_hit_どくばりセンボン}/300")
    random.seed(1); _immok_どくばりセンボン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="どく", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくばりセンボン")
        if _pdi.status == "poison": _immok_どくばりセンボン = False; break
    check("どく免疫(どく型には無効): どくばりセンボン", _immok_どくばりセンボン, "免疫タイプに状態異常が付与されないこと")
    random.seed(1); _immok_どくばりセンボン = True
    for _ in range(60):
        _pai = make_poke(type1="どく", atk_b=30, spatk_b=30); _pdi = make_poke(type1="はがね", def_b=255, spdef_b=255, hp_b=255)
        execute(_pai, _pdi, "どくばりセンボン")
        if _pdi.status == "poison": _immok_どくばりセンボン = False; break
    check("どく免疫(はがね型には無効): どくばりセンボン", _immok_どくばりセンボン, "免疫タイプに状態異常が付与されないこと")
# どくばりセンボン: 相手状態異常で威力2倍
_pcp = make_poke(type1="どく", atk_b=100, spatk_b=100)
_dn1 = make_poke(type1="くさ", def_b=100, spdef_b=100)
_dn2 = make_poke(type1="くさ", def_b=100, spdef_b=100); _dn2.status = "poison"
_pn = _ep(_pcp, _dn1, dl.get_move("どくばりセンボン"), BattleField())
_pd = _ep(_pcp, _dn2, dl.get_move("どくばりセンボン"), BattleField())
check("状態異常で威力2倍: どくばりセンボン", _pd == _pn * 2, f"normal={_pn} status={_pd}")


print(f'\n全技テスト: {PASS}件PASS / {FAIL}件FAIL (計{PASS+FAIL}件)')
if FAILURES:
    for f in FAILURES[:20]: print(f'  {f}')
    if len(FAILURES) > 20: print(f'  ...他{len(FAILURES)-20}件')
else:
    print('✅ 全テストパス')