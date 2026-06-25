---
title: '【ポケモンチャンピオンズ】メガメタグロス考察 M-3 使用率7位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率7位のメガメタグロスを実データで分析。サイコファング84.2%・バレットパンチ79.1%の物理アタッカー型を解説。はがね/エスパーの多耐性と弱点4タイプ、メガ後S178の速度ライン、環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-23'
heroImage: '../../assets/hero-metagross-m3.png'
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
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" />
  <div>
    <h2 style="margin:0 0 8px">メガメタグロス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>　特性（メガ前）: <strong>クリアボディ 99.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/22集計）時点のものです

シーズンM-3のシングルバトルで、メガメタグロスは**使用率7位**を記録。はがね/エスパーは耐性が多く、9タイプを半減・1タイプを無効化する一方、**弱点はほのお・じめん・ゴースト・あくの4タイプ**に絞られます。メガ進化後はこうげき145・ぼうぎょ150・とくぼう110・すばやさ110の高水準な種族値を備え、特性かたいツメで接触技の威力が1.3倍に高まります。

---

## なぜ今メガメタグロスが使用率7位なのか

### 1. 9タイプ半減・どく無効の多耐性

はがね/エスパーは、ノーマル・ひこう・いわ・くさ・こおり・ドラゴン・フェアリー・はがねを半減し、エスパーは×0.25まで軽減、どくを無効化します。弱点はほのお・じめん・ゴースト・あくの4タイプのみで、本来エスパーが弱点とするゴースト・あくは残るものの、フェアリー・かくとう（はがね×2・エスパー×0.5＝等倍）などはがねが多くの攻撃を抑えます。半減・無効が広いため、弱点を突かない相手には繰り出しから役割を持てます。

### 2. かたいツメ補正で接触技が1.3倍

メガ進化後の特性かたいツメは接触技の威力を1.3倍にします。採用率上位のサイコファング（84.2%・接触）・れいとうパンチ（61.4%・接触）・アイアンヘッド（28.1%・接触）はいずれも補正対象です。一方でじしん（74.1%）は非接触のため補正は乗りませんが、こうげき145の高い攻撃種族値と威力100で十分な打点になります。

### 3. メガ後S110で中速帯を上から叩く

メガ後すばやさ110は、ようき採用60.9%でS実数値178に達し、S102のガブリアス（最速S実数値169）やS100のメガリザードンY（同167）を上から叩けます。バレットパンチ（採用率79.1%・優先度+1）を併せ持つため、より速い相手にも先制打点を残せます。ただしようき型でもマスカーニャ（最速S実数値192）など一部の高速勢には後手を踏みます。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:72.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">145</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">150</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">110</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

こうげき145・ぼうぎょ150は最上位クラスで、物理火力と物理耐久を高水準で両立します。すばやさ110・とくぼう110もメガ進化前（すばやさ70・とくぼう90）から大幅に上昇しており、中速帯を上から叩く速度と特殊方面の被弾耐性を得ます。HPは80と低めで、弱点4タイプを突かれた際の一撃耐性は高くありません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="エスパー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー（×0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点4タイプのうち、じめんは使用率1位ガブリアスのじしん、ほのおはメガリザードンYの炎技、あくはマスカーニャ・サザンドラのあく技と、いずれも環境上位の主力技に頻出します。対面で受け切るのではなく、弱点を突かない相手に繰り出して打点を通す使い方が基本です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>サイコファング</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">84.2%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>バレットパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">79.1%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じしん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">74.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">61.4%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">28.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">25.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>コメットパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">23.7%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>くさわけ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.7%</td>
</tr>
</tbody>
</table>
</div>

サイコファング・バレットパンチ・じしん・れいとうパンチの4技で採用上位が固まっています。サイコファングは相手のリフレクター・ひかりのかべを破壊できるタイプ一致技、れいとうパンチはドラゴン・ひこう・じめんへの打点として、ガブリアス・カイリュー等の有力ドラゴンに有効です。じしんは非接触ですがでんき・はがね・ほのおへの打点として74.1%採用されています。

特性はメガ前の**クリアボディ99.2%**が主流で、相手からの能力低下を無効化します。メガ進化後はかたいツメに変化します。持ち物はメタグロスナイト96.7%でほぼ一択です。

---

## 主要型の解説

性格はようき60.9%・いじっぱり35.9%の2択です。EVはA32 S32（HP振りなし）が最多で40.1%、次いでH振り・S振りなしの耐久寄り型が続きます。S振りの有無で抜ける相手が変わるため、ここでは「S最大振り型」と「耐久寄り型」の2型に分けて解説します。

