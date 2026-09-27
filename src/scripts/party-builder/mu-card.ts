// 1v1 の「仮想敵カード」と同じ表記のカード（判定の見出し・型のチップ・結論の帯・ダメージレースの棒・技ごとのダメージ・
// 折りたたみの内訳）を静的HTMLで組み立てる。ポケモン情報ページ等のポップアップ(MatchupBreakdownPopup)が使う。
// 見た目は styles/mu-card.css。工房(PartyBuilderApp)の仮想敵カードと文言・並び・色を揃えている。
import { effLabel, renderAssumptions, renderMatchupTable } from "./matchup-table";
import { renderReplay, handleReplayClick } from "./mu-replay";
import { causeCat, causeLabel, causeShort, condText, extraLabel, koByMove, lateMark, raceBarItems, stepLabel, turnTag, type BarItem, type MoveDamage, type MoveHitDetail, type SeqStep } from "./matchup";
import type { Verdict } from "./types";
import type { Lang } from "./assumptions";

export interface MuCardVM {
  verdict: Verdict;
  /** 相手の型のチップ（翻訳済み）: 持ち物・特性・性格 */
  chips: string[];
  /** 相手の努力値の表記（例: A32 S32） */
  evLabel: string;
  /** 毎ターン(判定の対戦の経過。技名は翻訳済み)。無ければ最大打点1発で代用する。 */
  myTurns: SeqStep[];
  oppTurns: SeqStep[];
  my: MoveHitDetail | null;
  opp: MoveHitDetail | null;
  /** 技ごとのダメージ幅（技名は翻訳済み） */
  myMoves: MoveDamage[];
  oppMoves: MoveDamage[];
  /** 技が1つでも設定されているか（技の欄が空のとき「有効打なし」か「技が未設定」かを分ける）。無ければ設定あり扱い。 */
  myHasMoves?: boolean;
  oppHasMoves?: boolean;
  /** 棒の左に出すHPの持ち主のアイコンURLと名前（表示中のフォーム）。 */
  myIcon?: string;
  oppIcon?: string;
  myName?: string;
  oppName?: string;
  /** 最大HP（棒のセグメントの実数値の表示用）。hpOpp=相手、hpMe=自分。 */
  hpOpp: number;
  hpMe: number;
  /** 折りたたみの「くわしい内訳」の中身（表のHTML） */
  detailHtml: string;
  /** 持ち物名の翻訳（再生のメッセージ用）。無ければそのまま。 */
  tItem?(n: string): string;
  tPoke?(n: string): string;
  tAbility?(n: string): string;
  tMove(n: string): string;
}

