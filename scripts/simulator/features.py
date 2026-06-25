"""バトル状態の特徴量化（学習価値関数の入力）。

設計原則: 「特徴量 ⊇ プレイヤーが認知できる公開/推定情報」。
side1 視点で P(side1勝利) を予測する用のベクトルを返す。

v6: わざ・特性表現を拡張、画面/おいかぜ/しんぴのまもり、実効速度の完全化。
- 個体: 生存/HP/タイプ/状態異常/全6実数値/持ち物8/特性16カテゴリ/メガ/攻撃タイプ網羅18/能力フラグ10
- 期待ダメージ行列（相手画面で半減補正）、すばやさ上回り3×3（スカーフ/おいかぜ/天候/TR反転を反映）
- 開示情報、天候/フィールド/TR/重力/設置 ＋ 画面(R/LS/AV)/おいかぜ/しんぴのまもり
"""
from typing import List

from .data import get_type_effectiveness
from .damage import calc_damage
from .items import get_speed_item_multiplier
from .ability_categories import (CATEGORIES as _ABIL_CATS, ABILITY_CAT_BITS as _ABIL_CAT_BITS,
                                 SPECIES_PRIOR_CATS as _SPECIES_PRIOR_CATS)

_N_ABIL_CATS = len(_ABIL_CATS)
_ZERO_ABIL_CATS = [0.0] * _N_ABIL_CATS

def _ability_cats(p, opp_belief=False):
    """特性の効果カテゴリベクトル（与えられた状態の実特性）。
    不完全情報は呼び出し側の決定化（相手の隠れ情報をbeliefからサンプル）で担保するため、
    ここでは状態どおりに符号化する。決定化済み状態なら相手特性=サンプル値（真値ではない）。"""
    return [float(b) for b in _ABIL_CAT_BITS.get(p.ability, _ZERO_ABIL_CATS)]

TYPES = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく",
         "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン",
         "あく", "はがね", "フェアリー"]
_TI = {t: i for i, t in enumerate(TYPES)}
_WEATHER = {None: 0, "rain": 1, "sun": 2, "sunny": 2, "sandstorm": 3, "hail": 4, "snow": 4}
_STATUS = {"paralysis": 0, "sleep": 1, "freeze": 2, "burn": 3, "poison": 4, "badpoison": 4}
_STAGES = ["stage_attack", "stage_defense", "stage_sp_attack", "stage_sp_defense", "stage_speed",
           "stage_accuracy", "stage_evasion"]   # v7: 命中・回避ランク追加

# 持ち物効果カテゴリ
_ITEM_FLAGS = [
    {"きあいのタスキ"}, {"たべのこし"}, {"オボンのみ"}, {"ラムのみ", "カゴのみ"},
    {"シュカのみ", "ハバンのみ", "ソクノのみ", "ヨロギのみ"},
    {"しんぴのしずく", "じしゃく", "とけないこおり", "りゅうのキバ", "やわらかいすな",
     "するどいくちばし", "くろいメガネ", "まがったスプーン", "ようせいのハネ", "メタルコート", "のろいのおふだ"},
    {"こだわりスカーフ"}, {"ひかりのこな"},
]
# 特性効果カテゴリ（16）: 情報系/条件発動/タイプ干渉/攻撃リスク
_ABIL_FLAGS = [
    {"いかく"},                                                   # いかく
    {"あめふらし", "すなおこし", "ゆきふらし"},                    # 天候設置
    {"さいせいりょく"},                                            # 再生
    {"がんじょう", "ばけのかわ", "マルチスケイル", "マジックガード"},  # 耐え/削り耐性
    {"すなかき", "ようりょくそ", "すいすい", "ゆきかき"},            # 天候加速
    {"いたずらごころ"},                                            # 優先度+1(変化)
    {"マジックミラー", "ミラーアーマー", "おうごんのからだ"},        # 相手変化技を無効/反射
    {"イリュージョン"},                                            # 身元偽装
    {"ふゆう"},                                                    # 地面無効
    {"もらいび"},                                                  # 炎吸収
    {"かんそうはだ", "すいほう"},                                  # 水関連
    {"さめはだ", "ほのおのからだ", "どくしゅ", "どくげしょう", "のろわれボディ"},  # 攻撃/接触にリスク
    {"てんねん"},                                                  # 能力ランク無視
    {"かたやぶり", "きもったま"},                                  # 特性/無効貫通
    {"じゅうなん", "ふみん", "しぜんかいふく", "シンクロ", "リーフガード"},  # 状態異常耐性/治癒
    {"へんげんじざい", "バトルスイッチ", "マイティチェンジ"},      # フォルム/タイプ変化
]

