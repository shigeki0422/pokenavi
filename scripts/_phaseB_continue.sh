#!/bin/bash
# Phase B(継続学習)：Phase A完了待ち → 現行ネット退避 → 現行から継続学習(6時打切) →
# 本番ネット復元 → 継続学習ネット vs 現行ネット を同一戦術(d2/k4)で比較。本番ネットは保護。
set -u
cd /Users/shigeki/work/pokenavi/scripts
PY=./venv/bin/python
LOG=/tmp/phaseB.log
log(){ echo "$(date '+%m/%d %H:%M:%S') $*" | tee -a "$LOG"; }

now=$(date +%s); SIX=$(date -v6H -v0M -v0S +%s); [ "$now" -ge "$SIX" ] && SIX=$(date -v+1d -v6H -v0M -v0S +%s)
log "=== Phase B(継続学習) 起動。学習締切=$(date -r "$SIX" '+%m/%d %H:%M'). Phase A待機 ==="
while pgrep -f _opp_match.py >/dev/null; do sleep 60; done
log "Phase A 完了（コア解放）"

cp az_net_np.json az_net_prodbaseline.json
log "現行ネットを az_net_prodbaseline.json に退避（比較基準＋保護）"

log "STEP1 継続学習 開始（fresh=0, 最大100反復・6時で打切, eps0.6, 2メガ回避）"
OMP_NUM_THREADS=1 $PY train_az2.py 100 2000 32 256 128 0 > /tmp/phaseB_train.log 2>&1 &
TPID=$!
while [ "$(date +%s)" -lt "$SIX" ] && kill -0 "$TPID" 2>/dev/null; do sleep 120; done
if kill -0 "$TPID" 2>/dev/null; then
  log "6時到達→学習を打切り"
  kill "$TPID" 2>/dev/null; sleep 3
  pkill -9 -f train_az2.py 2>/dev/null; pkill -9 -f spawn_main 2>/dev/null; sleep 2
fi
log "STEP1 学習終了"

cp az_net_np.json az_net_continued.json
cp az_net_prodbaseline.json az_net_np.json
log "学習ネット→az_net_continued.json / 本番ネット復元（az_net_np.json）"

log "STEP2 評価: 継続学習ネット vs 現行ネット（両者 d2/k4・600戦）"
OMP_NUM_THREADS=1 $PY _net_vs_net.py 600 12 az_net_continued.json az_net_prodbaseline.json 2 4 0 > /tmp/phaseB_eval.log 2>&1
log "STEP2 評価完了"
log "=== Phase B 完了 ==="
echo "--- 学習履歴(末尾) ---" | tee -a "$LOG"; tail -6 /tmp/phaseB_train.log | tee -a "$LOG"
echo "--- 評価結果 ---" | tee -a "$LOG"; tail -3 /tmp/phaseB_eval.log | tee -a "$LOG"
