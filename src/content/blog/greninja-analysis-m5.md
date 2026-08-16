---
title: '【ポケモンチャンピオンズ】ゲッコウガ 考察 M-5 シーズン メガシンカ型の実数値'
description: 'M-5シーズン使用率17位のゲッコウガを考察。メガ石採用率65.4%、れいとうビーム91.1%を軸にしたメガゲッコウガS213の実数値と、きあいのタスキ型との違い、苦手・有利なポケモン、同居率上位のパートナーをデータで解説します。'
pubDate: '2026-08-16'
updatedDate: '2026-08-16'
heroImage: '../../assets/hero-greninja-m5.png'
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
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" />
  <div>
    <h2 style="margin:0 0 8px">ゲッコウガ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">17位</strong>　持ち物: <strong>ゲッコウガナイト 65.4%</strong>
    </div>
  </div>
</div>

M-5シーズン、ゲッコウガは使用率17位につけています。メガ石（ゲッコウガナイト）採用率は65.4%で過半数を占め、メガ進化でC133・S142に伸びる特殊アタッカー運用が主流です。れいとうビーム（採用率91.1%）・あくのはどう（86.4%）・ヘドロウェーブ（82.5%）と幅広い技の構成を持ち、対応する技のタイプに変化する特性へんげんじざいと組み合わせて崩す型です。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">125</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">77</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">133</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:71%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">142</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">630</span>
  </div>
</div>

メガ進化前のゲッコウガはA95・C103・S122（合計530）ですが、メガ進化でA125・C133・S142まで伸びます。素早さは環境最速クラスで、非メガ状態でもS122は多くの相手を上から攻撃できる水準です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

×4弱点は無く、かくとう・むし・くさ・でんき・フェアリーの×2弱点が5タイプに分散しています。耐性は6タイプに及び、エスパー無効も持つため防御面のバランスは悪くありません。詳細な相手対策は後述の「苦手なポケモン」を参照してください。

### 特性

**へんげんじざい（87.2%）**。場に出るたび1回だけ、自分が繰り出す技と同じタイプに変化します。最初に選んだ技のタイプ一致補正を確実に得られるため、みず・あく・こおり・どく・くさと技の幅が広いゲッコウガとの相性が良い特性です。**げきりゅう（12.8%）**はHPが1/3以下でみず技威力1.5倍になる特性で、少数派ながら選択肢に入ります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">91.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリューなどドラゴン複合への貫通打点。ほぼ確定枠</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。20%でひるみ。メタグロス等のエスパー複合に有効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3タイプ中最大威力。フェアリー対策の主力技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みずしゅりけん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15×2〜5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の連続技。一致補正込みで打点として機能</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">安定威力の一致水技。みずしゅりけんより高火力の選択肢</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くさむすび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20〜120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が重いほど威力上昇。カバルドン等の重量級への打点</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

### 型① メガシンカ型（おくびょう）

**性格採用率: おくびょう 53.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガシンカ型（おくびょう）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（87.2%、メガ後も継承）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（59.3%）<br>
<strong>持ち物:</strong> ゲッコウガナイト（65.4%）
</div>
<div>
<strong>技構成:</strong><br>
・れいとうビーム<br>
・あくのはどう<br>
・ヘドロウェーブ<br>
・みずしゅりけん or なみのり
</div>
</div>
</div>

メガ進化後にS213（おくびょう時）を得る、環境で最も採用されている型です。おくびょうはS↑A↓補正のためCには影響せず、C実数値は種族値133から算出される185にとどまります。れいとうビーム・あくのはどう・ヘドロウェーブの3タイプでほぼ全ての相手に等倍以上を取れる技構成が主流です。

性格採用率はおくびょう53.0%・ひかえめ41.0%とほぼ拮抗しています。ひかえめ選択時はC203・S194となり（Cは種族値133から算出、Sはおくびょう比で-19）、火力寄りの型として一定数採用されています。

**強み:**

