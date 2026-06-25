#!/bin/zsh
# 一晩パイプライン: テーマ再生成＋共進化自然構築 → マージ → 総当たり(新selector) → 静的エクスポート
set -e
cd /Users/shigeki/work/pokenavi/scripts
PY=venv/bin/python
export SEASON=M-3 COEVO_SEASON=M-3 LEARNED_SELECTION=1
unset SELECT_MODE
LOG=/tmp/overnight.log
say() { print -r -- "[$(date '+%H:%M:%S')] $*" | tee -a $LOG; }

say "START overnight pipeline (selector=m3 deployed, learned selection ON)"

# バックアップ
cp -f func1_themed_M-3.json func1_themed_M-3.bak.json 2>/dev/null || true
[ -d theme_f1_cache ] && mv -f theme_f1_cache theme_f1_cache.bak 2>/dev/null || true

# 1) テーマ再生成
say "STEP1 themed_gen ..."
$PY _themed_gen.py >> $LOG 2>&1
say "STEP1 done: $($PY -c 'import json;print(len(json.load(open("func1_themed_M-3.json"))["parties"]))') テーマ構築"

# 2) 共進化（自然構築） pop64 x 10世代
say "STEP2 coevolution ..."
$PY _coevo.py 64 10 30 M-3 >> $LOG 2>&1
say "STEP2 done: $($PY -c 'import json;print(len(json.load(open("/tmp/coevo_parties_M-3.json"))["parties"]))') 自然構築"

# 3) マージ（テーマ ∪ 強い自然構築40）
say "STEP3 merge pool ..."
$PY _func1_pool.py 40 >> $LOG 2>&1
say "STEP3 done: $($PY -c 'import json;d=json.load(open("func1_pool_M-3.json"));print(d["total"],"(theme",d["n_theme"],"+ natural",d["n_strong"],")")')"

# 4) 総当たり（マージプール・各1戦・MCTS@400・新selector）
say "STEP4 round-robin (theme_f1 over merged pool) ..."
POOL_FILE=func1_pool_M-3.json N_PER_CARD=1 MCTS_SIMS=400 $PY _theme_f1.py >> $LOG 2>&1
say "STEP4 done: $(ls theme_f1_cache/*.json | wc -l | tr -d ' ') 主役ファイル"

# 5) 静的エクスポート（localhost再生用）
say "STEP5 export static ..."
$PY _export_theme_static.py >> $LOG 2>&1
say "STEP5 done -> public/sim-data-theme"

say "ALL DONE"
