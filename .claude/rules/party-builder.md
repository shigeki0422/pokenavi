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
  - "scripts/rust_engine/engine/src/analysis.rs"
---

# パーティ構築・1v1判定・想定型の設計（2026-09-27 時点）

エンジンの仕様の正本は `scripts/simulator/REQUIREMENTS.md`（4-0-1 = 1v1判定、5-10 = 代表型）。ここは全体の構成と、ユーザーが決めた表示・判定の規則をまとめる。

## データの流れ

```
型生成器 scripts/_gen_type_pool.py
  → 型プール（固定版）_local/ai_work/frozen/type_pool_M-6_v41.json（読み取り専用）
  → 系統表 _local/ai_work/scripts/arch_view_data.py → frozen/type_groups_M-6_v41.json
      ├ scripts/gen_builder_data.py   → public/builder-data/（mon/*.json の mu = 代表型≤3、targets.json = 仮想敵）
      └ scripts/gen_archetype_data.py → src/data/archetypes.json（情報ページの想定型）
1v1エンジン Rust analysis.rs
  ├ wasm → public/engine/engine_wasm.wasm（＋ public/builder-data/engine.pack.json）… サイト（静的ページのビルド時・工房のブラウザ実行）
  └ pyengine → Cloud Run pokenavi-suggest（簡単構築の提案API。エンジンを変えたら再デプロイが要る。gcloud はユーザーが実行）
```

- `_local/` は gitignore。系統表と arch_view_data.py はリポジトリだけでは再生成できない。
- 系統表・型プールを作り直したら、gen_builder_data.py と gen_archetype_data.py を両方流す。

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
- 「倒されなかったら何ターンで倒せたか」は、倒れた側に「倒れても行動し続ける」印（`Poke.undying`）を付けて実HPのまま続きを回す（HPの水増しはしない）。
- へんげんじざい/リベロのタイプ変化は経過（棒・再生）にだけ反映し、技ごとのダメージ一覧は元のタイプで出す。
- 速度の目安: 1対面 0.47ms 以内（`scripts/tests/dump_all_matchups.ts` 系のベンチ）。判定を変えたら全対面ダンプで記号の変化を一覧にして確認する。

## 表示（src/scripts/party-builder/）
- `mu-card.ts`: 1v1カードの共有レンダラ（情報ページのポップアップ・工房・対策ページで同じもの）。棒は時系列でターン帯（T1, T2…）、後攻は小さな印、原因ごとの色分け、左に「その棒のHPの持ち主」のアイコン。タップで詳細「60〜72 (35〜42%)　※本シミュでは中央の66 (39%)で計算」。
- `mu-replay.ts`: 対戦再生（1ターンずつ・特性発動/メガシンカ/とどめは技そのもののダメージ）。操作やくわしい内訳を開いたときは画面内に収まるようスクロール。
- 情報ページ: `MatchupSection.astro`（相性表は自分の代表型の割合で重み付けした判定。自分の型の切替は置かない）＋ `MatchupBreakdownPopup.astro`（判定結果を `<template class="mbp-data">` のJSONで埋め込み、開いたときにクライアント描画。ポップアップ内で自分/相手の型をタブ切替）。`BuildArchetypeSection.astro` が想定型。
- 工房 `PartyBuilderApp.astro`: 仮想敵の前提（天候・フィールド・自分/相手の積み）はそのカードとEV逆算にだけ使い、相性表・穴の計算には反映しない。

## 既知の残課題
- 翻訳辞書に無いもの: Champions 独自の特性（はどうのぼうご・うなぎのぼり・ほのおのたてがみ）、フォーム名7件。
- 情報ページのHTMLは以前の約1.8倍（ポップアップのデータ埋め込み）。戻すならポップアップを開いたときにJSONを取得する方式へ。
- バチンウニは同名の系統が2つある（系統表側の問題）。
- ゲート R3-fb / R3-sel / R4 は記録が古く採り直せない（生成スクリプトが無い）。一致確認は fresh_parity / belief_parity で行う。
