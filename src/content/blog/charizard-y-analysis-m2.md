---
title: 'メガリザードンY M-2 使用率5位 ひでり構築と技構成'
description: 'チャンピオンズM-2使用率5位メガリザードンY構築を徹底解説。C159×ひでりのトップクラス火力、ソーラービーム即発動で技構成の幅が広く、晴れ展開の組み方・いわ4倍弱点への対策まで実データをもとに解説します。'
updatedDate: '2026-06-05'
pubDate: '2026-06-05'
draft: false
heroImage: '../../assets/hero-charizard-y-m2.png'
---

<style>
.poke-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  vertical-align: middle;
  margin-right: 4px;
}
.poke-icon-lg {
  display: block;
  width: 80px;
  height: 80px;
  margin: 0 auto 8px;
}
.type-badge {
  display: inline-block;
  width: 52px;
  height: 52px;
  vertical-align: middle;
  margin: 2px;
}
.type-badge-sm {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin: 1px 2px;
}
.item-icon {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin-right: 4px;
  object-fit: cover;
}
.pokemon-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 20px 0;
}
.pokemon-header img {
  width: 96px;
  height: 96px;
}
.type-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 8px 0;
}
.build-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.partner-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 12px;
  margin: 16px 0;
}
.partner-card {
  text-align: center;
  padding: 8px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}
.partner-card img {
  width: 56px;
  height: 56px;
  display: block;
  margin: 0 auto 4px;
}
.partner-card .name {
  font-size: 0.75rem;
  font-weight: bold;
}
.partner-card .rate {
  font-size: 0.7rem;
  color: #666;
}
</style>

<div class="pokemon-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" />
  <div>
    <h2 style="margin:0 0 8px">メガリザードンY</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong style="color:#dc2626">5位</strong>（リザードン全体） ／
      メガ石採用率 <strong style="color:#ea580c">63.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

M-2シーズンシングルバトルでリザードン全体は**使用率5位**を記録。リザードナイトYの採用率は**63.6%**、リザードナイトXは**34.9%**で、同じポケモンでメガ型が二極化しているのが特徴です。Y型は**C種族値159とひでりによるほのお技×1.5補正**を活かした特殊エース、X型はりゅうのまい起点の物理積みエースという役割分担になっており、対策側は型読みを強いられます。本記事ではY型に絞って採用型・技構成・有利不利の相手を実データで解説します。

---

## なぜ今、メガリザードンYが強いのか

メガリザードンYの強さは、メガ後特性**ひでり**を前提に成立しています。ひでりは場に出た（メガ進化した）ターンに天候を「にほんばれ」にする特性で、相手がすなあらし・あめなどを展開していても繰り出した瞬間に上書きできます。この「にほんばれ」状態がもたらす2つの効果が、Yの主力運用を支えています。

### 1. ひでり×C159で実質火力がトップクラス

メガリザードンYのとくこうは**159**。これだけでも環境トップクラスの数値ですが、にほんばれ下ではほのお技が×1.5倍になります。かえんほうしゃ（威力90）の実質ダメージ計算をすると:

<div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:14px;margin:16px 0;font-size:0.9em">
  <strong>かえんほうしゃ実質威力（ひでり補正あり）</strong><br>
  <span style="font-size:1.1em;color:#ea580c">
    威力90 × タイプ一致補正1.5 × ひでり1.5 = <strong>実質威力202.5</strong>
  </span><br>
  <small style="color:#777;margin-top:4px;display:block">※ひかえめならCが約10%上がり、ダメージが約1割上乗せされる</small>
</div>

通常のほのおタイプと比べ、**毎ターンほのお技が×1.5補正で安定して撃てる**点が差別化要因です。

### 2. ソーラービーム即発動で技範囲が広がる

