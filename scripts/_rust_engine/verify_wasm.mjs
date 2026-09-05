// wasm 版 1v1 が Python(正本)と一致するかを検証する。
// ケースは gen_wasm_cases.py が Python の実行結果を記録したもの。
// 使い方: node scripts/_rust_engine/verify_wasm.mjs [cases.jsonl]
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const WASM = path.join(HERE, "..", "rust_engine", "target", "wasm32-unknown-unknown",
                       "release-wasm", "engine_wasm.wasm");
const PACK = path.join(HERE, "..", "..", "public", "builder-data", "engine.pack.json");
const CASES = process.argv[2] || path.join(HERE, "cases", "wasm_1v1.jsonl");

const { instance } = await WebAssembly.instantiate(fs.readFileSync(WASM), {});
const E = instance.exports;
const enc = new TextEncoder(), dec = new TextDecoder();
const put = (s) => {
  const b = enc.encode(s), p = E.alloc(b.length);
  new Uint8Array(E.memory.buffer).set(b, p);
  return [p, b.length];
};
const take = () =>
  JSON.parse(dec.decode(new Uint8Array(E.memory.buffer, E.result_ptr(), E.result_len())));

const t0 = Date.now();
if (E.init(...put(fs.readFileSync(PACK, "utf8"))) !== 0) throw new Error("pack load 失敗");
console.log(`データパック読み込み: ${Date.now() - t0}ms`);

const cases = fs.readFileSync(CASES, "utf8").trim().split("\n").map((l) => JSON.parse(l));
let ok = 0;
const diffs = new Map();
const note = (k, ex) => {
  if (!diffs.has(k)) diffs.set(k, { n: 0, ex: [] });
  const d = diffs.get(k);
  d.n++;
  if (d.ex.length < 3) d.ex.push(ex);
};

const t1 = Date.now();
for (const c of cases) {
  if (E.analyze(...put(c.a), ...put(c.b), ...put("M-3")) !== 0) throw new Error("analyze 失敗");
  const got = take();
  let good = true;
  for (const [key, want] of [["a", c.sa], ["b", c.sb]]) {
    const g = got[key];
    const lbl = `${c.a.split("@")[0]} vs ${c.b.split("@")[0]} (${key})`;
    if (g.hp !== want.hp) { note("HP", `${lbl}: py=${want.hp} wasm=${g.hp}`); good = false; }
    if (g.speed !== want.speed) {
      note("実効素早さ", `${lbl}: py=${want.speed} wasm=${g.speed}`); good = false;
    }
    for (let i = 0; i < want.moves.length; i++) {
      const w = want.moves[i], x = g.moves[i];
      if (w.dmg === null) continue;                 // 変化技・無効技は対象外
      if (!x || x.n !== w.n) { note("技の並び", `${lbl}: py=${w.n} wasm=${x?.n}`); good = false; continue; }
      const wLo = w.dmgLo, wHi = w.dmgHi;
      if (x.hitsLo !== w.hitsLo) {
        note("確定数(最低乱数)", `${lbl} ${w.n}: py=${w.hitsLo} wasm=${x.hitsLo}`); good = false;
      }
      if (x.hitsHi !== w.hitsHi) {
        note("確定数(最高乱数)", `${lbl} ${w.n}: py=${w.hitsHi} wasm=${x.hitsHi}`); good = false;
      }
      if (x.dmgLo !== wLo) {
        note("与ダメ(最低乱数)", `${lbl} ${w.n}: py=${wLo} wasm=${x.dmgLo}`); good = false;
      }
      if (x.dmgHi !== wHi) {
        note("与ダメ(最高乱数)", `${lbl} ${w.n}: py=${wHi} wasm=${x.dmgHi}`); good = false;
      }
    }
  }
  if (good) ok++;
}
console.log(`照合: ${cases.length}件 / ${Date.now() - t1}ms`);
console.log(`\n=== wasm vs Python(正本) ===`);
console.log(`  完全一致 ${ok}/${cases.length} (${(100 * ok / cases.length).toFixed(1)}%)`);
for (const [k, d] of [...diffs].sort((x, y) => y[1].n - x[1].n)) {
  console.log(`\n  ${k}: ${d.n}件`);
  for (const e of d.ex) console.log(`      ${e}`);
}
process.exit(diffs.size ? 1 : 0);
