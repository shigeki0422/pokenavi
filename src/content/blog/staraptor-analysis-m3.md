---
title: '【ポケモンチャンピオンズ】メガムクホーク考察 M-3 使用率6位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率6位のメガムクホークを徹底分析。インファイト99.0%・はねやすめ91.3%・ブレイブバード90.6%の採用率を実データで解説。特性あまのじゃくでインファイト後にAB上昇する仕組みと環境上位への相性・パーティ構成まで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-staraptor-m3.png'
draft: true
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
  <img src="/images/pokemon/pokemon-0398-00.webp" alt="メガムクホーク" />
  <div>
    <h2 style="margin:0 0 8px">メガムクホーク</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">6位</strong>　特性: <strong>あまのじゃく（メガ後固定）</strong>　メガ前採用特性: <strong>いかく 97.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガムクホークは**使用率6位**を記録。素のムクホーク（ノーマル/ひこう）がメガ進化するとタイプが**かくとう/ひこう**に変わり、特性が**あまのじゃく**（自分の能力低下が逆に上昇に変わる）になります。

この特性の恩恵が最も大きいのがインファイト（採用率99.0%）です。インファイトはかくとうタイプ一致の威力120の高火力技ですが、使用後にこうげき・ぼうぎょが1段階ずつ下がるデメリットがあります。あまのじゃくのもとでは**このデメリットが逆転し、こうげき・ぼうぎょが1段階ずつ上がる**ため、インファイトを連打するほど火力と物理耐久が上がり続ける独自の戦術を取れます。

---

## なぜ今メガムクホークが使用率6位なのか

### 1. あまのじゃく＋インファイトで殴るほど強くなる

メガ後特性あまのじゃくは、自分の能力が下がるデメリット技のペナルティを逆転させます。インファイトの「使用後にA・Bが1段階ダウン」は**「使用後にA・Bが1段階アップ」**に変わります。こうげきが140と高い水準から始まり、インファイトを連打するたびに更に上昇するため、相手が交代しない限り火力と物理耐久が雪だるま式に積み上がります。

### 2. かくとう/ひこうの攻撃範囲の広さ

メガ後タイプがかくとう/ひこうになるため、タイプ一致技で広い範囲をカバーします。インファイト（かくとう）はノーマル・はがね・いわ・あく・こおりに等倍以上が通り、ブレイブバード（ひこう、採用率90.6%）はかくとう・むし・くさへの打点になります。ブレイズキック（ほのお、採用率53.1%）を合わせると、はがね・くさ・こおりなどひこう技でも止まりにくい相手への補完打点も確保できます。

### 3. すばやさ110からの先手と持続戦略

メガ後のすばやさは110で、環境上位の多くより速く先手を取れます。はねやすめ（採用率91.3%）で継続的にHPを回復しながら、インファイトで能力を上げ続けるため、対面での削り合いに強い持続型のアタッカーとして機能します。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">140</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">100</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">110</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">585</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

こうげき140はメガ後の環境でも高水準。ぼうぎょ100・とくぼう90とメガ進化で大きく底上げされ、すばやさ110と合わせてバランスの取れた物理アタッカーです。インファイトでA・Bが上がり続ける運用と噛み合った種族値配分になっています。

### タイプ・弱点（メガ進化後: かくとう/ひこう）

<div class="type-row">
  <strong>タイプ（メガ後）：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.25）</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

ひこうタイプがじめんを無効化するため、環境に多いガブリアスのじしん（採用率99.2%）を完全に無効化できます。むし技はかくとう×0.5・ひこう×0.5の掛け合わせで**×0.25**と大幅に軽減。一方、弱点は5タイプと多く、特にエスパー・フェアリー・ひこうの特殊技を上から浴びると危険です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>インファイト</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">99.0%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はねやすめ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">91.3%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ブレイブバード</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">90.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ブレイズキック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">53.1%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>とんぼがえり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ふきとばし</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みがわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>でんこうせっか</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7.2%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ダブルウイング</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>いのちがけ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3.1%</td>
</tr>
</tbody>
</table>
</div>

メガ前の採用特性は**いかく 97.5%**（こうげきを1段階下げる）。メガ進化すると特性はあまのじゃくに自動的に切り替わります。性格は**ようき 75.3%**が最多で、S110を最大まで伸ばす方向が主流です。

---

## 主要型の解説

性格分布はようき75.3%・いじっぱり19.8%の2択。ようき型はS実数値を優先し、いじっぱり型はこうげきに補正をかけて火力を高める選択になります。

### 型1: ようきAS型（最多採用）

