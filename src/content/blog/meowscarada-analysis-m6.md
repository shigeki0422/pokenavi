---
title: '【ポケモンチャンピオンズ】マスカーニャ 考察 M-6 シーズン 使用率13位の解説'
description: 'M-6シーズン使用率13位のマスカーニャを考察。くさ/あくの複合タイプとへんげんじざい・トリックフラワーを軸に、こだわりスカーフ型ときあいのタスキ型の違い、ボーマンダ・カバルドンなど得意/苦手をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-meowscarada-m6.png'
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
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" />
  <div>
    <h2 style="margin:0 0 8px">マスカーニャ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">13位</strong>　特性: <strong>へんげんじざい 83.1%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率・同居率データはすべて2026-09-10時点のものです。

M-6シーズンのマスカーニャは使用率13位。くさ/あくの複合タイプに、物理アタッカーとしてトリックフラワー・トリプルアクセルを主軸とする構成が定着しています。素早さ123という上位クラスの数値を持ち、こだわりスカーフで対面破壊に寄せるか、きあいのタスキ・いのちのたまで先制読みの一撃を狙うかが型の分岐点です。メガ進化は持ちません。

---

## マスカーニャの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">76</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:73%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">110</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:82%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">123</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

A110・S123が突出しており、物理アタッカーとして高い先制性能を持ちます。B70・D70は平均以下で、耐久で受け止める運用には向きません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

むし技には×4の最大弱点を持ち、かくとう・ひこう・どく・ほのお・こおり・フェアリーの6タイプにも×2で刺さります。一方でじめん・ゴースト・みず・くさ・でんき・あくの6タイプは半減で受けられ、エスパー技は無効です。

### 特性

**へんげんじざい（83.1%）**がほぼ固定で採用されています。登場するたび1回だけ、自分が出す技と同じタイプに変化する特性で、たとえば登場後最初にトリプルアクセル（こおり）を使うとこおりタイプに変化し、そのターンはタイプ一致補正が乗ります。毎ターン変化するわけではなく、1回変化した後は別のタイプの技を使ってもタイプは固定されたままです。もう一方の**しんりょく**（16.9%）はHPが最大の1/3以下になるとくさタイプの技の威力が1.5倍になる特性ですが、少数派です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリックフラワー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致。必中・必ず急所に当たるメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリプルアクセル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20/40/60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3回連続攻撃。全弾命中で威力120相当。ドラゴン等への打点として採用</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代し、後続へ対面を引き継ぐ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致。相手が持ち物を持っていると威力1.5倍で、以後の持ち物効果も奪える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。あく一致で相手の攻撃技を読んで先制できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこうへの打点として選ばれる補助的な選択技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場にどくびしを設置。とんぼがえりとの併用が前提の選択技</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：こだわりスカーフ型

**代表的な性格: ようき（全体の性格採用率55.4%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（83.1%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ（59.4%）
</div>
<div>
<strong>技構成:</strong><br>
・トリックフラワー<br>
・トリプルアクセル<br>
・とんぼがえり<br>
・はたきおとす
</div>
</div>
</div>

S実数値288（スカーフ込み）で環境の大半を上から動ける速度を確保し、トリックフラワー（くさ・威力70、必中・確定急所）とトリプルアクセル（こおり・3段技）の2タイプ打点で相手を上から縛ります。とんぼがえりで後続に対面を渡す選択肢も持ちますが、こだわりスカーフは最初に選んだ技に固定される仕様のため、一度技を選ぶとその後の対面では選択肢を変えられないリスクがあります。

**強み:**

A実数値162・S実数値288で、後述のいじっぱり型（S175・スカーフなし）より広い範囲の相手を上から動かせます。技を切り替えられない代わりに、相手のスカーフ非搭載の多くに先手を取って打点を通せます。

**弱み:**

技が固定されるため、選んだ技のタイプで受け止められる相手には打点を変えられず、トリプルアクセルが外れて連続攻撃が止まるとその場で択を絞られます。

---

### 型2：きあいのタスキ/いのちのたま型

**代表的な性格: いじっぱり（全体の性格採用率39.9%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ/いのちのたま型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（83.1%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32-B2-S32<br>
<strong>持ち物:</strong> きあいのタスキ（27.5%）／いのちのたま（9.5%）
</div>
<div>
<strong>技構成:</strong><br>
・トリックフラワー<br>
・トリプルアクセル<br>
・とんぼがえり<br>
・ふいうち
</div>
</div>
</div>

