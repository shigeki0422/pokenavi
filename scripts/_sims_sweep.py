"""MCTSのsims数を振って、特定局面での正解手率を測る。
局面: マスカーニャ(満タン153, スカーフ, へんげんじざい) vs サーフゴー(HP83, スカーフ)。初手。
正解=はたきおとす(あく×2で確定KO・マスカが先制)。誤り=トリックフラワー(くさ×0.5)等。
sims別に T 試行（seed違い）し、はたきおとす選択率を集計。400が妥当かを判断する材料。
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

MASUKA = "マスカーニャ@こだわりスカーフ:ようき:トリックフラワー|トリプルアクセル|とんぼがえり|はたきおとす:2/32/0/0/0/32:へんげんじざい"
SURF = "サーフゴー@こだわりスカーフ:ひかえめ:シャドーボール|ゴールドラッシュ|わるだくみ|じこさいせい:2/0/0/32/0/32:おうごんのからだ"
SIMS_LIST = [100, 200, 400, 800, 1600, 3200, 6400]
T = int(os.environ.get("TRIALS", "24"))
NPROC = int(os.environ.get("NPROC", "4"))
_W = {}

def _init():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    _W["L"] = get_loader(); _W["net"] = PVNetNP.load()

def _trial(args):
    sims, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, BattleField
    from simulator.belief import OpponentBelief
    from train_az2 import _net_ai
    L = _W["L"]; net = _W["net"]
    m = build_from_spec(parse_pokemon_spec(MASUKA), L, season="M-3", randomize=False)
    s = build_from_spec(parse_pokemon_spec(SURF), L, season="M-3", randomize=False); s.hp = 83
    a = BattleSide([m]); d = BattleSide([s]); f = BattleField()
    a.belief = OpponentBelief(L); d.belief = OpponentBelief(L)
    ai = _net_ai(net, L, 0, 12, seed, mcts=True, mcts_sims=sims, mcts_select="regret", mcts_fast=True)
    act = ai(a, d, f)
    nm = act.move.name_jp if act and act.type == "move" and act.move else f"[{act and act.type}]"
    return sims, nm

def main():
    jobs = [(sims, seed) for sims in SIMS_LIST for seed in range(T)]
    agg = {sims: {} for sims in SIMS_LIST}
    ctx = mp.get_context("fork")
    with ctx.Pool(NPROC, initializer=_init) as pool:
        for sims, nm in pool.imap_unordered(_trial, jobs, chunksize=2):
            agg[sims][nm] = agg[sims].get(nm, 0) + 1
    print(f"局面: マスカ満タン vs サーフゴー83・初手 / 各{T}試行 / 正解=はたきおとす(確定KO)\n")
    print(f"{'sims':>6} | {'はたきおとす(正解)':>16} | その他")
    for sims in SIMS_LIST:
        c = agg[sims]; ko = c.get("はたきおとす", 0)
        other = ", ".join(f"{k}:{v}" for k, v in sorted(c.items(), key=lambda x: -x[1]) if k != "はたきおとす")
        print(f"{sims:>6} | {ko:>3}/{T} ({ko/T*100:4.0f}%)      | {other}")

if __name__ == "__main__":
    main()
