// 対戦アシスト（叩き台）: パーティ工房の自パーティ × 相手1匹を、想定型テンプレごとにその場で試算する。
// 判定・ダメージはすべて工房と同じエンジン経路（judge1v1 / pairHitDetails / moveDamages）を使い、
// 相手・自分の型は保存操作なしで編集でき、変えた瞬間に技ごとのダメージが再計算される。
import { loadCore, loadMon, type CoreData } from "../party-builder/data";
import { loadStore, saveStore, createPartyFromSlots } from "../party-builder/storage";
import { importParty } from "../party-builder/spec";
import { resolveSlot } from "../party-builder/balance";
import { judge1v1, moveDamages, pairHitDetails, fmtKoProbPct, type MoveDamage, type MoveHitDetail } from "../party-builder/matchup";
import { symClass, archTitle } from "../party-builder/mu-card";
import { abilityText, openMuDialog } from "../party-builder/mu-cell-popup";
import { itemNameOf } from "../../i18n/game-terms";
import { initEngine, setScenario, setupMoveNames, type Scenario } from "../engine/wasm";
import { ALL_NATURES, EV_STAT_MAX, EV_TOTAL_MAX, natureDisp } from "../party-builder/stats";
import type { MonDetail, ResolvedBuild, Slot, StatArray, Store, TargetBuild } from "../party-builder/types";

const STATE_KEY = "pn-battle-v1";

type Lang = "ja" | "en" | "ko";
const L: Lang = (window as any).__BA_LANG__ ?? "ja";
const MAPS: Record<string, Record<string, string>> = (window as any).__BA_MAPS__ ?? {};
const PFX = L === "ja" ? "" : `/${L}`;
const tr = (m?: Record<string, string>) => (n: string) => (n && m?.[n]) || n;
const tMove = tr(MAPS.move), tAbil = tr(MAPS.ability), tNat = tr(MAPS.nature), tType = tr(MAPS.type);
function tPoke(n: string): string {
  if (!n || L === "ja") return n;
  const map = MAPS.poke ?? {};
  if (map[n]) return map[n];
  if (n.startsWith("メガ")) {
    const rest = n.slice(2);
    let base = map[rest], suf = "";
    if (!base && /[XYZ]$/.test(rest)) { suf = rest.slice(-1); base = map[rest.slice(0, -1)]; }
    if (base) return L === "ko" ? `메가${base}${suf}` : `Mega ${base}${suf ? ` ${suf}` : ""}`;
  }
  return n;
}
const tItem = (n: string) => (L === "ja" || !n ? n : itemNameOf(n, L, MAPS.item ?? {}, MAPS.poke ?? {}));
function tNatDisp(na: string): string {
  if (!na) return "";
  const raw = natureDisp(na);
  return raw.startsWith(na) ? tNat(na) + raw.slice(na.length) : tNat(na);
}
const typesTxt = (a: string, b: string | null) => [a, b].filter(Boolean).map((x) => tType(x!)).join(L === "ja" ? "・" : " / ");
const paren = (x: string) => (L === "ja" ? `（${x}）` : ` (${x})`);

