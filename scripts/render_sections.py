#!/usr/bin/env python3
"""事実ファイルから、記事の「LLMが自由に書くと誤りが出る」部分を定型で生成する（第2期、2026-10-18）。

第1期の render_matchup_rows.py（苦手/得意表の行）は変更せず、ここから委譲する。追加するブロック（すべて表1つ・注記1行）:
  arch_grid     … 型カード群の直後。相手の型で判定が割れる相手のうち、自分の型で判定が変わる個体 × 型 の記号表
  partner_grid  … 同居率 partner-grid の直後。苦手表の相手 × パートナー の耐性記号表
  diff_movers   … データ分析の採用率表の直後。前季→今季の変化上位と型帰属（1行ずつ・上位8件）

出力は gate:rows と同じマーカー（<!-- gate:rows start id=<id> facts=<sha> --> … <!-- gate:rows end id=<id> -->）。
article_gate.py が逐語比較し、検証済みブロック内の数値は照合を省く（生成値＝事実）。
理由・因果は書かない。判定記号と倍率だけを表に並べる。本文で言い直さない（2026-10-18 ユーザー指摘：
「誰に強い弱いの個々の話は細かすぎる。型としての全体傾向を言う。表の中で完結させる」）。

使い方:
  python3 scripts/render_sections.py --facts _local/article_facts/<slug>.json --out _local/article_facts/<slug>.sections.md
"""
import argparse
import re
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import render_matchup_rows as RR  # noqa: E402

FAV = {"◎", "○"}
UNFAV = {"▲", "×"}
TOP_RANK = 20              # arch_grid / partner_grid の対象：使用率がこの順位以内
MINORITY_PCT = 10.0        # arch_grid: 自分側の決め技の採用率がこれ未満の個体は除外して件数だけ注記
MAIN_MOVE_PCT = 30.0       # partner_grid: 相手の「主力技」とみなす採用率
MEGA_STONE_PCT = 50.0      # partner_grid: メガ石の採用率がこれ以上ならメガ形態で判定
MIN_PT = 3.0               # diff_movers: |変化| がこれ以上の項目だけ
MAX_MOVERS = 8
POOL_SHARE_PCT = 20.0      # diff_movers: 型内シェアがこれ以上なら「その型が持つ」とみなす

TABLE_OPEN = '<div style="overflow-x:auto;margin:12px 0">\n<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">'
TABLE_CLOSE = "</table>\n</div>"
TH = '<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">'
TD = '<td style="padding:6px 8px;border:1px solid #cbd5e1">'
TD_L = '<td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">'
NOTE = '<td colspan="{n}" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">'


def _by(facts):
    return RR._index(facts)


def _mult_text(v):
    if v is None:
        return None
    if v == 0:
        return "無効"
    return f"×{v:g}"


def _note_row(ncols, text):
    return f'<tr class="note">{NOTE.format(n=ncols)}{text}</td></tr>'


# ---------------------------------------------------------------- arch_grid --

def arch_grid_rows(facts, minority_pct=MINORITY_PCT, top_rank=TOP_RANK):
    """{"rows": [{opp_label, opp_sp, opp_nature, opp_item, opp_share, syms: {arch: sym}, moves: {arch: (move, selected)}}],
        "excluded_minority": int, "no_diff_opps": [opp]}"""
    by = _by(facts)
    cards = facts.get("cards", [])
    arches = [c["arch"] for c in cards]
    card_moves = {c["arch"]: set(c["moves"]) for c in cards}
    rank_of = {f["pokemon"]: f["value"] for f in by.get("usage_rank", []) if not f.get("season")}
    out = {"rows": [], "excluded_minority": 0, "no_diff_opps": []}
    mixed = [v for v in by.get("verdict", []) if v["value"] == "mixed" and (rank_of.get(v["opp_sp"]) or 9999) <= top_rank]
    mixed.sort(key=lambda v: rank_of.get(v["opp_sp"], 9999))
    for v in mixed:
        rows = [m for m in by.get("matchup", []) if m["opp"] == v["opp"]]
        groups = {}
        for m in rows:
            key = (m["opp_label"], m["opp_nature"], m["opp_item"], tuple(m.get("opp_ev") or []))
            groups.setdefault(key, {})[m["my_arch"]] = m
        any_diff = False
        for key, per in groups.items():
            if set(per) != set(arches):
                continue
            syms = {a: per[a]["sym"] for a in arches}
            if len(set(syms.values())) == 1:
                continue
            any_diff = True
            # 決め技が少数派技（採用率<minority）の型が含まれる個体は除外して件数だけ注記
            if any(per[a].get("my_move") is not None and (per[a].get("my_move_rate") is None or per[a]["my_move_rate"] < minority_pct) for a in arches):
                out["excluded_minority"] += 1
                continue
            m0 = per[arches[0]]
            out["rows"].append({
                "opp_label": m0["opp_label"], "opp_sp": v["opp_sp"], "opp_nature": m0["opp_nature"], "opp_item": m0["opp_item"],
                "opp_ev": list(m0.get("opp_ev") or []),
                "opp_share": m0.get("opp_share"), "syms": syms,
                "moves": {a: (per[a].get("my_move"), per[a].get("my_move") is not None and per[a]["my_move"] not in card_moves.get(a, set())) for a in arches},
            })
        if not any_diff:
            out["no_diff_opps"].append(v["opp"])
    return out


