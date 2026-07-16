---
title: 'メガカイリュー考察 M-2 特殊4色型 採用率と型別解説'
description: 'チャンピオンズM-2使用率16位メガカイリューを徹底解説。ひかえめCS特殊型・特殊4色技・しんそく先制のメカニズムを解説し、CS型・しんそく型・はねやすめ型・非メガ物理型の主要構築と相性パーティまで実データをもとに紹介します。'
updatedDate: '2026-05-24'
pubDate: '2026-05-24'
draft: false
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
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong>16位</strong> ／ カイリュナイト採用率 <strong>80.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン2026/05/30時点の集計です

---

ポケモンチャンピオンズのシングルバトルM-2シーズンで、カイリューは**使用率16位**を記録しています。その採用構成を見ると、カイリュナイトを持たせたメガカイリュー運用が**80.7%**と大きな割合を占めており、「カイリューを採用するならメガ進化させる」という認識がプレイヤーに広く浸透していることが分かります。

メガカイリューは**とくこうとすばやさが強化されるメガ進化**で、ひかえめ採用率66.5%が示す通り特殊アタッカー運用が主流です。エアスラッシュ55.6%・りゅうせいぐん53.1%・10まんボルト47.6%・かえんほうしゃ47.8%という特殊4色技構成が環境に刺さっています。

この記事では実際の対戦データをもとに、メガカイリューが採用される理由・主要な型の解説・苦手なポケモンと対処法・相性の良いパーティ構成まで徹底的に掘り下げます。

---

## なぜ今メガカイリューが強いのか

### 1. メガ進化でとくこうが大きく向上

メガ進化によってとくこうが100→145、すばやさが80→100に強化されます。一方こうげきは134→124に低下するため、通常カイリューの物理アタッカーとしてのイメージとは異なり、メガ進化後は特殊アタッカー運用が主流です。ひかえめ採用率66.5%というデータがその事実を裏付けており、エアスラッシュ55.6%・りゅうせいぐん53.1%という特殊技の採用率もメガカイリューが特殊技主体で立ち回ることを示しています。

### 2. マルチスケイルで初手の生存率が高い

カイリューの特性**マルチスケイル**は、HPが満タンのとき受けるダメージを半減する効果を持ちます。こおり4倍弱点という致命的なリスクを抱えながらも使用率16位を維持できている理由の一つがこれで、先発で出した初ターンは確定1発圏内の攻撃も耐える場面があります。メガ進化前後どちらでも特性は変わらないため、メガ進化するターンを含めてマルチスケイルの恩恵を受け続けられます。ただし状態異常・天候ダメージ・ステルスロック等でHPが削られると効果を失う点には注意が必要です。

### 3. 特殊4色技でM-2環境の主要ポケモンの多くに等倍以上を取れる

メガカイリューの最大の強みは、**ドラゴン（りゅうせいぐん）＋ひこう（エアスラッシュ）＋でんき（10まんボルト）＋ほのお（かえんほうしゃ）**という特殊4色技構成にあります。この4つの技だけで、M-2環境トップ20のうち大部分に等倍以上のダメージが取れます。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:26px;height:26px;display:block;margin:0 auto 2px">りゅうせいぐん</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:26px;height:26px;display:block;margin:0 auto 2px">エアスラッシュ</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;display:block;margin:0 auto 2px">10まんボルト</th>
  <th style="padding:6px 4px;border:1px solid #cbd5e1;min-width:60px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:26px;height:26px;display:block;margin:0 auto 2px">かえんほうしゃ</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">✕</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">✕</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガリザードンY</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0448-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガルカリオ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガギャラドス</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0094-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0428-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガミミロップ</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#e67e22;font-weight:bold">◎</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガハッサム</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#60a5fa">△</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#94a3b8">○</td>
  <td style="padding:6px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">◎×4</td>
</tr>
</tbody>
</table>
</div>

<small>◎×4=4倍、◎=効果抜群（2倍）、○=等倍、△=いまひとつ（0.5倍）、¼=4分の1、✕=無効。相手はメガ運用が主流のためメガ後タイプで判定（メガギャラドス＝みず/あく、メガミミロップ＝ノーマル/かくとう、メガハッサム＝むし/はがね等）。</small>

このように、4色の技で各相手に最低1つは等倍以上の打点を確保できる点が、メガカイリューが採用される大きな理由です。ただしガブリアス・アシレーヌ・ブリジュラスのように刺さる技が限定される相手もおり、技構成次第では有効打を欠く点には注意が必要です。

