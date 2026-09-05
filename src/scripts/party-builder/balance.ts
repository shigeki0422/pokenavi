// パーティバランス集計(攻撃/防御マトリクス・素早さ順・summary)【本物】
//
// 注(UI連携): attackMatrix/defenseMatrix/speedOrder/partySummary/resolveTarget は
// 生のPartyではなく ResolvedBuild[] を受け取る。マトリクス計算にはメガ解決後の
// t1/t2/技/実数値が必要で、それは resolveSlot() の出力そのものだから。
// UI側は「埋まっている枠だけ resolveSlot(slot, species, moves) した配列」を渡すこと。
import type { MoveDict, ResolvedBuild, SpeciesMaster, Slot, TargetBuild } from "./types";
import { effectiveSpeed, realStats } from "./stats";
import { eff, TYPES } from "./typechart";
import { judgeVsBuilds } from "./matchup";

export function resolveSlot(slot: Slot, species: SpeciesMaster[], moves: MoveDict): ResolvedBuild {
  const sm = species.find((s) => s.n === slot.sp);
  if (!sm) throw new Error(`resolveSlot: 種族データが見つかりません: ${slot.sp}`);

  const megaOpt = slot.item ? sm.mega.find((m) => m.stone === slot.item) : undefined;
  const t1 = megaOpt ? megaOpt.t1 : sm.t1;
  const t2 = megaOpt ? megaOpt.t2 : sm.t2;
  const bs = megaOpt ? megaOpt.bs : sm.bs;
  const ability = megaOpt && megaOpt.ability ? megaOpt.ability : slot.ability;

  const stats = realStats(bs, slot.evs, slot.nature);

  const resolvedMoves = (slot.moves || [])
    .map((n) => {
      const md = moves[n];
      if (!md) return null;
      return { n, type: md[0], cat: md[1], power: md[2] };
    })
    .filter((m): m is NonNullable<typeof m> => m !== null);

  return {
    sp: slot.sp,
    label: megaOpt ? megaOpt.name : sm.n,
    t1,
    t2,
    stats,
    item: slot.item,
    ability,
    nature: slot.nature,
    evs: slot.evs,
    moves: resolvedMoves,
    mega: !!megaOpt,
    icon: sm.icon,
  };
}

/** targets.json の1ビルドを ResolvedBuild 相当に解決する(bs/タイプは既に解決済みなのでメガ判定不要)。 */
export function resolveTarget(sp: string, label: string, icon: string, build: TargetBuild, moves: MoveDict): ResolvedBuild {
  const stats = realStats(build.bs, build.ev, build.nature);
  const resolve = (names: string[]) =>
    names
      .map((n) => {
        const md = moves[n];
        if (!md) return null;
        return { n, type: md[0], cat: md[1], power: md[2] };
      })
      .filter((m): m is NonNullable<typeof m> => m !== null);
  const resolvedMoves = resolve(build.moves);
  // mpool(採用率TOP10)があれば1v1判定用の技プールとして持たせる。工房でユーザーが
  // 編集した仮想敵(customTargets)にはmpoolが無く、その場合は指定4技だけで判定される。
  const pool = build.mpool && build.mpool.length ? resolve(build.mpool) : undefined;
  return {
    pool,
    sp,
    label,
    t1: build.t1,
    t2: build.t2,
    stats,
    item: build.item,
    ability: build.ability,
    nature: build.nature,
    evs: build.ev,
    moves: resolvedMoves,
    mega: false,
    icon,
  };
}

/**
 * resolveTarget の防御版。customTargets(localStorage由来)に不整合データが混入していても
 * throwせずnullを返す(H2のsanitizeで大半は防げるが、二層防御として呼び出し側は必ずこちら経由にする)。
 */
export function resolveTargetSafe(sp: string, label: string, icon: string, build: TargetBuild, moves: MoveDict): ResolvedBuild | null {
  try {
    return resolveTarget(sp, label, icon, build, moves);
  } catch (e) {
    return null;
  }
}

function isAttacking(m: ResolvedBuild["moves"][number]): boolean {
  return m.cat !== "status" && typeof m.power === "number" && (m.power as number) > 0;
}

export interface TypeMatrix {
  types: readonly string[];
  cells: (number | null)[][]; // cells[memberIndex][typeIndex]
}

/** 各メンバーが攻撃技で各タイプに通せる最大倍率。攻撃技を持たないメンバーは全typeでnull。 */
export function attackMatrix(party: ResolvedBuild[]): TypeMatrix {
  const cells: (number | null)[][] = party.map((b) => {
    const atkMoves = b.moves.filter(isAttacking);
    if (atkMoves.length === 0) return TYPES.map(() => null);
    return TYPES.map((defType) => {
      let best = 0;
      for (const mv of atkMoves) {
        const e = eff(mv.type, defType, null);
        if (e > best) best = e;
      }
      return best;
    });
  });
  return { types: TYPES, cells };
}

/** 各メンバーが各タイプの攻撃技を受けたときの被弾倍率。 */
export function defenseMatrix(party: ResolvedBuild[]): TypeMatrix {
  const cells: (number | null)[][] = party.map((b) => TYPES.map((atkType) => eff(atkType, b.t1, b.t2)));
  return { types: TYPES, cells };
}

export interface SpeedRow {
  sp: string;
  label: string;
  speed: number;
}

/** 有効素早さ(こだわりスカーフ込み)降順のリスト。 */
export function speedOrder(party: ResolvedBuild[]): SpeedRow[] {
  return party
    .map((b) => ({ sp: b.sp, label: b.label, speed: effectiveSpeed(b.stats[5], b.item) }))
    .sort((a, b) => b.speed - a.speed);
}

