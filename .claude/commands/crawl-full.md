# クロール詳細版

ポケモンチャンピオンズの全データを取得してDBに保存・ローカル反映する。
ランキングに加えて同居率（画像マッチング）＋技/持ち物/特性/性格/EV（OCR）を取得する。

**デバイス（Champions起動・ランキング画面）をUSB接続した状態で実行すること。**

## 手順

### 1. デバイス接続確認
```bash
adb devices
```
→ deviceが1件以上あることを確認。なければ中断。

### 2. ADBキャプチャ（簡易版と共通）
```bash
cd /Users/shigeki/work/pokenavi && python3 scripts/crawl_champions.py
```
200位まで自動撮影（約3時間）。完了まで待機。

### 3. クロップ（簡易版と共通）
```bash
python3 scripts/crop_panels.py /tmp/champ_crawl_$(date +%Y-%m-%d)
```

### 4. ランキング取り込み（簡易版と同じ手順4〜5を実施）
`scripts/insert_ranking_from_icons.py` の日付を更新してから：
```bash
python3 scripts/insert_ranking_from_icons.py
```

### 5. OCRワークフロー実行
`scripts/ocr_workflow_template.js` の `CRAWL_DATE` と `TOTAL_RANKS` を設定し、
Workflow ツールに貼り付けて実行（haiku モデルで200件並列OCR）。

### 6. 同居ポケモン（パートナー）の画像マッチング → DB投入
OCRワークフローが返した `partners` リストのアイコン画像（`_c_partner_*.png`）に対して
`insert_detail_from_journal.py` 内の `resolve_partner_form()` がコサイン類似度マッチングを行い
フォーム識別（キュウコン/アローラキュウコン、ロトム系等）付きで `pokemon_partners` テーブルに投入する。
技/持ち物/特性/性格/EVも同じスクリプトで一括投入される。

```bash
python3 scripts/insert_detail_from_journal.py
```
- `⚠ パートナー不一致` が出た場合はアイコン画像を確認して `OCR_POKEMON` に補正を追記
- EVが32超・無効性格名はスキップログで確認
- 性格は VALID_NATURES ゲートで自動フィルタ（25種以外はDB投入されない）

### 7. ページ再生成
```bash
python3 scripts/generate_pokemon_pages.py
python3 scripts/inject_faq_frontmatter.py
```

### 8. ローカル確認
```bash
npm run dev
```
→ http://localhost:4321 でランキング・詳細データが正しく反映されているか確認してもらい「パブリッシュ」を待つ。
デプロイはユーザーが `git push origin main` で実施。

## 注意事項
- `/tmp/champ_crawl_*` は絶対に削除しない
- 同居ポケモンのフォーム識別はパートナー画像のアイコンマッチングで自動判別（キュウコン/アローラキュウコン、ロトム系等）
- OCR誤読性格は `insert_detail_from_journal.py` の `OCR_NATURES` で自動補正
- DB投入後に `[SKIP_NATURE]` ログが多い場合は新しい誤読パターンなので `OCR_NATURES` に追記する
- デプロイは `git push origin main` のみ
