#!/usr/bin/env python3
"""
記事内の「検証可能な数値主張」を機械的に抜き出すチェックリスト生成ツール。

目的：
  レビューが「気づいた範囲」でしか数値を検算しないと、型内の性格/EV多様性や
  技の効果量（能力ランク等）を記憶・推測で書いた誤りを見落とす（ガブリアスM-7記事で多発）。
  このスクリプトは記事を正規表現でスキャンし、検算が必要な数値主張を**網羅的に**
  リストアップする。レビュー・執筆時は、このリストの全項目について
  「どのコマンドで検算したか」を1行ずつ埋めてから公開可否を判定する。

このスクリプト自身は正誤を判定しない（判定にはDB/JSON/engineへの実際の問い合わせが必要）。
あくまで「見落としなく検算対象を列挙する」ための網羅性担保ツール。

使い方:
  python3 scripts/article_verify_claims.py src/content/blog/garchomp-analysis-m7.md
  python3 scripts/article_verify_claims.py src/content/blog/garchomp-analysis-m7.md --json
"""
import re
import sys
import json
import argparse

# (ラベル, 正規表現, 検算方法のヒント, tier)
# tier1 = 「導出・計算」を要する主張（手計算ミスが実際に起きたカテゴリ）。公開可否判定では必ず全件潰す。
# tier2 = DBから直接コピーする値（ミスの主因は転記ミス・日付違いで、tier1より低リスク）。
PATTERNS = [
    ("実数値(A/B/C/D/S/H)", r'[ABCDSH]実数値\D{0,6}(\d{2,4})', None, 1),
    ("ステータス記号+数値 (A200/S154等)", r'(?<![A-Za-z0-9])([ABCDSH])(\d{2,4})(?![A-Za-z0-9%])',
     "python3 -c \"print(int((((種族値*2+31+EV//4)*50)//100+5)*補正))\" で検算。EVは32スケール表記に注意。同じ型内に複数の性格が存在する場合、少数派の性格がこの数値と同じEV配分を使っているかをarchetypes.json/type_groups.jsonで必ず確認する（推測禁止）", 1),
    ("能力ランク段階 (N段階)", r'(\d)段階', "sqlite3 scripts/pokenavi.db \"SELECT name_jp, effect_text FROM move_master WHERE name_jp='技名';\" で段階数を確認（記憶で書かない）", 1),
    ("倍率 (×N.N)", r'×\s*(\d+(?:\.\d+)?)', "段階数×0.5+1.0 (上昇) / 1.0-段階数×... (下降) で検算。技効果由来の倍率はmove_master.effect_textで確認", 1),
    ("確定/乱数N発", r'(確定|乱数)(\d)発', "scripts/simulator/damage.py の calc_damage 相当、またはdump_matchups系スクリプトの出力で検算（手計算しない）", 1),
    ("16通り中N通り", r'16通り中(\d+)通り', "ダメージロール計算の生成元を確認（乱数幅の算出根拠）", 1),
    ("パーセンテージ（汎用）", r'(\d+(?:\.\d+)?)\s*%', "DBの実測値(pokemon_usage/pokemon_moves/pokemon_items/pokemon_natures/pokemon_evs/pokemon_abilities)か、archetypes.jsonのtrend/shareかを明示して照合", 2),
    ("採用率/使用率順位", r'採用率\D{0,4}(\d+(?:\.\d+)?)\s*%|使用率\D{0,4}(\d+)\s*位', "sqlite3 scripts/pokenavi.db で season/rule/crawled_dateを指定して再確認", 2),
]

NATURE_WORDS = ["いじっぱり", "ようき", "おくびょう", "ひかえめ", "わんぱく", "しんちょう", "おだやか", "むじゃき", "ずぶとい"]


def is_css_noise(line: str) -> bool:
    """種族値バー等のCSS装飾行（width:NN%等）はprose上の新規主張ではないので除外する。"""
    return "style=" in line and ("width:" in line or "linear-gradient" in line)


def scan(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    findings = []
    seen_on_line = set()
    for i, line in enumerate(lines, start=1):
        if is_css_noise(line):
            continue
        for label, pattern, hint, tier in PATTERNS:
            for m in re.finditer(pattern, line):
                key = (i, m.start(), m.end())
                # 同じ文字範囲が複数パターンに重複マッチした場合は最初の1件だけ残す
                if any(k[0] == i and not (k[2] <= m.start() or k[1] >= m.end()) for k in seen_on_line):
                    continue
                seen_on_line.add(key)
                findings.append({
                    "line": i,
                    "label": label,
                    "match": m.group(0),
                    "context": line.strip()[:160],
                    "verify_hint": hint,
                    "tier": tier,
                })
        # 性格ワードが複数種類、同じ段落(=同じ行)に出てきたら「型内多様性」の可能性フラグ
        natures_in_line = [w for w in NATURE_WORDS if w in line]
        if len(natures_in_line) >= 2:
            findings.append({
                "line": i,
                "label": "複数性格の同時言及（型内多様性注意）",
                "match": "/".join(natures_in_line),
                "context": line.strip()[:160],
                "verify_hint": "各性格ごとにEV配分が異なる可能性がある。archetypes.jsonのtrend.evs/sets[]または元データ(type_groups.json)で性格ごとの実際のEV配分を確認してから数値を書く（『補正だけ外れる』という推測は禁止）",
                "tier": 1,
            })
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tier1-only", action="store_true",
                     help="導出・計算を要する高リスク項目（実数値・段階・倍率・確定数等）のみ表示する")
    args = ap.parse_args()

    findings = scan(args.path)
    if args.tier1_only:
        findings = [f for f in findings if f["tier"] == 1]

    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        return

    if not findings:
        print("検証対象の数値主張は検出されませんでした（正規表現の範囲内）。")
        return

    print(f"=== {args.path}: 検算対象 {len(findings)} 件 ===\n")
    print("この記事を『公開可』と判定する前に、以下の全項目について実際にコマンドを")
    print("実行して検算したことを確認する（推測・記憶での照合は不可）。\n")
    for idx, f in enumerate(findings, start=1):
        print(f"[{idx}] L{f['line']}: {f['label']} -> \"{f['match']}\"")
        print(f"     文脈: {f['context']}")
        if f["verify_hint"]:
            print(f"     検算方法: {f['verify_hint']}")
        print()


if __name__ == "__main__":
    main()
