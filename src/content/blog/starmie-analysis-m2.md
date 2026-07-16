---
title: 'メガスターミー徹底考察 M-2シーズン ちからもちが生む圧倒的火力'
description: 'M-2シングルバトル使用率20位・メガ採用率97.8%のメガスターミーを徹底分析。特性ちからもちで実質A200・火力指数42,585のアクアブレイクの破壊力、アクアジェット先制、アイススピナー・クイックターン活用法を実データをもとに解説します。'
updatedDate: '2026-05-22'
pubDate: '2026-05-22'
heroImage: '../../assets/hero-starmie-m2.png'
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
  <img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" />
  <div>
    <h2 style="margin:0 0 6px">メガスターミー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong>20位</strong> ／ スターミナイト採用率 <strong>97.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン開始8日目（2026/05/20）時点の集計です

---

**「スターミーを採用するなら、ほぼ全員がメガ進化させる」**

その理由は特性**ちからもち**にあります。メガ進化後の特性ちからもちは「物理技の攻撃力を2倍にする」という効果で、メガスターミーのこうげき（種族値100）を実質200相当に引き上げます。これはTier1の中でも突出した数値です。

全採用技を見ると**アクアブレイク・アクアジェット・アイススピナー・クイックターン・しねんのずつき・サイコカッター**と、全て物理技で構成されています。性格もいじっぱり71.4%・ようき24.9%と物理型ほぼ一択。AS型61.9%というEV配分は、ちからもちの恩恵を最大化するこうげきと、すばやさ120を活かすすばやさへの全力投資を示しています。

この記事では実データをもとに、なぜメガスターミーがこれほど高い採用率を誇るのか、どのような型で使われているのか、そしてパーティにどう組み込むべきかを徹底的に分析します。

---

## なぜ今メガスターミーが強いのか

### 1. ちからもちによる実質A200の圧倒的火力

メガスターミー最大の強みは特性**ちからもち**です。「物理技の攻撃力を2倍にする」この特性によって、種族値こうげき100のスターミーが実質こうげき200として機能します。

Lv50・いじっぱり・A32振りの実数値は**A167**で、ちからもち適用後は**実質A334**。これはTier1環境のあらゆる物理アタッカーを上回ります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">こうげき種族値</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">特性補正</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">実質こうげき（Lv50いじA32）</th>
</tr>
</thead>
<tbody>
<tr style="background:#fef9c3">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">メガスターミー</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1">ちからもち ×2.0</td>
  <td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;color:#dc2626">334</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">メガガブリアス</td>
  <td style="padding:8px;border:1px solid #cbd5e1">170</td>
  <td style="padding:8px;border:1px solid #cbd5e1">すながくれ（補正なし）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">233</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">メガギャラドス</td>
  <td style="padding:8px;border:1px solid #cbd5e1">155</td>
  <td style="padding:8px;border:1px solid #cbd5e1">かたやぶり（火力補正なし）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">277</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">メガルカリオ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">145</td>
  <td style="padding:8px;border:1px solid #cbd5e1">てきおうりょく（タイプ一致補正×2.0）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">200</td>
</tr>
</tbody>
</table>
</div>

ちからもちは「物理技すべて」に適用されるため、アクアブレイク・アイススピナー・しねんのずつきなど技を問わず恩恵を受けられる点も強力です。

### 2. みずタイプ物理技の圧倒的制圧力：アクアブレイク＋アクアジェット

アクアブレイク90.5%・アクアジェット87.2%という採用率は、この2つが事実上のメガスターミーの代名詞であることを示しています。

- **アクアブレイク**：高威力みず物理技。Bダウン20%の追加効果で次のターンも有利
- **アクアジェット**：優先度+1の先制みず物理技。削れた相手を確実に仕留める

高火力の通常技と先制技の組み合わせは、「倒しきれなかった場合の保険」が常に機能する状態を作ります。アクアブレイクで削り→アクアジェットで確実にフィニッシュ、という2段攻撃が非常に強力です。

### 3. アイススピナーによるドラゴン・くさ・じめん対策

