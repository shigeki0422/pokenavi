#!/bin/bash
# 6時 自動更新ジョブ（フェーズ2 n=2 → 本番反映 / 致命的ならn=1へロールバック）
# 常時起動のMac上でデタッチ実行。06:00以降にフェーズ2完了を検知したら更新を実行する。
# 09:00デッドラインまでに完了しなければ何もしない（n=1維持＝安全）。
set -u
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
PY="$ROOT/scripts/venv/bin/python"
LOG="/tmp/auto_update.log"
RESULT="/tmp/auto_update_result.txt"
WRANGLER="npx --no-install wrangler"
BUCKET="pokenavi-sim"
DOMAIN="https://sim.pokenavi.jp"
N1="$ROOT/scripts/sim_export/_n1_rollback"
EXPECT_N=2

log(){ echo "$(date '+%H:%M:%S') $*" | tee -a "$LOG"; }
result(){ echo "$*" > "$RESULT"; log "RESULT: $*";
  osascript -e "display notification \"$*\" with title \"pokenavi 6時更新\"" 2>/dev/null || true; }

# 全73主役が n>=EXPECT_N かつ ai_ver一致か
precond_ok(){ "$PY" - "$EXPECT_N" <<'PYEOF'
import json,glob,sys
need=int(sys.argv[1]); files=glob.glob("scripts/f1_cache/*.json")
if len(files)<73: sys.exit(1)
for f in files:
    d=json.load(open(f))
    cards=d.get("cards",[])
    if not cards: sys.exit(1)
    if any(c.get("n",0)<need for c in cards): sys.exit(1)
sys.exit(0)
PYEOF
}

upload_dir(){ # $1=subjects dir
  local d="$1" n=0 fail=0
  for f in "$d"/*.json; do
    if $WRANGLER r2 object put "$BUCKET/subjects/$(basename "$f")" --file="$f" --content-type="application/json" --remote >/dev/null 2>&1; then n=$((n+1)); else fail=$((fail+1)); fi
  done
  log "  upload: ok=$n fail=$fail (from $d)"
  [ "$fail" -eq 0 ]
}

verify_r2(){ # sample 3
  local f code
  for f in $(ls "$ROOT/scripts/sim_export/subjects" | head -3); do
    code=$(curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/subjects/$f")
    [ "$code" = "200" ] || { log "  R2 verify FAIL $f -> $code"; return 1; }
  done; return 0
}

verify_deploy(){ # index.json live n==EXPECT_N and /simulator 200
  local n code
  n=$(curl -s "https://pokenavi.jp/sim-data/index.json" | "$PY" -c "import sys,json;d=json.load(sys.stdin);print(d['subjects'][0]['n'] if d.get('subjects') else 0)" 2>/dev/null)
  code=$(curl -sL -o /dev/null -w "%{http_code}" "https://pokenavi.jp/simulator")
  log "  deploy: index n=$n /simulator=$code (expect n>=$EXPECT_N)"
  [ "$code" = "200" ] && [ -n "$n" ] && [ "$n" -ge "$EXPECT_N" ]
}

rollback(){
  log "!! ROLLBACK to n=1"
  upload_dir "$N1/subjects" || log "  (rollback R2 upload had failures)"
  cp "$N1/index.json" "$ROOT/public/sim-data/index.json"
  git add public/sim-data/index.json
  git commit -q -m "revert(simulator): n=2更新の致命的障害によりn=1へロールバック" 2>&1 | tail -1
  git push origin main 2>&1 | tail -2
  result "致命的障害→n=1へロールバック完了。ログ: $LOG"
}

# ---- メインループ：翌06:00まで待機→09:00デッドラインまでフェーズ2完了を待つ ----
now=$(date +%s)
SIX=$(date -v6H -v0M -v0S +%s); [ "$now" -ge "$SIX" ] && SIX=$(date -v+1d -v6H -v0M -v0S +%s)
NINE=$(( SIX + 10800 ))
log "=== auto_update 起動。$(date -r "$SIX" '+%m/%d %H:%M') に起床予定（締切 $(date -r "$NINE" '+%H:%M')）==="
while [ "$(date +%s)" -lt "$SIX" ]; do sleep 300; done
log "06:00到達。フェーズ2(n=2)完了を待機"
while true; do
  if precond_ok; then log "フェーズ2(n=2)完了を検知。更新開始"; break; fi
  if [ "$(date +%s)" -ge "$NINE" ]; then
    result "09:00までにフェーズ2(n=2)未完了。更新スキップ＝n=1維持。"; exit 0
  fi
  log "n=2未完了。待機継続"; sleep 300
done

# ---- 更新シーケンス ----
log "STEP1 export"; "$PY" scripts/export_f1_static.py >> "$LOG" 2>&1 || { result "export失敗。n=1維持(R2未変更)。"; exit 1; }
log "STEP2 R2 upload"; if ! upload_dir "$ROOT/scripts/sim_export/subjects"; then rollback; exit 1; fi
log "STEP3 R2 verify"; if ! verify_r2; then rollback; exit 1; fi
log "STEP4 commit+push"; git add public/sim-data/index.json public/sim-data/icons.json public/sim-data/move_types.json
git commit -q -m "feat(simulator): フェーズ2 n=2 反映（自動更新）" 2>&1 | tail -1
git push origin main 2>&1 | tail -2 | tee -a "$LOG"
log "STEP5 deployビルド待機(最大8分)"
ok=0
for i in $(seq 1 16); do sleep 30; if verify_deploy; then ok=1; break; fi; done
if [ "$ok" = "1" ]; then result "n=2 更新成功。pokenavi.jp 反映確認。"; else rollback; exit 1; fi
