"""メガライチュウX + メガ相棒(2メガ選出前提)の最良ペア探索。
エンジンはメガ石2枚保持OK・進化は1戦1体のみ(mega_used)。Xを出せない相手には相棒メガを出す
柔軟性が2メガ選出の強み。各候補相棒について team=[X, 相棒mega, 非メガfiller×4]を組み、
選出はMCTS探索(max_mega=2)で2メガ選出を許容→メタgauntletとMCTS@400で対戦し勝率で相棒をランク。
"""
import sys, os, random, math, json, sqlite3
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G
import _calib_probe as CP
from _xteam_search import _dexmap

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
SEL_SIMS = int(os.environ.get("SEL_SIMS", "100"))
_W = {}

def _mega_species(dexmap):
    c = sqlite3.connect(os.path.join(os.path.dirname(__file__), "pokenavi.db"))
    rows = c.execute("SELECT DISTINCT pokemon, item FROM pokemon_items WHERE season=? AND rule='single' AND item LIKE '%ナイト%'", (SEASON,)).fetchall()
    c.close()
    out = {}
    for nm, it in rows:
        if nm == "ライチュウ":
            continue
        out.setdefault(nm, it)   # 種ごと代表メガ石
    return out

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load()
    _W["play"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["sel"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SEL_SIMS, mcts_select="regret", mcts_fast=True)
    _W["dex"] = _dexmap()

def build_team(partner, pstone, D, dexmap, rng):
    x = CP.forced(D, "ライチュウ", "ライチュウナイトX", "せいでんき")
    pab = max(D["abil"].get(partner, {"": 1}), key=D["abil"].get(partner, {"": 1}).get) if D["abil"].get(partner) else None
    p = CP.forced(D, partner, pstone, pab)
    used_dex = {dexmap.get("ライチュウ", "0026"), dexmap.get(partner, "")}
    items = {pstone}; team = [x, p]
    pool = [q for q, _ in D["usage"][:55]]; rng.shuffle(pool)
    for nm in pool:
        if len(team) >= 6: break
        dx = dexmap.get(nm)
        if dx is None or dx in used_dex: continue
        it = max(D["items"].get(nm, {"": 1}), key=D["items"].get(nm, {"": 1}).get) if D["items"].get(nm) else None
        if it and "ナイト" in it: continue        # filler は非メガ(メガ枠はX/相棒で2つ)
        if it and it in items: continue
        team.append(CP.usf(D, nm)); used_dex.add(dx)
        if it: items.add(it)
    return team[:6]

def _job(args):
    seed, partner, pstone, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from _selnet import select_mcts
    L = _W["L"]; play = _W["play"]; sel_ai = _W["sel"]; D = _W["D"]
    dexmap = _W["dex"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    specs = build_team(partner, pstone, D, dexmap, rng)
    w = l = d = 0; both = 0; xin = 0
    for opp in gauntlet:
        for k in range(K):
            T = team(specs); O = team(opp)
            sa = select_mcts(T, O, L, sel_ai, n=3, rng=rng, topk=6, max_mega=2)   # 2メガ選出許容
            megas = sum(1 for p in sa if getattr(p, "mega_data", None) is not None)
            both += 1 if megas >= 2 else 0
            xin += 1 if any(getattr(p, "name", "") == "ライチュウ" for p in sa) else 0
            sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
            ton1 = (k % 2 == 0)
            s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try: r = Battle(s1, s2).run(play, play)
            except Exception: r = 0
            if r == 0: d += 1
            elif (r == 1) == ton1: w += 1
            else: l += 1
    return partner, specs, w, l, d, both, xin

def main():
    npart = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    gn = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    K = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    import time
    D = G.load(season=SEASON); rng = random.Random(2)
    dexmap = _dexmap(); _W["dex"] = dexmap
    megas = _mega_species(dexmap)
    # 使用率順で相棒候補を絞る
    order = [p for p, _ in D["usage"] if p in megas][:npart]
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"メガ相棒候補 {len(order)} / メタgauntlet {gn} / K={K} / 選出@{SEL_SIMS}(2メガ可) プレイ@{SIMS}", flush=True)
    jobs = [(600 + i, order[i], megas[order[i]], gauntlet, K) for i in range(len(order))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    rows = []
    for partner, specs, w, l, dd, both, xin in res:
        dec = w + l; wr = w / dec if dec else 0; tot = w + l + dd
        rows.append((wr, partner, w, l, dd, both / tot if tot else 0, xin / tot if tot else 0, specs))
    rows.sort(reverse=True)
    print(f"\n=== X+メガ相棒(2メガ選出) vs 使用率メタ (MCTS@{SIMS}・{time.time()-t0:.0f}秒) ===", flush=True)
    print(f"{'相棒':<14}{'勝率':>7}{'2メガ率':>8}{'X選出率':>8}", flush=True)
    for wr, partner, w, l, dd, br, xr, specs in rows:
        print(f"{partner:<14}{wr*100:6.1f}%{br*100:7.0f}%{xr*100:7.0f}%  ({w}-{l}-{dd})", flush=True)
    best = rows[0]
    json.dump({"partner": best[1], "winrate": best[0], "specs": best[7]}, open("/tmp/xmega_best.json", "w"), ensure_ascii=False)
    print(f"\n最良: X+{best[1]} {best[0]*100:.1f}% → /tmp/xmega_best.json", flush=True)

if __name__ == "__main__":
    main()