アイススピナー採用率64.8%は、みずタイプが苦手とするくさタイプ・ドラゴンタイプへの回答として機能しています。M-2環境トップにいるガブリアス（1位）への打点として特に重要で、こおり4倍のガブリアスを確実に処理できます。

---

## 基本スペック

### 通常スターミーの種族値

<div class="stat-bar-wrap">
  <div class="stat-row">
    <span class="stat-label">HP</span>
    <div class="stat-track"><div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">60</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">こうげき</span>
    <div class="stat-track"><div style="width:37.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">75</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">ぼうぎょ</span>
    <div class="stat-track"><div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">85</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくこう</span>
    <div class="stat-track"><div style="width:50%;background:linear-gradient(90deg,#a78bfa,#7c3aed);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">100</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくぼう</span>
    <div class="stat-track"><div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">85</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">すばやさ</span>
    <div class="stat-track"><div style="width:57.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span class="stat-val"><strong>115</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span class="stat-label">合計</span>
    <div style="flex:1"></div>
    <span style="width:36px;text-align:right;color:#2563eb">520</span>
  </div>
</div>

### メガ進化後の種族値

ポケモンチャンピオンズのメガスターミーは**本家シリーズには存在しないオリジナルのメガ進化**です。

<div class="stat-bar-wrap">
  <div class="stat-row">
    <span class="stat-label">HP</span>
    <div class="stat-track"><div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">60</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">こうげき</span>
    <div class="stat-track"><div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span class="stat-val"><strong>100</strong></span>
  </div>
  <div class="stat-row">
    <span class="stat-label">ぼうぎょ</span>
    <div class="stat-track"><div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">105</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくこう</span>
    <div class="stat-track"><div style="width:65%;background:linear-gradient(90deg,#a78bfa,#7c3aed);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">130</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">とくぼう</span>
    <div class="stat-track"><div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span class="stat-val">105</span>
  </div>
  <div class="stat-row">
    <span class="stat-label">すばやさ</span>
    <div class="stat-track"><div style="width:60%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span class="stat-val"><strong>120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span class="stat-label">合計</span>
    <div style="flex:1"></div>
    <span style="width:36px;text-align:right;color:#2563eb">620</span>
  </div>
</div>

**特性：ちからもち**（物理技の攻撃力を2倍にする）

種族値こうげき100は単体では高くないが、ちからもちにより**実質こうげき200**として機能する。これがメガスターミーのすべての強さの源泉です。

---

### ちからもち火力指数考察

「火力指数 = 実A × 技の基本威力 × タイプ一致補正」で技ごとの相対的な火力を比較します。  
Lv50・いじっぱり・A32振り（実A167）、ちからもち適用後（実質A334）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">基本威力</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">タイプ一致</th>
  <th style="padding:8px 8px;border:1px solid #cbd5e1">火力指数</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr style="background:#fef9c3">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">アクアブレイク</td>
  <td style="padding:8px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px;border:1px solid #cbd5e1">×1.5（みず）</td>
  <td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold;color:#dc2626">42,585</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">メイン打点・Bダウン付き</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">しねんのずつき</td>
  <td style="padding:8px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px;border:1px solid #cbd5e1">×1.5（エスパー）</td>
  <td style="padding:8px;border:1px solid #cbd5e1;font-weight:bold">40,080</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">どく・かくとうへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">アイススピナー</td>
  <td style="padding:8px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px;border:1px solid #cbd5e1">×1.0（タイプ不一致）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">26,720</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">ガブリアスに4倍 → 実効106,880</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">アクアジェット</td>
  <td style="padding:8px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px;border:1px solid #cbd5e1">×1.5（みず）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">20,040</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">優先度+1の先制技。先制技としては破格の火力</td>
</tr>
</tbody>
</table>
</div>

**比較：他Tier1の主力技火力指数**  
メガガブリアス じしん（A233・タイプ一致）: 233×100×1.5 = **34,950**  
メガギャラドス アクアブレイク（A277・タイプ一致）: 277×85×1.5 = **35,318**

