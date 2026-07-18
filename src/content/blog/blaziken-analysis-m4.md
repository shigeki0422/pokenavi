---
title: '【ポケモンチャンピオンズ】メガバシャーモ 考察 M-4 シーズン かそく加速アタッカーの立ち回り'
description: 'M-4シーズン使用率10位のメガバシャーモを考察。メガ石バシャーモナイト採用率72.9%の物理アタッカー型と、きあいのタスキ採用14.2%の非メガ型を比較し、フレアドライブ・インファイト・かみなりパンチのタイプ相性とダメージ計算をデータで詳しく分析します。'
pubDate: '2026-07-18'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-blaziken-m4.png'
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
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" />
  <div>
    <h2 style="margin:0 0 8px">メガバシャーモ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">10位</strong>（M-4）　持ち物: <strong>バシャーモナイト 72.9%</strong>
    </div>
  </div>
</div>

M-4シーズン、バシャーモは使用率10位につけています。特性かそくでターンが進むごとに素早さが1段階ずつ上がる加速型アタッカーで、いじっぱり性格72.6%・メガ石バシャーモナイト72.9%が主流です。一方できあいのタスキ採用14.2%の非メガ型も一定数存在し、メガ進化枠を他のポケモンに譲る構築で選ばれています。

---

## メガバシャーモの基本スペック

### 種族値（通常→メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:80%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">120</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">530</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげき160・すばやさ100（+20）を含む全ステータスが上昇します。特性はメガ進化前後とも**かそく**で変化しません（メタグロスのように進化で特性そのものが切り替わる仕組みとは異なります）。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
</tr>
</tbody>
</table>
</div>

弱点はひこう・じめん・みず・エスパーの4タイプ（いずれも×2）。無効タイプはありません。環境1位のガブリアス（ドラゴン/じめん）がじしんを99.5%採用、7位のアシレーヌ（みず/フェアリー）がうたかたのアリアを88.2%採用しており、いずれも×2弱点かつ高採用率のため、対面で受け出す運用には向きません。

### 特性

**かそく（98.5%）** はターン終わりに自分の素早さが1段階上がる特性です。場に出た初手は素の種族値のままですが、1ターン生存するごとに実質速度が積み上がっていくため、序盤は上から取れない相手でも数ターン後には上から動けるようになります。控えの**もうか（1.5%）** はHPが1/3以下でほのお技威力1.5倍になる特性ですが、採用はごくわずかです。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フレアドライブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致補正込みのメインウェポン。反動でHP1/3を失う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致補正込みのもう1本のメインウェポン。反動でB・D低下</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきを2段階上昇。フレアドライブ・インファイトの威力を底上げする積み技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシレーヌ・メガリザードンYなどフレアドライブ・インファイトが半減される相手への等倍以上の打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の技を無効化しつつかそくを1段階溜める、様子見・時間稼ぎの1手</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みきり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる同様に相手の技を防ぎつつ急所率上昇。まもると使い分けて連続使用の失敗を回避</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とびひざげり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトより高威力だが外すと反動でHP半分を失う。4枠目の選択技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バトンタッチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまいで上げたこうげき・かそくで上がったSを後続へ引き継ぐ</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：メガ確定 物理アタッカー型（いじっぱり 72.6% / ようき 16.3%）

**性格採用率: いじっぱり 72.6% / ようき 16.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="メガバシャーモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（98.5%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> バシャーモナイト（72.9%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・インファイト<br>
・つるぎのまい<br>
・かみなりパンチ（とびひざげり）
</div>
</div>
</div>

フレアドライブ（ほのお・威力120・採用率84.7%）とインファイト（かくとう・威力120・採用率67.2%）のタイプ一致技2本が主軸。つるぎのまい（採用率47.9%）でこうげきを2段階上げてから打つ運用が中心です。4枠目はかみなりパンチ（でんき・威力75・採用率45.7%）ととびひざげり（かくとう・威力130・採用率21.1%）が選択肢で、かみなりパンチはアシレーヌ（みず/フェアリー）やメガリザードンY（ほのお/ひこう）といったフレアドライブ・インファイトがともに半減される相手への貴重な等倍以上の打点になります（メガギャラドスやゲッコウガのようなみず/あく複合にはインファイトの方が一致1.5倍で打点が高くなります）。

**強み:**

いじっぱり型はH157 / A233 / B100 / C135 / D100 / S152（EV: H2-A32-S32）。A233は非メガ型（A172）より約35%高く、乱数の発生範囲を縮めて確定数を安定させます。

