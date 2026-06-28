---
title: '【ポケモンチャンピオンズ】メガルカリオ考察 M-2 使用率9位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率9位のメガルカリオを徹底分析。てきおうりょくによるインファイト実質威力240の破壊力、AS物理型・CS特殊型の構築を解説。環境上位ポケモンへのダメージ計算、パーティ構成まで実データで紹介します。'
updatedDate: '2026-06-04'
pubDate: '2026-06-04'
draft: false
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
      使用率: <strong style="color:#e67e22">9位</strong>　メガ石採用率: <strong>ルカリオナイト 97.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ルカリオは**使用率9位**を記録。そのうち**97.4%がルカリオナイトを採用**しており、実質ほぼ全ての対戦でメガ進化を前提とした構成になっています。

メガルカリオの最大の特徴は特性**てきおうりょく**。タイプ一致補正が通常の×1.5から**×2.0**に跳ね上がるため、インファイト（威力120）は実質威力240・コメットパンチ（威力90）は実質威力180という高い火力を誇ります。かくとう/はがねという優秀な複合タイプと合わせ、トップクラスの瞬間火力を持つアタッカーです。

---

## なぜ今メガルカリオが強いのか

### 1. てきおうりょく+インファイトで環境ポケモンを一撃圏内に

メガルカリオの最大の強みは**特性てきおうりょく**によるタイプ一致補正×2.0です。インファイトの基礎威力120にタイプ一致補正×2.0が乗り、実質威力**240**に達します。通常アタッカーのタイプ一致補正×1.5で威力180相当なのに対し、その1.3倍の火力です。

はがね/ドラゴンのブリジュラス（使用率2位）にはインファイトが×2（はがね2×ドラゴン1）で刺さり、つるぎのまい後なら確定1発も狙えます。

### 2. S112で環境上位の中速アタッカーに先手を取れる

メガ進化後のすばやさ種族値は**112**。ようき＋すばやさ最大振りですばやさ180になり、使用率上位を占める中速アタッカーに対し、相手も最速の場合でも先手を取れます。

- ガブリアス（S102・使用率1位）
- ブリジュラス（S85・2位）
- アーマーガア（S67・6位）
- ハッサム（S65・14位）

これらにはインファイトが等倍以上で通り、高火力を上から押し付けやすいのが強みです。なお、リザードン（S100・5位）も素早さでは上回りますが、相手のほのお技がメガルカリオに×2で刺さりこちらの打点は半減のため、先手を取っても不利です（後述の「苦手なポケモン」で扱います）。

ただし112を上回る高速勢には先手を取られます。メガゲッコウガ（みず/あく）・マスカーニャ（くさ/あく）はいずれもインファイトが×2（あく2）で1発圏内のため、ステルスロックや先発の攻撃でHPを削っておき、バレットパンチ（実質80）・しんそくの先制技で詰めれば先に倒せます。明確に不利なのは、**上から弱点を突けるメガマフォクシー（ほのお）・メガミミロップ（かくとう）**や、上から高速で撃ち合えるメガスターミーで、これらは後述の「苦手なポケモン」で扱います。

### 3. 先制技でタスキ・低HP処理（相手のSに関わらず先制）

はがねタイプの先制技**バレットパンチ**（採用率48.0%）をてきおうりょくで強化できるのも大きなポイントです。先制技は優先度+1で動くため、**相手のすばやさに関わらず先制**できます（前項のS112とは別系統）。通常のバレットパンチは威力40ですが、タイプ一致補正×2.0で実質威力80相当になります。

これにより以下の処理が安定します：
- きあいのタスキでHP1まで耐えた相手を確定1発
- メガゲッコウガやスカーフ持ちなど、すばやさで上回られる相手でも、瀕死圏まで削れていれば先制技で先に倒せる
- 弱点技で落とされる前に、相手を先制技で倒しきれる場面での詰め

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

はがねタイプがどくを無効化し、さらに9タイプへの耐性を持つのが特徴です。フェアリー技・ドラゴン技を半減できる点は環境的に重要です。ただし、環境のドラゴン・フェアリータイプ（ガブリアス・カイリュー・リザードン等）はじしんやほのお技などルカリオの弱点を突く技を併せ持つことが多く、タイプ耐性があっても受け出しできるわけではありません。弱点はほのお・じめん・かくとうの3タイプで、いずれも×2で通ります（エスパーはかくとう×2×はがね½で等倍に収まります）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊かくとう技。CS型のメインウェポン。反動・能力ダウンがなく毎ターン安定して撃てる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どく・でんき等への打点。カビゴンへの対策</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C2段階ダウン。CS型で使い切りの最大火力技。てきおうりょく補正で実質威力240</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

型①・型②の採用率は性格分布（ようき／おくびょう）を指標としています。

### 型1: つるぎのまい物理AS型（最多採用）

**性格採用率: ようき 66.6%**（AS物理型の指標。性格分布のうちようきが66.6%で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまいASようき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（84.0%）※メガ後てきおうりょく<br>
<strong>性格:</strong> ようき（A↑ S↓は使わない）<br>
<strong>EV:</strong> A32 S32（AS振り。余り2はHかBに振る）<br>
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

