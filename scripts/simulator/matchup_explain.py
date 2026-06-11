"""苦手理由の説明的分析（第1層・対戦不要の構造分析）。

2パーティの6×6個体マッチアップ（与ダメ/被ダメHP%・速度・1v1勝敗）を算出し、
「自分の穴（多くに負ける個体）」「相手の脅威（多くに勝つ個体）」と敗因要約を返す。
勝率だけでは分からない『なぜ苦手か』を提示する。
"""
import math
from typing import List

from .pokemon import parse_pokemon_spec, build_from_spec
from .battle import BattleField
from .features import _expected_frac
from .data import get_type_effectiveness


def _verdict(a, b, fld):
    """a vs b の1v1: 与ダメ/被ダメ(HP割合)・速度から勝敗を概算。"""
    da = _expected_frac(a, b, fld)   # a→b HP割合/ターン
    db = _expected_frac(b, a, fld)   # b→a
    ta = math.ceil(1 / da) if da > 0 else 99
    tb = math.ceil(1 / db) if db > 0 else 99
    af = a.get_effective_speed() >= b.get_effective_speed()
    if ta < tb or (ta == tb and af):
        v = "A"
    elif tb < ta or (tb == ta and not af):
        v = "B"
    else:
        v = "even"
    return v, round(da * 100), round(db * 100), af


def _has_setup(p):
    SETUP = {"つるぎのまい", "りゅうのまい", "ちょうのまい", "めいそう", "わるだくみ",
             "からをやぶる", "てっぺき", "ビルドアップ", "とぐろをまく", "こうそくいどう", "バトンタッチ"}
    return any(mv and mv.name_jp in SETUP for mv in (p.moves or []))


