---
title: '【ポケモンチャンピオンズ】コノヨザル考察 M-3 使用率45位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率45位のコノヨザルを徹底分析。ふんどのこぶし採用率98.0%・ビルドアップ77.8%の積み全抜き型と、まけんき60.3%でいかく反転を活かす構成を実データで解説。環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-19'
heroImage: '../../assets/hero-annihilape-m3.png'
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
  <img src="/images/pokemon/pokemon-0979-00.webp" alt="コノヨザル" />
  <div>
    <h2 style="margin:0 0 8px">コノヨザル</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">45位</strong>　特性: <strong>まけんき 60.3%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/19時点）の集計です

シーズンM-3のシングルバトルで、コノヨザルは**使用率45位**を記録。かくとう/ゴーストというタイプ複合は、**ノーマル技とかくとう技を両方無効化する唯一の組み合わせ**であり、ビルドアップで積みながらドレインパンチで回復しつつ全抜きを狙える耐久積みアタッカーとして環境に定着しています。

特性は**まけんき**が60.3%と最多で、いかくや能力低下技を受けるとこうげきが2段階上昇します。能力低下を逆用して積みの起点にできる点が、ドレインパンチ・ビルドアップと組み合わさった際の脅威の核心です。

---

## なぜ今コノヨザルが使用率45位なのか

### 1. ノーマル・かくとうを両方無効化する唯一のタイプ複合

かくとう/ゴーストの複合は、かくとう技がゴーストタイプに無効（×0）、ノーマル技もゴーストタイプに無効（×0）となることで、**ノーマルとかくとうの両タイプを同時に無効化する唯一の組み合わせ**です。環境上位に多いノーマル技（すてみタックル・ねこだまし等）やかくとう技（インファイト・ドレインパンチ等）が通らないため、これらを主力とする物理アタッカーに対して受け出しやすい立ち位置を取れます。

### 2. ふんどのこぶし＋ビルドアップ＋ドレインパンチで自己完結した全抜き構成

ふんどのこぶし（採用率98.0%）は受けたダメージ量に応じて威力が増加するタイプ一致技で、ビルドアップ（77.8%）でこうげき・ぼうぎょを同時に積みながら、ドレインパンチ（89.0%）でHPを回復することで、積んだ後の場持ちを高められます。回復しながら積み続けることで、後続の物理アタッカーを順次突破する全抜き展開が成立します。

### 3. まけんきでいかく等の能力低下を逆用できる

特性まけんき（60.3%）は、いかくや能力低下技を受けるとこうげきが2段階上昇します。いかく持ちのギャラドスやムクホークが繰り出してきたターンを逆用してA+2の状態を作り、そのまま積みの起点に転じられます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">110</strong></span>
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
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">535</span>
  </div>
</div>

HP110・こうげき115と物理攻撃に必要な耐久・火力は十分なラインです。ぼうぎょ80は積む前の物理耐久としては低めですが、ビルドアップを1〜2回積めば実質的な物理耐久を引き上げられます。とくぼう90はドレインパンチと組み合わせることで回復補助が効き、特殊攻撃への対応もある程度確保できます。すばやさ90は環境の中速帯に位置し、S90未満の相手には先手が取れる一方、S90超の高速勢には上から動かれます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ゴースト" />
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
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく（×0.5）</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ（×0.5）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

かくとう/ゴーストの複合により**ノーマル・かくとうを両方無効化**します。むし技は×0.25の超耐性になります。一方、弱点はひこう・エスパー・ゴースト・フェアリーの4タイプで、いずれも×2です。環境上位のフェアリー技（アシレーヌのムーンフォース等）やエスパー技には弱く、後出しには注意が必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ふんどのこぶし</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドレインパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">89.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">77.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">58.4%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アンコール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>インファイト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>がんせきふうじ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3.3%</td>
</tr>
</tbody>
</table>
</div>

