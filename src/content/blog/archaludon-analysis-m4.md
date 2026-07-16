---
title: '【ポケモンチャンピオンズ】ブリジュラス考察 M-4 使用率5位・型別採用率と立ち回り'
description: 'M-4シングルバトルで使用率5位のブリジュラスを分析。10まんボルト+11.0pp・エレクトロビーム-19.3ppと雨パ離れが鮮明。こだわりスカーフ+おくびょうで速度補強する型が台頭。型ごとの採用率・実数値・同居パートナーをデータで解説。'
pubDate: '2026-07-14'
heroImage: '../../assets/hero-archaludon-m4.png'
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
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス（M-4）" />
  <div>
    <h2 style="margin:0 0 8px">ブリジュラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">5位</strong>（M-3も5位）　特性: <strong>じきゅうりょく 68.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-4シーズン時点の集計です

M-4シングルバトルでブリジュラスは**使用率5位**。M-3と同順位を保ちつつも、内部の技構成は大きく変化しています。最大の変化は**10まんボルトが+11.0ppの60.6%に増加**し、**エレクトロビームが-19.3ppの16.9%に急減**したことです。M-3で同居率4位だったペリッパー・3位だったラグラージがM-4では圏外に落ち、雨展開前提のエレクトロビームを選ぶ理由が減ったことがデータに表れています。また**こだわりスカーフ+6.2pp・おくびょう+5.9pp**と速度補強型が台頭しています。

---

## なぜブリジュラスが環境上位に定着しているのか

### 1. はがね/ドラゴンの耐性が環境上位の多くをまとめられる

はがね/ドラゴン複合の弱点はかくとう・じめんの2タイプのみ。環境上位のマスカーニャ（くさ/あく）のくさ技は×0.25と強い耐性を持ちます。でんき技・みず技・ひこう技はいずれも×0.5の半減です。一方でじめん弱点（×2）はガブリアス（環境1位・じしん採用率）が直撃するため、ガブリアスへの受け出しは基本的にできません。耐性の広さとじめん弱点は常にセットで評価する必要があります。

### 2. C種族値125からの3方向特殊打点

ラスターカノン（はがね）・りゅうせいぐん（ドラゴン）・でんき技（10まんボルト/エレクトロビーム）の3タイプで打点を確保します。はがね・ドラゴン・でんきは環境上位の多くに等倍以上を取れるタイプ組み合わせで、単体で完結した特殊アタッカーとして機能します。

### 3. 特性じきゅうりょくで物理被弾を場持ちに変換

採用率68.9%のじきゅうりょくは、技のダメージを受けるたびに防御が1段階上昇します。物理アタッカーに対して被弾しながらB上昇を積み上げ、C125の特殊技でカウンターを取り続けられます。B種族値130（EV無振りで実数値150）との相乗効果で、物理技の削り耐性は高い水準にあります。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

最多EV構成「H2 C32 S32 ひかえめ」では**H167・B150・C194・S137**となります。S137はメガメタグロス（最速S178）・ガブリアス（最速S169）・ミミッキュ（ようきS162）・マスカーニャ（ようきS192）に後手となります。こだわりスカーフを持たせたおくびょう型ではS225となり、これらを上回ります。

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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

---

## 主要な技と採用率（M-4）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ラスターカノン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">74.6%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">76.4%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">+1.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">71.1%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">71.9%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">+0.8pp</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>10まんボルト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">49.6%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">60.6%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#059669">+11.0pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">39.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">37.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">-1.9pp</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ミラーコート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.7%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">19.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">+3.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">圏外</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">19.2%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はどうだん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">26.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">-8.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>エレクトロビーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">36.2%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">-19.3pp</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほえる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.5%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.2%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">+2.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドラゴンテール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.3%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">-1.4pp</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格はひかえめ42.2%・おくびょう18.4%・ずぶとい15.7%・おだやか14.7%。持ち物はオボンのみ30.5%・たべのこし21.7%・しろいハーブ18.5%・こだわりスカーフ15.3%が主流です。

### 型1: ひかえめ耐久火力型（最多採用）

**性格採用率: ひかえめ 42.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ひかえめ耐久火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（68.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）42.2%<br>
<strong>EV:</strong> H2 C32 S32（採用率21.9%）<br>
<strong>持ち物:</strong> オボンのみ（30.5%）／たべのこし（21.7%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（76.4%）<br>
・りゅうせいぐん（71.9%）<br>
・10まんボルト（60.6%）<br>
・ステルスロック（37.9%）またはほえる（16.2%）またはあくのはどう（19.2%）
</div>
</div>
</div>

