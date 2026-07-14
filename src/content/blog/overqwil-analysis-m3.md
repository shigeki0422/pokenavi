---
title: '【ポケモンチャンピオンズ】ハリーマン考察 M-3 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率105位のハリーマンを徹底分析。たべのこし46.5%の耐久型が主流で、どくばりセンボン62.8%・どくびし35.0%の毒まき構成と、ちいさくなる34.6%の回避積み型まで実データで解説。エスパー無効のあく/どく複合の活かし方を考察。'
updatedDate: '2026-06-20'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-overqwil-m3.png'
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
  <img src="/images/pokemon/pokemon-0904-00.webp" alt="ハリーマン" />
  <div>
    <h2 style="margin:0 0 8px">ハリーマン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">105位</strong>　特性: <strong>いかく 76.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

シーズンM-3のシングルバトルで、ハリーマンは**使用率105位**を記録。あく/どくの複合タイプはエスパーを無効化しゴースト技も半減し、特性いかく（76.7%）で相手のこうげきを1段階下げる能力を持ちます。どくびし（35.0%）で毒を撒きながらどくばりセンボン（62.8%）で削るサポート兼アタッカーとして、またちいさくなる（34.6%）で回避率を積む型まで複数の構成が採用されています。

特性は**いかく76.7%**が最多で、繰り出し時に相手のこうげきを1段階下げます。すいすい（19.5%）は雨下でのすばやさ2倍を活かす型です。

---

## なぜ今ハリーマンが使用率105位なのか

### 1. いかく＋あく/どくで物理受けと毒まきを同時にこなせる

特性いかく（76.7%）は繰り出し時に相手のこうげきを1段階下げます。あく/どくの複合により**エスパー技を無効化**し、ゴースト技も半減するため、これらを主力とする特殊アタッカーへの繰り出し成功率が高くなります。繰り出した後にどくびし（35.0%）を撒ければ、後続に毒ダメージを蓄積させながら有利な展開を作れます。

### 2. どくびし＋どくばりセンボンで毒サイクルを完結させられる

どくびし（35.0%）は設置後に地に足のついた相手が場に出るたびどく状態にします。どくばりセンボン（62.8%）はどく技・威力60の単発技で、**50%の確率で相手をどく状態にする**追加効果があります。また、相手がすでにどく状態・もうどく状態の場合は威力が2倍（実質120）になります。どくびしで後続を毒状態にしておけば、センボンの威力が2倍で通るため、撒き＋削りの二段構えが成立します。

### 3. かみくだく（46.0%）でぼうぎょダウンを狙いながらあくタイプ一致打点を通せる

かみくだく（46.0%）はあく技・タイプ一致で、20%の確率で相手のぼうぎょを1段階下げます。いかくで相手のこうげきを下げつつ、かみくだくで相手のぼうぎょを下げる両方向の能力操作が、ハリーマンの場持ちと崩し性能を同時に高めています。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">115</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

こうげき115は火力として十分なラインで、タイプ一致のどくばりセンボン・かみくだくに厚みを与えます。ぼうぎょ95はいかくと組み合わせることで物理耐久を実質的に引き上げられます。とくぼう65は低めで、特殊攻撃への耐性は高くありません。すばやさ85は環境の中速帯で、S85以下の相手には先手が取れますが、S90超の高速勢には上から動かれます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

あく/どくの複合により**エスパー技を無効化**し、ゴースト・あく・くさ・どくは×0.5で半減します。弱点はじめん（×2）の1タイプのみと少なく、環境上位でじめん技を主力にするポケモン（ガブリアス等）への後出しは厳禁です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくばりセンボン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">62.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみくだく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">46.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくびし</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">35.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちいさくなる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">34.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じごくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">27.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みちづれ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">25.4%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みがわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">22.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくどく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">21.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.0%</td>
</tr>
</tbody>
</table>
</div>

特性は**いかく76.7%・すいすい19.5%**の二択。いかくは繰り出し時に相手のこうげきを1段階下げる防御的な選択で、すいすいは雨下でのすばやさ2倍を活かすアタッカー向けの選択です。いかく個体が大多数を占めており、雨パーティ以外ではいかくが基本です。

---

## 主要型の解説

