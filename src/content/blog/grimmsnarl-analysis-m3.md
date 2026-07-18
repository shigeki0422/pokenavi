---
title: 'オーロンゲ考察 M-3 型別採用率と立ち回り'
description: 'チャンピオンズM-3使用率19位オーロンゲを徹底解説。いたずらごころ99.4%で変化技を先制発動し、リフレクター79.1%・ひかりのかべ73.6%を先手で展開。ひかりのねんど73.3%で壁8ターン継続。壁貼り役としての立ち回りと型別採用率を実データで解説します。'
updatedDate: '2026-07-18'
pubDate: '2026-06-24'
heroImage: '../../assets/hero-grimmsnarl-m3.png'
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
  <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ" />
  <div>
    <h2 style="margin:0 0 8px">オーロンゲ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">19位</strong>　特性: <strong>いたずらごころ 99.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/20）時点の集計です

シーズンM-3のシングルバトルで、オーロンゲは**使用率19位**を記録。特性いたずらごころで変化技の優先度を+1にし、**リフレクター79.1%・ひかりのかべ73.6%を先手で張る壁貼り役**として環境に定着しています。ひかりのねんど73.3%と合わせて壁を8ターン継続させ、後続のエースが動きやすい盤面を整えるのが主な役割です。

---

## なぜ今オーロンゲが19位なのか

### 1. いたずらごころで壁を先手展開できる

特性いたずらごころは変化技の優先度を+1にする。リフレクター・ひかりのかべをすばやさに関係なく先手で張れるため、**相手がどれだけ素早くても1ターン目から壁を展開できる**点が他の壁貼り役にない強みです。すばやさ60と遅い部類ですが、いたずらごころがある限りこの数値は壁展開の速度に影響しません。ただし、いたずらごころで優先度が上がった変化技は**あくタイプの相手には無効**になるため、すてゼリフ・ちょうはつでの先制妨害はドドゲザン（24位）などのあく相手には通りません。壁展開（リフレクター・ひかりのかべ）自体は自分にかける変化技なので、あく相手でも問題なく機能します。

### 2. ひかりのねんどで壁を8ターン継続させられる

持ち物採用率1位はひかりのねんど73.3%。ひかりのねんどを持つことでリフレクター・ひかりのかべの効果ターンが通常5ターンから**8ターン**に延長されます。後続エースが8ターンの間、物理・特殊の両方を半減で受けられるため、攻撃技の起点を確実に作れます。

### 3. すてゼリフで能力を下げながら後続へつなぐ

すてゼリフ採用率77.1%は、相手のこうげきとくこうを1段階ずつ下げつつ自分が交代する技です。壁を張った後にすてゼリフを打つことで、**相手の打点を下げながら後続のエースを安全に出せる**流れを作れます。相手の能力低下と壁効果が重なり、後続が大幅に動きやすくなります。

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
      <div style="width:60%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

こうげき120は高い水準ですが、壁貼り役として運用するためほとんど活かされません。ぼうぎょ65・とくぼう75と耐久は低めで、壁なしでは物理・特殊ともに受け出しが難しいステータスです。すばやさ60はいたずらごころで補うため、実質的に変化技限定の行動については速度が問われない構成になっています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく（¼）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

あく×フェアリーの複合タイプは、エスパーとドラゴンを無効化します。あく単体の弱点であるかくとうは等倍で受けられ、ゴーストは半減・あくは¼まで軽減されます。弱点はどく・はがね・フェアリーの3タイプで、これらのタイプを持つ相手には壁展開前の被弾に注意が必要です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ソウルクラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">80.4%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>リフレクター</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">79.1%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>すてゼリフ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">77.1%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ひかりのかべ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">73.6%</strong></td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ちょうはつ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">30.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ねこだまし</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">40</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">21.9%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>イカサマ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">95</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">13.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ふいうち</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">70</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">11.7%</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>じゃれつく</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ビルドアップ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">0.6%</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

性格分布はわんぱく60.5%が突出し、いじっぱり15.9%・しんちょう14.5%が続きます。実際のEV配分を見ると上位はいずれもHにB寄りの振り分けで、ぼうぎょを固める運用が主流です。役割は壁貼り＋すてゼリフの補助役で固定されており、ここではB特化のわんぱく型を中心に解説します。

### 型1: わんぱくHB壁貼り型（最多採用）

**性格採用率: わんぱく 60.5%**（B↑ A↓。物理方向の耐久を最大化する構成）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0861-00.webp" alt="オーロンゲ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBわんぱく壁貼り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いたずらごころ（99.4%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32 B32 C2（採用率26.1%。最多配分）<br>
<strong>持ち物:</strong> ひかりのねんど（73.3%）
</div>
<div>
<strong>技構成:</strong><br>
・リフレクター<br>
・ひかりのかべ<br>
・すてゼリフ<br>
・ソウルクラッシュ / ちょうはつ
</div>
</div>
</div>

**強み:**

