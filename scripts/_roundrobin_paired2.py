"""2戦目をペア方式で実施し、既存f1_cacheの各カードに記録を追記（n=2に）。
2戦目はP1/P2を1戦目と入替（両サイド均等）＋別シードで別の試合。両視点共有で計算量は半分のまま。
各subjectの全ペア完了時に、その既存ファイルを読んで2戦目を append→stats再計算→上書き保存。
env F1_MCTS_SIMS（本番=800）。引数: LIMIT(先頭何構築で試すか, 既定=全件)。
"""
import os, sys, json, time, zlib
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
from feature1 import play_and_record_both
from simulator.env import load_registered_parties, spec_to_string

SEASON = "M-2"
SIMS = int(os.environ.get("F1_MCTS_SIMS", "800"))
CACHE = os.environ.get("F1_CACHE_DIR", os.path.join(os.path.dirname(__file__), "f1_cache"))
PARTIES = []

def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)

TAG = os.environ.get("RR_SEEDTAG", "g2")             # シード識別。パスごとに変えて別試合に
OPP_FIRST = os.environ.get("RR_FIRST_OPPOSITE", "1") == "1"  # 1=1戦目と逆サイドをP1 / 0=同サイド

def _seed2(li, lj):
    a, b = sorted([li, lj])
    return zlib.crc32(f"{a}|{b}|{TAG}".encode("utf-8")) % (1 << 31)

def _job(args):
    first, second, seed = args
    recF, recS = play_and_record_both(PARTIES[first][1], PARTIES[second][1],
                                      season=SEASON, seed=seed, mcts_sims=SIMS)
    return first, second, recF, recS

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    _f1._ensure_loaded(SEASON, 8)
    L = _f1._W["loader"]
    parties = load_registered_parties(L, complete_only=True, season=SEASON)
    if limit:
        parties = parties[:limit]
    global PARTIES
    PARTIES = [(p.label, [spec_to_string(s) for s in p.specs]) for p in parties]
    N = len(PARTIES)
    L2I = {PARTIES[k][0]: k for k in range(N)}

    pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            base = i if (i + j) % 2 == 0 else j             # 基準のP1（1戦目）
            first = (j if base == i else i) if OPP_FIRST else base   # 逆サイド or 同サイド
            second = j if first == i else i
            pairs.append((first, second, _seed2(PARTIES[i][0], PARTIES[j][0])))
    total = len(pairs)
    print(f"2戦目ペア総当たり: {N}構築 / {total}ペア SIMS={SIMS}", flush=True)

    acc = {k: {} for k in range(N)}       # subject_idx -> {opp_idx: rec2}
    remaining = {k: N - 1 for k in range(N)}
    written = 0; done = 0; t0 = time.time()
    workers = max(1, (os.cpu_count() or 2) - 2)
    ctx = mp.get_context("fork")

    def flush(subj_idx):
        nonlocal written
        label = PARTIES[subj_idx][0]
        path = os.path.join(CACHE, _safe(label) + ".json")
        d = json.load(open(path, encoding="utf-8"))
        recs2 = acc[subj_idx]
        for c in d["cards"]:
            oi = L2I.get(c["label"])
            r2 = recs2.get(oi) if oi is not None else None
            if r2 is None:
                continue
            c["records"].append(r2)
            recs = c["records"]
            c["wins"] = sum(1 for r in recs if r["result"] == 1)
            c["losses"] = sum(1 for r in recs if r["result"] == 2)
            c["draws"] = sum(1 for r in recs if r["result"] == 0)
            c["n"] = len(recs)
            c["win_rate"] = c["wins"] / max(1, c["n"])
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        del acc[subj_idx]
        written += 1

    def emit(subj_idx, opp_idx, rec):
        acc[subj_idx][opp_idx] = rec
        remaining[subj_idx] -= 1
        if remaining[subj_idx] == 0:
            flush(subj_idx)

    with ctx.Pool(workers) as pool:
        for first, second, recF, recS in pool.imap_unordered(_job, pairs, chunksize=4):
            emit(first, second, recF)
            emit(second, first, recS)
            done += 1
            if done % 200 == 0 or done == total:
                el = time.time() - t0; rate = done / max(1e-9, el)
                eta = (total - done) / max(1e-9, rate)
                print(f"  {done}/{total}ペア  追記済subject {written}/{N}  {el/60:.1f}min  ETA {eta/60:.0f}min", flush=True)
    print(f"完了: {written}構築に2戦目を追記  {(time.time()-t0)/60:.1f}min", flush=True)

if __name__ == "__main__":
    main()
