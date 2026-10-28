---
title: '【ポケモンチャンピオンズ】サーナイト 考察 M-7 シーズン 使用率68位の3型解説'
description: 'M-7シーズン使用率68位（M-6: 80位）のサーナイトを考察。サーナイトナイト採用率82.8%、ハイパーボイス77.2%・サイコノイズ52.6%を軸に、メガシンカ型・きあいのタスキ型・メガ・めいそう型の3つの型の違いと、苦手・得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-28'
heroImage: '../../assets/hero-gardevoir-m7.png'
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
  <img src="/images/pokemon/pokemon-0282-00.webp" alt="サーナイト" />
  <div>
    <h2 style="margin:0 0 8px">サーナイト</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">68位</strong>（M-6: 80位）　持ち物: <strong>サーナイトナイト 82.8%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのサーナイトは使用率68位です（M-6: 80位）。サーナイトナイトでメガ進化する運用が中心で、特性はトレースが93.3%を占めます。ハイパーボイス（採用率77.2%）・マジカルフレイム（76.0%）・しんくうは（75.1%）・サイコノイズ（52.6%）の特殊技を軸に、技構成・持ち物の違いから3つの型に分かれます。

---

## サーナイトの基本スペック

<!-- gate:rows start id=base_stats facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
### 種族値（通常→メガサーナイト）

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
      <div style="width:34%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">68</span><span style="width:32px;text-align:right">68</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:32.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">65</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">85</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span><span style="width:32px;text-align:right">65</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:62.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:20%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">125</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">165</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:57.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#34d399,#059669);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">115</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">135</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:40%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:10%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">100</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">518</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">618</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

### 特性

<strong>トレース（93.3%）</strong>は、登場した時に相手の特性と同じ特性になります。メガ進化後は特性が<strong>フェアリースキン</strong>に変わり、ノーマルタイプの技がフェアリータイプになり、威力が上がります。ハイパーボイス（採用率77.2%）はノーマルタイプの技で、メガ後はフェアリータイプの技として撃てます。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイパーボイス</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">77.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルフレイム</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">76.0%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の特攻を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんくうは</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコノイズ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">52.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">2ターンの間、相手をかいふくふうじ状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">20.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特攻を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.5%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をまひ状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">サイコショック</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の防御の能力値でダメージ計算する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">ワイドフォース</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.7%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">サイコフィールド状態の効果を受けている場合、威力が1.5倍になり相手全体を攻撃する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻と特防が1段階ずつ上がる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物の組み合わせから、3つの型を紹介します。

### 型1：メガシンカ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0282-00.webp" alt="サーナイト" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガシンカ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> トレース（メガ後フェアリースキン）<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H32-C14-S20<br>
<strong>持ち物:</strong> サーナイトナイト
</div>
<div>
<strong>技構成:</strong><br>
・ハイパーボイス<br>
・しんくうは<br>
・マジカルフレイム<br>
・サイコノイズ
</div>
</div>
</div>

サーナイトナイト持ちの基本形で、4つの攻撃技で攻める型です。

<!-- gate:rows start id=card:1 facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
**他の型との違い:**

- 他の型に無い技：サイコノイズ
- ハイパーボイス：この型は必ず持ち、メガ・めいそう型では選択技
- しんくうは：この型は必ず持ち、メガ・めいそう型では選択技
<!-- gate:rows end id=card:1 -->

---

### 型2：きあいのタスキ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0282-00.webp" alt="サーナイト" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> トレース<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・10まんボルト<br>
・エナジーボール<br>
・トリックルーム<br>
選択技：サイコキネシス・ワイドフォース・アンコール
</div>
</div>
</div>

メガ枠を他のポケモンに回すパーティで使う型です。

<!-- gate:rows start id=card:2 facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
**他の型との違い:**

