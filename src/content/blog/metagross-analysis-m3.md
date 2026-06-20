---
title: '【ポケモンチャンピオンズ】メガメタグロス考察 M-3 使用率10位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率10位のメガメタグロスを徹底分析。サイコファング74.8%・バレットパンチ73.8%の物理アタッカー型を実データで解説。かたいツメ補正による接触技強化と先制打点の組み合わせ、環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-metagross-m3.png'
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
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" />
  <div>
    <h2 style="margin:0 0 8px">メガメタグロス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">10位</strong>　特性（メガ前）: <strong>クリアボディ 99.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガメタグロスは**使用率10位**を記録。はがね/エスパーという**弱点がほのお・じめんの2タイプのみ**の優秀な耐性を持ち、メガ進化後はこうげき145・ぼうぎょ150・とくぼう110・すばやさ110と全方位で高水準な種族値を備えます。特性かたいツメにより接触技の威力が1.3倍に高まり、サイコファング・じしん・アイアンヘッドといった物理技が軒並み強化されます。

---

## なぜ今メガメタグロスが使用率10位なのか

### 1. 弱点がほのお・じめんの2タイプのみ

はがね/エスパーの複合タイプは、はがねの豊富な耐性とエスパーが重複して組み合わさり、**弱点がほのお（はがね×2・エスパー×1）・じめん（はがね×2・エスパー×1）の2タイプのみ**に絞られます。かくとう（はがね×2・エスパー×0.5＝等倍）・ゴースト（はがね×0.5・エスパー×2＝等倍）・あく（はがね×0.5・エスパー×2＝等倍）はいずれも等倍止まりで、本来エスパータイプが弱点とするタイプをはがねが打ち消します。どくはがねが無効化するため、毒技を一切受けません。

### 2. かたいツメ補正で接触技が1.3倍に強化

メガ進化後の特性かたいツメは、接触判定のある技の威力を1.3倍にします。採用率上位のサイコファング（74.8%・威力80）・じしん（69.9%・威力100）・アイアンヘッド（36.3%・威力80）はいずれも接触技のため、補正後の実質威力はそれぞれ104・130・104相当になります。こうげき145と組み合わせると、素の種族値以上の火力を接触技全般に発揮できます。

### 3. バレットパンチによる先制打点とS110の中速帯制圧

バレットパンチ（採用率73.8%・優先度+1）により、スカーフなし環境の高速勢にも先制打点を入れられます。加えてメガ後のすばやさ110は、環境上位の中速帯（S80〜100前後）を上から制圧できる水準で、ようき採用60.3%でS実数値169に達し、いじっぱり採用36.4%のA実数値182と合わせて火力・速度の両面を高水準に保てます。

---

## 基本スペック

### 種族値（メガ進化後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#6b7280"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:72.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">145</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">150</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">110</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

こうげき145・ぼうぎょ150はいずれも最上位クラスの数値で、物理耐久と物理火力を高次元で両立しています。とくぼう110・すばやさ110もメガ進化前（とくぼう90・すばやさ70）から大幅に上昇しており、特殊方面の被弾にも粘れる耐久と、中速帯を上から制圧できる速度を得ます。HPは80と低めで、ほのお・じめん弱点から一撃で持っていかれないためにH方向のEVが一定数採用される理由です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="エスパー" />
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
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー（×0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

かくとう（はがね×2・エスパー×0.5＝等倍）・ゴースト（はがね×0.5・エスパー×2＝等倍）・あく（はがね×0.5・エスパー×2＝等倍）は2タイプの倍率が打ち消し合い等倍止まりです。エスパーはがねへの2タイプ両方で半減し×0.25の超耐性になります。**弱点はほのお・じめんの2タイプのみ**ですが、いずれも環境物理アタッカーの主力技（ガブリアスのじしん99%超採用等）に頻出するため、対面で受け切るのではなくパーティ単位でケアする必要があります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>サイコファング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">74.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致接触技。かたいツメで実質110。リフレクターを破壊する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。タイプ一致接触でかたいツメ補正あり。フェアリー・こおりへの先制打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">69.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">接触技。かたいツメで実質130。ほのお・でんき・はがねへの補完打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">62.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">接触技。かたいツメで実質97。ドラゴン・くさへの補完。ガブリアス等に有効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致接触技。かたいツメで実質104。フェアリー・こおりへの安定打点。30%ひるみ</td>
</tr>
</tbody>
</table>
</div>

特性はメガ前の**クリアボディ99.4%**が主流で、相手からの能力低下を無効化します。メガ進化後はかたいツメに変化するため、クリアボディはメガ進化前（交代直後など）の能力低下回避のみに機能します。ライトメタル（0.6%）は重さ関連技への対策で採用率は極めて低水準です。

---

## 主要型の解説

性格分布はようき60.3%・いじっぱり36.4%の2択で、S振りを優先するようき型と火力を最大化するいじっぱり型に二分されます。EV最多採用はH2-A32-S32（42.2%）で、ようき型でS実数値169を確保しつつA最大振りとH2を割り当てる型です。

### 型1: ようきH2-A32-S32型（最多採用）

