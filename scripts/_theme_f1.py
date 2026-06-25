"""テーマ97構築を「主役」かつ「対戦相手」として総当たり（各カード1戦・MCTS@400）。
feature1.play_and_record でターン毎リプレイを捕捉し、上位環境シミュレーションと同形式の
f1_cacheファイル（主役ごと {subject_label, subject_party, cards[records...], ai_ver}）を出力。
全(主役×相手)を1プールで並列実行（フル12コア活用）。出力→ scripts/theme_f1_cache/。
"""
import os, sys, json, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
import multiprocessing as mp
import feature1 as F1

SEASON = "M-3"
SIMS = int(os.environ.get("MCTS_SIMS", "400"))
N = int(os.environ.get("N_PER_CARD", "1"))
NPROC = int(os.environ.get("NPROC", "12"))
AI_VER = f"mcts{SIMS}-M3"
POOL_FILE = os.environ.get("POOL_FILE", "func1_themed_M-3.json")
OUT = os.path.join(os.path.dirname(__file__), os.environ.get("THEME_OUT", "theme_f1_cache"))

def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)

def main():
    parties = json.load(open(POOL_FILE, encoding="utf-8"))["parties"]
    labels = []
    for k, p in enumerate(parties):                 # ラベルは一意化（重複テーマ名に連番）
        base = p.get("theme") or ("自然体:" + "・".join((p.get("names") or [sp.split("@")[0].split(":")[0] for sp in p["specs"]])[:2]))
        lab = base; s = 1
        while lab in labels: s += 1; lab = f"{base} ({s})"
        labels.append(lab)
    specs = [p["specs"] for p in parties]
    n = len(parties)
    os.makedirs(OUT, exist_ok=True)
    F1._ensure_loaded(SEASON, 8)                     # 親で net ロード→fork子が継承
    # 既存キャッシュ（前回までの記録）を読み込み、(si,cj)→records へ。不足分(bi)だけ追加実行＝再開
    lab2idx = {lab: i for i, lab in enumerate(labels)}
    recs = {(si, cj): [] for si in range(n) for cj in range(n) if cj != si}
    for si in range(n):
        fp = os.path.join(OUT, _safe(labels[si]) + ".json")
        if not os.path.exists(fp): continue
        d = json.load(open(fp, encoding="utf-8"))
        for c in d.get("cards", []):
            cj = lab2idx.get(c["label"])
            if cj is not None and cj != si:
                recs[(si, cj)] = list(c.get("records", []))
    jobs = []
    for si in range(n):
        for cj in range(n):
            if cj == si: continue
            for bi in range(len(recs[(si, cj)]), N):   # 既存戦は温存、不足biのみ
                seed = F1._battle_seed(labels[cj], bi) ^ (si * 2654435761 & 0xffffffff)
                jobs.append(((si, cj, bi), specs[si], specs[cj], SEASON, 8, 0.6, seed, SIMS))
    print(f"テーマ{n} / 目標{N}戦per カード / MCTS@{SIMS} ×{NPROC} / 追加{len(jobs)}戦", flush=True)
    t0 = time.time(); done = 0
    ctx = mp.get_context("fork")
    with ctx.Pool(NPROC) as pool:
        for (si, cj, bi), rec in pool.imap_unordered(F1._worker, jobs, chunksize=4):
            recs[(si, cj)].append(rec); done += 1
            if done % 300 == 0:
                el = time.time() - t0
                print(f"  {done}/{len(jobs)} {el:.0f}s eta {el/done*(len(jobs)-done):.0f}s", flush=True)
    # 主役ごとに f1_cache 形式で保存
    for si in range(n):
        cards = []
        for cj in range(n):
            if cj == si: continue
            cards.append(F1._card_summary(labels[cj], specs[cj], recs[(si, cj)], len(recs[(si, cj)])))
        out = {"subject_label": labels[si], "subject_party": specs[si], "cards": cards, "ai_ver": AI_VER}
        json.dump(out, open(os.path.join(OUT, _safe(labels[si]) + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, separators=(",", ":"))
    print(f"完了 {time.time()-t0:.0f}s → {OUT}（{n}主役）", flush=True)

if __name__ == "__main__":
    main()
