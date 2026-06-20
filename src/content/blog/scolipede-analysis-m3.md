---
title: '【ポケモンチャンピオンズ】ペンドラー考察 M-3 使用率77位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率77位のペンドラーを徹底分析。かそく特性でS+1を積みながら、つるぎのまい69.6%・バトンタッチ54.9%で後続エースにS+A段階をそのまま引き継ぐバトン型と、メガ進化後のB149を活かす耐久型の採用実態を実データで解説します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-scolipede-m3.png'
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
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" />
  <div>
    <h2 style="margin:0 0 8px">ペンドラー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">77位</strong>　特性: <strong>かそく 99.3%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、ペンドラーは**使用率77位**を記録。特性かそくで毎ターンS+1を積みながら、つるぎのまい（69.6%）でA+2を乗せてバトンタッチ（54.9%）で後続に引き継ぐ**積みバトン型**が主流です。メガ進化（ペンドラナイト38.5%）ではS112→62と大幅に下がる一方B149になり、まもる（54.4%）でかそくを安全に積んでから強引に押す耐久物理型としての運用もあります。

---

## なぜ今ペンドラーが使用率77位なのか

### 1. かそく×バトンタッチで後続エースに積み状態を丸ごと渡せる

特性かそく（99.3%）は毎ターンS+1を積む。ペンドラー自身がつるぎのまいでA+2まで積んだ後にバトンタッチを使うと、**S上昇段階とA+2を後続に引き継げる**。受け取ったエースは積み済みの状態から攻撃を開始できるため、単体で積んで全抜きを狙うより受け渡し先の選択肢が広く、相手が耐性を合わせて対応しにくい。

### 2. まもるでかそくを安全に重ねながら積める

まもる（54.4%）はダメージを受けずに1ターンをやり過ごせる技で、ペンドラーは使用ターンにもかそくが発動してS+1を得る。つるぎのまい・まもるを組み合わせれば相手が有効打を持つポケモンを繰り出すターンを稼ぎながら積み段階を増やせる。

### 3. きゅうけつ採用でHP補填しながら場に留まれる

きゅうけつ（35.0%）はむしタイプの吸収技で、与えたダメージの一部を回復できる。タスキやオボンのみと組み合わせることで、相手の削りに対してHP補填しながら積みターンを伸ばせる。

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
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">140</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:74.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">149</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:49.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">99</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:31%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">62</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">−50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">585</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

通常時はS112と高速で、かそくとの組み合わせで積みながら先手を広げられます。一方、メガ進化するとS62と低速帯になるため先制はほぼ取れなくなりますが、A140・B149と物理火力・物理耐久が大幅に上がります。メガ後はS不利を受け入れ、B149の耐久を活かしながらじしん（54.7%）・まもる（54.4%）で場持ちする戦い方になります。

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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう（×0.5）</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく（×0.5）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

むし/どくの複合により、むし技はむし×1・どく×0.5で**×0.5の耐性**、かくとう技はむし×0.5・どく×1で**×0.5の耐性**になります。弱点はひこう・ほのお・いわ・エスパーの4タイプで、いずれも×2です。環境上位のムクホーク（ひこう技）やガブリアスがほのお技を採用している個体（一部）など、弱点を突かれる機会は多い点に注意が必要です。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">69.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>バトンタッチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">54.9%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じしん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">54.7%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>まもる</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">54.4%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>きゅうけつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">35.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>てっぺき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">33.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">20.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ダストシュート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みがわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.7%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくどく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8.1%</td>
</tr>
</tbody>
</table>
</div>

技採用率を見ると、バトンタッチ型（バトン＋つるぎのまい＋まもる）とメガ進化後の物理押し型（じしん＋つるぎのまい＋まもる）の2系統が混在しています。バトンタッチ54.9%とじしん54.7%がほぼ同率なのは、この2系統が環境に同数存在することを示しており、対面した際に即座に型を読みにくい状態が生まれています。

---

## 主要型の解説

性格分布はようき33.7%・いじっぱり31.8%・わんぱく16.1%の順で、バトン型はようき/いじっぱり、メガ後耐久型はわんぱくに分かれます。

### 型1: ようき/いじっぱりかそくバトン型（最多採用）

**性格採用率: ようき 33.7%・いじっぱり 31.8%**（バトン軸の2択。EV最多分布 H2-A32-S32 16.6%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようき/いじっぱりバトン型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（99.3%）<br>
<strong>性格:</strong> ようき（S↑ C↓）/ いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率16.6%）<br>
<strong>持ち物:</strong> きあいのタスキ（22.2%）/ オボンのみ（12.6%）/ たべのこし（11.5%）
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

かそくで毎ターンSを積みながら、つるぎのまいでA+2を乗せてバトンタッチで後続エースに引き継ぐ型です。ようき型はS最大化でかそく前から多くの相手に先手を取れる範囲が広く、積みながら速度を重ねてバトンを渡すまでの生存率が高まります。いじっぱり型はA実数値を上げて、バトンを渡す前に攻撃で削る択も取りやすくなります。まもるを挟むことで安全にかそくのS+1を積み、バトンを渡す準備ができます。きゅうけつでHPを補填しながら場に留まることで、積みターンをさらに確保できます。

**弱み:**

ひこう・ほのお・いわ・エスパーの弱点を突かれると積み始める前に致命打を受ける危険があります。ようき型はいじっぱり型よりA実数値が下がるため、積む前の攻撃力は低い。バトンタッチで引き継いでも、後続が弱点を持つ場合は引き継いだ積みが活きないケースがあります。きあいのタスキ採用個体は弱点技を1発まで耐えられますが、まもる・かそくのS+1で保険は使い切れません。

---

