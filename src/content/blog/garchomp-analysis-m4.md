---
title: '【ポケモンチャンピオンズ】ガブリアス考察 M-4 スケイルショット台頭・げきりん減・がんせきふうじ新定着の変化点を解説'
description: 'M-4シングルバトルで使用率1位継続のガブリアスを分析。スケイルショット30.5%→39.9%（+9.4pp）・げきりん45.5%→34.8%（-10.7pp）の入れ替え、がんせきふうじM-3圏外→30.0%の新定着、いじっぱり+4.9ppの背景を採用率データで解説。型別実数値・苦手な相手・パーティ構成まで紹介。'
pubDate: '2026-07-16'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-garchomp-m4.png'
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
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
  <div>
    <h2 style="margin:0 0 8px">ガブリアス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">1位</strong>（M-3から連続）　特性: <strong>さめはだ 99.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事はM-4シーズンのデータです。M-3版は[ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)をご覧ください。

シーズンM-4でも、ガブリアスは使用率1位を維持しています。ドラゴン/じめん複合と種族値合計600の高いステータスを持ち、一致技じしん（威力100・命中100）とS169（スカーフ時S253）の速度を武器にする、チャンピオンズを代表するアタッカーです。M-3からの主な変化はスケイルショット・げきりんの技入れ替えやがんせきふうじの新定着で、詳細は後述のデータ分析で解説します。

---

## ガブリアスの基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">108</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">102</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

こおり×4が最大の弱点です。M-4の使用率圏内ではアローラキュウコン（16位、フリーズドライ84.4%・ふぶき71.5%）とゲッコウガ（15位、れいとうビーム87.2%）が主なこおり脅威です。フェアリー×2ではミミッキュ（2位、じゃれつく98.2%）・アシレーヌ（7位、ムーンフォース98.0%）が該当します。

---

## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>さめはだ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.4%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すながくれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.6%</td>
</tr>
</tbody>
</table>
</div>

**さめはだ**は接触技を受けたとき、攻撃してきた相手のHPを最大HPの1/8削る特性です。こうげき130の高火力に加えて接触技を受けるたびに相手を1/8削る効果があり、物理アタッカーのダメージレースに影響します。採用率は99.4%で実質固定です。

---

## 主な型

### 型1：きあいのタスキ型（39.2%）

**性格採用率: ようき / いじっぱり（タスキ型内で二分）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキ型（ようき / 設置+スケイルショット）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.4%）<br>
<strong>性格:</strong> ようき（すばやさ↑ とくこう↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ステルスロック（まきびし）<br>
・スケイルショット<br>
・がんせきふうじ（ドラゴンテール）
</div>
</div>
</div>

タスキ込みで最低でも2ターン確保できる立ち位置から、設置技＋スケイルショットで動く構成。スケイルショットは使用後の混乱が発生しないため、げきりんより後続の行動を縛られにくいのが利点です。

**強み:**

H185 / A182 / B115 / D105 / S169。S169で多くの環境ポケモンに先手を確保できます。

**弱み:**

ゲッコウガ（実数値191）・マスカーニャ（実数値192）はようき型でも後手になります。

---

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキ型（いじっぱり / つるぎのまい）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.4%）<br>
<strong>性格:</strong> いじっぱり（こうげき↑ とくこう↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ（ラムのみ）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・つるぎのまい<br>
・スケイルショット<br>
・ステルスロック
</div>
</div>
</div>

タスキで1発保証しつつつるぎのまいを積む狙いの構成です。

**強み:**

H185 / A200 / B115 / D105 / S154。つるぎのまい1積み後のこうげきは実質A400相当となり、ようき型（A182）の2倍を超える打点に達します。

**弱み:**

S154はようき型（S169）と比べてS155〜169の速度帯のポケモンに先手を取れません。ゲッコウガ実数値191・マスカーニャ実数値192はようき型でも後手になるため、いじっぱり型では当然先手を取られます。

---

### 型2：こだわりスカーフ型（19.8%）

技が1種固定になるため設置技や積み技と組み合わせできない一方、S169にスカーフ補正（×1.5）がかかりS253となり、環境で最も多い速度帯を上回ります。

**性格採用率: ようき**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフ型（ようき・最速アタッカー）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.4%）<br>
<strong>性格:</strong> ようき（すばやさ↑ とくこう↓）<br>
<strong>EV:</strong> A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・スケイルショット<br>
・げきりん<br>
・がんせきふうじ
</div>
</div>
</div>

じしんを固定して先手で削る動きが主軸です。

**強み:**

H183 / A182 / S169（スカーフ補正後 S253）。環境で最も多い速度帯を上回る最速アタッカーです。

**弱み:**

技が1種固定になるため設置技や積み技と組み合わせできません。ミラー戦では相手もスカーフ持ちの可能性があり、相手がスカーフガブリアスだった場合はスカーフなしのこちらが先手を取られます。