**性格採用率: ようき 75.3%**（S重視型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0398-00.webp" alt="メガムクホーク" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようきインファイト連打型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.5%）※メガ後あまのじゃく<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（採用率28.4%）<br>
<strong>持ち物:</strong> ムクホークナイト（96.0%）
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・ブレイブバード<br>
・はねやすめ<br>
・ブレイズキック
</div>
</div>
</div>

**強み:**

ようき最速でS実数値は179（種族値110・EV32・補正1.1）となり、環境上位の多くより先手を取れます。インファイトを初回使用した後はA・Bが1段階ずつ上昇し、2発目以降はこうげき実数値がさらに高まります。いじっぱり型と比べて、A補正なしの代わりにS優位を確保するのがようき型の差別点です。ブレイブバードとの2タイプ一致技でかくとう・ひこうを通せない相手にはブレイズキックで対応します。

**弱み:**

こうげき補正がないためいじっぱり型と比べて初回インファイトの威力が約10%低く、インファイト1発で倒せなかった場面が出やすいです。ブレイブバードの反動で削れると、はねやすめを挟む必要があり攻撃の手が止まります。

---

### 型2: いじっぱりAS型

**性格採用率: いじっぱり 19.8%**（火力重視型の指標）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0398-00.webp" alt="メガムクホーク" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASいじっぱり火力型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（97.5%）※メガ後あまのじゃく<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（採用率11.6%）<br>
<strong>持ち物:</strong> ムクホークナイト（96.0%）
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・ブレイブバード<br>
・はねやすめ<br>
・ブレイズキック
</div>
</div>
</div>

**強み:**

こうげきに1.1倍の性格補正がかかり、ようき型よりA実数値が約10%高くなります。インファイト1発目から高い打点を出せるため、耐久寄りの相手をようき型では2発かかるところを1発で倒せる可能性があります。S実数値はようき型（179）に対しいじっぱり型では163（補正なし）となるため、S163超の相手にはようき型が先手を取れる場面でいじっぱり型は後手に回ります。

**弱み:**

S163以上の相手（ようき型メガムクホークS179等）に先手を取られる点で、ようき型とは差があります。いじっぱり型が多数派でないのはこのS帯の差が対環境で影響するためと考えられます。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

かくとう/ひこうは弱点が5タイプ（エスパー・ひこう・フェアリー・でんき・こおり）と多い一方、じめんを無効化するためガブリアスのじしんを受けられません。インファイト連打でA・Bを上げながら戦う運用上、物理受けを崩しやすい構図があります。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）をひこうタイプで無効化。インファイトがじめん×1・ドラゴン×1で等倍、ブレイブバードがドラゴン×1・ひこう×1で等倍かつS110でメガガブリアスより速い。ガブリアスからの主力打点じしんを受けずに一方的に殴れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトがあく×0.5×はがね×2=等倍だが、S110＞ドドゲザンで先手。ブレイブバードはあく×1×はがね×1=等倍。ドドゲザンからのふいうち（あく×1×かくとう×0.5=0.5倍）で半減できるため継続的に削られにくい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.0%）を無効化。インファイトがじめん×1で等倍かつS110＞カバルドンで先手。あくびで眠らされると厄介だが、はねやすめで引き続けるか相手の交代に合わせてインファイトを打てる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトがみず×1×フェアリー×2=×2弱点を突かれる側。ムーンフォース（フェアリー×2×かくとう×1=×2）が刺さる。S110＞アシレーヌで先手を取りブレイブバードでみず×1×フェアリー×1=等倍を打てるが、フェアリー弱点持ちのため慎重な対応が必要</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガリザードンYはS110で同速帯（メガ後S100なのでこちらが先手）。ただしソーラービーム（くさ×0.5×かくとう×1=0.5倍）は半減だが、ほのお技はかくとう×1×ひこう×1=等倍。メガリザードンXはドラゴン/ほのおでブレイズキックが半減される</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のエスパー・ひこう・フェアリー・でんき・こおりを主力技として持つ環境上位を中心に選定しました。

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
    <img src="/images/pokemon/pokemon-0025-01.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ライチュウ（アローラ）（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S130でこちらより速い。10まんボルト（でんき×2）を上から通される。サイコキネシス（エスパー×2）も刺さり2タイプの弱点を同時に突ける相手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん技を持つポケモン（ガブリアス等）を同伴し、ライチュウの前に引いて処理。メガムクホーク自身での対処は難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウォーターフォール・たきのぼり等のひこう×2技が刺さる。メガギャラドスはS81でこちらより遅いが、たつまき（ひこう×2）・かみなり（でんき×2）で両方の弱点を突ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブレイブバードで先手を取り削れるが、みず技は等倍止まりで受けきれない。でんき技を持つパートナーと連携して処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0282-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サーナイト（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（フェアリー×2）・サイコキネシス（エスパー×2）の両方が弱点。高とくこうから上から刺される形になりやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技を持つパートナーを同伴しサーナイトに打点を入れる。メガムクホーク自身のブレイズキックはフェアリー×1×エスパー×1=等倍で有効打を出しにくい</td>
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
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ムクホークが苦手なでんき・フェアリーへのじしん打点。じしんをひこうで無効化する役割も逆方向で補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ムクホークが苦手なほのお・エスパー複合への水技。フェアリー半減でムクホークのフェアリー弱点を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん無効のひこうタイプで補完。ムクホークと同じくガブリアスのじしんを無効化できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー">
    <div class="name">カイリュー</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね複合へのりゅうせいぐんとムクホークのかくとう技で役割補完。でんき技が来たときの受け役</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0080-01.webp" alt="ニョロトノ">
    <div class="name">ニョロトノ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あめを降らせてでんき技の脅威を軽減するサポート役として連携できる</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガムクホークは物理アタッカーとして高い突破力を持つ一方、弱点タイプが5つあるため受け役・耐性補完が必要です。残り5体で以下を補います。

