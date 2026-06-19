"""メガライチュウX軸の最強構築を探索→MCTS@400で使用率メタ検証。
Xを固定(エレキメイカー)、フィラー5体を多様に変えた候補を生成。各候補をメタgauntletと
MCTS@400で対戦(Xは必ず選出に入れる=軸の実効性を測る)、勝率でランク。
electric-terrain親和(接地電気/速い物理)フィラーも混ぜ、シナジーで50%超えるか確認。"""
import sys, os, random, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
import _calib_probe as CP

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

# 電気F親和フィラー(接地電気/速い物理)。アローラライチュウはXと同種(0026)で同居不可のため除外。
ELEC_FRIENDLY = ["エモンガ", "サンダース", "レアコイル", "ロトム", "デンリュウ", "ボルトロス"]

def _dexmap():
    import sqlite3
    c = sqlite3.connect(os.path.join(os.path.dirname(__file__), "pokenavi.db"))
    m = {}
    for nm, pid in c.execute("SELECT DISTINCT pokemon, pokemon_id FROM pokemon_usage WHERE season=? AND rule='single'", (SEASON,)):
        if pid: m[nm] = pid[:4]
    c.close()
    return m

def gen_xteam(D, rng, dexmap, syn=False):
    x = CP.forced(D, "ライチュウ", "ライチュウナイトX", "せいでんき")
    xdex = dexmap.get("ライチュウ", "0026")
    used_dex = {xdex}; items = set(); team = [x]      # 同dex(リージョン違い含む)は同居不可
    pool = [p for p, _ in D["usage"][:55]]
    if syn:
        ef = [p for p in ELEC_FRIENDLY if p in dexmap]
        rng.shuffle(ef); rest = [p for p, _ in D["usage"][:55] if p not in ef]; rng.shuffle(rest); pool = ef + rest
    else:
        rng.shuffle(pool)
    for nm in pool:
        if len(team) >= 6: break
        dx = dexmap.get(nm)
        if dx is None or dx in used_dex: continue      # 同種(同dex)除外
        it = max(D["items"].get(nm, {"": 1}), key=D["items"].get(nm, {"": 1}).get) if D["items"].get(nm) else None
        if it and "ナイト" in it: continue              # 既にX=メガ枠使用
        if it and it in items: continue
        team.append(CP.usf(D, nm)); used_dex.add(dx)
        if it: items.add(it)
    return team[:6]

def _job(args):
    seed, cand_specs, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = d = 0
    for opp in gauntlet:
        for k in range(K):
            T = team(cand_specs); O = team(opp)
            coreP = [T[0]]; rest = T[1:]
            fs = select_party(rest, O, L, n=2, temperature=0.3, rng=rng)
            sa = (coreP + fs)[:3]                     # Xを必ず選出に入れる
            sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
            ton1 = (k % 2 == 0)
            s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try: r = Battle(s1, s2).run(ai, ai)
            except Exception: r = 0
            if r == 0: d += 1
            elif (r == 1) == ton1: w += 1
            else: l += 1
    return cand_specs, w, l, d

def main():
    ncand = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    import time
    D = G.load(season=SEASON); rng = random.Random(1)
    dexmap = _dexmap()
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    cands = []
    for i in range(ncand):
        cands.append(gen_xteam(D, random.Random(100 + i), dexmap, syn=(i % 3 == 0)))  # 1/3は電気F親和フィラー
    print(f"X軸候補 {len(cands)} / メタgauntlet {gn} / K={K} / MCTS@{SIMS}", flush=True)
    jobs = [(500 + i, cands[i], gauntlet, K) for i in range(len(cands))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    rows = []
    for sp, w, l, dd in res:
        dec = w + l; wr = w / dec if dec else 0
        rows.append((wr, w, l, dd, sp))
    rows.sort(reverse=True)
    print(f"\n=== X軸構築 vs 使用率メタ (MCTS@{SIMS}・{time.time()-t0:.0f}秒) Top8 ===", flush=True)
    for wr, w, l, dd, sp in rows[:8]:
        names = [s.split("@")[0].split(":")[0] for s in sp]
        print(f"{wr*100:4.1f}% ({w}-{l}-{dd})  {' / '.join(names)}", flush=True)
    best = rows[0]
    json.dump({"winrate": best[0], "specs": best[4]}, open("/tmp/xteam_best.json", "w"), ensure_ascii=False)
    print(f"\n最良X構築 勝率 {best[0]*100:.1f}% → /tmp/xteam_best.json", flush=True)

if __name__ == "__main__":
    main()
