---
title: '【ポケモンチャンピオンズ】ハッサム 考察 M-7 シーズン 使用率37位の5型解説'
description: 'M-7シーズン使用率37位（M-6: 42位）のハッサムを考察。テクニシャン採用率98.9%を軸に、のろい型・つるぎのまい型・はねやすめ型・きりばらい型・メガ・つるぎのまい型の5型を比較し、メガリザードンXなど苦手、ミミッキュなど得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-27'
heroImage: '../../assets/hero-scizor-m7.png'
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
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" />
  <div>
    <h2 style="margin:0 0 8px">ハッサム</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">37位</strong>（M-6: 42位）　特性: <strong>テクニシャン 98.9%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのハッサムは使用率37位です（M-6: 42位）。特性テクニシャンの採用率は98.9%で、バレットパンチ（採用率99.5%）を主力に、のろい・つるぎのまい・きりばらい等の技構成の違いで5つの型に分かれます。

---

## ハッサムの基本スペック

<!-- gate:rows start id=base_stats facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
### 種族値（通常→メガハッサム）

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
      <div style="width:35%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:65%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:20%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">140</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:27.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">55</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">65</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:40%;background:linear-gradient(90deg,#34d399,#059669);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#34d399,#059669);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">100</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:32.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">65</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">75</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">500</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガ進化後も特性はテクニシャンのまま変わりません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

ほのお×4が最大の弱点で、M-7上位ではリザードンのかえんほうしゃ（採用率43.0%）やカイリューのかえんほうしゃ（採用率65.2%）が主な脅威です。

### 特性

<strong>テクニシャン（98.9%）</strong>が主流の特性です。威力60以下の技の威力を1.5倍にする効果で、一致技のバレットパンチと、選択技のダブルウイングを強化します。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">77.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">攻撃した後、手持ちの他のポケモンと交代する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2回復する。ひこうタイプが使うとそのターン中ひこうタイプでなくなる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">34.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃を2段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の防御と特防が1段階下がる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のろい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2減らし、相手をのろい状態にする。ゴーストタイプ以外の場合、自分の素早さを1段階下げて、攻撃・防御を1段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">23.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手が道具を持っていると威力が1.5倍になる。相手の道具を失わせる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">きりばらい</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の回避率を1段階下げる。リフレクター、まきびし、しんぴのまもり、フィールド等を解除する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">こわいかお</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.0%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の素早さを2段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">ダブルウイング</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.0%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">2回連続で攻撃する。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に5つの型を紹介します。

### 型1：のろい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">のろい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> テクニシャン<br>
<strong>性格:</strong> のんき<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・とんぼがえり<br>
・はねやすめ<br>
・のろい<br>
選択技：こわいかお
</div>
</div>
</div>

採用割合が最も高い型です。のろいによって、5つの型の中で唯一、攻撃と防御の両方を上げられます。

<!-- gate:rows start id=card:1 facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**他の型との違い:**

- 他の型に無い技：のろい
- 5つの型で最も低い実数値：すばやさ76（同じ値の型あり）
<!-- gate:rows end id=card:1 -->

---

### 型2：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> テクニシャン<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・とんぼがえり<br>
・インファイト<br>
・つるぎのまい<br>
選択技：はねやすめ・はたきおとす
</div>
</div>
</div>

メガ進化せずにつるぎのまいを積む型で、メガ・つるぎのまい型とはメガ進化の有無が異なります。

<!-- gate:rows start id=card:2 facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**他の型との違い:**

- はねやすめ型との技の違い：この型はつるぎのまい、はねやすめ型ははねやすめ
- 持ち物：オボンのみ（HPが最大HPの1/2以下になった時、最大HPの1/4回復する。1度使うと無くなる）
- 5つの型で最も低い実数値：ぼうぎょ152
<!-- gate:rows end id=card:2 -->

---

### 型3：はねやすめ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">はねやすめ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> テクニシャン<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・とんぼがえり<br>
・インファイト<br>
・はねやすめ<br>
選択技：はたきおとす・ダブルウイング
</div>
</div>
</div>

のろい・きりばらいの技枠をインファイトにした耐久型です。わんぱくのため、すばやさがのろい型・きりばらい型より下がりません。

<!-- gate:rows start id=card:3 facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**他の型との違い:**

- のろい型との技の違い：この型はインファイト、のろい型はのろい
<!-- gate:rows end id=card:3 -->

---

### 型4：きりばらい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きりばらい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> テクニシャン<br>
<strong>性格:</strong> のんき<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・とんぼがえり<br>
・はねやすめ<br>
・きりばらい
</div>
</div>
</div>

きりばらいでステルスロックなどの設置技を払う型です。

<!-- gate:rows start id=card:4 facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**他の型との違い:**

- 他の型に無い技：きりばらい
- 5つの型で最も低い実数値：すばやさ76（同じ値の型あり）
<!-- gate:rows end id=card:4 -->

---

### 型5：メガ・つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガ・つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> テクニシャン（メガ後 テクニシャン）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H32-A32-B2<br>
<strong>持ち物:</strong> ハッサムナイト
</div>
<div>
<strong>技構成:</strong><br>
・バレットパンチ<br>
・インファイト<br>
・はたきおとす<br>
・つるぎのまい<br>
選択技：とんぼがえり・はねやすめ
</div>
</div>
</div>

ハッサムナイトでメガ進化し、こうげき・ぼうぎょを伸ばした状態でつるぎのまいを積む型です。

<!-- gate:rows start id=card:5 facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**他の型との違い:**

- はたきおとす：この型は必ず持ち、つるぎのまい型・はねやすめ型では選択技
- 持ち物：ハッサムナイト
- 5つの型で最も高い実数値：こうげき222・とくぼう120・すばやさ95
<!-- gate:rows end id=card:5 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">のろい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">はねやすめ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">きりばらい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガ・つるぎのまい型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（しんちょう・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（おくびょう・ルカリオナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・ふうせん）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（のんき・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr class="note"><td colspan="6" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体3件は除く。メタグロスは型で判定が変わらない</td></tr>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">とんぼがえり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">58.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+18.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+15.7pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">はねやすめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">66.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+10.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きりばらい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">62.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">34.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-27.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">はたきおとす</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-13.1pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">インファイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">34.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">27.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-7.4pt</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゴツゴツメット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+28.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のんき（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+25.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">オボンのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いじっぱり（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">37.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-31.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ハッサムナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-16.2pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
- いじっぱり：68.7%→37.4%（-31.3pt）。つるぎのまい型・メガ・つるぎのまい型が選んでいるため、型の増減とは言い切れません。
- ゴツゴツメット：21.7%→50.6%（+28.9pt）。のろい型・はねやすめ型・きりばらい型が持つため、型の増減とは言い切れません。
- つるぎのまい：62.2%→34.9%（-27.3pt）。つるぎのまい型・メガ・つるぎのまい型に共通のため、型の増減とは言えません。
- のんき：5.0%→30.9%（+25.9pt）。のろい型・きりばらい型が選んでいるため、型の増減とは言い切れません。
- とんぼがえり：58.5%→77.4%（+18.9pt）。記事のすべての型に共通のため、型の増減とは言えません。
- ハッサムナイト：33.9%→17.7%（-16.2pt）。メガ・つるぎのまい型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- のろい：8.5%→24.2%（+15.7pt）。のろい型だけが持つため、この変化はその型の増減を示します。
- はたきおとす：36.9%→23.8%（-13.1pt）。メガ・つるぎのまい型が持ち、つるぎのまい型・はねやすめ型でも選択技のため、型の増減とは言えません。
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
<!-- gate:rows start id=weak facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のとんぼがえりは確定2発。メガリザードンXのフレアドライブ（採用率30.5%）は確定1発で、S76対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ型の選択技ダブルウイングは乱数2発（63%）。メガリザードンYのかえんほうしゃ（採用率43.0%）は確定1発で、S85対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ型の選択技ダブルウイングは確定4発。メガカイリューのかえんほうしゃ（採用率65.2%）は確定1発で、S85対S152で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ型の選択技ダブルウイングは確定2発。メガボーマンダのすてみタックル（採用率73.5%）は確定2発で、S85対S172で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のインファイトは確定2発。エースバーンのかえんボール（採用率99.3%）は確定1発で、S85対S171で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ・つるぎのまい型のインファイトは確定3発。ヒートロトムのオーバーヒート（採用率96.3%）は確定1発で、S95対S106で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のとんぼがえりは乱数3発（>99%）（相手のオボンのみ込み）。ウォッシュロトムのハイドロポンプ（採用率97.9%）は確定3発で、S85対S106で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ・つるぎのまい型の選択技とんぼがえりは乱数1発（69%）。サザンドラのかえんほうしゃ（採用率74.9%）は確定1発で、S95対S225（スカーフ込み）で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のバレットパンチは確定2発（ばけのかわ込み）。ミミッキュのシャドークロー（採用率48.8%）は確定3発で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ<br><span style="font-size:0.8em;color:#64748b">メガセグレイブで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のバレットパンチは確定3発。メガセグレイブのじしん（採用率89.0%）は乱数3発（91%）で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のとんぼがえりは確定2発。マスカーニャのはたきおとす（採用率66.0%）は確定4発（ハッサムのオボンのみ込み）で、S85対S175で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のバレットパンチは確定2発。キラフロルのパワージェム（採用率86.9%）は乱数2発（79%）で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のとんぼがえりは確定2発。ゴリランダーのはたきおとす（採用率47.7%）は確定3発で、S76対S107で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のとんぼがえりは乱数3発（>99%）。ブラッキーのイカサマ（採用率96.0%）は確定4発で、同速（S85）ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい型のバレットパンチは確定1発。アローラキュウコンのふぶき（採用率66.9%）は乱数4発（82%）で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でハッサムと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" loading="lazy">
    <div class="name">キラフロル</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" loading="lazy">
    <div class="name">ブラッキー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率3位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カイリュー<br><span style="font-weight:normal;font-size:0.85em">同居率4位・メガカイリューで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">キラフロル<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ライチュウ<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガライチュウYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブラッキー<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガボーマンダで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ハッサムの弱点：ほのお技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX・メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ボーマンダ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ウォッシュロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サザンドラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ハッサムの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンX・メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；ボーマンダ＝すてみタックル・じしん；エースバーン＝かえんボール・とびひざげり・ダストシュート・ふいうち・とんぼがえり；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト；ウォッシュロトム＝ハイドロポンプ・ボルトチェンジ・10まんボルト；サザンドラ＝あくのはどう・りゅうせいぐん・かえんほうしゃ・とんぼがえり</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=2aaa1f7fac4a5c9ce572b8e97dbd3774741c6d76 -->
**強み**

- 得意な相手は7体です。使用率上位では、ミミッキュ（3位）・セグレイブ（13位）にバレットパンチ、マスカーニャ（17位）にとんぼがえりで勝てます。
- タイプ相性では、ノーマル・くさ・こおり・エスパー・むし・ドラゴン・はがね・フェアリーを半減以下、どくを無効で受けられます。

**弱み**

- 苦手な相手は8体です。使用率上位では、メガリザードンX（6位）のフレアドライブ、メガリザードンY（6位）・カイリュー（12位）のかえんほうしゃで先に倒されます。
- 弱点はほのお（×4）です。

**型の選び分け**

- 「のろい型」：他の型に無い技はのろい。
- 「つるぎのまい型」：はねやすめ型のはねやすめの代わりにつるぎのまいを持つ。
- 「はねやすめ型」：のろい型ののろいの代わりにインファイトを持つ。
- 「きりばらい型」：他の型に無い技はきりばらい。
- 「メガ・つるぎのまい型」：はたきおとすを必ず持つ（つるぎのまい型・はねやすめ型では選択技）。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は37位です（M-6: 42位）。
- 採用率の変化が大きいのはゴツゴツメット（+28.9pt）・つるぎのまい（-27.3pt）・とんぼがえり（+18.9pt）です。
<!-- gate:rows end id=summary -->

---

*関連記事：[ミミッキュ考察 M-7](/blog/mimikyu-analysis-m7/)*
