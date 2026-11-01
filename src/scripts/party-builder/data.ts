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

/** search-index.json のポケモンレコード(名前→各言語URL)。相性/素早さタブの相手ヘッダを
 * 紹介ページへリンク化するための解決に使う(ページが存在しない種はエントリ自体が無い)。 */
export interface PokemonUrlEntry {
  u: string;
  ue: string;
  uk: string;
}
let nameUrlCache: Map<string, PokemonUrlEntry> | null = null;
let nameUrlPromise: Promise<Map<string, PokemonUrlEntry>> | null = null;

/** 仮想敵（1v1・素早さの相手）の体数。プレミアム会員は上位50体（counter-targets.json＝上位100体の先頭。先頭は targets.json と同一）。 */
export const TARGET_N =
  typeof document !== "undefined" && document.documentElement.classList.contains("pn-premium") ? 50 : 30;

/** 使用率順の先頭 n 種ぶん（メガX/Yで1種が複数エントリに分かれる） */
function topSpecies(groups: TargetGroup[], n: number): TargetGroup[] {
  const seen = new Set<string>();
  return groups.filter((g) => {
    if (!seen.has(g.sp)) seen.add(g.sp);
    return seen.size <= n;
  });
}

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
      TARGET_N > 30
        ? fetchJson<TargetGroup[]>("/builder-data/counter-targets.json").then((t) => topSpecies(t, TARGET_N))
        : fetchJson<TargetGroup[]>("/builder-data/targets.json"),
      fetchJson<string[]>("/builder-data/items.json"),
    ]);
    coreCache = { species, moves, targets, items };
    return coreCache;
  })();
  return corePromise;
}

/**
 * search-index.json のポケモンレコード(t:'p')を名前(和名)→{u,ue,uk}のMapにしてキャッシュする。
 * draft記事(ページが未生成)は search-index.json 生成時点で既に除外されているため、
 * このMapに無い種＝紹介ページが存在しない種として扱ってよい。
 */
export function loadNameUrlMap(): Promise<Map<string, PokemonUrlEntry>> {
  if (nameUrlCache) return Promise.resolve(nameUrlCache);
  if (nameUrlPromise) return nameUrlPromise;
  nameUrlPromise = (async () => {
    const records = await fetchJson<Array<Record<string, unknown>>>("/search-index.json");
    const map = new Map<string, PokemonUrlEntry>();
    for (const r of records) {
      if (r.t === "p" && typeof r.n === "string" && typeof r.u === "string") {
        map.set(r.n, { u: r.u, ue: String(r.ue ?? r.u), uk: String(r.uk ?? r.u) });
      }
    }
    nameUrlCache = map;
    return map;
  })();
  return nameUrlPromise;
}

/** loadNameUrlMap() 済みのキャッシュから同期で引く。未ロード時はnull(呼び出し側はリンク無し表示にフォールバック)。 */
export function nameUrlMapSync(): Map<string, PokemonUrlEntry> | null {
  return nameUrlCache;
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
