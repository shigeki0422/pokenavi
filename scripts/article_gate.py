#!/usr/bin/env python3
"""記事の公開ゲート（決定論的）。記事中の全数値が事実ファイルに存在するかを機械的に判定する。

exit 0 = PASS / 1 = FAIL / 2 = 入出力エラー

チェック:
  numbers … 全数値主張（article_claims）を事実ファイルと照合。候補0件 → FAIL(no_fact)
  rows    … <!-- gate:rows --> 区間が render_matchup_rows の出力と逐語一致し、事実ハッシュが最新か
  style   … article_style の検出（同一行の gate:allow マーカーで許可可）
  dates   … 「データは YYYY-MM-DD 時点」が detail_date と一致
  publish … draft:false なら pubDate==today・heroImage 実在・slugの季節
  names   … DBに実在するが事実ファイルに無いポケモン名 → WARN
  counts  … 「以下のN体」と表の行数

許可マーカー（同一行のHTMLコメント）: <!-- gate:allow <raw> reason="…" --> / <!-- gate:allow style reason="…" -->

使い方:
  python3 scripts/article_gate.py src/content/blog/<slug>.md --facts _local/article_facts/<slug>.json [--today YYYY-MM-DD] [--report out.json] [--strict] [--slug <slug>]
"""
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import article_claims as AC  # noqa: E402
import article_style as AS  # noqa: E402

STAT_WORD = {"HP": "H", "こうげき": "A", "ぼうぎょ": "B", "とくこう": "C", "とくぼう": "D", "すばやさ": "S"}
STAT_LETTERS = ["H", "A", "B", "C", "D", "S"]


class Ctx:
    def __init__(self, facts):
        self.facts = facts
        self.by = {}
        for f in facts["facts"]:
            self.by.setdefault(f["kind"], []).append(f)
        n = facts["names"]
        self.subject = facts["subject"]["name"]
        self.forms = set(facts["subject"].get("forms", [self.subject]))
        self.aliases = dict(n.get("aliases", {}))
        self.canonical = set(n.get("canonical", []))
        # 名前解決用：長い名前から順に探す
        self.name_keys = sorted(set(self.canonical) | set(self.aliases.keys()), key=len, reverse=True)
        self.moves = sorted(set(n.get("moves", [])), key=len, reverse=True)
        self.items = sorted(set(n.get("items", [])), key=len, reverse=True)
        self.arches = sorted(set(n.get("arches", [])), key=len, reverse=True)
        self.natures = sorted(set(n.get("natures", [])), key=len, reverse=True)
        self.abilities = sorted(set(n.get("abilities", [])), key=len, reverse=True)
        self.ev_strings = set()
        self.col_season = {}    # 表のセル行 → 列見出し（「M-6」列のセルの順位は前季の順位として照合する）
        self.weak_names = []    # run_gate が render_sections の結果で埋める（mult の「苦手な相手は…」解決用）
        self.strong_names = []
        for f in self.by.get("real_stat", []):
            ev = f.get("ev")
            if ev:
                self.ev_strings.add("-".join(f"{l}{e}" for l, e in zip(STAT_LETTERS, ev) if e))
        for c in facts.get("cards", []):
            self.ev_strings.add("-".join(f"{l}{e}" for l, e in zip(STAT_LETTERS, c["ev"]) if e))

    def canon(self, name):
        return self.aliases.get(name, name)

    def pokemon_in(self, text):
        """文中のポケモン名（正規名に解決）。長い名前を優先し、重なる短い名前は拾わない。"""
        found, covered = [], []
        for nm in self.name_keys:
            for m in re.finditer(re.escape(nm), text):
                if any(not (m.end() <= a or m.start() >= b) for a, b in covered):
                    continue
                covered.append((m.start(), m.end()))
                found.append(self.canon(nm))
        return found

    def words_in(self, text, vocab):
        found, covered = [], []
        for w in vocab:
            for m in re.finditer(re.escape(w), text):
                if any(not (m.end() <= a or m.start() >= b) for a, b in covered):
                    continue
                covered.append((m.start(), m.end()))
                found.append(w)
        return found


def _near(f, v, tol=0.051):
    x = f.get("value")
    return x is not None and abs(x - v) < tol


def _pk_ok(f, pokemons, allow_base=True):
    """事実のポケモンが文中の言及と整合するか。言及が無ければ制約なし。"""
    if not pokemons:
        return True
    cands = {f.get("pokemon"), f.get("opp"), f.get("opp_sp"), f.get("opp_label"), f.get("defender"), f.get("partner")}
    if allow_base:
        cands.add(f.get("base_pokemon"))
        cands.add(f.get("my_label"))
    return any(p in cands for p in pokemons)


