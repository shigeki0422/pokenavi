"""ペア単位の総当たり（重複排除）。未順序ペア(i<j)を1回だけ対戦し、
A対B記録とB対A記録(視点反転)を同時に得る＝計算量ほぼ半減。
P1/P2はペアごとに交互割当で先手有利の偏りを相殺。
各subjectの全カード完成時に f1_cache/ へ逐次書き出し（メモリ抑制）。
env F1_MCTS_SIMS で sims（本番=800）。引数: LIMIT(先頭何構築で試すか, 既定=全件)。
"""
import os, sys, json, time, zlib
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
from feature1 import play_and_record_both, _card_summary
from simulator.env import load_registered_parties, spec_to_string

SEASON = "M-2"
AI_VER = "mcts-guardq800-1"
SIMS = int(os.environ.get("F1_MCTS_SIMS", "800"))
CACHE = os.environ.get("F1_CACHE_DIR", os.path.join(os.path.dirname(__file__), "f1_cache"))
PARTIES = []   # [(label, specs6)]  fork継承でワーカー参照

def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)

def _seed(li, lj):
    a, b = sorted([li, lj])
    return zlib.crc32(f"{a}|{b}".encode("utf-8")) % (1 << 31)

def _job(args):
    i, j, first, second, seed = args
    recF, recS = play_and_record_both(PARTIES[first][1], PARTIES[second][1],
                                      season=SEASON, seed=seed, mcts_sims=SIMS)
    return first, second, recF, recS   # recF=firstのfirst視点, recS=secondの視点

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
    os.makedirs(CACHE, exist_ok=True)

    pairs = []
    for i in range(N):
        for j in range(i + 1, N):
            first, second = (i, j) if (i + j) % 2 == 0 else (j, i)   # P1交互で偏り相殺
            pairs.append((i, j, first, second, _seed(PARTIES[i][0], PARTIES[j][0])))
    total = len(pairs)
    print(f"ペア総当たり: {N}構築 / {total}ペア (=2倍展開で{total*2}カード) SIMS={SIMS}", flush=True)

    acc = {k: {} for k in range(N)}          # subject_idx -> {opp_idx: card}
    remaining = {k: N - 1 for k in range(N)}
    written = 0; done = 0; t0 = time.time()
    workers = max(1, (os.cpu_count() or 2) - 2)
    ctx = mp.get_context("fork")

    def emit(subj_idx, opp_idx, rec):
        opp_label, opp_specs = PARTIES[opp_idx]
        acc[subj_idx][opp_idx] = _card_summary(opp_label, opp_specs, [rec], 1)
        remaining[subj_idx] -= 1
        if remaining[subj_idx] == 0:
            label, specs = PARTIES[subj_idx]
            cards = [acc[subj_idx][o] for o in sorted(acc[subj_idx])]
            with open(os.path.join(CACHE, _safe(label) + ".json"), "w", encoding="utf-8") as f:
                json.dump({"subject_label": label, "subject_party": specs,
                           "ai_ver": AI_VER, "cards": cards}, f, ensure_ascii=False)
            del acc[subj_idx]
            return True
        return False

    with ctx.Pool(workers) as pool:
        for first, second, recF, recS in pool.imap_unordered(_job, pairs, chunksize=4):
            if emit(first, second, recF):
                written += 1
            if emit(second, first, recS):
                written += 1
            done += 1
            if done % 200 == 0 or done == total:
                el = time.time() - t0; rate = done / max(1e-9, el)
                eta = (total - done) / max(1e-9, rate)
                print(f"  {done}/{total}ペア  書込済subject {written}/{N}  "
                      f"{el/60:.1f}min  ETA {eta/60:.0f}min", flush=True)
    print(f"完了: {written}構築を f1_cache/ に書き出し  {(time.time()-t0)/60:.1f}min", flush=True)

if __name__ == "__main__":
    main()
