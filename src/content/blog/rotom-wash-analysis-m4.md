---
title: '【ポケモンチャンピオンズ】ウォッシュロトム 考察 M-4 シーズン ハイドロポンプ採用で変わる立ち回り'
description: 'M-4シーズン使用率17位のウォッシュロトムを考察。M-3では未採用だったハイドロポンプが99.0%まで浸透し、こだわりスカーフ26.5%・おくびょう18.9%の攻撃型が台頭。耐久型とスカーフ型の実数値・カバレッジをデータで分析します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-rotom-wash-m3.png'
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
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" />
  <div>
    <h2 style="margin:0 0 8px">ウォッシュロトム</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px" />
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">17位</strong>（M-3: 20位）　特性: <strong>ふゆう（100%）</strong>
    </div>
  </div>
</div>

M-4シーズン、ウォッシュロトムは使用率17位でM-3の20位から順位を上げました。でんき/みずの複合タイプに特性ふゆうを持ち、じめん技を無効化しながらはがね・ほのお・みず・こおり・ひこうに耐性を持つ耐久寄りのポケモンです。M-4最大の変化は、M-3では技採用データに登場すらしなかったハイドロポンプが99.0%まで一気に浸透したこと。でんき単打点では突破できなかったじめんタイプへの打点を手に入れたことが、順位上昇の背景にあります。

---

## ウォッシュロトムの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">107</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">107</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">86</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">520</span>
  </div>
</div>

HP50は低めですが、ぼうぎょ107・とくぼう107とバランス良く高く、両刀のとくこう105も合わせ持つ数値です。すばやさ86は環境上位より遅めで、性格・EV次第で「積極的に前に出る攻撃型」と「相手の攻撃を受けて機を伺う耐久型」のどちらにも寄せられます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

弱点はくさタイプのみ（×2）。本来はじめんタイプにも×2で弱いはずですが、特性ふゆうにより無効化されます。ひこう・ほのお・みず・こおりに耐性、はがねには×0.25の高耐性を持ち、単一弱点タイプという明確な強みがあります。ただしM-4使用率6位のマスカーニャがトリックフラワー（くさ・採用率97.3%）を高い採用率で持っており、唯一の弱点を突かれる機会は少なくありません。

### 特性

**ふゆう（100%）**は「地面にいないことになり、じめん技・まきびし・どくびし・ねばねばネットが効かない」効果です。でんき/みずタイプ単体でもじめん技（じしん・じならし等）を無効化でき、ガブリアス・カバルドンなど環境上位のじめんタイプが持つ主力技を受け出しの起点にできます。全個体がこの特性のため、型による特性の使い分けはありません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致の最大打点。じめんタイプへの反撃手段としてM-4で新規標準化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボルトチェンジ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。でんき一致で対面操作しつつ後続へ繋げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をやけど状態にし物理アタッカーの攻撃を弱体化。耐久型の主力</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10%の確率でまひ付与。スカーフ型のでんき一致メインウェポン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手と持ち物を入れ替える。こだわりスカーフを耐久型に押し付けて弱体化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いたみわけ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分と相手のHPを折半。耐久型の立て直し・対面継続用</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひかりのかべ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5ターン味方の特殊ダメージを軽減。耐久型のいたみわけ枠と選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほうでん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30%の確率でまひ付与。10まんボルトより低威力で採用は少数</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>でんじは</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をまひ状態にする。じめんタイプには無効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>イカサマ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のこうげき種族値でダメージ計算。物理アタッカー相手の奇襲用</td>
</tr>
</tbody>
</table>
</div>

ハイドロポンプ99.0%・ボルトチェンジ90.6%・おにび75.5%の3技はほぼ全個体共通のコア技で、4枠目が耐久型のいたみわけ/ひかりのかべ、攻撃型の10まんボルト/トリックに分かれる構図です。10まんボルトの採用率55.3%は、耐久型・攻撃型の双方に一定数使われていることを示しています。

---

## M-4の採用型

### 型1：耐久型（ずぶとい 48.3%）

**性格採用率: ずぶとい 48.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ふゆう（100%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B32（代表例・採用率11.9%）<br>
<strong>持ち物:</strong> たべのこし（32.9%）またはオボンのみ（32.1%）
</div>
<div>
<strong>技構成:</strong><br>
・ハイドロポンプ<br>
・ボルトチェンジ<br>
・おにび<br>
・いたみわけ（ひかりのかべ）
</div>
</div>
</div>

