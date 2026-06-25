"""設置技は本当に勝率を上げるか？ A/B。
設置技保持者を含むパーティを、(A)通常MCTS と (B)MCTS＋設置強制 で同一相手と対戦させ勝率差を見る。
B>A なら設置は有効＝ネットが過小評価＝再学習/誘導に価値。差が無ければネットは正しい（短い試合で設置は低価値）。
"""
import os, json, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "200"))
NPROC = int(os.environ.get("NPROC", "12"))
HAZARDS = {"ステルスロック", "どくびし", "まきびし", "ねばねばネット"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _force_hazard(act, my, opp, field):
    """場(相手側)に設置が無く、自分が設置技を持ち、PPがあれば設置を優先（序盤の起点作成を強制）。"""
    me = my.active
    if me is None or not me.is_alive: return act
    from simulator.ai import Action
    idx = opp.field_idx
    up = field.stealth_rock[idx] or field.spikes[idx] >= 3 or field.toxic_spikes[idx] >= 2
    for i, mv in enumerate(me.moves):
        if mv and mv.name_jp in HAZARDS and me.pp[i] > 0:
            # 既に該当設置が上がっていればスキップ
            if mv.name_jp == "ステルスロック" and field.stealth_rock[idx]: continue
            if mv.name_jp == "まきびし" and field.spikes[idx] >= 3: continue
            if mv.name_jp == "どくびし" and field.toxic_spikes[idx] >= 2: continue
            if mv.name_jp == "ねばねばネット" and field.sticky_web[idx]: continue
            return Action(type="move", move=mv, move_idx=i, do_mega=bool(getattr(act, "do_mega", False)))
    return act

def _job(args):
    party, opp, seed, force = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def base(my, opp_, f): return certain_ko_override(ai0(my, opp_, f), my, opp_, f)
    def AItest(my, opp_, f):                          # 自分側のみ設置強制（KO安全弁より後＝KO優先は維持）
        a = base(my, opp_, f)
        return _force_hazard(a, my, opp_, f) if force else a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(party); PB = team(opp)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        w = Battle(s1, s2).run(AItest, base)          # s1=被験側
        has = any(any(mv and mv.name_jp in HAZARDS for mv in m.moves) for m in sa)
        return (1 if w == 1 else 0), has
    except Exception:
        return None, False

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(7)
    base_jobs = []
    for _ in range(N):
        i, j = rng.sample(range(n), 2)
        base_jobs.append((pool[i], pool[j], rng.randrange(10 ** 6)))
    print(f"設置A/B {N}戦×2アーム MCTS@{SIMS}", flush=True)
    res = {}
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for force in (False, True):
            jobs = [(a, b, s, force) for (a, b, s) in base_jobs]
            t0 = time.time(); wins = sel = wins_h = sel_h = 0
            for (w, has) in p.map(_job, jobs):
                if w is None: continue
                sel += 1; wins += w
                if has: sel_h += 1; wins_h += w
            res[force] = (wins, sel, wins_h, sel_h)
            tag = "設置強制" if force else "通常"
            print(f"{tag}: 全体 {wins}/{sel}={wins/max(1,sel)*100:.1f}% / 設置保持時 {wins_h}/{sel_h}={wins_h/max(1,sel_h)*100:.1f}%  [{time.time()-t0:.0f}s]", flush=True)
    a=res[False]; b=res[True]
    print(f"\n設置保持パの勝率: 通常 {a[2]/max(1,a[3])*100:.1f}% → 設置強制 {b[2]/max(1,b[3])*100:.1f}%  差 {(b[2]/max(1,b[3])-a[2]/max(1,a[3]))*100:+.1f}pt")

if __name__ == "__main__":
    main()
