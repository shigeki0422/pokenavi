"""パーティ完成度計測。観点：
 (A) 2メガの攻撃範囲カバー（メガ=エース。2メガの抜群範囲が重複しない＝広く戦える）
 (B) 2メガの弱点重複（苦手が被ると的にされる）
 (C) パーティ全体の攻撃範囲カバー率（18タイプ中いくつを抜群で叩けるか）
 (D) パーティ全体の弱点重複（同一タイプに何体が弱点か＝刺さると総崩れ）
弱点は特性(ふゆう/もらいび/あついしぼう等の無効・半減・SE減)も加味。
使い方: venv/bin/python _party_quality.py [gen_pop_step1.json]
"""
import os, sys, json, collections, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.data import get_type_effectiveness

TYPES = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん",
         "ひこう", "エスパー", "むし", "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"]

IMMUNE = {"ふゆう": "じめん", "もらいび": "ほのお", "そうしょく": "くさ", "ちょすい": "みず",
          "よびみず": "みず", "かんそうはだ": "みず", "ひらいしん": "でんき",
          "でんきエンジン": "でんき", "ちくでん": "でんき", "フリーズスキン": None}
HALF = {"あついしぼう": {"ほのお", "こおり"}, "たいねつ": {"ほのお"}, "すいほう": {"ほのお"},
        "もふもふ": {"ほのお"}, "ぼうだん": set()}
SE_REDUCE = {"プリズムアーマー", "フィルター", "ハードロック"}


def adj_eff(atk, t1, t2, ability):
    if IMMUNE.get(ability) == atk: return 0.0
    e = get_type_effectiveness(atk, t1, t2)
    if ability in HALF and atk in HALF[ability]: e *= 0.5
    if ability in SE_REDUCE and e >= 2: e *= 0.75
    return e


def mon_profile(spec, L, season="M-3"):
    p = build_from_spec(parse_pokemon_spec(spec), L, season=season, randomize=False)
    atk = set()
    for m in p.moves:
        if getattr(m, "category", None) not in ("physical", "special"): continue
        if not getattr(m, "type", None): continue
        for T in TYPES:
            if get_type_effectiveness(m.type, T, None) >= 2:
                atk.add(T)
    is_mega = p.mega_data is not None
    if is_mega: p.do_mega_evolve()
    weak = {A for A in TYPES if adj_eff(A, p.type1, p.type2, p.ability) >= 2}
    return atk, weak, is_mega


def party_metrics(party, L, season="M-3"):
    profs = [mon_profile(s, L, season) for s in party]
    megas = [(a, w) for a, w, m in profs if m]
    allatk = set().union(*[a for a, w, m in profs]) if profs else set()

    if len(megas) >= 2:
        a1, w1 = megas[0]; a2, w2 = megas[1]
        mu = a1 | a2; mi = a1 & a2
        mega_cover = len(mu) / 18
        mega_atk_overlap = (len(mi) / len(mu)) if mu else 0
        mega_weak_shared = len(w1 & w2)
        mega_weak_overlap = (len(w1 & w2) / len(w1 | w2)) if (w1 | w2) else 0
    else:
        mega_cover = mega_atk_overlap = mega_weak_shared = mega_weak_overlap = None

    party_cover = len(allatk) / 18

    wcount = collections.Counter()
    for a, w, m in profs:
        for t in w:
            wcount[t] += 1
    max_shared = max(wcount.values()) if wcount else 0
    n3 = sum(1 for v in wcount.values() if v >= 3)
    worst_types = [t for t, v in wcount.items() if v == max_shared] if wcount else []
    return dict(n_mega=len(megas), mega_cover=mega_cover, mega_atk_overlap=mega_atk_overlap,
                mega_weak_shared=mega_weak_shared, mega_weak_overlap=mega_weak_overlap,
                party_cover=party_cover, weak_max_shared=max_shared, weak_n3=n3,
                worst_types=worst_types)
