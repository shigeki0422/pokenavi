---
title: '【ポケモンチャンピオンズ】ミミッキュ考察 M-4 シャドークロー増加と積みエース完成形'
description: 'M-4シングルバトルで使用率2位を維持したミミッキュを分析。シャドークロー+5.4pp・トリックルーム-5.8ppの変化が示す積みエース特化の完成形、同居率上昇のカバルドン・新登場のアシレーヌで読むアーキタイプ変化を解説。'
updatedDate: '2026-07-14'
pubDate: '2026-07-14'
heroImage: '../../assets/hero-mimikyu-m4.png'
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
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ（M-4）" />
  <div>
    <h2 style="margin:0 0 8px">ミミッキュ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">2位</strong>（M-3も2位）　特性: <strong>ばけのかわ 100%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-4シーズン時点の集計です

M-4のミミッキュは使用率2位を維持しています。ばけのかわで最初の1発を無効化しつつ、つるぎのまいで積んでからいのちのたま補正の一致技で押し切る「積みエース」として環境上位の一角を占め続けています。M-3からの変化点（技構成・同居率）は後述のデータ分析で解説します。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">90</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:48%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">96</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">476</span>
  </div>
</div>

A90・S96という数値は単体では高くありませんが、ばけのかわで確保したつるぎのまい1積みがA実数値を実質2倍にし、いのちのたまの1.3倍補正と合わせて環境上位を1発で仕留める火力に到達します。

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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はゴースト・はがねの2タイプのみ。かくとう・ノーマル・ドラゴンの3タイプを無効化します。

---

## 主要な技と採用率（M-4）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">M-4採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong>98.2%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かげうち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong>97.5%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong>84.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>シャドークロー</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong>68.0%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>のろい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ウッドハンマー</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">12.5%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ドレインパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>トリックルーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7.0%</td>
</tr>
</tbody>
</table>
</div>

じゃれつく・かげうち・つるぎのまいはほぼ固定枠。4枠目はシャドークロー68.0%が最多で、ウッドハンマー12.5%・ドレインパンチ9.1%が選択肢として続きます。

---

## 主要型の解説

### 型1: いのちのたまAS型（いじっぱり）—最多採用

**性格採用率: いじっぱり 80.7%**

EVはH1-A32-B1-S32（24.9%）とH2-A32-S32（23.4%）が拮抗しており、どちらも実数値の差は誤差範囲内（HP132・A156・S148が共通）。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたまASいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率23.4%）<br>
<strong>持ち物:</strong> いのちのたま（86.7%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく（98.2%）<br>
・かげうち（97.5%）<br>
・つるぎのまい（84.8%）<br>
・<span style="color:#1d4ed8">シャドークロー68.0% / ウッドハンマー12.5%</span>
</div>
</div>
</div>

ばけのかわを盾にしてつるぎのまいを1回積みます。積み後のA実数値は156×2=312相当となり、いのちのたまの1.3倍補正・タイプ一致1.5倍補正を合わせると、4枠目の技選択が確定数に直結します。積み後のじゃれつく（フェアリー90）はドラゴン・あく・かくとうタイプに×2で通り、積み後のシャドークロー（ゴースト70）はみず/フェアリーのアシレーヌのような相手にじゃれつく半減が刺さらない局面で等倍を確保します。

**強み:**

つるぎのまい1積み後のA実数値312相当は、いのちのたま・タイプ一致補正と合わせて環境上位を1発で仕留める火力に到達します。

**弱み:**

S実数値148（いじっぱりS32）を上回るポケモンに対して、ばけのかわ解除後は後手に回ります。S148は環境上位のガブリアスS169、マスカーニャS系統などを抜けないため、積み後でも一致先制技かげうち（優先度+1）で補う場面が増えます。また弱点のはがね技を持つブリジュラス・メタグロスにはじゃれつくが等倍・半減止まりで火力が出づらく、単体での突破は困難です。

---

### 型2: いのちのたまASようき型

**性格採用率: ようき（少数派）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたまASようき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（S162）<br>
<strong>持ち物:</strong> いのちのたま（86.7%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく（98.2%）<br>
・かげうち（97.5%）<br>
・つるぎのまい（84.8%）<br>
・シャドークロー 68.0%
</div>
</div>
</div>

**強み:**

S実数値162で、いじっぱり型のS148より14速い分、S149〜161帯の相手（積み後の優位を作る上で重要なライン）に対してつるぎのまい前から先手を取れます。

**弱み:**

A実数値は142（いじっぱり156より14低い）となり、積み後A284で動くためいじっぱり型積み後A312と比べて同じ相手に確定数が変わる局面があります。

---

### 型3: B振り耐久型（少数派）