const TXT = {
  ja: {
    win: "先に倒せる", lose: "先に倒される", draw: "引き分け", stallWin: "持久戦で勝ち", stallLose: "持久戦で負け",
    my: (n: number) => `自分 ${n >= 999 ? "6ターン以上" : `${n}ターン`}`,
    opp: (n: number) => `相手 ${n >= 999 ? "6ターン以上" : `${n}ターン`}`,
    first: "先手", second: "後手", barOpp: "相手 → 自分", barMe: "自分 → 相手", tie: "同速（先後は半々）", mutual: "相打ち", basis: "中央乱数で判定",  mutualBody: (n: number) => `${n}ターン目に互いに倒れる`, selfKoOpp: "相手は反動などで倒れる", selfKoMe: "自分は反動などで倒れる", tieNote: "※同速: 経過は自分が先に動いた場合",
    koOpp: (n: number) => `${n}ターンで倒される`, koMe: (n: number) => `${n}ターンで倒す`,
    part: (x: number) => `5ターンで約${x}%`, stopped: (x: number) => `倒れるまでに約${x}%`,
    healKey: "相手の回復（棒が戻る）", healKeyMe: "自分の回復（棒が戻る）",
    movesMe: "自分の技（相手へのダメージ）", movesOpp: "相手の技（自分へのダメージ）",
    turnN: (n: string) => `${n}ターン目`, range: (lo: string, hi: string) => `${lo}〜${hi}%`, simAt: (x: string) => `　※本シミュでは中央の${x}で計算`, simCap: (x: string) => `　※とどめ（残りHP ${x}）`, segHint: "棒をタップすると詳細",
    detail: "くわしい内訳（毎ターン・素早さ・判定）", replay: "くわしい内訳（対戦の再生・1ターンずつ）", noDmg: "ダメージ技なし", fellFirst: "動く前に倒される",
    noEffMove: "有効打なし(変化技・無効のみ)", noMoves: "技が未設定です",
  },
  en: {
    win: "You KO first", lose: "You get KOed first", draw: "Draw", stallWin: "Win by stall", stallLose: "Loss by stall",
    my: (n: number) => `You ${n >= 999 ? "6+ turns" : `${n}T`}`,
    opp: (n: number) => `Opp ${n >= 999 ? "6+ turns" : `${n}T`}`,
    first: "You move first", second: "You move second", barOpp: "Opponent → you", barMe: "You → opponent", tie: "Speed tie (50/50)", mutual: "Double KO", basis: "mid roll",  mutualBody: (n: number) => `Both faint on turn ${n}`, selfKoOpp: "Opponent faints from recoil etc.", selfKoMe: "You faint from recoil etc.", tieNote: "* Speed tie: shown as if you move first",
    koOpp: (n: number) => `KO in ${n}`, koMe: (n: number) => `KO in ${n}`,
    part: (x: number) => `~${x}% in 5 turns`, stopped: (x: number) => `~${x}% before fainting`,
    healKey: "Opponent heals (bar rolls back)", healKeyMe: "You heal (bar rolls back)",
    movesMe: "Your moves (damage to opponent)", movesOpp: "Opponent moves (damage to you)",
    turnN: (n: string) => `Turn ${n}`, range: (lo: string, hi: string) => `${lo}-${hi}%`, simAt: (x: string) => ` * this simulation uses the median ${x}`, simCap: (x: string) => ` * finishing blow (remaining HP ${x})`, segHint: "Tap a bar segment for details",
    detail: "Detailed breakdown (per turn, Speed, verdict)", replay: "Detailed breakdown (battle replay, turn by turn)", noDmg: "No damaging move", fellFirst: "KOed before moving",
    noEffMove: "No effective move (status moves/immune only)", noMoves: "No moves set",
  },
  ko: {
    win: "먼저 쓰러뜨림", lose: "먼저 쓰러짐", draw: "무승부", stallWin: "지구전 승리", stallLose: "지구전 패배",
    my: (n: number) => `나 ${n >= 999 ? "6턴 이상" : `${n}턴`}`,
    opp: (n: number) => `상대 ${n >= 999 ? "6턴 이상" : `${n}턴`}`,
    first: "선공", second: "후공", barOpp: "상대 → 나", barMe: "나 → 상대", tie: "동속(선후 반반)", mutual: "상쇄", basis: "중앙 난수 기준",  mutualBody: (n: number) => `${n}턴째에 서로 쓰러짐`, selfKoOpp: "상대는 반동 등으로 쓰러짐", selfKoMe: "나는 반동 등으로 쓰러짐", tieNote: "※동속: 경과는 내가 먼저 움직인 경우",
    koOpp: (n: number) => `${n}턴에 쓰러짐`, koMe: (n: number) => `${n}턴에 쓰러뜨림`,
    part: (x: number) => `5턴에 약 ${x}%`, stopped: (x: number) => `쓰러지기 전까지 약 ${x}%`,
    healKey: "상대 회복(막대가 되돌아감)", healKeyMe: "내 회복(막대가 되돌아감)",
    movesMe: "내 기술(상대에게 주는 대미지)", movesOpp: "상대 기술(나에게 주는 대미지)",
    turnN: (n: string) => `${n}턴째`, range: (lo: string, hi: string) => `${lo}~${hi}%`, simAt: (x: string) => ` ※본 시뮬레이션은 중앙값 ${x}로 계산`, simCap: (x: string) => ` ※마무리(남은 HP ${x})`, segHint: "막대를 탭하면 상세",
    detail: "자세한 내역(매 턴·스피드·판정)", replay: "자세한 내역(대전 재생·1턴씩)", noDmg: "대미지 기술 없음", fellFirst: "행동 전에 쓰러짐",
    noEffMove: "유효타 없음(변화기·무효만 있음)", noMoves: "기술이 설정되지 않았습니다",
  },
};

/** 区切り記号。日本語は全角、外国語は半角・英語の区切り。 */
const PUNCT = {
  ja: { colon: "：", lp: "（", rp: "）", tilde: "〜", sep: "・", slash: " ／ " },
  en: { colon: ": ", lp: " (", rp: ")", tilde: "-", sep: ", ", slash: " / " },
  ko: { colon: ": ", lp: " (", rp: ")", tilde: "~", sep: "·", slash: " / " },
};
export function punct(lang: Lang): (typeof PUNCT)["ja"] { return PUNCT[lang] ?? PUNCT.ja; }

