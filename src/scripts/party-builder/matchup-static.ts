// ビルド時専用: 各ポケモンの主流型 × 使用率上位30体(targets.json)の1v1集約判定。
// data.ts(loadCore)はfetch前提のブラウザ用のため、ここではnode:fsで直接読む。
import fs from "node:fs";
import path from "node:path";
import type { MoveDict, ResolvedBuild, SpeciesMaster, TargetGroup } from "./types";
import { resolveSlot, resolveTarget } from "./balance";
import { judgeVsBuilds } from "./matchup";
import { fromSpec } from "./spec";

export interface StaticMatchup {
  icon: string;
  name: string;
  sym: "◎" | "○" | "△" | "▲" | "×";
  dep: boolean;
}

const DATA_DIR = path.join(process.cwd(), "public", "builder-data");

function readJson<T>(rel: string): T {
  return JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));
}

const species = readJson<SpeciesMaster[]>("species.json");
const moves = readJson<MoveDict>("moves.json");
const targetGroups = readJson<TargetGroup[]>("targets.json");

const resolvedTargets = targetGroups.map((g) => ({
  icon: g.icon,
  name: g.sp,
  builds: g.builds.map((b) => resolveTarget(g.sp, g.label ?? g.sp, g.icon, b, moves)),
}));

function mainBuild(icon: string): ResolvedBuild | null {
  const monPath = path.join(DATA_DIR, "mon", `${icon}.json`);
  if (!fs.existsSync(monPath)) return null;
  let mon: { items?: { n: string }[]; builds?: string[] };
  try {
    mon = JSON.parse(fs.readFileSync(monPath, "utf8"));
  } catch {
    return null;
  }
  const builds = mon.builds ?? [];
  if (!builds.length) return null;
  const topItem = mon.items?.[0]?.n;
  const spec = (topItem && builds.find((s) => s.includes(`@${topItem}:`))) || builds[0];
  const slot = fromSpec(spec);
  if (!slot) return null;
  try {
    return resolveSlot(slot, species, moves);
  } catch {
    return null;
  }
}

const cache = new Map<string, StaticMatchup[] | null>();

export function getMatchups(icon: string): StaticMatchup[] | null {
  if (cache.has(icon)) return cache.get(icon)!;
  const me = mainBuild(icon);
  let result: StaticMatchup[] | null = null;
  if (me) {
    result = resolvedTargets
      .filter((t) => t.icon !== icon)
      .map((t) => {
        const v = judgeVsBuilds(me, t.builds);
        return { icon: t.icon, name: t.name, sym: v.sym, dep: v.dep };
      });
  }
  cache.set(icon, result);
  return result;
}