def render_arch_grid(facts):
    cards = facts.get("cards", [])
    arches = [c["arch"] for c in cards]
    r = arch_grid_rows(facts)
    if not r["rows"]:
        return ""
    L = [TABLE_OPEN, '<thead>\n<tr>', f'{TH.replace("background:#f1f5f9", "background:#f1f5f9;text-align:left")}相手（性格・持ち物個体）</th>']
    L += [f"{TH}{a}</th>" for a in arches]
    L += ["</tr>\n</thead>\n<tbody>"]
    # 同じ相手で判定の並びが同じ個体は1行にまとめる（カバルドンの3個体が ○○× で同じ、等）
    merged = []
    for row in r["rows"]:
        key = (row["opp_label"], tuple(row["syms"][a] for a in arches), tuple(row["moves"][a][1] for a in arches))
        for m in merged:
            if m["key"] == key:
                m["rows"].append(row)
                break
        else:
            merged.append({"key": key, "rows": [row]})
    # 性格・持ち物まで同じでEVだけ違う個体が別の行になると、同じラベルが2行並んで判定だけ違って見える
    # （2026-10-25 マスカーニャのミミッキュ）。その場合はEV配分をラベルに足す
    base_lbl = [(m["rows"][0]["opp_label"], m["rows"][0]["opp_nature"], m["rows"][0]["opp_item"]) for m in merged]
    for i, m in enumerate(merged):
        shade = ' style="background:#fafafa"' if i % 2 == 1 else ""
        rows = m["rows"]
        first = rows[0]
        # 個体の割合（型プール推定）は記事に書かない（ユーザー指示 2026-10-16・10-25）
        who = f"{first['opp_label']}（{first['opp_nature']}・{first['opp_item']}"
        if base_lbl.count(base_lbl[i]) > 1 and first.get("opp_ev"):
            who += "・" + "-".join(f"{l}{e}" for l, e in zip("HABCDS", first["opp_ev"]) if e)
        if len(rows) > 1:
            who += f" ほか{len(rows) - 1}個体"
        who += "）"
        cells = []
        for a in arches:
            mv, sel = first["moves"][a]
            cells.append(f"{TD}{first['syms'][a]}{'※' if sel else ''}</td>")
        L.append(f"<tr{shade}>{TD_L}{who}</td>" + "".join(cells) + "</tr>")
    note = "◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体"
    if any("※" in x for x in L):
        note += "。※＝上の型の技構成に無い選択技での判定"
    if r["excluded_minority"]:
        note += f"。採用率{MINORITY_PCT:g}%未満の技が決め手になる個体{r['excluded_minority']}件は除く"
    if r["no_diff_opps"]:
        note += f"。{'、'.join(r['no_diff_opps'])}は型で判定が変わらない"
    L.append(_note_row(1 + len(arches), note))
    L += ["</tbody>", TABLE_CLOSE]
    return "\n".join(L)


# ------------------------------------------------------------- partner_grid --

def _partner_form(by, name, season, mega_stone_pct):
    """判定に使う形態名（メガ石採用率がしきい値以上ならメガ形態）と、その石の採用率。"""
    item_rate = {f["name"]: f["value"] for f in by.get("adopt_rate", [])
                 if f["category"] == "item" and f["pokemon"] == name and f["season"] == season}
    best = None
    for mf in by.get("mega_form", []):
        if mf["pokemon"] == name:
            rate = item_rate.get(mf["stone"])
            if rate is not None and rate >= mega_stone_pct and (best is None or rate > best[1]):
                best = (mf["form"], rate)
    return best or (name, None)


def _main_moves(by, opp_sp, season, main_pct):
    power = {f["move"]: f for f in by.get("move_power", [])}
    out = []
    for f in by.get("adopt_rate", []):
        if f["category"] != "move" or f["pokemon"] != opp_sp or f["season"] != season or f["value"] < main_pct:
            continue
        mp = power.get(f["name"])
        if not mp or not mp.get("value") or mp.get("category") == "変化":
            continue
        out.append((f["name"], mp["type"], f["value"]))
    out.sort(key=lambda x: -x[2])
    return out


ABILITY_IMMUNE = {"ふゆう": "じめん", "ちょすい": "みず", "よびみず": "みず", "かんそうはだ": "みず", "ちくでん": "でんき",
                  "ひらいしん": "でんき", "でんきエンジン": "でんき", "もらいび": "ほのお", "そうしょく": "くさ"}


ABILITY_HALVE = {"あついしぼう": {"ほのお", "こおり"}, "たいねつ": {"ほのお"}, "きよめのしお": {"ゴースト"}, "すいほう": {"ほのお"}}


def partner_grid_rows(facts, main_pct=MAIN_MOVE_PCT, mega_stone_pct=MEGA_STONE_PCT):
    by = _by(facts)
    season = facts["subject"]["season"]
    maj = facts["sources"].get("majority_pct", 20)
    assert main_pct >= maj, f"partner_grid の主力技しきい値({main_pct})は majority_pct({maj})以上にする（技タイプが事実に無くなる）"
    types = {f["pokemon"]: f["value"] for f in by.get("types", [])}
    eff = {(f["atk_type"], f["defender"]): f["value"] for f in by.get("type_eff", [])}
    rank_of = {f["pokemon"]: f["value"] for f in by.get("usage_rank", []) if not f.get("season")}
    partners = sorted(by.get("partner_rank", []), key=lambda f: f["value"])
    cols = [(p["value"], p["partner"], *_partner_form(by, p["partner"], season, mega_stone_pct)) for p in partners]
    weak = [v for v in by.get("verdict", []) if v["value"] == "lose"]
    weak.sort(key=lambda v: rank_of.get(v["opp_sp"], 9999))
    rows, seen = [], {}
    for v in weak:
        moves = _main_moves(by, v["opp_sp"], season, main_pct)
        if not moves:
            continue
        key = (v["opp_sp"], tuple(moves))
        if key in seen:
            seen[key]["opp"] += "・" + v["opp"]
            continue
        row = {"opp": v["opp"], "opp_sp": v["opp_sp"], "moves": moves, "cells": []}
        for rank, base, form, stone_rate in cols:
            if form not in types:
                raise ValueError(f"partner_grid: {form} の types が事実に無い（article_facts.py を再実行する）")
            mults = []
            for m in moves:
                if (m[1], form) not in eff:
                    raise ValueError(f"partner_grid: type_eff/{m[1]}/{form} が事実に無い")
                mults.append(eff[(m[1], form)])
            sym = "◎" if all(x <= 0.5 for x in mults) else ("○" if mults[0] <= 0.5 else "")
            # 同じ種族どうし（相手リザードン×パートナーのメガリザードンY）は判定しない（2026-10-25 レビュー指摘）
            if base == v["opp_sp"]:
                sym = "—"
            row["cells"].append(sym)
        seen[key] = row
        rows.append(row)
    # 被写体の弱点タイプをパートナーが半減以下で受けられるか（「なぜ同じパーティに入るか」）。本文に手で書かせると
    # 誤る（2026-10-25 カバルドン：メガグソクムシャはみず等倍なのに「耐性で受けられる」と書いた）ので表で出す
    subj = facts["subject"]["name"]
    # 被写体もメガ石の採用率がしきい値以上ならメガ形態の弱点・特性で判定する（2026-10-28 ムクホーク：パートナーはメガで
    # 判定するのに被写体だけメガ前の弱点いわを出していた／マフォクシー：メガ後のふゆうでじめん無効）
    sform, _ = _partner_form(by, subj, season, mega_stone_pct)
    if not any(f["defender"] == sform for f in by.get("type_eff", [])):
        sform = subj
    own = []
    # 全ての型カードが同じ無効化特性（ふゆう等）を持つなら、そのタイプは弱点行に出さない（2026-10-27 ヒートロトムのじめん）
    # メガ形態で判定するときは、メガ進化する型の特性だけを見る（2026-10-28 フシギバナ：非メガのいのちのたま型が混ざり、あついしぼうが外れた）
    card_abs = ({c["mab"] for c in facts.get("cards", []) if c.get("mab")} if sform != subj
                else {c.get("ability") for c in facts.get("cards", [])})
    immune = {ABILITY_IMMUNE[a] for a in card_abs if a in ABILITY_IMMUNE} if len(card_abs) == 1 else set()
    # あついしぼう等でダメージが半減するタイプは、×2 なら実質等倍なので弱点行に出さない（2026-10-28 メガフシギバナのほのお・こおり）
    halve = set().union(*[ABILITY_HALVE[a] for a in card_abs if a in ABILITY_HALVE]) if len(card_abs) == 1 else set()
    for t_ in sorted({f["atk_type"] for f in by.get("type_eff", []) if f["defender"] == sform
                      and f["value"] * (0.5 if f["atk_type"] in halve else 1) >= 2} - immune):
        cells = []
        for rank, base, form, stone_rate in cols:
            if (t_, form) not in eff:
                raise ValueError(f"partner_grid: type_eff/{t_}/{form} が事実に無い")
            x = eff[(t_, form)]
            cells.append("無効" if x == 0 else ("◎" if x <= 0.5 else ""))
        own.append({"type": t_, "cells": cells})
    return {"cols": cols, "rows": rows, "own": own, "own_form": sform}


