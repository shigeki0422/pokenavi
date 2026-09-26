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


# Rust 経路（ENGINE=rust）が解釈しない指定。黙って無視されると「効かない」ではなく
# 「測っていない」結果になるので、起動時に落とす（SIMS_B を無視したまま探索量を比較し、
# 実際には同一 sims の健全性チェックになっていた事故の再発防止）。
_RUST_UNSUPPORTED = ("ORACLE_A", "ORACLE_REVEAL_A", "ACT_ORACLE", "ACT_ORACLE_Q",
                     "BUILD_MAP_RATE_A", "COLLAPSE_MEGA",
                     "VALUE_NOISE", "NET_POL", "NET_ENS")


_HP_DEFAULT = {"MCTS_FPU": "0.5", "RM_PRIOR_MIX": "0.25", "MCTS_P_FLOOR": "1e-3", "QSELECT_FRAC": "0.1",
               "SOLVE_PLAY": "0", "MCTS_MAX_DEPTH": "60",
               # ORACLE は既定で「素の env の値」＝両側同じ（従来どおり）。
               # HP_A="ORACLE=1" で **A側だけ** 完全情報にできる＝型予測の伸び代の測定。
               # ORACLE=1 を両側に掛けると「隠れ情報の無い別ゲーム」になり、通常条件の強さを
               # 予測しないことが実測で分かった（完全情報と通常条件の順位相関はほぼゼロ）。
               "ORACLE": os.environ.get("ORACLE", "0"),
               # HP_A="JOINT_BUILD=1" で A側だけ型プールから型まるごと決定化する
               "JOINT_BUILD": os.environ.get("JOINT_BUILD", "0"),
               # 先発の記録・消費した持ち物の記憶（2026-09-25 修正）。LEAD_SEEN=0 ITEM_GONE=0 と
               # HP_A="LEAD_SEEN=1,ITEM_GONE=1" で A側だけ修正版にして旧挙動と比べる
               "LEAD_SEEN": os.environ.get("LEAD_SEEN", "1"),
               "ITEM_GONE": os.environ.get("ITEM_GONE", "1"),
               # 計測用: HP_A="ORACLE_MIX=0.5" で A側だけ、その確率で相手の真の型を使う（精度と勝率の関係）
               "ORACLE_MIX": os.environ.get("ORACLE_MIX", "0"),
               # 計測用: HP_A="ORACLE_REVEAL=1" で A側だけ真の型の一部（1=持ち物 2=特性 4=技 8=性格・努力値）を使う
               "ORACLE_REVEAL": os.environ.get("ORACLE_REVEAL", "0")}


def _check_rust_env():
    bad = [k for k in _RUST_UNSUPPORTED if os.environ.get(k)]
    if bad:
        sys.exit(f"ENGINE=rust では未対応の指定です（Python経路で実行してください）: {', '.join(bad)}")


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
    s_a, s_b = (SIMS, SIMS_B) if a_first else (SIMS_B, SIMS)
    # HP_A="MCTS_FPU=0.3,RM_PRIOR_MIX=0.1": A側だけ探索パラメータを変える。
    # Rust は素の env を側1、*_2 を側2 に使うので、a_first に合わせて振り分ける。
    _hp = dict(kv.split("=") for kv in os.environ.get("HP_A", "").split(",") if "=" in kv)
    for k, v in _HP_DEFAULT.items():
        a_val = _hp.get(k, v)
        os.environ[k] = a_val if a_first else v
        os.environ[k + "_2"] = v if a_first else a_val
    r = E.mcts_3v3_ab(list(pa), sa, list(pb), sb, seed, s_a, p1, p2, SEASON, s_b)
    if r == 0:
        return 0
    return 1 if ((r == 1) == a_first) else -1


def main():
    N = int(os.environ.get("N", "200"))
    P = _m6_pool.load_parties()
    # 再現確認用に対戦の組と乱数の帯を変えられる（既定は従来と同じ）
    ab_seed = int(os.environ.get("AB_SEED", "24680"))
    rng = random.Random(ab_seed)
    _rust = os.environ.get("ENGINE") == "rust"
    if _rust:
        _check_rust_env()
    _six = _rust   # Rust は6体を渡して選出indexを別に指定する
    jobs = [((P[a] if _six else P[a]), P[b], (80000 if ab_seed == 24680 else ab_seed * 1000) + i * 7717, i % 2 == 0)
            for i, (a, b) in enumerate(rng.sample(range(len(P)), 2) for _ in range(N))]
    la = os.path.basename(NET_A) if NET_A else "本番ネット"
    lb = os.path.basename(NET_B) if NET_B else ("本番ネット" if _rust else "ランダム初期化ネット")
    sm = f"sims={SIMS}" + (f" vs {SIMS_B}" if SIMS_B != SIMS else "")
    print(f"■ {la} vs {lb}  {sm}  {N}戦  {_m6_pool.describe()}", flush=True)
    w = int(os.environ.get("AB_WORKERS", "0")) or max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(w) as pool:
        out = pool.map(_rust_battle if _rust else _battle, jobs, chunksize=1)
    # AB_DUMP=path: 1戦ごとの結果を書き出す（相手の型の種類ごとに勝率を分けて見る用）
    if os.environ.get("AB_DUMP"):
        import random as _r2
        rows = []
        for (pa, pb, seed, a_first), x in zip(jobs, out):
            rr = _r2.Random(seed)
            sa = rr.sample(range(len(pa)), 3); sb = rr.sample(range(len(pb)), 3)
            rows.append({"pa": pa, "pb": pb, "sa": sa, "sb": sb, "a_first": a_first, "r": x})
        with open(os.environ["AB_DUMP"], "w") as f:
            json.dump(rows, f, ensure_ascii=False)
    win = sum(1 for x in out if x > 0); lose = sum(1 for x in out if x < 0); draw = sum(1 for x in out if x == 0)
    dec = win + lose; wr = win / dec if dec else 0
    z = (win - dec * 0.5) / math.sqrt(dec * 0.25) if dec else 0
    print(f"{la}: {win}勝 {lose}敗 {draw}分 → 勝率{wr*100:.1f}%  z={z:+.2f} "
          f"p={math.erfc(abs(z)/math.sqrt(2)):.4f}", flush=True)


if __name__ == "__main__":
    main()
