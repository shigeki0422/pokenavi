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

### 2. ADBキャプチャ（画面オフからそのまま実行できる）
```bash
cd /Users/shigeki/work/pokenavi && LAUNCH=1 PANELS=move SKIP_TOP=1 python3 scripts/crawl_champions.py
```
`LAUNCH=1` が画面オン → 前日のアプリを終了 → 起動 → START → お知らせを閉じる（出ていれば）→
バトル → バトルデータ → ランクバトル → ポケモンタブ、までを自動でやる（2026-10-17 に実機で確定）。
**端末のロックが無効になっていることが前提**。お知らせはその日の最初の起動でしか出ないので、
画面を見て出ているときだけ閉じる（出ていないのに押すとホーム画面の別の場所を叩くため）。

手でランキング画面を開いてから実行するときは `LAUNCH=1` を外す。

完走すると画面を消す（`LAUNCH=1` のときだけ。手で開いて実行したときは操作中かもしれないので消さない）。
異常終了したときは画面を残すので、止まった状態をそのまま確認できる。
200位まで自動撮影。**`PANELS=move` を必ず付ける**（1体7〜9秒・200体で約30分）。

順位の判定に使うのは `move_00.png` のヘッダーのアイコンだけ（`insert_ranking_from_icons.py`）で、
残り5パネル（item/partner/nature/ev/ability）は詳細OCR専用。付け忘れると6パネル撮って
1体52秒・**約3時間**かかる（フルクロールと同じ所要時間になる）。

**`SKIP_TOP=1` は「1位が見えている」ときだけ付ける**（アプリを起動してランキング画面まで辿ってきた直後は必ずそうなる）。
付けると140回スワイプして先頭へ戻す工程（実測2分17秒）を省ける。どこまでスクロールしたか分からない状態で
付けると途中の順位から撮り始めてしまうので、その場合は付けずに実行する。先頭確認（1位との一致率）は
どちらでも走るので、ずれていれば止まる。

**途中で止めたら、再開前に端末をランキング一覧の先頭（1位が見える状態）に戻すこと。**
詳細画面のまま再開すると `scroll_to_top()` が戻り切れず「❌ 先頭に戻れていない」で終了する。
再開は `last_rank.txt` の次の順位から自動で続く。

### 3. クロップ
```bash
python3 scripts/crop_panels.py crawl_data/champ_crawl_$(date +%Y-%m-%d)
```
保存先は `crawl_data/`（`/tmp` は再起動で消えるため 2026-09-12 に移動済み。`crawl_champions.py` の
`OUTPUT_DIR` が正本）。

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
python3 scripts/generate_ranking_json.py
```

### 7. ポケモンページ再生成
```bash
python3 scripts/generate_pokemon_pages.py
python3 scripts/gen_builder_data.py   # パーティ工房のデータ(選択できるポケモン/型/仮想敵)を最新シーズンで再生成。scripts/builder_targets.json と提案キャッシュの一覧の記号(scripts/suggest_cache.json、_refresh_panel.py MATCHUP_ONLY=1)も続けて作り直す
python3 scripts/gen_learnset_data.py  # ポケモン情報ページ「覚える技」用データ(gen_builder_data.py の後に実行)
python3 scripts/inject_faq_frontmatter.py
```
- 想定型・1v1の型（型プール）はここでは作り直さない（詳細データの週次クロール `/crawl-full` の手順 7-2 で更新）。gen_builder_data.py は `scripts/pool_versions.json` の版を読むので、毎日流しても想定型と番号はずれない
- `gen_builder_data.py` を流したら、`public/builder-data/`・`scripts/builder_targets.json`・`scripts/suggest_cache.json` を**必ず一緒にコミット**する（2026-10-16〜19 は targets.json だけコミットされ、簡単構築の一覧の記号が古い相手のまま残った。test_all 46 が検出する）。コミット前に `cd scripts && PYTHONHASHSEED=0 venv/bin/python tests/test_all.py`（約3分）で 46（一覧の相手・記号の鮮度）を含む全件パスを確認し、コミット後に `git status --short public/builder-data scripts/builder_targets.json scripts/suggest_cache.json` が空であることを確認。suggest_cache.json が変わったら Cloud Run（pokenavi-suggest）の再デプロイが要るのでユーザーに伝える
- ビルド前の `[archetypes]` 警告（ランキングに新しく入った種に想定型が無い等）が出たら、ユーザーに伝えて次の詳細クロールで更新する

### 8. ローカル確認
```bash
npm run dev
```
→ http://localhost:4321 でランキングが正しく反映されているか確認してもらい「パブリッシュ」を待つ。
デプロイはユーザーが `git push origin main` で実施。

## 注意事項
- `crawl_data/champ_crawl_*` は絶対に削除しない（destructive_guard.py が拒否する）（過去分の画像マッチング遡及確認のため）
- アイコンマッチング重複時は必ず画像を目視確認してから RANK_OVERRIDES に追記する
- デプロイは `git push origin main` のみ（wrangler pages deploy は不要）
