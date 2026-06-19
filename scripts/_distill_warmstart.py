"""蒸留ウォームスタート: 旧champion(665)の方策/価値を、新encode(893)の新ネットへ移植。
dual-encoder: 旧encode(features_v665)でchampionを評価しラベル化、新encode(features)で新ネットを学習。
ゼロ初期化from-scratchの頭打ちを回避し、champion水準の893ネットを作る土台。
"""
import sys, os, random, math, pickle
from multiprocessing import Pool
import _pop_gen as G

SEASON = "M-3"
CHAMP = "az_net_coevo_M-3_prefeatfix.json"   # 旧665champion(+7.6pt)
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    _W["L"] = get_loader()
    _W["D"] = G.load(season=SEASON)

def _gen_samples(args):
    seed, n_battles = args
    from simulator.az_np import PVNetNP
    from simulator.alphazero import legal_actions_indexed
    from simulator.battle import Action, BattleSide, Battle
    from simulator.ai import HeuristicAI, _forced_charging_action, select_party
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator import features_v665 as fv
    from simulator.features import encode_state as enc_new
    L = _W["L"]; champ = PVNetNP.load(CHAMP); rng = random.Random(seed)
    fb = HeuristicAI()
    samples = []
    class DistillAI:
        def __call__(self, my_side, opp_side, field):
            me = my_side.active
            if not me.is_alive: return Action(type="pass")
            forced = _forced_charging_action(me)
            if forced: return forced
            legal = legal_actions_indexed(my_side, opp_side, field)
            if not legal: return fb(my_side, opp_side, field)
            idxs = [ix for _, ix in legal]
            try:
                pri, val = champ.evaluate(fv.encode_state(my_side, opp_side, field), idxs)
            except Exception:
                return fb(my_side, opp_side, field)
            if pri and len(legal) > 1:
                samples.append((enc_new(my_side, opp_side, field), dict(pri), list(idxs), float(val)))
            if not pri: return legal[0][0]
            best = max(pri, key=pri.get)
            for act, ix in legal:
                if ix == best: return act
            return legal[0][0]
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    pool = _W["D"]
    ai = DistillAI()
    for _ in range(n_battles):
        a = G.gen_party(pool, rng); b = G.gen_party(pool, rng)
        try:
            A = team(a); B = team(b)
            sa = select_party(A, B, L, n=3, temperature=0.5, rng=rng); sb = select_party(B, A, L, n=3, temperature=0.5, rng=rng)
            s1 = BattleSide(sa); s2 = BattleSide(sb); s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
            Battle(s1, s2).run(ai, ai)
        except Exception:
            pass
    return samples

def main():
    n_battles = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    workers = 12
    import time
    per = max(1, n_battles // workers)
    t0 = time.time()
    with Pool(workers, initializer=_winit) as p:
        res = p.map(_gen_samples, [(700 + k, per) for k in range(workers)])
    samples = [s for r in res for s in r]
    print(f"蒸留サンプル生成: {len(samples)}局面 {time.time()-t0:.0f}秒", flush=True)
    # 次元測定して新ネット作成
    from simulator.az_np import PVNetNP
    from simulator.az_loop import to_arrays
    dim = len(samples[0][0])
    net = PVNetNP(dim, hidden=256, hidden2=128, seed=0)
    X, PI, M, Y = to_arrays(samples)
    # held-out 相関検証用
    nh = max(1, len(X) // 10)
    net.train_pi(X[nh:], PI[nh:], M[nh:], Y[nh:], epochs=epochs, lr=0.05, batch=256)
    # スモーク: 新ネットの価値が championの価値(Y)を再現するか
    import numpy as np
    pv = np.array([net.evaluate(X[i], list(range(1)))[1] for i in range(nh)])
    yv = np.array(Y[:nh])
    r = float(np.corrcoef(pv, yv)[0, 1]) if len(pv) > 2 else 0.0
    mae = float(np.mean(np.abs(pv - yv)))
    print(f"蒸留検証(held-out {nh}): champ価値との相関 r={r:.3f} MAE={mae:.3f}", flush=True)
    net.save("az_net_coevo_M-3_distilled.json")
    print(f"保存: az_net_coevo_M-3_distilled.json (dim={dim}) {'→良好(r>0.7)' if r>0.7 else '→相関低・要確認'}", flush=True)

if __name__ == "__main__":
    main()
