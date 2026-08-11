---
title: '【ポケモンチャンピオンズ】ギャラドス 考察 M-5 シーズン パワーウィップ台頭とみずタイプ環境'
description: 'M-5シーズン使用率7位のギャラドスを考察。メガストーン採用率77.8%・りゅうのまい採用率82.3%の積みアタッカー型を実数値付きで分析し、たきのぼりに迫るパワーウィップ採用率57.3%の背景をみずタイプ上位勢の増加から検証します。'
pubDate: '2026-08-10'
updatedDate: '2026-08-10'
heroImage: '../../assets/hero-gyarados-m5.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" />
  <div>
    <h2 style="margin:0 0 8px">メガギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>（M-4: 8位）　持ち物: <strong>ギャラドスナイト 77.8%</strong>
    </div>
  </div>
</div>

M-5シーズン、ギャラドスは使用率8位から7位へ順位を上げました。りゅうのまいで攻撃・素早さを積んでからじしん・たきのぼり・パワーウィップで殴る積みアタッカー型が主流です。メガ進化でタイプがみず/ひこうからみず/あくへ変わり、じめん無効という通常時の強みを失う代わりに、ゴースト・あく・こおりへの耐性とエスパー無効を得るタイプ変化そのものが立ち回りの核になっています。

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

弱点はかくとう・むし・くさ・でんき・フェアリーの5タイプです（いずれも×2）。メガ進化前のみず/ひこうはじめん技を無効化できましたが、メガ後のみず/あくではじめん技は等倍で通ります（無効から等倍に変わるだけで、弱点になるわけではありません）。耐性面ではゴースト・あく・こおりを半減でき（もともと半減だったはがね・みず・ほのおと合わせて6タイプが耐性）、新たにエスパー技を無効化します。環境上位ではミミッキュ（5位）のじゃれつく（フェアリー・採用率97.3%）が弱点を突く代表的な技です。

### 特性

メガ進化前は**いかく（99.2%）**をほぼ全個体が採用しています（残りはじしんかじょう0.8%）。場に出た瞬間に相手の攻撃を1段階下げるため、りゅうのまいを積む隙を作りやすくなります。メガ進化後は**かたやぶり**に変わり、相手の特性に関係なく技を出せます（例外となる特性もあります）。ふゆう（サザンドラ16位・ウォッシュロトム27位が採用）を無視してじしんを通せる点が、りゅうのまい後の全抜きを支えます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃・素早さを1段階上昇。積みアタッカー型の始動技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">76.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタグロス（9位）・ブリジュラス（3位）等のはがね複合へ×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たきのぼり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">63.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致のメインウェポン。20%の確率でひるみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（6位・じめん単タイプ）等へ打点。みず技を半減する相手にも等倍以上で通る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（1位）のドラゴン/じめんへ×4。10%でこおり状態</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみくだく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致でゴースト・エスパーへの打点。20%で相手の防御ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を変化技封じ。りゅうのまいを積む隙を作る補助技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-4で必ず後攻。被弾していれば威力2倍</td>
</tr>
</tbody>
</table>
</div>

こおりのキバ（威力65）とたきのぼり（威力80）を比べると、ガブリアス（ドラゴン/じめん）へはこおりのキバが×4となり実質威力260相当で、たきのぼりの実質威力120（等倍）を大きく上回ります。じしん（76.8%）はメタグロス・ブリジュラスといったはがね複合の上位ポケモンをカバーする役割です。パワーウィップ（57.3%）はたきのぼり（63.1%）に迫る採用率まで伸び、選択の幅が広がっています（詳細は後述のデータ分析①）。

---

## M-5の採用型

### 型1：りゅうのまい積みアタッカー型（いじっぱり 47.5% / ようき 45.3%）

**性格採用率: いじっぱり 47.5% / ようき 45.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">りゅうのまい積みアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（99.2%）→メガ後かたやぶり<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（採用率26.5%・最多分布）<br>
<strong>持ち物:</strong> ギャラドスナイト（77.8%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・じしん<br>
・たきのぼり<br>
・パワーウィップ
</div>
</div>
</div>

