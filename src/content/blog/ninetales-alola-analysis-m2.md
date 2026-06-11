---
title: '【ポケモンチャンピオンズ】キュウコン（アローラ）考察 M-2 使用率52位 ゆきふらしオーロラベールの型と立ち回り'
description: 'M-2シングルバトルで使用率52位のキュウコン（アローラ）を徹底分析。ゆきふらし（採用率99.7%）からのオーロラベール88.5%・必中ふぶき87.1%・フリーズドライ69.9%を軸にした補助＋特殊アタッカー型を、性格おくびょう87.3%・とけないこおり46.7%の実データと実数値計算で解説します。'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-ninetales-alola-m2.png'
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
  <img src="/images/pokemon/pokemon-0038-01.webp" alt="キュウコン（アローラ）" />
  <div>
    <h2 style="margin:0 0 8px">キュウコン（アローラ）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">52位</strong>　特性: <strong>ゆきふらし 99.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、キュウコン（アローラ）は**使用率52位**を記録。特性は**ゆきふらし（採用率99.7%）**でほぼ統一されており、ゆきがくれ（0.3%）は実質採用されていません。

キュウコン（アローラ）の軸は、ゆきふらしで自分から展開する**ゆき状態**です。ゆき下でのみ使える**オーロラベール（採用率88.5%）**で味方の物理・特殊両方の被ダメージを軽減し、命中100扱いになる**ふぶき（87.1%）**と、みずタイプにも等倍以上で通る**フリーズドライ（69.9%）**で削る、補助と特殊アタックを兼ねるポケモンです。

持ち物は**とけないこおり 46.7%・きあいのタスキ 23.5%・オボンのみ 9.6%**で、こおり技を伸ばすとけないこおりが最多です。本記事では補助軸のオーロラベール型を基準に、火力を伸ばすわるだくみ型の差分も併せて解説します。

---

## なぜキュウコン（アローラ）が使われるのか

### 1. ゆきふらしから自前でオーロラベールを展開する

キュウコン（アローラ）の最大の役割は、ゆきふらしで**ゆき状態を自分で作り、その天候下でしか使えないオーロラベール（採用率88.5%）を起動する**ことです。オーロラベールは5ターンの間、味方の物理・特殊**両方**の被ダメージを軽減します。リフレクター・ひかりのかべを2枚張る手間を1枚で済ませられ、ゆきふらしの天候設置とセットで盤面を整えられる点が採用理由の中心です。

### 2. ゆき下で必中になるふぶきを撃てる

ふぶき（採用率87.1%）は本来命中70の技ですが、**ゆき状態では必中**になります。ゆきふらしを自分で展開するキュウコン（アローラ）は、この必中ふぶきを威力110で安定して撃てます。とけないこおり（46.7%）を持てば威力が1.2倍になり、ドラゴン・ひこう・じめん・くさへの主力打点になります。

### 3. フリーズドライでみずタイプにも刺さる

フリーズドライ（採用率69.9%）は**みずタイプの相手にも効果バツグン（×2）**になるこおり技です。通常こおり技はみずに半減されますが、フリーズドライはこれを覆します。環境上位のアシレーヌ（みず/フェアリー・4位）やカメックス（30位）、ミロカロス（50位）といったみず勢に、こおり技でありながら等倍以上で打点を持てるのが特徴です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">73</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">81</strong></span>
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
      <div style="width:54.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">109</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">505</span>
  </div>
</div>

すばやさ109・とくぼう100が目を引く配分で、とくこう81は特殊アタッカーとしては控えめです。おくびょう（採用率87.3%）でEVを最大振りすると**すばやさ実数値は177**になり、ガブリアス（最速S実数値169）やカイリュー（S実数値145）を上から叩けます。一方、とくこうはおくびょうC32振りで**とくこう実数値133**にとどまり、火力で押し切るより、ゆき・オーロラベール・必中ふぶきという補助＋削りの仕事で貢献するポケモンです。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="こおり" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2／×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね（×4）</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