# わざ分類（能力フラグ用・代表例）
_M_SETUP = {"つるぎのまい", "りゅうのまい", "ちょうのまい", "めいそう", "わるだくみ", "からをやぶる",
            "てっぺき", "ビルドアップ", "とぐろをまく", "こうそくいどう", "ロックカット", "アシッドボム",
            "はらだいこ", "めざましビンタ", "つめとぎ", "コットンガード", "とける"}
_M_RECOVER = {"はねやすめ", "じこさいせい", "なまける", "つきのひかり", "あさのひざし", "こうごうせい",
              "タマゴうみ", "ねむる", "じこあんじ", "ミルクのみ", "なかまづくり", "いのちがけ"}
_M_HAZARD = {"ステルスロック", "まきびし", "どくびし", "ねばねばネット"}
_M_PHAZE = {"ドラゴンテール", "ともえなげ", "ほえる", "ふきとばし"}
_M_PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_M_PROTECT = {"まもる", "みきり", "キングシールド", "トーチカ", "ニードルガード", "スレッドトラップ", "がまん"}
_M_TWOTURN = {"ソーラービーム", "ソーラーブレード", "とびはねる", "あなをほる", "ダイビング", "そらをとぶ",
              "ロケットずつき", "はかいこうせん", "ギガインパクト", "メテオビーム", "ジオコントロール"}
_M_TRAP = {"バインド", "まきつく", "しめつける", "かなしばり", "くろいまなざし", "ほのおのうず",
           "うずしお", "すなじごく", "マグマストーム", "とおせんぼう", "ありじごく"}
_M_STATUS = {"でんじは", "おにび", "どくどく", "どくのこな", "しびれごな", "ねむりごな", "キノコのほうし",
             "さいみんじゅつ", "へびにらみ", "あくび", "ちょうおんぱ", "どくガス", "やどりぎのタネ", "あまえる"}


def switch_wins_1v1_split(first_in, rest_in, out_f, hp_frac, faster) -> bool:
    """着地の1発(first_in)と以降の被ダメ(rest_in)を分けた1v1撃ち合いモデル。
    交代先がメガ進化する場合：着地はメガ前(first_in)、次ターン以降はメガ後(rest_in)で被弾する想定。"""
    import math as _m
    if out_f <= 1e-6:
        return False
    ko = _m.ceil(1.0 / min(out_f, 1.0))      # 相手を倒すのに要する攻撃回数（与≥1.0で1発）
    extra = (ko - 1) if faster else ko        # 着地以降に受ける被弾回数
    return hp_frac > first_in + rest_in * extra


def switch_wins_1v1(in_f, out_f, hp_frac, faster) -> bool:
    """交代先が相手との1v1に勝てるか＝真の有利交代（着地1発＋速度の撃ち合い）。
    例: 被0.87/与0.74/HP1.0/速い → 倒すのに2発・その間に2発被弾(1.74>1.0)で先に落ちる→False。"""
    if in_f <= 1e-6 and out_f > 1e-6:
        return True
    return switch_wins_1v1_split(in_f, in_f, out_f, hp_frac, faster)


