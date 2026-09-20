---
title: '【ポケモンチャンピオンズ】ルカリオ 考察 M-6 シーズン 使用率6位のわるだくみメガZ解説'
description: 'M-6シーズン使用率6位のルカリオ考察。メガ進化はルカリオナイトZ採用率93.7%が主流で、わるだくみ採用率81.7%とラスターカノン78.8%を軸にした特殊アタッカー型を中心に解説。苦手/得意ポケモンをダメージ計算で検証。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-lucario-m6.png'
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
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" />
  <div>
    <h2 style="margin:0 0 8px">ルカリオ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">6位</strong>　持ち物: <strong>ルカリオナイトZ 93.7%</strong>
    </div>
  </div>
</div>

M-6シーズン、ルカリオは使用率6位につけています（本記事の使用率・採用率データは2026-09-10時点のものです）。メガ進化には**ルカリオナイト**と**ルカリオナイトZ**の2種類のメガストーンがあり、M-6シーズンはルカリオナイトZの採用率が93.7%と圧倒的多数を占めています。ルカリオナイトZは特性がはどうのぼうごに変わり、とくこうが164まで伸びる特殊アタッカー仕様が特徴で、わるだくみ（採用率81.7%）で積んでからラスターカノン・はどうだんの一致技で押し切る構築が主流です。

---

## ルカリオの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガZ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">115</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+49</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+61</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">525</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

ルカリオナイトZに進化すると、とくこうが+49・すばやさが+61と大きく伸びる一方、こうげきは-10と下がります。もう一方のルカリオナイト（採用率5.4%）はこうげき145・ぼうぎょ88まで伸びる物理寄りの種族値配分で、性質が完全に異なります。本記事の苦手/得意判定は、採用率93.7%のメガZを基準にしています。EV最多分布のH2-C32-S32・おくびょう（採用率73.5%）構成では、メガZ後のC実数値は**216**、S実数値は**223**になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点は×2止まりですが、ほのお・かくとう・じめんの3タイプに広く弱点を持ちます。M-6上位ではガブリアス（1位）のじしん、ボーマンダ（2位）のじしん、カバルドン（5位）のじしんが主な脅威です。どくタイプの技はすべて無効で、耐性の幅も広くドラゴン・あくを半減できます。

### 特性

通常特性は**せいしんりょく（82.3%）**で、相手のひるみ・いかくの影響を受けません。メガ進化すると特性は固定で切り替わり、ルカリオナイトZ（採用率93.7%）は**はどうのぼうご**（接触技のダメージを半減）、ルカリオナイト（採用率5.4%）は**てきおうりょく**（一致技の威力が1.5倍ではなく2倍になる）です。てきおうりょくはルカリオナイト側の特性であり、多数派のメガZには、はどうのぼうごによる物理接触技への被弾軽減が主な恩恵になります。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">81.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこうを2段階上げる積み技。全採用技の中で最多</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">78.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致の最大打点。10%の確率で相手の特防を1段階下げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はどうだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう一致の必中技。回避型の相手にも確実に通せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト・エスパータイプへのサブウェポン。20%の確率で相手をひるませる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんくうは</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">45.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。積み終えた後の削り・後続への引き継ぎに使う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっていこうせん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">140</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致の最大火力。使用後に最大HPの1/2の反動を受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー・ゴーストタイプへのサブウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう一致の高火力だが命中不安あり</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### メガZ特殊型（おくびょう 73.5% / ひかえめ 20.6%）

**性格採用率: おくびょう 73.5% / ひかえめ 20.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガZ特殊型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（通常時82.3%）※メガZ後はどうのぼうご<br>
<strong>性格:</strong> おくびょう（S↑ A↓）またはひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（最多分布53.9%）<br>
<strong>持ち物:</strong> ルカリオナイトZ（93.7%）
</div>
<div>
<strong>技構成:</strong><br>
・わるだくみ<br>
・ラスターカノン<br>
・はどうだん<br>
・あくのはどう
</div>
</div>
</div>

わるだくみでとくこうを2段階上げてから、はがね一致のラスターカノン・かくとう一致で必中のはどうだん・ゴースト対策のあくのはどうで打点を撃ち分けます。積んだ後は素早さも確保されているため、多くの相手に対して先に大技を通せます。