const TX = {
  ja: {
    noParty: "パーティ工房に保存したパーティがここに出ます。まだこのブラウザにパーティがありません。", makeInBuilder: "パーティ工房で作る",
    demo: "サンプルのパーティで試す", importSum: "工房のエクスポート文字列を貼り付ける", importPh: "工房の「エクスポート」でコピーした6行",
    importBtn: "読み込む", importErr: "6行の形式で読み込めませんでした", importName: "読み込んだパーティ", demoName: "サンプル（使用率上位）",
    myParty: "自分のパーティ", editInBuilder: "工房で編集", notFound: "見つかりません", more: (n: number) => `ほか${n}匹`,
    noSetup: "積み技なし", setupPre: "を", setupLong: "回使った状態", setupShort: "回", dec: "減らす", inc: "増やす",
    item: "持ち物", ability: "特性", nature: "性格", moves: "技", none: "なし", total: "合計", noEv: "無振り",
    evAria: (x: string) => `${x}のEV`, decAria: (x: string) => `${x}を減らす`, incAria: (x: string) => `${x}を増やす`, moveAria: (n: number) => `技${n}`,
    promptOpp: "相手のポケモンを選ぶと、技ごとのダメージがここに出ます。", promptParty: "自分のパーティを選んでください。", calcErr: "型を計算できませんでした", muOpen: "1v1の内訳・対戦の再生",
    me: "自分", opp: "相手", edit: "編集", done: "完了", adjusting: "調整中", edited: "編集",
    dirtyNote: "この調整はこのページに記憶されています（工房のパーティは元のまま）", save: "工房のパーティに上書き保存", discard: "工房の型に戻す",
    setLbl: "型", setAria: "相手の型", tplFallback: (k: number) => `型${k}`, tplReset: "この型をテンプレに戻す",
    weather: "天候", terrain: "フィールド", weatherAuto: "特性まかせ",
    W: { "晴れ": "晴れ", "雨": "雨", "すなあらし": "すなあらし", "あられ": "あられ" } as Record<string, string>,
    T: { "エレキフィールド": "エレキフィールド", "グラスフィールド": "グラスフィールド", "サイコフィールド": "サイコフィールド", "ミストフィールド": "ミストフィールド" } as Record<string, string>,
    ko: (n: number) => `確${n}`, koR1: (p: number) => `乱1(${p}%)`, koRn: (n: number) => `乱${n}`, survive: "※耐",
    immune: "無効", mutual: "相打ち", tie: "同速", first: "先手", second: "後手",
    scenMe: (n: number) => `自分${n}積み`, scenOpp: (n: number) => `相手${n}積み`, sep: "・",
    dmMe: "自分 → 相手", dmOpp: "相手 → 自分", usage: "数字は採用率", noDmg: "有効なダメージ技なし", tplNoDmg: "型の技にダメージ技なし", extra: "ほかに持ちうる技",
    barOut: "与", barIn: "被",
    hNone: "有効打なし", h6: "6発以上", hR1: (p: number) => `乱数1発(約${p}%)`, hRn: (n: number) => `乱数${n}発`, hC: (n: number) => `確定${n}発`, hRp: (n: number, p: string) => `乱数${n}発(${p}%)`,
    confirmSave: (party: string, sp: string) => `工房のパーティ「${party}」の ${sp} をこの型で上書きします。`, loadFail: "読み込みに失敗しました。再読み込みしてください。",
  },
  en: {
    noParty: "Parties saved in the Party Workshop appear here. This browser has no saved parties yet.", makeInBuilder: "Build in the Party Workshop",
    demo: "Try with a sample party", importSum: "Paste a Workshop export", importPh: "The 6 lines copied with Export in the Workshop",
    importBtn: "Load", importErr: "Couldn't read it as 6 lines", importName: "Imported party", demoName: "Sample (top usage)",
    myParty: "Your party", editInBuilder: "Edit in Workshop", notFound: "No matches", more: (n: number) => `+${n} more`,
    noSetup: "No setup move", setupPre: "", setupLong: "use(s)", setupShort: "×", dec: "Decrease", inc: "Increase",
    item: "Item", ability: "Ability", nature: "Nature", moves: "Moves", none: "None", total: "Total", noEv: "No EVs",
    evAria: (x: string) => `${x} EV`, decAria: (x: string) => `Decrease ${x}`, incAria: (x: string) => `Increase ${x}`, moveAria: (n: number) => `Move ${n}`,
    promptOpp: "Pick the opponent's Pokémon to see the damage of each move here.", promptParty: "Choose your party.", calcErr: "Couldn't calculate this set", muOpen: "1v1 breakdown & replay",
    me: "You", opp: "Opp", edit: "Edit", done: "Done", adjusting: "Adjusted", edited: "Edited",
    dirtyNote: "These changes are kept on this page (your Workshop party is unchanged)", save: "Overwrite Workshop party", discard: "Revert to Workshop set",
    setLbl: "Set", setAria: "Opponent set", tplFallback: (k: number) => `Set ${k}`, tplReset: "Reset this set",
    weather: "Weather", terrain: "Terrain", weatherAuto: "From abilities",
    W: { "晴れ": "Sun", "雨": "Rain", "すなあらし": "Sandstorm", "あられ": "Hail" } as Record<string, string>,
    T: { "エレキフィールド": "Electric Terrain", "グラスフィールド": "Grassy Terrain", "サイコフィールド": "Psychic Terrain", "ミストフィールド": "Misty Terrain" } as Record<string, string>,
    ko: (n: number) => (n === 1 ? "OHKO" : `${n}HKO`), koR1: (p: number) => `${p}% OHKO`, koRn: (n: number) => `${n}HKO?`, survive: "*survives",
    immune: "Immune", mutual: "Double KO", tie: "Speed tie", first: "First", second: "Second",
    scenMe: (n: number) => `You +${n}`, scenOpp: (n: number) => `Opp +${n}`, sep: " / ",
    dmMe: "You → Opponent", dmOpp: "Opponent → You", usage: "% = usage", noDmg: "No damaging moves", tplNoDmg: "No damaging moves in this set", extra: "Other possible moves",
    barOut: "Atk", barIn: "Def",
    hNone: "No damaging move", h6: "6+ hits", hR1: (p: number) => `~${p}% OHKO`, hRn: (n: number) => `possible ${n}HKO`, hC: (n: number) => (n === 1 ? "OHKO" : `${n}HKO`), hRp: (n: number, p: string) => `${p}% ${n === 1 ? "OHKO" : `${n}HKO`}`,
    confirmSave: (party: string, sp: string) => `Overwrite ${sp} in Workshop party "${party}" with this set?`, loadFail: "Failed to load. Please reload the page.",
  },
  ko: {
    noParty: "파티 공방에 저장한 파티가 여기에 표시됩니다. 이 브라우저에는 아직 파티가 없습니다.", makeInBuilder: "파티 공방에서 만들기",
    demo: "샘플 파티로 체험하기", importSum: "공방 내보내기 문자열 붙여넣기", importPh: "공방의 '내보내기'로 복사한 6줄",
    importBtn: "불러오기", importErr: "6줄 형식으로 읽을 수 없습니다", importName: "불러온 파티", demoName: "샘플(사용률 상위)",
    myParty: "내 파티", editInBuilder: "공방에서 편집", notFound: "찾을 수 없습니다", more: (n: number) => `외 ${n}마리`,
    noSetup: "랭크업 기술 없음", setupPre: "", setupLong: "회 사용한 상태", setupShort: "회", dec: "줄이기", inc: "늘리기",
    item: "도구", ability: "특성", nature: "성격", moves: "기술", none: "없음", total: "합계", noEv: "무보정",
    evAria: (x: string) => `${x} EV`, decAria: (x: string) => `${x} 줄이기`, incAria: (x: string) => `${x} 늘리기`, moveAria: (n: number) => `기술 ${n}`,
    promptOpp: "상대 포켓몬을 고르면 기술별 대미지가 여기에 표시됩니다.", promptParty: "내 파티를 선택하세요.", calcErr: "이 샘플을 계산할 수 없습니다", muOpen: "1v1 상세・대전 재생",
    me: "나", opp: "상대", edit: "편집", done: "완료", adjusting: "조정 중", edited: "편집됨",
    dirtyNote: "이 조정은 이 페이지에 저장되어 있습니다(공방 파티는 그대로)", save: "공방 파티에 덮어쓰기", discard: "공방 샘플로 되돌리기",
    setLbl: "샘플", setAria: "상대 샘플", tplFallback: (k: number) => `샘플 ${k}`, tplReset: "이 샘플 초기화",
    weather: "날씨", terrain: "필드", weatherAuto: "특성에 따름",
    W: { "晴れ": "쾌청", "雨": "비", "すなあらし": "모래바람", "あられ": "싸라기눈" } as Record<string, string>,
    T: { "エレキフィールド": "일렉트릭필드", "グラスフィールド": "그래스필드", "サイコフィールド": "사이코필드", "ミストフィールド": "미스트필드" } as Record<string, string>,
    ko: (n: number) => `확${n}`, koR1: (p: number) => `난1(${p}%)`, koRn: (n: number) => `난${n}`, survive: "※버팀",
    immune: "무효", mutual: "상쇄", tie: "동속", first: "선공", second: "후공",
    scenMe: (n: number) => `나 ${n}회 랭크업`, scenOpp: (n: number) => `상대 ${n}회 랭크업`, sep: " · ",
    dmMe: "나 → 상대", dmOpp: "상대 → 나", usage: "숫자는 채용률", noDmg: "유효한 대미지 기술 없음", tplNoDmg: "이 샘플에 대미지 기술 없음", extra: "그 밖에 가능한 기술",
    barOut: "공격", barIn: "피격",
    hNone: "유효타 없음", h6: "6타 이상", hR1: (p: number) => `난수 1타(약 ${p}%)`, hRn: (n: number) => `난수 ${n}타`, hC: (n: number) => `확정 ${n}타`, hRp: (n: number, p: string) => `난수 ${n}타(${p}%)`,
    confirmSave: (party: string, sp: string) => `공방 파티 「${party}」의 ${sp}을(를) 이 샘플로 덮어씁니다.`, loadFail: "불러오기에 실패했습니다. 새로고침하세요.",
  },
};
const X = TX[L] ?? TX.ja;
const STAT = ["H", "A", "B", "C", "D", "S"] as const;
const WEATHERS = ["", "晴れ", "雨", "すなあらし", "あられ"] as const;
const TERRAINS = ["", "エレキフィールド", "グラスフィールド", "サイコフィールド", "ミストフィールド"] as const;

interface OppState {
  sp: string;
  icon: string;
  /** 表示中の型（テンプレの番号）。 */
  sel: number;
  /** 型ごとの編集（キー=テンプレの番号）。無い型はテンプレのまま。 */
  edits: Record<number, Slot>;
}

