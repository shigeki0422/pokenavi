---
title: '【ポケモンチャンピオンズ】コノヨザル考察 M-3 使用率40位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率40位のコノヨザルを徹底分析。ふんどのこぶし採用率98.7%・ビルドアップ75.9%の積み全抜き型と、まけんき55.3%でいかく反転を活かす構成を実データで解説。環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-20'
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
      使用率: <strong style="color:#e67e22">40位</strong>　特性: <strong>まけんき 55.3%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、コノヨザルは**使用率40位**を記録。かくとう/ゴーストというタイプ複合は、**ノーマル技とかくとう技を両方無効化する唯一の組み合わせ**であり、ビルドアップで積みながらドレインパンチで回復しつつ全抜きを狙える耐久積みアタッカーとして環境に定着しています。

特性は**まけんき**が55.3%と最多で、いかくや能力低下技を受けるとこうげきが2段階上昇します。能力低下を逆用して積みの起点にできる点が、ドレインパンチ・ビルドアップと組み合わさった際の脅威の核心です。

---

## なぜ今コノヨザルが使用率40位なのか

### 1. ノーマル・かくとうを両方無効化する唯一のタイプ複合

かくとう/ゴーストの複合は、かくとう技がゴーストタイプに無効（×0）、ノーマル技もゴーストタイプに無効（×0）となることで、**ノーマルとかくとうの両タイプを同時に無効化する唯一の組み合わせ**です。環境上位に多いノーマル技（すてみタックル・ねこだまし等）やかくとう技（インファイト・ドレインパンチ等）が通らないため、これらを主力とする物理アタッカーに対して受け出しやすい立ち位置を取れます。

### 2. ふんどのこぶし＋ビルドアップ＋ドレインパンチで自己完結した全抜き構成

ふんどのこぶし（採用率98.7%）は受けたダメージ量に応じて威力が増加するタイプ一致技で、ビルドアップ（75.9%）でこうげき・ぼうぎょを同時に積みながら、ドレインパンチ（89.4%）でHPを回復することで、積んだ後の場持ちを高められます。回復しながら積み続けることで、後続の物理アタッカーを順次突破する全抜き展開が成立します。

### 3. まけんきでいかく等の能力低下を逆用できる

特性まけんき（55.3%）は、いかく・威嚇系の技や能力低下効果を受けるとこうげきが2段階上昇します。相手がいかくを使うほどこうげきが上がる構造のため、いかく持ちポケモン（ガブリアスがいかくを持つケース等）が展開しやすい環境ではコノヨザルの積み始める隙を与える結果になります。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.7%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドレインパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">89.4%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">75.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">61.1%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">19.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アンコール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9.2%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8.7%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>インファイト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5.1%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>がんせきふうじ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2.8%</td>
</tr>
</tbody>
</table>
</div>

特性は**まけんき55.3%・やるき39.3%**の二択。まけんきはいかく等の能力低下を逆用してこうげきを2段階上げられる攻撃的な択で、やるきはねむり状態を完全無効化する安定性重視の択です。環境にいかく持ちが多い場合はまけんきが積む機会を増やし、催眠技を多用する相手が多い場合はやるきが安定します。

---

## 主要型の解説

性格分布はいじっぱり40.9%・ようき34.8%の2択が中心で、こうげきを最大化するいじっぱりと素早さを確保するようきに二分されます。

### 型1: いじっぱり積み全抜き型（最多採用）

**性格採用率: いじっぱり 40.9%**（こうげき最大化の積み型。EV最多分布 H32-A32 11.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0979-00.webp" alt="コノヨザル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱり積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> まけんき（55.3%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（採用率11.2%。HPと火力を同時に最大化）<br>
<strong>持ち物:</strong> たべのこし（52.8%）/ オボンのみ（29.8%）
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

いじっぱりでこうげきを最大化し、ビルドアップで積みながらドレインパンチで回復する自己完結した型です。ノーマル・かくとう技を無効化する対面でビルドアップを積み始め、ドレインパンチで場持ちを維持しながら全抜きを狙います。まけんき個体では、相手がいかくを使うほどこうげきが2段階上がるため、いかく持ちポケモンが繰り出してきたターンを積みの起点にできます。ちょうはつは相手の回復技や変化技を3ターン封じ、積んだ後の場持ちをさらに高めます。たべのこし（52.8%）は毎ターンの継続回復でドレインパンチと合わせた回復量を底上げし、長期戦での生存率を上げます。