**弱み:**

ようき型はH157 / A212 / B100 / C135 / D100 / S167で、いじっぱり型よりA実数値が約9%低い代わりにSが15高くなります。ただしガブリアス（ようき最速S169）にはようき型でも上から取れず、かそくが1段階入るまでは先手を取れない相手が残ります。

---

### 型2：きあいのタスキ 非メガ アタッカー型（きあいのタスキ 14.2%）

**性格採用率: ようき（想定・非メガ型の性格別内訳は非公開）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ 非メガアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（98.5%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H0-A32-S32（代表例）<br>
<strong>持ち物:</strong> きあいのタスキ（14.2%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・インファイト<br>
・かみなりパンチ<br>
・つるぎのまい
</div>
</div>
</div>

メガ進化枠を消費しない型で、きあいのタスキによりHP満タンから一撃を耐えて返り討ちにする運用です。技構成はメガ型と同じですが、パーティ全体でメガ進化権を他のポケモンに譲れる点が最大の違いになります。

**強み:**

H155 / A172 / B90 / C117 / D90 / S145（EV: H0-A32-S32、ようき）。きあいのタスキで確定1発を耐えられるため、瀕死上等の相討ち・後続への交代が読める相手に対して対面性能を発揮します。

**弱み:**

A172はメガ型のA233より約26%低く、一撃で処理できていた相手を取り逃す場面が増えます。またきあいのタスキは1回のみの効果で、すでにHPが減っている場面や複数回攻撃技には機能しません。

---

## データ分析①：M-3→M-4 技・持ち物・性格の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みきり（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>33.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+12.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">56.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-8.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-10.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">63.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>67.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.9pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま（持ち物）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>7.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バシャーモナイト（持ち物）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">76.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">74.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やんちゃ（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>3.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.6pp</td>
</tr>
</tbody>
</table>
</div>

M-4で最も動いたのは**まもる（-10.0pp）・つるぎのまい（-8.2pp）の採用率低下とみきりの上昇（+12.8pp）**です。まもるとみきりはどちらも優先度+4の見切り技ですが、みきりが同時に上昇していることから、単純な入れ替えというより見切り技全体の選択傾向が変化したと見られます。バシャーモナイトが-3.2pp・いじっぱりが-1.9pp低下する一方できあいのタスキ・いのちのたまが上昇しており、非メガ運用や火力寄りの構築が一定数M-4で増えたことが読み取れます。

---

## データ分析②：主要4技のカバレッジ計算

バシャーモの主力4技（フレアドライブ・インファイト・かみなりパンチ・じしん）が、M-4使用率上位15位（自分自身の10位を除く）の相手にどの程度刺さるかを検算しました。相手のメガ進化持ちはメガ石採用率50%超の個体をメガ後種族値・タイプで計算しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">相手</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">フレアドライブ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">インファイト</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">かみなりパンチ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">じしん</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ガブリアス（1位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ミミッキュ（2位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">カバルドン（3位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">メガメタグロス（4位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ブリジュラス（6位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">マスカーニャ（5位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">アシレーヌ（7位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">メガギャラドス（8位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">マフォクシー（9位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">メガリザードンY（11位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">サザンドラ（13位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">アーマーガア（14位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td></tr>
<tr><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">カイリュー（12位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 10px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ゲッコウガ（15位）</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center"><strong>×2</strong></td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
</tbody>
</table>
</div>

上位14匹のうち10匹にはいずれか1技以上が×2で通りますが、**ガブリアス（1位）・ミミッキュ（2位）・カバルドン（3位）・カイリュー（12位）の計4匹には4技すべて×2が入りません**。特にガブリアス・ミミッキュ・カバルドンは環境上位1〜3位であり、バシャーモの主力4技だけでは上位受けの一角に決定打を持てない構図が浮かびます。ただし**じしん（採用率5.9%）が単独で×2を取れるのはマフォクシーの1匹のみ**（メガメタグロス・ブリジュラスはフレアドライブ・インファイトと重複、アーマーガアははがね/ひこうでじしんが無効）で、他3技で代替が利く相手が多いため低採用率にとどまっています。一方**かみなりパンチ（採用率45.7%）が真に唯一の×2打点になるのはアシレーヌ・メガリザードンYの2匹**です。メガギャラドス・ゲッコウガ（ともにみず/あく）に対してはインファイトがかくとう×2・タイプ一致1.5倍で上回るため、かみなりパンチは最大打点ではありません。実際、メガギャラドス（H171、EV1振り）に対してA233（いじっぱりメガ型）のかみなりパンチは104〜122ダメージ（H171の61〜71%）にとどまり確定1発になりませんが、同条件のインファイトは246〜290ダメージ（143〜170%）となり確定1発で沈められます。かみなりパンチの採用理由は、インファイト・フレアドライブがともに半減されるアシレーヌ・メガリザードンYへの数少ない等倍以上の打点を確保する点にあります。

