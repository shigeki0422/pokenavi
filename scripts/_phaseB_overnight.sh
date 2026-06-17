#!/bin/bash
# Phase B 一晩ジョブ：Phase A(opp_match)完了待ち → 本番ネット退避 → 初めから学習(MCTS自己対戦) →
# 本番ネット復元 → 新ネット(d3@k2+畳み込み) vs 現行(d2@k4) 評価。全て自動・本番ネットは保護。
set -u
cd /Users/shigeki/work/pokenavi/scripts
PY=./venv/bin/python
LOG=/tmp/phaseB.log
log(){ echo "$(date '+%m/%d %H:%M:%S') $*" | tee -a "$LOG"; }

log "=== Phase B 起動。Phase A(opp_match)の完了を待機 ==="
while pgrep -f _opp_match.py >/dev/null; do sleep 60; done
log "Phase A 完了を検知（コア解放）"

cp az_net_np.json az_net_prodbaseline.json
log "本番ネットを az_net_prodbaseline.json に退避（保護）"

log "STEP1 初めから学習 開始（fresh, 14iters x 2000games x 32sims, eps_sel=0.6, 2メガ回避, arch256x128）"
OMP_NUM_THREADS=1 $PY train_az2.py 14 2000 32 256 128 1 > /tmp/phaseB_train.log 2>&1
TRAIN_RC=$?
log "STEP1 学習終了 (rc=$TRAIN_RC)"

cp az_net_np.json az_net_scratch.json
cp az_net_prodbaseline.json az_net_np.json
log "学習ネット→az_net_scratch.json / 本番ネット復元（az_net_np.json）"

if [ "$TRAIN_RC" -ne 0 ] || ! grep -q "保存:" /tmp/phaseB_train.log; then
  log "!! 学習が正常終了していない。評価をスキップ。/tmp/phaseB_train.log を確認"
  log "=== Phase B 異常終了 ==="
  exit 1
fi

log "STEP2 評価対局 開始（新 vs 現行 400戦）"
OMP_NUM_THREADS=1 $PY _net_vs_net.py 400 12 az_net_scratch.json az_net_prodbaseline.json > /tmp/phaseB_eval.log 2>&1
log "STEP2 評価完了"
log "=== Phase B 完了 ==="
echo "---- 学習サマリ（末尾） ----" | tee -a "$LOG"; tail -4 /tmp/phaseB_train.log | tee -a "$LOG"
echo "---- 評価結果 ----" | tee -a "$LOG"; tail -3 /tmp/phaseB_eval.log | tee -a "$LOG"