**強み:**

ひかえめC32でC実数値194。ラスターカノン・りゅうせいぐん・10まんボルトの3枠がM-4ではほぼ固定になっており、4枠目で役割を追加します。M-3と比べてエレクトロビームの枠が10まんボルトに置き換わり、天候依存なしでの安定打点が確保されました。じきゅうりょくで物理被弾のたびにB上昇を積み、高B種族値（130）と合わせて物理アタッカーに対して場持ちします。

**弱み:**

S137は環境速い側（マスカーニャようきS192・ガブリアス最速S169・メガメタグロス最速S178・ミミッキュようきS162）に後手となります。とくぼう65は低く、C125以上の特殊アタッカーからの特殊技は1発で大きなダメージを受けます。

---

### 型2: しろいハーブりゅうせいぐん型

**性格採用率: ひかえめ（持ち物しろいハーブ 18.5%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">しろいハーブ連射型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（68.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32<br>
<strong>持ち物:</strong> しろいハーブ（18.5%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（76.4%）<br>
・りゅうせいぐん（71.9%）<br>
・10まんボルト（60.6%）<br>
・ステルスロック（37.9%）またはあくのはどう（19.2%）
</div>
</div>
</div>

**強み:**

りゅうせいぐん（ドラゴン・威力130・命中90・使用後C2段階低下）の弱点を、しろいハーブ（能力低下を1度だけ自動回復）で補います。1試合でC無消費のりゅうせいぐんを実質2連射できます。型1との差異は、2発のりゅうせいぐんで対面処理力を最大化する点であり、連続した高火力技で2体を処理する展開で型1より優れた結果を出せます。

**弱み:**

しろいハーブ消費後は回復手段が残らず、型1のオボンのみ・たべのこしによる継戦能力には劣ります。2発目以降のりゅうせいぐん使用でCが落ちるため、中盤以降はラスターカノン・10まんボルトへの切り替えが必要になります。

---

### 型3: おくびょうスカーフ型（M-4新興）

**性格採用率: おくびょう 18.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">おくびょうスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（68.9%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）18.4%<br>
<strong>EV:</strong> C32 S32（または H0-C32-S32 調整）<br>
<strong>持ち物:</strong> こだわりスカーフ（15.3%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（76.4%）<br>
・りゅうせいぐん（71.9%）<br>
・10まんボルト（60.6%）<br>
・あくのはどう（19.2%）またはステルスロック（37.9%）
</div>
</div>
</div>

**強み:**

おくびょうS32のS実数値150にスカーフを持たせることでS225となり、ガブリアス最速S169・メガメタグロス最速S178・ミミッキュようきS162を超えられます。ひかえめスカーフ（S205）ではメガメタグロス最速S178を上回れますが、ガブリアススカーフ（S253）には届きません。おくびょうC32のC実数値177は型1のひかえめC194より17低くなります。速度と火力のどちらに比重を置くかが、ひかえめ型との選択軸です。

M-4でこだわりスカーフが9.1%→15.3%・おくびょうが12.5%→18.4%へ増加しており、この型の増加がデータに現れています。

**弱み:**

スカーフを持つため技が固定され、対面ごとに最適な技を選べません。またCがひかえめ型より低い（C177対C194）ため、確定数が1増える相手が存在します。持ち物がスカーフに固定されるためじきゅうりょくによる場持ちに回復手段が加わらず、物理被弾を積み上げてもB上昇だけで耐える展開となります。

---

### 型4: ずぶとい／おだやか耐久型

**性格採用率: ずぶとい 15.7% / おだやか 14.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久振り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（68.9%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）15.7% またはおだやか（D↑ A↓）14.7%<br>
<strong>EV:</strong> H32 B2 D32（8.8%）またはH32 D32 S2（4.8%）<br>
<strong>持ち物:</strong> たべのこし（21.7%）またはオボンのみ（30.5%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（76.4%）<br>
・10まんボルト（60.6%）<br>
・ステルスロック（37.9%）<br>
・ほえる（16.2%）またはドラゴンテール（14.9%）
</div>
</div>
</div>

**強み:**

