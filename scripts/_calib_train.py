"""ターン0選出価値の教師あり校正。
本体ネットと同じ893次元encode_state(特性54カテゴリ/天候/道具入り)のターン0特徴を、
MCTS強プレイでの実勝敗に回帰する校正ヘッドを学習する。自己対戦の価値ヘッドが
ターン0で雨を過小・Xを過大評価する(中盤局面支配・弱信号)のを、実測勝率の直接教師で是正。
不完全情報リーク回避: 相手の隠れ情報はbeliefから決定化してencode(自分の雨は可視なのでそのまま)。
play netは触らず別ヘッドを学習(機能1選出・機能2構築評価に転用可)。
"""
import sys, os, random, math, pickle, json
import numpy as np
from multiprocessing import Pool
import _pop_gen as G
from _selector import ValMLP

SEASON = os.environ.get("COEVO_SEASON", "M-3")
SIMS = int(os.environ.get("MCTS_SIMS", "200"))
PLAY_NET = os.environ.get("PLAY_NET")
POOL_FILE = os.environ.get("POOL_FILE", f"/tmp/coevo_parties_{SEASON}.json")
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from simulator.search_ai import SearchAI
    from train_az2 import _net_ai
    L = get_loader(); _W["L"] = L; _W["D"] = G.load(season=SEASON)
    net = PVNetNP.load(PLAY_NET) if PLAY_NET else PVNetNP.load()
    _W["ai"] = _net_ai(net, L, 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)
    _W["det"] = SearchAI(L, season=SEASON, seed=12345)
    pool = []
    if os.path.exists(POOL_FILE):
        pool = [p["specs"] for p in json.load(open(POOL_FILE, encoding="utf-8"))["parties"]]
    _W["pool"] = pool

# enabler特性/技 と abuser特性。abuserはメガ後特性も見る(雨コアのすいすい=メガラグラージのメガ後特性)。
_SYN = {
    "rain": ({"あめふらし"}, {"あまごい"}, {"すいすい"}),
    "sun": ({"ひでり"}, {"にほんばれ"}, {"ようりょくそ", "サンパワー"}),
    "sand": ({"すなおこし"}, {"すなあらし"}, {"すなかき", "すながくれ", "すなのちから"}),
    "snow": ({"ゆきふらし"}, {"ゆきげしき", "あられ"}, {"ゆきかき", "ゆきがくれ", "アイスボディ"}),
    "elec": ({"エレキメイカー"}, {"エレキフィールド"}, {"サーフテール"}),
}

def _eff_abils(p):
    s = {p.ability}
    md = getattr(p, "mega_data", None)
    if md is not None and getattr(md, "ability", None): s.add(md.ability)
    return s

def _movenames(p):
    return {mv.name_jp for mv in p.moves if mv}

def _stat_total(p):
    return p.max_hp + p.attack + p.defense + p.sp_attack + p.sp_defense + p.speed

def _detect_synergy(mons):
    pairs = []
    for kind, (set_ab, set_mv, ab_ab) in _SYN.items():
        enablers = [i for i, p in enumerate(mons) if (_eff_abils(p) & set_ab) or (_movenames(p) & set_mv)]
        abusers = [i for i, p in enumerate(mons) if _eff_abils(p) & ab_ab]
        for ei in enablers:
            for ai in abusers:
                if ei != ai: pairs.append((kind, ei, ai))
    # トリックルーム: 設置技持ち + 最も遅い高火力(エンドポイントは速度で汎用検出)
    tr = [i for i, p in enumerate(mons) if "トリックルーム" in _movenames(p)]
    if tr:
        slow = sorted(range(len(mons)), key=lambda i: mons[i].speed)
        for ei in tr:
            for ai in slow[:2]:
                if ai != ei: pairs.append(("tr", ei, ai)); break
    return pairs

def _assemble(mons, triple, rng):
    _, ei, ai = triple
    chosen = [ei, ai]
    rest = [i for i in range(len(mons)) if i not in chosen]
    third = max(rest, key=lambda i: _stat_total(mons[i])) if rest else None
    sel = [mons[ei], mons[ai]] + ([mons[third]] if third is not None else [])
    return sel[:3]

def _feat_det(my_sel, opp_sel):
    import copy
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from simulator.features import encode_state
    L = _W["L"]; det = _W["det"]
    s1 = BattleSide([copy.deepcopy(p) for p in my_sel]); s2 = BattleSide([copy.deepcopy(p) for p in opp_sel])
    bel = OpponentBelief(L, SEASON)
    cfg = det._sample_opp_config(s2, bel)
    for poke, c in zip(s2.party, cfg):
        if c is not None: det._determinize(poke, c)
    return encode_state(s1, s2, BattleField())

