---
title: '【ポケモンチャンピオンズ】メガギャラドス 考察 M-4 シーズン りゅうのまい型とタイプ変化の弱点'
description: 'M-4シーズン使用率8位のメガギャラドスを考察。メガストーン採用率80.5%・りゅうのまい採用率84.6%のデータから主力型を分析し、メガ進化でじめん無効を失い新たな弱点が生まれる点を実数値付きで検証、ミミッキュなど苦手な相手も整理します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-gyarados-m3.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" />
  <div>
    <h2 style="margin:0 0 8px">メガギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">8位</strong>（M-3: 15位）　持ち物: <strong>ギャラドスナイト 80.5%</strong>
    </div>
  </div>
</div>

M-4シーズン、ギャラドスは使用率15位から8位へ順位を上げました。りゅうのまいで攻撃・素早さを積んでからたきのぼり・じしん・こおりのキバで殴る積みアタッカー型が主流です。特筆すべき点は、メガ進化でタイプがみず/ひこうからみず/あくへ変わること。じめん無効という通常時の強みを失う代わりに、ゴースト・あく・こおりへの耐性（元から半減のはがね・みず・ほのおと合わせて計6タイプが耐性）とエスパー無効を新たに得るタイプ変化そのものが立ち回りの核になっています。

---

## メガギャラドスの基本スペック

### 種族値（通常→メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:78%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">125</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">79</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:41%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">81</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">540</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげき125→155・ぼうぎょ79→109・とくぼう100→130と上昇しますが、**すばやさは81のまま変化しません**。りゅうのまいを積むまでは環境上位の多くより遅く、積み技を通す隙をどう作るかが型の前提になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ（メガ進化後）：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

弱点はかくとう・むし・くさ・でんき・フェアリーの5タイプ（いずれも×2）。**メガ進化前のみず/ひこうはじめん技を無効化できましたが、メガ後のみず/あくではじめん技は等倍で通ります**（無効から弱点に変わるわけではなく、無効から等倍に変わるだけです）。一方でメガ進化前は弱点だったでんき技も×4から×2へ軽減され、新たにエスパー技が無効になります。耐性面ではゴースト・あく・こおりを新たに半減できるようになり（もともと半減だったはがね・みず・ほのおと合わせて6タイプが耐性）、新規獲得はゴースト・あく・こおりの3タイプです。環境上位ではミミッキュ（2位）のじゃれつく（フェアリー・採用率98.2%）が弱点を突く代表的な技です。

### 特性

メガ進化前は**いかく（99.1%）**が固定。場に出た瞬間に相手の攻撃を1段階下げるため、りゅうのまいを積むまでの起点を作りやすくなります。メガ進化後は**かたやぶり**に変わり、相手の特性に関係なく技を出せます（例外となる特性もあります）。ふゆう・もらいび等の相手特性を無視してたきのぼり・じしんを通せる点が、りゅうのまい後の全抜きを支えます。

---

## M-4の採用型

### 型1：りゅうのまい積みアタッカー型（ようき 49.9% / いじっぱり 43.1%）

**性格採用率: ようき 49.9% / いじっぱり 43.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">りゅうのまい積みアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（99.1%）→メガ後かたやぶり<br>
<strong>性格:</strong> ようき（S↑ C↓）またはいじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（採用率25.4%・最多分布）<br>
<strong>持ち物:</strong> ギャラドスナイト（80.5%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・たきのぼり<br>
・じしん<br>
・こおりのキバ
</div>
</div>
</div>

りゅうのまい（採用率84.6%）で攻撃・素早さを1段階ずつ上げ、たきのぼり（みず・威力80、採用率80.1%）を主力に殴る型。じしん（じめん・威力100、採用率77.8%）はメタグロス（4位）やブリジュラス（5位）のはがね/ドラゴンへ×2、こおりのキバ（こおり・威力65、採用率48.2%）はガブリアス（1位）のドラゴン/じめんへ×4というカバー範囲を持ちます。パワーウィップ（くさ・威力120、採用率43.8%）やかみくだく（あく・威力80、採用率22.6%）は選択技として一部の枠と入れ替わります。