def _move_frac(att, deff, mv, field, def_side=None) -> float:
    """指定技1つの deff への期待与ダメ割合（連続技合計・画面半減反映）。変化技/Noneは0。"""
    if att is None or deff is None or not att.is_alive or not deff.is_alive:
        return 0.0
    if mv is None or not getattr(mv, "power", None) or mv.category == "status":
        return 0.0
    from .battle import MULTI_HIT_2, MULTI_HIT_3, MULTI_HIT_RANDOM_25
    try:
        n = mv.name_jp
        if n in MULTI_HIT_3:
            sv = getattr(att, "_multi_hit_index", 0); d = 0.0
            for hi in range(3):
                att._multi_hit_index = hi; d += calc_damage(att, deff, mv, field, random_roll=0.925)
            att._multi_hit_index = sv
        else:
            d = calc_damage(att, deff, mv, field, random_roll=0.925)
            if n in MULTI_HIT_2:
                d *= 2
            elif n in MULTI_HIT_RANDOM_25:
                d *= 5 if getattr(att, "ability", "") == "スキルリンク" else 3
        if def_side is not None:
            if mv.category == "physical" and (def_side.reflect or def_side.aurora_veil):
                d *= 0.5
            elif mv.category == "special" and (def_side.light_screen or def_side.aurora_veil):
                d *= 0.5
        return min(1.5, d / max(1, deff.max_hp))
    except Exception:
        return 0.0


def _best_move_vs(att, deff, field):
    """att の deff への最大与ダメ技（MoveData）。無ければNone。"""
    best = None; bv = -1.0
    for mv in (getattr(att, "moves", None) or []):
        if mv and getattr(mv, "power", None) and mv.category != "status":
            fv = _move_frac(att, deff, mv, field)
            if fv > bv:
                bv = fv; best = mv
    return best


def _switch_block(my_o, my_active, opp_active, field, my_side, opp_side) -> List[float]:
    """自分の控え2体について交代読みの特徴を返す（各4次元）：
      [読み技被ダメ(相手の対自分アクティブ最大打点技を控えに当てた割合),
       その技が来る前提で交代優位(1v1勝ち), 最悪(控えへの最大打点)前提で交代優位, 控えが相手より速い]。
    相手の攻撃を読んで交代する判断（例: 相手ガブのげきりんはアシレーヌに0）を学習可能にする。"""
    out: List[float] = []
    mstar = _best_move_vs(opp_active, my_active, field) if (opp_active and my_active) else None
    ospd = _real_speed(opp_active, opp_side, field) if opp_active else -1.0
    for b in my_o[1:3]:   # 控え2体
        if b is None or not b.is_alive or opp_active is None:
            out += [0.0, 0.0, 0.0, 0.0]; continue
        anti_in = _move_frac(opp_active, b, mstar, field, my_side)              # 読み技の被ダメ
        max_in = _expected_frac(opp_active, b, field, my_side, multi_hit=True)   # 控えへの最大被ダメ
        out_f = _expected_frac(b, opp_active, field, opp_side, multi_hit=True)   # 控えの与ダメ
        bspd = _real_speed(b, my_side, field)
        faster = (bspd >= ospd) if ospd >= 0 else True
        hp = b.hp / max(1, b.max_hp)
        # 読み交代の1v1：着地(1ターン目)は読み技anti_in、2ターン目以降は控えへの最大打点max_inで撃ち合う
        wins_read = switch_wins_1v1_split(anti_in, max_in, out_f, hp, faster)
        # 最悪：初手から最大打点で撃たれる前提
        wins_worst = switch_wins_1v1(max_in, out_f, hp, faster)
        out += [anti_in,
                1.0 if wins_read else 0.0,
                1.0 if wins_worst else 0.0,
                1.0 if faster else 0.0]
    return out


