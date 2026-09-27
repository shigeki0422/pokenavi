// 1v1判定テーブルのマークアップ。ポケモン情報ページ・工房・簡単構築で共有する。
//
// 同じ表を各所で組み立てていたため、罫線・行見出し・桁数が食い違っていた
// （工房だけ縦罫線が無い／行見出しがテキスト／%が整数、など）。
// 見た目は styles/matchup-table.css、組み立てはここ、の1箇所に集約する。
// 呼び出し側は「表示に必要な値だけ」を詰めたビューモデルを渡す（翻訳済みの文字列と
// 解決済みのアイコンURL）。計算・翻訳・アイコン解決の作法は呼び出し側ごとに違うため。
import { causeLabel, extraLabel, stepLabel, type MoveHitDetail, type SeqStep } from "./matchup";
import type { Verdict } from "./types";
import { ASSUMPTIONS_LABEL, MATCHUP_ASSUMPTIONS, MATCHUP_LEAD, type Lang } from "./assumptions";
import { ABILITY_NAME_EN, ABILITY_NAME_KO } from "../../i18n/game-terms";

export interface MatchupColumnVM {
  /** 「型1」等の見出し */
  label: string;
  /** 見出し下の補足（持ち物・性格・努力値）。翻訳済み */
  meta: string[];
  /** 自分→相手 / 相手→自分 の最大打点。null は該当なし */
  my: MoveHitDetail | null;
  opp: MoveHitDetail | null;
  verdict: Verdict;
  /** 技名（翻訳済み）。detail が null のときのフォールバック */
  myMoveText: string;
  oppMoveText: string;
  /** 途中で技を切り替える手順。空でなければ与ダメ/被ダメのセルを手順表示にする。
   * 技名は翻訳済みで渡すこと（このモジュールは翻訳を持たない）。 */
  mySteps?: SeqStep[];
  oppSteps?: SeqStep[];
  /** 毎ターンの与ダメージ(技名は翻訳済み)。2件以上あれば手順・単発より優先して表示する。 */
  myTurns?: SeqStep[];
  oppTurns?: SeqStep[];
  /** 持久戦の技の並び（翻訳済み）。無ければ verdict.stall.seq をそのまま使う。 */
  stallSeq?: string[];
}

export interface MatchupTableVM {
  myName: string;
  oppName: string;
  myIconUrl: string;
  oppIconUrl: string;
  columns: MatchupColumnVM[];
}

interface Labels {
  rowSpeed: string;
  rowJudge: string;
  fast(f: boolean): string;
  hits(n: number | null): string;
  detail(d: MoveHitDetail | null, prob: string): string;
  conds(c: string): string;
  judge(win: boolean, mine: string, theirs: string, first: boolean, byPrio: boolean): string;
  draw: string;
  stall(win: boolean, turns: number): string;
  stallHits(turns: number): string;
  poisonLbl: string;
  /** 回復した側の名前を入れる。行は「攻撃側→防御側」で、回復するのは防御側（ページの主役の場合もある） */
  healLbl(name: string): string;
  planLose(turns: number): string;
  planStuck(turns: number): string;
  bindLbl: string;
  /** タイプ相性の注記。倍率が等倍で前提の型変化も無ければ空文字。 */
  eff(x: number): string;
  /** ひるんで動けなかったターン。 */
  flinchLbl: string;
  /** 先に倒されて動けなかったターン（相手の反動等だけを出す行）。 */
  idleLbl: string;
  /** 技が特性で無効になった行（ばけのかわ等）。 */
  blockedLbl(ab: string): string;
  /** 同速で先後が半々のときの素早さ行・判定行。 */
  tieLbl: string;
  tieJudge(mine: string, theirs: string): string;
  mutualJudge(turn: number): string;
  /** 防御側が技以外で減らしたHP（反動・ゴツゴツメット・天候等）。name は減った側。 */
  extraLbl(name: string, kind: string): string;
}


const mult = (x: number): string => `×${x}`;

