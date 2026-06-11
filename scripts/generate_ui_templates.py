"""UI（コンボボックス）用テンプレート一覧を正本DB表 templates から生成する。

正本は DB 表 templates の1か所のみ。このスクリプトはそこから UI が読む派生ファイル
（party_templates_new.txt 形式）を生成する build ステップ。上位 top 件のみ出力する。
"""
import os
import sqlite3
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "pokenavi.db")
OUT_PATH = os.path.join(os.path.dirname(__file__), "party_templates_new.txt")


def member_str(r) -> str:
    moves = [r[c] for c in ("move1", "move2", "move3", "move4") if r[c]]
    moves = (moves + ["なし", "なし", "なし", "なし"])[:4]
    ev = "/".join(str(r[c]) for c in ("ev_h", "ev_a", "ev_b", "ev_c", "ev_d", "ev_s"))
    return f'{r["pokemon"]}@{r["item"]}:{r["nature"]}:{"|".join(moves)}:{ev}:{r["ability"]}'


def main(top: int = 100):
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    pids = [r[0] for r in con.execute(
        "SELECT DISTINCT party_id FROM templates ORDER BY party_id LIMIT ?", (top,)).fetchall()]
    lines = ["// GENERATED from DB table `templates` by generate_ui_templates.py — do not edit by hand"]
    for pid in pids:
        rows = con.execute(
            "SELECT * FROM templates WHERE party_id=? ORDER BY slot", (pid,)).fetchall()
        label = rows[0]["label"] or f"#{pid}"
        username = label.split(" ", 1)[1] if " " in label else label
        members = ", ".join(f'"{member_str(r)}"' for r in rows)
        lines.append(f'  {{ id: "m1-{pid}-{username}", name: "{label}", tag: "M-1 #{pid}", party: [{members}] }},')
    con.close()
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"UIテンプレート {len(pids)} 件を {OUT_PATH} に生成。")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 100)
