// suggestFill()/tuneForTargets() — 提案・逆算層。
// suggestFill は product3_server.py の POST /complete {specs,fill,top} に接続し、
// 接続不可・タイムアウト・パース失敗時のみ擬似遅延スタブにフォールバックする。
// tuneForTargetsの素早さ逆算のみ現時点で本物（変更なし）。
import type { MonDetail, Party, ResolvedBuild, Slot, SpeciesMaster, StatArray, TuneSuggestion } from "./types";
import { fromSpec, toSpec } from "./spec";
import { speciesByName } from "./data";
import { EV_STAT_MAX, EV_TOTAL_MAX, calcStat, effectiveSpeed, natureMod, realStats } from "./stats";
import { judge1v1 } from "./matchup";

export interface SuggestDeps {
  species: SpeciesMaster[];
  loadMon: (icon: string) => Promise<MonDetail>;
}

function partyUsedNames(party: Party): Set<string> {
  const s = new Set<string>();
  for (const slot of party.slots) {
    if (slot && slot.sp) s.add(slot.sp);
  }
  return s;
}

const API_TIMEOUT_MS = 15000;

/** PartySuggestApp.astro と同じ判定式(本番ドメインはCloud Run、それ以外はローカルAPI)。 */
function apiBase(): string {
  return /(^|\.)pokenavi\.jp$/.test(location.hostname)
    ? "https://pokenavi-suggest-799947701075.asia-northeast1.run.app"
    : "http://localhost:8899";
}

/**
 * 空き枠への提案スタブ(フォールバック用)。600msの擬似遅延の後、パーティ未使用の使用率上位種から
 * mon json の builds[0](使用率最多の型)を適用した案を2〜3件返す。
 * 各案は emptyIdx と同じ長さの配列(emptyIdx[i]に対応する枠のSlot)。
 */
async function suggestFillStub(party: Party, emptyIdx: number[], deps: SuggestDeps): Promise<Slot[][]> {
  await new Promise((resolve) => setTimeout(resolve, 600));

  if (emptyIdx.length === 0) return [];

  const used = partyUsedNames(party);
  const candidates = [...deps.species].filter((s) => !used.has(s.n)).sort((a, b) => a.rank - b.rank);

  const need = emptyIdx.length;
  const proposalCount = Math.min(3, Math.max(1, Math.ceil(candidates.length / need)));
  const proposals: Slot[][] = [];

  let cursor = 0;
  for (let p = 0; p < proposalCount && proposals.length < 3; p++) {
    const slots: Slot[] = [];
    for (let i = 0; i < need; i++) {
      if (cursor >= candidates.length) break;
      const sp = candidates[cursor];
      cursor++;
      const detail = await deps.loadMon(sp.icon);
      const built = detail.builds.length ? fromSpec(detail.builds[0]) : null;
      slots.push(
        built ?? {
          sp: sp.n,
          item: "",
          ability: "",
          nature: "",
          evs: [0, 0, 0, 0, 0, 0],
          moves: [],
          targets: [],
        }
      );
    }
    if (slots.length === need) proposals.push(slots);
  }
  return proposals;
}

/**
 * /complete への実API接続。1件でも整合した提案が取れれば結果を返し、
 * 接続不可・タイムアウト・不正レスポンスの場合は null を返す(呼び出し側でスタブにフォールバック)。
 */
async function suggestFillApi(party: Party, emptyIdx: number[]): Promise<Slot[][] | null> {
  const filled = party.slots.filter((s): s is Slot => !!s);
  const fill = emptyIdx.length;
  if (fill < 1 || filled.length > 5 || filled.length + fill > 6) return null;

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), API_TIMEOUT_MS);
  try {
    const res = await fetch(`${apiBase()}/complete`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ specs: filled.map(toSpec), fill, top: 3 }),
      signal: controller.signal,
    });
    if (!res.ok) return null;
    const data = await res.json();
    if (!data || data.error || !Array.isArray(data.results)) return null;

    const proposals: Slot[][] = [];
    for (const r of data.results) {
      if (!r || !Array.isArray(r.specs) || r.specs.length !== fill) continue;
      const slots = r.specs.map((s: unknown) => (typeof s === "string" ? fromSpec(s) : null));
      if (slots.some((s: Slot | null) => s === null)) continue;
      proposals.push(slots as Slot[]);
    }
    return proposals.length ? proposals : null;
  } catch {
    return null;
  } finally {
    clearTimeout(timer);
  }
}

