---
title: '【ポケモンチャンピオンズ】メガリザードンY考察 M-2 ひでり特殊エース 採用型と晴れ展開の解説'
description: 'M-2シーズンで使用率5位のリザードン。63.6%が選ぶメガリザードンYを徹底分析。C159×ひでりのトップクラス火力、ソーラービーム即発動による技範囲の広さ、いわ4倍弱点への対策まで実データをもとに解説します。'
pubDate: '2026-05-22'
draft: true
heroImage: '../../assets/hero-charizard-y-m2.png'
---

<style>
.poke-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  vertical-align: middle;
  margin-right: 4px;
}
.poke-icon-lg {
  display: block;
  width: 80px;
  height: 80px;
  margin: 0 auto 8px;
}
.type-badge {
  display: inline-block;
  width: 52px;
  height: 52px;
  vertical-align: middle;
  margin: 2px;
}
.type-badge-sm {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin: 1px 2px;
}
.item-icon {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin-right: 4px;
  object-fit: cover;
}
.pokemon-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 20px 0;
}
.pokemon-header img {
  width: 96px;
  height: 96px;
}
.type-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 8px 0;
}
.build-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.partner-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 12px;
  margin: 16px 0;
}
.partner-card {
  text-align: center;
  padding: 8px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
}
.partner-card img {
  width: 56px;
  height: 56px;
  display: block;
  margin: 0 auto 4px;
}
.partner-card .name {
  font-size: 0.75rem;
  font-weight: bold;
}
.partner-card .rate {
  font-size: 0.7rem;
  color: #666;
}
</style>

<div class="pokemon-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" />
  <div>
    <h2 style="margin:0 0 8px">メガリザードンY</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      使用率 <strong style="color:#dc2626">5位</strong>（リザードン全体） ／
      メガ石採用率 <strong style="color:#ea580c">63.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

M-2シーズンシングルバトルでリザードン全体は**使用率5位**を記録。そのうち実に**63.6%がリザードナイトYを採用**しており、メガリザードンXの34.9%を大きく上回っています。この差はひとえに**ひでり＋C159という突出した特殊火力**から来ています。メガ進化した瞬間から天候「にほんばれ」が発動し、ほのお技が1.5倍になるだけでなく、相手の天候パーティへのカウンターとしても機能する万能性——それがM-2環境でYが主流となっている最大の理由です。

---

## なぜ今、メガリザードンYが強いのか

### 1. C159×ひでりの実質火力はトップクラス

メガリザードンYのとくこうは**159**。これだけでも環境トップクラスの数値ですが、とくせい**ひでり**によってメガ進化と同時に「にほんばれ」が発動し、ほのお技が×1.5倍になります。かえんほうしゃ（威力90）の実質ダメージ計算をすると:

<div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:14px;margin:16px 0;font-size:0.9em">
  <strong>かえんほうしゃ実質威力（ひでり補正あり）</strong><br>
  <span style="font-size:1.1em;color:#ea580c">
    威力90 × タイプ一致補正1.5 × ひでり1.5 = <strong>実質威力202.5</strong>
  </span><br>
  <small style="color:#777;margin-top:4px;display:block">※さらにひかえめ補正（×1.1）がかかる場合は実質222以上</small>
</div>

ひでりの恩恵は「天気を無料で展開できる」だけでなく、**毎ターンほのお技が安定して最大火力を発揮する**という点で、他のほのおタイプとの差別化要因になっています。

### 2. ソーラービーム即発動で技範囲が劇的に広がる

通常のソーラービームは2ターンかかりますが、にほんばれ状態では**1ターンで即発動**します。ソーラービームの採用率が61.0%という高さを誇るのは、ひでりとのシナジーによってくさが2倍以上通る相手に対して打点を持てるからです。たとえばカバルドン（じめん単）はくさ×2、イダイトウ（みず/ゴースト）はくさ×2×1=×2でいずれも弱点。一方ガブリアス（ドラゴン/じめん）はくさ×2×0.5=等倍止まりですが、それでもC159の高火力で削りを入れられます。

### 3. 天候パーティへのカウンター兼リーダー役

