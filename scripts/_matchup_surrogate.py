"""マッチアップ・サロゲート(Product3-a本命)。
総当たり89,700件を教師に、ダメージ計算ベースのリッチ・ペア特徴 → P(AがBに勝つ) をロジスティック学習。
任意環境での強さ = メタ相手の平均予測勝率。
env MAXSUBJ(0=全) で subject数制限（クイック検証用）。
"""
import os, json, glob, math, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import feature1 as _f1
from simulator.pokemon import build_from_spec, parse_pokemon_spec
from simulator.damage import calc_damage
from simulator.battle import BattleField
from simulator.ai import _effective_speed

FEATS = ["a_ohko", "b_ohko", "a_2hko", "b_2hko", "a_moff", "b_moff",
         "a_faster", "a_revenge", "b_revenge", "spd_adv", "off_adv", "def_adv"]


def build_party(specs, L):
    mons = []
    for s in specs:
        p = build_from_spec(parse_pokemon_spec(s), L, season="M-3", randomize=False)
        if p.mega_data is not None:
            p.do_mega_evolve()
        mons.append(p)
    return mons


def _dmg_safe(att, deff, mv, field, critical=False, roll=None):
    """副作用を持ち込まない calc_damage。
    calc_damage は半減きのみ消費で defender.item=None、充電技で attacker.charged=False と
    実体を書き換える（対戦本体では正しい）。分析側は同じオブジェクトを使い回すため、
    1回目の計算で相手のきのみが消え、2回目以降が「きのみ無し」になる事故が起きる。
    """
    _di = deff.item; _ai = att.item
    _c = getattr(att, "charged", None); _e = getattr(att, "_electromorphosis_charged", None)
    try:
        if roll is None:
            return calc_damage(att, deff, mv, field, critical)
        return calc_damage(att, deff, mv, field, critical, roll)
    finally:
        deff.item = _di; att.item = _ai
        if _c is not None: att.charged = _c
        if _e is not None: att._electromorphosis_charged = _e


def _bestdmg(a, b, field):
    best = 0
    for mv in a.moves:
        if mv.category not in ("physical", "special"): continue
        if not (mv.power or 0) > 0: continue
        try:
            d = _dmg_safe(a, b, mv, field, False, 0.85)
            if d > best: best = d
        except Exception:
            continue
    return best


def matchup_feats(A, B, field, spd):
    # spd: dict id(mon)->eff speed（事前計算）
    nA, nB = len(A), len(B)
    # ダメージ行列
    dAB = [[_bestdmg(a, b, field) for b in B] for a in A]   # A→B
    dBA = [[_bestdmg(b, a, field) for a in A] for b in B]   # B→A
    # A→B: 各Bを最大何%削れるか（Aの最善mon）
    offB = [max(dAB[i][j] for i in range(nA)) / B[j].max_hp for j in range(nB)]
    offA = [max(dBA[j][i] for j in range(nB)) / A[i].max_hp for i in range(nA)]
    a_ohko = sum(1 for x in offB if x >= 1.0) / nB
    b_ohko = sum(1 for x in offA if x >= 1.0) / nA
    a_2hko = sum(1 for x in offB if x >= 0.5) / nB
    b_2hko = sum(1 for x in offA if x >= 0.5) / nA
    a_moff = statistics.mean(min(x, 1.0) for x in offB)
    b_moff = statistics.mean(min(x, 1.0) for x in offA)
    # 速度・リベンジ: Aのmonがb を上から確1
    a_rev = 0
    for j in range(nB):
        if any(spd[id(A[i])] > spd[id(B[j])] and dAB[i][j] >= B[j].max_hp for i in range(nA)):
            a_rev += 1
    a_rev /= nB
    b_rev = 0
    for i in range(nA):
        if any(spd[id(B[j])] > spd[id(A[i])] and dBA[j][i] >= A[i].max_hp for j in range(nB)):
            b_rev += 1
    b_rev /= nA
    # Aの最速がbを抜いているか（相手ごとに1/0）の平均
    a_faster = statistics.mean(1.0 if max(spd[id(a)] for a in A) > spd[id(b)] else 0.0 for b in B)
    spd_adv = (max(spd[id(a)] for a in A) - max(spd[id(b)] for b in B)) / 200.0
    return [a_ohko, b_ohko, a_2hko, b_2hko, a_moff, b_moff,
            a_faster, a_rev, b_rev, spd_adv,
            a_ohko - b_ohko, b_2hko - a_2hko]