メガスターミーのアクアブレイク火力指数**42,585**は、同じみず物理技のメガギャラドスを**20%超上回る**。ちからもちの効果がいかに強力かを示しています。

---

#### 等倍アクアブレイクが確定1発を取れるM-2上位ポケモン

いじっぱりA32・実A334の条件で、みずタイプ**等倍**のM-2上位ポケモンへのダメージを、各記事の使用率最多型の実数値で算出します。

```
Base = floor( floor(22 × 85 × 334 / B) / 50 + 2 )
ダメージ幅 = floor(Base × 1.5 × 0.85) 〜 floor(Base × 1.5)
```

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#e0f2fe">
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:left">使用率最多型（採用率）</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:center">B</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:center">HP</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:center">ダメージ幅</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:center">HP比</th>
  <th style="padding:8px 12px;border:1px solid #7dd3fc;text-align:center">確定数</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #bae6fd">メガゲンガー（12位）<br><small style="color:#94a3b8">ゴースト/どく</small></td>
  <td style="padding:8px 12px;border:1px solid #bae6fd">おくびょうC32 S32（63.0%）</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">135</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">161〜190</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">119〜141%</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center;font-weight:700;color:#0369a1">確定1発</td>
</tr>
<tr style="background:#f0f9ff">
  <td style="padding:8px 12px;border:1px solid #bae6fd">メガルカリオ（9位）<br><small style="color:#94a3b8">かくとう/はがね</small></td>
  <td style="padding:8px 12px;border:1px solid #bae6fd">ようきA32 S32 B4（57.8%）</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">109</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">145</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">147〜174</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">101〜120%</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center;font-weight:700;color:#0369a1">確定1発</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #bae6fd">メガミミロップ（14位）<br><small style="color:#94a3b8">ノーマル/かくとう</small></td>
  <td style="padding:8px 12px;border:1px solid #bae6fd">ようきA32 S32（約60〜65%）</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">114</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">140</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">141〜166</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center">101〜119%</td>
  <td style="padding:8px 12px;border:1px solid #bae6fd;text-align:center;font-weight:700;color:#0369a1">確定1発</td>
</tr>
</tbody>
</table>
</div>

メガルカリオは最小乱数でHP比101%、メガミミロップも最小乱数101%と、いずれもギリギリ全乱数で確定1発に届いています。使用率最多型の標準的な耐久では、等倍であっても1発で落とせる——これがちからもち実質A334の火力水準です。

---

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="エスパー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">でんき
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">くさ
    <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">ゴースト
    <img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">あく
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">ほのお
    <img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">みず
    <img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">はがね
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">エスパー（0.5倍）
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">こおり（0.5倍）
    <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-left:8px;margin-right:3px">かくとう（0.5倍）
  </td>
</tr>
</tbody>
</table>
</div>

弱点は**でんき・くさ・ゴースト・あく・むし**の5タイプと多めです。一方でほのお・みず・はがね・かくとうへの耐性を持ち、エスパーは同タイプ補正により0.5倍と耐えます。M-2環境で多いゴーストタイプ（ゲンガー・ギルガルド）やあくタイプへは注意が必要です。

でんきタイプ（ブリジュラス等）への弱点は特に大きく、対戦序盤の出し順管理が重要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアブレイク</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>90.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプ一致高打点。Bダウン付きで次のターンも有利に</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理・先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>87.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制みず技。削れた相手を確実に仕留める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイススピナー</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>64.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン（ガブリアス等）・くさ対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃しながら交代（みずUターン）。サイクル構築の要</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しねんのずつき</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>43.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパータイプ一致物理技。どく・かくとうへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコカッター</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>23.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">急所率が高いエスパー物理技。しねんのずつきの代替</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こうそくスピン</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステロ・まきびし等の撒き技消去＋すばやさ上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・ぼうぎょ+1の積み技。耐久も上げながら強化</td>
</tr>
</tbody>
</table>
</div>

**全採用技が物理技のみ**という点は、ちからもちの恩恵を最大限に受けるための合理的な選択です。特性の恩恵を受けない特殊技を混ぜる意味がなく、全て物理技でちからもちの×2倍補正をフル活用する構成になっています。

