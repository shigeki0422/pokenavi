---
title: '【ポケモンチャンピオンズ】メガラグラージ考察 M-3 使用率7位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率7位のメガラグラージを徹底分析。じしん91.9%・ウェーブタックル73.9%の物理アタッカー型と、クイックターン66.6%の対面操作型を実データで解説。あめ下すいすいS268で環境最速クラスに変貌する天候パ構成まで紹介。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-swampert-m3.png'
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
  <img src="/images/pokemon/pokemon-0260-00.webp" alt="メガラグラージ" />
  <div>
    <h2 style="margin:0 0 8px">メガラグラージ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>　特性（メガ前）: <strong>げきりゅう 75.2%</strong>　メガ後特性: <strong>すいすい</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガラグラージは**使用率7位**を記録。みず/じめん複合により弱点が**くさタイプ1種のみ**という堅固な耐性と、メガ後こうげき150の高い物理火力を兼ね備えます。さらにメガ進化後の特性**すいすい**で、あめ下ではS実数値が最大268（ようき・S32振り換算で268）に倍増し、環境最速クラスの先手を取りながら物理技を押し付けられるのが上位定着の理由です。

特性は**げきりゅう75.2%**が主流（しめりけ24.8%が続く）。メガ前はHP1/3以下でみず技の威力が1.5倍になるげきりゅうを採用し、メガ進化後はすいすいに切り替わる構成が標準です。

---

## なぜ今メガラグラージが使用率7位なのか

### 1. 弱点がくさタイプ1種のみという圧倒的な耐性

みず/じめんの複合は、でんきを**完全無効（×0）**にしながら、ほのお・むし・はがねを半減（×0.5）で受けられます。みず技はじめんの×2でみず×0.5が相殺されて等倍、こおり技はじめんの×2とみず×0.5が相殺されて等倍止まりです。残る**弱点はくさの×2のみ**で、環境上位の物理アタッカーがよく採用するじめん・かくとう・ドラゴン・ほのお等の技がいずれも等倍以下に抑えられます。

### 2. メガ後こうげき150で物理範囲が広い

メガ進化後のこうげきは150。じしん（採用率91.9%）・ウェーブタックル（73.9%）のタイプ一致物理2技で、じめんとみずの広い範囲をカバーします。れいとうパンチ（71.6%）でくさ・ドラゴンへの補完打点も確保でき、3技合わせてほぼ全タイプに等倍以上で打点を通せます。

### 3. あめ下すいすいで対応できる速度帯が一変する

メガ後特性すいすいはあめ状態でSが2倍になります。いじっぱり・S32振りでS実数値122、ようき・S32振りで134。あめ下ではそれぞれ244・268に倍増し、**ようき・S32振りのS268は環境トップクラスの速度帯**です。アローラキュウコンのあまごいと組み合わせた天候パとして採用されるケースが多く、あめ展開下では高速物理アタッカーとして全抜きを狙えます。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">110</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">110</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">635</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

こうげき150・ぼうぎょ110・とくぼう110と物理攻守が高水準。すばやさ70はあめなし環境では控えめで、ようき・S32振りでもS134と高速勢には及びません。あめ下すいすいが前提の構成であれば速度問題は解消されますが、あめのない状態では上から殴られる展開が多い点は意識が必要です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="じめん" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効（×0）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

じめんがでんきを完全無効にし、みずのこおり×0.5とじめんの×2が相殺してこおりは等倍止まりです。みず技も同様にみず×0.5・じめん×2で相殺されて等倍になります。**弱点はくさの×2のみ**という優秀な耐性で、環境上位の物理アタッカーが使うノーマル・かくとう・ほのお・じめん・ドラゴン等の技をすべて等倍以下で受けられます。

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
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じしん</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">100</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">91.9%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ウェーブタックル</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">73.9%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>れいとうパンチ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">71.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>クイックターン</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">60</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">66.6%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ステルスロック</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">23.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>あくび</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">21.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7.9%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はたきおとす</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">65</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7.3%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>みがわり</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>どくづき</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">80</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3.6%</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布はいじっぱり56.4%・ようき20.5%が主流で、A特化か素早さを確保するかで分かれます。

### 型1: いじっぱり物理アタッカー型（最多採用）

