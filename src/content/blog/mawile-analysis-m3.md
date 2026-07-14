---
title: '【ポケモンチャンピオンズ】メガクチート考察 M-3 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率25位のメガクチートを徹底分析。ちからもちでA実数値172が実効2倍相当、ふいうち98.8%・じゃれつく98.8%の物理2枚看板と、つるぎのまい87.2%の積み型を実データで解説。はがね/フェアリーの弱点2タイプと立ち回りまで紹介します。'
updatedDate: '2026-06-26'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-mawile-m3.png'
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
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" />
  <div>
    <h2 style="margin:0 0 8px">メガクチート</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">25位</strong>　特性（メガ前）: <strong>いかく 96.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

シーズンM-3のシングルバトルで、メガクチートは**使用率25位**を記録。メガ進化後の特性**ちからもち**によりこうげき105（いじっぱりA32でA実数値172）が実効2倍相当となり、フェアリー/はがねの広い打点範囲と先制技ふいうちを合わせて物理的な圧力を維持します。

メガ前特性は**いかく**が96.9%と圧倒的で、出しただけで相手のこうげきを1段階下げてからメガ進化するのが基本の立ち回りです。弱点はほのお・じめんの2タイプのみというタイプ相性の良さも、環境での定着を支えています。

---

## なぜ今メガクチートが使用率25位なのか

### 1. ちからもちで実質こうげきが2倍相当

メガ進化後の特性ちからもちは、物理技の威力を2倍にする効果を持ちます。メガ後こうげき種族値105は控えめに見えますが、いじっぱりA32のA実数値172がちからもち補正でこうげき計算上2倍相当として働きます。じゃれつく（威力90）はちからもち込みで実質威力180、アイアンヘッド（威力80）は実質160相当となり、はがね/フェアリーのタイプ一致補正とあわせて非常に高い実火力を発揮します。

### 2. いかく（メガ前）→メガ進化の二段構え

いかく採用率96.9%の事実が示すとおり、メガクチートはまず素のクチートとして登場し、相手のこうげきを1段階下げてからメガ進化するのが基本です。この動きにより、メガ進化後のちからもち火力を押し付けつつ、相手物理アタッカーのダメージを抑えた状態で展開できます。

### 3. はがね/フェアリーで弱点がほのお・じめんの2タイプのみ

はがね/フェアリーの複合タイプはどく・ドラゴンを無効化し、ノーマル・くさ・こおり・エスパー・ひこう・いわ・あく・フェアリーを半減、むしを¼まで軽減します。弱点はほのお（×2）・じめん（×2）の2タイプのみで、環境上位の多くの打点を受け流せます。S実数値102（いじっぱりS無振り）と低速のため環境上位の大半に後攻となりますが、優先度+1のふいうちで先制打点を確保し、耐性で攻撃を受けてからつるぎのまいで積む立ち回りで速度の遅さを補います。

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

ぼうぎょ125・とくぼう95と守備面が強化されており、先に仕掛けられる展開に耐えながら攻撃できます。一方でHP50・すばやさ50（いじっぱりS無振りでS実数値102）は控えめで、ガブリアス（S実数値169）など環境上位の高速枠には上から殴られるため、ふいうちによる先制打点と組み合わせてS劣勢を補う立ち回りが基本です。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（¼）</th>
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
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

はがねがどくを、フェアリーがドラゴンを無効化します。弱点はほのお・じめんの2タイプのみで、あく等の打点を半減以下に抑えられます。一方、ガブリアス（じしん採用率99.5%）やリザードンといったほのお・じめん枠は明確な天敵であり、パーティ単位でのケアが必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">98.8%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">87.2%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>アイアンヘッド</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">32.2%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ほのおのキバ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">26.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はたきおとす</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">22.5%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かみなりパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">20.4%</td>
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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2.2%</td>
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

性格分布はいじっぱり85.8%・ゆうかん12.0%と物理こうげきに寄せた2択構成です。EV振りの最多は**H32-A32-B2（29.6%）**と**H32-A32-D2（15.9%）**で、HPとこうげきを最大化しつつ残り2をぼうぎょまたはとくぼうに振る型が主流です。

### 型1: いじっぱり積みアタッカー型（最多採用）