const T: Record<Lang, Labels> = {
  ja: {
    rowSpeed: "素早さ", rowJudge: "判定",
    fast: (f: boolean) => (f ? "先手" : "後手"),
    hits: (n: number | null) => (n == null ? "圏外" : n >= 999 ? "6ターン以上" : `確定${n}`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "圏外";
      if (d.hits >= 999) return "6ターン以上";
      const base = d.certain ? `確定${d.hits}` : `乱数${d.hits}発（${prob}%）`;
      return d.reason ? `${base}（${d.reason}込み）` : base;
    },
    conds: (c: string) => `${c} 込みで計算`,
    judge: (win: boolean, mine: string, theirs: string, first: boolean, byPrio: boolean) =>
      `${win ? "勝ち" : "負け"}：${mine}で倒す/${theirs}で倒される・`
      + `${byPrio ? "先制技で" : ""}${first ? "先手" : "後手"}`,
    draw: "引き分け：互いに6ターン以上かかる・決着つかず",
    stall: (win: boolean, turns: number) =>
      `持久戦で${win ? "勝ち" : "負け"}（${turns}ターン・相手が交代しない前提）`,
    stallHits: (turns: number) => `毒込み${turns}ターンで決着`,
    poisonLbl: "毒",
    healLbl: (n) => `↩ ${n}が回復`,
    flinchLbl: "ひるんで動けない", idleLbl: "（先に倒されて動けない）",
    tieLbl: "同速（先後は半々）", blockedLbl: (ab) => `${ab}で無効`,
    tieJudge: (m, o) => `同速（先後は半々）：自分が先に動いた場合は${m}で倒す/${o}で倒される`,
    mutualJudge: (n) => `相打ち：${n}ターン目に互いに倒れる`,
    extraLbl: (n, k) => `↓ ${n}の${causeLabel(k, "ja")}`,
    planLose: (n: number) => `毒込みでも${n}ターンで倒される`,
    planStuck: (n: number) => `毒込み${n}ターンでは決着つかず`,
    bindLbl: "拘束",
    eff: (x) => (x === 0 ? "効果なし" : x > 1 ? `効果抜群 ${mult(x)}` : x < 1 ? `今ひとつ ${mult(x)}` : ""),
  },
  en: {
    rowSpeed: "Speed", rowJudge: "Verdict",
    fast: (f: boolean) => (f ? "First" : "Second"),
    hits: (n: number | null) => (n == null ? "n/a" : n >= 999 ? "6+ turns" : `${n}HKO`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "n/a";
      if (d.hits >= 999) return "6+ turns";
      const base = d.certain ? `${d.hits}HKO` : `${d.hits} hits (${prob}%)`;
      return d.reason ? `${base} (incl. ${d.reason})` : base;
    },
    conds: (c: string) => `calculated with ${c}`,
    judge: (win: boolean, mine: string, theirs: string, first: boolean, byPrio: boolean) =>
      `${win ? "Win" : "Loss"}: ${mine} to KO / ${theirs} to be KOed, `
      + `${first ? "moves first" : "moves second"}${byPrio ? " (priority)" : ""}`,
    draw: "Draw: neither can KO within 5 turns",
    stall: (win: boolean, turns: number) =>
      `${win ? "Win" : "Loss"} by stalling (${turns} turns, assuming no switch)`,
    stallHits: (turns: number) => `Decided in ${turns} turns (incl. poison)`,
    poisonLbl: "Psn",
    healLbl: (n) => `↩ ${n} heals`,
    flinchLbl: "flinched", idleLbl: "(KOed before moving)",
    tieLbl: "Speed tie (50/50)", blockedLbl: (ab) => `blocked by ${ABILITY_NAME_EN[ab] ?? ab}`,
    tieJudge: (m, o) => `Speed tie (50/50): if you move first, ${m} to KO / ${o} to be KOed`,
    mutualJudge: (n) => `Double KO: both faint on turn ${n}`,
    extraLbl: (n, k) => `↓ ${n}: ${causeLabel(k, "en")}`,
    planLose: (n: number) => `KOed in ${n} turns even with poison`,
    planStuck: (n: number) => `No KO in ${n} turns even with poison`,
    bindLbl: "Bind",
    eff: (x) => (x === 0 ? "No effect" : x > 1 ? `Super effective ${mult(x)}` : x < 1 ? `Not very effective ${mult(x)}` : ""),
  },
  ko: {
    rowSpeed: "스피드", rowJudge: "판정",
    fast: (f: boolean) => (f ? "선공" : "후공"),
    hits: (n: number | null) => (n == null ? "권외" : n >= 999 ? "6턴 이상" : `확정${n}`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "권외";
      if (d.hits >= 999) return "6턴 이상";
      const base = d.certain ? `확정${d.hits}` : `난수${d.hits}발(${prob}%)`;
      return d.reason ? `${base}(${d.reason} 포함)` : base;
    },
    conds: (c: string) => `${c} 포함 계산`,
    judge: (win: boolean, mine: string, theirs: string, first: boolean, byPrio: boolean) =>
      `${win ? "승" : "패"}: ${mine}로 쓰러뜨림 / ${theirs}로 당함・`
      + `${byPrio ? "선제기로 " : ""}${first ? "선공" : "후공"}`,
    draw: "무승부: 5턴 안에 서로 쓰러뜨리지 못함",
    stall: (win: boolean, turns: number) =>
      `지구전으로 ${win ? "승리" : "패배"} (${turns}턴・상대가 교체하지 않는 전제)`,
    stallHits: (turns: number) => `독 포함 ${turns}턴으로 결착`,
    poisonLbl: "독",
    healLbl: (n) => `↩ ${n} 회복`,
    flinchLbl: "풀죽어 움직이지 못함", idleLbl: "(먼저 쓰러져 행동 못 함)",
    tieLbl: "동속(선후 반반)", blockedLbl: (ab) => `${ABILITY_NAME_KO[ab] ?? ab}(으)로 무효`,
    tieJudge: (m, o) => `동속(선후 반반): 내가 먼저 움직이면 ${m}로 쓰러뜨림 / ${o}로 당함`,
    mutualJudge: (n) => `상쇄: ${n}턴째에 서로 쓰러짐`,
    extraLbl: (n, k) => `↓ ${n}의 ${causeLabel(k, "ko")}`,
    planLose: (n: number) => `독을 걸어도 ${n}턴에 쓰러짐`,
    planStuck: (n: number) => `독을 걸어도 ${n}턴 안에 결착 없음`,
    bindLbl: "구속",
    eff: (x) => (x === 0 ? "효과 없음" : x > 1 ? `효과 굉장함 ${mult(x)}` : x < 1 ? `효과 별로 ${mult(x)}` : ""),
  },
};