/**
 * 空き枠への提案。実API(/complete)接続を優先し、接続不可・タイムアウト(15s)・パース失敗時は
 * 現行スタブ(suggestFillStub)にフォールバックする(UIは変更なし)。
 */
export async function suggestFill(party: Party, emptyIdx: number[], deps: SuggestDeps): Promise<Slot[][]> {
  if (emptyIdx.length === 0) return [];

  try {
    const apiResult = await suggestFillApi(party, emptyIdx);
    if (apiResult) return apiResult;
    console.warn("[suggestFill] API結果が空または不正のため、スタブ提案にフォールバックします");
  } catch (e) {
    console.warn("[suggestFill] API呼び出しに失敗したため、スタブ提案にフォールバックします", e);
  }
  return suggestFillStub(party, emptyIdx, deps);
}

/** 最速に振れる代表的な性格(攻撃系統の異なる2種から到達可能な方を提案) */
const SPEED_NATURES = ["おくびょう", "ようき"];

/**
 * 素の種族値Sを resolved の元になった種族マスタから取得する(メガ解決込み)。
 * 注(UI連携): これには data.ts の loadCore() で species キャッシュが populate 済みであることが前提。
 * ページ初期化で loadCore() を待ってから呼ぶこと。
 */
function baseSpeedOf(slot: Slot, resolved: ResolvedBuild): number | null {
  const sm = speciesByName(slot.sp);
  if (!sm) return null;
  if (resolved.mega) {
    const mega = sm.mega.find((m) => m.stone === slot.item);
    return mega ? mega.bs[5] : sm.bs[5];
  }
  return sm.bs[5];
}

/** slot/resolvedの元になった種族マスタから種族値6つ(メガ解決込み)を取得する。baseSpeedOfの汎化版。 */
function baseStatsOf(slot: Slot, resolved: ResolvedBuild): StatArray | null {
  const sm = speciesByName(slot.sp);
  if (!sm) return null;
  if (resolved.mega) {
    const mega = sm.mega.find((m) => m.stone === slot.item);
    return mega ? mega.bs : sm.bs;
  }
  return sm.bs;
}

function minEvForThreshold(baseSpeed: number, nature: string, threshold: number): number | null {
  for (let ev = 0; ev <= EV_STAT_MAX; ev++) {
    const s = calcStat(baseSpeed, ev, 31, natureMod(nature, 5));
    if (s >= threshold) return ev;
  }
  return null;
}

/** evs のうち statIdx 以外の合計(EV合計66制約の残り予算を出すため)。 */
function evTotalExcluding(evs: StatArray, ...excludeIdx: number[]): number {
  return evs.reduce((sum, v, i) => (excludeIdx.includes(i) ? sum : sum + v), 0);
}

/** resolved を、種族値bsと新しいevsから実数値を再計算した状態で複製する(EV総当たり探索用のプローブ)。 */
function withEvs(resolved: ResolvedBuild, bs: StatArray, nature: string, evs: StatArray): ResolvedBuild {
  return { ...resolved, evs, stats: realStats(bs, evs, nature) };
}

const EV_STAT_KEYS = ["H", "A", "B", "C", "D", "S"] as const;

/** ko/survive の提案不能理由の分類。集約表示(summarizeFails)のグルーピングキーにも使う。 */
type TuneReasonKind = "no-move" | "already-max" | "budget-exhausted" | "no-improvement" | "already-safe";

interface TuneOk {
  ok: true;
  suggestion: TuneSuggestion;
}
interface TuneFail {
  ok: false;
  reason: TuneReasonKind;
  /** 対象ラベルを含まない理由文(集約時に使い回すため)。 */
  text: string;
}
type TuneAttempt = TuneOk | TuneFail;

/**
 * 攻撃EV(A or C。judge1v1の現在のmyMoveの分類で決める)を0〜32総当たりし、
 * targetに対する確定数(myHits)が現在より縮む最小EVを探す。
 * 通常のEV合計66残り予算だけでなく、逆側の攻撃ステ(物理型ならC、特殊型ならA)を削って
 * 充当する振り替えも許可する(振り替え原資はこの1種のみ)。見つからない場合は理由を返す。
 */
