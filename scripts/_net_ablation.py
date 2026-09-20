"""ネット同士を MCTS@sims で対戦させる汎用ゲート。

既定は「学習済みネット vs ランダム初期化ネット」でネットの寄与量を測る。
NET_A / NET_B を指定すれば任意の2ネットを比較できる（価値事前学習の効果検証など）。

特徴量(v2/v3)も探索の集約(MAPLE)も効かなかった。どちらも「葉の評価関数」を良くする施策で、
効かないなら **そもそも葉の評価がボトルネックでない** 可能性がある。MCTS は実エンジンを
回すので、@400 の探索が届く範囲は評価関数が悪くても正しく判断できてしまう。

ランダム初期化ネットに対する勝率が小さければ、ネットの改善に投資しても伸びない。
大きければ、評価関数は効いており改善余地が残っている。

env: N(対戦数) SIMS(400) NET_B(比較相手。既定=ランダム初期化)
"""
import os, sys, math, random, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
import _m6_pool

SEASON = os.environ.get("POOL_SEASON", "M-6")
SIMS = int(os.environ.get("SIMS", "400"))
SIMS_B = int(os.environ.get("SIMS_B", "0")) or SIMS   # B側だけ探索量を変えられる
_f1._ensure_loaded(SEASON, 8)
NET_A = os.environ.get("NET_A")   # 未指定なら本番ネット
NET_B = os.environ.get("NET_B")   # 未指定ならランダム初期化


def _battle(args):
    pa, pb, seed, a_first = args
    import random as _r
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, certain_ko_override
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.az_np import PVNetNP
    from simulator.features import feature_dim
    from train_az2 import _net_ai
    L = _f1._W["loader"]; _r.seed(seed)
    netA = PVNetNP.load(NET_A) if NET_A else _f1._W["net"]
    if NET_B:
        netB = PVNetNP.load(NET_B)
    else:
        netB = PVNetNP(feature_dim(), hidden=netA.hidden, hidden2=netA.hidden2, seed=12345)
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
    B = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
    s1 = BattleSide(select_party(A, B, L, n=3, temperature=0.3, rng=_r), viewer_label="P1", source6=A)
    s2 = BattleSide(select_party(B, A, L, n=3, temperature=0.3, rng=_r), viewer_label="P2", source6=B)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    n1 = netA if a_first else netB
    n2 = netB if a_first else netA
    s_a, s_b = (SIMS, SIMS_B) if a_first else (SIMS_B, SIMS)
    ai1 = _net_ai(n1, L, 0, 12, seed, mcts=True, mcts_sims=s_a, mcts_select="regret", mcts_fast=True)
    ai2 = _net_ai(n2, L, 0, 12, seed ^ 0x5bd1e995, mcts=True, mcts_sims=s_b, mcts_select="regret", mcts_fast=True)
    # ORACLE_A=1: A側だけ相手の隠れ情報を全部見える状態にする（伸び代の測定用）
    if os.environ.get("ORACLE_A") == "1":
        (ai1 if a_first else ai2).oracle = True
        (ai2 if a_first else ai1).oracle = False
    # ACT_ORACLE: A側に「相手が今ターン実際に選ぶ手」を教える。分岐 5x5→5x1 で読める深さが倍になる。
    #   root=深さ0のみ / all=全深さ（上限測定）。battle は必ず ai1→ai2 の順に呼ぶ。
    # 型候補は ensure() 時に belief から引き継がれるので、map_rate も同じ経路で渡す
    # ORACLE_REVEAL_A: A側だけ型の一部を真値にする（伸び代の内訳を測る）
    _rv = os.environ.get("ORACLE_REVEAL_A")
    if _rv:
        _aiR = ai1 if a_first else ai2
        _aiR.oracle_reveal = {x for x in _rv.split(",") if x}
        if "bench" in _aiR.oracle_reveal:
            _aiR.hidden = False
    # JOINT_BUILD_A=1: A側だけ型まるごとサンプリングで決定化する（相手の型推定の改善をA/Bする）
    if os.environ.get("JOINT_BUILD_A") == "1":
        from simulator.belief import registered_builds_by_species
        _bk = registered_builds_by_species(L)
        _sA = s1 if a_first else s2
        _sA.belief.joint = True
        _sA.belief._builds = _bk
        _sA.belief._map_rate = float(os.environ.get("BUILD_MAP_RATE_A", "0") or 0)
    # NET_POL: A側の方策priorだけ別ネットから取る（どちらのヘッドが足を引っ張るかの切り分け）
    _np_ = os.environ.get("NET_POL")
    if _np_:
        from simulator.az_np import PVNetNP as _PV
        from simulator.features import encode_state as _enc
        _pol_net = _PV.load(_np_)
        _aiP = ai1 if a_first else ai2
        _baseP = _aiP.net_eval
        def _mix(A, B, f, _b=_baseP, _pn=_pol_net):
            pol, val = _b(A, B, f)
            p2, _ = _pn.evaluate(_enc(A, B, f), list(pol.keys())) if pol else ({}, 0)
            return (p2 or pol), val
        _aiP.net_eval = _mix
    # NET_ENS: A側の価値を「自ネットと NET_ENS の平均」にする（誤差が独立なら平均で減る）。方策は自ネット
    _ne = os.environ.get("NET_ENS")
    if _ne:
        from simulator.az_np import PVNetNP as _PV2
        from simulator.features import encode_state as _enc2
        _ens_net = _PV2.load(_ne)
        _aiE = ai1 if a_first else ai2
        _baseE = _aiE.net_eval
        def _avg(A, B, f, _b=_baseE, _en=_ens_net):
            pol, val = _b(A, B, f)
            _, v2 = _en.evaluate(_enc2(A, B, f), [0])
            return pol, 0.5 * (val + v2)
        _aiE.net_eval = _avg
    # COLLAPSE_MEGA=1: メガ石持ちはメガ前提で候補を出す（Rust本番と同じ＝教師πと条件を揃える）
    if os.environ.get("COLLAPSE_MEGA") == "1":
        ai1.collapse_mega = True; ai2.collapse_mega = True
    # VALUE_NOISE: A側の葉評価にガウス雑音を足す。雑音量→勝率の傾きから「評価誤差ゼロ」を外挿する。
    _vn = float(os.environ.get("VALUE_NOISE", "0") or 0)
    if _vn > 0:
        _aiV = ai1 if a_first else ai2
        _base = _aiV.net_eval
        _vr = _r.Random(seed ^ 0xC0FFEE)
        def _noisy(A, B, f, _b=_base, _g=_vr, _s=_vn):
            pol, val = _b(A, B, f)
            return pol, min(1.0, max(0.0, val + _g.gauss(0.0, _s)))
        _aiV.net_eval = _noisy
    _ao = os.environ.get("ACT_ORACLE", "")
    if _ao:
        from simulator.search_ai import SearchAI as _SA
        d = 1 if _ao == "root" else 99
        aiA, aiB = (ai1, ai2) if a_first else (ai2, ai1)
        aiA.act_oracle_depth = d
        _pend = []
        _q = float(os.environ.get("ACT_ORACLE_Q", "1") or 1)   # ヒントを与える確率
        _qr = _r.Random(seed ^ 0x1234567)
        if a_first:
            def p1(m, o, f):
                a2 = certain_ko_override(ai2(o, m, f), o, m, f)
                _pend.append(a2)
                ai1.opp_act_hint = _SA._action_index(a2) if _qr.random() < _q else None
                return certain_ko_override(ai1(m, o, f), m, o, f)
            def p2(m, o, f):
                return _pend.pop()
        else:
            def p1(m, o, f):
                a1 = certain_ko_override(ai1(m, o, f), m, o, f)
                ai2.opp_act_hint = _SA._action_index(a1) if _qr.random() < _q else None
                return a1
            def p2(m, o, f):
                return certain_ko_override(ai2(m, o, f), m, o, f)
    else:
        def p1(m, o, f): return certain_ko_override(ai1(m, o, f), m, o, f)
        def p2(m, o, f): return certain_ko_override(ai2(m, o, f), m, o, f)
    res = Battle(s1, s2, BattleField()).run(p1, p2)
    if res == 0:
        return 0
    return 1 if ((res == 1) == a_first) else -1


