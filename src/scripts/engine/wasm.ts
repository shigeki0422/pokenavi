// 対戦エンジン(Rust)の 1v1 判定を wasm 経由で呼ぶ薄いラッパー。
// ルール(ダメージ・確定数・素早さ・入場効果)は全てエンジン側にあり、ここでは
// 文字列と JSON の受け渡しだけを行う。TS 側にルールを再実装しないことが目的。
let mod: WebAssembly.Instance | null = null;
let mem: WebAssembly.Memory;
let season = "M-3";
/** 正式名 → spec に書ける別名。DB の正式名にはコロンを含むものがあり、
 * spec の区切りと衝突するため（ケンタロス:炎 → パルデアケンタロス(炎)）。 */
let aliases = new Map<string, string>();

type Exports = {
  memory: WebAssembly.Memory;
  alloc(n: number): number;
  init(p: number, n: number): number;
  analyze(ap: number, an: number, bp: number, bn: number, sp: number, sn: number): number;
  ko_prob(ap: number, an: number, bp: number, bn: number, sp: number, sn: number,
          att: number, mi: number, hits: number): number;
  name_aliases(): number;
  set_scenario(w: number, t: number, n: number): number;
  setup_move_names(): number;
  type_dynamic(): number;
  dealloc(p: number, n: number): void;
  result_ptr(): number;
  result_len(): number;
};

const enc = new TextEncoder();
const dec = new TextDecoder();

function ex(): Exports {
  if (!mod) throw new Error("engine wasm が未初期化。initEngine() を先に呼ぶこと");
  return mod.exports as unknown as Exports;
}

// 呼び出しごとに確保した領域は必ず返す。放置すると線形メモリが増え続け、
// ビルド時のような大量呼び出しで確保に失敗して wasm が停止する。
const pending: [number, number][] = [];

function put(s: string): [number, number] {
  const b = enc.encode(s);
  const p = ex().alloc(b.length);
  new Uint8Array(mem.buffer).set(b, p);
  pending.push([p, b.length]);
  return [p, b.length];
}

function release(): void {
  for (const [p, n] of pending) ex().dealloc(p, n);
  pending.length = 0;
}

function take(): unknown {
  const e = ex();
  const b = new Uint8Array(mem.buffer, e.result_ptr(), e.result_len());
  return JSON.parse(dec.decode(b));
}

/** wasm 本体とデータパックを直接渡して初期化する。ビルド時(Node)経路はこちらを使う。 */
export async function initEngineFrom(wasmBytes: BufferSource, packText: string, s = "M-3"): Promise<void> {
  if (mod) return;
  season = s;
  const w = await WebAssembly.instantiate(wasmBytes, {});
  mod = "instance" in w ? w.instance : (w as unknown as WebAssembly.Instance);
  mem = (mod.exports as unknown as Exports).memory;
  try {
    if (ex().init(...put(packText)) !== 0) throw new Error("データパックの読み込みに失敗");
  } finally {
    release();
  }
  ex().name_aliases();
  aliases = new Map(Object.entries(take() as Record<string, string>));
}

/** ブラウザ用。ページ描画前に一度だけ呼ぶ。 */
export async function initEngine(wasmUrl: string, packUrl: string, s = "M-3"): Promise<void> {
  if (mod) return;
  const [bytes, pack] = await Promise.all([
    fetch(wasmUrl).then((r) => r.arrayBuffer()),
    fetch(packUrl).then((r) => r.text()),
  ]);
  await initEngineFrom(bytes, pack, s);
}

/** 1v1判定を「この状況なら」に切り替える指定。既定(すべて0/未指定)は特性由来の天候のまま・積みなし。 */
export interface Scenario {
  /** 天候。未指定は特性任せ。 */
  weather?: "晴れ" | "雨" | "すなあらし" | "あられ" | null;
  /** フィールド。未指定は無し。 */
  terrain?: "エレキフィールド" | "グラスフィールド" | "サイコフィールド" | "ミストフィールド" | null;
  /** 自分側(specA)が積み技を使った回数。 */
  boost?: number;
}

const WEATHER_CODE: Record<string, number> = { "晴れ": 1, "雨": 2, "すなあらし": 3, "あられ": 4 };
const TERRAIN_CODE: Record<string, number> = {
  "エレキフィールド": 1, "グラスフィールド": 2, "サイコフィールド": 3, "ミストフィールド": 4,
};

let scenarioKeyStr = "";

/** 以降の analyze/koProb に効く前提を差し替える。エンジン側が状態を持つので、
 * 呼び出し側は「設定 → 計算 → 戻す」の順で使うこと。 */
export function setScenario(s: Scenario | null): void {
  const w = s?.weather ? (WEATHER_CODE[s.weather] ?? 0) : 0;
  const t = s?.terrain ? (TERRAIN_CODE[s.terrain] ?? 0) : 0;
  const n = Math.max(0, Math.min(6, Math.round(s?.boost ?? 0)));
  scenarioKeyStr = w || t || n ? `${w}.${t}.${n}` : "";
  ex().set_scenario(w, t, n);
}

