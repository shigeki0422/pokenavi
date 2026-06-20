"""母集団の全構築をコヒーレンス監査。違和感(同タイプ純攻撃重複/性格↔技カテゴリ不一致/
溜め技の天候不一致/ピボット2枚/積み2枚/罠技/持ち物重複/一致技なし/同種/3メガ)を検出。
"""
import json, sqlite3, _pop_gen as G
from simulator.data import NATURE_MODS

SEASON = "M-3"
DB = "pokenavi.db"
ROLE = {"ボルトチェンジ", "とんぼがえり", "クイックターン", "ニトロチャージ", "でんこうせっか", "しんそく", "バレットパンチ", "アクアジェット", "ねこだまし"}
TRAP = {"ギガインパクト", "はかいこうせん", "ブラストバーン", "ハイドロカノン", "ハードプラント", "すてみタックル", "とっしん", "メガトンキック", "メガトンパンチ", "ばくれつパンチ", "ロケットずつき", "はなびらのまい", "ぶんまわす"}
PIVOT = {"ボルトチェンジ", "とんぼがえり", "クイックターン"}
SETUP = {"つるぎのまい", "りゅうのまい", "わるだくみ", "ちょうのまい", "めいそう", "てっぺき", "りゅうせいぐん" and "x"}  # placeholder
SETUP = {"つるぎのまい", "りゅうのまい", "わるだくみ", "ちょうのまい", "めいそう", "てっぺき", "からをやぶる", "こうそくいどう", "ロックカット"}
SUN = {"ソーラービーム", "ソーラーブレード"}; RAIN = {"エレクトロビーム"}
ALWAYS = {"あなをほる", "そらをとぶ", "ダイビング", "ゴッドバード", "とびはねる", "メテオビーム", "ゴーストダイブ"}
WSET = {"あめふらし": "rain", "あまごい": "rain", "ひでり": "sun", "にほんばれ": "sun", "すなおこし": "sand", "ゆきふらし": "snow"}

def main():
    D = G.load(season=SEASON)
    c = sqlite3.connect(DB)
    mcat = {r[0]: r[1] for r in c.execute("SELECT name_jp,category FROM move_master")}
    mtype = {r[0]: r[1] for r in c.execute("SELECT name_jp,type FROM move_master")}
    c.close()
    mbs = D.get("mega_by_stone", {}); dexmap = D.get("dex", {})
    pool = json.load(open(f"func1_pool_{SEASON}.json", encoding="utf-8"))["parties"]
    flags = {k: [] for k in ["同タイプ純攻撃重複", "性格↔技カテゴリ不一致", "溜め技の天候不一致", "ピボット2枚", "積み2枚", "罠技", "持ち物重複", "一致技なし", "同種同居", "3メガ以上"]}

    def parse(s):
        st = {"name": s.split("@")[0].split(":")[0]}
        st["item"] = s.split("@")[1].split(":")[0] if "@" in s else None
        f = s.split(":")
        st["nature"] = f[1] if len(f) > 1 else ""
        st["moves"] = f[2].split("|") if len(f) > 2 and f[2] else []
        st["ability"] = f[-1] if len(f) >= 5 else ""
        return st

    for p in pool:
        tag = p.get("theme") if p.get("source") == "theme" else f"強Elo{p.get('elo')}"
        specs = p["specs"]
        weather = set()
        for s in specs:
            for a in [parse(s)["nature"]] + parse(s)["moves"] + [parse(s)["ability"]]:
                if a in WSET: weather.add(WSET[a])
        items = []; megas = 0; dexes = []
        for s in specs:
            st = parse(s); nm = st["name"]; mv = st["moves"]; it = st["item"]
            if it: items.append(it)
            if it in D["megastones"]: megas += 1
            dexes.append(dexmap.get(nm, nm))
            # メガ後タイプ(あれば)で一致判定
            mt = mbs.get(it)
            etypes = set()
            if it in mbs:
                row = sqlite3.connect(DB).execute("SELECT type1,type2 FROM pokemon_mega_stats WHERE mega_stone=?", (it,)).fetchone()
                etypes = set(t for t in (row or ()) if t)
            # 純攻撃(役割技除く)
            pure = [m for m in mv if mcat.get(m) in ("physical", "special") and m not in ROLE]
            tcnt = {}
            for m in pure:
                tcnt[mtype.get(m)] = tcnt.get(mtype.get(m), 0) + 1
            if any(v >= 2 for v in tcnt.values()):
                dup = [t for t, v in tcnt.items() if v >= 2]
                flags["同タイプ純攻撃重複"].append(f"{tag}/{nm}: {dup} ({'|'.join(mv)})")
            # 性格↔カテゴリ
            up, dn = NATURE_MODS.get(st["nature"], (None, None))
            pref = "phys" if (up == "attack" or dn == "sp_attack") else ("spec" if (up == "sp_attack" or dn == "attack") else None)
            atk = [m for m in mv if mcat.get(m) in ("physical", "special")]
            natk = [m for m in atk if m not in ROLE and m != "イカサマ"]   # 自分のAに依存しない技は除外
            nph = sum(1 for m in natk if mcat.get(m) == "physical"); nsp = sum(1 for m in natk if mcat.get(m) == "special")
            if pref == "phys" and nsp > nph and nsp >= 2:
                flags["性格↔技カテゴリ不一致"].append(f"{tag}/{nm}: {st['nature']}(物理↑)だが特殊技{nsp}>物理{nph} ({'|'.join(mv)})")
            if pref == "spec" and nph > nsp and nph >= 2:
                flags["性格↔技カテゴリ不一致"].append(f"{tag}/{nm}: {st['nature']}(特殊↑)だが物理技{nph}>特殊{nsp} ({'|'.join(mv)})")
            # 溜め技天候
            for m in mv:
                if (m in SUN and "sun" not in weather) or (m in RAIN and "rain" not in weather) or (m in ALWAYS):
                    flags["溜め技の天候不一致"].append(f"{tag}/{nm}: {m}")
            if len(set(mv) & PIVOT) >= 2: flags["ピボット2枚"].append(f"{tag}/{nm}: {'|'.join(mv)}")
            if len(set(mv) & SETUP) >= 2: flags["積み2枚"].append(f"{tag}/{nm}: {'|'.join(mv)}")
            for m in mv:
                if m in TRAP: flags["罠技"].append(f"{tag}/{nm}: {m}")
            # 一致技なし(攻撃技はあるのにSTABの攻撃技がゼロ)
            usetypes = etypes if etypes else set(filter(None, [mtype.get(m) for m in []]))
            if etypes and atk and not any(mtype.get(m) in etypes for m in atk):
                flags["一致技なし"].append(f"{tag}/{nm}(メガ{'/'.join(etypes)}): {'|'.join(mv)}")
        if len(items) != len(set(items)): flags["持ち物重複"].append(f"{tag}: {items}")
        if len(dexes) != len(set(dexes)): flags["同種同居"].append(f"{tag}: {[parse(s)['name'] for s in specs]}")
        if megas > 2: flags["3メガ以上"].append(f"{tag}: メガ{megas}")

    print(f"=== コヒーレンス監査（{len(pool)}構築）===\n")
    for k, v in flags.items():
        print(f"■ {k}: {len(v)}件")
        for x in v[:6]: print(f"   {x}")
        if len(v) > 6: print(f"   …他{len(v)-6}件")
        print()

if __name__ == "__main__":
    main()
