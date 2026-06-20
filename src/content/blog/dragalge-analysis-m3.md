---
title: '【ポケモンチャンピオンズ】メガドラミドロ考察 M-3 使用率29位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率29位のメガドラミドロを徹底分析。クイックターン85.7%・りゅうせいぐん84.2%の対面操作型と、どくびし39.3%の毒撒き型を実データで解説。さいせいりょくによるサイクル戦・とくぼう163の特殊耐久・環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-dragalge-m3.png'
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
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" />
  <div>
    <h2 style="margin:0 0 8px">メガドラミドロ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">29位</strong>　特性: <strong>てきおうりょく 72.6%</strong>（メガ後: さいせいりょく）
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガドラミドロは**使用率29位**を記録。メガ進化後に特性が**さいせいりょく**（交代で引っ込むたびにHPが最大値の1/3回復）に変わり、サイクル戦を繰り返しながら自己回復できる点が最大の特徴です。

クイックターン採用率85.7%で対面操作を行いながら回復を積み重ね、とくぼう163という突出した特殊耐久で特殊技を受け続けます。S44と環境最低水準の素早さを逆手に取り、**なまいき（S↓）・おだやか（D↑）で耐久を最大化**したサイクル特化の構成が主流です。

---

## なぜ今メガドラミドロが29位なのか

### 1. さいせいりょく＋クイックターンで毎ターン回復しながら対面操作

メガ進化後の特性さいせいりょくは、「引っ込むたびにHPの1/3を回復」するためクイックターンとの組み合わせが非常に強力です。クイックターン（採用率85.7%）でみずタイプ技を当てながら自分が交代し、引っ込む際にHP1/3を回復します。この動作を繰り返すことで、攻撃しながらHP管理を続けられます。消耗戦・サイクル戦においては相手より長く動き続けられる疑似的な持続力が生まれます。

### 2. とくぼう163で特殊アタッカーを安定して受けられる

メガ後のとくぼう163は環境随一の水準で、特殊アタッカーの技を複数回受けてもHPが残ります。どく/ドラゴン複合により、フェアリータイプの技を**完全に無効化**できるため、環境上位のフェアリー特殊アタッカーへ後出しできます。くさ・むし・はがね技も0.5倍に抑え、多くの攻撃をとくぼう163の壁で受け流します。

### 3. どくどく・どくびし・クイックターンで状態異常と対面操作を同時に担う

どくどく（採用率45.0%）とどくびし（採用率39.3%）の両方が採用圏に入り、相手に毒ダメージを蓄積させながらクイックターンで後続に有利な対面を作ります。どくびし採用型は場に残ることで交代してくる相手ポケモンにも毒を広げられ、サイクルを回しながらじわじわとHPを削る戦い方ができます。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+15</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">132</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:81.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">163</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:22%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">44</span>
    <span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">594</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

とくぼう163・ぼうぎょ105の耐久に全振りした反面、HP65は低い部類でS44は環境最低水準。特殊耐久は突出しているが、高速勢に先手を取られる前提で組まれたステータス配分です。とくこう132はヘドロウェーブ・りゅうせいぐんの打点として十分で、火力役と耐久役を兼ねられます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ドラゴン" />
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
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー
  </td>
</tr>
</tbody>
</table>
</div>

どくタイプがフェアリーへの無効を生み出し、ドラゴンタイプの最大の弱点を消しています。くさ・むし・はがねは2タイプ合計で0.5倍に収まります。一方、弱点はエスパー・じめん・こおり・ドラゴンの4タイプで、いずれも環境上位が採用する主力技（ガブリアスのじしん採用率99%超・ドラゴン技）に多く含まれます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">85.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に強制交代。さいせいりょくでHP1/3回復しながら対面操作</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致最大火力。使用後C2段階ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくどく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">もうどく付与。サイクルを回しながら削りを蓄積</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致どく技。10%でどく状態付与</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">39.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1枚でどく・2枚でもうどく。交代してくる相手に毒を広げる</td>
</tr>
</tbody>
</table>
</div>

クイックターンとりゅうせいぐんの2技がほぼ固定枠（85%超）で、残り2枠でどくどく・ヘドロウェーブ・どくびしの中から選ぶ構成が主流です。どくどくとヘドロウェーブで継続ダメージを稼ぐ型と、どくびしで交代先にも毒を広げる型に分かれます。

---

## 主要型の解説

性格分布はなまいき26.4%（S↓D↑）・おだやか20.8%（D↑A↓）が上位2つで、どちらもD方向に補正をかける耐久型です。S44はなまいきでさらに下がりますが、環境上位に後手を取られることが前提のため、素早さへの投資は見られません。

### 型1: H32-B2-D32 なまいき耐久型（最多採用）

**EV採用率: H32-B2-D32 13.7%**（最多EV配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">H32-D32 なまいき耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てきおうりょく（72.6%）※メガ後さいせいりょく<br>
<strong>性格:</strong> なまいき（D↑ S↓）<br>
<strong>EV:</strong> H32 B2 D32（採用率13.7%）<br>
<strong>持ち物:</strong> ドラミドナイト（97.9%）
</div>
<div>
<strong>技構成:</strong><br>
・クイックターン<br>
・りゅうせいぐん<br>
・どくどく or どくびし<br>
・ヘドロウェーブ
</div>
</div>
</div>

