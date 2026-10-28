---
title: '【ポケモンチャンピオンズ】グソクムシャ 考察 M-7 シーズン つるぎのまい型解説'
description: 'M-7シーズン使用率8位（M-6:6位）のグソクムシャ考察。「つるぎのまい型」「フルアタ・耐久型」「フルアタ・速攻型」の3型を比較し、M-6からのであいがしら-43.3pt・つるぎのまい+41.9ptの採用変化と型別の苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-25'
updatedDate: '2026-10-18'
heroImage: '../../assets/hero-golisopod-m7.png'
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
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" />
  <div>
    <h2 style="margin:0 0 8px">メガグソクムシャ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">8位</strong>（M-6: 6位）　持ち物: <strong>グソクムシャナイト 98.8%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・技・持ち物・性格・特性・EV・同居率はすべて2026-10-11時点の実測データに統一しています。

M-7シーズンのグソクムシャは使用率8位（M-6: 6位）です。持ち物グソクムシャナイトの採用率は98.8%で、ほぼ全個体がメガ進化前提です。M-7ではつるぎのまいでこうげきを積んでから押し切る構成が最多勢力です。

---

## グソクムシャの基本スペック

<!-- gate:rows start id=base_stats facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
### 種族値（通常→メガグソクムシャ）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:32px;text-align:right">メガ後</span>
    <span style="width:40px;text-align:right">差分</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:32px;text-align:right">75</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:62.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:12.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">125</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:70%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:17.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">140</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">175</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:30%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">70</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:45%;background:linear-gradient(90deg,#34d399,#059669);height:12px"></div>
      <div style="width:15%;background:linear-gradient(90deg,#34d399,#059669);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">120</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:20%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">40</span><span style="width:32px;text-align:right">40</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">530</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">630</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガ進化でこうげき+25・ぼうぎょ+35・とくこう+10・とくぼう+30と攻守が底上げされますが、すばやさは40のまま変化しません。型1・型2のEV配分（H32-A32-D2）ではすばやさ実数値60にとどまり、型3（ようき・H2-A32-S32）でもS101止まりです。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ（メガ進化後）：</strong>
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお×4の一点のみです。

### 特性

<strong>ききかいひ（100.0%）</strong>から、メガ進化後は<strong>かたいツメ</strong>に切り替わります。ききかいひはHPが1/2以下になると自動的に手持ちに戻る特性です。かたいツメは接触技の威力を上げる特性で、きゅうけつ・ふいうち・インファイト・であいがしら・とんぼがえり・アイアンヘッド・アクアジェットなど3つの型が採用する主要技はいずれも接触技です。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。相手が攻撃を選んでおりかつこの技を使ったターン中、まだ攻撃をしていない時でないと失敗する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きゅうけつ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">74.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手に与えたダメージの1/2自分のHPを回復する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃を2段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">43.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手をひるませる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">33.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の防御と特防が1段階下がる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドリルライナー</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">29.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">きゅうしょアップ+1で攻撃する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>であいがしら</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">22.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+2。登場して最初に出す技でない場合失敗する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.7%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">攻撃した後、手持ちの他のポケモンと交代する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">ちょうはつ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.2%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をちょうはつ状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.9%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## M-7の採用型

技・性格・EVの組み合わせから、採用割合が高い順に3つの型を紹介します。

### 型1：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ききかいひ（100.0%）→メガ進化後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-D2<br>
<strong>持ち物:</strong> グソクムシャナイト
</div>
<div>
<strong>技構成:</strong><br>
・きゅうけつ<br>
・つるぎのまい<br>
・ふいうち<br>
・インファイト
</div>
</div>
</div>

つるぎのまいでこうげきを2段階上げ、きゅうけつ・ふいうち・インファイトで押し切る構成です。4つ目の技はインファイトが主流で、ドリルライナー・アイアンヘッドが選択候補として並びます。

<!-- gate:rows start id=card:1 facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
**他の型との違い:**

- 他の型に無い技：つるぎのまい
- きゅうけつ：この型は必ず持ち、フルアタ・耐久型・フルアタ・速攻型では選択技
- ふいうち：この型は必ず持ち、フルアタ・耐久型・フルアタ・速攻型では選択技
<!-- gate:rows end id=card:1 -->

---

### 型2：フルアタ・耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ・耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ききかいひ（100.0%）→メガ進化後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-D2<br>
<strong>持ち物:</strong> グソクムシャナイト
</div>
<div>
<strong>技構成:</strong><br>
・であいがしら<br>
・とんぼがえり<br>
・アイアンヘッド<br>
・インファイト
</div>
</div>
</div>