### 型1: ようきAS型（最速S178）

**性格採用率: ようき 60.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ようきAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（メガ前99.2%）→メガ後かたいツメ<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（採用率40.1%）<br>
<strong>持ち物:</strong> メタグロスナイト（96.7%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・バレットパンチ<br>
・じしん<br>
・れいとうパンチ
</div>
</div>
</div>

**強み:**

ようきS32振りでS実数値178に達し、耐久寄り型（S振りなしでS実数値162）が後手を踏むガブリアス（最速S実数値169）・メガリザードンY（同167）を上から叩けます。先手でれいとうパンチをガブリアス・カイリューに、サイコファングを通せる点がS最大振りの価値です。れいとうパンチはこおり技なので、ドラゴン/ひこうのカイリューには×4が入ります。

**弱み:**

A32振りはようきで補正が乗らずA実数値197にとどまり、いじっぱり耐久寄り型のA実数値216より約9%低くなります。HP振りを切っているため、弱点4タイプを突かれた際の一撃耐性は耐久寄り型より低く、ガブリアスのじしんやメガリザードンYの炎技を先に受ける展開では一撃圏に入りやすくなります。

---

### 型2: いじっぱり耐久寄り型（HA重視）

**性格採用率: いじっぱり 35.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱり耐久寄り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（メガ前99.2%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（S振りなし）<br>
<strong>持ち物:</strong> メタグロスナイト（96.7%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・バレットパンチ<br>
・じしん<br>
・れいとうパンチ / アイアンヘッド
</div>
</div>
</div>

**強み:**

いじっぱりA32振りでA実数値216に達し、ようきAS型のA実数値197より約9%高い火力を出せます。さらにHP振りでH実数値が上がるため、ぼうぎょ150と合わせて物理アタッカーの攻撃を受けながら殴り返す展開で安定します。S振りを切る代わりに、バレットパンチ（優先度+1）の先制打点をA216基準で最大化し、速い相手は先制技で削る設計です。

**弱み:**

S振りがないためS実数値は162にとどまり、ようきAS型が上から叩けるガブリアス（最速S169）・メガリザードンY（同167）に対して後手を踏みます。これらに先制でれいとうパンチや炎弱点を突けない分、弱点を持つ相手との撃ち合いではバレットパンチや味方の補助に頼る必要があります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

メガメタグロスは多くの攻撃を半減しますが、弱点4タイプは環境上位の主力技に頻出します。ようきAS型のS実数値178を基準に、先手と打点の両面で相性を整理します（タイプ倍率は全件検算済み）。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようきS178＞ガブS169で先手。れいとうパンチ（×4）が無振りH183に対し確定1発（139〜163%）。じしん×2弱点を受ける前に処理できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチがドラゴン/ひこうに×4。ようきS178＞カイリュー最速S145で先手を取れ、圏内に入れやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチがあく/ドラゴンに×2の打点。ただしこだわりスカーフ採用83.1%のためようきS178でも多数派に後手を踏み、先制であく技（こちらにあく×2弱点）を通される。サイコファングはあくに無効でれいとうパンチ以外の打点が乏しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがはがね/ドラゴンに×2で通る。ようきS178＞ブリジュラスS85で先手。相手のはがね・ドラゴン技はこちら半減で受けやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミッキュのシャドークローはゴースト×2でこちらの弱点。バレットパンチ（はがねがゴースト/フェアリーに×2）で削れるが、ばけのかわで一度透かされ、剣の舞からのゴースト技で崩される</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のほのお・じめん・ゴースト・あくを×2で突ける相手が主な苦手対象です。

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
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガゲンガー（28位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（採用率81.7%）がゴースト×2でこちらの弱点。ゲンガナイト58.9%でメガ後S165となり、ようきS178が先手を取れる。じしんとサイコファングがゴースト/どくに×2で有効打はあるが、メガ後特性かげふみで交代を封じられ、後続に引けない点が脅威</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手じしん・サイコファングで削る。かげふみで縛られる前に一撃で処理できるかを計算してから対面するかどうか判断する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（5位圏内）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技（タイプ一致・晴れ補正）がほのお×2でこちらの弱点。メガ後S100でようきS178が上を取れるが、後出しから晴れ炎技を受けると一撃圏内になりやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこうで無効化されるため、でんき技（かみなりパンチ・ほのお/ひこうに×2）を持つ個体なら先手で削れる。みず・いわ技を持つ後続で処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく技がこちらにあく×2弱点。こだわりスカーフ73.7%でS実数値288と高速帯に入り、ようきS178でも先手を取れない。トリックフラワーの確定急所も脅威</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（優先度+1）で削るが、はがねはくさ/あくに等倍のため一撃にはならない。先制技持ちの後続や、くさ・あくを半減するはがね枠に引く</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率上位のポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。メタグロスが苦手なほのお枠へじしん・いわ技で対抗し、攻撃範囲を補完する</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわで一発耐え、剣の舞からの全抜き役。メタグロスの苦手なあく枠に対しフェアリー技で対抗できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊あく/ドラゴンの高速アタッカー。メタグロスのじめん弱点を浮遊で踏み倒し、特殊面から崩す役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速くさ/あく枠。すりかえ・トリックフラワーで対面を作り、メタグロスが受けにくいみず・じめん枠を削る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンの受け・展開枠。メタグロスのじめん弱点を電気技持ちの相手にも対応させ、サイクルを支える</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん物理受け枠。あくび・ステルスロックで起点を作り、メタグロスが受けにくい物理アタッカーを受け止める</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガメタグロスは物理耐久と接触技強化を備えた物理アタッカーですが、弱点のほのお・じめん・ゴースト・あくが環境上位の主力技に多く、パーティ単位でのカバーが必要です。

