// プレミアムの申込み（Stripe Checkout）と管理（カスタマーポータル）。カード情報は Stripe だけが扱う
import { readSession, sessionCookies, json, redirect } from '../../../lib/pages/session.js';
import { stripe, premiumUntil } from '../../../lib/pages/stripe.js';

const now = () => Math.floor(Date.now() / 1000);

export async function onRequest(ctx) {
  const { request, env, params } = ctx;
  const action = [].concat(params.path || []).join('/');
  if (!env.BILLING_ENABLED) return json(404, {});
  const origin = new URL(request.url).origin;
  const s = await readSession(request, env);

  if (action === 'checkout' && request.method === 'POST') {
    if (!s) return json(401, { error: 'ログインしてください' });
    if (s.p > now()) return json(409, { error: 'すでにプレミアム会員です' });
    const cs = await stripe(env, 'POST', 'checkout/sessions', {
      mode: 'subscription',
      line_items: { 0: { price: env.STRIPE_PRICE_ID, quantity: 1 } },
      customer: s.c || undefined,
      client_reference_id: s.u,
      subscription_data: { metadata: { pn_uid: s.u } },
      // 改正特商法の最終確認画面: 価格・自動更新は Checkout が表示する。規約と解約・返金の条件へのリンクを添える
      custom_text: { submit: { message: `お申込みにより[利用規約](${origin}/terms/)に同意したものとみなします。毎月自動で更新され、いつでも解約できます（日割りの返金はありません）。詳しくは[特定商取引法に基づく表記](${origin}/tokushoho/)をご覧ください。` } },
      locale: 'ja',
      success_url: `${origin}/api/billing/return?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${origin}/premium/`,
    });
    return json(200, { url: cs.url });
  }

  if (action === 'return' && request.method === 'GET') {
    const id = new URL(request.url).searchParams.get('session_id') || '';
    if (!s || !/^cs_[A-Za-z0-9_]+$/.test(id)) return redirect('/premium/');
    const cs = await stripe(env, 'GET', `checkout/sessions/${id}`);
    if (cs.client_reference_id !== s.u || !cs.customer) return redirect('/premium/');
    // 次回のログインで顧客を見つけられるよう、顧客に uid を記録する（メールアドレス等はサイト側に持たない）
    await stripe(env, 'POST', `customers/${cs.customer}`, { metadata: { pn_uid: s.u } });
    const next = { ...s, c: cs.customer, p: await premiumUntil(env, cs.customer), t: now() };
    return redirect('/premium/?welcome=1', await sessionCookies(env, next));
  }

  if (action === 'portal' && request.method === 'POST') {
    if (!s?.c) return json(401, { error: 'ログインしてください' });
    const ps = await stripe(env, 'POST', 'billing_portal/sessions', { customer: s.c, return_url: `${origin}/premium/` });
    return json(200, { url: ps.url });
  }

  return json(404, {});
}