りゅうのまい（採用率82.3%）で攻撃・素早さを1段階ずつ上げ、じしん（じめん・威力100、採用率76.8%）でメタグロス（9位・はがね/エスパー）・ブリジュラス（3位・はがね/ドラゴン）といったはがね複合を突く型です。たきのぼり（みず・威力80、採用率63.1%）とパワーウィップ（くさ・威力120、採用率57.3%）はどちらもメインウェポンの候補で、こおりのキバ（こおり・威力65、採用率49.0%）はガブリアス（1位）のドラゴン/じめんへ×4というカバー範囲を持ちます。かみくだく（あく・威力80、採用率25.0%）は選択技として一部の枠と入れ替わります。

**強み:**

いじっぱりはH171/A227/B130/C81/D150/S133。ようきはH171/A207/B130/C81/D150/S146。いじっぱりの積んだ後のA340（227×1.5）で計算すると、最大打点のじしん（じめん・威力100、採用率76.8%）はギャラドスのタイプ一致技ではありませんが、はがね/エスパー複合への×2弱点により、メガメタグロス（B170・H157）へ153〜180ダメージ（97〜114%）で乱数1発です。

**弱み:**

いじっぱりの積み後S199は、メガゲッコウガ（S213）・メガミミロップ（S205）・メガゲンガー（S200）・メガライチュウY（S200）にいずれも届かず、ようき（積み後S219）にすれば上回れます。ただしこれらは非スカーフの前提での比較で、サザンドラ（こだわりスカーフ82.9%・多数派ひかえめ76.1%ではスカーフ込みS実数値225、少数派おくびょう22.5%では247）やマスカーニャ（こだわりスカーフ55.2%・S実数値288）といったスカーフ持ちには、ようき（積み後S219）でも積んでも上から動けません。

### 型2：非メガたべのこし型（いじっぱり 47.5% / ようき 45.3%）

**性格採用率: いじっぱり 47.5% / ようき 45.3%**（メガ型・非メガ型を合わせたギャラドス全体の分布）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">非メガたべのこし型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（99.2%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（採用率26.5%・最多分布）<br>
<strong>持ち物:</strong> たべのこし（採用率11.4%・持ち物2位）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・じしん<br>
・たきのぼり<br>
・パワーウィップ
</div>
</div>
</div>

タイプはみず/ひこうのまま変化しません。メガ進化しない分、こうげき125・ぼうぎょ79・とくぼう100と型1（メガ後A155・B109・D130）より低い種族値で戦うことになります。メガ進化枠を空けたまま、りゅうのまいを積む型1と同じ運用を別の1枠で行える構成です。実数値はH171・B100・D120（いじっぱりA194／ようきA177、S133・146は型1と同じ）です。

**強み:**

メガ進化しないため、タイプはみず/ひこうのままです。カバルドン（6位）の主力技じしん（じめん、採用率98.5%）を無効化でき、型1（メガ後みず/あく）で等倍になってしまうじめん技を完封できます。ただしカバルドンはあくび（採用率95.3%）で交代を強制でき、ふきとばし（採用率53.7%）でこちらの積んだランク変化をリセットできるため、このじめん無効はりゅうのまいを積んだ後の打点勝負を保証するものではありません。また、かくとう技・むし技はいずれも耐性（×0.5）のままで、型1はメガ進化でこの2タイプが弱点（×2）に変わるため、この2タイプへの耐性を保てる点は非メガならではの強みです。持ち物にメガストーンを使わないため、パーティの別の枠でメガストーンを温存・使用できる選択肢も残ります。たべのこし（採用率11.4%）は毎ターンHP1/16を回復し、あくびやふきとばしで流された後にりゅうのまいを積み直す機会を作りやすくします。

**弱み:**

でんき技への弱点が型1（メガ後みず/あく・×2）よりさらに深刻です。みず/ひこうはでんき技を×4で受けてしまうため、ライチュウ（22位・ライチュウナイトY 97.2%でメガライチュウYに進化し特性ノーガード）のでんじほう（でんき・威力120、C実数値212）は482〜568ダメージとなり、非メガギャラドス（D120・H171）のH171を大きく超えます。型1（メガ後みず/あく・×2）でも同じでんじほうは193〜228（H171の113〜133%）で必中の確定1発が成立しますが、非メガはその2.5倍前後にあたる過剰打点を浴びる違いがあります。加えてみず/ひこうはいわ技に新たに弱点（×2）を持ちます（型1のメガ後みず/あくはいわ技が等倍）。攻撃面でも、りゅうのまいを積んだ後の実数値（いじっぱりA291）は型1の積み後A340より低く、例えばカバルドン（6位・わんぱく最多64.1%、H215・B154）へのパワーウィップは171〜202ダメージ（79〜94%）にとどまり、型1で成立する乱数1発（200〜236・93〜110%）が非メガでは成立しません。加えて特性はいかくのままでかたやぶりを得られないため、ふゆう持ちのサザンドラ・ウォッシュロトムへじしんを通せない点も型1との明確な差です。

