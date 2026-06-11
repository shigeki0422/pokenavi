---
title: '【ポケモンチャンピオンズ】メガハッサム 考察 M-2シーズン 使用率と型別解説'
description: 'M-2シングルバトルで使用率14位のメガハッサムを徹底分析。テクニシャン+バレットパンチの高水準な先制技、つるぎのまい積みの破壊力、ほのお一点弱点の耐性と対策、いじっぱりHA振りの運用まで実データで解説します。'
pubDate: '2026-06-05'
draft: false
heroImage: '../../assets/hero-scizor-m2.png'
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
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" />
  <div>
    <h2 style="margin:0 0 6px">ハッサム（メガ進化）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:4px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:40px;height:40px;vertical-align:middle" />
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:40px;height:40px;vertical-align:middle" />
    </div>
    <div style="margin-top:6px;font-size:0.85rem;color:#555">
      使用率 <strong>14位</strong> ／ メガ石採用率（ハッサムナイト）<strong>79.1%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30時点）の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ハッサムは**使用率14位**を記録しています。注目すべきはメガ石採用率が79.1%である点で、残り約21%はメガ進化なしで採用されています。これはメタルコート（9.5%）やオボンのみ（4.0%）など、別の持ち物型にも相当の需要があることを示しています。

それでもメガハッサムが強力な理由は明白です——**テクニシャン補正+バレットパンチという高水準の先制技**、**A150+つるぎのまいで積み後の高い火力**、そして**はがね/むしという組み合わせによるほのお一点弱点という安心感**。複数の役割を同時にこなせる万能アタッカーとして、M-2環境で安定した地位を保っています。

---

## なぜ今メガハッサムが強いのか

### 理由1: テクニシャン+バレットパンチ——高水準の先制技

バレットパンチの採用率は**99.7%**。ほぼ全てのハッサム使いがこの技を採用しています。

その理由は特性テクニシャンにあります。テクニシャンは**威力60以下の技の威力を1.5倍**にする特性です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">計算</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">実質威力</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ基本威力</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">×テクニシャン補正（威力60以下）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40 × 1.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">×はがね一致補正</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60 × 1.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">90相当</strong></td>
</tr>
</tbody>
</table>
</div>

**先制技（優先度+1）で実質威力90**というのは、通常の先制技（多くは威力40〜60）と比べても破格で、いわ・こおり・フェアリーには等倍以上で刺さります。

さらに**つるぎのまい後のバレットパンチ**は、いじっぱりA実数値222に2段階上昇が乗るため、先制でありながら多くのポケモンを確定1発圏に捉えることができます。「積んだ後に先制技でフィニッシュ」という流れが、メガハッサムの大きな強みです。

### 理由2: はがね/むし複合——ほのお以外は全て等倍以下

メガハッサムのタイプ相性は、防御面で非常に優れた組み合わせです。はがね単体ではかくとう・じめん・ほのお、むし単体ではほのお・ひこう・いわが弱点ですが、**この2タイプを組み合わせると弱点はほのお（4倍）のみ**になります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">攻撃タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">はがねへの倍率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">むしへの倍率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">複合後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">判定</th>
</tr>
</thead>
<tbody>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ほのお</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">×4（超ばつぐん）</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4倍弱点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">じめん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×1（等倍）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">相殺</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">かくとう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×1（等倍）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">相殺</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×1（等倍）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">相殺</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">いわ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">×1（等倍）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">相殺</td>
</tr>
</tbody>
</table>
</div>

「弱点が多そう」という先入観とは裏腹に、**実質的な弱点はほのお4倍のみ**という高水準の耐性を持ちます。M-2環境においてリザードン（5位）が多いため油断は禁物ですが、それ以外のポケモンに対しては非常に安定した耐性を持つことができます。

### 理由3: HA振り防御140で場持ちよく積める中・後発運用

メガハッサムはすばやさ75と遅めですが、その分**HA振りで防御140という高水準の物理耐久**を確保できます。これは環境の物理受け・高耐久ポケモンと並べてもトップクラスの数値です（下表は環境で防御に定評のあるポケモンと種族値を比較したもの）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">比較</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">メガハッサム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0681-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギルガルド（シールド）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">140</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#555">同値</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0227-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">エアームド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">140</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#555">同値</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#555">メガハッサムより低い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">118</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#555">メガハッサムより低い</td>
</tr>
</tbody>
</table>
</div>

HA振りによってこの防御140が最大化されます。環境の多くの物理技を受けながらつるぎのまいを積み、バレットパンチで確定1発フィニッシュという流れが成立するのは、この耐久力があってこそです。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">150</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>140</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">600</span>
  </div>
</div>

