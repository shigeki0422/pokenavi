---
title: '【ポケモンチャンピオンズ】キラフロル考察 M-3 使用率19位・タスキ72%の展開役'
description: 'M-3シングルバトルで使用率19位のキラフロルを徹底分析。M-2からメガナイト54.2%→タスキ72.0%へ逆転した構成変化とその背景、ステルスロック56.2%による展開型の立ち回り、じめん×4弱点の運用上の注意点を数値で解説。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-kirafurou-m3.png'
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
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">キラフロル</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">19位</strong>（M-2は15位）　特性: <strong>どくげしょう 94.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン時点の集計です

M-3シングルバトルでキラフロルは**使用率19位**。M-2の15位から4つ順位を落としました。最大の変化は持ち物構成で、M-2では**キラフロルナイト54.2%**がトップだったのに対し、M-3では**きあいのタスキ72.0%**へと逆転しています。パワージェム85.8%・ステルスロック56.2%を軸にした展開型が主流です。

---

## なぜM-3でもキラフロルが採用されるのか

### 1. 特性どくげしょうによる物理受け時のどくびし設置

特性**どくげしょう**（採用率94.5%）は、物理技のダメージを受けるたびに相手の場をどくびし状態にします。接触/非接触を問わず物理技なら1回受けるごとにどくびし1枚、2回受けるとどくびし2枚（相手が交代するたびに「もうどく」状態）が積まれます。攻撃を受けながら受動的にどくびしを敷ける点が、後続エースへの展開を有利にする実質的な設置役として機能します。

### 2. ステルスロック56.2%との組み合わせ

きあいのタスキ型でステルスロックを設置し、どくげしょうでどくびしを積んでからタスキで耐えつつ仕事を完結させる流れが主な運用です。タスキ消費後は後続に引き、設置した入場ダメージ（ステロ+どくびし）で相手をじわじわ削る展開を作ります。設置技2種をまとめて担えるポケモンとしての採用価値があります。

### 3. パワージェム85.8%・ヘドロウェーブ52.0%のタイプ一致打点

いわ/どくのタイプ一致技はカバレッジが広く、環境上位のムクホーク（パワージェムいわ×2）・ギャラドス（パワージェムいわ×2）・アローラキュウコン（パワージェムいわ×2、ヘドロウェーブどく×2）・リザードン（パワージェムいわ×4）への打点を1枠ずつで確保できます。

---

## 基本スペック

### 種族値

<div style="max-width:420px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:41.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">83</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#a78bfa,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">86</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0">
    <span style="width:72px;min-width:72px;color:#2563eb;font-weight:700;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

とくこう130が突出した特殊アタッカー型の種族値配分。すばやさ86はM-3環境において中速域で、おくびょうS32実数値151。

### タイプ相性（いわ/どく）

<table style="font-size:0.88em;border-collapse:collapse;width:100%;margin:12px 0">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 8px;text-align:left;border-bottom:2px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:6px 8px;text-align:left;border-bottom:2px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:6px 8px;text-align:left;border-bottom:2px solid #cbd5e1">耐性（½）</th>
  <th style="padding:6px 8px;text-align:left;border-bottom:2px solid #cbd5e1">耐性（¼）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 8px;vertical-align:top">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:40px;height:40px" />
  </td>
  <td style="padding:6px 8px;vertical-align:top">
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:40px;height:40px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:40px;height:40px" />
      <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:40px;height:40px" />
    </div>
  </td>
  <td style="padding:6px 8px;vertical-align:top">
    <div style="display:flex;flex-wrap:wrap;gap:4px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:40px;height:40px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:40px;height:40px" />
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:40px;height:40px" />
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:40px;height:40px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:40px;height:40px" />
    </div>
  </td>
  <td style="padding:6px 8px;vertical-align:top">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:40px;height:40px" />
  </td>
</tr>
</tbody>
</table>

---

## M-3採用型の解説

### 展開型（タスキ）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:48px;height:48px" />
  <strong style="font-size:1.1em">展開型</strong>
