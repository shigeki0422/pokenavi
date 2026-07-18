---
title: '【ポケモンチャンピオンズ】カバルドン考察 M-4 使用率3位・ふきとばし急増と物理耐久型シフトの理由'
description: 'M-4シングルバトルで使用率3位（M-3の6位から上昇）のカバルドンを徹底分析。ふきとばし47.7%（+12.9pp）急増・EV最多がB32型に逆転した背景・B187の物理耐久実数値・わんぱくH32-B32-D2型の採用理由をDBデータで解説します。'
updatedDate: '2026-07-18'
pubDate: '2026-07-16'
heroImage: '../../assets/hero-hippowdon-m4.png'
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
      使用率: <strong style="color:#e67e22">3位</strong>　特性: <strong>すなおこし 99.8%</strong>
    </div>
  </div>
</div>

> 本記事はM-4シーズンのデータです。M-3記事は[こちら](/blog/hippowdon-analysis-m3/)。

シーズンM-4のシングルバトルで、カバルドンは使用率3位。じめん単タイプで種族値合計525、すなおこしによる砂嵐展開・あくびでの交代誘発・ステルスロック設置を軸とした、環境屈指の耐久型ポケモンです。M-3からの変化点（ふきとばしの急増・EV配分の逆転）は後述のデータ分析で解説します。

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

HP108・ぼうぎょ118の高耐久が採用の根拠。すばやさ47（実数値67）は環境最低水準のため、先手で動くことは想定せず被弾前提のHP・防御重視型として運用されます。

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
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.8%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すなのちから</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.2%</td>
</tr>
</tbody>
</table>
</div>

**すなおこし**は場に出ると砂嵐を発生させる特性。砂嵐中はじめん/いわ/はがねタイプ以外のポケモンが毎ターン最大HPの1/16ずつダメージを受けます。カバルドン自身はじめんタイプのため砂嵐ダメージを受けず、なまけるやたべのこしの回復と組み合わせると長期消耗戦を優位に進められます。採用率99.8%で実質固定です。

---

## 主な型

### 型1：B32型（オボンのみ・たべのこし）

**性格: わんぱく**

M-4で最多EVになったH32-B32-D2型（EV採用率22.8%）。わんぱくのB↑補正と合わせてB187を確保し、環境上位のメタグロス（4位）が採用するサイコファング94.7%・バレットパンチ92.4%の物理打点を安定して受けられます。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">B32型（物理耐久重視）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> オボンのみ（61.9%）またはたべのこし（35.7%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ふきとばし（47.7%）<br>
・ステルスロック（76.2%）またはなまける（61.4%）
</div>
</div>
</div>

物理攻撃を主体とする相手にぶつける枠。B187の高い物理耐久でメタグロスの連打を受けながら、あくびで交代を誘いつつじしん（メタグロスに×2）で削ります。

**強み:**

H215 / A132 / B187 / D94 / S67。ふきとばし採用時はつるぎのまいを積んだミミッキュ（使用率2位）やガブリアス（使用率1位）のつるぎのまい29.2%を流す対策として機能します。

**弱み:**

物理方向に寄せているため、特殊アタッカーからの一撃には型2（D32型）ほど強くありません。

---

### 型2：D32型（オボンのみ・たべのこし）

**性格: わんぱく**

M-3まで最多だったH32-B2-D32型（EV採用率19.0%）。D124とわんぱくのB154を確保しつつ、特殊方向も拾える構成。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">D32型（特殊耐久も確保）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32-B2-D32<br>
<strong>持ち物:</strong> オボンのみまたはたべのこし
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック（76.2%）<br>
・なまける（61.4%）またはふきとばし（47.7%）
</div>
</div>
</div>

アシレーヌ（同居3位）のうたかたのアリア88.2%やサザンドラ（同居8位）の特殊打点を意識する場合はこちらを選びます。

**強み:**

H215 / A132 / B154 / D124 / S67。みず/こおりの特殊技を安定して耐えられる局面が増えます。

**弱み:**

B32型よりぼうぎょが33低くなり、物理アタッカーからの一撃には型1より劣ります。

---

## データ分析①：M-3→M-4 採用率変化

### 技採用率（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">97.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>98.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+0.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">93.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>94.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">≒同</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">84.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>76.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626"><strong>-8.5pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>61.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">≒同</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a"><strong>+12.9pp</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#666">+0.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほえる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.9pp</td>
</tr>
</tbody>
</table>
</div>

M-4で最も目立つ変化は**ふきとばし+12.9pp（34.8%→47.7%）**と、それと連動した**ステルスロック-8.5pp（84.7%→76.2%）**です。ふきとばしが増えた背景とステルスロックが減った背景については、後述のデータ分析セクションで詳しく考察します。

### 持ち物採用率（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オボンのみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">59.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">61.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たべのこし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>35.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.8pp</td>
</tr>
</tbody>
</table>
</div>

持ち物構成はM-3からほぼ変わらず、オボンのみ61.9%・たべのこし35.7%の2択が97%以上を占めます。

### 性格分布（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">補正</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わんぱく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">69.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">72.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ とくこう↓</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう↑ こうげき↓</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ↑ すばやさ↓</td>
</tr>
</tbody>
</table>
</div>

わんぱくが72.6%とM-3より+3.1ppさらに増加しており、B方向への強化が環境の主流です。

### EV配分（M-3比較）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">EV配分</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3最多</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">概要</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-B32-D2</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">22.8%（新最多）</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・ぼうぎょ全振り</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>H32-B2-D32</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.3%（旧最多）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP・とくぼう全振り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B22-D10</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・B重視型</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32-B22-D12</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全振り・B重視型</td>
</tr>
</tbody>
</table>
</div>