def explain_matchup(specsA: List[str], specsB: List[str], loader, season: str = "M-2") -> dict:
    A = [build_from_spec(parse_pokemon_spec(s), loader, season, randomize=False) for s in specsA]
    B = [build_from_spec(parse_pokemon_spec(s), loader, season, randomize=False) for s in specsB]
    fld = BattleField()
    cells = []
    a_lose = {i: 0 for i in range(len(A))}   # Aの各個体がBに負ける数
    b_win = {j: 0 for j in range(len(B))}     # Bの各個体がAに勝つ数
    a_win_tot = b_win_tot = 0
    for i, a in enumerate(A):
        row = []
        for j, b in enumerate(B):
            v, da, db, af = _verdict(a, b, fld)
            row.append({"v": v, "dealt": da, "taken": db, "faster": af})
            if v == "A":
                a_win_tot += 1
            elif v == "B":
                b_win_tot += 1
                a_lose[i] += 1
                b_win[j] += 1
        cells.append(row)

    liabilities = sorted(((A[i].name, c) for i, c in a_lose.items() if c >= 1),
                         key=lambda x: -x[1])
    threats = sorted(((B[j].name, c, _has_setup(B[j])) for j, c in b_win.items() if c >= 1),
                     key=lambda x: -x[1])
    # こちらが刺さる個体（多くのBに勝つ）と、それが止まる相手
    a_strong = sorted(((A[i].name, sum(1 for cell in cells[i] if cell["v"] == "A")) for i in range(len(A))),
                      key=lambda x: -x[1])

    # 敗因の自動文章化
    parts = []
    nB = len(B)
    top_threats = [t for t in threats if t[1] >= max(2, nB // 2)]
    if top_threats:
        names = "・".join(f"{t[0]}{'(積み有)' if t[2] else ''}" for t in top_threats[:3])
        parts.append(f"相手の{names}がこちらの多くに1v1勝ち（起点・詰めにされやすい）")
    top_liab = [l for l in liabilities if l[1] >= max(2, nB // 2)]
    if top_liab:
        names = "・".join(f"{l[0]}({l[1]}/{nB}敗)" for l in top_liab[:3])
        parts.append(f"特に{names}が与ダメ不足／被弾大で機能しにくい")
    if a_strong and a_strong[0][1] >= max(2, nB // 2):
        parts.append(f"{a_strong[0][0]}は刺さる（{a_strong[0][1]}/{nB}勝）ので選出の軸候補")
    summary = "。".join(parts) + "。" if parts else "明確な構造的不利は乏しい（実戦の立ち回り差が主因の可能性）。"

    return {
        "namesA": [p.name for p in A],
        "namesB": [p.name for p in B],
        "cells": cells,                       # cells[i][j] = {v,dealt,taken,faster}
        "a_win": a_win_tot, "b_win": b_win_tot,
        "liabilities": [{"name": n, "loses": c} for n, c in liabilities],
        "threats": [{"name": n, "wins": c, "setup": s} for n, c, s in threats],
        "summary": summary,
    }


def battle_explain(specsA: List[str], specsB: List[str], loader, n: int = 30,
                   season: str = "M-2", make_ai=None) -> dict:
    """第2層: 実戦の敗因（対戦後の最終状態を解析・エンジン非改変）。
    敗北時に相手のどの個体が生存して倒せなかったか／積み全抜きされたか／自分のどの個体が機能せず倒れるか。"""
    from .battle import Battle, BattleSide
    from .belief import OpponentBelief
    from .ai import HeuristicAI, select_party
    wins = losses = draws = 0
    opp_survive = {}     # 敗北時に生存していた相手個体
    your_dead = {}       # 敗北時に倒れていた自分個体
    setup_loss = 0       # 相手が積んだ個体を残して勝った（全抜き疑い）
    turns_sum = counted = 0
    for _ in range(n):
        A = [build_from_spec(parse_pokemon_spec(s), loader, season, randomize=True) for s in specsA]
        B = [build_from_spec(parse_pokemon_spec(s), loader, season, randomize=True) for s in specsB]
        s1 = BattleSide(select_party(A, B, loader))
        s2 = BattleSide(select_party(B, A, loader))
        s1.belief = OpponentBelief(loader); s2.belief = OpponentBelief(loader)
        ai = make_ai() if make_ai else HeuristicAI()
        b = Battle(s1, s2)
        w = b.run(ai, ai)
        turns_sum += getattr(b, "turn", 0) or getattr(b, "turn_count", 0) or 0
        counted += 1
        if w == 1:
            wins += 1
        elif w == 2:
            losses += 1
            swept = False
            for p in s2.party:
                if p.is_alive:
                    opp_survive[p.name] = opp_survive.get(p.name, 0) + 1
                    boosts = (getattr(p, "stage_attack", 0) + getattr(p, "stage_sp_attack", 0)
                              + getattr(p, "stage_speed", 0) + getattr(p, "stage_defense", 0)
                              + getattr(p, "stage_sp_defense", 0))
                    if boosts >= 3:
                        swept = True
            if swept:
                setup_loss += 1
            for p in s1.party:
                if not p.is_alive:
                    your_dead[p.name] = your_dead.get(p.name, 0) + 1
        else:
            draws += 1

    sl = max(1, losses)
    survive = sorted(opp_survive.items(), key=lambda x: -x[1])
    dead = sorted(your_dead.items(), key=lambda x: -x[1])
    parts = []
    if survive:
        names = "・".join(f"{n}({round(c/sl*100)}%)" for n, c in survive[:3])
        parts.append(f"敗北時、相手の{names}が生存（＝倒し切れていない核）")
    if setup_loss >= max(2, losses * 0.3):
        parts.append(f"積み全抜きでの敗北が{round(setup_loss/sl*100)}%（積みを許す前に倒す/流す必要）")
    if dead:
        names = "・".join(f"{n}({round(c/sl*100)}%)" for n, c in dead[:3])
        parts.append(f"自分の{names}が落ちやすい")
    summary = "。".join(parts) + "。" if parts else "実戦でも明確な偏りは少ない。"
    return {
        "n": n, "wins": wins, "losses": losses, "draws": draws,
        "win_rate": round(wins / max(1, n), 3),
        "opp_survive_on_loss": [{"name": k, "rate": round(v / sl, 2)} for k, v in survive[:5]],
        "your_dead_on_loss": [{"name": k, "rate": round(v / sl, 2)} for k, v in dead[:5]],
        "setup_loss_rate": round(setup_loss / sl, 2),
        "summary": summary,
    }
