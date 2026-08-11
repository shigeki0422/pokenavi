---
title: '【ポケモンチャンピオンズ】マスカーニャ 考察 M-5 シーズン きあいのタスキ型台頭の理由'
description: 'M-5シーズン使用率4位（M-4終盤:3位）のマスカーニャを考察。こだわりスカーフ採用率が70.9%→55.2%に低下する一方、きあいのタスキ28.7%・しんりょく20.7%が伸びた型分布の変化と、苦手なポケモン・同居率をデータで解説します。'
pubDate: '2026-08-10'
updatedDate: '2026-08-10'
heroImage: '../../assets/hero-meowscarada-m5.png'
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
      使用率: <strong style="color:#e67e22">4位</strong>（M-4終盤: 3位）　持ち物: <strong>こだわりスカーフ 55.2%</strong>
    </div>
  </div>
</div>

M-5シーズン、マスカーニャは使用率4位につけています。M-4終盤（2026-08-04時点）の3位からはほぼ横ばいで、順位自体に大きな動きはありません。特性**へんげんじざい**は最初に出す技のタイプに自分の身をタイプ変化させ、その技に一致技補正をかけるのが最大の特徴で、こだわりスカーフを軸にした対面操作アタッカーという基本コンセプトはM-4から継続しています。一方で中身の型分布は変わっており、こだわりスカーフ採用率は55.2%まで下がり、きあいのタスキ・しんりょくを組み合わせた別の型が台頭しています。

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

種族値合計530のうちS123が最大値で、こだわりスカーフ込みのS実数値は後述のとおり288に達します。A110は使用率1位のガブリアス（A130）ほどではなく、物理アタッカーとして突出した数値ではありませんが、へんげんじざいによる一致技補正がこの数値を底上げします。

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

むし×4が最大の弱点で、耐性タイプは6つ確保しつつも×2弱点が6タイプと非常に広いのが特徴です。特にフェアリー弱点は環境5位のミミッキュ（じゃれつく採用率97.3%）、どく弱点は14位のキラフロル（ヘドロウェーブ採用率61.6%）と、上位ポケモンの主力技が直撃しやすい点は立ち回りの制約になります。

### 特性

**へんげんじざい（79.3%）**が引き続き主流です。場に出てから最初に技を選んだ瞬間、自分のタイプがその技のタイプに変化し、一致技補正（×1.5）がかかります。くさ/あく本来のタイプ以外の技（かみなりパンチ・じゃれつく等）を最初に選んでも一致技扱いになる点が、後述の型の技構成の広さにつながっています。この変化は登場するたびに1回だけで、2手目以降の技には適用されません。もう一つの**しんりょく（20.7%）**はHPが1/3以下になるとくさ技の威力が1.5倍になる特性で、M-4時点の7.0%から3倍近くに採用率が伸びています（背景は後述のデータ分析で扱います）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">必中・必ず急所。へんげんじざいで一致技化されるメインウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリプルアクセル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20/40/60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">連続3回攻撃で全弾命中時の合計威力120（3発目は威力60）。ガブリアス・カイリュー等のドラゴンに×4</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">65.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が道具を持つと威力1.5倍。持ち物を失わせつつゴースト・エスパーへ打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。こだわりスカーフの技固定を対面操作で補う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>30.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手が攻撃技を選んだ時のみ成功。きあいのタスキ型と相性が良い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アーマーガア等のひこう複合へ×2。ギャラドスはメガ後（みず/あく、ギャラドスナイト採用率77.8%）なら×2、メガ前（みず/ひこう）なら×4</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置。とんぼがえりでの対面操作と組み合わせて継続的に削る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じゃれつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サザンドラ等のドラゴン/あく複合に×4だが採用率5.0%のため多くの個体は未採用。10%で相手のこうげきを1段階下げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>イカサマ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の実数値Aを参照。物理アタッカー相手に威力が伸びる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワージェム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードン等のほのおタイプ、ウルガモス等のむしタイプへの打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-5の採用型

### 型1：こだわりスカーフ アタッカー型

**性格採用率: ようき 61.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい（79.3%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（57.6%）<br>
<strong>持ち物:</strong> こだわりスカーフ（55.2%）
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

トリックフラワー（くさ・威力70・必中・必ず急所）とトリプルアクセル（こおり・連続3回攻撃で合計威力120）が主力技です。とんぼがえり（むし・威力70）は攻撃後に交代でき、こだわりスカーフの技固定デメリットを対面操作で補います。はたきおとす（あく・威力65、相手が道具を持っていると1.5倍）は相手の持ち物を落とす効果も兼ねた打点です。

