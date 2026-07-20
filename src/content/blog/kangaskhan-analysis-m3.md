---
title: '【ポケモンチャンピオンズ】メガガルーラ 考察 M-3 シーズン 採用型と立ち回り'
description: 'M-3シーズン使用率71位のメガガルーラ考察。M-2の34位から大幅ランクダウンした背景をデータで検証。主流型H27-A32いじっぱりの実数値・おやこあい込みダメージ計算・技択の判断基準を解説します。'
pubDate: '2026-07-03'
updatedDate: '2026-07-03'
heroImage: '../../assets/hero-kangaskhan-m3.png'
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
  <img src="/images/pokemon/pokemon-0115-00.webp" alt="メガガルーラ" />
  <div>
    <h2 style="margin:0 0 8px">メガガルーラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">71位</strong>　特性: <strong>きもったま 90.9%（※メガ後おやこあい）</strong>
    </div>
  </div>
</div>

M-3シーズンのメガガルーラは使用率**71位**。M-2の34位から大幅に順位を落としました。おやこあいによる実質1.25倍打点と先制技ふいうちを軸にした攻撃型は変わりませんが、環境の変化によって立ち位置が変化しています。

## メガガルーラの基本スペック

### 種族値（通常→メガ後）

<div style="overflow-x:auto">
<table style="border-collapse:collapse;width:100%;font-size:0.9em">
<thead><tr style="background:#f3f4f6">
<th style="padding:6px 8px;text-align:left">ステータス</th>
<th style="padding:6px 8px;text-align:right">通常</th>
<th style="padding:6px 8px;text-align:right">メガ後</th>
<th style="padding:6px 8px;text-align:right">変化</th>
</tr></thead>
<tbody>
<tr><td style="padding:6px 8px">HP</td><td style="padding:6px 8px;text-align:right">105</td><td style="padding:6px 8px;text-align:right"><strong style="color:#dc2626">105</strong></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;color:#6b7280">±0</td></tr>
<tr style="background:#f9fafb"><td style="padding:6px 8px">A（こうげき）</td><td style="padding:6px 8px;text-align:right">95</td><td style="padding:6px 8px;text-align:right"><strong style="color:#dc2626">125</strong></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</td></tr>
<tr><td style="padding:6px 8px">B（ぼうぎょ）</td><td style="padding:6px 8px;text-align:right">80</td><td style="padding:6px 8px;text-align:right"><strong style="color:#dc2626">100</strong></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</td></tr>
<tr style="background:#f9fafb"><td style="padding:6px 8px">C（とくこう）</td><td style="padding:6px 8px;text-align:right">40</td><td style="padding:6px 8px;text-align:right">60</td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</td></tr>
<tr><td style="padding:6px 8px">D（とくぼう）</td><td style="padding:6px 8px;text-align:right">80</td><td style="padding:6px 8px;text-align:right"><strong style="color:#dc2626">100</strong></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</td></tr>
<tr style="background:#f9fafb"><td style="padding:6px 8px">S（すばやさ）</td><td style="padding:6px 8px;text-align:right">90</td><td style="padding:6px 8px;text-align:right"><strong style="color:#dc2626">100</strong></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</td></tr>
<tr style="background:#e0f2fe"><td style="padding:6px 8px"><strong>合計</strong></td><td style="padding:6px 8px;text-align:right"><span style="color:#2563eb;white-space:nowrap">490</span></td><td style="padding:6px 8px;text-align:right"><span style="color:#2563eb;white-space:nowrap">590</span></td><td style="padding:6px 8px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</td></tr>
</tbody>
</table>
</div>

特性「おやこあい」：技が2回連続でヒットし、2回目のダメージは1回目の25%。実質的な技の威力倍率は1.25倍相当です。

### タイプ相性（ノーマル単）

<table style="border-collapse:collapse;font-size:0.9em">
<thead><tr style="background:#f3f4f6">
<th style="padding:6px 10px">弱点（×2）</th>
<th style="padding:6px 10px">無効</th>
</tr></thead>
<tbody>
<tr>
<td style="padding:6px 10px"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="height:20px;vertical-align:middle" /></td>
<td style="padding:6px 10px"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="height:20px;vertical-align:middle" /></td>
</tr>
</tbody>
</table>

ノーマル単タイプは弱点がかくとう1種のみです。ただし主力技のねこだまし・のしかかりを含むノーマル技がゴーストタイプに無効になる点は立ち回りに直結します。

