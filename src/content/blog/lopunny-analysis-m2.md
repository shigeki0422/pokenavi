---
title: '【ポケモンチャンピオンズ】メガミミロップ考察 M-2 S135高速+ねこだまし 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率14位のメガミミロップを分析。S135で環境上位の先手をとりつつ、ねこだまし67.4%でパーティをサポート。ようき型・いじっぱり型の使い分けと、スカーフガブリアス対策まで実データをもとに解説します。'
pubDate: '2026-05-22'
draft: false
heroImage: '../../assets/hero-lopunny-m2.png'
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
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0428-00.webp" alt="メガミミロップ" />
  <div>
    <h2 style="margin:0 0 6px">ミミロップ（メガ進化）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:4px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:40px;height:40px;vertical-align:middle" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:40px;height:40px;vertical-align:middle" />
    </div>
    <div style="margin-top:6px;font-size:0.85rem;color:#555">
      使用率 <strong>14位</strong> ／ メガ石採用率（ミミロップナイト）<strong>96.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン開始8日目（2026/05/20）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ミミロップは**使用率14位**を記録しています。メガ石採用率96.4%という圧倒的な数字が示すとおり、ミミロップを使うならほぼ全員がメガ進化を選択しています。

その理由は明快です——**S135という使用率TOP50内トップクラスの素早さ**、**きもったまによるゴーストへの攻撃貫通**、**ねこだましによる先制妨害**の3つが高水準で組み合わさったデザインを持っているからです。

---

## なぜ今メガミミロップが強いのか

### 理由1: S135は環境トップクラス——先手を取り続ける速さ

メガ進化後のすばやさ135は、**使用率TOP50内でメガゲッコウガに次ぐ2番目の速さ**です。以下は使用率TOP50内のS種族値ランキング（速い順・上位抜粋）です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ順位（TOP50内）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（使用率）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">S種族値</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ミミロップとの関係</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0658-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガゲッコウガ（28位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">142</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">↑ 上回られる</td>
</tr>
<tr style="background:#fef9c3">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-weight:bold">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px"><strong>メガミミロップ（14位）</strong>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>135</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">— 基準</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0655-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガマフォクシー（25位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">134</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る（差+1）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">123</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0658-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲッコウガ（素・28位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">122</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガスターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">119</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">115</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">102</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669;font-weight:bold">↓ 上回る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">スカーフガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">153（スカーフ込み）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">↑ 上回られる</td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.8em;color:#666;margin:4px 0">※ TOP50外でより速いポケモン：メガプテラ・メガフーディン（S=150）、メガスピアー（S=145）、ドラパルト（S=142）、メガライボルト（S=135・同速）</p>

スカーフなしではメガゲッコウガ（S=142）にのみ先手を取られ、それ以外のポケモンには先手を取れます。スカーフ持ちではガブリアス（S=153相当）にも上から動かれます。ガブリアスへの打点としてトリプルアクセル（こおり技）が採用されています（後述）。

### 理由2: きもったま——ノーマル・かくとう技の等倍範囲が環境トップクラス

**ノーマル・かくとう技はもともと等倍範囲が広く、弱点を突けるタイプも多い**のが強みです。ただしひこう・フェアリーなど半減タイプも存在し、ゴーストタイプには完全に無効化されていました。きもったまはこの無効を解消し、ノーマル・かくとう技両方をゴーストタイプに通せるようにします。

かくとう技の全18タイプに対する相性を整理すると：

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1">倍率</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">タイプ</th>
</tr>
</thead>
<tbody>
<tr style="background:#fef9c3">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;font-weight:bold;color:#dc2626">×2（弱点）</td>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">ノーマル・いわ・はがね・こおり・あく <span style="color:#555;font-size:0.85em">（5タイプ）</span></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;font-weight:bold;color:#2563eb">×1（等倍）</td>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">かくとう・じめん・ほのお・みず・くさ・でんき・ドラゴン・ゴースト<span style="color:#059669;font-weight:bold">*</span> <span style="color:#555;font-size:0.85em">（8タイプ）</span></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #cbd5e1;font-weight:bold;color:#555">×0.5（半減）</td>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">ひこう・どく・むし・エスパー・フェアリー <span style="color:#555;font-size:0.85em">（5タイプ）</span></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;font-weight:bold;color:#6b7280">×0（無効）</td>
  <td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><span style="text-decoration:line-through;color:#9ca3af">ゴースト</span> → <span style="color:#059669;font-weight:bold">きもったまで等倍に</span> <span style="color:#555;font-size:0.85em">（0タイプ）</span></td>
