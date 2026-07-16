---
title: 'メガドラミドロ考察 M-3 型別採用率と立ち回り'
description: 'チャンピオンズM-3使用率29位メガドラミドロを徹底解説。クイックターン92.0%・りゅうせいぐん89.5%の対面操作型と、どくびし45.1%の毒撒き型を実データで解説。さいせいりょくによるサイクル戦・とくぼう163（D実数値236）の特殊耐久・でんき・みず・ほのお等を半減する耐性・環境上位への相性とパーティ構成まで紹介します。'

updatedDate: '2026-06-26'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-dragalge-m3.png'
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
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" />
  <div>
    <h2 style="margin:0 0 8px">メガドラミドロ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">29位</strong>　特性: <strong>てきおうりょく 65.3%</strong>（メガ後: さいせいりょく）
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

シーズンM-3のシングルバトルで、メガドラミドロは**使用率29位**を記録。メガ進化後に特性が**さいせいりょく**（交代で引っ込むたびにHPが最大値の1/3回復）に変わり、サイクル戦を繰り返しながら自己回復できる点が最大の特徴です。

クイックターン採用率92.0%で対面操作を行いながら回復を積み重ね、とくぼう163という突出した特殊耐久で特殊技を受け続けます。S44と環境最低水準の素早さを逆手に取り、**なまいき（S↓）・おだやか（A↓）で耐久を最大化**したサイクル特化の構成が主流です。

---

## なぜ今メガドラミドロが29位なのか

### 1. さいせいりょく＋クイックターンで毎ターン回復しながら対面操作

メガ進化後の特性さいせいりょくは、「引っ込むたびにHPの1/3を回復」するためクイックターンとの組み合わせが非常に強力です。クイックターン（採用率92.0%）でみずタイプ技を当てながら自分が交代し、引っ込む際にHP1/3を回復します。この動作を繰り返すことで、攻撃しながらHP管理を続けられます。消耗戦・サイクル戦においては相手より長く動き続けられる疑似的な持続力が生まれます。

### 2. とくぼう163と豊富な耐性で特殊アタッカーを受けられる

メガ後のとくぼう163（なまいきD32でD実数値236）はトップクラスの水準で、特殊アタッカーの技を複数回受けてもHPが残ります。どく/ドラゴン複合は**くさ技を0.25倍**、むし・でんき・みず・ほのお技を0.5倍に抑えるため、これらのタイプの特殊アタッカーへ後出ししやすいのが特徴です。突出したとくぼうと多くの耐性を組み合わせ、サイクルの軸として特殊技を受け流します。

### 3. どくどく・どくびし・クイックターンで状態異常と対面操作を同時に担う

どくどく（採用率57.5%）とどくびし（採用率45.1%）の両方が採用圏に入り、相手に毒ダメージを蓄積させながらクイックターンで後続に有利な対面を作ります。どくびし採用型は場に残ることで交代してくる相手ポケモンにも毒を広げられ、サイクルを回しながらじわじわとHPを削る戦い方ができます。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+15</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">132</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:81.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">163</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:22%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">44</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">594</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

とくぼう163・ぼうぎょ105の耐久に全振りした反面、HP65は低い部類でS44は環境最低水準のため、高速勢には後手を前提とした運用になります。とくこう132はヘドロウェーブ・りゅうせいぐんの打点として十分で、火力役と耐久役を兼ねられます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½・¼）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（×0.25）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

どく/ドラゴン複合は無効タイプを持ちませんが、くさ技を0.25倍、むし・でんき・みず・ほのお技を0.5倍で受けられます（フェアリー技は等倍）。一方、弱点はエスパー・じめん・こおり・ドラゴンの4タイプで、いずれも環境上位が採用する主力技（ガブリアスのじしん採用率99%超・ドラゴン技）に多く含まれます。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>クイックターン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">92.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">89.5%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくどく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">57.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくびし</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">45.1%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>10まんボルト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">33.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">95</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">26.4%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ヘドロばくだん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">19.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ねっとう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.1%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>シャドーボール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドラゴンテール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3.6%</td>
</tr>
</tbody>
</table>
</div>

