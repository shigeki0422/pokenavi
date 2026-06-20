---
title: '【ポケモンチャンピオンズ】メガクチート考察 M-3 使用率24位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率24位のメガクチートを徹底分析。ちからもちで実質こうげき210相当、ふいうち98.6%・じゃれつく98.7%の物理2枚看板と、つるぎのまい80.6%の積み型を実データで解説。はがね/フェアリーの弱点2タイプと立ち回りまで紹介します。'
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
      使用率: <strong style="color:#e67e22">24位</strong>　特性（メガ前）: <strong>いかく 97.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガクチートは**使用率24位**を記録。メガ進化後の特性**ちからもち**によりこうげき105が実質2倍相当となり、フェアリー/はがねの広い打点範囲と先制技ふいうちを合わせて物理的な圧力を維持します。

メガ前特性は**いかく**が97.4%と圧倒的で、出しただけで相手のこうげきを1段階下げてからメガ進化するのが基本の立ち回りです。弱点はほのお・じめんの2タイプのみというタイプ相性の良さも、環境での定着を支えています。

---

## なぜ今メガクチートが使用率24位なのか

### 1. ちからもちで実質こうげきが2倍相当

メガ進化後の特性ちからもちは、物理技の威力を2倍にする効果を持ちます。メガ後こうげき種族値105は控えめに見えますが、ちからもちの補正込みで実質210相当の打点が出ます。じゃれつく（威力95）はちからもち込みで実質威力190、アイアンヘッド（威力80）は実質160相当となり、はがね/フェアリーのタイプ一致補正とあわせて非常に高い実火力を発揮します。

### 2. いかく（メガ前）→メガ進化の二段構え

いかく採用率97.4%の事実が示すとおり、メガクチートはまず素のクチートとして登場し、相手のこうげきを1段階下げてからメガ進化するのが基本です。この動きにより、メガ進化後のちからもち火力を押し付けつつ、相手物理アタッカーのダメージを抑えた状態で展開できます。

### 3. はがね/フェアリーで弱点がほのお・じめんの2タイプのみ

はがね/フェアリーの複合タイプはドラゴン・あく・ノーマルを無効化し、むし・くさ・こおり・エスパー・どく・かくとう・ひこう・フェアリー・はがねを半減します。弱点はほのお（×2）・じめん（×2）の2タイプのみで、環境上位の多くの打点を受け流せます。ふいうちで先制打点も確保しており、S50の遅さをある程度補えます。

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

ぼうぎょ125・とくぼう95と守備面が強化されており、先に仕掛けられる展開に耐えながら攻撃できます。一方でHP50・すばやさ50は低く、上から殴られる展開が多いため、ふいうちによる先制打点と組み合わせてS劣勢を補う立ち回りが基本です。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½以下）</th>
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
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル×0.5</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう×0.5</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう×0.5</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ×0.5</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし×0.5</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね×0.5</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ×0.5</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー×0.5</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり×0.5</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー×0.5</span>
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

はがねがどく・ドラゴンを無効化し、フェアリーがあくを無効化します。弱点はほのお・じめんの2タイプのみで、環境上位の多くの打点（かくとう・ドラゴン・あく等）を半減以下に抑えられます。一方、ガブリアス（じしん採用率99.2%）やリザードン・ウルガモスといったほのお枠は明確な天敵であり、パーティ単位でのケアが必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.7%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ふいうち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.6%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">80.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">50.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はたきおとす</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">28.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほのおのキバ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.3%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">11.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かわらわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.8%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>いわなだれ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1.4%</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布はいじっぱり83.6%・ゆうかん14.3%と物理こうげきに寄せた2択構成です。EV振りの最多は**H32-A32-B2（30.5%）**と**H32-A32-D2（20.6%）**で、HPとこうげきを最大化しつつ残り2をぼうぎょまたはとくぼうに振る型が主流です。