H32 B32振りでぼうぎょを最大化し、物理アタッカーからの先制をできるだけ耐えながら壁を張る構成です。いたずらごころで1ターン目にリフレクターかひかりのかべを先手展開し、2ターン目に残りの壁を張り、3ターン目にすてゼリフで後続へつなぐ3ターンの流れが基本です。ひかりのねんどで壁が8ターン継続するため、後続が複数回の壁恩恵を受けられます。ソウルクラッシュを採用した個体は、相手の変化技枠への打点と相手とくこうダウンを兼ねて攻撃にも参加できます。

**弱み:**

ぼうぎょを伸ばしてもとくぼう75は据え置きのため、特殊アタッカーからの攻撃はひかりのかべを展開する前に大ダメージを受けるリスクがあります。

---

## 環境ポケモンへの相性分析

あく/フェアリーはエスパー・ドラゴンを無効化しますが、壁貼り役として運用するため能動的に有利を取る場面は限定的です。オーロンゲ自身が直接戦うより、壁展開後に後続が有利を作る構図のため、ここでは「壁展開を妨害するポケモン」と「壁展開を活かしやすい相手」の視点で整理します。

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
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 展開しやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン技を無効化するため、カイリューのドラゴン主力技を受けながら壁を張れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 苦手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技が×2弱点。メガ後の高いこうげきからのはがね技がぼうぎょ65に刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 苦手</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね技が×2弱点。ぼうぎょ65に対して高火力はがね技が刺さる</td>
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
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下でつるぎのまいを積むじめん・ドラゴン物理エース</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0691-00.webp" alt="ドラミドロ">
    <div class="name">ドラミドロ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">メガ後さいせいりょくでサイクル性能が高く、壁展開と組み合わせやすい</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁と並行して設置・受けを担うはがね・ひこうの物理受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク">
    <div class="name">ムクホーク</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下で高火力ブレイブバードを叩き込む物理エース</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">壁下でめいそうを積むはがね・ドラゴンの特殊エース</div>
  </div>
</div>

**パーティ構成の基本方針:**

オーロンゲは自身がエースとして詰める役割ではなく、壁展開＋すてゼリフで後続のエースを通す補助役です。残り5体の構成では以下を意識します。

1. **物理エース**: リフレクターで物理ダメージが半減するため、ツルギのまい等で積んだ物理アタッカーが壁下でさらに受けにくくなる
2. **特殊エース**: ひかりのかべで特殊ダメージが半減するため、めいそう等を積んだ特殊アタッカーが壁下で安全に行動できる
3. **どく・はがね・フェアリー対策**: オーロンゲが苦手などく・はがね・フェアリータイプに対してサイクルを回せるポケモンを同伴する
4. **8ターンの活用**: ひかりのねんど8ターンの壁を最大限活用できるよう、エースが積んで全抜きを狙う構成が壁展開と噛み合う

---

## データ分析①：リフレクター・ひかりのかべ・すてゼリフの採用率から読む役割の固定度

オーロンゲの技採用率上位4技を並べると、役割の均質性が際立ちます。

| 技 | 採用率 | 役割 |
|---|---|---|
| ソウルクラッシュ | 80.4% | 攻撃＋とくこうダウン |
| リフレクター | 79.1% | 物理壁展開 |
| すてゼリフ | 77.1% | 能力ダウン＋後続へ交代 |
| ひかりのかべ | 73.6% | 特殊壁展開 |

ソウルクラッシュ・リフレクター・すてゼリフ・ひかりのかべの上位4技はいずれも70%以上の採用率で、**技4枠が実質これらで固定**されています。残り1枠の入れ替え候補がちょうはつ（30.5%）で、対面した相手はまずこの4技の流れを警戒する必要があります。

ソウルクラッシュの採用率80.4%は壁貼り役の技構成としては高い数値で、**攻撃技をほぼ全個体が採用している**点が特徴的です。壁を張り切った後にソウルクラッシュ→すてゼリフで相手のAとCを両方下げて後続に繋げば、壁効果と能力低下が重なって後続への圧力を最大化できます。

持ち物はひかりのねんど73.3%が支配的で、たべのこし15.9%・たつじんのおび5.1%が続きます。ひかりのねんどが約7割の個体に採用されていることから、**壁の8ターン継続を前提とした後続エースの設計**が環境で主流と判断できます。

---

## まとめ

オーロンゲはいたずらごころによるすばやさ非依存の壁展開と、ひかりのねんどによる8ターン継続が強みの補助役です。ソウルクラッシュ80.4%・リフレクター79.1%・すてゼリフ77.1%・ひかりのかべ73.6%の4技が実質固定で、対面した相手はまずこの流れを警戒する必要があります。型はわんぱく（B特化）が60.5%と主流です。

弱点はどく・はがね・フェアリーの3タイプで、これらの攻撃で壁展開前に突破されると役割を果たせません。ちょうはつ30.5%の採用は相手の壁貼り・積み技・回復技を封じる逆妨害として機能し、壁合戦になる対面ではちょうはつを先手で打つことで相手の補助行動を止められます。ただしいたずらごころ由来の先制変化技はあくタイプには無効なので、ドドゲザン（24位）などあく相手にはちょうはつ・すてゼリフが通らない点に注意が必要です。

---

## 関連記事

- [使用率上位 ムクホークのM-3考察](/blog/staraptor-analysis-m3/)
- [後続エース候補 メガメタグロスのM-3考察](/blog/metagross-analysis-m3/)
