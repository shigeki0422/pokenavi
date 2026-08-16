---
title: '【ポケモンチャンピオンズ】ライチュウ 考察 M-5 シーズン メガライチュウYのノーガード運用'
description: 'M-5シーズン使用率18位のライチュウを考察。ライチュウナイトY採用率97.2%、特性ノーガードでのでんじほう・きあいだま完全命中を軸にしたC212の実数値と、まれなメガライチュウX、苦手・有利なポケモン、同居率上位のパートナーをデータで解説します。'
pubDate: '2026-08-16'
updatedDate: '2026-08-16'
heroImage: '../../assets/hero-raichu-m5.png'
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
  <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" />
  <div>
    <h2 style="margin:0 0 8px">ライチュウ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">18位</strong>　持ち物: <strong>ライチュウナイトY 97.2%</strong>
    </div>
  </div>
</div>

M-5シーズン、ライチュウは使用率18位につけています。ライチュウには2種類のメガストーンが存在し、ライチュウナイトYが採用率97.2%とほぼ独占状態です。メガ進化後の特性は**ノーガード**（お互いの技の命中率が100%になる）に変わり、命中70%のきあいだま（採用率97.1%）を確実に当てられる点が最大の特徴です。もう一方の主力技であるでんじほう（命中50%、採用率97.5%）もノーガードで必中となり、でんじほう・きあいだまの両立で広い打点範囲を持つ特殊アタッカーとして運用されます。

---

## 基本スペック

### 種族値（メガライチュウY後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:80%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">160</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong>130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">585</span>
  </div>
</div>

メガ進化前はC90・S110（合計485）ですが、メガライチュウYでC160・S130まで伸び、種族値合計は585に達します。B55・D80は非メガ・メガ後ともに薄く、H60と合わせて耐久面はかなり低いため、一撃で仕留めるプレイングが前提です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

でんき単タイプのためじめん×2のみと弱点は1タイプに絞られますが、無効化する手段（ふゆう等）を持たないため直撃を受けます。ひこう・はがね・でんきの3タイプを半減できます。詳細な相手対策は後述の「苦手なポケモン」を参照してください。

### 特性

メガ進化前の特性は**ひらいしん（88.9%）**が中心で、でんきタイプの技を自分に引き寄せて無効化し特攻を1段階上げます。メガ進化すると特性は**ノーガード**に変わり、お互いの技の命中率が100%になります。きあいだま（命中70%、採用率97.1%）が必ず当たるようになる一方、相手の低命中技も必中になる諸刃の特性です。もう一方のメガストーンであるライチュウナイトX（1.5%）は特性が**エレキメイカー**（登場時5ターンの間エレキフィールドを展開）に変わり、A135の物理アタッカー型になりますが、環境での採用はごく少数です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>でんじほう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致最大威力技。相手をまひ状態にする。ほぼ確定枠</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">通常命中70%だがノーガードで確実に命中。ドドゲザン等のあく複合への高打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くさむすび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20〜120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">70.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン等の重量級じめんタイプへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">低耐久を補い、相手の状態異常・変化技を透かす</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボルトチェンジ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代できる。じめん対策枠への対面操作</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:26px;height:26px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の特攻を2段階アップ。積み後は確定数を大きく縮める</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

### 型① メガライチュウY 最速アタッカー型

**性格採用率: おくびょう 73.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガライチュウY 最速アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ひらいしん（88.9%、メガ後はノーガード）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（57.7%）<br>
<strong>持ち物:</strong> ライチュウナイトY（97.2%）
</div>
<div>
<strong>技構成:</strong><br>
・でんじほう<br>
・きあいだま<br>
・くさむすび<br>
・みがわり or ボルトチェンジ
</div>
</div>
</div>

メガ進化後にC212・S200（おくびょう時）を得る、環境で最も採用されている型です。でんじほう・きあいだま・くさむすびの3タイプで、じめんタイプを含めほぼ全ての相手に等倍以上を取れます。

