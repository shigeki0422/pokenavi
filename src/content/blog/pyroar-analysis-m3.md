---
title: '【ポケモンチャンピオンズ】カエンジシ考察 M-3 使用率90位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率90位のメガカエンジシを徹底分析。メガ後ほのおのたてがみ・C129/S126の特殊アタッカーとして、おくびょう74.2%・かえんほうしゃ89.7%を軸にした実データで解説。ねっさのだいちでじめん/はがね補完も可能。環境での立ち回りまで紹介します。'
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
      使用率: <strong style="color:#e67e22">90位</strong>　特性: <strong>メガ後ほのおのたてがみ</strong>（メガ前きんちょうかん 67.3%）
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、カエンジシは**使用率90位**を記録。メガ進化後はC129・S126と特殊アタッカーとして十分な数値を持ち、**ほのお/ノーマルのタイプ一致技にハイパーボイス（みがわり貫通）を加えた打点構成**が特徴です。

メガ後の特性は**ほのおのたてがみ**で固定され、ほのおタイプ技を受けても素早さが下がらず、こおりタイプによる「こおり」状態にもならない（凍りつかない）耐性を得ます。メガ前の特性はきんちょうかん67.3%が最多ですが、メガ進化した時点でほのおのたてがみへ上書きされる点に注意が必要です。

---

## なぜカエンジシが環境に存在するのか

### 1. メガ後S126で環境中速帯を大きく上回る

メガ後S126（おくびょうS32の場合S実数値195）は環境の多くのポケモンを上回ります。おくびょう採用率74.2%はこの素早さを最大化する意図を反映しており、上から動いてほのお技を通す展開を主軸とします。

### 2. メガ後ほのおのたてがみでほのお技・凍結に強い

メガ後の特性ほのおのたてがみは、ほのおタイプ技を受けても素早さが低下せず、こおりによる凍り状態にもならない耐性を与えます。S195の素早さを維持したまま、ミラー対面のほのお技や相手のこおり技による足止めを受けにくく、上から殴る展開を崩されにくい点に寄与します。

### 3. ハイパーボイス（音技）でみがわりを貫通する

ハイパーボイス（採用率51.6%）はノーマルタイプ一致の音技で、みがわりを貫通する特性があります。みがわりを張って様子見する相手に対し、みがわりごと削れるため消耗戦でのアドバンテージを取りやすい点が通常の技と異なります。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">89.7%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">63.6%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ハイパーボイス</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">51.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ねっさのだいち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">36.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ニトロチャージ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">35.7%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>にほんばれ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.3%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>おにび</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくび</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">12.4%</td>
</tr>
</tbody>
</table>
</div>

かえんほうしゃ（89.7%）が事実上の確定技で、オーバーヒート（63.6%）との2枚採用が主流です。オーバーヒートはC2段階低下というデメリットがあるため、倒し切れる相手に使い切る運用が基本で、かえんほうしゃとの使い分けが技選択の軸となります。

---

## 主要型の解説

性格分布はおくびょう74.2%・ひかえめ22.6%の2択が中心で、S最大化のおくびょうが圧倒的多数を占めます。

### 型1: おくびょうCS型（最多採用）

**性格採用率: おくびょう 74.2%**（S最大化。EV最多分布 H2-C32-S32 55.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0668-00.webp" alt="カエンジシ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSおくびょう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きんちょうかん（67.3%）※メガ後ほのおのたてがみ<br>
<strong>性格:</strong> おくびょう（S↑ C↓）<br>
<strong>EV:</strong> H2-C32-S32（採用率55.2%）<br>
<strong>持ち物:</strong> カエンジシナイト
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

おくびょうS32でメガ後S実数値195となり、環境の多くのポケモンを上から殴れます（メガゲンガーのメガ後S実数値200など高速メガ勢には先手を取られます）。ひかえめ型（S実数値178）が先手を取れないS120前後の相手——最速マスカーニャ（S実数値192）など——にも上から動けるのが、おくびょう型を選ぶ最大の理由です。ほのお技が×2で通る相手を上から削れるため、被弾前に試合の主導権を握れます。

**弱み:**

おくびょう（C↓）によりとくこうが低下するため、ひかえめ型と比べてC実数値が約1割低くなります。ひかえめ型では1発で倒せる相手を2発必要とする場面が生じ、上から殴れる代わりに削り切る速度で劣ります。

---

### 型2: ひかえめ火力型（2番目に多い構成）

**性格採用率: ひかえめ 22.6%**（C最大化。EV最多分布 B2-C32-S32 8.1%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0668-00.webp" alt="カエンジシ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSひかえめ火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きんちょうかん（67.3%）※メガ後ほのおのたてがみ<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> B2-C32-S32（採用率8.1%）<br>
<strong>持ち物:</strong> カエンジシナイト
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

ひかえめC32でC実数値199となり、おくびょう型（C162）より約23%高い火力が出ます。この火力差により、おくびょう型では2発必要な相手を1発で倒せる場面が生じます。

**弱み:**

