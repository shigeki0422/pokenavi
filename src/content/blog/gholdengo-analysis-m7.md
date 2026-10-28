---
title: '【ポケモンチャンピオンズ】サーフゴー 考察 M-7 シーズン 使用率9位の型解説'
description: 'M-7シーズン使用率9位（M-6も9位）のサーフゴー考察。耐久型・速攻型・こだわりスカーフを持つ型（採用率21.5%）の3型を比較し、型別の強み弱みとアーマーガア・キラフロルなど得意なポケモン、メガリザードンXなど苦手なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-26'
heroImage: '../../assets/hero-gholdengo-m7.png'
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
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" />
  <div>
    <h2 style="margin:0 0 8px">サーフゴー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>　特性: <strong>おうごんのからだ 100.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのサーフゴーは使用率9位です（M-6シーズン最終も9位）。はがね/ゴーストの複合タイプに、シャドーボール・ゴールドラッシュを中心とした特殊打点と、わるだくみでの積みを組み合わせる運用が主流です。耐久に寄せたEV配分で粘る個体と、すばやさに投資して積み後に押し切る個体、こだわりスカーフで技を1つに固定して上から撃つ個体が並立しています。

---

## サーフゴーの基本スペック

<!-- gate:rows start id=base_stats facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43.5%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">133</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">91</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">84</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">550</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

種族値はC133が最大で、特殊アタッカーとしての打点を支えます。種族値B95・D91はバランスの取れた数値で、種族値S84は型によって投資先が分かれます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はあく・じめん・ほのお・ゴーストの4タイプ（いずれも×2）です。このうちじめんは、耐久型・速攻型が持つふうせんで無効にできます。

### 特性

<strong>おうごんのからだ（100.0%）</strong>が唯一の特性で、相手からの変化技が効かない効果です。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゴールドラッシュ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">91.0%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">使用後、自分の特攻を2段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻を2段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じこさいせい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">62.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2回復する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">32.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をまひ状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">トリック</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手と自分が持っている道具を入れ替える。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルシャイン</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に3つの型を紹介します。

### 型1：耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> おうごんのからだ（100.0%）<br>
<strong>性格:</strong> ずぶとい（おだやかも同程度）<br>
<strong>EV:</strong> H32-D24-S10<br>
<strong>持ち物:</strong> ふうせん
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ゴールドラッシュ<br>
・わるだくみ<br>
・じこさいせい<br>
選択技：10まんボルト
</div>
</div>
</div>

ずぶとい・EV H32-D24-S10でHP・とくぼうを中心に耐久へ配分した個体です。ふうせんは攻撃技を1度受けるまでじめん技を無効化できる持ち物で、弱点4タイプのうちじめんへの保険になります。

<!-- gate:rows start id=card:1 facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
**他の型との違い:**

- 3つの型で最も高い実数値：HP194・ぼうぎょ126・とくぼう135
- 3つの型で最も低い実数値：とくこう153・すばやさ114
<!-- gate:rows end id=card:1 -->

---

### 型2：速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> おうごんのからだ（100.0%）<br>
<strong>性格:</strong> おくびょう（ひかえめも同程度）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> ふうせん
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ゴールドラッシュ<br>
・わるだくみ<br>
・じこさいせい<br>
選択技：10まんボルト
</div>
</div>
</div>

技構成は耐久型と同じシャドーボール・ゴールドラッシュ・わるだくみ・じこさいせいですが、EVをH2-C32-S32まで振り分け、S149・C185（わるだくみ後C370相当）まで速度と火力に投資します。

<!-- gate:rows start id=card:2 facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
**他の型との違い:**

- 4つの技・持ち物・実数値のどれにも、他の型に無い要素はありません
<!-- gate:rows end id=card:2 -->

---

### 型3：こだわりスカーフ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> おうごんのからだ（100.0%）<br>
<strong>性格:</strong> おくびょう（ひかえめも同程度）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ゴールドラッシュ<br>
・10まんボルト<br>
・トリック<br>
選択技：じこさいせい・パワージェム・マジカルシャイン・きあいだま
</div>
</div>
</div>

わるだくみを持たず、こだわりスカーフでS223まですばやさを引き上げて技を1つに固定して上から撃つ構成です。

<!-- gate:rows start id=card:3 facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
**他の型との違い:**

- 他の型に無い技：トリック
- 10まんボルト：この型は必ず持ち、耐久型・速攻型では選択技
- 持ち物：こだわりスカーフ（素早さが1.5倍になるが、同じ技しか出せなくなる）
- 3つの型で最も高い実数値：すばやさ223（こだわりスカーフ込み）
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">耐久型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">速攻型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">こだわりスカーフ型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（ひかえめ・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（いじっぱり・いのちのたま）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（しんちょう・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー（いじっぱり・いのちのたま）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体7件は除く。メタグロスは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析①：カバレッジ計算（使用率TOP10へのタイプ相性）


<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手（使用率順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュ（はがね）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき）</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアス（1位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#f1f5f9;color:#64748b;font-weight:bold">無効</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（2位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（3位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">カバルドン（4位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#f1f5f9;color:#64748b;font-weight:bold">無効</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（5位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">リザードン（6位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（7位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（8位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)（10位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td></tr>
</tbody>
</table>
</div>

---

## データ分析②：M-6からの技・持ち物採用率の変化