通常のソーラービームは溜め1ターンが必要ですが、にほんばれ下では**1ターンで即発動**します。ソーラービームの採用率が61.0%という高さを誇るのは、Yのメインウェポンであるほのお・ひこう技が等倍以下に止まるみず・じめん系の高耐久ポケモン（アシレーヌ・カバルドン・イダイトウなど）に対する**サブウェポン**として機能するからです。これらにくさ技は×2が通り、ほのお・ひこう一致技だけでは崩しきれない相手を抜けるようになります。一方ガブリアス（ドラゴン/じめん）はくさ×2×0.5=等倍止まりですが、それでもC159の高火力で削りは入れられます。

後続でほのおタイプを採用していれば、ウルガモスのほのおのまい等もにほんばれ補正の恩恵を受けられます。

### 3. にほんばれ下ではみず弱点が実質等倍に抑えられる

にほんばれ下では**みず技の威力が0.5倍に弱化**します。メガリザードンYはみず×2弱点ですが、ひでり下なら ×2×0.5=**実質×1（等倍）**まで軽減できます。アシレーヌ（みず/フェアリー・使用率4位）のうたかたのアリア・なみのり、イダイトウ(オス)（みず/ゴースト・8位）のたきのぼり、スターミー（みず/エスパー・20位）のアクアブレイク89.2%など、環境のみず技に対して被ダメージが半減します。

ひでりは火力面（×1.5補正）だけでなく、**みず弱点を実質等倍まで打ち消す防御効果も併せ持つ**点が、メガリザードンY運用の安定性を支えています。なお、いわ×4・でんき×2の弱点はひでりで軽減できないため、これらは依然として大きな脅威です。

---

## 基本スペック

### 種族値（メガリザードンY）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">104</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:79.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">159</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">115</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">634</span>
  </div>
</div>

C種族値159は現環境の特殊アタッカーで最上位クラスです。D種族値115はXのD85より大幅に高く、対面で特殊技を1発耐えてC159で殴り返す立ち回りが可能になります。一方でB種族値78は低く、物理技には脆い。S種族値100はおくびょう最速でS**167**止まりで、環境TOP50のうち以下のポケモンはメガ後の最速SがメガリザードンYを上回ります。

**メガ進化後にメガリザードンYを上回る相手**

- メガゲッコウガ（28位・メガ石40.8%・S142 → S213）
- メガミミロップ（13位・メガ石96.9%・S135 → S205）
- メガマフォクシー（25位・メガ石96.5%・S134 → S204）
- メガゲンガー（10位・メガ石82.4%・S130 → S200）
- メガスターミー（20位・メガ石97.7%・S120 → S189）
- メガルカリオ（9位・メガ石97.4%・S112 → S180）
- メガフラエッテ(永遠)（17位・メガ石97.4%・S102 → S169）
- メガキラフロル（15位・メガ石54.2%・S101 → S168）

**メガを介さず素早さで上回る相手**

- マスカーニャ（3位・S123 → S192）
- ゲッコウガ素体（28位・S122 → S191）
- ガブリアス（1位・S102 → S169）

特にガブリアス（S169）とメガフラエッテ(永遠)（S169）はおくびょう最速のメガリザードンY（S167）を**2差で上回る**ため、ガブリアスのがんせきふうじ採用率40.0%・いわなだれ採用率23.1%（いわ×4）、メガフラエッテのムーンフォース等が先に通ります。**おくびょう最速かひかえめCSの選択**は、こうした上位S帯との関係で決まります。

### メガ進化前後の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ後（Y）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">変化量</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px;border:1px solid #cbd5e1">84</td>
  <td style="padding:8px;border:1px solid #cbd5e1">104</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+20</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">109</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">159</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+50</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px;border:1px solid #cbd5e1">115</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
</tbody>
</table>
</div>