### 4. しんそく先制技がフィニッシャーとして機能する

しんそくの採用率は45.6%と半数近くに達しています。ノーマルタイプの先制技であるしんそくは、相手をメガカイリューの特殊技で削ったあと、残りHPを仕留めるフィニッシャーとして機能します。特に：

- りゅうせいぐんでとくこうが2段階下がった後でも、物理技のしんそくなら火力が落ちずに削りを継続できる
- 優先度+2のしんそくは、アクアジェット（優先度+1）など多くの先制技より先に動ける
- すばやさで上を取られる相手にも、削れていれば先制技で確実に倒し切れる

という場面で輝きます。特殊4色技で削りを入れ、しんそくで締めるという流れが、メガカイリューの基本的な立ち回りです。

---

## 基本スペック

### 種族値（メガカイリュー）

<div class="stat-bar-wrap">
  <div class="stat-row">
    <span class="stat-label">HP</span>
    <div class="stat-track"><div style="width:45.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">91</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">こうげき</span>
    <div class="stat-track"><div style="width:62%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">124</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">ぼうぎょ</span>
    <div class="stat-track"><div style="width:57.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">115</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくこう</span>
    <div class="stat-track"><div style="width:72.5%;background:linear-gradient(90deg,#a78bfa,#7c3aed);height:12px;border-radius:4px"></div></div>
    <span class="stat-val"><strong>145</strong></span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくぼう</span>
    <div class="stat-track"><div style="width:62.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">125</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">すばやさ</span>
    <div class="stat-track"><div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span class="stat-label">合計</span>
    <div style="flex:1"></div>
    <span style="width:36px;text-align:right;color:#2563eb">700</span>
  </div>
</div>

### メガ進化による変化

通常カイリューと比較したメガ進化後のステータス変化は以下の通りです。

| ステータス | 通常 | メガ後 | 変化 |
|---|---|---|---|
| HP | 91 | 91 | — |
| こうげき | 134 | 124 | **−10** |
| ぼうぎょ | 95 | 115 | **+20** |
| とくこう | 100 | **145** | **+45** |
| とくぼう | 100 | 125 | **+25** |
| すばやさ | 80 | 100 | **+20** |
| 合計 | 600 | 700 | **+100** |

注目点は**とくこうが100→145と大幅強化**される一方、**こうげきは134→124に低下**する点です。これがひかえめCS型が主流となっている理由であり、メガ進化によって物理アタッカーから特殊アタッカーへと運用が変わります。すばやさも80→100に強化され、りゅうのまいなしでも多くの環境ポケモンに先手を取れるようになります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
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
    <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">かくとう（0.5倍）<br>
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">ほのお（0.5倍）<br>
    <img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">みず（0.5倍）<br>
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">くさ（0.25倍）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:2px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

**こおり4倍弱点が最大のリスク**です。ドラゴンタイプとひこうタイプの両方がこおりに弱いため、こおり技を受けると確定1発で倒されます。環境にれいとうビーム・アイススピナー持ちが多い場合は特に注意が必要です。一方でじめん無効（ひこうタイプ）によりじしん系の技を無効化できる点、くさタイプへの4分の1耐性も見逃せません。

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
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>55.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう一致技。命中95%・ひるみ30%で相手の行動を封じる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン一致・高火力。命中90%・Cダウン後はしんそくで詰める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプ（アシレーヌ・ギャラドス）への有効打</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・くさタイプ（ハッサム等）処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんそく</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制技フィニッシャー。りゅうせいぐんCダウン後の保険</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>35.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP回復。耐久寄り運用・みがわりとの組み合わせ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型・AS型での採用。でんき・はがね対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスミラー・じめんタイプへの有効打</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理積み型。こうげき・すばやさ+1</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ・たべのこしとの組み合わせで耐久戦</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1：ひかえめCS型（特殊4色技）―― 最も採用率の高いスタンダード型

<div class="build-header">
  <span style="background:#6b7280;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：マルチスケイル（98.2%）</span>
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.5%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：C32 S32 H2（22.2%）</span>
  <span style="background:#16a34a;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：カイリュナイト</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| エアスラッシュ | ひこう（特殊） | ひこう一致・ひるみ30%・命中95% |
| りゅうせいぐん | ドラゴン（特殊） | ドラゴン一致最高打点・命中90% |
| 10まんボルト | でんき（特殊） | みずタイプ対策 |
| かえんほうしゃ | ほのお（特殊） | はがね・くさ対策 |

