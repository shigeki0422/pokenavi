---
paths:
  - "src/scripts/party-builder/**"
  - "src/components/PartyBuilderApp.astro"
  - "src/components/PartySuggestApp.astro"
  - "src/components/MatchupSection.astro"
  - "src/components/MatchupBreakdownPopup.astro"
  - "src/components/BuildArchetypeSection.astro"
  - "scripts/gen_builder_data.py"
  - "scripts/gen_archetype_data.py"
  - "scripts/arch_groups.py"
  - "scripts/update_type_pool.py"
  - "scripts/pool_checks.py"
  - "scripts/pool_versions.py"
  - "scripts/pool_versions.json"
  - "scripts/rust_engine/engine/src/analysis.rs"
---

# パーティ構築・1v1判定・想定型の設計（2026-09-27 時点・2026-10-08 型の出どころと努力値を追記）

エンジンの仕様の正本は `scripts/simulator/REQUIREMENTS.md`（4-0-1 = 1v1判定、5-10 = 代表型）。ここは全体の構成と、ユーザーが決めた表示・判定の規則をまとめる。

## データの流れ

```
使用率DB scripts/pokenavi.db
  → 型生成器 scripts/_gen_type_pool.py（generate_one）
  → 系統表 scripts/arch_groups.py（系統分け・命名。確認ページ _local/ai_work/scripts/arch_view_data.py もこれを import）
  → 版 _local/ai_work/pools/<シーズン>/<日付>/ type_pool.json・type_groups.json・meta.json・report.md（積み上げ。上書きしない）
     ポインタ scripts/pool_versions.json（コミットする）
       page   … 情報ページ用。週次で更新 → gen_builder_data.py（public/builder-data: mon/*.json の mu・targets.json・version.json）
                                         → gen_archetype_data.py（src/data/archetypes.json。"_version" に版）
       season … シーズン固定版（今は M-6/v41 = _local/ai_work/frozen/*_M-6_v41.json・読み取り専用）
                 → datapack_export.py（AI）・gen_party_pool.PartyGen（簡単構築の提案・補完 _product3_complete・提案キャッシュ）
                   ・_coevo_groups.py（生成集団・共進化）・_repop_builds.py・_audit_*.py
  努力値 … どの経路も scripts/ev_fill.py で合計66に揃えてから使う（生成器の出力・型プール/系統表の読み込み・工房の候補）
1v1エンジン Rust analysis.rs
  ├ wasm → public/engine/engine_wasm.wasm（＋ public/builder-data/engine.pack.json）… サイト（静的ページのビルド時・工房のブラウザ実行）
  └ pyengine → Cloud Run pokenavi-suggest（簡単構築の提案API。エンジンを変えたら再デプロイが要る。gcloud はユーザーが実行）
```