とくこう+50という変化量はXの+21と比べて大きく上回ります。さらにとくぼう+30によりD115となり、特殊耐久が大幅強化されています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;vertical-align:top">
    <div style="margin-bottom:6px"><strong>×4</strong></div>
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin:2px"><br>
    <div style="margin:8px 0 6px"><strong>×2</strong></div>
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;vertical-align:top">
    <div style="margin-bottom:6px"><strong>×1/2</strong></div>
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <div style="margin:8px 0 6px"><strong>×1/4</strong></div>
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;vertical-align:top">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fee2e2;border:1px solid #fca5a5;border-radius:8px;padding:12px;margin:12px 0">
  <strong style="color:#dc2626">いわ×4弱点の重み</strong><br>
  メガリザードンYは<strong>いわ技を×4</strong>で受けます。ステルスロックが設置された場で繰り出すと、最大HPの<strong>1/2</strong>を場に出た瞬間に削られます。環境上位ではガブリアス（がんせきふうじ40.0%・いわなだれ23.1%）が直接いわ技で焼き、カバルドン（ステルスロック84.4%）はステルスロックでメガリザードンYの繰り出しを咎めます。
</div>

---

## 主要型の解説

### 型1: ひでりソーラービーム型（ひかえめ・CS）

<div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>ひでりソーラービーム型</strong><br>
    <small style="color:#555">ひかえめ（最多採用）／ C32 S32 ／ 特性 もうか（86.1%）→メガ後ひでり ／ 持ち物 リザードナイトＹ</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#fef3c7">
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">1</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひでり込みで実質202.5。安定した主力技</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">2</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-11-grass.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひでりで即発動。みず・じめん・いわへの打点</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">3</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-02-flying.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひこう一致技。かくとう・むし・くさへ。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">4</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">最大火力の捨て技。フィニッシュに。命中90%・C-2</td>
</tr>
</tbody>
</table>
</div>
</div>

**採用率データとの照合**: ソーラービーム61.0%・かえんほうしゃ42.4%・エアスラッシュ32.9%・オーバーヒート26.6%・はねやすめ22.1%はY型の主力技です（採用率はリザードン全体での集計だが、X型主流のフレアドライブ33.3%・りゅうのまい26.9%・ドラゴンクロー24.0%とは技プールが分かれており、上記の特殊技群はY型の構成を反映しています）。

**ひかえめC振りの効果**: C種族値159にひかえめ補正（×1.1）がかかり、おくびょう型より約1割高い特殊火力になります。ひでり×タイプ一致補正の実質威力202.5でD無振りの中耐久ポケモンを2発圏に入れる火力です。

**ソーラービームの刺さり先**: メインのほのお・ひこう一致技が等倍以下に止まる、みず・じめん系の高耐久ポケモンを崩すためのサブウェポンです。環境上位では:
- **カバルドン**（じめん単）: くさ×2弱点を突ける。ステルスロック撒きの起点役を即発動ソーラービームで牽制できる
- **イダイトウ**（みず/ゴースト）: くさ×2×1=×2弱点を突ける
- **ガブリアス**（ドラゴン/じめん）: くさ×2×0.5=等倍止まりだがC159の威力で削りは入る

---

### 型2: おくびょう最速型（おくびょう・CS）

<div style="background:#f0fdf4;border:1px solid #4ade80;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>おくびょう最速型</strong><br>
    <small style="color:#555">おくびょう（30.0%採用）／ C32 S32 ／ 特性 もうか（86.1%）→メガ後ひでり ／ 持ち物 リザードナイトＹ</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#dcfce7">
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">1</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #86efac">安定打点。ひでり込みでトップクラスの火力</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">2</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-11-grass.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #86efac">ひでりで即発動。みず/いわ/じめんへの打点</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">3</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-02-flying.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #86efac">ひこう一致打点。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">4</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>はねやすめ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-00-normal.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #86efac">HP50%回復。S高い分先に動いて回復できる</td>
</tr>
</tbody>
</table>
</div>
</div>

**おくびょう型とひかえめ型の差**: おくびょう最速のSは167で、種族値S100帯のウルガモス（同S167で同速）やそれ以下の中速ポケモンを上から動けます。一方でガブリアス（S169）・マスカーニャ・ゲッコウガ・スターミー・ゲンガー・ミミロップ・マフォクシーには先手を取れません。性格採用率はひかえめ32.7%・おくびょう30.0%。