**弱み:**

ようき型と比べてすばやさに振らないため、S90超の相手（カイリュー・リザードン等）に先手を取られます。ビルドアップを積む前のぼうぎょ80は高くなく、上から弱点技（ひこう・フェアリー等）を受けると積みの隙を作れません。また、ふんどのこぶしはHP満タン状態での1発目は威力35と低く、積む前に動ける場面を見極める必要があります。

---

### 型2: ようき先手確保型（2番目に多い構成）

**性格採用率: ようき 34.8%**（素早さ確保の積み型。EV最多分布 H32-S32 7.6%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0979-00.webp" alt="コノヨザル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HSようき先手型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> まけんき（55.3%）/ やるき（39.3%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H32 S32（採用率7.6%。HPと素早さを同時に最大化）<br>
<strong>持ち物:</strong> たべのこし / オボンのみ
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

いじっぱり型ではS90の同速になるS90ポケモン（クレセリア・マリルリ等）に対して先手を取るための確率が50%止まりになるのに対し、ようき型はS実数値を引き上げることでS90帯との同速関係を解消できます。また、ステルスロック（19.4%）との組み合わせでは、相手の交代をより安全に誘えるため、ステロの展開役としての動きも取りやすくなります。やるき個体ではねむり技を完全無効化し、催眠展開から守れます。

**弱み:**

こうげきを最大化するいじっぱり型と比べてA実数値が低くなり、同じビルドアップ1積み後でも火力が劣ります。先手を取ることを優先するぶん、一撃で落とせる範囲が狭くなる点は積み回数で補う必要があります。

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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のインファイト（かくとう）はゴーストタイプで無効化できる。ただしメガ後のS値が高く、こちらが先手を取りにくい。バレットパンチ（はがね）は等倍で通り継続的に削られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー）が×2弱点で刺さる。こちらのふんどのこぶし・ドレインパンチはアシレーヌには等倍止まりで削りが追いつかない</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）・げきりん（ドラゴン）はいずれも等倍で通り、S102でこちらより速い。ただしいかく持ち個体ではまけんきが発動してA+2になるため、積みの起点に転じられる場合がある</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプを持ち、こちらの弱点を突くブレイブバード（ひこう×2）を繰り出せる。S100でこちら（S90）より速く先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・こおり技を持つアタッカーで削ってから出す。いわタイプの打点でカイリューに弱点を突ける枠を同伴する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技（ムーンフォース）が×2弱点。高いとくぼうを持ちドレインパンチの回復でも対応しきれない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技を持つアタッカー（ブリジュラス等）を後続に置き、アシレーヌに弱点を突く枠で対処する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123と高速でこちら（S90）より大きく速い。ゴースト技（シャドークロー等）を採用している個体には×2弱点で先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積む前に消耗させるか、ひこう・フェアリー技を持つポケモンでマスカーニャを処理してから展開する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0935-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハバタクカミ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー/ゴースト複合でこちらの弱点を2タイプで突ける。ムーンフォース（フェアリー×2）・シャドーボール（ゴースト×2）のどちらも×2弱点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どく技を持つ枠でハバタクカミのフェアリー技を受けてから対処する。コノヨザルを直接当てるのは避ける</td>
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
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。コノヨザルが苦手なひこう・フェアリー弱点をサポートするアタッカーを添えるパターン</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき・ドラゴン・はがねの広い打点。アシレーヌ（みず）・ギャラドスへでんき技で弱点を突ける補完枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうタイプでじめん無効。フェアリー耐性はないが、コノヨザルが処理しにくいくさ・はがね系を炎技で崩せる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーで物理受け補完。コノヨザルが苦手なひこう系への後出し交代先として機能</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー">
    <div class="name">カイリュー</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久ひこうタイプ。コノヨザルが無効にできないエスパー・フェアリー系を別枠でケア</div>
  </div>
