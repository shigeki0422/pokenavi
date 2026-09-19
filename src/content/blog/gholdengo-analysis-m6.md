---
title: '【ポケモンチャンピオンズ】サーフゴー 考察 M-6 シーズン 使用率9位の解説'
description: 'M-6シーズン使用率9位のサーフゴーを考察。はがね/ゴーストの複合タイプとシャドーボール・ゴールドラッシュ・わるだくみを軸にした積みアタッカー運用を、確定数データとタイプ相性の検算で解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-gholdengo-m6.png'
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
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" />
  <div>
    <h2 style="margin:0 0 8px">サーフゴー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>　特性: <strong>おうごんのからだ 100%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも同日のスナップショットを使用しています。

M-6シーズンのサーフゴーは使用率9位。はがね/ゴーストの複合タイプに、シャドーボール・ゴールドラッシュ・わるだくみ・じこさいせいを主軸とする積みアタッカー運用が主流です。C133の高い特殊火力とD91の特殊耐久を土台に、わるだくみで一段階火力を底上げしてから押し切る立ち回りが基本になります。

---

## サーフゴーの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:89%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">133</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:61%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">91</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">84</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">550</span>
  </div>
</div>

C133の特殊火力を中心に、B95・D91は弱点を突かれない攻撃なら一撃は耐える水準で、押し引きの両方に対応できるステータス配分です。S84は環境上位の多くより遅く、先手を確実に取れる数値ではありません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はじめん・ゴースト・ほのお・あくの4タイプ（いずれも×2）で、×4の弱点はありません。ノーマル・かくとう・どくを無効化し、むしを4分の1で受けられるなど、耐性面の広さが持ち味です。一方でじめん技は環境上位に広く採用されているため、選出段階でのケアが必要です。

### 特性

<strong>おうごんのからだ（100.0%）</strong>が唯一の特性で、相手からの変化技を無効化します。相手の積み技・能力低下技・状態異常技を一方的に無視できるため、後述のわるだくみを安全に通しやすい下地になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト一致のメインウェポン。20%で相手の特防を1段階下げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゴールドラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">94.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致の最大火力技。使用後に自分の特攻が2段階下がる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">83.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の特攻を2段階上昇。おうごんのからだで安全に積みやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じこさいせい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">70.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の最大HPの1/2を回復。積みながら長く場に残るための技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこう複合への追加打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手と自分の持ち物を交換。こだわりスカーフ型で耐久型を機能不全にする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/4を消費してみがわりを設置。状態異常・削り技を透かす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・はがね複合等への追加打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン・かくとう複合等への追加打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：積みアタッカー型（わるだくみ・じこさいせい）

**代表的な性格: ひかえめ（全体の性格採用率62.6%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">積みアタッカー型（わるだくみ・じこさいせい）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> おうごんのからだ（100.0%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H1-B1-C32-S32<br>
<strong>持ち物:</strong> ふうせん（50.0%）
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ゴールドラッシュ<br>
・わるだくみ<br>
・じこさいせい
</div>
</div>
</div>

シャドーボール（ゴースト・威力80）とゴールドラッシュ（はがね・威力120、使用後に自分の特攻が2段階下がる）の2タイプ打点に、わるだくみ（特攻2段階上昇）で火力を底上げする構成です。ふうせん（採用率50.0%）は攻撃技を受けるまでじめん技を無効化できる持ち物で、弱点4タイプのうちじめんへの保険になります。

**強み:**

ひかえめ・EV H1-B1-C32-S32のC実数値は**203**（HP163・S136）。わるだくみを1回積めばC406相当まで伸び、ゴールドラッシュで自分の特攻を2段階下げてもわるだくみ前の水準まで戻る計算になるため、積んだ後は継続して高火力を維持できます。

**弱み:**

こだわりスカーフによるS上昇がないため、後述のとおりS84はメガ進化を含む環境上位の多くより遅く、積む前に上から攻撃を受ける展開に弱い点は変わりません。

---

### 型2：こだわりスカーフ型

**代表的な性格: おくびょう（全体の性格採用率13.5%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> おうごんのからだ（100.0%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ（13.4%）
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ゴールドラッシュ<br>
・10まんボルト<br>
・トリック
</div>
</div>
</div>

わるだくみ・じこさいせいを積む余裕を捨て、こだわりスカーフで素早さを底上げしてから確定技で押し切る構成です。10まんボルトはみず・ひこう複合への追加打点として採用され、トリックはこだわりスカーフを機能させたくない耐久型に押し付ける択になります。

