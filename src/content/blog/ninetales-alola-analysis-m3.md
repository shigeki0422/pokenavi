---
title: 'キュウコン（アローラ）考察 M-3 使用率9位の採用理由と型別立ち回り'
description: 'チャンピオンズM-3使用率9位アローラキュウコンを徹底解説。オーロラベール98.0%・ひかりのねんど90.5%で壁展開の軸として機能。H2-D32-S32おくびょう型の実数値・苦手な相手・パートナー構成までDBデータで解説します。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-ninetales-alola-m3.png'
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
  <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" />
  <div>
    <h2 style="margin:0 0 8px">アローラキュウコン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>　特性: <strong>ゆきふらし 99.6%</strong>
    </div>
  </div>
</div>

シーズンM-3のシングルバトルで、アローラキュウコンは**使用率9位**。すばやさ109のこおり/フェアリータイプで、**オーロラベール採用率98.0%・ひかりのねんど採用率90.5%**というデータが示す通り、「あられ展開+オーロラベール」による壁設置が存在理由の中心です。ガブリアス（1位）・マスカーニャ（3位）といった物理アタッカーが環境上位に並ぶM-3では、物理・特殊両方を半減するオーロラベールを先手で貼ることが後続の全体的な生存率を上げます。

---

## データ分析①：オーロラベール一択という極端な技採用分布

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">分類</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーロラベール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フリーズドライ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>84.6%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふぶき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>74.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">54.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いたみわけ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.6%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミストフィールド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.4%</td>
</tr>
</tbody>
</table>
</div>

オーロラベール98.0%はこのポケモンの役割をほぼ一言で説明します。あられ状態でのみ使用できるオーロラベールは、物理・特殊の両方のダメージを5ターン（ひかりのねんど持参で8ターン）半減する壁技で、リフレクターとひかりのかべの効果を1枚で兼ねる点が他の壁要員との差別化要素です。

フリーズドライ（84.6%）とふぶき（74.8%）は両方採用が基本。フリーズドライは威力70・命中100で確実な打点を確保し、みずタイプに×2で通る点が独特です（ふぶきはみずに半減（×0.5））。ふぶきは威力110・命中70ですが、ゆきふらしによってあられ状態が続く限り命中100%になります。

アンコール（54.9%）は相手の変化技・積み技を封じて行動を縛る技。オーロラベール展開後に後続が積みやすい状況を作る役割を担います。ムーンフォース（49.6%）はあく・かくとうタイプへのフェアリー打点として採用されます。こおり技が等倍にとどまるこれらのタイプに対し、フェアリー×2で確実に打点を取れます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おくびょう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

**おくびょう（82.7%）**が主流。C無振り・とくこう↓でとくこう実数値を下げ、すばやさを最大化してオーロラベールを先手で展開することを優先します。壁を先手で貼ることが最優先の役割であり、とくこうの低下は妥協です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H2-D32-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">29.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう・すばやさ全振り+HP最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A1-C1-D32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう・すばやさ全振り、余りをA・Cへ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-C2-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り（物理偽装型）</td>
</tr>
</tbody>
</table>
</div>

最多のH2-D32-S32（29.7%）はとくぼうD32・すばやさS32を最大化した特殊耐久重視型。フリーズドライやふぶきは採用するが、ダメージより壁展開を優先する構成と一致します。

### 代表型の実数値（H2-D32-S32・おくびょう）

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>150</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう（おくびょう↓）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>152</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ（おくびょう↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>177</strong></td>
</tr>
</tbody>
</table>
</div>

すばやさ177（おくびょうS32）は、環境1位のガブリアス（ようきS32で実数値169）を上回ります。ただしマスカーニャ（ようきS32で実数値192）には先手を取られます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきふらし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆきがくれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.4%</td>
</tr>
</tbody>
</table>
</div>

