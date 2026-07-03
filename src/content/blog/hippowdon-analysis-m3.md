---
title: '【ポケモンチャンピオンズ】カバルドン考察 M-3 使用率8位の採用理由と型別立ち回り'
description: 'M-3シングルバトルで使用率8位のカバルドンを徹底分析。オボン59.3%・たべのこし36.5%の2強持ち物構成・わんぱくH32-B2-D32型の実数値・あくび+ステロ+なまける耐久型の採用理由をDBデータで解説します。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-hippowdon-m3.png'
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
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" />
  <div>
    <h2 style="margin:0 0 8px">カバルドン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">8位</strong>　特性: <strong>すなおこし 99.5%</strong>
    </div>
  </div>
</div>

> 本記事はM-3シーズンのデータです。

シーズンM-3のシングルバトルで、カバルドンは**使用率8位**（M-2の7位からほぼ横ばい）。すなおこしによる砂嵐展開・あくびでの交代誘発・ステルスロックの設置を組み合わせた耐久型として、環境に安定した地位を確立しています。持ち物はオボンのみ59.3%・たべのこし36.5%の2択が95%以上を占め、同じじめんタイプの使用率1位ガブリアスがきあいのタスキ（35.5%）を筆頭に即戦力型が多いのとは対照的に、カバルドンは**長期戦を前提とした構成**が主流です。

---

## M-3の採用率変化まとめ

### 技採用率（M-2比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">98.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>97.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">-0.2pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>93.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.3pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>84.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+0.3pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">53.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>60.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a"><strong>+7.7pp</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">44.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>34.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-9.7pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">がんせきふうじ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">圏外</td>
</tr>
</tbody>
</table>
</div>

最大の変化は**なまける+7.7pp（53.2%→60.9%）**と**ふきとばし-9.7pp（44.5%→34.8%）**です。なまけるとふきとばしは同じ枠を争うため、長期居座りを重視するなまける型が増え、積み技封じ役としてのふきとばし型が減少した形です。

### 持ち物採用率（M-2比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">64.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たべのこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>36.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">さらさらいわ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
</tbody>
</table>
</div>

オボン→たべのこしのシフトはなまける採用率増加と対応しています。なまけるで継続的に回復できる構成では、HP半減時に1回だけ回復するオボンより毎ターン回復するたべのこしとの相性が良く、長期消耗戦を狙う型が増えた結果と読み取れます。

---

## EV・性格

### 性格

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わんぱく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">69.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう↑ こうげき↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ すばやさ↓</td>
</tr>
</tbody>
</table>
</div>

**わんぱく（69.5%）**が主流で、B↑によりメタグロス（4位）やガブリアス（1位）の物理技を受けやすくします。**しんちょう（16.8%）**はD方向を強化してサザンドラ（13位）・アシレーヌ（14位）等の特殊技を意識した構成です。

### EV配分

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-B2-D32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">23.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくぼう全振り+B最小調整</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B18-D16</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・物理/特殊均等型</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B22-D12</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・B重視型</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B12-D22</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・D重視型</td>
</tr>
</tbody>
</table>
</div>

HP全振りはいずれの構成でも共通しており、H199の確保が第一優先です。BとDの振り分けはパーティが何を任せるかで変わります。最多構成のH32-B2-D32（わんぱく）はとくぼう方向を全振りしつつ、わんぱくのB補正でぼうぎょも底上げします。

### 代表型の実数値（H32-B2-D32・わんぱく）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">実数値</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>199</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき（わんぱく 中立）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">132</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ（わんぱく↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>152</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう（わんぱく↓）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">79</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>108</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
</tr>
</tbody>
</table>
</div>

H199の高いHPと物理耐久B152を合わせて、物理・特殊どちらも受けられる耐久性を持ちます。

---

## 特性

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すなおこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.5%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すなのちから</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.5%</td>
</tr>
</tbody>
</table>
</div>

**すなおこし**は場に出ると砂嵐を発生させる特性。砂嵐中はじめん/いわ/はがねタイプ以外のポケモンが毎ターン最大HPの1/16ずつダメージを受けます。カバルドン自身はじめんタイプのため砂嵐ダメージを受けず、なまけるやたべのこしの回復と相性よく長期戦に持ち込めます。採用率99.5%で実質固定。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">108</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">112</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:59%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">118</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">68</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23.5%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">47</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

HP108・ぼうぎょ118の高耐久が主な採用理由。すばやさ47（実数値67）は環境最低水準のため、先手で動くことは想定せず被弾前提のHP・防御重視型として運用されます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">免疫</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

**みず・くさ・こおり**が×2弱点。マスカーニャ（3位）のトリックフラワーとラグラージ（18位）のウェーブタックルはいずれも×2で、対面では大きなダメージを受けます。でんき無効により、ライチュウ（6位）のでんき技を透かせる点は耐久型として有用です。

---

## 主な型

### 型1：オボンのみ型（59.3%）

