---
title: '【ポケモンチャンピオンズ】ゲッコウガ 考察 M-4 シーズン メガシンカと型別解説'
description: 'M-4シーズン使用率15位のゲッコウガを考察。メガゲッコウガ（ゲッコウガナイト採用率49.5%）ときあいのタスキ型（40.1%）の2型を、実数値とタイプ相性データから比較分析。M-3シーズン21位から順位上昇した要因も採用率データの変化から検証します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-greninja-m4.png'
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
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" />
  <div>
    <h2 style="margin:0 0 8px">ゲッコウガ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">15位</strong>（M-3: 21位）　持ち物: <strong>ゲッコウガナイト 49.5% / きあいのタスキ 40.1%</strong>
    </div>
  </div>
</div>

M-4シーズン、ゲッコウガは使用率15位でM-3の21位から順位を上げました。れいとうビーム・あくのはどう・ヘドロウェーブ・みずしゅりけんの4技で幅広いタイプに打点を持つ特殊アタッカーで、持ち物はメガシンカするゲッコウガナイト（49.5%）と、きあいのタスキを持たせた無振り高速アタッカー（40.1%）の2型がほぼ二分しています。特性はへんげんじざい（73.1%）とげきりゅう（26.9%）で役割が分かれ、型ごとの選択と密接に結びついています。

---

## ゲッコウガの基本スペック

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
      <div style="width:48%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">72</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">67</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:69%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">103</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">71</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:81%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">122</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">530</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

通常時のS122は環境上位の中でも高水準で、メガ進化するとS142（実数値213・おくびょう）に到達します。C103もメガ後C133まで伸び、素早さと特殊火力を両立できる点がこのポケモンの土台です。一方でHP72・B67・D71と耐久面は薄く、一度でも有効打を受けると後続に繋がりにくい紙耐久です。

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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
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

弱点はかくとう・むし・くさ・でんき・フェアリーの5タイプ（いずれも×2）。特にフェアリーは環境2位のミミッキュがじゃれつく98.2%、7位のアシレーヌがムーンフォース98.0%を採用しており、上位ポケモンから弱点を突かれやすい構成です。一方であくタイプ由来のエスパー無効はマフォクシー（9位）などのエスパー技を完全に受け流せる利点になります。

### 特性

<strong>へんげんじざい（73.1%）</strong>は、場に出てから最初に技を出すときに1回だけ、その技と同じタイプに自分のタイプが変化する特性です。以降の技では発動しません。初手の技を必ずタイプ一致にできるため、対面の相手を読んで最も刺さる技を選べば1発目から確実にタイプ一致補正（1.5倍）が乗ります。<strong>げきりゅう（26.9%）</strong>はHPが最大HPの1/3以下になるとみずタイプの技の威力が1.5倍になる特性で、後述のきあいのタスキ型と組み合わせて使われます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリューに×4。10%でこおり状態にする追加効果を持つ最多採用技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致技。メタグロス・マフォクシーに×2。20%の確率でひるませる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">68.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャ・アシレーヌに×2。10%でどく状態にする追加効果</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みずしゅりけん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15×2〜5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1で先制。特殊技なのでC依存。バシャーモ・リザードンに×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ型の主力。カバルドン・マフォクシー・バシャーモ・リザードンに×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くさむすび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20〜120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の体重が重いほど威力上昇。カバルドン等の重量級への補完技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイドロポンプ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中80%となみのりより不安定だが高火力。採用は少数派</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マッドショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中時に相手の素早さを1段階下げる。採用は少数派</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置技を撒く変化技。攻撃技構成を圧迫するため採用は少数派</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理技で攻撃後に交代。C型のゲッコウガでは打点が伸びず採用は少数派</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：メガゲッコウガ型（おくびょう）

**性格採用率: おくびょう 53.3% / ひかえめ 40.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="メガゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガゲッコウガ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（73.1%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> ゲッコウガナイト（49.5%）
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