ハイドロポンプ（みず・威力110）とボルトチェンジ（でんき・威力70・交代技）を主軸に、おにび（やけど付与）で相手の物理アタッカーの攻撃を弱体化させます。たべのこしは毎ターン最大HPの1/16回復、オボンのみはHPが半分以下になった時点で1度だけ最大HPの1/4回復と役割が異なり、長期戦志向ならたべのこし、被弾からの立て直しを重視するならオボンのみが選ばれています。いたみわけは自分と相手のHPを折半する技で、耐久型の対面を継続させる択として採用されています。

**強み:**

H157 / A76 / B174 / C125 / D127 / S106（ずぶとい・H32-B32）。ぼうぎょ174はガブリアスのげきりん（ドラゴン・威力120・採用率34.8%）を受けても乱数急所を除けば1発で沈まない厚さです。おにびでやけどを付与した相手には物理受けとして長く場に残れます。

**弱み:**

すばやさは無振りの106止まりで、こだわりスカーフを持つ相手には後手に回ります。攻撃面もハイドロポンプ・ボルトチェンジのタイプ一致技のみで、はがね・くさタイプの相手に決定打を欠きます。

---

### 型2：スカーフ攻撃型（おくびょう 18.9% / ひかえめ 20.7%）

**性格採用率: ひかえめ 20.7% / おくびょう 18.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフ攻撃型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ふゆう（100%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）またはおくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（採用率14.5%・全EV中最多）<br>
<strong>持ち物:</strong> こだわりスカーフ（26.5%）
</div>
<div>
<strong>技構成:</strong><br>
・ハイドロポンプ<br>
・ボルトチェンジ<br>
・10まんボルト<br>
・トリック
</div>
</div>
</div>

こだわりスカーフで素早さを1.5倍にする代わりに技が固定される型です。ハイドロポンプ（威力110）・10まんボルト（威力90・まひ10%）・ボルトチェンジ（威力70・交代技）でタイプ一致打点をまかない、トリックで持ち物を耐久型ポケモンに押し付けて弱体化させる択も持ちます。

**強み:**

ひかえめはH127 / A76 / B127 / C172 / D127 / S138。すばやさ実数値138はこだわりスカーフ込みで207相当まで伸び、耐久型（S106）より先制範囲が大きく広がります。C172のハイドロポンプは、耐久型のC125相当と比べ一段高い打点を出せます。

**弱み:**

おくびょうはH127 / A76 / B127 / C157 / D127 / S151（スカーフ込み約226相当）。C172のひかえめ型と比べCが低い分、ハイドロポンプの威力は落ちます。技が1つに固定されるため、はがね・くさタイプへの打点がなく交代されるだけで機能停止します。

---

## データ分析①：M-3→M-4 技・性格・持ち物の変化

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイドロポンプ</strong>（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">未採用</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボルトチェンジ（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">±0.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おにび（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-11.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリック（技）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+12.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ（持ち物）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>26.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+12.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>18.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+10.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">51.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">48.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.8pp</td>
</tr>
</tbody>
</table>
</div>

最大の変化はハイドロポンプの新規採用（0%→99.0%）です。M-3のロトムはでんき単打点（10まんボルト・ボルトチェンジ）にとどまっており、ふゆうでじめん技こそ無効化できても、じめんタイプに攻撃で反撃する手段を持っていませんでした。M-4でハイドロポンプがほぼ全個体標準となったことで、カバルドン（じめん単・使用率3位）にみず×2の実質打点を得ています。

トリック採用率も13.3%→25.3%とほぼ倍増しており、こだわりスカーフ採用率の12.0pp増（14.5%→26.5%）・おくびょう採用率の10.7pp増と連動しています。攻撃技の拡充とスカーフ運用の広がりが同時に進んだシーズンです。一方でずぶとい（耐久型の主力性格）は51.1%→48.3%とわずかに減少しており、攻撃型の比率が相対的に増しています。

---

## データ分析②：でんき・みず打点のカバレッジ

M-4使用率上位15体に対し、ハイドロポンプ（みず）・10まんボルト/ボルトチェンジ（でんき）のうち最大打点を計算した結果です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（使用率）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">でんき</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">最大打点</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ギャラドス（8位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×4</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×4</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">アシレーヌ（7位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">アーマーガア（14位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ゲッコウガ（15位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">リザードン（11位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">マフォクシー（9位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">バシャーモ（10位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">カバルドン（3位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">無効</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×2</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">×2</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ガブリアス（1位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">無効</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ミミッキュ（2位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">メタグロス（4位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">カイリュー（12位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×1</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ブリジュラス（6位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#2563eb">×0.5</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">マスカーニャ（5位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#2563eb">×0.5</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">サザンドラ（13位）</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:center;color:#2563eb">×0.5</td></tr>
</tbody>
</table>
</div>

