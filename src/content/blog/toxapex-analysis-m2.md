---
title: '【ポケモンチャンピオンズ】ドヒドイデ考察 M-2 使用率57位 さいせいりょくの耐久型と立ち回り'
description: 'M-2シングルバトルで使用率57位のドヒドイデを徹底分析。B152/D142の二重耐久とさいせいりょく（採用率97.8%）による無限受け、どくどく87.7%・じこさいせい97.4%・くろいきり58.3%の定番技、たべのこし53.0%の持ち物事情を実データと実数値計算で解説します。'
updatedDate: '2026-06-11'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-toxapex-m2.png'
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
  <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" />
  <div>
    <h2 style="margin:0 0 8px">ドヒドイデ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">57位</strong>　特性: <strong>さいせいりょく 97.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ドヒドイデは**使用率57位**を記録。特性は**さいせいりょく（採用率97.8%）**でほぼ統一されており、ひとでなし（1.9%）・じゅうなん（0.3%）は実質採用されていません。

ドヒドイデの軸は**ぼうぎょ種族値152・とくぼう種族値142**という両受けの硬さと、さいせいりょくによる「交代するたびに最大HPの1/3を回復する」性質です。じこさいせい（採用率97.4%）で居座って回復し、どくどく（87.7%）でじわじわ削り、くろいきり（58.3%）で相手の積みをリセットする——攻撃ではなく**時間と毒で相手を消耗させる**受けポケモンとして機能します。

---

## なぜドヒドイデが使われるのか

### 1. B152・D142の二重耐久で物理も特殊も受ける

ドヒドイデのぼうぎょ種族値は**152**、とくぼう種族値は**142**と、物理・特殊の両面で環境屈指の硬さを持ちます。HD振り（おだやか）でとくぼう213、HB振り（わんぱく）ならぼうぎょ224まで伸びます。HP種族値こそ50と低いものの、防御側の種族値が高いため、等倍程度の攻撃なら何発でも耐えて行動を続けられます。

### 2. さいせいりょくで交代するたびに回復する

さいせいりょく（採用率97.8%）は、**戦闘から手持ちに引っ込めるたびに最大HPの1/3を回復する**特性です。じこさいせい（採用率97.4%）による自己回復に加え、交代でも体力が戻るため、削られても引っ込めて立て直し、再度繰り出せます。これにより、後続と組んだ受け回しで体力を維持しながら何度も同じ相手を受け続けられるのが最大の採用理由です。

### 3. どくどく＋じこさいせいで「相手だけが削れる」盤面を作る

どくどく（採用率87.7%）は相手を「もうどく」状態にし、ターン経過でダメージが増えていく変化技です。ドヒドイデ自身はじこさいせいで回復し続けるため、決定打を持たない相手に対しては**こちらは減らず相手だけが毒で削れていく**一方的な消耗戦に持ち込めます。トーチカ（40.9%）を絡めれば毒のターンを稼ぎつつ、接触してきた相手にどくを入れる動きも取れます。

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
      <div style="width:31.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">63</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:76%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">152</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:26.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">53</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:71%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">142</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:17.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">35</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">495</span>
  </div>
</div>

ぼうぎょ152・とくぼう142の二重耐久が軸で、こうげき63・とくこう53の打点は低く、すばやさ35もほぼ最遅の部類です。攻撃で勝つポケモンではなく、**硬い耐久で居座り、毒と回復で相手を削り切る**のが役割です。

### 耐久実数値（HD振り・おだやか基準）

最多のHD＋bふり（採用率36.7%・H32 D32 B2）に、おだやか（D↑）を採用した場合の実数値です。性格をわんぱく・ずぶとい（B↑）に変えるHB＋d型（19.3%）の差分も併記します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">HD型（おだやか）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">HB型（わんぱく）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">157</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">157</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">174</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">224</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">213</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">164</td>
</tr>
</tbody>
</table>
</div>

HD型はとくぼう213で特殊アタッカーを受けやすく、HB型はぼうぎょ224で物理アタッカーを受けやすい配分です。HPは157とそのままなので、どちらに振るかは「物理を主に受けたいか・特殊を主に受けたいか」で決まります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
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
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

どく/みずは耐性が8タイプと非常に多く、特にかくとう・むし・フェアリーを半減できるのが受けポケモンとして優秀です。弱点はでんき・じめん・エスパーの3タイプのみですが、いずれも環境上位に使い手が多く、特にでんき（ウォッシュロトム・ブリジュラスの10まんボルト）とじめん（ガブリアスのじしん）は刺さりやすい点に注意が必要です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">分類</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じこさいせい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2を回復。居座りの核</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくどく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をもうどくにし、ターン経過でダメージ増加。主な削り手段</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くろいきり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">58.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">両者の能力ランクをリセット。積みアタッカーへの解答</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まとわりつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">51.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4〜5ターン拘束し交代を防ぐ。毒との相性が良い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トーチカ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃を防ぎ、接触技にどくを入れる。毒のターン稼ぎ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しっぺがえし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">物理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後攻だと威力2倍。低速のドヒドイデと噛み合う打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技。交代で出てくる相手をどく状態にする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ひやみず</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">特殊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致技。30%でこうげきダウン、物理受けを補助</td>
</tr>
</tbody>
</table>
</div>

