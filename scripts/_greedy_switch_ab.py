"""統制A/B：攻撃方策を完全に同じ(Greedy=最大期待ダメージ)に固定し、交代の有無だけを変える。
 A = 純Greedy（交代しない・常に最大ダメージ攻撃）
 B = Greedy+優位交代（不利対面で『不利→有利かつ生存して殴り返せる』控えがあれば交代/ピボット、無ければGreedy同様に殴る）
B が A に勝てるか＝『旨みのある時だけ交代する』が本当に得かを純粋に測る。交代/ピボット使用率も集計。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"
N = int(os.environ.get("N", "400")); NPROC = int(os.environ.get("NPROC", "12"))
MYIN = float(os.environ.get("MYIN", "0.45"))    # 不利対面の閾値（被ダメ割合）
MARGIN = float(os.environ.get("MARGIN", "0.2"))  # 交代で被ダメがどれだけ下がれば優位とみなすか
OUTF = float(os.environ.get("OUTF", "0.8"))      # 交代先が相手に与えるダメ閾値
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_W = {}

def _mega_plus_random(party6, rng, n=3):
    """メガ1体＋非メガをランダムでn-1体（メガ+受け+攻め補完の現実的な選出）。
    メガ石持ちが居なければ全ランダム。メガが複数でも1体だけ採用。"""
    if len(party6) <= n:
        return list(party6)
    megas = [p for p in party6 if getattr(p, "mega_data", None) is not None]
    sel = [rng.choice(megas)] if megas else []
    pool = [p for p in party6 if p not in sel and getattr(p, "mega_data", None) is None]
    rng.shuffle(pool)
    sel += pool[:n - len(sel)]
    if len(sel) < n:   # 非メガが足りない（メガ多数）場合は残りで補完
        rest = [p for p in party6 if p not in sel]
        rng.shuffle(rest); sel += rest[:n - len(sel)]
    return sel[:n]

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.ai import GreedyAI
    _W["L"] = get_loader()
    _W["g"] = GreedyAI()

def _adv_target(my, opp, f):
    """不利対面で『不利→有利かつ生存して殴り返せる』控えindexを返す（無ければNone）。"""
    from simulator.battle import is_trapped
    from simulator.ai import _effective_speed
    from simulator.features import _expected_frac, switch_wins_1v1
    me = my.active; o = opp.active
    if me is None or o is None or not me.is_alive or not o.is_alive: return None
    if is_trapped(me, o): return None
    my_in = _expected_frac(o, me, f, my, multi_hit=True)
    if my_in < MYIN: return None                      # 不利でなければ交代しない＝対面で殴る
    ospd = _effective_speed(o, f); best = None; bg = 0.0
    for j, b in enumerate(my.party):
        if j == my.active_idx or not b.is_alive: continue
        in_f = _expected_frac(o, b, f, my, multi_hit=True); out_f = _expected_frac(b, o, f, opp, multi_hit=True)
        hp = b.hp / max(1, b.max_hp); faster = _effective_speed(b, f) > ospd
        # 真の有利交代＝交代先が1v1の撃ち合いに勝てる（着地1発＋速度考慮）。被ダメ改善も要件。
        if in_f <= my_in - MARGIN and switch_wins_1v1(in_f, out_f, hp, faster) and (out_f - in_f) > bg:
            bg = out_f - in_f; best = j
    return best

def _job(args):
    pa, pb, seed, b_is_s1 = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, Action
    L = _W["L"]; g = _W["g"]; rng = random.Random(seed)
    cnt = [0, 0, 0]  # [B総決定, Bピボット, Bハード交代]
    def A(my, opp, f): return g(my, opp, f)
    def B(my, opp, f):
        cnt[0] += 1
        tgt = _adv_target(my, opp, f)
        if tgt is not None:
            me = my.active
            for i, mv in enumerate(me.moves):
                if mv and mv.name_jp in PIVOT and me.pp[i] > 0:
                    if me.choice_locked_move and me.choice_locked_move != mv.name_jp: continue
                    cnt[1] += 1
                    return Action(type="move", move=mv, move_idx=i)
            cnt[2] += 1
            return Action(type="switch", switch_to=tgt)
        return g(my, opp, f)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        _mode = os.environ.get("SELECT_MODE")
        if _mode == "bulk":   # 耐久3体強制（参考・非現実的）
            def bulk3(party): return sorted(party, key=lambda p: -(p.max_hp + p.defense + p.sp_defense))[:3]
            sa = bulk3(PA); sb = bulk3(PB)
        elif _mode == "mega1":   # メガ1＋非メガ2体ランダム（メガ+受け+攻め補完の現実形）
            sa = _mega_plus_random(PA, rng); sb = _mega_plus_random(PB, rng)
        else:
            sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
            sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        ai1 = B if b_is_s1 else A
        ai2 = A if b_is_s1 else B
        w = Battle(s1, s2).run(ai1, ai2)
        res = 0 if w == 0 else (1 if ((w == 1) == b_is_s1) else -1)
        return res, cnt
    except Exception:
        return 0, cnt

def main():
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6), k % 2 == 0)
            for k in range(N) for a, b in [rng.sample(range(n), 2)]]
    print(f"統制A/B 純Greedy vs Greedy+優位交代 / M-1 {N}戦（攻撃方策は同一・交代有無のみ差）", flush=True)
    bw = aw = dr = 0; T = [0, 0, 0]; t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r, c in p.map(_job, jobs):
            if r == 1: bw += 1
            elif r == -1: aw += 1
            else: dr += 1
            for k in range(3): T[k] += c[k]
    dec = bw + aw
    print(f"完了 {time.time()-t0:.0f}s")
    print(f"Greedy+優位交代(B) {bw}勝 / 純Greedy(A) {aw}勝 / 引分 {dr}")
    print(f"Bの勝率（決着のみ）: {bw*100/max(1,dec):.1f}%")
    dec_tot, piv, hard = T
    print(f"Bの交代行動率: 全決定{dec_tot} 中 ピボット{piv}+ハード交代{hard} = {(piv+hard)*100/max(1,dec_tot):.1f}%（1試合あたり約{(piv+hard)/max(1,N):.2f}回）")

if __name__ == "__main__":
    main()
