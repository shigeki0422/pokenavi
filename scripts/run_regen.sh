#!/bin/zsh
# 新エンジン(ガード+Q+collapse_mega, AI_VER=mcts-guardq-1)で全データ再生成
set -e
cd /Users/shigeki/work/pokenavi/scripts
PY=venv/bin/python
LOG=/tmp/regen.log
say() { print -r -- "[$(date '+%H:%M:%S')] $*" | tee -a $LOG; }
say "START regen (guardq) — collapse_mega/qselect/downside_guard 既定ON"

# 1) ランクf1_cache 再生成（サーバ経由・新エンジン）
rm -rf f1_cache; mkdir f1_cache
say "STEP1 precompute (ranked, N=2) ..."
PRECOMPUTE_N=2 $PY precompute_f1.py >> $LOG 2>&1
say "STEP1 done: $(ls f1_cache/*.json 2>/dev/null | wc -l | tr -d ' ') 主役"

# 2) verify 静的エクスポート
say "STEP2 export verify ..."
$PY _export_verify_static.py >> $LOG 2>&1
say "STEP2 done -> public/sim-data-verify"

# 3) テーマ総当たり 再生成（in-process・新エンジン・マージプール）
[ -d theme_f1_cache ] && mv -f theme_f1_cache theme_f1_cache.pre_guardq 2>/dev/null || true
say "STEP3 theme round-robin ..."
SEASON=M-3 COEVO_SEASON=M-3 LEARNED_SELECTION=1 POOL_FILE=func1_pool_M-3.json N_PER_CARD=1 MCTS_SIMS=400 $PY _theme_f1.py >> $LOG 2>&1
say "STEP3 done: $(ls theme_f1_cache/*.json 2>/dev/null | wc -l | tr -d ' ') 主役"

# 4) theme 静的エクスポート
say "STEP4 export theme ..."
$PY _export_theme_static.py >> $LOG 2>&1
say "STEP4 done -> public/sim-data-theme"
say "ALL DONE"