---

### 型3: HB+CS複合型（ひかえめ）

<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>HB+CS複合型</strong><br>
    <small style="color:#555">ひかえめ ／ H32 B20 C11 S3（3.7%採用）／ 特性 もうか（86.1%）→メガ後ひでり ／ 持ち物 リザードナイトＹ ／ 技構成 かえんほうしゃ・ソーラービーム・エアスラッシュ・はねやすめ</small>
  </div>
</div>

<p style="font-size:0.88em;color:#555;margin:8px 0">
H32 B20の物理耐久に厚く振り、HP実数値を185まで上げる型です。CS主流のCS+h型（H2のみ＝HP実数値155）と比べHP実数値が30高く、ガブリアスのスケイルショット・マスカーニャのトリックフラワー・ハッサムのバレットパンチなど、ひこうで無効化できない物理技を1発耐えやすくなります。CS両振りの火力は落ちますが、低耐久のYを物理対面でも崩されにくくする選択として3.7%が採用しています。
</p>
</div>

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">用途・補足</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>ソーラービーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>61.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひでりで即発動。Y最多採用技。ほのお・ひこうが等倍以下に止まるみず・じめん系を崩すサブウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひでり×一致補正込みで実質202.5。安定したほのお打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう一致技。かくとう・くさへ。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中90%・C-2の代わりに最大火力。ひでり込みで実質292.5</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP50%回復。S優位を活かして先に回復できる場面も</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.85em;color:#666;margin:8px 0">
※採用率データ（X/Y合算）にはフレアドライブ33.3%・ニトロチャージ28.9%も含まれますが、これらは物理アタッカーであるメガリザードンX型の技です。C159の特殊運用が前提のY型では採用されないため、上表からは除外しています。
</p>

---

## 天候パーティ構築でのメガリザードンY

メガリザードンYは単独でひでり＋C159＋ソーラービーム即発動が完結するため、天候パーティとしての構築は限定的です。同居率TOP10にもようりょくそ・すなかき等の天候依存特性ポケモンは入っていません。

ひでり下のほのお技×1.5の恩恵を受ける後続として、ウルガモス（ほのおのまい等のほのお技が晴れ補正を受ける）を組む構築は稀に見られますが、メジャーではありません。なお、くさタイプのフシギバナはメガ進化採用率93.2%でメガフシギバナ（あついしぼう）になるため、ようりょくそ運用は事実上ありません。

**天候の取り合い**: ひでりはメガ進化したターンに天候を「にほんばれ」にします。相手があめ・すなあらしを先に展開していても、メガリザードンYが繰り出されたターンに天候は「にほんばれ」へ書き換わります。逆に相手があとから天候変化技や天候特性ポケモンを繰り出した場合は上書きされます。

---

## 苦手な相手と有利な相手（TOP30から抽出）

選定基準：使用率TOP30のうち、相手の主力技（採用率20%以上）でこちらの弱点を突かれる相手を「苦手」、こちらの技で弱点を突けて相手の主力技ではこちらが半減以下に抑えられる相手を「有利」とする。