def render_partner_grid(facts):
    r = partner_grid_rows(facts)
    if not r["rows"]:
        return ""
    L = [TABLE_OPEN, '<thead>\n<tr>', f'{TH.replace("background:#f1f5f9", "background:#f1f5f9;text-align:left")}苦手な相手（主力技）</th>']
    for rank, base, form, stone_rate in r["cols"]:
        # 見出しは同居率カードと同じ種族名にし、メガ形態で判定したときは小さく添える（2026-10-27 名前の食い違いの指摘が続いたため）
        sub = f"同居率{rank}位" + (f"・{form}で判定" if form != base else "")
        L.append(f"{TH}{base}<br><span style=\"font-weight:normal;font-size:0.85em\">{sub}</span></th>")
    L += ["</tr>\n</thead>\n<tbody>"]
    subj = facts["subject"]["name"]
    # リベロ・へんげんじざいは技を出すとタイプが変わるので、弱点行は「技を出す前」のタイプだと明記する（2026-10-25 エースバーン）
    protean = any(c.get("ability") in ("リベロ", "へんげんじざい") for c in facts.get("cards", []))
    oform = r.get("own_form", subj)
    own_lbl = f"{oform}の弱点（技を出す前）" if protean else f"{oform}の弱点"
    for row in r.get("own", []):
        L.append(f"<tr style=\"background:#eff6ff\">{TD_L}{own_lbl}：{row['type']}技</td>" + "".join(f"{TD}{c}</td>" for c in row["cells"]) + "</tr>")
    for i, row in enumerate(r["rows"]):
        shade = ' style="background:#fafafa"' if i % 2 == 1 else ""
        L.append(f"<tr{shade}>{TD_L}{row['opp']}</td>" + "".join(f"{TD}{c}</td>" for c in row["cells"]) + "</tr>")
    # 「どのパートナーが広く受けられるか」を本文で言い直すと読み違いが起きる（2026-10-25 ガブリアス・カバルドンで
    # ○を◎と読んだ誤り）ので、列ごとの ◎/○ の数を表の最終行に出して表の中で完結させる
    counts = []
    for j in range(len(r["cols"])):
        col = [row["cells"][j] for row in r["rows"]]
        counts.append(f"◎{col.count('◎')}・○{col.count('○')}")
    L.append(f"<tr>{TD_L}<strong>受けられる相手の数</strong></td>" + "".join(f"{TD}{c}</td>" for c in counts) + "</tr>")
    # 主力技の一覧はセルに入れると1列目が縦に伸びるので注記行にまとめる
    moves_note = "；".join(f"{row['opp']}＝{'・'.join(m[0] for m in row['moves'])}" for row in r["rows"])
    note = (f"◎＝主力技（採用率{MAIN_MOVE_PCT:g}%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。"
            f"青い行＝{oform}の弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が{MEGA_STONE_PCT:g}%以上の種はメガ形態で判定。主力技：{moves_note}")
    L.append(_note_row(1 + len(r["cols"]), note))
    L += ["</tbody>", TABLE_CLOSE]
    return "\n".join(L)


# -------------------------------------------------------------- diff_movers --

def _holders(facts, category, name, pool_share_pct=POOL_SHARE_PCT):
    by = _by(facts)
    cards = facts.get("cards", [])
    fixed, select, pool = [], [], []
    for c in cards:
        if category == "move":
            if name in c["moves"]:
                fixed.append(c["arch"])
            elif name in c.get("mpool", []):
                select.append(c["arch"])
        elif category == "item" and c["item"] == name:
            fixed.append(c["arch"])
        elif category == "nature" and c["nature"] == name:
            fixed.append(c["arch"])
        elif category == "ability" and c["ability"] == name:
            fixed.append(c["arch"])
    kind = {"move": "arch_move_share", "item": "arch_item_share", "nature": "nature_share"}.get(category)
    key = {"move": "move", "item": "item", "nature": "nature"}.get(category)
    if kind:
        for f in by.get(kind, []):
            if f["pokemon"] == facts["subject"]["name"] and f.get(key) == name and f["value"] >= pool_share_pct:
                pool.append((f["arch"], f["value"]))
    return {"fixed": fixed, "select": select, "pool": pool}


