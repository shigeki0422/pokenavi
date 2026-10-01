"""Product3クイック提案エンジン＋検証。
covered_sample候補 → 価値ネットのターン0パネル評価で強い順にランキング（対戦ゼロ）。
検証: サロゲート上位 vs 下位、および vs QD最終 を実戦で比較（上位が強ければサロゲート有効）。
env NCAND(300) PANEL(24) TOPN(60) K(12) SIMS(300) OUT(候補json)
"""
import os, sys, json, random, statistics
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", os.environ.get("SIMS", "300"))
import multiprocessing as mp
import feature1 as _f1
from gen_party_ga import _play_winner
from gen_party_pool import PartyGen
from _threat_coverage import load_threats, covered_sample

# M-3固定だとM-6運用でnet-t0とeval_vs_builtが旧環境のテンプレートで計算される。
SEASON = os.environ.get("POOL_SEASON", "M-3")
NCAND = int(os.environ.get("NCAND", "300"))
PANELN = int(os.environ.get("PANEL", "24"))
TOPN = int(os.environ.get("TOPN", "60"))
K = int(os.environ.get("K", "12"))

_W = {}
def _score_setup(L, net, panel_specs):
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    _W["L"] = L; _W["net"] = net
    _W["panel"] = [[build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp] for sp in panel_specs]

_SEL_SEED = 20261001    # 相手の仮定の抽選（自分の選出 2pi・パネル側 2pi+1）
_G_SEED = 20261002      # 選出と状態の符号化のダメージ計算（きまぐレーザー等がグローバル乱数を消費する）
# Rust live.rs の SEL_SEED/G_SEED と同じ値（_ensemble_surrogate の _R_SEED も live.rs の R_SEED と同じ）


class _seeded_global:
    """グローバル乱数を固定シードにして、終わったら元に戻す（採点がグローバル乱数の状態に依らず決まるように）"""
    def __init__(self, seed):
        self.seed = seed

    def __enter__(self):
        import random as _r
        self.st = _r.getstate(); _r.seed(self.seed)

    def __exit__(self, *a):
        import random as _r
        _r.setstate(self.st)


def _panel_eval(A, B, pi, encode=True, heuristic=False):
    """パネル1面: 学習選出（自分→パネル側、温度0）と、その選出の初期状態ベクトル。Rust live.rs panel_states_full と同じ。
    heuristic=True はヒューリスティック選出（ai.select_party。2段階採点の1段目＝旧採点モデルの学習時の特徴）"""
    import random as _r
    from simulator.learned_selection import learned_select_party
    from simulator.ai import select_party
    from simulator.ai import _state_snapshot, _state_restore
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    L = _W["L"]
    snap = _state_snapshot(list(A) + list(B))
    try:
        with _seeded_global(_G_SEED + pi):
            sel = select_party if heuristic else learned_select_party
            sa = sel(A, B, L, n=3, temperature=0.0, rng=_r.Random(_SEL_SEED + 2 * pi))
            sb = sel(B, A, L, n=3, temperature=0.0, rng=_r.Random(_SEL_SEED + 2 * pi + 1))
            ia = [next(k for k, p in enumerate(A) if p is m) for m in sa]
            ib = [next(k for k, p in enumerate(B) if p is m) for m in sb]
            x = None
            if encode:
                _state_restore(snap); snap = _state_snapshot(list(A) + list(B))
                s1 = BattleSide([A[i] for i in ia], source6=A); s2 = BattleSide([B[i] for i in ib], source6=B)
                s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
                x = encode_state(s1, s2, BattleField())
        return ia, ib, x
    finally:
        _state_restore(snap)


def panel_selections(A, panel=None, heuristic=False):
    """採点のパネル各面での選出 [(自分の6体の添字の並び, パネル側の6体の添字の並び), ...]（照合用）"""
    return [_panel_eval(A, B, pi, encode=False, heuristic=heuristic)[:2]
            for pi, B in enumerate(_W["panel"] if panel is None else panel)]


