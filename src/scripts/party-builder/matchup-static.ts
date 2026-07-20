// ビルド時専用: 各ポケモンの主流型 × 使用率上位30体(targets.json)の1v1集約判定。
// data.ts(loadCore)はfetch前提のブラウザ用のため、ここではnode:fsで直接読む。
import fs from "node:fs";
import path from "node:path";
import type { MoveDict, ResolvedBuild, SpeciesMaster, TargetGroup, Verdict } from "./types";
import { resolveSlot, resolveTarget } from "./balance";
import { judgeVsBuilds, judge1v1, bestMoveDamageRange } from "./matchup";
import { fromSpec } from "./spec";

export interface StaticMatchup {
  icon: string;
  name: string;
  sym: "◎" | "○" | "△" | "▲" | "×";
  dep: boolean;
  /** 相手側がメガ進化複数系統(X/Y等)のうちどれかを指すエントリの場合、
   * getMatchupBreakdown()呼び出し時に相手側の型を特定するための石の名前。
   * 単一系統の相手ならundefined。 */
  preferItem?: string;
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

function readMon(icon: string): { items?: { n: string }[]; builds?: string[] } | null {
  const monPath = path.join(DATA_DIR, "mon", `${icon}.json`);
  if (!fs.existsSync(monPath)) return null;
  try {
    return JSON.parse(fs.readFileSync(monPath, "utf8"));
  } catch {
    return null;
  }
}

/**
 * preferItem指定時はその持ち物(型プールのspec文字列内`@{item}:`)を含む型を優先して探す。
 * リザードンのようにメガ進化が複数系統(X/Y)あり、かつ主流の持ち物(石)がどちらか一方に
 * 偏っている種で、単純な「採用率最多の持ち物」だけを見ると、他方の系統(型)の型が
 * 一切考慮されなくなる問題があった(例: メガリザードンYの採用率が高いため、
 * mainBuild('0006-00')は常にY型を返し、X型の有利不利は計算されていなかった)。
 * mainBuildVariants()と組み合わせて、複数メガ種は系統ごとに個別評価する。
 */
function mainBuild(icon: string, preferItem?: string): ResolvedBuild | null {
  const mon = readMon(icon);
  const builds = mon?.builds ?? [];
  if (!builds.length) return null;
  const topItem = preferItem ?? mon?.items?.[0]?.n;
  const spec = (topItem && builds.find((s) => s.includes(`@${topItem}:`))) || builds[0];
  const slot = fromSpec(spec);
  if (!slot) return null;
  try {
    return resolveSlot(slot, species, moves);
  } catch {
    return null;
  }
}

export interface MainBuildVariant {
  /** 表示名。メガ進化が単一(または無し)ならその種の代表名、複数ならメガ名(例: メガリザードンX)。 */
  label: string;
  /** mainBuild()に渡すpreferItem。複数メガ系統がある場合のみ設定(石の名前)。 */
  preferItem: string | undefined;
  build: ResolvedBuild;
}
/**
 * その種にメガ進化が複数系統(石違い)ある場合(現状: リザードンX/Y、ライチュウX/Y)、
 * 系統ごとに代表型を1つずつ返す。1系統以下ならmainBuild()相当の単一結果を返す。
 * 「自分の型として何を採用するか」の唯一の窓口。ここを直せば有利・不利判定を
 * 使う全ページ(/pokemon/・/counters/・/matchup/)に反映される。
 */
const mainBuildVariantsCache = new Map<string, MainBuildVariant[]>();
export function mainBuildVariants(icon: string, defaultLabel: string): MainBuildVariant[] {
  const cached = mainBuildVariantsCache.get(icon);
  if (cached) return cached;
  const mon = readMon(icon);
  const builds = mon?.builds ?? [];
  let result: MainBuildVariant[];
  if (!builds.length) {
    result = [];
  } else {
    const sp = species.find((s) => builds[0]?.startsWith(`${s.n}@`));
    const megas = sp?.mega ?? [];
    if (megas.length < 2) {
      const build = mainBuild(icon);
      result = build ? [{ label: defaultLabel, preferItem: undefined, build }] : [];
    } else {
      result = [];
      for (const m of megas) {
        const build = mainBuild(icon, m.stone);
        if (build) result.push({ label: m.name, preferItem: m.stone, build });
      }
    }
  }
  mainBuildVariantsCache.set(icon, result);
  return result;
}

/**
 * 使用率上位プール(targets.json)の「対戦相手」表現。メガ進化が複数系統ある種
 * (現状: リザードン、ライチュウ)は、他ポケモンの「有利・不利な相手」表に
 * 「メガリザードンX」「メガリザードンY」として別々のエントリで出す(従来は
 * targets.jsonの1エントリ=Y型のみで計算され、X型に対する有利不利が他の
 * ポケモンのページに一切反映されていなかった)。単一系統の種はtargets.json
 * そのままの型プール(複数の持ち物パターン等)を使い、挙動を変えない。
 */
interface OpponentGroup {
  icon: string;
  name: string;
  builds: ResolvedBuild[];
  preferItem?: string;
}
const resolvedTargetsExpanded: OpponentGroup[] = (() => {
  const out: OpponentGroup[] = [];
  for (const t of resolvedTargets) {
    const variants = mainBuildVariants(t.icon, t.name);
    if (variants.length > 1) {
      for (const v of variants) out.push({ icon: t.icon, name: v.label, builds: [v.build], preferItem: v.preferItem });
    } else {
      out.push(t);
    }
  }
  return out;
})();

const cache = new Map<string, StaticMatchup[] | null>();

function judgeAgainstPool(me: ResolvedBuild, ownIcon: string): StaticMatchup[] {
  return resolvedTargetsExpanded
    .filter((t) => t.icon !== ownIcon)
    .map((t) => {
      const v = judgeVsBuilds(me, t.builds);
      return { icon: t.icon, name: t.name, sym: v.sym, dep: v.dep, preferItem: t.preferItem };
    });
}

export function getMatchups(icon: string, preferItem?: string): StaticMatchup[] | null {
  const cacheKey = preferItem ? `${icon}::${preferItem}` : icon;
  if (cache.has(cacheKey)) return cache.get(cacheKey)!;
  const me = mainBuild(icon, preferItem);
  const result = me ? judgeAgainstPool(me, icon) : null;
  cache.set(cacheKey, result);
  return result;
}

/** 「A vs B」直接比較ページ用: 2種の主流型同士の1v1詳細判定(getMatchupsの
 * 集約結果ではなく、双方の技名・確定数・素早さまで含むVerdict全体)を返す。 */
export interface HeadToHead {
  verdict: Verdict;
  me: ResolvedBuild;
  opp: ResolvedBuild;
}
export function getHeadToHead(iconA: string, iconB: string, preferItemA?: string): HeadToHead | null {
  const me = mainBuild(iconA, preferItemA);
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
const EV_LABELS = ["H", "A", "B", "C", "D", "S"] as const;
/** EV配分を「H2 A32 S32」のように非ゼロ値のみ表示する共通フォーマット。 */
function evLabel(evs: ResolvedBuild["evs"]): string {
  return evs
    .map((v, i) => (v > 0 ? `${EV_LABELS[i]}${v}` : null))
    .filter((s): s is string => s !== null)
    .join(" ");
}

export interface MatchupBuildRow {
  build: ResolvedBuild;
  verdict: Verdict;
  evLabel: string;
  /** 自分(me)がこの型に与える最大打点技のダメージ割合(%, 乱数min〜max)。 */
  myDmg: ReturnType<typeof bestMoveDamageRange>;
  /** この型が自分(me)に与える最大打点技のダメージ割合(%, 乱数min〜max)。 */
  oppDmg: ReturnType<typeof bestMoveDamageRange>;
}
export interface MatchupBreakdown {
  me: ResolvedBuild;
  oppName: string;
  builds: MatchupBuildRow[];
  sym: StaticMatchup["sym"];
  dep: boolean;
}
export function getMatchupBreakdown(
  myIcon: string,
  oppIcon: string,
  myPreferItem?: string,
  oppPreferItem?: string,
): MatchupBreakdown | null {
  const me = mainBuild(myIcon, myPreferItem);
  if (!me) return null;
  const oppGroup = resolvedTargetsExpanded.find((t) => t.icon === oppIcon && t.preferItem === oppPreferItem);
  if (!oppGroup || !oppGroup.builds.length) return null;
  const agg = judgeVsBuilds(me, oppGroup.builds);
  const builds = oppGroup.builds.map((build, i) => ({
    build,
    verdict: agg.verdicts[i],
    evLabel: evLabel(build.evs),
    myDmg: bestMoveDamageRange(me, build),
    oppDmg: bestMoveDamageRange(build, me),
  }));
  return { me, oppName: oppGroup.name, builds, sym: agg.sym, dep: agg.dep };
}