### 技の組み合わせパターン解説

メガスターミーの技は大きく「必須技」と「選択技」に分かれます。

**ほぼ必須（採用率85%以上）**
- アクアブレイク（90.5%）
- アクアジェット（87.2%）

この2本はメガスターミーの根幹をなすみず物理技コンビで、ほぼ全ての型に採用されます。アクアブレイクで高火力を出しつつBダウン20%追加効果、アクアジェットで先制フィニッシュという役割分担が完成されています。

**高採用（採用率50%以上）**
- アイススピナー（64.8%）: ガブリアス・ドラゴン対策として3枠目に最も選ばれる
- クイックターン（53.6%）: サイクル戦の要として4枠目に頻出

**選択技（採用率20〜45%）**
- しねんのずつき（43.1%）: エスパータイプ一致の強打点。どく・かくとうを処理
- サイコカッター（23.4%）: しねんのずつきより威力は下がるが急所率の高さが魅力

**実践でよく見る技セット3パターン：**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">パターン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技1</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特徴</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-weight:600">ドラゴン対策型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しねんのずつき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・ドラゴンに強い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-weight:600">サイクル型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">場持ち重視・情報収集</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-weight:600">積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ビルドアップ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積んで全抜きを狙う</td>
</tr>
</tbody>
</table>
</div>

アイススピナーとクイックターンを両立した4技構成も考えられますが、その場合しねんのずつき/サイコカッターのどちらかを諦めることになり、ゴースト・どく・かくとうへの対応が弱くなります。技構成は環境メタと相談しながら決める必要があります。

---

## 主要型の解説

### 型1：いじっぱりAS型（アクアブレイク+アクアジェット主軸）―― 最も採用率の高いスタンダード型

<div class="build-header">
  <span style="background:#6366f1;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：しぜんかいふく（89.7%）</span>
  <span style="background:#dc2626;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：いじっぱり（71.4%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：A32 S32（53.5%）</span>
  <span style="background:#1d4ed8;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">持ち物：スターミナイト（97.8%）</span>
</div>

**技構成（例）**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致メイン打点・Bダウン20%</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）先制</td><td style="padding:8px 12px;border:1px solid #cbd5e1">フィニッシャー先制技</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー</td><td style="padding:8px 12px;border:1px solid #cbd5e1">こおり（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン・くさ対策</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">しねんのずつき / クイックターン</td><td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー（物理） / みず（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">エスパータイプ一致 / サイクル維持</td></tr>
</tbody>
</table>
</div>

**強み**  
いじっぱり補正によるA最大化（実A167）+ ちからもちで**実質A334**が実現。アクアブレイク火力指数**42,585**は環境最高水準で、多くの相手を確定2発圏内に収めます。アクアブレイクでBダウンを狙いながら、次ターン以降アクアジェットで先制フィニッシュという黄金パターンが安定して機能します。

M-2環境トップのガブリアスに対してアイススピナーが4倍有効なため、ちからもちの火力と合わせてほぼ確定1発圏内に収まります。すばやさも最大限活かされ、多くの環境ポケモンより速く動けます。

**弱み**  
こうげきへの依存度が高いため、ぼうぎょが高いポケモン（アーマーガア・ハッサム等）には技が通りにくい場面があります。また97.8%メガ石採用のため、メガ進化できない場面（先に他のポケモンがメガ進化した後など）での運用は課題です。ただし**ポケモンチャンピオンズの1メガルールにより、1度の対戦でメガ進化できるのは1体のみ**のため、スターミーをメガ進化させるならパーティの他のポケモンはメガ石を持てない点に注意が必要です。

---

### 型2：ようきAS型（スピード特化）―― 2番目に多い高速物理型

<div class="build-header">
  <span style="background:#6366f1;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：しぜんかいふく（89.7%）</span>
  <span style="background:#059669;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：ようき（24.9%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：A32 S32（53.5%）</span>
</div>