**強み:**

ようきはH171/A207/B130/C81/D150/S146。りゅうのまいを1回積むと実数値でS219相当となり、メタグロスmega（S最速178）・メガリザードン（S167）・メガバシャーモ（S167）など環境上位の非スカーフ勢を素早さで上回ります。たきのぼり（威力120）は1積み後のA310で、メタグロス物理型（B170・H157）へ83〜98ダメージ（53〜62%）となり確定2発です。

**弱み:**

いじっぱりはH171/A227/B130/C81/D150/S133。いじっぱりA227はようきA207より火力を狙えますが、積み後のS199（いじっぱり）でもサザンドラ（こだわりスカーフ84.2%・S実数値247）やマスカーニャ（こだわりスカーフ70.9%・S実数値288）といったスカーフ持ちには積んでも上から動けません。

---

## データ分析①：M-3→M-4 技構成の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>84.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+14.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-10.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">77.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">48.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ちょうはつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-7.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみくだく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+12.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゆきなだれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-11.0pp</td>
</tr>
</tbody>
</table>
</div>

M-4の最大変化は**じしん（77.8%）・こおりのキバ（48.2%）の新台頭**です。M-3ではこの2技は上位技リストに掲載がありませんでしたが、M-4で一気に上位技へ入りました。こおりのキバ（威力65）はガブリアス（1位）に×4が入り、たきのぼり（実質威力120）より実質打点が高くなる技です。じしんはメタグロス（4位）・ブリジュラス（5位）といったはがね複合の上位ポケモンへの打点として機能します。

メガストーン採用率もM-3の56.5%からM-4は80.5%へ+24.0pp上昇し、りゅうのまいで積んで全抜きを狙う運用がより支配的になっています。

---

## データ分析②：メガ進化によるタイプ変化と弱点シフト

ギャラドスは数少ない「メガ進化でタイプそのものが変わる」ポケモンです。通常時のみず/ひこうとメガ後のみず/あくで、対応できるタイプが大きく入れ替わります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">環境上位ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技（タイプ）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">通常時（みず/ひこう）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後（みず/あく）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん（じめん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バシャーモ（10位・メガ後A233）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">インファイト（かくとう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（2位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じゃれつく（フェアリー・A156）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メタグロス（4位・メガ後）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サイコファング（エスパー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（5位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん（じめん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
</tbody>
</table>
</div>

じめん技を無効化できるのは通常時（メガ進化前）だけで、メガ進化した瞬間からガブリアス・ブリジュラス・カバルドン（3位）のじしんは等倍で通ります。一方でメガ後はメタグロスのサイコファング（エスパー）を無効化できるようになり、ゴースト・あく・こおりへの耐性も新たに得ます（はがね・みず・ほのおはメガ進化前から半減でした）。

具体的な被ダメージ量として、バシャーモ（メガ、A実数値233・いじっぱり）のインファイト（かくとう・威力120）はメガギャラドス（B130・H171）に244〜288ダメージ（H171の143〜168%）で確定1発。メガ進化前のみず/ひこうならかくとうは耐性（×0.5）だったため、この一撃はメガ進化による弱点シフトの影響がそのまま数値に表れています。

一方でこの変化は不利ばかりではありません。メタグロス（4位）のサイコファング（エスパー）は通常時のみず/ひこうなら等倍で通っていましたが、メガ後のみず/あくでは無効になります。相手がメタグロスのエスパー技を主力打点として構築していた場合、メガ進化のタイミングでその打点そのものを失わせられる関係です。

---

