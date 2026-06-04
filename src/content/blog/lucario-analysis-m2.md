---
title: '【ポケモンチャンピオンズ】メガルカリオ考察 M-2 使用率9位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率9位のメガルカリオを徹底分析。てきおうりょくによるインファイト実質威力240の破壊力、AS物理型・CS特殊型の構築を解説。環境上位ポケモンへのダメージ計算、パーティ構成まで実データで紹介します。'
pubDate: '2026-05-22'
draft: true
heroImage: '../../assets/hero-lucario-m2.png'
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
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" />
  <div>
    <h2 style="margin:0 0 8px">メガルカリオ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">9位</strong>　メガ石採用率: <strong>ルカリオナイト 97.7%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ルカリオは**使用率9位**を記録。そのうち**97.7%がルカリオナイトを採用**しており、実質ほぼ全ての対戦でメガ進化を前提とした構成になっています。

メガルカリオの最大の特徴は特性**てきおうりょく**。タイプ一致補正が通常の×1.5から**×2.0**に跳ね上がるため、インファイト（威力120）は実質威力240・コメットパンチ（威力90）は実質威力180という高い火力を誇ります。かくとう/はがねという優秀な複合タイプと合わせ、環境最強クラスのアタッカーです。

---

## なぜ今メガルカリオが強いのか

### 1. てきおうりょく+インファイトで環境ポケモンを一撃圏内に

メガルカリオの最大の強みは**特性てきおうりょく**によるタイプ一致補正×2.0です。インファイトの基礎威力120にタイプ一致補正×2.0が乗り、実質威力**240**に達します。通常アタッカーのタイプ一致補正×1.5で威力180相当なのに対し、その1.3倍の火力です。

はがね/ドラゴンのブリジュラス（使用率2位）にはインファイトが×2（はがね2×ドラゴン1）で刺さり、つるぎのまい後なら確定1発も狙えます。弱点を突けない相手でも、てきおうりょく補正の高火力により等倍インファイトで大きく削れるのが強みです。

### 2. S112で主要アタッカーを先手で処理できる

メガ進化後のすばやさは**112**。これはM-2環境の主要ポケモンを大きく上回る数値です。

- ガブリアス（S102）→ メガルカリオが先手
- リザードン（S100）→ メガルカリオが先手
- マスカーニャ（S123）→ ようき最速なら負ける
- ブリジュラス（S84）→ メガルカリオが先手
- アーマーガア（S98）→ メガルカリオが先手
- ハッサム（S65）→ メガルカリオが先手

ようき最速（S112実数値）で動けるため、ほぼ全ての無振りポケモンを先手で処理できます。スカーフガブリアス（S152相当）には負けますが、それ以外の環境ポケモンに対してはほぼ先手が保証されます。

### 3. 先制技でタスキ・低HP処理（相手のSに関わらず先制）

はがねタイプの先制技**バレットパンチ**（採用率48.0%）をてきおうりょくで強化できるのも大きなポイントです。先制技は優先度+1で動くため、**相手のすばやさに関わらず先制**できます（前項のS112とは別系統）。通常のバレットパンチは威力40ですが、タイプ一致補正×2.0で実質威力80相当になります。

これにより以下の処理が安定します：
- きあいのタスキ持ちをHP1から確定1発
- こだわりスカーフで先手を取られた後の処理
- 積み技（つるぎのまい）後に弱点技で倒されそうな場合の保険

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:72.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">145</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">88</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">112</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">625</span>
  </div>
</div>

こうげき145・とくこう140という両刀攻撃力は環境トップクラス。HPとDが70と低めで物理・特殊ともに耐久は不足しているため、**先手で攻撃するか先制技で処理する**という攻撃的な立ち回りが基本になります。

### メガ前→メガ後ステータス変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">145</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+35</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">88</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+18</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">115</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+25</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">112</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+22</td>
</tr>
</tbody>
</table>
</div>

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
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
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

はがねタイプがどくを無効化し、さらに9タイプへの耐性を持つのが特徴です。フェアリー・ドラゴン半減は環境的に重要で、ガブリアスのげきりんを半減で受けられます。弱点はほのお・じめん・かくとう・エスパーの4タイプ。特にガブリアス（使用率1位）のじしんと、リザードン（5位）のほのお技は天敵となります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120（実質240）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">71.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">てきおうりょくのタイプ一致補正×2.0。使用後BとD1段階ダウン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>コメットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90（実質180）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中率90。フェアリー・いわ・こおりに刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40（実質80）先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>48.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手のSに関わらず先制。タスキ処理・スカーフ持ち対処に</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>39.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A2段階アップ。AS型の必須技。1積みで全抜き圏が大幅拡大</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんくうは</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40（実質80）先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう先制技。優先度+1。CS特殊型でも採用可能</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はどうだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80（実質160）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊かくとう技。CS型のメインウェポン。インファイトのB・Dダウンなし</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・はがね・どく等への打点。リザードンのメガ前・カビゴンへの対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんそく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。ノーマルタイプ先制技。タスキ処理の保険として採用</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80（実質160）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊はがね技。CS型でフェアリー・いわ・こおりへの安定打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっていこうせん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120（実質240）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C2段階ダウン。CS型で使い切り技として採用。インファイトと合わせて超火力</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1: つるぎのまい物理AS型（最多採用）

