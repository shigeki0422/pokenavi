---
title: '【ポケモンチャンピオンズ】エルフーン考察 M-3 使用率47位 やどりぎ消耗型へシフトした採用率変化と立ち回り'
description: 'M-3シングルバトルで使用率47位のエルフーンを徹底分析。アンコール59.6%・やどりぎのタネ42.9%など、M-2からの技採用率の変化をデータで解説。いたずらごころ補助型の型別構成・環境上位への相性・パーティ構成まで紹介します。'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-whimsicott-m3.png'
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
  <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン" />
  <div>
    <h2 style="margin:0 0 8px">エルフーン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">47位</strong>　特性: <strong>いたずらごころ 98.0%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

シーズンM-3のシングルバトルで、エルフーンは**使用率47位**。特性**いたずらごころ**で変化技を優先度+1にして動かす補助役としての立ち位置はM-2から変わらないものの、**技構成の重心が「アンコール起点型」から「やどりぎ消耗型」へシフト**しています。アンコールが77.9%→59.6%と18pp低下し、やどりぎのタネが33.2%→42.9%と10pp上昇したことがその変化を示しています。

---

## なぜエルフーンが補助役として機能するのか

### 1. いたずらごころで変化技を先に通す

エルフーンの軸は**特性いたずらごころ**（採用率98.0%）。アンコール・おいかぜ・やどりぎのタネといった変化技が優先度+1で動くため、相手の攻撃より先に補助を差し込めます。すばやさ種族値116から変化技を優先度+1で先制できるため、S実数値184（おくびょうS32）と合わせて、相手より速い環境中速帯にも先手で補助を通せるのが最大の強みです。

### 2. やどりぎのタネ＋みがわりで削り続ける

M-3 でやどりぎのタネ採用率が42.9%（M-2比+9.7pp）に上昇しています。いたずらごころで先制してやどりぎを決めれば、毎ターン相手の最大HPの1/8を回収しながら削れます。みがわり（24.7%）やたべのこし（28.2%）を組み合わせることで複数ターン居座り、やどりぎで削り続ける消耗戦型が台頭しています。

### 3. おきみやげ・おいかぜで後続サポート

おきみやげ（33.7%）はいたずらごころで先制し、相手のA・Cを2段階下げて退場する技です。M-3では採用率がM-2比+7.3ppと上昇しており、アンコールで固定する戦術より「早期退場して後続に繋ぐ」戦術の比重が増しています。おいかぜ（50.9%）はガブリアス・ムクホーク・ライチュウなど、エルフーンと同居率の高い速攻アタッカーに加速を与える展開技として引き続き採用されています。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">77</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">116</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">480</span>
  </div>
</div>

すばやさ116は環境上位の速さで、おくびょうS32のS実数値は**184**。いたずらごころで変化技を優先度+1にすれば相手の通常攻撃より先に補助を差し込めます。S116の高さが活きるのは、同じいたずらごころ持ち同士やトリックルームといった同優先度帯で先手を確保できる局面です。こうげき67・とくこう77といずれも低く、ムーンフォースを除けば攻撃技の威力は高くないため、やどりぎやみがわり・補助技での貢献が主体です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="くさ" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく（×4）</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

くさ/フェアリーのタイプによりドラゴン技を無効化し、みず・でんき・くさ・じめん・かくとう・あくを耐性として持ちます。**どくが×4**（くさ×2・フェアリー×2）が最大の弱点で、ヘドロウェーブを採用するキラフロルやゲンガーに対して致命傷になります。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">分類</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致フェアリー打点。あくタイプ相手の唯一の攻撃手段</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いたずらごころで先制。積み技・変化技を3ターン固定</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おいかぜ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>50.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">味方のSを4ターン2倍。いたずらごころで先制展開</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やどりぎのタネ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>42.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">毎ターン最大HPの1/8を吸収。消耗戦型の核</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おきみやげ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・Cを2段階下げ退場。後続の着地点確保</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やどりぎ・たべのこしと組み合わせ消耗戦を成立させる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がむしゃら</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タスキ後の詰め。M-2比-25.5ppと大幅減少</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガドレイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致くさ打点＋HP吸収。M-2比+9.5ppと上昇</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">受け・展開役の変化技をいたずらごころで先制封じ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>コットンガード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Bを3段階上げ。やどりぎ型で物理を受け流す型に</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1: きあいのタスキ 速攻起点型（最多採用）

**主要EV: H2-C32-S32 43.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ 速攻起点型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いたずらごころ（98.0%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）／ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32（S実数値184。C実数値はひかえめ141・おくびょう129）<br>
<strong>持ち物:</strong> きあいのタスキ（51.2%）
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・アンコール<br>
・おいかぜ / おきみやげ<br>
・やどりぎのタネ / みがわり
</div>
</div>
</div>

**強み:**

タスキで最初の行動を確実に保証し、いたずらごころの変化技（アンコール・おいかぜ・おきみやげのいずれか）を相手より先に通します。S実数値184はおうじゃのしるし等の補助なしで多くの中速環境ポケモンを上回り、変化技の優先度加算前でも先手を確保しやすいです。

**弱み:**

タスキは一度きりで、ステルスロックや砂嵐・あられで潰れると初動の補助が通らなくなります。また**あくタイプには変化技が無効**で、アンコール・おきみやげ・ちょうはつが通らないため、初手に悪タイプが出た場合は仕事のほとんどを失います。

---

### 型2: たべのこし やどりぎ消耗型