def resolve(ctx: Ctx, claim, pokemons, natures, items, moves, arches, abilities):
    """候補事実のリストを返す（空ならno_fact）。"""
    k, v, s = claim.kind, claim.value, claim.sentence
    by = ctx.by
    unit_pk = ctx.canon(claim.unit_pokemon) if claim.unit_pokemon else None
    # 被写体（とそのメガ形態）は記事のどの文にも暗黙に存在する。単位（表の行・カード）のポケモンも常に含める。
    pks = list(dict.fromkeys(list(pokemons) + ([unit_pk] if unit_pk else []) + [ctx.subject] + sorted(ctx.forms)))
    arch_ctx = arches or ([claim.unit_arch] if claim.unit_arch else [])

    def filt(fs, **cond):
        out = []
        for f in fs:
            ok = True
            for key, val in cond.items():
                if val is None:
                    continue
                if f.get(key) != val:
                    ok = False
                    break
            if ok:
                out.append(f)
        return out

    if k == "stat_token":
        stat, val = v["stat"], v["value"]
        if "種族値" in s:
            return [f for f in by.get("base_stat", []) if f["stat"] == stat and f["value"] == val and _pk_ok(f, pks)]
        cands = [f for f in by.get("real_stat", []) + by.get("derived_stat", []) if f.get("stat") == stat and f["value"] == val]
        cands = [f for f in cands if _pk_ok(f, pks)]
        # 性格・持ち物・型は「あれば優先」。1文に複数の性格が並ぶ文（いじっぱり個体はS154、ようき個体はS169）で
        # 全部を同時に要求すると偽陽性になるため、絞って空になるなら絞らない
        for key, vals in (("nature", natures), ("item", items), ("arch", arch_ctx)):
            if vals:
                c2 = [f for f in cands if f.get(key) in vals]
                cands = c2 or cands
        if stat == "S":
            # エンジンの対面行が持つ素早さ（積み後など real_stat に無い値も含む）
            for f in by.get("matchup", []):
                if f.get("my_s") == val or (f.get("opp_s") == val and _pk_ok(f, pks)):
                    cands.append(f)
        return cands
    if k == "ev_spread":
        if v in ctx.ev_strings:
            return [{"id": "ev_spread"}]
        # 「H32-B32」のような部分表記は、その成分が一致する既知の配分があればOK
        parts = dict(re.findall(r"([HABCDS])(\d{1,2})", v))
        for f in by.get("real_stat", []):
            ev = f.get("ev")
            if ev and _pk_ok(f, pks) and all(ev[STAT_LETTERS.index(l)] == int(n) for l, n in parts.items()):
                return [f]
        return []
    if k == "ev_single":
        return [{"id": "ev_single"}] if 0 <= v <= 32 else []
    if k == "date":
        src = ctx.facts["sources"]
        return [{"id": "sources/date"}] if v in (src.get("detail_date"), src.get("prev_detail_date")) else []
    if k == "rank":
        partner_c = [f for f in by.get("partner_rank", []) if f["value"] == v and (f["partner"] in pokemons or f["partner"] == unit_pk)]
        if "同居率" in s or claim.unit_kind == "partner-card":
            return partner_c
        cands = [f for f in by.get("usage_rank", []) if f["value"] == v]
        prev = ctx.facts["sources"].get("prev_season")
        explicit = list(pokemons) + ([unit_pk] if unit_pk else []) + [ctx.subject]
        prev_in = bool(prev and prev in s) or "前シーズン" in s or (prev and ctx.col_season.get(claim.line) == prev)
        if prev_in and re.search(r"引き続き|維持|変わらず|据え置き|連続|キープ", s):
            # 「M-6から引き続き1位」：両シーズンとも同じ順位のポケモンだけ（2026-10-18: M-6は2位なのに
            # M-7の1位だけで照合して通っていた）
            now = {f["pokemon"] for f in cands if not f.get("season")}
            was = {f["pokemon"] for f in cands if f.get("season") == prev}
            return [f for f in cands if f["pokemon"] in (now & was) and f["pokemon"] in explicit] + partner_c
        if prev_in:
            c2 = [f for f in cands if f.get("season")]
            cands = c2 or cands
        else:
            cands = [f for f in cands if not f.get("season")]
        # 使用率順位は文中で名指しされたポケモン（または単位のポケモン）のもの。被写体は名指しが無くてもよい
        return [f for f in cands if f.get("pokemon") in explicit] + partner_c
    if k == "pt_diff":
        signed = claim.raw.startswith(("+", "-"))
        cands = [f for f in by.get("adopt_rate_diff", []) if (_near(f, v) if signed else abs(abs(f["value"]) - v) < 0.051)]
        names = moves + items + natures + abilities
        # 文中に名前が出ている差分を優先し、名前があるのに一致しなければ通さない（別の名前の差分と偶然一致させない）。
        # 名前の語彙に無い技（きりばらい等）もあるので、差分事実の名前が文に直接出ているかで判定する
        named = [f for f in cands if f["name"] in s]
        if named:
            cands = named
        elif names:
            cands = []
        return [f for f in cands if _pk_ok(f, pks)]
    if k in ("ko", "pct_range", "ko_prob_roll"):
        cands = [f for f in by.get("matchup", []) if _pk_ok(f, pks, allow_base=True)]
        if arch_ctx:
            c2 = [f for f in cands if f.get("my_arch") in arch_ctx]
            cands = c2 or cands
        def match_rows(rows, item_specific):
            out = []
            other = {"my": "opp", "opp": "my"}
            for f in rows:
                for side in ("my", "opp"):
                    mv = f.get(f"{side}_move")
                    # 技の制約：文中の技がこの側の技か、もう片方の側の技ならよい（「相手の技X…自分は確定2発」の形が普通）。
                    # 持ち物指定の行（「ゴツゴツメット個体には確定4発」）は別ビルドなので技の制約を外す
                    move_ok = (not moves) or item_specific or (mv in moves) or (f.get(f"{other[side]}_move") in moves)
                    if k == "ko":
                        hits, cert, prob = f.get(f"{side}_hits"), f.get(f"{side}_certain"), f.get(f"{side}_prob")
                        if hits == v["hits"] and bool(cert) == v["certain"]:
                            if v["prob"] is None or (prob is not None and abs(round(prob) - v["prob"]) <= 1):
                                if move_ok:
                                    out.append(f)
                    elif k == "pct_range":
                        lo, hi = f.get(f"{side}_pct_lo"), f.get(f"{side}_pct_hi")
                        if lo is not None and abs(lo - v[0]) < 0.051 and abs(hi - v[1]) < 0.051:
                            out.append(f)
                    elif k == "ko_prob_roll":
                        prob = f.get(f"{side}_prob")
                        if prob is not None and abs(prob - v / 16 * 100) <= 4:
                            out.append(f)
            return out

        # 持ち物が文中にあれば、その持ち物のビルド行を先に試す（「きあいのタスキ個体には確定2発」）。
        # 1文に代表行と持ち物別の補足が同居するので、無ければ全行で再試行する
        if items:
            c2 = [f for f in cands if f.get("opp_item") in items or f.get("my_item") in items]
            out = match_rows(c2, True) if c2 else []
            if out:
                return out
        return match_rows(cands, False)
    if k == "pct":
        out = []
        names = moves + items + natures + abilities + arch_ctx
        # 技/持ち物名が文中にあれば、その名前の採用率は被写体側のものでもよい
        # （「じしん（採用率68.1%）はアシレーヌに確定3発」のように相手名と並ぶのが普通）
        pks_adopt = list(pks) + [ctx.subject] + list(ctx.forms)
        for f in by.get("adopt_rate", []):
            if _near(f, v) and (not names or f["name"] in names) and _pk_ok(f, pks_adopt if names else pks):
                out.append(f)
        if not out and names:
            # 名前が文中にあるが別の名前の値かもしれない：ポケモン制約のみで再探索（例「メガX率32.3%」）
            out = [f for f in by.get("adopt_rate", []) if _near(f, v) and _pk_ok(f, pks)]
        for f in by.get("usage_rate", []):
            if _near(f, v) and _pk_ok(f, pks):
                out.append(f)
        # 型プール由来の推定割合（型シェア・型内の性格/技/持ち物/構成の割合・個体の割合）は記事に書かない
        # （ユーザー指示 2026-10-16「推定値の割合は載せない」。実測＝DBの採用率・使用率だけが書ける）。
        # ここで一致しても OK にせず、推定値だけが一致した場合は estimate_pct として FAIL にする。
        estimate = []
        for kind in ("arch_share", "nature_share", "arch_move_share", "arch_item_share", "arch_build_share"):
            for f in by.get(kind, []):
                if _near(f, v) and _pk_ok(f, pks):
                    estimate.append(f)
        for f in by.get("matchup", []):
            if not _pk_ok(f, pks):
                continue
            for key in ("opp_share", "my_share"):
                if f.get(key) is not None and abs(f[key] - v) < 0.051:
                    estimate.append(f)
            for side in ("my", "opp"):
                for key in (f"{side}_pct_lo", f"{side}_pct_hi"):
                    if f.get(key) is not None and abs(f[key] - v) < 0.051:
                        out.append(f)
                p = f.get(f"{side}_prob")
                if p is not None and abs(round(p) - v) <= 1:
                    out.append(f)
        # 技の追加効果の確率（「20%の確率でひるませる」）は move_effect（DB の effect_text）に書かれている。
        # 2026-10-25 まで照合先が無く、書き手が「低確率で」と言い換えたり gate:allow で通したりしていた
        if not out and (moves or items):
            vs = f"{v:g}%"
            out = [f for f in by.get("move_effect", []) if f.get("move") in moves and vs in (f.get("value") or "")]
            out += [f for f in by.get("item_effect", []) if f.get("item") in items and vs in (f.get("value") or "")]
        if not out and abilities:
            # 特性の効果の確率（のろわれボディ30%等）も DB の効果文と照合する（2026-10-27 ゲンガー）
            vs = f"{v:g}%"
            out = [f for f in by.get("ability_effect", []) if f.get("ability") in abilities and vs in str(f.get("value") or f.get("text") or "")]
        if not out and estimate:
            return [{"id": estimate[0].get("id"), "estimate": True}]
        return out
    if k == "stage":
        cands = [f for f in by.get("stage_change", []) if f["value"] == v]
        if moves:
            c2 = [f for f in cands if f["move"] in moves]
            cands = c2 or cands
        return cands
    if k == "move_duration":
        # 技の継続ターン数：主張（単一値 or 範囲）が事実の範囲に完全に収まっていればOK。
        # 事実が「3〜4」（分岐あり）のとき、本文がどちらか一方（例「3ターン」）を書くのは許す
        # （条件を正しく選んで片方だけ書くのは良い書き方。逆に範囲外・記憶での近似値は認めない）。
        cands = [f for f in by.get("move_duration", [])
                 if f["turns_min"] <= v["min"] and v["max"] <= f["turns_max"]]
        # 技名が文中に無くても（技データ表のように技名が同じ<tr>の別セルにある場合等）、
        # 他の数値系（stage等）と同じく「技名で絞れるなら絞る、無ければ値だけで判定」にする。
        if moves:
            c2 = [f for f in cands if f["move"] in moves]
            cands = c2 or cands
        return cands
    if k == "stab":
        # 「一致打点／一致技」の主張：技（または隣接するタイプ名）が、文中で言及されたポケモン
        # （無ければ被写体）のいずれかのタイプと一致するかを types/move_power 事実で照合する。
        type_sets = [set(t for t in f["value"] if t) for f in by.get("types", []) if f["pokemon"] in pks]
        if not type_sets:
            return []
        if v.get("type"):
            # 「かくとう一致」「一致フェアリー技」のようにタイプ名が直接書かれている場合はそれを直接照合
            return [f for f in by.get("types", []) if f["pokemon"] in pks and v["type"] in (f["value"] or [])]
        if not moves:
            return []  # どの技の話か分からなければ判定できない
        mtype = {f["move"]: f.get("type") for f in by.get("move_power", [])}
        # 「一致」の直前（読点・句点まで）にある技がすべて一致しているか。文中のどれか1技が一致すれば通していたため
        # 「じしんの一致技」（ルカリオ）が同じ文のインファイトで PASS していた（2026-10-25）
        for m_ in re.finditer("一致", s):
            seg = re.split(r"[、。\n]", s[:m_.start()])[-1]
            seg_moves = [mv for mv in moves if mv in seg and mtype.get(mv)]
            if seg_moves and not all(any(mtype.get(mv) in ts for ts in type_sets) for mv in seg_moves):
                return []
        return [f for f in by.get("move_power", [])
                if f["move"] in moves and any(f["type"] in ts for ts in type_sets)]
    if k == "mult":
        # 2026-10-18: ×N の主張はタイプ名を見ずにポケモン名＋数値だけで照合していたため、別タイプの type_eff や
        # 能力ランク定数(const/stage_mult 2.0/3.0/4.0)と値が偶然一致して PASS していた。タイプ名の役割
        # （攻撃側 atk / 防御側 def）を article_claims が付けるので、付いていれば const を候補にしない。
        atk_type = claim.extra.get("atk_type")
        def_type = claim.extra.get("def_type")
        if def_type:
            return [f for f in by.get("type_chart", [])
                    if _near(f, v, 0.001) and f["def_type"] == def_type and (not atk_type or f["atk_type"] == atk_type)]
        # 攻撃側タイプの候補：文中のタイプ語に加え、文中の技名のタイプ（「マジカルフレイムには弱点（×2）」）
        move_types = {f["type"] for f in by.get("move_power", []) if f["move"] in moves and f.get("type")}
        atk_set = ({atk_type} if atk_type else set()) | move_types
        # 「〜ナイトでメガ進化すると…×4」のように、メガ形態名を書かずに言及する文では、言及した種のメガ形態も防御側の候補にする
        mega_pks = []
        if "メガ進化" in s or "メガ" in s:
            for mf in by.get("mega_form", []):
                if mf["pokemon"] in pks:
                    mega_pks.append(mf["form"])
        pks_m = pks + mega_pks
        # 定数（スカーフ1.5倍・特性の威力1.3倍等）は、その名前が文中にあるときだけ候補にする（偶然一致の防止）
        unit_text = getattr(claim, "unit_text", "") or s
        named_const = [f for f in by.get("const", []) if _near(f, v, 0.001) and f.get("name") and f["name"] in unit_text]
        if atk_set:
            te = [f for f in by.get("type_eff", []) if _near(f, v, 0.001) and f.get("atk_type") in atk_set]
            explicit = [p for p in pokemons if p not in ctx.forms and p != ctx.subject]
            if explicit or unit_pk:
                return [f for f in te if _pk_ok(f, pks_m)] + named_const
            # 相手が名指しされていない段落（「得意な相手はいずれもじしん弱点（×2）」等）：文脈語で相手集合を決める
            group = ctx.strong_names if "得意" in s else (ctx.weak_names if "苦手" in s else None)
            if group:
                hit = [f for f in te if f["defender"] in group]
                if re.search(r"いずれも|全て|すべて|全員|どれも", s):
                    return (hit if {f["defender"] for f in hit} >= set(group) else []) + named_const
                return hit + named_const
            return [f for f in te if _pk_ok(f, pks_m)] + named_const
        out = [f for f in by.get("const", []) if _near(f, v, 0.001)]
        out += [f for f in by.get("type_eff", []) if _near(f, v, 0.001) and _pk_ok(f, pks_m)]
        return out
    if k == "base_stat":
        # 「種族値は540→640」のように合計値を書くこともあるので合計（bst）も候補にする（2026-10-27 ギャラドス）
        return [f for f in by.get("base_stat", []) + by.get("mega_delta", []) + by.get("bst", []) + by.get("bst_delta", [])
                if f["value"] == v and _pk_ok(f, pks)]
    if k == "bare_number":
        out = []
        sw = claim.extra.get("stat_word")
        for f in by.get("base_stat", []) + by.get("mega_delta", []) + by.get("bst", []) + by.get("bst_delta", []):
            if f["value"] == v and _pk_ok(f, pks) and (not sw or f.get("stat") in (None, sw)):
                out.append(f)
        for f in by.get("move_power", []):
            if f["value"] == v and (not moves or f["move"] in moves):
                out.append(f)
        for f in by.get("real_stat", []) + by.get("derived_stat", []):
            if f["value"] == v and _pk_ok(f, pks) and (not sw or f.get("stat") == sw):
                out.append(f)
        for f in by.get("matchup", []):
            if _pk_ok(f, pks) and any(f.get(key) == v for key in ("my_dmg_lo", "my_dmg_hi", "opp_dmg_lo", "opp_dmg_hi", "my_s", "opp_s")):
                out.append(f)
        return out
    return []


