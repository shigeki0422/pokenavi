"""価値ヘッド用コーパスをランダム方策の自己対戦から作る。

価値の学習に必要なのは (盤面, 最終勝敗) の組だけで、そこに至る行動の質は問わない。
ランダム方策は MCTS を一切呼ばないので桁違いに安く、しかも盤面空間を広く覆う。

実測（検証は MCTS 自己対戦の局面で統一・prod入力1037次元・256x128）:
    MCTS 1,428件      勝敗的中 58.7%  Brier 0.2365
    ランダム 60,000件  勝敗的中 68.3%  Brier 0.2137   ← +9.6pt
    ランダム 167,957件 勝敗的中 67.5%  Brier 0.2045
生成速度は 2,117 サンプル/秒 で、MCTS 自己対戦の 6.8 サンプル/秒 の約310倍。
12,000局・17万サンプルが79秒（MCTSなら約7時間）。

従来は価値も方策も MCTS 自己対戦から作っており、高価なデータを価値に使って
量が確保できず過学習していた（学習75% / 検証58%）。データの種類を分けるべき:
    価値ヘッド … (盤面, 勝敗)         → ランダムで安く大量に
    方策ヘッド … (盤面, MCTS訪問分布) → 強い探索が必須（ランダムでは学習できない）

状態分布とラベル方策は分離できる（2026-09-17 の設計）:
    POLICY=random  全ターンをランダムで指す（従来。ラベルは V^random ＝別の関数）
    POLICY=mcts    LABEL_SIMS の MCTS で指す（ラベルは V^MCTS ＝正しい目的関数）
    BURN=k         最初の k ターンだけランダムで進めて記録しない（開始局面を広げる）
                   BURN=rand で対戦ごとに 0..6 から抽選
「広い状態 × 強いラベル」= POLICY=mcts BURN=rand が本命。

env: G(対戦数) W(並列数) OUT_PREFIX(既定 /tmp/rnd) POLICY(random) LABEL_SIMS(400) BURN(0)
"""
import os, sys, random, time
sys.path.insert(0, "/Users/shigeki/work/pokenavi/scripts")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import multiprocessing as mp

SEASON = "M-6"
N_GAMES = int(os.environ.get("G", "200"))
W = int(os.environ.get("W", "12"))
POLICY = os.environ.get("POLICY", "random")
LABEL_SIMS = int(os.environ.get("LABEL_SIMS", "400"))
BURN = os.environ.get("BURN", "0")
SEED = int(os.environ.get("SEED", "7000"))
RECORD_PI = os.environ.get("RECORD_PI", "0") == "1"   # 根の訪問分布も記録（方策ヘッド用）
ENGINE = os.environ.get("ENGINE", "py")               # rust で Rust エンジン（BURN非対応）
NODE_TRACE = os.environ.get("NODE_TRACE", "0")        # >0 で探索木の内部ノードも教師にする
PER_GAME = int(os.environ.get("PER_GAME", "0"))       # 1対局から採る局面数（0=全部）。
                                                      # 同一対局の局面は勝敗ラベルを共有＝強く相関し、
                                                      # 価値ヘッドが過学習する（AlphaGo 2016 と同じ症状）


def _batch_rust(args):
    """Rust の mcts_3v3_trace で (盤面, 訪問分布, 勝敗) を集める。1コアで Python 13コア相当。"""
    import random as _r
    import pokenavi_engine as E
    from simulator.az_np import ACTION_DIM
    seed, parties, n = args
    rng = _r.Random(seed)
    out = []
    for g in range(n):
        gid = seed * 1000000 + g
        ia, ib = rng.sample(range(len(parties)), 2)
        pa = list(parties[ia][:6]); pb = list(parties[ib][:6])
        sa = rng.sample(range(len(pa)), 3); sb = rng.sample(range(len(pb)), 3)
        r, recs, nodes = E.mcts_3v3_trace(pa, sa, pb, sb, seed * 100003 + g, LABEL_SIMS, SEASON)
        if r == 0:
            continue
        # 探索木の内部ノード（= MCTS が実際に評価する分布・兄弟局面を含む）。
        # MCTS はこのノードの下も探索しているので訪問分布も教師にできる。
        # 価値ターゲットは逆伝播済みの値そのもの（λ収益の対象外）
        for x, v, pi in nodes:
            tot = sum(c for _, c in pi)
            if tot <= 0:
                continue
            out.append((x, v, {a: c / tot for a, c in pi}, [a for a, _ in pi], v, gid))
        keep = [(me, x, pi, rq) for me, x, pi, rq in recs
                if sum(c for _, c in pi) > 0 and len(pi) > 1]
        if PER_GAME and len(keep) > PER_GAME:
            keep = [keep[i] for i in sorted(rng.sample(range(len(keep)), PER_GAME))]
        for k, (me, x, pi, rq) in enumerate(keep):
            tot = sum(c for _, c in pi)
            y = 1.0 if (r == 1) == (me == 0) else 0.0
            out.append((x, y, {a: c / tot for a, c in pi}, [a for a, _ in pi], rq, gid))
    return out


