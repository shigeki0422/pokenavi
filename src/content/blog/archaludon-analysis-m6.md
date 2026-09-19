---
title: '【ポケモンチャンピオンズ】ブリジュラス 考察 M-6 シーズン 使用率7位の解説'
description: 'M-6シーズン使用率7位のブリジュラスを考察。はがね/ドラゴンの複合タイプにラスターカノン・りゅうせいぐん・10まんボルトを揃えた特殊型が主流で、M-5の使用率4位から7位へ後退しつつもずぶとい・ステルスロック採用が伸びた実態、カバルドン・メガボーマンダなど型別の得意/苦手をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-archaludon-m6.png'
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
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" />
  <div>
    <h2 style="margin:0 0 8px">ブリジュラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>（M-5: 4位）　特性: <strong>じきゅうりょく 75.2%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも同日のスナップショットを使用しています。

M-6シーズンのブリジュラスは使用率7位。はがね/ドラゴンの複合タイプに、ラスターカノン・りゅうせいぐん・10まんボルトの3種の特殊技を揃えた高火力の特殊アタッカーが主流です。種族値はA105・C125とどちらも高く、物理・特殊いずれの型も組めますが、実際の技採用は特殊技が上位を占めています。M-5の使用率4位からは後退していますが、技構成自体の骨格は維持されたまま、ステルスロックやドラゴンテールなど耐久・対面操作寄りの技の採用が伸びている点は後述のデータ分析で詳しく扱います。

---

## ブリジュラスの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:87%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">130</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:83%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">125</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

A105・C125と物理・特殊どちらも高水準ですが、B130の物理耐久に対してD65の特殊耐久は薄く、耐久面は物理寄りです。S85は最速スカーフ勢や上位アタッカーには後手に回るものの、グソクムシャ・カバルドン・ギルガルド・アーマーガア・ラウドボーンなど中速帯には先手を取れる数値で、一概に打点勝負一辺倒にはなりません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
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

弱点はかくとう・じめんの2タイプ（いずれも×2）に絞られる一方、耐性は8タイプに及び、くさは×0.25まで軽減、どくは無効です。使用率6位のルカリオ（かくとう/はがね）ははどうだん（かくとう・威力80、採用率75.1%）を主力にしており、後述の苦手表のとおりこの一致弱点技が主要因で不利がついています。かくとう・じめんを主力にする相手には選出段階での見極めが必要です。

### 特性

<strong>じきゅうりょく（75.2%）</strong>が主流です。物理・特殊どちらの技を受けても発動しますが、上がるのはぼうぎょのみで、物理耐久だけが積み上がっていきます。もう一方の<strong>がんじょう（24.8%）</strong>は、HPが満タンの時に一撃でひんしになるダメージを受けてもHPを1残して耐える特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致のメインウェポン。10%で相手のとくぼう低下</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">65.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン一致の最大火力。使用後に自分のとくこうが2段階下がる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこう複合等への追加打点。10%で相手をまひ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置し、交代の度に弱点倍率に応じた固定割合ダメージを与える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-6。控えがいる相手をランダムに交代させ、ステルスロックの被害を広げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はどうだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手に必ず命中する。かくとう技はあく・はがね複合に×4で通るため、これらのタイプへの打点として採用</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほえる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-6。控えがいる相手をランダムに交代させる。ドラゴンテールと役割が近い選択技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エレクトロビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1ターン溜めてから攻撃する高火力技。10まんボルトより高威力だが隙が大きい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー・ゴースト複合への追加打点。20%で相手をひるませる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐんの自己弱化を避けたい場面向けのドラゴン一致技</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：特殊アタッカー型

**代表的な性格: ひかえめ（全体の性格採用率36.7%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（75.2%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> オボンのみ（29.7%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン<br>
・りゅうせいぐん<br>
・10まんボルト<br>
・はどうだん
</div>
</div>
</div>

ラスターカノン（はがね・威力80）・りゅうせいぐん（ドラゴン・威力130）・10まんボルト（でんき・威力90）の3タイプ打点を揃え、相手のタイプに応じて撃ち分けます。はどうだん（かくとう・威力80、必中）は回避を積んだ相手やあく複合への保険で、りゅうせいぐんの自己C低下を避けたい場面の代替枠にもなります。

**強み:**

ひかえめ・EV H2-C32-S32のC実数値は**194**（HP167・S137）。3タイプの一致・準一致打点でほとんどの相手に等倍以上を取れ、単純な打点勝負で押し切る立ち回りが可能です。

**弱み:**

ステルスロック・ドラゴンテールを採用しないため、後述の型2が持つ設置・対面操作の役割は持てません。またH・Dに振らないため、耐久全般では型2に劣ります。

