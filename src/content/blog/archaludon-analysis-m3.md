---
title: 'ブリジュラス考察 M-3 型別採用率と立ち回り'
description: 'チャンピオンズM-3使用率4位ブリジュラスを解説。特性じきゅうりょく75.7%・ひかえめ49.6%が最多構成。りゅうせいぐん＋しろいハーブでC無消費2連射を狙う型、ステルスロックで展開を作る補助型など役割の違いをデータで解説。'
updatedDate: '2026-06-27'
pubDate: '2026-06-27'
heroImage: '../../assets/hero-archaludon-m3.png'
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
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">ブリジュラス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">4位</strong>（M-2は2位）　特性: <strong>じきゅうりょく 75.7% / がんじょう 24.1%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン時点の集計です

M-3シングルバトルでブリジュラスは**使用率4位**。M-2の2位からわずかに順位を落としましたが、依然として環境上位を支えるはがね/ドラゴンの特殊アタッカーです。特性**じきゅうりょく**（技のダメージを受けるたびに防御が1段階上がる）が75.7%で主流。ラスターカノン74.6%・りゅうせいぐん72.6%の2大火力技に加え、10まんボルト48.5%・エレクトロビーム40.1%のでんき技が場面を選んで採用される構成です。

---

## なぜブリジュラスが環境上位に定着しているのか

### 1. はがね/ドラゴンの耐性が環境上位をまとめて受けられる

ブリジュラスのタイプはかくとう・じめん以外の弱点が少なく、どく・むし・ひこう・でんき・みず・くさ・いわ・エスパー・はがね・ノーマルを等倍以下で受けます。環境1位ガブリアスのドラゴン技（りゅうせいぐん等）・じしんは、ドラゴン×1とじめん×2でそれぞれ等倍・弱点となります。しかしガブリアスの主力じしんは**じめん×2（弱点）**であるため、ガブリアスを「ブリジュラスで受ける」運用はできません。一方で使用率3位マスカーニャのくさ技にはがね（×0.25）、あく技には等倍と有利な耐性を持ち、マスカーニャに対して場に居続けやすい点が強みです。

### 2. C種族値125の特殊火力とじきゅうりょくの相乗効果

C種族値125（ひかえめC32実数値177）から放つラスターカノン・りゅうせいぐんは、環境トップ帯の多くに確実なダメージを与えます。特性じきゅうりょくにより技のダメージを受けるたびに防御が1段階上がる（物理・特殊問わず）ため、被弾しながら特殊で返す役割が成立します。後述するしろいハーブとの組み合わせでりゅうせいぐんのC2段階低下をリセットする型は、この高C種族値を無駄なく使い切る構成です。

### 3. 技構成の幅広さ

ラスターカノン・りゅうせいぐん・でんき技で打点を確保しながら、ステルスロック（37.4%）・ドラゴンテール（14.6%）・ほえる（12.6%）による展開補助、ミラーコート（15.5%）での特殊カウンターまで、1枠の選択で型が大きく変わります。アタッカーか補助かカウンターかを対戦前に読みにくく、相手の選出・立ち回りを迷わせる点が強みです。

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

B130・C125の攻防種族値が高く、S85は環境中速帯。最多EV構成「H2 C32 S32 ひかえめ」では**H166・B150・C177・S121**となります。S121はメガラグラージ（最速S116）を上回り先手を取れますが、ガブリアス（最速S151）・ミミッキュ（ようきS145）・メガメタグロス（S160）・メガムクホーク（最速S160）・メガライチュウY（最速S160）・スカーフマスカーニャには後手となります。

### タイプ・弱点（はがね/ドラゴン）

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（×0.25）</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき（×0.5）</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず（×0.5）</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう（×0.5）</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ（×0.5）</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー（×0.5）</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル（×0.5）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.5）</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね（×0.5）</span>
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

弱点はかくとう・じめんの2タイプのみ。どくを無効化し、くさを×0.25、むしを×0.5で受けます。環境上位のマスカーニャ（くさ/あく）のくさ技は×0.25と非常に強い耐性です。一方でかくとう・じめんは環境上位（ガブリアスのじしん、メガムクホークのかくとう技等）が採用しやすいタイプで、これらが実質的な被弾リスクになります。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ラスターカノン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">74.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうせいぐん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">72.6%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>10まんボルト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">48.5%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>エレクトロビーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#1d4ed8">40.1%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">37.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はどうだん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">28.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ミラーコート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドラゴンテール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほえる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">12.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.4%</td>
</tr>
</tbody>
</table>
</div>

