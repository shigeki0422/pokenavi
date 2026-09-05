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
  dmg?: null;
}

export interface EngineSide {
  hp: number;
  speed: number;
  moves: EngineMove[];
  /** 入場時に変化した攻撃/特攻ランク（いかく・ダウンロード等）。0なら変化なし。 */
  atkStage: number;
  spaStage: number;
}

/** 対面開始時に成立している場。ダメージ計算に効くので表示で明示する。 */
export interface EngineField {
  weather: string | null;
  terrain: string | null;
}

/** 1v1 の両側について HP・実効素早さ・各技の与ダメと確定数を得る。 */
export function analyze(specA: string, specB: string): { a: EngineSide; b: EngineSide; field: EngineField } {
  const e = ex();
  try {
    if (e.analyze(...put(specA), ...put(specB), ...put(season)) !== 0) {
      throw new Error("analyze 失敗");
    }
    return take() as { a: EngineSide; b: EngineSide; field: EngineField };
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
