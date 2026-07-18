---
title: '【ポケモンチャンピオンズ】マスカーニャ 考察 M-4 シーズン こだわりスカーフ型の立ち回り'
description: 'M-4シーズン使用率5位のマスカーニャを考察。こだわりスカーフ採用率70.9%・とんぼがえり71.1%・特性へんげんじざいで対面ごとにタイプを変えるスカーフアタッカーの型と、むし×4・フェアリー等6タイプの弱点、苦手なポケモンをデータで解説します。'
pubDate: '2026-07-16'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-meowscarada-m4.png'
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
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" />
  <div>
    <h2 style="margin:0 0 8px">マスカーニャ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">5位</strong>（M-3: 3位）　持ち物: <strong>こだわりスカーフ 70.9%</strong>
    </div>
  </div>
</div>

M-4シーズン、マスカーニャは使用率5位（M-3: 3位）で環境上位に定着しています。特性**へんげんじざい**で最初に出す技のタイプに自分の身をタイプ変化させ、その技に一致技補正をかけられるのが最大の特徴で、こだわりスカーフを70.9%が採用し、S123の素早さを1.5倍にして対面の相手を上から動かすアタッカー運用が主流です。

---

## マスカーニャの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">76</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">110</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">123</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

種族値合計530のうちS123が最大値で、こだわりスカーフ込みの実数値は後述のとおり288に達します。A110は環境上位のアタッカーとしては中堅クラスですが、へんげんじざいによる一致技補正がこの数値を底上げします。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
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

むし×4が最大の弱点で、耐性タイプは6つ確保しつつも×2弱点が6タイプと非常に広いのが特徴です。特にフェアリー弱点は環境2位のミミッキュ（じゃれつく採用率98.2%）、こおり弱点はアローラキュウコン（16位、フリーズドライ84.4%）と、上位ポケモンの主力技が直撃しやすい点は立ち回りの制約になります。

### 特性

**へんげんじざい（93.0%）**が固定に近い採用率です。場に出てから最初に技を選んだ瞬間、自分のタイプがその技のタイプに変化し、一致技補正（×1.5）がかかります。くさ/あく本来のタイプ以外の技（かみなりパンチ・じゃれつく等）を最初に選んでも一致技扱いになる点が、後述の型の技構成の広さにつながっています。この変化は登場するたびに1回だけで、2手目以降の技には適用されません。もう一つの**しんりょく（7.0%）**はHPが1/3以下になるとくさ技の威力が1.5倍になる特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリックフラワー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">必中・必ず急所。へんげんじざいで一致技化されるメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリプルアクセル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20/40/60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">86.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">連続3回攻撃。ガブリアス・カイリュー等のドラゴンに×4</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">71.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。こだわりスカーフの技固定を対面操作で補う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>64.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が道具を持つと威力1.5倍。持ち物を失わせつつゴースト・エスパーへ打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手が攻撃技を選んだ時のみ成功。きあいのタスキ型と相性が良い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス・アーマーガア等のみず・ひこう複合へ×2〜×4</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じゃれつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サザンドラ等のドラゴンに×4。10%で相手のこうげきを1段階下げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置。とんぼがえりでの対面操作と組み合わせて継続的に削る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワージェム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードン・ウルガモス等のほのお/むしへの打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：ようき スカーフアタッカー型

**性格採用率: ようき 58.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ようき スカーフアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（93.0%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（最多分布61.1%）<br>
<strong>持ち物:</strong> こだわりスカーフ（70.9%）
</div>
<div>
<strong>技構成:</strong><br>
・トリックフラワー<br>
・トリプルアクセル<br>
・とんぼがえり<br>
・はたきおとす
</div>
</div>
</div>

トリックフラワー（くさ・威力70・必中・必ず急所）とトリプルアクセル（こおり・連続3回攻撃で最大威力60）が主力技。とんぼがえり（むし・威力70）は攻撃後に交代でき、こだわりスカーフの技固定デメリットを対面操作で補います。はたきおとす（あく・威力65、相手が道具を持っていると1.5倍）は道具破壊を兼ねた打点です。

**強み:**

ようきのS実数値は192で、こだわりスカーフ込みだと288に達します。環境上位の多くのスカーフ持ち（S実数値200台前半が目安）を上から動かせる速さで、最初に選ぶ技をへんげんじざいで一致技化しつつ後攻を許さない対面操作ができます。