---

## データ分析①：たきのぼりを追い上げるパワーウィップ

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4（2026-07-13時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">63.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-17.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>57.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+13.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">77.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">76.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">82.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.3pp</td>
</tr>
</tbody>
</table>
</div>

M-4（2026-07-13時点）ではたきのぼり（80.1%）がパワーウィップ（43.8%）に36.3pp差をつけるメインウェポンでしたが、M-5ではたきのぼりが63.1%へ-17.0pp、パワーウィップが57.3%へ+13.5ppと、両者の差は5.8ppまで縮まりました。

背景には使用率上位に**みずタイプ**が定着していることがあります。M-5使用率2位のアシレーヌ（みず/フェアリー）・15位のイダイトウ（みず/ゴースト）・17位のゲッコウガ（みず/あく）・19位のダイケンキ（みず単）はいずれもみず技を耐性（×0.5）で受けられ、たきのぼりの打点を半減します。一方でパワーウィップ（くさ）はこの4体すべてに×2で通ります。特にアシレーヌはM-4の6位からM-5で2位へ上昇しており、みずタイプ上位勢の存在感が増したことが、たきのぼり一強からの技構成分散を招いた構図です（ゲッコウガはM-4の13位からM-5は17位へ下降していますが、上位圏内であること自体は変わりません）。

---

## データ分析②：メガ進化によるタイプ変化と弱点シフト

ギャラドスは数少ない「メガ進化でタイプそのものが変わる」ポケモンです。じめん無効を失う代わりにゴースト・あく・こおりへの耐性とエスパー無効を得る変化（前述）が、具体的にどの環境上位ポケモンとの対面を左右するかを整理します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">バシャーモ（23位・メガ後A233）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">インファイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミッキュ（5位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">じゃれつく（A156）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メタグロス（9位・メガ後）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">サイコファング</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">無効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス（3位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">10まんボルト（採用率58.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">がんせきふうじ（採用率26.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">等倍</td>
</tr>
</tbody>
</table>
</div>

具体的な被ダメージ量として、バシャーモ（メガ、A実数値233・いじっぱり）のインファイト（かくとう・威力120）はメガギャラドス（B130・H171）に244〜288ダメージ（H171の143〜168%）で確定1発です。ただしギャラドス自身の**いかく（採用率99.2%）**は場に出た瞬間に発動するため、バシャーモが対面に既に出ていた場合はA233が1段階下降（A155相当）し、ダメージは163〜192（95〜112%）まで下がり確定1発ではなくなります。バシャーモが後から場に出てきた場合はいかくの影響を受けず、確定1発のままです。メガ進化前のみず/ひこうならかくとうは耐性（×0.5）だったため、いずれのケースもメガ進化による弱点シフトの影響が数値に表れています。

---

## 苦手なポケモン