ラスターカノン（74.6%）・りゅうせいぐん（72.6%）・でんき技（10まんボルト48.5%＋エレクトロビーム40.1%）の3方向アタッカーが最多構成ですが、技範囲を広げるはどうだん（28.9%）、設置役を担うステルスロック（37.4%）、起点回避のドラゴンテール（14.6%）・ほえる（12.6%）、特殊反射のミラーコート（15.5%）と補助・カウンター型まで採用が広がっており、技構成の多様度はM-3環境上位でも高水準です。

でんき技の10まんボルト（安定打点）とエレクトロビーム（高威力・1ターン溜め）が合計88.6%と高採用で、ムクホーク（でんき×2）・リザードン（でんき×2）への打点として機能します。エレクトロビームは溜めターンが生じるため、受け出しに来る相手への読み打ちや雨展開下（即発動）での運用が前提です。

---

## 主要型の解説

性格はひかえめ49.6%・ずぶとい16.4%・おくびょう13.3%・おだやか10.9%と分散。持ち物はオボンのみ29.8%・たべのこし29.4%・しろいハーブ19.2%・こだわりスカーフ11.0%が主流です。

### 型1: ひかえめ火力型（最多採用）

**性格: ひかえめ 49.6%　持ち物: オボンのみ 29.8% / たべのこし 29.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ひかえめ耐久火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（75.7%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32（採用率25.3%）<br>
<strong>持ち物:</strong> オボンのみ（29.8%）／たべのこし（29.4%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（74.6%）<br>
・りゅうせいぐん（72.6%）<br>
・10まんボルト（48.5%）またはエレクトロビーム（40.1%）<br>
・ステルスロック（37.4%）またははどうだん（28.9%）
</div>
</div>
</div>

**強み:**

ひかえめC32でC実数値177。じきゅうりょくで被弾のたびに防御が1段階上がる（物理・特殊問わず）ため、アタッカーを相手にしながら特殊でカウンターを取り続けられます。オボンのみはHPが半分以下になると自動で回復するため、被弾後もB上昇と合わせて場持ちを延ばします。たべのこしはターンごとに1/16回復し、積み重ねでロングゲームに強い構成です。

**弱み:**

S121は環境上位アタッカーの多く（ガブリアス最速S151・ミミッキュS145・メガムクホーク最速S160・メガライチュウY最速S160・スカーフマスカーニャ等）に後手となるため、特殊弱点のとくぼう65が低い相手を上から取る動きは難しく、毎ターン被弾しながら反撃する立ち回りが基本です。特殊方向の弱点（とくぼう65）は種族値で低く、とくぼうに振っていない型はメガライチュウYの特殊技で大きなダメージを受けます。

---

### 型2: しろいハーブりゅうせいぐん型

**性格: ひかえめ 49.6%　持ち物: しろいハーブ 19.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">しろいハーブ連射型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（75.7%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32（25.3%）<br>
<strong>持ち物:</strong> しろいハーブ（19.2%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（74.6%）<br>
・りゅうせいぐん（72.6%）<br>
・10まんボルト（48.5%）またはエレクトロビーム（40.1%）<br>
・ステルスロック（37.4%）またははどうだん（28.9%）
</div>
</div>
</div>

**強み:**

りゅうせいぐん（ドラゴン・130）は使用後にCが2段階低下するデメリット技ですが、しろいハーブ（能力低下を1度だけ回復）により初回使用後のC低下をリセットできます。実質的に1試合で**威力130のりゅうせいぐんをC無消費で2連射**できる形になり、2発の威力合計は10まんボルト2発（90×2）やラスターカノン2発（80×2）を大きく上回ります。これは型1との最大の差別点で、単発の対面処理力が高い2体を連続して倒す展開で真価を発揮します。

**弱み:**

しろいハーブ消費後は2発目以降のりゅうせいぐんでCが落ちるため、C低下を補うラスターカノン等に切り替える必要があります。オボンのみ・たべのこしのような回復手段がないため、被弾が積み重なる長期戦には向きません。

