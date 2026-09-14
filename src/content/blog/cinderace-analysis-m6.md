---
title: '【ポケモンチャンピオンズ】エースバーン 考察 M-6 シーズン リベロと3型分散の解説'
description: 'M-6シーズン使用率19位のエースバーンを考察。ほのお単タイプとリベロの仕組み、かえんボール98.7%を軸にした技構成、こだわりスカーフ/きあいのタスキ/いのちのたまで割れる3つの型別の得意/苦手をデータで解説します。'
pubDate: '2026-09-14'
updatedDate: '2026-09-14'
heroImage: '../../assets/hero-cinderace-m6.png'
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
  <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" />
  <div>
    <h2 style="margin:0 0 8px">エースバーン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">19位</strong>　特性: <strong>リベロ 98.6%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・技/性格/持ち物などの採用率データは2026-09-10時点のものです。

M-6シーズンのエースバーンは使用率19位。ほのお単タイプにS種族値119の高速アタッカーで、特性リベロにより場に出て最初に繰り出す技のタイプに変化します。かえんボール98.7%・とびひざげり89.0%を中心とした技構成はほぼ固定されている一方、持ち物はこだわりスカーフ・きあいのタスキ・いのちのたまの3つに分散しており、この分散の実態は後述のデータ分析で詳しく扱います。

---

## エースバーンの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">116</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:79%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">119</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

A116・S119が突出し、B75・D75は平均的、C65は低めです。物理アタッカー専用の配分で、素早さは環境上位の多くに先手を取れる水準です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はみず・じめん・いわの3タイプ（いずれも×2）。無効タイプは持たず、B75・D75の耐久ラインも高くないため、この3タイプの一致技を受けると大きく削られます。使用率5位のカバルドンはじしん（じめん・採用率99.3%）を高採用しており、後述の苦手表のとおり打点勝負で先に落とされます。

### 特性

**リベロ（採用率98.6%）**がほぼ固定で採用されています。今の自分のタイプと異なるタイプの技を使うと、そのタイプに変化して一致補正を得る特性です（登場するたび1回だけ）。エースバーンは元々ほのお単タイプなので、ほのお技（かえんボール等）を使っている間はタイプが変わらずリベロも発動しません。ダストシュート（どく）のようにほのお以外の技を初めて使ったタイミングでどくタイプに変化し、以降は交代するまで固定されます。もう一方の**もうか**（採用率1.4%）はHPが1/3以下でほのお技の威力が1.5倍になる特性ですが、採用率は少数にとどまります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお一致のメインウェポン。10%で相手をやけどにする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とびひざげり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">89.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高火力のかくとう技。外れるか失敗すると自分の最大HPの1/2のダメージを受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ダストシュート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー等への打点。30%で相手をどくにする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に手持ちと交代し、後続へ対面を引き継ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>48.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手が攻撃技を選んでいる時のみ成功する先制技で、自分より速い相手への保険</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー/こおり/いわに抜群のはがね技。20%で相手をひるませる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>コートチェンジ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分側の場の状態（設置技等）を相手側と入れ替える。少数派の選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクロバット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物を持たない場合に威力2倍になるひこう技。少数派の選択</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：こだわりスカーフ型（速攻アタッカー）

**性格採用率: いじっぱり 51.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型（速攻アタッカー）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> リベロ（98.6%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ（33.0%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんボール<br>
・とびひざげり<br>
・ダストシュート<br>
・とんぼがえり
</div>
</div>
</div>

こだわりスカーフでS実数値をさらに引き上げ、初手からかえんボール・とびひざげり・ダストシュートの3タイプ打点を高速で押し付ける型です。技を固定される代償として、後述の型2・型3より広い範囲の相手に上から攻撃できます。

**強み:**

S実数値は**256**（S実数値171にこだわりスカーフの1.5倍補正）で、型3のS実数値171・型2のS実数値188を大きく上回ります。先制技に頼らず上から攻撃できる相手の範囲が広がる点が型2・型3にない強みです。