def _gen(args):
    seed, n_battles = args
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    from simulator.az_loop import explore_selection
    L = _W["L"]; ai = _W["ai"]; D = _W["D"]; pool = _W["pool"]; rng = random.Random(seed)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    def pick(): return rng.choice(pool) if (pool and rng.random() < 0.7) else G.gen_party(D, rng)
    def pick_synergy():
        last = None
        for _ in range(6):
            A = team(pick()); pr = _detect_synergy(A)
            if pr: return A, pr
            last = A
        return last, []
    def sel_mix(P, Q):
        return explore_selection(P, Q, L, rng, 1.0) if rng.random() < 0.5 else select_party(P, Q, L, n=3, temperature=0.4, rng=rng)
    out = []
    for _ in range(n_battles):
        try:
            rA = rng.random()
            B = team(G.gen_party(D, rng))   # 相手=メタ(usage生成)。製品用途=ラダーのメタ相手に戦う分布に合わせる
            if rA < 0.5:   # テスト側はシナジーコアを意図的に組成(ラベルは実勝敗)
                A, pr = pick_synergy()
                sa = _assemble(A, rng.choice(pr), rng) if pr else select_party(A, B, L, n=3, temperature=0.4, rng=rng)
            else:
                A = team(pick())
                sa = sel_mix(A, B)
            sb = sel_mix(B, A)
            fa = _feat_det(sa, sb); fb = _feat_det(sb, sa)
            s1 = BattleSide(sa); s2 = BattleSide(sb)
            s1.belief = OpponentBelief(L, SEASON); s2.belief = OpponentBelief(L, SEASON)
            w = Battle(s1, s2).run(ai, ai)
            if w == 0: continue
            out.append((fa, 1.0 if w == 1 else 0.0))
            out.append((fb, 1.0 if w == 2 else 0.0))
        except Exception:
            pass
    return out

def _pearson(xs, ys):
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    cov = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x-mx)**2 for x in xs)); sy = math.sqrt(sum((y-my)**2 for y in ys))
    return cov/(sx*sy) if sx and sy else 0.0

def main():
    import time
    n_battles = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    workers = 12
    per = max(1, n_battles // workers)
    t0 = time.time()
    with Pool(workers, initializer=_winit) as p:
        data = []
        for r in p.map(_gen, [(800 + k, per) for k in range(workers)]): data += r
    X = [d[0] for d in data]; Y = [d[1] for d in data]
    print(f"phase1 ラベル生成: {len(data)}局面 {time.time()-t0:.0f}秒 (勝率mean={np.mean(Y):.3f}) MCTS@{SIMS}", flush=True)
    ntr = int(len(X) * 0.9)
    sc = ValMLP(len(X[0]), hidden=128).fit(X[:ntr], Y[:ntr], epochs=80)
    pv = sc.predict(X[ntr:]); ya = np.asarray(Y[ntr:])
    r = _pearson(list(pv), list(ya)); mae = float(np.mean(np.abs(pv - ya)))
    print(f"phase2/3 学習: held-out Pearson r={r:.3f} MAE={mae:.3f} (n={len(ya)})", flush=True)
    with open("/tmp/calib_head.pkl", "wb") as fh: pickle.dump(sc, fh)
    print("保存: /tmp/calib_head.pkl", flush=True)
    _score_cores(sc)

def _score_cores(sc):
    import _calib_probe as CP
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.ai import select_party
    L = get_loader(); D = G.load(season=SEASON); rng = random.Random(0)
    _W["L"] = L; _W["det"] = __import__("simulator.search_ai", fromlist=["SearchAI"]).SearchAI(L, season=SEASON, seed=7)
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    gaunt = [G.gen_party(D, rng) for _ in range(24)]
    cores = [("雨コア", [CP.forced(D, "ペリッパー", "しめったいわ", "あめふらし"), CP.forced(D, "ラグラージ", "ラグラージナイト", "げきりゅう")]),
             ("対照(メガガブ)", [CP.forced(D, "ガブリアス", "ガブリアスナイト", "さめはだ"), CP.usf(D, "ブリジュラス")]),
             ("ライチュウX", [CP.forced(D, "ライチュウ", "ライチュウナイトX", "せいでんき")]),
             ("ライチュウY", [CP.forced(D, "ライチュウ", "ライチュウナイトY", "せいでんき")])]
    truewr = {"雨コア": 52.1, "対照(メガガブ)": 52.1, "ライチュウX": 41.7, "ライチュウY": 47.9}
    print(f"\n=== 校正ヘッドの型評価 (本番netの誤りを是正できたか / 実勝率はgauntlet48実測) ===", flush=True)
    print(f"{'型':<16}{'校正ヘッド値':>10}{'実勝率':>9}{'本番net値':>10}", flush=True)
    netval = {"雨コア": 0.307, "対照(メガガブ)": 0.606, "ライチュウX": 0.654, "ライチュウY": 0.644}
    for label, core in cores:
        cn = len(core); vs = []
        for opp in gaunt:
            ts = CP.build6(core, D, rng); T = team(ts); O = team(opp)
            coreP = T[:cn]; rest = T[cn:]; need = max(0, 3 - cn)
            fs = select_party(rest, O, L, n=need, temperature=0.3, rng=rng) if need else []
            sa = (coreP + fs)[:3]; sb = select_party(O, T, L, n=3, temperature=0.3, rng=rng)
            vs.append(float(sc.predict([_feat_det(sa, sb)])[0]))
        print(f"{label:<16}{np.mean(vs):>10.3f}{truewr[label]:>8.1f}%{netval[label]:>10.3f}", flush=True)

if __name__ == "__main__":
    main()
