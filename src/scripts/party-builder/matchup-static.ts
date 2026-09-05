// ビルド時専用: 各ポケモンの主流型 × 使用率上位30体(targets.json)の1v1集約判定。
// data.ts(loadCore)はfetch前提のブラウザ用のため、ここではnode:fsで直接読む。
import fs from "node:fs";
import path from "node:path";
import type { MonDetail, MoveDict, ResolvedBuild, SpeciesMaster, TargetBuild, TargetGroup, Verdict } from "./types";
import { resolveTarget } from "./balance";
import { judgeVsBuildsMulti, judge1v1, bestMoveHitDetail, pairHitDetails } from "./matchup";
import { initEngineFrom } from "../engine/wasm";

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

// 1v1 判定は対戦エンジン(wasm)が行う。ビルド時(Node)でもブラウザと同じ実装を使うため、
// ここで同期的に読み込んでおく（このモジュールの初期化中に judge1v1 が呼ばれるため）。
// 生成物が無い場合は scripts/build_engine_wasm.sh を先に実行する。
await initEngineFrom(
  fs.readFileSync(path.join(process.cwd(), "public", "engine", "engine_wasm.wasm")),
  fs.readFileSync(path.join(DATA_DIR, "engine.pack.json"), "utf8"),
);

function readJson<T>(rel: string): T {
  return JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));
}

const species = readJson<SpeciesMaster[]>("species.json");
const moves = readJson<MoveDict>("moves.json");
const targetGroups = readJson<TargetGroup[]>("targets.json");

const resolvedTargets = targetGroups.map((g) => ({
  icon: g.icon,
  name: g.label ?? g.sp,
  preferItem: g.stone,
  builds: g.builds.map((b) => resolveTarget(g.sp, g.label ?? g.sp, g.icon, b, moves)),
}));

function readMon(icon: string): MonDetail | null {
  const monPath = path.join(DATA_DIR, "mon", `${icon}.json`);
  if (!fs.existsSync(monPath)) return null;
  try {
    return JSON.parse(fs.readFileSync(monPath, "utf8"));
  } catch {
    return null;
  }
}

/**
 * 自分側の代表型(型1/2/3)。gen_builder_data.py が持ち物×攻撃軸(A/C/耐久)で合成した
 * mon/*.json の `mu` をそのまま解決する。相手側(targets.json builds)と完全に同じ
 * スキーマ・同じ生成ロジックなので、自分側だけ1型固定という非対称が無くなる。
 * preferItem指定時はその持ち物(＝メガ石)の型だけに絞る。
 * リザードンのようにメガ進化が複数系統(X/Y)ある種で、採用率最多の石だけを見ると
 * 他方の系統が一切評価されない問題があったため、mainBuildVariants()と組み合わせて
 * 系統ごとに個別評価する。
 */
const myVariantsCache = new Map<string, ResolvedBuild[]>();
function myVariants(icon: string, preferItem?: string): ResolvedBuild[] {
  const cacheKey = `${icon}::${preferItem ?? ""}`;
  const cached = myVariantsCache.get(cacheKey);
  if (cached) return cached;
  const mon = readMon(icon);
  let mu: TargetBuild[] = mon?.mu ?? [];
  if (preferItem) mu = mu.filter((b) => b.item === preferItem);
  const sp = mon?.n ?? "";
  const result = mu
    .map((b) => {
      try {
        return resolveTarget(sp, b.label ?? sp, icon, b, moves);
      } catch {
        return null;
      }
    })
    .filter((b): b is ResolvedBuild => !!b);
  myVariantsCache.set(cacheKey, result);
  return result;
}

/** 代表型のうち先頭(＝採用率最上位の型)。1体だけを示す用途(A vs B 比較ページ等)に使う。 */
function mainBuild(icon: string, preferItem?: string): ResolvedBuild | null {
  return myVariants(icon, preferItem)[0] ?? null;
}

export interface MainBuildVariant {
  /** 表示名。メガ進化が単一(または無し)ならその種の代表名、複数ならメガ名(例: メガリザードンX)。 */
  label: string;
  /** getMatchups()に渡すpreferItem。複数メガ系統がある場合のみ設定(石の名前)。 */
  preferItem: string | undefined;
  /** その系統に属する自分側の代表型(型1/2/3)。 */
  builds: ResolvedBuild[];
}
/**
 * その種にメガ進化が複数系統(石違い)ある場合(現状: リザードンX/Y、ライチュウX/Y)、
 * 系統ごとに代表型を1つずつ返す。1系統以下ならmainBuild()相当の単一結果を返す。
 * 「自分の型として何を採用するか」の唯一の窓口。ここを直せば有利・不利判定を
 * 使う全ページ(/pokemon/・/counters/・/matchup/)に反映される。
 */
