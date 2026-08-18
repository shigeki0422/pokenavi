// 実数値計算。移植元: scripts/simulator/pokemon.py の calc_stat()/calc_hp()（Lv50、EVは32スケールでev*2、IV既定31）
import type { StatArray } from "./types";

export const EV_STAT_MAX = 32;
export const EV_TOTAL_MAX = 66;

/** 性格補正テーブル: 性格名 -> [上昇stat idx, 下降stat idx]。idxは 1=A 2=B 3=C 4=D 5=S（0=Hは性格補正の対象外）。
 * 移植元: scripts/simulator/data.py の NATURE_MODS（stat_key文字列をH/A/B/C/D/Sのidxに変換）。
 * 五性（まじめ/きまぐれ/てれや/がんばりや/すなお）は補正なしのためここには含めない（NEUTRAL_NATURESを参照）。 */
export const NATURE_MODS: Record<string, [number, number]> = {
  いじっぱり: [1, 3],
  ゆうかん: [1, 5],
  やんちゃ: [1, 4],
  さみしがり: [1, 2],
  わんぱく: [2, 3],
  のうてんき: [2, 4],
  のんき: [2, 5],
  ずぶとい: [2, 1],
  おくびょう: [5, 1],
  せっかち: [5, 2],
  ようき: [5, 3],
  むじゃき: [5, 4],
  ひかえめ: [3, 1],
  おっとり: [3, 2],
  うっかりや: [3, 4],
  れいせい: [3, 5],
  おだやか: [4, 1],
  おとなしい: [4, 2],
  しんちょう: [4, 3],
  なまいき: [4, 5],
};

/** 補正のない五性（インポート厳密検証・型プリセットの妥当性チェック用） */
export const NEUTRAL_NATURES = ["まじめ", "きまぐれ", "てれや", "がんばりや", "すなお"];

export const ALL_NATURES = [...Object.keys(NATURE_MODS), ...NEUTRAL_NATURES];

/**
 * 性格補正込みの実数値(H以外)。
 * @param mod 性格補正倍率(1.1/0.9/1.0)。呼び出し側が natureMod() 等で解決して渡す。
 */
export function calcStat(base: number, ev: number, iv: number, mod: number, level: number = 50): number {
  return Math.floor((Math.floor((base * 2 + iv + ev * 2) * level / 100) + 5) * mod);
}

export function calcHp(base: number, ev: number, iv: number = 31, level: number = 50): number {
  return Math.floor((base * 2 + iv + ev * 2) * level / 100) + level + 10;
}

/** 指定stat idx(1=A..5=S)に対する性格補正倍率。0(H)は常に1.0。 */
export function natureMod(nature: string, statIdx: number): number {
  if (statIdx === 0) return 1.0;
  const m = NATURE_MODS[nature];
  if (!m) return 1.0;
  const [up, dn] = m;
  if (up === statIdx) return 1.1;
  if (dn === statIdx) return 0.9;
  return 1.0;
}

/**
 * 種族値bs・努力値evs・性格から実数値6つ([H,A,B,C,D,S])を計算する。IVは既定31固定（Lv50前提のモック）。
 */
export function realStats(bs: StatArray, evs: StatArray, nature: string, level: number = 50): StatArray {
  const iv = 31;
  return [
    calcHp(bs[0], evs[0], iv, level),
    calcStat(bs[1], evs[1], iv, natureMod(nature, 1), level),
    calcStat(bs[2], evs[2], iv, natureMod(nature, 2), level),
    calcStat(bs[3], evs[3], iv, natureMod(nature, 3), level),
    calcStat(bs[4], evs[4], iv, natureMod(nature, 4), level),
    calcStat(bs[5], evs[5], iv, natureMod(nature, 5), level),
  ];
}

/** こだわりスカーフ等を反映した有効素早さ。
 * 移植元: scripts/simulator/items.py get_speed_item_multiplier()。
 * 天候依存の素早さ特性(すいすい/ようりょくそ/すながくれ)は相手側の情報が必要なため
 * ここでは扱わない(既知の未対応。damage.ts末尾のコメント参照)。 */
export function effectiveSpeed(speed: number, item: string): number {
  if (item === "こだわりスカーフ") return Math.floor(speed * 1.5);
  if (item === "くろいてっきゅう") return Math.floor(speed * 0.5);
  return speed;
}

const STAT_LETTERS = ["H", "A", "B", "C", "D", "S"] as const;

/** PartySuggestApp.astro の NATURE 定数/natDisp() と同一フォーマットの性格表示。例: "ようき (S↑C↓)"。
 * 無補正(五性)は補正表記なしで性格名のみを返す。空文字は空文字のまま返す。 */
export function natureDisp(nature: string): string {
  if (!nature) return "";
  const m = NATURE_MODS[nature];
  if (!m) return nature;
  const [up, dn] = m;
  return `${nature} (${STAT_LETTERS[up]}↑${STAT_LETTERS[dn]}↓)`;
}