</div>

<div style="display:flex;gap:16px;flex-wrap:wrap;margin:12px 0 20px">
  <div style="flex:1;min-width:180px">
    <strong>特性:</strong> どくげしょう（94.5%）<br>
    <strong>性格:</strong> おくびょう（56.3%）<br>
    <strong>EV:</strong> A1-C32-S32（30.0%）<br>
    <strong>持ち物:</strong> きあいのタスキ（72.0%）
  </div>
  <div style="flex:1;min-width:180px">
    <strong>技構成:</strong><br>
    パワージェム（85.8%）<br>
    ステルスロック（56.2%）<br>
    ヘドロウェーブ（52.0%）<br>
    だいちのちから（58.2%）または<br>
    エナジーボール（46.8%）
  </div>
</div>

最多採用構成。おくびょうC32-S32のS実数値は151。ステルスロックを設置し、どくげしょうで物理技を誘ってどくびしを積む流れが基本です。タスキにより先発で確実に1〜2仕事こなせます。4枠目はだいちのちから（じめん技で対はがね）かエナジーボール（くさ技で対みず・じめん）の二択が多く、相手の構成に応じた選択が必要です。

**S実数値と速度圏について**：おくびょうS32で実数値151。環境上位のガブリアス最速S32実数値169、マスカーニャ最速S32実数値192より遅く、メタグロスはM-3でメタグロスナイト採用率97.4%のためメガ後S110・最速S32で実数値178にもS151では先手を取れません。展開役として先制が必要な場面では相手の行動を読んで動く意識が必要です。

### 特殊アタッカー型（ひかえめ）

<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:48px;height:48px" />
  <strong style="font-size:1.1em">特殊アタッカー型</strong>
</div>

<div style="display:flex;gap:16px;flex-wrap:wrap;margin:12px 0 20px">
  <div style="flex:1;min-width:180px">
    <strong>特性:</strong> どくげしょう（94.5%）<br>
    <strong>性格:</strong> ひかえめ（39.0%）<br>
    <strong>EV:</strong> C32-S32（20.4%）<br>
    <strong>持ち物:</strong> きあいのタスキ（72.0%）またはキラフロルナイト（20.8%）
  </div>
  <div style="flex:1;min-width:180px">
    <strong>技構成:</strong><br>
    パワージェム（85.8%）<br>
    だいちのちから（58.2%）<br>
    ヘドロウェーブ（52.0%）<br>
    エナジーボール（46.8%）
  </div>
</div>

ひかえめC32-S32はC実数値200、S実数値138。おくびょう型に対してS27低下の代わりにC49増加が得られます。こちらの型でキラフロルナイト（20.8%）を採用するとメガキラフロルに進化し、C実数値222・S実数値153に上昇します。ただしメガ進化ターンは「メガ進化してから行動」のため実質的に後攻になる点に注意が必要です。

---

## データ分析①：M-2→M-3の持ち物・技構成の変化

M-2とM-3でキラフロルの採用構成が大きく変化しました。

