// 1v1判定に使った対戦（中央乱数・方針選択後の組）を、ゲーム画面ふうに1ターンずつ送って見せる再生。
// 仮想バトル観戦（SimulatorApp）のリプレイと同じ見た目（スプライト・HPバー・能力変化・状態・そのターンのメッセージ）の簡易版。
// 観戦のリプレイは Python の対戦ログの文面を読み取る作りで、1v1の経過(race)とは形式が違うため流用せず、race から直接組み立てる。
// ボタン操作は mu-card.ts の bindMuCardClicks がまとめて受ける（data-mur-go）。
import type { Lang } from "./assumptions";
import { causeLabel } from "./matchup";
import type { Verdict } from "./types";

type Race = NonNullable<Verdict["race"]>;
interface SideState { hp: number; stg: number[]; status: string | null; item: string | null; disg: boolean }
interface MegaInfo { from: string; to: string; ability: string; stone: string }
/** 入場効果・メガシンカで発動した特性（エンジンの raceInit.events。実際の発動順）。stg は両者の能力ランクの変化。 */
interface StartEvent {
  phase: "entry" | "mega"; side: 0 | 1; ability: string; abilities: [string, string];
  weather: string | null; wx0: string | null; terrain: string | null; stg: [number[], number[]]; effect: boolean;
}
interface State { sides: [SideState, SideState]; weather: string | null; mega?: [MegaInfo | null, MegaInfo | null]; events?: StartEvent[] }

export interface ReplayVM {
  race: Race;
  init: State | null;
  names: [string, string];
  icons: [string, string];
  maxHp: [number, number];
  tMove(n: string): string;
  tItem(n: string): string;
  /** ポケモン名の翻訳（メガシンカ前の名前の表示用）。 */
  tPoke?(n: string): string;
  /** 特性名の翻訳（メガシンカ後の特性の表示用）。 */
  tAbility?(n: string): string;
}

