---
title: '【ポケモンチャンピオンズ】ヒスイダイケンキ 考察 M-7 シーズン 使用率40位の4型解説'
description: 'M-7シーズン使用率40位（M-6: 61位）のヒスイダイケンキを考察。特性きれあじ（採用率99.0%）とひけん・ちえなみ（99.2%）を軸にした物理アタッカーの4つの型を比較し、ガブリアスなど苦手、カバルドンなど得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-28'
heroImage: '../../assets/hero-samurott-hisui-m7.png'
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
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ヒスイダイケンキ" />
  <div>
    <h2 style="margin:0 0 8px">ヒスイダイケンキ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">40位</strong>（M-6: 61位）　特性: <strong>きれあじ 99.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのヒスイダイケンキは、あく一致のひけん・ちえなみ（採用率99.2%）とふいうち（81.3%）に、せいなるつるぎ・アクアカッター・アンコール・つるぎのまいなどを組み合わせる物理アタッカーです。M-6からは、アンコール・つるぎのまい・アクアカッターの採用率が上がり、せいなるつるぎ・シェルブレードの採用率が下がりました。

---

## ヒスイダイケンキの基本スペック

<!-- gate:rows start id=base_stats facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">108</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">528</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ゴースト</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

### 特性

<strong>きれあじ（99.0%）</strong>が主流の特性で、切る技の威力が1.5倍になります。主要技のうち対象はひけん・ちえなみ・せいなるつるぎ・アクアカッター・シェルブレードで、ふいうち・クイックターンは対象外です。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひけん・ちえなみ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の場をまきびし状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">81.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。相手が攻撃を選んでおりかつこの技を使ったターン中、まだ攻撃をしていない時でないと失敗する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>せいなるつるぎ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">58.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の能力変化を無視してダメージを与える。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアカッター</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">38.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">きゅうしょアップ+1で攻撃する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">31.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をアンコール状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">29.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃を2段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シェルブレード</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">25.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">50%の確率で相手の防御を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">攻撃した後、手持ちの他のポケモンと交代する。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技構成・持ち物の違いから、4つの型に分けて紹介します。

### 型1：くろいメガネ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ヒスイダイケンキ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">くろいメガネ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きれあじ（99.0%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H18-A32-B2-D6-S8<br>
<strong>持ち物:</strong> くろいメガネ
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・ふいうち<br>
・アクアカッター<br>
・せいなるつるぎ<br>
選択技：シェルブレード
</div>
</div>
</div>

HPととくぼうにもEVを振った型です。持ち物はラムのみの個体もあります。

<!-- gate:rows start id=card:1 facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
**他の型との違い:**

- アンコール型との技の違い：この型はアクアカッター、アンコール型はアンコール
- 持ち物：くろいメガネ（あくタイプの技の威力が1.2倍になる）
- 4つの型で最も高い実数値：HP183・ぼうぎょ102・とくぼう91
- 4つの型で最も低い実数値：すばやさ113
<!-- gate:rows end id=card:1 -->

---

### 型2：アンコール型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ヒスイダイケンキ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アンコール型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きれあじ（99.0%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・ふいうち<br>
・せいなるつるぎ<br>
・アンコール<br>
選択技：アクアカッター
</div>
</div>
</div>

きあいのタスキで1発耐えてから、アンコールで相手の技を縛る型です。

<!-- gate:rows start id=card:2 facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
**他の型との違い:**

- 他の型に無い技：アンコール
<!-- gate:rows end id=card:2 -->

---

### 型3：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ヒスイダイケンキ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きれあじ（99.0%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・ふいうち<br>
・アクアカッター<br>
・つるぎのまい<br>
選択技：せいなるつるぎ
</div>
</div>
</div>

つるぎのまいで攻撃を上げて攻める、きあいのタスキ持ちの型です。持ち物はラムのみの個体もあります。

<!-- gate:rows start id=card:3 facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
**他の型との違い:**

- 他の型に無い技：つるぎのまい
<!-- gate:rows end id=card:3 -->

