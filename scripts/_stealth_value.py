"""設置の価値イベントが実際に起きているかを規模で測る。
被験側に ステルスロック を強制で上げさせ、相手側が踏むダメージ・回数・タスキ破壊・4倍級被弾を集計。
イベントが豊富に起きているのに設置強制が勝率を上げない＝価値の学習(credit)失敗。
ほぼ起きない＝形式の真実（相手が踏まない）。
"""
import os, json, random, time, re
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import _pop_gen as G

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "200")); NPROC = int(os.environ.get("NPROC", "12"))
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override, Action
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    def base(my, opp, f): return certain_ko_override(ai0(my, opp, f), my, opp, f)
    def A1(my, opp, f):
        a = base(my, opp, f); me = my.active
        if me and me.is_alive and not f.stealth_rock[opp.field_idx]:
            for i, mv in enumerate(me.moves):
                if mv and mv.name_jp == "ステルスロック" and me.pp[i] > 0:
                    return Action(type="move", move=mv, move_idx=i, do_mega=bool(getattr(a, "do_mega", False)))
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    has_rock = any(any(mv and mv.name_jp == "ステルスロック" for mv in m.moves) for m in team(pa)[:0])  # placeholder
    out = {"games": 0, "rockset": 0, "hits": 0, "dmg": 0, "big": 0, "switch2": 0, "win": 0}
    try:
        PA = team(pa); PB = team(pb)
        if not any(any(mv and mv.name_jp == "ステルスロック" for mv in m.moves) for m in PA):
            return out                                # 被験側にステロ無し→対象外
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        b = Battle(s1, s2); w = b.run(A1, base)
        out["games"] = 1; out["win"] = 1 if w == 1 else 0
        maxhp = {m.name: m.max_hp for m in sb}
        for l in b.logs:
            if "ステルスロックを まき散らした" in l: out["rockset"] = 1
            m = re.search(r"(\S+) はステルスロックの効果を受けた！\((\d+)\)", l)
            if m:
                # side2(相手)の個体のみカウント
                nm = m.group(1); d = int(m.group(2))
                if nm in maxhp:
                    out["hits"] += 1; out["dmg"] += d
                    if d >= maxhp[nm] * 0.4: out["big"] += 1
            if "引っ込んだ" in l:
                nm = l.split(" は引っ込んだ")[0].strip()
                if nm in maxhp: out["switch2"] += 1
    except Exception:
        pass
    return out

def main():
    pool = [p["specs"] for p in json.load(open("func1_themed_M-3.json", encoding="utf-8"))["parties"]]
    n = len(pool); rng = random.Random(5)
    jobs = [(pool[i], pool[j], rng.randrange(10**6)) for i, j in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"{N}戦（被験側ステロ強制）で価値イベントを計測 MCTS@{SIMS}", flush=True)
    agg = {"games": 0, "rockset": 0, "hits": 0, "dmg": 0, "big": 0, "switch2": 0, "win": 0}
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r in p.map(_job, jobs):
            for k in agg: agg[k] += r[k]
    g = max(1, agg["games"])
    print(f"\n対象(被験側にステロ保持) {agg['games']}戦 / ステロ設置成功 {agg['rockset']}")
    print(f"相手のステロ被弾: 計{agg['hits']}回（1試合 {agg['hits']/g:.2f}回）/ 総ダメ{agg['dmg']}（1試合 {agg['dmg']/g:.0f}）")
    print(f"4倍級被弾(>=40%HP): {agg['big']}回（1試合 {agg['big']/g:.2f}）")
    print(f"相手の引っ込め交代: {agg['switch2']}（1試合 {agg['switch2']/g:.2f}）")
    print(f"被験側勝率: {agg['win']/g*100:.1f}%")

if __name__ == "__main__":
    main()