**強み:**

おくびょう・EV H2-C32-S32・こだわりスカーフ込みのS実数値は**223**（型1のS136より+87）。型1では上から動けない相手にも先手を取れる範囲が広がります。

**弱み:**

技を1つに固定されるため、シャドーボール・ゴールドラッシュ・10まんボルトを相手のタイプに応じて選び直す柔軟性がありません。またわるだくみを積まないため、C実数値は185（型1の積み後C406相当より大幅に低い）にとどまり、長期戦での火力は型1に劣ります。

---

## データ分析：カバレッジ計算（使用率TOP10へのタイプ相性）

M-6使用率TOP10（サーフゴー自身を除く9体）に対し、主力技3種のタイプ相性を検算しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手（使用率順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュ（はがね）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき）</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアス（1位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#f1f5f9;color:#64748b;font-weight:bold">無効※</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ボーマンダ（2位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アシレーヌ（3位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">グソクムシャ（4位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍※</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">カバルドン（5位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#f1f5f9;color:#64748b;font-weight:bold">無効</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ルカリオ（6位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（7位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">セグレイブ（8位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ギルガルド（10位）</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#dcfce7;color:#16a34a;font-weight:bold">×2</td><td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2;color:#dc2626">半減</td><td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td></tr>
</tbody>
</table>
</div>

採用率99.9%のシャドーボールはTOP10のうち9体全てに等倍以上（半減される相手が0体）で、外れのない選択です。使用率10位のギルガルド（はがね/ゴースト）は同複合ながら、サーフゴー自身のシャドーボールはゴースト一致でギルガルドに×2で通ります（後述の苦手表参照）。一方、採用率94.3%と一致技の中で最大威力を持つゴールドラッシュは、グソクムシャ・ルカリオ・ブリジュラス・ギルガルドの4体に半減されます。20.0%と少数派の10まんボルトは、アシレーヌに×2で刺さる一方、ガブリアス・カバルドンには無効となる両極端な打点で、汎用性ではシャドーボールに劣ります。

※グソクムシャは採用率98.9%のグソクムシャナイトを考慮するとメガ形態（むし/はがね）が実態で、10まんボルトは等倍止まりです（メガ前提のためカバレッジ表もむし/はがねで計算）。ガブリアスも採用率35.0%のガブリアスナイトZを考慮するとメガ形態（ドラゴン単+ふゆう）では10まんボルトが半減になります（無効はメガ以外の型のみ）。

---

## 苦手なポケモン

使用率TOP35を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュ（採用率94.3%）は確定2発ですが後手に回り、メガボーマンダの主力すてみタックル（採用率73.4%）の確定2発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはサーフゴーが上ですが、シャドーボールが確定3発なのに対しふいうち（49.3%）は確定2発のため、先に落とされます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定2発ですが、ギルガルドの主力ポルターガイスト（採用率54.0%）は確定1発。先に行動しても一撃で沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定2発ですが、素早さはミミッキュが上のため、主力シャドークロー（採用率59.2%）の確定2発に先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュは確定1発ですが、素早さはマスカーニャが上のため、主力はたきおとす（採用率59.0%）で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定2発ですが、素早さはイダイトウが上のため、主力ウェーブタックル（採用率96.5%）の確定2発に先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定2発ですが、メガリザードンXの主力フレアドライブ（採用率36.5%、ほのお×2弱点）は確定1発。先に一撃で沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">非一致の10まんボルト（採用率20.0%）でも確定2発止まり。メガリザードンYの主力かえんほうしゃ（採用率42.9%、ほのお×2弱点）の確定1発に先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定2発ですが、エースバーンの主力かえんボール（採用率98.7%、ほのお×2弱点）は確定1発で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってシャドーボールを当てても確定3発。ウルガモスの主力ほのおのまい（採用率70.6%、ほのお×2弱点）は確定2発のため、2発目で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュは確定2発ですが、素早さはオオニューラが上のため、主力じごくづき（採用率59.9%、あく×2弱点）の確定2発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールは確定3発ですが、素早さはカイリューが上のため、主力かえんほうしゃ（採用率66.8%、ほのお×2弱点）の確定2発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュは確定2発ですが、素早さはサザンドラが上のため、主力あくのはどう（採用率98.3%、あく×2弱点）の確定2発に先に押し切られます</td>
</tr>
</tbody>
</table>
</div>

苦手表はほのお・あく複合または高速アタッカーに偏っており、サーフゴーの弱点であるほのお・あく・じめん・ゴーストを一致技として持つ相手に、素早さで上から動かれる展開が主な負けパターンです。

