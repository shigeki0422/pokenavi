---
title: 'ドドゲザン考察 M-3 くろいメガネ分散・つるぎのまい採用率上昇の変化点'
description: 'チャンピオンズM-3使用率24位ドドゲザンを徹底解説。くろいメガネ53.2%・いのちのたま15.3%へ持ち物が分散し、つるぎのまい77.3%が定着。H32-A32-S2いじっぱり型の実数値・かわらわり急増の背景・パーティ構成をデータで解説。'
updatedDate: '2026-07-18'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-kingambit-m3.png'
draft: false
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
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" />
  <div>
    <h2 style="margin:0 0 8px">ドドゲザン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">24位</strong>　特性: <strong>そうだいしょう 86.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-3シーズンのデータです。M-2版は[ドドゲザン考察 M-2](/blog/kingambit-analysis-m2/)をご覧ください。

シーズンM-3のシングルバトルで、ドドゲザンは**使用率24位**（M-2と同順位）。あく/はがねの耐性複合と特性**そうだいしょう**（86.7%）を軸に、つるぎのまい積み＋ふいうち先制で詰める物理アタッカーとしての立ち位置はM-2から変わっていません。M-3では**くろいメガネの採用率が66.1%→53.2%に低下**し、いのちのたまが15.3%で新たに台頭。また**つるぎのまいが72.3%→77.3%**、**かわらわりが3.4%→10.3%**に増加するなど、技構成にも変化が見られます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">99.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>99.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドゲザン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>95.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.4pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">86.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>90.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>77.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かわらわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>10.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>けたぐり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>10.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハサミギロチン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.7pp</td>
</tr>
</tbody>
</table>
</div>

**かわらわり+6.9pp・けたぐり-7.5pp**の入れ替わりが最大の変化点です。かわらわりはひかりのかべ・リフレクターを破壊しながら攻撃できるかくとう技で、M-3でオーロンゲ（20位）やカバルドン（10位）など展開補助役の使用が増えた影響と一致します。けたぐりはヘビー級ポケモンへの打点として採用されてきましたが、環境上位の体重分布が変化したことで優先度が下がっています。

**つるぎのまい+5.0pp**の上昇は積み型志向の強まりを示します。くろいメガネ型でもつるぎのまいは標準採用されており、いのちのたま型でも積み前提の運用が中心です。全体的な積み型志向の強まりがつるぎのまい採用率を押し上げました。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くろいメガネ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">66.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-12.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いのちのたま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>15.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヨプのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.2pp</td>
</tr>
</tbody>
</table>
</div>

くろいメガネはあくタイプ技（ふいうち・ドゲザン）の威力を1.2倍に高める消費なしアイテムで、M-2では主力の66.1%を占めていました。M-3では53.2%に下がり、代わりに**いのちのたま（全技1.3倍・毎ターン最大HPの10%消耗）が15.3%**で台頭しています。いのちのたまはアイアンヘッドなどあく以外の技にも倍率が乗るため、4技すべてに火力補正をかけられる反面、消耗を伴う運用になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いじっぱり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">92.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ すばやさ↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

物理アタッカーとしてこうげきを最大化するいじっぱりが圧倒的主流（92.6%）です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-A32-S2</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">40.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・こうげき全振り+素早さ最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-A32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・こうげき全振り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-B32-D2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・ぼうぎょ全振り</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H2-A32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき全振り+素早さ調整</td>
</tr>
</tbody>
</table>
</div>

**H32-A32-S2（40.5%）**がM-3の標準配分として定着しています。HPとこうげきを最大化したうえで、S2（素早さ2ポイント）を加えて特定の素早さ帯を超えるミラー調整を行う型です。H32-A32（S振りなし）との差はS実数値が70か72かで、一部の速度調整を行う場合に使われます。

### 代表型の実数値（H32-A32-S2・いじっぱり）

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>207</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき（いじっぱり↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>205</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">140</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">105</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72</td>
</tr>
</tbody>
</table>
</div>

HP207・こうげき205と物理方面のスペックが高い一方、すばやさ72は環境下位の低速帯。ふいうちは優先度+1の先制技のため相手のすばやさに関わらず先に動けますが、同優先度帯での処理には物理受け性能が頼りになります。

---

## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率（M-3）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2比</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>そうだいしょう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まけんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">プレッシャー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">—</td>
</tr>
</tbody>
</table>
</div>

**そうだいしょう**はその試合で味方が倒れた数に応じて技の威力が上昇する特性（1体につき+10%、最大+50%）。登場時に倒れた数を参照するため、終盤の切り返しに適しています。

**まけんき**（12.8%、+1.9pp）は相手に能力を下げられたときにこうげきが2段階上がる特性で、いかくや能力低下技を逆用できます。採用率は増加傾向にあります。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">135</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">120</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
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
      <div style="width:25%;background:linear-gradient(90deg,#f87171,#ef4444);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">550</span>
  </div>
</div>

こうげき135・ぼうぎょ120・HP100と物理方面が高水準で、すばやさ50が低い。ふいうちの優先度+1で攻撃順を確保しながら、物理受け性能で居座る運用が基本です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span>ノーマル・くさ・こおり・ひこう・いわ・ドラゴン・はがね・ゴースト・あく（いずれも0.5倍）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

**かくとう×4**が最大の穴（あく2倍×はがね2倍）。環境上位に多いかくとう技を受けると物理耐久があっても一撃で落ちます。ほのお・じめんの×2弱点はリザードン（8位）・ガブリアス（1位）・カバルドン（10位）の主要技と噛み合います。一方でエスパー・どくを無効化し、11タイプを半減以下にするため、居座れる範囲は広い。