def _batch(args):
    seed, parties, n = args
    import random as _r
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle, BattleField, Action
    from simulator.features import encode_state
    L = get_loader(); rng = _r.Random(seed)
    out = []
    lab_ai = None
    if POLICY == "mcts":
        import feature1 as _f1
        _f1._ensure_loaded(SEASON, 1)
        from train_az2 import _net_ai
        _net = _f1._W["net"]; _L = _f1._W["loader"]
    for g in range(n):
        ia, ib = rng.sample(range(len(parties)), 2)
        _r.seed(seed * 1000 + g)
        A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in parties[ia][:3]]
        B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in parties[ib][:3]]
        s1 = BattleSide(A, viewer_label="P1"); s2 = BattleSide(B, viewer_label="P2")
        s1.field_idx = 0; s2.field_idx = 1
        b = Battle(s1, s2, BattleField())
        snaps = []
        def legal(side):
            act = side.active; o = []
            for i, m in enumerate(act.moves or []):
                if m is not None:
                    o.append(Action(type="move", move=m, move_idx=i, switch_to=-1, do_mega=False))
                    if getattr(act, "mega_data", None) is not None and not act.mega_evolved and not side.mega_used:
                        o.append(Action(type="move", move=m, move_idx=i, switch_to=-1, do_mega=True))
            for j, p in enumerate(side.party):
                if j != side.active_idx and p.is_alive:
                    o.append(Action(type="switch", move=None, move_idx=None, switch_to=j, do_mega=False))
            return o
        burn = rng.randint(0, 6) if BURN == "rand" else int(BURN)
        if POLICY == "mcts":
            from simulator.ai import certain_ko_override
            m1 = _net_ai(_net, _L, 0, 12, seed * 131 + g, mcts=True, mcts_sims=LABEL_SIMS,
                         mcts_select="regret", mcts_fast=True)
            m2 = _net_ai(_net, _L, 0, 12, seed * 131 + g + 7, mcts=True, mcts_sims=LABEL_SIMS,
                         mcts_select="regret", mcts_fast=True)
        def _rand(m):
            la = legal(m)
            return rng.choice(la) if la else Action(type="move", move=m.active.moves[0], move_idx=0, switch_to=-1, do_mega=False)
        pi_recs = [[], []]
        def _act(ai, side_i, m, o, f):
            if b.turn <= burn or POLICY != "mcts":
                return _rand(m)
            if not RECORD_PI:
                return certain_ko_override(ai(m, o, f), m, o, f)
            act, pi = ai.mcts_policy(m, o, f, temperature=1.0)
            if act is None:
                return _rand(m)
            lg = [ai._action_index(a) for a in ai._candidate_actions(m, o, f)]
            if pi and len(lg) > 1:
                pi_recs[side_i].append((encode_state(m, o, f), pi, lg))
            return certain_ko_override(act, m, o, f)
        def ai1(m, o, f): return _act(m1, 0, m, o, f)
        def ai2(m, o, f): return _act(m2, 1, m, o, f)
        def on_turn(bt):
            # side1視点の盤面を記録（価値は P(side1勝利)）。burn 中は記録しない
            if bt.turn > burn and not RECORD_PI:
                snaps.append(encode_state(bt.side1, bt.side2, bt.field))
        res = b.run(ai1, ai2, on_turn=on_turn)
        if res == 0:
            continue
        y = 1.0 if res == 1 else 0.0
        if RECORD_PI:
            for si, recs in enumerate(pi_recs):
                yy = y if si == 0 else 1.0 - y
                for feat, pi, lg in recs:
                    out.append((feat, yy, pi, lg))
        else:
            for v in snaps:
                out.append((v, y))
    return out


if __name__ == "__main__":
    import _m6_pool
    P = _m6_pool.load_parties()
    t0 = time.time()
    per = max(1, N_GAMES // W)
    with mp.get_context("fork").Pool(W) as pool:
        fn = _batch_rust if ENGINE == "rust" else _batch
        res = pool.map(fn, [(SEED + k, P, per) for k in range(W)])
    data = [x for r in res for x in r]
    X = np.array([d[0] for d in data], dtype=float)
    Y = np.array([d[1] for d in data], dtype=float)
    if RECORD_PI:
        from simulator.az_np import ACTION_DIM
        PI = np.zeros((len(data), ACTION_DIM)); M = np.zeros((len(data), ACTION_DIM))
        for k, d in enumerate(data):
            for ix in d[3]:
                M[k, ix] = 1.0
            for a, p in d[2].items():
                PI[k, a] = p
    el = time.time() - t0
    pref = os.environ.get("OUT_PREFIX", "/tmp/rnd")
    np.save(pref + "_X.npy", X); np.save(pref + "_Y.npy", Y)
    if RECORD_PI:
        np.save(pref + "_PI.npy", PI); np.save(pref + "_M.npy", M)
        if ENGINE == "rust":
            np.save(pref + "_Q.npy", np.array([d[4] for d in data], dtype=float))
            np.save(pref + "_G.npy", np.array([d[5] for d in data], dtype=np.int64))
    print(f"{ENGINE}/{POLICY}(sims={LABEL_SIMS},burn={BURN}) {per*W}局 → {len(X)}サンプル  {el:.0f}秒 → {pref}_X.npy "
          f"({len(X)/el:.0f}サンプル/秒)  勝率ラベル平均={Y.mean():.3f}", flush=True)
