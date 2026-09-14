---
title: '【ポケモンチャンピオンズ】アブソル 考察 M-6 シーズン 使用率31位のメガアブソルZ解説'
description: 'M-6シーズン使用率31位のアブソル考察。メガストーンはアブソルナイトZ採用率98.5%が主流で、素種族値A130・S75からA154・S151まで伸びるメガアブソルZの種族値・タイプ変化・技採用率・型構成に加え、使用率上位ポケモンとの苦手/得意関係をデータで解説します。'
pubDate: '2026-09-14'
updatedDate: '2026-09-14'
heroImage: '../../assets/hero-absol-m6.png'
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
  <img src="/images/pokemon/pokemon-0359-00.webp" alt="アブソル" />
  <div>
    <h2 style="margin:0 0 8px">メガアブソルZ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">31位</strong>　持ち物: <strong>アブソルナイトZ 98.5%</strong>
    </div>
  </div>
</div>

M-6シーズン、アブソルは使用率31位です（本記事のデータは2026-09-10時点のものです）。アブソルにはアブソルナイト・アブソルナイトZという2種類のメガストーンが実装されていますが、採用率はアブソルナイトZが98.5%、アブソルナイトが1.0%と大差がついており、本記事は主流のアブソルナイトZ（以下メガアブソルZ）を軸に解説します。メガアブソルZはタイプがあく/ゴーストに変化し、攻撃・素早さが大きく伸びる高速アタッカーです。

---

## アブソルの基本スペック

### 種族値

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
      <div style="width:33%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+24</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">75</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+76</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">465</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガアブソルZへの進化で伸びるのはこうげき（+24）とすばやさ（+76）のみで、ぼうぎょ・とくこう・とくぼうは変化しません（合計+100）。タイプもあく単からあく/ゴーストに変わります。本記事の苦手/得意判定は、主流のようきEV32構成（S種族値151→S実数値223）を基準にしています（いじっぱり構成との比較は後述の型カード部分を参照してください）。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

メガ進化前のあく単はかくとう・むし・フェアリーに×2弱点でしたが、メガ進化後のあく/ゴーストではノーマル・かくとうが無効化され、むし弱点も等倍まで解消されます。一方でゴーストタイプが乗ったことで、通常あく単で半減できていたゴースト・あく技への耐性は失われ等倍になります。フェアリー×2は進化後も変わらず最大の弱点です。M-6上位ではミミッキュ（12位）のじゃれつく採用率98.1%、ニンフィア（29位）のハイパーボイス採用率99.3%、アシレーヌ（3位）のムーンフォース採用率99.1%が主な脅威になります。加えてあく/ゴースト複合は上記の通りフェアリー×2弱点が残るうえゴースト・あく技への耐性を失っているため、種族値の耐久が低いことも合わさって受け出しの安定感は高くありません。

### 特性

通常特性は**せいぎのこころ（65.5%）**で、あくタイプの技を受けるとこうげきが1段階上がる効果ですが、メガ進化すると特性は固定で**きれあじ**に切り替わります。きれあじは「切る技の威力が1.5倍になる」特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドークロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">91.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きゅうしょアップ+1で攻撃するゴースト一致最大打点。全採用技の中で最多。きれあじ対象で威力1.5倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">69.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1のあく一致先制技。相手が攻撃技を選んでいる場合のみ成功する。きれあじ対象外</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">技構成の中で最大威力のサブウェポン。使用後ぼうぎょ・とくぼうが1段階下がる。きれあじ対象外</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきを2段階上げる積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つじぎり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">48.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きゅうしょアップ+1のあく一致技。インファイトの代わりに採用される選択技。きれあじ対象で威力1.5倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコカッター</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きゅうしょアップ+1のエスパー技。かくとうタイプへのサブウェポン。きれあじ対象で威力1.5倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じゃれつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうタイプへのサブウェポン。10%で相手のこうげきを1段階下げる。きれあじ対象外</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の低威力先制技。威力40と低いが確実に先制打点を出せる。きれあじ対象外</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型：メガアブソルZ 物理アタッカー型

**性格採用率: ようき 61.3% / いじっぱり 35.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0359-00.webp" alt="メガアブソルZ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガアブソルZ 物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいぎのこころ（通常時65.5%）※メガ後きれあじ<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（最多分布31.1%）<br>
<strong>持ち物:</strong> アブソルナイトZ（98.5%）
</div>
<div>
<strong>技構成:</strong><br>
・シャドークロー<br>
・ふいうち<br>
・インファイト<br>
・つるぎのまい
</div>
</div>
</div>