<table style="font-size:0.88em;border-collapse:collapse;width:100%;margin:12px 0">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 8px;border-bottom:2px solid #cbd5e1">項目</th>
  <th style="padding:6px 8px;border-bottom:2px solid #cbd5e1;text-align:right">M-2</th>
  <th style="padding:6px 8px;border-bottom:2px solid #cbd5e1;text-align:right">M-3</th>
  <th style="padding:6px 8px;border-bottom:2px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">使用率順位</td>
  <td style="padding:6px 8px;text-align:right">15位</td>
  <td style="padding:6px 8px;text-align:right">19位</td>
  <td style="padding:6px 8px;color:#dc2626">▼4</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">キラフロルナイト</td>
  <td style="padding:6px 8px;text-align:right">54.2%</td>
  <td style="padding:6px 8px;text-align:right">20.8%</td>
  <td style="padding:6px 8px;color:#dc2626">▼33.4pt</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">きあいのタスキ</td>
  <td style="padding:6px 8px;text-align:right">36.0%</td>
  <td style="padding:6px 8px;text-align:right">72.0%</td>
  <td style="padding:6px 8px;color:#059669">▲36.0pt</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">ステルスロック</td>
  <td style="padding:6px 8px;text-align:right">36.5%</td>
  <td style="padding:6px 8px;text-align:right">56.2%</td>
  <td style="padding:6px 8px;color:#059669">▲19.7pt</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">エナジーボール</td>
  <td style="padding:6px 8px;text-align:right">11.0%</td>
  <td style="padding:6px 8px;text-align:right">46.8%</td>
  <td style="padding:6px 8px;color:#059669">▲35.8pt</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">ロックカット</td>
  <td style="padding:6px 8px;text-align:right">16.1%</td>
  <td style="padding:6px 8px;text-align:right">0%</td>
  <td style="padding:6px 8px;color:#dc2626">消滅</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:6px 8px">ニードルガード</td>
  <td style="padding:6px 8px;text-align:right">27.9%</td>
  <td style="padding:6px 8px;text-align:right">11.6%</td>
  <td style="padding:6px 8px;color:#dc2626">▼16.3pt</td>
</tr>
<tr>
  <td style="padding:6px 8px">ヘドロウェーブ</td>
  <td style="padding:6px 8px;text-align:right">69.4%</td>
  <td style="padding:6px 8px;text-align:right">52.0%</td>
  <td style="padding:6px 8px;color:#dc2626">▼17.4pt</td>
</tr>
</tbody>
</table>

**M-2では「メガ進化してアタッカーとして動く」型が過半数**でしたが、M-3では展開設置役にシフトしています。ステルスロック+56.2%・エナジーボール+35.8ptの増加が連動しており、「設置してエナジーボールでみず・じめんを牽制しつつタスキで耐える」役割が明確になっています。一方でM-2に16.1%あったロックカット（S上昇）は消滅し、メガ後の高速化を目指す型が完全に淘汰されました。どくげしょう採用率もM-2の88.5%からM-3の94.5%に上昇しており、受動的などくびし設置への依存度が増しています。

---

## データ分析②：環境上位へのカバレッジ

パワージェム（いわ）・ヘドロウェーブ（どく）・だいちのちから（じめん）・エナジーボール（くさ）の4技タイプと、M-3環境上位の倍率一覧です。

<table style="font-size:0.85em;border-collapse:collapse;width:100%;margin:12px 0">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1">相手</th>
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1;text-align:center">いわ</th>
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1;text-align:center">どく</th>
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1;text-align:center">じめん</th>
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1;text-align:center">くさ</th>
  <th style="padding:5px 8px;border-bottom:2px solid #cbd5e1">最大倍率技</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">リザードン（ほのお/ひこう）</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×4</strong></td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×0</td>
  <td style="padding:5px 8px;text-align:center">×0.25</td>
  <td style="padding:5px 8px">パワージェム</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">ムクホーク（ノーマル/ひこう）</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×0</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px">パワージェム</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">ギャラドス（みず/ひこう）</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×0</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px">パワージェム</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">アローラキュウコン（こおり/フェアリー）</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px">いわ or どく</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">マスカーニャ（くさ/あく）</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px">ヘドロウェーブ</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">バシャーモ（ほのお/かくとう）</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px">だいちのちから</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">ライチュウ（でんき）</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px">だいちのちから</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">カバルドン（じめん）</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px;text-align:center">×1</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px">エナジーボール</td>
</tr>
<tr style="border-bottom:1px solid #e2e8f0">
  <td style="padding:5px 8px">メタグロス/メガメタグロス（はがね/エスパー）</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px;text-align:center">×0</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px">だいちのちから</td>
</tr>
<tr>
  <td style="padding:5px 8px">ブリジュラス（はがね/ドラゴン）</td>
  <td style="padding:5px 8px;text-align:center">×0.5</td>
  <td style="padding:5px 8px;text-align:center">×0</td>
  <td style="padding:5px 8px;text-align:center;color:#dc2626"><strong>×2</strong></td>
  <td style="padding:5px 8px;text-align:center">×0.25</td>
  <td style="padding:5px 8px">だいちのちから</td>