れいとうビーム（こおり・威力90）はガブリアス（じめん/ドラゴン・×4）とカイリュー（ドラゴン/ひこう・×4）に高打点、あくのはどう（あく・威力80）はメタグロス（はがね/エスパー・×2）とマフォクシー（ほのお/エスパー・×2）、ヘドロウェーブ（どく・威力95）はマスカーニャ（くさ/あく・×2）とアシレーヌ（みず/フェアリー・×2）に刺さります。メガ進化後はS142（実数値213）まで伸び、みずしゅりけん（みず・威力15・優先度+1・2〜5回攻撃）はA依存の物理連続技ではなく特殊技なのでC133がそのまま乗ります。

**強み:**

メガ進化でC133・S142まで強化され、初手のへんげんじざいで技のタイプに変化した瞬間からタイプ一致補正が乗った高火力を出せます。ガブリアス・カイリューへのこおり技×4は環境1位・12位への明確な打点です。

**弱み:**

HP実数値は種族値72のまま低く、メガ進化前後を問わず一撃で大きく削られやすい耐久です。相手の攻撃を受けてから動く運用には向かず、先手を取って撃ち合う立ち回りが前提になります。

---

### 型2：きあいのタスキ型（ひかえめ）

**性格採用率: ひかえめ 40.4% / おくびょう 53.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（26.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> きあいのタスキ（40.1%）
</div>
<div>
<strong>技構成:</strong><br>
・みずしゅりけん<br>
・なみのり<br>
・あくのはどう<br>
・れいとうビーム
</div>
</div>
</div>

きあいのタスキはHP満タン時に一撃で瀕死になる攻撃を受けてもHP1で耐える持ち物です。一度攻撃を受けてHPが最大の1/3以下まで減ると、げきりゅうでみずタイプの技の威力が1.5倍になり、なみのり（みず・威力90）やみずしゅりけんの底上げされた一撃で後続に繋げやすくなります。メガシンカせず通常特性のげきりゅうを使うため、パーティの他のポケモンにメガシンカ枠を譲れる点も型選択の要因です。

**強み:**

メガストーンを使わないため、他のメガシンカ候補と選出が競合しません。きあいのタスキで受けた一撃を耐え、げきりゅう発動後のなみのり・みずしゅりけんで打点を伸ばせます。

**弱み:**

タスキは1度きりの効果で、複数回攻撃を受ける多段技や設置技の残りダメージがある場面では機能しません。S122（ひかえめ時174）はメガ進化後のS142（実数値213）に比べて見劣りします。

---

## データ分析①：M-3→M-4 使用率と持ち物採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">指標</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>15位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6位上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガナイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+13.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">へんげんじざい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">71.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">73.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずしゅりけん採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">63.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+7.9pp</td>
</tr>
</tbody>
</table>
</div>

M-3の21位からM-4で15位へ上昇した背景には、ゲッコウガナイトの採用率が36.2%から49.5%へ+13.3pp伸びたことが挙げられます。M-3ではタスキ型がやや優勢だった「メガ型」と「きあいのタスキ型」の比率が、M-4ではメガ型優位（49.5% vs 40.1%）に反転しており、メガシンカによるS142・C133の高火力が評価を伸ばした形です。技面ではみずしゅりけんが55.9%から63.8%へ増加し、優先度+1の多段技としてタスキ型・メガ型双方での採用が広がっています。

---

## データ分析②：主要技のタイプ相性カバレッジ

れいとうビーム（こおり）・あくのはどう（あく）・ヘドロウェーブ（どく）・みずしゅりけん/なみのり（みず）の4タイプについて、M-4使用率TOP14への倍率を一覧化しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">相手（使用率順位）</th>
  <th style="padding:6px 8px;border:1px solid #cbd5e1">こおり</th>
  <th style="padding:6px 8px;border:1px solid #cbd5e1">あく</th>
  <th style="padding:6px 8px;border:1px solid #cbd5e1">どく</th>
  <th style="padding:6px 8px;border:1px solid #cbd5e1">みず</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス（1位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×4</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（2位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（3位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス（4位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（6位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（5位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（7位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドス（8位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マフォクシー（9位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">バシャーモ（10位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">リザードン（11位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サザンドラ（13位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×2</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（14位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー（12位）</td><td style="padding:6px 8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×4</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×0.5</td></tr>
</tbody>
</table>
</div>

