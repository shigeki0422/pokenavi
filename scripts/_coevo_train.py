"""共進化×ネット学習の統合（M-3 試作 Step2）。
多様な生成パーティ集団でMCTS自己対戦→候補ネット学習→【凍結アンカー】に対して大標本ゲート→採用。
昨晩の轍(固定73構築・選出温度0.6・小標本ゲートで漂流悪化)を回避：
 多様性は集団から / 選出温度は通常 / ゲートは凍結アンカー比較。本番ネットには触れない（別ファイル保存）。
"""
import sys, os, random, time, math, copy
from multiprocessing import Pool
import _pop_gen as G

SEASON = os.environ.get("COEVO_SEASON", "M-2")
NET_TMP = "/tmp/coevo_net.json"
ANCHOR_TMP = "/tmp/coevo_anchor.json"

# ---- 自己対戦ワーカー（MCTS・π記録） ----
_W = {}
def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    _W["L"] = get_loader()

def _selfplay_batch(args):
    seed, pool_specs, n_games, n_sims = args
    from simulator.az_np import PVNetNP
    from simulator.az_loop import _SelfPlayAI, explore_selection
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = _W["L"]; net = PVNetNP.load(NET_TMP); rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    samples = []
    for _ in range(n_games):
        a, b = rng.sample(pool_specs, 2)
        try:
            A = team(a); B = team(b)
            sa = explore_selection(A, B, L, rng, 0.3); sb = explore_selection(B, A, L, rng, 0.3)  # 通常多様性(2メガ回避済)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            tch = os.environ.get("TEACHER", "old"); sel = os.environ.get("TEACHER_SELECT", "duct")
            ai1 = _SelfPlayAI(L, net, n_sims, 0.25, 1.0, rng, teacher=tch, select=sel)
            ai2 = _SelfPlayAI(L, net, n_sims, 0.25, 1.0, rng, teacher=tch, select=sel)
            w = Battle(s1, s2).run(ai1, ai2)
            if w != 0:
                for f, pi, lg in ai1.records: samples.append((f, pi, lg, 1.0 if w == 1 else 0.0))
                for f, pi, lg in ai2.records: samples.append((f, pi, lg, 1.0 if w == 2 else 0.0))
        except Exception:
            pass
    return samples

# ---- NetGreedy ネット対ネット（ゲート/最終評価・凍結アンカー比較） ----
def _ng_batch(args):
    seed, pool_specs, n_games, pathA, pathB = args
    from simulator.az_np import PVNetNP
    from simulator.alphazero import NetGreedyAI
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = _W["L"]; netA = PVNetNP.load(pathA); netB = PVNetNP.load(pathB); rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    aw = al = dr = 0
    for g in range(n_games):
        a, b = rng.sample(pool_specs, 2)
        try:
            A = team(a); B = team(b)
            sa = select_party(A, B, L, n=3, temperature=0.3, rng=rng); sb = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            Aon1 = (g % 2 == 0)
            ai1 = NetGreedyAI(netA if Aon1 else netB); ai2 = NetGreedyAI(netB if Aon1 else netA)
            w = Battle(s1, s2).run(ai1, ai2)
            if w == 0: dr += 1
            elif (w == 1) == Aon1: aw += 1
            else: al += 1
        except Exception: dr += 1
    return aw, al, dr

def ng_eval(pool, pathA, pathB, N, workers, seedbase):
    per = max(1, N // workers)
    args = [(seedbase + k * 7919, pool, per, pathA, pathB) for k in range(workers)]
    with Pool(workers, initializer=_winit) as p:
        res = p.map(_ng_batch, args)
    aw = sum(r[0] for r in res); al = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = aw + al; wr = aw / dec if dec else 0.0
    z = (aw - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0.0
    from math import erfc; pv = erfc(abs(z) / math.sqrt(2)) if dec else 1.0
    return aw, al, dr, wr, pv

def main():
    epochs = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    games = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    n_sims = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    poolN = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    workers = 12
    from simulator.az_np import PVNetNP
    from simulator.az_loop import to_arrays
    D = G.load(season=SEASON); rng = random.Random(0)
    pool = [G.gen_party(D, rng) for _ in range(poolN)]   # 多様な生成集団（=拡充データ源）
    print(f"多様パーティ集団 {len(pool)} 生成", flush=True)
    anchor = PVNetNP.load(); anchor.save(ANCHOR_TMP)       # 凍結アンカー（=現行ネット, 本番az_net_np.jsonは不変）
    net = copy.deepcopy(anchor); net.save(NET_TMP)
    print(f"アンカー(現行ネット)を凍結。学習ネットは別管理。", flush=True)
    for ep in range(epochs):
        t0 = time.time()
        per = max(1, games // workers)
        args = [(1000 + ep * 100 + k, pool, per, n_sims) for k in range(workers)]
        samples = []
        with Pool(workers, initializer=_winit) as p:
            for s in p.map(_selfplay_batch, args): samples += s
        X, PI, M, Y = to_arrays(samples)
        cand = copy.deepcopy(net); cand.train_pi(X, PI, M, Y, epochs=15, lr=0.05, batch=256)
        cand.save(NET_TMP + ".cand")
        # ゲート: 候補 vs 凍結アンカー（大標本）
        aw, al, dr, wr, pv = ng_eval(pool, NET_TMP + ".cand", ANCHOR_TMP, 300, workers, 5000 + ep)
        accept = wr >= 0.52
        if accept:
            net = cand; net.save(NET_TMP)
        print(f"[epoch{ep+1}/{epochs}] 自己対戦{per*workers}局 学習{len(samples)}サンプル "
              f"候補vs凍結アンカー {aw}-{al}({wr*100:.1f}% p={pv:.3f}) [{'採用' if accept else '棄却'}] "
              f"{time.time()-t0:.0f}秒", flush=True)
    # 最終評価: 学習ネット vs 凍結アンカー（大標本）
    net.save("/tmp/coevo_final.json")
    aw, al, dr, wr, pv = ng_eval(pool, "/tmp/coevo_final.json", ANCHOR_TMP, 600, workers, 99000)
    print(f"\n=== 最終: 学習ネット vs 現行ネット（多様集団・600戦・NetGreedy）===", flush=True)
    print(f"学習ネット: {aw}勝 {al}敗 {dr}分 → 勝率{wr*100:.1f}%  p={pv:.4f}  "
          f"{'有意に強化' if pv<0.05 and wr>0.5 else ('有意に弱化' if pv<0.05 else '有意差なし')}", flush=True)
    out = "az_net_coevo.json" if SEASON == "M-2" else f"az_net_coevo_{SEASON}.json"
    import shutil; shutil.copy("/tmp/coevo_final.json", out)
    print(f"学習ネットを {out} に保存（本番az_net_np.jsonは不変）", flush=True)

if __name__ == "__main__":
    main()
