---
title: '【ポケモンチャンピオンズ】ダイケンキ（ヒスイ）考察 M-2 使用率23位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率23位のヒスイダイケンキを徹底分析。特性きれあじで威力1.5倍のせいなるつるぎ・ひけん・ちえなみを軸にしたAS型を解説。きあいのタスキ37%・くろいメガネ36%の持ち物事情、環境上位への相性、パーティ構成まで実データで紹介します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-samurott-hisui-m2.png'
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
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ（ヒスイ）" />
  <div>
    <h2 style="margin:0 0 8px">ダイケンキ（ヒスイ）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">23位</strong>　特性: <strong>きれあじ 99.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ヒスイダイケンキは**使用率23位**を記録。みず/あくという原種（みず単体）とは別物の複合タイプを持ち、ほぼ全個体（99.2%）が特性**きれあじ**を採用しています。

ヒスイダイケンキの軸は、きれあじで威力1.5倍になる「切る技」です。あく一致技の**ひけん・ちえなみ**（威力65、採用率98.2%）はきれあじ補正で威力約98（タイプ一致補正を含めた実質威力は約146）、かくとう技の**せいなるつるぎ**（威力90、採用率86.0%）はきれあじ補正で威力135に達します。S85とこうげき種族値108の中速物理アタッカーとして、広い攻撃範囲で削りつつまきびしも撒ける役割を担います。

---

## なぜヒスイダイケンキが使われるのか

### 1. きれあじで切る技の威力が1.5倍になる

ヒスイダイケンキの主要技のうち、ひけん・ちえなみ・せいなるつるぎ・シェルブレードはいずれも「切る技」に分類され、きれあじの1.5倍補正を受けます。一致のひけん・ちえなみはタイプ一致補正1.5×きれあじ1.5で**実質2.25倍**、同じく一致のシェルブレード（みず・威力75）も同様の倍率がかかります。

特にあく/かくとうの2点攻撃（ひけん・ちえなみ＋せいなるつるぎ）は、環境のはがね・ゴースト・あく・ノーマルへ広く刺さる範囲です。先制技のふいうち（採用率65.7%）は切る技ではないためきれあじ補正は乗りませんが、あく一致でタスキ・低HP処理を担います。

### 2. ひけん・ちえなみでまきびしを撒ける

ひけん・ちえなみは攻撃と同時に相手の場をまきびし状態にする技です。採用率98.2%とほぼ確定枠で、攻撃しながら設置ができるため、相手の交代に対してダメージを蓄積させられます。後続のアタッカーが乱数を確定にする補助として機能し、アタッカーでありながら設置役を兼ねられる点が採用理由になっています。

### 3. せいなるつるぎが能力変化を無視する

せいなるつるぎは相手の防御・特防の上昇を無視してダメージを与える技です。てっぺきなどで防御を積んだ相手にも、積み前と同じダメージを通せます。てっぺき採用率63.5%のアーマーガア（ひこう/はがねでせいなるつるぎは等倍）のように、防御を積んで居座る物理受けに対し、積みを無視して等倍打点を維持できる点で価値があります。なお相手がフェアリー（アシレーヌ・フラエッテ:永遠など）の場合はかくとうが×0.5に半減されるため、能力無視があっても崩し手段にはなりません。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:54%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">108</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">85</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">528</span>
  </div>
</div>

こうげき108・すばやさ85を軸にした中速物理アタッカーです。とくぼう65・ぼうぎょ80と耐久は高くなく、HP90で物理はある程度受けられますが、弱点を突かれる特殊技には脆い配分です。**先手で攻撃するか先制技で詰める**、または交代で隙を作る立ち回りが基本になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

あくタイプがエスパーを無効化し、みず・ほのお・こおり・はがね・ゴースト・あくを半減します。原種のみず単体と比べ、エスパー無効とゴースト・あく半減を獲得した一方、原種が等倍だったかくとう・むし・くさを弱点として抱える点が大きな違いです。弱点はくさ・でんき・かくとう・むし・フェアリーの5タイプで、いずれも×2で通ります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひけん・ちえなみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65（実質約98）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致・切る技（きれあじ×1.5）。攻撃と同時にまきびし設置。命中90</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>せいなるつるぎ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90（実質135）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">切る技（きれあじ×1.5）。相手の能力変化を無視。はがね・あく・ノーマルへの打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シェルブレード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75（実質約113）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">72.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致・切る技（きれあじ×1.5）。50%でB1段階ダウン。命中95</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>65.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手のSに関わらず先制。相手が攻撃技を選択時のみ成功。きれあじ対象外</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の技を固定。積み技や変化技を縛る変化技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。不利対面から後続へ繋ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊こおり技。ガブリアス・カイリューなどドラゴンへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1のみず先制技。ふいうちと異なり攻撃読み不要</td>
</tr>
</tbody>
</table>
</div>