**弱み:**

技を1つに固定されるため、相手が交代してきた際に対応技を変更できません。無効タイプの相手や後述の苦手なポケモンに対して受け直しがきかない点も型2・型3に劣ります。

---

### 型2：きあいのタスキ型（耐久）

**性格採用率: ようき 46.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型（耐久）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> リベロ（98.6%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ（31.2%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんボール<br>
・とびひざげり<br>
・ダストシュート<br>
・ふいうち
</div>
</div>
</div>

きあいのタスキで満タンからの一撃を1発は耐えつつ、技構成の1つにふいうち（優先度+1）を持つことで、相手が攻撃技を選んでいれば1回は先制で返せるようにした型です。とんぼがえりの代わりにふいうちを採用している点が型1・型3との違いです。

**強み:**

きあいのタスキにより最大HPからの一撃を必ず1耐えできるため、型3のように初手で上から縛られて落とされる展開を防げます。耐えた後、相手が攻撃技を選んでいればふいうちで優先的に追撃でき、後述の苦手表にあるボーマンダ・カバルドンのような1発で落とされる相手にも1回に限り打点を返せます。

**弱み:**

S実数値は**188**で型1のS256には及ばず、こだわりスカーフ持ちの相手に上から動かれる場面が型1より多くなります。またきあいのタスキは低火力の技や設置ダメージで先に削られていると発動せず、1試合に1回しか機能しません。

---

### 型3：いのちのたま型（最大打点）

**性格採用率: いじっぱり 51.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたま型（最大打点）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> リベロ（98.6%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> いのちのたま（24.4%）
</div>
<div>
<strong>技構成:</strong><br>
・かえんボール<br>
・とびひざげり<br>
・ダストシュート<br>
・とんぼがえり
</div>
</div>
</div>

いのちのたまで全ての技の威力を底上げし、無補正のS171でも押し切れる確定数の高さを重視した型です。技を選び直せる点は型1と共通しつつ、こだわりスカーフのS補正がない代わりに毎ターン打点が高いまま維持できます。

**強み:**

こだわりスカーフのように技を固定されないため、相手に応じてかえんボール・とびひざげり・ダストシュートを選び直せます。同じ技構成の型1（こだわりスカーフ）と比べ、技固定のリスクなく高い威力を出せる点が型3固有の利点です。

**弱み:**

S実数値は**171**で型1のS256・型2のS188より低く、こだわりスカーフ持ちの相手はもちろん、無補正で並ぶ相手にも先手を取られやすくなります。毎ターン最大HPの1/10を消費するため、削り合いが長引く展開では体力面で型1・型2より不利になります。

---

## データ分析：持ち物3分割の実態

※型ごとの説明では便宜上「型1〜3」と分けましたが、実際の採用データでは持ち物が明確な多数派を持たず、こだわりスカーフ33.0%・きあいのタスキ31.2%・いのちのたま24.4%の3つの選択肢に分散しています。技構成が固定されているのに持ち物だけが3分割される背景には、リベロの仕組みが関係しています。初手の技でタイプが決まりその後固定されるため、後続の相手を選ぶよりも「初撃をどう通すか」（速さで上から叩くか、耐えて返すか、威力を底上げするか）の一点で運用が分かれ、それが持ち物選択に集中していると読めます。

一方でEVの分布は持ち物ほど割れておらず、H2-A32-S32が単独で多数派を占めています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H2-A32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>69.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-B2-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.2%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-D2-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-B1-D1-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.0%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A32-S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.2%</td>
</tr>
</tbody>
</table>
</div>

H2-A32-S32が69.0%と圧倒的多数派で、残りはHPをB・Dに少量振り替える微調整型が分散しているにとどまります。持ち物の選択は「初撃をどう通すか」という運用方針の違いを反映して大きく割れる一方、EVは攻撃・素早さを最大化する配分がどの型でもほぼ共通しており、割れる軸と割れない軸がはっきり分かれています。使用率19位というデータの表面だけを見ると単一の型のポケモンに見えますが、実際には3つの型がほぼ拮抗して並立している点に注意が必要です。

