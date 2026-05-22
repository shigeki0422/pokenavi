---
title: '【ポケモンチャンピオンズ】メガカイリュー徹底考察 M-2シーズン オリジナルメガの全て'
description: 'M-2シングルバトル使用率17位のメガカイリューを徹底分析。ひかえめCS型・特殊4色技・しんそく先制のメカニズムを解説し、ラムのみ型・耐久型・りゅうのまい型の3構築と相性パーティまで実データをもとに紹介します。'
pubDate: '2026-05-22'
draft: true
heroImage: '../../assets/hero-dragonite-m2.png'
---

<style>
.poke-header { display:flex; align-items:center; gap:16px; margin:20px 0; }
.poke-header img { width:96px; height:96px; }
.build-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.item-icon { display:inline-block; width:32px; height:32px; vertical-align:middle; margin-right:4px; object-fit:cover; }
.partner-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(120px,1fr)); gap:12px; margin:16px 0; }
.partner-card { text-align:center; padding:8px; border:1px solid #e2e8f0; border-radius:8px; }
.partner-card img { width:56px; height:56px; display:block; margin:0 auto 4px; }
.partner-card .name { font-size:0.75rem; font-weight:bold; }
.partner-card .rate { font-size:0.7rem; color:#666; }
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
.stat-bar-wrap { max-width:380px; margin:16px 0; font-size:0.9em; }
.stat-row { display:flex; align-items:center; gap:8px; padding:6px 0; border-bottom:1px solid #e2e8f0; }
.stat-label { width:72px; min-width:72px; color:#555; font-weight:600; white-space:nowrap; }
.stat-track { flex:1; background:#eee; border-radius:4px; height:12px; }
.stat-val { width:36px; text-align:right; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" />
  <div>
    <h2 style="margin:0 0 6px">メガカイリュー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-11-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong>17位</strong> ／ カイリュナイト採用率 <strong>80.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン開始8日目（2026/05/20）時点の集計です

---

ポケモンチャンピオンズのシングルバトルM-2シーズンで、カイリューは**使用率17位**を記録しています。その採用構成を見ると、カイリュナイトを持たせたメガカイリュー運用が**80.8%**と圧倒的な割合を占めており、「カイリューを採用するならメガ進化させる」という認識がプレイヤーに広く浸透していることが分かります。

ポケモンチャンピオンズのメガカイリューは**本家シリーズには存在しないポケモンチャンピオンズオリジナルのメガ進化**です。データからとくこうとすばやさが大幅強化されていることが分かります。ひかえめ採用率66.7%・CS型が35.0%で主流となっており、エアスラッシュ・りゅうせいぐん・10まんボルト・かえんほうしゃという特殊4色技構成が環境に刺さっています。

この記事では実際の対戦データをもとに、メガカイリューの強さの秘密・主要な型の解説・苦手なポケモンと対処法・相性の良いパーティ構成まで徹底的に掘り下げます。

---

## なぜ今メガカイリューが強いのか

### 1. ポケモンチャンピオンズオリジナルのメガ進化でとくこうが劇的に向上

ポケモンチャンピオンズで実装されたオリジナルのメガ進化で、データからとくこうとすばやさが大幅強化されていることが分かります。通常カイリューは攻撃寄りの万能型というイメージが強いポケモンですが、メガ進化後はひかえめCS型が主流となっており、特殊アタッカーとしての運用が確立されています。エアスラッシュ54.5%・りゅうせいぐん52.8%という採用率は、メガカイリューが特殊技主体で立ち回ることを示しています。

### 2. 特殊4色技でM-2環境の主要ポケモンをほぼ全て処理できる

メガカイリューの最大の強みは、**ドラゴン（りゅうせいぐん）＋ひこう（エアスラッシュ）＋でんき（10まんボルト）＋ほのお（かえんほうしゃ）**という特殊4色技構成にあります。この4つの技だけで、M-2環境トップ20のうち大部分に等倍以上のダメージが取れます。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:26px;height:26px;display:block;margin:0 auto 2px">りゅうせいぐん</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-11-flying.png" alt="ひこう" style="width:26px;height:26px;display:block;margin:0 auto 2px">エアスラッシュ</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;display:block;margin:0 auto 2px">10まんボルト</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:26px;height:26px;display:block;margin:0 auto 2px">かえんほうしゃ</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0879-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0448-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0094-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0277-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミロップ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0227-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ハッサム</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
</tbody>
</table>
</div>

<small>◎=効果抜群（2倍）、○=等倍、△=いまひとつ（0.5倍）</small>

このように、4つの技だけで環境の主要ポケモンほぼ全てに対して等倍以上を取れるのが、メガカイリューが採用される大きな理由です。

### 3. しんそく先制技がフィニッシャーとして機能する

しんそくの採用率は44.6%と半数近くに達しています。ノーマルタイプの先制技であるしんそくは、相手をメガカイリューの特殊技で削ったあと、残りHPを確実に仕留めるフィニッシャーとして機能します。特に：

- りゅうせいぐんのCダウン後に安全に詰められる
- 相手の先制技（アクアジェットなど）に対して後手を打てる
- すばやさが低いポケモンへの確実な削り

という場面で輝きます。特殊4色技で削りを入れ、しんそくで締めるという流れが、メガカイリューの黄金パターンです。

---

## 基本スペック

### 種族値（通常カイリュー）

<div class="stat-bar-wrap">
  <div class="stat-row">
    <span class="stat-label">HP</span>
    <div class="stat-track"><div style="width:45.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">91</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">こうげき</span>
    <div class="stat-track"><div style="width:67%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span class="stat-val"><strong>134</strong></span>
  </div>
  <div class="stat-row">
    <span class="stat-label">ぼうぎょ</span>
    <div class="stat-track"><div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">95</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくこう</span>
    <div class="stat-track"><div style="width:50%;background:linear-gradient(90deg,#a78bfa,#7c3aed);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">100</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくぼう</span>
    <div class="stat-track"><div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">100</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">すばやさ</span>
    <div class="stat-track"><div style="width:40%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span class="stat-label">合計</span>
    <div style="flex:1"></div>
    <span style="width:36px;text-align:right;color:#2563eb">600</span>
  </div>
</div>

### メガ進化後の変化（データからの考察）

ポケモンチャンピオンズのメガカイリューは**本家シリーズには存在しないオリジナルのメガ進化**です。実際の対戦データから以下のことが確認できます。

**確実に強化されていること：**
- **とくこうが大幅強化** — ひかえめ66.7%・CS型35.0%が主流。通常カイリューのとくこう100は特筆すべき数値ではありませんが、メガ後はひかえめCS型が環境標準となっており、実質的なとくこうが大幅に伸びていることが分かります
- **すばやさが向上** — CS+HB型やCS型での運用が多く、S振りが主流になっているデータから、メガ後のすばやさも強化されているとみられます
- **タイプはドラゴン/ひこう** — 使用技（エアスラッシュ、りゅうせいぐん）や弱点挙動から判断

数値の詳細は確定データが存在しないため本記事では記載しませんが、特殊アタッカーとして環境トップクラスの火力を持つことは間違いありません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
  <img src="/images/types/type-11-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">いわ<br>
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">ドラゴン<br>
    <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">フェアリー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">むし（0.5倍）<br>
    <img src="/images/types/type-02-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">かくとう（0.5倍）<br>
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">ほのお（0.5倍）<br>
    <img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">みず（0.5倍）<br>
    <img src="/images/types/type-13-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">くさ（0.25倍）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

**こおり4倍弱点が最大のリスク**です。ドラゴンタイプとひこうタイプの両方がこおりに弱いため、こおり技を受けると確定1発で倒されます。環境にれいとうビーム・アイススピナー持ちが多い場合は特に注意が必要です。一方でじめん無効（ひこうタイプ）によりじしん系の技を完全に受けられる点、くさタイプへの4分の1耐性も見逃せません。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">分類</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">主な用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>54.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうSTAB技。ひるみ30%付きでサイクルを崩す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>52.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴンSTAB・高火力。Cダウン後はしんそくで詰める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプ（アシレーヌ・ギャラドス）への有効打</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>48.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・くさタイプ（ブリジュラス・ハッサム）処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんそく</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>44.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制技フィニッシャー。りゅうせいぐんCダウン後の保険</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>35.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP回復。耐久寄り運用・みがわりとの組み合わせ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型・AS型での採用。でんき・はがね対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスミラー・じめんタイプへの有効打</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.2%</td>
  <td style="padding:8px 12px;border:1px solid $cbd5e1">物理積み型。こうげき・すばやさ+1</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ・たべのこしとの組み合わせで耐久戦</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1：ひかえめCS型（特殊4色技）―― 最も採用率の高いスタンダード型

<div class="build-header">
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.7%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">努力値：CS（35.0%）</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| エアスラッシュ | ひこう（特殊） | STAB・ひるみ効果 |
| りゅうせいぐん | ドラゴン（特殊） | ドラゴンSTAB最高打点 |
| 10まんボルト | でんき（特殊） | みずタイプ対策 |
| かえんほうしゃ | ほのお（特殊） | はがね・くさ対策 |

**強み**  
とくこうとすばやさを最大限に引き出した純粋な特殊アタッカー構成。4色技によるタイプカバレッジが圧巻で、ひかえめ補正によるとくこう上昇で多くの環境ポケモンを確定2発圏内に捉えられます。りゅうせいぐんでとくこうが下がっても、しんそく（44.6%採用）で残ったHPを削れるのも優秀。りゅうせいぐんの使用後はエアスラッシュや10まんボルトで戦い続ける柔軟さがあります。

**弱み**  
りゅうせいぐん使用後のとくこうダウンが課題。こおり技への4倍弱点は致命的で、1発で倒される場合があります。また、フェアリータイプ（ミミロップ・フラエッテ）にはドラゴン技が無効のため、かえんほうしゃ・エアスラッシュなどで対応が必要です。

---

### 型2：ひかえめCS+HB型（ラムのみ）―― 状態異常対策を加えた安定型

<div class="build-header">
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.7%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">努力値：CS+HB（11.8%）</span>
  <span style="background:#d97706;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：ラムのみ（12.4%）</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| エアスラッシュ | ひこう（特殊） | STAB技 |
| りゅうせいぐん | ドラゴン（特殊） | 最高打点 |
| 10まんボルト | でんき（特殊） | みずタイプ対策 |
| はねやすめ / かえんほうしゃ | ひこう / ほのお | 自己回復 or 4色補完 |

**強み**  
HBに努力値を一部振ることで物理耐久が上がり、こうげき系の攻撃をより多く耐えられます。ラムのみで**まひ・やけど・ねむり**を1度無効化できるため、状態異常に依存した戦法を封じながら継続して動けます。特にきあいだめ戦術・おにびを使うポケモンへの回答になります。

**弱み**  
CS比較でのとくこうとすばやさが若干低下するため、火力面では純粋CS型に一歩及びません。また、ラムのみは1度しか使えないため、2度目の状態異常には無力です。

---

### 型3：CS+しんそくフィニッシャー型 ―― 先制技で詰めを確実にする型

<div class="build-header">
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.7%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">努力値：CS（35.0%）</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| りゅうせいぐん | ドラゴン（特殊） | 最高打点 |
| エアスラッシュ | ひこう（特殊） | STAB |
| 10まんボルト / かえんほうしゃ | でんき / ほのお | タイプ補完 |
| しんそく | ノーマル（物理）先制 | Cダウン後のフィニッシャー |

**強み**  
りゅうせいぐんを気兼ねなく打てるのが最大の強み。Cダウンしても**しんそく（優先度+2）**で相手を仕留められるため、りゅうせいぐん→しんそくの2ターンコンボが確立します。相手の先制技（アクアジェット等）をしんそくの後攻で回避しながら動ける場面もあります。

**弱み**  
しんそくは物理技のため、こうげきが低い（ひかえめ補正）と火力が不足する場合があります。フェアリー・いわタイプには無効・等倍止まりで、フィニッシャーとしての信頼性が下がります。

---

### 型4：いじっぱりAS型（りゅうのまい物理型）―― 15%が採用する物理積みルート

<div class="build-header">
  <span style="background:#dc2626;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：いじっぱり（9.1%）/ ようき（7.6%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">努力値：AS（9.9%）</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| りゅうのまい | ドラゴン（変化） | こうげき・すばやさ+1 |
| しんそく | ノーマル（物理）先制 | 先制フィニッシャー |
| じしん | じめん（物理） | はがね・でんき処理 |
| げきりん / りゅうのいぶき | ドラゴン（物理） | ドラゴンSTAB物理 |

**強み**  
りゅうのまいで積んだ後は物理こうげき134が実質的にさらに高まり、高耐久ポケモンも突破できます。しんそくとじしんによる物理範囲で、特殊型が苦手な相手（Dの高いポケモン）にも対応できます。こうげき134は環境でも最高水準。

**弱み**  
積む時間を作る必要があるため、対戦序盤に出しにくい。特殊型に比べてタイプカバレッジが劣り、みず・フェアリー・いわへの対応が限定的。フェアリータイプのポケモンにはドラゴン技が完全無効なので注意。

---

## 持ち物採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>カイリュナイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>80.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ進化必須。とくこう・すばやさ大幅強化のため</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラムのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まひ・やけど・ねむり無効化。状態異常技への保険</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たべのこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ・みがわりとのHP回復コンボ用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シルクのスカーフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんそく強化。ノーマル技の火力を上げる特化型</td>
</tr>
</tbody>
</table>
</div>

カイリュナイト80.8%という採用率は、メガ進化によるステータス強化が通常状態との差を大きく上回ることを示しています。ラムのみ12.4%は、メガカイリューを採用する際にメガ石を持てない場合の次善策として、通常カイリューとして状態異常対策をして使うプレイヤーが一定数いることを示しています。

---

## パーティ構成

### 苦手なポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#fef2f2">
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">苦手な理由</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">対処法</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0277-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミロップ
    <small style="color:#94a3b8;display:block">ノーマル/フェアリー</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">フェアリータイプでりゅうせいぐんが無効。高いこうげきと特性で対策</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">エアスラッシュ・かえんほうしゃで対応。じしん（物理型）も有効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-1001-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フラエッテ（永遠）
    <small style="color:#94a3b8;display:block">フェアリー</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">フェアリータイプでりゅうせいぐん無効。高いとくぼうでダメージが通りにくい</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">どくタイプのパートナーで対処。かえんほうしゃ・エアスラッシュを通す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0879-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア
    <small style="color:#94a3b8;display:block">はがね/ひこう</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">はがね/ひこうでドラゴン0.5倍・ひこう0.5倍。高い物理耐久</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">10まんボルトで2倍を狙う。かえんほうしゃは0.5倍なので非推奨</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0245-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">スイクン系・みずタイプ高耐久
    <small style="color:#94a3b8;display:block">みず</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">Dが高いみずタイプはかえんほうしゃが通らず、10まんボルトも耐える場合がある</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">パートナーのでんきタイプに処理を任せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガスターミー
    <small style="color:#94a3b8;display:block">みず/エスパー</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アイススピナー（こおり4倍）を持つ場合、確定1発で倒される</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">出し合いを避け、ガブリアスなどで先に対処する</td>
</tr>
</tbody>
</table>
</div>

### 相性の良いパートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">使用率1位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">フェアリー・いわへの物理打点を担当</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0227-00.webp" alt="ハッサム">
    <div class="name">ハッサム</div>
    <div class="rate">使用率15位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">フェアリー・こおり受け。こおりが4倍のカイリューを補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0208-00.webp" alt="ハガネール">
    <div class="name">はがね系</div>
    <div class="rate">フェアリー受け</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">ミミロップ・フラエッテへの回答</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0476-00.webp" alt="ドータクン系">
    <div class="name">はがねタイプ</div>
    <div class="rate">こおり受け</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">カイリューの4倍弱点こおりを受けられる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">みず系サポート</div>
    <div class="rate">ステロ展開</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">ステロで相手を削りカイリューの確定圏を広げる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0113-00.webp" alt="ハピナス">
    <div class="name">とくぼう壁</div>
    <div class="rate">特殊受け</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">カイリューが苦手な特殊こおり技を受ける</div>
  </div>
</div>

メガカイリューを採用する際の主な弱点補完は**こおり対策**と**フェアリー対策**の2軸です。特にこおり技（アイススピナー・れいとうビーム・ふぶき）を扱うポケモンに対して、先発でチェックできるポケモンをパーティに入れることが必須です。

**推奨パーティ構成の方針：**
1. メガカイリュー（特殊4色技フィニッシャー）
2. フェアリー・こおり対策のはがねタイプ（ハッサム・アーマーガアなど）
3. ステロを撒けるサポート役（ガブリアス・カバルドンなど）

---

## まとめ：型別比較表

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">攻撃力</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">耐久力</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">速度</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">範囲</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">状態異常耐性</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">向いている場面</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">CS特殊4色型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★☆☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★☆☆☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">環境に広く刺さる汎用構成</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">CS+HB ラムのみ型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">状態異常が多い環境・安定重視</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">CS+しんそく型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★☆☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★☆☆☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">りゅうせいぐんを気兼ねなく打ちたい時</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">AS りゅうのまい型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★☆☆☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">積み展開・物理環境</td>
</tr>
</tbody>
</table>
</div>

メガカイリューはポケモンチャンピオンズオリジナルのメガ進化を活かした特殊4色型が現環境の主流です。こおり4倍弱点という明確な弱点を持ちながら、それを上回るタイプカバレッジと火力でM-2シングル17位の使用率を維持しています。

1メガルールの中でカイリュナイトを採用するかどうかは、パーティの戦略全体に関わる重要な判断です。80.8%という高い採用率が示す通り、メガカイリューはその価値を十分に証明しています。環境に幅広く刺さる特殊4色技+しんそく構成を軸に、パーティの弱点を補完するポケモンを揃えることが、メガカイリューを最大限に活かす鍵となります。
