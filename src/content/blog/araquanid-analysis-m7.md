---
title: '【ポケモンチャンピオンズ】オニシズクモ 考察 M-7 シーズン 使用率79位の4型解説'
description: 'M-7シーズン使用率79位（M-6: 89位）のオニシズクモを考察。ねばねばネット採用率86.3%・ミラーコート78.3%と高く、物理型・特殊耐久型・両刀型・特殊アタッカー型の4型を比較し、ガブリアスなど苦手、カバルドンなど得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-28'
heroImage: '../../assets/hero-araquanid-m7.png'
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
  <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ" />
  <div>
    <h2 style="margin:0 0 8px">オニシズクモ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">79位</strong>（M-6: 89位）　持ち物: <strong>オボンのみ 53.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのオニシズクモは使用率79位です（M-6: 89位）。特性はすいほう（99.4%）です。技はねばねばネット（採用率86.3%）とミラーコート（78.3%）が高く、オニシズクモは攻撃技と持ち物の違いから4つの型に分かれます。

---

## オニシズクモの基本スペック

<!-- gate:rows start id=base_stats facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">68</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:46%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">92</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">132</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:21%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">42</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">454</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

4型のうち物理型・特殊耐久型・特殊アタッカー型の3型が、ミラーコートを型の4技に入れています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ひこう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">みず</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

### 特性

<strong>すいほう（99.4%）</strong>がほぼ全ての個体の特性です。ほのおタイプの技で受けるダメージが半減し、みずタイプの技の威力が2倍になり、やけど状態にならない効果があります。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねばねばネット</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の場をねばねばネット状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミラーコート</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">78.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度-5。使ったターンに相手から受けた特殊技のダメージを2倍にして返す。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアブレイク</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手の防御を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">38.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">水中状態の相手には威力が2倍になる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こごえるかぜ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の素早さを1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きゅうけつ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">21.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手に与えたダメージの1/2自分のHPを回復する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">とびかかる</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の攻撃を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">がむしゃら</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の残りHPから自分の残りHPを引いた数値のダメージを与える。相手のHPが自分のHP以下なら失敗する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.4%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物の組み合わせから、4つの型を紹介します。

### 型1：物理型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すいほう（99.4%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H32-A32-B2<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・アクアブレイク<br>
・きゅうけつ<br>
・ねばねばネット<br>
・ミラーコート<br>
選択技：とびかかる
</div>
</div>
</div>

こうげきに振り、アクアブレイクときゅうけつで攻める型です。

<!-- gate:rows start id=card:1 facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
**他の型との違い:**

- きゅうけつ：この型は必ず持ち、特殊アタッカー型では選択技
- 4つの型で最も低い実数値：とくこう63
<!-- gate:rows end id=card:1 -->

---

### 型2：特殊耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すいほう（99.4%）<br>
<strong>性格:</strong> おだやか<br>
<strong>EV:</strong> H32-D28-S6<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・なみのり<br>
・こごえるかぜ<br>
・ねばねばネット<br>
・ミラーコート<br>
選択技：れいとうビーム
</div>
</div>
</div>

とくぼうに振り、なみのりとこごえるかぜを持つ型です。

<!-- gate:rows start id=card:2 facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
**他の型との違い:**

- 他の型に無い技：こごえるかぜ
- 4つの型で最も高い実数値：とくぼう198
<!-- gate:rows end id=card:2 -->

---

### 型3：両刀型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">両刀型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すいほう（99.4%）<br>
<strong>性格:</strong> ゆうかん<br>
<strong>EV:</strong> H32-A32-B2<br>
<strong>持ち物:</strong> しんぴのしずく
</div>
<div>
<strong>技構成:</strong><br>
・アクアブレイク<br>
・なみのり<br>
・とびつく<br>
・ねばねばネット<br>
選択技：れいとうビーム
</div>
</div>
</div>

アクアブレイクとなみのりの物理・特殊2つのみず技を持つ型です。

<!-- gate:rows start id=card:3 facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
**他の型との違い:**

