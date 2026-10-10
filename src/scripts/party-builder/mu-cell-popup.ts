// 1v1相性ダイアログの唯一の入口。自分の型 × 相手の種の型 → wasm で判定 → renderMuPopup で描画 → 表示。
// ポケモン情報ページ（事前計算の埋め込み）・工房・簡単構築・対戦アシストがすべてここを通す。
import { loadCore } from "./data";
import { initEngine, setScenario, type Scenario } from "../engine/wasm";
import { fromSuggestSpec } from "./spec";
import { resolveSlot, resolveTargetSafe } from "./balance";
import { judge1v1, moveDamages, pairHitDetails, type MoveDamage } from "./matchup";
import { renderMatchupTable, matchupLead } from "./matchup-table";
import { archTitle, bindMuCardClicks, punct, renderMuPopup, type MuPopupData, type MuPopupMine, type MuPopupRow } from "./mu-card";
import type { ResolvedBuild, Verdict } from "./types";
import type { Lang } from "./assumptions";

export interface MuNames {
  tPoke(n: string): string;
  tMove(n: string): string;
  tItem(n: string): string;
  tAbil(n: string): string;
  tNature(n: string): string;
}
type Pair = ReturnType<typeof pairHitDetails>;
type Moves = ReturnType<typeof moveDamages>;
export interface OppGroup { label: string; icon: string; builds: ResolvedBuild[] }

const NO_ITEM: Record<Lang, string> = { ja: "道具なし", en: "no item", ko: "도구 없음" };
const EVK = ["H", "A", "B", "C", "D", "S"];
const esc = (s: string): string =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c] as string));

export const spriteUrl = (icon: string | null | undefined): string | null =>
  icon ? `/images/pokemon/pokemon-${icon}.webp` : null;

export function evStr(evs: ArrayLike<number>): string {
  return EVK.map((k, i) => (Number(evs[i]) ? `${k}${evs[i]}` : null)).filter(Boolean).join(" ");
}

/** 工房の仮想敵カードの「くわしい内訳」（経過の無い旧データ用の1列の表）。 */
export function muCardTableHtml(me: ResolvedBuild, grp: { label: string; icon: string }, opp: ResolvedBuild,
                                pair: Pair, verdict: Verdict, lang: Lang, n: MuNames): string {
  return renderMatchupTable({
    myName: n.tPoke(me.label), oppName: n.tPoke(grp.label),
    myIconUrl: spriteUrl(me.icon) || "", oppIconUrl: spriteUrl(grp.icon) || "",
    columns: [{
      label: "",
      meta: [n.tItem(opp.item) || NO_ITEM[lang], n.tNature(opp.nature), evStr(opp.evs)],
      my: pair.my, opp: pair.opp, verdict,
      myMoveText: n.tMove(pair.my?.n ?? verdict.myMove),
      oppMoveText: n.tMove(pair.opp?.n ?? verdict.oppMove),
      mySteps: pair.mySteps.map((s) => ({ ...s, n: n.tMove(s.n) })),
      oppSteps: pair.oppSteps.map((s) => ({ ...s, n: n.tMove(s.n) })),
      myTurns: pair.myTurns.map((s) => ({ ...s, n: n.tMove(s.n) })),
      oppTurns: pair.oppTurns.map((s) => ({ ...s, n: n.tMove(s.n) })),
      stallSeq: verdict.stall?.seq.map((x) => n.tMove(x)),
    }],
  } as Parameters<typeof renderMatchupTable>[0], lang, { compact: true });
}

/** 特性の表示。メガ石持ちは「入場時の特性→メガ後の特性」。 */
export function abilityText(b: { ability: string; megaAbility?: string }, tAbil: (n: string) => string): string {
  return b.megaAbility && b.megaAbility !== b.ability ? `${tAbil(b.ability)}→${tAbil(b.megaAbility)}` : tAbil(b.ability);
}

export const buildTitle = (b: ResolvedBuild, i: number, lang: Lang, n: MuNames): string =>
  archTitle(b, lang, i + 1) ?? `${n.tItem(b.item) || NO_ITEM[lang]}${punct(lang).sep}${n.tNature(b.nature)}`;
