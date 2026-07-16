---
title: 'アシレーヌ考察 M-3 使用率14位の採用理由と型別立ち回り'
description: 'チャンピオンズM-3使用率14位（M-2の4位から下落）のアシレーヌを徹底解説。ムーンフォース96.9%・うたかたのアリア84.4%・アクアジェット69.2%の技構成データ、オボン58.0%主体の持ち物変化、H32-C32-S2ひかえめ型の実数値と立ち回りを解説します。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-primarina-m3.png'
draft: false
---

<style>
.poke-header { display:flex; align-items:center; gap:16px; margin:20px 0; }
.poke-header img { width:96px; height:96px; }
.build-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.partner-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(120px,1fr)); gap:12px; margin:16px 0; }
.partner-card { text-align:center; padding:8px; border:1px solid #e2e8f0; border-radius:8px; }
.partner-card img { width:56px; height:56px; display:block; margin:0 auto 4px; }
.partner-card .name { font-size:0.75rem; font-weight:bold; }
.partner-card .rate { font-size:0.7rem; color:#666; }
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
  <div>
    <h2 style="margin:0 0 8px">アシレーヌ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">14位</strong>　特性: <strong>げきりゅう 92.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-3シーズンのデータです。M-2版は[アシレーヌ考察 M-2](/blog/primarina-analysis-m2/)をご覧ください。

シーズンM-3のシングルバトルでアシレーヌは**使用率14位**。M-2の4位から大幅に下落しましたが、みず/フェアリーという二刀流の打点とアクアジェットによる先制技を持ち、環境上位のガブリアス・リザードン・ドラゴン系への有効打として採用価値を保っています。持ち物はオボンのみ58.0%が主流で、M-2の46.6%からさらに集中が進みました。

---

## データ分析①：M-2→M-3の採用率変化

### 技採用率（M-2比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">97.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>96.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">-0.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>うたかたのアリア</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">79.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>84.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">66.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>69.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>41.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>28.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なみのり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エナジーボール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミストフィールド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.8pp</td>
</tr>
</tbody>
</table>
</div>

M-3で最も目立つ変化は**うたかたのアリア+5.2pp（84.4%）**と**クイックターン-5.7pp（24.6%）**の入れ替えです。うたかたのアリアは威力90のタイプ一致みず技で、同じみず特殊技のなみのり（威力90）と重複しますが、なみのりが全体技（味方を巻き込む）であるのに対し、うたかたのアリアは音技で特定の特性（防音等）に引っかかりません。M-3でなみのりも-5.7ppと下落しており、みず技はうたかたのアリア1択に収束しつつあります。

**エナジーボール（くさ・威力90）の新台頭（8.0%）**は、メガラグラージ（みず/じめん）への打点（くさ×4）として意識されたものと考えられます。

### 持ち物採用率（M-2比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">58.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+11.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+0.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんぴのしずく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようせいのハネ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.9pp</td>
</tr>
</tbody>
</table>
</div>

**オボンのみが+11.4pp（58.0%）**と大幅に集中したのがM-3の最大変化です。M-2でみず技の火力を底上げしていたしんぴのしずく（みずタイプ技×1.2）が-6.7ppに落ち込んだ分が、そのままオボンへ移行した形です。HPが半分以下になった時にHPの1/4を回復するオボンのみは、C126の高い特殊火力を維持しながら対面での安定性を確保できます。めいそう（+2.3pp）の採用増加と合わせると、「積んで場持ちする」方向への移行が読み取れます。

---

## EV・性格

### 性格

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひかえめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">70.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう↑ こうげき↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ こうげき↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ すばやさ↓</td>
</tr>
</tbody>
</table>
</div>

**ひかえめ（70.3%）**が主流。C126の高い特殊攻撃力をさらに1.1倍に伸ばし、ムーンフォースとうたかたのアリアの打点を最大化します。**ずぶとい（10.0%）**はB94をB121に引き上げて物理方向の耐久を確保する型で、めいそうと組み合わせた積み耐久を意識した配分です。

### EV配分

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-C32-S2</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">13.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくこう全振り、S最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B2-C32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくこう全振り、B最小調整</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-C32-D2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくこう全振り、D最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H2-C32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう・すばやさ全振り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B32-C2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ全振り（ずぶとい型）</td>
</tr>
</tbody>
</table>
</div>

EVの分布が分散しているのはアシレーヌの特徴で、「H32+C32」を軸にした耐久火力重視型が上位3種を占めています。最多の**H32-C32-S2（13.4%）**でも採用率は低く、環境全体でEV配分の正解が収束しきっていないことを示しています。

### 代表型の実数値（H32-C32-S2・ひかえめ）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">実数値</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>171</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき（ひかえめ↓）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう（ひかえめ↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>178</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">136</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">82</td>
</tr>
</tbody>
</table>
</div>

---

## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりゅう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">92.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うるおいボイス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.4%</td>
</tr>
</tbody>
</table>
</div>

**げきりゅう**はHPが1/3以下になった時にみず技の威力が1.5倍になる特性。アクアジェット（威力40）の瀕死ライン発動を意識するより、HPが削られた状態でのうたかたのアリア（威力90）の爆発力を活かす場面で機能します。**うるおいボイス（7.4%）**は音技をみずタイプに変換する特性で、うたかたのアリアがみず技として受けられると同時に一致補正になります（音技であることに変化はないため変化技には適用されない）。採用率が7.4%と少数のため、対面では基本的にげきりゅうとして扱います。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">126</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">116</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

とくこう126・とくぼう116と特殊面に特化した種族値配分。一方でこうげき74・すばやさ60と物理と素早さは低く、アクアジェット（優先度+1の先制技）を経由しなければS60の素のすばやさで後手を取りやすい点が立ち回りの制約になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

弱点はくさ・でんき・どくの3つ（いずれも×2）。環境上位のマスカーニャ（3位）のトリックフラワー（くさ×2・採用率98.2%）とライチュウ（6位）のくさむすび（くさ×2・採用率73.2%）がそれぞれ弱点を突いてきます。ドラゴン技無効は環境のドラゴン技持ちポケモンに対して有利に働きます。

---

## 主な型

### 型1：オボン耐久型（58.0%）

HP171・C178（ひかえめC32）の火力を維持しながらオボンのみの回復で場持ちを確保する主力型。めいそう（28.5%）や先制技のアクアジェット（69.2%）と組み合わせて、後手に回る素早さを補いながら対面を制します。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>オボン耐久型（主流）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>げきりゅう（92.6%）<br>
    <strong>性格：</strong>ひかえめ　<strong>EV：</strong>H32-C32-S2<br>
    <strong>持ち物：</strong>オボンのみ<br>
    H171 / B94 / C178 / D136 / S81
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成：</strong>ムーンフォース / うたかたのアリア / アクアジェット / アンコール（めいそう）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    ムーンフォース（フェアリー・威力95）とうたかたのアリア（みず・威力90）で二方向の打点を確保。アクアジェット（みず・威力40・優先度+1）でS60の遅さをカバーし、削れた相手を先制で処理します。アンコールは相手の補助技・積み技に合わせて縛り、めいそうはC・Dを1段階ずつ上げて継続戦力を高めます。
  </p>
</div>

### 型2：たべのこし積み型（15.9%）

毎ターンHP1/16を回復するたべのこしを持ち、めいそうを積みながら長期戦を制する型。ひかえめ型と比較して瞬間の回復量は小さいものの、複数ターンにわたって継続的に回復できる点が違いです。相手の特殊攻撃をD136で受けながらめいそうで特殊耐久を積み上げる運用に適しています。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>たべのこし積み型</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>げきりゅう（92.6%）<br>
    <strong>性格：</strong>ひかえめ（ずぶとい）　<strong>EV：</strong>H32-C32-S2<br>
    <strong>持ち物：</strong>たべのこし<br>
    H171 / B94 / C178 / D136 / S81
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成：</strong>ムーンフォース / うたかたのアリア / めいそう / アクアジェット（アンコール）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    オボン型と比べて一発の回復量では劣りますが、毎ターン自動回復するためめいそう積みと相性が良く、積む時間を稼ぎやすい利点があります。ずぶとい型（EV H32-B32-C2）ではぼうぎょをB121に上げ、物理攻撃もめいそう無しで受けやすくなります。
  </p>
</div>

---

## 苦手なポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・採用率98.2%）が×2弱点。S60のアシレーヌはほぼ確実に後手を取り、先に高火力くさ技を受けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび（くさ・採用率73.2%）でくさ×2、きあいだま（かくとう・採用率95.0%）は×0.5と通りにくいが、くさむすびで先手から弱点を突かれます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・採用率49.6%）で×2弱点。ラスターカノン（はがね・採用率74.6%）はアシレーヌに等倍ですが、でんき技を半数が採用しており対面では弱点を突かれるリスクがあります</td>
</tr>
</tbody>
</table>
</div>

---

## パートナー（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居9位</div>
  </div>
</div>

**ガブリアス（同居1位）**はドラゴン/じめんで、じしん・げきりんによる物理打点とアシレーヌのフェアリー・みず打点で技範囲が広く補い合います。ガブリアスが呼ぶこおり・みず・フェアリー技をアシレーヌが受けやすい場面もあり、サイクル構成として機能します。

**メタグロス（同居2位）**ははがね/エスパーで、アシレーヌが弱点を持つどく技をはがね耐性で受けられます。アシレーヌのフェアリー打点でドラゴン・あくタイプを処理し、メタグロスの物理打点で役割を分担する構成です。

**マスカーニャ（同居3位）**はくさ/あくで、くさ×4のメガラグラージや環境上位のじめんタイプへのくさ打点を持ちます。アシレーヌのフェアリー・みず打点と合わせて幅広いタイプへの対応が揃います。

---

## まとめ

M-3のアシレーヌはM-2の4位から14位へ下落しましたが、みず/フェアリーの二刀流打点とアクアジェットによる先制は引き続き採用価値を持っています。

- **オボンのみ58.0%（+11.4pp）**が主流として定着し、しんぴのしずくから耐久方向へシフト
- **うたかたのアリア84.4%（+5.2pp）**でみず技がほぼ一択に収束
- **エナジーボール8.0%が新台頭**（メガラグラージ対策・くさ×4）
- **H32-C32の耐久火力重視型**がEV配分の中心

S60の低い素早さがアクアジェット無しでは後手になりやすい制約は変わらず、マスカーニャ（3位）のトリックフラワー・ライチュウ（6位）のくさむすびといったくさ弱点技持ちへの対応はパーティ単位で別途用意が必要です。

---

*関連記事：[ガブリアス考察 M-3](/blog/garchomp-analysis-m3/) / [ミミッキュ考察 M-3](/blog/mimikyu-analysis-m3/)*
