"""探索あり自己対戦コーパス（_gen_value_corpus_big.py の探索版）。本番AI（Rust MCTS@400）同士だが、
序盤 X_TURNS ターンは根の訪問数^(1/X_TEMP) で手を抽選し根に Dirichlet ノイズ（pokenavi_engine.mcts_3v3_explore）、
選出は学習選出の値（z標準化）＋選出率（そのワーカーで提示された回数あたりの選出数）が50%を下回る種ほど大きいボーナス 2β·max(0, 0.5−率)を温度 SEL_TEMP で抽選（メガ1体の規則は候補側で保つ）。
価値の教師は最終勝敗のまま。

出力: OUT/shards/w{ワーカー}_c{チャンク}.npz（_gen_value_corpus_big.py と同じ列＋XW(抽選対象ターンの局面か)・XC(その対局で最善と違う手を引いた回数)
     ・RM/RO(手番側/相手側の選出に選出率の低い種が入るか)）、OUT/progress_w*.txt、OUT/sel_w*.json（種ごとの提示数・選出数）、
     OUT/xlog_w*.jsonl（チャンクごとの抽選の統計）。
env: OUT W TARGET CHUNK GUIDE(guide_pool_m6.json) GENOMES(系統の集団の glob。GROUPS と同じ系統表のもの) PER_GAME SIMS BASE_SEED TEST_EVERY  X_TURNS(6) X_TEMP(1.0) X_EPS(0.25) X_ALPHA(0.5) X_MINFRAC(0.1: 最多訪問の1割未満の手は引かない)
     SEL_MODE(explore|prod) SEL_TEMP(1.0) SEL_BETA(2.0)  GAME_MODE(explore|prod: prod は mcts_3v3_trace＝本番どおり)
停止: OUT/STOP。再実行で続きのチャンクから。
"""
import glob
import json
import math
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_k, "1")
import numpy as np
import multiprocessing as mp

SEASON = "M-6"
OUT = os.environ["OUT"]
W = int(os.environ.get("W", "12"))
TARGET = int(os.environ.get("TARGET", "150000"))
CHUNK = int(os.environ.get("CHUNK", "50"))
PER_GAME = int(os.environ.get("PER_GAME", "2"))
SIMS = int(os.environ.get("SIMS", "400"))
BASE_SEED = int(os.environ.get("BASE_SEED", "6100000000"))
TEST_EVERY = int(os.environ.get("TEST_EVERY", "25"))
X_TURNS = int(os.environ.get("X_TURNS", "6"))
X_TEMP = float(os.environ.get("X_TEMP", "1.0"))
X_EPS = float(os.environ.get("X_EPS", "0.25"))
X_ALPHA = float(os.environ.get("X_ALPHA", "0.5"))
X_MINFRAC = float(os.environ.get("X_MINFRAC", "0.1"))
SEL_MODE = os.environ.get("SEL_MODE", "explore")
SEL_TEMP = float(os.environ.get("SEL_TEMP", "1.0"))
SEL_BETA = float(os.environ.get("SEL_BETA", "2.0"))
GAME_MODE = os.environ.get("GAME_MODE", "explore")
AW = os.path.join(os.path.dirname(HERE), "_local", "ai_work")
RARE = {"カバルドン", "キラフロル", "オオニューラ", "イエッサン", "ゴリランダー", "マスカーニャ", "アーマーガア"}


def _pools():
    guide = [e["party"] for e in json.load(open(os.environ.get("GUIDE", os.path.join(HERE, "guide_pool_m6.json"))))]
    genomes = []
    for f in sorted(glob.glob(os.environ.get("GENOMES", os.path.join(AW, "coevo_groups*_M-6*.json")))):
        d = json.load(open(f))
        genomes += [[(x[0], x[1]) for x in p["groups"]] for p in d["parties"]]
    return guide, genomes


def _draw(rng, guide, genomes):
    import _coevo_groups as C
    if rng.random() < 0.5:
        return list(rng.choice(guide)), "g"
    return C.instantiate(rng.choice(genomes), rng), "c"


def skey(p):
    base = p.name.split("(")[0] if p.name.startswith("イエッサン") else p.name
    return base + ("(メガ)" if getattr(p, "mega_data", None) is not None else "")


