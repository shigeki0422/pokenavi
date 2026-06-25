---
title: '【ポケモンチャンピオンズ】メガクチート考察 M-3 使用率25位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率25位のメガクチートを徹底分析。ちからもちでA実数値172が実効2倍相当、ふいうち98.9%・じゃれつく98.7%の物理2枚看板と、つるぎのまい85.3%の積み型を実データで解説。はがね/フェアリーの弱点2タイプと立ち回りまで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-mawile-m3.png'
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
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" />
  <div>
    <h2 style="margin:0 0 8px">メガクチート</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">25位</strong>　特性（メガ前）: <strong>いかく 97.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガクチートは**使用率25位**を記録。メガ進化後の特性**ちからもち**によりこうげき105（いじっぱりA32でA実数値172）が実効2倍相当となり、フェアリー/はがねの広い打点範囲と先制技ふいうちを合わせて物理的な圧力を維持します。

メガ前特性は**いかく**が97.2%と圧倒的で、出しただけで相手のこうげきを1段階下げてからメガ進化するのが基本の立ち回りです。弱点はほのお・じめんの2タイプのみというタイプ相性の良さも、環境での定着を支えています。

---

## なぜ今メガクチートが使用率25位なのか

### 1. ちからもちで実質こうげきが2倍相当

メガ進化後の特性ちからもちは、物理技の威力を2倍にする効果を持ちます。メガ後こうげき種族値105は控えめに見えますが、いじっぱりA32のA実数値172がちからもち補正でこうげき計算上2倍相当として働きます。じゃれつく（威力90）はちからもち込みで実質威力180、アイアンヘッド（威力80）は実質160相当となり、はがね/フェアリーのタイプ一致補正とあわせて非常に高い実火力を発揮します。

### 2. いかく（メガ前）→メガ進化の二段構え

いかく採用率97.2%の事実が示すとおり、メガクチートはまず素のクチートとして登場し、相手のこうげきを1段階下げてからメガ進化するのが基本です。この動きにより、メガ進化後のちからもち火力を押し付けつつ、相手物理アタッカーのダメージを抑えた状態で展開できます。

### 3. はがね/フェアリーで弱点がほのお・じめんの2タイプのみ

はがね/フェアリーの複合タイプはどく・ドラゴン・あくを無効化し、ノーマル・くさ・こおり・エスパー・ひこう・いわ・フェアリー・むしを半減以下にします。弱点はほのお（×2）・じめん（×2）の2タイプのみで、環境上位の多くの打点を受け流せます。ふいうちで先制打点も確保しており、メガ後S実数値102（いじっぱり無振り）でも環境上位の高速枠には後れを取る速度をある程度補えます。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">105</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">125</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">95</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">480</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

ぼうぎょ125・とくぼう95と守備面が強化されており、先に仕掛けられる展開に耐えながら攻撃できます。一方でHP50・すばやさ50（いじっぱり無振りS実数値102）は控えめで、ガブリアス（S実数値169）など環境上位の高速枠には上から殴られるため、ふいうちによる先制打点と組み合わせてS劣勢を補う立ち回りが基本です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

はがねがどく・ドラゴンを無効化し、フェアリーがあくを無効化します。弱点はほのお・じめんの2タイプのみで、ドラゴン・あく等の打点を半減以下に抑えられます。一方、ガブリアス（じしん採用率99.6%）やリザードンといったほのお・じめん枠は明確な天敵であり、パーティ単位でのケアが必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ふいうち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.7%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">85.3%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">38.1%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はたきおとす</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">27.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほのおのキバ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">24.7%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">12.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かわらわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.0%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>サイコファング</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2.0%</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布はいじっぱり85.9%・ゆうかん11.9%と物理こうげきに寄せた2択構成です。EV振りの最多は**H32-A32-B2（30.9%）**と**H32-A32-D2（17.3%）**で、HPとこうげきを最大化しつつ残り2をぼうぎょまたはとくぼうに振る型が主流です。

### 型1: いじっぱり積みアタッカー型（最多採用）

**性格採用率: いじっぱり 85.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA積みアタッカー型（いじっぱり）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.2%）※メガ後ちからもち<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32 B2（採用率30.9%。余りBまたはD2）<br>
<strong>持ち物:</strong> クチートナイト（99.7%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく<br>
・ふいうち<br>
・つるぎのまい<br>
・アイアンヘッド / はたきおとす
</div>
</div>
</div>

**強み:**

