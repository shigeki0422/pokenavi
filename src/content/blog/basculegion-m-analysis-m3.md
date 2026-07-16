---
title: '【ポケモンチャンピオンズ】イダイトウ(オス)考察 M-3 使用率16位 スカーフおはかまいり型の採用理由'
description: 'M-3シングルバトルで使用率16位のイダイトウ(オス)を徹底分析。こだわりスカーフ74.1%・てきおうりょく93.0%・おはかまいり99.9%の採用実態をDBデータで解説。H2-A32-S32ようき型の実数値・4枠目分散の意味・同居率上位考察も掲載。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-basculegion-m-m3.png'
draft: true
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
  <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" />
  <div>
    <h2 style="margin:0 0 8px">イダイトウ(オス)</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">16位</strong>　特性: <strong>てきおうりょく 93.0%</strong>
    </div>
  </div>
</div>

> 本記事はM-3シーズンのデータです。M-2シーズンはDBにイダイトウ(オス)のデータが取得されていないため、シーズン比較は掲載しません。

M-3シングルバトルでイダイトウ(オス)は**使用率16位**。最多持ち物はこだわりスカーフ74.1%と突出しており、特性てきおうりょく93.0%・技おはかまいり99.9%を組み合わせた**スカーフおはかまいり型**が環境での主要な採用理由です。

おはかまいりは手持ちのポケモンがひんしになるたびに威力が50上がるゴースト物理技（基礎威力50）。てきおうりょくにより一致技の火力補正が通常の1.5倍から2.0倍に上がるため、ひんし数が増えるほど実質威力が急増します。ひんし0体でも実質威力100（50×2.0）、ひんし2体で実質威力300（150×2.0）と、試合後半になるほど攻撃力が跳ね上がる構造です。

---

## M-3 採用率データ

### 技採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おはかまいり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50〜300</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウェーブタックル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>94.5%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>86.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコファング</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.0%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">もろはのずつき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">150</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.6%</td>
</tr>
</tbody>
</table>
</div>

3枠は「おはかまいり・ウェーブタックル・アクアジェット」でほぼ固定。4枠目はサイコファング（6.0%）・こおりのキバ（5.5%）・アクアブレイク（3.9%）・もろはのずつき（3.6%）と採用率が分散しており、いずれも10%未満です。どの技を採用するかはパーティの苦手な相手によって変わる選択枠であり、4枠目の採用データだけで「この技が主流」とは言えない構造になっています。

### 持ち物採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/items/item-0287-scarf.png" alt="こだわりスカーフ" style="width:24px;height:24px;vertical-align:middle;margin-right:6px"><strong>こだわりスカーフ</strong>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">74.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/items/item-0275-tasuki.png" alt="きあいのタスキ" style="width:24px;height:24px;vertical-align:middle;margin-right:6px">きあいのタスキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span style="display:inline-block;width:24px;height:24px;background-image:url('/images/items/item-sprite.png');background-size:480px 648px;background-position:0px -192px;flex-shrink:0;vertical-align:middle;margin-right:6px"></span>いのちのたま
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.3%</td>
</tr>
</tbody>
</table>
</div>

こだわりスカーフが74.1%と圧倒的多数派。残り26%をきあいのタスキ（8.1%）・いのちのたま（7.3%）で分け合っています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">69.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

ようき（69.2%）が主流で、スカーフS実数値を最大化する構成が多数派です。いじっぱり（27.3%）はA実数値180まで伸ばしてスカーフなし・タスキ・いのちのたまと組み合わせる構成が中心と推測されます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP最小調整・A最大・S最大</td>
</tr>
</tbody>
</table>
</div>

A32-S32の全振りベースが大多数を占め、H2の余り振りが最多構成です。火力とSの確保を最優先とした配分で、耐久方向への投資はほぼ見られません。

### 代表型の実数値（H2-A32-S32・ようき）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">実数値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>197</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>164</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき中立</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき↓補正</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>143</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ時214</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てきおうりょく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">93.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すいすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.8%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かたやぶり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.3%</td>
</tr>
</tbody>
</table>
</div>