**性格採用率: いじっぱり（EV採用率4.5%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">B振り耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H29 A32 B5 S0（4.5%）<br>
<strong>持ち物:</strong> いのちのたま
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく<br>
・かげうち<br>
・つるぎのまい<br>
・シャドークロー
</div>
</div>
</div>

HP159・B105・S116（S無補正かつEV0）。S116と低速のため積みエースとして機能しないように見えますが、H29+B5でばけのかわ解除後の物理耐久を確保し、積みターンを増やす意図があります。S0+いじっぱりのため後手前提で動き、かげうち（優先度+1）で先手処理を補う構成です。

**強み:**

H29+B5でばけのかわ解除後も物理1発で倒されない耐久を確保できます。

**弱み:**

S116と低速のため、積みエースとして先手を取る運用には向きません。

---

## データ分析①：M-3→M-4 採用率変化

| 項目 | M-3 | M-4 | 方向 |
|---|---|---|---|
| シャドークロー | 62.6% | **68.0%** | +5.4pp |
| トリックルーム | 12.8% | **7.0%** | -5.8pp |
| つるぎのまい | 80.8% | **84.8%** | +4.0pp |
| いのちのたま | 84.6% | **86.7%** | +2.1pp |
| いじっぱり | 76.5% | **80.7%** | +4.2pp |
| ゆうかん | 1.2% | 2.3% | 少数維持 |

トリックルームは7.0%・ゆうかんは2.3%まで落ちており、M-4でTR軸として運用されているミミッキュは少数派です。シャドークロー・つるぎのまい・いのちのたま・いじっぱりがすべて同方向に増加していることが、積みエース路線への収束を裏付けています。

---

## データ分析②：シャドークロー+5.4ppの理由

シャドークロー（ゴースト70）はかげうち（ゴースト40）と同じゴースト技ですが、優先度+1の先制効果を持たない通常技です。なぜM-4で5.4pp増えたかを、4枠目候補との相性で整理します。

**4枠目技のタイプ相性比較（M-4環境上位向け）**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1;text-align:left">対象ポケモン</th>
  <th style="padding:8px;border:1px solid #cbd5e1">シャドークロー<br>ゴースト70</th>
  <th style="padding:8px;border:1px solid #cbd5e1">ウッドハンマー<br>くさ120</th>
  <th style="padding:8px;border:1px solid #cbd5e1">ドレインパンチ<br>かくとう75</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">アシレーヌ（みず/フェアリー）</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#16a34a">等倍</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#16a34a">×2（抜群）</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">半減（×0.5）</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">カバルドン（じめん）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">等倍（×1）</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#16a34a">×2</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0530-00.webp" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ドリュウズ（はがね/じめん）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">等倍（×1）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">等倍（はがね×0.5・じめん×2）</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#16a34a">×2（抜群）</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ブリジュラス（はがね/ドラゴン）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">等倍（×1）</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×0.25</strong>（はがね×0.5・ドラゴン×0.5）</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#16a34a">×2</strong>（はがね×2・ドラゴン×1）</td>
</tr>
</tbody>
</table>
</div>

同居率5位のアシレーヌ（みず/フェアリー）に対し、じゃれつく（フェアリー技）はフェアリー×0.5で半減されます。この局面でシャドークロー（ゴースト技）はみず×1・フェアリー×1で等倍、ウッドハンマー（くさ技）はみず×2・フェアリー×1で×2となります。積みじゃれつく（タマ×0.5）129ダメージに対して積みシャドークロー（タマ等倍）は202ダメージ、積みウッドハンマー（タマ・非一致×2）は反動込みでさらに高い打点になり、いずれも対B無振りHP155のアシレーヌを確1で仕留められます。

4枠目の選択は「じゃれつくが通らない相手への補完」という点で共通ですが、ウッドハンマーは自分もダメージを受ける反動デメリットがあります。シャドークローは急所率+1（きゅうしょランク+1）の付加価値に加え、反動なしで安定してアシレーヌやフェアリー複合全般に等倍以上を通せる汎用性が、多数派に選ばれる理由です。

---

## データ分析③：同居率から読むM-4アーキタイプ

同居率TOP10でM-3からの変化が顕著なのは、カバルドン（M-3の6位から3位に上昇）とアシレーヌ（M-4新登場・5位）です。リザードン・マスカーニャは順位を下げつつも10位圏内を維持し、マフォクシー・ゲッコウガ・ギャラドスが新たにTOP10入りしました。

| 同居率順位 | M-3 | M-4 |
|---|---|---|
| 1位 | ガブリアス | ガブリアス |
| 2位 | メタグロス | メタグロス |
| 3位 | ブリジュラス | **カバルドン（↑6→3位）** |
| 4位 | リザードン | ブリジュラス |
| 5位 | マスカーニャ | **アシレーヌ（M-4新登場）** |
| 6位 | カバルドン | リザードン（↓4→6位） |
| 7位 | サザンドラ | マフォクシー（新） |
| 8位 | クチート | ゲッコウガ（新） |
| 9位 | ライチュウ | マスカーニャ（↓5→9位） |
| 10位 | バシャーモ | ギャラドス（新） |