M-2環境では天候パーティとの対面が想定されます。相手がすなあらしや雨パを使う場合でも、メガリザードンYのひでりは**メガ進化した瞬間に相手の天候を上書き**します（ただし「にほんばれ」の持続は天候設置ターンに依存）。自パーティに天候アタッカー（ひでりで強化されるほのおタイプなど）を入れることで、メガリザードンYが展開した後に後続が恩恵を受ける「天候パーティ」としての運用も強力です。

---

## 基本スペック

### 種族値（メガリザードンY）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">104</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:79.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">159</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:57.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">115</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">634</span>
  </div>
</div>

C159は現環境の特殊アタッカーの中でもトップクラスの数値です。とくぼう115はXの85と比べて大幅に高く、特殊受けとして後出しされる相手にも打ち合えます。一方でぼうぎょ78は低く、物理攻撃への耐性は高くありません。すばやさ100は中速圏で、おくびょう最速にしてもS100族止まり。環境TOP30のうちマスカーニャ（S123）・ゲッコウガ（S122）・スターミー（S115）・ゲンガー（S110）・ミミロップ（S105）・マフォクシー（S104）・ガブリアス（S102）はYより速く、上から動けない。特にガブリアスはS102で先にがんせきふうじ（いわ4倍）を通せる点が致命的で、Yの素早さは「上を取れる相手」より「抜けない上位」を意識して立ち回る必要がある。**おくびょう最速かひかえめCSの選択**が重要になる。

### メガ進化前後の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px;border:1px solid #cbd5e1">メガ後（Y）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">変化量</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px;border:1px solid #cbd5e1">84</td>
  <td style="padding:8px;border:1px solid #cbd5e1">104</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+20</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1">78</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">109</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">159</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+50</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px;border:1px solid #cbd5e1">115</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">+30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1;color:#94a3b8">±0</td>
</tr>
</tbody>
</table>
</div>

とくこう+50という変化量はXの+21と比べて大きく上回ります。さらにとくぼう+30によりD115となり、特殊耐久が大幅強化されています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効・耐性</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;background:#fee2e2">
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> <strong>いわ（4倍）</strong>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> みず<br>
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> でんき
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    じめん <strong>無効</strong>（ひこうタイプ）<br>
    ほのお½ / くさ½ / むし½ / かくとう½
  </td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fee2e2;border:1px solid #fca5a5;border-radius:8px;padding:12px;margin:12px 0">
  <strong style="color:#dc2626">⚠️ いわ4倍弱点は致命的</strong><br>
  メガリザードンYの最大の弱点は<strong>いわタイプへの4倍弱点</strong>です。ステルスロック（ステロ）が設置されている状態で登場すると、最大HPの<strong>1/2ダメージ</strong>を受けます（通常は1/4、4倍弱点は1/2）。ガブリアス（がんせきふうじでいわ4倍を直接突く）や、カバルドン（ステルスロック設置でYの後出しに1/2を蓄積させる）など、環境上位のいわダメージ源との対面は致命的です。<strong>ステロ対策ポケモンとのセット採用が必須</strong>です。
</div>

---

## 主要型の解説

### 型1: ひでりソーラービーム型（ひかえめ・CS）

<div style="background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>ひでりソーラービーム型</strong><br>
    <small style="color:#555">C32 S32 ／ ひかえめ（最多採用）</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#fef3c7">
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #fcd34d;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">1</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひでり込みで実質202.5。安定した主力技</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">2</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-11-grass.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひでりで即発動。みず・じめん・いわへの打点</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #fcd34d">3</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-02-flying.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">ひこう一致技。かくとう・むし・くさへ。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:6px 10px;border:1px solid #fcd34d">4</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #fcd34d;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #fcd34d">最大火力の捨て技。フィニッシュに。命中90%・C-2</td>
</tr>
</tbody>
</table>
</div>
</div>

**採用率データとの照合**: ソーラービーム61.0%・かえんほうしゃ42.4%・エアスラッシュ32.9%・オーバーヒート26.6%という実データがこの型を裏付けています。

