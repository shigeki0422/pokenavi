---
title: '【ポケモンチャンピオンズ】ミロカロス考察 M-2 使用率50位 耐久型の技構成と立ち回り'
description: 'M-2シングルバトルで使用率50位のミロカロスを徹底分析。じこさいせい採用率93.6%・ねっとう95.2%の高耐久受けの型、ふしぎなうろこ/かちきの特性選択、れいとうビーム・ミラーコートのケアまで実データで解説。苦手な電気・草への対策も網羅します。'
pubDate: '2026-06-04'
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
  <img src="/images/pokemon/pokemon-0350-00.webp" alt="ミロカロス" />
  <div>
    <h2 style="margin:0 0 8px">ミロカロス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">50位</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ミロカロスは**使用率50位**を記録。みず単タイプの高耐久ポケモンで、じこさいせい（採用率93.6%）による自己回復とねっとう（95.2%）のやけど狙いを軸に、特殊アタッカーを起点にしながら相手を消耗させる**受け型**として運用されます。

種族値はHP95・とくぼう125とみず単タイプの優秀な特殊耐久を持ち、攻撃技に頼らず「居座って回復しながら削る」立ち回りが基本です。アタッカーが並ぶ環境上位とは性質が異なり、構築の受けの軸として50位に位置しています。

---

## なぜミロカロスが受けとして機能するのか

### 1. HP95・D125の高い特殊耐久＋じこさいせいで起点を作らせない

ミロカロスの核はHP95・とくぼう125という特殊方面の硬さです。みず単タイプはほのお・みず・こおり・はがねを×0.5で半減するため、環境に多いほのお特殊枠（リザードンのかえんほうしゃ、サザンドラのかえんほうしゃ・だいもんじ、ヒートロトムのオーバーヒート）を半減しつつ受けられます。

じこさいせい（採用率93.6%）は最大HPの50%を回復する変化技で、半減できる相手の攻撃ならターンを跨いで回復が上回り、相手に有効打がなければ居座り続けられます。攻撃を耐えて回復で押し返す動きが、ミロカロスを「特殊アタッカーの止め役」として成立させています。

### 2. ねっとうのやけどで物理アタッカーの火力も削れる

ねっとう（採用率95.2%）はメインの攻撃技でありながら、30%でやけどを付与します。やけどは相手のこうげきを半減し、毎ターン定数ダメージを与えるため、本来は特殊耐久型のミロカロスが**物理アタッカー相手にも居座りの余地を作れる**のが大きい点です。

タイプ一致のねっとうはみず半減でない相手に等倍以上で通り、ガブリアス（じめん/ドラゴン、みず×2弱点）には弱点を突けます。攻撃性能そのものは控えめですが、やけど分布で相手の物理エースを腐らせる役割を担います。

### 3. ミラーコート・くろいきりで起点回避

ミラーコート（採用率64.3%）は受けた特殊技のダメージを2倍にして返す技で、半減で耐えた特殊アタッカーをそのまま返り討ちにできます。特殊耐久が高いミロカロスとの相性が良く、めいそう持ちのアシレーヌなど特殊偏重の相手に刺さります。

くろいきり（47.0%）は場の能力ランク変化を全てリセットする技です。つるぎのまい・りゅうのまい・ちょうのまいなどの積みアタッカーを起点にされても、積みを帳消しにして受け直せます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#3b82f6">95</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">79</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:66%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:83%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">540</span>
  </div>
</div>

HP95・D125の特殊耐久に対し、B79は控えめで物理方面はそれほど硬くありません。とくこう100はありますが、攻撃は受けの片手間であり、性格・EVも耐久に振られるため火力は伸びません。すばやさ81は環境のアタッカー（ガブリアスS102・サザンドラS98など）に先手を取られる中速で、受けに回って回復で粘る運用が前提になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

