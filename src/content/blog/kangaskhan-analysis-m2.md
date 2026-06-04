---
title: '【ポケモンチャンピオンズ】メガガルーラ考察 M-2 使用率34位 技構成と立ち回り'
description: 'M-2シングルバトルで使用率34位のメガガルーラを実データで分析。おやこあいによる2回攻撃の仕様、れいとうパンチ76.6%・じしん75.5%・ふいうち61.8%の技構成、いじっぱりAS型の立ち回り、環境上位への相性まで解説します。'
pubDate: '2026-06-04'
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
  <img src="/images/pokemon/pokemon-0115-00.webp" alt="メガガルーラ" />
  <div>
    <h2 style="margin:0 0 8px">メガガルーラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">34位</strong>　メガ石採用率: <strong>ガルーラナイト 96.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ガルーラは**使用率34位**を記録。そのうち**96.6%がガルーラナイトを採用**しており、ほぼ全ての対戦でメガ進化を前提とした構成です。

メガガルーラの核となるのが特性**おやこあい**。攻撃技が2回判定で当たり、2発目は威力が4分の1（25%）に下がる仕様です。1回目で削り、2回目できあいのタスキやがんじょうを貫通する、あるいは確定数を1つ縮める動きが持ち味になります。タイプはノーマル単で、特性**きもったま**（採用率90.9%）を併せ持つためゴーストタイプにもノーマル技が等倍で通ります。

---

## なぜメガガルーラが採用されるのか

### 1. おやこあいの2回攻撃でタスキ・がんじょうを貫通

メガガルーラの最大の強みは特性**おやこあい**による2回攻撃です。1ターンに攻撃が2回判定され、1発目は通常威力、2発目は威力が4分の1になります。すてみタックル（威力120）なら1発目120＋2発目30相当の合計火力になります。

この仕様の実戦的な意味は火力の上乗せだけではありません。きあいのタスキでHP1を残した相手を2発目で確実に倒せること、そして1発目で「みがわり」を割ってから2発目で本体に通せることです。1回の行動で削りと処理を同時にこなせる点が、単発技のアタッカーにはない価値です。

### 2. きもったまでゴーストにノーマル技が通る

特性**きもったま**（採用率90.9%）により、本来ノーマル技が無効のゴーストタイプにもすてみタックル・のしかかりが等倍で通ります。M-2環境はゴースト/どくのゲンガー（10位）、はがね/ゴーストのギルガルド（11位）、ゴースト/フェアリーのミミッキュ（19位）とゴースト勢が多く、ノーマル技を透かされない点はメインウェポンの通りを安定させます。

### 3. れいとうパンチ・じしん・ほのおのパンチで弱点をピンポイントに突く

ノーマル単の一致技だけでは半減・無効を取られやすいため、メガガルーラは攻撃範囲を広げるサブウェポンを高採用率で抱えます。れいとうパンチ（76.6%）はドラゴン・ひこう・じめん・くさへ、じしん（75.5%）ははがね・どく・でんき・いわ・ほのおへ刺さります。両方を採用することで、一致技を半減するはがねタイプにもじしんで、ガブリアスやカイリューにはれいとうパンチで弱点を突けます。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">590</span>
  </div>
</div>

HP105・B100・D100と耐久が高水準でまとまり、A125の攻撃力と合わせて「硬くて殴れる」バランス型です。とくこう60は捨てており、技は全て物理。耐久があるためメガ進化の1ターンを挟んでも崩れにくく、ねこだまし→メガ進化→おやこあい技という安定した起点作りができます。

### メガ前→メガ後ステータス変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">105</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">105</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">125</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">100</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+10</td>
</tr>
</tbody>
</table>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">なし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト
  </td>
</tr>
</tbody>
</table>
</div>

ノーマル単タイプは弱点がかくとう1つだけで、ゴーストを無効化します。弱点が少なく耐久も高いため、メガ進化のターンを安全に挟みやすいのが利点です。ただし耐性も無効のゴースト以外は持たず、半減で受け回す芸当はできません。かくとうを高火力で連打してくる相手（オオニューラ等）には注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">76.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリュー等ドラゴン/じめん/ひこうへの弱点打点。10%こおり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どく・いわへの打点。ギルガルド・ドドゲザン対策</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70 先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>61.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手が攻撃技選択時のみ成功。高速アタッカーへの先制打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すてみタックル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>48.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技の最大火力。与ダメージの3分の1の反動</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねこだまし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40 先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+3で確定ひるみ。場に出た最初のターンのみ使用可。メガ進化の起点作りに</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のしかかり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">反動なしの一致技。30%まひ。すてみタックルとの選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサム・アーマーガア等はがね（じしん半減のひこう複合含む）への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドレインパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">与ダメージの半分を回復。ドドゲザン等あく/はがねへの打点と自己回復</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシレーヌ・ギャラドス等みず/ひこうへの打点</td>
</tr>
</tbody>
</table>
</div>