def _rust_battle(args):
    """本番経路（Rust IS-MCTS）で A/B する。net パスを側1/側2に振り分け、a_first で左右を入れ替える。"""
    import random as _r
    import pokenavi_engine as E
    pa, pb, seed, a_first = args
    rng = _r.Random(seed)
    sa = rng.sample(range(len(pa)), 3); sb = rng.sample(range(len(pb)), 3)
    na = NET_A or ""
    nb = NET_B or ""
    p1, p2 = (na, nb) if a_first else (nb, na)
    r = E.mcts_3v3_ab(list(pa), sa, list(pb), sb, seed, SIMS, p1, p2, SEASON)
    if r == 0:
        return 0
    return 1 if ((r == 1) == a_first) else -1


def main():
    N = int(os.environ.get("N", "200"))
    P = _m6_pool.load_parties()
    rng = random.Random(24680)
    _rust = os.environ.get("ENGINE") == "rust"
    _six = _rust   # Rust は6体を渡して選出indexを別に指定する
    jobs = [((P[a] if _six else P[a]), P[b], 80000 + i * 7717, i % 2 == 0)
            for i, (a, b) in enumerate(rng.sample(range(len(P)), 2) for _ in range(N))]
    la = os.path.basename(NET_A) if NET_A else "本番ネット"
    lb = os.path.basename(NET_B) if NET_B else ("本番ネット" if _rust else "ランダム初期化ネット")
    sm = f"sims={SIMS}" + (f" vs {SIMS_B}" if SIMS_B != SIMS else "")
    print(f"■ {la} vs {lb}  {sm}  {N}戦  {_m6_pool.describe()}", flush=True)
    w = int(os.environ.get("AB_WORKERS", "0")) or max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(w) as pool:
        out = pool.map(_rust_battle if _rust else _battle, jobs, chunksize=1)
    win = sum(1 for x in out if x > 0); lose = sum(1 for x in out if x < 0); draw = sum(1 for x in out if x == 0)
    dec = win + lose; wr = win / dec if dec else 0
    z = (win - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0
    print(f"{la}: {win}勝 {lose}敗 {draw}分 → 勝率{wr*100:.1f}%  z={z:+.2f} "
          f"p={math.erfc(abs(z)/math.sqrt(2)):.4f}", flush=True)


if __name__ == "__main__":
    main()