であいがしら・アイアンヘッドでタイプ一致の打点を並べ、とんぼがえりで攻撃後に交代して後続につなぎます。4つ目の技はインファイトのほか、ふいうち・きゅうけつを選ぶ個体もいます。

<!-- gate:rows start id=card:2 facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
**他の型との違い:**

- フルアタ・速攻型との技の違い：この型はインファイト、フルアタ・速攻型はアクアジェット
<!-- gate:rows end id=card:2 -->

---

### 型3：フルアタ・速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ・速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ききかいひ（100.0%）→メガ進化後かたいツメ<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> グソクムシャナイト
</div>
<div>
<strong>技構成:</strong><br>
・であいがしら<br>
・とんぼがえり<br>
・アイアンヘッド<br>
・アクアジェット
</div>
</div>
</div>

型2と同じであいがしら・とんぼがえり・アイアンヘッドの3枚に、S101でも上から動けない相手への先制技としてアクアジェットを加えた構成です。

<!-- gate:rows start id=card:3 facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
**他の型との違い:**

- アクアジェット：この型は必ず持ち、フルアタ・耐久型では選択技
- 3つの型で最も高い実数値：すばやさ101
- 3つの型で最も低い実数値：HP152・こうげき202・とくぼう140
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ・耐久型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ・速攻型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（ひかえめ・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（おくびょう・ルカリオナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（むじゃき・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（のんき・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー（いじっぱり・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。ガブリアスは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6→M-7 採用データの変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-7</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>8位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">下降</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>66.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+41.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きゅうけつ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>74.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+35.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>79.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+18.2pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>33.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+13.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-32.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">であいがしら採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-43.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-19.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアジェット採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-8.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき採用率（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>8.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+8.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん採用率（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">グソクムシャナイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">98.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>98.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+0.7pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
- であいがしら：65.4%→22.1%（-43.3pt）。フルアタ・耐久型・フルアタ・速攻型に共通のため、型の増減とは言えません。
- つるぎのまい：24.2%→66.1%（+41.9pt）。記事の型ではつるぎのまい型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- きゅうけつ：39.6%→74.8%（+35.2pt）。つるぎのまい型が持ち、フルアタ・耐久型・フルアタ・速攻型でも選択技のため、型の増減とは言えません。
- アイアンヘッド：75.1%→43.1%（-32.0pt）。記事のすべての型に共通のため、型の増減とは言えません。
- とんぼがえり：37.6%→17.7%（-19.9pt）。フルアタ・耐久型・フルアタ・速攻型に共通のため、型の増減とは言えません。
- ふいうち：61.7%→79.9%（+18.2pt）。つるぎのまい型が持ち、フルアタ・耐久型・フルアタ・速攻型でも選択技のため、型の増減とは言えません。
- インファイト：20.5%→33.7%（+13.2pt）。つるぎのまい型・フルアタ・耐久型に共通のため、型の増減とは言えません。
- ようき：0.3%→8.8%（+8.5pt）。フルアタ・速攻型だけが選んでいるため、この変化はその型の増減を示します。
<!-- gate:rows end id=diff_movers -->

---

## 苦手なポケモン

使用率上位のうち、相手の型が変わっても一貫して不利になる相手のみを掲載します。

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
<!-- gate:rows start id=weak facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX32.3%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技ドリルライナーは確定1発。メガリザードンXのフレアドライブ（採用率31.4%）は確定1発で、S60対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のふいうちは確定2発。メガリザードンYのかえんほうしゃ（採用率43.5%）は確定1発で、S60対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技ドリルライナーは確定1発。エースバーンのかえんボール（採用率99.2%）は確定1発で、S60対S171で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のインファイトは確定2発。ヒートロトムのオーバーヒート（採用率94.6%）は確定1発で、S60対S106で後手のため、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=weak -->
</tbody>
</table>
</div>

---

## 得意なポケモン