---

### 型3: ずぶとい耐久型

**性格: ずぶとい 16.4%　持ち物: たべのこし 29.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ずぶとい耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> じきゅうりょく（75.7%）／がんじょう（24.1%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 C32（H181 B150 C161 想定）<br>
<strong>持ち物:</strong> たべのこし（29.4%）
</div>
<div>
<strong>技構成:</strong><br>
・ラスターカノン（74.6%）<br>
・10まんボルト（48.5%）またはエレクトロビーム（40.1%）<br>
・ステルスロック（37.4%）<br>
・ほえる（12.6%）またはドラゴンテール（14.6%）
</div>
</div>
</div>

**強み:**

ずぶとい＋H振り＋じきゅうりょくで物理耐久を最大化し、じきゅうりょくのB上昇と合わせて物理攻撃を受けながらステルスロックを設置する展開を作ります。がんじょう（HPが満タンの時に一撃でひんしになる技のダメージを1残して耐える）を選択した場合は、タスキと同様の役割で確実に1回行動できます。たべのこしで継続回復しながらほえる・ドラゴンテールで相手を流す長期運用が可能です。

**弱み:**

C種族値125を活かしきれず、C実数値はひかえめ型より16低くなります（ひかえめC177・ずぶといC161）。火力が落ちる分、ひかえめ型なら1発で倒せる相手を2発かけることになる場面が増えます。型1・2と比べて打点を担う役割よりも展開役・場持ち役に寄っており、後続への依存度が高まります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

以下の相性はひかえめH2 C32 S32型（H166・C177・S121）を基準とします。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#888;font-weight:bold">△</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技は×0.25で受けられるが、スカーフマスカーニャ（S261）にS121のブリジュラスは後手。トリプルアクセル（こおり等倍×3）やはたきおとす（あく等倍）を上から連打される。B振り型なら1発は耐えるが、スカーフで縛られた対面では不利側の要素が大きい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン（はがね）がゴースト/フェアリーに×2。ミミッキュのようきS145に後手だがばけのかわで1回行動を稼がれる。ただしラスターカノン1発でばけのかわ解除＋大ダメージを与えられる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスのじしん（じめん×2）が弱点。最速ガブ（S151）・スカーフ最速ガブ（S226）ともにブリジュラスS121を上回り先手を取られる。ブリジュラスのでんき技はガブリアス（じめんタイプ）に無効。最大打点はりゅうせいぐん（ドラゴン×2）だが先手を取れないため交代を要する場面が多い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技がじめんタイプのため無効（ラグラージはみず/じめん複合でじめんがでんき免疫を持つ）。最大打点はりゅうせいぐん（等倍）かはどうだん（等倍）止まり。メガラグラージのじしん（じめん×2）がブリジュラスの弱点で、S106よりブリジュラスS121の方が速く先手は取れるが有効打に乏しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ムクホーク（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガムクホーク（採用率95.3%）はかくとう/ひこうに進化。かくとう技がブリジュラスの×2弱点。最速S160でブリジュラスS121を上回り先手を取られる</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のかくとう・じめんを主力に持つ環境上位を中心に選定しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2）が弱点で、最速S151に先手を取られる。でんき技が通らないため有効打に限りがある</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技を持つパートナー（ミミッキュ等）で処理する。ブリジュラスはりゅうせいぐんで削りを入れつつ引く択を取る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき無効（じめん複合のため）。なみのり・じしんが刺さり有効打がりゅうせいぐん等倍止まり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技を持つパートナーで対処。同居率2位のラグラージへの解答は外部に依存する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガムクホーク（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう（×2弱点）を主力に持ち、メガ後S160で先手を取られる。ブリジュラスのでんき技はひこう×2だがかくとう技を先に受ける場面が多い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー技・フェアリー技を持つポケモンで対処。ブリジュラス自身ではラスターカノンがかくとう/ひこうに等倍で処理効率が低い</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率上位パートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ブリジュラスが苦手なメガラグラージへじしん（等倍）、ミミッキュへじゃれつく方向での補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">ラグラージ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ブリジュラスが処理できないほのお・じめん対面をみず技で補完。雨展開でエレクトロビームの即発動補助にもなる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0279-00.webp" alt="ペリッパー">
    <div class="name">ペリッパー</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あめふらしで雨を展開。エレクトロビームを溜めなしで即発動させる組み合わせ。ラグラージとの3体セットで使われる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ブリジュラスが苦手なガブリアスへじゃれつく（フェアリー×2）で打点を出せる補完関係</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ようきスカーフS261で上から削り、ブリジュラスを安全に着地させる対面操作役</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率10位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでフェアリー耐性を持ち、ブリジュラスが苦手な相手を物理面でカバー</div>
  </div>
