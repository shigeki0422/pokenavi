// Google ログイン（OpenID Connect・scope=openid のみ。メールアドレスや名前は受け取らない）
import { userId, readCookie, readSession, sessionCookies, clearCookie, clearSession, json, redirect, safeReturn, RECHECK_SEC } from '../../../lib/pages/session.js';
import { findCustomer, premiumUntil } from '../../../lib/pages/stripe.js';

const STATE_COOKIE = 'pn_st';
const now = () => Math.floor(Date.now() / 1000);

export async function onRequest(ctx) {
  const { request, env, params } = ctx;
  const action = [].concat(params.path || []).join('/');
  if (!env.BILLING_ENABLED) return json(404, {});
  const url = new URL(request.url);
  const callback = url.origin + '/api/auth/callback';

  if (action === 'login' && request.method === 'GET') {
    const state = crypto.randomUUID();
    const ret = safeReturn(url.searchParams.get('return'));
    const q = new URLSearchParams({ client_id: env.GOOGLE_CLIENT_ID, redirect_uri: callback, response_type: 'code', scope: 'openid', state, prompt: 'select_account' });
    return redirect('https://accounts.google.com/o/oauth2/v2/auth?' + q, [
      `${STATE_COOKIE}=${encodeURIComponent(state + '|' + ret)}; Path=/api/auth/; Max-Age=600; HttpOnly; Secure; SameSite=Lax`,
    ]);
  }

  if (action === 'callback' && request.method === 'GET') {
    const [state, ret] = (readCookie(request, STATE_COOKIE) || '').split('|');
    if (url.searchParams.get('error')) return redirect('/premium/?login=cancelled', [clearCookie(STATE_COOKIE)]);
    if (!state || state !== url.searchParams.get('state') || !url.searchParams.get('code')) return redirect('/premium/?login=failed&r=state', [clearCookie(STATE_COOKIE)]);
    // コードの交換は Google と TLS で直接行うので、返ってきた id_token は署名検証なしで信頼できる（OIDC Core 3.1.3.7）
    const tr = await fetch('https://oauth2.googleapis.com/token', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ code: url.searchParams.get('code'), client_id: env.GOOGLE_CLIENT_ID, client_secret: env.GOOGLE_CLIENT_SECRET, redirect_uri: callback, grant_type: 'authorization_code' }),
    });
    const tok = await tr.json();
    let claims = null;
    try {
      claims = JSON.parse(atob(tok.id_token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/')));
    } catch (e) {}
    if (!tr.ok || !claims || claims.aud !== env.GOOGLE_CLIENT_ID || !['accounts.google.com', 'https://accounts.google.com'].includes(claims.iss) || claims.exp < now() || !claims.sub) {
      return redirect('/premium/?login=failed&r=token', [clearCookie(STATE_COOKIE)]);
    }
    const u = await userId(env, claims.sub);
    const c = await findCustomer(env, u);
    const p = await premiumUntil(env, c);
    return redirect(safeReturn(ret), [clearCookie(STATE_COOKIE), ...(await sessionCookies(env, { u, c, p, t: now() }))]);
  }

  if (action === 'logout' && request.method === 'POST') {
    return json(200, { ok: true }, clearSession());
  }

  if (action === 'me' && request.method === 'GET') {
    const s = await readSession(request, env);
    if (!s) return json(200, { enabled: true, loggedIn: false, premium: false }, clearSession());
    // 期限切れ直後は更新（自動継続）を反映するため、6時間を待たずに1分おきで確かめる
    if (now() - s.t > RECHECK_SEC || (s.p && s.p <= now() && now() - s.t > 60)) {
      if (!s.c) s.c = await findCustomer(env, s.u);
      s.p = await premiumUntil(env, s.c);
      s.t = now();
    }
    const cookies = await sessionCookies(env, s);
    return json(200, { enabled: true, loggedIn: true, premium: s.p > now(), until: s.p || null, customer: !!s.c }, cookies);
  }

  return json(404, {});
}
