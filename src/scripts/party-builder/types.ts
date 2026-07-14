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
  moves: string[];
  t1: string;
  t2: string | null;
  bs: StatArray; // メガ型は解決済みの値
  spec: string;
}

export interface TargetGroup {
  sp: string;
  label: string;
  icon: string;
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
  builds: string[]; // spec文字列(parse_pokemon_spec互換)
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