**採用率: AS系 66.3% / ようき 66.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまいASようき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ようき（A↑ S↓は使わない）<br>
<strong>EV:</strong> A32 S32（AS振り、最多型はH+2振り）<br>
<strong>持ち物:</strong> ルカリオナイト
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・インファイト<br>
・コメットパンチ / バレットパンチ<br>
・バレットパンチ / じしん / しんそく
</div>
</div>
</div>

**強み:**

S112最速を活かし、ほぼ全ての無振りポケモンより先手を取ります。つるぎのまいを1積みすればAが2段階上がり、てきおうりょくインファイトの火力がさらに伸びます。1積み後はブリジュラス・アシレーヌ・マスカーニャといった環境上位の多くを**確定1発**圏内に収められます。

コメットパンチ（命中率90）はフェアリー・いわ・こおりへの打点として機能し、フェアリータイプのフラエッテ(永遠)への確定1発圏が確保できます。

バレットパンチは先制技として4枠目に採用するケースが多く、スカーフ持ち・タスキ持ちの処理に使います。じしんはリザードン（メガ前）・カビゴン等への打点として選択肢になります。

**弱み:**

CS特殊型と比べ、初手から特殊耐久の高い相手に打点を選びにくく、つるぎのまいの積みターンを通す必要があります。積みを狙うターンに弱点（ほのお・じめん・エスパー）を突かれると一気に崩されます。

また、ガブリアスのじしんは2倍弱点で、スカーフガブリアスには先手を取られます。ガブリアスが多い環境では出し負けリスクがある点を把握して動きましょう。

---

### 型2: CS特殊型（2番目に多い構成）

**採用率: CS系 23.2% / おくびょう 18.9%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CS両刀おくびょう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り、最多型はH+2振り）<br>
<strong>持ち物:</strong> ルカリオナイト
</div>
<div>
<strong>技構成:</strong><br>
・はどうだん<br>
・ラスターカノン / てっていこうせん<br>
・しんくうは<br>
・じしん / バレットパンチ
</div>
</div>
</div>

**強み:**

おくびょうCSでとくこう140を最大活用する型です。はどうだんはインファイトと違いBとDダウンのデメリットがなく、安定したダメージを与え続けられます。てきおうりょくのタイプ一致補正×2.0で実質威力160になります。

ラスターカノンはフェアリー（アシレーヌ・フラエッテ永遠）に対して特殊はがね打点として機能します。てっていこうせんは実質威力240の超火力技ですが、使用後Cが2段階下がるため使い切り前提になります。

しんくうはは特殊型でも採用できるかくとう先制技で、タスキ持ち処理に使えます。

**物理型との使い分け:**

物理型に読みを入れてB方向に厚いポケモンを採用してくる相手に対して特殊型は刺さります。ブリジュラス等のB特化には特殊技の方がダメージが通りやすいケースもあります。一方、先制技をバレットパンチ（物理）かしんくうは（特殊）かで選択できる点が両型の使い分けポイントです。

**弱み:**

A145を生かしきれないため、物理型と比べると積み技による爆発力が低下します。おくびょうによってAが下がっているため、コメットパンチやバレットパンチの火力も大きく落ちます。

---

### 型3: AS+ぼうぎょ補強型（採用率3.6%）

AS型のうちEVの一部をBに割く派生型で、採用率は3.6%。Aを削る代わりにつるぎのまい積み中の物理被ダメを抑え、ガブリアスのじしん・げきりんに対して積み行動を通しやすくする狙いです。対ガブリアス意識の少数派構成として一定数見られます。

---

## 環境ポケモンへの相性分析