def diff_movers(facts, min_pt=MIN_PT, categories=("move", "item", "nature", "ability"), limit=MAX_MOVERS):
    by = _by(facts)
    subj = facts["subject"]["name"]
    season = facts["subject"]["season"]
    prev = facts["sources"].get("prev_season")
    rate = {}
    for f in by.get("adopt_rate", []):
        if f["pokemon"] == subj:
            rate[(f["category"], f["name"], f["season"])] = f["value"]
    card_arches = {c["arch"] for c in facts.get("cards", [])}
    lines, sole = [], []
    diffs = [f for f in by.get("adopt_rate_diff", []) if f["pokemon"] == subj and f["category"] in categories and abs(f["value"]) >= min_pt]
    diffs.sort(key=lambda f: -abs(f["value"]))
    cards_all = facts.get("cards", [])
    all_mega = bool(cards_all) and all(c.get("mab") for c in cards_all)
    # すべての型がメガ進化するなら、メガ前の特性の増減は型の判断に関係しない（2026-10-28 ウツボット）
    if all_mega:
        diffs = [f for f in diffs if f["category"] != "ability"]
    for f in diffs[:limit]:
        cat, name = f["category"], f["name"]
        a, b = rate.get((cat, name, prev)), rate.get((cat, name, season))
        h = _holders(facts, cat, name)
        holders = h["fixed"]
        # 記事の型カードと同名の型は、カードの技構成（4技・選択技）を正とする。型プールの推定割合だけで「共通」に
        # 数えると、カードに無い技を持つように読めて本文と矛盾する（2026-10-25 カイリュー：ドラゴンテール型のはねやすめ）
        # 性格・持ち物はカードが代表1つしか持たないので型プール側を正とし、技（4技＋選択技）だけカードを正とする
        pool_arches = [x[0] for x in h["pool"]
                       if cat != "move" or x[0] not in card_arches or x[0] in holders or x[0] in h["select"]]
        if cat in ("item", "nature", "ability"):
            # 持ち物・性格・特性はカードに1つだけ。カードの値（fixed）を正とし、型プールで一部の個体が持つ型は分けて書く
            # （2026-10-28 ヒスイヌメルゴン：なまいき＝型2の性格を「含まれません」、ひかえめを「すべての型に共通」と誤生成）
            verb = {"item": "持つ", "nature": "選んでいる", "ability": "持つ"}[cat]
            part = [x for x in dict.fromkeys(pool_arches) if x in card_arches and x not in holders]
            others = [x for x in pool_arches if x not in card_arches]
            if len(holders) == 1 and not part and not others:
                judge = f"{holders[0]}だけが{verb}ため、この変化はその型の増減を示します"
            elif holders and set(holders) == card_arches and len(card_arches) >= 2:
                judge = f"記事のすべての型が{verb}ため、型の増減とは言えません"
            elif holders:
                tail = (f"ほか、{'・'.join(part)}の一部の個体も{verb}" if part else "ほか、記事に載せていない型の個体も" + verb if others else "")
                judge = f"{'・'.join(holders)}が{verb}{tail}ため、型の増減とは言い切れません"
            elif part:
                judge = f"{'・'.join(part)}の一部の個体が{verb}もので、型の増減とは言えません"
            else:
                what = {"item": "持ち物", "nature": "性格", "ability": "特性"}[cat]
                judge = f"この記事の型の{what}には含まれません"
        elif len(holders) == 1 and len(set(pool_arches) | set(holders)) <= 1 and not [x for x in h["select"] if x not in holders]:
            judge = f"{holders[0]}だけが持つため、この変化はその型の増減を示します"
        elif len(holders) == 1 and [x for x in h["select"] if x not in holders]:
            sel = [x for x in h["select"] if x not in holders]
            judge = f"{holders[0]}が持ち、{'・'.join(sel)}でも選択技のため、型の増減とは言えません"
        elif len(holders) >= 2 or len(set(pool_arches)) >= 2:
            # 記事に載せていない型の名前は読者に通じないので出さない（2026-10-25「型カード外」は内部用語）
            # 選択技として持つ型も「共通」に含める（2026-10-27 サザンドラのだいもんじ）
            shown = [x for x in sorted(set(holders) | set(pool_arches) | set(h["select"]), key=lambda x: (x not in holders, x)) if x in card_arches]
            others = len(set(pool_arches) - card_arches)
            if len(holders) == 1 and not [x for x in shown if x not in holders]:
                # 記事の型では1つだけが持つのに「共通」と書くと、型カードの「他の型に無い技」と矛盾して見える（2026-10-27 ドヒドイデのくろいきり）
                judge = f"記事の型では{holders[0]}だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません"
            elif holders and shown and set(shown) == card_arches and len(card_arches) >= 2:
                judge = "記事のすべての型に共通のため、型の増減とは言えません"
            elif not holders and set(h["select"]) == card_arches and len(card_arches) >= 2:
                # 4技に入れている型が無く、どの型でも選択技（2026-10-28 マンムーのつららばり：4技のつららおとしと同じ「共通」に見えた）
                judge = "記事のすべての型で選択技にとどまるため、型の増減とは言えません"
            elif cat in ("item", "nature") and len(holders) >= 1 and [x for x in shown if x not in holders]:
                # 持ち物・性格はカードに1つだけ。代表個体が持たない型まで「共通」と書くとカードと食い違う（2026-10-28 ペリッパー・ブリムオン）
                part = [x for x in shown if x not in holders]
                verb = "持つ" if cat == "item" else "選んでいる"
                judge = (f"{'・'.join(holders)}が{verb}ほか、{'・'.join(part)}の一部の個体も{verb}ため、型の増減とは言えません")
            elif not holders:
                # 型カードの代表個体はどれも持たず、型の一部の個体が持つだけ（2026-10-28 エンペルト：カードはたべのこしなのに
                # ふうせんを「あくび型・クイックターン型に共通」と書きカードと食い違って見えた）
                who = "・".join(shown) if shown else "複数の型"
                verb = "採用している" if cat == "move" else "持つ" if cat == "item" else "選んでいる"
                judge = f"{who}の一部の個体が{verb}もので、型の増減とは言えません"
            else:
                who = "・".join(shown) + ("と、記事に載せていない型" if shown and others else "" if shown else "複数の型")
                judge = f"{who}に共通のため、型の増減とは言えません"
        elif not holders and h["select"]:
            judge = f"{'・'.join(h['select'])}の選択技のため、型の増減とは言えません"
        elif not holders and pool_arches:
            judge = (f"{pool_arches[0]}の一部の個体が採用しているもので、型の増減とは言えません" if pool_arches[0] in card_arches
                     else "記事に載せていない型の個体が採用しているもので、記事の型とは関係しません")
        else:
            what = {"move": "技構成", "item": "持ち物", "nature": "性格", "ability": "特性"}.get(cat, "技構成")
            judge = f"この記事の型の{what}には含まれません"
        if len(card_arches) <= 1:
            # 型が1つの記事では「型の増減」は意味を持たない（2026-10-28 ハラバリー：同じ型の中の置き換えを片方だけ「型の増減」と書いた）
            judge = ("記事の型の構成に含まれます" if holders else
                     "記事の型では選択技として含まれます" if h["select"] else "記事の型の構成には含まれません")
        lines.append(f"- {name}：{a}%→{b}%（{f['value']:+.1f}pt）。{judge}。")
        sole.append((holders[0] if judge.startswith(f"{holders[0] if holders else ''}だけが持つ") and holders else None, f["value"]))
    # 同じ型「だけが持つ」技が増える行と減る行の両方にあると、「その型の増減を示す」が互いに矛盾する
    # （2026-10-25 ゴリランダー：フルアタ型のドラムアタック+14.2pt ととんぼがえり-9.2pt）。型の中の入れ替わりと書く
    for arch in {a for a, _ in sole if a}:
        signs = {v > 0 for a, v in sole if a == arch}
        if len(signs) == 2:
            old_j = f"{arch}だけが持つため、この変化はその型の増減を示します。"
            new_j = f"{arch}だけが持つ技ですが、同じ型の技に増減が混在するため、型の中での入れ替わりを含みます。"
            lines = [x.replace(old_j, new_j) for x in lines]
    # 全行が「共通のため、型の増減とは言えません」なら、各行は共通の型だけを書き、結論は最後の1行にまとめる
    # （2026-10-25 イエッサン：8行すべて同じ文末で冗長との指摘）
    tail = "のため、型の増減とは言えません。"
    if len(lines) >= 2 and all(x.endswith("共通" + tail) for x in lines):
        lines = [x[: -len(tail)] + "。" for x in lines] + ["- どれも複数の型に共通する変化のため、型の増減とは言えません。"]
    return lines