**性格採用率: ようき 60.3%**（EV最多H2-A32-S32・採用率42.2%と組み合わせの主軸）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ようきH2-A32-S32型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（メガ前99.4%）→メガ後かたいツメ<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率42.2%）<br>
<strong>持ち物:</strong> メタグロスナイト（96.8%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・バレットパンチ<br>
・じしん<br>
・れいとうパンチ
</div>
</div>
</div>

**強み:**

ようきA32S32でS実数値169、A実数値182を確保します。S169はS102のガブリアスや、S110のほとんどの中速帯を上から制圧できる水準です。かたいツメ補正込みのサイコファング（実質威力110）・じしん（実質130）に加え、バレットパンチ（優先度+1）で削れた高速勢に先制打点を入れられます。れいとうパンチでドラゴンタイプや飛行タイプにも対応し、じしんのほのお・でんき・はがねへの打点と合わせて4技で広い範囲をカバーします。いじっぱり型（A実数値200）と比べてA実数値で約10%劣りますが、S169で抜ける相手（S102〜110台）への先制を維持できる点がようき型の採用理由です。

**弱み:**

C方向は補正下降のため特殊打点はほぼ出せません。HPは80・EV2振りにとどまるため、ほのお・じめん弱点の一撃耐性は高くなく、ガブリアスのじしんや使用率上位の炎技を先に受けると一撃圏内になるケースがあります。いじっぱり型と比べてAが約10%低く、2発かかる相手を1発で倒せないケースも生じます。

---

### 型2: いじっぱりH12-A22-S32型（2番目に多い構成）

**性格採用率: いじっぱり 36.4%**（EV H12-A22-S32・採用率5.8%が代表的な配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">いじっぱりH12-A22-S32型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> クリアボディ（メガ前99.4%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H12 A22 S32（採用率5.8%）<br>
<strong>持ち物:</strong> メタグロスナイト（96.8%）
</div>
<div>
<strong>技構成:</strong><br>
・サイコファング<br>
・バレットパンチ<br>
・じしん<br>
・れいとうパンチ / アイアンヘッド
</div>
</div>
</div>

**強み:**

いじっぱりA32振りのA実数値200はようき型の182と比べて約10%高く、かたいツメ補正込みのじしんやサイコファングで2発かかる耐久型を1発圏内に入れられるケースが増えます。S32はようき同様のS振りが多く、いじっぱりS32のS実数値は154で、S80〜100台の中速帯は引き続き上から制圧できます。バレットパンチの先制火力もA200基準で高くなるため、削れた高速勢への確定数がようき型より有利です。

**弱み:**

S154はようき型の169より低く、S102のガブリアス（ようきS実数値169）や、S110台のポケモンには先手を取られます。ようき型が上から倒せる相手に後手を踏む局面では、バレットパンチか先手を取れる味方で補う必要があります。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

はがね/エスパーは弱点がほのお・じめんの2タイプのみで多くの攻撃を等倍以下に抑えますが、弱点2タイプは環境物理アタッカーの主力技に頻出します。S110で中速帯には先手を取りやすい一方、高速勢や炎・地面打点を持つ相手には注意が必要です。

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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがかくとう/はがねに等倍×等倍＝等倍で通り、メガルカリオのインファイトはこちらにかくとう×2・エスパー×0.5＝等倍止まり。メガ後S110＞メガルカリオS145には先手を取られるが、バレットパンチで先制打点を入れつつじしんで削れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチがドラゴン/ひこうに×4。S110＞カイリューS100で先手かられいとうパンチを入れられる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0143-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カビゴン（圏内）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S110＞カビゴンS30台で先手。じしんがノーマルに等倍・サイコファングも等倍で通り、ぼうぎょ150でカビゴンの物理打点も耐えやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（はがね）がみず/ひこうに×0.25の超耐性で打点にならない。れいとうパンチは等倍通過。S110＞ギャラドスS81で先手かられいとうパンチを入れられるが、相手のじしん採用率次第では逆に弱点を突かれる</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のほのお・じめんを×2で突ける物理・特殊アタッカーが主な苦手相手です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99%超）がじめん×2でこちらの弱点を突く。ようきS169で互いに同速になるが、ガブリアスのじしんA130＋タイプ一致は先に受けると致命打になりやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこうタイプ（カイリュー・アーマーガア等）を同伴し、ガブリアスの前に引く。その後こちらかられいとうパンチやバレットパンチで削る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（5位圏内）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技（タイプ一致・晴れ補正）がほのお×2でこちらの弱点を突く。メガリザードンYのS実数値はようきS32で167前後と拮抗しており、上から炎技を受けると一撃圏内になりやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんで弱点を突けるが、ひこうタイプのリザードンYにはじしんが等倍で通らない（ひこう無効）。みず技を持つ後続で対処するか、バレットパンチで先制削りを入れてから後続に引く</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（9位）※高速個体
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後S145でこちらのS110より速く、つるぎのまい後のインファイトはかくとう等倍でも一撃圏内になりえる。しんくうは（優先度+1）で先制削りも受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（優先度+1）でインファイト後のBDダウンを活かして削る。じしんでの返しも等倍で通るため、先にバレットパンチで削った後続でじしんを入れる</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。メタグロスが苦手なほのお枠へのじしん・いわ技で対抗。互いのじしんが弱点と相性補完になる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー">
    <div class="name">カイリュー</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじしんを無効化。ガブリアスのじしん対策に。メタグロスのほのお弱点もカイリューが受ける役割を担える</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじしんを無効化する枠。メタグロスのじめん弱点をカバーしつつ、相手のはがね・くさへの炎技打点を担う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこう・みずでほのお・じめん両方をケアできる枠。メタグロスの2つの弱点を1体でカバーする</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ">
    <div class="name">メガルカリオ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">かくとう/はがねでほのお弱点を受けつつ、バレットパンチの先制打点を共有。物理アタッカー同士で役割が重なるが高速枠としての補完</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガメタグロスは物理耐久と接触技強化の物理アタッカーとして機能しますが、弱点のほのお・じめんが環境上位の主力技に多く、パーティ単位でのカバーが必要です。