interface BAState {
  partyId: string | null;
  oppMon: OppState | null;
  my: number;
  weather: string;
  terrain: string;
  boostMe: number;
  boostOpp: number;
  /** 複数の積み技を持つときに使う技（無ければ技欄の先頭の積み技）。 */
  setupMe: string;
  setupOpp: string;
  editMe: boolean;
  editOpp: boolean;
  /** 自分のポケモンのこのページだけの調整（パーティID → 枠番号 → 型）。工房へは「上書き保存」したときだけ書く。 */
  myEdits: Record<string, Record<number, Slot>>;
}

const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
const toKata = (s: string) => s.replace(/[ぁ-ゖ]/g, (c) => String.fromCharCode(c.charCodeAt(0) + 0x60));
const sprite = (icon: string) => (icon ? `/images/pokemon/pokemon-${icon}.webp` : "");
const ico = (icon: string, alt: string, cls = "ba-ico") => (icon ? `<img class="${cls}" src="${sprite(icon)}" alt="${esc(alt)}" loading="lazy" decoding="async">` : "");
const f1 = (x: number) => (x < 10 ? x.toFixed(1) : String(Math.round(x)));
const $ = (id: string) => document.getElementById(id)!;

let core: CoreData;
let store: Store;
let st: BAState;
const details = new Map<string, MonDetail>();
let SETUP = new Set<string>();
let pickAll = false;

// ---- 永続化（対戦中の再読み込みで消えないように） ----
function defaultState(): BAState {
  return { partyId: null, oppMon: null, my: 0, weather: "", terrain: "", boostMe: 0, boostOpp: 0, setupMe: "", setupOpp: "", editMe: false, editOpp: false, myEdits: {} };
}
function loadState(): BAState {
  try {
    const raw = localStorage.getItem(STATE_KEY);
    if (!raw) return defaultState();
    const x = JSON.parse(raw);
    const d = defaultState();
    return {
      ...d, ...x,
      oppMon: x.oppMon && typeof x.oppMon.sp === "string" ? x.oppMon : null,
      myEdits: x.myEdits && typeof x.myEdits === "object" ? x.myEdits : {},
    };
  } catch { return defaultState(); }
}
function saveState() {
  try { localStorage.setItem(STATE_KEY, JSON.stringify(st)); } catch { /* 保存不可は無視 */ }
}

// ---- 自分のパーティ ----
function activeParty() {
  return store.parties.find((p) => p.id === st.partyId) ?? store.parties.find((p) => p.id === store.activeId) ?? store.parties[0] ?? null;
}
function mySlots(): Slot[] {
  const p = activeParty();
  return p ? p.slots.filter((s): s is Slot => !!s) : [];
}
function resolveSafe(s: Slot): ResolvedBuild | null {
  try { return resolveSlot(s, core.species, core.moves); } catch { return null; }
}

// ---- 相手の型テンプレ ----
function templatesOf(o: OppState): TargetBuild[] {
  const d = details.get(o.icon);
  if (d?.mu?.length) return d.mu;
  // 代表型の無い種: 採用率1位の組で1型だけ作る
  const top = (xs?: { n: string }[]) => (xs && xs[0] ? xs[0].n : "");
  const sm = core.species.find((s) => s.n === o.sp);
  return [{
    idx: 1, item: top(d?.items), nature: top(d?.natures), ability: top(d?.abilities),
    ev: (d?.evs?.[0]?.ev ?? [0, 0, 0, 0, 0, 0]) as StatArray,
    moves: (d?.moves ?? []).slice(0, 4).map((m) => m.n),
    t1: sm?.t1 ?? "ノーマル", t2: sm?.t2 ?? null, bs: (sm?.bs ?? [50, 50, 50, 50, 50, 50]) as StatArray, spec: "",
  }];
}
function tplSlot(sp: string, b: TargetBuild): Slot {
  return { sp, item: b.item, ability: b.ability, nature: b.nature, evs: [...b.ev] as StatArray, moves: [...b.moves], targets: [] };
}
function oppSlot(o: OppState, k: number): Slot {
  return o.edits[k] ?? tplSlot(o.sp, templatesOf(o)[k] ?? templatesOf(o)[0]);
}
function tplTitle(o: OppState, k: number): string {
  const t = templatesOf(o)[k];
  return (t && archTitle(t, L, k + 1)) || X.tplFallback(k + 1);
}

// ---- 前提（場・積み） ----
function fieldScenario(withBoost: boolean): Scenario | null {
  const s: Scenario = {
    weather: (st.weather || null) as Scenario["weather"],
    terrain: (st.terrain || null) as Scenario["terrain"],
    boost: withBoost ? st.boostMe : 0,
    oppBoost: withBoost ? st.boostOpp : 0,
  };
  return s.weather || s.terrain || s.boost || s.oppBoost ? s : null;
}
function withScenario<T>(s: Scenario | null, fn: () => T): T {
  setScenario(s);
  try { return fn(); } finally { setScenario(null); }
}

function hitTxt(d: MoveHitDetail | null): string {
  if (!d || d.hits == null) return X.hNone;
  if (d.hits >= 999) return X.h6;
  // エンジンの確定数は中央乱数で数える（判定用）。ダメ計の表示としては「最高乱数なら少ない発数で倒せる」
  // ことが消えるので、耐え効果の無い対面に限り、最高乱数で届く発数を乱数として出す（%は16段階の乱数の概算）。
  if (d.certain && !d.reason && d.pctHi != null && d.pctHi > 0) {
    const nHi = Math.ceil(100 / d.pctHi);
    if (nHi < d.hits) {
      if (nHi === 1) {
        let k = 0;
        for (let r = 85; r <= 100; r++) if ((d.pctHi * r) / 100 >= 100) k++;
        return X.hR1(Math.round((k / 16) * 100));
      }
      return X.hRn(nHi);
    }
  }
  return d.certain ? X.hC(d.hits) : X.hRp(d.hits, fmtKoProbPct(d.prob));
}
function rangeTxt(d: MoveHitDetail | null): string {
  return d && d.pctLo != null && d.pctHi != null ? `${f1(d.pctLo)}〜${f1(d.pctHi)}%` : "—";
}
function evStr(evs: readonly number[]): string {
  const s = evs.map((v, i) => (v ? `${STAT[i]}${v}` : "")).filter(Boolean).join(" ");
  return s || X.noEv;
}

// ================= 描画 =================

function render() {
  renderParty();
  renderPicker();
  renderCalc();
  saveState();
}

/** 結果だけ描き直す（EVの入力中など、エディタの入力欄を壊さないため）。 */
function renderResults() {
  renderCalcResults();
  saveState();
}