const TXT = {
  ja: {
    mega: (a: string, b: string) => `${a}は ${b}に メガシンカした！`, megaSoon: "メガシンカする", megaBadge: "メガ",
    abil: (p: string, a: string) => `${p}の ${a}！`,
    wxStart: { sunny: "日差しが 強くなった！", rain: "雨が 降り始めた！", sandstorm: "砂あらしが 吹き始めた！", hail: "雪が 降り始めた！" } as Record<string, string>,
    terrStart: { electric: "エレキフィールドが 張られた！", grassy: "グラスフィールドが 張られた！", psychic: "サイコフィールドが 張られた！", misty: "ミストフィールドが 張られた！" } as Record<string, string>,
    stgFx: (p: string, s: string, d: number) => `${p}の ${s}が ${d <= -3 ? "がくーんと" : d === -2 ? "がくっと" : d >= 3 ? "ぐぐーんと" : d === 2 ? "ぐーんと" : ""}${d > 0 ? "上がった" : "下がった"}！`,
    start: "最初から", prev: "◀ 前", next: "次 ▶", turn: (t: number, n: number) => (t === 0 ? `対戦開始 / 全${n}ターン` : `ターン ${t} / ${n}`),
    begin: (a: string, b: string) => `${a} と ${b} の1対1`,
    uses: (p: string, m: string) => `${p}の ${m}！`, flinch: (p: string) => `${p}は ひるんで 動けない！`,
    dmg: (p: string, n: number, pct: string) => `${p}に ${n}ダメージ（${pct}%）`,
    blocked: (p: string) => `${p}の ばけのかわ で 攻撃を 防いだ！`,
    cause: (p: string, c: string, n: number) => `${p}は ${c}で ${n}ダメージ`,
    heal: (p: string, c: string, n: number) => `${p}は ${c}で ${n}回復`,
    stage: (p: string, s: string, d: number) => `${p}の ${s}が ${Math.abs(d)}段階 ${d > 0 ? "上がった" : "下がった"}`,
    item: (p: string, it: string) => `${p}の ${it}が なくなった`,
    status: (p: string, st: string) => `${p}は ${st}になった`,
    faint: (p: string) => `${p}は 倒れた！`, eot: "ターン終了",
    stats: ["攻撃", "防御", "特攻", "特防", "素早さ"],
    st: { burn: "やけど", poison: "どく", badpoison: "もうどく", paralysis: "まひ", sleep: "ねむり", freeze: "こおり" } as Record<string, string>,
    wx: { sunny: "☀ 晴れ", rain: "🌧 あめ", sandstorm: "🌪 すなあらし", hail: "❄ ゆき" } as Record<string, string>,
    healNames: { berry: "きのみ", leftovers: "たべのこし", grassy: "グラスフィールド", drain: "吸収", shellbell: "かいがらのすず", heal: "回復" } as Record<string, string>,
  },
  en: {
    mega: (a: string, b: string) => `${a} Mega Evolved into ${b}!`, megaSoon: "will Mega Evolve", megaBadge: "Mega",
    abil: (p: string, a: string) => `[${p}'s ${a}]`,
    wxStart: { sunny: "The sunlight turned harsh!", rain: "It started to rain!", sandstorm: "A sandstorm kicked up!", hail: "It started to snow!" } as Record<string, string>,
    terrStart: { electric: "An electric current ran across the battlefield!", grassy: "Grass grew to cover the battlefield!", psychic: "The battlefield got weird!", misty: "Mist swirled around the battlefield!" } as Record<string, string>,
    stgFx: (p: string, s: string, d: number) => `${p}'s ${s} ${d > 0 ? (d >= 3 ? "rose drastically" : d === 2 ? "rose sharply" : "rose") : (d <= -3 ? "severely fell" : d === -2 ? "harshly fell" : "fell")}!`,
    start: "Restart", prev: "◀ Prev", next: "Next ▶", turn: (t: number, n: number) => (t === 0 ? `Start / ${n} turns` : `Turn ${t} / ${n}`),
    begin: (a: string, b: string) => `${a} vs ${b}`,
    uses: (p: string, m: string) => `${p} used ${m}!`, flinch: (p: string) => `${p} flinched and couldn't move!`,
    dmg: (p: string, n: number, pct: string) => `${p} took ${n} damage (${pct}%)`,
    blocked: (p: string) => `${p}'s Disguise blocked the attack!`,
    cause: (p: string, c: string, n: number) => `${p} took ${n} damage from ${c}`,
    heal: (p: string, c: string, n: number) => `${p} restored ${n} HP (${c})`,
    stage: (p: string, s: string, d: number) => `${p}'s ${s} ${d > 0 ? "rose" : "fell"} by ${Math.abs(d)}`,
    item: (p: string, it: string) => `${p}'s ${it} is gone`,
    status: (p: string, st: string) => `${p} is now ${st}`,
    faint: (p: string) => `${p} fainted!`, eot: "End of turn",
    stats: ["Atk", "Def", "SpA", "SpD", "Spe"],
    st: { burn: "burned", poison: "poisoned", badpoison: "badly poisoned", paralysis: "paralyzed", sleep: "asleep", freeze: "frozen" } as Record<string, string>,
    wx: { sunny: "☀ Sun", rain: "🌧 Rain", sandstorm: "🌪 Sandstorm", hail: "❄ Snow" } as Record<string, string>,
    healNames: { berry: "berry", leftovers: "Leftovers", grassy: "Grassy Terrain", drain: "drain", shellbell: "Shell Bell", heal: "healing" } as Record<string, string>,
  },
  ko: {
    mega: (a: string, b: string) => `${a}은(는) ${b}(으)로 메가진화했다!`, megaSoon: "메가진화 예정", megaBadge: "메가",
    abil: (p: string, a: string) => `${p}의 ${a}!`,
    wxStart: { sunny: "햇살이 강해졌다!", rain: "비가 내리기 시작했다!", sandstorm: "모래바람이 불기 시작했다!", hail: "눈이 내리기 시작했다!" } as Record<string, string>,
    terrStart: { electric: "발밑에 전기가 흐르기 시작했다!", grassy: "발밑에 풀이 무성해졌다!", psychic: "발밑이 이상한 느낌이 되었다!", misty: "발밑이 안개로 뒤덮였다!" } as Record<string, string>,
    stgFx: (p: string, s: string, d: number) => `${p}의 ${s}이(가) ${d <= -3 ? "매우 크게 " : d === -2 ? "크게 " : d >= 3 ? "매우 크게 " : d === 2 ? "크게 " : ""}${d > 0 ? "올라갔다" : "떨어졌다"}!`,
    start: "처음부터", prev: "◀ 이전", next: "다음 ▶", turn: (t: number, n: number) => (t === 0 ? `대전 시작 / 전${n}턴` : `${t}턴 / ${n}`),
    begin: (a: string, b: string) => `${a} 대 ${b}의 1대1`,
    uses: (p: string, m: string) => `${p}의 ${m}!`, flinch: (p: string) => `${p}은(는) 풀이 죽어 움직일 수 없다!`,
    dmg: (p: string, n: number, pct: string) => `${p}에게 ${n}대미지(${pct}%)`,
    blocked: (p: string) => `${p}의 탈로 공격을 막았다!`,
    cause: (p: string, c: string, n: number) => `${p}은(는) ${c}(으)로 ${n}대미지`,
    heal: (p: string, c: string, n: number) => `${p}은(는) ${c}(으)로 ${n}회복`,
    stage: (p: string, s: string, d: number) => `${p}의 ${s}이(가) ${Math.abs(d)}랭크 ${d > 0 ? "올랐다" : "떨어졌다"}`,
    item: (p: string, it: string) => `${p}의 ${it}이(가) 없어졌다`,
    status: (p: string, st: string) => `${p}은(는) ${st} 상태가 되었다`,
    faint: (p: string) => `${p}은(는) 쓰러졌다!`, eot: "턴 종료",
    stats: ["공격", "방어", "특공", "특방", "스피드"],
    st: { burn: "화상", poison: "독", badpoison: "맹독", paralysis: "마비", sleep: "잠듦", freeze: "얼음" } as Record<string, string>,
    wx: { sunny: "☀ 쾌청", rain: "🌧 비", sandstorm: "🌪 모래바람", hail: "❄ 눈" } as Record<string, string>,
    healNames: { berry: "나무열매", leftovers: "먹다남은음식", grassy: "그래스필드", drain: "흡수", shellbell: "조개껍질방울", heal: "회복" } as Record<string, string>,
  },
};