1. **じめん対策**: ひこうタイプ（カイリュー・リザードン・ギャラドス）でガブリアスのじしん等を無効化する枠
2. **ほのお対策**: みず・いわ技を持つポケモンでリザードン等の炎技を受ける枠（ギャラドスはみず+ひこうで両方対応可）
3. **高速枠の補完**: S110で抜けない高速勢（S120以上）にはバレットパンチや後続の先制技で対処する設計
4. **物理受け突破**: ぼうぎょ150により物理アタッカーの受け役が困難になるため、特殊アタッカーや変化技持ちを崩し役として同伴する

---

## データ分析①：技採用率から読み取る「接触技4本」構成の必然性

メガメタグロスの技採用率上位5技を並べると、全て物理・接触技であることが分かります。

| 技 | 接触判定 | かたいツメ補正後実質威力 | 採用率 |
|---|---|---|---|
| サイコファング | 接触 | 110（85×1.3） | 74.8% |
| バレットパンチ | 接触 | 52（40×1.3） | 73.8% |
| じしん | 接触 | 130（100×1.3） | 69.9% |
| れいとうパンチ | 接触 | 97（75×1.3） | 62.5% |
| アイアンヘッド | 接触 | 104（80×1.3） | 36.3% |

5技全てがかたいツメの恩恵を受ける接触技です。こうげき145という高い素の攻撃種族値に1.3倍補正が乗ることで、等倍でもサイコファング・れいとうパンチ・アイアンヘッドが実質100超相当の威力になります。

特に注目されるのはじしんの採用率69.9%です。じしんははがね/エスパータイプのメタグロスが本来弱点とするほのお・でんき・はがねに打点を持てる技で、タイプ一致でない代わりにかたいツメ補正で実質130の威力を出せます。アイアンヘッドと採用率が約33ポイント差（じしん69.9%・アイアンヘッド36.3%）なのは、アイアンヘッドでカバーできるフェアリー・こおりへの打点をバレットパンチで先制補完できるのに対し、じしんにしかできないほのお・でんき・はがねへの打点は代替技がないためです。

性格採用率ようき60.3%・いじっぱり36.4%の拮抗は、「S169で中速帯を上から制圧する」とうき型と「A200でより高い火力を確保する」いじっぱり型の二択が環境の好みで割れている実態を示しています。いずれもS32最大振りが主流（最多EV採用がH2-A32-S32）なことから、**S最大確保は全型共通の前提**となっており、残り枠のH/Aをどこに割り振るかが型の分岐点です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ようきH2-A32-S32型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">EV採用率42.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">サイコファング・バレットパンチ・じしん・れいとうパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S169で中速帯（S110以下）を先制制圧できる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型よりAが約10%低く確定数が劣るケースがある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">いじっぱりH12-A22-S32型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">EV採用率5.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">サイコファング・バレットパンチ・じしん・れいとうパンチ / アイアンヘッド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A実数値200で1発圏内に入れられる相手が増える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S154でようき型が抜けるS102〜110台に先手を取られる</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガメタグロスははがね/エスパーの優秀な耐性（弱点はほのお・じめんの2タイプのみ）と、メガ後こうげき145・ぼうぎょ150・すばやさ110の高水準な種族値に、かたいツメによる接触技全般の1.3倍強化が加わった物理アタッカーです。採用率上位5技が全て接触技という珍しい構成で、技の選択がそのままかたいツメ補正の恩恵を最大化する方向に集約されています。

弱点のほのお・じめんはいずれも環境物理・特殊アタッカーの主力技に多く、ガブリアスのじしんやリザードンの炎技はパーティ単位でカバーする必要があります。ひこうタイプ（カイリュー・リザードン・ギャラドス）を同伴してじめん・ほのおを無効化・軽減しつつ、メガメタグロス自身はS110の先制制圧とバレットパンチの先制打点で中速帯を制圧するのが基本戦術です。

---

## 関連記事

- [使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [天敵のリザードンのM-3考察](/blog/charizard-y-analysis-m3/)
- [パートナー候補 カイリューのM-3考察](/blog/dragonite-analysis-m3/)
