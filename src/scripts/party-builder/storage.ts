// localStorage CRUD + バージョニング。キー: pn-builder-v1
import type { Party, Slot, StatArray, Store, TargetBuild, TargetGroup } from "./types";

export const STORAGE_KEY = "pn-builder-v1";
const SAVE_DEBOUNCE_MS = 300;

function genId(): string {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
}

function initialStore(): Store {
  return { v: 1, activeId: null, parties: [] };
}

/** Slot・TargetBuildの個々のフィールドを深く検証せず「オブジェクトかnullか」だけを見る構造チェック。
 * フィールド単位の型崩れ(数値のはずが文字列等)はここでは弾かない ―― sanitizeSlot/sanitizeTargetBuild
 * が値を矯正・除去する(H2: customTargets改竄によるXSS/クラッシュ対策の1層目)。 */
function isSlot(x: any): boolean {
  return !!x && typeof x === "object";
}

function isParty(x: any): x is Party {
  if (!x || typeof x !== "object") return false;
  if (typeof x.id !== "string" || typeof x.name !== "string") return false;
  if (typeof x.createdAt !== "number" || typeof x.updatedAt !== "number") return false;
  if (!Array.isArray(x.slots) || x.slots.length !== 6) return false;
  return x.slots.every((s: any) => s === null || isSlot(s));
}

function toStr(x: any): string {
  return typeof x === "string" ? x : "";
}

/** 長さ6の数値配列に矯正する。数値化できない要素は0、min/maxが与えられれば範囲にクランプする。 */
function toNumArray6(x: any, min?: number, max?: number): [number, number, number, number, number, number] {
  const src = Array.isArray(x) ? x : [];
  const out: number[] = [];
  for (let i = 0; i < 6; i++) {
    let n = Number(src[i]);
    if (!Number.isFinite(n)) n = 0;
    if (min !== undefined) n = Math.max(min, n);
    if (max !== undefined) n = Math.min(max, n);
    out.push(Math.round(n));
  }
  return out as [number, number, number, number, number, number];
}

function toStrArray(x: any): string[] {
  return Array.isArray(x) ? x.filter((v): v is string => typeof v === "string") : [];
}

/** localStorage(改竄可能)由来のSlotを深く検証・矯正する。sp が空/非文字列なら復元不能として null(=空枠)にする。 */
function sanitizeSlot(x: any): Slot | null {
  if (!x || typeof x !== "object") return null;
  const sp = toStr(x.sp);
  if (!sp) return null;
  return {
    sp,
    item: toStr(x.item),
    ability: toStr(x.ability),
    nature: toStr(x.nature),
    evs: toNumArray6(x.evs, 0, 32) as StatArray,
    moves: toStrArray(x.moves),
    targets: toStrArray(x.targets),
  };
}

/** localStorage由来のTargetBuild(仮想敵カスタム型)を深く検証・矯正する。t1(タイプ)が欠落した
 * ビルドは相性計算の前提が崩れるため復元不能としてnullを返す(呼び出し側で配列から除去)。 */
function sanitizeTargetBuild(x: any): TargetBuild | null {
  if (!x || typeof x !== "object") return null;
  const t1 = toStr(x.t1);
  if (!t1) return null;
  const t2raw = x.t2;
  const t2 = typeof t2raw === "string" && t2raw ? t2raw : null;
  let idx = Number(x.idx);
  if (!Number.isFinite(idx) || idx < 0) idx = 0;
  return {
    idx: Math.round(idx),
    item: toStr(x.item),
    nature: toStr(x.nature),
    ability: toStr(x.ability),
    ev: toNumArray6(x.ev, 0, 32) as StatArray,
    moves: toStrArray(x.moves),
    t1,
    t2,
    bs: toNumArray6(x.bs) as StatArray,
    spec: toStr(x.spec),
  };
}

function isStore(x: any): x is Store {
  if (!x || typeof x !== "object") return false;
  if (x.v !== 1) return false;
  if (!("activeId" in x) || (typeof x.activeId !== "string" && x.activeId !== null)) return false;
  if (!Array.isArray(x.parties)) return false;
  return x.parties.every(isParty);
}

/** customTargets(仮想敵カスタム型)の深いサニタイズ(H2)。各buildをsanitizeTargetBuildで検証・矯正し、
 * 不正なbuildは配列から除去する。labelの全buildが不正だった場合はそのラベルのエントリごと削除する
 * (既存Store v1に対する後方互換の追加フィールドのためバージョン上げ不要)。 */
function sanitizeCustomTargets(x: any): Record<string, TargetBuild[]> | undefined {
  if (!x || typeof x !== "object" || Array.isArray(x)) return undefined;
  const out: Record<string, TargetBuild[]> = {};
  for (const [label, builds] of Object.entries(x)) {
    if (!Array.isArray(builds)) continue;
    const cleaned = builds.map(sanitizeTargetBuild).filter((b): b is TargetBuild => b !== null);
    if (cleaned.length) out[label] = cleaned;
  }
  return Object.keys(out).length ? out : undefined;
}

