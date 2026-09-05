// アクティブパーティに対する構成ルール検証(純ロジック)。
// もちもの重複・EV合計超過(>66)・図鑑番号重複(species.jsonのicon先頭4桁)を検出する。
import type { Party, SpeciesMaster, Slot } from "./types";
import { EV_TOTAL_MAX } from "./stats";

export interface ValidationIssue {
  type: "item-dup" | "ev-over" | "dex-dup";
  message: string;
}

function filledSlots(party: Party): Slot[] {
  return party.slots.filter((s): s is Slot => !!s);
}

/** メガストーンを持たせている場合はメガ名、それ以外は種族名を返す(表示用ラベル)。 */
function labelOf(slot: Slot, sm: SpeciesMaster | undefined): string {
  if (!sm) return slot.sp;
  const mega = slot.item ? sm.mega.find((m) => m.stone === slot.item) : undefined;
  return mega ? mega.name : sm.n;
}

/** species.json の icon は "0445-00" 形式。先頭4桁が図鑑番号(フォーム違い・メガ元は同番号)。 */
function dexNoOf(icon: string): string {
  return icon.slice(0, 4);
}

export function validateParty(party: Party, species: SpeciesMaster[]): ValidationIssue[] {
  const out: ValidationIssue[] = [];
  const slots = filledSlots(party);
  const smOf = new Map(species.map((s) => [s.n, s]));

  // もちもの重複(「なし」＝空文字は対象外)
  const byItem = new Map<string, string[]>();
  for (const s of slots) {
    if (!s.item) continue;
    const label = labelOf(s, smOf.get(s.sp));
    const arr = byItem.get(s.item) ?? [];
    arr.push(label);
    byItem.set(s.item, arr);
  }
  for (const [item, labels] of byItem) {
    if (labels.length >= 2) {
      out.push({ type: "item-dup", message: `持ち物重複: ${item}(${labels.join("、")})` });
    }
  }

  // EV合計超過(1体の合計 > 66)
  for (const s of slots) {
    const sum = s.evs.reduce((a, b) => a + b, 0);
    if (sum > EV_TOTAL_MAX) {
      const label = labelOf(s, smOf.get(s.sp));
      out.push({ type: "ev-over", message: `EV合計超過: ${label}(合計${sum}、上限${EV_TOTAL_MAX})` });
    }
  }

  // 図鑑番号重複(フォーム違い・メガ元は同番号なので重複扱い)
  const byDex = new Map<string, string[]>();
  for (const s of slots) {
    const sm = smOf.get(s.sp);
    if (!sm) continue;
    const dex = dexNoOf(sm.icon);
    const label = labelOf(s, sm);
    const arr = byDex.get(dex) ?? [];
    arr.push(label);
    byDex.set(dex, arr);
  }
  for (const [dex, labels] of byDex) {
    if (labels.length >= 2) {
      out.push({ type: "dex-dup", message: `図鑑番号重複: ${labels.join("、")}(#${dex})` });
    }
  }

  return out;
}