/** 型の見出し。日本語は系統名、外国語は系統の番号（想定型セクションと同じ）＋分けた型の枝番（Set 1a）。系統名の無い型は null。 */
export function archTitle(b: { arch?: string; archNo?: number; archSub?: string }, lang: Lang, fallbackNo: number): string | null {
  if (!b.arch) return null;
  if (lang === "ja") return b.arch;
  const n = `${b.archNo ?? fallbackNo}${b.archSub ?? ""}`;
  return lang === "en" ? `Set ${n}` : `샘플 ${n}`;
}

const esc = (s: string): string =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c] as string));
const f1 = (x: number): string => (x < 10 ? x.toFixed(1) : String(Math.round(x)));

export function symClass(sym: string): string {
  return sym === "◎" || sym === "○" ? "muc-good" : sym === "△" ? "muc-mid" : "muc-bad";
}

/** 棒の配置。工房の muLayout と同じ: 左から積み、回復したら棒を戻して下の段に積む。100%で止める。 */
function layout(items: { dmg: number; heal: number }[]) {
  const out: { kind: "seg" | "heal"; i: number; lane: number; left: number; width: number }[] = [];
  let pos = 0, lane = 0;
  items.forEach((it, i) => {
    if (pos >= 100) return;
    out.push({ kind: "seg", i, lane, left: pos, width: Math.max(0, Math.min(it.dmg, 100 - pos)) });
    pos += it.dmg;
    if (it.heal > 0 && pos < 100) {
      const hs = Math.max(0, pos - it.heal);
      out.push({ kind: "heal", i, lane, left: hs, width: pos - hs });
      pos = hs;
      lane++;
    }
  });
  const lanes = out.reduce((m, L) => (L.kind === "seg" ? Math.max(m, L.lane + 1) : m), 1);
  return { out, lanes };
}