クイックターンとりゅうせいぐんの2技がほぼ固定枠（89%超）で、残り2枠でどくどく・どくびし・10まんボルト・ヘドロウェーブの中から選ぶ構成が主流です。どくどくで継続ダメージを稼ぐ型と、どくびしで交代先にも毒を広げる型に分かれます。

---

## 主要型の解説

性格分布はなまいき41.2%（S↓D↑）・おだやか20.3%（D↑A↓）が上位2つで、どちらもD方向に補正をかける耐久型です。S44はなまいきでさらに下がりますが、環境上位に後手を取られることが前提のため、素早さへの投資は見られません。

### 型1: H32-B2-D32 なまいき耐久型（最多採用）

**EV採用率: H32-B2-D32 19.4%**（最多EV配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">H32-B2-D32 なまいき耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てきおうりょく（65.3%）※メガ後さいせいりょく<br>
<strong>性格:</strong> なまいき（D↑ S↓）<br>
<strong>EV:</strong> H32 B2 D32（採用率19.4%）<br>
<strong>持ち物:</strong> ドラミドナイト（98.4%）
</div>
<div>
<strong>技構成:</strong><br>
・クイックターン<br>
・りゅうせいぐん<br>
・どくどく or どくびし<br>
・ヘドロウェーブ
</div>
</div>
</div>

**強み:**

DにEVを最大振りするため、おだやかC32型（D実数値201）よりD実数値が236と高く、特殊アタッカーの技を1発でも多く受けられるのがこの型の強みです。さいせいりょく回復と合わせた持続力でサイクルの軸を担い、受けに徹するならこの配分を選びます。

**弱み:**

CにEVを振らないためC実数値が152にとどまり、おだやかC32型（C実数値184）より約21%低い打点しか出せません。受けに専念する配分のため、サイクル中に自分から削りを入れて相手を能動的に倒す動きは苦手で、攻撃役を別途用意する前提になります。

---

### 型2: H32-B2-C32 おだやか特殊アタッカー耐久型

**EV採用率: H32-B2-C32 6.3%**（Cに最大振りする主要配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">H32-B2-C32 おだやか攻守バランス型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てきおうりょく（65.3%）※メガ後さいせいりょく<br>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 B2 C32（採用率6.3%）<br>
<strong>持ち物:</strong> ドラミドナイト（98.4%）
</div>
<div>
<strong>技構成:</strong><br>
・クイックターン<br>
・りゅうせいぐん<br>
・ヘドロウェーブ<br>
・どくどく or どくびし
</div>
</div>
</div>

**強み:**

CにEVを最大振りすることでC実数値が184まで上がり、D32型（CにEVを振らずC実数値152）より約21%高い打点でりゅうせいぐん・ヘドロウェーブを撃てます。サイクル中に自分から削りを入れて相手を能動的に倒したい場合はこちらを選びます。

**弱み:**

DにEVを振らないため、D実数値はおだやか補正込みで201にとどまり、D32振りのなまいき型（D実数値236）より特殊耐久が約15%低くなります。「受けに徹するならなまいきH32-D32」「打点を出しながら受けるならおだやかH32-C32」という棲み分けです。

---

## 環境ポケモンへの相性分析

### 有利・不利が出る環境上位ポケモン