/** 現在の前提を表す短い文字列。計算結果を使い回す側のキーに混ぜる。 */
export function scenarioKey(): string {
  return scenarioKeyStr;
}

/** 積み技(自分の能力を上げる変化技)の名前一覧。判定に使う表そのものを返す。 */
export function setupMoveNames(): string[] {
  ex().setup_move_names();
  return take() as string[];
}

/** 型だけでは無効(0倍)を判定できない技・特性。判定に使う条件そのものを返すので、
 * 表示側の事前除外がエンジンの挙動と食い違わない。 */
export function typeDynamic(): { moves: string[]; abilities: string[] } {
  ex().type_dynamic();
  return take() as { moves: string[]; abilities: string[] };
}

/** 初期化済みか。静的ビルドと実行時で分岐する呼び出し側の判定用。 */
export function engineReady(): boolean {
  return mod !== null;
}

/** ResolvedBuild を Python/Rust 共通の spec 文字列にする。
 * 書式は scripts/simulator/pokemon.py: parse_pokemon_spec と同じ 5 フィールド。
 * 種名にコロンを含む形(ケンタロス:炎 等)があるため、区切りは必ず最初の "@" から数える。 */
export function buildToSpec(b: {
  sp: string; item: string; ability: string; nature: string;
  evs: readonly number[]; moves: readonly { n: string }[];
}): string {
  const sp = aliases.get(b.sp) ?? b.sp;
  // コロンはフィールド区切りなので、種名に含まれたままだとパースが壊れる
  // （ケンタロス:炎 等。form_aliases の別名に置き換わっているはず）。
  // 初期化前に呼ばれると別名が空のまま壊れた spec を作ってしまうため、ここで止める。
  if (sp.includes(":")) {
    throw new Error(`spec に書けない種名です（初期化前の呼び出しの可能性）: ${b.sp}`);
  }
  return `${sp}@${b.item || ""}:${b.nature || ""}:${b.moves.map((m) => m.n).join("|")}`
    + `:${b.evs.join("/")}:${b.ability || ""}`;
}

export interface EngineMove {
  n: string;
  /** 変化技・無効技は null。最低乱数/最高乱数での与ダメ実数値。 */
  dmgLo?: number;
  dmgHi?: number;
  /** 確定数(999=圏外)。最低乱数と最高乱数のそれぞれ。 */
  hitsLo?: number;
  hitsHi?: number;
  /** 最大打点技の選定に使う値（1ターン目の防御側HP減少）。表示には使わない。
   * Python の _mu_engine._best_cached と同じ基準で選ぶために必要で、
   * ばけのかわ・天候の削り・たべのこしの回復が入る点が dmgLo と異なる。 */
  firstLo?: number;
  /** この技の与ダメ・確定数に実際に効いた条件（天候・フィールド・能力変化）。
   * 場に出ているだけで効いていないものは入らない。 */
  conds?: string[];
  dmg?: null;
}

export interface EngineSide {
  hp: number;
  speed: number;
  moves: EngineMove[];
  /** 毎ターン最善手を選び直した場合の手数(999=CAP内で倒せない)と、その技の並び。 */
  seqHits: number;
  seq: string[];
  /** 毎ターンの与ダメージ(最低/最高乱数の実数値)。並びは手順があれば手順、無ければ最大打点技の連打。
   * 経路は最低乱数で進めるので、じきゅうりょくの防御上昇・積みなど2ターン目以降の変化が入る。 */
  turns: { n: string; lo: number; hi: number }[];
}

/** エンジンが決める1v1の記号判定。刻み・先制技・手順・確定1の扱いを表示側に持たない。 */
export interface EngineVerdict {
  sym: "◎" | "○" | "△" | "▲" | "×";
  win: boolean;
  score: number;
  myHits: number;
  oppHits: number;
  myS: number;
  oppS: number;
  fast: boolean;
  koFirst: boolean;
  koByPriority: boolean;
  even: boolean;
  myMove: string | null;
  oppMove: string | null;
  mySeq: string[];
}

/** 1v1 の両側について HP・実効素早さ・各技の与ダメと確定数、および記号判定を得る。 */
export function analyze(specA: string, specB: string): { a: EngineSide; b: EngineSide; verdict: EngineVerdict } {
  const e = ex();
  try {
    if (e.analyze(...put(specA), ...put(specB), ...put(season)) !== 0) {
      throw new Error("analyze 失敗");
    }
    return take() as { a: EngineSide; b: EngineSide; verdict: EngineVerdict };
  } finally {
    release();
  }
}

/** hits 発以内に倒せる確率(0〜1)。ターン終了時の増減(たべのこし・オボン・砂)は
 * エンジンが対戦本体の処理をそのまま使うので、呼び出し側で再現しない。 */
export function koProb(spec0: string, spec1: string, att: number, moveIdx: number, hits: number): number {
  const e = ex();
  try {
    if (e.ko_prob(...put(spec0), ...put(spec1), ...put(season), att, moveIdx, hits) !== 0) {
      throw new Error("ko_prob 失敗");
    }
    return take() as number;
  } finally {
    release();
  }
}