**強み:**

ようきのS実数値は192で、こだわりスカーフ込みだと288に達します。使用率1位のガブリアスは最速でもS実数値169、スカーフを持たせても253であり、マスカーニャのスカーフ型288が上回ります。最初に選ぶ技をへんげんじざいで一致技化しつつ、先制技を除けば多くの相手に対して後手に回らない立ち回りができます。

**弱み:**

こだわりスカーフは最初に選んだ技に固定されるため、相手の交代読みが外れて選んだ技が通らない相手（半減以下）が出てくると、その技を撃ち続けるか自分から交代するかしか選べません。とんぼがえり以外の技を選んでいた場合は、対面操作の技すら選べず不利な打ち合いを強いられます。

---

### 型2：きあいのタスキ＋しんりょく型

**特性採用率: しんりょく 20.7%（M-4: 7.0%）　性格採用率: いじっぱり 32.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ＋しんりょく型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> しんりょく（20.7%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32-B2-S32（15.6%）<br>
<strong>持ち物:</strong> きあいのタスキ（28.7%）
</div>
<div>
<strong>技構成:</strong><br>
・トリックフラワー<br>
・トリプルアクセル<br>
・ふいうち<br>
・とんぼがえり
</div>
</div>
</div>

きあいのタスキはHP満タンから受けた一撃をHP1で耐える持ち物です。タスキで耐えた時点でHPは最大の1/3以下になるため、特性しんりょくの発動条件（HP1/3以下でくさ技威力1.5倍）を同時に満たします。トリックフラワーは通常でも一致技補正（×1.5）がかかりますが、しんりょく発動後はさらに1.5倍が乗り、無補正の実質威力70に対して157.5相当（一致技のみ・型1のスカーフ型は105相当）まで伸びます。ふいうち（優先度+1）はタスキで耐えた次のターン、相手が攻撃技を選んでいれば先制で打ち取れる技で、この型で採用率が上がっています。

**強み:**

型1のスカーフ型は最初に選んだ技に固定されますが、この型はこだわり系の道具を持たないため、場に出た後で相手の技を見てから技を選び直せます。HP1まで耐えてからのトリックフラワーは一致技補正としんりょくが重なり、スカーフ型のトリックフラワーより火力が高くなります。

**弱み:**

この型はいじっぱり（A↑ S無補正）のためS実数値は175にとどまり、こだわりスカーフのS実数値288はもちろん、スカーフを持たないようき型のS実数値192にも届きません。きあいのタスキは既に何らかのダメージ（設置技等）を受けていると発動せず、1回きりの効果のため、発動を前提にした運用が崩れると通常のアタッカーより打たれ弱くなります。

---

## データ分析①：M-4（2026-07-13時点）→M-5 技・持ち物・特性の採用率変化

技・持ち物・特性の採用率はM-4シーズン中盤（2026-07-13時点、クロール1日分）の値です。使用率順位のみ、M-4シーズンを通した最終値（2026-08-04時点）と比較します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位（M-4は最終日8/4時点）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.2%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">28.7%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">11.3%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">へんげんじざい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">93.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.3%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんりょく採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">20.7%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">30.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">71.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.1%</strong></td>
</tr>
</tbody>
</table>
</div>

使用率順位はM-4終盤の3位からM-5の4位でほぼ横ばいですが、型の内訳は変化しています。こだわりスカーフ採用率は70.9%→55.2%に低下し、代わってきあいのタスキが18.5%→28.7%、ふいうちが18.5%→30.9%と上昇しています。特性はへんげんじざいとしんりょくの2択で合計100%になるため、へんげんじざい93.0%→79.3%としんりょく7.0%→20.7%は同一の変化の裏表です（しんりょく採用者が増えた分だけへんげんじざい採用者が減っています）。きあいのタスキでHP1まで耐える→しんりょくが発動しトリックフラワーが強化される→優先度+1のふいうちで後続の相手も打ち取る、という一連の運用と整合的な採用率の伸び方です。とんぼがえり（71.1%→57.1%）も低下しており、こだわりスカーフを前提とした対面操作型の比率がM-4より下がったことを示しています。トリックフラワー（96.9%）・トリプルアクセル（87.3%）という主力の攻撃技自体の採用率はほぼ横ばいで、変化しているのは持ち物・特性・技の組み合わせ方です。

