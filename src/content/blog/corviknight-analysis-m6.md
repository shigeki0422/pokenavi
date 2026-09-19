---
title: '【ポケモンチャンピオンズ】アーマーガア 考察 M-6 シーズン 使用率14位のゴツゴツメット受け'
description: 'M-6シーズン使用率14位のアーマーガアを考察。ひこう/はがねの複合タイプでじしん無効を活かしつつ、たべのこしからゴツゴツメットへ主力アイテムが入れ替わった実態や、てっぺき/ビルドアップ2型の火力・耐久差をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-corviknight-m6.png'
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
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" />
  <div>
    <h2 style="margin:0 0 8px">アーマーガア</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">14位</strong>（M-5: 13位）　特性: <strong>プレッシャー 67.5%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも2026-09-10時点のスナップショットを使用しています。

M-6シーズンのアーマーガアは使用率14位。ひこう/はがねの複合タイプでじめんタイプの技を無効化しつつ、高いBを軸にはねやすめ・とんぼがえりで居座る耐久型が主流です。主力アイテムがたべのこしからゴツゴツメットへ大きく入れ替わった点は後述のデータ分析で詳しく扱います。

---

## アーマーガアの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">98</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">53</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">495</span>
  </div>
</div>

H98・B105の物理耐久が高い水準にあります。C53は低くとくこう技はほぼ通らない一方、D85もあり特殊面も一定の耐久を持ちます。S67は環境上位の多くに先手を取られる数値で、耐えてから打ち返す立ち回りが基本になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお・でんきの2タイプ（いずれも×2）に絞られ、耐性は6タイプ・むし/くさへの4分の1軽減・どく/じめんの無効化と非常に広範です。じめん技（使用率上位ではガブリアスのじしん67.6%やカバルドンのじしん99.3%）を完全に無効化できる点が最大の強みで、でんき技（ライチュウのでんじほう96.5%等）とほのお技（ラウドボーンのフレアソング99.4%等）を持つ相手には注意が必要です。

### 特性

<strong>プレッシャー（67.5%）</strong>が最多採用です。相手が自分を対象にした技を使うたびPPを1多く消費させる特性で、はねやすめでの居座りと組み合わせて相手の技を先に枯らす持久戦を狙えます。もう一方の<strong>ミラーアーマー（32.0%）</strong>は、自分が受ける能力ダウン効果を相手にそのまま跳ね返す特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2回復。使用したターンはひこうタイプでなくなる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。むしタイプでタイプ一致補正は付かない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">54.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ダメージがAでなくBの実数値で決まる。高いBをそのまま打点に変換できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の防御を2段階上昇。ボディプレスの威力を底上げする積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ブレイブバード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">37.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう一致の高威力技。与えたダメージの1/3を自分も受ける反動あり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ビルドアップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃・防御を1段階ずつ上昇。ブレイブバードの火力と耐久を同時に強化</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致で20%の確率でひるませる。反動のないもう一つの一致技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のろい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分のSを1段階下げ、A・Bを1段階ずつ上げる。少数派の選択技</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：耐久型（てっぺき・ボディプレス）

**代表的な性格: わんぱく（全体の性格採用率65.2%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久型（てっぺき・ボディプレス）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> プレッシャー（67.5%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> ゴツゴツメット（56.8%）
</div>
<div>
<strong>技構成:</strong><br>
・はねやすめ<br>
・とんぼがえり<br>
・てっぺき<br>
・ボディプレス
</div>
</div>
</div>

てっぺき（B2段階上昇）でBを積んでから、B依存のボディプレス（かくとう・威力80）で打点に変える構成です。攻撃技はボディプレス1本に絞り、はねやすめとの回復ループで居座ります。

**強み:**

わんぱく・EV H32-B32-D2のB実数値は**172**。てっぺきを1回使うとB2段階上昇（×2.0）でB実数値**344**まで伸び、ボディプレスの打点も同じ倍率で上昇します。型2のビルドアップ後のB実数値258（後述）より+86高く、耐久面では型2を上回る水準に達します。

**弱み:**

てっぺきを使うターンは攻撃できないため、積みに1ターンを要します。ブレイブバードやビルドアップを持たないため、A方向の火力（一致ひこう技）は選択肢にありません。