---

### 型2：ステルスロック型

**代表的な性格: おだやか（全体の性格採用率18.5%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ステルスロック型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> がんじょう（24.8%）<br>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32-B2-D32<br>
<strong>持ち物:</strong> たべのこし（22.2%）
</div>
<div>
<strong>技構成:</strong><br>
・ステルスロック<br>
・ドラゴンテール<br>
・ラスターカノン<br>
・10まんボルト
</div>
</div>
</div>

ステルスロック（いわ・設置技）を撒き、ドラゴンテール（ドラゴン・威力60、優先度-6）で控えのいる相手を強制交代させて被害を広げる型です。がんじょうを採用すれば、HP満タンの状態から瀕死になるはずの一撃を受けてもHP1で耐え、ステルスロックの設置を確実に通せます。ラスターカノン・10まんボルトは打点として残しつつ、りゅうせいぐん・はどうだんは採用せず対面操作を優先します。

**強み:**

おだやか・EV H32-B2-D32のD実数値は**128**（型1のD85より+43）で、特殊耐久は型1を大きく上回ります。さらにがんじょうを採用すれば、HP満タンの状態から瀕死になるはずの一撃を確実に耐えられるため、ステルスロックの設置や対面操作を安定して通せます。ステルスロック・ドラゴンテールは型1では採用しない技で、設置と対面操作という型1にない役割を担えます。

**弱み:**

C実数値は**145**（型1のC194より-49）で、一致最大打点のりゅうせいぐんを採用しないため決定力は型1に劣ります。S実数値も**105**（型1のS137より-32）で、最速勢には後手に回りますが、グソクムシャ・カバルドン・ギルガルド・アーマーガア・ラウドボーンなど中速帯には先手を取れます。

---

## データ分析：M-5→M-6 採用データの変化

※M-5列のデータはM-5シーズン最終スナップショット（2026-09-09時点）、M-6列のデータは2026-09-10時点を使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>7位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">下降</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>63.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+7.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+7.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴンテール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>24.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>24.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+7.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しろいハーブ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.1pp</td>
</tr>
</tbody>
</table>
</div>

使用率はM-5の4位からM-6で7位へ後退していますが、ラスターカノン・りゅうせいぐんの一致技採用率はほぼ横ばいで、アタッカー型の骨格自体は崩れていません。一方でステルスロック（+7.3pp）とドラゴンテール（+5.7pp）、そして耐久寄りの性格であるずぶとい（+7.0pp）・おだやか（型2の代表的な性格）がそろって伸びており、ステルスロック型（型2）の比率が増加したことがうかがえます。これに対応する形でひかえめ（-3.5pp）とオボンのみ（-4.9pp）、りゅうせいぐんの自己弱化を軽減するしろいハーブ（-2.1pp）が減少しており、瞬間火力に振った構成から設置・耐久を重視した構成へ分布が動いたシーズンといえます。使用率の後退幅（3位分）に対して技・性格の変化は数pp規模にとどまるため、「性能自体が弱くなった」というより「役割の比率が変わった」と読むのが妥当です。

---

## 苦手なポケモン