フェアリータイプによりドラゴン技を無効化できるのが対戦上重要で、ガブリアスのげきりん（採用率47.9%）やカイリューのドラゴン技を透かせます。一方で**はがねは×4の4倍弱点**（こおり×2×フェアリー×2）で、ハッサムのバレットパンチ（採用率99.7%）など先制のはがね技に極端に弱い点に注意してください。ほのお・どく・いわも×2弱点で、被弾耐性は高くありません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーロラベール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆき下でのみ使用可。5ターン物理・特殊の被ダメを軽減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふぶき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致こおり技。ゆき下で必中。10%こおり。主力打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フリーズドライ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">69.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずにも×2。アシレーヌ・カメックス等みず勢への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">52.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致フェアリー技。あく・ドラゴン・かくとうへの打点。10%C↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の技を固定。積み技・補助技を縛って後続を補助</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこうを2段階上げる積み技。火力で押し切る型向け</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのつぶて</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。削り残しの処理に</td>
</tr>
</tbody>
</table>
</div>

オーロラベール・ふぶき・フリーズドライの3枠が主軸で、4枠目をムーンフォース（一致フェアリー打点）かアンコール（補助）で選ぶのが標準的な技構成です。

---

## 主要型の解説

各型は持ち物分布（とけないこおり46.7%／きあいのタスキ23.5%／オボンのみ9.6%）を指標としています。性格はおくびょう87.3%が支配的で、ひかえめ（8.4%）は少数です。EVはCS振り（C32 S32）に余りをHへ回す「CS+h」が最多（20.1%）です。

### 型1: オーロラベール補助型（最多級）

**指標: とけないこおり 46.7%／おくびょう 87.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0038-01.webp" alt="キュウコン（アローラ）" style="width:48px;height:48px">
  <strong style="font-size:1.05em">オーロラベールCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ゆきふらし（99.7%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り。余りH）<br>
<strong>持ち物:</strong> とけないこおり
</div>
<div>
<strong>技構成:</strong><br>
・オーロラベール<br>
・ふぶき<br>
・フリーズドライ<br>
・ムーンフォース / アンコール
</div>
</div>
</div>

**強み:**

ゆきふらしでゆきを展開し、初手からオーロラベールを張って後続のエースが積む・殴る隙を作れます。とけないこおりでふぶき・フリーズドライの威力が1.2倍になるため、補助を張りながらこおり技の削りも両立できます。S実数値177で環境上位のアタッカーより先に動けるため、ベール展開を被弾前に通しやすい点も補助役として有利です。

**弱み:**

きあいのタスキ型と異なり、弱点技を1回耐える保険がありません。はがね×4・ほのお×2の弱点を突かれると、ベールを張る前に落とされる場面が増えます。火力もとくこう実数値133止まりで、わるだくみ型のように単体で押し切る力はありません。

---

### 型2: きあいのタスキ展開型

**指標: きあいのタスキ 23.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0038-01.webp" alt="キュウコン（アローラ）" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ゆきふらし（99.7%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り）<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・オーロラベール<br>
・ふぶき<br>
・フリーズドライ<br>
・アンコール / ムーンフォース
</div>
</div>
</div>

**強み:**

とけないこおり型と違い、弱点技を1回耐えてオーロラベール展開を確定で通せます。はがね×4の先制技（バレットパンチ）に対しても、タスキで1発耐えてからベールを張るか、こおり技で1手返せます。ベール展開を「相手の弱点技に依存せず通したい」構築では、火力1.2倍より耐えの保険を優先する選択です。

**弱み:**

とけないこおり型と比べてこおり技の威力1.2倍が乗らず、削り性能が落ちます。また、こおり技を撃つと同時にあられ・すなあらしなどの天候ダメージや先制技でタスキが潰れやすく、2回目以降の行動保証はありません。

---