性格分布はわんぱく37.4%・ようき22.9%・いじっぱり18.8%の3択が中心です。わんぱく（A↓B↑）はぼうぎょを最大化する耐久型、ようきはすばやさを上げる先手確保型、いじっぱりはこうげきを最大化するアタッカー型です。

### 型1: わんぱく耐久毒まき型（最多採用）

**性格採用率: わんぱく 37.4%**（ぼうぎょ最大化の耐久型。EV最多分布 H32-B32-D2 14.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0904-00.webp" alt="ハリーマン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBわんぱく耐久毒まき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（76.7%）<br>
<strong>性格:</strong> わんぱく（A↓ B↑）<br>
<strong>EV:</strong> H32 B32 D2（採用率14.2%。HPとぼうぎょを最大化）<br>
<strong>持ち物:</strong> たべのこし（46.5%）
</div>
<div>
<strong>技構成:</strong><br>
・どくばりセンボン<br>
・かみくだく<br>
・どくびし<br>
・じごくづき / ちいさくなる
</div>
</div>
</div>

**強み:**

わんぱくでぼうぎょを底上げしつつ、いかくで相手のこうげきをさらに下げることで、物理攻撃への実質耐久が大きく上がります。たべのこし（46.5%）の毎ターン回復と組み合わせることで、物理アタッカーと対面しながらどくびしを撒く余裕を作れます。どくびしを1枚撒いた後は、後続にどく状態を押し付けながら有利なサイクルを展開できます。どくばりセンボンは50%の確率でどく状態を付与でき、どくびしで後続を毒状態にしてあれば威力が2倍になるため、撒き後の打点として設計上の役割が一致しています。

**弱み:**

とくぼう65と低く、特殊アタッカーからの攻撃には耐久が十分ではありません。すばやさに振らないため、S85超の相手（コノヨザル・ガブリアス等）に上から動かれます。弱点のじめん技（ガブリアスのじしん等）は1発で落とされるリスクがあり、地面タイプへの後出しはできません。

---

### 型2: ようき先手確保型（2番目に多い構成）

**性格採用率: ようき 22.9%**（素早さ確保の型。EV最多分布 H2-A32-S32 7.0%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0904-00.webp" alt="ハリーマン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようき先手型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（76.7%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率7.0%。こうげきとすばやさを最大化）<br>
<strong>持ち物:</strong> たべのこし（46.5%）/ きあいのタスキ（5.3%）
</div>
<div>
<strong>技構成:</strong><br>
・どくばりセンボン<br>
・かみくだく<br>
・じごくづき<br>
・どくびし / ちいさくなる
</div>
</div>
</div>

**強み:**

ようき+S32振りによりS実数値を150まで引き上げ、わんぱく型（S無振りでS実数値105）では後手になるS実数値106〜149の中速帯に先手を取れるようになります。こうげきをA32まで振ることでどくばりセンボン・かみくだくの火力が高まり、削り役としての効率が向上します。先手でどくびしを撒いてから動けるため、設置前に相手を行動させるリスクを下げられます。ただしコノヨザル（最速S実数値156）やガブリアス（最速S実数値169）など環境上位の高速勢には依然として先手を取れません。

**弱み:**

わんぱく型と比べてぼうぎょに振らないため、物理耐久が低下します。いかくで相手のこうげきを下げても、ぼうぎょ実数値がわんぱく型より低い分、物理技での削りがより大きくなります。きあいのタスキ（5.3%）採用の場合はたべのこしの継続回復を放棄するため、場持ちが1回限りになります。

---

### 型3: ちいさくなる回避積み型

**性格: いじっぱり 18.8%**（こうげき最大化の積み型。EV最多分布 H32-B2-D32 5.6%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0904-00.webp" alt="ハリーマン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HDいじっぱり回避積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（76.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 B2 D32（採用率5.6%。HPと特防を最大化）<br>
<strong>持ち物:</strong> たべのこし（46.5%）/ オボンのみ（16.7%）
</div>
<div>
<strong>技構成:</strong><br>
・ちいさくなる<br>
・どくばりセンボン<br>
・かみくだく<br>
・どくびし / じごくづき
</div>
</div>
</div>

**強み:**