const esc = (s: string): string =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c] as string));

/** 乱数n発の確率(%)の表示。0%/100%という矛盾表示を避けて境界は「<1」「>99」で示す。 */
/** タイプ相性の注記（効果抜群 ×2 等。等倍で前提の型変化も無ければ空文字）。1v1カードの技の行と共通。 */
export function effLabel(x: number | null | undefined, lang: Lang): string {
  if (x == null) return "";
  return (T[lang] ?? T.ja).eff(x);
}

export function fmtProb(prob: number | null | undefined): string {
  const p = prob ?? 0;
  if (p < 1) return "<1";
  if (p > 99 && p < 100) return ">99";
  return String(Math.round(p));
}

/** 持久戦の技の並びを、連続する同じ技ごとの区間(開始ターン〜終了ターン)にまとめる。 */
function stallRuns(seq: string[]): { n: string; from: number; to: number }[] {
  const out: { n: string; from: number; to: number }[] = [];
  for (let i = 0; i < seq.length;) {
    let j = i;
    while (j < seq.length && seq[j] === seq[i]) j++;
    out.push({ n: seq[i], from: i + 1, to: j });
    i = j;
  }
  return out;
}

/** 判定行の文。持久戦で決まったならそれを、互いに圏外なら引き分けを優先する。 */
function judgeText(c: MatchupColumnVM, t: Labels): string {
  const v = c.verdict;
  if (v.stall?.side) {
    return t.stall(v.stall.side === "me", v.stall.turns);
  }
  if (v.draw) return t.draw;
  if (v.mutual) return t.mutualJudge(v.mutualTurn ?? v.myHits ?? 0);
  if (v.tie) return t.tieJudge(t.hits(v.myHits ?? null), t.hits(v.oppHits ?? null));
  return t.judge(v.win, t.hits(v.myHits ?? null), t.hits(v.oppHits ?? null), v.koFirst, v.koByPriority);
}