**技構成（例）**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致メイン打点</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）先制</td><td style="padding:8px 12px;border:1px solid #cbd5e1">先制フィニッシャー</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー</td><td style="padding:8px 12px;border:1px solid #cbd5e1">こおり（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・ドラゴン対策</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン / サイコカッター</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理） / エスパー（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">サイクル維持 / エスパータイプ一致</td></tr>
</tbody>
</table>
</div>

**強み**  
いじっぱり型よりもすばやさが高い分、より多くのポケモンに先制できます。特に同族（みずタイプ等）との対面でのスピード勝負を制しやすく、速い環境では安定して上を取れます。こうげきはいじっぱりより下がりますが、メガ進化後の強化されたこうげきがあれば十分な打点が出ます。

**弱み**  
いじっぱりに比べてこうげきが落ちるため、ギリギリのダメージラインで確定1発にならない場面が出てきます。すばやさが元々高いスターミーにとって、ようき補正の恩恵は限定的な場面もあります。

---

### 型3：AS+耐久振り型（HD+AまたはAS+H）

<div class="build-header">
  <span style="background:#6366f1;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">特性：しぜんかいふく（89.7%）</span>
  <span style="background:#dc2626;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">性格：いじっぱり（71.4%）</span>
  <span style="background:#8b5cf6;color:white;padding:4px 10px;border-radius:4px;font-size:0.85rem">EV：HD+A（4.9%）/ AS+H（3.2%）/ AS+B（3.5%）</span>
</div>

**技構成（例）**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">メインウェポン</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td><td style="padding:8px 12px;border:1px solid #cbd5e1">みず（物理）先制</td><td style="padding:8px 12px;border:1px solid #cbd5e1">フィニッシャー</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">アイススピナー / クイックターン</td><td style="padding:8px 12px;border:1px solid #cbd5e1">こおり / みず</td><td style="padding:8px 12px;border:1px solid #cbd5e1">対ドラゴン / サイクル</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">ビルドアップ / こうそくスピン</td><td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう変化 / ノーマル物理</td><td style="padding:8px 12px;border:1px solid #cbd5e1">積み技 / ステロ消去</td></tr>
</tbody>
</table>
</div>

**強み**  
耐久寄りの配分によって特殊技（でんき・くさ等）への耐久を高め、より多くの攻撃を耐えながら反撃できます。ビルドアップ採用型ではこうげきとぼうぎょを両方積めるため、長期戦でも強みを発揮します。こうそくスピン採用型はステロ・まきびしを消去しながらすばやさを上げる追加効果で、後続にも貢献します。

**弱み**  
AS最大化型に比べてこうげきまたはすばやさが落ちるため、火力や速度で劣る場面があります。積む時間を作るための立ち回りが必要で、即効性に欠けます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スターミナイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>97.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ進化で特性ちからもちを得る。実質A200により全物理技が2倍の火力で機能</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいのタスキ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">通常スターミー運用時のHP1耐え保険。メガなし特殊型での採用</td>
</tr>
</tbody>
</table>
</div>

**97.8%というスターミナイト採用率はM-2データの中でも最高水準**です。これは「スターミーを採用する = ちからもちを得るためにメガ進化させる」という認識がほぼ全プレイヤーに共有されていることを意味します。残り0.7%のきあいのタスキは、他のポケモンにメガ石を持たせた場合の通常スターミー運用に相当します。

ちからもちなしの通常スターミーは特殊アタッカー向きの種族値構成であり、物理技を使っても火力が出ません。スターミナイトを手放す理由がほとんどない理由はここにあります。

---

## 97.8%メガ採用率の考察：なぜスターミーはメガ必須なのか

一般的にポケモンチャンピオンズで97.8%のメガ採用率を記録するポケモンは稀です。この数字が示す意味を3つの観点から考察します。

### 1. ちからもちがなければ成立しない火力設計

全採用技が物理技という構成は、ちからもちによる実質A334を前提に設計されています。通常スターミーのこうげき種族値75のままでは、アクアブレイクの火力指数は75×2（Lv50無振り実数値）×85×1.5 ≒ **12,000程度**に過ぎません。ちからもちがあってこそ**42,585**まで引き上がります。

