// 記事の「事実ファイル」用の汎用1v1ダンプ。dump_matchups_garchomp_m7.ts を汎用化したもの。
// 判定ロジック(judge1v1/pairHitDetails/ダメージ計算等)には一切手を加えない。
//
// dump_matchups_garchomp_m7.ts との違い:
//   - SUBJECT_ICON を env で受ける（必須）。
//   - SUBJECT_BUILDS（TargetBuild配列のJSONパス）で自分側の代表型を差し替えられる。
//     無ければ mon/{icon}.json の mu を使う。記事の型カードと一致させるのが目的。
//   - 各ペア行に、自分/相手の 型名・持ち物・性格・EV・特性・実数値・メガ有無 を出す
//     （従来は持ち物名しか無く、性格違いの個体を記事側で区別できなかった）。
//   - 技の優先度(prio)・タイプ相性(eff)・与ダメ実数値(dmgLo/Hi)を出す。
//   - % は小数1桁に丸める。乱数確率は表示用の整数文字列(probInt)も併記する。
//   - publishable / excluded のどちらも allRows を必ず出す。
//
// 実行: cd pokenavi && SUBJECT_ICON=0445-00 [SUBJECT_BUILDS=path.json] [MAJORITY_PCT=20] \
//        [OPP_ICONS=0730-00,0778-00] [OPP_ITEM_MAJORITY=1] npx tsx scripts/tests/dump_matchups_facts.ts
import fs from "node:fs";
import path from "node:path";
import { initEngineFrom } from "../../src/scripts/engine/wasm";
import { resolveTarget } from "../../src/scripts/party-builder/balance";
import { judge1v1, pairHitDetails, fmtKoProbPct } from "../../src/scripts/party-builder/matchup";
import type { MoveDict, ResolvedBuild, TargetGroup, TargetBuild, Verdict, StatArray } from "../../src/scripts/party-builder/types";

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..", "..");
const DATA_DIR = path.join(ROOT, "public", "builder-data");
function readJson<T>(rel: string): T {
  return JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));
}

const SUBJECT_ICON = process.env.SUBJECT_ICON ?? "";
if (!SUBJECT_ICON) {
  console.error("SUBJECT_ICON が必要です（例: SUBJECT_ICON=0445-00）");
  process.exit(2);
}
const MAJORITY_PCT = Number(process.env.MAJORITY_PCT ?? "20");
const OPP_ITEM_MAJORITY = (process.env.OPP_ITEM_MAJORITY ?? "1") !== "0";
const OPP_ICONS = (process.env.OPP_ICONS ?? "").split(",").map((s) => s.trim()).filter(Boolean);
const OUT_OF_RANGE = 999;

await initEngineFrom(
  fs.readFileSync(path.join(ROOT, "scripts", "rust_engine", "target",
                           "wasm32-unknown-unknown", "release-wasm", "engine_wasm.wasm")),
  fs.readFileSync(path.join(DATA_DIR, "engine.pack.json"), "utf8"),
);

const moves = readJson<MoveDict>("moves.json");
const targetGroups = readJson<TargetGroup[]>("targets.json");
let builderVersion: unknown = null;
try { builderVersion = readJson("version.json"); } catch { builderVersion = null; }

function readMon(icon: string): any { return readJson(`mon/${icon}.json`); }

function majorityMoves(icon: string): Map<string, number> {
  const m = new Map<string, number>();
  for (const e of (readMon(icon).moves ?? []) as { n: string; pct: number }[]) {
    if (e.pct >= MAJORITY_PCT) m.set(e.n, e.pct);
  }
  return m;
}

function restrictToMajority(b: ResolvedBuild, maj: Map<string, number>): ResolvedBuild {
  const src = (b.pool && b.pool.length ? b.pool : b.moves) ?? [];
  return { ...b, pool: src.filter((m) => maj.has(m.n)) };
}

function majorityItems(icon: string): Set<string> {
  const s = new Set<string>();
  for (const e of (readMon(icon).items ?? []) as { n: string; pct: number }[]) {
    if (e.pct >= MAJORITY_PCT) s.add(e.n);
  }
  return s;
}

function hasAttack(b: ResolvedBuild): boolean {
  return (b.pool ?? []).some((m) => m.cat !== "status" && (m.power ?? 0) > 0);
}

const r1 = (x: number | null | undefined): number | null => (x == null ? null : Math.round(x * 10) / 10);
const prioOf = (n: string | null | undefined): number | null => (n && moves[n] ? moves[n][3] : null);

const subjectMon = readMon(SUBJECT_ICON);
const subjectTargetBuilds: TargetBuild[] = process.env.SUBJECT_BUILDS
  ? JSON.parse(fs.readFileSync(process.env.SUBJECT_BUILDS, "utf8"))
  : (subjectMon.mu as TargetBuild[]);
