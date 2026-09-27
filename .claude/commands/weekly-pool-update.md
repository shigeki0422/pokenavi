# 週次の型プール更新（想定型・1v1の型）

最新の使用率で型プール → 系統表を作り直し、ポケモン情報ページの「想定型」（src/data/archetypes.json）と 1v1 の代表型・仮想敵（public/builder-data の mon/*.json の mu・targets.json）を**同じ版から同時に**作る。Set N の系統番号（archNo）を想定型と 1v1 で揃えるため、片方だけ更新しない。
AI・提案API・共進化・datapack が使うシーズン固定版（scripts/pool_versions.json の season）はここでは変えない。
**生成後は localhost 確認 → ユーザー承認 → コミットの順。いきなり本番コミットしない。**

いつ: 詳細データ（技・持ち物・性格・努力値・特性）のクロール後（週1回）。新シーズン開始時。`node scripts/check_archetypes.mjs`（prebuild でも出る）が抜けを警告したとき。

## 手順

### 1. 実行（1コマンド）
```bash
cd /Users/shigeki/work/pokenavi && scripts/venv/bin/python scripts/update_type_pool.py
```
- シーズンは `POOL_SEASON`（無ければ DB の最新シーズン）。版は `<シーズン>/<今日>`（`VERSION=M-6/2026-09-27b` で別名）。同じ版が既にあれば止まる（上書きしない）
- 出力: `_local/ai_work/pools/<シーズン>/<日付>/` に `type_pool.json`・`type_groups.json`・`meta.json`（使用率の日・生成パラメータ・生成器の git ハッシュ・所要時間）・`report.md`（差分とチェック）
- 流れ: 型プール（並列 `JOBS`）→ 系統表 → チェック（プール・系統表）→ `scripts/pool_versions.json` の page を新しい版へ → `gen_builder_data.py` → `gen_archetype_data.py` → チェック（出力の整合）
- エラーがあれば終了コード1で止まる。プール・系統表のエラーならポインタも生成物も変えない。出力の整合のエラーならポインタを戻して生成物を作り直す
- 所要時間の目安: 約3分（2026-09-27 初回 160秒・12並列。型プール131s・前シーズン10s・系統2s・チェック各数秒・gen_* 数秒。内訳は meta.json の seconds）

### 2. レポートを読む（`report.md`）
- エラー（止まる）: 生成ルール（覚えない技・没収技、ジュエルと同タイプの攻撃技、こだわり×積み/守る/回復、EV 各≤32・合計≤66、性格、メガ石、PRUNE_W 未満の型（生成器が最後に落とす）、重みの合計）、命名・系統分け（〜型、名前の技は系統内85%以上（積み技は20%）、積み技が名前に入る、フルアタ型の条件、バトンは単独の系統、単一の型、系統≤6、5%未満の統合は同じ持ち物の区分の中だけ、同名の系統なし、＋物理技/特殊技の付け方）、出力の整合（archNo/archSub/割合が想定型と 1v1 で一致、分割ラベルの括弧で名前の語を繰り返さない、版の記録）
- 警告（止まらない）: 前の版との変化（系統数・系統の割合≥10pt・系統の消滅/新規・プールの採用率≥10pt・上位持ち物の入れ替わり・技の組の KL≥0.1。**DB の使用率の変化が3pt未満なのにプールが動いたものは「生成側の疑い」**）、DB の使用率との差（技10pt（上位10を4枠へ伸ばした目標と比べる）・持ち物5・性格5・努力値10・特性15）、こだわり×変化技2本以上が5%超、監査（_audit_type_pool）の違反率0.5%以上、ランキングの網羅、最新シーズン以外のデータの種
- 閾値は `scripts/pool_checks.py` の先頭の定数。規則は生成側（_gen_type_pool・arch_groups）の関数を import して判定している
- 「生成側の疑い」「系統名が変わった種」は数件を実データ（DB の使用率）と見比べてから進む

### 3. localhost で確認（ユーザーが確認・承認するまで待機）
```bash
npm run dev
```
- 増えた種・系統名が変わった種のページ（ja/en/ko）で想定型と 1v1 の相性表の Set N が合っていること
- en/ko の型名漏れはビルド後に `DIST=<dist> scripts/venv/bin/python scripts/pool_checks.py <前の版> <新しい版>` で確認できる

### 4. コミット（ユーザーの承認後のみ）
`src/data/archetypes.json`・`public/builder-data/`・`scripts/pool_versions.json` を一緒にコミットする（`_local` の版の実体は gitignore。ビルドに要るのは生成物だけ）。

## 戻すとき
`scripts/pool_versions.json` の page を前の版にして `scripts/venv/bin/python scripts/gen_builder_data.py && scripts/venv/bin/python scripts/gen_archetype_data.py`。版は消さずに残っている。

## シーズン固定版（season ポインタ）の切り替え
AI・提案API・共進化・datapack は `season` の版（今は `M-6/v41` = `_local/ai_work/frozen/`）。新シーズン開始時か環境が大きく変わったときだけ、週次の版を候補にして A/B（勝率・較正・fresh_parity/belief_parity）で確認してから `season` を切り替える。切り替えたら datapack_export・wasm・Cloud Run の再デプロイが要る（.claude/rules/party-builder.md）。
