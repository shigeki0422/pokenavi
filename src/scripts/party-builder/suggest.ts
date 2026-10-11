// tuneForTargets() — EV逆算層。
//
// 空き枠の候補出し(旧 suggestFill)はここから外した。Cloud Run の /complete を押すたびに
// 呼んでいて日々課金が発生するうえ、返るのは6匹の並びだけで採用理由が分からなかった。
// いまは「穴を埋める候補」と同じ材料でブラウザ内のエンジンだけを使って選ぶ
// (PartyBuilderApp.astro の computeFillPicks)。
// tuneForTargetsの素早さ逆算のみ現時点で本物（変更なし）。
import type { ResolvedBuild, Slot, SlotScenario, StatArray, TuneSuggestion } from "./types";
import { speciesByName } from "./data";
import { EV_STAT_MAX, EV_TOTAL_MAX, realStats } from "./stats";
import { judge1v1, moveHitsRange } from "./matchup";
import { setScenario } from "../engine/wasm";
import type { Lang } from "./assumptions";

const TXT = {
  ja: {
    noMyMove: "自分に有効な攻撃技がなく、EVでは改善できません",
    atkMax: (k: string) => `${k}は最大です。EVでは確定数を縮められません`,
    atkBudget: (k: string) => `EV合計上限(66)のため${k}を上げる振り替え先がありません`,
    koRealloc: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, h0: number, h1: number) => `${l}に対し ${ok}${oc}→${ok}${on}に振り替えて${k}${c}→${k}${e}にすると、確${h0}→確${h1}に短縮できます`,
    koPlain: (l: string, k: string, e: number, d: number, h0: number, h1: number) => `${l}に対し ${k}${e}(${k}+${d}) で確${h0}→確${h1}に短縮できます`,
    // 確定(最低乱数)では縮まらないが、中央乱数では縮む場合の控えめな提案。確定数自体は変わらないことを明記する。
    koReallocRandom: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, mid: number, probTxt: string) => `${l}に対し ${ok}${oc}→${ok}${on}に振り替えて${k}${c}→${k}${e}にすると、乱数${mid}発(${probTxt})に縮まることがあります（確定数は変わりません）`,
    koPlainRandom: (l: string, k: string, e: number, d: number, mid: number, probTxt: string) => `${l}に対し ${k}${e}(${k}+${d}) で乱数${mid}発(${probTxt})に縮まることがあります（確定数は変わりません）`,
    atkNoImprove: (k: string, m: number) => `${k}${m}まで振っても確定数は変わりません`,
    noOppMove: "相手に有効な攻撃技がなく、耐久調整の意味がありません",
    alreadySafe: "既に相手の攻撃で確定では倒されません(調整不要です)",
    defMax: (k: string) => `H・${k}は最大です。EVでは確定で耐えられる発数を伸ばせません`,
    defBudget: (k: string) => `EV合計上限(66)のためH・${k}を上げる振り替え先がありません`,
    surviveRealloc: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, h0: number, h1: number) => `${l}の攻撃に対し ${ak}${ac}→${ak}${an}に振り替えてH${h} ${k}${d}にすると、確定で${h0}→${h1}発目まで耐えられます`,
    survivePlain: (l: string, h: number, k: string, d: number, h0: number, h1: number) => `${l}の攻撃に対し H${h} ${k}${d} で確定で${h0}→${h1}発目まで耐えられます`,
    // 確定(最高乱数)では伸びないが、中央乱数では伸びる場合の控えめな提案。
    surviveReallocRandom: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, mid: number, probTxt: string) => `${l}の攻撃に対し ${ak}${ac}→${ak}${an}に振り替えてH${h} ${k}${d}にすると、乱数では${mid}発目まで耐えられることがあります（相手の技が${mid}発以内に当たる確率${probTxt}。確定で耐えられる発数は変わりません）`,
    survivePlainRandom: (l: string, h: number, k: string, d: number, mid: number, probTxt: string) => `${l}の攻撃に対し H${h} ${k}${d} で、乱数では${mid}発目まで耐えられることがあります（相手の技が${mid}発以内に当たる確率${probTxt}。確定で耐えられる発数は変わりません）`,
    defNoImprove: (k: string) => `H・${k}を上限まで振っても確定で耐えられる発数は変わりません`,
    otherMany: (n: number, t: string) => `その他の型(${n}件): ${t}`,
    otherOne: (t: string) => `その他の型: ${t}`,
    speedNow: (ev: number, s: number) => `現在の性格のままS${ev}振りで、想定敵(最速S${s})を抜けます`,
    speedNature: (nat: string, ev: number, s: number) => `現在の性格ではS32振りでも届きません。性格を${nat}にすればS${ev}振りで想定敵(最速S${s})を抜けます`,
    speedNone: (s: number) => `最速性格・S32振りでも想定敵(最速S${s})を抜けません`,
  },
  en: {
    noMyMove: "You have no effective attacking move, so EVs can't improve this",
    atkMax: (k: string) => `${k} is already maxed; EVs can't reduce the hits to KO`,
    atkBudget: (k: string) => `No EVs left to move into ${k} (total cap 66)`,
    koRealloc: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, h0: number, h1: number) => `vs ${l}: moving ${ok}${oc}→${ok}${on} into ${k}${c}→${k}${e} turns a guaranteed ${h0}HKO into a guaranteed ${h1}HKO`,
    koPlain: (l: string, k: string, e: number, d: number, h0: number, h1: number) => `vs ${l}: ${k}${e} (${k}+${d}) turns a guaranteed ${h0}HKO into a guaranteed ${h1}HKO`,
    koReallocRandom: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, mid: number, probTxt: string) => `vs ${l}: moving ${ok}${oc}→${ok}${on} into ${k}${c}→${k}${e} sometimes gets a ${mid}HKO (${probTxt}) — the guaranteed count doesn't change`,
    koPlainRandom: (l: string, k: string, e: number, d: number, mid: number, probTxt: string) => `vs ${l}: ${k}${e} (${k}+${d}) sometimes gets a ${mid}HKO (${probTxt}) — the guaranteed count doesn't change`,
    atkNoImprove: (k: string, m: number) => `Even ${k}${m} doesn't change the guaranteed hits to KO`,
    noOppMove: "The opponent has no effective attacking move, so bulk tuning has no effect",
    alreadySafe: "The opponent's attacks already can't guarantee a KO (no tuning needed)",
    defMax: (k: string) => `H and ${k} are already maxed; EVs can't increase the guaranteed hits you survive`,
    defBudget: (k: string) => `No EVs left to move into H/${k} (total cap 66)`,
    surviveRealloc: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, h0: number, h1: number) => `vs ${l}'s attacks: moving ${ak}${ac}→${ak}${an} into H${h} ${k}${d} guarantees surviving through hit ${h1} instead of ${h0}`,
    survivePlain: (l: string, h: number, k: string, d: number, h0: number, h1: number) => `vs ${l}'s attacks: H${h} ${k}${d} guarantees surviving through hit ${h1} instead of ${h0}`,
    surviveReallocRandom: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, mid: number, probTxt: string) => `vs ${l}'s attacks: moving ${ak}${ac}→${ak}${an} into H${h} ${k}${d} sometimes survives through hit ${mid} (their move lands within ${mid} hits ${probTxt} of the time) — the guaranteed count doesn't change`,
    survivePlainRandom: (l: string, h: number, k: string, d: number, mid: number, probTxt: string) => `vs ${l}'s attacks: H${h} ${k}${d} sometimes survives through hit ${mid} (their move lands within ${mid} hits ${probTxt} of the time) — the guaranteed count doesn't change`,
    defNoImprove: (k: string) => `Even maxing H and ${k} doesn't change the guaranteed hits you survive`,
    otherMany: (n: number, t: string) => `Other sets (${n}): ${t}`,
    otherOne: (t: string) => `Other sets: ${t}`,
    speedNow: (ev: number, s: number) => `With your current nature, S${ev} outspeeds the targets (fastest S${s})`,
    speedNature: (nat: string, ev: number, s: number) => `S32 isn't enough with your current nature. With ${nat}, S${ev} outspeeds the targets (fastest S${s})`,
    speedNone: (s: number) => `Even a Speed-boosting nature with S32 can't outspeed the targets (fastest S${s})`,
  },
  ko: {
    noMyMove: "유효한 공격 기술이 없어 EV로는 개선할 수 없습니다",
    atkMax: (k: string) => `${k}가 이미 최대입니다. EV로는 확정수를 줄일 수 없습니다`,
    atkBudget: (k: string) => `EV 합계 상한(66) 때문에 ${k}로 옮길 여유가 없습니다`,
    koRealloc: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, h0: number, h1: number) => `${l} 상대로 ${ok}${oc}→${ok}${on}을 옮겨 ${k}${c}→${k}${e}로 하면 확정${h0}→확정${h1}로 줄일 수 있습니다`,
    koPlain: (l: string, k: string, e: number, d: number, h0: number, h1: number) => `${l} 상대로 ${k}${e}(${k}+${d})로 확정${h0}→확정${h1}로 줄일 수 있습니다`,
    koReallocRandom: (l: string, ok: string, oc: number, on: number, k: string, c: number, e: number, mid: number, probTxt: string) => `${l} 상대로 ${ok}${oc}→${ok}${on}을 옮겨 ${k}${c}→${k}${e}로 하면 난수로 ${mid}로 줄어들 때가 있습니다(${probTxt}). 확정수는 변하지 않습니다`,
    koPlainRandom: (l: string, k: string, e: number, d: number, mid: number, probTxt: string) => `${l} 상대로 ${k}${e}(${k}+${d})로 난수로 ${mid}로 줄어들 때가 있습니다(${probTxt}). 확정수는 변하지 않습니다`,
    atkNoImprove: (k: string, m: number) => `${k}${m}까지 투자해도 확정수는 변하지 않습니다`,
    noOppMove: "상대에게 유효한 공격 기술이 없어 내구 조정이 의미가 없습니다",
    alreadySafe: "이미 상대의 공격에 확정으로 쓰러지지 않습니다(조정 불필요)",
    defMax: (k: string) => `H・${k}가 이미 최대입니다. EV로는 확정으로 버티는 횟수를 늘릴 수 없습니다`,
    defBudget: (k: string) => `EV 합계 상한(66) 때문에 H・${k}로 옮길 여유가 없습니다`,
    surviveRealloc: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, h0: number, h1: number) => `${l}의 공격에 대해 ${ak}${ac}→${ak}${an}을 옮겨 H${h} ${k}${d}로 하면 확정으로 ${h0}→${h1}번째 공격까지 버팁니다`,
    survivePlain: (l: string, h: number, k: string, d: number, h0: number, h1: number) => `${l}의 공격에 대해 H${h} ${k}${d}로 확정으로 ${h0}→${h1}번째 공격까지 버팁니다`,
    surviveReallocRandom: (l: string, ak: string, ac: number, an: number, h: number, k: string, d: number, mid: number, probTxt: string) => `${l}의 공격에 대해 ${ak}${ac}→${ak}${an}을 옮겨 H${h} ${k}${d}로 하면 난수로 ${mid}번째 공격까지 버틸 때가 있습니다(상대 기술이 ${mid}회 이내에 맞을 확률 ${probTxt}. 확정으로 버티는 횟수는 변하지 않습니다)`,
    survivePlainRandom: (l: string, h: number, k: string, d: number, mid: number, probTxt: string) => `${l}의 공격에 대해 H${h} ${k}${d}로 난수로 ${mid}번째 공격까지 버틸 때가 있습니다(상대 기술이 ${mid}회 이내에 맞을 확률 ${probTxt}. 확정으로 버티는 횟수는 변하지 않습니다)`,
    defNoImprove: (k: string) => `H・${k}를 상한까지 투자해도 확정으로 버티는 횟수는 변하지 않습니다`,
    otherMany: (n: number, t: string) => `그 외의 빌드(${n}건): ${t}`,
    otherOne: (t: string) => `그 외의 빌드: ${t}`,
    speedNow: (ev: number, s: number) => `현재 성격 그대로 S${ev} 투자로 상정 상대(최속 S${s})를 앞지릅니다`,
    speedNature: (nat: string, ev: number, s: number) => `현재 성격으로는 S32 투자로도 닿지 않습니다. 성격을 ${nat}로 하면 S${ev} 투자로 상정 상대(최속 S${s})를 앞지릅니다`,
    speedNone: (s: number) => `최속 성격・S32 투자로도 상정 상대(최속 S${s})를 앞지를 수 없습니다`,
  },
};
type Txt = (typeof TXT)["ja"];
export interface TuneI18n { lang: Lang; tName: (s: string) => string; tNature: (s: string) => string }


