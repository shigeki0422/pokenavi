---
title: '【ポケモンチャンピオンズ】ゲンガー 考察 M-5 シーズン メガシンカ型の実数値と4つの弱点'
description: 'M-5シーズン使用率19位のゲンガーを考察。メガ石採用率80.6%、シャドーボール88.3%を軸にしたメガゲンガーC222の実数値と、じめん・ゴースト・エスパー・あくの4弱点への対策、苦手・得意なポケモン、同居率上位のパートナーをデータで解説します。'
pubDate: '2026-08-17'
updatedDate: '2026-08-17'
heroImage: '../../assets/hero-gengar-m5.png'
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
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" />
  <div>
    <h2 style="margin:0 0 8px">ゲンガー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">19位</strong>　持ち物: <strong>ゲンガナイト 80.6%</strong>
    </div>
  </div>
</div>

M-5シーズン、ゲンガーは使用率19位につけています。メガ石（ゲンガナイト）採用率は80.6%と圧倒的多数を占め、メガ進化でC170まで伸びる特殊アタッカー運用が基本です。シャドーボール（採用率88.3%）・ヘドロウェーブ（74.6%）の一致技に加え、まもる（56.5%）・みちづれ（53.7%）・ほろびのうた（31.5%）といった行動保証・特殊戦術の採用率も高く、単純な殴り合いだけでなく駆け引きの多いポケモンです。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:85%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">170</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong>130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

メガ進化前はC130・S110（合計500）ですが、メガ進化でC170・S130まで伸びます。非メガのB60・メガ後のB80も高耐久とは言えず、殴り合いよりも一撃で仕留める・状態異常で流れを作る立ち回りが前提の種族値です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

じめん・ゴースト・エスパー・あくの4タイプに×2弱点を持つ、環境上位の中でも弱点の多いタイプです。一方でノーマル・かくとう無効、どく・むしは×0.25という防御的な強みもあります。詳細な相手対策は後述の「苦手なポケモン」を参照してください。

### 特性

**のろわれボディ（100%）**。技のダメージを受けると30%の確率で4ターンの間、相手をわざふうじ状態にします。メガ進化後は特性が**かげふみ**（ゴーストタイプ以外の相手を交代不能にする）に変わり、退場を許さず追い詰める運用と相性が良くなります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。20%で相手の特防を下げる。ほぼ確定枠</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">74.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致最大威力技。フェアリー対策の主力</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+4。相手の技を透かして状況を見極める</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みちづれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">53.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みちづれ状態のターンに自分を倒した相手を道連れにする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほろびのうた</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">場の全員に3ターン後ひんしになるほろび状態を付与</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こごえるかぜ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の素早さを1段階下げる補助打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドドゲザン等のあく複合への高火力だが命中70%</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

### 型① メガシンカ型 おくびょう

**性格採用率: おくびょう 76.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガシンカ型 おくびょう</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（100%、メガ後はかげふみ）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（37.1%）<br>
<strong>持ち物:</strong> ゲンガナイト（80.6%）
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ヘドロウェーブ<br>
・まもる<br>
・みちづれ or ほろびのうた
</div>
</div>
</div>

メガ進化でC222・S200（おくびょう時）を得る、環境で最も採用されている型です。まもる・みちづれで相手の行動を見極めつつ、メガシンカでかげふみを発動させて退場を許さず攻めきる構成が中心です。

**強み:**

C222は環境屈指の特殊火力で、シャドーボール・ヘドロウェーブの一致技だけで多くの相手を確定圏に収めます。かげふみで対面の相手を固定できるため、みちづれ・ほろびのうたとの相性も良好です。

**弱み:**

ゲンガナイトでメガ進化枠を1つ使うため、型②のようにメガ枠を他のポケモン（メタグロス・カイリュー等）に譲る構築は組めません。また型②のきあいのタスキと違い、先制技や高火力の一致技を受けた際にHP1で耐える行動保証がなく、後述の苦手表にある相手の弱点技を初手から受けると一撃で沈められる場面も少なくありません。

---

### 型② きあいのタスキ型（非メガ）

**持ち物採用率: きあいのタスキ 17.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型（非メガ）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（100%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（37.1%）<br>
<strong>持ち物:</strong> きあいのタスキ（17.2%）
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ヘドロウェーブ<br>
・ほろびのうた<br>
・まもる
</div>
</div>
</div>

メガ石を他のポケモンに譲り、H60という薄いHPをきあいのタスキで一撃で倒される攻撃への耐性に変える型です。非メガのC実数値182・S実数値178にとどまりますが、一発を耐えてほろびのうた・みちづれを確実に通せる保証が魅力です。

**強み:**

きあいのタスキで最低1回は行動が保証されるため、ほろびのうたを通しやすく、メガ枠を他のポケモン（メタグロス・カイリュー等）に譲る構築を組めます。

**弱み:**

C182・S178はメガ型のC222・S200を下回り、特にC火力の差（-40、約18%減）は確定数に直結します。使用率TOP30ではガブリアス（47.1%）・ブリジュラス（37.9%）・カバルドン（79.5%）・キラフロル（36.7%）の4体がステルスロックを採用率20%以上で持ち、踏んでいるとタスキが機能しません。