- **型の出どころは型プール（版指定）に一本化**（2026-10-08）: 提案・生成集団・工房・情報ページ・AI はすべて同じ型プールの版を使う（提案・生成集団・AI＝season、工房・情報ページ＝page）。提案（`PartyGen`）は手元に版が無ければ datapack の `build_pool`（Cloud Run。同じ season の版）を読む。`build_pool_<シーズン>.md`（手作りのドラフト型）は型プールの無い過去シーズン（M-3 等）専用（`gen_build_pool.py`・`gen_party_ga.py`・`_append_m4_builds.py` も過去シーズン用。`_gen_type_pool.md_builds` の M-4 上位構築 md は系統の事前分布で、型の出どころではない）。`pool_checks.py` が「型の出どころ」と「努力値の合計≠66」をエラーにする。
- 努力値は合計66（各≤32）。余りはその種の DB（そのシーズンの最新日）で余りが最も多く置かれている能力へ（同じ大きな振り先の配分を優先・データが無ければ H→B→D→S→A→C）。`ev_fill.py`。
- `gen_builder_data.py` はシーズンを DB の最新シーズンから自動で決めるので、新シーズンの使用率だけ入って詳細（技・努力値）がまだの日（例 M-7 の 2026-10-07）は page の版と食い違う。その間は `BUILDER_SEASON=<page のシーズン>` で流す。
- 週次の更新は1コマンド `scripts/venv/bin/python scripts/update_type_pool.py`（手順 `.claude/commands/weekly-pool-update.md`）。型プール → 系統表 → チェック → page ポインタ → gen_builder_data.py → gen_archetype_data.py → チェック。**想定型と 1v1 は必ず同じ版から同時に作る**（Set N の archNo を揃える。片方だけ流さない。gen_builder_data.py を毎日流すのは同じ page の版を読むので可）。
- 版の解決は `scripts/pool_versions.py`（pools/<版>/ に無ければ frozen/<name>_<シーズン>_<タグ>.json）。env で上書き: `POOL_VERSION`/`GROUPS`（想定型）、`BUILDER_POOL_VERSION`/`BUILDER_POOL_GROUPS`（1v1）、`BUILD_POOL`（datapack）、`TYPES`（監査）。
- 型プールの対象はシーズン中に使用率に出た全種。詳細（技・持ち物…）の日に圏外だった種はその種の最新の詳細の日、シーズン中の詳細が無い種は前のシーズン（archetypes の season に出る）、技が4つ未満の種（メタモン）は周辺分布の積で作る。
- `_local/` は gitignore。ビルドに要る生成物（archetypes.json・public/builder-data）と pool_versions.json をコミットすれば Cloudflare のビルドは通る。prebuild の `scripts/check_archetypes.mjs` がランキング最新シーズンの抜け・シーズン違い・版のずれを警告する（ビルドは止めない）。
- シーズン固定版（season）の切り替え: 新シーズン開始か環境の大変化のときだけ。週次の版を候補に A/B（勝率・較正・fresh_parity/belief_parity）で確認してから切り替え、datapack・wasm・Cloud Run を作り直す。

## 週次のチェック（scripts/pool_checks.py。update_type_pool.py が自動で流す）
- エラー（終了コード1で止める）: 生成ルール（覚えない技・没収技、ジュエルと同タイプの攻撃技、こだわり×積み/守る/回復＝item_ok、EV 各≤32・合計＝66、性格、他種のメガ石、PRUNE_W 未満の型（生成器が最後に落とす）、重みの合計）／命名・系統分け（下の規則）／出力の整合（archNo・archSub・割合が想定型と 1v1 で一致、分割ラベル、版の記録。`DIST=` で en/ko の型名漏れ）／努力値の合計≠66（想定型・1v1・工房の型プリセット・努力値の候補）／型の出どころ（提案の型が season の版にあり合計66・生成集団の系統表が season の版・1v1 の型が page の版にある）。
- 警告（report.md に一覧）: 前の版との変化（系統の割合≥10pt・系統の消滅/新規・プールの採用率≥10pt・上位持ち物の入れ替わり・技の組の KL≥0.1。DB の変化<3pt なのにプールが動いたら「生成側の疑い」）、DB の使用率との差（技10pt（上位10を4枠へ伸ばした目標）・持ち物5・性格5・努力値10・特性15）、こだわり×変化技2本以上>5%、監査の違反率≥0.5%、ランキングの網羅。
- 閾値は pool_checks.py の先頭の定数。規則は生成側の関数・定数（_gen_type_pool.item_ok/learnset/PRUNE_W、arch_groups.CORE/MAX_GROUPS/GIMMICK/full_attack）を import して判定する（二重に書かない）。検出のテストは test_all.py の 33。

## 型（系統）の規則
- 名前は機能で付ける（区別できる技≥85%・積み技は必ず名前に入れる・フルアタ型・バトンは単独の系統・1系統だけの種は「単一の型」）。末尾は必ず「〜型」（`arch_name()`）。
- 系統は ≤6、5%未満は同じ持ち物クラス内でだけ統合（持ち物クラスをまたいだ統合は禁止）。
- 1v1の代表型: 割合≥10%（`MIN_ARCH_SHARE`）の系統の上位3。3つ未満なら最大の系統を技の組→技×持ち物で分割（分割片も≥10%）。分割片の重みの合計＝元の系統の割合。並びは割合の降順。分割ラベルは「〜型（技）」（名前に含まれる語は括弧内で繰り返さない）。
- 相手の技は代表型の4技に限る（`mpool`）。
- 外国語版（en/ko）は型名を出さず「Set N / 샘플 N」。番号は想定型セクションの系統番号（`archNo`）、分割は「Set 1a/1b」（`archSub`）。
- EV は最大32、表記は H/A/B/C/D/S。