おくびょう型（S実数値195）と比べてS実数値が178と低く、おくびょう型が抜ける最速マスカーニャ（S実数値192）に先手を取れなくなります。上から動ける範囲がおくびょう型より狭まる分、被弾してから動く場面が増えます。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あく複合で、ほのお技×2で通る。メガ後S195は最速マスカーニャ（S実数値192）を上回り、上から処理できます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガハッサム（31位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/はがね複合でほのお技が×4で通る。メガ後S実数値127に対しS195で先手を取れ、かえんほうしゃ1発で大きく削れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガメタグロス（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/エスパー複合でほのお技が×2で通る。メガ後S実数値162に対しS195で先手を取れます（ただしかくとう技を持つ個体には弱点を突かれるため注意）</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴーストタイプには当方ノーマル技が無効。ほのお技は等倍で通る。相手のシャドーボールはノーマルタイプ無効で通らないが、メガゲンガー（メガストーン採用率58.9%）はメガ後S実数値200でカエンジシのS195を上回り先手を取られる。ヘドロウェーブ（採用率80.6%）等の別打点を持つ個体には注意が必要です</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率92.7%）・ウェーブタックル（同75.1%）の高火力物理で押され、こちらのほのお技はメガラグラージ（みず/じめん）に半減されます</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんきは無効化されるため、くさ×4で刺さるマスカーニャ（4位）・メガニウム（37位）のくさ技で処理する</td>
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
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず×2弱点でたきのぼり（採用率89.5%）が刺さり、こちらのほのお技はみず/ひこう複合に半減される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき×4で刺さるライチュウ（5位）・ウォッシュロトム（23位）のでんき技で上から処理する</td>
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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわでワンクッション。カエンジシが苦手な対面でじゃれつく・かげうちで圧力をかける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ/あくで高速物理。カエンジシが苦手なみずタイプにくさ技で打点を持ちつつ補完関係を形成</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0227-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでじめん無効・かくとう半減。カエンジシのかくとう・じめん弱点を補う耐久枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

カエンジシはほのお・ノーマルのタイプ一致打点を活かしつつ、4弱点（みず・かくとう・いわ・じめん）をパーティ全体でカバーする必要があります。

1. **じめん対策**: ひこうタイプや浮遊持ちでガブリアスのじしんを無効化する枠を用意する
2. **みず対策**: くさ・でんき技を持つポケモンで水タイプの相手に先手を取れる枠を確保する
3. **かくとう対策**: ひこう・エスパー・フェアリー技でかくとうタイプに圧力をかける枠を添える

---

## データ分析①：技採用率の二重構造が示す「一撃と持続」の使い分け

カエンジシの技採用率を並べると、ほのお技2枚体制が浮かび上がります。

| 技 | タイプ | 採用率 | 役割 |
|---|---|---|---|
| かえんほうしゃ | ほのお | 89.7% | 安定技・持続火力（やけど10%）|
| オーバーヒート | ほのお | 63.6% | 一撃最大火力（C2段階低下）|
| ハイパーボイス | ノーマル | 51.6% | みがわり貫通・補完打点 |
| ねっさのだいち | じめん | 36.0% | はがね・でんき補完 |
| ニトロチャージ | ほのお | 35.7% | S上昇技 |

かえんほうしゃ（89.7%）とオーバーヒート（63.6%）の同時採用率が高いことは、「倒し切りたい相手にオーバーヒート・それ以外にかえんほうしゃ」という使い分け運用が主流であることを示しています。オーバーヒートのC2段階低下デメリットを許容してでも最大火力を持つ判断が、約6割のプレイヤーが取る択となっています。

ねっさのだいち（36.0%）とニトロチャージ（35.7%）の採用率がほぼ拮抗していることは、第4の技枠を「はがね/でんき補完打点」か「S上昇」かで選択している実態を数値で示しています。メガ後S195でも上を取れない相手やこだわりスカーフ持ちを意識してSを積むか、ほのお技が通りにくいはがねへの打点を確保するかで、構築の方向性が二分されていると読めます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">おくびょう 74.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">かえんほうしゃ・オーバーヒート・ハイパーボイス・ねっさのだいち/ニトロチャージ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値195で多くの相手に先手を取れる（メガゲンガー200等の高速メガ勢には届かない）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C↓でひかえめ型より火力が約1割低い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CSひかえめ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ 22.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">かえんほうしゃ・オーバーヒート・ハイパーボイス・ねっさのだいち/ニトロチャージ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C実数値199で一発で倒せる範囲が広がる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値178でおくびょう型が抜けるマスカーニャ等のS120前後の相手に先手を取れない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

カエンジシはメガ後C129・S126という特殊アタッカーとして機能し、ほのお/ノーマルのタイプ一致技にハイパーボイスのみがわり貫通を組み合わせた打点構成が軸です。メガ後ほのおのたてがみでほのお技・凍結に強く、おくびょうS32でのS195先手展開が主流の動きとなります。

弱点はみず・かくとう・いわ・じめんの4タイプに及ぶため、パーティ単位でのカバーが必要です。使用率90位というポジションは、火力・素早さは環境水準を満たすものの弱点タイプの多さから採用コストが生じていることを反映しています。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [はがね/フェアリーで補完するメガクチートのM-3考察](/blog/mawile-analysis-m3/)
- [かくとうタイプのメガバシャーモM-3考察](/blog/blaziken-analysis-m3/)
