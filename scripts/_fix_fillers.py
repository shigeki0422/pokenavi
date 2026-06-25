"""フィラーの文脈不一致な溜め技を修正。天候源が無いパの ソーラービーム/エレクトロビーム や
常時2ターン技を、その種の使用率次点技(溜め技でない・重複でない)に差し替える。全パ一括。
軸(slot0)は技オプティマイザ管轄なので対象外。"""
import json, _pop_gen as G

SEASON = "M-3"
WSET = {"あめふらし": "rain", "あまごい": "rain", "ひでり": "sun", "にほんばれ": "sun", "すなおこし": "sand", "ゆきふらし": "snow"}
SUN = {"ソーラービーム", "ソーラーブレード"}; RAIN = {"エレクトロビーム"}
ALWAYS = {"あなをほる", "そらをとぶ", "ダイビング", "ゴッドバード", "とびはねる", "メテオビーム", "ゴーストダイブ"}
CHARGE_ALL = SUN | RAIN | ALWAYS

def team_weather(specs):
    w = set()
    for s in specs:
        for a in [s.split(":")[-1]] + (s.split(":")[2].split("|") if ":" in s else []):
            if a in WSET: w.add(WSET[a])
    return w

def bad_move(mv, w):
    return (mv in SUN and "sun" not in w) or (mv in RAIN and "rain" not in w) or (mv in ALWAYS)

def main():
    D = G.load(season=SEASON)
    fixed = 0
    for fn in ["func1_pool_M-3.json", "func1_themed_M-3.json"]:
        d = json.load(open(fn, encoding="utf-8"))
        for p in d["parties"]:
            w = team_weather(p["specs"])
            for si, s in enumerate(p["specs"]):
                if si == 0 and p.get("source") != "strong" and p.get("theme", "").startswith("メガ軸"):
                    continue  # 軸はオプティマイザ管轄
                if ":" not in s: continue
                parts = s.split(":")
                nm = parts[0].split("@")[0]
                moves = parts[2].split("|") if len(parts) > 2 and parts[2] else []
                cur = set(moves)
                changed = False
                usage = sorted(D["moves"].get(nm, {}), key=D["moves"][nm].get, reverse=True)
                for i, mv in enumerate(moves):
                    if bad_move(mv, w):
                        repl = next((u for u in usage if u not in cur and not bad_move(u, w)), None)
                        if repl:
                            cur.discard(mv); cur.add(repl); moves[i] = repl; changed = True; fixed += 1
                if changed:
                    parts[2] = "|".join(moves)
                    p["specs"][si] = ":".join(parts)
        json.dump(d, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"フィラーの溜め技を差し替え: {fixed}箇所")
    # 検証: 残存する文脈不一致
    d = json.load(open("func1_pool_M-3.json", encoding="utf-8"))
    rem = 0
    for p in d["parties"]:
        w = team_weather(p["specs"])
        for s in p["specs"]:
            for mv in (s.split(":")[2].split("|") if ":" in s else []):
                if bad_move(mv, w): rem += 1
    print(f"残存(軸のソーラー等含む): {rem}")

if __name__ == "__main__":
    main()