## 1v1判定（エンジン側の要点）
- 両者が同時に動く対戦シミュ。方針（最大打点・毎ターン最善・準備1手（積み・ねこだまし）・持久戦）を総当たりし、ミニマックスで選ぶ。交代なし・命中は必中。
- 判定は中央乱数の1点だけ（最低・最高乱数の計算と「乱数次第」表示は削除済み。戻さない）。技ごとのダメージは最低〜最高の幅で表示。
- 打ち切りは5ターン（持久戦は20）。PPを見ていないため、ユーザー判断で延ばさない。
- 相手を倒した行動の反動等で自分も倒れたら相打ち（引き分け）。同速は先後両方の平均。
- メガはメガ前の特性で入場 → 1ターン目の行動前に素早さ順でメガシンカ（ダブルいかく・天候の取り合い）。
- 無効（0倍）の技は撃つ手・最大打点技にしない（試合中に当たるようになればその時点から撃つ）。他の種のメガ石ではメガシンカしない（builder-data の持ち物からも外す）。REQUIREMENTS 4-0-1・2026-10-10。
- 表示側から渡す spec（2026-10-10）: 技は外さない（0倍の技も。外すと「0倍の技で接触を避ける」線が消える・へんげんじざい/へんしん/メガ後のスキンで当たる技まで外していた）。メガ石持ちの特性欄はメガ前の特性（targets.json・mon の mu は `ability`＝メガ前・`mab`＝メガ後。工房の特性の欄もメガ前を選べ、横に「→ メガ: 特性」）。表示用のメガ後の特性は `ResolvedBuild.megaAbility`（被弾倍率もこちら）。シーズンは渡さない（wasm.ts・`_explain.MU_GRID_SEASON` とも空文字）。
- 「倒されなかったら何ターンで倒せたか」は、倒れた側に「倒れても行動し続ける」印（`Poke.undying`）を付けて実HPのまま続きを回す（HPの水増しはしない）。
- へんげんじざい/リベロのタイプ変化は経過（棒・再生）にだけ反映し、技ごとのダメージ一覧は元のタイプで出す。
- 速度の目安: 1対面 0.47ms 以内（`scripts/tests/dump_all_matchups.ts` 系のベンチ）。判定を変えたら全対面ダンプで記号の変化を一覧にして確認する。