**ゆきふらし**は場に出ると5ターンのあられ状態を発生させる特性。あられ中はふぶきの命中が70%→100%になり、またオーロラベールの使用条件（あられ状態）を自力で満たせます。ゆきがくれ（あられ中に回避率が上がる）の採用は0.4%で実質固定です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">73</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">109</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">505</span>
  </div>
</div>

すばやさ109・とくぼう100が突出しており、残りは水準以下。こうげき67は特筆する値ではなく、こおりのつぶて（3.1%）の採用もほぼ皆無のため物理での打点は期待されていません。HP73・ぼうぎょ75は耐久面の穴で、特に物理技への耐久は低水準です。オーロラベールを自分自身に展開して生存率を上げながら仕事を完了させる設計です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

**はがね×4**が最大の穴。メタグロス（4位）のバレットパンチ（87.5%）やブリジュラス（5位）のはがね技が×4で刺さります。ほのお×2はリザードン（7位）・バシャーモ（10位）の主力技が直撃します。ドラゴン無効はガブリアス（1位）のげきりんを完全に無効化できる耐性で、対ガブリアスで役立ちます。

---

## 主な型

### 型1：ひかりのねんど型（90.5%）—— オーロラベール展開の軸

オーロラベールの効果を8ターンに延長するひかりのねんどを持たせた最多数派型。相手に対して十分な壁ターン数を確保することが後続の全抜きルートを広げます。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>ひかりのねんど型（壁展開）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>ゆきふらし（99.6%）<br>
    <strong>性格：</strong>おくびょう　<strong>EV：</strong>H2-D32-S32<br>
    <strong>持ち物：</strong><span style="display:inline-block;width:24px;height:24px;background-image:url('/images/items/item-sprite.png');background-size:480px 648px;background-position:-264px -216px;vertical-align:middle;flex-shrink:0"></span> ひかりのねんど<br>
    H149 / B95 / C90 / D152 / S177
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>オーロラベール / フリーズドライ / ふぶき / アンコール（ムーンフォース）
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    先発でオーロラベールを展開し、後続の積みアタッカーに壁8ターンを渡す。フリーズドライとふぶきは対ガブリアス（こおり×4）の打点として機能し、壁展開後も最低限の攻撃参加ができます。アンコールで相手の変化技を封じて壁展開の時間を稼ぐ場面も想定されます。
  </p>
</div>

---

## データ分析②：M-2→M-3シーズン比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">指標</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>使用率順位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">9位</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オーロラベール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">88.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>98.0%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふぶき採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">74.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">69.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84.6%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">49.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">54.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.4%</td>
</tr>
</tbody>
</table>
</div>

使用率がM-2の52位からM-3の9位へ大幅に上昇した背景には、環境上位の物理アタッカー（ガブリアス1位・マスカーニャ3位）増加が考えられます。オーロラベール採用率は88.5%→98.0%へさらに収束し、壁展開役としての役割が固定化されています。一方でわるだくみは26.9%→3.4%と激減しており、M-2では存在した「自分で積んで攻める型」がM-3では淘汰されました。フリーズドライ（69.9%→84.6%）とアンコール（41.5%→54.9%）の採用率上昇は、みずタイプへの打点確保と相手の積み技妨害を重視する方向への変化を示しています。

---

## データ分析③：持ち物の集中度——ひかりのねんど90.5%への高い集中

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
    <span style="display:inline-block;width:24px;height:24px;background-image:url('/images/items/item-sprite.png');background-size:480px 648px;background-position:-264px -216px;vertical-align:middle;margin-right:6px"></span>
    <strong>ひかりのねんど</strong>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.5%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/items/item-0275-tasuki.png" alt="きあいのタスキ" style="width:24px;height:24px;vertical-align:middle;margin-right:6px">
    きあいのタスキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.8%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span style="display:inline-block;width:24px;height:24px;background-image:url('/images/items/item-sprite.png');background-size:480px 648px;background-position:-456px 0px;vertical-align:middle;margin-right:6px"></span>
    とけないこおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/items/item-0158-obon.png" alt="オボンのみ" style="width:24px;height:24px;vertical-align:middle;margin-right:6px">
    オボンのみ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/items/item-0287-scarf.png" alt="こだわりスカーフ" style="width:24px;height:24px;vertical-align:middle;margin-right:6px">
    こだわりスカーフ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.7%</td>
