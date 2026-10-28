#!/usr/bin/env python3
"""記事本文の表記ゆれを機械的に揃える（内容は変えない）。gate:rows の生成ブロックは触らない。

使い方: python3 scripts/article_normalize.py src/content/blog/<slug>.md [--check]
  --check … 書き換えずに、揃える箇所があれば exit 1
"""
import argparse
import json
import re
import sys

# 能力名はゲーム内表記（ひらがな）に揃える。2026-10-25 カイリューのレビューで「素早さ」「すばやさ」の混在を指摘
REPLACE = [("素早さ", "すばやさ")]
BLOCK_RE = re.compile(r"(<!-- gate:rows start id=[^\s]+ facts=[0-9a-f]+ -->.*?<!-- gate:rows end id=[^\s]+ -->)", re.S)


def _strip_col_season(seg):
    """列見出しが「M-6」の列のセルにある「（M-6）」を消す（季節は列見出しで決まる。ゲートも列見出しで照合する）。"""
    def fix_table(tm):
        tbl = tm.group(0)
        heads = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", tbl, re.S)]

        def fix_row(rm):
            cells = list(re.finditer(r"(<td[^>]*>)(.*?)(</td>)", rm.group(0), re.S))
            row = rm.group(0)
            for ci, cm in reversed(list(enumerate(cells))):
                if ci < len(heads) and re.fullmatch(r"M-\d+", heads[ci]):
                    body = cm.group(2).replace(f"（{heads[ci]}）", "")
                    row = row[:cm.start(2)] + body + row[cm.end(2):]
            return row
        return re.sub(r"<tr[^>]*>.*?</tr>", fix_row, tbl, flags=re.S)
    return re.sub(r"<table.*?</table>", fix_table, seg, flags=re.S)


ARCH_DIMS_RE = re.compile(r"((?:技構成|技|持ち物|性格|EV)(?:[・、と](?:技構成|技|持ち物|性格|EV))*)の(組み合わせ|違い)")
DIM_KEY = {"技構成": "moves", "技": "moves", "持ち物": "item", "性格": "nature", "EV": "ev"}


def differing_dims(cards):
    """型カードの間で実際に違う要素（技・持ち物・性格・EV）。"""
    out = set()
    for d, k in DIM_KEY.items():
        vals = {json.dumps(sorted(c[k]) if k == "moves" else c[k], ensure_ascii=False) for c in cards}
        if len(vals) > 1:
            out.add(d)
    return out


def fix_arch_dims(seg, cards):
    """「技・持ち物・性格・EVの組み合わせから」の定型文を、型カードで実際に違う要素だけに絞る（2026-10-28：
    性格・EVが全型で同じ記事でも手本の定型を写し、27記事で事実と食い違った）。"""
    diff = differing_dims(cards)
    if len(cards) < 2 or not diff:
        return seg

    def rep(m):
        dims = re.split(r"[・、と]", m.group(1))
        keep = [d for d in dims if d in diff]
        return ("・".join(keep) + "の" + m.group(2)) if keep and len(keep) < len(dims) else m.group(0)
    return "\n".join(l if l.lstrip().startswith("<") else ARCH_DIMS_RE.sub(rep, l) for l in seg.split("\n"))


def normalize(text, cards=None):
    parts = BLOCK_RE.split(text)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 0:
            for a, b in REPLACE:
                p = p.replace(a, b)
            p = _strip_col_season(p)
            if cards:
                p = fix_arch_dims(p, cards)
            # 型カードの選択技を特定の技の後ろに付けると、その技が入れ替え可能に見え、card:N の「必ず持つ」と食い違う
            # （2026-10-28 バサギリ・ミミロップ・グレンアルマ。手本のゲンガー記事から62記事に広がった）。独立した行にする
            p = re.sub(r"^(・[^\n（<]+)（選択技：([^）\n]+)）(?:<br>)?$", r"\1<br>\n選択技：\2", p, flags=re.M)
            # 区切り線が2本続く（2026-10-28 マンムー）
            p = re.sub(r"\n---\n(?:[ \t]*\n)*---\n", "\n---\n", p)
            # 導入の「使用率28位（M-6: 27位）。」の体言止め（2026-10-27 ウォッシュロトム J11。19記事が同じ形）
            p = re.sub(r"(使用率\d+位)((?:（[^（）\n]*）)?)。", r"\1です\2。", p)
        out.append(p)
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = open(a.path, encoding="utf-8").read()
    # 事実ファイル（_local/article_facts/<slug>.json）があれば型カードを使う正規化も行う
    import os
    slug = os.path.basename(a.path)[:-3]
    fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_local", "article_facts", f"{slug}.json")
    cards = json.load(open(fp, encoding="utf-8")).get("cards") if os.path.exists(fp) else None
    new = normalize(text, cards)
    if new == text:
        return 0
    if a.check:
        print(f"[article_normalize] 表記ゆれあり: python3 scripts/article_normalize.py {a.path}")
        return 1
    open(a.path, "w", encoding="utf-8").write(new)
    print(f"[article_normalize] 揃えた: {a.path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