**ひかえめCS振りの優位性**: 種族値C159にひかえめ補正（×1.1）がかかり、ダメージ計算上はおくびょう型より約1割高い特殊火力になります（実数値そのものはEV振りとレベルで決まるため、ここでは性格補正分の伸びを指します）。ひでり込みのかえんほうしゃはD無振りのほとんどのポケモンを確定2発以内に取れます。相手がCS振りでなくHB振りのポケモンでも、ひでり×タイプ一致補正込みの高威力で突破できるケースが多い。

**ソーラービームの刺さり先**: くさが2倍以上通る相手への打点として機能します。環境上位では:
- **カバルドン**（じめん単）: くさ×2弱点を突ける。ステロ撒きの起点役を即発動ソーラービームで牽制できる
- **イダイトウ**（みず/ゴースト）: くさ×2×1=×2弱点を突ける
- **ガブリアス**（ドラゴン/じめん）: くさ×2×0.5=等倍止まりだがC159の威力で削りは入る

---

### 型2: おくびょう最速型（おくびょう・CS）

<div style="background:#f0fdf4;border:1px solid #4ade80;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>おくびょう最速型</strong><br>
    <small style="color:#555">C32 S32 ／ おくびょう（30.0%採用）</small>
  </div>
</div>

<div style="overflow-x:auto">
<table style="width:100%;border-collapse:collapse;font-size:0.88em">
<thead>
<tr style="background:#dcfce7">
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">スロット</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">技</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #86efac;text-align:left">用途</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">1</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #86efac">安定打点。ひでり込みでトップクラスの火力</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">2</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-11-grass.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #86efac">ひでりで即発動。みず/いわ/じめんへの打点</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #86efac">3</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-02-flying.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #86efac">ひこう一致打点。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#f0fdf4">
  <td style="padding:6px 10px;border:1px solid #86efac">4</td>
  <td style="padding:6px 10px;border:1px solid #86efac"><strong>はねやすめ</strong></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center"><img src="/images/types/type-00-normal.png" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #86efac;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #86efac">HP50%回復。S高い分先に動いて回復できる</td>
</tr>
</tbody>
</table>
</div>
</div>

**おくびょうvs.ひかえめの選択**: おくびょうにするとSが最速100族になり、S無振り同速グループを確実に上から抜けます。ひかえめ比でCが1.1→1.0に下がりますが、先手を取れる相手の範囲が広がることで**Cに振った火力を活かす機会が増える**という考え方もあります。M-2の採用率ではひかえめ32.7%・おくびょう30.0%と拮抗しており、環境のS100ラインポケモンの多さによって選択が変わります。

---

### 型3: ステロケア意識型（ひかえめ・HB+CS）

<div style="background:#eff6ff;border:1px solid #93c5fd;border-radius:8px;padding:14px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <div>
    <strong>HB+CS複合型</strong><br>
    <small style="color:#555">H32 B20 C11 S3（4.6%採用）</small>
  </div>
</div>

<p style="font-size:0.88em;color:#555;margin:8px 0">
Yの最大の問題はステロによる1/2ダメージとぼうぎょの低さです。この型はBにEVを少し振ることで、物理打点（特にガブリアスのじしん等）への耐性を確保しながら特殊火力も維持するバランス型です。採用率4.6%と低いですが、ステロが撒かれやすい環境への対応策として存在感があります。
</p>
</div>

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">用途・補足</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>ソーラービーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>61.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひでりで即発動。Y最多採用技。くさが2倍以上通る相手への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひでり×一致補正込みで実質202.5。安定したほのお打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう一致技。かくとう・くさへ。命中95%・ひるみ30%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中90%・C-2の代わりに最大火力。ひでり込みで実質292.5</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> <strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP50%回復。S優位を活かして先に回復できる場面も</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.85em;color:#666;margin:8px 0">
※採用率データ（X/Y合算）にはフレアドライブ33.3%・ニトロチャージ28.9%も含まれますが、これらは物理アタッカーであるメガリザードンX型の技です。C159の特殊運用が前提のY型では採用されないため、上表からは除外しています。
</p>

---

## 天候パーティ構築でのメガリザードンY

