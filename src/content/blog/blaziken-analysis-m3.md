---
title: '【ポケモンチャンピオンズ】メガバシャーモ考察 M-3 使用率16位 型別採用率と立ち回り'
description: 'M-3シングルバトルで使用率16位のメガバシャーモを徹底分析。フレアドライブ80.6%・インファイト63.3%の物理アタッカー型と、まもる58.0%＋つるぎのまい50.9%で加速する「まもる→かそく→全抜き」戦術を実データで解説。環境上位への相性とパーティ構成まで紹介します。'
pubDate: '2026-06-20'
heroImage: '../../assets/hero-blaziken-m3.png'
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
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="メガバシャーモ" />
  <div>
    <h2 style="margin:0 0 8px">メガバシャーモ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">16位</strong>　特性: <strong>かそく 97.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、メガバシャーモは**使用率16位**を記録。特性**かそく**（毎ターン終了時にすばやさが1段階上昇）でターンを重ねるごとに加速し、メガ後こうげき160・とくこう130の高火力を活かして全抜きを狙える点が上位定着の理由です。

まもる採用率58.0%が示すように、**まもる→かそくで1段階加速→次ターン先制**という基本パターンが普及しており、対戦相手はこの流れを崩すためにまもる読みの動作を強いられます。フレアドライブ（採用率80.6%）とインファイト（63.3%）でほのお・かくとう2タイプをカバーし、かみなりパンチ（33.6%）で補完を取る構成が主流です。

---

## なぜ今メガバシャーモが使用率16位なのか

### 1. かそくによる加速で先制権を奪取できる

特性かそくは毎ターン終了時にすばやさが1段階上昇します。メガ後すばやさ種族値100から出発し、まもるで1ターン凌ぎながら加速するだけで、翌ターンには実質S150相当以上の速度になります。まもる採用率58.0%はこの「まもる→加速→先制」戦術の普及を示しており、一度加速が始まると上から倒しきれるポケモンが急減するため、後続への制圧力が極めて高い。

### 2. こうげき160とフレアドライブ・インファイトの広い打点

メガ後こうげきは160と環境トップクラス。タイプ一致のフレアドライブ（採用率80.6%）とインファイト（63.3%）はそれぞれ、ほのおとかくとうで補完関係にあり、はがね・こおり・くさ・いわ・ノーマル・あくタイプのポケモンに等倍以上の打点を確保できます。環境上位の多くのポケモンにどちらかの技が2倍以上で通るため、選択肢として機能する範囲が広い。

### 3. つるぎのまい50.9%の積み技で瞬間火力を最大化

つるぎのまい（採用率50.9%）の採用率が過半を超えており、加速しながらA上昇も重ねる「かそく＋つるぎのまい」の動きが圧倒的な制圧力を生み出します。1ターンまもる→かそく→次ターンつるぎのまい→さらに加速、という展開が通れば、A160×2倍のフレアドライブが環境のほぼ全ポケモンを圏内に収めます。

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
    <span style="width:40px;text-align:right;font-size:0.82em;color:#aaa"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:80%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">160</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#2563eb">100</strong></span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">630</span>
    <span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげきが最大幅の+40となり160に到達。とくこう130・すばやさ100もメガで20ずつ上昇しており、火力と素早さを同時に伸ばすメガ進化です。一方、HPとぼうぎょ・とくぼうはいずれも80台にとどまり、耐久面は高くありません。物理耐久・特殊耐久ともに薄いため、先手を取られる展開ではかそくを活かせず一撃で落とされるリスクがあります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="かくとう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお（½）</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（½）</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり（½）</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく（½）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（¼）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    なし
  </td>
</tr>
</tbody>
</table>
</div>