</tr>
</tbody>
</table>
</div>

<p style="font-size:0.85em;color:#059669;margin:4px 0 12px"><strong>* きもったまにより、かくとう技を「無効」にできるタイプが存在しない状態になります。</strong></p>

きもったまによって相性が変わるのは、使用率TOP50内のゴースト複合ポケモン6体です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1">きもったまなし</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1">きもったまあり</th>
</tr>
</thead>
<tbody>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">8位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0902-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">イダイトウ(オス)</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">等倍 ↑</td></tr>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">10位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0094-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">ゲンガー</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#555;font-weight:bold">半減 ↑</td></tr>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">11位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0681-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">ギルガルド</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">弱点×2 ↑</td></tr>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">19位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0778-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">ミミッキュ</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#555;font-weight:bold">半減 ↑</td></tr>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">26位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0937-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">ソウブレイズ</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">等倍 ↑</td></tr>
<tr style="background:#fff7ed"><td style="padding:6px 10px;border:1px solid #cbd5e1">29位</td><td style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0911-00.webp" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">ラウドボーン</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#6b7280;font-weight:bold">無効</td><td style="padding:6px 10px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">等倍 ↑</td></tr>
</tbody>
</table>
</div>

きもったまなしでは**TOP50内の6体にノーマル・かくとう技が完全に無効化**されます。きもったまがあればすべてにダメージを与えられ、特に**ギルガルド（11位）は無効→弱点×2**という大きな恩恵があります。


### 理由3: 多彩な先制・妨害技が生む柔軟な立ち回り

メガミミロップは単純な高速アタッカーではなく、**サポートとしても機能できる**のが大きな強みです。

- **ねこだまし**（先制・相手を1ターン怯ませる）：67.4%の採用率。S135で確実に先手をとって相手の行動を1ターン封じることで、次のターンの技選択を有利に進められる
- **マッハパンチ**（先制かくとう技）：31.5%採用。つるぎのまいで積んだ後にスカーフ持ちへ打ち込む場面でも活躍
- **とんぼがえり**（22.2%）：S135で先手をとって攻撃しつつ自分が引っ込めるため、相手の反撃を受ける前に後続へ安全に繋げられる対面操作技

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:68%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>136</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">94</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">54</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:48%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">96</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">135</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">580</span>
  </div>
</div>

**S135が最大の個性**です。攻撃136も非常に高く、メガ進化前（76）から60も上昇するため、メガ進化ターン以降はアタッカーとしても機能します。HP65・ぼうぎょ94・とくぼう96は決して高くはなく、被ダメージは大きめなため、先手をとって攻め続けるスタイルが前提になります。

### タイプ・弱点（メガ後）

<div style="display:flex;align-items:center;gap:6px;margin:10px 0">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:40px;height:40px;vertical-align:middle" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:40px;height:40px;vertical-align:middle" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> かくとう</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ゴースト
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> あく
  </td>
</tr>
</tbody>
</table>
</div>

弱点は4タイプと多め。HP65と耐久面は低く、弱点技は一撃で倒されることも多い。特にエスパー・フェアリーはM-2環境に多く（フラエッテ永遠が11位、アシレーヌ・ミミッキュなどフェアリータイプも上位に集中）、これらのポケモンとの対面は基本的に不利です。

---

## 主要型の解説

### 型① ようき AS最速先制型（メイン構成・69.3%）

M-2環境で最も採用率が高い形です。