おくびょう選択時（53.0%）はスカーフ持ちを除けば、S213は環境上位のほぼ全てを上から攻撃できる水準です。ただしガブリアス（こだわりスカーフ採用率20.0%でS253）・サザンドラ（同82.9%でS247）・マスカーニャ（同55.2%でS288）のスカーフ型には上を取られるため、この3体には後出し前提の立ち回りが必要です。メガ進化前の1ターンだけ非メガのS実数値191で相手の初動を見てから、2ターン目にメガ進化して圧を強めるプレイングも取れます。

**弱み:**

メガ進化はパーティ内で1体しか使えない権利のため、ゲッコウガに割く分だけ他の候補（メタグロス・カイリュー等）から選択肢を奪います。またメガ進化を宣言した瞬間に相手へC185・S213のアタッカーであることが判明するため、以降の対面で最大打点を読まれやすくなる点も運用上の弱みです。

---

### 型② きあいのタスキ型（非メガ）

**持ち物採用率: きあいのタスキ 25.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型（非メガ）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（87.2%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（59.3%）<br>
<strong>持ち物:</strong> きあいのタスキ（25.3%）
</div>
<div>
<strong>技構成:</strong><br>
・れいとうビーム<br>
・あくのはどう<br>
・ヘドロウェーブ<br>
・みずしゅりけん
</div>
</div>
</div>

メガ石を他のポケモンに譲り、きあいのタスキでHP1割から耐えられる保証を得て初手から強引に攻撃を通す型です。非メガのC実数値155・S実数値191にとどまりますが、ミミッキュのじゃれつく（採用率97.3%）のような一撃で沈む火力を受けても最低1回は反撃できる安全性が持ち味です。

**強み:**

メガ進化を消費しないため、パーティ内の他のメガ枠（メタグロス・カイリュー等）と共存しやすく、初手からきあいのタスキを活かして先制で崩す運用に向きます。

**弱み:**

C155・S191はメガ型のC185・S213を大きく下回り、耐久上位の相手を確定数で仕留めきれない場面が増えます。タスキは1回しか機能しないため、まきびし・ステルスロックなどで先にHPを削られていると発動せず、あっさり突破されるリスクがあります。なお、みず/あくに対するいわ技（ステルスロック含む）は等倍のため、設置技で受けるダメージは最大HPの1/8で固定です。

---

## データ分析①：M-4以降メガ石が主流化した

M-2からM-5までの持ち物採用率を追うと、ゲッコウガの主流構築が「タスキで殴り合う型」から「メガで火力を伸ばす型」へ切り替わったことがわかります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">シーズン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガナイト</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">M-2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">35.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">15.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">M-3</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">45.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.6%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">M-4</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">49.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">M-5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">65.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">25.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.3%</td>
</tr>
</tbody>
</table>
</div>

M-3時点ではきあいのタスキ（45.6%）がゲッコウガナイト（36.2%）を上回り、非メガ運用が主流でした。しかしM-4で49.5%まで伸び、M-5では65.4%と過半数に達しています。こだわりスカーフは15.5%→3.3%へ一貫して減少しており、「先制で確定数を稼ぐ運用」から「メガでC185・S213まで伸ばし後続含めて崩す運用」へ構築の重心が移ったことが数値で確認できます。この4シーズンでの使用率順位（28位→21位→13位→17位）も、メガ主流化が進んだM-4以降に上昇しており、C+30・S+22というメガ進化の火力上昇が採用率を下支えしている可能性を示しています。

---

## 苦手なポケモン