じこさいせい・どくどくがほぼ確定枠で、残り2枠をくろいきり（積みリセット）・まとわりつく（拘束）・トーチカ（守り）から役割に応じて選ぶのが標準です。攻撃技はまとわりつく・しっぺがえし・ひやみずと採用率が低く、ドヒドイデが「殴って勝つ」ポケモンではないことが技構成からも読み取れます。

---

## 主要型の解説

各型は性格・EV配分（HD型 おだやか/しんちょう／HB型 わんぱく/ずぶとい）と技構成で分かれます。さいせいりょくが採用率97.8%とほぼ統一されているため、特性ではなく「物理と特殊どちらを主に受けるか」「拘束で詰ませるか積みリセットで対応するか」で型が決まります。

### 型1: 特殊受け（HD）型（最多）

**指標: HD＋bふり 36.7%／おだやか 27.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HD特殊受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さいせいりょく（97.8%）<br>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 D32 B2<br>
<strong>持ち物:</strong> たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・じこさいせい<br>
・どくどく<br>
・くろいきり / まとわりつく<br>
・トーチカ / しっぺがえし
</div>
</div>
</div>

**強み:**

とくぼう213で、特殊アタッカーの一致技を等倍なら何度でも受けながらじこさいせいで回復できます。HB型と比べてとくぼうが213対164と大きく上回るため、ウォッシュロトムの10まんボルト等のでんき特殊技を受ける際も、弱点でありながら一撃で崩れにくい配分です。サザンドラやアシレーヌの特殊技を受け出しから、どくどくを入れて受け回す動きが安定します。

**弱み:**

ぼうぎょが174とHB型（224）より低く、物理アタッカーのじめん・かくとう以外の等倍物理技でも削りが入りやすくなります。物理高火力が主体の相手にはHB型に役割を譲る必要があります。

---

### 型2: 物理受け（HB）型

**指標: HB＋dふり 19.3%／わんぱく 14.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0748-00.webp" alt="ドヒドイデ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HB物理受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さいせいりょく（97.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32 B32 D2<br>
<strong>持ち物:</strong> たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・じこさいせい<br>
・どくどく<br>
・くろいきり / まとわりつく<br>
・ひやみず / トーチカ
</div>
</div>
</div>

**強み:**

ぼうぎょ224で、HD型（174）より物理を大きく受けやすくなります。マスカーニャのトリックフラワー・はたきおとす等の物理打点を等倍で受け止め、ひやみず（30%こうげきダウン）を絡めれば物理アタッカーの火力をさらに削れます。物理主体の相手に対する受け出し性能はHD型より明確に上です。

**弱み:**

とくぼうが164とHD型（213）より低く、特殊アタッカーへの受け出しが甘くなります。でんき・エスパーの特殊弱点技はもちろん、等倍の特殊技でもHD型より削られるため、特殊軸の相手には後続に受けを譲る必要があります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ドヒドイデと相性がはっきり出るポケモンを有利・不利の両面から挙げます。B152/D142の二重耐久とさいせいりょくで多くの中火力アタッカーを受けられる一方、弱点のでんき・じめん・エスパーを高火力で突かれる相手、そして毒が効かないどく・はがねタイプには受けが機能しない点に注意してください。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/あくの一致技はどちらもどく/みずに等倍以下。トリックフラワー（92.9%）も大した痛手にならず、HB型なら受けてどくどくで削れる。トリプルアクセル（こおり・72.2%）はみずで半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー・97.0%）はどくで半減、うたかたのアリア（みず・79.2%）も半減。HD型なら等倍以上の打点がなく、どくどくで削り切れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2弱点。HB型でも高乱数〜確定圏で、受け出しが効かない。スケイルショット・げきりんは等倍だがじしんがほぼ確実に飛んでくる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・56.8%）が×2弱点。HD型でも継続的に削られ、おにび（80.6%）でこちらの打点も奪われる。どくどくは通るが、ハイドロポンプ（98.5%）は半減で受けても削り合いで押し負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・66.9%）が×2弱点。はがねタイプでどくどくが入らず、こちらの削り手段が消える。りゅうせいぐんは等倍で通る（ラスターカノンは半減）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく/ゴーストでどくどくは無効（どくタイプには毒が入らない）。主力のヘドロウェーブ（どく・81.7%）はどく/みずに×0.5で受かり、シャドーボール（ゴースト・71.1%）は等倍だがHD型なら耐えるが、こちらも有効打がなく決め手を欠く膠着になる</td>
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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）が×2弱点で受け出しが効かず、つるぎのまい（19.6%）で積まれると一撃圏に入る</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめんを無効化するひこう（アーマーガア）や半減するくさ枠に受けを任せる。積まれたらくろいきりで能力ランクをリセットしてから引く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねでどくどくが無効化され、削り手段が消える。10まんボルト（66.9%）が×2弱点で押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね弱点を突くじめん・かくとう枠（ガブリアスのじしん等）を合わせる。ドヒドイデ単体での受けは諦める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）が×2弱点。おにび（80.6%）でしっぺがえし等の打点を奪われ、どくどくは通るがハイドロポンプ等の削り合いで先に押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんきを無効化するじめん枠（ガブリアス）に引いてボルトチェンジごと透かす。じめん技で上から落とす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうでどくどくが無効。ちょうはつ（採用があれば）でこちらの変化技を封じられると詰む</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・ほのおの特殊枠（ウォッシュロトム等）を合わせてはがね弱点を突く。ドヒドイデでは突破できないため受け合いに付き合わない</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「ドヒドイデの弱点（でんき・じめん）を高火力で突く相手」と「どく・はがねで毒が無効化され削り手段を失う相手」に大別されます。前者はタイプ補完で受けを肩代わりし、後者は別の打点で突破する後続が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0354-00.webp" alt="ジュペッタ">
    <div class="name">ジュペッタ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ゴーストでかくとう・ノーマルを透かし、受け回しの軸を組む</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0478-00.webp" alt="ユキメノコ">
    <div class="name">ユキメノコ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">こおり/ゴーストでドラゴン・じめんに打点。ドヒドイデの苦手なじめん勢を削る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき無効のじめん枠。苦手なウォッシュロトム・ブリジュラスに上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん無効のはがね/ひこう枠。苦手なガブリアスのじしんを透かして受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速のあく/くさで、受け回しに足りない速攻と崩しを補う</div>
  </div>