# ------------------------------------------------------------------ render --

TYPE_IMG = {"ノーマル": "00-normal", "かくとう": "01-fighting", "ひこう": "02-flying", "どく": "03-poison", "じめん": "04-ground",
            "いわ": "05-rock", "むし": "06-bug", "ゴースト": "07-ghost", "はがね": "08-steel", "ほのお": "09-fire", "みず": "10-water",
            "くさ": "11-grass", "でんき": "12-electric", "エスパー": "13-psychic", "こおり": "14-ice", "ドラゴン": "15-dragon",
            "あく": "16-dark", "フェアリー": "17-fairy"}
SKIN_TYPE = {"フェアリースキン": "フェアリー", "スカイスキン": "ひこう", "フリーズスキン": "こおり", "エレキスキン": "でんき"}
MOVE_TABLE_MIN_PCT = 5.0
MOVE_TABLE_MAX_ROWS = 12


# DB（move_master.effect_text）の表記の乱れを技表に出す前に整える（意味は変えない）。2026-10-27 まもるの「見を守る」
EFFECT_FIX = [("見を守る", "身を守る"), ("使ったターン中相手", "使ったターン中、相手"), ("自分のHPのを", "自分のHPを"), ("この技は威力は", "この技の威力は"),
              # 「必ず先制できる」は優先度+2以上の技（しんそく等）がある環境では誤り（2026-10-27 ギルガルドのかげうち）
              ("必ず先制できる", "優先度0の技より先に出せる")]


def _clean_effect(s):
    # DB の効果文の先頭に付く技の分類タグ（「噛み10%の確率で…」）を落とす（2026-10-27 ギャラドス）
    s = re.sub(r"^(噛み|パンチ|波動|切る|弾)(?=[0-9相自場])", "", s)
    s = re.sub(r"^(優先度[+-]\d+)(?=[^。、\s])", r"\1。", s)
    # 「優先度+1。パンチ必ず…。(優先度+1)」：タグの残りと末尾の優先度の重複を落とす（2026-10-27 パーモットのマッハパンチ）
    s = re.sub(r"^(優先度[+-]\d+。)(噛み|パンチ|波動|切る|弾)", r"\1", s)
    m = re.match(r"^(優先度[+-]\d+)。", s)
    if m:
        s = re.sub(r"\s*[(（]" + re.escape(m.group(1)) + r"[)）]\s*$", "", s)
    s = re.sub(r"(\d)ー(\d)", r"\1〜\2", s)
    for a, b in EFFECT_FIX:
        s = s.replace(a, b)
    return s


def render_move_table(facts):
    """主要な技と採用率。備考は DB の効果文そのまま（2026-10-25：手書きの備考に効果の取り違え・確率の欠落が4記事で出た）。"""
    by = _by(facts)
    subj, season = facts["subject"]["name"], facts["subject"]["season"]
    maj = facts["sources"].get("majority_pct", 20)
    power = {f["move"]: f for f in by.get("move_power", [])}
    effect = {f["move"]: _clean_effect(f.get("value") or "") for f in by.get("move_effect", [])}
    # フェアリースキン等の主流特性ではノーマル技のタイプが変わる（2026-10-28 ニンフィアのハイパーボイスが「ノーマル」表示）
    cards = facts.get("cards", [])
    contrary = None
    if cards and all(c.get("mab") == "あまのじゃく" for c in cards if c.get("mab")) and any(c.get("mab") == "あまのじゃく" for c in cards):
        contrary = next(c["label"] for c in cards if c.get("mab") == "あまのじゃく")
    skin = None
    for f in by.get("adopt_rate", []):
        if f["pokemon"] == subj and f.get("category") == "ability" and f.get("season") == season and f["value"] >= 50 and f["name"] in SKIN_TYPE:
            skin = SKIN_TYPE[f["name"]]
    # メガ後の特性がスキン系で、メガ石の採用率がしきい値以上の被写体（2026-10-28 サーナイトのフェアリースキン）
    if not skin:
        mabs = {c.get("mab") for c in facts.get("cards", []) if c.get("mab")}
        if len(mabs) == 1 and next(iter(mabs)) in SKIN_TYPE and _partner_form(by, subj, season, MEGA_STONE_PCT)[0] != subj:
            skin = SKIN_TYPE[next(iter(mabs))]
    rows = sorted(((f["name"], f["value"]) for f in by.get("adopt_rate", [])
                   if f["pokemon"] == subj and f.get("category") == "move" and f.get("season") == season and f["value"] >= MOVE_TABLE_MIN_PCT),
                  key=lambda x: -x[1])[:MOVE_TABLE_MAX_ROWS]
    # 苦手/得意表の判定に使った自分の技は、注記どおり技表で採用率を確かめられるよう必ず載せる（2026-10-28 オーロンゲのパワーウィップ）
    used = {m.get("my_move") for m in by.get("matchup", []) if m.get("representative") and m.get("my_move")}
    # 型カードの固定技も載せる（2026-10-28 ミミロップ：型名の由来のバトンタッチが技表に無かった）
    used |= {mv for c in facts.get("cards", []) for mv in c.get("moves", [])}
    have = {mv for mv, _ in rows}
    extra = sorted(((f["name"], f["value"]) for f in by.get("adopt_rate", [])
                    if f["pokemon"] == subj and f.get("category") == "move" and f.get("season") == season and f["name"] in used and f["name"] not in have),
                   key=lambda x: -x[1])
    rows += extra
    th = '<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:{a}">{t}</th>'
    td = '<td style="padding:8px 12px;border:1px solid #cbd5e1{a}">{t}</td>'
    L = ['<div style="overflow-x:auto;margin:12px 0">', '<table style="width:100%;border-collapse:collapse;font-size:0.92em">',
         '<thead>', '<tr style="background:#f1f5f9">',
         th.format(a="left", t="技名"), th.format(a="center", t="タイプ"), th.format(a="center", t="威力"),
         th.format(a="center", t="採用率"), th.format(a="left", t="効果"), "</tr>", "</thead>", "<tbody>"]
    for i, (mv, rate) in enumerate(rows):
        mp = power.get(mv)
        if not mp:
            continue
        # メガ後があまのじゃくの被写体では、自分の能力を下げる効果が逆に上がる（2026-10-28 ムクホークのインファイト）
        if contrary and re.search(r"自分の.*下が|自分の.*下げ", effect.get(mv, "")):
            effect[mv] = effect[mv] + f"（{contrary}は特性あまのじゃくで逆に上がる）"
        ty = mp.get("type")
        if skin and ty == "ノーマル" and mp.get("value") is not None:
            ty = skin
        img = f'<img src="/images/types/type-{TYPE_IMG[ty]}.png" alt="{ty}" style="width:28px;height:28px;vertical-align:middle">' if ty in TYPE_IMG else (ty or "")
        pw = mp["value"] if mp.get("value") else "—"
        rt = f'<strong style="color:#dc2626">{rate}%</strong>' if rate >= maj else f"{rate}%"
        shade = ' style="background:#fafafa"' if i % 2 == 1 else ""
        L += [f"<tr{shade}>", td.format(a="", t=f"<strong>{mv}</strong>" if rate >= maj else mv), td.format(a=";text-align:center", t=img),
              td.format(a=";text-align:center", t=pw), td.format(a=";text-align:center", t=rt), td.format(a=";font-size:0.95em", t=effect.get(mv, "") or "—"), "</tr>"]
    L += ["</tbody>", "</table>", "</div>"]
    return "\n".join(L)