---

### 型3：わんぱく型（18.2%）

**性格採用率: わんぱく 18.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わんぱく型（H32-B32 / ステロ設置）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.4%）<br>
<strong>性格:</strong> わんぱく（ぼうぎょ↑ とくこう↓）<br>
<strong>EV:</strong> H32-B32-S2<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ステルスロック<br>
・まきびし<br>
・ドラゴンテール
</div>
</div>
</div>

H215・B161の耐久ラインでステルスロック・まきびしのダブル設置を狙う型。ドラゴンテールで相手を強制交代させながら設置ダメージを蓄積する動きが主軸です。

**強み:**

H215 / A150 / B161 / D105 / S124。こおり×4弱点技でもオボンのHPを活かして2発耐えやすくなります。

**弱み:**

A150（ようき型A182から32減）と火力は劣ります。

---

## データ分析①：M-3→M-4 採用率変化

### 技採用率（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">99.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>99.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">±0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">48.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">39.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+9.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>29.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>28.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まきびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>18.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+1.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>34.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-10.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">30.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新定着</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくづき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>14.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">新登場</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.0pp</td>
</tr>
</tbody>
</table>
</div>

最大の変化は**スケイルショット（+9.4pp）とげきりん（-10.7pp）の入れ替え**です。スケイルショットは威力25×2〜5回のドラゴン連続技で、最後にS+1・B-1の効果がつきます。げきりん（威力120）との比較では単発の最高打点は劣りますが、使用後の混乱が発生しない点が評価されています。

**つるぎのまい（+6.2pp）**の上昇はいじっぱり性格の増加と連動しており、「積んで上から一撃で仕留める」構成への志向が強まっています。

### 持ち物採用率（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいのタスキ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">39.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>23.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こだわりスカーフ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>19.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラムのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#16a34a">8.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いのちのたま</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.4pp</td>
</tr>
</tbody>
</table>
</div>

こだわりスカーフが-3.7ppと減少しています。スカーフは技が1種に固定されるため、ステルスロック・まきびしなどの設置技と共存できず、つるぎのまいとも相性が悪い点が背景にあります。**ラムのみ+4.3pp**はつるぎのまい型でおにび（やけど）・まひ・ねむり等の状態異常を受けても積み技を使える点が評価されていると見られます。

### 性格分布（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ようき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">57.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.9pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>いじっぱり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>28.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.9pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき↑ とくこう↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わんぱく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>18.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.0pp</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
</tbody>
</table>
</div>

ようきが過半数を割り込み（57.1%→50.2%）、いじっぱりが28.0%まで拡大しました。いじっぱり採用時のこうげき実数値は200（ようき時182）と18の差があり、つるぎのまいを1積みした後の打点差は実質2倍近くに広がります。一方でS実数値はようき169に対しいじっぱり154と15下がるため、先手の有無が変わる相手がいる点は前述の型カードのとおりです。

### EV分布（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H2-A32-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り+HP最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H0-A32-B2-S32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>9.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさ全振り+ぼうぎょ微調整</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B32-S2（わんぱく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ全振り（ステロ型）</td>
</tr>
</tbody>
</table>
</div>

最多EV配分**H2-A32-S32（49.9%）**が引き続き主流ですが、M-4で新たに**H0-A32-B2-S32（9.1%）**が台頭しています。BのEV差は2ポイントで実数値2の差（B115→B117）にとどまりますが、特定の物理打点の確定数を変える調整として一定数採用されています。

---

## データ分析②：スケイルショット増・げきりん減・がんせきふうじ新定着の読み方

M-4で最も注目される技変動は①スケイルショット+9.4pp、②げきりん-10.7pp、③がんせきふうじM-3圏外→30.0%新定着の3点です。

**スケイルショット（+9.4pp）とげきりん（-10.7pp）の入れ替え**：げきりん（威力120）は単発の最高打点ですが、使用後に混乱が確定するため後続の動きを縛ります。スケイルショット（威力25×2〜5回）は最後にS+1・B-1が付くため、スケイルショット後にS上昇が残り、混乱による自傷リスクもありません（なお両技ともドラゴン技のため、ゴースト/フェアリー複合のミミッキュには無効で、対ミミッキュ性能は入れ替えの理由になりません）。

**がんせきふうじの新定着（圏外→30.0%）**：がんせきふうじ（いわ・威力60・命中95・S-1効果）はM-3では採用17.2%未満で圏外でしたが、M-4で30.0%まで上昇しました。ガブリアスのじしんがひこうタイプに無効なため、相手のひこうタイプへの打点として、またこおり×4弱点を突いてくるアローラキュウコン（こおり/フェアリー、いわ×2）への補助打点として、がんせきふうじが評価されていると考えられます（同じくこおり×4弱点を突いてくるゲッコウガ＝みず/あくには、いわ技は等倍止まりで打点にはなりません）。また4枠目の選択肢はどくづき（14.0%・フェアリー対策）とがんせきふうじ（30.0%・ひこう/アローラキュウコン対策）の両方が採用されており、どちらを優先するかで打点の使い分けが分かれています。