</tr>
</tbody>
</table>

4技で環境上位の多くに等倍以上の打点を確保できます。ただしガブリアス（ドラゴン/じめん）はいわ×0.5・どく×0.5・じめん×1・くさ×1で最大倍率が等倍止まりであり、有効打がありません。

---

## 苦手なポケモン

**ガブリアス**（M-3使用率1位）: ガブリアスのじしん採用率99.5%。キラフロルはじめん×4弱点のためほぼ確実に弱点を突かれます。有効打もいわ×0.5・どく×0.5どまりで、直接対面では勝ち目がありません。展開役として先発で動く場合もガブリアスを選出された段階で後続に引かざるを得ない場面が多くなります。

**カバルドン**（M-3使用率8位）: じしん採用率97.8%で即座にじめん×4弱点を突かれます。エナジーボールで×2が通りますが、カバルドン側が先にじしんで動くため安全に動けません。どくびし・ステルスロック設置の前にやられるリスクが高い対面です。

**メタグロス**（M-3使用率4位）: M-3でメタグロスナイト採用率97.4%のためメガ後で対面します。メガメタグロスはS実数値178（最速S32）でS151のキラフロルより速く、先に動かれます。どく無効・じめんは×2有効ですが、先制を取れないためだいちのちからで動けるか不確実です。

---

## 同居ポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
    <div class="name">ガブリアス</div>
    <div class="rate">同居1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" />
    <div class="name">ミミッキュ</div>
    <div class="rate">同居2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" />
    <div class="name">マスカーニャ</div>
    <div class="rate">同居3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" />
    <div class="name">カバルドン</div>
    <div class="rate">同居4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" />
    <div class="name">メタグロス</div>
    <div class="rate">同居5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" />
    <div class="name">ブリジュラス</div>
    <div class="rate">同居6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0398-00.webp" alt="ムクホーク" />
    <div class="name">ムクホーク</div>
    <div class="rate">同居7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0392-00.webp" alt="バシャーモ" />
    <div class="name">バシャーモ</div>
    <div class="rate">同居8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" />
    <div class="name">ギャラドス</div>
    <div class="rate">同居9位</div>
  </div>
</div>

**ガブリアス・カバルドン**との同居が多いのは、いずれもステルスロックを設置できる展開役としてパーティに入ることが多く、キラフロルと役割が近いためです。「設置役を2枚積んで確実に刺す」構築か、選出に柔軟性を持たせる構成として選ばれています。

**ムクホーク・ギャラドス**はキラフロルのパワージェムが×2で効く相手ですが、これらのポケモン自体はキラフロルと攻撃が被らず、異なる打点を担当するため構成の穴を埋め合う形でパーティに並びます。

**マスカーニャ・バシャーモ**といったフィニッシャー候補との同居は、キラフロルが展開設置を担い後続のアタッカーが通りやすい状況を作る役割分担です。

---

## まとめ

M-3でキラフロルはメガ運用から展開設置役へとシフトし、**タスキ+ステルスロック+どくげしょう**のセットが現在の主流です。C種族値130のパワージェムで環境のひこう・ほのお複合（リザードン×4、ムクホーク×2、ギャラドス×2）に刺さる打点を持ちながら、どくびし・ステルスロックで後続を後押しする展開型として機能します。

一方でじめん×4弱点という根本的な問題があり、M-3使用率1位ガブリアス・8位カバルドンのじしんが99.5%・97.8%で採用されているため、これらとの対面を避ける選出管理が実質必須です。採用を検討する場合はガブリアス・カバルドンへの対処を他のポケモンで担保した上で選出する必要があります。

---

## 関連記事

- [ガブリアス考察 M-3](/blog/garchomp-analysis-m3)
- [カバルドン考察 M-3](/blog/hippowdon-analysis-m3)
- [マスカーニャ考察 M-3](/blog/meowscarada-analysis-m3)
