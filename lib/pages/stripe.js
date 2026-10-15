// Stripe REST API の薄い呼び出し（SDK は Workers で重いので使わない）
const API = 'https://api.stripe.com/v1/';

function form(obj, prefix = '', out = new URLSearchParams()) {
  for (const [k, v] of Object.entries(obj)) {
    if (v == null) continue;
    const key = prefix ? `${prefix}[${k}]` : k;
    if (typeof v === 'object') form(v, key, out);
    else out.append(key, String(v));
  }
  return out;
}

export async function stripe(env, method, path, params) {
  const url = API + path + (method === 'GET' && params ? '?' + form(params) : '');
  const res = await fetch(url, {
    method,
    headers: { Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`, 'Content-Type': 'application/x-www-form-urlencoded', 'Stripe-Version': '2024-06-20' },
    body: method === 'GET' ? undefined : form(params || {}),
  });
  const d = await res.json();
  if (!res.ok) throw new Error(`stripe ${path}: ${d.error?.message || res.status}`);
  return d;
}

export async function findCustomer(env, uid) {
  const r = await stripe(env, 'GET', 'customers/search', { query: `metadata['pn_uid']:'${uid}'`, limit: 1 });
  return r.data[0]?.id || null;
}

// 会員期限（unix秒）。有効なサブスクが無ければ 0
export async function premiumUntil(env, customerId) {
  if (!customerId) return 0;
  const r = await stripe(env, 'GET', 'subscriptions', { customer: customerId, status: 'all', limit: 5 });
  let until = 0;
  for (const s of r.data) {
    if (!['active', 'trialing', 'past_due'].includes(s.status)) continue;
    const end = s.current_period_end || s.items?.data?.[0]?.current_period_end || 0;
    until = Math.max(until, end);
  }
  return until;
}