**どくづきの位置づけ**：どくづき（どく・威力80）はM-4で14.0%と圏内に新登場した技です。みず/フェアリーのアシレーヌには×2で通りますが、ゴースト/フェアリー複合のミミッキュには等倍止まりで、フェアリー全般に有効な打点ではありません。対戦相手のアシレーヌを直接狙うどく打点として少数派ながら維持されています。

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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（98.2%）でフェアリー×2。こちらのじしんは等倍止まりのうえ、ばけのかわで初弾を無効化されるため2発の確保が必要な場面が多い（ドラゴン技はゴースト/フェアリー複合のミミッキュに無効で打点にならない）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（98.0%）でフェアリー×2。特殊技のためさめはだ効果なし。こちらのじしんはアシレーヌ（みず/フェアリー）に等倍止まりで確定数が伸びず、どくづきも14.0%にとどまるM-4では打点が限られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ（84.4%）・ふぶき（71.5%）がこおり×4。タスキなし個体は先手のこおり技で即倒する。タスキ持ちでも1ターンしか保証されない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（87.2%）でこおり×4。ゲッコウガの実数値は191（おくびょうEV32）で、ようきガブリアス169・いじっぱりガブリアス154のいずれに対しても先手を取る。スカーフなしでは型を問わず後手になる</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でガブリアスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
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
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" loading="lazy">
    <div class="name">アローラキュウコン</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

M-3からの変化として注目されるのは**アシレーヌがM-3圏外から2位へ新登場**、**マスカーニャが2位→4位に低下**という点です。メタグロスは3位→3位で変化なし。M-3上位だった**ライチュウ（7位）・アーマーガア（8位）・ムクホーク（9位）が圏外へ**去り、代わって**ギャラドス・マフォクシーが新たに6・7位へ**入りました。アローラキュウコン（5位→10位）・リザードン（6位→8位）は順位を落としつつも10位圏内を維持しています。

**ミミッキュ（1位）**はゴースト/フェアリーで、フェアリー技を半減・ドラゴン技を無効化して受けられます。ガブリアスが弱点を突かれやすいドラゴンタイプの相手には、じゃれつくで×2の打点も持ちます。一方でミミッキュ自身が苦手なはがねタイプは、ガブリアスのじしんが処理する役割分担です。

**アシレーヌ（2位）**はみず/フェアリーで、ガブリアスの弱点であるドラゴン技をタイプ相性で無効化でき、ムーンフォースでフェアリータイプの相手に打点を持ちます。アシレーヌが苦手などくタイプの相手（キラフロル等）は、ガブリアスのじしんが処理する役割分担です。

**メタグロス（3位）**ははがね/エスパーで、ガブリアスのこおり×4弱点を突くアローラキュウコンにバレットパンチ（はがね×4）が通ります。メタグロスの一致技（サイコファング・バレットパンチ）とガブリアスのじしん・ドラゴン技は打点の重なりが少なく、パーティ全体の攻撃範囲を補い合えます。

**ブリジュラス（5位）**ははがね/ドラゴンです。攻撃面では、ガブリアスのじしんが相手のはがねタイプ全般に×2で通るため、ブリジュラス自身のはがね技と合わせて対はがね打点を重ねられます（なお、ガブリアスの弱点であるこおり・ドラゴン・フェアリーはいずれもブリジュラスにとっても等倍で、ブリジュラスが苦手なじめん技もガブリアス自身が等倍で受けるため、互いの弱点を守り合う関係ではありません）。

---

## まとめ

M-4のガブリアスは使用率1位を維持しながら、以下の3点で技・型の構成が変化したシーズンです。

- **スケイルショット（+9.4pp）↔ げきりん（-10.7pp）**：使用後の混乱リスクをなくす技入れ替え
- **いじっぱり（+4.9pp）+ つるぎのまい（+6.2pp）**：A200の火力を積みで増幅させる「一撃狙い」構成への志向強化
- **がんせきふうじ（圏外→30.0%新定着）+ どくづき（圏外→14.0%新登場）**：じめん無効のひこう対策としてがんせきふうじが3割台に定着、どくづきはフェアリー直打点として少数採用

じしん99.5%の一致技とようきS169（スカーフ時S253）の速度は不変で、環境中心であり続ける基本性能は変わっていません。こおり×4・フェアリー×2の弱点に対して、パーティ全体でカバーを用意するか、タスキで1ターン保証する構成を選ぶかが採用時の主な検討事項です。

---

*関連記事：[ガブリアス考察 M-3](/blog/garchomp-analysis-m3/) / [メタグロス考察 M-4](/blog/metagross-analysis-m4/)*
</content>