// ---- 1. 自分のパーティ ----
function renderParty() {
  const el = $("ba-party");
  if (!store.parties.length) {
    el.innerHTML = `<div class="ba-empty">
      <p>${esc(X.noParty)}</p>
      <div class="ba-row">
        <a class="ba-btn" href="${PFX}/party-builder/">${esc(X.makeInBuilder)}</a>
        <button type="button" class="ba-btn-sub" id="ba-demo">${esc(X.demo)}</button>
      </div>
      <details class="ba-import"><summary>${esc(X.importSum)}</summary>
        <textarea id="ba-import-txt" rows="6" placeholder="${esc(X.importPh)}"></textarea>
        <button type="button" class="ba-btn-sub" id="ba-import-btn">${esc(X.importBtn)}</button>
        <span class="ba-err" id="ba-import-err"></span>
      </details>
    </div>`;
    return;
  }
  const p = activeParty()!;
  const opts = store.parties.map((pp) => `<option value="${esc(pp.id)}"${pp.id === p.id ? " selected" : ""}>${esc(pp.name)}</option>`).join("");
  const icons = mySlots().map((s) => {
    const sm = core.species.find((x) => x.n === s.sp);
    return ico(sm?.icon ?? "", tPoke(s.sp), "ba-ico-lg");
  }).join("");
  el.innerHTML = `<div class="ba-party-row">
      <select id="ba-party-sel" class="ba-sel" aria-label="${esc(X.myParty)}">${opts}</select>
      <a class="ba-link" href="${PFX}/party-builder/">${esc(X.editInBuilder)}</a>
    </div>
    <div class="ba-party-icons">${icons}</div>`;
}

function renderSuggest(q: string) {
  const box = $("ba-opp-sug");
  const qq = q.trim();
  if (!qq) { box.hidden = true; box.innerHTML = ""; return; }
  const qk = toKata(qq);
  const ql = qq.toLowerCase();
  const hits = core.species
    .filter((s) => s.n !== st.oppMon?.sp && (s.n.includes(qq) || s.n.includes(qk) || tPoke(s.n).toLowerCase().includes(ql)))
    .sort((a, b) => a.rank - b.rank)
    .slice(0, 8);
  box.innerHTML = hits.length
    ? hits.map((s, i) => `<button type="button" class="ba-sug${i === 0 ? " on" : ""}" data-add-opp="${esc(s.n)}">${ico(s.icon, tPoke(s.n))}${esc(tPoke(s.n))}</button>`).join("")
    : `<div class="ba-muted">${esc(X.notFound)}</div>`;
  box.hidden = false;
}
async function setOpp(sp: string) {
  const sm = core.species.find((s) => s.n === sp);
  if (!sm) return;
  await ensureDetail(sm.icon);
  st.oppMon = { sp, icon: sm.icon, sel: 0, edits: {} };
  st.setupOpp = "";
  st.boostOpp = 0;
  ($("ba-pick-wrap") as HTMLDetailsElement).open = false;
  const inp = $("ba-opp-search") as HTMLInputElement;
  inp.value = "";
  inp.blur();
  renderSuggest("");
  render();
}
/** 名前を打たずに選ぶ: 使用率順のアイコン一覧。 */
function renderPicker() {
  const list = [...core.species].filter((x) => !(x as any).off).sort((a, b) => a.rank - b.rank);
  const shown = pickAll ? list : list.slice(0, 30);
  $("ba-pick").innerHTML = shown.map((x) => `<button type="button" class="ba-pk${x.n === st.oppMon?.sp ? " on" : ""}" data-add-opp="${esc(x.n)}" title="${esc(tPoke(x.n))}">${ico(x.icon, tPoke(x.n))}<span>${esc(tPoke(x.n))}</span></button>`).join("")
    + (pickAll ? "" : `<button type="button" class="ba-pk ba-pk-more" id="ba-pick-more">${esc(X.more(list.length - shown.length))}</button>`);
}
async function ensureDetail(icon: string) {
  if (details.has(icon)) return;
  try { details.set(icon, await loadMon(icon)); } catch { /* 型データが無い種は採用率1位の組にも頼れないので空のまま */ }
}

// ---- 対面計算 ----
type Side = "me" | "opp";

function myRaw(): Slot | null {
  const slots = mySlots();
  if (!slots.length) return null;
  st.my = Math.min(st.my, slots.length - 1);
  return slots[st.my];
}
function myOverride(): Slot | null {
  const p = activeParty();
  return p ? st.myEdits[p.id]?.[st.my] ?? null : null;
}
function slotOf(side: Side): Slot | null {
  if (side === "me") return myOverride() ?? myRaw();
  const o = st.oppMon;
  return o ? oppSlot(o, o.sel) : null;
}
function setupMovesOf(s: Slot): string[] {
  return s.moves.filter((n) => SETUP.has(n));
}
/** エンジンは技欄の先頭の積み技を使うので、選んだ積み技を計算のときだけ先頭に回す。 */
function forCalc(s: Slot, pick: string): Slot {
  if (!pick || !s.moves.includes(pick)) return s;
  return { ...s, moves: [pick, ...s.moves.filter((n) => n !== pick)] };
}
function iconOf(sp: string): string {
  return core.species.find((x) => x.n === sp)?.icon ?? "";
}

function selOpts(entries: { n: string; pct?: number }[], cur: string, rest: string[] = [], t: (n: string) => string = (n) => n): string {
  const seen = new Set<string>();
  const out: string[] = [];
  const opt = (n: string, label: string) => {
    if (seen.has(n)) return;
    seen.add(n);
    out.push(`<option value="${esc(n)}"${n === cur ? " selected" : ""}>${esc(label)}</option>`);
  };
  if (cur && !entries.some((e) => e.n === cur)) opt(cur, t(cur));
  entries.forEach((e) => opt(e.n, e.pct != null ? `${t(e.n)}${paren(`${f1(e.pct)}%`)}` : t(e.n)));
  if (rest.length) {
    out.push(`<option disabled>──────</option>`);
    rest.forEach((n) => opt(n, t(n)));
  }
  return out.join("");
}

/** 積み技の前提。どの技を何回使った状態かを技名つきで出す（無い型では使えない）。 */
function setupRow(side: Side, s: Slot): string {
  const moves = setupMovesOf(s);
  const key = side === "me" ? "boostMe" : "boostOpp";
  if (!moves.length) return `<div class="ba-step ba-step-off">${esc(X.noSetup)}</div>`;
  const pickKey = side === "me" ? "setupMe" : "setupOpp";
  const cur = moves.includes(st[pickKey]) ? st[pickKey] : moves[0];
  const name = moves.length > 1
    ? `<select class="ba-sel ba-sel-sm" data-setup="${side}">${moves.map((n) => `<option value="${esc(n)}"${n === cur ? " selected" : ""}>${esc(tMove(n))}</option>`).join("")}</select>`
    : `<b>${esc(tMove(cur))}</b>`;
  return `<div class="ba-step">${name}${X.setupPre ? `<span class="ba-step-l">${X.setupPre}</span>` : ""}
    <button type="button" class="ba-sbtn" data-step="${key}" data-d="-1" aria-label="${esc(X.dec)}">▼</button>
    <b class="ba-step-v">${st[key]}</b>
    <button type="button" class="ba-sbtn" data-step="${key}" data-d="1" aria-label="${esc(X.inc)}">▲</button><span class="ba-step-l ba-step-long">${esc(X.setupLong)}</span><span class="ba-step-l ba-step-short">${esc(X.setupShort)}</span></div>`;
}