**A150は環境トップクラスの数値**。さらにぼうぎょ140という高水準の防御もあります。一方でHP70・すばやさ75と低く、正面から殴り合うというよりも**後手でバレットパンチを打ち込む、または耐久を活かして積んでからフィニッシュ**というスタイルが基本になります。

とくぼうも80→100に強化され、HP70と合わせて特殊方面も一定の耐久を持ちます。

### タイプ・弱点（メガ後）

<div style="display:flex;align-items:center;gap:6px;margin:10px 0">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:40px;height:40px;vertical-align:middle" />
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:40px;height:40px;vertical-align:middle" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（4倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ほのお
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle">ノーマル</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle">くさ</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle">エスパー</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle">はがね</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle">むし</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle">でんき</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px;vertical-align:middle">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> どく
  </td>
</tr>
</tbody>
</table>
</div>

どくタイプの技を無効化できるのも利点で、環境のどくどくや一部のどく技を受けずに済みます。

---

## 主要型の解説

### 型① いじっぱり HA最大振り メガ型（最多）

メガハッサムの基本形。いじっぱりでHA最大振り、余り2を H・B・S・D のどこかに振るバリエーションで、合計採用率は約34%（HA+b 14.2%・HA+s 12.5%・HA+d 7.6%）。余り2は実数値で1しか動かず確定数に影響するケースは稀のため、本質的な型としては1つにまとめる。技構成と持ち物の差で立ち回りが分かれる。

<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:48px;height:48px" />
  <div>
    <strong>いじっぱり HA最大振り メガ型</strong><br>
    <small style="color:#666">EV振り採用率合計 約34%</small>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>特性</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">テクニシャン（98.6%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（こうげき↑ とくこう↓）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32（余り2はH・B・S・Dから選択）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサムナイト（79.1%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>必須技</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（99.7%）・つるぎのまい（86.6%）・インファイト（72.4%）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>選択技</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（53.6%）／はねやすめ（29.6%）／とんぼがえり（20.6%）</td>
</tr>
</tbody>
</table>
</div>

**選択技による立ち回りの違い:**
- **はたきおとす型（53.6%）**: 相手の持ち物（オボンのみ・たべのこし・こだわりスカーフ等）を持っていない状態にできる副効果が強力。相手が道具を持っている場合は威力1.5倍で殴れる。テクニシャン対象外（威力65）。なお対応するポケモンが持つメガストーンは持っていない状態にできない仕様
- **はねやすめ型（29.6%）**: つるぎのまい→はねやすめで長期戦に持ち込み、半減・無効タイプの多さを活かして粘る構成
- **とんぼがえり型（20.6%）**: メガ進化前から繰り出しと交代を行い、対面操作で有利な選出を作る

**立ち回りのポイント:**
ぼうぎょ実数値192（B振り時）のおかげで、多くの物理技を1発受けながらつるぎのまいを積めます。いじっぱりA実数値222につるぎのまい1積み（A2段階上昇）を乗せたバレットパンチは、先制・実質威力90でありながら多くのポケモンを確定1発圏に捉えられます。

---

### 型② 無メガ・メタルコート型（9.5%）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム（通常）" style="width:48px;height:48px" />
  <div>
    <strong>無メガ メタルコート型</strong><br>
    <small style="color:#666">持ち物採用率 9.5%（メガなし）</small>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>特性</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">テクニシャン（98.6%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（91.0%）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32（主に）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタルコート（はがねタイプの技威力×1.2）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / インファイト / はたきおとす</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- メタルコート（無メガ型でのみ採用される持ち物）でバレットパンチが実質威力108相当（40×1.5×1.5×1.2）に伸び、メガ型の実質90を上回る先制火力を出せる
- メガ枠を他のポケモン（ガブリアスやリザードン等）に回せるため、パーティ全体のメガ枠選択を縛らずに済む

**弱み:**
- メガ型（A150・B140・D100）と比べ、A130・B100・D80止まりで耐久・火力ともに一段劣る
- 持ち物がメタルコートに固定されるため、メガ型で選べるオボンのみなどの回復・補助アイテム枠を切ることになる

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>バレットパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>99.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制技（優先度+1）。テクニシャン+タイプ一致補正で実質威力90相当。ほぼ全員が採用する必須技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>86.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき2段階アップ。積み後のバレットパンチが先制圏で多くのポケモンを確定1発に</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>72.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプへの対抗手段。ガブリアスやトリトドンなど幅広い相手に通る。ぼうぎょ・とくぼうが各1段階下がるデメリットあり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">テクニシャン対象外（威力65）。相手の持ち物を永続消失させる副効果。オボンのみ・たべのこし消去に有効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>29.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP半分回復。耐久型で長期戦を狙う場合に採用。防御140と組み合わせると場持ちが大幅に向上</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>20.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代できる。先発で使ってダメージを与えながら有利な後続に繋ぐサイクル戦術</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ダブルウイング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>12.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">40×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">テクニシャン補正あり（40×1.5=60×2）。かくとう・むし弱点への対抗手段として採用される場合がある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>むしくい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>7.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">テクニシャン補正対象外（ちょうど威力60なので対象外）。むし一致の通常火力枠として少数採用</td>
</tr>
</tbody>
</table>
</div>