### 2. アクアジェット先制技の価値もちからもちで初めて成立

アクアジェットは基本威力40と低めですが、ちからもち適用で火力指数**20,040**を実現します。通常スターミーのこうげきで使えば指数は**6,000前後**で先制技として非常に非力です。「ちからもちのあるメガスターミーが使うアクアジェット」だからこそフィニッシャーとして機能します。

### 3. すばやさ120との相乗効果

通常スターミーのすばやさ115から、メガ後は120に上昇。**ちからもちによる圧倒的火力 × すばやさ120**の組み合わせが、「上から高火力を押し付ける」というメガスターミーの基本戦術を成立させています。

---

## パーティ構成案

M-1シーズンのスターミー同居率データ（1位：ガブリアス、3位：アーマーガア、4位：ペリッパー、5位：ギルガルド）をもとに、実際の使われ方に即した2パターンを示します。

### パーティ構成案①「ガブリアス軸 バランス型」

スターミーの同居率1位はガブリアス。でんき無効のじめんタイプとして、スターミーの最大の弱点をカバーしながら、ステルスロックで試合全体のダメージ効率を上げる構成です。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主軸</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（スターミナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ちからもち高火力＋クイックターンでサイクルを主導</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき対策・ステロ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき無効・ブリジュラスへじしん打点。ステルスロックでクイックターンのダメージ蓄積を底上げ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理受け・起点作り</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうタイプでくさ耐性・あく耐性。とんぼがえりでスターミーを安全に着地</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">キングシールドで削りを防ぎつつ後出し。スターミーのゴースト弱点への抑止力</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・ゴースト崩し</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スターミーが苦手なゴースト・あく主体の相手に催眠・トリックで崩す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・むし処理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スターミーの弱点・くさ/むしをほのお技で一掃</td>
</tr>
</tbody>
</table>
</div>

**立ち回りの基本：**
1. **アーマーガア**のとんぼがえりorガブリアスのステルスロックで試合の主導権を取る
2. **メガスターミー**がアクアブレイク＋クイックターンで削りとサイクルを両立
3. スターミーが不利な相手（でんき・くさ・あく）はガブリアス・リザードン・ゲンガーで対処

---

### パーティ構成案②「ペリッパー雨展開型」

M-1スターミーの同居率4位はペリッパー。ペリッパーのあめふらしで雨状態を作り、**アクアブレイクの火力を1.5倍**に引き上げる構成です。ちからもちとの組み合わせで火力指数はさらに跳ね上がります。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">雨下エース</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（スターミナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">雨下アクアブレイクがちからもちと合わさり火力指数約63,000超。アクアジェットも雨下1.5倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">天候展開</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0279-00.webp" alt="ペリッパー" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ペリッパー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あめふらしで登場即雨展開。とんぼがえりでスターミーを後ろから安全に着地</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき対策</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき無効・じしんでブリジュラス処理。雨パの天敵・でんきタイプへの最終防衛線</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ペリッパー・スターミーに強い特殊アタッカーを受ける。はがねタイプでくさ半減</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・ゴースト処理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（ルカリオナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう/はがねタイプでスターミーの弱点・あく/ゴーストを補完。バレットパンチで先制</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・むし処理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スターミー・ペリッパーが弱いくさタイプを牽制。はがねタイプでフェアリーも半減</td>
</tr>
</tbody>
</table>
</div>

**立ち回りの基本：**
1. **ペリッパー**を先発してとんぼがえりで雨を維持しながらスターミーを着地
2. 雨下の**メガスターミー**がアクアブレイクで一撃圏内を広げてクイックターンでサイクルを回す
3. でんきタイプにはガブリアスを、あく・ゴーストにはルカリオを当てて補完

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
  <th style="padding:8px 6px;border:1px solid #cbd5e1">先制技</th>
  <th style="padding:8px 6px;border:1px solid #cbd5e1">サイクル</th>
  <th style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">向いている場面</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">いじっぱりAS</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★☆☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">環境標準・火力重視の汎用型</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">ようきAS</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★☆☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">高速環境・スピード勝負重視</td>