相手の主力打点がメガギャラドスの弱点（かくとう・むし・くさ・でんき・フェアリー）を高い採用率で突いてきて、なおかつギャラドス側の技が等倍以下にとどまり打点で有意に返せない相手を選んでいます（有利表と同じ選定基準）。使用率TOP30の中から代表的な数体を抜き出したものであり、網羅した一覧ではありません。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー・採用率97.3%）が×2弱点。A156のいじっぱり型なら124〜146ダメージ（メガギャラドスH171の73〜85%）で確定2発ですが、持ち物いのちのたま（採用率80.5%）込みだと160〜189（94〜111%）まで伸び、乱数1発になります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・採用率96.9%）が一致技かつ×2弱点。こだわりスカーフ採用率55.2%と過半数で、りゅうのまいを1回積んでも上から動かれます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">バシャーモ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（かくとう・採用率66.5%）が一致技かつ×2弱点。メガバシャーモ（持ち物バシャーモナイト63.7%）のA233なら244〜288（143〜168%）で確定1発ですが、ギャラドスのいかく（採用率99.2%）を対面から受けていればA155相当に下がり163〜192（95〜112%）まで軽減されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物ライチュウナイトY（採用率97.2%）でメガライチュウYに進化し、特性がノーガードに変化します。でんじほう（でんき・命中率50・採用率97.5%）ときあいだま（かくとう・命中率70・採用率97.1%）はいずれも×2弱点かつ本来は外れうる技ですが、ノーガードで必中になるため回避できません。C212のでんじほうはタイプ一致補正が乗り、メガギャラドス（D150・H171）に193〜228（113〜133%）で必中の確定1発です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0503-00.webp" alt="ダイケンキ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ダイケンキ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎ（かくとう・採用率95.1%）が×2弱点。特性きれあじ（採用率99.3%、採用率2位のげきりゅうは0.7%）で切る技の威力が1.5倍になり実質威力135相当です。最多分布のいじっぱりA167（EV32・採用率20.1%）なら132〜156ダメージ（メガギャラドスH171の77〜91%）で、ギャラドスの**いかく（採用率99.2%）**を対面から受けていればA111相当まで下がり88〜104（51〜61%）まで軽減されます。一方でギャラドス側のみず・あく技はたきのぼりが耐性（×0.5）、かみくだくが等倍止まりで打点に乏しく、確実に上回れるのはパワーウィップ（くさ・×2）に限られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボディプレス（かくとう・威力80・採用率55.6%）は使用者の防御実数値を攻撃側の数値として扱う技で、×2弱点も重なります。最多分布のわんぱくB172（EV32・採用率42.9%）なら81〜96ダメージ（メガギャラドスH171の47〜56%）ですが、ビルドアップ（採用率23.9%）を1回挟むとB258相当まで伸び120〜142（70〜83%）まで跳ね上がります。とんぼがえり（むし・威力70・採用率71.8%）も×2弱点で、45〜54（26〜32%）を与えつつ後続へ交代できます。ギャラドス側はじしんが無効、パワーウィップも×0.25で通らず、たきのぼり（みず・威力80、タイプ一致補正込み実質威力120）ですら等倍止まりの61〜72ダメージ（アーマーガアH205の30〜35%）と、返しの打点も弱いままです</td>
</tr>
</tbody>
</table>
</div>

---

## 有利なポケモン

相手の主力打点がメガギャラドスの弱点（かくとう・むし・くさ・でんき・フェアリー）を20%以上の採用率で突いてこず、かつ素早さ・持ち物の面でも打点勝負を覆されにくい相手を、実際のダメージ計算で確認します。**積んだ後の打点で有利が成立しても、相手が積む前にこちらを無力化する手段（交代強制・全回復・積み技リセット等）を高い採用率で持つ場合は「有利」から除外します**（この基準は後述のガブリアスにも同じ形で適用しています）。使用率TOP30の中から代表的な1体を抜き出したものであり、条件に該当する相手を網羅した一覧ではありません。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" alt="スターミー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">スターミー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（くさ・採用率57.3%）がみず/エスパーに×2。スターミナイト採用率97.7%と過半数を大きく超えるため対面はほぼ確実にメガスターミー（B実数値125・H実数値137）で、積む前のA227でも164〜194ダメージ（120〜142%）で確定1発です（詳細は表下）</td>
</tr>
</tbody>
</table>
</div>

スターミーはメガ進化するとS実数値がようき49.1%でS189、いじっぱり47.0%でS172と高水準になり、特性はちからもちに変わります。積む前のメガギャラドス（S実数値133〜146）に対しては先手を取れる点に注意が必要ですが、最大打点のアクアブレイク（みず・威力85、ちからもち込みA実数値304〜334）はギャラドス側のみずタイプによる半減（×0.5）で56〜73ダメージ（メガギャラドスH171の33〜43%）にとどまり、先制を取られてもこちらの確定1発の打点勝負自体は覆りません。

カバルドン（6位）はパワーウィップ（くさ・採用率57.3%）がじめん単タイプに×2で通ります。最多型はわんぱく64.1%・EV H32-B2-D32（21.4%）で、実数値はH215・B154です。積む前のA227のパワーウィップでは134〜158ダメージ（62〜73%）にとどまり確定2発（乱数でも1発は成立しません）ですが、りゅうのまいを積んだ後のA340なら200〜236ダメージ（93〜110%）で乱数1発になります。ただしカバルドンはあくび（採用率95.3%）で積む前に交代を強制でき、ふきとばし（採用率53.7%）で積んだランク変化そのものをリセットでき、なまける（採用率49.5%・全回復技）も約半数が採用しているため、りゅうのまいを積む隙を与えない限りこの打点は成立しません。積む前に無力化される手段を高い採用率で持つ相手にあたるため、本記事では「有利」の一覧には含めていません。