**強み:**

S200は環境上位の非スカーフ勢の大半を上から攻撃できる水準で、耐久寄り型のS155と比べても先制を取れる場面が広がります。C212でメガ後の火力を最大化できる点も、みがわりや積み技を採用する耐久寄り型との明確な違いです。

**弱み:**

耐久にほぼEVを割かないため、耐久寄り型（H165・B106）と比べると一発の被弾が致命傷になりやすく、後述する上位ポケモンのじめん一致技をほぼ確実に受けてしまいます。

---

### 型② メガライチュウY 耐久寄り型

**EV採用率: H30-B31-S5 2.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガライチュウY 耐久寄り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ひらいしん（88.9%、メガ後はノーガード）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H30-B31-S5（2.5%）<br>
<strong>持ち物:</strong> ライチュウナイトY（97.2%）
</div>
<div>
<strong>技構成:</strong><br>
・でんじほう<br>
・きあいだま<br>
・みがわり<br>
・わるだくみ
</div>
</div>
</div>

素早さを最小限に抑え、H・Bに配分してH実数値165・B実数値106まで確保する型です。C実数値198と最速型のC212に対しては劣りますが、みがわりを安定して出せる耐久を確保しています。

**強み:**

H165・B106の耐久を活かし、じめん技を持たない物理アタッカーの技であればみがわりを安定して立てられ、わるだくみで積む隙を作りやすい型です。ただしガブリアス・カバルドン等のじめん一致技を持つ相手にはみがわりごと崩されるため、通用する相手は限られます。

**弱み:**

S実数値155は環境上位のほぼ全てに後手を取る低速で、最速型のS200と比べると先制で仕留める運用はできません。積む前提のため、後述する上位ポケモンのじめん一致技を透かせないと機能しません。

---

## データ分析：97.2%対1.5%、2つのメガストーンの分岐点

ライチュウはメガストーンを2種類（ライチュウナイトX・Y）持ちますが、採用実態は大きく偏っています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガストーン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">主なステータス</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><strong>ライチュウナイトY</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">97.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ノーガード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C160・S130（特殊）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ライチュウナイトX</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エレキメイカー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A135・S110（物理）</td>
</tr>
</tbody>
</table>
</div>

メガライチュウXはA135の物理アタッカーで、エレキメイカーによる5ターンのエレキフィールド展開という独自の付加価値を持ちますが、採用率は1.5%にとどまります。ライチュウの主力技であるでんじほう・きあいだまはいずれも特殊技であるため、C160・ノーガードを得られるYの方が既存の技構成をそのまま活かせる点が、97.2%という圧倒的な採用率の差につながっています。Xを選ぶ場合は物理技（かみなりパンチ等）への技構成の組み替えが前提になりますが、そうした型は環境データ上ほぼ存在しません。

---

## 苦手なポケモン

唯一の弱点であるじめん×2を突く相手を、M-5使用率上位から公平に抽出しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.5%）がじめん×2。いじっぱりA200なら220〜260%で確定一発です</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.5%）がじめん×2でほぼ確定枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メタグロス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（39.6%）がじめん×2。約4割の個体が該当する条件付きの脅威です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（68.9%）がじめん×2</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0003-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フシギバナ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（88.6%）がじめん×2でほぼ確定枠</td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fef3cd;border:1px solid #f59e0b;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>⚠️ じめん一致技はほぼ全てが確定圏</strong><br>
  弱点がじめん1タイプに絞られる一方、環境上位の多くがじしん・だいちのちからを高採用率で持ちます。H60・B55の耐久ではほぼ確実に一撃圏に入るため、後出しは避け、対面から先に打点を通す立ち回りが基本です。
</div>

---

## 有利なポケモン

