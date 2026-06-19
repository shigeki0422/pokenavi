"""価値ヘッドの校正診断: 複数チーム型のターン0ネット価値 と 実MCTS勝率 を並べ、
価値が実勝率と一致しているか(選出に使える校正か)を見る。
NET 環境変数でネット切替(既定=本番az_net_np.json)。"""
import sys, os, math, random
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-3"
NET = os.environ.get("NET")
_W = {}

def forced(D, name, item, ability):
    mv = sorted(D["moves"].get(name, {}), key=D["moves"][name].get, reverse=True)[:4] if D["moves"].get(name) else []
    nat = max(D["natures"].get(name, {"": 1}), key=D["natures"].get(name, {"": 1}).get) if D["natures"].get(name) else None
    ev = D["evs"].get(name, [(None, 1)])[0][0]
    return G._spec(name, item, nat, mv, ev, ability)

def usf(D, name):
    return forced(D, name,
                  max(D["items"].get(name, {"": 1}), key=D["items"].get(name, {"": 1}).get) if D["items"].get(name) else None,
                  max(D["abil"].get(name, {"": 1}), key=D["abil"].get(name, {"": 1}).get) if D["abil"].get(name) else None)

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader(); _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load(NET) if NET else PVNetNP.load()
    _W["net"] = net
    _W["ai"] = _net_ai(net, _W["L"], 0, 12, 0, mcts=True, mcts_sims=400, mcts_select="regret", mcts_fast=True)

def build6(core, D, rng):
    names = {s.split("@")[0].split(":")[0] for s in core}
    pool = [p for p, _ in D["usage"][:80] if p not in names]; rng.shuffle(pool)
    team = list(core)
    for p in pool:
        if len(team) >= 6: break
        it = max(D["items"].get(p, {"": 1}), key=D["items"].get(p, {"": 1}).get) if D["items"].get(p) else None
        if it and "ナイト" in it: continue
        team.append(usf(D, p))
    return team[:6]

def _job(args):
    seed, label, core, gauntlet = args
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from simulator.features import encode_state
    L = _W["L"]; ai = _W["ai"]; net = _W["net"]; D = _W["D"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    cn = len(core); w = l = d = 0; vsum = 0.0; vn = 0; cin = 0
    for opp in gauntlet:
        ts = build6(core, D, rng)
        T = team(ts); O = team(opp)
        if os.environ.get("NO_FORCE") == "1":
            sa = select_party(T, O, L, n=3, temperature=0.3, rng=rng)   # 純ヒューリスティック選出(コア強制なし)
            core_in = sum(1 for p in sa if p in T[:cn]) >= cn           # コアが揃って選ばれたか
        else:
            coreP = T[:cn]; rest = T[cn:]; need = max(0, 3 - cn)
            fs = select_party(rest, O, L, n=need, temperature=0.3, rng=rng) if need else []
            sa = (coreP + fs)[:3]; core_in = True
        sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        vsum += net.evaluate(encode_state(s1, s2, BattleField()), [0])[1]; vn += 1
        cin += 1 if core_in else 0
        r = Battle(s1, s2).run(ai, ai)
        if r == 0: d += 1
        elif r == 1: w += 1
        else: l += 1
    return label, w, l, d, vsum, vn, cin

def main():
    gn = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    D = G.load(season=SEASON); rng = random.Random(0)
    gauntlet = [G.gen_party(D, rng) for _ in range(gn)]
    rain = [forced(D, "ペリッパー", "しめったいわ", "あめふらし"), forced(D, "ラグラージ", "ラグラージナイト", "げきりゅう")]
    ctrl = [forced(D, "ガブリアス", "ガブリアスナイト", "さめはだ"), usf(D, "ブリジュラス")]
    xteam = [forced(D, "ライチュウ", "ライチュウナイトX", "せいでんき")]
    yteam = [forced(D, "ライチュウ", "ライチュウナイトY", "せいでんき")]
    cfgs = [("雨コア", rain), ("対照(メガガブ)", ctrl), ("ライチュウX", xteam), ("ライチュウY", yteam)]
    jobs = []
    for ci, (label, core) in enumerate(cfgs):
        for j in range(3):
            jobs.append((2000 + ci * 50 + j, label, core, gauntlet[j::3]))
    with Pool(12, initializer=_winit) as p:
        res = p.map(_job, jobs)
    agg = {}
    for label, w, l, d, vs, vn, cin in res:
        a = agg.setdefault(label, [0, 0, 0, 0.0, 0, 0]); a[0] += w; a[1] += l; a[2] += d; a[3] += vs; a[4] += vn; a[5] += cin
    mode = "純ヒューリスティック選出(コア強制なし)" if os.environ.get("NO_FORCE") == "1" else "コア強制選出"
    print(f"\n=== 価値校正 (net={NET or '本番'}, MCTS@400, gauntlet{gn}, {mode}) ===")
    print(f"{'型':<16}{'ターン0価値':>10}{'実勝率':>10}{'コア組成率':>10}")
    for label, _ in cfgs:
        w, l, d, vs, vn, cin = agg[label]; dec = w + l; wr = w / dec if dec else 0; v = vs / vn if vn else 0
        print(f"{label:<16}{v:>10.3f}{wr*100:>9.1f}%{cin/vn*100 if vn else 0:>9.0f}%")

if __name__ == "__main__":
    main()
