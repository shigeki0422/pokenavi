"""持ち物名 → item-sprite.png の座標 を、ポケモン個別ページから抽出して JSON 化する。

ポケモン情報ページ（src/content/pokemon/*.md）は既にスプライト座標を埋め込んでいる。
外部サイトを引かずに、リポジトリ内の既存データから対応表を作る。

出力: public/sim-data/item_sprite.json  {持ち物名: [x, y]}（背景サイズは 480x648 固定）
"""
import collections
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src", "content", "pokemon", "*.md")
OUT = os.path.join(ROOT, "public", "sim-data", "item_sprite.json")
PAT = re.compile(
    r"background-size:480px 648px;background-position:(-?\d+)px (-?\d+)px[^>]*></span>([^<]+)</div>")


def main():
    votes = collections.defaultdict(collections.Counter)
    for p in glob.glob(SRC):
        with open(p, encoding="utf-8") as f:
            for x, y, name in PAT.findall(f.read()):
                votes[name.strip()][(int(x), int(y))] += 1
    conflicts = {k: dict(v) for k, v in votes.items() if len(v) > 1}
    out = {k: list(v.most_common(1)[0][0]) for k, v in sorted(votes.items())}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(out)}種 → {OUT}")
    if conflicts:
        print(f"⚠ 座標が割れた持ち物 {len(conflicts)}件:", list(conflicts)[:5])


if __name__ == "__main__":
    main()