</div>

**パーティ構成の基本方針:**

ドヒドイデは自力で相手を倒す力が弱く、毒と回復で時間をかけて崩す受けポケモンです。残り5体で以下の役割を補います。

1. **じめん対策**: じめんを無効化するひこう（アーマーガア）でガブリアスのじしんを受ける枠
2. **でんき対策**: でんきを無効化するじめん（ガブリアス）でウォッシュロトム・ブリジュラスの10まんボルトを透かす枠
3. **はがね崩し**: どくが効かないはがねを突くじめん・かくとう・ほのお枠
4. **決定力の補完**: 受けで作った毒ダメージの蓄積を、高速アタッカー（マスカーニャ）の一撃で詰める枠

---

## データ分析①：技採用率に見る「殴らない」設計

ドヒドイデの技採用率は、攻撃技より**変化技に大きく偏っている**点に特徴があります。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| じこさいせい | 変化 | 97.4% | 自己回復 |
| どくどく | 変化 | 87.7% | 削り（もうどく） |
| くろいきり | 変化 | 58.3% | 積みリセット |
| まとわりつく | 特殊 | 51.5% | 拘束 |
| トーチカ | 変化 | 40.9% | 守り・毒入れ |
| しっぺがえし | 物理 | 18.8% | 攻撃打点 |

上位5技のうち4技が変化技で、唯一の攻撃打点である**しっぺがえしは18.8%**にとどまります。最多のまとわりつく（51.5%）も威力20の拘束技で、ダメージより「相手を交代させず毒のターンを稼ぐ」ことが目的です。

この採用傾向は、ドヒドイデが「攻撃で勝つ」のではなく「**回復で減らず、毒で相手だけを削る**」消耗戦専用のポケモンであることを示します。じこさいせいで体力を維持し、くろいきりで相手の積みを無効化し、まとわりつくで交代を封じてどくどくを通す——攻撃ランキングではなく、相手を「動けなくして毒で溶かす」変化技の組み合わせが、この型の本質です。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>HD 36.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D213で特殊技を受ける。アシレーヌ等に安定</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B174で物理高火力に削られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HB物理受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HB 19.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B224で物理技を受ける。マスカーニャ等に安定</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D164で特殊高火力に削られやすい</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ドヒドイデはB152/D142の二重耐久とさいせいりょく（97.8%）を軸に、じこさいせいで回復しながらどくどくで相手を削り、くろいきりで積みをリセットする受けポケモンです。攻撃技はほぼ採用されず、「減らずに相手だけを溶かす」消耗戦が役割です。

性格・EVはHD型（おだやか・D213）とHB型（わんぱく・B224）に分かれ、特殊と物理どちらを主に受けるかで選びます。一方、弱点のでんき・じめんを高火力で突くガブリアス・ウォッシュロトム・ブリジュラス、毒が無効化されるはがね（ブリジュラス・アーマーガア）には受けが機能しないため、タイプ補完と別の打点を持つ後続が構築の前提になります。

---

## 関連記事

- [じしんで弱点を突く天敵 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [フェアリー技を半減で受けられる アシレーヌのM-2考察](/blog/primarina-analysis-m2/)
- [くさ受けに刺さる高速アタッカー リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
