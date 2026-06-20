---
title: '【ポケモンチャンピオンズ】カエンジシ考察 M-3 使用率81位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率81位のメガカエンジシを徹底分析。きんちょうかん65.7%で相手のきのみを封じる特殊型と、おくびょう72.2%・かえんほうしゃ90.1%を軸にした実データで解説。ねっさのだいちでじめん/はがね補完も可能。環境での立ち回りまで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-pyroar-m3.png'
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
  <img src="/images/pokemon/pokemon-0668-00.webp" alt="カエンジシ" />
  <div>
    <h2 style="margin:0 0 8px">メガカエンジシ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">81位</strong>　特性（メガ前）: <strong>きんちょうかん 65.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、カエンジシは**使用率81位**を記録。メガ進化後はC129・S126と特殊アタッカーとして十分な数値を持ち、**ほのお/ノーマルのタイプ一致技にハイパーボイス（みがわり貫通）を加えた打点構成**が特徴です。

特性は**きんちょうかん**が65.7%と最多で、相手のきのみ発動を完全に防いで継続回復・半減きのみの恩恵を奪う役割を担います。メガ前から特性が機能するため、出てきた時点でたべのこしやオボンのみを無力化できます。

---

## なぜカエンジシが環境に存在するのか

### 1. メガ後S126で環境中速帯を大きく上回る

メガ後S126（おくびょうS32の場合S実数値195）は環境の多くのポケモンを上回ります。おくびょう採用率72.2%はこの素早さを最大化する意図を反映しており、上から動いてほのお技を通す展開を主軸とします。

### 2. きんちょうかんで相手のきのみ回復を封じる

きんちょうかん（65.7%）は相手のきのみ（オボンのみ・各種半減きのみ等）の発動を防ぐ特性です。メガ進化前から発動するため、繰り出した瞬間から相手のオボンのみ・半減きのみを無効化できます。回復きのみに依存する耐久型を崩す際に有効で、相手の持ち物の選択肢を実質的に絞れます。

### 3. ハイパーボイス（音技）でみがわりを貫通する

ハイパーボイス（採用率56.5%）はノーマルタイプ一致の音技で、みがわりを貫通する特性があります。みがわりを張って様子見する相手に対し、みがわりごと削れるため消耗戦でのアドバンテージを取りやすい点が通常の技と異なります。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">86</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">88</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:46%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">92</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:64.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">129</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">86</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">126</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">607</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

C129・S126はメガ進化後の特殊アタッカーとして高い水準です。おくびょうS32でS実数値195、ひかえめC32でC実数値199となり、どちらの性格を選んでも攻撃面の一方は高いレベルを維持できます。HP86・B92・D86の耐久は並みで、上から弱点技を受けると大きなダメージになります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
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
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ×0.5</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり×0.5</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし×0.5</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね×0.5</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお×0.5</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はみず・かくとう・いわ・じめんの4タイプ（×2）です。ほのおタイプのみの弱点ではなくノーマルタイプも加わることで弱点が4タイプに増えており、コノヨザルなどのかくとう勢・ガブリアスのじめん技が刺さります。一方でゴースト無効により、シャドーボールを軸にしたゴーストタイプへの後出しは安定します。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">90.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">68.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ハイパーボイス</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">56.5%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ニトロチャージ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">37.7%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ねっさのだいち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">35.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>にほんばれ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.5%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>おにび</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくび</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.1%</td>
</tr>
</tbody>
</table>
</div>

かえんほうしゃ（90.1%）が事実上の確定技で、オーバーヒート（68.0%）との2枚採用が主流です。オーバーヒートはC2段階低下というデメリットがあるため、倒し切れる相手に使い切る運用が基本で、かえんほうしゃとの使い分けが技選択の軸となります。

---

## 主要型の解説

性格分布はおくびょう72.2%・ひかえめ26.0%の2択が中心で、S最大化のおくびょうが圧倒的多数を占めます。

### 型1: おくびょうきんちょうかん型（最多採用）