メガリザードンYの最大の特徴はひでりの「天候パーティリーダー」としての役割です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#fff7ed">
  <th style="padding:8px 12px;border:1px solid #fed7aa;text-align:left">ひでり恩恵ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #fed7aa;text-align:left">恩恵内容</th>
  <th style="padding:8px 12px;border:1px solid #fed7aa;text-align:left">パーティでの役割</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #fed7aa"><img src="/images/types/type-09-fire.png" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ほのおタイプ全般</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">ほのお技×1.5倍</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">ウルガモスなど後続が強化</td>
</tr>
<tr style="background:#fffbeb">
  <td style="padding:8px 12px;border:1px solid #fed7aa"><img src="/images/types/type-11-grass.png" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ソーラービーム持ち</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">2ターン→1ターン即発動</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">くさタイプへの広範囲対応</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #fed7aa">葉緑素（ようりょくそ）持ち</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">S2倍</td>
  <td style="padding:8px 12px;border:1px solid #fed7aa">超高速くさタイプアタッカーとして機能</td>
</tr>
</tbody>
</table>
</div>

**重要な点**: 相手がすなあらしや雨を展開していても、**メガ進化と同時ににほんばれで上書き**します。ただし相手が後から天候変化技を使う、または相手もひでり持ちを繰り出した場合は上書きされます。M-2では天候パーティへのカウンターとしてメガリザードンYを採用するケースも見られます。

---

## 弱点となる相手ポケモンと対策

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#fee2e2">
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">天敵ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">理由</th>
  <th style="padding:8px 12px;border:1px solid #fca5a5;text-align:left">対策パートナー案</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（使用率1位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">S102でYのS100を上から抜く。がんせきふうじ（いわ）が4倍弱点。さらにステルスロック84%・じしん採用率99%でYの起点を作る</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アーマーガア・ハッサム</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #fca5a5"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（使用率7位）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">じめん単タイプ。ステルスロック84%を撒きYの後出しに1/2ダメージを蓄積させる起点役（いわ技採用はほぼゼロのため直接の打点は持たない）</td>
  <td style="padding:8px 12px;border:1px solid #fca5a5">アーマーガア（デフォグでステロ除去）</td>
</tr>
</tbody>
</table>
</div>

---

## 相性の良いパーティメンバー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">ステロ除去・物理受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">いわ対策・フェアリー対策</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">自軍ならステロ展開役（対面では天敵）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">いわ受け・相互補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド">
    <div class="name">ギルガルド</div>
    <div class="rate">いわ受け・特殊耐性</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム">
    <div class="name">ハッサム</div>
    <div class="rate">フェアリー・いわ対策</div>
  </div>
</div>

**アーマーガアが最重要パートナー**: メガリザードンYにとって最も危険なのはステロによる1/2ダメージです。アーマーガアはデフォグでステロを除去でき、さらにガブリアスのじしんをひこうタイプで無効化、がんせきふうじ（いわ）も耐性で受けられます。具体的な運用は「初手でガブリアス等のステロ撒きを誘い、アーマーガアでデフォグ→ステロのない盤面でメガリザードンYを後出し」という流れ。これによりYは登場時の1/2ダメージを回避し、満タンからかえんほうしゃ・ソーラービームの確定数計算通りに殴れます。

**ガブリアスは自軍採用と対面で役割が逆**: 上記の天敵表のガブリアスは「相手の」ガブリアスを指します。自軍に採用する場合はステロ撒き・物理崩し役として優秀で、Yのいわ4倍を突いてくる相手（カバルドンなど）への先制ステロ返しにも使えます。

**天候パーティとの組み合わせ**: ひでりが発動した後、**ウルガモス（ほのおタイプ・ひでり恩恵）**などを後続に置くことで、メガリザードンYが倒された後も後続のほのお技×1.5を維持できます。

---

## XとYの使い分けまとめ

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:10px 14px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1">メガリザードンX</th>
  <th style="padding:10px 14px;border:1px solid #cbd5e1;background:#fefce8">メガリザードンY</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">採用率</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">34.9%</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>63.6%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">主力の向き</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">物理崩し・積みエース</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>特殊崩し・天候展開</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong style="color:#dc2626">159</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくせい</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">かたいツメ（接触技×1.3）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>ひでり（ほのお×1.5）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">最大弱点</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">4倍弱点なし（5種2倍）</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2"><strong>いわ4倍（ステロ1/2）</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ステロダメージ</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">1/4</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fee2e2"><strong>1/2（致命的）</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">積み技</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">りゅうのまい / ニトロチャージ</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">なし（火力押し）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">天候シナジー</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">なし</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;background:#fefce8"><strong>天候パーティのリーダー</strong></td>
