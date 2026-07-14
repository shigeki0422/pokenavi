// /builder-data/*.json の fetch + メモリキャッシュ
import type { MonDetail, MoveDict, SpeciesMaster, TargetGroup } from "./types";

export interface CoreData {
  species: SpeciesMaster[];
  moves: MoveDict;
  targets: TargetGroup[];
  items: string[];
}

let coreCache: CoreData | null = null;
let corePromise: Promise<CoreData> | null = null;
const monCache = new Map<string, MonDetail>();
const monPromises = new Map<string, Promise<MonDetail>>();

async function fetchJson<T>(url: string): Promise<T> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`fetch failed: ${url} (${res.status})`);
  return (await res.json()) as T;
}

/** species/moves/targets を並列fetchしメモリキャッシュする。2回目以降はキャッシュを返す。 */
export function loadCore(): Promise<CoreData> {
  if (coreCache) return Promise.resolve(coreCache);
  if (corePromise) return corePromise;
  corePromise = (async () => {
    const [species, moves, targets, items] = await Promise.all([
      fetchJson<SpeciesMaster[]>("/builder-data/species.json"),
      fetchJson<MoveDict>("/builder-data/moves.json"),
      fetchJson<TargetGroup[]>("/builder-data/targets.json"),
      fetchJson<string[]>("/builder-data/items.json"),
    ]);
    coreCache = { species, moves, targets, items };
    return coreCache;
  })();
  return corePromise;
}

/** 種ごとの詳細をオンデマンドでfetchし、iconキーでキャッシュする。 */
export function loadMon(icon: string): Promise<MonDetail> {
  const cached = monCache.get(icon);
  if (cached) return Promise.resolve(cached);
  const inflight = monPromises.get(icon);
  if (inflight) return inflight;
  const p = (async () => {
    const detail = await fetchJson<MonDetail>(`/builder-data/mon/${icon}.json`);
    monCache.set(icon, detail);
    monPromises.delete(icon);
    return detail;
  })();
  monPromises.set(icon, p);
  return p;
}

/** loadCore() 済みのspeciesキャッシュから名前で引く同期ルックアップ。未ロード時はundefined。 */
export function speciesByName(n: string): SpeciesMaster | undefined {
  if (!coreCache) return undefined;
  return coreCache.species.find((s) => s.n === n);
}

/** テスト/リセット用: メモリキャッシュを破棄する。 */
export function _resetCacheForTest(): void {
  coreCache = null;
  corePromise = null;
  monCache.clear();
  monPromises.clear();
}
