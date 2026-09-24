// (C15) GA4イベント計測ヘルパ。gtag は BaseHead.astro で PROD 環境のみ読み込まれるため、
// 開発環境やブロッカー等でgtag未定義のときは呼び出し側で判定せずに済むようno-opにする。
type GtagFn = (...args: unknown[]) => void;

declare global {
  interface Window {
    gtag?: GtagFn;
    track?: typeof track;
  }
}

export function track(name: string, params?: Record<string, unknown>): void {
  if (typeof window === 'undefined' || typeof window.gtag !== 'function') return;
  window.gtag('event', name, params ?? {});
}