export const buildShare = (b: ResolvedBuild): string => (b.weight != null ? `${Math.round(b.weight * 10) / 10}%` : "");
const argmax = (xs: (number | undefined)[]) => xs.reduce<number>((bi, x, i) => ((x ?? -1) > (xs[bi] ?? -1) ? i : bi), 0);

/** 相手の型1つぶんのカードのデータ。技名・持ち物名などは和名のまま（描画時に names で訳す）。
 * 計算済み（情報ページのビルド時）なら pre で渡す。 */
export function muPopupRow(me: ResolvedBuild, opp: ResolvedBuild, j: number, lang: Lang, n: MuNames,
                           pre?: { verdict: Verdict; pair: Pair | Omit<Pair, "mySteps" | "oppSteps">; moves: Moves; ev?: string }): MuPopupRow {
  const v = pre?.verdict ?? judge1v1(me, opp);
  const pair = pre?.pair ?? pairHitDetails(me, opp);
  const mv = pre?.moves ?? moveDamages(me, opp);
  return {
    t: buildTitle(opp, j, lang, n), sh: buildShare(opp), sym: v.sym,
    chips: [n.tItem(opp.item) || NO_ITEM[lang], abilityText(opp, n.tAbil), n.tNature(opp.nature)],
    ev: pre?.ev ?? evStr(opp.evs), hp: opp.stats[0], ic: opp.icon,
    v, mt: pair.myTurns, ot: pair.oppTurns, md: pair.my, od: pair.opp,
    mm: mv.my as MoveDamage[], om: mv.opp as MoveDamage[], nmh: !mv.myHasMoves, noh: !mv.oppHasMoves,
  };
}

/** 自分の型（1つ以上）× 相手の型の集合の MuPopupData。既定のタブは割合が最大の型（oppDef で指定も可）。 */
export function muPopupData(mines: ResolvedBuild[], opps: ResolvedBuild[], lang: Lang, n: MuNames,
                            opts: { oppDef?: number } = {}): MuPopupData {
  const oppDef = opts.oppDef ?? argmax(opps.map((b) => b.weight));
  return {
    def: argmax(mines.map((b) => b.weight)),
    mine: mines.map((me, i): MuPopupMine => ({
      t: buildTitle(me, i, lang, n), sub: buildShare(me) || evStr(me.evs),
      hp: me.stats[0], ic: me.icon, def: oppDef,
      rows: opps.map((opp, j) => muPopupRow(me, opp, j, lang, n)),
    })),
  };
}

let uidSeq = 0;
/** ダイアログの中身。head=true で「自分 vs 相手」の見出しと前提の一文も付ける（情報ページは見出しを静的HTMLで持つ）。 */
export function renderMuDialog(d: MuPopupData, lang: Lang,
                               ctx: { myName: string; oppName: string; myIcon: string; oppIcon: string; uid?: string; names?: MuNames; head?: boolean }): string {
  const uid = ctx.uid ?? `mud${++uidSeq}`;
  const names = ctx.names ? { tMove: ctx.names.tMove, tItem: ctx.names.tItem, tPoke: ctx.names.tPoke, tAbility: ctx.names.tAbil } : undefined;
  const tp = ctx.names?.tPoke ?? ((x: string) => x);
  const head = ctx.head
    ? `<div class="muc-dlg-hd"><img src="${esc(spriteUrl(ctx.myIcon) || "")}" alt="">${esc(tp(ctx.myName))}<span class="muc-dlg-vs">vs</span>`
      + `<img src="${esc(spriteUrl(ctx.oppIcon) || "")}" alt="">${esc(tp(ctx.oppName))}</div>`
      + `<div class="muc-dlg-sub">${esc(matchupLead(lang))}</div>`
    : "";
  return head + `<div class="muc-dlg-body">${renderMuPopup(d, lang, {
    myName: tp(ctx.myName), oppName: tp(ctx.oppName), myIcon: ctx.myIcon, oppIcon: ctx.oppIcon, uid, names,
  })}</div>`;
}

let ready: Promise<void> | null = null;
/** 判定に要るデータと wasm を読み込む（1回だけ）。 */
export function ensureMuEngine(): Promise<void> {
  ready ??= Promise.all([loadCore(), initEngine("/engine/engine_wasm.wasm", "/builder-data/engine.pack.json")])
    .then(() => { bindMuCardClicks(document); })
    .catch((e) => { ready = null; throw e; });
  return ready;
}

