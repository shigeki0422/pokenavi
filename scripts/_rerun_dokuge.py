"""どくげしょうキラフロルが物理技で気絶した影響試合だけを、修正後エンジンで再戦し差し替える。
未発火試合は触らない。影響ペアの両subjectの該当game_idxを置換し、そのカードのstatsを再計算。
env DRYRUN=1 で検出件数のみ表示。env F1_MCTS_SIMS（本番=800）。
"""
import os, sys, json, time, re, zlib, sqlite3, glob
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as _f1
from feature1 import play_and_record_both
from simulator.env import load_registered_parties, spec_to_string

SEASON = "M-2"
SIMS = int(os.environ.get("F1_MCTS_SIMS", "800"))
CACHE = os.path.join(os.path.dirname(__file__), "f1_cache")
DB = os.path.join(os.path.dirname(__file__), "pokenavi.db")
DRYRUN = os.environ.get("DRYRUN", "0") == "1"

def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)

def _path(label):
    return os.path.join(CACHE, _safe(label) + ".json")

_MOVECAT = {}
def _load_cat():
    con = sqlite3.connect(DB)
    for n, c in con.execute("SELECT name_jp, category FROM move_master"):
        _MOVECAT[n] = c
    con.close()

_HIT = re.compile(r"の (.+?) → キラフロル に \d+ ?ダメ")

def _game_affected(rec):
    """キラフロルが場で物理(or不明)技により気絶し、相手どくびし<2 の試合か。"""
    prev = {1: True, 2: True}
    for t in rec["turns"]:
        for si, key in ((1, "side1"), (2, "side2")):
            sd = t[key]; ai = sd["active_idx"]
            if ai >= len(sd["party"]):
                continue
            act = sd["party"][ai]
            if "キラフロル" not in act["name"]:
                prev[si] = act["alive"]
                continue
            if prev[si] and not act["alive"]:
                opp = t["side2" if si == 1 else "side1"]
                if opp["toxic_spikes"] < 2:
                    mv = None
                    for ln in (t.get("logs") or []):
                        m = _HIT.search(ln)
                        if m:
                            mv = m.group(1).strip()
                    if _MOVECAT.get(mv) != "special":   # 物理 or 不明は影響扱い（安全側）
                        return True
            prev[si] = act["alive"]
    return False

def detect():
    """affected: {(labelA,labelB sorted): set(game_idx)}"""
    affected = {}
    for f in glob.glob(os.path.join(CACHE, "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        if not any("キラフロル" in s and "どくげしょう" in s for s in d["subject_party"]):
            continue
        subj = d["subject_label"]
        for c in d["cards"]:
            opp = c["label"]
            key = tuple(sorted([subj, opp]))
            for gi, rec in enumerate(c["records"]):
                if _game_affected(rec):
                    affected.setdefault(key, set()).add(gi)
    return affected

PARTIES = {}   # label -> specs6（fork継承）

def _job(args):
    a, b, gi, seed = args
    recF, recS = play_and_record_both(PARTIES[a], PARTIES[b], season=SEASON, seed=seed, mcts_sims=SIMS)
    return a, b, gi, recF, recS

def main():
    _load_cat()
    _f1._ensure_loaded(SEASON, 8)
    L = _f1._W["loader"]
    parties = load_registered_parties(L, complete_only=True, season=SEASON)
    global PARTIES
    PARTIES = {p.label: [spec_to_string(s) for s in p.specs] for p in parties}

    affected = detect()
    n_pairs = len(affected)
    n_games = sum(len(v) for v in affected.values())
    print(f"影響ペア {n_pairs} / 影響試合 {n_games}  SIMS={SIMS}", flush=True)
    if DRYRUN:
        return

    jobs = []
    for (a, b), gis in affected.items():
        for gi in gis:
            seed = zlib.crc32(f"{a}|{b}|fix{gi}".encode("utf-8")) % (1 << 31)
            jobs.append((a, b, gi, seed))

    # file -> opp_label -> {game_idx: rec}
    repl = {}
    def stage(subj, opp, gi, rec):
        repl.setdefault(subj, {}).setdefault(opp, {})[gi] = rec

    workers = max(1, (os.cpu_count() or 2) - 2)
    ctx = mp.get_context("fork")
    done = 0; t0 = time.time()
    with ctx.Pool(workers) as pool:
        for a, b, gi, recF, recS in pool.imap_unordered(_job, jobs, chunksize=2):
            stage(a, b, gi, recF)
            stage(b, a, gi, recS)
            done += 1
            if done % 50 == 0 or done == len(jobs):
                el = time.time() - t0; rate = done / max(1e-9, el)
                eta = (len(jobs) - done) / max(1e-9, rate)
                print(f"  {done}/{len(jobs)}戦  {el/60:.1f}min  ETA {eta/60:.0f}min", flush=True)

    # 適用
    for subj, by_opp in repl.items():
        path = _path(subj)
        d = json.load(open(path, encoding="utf-8"))
        for c in d["cards"]:
            g = by_opp.get(c["label"])
            if not g:
                continue
            for gi, rec in g.items():
                c["records"][gi] = rec
            recs = c["records"]
            c["wins"] = sum(1 for r in recs if r["result"] == 1)
            c["losses"] = sum(1 for r in recs if r["result"] == 2)
            c["draws"] = sum(1 for r in recs if r["result"] == 0)
            c["n"] = len(recs)
            c["win_rate"] = c["wins"] / max(1, c["n"])
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
    print(f"差し替え完了: {len(repl)}ファイル更新  {(time.time()-t0)/60:.1f}min", flush=True)

    # 検証: 残存影響0か
    left = detect()
    print(f"再検出（残存影響）: ペア{len(left)} / 試合{sum(len(v) for v in left.values())}", flush=True)

if __name__ == "__main__":
    main()