- 他の型に無い技：とびつく
- 持ち物：しんぴのしずく（みずタイプの技の威力が1.2倍になる）
- 4つの型で最も低い実数値：すばやさ55
<!-- gate:rows end id=card:3 -->

---

### 型4：特殊アタッカー型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0752-00.webp" alt="オニシズクモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すいほう（99.4%）<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H26-C32-S8<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ハイドロポンプ<br>
・むしのさざめき<br>
・れいとうビーム<br>
・ミラーコート<br>
選択技：きゅうけつ
</div>
</div>
</div>

ハイドロポンプ・むしのさざめき・れいとうビームの特殊攻撃技3種を持ち、とくこうに振った型です。

<!-- gate:rows start id=card:4 facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
**他の型との違い:**

- 他の型に無い技：ハイドロポンプ・むしのさざめき
- れいとうビーム：この型は必ず持ち、特殊耐久型・両刀型では選択技
- 4つの型で最も高い実数値：とくこう112・すばやさ70
- 4つの型で最も低い実数値：HP169
<!-- gate:rows end id=card:4 -->

---

## データ分析：M-6からの技・持ち物・性格採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こごえるかぜ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+15.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アクアブレイク</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">68.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-13.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">なみのり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+12.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">27.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">21.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-6.2pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ミラーコート</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">74.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">78.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+4.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ねばねばネット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">82.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">86.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+3.6pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物・性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+16.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">オボンのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">39.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">53.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+13.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">27.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-8.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">しんぴのしずく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">14.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-4.4pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
- おだやか：1.9%→18.2%（+16.3pt）。特殊耐久型が選んでいるほか、特殊アタッカー型の一部の個体も選んでいるため、型の増減とは言い切れません。
- こごえるかぜ：9.9%→24.9%（+15.0pt）。特殊耐久型だけが持つため、この変化はその型の増減を示します。
- オボンのみ：39.5%→53.0%（+13.5pt）。物理型・特殊耐久型・特殊アタッカー型が持つため、型の増減とは言い切れません。
- アクアブレイク：68.5%→55.5%（-13.0pt）。両刀型・物理型に共通のため、型の増減とは言えません。
- なみのり：26.0%→38.5%（+12.5pt）。両刀型・特殊耐久型に共通のため、型の増減とは言えません。
- いじっぱり：36.0%→27.8%（-8.2pt）。物理型だけが選んでいるため、この変化はその型の増減を示します。
- きゅうけつ：27.9%→21.7%（-6.2pt）。物理型が持ち、特殊アタッカー型でも選択技のため、型の増減とは言えません。
- しんぴのしずく：19.3%→14.9%（-4.4pt）。両刀型だけが持つため、この変化はその型の増減を示します。
<!-- gate:rows end id=diff_movers -->

---

## 苦手なポケモン

