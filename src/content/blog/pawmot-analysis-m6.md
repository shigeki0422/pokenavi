---
title: '【ポケモンチャンピオンズ】パーモット 考察 M-6 シーズン 使用率28位の解説'
description: 'M-6シーズン使用率28位のパーモットを考察。でんき/かくとうの複合タイプとてつのこぶし・でんこうそうげきを軸に、きあいのタスキ採用率88.6%の1本構成、アシレーヌ・ギャラドスなど得意/苦手をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-pawmot-m6.png'
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
  <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" />
  <div>
    <h2 style="margin:0 0 8px">パーモット</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px" />
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">28位</strong>　特性: <strong>てつのこぶし 85.3%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも同時点のスナップショットを使用しています。

M-6シーズンのパーモットは使用率28位。でんき/かくとうの複合タイプに、パンチ技の威力を1.2倍にする特性てつのこぶしを組み合わせ、でんこうそうげき・インファイトの一致2打点で押し切る型が主流です。技構成・持ち物ともに1つの型へ収束しており、後述のとおりきあいのタスキが88.6%を占める1本構成のポケモンです。

---

## パーモットの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">115</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">490</span>
  </div>
</div>

A115・S105の物理アタッカー種で、B70・D60と耐久面はやや薄めです。C70はほぼ使わず、技構成は物理技一辺倒になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はじめん・エスパー・フェアリーの3タイプ（いずれも×2）で、耐性はいわ・むし・はがね・でんき・あくの5タイプ（いずれも×0.5）に及びます。使用率5位のカバルドンはじしん（じめん・威力100、採用率99.3%）を主力にしており、後述の苦手表のとおりこの弱点が実戦でも直接痛手になっています。

### 特性

**てつのこぶし（85.3%）**がほぼ固定で採用されています。パンチの技（でんこうそうげき・かみなりパンチ・れいとうパンチ・ほのおのパンチ・マッハパンチ等）の威力が1.2倍になる特性です。インファイトはパンチ技ではないため対象外で、威力補正はかかりません。もう一方の**ちくでん**（12.2%）はでんきタイプの技を無効化して最大HPの1/4を回復する特性で、でんき技を主体とする相手への受け出し用途ですが採用は少数です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>でんこうそうげき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">85.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき一致・パンチ技でてつのこぶし対象。使用後は自分のでんきタイプが失われる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>さいきのいのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">手持ちのひんしのポケモンを最大HPの1/2で復活させる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">77.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう一致だがパンチ技ではないためてつのこぶし対象外。使用後、自分の防御・特防が1段階下がる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パンチ技でてつのこぶし対象。ドラゴン/ひこう・ドラゴン/じめん等の複合弱点をつく</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マッハパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1でパンチ技のためてつのこぶし対象。削り合いで先手を確保</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほっぺすりすり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">必ず相手をまひ状態にする低威力技。少数派の選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パンチ技でてつのこぶし対象。でんこうそうげきの代替だが採用は少数</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パンチ技でてつのこぶし対象。はがね・むし複合への打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に固定する補助技。採用は少数</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねこだまし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+3で相手をひるませる。場に出て最初のターンのみ使用可能。採用は少数</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### アタッカー型（てつのこぶし・でんこうそうげき）

**代表的な性格: ようき（全体の性格採用率75.6%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アタッカー型（てつのこぶし・でんこうそうげき）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てつのこぶし（85.3%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ（88.6%）
</div>
<div>
<strong>技構成:</strong><br>
・でんこうそうげき<br>
・さいきのいのり<br>
・インファイト<br>
・れいとうパンチ
</div>
</div>
</div>

でんこうそうげき（でんき・威力120、てつのこぶしで威力144相当）とインファイト（かくとう・威力120）の一致2打点に、複合弱点を突くれいとうパンチ（こおり・威力75、てつのこぶしで威力90相当）を加えた構成です。さいきのいのりは高採用率ですが攻撃技ではなく、瀕死になった味方を最大HPの1/2で復活させる技で、パーティ全体の立て直しに使われます。ようき・EV H2-A32-S32のS実数値は**172**、A実数値は**167**です。

**強み:**

きあいのタスキ（採用率88.6%）を持たせることで、HPが満タンの状態から一撃で戦闘不能になる攻撃を受けてもHP1で耐えられます。S172は環境上位の多くの相手より速く、耐えてからマッハパンチ（優先度+1、てつのこぶしで威力48相当）で追撃するか、そのまま二の矢を継ぐ動きが取れます。

**弱み:**

きあいのタスキは連続技や複数体からの攻撃、状態異常のダメージでは発動せず、また既にHPが減っている場面では機能しません。1度発動すると効果が切れるため、対面を変えずに同じ相手と連続して戦う展開には弱くなります。

---

## データ分析：でんこうそうげき使用後のタイプ変化

でんこうそうげき（採用率85.1%）は、使用すると自分のでんきタイプが失われる効果を持ちます。この効果は本文の技解説だけでは伝わりにくいため、使用前後のタイプ相性の変化をデータで示します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">状態</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">耐性（×0.5）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用前（でんき/かくとう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用後（かくとう単タイプ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;gap:6px">
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