**性格採用率: いじっぱり 56.4%**（物理AT型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0260-00.webp" alt="メガラグラージ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HAいじっぱり物理型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（75.2%）※メガ後すいすい<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率38.7%。AとSを最大化）<br>
<strong>持ち物:</strong> ラグラージナイト（75.2%）/ オボンのみ（14.8%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ウェーブタックル<br>
・れいとうパンチ<br>
・クイックターン / ステルスロック
</div>
</div>
</div>

**強み:**

いじっぱりA32振りのA実数値は222。じしんはほのお・どく・はがね・でんきへ、ウェーブタックルはいわ・ひこう・ほのおへと広い範囲を高火力でカバーします。れいとうパンチでくさタイプとドラゴンの弱点を補完でき、3技合わせて環境上位のほとんどに等倍以上の打点が通ります。クイックターン採用個体はみずタイプ一致の打点を出しながら交代できるため、サイクル戦で有利対面を作りやすいのもポイントです。あめ下すいすいでS244（いじっぱり・S32振り）と高速帯に入り、ラグラージナイト採用の75.2%はメガ進化前提の構成です。

**弱み:**

ようき型と比べてS実数値が低く（いじっぱりS32でS122）、あめなし状態では素早さ帯が中低速で上から殴られます。くさタイプ（×2弱点）への後出しはれいとうパンチで対応する必要がありますが、くさ技を先に受けると大ダメージになるためにくさ枠には基本的に受け出しできません。

---

### 型2: ようき高速型（2番目に多い構成）

**性格採用率: ようき 20.5%**（あめなし状態でもS確保を優先する型）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0260-00.webp" alt="メガラグラージ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようき高速型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（75.2%）※メガ後すいすい<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（採用率9.4%。AとSを最大化）<br>
<strong>持ち物:</strong> ラグラージナイト（75.2%）/ オボンのみ（14.8%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ウェーブタックル<br>
・れいとうパンチ<br>
・クイックターン / ステルスロック
</div>
</div>
</div>

**強み:**

ようきS32振りのS実数値は134。あめなし状態でも素早さに余裕が生まれ、あめ下すいすいではS268と**いじっぱり型のS244を上回る速度帯**に入ります。あめ展開を軸にしない構成や、素早さ競争が厳しい環境で採用されます。

**弱み:**

いじっぱり型と比べてA実数値が202と低くなる（いじっぱりA32は222）。A実数値で約10%の差が生じ、2発必要な相手への確定数に影響するケースがあります。火力で劣る分、あめ展開の組み合わせが前提になりやすい型です。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

みず/じめん複合は弱点がくさの1タイプのみで、環境上位の物理アタッカーの主力技を等倍以下に受けられます。一方、くさ技を持つ相手と素早さで上回る高速特殊アタッカーが苦手です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが等倍で通る。ガブリアスのじしん（採用率99.2%）はこちらのじめんタイプで等倍。ウェーブタックルで×2の弱点を突ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ウェーブタックルが等倍、じしんもひこう技は無効化するため等倍。メガリザードンXはウェーブタックルが×0.5だが、じしんで×2と刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2と刺さる。相手のインファイトは等倍。ただしメガルカリオの素早さ（メガ後S112、ようき・S32でS実数値高水準）次第では先手を取られる場合がある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のじしんはこちらに等倍で通る。こちらのウェーブタックルは×2で弱点を突ける。ただし高HPでウェーブタックルの反動も考慮すると削り合いになる</td>
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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技（×2弱点）を上から通される。S123と高速でこちらの素早さを大きく上回るため、あめなし状態では先手を取れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチで×2の弱点を突けるが、先手を取られるため後続から対処するのが基本。あめ下すいすいならS268でマスカーニャを抜けるため、あめ展開前提で上から潰す選択肢もある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S100でこちら（S70）より速く、ちょうのまいで特攻・素早さを積まれると特殊技での削りが蓄積する。ほのおはこちらに等倍止まりだが、積んだ後の特殊打点が重い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんで×2の弱点を突ける。ただし先にちょうのまいを積まれると特殊耐久が追いつかないため、積む前にじしんで削るか、いわ技（×4）持ちの後続で処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S100でこちらより速く、でんきの弱点はじめんタイプで無効化されているためウェーブタックルが刺さりにくい（等倍）。れいとうパンチで対処したいが先手を取られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチが×4で弱点を突ける。あめ下すいすいならS268でカイリューを抜ける。あめなしではひこう・こおり技持ちの後続に引いて対処する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン">
    <div class="name">アローラキュウコン</div>
    <div class="rate">天候パ軸</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あまごいであめを展開し、すいすいを発動。天候パの核として機能</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">速い地面物理枠。メガラグラージが苦手なくさ枠への打点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうタイプ枠。くさ技をひこうで半減し、メガラグラージが苦手な相手をカバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">特殊枠補完</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリー。メガラグラージが物理で押し切れない高耐久に特殊打点を当てる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0227-00.webp" alt="エアームド">
    <div class="name">エアームド</div>
    <div class="rate">くさ対策枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ×0.25で受けられるひこう/はがね枠。メガラグラージの唯一の弱点くさをケア</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガラグラージはくさ以外の弱点がなく、多くの物理攻撃を等倍以下で受けられるため、受け出し役として柔軟に動けます。残り5体で以下を補います。

