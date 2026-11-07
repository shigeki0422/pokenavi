// /api/* → Cloud Run(pokenavi-suggest) の中継。ブラウザに Cloud Run の URL を出さず、
// Cloud Run 側は PROXY_SECRET を知るこの中継からの呼び出しだけを受け付けられるようにする。
import { readSession } from '../../lib/pages/session.js';

const ORIGIN = 'https://pokenavi-suggest-799947701075.asia-northeast1.run.app';
// パーティ診断は CPU を多く割り当てた別サービス（env.DIAG_ORIGIN）へ。並列に回せる計算なので台の CPU を増やすほど待ちが縮む。
// 改善案（improve）は画面から外しているので提案サービス側のまま
const DIAG_PATHS = new Set(['diagnose', 'diag_battle', 'job_status']);
const GET_PATHS = new Set(['species']);
const POST_PATHS = new Set(['suggest', 'simulate', 'complete', 'speed_detail', 'atk_detail', 'guide', 'diagnose', 'diag_battle', 'improve', 'job_status']);
const MAX_BODY_BYTES = 16 * 1024;
const MAX_CORE = 6; // パーティは6体。画面・サーバーと同じ上限

const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });

export async function onRequest({ request, env, params, waitUntil }) {
  const path = [].concat(params.path || []).join('/');
  const method = request.method;
  if (method === 'GET' ? !GET_PATHS.has(path) : method !== 'POST' || !POST_PATHS.has(path)) return json(404, {});

  const cacheKey = new Request(new URL(request.url).origin + '/api/' + path);
  if (method === 'GET') {
    const hit = await caches.default.match(cacheKey);
    if (hit) return hit;
  }

  const headers = {
    'X-Pokenavi-Proxy': env.PROXY_SECRET || '',
    'X-Pokenavi-Client-IP': request.headers.get('CF-Connecting-IP') || '',
  };
  // 診断の無料枠はプレミアム会員には掛けない（会員期限は署名付き Cookie の値。Stripe への問い合わせはしない）
  if (env.BILLING_ENABLED && (path === 'diagnose' || path === 'diag_battle')) {
    const s = await readSession(request, env);
    if (s && s.p > Math.floor(Date.now() / 1000)) headers['X-Pokenavi-Premium'] = '1';
  }
  let body;
  if (method === 'POST') {
    // サーバーは Content-Length で本文を読むので、chunked にならないよう読み切ってから送る
    body = await request.arrayBuffer();
    if (body.byteLength > MAX_BODY_BYTES) return json(413, { error: `リクエストボディが大きすぎます（上限${MAX_BODY_BYTES}バイト）` });
    headers['Content-Type'] = 'application/json';
    if (path === 'suggest') {
      let core;
      try { core = JSON.parse(new TextDecoder().decode(body)).core; } catch (e) { return json(400, { error: 'invalid json' }); }
      if (core != null && (!Array.isArray(core) || core.length > MAX_CORE)) return json(400, { error: `軸は${MAX_CORE}体までです` });
    }
  }

  let res;
  try {
    const origin = env.DIAG_ORIGIN && DIAG_PATHS.has(path) ? env.DIAG_ORIGIN : ORIGIN;
    res = await fetch(`${origin}/${path}`, { method, headers, body });
  } catch (e) {
    return json(502, { error: '計算サーバーに接続できませんでした' });
  }
  const out = new Response(res.body, { status: res.status, headers: { 'Content-Type': res.headers.get('Content-Type') || 'application/json; charset=utf-8' } });
  if (method === 'GET' && res.ok) {
    out.headers.set('Cache-Control', 'public, max-age=600');
    waitUntil(caches.default.put(cacheKey, out.clone()));
  }
  return out;
}
