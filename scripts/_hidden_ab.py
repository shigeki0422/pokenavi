"""隠れ選出レジームでの net vs net A/B。
NET_A(隠れ選出で再学習) vs NET_B(現行) を HIDDEN_SELECTION=1・source6付きで対戦。
NET_Aの勝率と、各ネットの交代/ピボット率を測る。隠れ選出で交代が機能＝Aが強く・よく交代するか。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("HIDDEN_SELECTION", "1")   # 上書き可（対照=0）
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "300")); NPROC = int(os.environ.get("NPROC", "12"))
NET_A = os.environ.get("NET_A", "/tmp/az_hidden.json")
NET_B = os.environ.get("NET_B", "az_net_np.json")
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L
    eng = os.environ.get("ENGINE", "mcts")
    def mk(path):
        if path == "greedy":            # 相手=Greedy(交代せず最大ダメージ)。仮説検証用
            from simulator.ai import GreedyAI
            return GreedyAI()
        net = PVNetNP.load(path)
        if eng == "tree":   # 本番sim-data(上位環境シミュレーション)と同一エンジン
            return _net_ai(net, L, 0, 12, 0, tree=True, tree_depth=2, tree_k=4, tree_det=8)
        return _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["A"] = mk(NET_A); _W["B"] = mk(NET_B)

def _mk(ai0, counter):
    from simulator.ai import certain_ko_override
    def AI(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        t = getattr(a, "type", None); counter[0] += 1
        if t == "switch": counter[2] += 1
        elif t == "move" and a.move and a.move.name_jp in PIVOT: counter[1] += 1
        return a
    return AI

def _job(args):
    pa, pb, seed, a_on1 = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; rng = random.Random(seed)
    ca = [0, 0, 0]; cb = [0, 0, 0]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        if os.environ.get("SELECT_MODE") == "mega1":
            def _m1(party, rng):
                megas = [p for p in party if getattr(p, "mega_data", None) is not None]
                sel = [rng.choice(megas)] if megas else []
                pool = [p for p in party if p not in sel and getattr(p, "mega_data", None) is None]
                rng.shuffle(pool); sel += pool[:3 - len(sel)]
                if len(sel) < 3:
                    rest = [p for p in party if p not in sel]; rng.shuffle(rest); sel += rest[:3 - len(sel)]
                return sel[:3]
            sa = _m1(PA, rng); sb = _m1(PB, rng)
        else:
            sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa, source6=PA); s2 = BattleSide(sb, source6=PB)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        aiA = _mk(_W["A"], ca); aiB = _mk(_W["B"], cb)
        ai1 = aiA if a_on1 else aiB; ai2 = aiB if a_on1 else aiA
        w = Battle(s1, s2).run(ai1, ai2)
        res = 0 if w == 0 else (1 if ((w == 1) == a_on1) else -1)
        return res, ca, cb
    except Exception:
        return 0, ca, cb

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6), k % 2 == 0)
            for k in range(N) for a, b in [rng.sample(range(n), 2)]]
    print(f"隠れ選出A/B  A={NET_A}  B={NET_B}  / {N}戦 MCTS@{SIMS}", flush=True)
    aw = bw = dr = 0; CA = [0, 0, 0]; CB = [0, 0, 0]; t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r, ca, cb in p.map(_job, jobs):
            if r == 1: aw += 1
            elif r == -1: bw += 1
            else: dr += 1
            for k in range(3): CA[k] += ca[k]; CB[k] += cb[k]
    dec = aw + bw
    print(f"完了 {time.time()-t0:.0f}s")
    print(f"A(再学習) {aw}勝 / B(現行) {bw}勝 / 分 {dr} → Aの勝率 {aw*100/max(1,dec):.1f}%")
    print(f"A 交代率: {(CA[1]+CA[2])*100/max(1,CA[0]):.1f}% (ピボ{CA[1]}+ハード{CA[2]}/{CA[0]})")
    print(f"B 交代率: {(CB[1]+CB[2])*100/max(1,CB[0]):.1f}% (ピボ{CB[1]}+ハード{CB[2]}/{CB[0]})")

if __name__ == "__main__":
    main()