def _engine_ref_ok(reason):
    """gate:allow causal reason="engine:<path>:L<n>" の path が ROOT 相対で実在し、n が行数以内か。"""
    m = re.match(r"engine:([^:\s]+):L(\d+)$", reason or "")
    if not m:
        return False, 'reason は engine:<path>:L<n> の形式'
    p = ROOT / m.group(1)
    if not p.exists():
        return False, f"{m.group(1)} が無い"
    n = int(m.group(2))
    total = p.read_text(encoding="utf-8", errors="replace").count("\n") + 1
    if n < 1 or n > total:
        return False, f"L{n} は {m.group(1)} の行数({total})を超えている"
    return True, ""


def run_gate(md_path, facts_path, today=None, slug=None, strict=False):
    text = Path(md_path).read_text(encoding="utf-8")
    facts = json.loads(Path(facts_path).read_text(encoding="utf-8"))
    ctx = Ctx(facts)
    # 1セル1行の表で、各 <td> 行の列見出しを引く（2026-10-25 アーマーガア：M-6列の「20位」をM-7の順位として照合していた）
    for tm in re.finditer(r"<table.*?</table>", text, re.S):
        tbl = tm.group(0)
        heads = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", tbl, re.S)]
        base = text.count("\n", 0, tm.start()) + 1
        for rm in re.finditer(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            for ci, cm in enumerate(re.finditer(r"<td[^>]*>", rm.group(1))):
                if ci < len(heads):
                    ln = base + tbl.count("\n", 0, rm.start(1) + cm.start())
                    ctx.col_season[ln] = heads[ci]
    lines = text.split("\n")
    results = []

    def add(level, cid, line, raw, reason, **kw):
        results.append({"id": cid, "level": level, "line": line, "raw": raw, "reason": reason, **kw})

    def allow_on(line, token):
        lt = lines[line - 1] if 0 < line <= len(lines) else ""
        al = AS.allowed(lt)
        return token in al or (token != "style" and any(t == token for t in al))

    # 2. rendered blocks（numbers より先に判定する：検証済みブロックの行は数値照合を省くため）
    verified = []  # [(line_start, line_end, id)]
    rendered = {}
    try:
        import render_sections as RS
        import render_matchup_rows as RR
        rendered = RS.render_all(facts)
        base = RR.render(facts)
        ctx.weak_names, ctx.strong_names = base["weak_names"], base["strong_names"]
        sha = RR.facts_sha1(facts)
        blocks = {}
        for m in re.finditer(r"<!-- gate:rows start id=([^\s]+) facts=([0-9a-f]+) -->\n(.*?)\n<!-- gate:rows end id=\1 -->", text, re.S):
            blocks[m.group(1)] = (m.group(2), m.group(3), text.count("\n", 0, m.start()) + 1, text.count("\n", 0, m.end()) + 1)
        norm = lambda t: re.sub(r"\s+", " ", t).strip()
        for bid, exp in rendered.items():
            if bid not in blocks:
                # 節に対応するブロックは、その節がある記事だけに要求する
                need = {"summary": "\n## まとめ", "move_table": "\n## 主要な技と採用率"}.get(bid)
                if bid.startswith("card:"):
                    need = f"### 型{bid.split(':')[1]}："
                if exp.strip() and (need is None or need in text):
                    add("FAIL", "rows_missing", 0, bid, f"{bid} の gate:rows ブロックが無い（render_sections.py の出力を貼る）")
                continue
            got_sha, got, line, line_end = blocks[bid]
            ok = True
            if got_sha != sha:
                add("FAIL", "rows_stale", line, bid, "事実ファイルが更新されている。render_sections.py を再実行して貼り直す")
                ok = False
            if norm(got) != norm(exp):
                add("FAIL", "rows_modified", line, bid, "gate:rows 区間が生成結果と一致しない（行は編集せず貼り直す）")
                ok = False
            if ok:
                verified.append((line, line_end, bid))
        for bid in blocks:
            if bid not in rendered:
                add("FAIL", "rows_unknown", blocks[bid][2], bid, "render_sections が生成しない id の gate:rows ブロック")
    except Exception as e:  # noqa: BLE001
        # 生成ブロックは必須なので、生成側のエラーで WARN のまま公開できないよう FAIL にする（2026-10-18）
        add("FAIL", "rows_check_error", 0, "", f"rows チェック中のエラー: {e}")

    def in_verified(line):
        for a, b, bid in verified:
            if a <= line <= b:
                return bid
        return None

    # 1. numbers
    claims = AC.extract_claims(text)
    for c in claims:
        s = c.sentence
        bid = in_verified(c.line)
        if bid:
            # 生成ブロック内の数値は生成器が facts から直接引いた値。逐語一致が照合そのもの。
            add("OK", "number", c.line, c.raw, "", kind=c.kind, fact=f"rows:{bid}")
            continue
        pokemons = ctx.pokemon_in(s)
        natures = ctx.words_in(s, ctx.natures)
        items = ctx.words_in(s, ctx.items)
        moves = ctx.words_in(s, ctx.moves)
        arches = ctx.words_in(s, ctx.arches)
        abilities = ctx.words_in(s, ctx.abilities)
        cands = resolve(ctx, c, pokemons, natures, items, moves, arches, abilities)
        if cands and cands[0].get("estimate"):
            add("FAIL", "estimate_pct", c.line, c.raw, f"型プール由来の推定割合（{cands[0]['id']}）は記事に書かない。DBの採用率・使用率だけを書く",
                kind=c.kind, sentence=s[:120])
        elif cands:
            add("OK", "number", c.line, c.raw, "", kind=c.kind, fact=cands[0].get("id"))
        elif allow_on(c.line, c.raw):
            add("ALLOW", "number", c.line, c.raw, AS.allowed(lines[c.line - 1]).get(c.raw, ""), kind=c.kind)
        elif c.kind == "bare_number" and not strict:
            add("WARN", "bare_number", c.line, c.raw, "事実ファイルに一致する値が無い（裸の数字）", kind=c.kind, sentence=s[:80])
        else:
            add("FAIL", "no_fact", c.line, c.raw, f"事実ファイルに一致する値が無い（{c.kind}; 文中のポケモン={pokemons or '-'} 性格={natures or '-'} 技={moves or '-'} 持ち物={items or '-'} 型={arches or '-'}）",
                kind=c.kind, sentence=s[:120])

    # 3. style
    for f in AS.check_all(text):
        if allow_on(f.line, "style"):
            add("ALLOW", "style", f.line, f.kind, AS.allowed(lines[f.line - 1]).get("style", ""))
        else:
            add("FAIL", "style", f.line, f.kind, f.detail)

    # 3a. 型カードの強み/弱みに相手名を書かない（型としての傾向を書く。相手ごとの差は arch_grid が持つ。2026-10-18）
    for m in re.finditer(r"\*\*(強み|弱み):\*\*\n\n(.*?)(?=\n\n\*\*|\n---|\n##|\Z)", AS.strip_blocks(text), re.S):
        body = m.group(2)
        base = text.count("\n", 0, m.start(2)) + 1
        names = [n for n in ctx.pokemon_in(body) if n != ctx.subject and n not in ctx.forms]
        if names:
            line = base
            if allow_on(line, "style"):
                add("ALLOW", "style", line, "card_opponent_name", AS.allowed(lines[line - 1]).get("style", ""))
            else:
                add("FAIL", "card_opponent_name", line, "、".join(dict.fromkeys(names)),
                    f"型カードの{m.group(1)}に相手名がある。型としての傾向だけを書き、相手ごとの差は arch_grid の表に任せる（役割対象として必要なら同じ行に gate:allow style）")

    # 3a2. 型の分かれ方・選択技（2026-10-25 ミミッキュ差分レビューの残 FAIL J6 を機械化）
    arch_names = [c["arch"] for c in facts.get("cards", [])]
    hr = [i for i, l in enumerate(lines) if l.strip() == "---"]
    if len(hr) >= 3:
        intro = "\n".join(lines[hr[1] + 1:hr[2]])
        named = [a for a in arch_names if a in intro]
        if len(named) >= 2:
            first = min(intro.find(a) for a in named)
            add("FAIL", "intro_arch_split", hr[1] + 2 + intro.count("\n", 0, first), "、".join(named),
                "冒頭で型の分かれ方を説明している（型の説明は「採用型」の節と型カードに1回だけ。冒頭は何者かを1〜2文で）")
    # 型カードの見出しの順と spec の cards の順が違うと、arch_grid の列が型カードと違う順に並ぶ（2026-10-25 イダイトウ）
    heads = re.findall(r"^### 型\d+：(.+)$", text, re.M)
    in_spec = [a for a in arch_names if a in heads]
    if heads and [h for h in heads if h in arch_names] != in_spec:
        add("FAIL", "card_order", 1, " / ".join(heads), f"型カードの順が spec の cards の順（{' / '.join(in_spec)}）と違う。spec を記事の順に並べ替えて article_facts.py を再実行する")
    # 型カードの説明文が技表の効果文の言い直しだけになっている（2026-10-27 ハッサム差分レビューの残 FAIL J6
    # 「つるぎのまいで攻撃を2段階上げてから攻めこむ型です」）。効果文の大半と重なり、ほかの情報がほぼ無い文を止める
    # 「技・持ち物・性格・EVの組み合わせから」の定型文に、型カードで違わない要素が入っている（2026-10-28 27記事）
    import article_normalize as _AN
    if len(facts.get("cards", [])) >= 2:
        for i, l in enumerate(lines, 1):
            if not l.lstrip().startswith("<") and _AN.fix_arch_dims(l, facts["cards"]) != l:
                add("FAIL", "arch_dims", i, _AN.ARCH_DIMS_RE.search(l).group(0),
                    "型の分かれ方に、型カードで違わない要素（性格・EV等）が入っている（python3 scripts/article_normalize.py <記事> で直る）")
    # 前季からの順位の向き（2026-10-28：前季順位を最終日の値に直したら、ガブリアス「2位から1位に浮上」が「1位から1位に浮上」、
    # キラフロル「M-6から変わらず」が15位→18位で偽になった。数値は照合しても向きの語は照合していなかった）
    _ps = facts["sources"].get("prev_season")
    _now = next((f["value"] for f in facts["facts"] if f["kind"] == "usage_rank" and not f.get("season") and f["pokemon"] == ctx.subject), None)
    _was = next((f["value"] for f in facts["facts"] if f["kind"] == "usage_rank" and f.get("season") == _ps and f["pokemon"] == ctx.subject), None)
    if _ps and _now and _was:
        _real = "up" if _now < _was else ("down" if _now > _was else "same")
        _words = {"up": r"浮上|上昇|順位を上げ|躍進|ランクアップ", "down": r"後退|下落|下降|低下|順位を下げ|順位を落と",
                  "same": r"変わらず|維持|据え置き|キープ|引き続き"}
        for i, l in enumerate(AS.strip_blocks(text).split("\n"), 1):
            if _ps not in l or "位" not in l or "<td" in l:
                continue
            for sent in re.split(r"(?<=。)", l):
                if _ps not in sent or "位" not in sent:
                    continue
                said = [k for k, w in _words.items() if re.search(w, sent)]
                if said and _real not in said:
                    add("FAIL", "rank_direction", i, sent.strip()[:40],
                        f"{_ps}: {_was}位→M-7: {_now}位なのに順位の向きを「{'/'.join(said)}」と書いている")
    # 種族値バーは base_stats ブロックだけ（2026-10-28 アブソル：手書きで増加分が緑になり、記事ごとに色・幅がばらばらだった）
    _sb = AS.strip_blocks(text)
    for i, l in enumerate(_sb.split("\n"), 1):
        if l.startswith("### 種族値") or (l.startswith('<div style="max-width:') and "合計" in _sb[_sb.find(l):_sb.find(l) + 6000].split("\n</div>")[0]):
            add("FAIL", "base_stats_hand", i, l[:30], "種族値の見出し・バーは手書きしない（render_sections.py の base_stats ブロックを貼る）")
            break
    # 型カードの説明文は任意・1文まで（2026-10-28 TOP80 差分レビューの残 FAIL 6本中5本が説明文の言い直し。既存32記事が2文なので WARN）
    for m in re.finditer(r"<!-- gate:rows start id=card:\d+", text):
        _i = text.rfind("</div>", 0, m.start())
        _intro = re.sub(r"<[^>]+>", "", text[_i + 6:m.start()]).strip()
        if _intro.count("。") > 1:
            add("WARN", "card_intro_long", text.count("\n", 0, m.start()), _intro[:30],
                "型カードの説明文が2文以上（任意・1文まで。カードと card ブロックに無い役割だけを書く）")
    # 種族値バーの直下で種族値を読み上げるだけの文（2026-10-28 レビュー最多の J1。既存記事に多いので WARN）
    _bs = {f["value"] for f in facts["facts"] if f["kind"] == "base_stat"}
    _sec = re.search(r"\n## [^\n]*種族値[^\n]*\n(.*?)(?=\n## |\n### )", text, re.S)
    if _sec and _bs:
        _base = text.count("\n", 0, _sec.start(1)) + 1
        for j, l in enumerate(_sec.group(1).split("\n")):
            if l.lstrip().startswith("<") or not l.strip():
                continue
            for sent in re.split(r"(?<=。)", re.sub(r"<[^>]+>", "", l)):
                vals = [int(v) for v in re.findall(r"(?:HP|こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ|[HABCDS])\s*(?:種族値)?[はが]?\s*(\d{2,3})", sent)]
                if vals and all(v in _bs for v in vals):
                    add("WARN", "base_stat_restate", _base + j, sent.strip()[:30], "種族値バーの数値を本文で読み上げている（判断材料になる解釈が無ければ削る）")
    # 画像番号と alt のポケモン名の食い違い（2026-10-28 ガルーラ：サーフゴーの同居率カードにデカヌチャンの画像）
    _icons = {}
    for f in facts["facts"]:
        if f.get("kind") == "matchup" and f.get("opp_icon"):
            for nm in {f.get("opp"), f.get("opp_sp")} - {None}:
                _icons.setdefault(nm, set()).add(f["opp_icon"])
    for i, l in enumerate(lines, 1):
        for ic, alt in re.findall(r'<img src="/images/pokemon/pokemon-(\d{4}-\d{2})\.webp" alt="([^"]+)"', l):
            if alt in _icons and ic not in _icons[alt] and ic[:4] not in {x[:4] for x in _icons[alt]}:
                add("FAIL", "image_mismatch", i, alt, f"{alt} の画像番号が {ic}（事実ファイルでは {'・'.join(sorted(_icons[alt]))}）")
    # 関連記事のリンク先が draft のままだと、この記事だけ公開したときにリンク切れになる（2026-10-28 ハラバリー・ブリムオン・フシギバナ）
    import os as _os
    _blog = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "src", "content", "blog")
    for i, l in enumerate(lines, 1):
        for lk in re.findall(r"\(/blog/([a-z0-9-]+)/\)", l):
            fp = _os.path.join(_blog, f"{lk}.md")
            if _os.path.exists(fp) and re.search(r"^draft:\s*true", open(fp, encoding="utf-8").read(), re.M):
                add("WARN", "link_to_draft", i, lk, "リンク先の記事が draft のまま。同時に公開するか、公開までリンクを外す")
    for line_no, sent, mv in AS.card_effect_restatements(text, {f["move"]: f.get("value") or "" for f in facts["facts"] if f["kind"] == "move_effect"}):
        add("FAIL", "card_effect_restate", line_no, mv,
            f"型カードの説明文「{sent[:40]}」が技表の{mv}の効果文の言い直し。他の型との違い（何のために採用するか）を書く")
    # 種族値バー表：1行に「通常形・メガ形」の値が並ぶ。値単体の照合だと、メガ側に通常形の値（135）を書いても
    # 通常形の事実に一致して通ってしまう（2026-10-25 ボーマンダ）。列の位置（通常形/メガ形）で照合する
    stat_of = {"HP": "H", "こうげき": "A", "ぼうぎょ": "B", "とくこう": "C", "とくぼう": "D", "すばやさ": "S"}
    bst = {}
    for f in ctx.by.get("base_stat", []):
        bst.setdefault(f["pokemon"], {})[f["stat"]] = f["value"]
    megas = [f["form"] for f in ctx.by.get("mega_form", []) if f["pokemon"] == ctx.subject]
    for rm in re.finditer(r'white-space:nowrap">(HP|こうげき|ぼうぎょ|とくこう|とくぼう|すばやさ)</span>(.*?)(?=white-space:nowrap">|</div>\s*</div>\s*$|\Z)', text, re.S):
        vals = [int(x) for x in re.findall(r'text-align:right">(?:<strong[^>]*>)?(\d+)', rm.group(2))]
        if not vals or ctx.subject not in bst:
            continue
        st = stat_of[rm.group(1)]
        ln = text.count("\n", 0, rm.start()) + 1
        if bst[ctx.subject].get(st) is not None and vals[0] != bst[ctx.subject][st]:
            add("FAIL", "base_stat_chart", ln, str(vals[0]), f"{ctx.subject}の{rm.group(1)}種族値は{bst[ctx.subject][st]}")
        allowed = {bst[m].get(st) for m in megas if m in bst}
        for v2 in vals[1:2]:
            if allowed and v2 not in allowed:
                add("FAIL", "base_stat_chart", ln, str(v2), f"メガ形の{rm.group(1)}種族値は{'/'.join(str(x) for x in sorted(a for a in allowed if a is not None))}")
    # 列見出しが前季（M-6）の列のセルに「（M-6）」と重ねて書かない（2026-10-25 アーマーガアの差分レビュー）
    prev_s = facts["sources"].get("prev_season")
    for ln, head in ctx.col_season.items():
        if prev_s and head == prev_s and 0 < ln <= len(lines) and f"（{prev_s}）" in lines[ln - 1]:
            add("FAIL", "col_redundant", ln, f"（{prev_s}）", f"列見出しが{prev_s}の列なので、セル内の「（{prev_s}）」は消す（季節は列見出しから照合される）")
    # タイトル・description に出す「〜型」は型カードの型名だけ（2026-10-27 ブラッキーの「イカサマ受け型」・少数派の型を外した後の残り）
    fm = re.match(r"---\n(.*?)\n---", text, re.S)
    if fm and arch_names:
        for ln_off, fl in enumerate(fm.group(1).split("\n")):
            if not fl.startswith(("title:", "description:")):
                continue
            for piece in re.split(r"[のをはがにでと、。「」（）()\s/／:：'0-9%．.]+", fl):
                tok = piece.split("・")[-1] if piece.endswith("型") else ""
                generic = ("型", "採用型", "各型", "全型", "つ型", "物理型", "特殊型", "メガ型", "メガ進化型", "非メガ型", "両刀型",
                           "積み型", "耐久型", "速攻型", "持つ型", "使う型")
                if not tok or tok in generic or tok.endswith(("型解説", "型別")):
                    continue
                if not any(tok == a or tok.endswith(a) or a.endswith(tok) for a in arch_names):
                    add("FAIL", "fm_unknown_arch", ln_off + 2, tok, f"タイトル/description の「{tok}」が型カードの型名に無い（型カード: {' / '.join(arch_names)}）")
    # 選択技の説明は表の注記（NOTE_ROW）が出す。本文で触れさせる検査は、採用0.5%の技まで本文に挙げさせて
    # 誤りを生んだ（2026-10-25 グソクムシャ）ので置かない

    # 3b. causal（仕組み語＋因果接続。事実ファイルに無い「なぜ」を記憶で書くのを止める。2026-10-18）
    for f in AS.check_causal(text, skip_ranges=[(a, b) for a, b, _ in verified]):
        al = AS.allowed(lines[f.line - 1] if 0 < f.line <= len(lines) else "")
        if "causal" in al:
            ok, why = _engine_ref_ok(al["causal"])
            if ok:
                add("ALLOW", "causal", f.line, f.kind, al["causal"])
            else:
                add("FAIL", "causal_allow_invalid", f.line, f.kind, f"gate:allow causal の reason が不正: {why}")
        else:
            add("FAIL", "causal_mechanic", f.line, f.kind, f.detail + '（仕組みの因果は事実ファイルで裏付けられる結果だけを書く。根拠がエンジン実装なら <!-- gate:allow causal reason="engine:<path>:L<n>" --> を同じ行に付ける）')

    # 4. dates
    src = facts["sources"]
    for m in re.finditer(r"データは(\d{4}-\d{2}-\d{2})時点", text):
        line = text.count("\n", 0, m.start()) + 1
        if m.group(1) != src.get("detail_date"):
            add("FAIL", "date_mismatch", line, m.group(1), f"事実ファイルの detail_date は {src.get('detail_date')}")

    # 5. publish state
    fm = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fmtext = fm.group(1) if fm else ""
    draft_m = re.search(r"^draft:\s*(true|false)", fmtext, re.M)
    draft = (draft_m.group(1) == "true") if draft_m else False
    if not draft:
        pub = re.search(r"^pubDate:\s*'?(\d{4}-\d{2}-\d{2})", fmtext, re.M)
        if today and (not pub or pub.group(1) != today):
            add("FAIL", "pubdate", 1, pub.group(1) if pub else "", f"draft:false の記事は pubDate を公開日（{today}）にする")
        hero = re.search(r"^heroImage:\s*'([^']+)'", fmtext, re.M)
        if hero:
            rel = hero.group(1)
            p = ROOT / "src" / "assets" / rel.split("/assets/")[-1]
            if not p.exists():
                add("FAIL", "hero_missing", 1, rel, "heroImage の実体が無い")
    sl = slug or Path(md_path).stem
    sm = re.search(r"-m(\d+)$", sl)
    if sm and f"M-{sm.group(1)}" != facts["subject"]["season"]:
        add("FAIL", "season_mismatch", 1, sl, f"事実ファイルの季節 {facts['subject']['season']} と slug が不一致")
    try:
        import pool_versions
        if src.get("pool_version") != pool_versions.pointer("page"):
            add("WARN", "pool_drift", 1, src.get("pool_version"), f"型プールの page 版が {pool_versions.pointer('page')} に進んでいる（事実ファイルを再生成するか確認）")
    except Exception:  # noqa: BLE001
        pass

    # 6. names
    known = set(facts["names"].get("known", []))
    clean = AC.strip_noise(text)
    # 長い既知名（アローラキュウコン）の中の短い名前（キュウコン）は別ポケモンとして数えない（2026-10-25 誤検出）
    covered = []
    for nm in sorted(known | ctx.canonical | set(ctx.aliases.keys()), key=len, reverse=True):
        if len(nm) >= 3:
            covered += [(m.start(), m.end(), nm) for m in re.finditer(re.escape(nm), clean)]
    for nm in sorted(known - ctx.canonical - set(ctx.aliases.keys()), key=len, reverse=True):
        if len(nm) < 3:
            continue
        for m in re.finditer(re.escape(nm), clean):
            if any(a <= m.start() and m.end() <= b and other != nm and len(other) > len(nm) for a, b, other in covered):
                continue
            line = clean.count("\n", 0, m.start()) + 1
            add("WARN", "unknown_pokemon", line, nm, "事実ファイルに無いポケモンへの言及（数値を書くなら spec の extra_pokemon に追加）")
            break

    # 7. counts
    for m in re.finditer(r"以下の(\d+)体", text):
        line = text.count("\n", 0, m.start()) + 1
        rest = text[m.end():]
        tb = re.search(r"<tbody>(.*?)</tbody>", rest, re.S)
        if tb:
            n = len(re.findall(r"<tr(?! class=\"note\")", tb.group(1)))
            if n != int(m.group(1)):
                add("FAIL", "count_mismatch", line, m.group(0), f"直後の表は{n}行")

    counts = {"FAIL": 0, "WARN": 0, "ALLOW": 0, "OK": 0}
    for r in results:
        counts[r["level"]] = counts.get(r["level"], 0) + 1
    return {"pass": counts["FAIL"] == 0, "counts": counts, "results": results,
            "facts": {"detail_date": src.get("detail_date"), "pool_version": src.get("pool_version")}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--facts", required=True)
    ap.add_argument("--today", default=None)
    ap.add_argument("--report", default=None)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--slug", default=None)
    args = ap.parse_args()
    if not os.path.exists(args.md) or not os.path.exists(args.facts):
        print("[article_gate] 入力ファイルが無い", file=sys.stderr)
        sys.exit(2)
    rep = run_gate(args.md, args.facts, today=args.today, slug=args.slug, strict=args.strict)
    c = rep["counts"]
    print(f"[article_gate] {'PASS' if rep['pass'] else 'FAIL'}  FAIL {c['FAIL']} / WARN {c['WARN']} / ALLOW {c['ALLOW']} / OK {c['OK']}  (detail_date={rep['facts']['detail_date']})")
    for r in sorted(rep["results"], key=lambda r: (r["level"] != "FAIL", r["level"] != "WARN", r["line"])):
        if r["level"] == "OK":
            continue
        extra = f"  ← {r['sentence']}" if r.get("sentence") else ""
        print(f"L{r['line']}: [{r['level']}:{r['id']}] {r['raw']} — {r['reason']}{extra}")
    if args.report:
        Path(args.report).write_text(json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
    sys.exit(0 if rep["pass"] else 1)


if __name__ == "__main__":
    main()