const esc = (s: string): string =>
  String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c] as string));
const hpColor = (f: number) => (f > 0.5 ? "#22c55e" : f > 0.2 ? "#eab308" : "#ef4444");

function stateOf(e: any): State | null { return e && e.st ? (e.st as State) : null; }

/** 1ターンぶんのメッセージ。行動→その行動に伴う増減→持ち物・能力変化・状態（両者）→倒れた、の順（race の発生順）。 */
const BIND_MOVES = new Set(["まきつく", "しめつける", "まとわりつく", "ほのおのうず", "うずしお", "すなじごく", "トラバサミ"]);

/** 1ターンぶんのメッセージ。bind は各側を拘束した技（ターンをまたいで持ち越す。「まとわりつくで 21ダメージ」と出すため）。 */
function turnMessages(vm: ReplayVM, entries: any[], prev: State | null, lang: Lang, bind: (string | null)[]): string[] {
  const t = TXT[lang] ?? TXT.ja;
  const out: string[] = [];
  let before = prev;
  for (const e of entries) {
    const st = stateOf(e);
    if (e.actor == null) out.push(`<span class="mur-eot">${esc(t.eot)}</span>`);
    else if (e.flinch) out.push(esc(t.flinch(vm.names[e.actor])));
    else if (e.move) out.push(`<b>${esc(t.uses(vm.names[e.actor], vm.tMove(e.move)))}</b>`);
    if (e.actor != null && e.move && BIND_MOVES.has(e.move) && !bind[1 - e.actor]) bind[1 - e.actor] = e.move;
    for (const ev of e.events as { side: 0 | 1; kind: string; amount: number; raw?: number }[]) {
      const who = vm.names[ev.side];
      // とどめの一撃は残りHPで頭打ちにせず、技そのもののダメージ（raw）を出す（100%超えもそのまま）
      const amt = ev.kind === "move" && ev.raw ? ev.raw : Math.abs(ev.amount);
      const pct = ((amt / Math.max(1, vm.maxHp[ev.side])) * 100).toFixed(1);
      if (ev.kind === "move") out.push(esc(t.dmg(who, amt, pct)));
      else if (ev.kind === "disguise") { out.push(esc(t.blocked(who))); out.push(esc(t.cause(who, causeLabel("disguise", lang), ev.amount))); }
      else if (ev.kind === "bind" && bind[ev.side]) out.push(esc(t.cause(who, vm.tMove(bind[ev.side]!), ev.amount)));
      else if (ev.amount > 0) out.push(esc(t.cause(who, causeLabel(ev.kind, lang), ev.amount)));
      else out.push(esc(t.heal(who, t.healNames[ev.kind] ?? causeLabel(ev.kind, lang), -ev.amount)));
    }
    if (st && before) {
      // 倒れたは、同じ行動に伴う両者の持ち物・能力変化・状態のメッセージより後に出す（りゅうせいぐんで倒したときの特攻ダウン等）
      const faints: string[] = [];
      for (const z of [0, 1] as const) {
        const a = before.sides[z], b = st.sides[z], who = vm.names[z];
        // 持ち物の消費→それによる能力変化（ジュエル→かるわざ 等）の順に出す
        if (a.item && a.item !== b.item) out.push(esc(t.item(who, vm.tItem(a.item))));
        b.stg.forEach((v, k) => { const d = v - (a.stg[k] ?? 0); if (d) out.push(esc(t.stage(who, t.stats[k], d))); });
        if (b.status && b.status !== a.status) out.push(esc(t.status(who, t.st[b.status] ?? b.status)));
        if (a.hp > 0 && b.hp <= 0) faints.push(`<b class="mur-faint">${esc(t.faint(who))}</b>`);
      }
      out.push(...faints);
    }
    if (st) before = st;
  }
  return out;
}

