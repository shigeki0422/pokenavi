"""M-1上位テンプレ上で3モデルの勝率・交代率を比較。
 M0 現行 = 移植ネット(旧挙動)        / override無し
 M1 今回 = 模倣ネット(交代学習済)     / override無し
 M2 強制 = 模倣ネット + 不利対面交代を強く促すoverride
ペア総当たり(0v1,0v2,1v2)・パーティはM-1テンプレからランダム。各モデルの勝率と自発交代/試合を集計。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120")); NPROC = int(os.environ.get("NPROC", "12"))
TRANSFER = "/tmp/transfer_net.json"; IMIT = "az_net_np.json"
MODELS = {0: (TRANSFER, "none"), 1: (IMIT, "none"), 2: (IMIT, "strong")}
NAMES = {0: "現行(移植)", 1: "今回(模倣)", 2: "強制交代"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["ai"] = {}
    for path in {TRANSFER, IMIT}:
        net = PVNetNP.load(path)
        _W["ai"][path] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _strong_switch(a, my, opp, f):
    from simulator.battle import is_trapped
    from simulator.ai import Action, _effective_speed
    from simulator.features import _expected_frac
    me = my.active; o = opp.active
    if me is None or o is None or not me.is_alive or not o.is_alive: return a
    if getattr(a, "type", None) == "switch" or is_trapped(me, o): return a
    my_in = _expected_frac(o, me, f, my)
    if my_in < 0.4: return a
    if _expected_frac(me, o, f, opp) >= 1.0 and _effective_speed(me, f) > _effective_speed(o, f): return a
    ospd = _effective_speed(o, f); best = None; bg = 0.0
    for j, b in enumerate(my.party):
        if j == my.active_idx or not b.is_alive: continue
        in_f = _expected_frac(o, b, f, my); out_f = _expected_frac(b, o, f, opp)
        hp = b.hp / max(1, b.max_hp); need = 1 if _effective_speed(b, f) > ospd else 2
        if in_f < my_in and out_f >= 0.5 and hp > in_f * need and out_f - in_f > bg:
            bg = out_f - in_f; best = j
    return Action(type="switch", switch_to=best) if best is not None else a

_PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
def _mk_ai(mid, counter):   # counter=[hard交代, ピボット, 全決定]
    from simulator.ai import certain_ko_override
    path, mode = MODELS[mid]; ai0 = _W["ai"][path]
    def AI(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        if mode == "strong":
            a = _strong_switch(a, my, opp, f)
        t = getattr(a, "type", None)
        if t == "switch": counter[0] += 1
        elif t == "move" and a.move and a.move.name_jp in _PIVOT: counter[1] += 1
        counter[2] += 1
        return a
    return AI

def _job(args):
    mi, mj, pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party
    L = _W["L"]; rng = random.Random(seed)
    ci = [0, 0, 0]; cj = [0, 0, 0]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        w = Battle(s1, s2).run(_mk_ai(mi, ci), _mk_ai(mj, cj))
        return mi, mj, w, ci, cj
    except Exception:
        return mi, mj, 0, [0, 0, 0], [0, 0, 0]

def main():
    parties = [json.load(open(f))["subject_party"] for f in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(5)
    print(f"M-1テンプレ {n}本 / 3モデル ペア総当たり 各{N}戦 MCTS@{SIMS}", flush=True)
    jobs = []
    for (mi, mj) in [(0, 1), (0, 2), (1, 2)]:
        for k in range(N):
            a, b = rng.sample(range(n), 2)
            # 先攻側の偏り回避: kの偶奇でモデルの side を入替
            if k % 2 == 0: jobs.append((mi, mj, parties[a], parties[b], 1000 + k))
            else: jobs.append((mj, mi, parties[a], parties[b], 1000 + k))
    win = {0: [0, 0], 1: [0, 0], 2: [0, 0]}                # [wins, games]
    sw = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0]}        # [hard, pivot, decisions]
    t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for mi, mj, w, ci, cj in p.imap_unordered(_job, jobs, chunksize=4):
            win[mi][1] += 1; win[mj][1] += 1
            if w == 1: win[mi][0] += 1
            elif w == 2: win[mj][0] += 1
            for k in range(3): sw[mi][k] += ci[k]; sw[mj][k] += cj[k]
    print(f"完了 {time.time()-t0:.0f}s\n")
    print(f"{'モデル':<14}{'勝率':>7} {'ハード':>7} {'ピボット':>8} {'合計交代/試合':>12} {'合計交代率':>10}")
    for mid in (0, 1, 2):
        g = max(1, win[mid][1]); wr = win[mid][0] / g
        hard, piv, dec = sw[mid]; tot = hard + piv
        print(f"{NAMES[mid]:<14}{wr*100:>6.1f}% {hard/g:>7.2f} {piv/g:>8.2f} {tot/g:>12.2f} {tot/max(1,dec)*100:>9.1f}%")
    print("\n（交代＝片側1試合あたり。合計＝ハード交代＋ピボット技。勝率は3モデル総当たり）")

if __name__ == "__main__":
    main()
