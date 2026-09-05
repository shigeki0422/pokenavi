// 1v1 エンジン(wasm)の生成物が public/ に揃っているかの確認。
// Cloudflare Pages のビルド環境に cargo は無いので、生成物はリポジトリにコミットしておき
// ここでは存在と鮮度だけを見る。作り直しは scripts/build_engine_wasm.sh。
import fs from "node:fs";
import path from "node:path";

const need = ["public/engine/engine_wasm.wasm", "public/builder-data/engine.pack.json"];
const missing = need.filter((f) => !fs.existsSync(path.join(process.cwd(), f)));
if (missing.length) {
  console.error(`[engine] 生成物がありません: ${missing.join(", ")}`);
  console.error("[engine] scripts/build_engine_wasm.sh を実行してからビルドしてください");
  process.exit(1);
}
const src = "scripts/rust_engine/engine/src";
if (fs.existsSync(src)) {
  const wasmT = fs.statSync(need[0]).mtimeMs;
  const newer = fs.readdirSync(src).filter((f) => f.endsWith(".rs"))
    .filter((f) => fs.statSync(path.join(src, f)).mtimeMs > wasmT);
  if (newer.length) {
    console.warn(`[engine] wasm よりエンジンのソースが新しい: ${newer.join(", ")}`);
    console.warn("[engine] scripts/build_engine_wasm.sh の再実行を検討してください");
  }
}