## M-3の採用型

持ち物はガルーラナイト89.3%とほぼ固定です。性格はいじっぱり83.9%が主流です。

### 主流型：H27-A32-B5-D1-S1 いじっぱり（15.9%）

<div class="build-header" style="display:flex;gap:1em;flex-wrap:wrap;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1em;margin:1em 0">
<div style="flex:1;min-width:180px">
<strong>特性:</strong> きもったま 87.7%（※メガ後おやこあい）<br/>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br/>
<strong>EV:</strong> H27-A32-B5-D1-S1<br/>
<strong>持ち物:</strong> ガルーラナイト
</div>
<div style="flex:1;min-width:180px">
<strong>技構成:</strong><br/>
ねこだまし / じしん<br/>
れいとうパンチ or ふいうち<br/>
ほのおのパンチ or ドレインパンチ
</div>
</div>

**実数値（メガ後）：H194 A177 B123 D121 S121**

A32いじっぱりでA177を確保しつつ、H27-B5でやや耐久にも配分した型です。S実数値121はS100族無振り（S120）より1高い程度で、S32投入（S136）と比較するとS15低くなります。速さよりも耐久方向に振った型です。

### 素早さ特化型：H2-A32-S32 いじっぱり（10.1%）

<div class="build-header" style="display:flex;gap:1em;flex-wrap:wrap;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1em;margin:1em 0">
<div style="flex:1;min-width:180px">
<strong>特性:</strong> きもったま 87.7%（※メガ後おやこあい）<br/>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br/>
<strong>EV:</strong> H2-A32-S32<br/>
<strong>持ち物:</strong> ガルーラナイト
</div>
<div style="flex:1;min-width:180px">
<strong>技構成:</strong><br/>
ねこだまし / じしん<br/>
れいとうパンチ / ふいうち<br/>
ほのおのパンチ or ドレインパンチ
</div>
</div>

**実数値（メガ後）：H181 A177 S136**

S32投入でS136を確保します。ガブリアス（S151最速）・ゲンガー（S160最速）・サザンドラ（S147最速）・マスカーニャ（S174最速）・ミミッキュ（S145最速）はいずれもS136を上回るため後手になります。先制技のふいうちや、ねこだましによる行動制限で補う立ち回りが前提になります。

### 耐久重視型：H32-A32-S2 いじっぱり（10.1%）

<div class="build-header" style="display:flex;gap:1em;flex-wrap:wrap;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:1em;margin:1em 0">
<div style="flex:1;min-width:180px">
<strong>特性:</strong> きもったま 87.7%（※メガ後おやこあい）<br/>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br/>
<strong>EV:</strong> H32-A32-S2<br/>
<strong>持ち物:</strong> ガルーラナイト
</div>
<div style="flex:1;min-width:180px">
<strong>技構成:</strong><br/>
ねこだまし / じしん<br/>
れいとうパンチ / ふいうち<br/>
ほのおのパンチ
</div>
</div>

**実数値（メガ後）：H196 A177 S121**

H32でH196を確保しながらA177も維持する型です。S2の実数値は121で、主流型（S121）と同値です。HPを優先し確定数を有利にすることで、先手を捨てる代わりに耐久力を得ます。

## おやこあい込みの打点

主要技のおやこあい実質ダメージです。A177（いじっぱり A32）前提。