---

### 型2：アタッカー型（ビルドアップ・ブレイブバード）

**代表的な性格: わんぱく（全体の性格採用率65.2%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アタッカー型（ビルドアップ・ブレイブバード）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> プレッシャー（67.5%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> ゴツゴツメット（56.8%）
</div>
<div>
<strong>技構成:</strong><br>
・はねやすめ<br>
・とんぼがえり<br>
・ビルドアップ<br>
・ブレイブバード
</div>
</div>
</div>

ビルドアップ（A・B各1段階上昇）でブレイブバード（ひこう一致・威力120）の火力を底上げしつつ耐久も引き上げる構成です。反動のないアイアンヘッド（はがね一致・威力80）に替える選択肢もあります。

**強み:**

わんぱく・EV H32-B32-D2のA実数値は無振りで**107**ですが、ビルドアップを1回使うとA1段階上昇（×1.5）でA実数値**160**に達し、型1にはない一致ひこう技の高火力を発揮できます。B実数値も1段階上昇（×1.5）で**258**まで伸びます。

**弱み:**

ブレイブバードは与えたダメージの1/3を自分も受ける反動があり、積みながら自分のHPも削れます。B実数値の伸びは型1のてっぺき後344に対し258（-86）にとどまり、耐久面では型1に劣ります。

---

## データ分析：M-5→M-6 採用データの変化

※M-5列のデータはM-5シーズン最終スナップショット（2026-09-09時点）、M-6列のデータは2026-09-10時点を使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>14位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">下降</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">56.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-28.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴツゴツメット採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新規首位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-23.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ビルドアップ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アイアンヘッド採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.9pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">98.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">99.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.1pp</td>
</tr>
</tbody>
</table>
</div>

