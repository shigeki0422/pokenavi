// TS の 1v1 判定（engine/wasm 経由）が Python(正本) と一致するかを検証するための出力側。
// scripts/tests/test_ts_engine.py から esbuild + node で実行され、判定結果を JSON で吐く。
// ここでは判定しない（比較は Python 側で行う）。
import fs from "node:fs";
import path from "node:path";
import { initEngineFrom, buildToSpec } from "../../src/scripts/engine/wasm";
import { judge1v1, moveBreakdown } from "../../src/scripts/party-builder/matchup";
import { resolveTarget } from "../../src/scripts/party-builder/balance";
import type { MoveDict, ResolvedBuild, TargetGroup } from "../../src/scripts/party-builder/types";

const ROOT = process.cwd();
const DATA = path.join(ROOT, "public", "builder-data");
const read = <T,>(rel: string): T => JSON.parse(fs.readFileSync(path.join(DATA, rel), "utf8"));

await initEngineFrom(
  fs.readFileSync(path.join(ROOT, "scripts", "rust_engine", "target",
                           "wasm32-unknown-unknown", "release-wasm", "engine_wasm.wasm")),
  fs.readFileSync(path.join(DATA, "engine.pack.json"), "utf8"),
);

const moves = read<MoveDict>("moves.json");
const targets = read<TargetGroup[]>("targets.json");
const builds: ResolvedBuild[] = [];
for (const g of targets) {
  for (const b of g.builds) {
    try { builds.push(resolveTarget(g.sp, g.label ?? g.sp, g.icon, b, moves)); } catch { /* skip */ }
  }
}

// 決定的にペアを選ぶ（Python 側と同じ並び・同じ添字を使うため乱数は使わない）
const N = Number(process.env.NPAIR || "400");
const out: unknown[] = [];
for (let k = 0; k < N; k++) {
  const a = builds[(k * 7) % builds.length];
  const b = builds[(k * 13 + 3) % builds.length];
  if (a === b) continue;
  const v = judge1v1(a, b);
  out.push({
    specA: buildToSpec({ ...a, moves: a.pool && a.pool.length ? a.pool : a.moves }),
    specB: buildToSpec({ ...b, moves: b.pool && b.pool.length ? b.pool : b.moves }),
    myHits: v.myHits, oppHits: v.oppHits, myS: v.myS, oppS: v.oppS,
    myMove: v.myMove, oppMove: v.oppMove, sym: v.sym, win: v.win,
    breakdown: moveBreakdown(a, b).map((m) => ({
      n: m.n, hits: m.hits, certain: m.certain,
      dmgLo: m.dmgLo, dmgHi: m.dmgHi, prob: m.prob === null ? null : Math.round(m.prob * 100) / 100,
    })),
  });
}
// 報告のあった表示バグの回帰確認用に、名指しの対面も1件出す。
// 「与ダメ」は技そのもののダメージであって、1ターンで減ったHPではない
// （ばけのかわの身代わり分・すなあらしの削り・たべのこしの回復を含めてはいけない）。
const byName = (sp: string) => builds.filter((b) => b.sp === sp);
const kaba = byName("カバルドン")[0], mimi = byName("ミミッキュ")[0];
const named = kaba && mimi
  ? { kabaVsMimi: moveBreakdown(kaba, mimi).find((m) => m.n === "じしん") ?? null,
      mimiHp: mimi.stats[0] }
  : null;
process.stdout.write(JSON.stringify({ pairs: out, named }));
