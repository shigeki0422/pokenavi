#!/usr/bin/env python3
"""article_claims / article_style / article_gate の回帰テスト。

実行: cd /Users/shigeki/work/pokenavi && python3 scripts/tests/test_article_gate.py
（scripts/tests/test_all.py と同じ check(desc, cond, detail) 流儀。FAILがあれば exit 1）
"""
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

import article_claims as AC  # noqa: E402
import article_style as AS  # noqa: E402

PASS = FAIL = 0
FAILURES = []


def check(desc, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        msg = f"FAIL: {desc}" + (f" → {detail}" if detail else "")
        FAILURES.append(msg)
        print(f"  ✗ {msg}")


def kinds(text):
    return [(c.kind, c.raw) for c in AC.extract_claims(text)]


# ---------------------------------------------------------------- claims ----
print("[claims] EV配分を実数値と誤認しない")
ks = kinds("<strong>EV:</strong> H2-A32-S32<br>")
check("EV配分は ev_spread 1件", ks == [("ev_spread", "H2-A32-S32")], str(ks))

print("[claims] CSS width は無視")
ks = kinds('<div style="width:54%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px"></div>')
check("CSS width:54% を主張として拾わない", ks == [], str(ks))

print("[claims] 乱数1発（約31%）の prob を取る")
cs = AC.extract_claims("ムーンフォース（採用率98.8%）は乱数1発（約31%）で、外れても2発目で沈めます。")
ko = [c for c in cs if c.kind == "ko"]
check("ko 1件", len(ko) == 1, str([(c.kind, c.raw) for c in cs]))
check("ko.certain False / hits 1 / prob 31", ko and ko[0].value == {"certain": False, "hits": 1, "prob": 31}, str(ko and ko[0].value))
check("採用率98.8% は pct", any(c.kind == "pct" and c.value == 98.8 for c in cs), str([(c.kind, c.value) for c in cs]))

print("[claims] 確定2発 は prob None")
cs = AC.extract_claims("じしん（採用率68.1%）は確定2発です。")
ko = [c for c in cs if c.kind == "ko"]
check("確定2発", ko and ko[0].value == {"certain": True, "hits": 2, "prob": None}, str(ko and ko[0].value))

print("[claims] 実数値トークン")
cs = AC.extract_claims("ようきでA182・S169、いじっぱりでA200・S154です。")
st = sorted((c.value["stat"], c.value["value"]) for c in cs if c.kind == "stat_token")
check("A182/S169/A200/S154", st == [("A", 182), ("A", 200), ("S", 154), ("S", 169)], str(st))

print("[claims] 種族値・pt差分・順位・倍率・段階・%範囲")
cs = AC.extract_claims("とくこう種族値141に特化し、使用率1位、ステルスロックは+7.9pt、こおり×4、こうげきが2段階上がり、1発43.9〜51.9%です。")
got = {c.kind: c.value for c in cs}
check("base_stat 141", got.get("base_stat") == 141, str(got))
check("rank 1", got.get("rank") == 1, str(got))
check("pt_diff 7.9", got.get("pt_diff") == 7.9, str(got))
check("mult 4", got.get("mult") == 4.0, str(got))
check("stage 2", got.get("stage") == 2, str(got))
check("pct_range (43.9, 51.9)", got.get("pct_range") == (43.9, 51.9), str(got))

print("[claims] 許容トークンは裸の数字にしない")
cs = AC.extract_claims("M-7シーズンのTOP30から、こおり1/8のダメージ、2〜5回連続攻撃。")
check("bare_number なし", not any(c.kind == "bare_number" for c in cs), str([(c.kind, c.raw) for c in cs]))

print("[claims] 単位の解決：tr のポケモン名 / partner-card / build-card の型名")
doc = """---
title: 't'
description: 'M-7シーズン使用率1位の考察。'
pubDate: '2026-10-14'
---

<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
  <strong style="font-size:1.05em">ステルスロック型</strong>
</div>

A182・S169の物理打点型です。

---

<tr>
  <td><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率68.1%）は確定3発です</td>
</tr>

<div class="partner-card">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
  <div class="name">ミミッキュ</div>
  <div class="rate">同居率2位</div>
</div>
"""
cs = AC.extract_claims(doc)
by_raw = {c.raw: c for c in cs}
check("description の 1位 は description 単位", by_raw.get("1位") and by_raw["1位"].unit_kind == "description", str(by_raw.get("1位") and by_raw["1位"].unit_kind))
check("tr の確定3発はアシレーヌ", by_raw.get("確定3発") and by_raw["確定3発"].unit_pokemon == "アシレーヌ", str(by_raw.get("確定3発") and by_raw["確定3発"].unit_pokemon))
check("tr の 2位 もアシレーヌ", any(c.raw == "2位" and c.unit_kind == "tr" and c.unit_pokemon == "アシレーヌ" for c in cs), str([(c.raw, c.unit_kind, c.unit_pokemon) for c in cs if c.raw == "2位"]))
check("partner-card の同居率2位はミミッキュ", any(c.raw == "2位" and c.unit_pokemon == "ミミッキュ" and c.unit_kind == "partner-card" for c in cs), str([(c.raw, c.unit_kind, c.unit_pokemon) for c in cs if c.raw == "2位"]))
check("build-card の A182 は型名付き", by_raw.get("A182") and by_raw["A182"].unit_arch == "ステルスロック型", str(by_raw.get("A182") and by_raw["A182"].unit_arch))
check("pubDate は frontmatter で空白化されて主張にならない", not any(c.kind == "date" and c.value == "2026-10-14" for c in cs), str([(c.kind, c.value) for c in cs if c.kind == "date"]))
check("行番号が正しい（確定3発は19行目）", by_raw.get("確定3発") and by_raw["確定3発"].line == 19, str(by_raw.get("確定3発") and by_raw["確定3発"].line))

# ---------------------------------------------------------------- style -----
print("[claims] 数字で始まる技名は裸の数字にしない")
check("10まんボルトの10を拾わない", not any(c.raw == "10" for c in AC.extract_claims("10まんボルト（採用率59.5%）で攻撃します。")))

print("[claims] 符号なしの pt も差分として拾う（足し算した値を素通りさせない）")
check("「5.8pt増えて」を pt_diff として拾う", any(c.kind == "pt_diff" and c.value == 5.8 for c in AC.extract_claims("合計した非スカーフ勢は5.8pt増えています。")))

print("[style] 強み欄の否定文")
f = [x for x in AS.check_all("**強み:**\n\n耐久面はほぼ同じ水準で、固いわけではありません。\n\n**弱み:**\n\nテスト\n") if x.kind.startswith("観点2")]
check("否定文を1件検出", len(f) == 1 and f[0].kind.startswith("観点2"), str([(x.kind, x.line) for x in f]))
check("行番号は3", f and f[0].line == 3, str(f and f[0].line))

print("[style] セルの文数・文字数")
cell = '<td style="padding:8px 12px;border:1px solid #cbd5e1">' + "あ。" * 3 + "</td>"
f = AS.check_all(cell)
check("3文は観点18e", any(x.kind.startswith("観点18e") for x in f), str([x.kind for x in f]))
cell = '<td style="padding:8px 12px;border:1px solid #cbd5e1">' + "あ" * 201 + "</td>"
f = AS.check_all(cell)
check("201字は観点18c", any(x.kind.startswith("観点18c") for x in f), str([x.kind for x in f]))

print("[style] 許可マーカー")
check("gate:allow style を解析", AS.allowed('x <!-- gate:allow style reason="2形態" -->') == {"style": "2形態"}, str(AS.allowed('x <!-- gate:allow style reason="2形態" -->')))
check("gate:allow 2.2倍 を解析", "2.2倍" in AS.allowed('<!-- gate:allow 2.2倍 reason="A400/A182" -->'))

print("[claims] 一致（STAB）主張の抽出：肯定形は拾い、否定形・動詞用法は拾わない")
check("「一致打点」を拾う", kinds("ウッドハンマーはくさタイプの一致打点です。") == [("stab", "一致")])
check("「かくとう一致の打点」を拾う（直前にタイプ名）",
      [c for c in AC.extract_claims("ドレインパンチはかくとう一致の打点です。") if c.kind == "stab"] != [])
check("「一致フェアリー技」を拾う（直後にタイプ名）",
      [c for c in AC.extract_claims("一致フェアリー技で弱点を突きます。") if c.kind == "stab"] != [])
check("「非一致」は拾わない（否定の接頭辞）", kinds("非一致の追加打点です。") == [])
check("「一致しない」は拾わない（動詞の否定形）", kinds("この技は一致しないため威力が低いです。") == [])
check("「一致補正がかかりません」は拾わない（否定文）",
      kinds("じめんタイプを失うため、この技に一致補正がかかりません。") == [])
check("「結果が一致する」は拾わない（動詞用法・STABと無関係）", kinds("結果が一致する相手を選びます。") == [])

print("[gate] 一致主張は「一致」の直前の技で判定する（同じ文の別の一致技で通さない）")
import article_gate as AG2
_fx = {"schema": 1, "slug": "t", "subject": {"name": "ルカリオ", "season": "M-7", "forms": ["ルカリオ"]},
       "sources": {"detail_date": "2026-10-11", "majority_pct": 20},
       "names": {"canonical": ["ルカリオ"], "aliases": {}, "known": ["ルカリオ"], "moves": ["じしん", "インファイト"], "items": [], "arches": [], "natures": []},
       "cards": [], "facts": [{"id": "types/ルカリオ", "kind": "types", "pokemon": "ルカリオ", "value": ["かくとう", "はがね"]},
                              {"id": "mp/じしん", "kind": "move_power", "move": "じしん", "type": "じめん", "value": 100},
                              {"id": "mp/インファイト", "kind": "move_power", "move": "インファイト", "type": "かくとう", "value": 120}]}
_cx = AG2.Ctx(_fx)
_c = [c for c in AC.extract_claims("インファイトで削り、じしんの一致技で倒します。") if c.kind == "stab"][0]
check("「じしんの一致技」は同じ文のインファイトがあっても一致にしない", AG2.resolve(_cx, _c, [], [], [], ["じしん", "インファイト"], [], []) == [])
_c2 = [c for c in AC.extract_claims("インファイトの一致打点で倒します。") if c.kind == "stab"][0]
check("「インファイトの一致打点」は一致", AG2.resolve(_cx, _c2, [], [], [], ["インファイト"], [], []) != [])

_fx2 = json.loads(json.dumps(_fx)); _fx2["names"]["moves"].append("アイアンヘッド")
_fx2["facts"].append({"id": "move_effect/アイアンヘッド", "kind": "move_effect", "move": "アイアンヘッド", "value": "20%の確率で相手をひるませる。"})
_cx2 = AG2.Ctx(_fx2)
_c3 = [c for c in AC.extract_claims("アイアンヘッドは20%の確率でひるませます。") if c.kind == "pct"][0]
check("技の追加効果の確率は move_effect と照合する", AG2.resolve(_cx2, _c3, [], [], [], ["アイアンヘッド"], [], []) != [])

print("[claims] ×N主張は直前のタイプ名をatk_typeとして拾う（2026-10-18: でんき×0.5がいわ×0.5の事実で誤ってPASSした件の再発防止）")
cs = AC.extract_claims("でんき技は無効から×0.5に変わります。")
mult_claims = [c for c in cs if c.kind == "mult"]
check("mult主張が1件", len(mult_claims) == 1, str(cs))
check("atk_type=でんき を拾う", mult_claims and mult_claims[0].extra.get("atk_type") == "でんき", str(mult_claims))
cs2 = AC.extract_claims("こだわりスカーフで素早さが1.5倍になります。")
mult_claims2 = [c for c in cs2 if c.kind == "mult"]
check("タイプ名が無ければatk_typeを付けない（スカーフの1.5倍等）",
      mult_claims2 and "atk_type" not in mult_claims2[0].extra, str(mult_claims2))

print("[style] 同居率の本文でパートナー表（受け・カバー）を言い直さない")
_pp = "## 同居率\n\n<div class=\"partner-grid\">\nx\n</div>\n\n{}\n\n## まとめ\n"
check("「受けられる範囲が広く…分担」を検出", any("言い直し" in f.kind for f in AS.check_partner_prose(_pp.format("サーフゴーは受けられる範囲が広く、対応を分担します。"))))
check("同居率の事実だけなら検出しない", AS.check_partner_prose(_pp.format("同居率1位はガブリアスで、M-6から変わっていません。")) == [])
check("被写体の弱点タイプの受けも表に任せる（本文では検出）", AS.check_partner_prose(_pp.format("グソクムシャはかくとう・じめんの両方を半減で受けられます。")) != [])
check("まとめでの同居パートナーの受けの言い直しを検出", any("言い直し" in f.kind for f in AS.check_all("## まとめ\n\n同居率上位のサーフゴーが苦手な相手の多くを受けられます。\n")))
check("まとめでも同居率の事実だけなら検出しない", not any("言い直し" in f.kind for f in AS.check_all("## まとめ\n\n同居率1位はガブリアスです。\n")))
print("[style] 表記ゆれ（素早さ→すばやさ）は normalize で揃え、残っていれば検出")
import article_normalize as AN
check("normalize は本文の素早さをすばやさに揃え、生成ブロックは触らない",
      AN.normalize("素早さが高い。\n<!-- gate:rows start id=weak facts=ab12 -->\n素早さ\n<!-- gate:rows end id=weak -->") ==
      "すばやさが高い。\n<!-- gate:rows start id=weak facts=ab12 -->\n素早さ\n<!-- gate:rows end id=weak -->")
check("M-6列のセルの「（M-6）」を消す", "<td>20位</td>" in AN.normalize("<table><tr><th>項目</th><th>M-6</th></tr><tr><td>順位</td><td>20位（M-6）</td></tr></table>"))
check("本文に素早さが残っていれば検出", any(f.kind == "表記ゆれ" for f in AS.check_all("素早さが高い。\n")))
print("[style] まとめが型カードの写しなら検出")
_doc = "### 型1：A型\n\nつるぎのまいで攻撃を上げてから一致技で押し切る積みアタッカーの型です。\n\n---\n\n## まとめ\n\n- つるぎのまいで攻撃を上げてから一致技で押し切る積みアタッカーの型です。\n"
check("まとめが型カードと同文なら検出", any("写し" in f.kind for f in AS.check_all(_doc)))
check("まとめが別の結論なら検出しない", not any("写し" in f.kind for f in AS.check_all(_doc.replace("- つるぎのまいで攻撃を上げてから一致技で押し切る積みアタッカーの型です。", "- 環境の速い相手が多いので、先手を取れる型を優先して選ぶのが無難です。"))))
print("[style] 手書きの強み/弱み・データ分析本文は検出")
check("手書きの強み欄を検出", any("手書き強み" in f.kind for f in AS.check_all("### 型1：A型\n\n**強み:**\n\n速い。\n")))
check("データ分析の手書き本文を検出", any("データ分析の手書き" in f.kind for f in AS.check_all("x\n## データ分析\n\n<table><tr><td>x。</td></tr></table>\n\nようきが増えています。\n\n## 次\n")))
check("データ分析の表の中の句点は検出しない", not any("データ分析の手書き" in f.kind for f in AS.check_all("x\n## データ分析\n\n<table>\n<tr><td>x。</td></tr>\n</table>\n\n## 次\n")))
check("特性名「せいでんき」を因果接続「せいで」と誤検出しない", not AS.check_causal("せいでんきは接触した相手をまひ状態にすることがあります。", []))
print("[style] 貼る位置コメントの残り")
check("<!-- 貼る位置 --> を検出", any(f.kind == "貼る位置コメントの残り" for f in AS.check_all("本文\n<!-- 貼る位置: 同居率の後 -->\n")))
print("[style] 長さ・粒度の上限（2026-10-18「冗長にしないルールはなぜ守られないか」→ 数値の上限をゲートに）")
card = ("### 型1：A型\n\n<div>\n<div class=\"build-header\"><strong style=\"font-size:1.05em\">A型</strong></div>\n</div>\n\n"
        "一文目です。二文目です。三文目です。\n\n**強み:**\n\n強い。もっと強い。さらに強い。\n\n**弱み:**\n\n弱い。\n\n---\n\n## 次\n")
ks = [f.kind for f in AS.check_card_prose(card)]
check("説明文3文・強み3文を検出", any("説明文" in k for k in ks) and any("強み" in k for k in ks) and not any("弱み" in k for k in ks), str(ks))
pre = "## 苦手なポケモン\n\n基準です。もう一文。\n\n<table></table>\n"
check("表の前の本文2文を検出", AS.check_pre_table(pre), str(AS.check_pre_table(pre)))
pre1 = "## 苦手なポケモン\n\n基準です。\n\n<table></table>\n"
check("表の前の本文1文は通す", not AS.check_pre_table(pre1))
part = "## 同居率上位\n\n<div class=\"partner-grid\">x</div>\n\n" + "役割。" * 20 + "\n\n" + "役割。" * 20 + "\n\n---\n## 次\n"
check("同居率の本文2段落を検出", AS.check_partner_prose(part), str(AS.check_partner_prose(part)))
blk = "<!-- gate:rows start id=weak facts=0 -->\n<td style=\"padding:8px 12px;border:1px solid #cbd5e1\">" + "あ" * 150 + "</td>\n<!-- gate:rows end id=weak -->"
check("strip_blocks で生成ブロックの中身が空白化される", "あ" not in AS.strip_blocks(blk) and AS.strip_blocks(blk).count("\n") == blk.count("\n"))

# ---------------------------------------------------------------- gate ------
try:
    import article_gate as AG  # noqa: E402
    HAVE_GATE = True
except Exception:
    HAVE_GATE = False

if HAVE_GATE:
    print("[gate] 最小の事実ファイルで PASS/FAIL")
    facts = {
        "schema": 1, "slug": "test-analysis-m7",
        "subject": {"name": "ガブリアス", "icon": "0445-00", "season": "M-7", "forms": ["ガブリアス"]},
        "sources": {"detail_date": "2026-10-11", "prev_detail_date": "2026-09-23", "prev_season": "M-6",
                    "pool_version": "M-7/2026-10-15", "majority_pct": 20},
        "names": {"canonical": ["ガブリアス", "アシレーヌ"], "aliases": {}, "known": ["ガブリアス", "アシレーヌ"],
                  "moves": ["じしん", "ムーンフォース"], "items": ["オボンのみ"], "arches": ["ステルスロック型"]},
        "cards": [],
        "facts": [
            {"id": "usage_rank/ガブリアス", "kind": "usage_rank", "pokemon": "ガブリアス", "value": 1},
            {"id": "adopt/move/ガブリアス/じしん/M-7", "kind": "adopt_rate", "category": "move", "pokemon": "ガブリアス", "name": "じしん", "season": "M-7", "value": 68.1},
            {"id": "adopt/move/アシレーヌ/ムーンフォース/M-7", "kind": "adopt_rate", "category": "move", "pokemon": "アシレーヌ", "name": "ムーンフォース", "season": "M-7", "value": 98.8},
            {"id": "real_stat/ガブリアス/ようき/2-32-0-0-0-32/きあいのタスキ/S", "kind": "real_stat", "pokemon": "ガブリアス", "nature": "ようき", "item": "きあいのタスキ", "arch": "ステルスロック型", "stat": "S", "value": 169},
            {"id": "mu/ステルスロック型/アシレーヌ#1", "kind": "matchup", "opp": "アシレーヌ", "opp_label": "アシレーヌ", "my_arch": "ステルスロック型",
             "my_move": "じしん", "my_move_rate": 68.1, "my_hits": 3, "my_certain": True, "my_prob": None,
             "opp_move": "ムーンフォース", "opp_move_rate": 98.8, "opp_hits": 1, "opp_certain": False, "opp_prob": 31,
             "my_s": 169, "opp_s": 82, "fast": True, "win": False, "representative": True},
        ],
    }
    good = "---\ntitle: 't'\ndescription: 'x'\npubDate: '2026-10-14'\ndraft: true\n---\n\n※本記事の使用率・採用率データは2026-10-11時点のものです。\n\nガブリアスは使用率1位です。ステルスロック型のようき個体はS169です。じしん（採用率68.1%）はアシレーヌに確定3発、ムーンフォース（採用率98.8%）は乱数1発（31%）です。\n"
    bad = good.replace("S169", "S170").replace("68.1%", "67.6%")
    with tempfile.TemporaryDirectory() as d:
        fp = os.path.join(d, "facts.json")
        json.dump(facts, open(fp, "w"), ensure_ascii=False)
        gp = os.path.join(d, "good.md"); open(gp, "w").write(good)
        bp = os.path.join(d, "bad.md"); open(bp, "w").write(bad)
        rep_good = AG.run_gate(gp, fp, today="2026-10-14", slug="test-analysis-m7")
        rep_bad = AG.run_gate(bp, fp, today="2026-10-14", slug="test-analysis-m7")
    check("正しい記事は FAIL 0", rep_good["counts"]["FAIL"] == 0, json.dumps([r for r in rep_good["results"] if r["level"] == "FAIL"], ensure_ascii=False)[:600])
    fails = [r["raw"] for r in rep_bad["results"] if r["level"] == "FAIL"]
    check("S170 と 67.6% が FAIL", "S170" in fails and "67.6%" in fails, str(fails))
    check("FAIL は 2件だけ", rep_bad["counts"]["FAIL"] == 2, str(fails))
    print("[gate] ×N主張はatk_typeで絞り込む（値が同じ別タイプのtype_effで誤ってPASSしない）")
    facts2 = {
        "schema": 1, "slug": "test-analysis-m7",
        "subject": {"name": "ガブリアス", "icon": "0445-00", "season": "M-7", "forms": ["ガブリアス", "メガガブリアスZ"]},
        "sources": {"detail_date": "2026-10-11", "prev_detail_date": "2026-09-23", "prev_season": "M-6",
                    "pool_version": "M-7/2026-10-15", "majority_pct": 20},
        "names": {"canonical": ["ガブリアス", "メガガブリアスZ"], "aliases": {}, "known": ["ガブリアス", "メガガブリアスZ"],
                  "moves": [], "items": [], "arches": []},
        "cards": [],
        "facts": [
            # いわ×0.5 は実在するが、でんき×0.5 は無い（＝でんき技への耐性の主張は事実に無い）
            {"id": "type_eff/いわ/メガガブリアスZ", "kind": "type_eff", "atk_type": "いわ", "defender": "メガガブリアスZ", "value": 0.5},
            {"id": "type_eff/でんき/メガガブリアスZ", "kind": "type_eff", "atk_type": "でんき", "defender": "メガガブリアスZ", "value": 1.0},
        ],
    }
    coincidence_md = "---\ntitle: 't'\ndescription: 'x'\npubDate: '2026-10-14'\ndraft: true\n---\n\n※本記事の使用率・採用率データは2026-10-11時点のものです。\n\nメガガブリアスZはでんき技を×0.5で受けます。\n"
    with tempfile.TemporaryDirectory() as d:
        fp2 = os.path.join(d, "facts2.json")
        json.dump(facts2, open(fp2, "w"), ensure_ascii=False)
        cp = os.path.join(d, "coincidence.md"); open(cp, "w").write(coincidence_md)
        rep_coincidence = AG.run_gate(cp, fp2, today="2026-10-14", slug="test-analysis-m7")
    fails2 = [r["raw"] for r in rep_coincidence["results"] if r["level"] == "FAIL"]
    check("でんき×0.5は、いわ×0.5の事実と誤って一致せずFAILになる", "×0.5" in fails2, str(fails2))
else:
    print("[gate] article_gate 未実装のためスキップ")

# ------------------------------------------------------------ render_matchup_rows ----
# 2026-10-17: 2つの再発防止テスト。
#   1) 技の採用率(move_rate)がNone（facts側に無い）のとき「None%」をそのまま出力していた。
#   2) 先手なのに負ける対面で、確定数が同じ/有利でも「確定数で下回り」と書いていた
#      （ガブリアスvsミミッキュ: 確定2発 対 確定2発・先手・ばけのかわで1発無効化、でlose）。
import render_matchup_rows as RM  # noqa: E402

print("[rows] 採用率が無い技は「None%」を出さない")
check("rate_clause(None) は空文字", RM.rate_clause(None) == "", repr(RM.rate_clause(None)))
check("rate_clause(68.1) は括弧付き", RM.rate_clause(68.1) == "（採用率68.1%）", repr(RM.rate_clause(68.1)))
check("rate_clause にメガの接頭辞を付けられる",
      RM.rate_clause(19.5, prefix="リザードン全体の") == "（リザードン全体の採用率19.5%）",
      repr(RM.rate_clause(19.5, prefix="リザードン全体の")))

print("[rows] 先手で負ける対面：確定数が同じ/有利なら「下回り」と書かない")
base = {"win": False, "fast": True, "my_s": 169, "opp_s": 148, "ko_by_priority": False,
        "my_move_prio": 0, "opp_move_prio": 0, "my_move": "じしん", "opp_move": "じゃれつく"}
tie = {**base, "my_hits": 2, "opp_hits": 2}
behind = {**base, "my_hits": 3, "opp_hits": 2}
txt_tie = RM.order_outcome_text(tie)
txt_behind = RM.order_outcome_text(behind)
check("確定数が同じなら「下回り」と書かない（誤った比較級を出さない）", "下回り" not in txt_tie, txt_tie)
check("確定数が同じでも先手・負けという事実は書く", "先手" in txt_tie and "倒されます" in txt_tie, txt_tie)
check("実際に下回るときは「下回り」と書く", "下回り" in txt_behind, txt_behind)

print("[rows] 相手が倒しきれない対面：「確定数で上回り/下回り」という比較級を重ねない")
win_opp_cant = {**base, "win": True, "fast": False, "my_hits": 4, "opp_hits": 999}
lose_my_cant = {**base, "win": False, "fast": True, "my_hits": 999, "opp_hits": 4}
check("相手が倒しきれないとき「確定数で上回り」と書かない", "上回り" not in RM.order_outcome_text(win_opp_cant), RM.order_outcome_text(win_opp_cant))
check("自分が倒しきれないとき「確定数で下回り」と書かない", "下回り" not in RM.order_outcome_text(lose_my_cant), RM.order_outcome_text(lose_my_cant))

print("[rows] 後手でも勝つ対面：確定数が同じなら「上回り」と書かない（対称バグの再発防止）")
tie_slow_win = {**base, "win": True, "fast": False, "my_hits": 2, "opp_hits": 2}
behind_slow_win = {**base, "win": True, "fast": False, "my_hits": 1, "opp_hits": 2}
txt_tie_slow = RM.order_outcome_text(tie_slow_win)
txt_behind_slow = RM.order_outcome_text(behind_slow_win)
check("確定数が同じなら「上回り」と書かない", "上回り" not in txt_tie_slow, txt_tie_slow)
check("確定数が同じでも後手・勝ちという事実は書く", "後手" in txt_tie_slow and "倒せます" in txt_tie_slow, txt_tie_slow)
check("実際に上回るときは「上回り」と書く", "上回り" in txt_behind_slow, txt_behind_slow)

print("[rows] 代表個体が多数派でないときの注記に句点(。)を混ぜない（文数カウントを狂わせるため）")
rep = {**base, "my_arch": "a", "my_move": "じしん", "my_move_rate": 50.0, "my_certain": True, "my_hits": 2,
       "my_prob_int": None, "my_reason": None, "opp_label": "カイリュー", "opp_sp": "カイリュー",
       "opp_nature": "いじっぱり", "opp_item": "ゴツゴツメット", "opp_share": 12.2, "opp_move": "アイススピナー",
       "opp_move_rate": 15.6, "opp_certain": True, "opp_hits": 2, "opp_prob_int": None, "opp_reason": None,
       "opp_ability": "マルチスケイル", "opp_mega": False}
cell = RM.reason_cell(rep, [{**rep, "opp_share": 60.0}], {})
check("注記（型内シェアの非多数派表示）に句点を含めない", "。" not in cell.split("のアイススピナー")[0].split("カイリュー")[1],
      cell)
# 2026-10-17: 「マルチスケイルで1発目が抑えられ」という理由付けは、確定数自体が特性を織り込み済み
# のはずで論理矛盾だったため撤回。不確かな理由は書かず、事実（確定数どおりには進まない）だけを書く。
check("不確かな理由（特性名）を書かない", "マルチスケイル" not in cell, cell)
check("確定数どおりに進まないという事実だけを書く", "確定数どおりには進まず" in cell, cell)

print("[rows] 倒しきれない相手には「倒しきれませんで、」という不自然な接続を使わない")
rep_cant = {**rep, "opp_hits": 999, "opp_certain": True, "opp_eff": 1}
cell_cant = RM.reason_cell(rep_cant, [], {})
check("「倒しきれませんで、」を使わない", "倒しきれませんで" not in cell_cant, cell_cant)
check("相手が倒しきれないときは「倒しきれず、」（先後の理由に読ませない。2026-10-28）", "倒しきれず、" in cell_cant and "倒しきれないため" not in cell_cant, cell_cant)

print("[rows] カードの表示技(moves)に無い技を使ったときは「選択技」と明記する")
card_moves = {"a": {"じしん", "つるぎのまい"}}
rep_sel = {**rep, "my_arch": "a", "my_move": "ウッドハンマー"}
cell_sel = RM.reason_cell(rep_sel, [], {}, card_moves)
check("カードに無い技は「選択技」と書く", "aの選択技ウッドハンマー" in cell_sel, cell_sel)
rep_def = {**rep, "my_arch": "a", "my_move": "じしん"}
cell_def = RM.reason_cell(rep_def, [], {}, card_moves)
check("カードにある技は「選択技」と書かない", "選択技" not in cell_def and "aのじしん" in cell_def, cell_def)

print("[rows] 有効な攻撃技が無い(my_move=None)ときは「選択技None」を出さない")
rep_noattack = {**rep, "my_move": None, "my_move_rate": None, "my_hits": 999, "my_certain": None, "my_reason": None}
cell_noattack = RM.reason_cell(rep_noattack, [], {})
check("「None」を出さない", "None" not in cell_noattack, cell_noattack)
check("有効な攻撃技が無い旨を書く", "有効な攻撃技が無く" in cell_noattack, cell_noattack)

print("[rows] タイプ相性で無効(0倍)なときは「倒しきれません」ではなく「無効」と書く")
check("eff=0は「無効」", RM.ko_text(True, 999, None, eff=0) == "無効", RM.ko_text(True, 999, None, eff=0))
check("eff非0なら「倒しきれません」", RM.ko_text(True, 999, None, eff=1) == "倒しきれません", RM.ko_text(True, 999, None, eff=1))
# eff省略(None)も「無効」扱いにする：エンジン側が無効技でダメージ計算自体を省略しeffをNoneのまま
# 返すことがあり（通常の「倒しきれない」ケースでは必ずeffに数値が入る）、Noneだけ別扱いにすると
# 実例（ギャラドス非メガへのじめん技）で「倒しきれません」という誤った文が生成されていた。
check("eff省略時(None)は「無効」扱い", RM.ko_text(True, 999, None) == "無効", RM.ko_text(True, 999, None))

print("[rows] 安全網：facts側の値不足でNoneが紛れ込んだら例外で止まる（publish前に気づける）")
try:
    RM.reason_cell({**rep, "my_arch": None}, [], {})
    check("Noneが紛れ込んだらValueErrorになる", False, "例外が発生しなかった")
except ValueError:
    check("Noneが紛れ込んだらValueErrorになる", True)

# ============================================================ 第2期（2026-10-18） ====
print("[rows] 2026-10-25 指摘：確定数の重複注記なし／持ち物・特性の持ち主を明記／少数派技の明示")
check("「（確定数は○○）」を重ねない", "確定数は" not in RM.order_outcome_text({**base, "win": False, "fast": True, "my_hits": 2, "opp_hits": 2, "ko_by_priority": True,
      "my_move": "じしん", "my_move_prio": 0, "opp_move": "じゃれつく", "opp_move_prio": 0,
      "my_ko_move": "じしん", "my_ko_move_prio": 0, "opp_ko_move": "かげうち", "opp_ko_move_prio": 1}))
check("きあいのタスキの持ち主を書く", RM.why_text("きあいのタスキ", "ガブリアス") == "（ガブリアスのきあいのタスキ込み）", RM.why_text("きあいのタスキ", "ガブリアス"))
check("多数派しきい値未満の技は少数派と添える", RM.rate_clause(19.0, minority_pct=20) == "（採用率19.0%・少数派）" and RM.rate_clause(68.1, minority_pct=20) == "（採用率68.1%）", RM.rate_clause(19.0, minority_pct=20))
long_rep = {**base, "my_hits": 5, "opp_hits": 3, "my_certain": True, "opp_certain": False, "opp_prob_int": 88, "my_s": 148, "opp_s": 106,
            "my_arch": "つるぎのまい型", "my_move": "シャドークロー", "opp_label": "ヒートロトム", "opp_move": "オーバーヒート", "opp_move_rate": 94.6,
            "my_reason": "たべのこし", "opp_reason": "ばけのかわ"}
lc = RM.reason_cell(long_rep, [], {}, subj="ミミッキュ", minority_pct=20)
check("理由セルは100字以内に収める（超えたら自分側の注記を落とす）", len(lc) <= 100 and "オーバーヒート" in lc, f"{len(lc)}: {lc}")
_ko = {**base, "win": True, "fast": False, "my_hits": 2, "opp_hits": 2, "ko_by_priority": True,
       "my_move": "シャドークロー", "my_move_prio": 0, "opp_move": "シャドーボール", "opp_move_prio": 0,
       "my_ko_move": "かげうち", "my_ko_move_prio": 1, "opp_ko_move": "シャドーボール", "opp_ko_move_prio": 0}
check("決着の技が表示技と違えば「最後は〜で」", RM.order_outcome_text(_ko).startswith("最後は優先度+1のかげうち"), RM.order_outcome_text(_ko))
check("決着の技が型の技構成に無ければ「選択技」", "選択技かげうち" in RM.order_outcome_text(_ko, {"シャドークロー", "じゃれつく"}), RM.order_outcome_text(_ko, {"シャドークロー"}))
_sd = {**base, "my_s": 80, "opp_s": 169, "my_base_s": 200, "opp_base_s": 169, "my_hits": 2, "opp_hits": 1}
check("低下で先後が入れ替わるときは「低下後」と明記", "S80（低下後）対S169" in RM.order_outcome_text(_sd), RM.order_outcome_text(_sd))
_sp = {**base, "my_s": 89, "opp_s": 200, "my_base_s": 178, "opp_base_s": 200, "my_hits": 2, "opp_hits": 1, "fast": False}
check("先後が変わらない低下（まひ後のS89）は変化前のS178で書く", "S178対S200" in RM.order_outcome_text(_sp), RM.order_outcome_text(_sp))
long2 = {**base, "my_hits": 1, "opp_hits": 2, "my_certain": True, "opp_certain": True, "win": True, "fast": False, "my_s": 139, "opp_s": 167,
         "my_arch": "非メガ・つるぎのまい型", "my_move": "きょけんとつげき", "opp_label": "メガリザードンX", "opp_move": "ドラゴンクロー", "opp_move_rate": 17.9,
         "my_reason": None, "opp_reason": "きあいのタスキ"}
lc2 = RM.reason_cell(long2, [], {}, subj="セグレイブ", minority_pct=20)
check("相手側の注記まで落として100字以内に収める", len(lc2) <= 100 and "ドラゴンクロー" in lc2, f"{len(lc2)}: {lc2}")
_gg = {**base, "win": True, "fast": False, "my_hits": 2, "opp_hits": 2, "ko_by_priority": True,
       "my_move": "グラススライダー", "my_move_prio": 0, "opp_move": "マジカルフレイム", "opp_move_prio": 0,
       "my_ko_move": "グラススライダー", "my_ko_move_prio": 0, "opp_ko_move": "マジカルフレイム", "opp_ko_move_prio": 0}
check("グラスフィールドのグラススライダーは優先度+1として書く（例外で止めない）", "グラスフィールドで優先度+1のグラススライダー" in RM.order_outcome_text(_gg), RM.order_outcome_text(_gg))
print("[rows] ko_by_priority で表示技に優先度が無いときは決め技（ko_move）の優先度で書く")
pr = {**base, "win": False, "fast": True, "my_hits": 2, "opp_hits": 2, "ko_by_priority": True,
      "my_move": "シャドークロー", "my_move_prio": 0, "opp_move": "じゃれつく", "opp_move_prio": 0,
      "my_ko_move": "シャドークロー", "my_ko_move_prio": 0, "opp_ko_move": "かげうち", "opp_ko_move_prio": 1}
t = RM.order_outcome_text(pr)
check("決め技かげうち(+1)で先に動かれる文になる", "かげうち" in t and "+1" in t and "先に倒されます" in t, t)
pr2 = {**pr, "win": True, "fast": False, "my_ko_move": "かげうち", "my_ko_move_prio": 1, "opp_ko_move": "じゃれつく", "opp_ko_move_prio": 0}
t2 = RM.order_outcome_text(pr2)
check("自分の決め技かげうち(+1)で先に倒せる文になる", "かげうち" in t2 and "先に倒せます" in t2, t2)
try:
    RM.order_outcome_text({**pr, "opp_ko_move": "じゃれつく", "opp_ko_move_prio": 0})
    check("優先度のある技が無いのに ko_by_priority なら例外", False, "例外が出なかった")
except ValueError:
    check("優先度のある技が無いのに ko_by_priority なら例外", True)

print("[claims] ×N のタイプ語の役割：「タイプには」は防御側、「への耐性」「技」は攻撃側")
c = [x for x in AC.extract_claims("はがねタイプにはほのお技が×2で通ります。") if x.kind == "mult"][0]
check("def_type=はがね / atk_type=ほのお", c.extra.get("def_type") == "はがね" and c.extra.get("atk_type") == "ほのお", str(c.extra))
c = [x for x in AC.extract_claims("じめんタイプを失うことで、いわ・どくへの耐性（ともに×0.5）も失います。") if x.kind == "mult"][0]
check("「どくへの耐性」は防御側にしない（atk=どく）", c.extra.get("atk_type") == "どく" and "def_type" not in c.extra, str(c.extra))

print("[style] 因果リント：仕組み語＋因果接続を検出し、名前だけの用法・EV配分・弱い語単独は拾わない")
cz = lambda s: [f.detail for f in AS.check_causal(s)]
check("メガ進化のタイミングの因果を拾う", cz("メガ進化は技を選んだターンにしか行えないため、交代直後はメガ進化前です。"))
check("アンコールの仕組みの因果を拾う", cz("先に動かれるとアンコールで固定されるため、積めません。"))
check("「がんじょう31.8%」の名前だけの用法は拾わない", not cz("※特性の採用率（がんじょう31.8%）は型ごとの集計が無いため全体の値です。"))
check("「アンコールを持たないため」は拾わない", not cz("アンコールを持たないため、相手の積みを縛れません。"))
check("「アンコール・めいそうのどちらも持たないため」は拾わない", not cz("アンコール・めいそうのどちらも持たないため、縛れません。"))
check("「受け出し」単独（弱い語1つ）は拾わない", not cz("こおり技は半減で受けられるため、受け出し先を用意できます。"))
check("弱い語2つ（特性・発動）は拾う", cz("物理技を受けても発動しますが、特性で上がるのはぼうぎょのみのため特殊には効きません。"))
check("EV配分の説明は拾わない", not cz("S振りのため特性の発動前に先手を取れます。"))
check("トリックルームは拾わない", not cz("トリックルームのため後手で動きます。"))
check("「M-6から」は因果接続にしない", not cz("メガ進化M-6から1位です。"))

if HAVE_GATE:
    print("[gate] 第2期：検証済みブロックの数値はスキップ／因果FAIL・allow検証／性格語なし nature_share／季節継続の順位／技名からタイプ")
    import render_sections as RS
    import render_matchup_rows as RR
    facts3 = {
        "schema": 1, "slug": "test-analysis-m7",
        "subject": {"name": "ミミッキュ", "icon": "0778-00", "season": "M-7", "forms": ["ミミッキュ"]},
        "sources": {"detail_date": "2026-10-11", "prev_detail_date": "2026-09-23", "prev_season": "M-6", "pool_version": "M-7/2026-10-15", "majority_pct": 20},
        "names": {"canonical": ["ミミッキュ", "ブラッキー", "メタグロス", "ガブリアス"], "aliases": {}, "known": ["ミミッキュ", "ブラッキー", "メタグロス", "ガブリアス"],
                  "moves": ["じゃれつく", "マジカルフレイム", "かげうち"], "items": ["ゴツゴツメット"], "arches": ["つるぎのまい型", "のろい・速攻型"], "natures": ["ずぶとい", "ようき"]},
        "cards": [
            {"arch": "つるぎのまい型", "item": "いのちのたま", "nature": "いじっぱり", "ability": "ばけのかわ", "ev": [2, 32, 0, 0, 0, 32], "moves": ["かげうち", "じゃれつく", "つるぎのまい", "シャドークロー"], "mpool": ["かげうち", "じゃれつく", "つるぎのまい", "シャドークロー", "ウッドハンマー"]},
            {"arch": "のろい・速攻型", "item": "いのちのたま", "nature": "いじっぱり", "ability": "ばけのかわ", "ev": [2, 32, 0, 0, 0, 32], "moves": ["かげうち", "じゃれつく", "のろい", "トリックルーム"], "mpool": ["かげうち", "じゃれつく", "のろい", "トリックルーム"]},
        ],
        "facts": [
            {"id": "usage_rank/ミミッキュ", "kind": "usage_rank", "pokemon": "ミミッキュ", "value": 5},
            {"id": "usage_rank/ミミッキュ/M-6", "kind": "usage_rank", "pokemon": "ミミッキュ", "season": "M-6", "value": 11},
            {"id": "usage_rank/ガブリアス", "kind": "usage_rank", "pokemon": "ガブリアス", "value": 1},
            {"id": "usage_rank/メタグロス", "kind": "usage_rank", "pokemon": "メタグロス", "value": 13},
            {"id": "usage_rank/ブラッキー", "kind": "usage_rank", "pokemon": "ブラッキー", "value": 28},
            {"id": "nature_share/ブラッキー/たべのこし型/ずぶとい", "kind": "nature_share", "pokemon": "ブラッキー", "arch": "たべのこし型", "nature": "ずぶとい", "value": 60.7},
            {"id": "arch_move_share/ミミッキュ/のろい・速攻型/のろい", "kind": "arch_move_share", "pokemon": "ミミッキュ", "arch": "のろい・速攻型", "move": "のろい", "value": 86.3},
            {"id": "arch_build_share/ミミッキュ/のろい・速攻型/かげうち|じゃれつく|のろい|トリックルーム", "kind": "arch_build_share", "pokemon": "ミミッキュ", "arch": "のろい・速攻型", "moves": ["かげうち", "じゃれつく", "のろい", "トリックルーム"], "value": 24.1},
            {"id": "types/メタグロス", "kind": "types", "pokemon": "メタグロス", "value": ["はがね", "エスパー"]},
            {"id": "types/ミミッキュ", "kind": "types", "pokemon": "ミミッキュ", "value": ["ゴースト", "フェアリー"]},
            {"id": "move_power/マジカルフレイム", "kind": "move_power", "move": "マジカルフレイム", "type": "ほのお", "category": "特殊", "value": 75},
            {"id": "type_eff/ほのお/メタグロス", "kind": "type_eff", "atk_type": "ほのお", "defender": "メタグロス", "value": 2.0},
            {"id": "type_eff/ほのお/ミミッキュ", "kind": "type_eff", "atk_type": "ほのお", "defender": "ミミッキュ", "value": 1.0},
            {"id": "type_chart/ほのお/はがね", "kind": "type_chart", "atk_type": "ほのお", "def_type": "はがね", "value": 2.0},
            {"id": "const/stage_mult/2", "kind": "const", "name": "2段階", "value": 2.0},
            {"id": "verdict/ガブリアス", "kind": "verdict", "opp": "ガブリアス", "opp_sp": "ガブリアス", "value": "mixed", "reasons": ["代表型によって勝敗が割れる"]},
            {"id": "mu/つるぎのまい型/ガブリアス#1", "kind": "matchup", "opp": "ガブリアス", "opp_sp": "ガブリアス", "opp_label": "ガブリアス", "opp_idx": 1, "opp_item": "きあいのタスキ", "opp_nature": "ようき", "opp_ev": [2, 32, 0, 0, 0, 32], "opp_share": 40.0,
             "my_arch": "つるぎのまい型", "my_move": "じゃれつく", "my_move_rate": 98.0, "my_hits": 2, "my_certain": True, "opp_move": "じしん", "opp_move_rate": 68.1, "opp_hits": 2, "opp_certain": True,
             "my_s": 148, "opp_s": 169, "fast": False, "ko_first": True, "ko_by_priority": False, "win": True, "sym": "○", "representative": False, "verdict": "mixed"},
            {"id": "mu/のろい・速攻型/ガブリアス#1", "kind": "matchup", "opp": "ガブリアス", "opp_sp": "ガブリアス", "opp_label": "ガブリアス", "opp_idx": 1, "opp_item": "きあいのタスキ", "opp_nature": "ようき", "opp_ev": [2, 32, 0, 0, 0, 32], "opp_share": 40.0,
             "my_arch": "のろい・速攻型", "my_move": "ウッドハンマー", "my_move_rate": 22.0, "my_hits": 2, "my_certain": True, "opp_move": "じしん", "opp_move_rate": 68.1, "opp_hits": 2, "opp_certain": True,
             "my_s": 148, "opp_s": 169, "fast": False, "ko_first": False, "ko_by_priority": False, "win": False, "sym": "△", "representative": False, "verdict": "mixed"},
            {"id": "mu/つるぎのまい型/ガブリアス#2", "kind": "matchup", "opp": "ガブリアス", "opp_sp": "ガブリアス", "opp_label": "ガブリアス", "opp_idx": 2, "opp_item": "こだわりスカーフ", "opp_nature": "ようき", "opp_ev": [2, 32, 0, 0, 0, 32], "opp_share": 30.0,
             "my_arch": "つるぎのまい型", "my_move": "じゃれつく", "my_move_rate": 98.0, "my_hits": 2, "my_certain": True, "opp_move": "じしん", "opp_move_rate": 68.1, "opp_hits": 2, "opp_certain": True,
             "my_s": 148, "opp_s": 253, "fast": False, "ko_first": False, "ko_by_priority": False, "win": False, "sym": "×", "representative": False, "verdict": "mixed"},
            {"id": "mu/のろい・速攻型/ガブリアス#2", "kind": "matchup", "opp": "ガブリアス", "opp_sp": "ガブリアス", "opp_label": "ガブリアス", "opp_idx": 2, "opp_item": "こだわりスカーフ", "opp_nature": "ようき", "opp_ev": [2, 32, 0, 0, 0, 32], "opp_share": 30.0,
             "my_arch": "のろい・速攻型", "my_move": "ウッドハンマー", "my_move_rate": 5.0, "my_hits": 1, "my_certain": True, "opp_move": "じしん", "opp_move_rate": 68.1, "opp_hits": 2, "opp_certain": True,
             "my_s": 148, "opp_s": 253, "fast": False, "ko_first": True, "ko_by_priority": True, "win": True, "sym": "○", "representative": False, "verdict": "mixed"},
        ],
    }
    _f = json.loads(json.dumps(facts3))
    _f["facts"] += [{"id": "adopt/move/ミミッキュ/のろい/M-6", "kind": "adopt_rate", "category": "move", "pokemon": "ミミッキュ", "name": "のろい", "season": "M-6", "value": 10.0},
                    {"id": "adopt/move/ミミッキュ/のろい/M-7", "kind": "adopt_rate", "category": "move", "pokemon": "ミミッキュ", "name": "のろい", "season": "M-7", "value": 30.0},
                    {"id": "diff/move/ミミッキュ/のろい", "kind": "adopt_rate_diff", "category": "move", "pokemon": "ミミッキュ", "name": "のろい", "value": 20.0},
                    {"id": "ams/ミミッキュ/つるぎのまい型/のろい", "kind": "arch_move_share", "pokemon": "ミミッキュ", "arch": "つるぎのまい型", "move": "のろい", "value": 25.0}]
    _f["sources"]["prev_season"] = "M-6"
    _dm = RS.diff_movers(_f)
    check("型カードに無い技を、型プールの推定割合だけでその型の共通技に数えない", any("のろい" in x and "のろい・速攻型だけが持つ" in x for x in _dm), str(_dm))
    rows = RS.arch_grid_rows(facts3)
    check("型で判定が違う個体だけが arch_grid の行になる（○と△）", len(rows["rows"]) == 1 and rows["rows"][0]["syms"] == {"つるぎのまい型": "○", "のろい・速攻型": "△"}, str(rows))
    blocks = RS.render_all(facts3)
    check("arch_grid / partner_grid / diff_movers の id が揃う", {"weak", "strong", "arch_grid", "partner_grid", "diff_movers"} <= set(blocks), str(list(blocks)))
    check("arch_grid の行に判定記号と選択技の※が出て、個体シェア（推定）は出ない", "40%" not in blocks["arch_grid"] and "○" in blocks["arch_grid"] and "△※" in blocks["arch_grid"], blocks["arch_grid"])
    sha3 = RR.facts_sha1(facts3)
    head = "---\ntitle: 't'\ndescription: 'x'\npubDate: '2026-10-14'\ndraft: true\n---\n\n※本記事の使用率・採用率データは2026-10-11時点のものです。\n\n"
    body = head + "\n".join(RR.wrap(k, v, sha3) for k, v in blocks.items()) + "\n\n"
    md_ok = body + "はがねタイプにはほのお技が×2で通ります。メタグロスにはマジカルフレイムが×2で通ります。ミミッキュはM-6の11位から5位に上がりました。\n"
    md_ng = body + ("このポケモンは60.7%です。ミミッキュはM-6から引き続き5位です。\n\n"
                    "のろい・速攻型でのろいを持つ個体は86.3%です。ずぶといブラッキーは60.7%です。ガブリアスのこの個体は40.0%です。\n\n"
                    "アンコールで固定されるため積めません。<!-- gate:allow causal reason=\"engine:scripts/nope.py:L1\" -->\n\n"
                    "メガ進化は技を選んだターンにしか行えないため交代直後はメガ進化前です。\n")
    with tempfile.TemporaryDirectory() as d:
        fp3 = os.path.join(d, "facts3.json"); json.dump(facts3, open(fp3, "w"), ensure_ascii=False)
        p_ok = os.path.join(d, "ok.md"); open(p_ok, "w").write(md_ok)
        p_ng = os.path.join(d, "ng.md"); open(p_ng, "w").write(md_ng)
        r_ok = AG.run_gate(p_ok, fp3, today="2026-10-14", slug="test-analysis-m7")
        r_ng = AG.run_gate(p_ng, fp3, today="2026-10-14", slug="test-analysis-m7")
    check("生成ブロック＋正しい本文は FAIL 0", r_ok["counts"]["FAIL"] == 0, json.dumps([r for r in r_ok["results"] if r["level"] == "FAIL"], ensure_ascii=False)[:800])
    check("生成ブロック内の数値は rows:<id> で OK 扱い", any(r.get("fact", "").startswith("rows:") for r in r_ok["results"] if r["level"] == "OK"), "")
    ng = {(r["id"], r["raw"]) for r in r_ng["results"] if r["level"] == "FAIL"}
    check("性格語の無い 60.7% は nature_share と一致させない", ("no_fact", "60.7%") in ng or ("estimate_pct", "60.7%") in ng, str(ng))
    check("型内の技シェア 86.3% は推定値なので estimate_pct で FAIL", ("estimate_pct", "86.3%") in ng, str(ng))
    check("性格シェア 60.7%（性格語あり）も estimate_pct で FAIL", ("estimate_pct", "60.7%") in ng, str(ng))
    check("個体シェア 40.0% も estimate_pct で FAIL", ("estimate_pct", "40.0%") in ng, str(ng))
    check("M-6=11位 なのに「引き続き5位」は FAIL", ("no_fact", "5位") in ng, str(ng))
    md_col = body + ('<table>\n<thead>\n<tr>\n  <th>項目</th>\n  <th>M-6</th>\n  <th>M-7</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n'
                     '  <td>使用率順位</td>\n  <td>11位</td>\n  <td>5位</td>\n</tr>\n</tbody>\n</table>\n')
    with tempfile.TemporaryDirectory() as d:
        fp7 = os.path.join(d, "facts7.json"); json.dump(facts3, open(fp7, "w"), ensure_ascii=False)
        p7 = os.path.join(d, "col.md"); open(p7, "w").write(md_col)
        r7 = AG.run_gate(p7, fp7, today="2026-10-14", slug="test-analysis-m7")
    check("表のM-6列の「11位」は前季の順位として照合する", not any(r["raw"] == "11位" for r in r7["results"] if r["level"] == "FAIL"), str([r for r in r7["results"] if r["level"] == "FAIL"])[:300])
    check("不正な engine 参照の gate:allow causal は FAIL", any(i == "causal_allow_invalid" for i, _ in ng), str(ng))
    check("メガ進化のタイミングの因果は causal_mechanic で FAIL", any(i == "causal_mechanic" for i, _ in ng), str(ng))
    md_card = body + "### 型1：つるぎのまい型\n\n<div>\n<div class=\"build-header\"><strong style=\"font-size:1.05em\">つるぎのまい型</strong></div>\n</div>\n\n積む型です。\n\n**強み:**\n\n火力が高いです。\n\n**弱み:**\n\nメタグロスに勝てません。\n\n---\n\n## 次\n"
    with tempfile.TemporaryDirectory() as d:
        fp4 = os.path.join(d, "facts4.json"); json.dump(facts3, open(fp4, "w"), ensure_ascii=False)
        p4 = os.path.join(d, "card.md"); open(p4, "w").write(md_card)
        r4 = AG.run_gate(p4, fp4, today="2026-10-14", slug="test-analysis-m7")
    check("強み/弱みの相手名（メタグロス）は card_opponent_name で FAIL", any(r["id"] == "card_opponent_name" and "メタグロス" in r["raw"] for r in r4["results"]), str([r for r in r4["results"] if r["level"] == "FAIL"]))
    _ci = "### 型1：A型\n\n<div>\n<div>x</div>\n</div>\n\n{}\n\n<!-- gate:rows start id=card:1 facts=abc -->\ny\n<!-- gate:rows end id=card:1 -->\n"
    with tempfile.TemporaryDirectory() as d:
        fpc = os.path.join(d, "factsc.json"); json.dump(facts3, open(fpc, "w"), ensure_ascii=False)
        rc = {}
        for k, s in (("two", "積む型です。後続につなぎます。"), ("one", "積む型です。")):
            pc = os.path.join(d, f"{k}.md"); open(pc, "w").write(body + _ci.format(s))
            rc[k] = {r["id"] for r in AG.run_gate(pc, fpc, today="2026-10-14", slug="test-analysis-m7")["results"] if r["level"] == "WARN"}
    with tempfile.TemporaryDirectory() as d:
        fph = os.path.join(d, "factsh.json"); json.dump(facts3, open(fph, "w"), ensure_ascii=False)
        ph = os.path.join(d, "hand.md"); open(ph, "w").write(body + "### 種族値\n\n<div style=\"max-width:480px;margin:16px 0\">\n<span>合計</span>\n</div>\n")
        rh = {r["id"] for r in AG.run_gate(ph, fph, today="2026-10-14", slug="test-analysis-m7")["results"] if r["level"] == "FAIL"}
    check("手書きの種族値バーは base_stats_hand で FAIL", "base_stats_hand" in rh, str(rh))
    with tempfile.TemporaryDirectory() as d:
        fpd = os.path.join(d, "factsd.json"); json.dump(facts3, open(fpd, "w"), ensure_ascii=False)
        rd = {}
        for k, s in (("ng", "ミミッキュはM-6の11位から使用率5位に後退しました。"), ("ok", "ミミッキュはM-6の11位から使用率5位に浮上しました。")):
            pd_ = os.path.join(d, f"{k}.md"); open(pd_, "w").write(body + s + "\n")
            rd[k] = {r["id"] for r in AG.run_gate(pd_, fpd, today="2026-10-14", slug="test-analysis-m7")["results"] if r["level"] == "FAIL"}
    check("前季11位→5位を「後退」と書くと rank_direction、「浮上」は通す", "rank_direction" in rd["ng"] and "rank_direction" not in rd["ok"], str(rd))
    _bsf = {"subject": {"name": "A", "forms": ["A", "メガA"]}, "cards": [{"item": "Aナイト"}],
            "facts": [{"kind": "base_stat", "pokemon": p, "stat": k, "value": v} for p, vs in (("A", [65, 130, 60, 75, 60, 75]), ("メガA", [65, 154, 60, 75, 60, 151]))
                      for k, v in zip("HABCDS", vs)] + [{"kind": "mega_form", "form": "メガA", "stone": "Aナイト"}]}
    import render_sections as RSx
    _bsh = RSx.render_base_stats(_bsf)
    check("種族値バー：増加分は同色の薄いバー（緑のバーにしない）・見出しにメガ名", "opacity:0.35" in _bsh and "background:#059669;height" not in _bsh
          and _bsh.startswith("### 種族値（通常→メガA）") and "+76" in _bsh, _bsh[:200])
    check("型カードの説明文2文は card_intro_long で WARN、1文は通す", "card_intro_long" in rc["two"] and "card_intro_long" not in rc["one"], str(rc))
    md_split = ("---\ntitle: 't'\ndescription: 'x'\npubDate: '2026-10-14'\ndraft: true\n---\n\n"
                "ミミッキュはつるぎのまい型とのろい・速攻型に分かれます。\n\n---\n\n"
                "### 型1：つるぎのまい型\n\nじゃれつくが主軸です。\n\n---\n\n## 苦手\n\nつるぎのまい型の選択技ウッドハンマーは確定2発。\n")
    with tempfile.TemporaryDirectory() as d:
        fp5 = os.path.join(d, "facts5.json"); json.dump(facts3, open(fp5, "w"), ensure_ascii=False)
        p5 = os.path.join(d, "split.md"); open(p5, "w").write(md_split)
        r5 = AG.run_gate(p5, fp5, today="2026-10-14", slug="test-analysis-m7")
    ids5 = {r["id"] for r in r5["results"] if r["level"] == "FAIL"}
    check("冒頭で2つ以上の型名を出すと intro_arch_split", "intro_arch_split" in ids5, str(ids5))
    md_order = md_split.replace("### 型1：つるぎのまい型", "### 型1：のろい・速攻型\n\nx\n\n---\n\n### 型2：つるぎのまい型")
    with tempfile.TemporaryDirectory() as d:
        fp6 = os.path.join(d, "facts6.json"); json.dump(facts3, open(fp6, "w"), ensure_ascii=False)
        p6 = os.path.join(d, "order.md"); open(p6, "w").write(md_order)
        r6 = AG.run_gate(p6, fp6, today="2026-10-14", slug="test-analysis-m7")
    _f8 = json.loads(json.dumps(facts3))
    _f8["facts"] += [{"id": "base_stat/ミミッキュ/A", "kind": "base_stat", "pokemon": "ミミッキュ", "stat": "A", "value": 90},
                     {"id": "base_stat/メガミミッキュ/A", "kind": "base_stat", "pokemon": "メガミミッキュ", "stat": "A", "value": 110},
                     {"id": "mega_form/ミミッキュ/メガミミッキュ", "kind": "mega_form", "pokemon": "ミミッキュ", "form": "メガミミッキュ", "stone": "x"}]
    md_bs = body + ('<div><span style="white-space:nowrap">こうげき</span>\n<span style="width:32px;text-align:right">90</span>'
                    '<span style="width:32px;text-align:right">90</span></div>\n')
    with tempfile.TemporaryDirectory() as d:
        fp8 = os.path.join(d, "facts8.json"); json.dump(_f8, open(fp8, "w"), ensure_ascii=False)
        p8 = os.path.join(d, "bs.md"); open(p8, "w").write(md_bs)
        r8 = AG.run_gate(p8, fp8, today="2026-10-14", slug="test-analysis-m7")
    check("種族値バー表のメガ側に通常形の値を書くと base_stat_chart", any(r["id"] == "base_stat_chart" for r in r8["results"] if r["level"] == "FAIL"), str([r["id"] for r in r8["results"] if r["level"] == "FAIL"]))
    check("型カードの順が spec と違うと card_order", any(r["id"] == "card_order" for r in r6["results"] if r["level"] == "FAIL"), str([r["id"] for r in r6["results"] if r["level"] == "FAIL"]))
    check("選択技の説明は表の注記が出す（本文で触れなくても FAIL にしない）", "card_selected_move_missing" not in ids5 and "選択技" in RR.NOTE_ROW, str(ids5))

_tg = "---\ntitle: x\n---\n\nM-7シーズンのウォッシュロトムは使用率28位（M-6: 27位）。\n\n弱点はくさタイプのみです（特性ふゆう）。\n\n| a | b |\n|---|---|\n| 1位 | 2位。 |\n"
_tgf = [x for x in AS.check_all(_tg) if x.kind == "体言止め"]
check("体言止め：括弧書きの前で名詞止めなら FAIL、述語ありと表は通す", len(_tgf) == 1 and _tgf[0].line == 5, str([(x.line, x.kind) for x in _tgf]))
import article_normalize as AN  # noqa: E402
check("正規化：使用率N位（…）。→ 使用率N位です（…）。", "使用率28位です（M-6: 27位）。" in AN.normalize(_tg) and not [x for x in AS.check_all(AN.normalize(_tg)) if x.kind == "体言止め"])

_rp = "---\ntitle: x\n---\n\nとくぼう100・すばやさ109が高いです。ただしすばやさ109・S177は5体に上を取られます。\n\nEVはH32-A32-S2で、A197から394まで上がり、A197（EV32）です。\n"
_rpf = [x for x in AS.check_all(_rp) if x.kind == "能力値の繰り返し"]
check("能力値の繰り返し：同じ段落のすばやさ109×2は FAIL、EV表記と「〜から」は数えない", len(_rpf) == 1 and _rpf[0].line == 5, str([(x.line, x.detail) for x in _rpf]))

print("[rows] 速い側が先制技で倒された行（koByPriority が立たない）は素早さではなく優先度で書く")
_pr = {**base, "win": False, "fast": True, "my_s": 177, "opp_s": 162, "my_hits": 5, "opp_hits": 1,
       "my_move": "ふぶき", "opp_move": "バレットパンチ", "opp_move_prio": 1, "my_ko_move": None, "my_ko_move_prio": None,
       "opp_ko_move": "バレットパンチ", "opp_ko_move_prio": 1}
_prt = RM.order_outcome_text(_pr)
check("先制技で倒された行は「優先度+1のバレットパンチで先に動かれ」", "優先度+1のバレットパンチで先に動かれ" in _prt and "先手" not in _prt, _prt)
_sc = {**base, "win": True, "fast": True, "my_s": 300, "opp_s": 200, "my_hits": 1, "opp_hits": 2, "my_item": "こだわりスカーフ", "my_base_s": 200}
check("スカーフで上がった素早さは「スカーフ込み」", "S300（スカーフ込み）" in RM.order_outcome_text(_sc), RM.order_outcome_text(_sc))

print("[sections] 型で判定が割れない記事のまとめは「型による有利不利の違い」の表を参照しない")
import render_sections as RSX  # noqa: E402
_sf = {"subject": {"name": "x", "season": "M-7"}, "sources": {"prev_season": "M-6"}, "facts": [],
       "cards": [{"arch": "a型", "moves": ["p", "q"], "mpool": [], "item": "i", "nature": "n", "ability": "t", "ev": "H32", "real_stats": {}},
                 {"arch": "b型", "moves": ["p", "r"], "mpool": [], "item": "i", "nature": "n", "ability": "t", "ev": "H32", "real_stats": {}}]}
check("arch_grid が空ならまとめで表を参照しない", "型による有利不利の違い" not in "".join(RSX.summary_lines(_sf, 3, 4, False)))
check("arch_grid があれば参照する", "型による有利不利の違い" in "".join(RSX.summary_lines(_sf, 3, 4, True)))
_sl = RSX.summary_lines(_sf, 3, 4, True)
check("まとめは強み・弱み・型の選び分けの要点を出す（数と型名の羅列だけにしない）",
      "**強み**" in _sl and "**弱み**" in _sl and "**型の選び分け**" in _sl and any("「a型」" in l and "q" in l for l in _sl), "\n".join(_sl))
check("技表の効果文：タグ残りと末尾の優先度の重複を落とす",
      RSX._clean_effect("優先度+1。パンチ必ず先制できる。(優先度+1)") == "優先度+1。優先度0の技より先に出せる。", RSX._clean_effect("優先度+1。パンチ必ず先制できる。(優先度+1)"))

print("[facts] 積み技の効果文：能力名を読点・「と」で並べる書き方と「ずつ」も読む")
import article_facts as AFX  # noqa: E402
_stg = lambda e: [(x["stat"], x["value"], x["direction"]) for x in AFX.stage_changes(e)]
check("ちょうのまい（特攻、特防、素早さ）", _stg("自分の特攻、特防、素早さを1段階上げる。") == [("C", 1, "up"), ("D", 1, "up"), ("S", 1, "up")], str(_stg("自分の特攻、特防、素早さを1段階上げる。")))
check("めいそう（特攻と特防が1段階ずつ上がる）", _stg("自分の特攻と特防が1段階ずつ上がる。") == [("C", 1, "up"), ("D", 1, "up")], str(_stg("自分の特攻と特防が1段階ずつ上がる。")))
check("からをやぶる（下げて、上げる）", _stg("自分の防御・特防を1段階下げて、攻撃・特攻・素早さを2段階上げる。") == [("B", 1, "down"), ("D", 1, "down"), ("A", 2, "up"), ("C", 2, "up"), ("S", 2, "up")])

_cf = {"subject": {"name": "x", "season": "M-7"}, "sources": {}, "facts": [],
       "cards": [{"arch": "a型", "moves": ["m1", "m2", "m3", "m4"], "item": "i", "ability": "あめうけざら", "mab": "メガランチャー", "real_stats": {}},
                 {"arch": "b型", "moves": ["m1", "m2", "m3", "m5"], "item": "i", "ability": "げきりゅう", "mab": "メガランチャー", "real_stats": {}}]}
check("メガ進化する型のカードに進化前の特性を違いとして出さない", not any("特性" in x for x in RSX.card_diff_lines(_cf, 0)), str(RSX.card_diff_lines(_cf, 0)))

_ce = "### 型1：つるぎのまい型\n\n・つるぎのまい\n\nつるぎのまいで攻撃を2段階上げてから攻めこむ型です。わるだくみで自分の特攻を2段階上げ、C212からC424まで伸ばせる型です。\n\n<!-- gate:rows start id=card:1 facts=ab -->\nx\n<!-- gate:rows end id=card:1 -->\n"
_cer = AS.card_effect_restatements(_ce, {"つるぎのまい": "自分の攻撃を2段階上げる。", "わるだくみ": "自分の特攻を2段階上げる。"})
check("型カードの説明文：効果文の言い直しだけの文を拾い、情報を足した文は通す", [x[2] for x in _cer] == ["つるぎのまい"] and _cer[0][0] == 5, str(_cer))

_trp = os.path.join(os.path.dirname(os.path.dirname(HERE)), "_local/article_facts/hatterene-analysis-m7.json")
if os.path.exists(_trp):
    _trr = RM.render(json.load(open(_trp)))
    check("トリックルームを型の技に持つ被写体の表には「トリックルームを使わない場合」の注記", RM.TR_NOTE in _trr["weak"] or RM.TR_NOTE in _trr["strong"])

_lp = {**base, "win": False, "fast": True, "my_s": 95, "opp_s": 67, "my_hits": 4, "opp_hits": 4, "ko_by_priority": True,
       "my_move": "シャドークロー", "opp_move": "じしん", "my_move_prio": 0, "opp_move_prio": 0,
       "my_ko_move": "かげうち", "my_ko_move_prio": 1, "opp_ko_move": "じしん", "opp_ko_move_prio": 0}
try:
    _lpt = RM.order_outcome_text(_lp)
except ValueError as e:
    _lpt = "ERR " + str(e)
check("負けた側だけが先制技を持つ優先度決着の行で止まらない", not _lpt.startswith("ERR") and "倒されます" in _lpt, _lpt)

_mj = {"subject": {"name": "x", "season": "M-7"}, "sources": {}, "facts": [],
       "cards": [{"arch": f"{k}型", "moves": [f"m{k}", "a", "b", "c"], "item": "i", "real_stats": {"H": 150, "A": 80, "B": 100, "C": 120, "D": 100, "S": s}}
                 for k, s in (("a", 90), ("b", 90), ("c", 90), ("d", 120))]}
_mjl = ["".join(RSX.card_diff_lines(_mj, i)) for i in range(4)]
check("過半数の型が同じ実数値なら「最も高い/低い」を出さず、外れた型にだけ出す", all("すばやさ" not in x for x in _mjl[:3]) and "すばやさ120" in _mjl[3], str(_mjl))

import article_normalize as ANX  # noqa: E402
_ac = [{"moves": ["a", "b"], "item": "x", "nature": "n", "ev": [1]}, {"moves": ["a", "c"], "item": "y", "nature": "n", "ev": [1]}]
check("型の分かれ方の定型文は、型カードで違う要素だけに絞る", ANX.normalize("技・持ち物・性格・EVの組み合わせから、2つの型を紹介します。", _ac) == "技・持ち物の組み合わせから、2つの型を紹介します。")

_sp = {"subject": {"name": "x", "season": "M-7"}, "sources": {}, "facts": [
    {"id": "mp1", "kind": "move_power", "move": "s1", "type": "みず", "category": "special", "value": 90},
    {"id": "mp2", "kind": "move_power", "move": "p1", "type": "みず", "category": "physical", "value": 90}],
       "cards": [{"arch": "特殊型", "moves": ["s1"], "item": "i", "real_stats": {"H": 1, "A": 120, "B": 1, "C": 1, "D": 1, "S": 1}},
                 {"arch": "物理型", "moves": ["p1"], "item": "j", "real_stats": {"H": 1, "A": 100, "B": 1, "C": 1, "D": 1, "S": 1}}]}
check("特殊技だけの型のカードに、こうげきを実数値の差として出さない", "こうげき" not in "".join(RSX.card_diff_lines(_sp, 0)), str(RSX.card_diff_lines(_sp, 0)))

_ghp = os.path.join(os.path.dirname(os.path.dirname(HERE)), "_local/article_facts/goodra-hisui-analysis-m7.json")
if os.path.exists(_ghp):
    _ghl = [x for x in RSX.diff_movers(json.load(open(_ghp))) if x.startswith(("- なまいき", "- ひかえめ"))]
    check("性格の採用率変化は、型カードの性格を持つ型を主語にする（含まれない・すべての型に共通と誤らない）",
          all("含まれません" not in x and "すべての型" not in x for x in _ghl) and any("たてこもる型が選んでいる" in x for x in _ghl), str(_ghl))

print(f"\n{PASS} passed, {FAIL} failed")
if FAIL:
    sys.exit(1)