ちいさくなる（34.6%）で回避率を2段階上げ、相手の攻撃を外させながら戦う型です。D32振りにより特殊耐久を補強し、特殊アタッカーからのちいさくなる積みの隙を広げます。いかくで物理耐久を補助しつつ、ちいさくなるを複数回積めば実質的な被弾頻度を下げて場持ちを延ばせます。たべのこし・オボンのみとの組み合わせで回避ループが成立した際の崩し性能は高くなります。

**弱み:**

回避率が運に依存するため、確実性がわんぱく型・ようき型より低くなります。積む前の1〜2ターンは耐久が不十分な対面が生じます。いじっぱり型はS無振りのため、S85超の相手に積む前に上から動かれると隙が生まれます。ちいさくなるを使う余裕がない対面では、他2型に比べて攻撃性能・耐久性能ともに劣ります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

あく/どくはエスパーを無効化しゴーストを半減するため、シャドーボール等を主力とするゴースト特殊アタッカーへの繰り出しに適し、こちらのかみくだくがゴースト複合に×2で刺さります。一方で弱点のじめん技を持つポケモンへの対面は危険です。

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
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（30位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲンガナイト採用率58.3%が最多のためメガゲンガー前提。メガ後もタイプはゴースト/どくで変化なく、主力のシャドーボール（ゴースト82.8%）・ヘドロウェーブ（どく79.3%）がともに半減。こちらのかみくだくはゴースト複合に×2で刺さる。メガゲンガーS130のようきS実数値200でこちら（S85）より速く先手は取られるが、特性かげふみで交代不可になるため繰り出し後は主力技が半減のまま削り切れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サーフゴー（23位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#d97706;font-weight:bold">△ 条件付き有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のシャドーボール（ゴースト97.4%）が半減。かみくだくがはがね/ゴースト複合に×2で通る。ただしこだわりスカーフ採用率が42.0%と最多で、スカーフ個体には最多性格ひかえめでS実数値204、おくびょうなら223（ハリーマン最速150を大きく上回る）となり先手を取られる。スカーフなし個体（ひかえめS136、おくびょうS149）には先手を取れるが、スカーフ有無を見極めるまでは△有利止まり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0080-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ヤドラン（85位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#d97706;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヤドランナイト採用率61.3%が最多のためメガヤドラン前提（B180/D80）。タイプはみず/エスパーで変化なく、かみくだくがエスパー複合に×2で通る。なまける84.6%・ボディプレス・てっぺき・めいそう24.9%の高耐久受け型が主流で、物理方面（B180）はてっぺきでさらに固められると処理が困難になる。特殊方面はD80と低水準のため、特殊技であれば削りやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）が×2弱点で刺さる。ガブリアスのS102でこちら（S85）より速く、上から弱点技を受ける。繰り出しは禁物</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ムクホーク（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムクホークのブレイブバード（ひこう）は等倍で通り、S100でこちらより速い。ただしいかくで相手のこうげきを下げた後の物理耐久はある程度確保できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）が×2弱点。ラグラージはS60と遅いが、こちらが上から動けてもじめん技の一撃で落ちるリスクがある</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴン複合でどく技が無効。こちらのどくびしも無効（はがねタイプはどくびしの影響を受けない）。かみくだくは等倍止まりで決定打に欠ける。ただしじめん技を持たない個体には安定して行動できる</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2弱点）をS102で先手から受ける。こちらの有効打がなく繰り出しも不可能</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり技（ガブリアスに×4）を持つ枠で先に処理してからハリーマンを展開する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2弱点）を持ち、高いHPと物理耐久でこちらの削りを耐えながら一撃で落とすリスクがある</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技（ラグラージに×4）を持つアタッカーで弱点を突いてから展開する。ラグラージへの直接対面は避ける</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S102の高速じめん/ドラゴン物理打点で、ハリーマンが受けにくいじめん・ドラゴン勢を上から削る役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速ひこうアタッカー。ハリーマンが貯めたどくびしとの組み合わせで削りを蓄積</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">ラグラージ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ウェーブタックル（みず）でほのおタイプ、れいとうパンチでドラゴンタイプへの打点を確保。クイックターンで対面操作しハリーマンの繰り出し機会を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき高速枠。ハリーマンのどくびしが通らないひこうタイプやみずタイプへのでんき打点を確保</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴン複合で広い耐性。どくびしが無効なはがねタイプを別枠で処理する役割</div>
  </div>