def _expected_frac(att, deff, field, def_side=None, multi_hit=False) -> float:
    """att→deff の最大与ダメージをHP割合で。相手側 def_side の画面で半減を反映。
    multi_hit=True で連続技(トリプルアクセル/タネマシンガン等)を合計ヒット分で見積もる
    （encode_stateの特徴量は既定False＝学習時と同じ初撃のみ＝ネット不変。解析/表示はTrue）。"""
    if att is None or deff is None or not att.is_alive or not deff.is_alive:
        return 0.0
    if multi_hit:
        from .battle import MULTI_HIT_2, MULTI_HIT_3, MULTI_HIT_RANDOM_25
    best = 0.0
    for mv in att.moves:
        if mv and mv.power and mv.category != "status":
            try:
                d = calc_damage(att, deff, mv, field, random_roll=0.925)
                if multi_hit:
                    n = mv.name_jp
                    if n in MULTI_HIT_3:                       # トリプルアクセル: 威力20/40/60
                        saved = getattr(att, "_multi_hit_index", 0)
                        d = 0.0
                        for hi in range(3):
                            att._multi_hit_index = hi
                            d += calc_damage(att, deff, mv, field, random_roll=0.925)
                        att._multi_hit_index = saved
                    elif n in MULTI_HIT_2:
                        d *= 2
                    elif n in MULTI_HIT_RANDOM_25:
                        d *= 5 if getattr(att, "ability", "") == "スキルリンク" else 3
                if def_side is not None:
                    if mv.category == "physical" and (def_side.reflect or def_side.aurora_veil):
                        d *= 0.5
                    elif mv.category == "special" and (def_side.light_screen or def_side.aurora_veil):
                        d *= 0.5
                f = d / max(1, deff.max_hp)
            except Exception:
                f = 0.0
            if f > best:
                best = f
    return min(1.5, best)


def _move_features(p) -> List[float]:
    """攻撃タイプ網羅18 ＋ 能力フラグ10（p.moves から算出）。"""
    cover = [0.0] * len(TYPES)
    pri = setup = recover = hazard = phaze = pivot = protect = twoturn = trap = status = 0.0
    for mv in (p.moves or []):
        if not mv:
            continue
        nm = mv.name_jp
        if mv.power and mv.category != "status" and mv.type in _TI:
            v = min(1.5, mv.power / 120.0)
            if v > cover[_TI[mv.type]]:
                cover[_TI[mv.type]] = v
            if mv.priority and mv.priority > 0:
                pri = 1.0
        if nm in _M_SETUP: setup = 1.0
        if nm in _M_RECOVER: recover = 1.0
        if nm in _M_HAZARD: hazard = 1.0
        if nm in _M_PHAZE: phaze = 1.0
        if nm in _M_PIVOT: pivot = 1.0
        if nm in _M_PROTECT: protect = 1.0
        if nm in _M_TWOTURN: twoturn = 1.0
        if nm in _M_TRAP: trap = 1.0
        if nm in _M_STATUS: status = 1.0
    return cover + [pri, setup, recover, status, hazard, phaze, pivot, protect, twoturn, trap]


def _real_speed(p, side, field) -> float:
    """実効速度: 実数値+ランク+麻痺 に スカーフ/おいかぜ/天候加速 を反映。"""
    if p is None or not p.is_alive:
        return -1.0
    spd = p.get_effective_speed()
    if p.ability != "ぶきよう":
        spd = spd * get_speed_item_multiplier(p.item)
    if getattr(side, "tailwind", False):
        spd *= 2
    w = field.weather
    if ((p.ability == "すなかき" and w == "sandstorm")
            or (p.ability == "ようりょくそ" and w == "sunny")
            or (p.ability == "すいすい" and w == "rain")
            or (p.ability == "ゆきかき" and w in ("hail", "snow"))):
        spd *= 2
    return spd


def _ordered_party(side):
    act = side.active
    bench = [p for i, p in enumerate(side.party) if i != side.active_idx]
    bench.sort(key=lambda p: (-(1 if p.is_alive else 0),
                              -((p.hp / p.max_hp) if p.max_hp else 0.0)))
    ordered = [act] + bench
    return ordered[:3] + [None] * (3 - len(ordered))


def _flags(name, groups) -> List[float]:
    return [1.0 if name in g else 0.0 for g in groups]


_VOL = 12   # v7: 戦略状態（猛毒蓄積/やどりぎ/あくび/ほろび/ちょうはつ/アンコール/かなしばり/いちゃもん/トラップ/溜め/まもる連投/こだわりロック）


