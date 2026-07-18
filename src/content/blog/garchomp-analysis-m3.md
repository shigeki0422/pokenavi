---
title: 'ガブリアス考察 M-3 まきびし台頭・スカーフ減少の変化点を解説'
description: 'チャンピオンズM-3使用率1位ガブリアスを徹底解説。まきびし14.2%の新登場・スカーフ26.7%（-6.3pp）・オボン19.5%（+3.6pp）の持ち物変化をデータで解説。H2-A32-S32ようき型の実数値・苦手な相手・パーティ構成まで紹介します。'
updatedDate: '2026-07-18'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-garchomp-m3.png'
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
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
  <div>
    <h2 style="margin:0 0 8px">ガブリアス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">1位</strong>　特性: <strong>さめはだ 99.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-3シーズンのデータです。M-2版は[ガブリアス考察 M-2](/blog/garchomp-analysis-m2/)をご覧ください。

シーズンM-3のシングルバトルで、ガブリアスは**使用率1位**（M-2から連続）。すばやさ102・こうげき130の攻守バランスとじしんの圧倒的な制圧力を軸に、タスキ・スカーフ・オボンといった多彩な持ち物で幅広い役割をこなす環境の中心です。M-3では**スカーフが33.0%→26.7%に減少**し、**オボンが15.9%→19.5%に増加**。また**まきびしが14.2%で新たに台頭**するなど、持ち物・技構成の分布に変化が出ています。

---

## M-3の採用率変化まとめ

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">99.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>99.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>36.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>31.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>23.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まきびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>14.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">圏外</td>
</tr>
</tbody>
</table>
</div>

最大の変化は**まきびし14.2%の新登場**と**ほのおのキバの圏外消滅**です。まきびしは相手の交代時に蓄積するダメージ設置技で、ステルスロックと合わせて「ダブル設置ガブリアス」の構成が生まれています。ほのおのキバはM-2でハッサム（はがね/むし）対策として採用されていましたが、M-3でハッサム（32位）の順位が下がったことが影響していると考えられます。

**つるぎのまい+3.9pp**の上昇は積み型志向の強まりで、ドドゲザン（24位）と同様のトレンドです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいのタスキ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">38.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こだわりスカーフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>26.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>19.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
</tbody>
</table>
</div>

こだわりスカーフ-6.3ppが最大の持ち物変化です。スカーフはすばやさを1.5倍にする代わりに1技固定になるため、まきびし・ステルスロック等の設置技と共存できません。まきびしの採用増加に伴い、複数の技を柔軟に使えるタスキ・オボン型が相対的に増えた結果と一致します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ようき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ とくこう↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

**ようき（59.0%）**が主流で、すばやさを最大化して多くの環境ポケモンに先手を確保します。**わんぱく（13.2%）**はH32-B振り型の物理受け構成に対応しており、ようき・いじっぱりとは運用が異なります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H2-A32-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り+HP最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B25-S9</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ重視型（わんぱく）</td>
</tr>
</tbody>
</table>
</div>

**H2-A32-S32（56.5%）**が標準配分として定着しています。HP2ポイント振ることでHP実数値が183→185と奇数になり、定数ダメージの回数調整に使われます。

### 代表型の実数値（H2-A32-S32・ようき）

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>185</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき（ようき 中立）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>182</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">115</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう（ようき↓）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">105</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ（ようき↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>169</strong></td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>さめはだ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.2%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すながくれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.8%</td>
</tr>
</tbody>
</table>
</div>

**さめはだ**は接触技を受けたとき、攻撃してきた相手のHPを最大HPの1/8削る特性。こうげき130のガブリアスに接触技を当てるリスクを高め、特に物理アタッカーのダメージレースで優位を取れます。採用率99.2%で実質固定。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">108</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">102</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

HP108・こうげき130・すばやさ102と攻撃・速さ・耐久の三拍子が揃った高種族値。すばやさ102はようきS32で実数値169となり、環境上位の多くに先手を確保できます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">免疫</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

**こおり×4**が最大の穴（ドラゴン2倍×じめん2倍）。環境にはアローラキュウコン（13位）・ゲッコウガ（31位）などこおり技の高採用率ポケモンが複数おり、対面すると一撃で落ちます。フェアリー×2はミミッキュ（2位）・アシレーヌ（15位）・クチート（25位）のじゃれつく・ムーンフォースが刺さります。一方でんき技を無効化できるため、ライチュウ（5位）のでんき技を透かせる点が強みです。

---

## 主な型

### 型1：きあいのタスキ型（38.7%）

一撃で落とされる弱点をタスキで保証し、設置技（ステルスロック・まきびし）＋攻撃技で幅広く動ける主力型。リード役として先発に置きやすく、こおり×4弱点でも初手の設置を確実に行えます。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>タスキ型（設置+攻撃）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>さめはだ（99.2%）<br>
    <strong>性格：</strong>ようき　<strong>EV：</strong>H2-A32-S32<br>
    <strong>持ち物：</strong>きあいのタスキ<br>
    H185 / A182 / B115 / D105 / S169
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>じしん / ステルスロック（まきびし）/ げきりん（がんせきふうじ）/ どくづき
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    初手で設置技を決めてから攻撃技で削る流れ。こおり技でタスキが割れても最低1ターン確保できるため、設置失敗を防ぎやすい。どくづき（採用率16.7%）はフェアリータイプへの打点（×2）として採用されます。
  </p>
