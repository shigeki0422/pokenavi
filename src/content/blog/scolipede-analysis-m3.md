---
title: '【ポケモンチャンピオンズ】ペンドラー考察 M-3 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率78位のペンドラーを徹底分析。かそく特性でS+1を積みながら、つるぎのまい72.2%・バトンタッチ61.9%で後続エースにS+A段階をそのまま引き継ぐバトン型と、メガ進化後のB149を活かす耐久型の採用実態を実データで解説します。'
updatedDate: '2026-06-26'
pubDate: '2026-06-26'
heroImage: '../../assets/hero-scolipede-m3.png'
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
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" />
  <div>
    <h2 style="margin:0 0 8px">ペンドラー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">78位</strong>　特性: <strong>かそく 98.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/25）時点の集計です

シーズンM-3のシングルバトルで、ペンドラーは**使用率78位**を記録。特性かそくで毎ターンS+1を積みながら、つるぎのまい（72.2%）でA+2を乗せてバトンタッチ（61.9%）で後続に引き継ぐ**積みバトン型**が主流です。メガ進化（ペンドラナイト32.0%）ではS112→62と大幅に下がる一方B149になり、まもる（58.9%）でかそくを安全に積んでから強引に押す耐久物理型としての運用もあります。なおメガ後の特性はシェルアーマー（急所無効）に変わり、かそくが働かない点に注意が必要です。

---

## なぜ今ペンドラーが使用率78位なのか

### 1. かそく×バトンタッチで後続エースに積み状態を丸ごと渡せる

特性かそく（98.9%）は毎ターンS+1を積みます。ペンドラー自身がつるぎのまいでA+2まで積んだ後にバトンタッチを使うと、**S上昇段階とA+2を後続に引き継げます**。受け取ったエースは積み済みの状態から攻撃を開始できるため、単体で積んで全抜きを狙うより受け渡し先の選択肢が広く、相手が耐性を合わせて対応しにくくなります。

### 2. まもるでかそくを安全に重ねながら積める

まもる（58.9%）はダメージを受けずに1ターンをやり過ごせる技で、ペンドラーは使用ターンにもかそくが発動してS+1を得られます。つるぎのまい・まもるを組み合わせれば相手が有効打を持つポケモンを繰り出すターンを稼ぎながら積み段階を増やせます。

### 3. きゅうけつ採用でHP補填しながら場に留まれる

きゅうけつ（31.4%）はむしタイプの吸収技で、与えたダメージの一部を回復できます。タスキやオボンのみと組み合わせることで、相手の削りに対してHP補填しながら積みターンを伸ばせます。

---

## 基本スペック

### 種族値（メガ進化前後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;margin-bottom:4px;font-size:0.82em;color:#555;font-weight:600">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">89</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">69</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">112</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">−50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">485</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+200</span>
  </div>
</div>

通常時はS112と高速で、かそくとの組み合わせで積みながら先手を広げられます。一方、メガ進化するとS62と低速帯になり、特性もシェルアーマーに変わるためかそくでS+1を積めなくなりますが、A140・B149と物理火力・物理耐久が大幅に上がります。メガ後はS不利を受け入れ、B149の耐久を活かしながらじしん（45.5%）・まもる（58.9%）で場持ちする戦い方になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="むし" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
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
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう（×0.25）</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（×0.25）</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく（×0.5）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.5）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

むし/どくの複合により、かくとう技・くさ技は**×0.25**、どく技・むし技は**×0.5**で受けられます。弱点はひこう・ほのお・いわ・エスパーの4タイプで、いずれも×2です。環境上位のムクホーク（ひこう技）など、弱点を突かれる機会は多い点に注意が必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>つるぎのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">72.2%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>バトンタッチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">61.9%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>まもる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">58.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じしん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">45.5%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>てっぺき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">34.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>きゅうけつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">31.4%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">26.9%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ダストシュート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">14.6%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みがわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>メガホーン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10.3%</td>
</tr>
</tbody>
</table>
</div>

技採用率を見ると、バトンタッチ型（バトン＋つるぎのまい＋まもる）とメガ進化後の物理押し型（じしん＋つるぎのまい＋まもる）の2系統が混在しています。バトンタッチ61.9%が過半数を占める一方、じしんも45.5%採用されており、対面した段階ではどちらの系統か即座に読みにくい状態が生まれています。

---

## 主要型の解説

性格分布はようき31.9%・いじっぱり30.4%が拮抗し、わんぱく18.4%が続きます。バトン型はようき/いじっぱり、メガ後耐久型はわんぱくに分かれます。

