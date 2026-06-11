"""sim_ui/index.html の POKEMON_ID マップ（名前→webp画像id）を DB から再生成する。

pokemon_base_stats の全種について webp(pokemon-{dex4}-{form2}.webp) が存在するものを登録。
表記ゆれ（スペースあり括弧）も正規化キーで両対応。手書きの欠落（デカヌチャン等）を解消する。
"""
import os
import re
import sqlite3

ROOT = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(ROOT, "pokenavi.db")
HTML = os.path.join(ROOT, "sim_ui", "index.html")
IMGDIR = os.path.join(ROOT, "..", "public", "images", "pokemon")

# リージョン/特殊フォルムのエイリアス（DBのform_indexがwebp番号と不一致・接頭辞表記のため、
# UI表示名（括弧形・正規化後）→ 実在webp id を明示マップ）。webp存在分のみ採用。
ALIASES = {
    "フラエッテ:永遠": "0670-05", "フラエッテ(永遠)": "0670-05",
    "キュウコン(アローラ)": "0038-01", "ライチュウ(アローラ)": "0026-01",
    "ヤドキング(ガラル)": "0199-01", "ヤドラン(ガラル)": "0080-02",
    "マッギョ(ガラル)": "0618-01",
    "ダイケンキ(ヒスイ)": "0503-01", "ゾロアーク(ヒスイ)": "0571-01",
    "ウインディ(ヒスイ)": "0059-01", "バクフーン(ヒスイ)": "0157-01",
    "クレベース(ヒスイ)": "0713-01", "ジュナイパー(ヒスイ)": "0724-01",
    "ヌメルゴン(ヒスイ)": "0706-01",
    "ルガルガン(たそがれ)": "0745-02", "ルガルガン(まよなか)": "0745-01",
    "ウォッシュロトム": "0479-02", "ビビヨン": "0666-18",
    "イダイトウ(オス)": "0902-00", "イダイトウ(メス)": "0902-01",
}


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute(
        "SELECT pokemon_name, dex_number, form_index FROM pokemon_base_stats "
        "ORDER BY dex_number, form_index").fetchall()
    entries = {}
    for r in rows:
        iid = f"{r['dex_number']:04d}-{r['form_index']:02d}"
        if not os.path.exists(os.path.join(IMGDIR, f"pokemon-{iid}.webp")):
            continue
        nm = r["pokemon_name"]
        entries.setdefault(nm, iid)
        norm = nm.replace(" (", "(")
        if norm != nm:
            entries.setdefault(norm, iid)
    for k, v in ALIASES.items():
        if os.path.exists(os.path.join(IMGDIR, f"pokemon-{v}.webp")):
            entries[k] = v   # webp実在分のみ、エイリアスを優先採用

    items = [f"'{k}':'{v}'" for k, v in entries.items()]
    lines = ["const POKEMON_ID = {"]
    for i in range(0, len(items), 6):
        lines.append("  " + ",".join(items[i:i + 6]) + ",")
    lines.append("};")
    block = "\n".join(lines)

    html = open(HTML, encoding="utf-8").read()
    new = re.sub(r"const POKEMON_ID = \{.*?\n\};", block, html, count=1, flags=re.DOTALL)
    if new == html:
        print("置換失敗（POKEMON_IDブロックが見つからない）")
        return 1
    open(HTML, "w", encoding="utf-8").write(new)
    print(f"POKEMON_ID 再生成: {len(entries)} エントリ")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
