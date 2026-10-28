---
title: '【ポケモンチャンピオンズ】メタグロス 考察 M-7 シーズン 使用率14位浮上の型解説'
description: 'M-7シーズン使用率14位（M-6:19位）に浮上したメタグロス考察。物理アタッカー型とてっぺき・ボディプレス型を比較し、じしん採用率68.2%（M-6比+13.0pt）などの技構成変化、苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-26'
heroImage: '../../assets/hero-metagross-m7.png'
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
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" />
  <div>
    <h2 style="margin:0 0 8px">メガメタグロス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">14位</strong>（M-6: 19位）　持ち物: <strong>メタグロスナイト 97.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズン、メタグロスは使用率がM-6シーズン最終の19位から14位まで浮上しました。メタグロスナイト（採用率97.0%）によるメガ進化が前提で、バレットパンチ・サイコファングを主軸にじしん・れいとうパンチ・かみなりパンチで打点を補う物理アタッカー型が主流です。

---

## メガメタグロスの基本スペック

<!-- gate:rows start id=base_stats facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
### 種族値（通常→メガメタグロス）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:32px;text-align:right">メガ後</span>
    <span style="width:40px;text-align:right">差分</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:32px;text-align:right">80</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:67.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">135</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">145</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:47.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">105</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:45%;background:linear-gradient(90deg,#34d399,#059669);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#34d399,#059669);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">110</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:35%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:20%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">110</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガ進化でSが+40上昇し、物理アタッカー型の実数値S162（EV32）の土台になります。ぼうぎょ150はてっぺき・ボディプレス型の土台になる数値です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点はあく・じめん・ほのお・ゴーストの4タイプで、耐性は半減8タイプとエスパーの4分の1耐性を合わせた9タイプと広く、どく無効も持ちます。

### 特性

**クリアボディ（99.4%）**が通常時の特性です。メガ進化前の、いかく等で能力ランクを下げられる場面でだけ効果を発揮し、相手の技や特性で能力ランクが下がりません。メガ進化すると特性は**かたいツメ**に変わり、接触技の威力が1.3倍になります（じしんのような非接触技は対象外）。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の場のひかりのかべ状態、リフレクター状態、オーロラベール状態を解除して攻撃する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">68.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">地中状態の相手には威力が2倍になる。グラスフィールド状態の時、威力が1/2になる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">34.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をまひ状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.2%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手をひるませる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">ボディプレス</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.5%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">この技は攻撃ではなく、防御の数値でダメージが決まる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">てっぺき</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の防御を2段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手が重いほど威力が上がる。威力20-120。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">コメットパンチ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で自分の攻撃を1段階上げる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

バレットパンチ（90.6%）とサイコファング（73.5%）が主軸で、れいとうパンチ（73.3%）・じしん（68.2%）がこれに次ぐ採用率を確保しています。かみなりパンチ（34.3%）は物理アタッカー型の選択技、アイアンヘッド（11.2%）は両型に共通する選択技です。ボディプレス（8.5%）・てっぺき（7.8%）はてっぺき・ボディプレス型の専用技、くさむすび（7.6%）はてっぺき・ボディプレス型の選択技です。

---

## 主な型

技・性格・EVの組み合わせから、採用割合が高い順に2つの型を紹介します。

### 型1：物理アタッカー型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.4%、メガ進化後はかたいツメ）<br>
<strong>性格:</strong> いじっぱり（64.0%、ようきも28.6%）<br>
<strong>EV:</strong> H2-A32-S32（採用率22.3%、全体最多）<br>
<strong>持ち物:</strong> メタグロスナイト（97.0%）
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・サイコファング<br>
・れいとうパンチ<br>
・じしん<br>
選択技：かみなりパンチ・アイアンヘッド
</div>
</div>
</div>

H157（EV2）・A216（EV32・いじっぱり補正込み）・S162（EV32）が主な実数値です。採用率90.6%のバレットパンチを中心に、サイコファング・れいとうパンチ・じしん・かみなりパンチ・アイアンヘッドの中から残り3枠を選ぶ構成です。

<!-- gate:rows start id=card:1 facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
**他の型との違い:**

- 他の型に無い技：れいとうパンチ・じしん
- もう一方の型より高い実数値：こうげき216・すばやさ162
- もう一方の型より低い実数値：HP157・ぼうぎょ170
<!-- gate:rows end id=card:1 -->

---

### 型2：てっぺき・ボディプレス型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">てっぺき・ボディプレス型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（99.4%、メガ進化後はかたいツメ）<br>
<strong>性格:</strong> わんぱく（5.4%）<br>
<strong>EV:</strong> H18-B20-S28（採用率1.3%）<br>
<strong>持ち物:</strong> メタグロスナイト（97.0%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・ボディプレス<br>
・てっぺき<br>
・バレットパンチ<br>
選択技：くさむすび・アイアンヘッド
</div>
</div>
</div>

H173・A165・B209・S158（EV: H18-B20-S28）が主な実数値です。

<!-- gate:rows start id=card:2 facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
**他の型との違い:**

- 他の型に無い技：ボディプレス・てっぺき
- もう一方の型より高い実数値：HP173・ぼうぎょ209
- もう一方の型より低い実数値：こうげき165・すばやさ158
<!-- gate:rows end id=card:2 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">物理アタッカー型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">てっぺき・ボディプレス型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガガブリアスZ（おくびょう・ガブリアスナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（ひかえめ・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（しんちょう・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX（ようき・リザードナイトX）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガカイリュー（ひかえめ・カイリュナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（いじっぱり・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（むじゃき・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr class="note"><td colspan="3" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体6件は除く</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの技・性格採用率の変化


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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+13.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">34.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.4pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">88.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+1.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">72.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">73.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+1.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">てっぺき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-2.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ボディプレス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-2.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サイコファング</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">73.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-6.2pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">57.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">64.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+6.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-2.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-2.9pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
- じしん：55.2%→68.2%（+13.0pt）。物理アタッカー型だけが持つため、この変化はその型の増減を示します。
- かみなりパンチ：24.9%→34.3%（+9.4pt）。物理アタッカー型の選択技のため、型の増減とは言えません。
- アイアンヘッド：17.4%→11.2%（-6.2pt）。物理アタッカー型・てっぺき・ボディプレス型の選択技のため、型の増減とは言えません。
- いじっぱり：57.9%→64.0%（+6.1pt）。物理アタッカー型だけが選んでいるため、この変化はその型の増減を示します。
- サイコファング：77.0%→73.5%（-3.5pt）。記事のすべての型に共通のため、型の増減とは言えません。
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
<!-- gate:rows start id=weak facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型の選択技かみなりパンチは確定1発。メガリザードンYのかえんほうしゃ（採用率43.0%）は確定1発で、S162対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のサイコファングは乱数2発（>99%）。ヒートロトムのオーバーヒート（採用率96.3%）は確定1発で、S162対S106で先手を取れますが確定数で下回り、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のバレットパンチは確定2発（ばけのかわ込み）。ミミッキュのシャドークロー（採用率48.8%）は確定2発で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のじしんは確定4発（相手のオボンのみ込み）。ブリジュラスの10まんボルト（採用率63.9%）は乱数4発（>99%）で、S162対S105で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型の選択技かみなりパンチは乱数1発（69%）。イダイトウ(オス)のおはかまいり（採用率99.7%）は乱数2発（91%）で、S162対S214で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型の選択技アイアンヘッドは確定2発（相手のきあいのタスキ込み）。セグレイブのじしん（採用率89.0%）は確定2発で、S162対S139で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型の選択技アイアンヘッドは確定2発（相手のきあいのタスキ込み）。イエッサン(オス)のマジカルフレイム（採用率95.0%）は確定3発で、S162対S161で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のサイコファングは確定2発（相手のきあいのタスキ込み）。キラフロルのだいちのちから（採用率63.1%）は確定2発で、S162対S151で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のれいとうパンチは確定2発。ゴリランダーの10まんばりき（採用率55.1%）は乱数2発（>99%）で、S162対S107で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のサイコファングは確定2発。メガライチュウYのきあいだま（採用率96.3%）は乱数3発（80%）で、S162対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のサイコファングは確定1発。オオニューラのインファイト（採用率98.4%）は確定2発で、S162対S172で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のサイコファングは乱数3発（95%）。ウォッシュロトムの10まんボルト（採用率44.7%）は乱数3発（95%）で、S162対S106で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のバレットパンチは確定1発。アローラキュウコンのふぶき（採用率66.9%）は確定5発で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカー型のれいとうパンチは確定2発。サザンドラのあくのはどう（採用率98.5%）は確定2発で、最後は優先度+1のバレットパンチで先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でメタグロスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率5位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サザンドラ<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カイリュー<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガカイリューで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロスの弱点：あく技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロスの弱点：じめん技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロスの弱点：ほのお技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロスの弱点：ゴースト技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝メガメタグロスの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=dd98ce0ae1c471241f1970865acfe226214723a8 -->
**強み**

- 得意な相手は12体です。使用率上位では、ミミッキュ（3位）にバレットパンチ、ブリジュラス（8位）にじしん、イダイトウ(オス)（10位）にかみなりパンチで勝てます。
- タイプ相性では、ノーマル・くさ・こおり・ひこう・エスパー・いわ・ドラゴン・はがね・フェアリーを半減以下、どくを無効で受けられます。

**弱み**

- 苦手な相手は2体です。使用率上位では、メガリザードンY（6位）のかえんほうしゃ、ヒートロトム（26位）のオーバーヒートで先に倒されます。
- 弱点はほのお・じめん・ゴースト・あくです。

**型の選び分け**

- 「物理アタッカー型」：他の型に無い技はれいとうパンチ・じしん。
- 「てっぺき・ボディプレス型」：他の型に無い技はボディプレス・てっぺき。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は14位です（M-6: 19位）。
- 採用率の変化が大きいのはじしん（+13.0pt）・かみなりパンチ（+9.4pt）・アイアンヘッド（-6.2pt）です。
<!-- gate:rows end id=summary -->

## 関連記事

- [ガブリアス M-7シーズン考察](/blog/garchomp-analysis-m7/)
- [ブリジュラス M-7シーズン考察](/blog/archaludon-analysis-m7/)
- [ミミッキュ M-7シーズン考察](/blog/mimikyu-analysis-m7/)
