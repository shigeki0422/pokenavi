---
title: '【ポケモンチャンピオンズ】ミミッキュ 考察 M-7 シーズン 使用率5位の採用型解説'
description: 'M-7シーズン使用率5位のミミッキュを考察。つるぎのまい型、のろい・速攻型、のろい・耐久型の技・持ち物・性格・EVの採用率、ばけのかわの効果、ガブリアス・カイリューなど得意なポケモンとメガリザードンX・メガグソクムシャなど苦手なポケモンをデータで解説します。'
pubDate: '2026-10-25'
updatedDate: '2026-10-14'
heroImage: '../../assets/hero-mimikyu-m7.png'
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
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" />
  <div>
    <h2 style="margin:0 0 8px">ミミッキュ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">5位</strong>　特性: <strong>ばけのかわ 100%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・技・持ち物・性格・特性・EV・同居率はすべて2026-10-11時点の実測データに統一しています。

M-7シーズンのミミッキュは使用率5位です。ゴースト/フェアリーの複合タイプに特性ばけのかわを持ち、じゃれつく・かげうちを中核とした攻撃型が主軸です。

---

## ミミッキュの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:64%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">96</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">476</span>
  </div>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

### 特性

HP55という低い種族値を補うのが特性<strong>ばけのかわ</strong>です。ばけたすがたの状態で技のダメージを受けると、ダメージの代わりに最大HPの1/8を消費してばれたすがたへ変わり、1発目のダメージだけを無効化します。連続技の2発目以降には通常どおりダメージが入ります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じゃれつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー一致のメインウェポン。低確率で相手の攻撃を1段階下げる追加効果もある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1でゴースト一致。相手が素早さで勝っていても先に動ける先制技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">77.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃を2段階上昇。ばけのかわで1発無効化しつつ積む隙を作るのに使う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドークロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">急所ランク+1でゴースト一致。かげうちより高火力だが優先度は通常</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウッドハンマー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・じめん・いわタイプへの弱点を突く打点だが、与えたダメージの1/3を自分も受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のろい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の最大HPの1/2を消費し、相手をのろい状態にする（のろい状態の相手は毎ターン最大HPの1/4のダメージを受ける）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリックルーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-7。5ターンの間、場の素早さ順を逆転させる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドレインパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">非一致のかくとう打点で、相手に与えたダメージの1/2を回復できる技。ルカリオには弱点（かくとう×2）として刺さりますが、サーフゴー・ギルガルドのはがね/ゴースト複合には無効（かくとう×0）です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をやけど状態にする。物理アタッカーの攻撃力を実質半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みちづれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分がみちづれ状態になる技。この状態中に自分が倒されると、倒した相手も道連れにして同時に倒す（連続使用は失敗する）</td>
</tr>
</tbody>
</table>
</div>

---

## M-7の採用型

じゃれつく（98.0%）・かげうち（96.8%）はほぼ全個体が採用する中核技です。残り2枠は、つるぎのまい・シャドークローを使う積みアタッカーのつるぎのまい型と、のろい・トリックルームを使うのろい・速攻型／のろい・耐久型に分かれます。のろい・速攻型はEV配分H2-A32-S32で素早さに重点を置き、のろい・耐久型はH28-A30-B6-S2でHP・ぼうぎょに重点を置いています。

### 型1：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> いのちのたま
</div>
<div>
<strong>技構成:</strong><br>
・かげうち<br>
・じゃれつく<br>
・つるぎのまい<br>
・シャドークロー
</div>
</div>
</div>

A実数値156・S実数値148の構成で、選択候補にはウッドハンマー・ドレインパンチ・のろいもあります。つるぎのまいを1回使うとA実数値312相当まで火力を伸ばせます。

**強み:**

つるぎのまいで自分のこうげきを2段階上昇させられるため、他の2型にはない最大火力を出せます。

**弱み:**

のろい・トリックルームを持たないため、素早さ操作や継続ダメージの手段がありません。

---

### 型2：のろい・速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">のろい・速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> いのちのたま
</div>
<div>
<strong>技構成:</strong><br>
・かげうち<br>
・じゃれつく<br>
・のろい<br>
・トリックルーム
</div>
</div>
</div>

A実数値156・S実数値148の構成です。選択候補にはウッドハンマー・シャドークロー・ドレインパンチもあります。

**強み:**

のろい・トリックルームで素早さを操作できます。S実数値148は型3（のろい・耐久型、S実数値118）より30高く、トリックルームを使う前でも先に動ける相手が多くなります。<!-- gate:allow 30 reason="型2のS実数値148と型3(のろい・耐久型)のS実数値118の差分(148-118)" -->

**弱み:**

つるぎのまいを持たないため積み技による大幅な火力上昇はなく、型3よりHP・ぼうぎょの投資も低くなっています。

---

### 型3：のろい・耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">のろい・耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H28-A30-B6-S2<br>
<strong>持ち物:</strong> いのちのたま
</div>
<div>
<strong>技構成:</strong><br>
・かげうち<br>
・じゃれつく<br>
・のろい<br>
・トリックルーム
</div>
</div>
</div>