if (!subjectTargetBuilds || !subjectTargetBuilds.length) {
  console.error("自分側の代表型が空です（SUBJECT_BUILDS または mon/{icon}.json の mu）");
  process.exit(2);
}

// majorityMoves は技の採用率%表示(myMoveUsageRate等)に使うだけで、技プールの絞り込みには使わない
// （2026-10-17: mpoolは実データで常にmovesと同一 <全86ビルドで確認>。種全体のicon単位で絞ると、
//  同じiconを複数メガ系統が共有する種（リザードンX/Y等）で型固有の主力技が誤って除外されるバグが
//  あった。ライブサイト本体（mu-cell-popup.ts/matchup-static.ts）と同じく、resolveTargetの出力
//  （pool=mpool=moves）をそのまま1v1判定に渡す）。
const subjectMaj = majorityMoves(SUBJECT_ICON);
const subjectBuilds: ResolvedBuild[] = subjectTargetBuilds.map((b) =>
  resolveTarget(subjectMon.n, b.label ?? subjectMon.n, SUBJECT_ICON, b, moves)
);

type SideFields = {
  arch: string | null; item: string; nature: string; ev: StatArray; ability: string;
  megaAbility: string | null; stats: StatArray; label: string; mega: boolean;
};
function sideFields(b: ResolvedBuild): SideFields {
  return {
    arch: b.arch ?? null, item: b.item, nature: b.nature, ev: b.evs, ability: b.ability,
    megaAbility: b.megaAbility ?? null, stats: b.stats, label: b.label, mega: b.mega,
  };
}

type BuildRow = {
  myBuild: string; oppBuild: string;
  my: SideFields; opp: SideFields & { share: number | null; idx: number | null };
  win: boolean; sym: Verdict["sym"];
  fast: boolean; koFirst: boolean; koByPriority: boolean;
  myS: number; oppS: number;
  myHits: number | null; oppHits: number | null;
  myMove: string | null; myMoveUsageRate: number | null; myMovePrio: number | null;
  oppMove: string | null; oppMoveUsageRate: number | null; oppMovePrio: number | null;
  myPctLo: number | null; myPctHi: number | null;
  oppPctLo: number | null; oppPctHi: number | null;
  myDmgLo: number | null; myDmgHi: number | null;
  oppDmgLo: number | null; oppDmgHi: number | null;
  myCertain: boolean | null; oppCertain: boolean | null;
  myProb: number | null; oppProb: number | null;
  myProbInt: string | null; oppProbInt: string | null;
  myReason: string | null; oppReason: string | null;
  myEff: number | null; oppEff: number | null;
  mySeq: string[];
  oppSeq: string[];
  // 決着の技（経過 race で相手のHPを0以下にした行動の技）。表示技 myMove/oppMove は最大打点の技で、
  // 先制技で決着した対面（koByPriority）では別の技になる。記事側が優先度の理由を正しく書くために持つ（2026-10-18）。
  myKoMove: string | null; myKoMovePrio: number | null;
  oppKoMove: string | null; oppKoMovePrio: number | null;
  oppItem: string;
};

function koMoveOf(race: Verdict["race"] | undefined, actor: 0 | 1): string | null {
  if (!race) return null;
  const def = 1 - actor;
  const ko = race.find((e) => e.actor === actor && e.hp[def] <= 0 && e.move);
  if (ko) return ko.move;
  const last = [...race].reverse().find((e) => e.actor === actor && e.move);
  return last ? last.move : null;
}

const ok: any[] = [];
const mixed: any[] = [];