ゆうかん型と同じA実数値172を確保しつつ、S下降補正を受けない分メガ後S実数値102を保てる（ゆうかん型はS実数値91）のがこの型の差です。S実数値102は無メガリザードン（S100→実数値120）やガブリアス（S102→実数値169）には届かないものの、ゆうかん型より11高い分、両者の中間に位置する中速帯（実数値91〜102の相手）には先に動ける場面が生まれます。トリックルームに依存しない通常構成で採用でき、トリックルーム軸を組まない標準的なパーティで運用する場合はこちらが基準型になります。

**弱み:**

ゆうかん型より速い分、トリックルーム下では逆に先に動けず、トリル軸に組み込むならゆうかん型に分がある点が弱みです。S実数値102でも環境上位の高速アタッカーには届かず、通常構成での速度的優位はゆうかん型との相対差（実数値91〜102の中速帯）にとどまります。

---

### 型2: ゆうかん耐久寄り型（2番目に多い構成）

**性格採用率: ゆうかん 11.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA物理型（ゆうかん）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.2%）※メガ後ちからもち<br>
<strong>性格:</strong> ゆうかん（A↑ S↓）<br>
<strong>EV:</strong> H32 A32 D2（採用率17.3%）<br>
<strong>持ち物:</strong> クチートナイト（99.7%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく<br>
・ふいうち<br>
・つるぎのまい<br>
・アイアンヘッド / はたきおとす
</div>
</div>
</div>

**強み:**

ゆうかんはSを下げる代わりにAを上げる性格で、S実数値が91まで落ちる代わりにこうげき実数値172をいじっぱりと同水準で確保できます。先手を取ることを最初から放棄し、ふいうちで先制するかトリックルームとの組み合わせを前提とした型です。いじっぱり型（S実数値102）と比べてSが11低い分、トリックルーム下では先に動きやすくなります。

**弱み:**

いじっぱり型（S実数値102）と比べてSが11低い実数値91となるため、通常の対面ではより多くの場面で後攻になります。ゆうかんを選ぶ意義はトリックルーム前提の構成に限られ、トリックルームなしの通常対戦では、いじっぱりより後攻機会が増える分だけ不利になります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

はがね/フェアリーの弱点がほのお・じめんの2タイプのみという耐性の広さにより、多くの上位ポケモンの主力技を半減以下に抑えられます。一方、メガ後S実数値102（いじっぱり無振り）は環境上位の高速枠（ガブリアスS実数値169・メガルカリオS実数値180等）に届かず、弱点を突く高速枠との対面は先にダメージを受ける前提になります。

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
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくがドラゴンに×2で抜群。カイリューのドラゴン技はこちらに無効。ただしじしん採用率21.7%の個体にはじめん弱点を突かれるため過信は禁物</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガルカリオはようきS32でS実数値180とクチート（S実数値102）より大幅に速く、かくとう技を先制で押し込める。じゃれつくはルカリオ（はがね/かくとう）に等倍止まりで、ふいうち（あく）は半減され先制打点も通りにくい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくはドドゲザン（はがね/あく）に等倍で入る。アイアンヘッドは×0.5で通りが悪い。ドドゲザンのふいうち（あく）はフェアリーで半減され通りが悪く、こちらのじゃれつくが一方的に刺さる対面</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.6%でじめん×2を先手で受ける。ガブリアスのS実数値169はクチート（S実数値102）より速く先手を取られる。じゃれつくはガブリアスに×2で入るが、先に動けず積む前に倒される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がこちらに×2。メガリザードンY（おくびょうでメガ後S実数値167）はクチート（S実数値102）より大幅に速く、先手で弱点を突かれる。じゃれつくは×0.5で通りが悪い</td>
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
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.6%でじめん×2を上から受ける。S実数値169でこちらより速く、積む前に先手で大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプ（ギャラドス等）でじしんを無効化する枠を同伴。クチートを出す前にガブリアスを削るか流す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がこちらに×2。メガリザードンY（おくびょうでメガ後S実数値167）に先手を取られ、かえんほうしゃ等で大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ技を持つ枠でリザードンを先に処理してからメガクチートを展開する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率98.1%でじめん×2を上から受ける。高HP・高Bでこちらの打点が通りにくく、あくびで流される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技の高速枠でカバルドンに弱点を突く。あくび展開前に積み技を通さない</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

