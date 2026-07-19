---
title: 'ドリュウズ考察 M-2 使用率55位 すなかきとかたやぶりの型別解説'
description: 'チャンピオンズM-2使用率55位ドリュウズを徹底解説。かたやぶり（採用率72.6%）でがんじょう等を貫く高火力じしん98.5%・アイアンヘッド96.1%のAS物理型と、すなかき26.2%で砂下S308相当（ようき）に達する高速型を実データで解説。スカーフ27.9%・タスキ25.1%・やわらかいすな20.4%の持ち物分岐も網羅します。'
updatedDate: '2026-07-18'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-excadrill-m2.png'
---

<style>
.poke-header { display:flex; align-items:center; gap:16px; margin:20px 0; }
.poke-header img { width:96px; height:96px; }
.build-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.item-icon { display:inline-block; width:32px; height:32px; vertical-align:middle; margin-right:4px; object-fit:cover; }
.partner-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(120px,1fr)); gap:12px; margin:16px 0; }
.partner-card { text-align:center; padding:8px; border:1px solid #e2e8f0; border-radius:8px; }
.partner-card img { width:56px; height:56px; display:block; margin:0 auto 4px; }
.partner-card .name { font-size:0.75rem; font-weight:bold; }
.partner-card .rate { font-size:0.7rem; color:#666; }
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ" />
  <div>
    <h2 style="margin:0 0 8px">ドリュウズ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">55位</strong>　特性: <strong>かたやぶり 72.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ドリュウズは**使用率55位**を記録。特性は**かたやぶり（採用率72.6%）**が主流で、すなかき（26.2%）が砂パ前提の選択肢として続きます。

ドリュウズの軸は**こうげき種族値135**から放つじしん（採用率98.5%）・アイアンヘッド（96.1%）の高火力一致技です。じめん/はがねという攻撃範囲の優れたタイプに、かたやぶりでがんじょう・ふゆう等の特性を無視して技を通せる性質が加わり、上から弱点を突く物理アタッカーとして機能します。

持ち物は**こだわりスカーフ 27.9%・きあいのタスキ 25.1%・やわらかいすな 20.4%・ドリュウズナイト 18.5%**と分散しており、役割によって型が分かれます。本記事では非メガを基準に、メガドリュウズ（メガ後A165・S103）の差分も併せて解説します。

---

## なぜドリュウズが使われるのか

### 1. かたやぶりでがんじょう・ふゆうを無視して技を通す

ドリュウズの主流特性は**かたやぶり（採用率72.6%）**で、相手の特性を無視して技を出せます。これにより、ステルスロック展開役のエアームド（はがね/ひこう）が持つがんじょう（採用率61.9%）を無視してきあいのタスキ相当の耐えを許さず、ふゆう持ちにもじしんを通せます。じしん98.5%・アイアンヘッド96.1%という一致技の高採用率は、この「特性に阻まれず火力を押し付ける」設計を反映しています。

### 2. じめん/はがねの一致技で環境上位に刺さる

じしん（じめん）は環境のはがね・いわ・どく・でんき・ほのおに広く刺さり、アイアンヘッド（はがね）はフェアリー・いわ・こおりに通ります。例えばキラフロル（いわ/どく・15位）にはじしんが×4（いわ2×どく2）で通り、ミミッキュ（ゴースト/フェアリー・19位）にはアイアンヘッドが×2（フェアリー弱点）で刺さります。2つの一致技だけで弱点を突ける相手が広いのが採用理由です。

### 3. つるぎのまいで火力を一段引き上げる

つるぎのまい（採用率33.5%）を1回積めばこうげきが2倍になり、いじっぱりのこうげき205から、高耐久のはがね・じめん勢も一致技で抜ける火力に届きます。低耐久（B60・D65）で受け回しには向かないため、上から殴るか積んで全抜きを狙う攻めの起用が基本です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">110</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">135</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">88</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">508</span>
  </div>
</div>

こうげき135・HP110が軸で、すばやさ88は環境中堅です。ようき＋すばやさ最大振りでもS154と、ガブリアス（S169）やリザードン（S167）には先手を取られます。ぼうぎょ60・とくぼう65と耐久面は脆く、弱点技はもちろん等倍でも被弾が痛いため、**速度を補うスカーフ／砂下のすなかき、または1回耐えるタスキ**で行動回数を確保するのが基本です。

### メガ進化（ドリュウズナイト採用率18.5%）

ドリュウズナイトの採用率は18.5%で、半数以上はスカーフ・タスキ・やわらかいすなの非メガ構成です。メガ進化するとこうげき165・ぼうぎょ100・すばやさ103まで上がり、特性は**かんつうドリル**（接触技を使う際、相手のまもる等の守りの効果を無視して本来の1/4のダメージを与える）に変化します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">通常</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">135</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">165</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+40</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+15</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">88</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">103</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+15</td>
</tr>
</tbody>
</table>
</div>

メガ後はすばやさ103（ようきでS170）まで伸び、ガブリアス（S169）をわずかに上回ります。こうげき165（いじっぱりでこうげき238）・ぼうぎょ100で攻守ともに強化され、つるぎのまいなしでも上位の物理打点を出せます。一方、スカーフで最速勢を抜く役割・タスキで1回耐える保険は失われ、メガ枠を1体に固定する制約がかかります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="じめん" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½・¼）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ(¼)</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-direction:column;gap:4px">
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

はがねの耐性が豊富で、でんき・どくを無効化できるのが対戦上重要です。ウォッシュロトムの10まんボルト（採用率56.8%）やキラフロルのどく技を透かせます。一方、弱点のほのお・みず・かくとう・じめんは4タイプと少ないものの、いずれも環境に多く、低耐久（B60・D65）と合わせて被弾は重い点に注意が必要です。特にじめん技は同タイプのガブリアス（じしん採用率99%級）から×2で通る一方、こちらのじしんはガブリアスに等倍止まりで、素のすばやさでは先に殴られます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん一致の主力打点。はがね・どく・でんき・ほのお・いわに刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致技。フェアリー・いわ・こおりに刺さる。30%ひるみ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いわなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう・むし・ほのおへの打点。リザードン・ウルガモスに刺さる。30%ひるみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき2段階上昇の積み技。火力を一段引き上げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つのドリル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">一撃</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一撃必殺技。高耐久を確率で突破。命中30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こうそくスピン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技を除去しつつS1段階上昇</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のS1段階低下。先手で速度勝負を制しやすくする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技。後続のために露払いする</td>
</tr>
</tbody>
</table>
</div>

じしん・アイアンヘッドの一致2枠はほぼ確定で、3枠目をいわなだれ（ひこう・むし対応）、残り1枠をつるぎのまい・つのドリル・こうそくスピン・がんせきふうじから役割に応じて選ぶのが標準的な技構成です。

---

## 主要型の解説

各型は持ち物分布（スカーフ27.9%／タスキ25.1%／やわらかいすな20.4%／ドリュウズナイト18.5%）と特性（かたやぶり72.6%／すなかき26.2%）を指標としています。性格はようき54.9%・いじっぱり42.7%が二分し、速度を取るか火力を取るかで選択が分かれます。

### 型1: こだわりスカーフ型（最多）

**指標: こだわりスカーフ 27.9%／かたやぶり 72.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かたやぶり（72.6%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り。最多はH+2）<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・アイアンヘッド<br>
・いわなだれ<br>
・つのドリル / がんせきふうじ
</div>
</div>
</div>

**強み:**

スカーフ補正でようきS154が約231相当となり、ガブリアス（S169）・マスカーニャ（S192）など最速の環境上位を上から叩けます。砂パートナーを必要とせず単体で速度を確保できるため、すなかき型と異なり構築の自由度が高いのが特長です。一撃必殺のつのドリルを採用すれば、スカーフで上を取った高耐久を確率で突破できます。

**弱み:**

こだわりで技を固定されるため、つるぎのまいで積めず火力は無補正のまま頭打ちです。後出しからつるぎのまいを積んで全抜きを狙う動きはできず、技選択を読まれると交代で受けられます。

---

### 型2: すなかき高速型（すなかき 26.2%）

**指標: すなかき 26.2%／やわらかいすな 20.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">すなかきAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなかき（26.2%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り）<br>
<strong>持ち物:</strong> やわらかいすな
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・アイアンヘッド<br>
・いわなだれ<br>
・つるぎのまい / つのドリル
</div>
</div>
</div>

**強み:**

すなかきは砂嵐下ですばやさが2倍になる特性で、いじっぱりのS140が砂下では280相当に達します。スカーフ型と異なり技を固定されないため、つるぎのまいで積みつつ最速勢を上から抜く動きが可能です。やわらかいすなでじしんの威力が補強され、いじっぱりのこうげき205と合わせて一致技の火力が型1より高くなります。

**弱み:**

砂嵐の維持役（カバルドン等）との同居が前提で、砂が止むとすばやさは素の140に戻り、スカーフ型のように単体では速度を確保できません。やわらかいすなはこだわりスカーフのような速度補正がないため、砂を切られた盤面では中速止まりになります。

---

### 型3: メガドリュウズ型（ドリュウズナイト 18.5%）

**指標: ドリュウズナイト 18.5%／いじっぱり 42.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0530-00.webp" alt="メガドリュウズ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かたやぶり（72.6%）※メガ後かんつうドリル<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り）<br>
<strong>持ち物:</strong> ドリュウズナイト
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・アイアンヘッド<br>
・いわなだれ<br>
・つるぎのまい
</div>
</div>
</div>

**強み:**

メガ後はこうげき165（いじっぱりでこうげき238）・すばやさ103（ようきでS170）に上がり、スカーフ・砂のどちらにも依存せずに火力と速度を両立できます。ぼうぎょ100でスカーフ型・すなかき型では耐えられない物理打点も1回受けやすくなり、つるぎのまいなしでも上位の物理打点を出せます。

**弱み:**

スカーフで最速勢を抜く・タスキで1回耐える保険を持てないため、S170を上回るマスカーニャ（S192）・ゲッコウガ（S191）には先手を許します。メガ枠を1体に固定する制約もあり、構築全体のメガ選択を縛ります。

---

### 補足: きあいのタスキ型（25.1%）

タスキ型は低耐久のドリュウズが弱点技を1回耐え、S154から確実に1手返せます。かたやぶりでがんじょうを無視しつつ、自身はタスキで耐えるため、初手のステルスロック設置や一撃必殺のつのドリルを安全に通しやすいのが利点です。先制技・砂嵐ダメージ・設置ダメージでタスキが潰れる点はスカーフ・メガ型にない弱点です。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ドリュウズと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ようき最大振りのS154（メガ後170・砂下すなかき308相当・スカーフ約231相当）は持ち物・特性で大きく変わる一方、素のすばやさでは環境上位の最速勢に先手を許す点、そしてB60・D65と耐久は低く、弱点（ほのお・みず・かくとう・じめん）はいずれも環境に多い点に注意してください。

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
    <img src="/images/pokemon/pokemon-0660-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×4（いわ2×どく2）。どく技を無効化でき、こちらの一致技で確定圏。スカーフ・メガなら上から処理</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ 速度有利だが等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん・アイアンヘッドとも等倍止まり（フェアリーにはがね×2でもみず半減で相殺）。S154＞112で先手だが、みず技（なみのり等）が×2弱点でアクアジェット（66.6%）の先制も痛く、撃ち合いは五分</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（はがね弱点・ドラゴン等倍）。10まんボルト（66.9%）は無効化でき、りゅうせいぐん（64.8%）も半減。S154＞150で先手。ただしはどうだん（26.9%）持ちにはかくとう×2を返される</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはドラゴン/じめんに等倍・アイアンヘッドも半減で有効打が乏しい。相手のじしん（採用率99%級）はこちらに×2。素のS169＞154で先に殴られ、スカーフ（約231相当）かメガ（170）で上を取っても等倍では一撃に届かない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ひこうでじしんが無効、アイアンヘッドも半減。ほのお技（かえんほうしゃ42.4%等）が×2弱点。S167＞154で先手を許す。いわなだれは×4で通る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ひこうでじしんが無効。たきのぼり（85.9%）が×2弱点。S146＜154で素は先手だが、りゅうのまい（73.3%）で抜かれ撃ち合いに負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（71.5%）が×2弱点。じしんは×2で通るがS156＞154でわずかに先手を許す。しんそく（23.6%）の先制も痛い</td>
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
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうでじしんが無効・アイアンヘッドも半減され、こちらはほのお技（かえんほうしゃ42.4%等）が×2。S167で先に殴られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ（ひこう×2）で先制して落とすか、みず・でんき枠（ウォッシュロトム等）を後続に置いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうでじしんが無効、たきのぼり（85.9%）が×2弱点。りゅうのまい（73.3%）を積まれると速度・火力で上回られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ（ひこう×2）を先に通すか、でんき・くさ枠（ウォッシュロトム・フシギバナ等）に引いてみず技を受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（71.5%）が×2弱点で、S156でわずかに先制される。しんそく（23.6%）の先制も低耐久に刺さる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう・エスパー・ゴースト枠（リザードン・ゲンガー等）でかくとうを半減・無効化して受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん単で高耐久。じしん（98.0%）が×2でこちらに通り、あくび（94.2%）で流される。一致じしんは等倍で一撃には届かない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまいを積んでから抜くか、くさ・みず枠（フシギバナ・カメックス等）でじめんを半減して受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0395-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">エンペルト（58位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/はがねでじしん以外を半減し、こちらはみず技が×2。じしんは×2で通るが高耐久で一撃に届かず撃ち合いで不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・でんき枠（フシギバナ・ウォッシュロトム等）を合わせてみず/はがね両方の弱点を突く</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「じしんを無効化するひこう・ふゆう勢」と「みず・かくとう・ほのお技で低耐久のこちらを撃ち合いで倒す相手」に大別されます。いずれも単体での切り返しは難しいため、後続のタイプ補完で受ける構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0395-00.webp" alt="エンペルト">
    <div class="name">エンペルト</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/はがねでドリュウズの弱点ほのお・みずを半減し、苦手なリザードンを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0855-00.webp" alt="ポットデス">
    <div class="name">ポットデス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ゴーストでかくとうを無効化。からをやぶる積みで攻撃面を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ひこうでじめん無効。ドリュウズが苦手なみず・ほのおに打点を持つ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">すなおこしで砂を展開し、すなかき型のS2倍を発動させる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでみず・くさを半減。ステルスロックで露払い</div>
  </div>
</div>

**パーティ構成の基本方針:**

ドリュウズは耐久が低く、じしんを無効化するひこう勢に止められやすいため、残り5体で以下の役割を補います。

1. **ひこう対策**: でんき・いわ枠（ウォッシュロトム等）でリザードン・ギャラドスのひこう勢に打点を持つ
2. **みず対策**: くさ・みず枠（フシギバナ・エンペルト）でアシレーヌ等のみず技を半減する枠
3. **かくとう対策**: ひこう・エスパー・ゴースト枠（ギャラドス・ポットデス）でルカリオのかくとう技を半減・無効化する枠
4. **砂の維持（すなかき型）**: すなおこしのカバルドンで砂を展開し、すなかきのS2倍を発動させる

---

## データ分析①：技採用率に見る「一致2枠＋いわ」の固定設計

ドリュウズの技採用率は、じしん98.5%・アイアンヘッド96.1%という**一致2枠がほぼ確定**で、いわなだれ64.8%が3枠目に固定される点に特徴があります。

| 技 | タイプ | 採用率 | 主な役割 |
|---|---|---|---|
| じしん | じめん | 98.5% | はがね・どく・でんき・ほのお・いわ |
| アイアンヘッド | はがね | 96.1% | フェアリー・いわ・こおり |
| いわなだれ | いわ | 64.8% | ひこう・むし・ほのお |
| つるぎのまい | ノーマル | 33.5% | 火力強化（積み） |

じしん・アイアンヘッドの2枠で弱点を突ける相手が広いため、3枠目のいわなだれは「一致技が等倍以下になるひこう（リザードン・ギャラドス）」を補完する目的で固定されます。残り1枠が、つるぎのまい33.5%（積み）・つのドリル29.2%（一撃必殺）・こうそくスピン19.2%（設置除去）・がんせきふうじ18.6%（S低下）と分散するのは、「攻撃範囲は一致2枠＋いわでほぼ完結し、最後の1枠を持ち物・特性に応じた役割技に充てる」という構築思想の表れです。スカーフ型はつのドリルで上を取った高耐久を確率突破し、すなかき・メガ型はつるぎのまいで積んで全抜きを狙う、と型ごとに最終枠が変わります。

---

## データ分析②：持ち物・特性の4分割に見る速度確保の3択

ドリュウズの最大の弱点はすばやさ88（ようきでS154）で、環境上位の最速勢に届かない点です。持ち物・特性の分布は、この速度をどう補うかの選択がそのまま型に反映されています。

| 速度確保手段 | 採用率 | ようき時のS（相当） | 特徴 |
|---|---|---|---|
| こだわりスカーフ | 27.9% | 約231相当 | 単体で速度確保。技固定 |
| すなかき（砂下） | 26.2% | 308相当 | 最速。砂維持役が必要 |
| メガ（S103） | 18.5% | 170 | 火力・耐久も同時強化 |
| きあいのタスキ（速度補正なし） | 25.1% | 154 | 1回耐えて返す |

スカーフ（約231相当）・砂下すなかき（308相当）はガブリアス（S169）・マスカーニャ（192）を上から叩ける一方、スカーフは技固定、すなかきは砂維持役（カバルドン）との同居が前提という制約を抱えます。メガは速度補正こそ控えめ（S170でガブリアスをわずかに上回る程度）ですが、火力・耐久も同時に伸びるため単体性能で勝ります。タスキは速度を補えない代わりに、低耐久のドリュウズが1回行動を保証されます。同程度に割れたこの4分布は、「ドリュウズの起用は速度をどう補うかで決まる」ことを定量的に示しています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">スカーフAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スカーフ 27.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">単体で最速勢を抜く。砂不要で構築自由</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技固定で積めず火力は無補正</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すなかきAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すなかき 26.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やわらかいすな</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">砂下S308相当で最速。積みも可能</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">砂維持役が必須。砂が切れると中速</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドリュウズナイト 18.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドリュウズナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A238・B100で火力と耐久を両立</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S170止まりで最速勢には届かず。メガ枠を縛る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">タスキAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タスキ 25.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">1回耐えて確実に1手返す。設置・一撃に安定</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">速度補正なし。先制・砂・設置で潰れる</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ドリュウズはこうげき135とじめん/はがねの優秀な攻撃範囲を軸に、じしん98.5%・アイアンヘッド96.1%・いわなだれ64.8%で環境上位に弱点を突く物理アタッカーです。かたやぶり（72.6%）でがんじょう・ふゆうを無視し、特性に阻まれず火力を押し付けられるのが最大の武器です。

持ち物・特性はスカーフ27.9%・すなかき26.2%・タスキ25.1%・メガ18.5%とほぼ4分割で、「単体で最速を取る」「砂下で最速かつ積む」「1回耐える」「火力と耐久を両立する」のどれを取るかで役割が変わります。一方、B60・D65の低耐久と、じしんを無効化するひこう勢への弱さは構築単位の補完が前提で、苦手なリザードン・ギャラドス・ルカリオには後続のタイプ補完で対応する必要があります。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [じしんを無効化する苦手枠 リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
- [砂を共有する同居枠 カバルドンのM-2考察](/blog/hippowdon-analysis-m2/)
