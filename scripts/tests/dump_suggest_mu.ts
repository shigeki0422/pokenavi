// 簡単構築の「ポケモン相性」一覧のセルをブラウザと同じ計算（openMuDialog の相手＝targets.json の代表型・judgeVsBuilds の集約）で出す。
// 実行: npx tsx scripts/tests/dump_suggest_mu.ts specs.json > out.json   （specs.json は spec 文字列の配列。出力 {spec: [[label, sym, dep], ...]}）
import fs from "node:fs";
import path from "node:path";
import { initEngineFrom } from "../../src/scripts/engine/wasm";
import { resolveSlot, resolveTargetSafe } from "../../src/scripts/party-builder/balance";
import { judgeVsBuilds } from "../../src/scripts/party-builder/matchup";
import { fromSuggestSpec } from "../../src/scripts/party-builder/spec";
import type { MoveDict, ResolvedBuild, SpeciesMaster, TargetGroup } from "../../src/scripts/party-builder/types";

const ROOT = "/Users/shigeki/work/pokenavi";
const DATA_DIR = process.env.DATA_DIR ?? path.join(ROOT, "public", "builder-data");
const readJson = <T,>(rel: string): T => JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));

await initEngineFrom(
  fs.readFileSync(path.join(ROOT, "public", "engine", "engine_wasm.wasm")),
  fs.readFileSync(path.join(DATA_DIR, "engine.pack.json"), "utf8"),
);
const moves = readJson<MoveDict>("moves.json");
const species = readJson<SpeciesMaster[]>("species.json");
const targets = readJson<TargetGroup[]>("targets.json");
const groups = targets.map((g) => ({
  label: g.label, builds: g.builds.map((b) => resolveTargetSafe(g.sp, g.label, g.icon, b, moves)).filter((b): b is ResolvedBuild => !!b),
}));
const specs: string[] = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out: Record<string, [string, string, boolean][] | null> = {};
for (const s of specs) {
  const slot = fromSuggestSpec(s);
  let me: ResolvedBuild | null = null;
  try { me = slot ? resolveSlot(slot, species, moves) : null; } catch { me = null; }
  out[s] = me ? groups.map((g) => { const a = judgeVsBuilds(me!, g.builds); return [g.label, a.sym, a.dep]; }) : null;
}
console.log(JSON.stringify(out));
