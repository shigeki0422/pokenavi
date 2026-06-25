"""隠れ選出レジームの動作確認＋交代率比較。
HIDDEN_SELECTION=0/1 で同一ネット net vs net を回し、クラッシュしないか＆交代/ピボット率が変わるかを見る。
BattleSideに source6(6体ソース)を渡し、見せ合い6体・未登場控えは決定化でサンプリングされる。
"""
import os, json, glob, random, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp

SEASON = "M-3"; SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N", "120")); NPROC = int(os.environ.get("NPROC", "12"))
NET_PATH = os.environ.get("NET_PATH", "az_net_np.json")
PIVOT = {"とんぼがえり", "ボルトチェンジ", "クイックターン"}
_W = {}

def _winit():
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from simulator.simulate import get_loader
    from simulator.az_np import PVNetNP
    from train_az2 import _net_ai
    _W["L"] = get_loader()
    _W["ai"] = _net_ai(PVNetNP.load(NET_PATH), _W["L"], 0, 12, 0, mcts=True, mcts_sims=SIMS, mcts_select="regret", mcts_fast=True)

def _job(args):
    pa, pb, seed = args
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.battle import BattleSide, Battle
    from simulator.belief import OpponentBelief
    from simulator.ai import select_party, certain_ko_override
    L = _W["L"]; ai0 = _W["ai"]; rng = random.Random(seed)
    cnt = [0, 0, 0]   # [総決定, ピボット, ハード交代]
    def wrap(my, opp, f):
        a = certain_ko_override(ai0(my, opp, f), my, opp, f)
        t = getattr(a, "type", None)
        cnt[0] += 1
        if t == "switch": cnt[2] += 1
        elif t == "move" and a.move and a.move.name_jp in PIVOT: cnt[1] += 1
        return a
    def team(sp): return [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=False) for s in sp]
    try:
        PA = team(pa); PB = team(pb)
        sa = select_party(PA, PB, L, n=3, temperature=0.3, rng=rng)
        sb = select_party(PB, PA, L, n=3, temperature=0.3, rng=rng)
        s1 = BattleSide(sa, source6=PA); s2 = BattleSide(sb, source6=PB)
        s1.belief = OpponentBelief(L); s2.belief = OpponentBelief(L)
        Battle(s1, s2).run(wrap, wrap)
        return cnt, 1
    except Exception as e:
        return (str(e), 0)

def main():
    mode = os.environ.get("HIDDEN_SELECTION", "0")
    parties = [json.load(open(p))["subject_party"] for p in glob.glob("f1_cache/*.json")]
    n = len(parties); rng = random.Random(9)
    jobs = [(parties[a], parties[b], rng.randrange(10**6)) for a, b in (rng.sample(range(n), 2) for _ in range(N))]
    print(f"NET={NET_PATH} HIDDEN_SELECTION={mode} / net vs net {N}戦 MCTS@{SIMS}", flush=True)
    T = [0, 0, 0]; ok = 0; errs = []
    t0 = time.time()
    with mp.get_context("fork").Pool(NPROC, initializer=_winit) as p:
        for r, status in p.map(_job, jobs):
            if status == 1:
                for k in range(3): T[k] += r[k]
                ok += 1
            else:
                errs.append(r)
    dec, piv, hard = T
    print(f"完了 {time.time()-t0:.0f}s / 正常終了 {ok}/{N}戦")
    if errs:
        from collections import Counter
        print("エラー上位:", Counter(errs).most_common(3))
    print(f"総決定 {dec} / ピボット {piv} / ハード交代 {hard}")
    print(f"交代行動率(ピボット+ハード): {(piv+hard)*100/max(1,dec):.1f}% / 1試合あたり {(piv+hard)/max(1,ok):.2f}回")

if __name__ == "__main__":
    main()