### 苦手な相手

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#fee2e2">
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">相手</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">苦手な理由（技は採用率付き）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">じしん99.2%はひこうで無効化できるものの、S169でおくびょう最速のメガリザードンY（S167）を抜き、先制から放たれるがんせきふうじ40.0%・いわなだれ23.1%でいわ×4を一発で焼かれる。さらにステルスロック50.7%で繰り出し自体も最大HP1/2で咎められる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">10まんボルト66.9%でこちらでんき×2。S種族値85で遅いが、ガブリアス・マスカーニャ等の上位S帯のあとに後出しできる。ラスターカノン55.7%は×0.5（はがね→ほのお0.5×ひこう1）で軽い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ステルスロック84.4%でメガリザードンYの繰り出しに最大HP1/2のダメージを蓄積。あくび94.2%で流される。じしん98.0%はひこうで無効だが、ステルスロック撒きの起点役として致命的</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">10まんボルト47.6%でこちらでんき×2。かえんほうしゃ47.8%はこちら半減だが、エアスラッシュ55.6%は等倍（ひこう→ほのお1×ひこう1）。でんき技採用個体には特に不利</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">メガ石採用率97.7%、メガ後S189（おくびょう最速）でメガリザードンY（S167）を抜く。主力のアクアブレイク89.2%はひでり下で実質等倍まで軽減できるものの、しねんのずつき39.4%・サイコカッター24.7%採用のエスパー個体でも、エスパー技は等倍止まりで弱点は突かれない。低耐久（H78/B78）のこちらは厳しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0479-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">ハイドロポンプ98.5%はひでり下で実質等倍まで軽減できるが、ボルトチェンジ88.7%・10まんボルト56.8%のでんき×2は軽減できず確定圏。ボルトチェンジで対面操作もされ、ひでりを撒き直す手間も加わる</td>
</tr>
</tbody>
</table>
</div>

### 有利な相手

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#dcfce7">
  <th style="padding:8px 12px;border:1px solid #86efac;text-align:left">相手</th>
  <th style="padding:8px 12px;border:1px solid #86efac;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">むし/はがねにほのお技×4。S167で最速ハッサム（S実数値128）を大幅に抜くが、主力のバレットパンチ99.7%は優先度+1の先制技でSの優位は無効化される。ただしバレットパンチ×0.5（はがね→ほのお0.5×ひこう1・テクニシャン込み実質威力60相当）は低耐久（H78/B78）でも耐えられる範囲のため、先制バレットパンチを受けてから同ターン中にかえんほうしゃ×4で焼く展開が成立する。インファイト72.4%は×0.5（かくとう→ほのお1×ひこう0.5）、はたきおとす53.6%は等倍だが、メガリザードンY側の持ち物はリザードナイトYで落とせない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">くさ/どくにほのお技×2・ひこう技×2。主力のだいちのちから88.4%はこちらひこうで無効、ギガドレイン56.9%は×0.25（くさ→ほのお0.5×ひこう0.5）、ヘドロばくだん55.0%は等倍（どく→ほのお1×ひこう1）でこちらの弱点を突く打点はない。ひでり下のかえんほうしゃで圧倒できる。ただしメガフシギバナの場合はあついしぼうでほのお×1相当に落ちる点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">はがね/ゴーストにかえんほうしゃ×2（はがね2×ゴースト1）。S種族値60に対し最速S167で大幅に先制し、ひでり込みのかえんほうしゃで上から焼ける。かげうち96.2%は優先度+1だが等倍（ゴースト→ほのお1×ひこう1）かつC97なので致命傷にはならない。ポルターガイスト67.6%・シャドーボール26.5%も等倍止まり、アイアンヘッド30.7%は×0.5（はがね→ほのお0.5×ひこう1）、せいなるつるぎ31.7%は×0.5（かくとう→ほのお1×ひこう0.5）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #86efac"><img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）</td>
  <td style="padding:8px 12px;border:1px solid #86efac">あく/はがねにかえんほうしゃ×2（あく1×はがね2）。S種族値50に対し最速S167で大幅に先制し、ひでり込みのかえんほうしゃで上から削れる。ただしふいうち99.0%は等倍（ほのお1×ひこう1）でA135の先制技が痛く、低耐久のこちらは確定数次第で拮抗する。条件付きの有利</td>
</tr>
</tbody>
</table>
</div>

---

## 相性の良いパーティメンバー