**弱み:**

こだわりスカーフは最初に選んだ技に固定されるため、相手の交代読みが外れて選んだ技が通らない相手（半減以下）が出てくると、その技を撃ち続けるか自分から交代するかしか選べません。とんぼがえり以外の技を選んでいた場合は、対面操作の技すら選べず不利な打ち合いを強いられます。

---

### 型2：いじっぱり アタッカー型

**性格採用率: いじっぱり 34.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱり アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（93.0%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（最多分布61.1%）<br>
<strong>持ち物:</strong> こだわりスカーフ、またはきあいのタスキ（18.5%）
</div>
<div>
<strong>技構成:</strong><br>
・トリックフラワー<br>
・トリプルアクセル<br>
・とんぼがえり<br>
・はたきおとす
</div>
</div>
</div>

技構成はようき型と同一で、性格による火力と素早さの違いが型を分けます。きあいのタスキ採用時はHP満タンから一撃技を確定1耐えできるため、後攻からでも確実に1発を通す運用に向きます。

**性格差：Aの違いが決めるカバルドンへの削り量、Sの違いが決めるガブリアスとの先手争い**

いじっぱりのA実数値は178でようき型（A162）より高く、カバルドン（3位・じめん単、わんぱく採用率72.6%・B実数値187）へトリックフラワー（くさ・×2弱点、常時急所）を撃つ場合、いじっぱりは116〜138ダメージ（54.0〜64.2%）で確定2発、ようきは104〜126ダメージ（48.4〜58.6%）で乱数2発にとどまります。A実数値の差はこのカバルドンとの対面で確定数の差として実際に現れます。S実数値はいじっぱりが175、ようきが192で、こだわりスカーフ込みではいじっぱりS262・ようきS288まで伸びます。環境1位のガブリアス（スカーフ採用率19.8%・ようき想定でS253）に対し、いじっぱり型のスカーフ込みS262はわずかに上回るにとどまりますが、ようき型のS288は余裕を持って上から取れます。

---

## データ分析①：M-3→M-4 使用率・採用データの変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">6.4%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">7.5%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どくびし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">5.3%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">5.1%</strong></td>
</tr>
</tbody>
</table>
</div>

使用率は3位から6位に下がりましたが、こだわりスカーフ70.9%・トリックフラワー97.3%・トリプルアクセル86.1%・とんぼがえり71.1%というコア技構成の採用率はM-3からほぼ横ばいです。型そのものの構築思想は変わっておらず、じゃれつく（フェアリー）採用が9.8%→7.5%に下がった一方、どくびし・パワージェムがそれぞれ5%台で新たに上位10技へ入り、こだわりスカーフの4枠目以降を補助的なタイプの技（どく・いわ）で埋める構築が一部で試されている点がM-4の変化です。

---

## データ分析②：技タイプ別カバレッジ計算

マスカーニャが採用する攻撃技（くさ・こおり・むし・あく・でんき・フェアリー）が、M-4使用率TOP15の相手にどこまで通るかを整理しました（相手ごとに最大打点となる技のみ抜粋）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">最大打点の技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">倍率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">当該技の採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリプルアクセル（こおり）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">86.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（3位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリックフラワー／トリプルアクセル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">97.3% / 86.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリュー（12位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリプルアクセル（こおり）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">86.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（8位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かみなりパンチ（でんき）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.3%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サザンドラ（13位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">じゃれつく（フェアリー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタグロス（4位）／マフォクシー（9位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">はたきおとす（あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">64.5%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アシレーヌ（7位）／ゲッコウガ（15位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリックフラワー（くさ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">97.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードン（11位）／アーマーガア（14位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かみなりパンチ（でんき）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.3%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（6位）／アローラキュウコン（16位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">（等倍が上限）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミッキュ（2位）／バシャーモ（10位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">（等倍が上限）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
</tbody>
</table>
</div>