どく/ドラゴン複合はくさ技を0.25倍・むし/でんき/みず/ほのお技を0.5倍で受けますが、エスパー・じめん・こおり・ドラゴンは弱点です（フェアリー技は等倍）。S44のため基本的に後手を取られる前提で、特殊耐久とさいせいりょく回復で戦います。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（環境順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">相性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（みず/フェアリー）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技は等倍・みず技は0.5倍で受けられるが、りゅうせいぐん（ドラゴン）はフェアリーに無効化されクイックターン（みず）も半減。打点はヘドロウェーブ（どく×2）採用個体に限られる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（くさ/あく）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">✕ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技は0.25倍だが、トリプルアクセル89.1%（こおり×2）が弱点に刺さる。S123で先手を取られるため後出しもしにくい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ライチュウ（でんき）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のでんじほう（でんき×0.5）・きあいだま（かくとう×0.5）・くさむすび（くさ×0.25）をいずれも軽減できる。とくぼう163で受け切り、HP実数値が低いライチュウへはりゅうせいぐん（ドラゴン等倍・おだやかC32振りC実数値184）で反撃できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（ドラゴン/じめん）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">✕ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2）・ドラゴン技（ドラゴン×2）がともに弱点。物理型のためぼうぎょ105で一定受けられるが、A130の一致じしんは脅威。後出しは基本できない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（ほのお/ひこう）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のソーラービーム76%（くさ×0.25）・かえんほうしゃ47%（ほのお×0.5）をいずれも軽減できる。最大特殊打点のオーバーヒート31%（ほのお×0.5）は晴れ補正込みでD236に対し最大約53%（メガドラミドロHP実数値122）を与えるが、2発目はオーバーヒートのC2段階ダウンで威力が落ち、さいせいりょく回復（HP1/3＝約40）も挟めるため受け回せる。エアスラッシュ（ひこう）も等倍止まり。りゅうせいぐん（ドラゴン等倍）で反撃できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（じめん）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">✕ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがじめん×2で弱点。耐久型のカバルドンはりゅうせいぐんを複数回受けられる可能性があり、あくびで流される展開が多い</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）・ドラゴン技がいずれも×2弱点。物理アタッカーのためぼうぎょ105で受けられる場面もあるが、一致じしんの打点は脅威</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうのアーマーガア（同居率1位）でじしんを無効化し、ガブリアスの前に引いて処理する。ドラミドロはガブリアスと対面させない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2）が弱点で、高いぼうぎょ・HPでりゅうせいぐんのCダウンを乗り越えられる。あくびでこちらのサイクルを崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技を持つ枠でカバルドンに弱点を突く。ドラミドロのどくびしを活かし毒にしてからサイクルを消耗させる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のサイコファング87.7%（エスパー×2）に加え、じしん75.6%（じめん×2）・れいとうパンチ58.5%（こおり×2）もいずれも×2弱点で、複数の弱点技を上から打たれる。物理アタッカーのためぼうぎょ105で一定は受けられるが、弱点を3タイプ突かれると消耗が早い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">有効な対策なし。エスパー・じめん・こおりの3タイプすべてが弱点のため、ドラミドロと直接対面させないことが前提</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0473-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マンムー（49位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん・こおりの両タイプがそれぞれ×2弱点で、つららばり・じしんのどちらでも一撃が重い。物理こおり技はぼうぎょ105でもダメージが蓄積する</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">有効な対策なし。はがね・ひこうタイプの枠でマンムーを処理し、ドラミドロと直接対面させない</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでじめんを無効化。ドラミドロが最も苦手なガブリアスのじしんを受けて立てる物理受け枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ">
    <div class="name">オーロンゲ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">いたずらごころのリフレクター・ひかりのかべでサイクルを補助。ドラミドロのどくびしと合わせ展開を整える</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S102の高速じめん枠。ドラミドロが後手を踏む相手を上から処理し、相手のじめん・ドラゴンを先に削る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S123の高速枠。ドラミドロが後手を踏む相手を上から処理し、クイックターンで作った有利対面を活かす</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ゴーストでフェアリーもエスパーも半減できる受け枠。ドラミドロが弱点とするエスパーを肩代わりできる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわで一度行動を保証し、つるぎのまいから上を取って削る。ドラミドロが対面を作った相手を高速で処理する詰め役</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガドラミドロはでんき・みず・ほのお等を半減する耐性・さいせいりょく回復・クイックターンによる対面操作を軸にしたサイクル戦が得意です。残り5体で以下を補います。

1. **じめん対策**: はがね/ひこうのアーマーガア（同居率1位）でガブリアスのじしんを無効化する枠。これがないとじめん弱点のドラミドロを安全に動かせません
2. **高速アタッカー**: S44のドラミドロが先手を取れないため、クイックターンで対面を作った後に上から殴るS100超の高速枠（マスカーニャ・ガブリアス等）
3. **エスパー対策**: エスパー×2弱点をカバーするはがね複合（サーフゴー）や高耐久枠でエスパーポケモンを処理する役割
4. **どくびし連携**: どくびしを採用した場合、どくが入った相手に対してクイックターンで交代を促しどくダメージを蓄積させる動線を用意する