- 他の型に無い技：ムーンフォース・エナジーボール・トリックルーム
- 10まんボルト：この型は必ず持ち、メガ・めいそう型では選択技
- 持ち物：きあいのタスキ（HPが満タンの時、一撃でひんしになる技のダメージを受けてもHPを1残して耐える。1度使うと無くなる）
- 3つの型で最も低い実数値：HP145・とくこう194・とくぼう135・すばやさ132
<!-- gate:rows end id=card:2 -->

---

### 型3：メガ・めいそう型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0282-00.webp" alt="サーナイト" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガ・めいそう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> トレース（メガ後フェアリースキン）<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H32-C14-S20<br>
<strong>持ち物:</strong> サーナイトナイト
</div>
<div>
<strong>技構成:</strong><br>
・サイコキネシス<br>
・マジカルフレイム<br>
・めいそう<br>
・みがわり<br>
選択技：10まんボルト・しんくうは・ハイパーボイス
</div>
</div>
</div>

攻撃技が2つで、他の2型より攻撃技の数が少ない型です。

<!-- gate:rows start id=card:3 facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
**他の型との違い:**

- 他の型に無い技：めいそう・みがわり
- サイコキネシス：この型は必ず持ち、きあいのタスキ型では選択技
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガシンカ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">きあいのタスキ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガ・めいそう型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（ひかえめ・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY（ひかえめ・リザードナイトY）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（おくびょう・ルカリオナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・ふうせん ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">セグレイブ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガセグレイブ（いじっぱり・セグレイブナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（いじっぱり・ボーマンダナイト ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（ようき・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガキラフロル（おくびょう・キラフロルナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サイコノイズ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">52.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+34.3pt</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">しんくうは</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">56.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">75.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+18.5pt</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ハイパーボイス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">59.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+17.9pt</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">マジカルフレイム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">58.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">76.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+17.4pt</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ムーンフォース</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-18.0pt</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サイコキネシス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-13.9pt</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">10まんボルト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-8.2pt</span></td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サーナイトナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">82.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+14.0pt</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-7.0pt</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-3.6pt</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ひかえめ（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">63.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#059669">+14.3pt</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おくびょう（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">14.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#dc2626">-9.2pt</span></td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
- サイコノイズ：18.3%→52.6%（+34.3pt）。メガシンカ型だけが持つため、この変化はその型の増減を示します。
- しんくうは：56.6%→75.1%（+18.5pt）。メガシンカ型が持ち、メガ・めいそう型でも選択技のため、型の増減とは言えません。
- ムーンフォース：38.8%→20.8%（-18.0pt）。記事の型ではきあいのタスキ型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- ハイパーボイス：59.3%→77.2%（+17.9pt）。メガシンカ型が持ち、メガ・めいそう型でも選択技のため、型の増減とは言えません。
- マジカルフレイム：58.6%→76.0%（+17.4pt）。メガシンカ型・メガ・めいそう型に共通のため、型の増減とは言えません。
- ひかえめ：63.4%→77.7%（+14.3pt）。記事のすべての型が選んでいるため、型の増減とは言えません。
- サーナイトナイト：68.8%→82.8%（+14.0pt）。メガシンカ型・メガ・めいそう型が持つため、型の増減とは言い切れません。
- サイコキネシス：33.4%→19.5%（-13.9pt）。メガ・めいそう型が持ち、きあいのタスキ型でも選択技のため、型の増減とは言えません。
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
<!-- gate:rows start id=weak facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは乱数2発（56%）。ミミッキュのかげうち（採用率96.5%）は確定2発で、優先度+1のかげうちで先に動かれ、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定1発。メガリザードンXのフレアドライブ（採用率30.5%）は確定1発で、S140対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定1発。イダイトウ(オス)のウェーブタックル（採用率89.5%）は乱数1発（94%）で、S140対S214（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のマジカルフレイムは確定2発。メガメタグロスのバレットパンチ（採用率90.6%）は確定2発で、優先度+1のバレットパンチで先に動かれ、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定2発。ゴリランダーのウッドハンマー（採用率12.9%・少数派）は確定2発で、最後はグラスフィールドで優先度+1のグラススライダーで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のサイコノイズは確定1発。オオニューラのフェイタルクロー（採用率95.8%）は確定1発で、S140対S172で後手のため、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。先後はトリックルームを使わない場合の判定。</td></tr>
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
<!-- gate:rows start id=strong facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定1発。ガブリアスのじしん（採用率65.5%）は確定2発で、S140対S253（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定2発。カバルドンのじしん（採用率97.3%）は確定2発で、S140対S67で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のマジカルフレイムは確定2発。アーマーガアのブレイブバード（採用率27.5%）は乱数2発（97%）で、S140対S78で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型のムーンフォースは確定2発。メガカイリューの10まんボルト（採用率59.5%）は乱数3発（81%）で、S132対S152で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型のムーンフォースは確定2発。イエッサン(オス)のワイドフォース（採用率99.7%）は確定3発で、S132対S161で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは乱数2発（81%）。メガライチュウYのでんじほう（採用率96.5%）は確定3発で、S140対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定2発。ブラッキーのイカサマ（採用率96.0%）は確定3発で、S140対S85で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型の選択技サイコキネシスは確定3発。ヒートロトムの10まんボルト（採用率30.6%）は乱数4発（>99%）で、S132対S106で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型のムーンフォースは確定3発。ウォッシュロトムの10まんボルト（採用率44.7%）は乱数3発（>99%）で、S132対S106で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型のムーンフォースは確定2発。アローラキュウコンのふぶき（採用率66.9%）は確定3発で、S132対S177で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガシンカ型のハイパーボイスは確定1発。サザンドラのあくのはどう（採用率98.5%）は乱数3発（>99%）で、S140対S225（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。先後はトリックルームを使わない場合の判定。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でサーナイトと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" loading="lazy">
    <div class="name">エースバーン</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率4位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">エースバーン<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イダイトウ(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">マスカーニャ<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガサーナイトの弱点：どく技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガサーナイトの弱点：はがね技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガサーナイトの弱点：ゴースト技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○2</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝メガサーナイトの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ミミッキュ＝じゃれつく・かげうち・シャドークロー・ウッドハンマー；メガリザードンX＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；イダイトウ(オス)＝おはかまいり・アクアジェット・ウェーブタックル・クイックターン；メタグロス＝バレットパンチ・サイコファング・れいとうパンチ・じしん・かみなりパンチ；ゴリランダー＝グラススライダー・ドラムアタック・とんぼがえり・10まんばりき・はたきおとす；オオニューラ＝インファイト・フェイタルクロー・ねこだまし・じごくづき</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=bc8bc7ec34ec07b3c2c632df141a40e92fa527f8 -->
**強み**

- 得意な相手は11体です。使用率上位では、ガブリアス（1位）・カバルドン（4位）にハイパーボイス、アーマーガア（11位）にマジカルフレイムで勝てます。
- タイプ相性では、かくとう・エスパーを半減以下、ドラゴンを無効で受けられます。

**弱み**

- 苦手な相手は6体です。使用率上位では、ミミッキュ（3位）のかげうち、メガリザードンX（6位）のフレアドライブ、イダイトウ(オス)（10位）のウェーブタックルで先に倒されます。
- 弱点はどく・ゴースト・はがねです。

**型の選び分け**

- 「メガシンカ型」：他の型に無い技はサイコノイズ。
- 「きあいのタスキ型」：他の型に無い技はムーンフォース・エナジーボール・トリックルーム。
- 「メガ・めいそう型」：他の型に無い技はめいそう・みがわり。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は68位です（M-6: 80位）。
- 採用率の変化が大きいのはサイコノイズ（+34.3pt）・しんくうは（+18.5pt）・ムーンフォース（-18.0pt）です。
<!-- gate:rows end id=summary -->