/** 最速に振れる代表的な性格(攻撃系統の異なる2種から到達可能な方を提案) */
const SPEED_NATURES = ["おくびょう", "ようき"];

/**
 * 素の種族値Sを resolved の元になった種族マスタから取得する(メガ解決込み)。
 * 注(UI連携): これには data.ts の loadCore() で species キャッシュが populate 済みであることが前提。
 * ページ初期化で loadCore() を待ってから呼ぶこと。
 */
/** slot/resolvedの元になった種族マスタから種族値6つ(メガ解決込み)を取得する。 */
function baseStatsOf(slot: Slot, resolved: ResolvedBuild): StatArray | null {
  const sm = speciesByName(slot.sp);
  if (!sm) return null;
  if (resolved.mega) {
    const mega = sm.mega.find((m) => m.stone === slot.item);
    return mega ? mega.bs : sm.bs;
  }
  return sm.bs;
}

/** 仮想敵ごとの前提をエンジンに反映する。判定側と同じ扱いにするため、
 * 空の指定は「既定」に戻す。 */
function useScenario(sc: SlotScenario | null | undefined): void {
  const on = !!(sc && (sc.w || sc.t || sc.n || sc.m));
  setScenario(on ? { weather: (sc!.w as never) || null, terrain: (sc!.t as never) || null, boost: sc!.n ?? 0, oppBoost: sc!.m ?? 0 } : null);
}