**てきおうりょく**は自分のタイプと一致する技の威力補正を通常の1.5倍から2.0倍に引き上げる特性。おはかまいり（ゴースト）・ウェーブタックル（みず）・アクアジェット（みず）のいずれにも乗り、スカーフと合わせて全一致技が2.0倍補正で動きます。採用率93.0%で実質固定です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">112</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
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
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

HP120は高水準ですが、ぼうぎょ65・とくぼう75は平均以下。攻撃重視の耐久で、被弾を想定した耐久型よりアタッカー運用に向いた配分です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">免疫</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

みず/ゴースト複合の特徴的な免疫構成で、ノーマルとかくとうを完全に無効にします。かくとう技を使う環境上位ポケモン（バシャーモ・ムクホーク等）に対して技を透かせる点は立ち回りの選択肢になります。

×2弱点はくさ・でんき・ゴースト・あくの4タイプ。環境上位ではライチュウ（6位）のくさむすび（くさ×2、採用率73.2%）・ボルトチェンジ（でんき×2、採用率29.2%）と、ミミッキュ（2位）のゴースト技（シャドークロー等）が主な弱点該当技です。

---

## 主な型

### 型1：スカーフてきおうりょく型（74.1%）

環境最多構成。スカーフでS214まで引き上げ、てきおうりょく補正のおはかまいりとウェーブタックルの択で相手に圧力をかけます。アクアジェットはスカーフ状態でも優先度+1で先手が取れるため、先手技を持つポケモンへの保険になります。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>スカーフてきおうりょく型</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>てきおうりょく（93.0%）<br>
    <strong>性格：</strong>ようき　<strong>EV：</strong>H2-A32-S32<br>
    <strong>持ち物：</strong>こだわりスカーフ<br>
    H197 / A164 / B85 / C90 / D95 / S143（スカーフ時S214）
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>おはかまいり / ウェーブタックル / アクアジェット / （サイコファング・こおりのキバ等から選択）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    こだわりスカーフにより技を固定してしまうため、選出時点でその試合に必要な技を1つ決める必要があります。おはかまいりで通せる相手には積極的に打ち、ゴーストが半減・無効の相手にはウェーブタックルに切り替えます。
  </p>
</div>

### 型2：きあいのタスキ型（8.1%）

HPを1残して耐える動きで、1発被弾後のアクアジェット優先度による切り返しを保証する型。スカーフ不採用のためSは143どまりですが、タスキで耐えてアクアジェットの優先度+1で後手から削りに行ける展開に特化しています。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>きあいのタスキ型</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>てきおうりょく（93.0%）<br>
    <strong>性格：</strong>いじっぱり　<strong>EV：</strong>A32-S32<br>
    <strong>持ち物：</strong>きあいのタスキ<br>
    H195 / A180 / B85 / C90 / D95 / S130
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>おはかまいり / ウェーブタックル / アクアジェット / （選択）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    タスキが一回限りの性質上、先発か相手の先手技が確実な場面での切り返しに向きます。いじっぱりA180で火力を補い、スカーフなしのS130で動くため速度優位は限定的です。
  </p>
</div>

---

## データ分析①：4枠目の分散が意味すること

おはかまいり（99.9%）・ウェーブタックル（94.5%）・アクアジェット（86.1%）の3枠は固定に近い一方、**4枠目はサイコファング6.0%・こおりのキバ5.5%・アクアブレイク3.9%・もろはのずつき3.6%と10%未満に分散**しています。

この分散は「4枠目に標準解が存在しない」ことを示しています。各採用技のカバレッジ対象は以下のとおりです。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">主なカバレッジ先</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコファング</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく複合（ゲンガー等）へのエスパー打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・ドラゴン複合へのこおり打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">反動なしのみず技（ウェーブタックルの代替）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">もろはのずつき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">反動ありの高威力いわ技</td>
</tr>
</tbody>
</table>
</div>