**強み:**

おくびょう採用時のS実数値223（メガZ後）は環境上位の非スカーフ勢の大半より速く、C実数値216から、わるだくみ1回（2段階上昇）でさらに火力を伸ばして先に動けます。ひかえめ採用時はS実数値が203に落ちる代わりにC実数値237まで伸び、火力を優先する型になります。

**弱み:**

おくびょう（S223・C216）とひかえめ（S203・C237）は同時に選べないため、先手を優先すればわるだくみ後の確定数が伸びにくく、火力を優先すればS203止まりでスカーフ持ちはもちろん最速メガ勢にも上を取られる場面が出ます。

---

## データ分析：3タイプの技構成は環境上位にどこまで刺さるか

ルカリオの採用技はあく（わるだくみ・あくのはどう）・はがね（ラスターカノン）・かくとう（はどうだん・しんくうは）の3タイプに集約されます。M-6使用率TOP10（ルカリオ自身を除く）のタイプに対する打点の通り方を整理すると、技の使い分けが必要な理由が見えてきます。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手（使用率）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">はがね技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">かくとう技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">あく技</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ボーマンダ（2位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（3位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">グソクムシャ（4位）※</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">カバルドン（5位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（7位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:700">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">セグレイブ（8位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:700">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:700">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サーフゴー（9位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:700">×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ギルガルド（10位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">半減</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:700">×2</td>
</tr>
</tbody>
</table>
</div>

※グソクムシャはメガストーン（グソクムシャナイト）採用率98.9%と圧倒的多数派で、素体のむし/みずからメガ後はむし/はがねに変わります。はがね→むし/はがねは半減、かくとう→むし/はがねは等倍で、素体（むし/みず）基準の倍率とは異なります。上表はメガ後の数値です。

サーフゴー・ギルガルドのはがね/ゴースト複合に対しては、かくとう技（はどうだん・しんくうは）が無効になる一方、あくのはどうは×2で通ります。採用率59.6%のあくのはどうは単なるサブウェポンではなく、環境9位・10位という上位にいる2体のゴースト複合に対して、主力技の中では実質あくのはどうのみが等倍以上で通る技として機能しています（採用率8.0%のシャドーボールも通りますが少数派です）。一方セグレイブ（8位）は、はがね・かくとうの両方が×2で刺さる有利タイプに見えますが、実際の対面はセグレイブのじしん（採用率87.6%）にじめん×2で弱点を突かれ、こちらのラスターカノン確定2発に対し確定1発で先に倒される不利な相手です。タイプ相性表と実戦の勝敗は必ずしも一致しません。ガブリアス・カバルドン・アシレーヌ寄りの相手には3タイプとも等倍〜半減止まりで、わるだくみによる火力の底上げに依存する場面が多くなります。

---

## 前シーズン比較：M-5からの型転換

M-5時点のルカリオは使用率29位に留まっていましたが、M-6では6位まで順位を上げています。その背景にはメガストーンの構成変化があります。

- **M-5**：メガストーンは「ルカリオナイト」96.4%が主流。技構成もインファイト（73.3%）・つるぎのまい（64.4%）・コメットパンチ（56.0%）・しんそく（51.2%）と、こうげきを積んで押し切る物理アタッカー運用でした
- **M-6**：「ルカリオナイトZ」（93.7%）が新規導入され、はどうのぼうご特性・とくこう164の特殊アタッカー型が主流に移行。技もわるだくみ（81.7%）・ラスターカノン（78.8%）・はどうだん（75.1%）と物理型から入れ替わっています

「ルカリオナイトZ」はM-6シーズンで初めて登場したアイテムで（M-2〜M-5の採用データには存在しません）、新規メガストーンの追加が使用率6位への急上昇の主因と考えられます。物理型（ルカリオナイト）からの乗り換えではなく、新しい型そのものが環境入りした形です。

---

## 苦手なポケモン