const mainBuildVariantsCache = new Map<string, MainBuildVariant[]>();
export function mainBuildVariants(icon: string, defaultLabel: string): MainBuildVariant[] {
  // defaultLabelは単一系統種の場合の表示名(ja/en/koで異なる)としてそのまま
  // 結果に埋め込まれるため、iconだけでキャッシュすると同じ種のja/en/koページ間で
  // ラベルが混線する(実際に発生: ニンフィアの日本語ページにSylveonという
  // 英語名が出た)。defaultLabelもキーに含める。
  const cacheKey = `${icon}::${defaultLabel}`;
  const cached = mainBuildVariantsCache.get(cacheKey);
  if (cached) return cached;
  const all = myVariants(icon);
  let result: MainBuildVariant[] = [];
  if (all.length) {
    const sm = species.find((s) => s.n === all[0].sp);
    // 実際に代表型として採用されているメガ石が2系統以上ある場合のみ分割する
    // (種としてX/Yが存在しても、片方が使用率0なら型が作られないので1系統扱い)。
    const usedStones = (sm?.mega ?? []).filter((m) => all.some((b) => b.item === m.stone));
    if (usedStones.length >= 2) {
      for (const m of usedStones) {
        const builds = myVariants(icon, m.stone);
        if (builds.length) result.push({ label: m.name, preferItem: m.stone, builds });
      }
    } else {
      result = [{ label: defaultLabel, preferItem: undefined, builds: all }];
    }
  }
  mainBuildVariantsCache.set(cacheKey, result);
  return result;
}

/**
 * 使用率上位プール(targets.json)の「対戦相手」表現。メガ進化が複数系統ある種
 * (現状: リザードン、ライチュウ)は、他ポケモンの「有利・不利な相手」表に
 * 「リザードンX」「リザードンY」として別々のエントリで出す(従来は
 * targets.jsonの1エントリ=Y型のみで計算され、X型に対する有利不利が他の
 * ポケモンのページに一切反映されていなかった)。
 * この分割は gen_builder_data.py の build_targets() 側で済んでおり(stone フィールド)、
 * ここでは targets.json をそのまま使う。以前はTS側でも再分割していたため、
 * 同じ相手が2重に列挙されていた。
 */
interface OpponentGroup {
  icon: string;
  name: string;
  builds: ResolvedBuild[];
  preferItem?: string;
}
const resolvedTargetsExpanded: OpponentGroup[] = resolvedTargets;

const cache = new Map<string, StaticMatchup[] | null>();

function judgeAgainstPool(mes: ResolvedBuild[], ownIcon: string): StaticMatchup[] {
  return resolvedTargetsExpanded
    .filter((t) => t.icon !== ownIcon)
    .map((t) => {
      const v = judgeVsBuildsMulti(mes, t.builds);
      return { icon: t.icon, name: t.name, sym: v.sym, dep: v.dep, preferItem: t.preferItem };
    });
}

/** 自分の代表型(最大3) × 相手の代表型(最大3)を総当たりで判定した集約結果。 */
export function getMatchups(icon: string, preferItem?: string): StaticMatchup[] | null {
  const cacheKey = preferItem ? `${icon}::${preferItem}` : icon;
  if (cache.has(cacheKey)) return cache.get(cacheKey)!;
  const mes = myVariants(icon, preferItem);
  const result = mes.length ? judgeAgainstPool(mes, icon) : null;
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
  /** 自分(me)がこの型に与える最大打点技の詳細(ダメージ%・確定数/乱数n発+確率)。 */
  myDmg: ReturnType<typeof bestMoveHitDetail>;
  /** この型が自分(me)に与える最大打点技の詳細。 */
  oppDmg: ReturnType<typeof bestMoveHitDetail>;
}
export interface MatchupBreakdown {
  me: ResolvedBuild;
  oppName: string;
  builds: MatchupBuildRow[];
  sym: StaticMatchup["sym"];
  dep: boolean;
}
/** 自分の型(ResolvedBuild)を直接指定する版。myBuildOptions()で得た複数候補
 * それぞれについてポップアップの内訳を出す(自分の型タブ切り替え)ために使う。 */
export function getMatchupBreakdownForBuild(
  me: ResolvedBuild,
  oppIcon: string,
  oppPreferItem?: string,
): MatchupBreakdown | null {
  const oppGroup = resolvedTargetsExpanded.find((t) => t.icon === oppIcon && t.preferItem === oppPreferItem);
  if (!oppGroup || !oppGroup.builds.length) return null;
  const agg = judgeVsBuildsMulti([me], oppGroup.builds);
  const builds = oppGroup.builds.map((build, i) => ({
    build,
    verdict: agg.verdicts[i],
    evLabel: evLabel(build.evs),
    // 与ダメ・被ダメは同じ場の前提で出す（向きごとに呼ぶと天候が食い違う）
    ...(() => { const d = pairHitDetails(me, build); return { myDmg: d.my, oppDmg: d.opp }; })(),
  }));
  return { me, oppName: oppGroup.name, builds, sym: agg.sym, dep: agg.dep };
}
export function getMatchupBreakdown(
  myIcon: string,
  oppIcon: string,
  myPreferItem?: string,
  oppPreferItem?: string,
): MatchupBreakdown | null {
  const me = mainBuild(myIcon, myPreferItem);
  if (!me) return null;
  return getMatchupBreakdownForBuild(me, oppIcon, oppPreferItem);
}

export interface MyBuildOption {
  /** タブ表示用ラベル(持ち物・性格)。 */
  label: string;
  build: ResolvedBuild;
}
/**
 * 自分側の主要な型を複数(最大count件)返す。相手側は既にtargets.json由来の
 * 型プール(最大3種)を評価対象にしているのに対し、自分側はmainBuild()で
 * 常に採用率最多の1型に固定されており「自分の型を変えたらどうなるか」が
 * 見えない、という指摘を受けて追加。preferItem指定時(メガ進化が複数系統
 * ある種)はその石を使う型の中から複数候補を探す。
 */
export function myBuildOptions(icon: string, preferItem: string | undefined, count = 3): MyBuildOption[] {
  return myVariants(icon, preferItem)
    .slice(0, count)
    .map((build) => ({ label: `${build.item}・${build.nature}`, build }));
}