STAT_JA = {"H": "HP", "A": "こうげき", "B": "ぼうぎょ", "C": "とくこう", "D": "とくぼう", "S": "すばやさ"}


def card_diff_lines(facts, idx):
    """型カードの「他の型との違い」。手書きの強み/弱みは、他の型にも当てはまる内容や他の型より劣る数値を
    強みに書く誤り（J7）が全記事で出た（2026-10-25）ので、型カードどうしの差だけを事実から出す。"""
    by = _by(facts)
    cards = facts.get("cards", [])
    c = cards[idx]
    others = [o for j, o in enumerate(cards) if j != idx]
    item_eff = {f["item"]: f.get("value") for f in by.get("item_effect", [])}
    out = []
    # 他の型の選択技（mpool）にある技も「他の型に無い」には数えない（2026-10-27 ブラッキーのあくび）
    uniq = [m for m in c["moves"] if all(m not in o["moves"] and m not in o.get("mpool", []) for o in others)]
    if uniq:
        out.append(f"- 他の型に無い技：{'・'.join(uniq)}")
    # 他の型では選択技にとどまる技（4技に固定しているのはこの型だけ）。2026-10-27 ライチュウのみがわりが「共通」扱いになった
    semi = [m for m in c["moves"] if m not in uniq and all(m not in o["moves"] for o in others)]
    for m in semi:
        sel = [o["arch"] for o in others if m in o.get("mpool", [])]
        out.append(f"- {m}：この型は必ず持ち、{'・'.join(sel)}では選択技")
    # 固有の技が無い型は、技構成が最も近い型との差を出す（2026-10-27 アローラキュウコンの速攻型・ラグラージの型2/3で差が出なかった）
    if not uniq and not semi and others:
        near = max(others, key=lambda o: (len(set(o["moves"]) & set(c["moves"])), o["item"] == c["item"]))
        mine = [m for m in c["moves"] if m not in near["moves"]]
        theirs = [m for m in near["moves"] if m not in c["moves"]]
        if mine and theirs:
            out.append(f"- {near['arch']}との技の違い：この型は{'・'.join(mine)}、{near['arch']}は{'・'.join(theirs)}")
    if all(o["item"] != c["item"] for o in others):
        eff = item_eff.get(c["item"])
        # メガストーンの効果文（「〜をメガシンカさせる」）は自明なので出さない。括弧内の句点は落とす
        if eff and "ナイト" in c["item"]:
            eff = None
        out.append(f"- 持ち物：{c['item']}" + (f"（{eff.rstrip('。')}）" if eff else ""))
    # メガ進化する型はメガ後の特性に固定されるので、進化前の特性の違いは型の差にならない（2026-10-27 カメックスのあめうけざら）
    if c.get("ability") and not c.get("mab") and all(o.get("ability") != c["ability"] for o in others):
        out.append(f"- 特性：{c['ability']}")
    # こだわりスカーフは対戦中のすばやさが1.5倍。実数値のままだと「最も遅い型」と逆に読める（2026-10-27 サザンドラ）
    def eff(card, st):
        v = (card.get("real_stats") or {}).get(st)
        if v is not None and st == "S" and card.get("item") == "こだわりスカーフ":
            return v * 3 // 2
        return v
    rs = {st: eff(c, st) for st in "HABCDS"}
    hi, lo = [], []
    # 攻撃に使わない側の実数値（特殊技だけの型のこうげき）は型の差として意味が無い（2026-10-28 エンペルト card:4 のこうげき106）
    cat = {f["move"]: f.get("category") for f in by.get("move_power", [])}
    used = {cat.get(m) for m in c["moves"] + c.get("mpool", [])}
    skip = ({"A"} if "physical" not in used else set()) | ({"C"} if "special" not in used else set())
    for st in "HABCDS":
        if st in skip:
            continue
        vals = [eff(o, st) for o in others]
        v = rs.get(st)
        if v is None or any(x is None for x in vals) or not vals:
            continue
        # 同値の型があっても「最も高い/低い側」に入るなら出す（2026-10-27 オオニューラ：速攻型2つが同じSで、何も出なかった）
        allv = vals + [v]
        if max(allv) == min(allv):
            continue
        # 過半数の型が同じ値なら「最も高い/低い」は差にならない（2026-10-28 エンペルト：4型中3型で同じ行が3枚に出た）。
        # 外れた1型の側だけに出す
        if allv.count(v) * 2 >= len(allv) and len(allv) > 2:
            continue
        if v == max(allv):
            scarf = "（こだわりスカーフ込み）" if st == "S" and c.get("item") == "こだわりスカーフ" else ""
            hi.append(f"{STAT_JA[st]}{v}{scarf}" + ("（同じ値の型あり）" if v in vals else ""))
        elif v == min(allv):
            lo.append(f"{STAT_JA[st]}{v}" + ("（同じ値の型あり）" if v in vals else ""))
    n = len(cards)
    # ギルガルドの実数値はシールドフォルム（2026-10-27 レビュー：攻撃時のブレードフォルムと取り違える）
    form = "（シールドフォルム）" if facts["subject"]["name"] == "ギルガルド" else ""
    # 型が2つなら「最も」ではなく「もう一方の型より」（2026-10-28 オーロンゲ）
    hi_lbl = "もう一方の型より高い実数値" if n == 2 else f"{n}つの型で最も高い実数値"
    lo_lbl = "もう一方の型より低い実数値" if n == 2 else f"{n}つの型で最も低い実数値"
    if hi:
        out.append(f"- {hi_lbl}{form}：{'・'.join(hi)}")
    if lo:
        out.append(f"- {lo_lbl}{form}：{'・'.join(lo)}")
    if not out:
        out.append("- 4つの技・持ち物・実数値のどれにも、他の型に無い要素はありません")
    return out


