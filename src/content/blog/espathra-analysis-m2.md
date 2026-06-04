---
title: '【ポケモンチャンピオンズ】クエスパトラ考察 M-2 使用率36位 かそくバトン積みエースの型と立ち回り'
description: 'M-2シングルバトルで使用率36位のクエスパトラを徹底分析。かそく+めいそう+ルミナコリジョンの積みエース型と、バトンタッチ採用率79.9%による起点作り型の2系統を実データで解説。EV振り・持ち物・環境上位との相性・苦手なポケモンと対策まで数値で紹介します。'
pubDate: '2026-06-04'
draft: true
---

<style>
.poke-header { display:flex; align-items:center; gap:16px; margin:20px 0; }
.poke-header img { width:96px; height:96px; }
.build-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.item-icon { display:inline-block; width:32px; height:32px; vertical-align:middle; margin-right:4px; object-fit:cover; }
.partner-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(120px,1fr)); gap:12px; margin:16px 0; }
.partner-card { text-align:center; padding:8px; border:1px solid #e2e8f0; border-radius:8px; }
.partner-card img { width:56px; height:56px; display:block; margin:0 auto 4px; }
.partner-card .name { font-size:0.75rem; font-weight:bold; }
.partner-card .rate { font-size:0.7rem; color:#666; }
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0956-00.webp" alt="クエスパトラ" />
  <div>
    <h2 style="margin:0 0 8px">クエスパトラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">36位</strong>　特性: <strong>かそく 99.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、クエスパトラは**使用率36位**。特性は**かそく**（採用率99.5%）でほぼ一択です。毎ターン終了時にすばやさが1段階ずつ上がり、ターンを重ねるほど相手を上から殴れるようになります。

クエスパトラの戦い方は大きく2系統に分かれます。1つは**めいそう＋ルミナコリジョン**で耐久と火力を同時に高めて全抜きを狙う積みエース型、もう1つは**バトンタッチ**（採用率79.9%）でかそくの素早さ上昇やめいそうの積みを後続に渡す起点作り型です。どちらもエスパー単タイプの素直な並耐久を、特性とめいそうで補って戦う点が共通しています。

---

## なぜクエスパトラが使われるのか

### 1. かそくで後手スタートから先手を奪い返せる

クエスパトラのすばやさ種族値は**105**。素のままではガブリアス（S102）はかろうじて抜けますが、マスカーニャ（S123）・ゲンガー（S110）・リザードン（S100、最速個体）といった高速勢には初手で先手を取れません。しかし**かそく**で1ターン経過するごとにすばやさが1段階（×1.5）上がるため、まもるやみがわりで1ターン凌げば、2ターン目以降は環境のほぼ全てを上から動けるようになります。

おくびょうですばやさ最大振り（S32）のクエスパトラはすばやさ実数値が約172。かそく1段階で約258となり、スカーフガブリアス（すばやさ実数値約253）すら上回ります。「初手は遅いが、生き残るほど手が付けられなくなる」という時間差の脅威が最大の武器です。

### 2. めいそう＋ルミナコリジョンで詰めの火力を作る

ルミナコリジョン（採用率90.4%）はエスパー特殊技（威力80）で、**命中後に相手の特防を2段階下げる**追加効果を持ちます。めいそう（採用率73.9%）で自分のとくこう・とくぼうを上げながらルミナコリジョンを撃てば、相手の特防はみるみる下がり、受け出してきた特殊受けも数発で崩せます。とくこう種族値101とかそくによる素早さ上昇が噛み合い、「積んで・上から・特防を割って抜く」という詰め筋が成立します。

### 3. バトンタッチで積んだ起点を引き継げる

バトンタッチ（採用率79.9%）はクエスパトラの技の中で2番目に高い採用率です。かそくで上がったすばやさやめいそうのとくこう・とくぼう上昇を、まるごと後続のアタッカーに引き継げます。クエスパトラ自身が苦手な相手（後述のあく・ゴースト勢）が出てきても、起点だけ作って高速アタッカーにバトンを繋ぐ動きができるため、単体で完結しなくても仕事ができるのが採用理由になっています。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">101</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">105</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">481</span>
  </div>
</div>

とくこう101・すばやさ105を軸にした特殊アタッカー寄りの配分です。HPは95と高めですが、ぼうぎょ・とくぼうがともに60と低く、無補正・無振りのままでは弱点を突かれずとも手痛いダメージを受けます。このため積み技めいそうやずぶとい＋HB振りで耐久を底上げする型が主流になっています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="エスパー" />
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
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
</tr>
</tbody>
</table>
</div>

エスパー単タイプの弱点はむし・ゴースト・あくの3つです。問題は、このうちあく・ゴーストが環境上位に多い点です。マスカーニャ（くさ/あく・3位）・ゲンガー（ゴースト/どく・10位）・ミミッキュ（ゴースト/フェアリー・19位）・サザンドラ（あく/ドラゴン・21位）・ドドゲザン（あく/はがね・24位）など、TOP30に弱点タイプを持つアタッカーが並びます。耐久が低いため、これらに先手を取られると積む前に崩されやすいのが構造的な弱点です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ルミナコリジョン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中後に相手のDを2段階ダウン。メインウェポン兼崩し技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バトンタッチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かそくのS上昇・めいそうの積みを後続へ引き継ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>73.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">CとDを1段階ずつアップ。火力と特殊耐久を同時に強化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>67.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃を防ぎつつ、かそくでSを1段階上げるターン稼ぎ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー特殊技。あくタイプ（サザンドラ等）への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みがわり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">状態異常・先制技を防ぎながらかそくのターンを稼ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト・エスパー（同族のスターミー等）への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アシストパワー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20〜</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">能力上昇1段階ごとに威力+20。めいそう・かそくを積むほど高威力</td>
</tr>
</tbody>
</table>
</div>

ルミナコリジョン・めいそう・まもるが3本柱で、4枠目をバトンタッチ・マジカルシャイン・みがわりから選ぶ構成が主流です。なお、めいそうとアシストパワーを併用してエスパー一致打点の威力を伸ばす型もありますが、アシストパワーの採用率は5.1%にとどまり、ルミナコリジョン軸が圧倒的多数です。

---

## 主要型の解説

性格分布は**ずぶとい43.1%**（HB耐久型の指標）と、**おくびょう30.1%＋ひかえめ22.2%**（CS抜き型の指標）に二分されます。EV振りでも HB系（合計約32%）と CS系（合計約15%）に分かれており、用途が明確に分かれているのが特徴です。

### 型1: ずぶといHB耐久バトン型（最多採用）

**性格採用率: ずぶとい 43.1%**（HB耐久型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0956-00.webp" alt="クエスパトラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ずぶといHBバトン型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B30 D2 S2（最多のHB+ds型）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・ルミナコリジョン<br>
・めいそう<br>
・バトンタッチ<br>
・まもる / みがわり
</div>
</div>
</div>

**強み:**

ずぶといでぼうぎょを補強し、低い物理耐久を底上げした型です。HB+ds振り（採用率11.6%）が最多で、HP・ぼうぎょに厚く振ります。まもる・みがわりでかそくのターンを稼ぎ、めいそうで特殊耐久も上げてから、上がったすばやさとめいそうの積みを**バトンタッチ**で後続のアタッカーに丸ごと渡せます。クエスパトラ自身が抜き切れなくても、起点だけ作って高速エースに繋ぐ動きが軸になります。

オボンのみはHPが半分以下になった時に最大HPの約25%を回復し、めいそうやまもるで粘る時間を延ばします。

**弱み:**

物理方向に厚く振る分、とくこうは無補正・無振りで火力が低く、ルミナコリジョン単発では押し切れません。バトンタッチで繋ぐ受け先がいないと仕事が薄く、構築単位での組み立てが前提になります。また、あく・ゴースト技を持つ高速勢（後述）に先手で弱点を突かれると、まもるを読まれた際に積む前に崩されます。

---

### 型2: CS抜き型（2番目の構成）

**性格採用率: おくびょう 30.1% / ひかえめ 22.2%**（CS抜き型の指標。両者で性格分布の過半数）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0956-00.webp" alt="クエスパトラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">おくびょうCSアタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> おくびょう（S↑ A↓）/ ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> C32 S32 H2（最多のCS+h型）<br>
<strong>持ち物:</strong> きあいのタスキ / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ルミナコリジョン<br>
・めいそう<br>
・マジカルシャイン / シャドーボール<br>
・まもる / みがわり
</div>
</div>
</div>

**強み:**

すばやさ・とくこうに最大振りして、めいそうから自分で全抜きを狙う型です。おくびょうS32ですばやさ実数値約172、かそく1段階で約258となり、スカーフガブリアス（すばやさ実数値約253）すら追い抜けます。めいそうを1回積めばとくこうが上がり、ルミナコリジョンの特防2段階ダウンと合わせて、特殊受けも数発で崩せます。マジカルシャインを採用すればあく半減のサザンドラ・ドドゲザンにフェアリー打点で抗える点が耐久型より優れます。

きあいのタスキは、初手で弱点技を受けても1回は確実に行動できるため、かそくで素早さを上げる猶予を作れます。ひかえめ型はおくびょう型より素の素早さが落ちる代わりにとくこう実数値が約10%高く、ルミナコリジョン1発で落とせる耐久ラインが広がります。

**弱み:**

耐久型と違い物理方向に振らないため、ふいうち（ドドゲザン99%・ダイケンキヒスイ66%採用）など先制技で削られると、タスキ前提でも2回目の被弾で落ちます。バトンタッチを切る構成が多く、自身が苦手な相手と対面した時に逃げ筋を持ちにくいのも耐久バトン型にはない弱みです。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、クエスパトラと相性がはっきり出るポケモンを有利・不利の両面から挙げます。クエスパトラはかそくで素早さを上げれば多くの相手を上から動けますが、初手は素のS105どまりで、ぼうぎょ・とくぼうが60と低いため、弱点（むし・ゴースト・あく）を突ける高速勢には積む前に崩されやすい点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素のS105＞S102で先手。弱点を突く技を持たず、めいそうを積めば特殊耐久でじしん以外を流せる。スカーフ型もかそく1段階で抜き返せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S85で先手確保。弱点タイプの技を持たず、めいそう＋ルミナコリジョンの特防ダウンで高D枠も崩せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（採用率99.7%）が先制かつむし/はがねのはがね打点。エスパー一致は等倍で、低耐久のこちらは先制技で削られ積む前に崩れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（採用率99.0%）が×2弱点の先制技。S50だが先制技で上から削られ、こちらのエスパー技はあく無効で通らない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ マジカルシャイン採用なら五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（採用率98.5%）が×2弱点でこちらのエスパー技は無効。マジカルシャイン（フェアリー）採用個体ならあく/ドラゴンに×4で一矢報いられるが、素のS105＜S98は微差で初手次第</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点のむし・ゴースト・あくを突く高速勢と、エスパー技を無効化／半減する相手が苦手です。いずれも使用率TOP30以内の実在ポケモンから選定しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123で素のクエスパトラ（S105）より速く、はたきおとす（採用率57.6%・あく×2）で先手で崩される。とんぼがえりで起点化も拒否される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・フェアリータイプ（ブリジュラス・ピクシー等）を後出ししてあく技を半減で受け、クエスパトラはバトンの受け先に温存する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S110で素のクエスパトラより速く、シャドーボール（採用率71.1%・ゴースト×2）で低耐久のこちらを上から先に落とす。かそくが乗る前の初手が特に危険</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくタイプ（サザンドラ・ドドゲザン等）でゴースト技を半減〜無効化して受ける。タスキで耐えればエスパー技がゲンガーに×2で返せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ばけのかわで1発耐え、かげうち（採用率93.6%・ゴースト×2）の先制技で削られる。つるぎのまい（86.7%）からの全抜きを許すと止まらない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくタイプでかげうち・シャドークローを半減して受け、ばけのかわを剥がしてから倒す。まもるでばけのかわを消費させない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0503-01.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ダイケンキ(ヒスイ)（23位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひけん・ちえなみ（98.2%・あく×2）とふいうち（65.7%・あく×2）のあく打点で崩される。先制技ふいうちを持つためかそくで上を取っても削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく半減のフェアリー（ピクシー）を合わせて受け、ふいうちを読んでまもる・みがわりで透かす</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0036-00.webp" alt="ピクシー">
    <div class="name">ピクシー</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">フェアリーであく技を半減。バトンの受け先や対あく枠として補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0154-00.webp" alt="メガニウム">
    <div class="name">メガニウム</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久で起点を作り、めいそう・かそくのバトン受けにも向く</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがねであく・むし技を半減。苦手なはがね複合への引き先</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん高火力でドドゲザン等はがねあくに打点。バトンの受け先</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでバトンの受け先。高火力でゴースト枠に打点</div>
  </div>
</div>

**パーティ構成の基本方針:**

クエスパトラは弱点のあく・ゴーストが環境に多く単体完結しにくいため、残り5体で以下を補います。

1. **あく・ゴースト対策**: フェアリー（ピクシー）・はがね（ブリジュラス）でマスカーニャ・ゲンガー・ミミッキュの弱点技を半減して受ける枠
2. **バトンタッチの受け先**: かそくのS上昇・めいそうの積みを活かせる高火力アタッカー（ガブリアス・イダイトウ等）
3. **はがねあくへの打点**: ドドゲザンなどエスパー技が通らない相手に、じめん・かくとう等で殴れる枠

---

## データ分析①：ルミナコリジョン90.4%が示す「崩し」への一極集中

クエスパトラの技採用率は、特殊エスパー技の選択がルミナコリジョンに一極集中しているのが特徴です。同じ威力80のエスパー特殊技でも、追加効果のない通常技ではなく、特防を2段階下げるルミナコリジョンが90.4%を占めます。

| 技 | タイプ | 威力 | 追加効果 | 採用率 |
|---|---|---|---|---|
| ルミナコリジョン | エスパー | 80 | 相手のDを2段階ダウン | **90.4%** |
| マジカルシャイン | フェアリー | 80 | なし | 26.5% |
| シャドーボール | ゴースト | 80 | 20%でDダウン | 10.1% |
| アシストパワー | エスパー | 20〜 | 能力上昇で威力増 | 5.1% |

この偏りが示すのは、クエスパトラが「素の火力で殴る」ではなく「**相手の特防を割って崩す**」ことを役割の中心に据えている点です。とくこう種族値は101と中堅で、めいそう1積みだけでは硬い特殊受けを抜き切れません。しかしルミナコリジョンを1発当てれば相手のとくぼうが2段階下がり、めいそうの自己強化と合わせて実質的な火力差が大きく開きます。マジカルシャイン（あく対策）やシャドーボール（同族・ゴースト対策）のサブ枠が採用率で大きく劣るのは、ルミナコリジョンの特防ダウンが「対面の崩し」と「後続バトンへの布石」を同時に担い、サブ打点より優先度が高いと判断されているためです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ずぶといHBバトン型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ずぶとい 43.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ルミナコリジョン・めいそう・バトンタッチ・まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">起点を作り後続に積みを引き継ぐ。物理耐久が高い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">自身の火力が低く受け先必須。先制技に弱い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">CS抜き型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう 30.1% / ひかえめ 22.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう / ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ルミナコリジョン・めいそう・マジカルシャイン・まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">かそく＋めいそうで自分から全抜き。サブ打点で範囲補完</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理耐久が薄くふいうち等で崩れる。逃げ筋が乏しい</td>
</tr>
</tbody>
</table>
</div>

**総評:**

クエスパトラは特性かそくで時間をかけて全環境を上から殴れるようになる、時間差の積みエースです。耐久型はバトンタッチ（採用率79.9%）で起点を後続に渡し、抜き型はめいそう＋ルミナコリジョンの特防ダウンで自ら崩します。

M-2環境ではガブリアス（1位）・ブリジュラス（2位）といった弱点を突けない上位に対し、めいそうを積んで詰める動きが通ります。一方、弱点のあく・ゴースト技を持つマスカーニャ（3位）・ゲンガー（10位）・ミミッキュ（19位）・ドドゲザン（24位）など、先制技や高速の崩し役が環境に多く、積む前に崩されやすいのが使用率36位にとどまる要因です。フェアリー・はがね・あくで弱点をケアする並びを組み、まもる・みがわりでかそくのターンを安全に稼げるかが運用の鍵になります。

---

## 関連記事

- [天敵となる先制技ふいうち持ち ドドゲザンのM-2考察](/blog/kingambit-analysis-m2/)
- [バトンの受け先候補 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [弱点を突く高速あくアタッカー マスカーニャのM-2考察](/blog/meowscarada-analysis-m2/)