**性格採用率: おくびょう 72.2%**（S最大化。EV最多分布 H2-C32-S32 57.6%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0668-00.webp" alt="カエンジシ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSおくびょうきんちょうかん型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きんちょうかん（65.7%）<br>
<strong>性格:</strong> おくびょう（S↑ C↓）<br>
<strong>EV:</strong> H2-C32-S32（採用率57.6%）<br>
<strong>持ち物:</strong> カエンジシナイト（99.3%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・オーバーヒート<br>
・ハイパーボイス<br>
・ねっさのだいち / ニトロチャージ
</div>
</div>
</div>

**強み:**

おくびょうS32でメガ後S実数値195となり、環境の多くのポケモンを上から殴れます。きんちょうかんにより出てきた時点で相手のたべのこし・オボンのみ・半減きのみを無効化し、回復による粘りを封じます。ハイパーボイスでみがわりを貫通し、オーバーヒートで倒し切りたい相手を1発で処理する構成です。ねっさのだいちを採用すると、ほのお技が通りにくいはがねタイプやでんきタイプへの打点を確保できます。

**弱み:**

おくびょう（C↓）によりとくこうが低下するため、ひかえめ型と比べてC実数値が約1割低くなります。オーバーヒートはC2段階低下のデメリットから連打しにくく、使い切りになる場面を見極める必要があります。みず・いわ・じめん・かくとうの4弱点を持つため、上から弱点技を受けると耐えられないケースが多い点はこの型固有の問題ではありません。

---

### 型2: ひかえめ火力型（2番目に多い構成）

**性格採用率: ひかえめ 26.0%**（C最大化。EV最多分布 B2-C32-S32 9.4%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0668-00.webp" alt="カエンジシ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSひかえめ火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きんちょうかん（65.7%）/ じしんかじょう（20.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> B2-C32-S32（採用率9.4%）<br>
<strong>持ち物:</strong> カエンジシナイト（99.3%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんほうしゃ<br>
・オーバーヒート<br>
・ハイパーボイス<br>
・ねっさのだいち / ニトロチャージ
</div>
</div>
</div>

**強み:**

ひかえめC32でC実数値199となり、おくびょう型（C162）より約23%高い火力が出ます。この火力差により、おくびょう型では2発必要な相手を1発で倒せる場面が生じます。じしんかじょうを採用した場合、相手を倒すたびにこうげきが1段階上昇しますが、この型の主力は特殊技であるため実用場面は限られます。

**弱み:**

おくびょう型（S実数値195）と比べてS実数値が178と低く、S種族値が100を超える相手（メガリザードン・メガバシャーモ等）に先手を取られる対象が増えます。おくびょう型が抜けるS120前後の相手にも先手を取れなくなるため、上から動ける範囲がおくびょう型より狭まります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

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
    <img src="/images/pokemon/pokemon-0227-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこう複合だがほのお技が×2で通る。かえんほうしゃ・オーバーヒートのどちらも大きなダメージになります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0724-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あく複合で、ほのお技×2で通る。カエンジシのS126がメガ後のメガマスカーニャのS相当より速い場合が多く、上から処理できます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2弱点）を採用率上位で使用し、S102（最速実数値169）でカエンジシが先手を取れない場合も多い。ねっさのだいちは等倍止まりで有効打になりません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0979-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">コノヨザル（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう×2弱点でドレインパンチ・ふんどのこぶしが刺さる。カエンジシのほのおはゴーストタイプのコノヨザルには等倍で通るが、ノーマルタイプのハイパーボイスはゴーストに無効（×0）です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴーストタイプには当方ノーマル技が無効。ほのお技は等倍で通る。相手のシャドーボールはノーマルタイプ無効で通らないが、ヘドロばくだん等の別打点を持つ個体には注意が必要です</td>
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
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず×2弱点でなみのり・ハイドロポンプが刺さる。みず技はほのおに×2、ノーマルに等倍で合成×2の弱点になります</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・くさ技を持つポケモンで削ってから対処する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん×2弱点でじしんが高威力で刺さる。使用率1位のガブリアスがじしんを採用している個体の多さが脅威です</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプや浮遊特性を持つポケモンでガブリアスのじしんを無効化してから展開する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0306-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガボーマンダ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ×2弱点でいわなだれが刺さる。ほのお技はドラゴン/ひこう複合に等倍止まりで一撃で処理できません</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり・いわ技を持つポケモンでボーマンダを処理してから出す</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">カエンジシが苦手なみず・いわへの打点を別枠でカバーしつつ、じめん技でカエンジシのはがね・でんき弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう/ノーマルでじめん無効。カエンジシのじめん弱点をひこうタイプで補完する物理枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0724-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ/あくで高速物理。カエンジシが苦手なみずタイプにくさ技で打点を持ちつつ補完関係を形成</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0227-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでじめん無効・かくとう半減。カエンジシのかくとう・じめん弱点を補う耐久枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわでワンクッション。カエンジシが苦手な対面でじゃれつく・かげうちで圧力をかける</div>
  </div>