でんき・かくとう・くさの技が刺さり弱点じめんも突かれない相手に加え、初手対面ならS200で先手を取れるギャラドスを挙げます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリーにでんじほうが×2。主力のムーンフォース・うたかたのアリア・アクアジェットはこちらの唯一の弱点じめんを突きません</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンにきあいだまが×2。主力のラスターカノン・りゅうせいぐん・10まんボルトはこちらの弱点を突きません</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう/はがねにでんじほうが×2。C212でんじほうは最多EV型に確定一発です。じめん技採用率0%でS実数値87（わんぱくH32-B32-D2）なので、S200のメガライチュウYが先手で押し切れます</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Y型（57.9%）のほのお/ひこうにでんじほうが×2で、弱点じめんも突かれません。X型（41.1%）はほのお/ドラゴンで半減となり、有利はY型限定です</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">イダイトウ(オス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ゴーストにでんじほうが×2で、じめん技非採用のため弱点も突かれません。スカーフ型（32.6%、S214）には先手を取られます</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0503-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ダイケンキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず単タイプにでんじほうが×2。じめん技非採用で弱点も突かれません</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガギャラドス（みず/あく、採用率77.8%）にでんじほうが×2で確定一発です。じしん（76.8%）で弱点は突かれますが、S146の相手にS200が先手を取れます。りゅうのまい（82.3%）で積まれると逆転されるため後出しは不可です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位のパートナー

M-5でライチュウと同じパーティに入る頻度が高いポケモン（同居率1〜5位）を紹介します。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
  </div>
</div>

このうち**アーマーガア**（ひこう/はがね）はじめん技を無効化でき、ライチュウが後出しできないガブリアス・カバルドンのじしんを受け持てる役割分担が成立しています。**ミミッキュ**はばけのかわで一撃を軽減しつつ後続に繋ぐ役割を果たせます。ガブリアス・アシレーヌ・マスカーニャは同居率上位ですが、じめん耐性という観点での明確な噛み合いはなく、単純に採用率が高い組み合わせとして同居しています。

---

## まとめ

M-5のライチュウは使用率18位で、ライチュウナイトYが採用率97.2%とほぼ独占する特殊アタッカーが基本コンセプトです。メガ進化後は特性がノーガードに変わり、命中70%のきあいだま（97.1%）を確実に当てながらでんじほう（97.5%）と合わせて広い技範囲を持ちます。

- **2種のメガストーンのうちYが97.2%を占め、Xはわずか1.5%**：既存の特殊技構成をそのまま活かせるYの方が合理的で、Xを選ぶ物理型はデータ上ほぼ存在しません
- **型は最速アタッカー型（S200）と耐久寄り型（S155・H165・B106、みがわり運用）に分かれる**：C実数値198〜212の範囲で、素早さか耐久かの配分が主な違いです
- **弱点はじめん1タイプのみだが、環境上位の多くが高採用率のじめん一致技を持ち、H60・B55の低耐久でほぼ確実に一撃圏**：ガブリアスのじしんは220〜260%に達します
- **アシレーヌ・アーマーガア・ブリジュラス・イダイトウ(オス)・ダイケンキには一致技が刺さり、弱点も突かれない**ため対面から打点を通せます。イダイトウ(オス)のスカーフ型（32.6%）には先手を取られます。リザードンはメガY限定で有利が成立し、メガX（41.1%）には半減されます
- **ギャラドスはじしん（76.8%）で弱点を突かれますが、初手対面ではS200が先手を取り確定一発**が通ります。りゅうのまい（82.3%）で積まれると逆転されるため後出しでは通用しません
- アーマーガアは同居率4位のパートナーとして、じめん技を無効化しガブリアス・カバルドンのじしんを受け持てる役割分担が成立しています

ノーガードによる完全命中の高火力と引き換えに耐久は薄いため、じめん技を無効化できるパートナーと組み合わせて運用するアタッカーです。

---

*関連記事：[サザンドラ考察 M-5](/blog/hydreigon-analysis-m5/)*