<div style="overflow-x:auto">
<table style="border-collapse:collapse;width:100%;font-size:0.9em">
<thead><tr style="background:#f3f4f6">
<th style="padding:6px 8px;text-align:left">技（タイプ）</th>
<th style="padding:6px 8px;text-align:right">威力</th>
<th style="padding:6px 8px;text-align:left">対象</th>
<th style="padding:6px 8px;text-align:right">相性</th>
<th style="padding:6px 8px;text-align:left">備考</th>
</tr></thead>
<tbody>
<tr>
<td style="padding:6px 8px"><img src="/images/types/type-14-ice.png" alt="こおり" style="height:18px;vertical-align:middle" /> れいとうパンチ（75）</td>
<td style="padding:6px 8px;text-align:right">75</td>
<td style="padding:6px 8px"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="height:20px;vertical-align:middle"> ガブリアス</td>
<td style="padding:6px 8px;text-align:right">×4</td>
<td style="padding:6px 8px">確定1発（おやこあい込み）</td>
</tr>
<tr style="background:#f9fafb">
<td style="padding:6px 8px"><img src="/images/types/type-16-dark.png" alt="あく" style="height:18px;vertical-align:middle" /> ふいうち（70）</td>
<td style="padding:6px 8px;text-align:right">70</td>
<td style="padding:6px 8px"><img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="height:20px;vertical-align:middle"> ゲンガー</td>
<td style="padding:6px 8px;text-align:right">×2</td>
<td style="padding:6px 8px">先制技（優先度+1）</td>
</tr>
<tr>
<td style="padding:6px 8px"><img src="/images/types/type-16-dark.png" alt="あく" style="height:18px;vertical-align:middle" /> ふいうち（70）</td>
<td style="padding:6px 8px;text-align:right">70</td>
<td style="padding:6px 8px"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="height:20px;vertical-align:middle"> マスカーニャ</td>
<td style="padding:6px 8px;text-align:right">×½</td>
<td style="padding:6px 8px">あく/くさ複合のため半減</td>
</tr>
<tr>
<td style="padding:6px 8px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="height:18px;vertical-align:middle" /> ほのおのパンチ（75）</td>
<td style="padding:6px 8px;text-align:right">75</td>
<td style="padding:6px 8px"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="height:20px;vertical-align:middle"> アーマーガア</td>
<td style="padding:6px 8px;text-align:right">×2</td>
<td style="padding:6px 8px">はがね/ひこうを突く</td>
</tr>
<tr>
<td style="padding:6px 8px"><img src="/images/types/type-04-ground.png" alt="じめん" style="height:18px;vertical-align:middle" /> じしん（100）</td>
<td style="padding:6px 8px;text-align:right">100</td>
<td style="padding:6px 8px"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="height:20px;vertical-align:middle"> ミミッキュ</td>
<td style="padding:6px 8px;text-align:right">×1</td>
<td style="padding:6px 8px">ゴースト/フェアリー：じめん等倍</td>
</tr>
</tbody>
</table>
</div>

じしんはガブリアス（ドラゴン/じめん）に等倍止まりで、れいとうパンチ×4の方が大幅に打点が高くなります。ミミッキュへはゴーストとフェアリーの両タイプを経由するため、ノーマル技は無効・じしんは等倍になります。

## データ分析①：M-2→M-3の技構成の変化

M-2とM-3で技採用率の優先順位が大きく入れ替わりました。

<div style="overflow-x:auto">
<table style="border-collapse:collapse;width:100%;font-size:0.9em">
<thead><tr style="background:#f3f4f6">
<th style="padding:6px 8px;text-align:left">技（タイプ）</th>
<th style="padding:6px 8px;text-align:right">M-2</th>
<th style="padding:6px 8px;text-align:right">M-3</th>
<th style="padding:6px 8px;text-align:right">変化</th>
</tr></thead>
<tbody>
<tr>
<td style="padding:6px 8px">ねこだまし</td>
<td style="padding:6px 8px;text-align:right">45.4%</td>
<td style="padding:6px 8px;text-align:right">68.2%</td>
<td style="padding:6px 8px;text-align:right;color:#059669">+22.8pt</td>
</tr>
<tr style="background:#f9fafb">
<td style="padding:6px 8px">じしん</td>
<td style="padding:6px 8px;text-align:right">75.5%</td>
<td style="padding:6px 8px;text-align:right">62.1%</td>
<td style="padding:6px 8px;text-align:right;color:#dc2626">-13.4pt</td>
</tr>
<tr>
<td style="padding:6px 8px">れいとうパンチ</td>
<td style="padding:6px 8px;text-align:right">76.6%</td>
<td style="padding:6px 8px;text-align:right">61.1%</td>
<td style="padding:6px 8px;text-align:right;color:#dc2626">-15.5pt</td>
</tr>
<tr style="background:#f9fafb">
<td style="padding:6px 8px">ふいうち</td>
<td style="padding:6px 8px;text-align:right">61.8%</td>
<td style="padding:6px 8px;text-align:right">60.5%</td>
<td style="padding:6px 8px;text-align:right;color:#6b7280">-1.3pt</td>
</tr>
<tr>
<td style="padding:6px 8px">すてみタックル</td>
<td style="padding:6px 8px;text-align:right">48.8%</td>
<td style="padding:6px 8px;text-align:right">—</td>
<td style="padding:6px 8px;text-align:right;color:#dc2626">消滅</td>
</tr>
<tr style="background:#f9fafb">
<td style="padding:6px 8px">ドレインパンチ</td>
<td style="padding:6px 8px;text-align:right">10.2%</td>
<td style="padding:6px 8px;text-align:right">16.4%</td>
<td style="padding:6px 8px;text-align:right;color:#059669">+6.2pt</td>
</tr>
<tr>
<td style="padding:6px 8px">のしかかり</td>
<td style="padding:6px 8px;text-align:right">23.8%</td>
<td style="padding:6px 8px;text-align:right">15.2%</td>
<td style="padding:6px 8px;text-align:right;color:#dc2626">-8.6pt</td>
</tr>
</tbody>
</table>
</div>