// 準備の技（積み技）のターンは与ダメージが0なので%を出さない。
const pctText = (lo: number | null, hi: number | null): string =>
  lo != null && hi != null && (lo > 0 || hi > 0) ? `${lo.toFixed(1)}〜${hi.toFixed(1)}%` : "";

/** 同じ技を撃ち続ける前提のセル。1行の%＋確定数＋技名。 */
function singleCell(d: MoveHitDetail | null, moveText: string, t: Labels): string {
  const p = pctText(d?.pctLo ?? null, d?.pctHi ?? null);
  const pct = p ? `<span class="mbp-pct">${p}</span>` : "";
  const conds = d?.conds ? `<div class="mbp-conds">${esc(t.conds(d.conds))}</div>` : "";
  return `<td>${pct}<div class="mbp-move">${esc(moveText)}</div>`
    + `<span class="mbp-hits">${esc(t.detail(d, fmtProb(d?.prob)))}</span>${effLine(d, t)}${conds}</td>`;
}

function effLine(d: MoveHitDetail | null, t: Labels): string {
  if (!d || d.eff == null) return "";
  const s = t.eff(d.eff);
  return s ? `<div class="mbp-eff">${esc(s)}</div>` : "";
}

/** 途中で技を切り替える手順のセル。手ごとに%と技名を並べ、確定数は手順全体で1つ。
 * 手数は最低乱数で走らせた結果なので「確定n」でよい（乱数で伸びる線は出さない）。 */
function seqCell(steps: SeqStep[], t: Labels): string {
  const lines = steps.map((s, i) =>
    `<div class="mbp-step"><span class="mbp-step-no">${i + 1}</span>`
    + `<span class="mbp-pct">${esc(pctText(s.pctLo, s.pctHi))}</span>`
    + `<span class="mbp-move">${esc(s.n)}</span></div>`).join("");
  const cs = [...new Set(steps.map((s) => s.conds).filter(Boolean))] as string[];
  const conds = cs.length ? `<div class="mbp-conds">${esc(t.conds(cs.join("・")))}</div>` : "";
  return `<td class="mbp-seq">${lines}`
    + `<span class="mbp-hits">${esc(t.hits(steps.length))}</span>${conds}</td>`;
}

/** 持久戦で決着する側のセル。ターンごとの技を並べ、決着ターンを確定数の代わりに出す。
 * 技の%は最大打点の技そのものの値（変化技は%なし）。 */
function stallCell(c: MatchupColumnVM, d: MoveHitDetail | null, moveText: string, t: Labels,
                   st: NonNullable<Verdict["stall"]> | (NonNullable<Verdict["plans"]>["me"] & object) = c.verdict.stall!): string {
  const outcome = (st as { outcome?: string }).outcome;
  const footer = outcome === "lose" ? t.planLose(st.turns) : outcome === "stuck" ? t.planStuck(st.turns) : t.stallHits(st.turns);
  // ターンごとの内訳(直接ダメージ＋毒)があれば、1ターン1行で出す。毒は1/16,2/16…と累積するので、
  // 技のダメージだけを並べると「なぜ倒れるのか」が読めない。
  if (st.trace && st.trace.length && st.defMax) {
    const names = c.stallSeq ?? st.seq;
    const pc = (v: number) => {
      const x = (v / st.defMax!) * 100;
      return x < 10 ? x.toFixed(1) : String(Math.round(x));
    };
    const lines = st.trace.map((tr, i) => {
      const parts = [
        tr.direct > 0 ? `<span class="mbp-pct">${pc(tr.direct)}%</span>` : "",
        `<span class="mbp-psn">${esc(t.poisonLbl)} ${pc(tr.poison)}%</span>`,
        tr.bind > 0 ? `<span class="mbp-bind">${esc(t.bindLbl)} ${pc(tr.bind)}%</span>` : "",
      ].join("");
      return `<div class="mbp-step"><span class="mbp-step-no">${i + 1}</span>${parts}<span class="mbp-move">${esc(names[i] ?? tr.n)}</span></div>`;
    }).join("");
    return `<td class="mbp-seq">${lines}<span class="mbp-hits">${esc(footer)}</span></td>`;
  }
  const runs = stallRuns(c.stallSeq ?? st.seq);
  const lines = runs.map((r) => {
    const no = r.from === r.to ? `${r.from}` : `${r.from}〜${r.to}`;
    const p = r.n === moveText ? pctText(d?.pctLo ?? null, d?.pctHi ?? null) : "";
    return `<div class="mbp-step"><span class="mbp-step-no">${no}</span>`
      + (p ? `<span class="mbp-pct">${p}</span>` : "")
      + `<span class="mbp-move">${esc(r.n)}</span></div>`;
  }).join("");
  const conds = d?.conds ? `<div class="mbp-conds">${esc(t.conds(d.conds))}</div>` : "";
  return `<td class="mbp-seq">${lines}<span class="mbp-hits">${esc(t.stallHits(st.turns))}</span>${conds}</td>`;
}

