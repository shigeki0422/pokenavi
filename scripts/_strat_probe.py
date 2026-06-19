"""戦略の実効性検証: 雨コア(ペリッパー+メガラグラージ) と メガライチュウX/Y を
本番ネット(MCTS@400)で gauntlet(usage生成メタ) と対戦させ勝率を測る。
テストチーム=コア固定+usfiller。両者select_party選出。"""
import sys, os, random, math
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-3"
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader(); _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load()
    _W["ai"] = _net_ai(net, _W["L"], 0, 12, 0, mcts=True, mcts_sims=400, mcts_select="regret", mcts_fast=True)

def forced(D, name, item, ability):
    mv = sorted(D["moves"].get(name, {}), key=D["moves"][name].get, reverse=True)[:4] if D["moves"].get(name) else []
    nat = max(D["natures"].get(name, {"": 1}), key=D["natures"].get(name, {"": 1}).get) if D["natures"].get(name) else None
    ev = D["evs"].get(name, [(None, 1)])[0][0]
    return G._spec(name, item, nat, mv, ev, ability)

def usfiller(D, name):
    return forced(D, name,
                  max(D["items"].get(name, {"": 1}), key=D["items"].get(name, {"": 1}).get) if D["items"].get(name) else None,
                  max(D["abil"].get(name, {"": 1}), key=D["abil"].get(name, {"": 1}).get) if D["abil"].get(name) else None)

def build_test(core_specs, core_names, D, rng):
    # コア + 非メガ・非コアのusage種でfillerを6体まで
    cands = [p for p, _ in D["usage"][:60] if p not in core_names
             and not D["items"].get(p, {}) or True]
    pool = [p for p, _ in D["usage"][:80] if p not in core_names]
    rng.shuffle(pool)
    team = list(core_specs)
    for p in pool:
        if len(team) >= 6: break
        # メガ石持ちfillerは避ける(コアに既にメガ)
        it = max(D["items"].get(p, {"": 1}), key=D["items"].get(p, {"": 1}).get) if D["items"].get(p) else None
        if it and "ナイト" in it: continue
        team.append(usfiller(D, p))
    return team[:6]

def _job(args):
    seed, label, core_specs, core_names, gauntlet, K = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; ai = _W["ai"]; D = _W["D"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    w = l = d = 0
    for opp in gauntlet:
        for k in range(K):
            ts = build_test(core_specs, core_names, D, rng)
            try:
                T = team(ts); O = team(opp); cn = len(core_specs)
                def tsel(P, Q):   # テスト側: コアを必ず選出に入れ、残りをselect_party(選出ベンチ交絡を排除)
                    core = P[:cn]; rest = P[cn:]; need = max(0, 3 - len(core))
                    fs = select_party(rest, Q, L, n=need, temperature=0.3, rng=rng) if need else []
                    return (core + fs)[:3]
                ton1 = (k % 2 == 0)   # テストチームの先後を交互に(側バイアス排除)
                if ton1:
                    sa = tsel(T, O); sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
                else:
                    sa = select_party(O, T, L, n=3, temperature=0.3, rng=rng); sb = tsel(T, O)
                s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
                r = Battle(s1, s2).run(ai, ai)
                if r == 0: d += 1
                elif (r == 1) == ton1: w += 1
                else: l += 1
            except Exception:
                d += 1
    return label, w, l, d

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    K = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    workers = 12
    import time
    D = G.load(season=SEASON); rng = random.Random(0)
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    rain = [forced(D, "ペリッパー", "しめったいわ", "あめふらし"), forced(D, "ラグラージ", "ラグラージナイト", "げきりゅう")]
    ctrl = [forced(D, "ガブリアス", "ガブリアスナイト", "さめはだ"), forced(D, "ラグラージ", "ラグラージナイト", "げきりゅう")]
    xteam = [forced(D, "ライチュウ", "ライチュウナイトX", "せいでんき")]
    yteam = [forced(D, "ライチュウ", "ライチュウナイトY", "せいでんき")]
    configs = [
        ("雨コア(ペリッパー+メガラグラージ)", rain, {"ペリッパー", "ラグラージ"}),
        ("対照(メガガブ+メガラグラージ)", ctrl, {"ガブリアス", "ラグラージ"}),
        ("メガライチュウX", xteam, {"ライチュウ"}),
        ("メガライチュウY", yteam, {"ライチュウ"}),
    ]
    # 各configをgauntletチャンク並列化
    jobs = []
    per = max(1, gn // (workers // 4 or 1))
    for ci, (label, core, names) in enumerate(configs):
        chunks = [gauntlet[i::3] for i in range(3)]
        for j, ch in enumerate(chunks):
            jobs.append((1000 + ci * 50 + j, label, core, names, ch, K))
    t0 = time.time()
    with Pool(workers, initializer=_winit) as p:
        res = p.map(_job, jobs)
    agg = {}
    for label, w, l, d in res:
        a = agg.setdefault(label, [0, 0, 0]); a[0] += w; a[1] += l; a[2] += d
    print(f"\n=== 戦略実効性 (本番ネットMCTS@400, vs usgauntlet, {time.time()-t0:.0f}秒) ===")
    for label, _, _ in configs:
        w, l, d = agg[label]; dec = w + l; wr = w / dec if dec else 0
        z = (w - dec * .5) / math.sqrt(dec * .25) if dec else 0
        from math import erfc; pv = erfc(abs(z) / math.sqrt(2)) if dec else 1
        print(f"{label}: {w}勝 {l}敗 {d}分 → {wr*100:.1f}% (p={pv:.3f})")

if __name__ == "__main__":
    main()