### 型1: ようき/いじっぱりかそくバトン型（最多採用）

**性格採用率: ようき 31.9%・いじっぱり 30.4%**（バトン軸の2択。EV最多分布 H2-A32-S32 13.4%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようき/いじっぱりバトン型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（98.9%）<br>
<strong>性格:</strong> ようき（S↑ C↓）/ いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率13.4%）<br>
<strong>持ち物:</strong> きあいのタスキ（24.3%）/ たべのこし（14.0%）/ オボンのみ（14.1%）
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・バトンタッチ<br>
・まもる<br>
・きゅうけつ
</div>
</div>
</div>

**強み:**

かそくで毎ターンSを積みながら、つるぎのまいでA+2を乗せてバトンタッチで後続エースに引き継ぐ型です。ようき型はS実数値180となり、ガブリアス（最速S169）など環境上位の一部より速くバトンを準備できます。ただしムクホーク・リザードンといった弱点を突ける高速勢には届かないため、先手範囲は限定的です。いじっぱり型はようき型より積む前のA実数値が高く、バトンを渡す前に攻撃で削る択も取りやすくなります。まもるを挟むことで安全にかそくのS+1を積み、バトンを渡す準備ができます。きゅうけつでHPを補填しながら場に留まることで、積みターンをさらに確保できます。

**弱み:**

ひこう・ほのお・いわ・エスパーの弱点を突かれると積み始める前に致命打を受ける危険があります。ようき型はいじっぱり型よりA実数値が下がるため、積む前の攻撃力は低くなります。バトンタッチで引き継いでも、後続が弱点を持つ場合は引き継いだ積みが活きないケースがあります。きあいのタスキ採用個体は弱点技を1発まで耐えられますが、まもる・かそくのS+1で保険は使い切れません。

---

### 型2: わんぱくメガ進化耐久型

**性格採用率: わんぱく 18.4%**（B強化でメガ後B149をさらに伸ばす。EV H32-B2-S32 4.7%等）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ABわんぱくメガ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（98.9%）※メガ後はシェルアーマー<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32 B2 S32（採用率4.7%）<br>
<strong>持ち物:</strong> ペンドラナイト（32.0%）
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・じしん<br>
・まもる<br>
・きゅうけつ
</div>
</div>
</div>

**強み:**

メガ進化でB89→B149に跳ね上がり、わんぱく補正でさらにB実数値を高められます。メガ後はシェルアーマーに変わるためかそくでS+1を積めませんが、つるぎのまいはメガ前にまもるで身を守りながら積めます。S62と低速になるぶん多くの相手に後攻になる一方、B149の物理耐久で物理技を受けながら、つるぎのまいで乗せたA+2をじしんで押すルートを取れます。じしんはA140（メガ後）から放てるため、補完打点としての火力水準は十分あります。

**弱み:**

バトン型と異なり積んだ能力を後続に渡さないため、ペンドラー自身でフィニッシュまで持っていく必要があります。メガ後はシェルアーマーでかそくが働かず、S62のまま低速なのでひこう・ほのお・エスパータイプの速い相手には弱点技で先手を取られます。バトン型に比べてパーティへの貢献が単体完結型になり、後続エースへのサポートが薄い点がデメリットです。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがガブリアスに等倍で通るが、相手のじしんもこちらに等倍。ようき型（S実数値180）なら最速ガブ（S169）に先攻でき積み始めやすいが、メガ型はS62で後攻になり削られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ムクホーク（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう技（ブレイブバード等）がむし/どくのこちらに×2で刺さる。かそくを積む前に弱点技で先制される危険が高い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ライチュウ（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ライチュウナイトY採用率96.4%でメガ前提。メガ後はC160・S実数値200（おくびょう）となり、積み前のペンドラー（ようきS実数値180）はもちろんS112勢を抜けず先手を取られる。最多採用のでんじほう（でんき）はむし/どくに等倍で、C160の高火力が刺さりまひも撒かれる。特性ノーガードでかくとう技（きあいだま）が必中になるが、むし/どくには¼で軽い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（97.9%）はこちらに等倍止まりで弱点を突かれず、S47と遅いため積み始めやすい</td>
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
    <img src="/images/pokemon/pokemon-0398-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ムクホーク（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう技がむし/どく両タイプに等倍ではなく×2弱点で直撃する。高Sで先手を奪われやすく積みを開始できない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・でんき技を持つアタッカーでムクホークを事前に削ってから展開する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がむしタイプに×2弱点。高速なリザードンに対して先手を取れず積みターンが作れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ技を持つ枠でリザードンを処理してからペンドラーを展開する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（使用率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">採用率87.7%のサイコファング（エスパー）がむし/どくどちらにも×2弱点で刺さり、A135の高火力で一撃が重い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・ゴースト技を持つ枠でメタグロスを処理してからペンドラーを展開する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン（パートナー上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">パートナー1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">バトンタッチでSとA+2を受け取り一気に全抜きを狙えるエース候補</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">パートナー2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ペンドラーのバトンを受け取って高速物理ひこうで制圧するバトン後エース</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ">
    <div class="name">ライチュウ</div>
    <div class="rate">パートナー3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">メガライチュウY（C160・S実数値200）でひこうタイプを高速でんきで処理するエース。メガ枠を使うためメガ型ペンドラーとは併用不可、バトン型と組ませる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">パートナー4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでペンドラーが弱いほのお・いわ技を半減し、高耐久で受け回す枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">パートナー5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわで一撃を防ぎつつつるぎのまいで積み、バトンを受けるエース候補</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">パートナー6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでひこう技を半減し、ペンドラーの弱点を補完する受け枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