上位15体のうち7体（ギャラドス・アシレーヌ・アーマーガア・ゲッコウガ・リザードン・マフォクシー・バシャーモ）に×2以上の打点が通り、うちギャラドスには×4が刺さります。一方でブリジュラス・マスカーニャ・サザンドラの3体は両打点とも×0.5に抑えられ、ガブリアス・カイリューには等倍以下（ガブリアスはでんきが無効）にとどまります。ハイドロポンプの追加は「でんき無効のじめんタイプに手も足も出ない」状態を解消した一方、あく・ドラゴン複合の相手には依然として決定打を欠く構図です。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・採用率97.3%）が唯一の弱点である×2を突きます。マスカーニャ側はでんき・みずどちらも×0.5で耐えるため、打点のぶつけ合いで一方的に不利です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき打点は無効、みずも等倍止まりで攻撃面の決定打がありません。げきりん（ドラゴン・威力120・採用率34.8%）は耐久型のぼうぎょ174でも乱数急所を除けば1発で沈まない程度に耐えますが、こちらから崩す手段が乏しい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・みずとも×0.5で受けられる一方、りゅうせいぐん（ドラゴン・威力130・採用率93.3%）は等倍で通り、スカーフ型のとくぼう127に対して1発でH実数値の9割前後まで削れる高火力です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・みずとも×0.5で受けられます。主力のラスターカノン（はがね・採用率76.4%）はこちらの耐性で×0.25に軽減できますが、りゅうせいぐん（ドラゴン・採用率71.9%）は等倍で通り、耐久型でも確定2発（1発でH実数値の71〜84%）まで削られます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でウォッシュロトムと同じパーティに入る頻度が高いポケモン（同居率上位、7位ルカリオ・8位ハッサムを除く主要8体）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、じめん技を無効化するふゆうの恩恵はガブリアス自身のじしんには及びませんが、他パーティのじめんタイプの技全般をロトムが受け止める役割分担ができます。ガブリアスのドラゴン打点はロトムが苦手とするマスカーニャ・サザンドラには等倍以上で通り、ロトムの手が届かない相手をガブリアスが処理する組み合わせです。

**ミミッキュ**（2位）はゴースト/フェアリーで、ロトムのおにびによるやけど付与が相手の物理アタッカーを弱体化させ、ミミッキュのばけのかわを消費させにくい対面作りに寄与します。ミミッキュのかげうちがマスカーニャ・サザンドラなどロトムの手が届かない相手に打点を持つ点で役割が分かれます。

**カバルドン**（3位）はじめん単で、ロトムのふゆうがじめん技を無効化する一方、カバルドンのあくびで相手の交代を促してロトムの安全な対面を作れます。カバルドン自身はロトムのハイドロポンプ・ボルトチェンジのタイプ一致打点が届く範囲外（同じパーティのため対戦しない）ですが、ステルスロック設置でパーティ全体の削り役を担います。

**メタグロス**（4位）ははがね/エスパーで、ロトムのはがね耐性（×0.25）とメタグロスのエスパー耐性を補い合う関係にはなりませんが、メタグロスのバレットパンチ・サイコファングがロトムの苦手なマスカーニャ（あく複合ゆえサイコファング無効）以外の相手をカバーします。

**マフォクシー**（5位）はほのお/エスパーで、ロトムのほのお耐性（×0.5）がパーティ内の弱点分散に寄与します。マフォクシーの特殊打点とロトムの両刀打点で、物理受け・特殊受けの双方に対応できる構成になります。

---

## まとめ

M-4のウォッシュロトムは使用率17位（M-3: 20位）に上昇し、攻撃面の課題を解消したシーズンでした。

- **ハイドロポンプが0%→99.0%で新規標準化**：M-3はでんき単打点でじめんタイプに反撃できませんでしたが、M-4でみず打点を得てカバルドンなどに×2が通るようになりました
- **こだわりスカーフ型が26.5%まで拡大**（M-3: 14.5%）：おくびょう18.9%・ひかえめ20.7%の攻撃特化型が耐久型（ずぶとい48.3%）と並ぶ選択肢に
- **弱点はくさタイプのみ**（ふゆうでじめん無効）だが、マスカーニャ（6位・トリックフラワー97.3%）には打点のぶつけ合いで一方的に不利

はがね×0.25を筆頭に広い耐性を持ちながら、ふゆうでじめんタイプの主力技を無効化できる点が基本的な強みです。耐久型・スカーフ型のどちらを選ぶかは、パーティ内でロトムに求める役割（受けて立て直すか、先制打点で崩すか）で判断する形になります。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