def _volatile_block(p) -> List[float]:
    """戦略系の揮発状態（StallAI等が作り出す、v6が盲目だった状態）。"""
    if p is None:
        return [0.0] * _VOL
    return [
        min(1.0, getattr(p, "bad_poison_count", 0) / 15.0),
        1.0 if getattr(p, "seeded", False) else 0.0,
        1.0 if getattr(p, "yawn_count", 0) else 0.0,
        (1.0 - getattr(p, "perish_count", 0) / 3.0) if getattr(p, "perish_count", 0) else 0.0,
        1.0 if getattr(p, "taunt_count", 0) else 0.0,
        1.0 if getattr(p, "encore_count", 0) else 0.0,
        1.0 if getattr(p, "disabled_turns", 0) else 0.0,
        1.0 if getattr(p, "torment", False) else 0.0,
        1.0 if getattr(p, "trapped", False) else 0.0,
        1.0 if getattr(p, "charging_move", None) else 0.0,
        min(1.0, getattr(p, "protect_consecutive", 0) / 3.0),
        1.0 if getattr(p, "choice_locked_move", None) else 0.0,
    ]


_POKE = 2 + len(TYPES) + 5 + 6 + len(_ITEM_FLAGS) + _N_ABIL_CATS + 1 + len(TYPES) + 10 + _VOL  # 特性は54効果カテゴリ
_PER_SIDE = 3 * _POKE + 7 + 2   # 7=能力ランク(A/B/C/D/S+命中+回避)
_MATRIX = 18   # 全対面期待ダメージ: 自分3×相手3 ＋ 相手3×自分3（交代の生存＋脅威判断用）
_SPEEDMAT = 9
# 交代読み特徴: 各側の控え2体×[読み技被ダメ, 読み技で交代優位, 最悪被ダメで交代優位, 速度上回り]＝4×2×2側=16
_SWITCH = 16
_DISCLOSE = 18
_FIELD = 5 + 1 + 4 + 1 + 2 + 1 + 8 + 2 + 10 + 4   # +4: wish/future-sight予約（両陣営）= 38


def _poke_block(p, side, opp_belief=False) -> List[float]:
    if p is None:
        return [0.0] * _POKE
    alive = 1.0 if p.is_alive else 0.0
    hpf = (p.hp / p.max_hp) if (p.is_alive and p.max_hp) else 0.0
    tvec = [0.0] * len(TYPES)
    for t in (p.type1, p.type2):
        if t in _TI:
            tvec[_TI[t]] = 1.0
    st = [0.0] * 5
    if p.status in _STATUS:
        st[_STATUS[p.status]] = 1.0
    stats = [p.max_hp / 250.0, p.attack / 300.0, p.defense / 300.0,
             p.sp_attack / 300.0, p.sp_defense / 300.0, p.speed / 300.0]
    items = _flags(p.item, _ITEM_FLAGS)
    # 特性は効果カテゴリで表現。相手側(opp_belief指定)は未知特性をマスク（不完全情報）。
    abils = _ability_cats(p, opp_belief)
    megav = 1.0 if (p.mega_data is not None and not p.mega_evolved and not side.mega_used) else 0.0
    return [alive, hpf] + tvec + st + stats + items + abils + [megav] + _move_features(p) + _volatile_block(p)


def _side_features(side, opp_belief=False) -> List[float]:
    block: List[float] = []
    for p in _ordered_party(side):
        block += _poke_block(p, side, opp_belief)
    act = side.active
    block += [max(-1.0, min(1.0, getattr(act, s, 0) / 6.0)) for s in _STAGES]
    alive = [p for p in side.party if p.is_alive]
    block.append(len(alive) / 3.0)
    block.append(sum(p.hp / p.max_hp for p in alive if p.max_hp) / 3.0)
    return block


def _disclosure(opp_view, ordered) -> List[float]:
    out: List[float] = []
    pdict = getattr(opp_view, "pokemon", {}) if opp_view is not None else {}
    for p in ordered:
        if p is None:
            out += [0.0, 0.0, 0.0]
            continue
        k = pdict.get(p.name)
        if k is None:
            out += [0.0, 0.0, 0.0]
        else:
            out += [min(1.0, len(getattr(k, "known_moves", []) or []) / 4.0),
                    1.0 if getattr(k, "known_item", None) else 0.0,
                    1.0 if getattr(k, "known_ability", None) else 0.0]
    return out