れいとうビーム（採用率9.9%）はとくこう100を活かした特殊技で、切る技が等倍以下に止まるガブリアス・カイリューにこおり×4を通すための選択肢です。物理技主体の構成ながら、ドラゴンへの打点として一部に採用されています。

---

## 主要型の解説

### 型1: AS物理アタッカー型（最多採用）

**性格採用率: いじっぱり 64.9%**（A↑ S↓。物理アタッカー型の指標で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ（ヒスイ）" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキASいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（最多型はH+2。採用率32.7%）<br>
<strong>持ち物:</strong> きあいのタスキ / くろいメガネ
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・せいなるつるぎ<br>
・シェルブレード<br>
・ふいうち
</div>
</div>
</div>

**強み:**

いじっぱりA32でこうげき種族値108を最大化し、きれあじ補正の乗った切る技で削っていく型です。あく/かくとうの2点に加えシェルブレードのみずで、はがね・ゴースト・ドラゴン・じめんなど環境の主要タイプへ等倍以上の打点を確保できます。先制技ふいうちで上から来る低耐久アタッカーやタスキ持ちを縛れるのも、S85で一部に抜かれるこのポケモンにとって重要です。

持ち物は、HP1で耐えて確実に一撃を入れるきあいのタスキ（37.0%）と、あく技を1.2倍に底上げするくろいメガネ（36.0%）が二分しています。タスキ型は対面性能と先制ふいうちの詰め、メガネ型はあく技にさらに1.2倍が乗るひけん・ちえなみの瞬間火力（実質威力約175相当）が持ち味です。

**弱み:**

ようき型ではないため、S85同速ライン（ブリジュラスなど）に対しいじっぱりだと素早さで競り負ける場合があります。また弱点5タイプはこちらより速い環境上位（メガルカリオS112のインファイト、マスカーニャS123のトリックフラワーなど）に分布しており、上から弱点を突かれると低いぼうぎょ・とくぼうで一撃で落とされやすい点が課題です。

---

### 型2: HA調整型（耐久寄せ）

**EV採用率: HA + bds 14.0%**（H20 A32 S10前後。耐久に厚く振る配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ（ヒスイ）" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HA耐久調整型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H20 A32 S10前後（B・Dにも少量）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし 等
</div>
<div>
<strong>技構成:</strong><br>
・ひけん・ちえなみ<br>
・せいなるつるぎ<br>
・ふいうち<br>
・アンコール / クイックターン
</div>
</div>
</div>

**強み:**

S最大振りを削ってHに回し、HP90を活かして物理攻撃を1〜2発受けながら攻撃する型です。AS型がタスキで1発受けるのに対し、こちらはHB方向の数値で複数回行動を狙えます。アンコール（採用率18.3%）で相手の積み技・変化技を縛り、せいなるつるぎの能力無視と合わせて積みアタッカーの起点を潰す動きや、クイックターン（16.0%）で不利対面から後続へ繋ぐ動きが取れます。

**AS型との使い分け:**

AS型はS32で同速・最速勝負に賭け、先制ふいうちと合わせて対面で削り切ることを狙います。一方HA型はSを落とす代わりに行動回数を確保し、アンコール・クイックターンで相手の動きを制限・回避する起点・サポート寄りの役割です。先手を取りに行くならAS型、対面より展開で勝つならHA型という住み分けになります。

**弱み:**

