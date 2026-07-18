---
title: '【ポケモンチャンピオンズ】メガゲンガー 考察 M-4 シーズン かげふみ+ほろびのうたロック'
description: 'M-4シーズン使用率18位のメガゲンガー考察。ゲンガナイト採用率78.2%でメガ運用が主流に。かげふみで交代を封じてほろびのうた・みちづれで詰ませる型と、シャドーボール・ヘドロウェーブの一致特殊型のデータを分析します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-gengar-m4.png'
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
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" />
  <div>
    <h2 style="margin:0 0 8px">メガゲンガー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">18位</strong>（M-3: 29位）　持ち物: <strong>ゲンガナイト 78.2%</strong>
    </div>
  </div>
</div>

M-4シーズン、ゲンガーは使用率18位につけています。ゲンガナイト採用率78.2%とメガ運用がほぼ前提で、メガ進化後は特性が**かげふみ**（ゴースト以外の相手を交代不可にする）に変わります。相手を交代封じした状態でほろびのうた・みちづれを絡めて詰ませる型と、シャドーボール・ヘドロウェーブの一致特殊技で殴る型の2系統が採用されています。

---

## メガゲンガーの基本スペック

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
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:85%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">500</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でとくこう170（+40）・すばやさ130（+20）と特殊アタッカーとしての数値が伸び、ぼうぎょ・とくぼうも+20ずつ上昇します。特性は**のろわれボディ**から**かげふみ**（ゴースト以外の相手が交代できなくなる）に変化します。

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
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はじめん・エスパー・ゴースト・あくの4タイプ（いずれも×2）。ノーマル・かくとう無効を含め、むし・どくを¼で受けられる耐性の広さが特徴です。ただし環境上位はこの4弱点タイプの技を高採用率で持つ相手が多く、1位ガブリアスのじしん（じめん）99.5%、2位ミミッキュのかげうち（ゴースト）97.5%、13位サザンドラのあくのはどう（あく）99.3%が代表的な脅威です。

### 特性

メガ進化前は**のろわれボディ（100%）**が固定。相手の技を受けるたびに30%の確率で4ターンの間その技をわざふうじ状態にします。メガ進化後は**かげふみ**に変わり、ゴースト以外の相手を交代不可にします（ミミッキュ等ゴーストタイプの相手はこの効果を受けません）。かげふみは後述のほろびのうた・みちづれと組み合わせる型の前提になる特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト一致。両型共通のメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みちづれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分が倒れた場合に相手も道連れ。ほろびのうたを通す前の保険</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致。フェアリー・くさへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1ターン攻撃を防ぐ。ほろびのうたのカウントを稼ぐロック型の要</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほろびのうた</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>41.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">場の全員が3ターン後に瀕死。かげふみで交代を封じた相手に通す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こごえるかぜ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の素早さダウン。アタッカー型で後続の速度優位を作る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やけど付与で物理アタッカーを機能不全にする補助技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう打点。カバルドン等のあく/じめんへのカバー範囲拡大</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たたりめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">状態異常の相手に威力2倍。おにび併用個体で採用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき打点。アーマーガア等のひこう複合への打点確保</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：ほろびのうた・みちづれロック型（おくびょう 83.7%）

**性格採用率: おくびょう 83.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="メガゲンガー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ほろびのうた・みちづれロック型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（100%）→メガ後かげふみ<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> ゲンガナイト（78.2%）
</div>
<div>
<strong>技構成:</strong><br>
・ほろびのうた<br>
・みちづれ<br>
・まもる<br>
・シャドーボール（ヘドロウェーブ）
</div>
</div>
</div>

かげふみで相手をゴースト以外交代不可にした状態でほろびのうた（場の全員がほろび状態になり3ターン後に瀕死）を宣言し、まもるでこちらへの攻撃を防ぎながらカウントを進める型です。相手はかげふみで逃げられないため、ほろびのうたのカウントが尽きると強制的に瀕死になります。みちづれは自分がその場で倒された場合に相手も道連れにする技で、ほろびのうたを通す前に相手の攻撃で先に倒された場合の保険として機能します。

**強み:**

H137 / A76 / B100 / C222 / D115 / S200（おくびょう H2-C32-S32）。S200は環境上位のガブリアス（ようき最多採用個体S169）・ミミッキュ（いじっぱり最多採用個体S148）を上回り、まもる・ほろびのうたを先に通しやすい速度です。

**弱み:**

まもるは連続で使うと成功率が前回使用時の1/3に下がるため、複数回連続でまもるを通す運用はできません。ほろびのうたを宣言してから3ターンの間、味方の場作りが必要になります。

---

### 型2：一致特殊アタッカー型（ひかえめ 14.7%）

**性格採用率: ひかえめ 14.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0094-00.webp" alt="メガゲンガー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">一致特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> のろわれボディ（100%）→メガ後かげふみ<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H18-C13-D3-S32（代表例）<br>
<strong>持ち物:</strong> ゲンガナイト
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ヘドロウェーブ<br>
・こごえるかぜ<br>
・きあいだま（10まんボルト）
</div>
</div>
</div>

シャドーボール（ゴースト・威力80）とヘドロウェーブ（どく・威力95）の一致技2種に加え、こごえるかぜ（こおり・威力55・採用率23.2%）で相手の素早さを下げ、S182では上から動けない相手にも後手を取りにくくする構成です。3枠目以降はきあいだま（かくとう・採用率10.2%）や10まんボルト（でんき・採用率7.3%）でカバー範囲を広げる選択肢もあります。ロック型と違いまもる・みちづれを積まず、毎ターン攻撃で押していく運用になります。