### 技の選択方針

**ほぼ確定枠:** バレットパンチ（99.7%）＋つるぎのまい（86.6%）の2枠は実質確定です。

**選択枠（2枠）:** 以下から採用
- **はがね対策・汎用火力:** インファイト（72.4%）— ほぼ必須に近い
- **持ち物消去:** はたきおとす（53.6%）— 環境にオボンのみ・食べ残し持ちが多いなら有効
- **場持ち:** はねやすめ（29.6%）— 長期戦・受け回し型に
- **サイクル戦:** とんぼがえり（20.6%）— 交代を絡めた戦術向け
- **テクニシャン技:** ダブルウイング（12.6%）— ひこう技でかくとう・むし弱点への対抗

---

## パーティ構成

この節では使用率TOP25から、メガハッサム（S75・ほのお4倍）のタイプ相性と相手の主力技（採用率）を突き合わせ、相性がはっきり出る相手だけを有利・不利の両面で抽出しています。倍率はバレットパンチ（はがね技）・インファイト（かくとう技）と、相手の主力技がこちらに通る倍率の両方で判定しています。

#### 苦手なポケモン

ほのお技で4倍弱点を突かれる相手と、こちらの有効打が通らないはがね系を挙げます。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのお4倍を突く最も警戒すべき相手</strong>。S100でこちらより速く、かえんほうしゃ（42.4%）・フレアドライブ（33.3%）で確定1発。後出しは不可能</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ウルガモス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのまい（79.7%）がほのお4倍で確定1発。S100で先に動かれ、ちょうのまい（97.4%）を積まれると突破が困難。後出しは避け、リザードンと同様にほのおを受けられる枠で対応する</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0655-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マフォクシー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ石採用率96.5%でメガ後S134（S実数値204）と大幅に速く、かえんほうしゃ（65.5%）がほのお4倍で確定1発</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（47.8%）採用個体にはほのお4倍で焼かれる。メガ石採用率80.7%でメガ後S100（S実数値167）とメガハッサムより速く、低耐久のこちらは1発で致命傷。ほのお非採用個体に対してもしんそく（45.6%）の先制で削られる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうでバレットパンチ×0.25・むし技×0.5。インファイトもひこうに半減され等倍止まり。はねやすめ（98.1%）で居座られると突破不能。一方こちらへの打点も乏しく、受け出してつるぎのまいを積み始める余地はある</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0681-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ゴーストでバレットパンチ×0.5。シールドフォルムの高ぼうぎょで受けられ、キングシールド（84.2%）でインファイトを読まれA2段階ダウン。かげうち（96.2%）で削られる</td>
</tr>
</tbody>
</table>
</div>

<div style="background:#fef3cd;border:1px solid #f59e0b;border-radius:8px;padding:12px 16px;margin:12px 0">
  <strong>⚠️ ほのお対策枠は必須</strong><br>
  ほのお4倍弱点はリザードン（5位）・ウルガモス（18位）・マフォクシー（25位）の3体に共通し、いずれもメガ後S100〜134でメガハッサム（S実数値127）より速く後出しが効きません。採用する場合は、これらを後出しから処理できる枠を必ず用意します。具体的には同居率上位の<strong>アシレーヌ</strong>（ほのお半減＋みず一致のうたかたのアリアでリザードンに等倍以上）でほのお技を受けつつ打点を作るのが基本です。マフォクシー（エスパー単）にはあくタイプの打点、ウルガモス（むし/ほのお）にはいわ技を持つ枠が有効です。ハッサムを引いてこれらで対応する動きを徹底します。
</div>

#### 有利なポケモン

バレットパンチ（はがね技：いわ・こおり・フェアリーに×2）が刺さり、相手の主力技でこちらの弱点を突かれない相手を挙げる。S75で多くの相手に後手を踏むため、つるぎのまいを1積みしてからバレットパンチで縛る運用が前提。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ/どくにバレットパンチ×2で先制圏。主力のヘドロウェーブ（69.4%）はどく無効、パワージェム（85.3%）もはがね/むしに等倍以下で受けられる</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト/フェアリーにバレットパンチ×2。ばける後もつるぎのまい後のバレットパンチで縛れる。じゃれつく（91.9%）はこちら×0.5で軽い</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0670-05.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フラエッテ（永遠）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー単にバレットパンチ×2。ムーンフォース（87.0%）はこちら×0.5で軽く、めいそうを積む前にバレットパンチで処理しやすい</td>
</tr>
</tbody>
</table>
</div>

