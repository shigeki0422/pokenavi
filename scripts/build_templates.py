"""登録テンプレートの正本（DB表 templates）を構築する。

データ源は GameWith「上位構築」（M-1）。情報が完全な構築のみを採用する。
JSバンドル(crawl_m1_rankings)はランキング側でパーティ非公開が多く完全データが少ないため、
記事クロール由来でキュレーション済みの完全73構築（party_templates_new.txt）をシードに用いる。
全件、種族・技がバトルDBで解決でき『不明』を含まないことを検証してから格納する。

格納後は本表 `templates` を唯一の正本とし、旧 m1_party / gamewith_parties.json /
party_templates_new.txt は冗長として扱う（UIの上位100や belief 事前分布も本表から生成）。
"""
import os
import sqlite3
import sys

from simulator.simulate import get_loader
from simulator.env import _load_templates_txt, is_complete_party

DB_PATH = os.path.join(os.path.dirname(__file__), "pokenavi.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS templates (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    party_id  INTEGER NOT NULL,   -- M-1 順位
    label     TEXT,
    slot      INTEGER NOT NULL,   -- 0..5
    pokemon   TEXT NOT NULL,
    item      TEXT,
    nature    TEXT,
    ability   TEXT,
    move1 TEXT, move2 TEXT, move3 TEXT, move4 TEXT,
    ev_h INTEGER, ev_a INTEGER, ev_b INTEGER, ev_c INTEGER, ev_d INTEGER, ev_s INTEGER,
    UNIQUE(party_id, slot)
);
"""


def main():
    loader = get_loader()
    parties = _load_templates_txt()
    complete = [p for p in parties if is_complete_party(p, loader)]
    print(f"完全な構築: {len(complete)} / {len(parties)}")
    incomplete = [p.party_id for p in parties if p not in complete]
    if incomplete:
        print(f"  除外(不完全): {incomplete}")

    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    con.execute("DELETE FROM templates")
    for party in complete:
        for slot, spec in enumerate(party.specs):
            mv = (spec["moves"] + ["", "", "", ""])[:4]
            e = spec["evs"]
            con.execute(
                "INSERT INTO templates (party_id, label, slot, pokemon, item, nature, ability,"
                " move1, move2, move3, move4, ev_h, ev_a, ev_b, ev_c, ev_d, ev_s)"
                " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (party.party_id, party.label, slot, spec["name"], spec["item"],
                 spec["nature"], spec["ability"], mv[0], mv[1], mv[2], mv[3],
                 e["H"], e["A"], e["B"], e["C"], e["D"], e["S"]))
    con.commit()
    n = con.execute("SELECT COUNT(DISTINCT party_id) FROM templates").fetchone()[0]
    print(f"templates 表に {n} パーティを格納（正本）。")
    con.close()


if __name__ == "__main__":
    sys.exit(main())