みず単タイプは弱点がくさ・でんきの2つだけで、ほのお・みず・こおり・はがねを半減します。ほのおを半減できるため、リザードン・ヒートロトム・サザンドラなどのほのお特殊技に受け出しが利く一方、弱点のでんき（ウォッシュロトム・ヒートロトムの10まんボルト）・くさ（フシギバナのギガドレイン）は×2で通るため、これらには受け出しできません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねっとう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">95.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。30%でやけど。物理アタッカーの火力を削る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じこさいせい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">93.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの50%回復。居座りの軸</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミラーコート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>64.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">受けた特殊技ダメージを2倍で反射（優先度-5）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>60.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・ドラゴン・じめん・ひこうへの打点。10%で凍り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くろいきり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">場の全能力ランク変化をリセット。積みアタッカー対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こごえるかぜ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S1段階ダウン。中速の補完だが採用は少数</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とぐろをまく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・B・命中アップ。少数の積み型</td>
</tr>
</tbody>
</table>
</div>

ねっとう・じこさいせいの2枠はほぼ確定で、残り2枠をミラーコート・れいとうビーム・くろいきりから相手に合わせて選ぶ構成が主流です。攻撃技はねっとう＋れいとうビームの2タイプにとどまり、削りよりも回復・反射・能力リセットで盤面を支える設計になっています。

---

## 特性の選択

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かちき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">45.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">能力を下げられるととくこうが2段階上がる。いかく・おにび等への切り返し</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>メロメロボディ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>33.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">接触してきた相手を30%でメロメロにする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふしぎなうろこ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>21.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">状態異常時にぼうぎょが1.5倍</td>
</tr>
</tbody>
</table>
</div>

最多のかちき（45.2%）は、ギャラドス・ガブリアスのいかくやウォッシュロトム・ヒートロトムのおにびで能力を下げられた瞬間にとくこうが2段階上がるため、受けに来た相手を逆に起点にできます。受け中心の構成で能力低下を仕掛けられる場面が多く、切り返しの択として最も支持されています。

ふしぎなうろこ（21.4%）は状態異常を受けるとぼうぎょが1.5倍になる特性で、B79という控えめな物理耐久を補います。やけど・どく状態をあえて受けることで物理方面の硬さが上がりますが、状態異常が前提のため発動が安定せず、能動的に切り返せるかちきに採用率で水をあけられています。

---

## 主要型の解説

### 型1: HBずぶとい 物理受け型（最多採用）

**性格採用率: ずぶとい 68.7%**（B↑ A↓。物理受けの指標で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0350-00.webp" alt="ミロカロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBずぶとい受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（HB全振り。最多型）<br>
<strong>特性:</strong> かちき / ふしぎなうろこ<br>
<strong>持ち物:</strong> たべのこし / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ねっとう<br>
・じこさいせい<br>
・ミラーコート / くろいきり<br>
・れいとうビーム
</div>
</div>
</div>

**強み:**

EV振りはHB（H32 B32）が採用率39.3%で最多。性格ずぶとい（68.7%）でぼうぎょを上げ、本来は控えめなB79を補って物理方面も受けられるようにする型です。ねっとうのやけど（30%）とかちき／ふしぎなうろこが噛み合い、物理アタッカーに居座りやすくなります。

持ち物はたべのこし（46.4%）が最多で、じこさいせいと合わせた継戦力で受けの軸として機能します。オボンのみ（25.6%）は被弾時の即時回復で、確定数をずらして1発耐えに寄せる選択です。

**弱み:**

物理耐久に寄せた分、でんき・くさの弱点（×2）を半減できないのは変わらず、ウォッシュロトムの10まんボルト・フシギバナのギガドレインには受け出しできません。攻撃技がねっとう＋れいとうビームのみで火力が低いため、回復が間に合わない高火力アタッカーには削り切られる前に押し切られます。

---

### 型2: HD特殊受け型（少数）