---

## データ分析②：技タイプ別カバレッジ計算

マスカーニャが採用する攻撃技（くさ・こおり・むし・あく・でんき・フェアリー・いわ）が、M-5使用率TOP15の相手にどこまで通るかを整理しました（相手ごとに最大打点となる技のみ抜粋）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリプルアクセル（こおり）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カイリュー（8位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリプルアクセル（こおり）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">87.3%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン（10位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">パワージェム（いわ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>×4</strong>（メガX形態は×2、表下で詳述）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス（7位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガ後：トリックフラワー／メガ前：かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガ後×2／メガ前×4（表下で詳述）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.9% / 13.5%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ（2位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリックフラワー（くさ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.9%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン（6位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリックフラワー／トリプルアクセル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.9% / 87.3%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メタグロス（9位）／<img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マフォクシー（11位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">はたきおとす（あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ（オス）" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">イダイトウ（オス）（15位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">トリックフラワー（くさ）／はたきおとす（あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.9% / 65.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア（13位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かみなりパンチ（でんき）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス（3位）／<img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミッキュ（5位）／<img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ハッサム（12位）／<img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">キラフロル（14位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">（等倍が上限）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
</tr>
</tbody>
</table>
</div>

TOP15の中で×4が確実に通るのはガブリアス・カイリューの2体です。リザードンへのパワージェム（いわ、採用率4.2%）は、非メガ・メガY形態（ほのお/ひこう）には×4で通りますが、メガX形態（ほのお/ドラゴン）には×2に半減します。M-5ではリザードンのメガストーン採用率データが欠損しており比率を出せないため、M-4時点（2026-07-13）の比率（メガY 65.3%・メガX 33.5%、非メガはごく少数）を参考値として付記します。ギャラドスへは、メガ後（みず/あく、採用率77.8%）にトリックフラワーが×2で通り、メガ前（みず/ひこう）にはかみなりパンチ（採用率13.5%）が×4で通ります。ブリジュラス・ミミッキュ・ハッサム・キラフロルには等倍止まりです。パワージェム・かみなりパンチはいずれも採用率が低く、こだわりスカーフでこれらを選んでいない試合ではトリックフラワー・トリプルアクセル・はたきおとすの範囲で打点を選ぶことになります。相手読みを外すと威力を発揮しきれない点は型1・型2共通の運用上のトレードオフです。なお、パワージェムは特殊技である一方、マスカーニャは物理寄り（攻撃110・特攻81、EV分布上位はC無振り）のため、実戦での主力打点にはなりにくい点も踏まえて読んでください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ばけのかわで攻撃1発を無効化されるため、S実数値では上回っていても初手の攻撃が透かされます。返しのじゃれつく（フェアリー・採用率97.3%）で×2を受け、優先度+1のかげうち（採用率96.6%）もあり、S優位が機能しません。マスカーニャの技はゴースト/フェアリー複合にいずれも等倍が上限で、有効打も乏しい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・採用率61.6%）とマジカルシャイン（フェアリー・採用率30.0%）がともに×2弱点。マスカーニャの技はいわ/どく複合に等倍が上限です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（ほのお・採用率65.4%）とマジカルシャイン（フェアリー・採用率46.7%）の両方が×2弱点を突きます。マフォクシナイト採用率99.2%でほぼ全個体がメガ化し、おくびょう採用時はS実数値204に達するため、マスカーニャのようき型(192)・いじっぱり型(175)いずれもスカーフ型(288)でなければ先手を取れません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（こおり・採用率91.1%）とヘドロウェーブ（どく・採用率82.5%）がともに×2弱点。マスカーニャ側もトリックフラワー（くさ）が×2で通りますが、メガ個体（65.4%）はメガ後S実数値213に達するため非スカーフのマスカーニャでは先手を取れません（非メガ個体・計34.6%はS122でマスカーニャが上回ります）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（60.4%）・だいもんじ（25.8%）のほのお技が×2弱点を突く場面が多い相手です（詳細は表下）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ハッサム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり（むし・採用率57.6%）が×4弱点。マスカーニャの技はむし/はがね複合に等倍が上限で、優先度+1のバレットパンチ（99.7%）で削り切られやすい相手です</td>
</tr>
</tbody>
</table>
</div>