/** 毎ターンのダメージを1ターン1行で並べるセル。防御上昇・積みなどでターンごとに変わる値がそのまま読める。
 * 末尾は単発の最大打点なら確定数/乱数n発、手順（技が切り替わる）なら判定と同じ確定数。 */
function turnsCell(turns: SeqStep[], d: MoveHitDetail | null, verdictHits: number | null | undefined, t: Labels,
                   defender: string): string {
  // 連続して同じ技・同じダメージのターンは「1〜4」のようにまとめる（値が変わるターンだけ行を分ける）。
  // ひるんだターンと、防御側が技以外でHPを減らしたターン（反動等）はまとめない。
  const runs: { n: string; p: string; from: number; to: number; heal: number; extra: string; lbl?: string }[] = [];
  // 判定の対戦の経過(ターン番号つき)なら1行1行動。後から動いた行動は 1' と表記し、ひるんだターンは番号なし。
  const timed = turns.some((s) => s.turn != null);
  turns.forEach((s, i) => {
    const p = s.blocked ? "" : pctText(s.pctLo, s.pctHi);
    const heal = s.healPct ? Math.round(s.healPct) : 0;
    const n = s.flinch ? t.flinchLbl : s.idle ? t.idleLbl : s.blocked ? `${s.n} → ${t.blockedLbl(s.blocked)}` : s.n;
    const extra = (s.extra ?? []).filter((x) => x.pct > 0)
      .map((x) => `<div class="mbp-extra">${x.turn != null ? `<span class="mbp-step-no">${esc(extraLabel(x, ""))}</span>` : ""}${esc(t.extraLbl(defender, x.kind))} ${x.pct < 10 ? x.pct.toFixed(1) : Math.round(x.pct)}%</div>`).join("");
    const last = runs[runs.length - 1];
    if (!timed && last && last.n === n && last.p === p && last.heal === heal && !heal && !extra && !last.extra && !s.flinch) last.to = i + 1;
    else runs.push({ n, p, from: i + 1, to: i + 1, heal, extra, lbl: timed ? stepLabel(s, i) : undefined });
  });
  const lines = runs.map((r) =>
    `<div class="mbp-step"><span class="mbp-step-no"${r.lbl === "" ? ' style="visibility:hidden"' : ""}>${r.lbl ?? (r.from === r.to ? r.from : `${r.from}〜${r.to}`)}</span>`
    + `<span class="mbp-pct">${esc(r.p)}</span>`
    + `<span class="mbp-move">${esc(r.n)}</span></div>`
    + r.extra
    + (r.heal > 0 ? `<div class="mbp-heal">${esc(t.healLbl(defender))} ${r.heal}%</div>` : "")).join("");
  const mixed = new Set(turns.map((s) => s.n)).size > 1;
  const foot = mixed || !d ? t.hits(verdictHits ?? null) : t.detail(d, fmtProb(d.prob));
  const conds = d?.conds ? `<div class="mbp-conds">${esc(t.conds(d.conds))}</div>` : "";
  return `<td class="mbp-seq">${lines}<span class="mbp-hits">${esc(foot)}</span>${mixed ? "" : effLine(d, t)}${conds}</td>`;
}

function dmgCell(d: MoveHitDetail | null, moveText: string, t: Labels, steps?: SeqStep[],
                 turns?: SeqStep[], verdictHits?: number | null, defender = ""): string {
  // 毎ターン(判定の対戦の経過)があれば、1ターンでもそれを出す（棒立ちの手順は倒れた後の手まで含むため使わない）。
  if (turns && turns.length > 0) return turnsCell(turns, d, verdictHits, t, defender);
  return steps && steps.length > 1 ? seqCell(steps, t) : singleCell(d, moveText, t);
}