/** 提案APIの spec（簡単構築）を自分の型に解決する。 */
export async function resolveSpec(spec: string): Promise<ResolvedBuild | null> {
  const core = await loadCore();
  const slot = fromSuggestSpec(spec);
  if (!slot) return null;
  try { return resolveSlot(slot, core.species, core.moves); } catch { return null; }
}

/** 相手の種の代表型（builder-data/targets.json）。メガX/Yで列が分かれる種は label の末尾で選ぶ。 */
export async function targetGroup(sp: string, label?: string): Promise<OppGroup | null> {
  const core = await loadCore();
  const gs = core.targets.filter((g) => g.sp === sp);
  const xy = label && /[XY]$/.test(label) ? label.slice(-1) : "";
  const g = gs.find((x) => label && x.label === label) ?? (xy ? gs.find((x) => x.label.endsWith(xy)) : undefined) ?? gs[0];
  if (!g) return null;
  const builds = g.builds.map((b) => resolveTargetSafe(g.sp, g.label, g.icon, b, core.moves)).filter((b): b is ResolvedBuild => !!b);
  return builds.length ? { label: g.label, icon: g.icon, builds } : null;
}

/** 1v1相性ダイアログを開く。show にページのポップアップの表示関数を渡す（無ければ共有のオーバーレイ）。
 * mine は自分の型（spec 文字列か解決済みの型。複数なら自分の型もタブ）、opp は相手の種（sp と列の label）か型の集合。 */
export async function openMuDialog(req: {
  lang: Lang; names: MuNames;
  mine: string | ResolvedBuild | ResolvedBuild[];
  opp: { sp: string; label?: string } | OppGroup;
  oppDef?: number; scenario?: Scenario | null;
  show?: (html: string) => void; loadingHtml?: string; errorHtml?: string; extraHtml?: string;
}): Promise<void> {
  const show = req.show ?? showMuOverlay;
  if (req.loadingHtml) show(req.loadingHtml);
  try {
    await ensureMuEngine();
    const mines = typeof req.mine === "string" ? [await resolveSpec(req.mine)] : Array.isArray(req.mine) ? req.mine : [req.mine];
    const grp = "builds" in req.opp ? req.opp : await targetGroup(req.opp.sp, req.opp.label);
    if (!grp || mines.some((m) => !m)) throw new Error("matchup data not found");
    const me = mines as ResolvedBuild[];
    if (req.scenario) setScenario(req.scenario);
    let d: MuPopupData;
    try { d = muPopupData(me, grp.builds, req.lang, req.names, { oppDef: req.oppDef }); }
    finally { if (req.scenario) setScenario(null); }
    show(renderMuDialog(d, req.lang, {
      myName: me[0].label, oppName: grp.label, myIcon: me[0].icon, oppIcon: grp.icon, names: req.names, head: true,
    }) + (req.extraHtml ?? ""));
  } catch (e) {
    console.warn("[openMuDialog]", e);
    if (req.errorHtml) show(req.errorHtml);
  }
}

let overlay: HTMLElement | null = null;
/** 自前のポップアップを持たないページ用の表示（対戦アシスト）。 */
export function showMuOverlay(html: string): void {
  if (!overlay) {
    overlay = document.createElement("div");
    overlay.className = "muc-dlg-ov";
    overlay.innerHTML = `<div class="muc-dlg" role="dialog" aria-modal="true"><button type="button" class="muc-dlg-x" aria-label="close">✕</button><div class="muc-dlg-in"></div></div>`;
    const close = () => { overlay!.hidden = true; document.documentElement.classList.remove("muc-dlg-lock"); };
    overlay.addEventListener("click", (e) => {
      const t = e.target as Element;
      if (t === overlay || t.closest(".muc-dlg-x")) close();
    });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && overlay && !overlay.hidden) close(); });
    document.body.appendChild(overlay);
  }
  overlay.querySelector(".muc-dlg-in")!.innerHTML = html;
  overlay.hidden = false;
  document.documentElement.classList.add("muc-dlg-lock");
}
