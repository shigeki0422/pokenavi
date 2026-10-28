#!/usr/bin/env python3
"""事実ファイルから苦手/得意表の <tr> 行を定型文で生成する。LLMは表の数値を一切書かない。

出力は2ブロック（マーカーで囲む。article_gate.py が逐語比較する）:
  <!-- gate:rows start id=weak facts=<facts.jsonのsha1> --> … <!-- gate:rows end id=weak -->
  <!-- gate:rows start id=strong facts=… --> … <!-- gate:rows end id=strong -->

理由列は記事レビュー.md 観点18e の定型のみ：
  S1 = "{自分の型}の{技}（採用率X%）は{確定N発|乱数N発（P%）|倒しきれません}{要因}。"
  S2 = "{相手}の{技}（採用率X%）は{同上}{要因}で、{先手/後手/同速/優先度}{のため先に倒せます|のため先に倒されます}。"
これ以外の表現は不可。言いたいことがあれば表の外の本文に書く。

使い方:
  python3 scripts/render_matchup_rows.py --facts _local/article_facts/<slug>.json [--out <slug>.rows.html]
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

TD = '<td style="padding:8px 12px;border:1px solid #cbd5e1">'
TD_C = '<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">'
IMG = '<img src="/images/pokemon/pokemon-{icon}.webp" alt="{label}" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">'
OUT_OF_RANGE = 999


def facts_sha1(path_or_facts):
    """事実ファイルの内容ハッシュ。generated_at は含めない（再生成しただけで行が古扱いにならないように）。"""
    facts = path_or_facts if isinstance(path_or_facts, dict) else json.loads(Path(path_or_facts).read_text(encoding="utf-8"))
    body = {k: v for k, v in facts.items() if k != "generated_at"}
    return hashlib.sha1(json.dumps(body, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def _index(facts):
    by = {}
    for f in facts["facts"]:
        by.setdefault(f["kind"], []).append(f)
    return by


def ko_text(certain, hits, prob_int, eff=None):
    if hits is None or hits >= OUT_OF_RANGE:
        # タイプ相性で無効(0倍)なら「倒しきれません」は不正確（ダメージが入るように読めてしまう）。
        # エンジン側はダメージ計算そのものをしない無効技でeffをNoneのまま返すことがあるため、
        # 0とNoneの両方を「無効」として扱う（通常の「倒しきれない」ケースではeffは必ず数値が入る）。
        return "無効" if eff == 0 or eff is None else "倒しきれません"
    if certain:
        return f"確定{hits}発"
    p = prob_int if prob_int is not None else "?"
    return f"乱数{hits}発（{p}%）"


def why_text(reason, holder=""):
    """holder＝受ける側（持ち物の持ち主）。2026-10-25「メガフラエッテのムーンフォースは確定2発（きあいのタスキで…）」
    がフラエッテ側のタスキに読めた（実際は受けるガブリアス側）ため、持ち物は持ち主を書く。特性（ばけのかわ等）は
    種で決まり取り違えないので持ち主を書かない。セル100字に収めるため「〜込み」で統一する。"""
    if not reason:
        return ""
    who = f"{holder}の" if holder else ""
    for item in ("きあいのタスキ", "オボンのみ", "たべのこし", "オレンのみ"):
        if item in reason:
            return f"（{who}{item}込み）"
    for ab in ("ばけのかわ", "がんじょう", "マルチスケイル", "ファントムガード"):
        if ab in reason:
            return f"（{ab}込み）"
    return f"（{reason}）"


# 場の状態で優先度が変わる技：{技: (優先度, 文頭の条件)}。根拠 scripts/rust_engine/engine/src/battle.rs:L336
COND_PRIORITY = {"グラススライダー": (1, "グラスフィールドで")}


def order_outcome_text(m, my_moves=None, speed_notes=True):
    """先後と結果を、その組み合わせで論理的に成り立つ文で返す。
    「先手のため先に倒されます」のような、先後が結果の理由にならない文を作らない。"""
    win = m["win"]
    my_h = m.get("my_hits") if m.get("my_hits") is not None else OUT_OF_RANGE
    opp_h = m.get("opp_hits") if m.get("opp_hits") is not None else OUT_OF_RANGE
    if m["ko_by_priority"]:
        # 表示技（最大打点）に優先度が無くても、決着の技（my_ko_move/opp_ko_move。dump_matchups_facts.ts が race から出す）
        # に優先度があればそれを使う。2026-10-18: ミミッキュ vs ゲンガーで、かげうち(+1)で決着しているのに表示技
        # シャドークロー(0)しか見ず「確定数どおりに先に倒せます」と誤生成していた。
        my_pm, my_pn = m.get("my_move_prio") or 0, m["my_move"]
        if not my_pm and (m.get("my_ko_move_prio") or 0):
            my_pm, my_pn = m["my_ko_move_prio"], m["my_ko_move"]
        op_pm, op_pn = m.get("opp_move_prio") or 0, m["opp_move"]
        if not op_pm and (m.get("opp_ko_move_prio") or 0):
            op_pm, op_pn = m["opp_ko_move_prio"], m["opp_ko_move"]
        # 場の状態で優先度が変わる技（技表の優先度は0）。2026-10-25 ゴリランダーのグラススライダーで例外停止していた
        my_cond = op_cond = ""
        if not my_pm:
            for nm in (m.get("my_ko_move"), m["my_move"]):
                if nm in COND_PRIORITY:
                    my_pm, my_pn, my_cond = COND_PRIORITY[nm][0], nm, COND_PRIORITY[nm][1]
                    break
        if not op_pm:
            for nm in (m.get("opp_ko_move"), m["opp_move"]):
                if nm in COND_PRIORITY:
                    op_pm, op_pn, op_cond = COND_PRIORITY[nm][0], nm, COND_PRIORITY[nm][1]
                    break
        # 確定数は同じセルの前半で表示技について書いているので、ここで「（確定数は○○）」を重ねない（2026-10-25 重複の指摘）
        my_note = op_note = ""
        # 決着の技が確定数を書いた技と違うときは「最後は〜で」と書き、どの技で先に動くかを取り違えさせない
        # （2026-10-25「シャドークローは確定2発…かげうちで先に動き」が同じ技の話に読めた）
        if win and my_pm > 0:
            if my_pn != m["my_move"]:
                sel = "選択技" if my_moves is not None and my_pn not in my_moves else ""
                return f"最後は{my_cond}優先度{my_pm:+d}の{sel}{my_pn}で先に倒せます"
            return f"{my_cond}優先度{my_pm:+d}の{my_pn}で先に動き、先に倒せます{my_note}"
        if not win and op_pm > 0:
            if op_pn != m["opp_move"]:
                return f"最後は{op_cond}優先度{op_pm:+d}の{op_pn}で先に倒されます"
            return f"{op_cond}優先度{op_pm:+d}の{op_pn}で先に動かれ、先に倒されます{op_note}"
        if win and op_pm < 0:
            return f"相手の{op_pn}は優先度{op_pm:+d}のため後手になり、先に倒せます"
        if not win and my_pm < 0:
            return f"{my_pn}は優先度{my_pm:+d}のため後手になり、先に倒されます"
        if "my_ko_move" not in m:
            pass  # 旧 facts（決め技フィールドが無い）は従来の素早さ文に落とす
        elif (not win and my_pm > 0) or (win and op_pm > 0):
            # 負けた側だけが先制技を持つ行（2026-10-28 ジュペッタのかげうち vs カバルドン）。優先度は決着の理由に
            # ならないので素早さの文に落とす（ここで止めると記事が書けない）
            pass
        else:
            raise ValueError(f"ko_by_priority なのに優先度のある技が無い: my={my_pn}({my_pm}) opp={op_pn}({op_pm})")
    # エンジンの koByPriority は ko_first≠fast のときしか立たず、速い側が先制技で倒された行が素早さ文に落ちて
    # 「S177対S162で先手を取れますが…先に倒されます」と書いていた（2026-10-27 アローラキュウコン vs メガメタグロスのバレットパンチ）
    # 遅い側が先制技で倒された行も、素早さではなく優先度で書く（2026-10-28 ガラルヤドキング vs ミミッキュのかげうち）
    if not win:
        pm, pn = m.get("opp_ko_move_prio") or 0, m.get("opp_ko_move")
        if pn and pm > max(m.get("my_move_prio") or 0, m.get("my_ko_move_prio") or 0):
            if pn != m["opp_move"]:
                return f"最後は優先度{pm:+d}の{pn}で先に倒されます"
            return f"優先度{pm:+d}の{pn}で先に動かれ、先に倒されます"
    if win:
        pm, pn = m.get("my_ko_move_prio") or 0, m.get("my_ko_move")
        if pn and pm > max(m.get("opp_move_prio") or 0, m.get("opp_ko_move_prio") or 0):
            if pn != m["my_move"]:
                sel = "選択技" if my_moves is not None and pn not in my_moves else ""
                return f"最後は優先度{pm:+d}の{sel}{pn}で先に倒せます"
            return f"優先度{pm:+d}の{pn}で先に動き、先に倒せます"
    # 対戦中に素早さを下げられた値（がんせきふうじ等）が出ると、型カードの実数値と食い違って見える（2026-10-25
    # カバルドンS44・リザードンS80）。実数値より低いときは「低下後」と明記する
    # 積み技・特性で上がった値（からをやぶる後のS260、かるわざ後のS344）も実数値と食い違って見える（2026-10-27 カメックス・フラエッテ）
    def _chg(s, base, item):
        if not speed_notes or not base or s == base:
            return ""
        if s < base:
            return "（低下後）"
        return "（スカーフ込み）" if item == "こだわりスカーフ" and s == base * 3 // 2 else "（上昇後）"
    # 変化前の実数値でも先後が同じなら変化前の値を出す（2026-10-28 ヒスイゾロアーク vs ライチュウ：でんじほうのまひ後の
    # S89 を出し、最初の行動順 S178対S200 と食い違って見えた）。こだわりスカーフは持ち物の値なのでそのまま
    mb, ob = m.get("my_base_s"), m.get("opp_base_s")
    if mb and ob and mb != ob and (mb > ob) == (m["my_s"] > m["opp_s"]) and m["my_s"] != m["opp_s"]:
        if m.get("my_item") != "こだわりスカーフ":
            m = {**m, "my_s": mb}
        if m.get("opp_item") != "こだわりスカーフ":
            m = {**m, "opp_s": ob}
    my_low = _chg(m["my_s"], m.get("my_base_s"), m.get("my_item"))
    op_low = _chg(m["opp_s"], m.get("opp_base_s"), m.get("opp_item"))
    s = f"S{m['my_s']}{my_low}対S{m['opp_s']}{op_low}"
    if m["my_s"] == m["opp_s"]:
        if win:
            return f"同速（S{m['my_s']}）ですが確定数で上回り、先に倒せます"
        if my_h > opp_h:
            return f"同速（S{m['my_s']}）で確定数も下回るため、先に倒されます"
        return f"同速（S{m['my_s']}）のため先後は運次第で、勝ち切れません"
    if win and m["fast"]:
        return f"{s}で先手を取り、先に倒せます"
    if win and not m["fast"]:
        # 相手が倒しきれない(opp_h=OUT_OF_RANGE)場合、s1/s2側に既に「倒しきれないため」と出ているので、
        # ここでさらに「確定数で上回り」と比較級を重ねない（比較対象が無いのに比較しているように読める）。
        if opp_h >= OUT_OF_RANGE:
            return f"{s}で後手ですが、先に倒せます"
        # 後手でも勝つ場合、確定数が相手より少ない（上回る）とは限らない（確定数が同じでも、
        # 相打ち・乱数のズレ等で先に倒せることがある）。成り立たない比較級を使わない。
        if my_h < opp_h:
            return f"{s}で後手ですが確定数で上回り、先に倒せます"
        return f"{s}で後手ですが、確定数どおりに先に倒せます"
    if not win and m["fast"]:
        # 自分が倒しきれない(my_h=OUT_OF_RANGE)場合も、s1側に既に「倒しきれない」と出ているので重ねない。
        if my_h >= OUT_OF_RANGE:
            return f"{s}で先手を取りますが、先に倒されます"
        # 先手でも負ける場合、確定数が相手より多い（下回る）とは限らない。
        if my_h > opp_h:
            return f"{s}で先手を取れますが確定数で下回り、先に倒されます"
        # 確定数が同じ/有利なのに先手で負けるケース：なぜ負けるかの正確な理由（技の自己デバフ・
        # 行動順の内部計算等）はこの事実セットからは特定できないため、不確かな理由を書かない。
        # 「確定数どおりには進まない」という事実だけを書く（2026-10-17: マルチスケイル等の特性を
        # 理由として書いたところ、確定数の算出自体がその特性を織り込み済みのはずで論理矛盾になった）。
        return f"{s}で先手を取りますが、確定数どおりには進まず、先に倒されます"
    # 自分が倒しきれない行で「後手のため」と書くと、素早さが負けの理由に読める（2026-10-28 ウツボット vs ブリジュラス）
    if my_h >= OUT_OF_RANGE:
        return f"{s}で後手になり、先に倒されます"
    return f"{s}で後手のため、先に倒されます"


def rate_clause(rate, prefix="", minority_pct=None):
    """採用率の括弧書き。事実が無い(None)技は「採用率」自体を主張しない（空文字を返す）。
    minority_pct 未満の技は「少数派」と添える（2026-10-25 採用率19.0%の技が相手の主力技に見えるとの指摘）。"""
    if rate is None:
        return ""
    tag = "・少数派" if minority_pct is not None and rate < minority_pct else ""
    return f"（{prefix}採用率{rate}%{tag}）"


NOTE_ROW = ('<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">'
            '※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。'
            '「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>')
SELECT_NOTE = '「選択技」は型の4技には無いが、その型で採用されることがある技。'
TR_NOTE = '先後はトリックルームを使わない場合の判定。'


def reason_cell(rep, others, item_rate, card_moves=None, subj="", minority_pct=None):
    """理由セル（2文・100字目安）。2026-10-18 圧縮：代表個体の注記・種全体の接頭辞・持ち物違い個体の確定数・
    自分の技の採用率を全部セルから外し、表の最終行の注記（NOTE_ROW）1行に寄せた。これらは個々のレビュー
    指摘への開示として足されたもので、積み上がった結果セルが150〜200字になり「表が長い」と指摘された。"""
    card_moves = card_moves or {}
    if rep.get("my_move") is None:
        # 有効な攻撃技が無い（相手の特性・タイプで手持ちの技が軒並み通らない等）。技名を主語にできないので書き方を変える。
        s1 = f"{rep['my_arch']}には有効な攻撃技が無く、倒しきれません。"
    else:
        my_defined = card_moves.get(rep["my_arch"])
        # mpool の候補技をエンジンが選んだ場合、カードの技構成と矛盾して見えないよう「選択技」と明記する
        my_label = f"{rep['my_arch']}の選択技{rep['my_move']}" if my_defined is not None and rep["my_move"] not in my_defined \
            else f"{rep['my_arch']}の{rep['my_move']}"
        s1_ko = f"{my_label}は{ko_text(rep['my_certain'], rep['my_hits'], rep.get('my_prob_int'), rep.get('my_eff'))}"
        s1 = f"{s1_ko}{why_text(rep['my_reason'], '相手')}。"
    opp_ko = ko_text(rep["opp_certain"], rep["opp_hits"], rep.get("opp_prob_int"), rep.get("opp_eff"))
    # 「倒しきれませんで、」は動詞の打ち切り方が連体形的に続かず不自然なので、この場合だけ接続を変える
    # 「倒しきれないため、S..で先手を取り」は倒しきれないことが先手の理由に読める（2026-10-28 ラウドボーン）
    opp_clause = "倒しきれず、" if opp_ko == "倒しきれません" else f"{opp_ko}{why_text(rep['opp_reason'], subj)}で、"
    s2 = f"{rep['opp_label']}の{rep['opp_move']}{rate_clause(rep['opp_move_rate'], minority_pct=minority_pct)}は{opp_clause}{order_outcome_text(rep, card_moves.get(rep.get('my_arch')))}"
    cell = s1 + s2 + "。"
    # セルは100字まで（article_style.MAX_CELL_CHARS）。超えるときは自分側の持ち物・特性の注記を落とす
    # （確定数そのものは注記込みの値なので、落としても結果は変わらない）。
    if len(cell) > 100 and rep.get("my_move") is not None:
        cell = f"{s1_ko}。" + s2 + "。"
    if len(cell) > 100 and opp_ko != "倒しきれません":
        # それでも超えるときは相手側の注記も落とす（2026-10-25 セグレイブ 110字）
        s2_bare = f"{rep['opp_label']}の{rep['opp_move']}{rate_clause(rep['opp_move_rate'], minority_pct=minority_pct)}は{opp_ko}で、{order_outcome_text(rep, card_moves.get(rep.get('my_arch')))}"
        head = f"{s1_ko}。" if rep.get("my_move") is not None else s1
        cell = head + s2_bare + "。"
    if len(cell) > 100:
        # 最後に素早さの注記（スカーフ込み・上昇後・低下後）を落とす（2026-10-27 注記追加で 101〜103字）
        cell = cell.replace(order_outcome_text(rep, card_moves.get(rep.get('my_arch'))),
                            order_outcome_text(rep, card_moves.get(rep.get('my_arch')), speed_notes=False))
    # 安全網：facts側の値がNone/未知のまま文字列化されて紛れ込んだら、黙って出さずに例外で止める
    # （None%・選択技None のような事例が実際に起きたため。次に同種の漏れがあっても publish 前に気づけるようにする）。
    if "None" in cell:
        raise ValueError(f"reason_cell に None が紛れ込みました（facts側の値不足）: {cell}")
    return cell


def render(facts):
    by = _index(facts)
    season = facts["subject"]["season"]
    card_moves = {c["arch"]: set(c["moves"]) for c in facts.get("cards", []) if c.get("arch") and c.get("moves")}
    card_s = {c["arch"]: (c.get("real_stats") or {}).get("S") for c in facts.get("cards", [])}
    rank_of = {f["pokemon"]: f["value"] for f in by.get("usage_rank", []) if not f.get("season")}
    item_rate = {}
    for f in by.get("adopt_rate", []):
        if f["category"] == "item" and f["season"] == season:
            item_rate.setdefault(f["pokemon"], {})[f["name"]] = f["value"]
    rows_by_opp = {}
    for m in by.get("matchup", []):
        rows_by_opp.setdefault(m["opp"], []).append(m)
    blocks = {"weak": [], "strong": []}
    names = {"weak": [], "strong": []}
    verdicts = [v for v in by.get("verdict", []) if v["value"] in ("win", "lose")]
    verdicts.sort(key=lambda v: rank_of.get(v["opp_sp"], 9999))
    for v in verdicts:
        rows = rows_by_opp.get(v["opp"], [])
        rep = next((m for m in rows if m["representative"]), None)
        if rep is None:
            continue
        key = "strong" if v["value"] == "win" else "weak"
        rank = rank_of.get(v["opp_sp"])
        if v.get("stone"):
            rate = item_rate.get(v["opp_sp"], {}).get(v["stone"])
            rank_cell = f"{rank}位（{v['stone']}{rate}%）"
        else:
            rank_cell = f"{rank}位"
        shade = ' style="background:#fafafa"' if len(blocks[key]) % 2 == 1 else ""
        rep = dict(rep, my_base_s=card_s.get(rep["my_arch"]),
                   opp_base_s=(rep.get("opp_stats") or [None] * 6)[5])
        cell = reason_cell(rep, [m for m in rows if not m["representative"]], item_rate.get(v["opp_sp"], {}), card_moves,
                           subj=facts["subject"]["name"], minority_pct=facts.get("sources", {}).get("majority_pct"))
        blocks[key].append(
            f"<tr{shade}>\n"
            f"  {TD}\n    {IMG.format(icon=rep['opp_icon'], label=v['opp'])}{v['opp']}"
            # 理由文はメガ形態などの代表個体で書くので、名前の列にも判定した個体を添える（2026-10-27 表記の食い違いの指摘）
            + (f"<br><span style=\"font-size:0.8em;color:#64748b\">{rep['opp_label']}で判定</span>" if rep.get("opp_label") and rep["opp_label"] != v["opp"] else "")
            + "\n  </td>\n"
            f"  {TD_C}{rank_cell}</td>\n"
            f"  {TD}{cell}</td>\n"
            f"</tr>"
        )
        names[key].append(v["opp"])
    for key in blocks:
        if blocks[key]:
            # 表に「選択技」が無ければその説明は出さない（2026-10-25 該当行が無い説明はノイズとの指摘）
            note = NOTE_ROW if any("選択技" in r for r in blocks[key]) else NOTE_ROW.replace(SELECT_NOTE, "")
            # 1対1の判定（analysis.rs）はトリックルームを使わない。トリックルームを型の技に持つ被写体で、
            # 「S49対S148で後手」がトリックルーム下の先後と食い違って読める（2026-10-28 ブリムオン）
            if any("トリックルーム" in c.get("moves", []) for c in facts.get("cards", [])):
                note = note.replace("</td></tr>", TR_NOTE + "</td></tr>")
            blocks[key].append(note)
    return {"weak": "\n".join(blocks["weak"]), "strong": "\n".join(blocks["strong"]),
            "weak_names": names["weak"], "strong_names": names["strong"]}


def wrap(block_id, html, sha):
    return f"<!-- gate:rows start id={block_id} facts={sha} -->\n{html}\n<!-- gate:rows end id={block_id} -->"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--facts", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    facts = json.loads(Path(args.facts).read_text(encoding="utf-8"))
    sha = facts_sha1(args.facts)
    r = render(facts)
    out = wrap("weak", r["weak"], sha) + "\n\n" + wrap("strong", r["strong"], sha) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf-8")
        print(f"[render_matchup_rows] weak={len(r['weak_names'])} {r['weak_names']} / strong={len(r['strong_names'])} {r['strong_names']} -> {args.out}")
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
