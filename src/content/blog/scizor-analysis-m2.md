---
title: '【ポケモンチャンピオンズ】メガハッサム 考察 M-2シーズン 使用率と型別解説'
description: 'M-2シングルバトルで使用率14位のメガハッサムを徹底分析。テクニシャン+バレットパンチの高水準な先制技、つるぎのまい積みの破壊力、ほのお一点弱点の耐性と対策、いじっぱりHA振りの運用まで実データで解説します。'
pubDate: '2026-05-22'
draft: true
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

**先制技（優先度+1）で実質威力90**というのは、通常の先制技と比べても破格です。マッハパンチ（優先度+1、威力40→テクニシャン適用外のかくとうタイプ）と比較しても、はがねというタイプのほうが通りが良い場面が多いです。

さらに**A150+つるぎのまい後のバレットパンチ**は、積んだ後なら先制でありながら多くのポケモンを確定1発圏に捉えることができます。「積んだ後に先制技でフィニッシュ」という流れが、メガハッサムの大きな強みです。

### 理由2: はがね/むし複合——ほのお以外は全て等倍以下

メガハッサムのタイプ相性は、防御面で非常に優れた組み合わせです。一般的にはがねタイプはかくとう・じめんに弱く、むしタイプはほのお・ひこう・いわに弱いと思われがちですが、**この2タイプを組み合わせると相殺効果で実質弱点はほのお（4倍）のみ**になります。

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

とくぼう100もメガ進化で強化（80→100）されており、特殊方面の被ダメージも想定より少ない場面があります。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">等倍（実質相殺）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> ほのお
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.8em;text-align:left">
    かくとう・じめん・ひこう・いわ（各々相殺）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.8em;text-align:left">
    ノーマル・くさ・こおり・ドラゴン・フェアリー（½）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px"> どく
  </td>
</tr>
</tbody>
</table>
</div>

どくタイプを完全無効化することも特筆すべき点です。フラエッテ（永遠）のムーンフォースや一部のどく技を無効化できる点は場面によって活きることがあります。

---

## 主要型の解説

### 型① いじっぱり HA+b 積みバレット型（最多・14.2%）

EV振りの中で最も採用率が高い基本形です。HAをベースに余りをぼうぎょへ振り、物理耐久をわずかに上積みしています。

<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:48px;height:48px" />
  <div>
    <strong>いじっぱり HA+b 積みバレット型</strong><br>
    <small style="color:#666">EV振り採用率 14.2%</small>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32 B2（HA+b）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサムナイト</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例①</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / インファイト / はたきおとす</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例②</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / はねやすめ / インファイト</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- A150×いじっぱり補正（×1.1）= A実数値165（こうげきEV32振り時）の攻撃力
- テクニシャン+バレットパンチの先制技が最大効率で機能
- HA振りベースで耐久を確保しつつ、余りのぼうぎょで物理耐久を上積み
- つるぎのまい後（A実数値165×2=330相当）のバレットパンチが広い範囲で確定1発
- インファイトでアーマーガア以外の多くのはがね系（ブリジュラス・ドドゲザン等）に等倍以上を入れられる

**弱み:**
- ほのお技1発で即戦闘不能（ほのお技持ちに絶対に出し負けしない読みが必要）
- すばやさ75と遅いため、正面対決では後手になる場面が多い
- はたきおとすはテクニシャン対象外（威力65）のため、補正なし

**立ち回りのポイント:**
HA振りの真価は「つるぎのまいを積める場面を作れること」にあります。ぼうぎょ140という数値のおかげで、多くの物理技を1発受けながらつるぎのまいを積めます。積んだ後はバレットパンチ（先制・実質威力90+A330補正）で多くのポケモンを確定1発圏に捉えられます。

**はたきおとす（53.6%採用）の役割:**
テクニシャン対象外（威力65）ですが、**命中100で相手の持ち物を永続的に消失させる**副効果が強力です。相手のオボンのみ・食べ残し・こだわり系アイテムを消し飛ばしながら等倍以上のダメージが与えられます。なおメガストーンや進化アイテムははたきおとすでは奪えない仕様のため、メガ進化要員には持ち物消失を狙えませんが、消耗品・補正アイテムを落とす効果は多くの場面で有効です。

---

### 型② いじっぱり HA+s 速度調整型（12.5%）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:48px;height:48px" />
  <div>
    <strong>いじっぱり HA+s 速度調整型</strong><br>
    <small style="color:#666">EV振り採用率 12.5%</small>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32 S2（HA+s）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサムナイト</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / インファイト / とんぼがえり</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- Sに振ることで素早さの近い遅めのポケモン（カバルドン・ブリジュラスなど）に先手をとれる可能性が増す
- バレットパンチ（先制技）に頼らない正面対決の選択肢が増える
- はねやすめ不採用で技範囲を広げやすい

**弱み:**
- Sに振った分HPまたは防御が下がり、「積めるほどの耐久」が損なわれる可能性がある
- バレットパンチで補える場面であれば、Sへの投資の必要性が薄れることもある

---

### 型③ いじっぱり HA+d 特殊耐久調整型（7.6%）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0212-00.webp" alt="メガハッサム" style="width:48px;height:48px" />
  <div>
    <strong>いじっぱり HA+d 特殊耐久調整型</strong><br>
    <small style="color:#666">EV振り採用率 7.6%</small>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32 D2（HA+d）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサムナイト</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / インファイト / はねやすめ</td>
</tr>
</tbody>
</table>
</div>

