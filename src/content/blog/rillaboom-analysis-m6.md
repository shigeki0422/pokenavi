---
title: '【ポケモンチャンピオンズ】ゴリランダー 考察 M-6 シーズン 使用率11位の解説'
description: 'M-6シーズン使用率11位のゴリランダーを考察。特性グラスメイカーでグラスフィールドを自動展開し、グラススライダーの先制化とグラスシードのB上昇を両立する仕組み、A実数値194の火力とアシレーヌ・ルカリオとの弱点補完をデータで解説します。'
pubDate: '2026-09-14'
updatedDate: '2026-09-14'
heroImage: '../../assets/hero-rillaboom-m6.png'
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
  <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" />
  <div>
    <h2 style="margin:0 0 8px">ゴリランダー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">11位</strong>　特性: <strong>グラスメイカー 99.7%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・採用率データは2026-09-10時点のものです。

M-6シーズンのゴリランダーは使用率11位。くさ単タイプながら特性グラスメイカーで登場時からグラスフィールドを自動展開し、一致技グラススライダーを実質的な先制技として使えるのが最大の特徴です。A32・いじっぱりのA実数値は194に達し、グラススライダー・はたきおとす・とんぼがえりを軸に高い制圧力を発揮します。

---

## ゴリランダーの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:83%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">125</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

A125・H100の高い物理アタッカーラインが特徴で、C60・D70の特殊面は控えめです。S85は環境上位の多くに素の状態では劣りますが、後述のグラスフィールド展開下ではグラススライダーが優先度+1になるため、Sの遅さを実質的にカバーできます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお・こおり・どく・ひこう・むしの5タイプ（いずれも×2）と単タイプなりに広く、無効はありません。耐性はじめん・みず・くさ・でんきの4タイプに半減が付きます。ほのお・こおりは環境上位に広く存在する弱点で、選出段階でのケアが必要です。

### 特性

**グラスメイカー（99.7%）**がほぼ固定で採用されています。場に出てから5ターンの間、全体の場をグラスフィールド状態にする特性です。グラスフィールドが展開されている間、地面にいるポケモンのグラススライダーは優先度+1になり、さらに地面にいるポケモンのくさ技の威力がフィールド補正で1.3倍になります（いのちのたまの1.3倍補正とは別枠で、両方所持していれば重複して乗ります）。ゴリランダー自身もグラス技（グラススライダー・ウッドハンマー）が対象のため、S85を先制で補うだけでなく火力そのものも底上げされる点が中核的な強みです（優先度+1になるのはグラススライダーのみですが、フィールド補正の威力1.3倍はグラス技全般に及びます）。もう一方の**しんりょく**（0.3%）はHPが1/3以下でくさ技が1.5倍になる特性ですが、採用率は少数にとどまります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>グラススライダー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">94.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致。グラスフィールド下で優先度+1になるメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が道具を持っていれば威力1.5倍。道具を失わせる追加効果</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">61.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代し後続へ対面を引き継ぐ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんばりき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技が半減されるはがね・ほのおタイプへの打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラムアタック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>39.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致。相手の素早さを1段階下げる追加効果</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウッドハンマー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>26.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致最大打点。与えたダメージの1/3の反動を受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やどりぎのタネ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手からHPを吸収し続ける。くさタイプの相手には無効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃を2段階上昇</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を変化技禁止状態にする</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：いのちのたまアタッカー型

**代表的な性格: いじっぱり（全体の性格採用率86.8%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いのちのたまアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> グラスメイカー（99.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-S2<br>
<strong>持ち物:</strong> いのちのたま（24.8%）
</div>
<div>
<strong>技構成:</strong><br>
・グラススライダー<br>
・はたきおとす<br>
・とんぼがえり<br>
・10まんばりき
</div>
</div>
</div>

いのちのたまで全技の威力を1.3倍にし、グラススライダー・はたきおとす・とんぼがえりの3タイプでの打点を底上げする構成です。10まんばりきはくさ技が半減される相手（はがね・ほのおタイプ等）への専用の打点で、いのちのたまの一律1.3倍補正がこの非くさ打点にもそのまま乗る点が次に紹介するグラスシード型との違いです。

**強み:**

H32-A32-S2・いじっぱりのA実数値は**194**（H207）。いのちのたまの補正込みで、はたきおとす・とんぼがえり・10まんばりきなど技タイプを問わず打点を伸ばせるため、相手の耐性次第で技を選び分けても火力が落ちません。

**弱み:**

型1の技構成にはウッドハンマー（威力120）が含まれておらず、くさ最大打点はグラススライダー（威力55）にとどまるため、くさ技が等倍以下で通る相手への一撃の大きさは型2に劣ります。加えていのちのたまは攻撃のたびに最大HPの1/10の反動を受けるため、長期戦での運用には向きません。

---

### 型2：グラスシード耐久型