function raceBar(t: (typeof TXT)["ja"], turns: SeqStep[], hits: number, isOpp: boolean, ko: boolean, died: boolean, selfKo: boolean,
                 tMove: (n: string) => string, defHp: number, lang: Lang, ownerIcon: string, ownerName: string,
                 raceItems: BarItem[] | null): string {
  const used: string[] = [];
  turns.forEach((tn) => { if (tn.n && !tn.flinch && !tn.idle && used[used.length - 1] !== tn.n) used.push(tn.n); });
  const P = punct(lang);
  const title = `${isOpp ? t.barOpp : t.barMe}${used.length ? `${P.lp}${used.map(tMove).join(" → ")}${P.rp}` : ""}`;
  // 区間は判定の対戦の経過(race)の発生順（raceBarItems）。無い旧データだけ毎ターン行から作る。
  let items: BarItem[];
  if (raceItems) {
    items = raceItems;
  } else {
    items = [];
    turns.forEach((tn, ti) => {
      const lbl = stepLabel(tn, ti);
      const turn = tn.turn ?? ti + 1;
      if (!tn.flinch && !tn.idle) items.push({ sub: "move", dmg: tn.pctDealt ?? tn.pctLo ?? 0, heal: 0, lbl, turn, move: tn.n, pctLo: tn.pctLo, pctHi: tn.pctHi });
      (tn.extra ?? []).forEach((x) => { if (x.pct > 0) items.push({ sub: x.kind, dmg: x.pct, heal: 0, lbl: extraLabel(x, lbl), turn }); });
      if ((tn.healPct ?? 0) > 0) items.push({ sub: "heal", dmg: 0, heal: tn.healPct!, lbl, turn });
    });
  }
  // 棒の左に、その棒が削っているHPの持ち主（自分→相手なら相手、相手→自分なら自分）のアイコン
  const ico = ownerIcon ? `<img class="muc-bar-ico" src="${esc(ownerIcon)}" alt="${esc(ownerName)}" title="${esc(ownerName)}" loading="lazy">` : "";
  if (!items.some((it) => it.dmg > 0 || it.heal > 0)) {
    return `<div class="muc-race"><div class="muc-race-lbl"><span>${esc(title)}</span><span>${esc(died ? t.fellFirst : t.noDmg)}</span></div><div class="muc-bar-row">${ico}<div class="muc-bar"></div></div></div>`;
  }
  const { out, lanes } = layout(items);
  // 倒れた側の棒は必ず右端まで埋める（%の丸めで僅かに届かないのを、最後のセグメントで埋める）。
  if (ko || selfKo) {
    const segsOnly = out.filter((L) => L.kind === "seg" && L.width > 0);
    const last = segsOnly[segsOnly.length - 1];
    if (last && last.left + last.width < 100) last.width = 100 - last.left;
  }
  const hpOf = (pct: number) => Math.round(pct * defHp / 100);
  const laneStyle = (L: { lane: number }) => (lanes > 1 ? `top:${(L.lane * 100 / lanes).toFixed(2)}%;height:${(100 / lanes).toFixed(2)}%;bottom:auto;` : "");
  const segs = out.map((L) => {
    const it = items[L.i];
    if (L.kind === "heal") {
      return `<span class="muc-heal" style="top:calc(${((L.lane + 1) * 100 / lanes).toFixed(2)}% - 5px);height:5px;bottom:auto;left:${L.left.toFixed(2)}%;width:${L.width.toFixed(2)}%"></span>`;
    }
    if (it.sub === "heal" || L.width <= 0) return "";
    // 技以外のHP減少は原因のカテゴリ（自分の行動による自傷・天候・状態異常・ばけのかわ等）で見た目を分け、
    // 幅があれば「短縮名＋番号」（例: 肌2）を入れる
    const cls = it.sub === "move" ? (isOpp ? "muc-seg-foe" : "muc-seg-me") : `muc-seg-self muc-seg-${causeCat(it.sub)}`;
    // ターン番号はターン帯に出すので区間には入れない。後から動いた行動は小さな印、幅があれば技名（原因は短縮名）。
    const late = it.order === "late" ? `<small class="muc-late">${esc(lateMark(lang))}</small>` : "";
    const name = it.sub === "move" ? (it.move ? tMove(it.move) : "") : causeShort(it.sub, lang);
    const label = it.sub === "move"
      ? (L.width >= 22 ? `${late}${esc(name)}` : L.width >= 6 ? late : "")
      : (L.width >= 9 ? `${late}${esc(name)}` : L.width >= 5 ? esc(name) : "");
    // タップで詳細（ターン番号・技名/原因・実際に減ったHPと%・技の幅）を出す。表示は bindMuCardClicks。
    const mv = it.move ? tMove(it.move) : "";
    const what = it.sub === "move" ? mv
      : it.sub === "disguise" ? `${mv} → ${causeLabel("disguise", lang)}`
      : `${ownerName}${P.colon}${causeLabel(it.sub, lang)}`;
    const range = it.sub === "move" && it.pctLo != null && it.pctHi != null ? t.range(f1(it.pctLo), f1(it.pctHi)) : "";
    const got = `${hpOf(it.dmg)} (${f1(it.dmg)}%)`;
    const head = raceItems ? turnTag(it, lang) : t.turnN(it.lbl);
    const detail = range
      ? `${head} ${what}${P.colon}${range}${(it.dmg < (it.pctLo ?? 0) - 0.05 ? t.simCap : t.simAt)(got)}`
      : `${head} ${what}${P.colon}${got}`;
    return `<button type="button" class="muc-seg ${cls}" style="${laneStyle(L)}left:${L.left.toFixed(2)}%;width:${L.width.toFixed(2)}%" `
      + `title="${esc(detail)}" data-muc-d="${esc(detail)}">${label ? `<span class="muc-seg-lbl">${label}</span>` : ""}</button>`;
  }).join("");
  // ターンの帯: 同じターンの区間がひとまとまりだと分かるよう、棒の上にターンごとの範囲（T1, T2…）を交互の色で示す
  const turnSpan = new Map<number, [number, number]>();
  out.forEach((L) => {
    if (L.kind !== "seg" || L.width <= 0) return;
    const it = items[L.i];
    const cur = turnSpan.get(it.turn);
    const r: [number, number] = [L.left, L.left + L.width];
    turnSpan.set(it.turn, cur ? [Math.min(cur[0], r[0]), Math.max(cur[1], r[1])] : r);
  });
  const bands = [...turnSpan.entries()].sort((a, b) => a[0] - b[0]).map(([tn, [l, r]], k) =>
    `<span class="muc-tband${k % 2 ? " muc-tband-alt" : ""}" style="left:${l.toFixed(2)}%;width:${Math.max(0, r - l).toFixed(2)}%">${r - l >= 6 ? `T${tn}` : ""}</span>`).join("");
  const acc = items.reduce((a, it) => a + it.dmg - it.heal, 0);
  const right = ko ? (isOpp ? t.koOpp(hits) : t.koMe(hits))
    : selfKo ? (isOpp ? t.selfKoMe : t.selfKoOpp)
    : died ? t.stopped(Math.min(99, Math.max(0, Math.round(acc))))
    : t.part(Math.min(99, Math.max(1, Math.round(acc))));
  // 凡例は、この棒に実際に出ている原因だけを原因名で出す
  const kinds = [...new Set(items.filter((it) => it.sub !== "move" && it.sub !== "heal" && it.dmg > 0).map((it) => it.sub))];
  const anyHeal = items.some((it) => it.sub === "heal");
  const legend = kinds.length || anyHeal
    ? `<div class="muc-legend">${anyHeal ? `<i class="muc-heal-key"></i>${esc(isOpp ? t.healKeyMe : t.healKey)}` : ""}`
      + kinds.map((k) => `<i class="muc-seg-self muc-seg-${causeCat(k)}"></i>${esc(causeLabel(k, lang))}`).join("") + `</div>`
    : "";
  return `<div class="muc-race"><div class="muc-race-lbl"><span>${esc(title)}</span><span>${esc(right)}</span></div>`
    + `<div class="muc-bar-row">${ico}<div class="muc-bar-col"><div class="muc-tbands">${bands}</div>`
    + `<div class="muc-bar"${lanes > 1 ? ` style="height:${lanes * 20}px"` : ""}>${segs}${ko ? `<span class="muc-ko">✕</span>` : selfKo ? `<span class="muc-ko muc-ko-self">✕</span>` : ""}</div></div></div>${legend}</div>`;
}