---

## データ分析：メガ進化の有無でC実数値がどこまで変わるか

メガシンカ型・きあいのタスキ型のC実数値を比較します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">C実数値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">S実数値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><strong>メガ進化型</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">222</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">200</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かげふみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ型（非メガ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">182</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">178</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろわれボディ</td>
</tr>
</tbody>
</table>
</div>

メガ進化によるC+40（約22%増、222/182）は特殊アタッカーとして無視できない差です。一方でじめん弱点への耐性は型によらず共通の課題です。ガブリアスのじしん（威力100、じめんタイプ、採用率99.5%）を、多数派の性格であるようき（採用率50.9%、A実数値182。ようきは素早さ↑・特攻↓の補正でAは無補正）で計算すると、メガゲンガー（B実数値100、HP137）に206〜246ダメージ＝150〜180%となり、最低乱数206がHP137を上回るため耐久が非メガ・メガ後のどちらでも確定1発です。メガ石採用率が80.6%と圧倒的多数派なのは、耐久面の弱さがどの型でも変わらない以上、火力を最大化した方が合理的というデータの帰結と言えます。

---

## 苦手なポケモン

じめん・ゴースト・エスパー・あくの×2弱点を突く相手のうち、その技の採用率が高く（目安60%前後以上）実際に確定圏の打点になる、または先制・優先度技で速度に関係なく通る相手を、M-5使用率TOP30から公平に抽出しています（採用率が低い技や、双方が等倍以上で撃ち合う相手、相手の攻撃種族値が低くタイプ有利ほど脅威にならない技は除外）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.5%）がじめん×2。150〜180%の確定1発</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（96.6%）・シャドークロー（57.9%）がゴースト×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.5%）がじめん×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（76.8%）がじめん×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メタグロス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコファング（87.5%）がエスパー×2、じしん（39.6%）もじめん×2で二重に刺さる</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0655-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マフォクシー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス（56.7%）がエスパー×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">イダイトウ(オス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（72.4%）がゴースト×2。特性てきおうりょく（94.8%）で一致技が2倍化し、多数派のひかえめ（40.3%、C実数値145）なら156〜184（113.9〜134.3%）の確定1発だが、ひかえめ＋こだわりスカーフのS実数値は195でメガゲンガーのS200に届かず後出し・交代際に限る。実際に上を取れるのはようき系スカーフ（S実数値214、ようき18.4%）で、その場合C実数値118に下がるためシャドーボールは128〜152（93.4〜110.9%）の乱数1発にとどまる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">サザンドラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（99.2%）があく×2。スカーフ82.9%で先制も</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（68.9%）がじめん×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（86.4%）があく×2。おくびょうのメガ個体（メガ採用率65.4%×おくびょう53.0%）はS213でS200を上回る。シャドーボールも半減で受け返せない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0503-01.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ヒスイダイケンキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひけん・ちえなみ（99.4%）・ふいうち（84.8%、優先度+1）があく×2。ふいうちは速度に関係なく先制できるが、攻撃技以外を選ぶと失敗する技で、ゲンガーはまもる（56.5%）・みちづれ（53.7%）を高採用率で持つ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0681-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト（62.9%）がゴースト×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1000-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">サーフゴー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（98.8%）がゴースト×2でほぼ確定枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0983-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ドドゲザン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（98.9%、優先度+1）があく×2。速度に関係なく先制できるが、攻撃技以外を選ぶと失敗する技で、ゲンガーはまもる（56.5%）・みちづれ（53.7%）を高採用率で持つ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0197-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブラッキー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">イカサマ（97.7%）があく×2。相手（メガゲンガー）自身のA76・B100を参照する特殊な仕様で、84〜98（HP137の61〜72%）の確定2発。ねがいごと70.3%・つきのひかり28.7%の回復とどくどく63.1%・あくび32.9%で長期戦にも強く、シャドーボールはあく半減・ヘドロウェーブも3発かかるため突破が難しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0003-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フシギバナ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（88.6%）がじめん×2</td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fef3cd;border:1px solid #f59e0b;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>⚠️ 使用率TOP30の半数近くが4弱点の高採用率一致技を持つ</strong><br>
  じめん・ゴースト・エスパー・あくのいずれかを高い採用率で運用する相手が使用率上位に多数存在し、H60・B60〜80の低耐久と合わせて後出しはほぼ通りません。かげふみ・みちづれ・ほろびのうたで先に主導権を握る立ち回りが前提です。
</div>

---

## 得意なポケモン

ゴースト・どくの一致技が刺さり（×2）、かつ相手の主力技がゲンガーの弱点を突かない相手を挙げます。この基準を満たす相手は環境上位では少数のため、苦手表（TOP30まで）より広くTOP30台まで対象を拡大して抽出しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">得意な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリーにヘドロウェーブが×2。主力のムーンフォース等はこちらの弱点を突かない</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0700-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ニンフィア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー単タイプにヘドロウェーブが×2だが、多数派耐久（HP202・D152）では確定2発止まり。主力ハイパーボイス（98.8%）は特性フェアリースキン（99.4%）でフェアリー技になり通るが、34〜41（HP137の24.8〜29.9%）にとどまる。あくび87.8%には注意</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0038-01.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アローラキュウコン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり/フェアリーにヘドロウェーブが×2。主力のオーロラベール等はゲンガーの弱点を突かない</td>
</tr>
</tbody>
</table>
</div>