どの技を選ぶかはパーティ全体の弱点に応じて変わるため、イダイトウを採用するときは3枠固定を前提に、パーティが苦手な相手への打点を4枠目で補う設計になっています。

---

## データ分析②：スカーフS214で先手を取れる相手・取れない相手

こだわりスカーフ採用時のS実数値は214。この速度でどこまで先手を取れるかを整理します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">素のS実数値（最速）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">スカーフS</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">スカーフ採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">イダイトウ（S214）との比較</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャ（3位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">192</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">288</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">多数派（スカーフ）には先手を取れない。無スカーフ（S192）には先手を取れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">169</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">253</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無スカーフ多数派（S169）には先手を取れる。スカーフ個体（S253）には先手を取れない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ライチュウ（6位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">178</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフS214で先手を取れるが、くさむすびをくさ×2で受けてしまう（採用率73.2%）。きあいだまはかくとう無効で透かせる</td>
</tr>
</tbody>
</table>
</div>

マスカーニャはスカーフ採用率70.8%と多数派がスカーフ持ちです。くさ×2弱点のトリックフラワーをS288で先に受けると即戦闘不能圏になるため、マスカーニャへの速度優位は多数派に対して成立しません。ガブリアスはスカーフ23.5%と少数派のため、素のS169に対してはスカーフS214で先手を取れます。

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
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすびをくさ×2で受ける（採用率73.2%）。きあいだまはかくとう無効で透かせるが、主力のくさ技が刺さるため対面では不利。ボルトチェンジ（でんき×2）の採用率は29.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト×2弱点。ばけのかわにより初手のおはかまいりが確定1発にならず、返しのゴースト技（シャドークロー等）で×2を受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ×2弱点。スカーフ採用率70.8%（S288）の多数派に対して先手を取れず、トリックフラワー×2で即戦闘不能圏</td>
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
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" loading="lazy">
    <div class="name">ムクホーク</div>
    <div class="rate">同居5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居10位</div>
  </div>
</div>

**ガブリアス（1位）**はじめん/ドラゴンの物理エースで、イダイトウがカバーしにくいでんきを無効化できます。イダイトウのみず/ゴーストとタイプ攻撃範囲が重なりにくいため、パーティの攻撃カバレッジを広げやすい組み合わせです。

**ブリジュラス（2位）**ははがね/ドラゴン複合でフェアリーに対してドラゴン技・はがね技を使えます。イダイトウが免疫を持つノーマル・かくとうを苦にしないため、両者の苦手範囲が重なりにくいのが同居の理由です。

**ムクホーク（5位）**はかくとう技とひこう技の二刀流アタッカーです。イダイトウがかくとう免疫で透かせる相手を別枠で処理しつつ、ムクホークが苦手なでんき・いわ方面はイダイトウのみず技で補う形が成立します。

**アーマーガア（9位）**はひこう/はがね耐久型で、イダイトウが苦手なくさを大幅に軽減できます（でんきはアーマーガア自身も弱点のため補完になりません）。

---

## まとめ

M-3のイダイトウ(オス)は使用率16位で、こだわりスカーフ74.1%・てきおうりょく93.0%・おはかまいり99.9%という高い集約度で型が固まっています。

- こだわりスカーフ + ようきH2-A32-S32でS214を確保し、環境上位の多くに速度優位を確立
- てきおうりょくによりおはかまいり・ウェーブタックル・アクアジェットの全一致技が2.0倍補正で動く
- おはかまいりはひんし数に応じて実質威力が非線形にスケールするため、試合後半での爆発力が採用理由
- ノーマル・かくとう免疫のみず/ゴースト複合でバシャーモ・ムクホーク系の技を無効化できる

くさ×2・でんき×2・ゴースト×2・あく×2の4弱点と、こだわりによる技固定が主な運用上の制約です。マスカーニャ（スカーフ70.8%）への速度優位は多数派に対して成立しない点に注意が必要です。

---

## 関連記事

- [ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)
- [ミミッキュ考察 M-3](/blog/mimikyu-analysis-m3/)