使用率上位のうち、相手の型が変わっても一貫して不利になる相手のみを掲載します。

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
<!-- gate:rows start id=weak facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発。ガブリアスのげきりん（採用率27.0%）は確定2発で、S62対S253（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは乱数4発（96%）。アシレーヌのムーンフォース（採用率98.3%）は確定4発（オニシズクモのオボンのみ込み）で、S62対S80で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発（ばけのかわ込み）。ミミッキュのシャドークロー（採用率48.8%）は乱数2発（99%）で、S62対S148で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発。メガリザードンXのかみなりパンチ（採用率18.8%・少数派）は確定2発で、S62対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊アタッカー型のハイドロポンプは乱数4発（99%）（相手のオボンのみ込み）。ブリジュラスの10まんボルト（採用率63.9%）は乱数3発（65%）で、S70対S105で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊耐久型の選択技れいとうビームは確定3発。メガカイリューの10まんボルト（採用率59.5%）は確定3発で、S68対S152で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発。セグレイブのきょけんとつげき（採用率86.4%）は確定2発で、S62対S139で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは乱数2発（96%）。メガメタグロスのサイコファング（採用率73.5%）は確定2発で、S62対S162で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊アタッカー型のれいとうビームは確定1発。メガボーマンダのすてみタックル（採用率73.5%）は確定1発で、S70対S172で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定1発。メガライチュウYのでんじほう（採用率96.5%）は確定1発で、S62対S200で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定4発。ウォッシュロトムのボルトチェンジ（採用率86.2%）は確定4発（オニシズクモのオボンのみ込み）で、S62対S106で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発。カバルドンのじしん（採用率97.3%）は確定3発で、S62対S67で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊耐久型のなみのりは確定4発。メガリザードンYのソーラービーム（採用率65.9%）は確定5発（オニシズクモのオボンのみ込み）で、S68対S120で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">両刀型のなみのりは確定2発。メガルカリオZのあくのはどう（採用率73.5%）は確定4発で、S55対S223で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">両刀型のアクアブレイクは確定1発。ヒートロトムのボルトチェンジ（採用率89.3%）は確定2発で、S55対S106で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">両刀型のアクアブレイクは確定2発。ゲッコウガのヘドロウェーブ（採用率73.3%）は確定3発で、S55対S174で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のアクアブレイクは確定2発。アローラキュウコンのフリーズドライ（採用率73.0%）は乱数3発（94%）で、S62対S177で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でオニシズクモと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" loading="lazy">
    <div class="name">イエッサン(オス)</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0478-00.webp" alt="ユキメノコ" loading="lazy">
    <div class="name">ユキメノコ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" loading="lazy">
    <div class="name">ウルガモス</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0900-00.webp" alt="バサギリ" loading="lazy">
    <div class="name">バサギリ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率2位・メガルカリオZで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率4位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イエッサン(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ユキメノコ<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ウルガモス<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">バサギリ<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ライチュウ<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガライチュウYで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オニシズクモの弱点：いわ技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オニシズクモの弱点：でんき技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オニシズクモの弱点：ひこう技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">セグレイブ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ボーマンダ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ライチュウ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ウォッシュロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○6</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○7</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○8</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝オニシズクモの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ガブリアス＝じしん・かえんほうしゃ・りゅうせいぐん；アシレーヌ＝ムーンフォース・うたかたのアリア・アクアジェット；ミミッキュ＝じゃれつく・かげうち・シャドークロー・ウッドハンマー；メガリザードンX＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；ブリジュラス＝りゅうせいぐん・ラスターカノン・10まんボルト；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；セグレイブ＝こおりのつぶて・じしん・きょけんとつげき・つららおとし；メタグロス＝バレットパンチ・サイコファング・れいとうパンチ・じしん・かみなりパンチ；ボーマンダ＝すてみタックル・じしん；ライチュウ＝でんじほう・きあいだま・ねこだまし・ボルトチェンジ；ウォッシュロトム＝ハイドロポンプ・ボルトチェンジ・10まんボルト</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=d822968a70cc3cb605474cb7c22c6e3de093fed1 -->
**強み**

- 得意な相手は6体です。使用率上位では、カバルドン（4位）にアクアブレイク、メガリザードンY（6位）・ルカリオ（7位）になみのりで勝てます。
- タイプ相性では、みず・こおり・かくとう・じめん・はがねを半減以下で受けられます。

**弱み**

- 苦手な相手は11体です。使用率上位では、ガブリアス（1位）のげきりん、アシレーヌ（2位）のムーンフォース、ミミッキュ（3位）のシャドークローで先に倒されます。
- 弱点はでんき・ひこう・いわです。

**型の選び分け**

- 「物理型」：きゅうけつを必ず持つ（特殊アタッカー型では選択技）。
- 「特殊耐久型」：他の型に無い技はこごえるかぜ。
- 「両刀型」：他の型に無い技はとびつく。
- 「特殊アタッカー型」：他の型に無い技はハイドロポンプ・むしのさざめき。
- 苦手/得意の判定は、どの型でも同じです。

**M-6からの変化**

- 使用率は79位です（M-6: 89位）。
- 採用率の変化が大きいのはこごえるかぜ（+15.0pt）・オボンのみ（+13.5pt）・アクアブレイク（-13.0pt）です。
<!-- gate:rows end id=summary -->

---

*関連記事：[ガブリアス考察 M-7](/blog/garchomp-analysis-m7/)・[オニシズクモ考察 M-2](/blog/araquanid-analysis-m2/)*