リザードンの同居率TOP10（M-2、最新クロール）は以下です。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ（同居率1位）</div>
    <div class="rate">特殊エースの補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア（2位）</div>
    <div class="rate">物理受け・とんぼがえり</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス（3位）</div>
    <div class="rate">ステルスロック展開役</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス（4位）</div>
    <div class="rate">いわ・でんき受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ（5位）</div>
    <div class="rate">高速物理アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン（6位）</div>
    <div class="rate">ステルスロック展開役</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)（7位）</div>
    <div class="rate">みず物理アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ（8位）</div>
    <div class="rate">ばけのかわ起点・つるぎのまい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ（9位）</div>
    <div class="rate">かくとう・はがねアタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド">
    <div class="name">ギルガルド（10位）</div>
    <div class="rate">いわ受け・キングシールド</div>
  </div>
</div>

**アーマーガア（同居率2位）の役割**: 同居率2位の物理受け。はねやすめ98.1%・てっぺき63.5%で耐久を確保し、とんぼがえり62.1%でメガリザードンYを安全に後投げできます。ガブリアスのじしん99.2%をひこうで無効化できる点は重要ですが、いわ技は「はがね半減×ひこう弱点＝等倍」で受けるため、いわ技の受け役にはなりません。設置技除去のきりばらいは採用率13.6%で少数派なので、ステルスロック対策の主役にはなりにくい点に注意。

**ガブリアス・カバルドン（同居率3位・6位）の役割**: 自軍に採用すればステルスロック撒き役。ガブリアスのステルスロック採用率は50.7%、カバルドンは84.4%。相手のメガリザードンY・ウルガモス等のいわ×4ポケモンを削る起点になります。「対面で苦手な相手」と「自軍に入れたいパートナー」が同一ポケモンなのは、ステルスロックという技自体の役割の重さを示しています。

**ブリジュラス（同居率4位）の役割**: メガリザードンYが弱点とするいわ（はがね0.5×ドラゴン1=×0.5）・でんき（はがね0.5×ドラゴン0.5=×0.25）・みず（はがね0.5×ドラゴン0.5=×0.25）をすべて半減以下で受けられる耐性補完。メガリザードンYが苦手なウォッシュロトムのハイドロポンプも半減（×0.25）で受け、10まんボルト（採用率66.9%）で反撃できます。

**後続のほのおアタッカー**: ウルガモス（使用率18位）は同居率TOP10圏外ながら、ひでり下で自分のほのお技も×1.5になる強化対象です。ただし同居率上位はアシレーヌ・アーマーガア・ガブリアスなど天候非依存のポケモンが占めており、天候パーティとしての採用は限定的。晴れ下のソーラービーム即発動と一致補正で**単独でも完結する特殊エース**としての運用が主流です。

---

## XとYの使い分けまとめ

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:10px 14px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1">メガリザードンX</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1;background:#fefce8">メガリザードンY</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">採用率</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">34.9%</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>63.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">主力の向き</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">物理崩し・積みエース</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>特殊崩し・天候展開</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong style="color:#dc2626">159</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくせい</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">かたいツメ（接触技×1.3）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>ひでり（ほのお×1.5）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">最大弱点</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">4倍弱点なし（3種2倍）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2"><strong>いわ4倍（ステルスロック1/2）</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ステルスロックダメージ</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">1/4</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2"><strong>1/2（致命的）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">積み技</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">りゅうのまい / ニトロチャージ</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">なし（火力押し）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">天候シナジー</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">なし</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>ひでり自己完結（天候パーティ採用は限定的）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">Yを選ぶ状況</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">火力押し・天候展開・特殊受けの多い環境</td>
</tr>
</tbody>
</table>
</div>

---

## データ分析①：リザードナイトY 63.6% vs X 34.9% — 同一ポケモンでメガ型が二極化する構造

同じポケモンの2系統のメガ石が両方とも30%超で採用されるのは現環境でも稀です。リザードンの場合、リザードナイトY（63.6%）とリザードナイトX（34.9%）が併存し、それぞれ別系統の技プールに分かれています。

