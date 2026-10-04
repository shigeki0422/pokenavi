"""価値ヘッド用の大規模コーパス（対局数を稼ぐ版）。本番AI同士（Rust MCTS@400・学習選出 温度0.6・JOINT_BUILD 既定）で
多様なパーティ（guide_pool_m6 の3000党＋共進化の系統集団から毎戦型を引く）を対戦させ、1対局から PER_GAME 局面だけ抜き出す。

価値ヘッドの実効サンプル数は局面数でなく対局数（同一対局の局面は勝敗ラベルを共有して強く相関する）なので、
対局を増やして1対局あたりの局面を減らす。

出力: OUT/shards/w{ワーカー}_c{チャンク}.npz（X float32 1037次元・Y・Q(根の価値)・PI・M・G(対局id)・T(手番の通し番号)・NT・ME・TEST）
     OUT/progress_w{ワーカー}.txt。チャンク単位で原子的に保存するので、再起動すると続きのチャンクから再開する。
env: OUT  W(10)  TARGET(総対局数・既定400000)  CHUNK(100)  PER_GAME(2)  SIMS(400)  SEL_TEMP(0.6)  BASE_SEED(5100000000)
     TEST_EVERY(25: idx%25==0 の対局を検証用に印を付ける)
停止: OUT/STOP を作ると各ワーカーが今のチャンクを保存して抜ける（消して再実行すれば続きから）。
"""
import glob
import json
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
OUT = os.environ.get("OUT", os.path.join(os.path.dirname(HERE), "_local", "ai_work", "valcorpus_20261002"))
W = int(os.environ.get("W", "10"))
TARGET = int(os.environ.get("TARGET", "400000"))
CHUNK = int(os.environ.get("CHUNK", "100"))
PER_GAME = int(os.environ.get("PER_GAME", "2"))
SIMS = int(os.environ.get("SIMS", "400"))
SEL_TEMP = float(os.environ.get("SEL_TEMP", "0.6"))
BASE_SEED = int(os.environ.get("BASE_SEED", "5100000000"))
TEST_EVERY = int(os.environ.get("TEST_EVERY", "25"))
AW = os.path.join(os.path.dirname(HERE), "_local", "ai_work")


def _pools():
    guide = [e["party"] for e in json.load(open(os.path.join(HERE, "guide_pool_m6.json")))]
    genomes = []
    for f in sorted(glob.glob(os.path.join(AW, "coevo_groups*_M-6*.json"))):
        d = json.load(open(f))
        genomes += [[(x[0], x[1]) for x in p["groups"]] for p in d["parties"]]
    return guide, genomes


def _draw(rng, guide, genomes):
    import _coevo_groups as C
    if rng.random() < 0.5:
        return list(rng.choice(guide)), "g"
    return C.instantiate(rng.choice(genomes), rng), "c"


def worker(w):
    import pokenavi_engine as E
    from simulator.simulate import get_loader
    from simulator.pokemon import build_from_spec, parse_pokemon_spec
    from simulator.learned_selection import learned_select_party
    L = get_loader()
    guide, genomes = _pools()
    per_w = (TARGET + W - 1) // W
    nchunks = (per_w + CHUNK - 1) // CHUNK
    sd = os.path.join(OUT, "shards")
    prog = os.path.join(OUT, f"progress_w{w}.txt")
    for c in range(nchunks):
        path = os.path.join(sd, f"w{w}_c{c:05d}.npz")
        if os.path.exists(path):
            continue
        if os.path.exists(os.path.join(OUT, "STOP")):
            return
        t0 = time.time()
        rows = {k: [] for k in ("X", "Y", "Q", "PI", "M", "G", "T", "NT", "ME", "TEST")}
        games = draws = fails = 0
        src = {"gg": 0, "cg": 0, "cc": 0}
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
                s1 = learned_select_party(P1, P2, L, n=3, temperature=SEL_TEMP)
                s2 = learned_select_party(P2, P1, L, n=3, temperature=SEL_TEMP)
                ia = [next(i for i, q in enumerate(P1) if q is p) for p in s1]
                ib = [next(i for i, q in enumerate(P2) if q is p) for p in s2]
                r, recs, _ = E.mcts_3v3_trace(list(pa), ia, list(pb), ib, seed, SIMS, SEASON, "", 0, "")
            except Exception as e:
                fails += 1
                print(f"[w{w}] 失敗 seed={seed}: {e!r}", flush=True)
                continue
            games += 1
            src["".join(sorted(ka + kb))] += 1
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
        arr = {
            "X": np.array(rows["X"], np.float32).reshape(-1, 1037),
            "Y": np.array(rows["Y"], np.float32), "Q": np.array(rows["Q"], np.float32),
            "PI": np.array(rows["PI"], np.float32).reshape(-1, 12), "M": np.array(rows["M"], np.uint8).reshape(-1, 12),
            "G": np.array(rows["G"], np.int64), "T": np.array(rows["T"], np.int16), "NT": np.array(rows["NT"], np.int16),
            "ME": np.array(rows["ME"], np.int8), "TEST": np.array(rows["TEST"], np.int8),
            "META": np.array([games, draws, fails, src["gg"], src["cg"], src["cc"]], np.int64),
        }
        tmp = path + ".tmp.npz"
        np.savez_compressed(tmp, **arr)
        os.replace(tmp, path)
        with open(prog, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} c={c} games={games} draws={draws} fails={fails} "
                    f"samples={len(rows['Y'])} {time.time()-t0:.0f}s\n")


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "shards"), exist_ok=True)
    for f in glob.glob(os.path.join(OUT, "shards", "*.tmp.npz")):
        os.remove(f)
    print(f"開始 {time.strftime('%Y-%m-%d %H:%M:%S')} W={W} TARGET={TARGET} CHUNK={CHUNK} PER_GAME={PER_GAME} "
          f"SIMS={SIMS} SEL_TEMP={SEL_TEMP} OUT={OUT}", flush=True)
    ps = [mp.get_context("spawn").Process(target=worker, args=(w,)) for w in range(W)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print(f"終了 {time.strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