function monHtml(vm: ReplayVM, z: 0 | 1, s: SideState | null, lang: Lang, megaPhase: "before" | "after" | null): string {
  const t = TXT[lang] ?? TXT.ja;
  const max = vm.maxHp[z];
  const hp = s ? s.hp : max;
  const f = Math.max(0, Math.min(1, hp / Math.max(1, max)));
  const stg = s ? s.stg.map((v, k) => (v ? `<span class="${v > 0 ? "mur-up" : "mur-dn"}">${esc(t.stats[k])}${v > 0 ? "▲" : "▼"}${Math.abs(v)}</span>` : "")).join("") : "";
  const status = s && s.status ? `<span class="mur-st">${esc(t.st[s.status] ?? s.status)}</span>` : "";
  const item = s && s.item ? `<span class="mur-item">${esc(vm.tItem(s.item))}</span>` : "";
  // メガシンカ: 開始画面はメガシンカ前の名前＋「メガシンカする」、1ターン目以降はメガ後の名前＋「メガ」バッジ
  const mi = vm.init && (vm.init as State).mega ? (vm.init as State).mega![z] : null;
  const name = mi && megaPhase === "before" ? (vm.tPoke ? vm.tPoke(mi.from) : mi.from) : vm.names[z];
  const megaB = mi ? `<span class="mur-mega">${esc(megaPhase === "before" ? t.megaSoon : t.megaBadge)}</span>` : "";
  const ab = mi && megaPhase === "after" ? `<span class="mur-item">${esc(vm.tAbility ? vm.tAbility(mi.ability) : mi.ability)}</span>` : "";
  return `<div class="mur-mon${hp <= 0 ? " mur-dead" : ""}">`
    + `<div class="mur-ico">${vm.icons[z] ? `<img src="${esc(vm.icons[z])}" alt="${esc(vm.names[z])}" loading="lazy">` : ""}${hp <= 0 ? '<span class="mur-x">×</span>' : ""}</div>`
    + `<div class="mur-body"><div class="mur-name">${esc(name)}${megaB}</div>`
    + `<div class="mur-hprow"><div class="mur-hpbar"><div class="mur-hpfill" style="width:${(f * 100).toFixed(1)}%;background:${hpColor(f)}"></div></div>`
    + `<span class="mur-hp">${Math.max(0, hp)}/${max}</span></div>`
    + `<div class="mur-badges">${status}${stg}${ab}${item}</div></div></div>`;
}