最大の変化は**ねこだまし採用率が+22.8pt**上昇したことです。M-2の45%から一気に68%まで伸びており、ガルーラを使う側がねこだましを中心に据えた構成にシフトしたことを示しています。逆にすてみタックルはほぼ消滅しました。M-3ではマスカーニャ（スカーフ70.8%でS174）・ミミッキュ（いのちのたま84.6%）が環境上位に多く、後手からすてみタックルで押す戦法より、ねこだましで対面操作・後続の動きを確保する使い方に変わったと見られます。

## データ分析②：使用率71位への下落とマスカーニャの台頭

M-2の34位→M-3の71位という大幅後退の背景を環境上位のデータで検証します。

M-3でS174最速のマスカーニャが**3位**（スカーフ70.8%でS261相当まで加速）に入り、ふいうちが届かない「とんぼがえり+ねこだまし透かし」の対面操作が広まったことがメガガルーラには逆風になりました。マスカーニャのスカーフ採用70.8%は、まずゴースト技でねこだましを透かしながら交代を強いる動きを可能にします。

また、バシャーモ（10位）はきあいのタスキ13.7%・メガバシャーモナイト非採用が大半（持ち物TOP5にメガ石不在）で無メガ運用が多いです。かそく蓄積後はメガガルーラより速くなり、かくとう技の一撃で落とされるリスクがあります。

一方で、ガブリアス（1位）へのれいとうパンチ×4・ゲンガー（29位）へのふいうち×2はおやこあい込みで確定1発圏内に収まります。71位まで落ちながらもガルーラナイト89.3%と型が固定されている点は、「当たれば強い」確実性への評価を反映しています。

## 苦手なポケモン

- **ゴーストタイプ全般**：ねこだまし・のしかかりなどノーマル技がすべて無効です。<img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="height:20px;vertical-align:middle"> ゲンガーにはふいうち×2で対処できますが、ゴーストタイプの透かしを利用した対面操作は全型共通の泣き所です。
- **<img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="height:20px;vertical-align:middle"> メガルカリオ（ルカリオ45位・メガ石採用90.9%）**：S162最速（メガ後）でメガガルーラS136（S32型）を上回ります。かくとう技がガルーラの弱点×2で、受け出し・後続からの打ち合いでも不利です。
- **コノヨザル（46位）**：S138最速でメガガルーラS136（S32型）を上回ります。ふんどのこぶし（かくとう）・ドレインパンチでかくとう弱点を突かれ続けるうえ、ちょうはつ62.6%でねこだまし後の補助技も封じられやすいです。

## 同居率上位の分析

M-3同居率1位〜10位：ガブリアス、ミミッキュ、アシレーヌ、ブリジュラス、マスカーニャ、ゲンガー、アーマーガア、イダイトウ(オス)、リザードン、バシャーモ

同居上位の顔ぶれは「ガルーラ自身が苦手とするゴーストタイプへの打点を持つ」「ガルーラが苦手とするかくとう環境への対処」に分かれます。

- **<img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="height:20px;vertical-align:middle"> ゲンガー（6位）**：ゴーストタイプでバシャーモ・コノヨザル等のかくとう使いを牽制し、ガルーラと選出を分散する役割を担います。
- **<img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="height:20px;vertical-align:middle"> アーマーガア（7位）**：かくとうタイプへの耐性（はがね半減・ひこう半減）を持ち、ガルーラのかくとう弱点をフォローします。
- **<img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="height:20px;vertical-align:middle"> アシレーヌ（3位）**：バシャーモのほのお技・かくとう技を受けられるみず耐性を持ち、ガルーラが苦手とするかくとう環境への対処として同居します。

## 関連記事

- [ガブリアス 考察 M-3](/blog/garchomp-analysis-m3/)
- [マスカーニャ 考察 M-3](/blog/meowscarada-analysis-m3/)

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/mega-kangaskhan/)**
