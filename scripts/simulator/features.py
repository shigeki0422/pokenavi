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

TYPES = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく",
         "じめん", "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン",
         "あく", "はがね", "フェアリー"]
_TI = {t: i for i, t in enumerate(TYPES)}
_WEATHER = {None: 0, "rain": 1, "sun": 2, "sandstorm": 3, "hail": 4, "snow": 4}
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
    {"がんじょう", "ばけのかわ", "マルチスケイル"},                # 耐え
    {"すなかき", "ようりょくそ"},                                  # 天候加速
    {"いたずらごころ"},                                            # 優先度+1(変化)
    {"マジックミラー", "ミラーアーマー"},                          # 反射
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


def _expected_frac(att, deff, field, def_side=None) -> float:
    """att→deff の最大与ダメージをHP割合で。相手側 def_side の画面で半減を反映。"""
    if att is None or deff is None or not att.is_alive or not deff.is_alive:
        return 0.0
    best = 0.0
    for mv in att.moves:
        if mv and mv.power and mv.category != "status":
            try:
                d = calc_damage(att, deff, mv, field, random_roll=0.925)
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
    if (p.ability == "すなかき" and w == "sandstorm") or (p.ability == "ようりょくそ" and w == "sun"):
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


_POKE = 2 + len(TYPES) + 5 + 6 + len(_ITEM_FLAGS) + len(_ABIL_FLAGS) + 1 + len(TYPES) + 10 + _VOL  # =96
_PER_SIDE = 3 * _POKE + 7 + 2   # 7=能力ランク(A/B/C/D/S+命中+回避)
_MATRIX = 6
_SPEEDMAT = 9
_DISCLOSE = 18
_FIELD = 5 + 1 + 4 + 1 + 2 + 1 + 8 + 2 + 10 + 4   # +4: wish/future-sight予約（両陣営）= 38


def _poke_block(p, side) -> List[float]:
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
    abils = _flags(p.ability, _ABIL_FLAGS)
    megav = 1.0 if (p.mega_data is not None and not p.mega_evolved and not side.mega_used) else 0.0
    return [alive, hpf] + tvec + st + stats + items + abils + [megav] + _move_features(p) + _volatile_block(p)


def _side_features(side) -> List[float]:
    block: List[float] = []
    for p in _ordered_party(side):
        block += _poke_block(p, side)
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
    f = _side_features(side1) + _side_features(side2)

    # 期待ダメージ行列（相手画面で半減）
    for tgt in o2:
        f.append(_expected_frac(a1, tgt, field, side2))
    for tgt in o1:
        f.append(_expected_frac(a2, tgt, field, side1))

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