本記事の苦手/得意判定は、採用率93.7%のルカリオナイトZに限定した上で、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスの持ち物は多数派のメガZ（ガブリアスナイトZ、採用率35.0%）が最多です。メガZ同士は素早さ同数（S223）で先手を保証できず、かえんほうしゃ（採用率24.9%）を受けつつ確定2発対2発の五分に留まります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）を当てても確定2発。ボーマンダのじしん（採用率67.5%）はじめん×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもラスターカノン（採用率78.8%）は確定4発と決め手を欠き、アシレーヌの最大打点となるムーンフォース（採用率99.1%）の確定2発で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもはどうだん（採用率75.1%）は確定3発止まり。グソクムシャのインファイト（採用率24.9%）はかくとう×2でこちらの弱点を突き、確定2発で先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもラスターカノン（採用率78.8%）は確定4発止まり。カバルドンの最大打点となるじしん（採用率99.3%）はじめん×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもあくのはどう（採用率59.6%）は確定3発止まり。ギルガルドの最大打点となるポルターガイスト（採用率54.0%）の確定2発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスの持ち物は多数派のゴツゴツメット（採用率36.9%、非メガ）が最多です。先手を取ってあくのはどう（採用率59.6%）を当てても確定4発と決め手を欠き、ギャラドスの最大打点となるじしん（採用率53.4%）はじめん×2でこちらの弱点を突き、確定2発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってはどうだん（採用率75.1%）を当てても確定2発。メガリザードンXのかえんほうしゃ（採用率42.9%）はほのお×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもあくのはどう（採用率59.6%）は確定4発と決め手を欠き、メガリザードンYのかえんほうしゃ（採用率42.9%）はほのお×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はどうだん（採用率75.1%）を放つ前に上から動かれ、エースバーンのかえんボール（採用率98.7%）はほのお×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもあくのはどう（採用率59.6%）は確定4〜5発（EVによる）と決め手を欠き、ウルガモスのほのおのまい（採用率70.6%）はほのお×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）を当てても確定2発。オオニューラの最大打点となるインファイト（採用率99.4%）はかくとう×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリューの持ち物は多数派のメガストーン（カイリュナイト、採用率75.2%）が最多です。先手を取ってラスターカノン（採用率78.8%）を当てても確定3発と決め手を欠き、カイリューのかえんほうしゃ（採用率66.8%）はほのお×2でこちらの弱点を突き、確定1発で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技・かくとう技はいずれもセグレイブに×2で通る有利タイプに見えますが、先手を取ってラスターカノン（採用率78.8%）を当てても確定2発。セグレイブの最大打点となるじしん（採用率87.6%）はじめん×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウォッシュロトムの持ち物は多数派のオボンのみ（採用率33.5%）・たべのこし（採用率32.9%）が上位で、こだわりスカーフ（採用率15.2%）は少数派です。多数派のS106に対しルカリオ（S223）は先手を取れますが、はどうだん（採用率75.1%）は確定3発と決め手を欠き、相手のハイドロポンプ（採用率97.1%）の確定2発に先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってはどうだん（採用率75.1%）を当てても、きあいのタスキ（採用率88.6%）で初撃を耐えられます。パーモットの主力インファイト（採用率77.5%、かくとう×2）で確定2発を作られたうえ、マッハパンチ（採用率51.1%、優先度+1）で先に詰められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってあくのはどう（採用率59.6%）を当てても確定2発。メタグロスの最大打点となるじしん（採用率43.5%）はじめん×2でこちらの弱点を突き、確定1発で先に倒されます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