const REACT = new Set(["まけんき", "かちき"]);

/** 入場効果・メガシンカの特性の発動メッセージ。相手のまけんき・かちき（下げられて上がった分）は相手の特性として分けて出す。 */
function eventMessages(vm: ReplayVM, ev: StartEvent, names: [string, string], lang: Lang): string[] {
  const t = TXT[lang] ?? TXT.ja;
  const ta = (a: string) => (vm.tAbility ? vm.tAbility(a) : a);
  const out: string[] = [];
  if (!ev.effect) return out;
  out.push(`<b>${esc(t.abil(names[ev.side], ta(ev.ability)))}</b>`);
  if (ev.weather) out.push(esc(t.wxStart[ev.weather] ?? ev.weather));
  if (ev.terrain) out.push(esc(t.terrStart[ev.terrain] ?? ev.terrain));
  for (const z of [ev.side, 1 - ev.side] as (0 | 1)[]) {
    const d = ev.stg[z] ?? [];
    const react = z !== ev.side && REACT.has(ev.abilities[z]) && d.some((x) => x > 0) && d.some((x) => x < 0);
    d.forEach((x, k) => { if (x < 0 || (x > 0 && !react)) out.push(esc(t.stgFx(names[z], t.stats[k], x))); });
    if (react) {
      out.push(`<b>${esc(t.abil(names[z], ta(ev.abilities[z])))}</b>`);
      d.forEach((x, k) => { if (x > 0) out.push(esc(t.stgFx(names[z], t.stats[k], x))); });
    }
  }
  return out;
}

