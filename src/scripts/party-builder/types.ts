// パーティ構築ページ 純粋ロジック層の型定義
// 契約: /Users/shigeki/.claude/plans/1-2-ai-ai-tranquil-moore.md 「差し替え境界」「localStorageスキーマ」参照

/** 種族値・ステータス実数値配列の並び順は常に H,A,B,C,D,S */
export type StatArray = [number, number, number, number, number, number];

// ---- localStorage 永続データ (storage.ts) ----

export interface Slot {
  sp: string;
  item: string;
  ability: string;
  nature: string;
  evs: StatArray; // 0-32
  moves: string[];
  targets: string[]; // 仮想敵ラベル(targets.jsonのlabel)、ポケモン毎に保存
}

export interface Party {
  id: string;
  name: string;
  createdAt: number;
  updatedAt: number;
  slots: (Slot | null)[]; // 長さ6
}

export interface Store {
  v: 1;
  activeId: string | null;
  parties: Party[];
  /** 仮想敵カスタム型(キー=仮想敵ラベル)。未編集のラベルはtargets.jsonのデフォルトのまま。
   * 既存Store(v1)に対する後方互換の追加フィールド(バージョン上げ不要)。 */
  customTargets?: Record<string, TargetBuild[]>;
}

// ---- 静的データ (public/builder-data/*.json) ----

export interface MegaOption {
  name: string;
  stone: string;
  t1: string;
  t2: string | null;
  bs: StatArray;
  ability: string;
}

export interface SpeciesMaster {
  n: string;
  rank: number;
  icon: string;
  t1: string;
  t2: string | null;
  bs: StatArray;
  mega: MegaOption[];
}

/** 技名 -> [タイプ, 分類, 威力(null=変化技等), 優先度] */
export type MoveEntry = [string, "physical" | "special" | "status", number | null, number];
export type MoveDict = Record<string, MoveEntry>;

export interface TargetBuild {
  idx: number;
  item: string;
  nature: string;
  ability: string;
  ev: StatArray;
  /** 表示・プリセット用の代表4技(採用率TOP4)。1v1判定には mpool を使う。 */
  moves: string[];
  /** 1v1判定用の技プール(採用率TOP10)。gen_builder_data.py が付与する。
   * ユーザーが工房で編集した仮想敵(customTargets)には無いため、その場合は moves を使う。 */
  mpool?: string[];
  t1: string;
  t2: string | null;
  bs: StatArray; // メガ型は解決済みの値
  /** メガ進化後の型か(bs/t1/t2は解決済み)。表示ラベルの選択に使う。 */
  mega?: boolean;
  /** メガ型ならメガ名(例: メガカイリュー)、それ以外は種名。 */
  label?: string;
  spec: string;
}

export interface TargetGroup {
  sp: string;
  label: string;
  icon: string;
  /** メガ進化が複数系統(X/Y)ある種は同じiconで複数エントリに分かれる。その識別用のメガ石名。
   * 単一系統の種には無い。matchup-static.ts の preferItem と対応する。 */
  stone?: string;
  builds: TargetBuild[];
}

export interface MonDetailEntry {
  n: string;
  pct: number;
}

export interface MonDetailEvEntry {
  ev: StatArray;
  pct: number;
}

export interface MonDetail {
  n: string;
  items: MonDetailEntry[];
  abilities: MonDetailEntry[];
  natures: MonDetailEntry[];
  evs: MonDetailEvEntry[];
  moves: MonDetailEntry[];
  learnset: string[];
  builds: string[]; // spec文字列(parse_pokemon_spec互換)。工房の「型プリセット」用
  /** 1v1判定に使うこの種の代表型(型1/2/3)。相手側(targets.json builds)と同一スキーマ。
   * 自分側・相手側の非対称(自分は1型固定)を解消するために追加(2026-08)。 */
  mu?: TargetBuild[];
}

// ---- 解決済みビルド (balance.ts / matchup.ts が扱う共通表現) ----

export interface ResolvedMove {
  n: string;
  type: string;
  cat: "physical" | "special" | "status";
  power: number | null;
}

export interface ResolvedBuild {
  sp: string;
  label: string;
  t1: string;
  t2: string | null;
  stats: StatArray; // 実数値 [H,A,B,C,D,S]
  item: string;
  ability: string;
  nature: string;
  evs: StatArray;
  moves: ResolvedMove[];
  /**
   * 1v1判定でこのポケモンが選べる技の全体(採用率TOP10プール)。
   * 「互いに最良の弱点を突く技を打ち合ったらどうなるか」で有利不利を判定するため、
   * 静的マッチアップ(pokemon/counters/matchup ページ・工房の仮想敵)ではここを見る。
   * 未設定(＝工房でユーザーが4技を決めた自分の枠)の場合は moves がそのまま使われる。
   */
  pool?: ResolvedMove[];
  mega: boolean;
  icon: string;
}

// ---- 1v1判定 (matchup.ts) 差し替え境界 ----

export interface Verdict {
  sym: "◎" | "○" | "△" | "▲" | "×";
  win: boolean;
  fast: boolean;
  myS: number;
  oppS: number;
  myHits: number | null;
  oppHits: number | null;
  myMove: string | null;
  oppMove: string | null;
  stub: boolean;
}

/**
 * 相手の複数型(≤3)を踏まえた集約判定。移植元: scripts/_explain.py matchup_grid()。
 * sym は各型の1v1スコア平均のシンボル化、dep は型により有利不利のシンボルが割れるか。
 */
export interface AggregateVerdict {
  sym: Verdict["sym"];
  dep: boolean;
  verdicts: Verdict[];
}

// ---- 提案・逆算 (suggest.ts) ----

export interface TuneSuggestion {
  kind: "speed" | "ko" | "survive";
  text: string;
  evs?: StatArray;
  stub: boolean;
}