function compactHtml(side: Side, s: Slot, rb: ResolvedBuild): string {
  return `<div class="ba-kv"><span>${X.item}</span><b>${esc(tItem(s.item) || X.none)}</b></div>
    <div class="ba-kv"><span>${X.ability}</span><b>${esc(abilityText(rb, tAbil) || "—")}</b></div>
    <div class="ba-kv"><span>${X.nature}</span><b>${esc(tNatDisp(s.nature) || "—")}</b></div>
    <div class="ba-kv"><span>EV</span><b>${esc(evStr(s.evs))}</b></div>
    <div class="ba-stats">${rb.stats.map((v, i) => `<span><small>${STAT[i]}</small>${v}</span>`).join("")}</div>
    <div class="ba-kv ba-kv-mv"><span>${X.moves}</span><b>${s.moves.map((n) => esc(tMove(n))).join(" / ") || "—"}</b></div>
    ${setupRow(side, s)}`;
}

function editorHtml(side: Side, s: Slot, d: MonDetail | undefined): string {
  const moveList = [...(d?.moves ?? [])];
  const learn = (d?.learnset ?? []).filter((n) => !moveList.some((m) => m.n === n)).sort((a, b) => a.localeCompare(b, "ja"));
  const tot = s.evs.reduce((a, b) => a + b, 0);
  const ds = `data-side="${side}"`;
  return `<label class="ba-f"><span>${X.item}</span><select class="ba-sel" ${ds} data-edit="item">${selOpts(d?.items ?? [], s.item, core.items, tItem)}<option value=""${s.item ? "" : " selected"}>${X.none}</option></select></label>
    <label class="ba-f"><span>${X.ability}</span><select class="ba-sel" ${ds} data-edit="ability">${selOpts(d?.abilities ?? [], s.ability, [], tAbil)}</select></label>
    <label class="ba-f"><span>${X.nature}</span><select class="ba-sel" ${ds} data-edit="nature">${selOpts(d?.natures ?? [], s.nature, ALL_NATURES, tNatDisp)}</select></label>
    <div class="ba-evs">
      <div class="ba-evs-h"><span>EV</span><small id="ba-ev-total-${side}" class="${tot > EV_TOTAL_MAX ? "ba-err" : ""}">${X.total} ${tot}/${EV_TOTAL_MAX}</small></div>
      ${s.evs.map((v, i) => `<div class="ba-ev">
        <span class="ba-ev-l">${STAT[i]}</span><b class="ba-ev-real" id="ba-real-${side}-${i}"></b>
        <input type="number" inputmode="numeric" min="0" max="${EV_STAT_MAX}" value="${v}" ${ds} data-ev="${i}" aria-label="${esc(X.evAria(STAT[i]))}">
        <button type="button" class="ba-sbtn" ${ds} data-evd="${i}" data-d="-1" aria-label="${esc(X.decAria(STAT[i]))}">▼</button>
        <button type="button" class="ba-sbtn" ${ds} data-evd="${i}" data-d="1" aria-label="${esc(X.incAria(STAT[i]))}">▲</button>
        <button type="button" class="ba-qbtn" ${ds} data-evset="${i}" data-v="0">0</button>
        <button type="button" class="ba-qbtn" ${ds} data-evset="${i}" data-v="${EV_STAT_MAX}">32</button></div>`).join("")}
    </div>
    <div class="ba-moves">${[0, 1, 2, 3].map((mi) => `<select class="ba-sel" ${ds} data-move="${mi}" aria-label="${esc(X.moveAria(mi + 1))}">
        <option value="">—</option>${selOpts(moveList, s.moves[mi] ?? "", learn, tMove)}</select>`).join("")}</div>
    ${setupRow(side, s)}`;
}

function renderCalc() {
  const el = $("ba-calc");
  const res = $("ba-result");
  const mySlot = slotOf("me");
  const o = st.oppMon;
  if (!mySlot || !o) {
    res.innerHTML = `<div class="ba-muted">${esc(mySlot ? X.promptOpp : X.promptParty)}</div>`;
    el.innerHTML = "";
    $("ba-field").innerHTML = "";
    $("ba-bar").hidden = true;
    return;
  }
  const myIcon = iconOf(mySlot.sp);
  // 編集に使う候補（採用率つき）を後から読み込んで描き直す
  for (const ic of [myIcon, o.icon]) if (ic && !details.has(ic)) { ensureDetail(ic).then(() => renderCalc()); }
  const me = resolveSafe(mySlot);
  const tpls = templatesOf(o);
  o.sel = Math.min(o.sel, tpls.length - 1);
  const os = oppSlot(o, o.sel);
  const opp = resolveSafe(os);
  if (!me || !opp) { res.innerHTML = `<div class="ba-err">${esc(X.calcErr)}</div>`; return; }

  const myTabs = mySlots().map((s, i) => `<button type="button" class="ba-ptab${i === st.my ? " on" : ""}" data-my-pick="${i}">${ico(iconOf(s.sp), tPoke(s.sp))}</button>`).join("");
  const dirty = !!myOverride();
  const myPanel = `<section class="ba-panel ba-panel-me">
      <div class="ba-panel-h"><span class="ba-side ba-side-me">${X.me}</span>
        <button type="button" class="ba-edit-btn" data-toggle-edit="me">${st.editMe ? X.done : X.edit}</button></div>
      <div class="ba-ptabs">${myTabs}</div>
      <div class="ba-mon">${ico(me.icon, tPoke(me.label), "ba-ico-xl")}<div><b id="ba-label-me">${esc(tPoke(me.label))}</b>${dirty ? `<i class="ba-edited">${X.adjusting}</i>` : ""}<div class="ba-types" id="ba-types-me">${esc(typesTxt(me.t1, me.t2))}</div></div></div>
      ${st.editMe ? editorHtml("me", mySlot, details.get(myIcon)) : compactHtml("me", mySlot, me)}
      ${dirty ? `<div class="ba-row ba-dirty"><span class="ba-muted">${esc(X.dirtyNote)}</span>
        <button type="button" class="ba-btn-sub ba-btn-save" id="ba-my-save">${esc(X.save)}</button>
        <button type="button" class="ba-btn-sub" id="ba-my-discard">${esc(X.discard)}</button></div>` : ""}
    </section>`;

  const oppPanel = `<section class="ba-panel ba-panel-opp">
      <div class="ba-panel-h"><span class="ba-side ba-side-opp">${X.opp}</span>
        <button type="button" class="ba-edit-btn" data-toggle-edit="opp">${st.editOpp ? X.done : X.edit}</button></div>
      <div class="ba-mon">${ico(o.icon, tPoke(o.sp), "ba-ico-xl")}<div><b id="ba-label-opp">${esc(tPoke(opp.label))}</b>${o.edits[o.sel] ? `<i class="ba-edited">${X.edited}</i>` : ""}<div class="ba-types" id="ba-types-opp">${esc(typesTxt(opp.t1, opp.t2))}</div></div></div>
      <label class="ba-tplsel"><span>${X.setLbl}</span><select class="ba-sel" id="ba-tpl-sel" aria-label="${esc(X.setAria)}">${tpls.map((t, k) => {
        const lbl = `${tplTitle(o, k)}${t.share != null ? paren(`${f1(t.share)}%`) : ""}${o.edits[k] ? `${X.sep}${X.edited}` : ""}`;
        return `<option value="${k}"${k === o.sel ? " selected" : ""} data-tpl-label="${esc(lbl)}">${esc(lbl)}</option>`;
      }).join("")}</select></label>
      ${st.editOpp ? editorHtml("opp", os, details.get(o.icon)) : compactHtml("opp", os, opp)}
      ${o.edits[o.sel] ? `<div class="ba-row"><button type="button" class="ba-btn-sub" id="ba-tpl-reset">${esc(X.tplReset)}</button></div>` : ""}
    </section>`;

  const field = `<div class="ba-field">
      <label class="ba-f"><span>${X.weather}</span><select class="ba-sel" id="ba-weather">${WEATHERS.map((w) => `<option value="${w}"${w === st.weather ? " selected" : ""}>${w ? X.W[w] : X.weatherAuto}</option>`).join("")}</select></label>
      <label class="ba-f"><span>${X.terrain}</span><select class="ba-sel" id="ba-terrain">${TERRAINS.map((w) => `<option value="${w}"${w === st.terrain ? " selected" : ""}>${w ? X.T[w] : X.none}</option>`).join("")}</select></label>
    </div>`;

  el.innerHTML = `<div class="ba-panels${st.editMe || st.editOpp ? " ba-editing" : ""}">${myPanel}${oppPanel}</div>`;
  $("ba-field").innerHTML = field;
  renderCalcResults();
}