### 型2: わんぱくメガ進化耐久型

**性格採用率: わんぱく 16.1%**（B強化でメガ後B149をさらに伸ばす。EV A32-B32-D2 6.1%等）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0545-00.webp" alt="ペンドラー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ABわんぱくメガ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（99.3%）※メガ後も同特性<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> A32 B32 D2（採用率6.1%）<br>
<strong>持ち物:</strong> ペンドラナイト（38.5%）
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

メガ進化でB89→B149に跳ね上がり、わんぱく補正でさらにB実数値を高められます。S62と低速になるぶん多くの相手に後攻になりますが、B149の物理耐久で物理技を受けながらまもるでかそくのS+1を積み、つるぎのまいでA+2を乗せてじしんで押すルートを取れます。じしんはA140（メガ後）から放てるため、補完打点としての火力水準は十分あります。

**弱み:**

バトン型と異なり積んだ能力を後続に渡さないため、ペンドラー自身でフィニッシュまで持っていく必要があります。S62と低速なのでひこう・ほのお・エスパータイプの速い相手には弱点技で先手を取られます。バトン型に比べてパーティへの貢献が単体完結型になり、後続エースへのサポートが薄い点がデメリットです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがガブリアスに等倍で通るが、相手のじしん（じめん）もこちらに等倍。S112（通常）なら後攻になることが多くバトン型は積む前に削られるリスクがある</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技はこちらに等倍だが、高Sで先手を取られやすく積む前に削られる。じしんでライチュウに×2を狙えるが先攻が難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0477-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ヨノワール（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴーストタイプでこちらの技が弱点でなく、低Sでバトン型の積みターンを確保しやすい。じしんが等倍で通る</td>
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
    <img src="/images/pokemon/pokemon-0065-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フーディン（上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー技がむし/どくどちらにも×2弱点で刺さる。高Sで先手をほぼ奪われる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・ゴースト技を持つ枠でフーディンを優先処理してからペンドラーを投入する</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ペンドラーが苦手なひこうタイプに対してでんき打点を持てるサポート枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0260-00.webp" alt="ラグラージ">
    <div class="name">ラグラージ</div>
    <div class="rate">パートナー4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお・いわ弱点をみず技でケアできる補完枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ">
    <div class="name">オーロンゲ</div>
    <div class="rate">パートナー5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">リフレクター・ひかりのかべで先制ダメージを軽減し積みターンを作る補助枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

バトン型では、ペンドラーが積んでバトンを渡した後のエースに弱点対応がないポケモンを選ぶことが重要です。

1. **バトン受け取りエース**: ガブリアス・ムクホークなど物理アタッカーで、S上昇込みの速度とA+2の火力で全抜きできるポケモン
2. **ひこう・ほのお対策**: ペンドラーの弱点4タイプ（ひこう・ほのお・いわ・エスパー）に対して打点を持つ枠をパーティに置く
3. **壁サポート**: オーロンゲ等でリフレクター・ひかりのかべを張り、ペンドラーの積みターンを確保する

---

## データ分析①：バトンタッチとじしんが同率採用率から見える2つの型の共存

ペンドラーの技採用率の特徴は、バトンタッチ（54.9%）とじしん（54.7%）がほぼ同率である点にあります。

| 技 | 採用率 | 役割 |
|---|---|---|
| つるぎのまい | 69.6% | A+2積み（バトン型・メガ型共通） |
| バトンタッチ | 54.9% | 積み状態を後続に渡す（バトン型専用） |
| じしん | 54.7% | 補完打点（メガ型・一部バトン型） |
| まもる | 54.4% | かそく安全積み（両型共通） |
| きゅうけつ | 35.0% | HP補填（両型共通） |

バトンタッチとじしんが同採用率というのは、**バトン渡し型とメガ押し込み型が環境でほぼ均等に使われている**ことを数値が示しています。どちらの型かは持ち物（ペンドラナイト38.5%がメガ型、タスキ22.2%・オボン12.6%・たべのこし11.5%がバトン型に多い）でおおよそ判別できますが、ペンドラーを出してきた段階では型が読めない状態になります。

持ち物分布を見ると、ペンドラナイト（38.5%）が最多ではあるものの、残り61.5%は非メガ石であり、過半数がバトン型または非メガ物理型です。対面した際には「ペンドラナイト＝メガ型」「タスキ/オボン/たべのこし＝バトン型」と持ち物から判断するのが現実的な読み筋になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASようきバトン型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ようき 33.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・バトンタッチ・まもる・きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S最大化でかそく前から先手範囲が広く積みやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型より積む前の火力が劣る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASいじっぱりバトン型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり 31.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・バトンタッチ・まもる・きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ようき型より積む前の火力があり攻撃択も取りやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S最大化できずようき型より先手範囲が狭い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ABわんぱくメガ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく 16.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・じしん・まもる・きゅうけつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B149の物理耐久で物理技を受けながら積める</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S62で弱点タイプに先手を取られやすく後続サポートが薄い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ペンドラーはかそく特性でSを積みながらつるぎのまいでA+2を乗せてバトンタッチで後続に渡す積みバトン型が最多構成です。ようき（33.7%）・いじっぱり（31.8%）の2択でバトン型、わんぱく（16.1%）でメガ進化耐久型に分かれ、持ち物（ペンドラナイト38.5%・タスキ22.2%等）で型を判断できます。弱点はひこう・ほのお・いわ・エスパーの4タイプで、特にひこう技を持つムクホークや高速ほのおタイプへの対処はパーティで用意する必要があります。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [ラグラージのM-3考察](/blog/swampert-analysis-m3/)
- [オーロンゲのM-3考察](/blog/grimmsnarl-analysis-m3/)