### 補足: わるだくみ積み型（26.9%）

わるだくみでとくこうを2段階上げ、補助役ではなく特殊アタッカーとして押し切る型です。アンコールで相手の積み技・補助技を縛ってから積むと隙を作りやすく、ふぶき・フリーズドライ・ムーンフォースの範囲で上から削れます。ただしとくこう実数値133が素の値のため、無補正では1回積んでようやく中火力という水準で、ベールを張らないぶん補助役としての貢献は失われます。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、キュウコン（アローラ）と相性がはっきり出るポケモンを有利・不利の両面から挙げます。S実数値177（おくびょう）で環境上位を上から叩ける一方、HP実数値149・ぼうぎょ実数値95と低く、はがね×4・ほのお×2の弱点技には極端に脆い点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふぶきが×4（ドラゴン2×じめん2）。S実数値177＞169で先手。げきりん（47.9%）はフェアリーで無効化できる。ただしいわ・ほのお技を持つ個体には×2弱点を突かれる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふぶきが×4（ドラゴン2×ひこう2）。S実数値177＞145で先手。ドラゴン技はフェアリーで無効。ただしかえんほうしゃ（47.8%）は×2弱点（ほのお）を突き、しんそくの先制も合わせると、これらを持つ個体やマルチスケイル下では確定で落としきれない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライが×2（みず特効）。S実数値177＞112で先手。ムーンフォース（97.0%）はフェアリーで×0.5、アクアジェット（66.6%）もみずで×0.5に軽減でき、被弾を抑えて削り合える。ただし低耐久ゆえ一撃で落としきれないと反撃で削られる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ 速度逆転で先手を許す</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふぶきが×2（くさ弱点）。だがS実数値192＞177で上を取られ、はたきおとす（57.6%）でとけないこおりを叩き落とされる。トリプルアクセル（72.2%）はこおりで×0.5に軽減できる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（99.7%）が×4弱点（はがね）。優先度+1の先制でこちらのSと無関係に上から落とされる。ふぶきは半減され打点が乏しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.4%）が×2弱点（ほのお）。ふぶきはほのお/ひこうに等倍止まりで一撃に届かず、被弾で崩れる。S実数値177＞167で先手は取れるが押し切れない</td>
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
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（99.7%）が×4弱点を先制で突き、Sと無関係に上から落とされる。ふぶきは半減で抜けない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・じめん枠（リザードン等）を後続に置いてはがね弱点を突く。先発でぶつけず、ベール展開後に交代で受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.4%）が×2弱点。ふぶきはほのお/ひこうに等倍で一撃に届かず、撃ち合いで押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ枠（カメックス・ミロカロス等）を後続に置いてほのお技を半減して受ける。ベール下なら後続が撃ち合いに耐えやすい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0937-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ソウブレイズ（26位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ゴーストでふぶきを半減し、むねんのつるぎ（82.8%）が×2弱点（ほのお）を突く。一致こおり打点が通らない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ枠でほのお技を半減して受ける。フリーズドライも半減されるため、後続のみず・じめん打点で崩す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S実数値192で上を取られ、はたきおとす（57.6%）でとけないこおりを落とされる。トリックフラワー（くさ・92.9%）は等倍で通る</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・はがね枠（ハッサム・ソウブレイズ等）を後続に置いてくさ・あくを半減しつつ上から殴る</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「キュウコン（アローラ）の弱点（はがね・ほのお・いわ）を等倍以上で突く相手」と「S実数値177を上回る、または先制技で隙を突く相手」に大別されます。いずれも単体での切り返しは難しいため、ベール展開後に後続のタイプ補完で受ける構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0350-00.webp" alt="ミロカロス">
    <div class="name">ミロカロス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久のみず枠。ベール下で苦手なほのおを半減して受け、起点役の後ろで粘る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0199-01.webp" alt="ヤドキング（ガラル）">
    <div class="name">ヤドキング（ガラル）</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">どく/エスパーの高耐久特殊枠。ベールを活かして殻を破る等で積み、火力を通す</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス">
    <div class="name">カメックス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず枠。苦手なほのお・はがねを後続で受け、ベール下で撃ち合いに強い</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん枠。ベール下で並び、はがね・ほのおに地面打点を持つアタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム">
    <div class="name">ハッサム</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/むしで苦手なはがね・いわを半減。ベール下でつるぎのまいを積む</div>
  </div>