</tr>
<tr>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">AS+耐久振り</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">特殊攻撃が多い環境・安定重視</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">ビルドアップ型</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★★</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★☆☆</td>
  <td style="padding:8px;border:1px solid #cbd5e1">★★★★☆</td>
  <td style="padding:8px 10px;border:1px solid #cbd5e1;text-align:left">長期戦・積み展開向き</td>
</tr>
</tbody>
</table>
</div>

---

## M-2シングル環境でのメガスターミーの位置づけ

使用率20位という順位だけ見ると「環境の外縁」に見えますが、メガスターミーの本質的な価値は使用率以上のものがあります。

### ガブリアス（1位）へのメタとして機能

M-2環境トップのガブリアスに対して、アイススピナーで4倍有効打を取れるのはメガスターミーの重要な価値です。ただしアイススピナーで先手を取れれば確実にガブリアスを処理できるため、ガブリアス対策カードとしての採用価値があります。

### みずタイプの中での独自性

M-2環境にはみずタイプのポケモンが複数います（アシレーヌ4位・ギャラドス10位・スターミー20位）。アシレーヌが特殊みずアタッカーとしての地位を確立する中、メガスターミーは**ちからもちによる突出した物理火力**でその差別化を図っています。

### クイックターンによるサイクル貢献

クイックターン53.6%という採用率は、メガスターミーがアタッカーとしての役割だけでなく**サイクル構築のパーツ**としても機能することを示しています。攻撃しながら交代するみずタイプのUターンは、相手に情報を与えながら有利なポケモンを後ろから出す「崩し起点」として機能します。特にステロ展開と組み合わせることで、相手の体力を削りながらサイクルを回せます。

---

## 対メガスターミーの立ち回り指針

メガスターミーを使う側だけでなく、**対面する側の視点**も把握しておくことで戦術の幅が広がります。

### 対策の基本方針

1. **でんき技で弱点を突く** — ブリジュラス等のでんき技が2倍。ただしブリジュラスはS120のメガスターミーより遅いため、サイクル中の後出しから技を通すのが基本
2. **ゴースト・あくタイプで崩す** — エスパータイプへのゴースト・あく技が2倍。ゲンガー（12位）・キラフロル（13位）・ギルガルド（16位）が有効
3. **くさタイプで圧力をかける** — マスカーニャ（3位）などのくさ技が2倍。ただしアイススピナーに注意
4. **ぼうぎょが高いポケモンで受ける** — アーマーガア・ハッサムなどBが高いポケモンは物理技の通りが悪い

### 注意点：アクアジェット先制を忘れずに

対面でメガスターミーを削れたとしても、アクアジェットで先制されるリスクを常に意識する必要があります。87.2%という採用率は事実上の必須技であり、「削れたら先制で仕留められる」と想定して動くことが重要です。

---

## まとめ

メガスターミーの本質は**特性ちからもちによる実質A334の圧倒的物理火力**です。アクアブレイク火力指数42,585はTier1環境で最高水準であり、すばやさ120との組み合わせが「上から高火力を押し付ける」という強力な攻め方を可能にします。

97.8%というほぼ全員がメガ石を採用する事実は、「ちからもちなしのスターミーに採用価値はない」という環境の総意です。いじっぱりAS型でアクアブレイク+アクアジェット+アイススピナーの3本柱を持ちつつ、クイックターンかしねんのずつきを選択するのが現環境のスタンダードです。

でんき・くさ・あく・ゴーストへの対策をパートナーに任せながら、ちからもちの火力でM-2環境上位を削っていくスタイルがメガスターミーの基本となります。

---

## 関連考察記事

- [【ポケモンチャンピオンズ】ガブリアス徹底考察 M-2シーズン使用率1位](/blog/garchomp-analysis-m2/)
- [【ポケモンチャンピオンズ】メガフラエッテ徹底考察 M-2シーズン](/blog/florette-analysis-m2/)
