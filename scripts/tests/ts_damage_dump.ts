// Python(scripts/simulator/damage.py)との数値パリティ検証用: TS側(src/scripts/party-builder/damage.ts)の
// ダメージ計算結果を JSON で吐き出す。scripts/tests/test_ts_damage_parity.py から呼ばれる。
// 使い方: npx esbuild --bundle ... ではなく node --experimental-strip-types 相当が要るため、
//         test_ts_damage_parity.py が esbuild でバンドルしてから node で実行する。
import fs from "node:fs";
import path from "node:path";
import { calcHitDamages, fieldWeather, multiHitCount } from "../../src/scripts/party-builder/damage";
import { resolveTarget } from "../../src/scripts/party-builder/balance";
import type { MoveDict, ResolvedBuild, TargetGroup, MonDetail, TargetBuild } from "../../src/scripts/party-builder/types";

const DATA_DIR = path.join(process.cwd(), "public", "builder-data");
const read = <T,>(rel: string): T => JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));

const moves = read<MoveDict>("moves.json");
const targets = read<TargetGroup[]>("targets.json");

// targets.json の全型を解決し、総当たりで「攻撃側の各技 × 防御側」のダメージを出す
const builds: ResolvedBuild[] = [];
for (const g of targets) {
  for (const b of g.builds) {
    try {
      builds.push(resolveTarget(g.sp, g.label ?? g.sp, g.icon, b, moves));
    } catch {
      /* skip */
    }
  }
}
// mon/*.json の代表型(mu)も混ぜて、天候特性持ち(キュウコン/バンギラス/ペリッパー等)を確実に含める
for (const f of fs.readdirSync(path.join(DATA_DIR, "mon"))) {
  const mon = read<MonDetail>(path.join("mon", f));
  const icon = f.replace(/\.json$/, "");
  for (const b of (mon.mu ?? []) as TargetBuild[]) {
    try {
      builds.push(resolveTarget(mon.n, b.label ?? mon.n, icon, b, moves));
    } catch {
      /* skip */
    }
  }
}

interface Case {
  atk: ResolvedBuild;
  def: ResolvedBuild;
  move: string;
  roll: number;
  /** 1発ごとのダメージ列（連続技はヒット数分）。Python側は同じヒット数でループして比較する。 */
  hits: number[];
  nhits: number;
  weather: string | null;
}

// 決定的な擬似乱数でケースをサンプリング（毎回同じ組を検証する）
let seed = 12345;
const rnd = () => ((seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);

const cases: Case[] = [];
const N = Number(process.env.PARITY_N ?? 400);
while (cases.length < N) {
  const a = builds[Math.floor(rnd() * builds.length)];
  const d = builds[Math.floor(rnd() * builds.length)];
  if (!a || !d || !a.moves.length) continue;
  const mv = a.moves[Math.floor(rnd() * a.moves.length)];
  if (!mv || mv.cat === "status" || !mv.power) continue;
  // きまぐレーザーはPython側が真の乱数(30%で威力2倍)で非決定的なため、パリティ検証の対象外
  // (TS側は基礎威力を採用する決定的近似。damage.ts末尾の未サポート一覧に記載)。
  if (mv.n === "きまぐレーザー") continue;
  const roll = Math.floor(rnd() * 16) / 15;
  cases.push({
    atk: a,
    def: d,
    move: mv.n,
    roll,
    hits: calcHitDamages(a, d, mv, { randomRoll: roll }),
    nhits: multiHitCount(a, mv),
    weather: fieldWeather(a, d),
  });
}

process.stdout.write(JSON.stringify(cases));
