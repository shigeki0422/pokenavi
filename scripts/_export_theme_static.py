"""テーマ総当たり(theme_f1_cache)を、上位環境シミュレーションと同形式の静的JSONへ書き出す。
export_f1_static のヘルパ（compute_faults / compute_vs_pokemon / _replay / explain_matchup / export_icons）を
そのまま再利用し、SEASON=M-3・出力先をテーマ用に差し替える。フロントは simulator と同じ契約で読む。

出力: public/sim-data-theme/ に index/rankers/saved/icons/move_types ＋ subjects/<safe>.json（同梱配信）。
"""
import glob, json, os, sqlite3
import export_f1_static as E

E.SEASON = "M-3"
SEASON = "M-3"
CACHE_DIR = os.path.join(os.path.dirname(__file__), "theme_f1_cache")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "sim-data-theme")
SUBJ_DIR = os.path.join(OUT_DIR, "subjects")
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")

def main():
    os.makedirs(SUBJ_DIR, exist_ok=True)
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    files = sorted(glob.glob(os.path.join(CACHE_DIR, "*.json")))
    rankers = {}; saved = {}; index_subjects = []; ai_ver = None
    print(f"対象: {len(files)} 主役ファイル")
    for i, fp in enumerate(files, 1):
        d = json.load(open(fp, encoding="utf-8"))
        subj = d["subject_label"]; party = d["subject_party"]; cards = d["cards"]
        ai_ver = d.get("ai_ver")
        rankers[subj] = party
        summary = [{"label": c["label"], "specs": c["specs"], "win_rate": c["win_rate"],
                    "wins": c["wins"], "losses": c["losses"], "draws": c["draws"], "n": c["n"]} for c in cards]
        saved[subj] = {"cards": summary}
        wr = (sum(c["win_rate"] for c in cards) / len(cards)) if cards else None
        index_subjects.append({"label": subj, "file": E._safe(subj) + ".json",
                               "win_rate": wr, "n": cards[0]["n"] if cards else 0})
        opp = {}
        for c in cards:
            opp[c["label"]] = {
                "faults": E.compute_faults(c),
                "matchup": E.explain_matchup(party, c["specs"], E._loader, SEASON),
                "replays": [E._replay(r) for r in c.get("records", [])],
            }
        vp = E.compute_vs_pokemon(cards)
        for p in vp["pokemon"]:
            if p["builds"]:
                p["matchup"] = E.explain_matchup(party, [p["builds"][0]["spec"]], E._loader, SEASON)
        out = {"subject": {"label": subj, "party": party}, "cards": summary, "opp": opp, "vs_pokemon": vp}
        json.dump(out, open(os.path.join(SUBJ_DIR, E._safe(subj) + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"))
        if i % 10 == 0 or i == len(files): print(f"  [{i}/{len(files)}] {subj}")

    def w(name, obj):
        json.dump(obj, open(os.path.join(OUT_DIR, name), "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"))
    w("rankers.json", [{"label": k, "party": v} for k, v in sorted(rankers.items())])
    w("saved.json", saved)
    w("icons.json", E.export_icons(con))
    w("move_types.json", {r["name_jp"]: r["type"]
                          for r in con.execute("SELECT name_jp, type FROM move_master").fetchall()})
    w("index.json", {"ai_ver": ai_ver, "subjects": index_subjects})
    sz = sum(os.path.getsize(os.path.join(SUBJ_DIR, f)) for f in os.listdir(SUBJ_DIR))
    print(f"完了 → {OUT_DIR} / subjects {len(files)}本 計{sz/1e6:.1f}MB")

if __name__ == "__main__":
    main()