使用率TOP35を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはブリジュラスが上ですが、10まんボルト（採用率63.1%）は確定5発と決め手を欠き、メガグソクムシャのインファイト（採用率24.9%、かくとう×2弱点）の確定1発に先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはブリジュラスが上ですが、ラスターカノン（採用率75.1%）は確定5発止まり。カバルドンの主力じしん（採用率99.3%、じめん×2弱点）は確定4発で先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（ルカリオナイトZ採用率93.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%）は確定3発。メガルカリオの主力はどうだん（採用率75.1%）は必中で確定2発のため、後手のブリジュラスは先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%）とサーフゴーの主力シャドーボール（採用率99.9%）はともに確定4発ですが、素早さで劣るブリジュラスが後手に回り先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはブリジュラスが上ですが、10まんボルト（採用率63.1%）は確定5発と決め手を欠き、ギルガルドのせいなるつるぎ（採用率36.6%）の確定2発に先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%）は確定2発。メガリザードンYの主力かえんほうしゃ（採用率42.9%）は確定1発で、先手を取られて押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）とエースバーンの主力とびひざげり（採用率89.0%）はともに確定2発ですが、素早さで劣るブリジュラスが後手に回り先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後攻交代技のドラゴンテール（採用率24.6%）とウルガモスの主力ほのおのまい（採用率70.6%）はともに確定4発。優先度-6のドラゴンテールは常に後攻となるため、先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）とオオニューラの主力インファイト（採用率99.4%、かくとう×2弱点）はともに確定2発ですが、素早さで劣るブリジュラスが後手に回り先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）とパーモットの主力インファイト（採用率77.5%、かくとう×2弱点）はともに確定2発ですが、素早さで劣るブリジュラスが後手に回り先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位（メタグロスナイト採用率98.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%）は確定5発。メガメタグロスの主力じしん（採用率43.5%、じめん×2弱点）は確定4発で、素早さで劣るブリジュラスは先に押し切られます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP35を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）で確定1発。メガボーマンダの主力じしん（採用率67.5%）は確定2発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="メガセグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガセグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位（セグレイブナイト採用率51.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）で確定2発。メガセグレイブの主力じしん（採用率87.6%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（採用率75.1%）で確定3発。ミミッキュの主力じゃれつく（採用率98.1%）はB130・じきゅうりょくによる防御上昇で決め手を欠くうえ、ばけのかわ（ばけたすがた時は技のダメージの代わりに最大HP1/8を消費してばれたすがたに変わる）の分だけ実戦では確定数+1ターン必要になり、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）で確定2発。マスカーニャの主力はたきおとす（採用率59.0%）は確定4発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さで勝り、10まんボルト（採用率63.1%）が確定3発。アーマーガアの主力ボディプレス（採用率54.3%）はB130の高耐久で決め手を欠き、先手を取り続けられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%、×4弱点）で確定2発。ギャラドスの主力じしん（採用率53.4%）は確定4発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率63.1%）で確定2発。イダイトウ(メス)の主力ウェーブタックル（採用率96.5%）はB130の高耐久で決め手を欠き、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）で確定1発。メガリザードンXの主力かえんほうしゃ（採用率42.9%）は確定2発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（採用率75.1%）で確定1発。アローラキュウコンの主力ふぶき（採用率69.1%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さで勝り、りゅうせいぐん（採用率65.3%）が確定2発。ラウドボーンの主力フレアソング（採用率99.4%）も確定2発ですが、先手を取って押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）が確定4発なのに対し、ウォッシュロトムの主力ハイドロポンプ（採用率97.1%）は確定5発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率65.3%）で確定2発。イエッサン(オス)の主力マジカルシャイン（採用率70.2%）は確定4発止まりで、先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でブリジュラスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**グソクムシャ**（3位）はむし/みずで、弱点のひこう・いわ・でんきをいずれもブリジュラスが耐性（×0.5）で受けられます。逆にブリジュラスの弱点であるかくとう・じめんはグソクムシャも半減（×0.5）で受けられるため、これらの技を撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**アシレーヌ**（4位）はみず/フェアリーで、弱点のどくをブリジュラスが無効化できます。逆にブリジュラスの弱点であるかくとうはアシレーヌが半減（×0.5）で受けられるため、どく・かくとうを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**ミミッキュ**（6位）はゴースト/フェアリーで、弱点のはがねをブリジュラスが耐性（×0.5）で受けられます。逆にブリジュラスの弱点であるかくとうはミミッキュが無効化できるため、はがね・かくとうを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**イダイトウ(オス)**（8位）はみず/ゴーストで、弱点のくさ・でんきをいずれもブリジュラスが耐性（くさ×0.25、でんき×0.5）で受けられます。逆にブリジュラスの弱点であるかくとうはイダイトウ(オス)が無効化できるため、くさ・でんき・かくとうを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

---

## まとめ

M-6のブリジュラスはM-5の4位から7位へ使用率を落としましたが、ラスターカノン・りゅうせいぐんの一致2打点を軸とする技構成自体は継続しており、性能面で大きく弱体化したわけではありません。

- **使用率4位→7位**：ラスターカノン(75.1%)・りゅうせいぐん(65.3%)の主力2技はほぼ横ばいで、アタッカーとしての骨格は維持されています
- **ステルスロック+7.3pp・ドラゴンテール+5.7pp・ずぶとい+7.0pp**：設置・対面操作寄りの型2の比率が増加しています
- **ひかえめ-3.5pp・オボンのみ-4.9pp・しろいハーブ-2.1pp**：瞬間火力型（型1）の一部が耐久寄りの構成へ移行しています

A105・C125の高い両攻撃種族値を背景に、りゅうせいぐんの一致打点で押し切る型1か、ステルスロック・ドラゴンテールで対面を作る型2かは、パーティ内での役割に応じた選択になります。弱点はかくとう・じめんの2タイプに絞られる一方、この2タイプを主力にする使用率上位（メガグソクムシャ・カバルドン・メガルカリオ等）には共通して不利がつくため、選出段階でのケアが引き続き求められます。