H158・A154・B106・S118の構成です。素早さへの投資をH・Bに回しているため、各型の代表個体で比べると、つるぎのまい型、のろい・速攻型（いずれもいじっぱり・H132・B100・S148）よりH+26・B+6高い一方、S実数値は30低くなります。<!-- gate:allow 30 reason="事実シートのS実数値148(つるぎのまい型/のろい・速攻型)とS実数値118(のろい・耐久型)の差分(148-118)" -->

**強み:**

HPに厚く投資しているため、物理・特殊の両方で他の2型より耐える個体です。

**弱み:**

トリックルームを張る前はS実数値118で、つるぎのまい型・のろい・速攻型より遅く、後手に回りやすい構成です。

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=926dbb39045b133517f6e2be5fd9b78a73078fe2 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">のろい・速攻型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">のろい・耐久型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（しんちょう・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（いじっぱり・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（むじゃき・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△※</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体5件は除く。ゴリランダーは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの採用傾向の変化

ミミッキュの使用率は、M-6シーズン終盤（2026-09-23時点）の**11位**から、M-7シーズン（2026-10-11時点）では**5位**まで上昇しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6終盤（2026-09-23）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7（2026-10-11）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">差分</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じゃれつく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">96.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">98.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かげうち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">96.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-4.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シャドークロー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">63.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">57.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-6.1pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ウッドハンマー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">22.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+6.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+2.4pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">トリックルーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+4.7pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ドレインパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.8pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おにび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-1.6pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物・性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6終盤（2026-09-23）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7（2026-10-11）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">差分</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-1.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">のろいのおふだ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+3.2pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゴツゴツメット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いじっぱり（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">78.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">83.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+5.8pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ようき（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-5.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゆうかん（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+1.2pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=926dbb39045b133517f6e2be5fd9b78a73078fe2 -->
- ウッドハンマー：15.1%→22.0%（+6.9pt）。つるぎのまい型、のろい・速攻型に共通 → 型の増減とは言えない
- シャドークロー：63.4%→57.3%（-6.1pt）。つるぎのまい型、のろい・耐久型に共通 → 型の増減とは言えない
- いじっぱり：78.1%→83.9%（+5.8pt）。つるぎのまい型、のろい・耐久型、のろい・速攻型に共通 → 型の増減とは言えない
- ようき：16.8%→11.5%（-5.3pt）。のろい・速攻型の個体が採用
- トリックルーム：5.2%→9.9%（+4.7pt）。のろい・耐久型、のろい・速攻型に共通 → 型の増減とは言えない
- つるぎのまい：81.6%→77.4%（-4.2pt）。つるぎのまい型だけが持つ → その型の増減を示す
- のろいのおふだ：2.8%→6.0%（+3.2pt）。この記事の型の技構成には含まれない
<!-- gate:rows end id=diff_movers -->

この使用率上昇の期間に、技ではウッドハンマー・トリックルーム・のろいの採用が、持ち物ではいじっぱり性格・のろいのおふだの採用が広がっています。

持ち物のろいのおふだ（2.8%→6.0%、+3.2pt）は、ゴースト技の威力を1.2倍にする効果があります。<!-- gate:allow 1.2倍 reason="エンジン実装のsymsテーブルでのろいのおふだのゴースト技補正値を確認済み" --> 採用率80.2%のいのちのたまは攻撃のたびに自分も反動を受けますが、のろいのおふだはゴースト技に限って威力を上げる代わりに反動がなく、かげうち・シャドークローと組み合わせて採用が広がっています。

いじっぱり個体（つるぎのまい型・のろい・速攻型）はA実数値156・S実数値148、のろい・耐久型のいじっぱり個体はS実数値118です。ようき個体はA実数値142・S実数値162で、いじっぱり個体では後手になるメガカイリュー（S152）にも先手を取れる速さです。ようきの採用率は16.8%から11.5%（-5.3pt）に減っており、メガカイリューより先に動ける個体の比率が下がったことを示します。

---

## 苦手なポケモン

使用率上位30体程度を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、相手の型が変わっても勝敗が変わらない相手のみを掲載します。<!-- gate:allow 20% reason="spec.majority_pct=20(事実シート冒頭の多数派しきい値)を手順説明文で参照" -->

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
<!-- gate:rows start id=weak facts=926dbb39045b133517f6e2be5fd9b78a73078fe2 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX32.3%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。メガリザードンXのフレアドライブ（採用率31.4%）は確定2発（ばけのかわ込み）で、S148対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発。メガリザードンYのかえんほうしゃ（採用率43.5%）は確定2発で、S148対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい・速攻型の選択技シャドークローは乱数4発（45%）。メガグソクムシャのふいうち（採用率79.9%）は確定4発（ばけのかわ込み）で、優先度+1のふいうちで先に動かれ、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定4発。アーマーガアのブレイブバード（採用率28.4%）は確定3発（ばけのかわ込み）で、S148対S78で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発。メガメタグロスのサイコファング（採用率75.7%）は確定2発（ばけのかわ込み）で、S148対S162で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。メガギャラドスのじしん（採用率67.5%）は確定2発で、S148対S219で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">フラエッテ(永遠)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。メガフラエッテのムーンフォース（採用率96.9%）は確定2発（ばけのかわ込み）で、S148対S169で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定5発。ヒートロトムのオーバーヒート（採用率94.6%）は乱数3発（88%）（ばけのかわ込み）で、S148対S106で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=weak -->
</tbody>
</table>
</div>

