#!/bin/zsh
set -e
cd /Users/shigeki/work/pokenavi/scripts
PY=venv/bin/python
LOG=/tmp/ranked.log
say(){ print -r -- "[$(date '+%H:%M:%S')] $*" | tee -a $LOG; }
say "START ranked-only (N=1, 新エンジン guardq, MCTS@800)"
rm -rf f1_cache; mkdir f1_cache
PRECOMPUTE_N=1 $PY precompute_f1.py >> $LOG 2>&1
say "precompute done: $(ls f1_cache/*.json 2>/dev/null|wc -l|tr -d ' ') 主役"
$PY _export_verify_static.py >> $LOG 2>&1
say "ALL DONE -> public/sim-data-verify"
