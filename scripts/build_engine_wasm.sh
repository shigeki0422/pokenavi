#!/bin/bash
# ブラウザ/ビルド時に使う 1v1 エンジン(wasm)とデータパックを public/ に用意する。
#   scripts/build_engine_wasm.sh
# 対戦ルールは Rust エンジンだけが持ち、TS 側は表示計算のみを行う。
# datapack.json が無い/古い場合は先に _rust_engine/datapack_export.py を実行すること。
set -e
export PATH="$HOME/.cargo/bin:$PATH"
cd "$(dirname "$0")/.."
OUT=public/engine

echo "=== wasm ビルド ==="
(cd scripts/rust_engine && cargo build --profile release-wasm -p engine_wasm --target wasm32-unknown-unknown)
mkdir -p "$OUT"
cp scripts/rust_engine/target/wasm32-unknown-unknown/release-wasm/engine_wasm.wasm "$OUT/"

echo "=== データパック書き出し ==="
scripts/venv/bin/python scripts/_rust_engine/wasm_pack_export.py

ls -l "$OUT/engine_wasm.wasm" public/builder-data/engine.pack.json | awk '{printf "  %-52s %8.0f KB\n", $9, $5/1024}'