</tr>
<tr>
  <td style="padding:8px 14px;border:1px solid #cbd5e1;text-align:left;font-weight:600">Yを選ぶ状況</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px 14px;border:1px solid #cbd5e1">火力押し・天候展開・特殊受けの多い環境</td>
</tr>
</tbody>
</table>
</div>

---

## データ分析①：ひでり補正が生む実質火力 — 通常のほのおアタッカーとの比較

メガリザードンYの最大の強みである「C159×ひでり」の火力を定量的に示します。かえんほうしゃの実質威力を条件別に比較すると以下の通りです。

| 条件 | 実質威力（かえんほうしゃ） | 計算式 |
|---|---|---|
| 一般的なほのおアタッカー（タイプ一致のみ） | 135 | 威力90×1.5 |
| メガリザードンY（おくびょう・ひでりあり） | 202.5 | 威力90×1.5×1.5 |
| **メガリザードンY（ひかえめ・ひでりあり）** | **222** | **威力90×1.5×1.5×1.1** |

ひかえめCS型のかえんほうしゃ（実質222）は、一般的なほのおアタッカー（実質135）と比べると**約1.65倍の火力**を誇ります。同じ技名でも受けるダメージはまったく別物です。

ソーラービームが採用率1位（61.0%）である理由も定量的に説明できます。通常は2ターン必要なソーラービームが、ひでり下では1ターンで即発動します。つまり「みず/いわ/じめんへの打点」を**タイムコストゼロで追加できる**という効果です。かえんほうしゃで通常の相手を処理しながら、弱点タイプにはソーラービームで対応するという構成が、ひでりがある限りほぼノーコストで成立するためソーラービームの採用が合理的になっています。

また、オーバーヒートはひでり込みで実質威力292.5（威力130×1.5×1.5）に達します。C-2デメリットを受け入れた上でも、この1発でほとんどのポケモンを確定圏内に捉えられるため、26.6%という一定の採用率が維持されています。

**この火力が立ち回りに与える示唆**は「弱点を突かない相手すら2発で落とせる」点にあります。ひかえめCS型のかえんほうしゃ（実質222）は、ほのおを等倍で受けるカバルドン（じめん単・使用率7位）のようなHB寄りの高耐久にも刺さり、ソーラービーム（くさ×2弱点）と合わせれば確定2発が見込めます。一方で**逆算すると弱点を突かれた側のYは1発で沈む**——ガブリアスのがんせきふうじ（いわ4倍）はYに対し、ステロ1/2の蓄積がなくても高乱数〜確定1発の圏内です。つまり「Yは殴り合えば2発で大半を落とすが、いわ技には触れた瞬間に落ちる」という非対称性こそが、ステロ管理と素早さラインの見極めが勝敗を分ける理由になっています。

---

## まとめ

メガリザードンYはM-2シーズンで全リザードン採用の**63.6%**を占める、トップクラスの特殊アタッカーです。

- **C159×ひでり**の組み合わせでかえんほうしゃの実質威力は202.5——安定した超火力
- **ソーラービーム即発動**によりくさが2倍以上通る相手への打点を確保できる広い技範囲
- **いわ4倍弱点・ステロ1/2ダメージ**は致命的→アーマーガアなどのステロ対策ポケモンとのセットが前提
- **天候パーティのリーダー**として後続ポケモンへ恩恵を与えるパーティ全体設計が可能
- **ひでり天候展開を軸にしたパーティ構築**が最大の強みを引き出す

いわ4倍という大きなリスクを抱えながらも、それを補って余りある圧倒的な特殊火力がM-2環境でYを選ぶ筆頭の理由です。**ステロを撒かせない守りの構築**と組み合わせることで、メガリザードンYはトップクラスの火力砲台として機能します。