ほのお/かくとうの複合タイプで弱点は**みず・じめん・ひこう・エスパー・フェアリーの5タイプ**。いわはほのおが×2、かくとうが×0.5で相殺されて等倍です。むしはほのお×0.5とかくとう×0.5が重なり×0.25の強耐性になります。弱点5タイプのうち、みず・じめん・ひこう・フェアリーは環境上位に採用ポケモンが多く、かそくが間に合わないうちに弱点を突かれるリスクが高い点に注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フレアドライブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">80.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致ほのお最大火力。反動1/3・10%やけど</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致かくとう高火力。使用後B・D1段階ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">58.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃を防ぎながらかそくで1段階加速する。基本戦術の起点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>50.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき2段階上昇。かそくと組み合わせてA320相当の全抜き態勢へ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこうタイプへの補完打点。10%マヒ</td>
</tr>
</tbody>
</table>
</div>

特性は**かそく97.5%・もうか2.5%**と、ほぼすべての個体がかそくを採用します。もうかはHP1/3以下でほのお技が1.5倍になる特性ですが、かそくによる全抜き戦術と相性が良いため、もうかを選ぶ意義はほとんどありません。

---

## 主要型の解説

性格分布はいじっぱり67.7%・ようき23.4%で、物理アタッカーとしてA上昇かS上昇かの二択に集約されます。最多EV振りはH2-A32-S32（採用率51.3%）で、すばやさとこうげきを最大まで伸ばし、残り2をHPに振る構成です。

### 型1: いじっぱりHA+S物理アタッカー型（最多採用）

**性格採用率: いじっぱり 67.7%**（物理火力重視型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="メガバシャーモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HASいじっぱり物理型（最多）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（97.5%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率51.3%）<br>
<strong>持ち物:</strong> バシャーモナイト（70.6%）/ きあいのタスキ（16.8%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・インファイト<br>
・まもる<br>
・つるぎのまい / かみなりパンチ
</div>
</div>
</div>

**強み:**

いじっぱりでこうげきを最大化し、かそくとまもるを組み合わせた全抜き戦術を狙う型です。A32 S32のEV振りでこうげきと素早さを両立し、まもる→かそく発動→次ターンから先制権を確保する流れが基本。つるぎのまいを採用する場合、まもる→かそく1段階上昇→つるぎのまいでA2段階上昇、という2ターンで加速と火力上昇を両立できます。いじっぱりのA上昇補正により、ようき型と比べてフレアドライブの実ダメージが約10%高く、2発が必要だった相手を1発で圏内に収めやすくなります。

バシャーモナイトを持てばメガ進化でこうげきが160になるため、いじっぱりと組み合わせてA実数値は最大水準に達します。きあいのタスキ採用個体（16.8%）は1発を確定で耐えてかそくを1回発動できますが、メガ進化しない分こうげきは素のままとなります。

**弱み:**

いじっぱりはようき型に対してS実数値が下がり、同速対決でようき型に劣ります。すばやさ100の素の段階では、S100以上の相手に先手を取られるため、まもるを挟む前にひこう・エスパー・みず技で倒されるリスクがあります。フレアドライブの反動1/3も、全抜き中にHP管理を困難にします。

---

### 型2: ようきAS物理アタッカー型

**性格採用率: ようき 23.4%**（素早さ重視型の指標。いじっぱりに次ぐ2位）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0257-00.webp" alt="メガバシャーモ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ASようきS最速型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かそく（97.5%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（採用率5.4%）<br>
<strong>持ち物:</strong> バシャーモナイト（70.6%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・インファイト<br>
・まもる<br>
・かみなりパンチ / つるぎのまい
</div>
</div>
</div>

**強み:**

ようきにすることでS実数値が上がり、メガ後S100の無補正型では上から倒されるSライン付近のポケモンを先手で処理できます。かそく1回後のS上昇量は素早さ実数値に比例するため、いじっぱり型より加速後の到達Sが高くなり、2段階加速後の速度優位の幅が広がります。まもるを挟んで1段階加速した時点で抜けるポケモンの数がいじっぱり型より多い点が、S実数値の重要性を示しています。

**弱み:**

いじっぱり型と比べてこうげきが約10%落ちるため、2発が必要になる場面が増えます。フレアドライブの反動との兼ね合いで、体力管理がより難しくなる型です。採用率5.4%と少数派であり、大部分はいじっぱりを選んでいます。