最大の変化は主力アイテムの入れ替わりです。M-5はたべのこし（56.9%）が首位でオボンのみ（37.3%）が続く「継続回復＋一発耐え」の構成でしたが、M-6ではたべのこしが28.3%（-28.6pp）、オボンのみが13.7%（-23.6pp）へ大きく後退し、代わってM-5では圏外だったゴツゴツメット（56.8%）が新たに首位に立ちました。ゴツゴツメットは接触技を受けると相手に最大HPの1/6のダメージを与えるアイテムで、はねやすめによる回復ループと組み合わせることで、接触技を持つ物理アタッカーを繰り返し受けるほど相手の消耗を早める運用に変わったことを示しています。技構成自体（はねやすめ99.1%・とんぼがえり73.4%・ボディプレス54.3%・てっぺき51.3%）はM-5からほぼ変わらず、ビルドアップ（+5.4pp）とアイアンヘッド（-5.9pp）が入れ替わるように動いた程度で、技の骨格よりもアイテム選択の方に大きな変化が出たシーズンです。

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
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはアーマーガアが上だが、対アーマーガアで最も通るインファイト（採用率24.9%、等倍）が確定3発（ゴツゴツメット型基準。たべのこし/オボン型では確定4発）の一方、こちらのブレイブバード（採用率37.6%）は確定5発止まりで、削り負けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルトを持つ個体（採用率20.0%、でんき×2弱点）はふうせん高速型×ゴツゴツメット型基準で確定2発。こちらのブレイブバード（採用率37.6%）は決定打を欠き、押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラスの主力10まんボルト（採用率63.1%、でんき×2弱点）が確定3発。こちらのボディプレス（採用率54.3%）は決定打を欠き、押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">対アーマーガアで最も通るシャドーボール（採用率42.9%）がゴツゴツメット型基準で確定3発。こちらのブレイブバード（採用率37.6%）は決定打を欠き、押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガリザードンXで最も多いフレアドライブ（採用率36.5%、ほのお×2弱点）が確定2発。こちらのブレイブバード（採用率37.6%）は確定3発止まりで、先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガリザードンYで最も多いかえんほうしゃ（採用率42.9%、ほのお×2弱点）が確定1発。こちらのブレイブバード（採用率37.6%）は確定3発止まりで、初手で沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エースバーンの主力かえんボール（採用率98.7%、ほのお×2弱点）が確定2発。こちらのブレイブバード（採用率37.6%）は確定3発止まりで、先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウォッシュロトムの主力10まんボルト（採用率50.8%、でんき×2弱点）が確定2発。こちらのボディプレス（採用率54.3%）は確定4発止まりで、押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アーマーガアのS実数値87がラウドボーンの86をわずかに上回り先手を取れます（アーマーガアがのんき型〈24.0%〉の場合はS78で後手）。ラウドボーンの主力フレアソング（採用率99.4%、ほのお×2弱点）が確定2発で、こちらのブレイブバード（採用率37.6%）は確定5発止まりのため削り切れません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位（メタグロスナイト採用率98.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチを持つ個体（採用率31.4%、でんき×2弱点）は確定3発。こちらのボディプレス（採用率54.3%）は決定打を欠き、押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位（カイリュナイト採用率75.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガカイリューの主力かえんほうしゃ（採用率66.8%、ほのお×2弱点）が確定2発。こちらのブレイブバード（採用率37.6%）は確定4発止まりで、押し切られます</td>
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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガボーマンダの主力すてみタックル（採用率73.4%）は確定5発止まり。こちらのブレイブバード（採用率37.6%）が確定4発で先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミッキュの主力シャドークロー（採用率59.2%）は確定5発止まり。こちらのブレイブバード（採用率37.6%）が確定3発で先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャの主力トリプルアクセル（採用率90.1%）は確定3発止まり。こちらのブレイブバード（採用率37.6%）が確定2発で先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴリランダーの主力はたきおとす（採用率66.5%）は決定打を欠きます。こちらのブレイブバード（採用率37.6%）が確定3発で先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">キラフロルの主力パワージェム（採用率80.8%）は確定3発止まり。こちらのアイアンヘッド（採用率22.9%）が確定2発で先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガの主力れいとうビーム（採用率92.9%）は確定3発止まり。こちらのボディプレス（採用率54.3%）が確定2発で先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アローラキュウコンの主力ふぶき（採用率69.1%）は確定3発止まり。こちらのアイアンヘッド（採用率22.9%）が確定2発で先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オオニューラの主力インファイト（採用率99.4%）は確定3発止まり。こちらのブレイブバード（採用率37.6%）が確定1発で先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でアーマーガアと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
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
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" loading="lazy">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、弱点のドラゴン・フェアリー技をアーマーガアが耐性（×0.5）で受けられます。逆にアーマーガアの弱点であるでんき技はガブリアスがじめんタイプで無効化できるため、でんき・ドラゴン・フェアリーを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**アシレーヌ**（2位）はみず/フェアリーで、弱点のどく・くさ技をアーマーガアが無効化・4分の1軽減で受けられます。逆にアーマーガアの弱点であるほのお技はアシレーヌが耐性（×0.5）で受けられるため、どく・くさ・ほのおを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**ボーマンダ**（3位）はドラゴン/ひこうで、弱点のドラゴン・フェアリー技をアーマーガアが耐性（×0.5）で受けられます。逆にアーマーガアの弱点であるほのお技はボーマンダが耐性（×0.5）で受けられるため、ほのお・ドラゴン・フェアリーを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**グソクムシャ**（4位）はむし/みずで、弱点のひこう技をアーマーガアが耐性（×0.5）で受けられます。

---

## まとめ

M-6のアーマーガアは使用率13位から14位へ小幅に後退しましたが、技構成の骨格（はねやすめ・とんぼがえり・ボディプレス・てっぺき）はM-5からほぼ変わらず、主力アイテムの入れ替わりが最大の変化点となったシーズンです。

- **使用率13位→14位**：わずかな後退にとどまり、技構成自体は継続しています
- **たべのこし-28.6pp・ゴツゴツメット圏外→56.8%**：継続回復から接触技への反撃へ、耐久運用の方向性が大きく変わりました
- **ビルドアップ+5.4pp・アイアンヘッド-5.9pp**：攻撃面はブレイブバード軸の型がやや優勢になっています

弱点がほのお・でんきの2タイプに絞られ、じめん技を無効化できる高い耐性を土台に、てっぺきでBを積んでボディプレスで押すか、ビルドアップでブレイブバードの火力を伸ばすかは、パーティ内での役割に応じた選択になります。ほのお・でんき技を持つ相手には選出段階でのケアが求められます。

---