バレットパンチは先制技として4枠目に採用するケースが多く、スカーフ持ち・タスキ持ちの処理に使います。じしんはカビゴン等への打点として選択肢になります。

**弱み:**

CS特殊型と比べ、初手から特殊耐久の高い相手に打点を選びにくく、つるぎのまいの積みターンを通す必要があります。積みを狙うターンに弱点（ほのお・じめん・かくとう）を突かれると一気に崩されます。

また、ガブリアスのじしんは2倍弱点で、スカーフガブリアスには先手を取られます。ガブリアスが多い環境では、初手にルカリオを置かずじしんを無効化できるひこうタイプ（アーマーガア等）から入り、ガブリアスを処理または引かせてからルカリオを後投げで通すと安全です。

---

### 型2: CS特殊型（2番目に多い構成）

**性格採用率: おくびょう 18.9%**（CS特殊型の指標。性格分布でようきに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">CS両刀おくびょう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（84.0%）※メガ後てきおうりょく<br>
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

おくびょうCSでとくこう140を最大活用する型です。はどうだんは反動や能力ダウンがなく、安定したダメージを与え続けられます。てきおうりょくのタイプ一致補正×2.0で実質威力160になります。

ラスターカノンはフェアリー（アシレーヌ・フラエッテ永遠）に対して特殊はがね打点として機能します。てっていこうせんは実質威力240の超火力技ですが、使用後Cが2段階下がるため使い切り前提になります。

しんくうはは特殊型でも採用できるかくとう先制技で、タスキ持ち処理に使えます。

**物理型との使い分け:**

物理型に読みを入れてB方向に厚いポケモンを採用してくる相手に対して特殊型は刺さります。ブリジュラス等のB特化には特殊技の方がダメージが通りやすいケースもあります。一方、先制技をバレットパンチ（物理）かしんくうは（特殊）かで選択できる点が両型の使い分けポイントです。

**弱み:**

A145を生かしきれないため、物理型と比べると積み技による爆発力が低下します。また物理打点を切るため、はどうだん・しんくうはの先制以外で物理方向の高速処理ができず、とくぼうの高い特殊受け（カバルドン等の高D枠）に止まりやすいのも物理型にはない弱みです。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、メガルカリオと相性がはっきり出るポケモンを有利・不利の両面から挙げます。メガ後はS112（実数値180）に上がり、てきおうりょくでかくとう・はがねの一致技が実質×2補正となる一方、HP70・D70と耐久は低く、こちらの弱点（ほのお・じめん・かくとう）を突いてくる相手には脆い点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト×2弱点。S85で先手確保。確定1発圏内</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技は等倍（みず0.5×フェアリー2で相殺）。先手確保でCS型でも処理可</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分〜やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S67より先手。ただしコメットパンチは半減（はがね0.5×ひこう1）、インファイト等倍（はがね2×ひこう0.5）が主打点。高耐久で一撃では落としにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分〜やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S65より先手。コメットパンチは半減（むし1×はがね0.5）、インファイト等倍（むし0.5×はがね2）が主打点。高耐久＋バレットパンチに注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ:永遠（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー単体にコメットパンチ／ラスターカノンが×2。S実数値180＞メガ後S169で先手を取り、はがね技で確定圏。主力のムーンフォース（採用率87%）はこちらに等倍（フェアリー2×はがね½）だが、先手の×2はがね技で先に押し切れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ/どくにコメットパンチ／ラスターカノンが×2。S実数値180＞メガ後S168で先手確保</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（炎技に注意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×2（あく2×ドラゴン1）、S112＞98で先手。ただしかえんほうしゃ（採用率67%）・だいもんじ（14%）採用率が高く、ほのお技はこちらに×2で刺さるため、被弾前に1発で押し切りたい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 超有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×4（あく2×はがね2）。低速で先手確保。先制技ふいうち（採用率99%）もこちらにあく0.5×はがね1＝×0.5半減で脅威は小さい</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが弱点×2。スカーフ型はすばやさ約253で先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化できるひこうタイプ（アーマーガア等）を同伴し、ガブリアスの前に引いて受ける。スカーフ型には先制技で削る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がメガルカリオに×2、低耐久で1発耐えがたい。こちらの打点も乏しく、はがね技は両形態に半減、かくとう技も主流のメガY（ほのお/ひこう）には半減（メガXには等倍）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ・でんきタイプを同伴し、リザードンに後出しして弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガマフォクシー（25位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S134（S実数値204）で上を取られ、かえんほうしゃ（採用率66%）のほのお技がメガルカリオに×2。低耐久を上から削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">削れていればバレットパンチ等の先制技で先に倒す。みず・いわタイプを同伴して後続から受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガミミロップ（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S135でこちらより速く、ねこだまし＋高火力のかくとう技（こちらには等倍）で低耐久を上から削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">削れていればバレットパンチ等の先制技で先に倒す。ひこう・エスパータイプを同伴して後続から受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガスターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S120（S実数値189）で上を取られ、アクアジェット（採用率87%）の先制技も持つ。こちらの一致技はみず/エスパーに半減（はがね½・かくとう½）で打点が乏しく、撃ち合いで主導権を取りにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">削れていればバレットパンチ等の先制技で削る。でんき・くさタイプを同伴して後続から弱点を突く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/ほのおにインファイト×0.5（むし0.5×ほのお1）・コメットパンチ×0.5と打点が乏しく、ほのお技はメガルカリオに×2弱点。素ではルカリオ（S実数値180）が速いが、ちょうのまい1積みで抜かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ技（×4）・みず技（×2）で弱点を突くポケモンをパーティに入れて受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高HP・高Bの耐久にA125の高火力を備え、弱点を突けないこちらでは殴り合いで押し負ける。さらにいかくでこちらのAを1段階下げられ、つるぎのまいの積みも実質1段階分削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガルカリオ単体では受からない。でんき技（×4）・いわ技（×2）で弱点を突くポケモンをパーティで合わせる</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">同居率3位。高速地面枠でルカリオが苦手なほのお・じめん枠に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">砂嵐+ステロでダメージ蓄積サポート</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでルカリオの弱点ほのおを半減。みず技でガブリアス・リザードンに打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお対策。みずタイプでメガルカリオの弱点補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">同居率2位。S110の高速特殊アタッカーで、物理偏重になりがちな構成に特殊打点を補う</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガルカリオは耐久が低く弱点も4タイプと多いため、残り5体で以下の役割を補います。