</div>

**パーティ構成の基本方針:**

コノヨザルはビルドアップ＋ドレインパンチで自己完結した全抜き構成を取れる一方、弱点のひこう・エスパー・ゴースト・フェアリーをパーティ単位でカバーする必要があります。残り5体で以下を補います。

1. **ひこう対策**: いわ・でんき技を持つ枠でコノヨザルが苦手なひこうタイプ（カイリュー・リザードン）に打点を入れる
2. **フェアリー対策**: はがね・どく技を持つアタッカーでアシレーヌ・ハバタクカミへの打点を用意する
3. **高速枠との速度差補完**: S90超の高速ポケモンに対してコノヨザルより先に削れるアタッカーを添える
4. **まけんき連携**: いかく持ちが多い環境では、コノヨザルを先発に置いて積みの起点を作り、後続の全抜きにつなぐ

---

## データ分析①：ふんどのこぶし98.7%が示す「受けてから崩す」設計

コノヨザルの技採用率を並べると、ふんどのこぶし（98.7%）の採用率が突出しています。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| ふんどのこぶし | 攻撃 | 98.7% | 受けるほど威力が上がるメイン技 |
| ドレインパンチ | 攻撃 | 89.4% | 回復しながら削るサブ技 |
| ビルドアップ | 変化 | 75.9% | A・B同時積み |
| ちょうはつ | 変化 | 61.1% | 相手の変化技封じ |
| ステルスロック | 変化 | 19.4% | 設置技 |

ふんどのこぶしとドレインパンチの両採用率がともに89%超であることは、「受けてHP減少→ふんどのこぶしの威力増加→ドレインパンチで回復」というサイクルが構成の核心であることを示しています。ビルドアップ75.9%と合わせると、**受け出し→積み→回復の自己完結ループが主流型の設計思想**であることが採用率から読み取れます。

一方、ちょうはつ61.1%の採用は注目に値します。コノヨザルは積んだ後の突破が難しいため、相手が回復技や積み返し技でカウンターしてくることを想定しており、ちょうはつで3ターン変化技を封じることで積みの安全圏を確保しようとしています。

持ち物はたべのこし52.8%・オボンのみ29.8%が合わせて82.6%を占め、回復実の運用が主流です。攻撃的な持ち物（きあいのタスキ4.4%）の採用率はごくわずかで、**長期戦・持久戦を前提とした耐久運用**が実態に即しています。遭遇時はまず回復実を持つ積み型を疑い、ふんどのこぶし・ビルドアップ・ドレインパンチ・ちょうはつの4技構成を前提に対策を立てるのが確率的に妥当です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 40.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふんどのこぶし・ドレインパンチ・ビルドアップ・ちょうはつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こうげきを最大化し積み後の一撃が重い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S90超の相手に先手を取られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HSようき先手型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 34.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふんどのこぶし・ドレインパンチ・ビルドアップ・ちょうはつ/ステルスロック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S90帯との同速を解消し先手圏を広げられる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型より積み後の火力が劣る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

コノヨザルはかくとう/ゴーストという唯一のタイプ複合でノーマル・かくとうを無効化し、ビルドアップ＋ドレインパンチ＋たべのこしによる自己完結した積み全抜き構成が主流です。まけんき（55.3%）によりいかく等の能力低下を逆用できる点が戦略の幅を広げており、ふんどのこぶし（98.7%）の採用率の高さは「受けてから崩す」設計の徹底を示しています。

弱点はひこう・エスパー・ゴースト・フェアリーの4タイプで、特にフェアリー技を持つアシレーヌや高速ゴーストタイプとの対面は不利です。積む隙を与えられるかどうかが使用判断の軸となるため、パーティではコノヨザルが苦手とするひこう・フェアリー枠を別途カバーする枠を用意することが前提となります。

---

## 関連記事

- [使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [コノヨザルが苦手なアシレーヌのM-3考察](/blog/primarina-analysis-m3/)
- [でんき技でアシレーヌに打点を持つブリジュラスのM-3考察](/blog/archaludon-analysis-m3/)