export interface PartySummary {
  physical: number;
  special: number;
  mega: number;
  scarf: number;
  avgSpeed: number;
  weakOverlap: { type: string; count: number };
}

export function partySummary(party: ResolvedBuild[]): PartySummary {
  const physical = party.filter((b) => b.moves.some((m) => m.cat === "physical" && isAttacking(m))).length;
  const special = party.filter((b) => b.moves.some((m) => m.cat === "special" && isAttacking(m))).length;
  const mega = party.filter((b) => b.mega).length;
  const scarf = party.filter((b) => b.item === "こだわりスカーフ").length;
  const speeds = party.map((b) => effectiveSpeed(b.stats[5], b.item));
  const avgSpeed = speeds.length ? speeds.reduce((a, b) => a + b, 0) / speeds.length : 0;

  const def = defenseMatrix(party);
  let worstType = TYPES[0] as string;
  let worstCount = -1;
  TYPES.forEach((t, ti) => {
    const count = def.cells.reduce((acc, row) => acc + ((row[ti] ?? 0) >= 2 ? 1 : 0), 0);
    if (count > worstCount) {
      worstCount = count;
      worstType = t;
    }
  });

  return {
    physical,
    special,
    mega,
    scarf,
    avgSpeed,
    weakOverlap: { type: worstType, count: Math.max(0, worstCount) },
  };
}

export interface OppCol {
  label: string;
  /** その相手の想定型(≤3、targets.jsonのbuilds全部をresolveTarget済み)。matchup_gridと同じ集約対象。 */
  builds: ResolvedBuild[];
}

export interface HoleInfo {
  /** 誰も集約◎/○を取れない相手のラベル一覧(表示順はoppColsの順) */
  holeLabels: string[];
  /** oppCols中で「穴」に該当するインデックス集合 */
  holeIdx: Set<number>;
}

/**
 * パーティの「穴」判定: 代表型1体ではなく、相手の複数型(≤3)を集約したシンボル(judgeVsBuilds)で判定する。
 * matchup_grid と同じ意味論: 誰も集約◎/○を取れない相手＝穴。party内の誰か1体でも集約◎/○を取れれば穴ではない。
 */
export function findHoles(party: ResolvedBuild[], oppCols: OppCol[]): HoleInfo {
  const holeLabels: string[] = [];
  const holeIdx = new Set<number>();
  oppCols.forEach((o, ci) => {
    const covered = party.some((b) => {
      const agg = judgeVsBuilds(b, o.builds);
      return agg.sym === "◎" || agg.sym === "○";
    });
    if (!covered) {
      holeLabels.push(o.label);
      holeIdx.add(ci);
    }
  });
  return { holeLabels, holeIdx };
}

/**
 * 1体(味方 or 「穴を埋める候補」の候補種)が oppCols の何列目を集約◎/○で取れるかの集合。
 * findHoles と同じ判定条件(judgeVsBuildsのsymが◎/○)を1体単位で返す版。「穴を埋める候補」機能で
 * party各メンバー・候補種(最大50)双方に使う(judgeVsBuildsの呼び出しをこの1回に閉じ込め、
 * 入れ替え探索側は集合演算のみで行う)。
 */
export function coverageSet(build: ResolvedBuild, oppCols: OppCol[]): Set<number> {
  const s = new Set<number>();
  oppCols.forEach((o, ci) => {
    const agg = judgeVsBuilds(build, o.builds);
    if (agg.sym === "◎" || agg.sym === "○") s.add(ci);
  });
  return s;
}

/**
 * partyの各メンバー(coverageSets、findHolesと同じ並び)について、「そのメンバーを外すと
 * 露出する列(=そのメンバー以外に誰も集約◎/○を取れていない列)」を求める。
 * 「穴を埋める候補」の入れ替え探索(6×候補数)をjudgeVsBuilds再計算無しの集合演算だけで行うための前処理。
 */
export function exposedOnRemoval(coverageSets: Set<number>[], oppColsLen: number): Set<number>[] {
  const coverCount = new Array(oppColsLen).fill(0);
  coverageSets.forEach((s) => s.forEach((ci) => { coverCount[ci]++; }));
  return coverageSets.map((s) => {
    const exposed = new Set<number>();
    s.forEach((ci) => { if (coverCount[ci] === 1) exposed.add(ci); });
    return exposed;
  });
}

/**
 * 「現状の穴集合(holeIdx)」から、1体を外した際に露出する列(exposed)を穴に加え、
 * 代わりに入れる候補のカバレッジ(candCov)で埋まる列を穴から除いた、入れ替え後の穴集合を返す。
 * judgeVsBuildsを一切呼ばない純粋な集合演算(「穴を埋める候補」の入れ替え探索の中核)。
 */
export function holesAfterSwap(holeIdx: Set<number>, exposed: Set<number>, candCov: Set<number>): Set<number> {
  const after = new Set<number>(holeIdx);
  exposed.forEach((ci) => after.add(ci));
  candCov.forEach((ci) => after.delete(ci));
  return after;
}

/** 防御相性タブ用: 「全員が等倍以上で受ける(半減以下の受け手がいない)」タイプのインデックス集合。 */
export function findWeakGapTypeIdx(party: ResolvedBuild[]): Set<number> {
  const dm = defenseMatrix(party);
  const gapIdx = new Set<number>();
  TYPES.forEach((_, ti) => {
    const hasResist = dm.cells.some((row) => (row[ti] ?? 1) < 1);
    if (!hasResist) gapIdx.add(ti);
  });
  return gapIdx;
}