---

## 苦手なポケモン

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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率99.5%）が×2弱点。ようき最速個体（S169）のじしんはA200〜219 → 209〜270ダメージで、メガバシャーモ（H157）を確定1発で上回ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコファング（エスパー・採用率94.7%）が×2弱点。メガ後A216（いじっぱり）基準で211〜248ダメージとなり、メガバシャーモ（H157）を確定1発で上回ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（みず・採用率88.2%）が×2弱点。ひかえめC195基準で202〜237ダメージとなり、メガバシャーモを確定1発で上回ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（みず・採用率80.1%）・じしん（じめん・採用率77.8%）がいずれも×2弱点。持ち物はギャラドスナイト80.5%でメガ後（みず/あく）でも両技とも×2弱点のまま通ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス（エスパー・採用率56.7%）・サイコショック（エスパー・採用率39.7%）がいずれも×2弱点。フレアドライブ・インファイトはともに半減されるため打点も乏しい相手です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でバシャーモと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" loading="lazy">
    <div class="name">アローラキュウコン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" loading="lazy">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、バシャーモの弱点であるひこう・エスパーへのじしん・げきりんの打点を持ちません。両者に共通するじめん・みず弱点は重なりますが、ガブリアスのつるぎのまい・スケイルショットで先制圧力をかけ、バシャーモが後続で押し切る役割分担が成立します。

**ミミッキュ**（2位）はゴースト/フェアリーで、バシャーモの弱点タイプ（ひこう・じめん・みず・エスパー）をすべて等倍以下で受けられるため、対面を選ばず出せる壁役になります。ばけのかわで一度は行動保証されるかげうちが、バシャーモの弱点を突く相手への牽制になります。

**ブリジュラス**（3位）ははがね/ドラゴンで、バシャーモの弱点であるみず・エスパーをともに耐性（×0.5）で受けられます。ラスターカノン・りゅうせいぐんの特殊打点はバシャーモの物理打点と方向性が異なり、相手の受け出しを崩す役割を分担します。

**ギャラドス**（4位）はみず/ひこうで、バシャーモの弱点2つ（みず・ひこう）と同じタイプを持つため弱点は重なりますが、りゅうのまいで積んでからのたきのぼり・じしんが高打点を出せる別ルートのアタッカーとしてパーティ内で役割を分けられます。

**マスカーニャ**（5位）はくさ/あくで、バシャーモの弱点であるエスパーを無効（×0）で受けられます。はたきおとすで相手の持ち物を落とし、バシャーモの後続としての通りやすさを補助します。

**カバルドン**（6位）はじめん単タイプで、あくびによる交代誘導とステルスロックの設置役です。バシャーモの弱点であるじめん・みずのうちじめんは同タイプで無効にできませんが、ステルスロックで削った後にバシャーモが一撃で処理する運用がしやすくなります。

---

## まとめ

M-4のバシャーモは使用率10位で、特性かそくによる加速と高いこうげき種族値を軸にした物理アタッカーという基本性能は前シーズンから変わりません。

- **バシャーモナイト72.9%のメガ型が主流**：いじっぱり72.6%・ようき16.3%で、A実数値はいじっぱり型の方が非メガ型より約35%高い
- **きあいのタスキ型（14.2%）は非メガでメガ枠を温存**：A実数値はメガ型より約26%低い代わりに確定1発を耐える対面性能を持つ
- **かみなりパンチ（45.7%）はアシレーヌ・メガリザードンYに対する唯一の×2打点**：メガギャラドス・ゲッコウガにはインファイトの方が一致1.5倍で上回るため、かみなりパンチが最大打点になるのは限定的。じしん（5.9%）は他技と打点が重複する相手が多く採用率が伸びていない

弱点はひこう・じめん・みず・エスパーの4タイプで、ガブリアス（1位）・メタグロス（4位）・アシレーヌ（7位）・ギャラドス（8位）といった上位常連の主力技がいずれも×2で確定1発圏に入るため、後出しではなく先制して押し切る立ち回りが前提になります。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