**強み**  
とくこうとすばやさを最大限に引き出した特殊アタッカー構成。4タイプの技で広い範囲をカバーでき、ひかえめ補正によるとくこう上昇で多くの環境ポケモンを確定2発圏内に捉えられます。りゅうせいぐん使用後もエアスラッシュや10まんボルトで継続的に圧力をかけられる柔軟さが強みです。

**弱み**  
りゅうせいぐん使用後のとくこうダウンが課題で、しんそくがないため削り切れない場面が生じやすいです。また、はねやすめを採用しないためマルチスケイルの再発動ができず、ステルスロックや天候ダメージでHPが削れると開幕からマルチスケイルが機能しなくなります。

---

### 型2：ひかえめCS型（しんそく採用）―― りゅうせいぐん後の詰めを確実にする型

<div class="build-header">
  <span style="background:#6b7280;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：マルチスケイル（98.2%）</span>
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.5%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：C32 S32 H2（22.2%）</span>
  <span style="background:#16a34a;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：カイリュナイト</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| りゅうせいぐん | ドラゴン（特殊） | ドラゴン一致最高打点・命中90% |
| エアスラッシュ | ひこう（特殊） | ひこう一致・ひるみ30%・命中95% |
| 10まんボルト / かえんほうしゃ | でんき / ほのお | タイプ補完（1枠） |
| しんそく | ノーマル（物理）先制 | Cダウン後のフィニッシャー |

**強み**  
りゅうせいぐんを気兼ねなく打てるのが最大の強み。とくこうが2段階ダウンしても**しんそく（優先度+2）**で相手を仕留められるため、りゅうせいぐん→しんそくの2ターンコンボが安定します。タイプ補完技が1枠に絞られる分、4色型より技範囲は狭まりますが、試合の締め方が明確になります。

**弱み**  
しんそくはメガ後のこうげき124をベースにした物理技のため、ひかえめ補正がついても火力はさほど高くありません。カバーできないタイプが増える点も注意です。

---

### 型3：ひかえめHBS型（メガ耐久特殊型）―― マルチスケイルを活かした崩し型

<div class="build-header">
  <span style="background:#6b7280;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：マルチスケイル（98.2%）</span>
  <span style="background:#3b82f6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ（66.5%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：C32 S32 B1 H1（11.3%）</span>
  <span style="background:#16a34a;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：カイリュナイト</span>
</div>

**技構成（例）**

| 技 | タイプ | 採用理由 |
|---|---|---|
| エアスラッシュ | ひこう（特殊） | ひこう一致・ひるみ30%・命中95% |
| りゅうせいぐん | ドラゴン（特殊） | ドラゴン一致最高打点・命中90% |
| 10まんボルト / かえんほうしゃ | でんき / ほのお | タイプ補完 |
| はねやすめ | ひこう（変化） | HP回復でマルチスケイル再発動を狙う |

**強み**  
HBにEVを振ることで物理方面の耐久が向上し、マルチスケイルと合わせて先発での行動保証がさらに高まります。はねやすめでHPを満タンに戻すことでマルチスケイルを再発動し、2度目の被弾も半減できる場面があります。

**弱み**  
CSフルに振った型よりとくこうとすばやさが下がるため、火力・速度で劣ります。はねやすめを打つ隙がない試合展開では、回復技の枠が無駄になることもあります。

---

### 型4：非メガ型（ラムのみ / りゅうのまい物理）―― メガ進化権を別のポケモンに渡す構成

<div class="build-header">
  <span style="background:#6b7280;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：マルチスケイル（98.2%）</span>
  <span style="background:#dc2626;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ひかえめ / いじっぱり / ようき</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：C32 S32 / A32 S32</span>
  <span style="background:#d97706;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：ラムのみ（11.7%）など</span>
</div>

**代表的な技構成**

| 技 | タイプ | 採用理由 |
|---|---|---|
| エアスラッシュ / りゅうせいぐん | ひこう / ドラゴン | 一致技 |
| 10まんボルト / かえんほうしゃ | でんき / ほのお | タイプ補完 |
| りゅうのまい | ドラゴン（変化） | 物理型の場合の積み技 |
| しんそく / じしん | ノーマル / じめん | フィニッシャー |

