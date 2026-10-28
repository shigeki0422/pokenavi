---
title: '【ポケモンチャンピオンズ】ガラルヤドキング 考察 M-7 シーズン 使用率75位の3型解説'
description: 'M-7シーズン使用率75位（M-6: 81位）のガラルヤドキングを考察。さいせいりょく採用率99.4%を軸に、さむいギャグ型・めいそう型・アシッドボム型の3型を比較し、シュカのみ8.4%→31.0%への増加やミミッキュなど苦手なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-28'
heroImage: '../../assets/hero-slowking-galar-m7.png'
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
  <img src="/images/pokemon/pokemon-0199-01.webp" alt="ガラルヤドキング" />
  <div>
    <h2 style="margin:0 0 8px">ガラルヤドキング</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">75位</strong>（M-6: 81位）　特性: <strong>さいせいりょく 99.4%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのガラルヤドキングは使用率75位です（M-6: 81位）。HP95・とくぼう110の特殊耐久に、特性さいせいりょく（採用率99.4%）の回復を組み合わせた受けポケモンです。技はさむいギャグ（採用率62.3%）・ヘドロばくだん（57.6%）・かえんほうしゃ（48.2%）が上位で、技構成と持ち物の違いから3つの型に分かれます。

---

## ガラルヤドキングの基本スペック

<!-- gate:rows start id=base_stats facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
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
      <div style="width:55%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:15%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">490</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

### 特性

<strong>さいせいりょく（99.4%）</strong>がほぼ全個体の特性です。手持ちに戻ると最大HPの1/3回復します。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>さむいギャグ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">62.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">5ターンの間ゆき状態にする。手持ちの他のポケモンと交代する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロばくだん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">30%の確率で相手をどく状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">48.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をやけど状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">36.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">36.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2回復する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アシッドボム</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の特防を2段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">どくどく</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をもうどく状態にする。どくタイプが使うと相手に必ず命中する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.0%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻と特防が1段階ずつ上がる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.5%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をどく状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

### 型1：さむいギャグ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0199-01.webp" alt="ガラルヤドキング" style="width:48px;height:48px">
  <strong style="font-size:1.05em">さむいギャグ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さいせいりょく<br>
<strong>性格:</strong> おだやか<br>
<strong>EV:</strong> H32-C14-D20<br>
<strong>持ち物:</strong> シュカのみ
</div>
<div>
<strong>技構成:</strong><br>
・ヘドロばくだん<br>
・かえんほうしゃ<br>
・れいとうビーム<br>
・さむいギャグ<br>
選択技：なまける・アシッドボム・どくどく・ヘドロウェーブ
</div>
</div>
</div>

さむいギャグで交代しながら、さいせいりょくの回復を重ねて戦う型です。

<!-- gate:rows start id=card:1 facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
**他の型との違い:**

- 他の型に無い技：さむいギャグ
- れいとうビーム：この型は必ず持ち、めいそう型・アシッドボム型では選択技
- 持ち物：シュカのみ（じめんタイプの効果バツグンの技で受けるダメージを半減する。1度使うと無くなる）
<!-- gate:rows end id=card:1 -->

---

### 型2：めいそう型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0199-01.webp" alt="ガラルヤドキング" style="width:48px;height:48px">
  <strong style="font-size:1.05em">めいそう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さいせいりょく<br>
<strong>性格:</strong> おだやか<br>
<strong>EV:</strong> H32-C14-D20<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ヘドロばくだん<br>
・かえんほうしゃ<br>
・なまける<br>
・めいそう<br>
選択技：ヘドロウェーブ・どくどく・れいとうビーム
</div>
</div>
</div>

めいそうで特攻と特防を上げ、なまけるで回復しながら戦う型です。

<!-- gate:rows start id=card:2 facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
**他の型との違い:**

- 他の型に無い技：めいそう
- なまける：この型は必ず持ち、さむいギャグ型・アシッドボム型では選択技
- 持ち物：オボンのみ（HPが最大HPの1/2以下になった時、最大HPの1/4回復する。1度使うと無くなる）
<!-- gate:rows end id=card:2 -->

---

### 型3：アシッドボム型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0199-01.webp" alt="ガラルヤドキング" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アシッドボム型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さいせいりょく<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H32-C20-D14<br>
<strong>持ち物:</strong> たつじんのおび
</div>
<div>
<strong>技構成:</strong><br>
・ヘドロばくだん<br>
・アシッドボム<br>
・サイコキネシス<br>
・かえんほうしゃ<br>
選択技：れいとうビーム・なまける・ヘドロウェーブ
</div>
</div>
</div>

アシッドボムで相手のとくぼうを下げてから、ヘドロばくだんとサイコキネシスで攻める型です。

<!-- gate:rows start id=card:3 facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
**他の型との違い:**