TYPE_ORDER = ["ノーマル", "ほのお", "みず", "でんき", "くさ", "こおり", "かくとう", "どく", "じめん", "ひこう", "エスパー", "むし",
              "いわ", "ゴースト", "ドラゴン", "あく", "はがね", "フェアリー"]


def _type_lines(by, forms):
    """形態ごとの（弱点, 受けられるタイプ）。形態間で同じなら1つにまとめる。"""
    res = []
    for fm in forms:
        eff = {f["atk_type"]: f["value"] for f in by.get("type_eff", []) if f.get("defender") == fm}
        if len(eff) < 18:
            continue
        weak = "・".join([f"{k}（×4）" for k in TYPE_ORDER if eff[k] == 4] + [k for k in TYPE_ORDER if eff[k] == 2]) or "なし"
        res_t = [k for k in TYPE_ORDER if 0 < eff[k] < 1]
        imm = [k for k in TYPE_ORDER if eff[k] == 0]
        guard = "・".join(res_t) + "を半減以下" if res_t else ""
        if imm:
            guard += ("、" if guard else "") + "・".join(imm) + "を無効"
        res.append((fm, weak, guard or "半減以下で受けられるタイプなし"))
    if len({(w, g) for _, w, g in res}) == 1:
        return [("", res[0][1], res[0][2])]
    return res


def _top_opps(by, verdict, n=3):
    rank_of = {f["pokemon"]: f["value"] for f in by.get("usage_rank", []) if not f.get("season")}
    reps = {m["opp"]: m for m in by.get("matchup", []) if m["representative"]}
    vs = sorted((v for v in by.get("verdict", []) if v["value"] == verdict and v["opp"] in reps),
                key=lambda v: rank_of.get(v["opp_sp"], 9999))
    return [(v["opp"], rank_of.get(v["opp_sp"]), reps[v["opp"]]) for v in vs[:n]]


def _by_move(top, key):
    """同じ技で決まる相手をまとめる：「A（1位）・B（3位）をじしん」"""
    groups = {}
    for o, r, m in top:
        groups.setdefault(m[key] or "有効な攻撃技なし", []).append(f"{o}（{r}位）")
    return groups


def _card_point(line):
    """card_diff の1行目を、まとめの1文に直す。"""
    s = line[2:]
    s = re.sub(r"^(.+?)との技の違い：この型は(.+?)、\1は(.+)$", r"\1の\3の代わりに\2を持つ", s)
    s = re.sub(r"^(他の型に無い[^：]+)：", r"\1は", s)
    s = re.sub(r"^([^：]+)：この型は必ず持ち、(.+)では選択技$", r"\1を必ず持つ（\2では選択技）", s)
    s = re.sub(r"^([^：]+)：", r"\1は", s)
    return s


def summary_lines(facts, weak_n, strong_n, has_arch_grid=True):
    """まとめ：強み・弱み・型の選び分け・前季からの変化の要点を、事実ファイルだけから組み立てる。
    2026-10-25：手書きのまとめは型カードの写し・誤った一般化で毎回 FAIL したので生成に置換。
    2026-10-28：順位・型名・苦手得意の数だけでは「何の役にも立たない」（ユーザー）ので、表の上位の相手と決め手の技、
    タイプ相性、型ごとの違い、採用率の大きな変化を要点として出す"""
    by = _by(facts)
    subj = facts["subject"]["name"]
    prev = facts["sources"].get("prev_season")
    now = next((f["value"] for f in by.get("usage_rank", []) if f["pokemon"] == subj and not f.get("season")), None)
    was = next((f["value"] for f in by.get("usage_rank", []) if f["pokemon"] == subj and f.get("season") == prev), None)
    cards = facts.get("cards", [])
    forms = [subj] + [f for f in (facts["subject"].get("forms") or []) if f != subj]
    tl = _type_lines(by, forms)
    out = ["**強み**", ""]
    top = _top_opps(by, "win")
    if top:
        g = _by_move(top, "my_move")
        out.append(f"- 得意な相手は{strong_n}体です。使用率上位では、" + "、".join("・".join(os_) + f"に{mv}" for mv, os_ in g.items()) + "で勝てます。")
    else:
        out.append("- 1対1で得意と判定できた相手はいません。")
    out += [f"- タイプ相性では、{fm + 'は' if fm else ''}{g}" + ("で受けられます。" if "なし" not in g else "。") for fm, _, g in tl]
    out += ["", "**弱み**", ""]
    top = _top_opps(by, "lose")
    if top:
        g = _by_move(top, "opp_move")
        out.append(f"- 苦手な相手は{weak_n}体です。使用率上位では、" + "、".join("・".join(os_) + f"の{mv}" for mv, os_ in g.items()) + "で先に倒されます。")
    else:
        out.append("- 1対1で苦手と判定された相手はいません。")
    out += [f"- {fm + 'の' if fm else ''}弱点は{w}です。" for fm, w, _ in tl]
    if len(cards) >= 2:
        out += ["", "**型の選び分け**", ""]
        for i, c in enumerate(cards):
            first = next((l for l in card_diff_lines(facts, i) if l.startswith("- ")), None)
            if first:
                out.append(f"- 「{c['arch']}」：{_card_point(first)}。")
        out.append("- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。" if has_arch_grid
                   else "- 苦手/得意の判定は、どの型でも同じです。")
    out += ["", f"**{prev}からの変化**" if prev else "**使用率**", ""]
    if now is not None:
        out.append(f"- 使用率は{now}位です" + (f"（{prev}: {was}位）。" if was is not None else "。"))
    movers = sorted((f for f in by.get("adopt_rate_diff", []) if f["pokemon"] == subj and f["category"] in ("move", "item")),
                    key=lambda f: -abs(f["value"]))[:3]
    if movers and prev:
        out.append("- 採用率の変化が大きいのは" + "・".join(f"{f['name']}（{f['value']:+.1f}pt）" for f in movers) + "です。")
    return out


STAT_ROWS = [("H", "HP", "#f472b6,#db2777"), ("A", "こうげき", "#fb923c,#ea580c"), ("B", "ぼうぎょ", "#60a5fa,#2563eb"),
             ("C", "とくこう", "#c084fc,#7c3aed"), ("D", "とくぼう", "#34d399,#059669"), ("S", "すばやさ", "#fbbf24,#d97706")]
_ROW = '  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">'
_NUM = '<span style="width:32px;text-align:right">{}</span>'