S10前後ではS85のAS型が先手を取れていた同速〜中速勢（ブリジュラスS85、ドドゲザンS50やギルガルドS60など）にも上を取られ、有利対面でも先制されます。耐久に振っても弱点5タイプの×2打点は重く、特殊アタッカーの一致弱点技は受け切れない点はAS型と共通の課題です。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率TOP30のうち、ヒスイダイケンキと相性がはっきり出るポケモンを有利・不利の両面から挙げます。S85・こうげき108を基準に、きれあじ補正の乗った切る技（ひけん・ちえなみ／せいなるつるぎ／シェルブレード）の通りと、相手の主力技（採用率はpokemon_movesで確認）がこちらの弱点5タイプ（くさ・でんき・かくとう・むし・フェアリー）を突くかで判定しています。

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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 超有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎが×4（あく2×はがね2）＋きれあじ補正で確定1発圏。S50で先手確保。先制ふいうち（採用率99%）もこちらにあく0.5×みず1＝×0.5で軽い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひけん・ちえなみ（あく）が×2（はがね1×ゴースト2）＋きれあじ補正。S60で先手。せいなるつるぎはかくとうがゴーストに無効のため通らない点に注意。主力のかげうち・ポルターガイスト（ゴースト）はこちらに×0.5。シールドフォルムのB140に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎが×2（はがね2×ドラゴン1）＋きれあじ補正だがB130で一撃は難しい。S85同速。10まんボルト（でんき・採用率67%）がこちらに×2弱点のため、いじっぱりだと同速負けで先に被弾するリスク</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シェルブレード（みず）がほのお/ひこうに×2＋きれあじ補正で刺さるが、S100でこちらが遅い。相手のほのお技はこちら×0.5で軽く、被弾には強い。先手シェルブレードを撃てないため一撃は難しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分（こおり技次第）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（採用率9.9%）を持てばこおり×4で確1だが採用率は低い。切る技は等倍止まり。S102でこちらが遅く、じしん（採用率99%）はこちら等倍。こおり技なしでは押し負ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">▲ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（かくとう）がこちらに×2弱点。メガ後S112でこちらが遅く、低いとくぼう・防御を上から削られる。せいなるつるぎは等倍止まり（はがね2×かくとう0.5）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">▲ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123で上を取られ、トリックフラワー（くさ・採用率93%）がこちらに×2弱点。こちらのひけん・ちえなみはあく0.5×くさ1＝×0.5で軽い。撃ち合いで先に落とされやすい</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点5タイプ（くさ・でんき・かくとう・むし・フェアリー）の一致技を持ち、かつこちらより速い、または高耐久でこちらの打点が乏しい使用率上位を挙げます。

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
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー・採用率97%）がこちらに×2弱点。とくぼう65では特殊耐久も足りず、せいなるつるぎ（はがね・あくでなくかくとう）はみず/フェアリーに等倍止まりで一撃に届きにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技を半減できるどくタイプ（キラフロル＝いわ/どくで×0.5）やはがね/ひこうのアーマーガア（×0.5）を同伴し、後出し処理する。アンコール型ならめいそうを縛って起点化を防ぐ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0939-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハラバリー（32位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パラボラチャージ（でんき・採用率99%）がこちらに×2弱点。なまける（83%）で回復しつつ居座られ、シェルブレード等倍では削り切れず持久戦で負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめんタイプ（ガブリアス・カバルドン等）を同伴し、でんき技を無効化して後出しする。せいなるつるぎはでんき単体に等倍のため単体では崩しにくい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S100でこちらより速く、むしのさざめき（むし・採用率34%）・ギガドレイン（くさ・59%）がともにこちらに×2弱点。ちょうのまいの起点にされやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・でんきタイプ（キラフロル・ハラバリー等）を同伴し、ちょうのまい前に弱点で処理する。アンコール型ならちょうのまいを縛れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ:永遠（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー・採用率87%）がこちらに×2弱点。めいそう（86%）で積まれると、せいなるつるぎの能力無視はあっても等倍打点では落とし切れず、ドレインキッスで回復され持久戦で負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技を半減できるキラフロル（いわ/どく）やアーマーガア（ひこう/はがね）を同伴して受ける。アンコールでめいそうを縛り、後続のどく打点で突破する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ばけのかわで一撃を耐え、じゃれつく（フェアリー・採用率92%）がこちらに×2弱点。つるぎのまい（87%）の起点にされやすい。こちらの先制ふいうちもばけのかわで止まる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技を半減できるキラフロル（いわ/どく）やアーマーガア（ひこう/はがね）を同伴して受ける。ばけのかわを別の駒で剥がしてから処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム">
    <div class="name">ウォッシュロトム</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/でんきででんきを半減し、苦手なハラバリー等のでんき枠を受けられる。でんき技でひこう・みず枠に打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン">
    <div class="name">ドドゲザン</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あく/はがねでむしを1/4に軽減。はがね技で苦手なフェアリー枠に弱点を突いて攻める</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめんでハラバリー等のでんき技を無効化。じしんでヒスイダイケンキの苦手なでんき枠に打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル">
    <div class="name">キラフロル</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">いわ/どくでフェアリーを半減し、アシレーヌの苦手枠を受ける。いわ技でウルガモスに弱点を突く</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう/はがねでくさ・フェアリーを半減し、苦手枠を後出しで受ける。とんぼがえりで対面操作</div>
  </div>
