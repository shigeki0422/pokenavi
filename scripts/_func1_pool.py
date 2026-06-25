"""機能1 母集団の統合: 戦略テーマ構築(func1_themed) ∪ 共進化の強生き残り(coevo_parties)。
テーマ偏重による実環境乖離を防ぐため、純粋に強い生存構築を大量に混ぜる。
種族集合で重複除去(テーマ側を優先保持)。source/theme/elo/screen_wr ラベル付きで永続化。
出力: scripts/func1_pool_{SEASON}.json
"""
import sys, os, json
SEASON = os.environ.get("COEVO_SEASON", "M-3")
COEVO = f"/tmp/coevo_parties_{SEASON}.json"
THEMED = f"func1_themed_{SEASON}.json"

def sig(specs):
    return frozenset(s.split("@")[0].split(":")[0] for s in specs)

def main():
    strong_n = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    pool = []; seen = set()
    th = json.load(open(THEMED, encoding="utf-8"))["parties"]
    for p in th:
        k = sig(p["specs"])
        if k in seen: continue
        seen.add(k)
        pool.append({"source": "theme", "theme": p["theme"], "screen_wr": p.get("screen_wr"), "specs": p["specs"]})
    nth = len(pool)
    cv = json.load(open(COEVO, encoding="utf-8"))["parties"]
    added = 0
    for p in cv:
        if added >= strong_n: break
        k = sig(p["specs"])
        if k in seen: continue
        seen.add(k)
        pool.append({"source": "strong", "elo": round(p.get("elo", 0)), "specs": p["specs"],
                     "names": p.get("names")})
        added += 1
    out = f"func1_pool_{SEASON}.json"
    json.dump({"season": SEASON, "n_theme": nth, "n_strong": added, "total": len(pool), "parties": pool},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    tcat = Counter(p["theme"].split(":")[0] for p in pool if p["source"] == "theme")
    print(f"母集団統合: テーマ{nth} + 強生き残り{added} = 計{len(pool)} → {out}")
    print("テーマ別:", dict(tcat))

if __name__ == "__main__":
    main()