/** 常に同じ前提の折りたたみ。表と一緒に出す。 */
export function renderAssumptions(lang: Lang): string {
  const items = (MATCHUP_ASSUMPTIONS[lang] ?? MATCHUP_ASSUMPTIONS.ja)
    .map((a) => `<li>${esc(a)}</li>`).join("");
  return `<details class="mbp-assume"><summary>${esc(ASSUMPTIONS_LABEL[lang] ?? ASSUMPTIONS_LABEL.ja)}</summary>`
    + `<ul>${items}</ul></details>`;
}

export function matchupLead(lang: Lang): string {
  return MATCHUP_LEAD[lang] ?? MATCHUP_LEAD.ja;
}

export function renderMatchupTable(vm: MatchupTableVM, lang: Lang, opts: { compact?: boolean } = {}): string {
  const t = T[lang] ?? T.ja;
  const ico = (url: string, name: string, cls: string) =>
    url ? `<img class="${cls}" src="${esc(url)}" alt="${esc(name)}" loading="lazy">` : "";
  const arrow = (fromUrl: string, fromName: string, toUrl: string, toName: string) =>
    `<td class="lft"><div class="mbp-lbl-icons">${ico(fromUrl, fromName, "mbp-mini-lbl")}`
    + `<span>↓</span>${ico(toUrl, toName, "mbp-mini-lbl")}</div></td>`;

  const head = `<tr><th class="lft"></th>` + vm.columns.map((c) =>
    `<th>${esc(c.label)}<div class="mbp-build-meta">${c.meta.map(esc).join("<br>")}</div></th>`).join("") + `</tr>`;
  const myRow = arrow(vm.myIconUrl, vm.myName, vm.oppIconUrl, vm.oppName)
    + vm.columns.map((c) => c.verdict.stall?.side === "me"
      ? stallCell(c, c.my, c.myMoveText, t)
      : c.verdict.plans?.me ? stallCell(c, c.my, c.myMoveText, t, c.verdict.plans.me)
      : dmgCell(c.my, c.myMoveText, t, c.mySteps, c.myTurns, c.verdict.myHits, vm.oppName)).join("");
  const oppRow = arrow(vm.oppIconUrl, vm.oppName, vm.myIconUrl, vm.myName)
    + vm.columns.map((c) => c.verdict.stall?.side === "opp"
      ? stallCell(c, c.opp, c.oppMoveText, t)
      : c.verdict.plans?.opp ? stallCell(c, c.opp, c.oppMoveText, t, c.verdict.plans.opp)
      : dmgCell(c.opp, c.oppMoveText, t, c.oppSteps, c.oppTurns, c.verdict.oppHits, vm.myName)).join("");
  const spdRow = `<td class="lft">${esc(t.rowSpeed)}</td>` + vm.columns.map((c) =>
    `<td class="mbp-spd-cell ${c.verdict.fast ? "mbp-spd-win" : "mbp-spd-lose"}">`
    + `<div>${esc(c.verdict.tie ? t.tieLbl : t.fast(c.verdict.fast))}</div>`
    + `<div>${ico(vm.myIconUrl, vm.myName, "mbp-mini")}S${c.verdict.myS} / `
    + `${ico(vm.oppIconUrl, vm.oppName, "mbp-mini")}S${c.verdict.oppS}</div></td>`).join("");
  const judgeRow = `<td class="lft">${esc(t.rowJudge)}</td>` + vm.columns.map((c) =>
    `<td class="${c.verdict.win ? "mbp-judge-win" : "mbp-judge-lose"}">`
    + `<b class="mbp-sym">${esc(c.verdict.sym)}</b>`
    + `<div class="mbp-judge-text">${esc(judgeText(c, t))}</div>`
    + `</td>`).join("");

  return `<div class="mbp-scroll"><table class="mbp-table">${opts.compact ? "" : head}`
    + `<tr>${myRow}</tr><tr>${oppRow}</tr><tr>${spdRow}</tr><tr>${judgeRow}</tr></table></div>`;
}