TOP15の中で×4が通る相手が4体（ガブリアス・カイリュー・ギャラドス・サザンドラ）ある一方、カバルドンには×2、ミミッキュ・バシャーモ・ブリジュラス・アローラキュウコンには等倍止まりです（採用率5.1%のパワージェムはリザードン×4・アローラキュウコン×2の打点を持ちますが、少数派のため対象から除外しています）。かみなりパンチ・じゃれつくは高倍率が出る技ですが採用率14.3%・7.5%にとどまり、こだわりスカーフでこれらを選んでいない試合では、トリックフラワー・トリプルアクセル・はたきおとすの範囲で打点を選ぶことになり、相手読みを外すと威力を発揮しきれない点は運用上のトレードオフです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー・採用率98.2%）が×2弱点。マスカーニャの技はゴースト/フェアリー複合にいずれも等倍が上限で、有効打が乏しい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率84.2%）とマジカルシャイン（フェアリー・採用率63.7%）の両方が×2弱点を突きます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（ほのお・採用率84.7%）とインファイト（かくとう・採用率67.2%）の両方が×2弱点。マスカーニャの技はほのお/かくとう複合に等倍が上限です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（こおり・採用率87.2%）とヘドロウェーブ（どく・採用率68.1%）がともに×2弱点。マスカーニャ側もトリックフラワー（くさ）・とんぼがえり（むし）がともに×2で通るため撃ち合いになりやすい相手です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ（こおり・採用率84.4%）とムーンフォース（フェアリー・採用率47.4%）がともに×2弱点。主力4技（トリックフラワー・トリプルアクセル・とんぼがえり・はたきおとす）は等倍止まりで、決定打を欠きます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でマスカーニャと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、マスカーニャのむし×4弱点をガブリアスは等倍で受けられる関係です。一方、マスカーニャのこおり弱点（×2）はこおり技を持つ相手を苦手にしますが、ガブリアス自身もこおり×4弱点を抱えるため、こおり技を撃たれる相手に対しては両者とも弱く、この組み合わせで解決される弱点ではありません。ガブリアスのじしんがマスカーニャの弱点であるほのおタイプの相手を処理する一方、マスカーニャの攻撃技はこおりタイプに抜群を取れないため、こおりタイプの相手はガブリアスのがんせきふうじ等、別の枠で対応する必要があります。

**カバルドン**（3位）はじめん単タイプで、あくびとステルスロックのサポート役です。カバルドンのあくびで後続への引き先を確保し、相手の対面選択を狂わせたところにマスカーニャのスカーフ技を通しやすくします。

**アシレーヌ**（3位）はみず/フェアリーで、マスカーニャのほのお弱点（×2）をアシレーヌが耐性（×0.5）で受けられます。アシレーヌのフェアリー打点がドラゴン・あくタイプの相手を処理し、マスカーニャのはたきおとす（あく）がエスパー・ゴーストタイプの相手を分担します。

**ミミッキュ**（4位）はゴースト/フェアリーで、ばけのかわを盾に積み技（つるぎのまい84.8%）で後続を通す運用です。マスカーニャのとんぼがえりで相手の後出しを誘い、ミミッキュが安全に場に出るターンを作る組み合わせが機能します。

**ブリジュラス**（6位）ははがね/ドラゴンで、マスカーニャのひこう弱点（×2）をブリジュラスが耐性（×0.5）でカバーします。ブリジュラスのラスターカノン・りゅうせいぐんが特殊方面の打点を担い、マスカーニャの物理打点と役割が分かれています。

---

## まとめ

M-4のマスカーニャは使用率5位（M-3: 3位）ながら、型の構築思想はM-3から大きく変わっていません。

- **こだわりスカーフ70.9%・トリックフラワー97.3%・トリプルアクセル86.1%・とんぼがえり71.1%というコア構成はM-3からほぼ横ばい**：使用率順位は下がったものの、主流の型自体は安定
- **ようき型（S192・スカーフ込み288）は環境1位ガブリアスのスカーフ個体（S253）に余裕で先手を取れるが、いじっぱり型（S262）はわずかに上回るのみ**：一方でいじっぱり型はA178でカバルドンへの削り量が優る。EV配分は同一（H2-A32-S32）
- **どくびし・パワージェムがM-4で新たに上位10技へ台頭**：こだわりスカーフの技固定という制約の中で、ガブリアス以外への打点を補う技選択が模索されている

へんげんじざいで最初の技を必ず一致技化できる点と、こおり・むし技を絡めた広い打点範囲が武器ですが、フェアリー・ほのお複合には等倍止まりが多く、ミミッキュ・マフォクシー・バシャーモといった上位ポケモンには有効打を欠く場面があります。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