</div>

**パーティ構成の基本方針:**

ヒスイダイケンキはとくぼう65と弱点5タイプの広さがネックなので、残り5体で以下の役割を補います。

1. **フェアリー対策**: フェアリー技を半減できるキラフロル（いわ/どく）・アーマーガア（ひこう/はがね）でムーンフォース等を受ける枠
2. **でんき対策**: じめんタイプ（ガブリアス等）でパラボラチャージ等を無効化する枠
3. **くさ・むし対策**: はがね・ほのおタイプ（アーマーガア・リザードン等）で受ける枠
4. **まきびし活用**: ひけん・ちえなみのまきびしと相性の良い、相手の交代を誘う展開役

---

## データ分析①：きれあじ補正が生む実質威力と持ち物の二極化

ヒスイダイケンキの主要技のうち、ひけん・ちえなみ・せいなるつるぎ・シェルブレードはきれあじで威力1.5倍になり、ふいうちだけは対象外です。一致技にはさらにタイプ一致補正1.5倍が乗るため、実質威力は次のようになります。

| 技 | 基本威力 | きれあじ | 一致補正 | 実質威力 | きれあじ対象 |
|---|---|---|---|---|---|
| ひけん・ちえなみ（あく一致） | 65 | ×1.5 | ×1.5 | **約146** | ○ |
| せいなるつるぎ（かくとう） | 90 | ×1.5 | — | **135** | ○ |
| シェルブレード（みず一致） | 75 | ×1.5 | ×1.5 | **約169** | ○ |
| ふいうち（あく一致） | 70 | — | ×1.5 | 105 | ✕（先制） |

数値上はシェルブレード・ひけん・ちえなみの一致切る技が最も伸びますが、立ち回り上の主軸が**ひけん・ちえなみ（採用率98.2%）**である点が重要です。せいなるつるぎ86.0%・シェルブレード72.0%が外れることはあっても、ひけん・ちえなみはほぼ全個体が採用しています。これは「高火力のあく打点」であると同時に、攻撃しながらまきびしを設置できる唯一の技だからです。きれあじ補正で実質威力約146のあく技を撃ちつつ、外しても（命中90）相手の交代に設置で圧をかけられるため、削りと展開を一手で両立できる点がこのポケモンの核になっています。

一方で持ち物は**きあいのタスキ37.0%・くろいメガネ36.0%**とほぼ二分しています。タスキ型はとくぼう65・S85という「中速・低耐久ゆえに弱点技で1発で落とされる」弱点をHP1耐え＋先制ふいうちで補う対面・詰め寄りの選択、メガネ型はあく技をさらに1.2倍（ひけん・ちえなみが実質威力約175相当）に伸ばして火力で押し切る選択です。さらにこだわりスカーフ16.3%が、S85で抜けない中速〜高速勢の上を取る奇襲枠として続きます。低耐久ゆえの「耐えて殴る」か「速く・重く殴る」かで、持ち物が役割を規定しているのが読み取れます。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">AS物理アタッカー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 64.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.85em">タスキ / くろいメガネ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">切る技の高火力。タスキ＋先制ふいうちで詰め</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">弱点5タイプ。低耐久で弱点技に弱い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HA耐久調整型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA振り 14.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.85em">オボンのみ 等</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">行動回数確保。アンコール・クイックターンで展開</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">中速勢に抜かれる。弱点技は受け切れない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ヒスイダイケンキは、きれあじで底上げされたあく/かくとう/みずの切る技を軸に、まきびし設置と先制ふいうちを兼ねる中速物理アタッカーです。せいなるつるぎの×4が刺さるドドゲザンや、ひけん・ちえなみのあく×2でゴースト系を上から削れるギルガルドなど、はがね・ゴースト・あく系への明確な有利を持ちます。

一方で、みず/あくが抱えるくさ・でんき・かくとう・むし・フェアリーの弱点5タイプはいずれも環境上位（ルカリオ・マスカーニャ・アシレーヌ・ウルガモス等）に分布し、ぼうぎょ80・とくぼう65では弱点技を受けると崩されやすいのが使用率23位に留まる主因です。フェアリー・でんき・くさを受けられる駒をパーティで補い、まきびし＋切る技の削りを後続のアタッカーに繋げる構築運用が、このポケモンの強みを引き出す前提になります。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [かくとう打点で対面有利を取れるメガルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [同じはがねアタッカー ハッサムのM-2考察](/blog/scizor-analysis-m2/)
</content>
</invoke>
