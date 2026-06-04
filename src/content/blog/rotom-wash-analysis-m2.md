---
title: '【ポケモンチャンピオンズ】ウォッシュロトム考察 M-2 使用率22位 ボルトチェンジとおにびの起点作り'
description: 'M-2シングルバトルで使用率22位のウォッシュロトムを徹底分析。ハイドロポンプ採用率98.5%・ボルトチェンジ88.7%・おにび80.6%のサポート型から、ふゆうでじめん無効・くさ/ゴースト/あく弱点まで実データで解説。HD耐久型の立ち回りと苦手なポケモンの対策を紹介します。'
pubDate: '2026-06-04'
draft: true
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
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" />
  <div>
    <h2 style="margin:0 0 8px">ウォッシュロトム</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px" />
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">22位</strong>　特性: <strong>ふゆう 100%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ウォッシュロトムは**使用率22位**を記録。特性は**ふゆう100%**で、でんき/みずの弱点であるじめんを無効化しているのが最大の特徴です。

技構成は**ハイドロポンプ採用率98.5%・ボルトチェンジ88.7%・おにび80.6%**が軸で、攻めて崩すアタッカーというより、**ボルトチェンジで対面操作しながらおにびで物理アタッカーを機能停止させる起点作り役**として採用されています。

---

## ウォッシュロトムの特徴

### 1. ふゆうでじめん無効、攻撃範囲はでんき/みずの一貫性

ウォッシュロトムはでんき/みずという複合タイプを、特性**ふゆう**でじめん無効と組み合わせています。でんき単体ならじめんが×2弱点ですが、ふゆうにより**じめん技を完全に無効化**します。環境1位ガブリアスのじしん（採用率99.2%）・7位カバルドンのじしん（98.0%）を受けてもダメージ0です。

攻撃面はハイドロポンプ（みず）と10まんボルト／ボルトチェンジ（でんき）の2タイプで、この2つは多くの環境上位に等倍以上で通る一貫性の高い組み合わせです。みずはガブリアス・リザードン・カバルドンに×2、でんきはアシレーヌ・アーマーガア・ギャラドスに×2で刺さります。

### 2. ボルトチェンジで対面操作しながら火力を出す

ボルトチェンジ（採用率88.7%）はダメージを与えつつ味方に交代できるでんき技です。不利な相手に後出しされても、ボルトチェンジで削りながら有利な味方に引いて対面を立て直せます。とくこう105からのタイプ一致補正が乗るため、交代しつつ相手に無視できない負荷をかけられるのが、単なる交代技との違いです。

### 3. おにびで物理アタッカーを起点化

おにび（採用率80.6%）はやけど状態にして相手のこうげき実数値を半減させる変化技です。環境上位の物理アタッカー（ガブリアス・マスカーニャ・ドドゲザン等）に通せば、こうげきを半減させて後続の物理受けを通しやすくします。ふゆうでじしんを無効化しながらガブリアスに後出しし、おにびを入れて起点化する動きが代表的です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">107</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">105</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">107</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">86</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">520</span>
  </div>
</div>

ぼうぎょ107・とくぼう107と両防御が高く、HP50の低さをEV振りとオボンのみで補えば物理・特殊どちらにも一定の役割を持てます。とくこう105は崩しの主役を張るには物足りませんが、ボルトチェンジで負荷をかけながら回す用途には十分です。すばやさ86は環境の中速ラインで、後述のとおり多くのアタッカーには先手を取れません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="でんき" />
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん（ふゆう）
  </td>
</tr>
</tbody>
</table>
</div>

弱点はくさ・ゴースト・あくの3タイプのみで、いずれも×2で通ります。ほのお・みず・でんき・こおり・ひこう・はがねの6タイプを半減でき、ふゆうでじめんを無効化するため、環境に多いじめん・ほのお・はがね物理に受け出ししやすい耐性構成です。一方で、8位イダイトウ（オス）のおはかまいり（ゴースト・採用率99.9%）や21位サザンドラのあくのはどう（あく・98.5%）など、弱点を突く一致技を主力に持つ相手には受け出しできません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイドロポンプ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中率80。一致のメイン火力。ガブリアス・リザードン・カバルドンに×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボルトチェンジ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">88.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に味方へ交代。対面操作の軸</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">80.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やけど付与でこうげき半減。物理アタッカーの起点化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">交代しないでんき打点。居座って撃つ用</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いたみわけ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP50の低さを補う回復兼相手削り。耐久型で採用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型で持ち物を押し付け、相手を縛る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほうでん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30%まひのでんき打点。10まんボルトと選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C2段階アップ。少数の積みアタッカー型</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布は耐久を盛る**ずぶとい33.2%・おだやか13.4%・なまいき13.3%**と、火力・速度を確保する**ひかえめ27.8%・おくびょう10.2%**に二分されます。EVも耐久振りのHD・HB系（HD+b型が最多採用率19.6%）と、火力振りのCS系（CS+h型9.1%）に分かれており、サポート寄りとアタッカー寄りの2型が併存しています。

