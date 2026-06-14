"""全ランカーを順次 N 戦で事前計算（サーバHTTP経由・逐次）。
リリース優先で N=3。後で N=10/20 に増やすと、同一AIバージョンの既存戦を再利用し不足分だけ追記する
（サーバ側 run_roundrobin の existing 再利用＝段階拡張）。重い計算はサーバ側、本スクリプトはHTTP制御のみ。
"""
import json
import os
import re
import time
import urllib.request

BASE = "http://localhost:8888"
N = int(os.environ.get("PRECOMPUTE_N", "3"))   # 1カードの対戦数。env PRECOMPUTE_N で段階実行（1→3）
AI_VER = "k4-megaeval-1mega-d2"  # sim_server.AI_VER と一致させる（再開判定用）
BUDGET_SEC = 48 * 3600
RESERVE_SEC = 20 * 60            # N=3は1体〜15分想定。20分未満なら次は開始しない
CACHE_DIR = os.path.join(os.path.dirname(__file__), "f1_cache")
DEADLINE = time.time() + BUDGET_SEC


def get(path):
    with urllib.request.urlopen(BASE + path, timeout=30) as r:
        return json.load(r)


def post(path, body):
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def num(label):
    m = re.search(r"#(\d+)", label)
    return int(m.group(1)) if m else 9999


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def _safe(name):
    return "".join(c if c.isalnum() else "_" for c in name)


def already_done(label, expected):
    """同一AIバージョンで、全カード(expected枚)が揃い各N戦以上ならTrue（再開時のスキップ用）。
    カード欠落（データ修正でカードを削除した等）も未完了として再訪させる。"""
    path = os.path.join(CACHE_DIR, _safe(label) + ".json")
    if not os.path.isfile(path):
        return False
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
    except Exception:
        return False
    cards = d.get("cards") or []
    return (d.get("ai_ver") == AI_VER and len(cards) >= expected
            and all(c.get("n", 0) >= N for c in cards))


def main():
    rankers = {r["label"]: r["party"] for r in get("/api/f1/rankers")}
    targets = sorted(rankers.keys(), key=num)
    log(f"targets: {len(targets)} 体  N={N}  AI_VER={AI_VER}")
    done = 0
    for label in targets:
        party = rankers.get(label)
        if not party:
            log("skip (no party):", label)
            continue
        if already_done(label, len(targets) - 1):
            log("skip (済: 同AI版で全%dカードN>=%d):" % (len(targets) - 1, N), label)
            continue
        remain = DEADLINE - time.time()
        if remain < RESERVE_SEC:
            log(f"STOP: remaining {int(remain/60)}min < reserve; not starting", label)
            break
        res = post("/api/f1/analyze",
                   {"p1": party, "n": N, "season": "M-2", "exclude_label": label})
        aid = res["analysis_id"]
        log("START", label, aid, f"(remaining {int(remain/60)}min)")
        while True:
            if time.time() > DEADLINE:
                log("HARD DEADLINE during", label)
                return
            try:
                p = get(f"/api/f1/progress/{aid}")
                if not p.get("running"):
                    log("DONE", label, "done", p.get("done"), "saved", p.get("saved"))
                    break
            except Exception as e:
                log("poll error", e)
            time.sleep(15)
        done += 1
    log(f"ALL DONE: computed {done} subjects this run (N={N})")


if __name__ == "__main__":
    main()