1. **じめん対策**: ひこう・浮遊枠（サザンドラ・カイリュー等）でガブリアスのじしんを無効化する
2. **ほのお対策**: みず・いわ技を持つ枠でメガリザードンYの炎技を受ける
3. **あく・ゴースト対策**: フェアリー技持ち（ミミッキュ等）でマスカーニャ・サザンドラ・ゴースト勢に対抗する
4. **高速枠の補完**: ようきS178で抜けないマスカーニャ（S192）等にはバレットパンチや味方の先制技で対処する

---

## データ分析①：弱点4タイプは環境上位の主力技にどれだけ刺さるか

メガメタグロスの弱点はほのお・じめん・ゴースト・あくの4タイプです。これらが環境上位ポケモンの主力技として実際にどれだけ採用されているかを並べると、「多耐性だが弱点が刺さりやすい」構図が定量的に見えます。

| 弱点タイプ | 主な使い手（環境順位） | 該当技と採用率 |
|---|---|---|
| じめん | ガブリアス（1位） | じしん（99%超） |
| ほのお | メガリザードンY（上位） | かえんほうしゃ等（一致・高採用） |
| あく | マスカーニャ・サザンドラ（上位） | はたきおとす・あくのはどう等（一致） |
| ゴースト | ミミッキュ（上位） | シャドークロー・シャドーボール（一致） |

弱点4タイプはいずれも使用率上位のタイプ一致技で運用されており、対面で受け止められる相手は限られます。これがメガメタグロスを「弱点を突かない相手に繰り出して打点を通す」攻めの軸として運用する根拠です。一方で耐性側を見ると、半減9タイプ＋どく無効により、ノーマル・ひこう・いわ・くさ・こおり・ドラゴン・フェアリー・はがねを主力とする相手には繰り出しから役割を持てます。

この耐性と弱点の偏りが、同居率上位に浮遊・ひこう・フェアリー技持ち（サザンドラ・カイリュー・ミミッキュ）が並ぶ理由でもあります。メタグロス側の弱点3タイプ（じめん・あく・ゴースト）を相方が補完する構築思想が、同居率データから読み取れます。

---

## まとめ：総評

メガメタグロスは、はがね/エスパーの多耐性（半減9タイプ＋どく無効）と、メガ後こうげき145・ぼうぎょ150・すばやさ110の高水準な種族値、かたいツメによる接触技強化を備えた物理アタッカーです。ようきAS型はS実数値178でガブリアス・メガリザードンYを上から叩け、いじっぱり耐久寄り型はA実数値216の火力とHP振りの安定感を取ります。S振りの有無で抜ける相手が変わるため、構築の速度ラインに合わせて型を選びます。

弱点のほのお・じめん・ゴースト・あくはいずれも環境上位のタイプ一致技に多く、ガブリアスのじしん・メガリザードンYの炎技・マスカーニャのあく技はパーティ単位でカバーが必要です。浮遊・ひこう・フェアリー技持ちを同伴して弱点3タイプを補完しつつ、メタグロス自身は弱点を突かない相手にれいとうパンチ・サイコファング・じしんで打点を通すのが基本戦術です。

---

## 関連記事

- [使用率1位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [同居率上位 ラグラージのM-3考察](/blog/swampert-analysis-m3/)
- [環境上位 ライチュウYのM-3考察](/blog/raichu-y-analysis-m3/)
