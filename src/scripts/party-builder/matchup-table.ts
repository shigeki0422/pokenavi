// 1v1判定テーブルのマークアップ。ポケモン情報ページ・工房・簡単構築で共有する。
//
// 同じ表を各所で組み立てていたため、罫線・行見出し・桁数が食い違っていた
// （工房だけ縦罫線が無い／行見出しがテキスト／%が整数、など）。
// 見た目は styles/matchup-table.css、組み立てはここ、の1箇所に集約する。
// 呼び出し側は「表示に必要な値だけ」を詰めたビューモデルを渡す（翻訳済みの文字列と
// 解決済みのアイコンURL）。計算・翻訳・アイコン解決の作法は呼び出し側ごとに違うため。
import type { MoveHitDetail, SeqStep } from "./matchup";
import type { Verdict } from "./types";
import { ASSUMPTIONS_LABEL, MATCHUP_ASSUMPTIONS, MATCHUP_LEAD, type Lang } from "./assumptions";

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
  seqNote: string;
  fast(f: boolean): string;
  hits(n: number | null): string;
  detail(d: MoveHitDetail | null, prob: string): string;
  conds(c: string): string;
  judge(win: boolean, mine: string, theirs: string, fast: boolean): string;
}

const T: Record<Lang, Labels> = {
  ja: {
    rowSpeed: "素早さ", rowJudge: "判定", seqNote: "（手順）",
    fast: (f: boolean) => (f ? "先手" : "後手"),
    hits: (n: number | null) => (n == null || n >= 999 ? "圏外" : `確定${n}`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "圏外";
      const base = d.certain ? `確定${d.hits}` : `乱数${d.hits}発（${prob}%）`;
      return d.reason ? `${base}（${d.reason}込み）` : base;
    },
    conds: (c: string) => `${c} 込みで計算`,
    judge: (win: boolean, mine: string, theirs: string, fast: boolean) =>
      `${win ? "勝ち" : "負け"}：${mine}で倒す/${theirs}で倒される・${fast ? "先手" : "後手"}`,
  },
  en: {
    rowSpeed: "Speed", rowJudge: "Verdict", seqNote: " (line)",
    fast: (f: boolean) => (f ? "First" : "Second"),
    hits: (n: number | null) => (n == null || n >= 999 ? "n/a" : `${n}HKO`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "n/a";
      const base = d.certain ? `${d.hits}HKO` : `${d.hits} hits (${prob}%)`;
      return d.reason ? `${base} (incl. ${d.reason})` : base;
    },
    conds: (c: string) => `calculated with ${c}`,
    judge: (win: boolean, mine: string, theirs: string, fast: boolean) =>
      `${win ? "Win" : "Loss"}: ${mine} to KO / ${theirs} to be KOed, ${fast ? "faster" : "slower"}`,
  },
  ko: {
    rowSpeed: "스피드", rowJudge: "판정", seqNote: "（순서）",
    fast: (f: boolean) => (f ? "선공" : "후공"),
    hits: (n: number | null) => (n == null || n >= 999 ? "권외" : `확정${n}`),
    detail: (d: MoveHitDetail | null, prob: string) => {
      if (!d || d.hits == null) return "권외";
      const base = d.certain ? `확정${d.hits}` : `난수${d.hits}발(${prob}%)`;
      return d.reason ? `${base}(${d.reason} 포함)` : base;
    },
    conds: (c: string) => `${c} 포함 계산`,
    judge: (win: boolean, mine: string, theirs: string, fast: boolean) =>
      `${win ? "승" : "패"}: ${mine}로 쓰러뜨림 / ${theirs}로 당함・${fast ? "선공" : "후공"}`,
  },
};

const esc = (s: string): string =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c] as string));

/** 乱数n発の確率(%)の表示。0%/100%という矛盾表示を避けて境界は「<1」「>99」で示す。 */
export function fmtProb(prob: number | null | undefined): string {
  const p = prob ?? 0;
  if (p < 1) return "<1";
  if (p > 99 && p < 100) return ">99";
  return String(Math.round(p));
}