for (const g of targetGroups) {
  if (g.icon === SUBJECT_ICON) continue;
  if (OPP_ICONS.length && !OPP_ICONS.includes(g.icon)) continue;
  const oppMaj = majorityMoves(g.icon);
  const oppItemMaj = OPP_ITEM_MAJORITY ? majorityItems(g.icon) : new Set<string>();
  const itemFilteredBuilds = oppItemMaj.size
    ? g.builds.filter((b) => oppItemMaj.has(b.item))
    : g.builds;
  const oppSourceBuilds = itemFilteredBuilds.length ? itemFilteredBuilds : g.builds;
  const oppBuilds = oppSourceBuilds.map((b) => ({
    tb: b,
    // ラベルはビルド単位(b.label)を使う。g.label は種グループ共通の名前で、
    // メガ石持ちビルドでも「メガ○○」にならず元の種名のまま出てしまう（記事側で検出・2026-10-17）。
    // 技プールは絞り込まない（上のsubjectBuildsと同じ理由）。
    rb: resolveTarget(g.sp, b.label ?? g.label ?? g.sp, g.icon, b, moves),
  }));
  if (!oppBuilds.length) continue;

  const rows: BuildRow[] = [];
  for (const me of subjectBuilds) {
    for (const { tb, rb: opp } of oppBuilds) {
      const v = judge1v1(me, opp);
      const d = pairHitDetails(me, opp);
      rows.push({
        myBuild: me.arch ?? me.item, oppBuild: opp.item,
        my: sideFields(me),
        opp: { ...sideFields(opp), share: tb.share ?? null, idx: tb.idx ?? null },
        win: v.win, sym: v.sym,
        fast: v.fast, koFirst: v.koFirst, koByPriority: v.koByPriority,
        myS: v.myS, oppS: v.oppS,
        myHits: v.myHits, oppHits: v.oppHits,
        myMove: v.myMove, myMoveUsageRate: v.myMove ? subjectMaj.get(v.myMove) ?? null : null,
        myMovePrio: prioOf(v.myMove),
        oppMove: v.oppMove, oppMoveUsageRate: v.oppMove ? oppMaj.get(v.oppMove) ?? null : null,
        oppMovePrio: prioOf(v.oppMove),
        myPctLo: r1(d.my?.pctLo), myPctHi: r1(d.my?.pctHi),
        oppPctLo: r1(d.opp?.pctLo), oppPctHi: r1(d.opp?.pctHi),
        myDmgLo: d.my?.dmgLo ?? null, myDmgHi: d.my?.dmgHi ?? null,
        oppDmgLo: d.opp?.dmgLo ?? null, oppDmgHi: d.opp?.dmgHi ?? null,
        myCertain: d.my?.certain ?? null, oppCertain: d.opp?.certain ?? null,
        myProb: d.my?.prob ?? null, oppProb: d.opp?.prob ?? null,
        myProbInt: d.my && d.my.prob != null ? fmtKoProbPct(d.my.prob) : null,
        oppProbInt: d.opp && d.opp.prob != null ? fmtKoProbPct(d.opp.prob) : null,
        myReason: d.my?.reason ?? null, oppReason: d.opp?.reason ?? null,
        myEff: d.my?.eff ?? null, oppEff: d.opp?.eff ?? null,
        mySeq: v.mySeq ?? [],
        oppSeq: v.oppSeq ?? [],
        myKoMove: koMoveOf(v.race, 0), myKoMovePrio: prioOf(koMoveOf(v.race, 0)),
        oppKoMove: koMoveOf(v.race, 1), oppKoMovePrio: prioOf(koMoveOf(v.race, 1)),
        oppItem: opp.item,
      });
    }
  }

  const noMyAttack = subjectBuilds.some((b) => !hasAttack(b));
  const noOppAttack = oppBuilds.some(({ rb }) => !hasAttack(rb));
  const stall = rows.some((r) => (r.myHits ?? OUT_OF_RANGE) >= OUT_OF_RANGE
                              && (r.oppHits ?? OUT_OF_RANGE) >= OUT_OF_RANGE);
  const wins = new Set(rows.map((r) => r.win));

  const base = {
    name: g.label ?? g.sp,
    sp: g.sp,
    icon: g.icon,
    ...(g.stone ? { stone: g.stone } : {}),
    allRows: rows,
  };

  if (noMyAttack || noOppAttack || stall || wins.size > 1) {
    const reasons: string[] = [];
    if (noMyAttack) reasons.push("自分側に多数派の攻撃技が無い");
    if (noOppAttack) reasons.push("相手側に多数派の攻撃技が無い");
    if (stall) reasons.push("多数派技では互いに倒しきれない(決着しない)");
    if (wins.size > 1) reasons.push("代表型によって勝敗が割れる");
    mixed.push({ ...base, verdict: "mixed", reasons });
    continue;
  }

  const win = [...wins][0];
  const rank = (r: BuildRow) => (r.oppHits ?? OUT_OF_RANGE) - (r.myHits ?? OUT_OF_RANGE);
  const rep = [...rows].sort((a, b) => win ? rank(a) - rank(b) : rank(b) - rank(a))[0];
  ok.push({ ...base, verdict: win ? "win" : "lose", representative: rep });
}

console.log(JSON.stringify({
  subject: {
    icon: SUBJECT_ICON, name: subjectMon.n,
    majorityMoves: [...subjectMaj].map(([n, pct]) => ({ n, pct })),
    builds: subjectBuilds.map(sideFields),
  },
  majorityPct: MAJORITY_PCT,
  oppItemMajority: OPP_ITEM_MAJORITY,
  builderVersion,
  publishable: ok,
  excluded: mixed,
}, null, 2));