**EV採用率: HD 8.0%**（D方向に厚くした特殊受け）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0350-00.webp" alt="ミロカロス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HD特殊受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> おだやか（D↑ A↓）<br>
<strong>EV:</strong> H32 D32（HD振り）<br>
<strong>特性:</strong> かちき<br>
<strong>持ち物:</strong> たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・ねっとう<br>
・じこさいせい<br>
・ミラーコート<br>
・れいとうビーム / くろいきり
</div>
</div>
</div>

**強み:**

性格おだやか（17.2%）でとくぼうを上げ、元から高いD125をさらに伸ばす型です。HB型がぼうぎょを補って汎用的に受けるのに対し、HD型は特殊アタッカー（サザンドラ・リザードン特殊型・アシレーヌ）への受け性能に特化します。ミラーコートとの相性が良く、半減で耐えた特殊技を2倍で反射して特殊アタッカーを返り討ちにできます。

**弱み:**

ぼうぎょに振らないため物理方面はHB型より脆く、ねっとうのやけどが乗らないと物理アタッカーには押し負けます。採用率はHB型（HB系合計で半数超）に対しHD系で1割強にとどまり、汎用性ではHB型に劣ります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ミロカロスと相性がはっきり出るポケモンを有利・不利の両面から挙げます。受け型のため「半減で受けて回復が上回るか」「弱点を突かれて崩されるか」が判断軸です。

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
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42%）・フレアドライブ（33%）を半減。ねっとうがほのお/ひこうに×2弱点。ただしソーラービーム（61%）はくさで×2のため警戒</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（67%）半減、あくのはどう（99%）・りゅうせいぐん（90%）も特殊なのでD125で受けやすい。ミラーコートで反射も狙える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのまい（むし/ほのお）を半減し特殊耐久で受けきる。一致ねっとうがほのおに×2で打点十分（れいとうビームはむし/ほのおに×0.5で通らない）。ただしギガドレイン（59%）はくさ×2のため注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S102で先手を取られ、A130のじしん（99%・等倍）は重い。ねっとうがじめん/ドラゴンに×2弱点で、やけどを引ければ物理火力を削って受け返せる。スケイルショット後の高速化にも注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（99%）・ドゲザン等の物理技をねっとうのやけどで弱化できる。ねっとうははがね/あくに×0.5で打点は薄いが、やけどでA物理を腐らせて受け返す。つるぎのまい（72%）の積みにはくろいきりで対応</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（57%）がでんき×2弱点。ねっとう・れいとうビームはでんき/みずに半減〜等倍で打点が薄く、回復しても押し負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレイン（57%）がくさ×2弱点でHPを吸われ続け、やどりぎのタネ（59%）で消耗。れいとうビームは×2で通るが受け合いでは不利</td>
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
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（57%）がでんき×2弱点。みず・こおりの攻撃技はでんき/みずに半減〜等倍で有効打が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんきを無効化するじめんタイプ（ガブリアス・カバルドン）を同伴し、ロトムの前に引いて10まんボルトを透かす</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギガドレイン（57%）がくさ×2弱点でHPを吸われ、やどりぎのタネ・どくで定数ダメージを受け続ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（くさ×2）を持つ別枠や、くさを半減するほのお・はがねタイプ（リザードン・ギルガルド）を後出しして処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（93%・くさ）が×2弱点かつ急所確定。S123で先手を取られ、はたきおとすでたべのこしを奪われる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（くさ/あくに×2）持ちで上から処理できる高速枠を同伴。くさを半減するはがね・ほのおタイプで受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから・パワージェムはミロカロスに等倍だが、ヘドロウェーブ（69%・どく）で削られつつステルスロックで負担。ねっとう・れいとうビームは半減〜等倍で有効打が薄い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん技（だいちのちから等）を持つガブリアス・カバルドンでいわ/どくの弱点（×2）を突いて落とす</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねっとう・れいとうビームをはがね/ゴーストで半減され、有効打が通らない。こちらの攻撃が軽く、起点にされやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん技（だいちのちから・じしん）を持つアタッカーではがねの弱点（×2）を突いて処理する</td>
</tr>
</tbody>
</table>
</div>
---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム">
    <div class="name">ヒートロトム</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき/ほのおでミロカロスの弱点くさを半減し合う。ボルトチェンジで起点作り</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0887-00.webp" alt="ドラパルト">
    <div class="name">ドラパルト</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速ゴーストアタッカー。受けで止まった盤面に打点を補う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめんでミロカロスの弱点でんきを無効化。ロトム対策の受け先</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ゴーストでくさを半減し、フシギバナ等の苦手枠を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのおでくさを半減。苦手な草枠に上から打点を入れる</div>
  </div>