/**
 * 素早さ実数値が threshold 以上になる最小のS努力値。
 *
 * 実数値ではなく判定と同じ実効素早さ（こだわりスカーフ・すなかき等の特性・積み込み）で
 * 比べる。種族値から計算していた頃は、自分がスカーフを持っていてもその分を見ずに
 * 過剰にSを振る提案が出ていた。ref は閾値の出どころになった相手（天候特性が絡むため、
 * 同じ対面で測らないと前提が食い違う）。
 */
function minEvForThreshold(
  resolved: ResolvedBuild, bs: StatArray, nature: string, threshold: number, ref: ResolvedBuild,
): number | null {
  for (let ev = 0; ev <= EV_STAT_MAX; ev++) {
    const evs = [...resolved.evs] as StatArray;
    evs[5] = ev;
    const probe = withEvs(resolved, bs, nature, evs);
    if (judge1v1(probe, ref).myS >= threshold) return ev;
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

/** 確率(%)の表示。0.2%が「0%」、99.8%が「100%」に丸まる矛盾を避け、境界は「<1」「>99」で示す
 * (「乱数1発(63%)」等、他画面の既存表記と同じ規則)。 */
function fmtProbPct(p: number): string {
  return p < 1 ? "<1%" : p > 99 ? ">99%" : `${Math.round(p)}%`;
}

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
 * targetに対する確定数(最低乱数でも倒せる発数。中央乱数のmyHitsではない)が現在より縮む
 * 最小EVを探す。通常のEV合計66残り予算だけでなく、逆側の攻撃ステ(物理型ならC、特殊型ならA)を
 * 削って充当する振り替えも許可する(振り替え原資はこの1種のみ)。
 * 確定では縮まらないが中央乱数でなら縮む組み合わせが見つかった場合は、それを「乱数n発」と
 * 明記したうえで控えめに提案する(確定数自体は変わらないことを文中で明示する)。
 * 見つからない場合は理由を返す。
 */
function findKoSuggestion(slot: Slot, resolved: ResolvedBuild, bs: StatArray, target: ResolvedBuild, t: Txt, label: string): TuneAttempt {
  const baseline = judge1v1(resolved, target);
  if (baseline.myMove === null) {
    return { ok: false, reason: "no-move", text: t.noMyMove };
  }
  const usedMove = resolved.moves.find((m) => m.n === baseline.myMove);
  if (!usedMove || usedMove.cat === "status") {
    return { ok: false, reason: "no-move", text: t.noMyMove };
  }
  const baseRange = moveHitsRange(resolved, target, 0, baseline.myMove);
  if (!baseRange) {
    return { ok: false, reason: "no-move", text: t.noMyMove };
  }
  const baselineHits = baseRange.lo; // 確定数(最低乱数でも倒せる発数)
  const statIdx = usedMove.cat === "physical" ? 1 : 3;
  const oppIdx = usedMove.cat === "physical" ? 3 : 1;
  const key = EV_STAT_KEYS[statIdx];
  const oppKey = EV_STAT_KEYS[oppIdx];
  const curEv = resolved.evs[statIdx];
  const oppCur = resolved.evs[oppIdx];

  if (curEv >= EV_STAT_MAX) {
    return { ok: false, reason: "already-max", text: t.atkMax(key) };
  }

  // otherSum: statIdx・oppIdx以外(H,B,D,Sのうちこの2つを除いたもの)のEV合計。振り替え原資(oppIdx)は
  // 0まで解放できる前提で、statIdxが到達しうる理論上限を maxReachable として求める。
  const otherSum = evTotalExcluding(resolved.evs, statIdx, oppIdx);
  const maxReachable = Math.min(EV_STAT_MAX, EV_TOTAL_MAX - otherSum);

  if (maxReachable <= curEv) {
    return { ok: false, reason: "budget-exhausted", text: t.atkBudget(key) };
  }

  let randomCand: { evs: StatArray; ev: number; oppNew: number; mid: number; probTxt: string } | null = null;
  for (let ev = curEv + 1; ev <= maxReachable; ev++) {
    // oppIdxをこのevに対して許される最大値まで残す(必要な分だけ削る。0まで無条件に削らない)。
    const oppAllowed = EV_TOTAL_MAX - otherSum - ev;
    const oppNew = Math.min(oppCur, oppAllowed);
    const evs = [...resolved.evs] as StatArray;
    evs[statIdx] = ev;
    evs[oppIdx] = oppNew;
    const probe = withEvs(resolved, bs, slot.nature, evs);
    const r = moveHitsRange(probe, target, 0, baseline.myMove);
    if (!r) continue;
    if (r.lo < baselineHits) {
      const sacrificed = oppNew < oppCur;
      const text = sacrificed
        ? t.koRealloc(label, oppKey, oppCur, oppNew, key, curEv, ev, baselineHits, r.lo)
        : t.koPlain(label, key, ev, ev - curEv, baselineHits, r.lo);
      return { ok: true, suggestion: { kind: "ko", text, evs, stub: false } };
    }
    // 確定ではまだ縮まらないが、中央乱数(判定と同じ基準)でなら縮む最小EVを控えとして1件だけ覚えておく
    // (確定の改善が見つからなかったときだけ、乱数と明記して提案する)。
    if (!randomCand && r.mid < baseRange.mid) {
      randomCand = { evs, ev, oppNew, mid: r.mid, probTxt: r.midProb == null ? "" : fmtProbPct(r.midProb) };
    }
  }
  if (randomCand) {
    const sacrificed = randomCand.oppNew < oppCur;
    const text = sacrificed
      ? t.koReallocRandom(label, oppKey, oppCur, randomCand.oppNew, key, curEv, randomCand.ev, randomCand.mid, randomCand.probTxt)
      : t.koPlainRandom(label, key, randomCand.ev, randomCand.ev - curEv, randomCand.mid, randomCand.probTxt);
    return { ok: true, suggestion: { kind: "ko", text, evs: randomCand.evs, stub: false } };
  }
  return { ok: false, reason: "no-improvement", text: t.atkNoImprove(key, maxReachable) };
}

/**
 * HP・防御(相手のoppMoveの分類に応じB or D)のEVを総当たりし、targetの攻撃に対する
 * 確定で耐えられる発数(最高乱数でも倒されない発数。中央乱数のoppHitsではない)が
 * 現在より伸びる最小の追加EV合計を探す(H・防御同時探索)。通常のEV合計66残り予算だけでなく、
 * 自分の逆側攻撃ステ(judge1v1のmyMoveの分類と逆側。物理型ならC、特殊型ならA)を削って
 * 充当する振り替えも許可する(振り替え原資はこの1種のみ)。
 * 確定では伸びないが中央乱数でなら伸びる組み合わせが見つかった場合は、それを「乱数」と
 * 明記したうえで控えめに提案する(確定で耐えられる発数自体は変わらないことを文中で明示する)。
 * 見つからない場合は理由を返す。
 */
function findSurviveSuggestion(slot: Slot, resolved: ResolvedBuild, bs: StatArray, target: ResolvedBuild, t: Txt, label: string): TuneAttempt {
  const baseline = judge1v1(resolved, target);
  if (baseline.oppMove === null) {
    return { ok: false, reason: "no-move", text: t.noOppMove };
  }
  const usedMove = target.moves.find((m) => m.n === baseline.oppMove);
  if (!usedMove || usedMove.cat === "status") {
    return { ok: false, reason: "no-move", text: t.noOppMove };
  }
  const baseRange = moveHitsRange(resolved, target, 1, baseline.oppMove);
  if (!baseRange) {
    return { ok: false, reason: "no-move", text: t.noOppMove };
  }
  const baselineHits = baseRange.hi; // 確定で耐えられる発数(最高乱数でもこの発数までは倒されない)
  if (baselineHits >= 999) {
    return { ok: false, reason: "already-safe", text: t.alreadySafe };
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
    return { ok: false, reason: "already-max", text: t.defMax(defKey) };
  }

  const otherSum = evTotalExcluding(resolved.evs, 0, defIdx, ...(atkIdx !== null ? [atkIdx] : []));
  const plainBudget = EV_TOTAL_MAX - otherSum - atkCur; // 振り替えなしで使える上限(従来のbudget相当)
  const reallocBudget = EV_TOTAL_MAX - otherSum; // 振り替え(atkIdxを0まで解放)込みで使える上限
  const maxCost = Math.min(EV_STAT_MAX * 2, reallocBudget);

  if (maxCost <= curH + curD) {
    return { ok: false, reason: "budget-exhausted", text: t.defBudget(defKey) };
  }

  let randomCand: { evs: StatArray; h: number; d: number; atkNew: number; mid: number; probTxt: string } | null = null;
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
      const r = moveHitsRange(probe, target, 1, baseline.oppMove);
      if (!r) continue;
      if (r.hi > baselineHits) {
        const sacrificed = atkIdx !== null && atkNew < atkCur;
        const text = sacrificed
          ? t.surviveRealloc(label, atkKey!, atkCur, atkNew, h, defKey, d, baselineHits, r.hi)
          : t.survivePlain(label, h, defKey, d, baselineHits, r.hi);
        return { ok: true, suggestion: { kind: "survive", text, evs, stub: false } };
      }
      // 確定ではまだ伸びないが、中央乱数(判定と同じ基準)でなら伸びる最小コストを控えとして1件だけ覚えておく。
      if (!randomCand && r.mid > baseRange.mid) {
        randomCand = { evs, h, d, atkNew, mid: r.mid, probTxt: r.midProb == null ? "" : fmtProbPct(r.midProb) };
      }
    }
  }
  if (randomCand) {
    const sacrificed = atkIdx !== null && randomCand.atkNew < atkCur;
    const text = sacrificed
      ? t.surviveReallocRandom(label, atkKey!, atkCur, randomCand.atkNew, randomCand.h, defKey, randomCand.d, randomCand.mid, randomCand.probTxt)
      : t.survivePlainRandom(label, randomCand.h, defKey, randomCand.d, randomCand.mid, randomCand.probTxt);
    return { ok: true, suggestion: { kind: "survive", text, evs: randomCand.evs, stub: false } };
  }
  return { ok: false, reason: "no-improvement", text: t.defNoImprove(defKey) };
}

