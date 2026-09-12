"""勝率サロゲート(Product3-a)：総当たりデータを教師に『構築特徴→期待勝率』を学習。
対戦ゼロで強さを予測。線形Ridge(numpyのみ)＝重み＝構築論として解釈可能。
出力: surrogate_model.json（特徴名/重み/標準化パラメタ）＋CV評価。
"""
import os, json, glob, statistics, math
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.data import get_type_effectiveness
from _party_quality import TYPES, adj_eff
from _construction_gap import (HAZARD_MOVES, SETUP_MOVES, PIVOT, STATUS, RECOVERY,
                               RECOVERY_ITEM, WEATHER_AB, WEATHER_MV)
from _threat_coverage import load_threats, team_coverage
from gen_party_pool import PartyGen

FEATS = ["hazard", "pivot", "priority", "setup", "status", "recovery", "scarf", "weather",
         "bulk_inv", "mixed_off", "spec_cnt", "phys_cnt", "def_cover", "threat_cov",
         "atk_cover", "weak_max", "n_mega", "usage_sum", "avg_speed", "fast_cnt"]


def _spec_mega_item(s): return s.split("@", 1)[1].split(":")[0]
def _ev_h(s): return int(s.split("@")[1].split(":")[3].split("/")[0])


def features(party, L, pg, threats):
    mons = []
    for s in party:
        p = build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
        mons.append(p)
    mv = [{m.name_jp for m in p.moves} for p in mons]
    f = {}
    f["hazard"] = 1 if any(s & HAZARD_MOVES for s in mv) else 0
    f["pivot"] = sum(1 for s in mv if s & PIVOT)
    f["priority"] = sum(1 for p in mons if any(getattr(m, "priority", 0) > 0 for m in p.moves))
    f["setup"] = sum(1 for s in mv if s & SETUP_MOVES)
    f["status"] = sum(1 for s in mv if s & STATUS)
    f["recovery"] = sum(1 for i, p in enumerate(mons) if (mv[i] & RECOVERY) or (p.item in RECOVERY_ITEM))
    f["scarf"] = sum(1 for p in mons if p.item == "こだわりスカーフ")
    f["weather"] = sum(1 for i, p in enumerate(mons) if (p.ability in WEATHER_AB) or (mv[i] & WEATHER_MV))
    f["bulk_inv"] = sum(1 for s in party if _ev_h(s) >= 16)

    megamons = []
    for p in mons:
        if p.mega_data is not None:
            p.do_mega_evolve()
            megamons.append(p)

    phys = sum(1 for p in mons if sum(1 for m in p.moves if m.category == "physical") >= 2)
    spec = sum(1 for p in mons if sum(1 for m in p.moves if m.category == "special") >= 2)
    f["spec_cnt"] = spec
    f["phys_cnt"] = phys
    f["mixed_off"] = 1.0 if (phys >= 1 and spec >= 1) else 0.0
    f["def_cover"] = sum(1 for A in TYPES
                         if any(adj_eff(A, p.type1, p.type2, p.ability) < 1 for p in megamons)) / 18.0

    atk = set()
    for p in mons:
        for m in p.moves:
            if m.category not in ("physical", "special"): continue
            if not m.type: continue
            for T in TYPES:
                if get_type_effectiveness(m.type, T, None) >= 2:
                    atk.add(T)
    f["atk_cover"] = len(atk) / 18.0

    wc = {A: 0 for A in TYPES}
    for p in mons:
        for A in TYPES:
            if adj_eff(A, p.type1, p.type2, p.ability) >= 2:
                wc[A] += 1
    f["weak_max"] = max(wc.values())
    f["threat_cov"] = team_coverage(party, L, threats)[0]
    f["n_mega"] = sum(1 for s in party if _is_mega_item(_spec_mega_item(s)))
    f["usage_sum"] = sum(1.0 / pg.rank.get(s.split("@")[0], 1.0) for s in party)
    f["avg_speed"] = statistics.mean(p.speed for p in mons)
    f["fast_cnt"] = sum(1 for p in mons if p.speed >= 150)
    return [float(f[k]) for k in FEATS]


def _is_mega_item(it):
    return (it.endswith("ナイト") or it.endswith("ナイトＸ") or it.endswith("ナイトＹ")
            or it.endswith("ナイトX") or it.endswith("ナイトY"))