def _stat_chart(base, mega=None):
    """種族値バー。メガ形があれば 通常/メガ後/差分 の3列（増加分は同色の薄いバー、減少分は赤いバー）。
    2026-10-28：記事ごとに手書きで色・幅・増減の表し方がばらばらだった（アブソルは増加分が緑）。ガブリアス記事の書式に統一"""
    L = ['<div style="max-width:480px;margin:16px 0;font-size:0.9em">']
    if mega:
        L += ['  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">',
              '    <span style="width:72px;min-width:72px"></span>', '    <div style="flex:1"></div>',
              '    <span style="width:32px;text-align:right">通常</span>', '    <span style="width:32px;text-align:right">メガ後</span>',
              '    <span style="width:40px;text-align:right">差分</span>', '  </div>']
    for k, label, col in STAT_ROWS:
        b = base[k]
        m = mega[k] if mega else b
        grad = f"linear-gradient(90deg,{col})"
        L += [_ROW, f'    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">{label}</span>']
        if m == b:
            L += ['    <div style="flex:1;background:#eee;border-radius:4px;height:12px">',
                  f'      <div style="width:{b / 2:g}%;background:{grad};height:12px;border-radius:4px"></div>', '    </div>']
        else:
            lo, hi = min(b, m), max(b, m)
            extra = f"background:{grad};height:12px;opacity:0.35" if m > b else "background:#dc2626;height:12px"
            L += ['    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">',
                  f'      <div style="width:{lo / 2:g}%;background:{grad};height:12px"></div>',
                  f'      <div style="width:{(hi - lo) / 2:g}%;{extra}"></div>', '    </div>']
        if not mega:
            L.append("    " + _NUM.format(b))
        elif m == b:
            L.append("    " + _NUM.format(b) + _NUM.format(m) + '<span style="width:40px"></span>')
        else:
            mv = f'<strong style="color:#dc2626">{m}</strong>' if m > b else str(m)
            dc = "#059669" if m > b else "#dc2626"
            L.append("    " + _NUM.format(b) + _NUM.format(mv)
                     + f'<span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:{dc}">{m - b:+d}</span>')
        L.append("  </div>")
    tb = sum(base[k] for k, _, _ in STAT_ROWS)
    tot = '<span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">{}</span>'
    L += ['  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">',
          '    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>', '    <div style="flex:1"></div>']
    if mega:
        tm = sum(mega[k] for k, _, _ in STAT_ROWS)
        d = (f'<span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">{tm - tb:+d}</span>'
             if tm != tb else '<span style="width:40px"></span>')
        L.append("    " + tot.format(tb) + tot.format(tm) + d)
    else:
        L.append("    " + tot.format(tb))
    L += ["  </div>", "</div>"]
    return "\n".join(L)


def render_base_stats(facts):
    """「### 種族値」見出しと種族値バー（メガ形ごとに1つ）。"""
    bs = {}
    for f in facts["facts"]:
        if f["kind"] == "base_stat":
            bs.setdefault(f["pokemon"], {})[f["stat"]] = f["value"]
    subj = facts["subject"]["name"]
    megas = [m for m in facts["subject"].get("forms", []) if m != subj and m.startswith("メガ") and len(bs.get(m, {})) == 6]
    if len(bs.get(subj, {})) != 6:
        return ""
    stone = {f["form"]: f["stone"] for f in facts["facts"] if f["kind"] == "mega_form"}
    items = [c.get("item") for c in facts.get("cards", [])]
    megas.sort(key=lambda m: items.index(stone[m]) if stone.get(m) in items else len(items))
    if not megas:
        return "### 種族値\n\n" + _stat_chart(bs[subj])
    if len(megas) == 1:
        return f"### 種族値（通常→{megas[0]}）\n\n" + _stat_chart(bs[subj], bs[megas[0]])
    parts = [f"### 種族値（通常→{'／'.join(megas)}）"]
    for m in megas:
        parts.append(f'<p style="margin:12px 0 0;font-size:0.85em;font-weight:600;color:#555">通常→{m}</p>\n\n' + _stat_chart(bs[subj], bs[m]))
    return "\n\n".join(parts)


def render_all(facts):
    out = {}
    out["base_stats"] = render_base_stats(facts)
    r = RR.render(facts)
    out["weak"], out["strong"] = r["weak"], r["strong"]
    arch_grid = render_arch_grid(facts)
    out["summary"] = "\n".join(summary_lines(facts, len(r["weak_names"]), len(r["strong_names"]), bool(arch_grid.strip())))
    out["move_table"] = render_move_table(facts)
    cards = facts.get("cards", [])
    if len(cards) >= 2:
        for i in range(len(cards)):
            out[f"card:{i + 1}"] = "**他の型との違い:**\n\n" + "\n".join(card_diff_lines(facts, i))
    out["arch_grid"] = arch_grid
    out["partner_grid"] = render_partner_grid(facts)
    out["diff_movers"] = "\n".join(diff_movers(facts))
    for k, v in out.items():
        if "None" in v:
            raise ValueError(f"render_sections: ブロック {k} に None が紛れ込んだ（facts 側の値不足）")
    return out


ORDER_NOTE = {
    "base_stats": "「## ◯◯の基本スペック」見出しの直後（「### 種族値」見出しと種族値バーを含む。手書きの種族値バーは置かない）",
    "weak": "苦手なポケモン表の <tbody> 内",
    "strong": "得意なポケモン表の <tbody> 内",
    "arch_grid": "型カード群（最後の型の --- ）の直後に「### 型による有利不利の違い」の見出しを付けて貼る",
    "partner_grid": "同居率セクションの <div class=\"partner-grid\">…</div> の直後",
    "diff_movers": "データ分析セクションの採用率比較表の直後",
    "move_table": "「## 主要な技と採用率」見出しの直後（手書きの技表は置かない）",
    "summary": "「## まとめ」見出しの直後（書き手の本文はこのブロックの後に結論1〜2文だけ）",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--facts", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    facts = json.loads(Path(args.facts).read_text(encoding="utf-8"))
    sha = RR.facts_sha1(args.facts)
    blocks = render_all(facts)
    parts = []
    for bid, html in blocks.items():
        if not html.strip():
            continue
        note = ORDER_NOTE.get(bid) or (f"型{bid.split(':')[1]}のカード（型カードの説明文の後、その型の --- の直前）。手書きの強み/弱みは置かない" if bid.startswith("card:") else bid)
        parts.append(f"<!-- 貼る位置: {note} -->\n" + RR.wrap(bid, html, sha))
    out = "\n\n".join(parts) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        sizes = {k: v.count("\n") + 1 if v else 0 for k, v in blocks.items()}
        print(f"[render_sections] {sizes} -> {args.out}")
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