おやこあい補正は全ての攻撃技に乗るため、上記の威力はいずれも「1発目通常＋2発目4分の1」の2回判定で入ります。先制技ふいうちにもおやこあいが乗る点が特徴で、削れた高速アタッカーを2回判定で確実に倒しきれます。

---

## 主要型の解説

性格はいじっぱり89.3%・ようき7.0%で、ほぼいじっぱりの物理型に固定されています。技は4枠を「すてみタックル/のしかかり・れいとうパンチ・じしん・ふいうち/ねこだまし」から選ぶ形が主流です。

### 型1: いじっぱりAS型（最多採用）

**性格採用率: いじっぱり 89.3%**　**EV: AS+hb 20.5%（AS振りに余りをHBへ）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0115-00.webp" alt="メガガルーラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱりAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（余りをHBに）<br>
<strong>持ち物:</strong> ガルーラナイト
</div>
<div>
<strong>技構成:</strong><br>
・すてみタックル / のしかかり<br>
・れいとうパンチ<br>
・じしん<br>
・ふいうち / ねこだまし
</div>
</div>
</div>

**強み:**

A32・S32の最速いじっぱりは、すばやさ実数値でメガ後S100相当に届き、ガブリアス（S102）にこそ届かないものの、リザードン（S100）と同速、サザンドラ（S98）・ミミッキュ（S96）・キラフロル（S86）といった環境上位を上から叩けます。れいとうパンチ・じしんの2枠で弱点を突き分け、ふいうちでこちらより速いマスカーニャ（S123）・オオニューラ（S120）・スターミー（S115）・ゲンガー（S110）にも先制で打点を持てます。

おやこあいですてみタックルが2回判定になるため、HA振りより火力で劣るぶんを2発目の上乗せが補います。きあいのタスキ持ちを1ターンで処理できるのもAS型の強みです。

**弱み:**

HBへの振りが余り程度のため耐久面はメガ後の素の数値頼みで、ようきにしない限りオオニューラ（S120）・マスカーニャ（S123）には先手を取られ、かくとう技や高火力技で削られます。最速にしても抜けない高速勢が多く、ふいうちで対処できなければ押し負ける場面があります。

---

### 型2: HA耐久振り型（2番目に多い構成）

**性格採用率: いじっぱり**　**EV: HA 15.5%（H・Aに厚く振る）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0115-00.webp" alt="メガガルーラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱりHA型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（耐久重視）<br>
<strong>持ち物:</strong> ガルーラナイト
</div>
<div>
<strong>技構成:</strong><br>
・すてみタックル / のしかかり<br>
・れいとうパンチ<br>
・じしん<br>
・ねこだまし / ふいうち
</div>
</div>
</div>

**強み:**

AS型がすばやさに割く32をHに回すことで、HP実数値が大きく伸び、B100・D100の両受けがさらに硬くなります。ねこだまし→メガ進化の起点作りを耐久で安定させ、攻撃を1〜2発受けてから殴り返す「居座り型」として機能します。すばやさを捨てるためふいうちの先制依存度が上がる一方、ねこだましでひるませてから動ける場面が増えます。

**弱み:**

AS型がすばやさで先制できたリザードン・サザンドラ・キラフロルなどに先手を取られ、れいとうパンチで縛れていた相手を上から処理できなくなります。耐久を活かすには受け出しが前提になるため、かくとう弱点を突かれる交代戦では脆さが残ります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、メガガルーラと相性がはっきり出るポケモンを有利・不利の両面から挙げます。メガ後はノーマル単・S100で、れいとうパンチ・じしん・ふいうちの3技で広い弱点をカバーできる一方、半減で受け回す耐性を持たず、かくとう弱点とこちらより速い高速勢が弱点です。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（同速注意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチが×4（ドラゴン2×じめん2）。おやこあいの2回判定でタスキも貫通。ただしS102でこちらより速く、じしん（採用率99%）は等倍で通るため受けは利かない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S100で同速。じしんが×2（メガXのほのお/ドラゴン）またはひこう浮きで無効（メガY・通常ほのお/ひこう）と形態依存。後出しはほのお技×2で受けられない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（はがね2×ゴースト1）。S60で先手確保。きもったまでノーマル技も等倍で通る。ただしキングシールド・ポルターガイストには注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（あく1×はがね2）。S50で先手確保。先制技ふいうち（採用率99%）もあくはこちらに等倍だが、Bが高く一撃では落ちないため2回判定とじしんで詰める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（ゴースト1×どく2）。S110でこちらより速いがHP60・B60と低耐久。ふいうち（先制）または削れていればおやこあいで処理可能</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（炎技採用時）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ（採用率21%）が×4（むし2×はがね2）で刺さる。S65で先手。炎技不採用だとじしん半減・ノーマル半減で打点が細く、つるぎのまい＋バレットパンチに注意</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

