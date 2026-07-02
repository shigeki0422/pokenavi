# クロール簡易版

ポケモンチャンピオンズのランキングのみ取得してDBに保存・ローカル反映する。
詳細データ（技/持ち物/特性/性格/EV）は取得しない。

**デバイス（Champions起動・ランキング画面）をUSB接続した状態で実行すること。**

## 手順

### 1. デバイス接続確認
```bash
adb devices
```
→ deviceが1件以上あることを確認。なければ中断。

### 2. ADBキャプチャ
```bash
cd /Users/shigeki/work/pokenavi && python3 scripts/crawl_champions.py
```
200位まで自動撮影（約3時間）。完了まで待機。

### 3. クロップ
```bash
python3 scripts/crop_panels.py /tmp/champ_crawl_$(date +%Y-%m-%d)
```

### 4. insert_ranking_from_icons.py の日付設定
`scripts/insert_ranking_from_icons.py` の以下2箇所を今日の日付に更新する：
- `TARGETS` dict に `"YYYY-MM-DD": {}` を追加
- `CRAWLED_DATE = "YYYY-MM-DD"` を更新

### 5. アイコンマッチング → DB投入
```bash
python3 scripts/insert_ranking_from_icons.py
```
重複が出た場合は該当ランクの画像を確認して `TARGETS["YYYY-MM-DD"]` にオーバーライドを追記し再実行。

### 6. ranking.json 再生成
```bash
python3 -c "
import sqlite3, json
conn = sqlite3.connect('scripts/pokenavi.db')
conn.row_factory = sqlite3.Row
SEASON, RULE = 'M-3', 'single'
dates = [r[0] for r in conn.execute(f\"SELECT DISTINCT crawled_date FROM pokemon_usage WHERE season='{SEASON}' AND rule='{RULE}' ORDER BY crawled_date\").fetchall()]
all_rows = conn.execute(f\"SELECT pokemon, rank, crawled_date, pokemon_id FROM pokemon_usage WHERE season='{SEASON}' AND rule='{RULE}' ORDER BY crawled_date, rank\").fetchall()
pokemon_map = {}
for row in all_rows:
    name = row['pokemon']
    if name not in pokemon_map:
        pokemon_map[name] = {'name': name, 'id': row['pokemon_id'], 'dates': {}}
    pokemon_map[name]['dates'][row['crawled_date']] = {'rank': row['rank'], 'rate': None}
latest = dates[-1]
# 過去に200位以内に入ったことがあるポケモンを対象に（最新日ランク外も含める）
pokemon_list = [p for p in pokemon_map.values() if any(d.get('rank', 9999) <= 200 for d in p['dates'].values())]
pokemon_list.sort(key=lambda p: p['dates'].get(latest, {}).get('rank', 9999))
with open('src/data/ranking.json', 'w', encoding='utf-8') as f:
    json.dump({'dates': dates, 'pokemon': pokemon_list}, f, ensure_ascii=False, indent=2)
print(f'Done: {len(pokemon_list)} pokemon, latest={latest}')
"
```

### 7. ポケモンページ再生成
```bash
python3 scripts/generate_pokemon_pages.py
python3 scripts/inject_faq_frontmatter.py
```

### 8. ローカル確認
```bash
npm run dev
```
→ http://localhost:4321 でランキングが正しく反映されているか確認してもらい「パブリッシュ」を待つ。
デプロイはユーザーが `git push origin main` で実施。

## 注意事項
- `/tmp/champ_crawl_*` は絶対に削除しない（過去分の画像マッチング遡及確認のため）
- アイコンマッチング重複時は必ず画像を目視確認してから RANK_OVERRIDES に追記する
- デプロイは `git push origin main` のみ（wrangler pages deploy は不要）