なお使用率1位・同居率1位のガブリアスはこおりのキバ採用時（採用率49.0%）にドラゴン/じめんの複合弱点で×4の打点が刺さり、A227のいじっぱり型なら最多分布のガブリアス（H2-A32-S32・ようき50.9%、H実数値185）へ197〜232ダメージ（106〜125%）が通ります。ただしきあいのタスキ（採用率40.2%）採用個体には確定1発が成立せず、ようき最多50.9%のS実数値169は積む前のメガギャラドス（S実数値133〜146）を上回り、こだわりスカーフ採用率20.0%の個体も一定数存在するため、先手を取られて打点を返される展開もあり得ます。打点自体は通っても速度・持ち物次第で結果が入れ替わる「互角〜条件付き」の相手であり、本記事では有利な相手には含めていません。

---

## 同居率上位の分析

M-5でギャラドスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" loading="lazy">
    <div class="name">ニンフィア</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" loading="lazy">
    <div class="name">ウルガモス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、こおり技に×4弱点を持ちます。メガギャラドスはこおり技を耐性（×0.5）で受けられるため、こおり打点を持つ相手への引き先になれます。逆にガブリアスはでんき技を無効化できるため、メガギャラドスの弱点であるでんき技をガブリアス側で受けられる関係です。

**ブリジュラス**（2位）ははがね/ドラゴンで、むし・でんき技を耐性（×0.5）、くさ技を×0.25でさらに大きく軽減できます。メガギャラドスの弱点であるこの3タイプをブリジュラスがカバーする一方向の補完関係です。

**ミミッキュ**（3位）はゴースト/フェアリーで、はがね技に×2弱点を持ちます。メガギャラドスははがね技を耐性（×0.5）で受けられ、ミミッキュの弱点をカバーできます。一方でミミッキュはかくとう技を無効化・むし技を耐性（×0.25）で受けられるため、メガギャラドスの弱点であるかくとう・むし技をミミッキュ側が引き受けられます。

**カバルドン**（4位）はじめん単タイプで、でんき技を無効化します。メガギャラドスの弱点であるでんき技をカバルドンが引き受けられる組み合わせです。一方でカバルドンはみず・くさ・こおり技が弱点で、メガギャラドスはみず・こおり技を耐性（×0.5）で受けられるため、この2タイプについては補い合えます。

**マフォクシー**（5位）はほのお/エスパーで、ゴースト・あく技に×2弱点を持ちます。メガギャラドスはゴースト・あく技をいずれも耐性（×0.5）で受けられ、マフォクシー側の弱点をカバーします。一方でマフォクシーはかくとう・くさ・フェアリー技を耐性（×0.5）で受けられるため、メガギャラドスの弱点3タイプをマフォクシー側が引き受ける相互補完の関係です。

**マスカーニャ**（6位）はくさ/あくで、くさ・でんき技を耐性（×0.5）で受けられ、メガギャラドスの弱点2タイプをカバーします。一方でマスカーニャ自身もかくとう・むし・フェアリー技が弱点で、メガギャラドスと重なる部分は他の枠での対応が必要です。

---

## まとめ

M-5のギャラドスは使用率8位から7位へ上昇したシーズンです。

- **りゅうのまい積みアタッカー型が主流です**（りゅうのまい82.3%・じしん76.8%）：たきのぼり（63.1%）とパワーウィップ（57.3%）の採用率差が5.8ppまで縮まり、みずタイプ上位勢の増加を背景に技構成が分散しています
- **メガ進化でみず/ひこう→みず/あくへタイプが変化します**：じめん無効を失う代わりにゴースト・あく・こおりへの耐性とエスパー無効を獲得します（はがね・みず・ほのおはもともと半減）。バシャーモのインファイト（かくとう）は耐性から弱点へ変わり確定1発になります
- **同居率1位はガブリアスです**：こおり技とでんき技を互いに受け合う関係で、メガギャラドスの弱点であるでんき技をガブリアス・カバルドンが引き受ける組み合わせが同居率上位に並んでいます

積む前は環境上位の非スカーフ勢より遅く、りゅうのまいを通す隙をパーティでどう作るかが運用の前提になります。積んだ後の火力・素早さは高水準ですが、こだわりスカーフを持つマスカーニャ・サザンドラには積んでも上から動けない点は変わりません。

---

*関連記事：[メガギャラドス考察 M-4](/blog/gyarados-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/mega-gyarados/)**
