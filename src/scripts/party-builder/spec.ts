// spec文字列 <-> Slot 相互変換。scripts/simulator/pokemon.py: parse_pokemon_spec 互換書式。
// 書式: 種名@持ち物:性格:技1|技2|技3|技4:H/A/B/C/D/S:特性 （5フィールド固定・厳密検証）
import type { Party, Slot, StatArray } from "./types";
import { ALL_NATURES, EV_STAT_MAX } from "./stats";

const SLOT_COUNT = 6;

function genId(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
}

// M-4「軸から簡単構築」(scripts/gen_party_pool.py) の型プールは種名にFORM_FIX（コロン形の
// spec区切りとの衝突回避）を適用済みで返す。工房 species.json はcrawlerの使用率名(コロン形含む)を
// そのまま使うため、提案API由来のspecを取り込む際はここで名前を揃える必要がある。
// gen_party_pool.py FORM_FIXの逆写像 + 同種族値/同タイプの代替解決(性別フォーム等・見た目のみ簡略化)。
// 一覧の突合結果(2026-07-15時点、pool種名 vs species.json n)は上記2種のみが真の表記不一致で、
// 他の不一致(エンブオー/スピンロトム/パンプジン(ちゅうだましゅ)/ヒスイダイケンキ)は
// species.json(使用率上位200種)に元々収録が無いカバレッジ欠落のため、ここに追加してはならない
// (誤って別種にマッピングしてしまう。特にヒスイダイケンキは通常のダイケンキとタイプが異なる別種)。
const SUGGEST_NAME_FIX: Record<string, string> = {
  "パルデアケンタロス(炎)": "ケンタロス:炎",
  "パルデアケンタロス(水)": "ケンタロス:水",
  "パルデアケンタロス(闘)": "ケンタロス:格",
  "ニャオニクス(メス)": "ニャオニクス(オス)", // 種族値・タイプは同一、アイコン/特性表示のみオス型に簡略化
};

/** 提案API(型プール)由来の種名を工房species.jsonの表記に正規化する。対応表に無い名前はそのまま返す。 */
export function normalizeSuggestSpeciesName(name: string): string {
  return SUGGEST_NAME_FIX[name] || name;
}

/** 「軸から簡単構築」が返す spec 文字列（scripts/gen_party_pool.py 生成、fromSpec と同一書式）を
 * 種名正規化のうえ Slot 化する。fromSpec と違い種名部分のみ SUGGEST_NAME_FIX を通す。 */
export function fromSuggestSpec(s: string): Slot | null {
  if (typeof s !== "string") return null;
  const atIdx = s.indexOf("@");
  if (atIdx < 0) return fromSpec(s);
  const sp = normalizeSuggestSpeciesName(s.slice(0, atIdx).trim());
  return fromSpec(sp + s.slice(atIdx));
}

export function toSpec(slot: Slot): string {
  const moves = (slot.moves || []).join("|");
  const evs = slot.evs.join("/");
  return `${slot.sp}@${slot.item || ""}:${slot.nature || ""}:${moves}:${evs}:${slot.ability || ""}`;
}

function parseEvs(raw: string): StatArray | null {
  const toks = raw.split("/");
  if (toks.length !== 6) return null;
  const vals: number[] = [];
  for (const t of toks) {
    if (!/^\d+$/.test(t)) return null;
    const n = Number(t);
    if (!Number.isInteger(n) || n < 0 || n > EV_STAT_MAX) return null;
    vals.push(n);
  }
  return vals as StatArray;
}

export function fromSpec(s: string): Slot | null {
  if (typeof s !== "string") return null;
  const atCount = (s.match(/@/g) || []).length;
  if (atCount !== 1) return null;
  const atIdx = s.indexOf("@");
  const sp = s.slice(0, atIdx).trim();
  if (!sp) return null;
  const rest = s.slice(atIdx + 1);
  const fields = rest.split(":");
  if (fields.length !== 5) return null;
  const [itemRaw, natureRaw, movesRaw, evRaw, abilityRaw] = fields;

  const item = itemRaw.trim();

  const nature = natureRaw.trim();
  if (nature && !ALL_NATURES.includes(nature)) return null;

  let moves: string[] = [];
  const movesTrim = movesRaw.trim();
  if (movesTrim !== "") {
    moves = movesTrim.split("|").map((m) => m.trim());
    if (moves.some((m) => m === "")) return null;
    if (moves.length > 4) return null;
  }

  const evs = parseEvs(evRaw.trim());
  if (!evs) return null;

  const ability = abilityRaw.trim();

  return { sp, item, ability, nature, evs, moves, targets: [] };
}

export function exportParty(p: Party): string {
  const lines: string[] = [];
  for (let i = 0; i < SLOT_COUNT; i++) {
    const slot = p.slots[i];
    lines.push(slot ? toSpec(slot) : "");
  }
  return lines.join("\n");
}

export function importParty(text: string): Party | null {
  if (typeof text !== "string") return null;
  const lines = text.split(/\r?\n/);
  // 末尾の余分な空行は許容(コピペ時のトレーリング改行対策)
  while (lines.length > SLOT_COUNT && lines[lines.length - 1].trim() === "") lines.pop();
  if (lines.length !== SLOT_COUNT) return null;

  const slots: (Slot | null)[] = [];
  for (const line of lines) {
    if (line.trim() === "") {
      slots.push(null);
      continue;
    }
    const slot = fromSpec(line);
    if (!slot) return null;
    slots.push(slot);
  }

  const now = Date.now();
  return {
    id: genId(),
    name: "インポート",
    createdAt: now,
    updatedAt: now,
    slots,
  };
}