**強み:**
- Dに振ることで特殊方面（りゅうせいぐん・なみのり等）への耐性を補強できる
- 物理防御140に特殊防御も上乗せした「全体的に固い」ポケモンになれる
- はねやすめ（29.6%採用）との組み合わせで長期的な場持ちを目指せる

**採用意図:**
メガハッサムはとくぼうが100（メガ前80）に上昇しているため、特殊耐久型の価値が生まれています。ゲンガー（10位）やアシレーヌ（4位）などの特殊アタッカーに対して、1発耐えながらバレットパンチで倒す立ち回りが狙えます。

---

### 型④ 無メガ・メタルコート型（9.5%）

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（91.0%）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 A32（主に）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタルコート（はがねタイプの技威力×1.2）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ / つるぎのまい / インファイト / はたきおとす</td>
</tr>
</tbody>
</table>
</div>

**メタルコート型の採用意義:**
メガ枠を別のポケモン（ガブリアスやリザードン等）に使いたい場合、ハッサムは無メガで採用されます。その際、メタルコートを持たせることで**バレットパンチの威力をさらに1.2倍に強化**できます。

テクニシャン+タイプ一致補正+メタルコートのバレットパンチは実質威力108相当（40×1.5×1.5×1.2）になります。種族値はメガ前（A130）になりますが、それでも十分な先制火力を確保できます。

**弱み:**
- メガ進化しないためA130（メガ後A150より20低い）
- 持ち物がメタルコートに固定されるためオボンのみなどの回復手段が使えない

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

この節は使用率TOP25から、メガハッサム（S75・ほのお4倍）のタイプ相性と相手の主力技（採用率）を突き合わせ、相性がはっきり出る相手だけを有利・不利の両面で抽出する。倍率はバレットパンチ（はがね技）・インファイト（かくとう技）と、相手の主力技がこちらに通る倍率の両方で判定した。

#### 苦手なポケモン

ほのお技で4倍弱点を突かれる相手と、こちらの有効打が通らないはがね系を挙げる。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S104でこちらより速く、かえんほうしゃ（65.5%）がほのお4倍で確定1発</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうでバレットパンチ×0.25・むし技×0.5。インファイトもひこうに半減され等倍止まり。はねやすめ（98.1%）で居座られると突破不能。一方こちらへの打点も乏しく、起点にしてつるぎのまいを積める場合もある</td>
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
  ほのお4倍弱点はリザードン（5位）・ウルガモス（18位）・マフォクシー（25位）の3体に共通し、いずれもS100以上でメガハッサムより速く後出しが効かない。採用する場合は、これらを後出しから処理できる枠を必ず用意する。具体的には<strong>アシレーヌ</strong>（ほのお半減＋うたかたのアリアで等倍以上）、<strong>ギャラドス</strong>（ほのお半減＋たきのぼり）でほのお技を受け流すか、高耐久＋じしんを持つ<strong>カバルドン</strong>でリザードン・マフォクシーに打点を作る。ハッサムを引いてこれらで対応する動きを基本にする。
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
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン/ひこう。マルチスケイル下でもつるぎのまい後のバレットパンチ＋追撃で押し切れ、相手のドラゴン技・じしんはこちら等倍以下。ほのお技を持たれていなければ有利</td>
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
    <div class="rate">同居1位／ねこだまし起点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居4位／特殊受け</div>
  </div>
</div>

**パーティ構成のポイント:**
1. **ほのお対策が最優先:** ほのお4倍を受け流せる枠を必ず添える。同居率上位のアシレーヌ（ほのお半減）や、高耐久でじしんを持つカバルドンが自然に組み込める
2. **速度不足の補完:** S75と遅いため、ガブリアス（S102）など高速アタッカーで先に削り、メガハッサムのバレットパンチで縛る流れを作る。ミミロップ（ねこだまし）で動きを止めて積みの起点を作るのも有効
3. **はねやすめ採用時:** 長期戦が見込まれる場合、はねやすめ型は耐久をさらに活かせる。対面性能が下がる代わりに場持ちが向上する

---

## データ分析①：テクニシャン+バレットパンチ99.7%の数値的根拠

バレットパンチの採用率99.7%はハッサムの技の中でも突出した高水準ですが、この数値の背景にはテクニシャン補正の計算があります。

| 条件 | バレットパンチ威力 | 倍率 | 備考 |
|---|---|---|---|
| 素の威力 | 40 | — | 先制技（+1優先度） |
| テクニシャン補正 | 60 | ×1.5 | 威力60以下に発動 |
| タイプ一致補正 | **90** | ×1.5 | はがねタイプ一致 |

テクニシャン（威力60以下の技を1.5倍）+タイプ一致の組み合わせで、先制技としての実質威力が90に達します。

この90という数値は、先制技でない通常の「アイアンヘッド（威力80）」を上回り、しかも優先度+1で先手を取れます。S75と遅いメガハッサムにとって、「後手でも確実に動ける先制技が実質威力90」という組み合わせが99.7%という採用率を生んでいます。

メガ進化後のA150と組み合わせると、耐久に振っていないポケモンへの確定圏内が広がり、「場に出るだけで相手の行動を制限する」抑止力として機能します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">積みバレット型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA+b</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ / つるぎのまい / インファイト / はたきおとす</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">14.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">中・後発で積んでフィニッシュ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">速度調整型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA+s</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ / つるぎのまい / インファイト / とんぼがえり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">遅いポケモンへの先手確保</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">特殊耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA+d</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">バレットパンチ / つるぎのまい / はねやすめ / インファイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特殊アタッカーに1発耐えてバレット</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">無メガ メタルコート型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HA</td>
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