シャドークロー（ゴースト・急所アップ+1）を一致最大打点に据え、優先度技のふいうちで素早さで上回れない相手にも先に打点を通し、インファイトではがね・あく・いわ等への打点を補います。つるぎのまいの採用率は63.0%と高く、積んでから畳みかける運用も主流の一角です。

**強み:**

S223（ようき・EV32）はメガガブリアスZ・メガルカリオZ（いずれもS223）と並ぶ環境最速帯で、多くの相手に対して先手を取れます。優先度技のふいうちを併用すれば、素早さで上回れない相手にも先に打点を通せます。ただしマスカーニャ（S262）はこだわりスカーフ採用が過半数を占め、エースバーンもスカーフ運用が一定数存在するため、これらに対してはふいうちなしでは後手に回ります。

**弱み:**

こうげきをA206（ようき・EV32）に留めているため、A226まで伸びるいじっぱり構成と比べると確定数で劣る場面があります。

なお性格別では、S223のようき（61.3%）が最多ですが、A226まで伸ばすいじっぱり（35.6%、S203）も一定数採用されています。技構成はどちらも同じ（シャドークロー軸）で、性格差はS223とA226のどちらを優先するかの違いに留まるため、本記事では型カードを1つに統合しています。いじっぱり構成はS203となり、S223前提の本記事の苦手/得意判定より後手を取られる相手が増える点に注意してください。

---

## データ分析①：主力シャドークローはきれあじでどこまで火力を伸ばせるか

きれあじは「切る技の威力を1.5倍にする」特性です。この特性が対象とする「切る技」はゲーム内共通で決められた技リストであり、シャドークロー・つじぎり・サイコカッター・シザークロスなどが該当します。一方、インファイト・ふいうち・かげうち・じゃれつくはこのリストに含まれず、きれあじの恩恵を受けません。

アブソルの採用技を照らし合わせると、採用率91.0%で最多のシャドークローはきれあじ対象で、素の威力70が実質105相当まで伸びます。対して採用率2位のインファイト（威力120、67.5%）や、優先度技のふいうち（威力70、69.7%）・かげうち（威力40、10.6%）はいずれもきれあじの対象外で、素の威力のまま運用されます。

さらにシャドークローはアブソルのゴースト一致技でもあるため、タイプ一致1.5倍も上乗せされます。きれあじ（×1.5）と一致（×1.5）の両補正込みで実質157.5相当（70×1.5×1.5）となり、ここで初めて素の威力120のインファイト（かくとうタイプでアブソルとタイプ一致せず、補正なしの120のまま）を上回ります。インファイトは威力こそ高いものの追加効果でぼうぎょ・とくぼうが下がるデメリットもあり、両補正が重なるシャドークローがメガアブソルZの主力打点として選ばれていると考えられます。じゃれつく（90）はかくとう方面へのサブウェポン、つじぎり（70、きれあじ対象・あく一致）はインファイトと択になるあく一致技として採用されていますが、いずれも採用率は伸び悩んでおり、シャドークロー軸の構成が主流であることがわかります。

---

## 苦手なポケモン