</div>

### 型2：こだわりスカーフ型（26.7%）

すばやさを1.5倍にして環境最速クラスの先制を確保する型。ようきS32の実数値169がさらに×1.5倍になるため、大半の環境ポケモンを上回れます。技が1種に固定されるため、設置技との併用はできません。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>スカーフ型（最速アタッカー）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>さめはだ（99.2%）<br>
    <strong>性格：</strong>ようき　<strong>EV：</strong>A32-S32<br>
    <strong>持ち物：</strong>こだわりスカーフ<br>
    H183 / A182 / S169（スカーフ補正後）
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>じしん / げきりん / スケイルショット / がんせきふうじ
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    じしん固定で多くの相手を先手で圧倒します。げきりんはドラゴン技として最高打点ですが、使用後は2〜3ターンの混乱確定。スケイルショットは多段技で連続攻撃できますが、ミミッキュのばけのかわを崩した後の打点にも使えます。
  </p>
</div>

### 型3：オボンのみ型（19.5%）

HP半減時にHPを回復するオボンのみで、こおり×4弱点でもワンパン耐えから反撃できる耐久型。設置技と攻撃技を組み合わせた自由度の高い構成が可能です。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>オボン型（耐久+設置）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>さめはだ（99.2%）<br>
    <strong>性格：</strong>ようき（いじっぱり）　<strong>EV：</strong>H2-A32-S32<br>
    <strong>持ち物：</strong>オボンのみ
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>じしん / ステルスロック / まきびし / げきりん（スケイルショット）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    タスキと異なりHPが残った状態での戦闘継続が強み。オボン発動後もさめはだで相手の接触技を削りながら立ち回れます。ステルスロック+まきびしのダブル設置を狙う構成にも使われます。
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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ばけのかわで初手1発を無効化しつつ、じゃれつく（採用率95.4%）でフェアリー×2を確実に当ててくる。タスキを持たせても相手のばけのかわが壁になり、一撃での処理が難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ（84.9%）・ふぶき（74.2%）のこおり×4弱点技をほぼ確実に持つ。すばやさも高く、先手でこおり技を撃たれるとタスキ以外では即倒</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（96.9%）でフェアリー×2。特殊技のためさめはだは無効。ガブリアスのじしんはみず/フェアリーのアシレーヌに等倍止まりで削りにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ（31位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ122でガブリアスより速く、れいとうビーム（88.6%）でこおり×4弱点を先手で突いてくる。スカーフなしでは対面不利</td>
</tr>
</tbody>
</table>
</div>

---

## パートナー（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">共演1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">共演2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">共演3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">共演4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">共演5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">共演6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" loading="lazy">
    <div class="name">ムクホーク</div>
    <div class="rate">共演7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">共演8位</div>
  </div>
</div>

**ミミッキュ（1位）**はガブリアスの苦手なフェアリー技を持つが、同居率トップはミミッキュへの対策をパーティ側で持つのではなく、選出を分ける形で同時採用されているためです。ミミッキュのばけのかわと奇襲性でガブリアスが苦手な相手を倒してもらい、ガブリアスが受けで動く役割分担になります。

**ブリジュラス（3位）**ははがね/ドラゴンタイプでフェアリー技を等倍で受けつつ、ガブリアスが苦手なミミッキュ・アシレーヌへの牽制役として機能します。ブリジュラスにドラゴン技が刺さる相手をガブリアスのじしんが処理する補完関係です。

**メタグロス（5位）**ははがね/エスパーで、ガブリアスのこおり×4弱点を突くアローラキュウコンへのはがね技（アイアンヘッド等）が刺さります。ガブリアスのじしんがメタグロスに×2で通るため、二体で広い範囲を圧倒できます。

**アーマーガア（8位）**はひこう/はがねでガブリアスのじしんが無効。選出した際にじしんを気にせず動けるため、対戦中の技選択の自由度が上がります。

---

## まとめ

M-3のガブリアスは使用率1位を維持しながら、持ち物・技構成の分布が変化したシーズンです。

- タスキ38.7%（横ばい）が主力維持
- スカーフ26.7%（-6.3pp）が減少、オボン19.5%（+3.6pp）が増加
- まきびし14.2%が新台頭（ステルスロックと組み合わせたダブル設置型）
- ほのおのキバが圏外消滅（ハッサム対策需要の低下）

じしん99.5%の安定した一致技と、すばやさ169（ようきS32）で多くの環境ポケモンに先手を確保できる基本性能は変わりません。こおり×4弱点とフェアリー×2弱点への対策をパーティ単位で用意することが、ガブリアスを活かす上での最大の課題です。
