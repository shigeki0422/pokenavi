"""母集団の全個体の技構成をコヒーレントに整える（in-place）。
オプティマイザでMCTS学習済みの軸（/tmp/moveset_opts.json のテーマ slot0）のみ保護し、
それ以外の全個体に coherent_set を適用：同タイプ純攻撃の重複排除・罠/文脈外溜め技除去・
一致技補充・性格/EVの主カテゴリ合わせ。役割技/変化技/積み/壁は温存する。"""
import json, os, _pop_gen as G

SEASON = "M-3"
WSET = {"あめふらし": "rain", "あまごい": "rain", "ひでり": "sun", "にほんばれ": "sun",
        "すなおこし": "sand", "ゆきふらし": "snow", "メガソーラー": "sun"}

def team_weather(specs):
    w = set()
    for s in specs:
        parts = s.split(":")
        ab = parts[-1] if len(parts) >= 5 else ""
        mvs = parts[2].split("|") if len(parts) > 2 and parts[2] else []
        for a in [ab] + mvs:
            if a in WSET: w.add(WSET[a])
    return w

def parse_spec(s):
    name = s.split("@")[0].split(":")[0]
    item = s.split("@")[1].split(":")[0] if "@" in s else None
    parts = s.split(":")
    nat = parts[1] if len(parts) > 1 else ""
    mv = parts[2].split("|") if len(parts) > 2 and parts[2] else []
    ev = None
    if len(parts) > 3 and parts[3]:
        try: ev = tuple(int(x) for x in parts[3].split("/"))
        except ValueError: ev = None
    ab = parts[4] if len(parts) > 4 else ""
    return name, item, nat, mv, ev, ab

def main():
    D = G.load(season=SEASON)
    opt = json.load(open("/tmp/moveset_opts.json", encoding="utf-8")) if os.path.exists("/tmp/moveset_opts.json") else {}
    protected = set(opt.keys())
    print(f"保護する学習済み軸: {len(protected)}テーマ {sorted(protected)}")
    total = changed = 0
    for fn in ["func1_pool_M-3.json", "func1_themed_M-3.json"]:
        if not os.path.exists(fn): continue
        d = json.load(open(fn, encoding="utf-8"))
        for p in d["parties"]:
            w = team_weather(p["specs"])
            theme = p.get("theme", "")
            for si, s in enumerate(p["specs"]):
                name, item, nat, mv, ev, ab = parse_spec(s)
                total += 1
                if si == 0 and p.get("source") == "theme" and theme in protected:
                    nnat, nev = G.align_nat_ev(D, mv, nat, ev, fallback=G.species_orient(D, name, item))
                    nmv = mv                                # 学習済み軸の技は温存、性格/EVのみ整合
                else:
                    nmv, nnat, nev = G.coherent_set(D, name, item, mv, nat, ev, weather=w)
                ns = G._spec(name, item, nnat, nmv, nev, ab)
                if ns != s:
                    p["specs"][si] = ns; changed += 1
        json.dump(d, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"対象個体 {total} / 変更 {changed}")

if __name__ == "__main__":
    main()