**性格採用率: いじっぱり 85.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA積みアタッカー型（いじっぱり）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（96.9%）※メガ後ちからもち<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32 B2（採用率29.6%。余りBまたはD2）<br>
<strong>持ち物:</strong> クチートナイト（99.6%）
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

ゆうかん型と同じA実数値172を確保しつつ、S下降補正を受けない分S実数値102を保てる（ゆうかん型はS実数値91）のがこの型の差です。S実数値102は元から低速で環境上位の高速枠には届きませんが、ゆうかん型より7高い分、通常構成ではゆうかん型より後攻になる場面が減ります。トリックルームに依存しない標準的なパーティで運用する場合はこちらが基準型になります。

**弱み:**

S実数値102はメガクチートを採用する以上どの型でも低速で、トリックルーム下ではゆうかん型（S実数値91）の方が先に動けるため、トリル軸に組み込むならゆうかん型に分がある点がこの型固有の弱みです。通常構成での速度はあくまでゆうかん型との相対差（7）にとどまり、環境上位の高速アタッカーへの後攻は変わりません。

---

### 型2: ゆうかん耐久寄り型（2番目に多い構成）

**性格採用率: ゆうかん 12.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0303-00.webp" alt="メガクチート" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA物理型（ゆうかん）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（96.9%）※メガ後ちからもち<br>
<strong>性格:</strong> ゆうかん（A↑ S↓）<br>
<strong>EV:</strong> H32 A32 D2（採用率15.9%）<br>
<strong>持ち物:</strong> クチートナイト（99.6%）
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

ゆうかんはSを下げる代わりにAを上げる性格で、S実数値が91まで落ちる代わりにこうげき実数値172をいじっぱりと同水準で確保できます。先手を取ることを最初から放棄し、ふいうちで先制するかトリックルームとの組み合わせを前提とした型です。いじっぱり型（S実数値102）と比べてSが7低い分、トリックルーム下では先に動きやすくなります。

**弱み:**

いじっぱり型（S実数値102）と比べてSが7低い実数値91となるため、トリックルームなしの通常対面ではより多くの場面で後攻になります。ゆうかんを選ぶ意義はトリックルーム前提の構成に限られ、通常対戦ではいじっぱりより後攻機会が増える分だけ不利になります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

はがね/フェアリーの弱点がほのお・じめんの2タイプのみという耐性の広さにより、多くの上位ポケモンの主力技を半減以下に抑えられます。一方、S実数値102（いじっぱりS無振り）は環境上位の高速枠（ガブリアスS実数値169・メガルカリオS実数値180等）に大きく届かず、弱点を突く高速枠との対面は先にダメージを受ける前提になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつくがドラゴンに×2で抜群。カイリューのドラゴン技はこちらに無効。ただしかえんほうしゃ31.2%（ほのお×2弱点）・じしん21.6%（じめん×2弱点）を持つ個体には弱点を突かれるため過信は禁物</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.5%でじめん×2を先手で受ける。ガブリアスのS実数値169はクチート（S実数値102）より速く先手を取られる。じゃれつくはガブリアスに×2で入るが、先に動けず積む前に倒される</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.5%でじめん×2を上から受ける。S実数値169でこちらより速く、積む前に先手で大ダメージを受ける</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率97.9%でじめん×2を上から受ける。高HP・高Bでこちらの打点が通りにくく、あくびで流される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技の高速枠でカバルドンに弱点を突く。あくび展開前に積み技を通さない</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

同居率上位はミミッキュ（1位）・ガブリアス（2位）ですが、ガブリアスはじめん技を主力とし役割が重複するため、ここではクチートの弱点であるじめん・ほのおを補完できる同居率3位以下の枠を選んで紹介します。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう複合でガブリアス・カバルドンのじしんを無効化。メガクチートの最大の弱点じめんをカバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム">
    <div class="name">ウォッシュロトム</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/でんきでほのお技を半減し、みず打点でほのお枠を処理。クチートの苦手なほのお対面を受けられる枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速枠で先に相手を削り、S実数値102のクチートが上から殴られる相手を事前に処理して通りやすい盤面を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル">
    <div class="name">キラフロル</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊高火力枠でクチートの物理と打点を分散。どくびし設置で受け回しを崩しクチートの全抜きを後押し</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガクチートはほのお・じめんの2タイプが弱点で、いずれもガブリアスやリザードン等の環境上位が採用する主力技です。残り5体で以下をカバーします。