サザンドラのあくのはどう（採用率99.2%）はマスカーニャに半減、りゅうせいぐん（採用率93.0%）は等倍止まりで、この2つは脅威になりません。こだわりスカーフ採用率82.9%（ひかえめ76.1%が主流）ならS実数値225にとどまり、マスカーニャのスカーフ型（288）には後手を取ります。おくびょう（採用率22.5%）ならS実数値247まで伸びますが、それでも288には届きません。互いにスカーフを持つ場合はマスカーニャが先に動いてトリプルアクセル（こおり技、あく/ドラゴン複合に×2）を通せるため、脅威になるのは主にマスカーニャが非スカーフ（タスキ・いのちのたま等、合計44.8%）でほのお技を受けてしまう場面です。

---

## 同居率上位の分析

M-5でマスカーニャと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" loading="lazy">
    <div class="name">キラフロル</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム" loading="lazy">
    <div class="name">ハッサム</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、マスカーニャのどく弱点（×2）・ほのお弱点（×2）を耐性（×0.5）で受けられます。一方でガブリアス自身もこおり×4・フェアリー×2の弱点を抱えており、この2タイプに対してはマスカーニャと弱点を共有します。ガブリアスのじしんがほのおタイプの相手を処理する一方、マスカーニャのはたきおとす（あく）がゴースト・エスパータイプの相手を分担します。

**アシレーヌ**（2位）はみず/フェアリーで、マスカーニャのむし弱点（×4）・こおり弱点（×2）・かくとう弱点（×2）・ほのお弱点（×2）をいずれも耐性（×0.5）で受けられます。アシレーヌのフェアリー打点がドラゴン・あくタイプの相手を処理し、マスカーニャのトリプルアクセル（こおり）がドラゴンタイプの相手を分担します。

**カイリュー**（3位）はドラゴン/ひこうで、マスカーニャのむし弱点（×4）・かくとう弱点（×2）・ほのお弱点（×2）を耐性（×0.5）で受けられます。ガブリアスと同様にこおり×4・フェアリー×2の弱点は共有しますが、カイリューはかえんほうしゃ（採用率66.7%）・りゅうせいぐん（採用率54.4%）で特殊方面を担い（物理技はしんそく採用率41.2%が中心）、マスカーニャの物理打点と役割が分かれています。

**カバルドン**（4位）はじめん単タイプで、あくびとステルスロックのサポート役です。あくびで相手に交代を強い、出てきた相手に対してマスカーニャの攻撃技を通しやすくします。

**ブリジュラス**（5位）ははがね/ドラゴンで、マスカーニャのどく弱点（×2）を無効（×0）でカバーします。ブリジュラスのラスターカノン・りゅうせいぐんが特殊方面の打点を担い、マスカーニャの物理打点と役割が分かれています。

---

## まとめ

M-5のマスカーニャは使用率4位で、M-4終盤（2026-08-04時点の3位）からほぼ横ばいです。順位は動いていない一方、こだわりスカーフ一辺倒だったM-4（2026-07-13時点）から型の分布が変わっています。

- **こだわりスカーフ採用率は70.9%→55.2%に低下し、きあいのタスキ（18.5%→28.7%）・ふいうち（18.5%→30.9%）が上昇**：特性はへんげんじざい/しんりょくの2択で合計100%のため、しんりょく採用率の上昇（7.0%→20.7%）は表裏一体の変化。タスキで耐えてしんりょくを発動させ、優先度技のふいうちで後続を打ち取る運用と整合的
- **スカーフ型（S実数値192・スカーフ込み288）は使用率1位のガブリアス（最速S169、スカーフ時253）を上から動かせるが、タスキ+しんりょく型（いじっぱりでS175）はより遅く、その代わりトリックフラワーの実質威力が105相当→157.5相当まで伸びる**：どちらを選ぶかで速さと火力のどちらを優先するかが分かれる
- **トリックフラワー96.9%・トリプルアクセル87.3%という主力攻撃技の採用率はM-4からほぼ横ばい**：変化しているのは持ち物・特性・技の組み合わせ方で、基本の攻撃範囲は継続

へんげんじざいで最初の技を必ず一致技化できる点と、こおり・むし技を絡めた広い打点範囲が武器ですが、フェアリー・どく複合には等倍止まりが多く、ミミッキュ・キラフロル・マフォクシーといった上位ポケモンには有効打を欠く場面があります。

---

*関連記事：[マスカーニャ考察 M-4](/blog/meowscarada-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/meowscarada/)**