スターミー（みず/エスパー）はシャドーボールが×2で通る一方、メガ個体の約半数がエスパー技（しねんのずつき27.9%・サイコカッター23.2%）を採用しゲンガーの弱点を突くため一方的な得意とは言えません。マスカーニャ（くさ/あく、使用率3位）もヘドロウェーブ×2で確定1発（174〜205%）を取れますが、多数派の性格ようき（61.1%、非スカーフ時S192）で計算すると、ふいうち（30.9%、優先度+1）はあく×2で128〜152（93.4〜110.9%、乱数1発）、はたきおとす（65.1%、優先度0）もあく×2で120〜144（87.6〜105.1%、乱数1発）です。ふいうちは優先度+1のため速度に関係なく先制できますが、攻撃技以外を選んだ場合は失敗する技で、ゲンガーはまもる（56.5%）・みちづれ（53.7%）を高採用率で持つため過信はできません。こだわりスカーフ採用時（55.2%、S288）ははたきおとすも含めてメガゲンガー（S200）より先に動けますが、非スカーフ個体がはたきおとすを選ぶ場合はS192がS200に届かずゲンガー側が先に動きます。いずれの場合もダメージは乱数1発〜確定1発の範囲にとどまり、一方的な得意とは言えません。

---

## 同居率上位のパートナー

M-5でゲンガーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）のうち、同居率上位で補完が噛み合う2体を解説します。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率5位</div>
  </div>
</div>

同居率上位の**アーマーガア**（ひこう/はがね）はじめん無効を持ち、ゲンガーが被弾を避けたい相手のじめん一致技（前述のガブリアス・カバルドンのじしん等）を受け持てます（ゴーストは等倍のため耐性はありません）。**サザンドラ**は特性ふゆう（採用率100%）でじめん技を無効化でき、ゲンガーの最大の穴であるじめん一致技への後出し役として機能します。ただしサザンドラ自身はフェアリー×4という大きな弱点を抱え、フェアリー使いに対しては共倒れのリスクがあるため、じめん以外の万能な受け役ではない点には注意が必要です。

---

## データ分析：M-4からの変化

M-4シーズンのゲンガーは使用率20位でしたが、M-5では19位に順位を上げています。技採用率を比較すると、行動保証系の技の採用が下がり一致技中心の構成にシフトしていることが分かります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドーボール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">86.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">88.3%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ヘドロウェーブ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">74.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ほろびのうた採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">41.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.5%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こごえるかぜ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">みちづれ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">63.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">53.7%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゲンガナイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">78.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80.6%</td>
</tr>
</tbody>
</table>
</div>

ヘドロウェーブが55.7%→74.6%へ大きく伸びる一方、ほろびのうた・こごえるかぜ・みちづれといった駆け引き系の技はいずれも採用率を下げています。ヘドロウェーブとシャドーボールの一致2枠を確定させ、残り2枠でまもる＋みちづれ・ほろびのうたのいずれかを選ぶという、より攻撃寄りの構成に寄っている変化と読めます。メガ石採用率もM-4の78.2%からM-5は80.6%へ微増し、火力を最大化する方向性が一貫して強まっています。

---

## まとめ

M-5のゲンガーは使用率19位で、メガ石採用率80.6%とシャドーボール（88.3%）・ヘドロウェーブ（74.6%）を軸にした特殊アタッカーが基本コンセプトです。メガ進化でC170、実数値C222（おくびょう時）に達し、特性がかげふみに変わり退場を許さない圧力をかけられます。

- **メガ進化型（80.6%）はC222、非メガのきあいのタスキ型（17.2%）はC182にとどまる**：耐久面の弱さは型によらず共通のため、火力を最大化するメガ進化が多数派という結果になっています
- **じめん・ゴースト・エスパー・あくの4タイプ×2弱点に環境上位の多くが該当**し、ガブリアスのじしんは検算上150〜180%の確定1発。H60・B60〜80の低耐久と合わせて後出しは危険です
- **アシレーヌには一致技が刺さり、弱点も突かれない**ため対面から積極的に打点を通せますが、**ニンフィアは一致技が刺さるものの多数派耐久（HP202・D152）では確定2発止まり**で、あくび87.8%を採用しているため一撃で崩せる相手ではありません
- **M-4からM-5にかけてヘドロウェーブ採用が55.7%→74.6%へ増加**し、駆け引き系の技より一致2枠を優先する攻撃的な構成にシフトしています

高いC実数値とかげふみ・みちづれ・ほろびのうたの駆け引きが武器ですが、4タイプに及ぶ弱点を同居率上位のアーマーガア・サザンドラ等で補いながら運用するのが前提のポケモンです。

---

*関連記事：[メタグロス考察 M-5](/blog/metagross-analysis-m5/)*