function moveBars(list: MoveDamage[], mine: boolean, tMove: (n: string) => string, lang: Lang, hasMoves = true): string {
  const t = TXT[lang] ?? TXT.ja;
  if (!list.length) return `<div class="muc-mv-none">${esc(hasMoves ? t.noEffMove : t.noMoves)}</div>`;
  const P = punct(lang);
  // 技名の下に、その数値の前提（連続技の回数・天候/フィールド・能力変化）と相性（効果抜群 ×2・へんげんじざい後のタイプ）を小さく出す。
  return [...list].sort((a, b) => b.pctHi - a.pctHi).map((m) => {
    const notes = [condText(m.conds, lang), effLabel(m.eff, lang)].filter(Boolean).join(" / ");
    return `<div class="muc-mv${mine ? " muc-mv-me" : ""}"><span class="muc-mv-n">${esc(tMove(m.n))}`
    + `${notes ? `<small class="muc-mv-c">${esc(notes)}</small>` : ""}</span>`
    + `<span class="muc-mv-g"><i class="hi" style="width:${Math.min(100, m.pctHi).toFixed(1)}%"></i><i class="lo" style="width:${Math.min(100, m.pctLo).toFixed(1)}%"></i></span>`
    + `<span class="muc-mv-p">${f1(m.pctLo)}${P.tilde}${f1(m.pctHi)}%</span></div>`;
  }).join("");
}

/** カードの棒のセグメント(button)をタップ/クリック/Enterしたとき、そのカードの詳細欄に内容を出す。ページで1回呼ぶ。 */
export function bindMuCardClicks(root: Document | HTMLElement): void {
  root.addEventListener("click", (e) => {
    if (e.target && handleReplayClick(e.target as Element)) return;
    const seg = (e.target as Element | null)?.closest?.(".muc-seg[data-muc-d]") as HTMLElement | null;
    if (!seg) return;
    const box = seg.closest(".muc-card")?.querySelector(".muc-segdetail") as HTMLElement | null;
    if (!box) return;
    box.textContent = seg.dataset.mucD ?? "";
    box.hidden = false;
  });
}

