#!/bin/bash
# フェーズ3(n=5)完了を検知して本番反映する自動ジョブ。
# 時間ゲートなし＝precond(全73がn>=5)成立で即実行。致命的障害ならn=2へロールバック。
set -u
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
PY="$ROOT/scripts/venv/bin/python"
LOG="/tmp/auto_update_n5.log"
RESULT="/tmp/auto_update_n5_result.txt"
WRANGLER="npx --no-install wrangler"
BUCKET="pokenavi-sim"
DOMAIN="https://sim.pokenavi.jp"
RB="$ROOT/scripts/sim_export/_n2_rollback"   # ロールバック先=現行n=2
EXPECT_N=5
DEADLINE=$(( $(date +%s) + 57600 ))          # 16時間後に諦める（フェーズ3が死んだ場合の保険）

log(){ echo "$(date '+%m/%d %H:%M:%S') $*" | tee -a "$LOG"; }
result(){ echo "$*" > "$RESULT"; log "RESULT: $*";
  osascript -e "display notification \"$*\" with title \"pokenavi n=5更新\"" 2>/dev/null || true; }

precond_ok(){ "$PY" - "$EXPECT_N" <<'PYEOF'
import json,glob,sys
need=int(sys.argv[1]); files=glob.glob("scripts/f1_cache/*.json")
if len(files)<73: sys.exit(1)
for f in files:
    d=json.load(open(f)); cards=d.get("cards",[])
    if not cards or any(c.get("n",0)<need for c in cards): sys.exit(1)
sys.exit(0)
PYEOF
}

upload_dir(){ local d="$1" n=0 fail=0
  for f in "$d"/*.json; do
    if $WRANGLER r2 object put "$BUCKET/subjects/$(basename "$f")" --file="$f" --content-type="application/json" --remote >/dev/null 2>&1; then n=$((n+1)); else fail=$((fail+1)); fi
  done
  log "  upload: ok=$n fail=$fail (from $d)"; [ "$fail" -eq 0 ]; }

verify_r2(){ local f code
  for f in $(ls "$ROOT/scripts/sim_export/subjects" | head -3); do
    code=$(curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/subjects/$f")
    [ "$code" = "200" ] || { log "  R2 verify FAIL $f -> $code"; return 1; }
  done; return 0; }

verify_deploy(){ local n code
  n=$(curl -s "https://pokenavi.jp/sim-data/index.json" | "$PY" -c "import sys,json;d=json.load(sys.stdin);print(d['subjects'][0]['n'] if d.get('subjects') else 0)" 2>/dev/null)
  code=$(curl -sL -o /dev/null -w "%{http_code}" "https://pokenavi.jp/simulator")
  log "  deploy: index n=$n /simulator=$code (expect n>=$EXPECT_N)"
  [ "$code" = "200" ] && [ -n "$n" ] && [ "$n" -ge "$EXPECT_N" ]; }

rollback(){ log "!! ROLLBACK to n=2"
  upload_dir "$RB/subjects" || log "  (rollback R2 upload had failures)"
  cp "$RB/index.json" "$ROOT/public/sim-data/index.json"
  git add public/sim-data/index.json
  git commit -q -m "revert(simulator): n=5更新の致命的障害によりn=2へロールバック" 2>&1 | tail -1
  git push origin main 2>&1 | tail -2
  result "n=5更新が致命的障害→n=2へロールバック完了。ログ: $LOG"; }

log "=== auto_update_n5 起動。フェーズ3(n=5)完了を待機（締切 $(date -r "$DEADLINE" '+%m/%d %H:%M')）==="
while true; do
  if precond_ok; then log "フェーズ3(n=5)完了を検知。更新開始"; break; fi
  if [ "$(date +%s)" -ge "$DEADLINE" ]; then result "16時間以内にn=5未完了。更新スキップ＝n=2維持。"; exit 0; fi
  sleep 300
done

log "STEP1 export"; "$PY" scripts/export_f1_static.py >> "$LOG" 2>&1 || { result "export失敗。n=2維持(R2未変更)。"; exit 1; }
log "STEP2 R2 upload"; if ! upload_dir "$ROOT/scripts/sim_export/subjects"; then rollback; exit 1; fi
log "STEP3 R2 verify"; if ! verify_r2; then rollback; exit 1; fi
log "STEP4 commit+push"; git add public/sim-data/index.json public/sim-data/icons.json public/sim-data/move_types.json
git commit -q -m "feat(simulator): フェーズ3 n=5 反映（自動更新）" 2>&1 | tail -1
git push origin main 2>&1 | tail -2 | tee -a "$LOG"
log "STEP5 deployビルド待機(最大8分)"
ok=0
for i in $(seq 1 16); do sleep 30; if verify_deploy; then ok=1; break; fi; done
if [ "$ok" = "1" ]; then result "n=5 更新成功。pokenavi.jp 反映確認。"; else rollback; exit 1; fi