/** 1回の攻撃の%幅から確定数（タスキ等の耐え・回復は数えない、ダメ計の慣習どおり）。 */
function koTxt(lo: number, hi: number, def: ResolvedBuild): string {
  if (hi <= 0) return "";
  const nLo = Math.ceil(100 / lo), nHi = Math.ceil(100 / hi);
  const sash = nHi === 1 && (def.item === "きあいのタスキ" || def.ability === "がんじょう" || def.ability === "ばけのかわ") ? X.survive : "";
  if (nLo === nHi) return nLo >= 6 ? "" : `${X.ko(nLo)}${sash}`;
  if (nHi === 1) {
    let k = 0;
    for (let r = 85; r <= 100; r++) if ((hi * r) / 100 >= 100) k++;
    return `${X.koR1(Math.round((k / 16) * 100))}${sash}`;
  }
  return nHi >= 6 ? "" : X.koRn(nHi);
}

function moveRows(list: MoveDamage[], def: ResolvedBuild, mine: boolean, pct?: Map<string, number>): string {
  const sorted = pct
    ? [...list].sort((a, b) => (pct.get(b.n) ?? -1) - (pct.get(a.n) ?? -1) || b.pctHi - a.pctHi)
    : [...list].sort((a, b) => b.pctHi - a.pctHi);
  return sorted.map((m) => {
    const ko = koTxt(m.pctLo, m.pctHi, def);
    const eff = m.eff != null && m.eff !== 1 ? `<small class="ba-eff">${m.eff === 0 ? X.immune : `×${m.eff}`}</small>` : "";
    const use = pct?.has(m.n) ? `<small class="ba-use">${f1(pct.get(m.n)!)}%</small>` : "";
    return `<div class="ba-dm${mine ? " ba-dm-me" : ""}">
      <span class="ba-dm-n">${esc(tMove(m.n))}${eff}${use}</span>
      <span class="ba-dm-p">${f1(m.pctLo)}〜${f1(m.pctHi)}%</span>
      <span class="ba-dm-k${m.pctHi >= 100 ? " ba-dm-ohko" : ""}">${esc(ko)}</span>
      <span class="ba-dm-g"><i class="hi" style="width:${Math.min(100, m.pctHi).toFixed(1)}%"></i><i class="lo" style="width:${Math.min(100, m.pctLo).toFixed(1)}%"></i></span>
    </div>`;
  }).join("");
}

/** 相手が型の4技以外に持ちうる技（採用率上位のうち型に入っていないもの）の自分へのダメージ。 */
function extraOppDamages(me: ResolvedBuild, os: Slot, d: MonDetail | undefined): MoveDamage[] {
  // 積み技は足さない（型に積み技が無いとき、足した積み技で相手の積みの前提が効いてしまう）
  const extra = (d?.moves ?? []).map((m) => m.n).filter((n) => !os.moves.includes(n) && !SETUP.has(n));
  if (!extra.length) return [];
  const ext = resolveSafe(forCalc({ ...os, moves: [...os.moves, ...extra] }, st.setupOpp));
  if (!ext) return [];
  return withScenario(fieldScenario(true), () => moveDamages(me, ext).opp.filter((m) => extra.includes(m.n)));
}

