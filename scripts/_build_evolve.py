"""ビルド(型)をMCTS実戦結果で淘汰する。各メンバーについて、別アイテム(メガ石含む)＋
それに整合した技構成の代替ビルドを数案生成し、パーティ勝率をMCTS@SIMSで比較して最良を採用。
「非メガ・フルアタ ラグラージ」等は、フルアタがメガで最強→MCTSがメガ型を選ぶ形で結果的に是正される。
独立サンプリングのFrankensteinを結果で篩い落とす実験的パス。
"""
import os, sys, json, random, time, itertools
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G
import _coevo as C

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "250"))
GAUNTLET = int(os.environ.get("GAUNTLET", "10"))   # 1ビルドあたりの評価対戦数
MAXCAND = int(os.environ.get("MAXCAND", "4"))      # 現行＋代替アイテム数
NPROC = int(os.environ.get("NPROC", "12"))
POOL = "func1_themed_M-3.json"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    _W["ai"] = _net_ai(PVNetNP.load(), L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    key, party, opp, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def AI(my, opp_, f): return certain_ko_override(ai0(my, opp_, f), my, opp_, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(party); PB = team(opp)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        w = Battle(s1, s2).run(AI, AI)
    except Exception:
        w = 0
    return key, (1 if w == 1 else 0)

def member_spec(D, nm, item, rng):
    """種nm・指定アイテムで整合したメンバーspecを作る（技/性格/EVは使用率サンプリング→coherent_set）。"""
    nat = G._wchoice(D["natures"].get(nm, {}), rng)
    ab = G._wchoice(D["abil"].get(nm, {}), rng)
    mv = G._wsample_dict(D["moves"].get(nm, {}), 4, rng)
    ep = D["evs"].get(nm, []); ev = None
    if ep:
        i = G._wchoice({i: w for i, (sp, w) in enumerate(ep)}, rng)
        if i is not None: ev = ep[i][0]
    mv, nat, ev = G.coherent_set(D, nm, item, mv, nat, ev)
    return G._spec(nm, item, nat, mv, ev, ab)

def gen_candidates(D, party, j, rng):
    """slot j の代替ビルド候補（現行＋別アイテム）。他メンバーの持ち物/メガ枠は尊重。"""
    mons = [C.parse_my(s) for s in party]
    nm = mons[j]["name"]; cur_item = mons[j]["item"]
    used = {mons[k]["item"] for k in range(6) if k != j and mons[k]["item"]}
    megas_excl = sum(1 for k in range(6) if k != j and mons[k]["item"] in D["megastones"])
    cands = [party[j]]                                  # 現行ビルドを基準に含める
    items = sorted(D["items"].get(nm, {}).items(), key=lambda x: -x[1])
    picked = {cur_item}
    for it, rate in items:
        if len(cands) >= MAXCAND: break
        if it in picked or it in used: continue
        if it in D["megastones"]:
            if not G.valid_megastone(D, nm, it) or megas_excl >= 2: continue
        if it not in D["megastones"] and rate < 2.0: continue   # 薄いアイテムは候補にしない
        picked.add(it)
        cands.append(member_spec(D, nm, it, rng))
    # メガ石が候補に無く、枠が空いていてメガ可能種なら足す（フルアタ非メガ→メガ型の比較用）
    if megas_excl < 2 and not any(C.parse_my(c)["item"] in D["megastones"] for c in cands):
        st = next((k for k in D["items"].get(nm, {}) if k in D["megastones"] and G.valid_megastone(D, nm, k) and k not in used), None)
        if st: cands.append(member_spec(D, nm, st, rng))
    return cands

def main():
    D = G.load(season=SEASON); C.D = D
    obj = json.load(open(POOL, encoding="utf-8"))
    pool = [list(p["specs"]) for p in obj["parties"]]
    n = len(pool); rng = random.Random(0)
    opp_sample = {i: [pool[k] for k in rng.sample([x for x in range(n) if x != i], GAUNTLET)] for i in range(n)}
    # 全(party,slot,candidate)×gauntlet のジョブを作る（候補は元パーティ基準で評価）
    cand_map = {}; jobs = []
    for i in range(n):
        for j in range(6):
            cands = gen_candidates(D, pool[i], j, rng)
            cand_map[(i, j)] = cands
            for ci, cspec in enumerate(cands):
                variant = list(pool[i]); variant[j] = cspec
                for gi, opp in enumerate(opp_sample[i]):
                    jobs.append(((i, j, ci), variant, opp, 1000 + i * 37 + j * 7 + ci * 3 + gi))
    print(f"母集団{n} / 候補総数{sum(len(v) for v in cand_map.values())} / 総対戦{len(jobs)} / MCTS@{SIMS}", flush=True)
    wins = {}; t0 = time.time(); done = 0
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as pool_proc:
        for key, w in pool_proc.imap_unordered(_job, jobs, chunksize=8):
            wins[key] = wins.get(key, 0) + w; done += 1
            if done % 1000 == 0:
                el = time.time() - t0
                print(f"  {done}/{len(jobs)} {el:.0f}s eta {el/done*(len(jobs)-done):.0f}s", flush=True)
    # 各(party,slot)で最良候補を採用（現行が最良ならそのまま）
    changed = 0
    for i in range(n):
        for j in range(6):
            cands = cand_map[(i, j)]
            best = max(range(len(cands)), key=lambda ci: wins.get((i, j, ci), 0))
            if best != 0 and wins.get((i, j, best), 0) > wins.get((i, j, 0), 0):
                pool[i][j] = cands[best]; changed += 1
    # 整合（同種/持ち物重複/メガ≤2/外来石/技整合）を最終化
    for i in range(n):
        mons = C.repair([C.parse_my(s) for s in pool[i]], rng)
        for m in mons:
            mv, nat, ev = G.coherent_set(D, m["name"], m["item"], m["moves"], m["nature"], m["ev"])
            m["moves"], m["nature"], m["ev"] = mv, nat, ev
        pool[i] = [C.to_spec(m) for m in mons]
    for i, p in enumerate(obj["parties"]): p["specs"] = pool[i]
    json.dump(obj, open(POOL, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"ビルド淘汰: {changed}スロット変更 / {time.time()-t0:.0f}s", flush=True)

if __name__ == "__main__":
    main()
