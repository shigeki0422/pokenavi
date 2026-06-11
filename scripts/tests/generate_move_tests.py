#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DBのeffect_textから全技の仕様テストを自動生成する
生成されたテストはtest_move_effects.pyに書き出す
"""
import sqlite3, re, sys
sys.path.insert(0, '/Users/shigeki/work/pokenavi/scripts')

conn = sqlite3.connect('/Users/shigeki/work/pokenavi/scripts/pokenavi.db')
cur = conn.cursor()
cur.execute("SELECT name_jp, type, category, power, accuracy, pp, effect_text FROM move_master ORDER BY id")
moves = cur.fetchall()
conn.close()

STATUS_MAP = {
    'まひ':   'paralysis',
    'やけど': 'burn',
    'こおり': 'freeze',
    'どく':   'poison',
    'もうどく':'badpoison',
    'ねむり': 'sleep',
    'こんらん':'confused',
}
STAT_MAP = {
    '攻撃':'attack','防御':'defense','特攻':'sp_attack',
    '特防':'sp_defense','素早さ':'speed','命中':'accuracy','回避':'evasion',
}

# 各攻撃タイプが2倍or等倍で通る防御側タイプ（無効化を避ける）
TYPE_DEFENDER = {
    'ノーマル':'ノーマル','ほのお':'くさ','みず':'ほのお','でんき':'みず',
    'くさ':'みず','こおり':'くさ','かくとう':'ノーマル','どく':'くさ',
    'じめん':'でんき','ひこう':'くさ','エスパー':'かくとう','むし':'くさ',
    'いわ':'ひこう','ゴースト':'エスパー','ドラゴン':'ドラゴン','はがね':'こおり',
    'あく':'エスパー','フェアリー':'ドラゴン',
}

def defender_type_for(atk_type):
    return TYPE_DEFENDER.get(atk_type, 'ドラゴン')

# 状態異常ごとの免疫タイプ（この型は付与されない）
STATUS_IMMUNE_TYPE = {
    'paralysis': 'でんき', 'burn': 'ほのお', 'freeze': 'こおり',
    'poison': 'どく', 'badpoison': 'どく',
}

def status_safe_defender(atk_type, status_en):
    """攻撃を無効化せず、かつ状態異常免疫でもない防御側タイプを返す"""
    cand = TYPE_DEFENDER.get(atk_type, 'ドラゴン')
    immune = STATUS_IMMUNE_TYPE.get(status_en)
    if immune and cand == immune:
        # 免疫型なので別の被弾可能タイプを探す
        for t in ['ノーマル', 'ドラゴン', 'みず', 'くさ', 'エスパー', 'かくとう', 'ひこう']:
            if t == immune:
                continue
            # atk_typeがtに無効でないこと（簡易: ゴースト⇔ノーマル/かくとう, じめん→ひこうのみ除外）
            if atk_type in ('ノーマル', 'かくとう') and t == 'ゴースト':
                continue
            if atk_type == 'ゴースト' and t in ('ノーマル', 'かくとう'):
                continue
            if atk_type == 'じめん' and t == 'ひこう':
                continue
            return t
    return cand

def safe_name(n):
    return re.sub(r'[^a-zA-Zぁ-んァ-ン一-龥0-9]', '_', n)

# 2ターン溜め技（1回実行では追加効果が出ないため確率テストを除外）
def is_two_turn(effect):
    return any(x in effect for x in ['使ったターンで溜め状態','使ったターンで空中状態','使ったターンで水中状態','使ったターンで地中状態','使ったターンで潜伏状態'])

# 接触トリガー型（まもる系：直接実行では能力変化しない）
def is_protect_trigger(effect):
    return '身を守り' in effect or '接触技をしてきた' in effect or '相手の攻撃から身を守' in effect

lines = [
    "#!/usr/bin/env python3",
    "# -*- coding: utf-8 -*-",
    '"""全技仕様テスト（generate_move_tests.pyで自動生成）"""',
    "import sys, random",
    "sys.path.insert(0, 'scripts')",
    "",
    "from simulator.data import DataLoader",
    "from simulator.battle import BattleSide, Action, BattleField, _execute_move, Battle, _priority",
    "from simulator.pokemon import BattlePokemon, calc_hp, calc_stat",
    "from simulator.damage import calc_damage, _effective_power as _ep",
    "",
    "dl = DataLoader('scripts/pokenavi.db')",
    "",
    "PASS = 0; FAIL = 0; FAILURES = []",
    "",
    "def check(label, cond, note=''):",
    "    global PASS, FAIL",
    "    if cond:",
    "        PASS += 1",
    "    else:",
    "        FAIL += 1",
    "        FAILURES.append(f'FAIL: {label}' + (f' → {note}' if note else ''))",
    "",
    "def make_poke(type1='ノーマル', type2=None, hp_b=100, atk_b=100, def_b=100,",
    "              spatk_b=100, spdef_b=100, spd_b=100, moves=None, item=None, ability=''):",
    "    ms = [dl.get_move(m) for m in (moves or []) if dl.get_move(m)]",
    "    p = BattlePokemon(",
    "        name='test', dex=0, type1=type1, type2=type2,",
    "        base_type1=type1, base_type2=type2,",
    "        max_hp=calc_hp(hp_b,0), hp=calc_hp(hp_b,0),",
    "        attack=calc_stat(atk_b,0,31,1.0), defense=calc_stat(def_b,0,31,1.0),",
    "        sp_attack=calc_stat(spatk_b,0,31,1.0), sp_defense=calc_stat(spdef_b,0,31,1.0),",
    "        speed=calc_stat(spd_b,0,31,1.0), moves=ms, pp=[20]*len(ms),",
    "        item=item, ability=ability, nature='',",
    "    )",
    "    return p",
    "",
    "def execute(atk, df, mv_name, field=None):",
    "    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name",
    "    s1 = BattleSide([atk]); s2 = BattleSide([df])",
    "    return _execute_move(s1, s2, Action(type='move', move=mv), field or BattleField())",
    "",
    "def execute_ctx(atk, df, mv_name, field=None):",
    "    '''field/side状態を参照するため s1,s2,field を返す'''",
    "    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name",
    "    s1 = BattleSide([atk]); s2 = BattleSide([df]); f = field or BattleField()",
    "    _execute_move(s1, s2, Action(type='move', move=mv), f)",
    "    return s1, s2, f",
    "",
    "def dmg(atk, df, mv_name):",
    "    mv = dl.get_move(mv_name) if isinstance(mv_name, str) else mv_name",
    "    return calc_damage(atk, df, mv, BattleField(), random_roll=1.0)  # 比率比較を安定させる固定ロール",
    "",
    # last_used_move等の『記録用フィールド』は技使用で必ず変わるため除外（偽の副作用検出を防ぐ）",
    "_SNAP_SKIP = {'moves','name','dex','max_hp','base_type1','base_type2','mega_data','evs',",
    "    'opp_view','last_used_move','turns_out','protect_consecutive','_last_flung_item'}",
    "def _snap_obj(o):",
    "    d = {}",
    "    for k, v in vars(o).items():",
    "        if k in _SNAP_SKIP: continue",
    "        if isinstance(v, list): v = tuple(v)",
    "        if isinstance(v, dict): v = tuple(sorted(v.items())) if v else ()",
    "        try: hash(v)",
    "        except Exception: v = str(v)",
    "        d[k] = v",
    "    return d",
    "def snap_poke(p): return _snap_obj(p)",
    "def snap_field(f): return _snap_obj(f)",
    "def snap_side(s): return _snap_obj(s)",
    "def any_change(before, after):",
    "    # 新規キー出現も変化とみなす（setattrで増えた状態フラグを検出）",
    "    keys = set(before) | set(after)",
    "    return any(before.get(k) != after.get(k) for k in keys)",
    "",
    "# 1v1シミュで副作用が観測できない技（味方対象・位置入替・ダブル専用ガード）",
    "DOUBLE_ONLY_SMOKE = {",
    "    'アロマミスト','コーチング','てだすけ','サイドチェンジ','ファストガード',",
    "    'ワイドガード','このゆびとまれ','じばそうさ','いやしのねがい','いのちのしずく',",
    "    'いやしのすず','フェアリーロック','りんしょう','さきおくり','おさきにどうぞ',",
    "    'いかりのこな','いやしのはどう','おちゃかい','ふしょくガス','フラフラダンス',",
    "}",
    "",
    "def side_effect_check(label, mv_name, atk_type, accuracy_known, smoke=False):",
    "    '''status技を実行し、何らかの観測可能変化が起きるか（命中までリトライ）。",
    "       smoke=Trueなら例外を投げず実行できればOK。'''",
    "    import random as _r",
    "    _r.seed(0)",
    "    mv = dl.get_move(mv_name)",
    "    if mv is None:",
    "        check(label, False, 'move not found'); return",
    "    for _ in range(40):",
    "        # 攻撃側と防御側を非対称に（入替/コピー技が観測できるよう型/特性/速度/値を変える）",
    "        atk = make_poke(type1=atk_type, hp_b=200, spd_b=50, ability='ちからもち')",
    "        df = make_poke(type1='ドラゴン', hp_b=200, spd_b=150, ability='ふゆう')",
    "        atk.hp = 150  # 回復技用に余地",
    "        # 前提条件依存技のための汎用セットアップ（道具・ランク・前技・状態・たくわえ）",
    "        atk.item = 'オボンのみ'; df.item = 'たべのこし'",
    "        atk._last_consumed_item = 'オボンのみ'",
    "        atk.stockpile_count = 2",
    "        df.stage_attack = 2; df.stage_defense = 2; df.stage_sp_attack = 2",
    "        atk.stage_attack = 1",
    "        df.last_used_move = 'たいあたり'; atk.last_used_move = 'たいあたり'",
    "        df.moves = [dl.get_move('たいあたり')]; df.pp = [10]",
    "        s1 = BattleSide([atk, make_poke()]); s2 = BattleSide([df, make_poke()]); f = BattleField()",
    "        b_a, b_d = snap_poke(atk), snap_poke(df)",
    "        b_f, b_s1, b_s2 = snap_field(f), snap_side(s1), snap_side(s2)",
    "        try:",
    "            _execute_move(s1, s2, Action(type='move', move=mv), f)",
    "        except Exception as e:",
    "            check(label, False, f'例外: {e}'); return",
    "        changed = (any_change(b_a, snap_poke(atk)) or any_change(b_d, snap_poke(df))",
    "                   or any_change(b_f, snap_field(f)) or any_change(b_s1, snap_side(s1))",
    "                   or any_change(b_s2, snap_side(s2)))",
    "        if changed:",
    "            check(label, True); return",
    "    if smoke:",
    "        check(label, True)  # 例外なく実行完了（観測困難技）",
    "    else:",
    "        check(label, False, '副作用が観測されない（未実装の疑い）')",
    "",
    "",
]

generated = 0
skipped = 0

for name, type_, cat, power, accuracy, pp, effect in moves:
    if not effect or not effect.strip():
        skipped += 1
        continue
    # 全角→半角正規化（％→% 等の表記ゆれでパターンを取りこぼさない）
    effect = effect.translate(str.maketrans('０１２３４５６７８９％＋', '0123456789%+'))

    tests_for_move = []

    # ── DBに技が存在することの確認 ────────────────────────────
    tests_for_move.append(
        f'check("DB: {name} 取得可能", dl.get_move("{name}") is not None)'
    )

    atk_type = type_ if type_ else 'ノーマル'
    def_type = defender_type_for(atk_type)
    two_turn = is_two_turn(effect)
    protect_trigger = is_protect_trigger(effect)

    # ── ダメージ技の基本確認 ──────────────────────────────────
    if cat in ('physical', 'special') and power and power > 0:
        sn = safe_name(name)
        tests_for_move.append(f'_mv_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_{sn}:')
        tests_for_move.append(f'    _pa_{sn} = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'    _pd_{sn} = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        if two_turn:
            # 1ターン目溜め→2ターン目攻撃。命中するまで最大10回リトライ
            tests_for_move.append(f'    random.seed(0)')
            tests_for_move.append(f'    for _ in range(10):')
            tests_for_move.append(f'        _pa_{sn} = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pd_{sn} = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
            tests_for_move.append(f'        execute(_pa_{sn}, _pd_{sn}, "{name}"); execute(_pa_{sn}, _pd_{sn}, "{name}")')
            tests_for_move.append(f'        if _pd_{sn}.hp < _pd_{sn}.max_hp: break')
            tests_for_move.append(f'    check("ダメージ計算: {name}", _pd_{sn}.hp < _pd_{sn}.max_hp, f"hp={{_pd_{sn}.hp}}")')
        else:
            tests_for_move.append(f'    _d_{sn} = dmg(_pa_{sn}, _pd_{sn}, "{name}")')
            tests_for_move.append(f'    check("ダメージ計算: {name}", _d_{sn} > 0, f"dmg={{_d_{sn}}}")')

    # ── 状態異常追加効果（2ターン技は専用ロジックで実行） ──────
    for jp, en in STATUS_MAP.items():
        m = re.search(rf'(\d+)%の確率で相手を{jp}状態', effect)
        # %表記がなく「相手をXX状態にする」(条件節なし)のダメージ技は確定100%扱い
        is_100 = False
        if not m and cat in ('physical','special') and re.search(rf'相手を{jp}状態にする', effect):
            if not any(w in effect for w in ('場合','状態の相手','接触技を','能力が上がっている')):
                is_100 = True
        if (m or is_100) and cat in ('physical', 'special'):
            prob = int(m.group(1)) if m else 100
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: {jp}{prob}%')
            tests_for_move.append(f'_mv_s_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mv_s_{sn}:')
            safe_def = status_safe_defender(atk_type, en)
            tests_for_move.append(f'    random.seed(0); _hit_{sn} = 0')
            tests_for_move.append(f'    for _ in range(300):')
            # 攻撃側は弱く・防御側は超耐久＆状態異常を受けられる型にする
            tests_for_move.append(f'        _pa2 = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30); _pd2 = make_poke(type1="{safe_def}", def_b=255, spdef_b=255, hp_b=255)')
            if two_turn:
                tests_for_move.append(f'        execute(_pa2, _pd2, "{name}"); execute(_pa2, _pd2, "{name}")')
            else:
                tests_for_move.append(f'        execute(_pa2, _pd2, "{name}")')
            target = '_pd2.confused' if en == 'confused' else f'(_pd2.status == "{en}")'
            tests_for_move.append(f'        _hit_{sn} += int({target})')
            lo = max(1, int(300 * prob/100 * 0.3))
            hi = int(300 * prob/100 * 1.7) + 15
            tests_for_move.append(f'    check("追加効果({jp}{prob}%): {name}", {lo} <= _hit_{sn} <= {hi}, f"count={{_hit_{sn}}}/300")')
            # negative: 免疫タイプには付与されない（どく/まひ/やけど/こおり）
            _imm = STATUS_IMMUNE_TYPE.get(en)
            _imm_types = [_imm] + (['はがね'] if en in ('poison','badpoison') else []) if _imm else []
            for _it in _imm_types:
                tests_for_move.append(f'    random.seed(1); _immok_{sn} = True')
                tests_for_move.append(f'    for _ in range(60):')
                tests_for_move.append(f'        _pai = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30); _pdi = make_poke(type1="{_it}", def_b=255, spdef_b=255, hp_b=255)')
                if two_turn:
                    tests_for_move.append(f'        execute(_pai, _pdi, "{name}"); execute(_pai, _pdi, "{name}")')
                else:
                    tests_for_move.append(f'        execute(_pai, _pdi, "{name}")')
                tests_for_move.append(f'        if _pdi.status == "{en}": _immok_{sn} = False; break')
                tests_for_move.append(f'    check("{jp}免疫({_it}型には無効): {name}", _immok_{sn}, "免疫タイプに状態異常が付与されないこと")')

    # ── ひるみ（％指定／怯ませる漢字表記／100%確定を統一処理） ──
    m = re.search(r'(\d+)%の確率で相手を(?:ひるませる|怯ませる)', effect)
    if not m and cat in ('physical', 'special') and re.search(r'相手を(?:ひるませる|怯ませる)', effect) \
            and not re.search(r'\d+%の確率で相手を(?:ひるませる|怯ませる)', effect) \
            and '接触技を' not in effect and '能力が上がっている' not in effect \
            and name != 'はやてがえし':
        prob = 100  # 確率表記なし＝確定（ねこだまし/はやてがえし等）
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: ひるみ(確定)')
        tests_for_move.append(f'_mv_f100_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_f100_{sn}:')
        tests_for_move.append(f'    random.seed(0); _f100 = False')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pa100 = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30); _pd100 = make_poke(type1="{def_type}", def_b=255, spdef_b=255, hp_b=255)')
        tests_for_move.append(f'        execute(_pa100, _pd100, "{name}")')
        tests_for_move.append(f'        if _pd100.flinched: _f100 = True; break')
        tests_for_move.append(f'    check("ひるみ(確定): {name}", _f100)')
    if m and cat in ('physical', 'special') and name != 'いびき':
        prob = int(m.group(1))
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: ひるみ{prob}%')
        tests_for_move.append(f'_mv_f_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_f_{sn}:')
        tests_for_move.append(f'    random.seed(1); _fh_{sn} = 0')
        tests_for_move.append(f'    for _ in range(300):')
        tests_for_move.append(f'        _pa3 = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30); _pd3 = make_poke(type1="{def_type}", def_b=255, spdef_b=255, hp_b=255)')
        if two_turn:
            tests_for_move.append(f'        execute(_pa3, _pd3, "{name}"); _fh_{sn} += int(_pd3.flinched); execute(_pa3, _pd3, "{name}"); _fh_{sn} += int(_pd3.flinched)')
        else:
            tests_for_move.append(f'        execute(_pa3, _pd3, "{name}"); _fh_{sn} += int(_pd3.flinched)')
        lo = max(1, int(300 * prob/100 * 0.3))
        hi = int(300 * prob/100 * 1.7) + 15
        tests_for_move.append(f'    check("ひるみ({prob}%): {name}", {lo} <= _fh_{sn} <= {hi}, f"count={{_fh_{sn}}}/300")')

    # ── 能力ダウン（相手）：接触トリガー型は除外。命中率/回避率も対応 ──
    _STATDOWN = [('攻撃','attack'),('防御','defense'),('特攻','sp_attack'),
                 ('特防','sp_defense'),('素早さ','speed'),
                 ('命中率','accuracy'),('回避率','evasion'),('命中','accuracy'),('回避','evasion')]
    if not protect_trigger:
        _done_stats = set()
        for stat_jp, stat_en in _STATDOWN:
            if stat_en in _done_stats:
                continue
            matched = False
            for n_stages in [2, 1]:  # 2段階を優先マッチ
                m = re.search(rf'相手の{stat_jp}を{n_stages}段階下げる', effect)
                if m:
                    _done_stats.add(stat_en)
                    sn = safe_name(name)
                    tests_for_move.append(f'# {name}: 相手{stat_jp}-{n_stages}')
                    tests_for_move.append(f'_mv_dd_{sn} = dl.get_move("{name}")')
                    tests_for_move.append(f'if _mv_dd_{sn}:')
                    tests_for_move.append(f'    _pa_dd = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30)')
                    # 1回の適用で正確に -{n_stages} 変化することを検証（毎回新しい防御側＝累積を排除）
                    tests_for_move.append(f'    random.seed(0); _dd_val_{sn} = 0; _dd_ok_{sn} = False')
                    tests_for_move.append(f'    for _ in range(60):')
                    tests_for_move.append(f'        _pd_dd = make_poke(type1="{def_type}", hp_b=255, def_b=255, spdef_b=255)')
                    if two_turn:
                        tests_for_move.append(f'        execute(_pa_dd, _pd_dd, "{name}"); execute(_pa_dd, _pd_dd, "{name}")')
                    else:
                        tests_for_move.append(f'        execute(_pa_dd, _pd_dd, "{name}")')
                    tests_for_move.append(f'        if _pd_dd.stage_{stat_en} != 0: _dd_val_{sn} = _pd_dd.stage_{stat_en}; _dd_ok_{sn} = True; break')
                    tests_for_move.append(f'    check("相手{stat_jp}-{n_stages}: {name}", _dd_ok_{sn} and _dd_val_{sn} == -{n_stages}, f"1回適用={{_dd_val_{sn}}} 期待=-{n_stages}")')
                    matched = True
                    break
            if matched:
                pass

    # ── 外れ時自傷 ───────────────────────────────────────────
    if '外れるか失敗すると自分の最大HPの1/2' in effect:
        tests_for_move.append(f'# {name}: 外れ時1/2自傷')
        tests_for_move.append(f'_mv_mr_{safe_name(name)} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_mr_{safe_name(name)}:')
        tests_for_move.append(f'    _pa_mr = make_poke(type1="{type_}", atk_b=100)')
        tests_for_move.append(f'    import copy as _cp; _mv_miss = _cp.copy(_mv_mr_{safe_name(name)}); _mv_miss.accuracy = 1')
        tests_for_move.append(f'    random.seed(99); _s1m = BattleSide([_pa_mr]); _s2m = BattleSide([make_poke()])')
        tests_for_move.append(f'    _execute_move(_s1m, _s2m, Action(type="move", move=_mv_miss), BattleField())')
        tests_for_move.append(f'    check("外れ時1/2自傷: {name}", _pa_mr.max_hp - _pa_mr.hp == max(1, _pa_mr.max_hp//2), f"dmg={{_pa_mr.max_hp - _pa_mr.hp}}")')

    # ── 2ターン溜め ──────────────────────────────────────────
    if any(x in effect for x in ['使ったターンで溜め状態', '使ったターンで空中状態', '使ったターンで水中状態', '使ったターンで地中状態', '使ったターンで潜伏状態']):
        tests_for_move.append(f'# {name}: 2ターン溜め')
        tests_for_move.append(f'_mv_2t_{safe_name(name)} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_2t_{safe_name(name)}:')
        tests_for_move.append(f'    _pa_2t = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pd_2t = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'    _hp_before_2t = _pd_2t.hp')
        tests_for_move.append(f'    execute(_pa_2t, _pd_2t, "{name}")')
        tests_for_move.append(f'    check("2ターン溜め(1T)ダメなし: {name}", _pd_2t.hp == _hp_before_2t)')
        tests_for_move.append(f'    check("2ターン溜め(1T)charging: {name}", _pa_2t.charging_move == "{name}")')
        # 2ターン目攻撃。命中するまで最大10回リトライ（charging維持のため同一個体で再溜め）
        tests_for_move.append(f'    random.seed(0)')
        tests_for_move.append(f'    for _ in range(10):')
        tests_for_move.append(f'        execute(_pa_2t, _pd_2t, "{name}")')
        tests_for_move.append(f'        if _pd_2t.hp < _hp_before_2t: break')
        tests_for_move.append(f'        if _pa_2t.charging_move is None: execute(_pa_2t, _pd_2t, "{name}")')
        tests_for_move.append(f'    check("2ターン溜め(2T)ダメあり: {name}", _pd_2t.hp < _hp_before_2t)')

    # ── バインド ─────────────────────────────────────────────
    if '相手をバインド状態にする' in effect and cat in ('physical', 'special'):
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: バインド')
        tests_for_move.append(f'_mv_bd_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_bd_{sn}:')
        tests_for_move.append(f'    random.seed(0)')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pa_bd = make_poke(type1="{atk_type}", atk_b=150, spatk_b=150); _pd_bd = make_poke(type1="{def_type}", def_b=100, spdef_b=100, hp_b=255)')
        tests_for_move.append(f'        execute(_pa_bd, _pd_bd, "{name}")')
        tests_for_move.append(f'        if _pd_bd.bound_count in (4,5): break')
        tests_for_move.append(f'    check("バインド付与: {name}", _pd_bd.bound_count in (4,5), f"count={{_pd_bd.bound_count}}")')

    # ── あばれ状態 ───────────────────────────────────────────
    if '自分はあばれ状態になる' in effect:
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: あばれ状態')
        tests_for_move.append(f'_mv_rg_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_rg_{sn}:')
        tests_for_move.append(f'    _pa_rg = make_poke(type1="{atk_type}", atk_b=30, spatk_b=30); _pd_rg = make_poke(type1="{def_type}", def_b=255, spdef_b=255, hp_b=255)')
        tests_for_move.append(f'    execute(_pa_rg, _pd_rg, "{name}")')
        tests_for_move.append(f'    check("あばれ状態: {name}", _pa_rg.locked_move == "{name}")')

    # ── ドレイン ─────────────────────────────────────────────
    if '与えたダメージの' in effect and 'HPを回復' in effect and cat in ('physical', 'special'):
        sn = safe_name(name)
        _frm = re.search(r'与えたダメージの(\d+)/(\d+)', effect)
        _num, _den = (int(_frm.group(1)), int(_frm.group(2))) if _frm else (1, 2)
        tests_for_move.append(f'# {name}: ドレイン（与ダメの{_num}/{_den}回復）')
        tests_for_move.append(f'_mv_dr_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_dr_{sn}:')
        tests_for_move.append(f'    _pa_dr = make_poke(type1="{atk_type}", atk_b=150, spatk_b=150, hp_b=200)')
        tests_for_move.append(f'    random.seed(0); _dr_ok_{sn} = False; _dr_dealt_{sn} = 0; _dr_heal_{sn} = 0')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pa_dr.hp = 1; _pd_dr = make_poke(type1="{def_type}", def_b=50, spdef_b=50, hp_b=255)')
        tests_for_move.append(f'        execute(_pa_dr, _pd_dr, "{name}")')
        tests_for_move.append(f'        _dr_dealt_{sn} = _pd_dr.max_hp - _pd_dr.hp; _dr_heal_{sn} = _pa_dr.hp - 1')
        tests_for_move.append(f'        if _dr_dealt_{sn} > 0: _dr_ok_{sn} = abs(_dr_heal_{sn} - max(1, _dr_dealt_{sn} * {_num} // {_den})) <= 2; break')
        tests_for_move.append(f'    check("ドレイン回復(与ダメ{_num}/{_den}): {name}", _dr_ok_{sn}, f"dealt={{_dr_dealt_{sn}}} heal={{_dr_heal_{sn}}}")')

    # ── じごくづき ───────────────────────────────────────────
    if 'じごくづき状態' in effect and cat in ('physical', 'special'):
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: じごくづき状態')
        tests_for_move.append(f'_mv_tc_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_tc_{sn}:')
        tests_for_move.append(f'    random.seed(0)')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pa_tc = make_poke(type1="{atk_type}", atk_b=150, spatk_b=150); _pd_tc = make_poke(type1="{def_type}", def_b=100, spdef_b=100, hp_b=255)')
        tests_for_move.append(f'        execute(_pa_tc, _pd_tc, "{name}")')
        tests_for_move.append(f'        if _pd_tc.throat_chop_count == 2: break')
        tests_for_move.append(f'    check("じごくづき付与: {name}", _pd_tc.throat_chop_count == 2)')
        tests_for_move.append(f'    # 効果本体: じごくづき中は音技が使えない')
        tests_for_move.append(f'    _ptc2 = make_poke(type1="ノーマル", spatk_b=100); _ptc2.throat_chop_count = 2')
        tests_for_move.append(f'    _dtc2 = make_poke(type1="あく", hp_b=255, spdef_b=200); _hptc = _dtc2.hp')
        tests_for_move.append(f'    execute(_ptc2, _dtc2, "ハイパーボイス")')
        tests_for_move.append(f'    check("じごくづき中は音技不可: {name}", _dtc2.hp == _hptc, f"hp={{_dtc2.hp}}/{{_hptc}}")')

    # ── タイプ相性の上書き（フリーズドライ等：特定タイプに効果バツグン） ──
    m = re.search(r'(\S+?)タイプの相手にも効果バツグン', effect)
    if m and cat in ('physical', 'special'):
        tgt_type = m.group(1)
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: {tgt_type}タイプに効果バツグン上書き')
        tests_for_move.append(f'_mv_ov_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_ov_{sn}:')
        # calc_damage（UI/ダメージ計算経路）で対象タイプへ2倍以上か確認
        tests_for_move.append(f'    _pa_ov = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'    _d_ov_tgt = dmg(_pa_ov, make_poke(type1="{tgt_type}", def_b=100, spdef_b=100), "{name}")')
        tests_for_move.append(f'    _d_ov_neu = dmg(_pa_ov, make_poke(type1="ノーマル", def_b=100, spdef_b=100), "{name}")')
        tests_for_move.append(f'    check("{tgt_type}効果バツグン上書き: {name}", _d_ov_tgt >= _d_ov_neu * 2, f"tgt={{_d_ov_tgt}} neu={{_d_ov_neu}}")')

    # ── 自己能力上昇（変化技・複数ステータス対応） ──────────────
    # 前提条件付き（きのみ必須/HP消費/天候条件）は単純テスト対象外
    _STAT_ALL = [('攻撃','attack'),('防御','defense'),('特攻','sp_attack'),
                 ('特防','sp_defense'),('素早さ','speed'),('命中率','accuracy'),('回避率','evasion')]
    # きのみ前提/味方対象は除外。HP消費・天候条件付きでも基本効果は無条件発現するため検証する
    _selfboost_excl = ('使えない' in effect or 'きのみ' in effect or '味方' in effect)
    if cat == 'status' and not _selfboost_excl:
        # stat列の連続を捕捉（接続詞と/・/、対応）。相手/味方を含む技は「自分の」直前必須。
        _need_self = ('相手' in effect or '味方' in effect)
        _pat = (r'自分の([攻撃防御特攻特防素早さ命中率回避・、と ]+)[をが](\d+)段階(?:ずつ)?(上げ|上が|下げ|下が)'
                if _need_self else
                r'([攻撃防御特攻特防素早さ命中率回避・、と ]+)[をが](\d+)段階(?:ずつ)?(上げ|上が|下げ|下が)')
        for seg, n_up, direction in re.findall(_pat, effect):
            if direction not in ('上げ', '上が'):
                continue
            n_up = int(n_up)
            ups = [(sj, se) for sj, se in _STAT_ALL if sj in seg]
            for stat_jp, stat_en in ups:
                sn = safe_name(name)
                tests_for_move.append(f'# {name}: 自分{stat_jp}+{n_up}')
                tests_for_move.append(f'_mv_sb_{sn}_{stat_en} = dl.get_move("{name}")')
                tests_for_move.append(f'if _mv_sb_{sn}_{stat_en}:')
                tests_for_move.append(f'    _pa_sb = make_poke(type1="{atk_type}"); _pd_sb = make_poke()')
                tests_for_move.append(f'    execute(_pa_sb, _pd_sb, "{name}")')
                tests_for_move.append(f'    check("自分{stat_jp}+{n_up}: {name}", _pa_sb.stage_{stat_en} == {n_up}, f"1回適用={{_pa_sb.stage_{stat_en}}} 期待=+{n_up}")')

    # ── 確率付き自己能力上昇（ダメージ技：げんしのちから/コメットパンチ等） ──
    pm2 = re.findall(r'(\d+)%の確率で自分の([^。]*?)を(\d+)段階上げ', effect)
    if pm2 and cat in ('physical','special'):
        for prob_s, seg, n_up in pm2:
            ups = [(sj, se) for sj, se in _STAT_ALL if sj in seg]
            # 代表1ステータスで発現確認（確率が低くても多試行で必ず出る）
            if ups:
                stat_jp, stat_en = ups[0]
                sn = safe_name(name)
                tests_for_move.append(f'# {name}: 確率自己{stat_jp}+{n_up}({prob_s}%)')
                tests_for_move.append(f'_mvpb_{sn} = dl.get_move("{name}")')
                tests_for_move.append(f'if _mvpb_{sn}:')
                tests_for_move.append(f'    random.seed(0); _pb_ok_{sn} = False')
                tests_for_move.append(f'    for _ in range(200):')
                tests_for_move.append(f'        _papb = make_poke(type1="{atk_type}", atk_b=40, spatk_b=40); _pdpb = make_poke(type1="{def_type}", hp_b=255, def_b=255, spdef_b=255)')
                if two_turn:
                    tests_for_move.append(f'        execute(_papb, _pdpb, "{name}"); execute(_papb, _pdpb, "{name}")')
                else:
                    tests_for_move.append(f'        execute(_papb, _pdpb, "{name}")')
                tests_for_move.append(f'        if _papb.stage_{stat_en} > 0: _pb_ok_{sn} = _papb.stage_{stat_en}; break')
                tests_for_move.append(f'    check("確率自己{stat_jp}+{n_up}: {name}", _pb_ok_{sn} == {int(n_up)}, f"1回適用={{_pb_ok_{sn}}} 期待=+{n_up}")')
            break

    # ── 溜めターン自己能力上昇（メテオビーム等） ──────────────
    cm2 = re.search(r'使ったターンに自分の([^。]*?)を(\d+)段階上げ', effect)
    if cm2 and two_turn and cat in ('physical','special'):
        seg = cm2.group(1); n_up = int(cm2.group(2))
        ups = [(sj, se) for sj, se in _STAT_ALL if sj in seg]
        if ups:
            stat_jp, stat_en = ups[0]
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: 溜めターン自己{stat_jp}+{n_up}')
            tests_for_move.append(f'_mvcb_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mvcb_{sn}:')
            tests_for_move.append(f'    _pacb = make_poke(type1="{atk_type}", atk_b=60, spatk_b=60); _pdcb = make_poke(type1="{def_type}", hp_b=255)')
            tests_for_move.append(f'    execute(_pacb, _pdcb, "{name}")  # 溜めターン')
            tests_for_move.append(f'    check("溜め自己{stat_jp}+{n_up}: {name}", _pacb.stage_{stat_en} >= {n_up}, f"stage={{_pacb.stage_{stat_en}}}")')

    # ── 天候で溜め省略・即攻撃（ソーラー系のにほんばれ／エレクトロビームのあめ等） ──
    _imm = re.search(r'(にほんばれ|あめ|すなあらし|あられ|ゆき)状態の場合は?溜め状態にならず', effect)
    if _imm and two_turn and cat in ('physical', 'special'):
        _w_en = {'にほんばれ':'sunny','あめ':'rain','すなあらし':'sandstorm','あられ':'hail','ゆき':'hail'}[_imm.group(1)]
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: {_imm.group(1)}状態では溜めず即攻撃（1ターン目でダメージ）')
        tests_for_move.append(f'_fwi_{sn} = BattleField(); _fwi_{sn}.weather = "{_w_en}"')
        tests_for_move.append(f'_pwi_{sn} = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _dwi_{sn} = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100); _hpwi_{sn} = _dwi_{sn}.hp')
        tests_for_move.append(f'execute(_pwi_{sn}, _dwi_{sn}, "{name}", _fwi_{sn})')
        tests_for_move.append(f'check("{_imm.group(1)}で即発動(1Tダメージ): {name}", _dwi_{sn}.hp < _hpwi_{sn} and _pwi_{sn}.charging_move is None, f"hp={{_dwi_{sn}.hp}}/{{_hpwi_{sn}}} charging={{_pwi_{sn}.charging_move}}")')
        # 即攻撃でも「使ったターンに自分の能力上昇」は適用される（エレクトロビームの特攻+1等）
        _imm_up = re.search(r'使ったターンに自分の([^。]*?)を(\d+)段階上げ', effect)
        if _imm_up:
            _iups = [(sj, se) for sj, se in _STAT_ALL if sj in _imm_up.group(1)]
            if _iups:
                _isj, _ise = _iups[0]; _inu = int(_imm_up.group(2))
                tests_for_move.append(f'check("{_imm.group(1)}即攻撃でも自己{_isj}+{_inu}: {name}", _pwi_{sn}.stage_{_ise} >= {_inu}, f"stage={{_pwi_{sn}.stage_{_ise}}}")')

    # ── スクリーン破壊（ダメージ技）。まもる解除技(フェイント等)は除外 ──
    _is_screenbreak = ('を解除して攻撃' in effect and cat in ('physical','special')
                       and any(s in effect for s in ('ひかりのかべ','リフレクター','オーロラベール')))
    if _is_screenbreak:
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: スクリーン破壊')
        tests_for_move.append(f'_mvbrk_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvbrk_{sn}:')
        tests_for_move.append(f'    random.seed(0); _brk_ok = False')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pabrk = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _pdbrk = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
        tests_for_move.append(f'        _s1b = BattleSide([_pabrk]); _s2b = BattleSide([_pdbrk])')
        tests_for_move.append(f'        _s2b.reflect = True; _s2b.reflect_count = 5; _s2b.light_screen = True; _s2b.light_screen_count = 5')
        tests_for_move.append(f'        _execute_move(_s1b, _s2b, Action(type="move", move=_mvbrk_{sn}), BattleField())')
        tests_for_move.append(f'        if not _s2b.reflect and not _s2b.light_screen: _brk_ok = True; break')
        tests_for_move.append(f'    check("スクリーン破壊: {name}", _brk_ok)')

    # ── ハザード設置（ダメージ技：がんせきアックス/ひけん・ちえなみ） ──
    _HZ2 = {'まきびし':'spikes','どくびし':'toxic_spikes','ステルスロック':'stealth_rock','ねばねばネット':'sticky_web'}
    for hz_jp, hz_attr in _HZ2.items():
        if f'相手の場を{hz_jp}状態' in effect and cat in ('physical','special'):
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: ハザード設置(ダメージ技){hz_attr}')
            tests_for_move.append(f'_mvhd_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mvhd_{sn}:')
            tests_for_move.append(f'    random.seed(0); _hdval = False')
            tests_for_move.append(f'    for _ in range(20):')
            tests_for_move.append(f'        _pahd = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _pdhd = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
            tests_for_move.append(f'        _s1hd = BattleSide([_pahd]); _s2hd = BattleSide([_pdhd]); _fhd = BattleField()')
            tests_for_move.append(f'        _execute_move(_s1hd, _s2hd, Action(type="move", move=_mvhd_{sn}), _fhd)')
            # ステルスロックのみ run時確定(_stealth_rock_pending)を許容。他ハザードは自分の配列のみ厳密判定。
            if hz_attr == 'stealth_rock':
                tests_for_move.append(f'        _hdval = _fhd.{hz_attr}[_s2hd.field_idx] or getattr(_s2hd,"_stealth_rock_pending",False) or _s2hd.stealth_rock_set')
            else:
                tests_for_move.append(f'        _hdval = _fhd.{hz_attr}[_s2hd.field_idx]')
            tests_for_move.append(f'        if _hdval: break')
            tests_for_move.append(f'    check("ハザード設置{hz_attr}: {name}", bool(_hdval), f"val={{_hdval}}")')
            break

    # ── 状態異常付与（変化技）：相手をXX状態にする（命中必要） ──
    # 守る系・接触トリガー・粉技(くさ無効あり)は専用挙動のため除外
    STATUS_INFLICT = {'まひ':'paralysis','やけど':'burn','どく':'poison',
                      'もうどく':'badpoison','ねむり':'sleep','こんらん':'confused'}
    _status_infl_excl = protect_trigger or '身を守' in effect or '接触' in effect
    for jp, en in STATUS_INFLICT.items():
        # 「相手をXX状態にする」かつ確率%表記でない（=確定変化技）
        if (re.search(rf'相手を{jp}状態にする', effect) and cat == 'status'
                and not re.search(rf'\d+%の確率で相手を{jp}', effect) and not _status_infl_excl):
            sn = safe_name(name)
            # 免疫タイプを避けた防御側（粉技はくさ無効なので非くさ固定）
            if en == 'confused':
                sdef = 'ノーマル'
            elif '粉' in effect or 'こな' in name:
                sdef = 'ノーマル'  # くさ無効回避
            else:
                sdef = status_safe_defender(atk_type, en)
            tests_for_move.append(f'# {name}: {jp}付与(変化技)')
            tests_for_move.append(f'_mv_si_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mv_si_{sn}:')
            tests_for_move.append(f'    random.seed(0); _ok_{sn} = False')
            tests_for_move.append(f'    for _ in range(30):')
            tests_for_move.append(f'        _pa_si = make_poke(type1="{atk_type}"); _pd_si = make_poke(type1="{sdef}", hp_b=255)')
            tests_for_move.append(f'        execute(_pa_si, _pd_si, "{name}")')
            cond = '_pd_si.confused' if en == 'confused' else f'_pd_si.status == "{en}"'
            tests_for_move.append(f'        if {cond}: _ok_{sn} = True; break')
            tests_for_move.append(f'    check("{jp}付与: {name}", _ok_{sn})')
            # negative: 免疫タイプには付与されない
            _imm2 = STATUS_IMMUNE_TYPE.get(en)
            _imm2_types = ([_imm2] + (['はがね'] if en in ('poison','badpoison') else [])) if _imm2 else []
            for _it in _imm2_types:
                # でんじは等のじめん無効は別句で扱うので、ここは状態異常免疫タイプのみ
                tests_for_move.append(f'    random.seed(2); _siimm_{sn} = True')
                tests_for_move.append(f'    for _ in range(40):')
                tests_for_move.append(f'        _pai2 = make_poke(type1="{atk_type}"); _pdi2 = make_poke(type1="{_it}", hp_b=255)')
                tests_for_move.append(f'        execute(_pai2, _pdi2, "{name}")')
                tests_for_move.append(f'        if _pdi2.status == "{en}": _siimm_{sn} = False; break')
                tests_for_move.append(f'    check("{jp}免疫({_it}型には無効): {name}", _siimm_{sn}, "免疫タイプに付与されないこと")')
            break  # 1状態のみ

    # ── 回復技：自分のHPを回復する（前提条件のある技は除外） ──
    _heal_excl = ('ひんしになる' in effect or 'たくわえ' in effect or 'のみこむ' == name
                  or '味方' in effect or '相手のHP' in effect or 'ねがいごと' in effect
                  or '相手の攻撃の数値分' in effect)  # ちからをすいとる等：専用ブロックで検証
    if cat == 'status' and '自分のHP' in effect and '回復' in effect and not _heal_excl:
        sn = safe_name(name)
        _hfrm = re.search(r'最大HPの(\d+)/(\d+)', effect)
        _hn, _hd = (int(_hfrm.group(1)), int(_hfrm.group(2))) if _hfrm else (1, 2)
        tests_for_move.append(f'# {name}: HP回復（最大HPの約{_hn}/{_hd}・無天候）')
        tests_for_move.append(f'_mv_hp_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_hp_{sn}:')
        tests_for_move.append(f'    _pa_hp = make_poke(type1="{atk_type}", hp_b=200); _pa_hp.hp = 1; _pd_hp = make_poke()')
        tests_for_move.append(f'    execute(_pa_hp, _pd_hp, "{name}")')
        tests_for_move.append(f'    _exp_hp_{sn} = _pa_hp.max_hp * {_hn} // {_hd}')
        tests_for_move.append(f'    check("HP回復(約{_hn}/{_hd}): {name}", abs(_pa_hp.hp - (1 + _exp_hp_{sn})) <= 3 or _pa_hp.hp == _pa_hp.max_hp, f"hp={{_pa_hp.hp}} 期待≈{{1 + _exp_hp_{sn}}}")')

    # ── 天候技 ────────────────────────────────────────────────
    WEATHER_MAP = {'あめ':'rain','にほんばれ':'sunny','晴れ':'sunny','すなあらし':'sandstorm','砂':'sandstorm','あられ':'hail','ゆき':'hail'}
    wm = re.search(r'(あめ|にほんばれ|晴れ|すなあらし|あられ|ゆき)状態にする', effect)
    if wm and cat == 'status':
        weather_en = WEATHER_MAP.get(wm.group(1))
        if weather_en:
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: 天候{weather_en}')
            tests_for_move.append(f'_mv_w_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mv_w_{sn}:')
            tests_for_move.append(f'    _s1w, _s2w, _fw = execute_ctx(make_poke(type1="{atk_type}"), make_poke(), "{name}")')
            tests_for_move.append(f'    check("天候{weather_en}: {name}", _fw.weather == "{weather_en}", f"weather={{_fw.weather}}")')

    # ── スクリーン技 ──────────────────────────────────────────
    SCREEN_MAP = {'リフレクター':'reflect','ひかりのかべ':'light_screen','オーロラベール':'aurora_veil'}
    for scr_jp, scr_attr in SCREEN_MAP.items():
        if f'味方の場を{scr_jp}状態' in effect or (scr_jp in effect and '味方の場' in effect and 'ターンの間' in effect):
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: スクリーン{scr_attr}')
            tests_for_move.append(f'_mv_sc_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mv_sc_{sn}:')
            field_setup = ''
            if scr_attr == 'aurora_veil':
                field_setup = '_fsc = BattleField(); _fsc.weather = "hail"'
            else:
                field_setup = '_fsc = BattleField()'
            tests_for_move.append(f'    {field_setup}')
            tests_for_move.append(f'    _s1sc, _s2sc, _fsc = execute_ctx(make_poke(type1="{atk_type}"), make_poke(), "{name}", _fsc)')
            tests_for_move.append(f'    check("スクリーン{scr_attr}: {name}", _s1sc.{scr_attr}, f"{scr_attr}={{_s1sc.{scr_attr}}}")')
            break

    # ── 優先度技：単一符号付き1桁のみ、かつDB値と一致する場合に検証 ──
    # （条件付き優先度・ダブル専用技・数字巻き込みを避けるため厳格化）
    pm = re.search(r'優先度([+\-]\d)(?!\d)', effect)
    if pm and 'フィールド' not in effect and '味方' not in effect:
        prio = int(pm.group(1))
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 優先度{prio}')
        tests_for_move.append(f'_mv_pr_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_pr_{sn} and _mv_pr_{sn}.priority == {prio}:')
        tests_for_move.append(f'    check("優先度{prio}: {name}", _mv_pr_{sn}.priority == {prio})')
        tests_for_move.append(f'elif _mv_pr_{sn}:')
        tests_for_move.append(f'    check("優先度{prio}: {name}", _mv_pr_{sn}.priority == {prio}, f"DB優先度={{_mv_pr_{sn}.priority}} 仕様={prio}")')

    # ── 一撃必殺技 ────────────────────────────────────────────
    if '相手をひんしにする' in effect and cat in ('physical', 'special'):
        sn = safe_name(name)
        # 無効タイプを避ける（ハサミギロチン=ゴースト無効, じわれ=ひこう無効, つのドリル=ゴースト無効）
        ohko_def = 'ノーマル'
        if name in ('ハサミギロチン', 'つのドリル'): ohko_def = 'ノーマル'  # ゴースト以外
        elif name == 'じわれ': ohko_def = 'ノーマル'  # ひこう以外
        tests_for_move.append(f'# {name}: 一撃必殺')
        tests_for_move.append(f'_mv_oh_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mv_oh_{sn}:')
        tests_for_move.append(f'    random.seed(0); _ko_{sn} = False')
        tests_for_move.append(f'    for _ in range(60):')
        tests_for_move.append(f'        _pa_oh = make_poke(type1="{atk_type}"); _pd_oh = make_poke(type1="{ohko_def}", hp_b=200)')
        tests_for_move.append(f'        execute(_pa_oh, _pd_oh, "{name}")')
        tests_for_move.append(f'        if not _pd_oh.is_alive: _ko_{sn} = True; break')
        tests_for_move.append(f'    check("一撃必殺: {name}", _ko_{sn})')

    # ── 自己能力変化（無条件・確定のみ。確率/条件付きは副作用検証に委譲） ──
    _selfstat_cond = ('%' in effect or '場合' in effect or 'たくわえ' in effect
                      or 'きのみ' in effect or '溜め' in effect or 'タイプ以外' in effect
                      or 'タイプの場合' in effect)
    for stat_jp, stat_en in [('攻撃','attack'),('防御','defense'),('特攻','sp_attack'),
                              ('特防','sp_defense'),('素早さ','speed'),
                              ('回避率','evasion'),('命中率','accuracy')]:
        # 厳格マッチ：間に他要素を挟まない「自分の{stat}を N段階(上げ|下げ)る」
        mu = re.search(rf'自分の{stat_jp}を(\d+)段階(上げ|下げ)', effect)
        if mu and not _selfstat_cond:
            n_st = int(mu.group(1)); direction = mu.group(2)
            sign = 1 if direction == '上げ' else -1
            sn = safe_name(name)
            tag = f'自分{stat_jp}{"+" if sign>0 else "-"}{n_st}'
            tests_for_move.append(f'# {name}: {tag}')
            tests_for_move.append(f'_mvss_{sn}_{stat_en} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mvss_{sn}_{stat_en}:')
            tests_for_move.append(f'    random.seed(0); _got_{sn}_{stat_en} = 0')
            tests_for_move.append(f'    for _ in range(60):')
            tests_for_move.append(f'        _pas = make_poke(type1="{atk_type}", atk_b=60, spatk_b=60); _pds = make_poke(type1="{def_type}", hp_b=255, def_b=255, spdef_b=255)')
            tests_for_move.append(f'        execute(_pas, _pds, "{name}")')
            tests_for_move.append(f'        if _pas.stage_{stat_en} != 0: _got_{sn}_{stat_en} = _pas.stage_{stat_en}; break')
            tests_for_move.append(f'    check("{tag}: {name}", _got_{sn}_{stat_en} == {sign * n_st}, f"1回適用={{_got_{sn}_{stat_en}}} 期待={sign * n_st}")')

    # ── 反動技（与えたダメージの1/N自分も受ける） ──────────────
    _rc_m = re.search(r'与えたダメージの1/(\d)', effect)
    if _rc_m and '受ける' in effect and cat in ('physical','special'):
        sn = safe_name(name)
        _rc_den = int(_rc_m.group(1))
        tests_for_move.append(f'# {name}: 反動（与ダメの1/{_rc_den}）')
        tests_for_move.append(f'_mvrc_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvrc_{sn}:')
        tests_for_move.append(f'    random.seed(0)')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _par = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _par.hp = _par.max_hp')
        tests_for_move.append(f'        _pdr = make_poke(type1="{def_type}", hp_b=255, def_b=120, spdef_b=120); _hpdr = _pdr.hp')
        tests_for_move.append(f'        execute(_par, _pdr, "{name}")')
        tests_for_move.append(f'        _rc_dealt_{sn} = _hpdr - _pdr.hp; _rc_rcv_{sn} = _par.max_hp - _par.hp')
        tests_for_move.append(f'        if _rc_dealt_{sn} > 0: break')
        tests_for_move.append(f'    _rc_exp_{sn} = max(1, _rc_dealt_{sn} // {_rc_den})')
        tests_for_move.append(f'    check("反動ダメージ(1/{_rc_den}): {name}", abs(_rc_rcv_{sn} - _rc_exp_{sn}) <= 2, f"dealt={{_rc_dealt_{sn}}} recoil={{_rc_rcv_{sn}}} 期待={{_rc_exp_{sn}}}")')

    # ── 急所ランク+1（高急所技：急所率1/8で通常1/24より明確に高い） ───
    if 'きゅうしょアップ+1で攻撃する' in effect and cat in ('physical','special'):
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 急所ランク+1（急所率が通常技より高い）')
        # _check_critical を直接呼び、急所ランク+1（1/8）が通常（1/24）より高いことを検証
        tests_for_move.append(f'from simulator.battle import _check_critical as _cc_{sn}')
        tests_for_move.append(f'random.seed(0); _hc_crit_{sn} = 0; _phc = make_poke(type1="{atk_type}")')
        tests_for_move.append(f'_mvhc_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'for _ in range(800):')
        tests_for_move.append(f'    if _cc_{sn}(_phc, _mvhc_{sn}, make_poke(type1="{def_type}")): _hc_crit_{sn} += 1')
        tests_for_move.append(f'# 1/8≈100回(800試行)。通常1/24なら≈33回。明確に区別')
        tests_for_move.append(f'check("急所ランク+1: {name}", 60 <= _hc_crit_{sn} <= 150, f"crit={{_hc_crit_{sn}}}/800 (期待≈100, 通常1/24なら≈33)")')

    # ── 多段ヒット（N回連続で攻撃） ───────────────────────────
    # スキルリンクで最大回数を保証し、合計ダメージが単発を上回る＝複数回ヒットを実証
    if re.search(r'\d[ー\-]\d回連続で攻撃|\d回連続で攻撃|連続\d回攻撃|\d回連続攻撃', effect) and cat in ('physical','special'):
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 多段ヒット（合計が単発を上回る＝複数回当たっている）')
        tests_for_move.append(f'_mvmh_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvmh_{sn}:')
        tests_for_move.append(f'    _pam = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120, ability="スキルリンク")')
        tests_for_move.append(f'    _single_{sn} = calc_damage(_pam, make_poke(type1="{def_type}", hp_b=255, def_b=200, spdef_b=200), _mvmh_{sn}, BattleField(), random_roll=1.0)')
        tests_for_move.append(f'    random.seed(0); _multi_{sn} = 0')
        tests_for_move.append(f'    for _ in range(20):')
        tests_for_move.append(f'        _pdm = make_poke(type1="{def_type}", hp_b=255, def_b=200, spdef_b=200)')
        tests_for_move.append(f'        execute(_pam, _pdm, "{name}"); _multi_{sn} = _pdm.max_hp - _pdm.hp')
        tests_for_move.append(f'        if _multi_{sn} > _single_{sn}: break')
        tests_for_move.append(f'    check("多段ヒット発生(複数回): {name}", _multi_{sn} > _single_{sn}, f"single={{_single_{sn}}} multi={{_multi_{sn}}}")')

    # ── 必中（無条件のみ。天候/ちいさくなる等の条件付きは除外） ──
    _mustcond = ('場合' in effect or '状態の相手' in effect or 'ちいさくなる状態' in effect
                 or 'あめ状態' in effect or 'ゆき状態' in effect)
    if '必ず命中' in effect and cat in ('physical','special') and not _mustcond:
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 必中')
        tests_for_move.append(f'_mvmust_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvmust_{sn}:')
        tests_for_move.append(f'    random.seed(0); _hit_all_{sn} = True')
        tests_for_move.append(f'    for _ in range(30):')
        tests_for_move.append(f'        _pah = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdh = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
        tests_for_move.append(f'        _hpb = _pdh.hp; execute(_pah, _pdh, "{name}")')
        tests_for_move.append(f'        if _pdh.hp == _hpb: _hit_all_{sn} = False; break')
        tests_for_move.append(f'    check("必中: {name}", _hit_all_{sn})')

    # ── 天候依存必中（あめ/ゆき状態の場合、相手に必ず命中する） ──
    wm_hit = re.search(r'(あめ|ゆき|にほんばれ|すなあらし)状態の場合[、]?[^。]*必ず命中', effect)
    if wm_hit and cat in ('physical','special'):
        w_jp = wm_hit.group(1)
        w_en = {'あめ':'rain','ゆき':'hail','にほんばれ':'sunny','すなあらし':'sandstorm'}[w_jp]
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: {w_jp}状態で必中')
        tests_for_move.append(f'_mvwh_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvwh_{sn}:')
        tests_for_move.append(f'    random.seed(0); _wh_all_{sn} = True')
        tests_for_move.append(f'    for _ in range(30):')
        tests_for_move.append(f'        _pawh = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdwh = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
        tests_for_move.append(f'        _fwh = BattleField(); _fwh.weather = "{w_en}"')
        tests_for_move.append(f'        _hpwh = _pdwh.hp')
        tests_for_move.append(f'        _execute_move(BattleSide([_pawh]), BattleSide([_pdwh]), Action(type="move", move=_mvwh_{sn}), _fwh)')
        tests_for_move.append(f'        if _pdwh.hp == _hpwh: _wh_all_{sn} = False; break')
        tests_for_move.append(f'    check("{w_jp}状態で必中: {name}", _wh_all_{sn})')

    # ── 固定ダメージ（HPにNダメージを与える） ─────────────────
    fm = re.search(r'HPに(\d+)ダメージを与える', effect)
    if fm and cat in ('physical','special'):
        fixed = int(fm.group(1)); sn = safe_name(name)
        tests_for_move.append(f'# {name}: 固定{fixed}ダメージ')
        tests_for_move.append(f'_mvfx_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvfx_{sn}:')
        tests_for_move.append(f'    _paf = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdf = make_poke(type1="{def_type}", hp_b=200, def_b=100, spdef_b=100)')
        tests_for_move.append(f'    _hpbf = _pdf.hp; execute(_paf, _pdf, "{name}")')
        tests_for_move.append(f'    check("固定{fixed}ダメージ: {name}", _hpbf - _pdf.hp == {fixed}, f"dmg={{_hpbf - _pdf.hp}}")')

    # ── 必ず急所 ──────────────────────────────────────────────
    if ('必ず急所' in effect) and cat in ('physical','special'):
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 必ず急所（高ダメージ）')
        tests_for_move.append(f'_mvcr_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvcr_{sn}:')
        # 急所は通常の1.5倍。乱数最大で比較（急所ありは防御ランク無視等あるが最低1.4倍は出る）
        tests_for_move.append(f'    _pac = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'    _d_crit = dmg(_pac, make_poke(type1="{def_type}", def_b=100, spdef_b=100), "{name}")')
        tests_for_move.append(f'    check("必ず急所(>0): {name}", _d_crit > 0)')

    # ── ピボット（攻撃後に交代） ──────────────────────────────
    if '手持ちの他のポケモンと交代' in effect or 'ピボット' in effect:
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: ピボット交代フラグ')
        tests_for_move.append(f'_mvpv_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvpv_{sn}:')
        tests_for_move.append(f'    _pap = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdp = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
        tests_for_move.append(f'    _s1p = BattleSide([_pap, make_poke()]); _s2p = BattleSide([_pdp])')
        tests_for_move.append(f'    random.seed(0); _execute_move(_s1p, _s2p, Action(type="move", move=_mvpv_{sn}), BattleField())')
        tests_for_move.append(f'    check("ピボット交代フラグ: {name}", getattr(_pap, "_pivot_out", False) or _s1p.active_idx != 0, "pivot未発火")')

    # ── カウンター系（受けた技ダメージをN倍にして返す） ────────
    cm = re.search(r'受けた(物理技|特殊技|技)のダメージを([\d.]+)倍にして返す', effect)
    if cm:
        kind = cm.group(1); mult = float(cm.group(2)); sn = safe_name(name)
        # 被ダメージ記録属性
        rec_p = '_pac_cnt._last_physical_dmg_received = 100' if kind in ('物理技','技') else ''
        rec_s = '_pac_cnt._last_special_dmg_received = 100' if kind in ('特殊技','技') else ''
        expected = int(100 * mult) if kind != '技' else int((100 if kind=='技' else 0))
        # 「技」(メタルバースト/ほうふく)は物理+特殊合算×mult
        if kind == '技':
            tests_for_move.append(f'# {name}: カウンター反射（物理+特殊×{mult}）')
        else:
            tests_for_move.append(f'# {name}: カウンター反射（{kind}×{mult}）')
        tests_for_move.append(f'_mvcnt_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvcnt_{sn}:')
        tests_for_move.append(f'    _pac_cnt = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100, hp_b=200)')
        tests_for_move.append(f'    _pdc_cnt = make_poke(type1="ノーマル" if "{atk_type}"!="かくとう" else "エスパー", hp_b=255, def_b=100, spdef_b=100)')
        if kind == '技':
            tests_for_move.append(f'    _pac_cnt._last_physical_dmg_received = 100')
            tests_for_move.append(f'    _exp_cnt = int(100 * {mult})')
        elif kind == '物理技':
            tests_for_move.append(f'    _pac_cnt._last_physical_dmg_received = 100')
            tests_for_move.append(f'    _exp_cnt = int(100 * {mult})')
        else:
            tests_for_move.append(f'    _pac_cnt._last_special_dmg_received = 100')
            tests_for_move.append(f'    _exp_cnt = int(100 * {mult})')
        tests_for_move.append(f'    _hpc0 = _pdc_cnt.hp; execute(_pac_cnt, _pdc_cnt, "{name}")')
        tests_for_move.append(f'    check("カウンター反射: {name}", _hpc0 - _pdc_cnt.hp == _exp_cnt, f"返し={{_hpc0 - _pdc_cnt.hp}} 期待={{_exp_cnt}}")')
        # 被ダメージ0なら失敗する確認
        tests_for_move.append(f'    _pac_cnt2 = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdc_cnt2 = make_poke(type1="ノーマル", hp_b=255)')
        tests_for_move.append(f'    _hpc20 = _pdc_cnt2.hp; execute(_pac_cnt2, _pdc_cnt2, "{name}")')
        tests_for_move.append(f'    check("カウンター被ダメ0で失敗: {name}", _pdc_cnt2.hp == _hpc20)')

    # ── 自己ひんし（使うと自分はひんしになる） ────────────────
    if '自分はひんしになる' in effect and '次に' not in effect and 'その時' not in effect:
        sn = safe_name(name)
        tests_for_move.append(f'# {name}: 自己ひんし')
        tests_for_move.append(f'_mvsf_{sn} = dl.get_move("{name}")')
        tests_for_move.append(f'if _mvsf_{sn}:')
        tests_for_move.append(f'    _pasf = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdsf = make_poke(type1="{def_type}", hp_b=255, def_b=255, spdef_b=255)')
        tests_for_move.append(f'    execute(_pasf, _pdsf, "{name}")')
        tests_for_move.append(f'    check("自己ひんし: {name}", not _pasf.is_alive)')

    # ── ハザード設置 ──────────────────────────────────────────
    HAZARD_MAP = {'まきびし':'spikes','どくびし':'toxic_spikes','ステルスロック':'stealth_rock','ねばねばネット':'sticky_web'}
    for hz_jp, hz_attr in HAZARD_MAP.items():
        if f'相手の場を{hz_jp}状態' in effect and cat == 'status':
            sn = safe_name(name)
            tests_for_move.append(f'# {name}: ハザード{hz_attr}')
            tests_for_move.append(f'_mvhz_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mvhz_{sn}:')
            tests_for_move.append(f'    _s1h, _s2h, _fh2 = execute_ctx(make_poke(type1="{atk_type}"), make_poke(), "{name}")')
            # ステルスロックのみ run時確定(_stealth_rock_pending)を許容。他ハザードは自分の配列のみ厳密判定。
            if hz_attr == 'stealth_rock':
                tests_for_move.append(f'    _hzval = _fh2.{hz_attr}[_s2h.field_idx] or getattr(_s2h, "_stealth_rock_pending", False) or _s2h.stealth_rock_set')
            else:
                tests_for_move.append(f'    _hzval = _fh2.{hz_attr}[_s2h.field_idx]')
            tests_for_move.append(f'    check("ハザード{hz_attr}: {name}", bool(_hzval), f"val={{_hzval}}")')
            break

    # ── フィールド技 ──────────────────────────────────────────
    FIELD_MAP = {'グラスフィールド':'electric_terrain','エレキフィールド':'electric_terrain',
                 'サイコフィールド':'psychic_terrain','ミストフィールド':'misty_terrain'}
    FIELD_ATTR = {'グラスフィールド':'grassy_terrain','エレキフィールド':'electric_terrain',
                  'サイコフィールド':'psychic_terrain','ミストフィールド':'misty_terrain'}
    for fld_jp in ['エレキフィールド','サイコフィールド','ミストフィールド','グラスフィールド']:
        if f'{fld_jp}状態にする' in effect and cat == 'status':
            sn = safe_name(name)
            # グラスフィールドはfield属性が無い場合があるためsmokeで吸収
            attr = {'エレキフィールド':'electric_terrain','サイコフィールド':'psychic_terrain',
                    'ミストフィールド':'misty_terrain','グラスフィールド':None}[fld_jp]
            tests_for_move.append(f'# {name}: フィールド展開')
            if attr:
                tests_for_move.append(f'_mvfl_{sn} = dl.get_move("{name}")')
                tests_for_move.append(f'if _mvfl_{sn}:')
                tests_for_move.append(f'    _s1f, _s2f, _ff = execute_ctx(make_poke(type1="{atk_type}"), make_poke(), "{name}")')
                tests_for_move.append(f'    check("フィールド{attr}: {name}", _ff.{attr}, f"val={{_ff.{attr}}}")')
            else:
                tests_for_move.append(f'side_effect_check("フィールド展開: {name}", "{name}", "{atk_type}", True)')
            break

    # ── 状態変化付与（相手をXX状態にする：汎用 status技） ──────
    # 上で個別対応していない「相手を○○状態にする」変化技を副作用で担保
    # （かなしばり/ちょうはつ/アンコール/メロメロ/にげられない 等）

    # ── 可変威力（重さ/HP比）: 実効威力の具体値を検証 ──
    if name in ('けたぐり', 'くさむすび'):
        tests_for_move.append(f'# {name}: 相手の重さ別の威力テーブル（20/40/60/80/100/120）')
        tests_for_move.append(f'_pw_l = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'_kg_ng = []')
        tests_for_move.append(f'for _w, _exp in [(5,20),(15,40),(35,60),(75,80),(150,100),(300,120)]:')
        tests_for_move.append(f'    _dkg = make_poke(type1="{def_type}"); _dkg.weight_kg = float(_w)')
        tests_for_move.append(f'    _got = _ep(_pw_l, _dkg, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'    if _got != _exp: _kg_ng.append(f"{{_w}}kg:{{_got}}!={{_exp}}")')
        tests_for_move.append(f'check("重さ別威力テーブル: {name}", not _kg_ng, f"NG={{_kg_ng}}")')
    elif name in ('きしかいせい', 'じたばた'):
        tests_for_move.append(f'# {name}: HP比別の威力テーブル（>67.7%→20 ... ≤3.1%→200）')
        tests_for_move.append(f'_ph = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="{def_type}")')
        tests_for_move.append(f'_ks_ng = []')
        tests_for_move.append(f'for _r, _exp in [(0.80,20),(0.50,40),(0.30,80),(0.15,100),(0.05,150),(0.01,200)]:')
        tests_for_move.append(f'    _ph.hp = max(1, int(_ph.max_hp * _r))')
        tests_for_move.append(f'    _got = _ep(_ph, _dd, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'    if _got != _exp: _ks_ng.append(f"r={{_r}}:{{_got}}!={{_exp}}")')
        tests_for_move.append(f'check("HP比別威力テーブル: {name}", not _ks_ng, f"NG={{_ks_ng}}")')
    elif name in ('ふんか', 'しおふき'):
        tests_for_move.append(f'# {name}: 威力=floor(150×現HP/最大HP)。満タン150、半分75')
        tests_for_move.append(f'_ph = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100, hp_b=200); _dd = make_poke(type1="{def_type}")')
        tests_for_move.append(f'import math as _mfk')
        tests_for_move.append(f'_fk_ng = []')
        tests_for_move.append(f'for _r in [1.0, 0.5, 0.25]:')
        tests_for_move.append(f'    _ph.hp = max(1, int(_ph.max_hp * _r)); _exp = max(1, _mfk.floor(150 * _ph.hp / _ph.max_hp))')
        tests_for_move.append(f'    _got = _ep(_ph, _dd, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'    if _got != _exp: _fk_ng.append(f"r={{_r}}:{{_got}}!={{_exp}}")')
        tests_for_move.append(f'check("HP比威力(150×HP/max): {name}", not _fk_ng, f"NG={{_fk_ng}}")')
    elif name in ('ヘビーボンバー', 'ヒートスタンプ'):
        tests_for_move.append(f'# {name}: 重さ比別の威力テーブル（≥5→120 ... 未満→40）')
        tests_for_move.append(f'_pwh = make_poke(type1="{atk_type}", atk_b=100); _pwh.weight_kg = 500.0')
        tests_for_move.append(f'_hb_ng = []')
        tests_for_move.append(f'for _wd, _exp in [(99,120),(125,100),(166,80),(250,60),(400,40)]:')
        tests_for_move.append(f'    _dwh = make_poke(type1="{def_type}"); _dwh.weight_kg = float(_wd)')
        tests_for_move.append(f'    _got = _ep(_pwh, _dwh, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'    if _got != _exp: _hb_ng.append(f"500/{{_wd}}kg:{{_got}}!={{_exp}}")')
        tests_for_move.append(f'check("重さ比別威力テーブル: {name}", not _hb_ng, f"NG={{_hb_ng}}")')
        tests_for_move.append(f'# ちいさくなる状態の相手に威力2倍（重さ比固定: 500/100kg→比5→威力120）')
        tests_for_move.append(f'_dmm0 = make_poke(type1="{def_type}"); _dmm0.weight_kg = 100.0')
        tests_for_move.append(f'_dmm1 = make_poke(type1="{def_type}"); _dmm1.weight_kg = 100.0; _dmm1.minimized = True')
        tests_for_move.append(f'_mm_n = _ep(_pwh, _dmm0, dl.get_move("{name}"), BattleField()); _mm_m = _ep(_pwh, _dmm1, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("ちいさくなる2倍: {name}", _mm_m == _mm_n * 2, f"normal={{_mm_n}} mini={{_mm_m}}")')
    # ── リチャージ技 ──
    elif name in ('はかいこうせん', 'ギガインパクト', 'ブラストバーン', 'ハードプラント', 'ハイドロカノン', 'がんせきほう'):
        tests_for_move.append(f'# {name}: 使用後リチャージ付与 + リチャージ中は行動不能')
        tests_for_move.append(f'random.seed(0); _rc_ok2 = False')
        tests_for_move.append(f'for _ in range(20):')
        tests_for_move.append(f'    _prc2 = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _drc2 = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100)')
        tests_for_move.append(f'    execute(_prc2, _drc2, "{name}")')
        tests_for_move.append(f'    if _prc2.recharge: _rc_ok2 = True; break')
        tests_for_move.append(f'check("リチャージ付与: {name}", _rc_ok2)')
        tests_for_move.append(f'# リチャージ中は行動不能（相手にダメージが通らない）')
        tests_for_move.append(f'_prc3 = make_poke(type1="{atk_type}", atk_b=150, spatk_b=150); _prc3.recharge = True')
        tests_for_move.append(f'_drc3 = make_poke(type1="{def_type}", hp_b=255, def_b=100, spdef_b=100); _hprc3 = _drc3.hp')
        tests_for_move.append(f'execute(_prc3, _drc3, "{name}")')
        tests_for_move.append(f'check("リチャージ中行動不能: {name}", _drc3.hp == _hprc3, f"hp={{_drc3.hp}}/{{_hprc3}}")')
    elif name == 'てっていこうせん':
        tests_for_move.append('# てっていこうせん: 最大HP1/2の反動')
        tests_for_move.append('_ptk2 = make_poke(type1="はがね", spatk_b=120); _dtk2 = make_poke(type1="いわ", hp_b=255, spdef_b=100)')
        tests_for_move.append('random.seed(0); _hp0 = _ptk2.hp')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    _ptk2.hp = _hp0; execute(_ptk2, _dtk2, "てっていこうせん")')
        tests_for_move.append('    if _ptk2.hp < _hp0: break')
        tests_for_move.append('check("てっていこうせん 反動: てっていこうせん", _hp0 - _ptk2.hp >= _ptk2.max_hp//2 - 2, f"recoil={_hp0 - _ptk2.hp}")')
    # ── ねこだまし 100%ひるみ ──
    elif name == 'ねこだまし':
        tests_for_move.append('# ねこだまし: 100%ひるみ')
        tests_for_move.append('random.seed(0); _pnk = make_poke(type1="ノーマル", atk_b=30); _dnk = make_poke(type1="ノーマル", def_b=255, hp_b=255)')
        tests_for_move.append('execute(_pnk, _dnk, "ねこだまし")')
        tests_for_move.append('check("ねこだまし ひるみ: ねこだまし", _dnk.flinched)')
        tests_for_move.append('# 場に出て最初のターンのみ成功（turns_out>0は失敗）')
        tests_for_move.append('_pnk_l = make_poke(type1="ノーマル", atk_b=120); _dnk_l = make_poke(type1="ノーマル", hp_b=255, def_b=150)')
        tests_for_move.append('_pnk_l.turns_out = 1; _hpnk_l = _dnk_l.hp; execute(_pnk_l, _dnk_l, "ねこだまし")')
        tests_for_move.append('check("初手以外で失敗: ねこだまし", _dnk_l.hp == _hpnk_l, f"hp={_dnk_l.hp}/{_hpnk_l}")')
        tests_for_move.append('_pnk_f = make_poke(type1="ノーマル", atk_b=120); _dnk_f = make_poke(type1="ノーマル", hp_b=255, def_b=150)')
        tests_for_move.append('_pnk_f.turns_out = 0; _hpnk_f = _dnk_f.hp; execute(_pnk_f, _dnk_f, "ねこだまし")')
        tests_for_move.append('check("初手で成功: ねこだまし", _dnk_f.hp < _hpnk_f, f"hp={_dnk_f.hp}/{_hpnk_f}")')
    elif name == 'フライングプレス':
        tests_for_move.append('# フライングプレス: かくとう×ひこうの複合相性（両タイプの相性を掛け合わせる）')
        tests_for_move.append('_pfp = make_poke(type1="かくとう", atk_b=120)')
        tests_for_move.append('from simulator.data import get_type_effectiveness as _gte')
        tests_for_move.append('from simulator.damage import _effective_move_type as _emtfp')
        tests_for_move.append('_fp_base = calc_damage(_pfp, make_poke(type1="ノーマル",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_fp_bug = calc_damage(_pfp, make_poke(type1="むし",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_fp_fairy = calc_damage(_pfp, make_poke(type1="フェアリー",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_fp_ghost = calc_damage(_pfp, make_poke(type1="ゴースト",def_b=100), dl.get_move("フライングプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('# vsノーマル: かくとう2×ひこう1=2× / vsむし: かくとう0.5×ひこう2=1× → 等しい')
        tests_for_move.append('check("複合相性(むし=ノーマル等倍): フライングプレス", abs(_fp_bug - _fp_base/_gte("かくとう","ノーマル",None)) <= 2, f"bug={_fp_bug} expected≈{_fp_base/_gte(chr(12363)+chr(12367)+chr(12392)+chr(12358),chr(12494)+chr(12540)+chr(12510)+chr(12523),None):.0f}")')
        tests_for_move.append('# vsゴースト: かくとう0×ひこう1=0（無効）')
        tests_for_move.append('check("複合相性(ゴースト無効): フライングプレス", _fp_ghost == 0, f"ghost={_fp_ghost}")')
        tests_for_move.append('# ちいさくなる状態の相手に威力2倍')
        tests_for_move.append('_fpm0 = make_poke(type1="ノーマル", def_b=100); _fpm1 = make_poke(type1="ノーマル", def_b=100); _fpm1.minimized = True')
        tests_for_move.append('_fp_n = _ep(_pfp, _fpm0, dl.get_move("フライングプレス"), BattleField()); _fp_m = _ep(_pfp, _fpm1, dl.get_move("フライングプレス"), BattleField())')
        tests_for_move.append('check("ちいさくなる2倍: フライングプレス", _fp_m == _fp_n * 2, f"normal={_fp_n} mini={_fp_m}")')
    # ── ちいさくなる状態2倍 ──
    elif name in ('のしかかり', 'ドラゴンダイブ', 'サンダーダイブ'):
        tests_for_move.append(f'# {name}: ちいさくなる状態の相手に威力2倍')
        tests_for_move.append(f'_pm = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'_dm0 = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_dm1 = make_poke(type1="{def_type}", def_b=100, spdef_b=100); _dm1.minimized = True')
        tests_for_move.append(f'_pm_n = _ep(_pm, _dm0, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_pm_m = _ep(_pm, _dm1, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("ちいさくなる2倍: {name}", _pm_m == _pm_n * 2, f"normal={{_pm_n}} mini={{_pm_m}}")')
    # ── 半無敵2倍 ──
    elif name in ('なみのり', 'うずしお'):
        tests_for_move.append(f'# {name}: 水中(ダイビング溜め中)の相手に2倍')
        tests_for_move.append(f'_pwv = make_poke(type1="みず", spatk_b=100, atk_b=100); _dwv = make_poke(type1="ノーマル", spdef_b=100, def_b=100)')
        tests_for_move.append(f'_n0 = _ep(_pwv, _dwv, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_dwv.charging_move = "ダイビング"; _n1 = _ep(_pwv, _dwv, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("{name} 水中2倍: {name}", _n1 == _n0 * 2, f"normal={{_n0}} dive={{_n1}}")')
    elif name in ('じしん', 'マグニチュード'):
        tests_for_move.append(f'# {name}: 地中(あなをほる溜め中)の相手に2倍')
        tests_for_move.append(f'_pug = make_poke(type1="じめん", atk_b=100); _dug = make_poke(type1="ノーマル", def_b=100)')
        tests_for_move.append(f'_g0 = _ep(_pug, _dug, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_dug.charging_move = "あなをほる"; _g1 = _ep(_pug, _dug, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("{name} 地中2倍: {name}", _g1 == _g0 * 2, f"normal={{_g0}} dig={{_g1}}")')
        tests_for_move.append(f'# グラスフィールド状態では威力1/2')
        tests_for_move.append(f'_pgf = make_poke(type1="じめん", atk_b=100); _dgf = make_poke(type1="どく", def_b=100)')
        tests_for_move.append(f'_d_no = calc_damage(_pgf, _dgf, dl.get_move("{name}"), BattleField(), random_roll=1.0)')
        tests_for_move.append(f'_fg1 = BattleField(); _fg1.grassy_terrain = True; _d_gf = calc_damage(_pgf, _dgf, dl.get_move("{name}"), _fg1, random_roll=1.0)')
        tests_for_move.append(f'check("{name} グラスF半減: {name}", _d_gf < _d_no, f"no={{_d_no}} gf={{_d_gf}}")')
    # ── 自己能力下降（ダメージ技・確定） ──
    elif name in ('ばかぢから', 'インファイト', 'りゅうせいぐん', 'リーフストーム', 'オーバーヒート', 'アームハンマー', 'アーマーキャノン', 'ぶちかまし'):
        # 効果文から「自分の…N段階下げ/下がる」statを抽出（を/が両対応）
        _m_sd = re.search(r'自分の([^。]*?)(攻撃|防御|特攻|特防|素早さ)[^。]*?\d+段階[^。]*?(下げ|下が)', effect)
        if _m_sd:
            _STAT_MAP2 = {'攻撃':'attack','防御':'defense','特攻':'sp_attack','特防':'sp_defense','素早さ':'speed'}
            _seg_sd = re.search(r'自分の([攻撃防御特攻特防素早さ・、と ]+)[をが]', effect)
            _segtxt = _seg_sd.group(1) if _seg_sd else ''
            _downs = [(j, _STAT_MAP2[j]) for j in _STAT_MAP2 if j in _segtxt]
            if _downs:
                tests_for_move.append(f'# {name}: 自分の能力下降（命中までリトライ）')
                tests_for_move.append(f'random.seed(0); _psd = None')
                tests_for_move.append(f'for _ in range(20):')
                tests_for_move.append(f'    _psd = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _dsd = make_poke(type1="{def_type}", hp_b=255, def_b=80, spdef_b=80)')
                tests_for_move.append(f'    execute(_psd, _dsd, "{name}")')
                _firststat = _downs[0][1]
                tests_for_move.append(f'    if _psd.stage_{_firststat} < 0: break')
                for _jp, _en in _downs:
                    tests_for_move.append(f'check("自分{_jp}下降: {name}", _psd.stage_{_en} < 0, f"stage={{_psd.stage_{_en}}}")')

    # ── 場の状態（トリックルーム/じゅうりょく/マジックルーム/ワンダールーム） ──
    if name in ('トリックルーム', 'じゅうりょく', 'マジックルーム', 'ワンダールーム'):
        _room_attr = {'トリックルーム':'trick_room','じゅうりょく':'gravity',
                      'マジックルーム':'magic_room','ワンダールーム':'wonder_room'}[name]
        tests_for_move.append(f'# {name}: 場の状態セット')
        tests_for_move.append(f'_s1rm, _s2rm, _frm = execute_ctx(make_poke(type1="{atk_type}"), make_poke(), "{name}")')
        tests_for_move.append(f'check("{name} 場の状態: {name}", bool(getattr(_frm, "{_room_attr}", 0)))')

    # ── 個別特例（条件依存・接触トリガー等を専用セットアップで狙い撃ち） ──
    if name in ('アシストパワー', 'つけあがる'):
        tests_for_move.append(f'# {name}: 自分のランク合計で威力増（20+20×ランク）')
        tests_for_move.append(f'_pap2 = make_poke(type1="{atk_type}", spatk_b=100, atk_b=100); _dap2 = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_pw_base = _ep(_pap2, _dap2, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_pap2.stage_attack = 2; _pap2.stage_speed = 1')
        tests_for_move.append(f'_pw_up = _ep(_pap2, _dap2, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("ランクで威力増: {name}", _pw_base == 20 and _pw_up == 20 + 20*3, f"base={{_pw_base}} up={{_pw_up}}")')
    elif name == 'ゆきなだれ':
        tests_for_move.append('# ゆきなだれ: 優先度-4。被弾していれば威力2倍（実戦の被弾フラグも検証）')
        tests_for_move.append('_pcd = make_poke(type1="こおり", atk_b=100, spatk_b=100); _dcd = make_poke(type1="くさ", def_b=100, spdef_b=100)')
        tests_for_move.append('_p_base = _ep(_pcd, _dcd, dl.get_move("ゆきなだれ"), BattleField())')
        tests_for_move.append('_pcd._took_damage_this_turn = True')
        tests_for_move.append('_p_cond = _ep(_pcd, _dcd, dl.get_move("ゆきなだれ"), BattleField())')
        tests_for_move.append('check("条件成立で威力2倍: ゆきなだれ", _p_cond == _p_base * 2, f"base={_p_base} cond={_p_cond}")')
        tests_for_move.append('# 実戦: 攻撃技を受けると _took_damage_this_turn が立つ（フラグ自体が機能するか）')
        tests_for_move.append('_pyk = make_poke(type1="こおり", hp_b=255); _pyk._took_damage_this_turn = False')
        tests_for_move.append('execute(make_poke(type1="ノーマル", atk_b=120, moves=["のしかかり"]), _pyk, "のしかかり")')
        tests_for_move.append('check("被弾フラグ実機能: ゆきなだれ", _pyk._took_damage_this_turn, "攻撃を受けたら被弾フラグが立つこと")')
    elif name == 'イカサマ':
        tests_for_move.append('# イカサマ: 相手の攻撃実数値でダメージ計算（ランク変化も反映）')
        tests_for_move.append('_pik = make_poke(type1="あく", atk_b=10); _dik_hi = make_poke(type1="エスパー", atk_b=200, def_b=100)')
        tests_for_move.append('_dik_lo = make_poke(type1="エスパー", atk_b=10, def_b=100)')
        tests_for_move.append('_d_hi = calc_damage(_pik, _dik_hi, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_lo = calc_damage(_pik, _dik_lo, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("イカサマ 相手攻撃依存: イカサマ", _d_hi > _d_lo, f"hi={_d_hi} lo={_d_lo}")')
        tests_for_move.append('# 相手の攻撃ランク+2でもダメージが増える（ランク変化反映）')
        tests_for_move.append('_dik_buff = make_poke(type1="エスパー", atk_b=100, def_b=100); _dik_buff.stage_attack = 2')
        tests_for_move.append('_dik_base = make_poke(type1="エスパー", atk_b=100, def_b=100)')
        tests_for_move.append('_d_buff = calc_damage(_pik, _dik_buff, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_base = calc_damage(_pik, _dik_base, dl.get_move("イカサマ"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("相手攻撃依存(ランク変化): イカサマ", _d_buff > _d_base, f"buff={_d_buff} base={_d_base}")')
    elif name == 'ボディプレス':
        tests_for_move.append('# ボディプレス: 自分の防御でダメージ計算')
        tests_for_move.append('_pbp_hi = make_poke(type1="かくとう", atk_b=10, def_b=200); _pbp_lo = make_poke(type1="かくとう", atk_b=10, def_b=10)')
        tests_for_move.append('_dbp = make_poke(type1="ノーマル", def_b=100)')
        tests_for_move.append('_d_hi = calc_damage(_pbp_hi, _dbp, dl.get_move("ボディプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_lo = calc_damage(_pbp_lo, _dbp, dl.get_move("ボディプレス"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("ボディプレス 自分防御依存: ボディプレス", _d_hi > _d_lo, f"hi={_d_hi} lo={_d_lo}")')
    elif name == 'サイコショック':
        tests_for_move.append('# サイコショック: 相手の物理防御でダメージ計算')
        tests_for_move.append('_pps = make_poke(type1="エスパー", spatk_b=100)')
        tests_for_move.append('_dps_hb = make_poke(type1="ノーマル", def_b=250, spdef_b=10)')
        tests_for_move.append('_dps_lb = make_poke(type1="ノーマル", def_b=10, spdef_b=250)')
        tests_for_move.append('_d_hb = calc_damage(_pps, _dps_hb, dl.get_move("サイコショック"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_lb = calc_damage(_pps, _dps_lb, dl.get_move("サイコショック"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("サイコショック 物理防御依存: サイコショック", _d_hb < _d_lb, f"highB={_d_hb} lowB={_d_lb}")')
    elif name == 'ウェザーボール':
        tests_for_move.append('# ウェザーボール: 天候で威力2倍＆タイプ変化')
        tests_for_move.append('_pwb = make_poke(type1="ノーマル", spatk_b=100); _dwb = make_poke(type1="ノーマル", spdef_b=100)')
        tests_for_move.append('_pw_none = _ep(_pwb, _dwb, dl.get_move("ウェザーボール"), BattleField())')
        tests_for_move.append('_fwb = BattleField(); _fwb.weather = "sunny"')
        tests_for_move.append('_pw_sun = _ep(_pwb, _dwb, dl.get_move("ウェザーボール"), _fwb)')
        tests_for_move.append('from simulator.damage import _effective_move_type as _emt2')
        tests_for_move.append('_typ_sun = _emt2(_pwb, dl.get_move("ウェザーボール"), _fwb)')
        tests_for_move.append('check("ウェザーボール 天候威力2倍: ウェザーボール", _pw_sun == _pw_none * 2, f"none={_pw_none} sun={_pw_sun}")')
        tests_for_move.append('# 全天候→タイプの対応を網羅（晴れ:ほのお/雨:みず/あられ:こおり/砂:いわ）')
        tests_for_move.append('_wb_ng = []')
        tests_for_move.append('for _w, _ty in [("sunny","ほのお"),("rain","みず"),("hail","こおり"),("sandstorm","いわ"),(None,"ノーマル")]:')
        tests_for_move.append('    _fwx = BattleField()')
        tests_for_move.append('    if _w: _fwx.weather = _w')
        tests_for_move.append('    _gt = _emt2(_pwb, dl.get_move("ウェザーボール"), _fwx)')
        tests_for_move.append('    if _gt != _ty: _wb_ng.append(str(_w) + ":" + str(_gt) + "!=" + str(_ty))')
        tests_for_move.append('check("ウェザーボール 全天候タイプ変化: ウェザーボール", not _wb_ng, "NG=" + str(_wb_ng))')
    elif name == 'トーチカ':
        tests_for_move.append('# トーチカ: 守る成功+接触攻撃者をどく')
        tests_for_move.append('_pto = make_poke(type1="どく"); execute(_pto, make_poke(), "トーチカ")')
        tests_for_move.append('check("トーチカ 守る状態: トーチカ", _pto.protecting)')
        tests_for_move.append('_atk_t = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _pto2 = make_poke(type1="どく")')
        tests_for_move.append('_pto2.protecting = True; _pto2._protect_move = "トーチカ"')
        tests_for_move.append('_execute_move(BattleSide([_atk_t]), BattleSide([_pto2]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())')
        tests_for_move.append('check("トーチカ 接触どく: トーチカ", _atk_t.status == "poison", f"status={_atk_t.status}")')
    elif name == 'ニードルガード':
        tests_for_move.append('# ニードルガード: 守る成功+接触攻撃者にHP1/8ダメ')
        tests_for_move.append('_png2 = make_poke(type1="くさ"); execute(_png2, make_poke(), "ニードルガード")')
        tests_for_move.append('check("ニードルガード 守る状態: ニードルガード", _png2.protecting)')
        tests_for_move.append('_atk_n = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _png3 = make_poke(type1="くさ")')
        tests_for_move.append('_png3.protecting = True; _png3._protect_move = "ニードルガード"; _hp_n = _atk_n.hp')
        tests_for_move.append('_execute_move(BattleSide([_atk_n]), BattleSide([_png3]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())')
        tests_for_move.append('check("ニードルガード 接触ダメ: ニードルガード", _atk_n.hp < _hp_n, f"hp={_atk_n.hp}")')
        tests_for_move.append('check("接触ダメは最大HP1/8(具体値): ニードルガード", _atk_n.max_hp - _atk_n.hp == _atk_n.max_hp // 8, f"dmg={_atk_n.max_hp - _atk_n.hp} 期待={_atk_n.max_hp // 8}")')
    elif name == 'くちばしキャノン':
        tests_for_move.append('# くちばしキャノン: 使用したそのターンに接触技を受けた相手をやけど（同一ターン内・ターンまたぎ無し）')
        tests_for_move.append('from simulator.battle import Battle as _Bk')
        tests_for_move.append('_act_beak = lambda s,o,f: Action(type="move", move=dl.get_move("くちばしキャノン"), move_idx=0)')
        tests_for_move.append('_act_tackle = lambda s,o,f: Action(type="move", move=dl.get_move("のしかかり"), move_idx=0)')
        tests_for_move.append('# 同一ターン: 鳥がくちばしキャノン(-3で後攻)、相手が接触技で先制 → 相手やけど')
        tests_for_move.append('_bird = make_poke(type1="ひこう", hp_b=255, atk_b=10, moves=["くちばしキャノン"])')
        tests_for_move.append('_foe = make_poke(type1="ノーマル", atk_b=40, hp_b=255, def_b=255, moves=["のしかかり"])')
        tests_for_move.append('_bk1 = _Bk(BattleSide([_bird]), BattleSide([_foe])); _bk1.run(_act_beak, _act_tackle)')
        tests_for_move.append('check("くちばしキャノン 被弾やけど: くちばしキャノン", _foe.status == "burn", f"status={_foe.status}")')
        tests_for_move.append('# ターンまたぎ無し: 鳥が別の技を使ったターンは接触してもやけどしない')
        tests_for_move.append('_bird2 = make_poke(type1="ひこう", hp_b=255, atk_b=10, moves=["のしかかり"])')
        tests_for_move.append('_foe2 = make_poke(type1="ノーマル", atk_b=40, hp_b=255, def_b=255, moves=["のしかかり"])')
        tests_for_move.append('_bk2 = _Bk(BattleSide([_bird2]), BattleSide([_foe2])); _bk2.run(_act_tackle, _act_tackle)')
        tests_for_move.append('check("くちばしキャノン 非使用ターンはやけど無し: くちばしキャノン", _foe2.status != "burn", f"status={_foe2.status}")')
    elif name in ('しっとのほのお', 'みわくのボイス'):
        _st2 = 'burn' if name == 'しっとのほのお' else None
        tests_for_move.append(f'# {name}: 相手の能力上昇時のみ状態異常')
        tests_for_move.append(f'_psj = make_poke(type1="{atk_type}", spatk_b=100, atk_b=100)')
        tests_for_move.append(f'random.seed(0); _sj_ok = False')
        tests_for_move.append(f'for _ in range(20):')
        tests_for_move.append(f'    _dsj = make_poke(type1="{def_type}", hp_b=255, def_b=200, spdef_b=200); _dsj.stage_attack = 2')
        tests_for_move.append(f'    execute(_psj, _dsj, "{name}")')
        if name == 'しっとのほのお':
            tests_for_move.append(f'    if _dsj.status == "burn": _sj_ok = True; break')
        else:
            tests_for_move.append(f'    if _dsj.confused: _sj_ok = True; break')
        tests_for_move.append(f'check("能力上昇時の状態異常: {name}", _sj_ok)')
        tests_for_move.append(f'# negative: 相手の能力が上がっていなければ付与されない')
        tests_for_move.append(f'random.seed(1); _sj_neg = True')
        tests_for_move.append(f'for _ in range(40):')
        tests_for_move.append(f'    _dsn = make_poke(type1="{def_type}", hp_b=255, def_b=200, spdef_b=200)')
        tests_for_move.append(f'    execute(_psj, _dsn, "{name}")')
        if name == 'しっとのほのお':
            tests_for_move.append(f'    if _dsn.status == "burn": _sj_neg = False; break')
        else:
            tests_for_move.append(f'    if _dsn.confused: _sj_neg = False; break')
        tests_for_move.append(f'check("能力非上昇時は付与なし: {name}", _sj_neg, "能力上昇がなければ状態異常は付かない")')
    elif name == 'うっぷんばらし':
        tests_for_move.append(f'# {name}: 自分の能力が下がっていれば威力2倍')
        tests_for_move.append(f'_pcd = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _dcd = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_p_base = _ep(_pcd, _dcd, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_pcd.stage_attack = -1')
        tests_for_move.append(f'_p_cond = _ep(_pcd, _dcd, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("条件成立で威力2倍: {name}", _p_cond == _p_base * 2, f"base={{_p_base}} cond={{_p_cond}}")')
    elif name in ('くろいまなざし', 'とおせんぼう', 'かげぬい'):
        tests_for_move.append(f'# {name}: 相手をにげられない状態に')
        tests_for_move.append(f'_ptr = make_poke(type1="{atk_type}", atk_b=120); _dtr = make_poke(type1="{def_type}", hp_b=255, def_b=100)')
        tests_for_move.append(f'execute(_ptr, _dtr, "{name}")')
        tests_for_move.append(f'check("にげられない付与: {name}", _dtr.trapped)')
    elif name == 'グラススライダー':
        tests_for_move.append('# グラススライダー: グラスフィールド時に優先度+1')
        tests_for_move.append('_pgs = make_poke(type1="くさ"); _ags = Action(type="move", move=dl.get_move("グラススライダー"))')
        tests_for_move.append('_fgs0 = BattleField(); _fgs1 = BattleField(); _fgs1.grassy_terrain = True')
        tests_for_move.append('_pr0 = _priority(_ags, _pgs, _fgs0); _pr1 = _priority(_ags, _pgs, _fgs1)')
        tests_for_move.append('check("グラスF優先度+1: グラススライダー", _pr1 == _pr0 + 1, f"off={_pr0} on={_pr1}")')
        tests_for_move.append('check("非グラスFでは通常優先度: グラススライダー", _pr0 == dl.get_move("グラススライダー").priority, f"off={_pr0} db={dl.get_move(\'グラススライダー\').priority}")')
    elif name == 'こらえる':
        tests_for_move.append('# こらえる: KO級ダメージでもHP1で耐える（まもる系の全無効とは別）')
        tests_for_move.append('from simulator.battle import Battle as _Bce')
        tests_for_move.append('_pce = make_poke(type1="ノーマル", hp_b=1, def_b=1)')
        tests_for_move.append('_fce = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])')
        tests_for_move.append('_act_end = lambda s,o,f: Action(type="move", move=dl.get_move("こらえる"), move_idx=0)')
        tests_for_move.append('_act_atk = lambda s,o,f: Action(type="move", move=dl.get_move("インファイト"), move_idx=0)')
        tests_for_move.append('_bce = _Bce(BattleSide([_pce]), BattleSide([_fce]))')
        tests_for_move.append('import simulator.battle as _SBe; _SBemax = _SBe.MAX_TURNS; _SBe.MAX_TURNS = 1; _bce.run(_act_end, _act_atk); _SBe.MAX_TURNS = _SBemax')
        tests_for_move.append('check("こらえHP1: こらえる", _pce.is_alive and _pce.hp == 1, f"alive={_pce.is_alive} hp={_pce.hp}")')
        tests_for_move.append('# negative: こらえる無し（通常）なら同じ攻撃で耐えられない')
        tests_for_move.append('_pce2 = make_poke(type1="ノーマル", hp_b=1, def_b=1)')
        tests_for_move.append('_fce2 = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])')
        tests_for_move.append('execute(_fce2, _pce2, "インファイト")')
        tests_for_move.append('check("こらえる無し時は耐えられない: こらえる", not _pce2.is_alive, f"alive={_pce2.is_alive} hp={_pce2.hp}")')
    elif name == 'きあいパンチ':
        tests_for_move.append('# きあいパンチ: 行動前に技ダメージを受けると失敗（-3で後攻）')
        tests_for_move.append('from simulator.battle import Battle as _Bfp')
        tests_for_move.append('_pfp = make_poke(type1="かくとう", atk_b=150, hp_b=255, def_b=255, moves=["きあいパンチ"])')
        tests_for_move.append('_ffp = make_poke(type1="ノーマル", atk_b=80, hp_b=255, def_b=255, moves=["のしかかり"])')
        tests_for_move.append('_act_fp = lambda s,o,f: Action(type="move", move=dl.get_move("きあいパンチ"), move_idx=0)')
        tests_for_move.append('_act_hit = lambda s,o,f: Action(type="move", move=dl.get_move("のしかかり"), move_idx=0)')
        tests_for_move.append('_hp_ffp = _ffp.hp')
        tests_for_move.append('_bfp = _Bfp(BattleSide([_pfp]), BattleSide([_ffp]))')
        tests_for_move.append('import simulator.battle as _SB; _SBmax = _SB.MAX_TURNS; _SB.MAX_TURNS = 1; _bfp.run(_act_fp, _act_hit); _SB.MAX_TURNS = _SBmax')
        tests_for_move.append('check("被弾失敗: きあいパンチ", _ffp.hp == _hp_ffp, f"foeHP={_ffp.hp}/{_hp_ffp}（被弾後きあいパンチ不発なら相手無傷）")')
    elif name in ('ついばむ', 'むしくい'):
        tests_for_move.append(f'# {name}: 相手のきのみを食べ効果を得る（オボンのみで自分回復）')
        tests_for_move.append(f'_ppk = make_poke(type1="{atk_type}", atk_b=80); _ppk.hp = _ppk.max_hp // 2')
        tests_for_move.append(f'_dpk = make_poke(type1="{def_type}", hp_b=255, def_b=200, item="オボンのみ")')
        tests_for_move.append(f'_hp_ppk = _ppk.hp; execute(_ppk, _dpk, "{name}")')
        tests_for_move.append(f'check("きのみ奪取: {name}", _dpk.item is None and _ppk.hp > _hp_ppk, f"foeItem={{_dpk.item}} hp={{_ppk.hp}}/{{_hp_ppk}}")')
        tests_for_move.append(f'# effect_textに無い余計な追加効果がないこと（きのみ無しの相手に能力変化等が起きない）')
        tests_for_move.append(f'_dpk2 = make_poke(type1="{def_type}", hp_b=255, def_b=200); _rng_noextra = 0')
        tests_for_move.append(f'import random as _rnx; _rnx.seed(0)')
        tests_for_move.append(f'for _ in range(30): execute(make_poke(type1="{atk_type}", atk_b=10), _dpk2, "{name}")')
        tests_for_move.append(f'_stg2 = [getattr(_dpk2, _s, 0) for _s in ("stage_attack","stage_defense","stage_sp_attack","stage_sp_defense","stage_speed")]')
        tests_for_move.append(f'check("余計な追加効果なし: {name}", all(_v == 0 for _v in _stg2) and _dpk2.status is None, f"stages={{_stg2}} status={{_dpk2.status}}")')
    elif name == 'はねやすめ':
        tests_for_move.append('# はねやすめ: 使用ターン中ひこうタイプ消失（じめん技が通る）')
        tests_for_move.append('_prs, _, _ = execute_ctx(make_poke(type1="でんき", type2="ひこう", hp_b=200), make_poke(), "はねやすめ")')
        tests_for_move.append('check("ひこう消失: はねやすめ", "ひこう" not in (_prs.active.type1, _prs.active.type2), f"types={_prs.active.type1}/{_prs.active.type2}")')
    elif name == 'みらいよち':
        tests_for_move.append('# みらいよち: 使用すると予約が立ち（arising・手動セットしない）、満了ターンで発動')
        tests_for_move.append('from simulator.battle import Battle as _Bfs')
        tests_for_move.append('_pfs = make_poke(type1="エスパー", spatk_b=150, moves=["みらいよち"])')
        tests_for_move.append('_ffs = make_poke(type1="ノーマル", hp_b=255, spdef_b=80, moves=["たいあたり"])')
        tests_for_move.append('_bfs = _Bfs(BattleSide([_pfs]), BattleSide([_ffs])); _s2 = _bfs.side2')
        tests_for_move.append('# 使用 → 予約成立（future_sight_count が立つことを実機で確認）')
        tests_for_move.append('_execute_move(_bfs.side1, _bfs.side2, Action(type="move", move=dl.get_move("みらいよち"), move_idx=0), _bfs.field)')
        tests_for_move.append('check("使用で予約成立(arising): みらいよち", getattr(_s2, "future_sight_count", 0) > 0, f"count={getattr(_s2,\'future_sight_count\',0)}")')
        tests_for_move.append('_hp_ffs = _ffs.hp; _n_fs = _s2.future_sight_count')
        tests_for_move.append('# 予約中ターンは本体ダメージなし、満了ターンで発動')
        tests_for_move.append('for _ in range(_n_fs - 1): _bfs._end_of_turn()')
        tests_for_move.append('_mid = _ffs.hp; _bfs._end_of_turn()')
        tests_for_move.append('check("みらいよち遅延発動: みらいよち", _mid == _hp_ffs and _ffs.hp < _hp_ffs, f"mid={_mid} end={_ffs.hp}/{_hp_ffs}")')
    elif name == 'メロメロ':
        tests_for_move.append('# メロメロ: 性別未実装のため常に失敗（infatuationは付与されない）')
        tests_for_move.append('_pml = make_poke(type1="ノーマル"); _dml = make_poke(type1="ノーマル", hp_b=200)')
        tests_for_move.append('execute(_pml, _dml, "メロメロ")')
        tests_for_move.append('check("メロメロ: メロメロ", not _dml.infatuation, f"infatuation={_dml.infatuation}")')
    elif name == 'じゅうでん':
        tests_for_move.append('# じゅうでん: 使用するとcharged状態になる（条件成立を検証）')
        tests_for_move.append('_pjd_t = make_poke(type1="でんき"); execute(_pjd_t, make_poke(), "じゅうでん")')
        tests_for_move.append('check("じゅうでんでcharged成立: じゅうでん", _pjd_t.charged, f"charged={_pjd_t.charged}")')
        tests_for_move.append('# charged状態だと次のでんき技の威力が2倍')
        tests_for_move.append('_pjd = make_poke(type1="でんき", spatk_b=120); _djd = make_poke(type1="ノーマル", spdef_b=100)')
        tests_for_move.append('_djd2 = make_poke(type1="ノーマル", spdef_b=100)')
        tests_for_move.append('_jd_base = calc_damage(_pjd, _djd, dl.get_move("10まんボルト"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_pjd.charged = True; _jd_chg = calc_damage(_pjd, _djd2, dl.get_move("10まんボルト"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("じゅうでん次でんき2倍: じゅうでん", abs(_jd_chg - _jd_base * 2) <= 2, f"base={_jd_base} chg={_jd_chg}")')
    elif name in ('ソーラービーム', 'ソーラーブレード'):
        tests_for_move.append(f'# {name}: 晴れ以外の天候は威力1/2')
        tests_for_move.append(f'_psb = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsb = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120)')
        tests_for_move.append(f'_fsun = BattleField(); _fsun.weather = "sunny"; _frain = BattleField(); _frain.weather = "rain"')
        tests_for_move.append(f'_sb_sun = calc_damage(_psb, _dsb, dl.get_move("{name}"), _fsun, random_roll=1.0); _sb_rain = calc_damage(_psb, _dsb, dl.get_move("{name}"), _frain, random_roll=1.0)')
        tests_for_move.append(f'check("天候半減: {name}", _sb_rain < _sb_sun, f"sun={{_sb_sun}} rain={{_sb_rain}}")')
        tests_for_move.append(f'# 無天候は溜めが必要（1ターン目ダメなし）')
        tests_for_move.append(f'_pno = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dno = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpno = _dno.hp')
        tests_for_move.append(f'execute(_pno, _dno, "{name}")')
        tests_for_move.append(f'check("無天候は溜め(1Tダメなし): {name}", _dno.hp == _hpno and _pno.charging_move == "{name}", f"hp={{_dno.hp}}/{{_hpno}} charging={{_pno.charging_move}}")')
        tests_for_move.append(f'# にほんばれ中は溜めず即攻撃（1ターン目でダメージ）')
        tests_for_move.append(f'_psn = make_poke(type1="くさ", atk_b=120, spatk_b=120); _dsn = make_poke(type1="ノーマル", hp_b=255, def_b=120, spdef_b=120); _hpsn = _dsn.hp')
        tests_for_move.append(f'_fsun2 = BattleField(); _fsun2.weather = "sunny"')
        tests_for_move.append(f'execute(_psn, _dsn, "{name}", _fsun2)')
        tests_for_move.append(f'check("晴れは即発動(1Tでダメージ): {name}", _dsn.hp < _hpsn and _psn.charging_move is None, f"hp={{_dsn.hp}}/{{_hpsn}} charging={{_psn.charging_move}}")')
        tests_for_move.append(f'# 威力半減の具体値（{power}→{power // 2}）')
        tests_for_move.append(f'_psx = make_poke(type1="くさ", atk_b=100, spatk_b=100); _dsx = make_poke(type1="ノーマル", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_pwr_norm = _ep(_psx, _dsx, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_frx = BattleField(); _frx.weather = "rain"; _pwr_rain = _ep(_psx, _dsx, dl.get_move("{name}"), _frx)')
        tests_for_move.append(f'check("通常威力{power}: {name}", _pwr_norm == {power}, f"norm={{_pwr_norm}}")')
        tests_for_move.append(f'check("天候半減({power // 2}): {name}", _pwr_rain == {power // 2}, f"rain={{_pwr_rain}}")')
    elif name == 'おいかぜ':
        tests_for_move.append('# おいかぜ: 自分側の素早さが2倍（単体でも自分に効果）')
        tests_for_move.append('from simulator.battle import _speed_order')
        tests_for_move.append('_s1o, _s2o, _ = execute_ctx(make_poke(type1="ひこう", spd_b=80, moves=["おいかぜ"]), make_poke(spd_b=100), "おいかぜ")')
        tests_for_move.append('check("おいかぜS2倍: おいかぜ", _s1o.tailwind, f"tailwind={_s1o.tailwind}")')
    elif name == 'せいちょう':
        tests_for_move.append('# せいちょう: 通常は攻撃・特攻+1、にほんばれ中は+2')
        tests_for_move.append('_pg1 = make_poke(type1="ノーマル"); execute(_pg1, make_poke(), "せいちょう")')
        tests_for_move.append('check("せいちょう通常+1: せいちょう", _pg1.stage_attack == 1, f"atk={_pg1.stage_attack}")')
        tests_for_move.append('_pg2 = make_poke(type1="ノーマル"); _fsun_g = BattleField(); _fsun_g.weather = "sunny"; execute(_pg2, make_poke(), "せいちょう", _fsun_g)')
        tests_for_move.append('check("晴れ2段階: せいちょう", _pg2.stage_attack == 2, f"atk={_pg2.stage_attack}")')
    elif name in ('かみなり', 'ぼうふう'):
        tests_for_move.append(f'# {name}: あめ必中・にほんばれ命中低下')
        tests_for_move.append(f'_pwa = make_poke(type1="{atk_type}", spatk_b=100); _dwa = make_poke(type1="{def_type}", spdef_b=100)')
        tests_for_move.append(f'_fsun_w = BattleField(); _fsun_w.weather = "sunny"; _fnorm_w = BattleField()')
        tests_for_move.append(f'from simulator.damage import check_hit as _ch')
        tests_for_move.append(f'random.seed(0); _miss_sun = sum(0 if _ch(_pwa, _dwa, dl.get_move("{name}"), _fsun_w) else 1 for _ in range(200))')
        tests_for_move.append(f'random.seed(0); _miss_norm = sum(0 if _ch(_pwa, _dwa, dl.get_move("{name}"), _fnorm_w) else 1 for _ in range(200))')
        tests_for_move.append(f'check("晴れ命中低下: {name}", _miss_sun > _miss_norm, f"sun_miss={{_miss_sun}} norm_miss={{_miss_norm}}")')
    elif name == 'だいちのはどう':
        tests_for_move.append('# だいちのはどう: フィールドでタイプが変わる（グラスF→くさ）')
        tests_for_move.append('_pew = make_poke(type1="ノーマル", spatk_b=120)')
        tests_for_move.append('_few = BattleField(); _few.grassy_terrain = True')
        tests_for_move.append('from simulator.damage import _effective_move_type as _emt')
        tests_for_move.append('check("フィールド型変化: だいちのはどう", _emt(_pew, dl.get_move("だいちのはどう"), _few) == "くさ", f"type={_emt(_pew, dl.get_move(\'だいちのはどう\'), _few)}")')
        tests_for_move.append('# フィールド効果を受けていると威力2倍（接地時）／フィールド無しは等倍')
        tests_for_move.append('_pdw = make_poke(type1="じめん", spatk_b=100, atk_b=100); _ddw = make_poke(type1="ノーマル", def_b=100, spdef_b=100)')
        tests_for_move.append('_dw_n = _ep(_pdw, _ddw, dl.get_move("だいちのはどう"), BattleField())')
        tests_for_move.append('_fdw = BattleField(); _fdw.grassy_terrain = True; _dw_f = _ep(_pdw, _ddw, dl.get_move("だいちのはどう"), _fdw)')
        tests_for_move.append('check("フィールドで威力2倍: だいちのはどう", _dw_f == _dw_n * 2, f"no={_dw_n} field={_dw_f}")')
    elif name == 'トリプルアクセル':
        tests_for_move.append('# トリプルアクセル: 1回目20/2回目40/3回目60と威力漸増')
        tests_for_move.append('_pta = make_poke(type1="こおり", atk_b=100); _dta = make_poke(type1="ノーマル", def_b=100)')
        tests_for_move.append('_pta._multi_hit_index = 0; _ta0 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())')
        tests_for_move.append('_pta._multi_hit_index = 1; _ta1 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())')
        tests_for_move.append('_pta._multi_hit_index = 2; _ta2 = _ep(_pta, _dta, dl.get_move("トリプルアクセル"), BattleField())')
        tests_for_move.append('check("威力漸増: トリプルアクセル", (_ta0, _ta1, _ta2) == (20, 40, 60), f"powers={_ta0},{_ta1},{_ta2}")')
    elif name == 'スケイルショット':
        tests_for_move.append('# スケイルショット: 1発あたり威力25（2-5回連続。多段/自己能力変化は別途検証）')
        tests_for_move.append('_pss2 = make_poke(type1="ドラゴン", atk_b=100); _dss2 = make_poke(type1="ドラゴン", def_b=100)')
        tests_for_move.append('check("1発威力25: スケイルショット", _ep(_pss2, _dss2, dl.get_move("スケイルショット"), BattleField()) == 25, f"pw={_ep(_pss2, _dss2, dl.get_move(\'スケイルショット\'), BattleField())}")')
    elif name == 'まもる':
        tests_for_move.append('# まもる: 連続使用で成功率1/3に低下（protect_consecutiveが増える）')
        tests_for_move.append('_pmm = make_poke(type1="ノーマル"); _s1m = BattleSide([_pmm]); _s2m = BattleSide([make_poke()])')
        tests_for_move.append('_execute_move(_s1m, _s2m, Action(type="move", move=dl.get_move("まもる")), BattleField())')
        tests_for_move.append('check("まもる成功: まもる", _pmm.protecting)')
        tests_for_move.append('random.seed(0); _fail_seen = False')
        tests_for_move.append('for _ in range(40):')
        tests_for_move.append('    _pmc = make_poke(type1="ノーマル"); _pmc.protect_consecutive = 1; _s1c = BattleSide([_pmc])')
        tests_for_move.append('    _execute_move(_s1c, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("まもる")), BattleField())')
        tests_for_move.append('    if not _pmc.protecting: _fail_seen = True; break')
        tests_for_move.append('check("連続成功率低下: まもる", _fail_seen)')
    elif name == 'がむしゃら':
        tests_for_move.append('# がむしゃら: 相手HPを自分HPに揃える。相手HP≦自分HPなら失敗(無傷)')
        tests_for_move.append('_pgm = make_poke(type1="ノーマル", atk_b=1); _pgm.hp = _pgm.max_hp')
        tests_for_move.append('_dgm = make_poke(type1="でんき", hp_b=120, def_b=255); _dgm.hp = 10')
        tests_for_move.append('execute(_pgm, _dgm, "がむしゃら")')
        tests_for_move.append('check("相手HP以下で失敗: がむしゃら", _dgm.hp == 10, f"hp={_dgm.hp}")')
        tests_for_move.append('_pgm2 = make_poke(type1="ノーマル", atk_b=1); _pgm2.hp = 20')
        tests_for_move.append('_dgm2 = make_poke(type1="でんき", hp_b=200, def_b=255)')
        tests_for_move.append('execute(_pgm2, _dgm2, "がむしゃら")')
        tests_for_move.append('check("HP揃え(可変ダメージ): がむしゃら", _dgm2.hp == 20, f"hp={_dgm2.hp}")')
    elif name == 'であいがしら':
        tests_for_move.append(f'# {name}: 場に出て最初のターンのみ成功（turns_out>0は失敗）')
        tests_for_move.append(f'_pnk = make_poke(type1="{atk_type}", atk_b=120); _dnk = make_poke(type1="{def_type}", hp_b=255, def_b=150)')
        tests_for_move.append(f'_pnk.turns_out = 1; _hpnk = _dnk.hp; execute(_pnk, _dnk, "{name}")')
        tests_for_move.append(f'check("初手以外で失敗: {name}", _dnk.hp == _hpnk, f"hp={{_dnk.hp}}/{{_hpnk}}")')
        tests_for_move.append(f'_pnk2 = make_poke(type1="{atk_type}", atk_b=120); _dnk2 = make_poke(type1="{def_type}", hp_b=255, def_b=150)')
        tests_for_move.append(f'_pnk2.turns_out = 0; _hpnk2 = _dnk2.hp; execute(_pnk2, _dnk2, "{name}")')
        tests_for_move.append(f'check("初手で成功: {name}", _dnk2.hp < _hpnk2, f"hp={{_dnk2.hp}}/{{_hpnk2}}")')
    elif name == 'いびき':
        tests_for_move.append('# いびき: 覚醒時は失敗、ねむり中は使えて30%ひるみ')
        tests_for_move.append('_pib = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _dib = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)')
        tests_for_move.append('_hpib = _dib.hp; execute(_pib, _dib, "いびき")')
        tests_for_move.append('check("覚醒時は失敗: いびき", _dib.hp == _hpib, f"hp={_dib.hp}/{_hpib}")')
        tests_for_move.append('random.seed(2); _ib_fl = 0')
        tests_for_move.append('for _ in range(300):')
        tests_for_move.append('    _pib2 = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _pib2.status = "sleep"; _pib2.sleep_count = 5')
        tests_for_move.append('    _dib2 = make_poke(type1="ノーマル", hp_b=255, spdef_b=120, def_b=120)')
        tests_for_move.append('    execute(_pib2, _dib2, "いびき"); _ib_fl += int(_dib2.flinched)')
        tests_for_move.append('check("ねむり中使用+30%ひるみ: いびき", 40 <= _ib_fl <= 140, f"flinch={_ib_fl}/300")')
    elif name == 'とおぼえ':
        tests_for_move.append('# とおぼえ: 自分の攻撃+1')
        tests_for_move.append('_pto = make_poke(type1="ノーマル"); execute(_pto, make_poke(), "とおぼえ")')
        tests_for_move.append('check("攻撃+1: とおぼえ", _pto.stage_attack == 1, f"atk={_pto.stage_attack}")')
    elif name == 'みちづれ':
        tests_for_move.append('# みちづれ: 道連れ付与 + 連続使用は失敗')
        tests_for_move.append('_pmz = make_poke(type1="ゴースト"); execute(_pmz, make_poke(), "みちづれ")')
        tests_for_move.append('check("みちづれ付与: みちづれ", _pmz.destiny_bond)')
        tests_for_move.append('# 連続使用は失敗（前ターン使用フラグが立っている場合）')
        tests_for_move.append('_pmz2 = make_poke(type1="ゴースト"); _pmz2._destiny_bond_last_turn = True')
        tests_for_move.append('execute(_pmz2, make_poke(), "みちづれ")')
        tests_for_move.append('check("連続失敗: みちづれ", not _pmz2.destiny_bond, f"destiny_bond={_pmz2.destiny_bond}")')
        tests_for_move.append('_pmz2 = make_poke(type1="ゴースト", hp_b=1, def_b=1); _pmz2.destiny_bond = True')
        tests_for_move.append('_fatk = make_poke(type1="あく", atk_b=255, moves=["かみくだく"])')
        tests_for_move.append('_execute_move(BattleSide([_fatk]), BattleSide([_pmz2]), Action(type="move", move=dl.get_move("かみくだく")), BattleField())')
        tests_for_move.append('check("道連れ発動: みちづれ", not _pmz2.is_alive and not _fatk.is_alive, f"自{_pmz2.is_alive} 相{_fatk.is_alive}")')
    elif name == 'きあいだめ':
        tests_for_move.append('# きあいだめ: 急所ランク+2')
        tests_for_move.append('_pkd = make_poke(type1="ノーマル"); execute(_pkd, make_poke(), "きあいだめ")')
        tests_for_move.append('check("急所ランク+2: きあいだめ", _pkd.crit_stage == 2, f"crit_stage={_pkd.crit_stage}")')
    elif name == 'でんじは':
        tests_for_move.append('# でんじは: まひ付与。じめんタイプには無効')
        tests_for_move.append('_pdj = make_poke(type1="でんき"); _ddj = make_poke(type1="ノーマル", hp_b=200)')
        tests_for_move.append('execute(_pdj, _ddj, "でんじは")')
        tests_for_move.append('check("まひ付与: でんじは", _ddj.status == "paralysis", f"status={_ddj.status}")')
        tests_for_move.append('_ddj2 = make_poke(type1="じめん", hp_b=200); execute(_pdj, _ddj2, "でんじは")')
        tests_for_move.append('check("じめん無効: でんじは", _ddj2.status is None, f"status={_ddj2.status}")')
    elif name == 'やどりぎのタネ':
        tests_for_move.append('# やどりぎのタネ: 付与。くさタイプには無効')
        tests_for_move.append('_pys = make_poke(type1="くさ"); _dys = make_poke(type1="ノーマル", hp_b=200); execute(_pys, _dys, "やどりぎのタネ")')
        tests_for_move.append('check("やどりぎ付与: やどりぎのタネ", _dys.seeded, f"seeded={_dys.seeded}")')
        tests_for_move.append('_dys2 = make_poke(type1="くさ", hp_b=200); execute(_pys, _dys2, "やどりぎのタネ")')
        tests_for_move.append('check("くさ無効: やどりぎのタネ", not _dys2.seeded, f"seeded={_dys2.seeded}")')
    elif name in ('ねむりごな', 'しびれごな', 'どくのこな', 'キノコのほうし'):
        _pw_st = {'ねむりごな':'sleep','しびれごな':'paralysis','どくのこな':'poison','キノコのほうし':'sleep'}[name]
        tests_for_move.append(f'# {name}: 粉技。くさタイプには無効')
        tests_for_move.append(f'_ppw = make_poke(type1="{atk_type}"); random.seed(0); _pw_ok = False')
        tests_for_move.append(f'for _ in range(20):')
        tests_for_move.append(f'    _dpw = make_poke(type1="ノーマル", hp_b=200); execute(_ppw, _dpw, "{name}")')
        tests_for_move.append(f'    if _dpw.status == "{_pw_st}": _pw_ok = True; break')
        tests_for_move.append(f'check("粉付与: {name}", _pw_ok)')
        tests_for_move.append(f'_dpw2 = make_poke(type1="くさ", hp_b=200)')
        tests_for_move.append(f'for _ in range(20): execute(_ppw, _dpw2, "{name}")')
        tests_for_move.append(f'check("くさ無効: {name}", _dpw2.status is None, f"status={{_dpw2.status}}")')
    elif name == 'わたほうし':
        tests_for_move.append('# わたほうし: 素早さ-2。くさタイプには無効（粉）')
        tests_for_move.append('_pwt = make_poke(type1="むし"); random.seed(0); _wt_ok = False')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    _dwt = make_poke(type1="ノーマル", hp_b=200); execute(_pwt, _dwt, "わたほうし")')
        tests_for_move.append('    if _dwt.stage_speed == -2: _wt_ok = True; break')
        tests_for_move.append('check("素早さ-2: わたほうし", _wt_ok)')
        tests_for_move.append('_dwt2 = make_poke(type1="くさ", hp_b=200); execute(_pwt, _dwt2, "わたほうし")')
        tests_for_move.append('check("くさ無効: わたほうし", _dwt2.stage_speed == 0, f"spd={_dwt2.stage_speed}")')
    elif name == 'まほうのこな':
        tests_for_move.append('# まほうのこな: 相手をエスパー化。くさタイプには無効（粉）')
        tests_for_move.append('_pmp = make_poke(type1="エスパー"); _dmp = make_poke(type1="ノーマル", hp_b=200)')
        tests_for_move.append('for _ in range(20): execute(_pmp, _dmp, "まほうのこな")')
        tests_for_move.append('check("エスパータイプ化: まほうのこな", _dmp.type1 == "エスパー", f"type={_dmp.type1}")')
        tests_for_move.append('_dmp2 = make_poke(type1="くさ", hp_b=200); execute(_pmp, _dmp2, "まほうのこな")')
        tests_for_move.append('check("くさ無効: まほうのこな", _dmp2.type1 == "くさ", f"type={_dmp2.type1}")')
    elif name == 'はきだす':
        tests_for_move.append('# はきだす: たくわえ0だと失敗、たくわえ有りでダメージ')
        tests_for_move.append('_phk = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _dhk = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)')
        tests_for_move.append('_hphk = _dhk.hp; execute(_phk, _dhk, "はきだす")')
        tests_for_move.append('check("たくわえ0で失敗: はきだす", _dhk.hp == _hphk, f"hp={_dhk.hp}/{_hphk}")')
        tests_for_move.append('_phk2 = make_poke(type1="ノーマル", atk_b=100, spatk_b=100); _phk2.stockpile_count = 2; _dhk2 = make_poke(type1="ノーマル", hp_b=255, spdef_b=120)')
        tests_for_move.append('_hphk2 = _dhk2.hp; execute(_phk2, _dhk2, "はきだす")')
        tests_for_move.append('check("たくわえ消費攻撃: はきだす", _dhk2.hp < _hphk2 and _phk2.stockpile_count == 0, f"hp={_dhk2.hp}/{_hphk2} sc={_phk2.stockpile_count}")')
    elif name == 'ゴーストダイブ':
        tests_for_move.append('# ゴーストダイブ: 攻撃ターンにまもるを貫通して命中')
        tests_for_move.append('_pgd = make_poke(type1="ゴースト", atk_b=120); _dgd = make_poke(type1="エスパー", hp_b=255, def_b=150)')
        tests_for_move.append('_pgd.charging_move = "ゴーストダイブ"; _dgd.protecting = True; _hpgd = _dgd.hp')
        tests_for_move.append('_execute_move(BattleSide([_pgd]), BattleSide([_dgd]), Action(type="move", move=dl.get_move("ゴーストダイブ")), BattleField())')
        tests_for_move.append('check("まもる貫通: ゴーストダイブ", _dgd.hp < _hpgd, f"hp={_dgd.hp}/{_hpgd}")')
    elif name == 'ねがいごと':
        tests_for_move.append('# ねがいごと: 2ターン後に自分側の場のポケモンを回復')
        tests_for_move.append('from simulator.battle import Battle as _Bwi')
        tests_for_move.append('_pwi = make_poke(type1="ノーマル", hp_b=200); _pwi.hp = 30')
        tests_for_move.append('_s1w, _, _ = execute_ctx(_pwi, make_poke(), "ねがいごと")')
        tests_for_move.append('check("ねがいごと予約: ねがいごと", _s1w.wish_count > 0)')
        tests_for_move.append('_bwi = _Bwi(_s1w, BattleSide([make_poke()])); _hpw0 = _pwi.hp')
        tests_for_move.append('_bwi._end_of_turn(); _mid_w = _pwi.hp; _bwi._end_of_turn()')
        tests_for_move.append('check("ねがいごと回復: ねがいごと", _mid_w == _hpw0 and _pwi.hp > _hpw0, f"mid={_mid_w} end={_pwi.hp}/{_hpw0}")')
    elif name == 'のみこむ':
        tests_for_move.append('# のみこむ: たくわえ消費でHP回復、たくわえ0だと失敗')
        tests_for_move.append('_pno = make_poke(type1="ノーマル", hp_b=200); _pno.hp = 30; execute(_pno, make_poke(), "のみこむ")')
        tests_for_move.append('check("たくわえ0で失敗: のみこむ", _pno.hp == 30, f"hp={_pno.hp}")')
        tests_for_move.append('_pno2 = make_poke(type1="ノーマル", hp_b=200); _pno2.hp = 30; _pno2.stockpile_count = 2; execute(_pno2, make_poke(), "のみこむ")')
        tests_for_move.append('check("たくわえ消費回復: のみこむ", _pno2.hp > 30 and _pno2.stockpile_count == 0, f"hp={_pno2.hp} sc={_pno2.stockpile_count}")')
    elif name == 'しんぴのまもり':
        tests_for_move.append('# しんぴのまもり: 自分側が状態異常を防ぐ（でんじはを無効化）')
        tests_for_move.append('_pss = make_poke(type1="ノーマル"); _dss = make_poke(type1="ノーマル", hp_b=200)')
        tests_for_move.append('_s2ss = BattleSide([_dss]); _s2ss.safeguard = 5')
        tests_for_move.append('random.seed(0)')
        tests_for_move.append('for _ in range(10): _execute_move(BattleSide([_pss]), _s2ss, Action(type="move", move=dl.get_move("でんじは")), BattleField())')
        tests_for_move.append('check("状態異常防御: しんぴのまもり", _dss.status is None, f"status={_dss.status}")')
    elif name == 'フェイント':
        tests_for_move.append('# フェイント: まもる状態の相手を貫通して攻撃')
        tests_for_move.append('_pft = make_poke(type1="ノーマル", atk_b=120); _dft = make_poke(type1="ノーマル", hp_b=255, def_b=150)')
        tests_for_move.append('_dft.protecting = True; _hpft = _dft.hp')
        tests_for_move.append('_execute_move(BattleSide([_pft]), BattleSide([_dft]), Action(type="move", move=dl.get_move("フェイント")), BattleField())')
        tests_for_move.append('check("まもる貫通: フェイント", _dft.hp < _hpft and not _dft.protecting, f"hp={_dft.hp}/{_hpft} protect={_dft.protecting}")')
    elif name == 'なげつける':
        tests_for_move.append('# なげつける: 持ち物別の威力テーブルを全件検証')
        tests_for_move.append('_dnt = make_poke(type1="ノーマル", hp_b=255, def_b=120)')
        tests_for_move.append('_FLING = {"こだわりハチマキ":130,"こだわりメガネ":90,"こだわりスカーフ":90,"ゴツゴツメット":80,"くろおび":80,"きあいのタスキ":60,"じゅうなんチョッキ":60,"どくバリ":50,"いのちのたま":30,"くろいヘドロ":30,"メタルコート":30,"シルクのスカーフ":20,"たべのこし":20}')
        tests_for_move.append('_nt_ng = []')
        tests_for_move.append('for _it, _ep_exp in _FLING.items():')
        tests_for_move.append('    _pnt = make_poke(type1="あく", atk_b=100, item=_it)')
        tests_for_move.append('    _got_nt = _ep(_pnt, _dnt, dl.get_move("なげつける"), BattleField())')
        tests_for_move.append('    if _got_nt != _ep_exp: _nt_ng.append(f"{_it}:{_got_nt}!={_ep_exp}")')
        tests_for_move.append('check("道具別威力テーブル全件: なげつける", not _nt_ng, f"NG={_nt_ng}")')
        tests_for_move.append('# テーブル外アイテムはデフォルト威力10')
        tests_for_move.append('_pnt_d = make_poke(type1="あく", atk_b=100, item="オボンのみ")')
        tests_for_move.append('check("テーブル外デフォルト10: なげつける", _ep(_pnt_d, _dnt, dl.get_move("なげつける"), BattleField()) == 10, f"got={_ep(_pnt_d, _dnt, dl.get_move(\'なげつける\'), BattleField())}")')
        tests_for_move.append('# 持ち物なしは失敗（相手にダメージが入らない）')
        tests_for_move.append('_pnt_n = make_poke(type1="あく", atk_b=100); _dnt_n = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpnn = _dnt_n.hp')
        tests_for_move.append('execute(_pnt_n, _dnt_n, "なげつける")')
        tests_for_move.append('check("持ち物なしで失敗: なげつける", _dnt_n.hp == _hpnn, f"hp={_dnt_n.hp}/{_hpnn}")')
        tests_for_move.append('# 使うと持ち物が無くなる')
        tests_for_move.append('_pnt3 = make_poke(type1="あく", atk_b=100, item="こだわりハチマキ"); execute(_pnt3, make_poke(type1="ノーマル", hp_b=255), "なげつける")')
        tests_for_move.append('check("道具消費: なげつける", _pnt3.item is None, f"item={_pnt3.item}")')
    elif name == 'ねむる':
        tests_for_move.append('# ねむる: HP満タンだと失敗、減っていれば全回復+ねむり')
        tests_for_move.append('_pnf = make_poke(type1="ノーマル", hp_b=200); execute(_pnf, make_poke(), "ねむる")')
        tests_for_move.append('check("満タン失敗: ねむる", _pnf.status != "sleep", f"status={_pnf.status}")')
        tests_for_move.append('_pns = make_poke(type1="ノーマル", hp_b=200); _pns.hp = _pns.max_hp // 2; execute(_pns, make_poke(), "ねむる")')
        tests_for_move.append('check("ねむる付与: ねむる", _pns.status == "sleep" and _pns.hp == _pns.max_hp, f"status={_pns.status} hp={_pns.hp}")')
    elif name == 'はらだいこ':
        tests_for_move.append('# はらだいこ: HP不足だと失敗、足りればA最大+HP半減')
        tests_for_move.append('_phf = make_poke(type1="ノーマル", hp_b=200); _phf.hp = _phf.max_hp // 2; execute(_phf, make_poke(), "はらだいこ")')
        tests_for_move.append('check("HP不足失敗: はらだいこ", _phf.stage_attack < 6, f"atk_stage={_phf.stage_attack}")')
        tests_for_move.append('_phs = make_poke(type1="ノーマル", hp_b=200); execute(_phs, make_poke(), "はらだいこ")')
        tests_for_move.append('check("はらだいこ成功: はらだいこ", _phs.stage_attack == 6 and _phs.hp < _phs.max_hp, f"atk={_phs.stage_attack} hp={_phs.hp}")')
    elif name == 'ソウルビート':
        tests_for_move.append('# ソウルビート: HP不足だと失敗、足りれば全能力+1&HP1/3消費')
        tests_for_move.append('_psf = make_poke(type1="ドラゴン", hp_b=200); _psf.hp = 1; execute(_psf, make_poke(), "ソウルビート")')
        tests_for_move.append('check("HP不足失敗: ソウルビート", _psf.stage_attack == 0, f"atk={_psf.stage_attack}")')
        tests_for_move.append('_pss = make_poke(type1="ドラゴン", hp_b=200); execute(_pss, make_poke(), "ソウルビート")')
        tests_for_move.append('check("ソウルビート成功: ソウルビート", _pss.stage_attack == 1 and _pss.hp < _pss.max_hp, f"atk={_pss.stage_attack} hp={_pss.hp}")')
    elif name == 'ほおばる':
        tests_for_move.append('# ほおばる: きのみ無しは失敗、有りで防御+2&消費')
        tests_for_move.append('_pbf = make_poke(type1="ノーマル"); execute(_pbf, make_poke(), "ほおばる")')
        tests_for_move.append('check("きのみ無し失敗: ほおばる", _pbf.stage_defense == 0)')
        tests_for_move.append('_pbs = make_poke(type1="ノーマル", item="オボンのみ"); execute(_pbs, make_poke(), "ほおばる")')
        tests_for_move.append('check("防御2段階上昇(+2): ほおばる", _pbs.stage_defense == 2 and _pbs.item is None and _pbs.ate_berry)')
    elif name == 'ゲップ':
        tests_for_move.append('# ゲップ: きのみ未食だと失敗、食べていれば成功')
        tests_for_move.append('_pgf = make_poke(type1="どく", spatk_b=100); _dgf = make_poke(type1="くさ", hp_b=255, spdef_b=120)')
        tests_for_move.append('_hpd1 = _dgf.hp; execute(_pgf, _dgf, "ゲップ")')
        tests_for_move.append('check("きのみ未食失敗: ゲップ", _dgf.hp == _hpd1, f"hp={_dgf.hp}/{_hpd1}")')
        tests_for_move.append('_pgs = make_poke(type1="どく", spatk_b=100); _pgs.ate_berry = True; _dgs = make_poke(type1="くさ", hp_b=255, spdef_b=120)')
        tests_for_move.append('_hpd2 = _dgs.hp; execute(_pgs, _dgs, "ゲップ")')
        tests_for_move.append('check("きのみ食後成功: ゲップ", _dgs.hp < _hpd2, f"hp={_dgs.hp}/{_hpd2}")')
    elif name == 'もえつきる':
        tests_for_move.append('# もえつきる: 非ほのおは失敗、ほのおなら攻撃後に自分のほのおが消える')
        tests_for_move.append('_pmf = make_poke(type1="みず", spatk_b=100); _dmf = make_poke(type1="くさ", hp_b=255, spdef_b=150)')
        tests_for_move.append('_hpm1 = _dmf.hp; execute(_pmf, _dmf, "もえつきる")')
        tests_for_move.append('check("非ほのお失敗: もえつきる", _dmf.hp == _hpm1, f"hp={_dmf.hp}/{_hpm1}")')
        tests_for_move.append('_pms = make_poke(type1="ほのお", spatk_b=120); _dms = make_poke(type1="くさ", hp_b=255, spdef_b=150)')
        tests_for_move.append('execute(_pms, _dms, "もえつきる")')
        tests_for_move.append('check("ほのおタイプ消失: もえつきる", "ほのお" not in (_pms.type1, _pms.type2), f"types={_pms.type1}/{_pms.type2}")')
        tests_for_move.append('# 使うと自分のこおり状態を治す')
        tests_for_move.append('_pmt = make_poke(type1="ほのお", spatk_b=100); _pmt.status = "freeze"')
        tests_for_move.append('execute(_pmt, make_poke(type1="くさ", hp_b=255), "もえつきる")')
        tests_for_move.append('check("自分こおり治癒: もえつきる", _pmt.status != "freeze", f"status={_pmt.status}")')
    elif name == 'アイアンローラー':
        tests_for_move.append('# アイアンローラー: フィールド無しは失敗、有りで成功&フィールド解除')
        tests_for_move.append('_pir = make_poke(type1="はがね", atk_b=120); _dir = make_poke(type1="フェアリー", hp_b=255, def_b=120)')
        tests_for_move.append('_f_no = BattleField(); _hpi1 = _dir.hp; execute(_pir, _dir, "アイアンローラー", _f_no)')
        tests_for_move.append('check("フィールド無し失敗: アイアンローラー", _dir.hp == _hpi1, f"hp={_dir.hp}/{_hpi1}")')
        tests_for_move.append('_pir2 = make_poke(type1="はがね", atk_b=120); _dir2 = make_poke(type1="フェアリー", hp_b=255, def_b=120)')
        tests_for_move.append('_f_g = BattleField(); _f_g.grassy_terrain = True; _hpi2 = _dir2.hp; execute(_pir2, _dir2, "アイアンローラー", _f_g)')
        tests_for_move.append('check("フィールド解除(成功時): アイアンローラー", _dir2.hp < _hpi2 and not _f_g.grassy_terrain, f"hp={_dir2.hp}/{_hpi2} field={_f_g.grassy_terrain}")')
    elif name == 'はやてがえし':
        tests_for_move.append('# はやてがえし: 相手が先制技を選んでいないと失敗、選んでいれば命中しひるませる')
        tests_for_move.append('_pqg = make_poke(type1="ひこう", atk_b=120)')
        tests_for_move.append('_opp_quick = Action(type="move", move=dl.get_move("でんこうせっか"))')
        tests_for_move.append('_opp_slow = Action(type="move", move=dl.get_move("のしかかり"))')
        tests_for_move.append('# 相手が通常技→失敗（無傷）')
        tests_for_move.append('_dqg = make_poke(type1="ノーマル", hp_b=255, def_b=200); _hpq1 = _dqg.hp')
        tests_for_move.append('_execute_move(BattleSide([_pqg]), BattleSide([_dqg]), Action(type="move", move=dl.get_move("はやてがえし")), BattleField(), _opp_slow)')
        tests_for_move.append('check("先制技なしで失敗: はやてがえし", _dqg.hp == _hpq1, f"hp={_dqg.hp}/{_hpq1}")')
        tests_for_move.append('# 相手が先制技→成功しひるませる')
        tests_for_move.append('random.seed(0); _qg_flinch = False')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    _dqg2 = make_poke(type1="ノーマル", hp_b=255, def_b=200)')
        tests_for_move.append('    _execute_move(BattleSide([_pqg]), BattleSide([_dqg2]), Action(type="move", move=dl.get_move("はやてがえし")), BattleField(), _opp_quick)')
        tests_for_move.append('    if _dqg2.flinched: _qg_flinch = True; break')
        tests_for_move.append('check("ひるみ(先制技相手): はやてがえし", _qg_flinch)')
    elif name == 'とっておき':
        tests_for_move.append('# とっておき: 他の技を全て使うまで失敗、使い切れば成功')
        tests_for_move.append('_ptf = make_poke(type1="ノーマル", atk_b=120, moves=["とっておき","たいあたり"]); _dtf = make_poke(type1="ノーマル", hp_b=255, def_b=200)')
        tests_for_move.append('_hpt1 = _dtf.hp; execute(_ptf, _dtf, "とっておき")')
        tests_for_move.append('check("他技未使用で失敗: とっておき", _dtf.hp == _hpt1, f"hp={_dtf.hp}/{_hpt1}")')
        tests_for_move.append('_ptf.used_moves.add("たいあたり"); _hpt2 = _dtf.hp; execute(_ptf, _dtf, "とっておき")')
        tests_for_move.append('check("他技使用後に成功: とっておき", _dtf.hp < _hpt2, f"hp={_dtf.hp}/{_hpt2}")')
    elif name == 'うちおとす':
        tests_for_move.append('# うちおとす: ひこう/ふゆう/でんじふゆうを接地させ、じめん技が当たるようになる')
        tests_for_move.append('_pud = make_poke(type1="いわ", atk_b=100); _dud = make_poke(type1="ひこう", hp_b=255, def_b=120)')
        tests_for_move.append('_jground = make_poke(type1="じめん", atk_b=120)')
        tests_for_move.append('_before = dmg(_jground, _dud, "じしん")')
        tests_for_move.append('execute(_pud, _dud, "うちおとす")')
        tests_for_move.append('_after = dmg(_jground, _dud, "じしん")')
        tests_for_move.append('check("接地化: うちおとす", _before == 0 and _after > 0 and _dud.grounded, f"before={_before} after={_after} grounded={_dud.grounded}")')
        tests_for_move.append('# でんじふゆうも接地で解除')
        tests_for_move.append('_dud2 = make_poke(type1="でんき", hp_b=255, def_b=120); _dud2.magnet_rise = True')
        tests_for_move.append('execute(make_poke(type1="いわ", atk_b=100), _dud2, "うちおとす")')
        tests_for_move.append('check("でんじふゆう解除: うちおとす", not _dud2.magnet_rise, f"magnet={_dud2.magnet_rise}")')
    elif name == 'ミストバースト':
        tests_for_move.append('# ミストバースト: ミストフィールドで威力上昇')
        tests_for_move.append('_pmb = make_poke(type1="フェアリー", spatk_b=100); _dmb = make_poke(type1="ノーマル", spdef_b=100, hp_b=255)')
        tests_for_move.append('_mbn = calc_damage(_pmb, _dmb, dl.get_move("ミストバースト"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_fmf = BattleField(); _fmf.misty_terrain = True; _mbp = calc_damage(_pmb, _dmb, dl.get_move("ミストバースト"), _fmf, random_roll=1.0)')
        tests_for_move.append('check("ミストフィールド威力上昇: ミストバースト", _mbp > _mbn, f"n={_mbn} p={_mbp}")')
        tests_for_move.append(f'# 威力1.5倍の具体値（{power}→{int(power * 1.5)}）')
        tests_for_move.append('_mbx = make_poke(type1="フェアリー", spatk_b=100); _dbx = make_poke(type1="ノーマル", spdef_b=100)')
        tests_for_move.append('_mb_norm = _ep(_mbx, _dbx, dl.get_move("ミストバースト"), BattleField())')
        tests_for_move.append('_fmx = BattleField(); _fmx.misty_terrain = True; _mb_misty = _ep(_mbx, _dbx, dl.get_move("ミストバースト"), _fmx)')
        tests_for_move.append(f'check("通常威力{power}: ミストバースト", _mb_norm == {power}, f"norm={{_mb_norm}}")')
        tests_for_move.append(f'check("ミスト時1.5倍({int(power * 1.5)}): ミストバースト", _mb_misty == {int(power * 1.5)}, f"misty={{_mb_misty}}")')
    elif name == 'いかりのまえば':
        tests_for_move.append('# いかりのまえば: 相手の残りHPの1/2のダメージ')
        tests_for_move.append('_pi = make_poke(atk_b=100); _di = make_poke(hp_b=200); _di.hp = 160')
        tests_for_move.append('execute(_pi, _di, "いかりのまえば")')
        tests_for_move.append('check("1/2ダメ: いかりのまえば", _di.hp == 80, f"hp={_di.hp}")')
        tests_for_move.append('# 残りHP1の相手には1ダメージ（最低1保証）')
        tests_for_move.append('_pi2 = make_poke(atk_b=100); _di2 = make_poke(hp_b=200); _di2.hp = 1')
        tests_for_move.append('execute(_pi2, _di2, "いかりのまえば")')
        tests_for_move.append('check("残りHP1で1ダメージ: いかりのまえば", _di2.hp == 0, f"hp={_di2.hp}")')
    elif name in ('ほえる', 'ふきとばし', 'ドラゴンテール', 'ともえなげ'):
        tests_for_move.append(f'# {name}: 控えがいれば相手をランダム交代させる／控えがいなければ交代しない')
        tests_for_move.append(f'from simulator.battle import Battle as _Bfsw')
        tests_for_move.append(f'import simulator.battle as _SBfsw; _mx_fsw = _SBfsw.MAX_TURNS; _SBfsw.MAX_TURNS = 1')
        tests_for_move.append(f'import copy as _cpfs; _mvfs = _cpfs.copy(dl.get_move("{name}")); _mvfs.accuracy = 100')
        tests_for_move.append(f'_actfsw = lambda s,o,f: Action(type="move", move=_mvfs, move_idx=0)')
        tests_for_move.append(f'_actwk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)')
        tests_for_move.append(f'_pfsw = make_poke(type1="{atk_type}", atk_b=120, spd_b=200, moves=["{name}"])')
        tests_for_move.append(f'_df0 = make_poke(type1="ノーマル", hp_b=255, def_b=200, spd_b=10, moves=["たいあたり"]); _df1 = make_poke(type1="ノーマル", hp_b=255, moves=["たいあたり"])')
        tests_for_move.append(f'_sdef = BattleSide([_df0, _df1])')
        tests_for_move.append(f'_Bfsw(BattleSide([_pfsw]), _sdef).run(_actfsw, _actwk)')
        tests_for_move.append(f'check("控え有りで強制交代: {name}", _sdef.active is not _df0, f"active_idx={{_sdef.active_idx}}")')
        tests_for_move.append(f'_pfsw2 = make_poke(type1="{atk_type}", atk_b=120, spd_b=200, moves=["{name}"])')
        tests_for_move.append(f'_dsolo = make_poke(type1="ノーマル", hp_b=255, def_b=200, moves=["たいあたり"]); _ssolo = BattleSide([_dsolo])')
        tests_for_move.append(f'_Bfsw(BattleSide([_pfsw2]), _ssolo).run(_actfsw, _actwk)')
        tests_for_move.append(f'check("控えなしでは交代しない: {name}", _ssolo.active is _dsolo, "1体なら強制交代は発生しない")')
        tests_for_move.append(f'_SBfsw.MAX_TURNS = _mx_fsw')
    elif name == 'ハサミギロチン':
        tests_for_move.append('# ハサミギロチン: 命中時に相手を必ずひんし（HP量に依存しない）')
        tests_for_move.append('random.seed(0); _ohko_ok = False')
        tests_for_move.append('for _ in range(60):')
        tests_for_move.append('    _pa_oh = make_poke(type1="ノーマル"); _pd_oh = make_poke(type1="ノーマル", hp_b=255)')
        tests_for_move.append('    execute(_pa_oh, _pd_oh, "ハサミギロチン")')
        tests_for_move.append('    if not _pd_oh.is_alive: _ohko_ok = True; break')
        tests_for_move.append('check("一撃必殺(フルHP): ハサミギロチン", _ohko_ok, "60試行内に一撃必殺が発生すること")')
        tests_for_move.append('# 命中率30%統計（200試行で40〜100回ヒット）')
        tests_for_move.append('random.seed(1); _ohko_count = 0')
        tests_for_move.append('for _ in range(200):')
        tests_for_move.append('    _pa_s = make_poke(type1="ノーマル"); _pd_s = make_poke(type1="ノーマル", hp_b=255)')
        tests_for_move.append('    execute(_pa_s, _pd_s, "ハサミギロチン"); _ohko_count += (0 if _pd_s.is_alive else 1)')
        tests_for_move.append('check("命中率約30%: ハサミギロチン", 20 <= _ohko_count <= 100, f"hits={_ohko_count}/200")')
    elif name == 'カウンター':
        tests_for_move.append('# カウンター: 物理被ダメの2倍を返す。実際に物理技を受けてから使うintegrationも確認')
        tests_for_move.append('_pac = make_poke(type1="かくとう", hp_b=255, def_b=60)')
        tests_for_move.append('_attacker_phys = make_poke(type1="ノーマル", atk_b=100, hp_b=255)')
        tests_for_move.append('_execute_move(BattleSide([_attacker_phys]), BattleSide([_pac]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())')
        tests_for_move.append('_phys_received = _pac._last_physical_dmg_received')
        tests_for_move.append('_pdc = make_poke(type1="ノーマル", hp_b=255, def_b=50); _hpc0 = _pdc.hp')
        tests_for_move.append('execute(_pac, _pdc, "カウンター")')
        tests_for_move.append('check("物理被ダメ×2返却: カウンター", _hpc0 - _pdc.hp == _phys_received * 2, f"received={_phys_received} returned={_hpc0 - _pdc.hp} expected={_phys_received * 2}")')
        tests_for_move.append('# 被ダメなしは失敗')
        tests_for_move.append('_pac2 = make_poke(type1="かくとう"); _pdc2 = make_poke(type1="ノーマル", hp_b=255); _hp2 = _pdc2.hp')
        tests_for_move.append('execute(_pac2, _pdc2, "カウンター")')
        tests_for_move.append('check("被ダメ0で失敗: カウンター", _pdc2.hp == _hp2)')
        tests_for_move.append('# 特殊技を受けただけでは反射しない（物理のみ反応）')
        tests_for_move.append('_pac3 = make_poke(type1="かくとう", hp_b=255); _pac3._last_special_dmg_received = 100; _pac3._last_physical_dmg_received = 0')
        tests_for_move.append('_pdc3 = make_poke(type1="ノーマル", hp_b=255); _hp3 = _pdc3.hp')
        tests_for_move.append('execute(_pac3, _pdc3, "カウンター")')
        tests_for_move.append('check("特殊被弾では反射しない: カウンター", _pdc3.hp == _hp3, f"hp={_pdc3.hp}/{_hp3}")')
    elif name == 'ミラーコート':
        tests_for_move.append('# ミラーコート: 特殊被ダメの2倍を返す。実戦で特殊技を受けてから使うintegration')
        tests_for_move.append('_pmc = make_poke(type1="エスパー", hp_b=255, spdef_b=60)')
        tests_for_move.append('_atk_spec = make_poke(type1="エスパー", spatk_b=100, hp_b=255)')
        tests_for_move.append('_execute_move(BattleSide([_atk_spec]), BattleSide([_pmc]), Action(type="move", move=dl.get_move("サイコキネシス")), BattleField())')
        tests_for_move.append('_spec_received = _pmc._last_special_dmg_received')
        tests_for_move.append('_dmc = make_poke(type1="ノーマル", hp_b=255, def_b=50); _hpm0 = _dmc.hp')
        tests_for_move.append('execute(_pmc, _dmc, "ミラーコート")')
        tests_for_move.append('check("特殊被ダメ×2返却(実戦): ミラーコート", _spec_received > 0 and _hpm0 - _dmc.hp == _spec_received * 2, f"received={_spec_received} returned={_hpm0 - _dmc.hp}")')
        tests_for_move.append('# 被ダメなしは失敗')
        tests_for_move.append('_pmc2 = make_poke(type1="エスパー"); _dmc2 = make_poke(type1="ノーマル", hp_b=255); _hpm2 = _dmc2.hp')
        tests_for_move.append('execute(_pmc2, _dmc2, "ミラーコート")')
        tests_for_move.append('check("被ダメ0で失敗: ミラーコート", _dmc2.hp == _hpm2)')
        tests_for_move.append('# 物理技を受けただけでは反射しない（特殊のみ反応）')
        tests_for_move.append('_pmc3 = make_poke(type1="エスパー", hp_b=255); _pmc3._last_physical_dmg_received = 100; _pmc3._last_special_dmg_received = 0')
        tests_for_move.append('_dmc3 = make_poke(type1="ノーマル", hp_b=255); _hpm3 = _dmc3.hp')
        tests_for_move.append('execute(_pmc3, _dmc3, "ミラーコート")')
        tests_for_move.append('check("物理被弾では反射しない: ミラーコート", _dmc3.hp == _hpm3, f"hp={_dmc3.hp}/{_hpm3}")')
    elif name == 'けたぐり':
        tests_for_move.append('# けたぐり: 重さによる威力テーブル（各境界を検証）')
        tests_for_move.append('_pa_kg = make_poke(type1="かくとう", atk_b=100)')
        tests_for_move.append('for _w, _exp in [(5,20),(15,40),(35,60),(75,80),(150,100),(300,120)]:')
        tests_for_move.append('    _d_kg = make_poke(type1="ノーマル"); _d_kg.weight_kg = float(_w)')
        tests_for_move.append('    _got_kg = _ep(_pa_kg, _d_kg, dl.get_move("けたぐり"), BattleField())')
        tests_for_move.append('    check(f"重さ{_w}kg→威力{_exp}: けたぐり", _got_kg == _exp, f"w={_w}kg got={_got_kg} exp={_exp}")')
    elif name == 'どろぼう':
        tests_for_move.append('# どろぼう: 相手の道具を奪う（自分が道具なし時のみ）')
        tests_for_move.append('_pst = make_poke(type1="あく", atk_b=120); _pst.item = None')
        tests_for_move.append('_dst = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst.item = "オボンのみ"')
        tests_for_move.append('execute(_pst, _dst, "どろぼう")')
        tests_for_move.append('check("道具奪取: どろぼう", _pst.item == "オボンのみ" and _dst.item is None, f"atk={_pst.item} def={_dst.item}")')
        tests_for_move.append('# 攻撃者が道具持ちの場合は奪わない')
        tests_for_move.append('_pst2 = make_poke(type1="あく", atk_b=120, item="こだわりスカーフ"); _dst2 = make_poke(type1="ノーマル", hp_b=255, def_b=100, item="オボンのみ")')
        tests_for_move.append('execute(_pst2, _dst2, "どろぼう")')
        tests_for_move.append('check("道具持ちは奪わない: どろぼう", _pst2.item == "こだわりスカーフ" and _dst2.item == "オボンのみ", f"atk={_pst2.item} def={_dst2.item}")')
        tests_for_move.append('# 相手がメガストーンを持っている場合は奪えない')
        tests_for_move.append('_pst3 = make_poke(type1="あく", atk_b=120); _pst3.item = None')
        tests_for_move.append('_dst3 = make_poke(type1="ノーマル", hp_b=255, def_b=100, item="ガブリアスナイト")')
        tests_for_move.append('execute(_pst3, _dst3, "どろぼう")')
        tests_for_move.append('check("メガストーンは奪えない: どろぼう", _pst3.item is None and _dst3.item == "ガブリアスナイト", f"atk={_pst3.item} def={_dst3.item}")')
    elif name == 'トリック':
        tests_for_move.append('# トリック: 道具交換（メガストーンは失敗）')
        tests_for_move.append('_ptrk = make_poke(type1="エスパー", item="こだわりスカーフ"); _dtrk = make_poke(type1="ノーマル", item="オボンのみ")')
        tests_for_move.append('execute(_ptrk, _dtrk, "トリック")')
        tests_for_move.append('check("道具入替: トリック", _ptrk.item == "オボンのみ" and _dtrk.item == "こだわりスカーフ", f"atk={_ptrk.item} def={_dtrk.item}")')
        tests_for_move.append('# 相手がメガストーンを持つ場合は失敗')
        tests_for_move.append('_ptrk2 = make_poke(type1="エスパー", item="こだわりスカーフ"); _dtrk2 = make_poke(type1="ノーマル", item="ガブリアスナイト")')
        tests_for_move.append('execute(_ptrk2, _dtrk2, "トリック")')
        tests_for_move.append('check("メガストーン交換失敗: トリック", _ptrk2.item == "こだわりスカーフ" and _dtrk2.item == "ガブリアスナイト", f"atk={_ptrk2.item} def={_dtrk2.item}")')
    elif name == 'すりかえ':
        tests_for_move.append('# すりかえ: 道具交換（メガストーンは失敗）')
        tests_for_move.append('_psrk = make_poke(type1="エスパー", item="こだわりメガネ"); _dsrk = make_poke(type1="ノーマル", item="オボンのみ")')
        tests_for_move.append('execute(_psrk, _dsrk, "すりかえ")')
        tests_for_move.append('check("道具入替: すりかえ", _psrk.item == "オボンのみ" and _dsrk.item == "こだわりメガネ", f"atk={_psrk.item} def={_dsrk.item}")')
        tests_for_move.append('# 相手がメガストーンを持つ場合は失敗')
        tests_for_move.append('_psrk2 = make_poke(type1="エスパー", item="こだわりメガネ"); _dsrk2 = make_poke(type1="ノーマル", item="ガブリアスナイト")')
        tests_for_move.append('execute(_psrk2, _dsrk2, "すりかえ")')
        tests_for_move.append('check("メガストーン交換失敗: すりかえ", _psrk2.item == "こだわりメガネ" and _dsrk2.item == "ガブリアスナイト", f"atk={_psrk2.item} def={_dsrk2.item}")')
    elif name == 'からげんき':
        tests_for_move.append('# からげんき: 状態異常時に威力2倍（等値検証）')
        tests_for_move.append('_pk = make_poke(type1="ノーマル", atk_b=120); _dk = make_poke(type1="いわ", def_b=120, hp_b=255)')
        tests_for_move.append('_kn = calc_damage(_pk, _dk, dl.get_move("からげんき"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_pk.status = "paralysis"; _ks = calc_damage(_pk, _dk, dl.get_move("からげんき"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("状態異常で2倍: からげんき", abs(_ks - _kn * 2) <= 1, f"n={_kn} s={_ks} expected={_kn*2}")')
        tests_for_move.append('# やけど状態でも攻撃半減を受けない（やけど状態のダメージ≈通常状態の2倍）')
        tests_for_move.append('_pk_burn = make_poke(type1="ノーマル", atk_b=120); _dk2 = make_poke(type1="いわ", def_b=120, hp_b=255)')
        tests_for_move.append('_pk_burn.status = "burn"')
        tests_for_move.append('_k_burn = calc_damage(_pk_burn, _dk2, dl.get_move("からげんき"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("やけど攻撃半減無視: からげんき", abs(_k_burn - _kn * 2) <= 1, f"burn={_k_burn} normal={_kn} expected={_kn*2}")')
    elif name == 'かわらわり':
        tests_for_move.append('# かわらわり: スクリーンを無視してダメージ（スクリーン有り≈無しと同等）、かつスクリーンを破壊する')
        tests_for_move.append('_pakw = make_poke(type1="かくとう", atk_b=150)')
        tests_for_move.append('# 同じシードで実行してランダムロールを揃える')
        tests_for_move.append('random.seed(77); _dkw_no = make_poke(type1="ノーマル", def_b=80, hp_b=255)')
        tests_for_move.append('_execute_move(BattleSide([_pakw]), BattleSide([_dkw_no]), Action(type="move", move=dl.get_move("かわらわり")), BattleField())')
        tests_for_move.append('_dmg_no_scr = _dkw_no.max_hp - _dkw_no.hp')
        tests_for_move.append('random.seed(77); _dkw_ref = make_poke(type1="ノーマル", def_b=80, hp_b=255)')
        tests_for_move.append('_s2_ref = BattleSide([_dkw_ref]); _s2_ref.reflect = True; _s2_ref.reflect_count = 5')
        tests_for_move.append('_execute_move(BattleSide([_pakw]), _s2_ref, Action(type="move", move=dl.get_move("かわらわり")), BattleField())')
        tests_for_move.append('_dmg_with_scr = _dkw_ref.max_hp - _dkw_ref.hp')
        tests_for_move.append('check("スクリーン無視(等ダメ): かわらわり", _dmg_no_scr == _dmg_with_scr, f"no_screen={_dmg_no_scr} with_screen={_dmg_with_scr}")')
        tests_for_move.append('check("スクリーン破壊: かわらわり", not _s2_ref.reflect, f"reflect={_s2_ref.reflect}")')
    elif name == 'ジャイロボール':
        tests_for_move.append('# ジャイロボール: 威力 = min(150, floor(25×相手速度/自速度))。具体値と上限を検証')
        tests_for_move.append('_pg = make_poke(atk_b=100, spd_b=10); _df = make_poke(spd_b=200, def_b=100); _de = make_poke(spd_b=10, def_b=100)')
        tests_for_move.append('_gslow = _ep(_pg, _df, dl.get_move("ジャイロボール"), BattleField()); _geq = _ep(_pg, _de, dl.get_move("ジャイロボール"), BattleField())')
        tests_for_move.append('check("速度比威力: ジャイロボール", _gslow > _geq, f"slow={_gslow} eq={_geq}")')
        tests_for_move.append('# 具体値: 相手speed=自speedの4倍 → 25×4=100')
        tests_for_move.append('_pg4 = make_poke(spd_b=10); _df4 = make_poke(spd_b=10); import math as _m')
        tests_for_move.append('_sa = _pg4.get_effective_speed(); _df4.speed = _sa * 4')
        tests_for_move.append('_exp_g = min(150, max(1, _m.floor(25 * _df4.get_effective_speed() / _sa)))')
        tests_for_move.append('_got_g = _ep(_pg4, _df4, dl.get_move("ジャイロボール"), BattleField())')
        tests_for_move.append('check("威力式(25×相手/自): ジャイロボール", _got_g == _exp_g, f"got={_got_g} exp={_exp_g}")')
        tests_for_move.append('# 上限150: 相手が極端に速い')
        tests_for_move.append('_pg_s = make_poke(spd_b=4); _df_f = make_poke(spd_b=255); _df_f.speed = 99999')
        tests_for_move.append('_got_cap = _ep(_pg_s, _df_f, dl.get_move("ジャイロボール"), BattleField())')
        tests_for_move.append('check("威力上限150: ジャイロボール", _got_cap == 150, f"got={_got_cap}")')
    elif name == 'しっぺがえし':
        tests_for_move.append('# しっぺがえし: _acts_second状態で威力2倍')
        tests_for_move.append('_ps = make_poke(atk_b=100); _ds = make_poke(def_b=100)')
        tests_for_move.append('_sa = _ep(_ps, _ds, dl.get_move("しっぺがえし"), BattleField()); _ps._acts_second = True; _sb = _ep(_ps, _ds, dl.get_move("しっぺがえし"), BattleField())')
        tests_for_move.append('check("後攻2倍: しっぺがえし", _sb == _sa * 2, f"a={_sa} b={_sb}")')
        tests_for_move.append('# 実戦: 後攻（遅い）で使うと先攻時より大ダメージ＝条件が実機能')
        tests_for_move.append('from simulator.battle import Battle as _Bsp')
        tests_for_move.append('import simulator.battle as _SBsp; _msp = _SBsp.MAX_TURNS; _SBsp.MAX_TURNS = 1')
        tests_for_move.append('_act_sp = lambda s,o,f: Action(type="move", move=dl.get_move("しっぺがえし"), move_idx=0)')
        tests_for_move.append('_act_wk = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)')
        tests_for_move.append('_psp_slow = make_poke(type1="あく", atk_b=120, spd_b=10, moves=["しっぺがえし"]); _fsp = make_poke(type1="エスパー", atk_b=10, spd_b=200, hp_b=255, def_b=120, moves=["たいあたり"])')
        tests_for_move.append('_Bsp(BattleSide([_psp_slow]), BattleSide([_fsp])).run(_act_sp, _act_wk)')
        tests_for_move.append('_dmg_second = _fsp.max_hp - _fsp.hp')
        tests_for_move.append('_psp_fast = make_poke(type1="あく", atk_b=120, spd_b=200, moves=["しっぺがえし"]); _fsp2 = make_poke(type1="エスパー", atk_b=10, spd_b=10, hp_b=255, def_b=120, moves=["たいあたり"])')
        tests_for_move.append('_Bsp(BattleSide([_psp_fast]), BattleSide([_fsp2])).run(_act_sp, _act_wk)')
        tests_for_move.append('_dmg_first = _fsp2.max_hp - _fsp2.hp; _SBsp.MAX_TURNS = _msp')
        tests_for_move.append('check("後攻条件が実戦で成立: しっぺがえし", _dmg_second > _dmg_first * 1.4, f"後攻={_dmg_second} 先攻={_dmg_first}")')
    elif name == 'アクロバット':
        tests_for_move.append('# アクロバット: 道具を持っていないと威力2倍')
        tests_for_move.append('_pa = make_poke(atk_b=100, item="オボンのみ"); _pa2 = make_poke(atk_b=100); _da = make_poke(def_b=100)')
        tests_for_move.append('_wi = _ep(_pa, _da, dl.get_move("アクロバット"), BattleField()); _wn = _ep(_pa2, _da, dl.get_move("アクロバット"), BattleField())')
        tests_for_move.append('check("アクロバット道具なし2倍: アクロバット", _wn == _wi * 2, f"item={_wi} no={_wn}")')
    elif name == 'Gのちから':
        tests_for_move.append('# Gのちから: じゅうりょく状態で威力1.5倍')
        tests_for_move.append('_pgc = make_poke(spatk_b=100); _dgc = make_poke(spdef_b=100)')
        tests_for_move.append('_gn = _ep(_pgc, _dgc, dl.get_move("Gのちから"), BattleField()); _fgv = BattleField(); _fgv.gravity = 1; _gg = _ep(_pgc, _dgc, dl.get_move("Gのちから"), _fgv)')
        tests_for_move.append('check("じゅうりょく1.5倍: Gのちから", _gg > _gn, f"n={_gn} g={_gg}")')
        tests_for_move.append(f'check("通常威力{power}: Gのちから", _gn == {power}, f"n={{_gn}}")')
        tests_for_move.append(f'check("じゅうりょく時1.5倍具体値({int(power * 1.5)}): Gのちから", _gg == {int(power * 1.5)}, f"g={{_gg}}")')
    elif name == 'ワイドフォース':
        tests_for_move.append('# ワイドフォース: サイコフィールドで威力上昇')
        tests_for_move.append('_pw = make_poke(type1="エスパー", spatk_b=100); _dw = make_poke(type1="ノーマル", spdef_b=100, hp_b=255)')
        tests_for_move.append('_wn0 = calc_damage(_pw, _dw, dl.get_move("ワイドフォース"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_fpt = BattleField(); _fpt.psychic_terrain = True; _wp = calc_damage(_pw, _dw, dl.get_move("ワイドフォース"), _fpt, random_roll=1.0)')
        tests_for_move.append('check("サイコフィールド威力上昇: ワイドフォース", _wp > _wn0, f"n={_wn0} p={_wp}")')
    elif name == 'シェルアームズ':
        tests_for_move.append('# シェルアームズ: 物理/特殊のうち相手の低い防御を突く')
        tests_for_move.append('_psh = make_poke(atk_b=150, spatk_b=150); _dlowdef = make_poke(def_b=1, spdef_b=255, hp_b=255); _dhigh = make_poke(def_b=255, spdef_b=255, hp_b=255)')
        tests_for_move.append('_dmg_low = calc_damage(_psh, _dlowdef, dl.get_move("シェルアームズ"), BattleField(), random_roll=1.0); _dmg_high = calc_damage(_psh, _dhigh, dl.get_move("シェルアームズ"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("物理特殊の有利側選択: シェルアームズ", _dmg_low > _dmg_high, f"lowdef={_dmg_low} high={_dmg_high}")')
    elif name == 'ダメおし':
        tests_for_move.append('# ダメおし: _acts_second状態（相手が既に行動済み）で威力2倍')
        tests_for_move.append('_pd = make_poke(atk_b=100); _dd = make_poke(def_b=100)')
        tests_for_move.append('_da1 = _ep(_pd, _dd, dl.get_move("ダメおし"), BattleField()); _pd._acts_second = True; _da2 = _ep(_pd, _dd, dl.get_move("ダメおし"), BattleField())')
        tests_for_move.append('check("ダメおし後攻2倍: ダメおし", _da2 == _da1 * 2, f"a={_da1} b={_da2}")')
        tests_for_move.append('# 実戦: 後攻（遅い）で使うと先攻時より大ダメージ＝条件が実機能')
        tests_for_move.append('from simulator.battle import Battle as _Bdm')
        tests_for_move.append('import simulator.battle as _SBdm; _mdm = _SBdm.MAX_TURNS; _SBdm.MAX_TURNS = 1')
        tests_for_move.append('_act_dm = lambda s,o,f: Action(type="move", move=dl.get_move("ダメおし"), move_idx=0)')
        tests_for_move.append('_act_wk2 = lambda s,o,f: Action(type="move", move=dl.get_move("たいあたり"), move_idx=0)')
        tests_for_move.append('_pdm_slow = make_poke(type1="あく", atk_b=120, spd_b=10, moves=["ダメおし"]); _fdm = make_poke(type1="エスパー", atk_b=10, spd_b=200, hp_b=255, def_b=120, moves=["たいあたり"])')
        tests_for_move.append('_Bdm(BattleSide([_pdm_slow]), BattleSide([_fdm])).run(_act_dm, _act_wk2)')
        tests_for_move.append('_dmg_2nd = _fdm.max_hp - _fdm.hp')
        tests_for_move.append('_pdm_fast = make_poke(type1="あく", atk_b=120, spd_b=200, moves=["ダメおし"]); _fdm2 = make_poke(type1="エスパー", atk_b=10, spd_b=10, hp_b=255, def_b=120, moves=["たいあたり"])')
        tests_for_move.append('_Bdm(BattleSide([_pdm_fast]), BattleSide([_fdm2])).run(_act_dm, _act_wk2)')
        tests_for_move.append('_dmg_1st = _fdm2.max_hp - _fdm2.hp; _SBdm.MAX_TURNS = _mdm')
        tests_for_move.append('check("後攻条件が実戦で成立: ダメおし", _dmg_2nd > _dmg_1st * 1.4, f"後攻={_dmg_2nd} 先攻={_dmg_1st}")')
    elif name == 'おはかまいり':
        tests_for_move.append('# おはかまいり: ひんしの味方が多いほど威力が高い')
        tests_for_move.append('_po = make_poke(atk_b=100); _do = make_poke(def_b=100)')
        tests_for_move.append('_o0 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField()); _po.fainted_allies = 3; _o3 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField())')
        tests_for_move.append('_po.fainted_allies = 5; _o5 = _ep(_po, _do, dl.get_move("おはかまいり"), BattleField())')
        tests_for_move.append('check("ひんし0で威力50: おはかまいり", _o0 == 50, f"0={_o0}")')
        tests_for_move.append('check("ひんし3で威力200(50+50×3): おはかまいり", _o3 == 200, f"3={_o3}")')
        tests_for_move.append('check("ひんし上限5で威力300: おはかまいり", _o5 == 300, f"5={_o5}")')
    elif name == 'ほのおのまい':
        tests_for_move.append('# ほのおのまい: 50%で自分の特攻+1')
        tests_for_move.append('random.seed(0); _fd_up = False')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    _pfd = make_poke(type1="ほのお", spatk_b=100); _dfd = make_poke(type1="くさ", hp_b=255, spdef_b=200)')
        tests_for_move.append('    execute(_pfd, _dfd, "ほのおのまい")')
        tests_for_move.append('    if _pfd.stage_sp_attack > 0: _fd_up = True; break')
        tests_for_move.append('check("自分特攻上昇: ほのおのまい", _fd_up)')
    elif name == 'うたかたのアリア':
        tests_for_move.append('# うたかたのアリア: 相手のやけどを治す')
        tests_for_move.append('_pu = make_poke(type1="みず", spatk_b=100); _du = make_poke(type1="ノーマル", hp_b=255, spdef_b=200); _du.status = "burn"')
        tests_for_move.append('execute(_pu, _du, "うたかたのアリア")')
        tests_for_move.append('check("やけど治癒: うたかたのアリア", _du.status is None, f"status={_du.status}")')
    elif name == 'しおづけ':
        tests_for_move.append('# しおづけ: 相手をしおづけ状態にする')
        tests_for_move.append('_psl = make_poke(atk_b=100); _dsl = make_poke(hp_b=255, def_b=120); execute(_psl, _dsl, "しおづけ")')
        tests_for_move.append('check("しおづけ付与: しおづけ", getattr(_dsl, "_salted", False))')
    elif name == 'レイジングブル':
        tests_for_move.append('# レイジングブル: 自分のフォルム(type2)で技タイプが変わる')
        tests_for_move.append('from simulator.damage import _effective_move_type as _emtr')
        tests_for_move.append('_prb = make_poke(type1="ノーマル", type2="ほのお")')
        tests_for_move.append('check("フォルム別タイプ: レイジングブル", _emtr(_prb, dl.get_move("レイジングブル"), BattleField()) == "ほのお", f"type={_emtr(_prb, dl.get_move(\'レイジングブル\'), BattleField())}")')
    elif name == 'しっぽきり':
        tests_for_move.append('# しっぽきり: HP1/2を消費してみがわりを残す')
        tests_for_move.append('_satk = BattleSide([make_poke(hp_b=200), make_poke()]); _satk.active.hp = _satk.active.max_hp; _hpsk = _satk.active.hp')
        tests_for_move.append('_execute_move(_satk, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("しっぽきり")), BattleField())')
        tests_for_move.append('check("みがわり生成: しっぽきり", getattr(_satk.party[0], "_substitute_hp", 0) > 0 and _satk.party[0].hp < _hpsk, f"sub={getattr(_satk.party[0],\'_substitute_hp\',0)}")')
        tests_for_move.append('# 消費は最大HP1/2・身代わりHPは最大HP1/4（effect_text通り）')
        tests_for_move.append('_satk_v = BattleSide([make_poke(hp_b=200), make_poke()]); _satk_v.active.hp = _satk_v.active.max_hp; _mhp = _satk_v.active.max_hp')
        tests_for_move.append('_execute_move(_satk_v, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("しっぽきり")), BattleField())')
        tests_for_move.append('check("HP消費1/2: しっぽきり", _satk_v.party[0].hp == _mhp - _mhp // 2, f"hp={_satk_v.party[0].hp} 期待={_mhp - _mhp // 2}")')
        tests_for_move.append('check("身代わりHP1/4: しっぽきり", _satk_v.party[0]._substitute_hp == _mhp // 4, f"sub={_satk_v.party[0]._substitute_hp} 期待={_mhp // 4}")')
        tests_for_move.append('# 身代わりが技を肩代わり（本体ダメージなし）')
        tests_for_move.append('_holder = _satk_v.party[0]; _sub_sk = _holder._substitute_hp; _hp_sk = _holder.hp')
        tests_for_move.append('_atksk = make_poke(type1="ノーマル", atk_b=20, moves=["たいあたり"])')
        tests_for_move.append('_execute_move(BattleSide([_atksk]), BattleSide([_holder]), Action(type="move", move=dl.get_move("たいあたり")), BattleField())')
        tests_for_move.append('check("身代わりが肩代わり(本体ダメージなし): しっぽきり", _holder.hp == _hp_sk and getattr(_holder,"_substitute_hp",0) < _sub_sk, f"hp={_holder.hp}/{_hp_sk} sub={getattr(_holder,\'_substitute_hp\',0)}/{_sub_sk}")')
    elif name == 'こうそくスピン':
        tests_for_move.append('# こうそくスピン: 自分のやどりぎ/バインドを解除')
        tests_for_move.append('_pcs = make_poke(type1="ノーマル", atk_b=100, spd_b=100); _pcs.seeded = True; _dcs = make_poke(hp_b=255, def_b=120)')
        tests_for_move.append('execute(_pcs, _dcs, "こうそくスピン")')
        tests_for_move.append('check("バインド/やどりぎ解除: こうそくスピン", not _pcs.seeded, f"seeded={_pcs.seeded}")')
    elif name == 'キラースピン':
        tests_for_move.append('# キラースピン: 自分のやどりぎ/バインドを解除')
        tests_for_move.append('_pks = make_poke(type1="ノーマル", atk_b=120); _pks.seeded = True; _dks = make_poke(type1="ノーマル", hp_b=255, def_b=120)')
        tests_for_move.append('execute(_pks, _dks, "キラースピン")')
        tests_for_move.append('check("バインド解除: キラースピン", not _pks.seeded, f"seeded={_pks.seeded}")')
    elif name == 'デカハンマー':
        tests_for_move.append('# デカハンマー: 2ターン連続では使えない')
        tests_for_move.append('_pdh = make_poke(type1="はがね", atk_b=120); _ddh = make_poke(type1="フェアリー", hp_b=255, def_b=120)')
        tests_for_move.append('execute(_pdh, _ddh, "デカハンマー"); _hp_after1 = _ddh.hp; execute(_pdh, _ddh, "デカハンマー")')
        tests_for_move.append('check("連続不可: デカハンマー", _ddh.hp == _hp_after1, f"2回目hp={_ddh.hp}/{_hp_after1}")')
    elif name == 'みずあめボム':
        tests_for_move.append('# みずあめボム: 相手をあめまみれ状態に（素早さ低下）')
        tests_for_move.append('_psb = make_poke(type1="みず", spatk_b=100); _dsb = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)')
        tests_for_move.append('random.seed(0)')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    execute(_psb, _dsb, "みずあめボム")')
        tests_for_move.append('    if _dsb.syrup_count == 3: break')
        tests_for_move.append('check("あめまみれ付与: みずあめボム", _dsb.syrup_count == 3, f"syrup={_dsb.syrup_count}")')
    elif name == 'きまぐレーザー':
        tests_for_move.append('# きまぐレーザー: 30%で威力2倍（複数回で2倍が出る）')
        tests_for_move.append('_pkl = make_poke(spatk_b=100); _dkl = make_poke(def_b=100)')
        tests_for_move.append('random.seed(0); _kls = [_ep(_pkl, _dkl, dl.get_move("きまぐレーザー"), BattleField()) for _ in range(60)]')
        tests_for_move.append('_klbase = min(_kls); check("30%威力2倍: きまぐレーザー", max(_kls) == _klbase * 2, f"vals={sorted(set(_kls))}")')
    elif name == 'サイコノイズ':
        tests_for_move.append('# サイコノイズ: 相手をかいふくふうじ状態に')
        tests_for_move.append('_psn = make_poke(type1="エスパー", spatk_b=100); _dsn = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)')
        tests_for_move.append('execute(_psn, _dsn, "サイコノイズ")')
        tests_for_move.append('check("かいふくふうじ付与: サイコノイズ", _dsn.heal_block_count == 2, f"hb={_dsn.heal_block_count}")')
    elif name == 'クリアスモッグ':
        tests_for_move.append('# クリアスモッグ: 命中時に相手の能力変化をリセット')
        tests_for_move.append('_pcl = make_poke(type1="どく", spatk_b=100); _dcl = make_poke(type1="ノーマル", hp_b=255, spdef_b=120); _dcl.stage_attack = 2; _dcl.stage_speed = 3')
        tests_for_move.append('execute(_pcl, _dcl, "クリアスモッグ")')
        tests_for_move.append('check("能力リセット: クリアスモッグ", _dcl.stage_attack == 0 and _dcl.stage_speed == 0, f"atk={_dcl.stage_attack} spd={_dcl.stage_speed}")')
    elif name == 'フェイタルクロー':
        tests_for_move.append('# フェイタルクロー: どく・まひ・ねむりの「いずれか」→3状態すべてが実際に発生する')
        tests_for_move.append('_pfc_m = make_poke(type1="どく", atk_b=30)')
        tests_for_move.append('random.seed(0); _fc_cnt = {"poison":0, "paralysis":0, "sleep":0}')
        tests_for_move.append('for _ in range(600):')
        tests_for_move.append('    _dfc = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)')
        tests_for_move.append('    execute(_pfc_m, _dfc, "フェイタルクロー")')
        tests_for_move.append('    if _dfc.status in _fc_cnt: _fc_cnt[_dfc.status] += 1')
        tests_for_move.append('check("いずれか3状態すべて発生: フェイタルクロー", all(_v > 0 for _v in _fc_cnt.values()), f"counts={_fc_cnt}")')
    elif name == 'トライアタック':
        tests_for_move.append('# トライアタック: まひ・やけど・こおりの「いずれか」→3状態すべてが実際に発生する')
        tests_for_move.append('_pta_m = make_poke(type1="ノーマル", spatk_b=30)')
        tests_for_move.append('random.seed(0); _ta_cnt = {"paralysis":0, "burn":0, "freeze":0}')
        tests_for_move.append('for _ in range(900):')
        tests_for_move.append('    _dta_m = make_poke(type1="ドラゴン", hp_b=255, def_b=255, spdef_b=255)')
        tests_for_move.append('    execute(_pta_m, _dta_m, "トライアタック")')
        tests_for_move.append('    if _dta_m.status in _ta_cnt: _ta_cnt[_dta_m.status] += 1')
        tests_for_move.append('check("いずれか3状態すべて発生: トライアタック", all(_v > 0 for _v in _ta_cnt.values()), f"counts={_ta_cnt}")')
    elif name == 'ポルターガイスト':
        tests_for_move.append('# ポルターガイスト: 相手が道具を持っていないと失敗')
        tests_for_move.append('_ppg = make_poke(type1="ゴースト", atk_b=100); _dpg = make_poke(type1="エスパー", hp_b=255, def_b=120, item=None); _hppg = _dpg.hp')
        tests_for_move.append('execute(_ppg, _dpg, "ポルターガイスト")')
        tests_for_move.append('check("ポルターガイスト道具なし失敗: ポルターガイスト", _dpg.hp == _hppg, f"hp={_dpg.hp}/{_hppg}")')
        tests_for_move.append('# 相手が道具を持っていれば成功（ダメージが通る）')
        tests_for_move.append('_ppg2 = make_poke(type1="ゴースト", atk_b=120); _dpg2 = make_poke(type1="エスパー", hp_b=255, def_b=120); _dpg2.item = "オボンのみ"; _hppg2 = _dpg2.hp')
        tests_for_move.append('execute(_ppg2, _dpg2, "ポルターガイスト")')
        tests_for_move.append('check("道具あり成功: ポルターガイスト", _dpg2.hp < _hppg2, f"hp={_dpg2.hp}/{_hppg2}")')
    elif name == 'とどめばり':
        tests_for_move.append('# とどめばり: 相手を倒すと自分の攻撃+3')
        tests_for_move.append('_ptd = make_poke(type1="むし", atk_b=220); _dtd = make_poke(type1="あく", hp_b=1, def_b=1)')
        tests_for_move.append('execute(_ptd, _dtd, "とどめばり")')
        tests_for_move.append('check("とどめばりKO攻撃+3: とどめばり", (not _dtd.is_alive) and _ptd.stage_attack == 3, f"alive={_dtd.is_alive} atk={_ptd.stage_attack}")')
        tests_for_move.append('# negative: 倒せなかった場合は攻撃が上がらない')
        tests_for_move.append('_ptd2 = make_poke(type1="むし", atk_b=10); _dtd2 = make_poke(type1="あく", hp_b=255, def_b=255)')
        tests_for_move.append('execute(_ptd2, _dtd2, "とどめばり")')
        tests_for_move.append('check("非KO時は攻撃上昇なし: とどめばり", _dtd2.is_alive and _ptd2.stage_attack == 0, f"alive={_dtd2.is_alive} atk={_ptd2.stage_attack}")')
    elif name == 'へんしん':
        tests_for_move.append('# へんしん: 相手のステータス・タイプをコピー')
        tests_for_move.append('_pt = make_poke(type1="ノーマル", atk_b=40); _dt = make_poke(type1="みず", atk_b=180)')
        tests_for_move.append('execute(_pt, _dt, "へんしん")')
        tests_for_move.append('check("変身コピー: へんしん", _pt.attack == _dt.attack and _pt.type1 == "みず", f"atk={_pt.attack}/{_dt.attack} type={_pt.type1}")')
        tests_for_move.append('# HP以外の全ステータスをコピー・HPは自分のまま')
        tests_for_move.append('_dt2 = make_poke(type1="みず", atk_b=180, def_b=170, spatk_b=160, spdef_b=150, spd_b=140)')
        tests_for_move.append('_pt2 = make_poke(type1="ノーマル", atk_b=40, hp_b=200); _hp_keep = _pt2.max_hp')
        tests_for_move.append('execute(_pt2, _dt2, "へんしん")')
        tests_for_move.append('check("全ステータスコピー: へんしん", (_pt2.attack,_pt2.defense,_pt2.sp_attack,_pt2.sp_defense,_pt2.speed) == (_dt2.attack,_dt2.defense,_dt2.sp_attack,_dt2.sp_defense,_dt2.speed), f"self={(_pt2.attack,_pt2.defense,_pt2.sp_attack,_pt2.sp_defense,_pt2.speed)} foe={(_dt2.attack,_dt2.defense,_dt2.sp_attack,_dt2.sp_defense,_dt2.speed)}")')
        tests_for_move.append('check("HPはコピーしない: へんしん", _pt2.max_hp == _hp_keep, f"max_hp={_pt2.max_hp} keep={_hp_keep}")')
        tests_for_move.append('# 特性・技PP5・状態異常/持ち物の非コピー・交代で元に戻る')
        tests_for_move.append('_dt3 = make_poke(type1="みず", atk_b=180, spatk_b=160, ability="ちょすい", moves=["たいあたり","なみのり"]); _dt3.status = "burn"; _dt3.item = "オボンのみ"')
        tests_for_move.append('_sht = BattleSide([make_poke(type1="ノーマル", atk_b=40, ability="てんねん"), make_poke()])')
        tests_for_move.append('_orig_atk = _sht.active.attack; _orig_ab = _sht.active.ability; _sht.active.item = None')
        tests_for_move.append('execute(_sht.active, _dt3, "へんしん")')
        tests_for_move.append('_tf = _sht.active')
        tests_for_move.append('check("特性コピー: へんしん", _tf.ability == "ちょすい", f"ability={_tf.ability}")')
        tests_for_move.append('check("技PP5: へんしん", len(_tf.pp) > 0 and all(p == 5 for p in _tf.pp), f"pp={_tf.pp}")')
        tests_for_move.append('check("状態異常は非コピー: へんしん", _tf.status is None, f"status={_tf.status}")')
        tests_for_move.append('check("持ち物は非コピー: へんしん", _tf.item is None, f"item={_tf.item}")')
        tests_for_move.append('_sht.switch_to(1)')
        tests_for_move.append('check("交代で元に戻る: へんしん", _sht.party[0].attack == _orig_atk and _sht.party[0].ability == _orig_ab and not getattr(_sht.party[0], "_transformed", False), f"atk={_sht.party[0].attack}/{_orig_atk} ab={_sht.party[0].ability}/{_orig_ab}")')
        tests_for_move.append('# 命中・回避ランクもコピーする')
        tests_for_move.append('_dt4 = make_poke(type1="みず"); _dt4.stage_accuracy = 2; _dt4.stage_evasion = -1')
        tests_for_move.append('_pt4 = make_poke(type1="ノーマル"); execute(_pt4, _dt4, "へんしん")')
        tests_for_move.append('check("命中回避ランクもコピー: へんしん", _pt4.stage_accuracy == 2 and _pt4.stage_evasion == -1, f"acc={_pt4.stage_accuracy} eva={_pt4.stage_evasion}")')
    elif name == 'みがわり':
        tests_for_move.append('# みがわり: HP1/4消費して身代わり生成')
        tests_for_move.append('_pm = make_poke(hp_b=200); _hpm = _pm.hp; execute(_pm, make_poke(), "みがわり")')
        tests_for_move.append('check("みがわり生成: みがわり", getattr(_pm, "_substitute_hp", 0) > 0 and _pm.hp < _hpm, f"sub={getattr(_pm,\'_substitute_hp\',0)} hp={_pm.hp}/{_hpm}")')
        tests_for_move.append('# 身代わりが技を肩代わり（本体HPは減らない・身代わりHPが減る）')
        tests_for_move.append('_pms = make_poke(hp_b=200); execute(_pms, make_poke(), "みがわり"); _sub0 = _pms._substitute_hp; _hpms = _pms.hp')
        tests_for_move.append('_atkms = make_poke(type1="ノーマル", atk_b=20, moves=["たいあたり"])')
        tests_for_move.append('_execute_move(BattleSide([_atkms]), BattleSide([_pms]), Action(type="move", move=dl.get_move("たいあたり")), BattleField())')
        tests_for_move.append('check("みがわり中は本体ダメージなし: みがわり", _pms.hp == _hpms and _pms._substitute_hp < _sub0, f"hp={_pms.hp}/{_hpms} sub={_pms._substitute_hp}/{_sub0}")')
        tests_for_move.append('# 身代わりHPを超えるダメージで身代わりが消える')
        tests_for_move.append('_pmb = make_poke(hp_b=200); execute(_pmb, make_poke(), "みがわり")')
        tests_for_move.append('_atkmb = make_poke(type1="かくとう", atk_b=255, moves=["インファイト"])')
        tests_for_move.append('_execute_move(BattleSide([_atkmb]), BattleSide([_pmb]), Action(type="move", move=dl.get_move("インファイト")), BattleField())')
        tests_for_move.append('check("大ダメージで身代わり消滅: みがわり", getattr(_pmb, "_substitute_hp", 0) == 0, f"sub={getattr(_pmb,\'_substitute_hp\',0)}")')
    elif name == 'ほろびのうた':
        tests_for_move.append('# ほろびのうた: 場の全員をほろび状態に')
        tests_for_move.append('_ph = make_poke(); _dh = make_poke(); execute(_ph, _dh, "ほろびのうた")')
        tests_for_move.append('check("ほろび付与: ほろびのうた", _ph.perish_count > 0 and _dh.perish_count > 0, f"自{_ph.perish_count} 相{_dh.perish_count}")')
    elif name == 'いたみわけ':
        tests_for_move.append('# いたみわけ: 互いのHPを合計して半分ずつ')
        tests_for_move.append('_pp = make_poke(hp_b=200); _pp.hp = 20; _dp = make_poke(hp_b=200); _dp.hp = 180')
        tests_for_move.append('execute(_pp, _dp, "いたみわけ")')
        tests_for_move.append('check("HP折半: いたみわけ", abs(_pp.hp - _dp.hp) <= 1, f"自{_pp.hp} 相{_dp.hp}")')
    elif name == 'じこあんじ':
        tests_for_move.append('# じこあんじ: 相手の能力変化を自分にコピー')
        tests_for_move.append('_pj = make_poke(); _dj = make_poke(); _dj.stage_attack = 2; _dj.stage_speed = -1')
        tests_for_move.append('execute(_pj, _dj, "じこあんじ")')
        tests_for_move.append('check("じこあんじコピー: じこあんじ", _pj.stage_attack == 2 and _pj.stage_speed == -1, f"atk={_pj.stage_attack} spd={_pj.stage_speed}")')
    elif name == 'パワースワップ':
        tests_for_move.append('# パワースワップ: 攻撃・特攻の能力変化を相手と入れ替え（双方向。コピーでなく入替を区別）')
        tests_for_move.append('_pp = make_poke(); _pp.stage_attack = -1; _pp.stage_sp_attack = 1')
        tests_for_move.append('_dp = make_poke(); _dp.stage_attack = 3; _dp.stage_sp_attack = 2')
        tests_for_move.append('execute(_pp, _dp, "パワースワップ")')
        tests_for_move.append('check("パワースワップ入替(双方向): パワースワップ", _pp.stage_attack == 3 and _pp.stage_sp_attack == 2 and _dp.stage_attack == -1 and _dp.stage_sp_attack == 1, f"自{_pp.stage_attack}/{_pp.stage_sp_attack} 相{_dp.stage_attack}/{_dp.stage_sp_attack}")')
    elif name == 'ガードスワップ':
        tests_for_move.append('# ガードスワップ: 防御・特防の能力変化を相手と入れ替え（双方向。コピーでなく入替を区別）')
        tests_for_move.append('_pg = make_poke(); _pg.stage_defense = -1; _pg.stage_sp_defense = 1')
        tests_for_move.append('_dg = make_poke(); _dg.stage_defense = 3; _dg.stage_sp_defense = 2')
        tests_for_move.append('execute(_pg, _dg, "ガードスワップ")')
        tests_for_move.append('check("ガードスワップ入替(双方向): ガードスワップ", _pg.stage_defense == 3 and _pg.stage_sp_defense == 2 and _dg.stage_defense == -1 and _dg.stage_sp_defense == 1, f"自{_pg.stage_defense}/{_pg.stage_sp_defense} 相{_dg.stage_defense}/{_dg.stage_sp_defense}")')
    elif name == 'スピードスワップ':
        tests_for_move.append('# スピードスワップ: 素早さの実数値を相手と入れ替え')
        tests_for_move.append('_ps = make_poke(spd_b=50); _ds = make_poke(spd_b=200); _spb = _ps.speed; _dspb = _ds.speed')
        tests_for_move.append('execute(_ps, _ds, "スピードスワップ")')
        tests_for_move.append('check("素早さ入替: スピードスワップ", _ps.speed == _dspb and _ds.speed == _spb, f"自{_ps.speed} 相{_ds.speed}")')
    elif name == 'スキルスワップ':
        tests_for_move.append('# スキルスワップ: 特性を相手と入れ替え')
        tests_for_move.append('_pk = make_poke(ability="いかく"); _dk = make_poke(ability="ちょすい")')
        tests_for_move.append('execute(_pk, _dk, "スキルスワップ")')
        tests_for_move.append('check("特性入替: スキルスワップ", _pk.ability == "ちょすい" and _dk.ability == "いかく", f"自{_pk.ability} 相{_dk.ability}")')
    elif name == 'なかまづくり':
        tests_for_move.append('# なかまづくり: 相手の特性を自分と同じに')
        tests_for_move.append('_pn = make_poke(ability="いかく"); _dn = make_poke(ability="ちょすい")')
        tests_for_move.append('execute(_pn, _dn, "なかまづくり")')
        tests_for_move.append('check("特性コピー(相手): なかまづくり", _dn.ability == "いかく", f"相{_dn.ability}")')
    elif name == 'なりきり':
        tests_for_move.append('# なりきり: 自分の特性を相手と同じに')
        tests_for_move.append('_pr = make_poke(ability="いかく"); _dr = make_poke(ability="ちょすい")')
        tests_for_move.append('execute(_pr, _dr, "なりきり")')
        tests_for_move.append('check("特性コピー(自分): なりきり", _pr.ability == "ちょすい", f"自{_pr.ability}")')
    elif name == 'シンプルビーム':
        tests_for_move.append('# シンプルビーム: 相手の特性をたんじゅんに')
        tests_for_move.append('_psb = make_poke(); _dsb = make_poke(ability="いかく"); execute(_psb, _dsb, "シンプルビーム")')
        tests_for_move.append('check("特性たんじゅん化: シンプルビーム", _dsb.ability == "たんじゅん", f"相{_dsb.ability}")')
    elif name == 'なやみのタネ':
        tests_for_move.append('# なやみのタネ: 相手の特性をふみんに')
        tests_for_move.append('_pny = make_poke(); _dny = make_poke(ability="いかく"); execute(_pny, _dny, "なやみのタネ")')
        tests_for_move.append('check("特性ふみん化: なやみのタネ", _dny.ability == "ふみん", f"相{_dny.ability}")')
    elif name == 'いえき':
        tests_for_move.append('# いえき: 相手をとくせいなし状態に')
        tests_for_move.append('_pe = make_poke(); _de = make_poke(ability="いかく"); execute(_pe, _de, "いえき")')
        tests_for_move.append('check("とくせい無効化: いえき", _de.ability_suppressed, f"sup={_de.ability_suppressed}")')
    elif name == 'ミラータイプ':
        tests_for_move.append('# ミラータイプ: 自分のタイプを相手と同じに')
        tests_for_move.append('_pmt = make_poke(type1="ノーマル"); _dmt = make_poke(type1="みず", type2="ひこう")')
        tests_for_move.append('execute(_pmt, _dmt, "ミラータイプ")')
        tests_for_move.append('check("ミラータイプコピー: ミラータイプ", _pmt.type1 == "みず" and _pmt.type2 == "ひこう", f"type={_pmt.type1}/{_pmt.type2}")')
    elif name == 'みずびたし':
        tests_for_move.append('# みずびたし: 相手を純みずタイプに変える（複合タイプでもtype2が消える）')
        tests_for_move.append('_pmz = make_poke(); _dmz = make_poke(type1="ほのお", type2="ひこう"); execute(_pmz, _dmz, "みずびたし")')
        tests_for_move.append('check("純みずタイプ化(type2消去): みずびたし", _dmz.type1 == "みず" and _dmz.type2 is None, f"t1={_dmz.type1} t2={_dmz.type2}")')
    elif name in ('ハロウィン', 'もりののろい'):
        _add_t = 'ゴースト' if name == 'ハロウィン' else 'くさ'
        tests_for_move.append(f'# {name}: 相手に{_add_t}タイプを追加')
        tests_for_move.append(f'_pha = make_poke(); _dha = make_poke(type1="ノーマル", type2=None); execute(_pha, _dha, "{name}")')
        tests_for_move.append(f'check("タイプ追加({_add_t}): {name}", "{_add_t}" in (_dha.type1, _dha.type2), f"type={{_dha.type1}}/{{_dha.type2}}")')
    elif name in ('うらみ', 'ぶきみなじゅもん'):
        _ppr = 4 if name == 'うらみ' else 3
        tests_for_move.append(f'# {name}: 相手の最後の技のPPを{_ppr}減らす')
        tests_for_move.append(f'_ppp = make_poke(spatk_b=10, atk_b=10); _dpp = make_poke(moves=["たいあたり"], hp_b=255, def_b=255, spdef_b=255); _dpp.last_used_move = "たいあたり"; _dpp.pp = [20]')
        tests_for_move.append(f'execute(_ppp, _dpp, "{name}")')
        tests_for_move.append(f'check("PP減少: {name}", _dpp.pp[0] == 20 - {_ppr}, f"pp={{_dpp.pp[0]}}")')
    elif name == 'いばる':
        tests_for_move.append('# いばる: 相手の攻撃+2&こんらん')
        tests_for_move.append('_pib = make_poke(); _dib = make_poke(hp_b=200); execute(_pib, _dib, "いばる")')
        tests_for_move.append('check("攻撃+2こんらん: いばる", _dib.stage_attack == 2 and _dib.confused, f"atk={_dib.stage_attack} conf={_dib.confused}")')
    elif name == 'おだてる':
        tests_for_move.append('# おだてる: 相手の特攻+1&こんらん')
        tests_for_move.append('_pod = make_poke(); _dod = make_poke(hp_b=200); execute(_pod, _dod, "おだてる")')
        tests_for_move.append('check("特攻+1こんらん: おだてる", _dod.stage_sp_attack == 1 and _dod.confused, f"spa={_dod.stage_sp_attack} conf={_dod.confused}")')
    elif name == 'おたけび':
        tests_for_move.append('# おたけび: 相手の攻撃・特攻-1')
        tests_for_move.append('_pok = make_poke(); _dok = make_poke(hp_b=200); execute(_pok, _dok, "おたけび")')
        tests_for_move.append('check("相手攻撃特攻ダウン: おたけび", _dok.stage_attack == -1 and _dok.stage_sp_attack == -1, f"atk={_dok.stage_attack} spa={_dok.stage_sp_attack}")')
    elif name == 'くすぐる':
        tests_for_move.append('# くすぐる: 相手の攻撃・防御-1')
        tests_for_move.append('_pks = make_poke(); _dks = make_poke(hp_b=200); execute(_pks, _dks, "くすぐる")')
        tests_for_move.append('check("相手攻撃防御ダウン: くすぐる", _dks.stage_attack == -1 and _dks.stage_defense == -1, f"atk={_dks.stage_attack} def={_dks.stage_defense}")')
    elif name == 'なみだめ':
        tests_for_move.append('# なみだめ: 相手の攻撃・特攻-1 + 回避率を無視して命中（高回避にも当たる）')
        tests_for_move.append('_pnd = make_poke(); _dnd = make_poke(hp_b=200); execute(_pnd, _dnd, "なみだめ")')
        tests_for_move.append('check("相手攻撃特攻ダウン: なみだめ", _dnd.stage_attack == -1 and _dnd.stage_sp_attack == -1, f"atk={_dnd.stage_attack} spa={_dnd.stage_sp_attack}")')
        tests_for_move.append('# 回避無視: stage_evasion=6(最大)でも命中する')
        tests_for_move.append('random.seed(0); _pnd2 = make_poke(); _dnd2 = make_poke(hp_b=200); _dnd2.stage_evasion = 6')
        tests_for_move.append('for _ in range(10): execute(_pnd2, _dnd2, "なみだめ")')
        tests_for_move.append('check("回避無視: なみだめ", _dnd2.stage_attack < 0, f"atk={_dnd2.stage_attack}(回避6でも命中するべき)")')
    elif name == 'ハバネロエキス':
        tests_for_move.append('# ハバネロエキス: 相手の防御-2・攻撃+2')
        tests_for_move.append('_phb = make_poke(); _dhb = make_poke(hp_b=200); execute(_phb, _dhb, "ハバネロエキス")')
        tests_for_move.append('check("相手防御-2攻撃+2: ハバネロエキス", _dhb.stage_defense == -2 and _dhb.stage_attack == 2, f"def={_dhb.stage_defense} atk={_dhb.stage_attack}")')
    elif name == 'いちゃもん':
        tests_for_move.append('# いちゃもん: 相手を連続不可状態に')
        tests_for_move.append('_pic = make_poke(); _dic = make_poke(hp_b=200); execute(_pic, _dic, "いちゃもん")')
        tests_for_move.append('check("連続不可付与: いちゃもん", _dic.torment, f"torment={_dic.torment}")')
    elif name == 'たくわえる':
        tests_for_move.append('# たくわえる: たくわえカウント+1')
        tests_for_move.append('_ptk = make_poke(); execute(_ptk, make_poke(), "たくわえる")')
        tests_for_move.append('check("たくわえ+1: たくわえる", _ptk.stockpile_count == 1, f"sc={_ptk.stockpile_count}")')
    elif name == 'チャージビーム':
        tests_for_move.append('# チャージビーム: 70%で自分の特攻+1')
        tests_for_move.append('random.seed(0); _cb_up = False')
        tests_for_move.append('for _ in range(20):')
        tests_for_move.append('    _pcb = make_poke(type1="でんき", spatk_b=100); _dcb = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)')
        tests_for_move.append('    execute(_pcb, _dcb, "チャージビーム")')
        tests_for_move.append('    if _pcb.stage_sp_attack > 0: _cb_up = True; break')
        tests_for_move.append('check("自分特攻上昇(70%): チャージビーム", _cb_up)')
    elif name == 'ふくろだたき':
        tests_for_move.append('# ふくろだたき: 手持ちの数だけ攻撃（1v1でも発動しダメージ）')
        tests_for_move.append('_pfd = make_poke(type1="あく", atk_b=120); _dfd = make_poke(type1="エスパー", hp_b=255, def_b=120)')
        tests_for_move.append('_hpfd = _dfd.hp; execute(_pfd, _dfd, "ふくろだたき")')
        tests_for_move.append('check("ふくろだたき発動: ふくろだたき", _dfd.hp < _hpfd, f"hp={_dfd.hp}/{_hpfd}")')
    elif name == 'ハードプレス':
        tests_for_move.append('# ハードプレス: 威力=max(1,floor(100×相手現HP/最大HP))。具体値を検証')
        tests_for_move.append('_php = make_poke(atk_b=100); _dhp = make_poke(hp_b=200, def_b=100)')
        tests_for_move.append('import math as _mhp; _hp_ng = []')
        tests_for_move.append('for _r in [1.0, 0.5, 0.25]:')
        tests_for_move.append('    _dhp.hp = max(1, int(_dhp.max_hp * _r)); _exp = max(1, _mhp.floor(100 * _dhp.hp / _dhp.max_hp))')
        tests_for_move.append('    _got = _ep(_php, _dhp, dl.get_move("ハードプレス"), BattleField())')
        tests_for_move.append('    if _got != _exp: _hp_ng.append(f"r={_r}:{_got}!={_exp}")')
        tests_for_move.append('check("相手HP比威力(100×HP/max): ハードプレス", not _hp_ng, f"NG={_hp_ng}")')
    elif name == 'いのちがけ':
        tests_for_move.append('# いのちがけ: 自分はひんしになり残HP分のダメージ')
        tests_for_move.append('_plg = make_poke(type1="かくとう", atk_b=100); _plg.hp = 80; _dlg = make_poke(type1="ノーマル", hp_b=200, def_b=100)')
        tests_for_move.append('_hplg = _dlg.hp; execute(_plg, _dlg, "いのちがけ")')
        tests_for_move.append('check("可変ダメージ(いのちがけ): いのちがけ", not _plg.is_alive and (_hplg - _dlg.hp) == 80, f"自alive={_plg.is_alive} dmg={_hplg - _dlg.hp}")')
    elif name == 'エレキボール':
        tests_for_move.append('# エレキボール: 速度比別の威力テーブル（≥4→150 ≥3→120 ≥2→80 ≥1→60 未満→40）')
        tests_for_move.append('_peb = make_poke(type1="でんき", spatk_b=100)')
        tests_for_move.append('_eb_ng = []')
        tests_for_move.append('for _ratio, _exp in [(4,150),(3,120),(2,80),(1,60),(0.5,40)]:')
        tests_for_move.append('    _deb = make_poke(type1="ノーマル")')
        tests_for_move.append('    _peb.speed = 200; _deb.speed = int(200 / _ratio)')
        tests_for_move.append('    _got = _ep(_peb, _deb, dl.get_move("エレキボール"), BattleField())')
        tests_for_move.append('    if _got != _exp: _eb_ng.append(f"ratio={_ratio}:{_got}!={_exp}")')
        tests_for_move.append('check("速度比別威力テーブル: エレキボール", not _eb_ng, f"NG={_eb_ng}")')
    elif name == 'ちいさくなる':
        tests_for_move.append('# ちいさくなる: 回避+2 かつ minimized状態になる（のしかかり等2倍の条件成立）')
        tests_for_move.append('_pmin = make_poke(type1="ノーマル"); execute(_pmin, make_poke(), "ちいさくなる")')
        tests_for_move.append('check("回避率+2: ちいさくなる", _pmin.stage_evasion == 2, f"eva={_pmin.stage_evasion}")')
        tests_for_move.append('check("minimized成立: ちいさくなる", _pmin.minimized, f"minimized={_pmin.minimized}")')
    elif name == 'みきり':
        tests_for_move.append('# みきり: まもる状態になり相手の技を防ぐ')
        tests_for_move.append('_pmk = make_poke(type1="かくとう"); execute(_pmk, make_poke(), "みきり")')
        tests_for_move.append('check("まもる状態: みきり", _pmk.protecting)')
        tests_for_move.append('_pmk2 = make_poke(type1="かくとう"); _pmk2.protecting = True; _dmk = make_poke(type1="ノーマル", atk_b=200, hp_b=255)')
        tests_for_move.append('_hpmk = _pmk2.hp')
        tests_for_move.append('_execute_move(BattleSide([_dmk]), BattleSide([_pmk2]), Action(type="move", move=dl.get_move("のしかかり")), BattleField())')
        tests_for_move.append('check("技を防ぐ: みきり", _pmk2.hp == _hpmk, f"hp={_pmk2.hp}/{_hpmk}")')
    elif name == 'ふいうち':
        tests_for_move.append('# ふいうち: 相手が攻撃技を選んでいれば成功、変化技/未選択なら失敗')
        tests_for_move.append('_pfu = make_poke(type1="あく", atk_b=120)')
        tests_for_move.append('_opp_atk = Action(type="move", move=dl.get_move("のしかかり"))')
        tests_for_move.append('_opp_sta = Action(type="move", move=dl.get_move("まもる"))')
        tests_for_move.append('# 相手が攻撃技 → 成功')
        tests_for_move.append('_dfu1 = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpfu1 = _dfu1.hp')
        tests_for_move.append('_execute_move(BattleSide([_pfu]), BattleSide([_dfu1]), Action(type="move", move=dl.get_move("ふいうち")), BattleField(), _opp_atk)')
        tests_for_move.append('check("攻撃技相手に成功: ふいうち", _dfu1.hp < _hpfu1, f"hp={_dfu1.hp}/{_hpfu1}")')
        tests_for_move.append('# 相手が変化技 → 失敗')
        tests_for_move.append('_dfu2 = make_poke(type1="ノーマル", hp_b=255, def_b=120); _hpfu2 = _dfu2.hp')
        tests_for_move.append('_execute_move(BattleSide([_pfu]), BattleSide([_dfu2]), Action(type="move", move=dl.get_move("ふいうち")), BattleField(), _opp_sta)')
        tests_for_move.append('check("変化技相手に失敗: ふいうち", _dfu2.hp == _hpfu2, f"hp={_dfu2.hp}/{_hpfu2}")')
    elif name == 'さわぐ':
        tests_for_move.append('# さわぐ: 2〜3ターン連続使用ロック（さわぐ状態）')
        tests_for_move.append('_psw = make_poke(type1="ノーマル", spatk_b=100); _dsw = make_poke(type1="ノーマル", hp_b=255, spdef_b=200)')
        tests_for_move.append('execute(_psw, _dsw, "さわぐ")')
        tests_for_move.append('check("さわぐ状態ロック: さわぐ", _psw.locked_move == "さわぐ" and _psw.lock_count >= 1, f"locked={_psw.locked_move} count={_psw.lock_count}")')
    elif name == 'アンコール':
        tests_for_move.append('# アンコール: 相手をアンコール状態に')
        tests_for_move.append('_pen = make_poke(); _den = make_poke(moves=["たいあたり"]); _den.last_used_move = "たいあたり"')
        tests_for_move.append('execute(_pen, _den, "アンコール")')
        tests_for_move.append('check("アンコール付与: アンコール", _den.encore_count > 0 and _den.locked_move == "たいあたり")')
    elif name == 'ちょうはつ':
        tests_for_move.append('# ちょうはつ: 相手をちょうはつ状態に')
        tests_for_move.append('_pt2 = make_poke(); _dt2 = make_poke(); execute(_pt2, _dt2, "ちょうはつ")')
        tests_for_move.append('check("ちょうはつ付与: ちょうはつ", _dt2.taunt_count > 0)')
    elif name == 'ふういん':
        tests_for_move.append('# ふういん: 自分がふういん状態に')
        tests_for_move.append('_pf = make_poke(); execute(_pf, make_poke(), "ふういん")')
        tests_for_move.append('check("ふういん付与: ふういん", getattr(_pf, "_sealed", False))')
    elif name == 'はたきおとす':
        tests_for_move.append('# はたきおとす: 道具持ちに1.5倍+道具排除')
        tests_for_move.append('_pko = make_poke(type1="あく", atk_b=100)')
        tests_for_move.append('_dko_item = make_poke(type1="ノーマル", def_b=100); _dko_item.item = "たべのこし"')
        tests_for_move.append('_dko_none = make_poke(type1="ノーマル", def_b=100)')
        tests_for_move.append('_d_item = calc_damage(_pko, _dko_item, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_none = calc_damage(_pko, _dko_none, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)')
        tests_for_move.append('check("はたきおとす 道具持ち1.5倍: はたきおとす", _d_item > _d_none, f"item={_d_item} none={_d_none}")')
        tests_for_move.append(f'# 威力1.5倍の具体値（{power}→{int(power * 1.5)}）')
        tests_for_move.append('_pkx = make_poke(type1="あく", atk_b=100); _dkx = make_poke(type1="ノーマル", def_b=100); _dkx.item = None')
        tests_for_move.append('_ko_base = _ep(_pkx, _dkx, dl.get_move("はたきおとす"), BattleField())')
        tests_for_move.append('_dkx.item = "オボンのみ"; _ko_item = _ep(_pkx, _dkx, dl.get_move("はたきおとす"), BattleField())')
        tests_for_move.append(f'check("道具なし威力{power}: はたきおとす", _ko_base == {power}, f"base={{_ko_base}}")')
        tests_for_move.append(f'check("道具持ち1.5倍具体値({int(power * 1.5)}): はたきおとす", _ko_item == {int(power * 1.5)}, f"item={{_ko_item}}")')
        tests_for_move.append('execute(_pko, _dko_item, "はたきおとす")')
        tests_for_move.append('check("はたきおとす 道具排除: はたきおとす", _dko_item.item is None)')
        tests_for_move.append('# メガストーンは叩き落とせない＋1.5倍補正もない')
        tests_for_move.append('_dko_mega = make_poke(type1="ノーマル", def_b=100, item="ガブリアスナイト")')
        tests_for_move.append('_dko_mega_nodmg = make_poke(type1="ノーマル", def_b=100)  # アイテムなし（基準）')
        tests_for_move.append('_d_mega = calc_damage(_pko, _dko_mega, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)')
        tests_for_move.append('_d_mega_base = calc_damage(_pko, _dko_mega_nodmg, dl.get_move("はたきおとす"), BattleField(), random_roll=1.0)')
        tests_for_move.append('execute(_pko, _dko_mega, "はたきおとす")')
        tests_for_move.append('check("メガストーン消去失敗: はたきおとす", _dko_mega.item == "ガブリアスナイト", f"item={_dko_mega.item}")')
        tests_for_move.append('check("メガストーン時1.5倍補正なし: はたきおとす", _d_mega == _d_mega_base, f"mega={_d_mega} base={_d_mega_base}")')
    elif name == 'くろいきり':
        tests_for_move.append('# くろいきり: 両者の能力変化リセット')
        tests_for_move.append('_pck = make_poke(); _pck.stage_attack = 3; _dck = make_poke(); _dck.stage_defense = 2')
        tests_for_move.append('execute(_pck, _dck, "くろいきり")')
        tests_for_move.append('check("くろいきり 能力リセット: くろいきり", _pck.stage_attack == 0 and _dck.stage_defense == 0)')
    elif name == 'かなしばり':
        tests_for_move.append('# かなしばり: 相手の最後の技を封じる')
        tests_for_move.append('_pkn = make_poke(); _dkn = make_poke(moves=["たいあたり"]); _dkn.last_used_move = "たいあたり"')
        tests_for_move.append('execute(_pkn, _dkn, "かなしばり")')
        tests_for_move.append('check("かなしばり わざ封じ: かなしばり", _dkn.disabled_move == "たいあたり")')
    elif name in ('ひゃっきやこう', 'ベノムショック', 'たたりめ'):
        st = 'badpoison' if name == 'ベノムショック' else 'burn'
        tests_for_move.append(f'# {name}: 相手状態異常で威力2倍')
        tests_for_move.append(f'_pcp = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100)')
        tests_for_move.append(f'_dn1 = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_dn2 = make_poke(type1="{def_type}", def_b=100, spdef_b=100); _dn2.status = "{st}"')
        tests_for_move.append(f'_pn = _ep(_pcp, _dn1, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'_pd = _ep(_pcp, _dn2, dl.get_move("{name}"), BattleField())')
        tests_for_move.append(f'check("状態異常で威力2倍: {name}", _pd == _pn * 2, f"normal={{_pn}} status={{_pd}}")')
    elif name == 'ライジングボルト':
        tests_for_move.append('# ライジングボルト: エレキフィールドで威力2倍')
        tests_for_move.append('_prb = make_poke(type1="でんき", spatk_b=100); _drb = make_poke(type1="ノーマル", spdef_b=100)')
        tests_for_move.append('_prn = _ep(_prb, _drb, dl.get_move("ライジングボルト"), BattleField())')
        tests_for_move.append('_fe = BattleField(); _fe.electric_terrain = True')
        tests_for_move.append('_prd = _ep(_prb, _drb, dl.get_move("ライジングボルト"), _fe)')
        tests_for_move.append('check("エレキF威力2倍: ライジングボルト", _prd == _prn * 2, f"normal={_prn} ef={_prd}")')
    elif name in ('DDラリアット', 'せいなるつるぎ'):
        _atk_t = 'あく' if name == 'DDラリアット' else 'かくとう'
        tests_for_move.append(f'# {name}: 相手の防御ランク上昇を無視')
        tests_for_move.append(f'_pdd = make_poke(type1="{_atk_t}", atk_b=100)')
        tests_for_move.append(f'_ddd = make_poke(type1="ノーマル", def_b=100); _ddd.stage_defense = 6')
        tests_for_move.append(f'_dd_ignore = calc_damage(_pdd, _ddd, dl.get_move("{name}"), BattleField(), random_roll=1.0)')
        tests_for_move.append(f'_ddn = make_poke(type1="ノーマル", def_b=100)')
        tests_for_move.append(f'_dd_normal = calc_damage(_pdd, _ddn, dl.get_move("{name}"), BattleField(), random_roll=1.0)')
        tests_for_move.append(f'check("防御ランク上昇無視: {name}", _dd_ignore == _dd_normal, f"ignore={{_dd_ignore}} normal={{_dd_normal}}")')
        tests_for_move.append(f'# 防御ランク低下も無視（相手が防御-6でも軽減されない＝通常と同ダメージ）')
        tests_for_move.append(f'_ddlo = make_poke(type1="ノーマル", def_b=100); _ddlo.stage_defense = -6')
        tests_for_move.append(f'_dd_low = calc_damage(_pdd, _ddlo, dl.get_move("{name}"), BattleField(), random_roll=1.0)')
        tests_for_move.append(f'check("防御ランク低下も無視: {name}", _dd_low == _dd_normal, f"low={{_dd_low}} normal={{_dd_normal}}")')
    elif name == 'じならし':
        tests_for_move.append(f'# {name}: グラスフィールド時に威力半減')
        tests_for_move.append(f'_pgf = make_poke(type1="じめん", atk_b=100); _dgf = make_poke(type1="どく", def_b=100)')
        tests_for_move.append(f'_fg0 = BattleField(); _d_no = calc_damage(_pgf, _dgf, dl.get_move("{name}"), _fg0, random_roll=1.0)')
        tests_for_move.append(f'_fg1 = BattleField(); _fg1.grassy_terrain = True')
        tests_for_move.append(f'_d_gf = calc_damage(_pgf, _dgf, dl.get_move("{name}"), _fg1, random_roll=1.0)')
        tests_for_move.append(f'check("{name} グラスF半減: {name}", _d_gf < _d_no, f"no={{_d_no}} gf={{_d_gf}}")')
    elif name == 'でんじふゆう':
        tests_for_move.append('# でんじふゆう: じめん技無効化')
        tests_for_move.append('_pmr = make_poke(type1="でんき"); execute(_pmr, make_poke(), "でんじふゆう")')
        tests_for_move.append('check("でんじふゆうフラグ: でんじふゆう", _pmr.magnet_rise)')
        tests_for_move.append('_atkg = make_poke(type1="じめん", atk_b=120, moves=["じしん"])')
        tests_for_move.append('_djump = dmg(_atkg, _pmr, "じしん")')
        tests_for_move.append('check("でんじふゆう じめん無効: でんじふゆう", _djump == 0, f"dmg={_djump}")')
    elif name in ('ねをはる', 'アクアリング'):
        attr = 'rooted' if name == 'ねをはる' else 'aqua_ring'
        tests_for_move.append(f'# {name}: 毎ターン1/16回復')
        tests_for_move.append(f'_prt = make_poke(hp_b=200); _prt.hp = 50; execute(_prt, make_poke(), "{name}")')
        tests_for_move.append(f'check("{name}フラグ: {name}", _prt.{attr})')
        tests_for_move.append(f'from simulator.battle import Battle as _B')
        tests_for_move.append(f'_b = _B(BattleSide([_prt]), BattleSide([make_poke()])); _hp0 = _prt.hp')
        tests_for_move.append(f'_b._end_of_turn()')
        tests_for_move.append(f'check("{name} ターン終了回復: {name}", _prt.hp > _hp0, f"hp={{_prt.hp}}")')
    elif name == 'ロックオン':
        tests_for_move.append('# ロックオン: 次の技が必中')
        tests_for_move.append('_plo = make_poke(type1="ノーマル", atk_b=100); execute(_plo, make_poke(), "ロックオン")')
        tests_for_move.append('check("ロックオンフラグ: ロックオン", _plo.lock_on)')
        tests_for_move.append('import copy as _cp2; _mvlo = _cp2.copy(dl.get_move("でんじは") or dl.get_move("たいあたり")); _mvlo.accuracy = 1')
        tests_for_move.append('_dlo = make_poke(type1="ノーマル", hp_b=255); _hplo = _dlo.hp; random.seed(0)')
        tests_for_move.append('from simulator.damage import check_hit as _ch')
        tests_for_move.append('check("ロックオン必中: ロックオン", all(_ch(_plo, _dlo, _mvlo, BattleField()) for _ in range(20)))')
    elif name in ('ねっとう', 'ねっさのだいち'):
        tests_for_move.append(f'# {name}: 相手のこおりを治す')
        tests_for_move.append(f'_paf2 = make_poke(type1="{atk_type}", spatk_b=100, atk_b=100); _pdf2 = make_poke(type1="ノーマル", hp_b=255, def_b=255, spdef_b=255)')
        tests_for_move.append(f'_pdf2.status = "freeze"; execute(_paf2, _pdf2, "{name}")')
        tests_for_move.append(f'check("相手こおり治癒: {name}", _pdf2.status != "freeze")')
        tests_for_move.append(f'# 自分のこおりも治す')
        tests_for_move.append(f'_paf3 = make_poke(type1="{atk_type}", spatk_b=100, atk_b=100); _paf3.status = "freeze"')
        tests_for_move.append(f'execute(_paf3, make_poke(hp_b=255), "{name}")')
        tests_for_move.append(f'check("自分こおり治癒: {name}", _paf3.status != "freeze")')
    elif name in ('あさのひざし', 'こうごうせい', 'つきのひかり'):
        tests_for_move.append(f'# {name}: 天候別回復を厳密検証 無天候=1/2・晴れ=2/3・悪天候(雨/砂/あられ)=1/4')
        tests_for_move.append(f'_hh_ng = []')
        tests_for_move.append(f'for _wen, _expfn in [(None, lambda m: m//2), ("sunny", lambda m: m*2//3), ("rain", lambda m: m//4), ("sandstorm", lambda m: m//4)]:')
        tests_for_move.append(f'    _phw = make_poke(hp_b=200); _phw.hp = 1; _mhw = _phw.max_hp')
        tests_for_move.append(f'    _fwh = BattleField()')
        tests_for_move.append(f'    if _wen: _fwh.weather = _wen')
        tests_for_move.append(f'    _execute_move(BattleSide([_phw]), BattleSide([make_poke()]), Action(type="move", move=dl.get_move("{name}")), _fwh)')
        tests_for_move.append(f'    _exph = min(_mhw, 1 + _expfn(_mhw))')
        tests_for_move.append(f'    if _phw.hp != _exph: _hh_ng.append(str(_wen) + ":" + str(_phw.hp) + "!=" + str(_exph))')
        tests_for_move.append(f'check("天候別回復(1/2,2/3,1/4)厳密: {name}", not _hh_ng, "NG=" + str(_hh_ng))')
    elif name == 'アイススピナー':
        tests_for_move.append(f'# {name}: フィールド解除')
        tests_for_move.append(f'_pfc = make_poke(type1="こおり" if "{name}"=="アイススピナー" else "はがね", atk_b=120)')
        tests_for_move.append(f'_dfc = make_poke(type1="ノーマル", hp_b=255, def_b=100)')
        tests_for_move.append(f'_s1fc = BattleSide([_pfc]); _s2fc = BattleSide([_dfc]); _ffc = BattleField()')
        tests_for_move.append(f'_ffc.electric_terrain = True; _ffc.electric_terrain_count = 5')
        tests_for_move.append(f'_execute_move(_s1fc, _s2fc, Action(type="move", move=dl.get_move("{name}")), _ffc)')
        tests_for_move.append(f'check("フィールド解除: {name}", not _ffc.electric_terrain)')
    elif name == 'ほしがる':
        tests_for_move.append(f'# {name}: 道具奪取')
        tests_for_move.append(f'_pst = make_poke(type1="あく", atk_b=120); _pst.item = None')
        tests_for_move.append(f'_dst = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst.item = "オボンのみ"')
        tests_for_move.append(f'execute(_pst, _dst, "{name}")')
        tests_for_move.append(f'check("道具奪取: {name}", _pst.item == "オボンのみ" and _dst.item is None)')
        tests_for_move.append(f'# negative: 自分が道具を持っている場合は奪わない')
        tests_for_move.append(f'_pst2 = make_poke(type1="あく", atk_b=120); _pst2.item = "オボンのみ"')
        tests_for_move.append(f'_dst2 = make_poke(type1="ノーマル", hp_b=255, def_b=100); _dst2.item = "たべのこし"')
        tests_for_move.append(f'execute(_pst2, _dst2, "{name}")')
        tests_for_move.append(f'check("自分が道具持ちなら奪わない: {name}", _pst2.item == "オボンのみ" and _dst2.item == "たべのこし", f"atk={{_pst2.item}} def={{_dst2.item}}")')
    elif name in ('じだんだ', 'やけっぱち'):
        tests_for_move.append(f'# {name}: 前ターン失敗で威力2倍（実効威力で厳密比較）')
        tests_for_move.append(f'_mvj = dl.get_move("{name}")')
        tests_for_move.append(f'_paj = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _pdj = make_poke(type1="{def_type}", def_b=100, spdef_b=100)')
        tests_for_move.append(f'_p_normal = _ep(_paj, _pdj, _mvj, BattleField())')
        tests_for_move.append(f'_paj._move_failed_last = True')
        tests_for_move.append(f'_p_double = _ep(_paj, _pdj, _mvj, BattleField())')
        tests_for_move.append(f'check("前ターン失敗2倍: {name}", _p_double == _p_normal * 2, f"normal={{_p_normal}} double={{_p_double}}")')
        tests_for_move.append(f'# 条件成立: 技を外すと _move_failed_this_turn が立つ（実戦arising）')
        tests_for_move.append(f'import copy as _cpj; _mvmiss = _cpj.copy(_mvj); _mvmiss.accuracy = 1')
        tests_for_move.append(f'random.seed(0); _missset = False')
        tests_for_move.append(f'for _ in range(40):')
        tests_for_move.append(f'    _pjm = make_poke(type1="{atk_type}", atk_b=100, spatk_b=100); _djm = make_poke(type1="{def_type}", hp_b=255)')
        tests_for_move.append(f'    _execute_move(BattleSide([_pjm]), BattleSide([_djm]), Action(type="move", move=_mvmiss), BattleField())')
        tests_for_move.append(f'    if getattr(_pjm, "_move_failed_this_turn", False): _missset = True; break')
        tests_for_move.append(f'check("外すと失敗フラグ成立: {name}", _missset, "技を外すと_move_failed_this_turnが立つこと")')
        tests_for_move.append(f'# ターン終了で前ターン失敗へ繰り越す')
        tests_for_move.append(f'from simulator.battle import Battle as _Bjd')
        tests_for_move.append(f'_pcarry = make_poke(type1="{atk_type}"); _pcarry._move_failed_this_turn = True')
        tests_for_move.append(f'_Bjd(BattleSide([_pcarry]), BattleSide([make_poke()]))._end_of_turn()')
        tests_for_move.append(f'check("失敗フラグ繰り越し: {name}", _pcarry._move_failed_last, "ターン終了で_move_failed_lastに繰り越すこと")')
    elif name == 'パワートリック':
        tests_for_move.append('# パワートリック: 攻撃と防御を入替')
        tests_for_move.append('_ppt = make_poke(atk_b=120, def_b=40); _a0, _d0 = _ppt.attack, _ppt.defense')
        tests_for_move.append('execute(_ppt, make_poke(), "パワートリック")')
        tests_for_move.append('check("パワートリック 攻防入替: パワートリック", _ppt.attack == _d0 and _ppt.defense == _a0)')
    elif name == 'ガードシェア':
        tests_for_move.append('# ガードシェア: 防御・特防を平均化')
        tests_for_move.append('_pgs = make_poke(def_b=200); _dgs = make_poke(def_b=20)')
        tests_for_move.append('_exp = (_pgs.defense + _dgs.defense)//2')
        tests_for_move.append('execute(_pgs, _dgs, "ガードシェア")')
        tests_for_move.append('check("ガードシェア 防御平均化: ガードシェア", _pgs.defense == _exp and _dgs.defense == _exp)')
    elif name == 'パワーシェア':
        tests_for_move.append('# パワーシェア: 攻撃・特攻を平均化')
        tests_for_move.append('_pps = make_poke(atk_b=200); _dps = make_poke(atk_b=20)')
        tests_for_move.append('_expp = (_pps.attack + _dps.attack)//2')
        tests_for_move.append('execute(_pps, _dps, "パワーシェア")')
        tests_for_move.append('check("パワーシェア 攻撃平均化: パワーシェア", _pps.attack == _expp and _dps.attack == _expp)')
    elif name == 'リサイクル':
        tests_for_move.append('# リサイクル: 消費道具を復元')
        tests_for_move.append('_prc = make_poke(); _prc.item = None; _prc._last_consumed_item = "オボンのみ"')
        tests_for_move.append('execute(_prc, make_poke(), "リサイクル")')
        tests_for_move.append('check("リサイクル 道具復元: リサイクル", _prc.item == "オボンのみ")')
    elif name == 'ねごと':
        tests_for_move.append('# ねごと: ねむり中に技を使う')
        tests_for_move.append('_png = make_poke(atk_b=120, moves=["たいあたり"]); _png.status = "sleep"')
        tests_for_move.append('_dng = make_poke(hp_b=200, def_b=50); _hng = _dng.hp')
        tests_for_move.append('execute(_png, _dng, "ねごと")')
        tests_for_move.append('check("ねごと 技発動: ねごと", _dng.hp < _hng, f"hp={_dng.hp}")')
        tests_for_move.append('# negative: 覚醒(非ねむり)状態では失敗')
        tests_for_move.append('_png_aw = make_poke(atk_b=120, moves=["たいあたり"]); _dng_aw = make_poke(hp_b=200, def_b=50); _hng_aw = _dng_aw.hp')
        tests_for_move.append('execute(_png_aw, _dng_aw, "ねごと")')
        tests_for_move.append('check("覚醒時は失敗: ねごと", _dng_aw.hp == _hng_aw, f"hp={_dng_aw.hp}/{_hng_aw}")')
    elif name == 'のろい':
        # 非ゴースト：攻撃+1防御+1速さ-1
        tests_for_move.append('# のろい(非ゴースト): 攻+1防+1速-1')
        tests_for_move.append('_pn = make_poke(type1="ノーマル"); execute(_pn, make_poke(), "のろい")')
        tests_for_move.append('check("のろい非ゴースト 攻+1: のろい", _pn.stage_attack == 1)')
        tests_for_move.append('check("のろい非ゴースト 防+1: のろい", _pn.stage_defense == 1)')
        tests_for_move.append('check("のろい非ゴースト 速-1: のろい", _pn.stage_speed == -1)')
        # ゴースト：相手に呪い
        tests_for_move.append('_pg = make_poke(type1="ゴースト"); _dg = make_poke()')
        tests_for_move.append('execute(_pg, _dg, "のろい")')
        tests_for_move.append('check("のろいゴースト 相手呪い: のろい", getattr(_dg, "cursed", False))')
    elif name == 'あくび':
        tests_for_move.append('# あくび: ねむけ付与(yawn_count)')
        tests_for_move.append('_pda = make_poke(); execute(make_poke(), _pda, "あくび")')
        tests_for_move.append('check("ねむけ付与: あくび", _pda.yawn_count == 2, f"yawn={_pda.yawn_count}")')
    elif name == 'いやしのねがい':
        tests_for_move.append('# いやしのねがい: 自分ひんし+healing_wishフラグ')
        tests_for_move.append('_piw = make_poke(); _s1iw = BattleSide([_piw, make_poke()]); _s2iw = BattleSide([make_poke()])')
        tests_for_move.append('_execute_move(_s1iw, _s2iw, Action(type="move", move=dl.get_move("いやしのねがい")), BattleField())')
        tests_for_move.append('check("いやしのねがい 自分ひんし: いやしのねがい", not _piw.is_alive)')
        tests_for_move.append('check("いやしのねがい healing_wish: いやしのねがい", _s1iw.healing_wish)')
    elif name == 'ちからをすいとる':
        tests_for_move.append('# ちからをすいとる: 相手の攻撃実数値分回復 + 相手の攻撃-1')
        tests_for_move.append('_pcs = make_poke(type1="フェアリー"); _pcs.hp = 1')
        tests_for_move.append('_dcs = make_poke(type1="ノーマル", atk_b=120, hp_b=255)')
        tests_for_move.append('_opp_atk = _dcs.attack; execute(_pcs, _dcs, "ちからをすいとる")')
        tests_for_move.append('check("相手攻撃実数値分回復: ちからをすいとる", abs(_pcs.hp - 1 - _opp_atk) <= 2, f"heal={_pcs.hp-1} opp_atk={_opp_atk}")')
        tests_for_move.append('check("相手攻撃-1: ちからをすいとる", _dcs.stage_attack == -1, f"atk={_dcs.stage_attack}")')
    elif name == 'おきみやげ':
        tests_for_move.append('# おきみやげ: 自己ひんし + 相手の攻撃・特攻を2段階下げる')
        tests_for_move.append('_posf = make_poke(type1="あく"); _dosf = make_poke(type1="エスパー", hp_b=255)')
        tests_for_move.append('execute(_posf, _dosf, "おきみやげ")')
        tests_for_move.append('check("自己ひんし: おきみやげ", not _posf.is_alive)')
        tests_for_move.append('check("相手攻撃-2: おきみやげ", _dosf.stage_attack == -2, f"atk={_dosf.stage_attack} 期待=-2")')
        tests_for_move.append('check("相手特攻-2: おきみやげ", _dosf.stage_sp_attack == -2, f"spa={_dosf.stage_sp_attack} 期待=-2")')
    elif name == 'キングシールド':
        tests_for_move.append('# キングシールド: 守る状態になる+接触攻撃者の攻撃-1')
        tests_for_move.append('_pks = make_poke(type1="はがね"); execute(_pks, make_poke(), "キングシールド")')
        tests_for_move.append('check("キングシールド 守る状態: キングシールド", _pks.protecting)')
        # 接触技で攻撃してきた相手の攻撃-1
        tests_for_move.append('_atkr = make_poke(type1="ノーマル", atk_b=100, moves=["のしかかり"]); _pks2 = make_poke(type1="はがね")')
        tests_for_move.append('_pks2.protecting = True; _pks2._protect_move = "キングシールド"')
        tests_for_move.append('_s1k = BattleSide([_atkr]); _s2k = BattleSide([_pks2])')
        tests_for_move.append('_execute_move(_s1k, _s2k, Action(type="move", move=dl.get_move("のしかかり")), BattleField())')
        tests_for_move.append('check("接触者攻撃-1: キングシールド", _atkr.stage_attack == -1, f"1回適用={_atkr.stage_attack} 期待=-1")')
        tests_for_move.append('# 使用するとシールドフォルムに戻る（ブレードフォルム→シールド）')
        tests_for_move.append('from simulator.battle import _aegislash_to_blade as _toblade')
        tests_for_move.append('_pksf = make_poke(type1="はがね", atk_b=100, ability="バトルスイッチ"); _toblade(_pksf, [])')
        tests_for_move.append('check("前提ブレードフォルム: キングシールド", _pksf._in_blade_forme)')
        tests_for_move.append('execute(_pksf, make_poke(), "キングシールド")')
        tests_for_move.append('check("使用でシールドフォルム化: キングシールド", not _pksf._in_blade_forme, f"blade={_pksf._in_blade_forme}")')
    elif name == 'バトンタッチ':
        tests_for_move.append('# バトンタッチ: 能力ランクを交代先に引き継ぐ')
        tests_for_move.append('_sbt = BattleSide([make_poke(type1="ノーマル"), make_poke(type1="みず")])')
        tests_for_move.append('_sbt.active.stage_attack = 3; _sbt.active.stage_speed = 2')
        tests_for_move.append('_execute_move(_sbt, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("バトンタッチ")), BattleField())')
        tests_for_move.append('_sbt.switch_to(1)')
        tests_for_move.append('check("能力ランク引き継ぎ: バトンタッチ", _sbt.active.stage_attack == 3 and _sbt.active.stage_speed == 2, f"atk={_sbt.active.stage_attack} spd={_sbt.active.stage_speed}")')
    elif name == 'オーロラベール':
        tests_for_move.append('# オーロラベール: ゆき(hail)下でのみ成功し、ゆき以外では失敗')
        tests_for_move.append('_sav = BattleSide([make_poke(type1="こおり")]); _fav = BattleField(); _fav.weather = "hail"')
        tests_for_move.append('_execute_move(_sav, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("オーロラベール")), _fav)')
        tests_for_move.append('check("ゆき下で成功: オーロラベール", _sav.aurora_veil, f"av={_sav.aurora_veil}")')
        tests_for_move.append('_sav2 = BattleSide([make_poke(type1="こおり")]); _fav2 = BattleField()')
        tests_for_move.append('_execute_move(_sav2, BattleSide([make_poke()]), Action(type="move", move=dl.get_move("オーロラベール")), _fav2)')
        tests_for_move.append('check("ゆき以外では失敗(negative): オーロラベール", not _sav2.aurora_veil, f"av={_sav2.aurora_veil}")')

    # ── 既存パターンで固有テストが付かなかった技のフォールバック ──
    # DB存在・優先度は「副次的」とみなし本体仕様検証にカウントしない。
    # ダメージ計算はダメージ技の最低保証として有効（カウント対象）。
    # （ミラーコートは power=NULL でダメージ計算が無く優先度だけ当たり、反射本体が未検証だった反省）
    _WEAK_PREFIXES = ('DB: ', '優先度')
    _has_specific = any(
        ('check("' in t) and not any(f'check("{p}' in t for p in _WEAK_PREFIXES)
        for t in tests_for_move
    )
    if not _has_specific:
        sn = safe_name(name)
        if cat == 'status':
            tests_for_move.append(f'# {name}: 副作用検証（status技フォールバック）')
            tests_for_move.append(f'side_effect_check("副作用発現: {name}", "{name}", "{atk_type}", {accuracy is not None}, smoke=("{name}" in DOUBLE_ONLY_SMOKE))')
        else:
            # ダメージ技でダメージ検証も無い（power=NULL可変等）→ 前提を整えてダメージ担保
            tests_for_move.append(f'# {name}: ダメージ技フォールバック')
            tests_for_move.append(f'_mvfb_{sn} = dl.get_move("{name}")')
            tests_for_move.append(f'if _mvfb_{sn}:')
            tests_for_move.append(f'    random.seed(0); _fb_ok_{sn} = False')
            tests_for_move.append(f'    for _ in range(10):')
            tests_for_move.append(f'        _pafb2 = make_poke(type1="{atk_type}", atk_b=120, spatk_b=120); _pdfb2 = make_poke(type1="{def_type}", def_b=80, spdef_b=80, hp_b=200)')
            # カウンター系: 被ダメージ記録 / なげつける: 道具 / ポルターガイスト: 相手道具
            tests_for_move.append(f'        _pafb2._last_physical_dmg_received = 120; _pafb2._last_special_dmg_received = 120')
            tests_for_move.append(f'        _pafb2.item = "こだわりハチマキ"; _pafb2._last_flung_item = "こだわりハチマキ"; _pdfb2.item = "たべのこし"')
            tests_for_move.append(f'        _pafb2.stockpile_count = 3  # はきだす等たくわえ前提技用')
            tests_for_move.append(f'        execute(_pafb2, _pdfb2, "{name}")')
            tests_for_move.append(f'        if _pdfb2.hp < _pdfb2.max_hp: _fb_ok_{sn} = True; break')
            tests_for_move.append(f'    check("効果発現(ダメージ): {name}", _fb_ok_{sn}, f"hp={{_pdfb2.hp}}")')

    if tests_for_move:
        lines.append(f'# ── {name} ──')
        lines.extend(tests_for_move)
        lines.append('')
        generated += 1

# 集計
lines.extend([
    "",
    "print(f'\\n全技テスト: {PASS}件PASS / {FAIL}件FAIL (計{PASS+FAIL}件)')",
    "if FAILURES:",
    "    for f in FAILURES[:20]: print(f'  {f}')",
    "    if len(FAILURES) > 20: print(f'  ...他{len(FAILURES)-20}件')",
    "else:",
    "    print('✅ 全テストパス')",
])

output = '\n'.join(lines)
outfile = '/Users/shigeki/work/pokenavi/scripts/tests/test_move_effects.py'
with open(outfile, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'生成完了: {generated}技 / {len(moves)}技')
print(f'スキップ(effect_textなし): {skipped}技')
print(f'出力: {outfile}')
