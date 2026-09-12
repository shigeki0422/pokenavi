"""上位プレイヤーテンプレ(M-1/M-2) vs 生成パーティ(GA) の構築要素ギャップ分析。
人間チームにあって生成に足りない『構築の観点』を、チーム単位の特徴で定量比較する。
"""
import os, sys, json, collections, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.ai import HAZARD_MOVES, SETUP_MOVES
from _party_quality import TYPES, adj_eff
from gen_party_pool import _item_of

PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
STATUS = {"どくどく", "おにび", "でんじは", "あくび", "ちょうはつ", "キノコのほうし",
          "ねむりごな", "しびれごな", "どくのこな", "やどりぎのタネ", "さいみんじゅつ", "でんじゃく"}
RECOVERY = {"じこさいせい", "はねやすめ", "なまける", "タマゴうみ", "こうごうせい",
            "あさのひざし", "つきのひかり", "げっこう", "ねむる"}
RECOVERY_ITEM = {"たべのこし", "くろいヘドロ", "オボンのみ"}
WEATHER_AB = {"ひでり", "あめふらし", "すなおこし", "ゆきふらし"}
WEATHER_MV = {"にほんばれ", "あまごい", "すなあらし", "あられ", "ゆきげしき"}


def spec_ev_h(s):
    return int(s.split("@")[1].split(":")[3].split("/")[0])


def team_features(party, L, season="M-3"):
    mons = [build_from_spec(parse_pokemon_spec(s), L, season=season, randomize=False) for s in party]
    f = {}
    def any_mon(pred): return sum(1 for m in mons if pred(m))
    mvset = lambda m: {mv.name_jp for mv in m.moves}
    f["hazard"] = 1 if any(mvset(m) & HAZARD_MOVES for m in mons) else 0
    f["pivot"] = any_mon(lambda m: mvset(m) & PIVOT)
    f["priority"] = any_mon(lambda m: any(getattr(mv, "priority", 0) > 0 for mv in m.moves))
    f["setup"] = any_mon(lambda m: mvset(m) & SETUP_MOVES)
    f["status"] = any_mon(lambda m: mvset(m) & STATUS)
    f["recovery"] = any_mon(lambda m: (mvset(m) & RECOVERY) or (m.item in RECOVERY_ITEM))
    f["scarf"] = 1 if any(m.item == "こだわりスカーフ" for m in mons) else 0
    f["trickroom"] = 1 if any("トリックルーム" in {mv.name_jp for mv in m.moves} for m in mons) else 0
    f["weather"] = 1 if any((m.ability in WEATHER_AB) or ({mv.name_jp for mv in m.moves} & WEATHER_MV)
                            for m in mons) else 0
    f["bulk_inv"] = sum(1 for s in party if spec_ev_h(s) >= 16)

    phys = spec = 0
    for m in mons:
        p = sum(1 for mv in m.moves if mv.category == "physical")
        s = sum(1 for mv in m.moves if mv.category == "special")
        if p > s: phys += 1
        elif s > p: spec += 1
    f["mixed_off"] = 1 if (phys >= 1 and spec >= 1) else 0
    f["phys_cnt"] = phys; f["spec_cnt"] = spec

    resisted = 0
    for A in TYPES:
        if any(adj_eff(A, m.type1, m.type2, m.ability) < 1 for m in mons):
            resisted += 1
    f["def_cover"] = resisted / len(TYPES)
    return f