</tr>
</tbody>
</table>
</div>

ひかりのねんど90.5%はアローラキュウコンの持ち物選択が実質固定に近いことを示します。ひかりのねんどはリフレクター・ひかりのかべ・オーロラベールの持続を5ターンから8ターンに延長する効果を持ち、オーロラベールと組み合わせることで最大のターン数を確保できます。スカーフ（0.7%）・とけないこおり（2.5%）はニッチな採用にとどまり、対戦中に「ひかりのねんどを持っていない」と判断するのは少数の対戦のみです。

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
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/エスパーに対しこおり・フェアリー両方×0.5でダメージが通りにくい。一方バレットパンチ（先制・採用率87.5%）がはがね×4で大ダメージ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンに対しこおりは等倍・フェアリーも等倍で削りにくく、こちらのはがね×4弱点をはがね技で突かれる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">リザードン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガリザードンY（採用率75.9%）のほのお技が×2弱点で刺さる。こおり技はほのお/ひこうに等倍どまり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（85.0%）でほのお×2。こおり技はほのお/かくとうに×0.5半減で通らない</td>
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
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" loading="lazy">
    <div class="name">ムクホーク</div>
    <div class="rate">同居9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居10位</div>
  </div>
</div>

**ガブリアス（同居1位）**はオーロラベールで受けた後に先手で積み技を展開したり、設置技と攻撃技を組み合わせて立ち回る典型的な壁展開後エースです。ガブリアスのじしんはアローラキュウコンのはがね×4弱点を持つメタグロス・ブリジュラスへの打点も兼ねます。

**バシャーモ（同居2位）**は壁8ターン中にすばやさを積んで全抜きを目指す積みアタッカーの筆頭。バシャーモが苦手なみず・じめん・ひこうへの対応はパーティ単位で構成します。

**メタグロス（同居3位）**・**ブリジュラス（同居10位）**はアローラキュウコンのはがね×4弱点を一見埋めないように見えますが、壁展開後の詰め役として同パーティに入ります。はがね技でこちらを倒しに来る相手を、メタグロスやブリジュラスが逆に処理する役割分担です。

**ミミッキュ（同居4位）**はばけのかわで一撃を凌いで壁中につるぎのまいを積み全抜きを狙います。ゴースト/フェアリーはフリーズドライが等倍どまりですが、壁中に積むことを目的に採用されます。

---

## まとめ

M-3のアローラキュウコンは使用率9位で、**オーロラベール98.0%・ひかりのねんど90.5%**の採用率データが示す通り、壁展開に特化したサポート運用が確立されています。

- オーロラベール（98.0%）+ ひかりのねんど（90.5%）で物理・特殊両方のダメージを8ターン半減
- ゆきふらし（99.6%）でふぶきの命中を100%に引き上げ、あられ条件を自力で満たす
- S177（おくびょうS32）でガブリアス（S169）に先手を確保しつつ、オーロラベールを先手で展開
- はがね×4・ほのお×2という明確な弱点があり、環境4位のメタグロス・7位のリザードンに対しては壁展開前に倒されるリスクが高い

後続エース（ガブリアス・バシャーモ・ミミッキュ等）が壁を活かして詰める構築に組み込むことが前提の採用です。

---

## 関連記事

- [ガブリアス考察 M-3 — 使用率1位の持ち物・技変化を解説](/blog/garchomp-analysis-m3/)
- [マスカーニャ考察 M-3](/blog/meowscarada-analysis-m3/)
