#!/bin/bash
# R0〜R4 パリティゲート一括実行（scripts/ を cwd にして実行すること）
#   使い方: ./_rust_engine/run_gates.sh [r03|r4|all]   （既定 all）
#
# ケースは Python(正本) の記録なので、記録後に simulator/**.py を変えると
# エンジンが正しくてもゲートが赤くなる。各ケースのヘッダに刻んだ sim_hash を
# ゲートが datapack と突き合わせ、古ければ結果と一緒にそう言う（casehdr.rs）。
# 全ゲートが緑で終わったら、そのコーパスは現在の仕様と一致しているので刻印を更新する。
set -e
export PATH="$HOME/.cargo/bin:$PATH"
cd "$(dirname "$0")/.."
WHICH="${1:-all}"

venv/bin/python _rust_engine/datapack_export.py
(cd rust_engine && cargo build --release)

if [ "$WHICH" = "all" ] || [ "$WHICH" = "r03" ]; then
  venv/bin/python _rust_engine/gate_r0.py
  (cd _rust_engine
   ../rust_engine/target/release/gate_r1 datapack.json cases/shard_0*.jsonl cases/synth_00.jsonl
   R2_COVERAGE_OUT=coverage_r2.json ../rust_engine/target/release/gate_r2 datapack.json \
     cases/turn_0*.jsonl cases/turn_80.jsonl cases/turn_81.jsonl
   # R3-T1: CPython MT19937 ビット一致
   ../rust_engine/target/release/gate_r3_rng cases/rng_00.jsonl
   # R3-T2/T3: フル対戦パリティ（gg 50,000 / heuristic 10,000 / partial-spec 2,000）
   ../rust_engine/target/release/gate_r3 datapack.json cases/fb_*.jsonl
   # R3 追加: select_party（選出順＋副作用後の全状態）
   ../rust_engine/target/release/gate_r3_sel datapack.json cases/sel_00.jsonl)
  # 使用率に出ないアイテム（M-C追加分など）は乱数サンプリングのコーパスに現れないので、
  # 明示ケースで wasm と突き合わせる（ここが無いと実装漏れがゲートを素通りする）。
  venv/bin/python _rust_engine/gen_newitem_cases.py
  node _rust_engine/verify_wasm.mjs _rust_engine/cases/wasm_newitem.jsonl
fi

if [ "$WHICH" = "all" ] || [ "$WHICH" = "r4" ]; then
  (cd _rust_engine
   # R4-G1/G2: encode_state(905) ＋ 逐次ネットforward のビット一致（≥20万状態）
   ../rust_engine/target/release/gate_r4_enc datapack.json cases/enc_0*.jsonl
   # R4-G3: MCTS フル対戦パリティ（逐次ネット・sorted belief・HASHSEED=0）
   ../rust_engine/target/release/gate_r4_mcts datapack.json cases/mc_[0-9]*.jsonl)
  # R4 追加: mcts_vs_dist（select_party temp0.3 込み）… pyengine(pokenavi_engine) が必要。
  # このゲートだけは記録ケースではなく Python と Rust を両方その場で走らせて突き合わせる。
  # 呼ぶのは cargo が作る gate バイナリではなく venv に入った .so なので、ここで必ず作り直す。
  # 作り直しを省いた結果、9/2ビルドの .so が9/5の _effective_speed 修正を含まないまま
  # 「Rustの乖離」に見える事故が起きた（`|| true` で失敗も握り潰されていた）。
  # VIRTUAL_ENV を明示する。省略すると maturin がリポジトリ直下の .venv(Python3.14)を掴み、
  # pyo3 0.22 がビルドできず失敗する（正しいインストール先は scripts/venv の cpython-312）。
  VIRTUAL_ENV="$(pwd)/venv" venv/bin/maturin develop -m rust_engine/pyengine/Cargo.toml --release -q
  VD_N="${VD_N:-40}" venv/bin/python _rust_engine/gate_r4_vsdist.py
fi

# ここまで来た＝全ゲートが乖離0。コーパスは現在の simulator/** と一致しているので刻印を更新する。
if [ "$WHICH" = "all" ]; then
  venv/bin/python _rust_engine/case_stamp.py --stamp | tail -3
fi

echo "=== gates done ($WHICH) ==="
