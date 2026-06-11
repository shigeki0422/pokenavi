"""
GameWith ポケモンチャンピオンズ 上位構築クローラー
https://gamewith.jp/pokemon-champions/560474
1ページ(50件)×2ページ = 100件取得
"""
import json
import time
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://gamewith.jp/pokemon-champions/560474"
OUT = Path(__file__).parent / "gamewith_parties.json"

STAT_LABEL_MAP = {"HP": "H", "攻撃": "A", "防御": "B", "特攻": "C", "特防": "D", "素早": "S"}


def extract_structures(page) -> list[dict]:
    return page.evaluate("""() => {
        const results = [];
        document.querySelectorAll('.w-structure').forEach(s => {
            const rank    = s.querySelector('._rank > div:last-child')?.textContent.trim() ?? '';
            const mode    = s.querySelector('._battle-mode')?.textContent.trim() ?? '';
            const season  = s.querySelector('._season')?.textContent.trim() ?? '';
            const trainer = s.querySelector('._user-name-text')?.textContent.trim() ?? '';
            const point   = s.querySelector('._point')?.textContent.trim() ?? '';

            // ポケモン名リスト（w-pokemon-list 内）
            const nameEls = Array.from(s.querySelectorAll('.w-pokemon-list .w-pokemon ._name'));
            const names = nameEls.map(el => el.innerText.replace(/\\n/g, '').trim());

            // 詳細パネルリスト（_pokemon-details 内）
            const details = Array.from(s.querySelectorAll('._pokemon-details .w-pokemon-detail'));

            const pokemons = names.map((name, i) => {
                const detail = details[i];
                if (!detail) return { name };

                const metas = {};
                detail.querySelectorAll('._meta-row').forEach(row => {
                    const label = row.querySelector('._meta-label')?.textContent.replace(':', '').trim() ?? '';
                    const value = row.querySelector('._meta-value')?.textContent.trim() ?? '';
                    metas[label] = value;
                });

                const moves = Array.from(detail.querySelectorAll('._move-name')).map(m => m.textContent.trim());
                const nature = detail.querySelector('._nature-value')?.textContent.trim() ?? '';

                const evOrder = ['HP', '攻撃', '防御', '特攻', '特防', '素早'];
                const evs = {};
                detail.querySelectorAll('._stat-cell').forEach(cell => {
                    const lbl = cell.querySelector('._label')?.textContent.trim() ?? '';
                    const ev  = cell.querySelector('._ev')?.textContent.replace(/[()]/g, '').trim() ?? '0';
                    evs[lbl] = parseInt(ev, 10);
                });
                const evStr = evOrder.map(l => evs[l] ?? 0).join('/');

                return {
                    name,
                    item:    metas['もちもの'] ?? '',
                    ability: metas['とくせい'] ?? '',
                    moves,
                    nature,
                    ev: evStr
                };
            });

            results.push({ rank, mode, season, trainer, point, pokemons });
        });
        return results;
    }""")


def crawl_page(page, page_num: int) -> list[dict]:
    if page_num > 1:
        # ページボタンをクリック（上部のページネーションの該当番号）
        btns = page.query_selector_all('.w-page')
        target = None
        for btn in btns:
            if btn.inner_text().strip() == str(page_num):
                target = btn
                break
        if target:
            target.click()
            time.sleep(3)

    structures = extract_structures(page)
    print(f"  ページ{page_num}: {len(structures)}件取得")
    return structures


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"ロード中: {URL}")
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        time.sleep(8)

        all_data = []
        for pg in [1, 2]:
            data = crawl_page(page, pg)
            all_data.extend(data)
            time.sleep(2)

        browser.close()

    OUT.write_text(json.dumps(all_data, ensure_ascii=False, indent=2))
    print(f"\n合計 {len(all_data)} 件 → {OUT}")

    # サンプル表示
    if all_data:
        s = all_data[0]
        print(f"\n--- サンプル: {s['rank']} {s['trainer']} ---")
        for pk in s['pokemons']:
            print(f"  {pk.get('name')}@{pk.get('item')} 性格={pk.get('nature')} "
                  f"特性={pk.get('ability')} EV={pk.get('ev')}")
            print(f"    技={pk.get('moves')}")


if __name__ == "__main__":
    main()
