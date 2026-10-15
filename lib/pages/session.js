// プレミアム会員のログイン状態（Cloudflare Pages Functions 用）。サイト側にDBは持たない:
// 会員かどうかの正本は Stripe、利用者の識別は Google の固有ID(sub)を SESSION_SECRET で
// HMAC した値(uid)だけ。Cookie には uid・Stripe 顧客ID・会員期限を署名付きで入れる。
const COOKIE = 'pn_s';
const MAX_AGE = 60 * 60 * 24 * 30;
export const RECHECK_SEC = 6 * 60 * 60;

const enc = new TextEncoder();
const b64url = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const fromB64url = (s) => Uint8Array.from(atob(s.replace(/-/g, '+').replace(/_/g, '/')), (c) => c.charCodeAt(0));

async function hmac(secret, data) {
  const key = await crypto.subtle.importKey('raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return crypto.subtle.sign('HMAC', key, enc.encode(data));
}

export async function userId(env, googleSub) {
  return b64url(await hmac(env.SESSION_SECRET, 'google:' + googleSub)).slice(0, 32);
}

export function readCookie(request, name) {
  const m = (request.headers.get('Cookie') || '').match(new RegExp('(?:^|;\\s*)' + name + '=([^;]+)'));
  return m ? decodeURIComponent(m[1]) : null;
}

export async function readSession(request, env) {
  const raw = readCookie(request, COOKIE);
  if (!raw || !env.SESSION_SECRET) return null;
  const [body, sig] = raw.split('.');
  if (!body || !sig || b64url(await hmac(env.SESSION_SECRET, body)) !== sig) return null;
  try {
    return JSON.parse(new TextDecoder().decode(fromB64url(body)));
  } catch (e) {
    return null;
  }
}

export async function sessionCookie(env, s) {
  const body = b64url(enc.encode(JSON.stringify(s)));
  const sig = b64url(await hmac(env.SESSION_SECRET, body));
  return `${COOKIE}=${body}.${sig}; Path=/; Max-Age=${MAX_AGE}; HttpOnly; Secure; SameSite=Lax`;
}

export const clearCookie = (name = COOKIE) => `${name}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`;

export const json = (status, obj, headers = {}) =>
  new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...headers } });

export function redirect(location, cookies = []) {
  const h = new Headers({ Location: location, 'Cache-Control': 'no-store' });
  for (const c of cookies) h.append('Set-Cookie', c);
  return new Response(null, { status: 302, headers: h });
}

export const safeReturn = (p) => (typeof p === 'string' && p.startsWith('/') && !p.startsWith('//') ? p : '/premium/');