A実数値178（型1のA162より+16）で、技を固定せず場面ごとに打点を選べる自由度を持ちます。きあいのタスキはHP満タンから一撃を耐えて反撃できる保険として、いのちのたまは威力1.3倍で確定数を詰める用途として使い分けられます。ふいうちは優先度+1のため、後手に回っても相手の攻撃前に打点を通せます。

**強み:**

A実数値178と型1のA162より高く、こだわりスカーフのように技を1つに固定されないため、とんぼがえりやふいうちを場面に応じて選べます。

**弱み:**

S実数値175はスカーフを持つ相手には後手に回り、型1のS288のような広範な先制は取れません。いのちのたま採用時は攻撃のたびに最大HPの1/10の反動を受けるため、被弾が重なるとタスキ型より先に落ちやすくなります。

---

## データ分析：技・持ち物採用率から見る構築思想

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>59.4%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.5%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>55.4%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.9%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">64.2%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.0%</td>
</tr>
</tbody>
</table>
</div>

こだわりスカーフ（59.4%）とようき（55.4%）の採用率はほぼ一致しており、素早さを最大化する層が過半数を占めています。一方できあいのタスキ（27.5%）といのちのたま（9.5%）を合わせると37.0%と、非スカーフのいじっぱり型（39.9%）とおおむね対応する規模です。技面では、とんぼがえり（64.2%）が対面操作の主力である一方、ふいうち（27.0%）はきあいのタスキ・いのちのたま型で採用される優先度技で、こだわりスカーフ型にはS実数値288という高い素早さがあるため採用意義が薄く、非スカーフ型に偏って選ばれていると読めます。素早さを固定して押し通すか、耐久・柔軟性を残して打点を選ぶかで、持ち物・性格・技の3つの採用率がセットで動いている構造です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">非スカーフ型のふいうち（採用率27.0%）でも確定4〜5発止まり。グソクムシャの主力のであいがしら（採用率83.0%、優先度+2。ただし登場後最初の技でないと失敗するため初手限定）は確定1発、とんぼがえり（採用率50.9%）でも確定2発で、どちらも先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="メガセグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガセグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位（セグレイブナイト採用率51.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）は確定2〜3発。メガセグレイブの主力きょけんとつげき（採用率79.8%）は確定1発で、先手を取っても倒し切る前に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオZ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（ルカリオナイトZ採用率93.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（採用率96.1%）は確定2〜3発（いのちのたま型で2発）。メガルカリオZの主力はどうだん（採用率75.1%、特殊技）は確定1〜2発。こだわりスカーフ型（S288）は先手を取れますが、きあいのタスキ・いのちのたま型（S175）はメガルカリオZ（S223）に後手を取られ、決め手を欠いたまま先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率59.0%）はこだわりスカーフ・きあいのタスキ型ではそもそも確定圏に入らず、いのちのたま型でも確定4〜5発と決め手を欠きます。ブリジュラスの主力りゅうせいぐん（採用率65.3%）は確定2発で、先手を取っても倒し切る前に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）は確定2発。マスカーニャはスカーフ型（S288）はもちろん非スカーフ型（S175）でもミミッキュ（S148）より速く先手を取れますが、ばけのかわ（採用率100%、1発分のダメージを無効化しHP1/8を消費する特性）で1発分を無効化されるため倒し切れず、返しのじゃれつく（採用率98.1%、フェアリー×2弱点）で確定1発、きあいのタスキ型でも耐えた残りHPを優先度+1のかげうち（採用率96.1%）で削り切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）は確定3〜4発。アーマーガアの主力ブレイブバード（採用率37.6%、ひこう×2弱点）はこちらがこだわりスカーフ・いのちのたま型なら確定1発、きあいのタスキ型でも確定2発で、先手を取っても倒し切る前に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（採用率96.1%）は確定2〜3発かかるのに対し、アローラキュウコンの主力ふぶき（採用率69.1%、こおり×2弱点）は確定1〜2発。こだわりスカーフ型（S288）は先手を取れますが、非スカーフ型（S175）はアローラキュウコンのおくびょう個体（採用率88.6%、S177）に後手を取られ、決め手を欠いたまま先に沈められます</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）が確定1発。メガボーマンダの主力すてみタックル（採用率73.4%）も確定1発です。メガボーマンダはいじっぱり53.2%（メガ後S172）が最多で、こだわりスカーフ・きあいのタスキ・いのちのたま型（S288／S175／S175）のいずれもこの個体に先手を取って一撃で沈められます。ただしようき17.7%＋おくびょう7.2%＝約25%のS189個体には、非スカーフ型（S175）は逆に先制されてしまう点に注意してください（この場合はきあいのタスキ型ならすてみタックルを1発耐えて返り討ちにできます）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）が確定1〜2発（いのちのたま型で1発）。カバルドンの主力じしん（採用率99.3%）は確定3発止まりで、素早さも上回るため先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率59.0%）が確定1〜2発。サーフゴーの主力ゴールドラッシュ（採用率94.3%）も確定1〜2発ですが、非スカーフ型（S175）はサーフゴーの多数派（S136以下）に対して先手を取れます。ただしこだわりスカーフ個体（採用率13.4%、S204）には逆に非スカーフ型が抜かれる点に注意してください</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（採用率96.1%）が確定1発。イダイトウ(メス)の主力ウェーブタックル（採用率96.5%）は確定2発止まりのため、こだわりスカーフ51.1%採用の相手に後手に回っても1発は確実に耐えて確定1発で返せます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（採用率96.1%）が確定1〜2発。ウォッシュロトムの主力ハイドロポンプ（採用率97.1%）は確定3〜4発止まりで、素早さも上回るため先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（採用率96.1%）が確定1発。イエッサン(オス)の主力マジカルシャイン（採用率70.2%）は確定2発止まりのため、こだわりスカーフ60.8%採用の相手に後手に回っても1発は確実に耐えて確定1発で返せます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位（カイリュナイト採用率75.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（採用率90.1%）が確定1発。メガカイリューの主力かえんほうしゃ（採用率66.8%）も確定1発ですが、素早さで上回るため先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でマスカーニャと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**アシレーヌ**（1位）はみず/フェアリーで、マスカーニャの弱点であるフェアリー技への耐性は持ちません。アシレーヌの弱点であるどく・くさ・でんき技のうち、くさ・でんきはマスカーニャが半減で受けられるため、それらの技を撃ってくる相手への受け出し先を用意できる組み合わせです。