def encode_state(side1, side2, field) -> List[float]:
    a1, a2 = side1.active, side2.active
    o1, o2 = _ordered_party(side1), _ordered_party(side2)
    # P(side1勝利)をside1視点で予測: side1=自分(フル情報)、side2=相手(未知特性はside1のbeliefでマスク)
    f = _side_features(side1) + _side_features(side2, getattr(side1, "belief", None))

    # 全対面期待ダメージ行列（相手画面で半減）。控えも含む全体×全体＝交代の生存＋脅威を直接表現。
    for att in o1:                       # 自分の各体 → 相手の各体（与ダメ）
        for deff in o2:
            f.append(_expected_frac(att, deff, field, side2))
    for att in o2:                       # 相手の各体 → 自分の各体（被ダメ）
        for deff in o1:
            f.append(_expected_frac(att, deff, field, side1))

    # すばやさ上回り 3×3（実効速度・TR反転）
    tr = bool(field.trick_room)
    s1s = [_real_speed(p, side1, field) for p in o1]
    s2s = [_real_speed(p, side2, field) for p in o2]
    for i in range(3):
        for j in range(3):
            if s1s[i] < 0 or s2s[j] < 0:
                f.append(0.0)
            else:
                faster = (s1s[i] <= s2s[j]) if tr else (s1s[i] >= s2s[j])
                f.append(1.0 if faster else 0.0)

    # （交代読み特徴 _switch_block は実験したが勝率に効かず、本番905ネット互換のため未使用。
    #   関数は _manual_battle 等の解析用に残置。再採用時は feature_dim と本番ネット再学習が必要）

    # 開示情報
    f += _disclosure(getattr(side1, "opp_view", None), o2)
    f += _disclosure(getattr(side2, "opp_view", None), o1)

    # 天候＋残ターン
    w = [0.0] * 5
    w[_WEATHER.get(field.weather, 0)] = 1.0
    f += w
    f.append(min(1.0, getattr(field, "weather_count", 0) / 5.0))
    terr = [1.0 if getattr(field, a, False) else 0.0
            for a in ("misty_terrain", "electric_terrain", "psychic_terrain", "grassy_terrain")]
    f += terr
    tcount = max(getattr(field, a, 0) for a in ("misty_terrain_count", "electric_terrain_count",
                                                "psychic_terrain_count", "grassy_terrain_count"))
    f.append(min(1.0, tcount / 5.0))
    f.append(1.0 if field.trick_room else 0.0)
    f.append(min(1.0, getattr(field, "trick_room_count", 0) / 5.0))
    f.append(min(1.0, getattr(field, "gravity", 0) / 5.0))
    # ねがいごと / みらいよち の予約（両陣営）＝遅延回復・遅延攻撃の着弾
    for s in (side1, side2):
        f.append(min(1.0, getattr(s, "wish_count", 0) / 2.0))
        f.append(min(1.0, getattr(s, "future_sight_count", 0) / 3.0))
    for s in (side1, side2):
        idx = s.field_idx
        f.append(1.0 if field.stealth_rock[idx] else 0.0)
        f.append(field.spikes[idx] / 3.0)
        f.append(field.toxic_spikes[idx] / 2.0)
        f.append(1.0 if field.sticky_web[idx] else 0.0)
    # 画面・おいかぜ・しんぴのまもり（陣営別）
    for s in (side1, side2):
        f.append(1.0 if getattr(s, "reflect", False) else 0.0)
        f.append(1.0 if getattr(s, "light_screen", False) else 0.0)
        f.append(1.0 if getattr(s, "aurora_veil", False) else 0.0)
        f.append(1.0 if getattr(s, "tailwind", False) else 0.0)
        f.append(min(1.0, getattr(s, "safeguard", 0) / 5.0))
    f.append(1.0 if a1.get_effective_speed() >= a2.get_effective_speed() else 0.0)
    f.append(max(-1.0, min(1.0, (a1.get_effective_speed() - a2.get_effective_speed()) / 200.0)))
    return f


def feature_dim() -> int:
    return 2 * _PER_SIDE + _MATRIX + _SPEEDMAT + _DISCLOSE + _FIELD