/** 穴(null)を左詰めする(migrate用)。既存データが枠の途中でnullを持っていても、
 * 埋まっている枠を前方に詰め、末尾にnullを補って長さ6を維持する。 */
function compactSlots(slots: (Slot | null)[]): (Slot | null)[] {
  const filled = slots.filter((s): s is Slot => s !== null);
  const out: (Slot | null)[] = [...filled];
  while (out.length < 6) out.push(null);
  return out;
}

export function loadStore(): Store {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return initialStore();
    const parsed = JSON.parse(raw);
    if (!isStore(parsed)) return initialStore();
    parsed.parties.forEach((p) => {
      p.slots = compactSlots(p.slots.map((s) => (s === null ? null : sanitizeSlot(s))));
    });
    const sane = sanitizeCustomTargets(parsed.customTargets);
    if (sane) parsed.customTargets = sane;
    else delete parsed.customTargets;
    return parsed;
  } catch {
    return initialStore();
  }
}

/**
 * 仮想敵の「効果的builds」を返すヘルパ。store.customTargets に該当ラベルの編集済み型があれば
 * それで targets.json 由来のbuildsを差し替える。targets.json参照箇所(マトリクス・穴判定・仮想敵パネル)は
 * すべてこのヘルパ経由で取得すること(core.targets を直接参照しない)。
 */
export function getEffectiveTargets(store: Store, coreTargets: TargetGroup[]): TargetGroup[] {
  const custom = store.customTargets;
  if (!custom) return coreTargets;
  return coreTargets.map((g) => {
    const builds = custom[g.label];
    return builds && builds.length ? { ...g, builds } : g;
  });
}

let saveTimer: ReturnType<typeof setTimeout> | null = null;

/** 300msデバウンスでlocalStorageへ書き込む。 */
export function saveStore(s: Store): void {
  if (saveTimer) clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    saveTimer = null;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(s));
    } catch {
      // localStorage不可(容量超過・シークレットモード等)は無視。UIはsaveStore呼び出し側で失敗を気にしない設計。
    }
  }, SAVE_DEBOUNCE_MS);
}

function emptySlots(): (Slot | null)[] {
  return [null, null, null, null, null, null];
}

export function createParty(store: Store, name?: string): Party {
  const now = Date.now();
  const party: Party = {
    id: genId(),
    name: name && name.trim() ? name.trim() : `パーティ${store.parties.length + 1}`,
    createdAt: now,
    updatedAt: now,
    slots: emptySlots(),
  };
  store.parties.push(party);
  store.activeId = party.id;
  saveStore(store);
  return party;
}

/** 6枠ぶんのSlot配列(不足分はnullで補われている前提)からパーティを新規作成しアクティブ化する。
 * 「軸から簡単構築」からの引き継ぎインポート等、既に組み上がったSlotを丸ごと1パーティとして
 * 追加したいケース向け(createPartyは常に空枠から作る点が異なる)。 */
export function createPartyFromSlots(store: Store, slots: (Slot | null)[], name?: string): Party {
  const now = Date.now();
  const padded = slots.slice(0, 6);
  while (padded.length < 6) padded.push(null);
  const party: Party = {
    id: genId(),
    name: name && name.trim() ? name.trim() : `パーティ${store.parties.length + 1}`,
    createdAt: now,
    updatedAt: now,
    slots: padded,
  };
  store.parties.push(party);
  store.activeId = party.id;
  saveStore(store);
  return party;
}

export function duplicateParty(store: Store, id: string): Party | null {
  const src = store.parties.find((p) => p.id === id);
  if (!src) return null;
  const now = Date.now();
  const copy: Party = {
    id: genId(),
    name: `${src.name}のコピー`,
    createdAt: now,
    updatedAt: now,
    slots: src.slots.map((s): Slot | null =>
      s ? { ...s, evs: [...s.evs] as StatArray, moves: [...s.moves], targets: [...s.targets] } : null
    ),
  };
  store.parties.push(copy);
  store.activeId = copy.id;
  saveStore(store);
  return copy;
}

export function renameParty(store: Store, id: string, name: string): boolean {
  const p = store.parties.find((pp) => pp.id === id);
  if (!p || !name.trim()) return false;
  p.name = name.trim();
  p.updatedAt = Date.now();
  saveStore(store);
  return true;
}

export function deleteParty(store: Store, id: string): boolean {
  const idx = store.parties.findIndex((p) => p.id === id);
  if (idx === -1) return false;
  store.parties.splice(idx, 1);
  if (store.activeId === id) {
    store.activeId = store.parties.length ? store.parties[0].id : null;
  }
  saveStore(store);
  return true;
}