### 型1: いじっぱり積みアタッカー型（最多採用）

**性格採用率: いじっぱり 83.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA積みアタッカー型（いじっぱり）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.4%）※メガ後ちからもち<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32 B2（採用率30.5%。余りBまたはD2）<br>
<strong>持ち物:</strong> クチートナイト（99.8%）
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

いじっぱり補正でこうげき実数値をさらに高め、つるぎのまい後のちからもち込み打点は耐久型のポケモンも一撃圏内に入れられます。ふいうちで優先度+1の先制打点を持つため、S50の遅さを補いながらHP満タン付近の高速アタッカーにもダメージを与えられます。つるぎのまいを積む隙が確保できる場面（いかくで弱体化した物理アタッカー対面など）でそのまま爆発的な火力を出せるのが最大の強みです。

**弱み:**

S50で大半のポケモンに先手を取られるため、ふいうちを読まれて攻撃技ではなく変化技を使われると先制技が不発に終わります。ほのお・じめんの弱点を突かれると耐久が追いつかず、特にガブリアスのじしんは先に動かれて大ダメージを受けます。

---

### 型2: ゆうかん耐久寄り型（2番目に多い構成）

**性格採用率: ゆうかん 14.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA物理型（ゆうかん）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.4%）※メガ後ちからもち<br>
<strong>性格:</strong> ゆうかん（A↑ S↓）<br>
<strong>EV:</strong> H32 A32 D2（採用率20.6%）<br>
<strong>持ち物:</strong> クチートナイト（99.8%）
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

ゆうかんはSを下げる代わりにAを上げる性格で、S50がさらに低くなる代わりにこうげき実数値がいじっぱりと同水準になります。先手を取ることを最初から放棄し、ふいうちで先制するかトリックルームとの組み合わせを前提とした型です。いじっぱり型と比べてSが落ちる分、トリックルーム下では動きやすくなります。

**弱み:**

いじっぱり型と比べてSがさらに低くなるため、通常の対面ではより多くの場面で後攻になります。ゆうかんを選ぶ意義はトリックルーム前提の構成か、S実数値を調整して特定のポケモンを下回る逆張り採用に限られます。トリックルームなしの通常対戦では、いじっぱりとの明確な差が出しにくい構成です。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

はがね/フェアリーの弱点がほのお・じめんの2タイプのみという耐性の広さにより、多くの上位ポケモンの主力技を半減以下に抑えられます。一方、S50で先手をほぼ取れないため、弱点を突く高速枠との対面は先にダメージを受ける前提になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくがドラゴン×2。カイリューのドラゴン技はこちらに無効。カイリューのじしん採用率が低ければじめん弱点も突かれにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくはルカリオ（はがね/かくとう）にフェアリー×はがね0.5×かくとう0.5＝×0.25と抜群にならない。インファイトはこちらにかくとう×はがね0.5×フェアリー0.5＝×0.25で通りが悪い。お互いの主力が半減以下になる対面</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくがドドゲザン（はがね/あく）にフェアリー×あく2×はがね0.5＝等倍。アイアンヘッドははがね×はがね0.5×あく1＝×0.5。ちからもちアイアンヘッドでも大ダメージは期待しにくいが、じゃれつくなら等倍で入る。ドドゲザンのふいうち（あく）はこちらには等倍で通る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.2%でじめん×2を先手で受ける。S102でこちらより速く、先手を取られる。じゃれつくはドラゴン×2×じめん0.5＝等倍に留まる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がこちらに×2。S100でこちらより速く先手で弱点を突かれる。じゃれつくは×0.5で通りが悪い</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.2%でじめん×2を上から受ける。S102でこちらより速く、積む前に先手で大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプ（ギャラドス等）でじしんを無効化する枠を同伴。クチートを出す前にガブリアスを削るか流す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がこちらに×2。S100で先手を取られ、かえんほうしゃ等で先手から大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ技を持つ枠でリザードンを先に処理してからメガクチートを展開する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率98.0%でじめん×2を上から受ける。高HP・高Bでこちらの打点が通りにくく、あくびで流される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技の高速枠でカバルドンに弱点を突く。あくび展開前に積み技を通さない</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">推奨同伴枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう複合でガブリアス・カバルドンのじしんを無効化。メガクチートの最大の弱点じめんをカバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">推奨同伴枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじめんを無効化。メガクチートが苦手なほのお枠の対面はリザードンで先に対処</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">推奨同伴枠</div>
    <div style="font-size:0.65rem;code:#888;margin-top:2px">高速地面枠。メガクチートが苦手なほのお・じめん枠に先制で打点を入れて削りを蓄積</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">推奨同伴枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みずでほのお・じめんの両弱点に打点を持つ。メガクチートの2つの弱点タイプをまとめてケアできる特殊枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガクチートはほのお・じめんの2タイプが弱点で、いずれもガブリアスやリザードン等の環境上位が採用する主力技です。残り5体で以下をカバーします。