カバルドン（じめん単）はM-4で採用率・同居率がともに上昇しており、ミミッキュとの役割分担が明確です。

**カバルドンとの同居:** カバルドンはすなあらし展開役として敵の特殊アタッカーを砂ダメージで削ります。ミミッキュはばけのかわを活かして物理方面から詰めます。カバルドンのじめん技はミミッキュが苦手なはがね複合（ブリジュラスを除く）への打点になります。

**アシレーヌとの同居:** M-4で新たにTOP5入りしたアシレーヌ（みず/フェアリー）は特殊方面の火力担当です。ミミッキュのじゃれつくがアシレーヌ自身には半減される一方、パーティとしてはタイプの異なる打点を両者で分担できます。

サザンドラ・クチート・ライチュウ・バシャーモがTOP10から外れ、代わってマフォクシー・ゲッコウガ・ギャラドスが新規に入った点は、M-4でミミッキュを採用する構築の相手選びに幅が出たことを示しています。

---

## パートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんでブリジュラス・メタグロスへ打点。ステルスロックでミミッキュの確定数を操作</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでフェアリー技を半減。ミミッキュが苦手な相手に対して別方向から圧力</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位（M-3：6位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">砂嵐展開役。ステルスロック設置でミミッキュが積む前の削りを補助</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンではがね技を半減（×0.5）し耐性補完。ミミッキュの弱点を一部カバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率5位（M-3圏外→M-4新登場）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊方面の火力担当。ミミッキュとタイプ補完しはがね系を共同で対処</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率6位（M-3：4位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお打点でブリジュラス（はがね/ドラゴン）に等倍以上を通す物理・特殊両対応の攻め筋</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率7位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">特殊アタッカーとしてミミッキュの物理打点と役割を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率8位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速アタッカーとして先手を取れない相手をミミッキュの前に処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率9位（M-3：5位）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">スカーフによる対面操作でミミッキュが積む起点を作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率10位（M-4新）</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">物理アタッカーとしてミミッキュと打点を分担</div>
  </div>
</div>

---

## まとめ

M-4のミミッキュは積みエース特化が完成形に近づいたシーズンです。シャドークロー68.0%・つるぎのまい84.8%・いのちのたま86.7%・いじっぱり80.7%が同方向に増加し、「ばけのかわで1積みしてタマ打点で押し切る」運用の多数派としての地位が固まっています。

4枠目の選択がじゃれつくで半減されるアシレーヌへのシャドークロー（等倍）か、カバルドン（じめん単）へのウッドハンマー（×2）かという判断は、選出読みと並んで構築段階での重要な決定事項です。カバルドンとの同居率上昇（M-3の6位→M-4の3位）は、ミミッキュが物理方面から詰める役割を担うパーティ構成が拡大したことを示しています。

---

## 関連記事

- [ミミッキュ M-3 考察](/blog/mimikyu-analysis-m3/)
- [使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [使用率2位 ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)

---

<details>
<summary style="cursor:pointer;color:#64748b;font-size:0.85em">検算済み実数値リスト（Lv50・個体値31・Champions EVスケール）</summary>

```
HP計算: floor((種族値×2+31+EV×2)×50/100)+60
他ステ: floor(floor((種族値×2+31+EV×2)×50/100)+5)×性格補正
（EVはChampions 0-32スケール、式でEV×2として代入）

ミミッキュ（HP55/A90/B80/C50/D105/S96）
  H2-A32-S32 いじっぱり : HP132, A156, S148
  H1-A32-B1-S32 いじっぱり: HP132, A156, B101, S148
  H29-A32-B5-S0 いじっぱり: HP159, A156, B105, S116
  A32 ようき S32        : A142, S162

ガブリアス H2-A32-S32 ようき: HP185, B100, S169
アシレーヌ 無振り: HP155, B94
カバルドン 無振り: HP183, B138
ドリュウズ 無振り: HP185, B80
ブリジュラス 無振り: HP165, B150

ダメージ（積みA312・タマ×1.3・一致×1.5）
  →アシレーヌB無振り じゃれつく×0.5: 129（HP155未満=2発）
  →アシレーヌB無振り シャドークロー等倍: 202（確1）
  →カバルドンB無振り じゃれつく等倍: 176（HP183未満=2発）
  →カバルドンB無振り ウッドハンマー（非一致）×2: 314（確1）
  ゴースト技→カバルドン（じめん単）: 等倍（×1）
```

</details>
</content>
