"""人気軸の提案を事前計算し suggest_cache.json に保存（コールドスタート/新インスタンスでも即時返却）。
フロントと同じ /species 変種（{sp,mega}）で計算するのでキャッシュキーが一致する。
env: PRECOMPUTE_N(人気変種の上位数, 既定30)
"""
import os, json, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("GA_SIMS", "1")
import product3_server as S

N = int(os.environ.get("PRECOMPUTE_N", "30"))
OUT = os.environ.get("PRECOMPUTE_OUT") or S._SCACHE_FILE   # STAGING出力用（既定＝本番ファイル）
SAVE_EVERY = int(os.environ.get("SAVE_EVERY", "5"))   # 途中経過をこの件数ごとに保存（ローカル確認用）
variants = sorted(S.VARIANTS, key=lambda v: v.get("rank", 9999))[:N]
cores = [[]] + [[{"sp": v["sp"], "mega": v["mega"]}] for v in variants]   # おまかせ＋人気変種
S._SCACHE.clear()
t0 = time.time()
for i, c in enumerate(cores):
    S.suggest(c, 100, 5)
    lbl = "おまかせ" if not c else f"{c[0]['sp']}/{c[0]['mega']}"
    print(f"  {i+1}/{len(cores)} {lbl}", flush=True)
    if (i + 1) % SAVE_EVERY == 0:
        json.dump(S._SCACHE, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
json.dump(S._SCACHE, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print(f"{OUT} 保存: {len(S._SCACHE)}件 / {time.time()-t0:.0f}s", flush=True)