- 他の型に無い技：サイコキネシス
- アシッドボム：この型は必ず持ち、さむいギャグ型では選択技
- 持ち物：たつじんのおび（効果バツグンの技の威力が1.2倍になる）
- 3つの型で最も高い実数値：とくこう165
- 3つの型で最も低い実数値：とくぼう144
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">さむいギャグ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">めいそう型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシッドボム型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガガブリアスZ（おくびょう・ガブリアスナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（ひかえめ・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY（ひかえめ・リザードナイトY）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ ほか2個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガキラフロル（おくびょう・キラフロルナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー（いじっぱり・いのちのたま）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定</td></tr>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">さむいギャグ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">73.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">62.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-11.6pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ヘドロばくだん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">57.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">48.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-11.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+19.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">なまける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">43.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-6.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">どくどく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-7.2pt</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シュカのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+22.6pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">49.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-21.7pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">オボンのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+0.8pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おだやか（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">53.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+15.4pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">なまいき（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-10.7pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
- シュカのみ：8.4%→31.0%（+22.6pt）。さむいギャグ型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- たべのこし：49.7%→28.0%（-21.7pt）。さむいギャグ型・めいそう型の一部の個体が持つもので、型の増減とは言えません。
- れいとうビーム：17.6%→36.9%（+19.3pt）。さむいギャグ型が持ち、めいそう型・アシッドボム型でも選択技のため、型の増減とは言えません。
- おだやか：53.1%→68.5%（+15.4pt）。さむいギャグ型・めいそう型が選んでいるほか、アシッドボム型の一部の個体も選んでいるため、型の増減とは言い切れません。
- かえんほうしゃ：60.1%→48.2%（-11.9pt）。記事のすべての型に共通のため、型の増減とは言えません。
- さむいギャグ：73.9%→62.3%（-11.6pt）。記事の型ではさむいギャグ型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- なまいき：23.0%→12.3%（-10.7pt）。この記事の型の性格には含まれません。
- ヘドロばくだん：47.7%→57.6%（+9.9pt）。記事のすべての型に共通のため、型の増減とは言えません。
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
<!-- gate:rows start id=weak facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう型のヘドロばくだんは確定3発。ミミッキュのかげうち（採用率96.5%）は確定3発で、優先度+1のかげうちで先に動かれ、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のれいとうビームは乱数2発（93%）。カバルドンのじしん（採用率97.3%）は確定2発で、S50対S67で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは乱数2発（88%）。メガリザードンXのドラゴンクロー（採用率17.9%・少数派）は確定2発で、S50対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシッドボム型のサイコキネシスは確定3発。イダイトウ(オス)のおはかまいり（採用率99.7%）は確定2発で、S50対S214（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは確定2発。セグレイブのきょけんとつげき（採用率86.4%）は確定2発で、S50対S139で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のかえんほうしゃは乱数2発（89%）。メガメタグロスのサイコファング（採用率73.5%）は確定2発で、S50対S162で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは確定2発。マスカーニャのはたきおとす（採用率66.0%）は確定2発で、S50対S288（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは乱数3発（98%）。ギャラドスのじしん（採用率66.6%）は確定3発で、S50対S101で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは確定4発（相手のたべのこし込み）。ブラッキーのイカサマ（採用率96.0%）は確定3発で、S50対S85で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のかえんほうしゃは確定2発。メガルカリオZのあくのはどう（採用率73.5%）は確定3発で、S50対S223で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のかえんほうしゃは確定2発。アーマーガアのブレイブバード（採用率27.5%）は確定3発で、S50対S78で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のれいとうビームは確定2発。メガカイリューのりゅうせいぐん（採用率35.5%）は確定3発で、S50対S152で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型のれいとうビームは確定1発。メガボーマンダのじしん（採用率72.0%）は確定2発で、S50対S172で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは乱数3発（61%）。ヒートロトムの10まんボルト（採用率30.6%）は確定5発で、S50対S106で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さむいギャグ型の選択技ヘドロウェーブは確定2発。アローラキュウコンのふぶき（採用率66.9%）は確定4発で、S50対S177で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でガラルヤドキングと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
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
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" loading="lazy">
    <div class="name">ハッサム</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス" loading="lazy">
    <div class="name">バンギラス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" loading="lazy">
    <div class="name">ドヒドイデ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率2位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ハッサム<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">バンギラス<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ドヒドイデ<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガラルヤドキングの弱点：あく技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガラルヤドキングの弱点：じめん技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガラルヤドキングの弱点：ゴースト技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">セグレイブ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブラッキー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ガラルヤドキングの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ミミッキュ＝じゃれつく・かげうち・シャドークロー・ウッドハンマー；カバルドン＝じしん；メガリザードンX＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；イダイトウ(オス)＝おはかまいり・アクアジェット・ウェーブタックル・クイックターン；セグレイブ＝こおりのつぶて・じしん・きょけんとつげき・つららおとし；メタグロス＝バレットパンチ・サイコファング・れいとうパンチ・じしん・かみなりパンチ；マスカーニャ＝トリックフラワー・トリプルアクセル・はたきおとす・とんぼがえり；ギャラドス＝じしん・パワーウィップ・たきのぼり・こおりのキバ・ゆきなだれ；ブラッキー＝イカサマ</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=d448573df7c37d68d7bf47282e78da66fdbb523d -->
**強み**

- 得意な相手は6体です。使用率上位では、ルカリオ（7位）・アーマーガア（11位）にかえんほうしゃ、カイリュー（12位）にれいとうビームで勝てます。
- タイプ相性では、くさ・かくとう・どく・フェアリーを半減以下で受けられます。

**弱み**

- 苦手な相手は9体です。使用率上位では、ミミッキュ（3位）のかげうち、カバルドン（4位）のじしん、メガリザードンX（6位）のドラゴンクローで先に倒されます。
- 弱点はじめん・ゴースト・あくです。

**型の選び分け**

- 「さむいギャグ型」：他の型に無い技はさむいギャグ。
- 「めいそう型」：他の型に無い技はめいそう。
- 「アシッドボム型」：他の型に無い技はサイコキネシス。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は75位です（M-6: 81位）。
- 採用率の変化が大きいのはシュカのみ（+22.6pt）・たべのこし（-21.7pt）・れいとうビーム（+19.3pt）です。
<!-- gate:rows end id=summary -->

---

*関連記事：[ミミッキュ考察 M-7](/blog/mimikyu-analysis-m7/)　[ガブリアス考察 M-7](/blog/garchomp-analysis-m7/)*