でんこうそうげき使用後は最大の弱点だったじめん（カバルドンのじしん等）が等倍に戻る一方、代わりにひこうが新たな弱点（×2）として加わり、はがね・でんきへの耐性も失われます。採用率85.1%の主力技を使えばこの状態は高頻度で発生するため、「でんこうそうげきを打った後のパーモットはじめん技を等倍で受けられるが、ひこう技には弱点を晒す」という点は選出・立ち回りの判断材料になります。

---

## 苦手なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ（採用率59.2%）は確定2発止まりで、メガボーマンダの主力すてみタックル（採用率73.4%）も確定2発と並びます。素早さは同速のため先手を取れるかは運次第で、最速個体（ようき/おくびょう計約25%）にはS189まで伸ばされ確実に上を取られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率77.5%）は確定3発止まり。素早さはパーモットが上ですが、メガグソクムシャの主力ドリルライナー（採用率25.6%）は確定2発でこちらより打点が高く、先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率77.5%）は確定3発止まり。カバルドンの主力じしん（採用率99.3%、じめん×2弱点）は確定1発で、先手を取っても押し切れません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%）は決定打に欠け、ギルガルドの主力ポルターガイスト（採用率54.0%）の確定1発に先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%）は確定2発。ミミッキュの主力じゃれつく（採用率98.1%、フェアリー×2弱点）も確定2発と並びますが、ミミッキュはかげうち（採用率96.1%、優先度+1）を持ち、削り合いで先に押し切ってきます。ばけのかわは1回分のダメージを無効化する代わりに最大HPの1/8を失う特性です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはアローラキュウコンが上。インファイト（採用率77.5%）は確定2発ですが、主力ムーンフォース（採用率47.1%、フェアリー×2弱点）も確定2発で、先手を取られるため先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%）では決定打に欠け、ラウドボーンの主力フレアソング（採用率99.4%）の確定2発に先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチ（採用率59.2%）は確定2発ですが、メガカイリューの主力りゅうせいぐん（採用率50.8%）も確定2発で並びます。メガカイリューはしんそく（採用率39.6%、優先度+1）を持ち、削り合いで先に押し切ってきます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率77.5%）は確定3発止まり。メガメタグロスの主力サイコファング（採用率78.2%、エスパー×2弱点）は確定2発で、先に押し切られます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%、でんき×2弱点）が確定1発。アシレーヌの主力ムーンフォース（採用率99.1%）も確定1発ですが、素早さで上回り先手を取って仕留められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率77.5%）が確定2発。ブリジュラスの主力りゅうせいぐん（採用率65.3%）も確定2発ですが、素早さで上回り先手を取り続けられます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%、でんき×4弱点）が確定1発。ギャラドスの主力じしん（採用率53.4%）も確定1発ですが、素早さで上回り先手を取って仕留められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんこうそうげき（採用率85.1%）が確定1発。メガリザードンYの主力かえんほうしゃ（採用率42.9%）も確定1発ですが、素早さで上回り先手を取って仕留められます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でパーモットと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0972-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**グソクムシャ**（1位）はグソクムシャナイト採用率98.9%とほぼメガ進化前提で、メガ進化後はむし/はがねになります。メガグソクムシャもでんき・じめんとも等倍で受けるため、パーモットの弱点であるじめんを肩代わりできる関係ではありません。

**アシレーヌ**（3位）はみず/フェアリーで、自身の弱点であるでんき技をパーモットが半減で受けられます。パーモットの弱点であるフェアリー技については、アシレーヌ自身もフェアリータイプのため等倍で受けてしまい、この方向の補完はありません。

**ボーマンダ**（4位）はドラゴン/ひこうで、パーモットの弱点であるじめん技を無効化できます。逆にボーマンダの弱点であるいわ技はパーモットが半減で受けられるため、じめん・いわを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**サーフゴー**（10位）ははがね/ゴーストで、パーモットの弱点であるエスパー・フェアリー技をそれぞれ半減で受けられます。パーモットの3弱点のうち2つをサーフゴーがカバーする組み合わせです。

---

## まとめ

M-6のパーモットは使用率28位ながら、技構成・性格・持ち物のいずれも1つの型へ強く収束したポケモンです。

- **技構成**：でんこうそうげき（85.1%）・インファイト（77.5%）の一致2打点にれいとうパンチ（59.2%）・マッハパンチ（51.1%）を添えた構成が主流です
- **持ち物**：きあいのタスキが88.6%を占め、こだわりスカーフ（3.6%）・いのちのたま（3.1%）は少数派にとどまります
- **でんこうそうげき使用後の仕様**：じめん弱点は消える代わりにひこうが新たな弱点になり、はがね・でんきへの耐性も失われます

A115・S105を活かした先手アタッカーとして機能する一方、じしん（採用率99.3%）を主力とするカバルドンには打点で押し切れません。同じじめん弱点を突くメガグソクムシャのドリルライナーは採用率25.6%にとどまり、カバルドンほど一貫した脅威ではありません。じめん・エスパー・フェアリーの3弱点をパートナーでどう分散するかが選出の鍵になります。

---

**関連記事**: [アシレーヌ考察 M-6シーズン](/blog/primarina-analysis-m6/)
