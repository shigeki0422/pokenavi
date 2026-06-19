"""機能2(パーティ提案)本筋パイプライン。
共進化プール(多様候補)＋生成器候補を、MCTS@400で実使用率メタと対戦させ勝率でランク(=真値)。
有意にメタを上回る(>閾値)構築だけ採用し、種族重複の多いチームを間引いて多様な強構築を永続化。
NetGreedy進化の弱評価ランクでなく、最終はMCTS実勝率で選ぶ(build_signalの知見)。
出力: scripts/func2_teams_{SEASON}.json（機能2が参照する永続データ）。
"""
import sys, os, random, math, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G

SEASON = os.environ.get("COEVO_SEASON", "M-3")
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
POOL_FILE = f"/tmp/coevo_parties_{SEASON}.json"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    seed, cand, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = d = 0
    for opp in gauntlet:
        for k in range(K):
            A = team(cand); B = team(opp)
            sa = select_party(A, B, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
            ton1 = (k % 2 == 0)
            s1 = BattleSide(sa if ton1 else sb); s2 = BattleSide(sb if ton1 else sa)
            s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            try: r = Battle(s1, s2).run(ai, ai)
            except Exception: r = 0
            if r == 0: d += 1
            elif (r == 1) == ton1: w += 1
            else: l += 1
    return cand, w, l, d

def _species(specs):
    return [s.split("@")[0].split(":")[0] for s in specs]

def main():
    ncoevo = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    ngen = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    gn = int(sys.argv[3]) if len(sys.argv) > 3 else 14
    K = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    thr = float(os.environ.get("WIN_THR", "0.55"))
    import time
    D = G.load(season=SEASON); rng = random.Random(7)
    cands = []
    if os.path.exists(POOL_FILE):
        cands += [p["specs"] for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"][:ncoevo]]
    cands += [G.gen_party(D, rng) for _ in range(ngen)]
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    print(f"候補 {len(cands)}(共進化{ncoevo}+生成{ngen}) / メタgauntlet {gn} / 各{gn*K}戦 / MCTS@{SIMS} / 採用閾値{thr*100:.0f}%", flush=True)
    jobs = [(800 + i, cands[i], gauntlet, K) for i in range(len(cands))]
    t0 = time.time()
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    rows = []
    for cand, w, l, d in res:
        dec = w + l; wr = w / dec if dec else 0
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        rows.append({"wr": wr, "z": z, "w": w, "l": l, "d": d, "specs": cand, "species": _species(cand)})
    rows.sort(key=lambda r: -r["wr"])
    # 採用＝閾値超 & 種族5体以上一致の重複を間引く（多様性）
    kept = []
    for r in rows:
        if r["wr"] < thr: continue
        sset = set(r["species"])
        if any(len(sset & set(k["species"])) >= 5 for k in kept): continue
        kept.append(r)
    print(f"\n=== 機能2 提案候補（メタ実勝率>{thr*100:.0f}%・多様化後）{time.time()-t0:.0f}秒 ===", flush=True)
    for i, r in enumerate(kept[:12]):
        print(f"{i+1}. {r['wr']*100:.1f}% (z={r['z']:+.2f}) {' / '.join(r['species'])}", flush=True)
    out = f"func2_teams_{SEASON}.json"
    json.dump({"season": SEASON, "threshold": thr, "mcts_sims": SIMS,
               "teams": [{"winrate": r["wr"], "z": r["z"], "specs": r["specs"], "species": r["species"]} for r in kept]},
              open(out, "w"), ensure_ascii=False, indent=1)
    print(f"\n採用{len(kept)}件を {out} に永続化（全{len(rows)}候補中・閾値{thr*100:.0f}%超）", flush=True)

if __name__ == "__main__":
    main()