---

## 環境ポケモンへの相性分析

### 有利・不利がはっきり出る主要ポケモン

ほのお/かくとうは弱点が5タイプあり多くの方向から弱点を突かれますが、耐久面（HP80・ぼうぎょ80・とくぼう80）で先手を許すと致命的なダメージを受けます。一方でかそくが1〜2回発動すれば大半のポケモンより速くなり、こうげき160の高火力で一方的に押し込める展開になります。

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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（使用率上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトが×4。フレアドライブも×2。耐久型でもA160の一致打点で圧倒できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0879-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドリュウズ（使用率上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがはがね×2・じめん等倍で×2。インファイトもはがね×2。かそく加速後はS100のこちらが先手を取れる局面が増える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがじめん×2弱点。S102のガブリアスはメガ前のS100より速く、まもる前に先制されるリスクがある。りゅうせいぐんも等倍で通る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプのみず技が×2弱点。ムーンフォースもフェアリー×2弱点。2方向から弱点を突かれる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブは×0.5の半減。インファイトは×2。相手のほのお技はこちらに×0.5で刺さりにくいが、ひこう技はこちらに×2弱点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ やや不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがはがね×2・かくとう等倍で×2。ただしメガルカリオのメガ後S112はこちらの素のS100より速く、まもる前に先制される場面がある。相手のインファイトはかくとう×1・ほのお等倍で等倍</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点の5タイプ（みず・じめん・ひこう・エスパー・フェアリー）を主力技に持つポケモンが天敵です。特にかそく前のS100では多くの高速勢に先手を取られるため、一度でも弱点技を受けると一撃で倒される耐久の薄さが課題になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）がじめん×2弱点。S102でメガ前のこちら（S100）より速く、まもる前に先制されるリスクがある</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこう枠（ギャラドス・リザードン等）を添え、ガブリアス対面で引いて弱点技を避ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず技とムーンフォースの両方がこちらの弱点を突く。みず技×2・フェアリー技×2でいずれも半減できる手段がない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね複合（ドドゲザン等）でフェアリー技を半減しつつアシレーヌを牽制する枠を用意する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちら（S100）より速く、トリックフラワーで継続的に削られる。こちらのほのお技はくさ×0.5・あく等倍で×0.5の半減となり打点が薄い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイトがくさ等倍・あく×0.5で×0.5の半減にとどまるため、かそく後の先制かほのお弱点を持つ枠で処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-01.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガリザードンY（5位・メガ）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後S100はこちらと同速のため先制権が確保できず、にほんばれ＋ほのお技が威力アップすることで拮抗した打ち合いになる。エアスラッシュはひこう×2弱点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かそくを先に発動させた後なら先制できる。いわタイプの技を持つ枠（ガブリアス等）で弱点×4を狙う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率98.0%）がじめん×2弱点。高HPと高Bでインファイトを1発耐えるケースがある。あくびでかそくの展開を妨害される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがじめん等倍・かくとう等倍で等倍止まりだが、A160の火力で2発圏内に入れることを狙う。くさ技を持つ枠を同伴してカバルドンを先に処理する</td>
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
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんがバシャーモの苦手なじめん枠に強く、じめん・ドラゴン打点でカバルドン等も処理できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじめんを無効化。バシャーモが苦手なガブリアス・カバルドンのじしんを受ける枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ひこうでじめん無効。特殊ほのお打点でバシャーモと役割を分担しやすい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン">
    <div class="name">ドドゲザン</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">フェアリー弱点をバシャーモが物理で処理しにくい分、はがね打点でフェアリー枠を牽制</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率上位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーでカバルドン・ガブリアスのじめん技を牽制。特殊方向の補完枠</div>
  </div>
</div>

**パーティ構成の基本方針:**

メガバシャーモはかそくによる全抜き性能が高い反面、弱点が5タイプあり先手を取られると一撃で落とされます。残り5体で以下を補います。