1. **じめん（ガブリアス）対策**: カバルドンやみず・こおりタイプでガブリアスのじしんを受ける枠
2. **ほのお対策**: みずタイプ（アシレーヌ等）でリザードン・マフォクシーのほのお技を受ける枠
3. **かくとう対策**: ひこう・エスパータイプでメガミミロップ等のかくとう技を受ける枠
4. **ステルスロック展開**: カバルドン等でステロを撒き、交換読みダメージを蓄積

---

## データ分析①：技採用率が示す「先制技4枠目」の枠争い

メガルカリオの技採用率を並べると、メインウェポンとは別に**先制技が3種で票を分け合っている**構図が見えます。

| 技 | タイプ | 役割 | 採用率 |
|---|---|---|---|
| バレットパンチ | はがね | 先制（一致・実質80） | 48.0% |
| しんそく | ノーマル | 先制（一致なし・威力40） | 23.6% |
| しんくうは | かくとう | 先制（一致・実質80） | 26.0% |

3つの先制技の採用率を合計すると97.6%に達し、ほぼ全ての個体が**いずれか1種の先制技を必ず搭載**していることが分かります。HP70・D70と低耐久なメガルカリオにとって、上から殴られても瀕死圏の相手を取りこぼさない先制技は「枠を1つ割く価値のある必須要素」と扱われていると読めます。

タイプ一致のバレットパンチ（実質80）・しんくうは（実質80）が物理型・特殊型でそれぞれ主流になる一方、しんそく23.6%は一致補正が乗らない（威力40）にもかかわらず一定数採用されています。バレットパンチははがねを半減するほのお・みず・でんき・はがねタイプに通りにくく、しんくうははかくとうを半減するひこう・エスパー・どくに刺さりません。しんそくはこれら一致先制技が半減される相手にも等倍で40を入れられるため、低耐久ゆえに相手の取りこぼしが致命傷になるルカリオが、先制技の通り先を散らす保険として採用していると読めます。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">つるぎのまいAS物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ようき 66.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・インファイト・コメットパンチ・バレットパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の爆発力最大。先制技で詰め対応</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積みターンが必要。ガブじしん読みが必須</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CS特殊型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう 18.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">はどうだん・ラスターカノン・しんくうは・じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">能力ダウンなしで安定。物理型と誤認させる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み爆発力が低下。A145を生かせない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガルカリオはてきおうりょくによる高火力と、S112による先手を両立した環境上位のアタッカーです。先制技を持つため単体でも詰め性能を発揮できます。

M-2環境では使用率2位のブリジュラス（はがね/ドラゴン）にインファイトが×2で刺さるのが大きな強みです。一方でアーマーガア・ハッサムなどはがね複合にはコメットパンチが半減しインファイト等倍止まりとなるため、過信せず先手とインファイトで押す立ち回りが基本になります。攻撃範囲の広さから9位という高い使用率を維持しています。

弱点のガブリアス（1位）はパーティ構成でケアしつつ、ブリジュラスや各種はがねタイプに積極的に攻撃を仕掛けていくのが基本戦術となります。つるぎのまい1積みを通す機会を作れるかどうかが勝敗を分ける重要なポイントです。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [単体では受けにくいギャラドスのM-2考察](/blog/gyarados-analysis-m2/)
- [同じはがねアタッカー ハッサムのM-2考察](/blog/scizor-analysis-m2/)