M-6シーズン最終（2026-09-23）とM-7現在（2026-10-24）の技・持ち物採用率を比較すると、以下のような変化が見られます。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">トリック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+11.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">10まんボルト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">29.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+2.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">わるだくみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">84.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">73.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-10.8pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドーボール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">98.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">97.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-1.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゴールドラッシュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">93.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">91.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-2.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じこさいせい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">63.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">62.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-1.3pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+12.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+6.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ふうせん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">71.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">51.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-20.1pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
- ひかえめ：65.6%→45.3%（-20.3pt）。耐久型・速攻型・こだわりスカーフ型の一部の個体が選んでいるもので、型の増減とは言えません。
- ふうせん：71.3%→51.2%（-20.1pt）。耐久型・速攻型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- こだわりスカーフ：9.4%→21.5%（+12.1pt）。こだわりスカーフ型だけが持つため、この変化はその型の増減を示します。
- トリック：8.2%→19.6%（+11.4pt）。こだわりスカーフ型だけが持つため、この変化はその型の増減を示します。
- わるだくみ：84.3%→73.5%（-10.8pt）。耐久型・速攻型に共通のため、型の増減とは言えません。
- おくびょう：16.4%→26.9%（+10.5pt）。速攻型・こだわりスカーフ型が選んでいるほか、記事に載せていない型の個体も選んでいるため、型の増減とは言い切れません。
- おだやか：5.1%→14.5%（+9.4pt）。耐久型の一部の個体が選んでいるもので、型の増減とは言えません。
- たべのこし：9.4%→15.7%（+6.3pt）。耐久型の一部の個体が持つもので、型の増減とは言えません。
<!-- gate:rows end id=diff_movers -->

対戦相手としては、こだわりスカーフを持つ個体やトリックを採用する個体に当たる場面が増えており、上から一撃を受けたり、持ち物を奪われたりする展開を想定しておく必要があります。

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
<!-- gate:rows start id=weak facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型の選択技パワージェムは確定2発。メガリザードンXのフレアドライブ（採用率30.5%）は確定2発で、S223（スカーフ込み）対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型の選択技パワージェムは確定3発。メガカイリューのかえんほうしゃ（採用率65.2%）は確定2発で、S223（スカーフ込み）対S152で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型のゴールドラッシュは乱数4発（98%）。イエッサン(オス)のマジカルフレイム（採用率95.0%）は確定3発で、S114対S161で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型のゴールドラッシュは確定2発。マスカーニャのはたきおとす（採用率66.0%）は確定2発で、S114対S288（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型のシャドーボールは乱数2発（68%）。エースバーンのかえんボール（採用率99.3%）は確定1発で、S114対S171で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型のシャドーボールは確定2発。メガライチュウYのでんじほう（採用率96.5%）は確定2発で、S114対S200で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型のシャドーボールは確定3発。ヒートロトムのオーバーヒート（採用率96.3%）は確定2発で、S114対S106で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型の選択技マジカルシャインは確定1発。サザンドラのあくのはどう（採用率98.5%）は乱数1発（81%）で、S223対S225で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻型のシャドーボールは確定3発（相手のオボンのみ込み）。ブリジュラスの10まんボルト（採用率63.9%）は確定4発で、S149対S105で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻型の選択技10まんボルトは確定2発。アーマーガアのブレイブバード（採用率27.5%）は確定5発で、S149対S78で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型のシャドーボールは確定2発。キラフロルのだいちのちから（採用率63.1%）は確定2発で、S223（スカーフ込み）対S151で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐久型の選択技10まんボルトは確定3発。ブラッキーのイカサマ（採用率96.0%）は乱数3発（94%）で、S114対S85で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻型のゴールドラッシュは確定1発。アローラキュウコンのふぶき（採用率66.9%）は確定5発で、S149対S177で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でサーフゴーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率5位・メガボーマンダで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率6位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メタグロス<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガメタグロスで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カイリュー<br><span style="font-weight:normal;font-size:0.85em">同居率9位・メガカイリューで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガルカリオZで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴーの弱点：あく技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴーの弱点：じめん技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴーの弱点：ほのお技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴーの弱点：ゴースト技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ライチュウ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サザンドラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝サーフゴーの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンX＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；イエッサン(オス)＝ワイドフォース・マジカルフレイム・マジカルシャイン；マスカーニャ＝トリックフラワー・トリプルアクセル・はたきおとす・とんぼがえり；エースバーン＝かえんボール・とびひざげり・ダストシュート・ふいうち・とんぼがえり；ライチュウ＝でんじほう・きあいだま・ねこだまし・ボルトチェンジ；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト；サザンドラ＝あくのはどう・りゅうせいぐん・かえんほうしゃ・とんぼがえり</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=6a948e9cfc9b7edab398b50587670cb292811697 -->
**強み**

- 得意な相手は5体です。使用率上位では、ブリジュラス（8位）・キラフロル（18位）にシャドーボール、アーマーガア（11位）に10まんボルトで勝てます。
- タイプ相性では、くさ・こおり・ひこう・エスパー・むし・いわ・ドラゴン・はがね・フェアリーを半減以下、ノーマル・かくとう・どくを無効で受けられます。

**弱み**

- 苦手な相手は8体です。使用率上位では、メガリザードンX（6位）のフレアドライブ、カイリュー（12位）のかえんほうしゃ、イエッサン(オス)（16位）のマジカルフレイムで先に倒されます。
- 弱点はほのお・じめん・ゴースト・あくです。

**型の選び分け**

- 「耐久型」：3つの型で最も高い実数値はHP194・ぼうぎょ126・とくぼう135。
- 「速攻型」：4つの技・持ち物・実数値のどれにも、他の型に無い要素はありません。
- 「こだわりスカーフ型」：他の型に無い技はトリック。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は9位です（M-6: 9位）。
- 採用率の変化が大きいのはふうせん（-20.1pt）・こだわりスカーフ（+12.1pt）・トリック（+11.4pt）です。
<!-- gate:rows end id=summary -->

関連記事: [ガブリアス M-7シーズン考察](/blog/garchomp-analysis-m7/) / [サーフゴー M-6シーズン考察](/blog/gholdengo-analysis-m6/)