**強み:**

H153 / A76 / B100 / C223 / D118 / S182（ひかえめ H18-C13-D3-S32）。C223はロック型（C222・むじゃき想定なし）とほぼ同等ながらHPが153とロック型のH137より高く、被弾しても行動しやすい耐久があります。

**弱み:**

S182はロック型のS200より低く、マフォクシー（メガ後最速想定S204）に上から動かれます。かげふみで交代不可にはできても、行動順で後手に回るため先制で削られる展開があります。

---

## データ分析①：M-3→M-4 採用データの変化

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>18位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲンガナイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">82.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">78.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong>採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+33.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みちづれ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>63.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+18.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほろびのうた</strong>採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">41.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">82.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-26.5pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいだま採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-28.0pp</strong></td>
</tr>
</tbody>
</table>
</div>

M-4最大の変化は**ほろびのうたの新規台頭（41.6%）**と、それに伴う**まもる（+33.8pp）・みちづれ（+18.2pp）**の伸びです。ヘドロウェーブはM-3時点で既に82.2%の主力技として確立していましたが、M-4ではほろびのうた・まもるに枠を譲る形で55.7%まで下がり、同様にきあいだま（38.2%→10.2%）も大きく採用を落としています。かげふみで交代封じした相手にほろびのうたを通し、まもるでカウントを稼ぐロック型が新たに確立したことで、既存の一致打点技（ヘドロウェーブ・きあいだま）の採用機会がその分削られた構図です。使用率が29位から18位へ上昇した時期と、このロック型の採用率上昇が重なっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率99.5%）が×2弱点。持ち物はきあいのタスキ39.2%・オボンのみ23.2%が主流でスカーフは19.8%に留まるため、メガ後S200のゲンガーが先に動ける場面が多いものの、じしん1発の被ダメージが大きく打ち合いには向きません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（ゴースト・採用率97.5%）・シャドークロー（ゴースト・採用率68.0%）が×2弱点。ゴーストタイプのためかげふみで交代を封じられません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率98.4%）が×2弱点。オボンのみ61.9%・たべのこし35.7%の耐久型が多く、シャドーボール・ヘドロウェーブでも高耐久を崩しきれません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率99.3%）が×2弱点。こだわりスカーフ84.2%が主流で、EV最多分布のS32・ひかえめ採用時でもスカーフ込みでS225となりゲンガーのS200を上回るため、先制であくのはどうを受けます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス（エスパー・採用率56.7%）・サイコショック（エスパー・採用率39.7%）が×2弱点。マフォクシナイト99.1%でメガ運用が前提のためメガ後S204（最速想定）がゲンガーのメガ後S200を上回り、先制でエスパー技を受けます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でゲンガーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0503-00.webp" alt="ダイケンキ" loading="lazy">
    <div class="name">ダイケンキ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0939-00.webp" alt="ハラバリー" loading="lazy">
    <div class="name">ハラバリー</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" loading="lazy">
    <div class="name">スターミー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン" loading="lazy">
    <div class="name">エルフーン</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、じしん99.5%の物理打点で相手を崩す役割を担います。ステルスロック49.6%が場を整え、ゲンガーがかげふみで交代を封じた相手にほろびのうたを通す運びを後押しします。

**アーマーガア**（2位）ははがね/ひこうで、ゲンガーの弱点であるじめんタイプの技をひこう耐性で無効化できます。アーマーガアのてっぺき・ボディプレスで受け出しを担い、ゲンガーは相手の交代を封じてほろびのうたで詰める役割分担です。

**アシレーヌ**（3位）はみず/フェアリーで、ゲンガーの弱点であるあく・じめん・ゴーストへの打点は持ちませんが、ムーンフォース（フェアリー）で別方向の相手を処理する役割分担です。

**ダイケンキ**（4位）はみず単タイプで、ひけん・ちえなみでゲンガーとは異なる範囲の相手に打点を持ち、攻めの手数を分担します。

**ハラバリー**（5位）はでんき単タイプで、みず・ひこうタイプの相手にでんき打点を持ちます。

**カバルドン**（6位）はあくびとステルスロックのサポート役です。あくびで相手の交代を強制し、ゲンガーがメガ進化してかげふみを起動する対面を作りやすくします。

---

## まとめ

M-4のゲンガーは使用率29位から18位へ順位を上げ、ゲンガナイト採用率78.2%とメガ運用がほぼ前提のシーズンです。

- **まもる（+33.8pp）・ほろびのうた（新台頭41.6%）が採用率を伸ばした**：かげふみで相手を交代封じし、ほろびのうたのカウントをまもるで稼いで詰める「ロック型」がM-4で確立
- **既存の一致打点技はロック型に枠を譲り採用減**：ヘドロウェーブ（82.2%→55.7%）・きあいだま（38.2%→10.2%）がともに大きく採用を落とし、まもる・ほろびのうたに置き換わった
- **弱点はじめん・エスパー・ゴースト・あくの4タイプ**：環境上位のガブリアス・サザンドラ・マフォクシーが該当タイプの技を高採用率で持つため、これらへの一貫した打点は乏しい

かげふみによる交代封じは、ロック型・アタッカー型どちらの構成でも相手の逃げ道を断つ役割として機能します。型を選ぶ際は、まもる・ほろびのうたで詰めるロック型のS200か、被弾に強いH153の特殊アタッカー型かをパーティの役割に応じて判断する必要があります。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