**代表的な性格: いじっぱり（全体の性格採用率86.8%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">グラスシード耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> グラスメイカー（99.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-B2<br>
<strong>持ち物:</strong> グラスシード（17.5%）
</div>
<div>
<strong>技構成:</strong><br>
・グラススライダー<br>
・ウッドハンマー<br>
・はたきおとす<br>
・とんぼがえり
</div>
</div>
</div>

グラスシードは「グラスフィールド状態の時に防御が1段階上がる」持ち物で、グラスメイカー自身が場を展開した瞬間に自動で発動します。場に出たターンからB上昇状態で受け出せる型です。型1のいのちのたまが技タイプを問わず火力を底上げするのに対し、この型はグラスシードの効果がB上昇のみに限られる代わりに反動がなく、ウッドハンマー（威力120、与えたダメージの1/3の反動あり）を主力打点として使い切れます。

**強み:**

B実数値は112ですが、グラスシードの防御1段階上昇（×1.5）が乗ると**168**まで伸びます。発動条件がグラスメイカー起動と同時のため実戦で確実に乗る点が特徴です。いのちのたまのような反動がないため、被ダメージの大きいウッドハンマーを連発しても自滅しにくい点が型1との違いです。

**弱み:**

いのちのたまのような技全体への威力補正がないため、グラス技以外（10まんばりき等）の打点は型1に劣ります。またグラスシードは1度の対戦で1回しか発動しないため、場に出た瞬間の防御上昇を使い切った後は通常のBのまま戦うことになります。

---

## データ分析：くさタイプ打点のカバレッジ

M-6使用率TOP20（2026-09-10時点、ゴリランダー自身を除く19体）を対象に、くさタイプの技（グラススライダー・ドラムアタック・ウッドハンマー）とサブウェポンの10まんばりき（じめん技）がどこまで通るかを機械的に整理しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手（使用率順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">くさ技倍率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10まんばりき倍率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/じめん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボーマンダ（2位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">無効（×0）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシレーヌ（3位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず/フェアリー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">グソクムシャ（4位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">むし/みず</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（5位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">じめん単</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ルカリオ（6位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かくとう/はがね</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（7位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">はがね/ドラゴン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">セグレイブ（8位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/こおり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サーフゴー（9位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">はがね/ゴースト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギルガルド（10位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">はがね/ゴースト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミッキュ（12位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ゴースト/フェアリー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャ（13位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">くさ/あく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アーマーガア（14位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ひこう/はがね</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">無効（×0）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（15位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">無効（×0）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">キラフロル（16位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">いわ/どく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×4</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">イダイトウ（メス）（17位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず/ゴースト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードン（18位、メガYが60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ほのお/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">無効（×0）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エースバーン（19位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ほのお単</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガ（20位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず/あく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
</tbody>
</table>
</div>

※表中の「—」は等倍を示します。

