// (C03) 横スクロール可能な相性表(.mg)の右端フェード+矢印ヒント。
// 簡単構築(PartySuggestApp.astro)にあった実装を、工房(PartyBuilderApp.astro)とも共有するため切り出した。
// CSS(.mg-wrap/.mg-hint/.mg-wrap.mg-scrolled)は各ページ側のスタイルシートに残したまま、
// マークアップ生成(mgWrapHtml)とヒントの表示/消去ロジック(initMgHints)だけをここに集約する。

/** テーブルHTMLを.mg-wrap({.mg}+{.mg-hint})で包む。 */
export function mgWrapHtml(tableHtml: string): string {
  return `<div class="mg-wrap"><div class="mg">${tableHtml}</div><div class="mg-hint" aria-hidden="true">→</div></div>`;
}

/** 新しく描画された.mg-wrapに横スクロールヒントの表示/消去を仕込む(冪等: data-mg-initで二重登録を防ぐ)。
 * (C05) 前回は{once:true}で初回スクロールしたら二度と出なかったが、右端まで見た後スクロールを
 * 左端(scrollLeft<=2px)まで戻したときは「まだ他の列がある」ことを再度知らせたいため、
 * スクロール位置に応じて毎回表示/非表示を切り替える。 */
// タブ切替のたびに.mg-wrapはinnerHTML置換で新しいDOMノードになる。ノードごとにwindowへ
// resizeリスナーを足すと、古いノードは破棄されてもリスナーだけ残り続けて溜まる。
// 生きている.mg-wrapだけを都度再チェックする1本のリスナーに集約する。
let resizeBound = false;
function checkWrap(wrap: HTMLElement): void {
  const mg = wrap.querySelector<HTMLElement>('.mg');
  if (!mg) return;
  if (mg.scrollWidth <= mg.clientWidth + 2) { wrap.classList.add('mg-scrolled'); return; }
  wrap.classList.toggle('mg-scrolled', mg.scrollLeft > 2);
}

export function initMgHints(root: ParentNode = document): void {
  root.querySelectorAll<HTMLElement>('.mg-wrap:not([data-mg-init])').forEach((wrap) => {
    wrap.setAttribute('data-mg-init', '1');
    const mg = wrap.querySelector<HTMLElement>('.mg');
    if (!mg) return;
    checkWrap(wrap);
    mg.addEventListener('scroll', () => checkWrap(wrap), { passive: true });
  });
  if (!resizeBound) {
    resizeBound = true;
    window.addEventListener('resize', () => {
      document.querySelectorAll<HTMLElement>('.mg-wrap').forEach(checkWrap);
    });
  }
}