<div class="build-header">
  <img src="/images/pokemon/pokemon-0428-00.webp" alt="メガミミロップ" style="width:48px;height:48px" />
  <div>
    <strong>ようき AS最速先制型</strong><br>
    <small style="color:#666">性格採用率 69.3%</small>
  </div>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">内容</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき（すばやさ↑ とくこう↓）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>努力値</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき252 すばやさ252（AS）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミロップナイト</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例①</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねこだまし / インファイト / トリプルアクセル / とんぼがえり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例②</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねこだまし / インファイト / マッハパンチ / つるぎのまい</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- S実数値205で、いじっぱり型（S187）では先手を取れないようきマスカーニャ（S192・使用率3位）、おくびょうメガマフォクシー（S204・25位・おくびょう採用率87%）にも先手を取れる
- ようきでS135を確保し、いじっぱり型（S補正なし）と同じS135を維持しながら攻撃も最大まで伸ばせる
- ねこだましで被ダメなしの安定した先制打点を確保しつつ、次のターンにインファイトの高火力やとんぼがえりでの対面操作など状況に応じた器用な動きができる

**弱み:**
- ねこだましは場に出た最初のターンにしか使えないため、一度引いて再出場した場合は使えない

**立ち回りのポイント:**
対戦序盤は先発でねこだまし→後続へのつなぎ、または中盤に疲弊した相手へのインファイトで確定1発圏に持ち込む使い方が一般的です。とんぼがえりを採用した場合は、**S135で先制とんぼがえり→相手の反撃前に後続へ引ける**ため、パーティ全体のサイクル回転率が高まります。

---

### 型② いじっぱり 火力特化型（28.9%）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0428-00.webp" alt="メガミミロップ" style="width:48px;height:48px" />
  <div>
    <strong>いじっぱり 火力特化型</strong><br>
    <small style="color:#666">性格採用率 28.9%</small>
  </div>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">内容</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（こうげき↑ とくこう↓）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>努力値</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき252 すばやさ252（AS）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミロップナイト</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト / とびひざげり / マッハパンチ / つるぎのまい（またはねこだまし）</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- こうげき136×いじっぱり補正（×1.1）= 実質こうげき149相当のパワー
- インファイト・とびひざげりの火力が増し、よりはっきりした確定1発ラインが広がる
- つるぎのまいと組み合わせることで積んだ後のマッハパンチが先制圏内で多くのポケモンを倒せる

**弱み:**
- S実数値がようき（205）より低い187にとどまるため、ようきマスカーニャ（S192）やおくびょうメガマフォクシー（S204）に先手を取られる
- ねこだましを採用しない場合、先制で相手の行動を封じる手段がなくなる

**いじっぱり型の採用意義:**
A実数値がようき（188）に対していじっぱり（206）と約10%高く、ようき型では2発必要な相手を1発で倒せるケースが生まれます。特につるぎのまい後（A412相当）はその差がさらに広がります。一方で、ようきマスカーニャ（使用率3位）やおくびょうメガマフォクシー（25位）に先手を取られるリスクを受け入れる選択です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">解説</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねこだまし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>67.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制技（優先度+3）・相手を1ターン怯ませる。優先度が高いため相手のSに関わらず確実に先手をとれる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>62.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力120の安定命中かくとう技。使用後ぼうぎょ・とくぼうが各1段階下がるデメリットあり。きもったまでゴーストにも有効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリプルアクセル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>43.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">20×3</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3回連続で当たるこおり技。スカーフガブリアスへの対抗手段として採用。命中率90%（3発全部で約73%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とびひざげり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>31.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力130の高火力かくとう技。命中90%・外れると自分がダメージを受けるリスクあり。インファイトとの差別化ポイントはデメリット内容</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マッハパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>31.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制かくとう技（優先度+1）。きもったまでゴーストにも有効。つるぎのまい後のフィニッシュ手段</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>30.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき2段階アップ。A136→272相当になり、多くのポケモンを確定1発圏に</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>メガトンキック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>23.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ノーマル一致の高火力技。かくとう技を半減するひこう・どく・むし・エスパー・フェアリータイプへ等倍で通る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>22.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に自分が交代できる。S135で先手をとって攻撃しつつ有利な後続に繋げるサイクル技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>21.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">安定命中のこおり技。ガブリアス（ドラゴン/じめん・使用率1位）、カイリュー（ドラゴン/ひこう・16位）にこおり×4で刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガインパクト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>13.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">150</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力150の大技だが使用後1ターン反動で動けない。つるぎのまいとの組み合わせで確定1発フィニッシャーとして採用</td>
</tr>
</tbody>
</table>
</div>