export function renderMuCard(vm: MuCardVM, lang: Lang): string {
  const t = TXT[lang] ?? TXT.ja;
  const P = punct(lang);
  const v = vm.verdict;
  let head: string, body = "";
  if (v.stall?.side) {
    head = v.stall.side === "me" ? t.stallWin : t.stallLose;
  } else if (v.draw) {
    head = t.draw;
  } else if (v.mutual) {
    head = t.mutual; body = t.mutualBody(v.mutualTurn ?? v.myHits ?? 0);
  } else {
    head = v.win ? t.win : t.lose;
    body = `${t.my(v.myHits ?? 999)}${P.slash}${t.opp(v.oppHits ?? 999)}`;
  }
  const race = v.race;
  const fainted = (side: 0 | 1) => !!race && race.some((e) => e.hp[side] <= 0);
  const single = (d: MoveHitDetail | null): SeqStep[] =>
    d && d.pctLo != null ? [{ n: d.n, pctLo: d.pctLo, pctHi: d.pctHi, conds: null }] : [];
  const myTurns = race ? vm.myTurns : (vm.myTurns.length > 1 ? vm.myTurns : single(vm.my));
  const oppTurns = race ? vm.oppTurns : (vm.oppTurns.length > 1 ? vm.oppTurns : single(vm.opp));
  // ✕ は自分の技で相手を倒したときだけ（相手の反動等の自滅では付けない）。
  const myKo = race ? koByMove(race, 0) : (v.myHits ?? 999) < 999;
  const oppKo = race ? koByMove(race, 1) : (v.oppHits ?? 999) < 999;
  return `<div class="muc-card">`
    + `<div class="muc-head"><span class="muc-sym ${symClass(v.sym)}">${esc(v.sym)}</span>`
    + `<span class="muc-tag">${esc(v.mutual ? t.mutual : v.tie ? t.tie : v.koFirst ? t.first : t.second)}</span>`
    + `</div>`
    + `<div class="muc-tags">${vm.chips.filter(Boolean).map((c) => `<span class="muc-tag">${esc(c)}</span>`).join("")}</div>`
    + `<div class="muc-evline"><b>${esc(vm.evLabel)}</b><span>${P.lp.trim()}S ${v.myS} vs ${v.oppS}${P.rp}</span></div>`
    + `<div class="muc-vbox ${symClass(v.sym)}"><b>${esc(head)}</b>${body ? `<span>${esc(body)}</span>` : ""}`
    + `<small class="muc-basis">${esc(t.basis)}</small></div>`
    + raceBar(t, myTurns, v.myHits ?? 999, false, myKo, fainted(0), !!race && !myKo && fainted(1), vm.tMove, vm.hpOpp, lang, vm.oppIcon ?? "", vm.oppName ?? "",
              race ? raceBarItems(race, 1, vm.hpOpp, vm.myTurns) : null)
    + raceBar(t, oppTurns, v.oppHits ?? 999, true, oppKo, fainted(1), !!race && !oppKo && fainted(0), vm.tMove, vm.hpMe, lang, vm.myIcon ?? "", vm.myName ?? "",
              race ? raceBarItems(race, 0, vm.hpMe, vm.oppTurns) : null)
    + `<div class="muc-segdetail" hidden aria-live="polite"></div><div class="muc-seghint">${esc(t.segHint)}</div>`
    + (v.tie ? `<div class="muc-legend">${esc(t.tieNote)}</div>` : "")
    + `<div class="muc-mv-h">${esc(t.movesMe)}</div>${moveBars(vm.myMoves, true, vm.tMove, lang, vm.myHasMoves ?? true)}`
    + `<div class="muc-mv-h">${esc(t.movesOpp)}</div>${moveBars(vm.oppMoves, false, vm.tMove, lang, vm.oppHasMoves ?? true)}`
    // くわしい内訳 = 判定に使った対戦の再生（1ターンずつ）。経過(race)が無い旧データ・持久戦の上書き時は従来の表。
    + (race
      ? `<details class="muc-detail"><summary>${esc(t.replay)}</summary>${renderReplay({
          race, init: (v as { raceInit?: never }).raceInit ?? null,
          names: [vm.myName ?? "", vm.oppName ?? ""], icons: [vm.myIcon ?? "", vm.oppIcon ?? ""], maxHp: [vm.hpMe, vm.hpOpp],
          tMove: vm.tMove, tItem: vm.tItem ?? ((n: string) => n), tPoke: vm.tPoke, tAbility: vm.tAbility,
        }, lang)}</details>`
      : `<details class="muc-detail"><summary>${esc(t.detail)}</summary>${vm.detailHtml}</details>`)
    + `</div>`;
}