**強み:**

HPとDに最大振りすることで特殊耐久を最大化し、さいせいりょく回復と合わせた持続力がこの型の最大の強みです。なまいき補正によりD実数値がさらに上がり、とくぼう163のベースと合わせて特殊アタッカーの技を複数回受けられます。フェアリー技を無効化できるため、環境上位のフェアリー特殊アタッカーを安定して受ける役割を担います。クイックターンで引っ込むたびにHP1/3を回復するため、相手の攻撃を受けても回復サイクルでHPを維持できます。

**弱み:**

S44はなまいきでさらに下がり、事実上全ての環境ポケモンに後手を取られます。エスパー・じめん・こおり・ドラゴンの4タイプ弱点はいずれも環境上位が採用する技のタイプで、弱点を突かれると一撃の重さを引き受ける覚悟が必要です。HP65の低さから、さいせいりょく回復量も1回あたり約21（最大HP実数値の1/3）と数値は高くないため、HPが低い状態での後出しは危険です。

---

### 型2: H32-B2-C32 おだやか特殊アタッカー耐久型

**EV採用率: H32-B2-C32 9.6%**（2番目に多いEV配分）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0691-00.webp" alt="メガドラミドロ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">H32-C32 おだやか攻守バランス型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てきおうりょく（72.6%）※メガ後さいせいりょく<br>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 B2 C32（採用率9.6%）<br>
<strong>持ち物:</strong> ドラミドナイト（97.9%）
</div>
<div>
<strong>技構成:</strong><br>
・クイックターン<br>
・りゅうせいぐん<br>
・ヘドロウェーブ<br>
・どくどく or どくびし
</div>
</div>
</div>

**強み:**

CにEVを最大振りすることでとくこう実数値が上がり、りゅうせいぐん・ヘドロウェーブの打点がH32-D32型より高くなります。おだやか補正でDも確保しつつ、とくこう132をさらに活かした攻撃参加ができます。H32-D32型との差は、火力で能動的に削れるかどうかで、りゅうせいぐんで確定圏に入る相手が増えます。

**弱み:**

H32-D32型と比べてとくぼう補正を乗せていないため、D実数値はおだやか補正の分だけ上乗せされますが、EV振りはD側にないため特殊耐久の純粋な数値はH32-D32型より低くなります。「受けに使うならなまいきH32-D32」「打点を出しながら受けるならおだやかH32-C32」という棲み分けです。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

どく/ドラゴン複合は**フェアリーを無効化**し、くさ・むし・はがね技を半減で受けますが、エスパー・じめん・こおり・ドラゴンは弱点です。S44のため基本的に後手を取られる前提で、特殊耐久とさいせいりょく回復で戦います。

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
    アシレーヌ（みず/フェアリー）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース等フェアリー技を完全無効化。クイックターン（みず）・りゅうせいぐん（ドラゴン）でともに等倍以上の打点を持つ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    マスカーニャ（くさ/あく）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技を0.5倍に半減。あく技も等倍止まりで受けられる。とくぼう163で複数回受けながらさいせいりょく回復を繰り返せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    ガブリアス（ドラゴン/じめん）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">✕ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2）・ドラゴン技（ドラゴン×2）がともに弱点。物理型のためぼうぎょ105で一定受けられるが、A130の一致じしんは脅威。後出しは基本できない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    リザードン（ほのお/ひこう）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・ひこう技ともに等倍で、とくぼう163でそれなりに受けられる。ただしメガリザードンYの特殊火力はとくこうが高く、複数回被弾すると消耗する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    カバルドン（じめん）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">✕ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがじめん×2で弱点。耐久型のカバルドンはりゅうせいぐんを複数回受けられる可能性があり、あくびで流される展開が多い</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）・ドラゴン技がいずれも×2弱点。物理アタッカーのためぼうぎょ105で受けられる場面もあるが、一致じしんの打点は脅威</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプ（リザードン・ギャラドス等）でじしんを無効化し、ガブリアスの前に引いて処理する。ドラミドロはガブリアスと対面させない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん×2）が弱点で、高いぼうぎょ・HPでりゅうせいぐんのCダウンを乗り越えられる。あくびでこちらのサイクルを崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技を持つ枠でカバルドンに弱点を突く。ドラミドロのどくびしを活かし毒にしてからサイクルを消耗させる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    高速エスパー枠（エーフィ等）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー技が×2弱点。S44のため先制されることが多く、エスパー技を上から打たれると大ダメージを受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく複合や高いとくぼうを持つ枠を先に出し、エスパー枠を消耗させてからドラミドロを動かす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    こおり複合アタッカー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり技が×2弱点。とくぼう163で特殊こおり技は複数回受けられる場合もあるが、物理こおり技はぼうぎょ105でもダメージが蓄積する</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプ（こおりを半減）やほのおタイプでこおり枠をあらかじめ処理する</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。ドラミドロが苦手なガブリアス同士でじしんを撃ち合い相殺、ドラミドロを温存できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">ひこう無効枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうタイプでじしんを無効化。ドラミドロが最も苦手なじめん弱点をカバー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">ひこう無効枠</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ひこうでじしんを無効化しつつ、どく弱点のくさタイプにも強い</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">フェアリー無効連携</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ドラミドロのフェアリー無効を活かし、フェアリー系の技をドラミドロで全て引き受けてアシレーヌの苦手を補う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">高速アタッカー</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S123の高速枠。ドラミドロが後手を踏む相手を上から処理し、クイックターンで作った有利対面を活かす</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガドラミドロはフェアリー無効・さいせいりょく回復・クイックターンによる対面操作を軸にしたサイクル戦が得意です。残り5体で以下を補います。