1. **じめん対策**: ひこうタイプ（ギャラドス等）でじしんを無効化する枠
2. **ほのお対策**: みずタイプ（ウォッシュロトム等）でほのお技を半減し打点元を処理する枠
3. **先手確保**: メガクチートはS実数値102で環境上位の高速枠には後攻になるため、高速アタッカーで先に相手を削ってからクチートを通す流れが基本
4. **いかくシナジー**: メガ前いかくで相手物理を弱体化するため、同じく物理アタッカーが多い構成と相性が良い

---

## データ分析①：確定3技（ふいうち・じゃれつく・つるぎのまい）と4技目の分散から読むクチートの構築思想

メガクチートの技採用率を見ると、ふいうち98.8%・じゃれつく98.8%・つるぎのまい87.2%の3技がほぼ確定採用で、4技目のみが構築によって分散しています。

| 技 | 採用率 | 役割 |
|---|---|---|
| ふいうち | 98.8% | 優先度+1先制打点 |
| じゃれつく | 98.8% | タイプ一致フェアリー主力 |
| つるぎのまい | 87.2% | こうげき2段階上昇 |
| アイアンヘッド | 32.2% | タイプ一致はがね補完 |
| ほのおのキバ | 26.1% | はがね・くさへの打点 |
| はたきおとす | 22.5% | 持ち物剥奪 |
| かみなりパンチ | 20.4% | みず・ひこう複合への打点 |

**確定3技それぞれの役割**

- **ふいうち（98.8%）**：S102で環境の高速枠に後攻になる場面でも、優先度+1で先制打点を取れます。積み前の削りと削れた相手への詰めを両立します。
- **じゃれつく（98.8%）**：タイプ一致フェアリー技として最高威力のメインウェポンです。積み後の打点元であり、ドラゴン・あくタイプへの通りも良いです。
- **つるぎのまい（87.2%）**：A1段階上昇で耐性受けに来た相手も崩せます。耐久型のパーティが「受けで止める」前提を崩す積み技として、スピードより圧力が求められる場面で機能します。

**4技目の分散が示す構築ごとの補完**

3技でフェアリー・あく・積みの軸は固定されており、4技目のみが採用者のパーティの穴に応じて選ばれています。アイアンヘッド（32.2%）はフェアリー耐性を持つはがねタイプへの打点確保、ほのおのキバ（26.1%）は主にはがね・くさへの補完、はたきおとす（22.5%）はオボンのみ・こだわりスカーフ等の持ち物を剥奪して積みを通しやすくする役割、かみなりパンチ（20.4%）はみず・ひこう複合への打点として選ばれています。最多のアイアンヘッドでも32.2%と採用者の3分の1未満であり、どれが「正解」ということはなく、パーティ単位の補完が分散を生んでいます。

自分のパーティでアイアンヘッド・ほのおのキバ・はたきおとす・かみなりパンチのうちどれを選ぶかは、残り5体が誰を苦手としているかで決まります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 85.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じゃれつく・ふいうち・つるぎのまい・アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の打点が高くふいうちで先制も取れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうちを読まれると先制が不発になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HA物理型（ゆうかん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆうかん 12.0%</td>
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

S実数値102（いじっぱりS無振り）で環境上位の高速枠（ガブリアスS実数値169・メガリザードンYS実数値167等）には後れを取り、ほのお・じめんの弱点を持つ2タイプは環境上位の主力技と重なります。パーティ単位でひこう枠・みず枠を添え、ガブリアス・リザードンへの対策を確保した上でメガクチートを展開するのが実戦での基本構成です。

---

## 関連記事

- [メガムクホークのM-3考察 使用率と立ち回り](/blog/staraptor-analysis-m3/)
- [メガバシャーモのM-3考察 ほのお/かくとうの型別解説](/blog/blaziken-analysis-m3/)
- [メガメタグロスのM-3考察 はがね枠の採用率と立ち回り](/blog/metagross-analysis-m3/)