/** 技ごとのダメージ（相手を選んだ直後に見える位置）・下の結果バー・エディタの派生表示を描き直す。 */
function renderCalcResults() {
  const res = $("ba-result");
  const bar = $("ba-bar");
  const mySlot = slotOf("me");
  const o = st.oppMon;
  if (!mySlot || !o) { bar.hidden = true; return; }
  const tpls = templatesOf(o);
  const myCalc = forCalc(mySlot, st.setupMe);
  const me = resolveSafe(myCalc);
  if (!me) return;
  const rows = withScenario(fieldScenario(true), () => tpls.map((_, k) => {
    const s = oppSlot(o, k);
    const opp = resolveSafe(forCalc(s, st.setupOpp));
    if (!opp) return null;
    const v = judge1v1(me, opp);
    return { k, opp, v, mb: k === o.sel ? moveDamages(me, opp) : null, pd: k === o.sel ? pairHitDetails(me, opp) : null };
  }));
  const cur = rows.find((r) => r && r.k === o.sel);
  if (!cur || !cur.mb || !cur.pd) { res.innerHTML = ""; bar.hidden = true; return; }
  const { opp, v, mb, pd } = cur;

  const sel = document.getElementById("ba-tpl-sel") as HTMLSelectElement | null;
  if (sel) [...sel.options].forEach((op, k) => { const r = rows[k]; op.textContent = `${r ? `${r.v.sym} ` : ""}${op.dataset.tplLabel ?? ""}`; });
  const order = v.mutual ? X.mutual : v.tie ? X.tie : v.koFirst ? X.first : X.second;
  const scenTxt = [st.weather ? X.W[st.weather] : "", st.terrain ? X.T[st.terrain] : "", st.boostMe && setupMovesOf(mySlot).length ? X.scenMe(st.boostMe) : "", st.boostOpp && setupMovesOf(oppSlot(o, o.sel)).length ? X.scenOpp(st.boostOpp) : ""].filter(Boolean).join(X.sep);
  const isStatus = (n: string) => core.moves[n]?.[1] === "status";
  const oppMoves = oppSlot(o, o.sel).moves;
  const immune = (moves: string[], dealt: MoveDamage[]) => moves.filter((n) => !isStatus(n) && core.moves[n] && !dealt.some((m) => m.n === n));
  const immuneRow = (n: string, pct?: Map<string, number>) => `<div class="ba-dm ba-dm-imm"><span class="ba-dm-n">${esc(tMove(n))}${pct?.has(n) ? `<small class="ba-use">${f1(pct.get(n)!)}%</small>` : ""}</span><span class="ba-dm-p">0%</span><span class="ba-dm-k">${X.immune}</span></div>`;
  const od = details.get(o.icon);
  const usePct = new Map((od?.moves ?? []).map((m) => [m.n, m.pct] as [string, number]));
  const extra = extraOppDamages(me, oppSlot(o, o.sel), od);
  res.innerHTML = `<div class="ba-res">
      <div class="ba-res-h">
        <span class="muc-sym ${symClass(v.sym)}">${v.sym}</span>
        <span class="ba-res-o ${v.koFirst ? "ba-first" : "ba-second"}">${order}</span>
        <span class="ba-res-s">S ${v.myS}/${v.oppS}</span>
        ${scenTxt ? `<span class="ba-res-sc">${esc(scenTxt)}</span>` : ""}
        <button type="button" class="ba-mu-open" data-mu-open>${esc(X.muOpen)}</button>
      </div>
      <div class="ba-dm-h ba-me-c">${X.dmMe} <small>HP ${opp.stats[0]}</small></div>
      ${mb.my.length ? moveRows(mb.my, opp, true) : `<div class="ba-muted">${esc(X.noDmg)}</div>`}
      ${immune(mySlot.moves, mb.my).map((n) => immuneRow(n)).join("")}
      <div class="ba-dm-h ba-opp-c">${X.dmOpp} <small>HP ${me.stats[0]}${X.sep}${X.usage}</small></div>
      ${mb.opp.length ? moveRows(mb.opp, me, false, usePct) : `<div class="ba-muted">${esc(X.tplNoDmg)}</div>`}
      ${immune(oppMoves, mb.opp).map((n) => immuneRow(n, usePct)).join("")}
      ${extra.length ? `<div class="ba-dm-sep">${esc(X.extra)}</div>${moveRows(extra, me, false, usePct)}` : ""}
    </div>`;

  // エディタの派生表示（入力欄は作り直さない）
  const sync = (side: Side, rb: ResolvedBuild, s: Slot) => {
    rb.stats.forEach((x, i) => { const e = document.getElementById(`ba-real-${side}-${i}`); if (e) e.textContent = String(x); });
    const tot = s.evs.reduce((a, b) => a + b, 0);
    const te = document.getElementById(`ba-ev-total-${side}`);
    if (te) { te.textContent = `${X.total} ${tot}/${EV_TOTAL_MAX}`; te.className = tot > EV_TOTAL_MAX ? "ba-err" : ""; }
    const lb = document.getElementById(`ba-label-${side}`); if (lb) lb.textContent = tPoke(rb.label);
    const ty = document.getElementById(`ba-types-${side}`); if (ty) ty.textContent = typesTxt(rb.t1, rb.t2);
  };
  sync("me", me, mySlot);
  sync("opp", opp, oppSlot(o, o.sel));

  bar.hidden = false;
  bar.innerHTML = `<div class="ba-bar-in">
      ${ico(me.icon, me.label, "ba-bar-ico")}
      <div class="ba-bar-rows">
        <div class="ba-bar-r"><span class="ba-bar-k ba-me-c">${X.barOut}</span><b>${rangeTxt(pd.my)}</b><span class="ba-bar-hit">${hitTxt(pd.my)}</span><small>${esc(tMove(pd.my?.n ?? ""))}</small></div>
        <div class="ba-bar-r"><span class="ba-bar-k ba-opp-c">${X.barIn}</span><b>${rangeTxt(pd.opp)}</b><span class="ba-bar-hit">${hitTxt(pd.opp)}</span><small>${esc(tMove(pd.opp?.n ?? ""))}</small></div>
      </div>
      <div class="ba-bar-v"><span class="muc-sym ${symClass(v.sym)}">${v.sym}</span><small>${order}</small></div>
      ${ico(opp.icon, opp.label, "ba-bar-ico")}
    </div>`;
}

/** 工房・簡単構築・情報ページと同じ1v1ダイアログ（相手の型はタブ・既定は表示中の型）。場・積みの前提はこのページの指定どおり。 */
function openMuFor() {
  const mySlot = slotOf("me");
  const o = st.oppMon;
  const me = mySlot ? resolveSafe(forCalc(mySlot, st.setupMe)) : null;
  if (!me || !o) return;
  const builds = templatesOf(o).map((t, k) => {
    const rb = resolveSafe(forCalc(oppSlot(o, k), st.setupOpp));
    return rb ? { ...rb, weight: t.share, arch: t.arch, archNo: t.archNo, archSub: t.archSub } : null;
  });
  const cur = builds[o.sel];
  if (!cur) return;
  const ok = builds.filter((b): b is ResolvedBuild => !!b);
  openMuDialog({
    lang: L, names: { tPoke, tMove, tItem, tAbil, tNature: tNat }, mine: me,
    opp: { label: o.sp, icon: o.icon, builds: ok }, oppDef: ok.indexOf(cur), scenario: fieldScenario(true),
  });
}

// ================= 操作 =================

function editSlot(side: Side, fn: (s: Slot) => void, full: boolean) {
  if (side === "me") {
    const p = activeParty();
    const base = slotOf("me");
    if (!p || !base) return;
    const s = structuredClone(base);
    fn(s);
    (st.myEdits[p.id] ??= {})[st.my] = s;
    // 1文字目の調整で「調整中」の印と保存ボタンを出すため、最初の1回は全体を描き直す
    if (full || !document.getElementById("ba-my-save")) { renderCalc(); saveState(); } else renderResults();
    return;
  }
  const o = st.oppMon;
  if (!o) return;
  const s = o.edits[o.sel] ?? structuredClone(oppSlot(o, o.sel));
  fn(s);
  o.edits[o.sel] = s;
  if (full) { renderCalc(); saveState(); } else renderResults();
}
function setEv(side: Side, i: number, raw: number) {
  editSlot(side, (s) => {
    const others = s.evs.reduce((a, b, j) => (j === i ? a : a + b), 0);
    s.evs[i] = Math.max(0, Math.min(EV_STAT_MAX, EV_TOTAL_MAX - others, Math.round(raw) || 0));
  }, false);
  const inp = document.querySelector(`[data-side="${side}"][data-ev="${i}"]`) as HTMLInputElement | null;
  const cur = slotOf(side);
  if (inp && cur && document.activeElement !== inp) inp.value = String(cur.evs[i]);
}

function saveMyToParty() {
  const p = activeParty();
  const ov = myOverride();
  if (!p || !ov) return;
  const raw = p.slots[st.my];
  if (!confirm(X.confirmSave(p.name, tPoke(raw?.sp ?? "")))) return;
  p.slots[st.my] = { ...ov, targets: raw?.targets ?? [], scenarios: raw?.scenarios };
  p.updatedAt = Date.now();
  saveStore(store);
  delete st.myEdits[p.id][st.my];
  render();
}