HP半減時に回復するオボンのみで、みず・くさ×2弱点の一撃をHP50%超で受けても即倒を防げる場合があります。わんぱくH32-B2-D32型でステルスロック設置→あくびで交代誘発→なまけるで体力維持という流れが基本です。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>オボン型（設置+あくび）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>すなおこし（99.5%）<br>
    <strong>性格：</strong>わんぱく　<strong>EV：</strong>H32-B2-D32<br>
    <strong>持ち物：</strong>オボンのみ<br>
    H199 / A132 / B152 / C79 / D108 / S67
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>じしん / あくび / ステルスロック / <strong>なまける（60.9%）or ふきとばし（34.8%）</strong>
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    先発または中盤以降の安定枠として機能。初手でステルスロック設置後、あくびで相手の交代を誘いながらじしんで削る。4枠目はなまける（長期居座り）かふきとばし（積みエース対策）かでパーティの役割分担が変わる。
  </p>
</div>

### 型2：たべのこし型（36.5%）

毎ターン最大HPの1/16を回復するたべのこしで長期消耗を狙う型。砂嵐ダメージを相手に与えながらこちらはたべのこしで継続回復し、なまけるを組み合わせると回復量がさらに上がります。

<div style="border:1px solid #e2e8f0;border-radius:10px;padding:16px;margin:12px 0;background:#fafafa">
  <div class="build-header">
    <strong>たべのこし型（毎ターン回復）</strong>
  </div>
  <p style="font-size:0.88em;color:#444;margin:8px 0">
    <strong>特性：</strong>すなおこし（99.5%）<br>
    <strong>性格：</strong>わんぱく　<strong>EV：</strong>H32-B2-D32<br>
    <strong>持ち物：</strong>たべのこし<br>
    H199 / A132 / B152 / C79 / D108 / S67
  </p>
  <p style="font-size:0.88em;margin:4px 0">
    <strong>技構成例：</strong>じしん / あくび / ステルスロック / <strong>なまける（60.9%）or ふきとばし（34.8%）</strong>
  </p>
  <p style="font-size:0.85em;color:#555;margin:8px 0">
    相手が集中攻撃せず削り合いになる局面でオボン型より優位。一発の強打でHPを大きく削られる展開ではオボンのほうが安定する。4枠目の選択基準はオボン型と同じ。
  </p>
</div>

---

## データ分析①：なまける採用率上昇とふきとばし減少の関係

M-2からM-3にかけて、なまける+7.7pp・ふきとばし-9.7ppという逆向きの変化が起きています。

カバルドンの技枠は「じしん・あくび・ステルスロック」の3枠がほぼ固定（採用率97.8%/93.9%/84.7%）のため、4枠目がなまけるかふきとばしかの二択になります。

ふきとばしは積み技（つるぎのまい・めいそう等）を使った相手を強制交代させる技で、積みエースへの対策として有効です。一方なまけるは自己回復技で長期居座りを支えます。

M-3環境ではミミッキュ（2位）のつるぎのまい採用率が80.8%と依然高いにもかかわらず、なまける型が増えています。これはカバルドンの役割が「積み対策役」から「設置役＋消耗役」にシフトしたことを示しており、積みエースへの対策はパーティの他のポケモンに任せる構成が増えていると読み取れます。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（98.2%）のくさ×2で大きくダメージを受ける。カバルドンのじしんはくさ/あく複合のマスカーニャに半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ石採用率97.4%のメガメタグロスはれいとうパンチ（60.0%）のこおり×2打点を持ち、カバルドンを確実に削る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（84.4%）のみず×2で継続的に削られる。なまけるでの回復が追いつきにくい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（90.7%）のみず×2で削られる。カバルドンのじしんはひこう/みずのギャラドスに無効</td>
</tr>
</tbody>
</table>
</div>

---

## パートナー（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" loading="lazy">
    <div class="name">ライチュウ</div>
    <div class="rate">同居10位</div>
  </div>
</div>

**ミミッキュ（1位）**はばけのかわとつるぎのまいでフィニッシャー役を担い、カバルドンが設置したステルスロックを活かして削れた相手を倒す役割分担です。

**メタグロス（2位）**はカバルドンが苦手なマスカーニャ（くさ）をサイコファング（91.1%）で処理できる役割を持ち、カバルドンが担えない物理エース枠として機能します。

**マスカーニャ（3位）**はカバルドンがステロ設置・砂嵐展開で削った相手にマスカーニャが畳み掛ける役割分担で同居します。カバルドンが序盤の設置役、マスカーニャが終盤の決め役という構成です。

**ガブリアス（5位）**はカバルドンと同じくステルスロック採用率が高く、どちらが設置役を担うかで選出を柔軟に変えられる形です。カバルドンが先発で設置、ガブリアスが後詰め攻撃役という分業も成立します。

---

## まとめ

M-3のカバルドンは使用率8位で環境の安定した耐久枠として機能しています。

- オボン59.3%・たべのこし36.5%の2択がほぼ全採用率を占める
- なまける60.9%（+7.7pp）が増加し、ふきとばし34.8%（-9.7pp）が減少
- 技4枠は「じしん/あくび/ステルスロック/なまける」が多数派
- わんぱくH32-B2-D32が最多EV（23.3%）：H199/B152/D108

みず・くさ・こおり×2弱点は環境上位のマスカーニャ・ラグラージ・アシレーヌ・ギャラドスに刺さるため、対面不利のポケモンへはパーティの他の枠で対応しつつ、カバルドン自身はステロ設置と砂嵐展開で間接的に試合に貢献する設計が基本です。

---

## 関連記事

- [ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)