みず/あくの弱点タイプ（かくとう・むし・くさ・でんき・フェアリー）を突く技を、一致・非一致を問わず採用率50%以上で持つ相手を中心に、主流技が等倍以下に止まりダメージレースで押し切れない相手も含めて挙げています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（98.2%）がフェアリー×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（96.9%）がくさ×2。スカーフ採用率55.2%で先手も取られます</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（58.8%）がでんき×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（97.3%）がフェアリー×2。ばけのかわで最初の1発のダメージを無効化されます（最大HPの1/8を消費）</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（57.3%）がくさ×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ソーラービーム（57.5%）がくさ×2。ひでり下のリザードナイトY（57.9%）では1ターン技として即撃てますが、リザードナイトX（41.1%）では溜めが挟まるため初撃を避けやすい点に注意</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボディプレス（55.6%）がかくとう×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ハッサム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり（57.6%）がむし×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">サザンドラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり（78.0%）がむし×2。スカーフ採用率82.9%でS225〜247と先手も取られます</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0026-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ライチュウ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんじほう（97.5%）がでんき×2、きあいだま（97.1%）がかくとう×2、くさむすび（70.6%）がくさ×2と弱点3種を高採用率で持ちます。メガ石はライチュウナイトY（97.2%）が一択で、メガ後は特性ノーガードによりでんじほうが必中化します（詳細は表下）</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0503-01.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ダイケンキ（ヒスイの姿）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎ（95.1%）がかくとう×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ウルガモス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレイン（79.6%）がくさ×2、むしのさざめき（39.3%）もむし×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0257-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">バシャーモ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（66.5%）がかくとう×2、かみなりパンチ（44.3%）もでんき×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0479-02.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ウォッシュロトム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボルトチェンジ（87.8%）・10まんボルト（51.9%）がでんき×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0983-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ドドゲザン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（98.9%）は半減だが優先度+1で先制されるため、主流技が通らずダメージレースで押し切れません。こちらの等倍打点はみず技のみ</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0428-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミロップ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ進化率95.8%で、メガ後はノーマル/かくとう。インファイト（67.1%）・優先度+1のマッハパンチ（60.1%）がともにかくとう×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0700-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ニンフィア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特性フェアリースキン（99.4%）で主力のハイパーボイス（98.8%）がフェアリー技化し×2で通ります</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0003-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フシギバナ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレイン（61.1%）がくさ×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（65.7%）がかくとう×2。メガ進化率97.3%</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0398-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ムクホーク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（94.4%）がかくとう×2。メガ進化率82.2%で、メガ後はかくとう/ひこう</td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fef3cd;border:1px solid #f59e0b;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>⚠️ 5タイプの弱点に上位ポケモンが分散</strong><br>
  ×4弱点こそありませんが、環境上位の一定数がいずれかの弱点タイプの一致技を採用率50%以上で持ちます。B77・D81と耐久も高くないため、後出しよりも対面から積極的に打点を通す立ち回りが基本です。
</div>

---

## 有利なポケモン

みず・あく・こおり・どくの技が刺さり、かつ相手の主力技でこちらの弱点（かくとう・むし・くさ・でんき・フェアリー）を突く技を持たない、または持っていても採用率が低く実運用上ほぼ機能しない相手に絞っています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん/ドラゴンにれいとうビームが×4。主力技はこちらの弱点を突きません（スカーフ採用率20.0%の個体はS253で先手を取られます）</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん単タイプにみず・こおり・くさが×2。主力のじしん・あくび（95.3%）は弱点を突きませんが、あくびで交代を強要されます</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">イダイトウ（オス）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力技（シャドーボール・なみのり・アクアジェット・れいとうビーム）はいずれも半減以下で決定打を欠きます</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0094-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（88.3%）は半減、ヘドロウェーブ（74.6%）も等倍止まりで決定打を欠きます。こちらのあくのはどうはゴースト/どく複合に×2（詳細は表下）</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0121-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">スターミー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/エスパーにあくのはどう・くさむすびが×2。主力技は弱点を突かず、メガ後S189でもゲッコウガのS213には届きません</td>
</tr>
</tbody>
</table>
</div>

<div style="background:#f1f5f9;border:1px solid #94a3b8;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>ゲンガーとの打点比較</strong><br>
  ゲンガーはきあいだま（採用率10.0%、かくとう×2）も持つため、持たれた個体には不利です。ただし多数派（88.3%）のシャドーボールは半減、ヘドロウェーブ（74.6%）も等倍止まりで、メガゲンガー（C170、実数値C222）のヘドロウェーブはメガゲッコウガ（実数値D101・HP149）に対して最大乱数でも与ダメージ93.3%と確定2発。対してこちらのあくのはどう（メガゲッコウガC実数値185、ゴースト/どく複合に×2）はメガゲンガー（実数値D115・HP137）に最低乱数でも107.3%となり確定1発です。この打点差から、きあいだま非採用の多数派に対しては有利と判定できます。