本記事の苦手/得意判定は、採用率93.7%のルカリオナイトZに限定した上で、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってはどうだん（採用率75.1%、かくとう×2）で確定2発。ブリジュラスの主力10まんボルト（採用率63.1%）は確定3発に留まり、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）で確定2発。ミミッキュの最大打点となるじゃれつく（採用率98.1%）は確定3発に留まり、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャの主流はこだわりスカーフ（採用率59.4%、S262）で、ルカリオ（S223）は後手を取られます。それでもはどうだん（採用率75.1%）は確定1発の一撃で、マスカーニャの最大打点トリックフラワー（採用率96.1%）の確定3発を待たずに沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）で確定2発。キラフロルの最大打点となるだいちのちから（採用率57.6%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってあくのはどう（採用率59.6%）で確定2発。イダイトウ(メス)の最大打点となるウェーブタックル（採用率96.5%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってはどうだん（採用率75.1%）で確定2発。ゲッコウガの最大打点となるなみのり（採用率33.7%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）で確定1発。アローラキュウコンの最大打点となるムーンフォース（採用率47.1%）は確定2発に留まり、決まる前に先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってラスターカノン（採用率78.8%）で確定2発。ゴリランダーの最大打点となる10まんばりき（採用率50.3%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サザンドラの主流はこだわりスカーフ（採用率86.7%、S225）で、ルカリオ（S223）は後手を取られます。それでもはどうだん（採用率75.1%）は確定1発の一撃で、サザンドラの最大打点かえんほうしゃ（採用率73.3%）の確定2発を待たずに沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってはどうだん（採用率75.1%）で確定3発。アーマーガアの最大打点となるボディプレス（採用率54.3%）も確定3発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってあくのはどう（採用率59.6%）で確定2発。ラウドボーンの最大打点となるフレアソング（採用率99.4%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってあくのはどう（採用率59.6%）で確定2発。イエッサン(オス)の最大打点となるワイドフォース（採用率99.4%）も確定2発ですが、先制で押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でルカリオと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**カバルドン**（1位）はじめん単タイプで、ステルスロックやあくびのサポートを担います。

**ボーマンダ**（2位）はドラゴン/ひこうで、ルカリオの弱点3種のうちじめん技を無効化し、ほのお技も半減で受けられます。ルカリオの弱点をボーマンダが肩代わりできる補完関係です。

**アシレーヌ**（4位）はみず/フェアリーで、ルカリオの弱点であるかくとう・ほのおタイプの技を半減で受けられ、被弾を分散できます。

---

## まとめ

M-6のルカリオは使用率6位で、ルカリオナイトZ（採用率93.7%）によりとくこう164の特殊アタッカーとして運用されるのが最大の特徴です。

- **メガZ特殊型が圧倒的主流**：わるだくみ（採用率81.7%）で積んでから、ラスターカノン・はどうだん・あくのはどうの3タイプで打点を撃ち分けます
- **技の使い分けが刺さる範囲を決める**：あくのはどうはサーフゴー・ギルガルドのはがね/ゴースト複合に×2で通る一方、かくとう技はこの2体に無効。3タイプの技構成でも環境上位を網羅しきれない場面があります
- **主流技同士で判定すると得意12体・苦手17体**：ブリジュラス・ミミッキュ・マスカーニャ・キラフロル・イダイトウ(メス)・ゲッコウガ・アローラキュウコン・ゴリランダー・サザンドラ・アーマーガア・ラウドボーン・イエッサン(オス)には有利に立てる一方、ガブリアス・ボーマンダ・アシレーヌ・グソクムシャ・カバルドン・セグレイブ・ギルガルド・ギャラドス・メガリザードンX/Y・エースバーン・ウルガモス・オオニューラ・カイリュー・ウォッシュロトム・パーモット・メタグロスには弱点タイプを突かれる、または速度面で不利になります

苦手表の多くはほのお技×2（メガリザードンX/Y・エースバーン・ウルガモス・カイリュー）やじめん技×2（ガブリアス・ボーマンダ・カバルドン・ギャラドス・セグレイブ・メタグロス）が原因です。マスカーニャ・サザンドラのようにこだわりスカーフ持ちが多数派の相手には、ルカリオ（S223）が後手に回りますが、いずれもはどうだんの一撃で相手の確定数を待たず沈められるため得意表に残ります。一方ウォッシュロトムは主流のオボンのみ・たべのこし相手なら先手を取れるものの、はどうだんが確定3発止まりで決定打を欠き、相手のハイドロポンプに先に沈められるため苦手表に入っています。同居率2位のボーマンダ・4位のアシレーヌのように異なる弱点タイプを持つポケモンをパーティに編成しておくと、ほのお・じめん技持ちへの弱点を補完できます。

---

*関連記事：[メガボーマンダ考察 M-6](/blog/salamence-analysis-m6/)、[ガブリアス考察 M-6](/blog/garchomp-analysis-m6/)*