特性は**まけんき60.3%・やるき34.5%**の二択。まけんきはいかく等の能力低下を逆用してこうげきを2段階上げられる攻撃的な択で、やるきはねむり状態を完全無効化する安定性重視の択です。環境にいかく持ちが多い場合はまけんきが積む機会を増やし、催眠技を多用する相手が多い場合はやるきが安定します。

---

## 主要型の解説

性格分布はいじっぱり42.1%・ようき33.3%の2択が中心で、こうげきを最大化するいじっぱりと素早さを確保するようきに二分されます。

### 型1: いじっぱり積み全抜き型（最多採用）

**性格採用率: いじっぱり 42.1%**（こうげき最大化の積み型。EV分布 H32-A32-S2 5.8%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0979-00.webp" alt="コノヨザル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱり積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> まけんき（60.3%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（HPと火力を同時に最大化）<br>
<strong>持ち物:</strong> たべのこし（50.6%）/ オボンのみ（28.9%）
</div>
<div>
<strong>技構成:</strong><br>
・ふんどのこぶし<br>
・ドレインパンチ<br>
・ビルドアップ<br>
・ちょうはつ
</div>
</div>
</div>

**強み:**

いじっぱりでこうげきを最大化し、ビルドアップで積みながらドレインパンチで回復する自己完結した型です。ノーマル・かくとう技を無効化する対面でビルドアップを積み始め、ドレインパンチで場持ちを維持しながら全抜きを狙います。まけんき個体では、相手がいかくを使うほどこうげきが2段階上がるため、いかく持ちポケモンが繰り出してきたターンを積みの起点にできます。ちょうはつは相手の回復技や変化技を3ターン封じ、積んだ後の場持ちをさらに高めます。すばやさに振らずこうげきを最大化するため、ようき型では2発になる相手をビルドアップ1積み後に1発で落とせる火力が出ます。

**弱み:**

ようき型と比べてすばやさに振らないため、S90超の相手（カイリュー・リザードン等）に先手を取られます。ビルドアップを積む前のぼうぎょ80は高くなく、上から弱点技（ひこう・フェアリー等）を受けると積みの隙を作れません。また、ふんどのこぶしはHP満タン状態での1発目は威力35と低く、積む前に動ける場面を見極める必要があります。

---

### 型2: ようき先手確保型（2番目に多い構成）

**性格採用率: ようき 33.3%**（素早さ確保の積み型。EV最多分布 H32-S32 8.4%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0979-00.webp" alt="コノヨザル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HSようき先手型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> まけんき（60.3%）/ やるき（34.5%）<br>
<strong>性格:</strong> ようき（S↑ D↓）<br>
<strong>EV:</strong> H32 S32（採用率8.4%。HPと素早さを同時に最大化）<br>
<strong>持ち物:</strong> たべのこし（50.6%）/ オボンのみ（28.9%）
</div>
<div>
<strong>技構成:</strong><br>
・ふんどのこぶし<br>
・ドレインパンチ<br>
・ビルドアップ<br>
・ちょうはつ / ステルスロック
</div>
</div>
</div>

**強み:**

ようきはS実数値156で、いじっぱり型（無補正142）では先手を取れない使用率3位のミミッキュ（採用率77.4%のいじっぱりでS実数値148）を通常攻撃では上から動けます。ただしミミッキュは先制技かげうち（ゴーストでコノヨザルに弱点を突く）とばけのかわを持つため、この素早さ差で対面を制せるわけではなく、化けの皮を消費させた後にかげうち以外で打ち合う局面で活きる差です。それでも、いじっぱり型がまったく先手を取れないのに対し、ようき型なら積み技や交代読みで先に動く選択肢を確保できる点が実数値差として効きます。また、ステルスロック（16.1%）との組み合わせでは、相手の交代をより安全に誘えるため、設置技の展開役としての動きも取りやすくなります。やるき個体ではねむり技を完全無効化し、催眠展開から守れます。

**弱み:**

こうげきを最大化するいじっぱり型と比べてA実数値が低くなり、同じビルドアップ1積み後でも一撃で落とせる相手が狭くなります。火力不足は積み回数を重ねて補う必要があります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