## 苦手なポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー・採用率98.2%）が×2弱点。A156のいじっぱり型で計算すると124〜147ダメージ（メガギャラドスH171の73〜86%）となり確定2発です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（かくとう・採用率67.2%）が×2弱点。メガバシャーモ（持ち物バシャーモナイト72.9%）のA233なら確定1発（144〜169%）です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり（むし・採用率71.1%）が×2弱点。こだわりスカーフ採用率70.9%と高く、りゅうのまいを1回積んでも上から動かれます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんじほう（でんき・採用率96.6%）ときあいだま（かくとう・採用率96.2%）の両方が×2弱点で、どちらの技も高い採用率のため回避が難しい相手です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でギャラドスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" loading="lazy">
    <div class="name">バシャーモ</div>
    <div class="rate">7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-00.webp" alt="アローラキュウコン" loading="lazy">
    <div class="name">アローラキュウコン</div>
    <div class="rate">9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、こおり技に×4弱点を持ちます。メガギャラドスはこおり技を耐性（×0.5）で受けられるため、こおり打点を持つ相手への引き先になれます。逆にガブリアスはでんき技を無効化できるため、メガギャラドスの弱点であるでんき技をガブリアス側で受けられる関係です。

**ミミッキュ**（2位）はゴースト/フェアリーで、はがね技に×2弱点を持ちます。メガギャラドスははがね技を耐性（×0.5）で受けられ、ミミッキュの弱点をカバーできます。一方でミミッキュはかくとう技を無効化・むし技を耐性（×0.25）で受けられるため、メガギャラドスの弱点であるかくとう・むし技をミミッキュ側が引き受けられます。

**カバルドン**（3位）はじめん単タイプで、でんき技を無効化します。メガギャラドスの弱点であるでんき技をカバルドンが引き受けられる組み合わせです。一方でカバルドンはみず・くさ・こおり技が弱点で、メガギャラドスはみず・こおり技を耐性（×0.5）で受けられるため、この2タイプについては補い合えます。

**マフォクシー**（5位）はほのお/エスパーで、ゴースト・あく技に×2弱点を持ちます。メガギャラドスはゴースト・あく技をいずれも耐性（×0.5）で受けられ、マフォクシー側の弱点をカバーします。一方でマフォクシーはかくとう・くさ・フェアリー技を耐性（×0.5）で受けられるため、メガギャラドスの弱点3タイプをマフォクシー側が引き受ける相互補完の関係です。

**ブリジュラス**（4位）ははがね/ドラゴンで、むし・くさ・でんき技を耐性（×0.5前後）で受けられます。メガギャラドスの弱点であるこの3タイプをブリジュラスがカバーする一方向の補完関係です。

**マスカーニャ**（6位）はくさ/あくで、くさ・でんき技を耐性（×0.5）で受けられ、メガギャラドスの弱点2タイプをカバーします。一方でマスカーニャ自身もかくとう・むし・フェアリー技が弱点で、メガギャラドスと重なる部分は他の枠での対応が必要です。

---

## まとめ

M-4のギャラドスは使用率15位から8位へ上昇し、メガストーン採用率も80.5%まで伸びたシーズンです。

- **りゅうのまい積みアタッカー型が主流**（りゅうのまい84.6%・たきのぼり80.1%）：じしん（77.8%）・こおりのキバ（48.2%）がM-3の圏外から一気に上位技へ台頭し、ガブリアス・ブリジュラス・メタグロスへの打点を確保
- **メガ進化でみず/ひこう→みず/あくへタイプが変化**：じめん無効を失う代わりにゴースト・あく・こおりへの耐性とエスパー無効を獲得（はがね・みず・ほのおはもともと半減）。特にバシャーモのインファイト（かくとう）は耐性から弱点へ変わり確定1発になる
- **同居率1位はガブリアス**：こおり技とでんき技を互いに受け合う関係で、メガギャラドスの弱点であるでんき技をガブリアス・カバルドンが引き受ける構成が上位を占める

積む前は環境上位の非スカーフ勢より遅く、りゅうのまいを通す隙をパーティでどう作るかが運用の前提になります。積んだ後の火力・素早さは高水準ですが、こだわりスカーフを持つマスカーニャ・サザンドラには積んでも上から動けない点は変わりません。

---

*関連記事：[メタグロス考察 M-4](/blog/metagross-analysis-m4/)*