const pctText = (lo: number | null, hi: number | null): string =>
  lo != null && hi != null ? `${lo.toFixed(1)}〜${hi.toFixed(1)}%` : "";

/** 同じ技を撃ち続ける前提のセル。1行の%＋確定数＋技名。 */
function singleCell(d: MoveHitDetail | null, moveText: string, t: Labels): string {
  const p = pctText(d?.pctLo ?? null, d?.pctHi ?? null);
  const pct = p ? `<span class="mbp-pct">${p}</span>` : "";
  const conds = d?.conds ? `<div class="mbp-conds">${esc(t.conds(d.conds))}</div>` : "";
  return `<td>${pct}<span class="mbp-hits">${esc(t.detail(d, fmtProb(d?.prob)))}</span>`
    + `<div class="mbp-move">${esc(moveText)}</div>${conds}</td>`;
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
    + `<span class="mbp-hits">${esc(t.hits(steps.length))}<span class="mbp-seq-note">${esc(t.seqNote)}</span></span>`
    + `${conds}</td>`;
}

function dmgCell(d: MoveHitDetail | null, moveText: string, t: Labels, steps?: SeqStep[]): string {
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

export function renderMatchupTable(vm: MatchupTableVM, lang: Lang): string {
  const t = T[lang] ?? T.ja;
  const ico = (url: string, name: string, cls: string) =>
    url ? `<img class="${cls}" src="${esc(url)}" alt="${esc(name)}" loading="lazy">` : "";
  const arrow = (fromUrl: string, fromName: string, toUrl: string, toName: string) =>
    `<td class="lft"><div class="mbp-lbl-icons">${ico(fromUrl, fromName, "mbp-mini-lbl")}`
    + `<span>↓</span>${ico(toUrl, toName, "mbp-mini-lbl")}</div></td>`;

  const head = `<tr><th class="lft"></th>` + vm.columns.map((c) =>
    `<th>${esc(c.label)}<div class="mbp-build-meta">${c.meta.map(esc).join("<br>")}</div></th>`).join("") + `</tr>`;
  const myRow = arrow(vm.myIconUrl, vm.myName, vm.oppIconUrl, vm.oppName)
    + vm.columns.map((c) => dmgCell(c.my, c.myMoveText, t, c.mySteps)).join("");
  const oppRow = arrow(vm.oppIconUrl, vm.oppName, vm.myIconUrl, vm.myName)
    + vm.columns.map((c) => dmgCell(c.opp, c.oppMoveText, t, c.oppSteps)).join("");
  const spdRow = `<td class="lft">${esc(t.rowSpeed)}</td>` + vm.columns.map((c) =>
    `<td class="mbp-spd-cell ${c.verdict.fast ? "mbp-spd-win" : "mbp-spd-lose"}">`
    + `<div>${esc(t.fast(c.verdict.fast))}</div>`
    + `<div>${ico(vm.myIconUrl, vm.myName, "mbp-mini")}S${c.verdict.myS} / `
    + `${ico(vm.oppIconUrl, vm.oppName, "mbp-mini")}S${c.verdict.oppS}</div></td>`).join("");
  const judgeRow = `<td class="lft">${esc(t.rowJudge)}</td>` + vm.columns.map((c) =>
    `<td class="${c.verdict.win ? "mbp-judge-win" : "mbp-judge-lose"}">`
    + `<b class="mbp-sym">${esc(c.verdict.sym)}</b>`
    + `<div class="mbp-judge-text">${esc(t.judge(c.verdict.win,
        t.hits(c.verdict.myHits ?? null), t.hits(c.verdict.oppHits ?? null), c.verdict.fast))}</div></td>`).join("");

  return `<div class="mbp-scroll"><table class="mbp-table">${head}`
    + `<tr>${myRow}</tr><tr>${oppRow}</tr><tr>${spdRow}</tr><tr>${judgeRow}</tr></table></div>`;
}