### 型1: HD耐久サポート型（最多採用）

**EV採用率: HD + b 19.6%**（HB・HD系の耐久振りで最多。性格はずぶとい等）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HD耐久サポート型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ずぶとい（B↑ A↓）／おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 D24 B10（HDB配分。最多型）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・ハイドロポンプ<br>
・ボルトチェンジ<br>
・おにび<br>
・いたみわけ / 10まんボルト
</div>
</div>
</div>

**強み:**

ぼうぎょ107・とくぼう107の両受け耐久にH振りとオボンのみを重ね、物理・特殊どちらの中速アタッカーにも後出しできます。ふゆうでじめんを無効化するため、ガブリアス・カバルドンのじしんに受け出してからおにびでこうげきを半減させ、後続の物理受けが通る盤面を作れます。いたみわけはHP50の低さを補いつつ相手のHPを削れるため、たべのこしと合わせて長く居座れます。

**弱み:**

火力をEVに割かないため、ボルトチェンジ・10まんボルトの削り量が小さく、相手を倒しきる性能はありません。アタッカーというより「おにび＋対面操作で味方の通りを作る」役割に徹する型で、おにびが効かない特殊アタッカーやみがわり持ちには仕事が薄くなります。

---

### 型2: CSスカーフ／アタッカー型

**EV採用率: CS + h 9.1%**（CS系の火力振り。性格はひかえめ／おくびょう）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CSアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ひかえめ（C↑ A↓）／おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り。余り2はH）<br>
<strong>持ち物:</strong> こだわりスカーフ（採用率15.7%） / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ハイドロポンプ<br>
・10まんボルト<br>
・ボルトチェンジ<br>
・トリック / おにび
</div>
</div>
</div>

**強み:**

おくびょうCSですばやさを最大まで伸ばし、すばやさ86という中速をスカーフで補って上から動く型です。トリックでこだわりスカーフを耐久型や積みアタッカーに押し付け、技を固定して機能停止させられます。とくこう105からのハイドロポンプ・10まんボルトを上から撃てるため、HD型より削り・縛り性能が高くなります。

**弱み:**

耐久にEVを割かないため、HD型のように後出しから受けて起点を作る動きはできません。スカーフでこだわるため変化技のおにび・いたみわけと両立しづらく、対面性能と引き換えにサポートの柔軟さを失います。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率TOP30のうち、ウォッシュロトムと相性がはっきり出るポケモンを有利・不利の両面から挙げます。基準は「こちらの一致技（みず・でんき）が×2で通り、相手の主力技を受けられるか」「すばやさ86で先手を取れるか」「弱点のくさ・ゴースト・あくを突かれないか」です。ふゆうでじめんを無効化する一方、HP50と低耐久で弱点技を1発でも貰うと崩れやすい点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）をふゆうで無効。ハイドロポンプが×2（じめん2×ドラゴン1）で刺さる。後出ししておにび／ハイドロポンプを通せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.0%）をふゆうで無効。ハイドロポンプが×2。なまける・あくびで粘られるが弱点を突き続けられる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプが×2（メガY含む）、ほのお技はこちらに×0.5。ただしソーラービーム（くさ・61.0%）は弱点×2なので、くさ技採用個体には後出ししない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのみず・でんき技ははがね/ひこうに半減で打点は乏しいが、相手のボディプレス・アイアンヘッドはこちら半減で受けられ、おにびで起点化できる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトが×4（でんき2×みず2、みず/ひこうの両方に有効）。すばやさ86＞81で先手。いかくは入るがでんき技で一撃圏</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトが×2（みず2×フェアリー1）で刺さる。ただしムーンフォース（フェアリー・採用率97.0%）は等倍で高火力、こちらのみず技は半減。撃ち合いは互角</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・92.9%）が×2弱点で、すばやさ123に上から削られる。はたきおとすでオボンのみも狙われる</td>
</tr>
</tbody>
</table>
</div>

アーマーガア戦はみず・でんき技ともはがね/ひこうに半減され打点が乏しいため、やや有利の根拠は「相手の物理技を半減で受けつつおにびで起点化できる」点にあります。決定力はないので削りきりは後続に任せます。

### 苦手なポケモンと対策