同居率上位はミミッキュ（1位）・ガブリアス（2位）・カバルドン（3位）ですが、上位3体はじめん技を主力とする（ガブリアス・カバルドン）か役割が重複するため、ここではクチートの弱点であるじめん・ほのおを補完できる同居率4位以下の枠を選んで紹介します。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう複合でガブリアス・カバルドンのじしんを無効化。メガクチートの最大の弱点じめんをカバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">ラグラージ</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/じめんでほのお技を半減し、みず打点でほのお枠を処理。クチートの苦手なほのお対面を受けられる枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速枠で先に相手を削り、S実数値102のクチートが上から殴られる相手を事前に処理して通りやすい盤面を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル">
    <div class="name">キラフロル</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊高火力枠でクチートの物理と打点を分散。どくびし設置で受け回しを崩しクチートの全抜きを後押し</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガクチートはほのお・じめんの2タイプが弱点で、いずれもガブリアスやリザードン等の環境上位が採用する主力技です。残り5体で以下をカバーします。

1. **じめん対策**: ひこうタイプ（ギャラドス等）でじしんを無効化する枠
2. **ほのお対策**: みずタイプ（ラグラージ等）でほのお技を半減し打点元を処理する枠
3. **先手確保**: メガクチートはメガ後S実数値102で環境上位の高速枠には後攻になるため、高速アタッカーで先に相手を削ってからクチートを通す流れが基本
4. **いかくシナジー**: メガ前いかくで相手物理を弱体化するため、同じく物理アタッカーが多い構成と相性が良い

---

## データ分析①：ふいうちとつるぎのまいの高採用率が示す「先制＋積み」の二択戦術

メガクチートの技採用率をみると、ふいうち98.9%・つるぎのまい85.3%という2つの技が高採用率を保っています。

| 技 | 採用率 | 役割 |
|---|---|---|
| ふいうち | 98.9% | 優先度+1先制打点 |
| じゃれつく | 98.7% | タイプ一致フェアリー主力 |
| つるぎのまい | 85.3% | こうげき2段階上昇 |
| アイアンヘッド | 38.1% | タイプ一致はがね補完 |
| はたきおとす | 27.4% | 持ち物剥奪 |

つるぎのまい85.3%という高採用率は、環境上位の高速枠に先手を取れないクチートが「1ターン耐えて積む」前提で運用されていることを示します。いじっぱりA32のA実数値は172で、ちからもち補正によりこうげき計算上は実効2倍相当、つるぎのまい1積み後はさらに2段階上昇でこうげき計算上4倍相当の打点になります。この火力なら、半減のはがね/フェアリー耐性で受けに来た相手すら一致じゃれつくで2発圏に入れられ、積みが通れば耐性受けでは止まらない打点に化けます。つまりつるぎのまいは「速くないから諦める」技ではなく、「耐性で耐えてから積み、受けを正面から崩す」ための主軸であり、85.3%という数字はこの崩しがクチート採用の本質であることを裏づけます。

一方、4技目は割れており最多のアイアンヘッド（38.1%）でも4割に届きません。はたきおとす（27.4%）・ほのおのキバ（24.7%）・かみなりパンチ（12.8%）が続きます。じゃれつく・ふいうちでフェアリー・あくの2打点を確保済みのため、4技目は持ち物剥奪（はたきおとす）や、苦手なはがね/ひこう・みず複合への打点（ほのおのキバ・かみなりパンチ）といった構築ごとの補完役を担い、確定3技に対して4技目だけが構築思想で分散しているのが読み取れます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HA積みアタッカー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 85.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じゃれつく・ふいうち・つるぎのまい・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の打点が高くふいうちで先制も取れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうちを読まれると先制が不発になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HA物理型（ゆうかん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん 11.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じゃれつく・ふいうち・つるぎのまい・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">トリックルーム下での優先展開を狙いやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">通常対面ではSがさらに低くなり後攻機会が増える</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガクチートははがね/フェアリーの弱点2タイプという恵まれたタイプ相性と、ちからもちによる実質2倍火力を武器に、いかく（メガ前）→メガ進化の二段展開で環境に居場所を確保しています。じゃれつく・ふいうちのほぼ全員採用が示すとおり、フェアリー打点と先制打点の両立がこのポケモンの核心です。

メガ後S実数値102（いじっぱり無振り）でも環境上位の高速枠（ガブリアスS実数値169・メガリザードンYS実数値167等）には後れを取り、ほのお・じめんの弱点を持つ2タイプは環境上位の主力技と重なります。パーティ単位でひこう枠・みず枠を添え、ガブリアス・リザードンへの対策を確保した上でメガクチートを展開するのが実戦での基本構成です。

---

## 関連記事

- [メガムクホークのM-3考察 使用率と立ち回り](/blog/staraptor-analysis-m3/)
- [メガバシャーモのM-3考察 ほのお/かくとうの型別解説](/blog/blaziken-analysis-m3/)
- [メガメタグロスのM-3考察 はがね枠の採用率と立ち回り](/blog/metagross-analysis-m3/)