/** 再生のHTML。全ターンの画面を先に作っておき、ボタンで表示を切り替える（通信なし・軽量）。 */
export function renderReplay(vm: ReplayVM, lang: Lang): string {
  const t = TXT[lang] ?? TXT.ja;
  const maxTurn = vm.race.reduce((m, e) => Math.max(m, e.turn), 0);
  const frames: string[] = [];
  let prev: State | null = vm.init;
  const frame = (k: number, st: State | null, msgs: string[]) => {
    const wx = st && st.weather ? `<div class="mur-wx">${esc(t.wx[st.weather] ?? st.weather)}</div>` : "";
    // 並びは 左＝自分・右＝相手（開始メッセージの順と揃える）
    const ph = k === 0 ? "before" : "after";
    return `<div class="mur-frame" data-mur-f="${k}"${k ? " hidden" : ""}>${wx}`
      + `<div class="mur-field">${monHtml(vm, 0, st ? st.sides[0] : null, lang, ph)}${monHtml(vm, 1, st ? st.sides[1] : null, lang, ph)}</div>`
      + `<div class="mur-msgs">${msgs.map((m) => `<div>${m}</div>`).join("")}</div></div>`;
  };
  const bind: (string | null)[] = [null, null];
  const megas = vm.init && vm.init.mega ? vm.init.mega : [null, null];
  const tp = (n: string) => (vm.tPoke ? vm.tPoke(n) : n);
  const baseName = (z: 0 | 1) => (megas[z] ? tp(megas[z]!.from) : vm.names[z]);
  // メガシンカ後の名前（翻訳が無い言語は「Mega ◯◯」）
  const megaName = (z: 0 | 1) => {
    const m = megas[z]!;
    if (lang === "ja" || tp(m.to) !== m.to) return tp(m.to);
    const suf = /[XYZ]$/.test(m.to) ? m.to.slice(-1) : "";
    return lang === "ko" ? `메가${tp(m.from)}${suf}` : `Mega ${tp(m.from)}${suf ? ` ${suf}` : ""}`;
  };
  vm = { ...vm, names: [megas[0] ? megaName(0) : vm.names[0], megas[1] ? megaName(1) : vm.names[1]] };
  const events = vm.init && vm.init.events ? vm.init.events : null;
  const pre: [string, string] = [baseName(0), baseName(1)];
  // 開始画面はメガシンカ前の状態（メガシンカで変わった能力ランク・天候を戻して見せる）
  let st0: State | null = prev;
  const megaEv = events ? events.filter((e) => e.phase === "mega") : [];
  if (prev && megaEv.length) {
    const sides = prev.sides.map((sd, z) => ({ ...sd, stg: sd.stg.map((v, k) => v - megaEv.reduce((a, e) => a + (e.stg[z]?.[k] ?? 0), 0)) })) as [SideState, SideState];
    const wxEv = megaEv.find((e) => e.weather);
    st0 = { ...prev, sides, weather: wxEv ? wxEv.wx0 : prev.weather };
  }
  const startMsgs = [esc(t.begin(pre[0], pre[1]))];
  if (events) for (const e of events.filter((x) => x.phase === "entry")) startMsgs.push(...eventMessages(vm, e, pre, lang));
  frames.push(frame(0, st0, startMsgs));
  for (let tn = 1; tn <= maxTurn; tn++) {
    const entries = vm.race.filter((e) => e.turn === tn);
    const msgs = turnMessages(vm, entries, prev, lang, bind);
    // 1ターン目の行動前にメガシンカ（エンジンの記録があれば実際の順＝素早さ順と、メガ後の特性の発動）
    if (tn === 1 && megaEv.length) {
      const head: string[] = [];
      const cur: [string, string] = [pre[0], pre[1]];
      for (const e of megaEv) {
        head.push(`<b>${esc(t.mega(pre[e.side], vm.names[e.side]))}</b>`);
        cur[e.side] = vm.names[e.side];
        head.push(...eventMessages(vm, e, cur, lang));
      }
      msgs.unshift(...head);
    } else if (tn === 1) {
      const firstActor = (entries.find((e) => e.actor != null)?.actor ?? 0) as 0 | 1;
      const order: (0 | 1)[] = firstActor === 0 ? [0, 1] : [1, 0];
      const megaMsgs = order.filter((z) => megas[z]).map((z) => `<b>${esc(t.mega(baseName(z), vm.names[z]))}</b>`);
      msgs.unshift(...megaMsgs);
    }
    const last = [...entries].reverse().find((e: any) => e.st);
    const st = last ? (last as any).st as State : prev;
    frames.push(frame(tn, st, msgs));
    prev = st;
  }
  const labels = Array.from({ length: maxTurn + 1 }, (_, k) => t.turn(k, maxTurn));
  return `<div class="mur" data-mur-cur="0" data-mur-n="${maxTurn}" data-mur-labels="${esc(JSON.stringify(labels))}">`
    + `<div class="mur-ctrl"><button type="button" data-mur-go="first">${esc(t.start)}</button>`
    + `<button type="button" data-mur-go="-1">${esc(t.prev)}</button>`
    + `<span class="mur-turn">${esc(labels[0])}</span>`
    + `<button type="button" data-mur-go="1">${esc(t.next)}</button></div>`
    + frames.join("") + `</div>`;
}