1. **じめん対策**: ひこうタイプ（リザードン・ギャラドス）でガブリアスのじしんを無効化する枠。これがないとじめん弱点のドラミドロを安全に動かせません
2. **高速アタッカー**: S44のドラミドロが先手を取れないため、クイックターンで対面を作った後に上から殴るS100超の高速枠（マスカーニャ等）
3. **エスパー対策**: エスパー×2弱点をカバーするあく複合や高耐久枠でエスパーポケモンを処理する役割
4. **どくびし連携**: どくびしを採用した場合、どくが入った相手に対してクイックターンで交代を促しどくダメージを蓄積させる動線を用意する

---

## データ分析①：クイックターン85.7%が示すサイクル特化の徹底

メガドラミドロの技採用率から、このポケモンの役割が「攻撃で削るアタッカー」ではなく「さいせいりょく回復を繰り返すサイクル役」に徹していることが読み取れます。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| クイックターン | 対面操作 | 85.7% | さいせいりょく回復＋後続有利対面 |
| りゅうせいぐん | 攻撃 | 84.2% | タイプ一致最大火力 |
| どくどく | 変化 | 45.0% | もうどく付与・削り蓄積 |
| ヘドロウェーブ | 攻撃 | 39.4% | タイプ一致どく技 |
| どくびし | 変化 | 39.3% | 場への毒撒き |

注目すべきはクイックターン85.7%という高い採用率です。クイックターンは「みずタイプの攻撃技として威力を出しながら、使用後に自分が引っ込む」技で、引っ込む際にさいせいりょくが発動してHP1/3を回復します。つまり**攻撃しながら自己回復する**一石二鳥の動きが可能で、サイクル戦においてはクイックターンを使うたびにHPを回復しながら対面を有利に操作できます。

また、どくどく45.0%とどくびし39.3%の両方が高い採用率を保っており、合計すると84.3%の個体が何らかの毒付与手段を持っています。りゅうせいぐん84.2%もほぼ固定で採用されているため、**「クイックターン+りゅうせいぐん+どくどくorどくびし」の3枠がほぼ固定**で、最後の1枠にヘドロウェーブ（39.4%）か別の変化技を入れる構成が実態です。

持ち物採用率97.9%がドラミドナイトと極めて集中していることも、この型の「メガ進化ありきのさいせいりょくサイクル」という役割をデータが明確に示しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">H32-D32 なまいき耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">13.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なまいき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">クイックターン・りゅうせいぐん・どくどく・どくびし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D補正＋H32でとくぼう最大化。フェアリー特殊技を最も安全に受けられる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">とくこうに振らないため打点が低く、相手の高耐久を削り切れない場面がある</td>
  </tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">H32-C32 おだやか攻守型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">クイックターン・りゅうせいぐん・ヘドロウェーブ・どくどく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C32振りでとくこう132を活かした攻撃参加が可能。りゅうせいぐん・ヘドロウェーブの確定圏が広がる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D方向のEV振りがない分、なまいき型より特殊耐久の実数値は下がる</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガドラミドロはさいせいりょく＋クイックターンによるサイクル戦特化型で、M-3で29位という順位はフェアリー技を無効化できる特殊耐久枠として安定した需要があることを示しています。

クイックターン85.7%・りゅうせいぐん84.2%・どくどく45.0%・どくびし39.3%というデータは、このポケモンが「攻撃→交代回復→再度後出し」のサイクルを繰り返す役割に徹していることを明確に示しています。S44の低速は割り切り、とくぼう163というトップクラスの特殊耐久と特性さいせいりょくを軸にした独自の立ち回りが環境での居場所を作っています。

弱点はじめん・エスパー・こおり・ドラゴンの4タイプと多く、特にじめんを持つガブリアスは弱点が2つ重なるため直接対面は避けるべきです。ひこうタイプの枠をパーティに入れてじめん無効を確保し、ドラミドロはフェアリー・くさ・はがねに対する特殊受けとして使うのが基本戦術です。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [フェアリー無効で連携できるドラゴンタイプの考察](/blog/dragon-type-analysis-m3/)
- [サイクル戦の相棒 アシレーヌのM-3考察](/blog/primarina-analysis-m3/)