同じ基準で掲載します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<!-- gate:rows start id=strong facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型の選択技ドリルライナーは確定4発（相手のオボンのみ込み）。ブリジュラスの10まんボルト（採用率71.1%）は乱数4発（90%）で、最後は優先度+1の選択技ふいうちで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型のアイアンヘッドは乱数4発（>99%）（相手のオボンのみ込み）。カバルドンのじしん（採用率98.2%）は確定4発で、S101対S67で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技アイアンヘッドは確定2発（ばけのかわ込み）。ミミッキュのシャドークロー（採用率57.3%）は乱数4発（45%）で、S60対S148で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のふいうちは確定2発。サーフゴーのシャドーボール（採用率97.8%）は乱数3発（97%）で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ<br><span style="font-size:0.8em;color:#64748b">メガセグレイブで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型のアイアンヘッドは確定2発。メガセグレイブのじしん（採用率92.1%）は乱数3発（96%）で、最後は優先度+1のアクアジェットで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型の選択技ふいうちは確定1発。イダイトウ(オス)のウェーブタックル（採用率86.3%）は確定2発で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のふいうちは確定2発。メガメタグロスのじしん（採用率68.0%）は乱数4発（70%）で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技アイアンヘッドは確定2発（相手のきあいのタスキ込み）。キラフロルのパワージェム（採用率87.9%）は乱数3発（97%）で、最後は優先度+1のふいうちで先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のきゅうけつは確定1発。ゴリランダーのはたきおとす（採用率44.5%）は倒しきれず、S60対S107で後手ですが、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型のとんぼがえりは確定2発（相手のきあいのタスキ込み）。マスカーニャのはたきおとす（採用率64.3%）は確定5発で、最後は優先度+1のアクアジェットで先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のふいうちは確定2発（相手のきあいのタスキ込み）。ゲンガーのシャドーボール（採用率84.5%）は乱数3発（97%）で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・耐久型のであいがしらは確定2発。メガライチュウYのでんじほう（採用率97.1%）は確定3発で、S60対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・耐久型のとんぼがえりは確定2発（相手のきあいのタスキ込み）。ゲッコウガのなみのり（採用率36.9%）は確定3発で、最後は優先度+1の選択技ふいうちで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">フラエッテ(永遠)<br><span style="font-size:0.8em;color:#64748b">メガフラエッテで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技アイアンヘッドは確定1発。メガフラエッテのムーンフォース（採用率96.9%）は乱数4発（97%）で、S60対S169で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カメックス<br><span style="font-size:0.8em;color:#64748b">メガカメックスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型の選択技きゅうけつは確定2発。メガカメックスのみずのはどう（採用率16.4%・少数派）は確定2発で、最後は優先度+1の選択技ふいうちで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技アイアンヘッドは確定2発。オオニューラのほのおのパンチ（採用率15.0%・少数派）は確定3発で、S60対S172で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型の選択技きゅうけつは確定2発。ブラッキーのイカサマ（採用率98.1%）は確定4発で、S101対S85で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ・速攻型の選択技ふいうちは確定2発。ギルガルドのポルターガイスト（採用率76.4%）は確定2発で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-7でグソクムシャと同じパーティに入る頻度が高いポケモン（同居率1〜10位、2026-10-11時点）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" loading="lazy">
    <div class="name">キラフロル</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" loading="lazy">
    <div class="name">イエッサン(オス)</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">キラフロル<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イエッサン(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガボーマンダで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャの弱点：ほのお技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX・メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝メガグソクムシャの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンX・メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；エースバーン＝かえんボール・とびひざげり・ダストシュート・ふいうち・とんぼがえり；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=6bdfeeb7e39ece8a67f902ceeed2e9be5802bce4 -->
**強み**

- 得意な相手は18体です。使用率上位では、ブリジュラス（3位）にドリルライナー、カバルドン（4位）・ミミッキュ（5位）にアイアンヘッドで勝てます。
- タイプ相性では、グソクムシャはみず・こおり・かくとう・じめん・はがねを半減以下で受けられます。
- タイプ相性では、メガグソクムシャはノーマル・くさ・こおり・エスパー・むし・ドラゴン・はがね・フェアリーを半減以下、どくを無効で受けられます。

**弱み**

- 苦手な相手は4体です。使用率上位では、メガリザードンX（6位）のフレアドライブ、メガリザードンY（6位）のかえんほうしゃ、エースバーン（20位）のかえんボールで先に倒されます。
- グソクムシャの弱点はでんき・ひこう・いわです。
- メガグソクムシャの弱点はほのお（×4）です。

**型の選び分け**

- 「つるぎのまい型」：他の型に無い技はつるぎのまい。
- 「フルアタ・耐久型」：フルアタ・速攻型のアクアジェットの代わりにインファイトを持つ。
- 「フルアタ・速攻型」：アクアジェットを必ず持つ（フルアタ・耐久型では選択技）。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は8位です（M-6: 6位）。
- 採用率の変化が大きいのはであいがしら（-43.3pt）・つるぎのまい（+41.9pt）・きゅうけつ（+35.2pt）です。
<!-- gate:rows end id=summary -->

## 関連記事

- [M-6シーズン（使用率6位）のグソクムシャ考察](/blog/golisopod-analysis-m6/)