</div>

**パーティ構成の基本方針:**

ミロカロスは弱点がでんき・くさの2タイプに絞られる代わり、これらには受け出しできません。残り5体で苦手枠を埋めます。

1. **でんき対策**: じめんタイプ（ガブリアス・カバルドン）ででんき技を無効化する受け先を用意
2. **くさ対策**: ほのお・はがねタイプ（リザードン・ギルガルド）でくさを半減して処理
3. **打点補完**: ミロカロス自身の火力が低いため、ドラパルト等の高速アタッカーで詰め筋を作る

---

## データ分析①：攻撃技2枠に対し変化技に偏る技構成

ミロカロスの技採用率を見ると、攻撃技と変化技の比率が受け型の性質をはっきり示しています。

| 技 | 分類 | 採用率 |
|---|---|---|
| ねっとう | 攻撃（みず） | 95.2% |
| じこさいせい | 回復 | 93.6% |
| ミラーコート | 反射 | 64.3% |
| れいとうビーム | 攻撃（こおり） | 60.7% |
| くろいきり | 能力リセット | 47.0% |

攻撃技はねっとう・れいとうビームの2つだけで、残りの上位はすべて回復・反射・能力リセットの変化技です。攻撃範囲はみず＋こおりの2タイプに固定され、純粋な火力では環境上位のアタッカーに遠く及びません。ミロカロスの役割は相手を倒すことではなく、**じこさいせいで居座りながら、ミラーコートで特殊技を返し、くろいきりで積みを消す**ことにあります。

注目すべきはミラーコート（64.3%）とくろいきり（47.0%）が攻撃技のれいとうビーム（60.7%）と同等以上に採用されている点です。これは多くのミロカロスが攻撃の2枠目を切ってでも、特殊反射と積みリセットという「相手の勝ち筋を潰す」択を優先していることを意味します。受けの軸として、自分から崩すより相手の崩しを無効化する設計が徹底されています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HBずぶとい受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ずぶとい 68.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ねっとう・じこさいせい・ミラーコート・れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B補強で物理にも居座れる。やけど＋回復で汎用的</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">でんき・くさ弱点は変わらず。火力が低い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HD 8.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ねっとう・じこさいせい・ミラーコート・れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊アタッカーへの受けに特化。反射が刺さる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理にHB型より脆い。汎用性で劣る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ミロカロスはHP95・D125の特殊耐久とじこさいせい（93.6%）を軸に、ほのお特殊枠（リザードン・サザンドラ）を起点にしながら相手を消耗させる受け型です。ねっとうのやけど・かちきの切り返し・ミラーコートの反射・くろいきりの積みリセットを組み合わせ、攻撃面の薄さを盤面コントロールで補います。

一方で弱点のでんき（ウォッシュロトム）・くさ（フシギバナ・マスカーニャ）には受け出しできず、これらをパーティの他5体（じめん枠・ほのお/はがね枠）で確実にケアできるかが採用の前提になります。アタッカー全盛の環境で50位という位置は、受け構築の軸として一定の需要があることを示しています。

---

## 関連記事

- [天敵となる電気枠 ウォッシュロトムのM-2考察](/blog/rotom-wash-analysis-m2/)
- [苦手な草枠 フシギバナのM-2考察](/blog/venusaur-analysis-m2/)
- [同居率3位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