| 系統 | 主力技と採用率 | 役割 |
|---|---|---|
| Y型主流 | ソーラービーム61.0%・かえんほうしゃ42.4%・エアスラッシュ32.9%・オーバーヒート26.6%・はねやすめ22.1% | C種族値159＋ひでりの特殊エース |
| X型主流 | フレアドライブ33.3%・ニトロチャージ28.9%・りゅうのまい26.9%・ドラゴンクロー24.0%・かみなりパンチ18.2% | かたいツメ＋りゅうのまい起点の物理積みエース |

技採用率はリザードン全体での集計ですが、特殊技（ソーラービーム・かえんほうしゃ・オーバーヒート）と物理技（フレアドライブ・ニトロチャージ・ドラゴンクロー）が明確に分かれており、合算採用率がそのまま各メガ石の採用率（Y=63.6%、X=34.9%）に近くなっています。**対策側はリザードン選出時にY型かX型かを読まないと対面を誤る**——Y型を想定してD振り受けを選ぶと、X型のドラゴンクロー＋りゅうのまいで物理側から崩される、という非対称な読み合いが発生します。

## データ分析②：Y型主力技と環境TOP10のタイプ相性カバレッジ

Y型の主力2技（かえんほうしゃ＋ソーラービーム）が環境TOP10へどう刺さるかを倍率で示します。

| 順位 | ポケモン | かえんほうしゃ | ソーラービーム |
|---|---|---|---|
| 1 | ガブリアス（ドラゴン/じめん） | ×0.5（ほのお0.5×じめん1） | ×1（くさ2×ドラゴン0.5） |
| 2 | ブリジュラス（はがね/ドラゴン） | ×1（はがね2×ドラゴン0.5） | ×0.25（くさ0.5×はがね0.5） |
| 3 | マスカーニャ（くさ/あく） | ×2（くさ2×あく1） | ×0.5（くさ半減） |
| 4 | アシレーヌ（みず/フェアリー） | ×0.5（ほのお0.5×フェアリー1） | ×2（くさ2×フェアリー1） |
| 5 | リザードン（ほのお/ひこう） | ×0.5 | ×0.25（くさ0.5×ひこう0.5） |
| 6 | アーマーガア（はがね/ひこう） | ×2（はがね2×ひこう1） | ×0.25 |
| 7 | カバルドン（じめん） | ×1 | ×2 |
| 8 | イダイトウ(オス)（みず/ゴースト） | ×0.5 | ×2（くさ2×ゴースト1） |
| 9 | ルカリオ（かくとう/はがね） | ×2（はがね2×かくとう1） | ×0.5（かくとう1×はがね0.5） |
| 10 | ゲンガー（ゴースト/どく） | ×1（ほのお1×ゴースト1×どく1） | ×0.5（くさ1×ゴースト1×どく0.5） |

かえんほうしゃ単体ではTOP10のうち**3体に×2、3体に×1、4体に×0.5以下**。ソーラービームは**3体に×2、1体に×1、6体に×0.5以下**。**2技を併用すると、リザードンを除くTOP10の9体すべてに×1以上の打点が成立**します（同タイプのリザードン以外でカバレッジが不足する相手はいない）。ソーラービームの採用率が61.0%と最も高い理由は、ほのお技を半減・無効化するみず／じめん／いわタイプの高耐久相手（環境上位ではアシレーヌ・カバルドン・イダイトウなど）を弱点で抜くためです。

---

## まとめ

メガリザードンYはM-2シーズンで全リザードン採用の**63.6%**を占める特殊エースです。

- **C種族値159×ひでり**でかえんほうしゃ実質威力202.5（ひかえめならC232）
- **ソーラービーム即発動**でアシレーヌ・カバルドン・イダイトウ等のみず/じめん受けに×2の打点
- **いわ×4・ステルスロック最大HP1/2**——カバルドン（ステルスロック84.4%）・ガブリアス（いわ技合算約63%）が苦手
- **同居率1〜4位はアシレーヌ・アーマーガア・ガブリアス・ブリジュラス**で、ステルスロック展開役（ガブリアス・カバルドン）と耐性補完（アーマーガア・ブリジュラス）を組み合わせるのが定番