function findKoSuggestion(slot: Slot, resolved: ResolvedBuild, bs: StatArray, target: ResolvedBuild): TuneAttempt {
  const baseline = judge1v1(resolved, target);
  if (baseline.myMove === null) {
    return { ok: false, reason: "no-move", text: "自分に有効な攻撃技がなく、EVでは改善できません" };
  }
  const baselineHits = baseline.myHits ?? 999;
  const usedMove = resolved.moves.find((m) => m.n === baseline.myMove);
  if (!usedMove || usedMove.cat === "status") {
    return { ok: false, reason: "no-move", text: "自分に有効な攻撃技がなく、EVでは改善できません" };
  }
  const statIdx = usedMove.cat === "physical" ? 1 : 3;
  const oppIdx = usedMove.cat === "physical" ? 3 : 1;
  const key = EV_STAT_KEYS[statIdx];
  const oppKey = EV_STAT_KEYS[oppIdx];
  const curEv = resolved.evs[statIdx];
  const oppCur = resolved.evs[oppIdx];

  if (curEv >= EV_STAT_MAX) {
    return { ok: false, reason: "already-max", text: `${key}は最大です。EVでは確定数を縮められません` };
  }

  // otherSum: statIdx・oppIdx以外(H,B,D,Sのうちこの2つを除いたもの)のEV合計。振り替え原資(oppIdx)は
  // 0まで解放できる前提で、statIdxが到達しうる理論上限を maxReachable として求める。
  const otherSum = evTotalExcluding(resolved.evs, statIdx, oppIdx);
  const maxReachable = Math.min(EV_STAT_MAX, EV_TOTAL_MAX - otherSum);

  if (maxReachable <= curEv) {
    return { ok: false, reason: "budget-exhausted", text: `EV合計上限(66)のため${key}を上げる振り替え先がありません` };
  }

  for (let ev = curEv + 1; ev <= maxReachable; ev++) {
    // oppIdxをこのevに対して許される最大値まで残す(必要な分だけ削る。0まで無条件に削らない)。
    const oppAllowed = EV_TOTAL_MAX - otherSum - ev;
    const oppNew = Math.min(oppCur, oppAllowed);
    const evs = [...resolved.evs] as StatArray;
    evs[statIdx] = ev;
    evs[oppIdx] = oppNew;
    const probe = withEvs(resolved, bs, slot.nature, evs);
    const v = judge1v1(probe, target);
    const vHits = v.myHits ?? 999;
    if (vHits < baselineHits) {
      const sacrificed = oppNew < oppCur;
      const text = sacrificed
        ? `${target.label}に対し ${oppKey}${oppCur}→${oppKey}${oppNew}に振り替えて${key}${curEv}→${key}${ev}にすると、確${baselineHits}→確${vHits}に短縮できます`
        : `${target.label}に対し ${key}${ev}(${key}+${ev - curEv}) で確${baselineHits}→確${vHits}に短縮できます`;
      return { ok: true, suggestion: { kind: "ko", text, evs, stub: false } };
    }
  }
  return { ok: false, reason: "no-improvement", text: `${key}${maxReachable}まで振っても確定数は変わりません` };
}

/**
 * HP・防御(相手のoppMoveの分類に応じB or D)のEVを総当たりし、targetの攻撃に対する
 * 被弾確定数(oppHits)が現在より伸びる最小の追加EV合計を探す(H・防御同時探索)。
 * 通常のEV合計66残り予算だけでなく、自分の逆側攻撃ステ(judge1v1のmyMoveの分類と逆側。
 * 物理型ならC、特殊型ならA)を削って充当する振り替えも許可する(振り替え原資はこの1種のみ)。
 * 見つからない場合は理由を返す。
 */