1. **じめん対策**: ガブリアスのじしんを無効化するひこう枠（ギャラドス・リザードン）でバシャーモのじめん弱点をカバー
2. **みず対策**: みず技に強いくさタイプや特殊受け枠を用意してアシレーヌ・カバルドンへの打点を確保
3. **フェアリー対策**: はがね複合（ドドゲザン等）でムーンフォースを半減しつつバシャーモを通す隙を作る
4. **かそくの展開支援**: 相手の素早いポケモンを先に削っておき、バシャーモが1回まもるだけで先制できる状況を整える

---

## データ分析①：まもる採用率58%が示す「かそく展開依存」の実態

バシャーモの技採用率を並べると、攻撃技とサポート技の役割分担が明確です。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| フレアドライブ | 攻撃 | 80.6% | ほのお主打点 |
| インファイト | 攻撃 | 63.3% | かくとう主打点 |
| まもる | 変化 | 58.0% | かそく加速の起点 |
| つるぎのまい | 変化 | 50.9% | A2段階上昇 |
| かみなりパンチ | 攻撃 | 33.6% | みず・ひこう補完 |

注目すべきは**まもる58.0%とつるぎのまい50.9%がともに過半を超えている**点です。攻撃技のフレアドライブ・インファイトは「撃ちたい技」ですが、まもる・つるぎのまいは「ターンを消費して態勢を整える技」です。これら変化技の高採用率は、バシャーモがかそく1回では不十分な場面が多く、複数ターンの準備が前提になっていることを示しています。

持ち物採用率を見ると**バシャーモナイト70.6%・きあいのタスキ16.8%**の2択構造です。バシャーモナイトの7割超は「メガ進化でこうげき160を最大化する正攻法」、タスキ16.8%は「1発を確定で耐えて最低1回かそく発動を保証する保険型」という目的の違いで選ばれています。同じかそく戦術でも、「高火力で押し切るか、1回の生存保証を取るか」の方向性が持ち物に表れています。

タスキ個体はバシャーモナイトを持たないためメガ進化できず、こうげきは素の120止まりになります。フレアドライブ・インファイトの実火力がメガ型と比べて大きく落ちるため、タスキ型はかそくを複数回積んでS優位を確立することに特化した動きになります。**遭遇時に持ち物が判明するまでどちらか分からない点が、バシャーモに対する読みを複雑にしています。**

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">いじっぱりHA+S物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 67.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">フレアドライブ・インファイト・まもる・つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A160+いじっぱりで最大火力。2発が必要な相手を1発圏内に</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ようき型より加速後のS到達が低い。フレアドライブ反動でHP管理が難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ようきAS物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき 23.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">フレアドライブ・インファイト・まもる・かみなりパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">いじっぱり型より加速後のS到達が高く、抜けるポケモンの幅が広い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こうげきが約10%低く、いじっぱり型なら1発の相手を2発必要とする場面が増える</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガバシャーモは特性かそくによる加速と、こうげき160の高火力を組み合わせた全抜きアタッカーです。まもる→かそく→先制という基本パターンが確立しており、1〜2ターンの準備で環境のほぼ全ポケモンを上から殴れる状態になります。つるぎのまい50.9%の採用も合わさると、加速しながらAも上昇してほぼ止められない状態になる局面が生まれます。

弱点は5タイプと多く、HPとぼうぎょ・とくぼうがいずれも80台と耐久は薄いため、かそくを積む前に弱点技を受けると一撃で落とされます。特にガブリアスのじしん・アシレーヌのみず技などはバシャーモが全抜き態勢に入る前に確定で機能します。パーティ単位でじめん・みず・フェアリー対策を厚くし、バシャーモが安全にかそくを積める対面を作ることが使用する上での前提条件です。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-3考察](/blog/garchomp-analysis-m3/)
- [みず・フェアリーを持つアシレーヌのM-3考察](/blog/primarina-analysis-m3/)
- [ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