</div>

<div style="background:#f1f5f9;border:1px solid #94a3b8;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>ライチュウのメガ後火力</strong><br>
  メガ石はライチュウナイトYが97.2%で一択。メガライチュウYはとくこう種族値160（非メガは90）まで伸び、特性ノーガードででんじほうが必中化します。とくこう種族値160は「種族値」であり、実数値（EV32・C上昇性格なら200超）とは異なる点に注意してください。
</div>

<div style="background:#f1f5f9;border:1px solid #94a3b8;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>互角の相手：ブラッキー（27位）</strong><br>
  最大打点ヘドロウェーブでも与ダメージ約32.7〜38.6%で、ねがいごと・たべのこしで回復されます。相手の主力イカサマも半減され乱数4発（確定5発）止まり。決定打はどくどくによる継続ダメージで、双方一撃で沈める技が無い互角の相手です。
</div>

---

## 同居率上位のパートナー

M-5でゲッコウガと同じパーティに入る頻度が高いポケモン（同居率1〜5位）を紹介します。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
  </div>
</div>

**ミミッキュ**（同居率2位）はゴースト/フェアリータイプで、ゲッコウガの弱点であるフェアリー・でんきの技をタイプで受けられるわけではありません（両技ともミミッキュに等倍で通ります）。弱点補完というより、単純に同居率が高い組み合わせとして順位のみ紹介します。**ガブリアス**（同居率1位）はじめんタイプによりでんき技を無効化でき、ゲッコウガのでんき弱点をカバーできます。一方でガブリアス自身もフェアリー技には×2で弱く、フェアリー弱点はガブリアスとゲッコウガの両方が共有するため、この組み合わせで補い切れない弱点として意識しておく必要があります。

---

## まとめ

M-5のゲッコウガは使用率17位で、メガ石採用率65.4%とれいとうビーム（91.1%）・あくのはどう（86.4%）・ヘドロウェーブ（82.5%）の3タイプ展開が基本コンセプトです。特性へんげんじざいで最初の一致技を確実に得ながら、メガ進化でS213まで伸びる高速アタッカーです（おくびょう時のC実数値は185で、非メガ時の155から+30・約19%増）。

- **メガ進化型（65.4%）と非メガのきあいのタスキ型（25.3%）に大別できる**：メガはS213・C185の火力、タスキ型はS191・C155にとどまるがメガ枠を温存でき、パーティ全体のメガ進化権をどこに配分するかで型が分かれます
- **×4弱点は無いが、かくとう・むし・くさ・でんき・フェアリーの5タイプ×2弱点を採用率50%以上の一致技で突く相手が環境上位に多く**、後出しは危険です
- **カバルドン・ガブリアス・イダイトウ（オス）・スターミー・ゲンガーには一致技が刺さり、主力技もこちらの弱点を突きません**（カバルドンのあくび、ガブリアスとのフェアリー弱点共有には注意）。逆にニンフィアは特性フェアリースキンでハイパーボイスがフェアリー技化し×2で通るため苦手側です。ドドゲザンも苦手側で、実質の理由は先制のふいうちそのものより、あく/はがねタイプにこちらの主流技（こおり・あく半減、どく無効）が通らずダメージレースで押し切れない点にあります。ブラッキーはイカサマが半減かつA無振りで乱数4発（確定5発）止まり、双方に決定打が無く互角です

幅広い技の構成と高い素早さで対面を制圧できる一方、耐久面は低く、5タイプに散った弱点をパートナーで補いながら運用するアタッカーです。

---

*関連記事：[メタグロス考察 M-5](/blog/metagross-analysis-m5/)*