function findSurviveSuggestion(slot: Slot, resolved: ResolvedBuild, bs: StatArray, target: ResolvedBuild): TuneAttempt {
  const baseline = judge1v1(resolved, target);
  if (baseline.oppMove === null) {
    return { ok: false, reason: "no-move", text: "相手に有効な攻撃技がなく、耐久調整の意味がありません" };
  }
  const baselineHits = baseline.oppHits ?? 999;
  if (baselineHits >= 999) {
    return { ok: false, reason: "already-safe", text: "既に相手の攻撃で確定では倒されません(調整不要です)" };
  }
  const usedMove = target.moves.find((m) => m.n === baseline.oppMove);
  if (!usedMove || usedMove.cat === "status") {
    return { ok: false, reason: "no-move", text: "相手に有効な攻撃技がなく、耐久調整の意味がありません" };
  }
  const defIdx = usedMove.cat === "physical" ? 2 : 4;
  const defKey = EV_STAT_KEYS[defIdx];

  // 振り替え原資: 自分の攻撃側の不使用ステータス(judge1v1のmyMoveの分類と逆側)。
  // 自分に有効な攻撃技が無い場合は振り替え原資なし(通常の残り予算のみで探索)。
  let atkIdx: number | null = null;
  if (baseline.myMove !== null) {
    const myUsed = resolved.moves.find((m) => m.n === baseline.myMove);
    if (myUsed && myUsed.cat !== "status") {
      atkIdx = myUsed.cat === "physical" ? 3 : 1;
    }
  }
  const atkKey = atkIdx !== null ? EV_STAT_KEYS[atkIdx] : null;

  const curH = resolved.evs[0];
  const curD = resolved.evs[defIdx];
  const atkCur = atkIdx !== null ? resolved.evs[atkIdx] : 0;

  if (curH >= EV_STAT_MAX && curD >= EV_STAT_MAX) {
    return { ok: false, reason: "already-max", text: `H・${defKey}は最大です。EVでは被弾数を伸ばせません` };
  }

  const otherSum = evTotalExcluding(resolved.evs, 0, defIdx, ...(atkIdx !== null ? [atkIdx] : []));
  const plainBudget = EV_TOTAL_MAX - otherSum - atkCur; // 振り替えなしで使える上限(従来のbudget相当)
  const reallocBudget = EV_TOTAL_MAX - otherSum; // 振り替え(atkIdxを0まで解放)込みで使える上限
  const maxCost = Math.min(EV_STAT_MAX * 2, reallocBudget);

  if (maxCost <= curH + curD) {
    return { ok: false, reason: "budget-exhausted", text: `EV合計上限(66)のためH・${defKey}を上げる振り替え先がありません` };
  }

  for (let cost = curH + curD; cost <= maxCost; cost++) {
    for (let h = Math.max(curH, cost - EV_STAT_MAX); h <= Math.min(EV_STAT_MAX, cost); h++) {
      const d = cost - h;
      if (d < curD || d > EV_STAT_MAX) continue;
      const extra = Math.max(0, cost - plainBudget); // 通常予算を超えた分だけ振り替え原資から充当
      if (atkIdx === null && extra > 0) continue;
      const atkNew = atkCur - extra;
      if (atkNew < 0) continue;
      const evs = [...resolved.evs] as StatArray;
      evs[0] = h;
      evs[defIdx] = d;
      if (atkIdx !== null) evs[atkIdx] = atkNew;
      const probe = withEvs(resolved, bs, slot.nature, evs);
      const v = judge1v1(probe, target);
      const vHits = v.oppHits ?? 999;
      if (vHits > baselineHits) {
        const sacrificed = atkIdx !== null && atkNew < atkCur;
        const text = sacrificed
          ? `${target.label}の攻撃に対し ${atkKey}${atkCur}→${atkKey}${atkNew}に振り替えてH${h} ${defKey}${d}にすると、被弾${baselineHits}→${vHits}に耐えられます`
          : `${target.label}の攻撃に対し H${h} ${defKey}${d} で被弾${baselineHits}→${vHits}に耐えられます`;
        return { ok: true, suggestion: { kind: "survive", text, evs, stub: false } };
      }
    }
  }
  return { ok: false, reason: "no-improvement", text: `H・${defKey}を上限まで振っても被弾数は変わりません` };
}

/**
 * ko/surviveの提案不能理由を仮想敵ごとに集約する。
 * 1件のみなら対象名つきでそのまま1行、複数件なら理由文でグルーピングし、件数の多い順に
 * 最大2行(「その他の型: 理由」)に圧縮する(仮想敵の数だけ理由行が増えるのを防ぐため)。
 */
function summarizeFails(fails: { label: string; text: string }[], kind: "ko" | "survive"): TuneSuggestion[] {
  if (fails.length === 0) return [];
  if (fails.length === 1) {
    return [{ kind, text: `${fails[0].label}: ${fails[0].text}`, stub: false }];
  }
  const groups = new Map<string, number>();
  for (const f of fails) groups.set(f.text, (groups.get(f.text) ?? 0) + 1);
  const sorted = [...groups.entries()].sort((a, b) => b[1] - a[1]).slice(0, 2);
  return sorted.map(([text, count]) => ({
    kind,
    text: count > 1 ? `その他の型(${count}件): ${text}` : `その他の型: ${text}`,
    stub: false,
  }));
}