### 相性の良いパーティパートナー

以下はハッサムの同居率TOP10のうち、役割が噛み合うパートナーを抜粋した（カッコ内は同居率順位）。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居5位／ほのお受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居9位／高耐久・ステロ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居3位／高速・タイプ補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0428-00.webp" alt="ミミロップ">
    <div class="name">ミミロップ</div>
    <div class="rate">同居1位／ねこだましで足止め</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居4位／特殊受け</div>
  </div>
</div>

**パーティ構成のポイント:**
1. **ほのお対策が最優先:** ほのお4倍を受け流せる枠を必ず添える。同居率上位のアシレーヌ（ほのお半減）や、高耐久でじしんを持つカバルドンが自然に組み込める
2. **速度不足の補完:** S75と遅いため、ガブリアス（S102）など高速アタッカーで先に削り、メガハッサムのバレットパンチで縛る流れを作る。ミミロップ（ねこだまし）で相手の動きを止め、つるぎのまいを積む隙を作るのも有効
3. **はねやすめ採用時:** 長期戦が見込まれる場合、はねやすめ型は耐久をさらに活かせる。対面性能が下がる代わりに場持ちが向上する

---

## データ分析①：採用率に見る「先制技に全振りする構築思想」

ハッサムの実データを並べると、**他のアタッカーには見られない極端な採用率の偏り**が見えてきます。

### 環境上位のバレットパンチ使用ポケモンとの比較

バレットパンチを採用する環境ポケモンの中でも、ハッサムの採用率は突出しています。

| ポケモン（使用率順位） | バレットパンチ採用率 |
|---|---|
| **ハッサム（14位）** | **99.7%** |
| メガルカリオ（9位） | 48.0% |
| カイリキー（圏外） | 81.0% |

メガルカリオは A・C 両刀でメインウェポン候補が多いため、バレットパンチの採用は半分以下に留まります。一方ハッサムは**ほぼ全個体がバレットパンチを採用**しており、選択肢としてではなく「**確定枠**」として扱われていることがデータから読み取れます。

### 持ち物の集中：「バレットパンチ強化アイテム」が約89%

| 持ち物 | 採用率 | 効果 |
|---|---|---|
| ハッサムナイト | 79.1% | メガ進化でA130→150（バレットパンチ強化） |
| メタルコート | 9.5% | はがね技1.2倍（バレットパンチ強化） |
| オボンのみ | 4.0% | 回復 |
| ラムのみ | 2.7% | 状態異常治療 |

**約89%（79.1+9.5）の個体が「バレットパンチを強化する持ち物」を選択**しています。回復・状態異常対策などの汎用アイテムは10%程度に留まり、ハッサムが**耐久・回復よりもバレットパンチの威力上積みを優先する構築思想**で運用されていることが分かります。

### 積み技86.6%との組み合わせ

つるぎのまいは採用率86.6%（技採用率2位）。先制技持ちアタッカーは通常「タスキ + 先制技で削るだけ」の運用が多い中、ハッサムは**つるぎのまい→積んだ後のバレットパンチで詰める**という、攻撃的な使い方を主流としています。先制技で対面処理する役ではなく、「**1回でも積めればパーティ全体を詰ませられる**フィニッシャー」として運用されているのが、技採用率の組み合わせから読み取れます。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">得意場面</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">HA最大振り メガ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32（余り2は任意）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ / つるぎのまい / インファイト / はたきおとす or はねやすめ or とんぼがえり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">約34%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガ枠で採用する基本形</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">無メガ メタルコート型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ / つるぎのまい / インファイト / はたきおとす</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガ枠を別ポケモンに使う場合</td>
</tr>
</tbody>
</table>
</div>

メガハッサムはM-2環境において、**テクニシャン+バレットパンチという高水準の先制技**・**A150+つるぎのまいによる積み後の爆発力**・**ほのお一点弱点という安心感のある耐性**を兼ね備えた万能アタッカーです。

いじっぱり（91.0%）が大半を占め、EV振りもHA軸が最多であることが示すように、最もシンプルで強い使い方は「HA振りで耐久を確保→中・後発でつるぎのまいを積む→バレットパンチで先制フィニッシュ」という形です。

ほのお4倍弱点（リザードン・ウルガモス・マフォクシー）への対策枠を用意できれば、はがね/むし複合の安定した耐性を活かして戦える強力なメガ進化ポケモンです。