## 表示（src/scripts/party-builder/）
- `mu-card.ts`: 1v1カードの共有レンダラ（情報ページのポップアップ・工房・対策ページで同じもの）。棒は時系列でターン帯（T1, T2…）、後攻は小さな印、原因ごとの色分け、左に「その棒のHPの持ち主」のアイコン。タップで詳細「60〜72 (35〜42%)　※本シミュでは中央の66 (39%)で計算」。
- **1v1相性ダイアログは `mu-cell-popup.ts` の `openMuDialog`（ライブ計算：自分の型×相手の種の代表型 → wasm → 表示）／`renderMuDialog`（情報ページの埋め込みデータ）だけを使う**（工房・簡単構築・情報ページ・対戦アシスト）。ページ側で `renderMatchupTable`/`renderMuPopup`/`renderMuCard` を直接呼ばない（prebuild の `scripts/check_mu_dialog.mjs` が止める）。簡単構築の「ポケモン相性」の一覧（Cloud Run `_explain.matchup_grid`・提案キャッシュの matchup）もダイアログと同じ相手＝page の版の代表型（`scripts/builder_targets.json`＝gen_builder_data.py が targets.json と同時に書く写し。同じ列・順番・メガX/Y）と同じ集約（割合の重み付き平均・`*`＝型ごとの記号の最良≠最悪、`mu_agg`＝matchup.ts judgeVsBuildsMulti）。エンジンへの入力はどちらも spec をそのまま渡す（技を外さない・メガ石持ちの特性はメガ前・シーズン無し。どちらかを変えたら `_explain.py` も直す。test_all の 46 が wasm と全セル、47 が入力の規則を突き合わせる）。週次の update_type_pool.py が `_refresh_panel.py MATCHUP_ONLY=1` で一覧の記号と素早さタブも作り直す（Cloud Run の再デプロイが要る）。素早さタブの相手列・内訳（`/speed_detail`、X/Y は `lbl`）も同じ page の版の代表型。提案（パーティの中身）と採点・必然性リペアの穴判定（`_explain.load_top_builds`/`_opp_columns`）は season の版のまま。「攻撃相性」タブはタイプ相性の表（内訳 `/atk_detail`）。
- `mu-replay.ts`: 対戦再生（1ターンずつ・特性発動/メガシンカ/とどめは技そのもののダメージ）。操作やくわしい内訳を開いたときは画面内に収まるようスクロール。
- 情報ページ: `MatchupSection.astro`（相性表は自分の代表型の割合で重み付けした判定。自分の型の切替は置かない）＋ `MatchupBreakdownPopup.astro`（判定結果を `<template class="mbp-data">` のJSONで埋め込み、開いたときにクライアント描画。ポップアップ内で自分/相手の型をタブ切替）。`BuildArchetypeSection.astro` が想定型。
- 簡単構築 `PartySuggestApp.astro` の「選出ガイド」タブ（2026-10-02 相手集団の統計に変更）: タブを開いたときに `POST /guide {specs}` で1提案ずつ計算（`scripts/_select_guide.py`＋Rust `guide_rows`、約1.2秒・同じパーティはメモ）。相手＝使用率＋同居率の生成器で引いた M-6 の3000党（`scripts/guide_pool_m6.json`、`_guide_opps.py` が作る。シーズンを替えたら作り直す）。相手ごとに学習選出（先頭＝リード）と貪欲AI 8戦の勝率（MCTS@400 へ線形較正）を出し、集計だけを表示: 全体の有利度・よく選ぶ3匹・各ポケモンの選出率/先発率・「相手にこれがいたら入れる/外す」・苦手/得意な相手。少数の相手（旧版の10構築・旧々版 `_d1_guide.py` の8構築）は1対面ごとの揺れがそのまま出るので使わない。表示の基準（z≥6・差25pt／2.5pt）は独立な2集団で97〜98%再現する値（REQUIREMENTS 4-1j）。
- 工房 `PartyBuilderApp.astro`: 仮想敵の前提（天候・フィールド・自分/相手の積み）はそのカードとEV逆算にだけ使い、相性表・穴の計算には反映しない。

## 既知の残課題
- 翻訳辞書に無いもの: Champions 独自の特性（はどうのぼうご・うなぎのぼり・ほのおのたてがみ）、フォーム名7件。
- 情報ページのHTMLは以前の約1.8倍（ポップアップのデータ埋め込み）。戻すならポップアップを開いたときにJSONを取得する方式へ。
- 同名の系統（v41 のバチンウニ グランドコート×2・ガラルヤドラン フルアタ×2）は arch_groups.py で名前だけでまとめるよう直した（週次の版から。v41 の固定版には残る）。
- ranking.json の画像IDの誤り（generate_ranking_json.py の ALIASES）: カットロトム/スピンロトムが逆（ページは 0479-05 がカット）、アローラペルシアン・アローラライチュウが None。想定型の確認はページの名前→ID と species.json で引いているので影響しない。
- 系統の割合は1%未満の系統を落とすので合計が 99.4〜100%。
- ゲート R3-fb / R3-sel / R4 は記録が古く採り直せない（生成スクリプトが無い）。一致確認は fresh_parity / belief_parity で行う。