def surrogate_score(specs, panel=None, heuristic=False):
    """ネットのパネル特徴: パネル20面それぞれで、学習選出（既定のモデル）で選んだ両者の初期状態をネットで評価した平均。
    面ごとに個体を巻き戻し、乱数は面ごとの固定シード（グローバル乱数に依らず決まる）。Rust 経路（_live_rust.feats＝
    live.rs panel_states_full で選出まで完結）と一致（_rust_engine/live_parity.py）。
    panel: 構築済みパネル（既定 _W["panel"]）。heuristic: 選出をヒューリスティックに（2段階採点の1段目）"""
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = _W["L"]; net = _W["net"]
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    vals = [net.evaluate(_panel_eval(A, B, pi, heuristic=heuristic)[2], [0])[1]
            for pi, B in enumerate(_W["panel"] if panel is None else panel)]
    return statistics.mean(vals)

def eval_vs_built(specs, opp_built):
    """自分specs vs 相手(構築済み)。価値ネットの想定有利度と、学習選出が選ぶ自分の3体を返す。"""
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    from simulator.belief import OpponentBelief
    from simulator.battle import BattleSide, BattleField
    from simulator.features import encode_state
    L = _W["L"]; net = _W["net"]
    A = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in specs]
    names = [s.split("@")[0] for s in specs]
    sa = learned_select_party(A, opp_built, L, n=3, temperature=0.0)   # 貪欲＝各相手に最適な選出3体
    sb = learned_select_party(opp_built, A, L, n=3, temperature=0.0)
    s1 = BattleSide(sa, source6=A); s2 = BattleSide(sb, source6=opp_built)
    s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
    v = net.evaluate(encode_state(s1, s2, BattleField()), [0])[1]
    pick = []
    for m in sa:
        try: pick.append(names[A.index(m)])
        except ValueError: pass
    return float(v), pick

def wr_vs(cands, opps, seedbase):
    jobs = []; owner = []
    rng = random.Random(seedbase)
    for i, p in enumerate(cands):
        for k in range(K):
            jobs.append((p, rng.choice(opps), (seedbase + i * 131 + k * 7) & 0x7fffffff)); owner.append(i)
    workers = max(1, (os.cpu_count() or 2) - 2)
    with mp.get_context("fork").Pool(workers) as pool:
        res = pool.map(_play_winner, jobs, chunksize=4)
    w = sum(1 for r in res if r == 1); dec = sum(1 for r in res if r in (1, 2))
    return w / dec if dec else 0.5

def main():
    _f1._ensure_loaded(SEASON, 8); L = _f1._W["loader"]; net = _f1._W["net"]
    pg = PartyGen(); th = load_threats(L); rng = random.Random(0)
    final = [e["party"] for e in json.load(open("gen_pop_step1.json"))]
    panel = [final[i] for i in rng.sample(range(len(final)), PANELN)]
    _score_setup(L, net, panel)
    # 候補生成＋スコアリング
    cands = []
    while len(cands) < NCAND:
        p = covered_sample(pg, L, th, rng, tries=6)
        if p: cands.append(p)
    scored = sorted(((surrogate_score(p), p) for p in cands), key=lambda x: -x[0])
    print(f"候補{len(scored)}体をサロゲート評価。スコア範囲 {scored[-1][0]:.3f}〜{scored[0][0]:.3f}", flush=True)
    top = [p for _, p in scored[:TOPN]]
    bot = [p for _, p in scored[-TOPN:]]
    out = os.environ.get("OUT")
    if out:
        json.dump([{"party": p, "score": round(s, 4)} for s, p in scored], open(out, "w"), ensure_ascii=False)
    # 検証
    print("検証中（上位/下位 × QD最終）...", flush=True)
    top_f = wr_vs(top, final, 1000)
    bot_f = wr_vs(bot, final, 5000)
    tvb = wr_vs(top, bot, 9000)
    print(f"\n■ サロゲート検証（K={K}戦/体, SIMS={os.environ.get('GA_SIMS')}）")
    print(f"  サロゲート上位{TOPN} vs QD最終: {top_f*100:.1f}%   (無選抜covered_sample=46%)")
    print(f"  サロゲート下位{TOPN} vs QD最終: {bot_f*100:.1f}%")
    print(f"  上位 vs 下位 直接対決: {tvb*100:.1f}%  (>55%ならサロゲートが強さを識別)")

if __name__ == "__main__":
    main()