</div>

**パーティ構成の基本方針:**

ハリーマンはいかく＋どくびし撒きでサイクルを有利にする前衛役として機能しますが、弱点のじめん技と特殊耐久の低さをパーティ全体でカバーする必要があります。

1. **じめん対策**: こおり技（ガブリアスに×4）・くさ技（ラグラージに×4）を持つ枠で弱点のじめん勢への打点を用意する
2. **どくびし展開の完結**: ひこう・はがねタイプはどくびしが無効なため、これらを処理できる枠を別途確保する
3. **特殊耐久の補完**: とくぼう65の低さをカバーできる特殊受け枠をパーティに加える
4. **高速枠との連携**: ハリーマンがいかくで物理耐久を補助した後、高速アタッカー（ムクホーク・ガブリアス）で一気に展開する

---

## データ分析①：どくびし35.0%が示す「毒まきサイクル」設計の実態

ハリーマンの技採用率を並べると、どくばりセンボン（62.8%）が最多ですが、どくびし（35.0%）との同時採用が多いことが特徴的です。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| どくばりセンボン | 攻撃 | 62.8% | どく付与50%・どく状態時威力2倍 |
| かみくだく | 攻撃 | 46.0% | タイプ一致打点・B低下 |
| どくびし | 変化 | 35.0% | 後続への毒蓄積 |
| ちいさくなる | 変化 | 34.6% | 回避積み |
| じごくづき | 攻撃 | 27.3% | 音技封じ |

どくびし（35.0%）とどくばりセンボン（62.8%）の両方を採用している割合が高いと推定されることは、「センボンで目の前の相手を削りながら、どくびしで後続も毒状態にする」二段構えの設計思想を示しています。特に注目に値するのはちいさくなる（34.6%）の採用率です。毒まきサポートとしての役割と、回避積みによる自己完結した崩し役の役割が約3割の個体で両立されており、**単純な設置サポート役だけでなく、積み型としての運用も一定数存在**していることが採用率から読み取れます。

持ち物はたべのこし（46.5%）が突出して最多で、オボンのみ（16.7%）と合わせると63.2%が回復アイテム採用です。**攻撃寄りの瞬間火力より継続戦闘を重視する運用**が主流です。じごくづき（27.3%）の採用は、特定の音技（エスパーきのみを使う相手等）への対策というよりも、あくタイプ一致打点としてかみくだくとの択の一つとして機能していると考えられます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HBわんぱく耐久毒まき型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">わんぱく 37.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">どくばりセンボン・かみくだく・どくびし・じごくづき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いかく+B振りで物理耐久が高く、どくびし撒きの場持ちが安定</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊耐久が低くS無振りで中速帯に上から動かれやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASようき先手型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 22.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">どくばりセンボン・かみくだく・じごくづき・どくびし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値150までの中速帯への先手圏を確保しつつA32で火力も維持</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">わんぱく型よりぼうぎょ実数値が低く物理技の削りが大きい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HDいじっぱり回避積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり 18.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ちいさくなる・どくばりセンボン・かみくだく・どくびし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">回避積みが決まれば場持ちが大幅に伸び崩し性能が高まる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積む隙がない対面では他型に劣り、回避依存で安定性が低い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ハリーマンはいかく（76.7%）による物理サポートとどくびし（35.0%）の毒まきを組み合わせた前衛サポート役が主流です。弱点はじめんの1タイプのみと少なく、エスパーを無効化しゴーストを半減するタイプ複合がエスパー系特殊アタッカーへの繰り出しを可能にします。

遭遇時はいかく発動を前提に、たべのこし耐久型のどくびし撒き構成（わんぱく HB振り）を第一に警戒します。どくびしを撒かれた後はひこう・はがねタイプで無効化するか、すばやく倒してどくびしの展開を止めることが対策の軸になります。じめん技（ガブリアスのじしん等）が刺さる対面では、積極的にじめん技を通しにいくことでハリーマンの場持ちを削れます。

---

## 関連記事

- [ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [ラグラージのM-3考察](/blog/swampert-analysis-m3/)
- [メガメタグロスのM-3考察](/blog/metagross-analysis-m3/)