かくとう/ゴーストはノーマル・かくとうを無効化するため、これらを主力とする物理アタッカーに強い一方、弱点のひこう・エスパー・ゴースト・フェアリーを持ち、かつS90以上の相手には先手を取られるリスクがあります。

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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドドゲザンのふいうち（あく）はかくとう無効ではなく等倍だが、ドレインパンチが×4（あく×2・はがね×2）で通り高火力を出せる。こちらのかくとう技をゴーストタイプ無効で受けられないドドゲザンには、ドレインパンチで一方的に打点を通せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">バシャーモ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力のインファイト（65.0%）・とびひざげり（19.7%）といったかくとう技をゴーストタイプで無効化できる。フレアドライブ（ほのお）は等倍止まりで、S80のバシャーモにはこちらが先手を取れるため、かくとう技を透かしながら殴り合える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のインファイト（かくとう）はゴーストタイプで無効化できる。こちらはドレインパンチが×2で刺さるが（ふんどのこぶしは等倍）、メガ後の最速個体でS実数値180に達しこちらより速く、積む前に上から削られ、加えて優先度技のバレットパンチでも削られるため対面では押し負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー）が×2弱点で刺さる。こちらはふんどのこぶしが等倍・ドレインパンチが×0.5半減と打点が乏しく、高いとくぼうもあって削り切れない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプを持ちこちらの弱点を突けるブレイブバード（ひこう×2）を受けやすく、こちらのタイプ一致技も等倍〜半減止まりで有効打に欠ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）・げきりん（ドラゴン）はいずれも等倍で通り、S102でこちらより速い。こちらのふんどのこぶし・ドレインパンチも等倍止まりで弱点を突けず、上から殴り合う展開では不利</td>
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
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプを持ち、こちらの弱点を突くブレイブバード（ひこう×2）が刺さる。S80でこちらより遅いため先手は取れるが、マルチスケイルで弱点でない技1発を耐えてから反撃される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり×4が刺さるため、れいとうパンチ（採用率10.5%）採用個体ならマルチスケイル解除後に縛れる。非採用なら同居率上位ライチュウのでんき技で対面前に削る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技（ムーンフォース）が×2弱点。ドレインパンチが半減・ふんどのこぶしも等倍で、高いとくぼうを抜けず削り切れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき×2が刺さる同居率上位のライチュウ・ブリジュラスを後続に控え、アシレーヌが出たら交代してでんき技で落とす</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちら（S90）より速く、とんぼがえり（先制で対面操作）・はたきおとし（オボンのみ等の持ち物剥奪）でこちらの積み展開を崩しながら主導権を握られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふんどのこぶしがマスカーニャ（くさ/あく）に×2で刺さるため対面の打ち合いは互角以上だが、とんぼがえりで安定して逃げられる。引き先を読んでビルドアップを積む隙を作るか、後続のアタッカーで縛って交代を許さない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（使用率3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー×2）・かげうち（ゴースト×2の先制技）で弱点を突かれる。ばけのかわで攻撃1回を無効化されるうえ、ドレインパンチ（かくとう）は無効化されるため、積む前に削られやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふんどのこぶし（ゴースト×2）で殴り返せるが、ばけのかわを剥がす1手が必要。同居率上位のメタグロス（はがね/エスパー）でフェアリー技を半減しつつコメットパンチで処理する</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。コノヨザルが苦手なひこう・フェアリー弱点をサポートするアタッカーを添えるパターン</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき・ドラゴン・はがねの広い打点。アシレーヌ（みず）・ギャラドスへでんき技で弱点を突ける補完枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんきの高速アタッカー。コノヨザルが苦手なアシレーヌ（みず）・ひこう系にでんき技で弱点を突ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうの高速物理枠。コノヨザルが処理しにくいくさ・むし・かくとう系に上から打点を入れる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでフェアリーに弱点を突く枠。コノヨザルが苦手なアシレーヌ・ハバタクカミへ打点を持てる</div>
  </div>
</div>

**パーティ構成の基本方針:**