/** 再生のボタン（data-mur-go）を受ける。bindMuCardClicks から呼ぶ。 */
export function handleReplayClick(target: Element): boolean {
  const btn = target.closest?.("[data-mur-go]") as HTMLElement | null;
  if (!btn) return false;
  const root = btn.closest(".mur") as HTMLElement | null;
  if (!root) return true;
  const n = Number(root.dataset.murN ?? 0);
  const cur = Number(root.dataset.murCur ?? 0);
  const go = btn.dataset.murGo;
  const next = go === "first" ? 0 : Math.max(0, Math.min(n, cur + Number(go)));
  root.dataset.murCur = String(next);
  root.querySelectorAll<HTMLElement>(".mur-frame").forEach((f) => { f.hidden = Number(f.dataset.murF) !== next; });
  const labels = JSON.parse(root.dataset.murLabels ?? "[]") as string[];
  const lab = root.querySelector(".mur-turn");
  if (lab) lab.textContent = labels[next] ?? "";
  requestAnimationFrame(() => fitReplay(root));
  return true;
}

function scrollParent(el: HTMLElement): HTMLElement | null {
  for (let p = el.parentElement; p && p !== document.body && p !== document.documentElement; p = p.parentElement) {
    const oy = getComputedStyle(p).overflowY;
    if ((oy === "auto" || oy === "scroll") && p.scrollHeight > p.clientHeight) return p;
  }
  return null;
}

/** 画面の上端・下端に固定表示された要素（ヘッダー・下部バー等）に隠れる高さ。 */
function edgeCover(root: HTMLElement, x: number, y: number, fromTop: boolean): number {
  let cover = 0;
  for (let el = document.elementFromPoint(x, y) as HTMLElement | null; el && el !== document.body; el = el.parentElement) {
    if (el.contains(root)) break;
    const pos = getComputedStyle(el).position;
    if (pos !== "fixed" && pos !== "sticky") continue;
    const r = el.getBoundingClientRect();
    cover = Math.max(cover, fromTop ? r.bottom : window.innerHeight - r.top);
  }
  return cover;
}

/** 操作ボタン〜そのターンのメッセージ末尾が見えるようにスクロール。収まらなければ操作ボタンを上端に合わせる。 */
function fitReplay(root: HTMLElement): void {
  const ctrl = root.querySelector<HTMLElement>(".mur-ctrl");
  const frame = root.querySelector<HTMLElement>(".mur-frame:not([hidden])");
  if (!ctrl || !frame) return;
  const sp = scrollParent(root);
  const x = ctrl.getBoundingClientRect().left + 8;
  let vTop = 0, vBot = window.innerHeight;
  if (sp) {
    const r = sp.getBoundingClientRect();
    vTop = Math.max(vTop, r.top);
    vBot = Math.min(vBot, r.bottom);
  }
  vTop = Math.max(vTop, edgeCover(root, x, vTop + 1, true));
  vBot = Math.min(vBot, window.innerHeight - edgeCover(root, x, vBot - 1, false));
  const top = ctrl.getBoundingClientRect().top - 4;
  const bot = frame.getBoundingClientRect().bottom + 4;
  let dy = 0;
  if (bot - top > vBot - vTop) dy = top - vTop;
  else if (top < vTop) dy = top - vTop;
  else if (bot > vBot) dy = bot - vBot;
  if (Math.abs(dy) < 1) return;
  // 連打でスムーズスクロールが途中の間も目標がずれないよう、現在位置からの絶対位置で指定する
  if (sp) sp.scrollTo({ top: sp.scrollTop + dy, behavior: "smooth" });
  else window.scrollTo({ top: window.scrollY + dy, behavior: "smooth" });
}