**主要EV: H32-B32 1.3%（HB配分の指標）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">たべのこし やどりぎ消耗型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いたずらごころ（98.0%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）／おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 B32（HB耐久）<br>
<strong>持ち物:</strong> たべのこし（28.2%）
</div>
<div>
<strong>技構成:</strong><br>
・やどりぎのタネ<br>
・みがわり<br>
・アンコール / ちょうはつ<br>
・ムーンフォース / コットンガード
</div>
</div>
</div>

**強み:**

やどりぎのタネ＋たべのこし＋みがわりで複数ターン居座り、じわじわ削り続ける消耗戦型です。コットンガードでBを3段階上げれば物理アタッカーの攻撃を流しながらやどりぎで削れます。タスキ型が「1ターンの仕事人」なのに対し、こちらは相手のHPを継続的に削ることで後続の詰めに繋げます。

**弱み:**

タスキで初手を保証する型1と異なり、被弾を耐える保証がないため、消耗戦を成立させる前に落とされるリスクがあります。あくタイプ相手にはやどりぎのタネ・みがわりといった消耗戦の核が機能せず、ムーンフォース頼みの削りになり、この型本来の戦術を発揮できません。

---

## データ分析①：M-2からM-3への技採用率の変化

エルフーンの技構成はM-3で大きく変化しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">差分</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ムーンフォース</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">91.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">86.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#1d4ed8">-5.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アンコール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">59.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">-18.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おいかぜ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#1d4ed8">-5.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">やどりぎのタネ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">42.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">+9.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おきみやげ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+7.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">がむしゃら</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">43.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">-25.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ギガドレイン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">+9.5pp</td>
</tr>
</tbody>
</table>
</div>

最も大きな変化は**アンコールの18pp減とがむしゃらの25pp減**です。がむしゃらはタスキ運用（被弾後に相手をHP1まで削る即詰め技）と一体の技で、この大幅減少はタスキ後の瞬間詰めよりも持続的な戦術を選ぶプレイヤーが増えたことを示しています。連動して**やどりぎのタネが+9.7pp、ギガドレインが+9.5pp**と上昇し、HPを回収しながら削り続けるスタイルへのシフトが数値に表れています。

持ち物でも同じ傾向が確認できます。きあいのタスキが61.7%→51.2%と低下し、たべのこしが23.5%→28.2%と上昇しています。タスキと不可分だったがむしゃらの減少と合わせて、消耗戦型の増加が複数の指標から裏付けられます。

---

## 苦手なポケモンと対策

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくタイプに変化技が無効。アンコール・おきみやげ・ちょうはつが失敗し、S123で上から処理される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす・トリプルアクセルを物理耐久で受けられるはがね枠に引く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく×4）で一撃。ステルスロック（54.8%）でタスキも潰される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん技で弱点を突けるガブリアス等を後ろに控えさせ受け出し処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（30位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・採用率79.3%）が×4で一撃。変化技は通るが被弾前提のため実質機能しない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー打点を持つ後続に繋ぐ。エルフーンで相手取らない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド（はがね・採用率31.1%）が×2。ムーンフォースもはがねで半減され有効打が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコールで技を固定できても押し切れないため、物理受け枠に引くのが基本</td>
</tr>
</tbody>
</table>
</div>

苦手筋の中心は**あくタイプ**です。いたずらごころで優先度が上がった変化技はあくタイプに無効化されるため、マスカーニャ・ゲッコウガ・サザンドラが初手に来た場合は引くのが鉄則です。

---

## パーティ構成

### M-3 同居率上位パートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おいかぜで加速する環境1位地面枠。エルフーンの悪・はがねへの地面打点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おいかぜで加速するでんき枠。エルフーンが苦手なひこう・みずへの電気打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おいかぜで加速するほのお/ひこう枠。どく弱点のエルフーンに代わりほのおを受けられる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでエルフーンのどく弱点を補完。おいかぜ後の速攻枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おいかぜで加速するかくとう/ひこう枠。いかくでAを下げながら高火力で制圧する速攻アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">どく無効・はがね半減で高耐久。エルフーンの弱点どく・ほのお・こおりの引き先</div>
  </div>
</div>

**M-3 パーティ構成の方針:**

M-3 のエルフーンは依然としておいかぜ展開の軸として同居率上位を占めています。ガブリアス（1位）・ライチュウ（2位）・ムクホーク（6位）はおいかぜ後の速攻アタッカー枠として同居率が高く、エルフーンがおいかぜを張ってから引いてアタッカーを通す展開が基本構成です。アーマーガア（9位）はエルフーンのどく・ほのお弱点を補う受け枠として引き続き選ばれています。

---

## まとめ

M-3のエルフーンは**使用率47位**。いたずらごころで変化技を先に通す補助役としての基本軸はM-2から変わりませんが、技構成の重心は「アンコール即詰め型」から「やどりぎ消耗型」へシフトしています（データ分析①参照）。

明確な苦手筋は**あくタイプ**（変化技が無効）と**どく技持ち**（×4弱点）の2点で、この2つへの対応が必須です。おいかぜで加速したい速攻アタッカーのサポート役として組み込み、悪タイプへの引き先と毒弱点のカバー枠をパーティで用意することが運用の前提になります。

---

## 関連記事

- [M-2シーズンのエルフーン考察](/blog/whimsicott-analysis-m2/)
- [同居率1位 ガブリアスのM-3考察](/pokemon/garchomp/)
- [同居率6位 メガムクホークのM-3考察](/blog/staraptor-analysis-m3/)