M-3最多だったH32-B2-D32（D全振り型）からH32-B32-D2（B全振り型）が逆転してM-4の新最多になりました。EV最多が入れ替わった背景はデータ分析③で詳述します。

### 代表型の実数値比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">わんぱく H32-B32-D2<br>（M-4最多）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">わんぱく H32-B2-D32<br>（M-3最多）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>215</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>215</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">132</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">132</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ（わんぱく↑）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">187</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">154</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">94</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>124</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67</td>
</tr>
</tbody>
</table>
</div>

M-4最多のB32型はB187と、M-3最多のD32型（B154）より33ポイント高い物理耐久を確保します。その代わりD実数値はD94に下がり、特殊方向はD124のD32型に比べて30ポイント低くなります。

---

## データ分析②：ふきとばし急増とステルスロック減少の連動

M-4でカバルドンの技構成に最大の変化が起きました。ふきとばし+12.9pp（34.8%→47.7%）とステルスロック-8.5pp（84.7%→76.2%）が逆向きに動いており、この2つの変化は連動しています。

カバルドンの技枠は「じしん・あくび」がほぼ固定（98.4%/94.0%）のため、残り2枠の構成が変化のポイントです。M-3では「ステルスロック+なまける」が多数派でしたが、M-4では「ふきとばし」が4枠目の選択肢として浸透したことで、ステルスロックを外してふきとばしを採用する構成が増えました。

**ふきとばしが増えた理由**はガブリアス（使用率1位）のつるぎのまい採用率29.2%と、ミミッキュ（使用率2位）のつるぎのまい84.8%の存在です。あくびで交代を誘いながらふきとばしでリセットすると、積みを使った相手を強制退場させられます。ほえる（採用率4.1%）も同じ強制交代技ですが、ふきとばしに採用が集約されています。

**ステルスロックが減った理由**は、ステルスロックの主な受益者であるミミッキュ・マスカーニャが交代を嫌うポケモンで、あくびによる交代誘発でステルスロックのダメージを稼ぐ展開が成立しにくい点にあります。ステロ設置の担い手はガブリアス（ステルスロック49.6%）やブリジュラス（ステルスロック37.9%）も担えるため、カバルドンが担う必要性が下がったと解釈できます。

---

## データ分析③：EV最多逆転——B32型台頭とメタグロスの物理化

M-3最多のH32-B2-D32（D全振り）からH32-B32-D2（B全振り）が逆転したM-4のEVシフトを数値で確認します。

メタグロス（使用率4位、メガストーン採用率ほぼ100%）の主力技採用率はサイコファング94.7%・バレットパンチ92.4%と物理技が主流です。D32型（B154）でも受けられますが、B32型（B187）はさらに33ポイント高い物理耐久を確保します。

M-4環境でブリジュラス（使用率5位）・メタグロス（4位）と物理型の高使用率ポケモンが上位に並んでいることが、カバルドンの物理耐久重視化を後押しした構図です。

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
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（97.3%）のくさ×2で大きくダメージを受ける。カバルドンのじしんはくさ/あく複合のマスカーニャに半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（88.2%）のみず×2で継続的に削られる。じしんはみず/フェアリー複合に等倍で有効打にはなるが、うたかたのアリアのダメージがなまけるの回復量を上回る局面が多い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドンの主力技じしんがひこう複合で無効（×0）。たきのぼりのみず×2で弱点を突かれる。ふきとばし非採用型では積まれた際の打点がなく止めにくい</td>
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
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率6位（M-4新）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率7位（M-3：9位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率8位（M-3：4位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率9位（M-3：5位）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率10位（M-4新）</div>
  </div>
</div>

**ミミッキュ（1位）**はM-3から引き続き同居トップ。ばけのかわとつるぎのまい（84.8%）でフィニッシャー役を担い、カバルドンがあくびとふきとばしで場を整えた後に積んで全抜きを狙う役割分担です。

**メタグロス（2位）**ははがねタイプのためマスカーニャのトリックフラワー（くさ）を半減でき、カバルドンが苦手なマスカーニャへの対抗手段を担える耐性が同居の軸です。

**アシレーヌ（3位・M-3：8位）**は味方として同居率3位に入る一方、対戦相手としてのアシレーヌは苦手なポケモン（使用率7位）でもあります。カバルドンが対面できないひこう/ドラゴン複合やガブリアスへの対抗手段をパーティに加える意味で、選出時はアシレーヌを分けて採用し、カバルドン自身は他の役割を担う構成が中心です。なおアシレーヌはカバルドンが展開した砂嵐でダメージを受ける点も同居時の留意点です。

**ブリジュラス（5位）**ははがねタイプのため砂嵐ダメージを受けません。カバルドンが不得意な特殊攻撃（りゅうせいぐん71.9%・ラスターカノン76.4%）をブリジュラスが担い、物理受けのカバルドンと特殊攻撃役のブリジュラスで役割を分担する構成です。

---

## まとめ

M-4のカバルドンは使用率3位に上昇し、M-3からの主な変化は以下の2点です。

- **ふきとばし47.7%（+12.9pp）**：ガブリアス・ミミッキュのつるぎのまいを流す積みリセット役として機能
- **EV最多がH32-B32-D2（22.8%）に逆転**：わんぱく補正込みでB187を確保。メタグロスの物理連打を安定して受ける物理環境への対応

技4枠の構成は「じしん/あくび/ふきとばし/ステルスロック」か「じしん/あくび/なまける/ステルスロック」かで選出意図が変わります。前者は積みエース対策を自身で担い、後者はステロ設置と長期消耗を優先するかたちです。パーティの積みエース対策が他の枠で確保できているかどうかで選択してください。

---

## 関連記事

- [カバルドン考察 M-3](/blog/hippowdon-analysis-m3/)
- [ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)
</content>
