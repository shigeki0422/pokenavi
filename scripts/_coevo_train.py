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
            _eps = float(os.environ.get("SEL_EPS", "0.3"))   # 選出探索度(1.0=全探索でsynergy 3体組も経験)
            sa = explore_selection(A, B, L, rng, _eps); sb = explore_selection(B, A, L, rng, _eps)
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
    gate_ai = os.environ.get("GATE_AI", "ng")
    if gate_ai == "mcts":
        from train_az2 import _net_ai
        gsims = int(os.environ.get("GATE_SIMS", "400"))
        aiA = _net_ai(netA, L, 0, 12, 0, mcts=True, mcts_sims=gsims, mcts_select="regret", mcts_fast=True)
        aiB = _net_ai(netB, L, 0, 12, 0, mcts=True, mcts_sims=gsims, mcts_select="regret", mcts_fast=True)
        mkA = lambda: aiA; mkB = lambda: aiB
    else:
        mkA = lambda: NetGreedyAI(netA); mkB = lambda: NetGreedyAI(netB)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    aw = al = dr = 0
    for g in range(n_games):
        a, b = rng.sample(pool_specs, 2)
        try:
            A = team(a); B = team(b)
            sa = select_party(A, B, L, n=3, temperature=0.3, rng=rng); sb = select_party(B, A, L, n=3, temperature=0.3, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            Aon1 = (g % 2 == 0)
            ai1 = mkA() if Aon1 else mkB(); ai2 = mkB() if Aon1 else mkA()
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

def _broad_party(D, rng, topN=90):
    """top使用率種から広く6体を組む(usage偏重を緩め、synergyの同居を自然に発生させる)。
    制約: 重複種なし・重複道具なし・メガ最大1。各種はusage上位セット。"""
    species = [p for p, _ in D["usage"][:topN]]
    if len(species) < 6:
        species = [p for p, _ in D["usage"]]
    pick = rng.sample(species, 6)
    specs = []; used_items = set(); megas = 0
    for nm in pick:
        items = sorted(D["items"].get(nm, {}), key=D["items"][nm].get, reverse=True) if D["items"].get(nm) else [None]
        item = None
        for it in (items or [None]):
            if it in used_items: continue
            ismega = bool(it and "ナイト" in it)
            if ismega and megas >= 1: continue
            item = it; break
        if item and "ナイト" in item: megas += 1
        if item: used_items.add(item)
        ab = max(D["abil"].get(nm, {"": 1}), key=D["abil"].get(nm, {"": 1}).get) if D["abil"].get(nm) else None
        mv = sorted(D["moves"].get(nm, {}), key=D["moves"][nm].get, reverse=True)[:4] if D["moves"].get(nm) else []
        nat = max(D["natures"].get(nm, {"": 1}), key=D["natures"].get(nm, {"": 1}).get) if D["natures"].get(nm) else None
        ev = D["evs"].get(nm, [(None, 1)])[0][0]
        specs.append(G._spec(nm, item, nat, mv, ev, ab))
    return specs


def _rain_value(net_path, L, D, rng):
    """雨コア選出(ペリッパー+メガラグラージ)のターン0ネット価値。学習で上がるか追う指標。"""
    from simulator.az_np import PVNetNP
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.features import encode_state
    from simulator.ai import select_party
    net = PVNetNP.load(net_path)
    def F(nm, it, ab):
        mv = sorted(D["moves"].get(nm, {}), key=D["moves"][nm].get, reverse=True)[:4] if D["moves"].get(nm) else []
        nat = max(D["natures"].get(nm, {"": 1}), key=D["natures"].get(nm, {"": 1}).get) if D["natures"].get(nm) else None
        ev = D["evs"].get(nm, [(None, 1)])[0][0]
        return G._spec(nm, it, nat, mv, ev, ab)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    rain = team([F("ペリッパー", "しめったいわ", "あめふらし"), F("ラグラージ", "ラグラージナイト", "げきりゅう"), F("マスカーニャ", "きあいのタスキ", "へんげんじざい")])
    vs = []
    for _ in range(6):
        opp = team(G.gen_party(D, rng))
        s1 = BattleSide(rain); s2 = BattleSide(opp); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        vs.append(net.evaluate(encode_state(s1, s2, BattleField()), [0])[1])
    return sum(vs) / len(vs)


def main():
    epochs = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    games = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    n_sims = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    poolN = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    workers = 12
    from simulator.az_np import PVNetNP
    from simulator.az_loop import to_arrays
    D = G.load(season=SEASON); rng = random.Random(0)
    pool_file = os.environ.get("POOL_FILE")
    diverse = os.environ.get("DIVERSE_POOL") == "1"
    if pool_file:
        import json
        pf = json.load(open(pool_file))
        pool = [p["specs"] for p in pf["parties"]]   # 共進化で自然発見した集団(雨等のsynergyが台頭)
        src = f"進化集団:{pool_file}"
    elif diverse:
        pool = [_broad_party(D, rng) for _ in range(poolN)]   # top使用率から広く6体=synergy同居を自然発生
        src = "広域(_broad)"
    else:
        pool = [G.gen_party(D, rng) for _ in range(poolN)]   # 多様な生成集団（=拡充データ源）
        src = "標準(gen)"
    print(f"多様パーティ集団 {len(pool)} 生成 ({src})", flush=True)
    probe_L = __import__("simulator.simulate", fromlist=["get_loader"]).get_loader() if os.environ.get("RAIN_PROBE") == "1" else None
    new_arch = os.environ.get("NEW_ARCH") == "1"
    if new_arch:
        # 新encode次元のネットをゼロ初期化。アンカー=best-so-far(採用ごとに更新)で単調改善・ドリフト防止。
        from simulator.features import encode_state
        from simulator.battle import BattleSide, BattleField
        from simulator.pokemon import build_from_spec, parse_pokemon_spec
        _L = __import__("simulator.simulate", fromlist=["get_loader"]).get_loader()
        _samp = [build_from_spec(parse_pokemon_spec(s), _L, season=SEASON, randomize=False) for s in pool[0][:3]]
        dim = len(encode_state(BattleSide(_samp), BattleSide(_samp), BattleField()))
        _start = os.environ.get("START_NET")
        net = PVNetNP.load(_start) if _start else PVNetNP(dim, hidden=256, hidden2=128, seed=0)
        net.save(NET_TMP); net.save(ANCHOR_TMP)
        print(f"新アーキ: 入力{dim}次元 開始={'継続:'+_start if _start else 'ゼロ初期化'}。アンカー=best-so-far方式。", flush=True)
        if probe_L is not None:
            print(f"  [雨コア価値0] {_rain_value(NET_TMP, probe_L, D, random.Random(7)):.3f}", flush=True)
    else:
        anchor = PVNetNP.load(); anchor.save(ANCHOR_TMP)       # 凍結アンカー（=現行ネット, 本番az_net_np.jsonは不変）
        start = os.environ.get("START_NET")                     # 継続学習: 既存学習ネットから再開（アンカーは現行のまま）
        net = PVNetNP.load(start) if start else copy.deepcopy(anchor)
        net.save(NET_TMP)
        print(f"アンカー(現行ネット)を凍結。学習ネット開始={'継続:'+start if start else '現行から'}。", flush=True)
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
        no_gate = os.environ.get("NO_GATE") == "1"
        if no_gate:
            # 探索的選出(ε大)で得た実結果価値はヒューリスティック選出ゲートに映らない→常に蓄積。
            net = cand; net.save(NET_TMP)
            if new_arch: net.save(ANCHOR_TMP)
            gate_s = "蓄積(NO_GATE)"
        else:
            # ゲート: 候補 vs 凍結アンカー（大標本）
            aw, al, dr, wr, pv = ng_eval(pool, NET_TMP + ".cand", ANCHOR_TMP, 300, workers, 5000 + ep)
            accept = wr >= 0.52
            if accept:
                net = cand; net.save(NET_TMP)
                if new_arch: net.save(ANCHOR_TMP)
            gate_s = (f"候補vs{'best-so-far' if new_arch else '凍結アンカー'} {aw}-{al}"
                      f"({wr*100:.1f}% p={pv:.3f}) [{'採用' if accept else '棄却'}]")
        rain_s = ""
        if probe_L is not None:
            rain_s = f" 雨コア価値={_rain_value(NET_TMP, probe_L, D, random.Random(7)):.3f}"
        print(f"[epoch{ep+1}/{epochs}] 自己対戦{per*workers}局 学習{len(samples)}サンプル "
              f"{gate_s}{rain_s} {time.time()-t0:.0f}秒", flush=True)
    # 最終評価: 学習ネット vs 凍結アンカー（大標本）
    net.save("/tmp/coevo_final.json")
    aw, al, dr, wr, pv = ng_eval(pool, "/tmp/coevo_final.json", ANCHOR_TMP, 600, workers, 99000)
    print(f"\n=== 最終: 学習ネット vs 現行ネット（多様集団・600戦・NetGreedy）===", flush=True)
    print(f"学習ネット: {aw}勝 {al}敗 {dr}分 → 勝率{wr*100:.1f}%  p={pv:.4f}  "
          f"{'有意に強化' if pv<0.05 and wr>0.5 else ('有意に弱化' if pv<0.05 else '有意差なし')}", flush=True)
    out = os.environ.get("OUT_NET") or ("az_net_coevo.json" if SEASON == "M-2" else f"az_net_coevo_{SEASON}.json")
    import shutil; shutil.copy("/tmp/coevo_final.json", out)
    print(f"学習ネットを {out} に保存（本番az_net_np.jsonは不変）", flush=True)

if __name__ == "__main__":
    main()