1. **でんき対策**: じめん技や雨天候でライチュウ等のでんき勢を牽制できる枠
2. **フェアリー・エスパー対策**: はがね技を持つポケモンやどく技でフェアリー弱点をカバー
3. **ひこう対策**: いわ技・でんき技を持つポケモンでひこう弱点を突いてくる相手への打点を確保
4. **回復サポート**: はねやすめで自己回復できるためヒーラー役は不要だが、毒・やけど等の状態異常対策は必要

---

## データ分析①：インファイト99.0%が示す「あまのじゃく特化」の運用思想

メガムクホークの技採用率を並べると、インファイト99.0%という突出した数値が目を引きます。他の技と比較すると、この採用率が何を示しているかが明確になります。

| 技 | 採用率 | 役割 |
|---|---|---|
| インファイト | 99.0% | あまのじゃくでAB上昇に逆転するメイン技 |
| はねやすめ | 91.3% | HP回復・継戦能力の確保 |
| ブレイブバード | 90.6% | タイプ一致ひこう火力 |
| ブレイズキック | 53.1% | はがね・くさへの補完 |
| とんぼがえり | 16.5% | 対面操作 |

インファイト・はねやすめ・ブレイブバードの3技は90%を超える採用率を誇り、実質的に**ほぼ全個体がこの3技を確定で採用**しています。これは「インファイトで削り・ブレイブバードで広い範囲をカバー・はねやすめで継戦するセット」が非常に完成度の高いコアであることを示しています。

残り1枠にブレイズキック53.1%・とんぼがえり16.5%が入る形で、ブレイズキックがはがね・くさタイプへの補完打点として過半数に採用されています。とんぼがえりの16.5%は対面操作に特化した運用を選んだ場合の選択肢と見ることができます。

持ち物採用率はムクホークナイト96.0%と圧倒的で、こだわりスカーフ3.4%はほとんど誤差範囲です。これは「インファイト連打でABを上げながら戦う」という特殊性がメガ進化前提の運用と不可分であり、こだわりスカーフ型ではインファイトのデメリット反転という最大の旨みを活かせないためです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASようき型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ようき 75.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">インファイト・ブレイブバード・はねやすめ・ブレイズキック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S179で環境上位の多くより先手を確保できる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型より初回インファイトの火力が約10%低い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASいじっぱり型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり 19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">インファイト・ブレイブバード・はねやすめ・ブレイズキック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A補正でようき型より初回インファイトの威力が約10%高い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S163でようき型（S179）が先手を取れる相手に後手に回る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガムクホークはかくとう/ひこうへのタイプ変化と特性あまのじゃくの組み合わせにより、インファイトを連打するほどA・Bが上昇し続ける独自の物理アタッカーです。インファイト99.0%・はねやすめ91.3%・ブレイブバード90.6%の採用率が示すように、3技がほぼ確定の「コア」として機能しており、残り1枠をブレイズキックかとんぼがえりで補完する形が実態です。

弱点は5タイプと多く、エスパー・フェアリー・でんき・ひこう・こおりの特殊技を上から浴びると危険なため、これらへの対策をパーティ単位で用意する必要があります。ガブリアスのじしんを無効化できるひこうタイプの恩恵は大きく、環境最多使用率のガブリアスに対して一方的に有利を取れる点が使用率6位の一因です。

---

## 関連記事

- [使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [ムクホークが苦手なライチュウ（アローラ）のM-3考察](/blog/raichu-alola-analysis-m3/)
- [使用率2位 ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