/** 型ごとのカードをタブで切り替える（CSSだけで切り替わる。uid はページ内で一意に）。
 * 見出しは型の系統名(arch)＋想定使用率(share%)と記号。既定は defaultIdx（割合が最大の型）。 */
export function renderMuTabs(tabs: { title: string; share: string; sym: string; html: string }[], uid: string,
                             defaultIdx: number, capLabel: string): string {
  if (tabs.length <= 1) return tabs[0]?.html ?? "";
  const radios = tabs.map((_, i) =>
    `<input type="radio" class="muc-tab-radio" name="${esc(uid)}" id="${esc(uid)}-${i}"${i === defaultIdx ? " checked" : ""}>`).join("");
  const labels = tabs.map((tb, i) =>
    `<label class="muc-tab" for="${esc(uid)}-${i}"><span class="muc-tab-sym ${symClass(tb.sym)}">${esc(tb.sym)}</span>`
    + `${esc(tb.title)}${tb.share ? `<span class="muc-tab-share">${esc(tb.share)}</span>` : ""}</label>`).join("");
  const panels = tabs.map((tb) => `<div class="muc-tab-panel">${tb.html}</div>`).join("");
  return `<div class="muc-tabs">${radios}<div class="muc-tab-labels"><span class="muc-tab-cap">${esc(capLabel)}</span>${labels}</div>`
    + `<div class="muc-tab-panels">${panels}</div></div>`;
}

/** 1v1ポップアップ（ポケモン情報ページ・対策ページ）の1枚ぶんのデータ。名前は和名のまま持ち、表示時に dict で訳す。
 * ページに埋め込むJSONを小さくするため、null・false の項目は省いてある（読む側は無い＝null/false とみなす）。 */
export interface MuPopupRow {
  /** 相手の型のタブ見出し・割合・記号（翻訳済み） */
  t: string; sh: string; sym: string;
  chips: string[]; ev: string;
  /** 相手の最大HP・アイコンID */
  hp: number; ic: string;
  v: Verdict;
  mt?: SeqStep[]; ot?: SeqStep[];
  md?: MoveHitDetail | null; od?: MoveHitDetail | null;
  mm?: MoveDamage[]; om?: MoveDamage[];
  /** 技が1つも無い（「技が未設定」を出す） */
  nmh?: boolean; noh?: boolean;
}
export interface MuPopupMine {
  /** 自分の型のタブ見出し・補足（割合か努力値） */
  t: string; sub: string;
  hp: number; ic: string;
  /** 既定で開く相手の型 */
  def?: number;
  rows: MuPopupRow[];
}
export interface MuPopupData {
  mine: MuPopupMine[];
  def?: number;
  /** 和名→表示名（技 m・持ち物 i・ポケモン p・特性 a）。日本語版は空 */
  dict?: { m?: Record<string, string>; i?: Record<string, string>; p?: Record<string, string>; a?: Record<string, string> };
}

const POPUP_TXT = {
  ja: { my: "自分の型", opp: "相手の型" },
  en: { my: "Your build", opp: "Opponent build" },
  ko: { my: "내 빌드", opp: "상대 빌드" },
};