---

### 型4：スカーフ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ヒスイダイケンキ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> きれあじ（99.0%）<br>
<strong>性格:</strong> ようき<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・シェルブレード<br>
・クイックターン<br>
・せいなるつるぎ<br>
選択技：アクアカッター
</div>
</div>
</div>

こだわりスカーフを持ち、クイックターンで攻撃しながら交代できる型です。

<!-- gate:rows start id=card:4 facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
**他の型との違い:**

- 他の型に無い技：クイックターン
- シェルブレード：この型は必ず持ち、くろいメガネ型では選択技
- 持ち物：こだわりスカーフ（素早さが1.5倍になるが、同じ技しか出せなくなる）
- 4つの型で最も高い実数値：すばやさ225（こだわりスカーフ込み）
- 4つの型で最も低い実数値：こうげき160
<!-- gate:rows end id=card:4 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">くろいメガネ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アンコール型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">スカーフ型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX（ようき・リザードナイトX）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY（ひかえめ・リザードナイトY）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY（おくびょう・リザードナイトY）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（おくびょう・ルカリオナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（のんき・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガセグレイブ（いじっぱり・セグレイブナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロス（いじっぱり・メタグロスナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（ようき・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr class="note"><td colspan="5" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの技・持ち物・性格採用率の変化

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">せいなるつるぎ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">58.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-31.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シェルブレード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">48.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">25.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-23.4pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アンコール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+18.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アクアカッター</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+17.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">29.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+15.7pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ふいうち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+13.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">クイックターン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-9.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+7.3pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物・性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">29.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+24.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">27.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-11.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">くろいメガネ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-9.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-8.7pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+8.6pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">しんちょう（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">0.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ようき（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">22.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-9.1pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
- せいなるつるぎ：90.0%→58.7%（-31.3pt）。記事のすべての型に共通のため、型の増減とは言えません。
- ラムのみ：4.6%→29.5%（+24.9pt）。くろいメガネ型・つるぎのまい型の一部の個体が持つもので、型の増減とは言えません。
- シェルブレード：48.9%→25.5%（-23.4pt）。スカーフ型が持ち、くろいメガネ型でも選択技のため、型の増減とは言えません。
- アンコール：13.2%→31.5%（+18.3pt）。記事の型ではアンコール型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- アクアカッター：21.3%→38.3%（+17.0pt）。記事のすべての型に共通のため、型の増減とは言えません。
- つるぎのまい：13.4%→29.1%（+15.7pt）。記事の型ではつるぎのまい型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- ふいうち：68.3%→81.3%（+13.0pt）。くろいメガネ型・つるぎのまい型・アンコール型と、記事に載せていない型に共通のため、型の増減とは言えません。
- きあいのタスキ：27.9%→16.3%（-11.6pt）。アンコール型・つるぎのまい型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
<!-- gate:rows end id=diff_movers -->

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
<!-- gate:rows start id=weak facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のアクアカッターは乱数2発（>99%）。ガブリアスのじしん（採用率65.5%）は確定2発で、S113対S253（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール型の選択技アクアカッターは確定5発。アシレーヌのムーンフォース（採用率98.3%）は確定2発（ヒスイダイケンキのきあいのタスキ込み）で、最後は優先度+1のアクアジェットで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型の選択技シェルブレードは乱数2発（88%）。ミミッキュのじゃれつく（採用率97.5%）は確定1発で、S113対S148で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ<br><span style="font-size:0.8em;color:#64748b">メガグソクムシャで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のアクアカッターは確定3発。メガグソクムシャのきゅうけつ（採用率77.0%）は確定2発（ヒスイダイケンキのきあいのタスキ込み）で、最後は優先度+1のふいうちで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のふいうちは乱数3発（70%）。メガカイリューの10まんボルト（採用率59.5%）は確定2発で、最後は優先度+2のしんそくで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のひけん・ちえなみは乱数2発（55%）。メガボーマンダのすてみタックル（採用率73.5%）は乱数1発（63%）で、S113対S172で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール型のせいなるつるぎは確定2発。ゴリランダーのグラススライダー（採用率98.1%）は確定2発で、グラスフィールドで優先度+1のグラススライダーで先に動かれ、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のアクアカッターは確定1発。オオニューラのインファイト（採用率98.4%）は確定1発で、S113対S172で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール型の選択技アクアカッターは確定2発。カバルドンのじしん（採用率97.3%）は確定2発で、S137対S67で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のひけん・ちえなみは確定1発。サーフゴーの10まんボルト（採用率32.1%）は確定2発で、S113対S223（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のふいうちは乱数1発（88%）。イダイトウ(オス)のウェーブタックル（採用率89.5%）は確定3発で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のアクアカッターは確定2発（相手のきあいのタスキ込み）。キラフロルのヘドロウェーブ（採用率59.3%）は確定2発で、最後は優先度+1のふいうちで先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くろいメガネ型のふいうちは確定2発（相手のきあいのタスキ込み）。ゲンガーのヘドロウェーブ（採用率71.3%）は確定2発で、優先度+1のふいうちで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ型のせいなるつるぎは確定3発。ブラッキーのイカサマ（採用率96.0%）は確定4発で、S225（スカーフ込み）対S85で先手を取り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でヒスイダイケンキと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" loading="lazy">
    <div class="name">フラエッテ(永遠)</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" loading="lazy">
    <div class="name">ドヒドイデ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" loading="lazy">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フラエッテ(永遠)<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ドヒドイデ<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率7位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ゲンガー<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガゲンガーで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒスイダイケンキの弱点：かくとう技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒスイダイケンキの弱点：くさ技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒスイダイケンキの弱点：でんき技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒスイダイケンキの弱点：むし技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒスイダイケンキの弱点：フェアリー技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">グソクムシャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ボーマンダ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○6</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○6</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ヒスイダイケンキの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ガブリアス＝じしん・かえんほうしゃ・りゅうせいぐん；アシレーヌ＝ムーンフォース・うたかたのアリア・アクアジェット；ミミッキュ＝じゃれつく・かげうち・シャドークロー・ウッドハンマー；グソクムシャ＝ふいうち・きゅうけつ・アイアンヘッド・インファイト；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；ボーマンダ＝すてみタックル・じしん；ゴリランダー＝グラススライダー・ドラムアタック・とんぼがえり・10まんばりき・はたきおとす；オオニューラ＝インファイト・フェイタルクロー・ねこだまし・じごくづき</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=a76a4662032885ed01e3940e85757fdf467978c3 -->
