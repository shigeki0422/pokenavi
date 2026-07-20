// ビルド時専用: 各ポケモンの主流型 × 使用率上位30体(targets.json)の1v1集約判定。
// data.ts(loadCore)はfetch前提のブラウザ用のため、ここではnode:fsで直接読む。
import fs from "node:fs";
import path from "node:path";
import type { MoveDict, ResolvedBuild, SpeciesMaster, TargetGroup, Verdict } from "./types";
import { resolveSlot, resolveTarget } from "./balance";
import { judgeVsBuilds, judge1v1 } from "./matchup";
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

/** 「A vs B」直接比較ページ用: 2種の主流型同士の1v1詳細判定(getMatchupsの
 * 集約結果ではなく、双方の技名・確定数・素早さまで含むVerdict全体)を返す。 */
export interface HeadToHead {
  verdict: Verdict;
  me: ResolvedBuild;
  opp: ResolvedBuild;
}
export function getHeadToHead(iconA: string, iconB: string): HeadToHead | null {
  const me = mainBuild(iconA);
  const opp = mainBuild(iconB);
  if (!me || !opp) return null;
  return { verdict: judge1v1(me, opp), me, opp };
}

/**
 * getMatchups()の集約(◎/○/△/▲/×とdep)の「内訳」を返す唯一の窓口。
 * /counters/・/pokemon/(MatchupSection)双方のポップアップはこの関数だけを使い、
 * 「相手の型として何を採用するか」のロジック(=targets.jsonの型プール、最大3種)を
 * 一箇所に統一する。ここを直せば両ページの表示が同時に直る。
 * myIconは主流型1つ固定(自分の型は確定しているという前提)、oppIconは使用率上位
 * プール内の種である必要がある(getMatchups()と同じ前提)。プール外ならnull。
 */
export interface MatchupBuildRow {
  build: ResolvedBuild;
  verdict: Verdict;
}
export interface MatchupBreakdown {
  me: ResolvedBuild;
  oppName: string;
  builds: MatchupBuildRow[];
  sym: StaticMatchup["sym"];
  dep: boolean;
}
export function getMatchupBreakdown(myIcon: string, oppIcon: string): MatchupBreakdown | null {
  const me = mainBuild(myIcon);
  if (!me) return null;
  const oppGroup = resolvedTargets.find((t) => t.icon === oppIcon);
  if (!oppGroup || !oppGroup.builds.length) return null;
  const agg = judgeVsBuilds(me, oppGroup.builds);
  const builds = oppGroup.builds.map((build, i) => ({ build, verdict: agg.verdicts[i] }));
  return { me, oppName: oppGroup.name, builds, sym: agg.sym, dep: agg.dep };
}
