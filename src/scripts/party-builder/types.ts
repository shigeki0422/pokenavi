// パーティ構築ページ 純粋ロジック層の型定義
// 契約: /Users/shigeki/.claude/plans/1-2-ai-ai-tranquil-moore.md 「差し替え境界」「localStorageスキーマ」参照

/** 種族値・ステータス実数値配列の並び順は常に H,A,B,C,D,S */
export type StatArray = [number, number, number, number, number, number];

// ---- localStorage 永続データ (storage.ts) ----

/** 仮想敵ごとの「この状況なら」の前提。未設定のキーは既定(特性任せ・積みなし)。 */
export interface SlotScenario {
  /** 天候(表示名)。空文字・未設定は指定なし。 */
  w?: string;
  /** フィールド(表示名)。空文字・未設定は無し。 */
  t?: string;
  /** 自分側の積み回数(0〜6)。 */
  n?: number;
  /** 相手側(仮想敵)の積み回数(0〜6)。相手の型の先頭の積み技を使う。 */
  m?: number;
}

export interface Slot {
  sp: string;
  item: string;
  ability: string;
  nature: string;
  evs: StatArray; // 0-32
  moves: string[];
  targets: string[]; // 仮想敵ラベル(targets.jsonのlabel)、ポケモン毎に保存
  /** 仮想敵ラベル -> 前提。相手ごとに「砂・1積み」等を残せるようにするため仮想敵単位で持つ。
   * 既存Slotに対する後方互換の追加フィールド(無ければ既定の前提)。 */
  scenarios?: Record<string, SlotScenario>;
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
  /** 入場時（メガ前）の特性。spec の特性欄と同じ。 */
  ability: string;
  /** メガ型のメガ後の特性（表示用）。 */
  mab?: string;
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
  /** 型生成器の系統名（gen_builder_data.py の _pool_variants）。型プールに無い種には無い。 */
  arch?: string;
  /** 系統の番号（想定型セクションと同じ割合順）と、系統を分けた型の枝番（a, b…）。外国語版の見出し「Set 1a」に使う。 */
  archNo?: number;
  archSub?: string;
  /** 種全体に占めるこの型の割合(%)。複数型の判定の重みに使う。型プールに無い種には無い。 */
  share?: number;
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
  /** 技の優先度。決着ターンにどちらが先に動くかの判定に使う(ふいうち・かげうち等)。 */
  prio: number;
}

export interface ResolvedBuild {
  sp: string;
  label: string;
  t1: string;
  t2: string | null;
  stats: StatArray; // 実数値 [H,A,B,C,D,S]
  item: string;
  /** 入場時の特性（メガ石持ちはメガ前の特性。エンジンの spec に渡す）。 */
  ability: string;
  /** メガ後の特性。被弾倍率・表示に使う。 */
  megaAbility?: string;
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
  /** 複数型を集約するときの重み（種全体に占める型の割合%）。無ければ等しく扱う。 */
  weight?: number;
  /** 型の系統名（builder-data の arch）。型プールに無い種には無い。 */
  arch?: string;
  archNo?: number;
  archSub?: string;
}

// ---- 1v1判定 (matchup.ts) 差し替え境界 ----

/** どくどく＋回復技の持久戦ルート。side は判定を見ている自分から見た勝者(勝てる側が無い/両方勝てるなら null)。 */
export interface StallInfo {
  side: "me" | "opp" | null;
  turns: number;
  seq: string[];
  /** ターンごとの内訳(実数値)。direct=技の直接ダメージ、poison=ターン終了時の毒、heal=相手の回復(オボン等)。
   * defMax は攻められる側の最大HP（%換算の分母）。 */
  trace?: { n: string; direct: number; poison: number; bind: number; heal: number; defHp: number; attHp: number }[];
  defMax?: number;
  attMax?: number;
}

/** 勝ち筋が無い側が どくどく を入れた場合の見込み(表示用。記号・勝敗には影響しない)。 */
export interface StallPlan extends Omit<StallInfo, "side"> {
  outcome: "win" | "lose" | "stuck";
}

export interface Verdict {
  sym: "◎" | "○" | "△" | "▲" | "×";
  win: boolean;
  /** 素早さ実数値の比較。素早さ行の表示用。 */
  fast: boolean;
  /** 決着ターンにどちらが先に動くか。先制技で倒しきる線があれば素早さで負けていても true。
   * 勝敗・記号はこちらで決める。 */
  koFirst: boolean;
  /** 先後が素早さではなく技の優先度で決まった。表示で理由を出すために持つ。 */
  koByPriority: boolean;
  /** 素早さも決着ターンの優先度も同値で、先後がランダムになる。確定数も同じなら真の五分。 */
  even: boolean;
  myS: number;
  oppS: number;
  myHits: number | null;
  oppHits: number | null;
  myMove: string | null;
  oppMove: string | null;
  /** 判定の対戦で実際に撃った技の並び。同じ技の連打なら空。準備の技を使うときは先頭がその技。 */
  mySeq: string[];
  oppSeq?: string[];
  /** 1ターン目に使う準備の技（積み技・ねこだまし）。無ければ null。 */
  myPrep?: string | null;
  oppPrep?: string | null;
  /** 同速で、先後によって結果が変わる（記号は両方の順の平均。経過は自分が先の場合）。 */
  tie?: boolean;
  /** 相打ち（相手を倒した行動の反動等で同時に倒れる等）。引き分け扱い。mutualTurn はそのターン。 */
  mutual?: boolean;
  mutualTurn?: number | null;
  /** 判定の対戦の経過（エンジンの RaceEntry）。倒れた後の行動は含まない。 */
  race?: { turn: number; actor: 0 | 1 | null; move: string | null; flinch: boolean; hp: [number, number];
           events: { side: 0 | 1; kind: string; amount: number; raw?: number }[] }[];
  /** 互いに圏外で決着がつかない(引き分け)。 */
  draw?: boolean;
  /** 持久戦で勝敗が決まったか。記号・win には反映済みなので表示だけに使う。 */
  stall?: StallInfo;
  /** 持久戦で勝てない側でも、どくどくを持つなら入れた場合の内訳。 */
  plans?: { me?: StallPlan | null; opp?: StallPlan | null };
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