ずぶとい型（H32 B2 D32）では**H197・B167**と物理耐久を最大化し、じきゅうりょくのB上昇をさらに活かします。おだやか型（H32 D32 S2）ではD128と特殊耐久を補い、とくぼう種族値65の低さをEVで補います。どちらもたべのこし回復と合わせてステルスロック設置・ほえる・ドラゴンテールによる流し役として機能します。型1〜3との差異は、ステルスロック設置を確実に行い後続エースに引き継ぐ展開役として特化している点です。

**弱み:**

Cに補正・投資がなく（ずぶとい・おだやかはC無補正でEV0、C実数値145）、型1のひかえめC194と比較してC49低く、1発確定が2発になる相手が増えます。火力を出す場面が少ないため、アタッカーとして採用する価値は薄く、展開補助後に後続に依存する構成です。

---

## データ分析①：M-3→M-4のでんき技シフト——雨パ依存からの脱却

M-3→M-4で最大の変化はでんき技選択です。

| 指標 | M-3 | M-4 | 変化 |
|---|---|---|---|
| 10まんボルト | 49.6% | **60.6%** | **+11.0pp** |
| エレクトロビーム | 36.2% | 16.9% | -19.3pp |
| ペリッパー（同居率） | 4位 | 圏外 | 大幅低下 |
| ラグラージ（同居率） | 3位 | 圏外 | 大幅低下 |

エレクトロビームは**通常2ターン**かかる溜め技で、雨下のみ1ターンで発動できます。M-3ではペリッパー（同居率4位）・ラグラージ（3位）との雨軸3体が組まれていた背景があります。M-4でペリッパー・ラグラージが同居率圏外に落ちたことで、雨展開なしでの単体運用が前提となり、溜めが必要なエレクトロビームより安定打点の10まんボルトへ需要がシフトしました。

でんき技の採用目的は変わらず（かくとう/ひこう複合への×2・みず系への打点）ですが、天候依存を切ることで**汎用的なアタッカーとして単体採用しやすくなった**点がM-4の変化です。

---

## データ分析②：4枠目の変化——はどうだんからあくのはどうへ

3枠（ラスターカノン+りゅうせいぐん+10まんボルト）が固定化されるにつれ、4枠目の選択が型の個性を決める形になっています。

| 4枠目候補 | M-3 | M-4 | 変化 |
|---|---|---|---|
| ステルスロック | 39.8% | 37.9% | -1.9pp |
| はどうだん | 26.8% | 18.8% | -8.0pp |
| あくのはどう | 圏外 | **19.2%** | — |
| ミラーコート | 16.7% | 19.8% | +3.1pp |
| ほえる | 13.5% | 16.2% | +2.7pp |

はどうだんはかくとうタイプ（威力80・命中100）でかくとう弱点への打点として採用されていましたが、M-4ではあくのはどう（あくタイプ・威力80・命中100・ひるみ20%）に8.0ppの需要が移っています。

あくのはどうが刺さる相手として環境にはゲンガー（ゴースト/どく）があり、あくのはどうで×2を取れます。一方でミミッキュ（ゴースト/フェアリー）にあくのはどうは等倍、マスカーニャ（くさ/あく）には半減です。M-4の同居率1位にミミッキュが上昇している点と照らすと、ミミッキュへの直接打点（ラスターカノンが×2）は確保できており、あくのはどうはゲンガー・あく耐性のないゴーストタイプへの打点として採用が増えたと読めます。

---

## 環境ポケモンへの相性

