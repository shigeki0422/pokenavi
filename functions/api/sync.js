// プレミアム会員の端末間同期（工房のパーティ）。D1（binding: DB）に「会員ID(uid)→Store」を1行だけ持つ。
// uid は Google のIDを HMAC した値で、メールアドレス等の個人情報とは結び付けない。
import { readSession, json } from '../../lib/pages/session.js';

const MAX_BYTES = 512 * 1024;
const now = () => Math.floor(Date.now() / 1000);

async function ensureTable(db) {
  await db.prepare('CREATE TABLE IF NOT EXISTS party_sync (uid TEXT PRIMARY KEY, data TEXT NOT NULL, rev INTEGER NOT NULL, updated_at INTEGER NOT NULL)').run();
}

export async function onRequest({ request, env }) {
  if (!env.BILLING_ENABLED || !env.DB) return json(404, {});
  const s = await readSession(request, env);
  if (!s) return json(401, { error: 'ログインしてください' });
  // 解約後も自分のデータの削除だけはできるようにする
  if (request.method !== 'DELETE' && !(s.p > now())) return json(403, { error: '端末間の同期はプレミアム会員の機能です' });
  await ensureTable(env.DB);

  if (request.method === 'GET') {
    const row = await env.DB.prepare('SELECT data, rev, updated_at FROM party_sync WHERE uid = ?').bind(s.u).first();
    return json(200, row ? { data: JSON.parse(row.data), rev: row.rev, updatedAt: row.updated_at } : { data: null, rev: 0 });
  }

  if (request.method === 'PUT') {
    const text = await request.text();
    if (text.length > MAX_BYTES) return json(413, { error: '保存できる大きさを超えています' });
    let body;
    try { body = JSON.parse(text); } catch (e) { return json(400, { error: 'invalid json' }); }
    const { data, baseRev } = body || {};
    if (!data || typeof data !== 'object' || !Array.isArray(data.parties) || !Number.isInteger(baseRev)) return json(400, { error: 'invalid' });
    const payload = JSON.stringify(data);
    // 版番号が合うときだけ書く（他の端末が先に書いていたら 409 で今の中身を返し、端末側で統合し直す）
    const r = baseRev === 0
      ? await env.DB.prepare('INSERT INTO party_sync (uid, data, rev, updated_at) VALUES (?, ?, 1, ?) ON CONFLICT(uid) DO NOTHING').bind(s.u, payload, now()).run()
      : await env.DB.prepare('UPDATE party_sync SET data = ?, rev = rev + 1, updated_at = ? WHERE uid = ? AND rev = ?').bind(payload, now(), s.u, baseRev).run();
    if (!r.meta.changes) {
      const cur = await env.DB.prepare('SELECT data, rev FROM party_sync WHERE uid = ?').bind(s.u).first();
      return json(409, cur ? { data: JSON.parse(cur.data), rev: cur.rev } : { data: null, rev: 0 });
    }
    return json(200, { rev: baseRev + 1 });
  }

  if (request.method === 'DELETE') {
    await env.DB.prepare('DELETE FROM party_sync WHERE uid = ?').bind(s.u).run();
    return json(200, { ok: true });
  }

  return json(405, {});
}