---

## データ分析①：クイックターン92.0%が示すサイクル特化の徹底

メガドラミドロの技採用率から、このポケモンの役割が「攻撃で削るアタッカー」ではなく「さいせいりょく回復を繰り返すサイクル役」に徹していることが読み取れます。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| クイックターン | 対面操作 | 92.0% | さいせいりょく回復＋後続有利対面 |
| りゅうせいぐん | 攻撃 | 89.5% | タイプ一致最大火力 |
| どくどく | 変化 | 57.5% | もうどく付与・削り蓄積 |
| どくびし | 変化 | 45.1% | 場への毒撒き |
| 10まんボルト | 攻撃 | 33.8% | みず・ひこうへの打点 |

注目すべきはクイックターン92.0%という高い採用率です。クイックターンは「みずタイプの攻撃技として威力を出しながら、使用後に自分が引っ込む」技で、引っ込む際にさいせいりょくが発動してHP1/3を回復します。つまり**攻撃しながら自己回復する**一石二鳥の動きが可能で、サイクル戦においてはクイックターンを使うたびにHPを回復しながら対面を有利に操作できます。

また、どくどく57.5%とどくびし45.1%の両方が高い採用率を保っており、何らかの毒付与手段を持つ個体が大多数を占めます。りゅうせいぐん89.5%もほぼ固定で採用されているため、**「クイックターン+りゅうせいぐん+どくどくorどくびし」の3枠がほぼ固定**で、最後の1枠に10まんボルト（33.8%）かヘドロウェーブ（26.4%）を入れる構成が実態です。みず・ドラゴンの一致技だけだとガブリアス（じめん）やアーマーガア（はがね/ひこう）に通りが悪く、10まんボルトでみず・ひこうへの打点を補う選択が5位（33.8%）に入っています。

持ち物採用率98.4%がドラミドナイトと極めて集中していることも、この型の「メガ進化ありきのさいせいりょくサイクル」という役割をデータが明確に示しています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">H32-B2-D32 なまいき耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">19.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なまいき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">クイックターン・りゅうせいぐん・どくどく・どくびし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D実数値236で特殊技を最も安全に受けられる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C実数値152と低く、相手の高耐久を削り切れない場面がある</td>
  </tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">H32-B2-C32 おだやか攻守型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">クイックターン・りゅうせいぐん・ヘドロウェーブ・どくどく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C実数値184でD32型より約21%高い打点を出せる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D実数値201とD32型（236）より約15%低い特殊耐久</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガドラミドロはさいせいりょく＋クイックターンによるサイクル戦特化型で、M-3で29位という順位はとくぼう163の特殊耐久と豊富な耐性を活かす特殊受け枠として安定した需要があることを示しています。

クイックターン92.0%・りゅうせいぐん89.5%・どくどく57.5%・どくびし45.1%というデータは、このポケモンが「攻撃→交代回復→再度後出し」のサイクルを繰り返す役割に徹していることを明確に示しています。S44の低速は割り切り、とくぼう163というトップクラスの特殊耐久と特性さいせいりょくを軸にした独自の立ち回りが環境での居場所を作っています。

弱点はじめん・エスパー・こおり・ドラゴンの4タイプと多く、特にじめんを持つガブリアスは弱点が2つ重なるため直接対面は避けるべきです。ひこう・はがねタイプの枠（アーマーガア等）をパーティに入れてじめん無効を確保し、ドラミドロはくさ技を0.25倍・むし/でんき/みず/ほのお技を0.5倍で受ける特殊受けとして使うのが基本戦術です。

---

## 関連記事

- [環境上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [はがね/エスパーのメガメタグロスのM-3考察](/blog/metagross-analysis-m3/)
- [みず枠パートナー ラグラージのM-3考察](/blog/swampert-analysis-m3/)
