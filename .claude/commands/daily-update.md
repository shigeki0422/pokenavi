# 毎日更新スキル

ポケモンチャンピオンズの使用率データを最新クロール結果に更新する。
**ページ生成後はlocalhost確認→ユーザー承認→デプロイの順に進める。いきなり本番コミットしない。**

## 手順

### 1. DBの最新クロール日を確認
```bash
cd /Users/shigeki/work/pokenavi && python3 -c "
import sqlite3
conn = sqlite3.connect('scripts/pokenavi.db')
rows = conn.execute(\"SELECT crawled_date, COUNT(*) FROM pokemon_usage WHERE season='M-3' AND rule='single' GROUP BY crawled_date ORDER BY crawled_date\").fetchall()
for r in rows: print(r)
"
```

### 2. EVデータの事前チェック（32超過がある場合はDB修正してから進む）
```bash
sqlite3 scripts/pokenavi.db "SELECT MAX(ev_h), MAX(ev_a), MAX(ev_b), MAX(ev_c), MAX(ev_d), MAX(ev_s) FROM pokemon_evs WHERE season='M-3' AND rule='single' AND crawled_date=(SELECT MAX(crawled_date) FROM pokemon_evs WHERE season='M-3' AND rule='single');"
```

### 3. ranking.json を再生成
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
pokemon_list = sorted(pokemon_map.values(), key=lambda p: p['dates'].get(latest, {}).get('rank', 9999))
pokemon_list = [p for p in pokemon_list if p['dates'].get(latest, {}).get('rank', 9999) <= 200]
with open('src/data/ranking.json', 'w', encoding='utf-8') as f:
    json.dump({'dates': dates, 'pokemon': pokemon_list}, f, ensure_ascii=False, indent=2)
print(f'Done: {len(pokemon_list)} pokemon, dates={dates}')
"
```

### 4. 全ポケモン情報ページを再生成
```bash
python3 scripts/generate_pokemon_pages.py
```

### 5. localhost で確認（ユーザーが確認・承認するまで待機）
```bash
npm run dev
```
→ ユーザーが http://localhost:4321 で確認し「問題なし」と言ったら次へ進む

### 6. ビルド
```bash
npm run build
```

### 7. コミット＆デプロイ（ユーザーの承認後のみ実行）
```bash
git add src/data/ranking.json src/content/pokemon/ && \
git commit -m "feat: $(date +%m/%d)クロールデータ反映（使用率ランキング・ポケモン情報ページ更新）" && \
git push origin main && \
npx wrangler pages deploy dist --project-name pokenavi --branch main
```

## 注意事項

- 新ポケモンが登場した場合は `scripts/generate_pokemon_pages.py` の `POKEMON_DATA` に追加が必要
- pokemon_idが`None`や誤りの場合はDB修正が必要（地域・フォルム違いに注意）
- 新しいクロール日のデータに重複行がないか事前確認推奨
- **EVは32スケール上限**（チャンピオンズ仕様）。手順2のチェックで32超があればDB修正してから再生成する
- **localhost確認前に本番コミット・デプロイしない**。ユーザーが確認・承認してから手順7を実行する