---

## 主な型

### 型1：くろいメガネ型（53.2%）

ふいうち・ドゲザンのあく2技に1.2倍補正をかける安定型。いのちのたまの消耗リスクなしで安定した先制火力を維持します。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>くろいメガネ型（標準）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>そうだいしょう（86.7%）<br>
    <strong>性格：</strong>いじっぱり　<strong>EV：</strong>H32-A32-S2<br>
    <strong>持ち物：</strong>くろいメガネ<br>
    H207 / A205 / B140 / D105 / S72
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>ふいうち / ドゲザン / アイアンヘッド / つるぎのまい
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    つるぎのまい＋そうだいしょう補正が乗った状態でのふいうち先制が詰め筋。アイアンヘッドはフェアリータイプへの打点（×2）。くろいメガネ採用時はふいうち・ドゲザンにのみ補正がかかるため、アイアンヘッドは補正なし。
  </p>
</div>

### 型2：いのちのたま型（15.3%）

M-3で新台頭した型。4技すべてに1.3倍補正がかかるため、アイアンヘッドを含む全技の火力が上がります。毎ターン最大HPの約10%を消耗するリスクがある分、先制ふいうちで仕留めきれない場面での対応幅が広がります。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>いのちのたま型</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>そうだいしょう（86.7%）<br>
    <strong>性格：</strong>いじっぱり　<strong>EV：</strong>H32-A32-S2<br>
    <strong>持ち物：</strong>いのちのたま
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>ふいうち / ドゲザン / アイアンヘッド / つるぎのまい（かわらわり）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    くろいメガネ型より全技の打点が高く、アイアンヘッドにも1.3倍補正がかかります。毎ターン最大HPの約10%を消耗するため、積み前提で仕留めきる運用が基本です。
  </p>
</div>

### 型3：ヨプのみ型（6.2%）

かくとう技の×4弱点を保険のみで軽減する型。きあいのタスキと異なり、HPが少ない状態でも1度限りの軽減が発動します。かくとう技を1発受けつつ味方が1体倒れた場合、そうだいしょう+10%補正がかかった状態で反撃するプランをとれます。

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
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ムクホーク（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率98.4%）で×4弱点を突かれます。すばやさも上を取られるため対面不利。パーティのかくとう対策枠で処理先を用意することで回避できます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技（×2弱点）を高火力で撃てる。すばやさでも上を取られやすい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（×2弱点）・すなおこしによる消耗。物理耐久が高くつるぎのまいを積んでも崩しにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率92.9%・×2弱点）が主な脅威。みず/じめんタイプのためアイアンヘッドが半減されます。ガブリアスなどじめん耐性のある先発で処理してからドドゲザンを繰り出す構成が有効です。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.5%・×2弱点）をほぼ全個体が持ち、こちらから殴り合いにはいけません。ムクホークなどひこう/ゴーストタイプをガブリアスより先に出してじしんを誘わせる対策が有効です。</td>
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
    <div class="rate">共演1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">共演2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" loading="lazy">
    <div class="name">ムクホーク</div>
    <div class="rate">共演3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">共演4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">共演5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">共演6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">共演7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">共演8位</div>
  </div>
</div>

**ガブリアス（1位）**はM-3環境最上位ポケモンで、多くのパーティに採用されるため同居率が高い。ドドゲザンのはがねタイプでこおり技をガブリアスに代わって受けられる場面があります。一方ガブリアスはじしん（採用率99.5%）をほぼ全個体が持ち、ドドゲザンの×2弱点を突くため、同時選出時には選出順の調整が必要です。

**ライチュウ（2位）**は高い素早さで先手を取りながら削りを入れ、ドドゲザンを後続に繰り出す構成。ライチュウが相手の特殊アタッカーに消耗させてから、物理耐久のあるドドゲザンで詰める流れになります。

**ムクホーク（3位）**はドドゲザンの苦手なかくとう技を持つが、高い素早さで先手を取れる攻め寄りの共演。どちらが先に弱点を突かれるかの読み合いになる。

**ブリジュラス（5位）**ははがね/ドラゴンタイプ。ブリジュラスはフェアリーを無効化し、ドドゲザンはエスパーを無効化するため、タイプ的な相互補完が成立します。ミミッキュや特殊アタッカーへの対応をブリジュラスが担い、ドドゲザンが物理で詰める役割分担になります。

**ミミッキュ（8位）**はばけのかわで一度の行動が保証されるため、相手の先制技を受けながらのろいやつるぎのまいを積んで後続のドドゲザンへつなぐ動きが可能です。ミミッキュが削りを入れた後、ドドゲザンがふいうちで先制してそのまま詰める流れになります。

---

## まとめ

M-3のドドゲザンは使用率24位を維持しつつ、持ち物・技構成に変化が出たシーズンです。

- くろいメガネ53.2%（M-2比-12.9pp）、いのちのたま15.3%が新台頭
- つるぎのまい77.3%（+5.0pp）が標準化
- かわらわり10.3%（+6.9pp）でスクリーン対策が増加
- H32-A32-S2・いじっぱりが40.5%で定着

基本的な運用（そうだいしょう×ふいうち積み型）は変わらず、対スクリーン意識の高まりといのちのたまによる全技火力化が加わった形です。かくとう×4弱点はM-3も最大の課題で、ムクホーク（7位）・バシャーモ（11位）など上位のかくとう使いへの対策をパーティ単位で用意する必要があります。

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/kingambit/)**
