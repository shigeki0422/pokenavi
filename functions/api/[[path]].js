// /api/* → Cloud Run(pokenavi-suggest) の中継。ブラウザに Cloud Run の URL を出さず、
// Cloud Run 側は PROXY_SECRET を知るこの中継からの呼び出しだけを受け付けられるようにする。
const ORIGIN = 'https://pokenavi-suggest-799947701075.asia-northeast1.run.app';
const GET_PATHS = new Set(['species']);
const POST_PATHS = new Set(['suggest', 'simulate', 'complete', 'speed_detail', 'atk_detail', 'guide', 'diagnose', 'diag_battle', 'improve', 'job_status']);
const MAX_BODY_BYTES = 16 * 1024;

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
  let body;
  if (method === 'POST') {
    // サーバーは Content-Length で本文を読むので、chunked にならないよう読み切ってから送る
    body = await request.arrayBuffer();
    if (body.byteLength > MAX_BODY_BYTES) return json(413, { error: `リクエストボディが大きすぎます（上限${MAX_BODY_BYTES}バイト）` });
    headers['Content-Type'] = 'application/json';
  }

  let res;
  try {
    res = await fetch(`${ORIGIN}/${path}`, { method, headers, body });
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