### 有利なポケモン

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
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト×2弱点。S84で先手確保。確定1発圏内</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S100でメガルカリオS112が先手。コメットパンチ等で処理。ただしほのお技には要注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123で先手を取られる。ただし倒されたとしても突破コストを残せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトは等倍（はがね2×ひこう0.5）だがA145の高火力＋S98より先手。コメットパンチも通る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">コメットパンチ・ラスターカノンでフェアリー半減なし（みず/フェアリー）。先手確保でCS型でも処理可</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトは等倍（むし0.5×はがね2）だがA145＋S65より先手で押し切れる。バレットパンチには注意</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが弱点×2。スカーフ型はS152で先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">対面は避け、パーティ構成でカバー。ひこう・ふゆうのポケモンでじしんを透かす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/エスパーでエスパー技が弱点×2。S115で先手を取られ、サイコキネシスで上から落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ等の先制技で削るか、はがね・あくタイプをパーティに入れて受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/ほのおにインファイト×0.25・コメットパンチ×0.5と打点が乏しく、ほのお技はメガルカリオに×2弱点。S100でほぼ同速</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（×2、ほのお）で弱点を突くか、みず・いわタイプをパーティに入れて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ひこうにかくとう・はがね打点とも等倍止まりで弱点を突けず、高いA・耐久で殴り合いに不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガルカリオ単体では受からない。でんき・いわ技を持つポケモン（弱点×2）をパーティで合わせる</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">環境1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">エスパー・ほのお対策として補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">環境7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">砂嵐+ステロでダメージ蓄積サポート</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-00.webp" alt="ロトム">
    <div class="name">ロトム系</div>
    <div class="rate">電気/炎対策</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ガブリアスのじしんをひこうで無効化</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">環境4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお対策。みずタイプでメガルカリオの弱点補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0663-00.webp" alt="ファイアロー">
    <div class="name">ファイアロー</div>
    <div class="rate">先制技役</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">かくとう弱点の処理。ブレイブバードで格闘対策</div>
  </div>
</div>

**パーティ構成の基本方針:**

ルカリオナイトを持たせるため、パーティに他のメガ進化ポケモンを入れることができません。そのため残り5体で以下の役割を補います。

1. **ガブリアス対策**: カバルドンやみず・こおりタイプでガブリアスのじしんを受ける枠
2. **ほのお対策**: みずタイプ（アシレーヌ等）でほのお攻撃を受ける枠
3. **エスパー対策**: あく・はがねタイプでエスパー技を受ける枠
4. **ステルスロック展開**: カバルドン等でステロを撒き、交換読みダメージを蓄積

---

## データ分析①：てきおうりょく補正が生む実質威力の差

メガルカリオの特性「てきおうりょく」はタイプ一致補正を通常の1.5倍から2.0倍に引き上げます。この差が具体的な威力数値でどれだけ影響するかを確認します。

| 技 | 基本威力 | 通常タイプ一致（×1.5） | てきおうりょく（×2.0） | 倍率差 |
|---|---|---|---|---|
| インファイト | 120 | 180 | **240** | +33% |
| コメットパンチ | 90 | 135 | **180** | +33% |
| バレットパンチ | 40 | 60 | **80** | +33% |
| しんそく（参考・一致なし） | 80 | — | 80 | — |

インファイトの実質威力240は、通常アタッカーのタイプ一致補正×1.5で180相当に対し1.3倍。採用率71.5%のインファイトがこれだけの実質威力を持つことで、メガルカリオは「インファイトの通りが良いパーティ」に対して圧倒的なパワーを発揮します。

バレットパンチ（48.0%採用）も実質威力80となり、先制技としては破格の数値です。「先制技の割に痛い」という評価はこの補正によるものです。てきおうりょくの恩恵は、採用率上位3技の全てに均等に乗るため、**メガルカリオの全体的な打点が底上げされている**のが実態です。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">つるぎのまいAS物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">66.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・インファイト・コメットパンチ・バレットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の爆発力最大。先制技で詰め対応</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積みターンが必要。ガブじしん読みが必須</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CS特殊型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">はどうだん・ラスターカノン・しんくうは・じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B・Dダウンなし。物理型への読み外し</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み爆発力が低下。A145を生かせない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">AS+B補強型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・インファイト・コメットパンチ・バレットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み中の被ダメ軽減。対ガブリアス意識</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A火力がAS型より低下</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガルカリオはてきおうりょくによる高火力と、S112による先手を両立した環境上位のアタッカーです。ルカリオナイトを採用するため他のメガ進化との共存はできませんが、高い火力と先制技により単体で完結した強さがあります。

M-2環境では使用率2位のブリジュラス（はがね/ドラゴン）にインファイトが×2で刺さるほか、アーマーガア・ハッサムなどはがね複合にも等倍以上で打点を持ち、はがね打点も含めた攻撃範囲の広さから9位という高い使用率を維持しています。

弱点のガブリアス（1位）はパーティ構成でケアしつつ、ブリジュラスや各種はがねタイプに積極的に攻撃を仕掛けていくのが基本戦術となります。つるぎのまい1積みを通す機会を作れるかどうかが勝敗を分ける重要なポイントです。
