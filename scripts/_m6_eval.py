"""M-6 net/設定 A/B。同一パーティ供給・同一 sims で A と B を直接対決させる。

_m3_mctseval.py の M-6 版。相手プールは PARTIES（既定=提案キャッシュ）か _pop_gen 生成。
A/B の差は env で与える:
  NET_A / NET_B          価値ネットjson（未指定=本番 az_net_np.json）
  BELIEF_A / BELIEF_B    信念シーズン（未指定=M-2＝従来）
  SIMS_A / SIMS_B        MCTS sims（既定 SIMS=400）
  EST_A / EST_B          火力見積もり補正 on|off（既定on＝姿変化・連続技あり）

EST_* は env ではなく simulator.ai のモジュール変数を呼び出しの前後で切り替える。
env はプロセス全体に効いてしまい片側だけ変えられないため。この経路は _net_ai＝Python
MCTS を直接使う（engine_dispatch の greedy_3v3/mcts_3v3 は通らない）ので、
Python 側のフラグだけで一貫する。
env: N(戦数) WORKERS POOL_SEASON(M-6) PARTIES SIMS SEL_TEMP(0.3) SEED(400)

先後は1戦ごとに入れ替える。BELIEF_* を使う側は Rust が使えない（sim.rs の
BELIEF_SEASON="M-2" 定数）ので engine_dispatch が Python 経路へ落とす＝
A/B で速度差は出るが結果の比較可能性は保たれる。
"""
import os, sys, math, random, json
os.environ.setdefault("OMP_NUM_THREADS", "1")
from multiprocessing import Pool

SEASON = os.environ.get("POOL_SEASON", "M-6")
PARTIES = os.environ.get("PARTIES", "suggest_cache.json")
SIMS = int(os.environ.get("SIMS", "400"))
SIMS_A = int(os.environ.get("SIMS_A", SIMS)); SIMS_B = int(os.environ.get("SIMS_B", SIMS))
NET_A = os.environ.get("NET_A") or None; NET_B = os.environ.get("NET_B") or None
BELIEF_A = os.environ.get("BELIEF_A") or None; BELIEF_B = os.environ.get("BELIEF_B") or None
EST_A = os.environ.get("EST_A", "on") == "on"; EST_B = os.environ.get("EST_B", "on") == "on"
SEL_TEMP = float(os.environ.get("SEL_TEMP", "0.3"))
SEED = int(os.environ.get("SEED", "400"))
_W = {}


def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    _W["L"] = get_loader()
    import _m6_pool
    _W["P"] = _m6_pool.load_parties(PARTIES)


def _ai(net_path, sims, seed, L):
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    net = PVNetNP.load(net_path) if net_path else PVNetNP.load()
    return _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=sims,
                   mcts_select="regret", mcts_fast=True)


def _batch(args):
    seed, n = args
    from simulator.battle import BattleSide, Battle, BattleField
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; P = _W["P"]; rng = random.Random(seed)
    aiA = _ai(NET_A, SIMS_A, seed, L)
    aiB = _ai(NET_B, SIMS_B, seed ^ 1540483477, L)

    def team(sp):
        return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]

    aw = al = dr = 0
    for g in range(n):
        a, b = rng.sample(P, 2)
        A = team(a); B = team(b)
        import simulator.ai as _AI0
        _sv = (_AI0._BLADE_ON, _AI0._MULTI_HIT_ON)
        Aon1_pre = (g % 2 == 0)
        _AI0._BLADE_ON = _AI0._MULTI_HIT_ON = (EST_A if Aon1_pre else EST_B)
        sa = select_party(A, B, L, n=3, temperature=SEL_TEMP, rng=rng)
        _AI0._BLADE_ON = _AI0._MULTI_HIT_ON = (EST_B if Aon1_pre else EST_A)
        sb = select_party(B, A, L, n=3, temperature=SEL_TEMP, rng=rng)
        _AI0._BLADE_ON, _AI0._MULTI_HIT_ON = _sv
        s1 = BattleSide(sa, viewer_label="P1", source6=A)
        s2 = BattleSide(sb, viewer_label="P2", source6=B)
        Aon1 = (g % 2 == 0)
        # 信念シーズンは「そのAIが持つ知識」なので側ごとに与える
        s1.belief = OpponentBelief(L, (BELIEF_A if Aon1 else BELIEF_B))
        s2.belief = OpponentBelief(L, (BELIEF_B if Aon1 else BELIEF_A))
        import simulator.ai as _AI

        def _wrap(inner, est):
            def _f(m, o, f):
                sb, sm = _AI._BLADE_ON, _AI._MULTI_HIT_ON
                _AI._BLADE_ON = _AI._MULTI_HIT_ON = est
                try:
                    return certain_ko_override(inner(m, o, f), m, o, f)
                finally:
                    _AI._BLADE_ON, _AI._MULTI_HIT_ON = sb, sm
            return _f

        f1 = _wrap(aiA, EST_A); f2 = _wrap(aiB, EST_B)
        try:
            w = Battle(s1, s2, BattleField()).run(f1 if Aon1 else f2, f2 if Aon1 else f1)
        except Exception:
            w = 0
        if w == 0:
            dr += 1
        elif (w == 1) == Aon1:
            aw += 1
        else:
            al += 1
    return aw, al, dr


def main():
    N = int(os.environ.get("N", sys.argv[1] if len(sys.argv) > 1 else "500"))
    workers = int(os.environ.get("WORKERS", str(max(1, (os.cpu_count() or 2) - 1))))
    per = max(1, N // workers)
    print(f"■ M-6 A/B: A(net={NET_A or '本番'} belief={BELIEF_A or 'M-2'} sims={SIMS_A} est={'on' if EST_A else 'off'}) vs "
          f"B(net={NET_B or '本番'} belief={BELIEF_B or 'M-2'} sims={SIMS_B} est={'on' if EST_B else 'off'}) "
          f"{per*workers}戦 season={SEASON}", flush=True)
    with Pool(workers, initializer=_winit) as p:
        res = p.map(_batch, [(SEED + k * 97, per) for k in range(workers)])
    aw = sum(r[0] for r in res); al = sum(r[1] for r in res); dr = sum(r[2] for r in res)
    dec = aw + al
    wr = aw / dec if dec else 0
    z = (aw - dec * .5) / math.sqrt(dec * .25) if dec else 0
    pv = math.erfc(abs(z) / math.sqrt(2)) if dec else 1
    print(f"A: {aw}勝 {al}敗 {dr}分 → {wr*100:.1f}% z={z:+.2f} p={pv:.4f} "
          f"{'A有意に強い' if pv < 0.05 and wr > 0.5 else ('B有意に強い' if pv < 0.05 else '有意差なし')}",
          flush=True)


if __name__ == "__main__":
    main()