弱点のくさ・ゴースト・あくを一致技で突いてくる相手、またはすばやさ86を上回り高火力で押してくる相手が苦手です。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・採用率92.9%・必中急所）が×2弱点。すばやさ123で上から削られ、はたきおとすで持ち物も落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技を半減するほのお・はがねタイプ（ハッサム等）を同伴し、マスカーニャの前に引いて受ける。ウォッシュロトム単体では対面しない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">イダイトウ(オス)（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おはかまいり（ゴースト・採用率99.9%）が×2弱点で高火力。アクアジェット（みず先制・91.1%）はこちら半減だが、おはかまいりで上から崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴーストを半減するあく・ノーマルタイプ（ドドゲザン等）を同伴して受ける。10まんボルトはみず/ゴーストに×2で通るが受け出しは不可</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく・採用率98.5%）が×2弱点。すばやさ98で先手を取られ、こちらのみず・でんき技は等倍止まりで決定力がない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくを半減するフェアリー・かくとうタイプ（フラエッテ永遠等）を同伴して受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち・シャドークロー（ゴースト・採用率93.6%/61.0%）が×2弱点。ばけのかわで一撃を耐えてから上から崩される。こちらのみず・でんきはゴースト/フェアリーに等倍止まり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴーストを半減するあくタイプ（ドドゲザン・サザンドラ等）を同伴して受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致技が×2弱点。みず・でんきはくさ/どくに半減でこちらの打点が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・ひこう・エスパー技を持つアタッカーで弱点を突く。対面は避け後続で処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あく/ドラゴンでロトムの弱点くさを半減。とんぼがえりと合わせ対面操作で回す</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0503-01.webp" alt="ダイケンキ(ヒスイ)">
    <div class="name">ダイケンキ(ヒスイ)</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/はがねでくさを半減。ボルトチェンジから着地させる受けの相方</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。おにびで起点化した相手に上から打点を入れる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ枠でロトムが苦手なくさ受け（フシギバナ等）に打点。とんぼがえりで対面操作を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね複合であくを半減。ボルトチェンジから着地し高火力で詰める</div>
  </div>
</div>

**パーティ構成の基本方針:**

ウォッシュロトムは弱点がくさ・ゴースト・あくの3つに絞られる代わりにHP50と低耐久で、攻撃面の決定力も低めです。ボルトチェンジで対面を操作しつつ、以下の役割を後続で補います。

1. **くさ・あく対策**: はがね・ほのおタイプ（ダイケンキ ヒスイ・ハッサム等）でくさを、フェアリー・かくとうであくを受ける枠
2. **決定力の補完**: ガブリアス・ルカリオなど、おにびで起点化した相手を上から倒すアタッカー
3. **対面操作の連携**: とんぼがえり・クイックターン持ち（サザンドラ・マスカーニャ）でボルトチェンジと組み合わせ、有利対面を作り続ける

---

## データ分析①：火力ではなく「ボルトチェンジ＋おにび」が採用理由

ウォッシュロトムの技採用率を見ると、攻撃技ハイドロポンプ（98.5%）に次ぐ採用率がボルトチェンジ（88.7%）・おにび（80.6%）で、純粋な連打火力技10まんボルトは56.8%にとどまります。

| 技 | 役割 | 採用率 |
|---|---|---|
| ハイドロポンプ | 一致メイン火力 | 98.5% |
| ボルトチェンジ | 対面操作（攻撃＋交代） | 88.7% |
| おにび | 物理アタッカーの起点化 | 80.6% |
| 10まんボルト | 居座り用でんき打点 | 56.8% |

とくこう105は連打アタッカーとして見ると中堅で、性格も耐久振りのずぶとい（33.2%）が火力振りのひかえめ（27.8%）を上回ります。つまりウォッシュロトムは「火力で押す枠」ではなく、**ふゆうでじしんを無効化しながらボルトチェンジで対面を操作し、おにびで物理アタッカーを機能停止させる起点作り役**として22位の使用率を得ているとわかります。10まんボルトよりボルトチェンジの採用率が30ポイント以上高い事実が、この役割の性格を端的に示しています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">EV（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD耐久サポート型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">HD+b 19.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ/たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ハイドロポンプ・ボルトチェンジ・おにび・いたみわけ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">両受け耐久で後出し、おにびで起点化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">決定力が低く倒しきれない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CSアタッカー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">CS+h 9.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ハイドロポンプ・10まんボルト・ボルトチェンジ・トリック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">スカーフで上から削り、トリックで縛る</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">後出し受けができない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ウォッシュロトムは、ふゆうでじめんを無効化する耐性とボルトチェンジ・おにびを軸にした起点作りで、M-2で使用率22位を維持しています。ガブリアス・カバルドンといった環境上位のじめん枠に後出しして弱点を突き、おにびで物理アタッカーを機能停止させるのが基本的な仕事です。

一方で弱点のくさ・ゴーストを一致技で突くマスカーニャ（3位）・イダイトウ オス（8位）には受け出しできず、決定力も低いため単体で完結する枠ではありません。ボルトチェンジで有利な味方に繋ぐ前提で、くさ・あく受けと決定力のあるアタッカーを後続に揃えることが採用の条件になります。

---

## 関連記事

- [後出しで弱点を突ける使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [でんき技が×4で刺さるギャラドスのM-2考察](/blog/gyarados-analysis-m2/)
- [ボルトチェンジから繋ぐ相方 ルカリオのM-2考察](/blog/lucario-analysis-m2/)