**ボーマンダ**（2位）はドラゴン/ひこうで、マスカーニャの弱点であるひこう技への耐性は持ちませんが、マスカーニャの最大弱点であるむし技（×4）とかくとう技を半減で受けられます。逆にボーマンダの弱点であるこおり技はマスカーニャも×2弱点で共通の急所となるため補完にはなりませんが、むし・かくとう技の半減は互いの弱点を補い合う組み合わせです。

**カバルドン**（4位）はじめん単タイプで、でんき技を無効化できます。マスカーニャ自身もでんき技を半減で受けられるため直接の弱点補完にはなりませんが、カバルドンの弱点であるくさ技をマスカーニャが半減で受けられるため、両者で受け出しを分担できる組み合わせです。

---

## まとめ

M-6のマスカーニャは使用率13位ながら、S123の素早さを活かした物理アタッカーとして安定した役割を担っています。

- **こだわりスカーフ型（59.4%）**：S実数値288で対面の大半を上から動かし、トリックフラワー・トリプルアクセルの2タイプ打点で押し切る型
- **きあいのタスキ/いのちのたま型（合計37.0%）**：A実数値178と型1より高い攻撃力を持ち、技を固定せずふいうちなどを状況に応じて選べる型
- **技の採用率**：とんぼがえり（64.2%）で対面操作を担いつつ、ふいうち（27.0%）は非スカーフ型に偏って選ばれる傾向

むし技への×4弱点とかくとう・ひこう・どく・ほのお・こおり・フェアリーへの×2弱点は環境上位に広く存在するため、選出段階でのケアが必要です。一方でエスパー技を無効化し、じめん・ゴースト・みず・くさ・でんき・あく技を半減で受けられる点は、対面操作から後続へつなぐ運用の土台になっています。

---

**関連記事**: [ボーマンダ考察 M-6](/blog/salamence-analysis-m6/)　[カバルドン考察 M-6](/blog/hippowdon-analysis-m6/)