/**
 * 素早さ・確定数・耐久調整の逆算(すべて本実装)。
 * speed: 対象群のうち最速の実効S+1以上になる最小のS EV(0-32総当たり)を現在の性格で探す。
 *   現性格で32振っても届かない場合は最速性格(おくびょう/ようき)での到達可否を追加提案する。
 * ko: 選択中の仮想敵ごとに、judge1v1のmyMoveが使う攻撃EV(A or C)を総当たりし、
 *   確定数(myHits)が縮む最小EVを提案する(findKoSuggestion)。通常予算で足りない場合は
 *   逆側攻撃ステからの振り替えも試す。改善が見つからない対象は理由を集約して表示する。
 * survive: 選択中の仮想敵ごとに、judge1v1のoppMoveが使う耐久EV(H・B or D)を総当たりし、
 *   被弾確定数(oppHits)が伸びる最小の追加EV合計を提案する(findSurviveSuggestion)。
 *   同様に逆側攻撃ステからの振り替えを試し、見つからない対象は理由を集約して表示する。
 */
export function tuneForTargets(slot: Slot, resolved: ResolvedBuild, targets: ResolvedBuild[]): TuneSuggestion[] {
  const out: TuneSuggestion[] = [];
  if (targets.length === 0) return out;

  const oppMaxS = Math.max(...targets.map((t) => effectiveSpeed(t.stats[5], t.item)));
  const threshold = oppMaxS + 1;

  const baseSpeed = baseSpeedOf(slot, resolved);
  if (baseSpeed !== null) {
    const found = minEvForThreshold(baseSpeed, slot.nature, threshold);
    if (found !== null) {
      out.push({
        kind: "speed",
        text: `現在の性格のままS${found}振りで、想定敵(最速S${oppMaxS})を抜けます`,
        evs: [slot.evs[0], slot.evs[1], slot.evs[2], slot.evs[3], slot.evs[4], found],
        stub: false,
      });
    } else {
      let bestNature: string | null = null;
      let bestEv: number | null = null;
      for (const nat of SPEED_NATURES) {
        const ev = minEvForThreshold(baseSpeed, nat, threshold);
        if (ev !== null && (bestEv === null || ev < bestEv)) {
          bestEv = ev;
          bestNature = nat;
        }
      }
      if (bestNature !== null && bestEv !== null) {
        out.push({
          kind: "speed",
          text: `現在の性格ではS32振りでも届きません。性格を${bestNature}にすればS${bestEv}振りで想定敵(最速S${oppMaxS})を抜けます`,
          evs: [slot.evs[0], slot.evs[1], slot.evs[2], slot.evs[3], slot.evs[4], bestEv],
          stub: false,
        });
      } else {
        out.push({
          kind: "speed",
          text: `最速性格・S32振りでも想定敵(最速S${oppMaxS})を抜けません`,
          stub: false,
        });
      }
    }
  }

  const bs = baseStatsOf(slot, resolved);
  if (bs !== null) {
    const koAttempts = targets.map((t) => ({ label: t.label, attempt: findKoSuggestion(slot, resolved, bs, t) }));
    const koOk = koAttempts.filter((a): a is { label: string; attempt: TuneOk } => a.attempt.ok);
    const koFail = koAttempts.filter((a): a is { label: string; attempt: TuneFail } => !a.attempt.ok);
    out.push(...koOk.map((a) => a.attempt.suggestion));
    out.push(...summarizeFails(koFail.map((a) => ({ label: a.label, text: a.attempt.text })), "ko"));

    const surviveAttempts = targets.map((t) => ({ label: t.label, attempt: findSurviveSuggestion(slot, resolved, bs, t) }));
    const surviveOk = surviveAttempts.filter((a): a is { label: string; attempt: TuneOk } => a.attempt.ok);
    const surviveFail = surviveAttempts.filter((a): a is { label: string; attempt: TuneFail } => !a.attempt.ok);
    out.push(...surviveOk.map((a) => a.attempt.suggestion));
    out.push(...summarizeFails(surviveFail.map((a) => ({ label: a.label, text: a.attempt.text })), "survive"));
  }

  return out;
}
