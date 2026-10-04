"""パーティ診断の全体有利度の事前計算（MCTS@64・2026-10-02）。途中保存・再開・停止ファイルつき。
対象: 参照分布 ref（相手集団と同じ生成器 _guide_opps で別シード SEED の NP 党）と提案キャッシュ suggest_cache.json の全提案パーティ
（各キーの1位→2位…の順。ref と1位を交互に先に回す）。1党＝相手 guide_pool の先頭 ADV_OPPS 党×ADV_K 戦を MC_NC 個に分けて回す
（_diagnose.mcts_adv と同じ分け方・シード）。
出力: 結果の行 OUT/res.jsonl（再開用）・diag_adv_m6.json（党ごとの adv/se。サーバが読み直す）・diag_ref_m6.json（ref の adv の昇順。MIN_REF 党以上で書く）。
止める: touch OUT/STOP（走っている分を書いてから抜ける）。再開: 同じコマンドをもう一度。
使い方: POOL_SEASON=M-6 USAGE_SEASON=M-6 ENGINE=rust venv/bin/python _diag_ref.py   env: NP(300) SEED(1) PROCS(8) OUT(_local/ai_work/diag_mcts)
"""
import json
import multiprocessing as mp
import os
import random
import time

import _diagnose as DG
import _select_guide as SG

SEASON = os.environ.get("POOL_SEASON", "M-6")
OUT = os.environ.get("OUT") or os.path.join(DG._DIR, "..", "_local", "ai_work", "diag_mcts")
MIN_REF = 30


def ref_parties(np_, seed):
    import _guide_opps as GO
    GO.C.load()
    rng = random.Random(seed)
    out = []
    while len(out) < np_:
        specs = GO.C.instantiate(GO.C.gen_party(rng), rng)
        if GO.C.plausible(specs):
            out.append(specs)
    return out


def cache_parties():
    cache = json.load(open(os.path.join(DG._DIR, "suggest_cache.json"), encoding="utf-8"))
    ranks = {}
    for v in cache.values():
        for ri, r in enumerate(v["results"]):
            ranks.setdefault(ri, []).append(r["specs"])
    return [ranks[ri] for ri in sorted(ranks)]


def _dump(path, obj):
    tmp = path + ".tmp"
    json.dump(obj, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
    os.replace(tmp, path)


def main():
    np_, seed = int(os.environ.get("NP", "300")), int(os.environ.get("SEED", "1"))
    os.makedirs(OUT, exist_ok=True)
    res_path, stop = os.path.join(OUT, "res.jsonl"), os.path.join(OUT, "STOP")
    ref = ref_parties(np_, seed)
    by_rank = cache_parties()
    order, seen = [], set()

    def add(kind, sp):
        k = DG.party_key(sp)
        if k not in seen:
            seen.add(k)
            order.append((kind, sp))

    for i in range(max(len(ref), len(by_rank[0]))):
        if i < len(ref):
            add("ref", ref[i])
        if i < len(by_rank[0]):
            add("cache", by_rank[0][i])
    for rk in by_rank[1:]:
        for sp in rk:
            add("cache", sp)
    opps = SG.load_pool()[:DG.ADV_OPPS]
    got = {}
    if os.path.exists(res_path):
        for line in open(res_path, encoding="utf-8"):
            try:
                k, i, ws = json.loads(line)
            except ValueError:
                continue
            got.setdefault(k, {})[i] = ws
    kind_of = {DG.party_key(sp): kind for kind, sp in order}
    jobs = []
    for kind, sp in order:
        k = DG.party_key(sp)
        for i, j in enumerate(DG.mchunk_jobs(sp, opps, SEASON, DG.ADV_K)):
            if i not in got.get(k, {}):
                jobs.append(((k, i), j))
    total_p = len(order)

    def write():
        adv, refv = {}, []
        for k, ch in got.items():
            if len(ch) < DG.MC_NC:
                continue
            ws = [w for c in ch.values() for w in c if w is not None]
            m, se = DG.mean_se(ws)
            adv[k] = {"adv": round(m, 4), "se": round(se, 4), "n_opp": len(ws), "k": DG.ADV_K, "sims": DG.SIMS, "kind": kind_of.get(k, "?")}
            if kind_of.get(k) == "ref":
                refv.append(round(m, 4))
        _dump(DG.ADV_FILE, {"season": SEASON, "sims": DG.SIMS, "n_opp": len(opps), "k": DG.ADV_K, "adv": adv})
        if len(refv) >= MIN_REF:
            _dump(DG.REF_FILE, {"season": SEASON, "seed": seed, "method": f"mcts{DG.SIMS}", "n_opp": len(opps), "k": DG.ADV_K,
                                "n_target": len(ref), "adv": sorted(refv)})
        return len(adv), len(refv)

    print(f"党 {total_p}（ref {len(ref)}・cache {total_p - len(ref)}） 残りの塊 {len(jobs)}/{total_p * DG.MC_NC}", flush=True)
    if os.path.exists(stop):
        print("STOP があるので抜ける（消してから再実行）", flush=True)
        return
    t0, n_done = time.time(), 0
    with mp.get_context("fork").Pool(int(os.environ.get("PROCS", "8"))) as pool, open(res_path, "a", encoding="utf-8") as f:
        for (k, i), rows in pool.imap_unordered(_job, jobs, chunksize=1):
            got.setdefault(k, {})[i] = rows
            f.write(json.dumps([k, i, rows], ensure_ascii=False) + "\n")
            f.flush()
            n_done += 1
            if len(got[k]) == DG.MC_NC:
                na, nr = write()
                el = time.time() - t0
                print(f"{time.strftime('%H:%M:%S')} 党 {na}/{total_p}（ref {nr}） 塊 {n_done}/{len(jobs)} "
                      f"残り約 {el / n_done * (len(jobs) - n_done) / 3600:.1f}h", flush=True)
            if os.path.exists(stop):
                pool.terminate()
                break
    na, nr = write()
    print(f"終了 党 {na}/{total_p}（ref {nr}） {time.time() - t0:.0f}s", flush=True)


def _job(a):
    key, j = a
    return key, [r[1] if r else None for r in DG.mrows_at(j)]


if __name__ == "__main__":
    main()