1. **じめん対策**: ひこうタイプ（ギャラドス・リザードン・カイリュー）でじしんを無効化する枠
2. **ほのお対策**: みずタイプ（アシレーヌ等）でほのお技の打点元を処理する枠
3. **先手確保**: メガクチートはS50でほぼ後攻のため、高速アタッカーで先に相手を削ってからクチートを通す流れが基本
4. **いかくシナジー**: メガ前いかくで相手物理を弱体化するため、同じく物理アタッカーが多い構成と相性が良い

---

## データ分析①：ふいうちとつるぎのまいの高採用率が示す「先制＋積み」の二択戦術

メガクチートの技採用率をみると、ふいうち98.6%・つるぎのまい80.6%という2つの技が高採用率を保っています。

| 技 | 採用率 | 役割 |
|---|---|---|
| じゃれつく | 98.7% | タイプ一致フェアリー主力 |
| ふいうち | 98.6% | 優先度+1先制打点 |
| つるぎのまい | 80.6% | こうげき2段階上昇 |
| アイアンヘッド | 50.0% | タイプ一致はがね補完 |
| はたきおとす | 28.3% | 持ち物剥奪 |

注目すべきは**ふいうちとつるぎのまいがほぼ全員が採用している**点です。ふいうちは「今すぐ先制で削る」技であり、つるぎのまいは「1ターン積んで後から大火力を出す」技です。この2択を状況に応じて使い分けるのがメガクチートの基本戦術で、ふいうちで先制しつつ、相手が変化技を使ってくる場面にはつるぎのまいを差し込む読み合いが生まれます。

アイアンヘッドの採用率が50.0%に留まる点も示唆的です。4技目の枠は**アイアンヘッド（50.0%）かはたきおとす（28.3%）**で、残り約20%は別の技を採用していることが読み取れます。アイアンヘッドが半数にとどまる背景には、じゃれつくとふいうちで既にフェアリー・あくの2打点を確保しており、はがね技よりも持ち物剥奪（はたきおとす）を優先するプレイヤーが一定数いることがあります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 83.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じゃれつく・ふいうち・つるぎのまい・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の打点が高くふいうちで先制も取れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうちを読まれると先制が不発になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HA物理型（ゆうかん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん 14.3%</td>
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

S50という致命的な遅さを抱えており、ほのお・じめんの弱点を持つ2タイプは環境上位の主力技と重なります。パーティ単位でひこう枠・みず枠を添え、ガブリアス・リザードンへの対策を確保した上でメガクチートを展開するのが実戦での基本構成です。

---

## 関連記事

- [メガクチートの弱点じめんを持つ使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [ほのお弱点を突かれるリザードンのM-3考察](/blog/charizard-analysis-m3/)
- [ドラゴン無効でじゃれつくが刺さるカイリューのM-3考察](/blog/dragonite-analysis-m3/)