以下の相性はひかえめH2 C32 S32型（H167・B150・C194・S137）を基準とします。

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
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="ミミッキュ">ミミッキュ（同居率1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（はがね）がゴースト/フェアリーに×2。ようきS162に後手だがばけのかわを剥がしつつ大ダメージを与えられる。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="ガブリアス">ガブリアス（環境1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">×</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2弱点）を採用率39.2%のきあいのタスキ型・23.2%のオボン型問わず放てる。でんき技はじめん複合に無効。最速S169に後手で引く択が必要。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="メタグロス">メガメタグロス（同居率4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ率98.4%でメガ後はがね/エスパー・S110（最速S178）。ブリジュラスS137は最速メガメタグロスS178に後手。りゅうせいぐんはドラゴン技ではがねに半減（×0.5）。有効打に乏しく先手も取れない。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="カバルドン">カバルドン（同居率3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">×</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん単タイプのためでんき技（×0）が無効。最大打点はドラゴン・はがね技（いずれも等倍）。カバルドンのじしんがじめん×2弱点。有効打に乏しくじめん技を受けるリスクが高い。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="アシレーヌ">アシレーヌ（同居率5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリー複合。10まんボルトがみず×2（フェアリーは等倍で合計×2）。S137でアシレーヌ（S実数値110）に先手を取れる。ムーンフォース（フェアリー）はブリジュラスに等倍。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="マスカーニャ">マスカーニャ（同居率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あく複合。最速S123（実数値192）でブリジュラスS137を上回り先手を取られる。主力のトリプルアクセル（こおり）はこおり×2・はがね×0.5で合計等倍にとどまり、有効打には乏しいが先手で削られる点は負担になる。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px" alt="バシャーモ">バシャーモ（環境10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">×</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/かくとう複合。かくとう技がはがね/ドラゴン複合に×2。ほのお技は等倍で通るためかくとう×2弱点が主な脅威。こだわりスカーフ型では先手を取られるリスクもある。</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率上位パートナー（M-4）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ガブリアスへじゃれつく（フェアリー×2）。ブリジュラスが苦手な対面の処理役</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ブリジュラスが有効打を出しにくいカバルドン・ラグラージへのじしん打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロック設置役。ブリジュラスがアタッカーに集中できる展開を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカー枠。フェアリー耐性を持ちブリジュラスと弱点が異なる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ブリジュラスが苦手なかくとう・じめん方面をみず技で補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率6位（M-3：5位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカー枠。スカーフによる対面操作でブリジュラスの起点を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率7位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカーとしてブリジュラスと打点を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率8位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊アタッカーとしてブリジュラスの物理打点と役割を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率9位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">かそくで加速する物理アタッカー。ブリジュラスの後方から積みを狙う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">ラグラージ</div>
    <div class="rate">同居率10位（M-3：3位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/じめん複合。ブリジュラスが苦手なかくとう・じめん方面をみず技で補完</div>
  </div>
</div>

**M-3との最大の違いはペリッパーが圏外に落ちた点**です。M-3ではペリッパー（同居率4位）・ラグラージ（3位）による雨軸が特徴的でしたが、M-4では雨展開前提のエレクトロビームが16.9%まで減少しており、ペリッパーはパートナー構成から消えました。一方でラグラージは順位を3位→10位に落としつつも10位圏内を維持しています。代わりにカバルドン（3位）・メタグロス（4位）といった物理軸のポケモンが上昇し、特殊アタッカーのブリジュラスと物理アタッカーを組み合わせる軸が増えています。

---

## 総評

ブリジュラスはM-4でも使用率5位を維持しつつ、内部構成をM-3から大きく変えました。雨パ依存のエレクトロビームから10まんボルトへのシフト・はどうだんからあくのはどうへの4枠目変化・おくびょうスカーフ型の台頭という3つの変化がデータに明確に現れています。ラスターカノン+りゅうせいぐん+10まんボルトの3枠が固定化し、4枠目と性格・持ち物の選択が型を決める形になっています。じめん弱点（ガブリアス・カバルドン）とでんき無効（じめん複合全般）は構造上解消されないため、ミミッキュ・ガブリアスなどのパートナーで対面補完することが選出を組む前提となります。

---

## 関連記事

- [ブリジュラス考察 M-3](/blog/archaludon-analysis-m3/)
- [ブリジュラス考察 M-2](/blog/archaludon-analysis-m2/)
- [使用率1位 ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)

---

## 検算済み実数値リスト

本記事で使用した実数値（Lv50・個体値31・EV最大32スケール）：

| 型 | H | B | C | D | S |
|---|---|---|---|---|---|
| ひかえめ H2 C32 S32 | 167 | 150 | 194 | — | 137 |
| おくびょう C32 S32 | — | — | 177 | — | 150 |
| おくびょうスカーフ S | — | — | — | — | 225 |
| ひかえめスカーフ S | — | — | — | — | 205 |
| ずぶとい H32 B2 D32 | 197 | 167 | 145 | 117 | — |
| おだやか H32 D32 S2 | 197 | — | 145 | 128 | 107 |
| ガブリアス最速 S32 | — | — | — | — | 169 |
| ガブリアス最速スカーフ | — | — | — | — | 253 |
| ミミッキュ ようき S32 | — | — | — | — | 162 |
| メガメタグロス 最速 S32 | — | — | — | — | 178 |
| マスカーニャ ようき S32 | — | — | — | — | 192 |