### 技の選択方針

**必須枠（2〜3枠）:** ねこだまし＋インファイト（またはとびひざげり）は多くの構成で採用されます。

**選択枠（1〜2枠）:** 以下の中からパーティの役割に応じて選択します。
- **スカーフガブリアス対策:** トリプルアクセル（43.9%）
- **先制フィニッシュ:** マッハパンチ（31.5%）
- **積み型:** つるぎのまい（30.6%）
- **後続つなぎ:** とんぼがえり（22.2%）
- **かくとう耐性対策:** メガトンキック（23.6%）またはれいとうパンチ（21.2%）

---

## パーティ構成

### 苦手なポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策手段</th>
</tr>
</thead>
<tbody>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0670-05.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フラエッテ（永遠）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー技持ち。サポート役として対面すると大きな被害を受ける可能性</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（等倍）で先手からの削りを狙う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">スカーフガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ込みS153でメガミミロップ（135）を上回り、こちらが先手を取れない数少ない相手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（こおり技3連打）が対抗手段</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこう複合。インファイトが等倍かつひこうタイプでこちらの弱点を突ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガトンキック（ノーマル技）で対抗可能</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリー複合。かくとう技を半減し弱点を突けないうえ、高い耐久でこちらの攻撃を受けつつフェアリー技でこちらの弱点を突ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">有効打が乏しく対面は不利。受け出しを許さない立ち回りが必要</td>
</tr>
</tbody>
</table>
</div>

### 相性の良いパーティパートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">フェアリー半減</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">フェアリー半減・受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">高火力補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ">
    <div class="name">ドリュウズ</div>
    <div class="rate">ステロ+削り</div>
  </div>
</div>

**パーティ構成のポイント:**
1. **フェアリー対策枠**が重要：アシレーヌ・フラエッテ（永遠）などミミロップの弱点を突くフェアリータイプに対し、フェアリーを半減するはがねタイプ（アーマーガア・ブリジュラス）で受けられる構成が望ましい
2. **ねこだまし活用の後続**：ねこだましで相手の行動を1ターン封じた後、こちらは自由に技を選択できる。とんぼがえりで後続に繋ぐか、インファイトで攻めるかをその場で判断できるのがメガミミロップの強み

---

## まとめ：型比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">採用率目安</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">得意場面</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">最速先制型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">AS</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ねこだまし / インファイト / トリプルアクセル / とんぼがえり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">69.3%（性格採用率）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">先発でサポート・スカーフガブリアス対策</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">火力特化型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">AS</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">インファイト / とびひざげり / マッハパンチ / つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">積み後のワンパン狙い・先制技フィニッシュ</td>
</tr>
</tbody>
</table>
</div>

メガミミロップはM-2環境において、**S135高速**・**きもったまによるゴースト貫通**・**ねこだましによる先制サポート**という3つの特性を組み合わせた立ち回りが強みです。ようき最速型が主流（69.3%）というデータが示すように、現環境では純粋な速度を活かしたサポート型運用が最も評価されています。

弱点の多さ（かくとう・ひこう・エスパー・フェアリー）と耐久の低さは無視できませんが、「先手をとり続けること」を前提とした立ち回りで、パーティの要として機能できます。特に環境上位に多いフェアリータイプ（アシレーヌ・フラエッテ永遠など）への対策枠を用意したうえで、メガ枠に採用する価値は十分にあります。
