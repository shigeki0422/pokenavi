"""gamewith M-2上位構築(m2_top_builds.json)を 正本DB表 templates に登録。
party_id = 1000 + 順位（M-1=1..100 と衝突回避）, label = "M-2#順位 ユーザ名"。
完全開示(6体とも4技、ただしメタモン=へんしんのみは可)のみ登録。
dry-run既定。 `commit` 引数でDB反映（既存M-2分=party_id 1000..1999 を入替）。
"""
import os, sys, json, sqlite3
os.environ.setdefault("OMP_NUM_THREADS", "1")
from simulator.simulate import get_loader
from simulator.pokemon import build_from_spec, parse_pokemon_spec

SEASON = "M-2"; SRC = "m2_top_builds.json"; DB = "pokenavi.db"; PID_BASE = 1000

def mon_ok(name, moves):
    real = [m for m in moves if m and m not in ("なし", "不明")]
    return len(real) == 4 or (name == "メタモン" and real == ["へんしん"])

def to_spec(mon):
    n, it, na, mo, ev, ab = mon
    real = [m for m in mo if m and m not in ("なし", "不明")]
    return f"{n}@{it}:{na}:{'|'.join(real)}:{ev.replace(',', '/')}:{ab}"

def main():
    commit = len(sys.argv) > 1 and sys.argv[1] == "commit"
    L = get_loader()
    builds = json.load(open(SRC, encoding="utf-8"))
    rows = []          # (party_id, label, slot, pokemon, item, nature, ability, m1..m4, evs[6])
    skipped = []
    for b in builds:
        if not all(mon_ok(m[0], m[3]) for m in b["mons"]):
            skipped.append((b["r"], b["un"], [m[0] for m in b["mons"] if not mon_ok(m[0], m[3])]))
            continue
        # 6体すべてビルド検証
        try:
            for m in b["mons"]:
                build_from_spec(parse_pokemon_spec(to_spec(m)), L, season=SEASON, randomize=False)
        except Exception as e:
            skipped.append((b["r"], b["un"], [f"build失敗:{e}"]))
            continue
        pid = PID_BASE + int(b["r"]); label = f"M-2#{b['r']} {b['un']}"
        for slot, m in enumerate(b["mons"]):
            n, it, na, mo, ev, ab = m
            real = [x for x in mo if x and x not in ("なし", "不明")]
            mv = (real + [None, None, None, None])[:4]
            evk = [int(x) for x in ev.split(",")]
            rows.append((pid, label, slot, n, it, na, ab, mv[0], mv[1], mv[2], mv[3], *evk))
    parties = len({r[0] for r in rows})
    print(f"登録対象: {parties}構築 / {len(rows)}行   除外: {len(skipped)}件")
    for r, un, why in skipped:
        print(f"  skip M-2#{r} {un}: {why}")
    if not commit:
        print("\n[dry-run] commit する場合: venv/bin/python _m2_register.py commit")
        print("sample:", rows[0][:7], "...EV", rows[0][11:])
        return
    con = sqlite3.connect(DB)
    con.execute("DELETE FROM templates WHERE party_id BETWEEN ? AND ?", (PID_BASE, PID_BASE + 999))
    con.executemany(
        "INSERT INTO templates(party_id,label,slot,pokemon,item,nature,ability,"
        "move1,move2,move3,move4,ev_h,ev_a,ev_b,ev_c,ev_d,ev_s) "
        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.commit()
    n = con.execute("SELECT COUNT(DISTINCT party_id) FROM templates WHERE label LIKE 'M-2%'").fetchone()[0]
    con.close()
    print(f"\nDB反映完了: templates に M-2 {n}構築を登録")

if __name__ == "__main__":
    main()