バトン型では、ペンドラーが積んでバトンを渡した後のエースに弱点対応がないポケモンを選ぶことが重要です。

1. **バトン受け取りエース**: ガブリアス・ムクホークなど物理アタッカーで、S上昇込みの速度とA+2の火力で全抜きできるポケモン
2. **ひこう・ほのお対策**: ペンドラーの弱点4タイプ（ひこう・ほのお・いわ・エスパー）に対して打点を持つ枠をパーティに置く
3. **壁サポート**: オーロンゲ（同居率8位）等でリフレクター・ひかりのかべを張り、ペンドラーの積みターンを確保する

---

## データ分析①：技と持ち物の採用率から2つの型の比率を読む

ペンドラーの技採用率を役割で分けると、バトン軸の技とメガ物理軸の技が併存していることが見えます。

| 技 | 採用率 | 役割 |
|---|---|---|
| つるぎのまい | 72.2% | A+2積み（バトン型・メガ型共通） |
| バトンタッチ | 61.9% | 積み状態を後続に渡す（バトン型専用） |
| まもる | 58.9% | 安全に1ターン稼ぐ（両型共通） |
| じしん | 45.5% | 補完打点（メガ型・一部バトン型） |
| きゅうけつ | 31.4% | HP補填（両型共通） |

バトン型専用のバトンタッチが61.9%、メガ型に寄るじしんが45.5%で、**バトン渡し型が過半数を占めつつメガ押し込み型も半数近く存在する**ことを数値が示しています。型の判別は持ち物が手がかりになり、ペンドラナイト（32.0%）がメガ型、きあいのタスキ（24.3%）・オボンのみ（14.1%）・たべのこし（14.0%）はバトン型に多く採用されます。

持ち物分布を見ると、ペンドラナイト（32.0%）が最多ではあるものの、残り68.0%は非メガ石であり、過半数がバトン型または非メガ物理型です。対面した際には「ペンドラナイト＝メガ型」「タスキ/たべのこし/オボン＝バトン型」と持ち物から判断するのが現実的な読み筋になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ようき/いじっぱりバトン型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ようき 31.9% / いじっぱり 30.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき / いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・バトンタッチ・まもる・きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ようきはS実数値180で最速ガブ（169）に先攻、いじっぱりは積む前のAが約10%高い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">弱点4タイプの高速勢に先手を取られると積めない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ABわんぱくメガ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく 18.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・じしん・まもる・きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B149の物理耐久で物理技を受けながら積める</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S62で弱点タイプに先手を取られやすく後続サポートが薄い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ペンドラーはかそく特性でSを積みながらつるぎのまいでA+2を乗せてバトンタッチで後続に渡す積みバトン型が最多構成です。ようき（31.9%）・いじっぱり（30.4%）の2択でバトン型、わんぱく（18.4%）でメガ進化耐久型に分かれ、持ち物（ペンドラナイト32.0%・タスキ24.3%等）で型を判断できます。メガ型は特性がシェルアーマーに変わりかそくが働かない点に注意が必要です。弱点はひこう・ほのお・いわ・エスパーの4タイプで、特にひこう技を持つムクホークや高速ほのおタイプへの対処はパーティで用意する必要があります。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [ラグラージのM-3考察](/blog/swampert-analysis-m3/)
- [オーロンゲのM-3考察](/blog/grimmsnarl-analysis-m3/)