</div>

**パーティ構成の基本方針:**

キュウコン（アローラ）はゆきふらし＋オーロラベールで盤面を整える起点役のため、ベールが効いている5ターンの間に後続のエースが仕事をする構築が基本です。

1. **ほのお・はがね対策**: みず（ミロカロス・カメックス）で苦手なほのお・はがね技を半減して受ける枠
2. **ベールを活かすエース**: ベール下で積み技を通すアタッカー（ハッサムのつるぎのまい、ヤドキング（ガラル）の積み等）
3. **じめん打点**: はがね・ほのおに強いじめん枠（ガブリアス）で苦手枠を上から崩す

---

## データ分析①：こおり技に偏る技採用率が示す「天候軸の補助役」設計

キュウコン（アローラ）の技採用率は、一致のこおり技と補助技に偏り、一致フェアリー技のムーンフォースが半数程度にとどまる点に特徴があります。

| 技 | タイプ | 採用率 | 役割 |
|---|---|---|---|
| オーロラベール | こおり | 88.5% | 補助（被ダメ軽減） |
| ふぶき | こおり | 87.1% | こおり主力打点 |
| フリーズドライ | こおり | 69.9% | みず特効打点 |
| ムーンフォース | フェアリー | 52.8% | フェアリー打点 |

注目すべきは、**こおり技3種（オーロラベール・ふぶき・フリーズドライ）がいずれも70%以上**で、一致フェアリー技のムーンフォース（52.8%）を上回る点です。これは、キュウコン（アローラ）が「フェアリーの攻撃範囲」ではなく「ゆきふらしで作るゆき天候の軸」として採用されていることを示します。

ふぶきはゆき下で必中になり、オーロラベールはゆき下でしか撃てません。とけないこおり（46.7%）でこおり技の威力が1.2倍になることも合わせ、3枠をこおり技で固めるのは、ゆきという天候資源を最大限に使う合理的な構成です。火力で押し切るわるだくみ（26.9%）が少数派にとどまるのも、このポケモンの主役が攻撃ではなく天候・補助である裏付けといえます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">オーロラベールCS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とけないこおり 46.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とけないこおり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こおり技1.2倍で補助と削りを両立</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">弱点技を耐える保険がない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">タスキCS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ 23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">弱点技を1回耐えてベールを確定で通す</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こおり技1.2倍が乗らず削りが落ちる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">わるだくみ積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ 26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ等</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C2段階上昇で特殊アタッカーとして押す</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ベールを張らず補助の貢献を失う</td>
</tr>
</tbody>
</table>
</div>

**総評:**

キュウコン（アローラ）はゆきふらしとオーロラベールを軸に、ゆき天候を自前で作って後続を補助する起点役です。ゆき下で必中になるふぶき・みずに刺さるフリーズドライで削りも兼ね、S実数値177で環境上位のアタッカーより先に動ける点が補助役として有利に働きます。

持ち物はとけないこおり46.7%・きあいのタスキ23.5%が中心で、「こおり技の威力を伸ばす」か「弱点技を1回耐えてベールを確定で通す」かで役割が変わります。一方、はがね×4・ほのお×2の弱点と低耐久から単体性能は高くなく、ハッサムのバレットパンチやリザードンのかえんほうしゃには後続のタイプ補完で対応する前提のポケモンです。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [苦手なほのおの主軸 リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
- [フリーズドライが刺さるみず枠 アシレーヌのM-2考察](/blog/primarina-analysis-m2/)
