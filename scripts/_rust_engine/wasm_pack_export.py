"""ブラウザ用の小さいデータパックを書き出す。

`datapack_export.py` が作る datapack.json は MCTS 用の重み(net 5.9MB)と使用率統計(usage
0.7MB)を含むが、1v1 判定はどちらも読まない。spec が型を全て明示するため使用率が不要で、
評価関数も使わないため。ここでは 1v1 に必要なテーブルだけを残す。

出力: public/builder-data/engine.pack.json
"""
import json
import os
import sys

# Pack::from_value が読むキーのうち、1v1 の実走に要るものだけ。
# net(MCTSの評価関数) / usage(選出・提案) / registered_spreads(相手型の推定) は除く。
KEEP = [
    "header", "types", "type_chart", "nature_mods", "form_aliases", "region_prefixes",
    "move_master", "secondary_moves", "pokemon_base_stats", "pokemon_mega_stats",
    "usage_names_in_moves", "ability_cats",
]

SRC = os.path.join(os.path.dirname(__file__), "datapack.json")
DST = os.path.join(os.path.dirname(__file__), "..", "..", "public", "builder-data", "engine.pack.json")


def main():
    if not os.path.exists(SRC):
        sys.exit(f"{SRC} が無い。先に _rust_engine/datapack_export.py を実行する")
    d = json.load(open(SRC))
    missing = [k for k in KEEP if k not in d]
    if missing:
        sys.exit(f"datapack に必要なキーが無い: {missing}")
    sub = {k: d[k] for k in KEEP}
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w") as f:
        json.dump(sub, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{os.path.relpath(DST)}: {os.path.getsize(DST)/1e3:.0f}KB "
          f"(元 {os.path.getsize(SRC)/1e6:.1f}MB)")


if __name__ == "__main__":
    main()