TOP20圏内でくさ技が半減以下になる相手は10体（ボーマンダ・ルカリオ・ブリジュラス・セグレイブ・サーフゴー・ギルガルド・マスカーニャ・アーマーガア・リザードン・エースバーン）で、このうちルカリオ・ブリジュラス・サーフゴー・ギルガルド・エースバーンの5体は10まんばりきが弱点を突けて穴を埋められます。一方、じめん技はひこうタイプに無効となるため、ボーマンダ・アーマーガア・リザードン・ギャラドスのようなひこう複合の相手には10まんばりきも通らず、くさ以外の決定打を欠きます（ギャラドスはくさ技自体は等倍で通ります）。さらにマスカーニャ（くさ/あく）はくさ技だけでなくじめん技にも×0.5にとどまるため、10まんばりきで補いきれない相手の中でも最も崩しにくい対面です。実際にボーマンダ・アーマーガア・リザードンの3体は後述の「苦手なポケモン」にも並んでおり、技構成のカバレッジが機能しない範囲がそのまま苦手対面として現れています。逆にキラフロル（16位、いわ/どく）はくさ技が等倍にとどまる一方、10まんばりきが×4で突き刺さる最大の相殺ポイントになっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率66.5%）は確定5発と決め手を欠き、メガボーマンダの主力すてみタックル（採用率73.4%）の確定1発に先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さで上回りますが、10まんばりき（採用率50.3%）は確定4発。メガグソクムシャの主力であいがしら（採用率83.0%、出てきた直後の対面限定の技）の確定1発に、その対面では先制でも押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウッドハンマー（採用率26.7%）は確定2発。セグレイブの主力つららおとし（採用率43.3%、こおり×2弱点）も確定2発ですが、素早さはセグレイブが上のため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さでは上回りますが、はたきおとす（採用率66.5%）はほぼ倒しきれない水準に留まります。一方アーマーガアの主力ブレイブバード（採用率37.6%、ひこう×2弱点）は確定3発でじりじり削られ、決め手を欠いたまま押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんばりき（採用率50.3%）は確定2発。メガリザードンXの主力フレアドライブ（採用率36.5%、ほのお×2弱点）の確定1発に、素早さで劣るため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率66.5%）は確定3発。メガリザードンYの主力かえんほうしゃ（採用率42.9%、ほのお×2弱点）の確定1発に、素早さで劣るため先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんばりき（採用率50.3%）は確定1発ですが、エースバーンの主力かえんボール（採用率98.7%、ほのお×2弱点）も確定1発で、素早さで劣るため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率66.5%）は確定3発。ウルガモスの主力むしのさざめき（採用率35.4%）は確定2発で、素早さで劣るため先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率66.5%）は確定4発と決め手を欠き、カイリューの主力エアスラッシュ（採用率45.2%、ひこう×2弱点）の確定2発に、素早さで劣るため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり（採用率61.5%）は確定2発。サザンドラの主力りゅうせいぐん（採用率95.7%）も確定2発と互角ですが、素早さで劣るため先に沈められます</td>
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
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">グラススライダー（採用率94.5%、くさ×2弱点）が確定1発。アシレーヌの主力ムーンフォース（採用率99.1%）は確定2発止まりで、グラスフィールド下の優先度+1もあり先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウッドハンマー（採用率26.7%、じめん×2弱点）で確定1発。カバルドンの主力じしん（採用率99.3%）は確定不可の水準で、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率66.5%）が確定2発。ギルガルドの主力ポルターガイスト・シャドーボール（採用率54.0%/42.9%）も確定2発と競り合いますが、素早さで上回り先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さでは後攻になりますが、ドラムアタック（採用率39.1%）が確定2発。ミミッキュの主力じゃれつく（採用率98.1%）は確定3発と決め手を欠くため、後攻でも先に沈めきれます（ばけのかわは1回目の攻撃をダメージの代わりに最大HPの1/8を削るだけで済ませる特性で、2発目以降は通常通りダメージが通ります）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウッドハンマー（採用率26.7%）が確定3発。ギャラドスの主力やけっぱち（採用率28.9%）も確定3発と互角ですが、素早さで上回り先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ（メス）" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ（メス）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴリランダーのS実数値107では後攻ですが、グラスフィールド下でグラススライダー（採用率94.5%）の優先度+1により先に動け、確定1発で落とせます。イダイトウの主力ウェーブタックル（採用率96.5%）は確定3発です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴリランダーのS実数値107では後攻になる型もありますが、グラスフィールド下のグラススライダーが優先度+1のため、いずれの型に対しても先に動け、確定1発で落とせます。ウォッシュロトムの主力ハイドロポンプ（採用率97.1%）は確定4発です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウッドハンマー（採用率26.7%）が確定2発。ニンフィアの主力ハイパーボイス（採用率99.3%）は確定3発で、素早さで上回り先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でゴリランダーと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**アシレーヌ**（3位）はみず/フェアリーで、ゴリランダーの弱点であるほのお・こおり・むしの3タイプを半減で受けられます。逆にアシレーヌの弱点であるくさ・でんき技はゴリランダーが半減で受けられるため、お互いに相手の弱点タイプを持ち込まれた際の受け出し先を用意できる組み合わせです（どく技はどちらも弱点のため補完できません）。

**ルカリオ**（4位）はかくとう/はがねで、ゴリランダーの弱点であるどく技を無効化でき、むし技も4分の1、こおり技も半減で受けられます。ゴリランダーの弱点5タイプのうち3タイプをルカリオがカバーする組み合わせです。なお同居率8位のブリジュラス（はがね/ドラゴン）、9位のサーフゴー（はがね/ゴースト）、10位のギルガルド（はがね/ゴースト）も同じくどく技を無効化でき、どく技への受け出し先はルカリオに限られません。

**ボーマンダ**（1位）はドラゴン/ひこうで、ゴリランダーの弱点であるほのお・むしを半減で受けられます。ただしこおり技はボーマンダも4倍弱点のため、ゴリランダーの弱点をそのまま共有してしまう点には注意が必要です。

---

## まとめ

M-6のゴリランダーは使用率11位。特性グラスメイカーによるグラスフィールドの自動展開が、S85というやや控えめな素早さを補うだけでなく、くさ技の火力自体も底上げする中核の仕組みです。

- **グラスメイカー99.7%固定**：登場から5ターン、グラススライダーが優先度+1になる状態を自動で作れるうえ、くさ技（グラススライダー・ウッドハンマー）の威力が1.3倍になります
- **A実数値194（いじっぱりH32-A32-S2）**：いのちのたまと組み合わせることで技タイプを問わず高火力を維持できます
- **弱点5タイプ・耐性4タイプ**：はがね・ほのお系のくさ半減相手には10まんばりき（採用率50.3%）で穴を埋められますが、ひこう複合（ボーマンダ・アーマーガア・リザードンなど）にはじめん技も無効となるため決定打を欠きます

ほのお・こおり・どく・ひこう・むしの5弱点は環境上位に広く存在するため、選出段階でのケアは引き続き必要ですが、アシレーヌ・ルカリオといった弱点補完に優れるパートナーとの同居率が高く、パーティ単位でのカバーがしやすいポケモンです。

---