---

## 苦手なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダストシュートは最大で確定3発。メガボーマンダの主力すてみタックル（採用率73.4%）は確定1〜2発で、型によっては先手を取れますが、火力差で先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とびひざげり（採用率89.0%）は確定2発ですが、カバルドンの主力じしん（採用率99.3%、じめん×2弱点）が確定1発で先に落とされます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダストシュート（採用率75.8%）は確定3発止まり。ギャラドスの主力たきのぼり（採用率63.1%、みず×2弱点）は確定2発で先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダストシュート（採用率75.8%）は確定2〜3発、カイリューの主力りゅうせいぐん（採用率50.8%）は確定1〜2発。素早さでは先手を取れますが、火力差で先に落とされます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定1発。メガグソクムシャの主力ドリルライナー（採用率25.6%）は確定1発ですが、素早さで上回り先に倒し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定1発。ルカリオの主力はどうだん（採用率75.1%）は確定2発止まりで、先に倒し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とびひざげり（採用率89.0%）が確定2発。ブリジュラスの主力りゅうせいぐん（採用率65.3%）も確定2発ですが、先手を取って先に倒し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定1発。サーフゴーの主力シャドーボール（採用率99.9%）は確定2発止まりで、先に倒し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定1発。ゴリランダーの主力10まんばりき（採用率50.3%）も確定1発ですが、先手を取って先に倒し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定2発。アーマーガアの主力ブレイブバード（採用率37.6%）は確定3発止まりで、先に倒し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダストシュート（採用率75.8%）が確定2発。メガリザードンYの主力オーバーヒート（採用率22.7%）も確定2発ですが、先手を取って先に倒し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定3発。ウルガモスの主力むしのさざめき（採用率35.4%）は確定4発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんボール（採用率98.7%）が確定2発。アローラキュウコンの主力ふぶき（採用率69.1%）は確定5発止まりで、先に倒し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダストシュート（採用率75.8%）が確定2発。ニンフィアの主力ハイパーボイス（採用率99.3%）は確定4発止まりで、先に倒し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でエースバーンと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
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
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ボーマンダ**（1位）はドラゴン/ひこうで、みず技を半減で受けられます。エースバーンの弱点であるみず・じめんのうち、じめん技はひこうタイプで無効化できるため、じめん技を撃ってくる相手への受け出し先を用意できる組み合わせです。

**ガブリアス**（3位）はドラゴン/じめんで、エースバーンの弱点であるじめん・いわのうち、いわ技を半減で受けられます。ガブリアスの弱点であるこおり技も、エースバーン側は半減で受けられます。

**カバルドン**（6位）はじめん単タイプです。あくびによる交代誘導とステルスロックの設置役を担い、カバルドンが場を動かしている間にエースバーンを後続の攻め手として対面に出せる選出構築上の役割分担があります。

---

## まとめ

M-6のエースバーンは使用率19位。かえんボール98.7%・とびひざげり89.0%を中心とした技構成はほぼ固定される一方、持ち物はこだわりスカーフ33.0%・きあいのタスキ31.2%・いのちのたま24.4%と3分割されています。

- **使用率19位**：ほのお単タイプ、A116・S119の物理アタッカー。特性リベロは場に出て最初の技のタイプに1度だけ変化する仕組みです
- **技構成はほぼ固定**：かえんボール・とびひざげり・ダストシュートの3タイプ打点が主力技の中核です
- **持ち物は3分割**：こだわりスカーフ（速攻）・きあいのタスキ（耐久）・いのちのたま（最大打点）のいずれかを選ぶかたちで型が分かれています

みず・じめん・いわの3弱点は環境上位に広く存在するため、選出段階でのケアが引き続き求められます。

---

## 関連記事

- [【ポケモンチャンピオンズ】アシレーヌ 考察 M-6 シーズン 使用率3位の解説](/blog/primarina-analysis-m6/)