def explore_select(P, Q, L, rng, cnt):
    from simulator.learned_selection import learned_select_scores, learned_select_party
    if SEL_MODE == "prod":
        return learned_select_party(P, Q, L, n=3, temperature=0.6)
    cands = learned_select_scores(P, Q, L, n=3)
    if not cands:
        return learned_select_party(P, Q, L, n=3, temperature=0.6)
    s = np.array([sc for _, sc in cands]); sd = s.std()
    z = (s - s.mean()) / sd if sd > 1e-9 else s * 0.0
    bon = {}
    for p in P:
        c, o = cnt.get(skey(p), [0, 0])
        bon[id(p)] = 2.0 * max(0.0, 0.5 - (c + 1.0) / (o + 2.0))
    zb = np.array([z[i] + SEL_BETA * sum(bon[id(p)] for p in order) for i, (order, _) in enumerate(cands)])
    ws = np.exp((zb - zb.max()) / max(1e-6, SEL_TEMP))
    r = rng.random() * ws.sum(); acc = 0.0
    pick = cands[-1][0]
    for (order, _), w in zip(cands, ws):
        acc += float(w)
        if r <= acc:
            pick = order
            break
    LAST_GAP.append(max(sc for _, sc in cands) - next(sc for o, sc in cands if o is pick))
    return pick


LAST_GAP = []


