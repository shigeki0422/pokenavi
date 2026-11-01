// プレミアム会員の端末間同期。保存先は /api/sync（Cloudflare D1。会員ID→Store 1件）。
// 工房を開いたときにサーバーの Store と統合し、以後は保存のたびに少し待って送る。
import type { Party, Store } from "./types";
import { onStoreSaved, sanitizeStore } from "./storage";

const PUSH_DEBOUNCE_MS = 3000;
const TOMBSTONE_TTL_MS = 90 * 24 * 60 * 60 * 1000;
const MAX_BYTES = 512 * 1024;

export type SyncState = "syncing" | "ok" | "error" | "too-large";

/** 新しい端末で自動的に作られた、まだ一度も触っていない空のパーティ */
const untouchedEmpty = (p: Party) => p.slots.every((s) => !s) && p.updatedAt === p.createdAt;

/** パーティごとに新しい方を採り、削除の記録より古いものは消す。activeId は端末ごとなので手元を優先。 */
export function mergeStores(local: Store, remote: Store | null): Store {
  if (!remote) return local;
  const now = Date.now();
  const deleted: Record<string, number> = {};
  for (const src of [remote.deleted, local.deleted]) {
    for (const [id, at] of Object.entries(src || {})) {
      if (now - at < TOMBSTONE_TTL_MS) deleted[id] = Math.max(deleted[id] || 0, at);
    }
  }
  const byId = new Map<string, Party>(remote.parties.map((p) => [p.id, p]));
  const remoteHasReal = remote.parties.some((p) => !untouchedEmpty(p));
  for (const p of local.parties) {
    if (remoteHasReal && untouchedEmpty(p) && !byId.has(p.id)) continue;
    const r = byId.get(p.id);
    if (!r || p.updatedAt >= r.updatedAt) byId.set(p.id, p);
  }
  for (const [id, at] of Object.entries(deleted)) {
    const p = byId.get(id);
    if (p && p.updatedAt <= at) byId.delete(id);
  }
  const parties = [...byId.values()].sort((a, b) => a.createdAt - b.createdAt);
  const activeId = parties.some((p) => p.id === local.activeId) ? local.activeId : parties[0]?.id ?? null;
  const customTargets = { ...(remote.customTargets || {}), ...(local.customTargets || {}) };
  const out: Store = { v: 1, activeId, parties };
  if (Object.keys(customTargets).length) out.customTargets = customTargets;
  if (Object.keys(deleted).length) out.deleted = deleted;
  return out;
}

/** 送る中身（activeId は端末ごとなので比較にも送信にも含めない） */
const payloadOf = (s: Store) => JSON.stringify({ v: 1, activeId: null, parties: s.parties, customTargets: s.customTargets, deleted: s.deleted });

export function startSync(opts: { getStore: () => Store; replaceStore: (s: Store) => void; onState: (st: SyncState, at?: number) => void }): void {
  let rev = 0;
  let lastSent = "";
  let timer: ReturnType<typeof setTimeout> | null = null;

  async function push(keepalive = false, retried = false): Promise<void> {
    timer = null;
    const body = payloadOf(opts.getStore());
    if (body === lastSent) return;
    if (body.length > MAX_BYTES) { opts.onState("too-large"); return; }
    opts.onState("syncing");
    try {
      const r = await fetch("/api/sync", { method: "PUT", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ baseRev: rev, data: JSON.parse(body) }), keepalive });
      const d = await r.json().catch(() => ({}));
      if (r.status === 409 && !retried) {
        // 他の端末が先に書いた。統合し直して送り直す
        rev = d.rev || 0;
        opts.replaceStore(mergeStores(opts.getStore(), sanitizeStore(d.data)));
        return push(keepalive, true);
      }
      if (!r.ok) throw new Error(String(r.status));
      rev = d.rev;
      lastSent = body;
      opts.onState("ok", Date.now());
    } catch {
      opts.onState("error");
    }
  }

  (async () => {
    opts.onState("syncing");
    try {
      const r = await fetch("/api/sync");
      if (!r.ok) throw new Error(String(r.status));
      const d = await r.json();
      rev = d.rev || 0;
      const remote = d.data ? sanitizeStore(d.data) : null;
      const local = opts.getStore();
      const merged = mergeStores(local, remote);
      if (payloadOf(merged) !== payloadOf(local)) opts.replaceStore(merged);
      lastSent = remote ? payloadOf(remote) : "";
      if (payloadOf(merged) !== lastSent) await push();
      else opts.onState("ok", Date.now());
    } catch {
      opts.onState("error");
      return;
    }
    onStoreSaved(() => {
      if (timer) clearTimeout(timer);
      timer = setTimeout(() => push(), PUSH_DEBOUNCE_MS);
    });
    // 待ち時間中に閉じられても失わないよう、隠れるときは待たずに送る
    document.addEventListener("visibilitychange", () => {
      if (document.visibilityState === "hidden" && timer) { clearTimeout(timer); push(true); }
    });
  })();
}