コノヨザルはビルドアップ＋ドレインパンチで自己完結した全抜き構成を取れる一方、弱点のひこう・エスパー・ゴースト・フェアリーをパーティ単位でカバーする必要があります。残り5体で以下を補います。

1. **ひこう対策**: いわ・でんき技を持つ枠でコノヨザルが苦手なひこうタイプ（カイリュー・ムクホーク）に打点を入れる
2. **フェアリー対策**: はがね・どく技を持つアタッカーでアシレーヌ・ハバタクカミへの打点を用意する
3. **高速枠との速度差補完**: S90超の高速ポケモンに対してコノヨザルより先に削れるアタッカーを添える
4. **まけんき連携**: いかく持ちが多い環境では、コノヨザルを先発に置いていかくを受けてA+2の状態から積み始め、後続の全抜きにつなぐ

---

## データ分析①：ふんどのこぶし98.0%が示す「受けてから崩す」設計

コノヨザルの技採用率を並べると、ふんどのこぶし（98.0%）の採用率が突出しています。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| ふんどのこぶし | 攻撃 | 98.0% | 受けるほど威力が上がるメイン技 |
| ドレインパンチ | 攻撃 | 89.0% | 回復しながら削るサブ技 |
| ビルドアップ | 変化 | 77.8% | A・B同時積み |
| ちょうはつ | 変化 | 58.4% | 相手の変化技封じ |
| ステルスロック | 変化 | 16.1% | 設置技 |

ふんどのこぶしとドレインパンチの両採用率がともに89%超であることは、「受けてHP減少→ふんどのこぶしの威力増加→ドレインパンチで回復」というサイクルが構成の核心であることを示しています。ビルドアップ77.8%と合わせると、**受け出し→積み→回復の自己完結ループが主流型の設計思想**であることが採用率から読み取れます。

一方、ちょうはつ58.4%の採用は注目に値します。コノヨザルは積んだ後の突破が難しいため、相手が回復技や積み返し技でカウンターしてくることを想定しており、ちょうはつで3ターン変化技を封じることで積みの安全圏を確保しようとしています。

持ち物はたべのこし50.6%・オボンのみ28.9%が合わせて79.5%を占め、回復実の運用が主流です。攻撃的な持ち物（きあいのタスキ3.9%）の採用率はごくわずかで、**長期戦・持久戦を前提とした耐久運用**が実態に即しています。遭遇時はまず回復実を持つ積み型を疑い、ふんどのこぶし・ビルドアップ・ドレインパンチ・ちょうはつの4技構成を前提に対策を立てるのが確率的に妥当です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HAいじっぱり積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 42.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふんどのこぶし・ドレインパンチ・ビルドアップ・ちょうはつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こうげきを最大化し積み後の一撃が重い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S90超の相手に先手を取られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HSようき先手型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 33.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふんどのこぶし・ドレインパンチ・ビルドアップ・ちょうはつ/ステルスロック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値156でいじっぱりミミッキュ（148）を抜ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型より積み後の火力が劣る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

コノヨザルはかくとう/ゴーストという唯一のタイプ複合でノーマル・かくとうを無効化し、ビルドアップ＋ドレインパンチ＋たべのこしによる自己完結した積み全抜き構成が主流です。まけんき（60.3%）によりいかく等の能力低下を逆用できる点が戦略の幅を広げており、ふんどのこぶし（98.0%）の採用率の高さは「受けてから崩す」設計の徹底を示しています。

弱点はひこう・エスパー・ゴースト・フェアリーの4タイプで、特にフェアリー技を持つアシレーヌや高速ゴーストタイプとの対面は不利です。積む隙を与えられるかどうかが使用判断の軸となるため、パーティではコノヨザルが苦手とするひこう・フェアリー枠を別途カバーする枠を用意することが前提となります。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [みず枠パートナー ラグラージのM-3考察](/blog/swampert-analysis-m3/)
- [はがねタイプのメガメタグロスのM-3考察](/blog/metagross-analysis-m3/)