**強み**

- 得意な相手は6体です。使用率上位では、カバルドン（4位）にアクアカッター、サーフゴー（9位）にひけん・ちえなみ、イダイトウ(オス)（10位）にふいうちで勝てます。
- タイプ相性では、ほのお・みず・こおり・ゴースト・あく・はがねを半減以下、エスパーを無効で受けられます。

**弱み**

- 苦手な相手は8体です。使用率上位では、ガブリアス（1位）のじしん、アシレーヌ（2位）のムーンフォース、ミミッキュ（3位）のじゃれつくで先に倒されます。
- 弱点はでんき・くさ・かくとう・むし・フェアリーです。

**型の選び分け**

- 「くろいメガネ型」：アンコール型のアンコールの代わりにアクアカッターを持つ。
- 「アンコール型」：他の型に無い技はアンコール。
- 「つるぎのまい型」：他の型に無い技はつるぎのまい。
- 「スカーフ型」：他の型に無い技はクイックターン。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は40位です（M-6: 61位）。
- 採用率の変化が大きいのはせいなるつるぎ（-31.3pt）・ラムのみ（+24.9pt）・シェルブレード（-23.4pt）です。
<!-- gate:rows end id=summary -->

---

*関連記事：[ガブリアス考察 M-7](/blog/garchomp-analysis-m7/)・[アシレーヌ考察 M-7](/blog/primarina-analysis-m7/)*