/**
 * ko/surviveの提案不能理由を仮想敵ごとに集約する。
 * 1件のみなら対象名つきでそのまま1行、複数件なら理由文でグルーピングし、件数の多い順に
 * 最大2行(「その他の型: 理由」)に圧縮する(仮想敵の数だけ理由行が増えるのを防ぐため)。
 */
function summarizeFails(fails: { label: string; text: string }[], kind: "ko" | "survive", t: Txt): TuneSuggestion[] {
  if (fails.length === 0) return [];
  if (fails.length === 1) {
    return [{ kind, text: `${fails[0].label}: ${fails[0].text}`, stub: false }];
  }
  const groups = new Map<string, number>();
  for (const f of fails) groups.set(f.text, (groups.get(f.text) ?? 0) + 1);
  const sorted = [...groups.entries()].sort((a, b) => b[1] - a[1]).slice(0, 2);
  return sorted.map(([text, count]) => ({
    kind,
    text: count > 1 ? t.otherMany(count, text) : t.otherOne(text),
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
export function tuneForTargets(
  slot: Slot, resolved: ResolvedBuild, targets: ResolvedBuild[],
  scenarios?: (SlotScenario | null | undefined)[],
  i18n?: TuneI18n,
): TuneSuggestion[] {
  const out: TuneSuggestion[] = [];
  if (targets.length === 0) return out;
  const scOf = (i: number) => (scenarios ? scenarios[i] : null);
  try {
    tuneInner(slot, resolved, targets, scOf, out, i18n ?? { lang: "ja", tName: (s) => s, tNature: (s) => s });
  } finally {
    setScenario(null);
  }
  return out;
}

function tuneInner(
  slot: Slot, resolved: ResolvedBuild, targets: ResolvedBuild[],
  scOf: (i: number) => SlotScenario | null | undefined, out: TuneSuggestion[], i18n: TuneI18n,
): void {
  const t = TXT[i18n.lang] ?? TXT.ja;
  const bs = baseStatsOf(slot, resolved);

  // 想定敵の中で一番速い相手。天候特性(すなかき等)や仮想敵ごとの前提で変わるので、
  // 実数値ではなく判定と同じ実効素早さで比べる。
  let oppMaxS = -1;
  let refIdx = -1;
  targets.forEach((t, i) => {
    useScenario(scOf(i));
    const s = judge1v1(resolved, t).oppS;
    if (s > oppMaxS) { oppMaxS = s; refIdx = i; }
  });
  const threshold = oppMaxS + 1;

  if (bs !== null && refIdx >= 0) {
    const ref = targets[refIdx];
    useScenario(scOf(refIdx));
    const found = minEvForThreshold(resolved, bs, slot.nature, threshold, ref);
    if (found !== null) {
      out.push({
        kind: "speed",
        text: t.speedNow(found, oppMaxS),
        evs: [slot.evs[0], slot.evs[1], slot.evs[2], slot.evs[3], slot.evs[4], found],
        stub: false,
      });
    } else {
      let bestNature: string | null = null;
      let bestEv: number | null = null;
      for (const nat of SPEED_NATURES) {
        const ev = minEvForThreshold(resolved, bs, nat, threshold, ref);
        if (ev !== null && (bestEv === null || ev < bestEv)) {
          bestEv = ev;
          bestNature = nat;
        }
      }
      if (bestNature !== null && bestEv !== null) {
        out.push({
          kind: "speed",
          text: t.speedNature(i18n.tNature(bestNature), bestEv, oppMaxS),
          evs: [slot.evs[0], slot.evs[1], slot.evs[2], slot.evs[3], slot.evs[4], bestEv],
          stub: false,
        });
      } else {
        out.push({
          kind: "speed",
          text: t.speedNone(oppMaxS),
          stub: false,
        });
      }
    }
  }

  if (bs !== null) {
    // 確定数・耐久の逆算は judge1v1 を回すだけなので、その相手の前提を敷けばそのまま効く。
    const koAttempts = targets.map((tg, i) => {
      useScenario(scOf(i));
      return { label: i18n.tName(tg.label), attempt: findKoSuggestion(slot, resolved, bs, tg, t, i18n.tName(tg.label)) };
    });
    const koOk = koAttempts.filter((a): a is { label: string; attempt: TuneOk } => a.attempt.ok);
    const koFail = koAttempts.filter((a): a is { label: string; attempt: TuneFail } => !a.attempt.ok);
    out.push(...koOk.map((a) => a.attempt.suggestion));
    out.push(...summarizeFails(koFail.map((a) => ({ label: a.label, text: a.attempt.text })), "ko", t));

    const surviveAttempts = targets.map((tg, i) => {
      useScenario(scOf(i));
      return { label: i18n.tName(tg.label), attempt: findSurviveSuggestion(slot, resolved, bs, tg, t, i18n.tName(tg.label)) };
    });
    const surviveOk = surviveAttempts.filter((a): a is { label: string; attempt: TuneOk } => a.attempt.ok);
    const surviveFail = surviveAttempts.filter((a): a is { label: string; attempt: TuneFail } => !a.attempt.ok);
    out.push(...surviveOk.map((a) => a.attempt.suggestion));
    out.push(...summarizeFails(surviveFail.map((a) => ({ label: a.label, text: a.attempt.text })), "survive", t));
  }
}