def worker(w):
    import pokenavi_engine as E
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    L = get_loader()
    guide, genomes = _pools()
    per_w = (TARGET + W - 1) // W
    nchunks = (per_w + CHUNK - 1) // CHUNK
    sd = os.path.join(OUT, "shards")
    prog = os.path.join(OUT, f"progress_w{w}.txt")
    selp = os.path.join(OUT, f"sel_w{w}.json")
    cnt = json.load(open(selp)) if os.path.exists(selp) else {}
    for c in range(nchunks):
        path = os.path.join(sd, f"w{w}_c{c:05d}.npz")
        if os.path.exists(path):
            continue
        if os.path.exists(os.path.join(OUT, "STOP")):
            return
        t0 = time.time()
        rows = {k: [] for k in ("X", "Y", "Q", "PI", "M", "G", "T", "NT", "ME", "TEST", "XW", "XC", "RM", "RO")}
        games = draws = fails = 0
        src = {"gg": 0, "cg": 0, "cc": 0}
        xs = {"win": 0, "chg": 0, "gap": [], "nrat": []}
        ccopy = {k: list(v) for k, v in cnt.items()}
        for j in range(CHUNK):
            idx = c * CHUNK + j
            seed = BASE_SEED + w * 10_000_000 + idx
            rng = random.Random(seed ^ 0x9E3779B9)
            try:
                pa, ka = _draw(rng, guide, genomes)
                pb, kb = _draw(rng, guide, genomes)
                random.seed(seed)
                P1 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pa]
                P2 = [build_from_spec(parse_pokemon_spec(s), L, season=SEASON, randomize=True) for s in pb]
                s1 = explore_select(P1, P2, L, rng, ccopy)
                s2 = explore_select(P2, P1, L, rng, ccopy)
                ia = [next(i for i, q in enumerate(P1) if q is p) for p in s1]
                ib = [next(i for i, q in enumerate(P2) if q is p) for p in s2]
                if GAME_MODE == "prod":
                    r, recs, _ = E.mcts_3v3_trace(list(pa), ia, list(pb), ib, seed, SIMS, SEASON, "", 0, "")
                    xl = [(0, 0, False, False, 0, 0, 0.0, 0.0, 0)] * len(recs)
                else:
                    r, recs, xl = E.mcts_3v3_explore(list(pa), ia, list(pb), ib, seed, SIMS, SEASON,
                                                     X_TURNS, X_TEMP, X_EPS, X_ALPHA, min_frac=X_MINFRAC)
            except Exception as e:
                fails += 1
                print(f"[w{w}] 失敗 seed={seed}: {e!r}", flush=True)
                continue
            for P, S in ((P1, s1), (P2, s2)):
                for p in P:
                    ccopy.setdefault(skey(p), [0, 0])
                    ccopy[skey(p)][1] += 1
                for p in S:
                    ccopy[skey(p)][0] += 1
            games += 1
            src["".join(sorted(ka + kb))] += 1
            rare = [any(p.name.split("(")[0] in RARE for p in s1), any(p.name.split("(")[0] in RARE for p in s2)]
            nchg = 0
            for t in xl:
                if t[2]:
                    xs["win"] += 1
                    if t[3]:
                        xs["chg"] += 1; nchg += 1
                        xs["gap"].append(t[7] - t[6]); xs["nrat"].append(t[4] / max(1, t[5]))
            if r == 0:
                draws += 1
                continue
            ok = [k for k, rec in enumerate(recs) if sum(n for _, n in rec[2]) > 0]
            if not ok:
                continue
            pick = sorted(rng.sample(ok, min(PER_GAME, len(ok))))
            for k in pick:
                me, x, pi, rq = recs[k]
                tot = float(sum(n for _, n in pi))
                p = np.zeros(12, np.float32); m = np.zeros(12, np.uint8)
                for a, n in pi:
                    p[a] = n / tot; m[a] = 1
                rows["X"].append(np.asarray(x, np.float32))
                rows["Y"].append(1.0 if (r == 1) == (me == 0) else 0.0)
                rows["Q"].append(rq); rows["PI"].append(p); rows["M"].append(m)
                rows["G"].append(seed); rows["T"].append(k); rows["NT"].append(len(recs)); rows["ME"].append(me)
                rows["TEST"].append(1 if idx % TEST_EVERY == 0 else 0)
                rows["XW"].append(1 if (k < len(xl) and xl[k][2]) else 0)
                rows["XC"].append(nchg)
                rows["RM"].append(int(rare[me])); rows["RO"].append(int(rare[1 - me]))
        arr = {
            "X": np.array(rows["X"], np.float32).reshape(-1, 1037),
            "Y": np.array(rows["Y"], np.float32), "Q": np.array(rows["Q"], np.float32),
            "PI": np.array(rows["PI"], np.float32).reshape(-1, 12), "M": np.array(rows["M"], np.uint8).reshape(-1, 12),
            "G": np.array(rows["G"], np.int64), "T": np.array(rows["T"], np.int16), "NT": np.array(rows["NT"], np.int16),
            "ME": np.array(rows["ME"], np.int8), "TEST": np.array(rows["TEST"], np.int8),
            "XW": np.array(rows["XW"], np.int8), "XC": np.array(rows["XC"], np.int16),
            "RM": np.array(rows["RM"], np.int8), "RO": np.array(rows["RO"], np.int8),
            "META": np.array([games, draws, fails, src["gg"], src["cg"], src["cc"]], np.int64),
        }
        tmp = path + ".tmp.npz"
        np.savez_compressed(tmp, **arr)
        os.replace(tmp, path)
        cnt = ccopy
        with open(selp + ".tmp", "w") as f:
            json.dump(cnt, f, ensure_ascii=False)
        os.replace(selp + ".tmp", selp)
        g = np.array(xs["gap"]) if xs["gap"] else np.zeros(1)
        with open(os.path.join(OUT, f"xlog_w{w}.jsonl"), "a") as f:
            f.write(json.dumps({"c": c, "games": games, "win": xs["win"], "chg": xs["chg"],
                                "gap_mean": float(g.mean()), "gap_p90": float(np.quantile(g, 0.9)),
                                "gap_gt20": int((g > 0.20).sum()), "gap_gt10": int((g > 0.10).sum()),
                                "nrat_mean": float(np.mean(xs["nrat"])) if xs["nrat"] else 0.0,
                                "sec": time.time() - t0}) + "\n")
        with open(prog, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} c={c} games={games} draws={draws} fails={fails} "
                    f"samples={len(rows['Y'])} {time.time()-t0:.0f}s\n")


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "shards"), exist_ok=True)
    for f in glob.glob(os.path.join(OUT, "shards", "*.tmp.npz")):
        os.remove(f)
    print(f"開始 {time.strftime('%Y-%m-%d %H:%M:%S')} W={W} TARGET={TARGET} CHUNK={CHUNK} PER_GAME={PER_GAME} SIMS={SIMS} "
          f"X=({X_TURNS},{X_TEMP},{X_EPS},{X_ALPHA},{X_MINFRAC}) SEL={SEL_MODE}(T{SEL_TEMP},β{SEL_BETA}) GAME={GAME_MODE} OUT={OUT}", flush=True)
    ps = [mp.get_context("spawn").Process(target=worker, args=(w,)) for w in range(W)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print(f"終了 {time.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