TOP14中10体に、4技のうち少なくとも1つが抜群（×2以上）の打点があります。特にれいとうビームはガブリアス・カイリューに×4、カバルドン・マスカーニャ・サザンドラに×2と5体に有効打点を持ち、単体で最もカバレッジが広い技です。一方でミミッキュ（2位）・ブリジュラス（6位）・ギャラドス（8位）・アーマーガア（14位）には4技いずれも等倍以下にとどまり、これら4体には打点で優位を作れません。

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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー・採用率98.2%）が×2弱点。かげうち（ゴースト・採用率97.5%）はあくタイプで半減できますが、ばけのかわを崩す前にHP72の紙耐久を削られやすく、じゃれつく1発でも大きなダメージを負う相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・採用率97.3%）が×2弱点。ゲッコウガのヘドロウェーブはマスカーニャ（くさ/あく）に×2で通りますが、先に打点を通されると耐久面で崩れやすい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー・採用率98.0%）が×2弱点。アシレーヌ自身もみず/フェアリーでゲッコウガのみず技を半減するため、打点の取り合いで不利になりやすい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（かくとう・採用率67.2%）・かみなりパンチ（でんき・採用率45.7%）がいずれも×2弱点。物理・特殊の両面から弱点を突けるためどちらの技構成にも打点が通ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・採用率55.3%）が×2弱点。ロトム自身もでんき/みずでゲッコウガのみず技を半減するため、みず技主体の型では攻めきれません</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でゲッコウガと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ミミッキュ**（1位）はゴースト/フェアリーで、ばけのかわで安全に前に出てつるぎのまいを積める役割を持ちます。ゲッコウガはフェアリー弱点の相手（ドラゴン・かくとう・あく等）に有効打点を持たないため、じゃれつくで押せるミミッキュがその穴を補う関係です。

**ガブリアス**（2位）はじめん/ドラゴンで、ゲッコウガのみず・あく耐性（ともに×0.5〜等倍）とタイプ被りが少なく、じしんで受け出せる相手が異なります。ゲッコウガのれいとうビーム×4がガブリアスの弱点であるこおりを補完し、パーティ内で共有される弱点タイプを絞れる組み合わせです。

**カバルドン**（3位）はじめん単タイプで、あくびによる交代誘発とすなあらしでの回復サポートを担います。カバルドンが相手の後続を引き出した隙に、ゲッコウガが有利な相手へ安全に交代できる運用が中心です。

**メタグロス**（5位）ははがね/エスパーで、どく技を無効化する耐性を持ちます。ゲッコウガはあくタイプ由来でエスパー技を無効化するため、両者は互いに異なる無効タイプを持ち、パーティ全体で受けられる技の幅を広げる役割分担になっています。

**バシャーモ**（6位）はほのお/かくとうで、ゲッコウガのかくとう弱点をバシャーモ自身は半減で持たないためカバーにはなりませんが、バシャーモのつるぎのまい後の高火力とゲッコウガの初手からの高速打点で、異なるタイミングで攻め筋を作れる組み合わせです。

---

## まとめ

M-4のゲッコウガは使用率15位に上昇し、M-3の21位から順位を伸ばしたシーズンです。

- **ゲッコウガナイト採用率が36.2%→49.5%に上昇**：メガ進化後のS142・C133を活かした高速アタッカー運用がM-4で優位に
- **れいとうビーム・あくのはどう・ヘドロウェーブ・みずしゅりけんの4技でTOP14中10体に等倍以上の打点**：単一タイプでは崩せない相手を複合的にカバーする技構成
- **へんげんじざいは場に出て最初の技でのみ発動**：以降の技には適用されないため、初手の選択がタイプ一致補正の可否を左右する

HP72・B67・D71という薄い耐久は変わらず、ミミッキュ・アシレーヌのフェアリー技やマスカーニャのくさ技など上位ポケモンの弱点技を受けると崩れやすい点は共通の弱みです。メガ進化での高速アタッカー運用か、きあいのタスキで一撃を凌いでげきりゅうを起動するかは、パーティ内のメガシンカ枠の空き状況に応じた判断になります。

---

*関連記事：[ガブリアス考察 M-4](/blog/garchomp-analysis-m4/)*