使用率上位から、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。今回判定した範囲では苦手18体・得意6体となり、苦手側が多数を占めます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取っても確定2発止まりで、メガ・スカーフ型のガブリアスにはこちらが先にりゅうせいぐん（採用率28.6%、最多採用のじしん67.6%とは別の選択技）の確定1発で倒されます（きあいのタスキ型のガブリアスには先手を取れます）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発と決め手を欠き、ボーマンダの主力すてみタックル（採用率73.4%）の確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。アシレーヌの主力ムーンフォース（採用率99.1%、フェアリー×2）の確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発と決め手を欠き、グソクムシャの主力であいがしら（採用率83.0%）の確定1発で先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発と耐久を崩しきれず、カバルドンの主力じしん（採用率99.3%）の確定2発で先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもインファイト（採用率67.5%）は確定3発止まり。ブリジュラスの主力りゅうせいぐん（採用率65.3%）の確定2発に先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもインファイト（採用率67.5%）は確定2発止まり。セグレイブの一致技きょけんとつげき（採用率79.8%）の確定1発で返り討ちに遭います</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。ゴリランダーの主力ドラムアタック（採用率39.1%）の確定1発で先に倒されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。ミミッキュの主力じゃれつく（採用率98.1%、フェアリー×2）の確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発止まり。アーマーガアの主力ブレイブバード（採用率37.6%）の確定2発に先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発止まり。ギャラドスの主力たきのぼり（採用率63.1%）の確定2発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。メガリザードンXの主力フレアドライブ（採用率36.5%）の確定1発で先に倒されます（リザードンはメガストーン採用率がリザードナイトY 60.6%・リザードナイトX 37.6%で分かれており、この行はリザードナイトX採用時を指します）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。メガリザードンYの主力かえんほうしゃ（採用率42.9%）の確定1発で先に倒されます（リザードナイトY採用率60.6%が主流の型です）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取っても確定2発止まりで、かえんボール（採用率98.7%）の確定1発で倒されます（こだわりスカーフ型のエースバーンには後手）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発止まり。アローラキュウコンの主力ムーンフォース（採用率47.1%、フェアリー×2）の確定2発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定3発止まり。カイリューの主力りゅうせいぐん（採用率50.8%）の確定2発に先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。パーモットの主力でんこうそうげき（採用率85.1%）の確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもシャドークロー（採用率91.0%）は確定2発止まり。ニンフィアの特性フェアリースキンでフェアリータイプ化したハイパーボイス（採用率99.3%、フェアリー×2）の確定1発で先に倒されます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率上位から、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています。イエッサン(オス)は使用率35位ですが、判定対象に含めた範囲で一貫して有利になったため掲載しています）。

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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってシャドークロー（採用率91.0%）で確定1発。サーフゴーの主力ゴールドラッシュ（採用率94.3%）も確定1発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってシャドークロー（採用率91.0%）で確定1発。イダイトウの主力ウェーブタックル（採用率96.5%）も確定1発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってインファイト（採用率67.5%）で確定2発。ゲッコウガの主力れいとうビーム（採用率92.9%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってシャドークロー（採用率91.0%）で確定2発。オオニューラの主力じごくづき（採用率59.9%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってシャドークロー（採用率91.0%）で確定2発。ラウドボーンの主力フレアソング（採用率99.4%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってつじぎり（採用率48.1%）で確定2発。イエッサン(オス)の主力マジカルシャイン（採用率70.2%）も確定2発ですが、先制で押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でアブソルと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、一致技じしんはでんき・はがねタイプに×2で通ります。アブソルのシャドークロー・ふいうちはいずれもでんき・はがねに等倍止まりのため、ガブリアスが攻撃面で補える組み合わせです。

**アシレーヌ**（2位）や**ボーマンダ**（4位）はいずれもアブソルの苦手リストに入る相手で、直接の相性補完というよりは環境上位への対応を分担する構成として選ばれていると考えられます（[ボーマンダの考察記事](/blog/salamence-analysis-m6/)も参照）。

**カバルドン**（3位）はじめん単タイプで、ステルスロックやあくびのサポートを担い、アブソルが押し切れない相手に設置技で圧力をかけられます（詳細は[カバルドンの考察記事](/blog/hippowdon-analysis-m6/)）。

同居率9位の**グソクムシャ**もアブソルの苦手相手の一つですが、メガ進化後のかたいツメ運用で高い制圧力を持つため、アブソルが崩せない相手をグソクムシャ側で受け持つ構図と考えられます（詳細は[グソクムシャの考察記事](/blog/golisopod-analysis-m6/)）。

---

## まとめ

M-6のアブソルは使用率31位で、メガストーンはアブソルナイトZ（採用率98.5%）が主流です。

- **メガアブソルZは高速アタッカー**：素種族値A130・S75からメガ進化でA154・S151まで伸び、S実数値223まで到達します。シャドークロー・ふいうちを軸に先手から打点を通す構成が中心です
- **タイプ変化で耐性が入れ替わる**：メガ進化前のあく単はかくとう・むし・フェアリーに弱点でしたが、メガ後のあく/ゴーストはノーマル・かくとうが無効化される一方、ゴースト・あく耐性を失いフェアリー×2弱点は残ります
- **主流技同士で判定すると得意6体・苦手18体**：サーフゴー・イダイトウ(メス)・ゲッコウガ・オオニューラ・ラウドボーン・イエッサン(オス)には先制で押し切れる一方、ガブリアス・ボーマンダ・アシレーヌ・グソクムシャ・カバルドンなど使用率上位の多くには火力・耐久面で届かず不利になります

苦手表の多くは、シャドークロー・インファイトが確定2〜3発止まりで相手の一致技の確定1〜2発に押し切られるパターンです。使用率31位という順位が示す通り、アブソル単体で環境上位を押し切る場面は限定的で、同居率上位のガブリアス・カバルドンのような高採用率のパートナーと役割を分担する構築が前提になります。

---