選定基準は「こちらより速くかくとう技で弱点を突ける」「半減・無効でこちらの打点が大きく削がれ受けに回れない」相手です。

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
    <img src="/images/pokemon/pokemon-0903-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">オオニューラ（33位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S120でこちらより速く、インファイト（採用率99%）が×2弱点。ねこだまし（36%）→インファイトで上から崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト（ギルガルド・ミミッキュ、かくとう無効）やフェアリー（ピクシー、かくとう半減）を同伴し受け出して処理する。先手は取れないためガルーラ単体で勝とうとしない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位・スカーフ/同速）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S102でこちらより速く、じしん（99%）が等倍で通り高HP・高Bを抜けない場面がある。スカーフ型は確実に先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ×4が刺さるので削れていればふいうちで先に処理。受けるならじしんを無効化するアーマーガア等ひこうタイプを同伴する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう/はがねでじしん無効・ノーマル等倍、れいとうパンチも半減（ひこう2×はがね0.5＝等倍）でB105を抜けない。はねやすめ（98%）で受け回される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ（×2）採用個体なら殴り合える。非採用なら、でんき・ほのおタイプを同伴して弱点を突いて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちらより速い。とんぼがえり（70%）で削りつつ交代され、トリックフラワー（93%・急所必中）で居座る側に消耗を強いられる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（先制）で削る。みず・ひこう・どくなどくさ/あくの弱点を突けるタイプを同伴して上から処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ">
    <div class="name">オオニューラ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S120の高速かくとう。ガルーラが苦手なはがね・あく枠に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0036-00.webp" alt="ピクシー">
    <div class="name">ピクシー</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">フェアリーでかくとうを半減。ガルーラの弱点を補完する受け枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。ステロ展開でおやこあいの2回判定と合わせ確定数を縮める</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーでかくとう半減。リザードン等ほのおにも後出ししやすい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう/はがねでガブリアスのじしんを無効化。はねやすめで居座る受け回し枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガガルーラは耐久が高い反面、半減で受け回せず、かくとう弱点と高速勢が明確な穴です。残り5体で以下を補います。

1. **かくとう対策**: フェアリー（ピクシー・アシレーヌ）でオオニューラ等のインファイトを半減して受ける枠
2. **高速アタッカー対策**: ガルーラより速いマスカーニャ・スターミーを上から処理できる高速枠
3. **ステルスロック展開**: ガブリアス・カバルドンでステロを撒き、おやこあいの2回判定と合わせて確定数を縮める

---

## データ分析①：おやこあいの2回判定が確定数に与える影響

おやこあいは「1発目通常威力＋2発目4分の1威力」の2回判定です。単純な火力換算では通常の1.25倍（1+0.25）ですが、実戦での価値はこの数値以上に立ち回りへ効きます。

| 状況 | 単発技 | おやこあい（2回判定） |
|---|---|---|
| きあいのタスキ持ち | HP1で耐えられる | 1発目で削り2発目で処理 |
| みがわり持ち | みがわりを割って終了 | 1発目で身代わりを割り2発目を本体に通す |
| 高耐久を「乱数2発」 | 乱数次第で1ターン目に倒せない | 2発目の上乗せで確定2発に寄せられる |

最も効くのは**きあいのタスキ・がんじょうの貫通**です。M-2環境はきあいのタスキ採用が広く、単発アタッカーは1ターンでは処理しきれませんが、メガガルーラは1回の行動でタスキを潰して倒しきれます。これにより、すばやさで上回られても「1ターンで確実に1体落とす」役割が安定し、HP105・B100・D100の耐久で次の相手も受けながら動けます。火力種族値A125が突出して高いわけではない（メガリザードンXのA130等が上）にもかかわらず採用される理由は、この処理の確実性にあります。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">EV指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">いじっぱりAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">AS+hb 20.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">すてみタックル・れいとうパンチ・じしん・ふいうち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">リザードン・サザンドラ等を上から処理。タスキ貫通</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">オオニューラ・マスカーニャに先手を取れない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">いじっぱりHA型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA 15.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">すてみタックル・れいとうパンチ・じしん・ねこだまし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">HP最大化で受け出しが安定。居座り性能が高い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">AS型が抜けた中速勢に先手を取れずふいうち依存</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガガルーラはおやこあいの2回判定による「確実な1体処理」と、HP105・B100・D100の高耐久を両立した物理アタッカーです。れいとうパンチ・じしん・ふいうちの3技で広い弱点をカバーし、きもったまでゴースト勢にもノーマル技を通せます。

弱点はかくとう1つで耐久も高いため、ねこだまし→メガ進化の起点作りが安定するのが採用理由です。一方で半減で受け回せず、オオニューラ（33位・S120の高速かくとう）やマスカーニャ（3位）といったこちらより速い相手には先手を取れません。これらをパーティのフェアリー・高速枠でケアしつつ、おやこあいでタスキ持ちを確実に処理していく立ち回りが基本になります。使用率34位ながら、確定数を縮める2回判定の安定性で根強く採用されています。

---

## 関連記事

- [天敵となる高速かくとう ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同じ物理アタッカー メガルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [同居しやすいはがね枠 ハッサムのM-2考察](/blog/scizor-analysis-m2/)