</div>

**同居率3位にペリッパーが入る点がM-3の特徴**です。ペリッパーのあめふらしはエレクトロビームを溜めなしで即発動させ（雨下では1ターンで使える仕様）、ラグラージも加えた3体軸が同居率上位に揃っています。この「ペリッパー＋ラグラージ＋ブリジュラス」の組み合わせは、雨展開でブリジュラスのエレクトロビームを即発動させながらラグラージの水技も強化する構成で、相手のでんき対策（メガラグラージが当然選出される）を逆手に取っています。

---

## データ分析①：M-2→M-3のでんき技シフト

M-2とM-3の技採用率を比較すると、でんき技の優先度に変化が見られます。

| 技 | M-2 | M-3 | 変化 |
|---|---|---|---|
| 10まんボルト | 66.9% | 48.5% | −18.4pt |
| エレクトロビーム | 10.6% | 40.1% | +29.5pt |
| ラスターカノン | 55.7% | 74.6% | +18.9pt |
| りゅうせいぐん | 64.8% | 72.6% | +7.8pt |
| ステルスロック | 49.8% | 37.4% | −12.4pt |
| ほえる | 23.4% | 12.6% | −10.8pt |

M-2では10まんボルトが最多でんき技（66.9%）でエレクトロビームは10.6%に留まっていました。M-3では10まんボルトが48.5%に減り、エレクトロビームが40.1%まで急増しています。この変化はペリッパー（同居率3位）による雨展開の普及と対応しています。雨下ではエレクトロビームの溜めターンがなくなり、威力130（10まんボルト90の1.44倍）の打点を即発動できます。

一方でステルスロックは49.8%→37.4%に減少し、ほえる（相手を強制交代させる変化技）も23.4%→12.6%に減っています。M-2では「展開・削り」の補助役割が強かったブリジュラスが、M-3ではラスターカノン採用率の上昇（55.7%→74.6%）も合わせて**アタッカー寄りの構成へシフトしている**傾向がデータから読み取れます。

### エレクトロビームが有効な対象の環境採用率

エレクトロビームが抜群（×2）を取れる相手は**ひこう・みずタイプ**ですが、ラグラージ（みず/じめん）にはじめんタイプのでんき免疫があるため無効です。環境上位でエレクトロビームが有効な相手を整理すると：

- **ムクホーク（7位）**: かくとう/ひこうにでんき×2（メガ後もかくとう/ひこう）
- **リザードン（8位）**: ほのお/ひこうにでんき×2
- **ペリッパー（18位）**: みず/ひこうにでんき×4（じめんタイプなし）

ステルスロック・ほえる採用率の低下と合わせて見ると、上記3体が軸の相手チームに対してエレクトロビームで強引に打点を作る運用が M-3で増えたことが数値から確認できます。

---

**総評:**

ブリジュラスはC177（ひかえめC32）のラスターカノン・りゅうせいぐん・でんき技の3方向で特殊打点を確保しつつ、じきゅうりょくで物理被弾をB上昇に変えて場持ちを延ばす特殊アタッカーです。M-3ではエレクトロビームの採用が急増（10.6%→40.1%）し、ペリッパー・ラグラージとの雨軸3体セットが同居率上位に現れているのが特徴的な変化です。一方でじめん×2弱点（ガブリアス1位・メガラグラージ12位に共通）とでんき技がラグラージに無効な点は、いずれの型でもカバーできない構造上の制約であり、パートナーのくさ技・フェアリー技でのフォローが選出を組む上での前提となります。

---

## 関連記事

- [使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [使用率2位 ミミッキュのM-3考察](/blog/mimikyu-analysis-m3/)
- [使用率2位 ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
