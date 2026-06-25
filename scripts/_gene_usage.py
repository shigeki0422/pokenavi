"""トーナメント記録(theme_f1_cache)から各構築の「遺伝子使用率」を測定し、死に遺伝子を検出。
- メンバー選出率：6体が選出(3体)に入った割合
- 技使用：各メンバーの4技が実戦で1度でも使われたか（使われない＝死に技。例 こだわり+わるだくみ）
- メガ実行率：その構築でメガ進化が実際に起きた割合（軸が遊んでいないか）
進化機構(_usage_evolve)の照準データ。単体実行で母集団の死に遺伝子サマリを表示。
"""
import json, os, glob, re, sqlite3
import _pop_gen as G

CACHE = os.path.join(os.path.dirname(__file__), "theme_f1_cache")
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")

def parse_spec(s):
    nm = s.split("@")[0].split(":")[0]
    it = s.split("@")[1].split(":")[0] if "@" in s else ""
    f = s.split(":")
    mv = f[2].split("|") if len(f) > 2 and f[2] else []
    return nm, it, mv

def gene_usage(d, megastones):
    """1主役キャッシュ→{member: {sel, sel_rate, moves:{mv:used}, dead_moves}], mega_rate, battles}"""
    party = d["subject_party"]
    members = [parse_spec(s) for s in party]
    battles = 0; sel = {nm: 0 for nm, _, _ in members}
    moveuse = {nm: {mv: 0 for mv in mvs} for nm, _, mvs in members}
    active_cnt = {nm: 0 for nm, _, _ in members}
    mega_used = 0
    for c in d["cards"]:
        for rec in c.get("records", []):
            battles += 1
            s1 = set(rec.get("selected1", []))
            for nm in s1:
                if nm in sel: sel[nm] += 1
            # メガ実行：最終ターンの side1 に mega フラグ
            turns = rec.get("turns", [])
            if turns:
                last = turns[-1].get("side1", {})
                if any(p.get("mega") for p in last.get("party", [])): mega_used += 1
            # 技使用：ログ走査（"{member} の {move}" を含む行）
            for t in turns:
                for l in t.get("logs", []):
                    for nm, _, mvs in members:
                        if nm in s1 and (nm + " の ") in l:
                            for mv in mvs:
                                if mv and (nm + " の " + mv) in l:
                                    moveuse[nm][mv] += 1
    out = {}
    for nm, it, mvs in members:
        srate = sel[nm] / battles if battles else 0
        used = {mv: moveuse[nm][mv] for mv in mvs}
        dead = [mv for mv in mvs if mv and moveuse[nm][mv] == 0]
        out[nm] = {"item": it, "sel": sel[nm], "sel_rate": round(srate, 3),
                   "moves": used, "dead_moves": dead, "is_mega_stone": it in megastones}
    return {"members": out, "battles": battles, "mega_rate": round(mega_used / battles, 3) if battles else 0}

def main():
    D = G.load(season="M-3"); ms = D["megastones"]
    files = sorted(glob.glob(os.path.join(CACHE, "*.json")))
    dead_members = []; dead_moves = []; low_mega = []
    allstats = {}
    for fp in files:
        d = json.load(open(fp, encoding="utf-8"))
        st = gene_usage(d, ms); lab = d["subject_label"]; allstats[lab] = st
        for nm, m in st["members"].items():
            if m["sel_rate"] < 0.30:
                dead_members.append((lab, nm, m["item"], m["sel_rate"], m["is_mega_stone"]))
            for dm in m["dead_moves"]:
                if m["sel"] >= max(5, st["battles"] * 0.2):   # 十分選出された上で未使用の技のみ
                    dead_moves.append((lab, nm, m["item"], dm))
        # メガ石を持つ構築なのにメガ実行率が低い＝軸が遊んでいる
        if any(m["is_mega_stone"] for m in st["members"].values()) and st["mega_rate"] < 0.5:
            low_mega.append((lab, st["mega_rate"]))
    json.dump(allstats, open(os.path.join(os.path.dirname(__file__), "gene_usage_M-3.json"), "w", encoding="utf-8"),
              ensure_ascii=False, separators=(",", ":"))
    print(f"=== 死に遺伝子サマリ（{len(files)}構築）===\n")
    print(f"■ 低選出メンバー(選出率<30%): {len(dead_members)}件")
    for lab, nm, it, sr, ism in sorted(dead_members, key=lambda x: x[3])[:15]:
        print(f"   {sr*100:4.0f}% {lab} / {nm}@{it}{' [メガ軸]' if ism else ''}")
    print(f"\n■ 死に技(十分選出されたが使用0): {len(dead_moves)}件")
    for lab, nm, it, dm in dead_moves[:15]:
        print(f"   {lab} / {nm}@{it}: {dm}")
    print(f"\n■ メガ実行率<50%(軸が遊ぶ構築): {len(low_mega)}件")
    for lab, mr in sorted(low_mega, key=lambda x: x[1])[:15]:
        print(f"   メガ実行{mr*100:4.0f}% {lab}")

if __name__ == "__main__":
    main()