---

## 得意なポケモン

同じ基準で掲載します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<!-- gate:rows start id=strong facts=926dbb39045b133517f6e2be5fd9b78a73078fe2 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは乱数1発（81%）。ガブリアスのじしん（採用率68.1%）は確定2発（ばけのかわ込み）で、S148対S253で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技ウッドハンマーは確定2発。アシレーヌのうたかたのアリア（採用率75.3%）は確定2発（ばけのかわ込み）で、S148対S80で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発。サーフゴーのシャドーボール（採用率97.8%）は乱数2発（88%）で、S148対S114で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。メガセグレイブのつららおとし（採用率57.3%）は確定2発で、S148対S139で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは乱数1発（81%）。イダイトウ(オス)のおはかまいり（採用率99.9%）は確定2発で、S148対S214で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。カイリューのじしん（採用率28.5%）は確定2発（ばけのかわ込み）で、S148対S114で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発（相手のきあいのタスキ込み）。ゲンガーのシャドーボール（採用率84.5%）は確定2発（ばけのかわ込み）で、最後は優先度+1のかげうちで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定1発。メガライチュウYのでんじほう（採用率97.1%）は乱数2発（94%）で、S148対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型の選択技ウッドハンマーは確定1発。メガゲッコウガのみずしゅりけん（採用率48.9%）は乱数2発（45%）で、S148対S213で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カメックス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは乱数2発（91%）。メガカメックスのあくのはどう（採用率84.1%）は確定3発（ばけのかわ込み）で、S148対S130で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発。オオニューラのじごくづき（採用率50.9%）は確定3発で、S148対S146で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじゃれつくは確定2発。ブラッキーのイカサマ（採用率98.1%）は確定2発（ばけのかわ込み）で、S148対S85で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のシャドークローは確定2発。ギルガルドのポルターガイスト（採用率76.4%）は確定2発（ばけのかわ込み）で、S148対S112で先手を取り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

使用率上位には、ブリジュラス（3位）・カバルドン（4位）・ルカリオ（7位）・ボーマンダ（10位）・キラフロル（16位）・イエッサン(オス)（17位）・ゴリランダー（18位）・マスカーニャ（19位）・エースバーン（20位）も含まれますが、相手の型（個体）によって勝敗が変わるため、苦手/得意いずれの表にも掲載していません。

---

## 同居率上位の分析

M-7でミミッキュと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=926dbb39045b133517f6e2be5fd9b78a73078fe2 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガリザードンY<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガメタグロス<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガルカリオZ<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガグソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガカイリュー<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュの弱点：はがね技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュの弱点：ゴースト技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX・メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">グソクムシャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">フラエッテ(永遠)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎2・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎2・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ミミッキュの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンX・メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；グソクムシャ＝ふいうち・きゅうけつ・アイアンヘッド・インファイト；アーマーガア＝とんぼがえり・ボディプレス・アイアンヘッド；メタグロス＝バレットパンチ・サイコファング・れいとうパンチ・じしん・かみなりパンチ；ギャラドス＝じしん・パワーウィップ・たきのぼり・ゆきなだれ・こおりのキバ；フラエッテ(永遠)＝ムーンフォース・ドレインキッス；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

M-7のミミッキュは使用率5位で、M-6終盤（2026-09-23時点、11位）から大きく順位を上げました。

- **じゃれつく・かげうちは固定、残り2枠で型が分岐**：じゃれつく98.0%・かげうち96.8%はほぼ全個体が採用する一方、残り2枠は積み技を使うつるぎのまい型と、のろい・トリックルームを使うのろい・速攻型／のろい・耐久型に分かれます
- **M-6からつるぎのまいの採用率が減少**：つるぎのまいの採用率は81.6%から77.4%（-4.2pt）に減り、ミミッキュの中でのつるぎのまい型の比率が下がりました。一方でトリックルーム（+4.7pt）・のろい（+2.4pt）は増加しています
- **得意・苦手の傾向**：ガブリアス・カイリュー・サーフゴー・ブラッキーなど環境上位の複数体を先に倒せる一方、メガリザードンX/Y・メガメタグロス・メガグソクムシャなどには先に倒されます

関連記事: [ミミッキュ M-6シーズン考察](/blog/mimikyu-analysis-m6/)、[ガブリアス M-7シーズン考察](/blog/garchomp-analysis-m7/)、[メガボーマンダ M-6シーズン考察](/blog/salamence-analysis-m6/)