function bind() {
  const root = $("ba-app");
  root.addEventListener("click", async (e) => {
    const t = e.target as HTMLElement;
    const q = (sel: string) => t.closest(sel) as HTMLElement | null;
    let x: HTMLElement | null;
    if (q("[data-mu-open]")) {
      openMuFor();
    } else if ((x = q("[data-add-opp]"))) {
      await setOpp(x.dataset.addOpp!);
      $("ba-calc").scrollIntoView({ behavior: "smooth", block: "start" });
    } else if (t.id === "ba-pick-more") {
      pickAll = true; renderPicker();
    } else if ((x = q("[data-my-pick]"))) {
      st.my = Number(x.dataset.myPick); st.setupMe = ""; st.boostMe = 0; render();
    } else if ((x = q("[data-tpl]"))) {
      const o = st.oppMon; if (o) { o.sel = Number(x.dataset.tpl); renderCalc(); saveState(); }
    } else if ((x = q("[data-toggle-edit]"))) {
      const k = x.dataset.toggleEdit === "me" ? "editMe" : "editOpp";
      st[k] = !st[k]; renderCalc(); saveState();
    } else if ((x = q("[data-step]"))) {
      const k = x.dataset.step as "boostMe" | "boostOpp";
      st[k] = Math.max(0, Math.min(6, st[k] + Number(x.dataset.d)));
      renderCalc(); saveState();
    } else if ((x = q("[data-evd]"))) {
      const side = x.dataset.side as Side, i = Number(x.dataset.evd);
      setEv(side, i, (slotOf(side)?.evs[i] ?? 0) + Number(x.dataset.d));
    } else if ((x = q("[data-evset]"))) {
      setEv(x.dataset.side as Side, Number(x.dataset.evset), Number(x.dataset.v));
    } else if (t.id === "ba-tpl-reset") {
      const o = st.oppMon; if (o) { delete o.edits[o.sel]; renderCalc(); saveState(); }
    } else if (t.id === "ba-my-save") {
      saveMyToParty();
    } else if (t.id === "ba-my-discard") {
      const p = activeParty(); if (p) { delete st.myEdits[p.id]?.[st.my]; render(); }
    } else if (t.id === "ba-reset") {
      st = { ...defaultState(), partyId: st.partyId, my: st.my, myEdits: st.myEdits };
      render();
    } else if (t.id === "ba-demo") {
      demoParty();
    } else if (t.id === "ba-import-btn") {
      const p = importParty(($("ba-import-txt") as HTMLTextAreaElement).value);
      if (!p) { $("ba-import-err").textContent = X.importErr; return; }
      const np = createPartyFromSlots(store, p.slots, X.importName);
      st.partyId = np.id; render();
    }
  });
  root.addEventListener("change", (e) => {
    const t = e.target as HTMLElement;
    if (t.id === "ba-party-sel") { st.partyId = (t as HTMLSelectElement).value; st.my = 0; render(); return; }
    if (t.id === "ba-weather") { st.weather = (t as HTMLSelectElement).value; render(); return; }
    if (t.id === "ba-terrain") { st.terrain = (t as HTMLSelectElement).value; render(); return; }
    if (t.id === "ba-tpl-sel") {
      const o = st.oppMon; if (o) { o.sel = Number((t as HTMLSelectElement).value); renderCalc(); saveState(); }
      return;
    }
    if (t.dataset.setup) {
      st[t.dataset.setup === "me" ? "setupMe" : "setupOpp"] = (t as HTMLSelectElement).value;
      renderCalc(); saveState(); return;
    }
    const side = t.dataset.side as Side | undefined;
    if (!side) return;
    const ed = t.dataset.edit;
    if (ed) {
      const val = (t as HTMLSelectElement).value;
      editSlot(side, (s) => {
        (s as any)[ed] = val;
        // メガストーンを外した・付けたで特性の候補が変わるので、候補外の特性は採用率1位へ
        if (ed === "item") {
          const d = details.get(iconOf(s.sp));
          if (d?.abilities?.length && !d.abilities.some((a) => a.n === s.ability)) s.ability = d.abilities[0].n;
        }
      }, true);
    } else if (t.dataset.move != null) {
      const mi = Number(t.dataset.move);
      editSlot(side, (s) => { const m = [...s.moves]; m[mi] = (t as HTMLSelectElement).value; s.moves = m.filter(Boolean); }, true);
    } else if (t.dataset.ev != null) {
      setEv(side, Number(t.dataset.ev), Number((t as HTMLInputElement).value));
      const cur = slotOf(side);
      if (cur) (t as HTMLInputElement).value = String(cur.evs[Number(t.dataset.ev)]);
    }
  });
  // EVは打っている最中から反映（入力欄は作り直さない）
  root.addEventListener("input", (e) => {
    const t = e.target as HTMLInputElement;
    if (t.dataset.ev != null && t.value !== "" && t.dataset.side) setEv(t.dataset.side as Side, Number(t.dataset.ev), Number(t.value));
    if (t.id === "ba-opp-search") renderSuggest(t.value);
  });
  $("ba-opp-search").addEventListener("keydown", async (e) => {
    if (e.key !== "Enter" || e.isComposing) return;
    const first = document.querySelector("#ba-opp-sug [data-add-opp]") as HTMLElement | null;
    if (first) {
      e.preventDefault();
      await setOpp(first.dataset.addOpp!);
      $("ba-calc").scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
}

/** このブラウザにパーティが無いとき用: 使用率上位6種の代表型1でパーティを作る。 */
async function demoParty() {
  const top = [...core.species].filter((s) => !(s as any).off).sort((a, b) => a.rank - b.rank).slice(0, 6);
  const slots: (Slot | null)[] = [];
  for (const s of top) {
    await ensureDetail(s.icon);
    const t = details.get(s.icon)?.mu?.[0];
    if (t) slots.push(tplSlot(s.n, t));
  }
  const p = createPartyFromSlots(store, slots, X.demoName);
  st.partyId = p.id;
  render();
}

async function init() {
  try {
    const [c] = await Promise.all([loadCore(), initEngine("/engine/engine_wasm.wasm", "/builder-data/engine.pack.json")]);
    core = c;
  } catch (e) {
    console.warn("[battle-assist] 初期化に失敗", e);
    $("ba-loading").textContent = X.loadFail;
    return;
  }
  SETUP = new Set(setupMoveNames());
  store = loadStore();
  st = loadState();
  if (st.oppMon) await ensureDetail(st.oppMon.icon);
  $("ba-loading").remove();
  $("ba-main").hidden = false;
  ($("ba-pick-wrap") as HTMLDetailsElement).open = !st.oppMon;
  bind();
  render();
  // ダメージ一覧が見えている間は下の結果バーを出さない（同じ数字が二重になる）
  new IntersectionObserver(([en]) => { document.body.classList.toggle("ba-res-visible", en.isIntersecting); }, { threshold: 0.15 })
    .observe($("ba-result"));
}
init();