**強み**  
メガ進化権を別のポケモン（メガルカリオ・メガリザードン等）に渡しながら通常カイリューとして運用できます。こうげき134・ひこうタイプのじめん無効を維持しており、りゅうのまいで積んだ後のじしん・しんそくによる物理全抜きや、ラムのみによる状態異常無効化が主な採用理由です。また、**メガカイリュー（特殊型）と外見上の区別がつかない**ため、相手はりゅうせいぐんやエアスラッシュを警戒してはがね・フェアリータイプを引っ込めがちになります。その読み違いを突いてじしんを通しやすい点も、非メガ物理型ならではの強みです。

**弱み**  
メガ進化しないためS80・とくこう100のまま。メガカイリューと比べて速度と火力の両面で劣ります。じしん・しんそく・りゅうのまいなど物理技が中心となるため、技範囲がドラゴン・ひこう・ノーマル・じめんに絞られます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>80.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ進化でとくこう100→145・すばやさ80→100に大幅強化。特殊アタッカーとして高い火力を得る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラムのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まひ・やけど・ねむり無効化。状態異常技への保険</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たべのこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ・みがわりとのHP回復コンボ用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シルクのスカーフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんそく強化。ノーマル技の火力を上げる特化型</td>
</tr>
</tbody>
</table>
</div>

カイリュナイト80.7%という採用率は、メガ進化によるステータス強化が通常状態との差を大きく上回ることを示しています。ラムのみ11.7%は、メガカイリューを採用する際にメガ石を持てない場合の次善策として、通常カイリューとして状態異常対策をして使うプレイヤーが一定数いることを示しています。

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
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0670-05.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フラエッテ（永遠）
    <small style="color:#94a3b8;display:block">フェアリー</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">フェアリーでりゅうせいぐん無効。とくぼうが高く、かえんほうしゃ・エアスラッシュ（ともに等倍）でも確定数が伸びない</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">どく技で弱点（×2）を突けるキラフロル等のパートナーで処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア
    <small style="color:#94a3b8;display:block">はがね/ひこう</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">りゅうせいぐん・エアスラッシュをともに0.5倍で受け、高い物理耐久とはねやすめで居座る。かえんほうしゃ非採用（採用率47.8%）の型では突破しづらい</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">かえんほうしゃ（はがね弱点×2）を採用しておく。10まんボルトもひこう2倍で弱点を突ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガスターミー
    <small style="color:#94a3b8;display:block">みず/エスパー</small>
  </td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アイススピナー（採用率64.9%）がこおり4倍を突き、こちらの満タンマルチスケイルでも確定1発圏内</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">メガカイリューを後発に温存し、ガブリアスなどで先に処理する</td>
</tr>
</tbody>
</table>
</div>

### 相性の良いパートナー

同居率上位（champs.pokedb.tokyoの同居データ）から、フェアリー対策やステルスロック撒きを担える補完枠を挙げます。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル">
    <div class="name">キラフロル</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">ヘドロウェーブ（どく×2）でフェアリーに打点。ステルスロックも撒ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">ステルスロック撒き。いわ・はがねへの物理打点を担当</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">はがね/ゴーストでフェアリー技0.5倍。フラエッテを受け回せる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.68rem;color:#555;margin-top:2px">ステルスロック+あくびで起点を作り、物理を受け止める</div>
  </div>
</div>

メガカイリューを採用する際の主な弱点補完は**フェアリー対策**です。りゅうせいぐんを無効化するフェアリー（フラエッテ等）に対し、どく・はがねで殴れるポケモンを添えると役割を回しやすくなります。こおり4倍弱点については、環境上位にこおり技持ちが少ない（アイススピナー持ちのメガスターミーが主）ため、その個体を後発処理できる枠を1つ用意すれば足ります。

**推奨パーティ構成の方針：**
1. メガカイリュー（特殊4色技フィニッシャー）
2. フェアリーに弱点（どく・はがね）を突けるポケモン（キラフロル・ギルガルドなど）
3. ステルスロックを撒けるサポート役（ガブリアス・カバルドンなど）

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
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">HBS はねやすめ型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★☆☆☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">はねやすめで居座る耐久寄り運用</td>
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
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">非メガ りゅうのまい型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">メガ枠を他に譲る積み展開</td>
</tr>
</tbody>
</table>
</div>

メガカイリューは特殊4色型が現環境の主流です。こおり4倍弱点という明確な弱点を持ちながら、それを上回るタイプ範囲と火力でM-2シングル16位の使用率を維持しています。

カイリュナイト採用率80.7%が示す通り、メガカイリューは特殊アタッカーとして広く採用されています。環境に幅広く刺さる特殊4色技+しんそく構成を軸に、パーティの弱点を補完するポケモンを揃えることが、メガカイリューを最大限に活かす鍵となります。