---

## 得意なポケモン

使用率TOP35を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボールとブリジュラスの3番手技10まんボルト（採用率63.1%、上位はラスターカノン75.1%・りゅうせいぐん65.3%）は共に確定4発ですが、代表的な型の組み合わせでは先に行動でき押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率20.0%、でんき×2弱点）で確定2発。アーマーガアの主力ブレイブバード（採用率37.6%）は倒しきれない水準にとどまり、先に押し切れます（はねやすめ〈採用率99.1%〉で粘られても、ブレイブバード単体では決定打にならないため結果は変わりません）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（採用率20.0%、でんき×4弱点）で確定1発。ギャラドスの8番手技やけっぱち（採用率28.9%）はもちろん、上位技パワーウィップ（67.3%）・たきのぼり（63.1%）・じしん（53.4%、はがね複合に有効）でも確定2発止まりで、素早さで上回るサーフゴーが先に沈めます（ギャラドスナイト採用率24.1%のメガギャラドスはみず/あくで、でんき技の弱点は×4から×2に下がる点に注意）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴールドラッシュ（採用率94.3%、はがね×4弱点）で確定1発。アローラキュウコンの主力ふぶき（採用率69.1%）は確定5発と決め手を欠くため、素早さで劣ってもゴールドラッシュ1発で沈められ、一方的に処理できます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト×2弱点）とラウドボーンの主力フレアソング（採用率99.4%）は共に確定2発ですが、素早さはサーフゴーが上のため先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

なお、アーマーガア・ギャラドスの2体は採用率20.0%の10まんボルトの命中が前提の結論です。ゴールドラッシュ・シャドーボールなど型を問わず持つ技だけでは、この2体に対して同じ結論にはなりません。

得意表は、サーフゴーが等倍以上を取れるうえに素早さでも上回れる相手、またはサーフゴー自身が耐性を持つタイプの一致技しか持たない相手に偏っています。逆に上記の苦手表と合わせると、S84という素早さそのものは環境上位の一部にしか優位を取れない水準であることが分かります。

---

## 同居率上位の分析

M-6でサーフゴーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ボーマンダ**（1位）はドラゴン/ひこうで、じめん技を無効化できます。サーフゴーの弱点のひとつであるじめん技を持つ相手には、ボーマンダに受け出すことでケアできます。逆にボーマンダの弱点であるこおり（×4）・フェアリー（×2）はサーフゴーが半減で受けられるため、双方が相手の弱点タイプに受け出し先を用意できる組み合わせです。

**カバルドン**（2位）はステルスロック（採用率92.7%）・あくび（採用率96.5%）を高採用しており、設置技と交代誘導で相手を崩してから、サーフゴーがわるだくみを通しやすい状況を作る役割分担があります。

**アシレーヌ**（3位）はみず/フェアリーで、サーフゴーの弱点であるほのお技を半減で受けられます。逆にアシレーヌの弱点であるどく技はサーフゴーが無効化できるため、双方が相手の弱点タイプに受け出し先を用意できる組み合わせです。

**ガブリアス**（4位）は弱点のこおり（×4）・ドラゴン（×2）・フェアリー（×2）をいずれもサーフゴーが半減で受けられます。ガブリアス側からサーフゴーの弱点を直接カバーする関係にはありませんが、ガブリアスを狙ったこおり・ドラゴン・フェアリー技への受け出し役としてサーフゴーが機能します。

---

## まとめ

M-6のサーフゴーは使用率9位。はがね/ゴーストの複合タイプでノーマル・かくとう・どくを無効化しつつ、C133の高い特殊火力をシャドーボール・ゴールドラッシュ・わるだくみで発揮する積みアタッカーが主流です。

- **タイプ相性**: 弱点はじめん・ゴースト・ほのお・あくの4タイプ（×4弱点なし）。耐性は8タイプに及び、むしを4分の1で受けられます
- **技構成**: シャドーボール（99.9%）はTOP10使用率相手に半減される例がなく、ゴールドラッシュ（94.3%、使用後に自分の特攻が2段階下がる）と合わせて2タイプ打点を確保しています
- **弱点への対策**: 使用率上位パートナー（ボーマンダ・アシレーヌ・ガブリアス）がサーフゴーの弱点タイプの一部を受け止める組み合わせで選出されています

S84はメガ進化を含む環境上位の多くより遅く、苦手表に挙げた相手には上から攻撃されて崩されるため、積む前のタイミングと選出段階でのケアが引き続き求められます。

---