/** 1v1ポップアップの中身（自分の型タブ・相手の型タブ・カード）。ポップアップを開いたときにクライアントで組み立てる。 */
export function renderMuPopup(d: MuPopupData, lang: Lang,
                              ctx: { myName: string; oppName: string; myIcon: string; oppIcon: string; uid: string }): string {
  const L = POPUP_TXT[lang] ?? POPUP_TXT.ja;
  const tr = (m?: Record<string, string>) => (n: string) => (n && m?.[n]) || n;
  const tMove = tr(d.dict?.m), tItem = tr(d.dict?.i), tPoke = tr(d.dict?.p), tAbility = tr(d.dict?.a);
  const tMoveDash = (n: string | null | undefined) => (n ? tMove(n) : "—");
  const sprite = (ic: string) => `/images/pokemon/pokemon-${ic}.webp`;
  const uid = esc(ctx.uid);
  const multi = d.mine.length > 1;
  const withPct = <T extends { dmgLo?: number | null; dmgHi?: number | null; pctLo?: number | null; pctHi?: number | null }>(m: T | null | undefined, hp: number): T | null =>
    !m ? null : m.pctLo == null && m.dmgLo != null && m.dmgHi != null ? { ...m, pctLo: (m.dmgLo / hp) * 100, pctHi: (m.dmgHi / hp) * 100 } : m;
  const card = (me: MuPopupMine, r: MuPopupRow): string => {
    type St = { sides: { hp?: number; stg?: number[] }[] };
    const full = (x: St, hp?: number[]): St => ({ ...x, sides: x.sides.map((sd, z) => ({ ...sd, hp: sd.hp ?? hp?.[z], stg: sd.stg ?? [0, 0, 0, 0, 0] })) });
    let st: St | null = null;
    const init = (r.v as { raceInit?: St }).raceInit;
    const v: Verdict = r.v.race ? {
      ...r.v,
      ...(init ? { raceInit: full(init) } : {}),
      race: r.v.race.map((e) => {
        const cur = (e as { st?: St }).st;
        if (cur) st = full(cur, e.hp);
        return { ...e, st: st ?? undefined };
      }),
    } : r.v;
    const md = withPct(r.md, r.hp), od = withPct(r.od, me.hp), mt = r.mt ?? [], ot = r.ot ?? [];
    const trs = (xs: SeqStep[]) => xs.map((x) => ({ ...x, n: tMove(x.n) }));
    const detailHtml = v.race ? "" : renderAssumptions(lang) + renderMatchupTable({
      myName: ctx.myName, oppName: ctx.oppName, myIconUrl: sprite(ctx.myIcon), oppIconUrl: sprite(ctx.oppIcon),
      columns: [{
        label: "", meta: [], my: md, opp: od, verdict: v,
        stallSeq: v.stall?.seq.map((n) => tMove(n)),
        myTurns: trs(mt), oppTurns: trs(ot),
        myMoveText: tMoveDash(md?.n ?? v.myMove), oppMoveText: tMoveDash(od?.n ?? v.oppMove),
      }],
    }, lang, { compact: true });
    return renderMuCard({
      verdict: v, chips: r.chips, evLabel: r.ev,
      myTurns: mt, oppTurns: ot, my: md, opp: od,
      myMoves: (r.mm ?? []).map((m) => withPct(m, r.hp)!), oppMoves: (r.om ?? []).map((m) => withPct(m, me.hp)!), myHasMoves: !r.nmh, oppHasMoves: !r.noh,
      detailHtml, tMove, hpOpp: r.hp, hpMe: me.hp,
      myIcon: sprite(me.ic), oppIcon: sprite(r.ic), myName: ctx.myName, oppName: ctx.oppName,
      tItem, tPoke, tAbility,
    }, lang);
  };
  let h = "";
  if (multi) {
    h += d.mine.map((_, i) => `<input type="radio" name="mbp-tab-${uid}" id="mbp-tab-${uid}-${i}" class="mbp-tab-radio"${i === (d.def ?? 0) ? " checked" : ""}>`).join("");
    h += `<div class="mbp-tab-labels"><span class="mbp-tab-cap">${esc(L.my)}</span>`
      + d.mine.map((me, i) => `<label for="mbp-tab-${uid}-${i}" class="mbp-tab-label">${esc(me.t)}<span class="mbp-tab-sub">${esc(me.sub)}</span></label>`).join("")
      + `</div>`;
  }
  h += `<div class="mbp-tab-panels ${multi ? "" : "single"}">` + d.mine.map((me, i) => {
    const multiOpp = me.rows.length > 1;
    let p = `<div class="mbp-tab-panel">`;
    if (multiOpp) {
      p += me.rows.map((_, j) => `<input type="radio" name="mbp-otab-${uid}-${i}" id="mbp-otab-${uid}-${i}-${j}" class="mbp-otab-radio"${j === (me.def ?? 0) ? " checked" : ""}>`).join("");
      p += `<div class="mbp-otab-labels"><span class="mbp-tab-cap">${esc(L.opp)}</span>`
        + me.rows.map((r, j) => `<label for="mbp-otab-${uid}-${i}-${j}" class="mbp-otab-label"><span class="mbp-otab-sym ${symClass(r.sym)}">${esc(r.sym)}</span>${esc(r.t)}<span class="mbp-tab-sub">${esc(r.sh)}</span></label>`).join("")
        + `</div>`;
    }
    p += `<div class="mbp-otab-panels ${multiOpp ? "" : "single"}">` + me.rows.map((r) => `<div class="mbp-otab-panel">${card(me, r)}</div>`).join("") + `</div>`;
    return p + `</div>`;
  }).join("") + `</div>`;
  return h;
}