</div>

**パーティ構成の基本方針:**

カエンジシはほのお・ノーマルのタイプ一致打点を活かしつつ、4弱点（みず・かくとう・いわ・じめん）をパーティ全体でカバーする必要があります。

1. **じめん対策**: ひこうタイプや浮遊持ちでガブリアスのじしんを無効化する枠を用意する
2. **みず対策**: くさ・でんき技を持つポケモンで水タイプの相手に先手を取れる枠を確保する
3. **かくとう対策**: ひこう・エスパー・フェアリー技でかくとうタイプに圧力をかける枠を添える
4. **きんちょうかん連携**: 相手の回復きのみを無効化したい場面を想定し、たべのこし・オボンのみに依存する耐久型への展開ルートを作る

---

## データ分析①：技採用率の二重構造が示す「一撃と持続」の使い分け

カエンジシの技採用率を並べると、ほのお技2枚体制が浮かび上がります。

| 技 | タイプ | 採用率 | 役割 |
|---|---|---|---|
| かえんほうしゃ | ほのお | 90.1% | 安定技・持続火力（やけど10%）|
| オーバーヒート | ほのお | 68.0% | 一撃最大火力（C2段階低下）|
| ハイパーボイス | ノーマル | 56.5% | みがわり貫通・補完打点 |
| ニトロチャージ | ほのお | 37.7% | S上昇技 |
| ねっさのだいち | じめん | 35.0% | はがね・でんき補完 |

かえんほうしゃ（90.1%）とオーバーヒート（68.0%）の同時採用率が高いことは、「倒し切りたい相手にオーバーヒート・それ以外にかえんほうしゃ」という使い分け運用が主流であることを示しています。オーバーヒートのC2段階低下デメリットを許容してでも最大火力を持つ判断が、約7割のプレイヤーが取る択となっています。

ニトロチャージ（37.7%）の採用は注目に値します。メガ後でもS126と高いカエンジシがさらにSを上げる需要があるということは、環境に存在するS130以上の相手（一部メガ進化後の高速型等）を意識した採用と読めます。ニトロチャージとねっさのだいちの採用率がともに35〜38%と拮抗していることは、第4の技枠を「S上昇」か「はがね/でんき補完」かで選択している実態を数値で示しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CSおくびょう型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">おくびょう 72.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">かえんほうしゃ・オーバーヒート・ハイパーボイス・ねっさのだいち/ニトロチャージ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値195で多くの相手に先手を取れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C↓でひかえめ型より火力が約1割低い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CSひかえめ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ 26.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">かえんほうしゃ・オーバーヒート・ハイパーボイス・ねっさのだいち/ニトロチャージ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C実数値199で一発で倒せる範囲が広がる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値178でおくびょう型が抜けるS120前後の相手に先手を取れない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

カエンジシはメガ後C129・S126という特殊アタッカーとして機能し、ほのお/ノーマルのタイプ一致技にハイパーボイスのみがわり貫通を組み合わせた打点構成が軸です。きんちょうかん（65.7%）でたべのこし・オボンのみ等の回復きのみを無効化し、おくびょうS32での先手展開が主流の動きとなります。

弱点はみず・かくとう・いわ・じめんの4タイプに及ぶため、パーティ単位でのカバーが必要です。使用率81位というポジションは、火力・素早さは環境水準を満たすものの弱点タイプの多さから採用コストが生じていることを反映しています。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [はがね/フェアリーで補完するメガクチートのM-3考察](/blog/mawile-analysis-m3/)
- [かくとうタイプのメガバシャーモM-3考察](/blog/blaziken-analysis-m3/)