1. **あめ展開役**: アローラキュウコン等のあまごい要員でメガラグラージのすいすいを発動し、高速物理アタッカーとして機能させる
2. **くさ対策**: エアームド（くさ×0.25）・リザードン（ひこー型ならくさ半減）など、くさ技を受けられる枠を1体以上用意する
3. **特殊打点補完**: メガラグラージは物理一辺倒のため、物理耐久が高い相手に特殊技で対処できる枠（アシレーヌ等）が助けになる
4. **サイクル補完**: クイックターンで対面操作しながら有利対面を作り、後続の高速アタッカーに繋ぐ運用が基本

---

## データ分析①：技採用率が示す「単純破壊」と「サイクル運用」の二軸

メガラグラージの技採用率を並べると、火力技とサイクル系技が混在した特徴的な分布が見えます。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| じしん | 攻撃（タイプ一致） | 91.9% | 主力打点 |
| ウェーブタックル | 攻撃（タイプ一致） | 73.9% | 高火力打点 |
| れいとうパンチ | 攻撃（補完） | 71.6% | くさ・ドラゴン対策 |
| クイックターン | 攻撃＋交代 | 66.6% | 対面操作 |
| ステルスロック | 設置 | 23.0% | 後続の削りを蓄積 |

注目点はクイックターンが66.6%と3位に入ることです。じしん・ウェーブタックルの2タイプ一致高火力攻撃と並ぶ採用率で、「ダメージを出しながら交代できる」点が重視されています。メガラグラージが高い物理耐性を持つため、相手の弱い打点を受け出してからクイックターンで有利対面を作り、後続のエースに繋ぐサイクル役としての運用が約2/3の個体で共通していると言えます。

一方、ステルスロック23.0%は少数派ですが、設置技を持つ個体はクイックターンと組み合わせて「ステルスロック設置→クイックターンで有利対面を作る」2段階の展開を狙います。持ち物採用率ではオボンのみ14.8%・たべのこし5.0%の回復系実が計19.8%あり、これらはサイクル持続を重視した構成と対応しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HAいじっぱり物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 56.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じしん・ウェーブタックル・れいとうパンチ・クイックターン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A実数値222の高火力で広範囲をカバー。あめ下S244</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">あめなし状態でS122と低速。くさ枠に受け出し困難</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ASようき高速型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 20.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">じしん・ウェーブタックル・れいとうパンチ・クイックターン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">あめなし状態でS134。あめ下S268で環境トップ帯</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A実数値202といじっぱり型より約10%低い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガラグラージはみず/じめん複合の弱点1タイプという堅固な耐性と、こうげき150の高い物理火力を兼ね備えた汎用性の高い物理アタッカーです。じしん・ウェーブタックル・れいとうパンチの3技で広範囲をカバーし、クイックターンでサイクルも回せるため、単なる火力枠にとどまらない対面操作役も担えます。

最大の特徴はアローラキュウコンとの天候パで、あめ下すいすいによりS実数値が最大268に倍増して環境最速クラスに変貌します。くさタイプへの対策はパーティ単位でケアする前提で、エアームドやリザードンなどのひこう枠をセットで採用するのが基本戦術です。

---

## 関連記事

- [使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [メガラグラージの弱点くさを担うマスカーニャのM-3考察](/blog/meowscarada-analysis-m3/)
- [天候パで組むアローラキュウコンのM-3考察](/blog/alolan-ninetales-analysis-m3/)
