"""メガ石の確定再配置パス。各構築で選出率を実測し、メガ可能種(石が使用率に存在・メガ率≥50%)の
うち選出率上位に石を載せ替える。石数(≤2)は維持。低選出の個体に石が載って遊ぶ損失を解消する不変条件
（石は選出される個体に載せる）。山登りのノイズに依存しないため確定適用。
"""
import os, json, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G
import _coevo as C
import _usage_evolve as E

POOL = "func1_themed_M-3.json"
GAMES = int(os.environ.get("GAMES", "40"))

def main():
    D = G.load(season="M-3"); C.D = D; ms = D["megastones"]
    obj = json.load(open(POOL, encoding="utf-8"))
    parties = [p["specs"] for p in obj["parties"]]; n = len(parties)
    rng = random.Random(11)
    args = [(parties[i], [parties[k] for k in rng.sample([x for x in range(n) if x != i], GAMES)], 50 + i, True)
            for i in range(n)]
    with mp.get_context("fork").Pool(12, initializer=E._winit) as pool:
        stats = pool.map(E._eval, args)
    moved = 0
    for i, p in enumerate(obj["parties"]):
        specs = parties[i]; mons = [C.parse_my(s) for s in specs]
        names = [m["name"] for m in mons]
        b = max(1, stats[i]["n"]); srate = {nm: stats[i]["sel"].get(nm, 0) / b for nm in names}
        weather = set()
        for m in mons:
            for a in [m["ability"]] + (m["moves"] or []):
                if a in G._WSET: weather.add(G._WSET[a])
        holders = [k for k in range(6) if mons[k]["item"] in ms]
        capable = [k for k in range(6) if E.species_stone(D, names[k]) and E.mega_usage_rate(D, names[k]) >= 0.5]
        if not capable or not holders: continue
        nstone = len(holders)
        desired = sorted(capable, key=lambda k: srate.get(names[k], 0), reverse=True)[:nstone]
        if set(desired) == set(holders): continue
        used = {mons[k]["item"] for k in range(6) if mons[k]["item"] and mons[k]["item"] not in ms}
        for k in holders:                         # desiredでない石持ち→非メガへ降格
            if k not in desired:
                mons[k]["item"] = G.fallback_item(D, names[k], used); used.add(mons[k]["item"])
                E._coherent_mon(D, mons[k], weather, rng)
        for k in desired:                          # 石無し→石付与
            if mons[k]["item"] not in ms:
                mons[k]["item"] = E.species_stone(D, names[k]); E._coherent_mon(D, mons[k], weather, rng)
        p["specs"] = [C.to_spec(x) for x in C.repair(mons, rng)]
        moved += 1
        before = [names[k] for k in holders]; after = [names[k] for k in desired]
        if before != after:
            print(f"  {p['theme']}: 石 {before} → {after}")
    json.dump(obj, open(POOL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"メガ石再配置: {moved}構築")

if __name__ == "__main__":
    main()
