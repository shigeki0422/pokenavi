---
title: '【ポケモンチャンピオンズ】アシレーヌ考察 M-2 使用率4位 型別採用率と立ち回り'
description: 'M-2シングルバトルで使用率4位のアシレーヌを徹底分析。ムーンフォース採用率97%・うたかたのアリア79.2%を軸にしたみず/フェアリーの優秀な攻撃範囲、ひかえめ特殊型とずぶとい耐久型の違い、環境上位への相性を実データで解説します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-primarina-m2.png'
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
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
  <div>
    <h2 style="margin:0 0 8px">アシレーヌ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">4位</strong>　特性: <strong>げきりゅう 95.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、アシレーヌは**使用率4位**を記録。みず/フェアリーという受けにくい複合タイプと、とくこう種族値126・とくぼう116の高い特殊性能を活かした特殊アタッカー兼耐久枠として広く採用されています。

アシレーヌの軸は**ムーンフォース（採用率97.0%）とうたかたのアリア（79.2%）**の一致技2枚。みず・フェアリーはどちらも半減されにくく、環境上位のドラゴン・あく・ほのお・じめんに刺さるため、技スペースを攻撃技に割かずとも広い範囲に等倍以上を通せるのが最大の持ち味です。

---

## なぜ今アシレーヌが強いのか

### 1. ムーンフォース＋うたかたのアリアの受けにくい攻撃範囲

アシレーヌの一致技は**ムーンフォース（フェアリー・採用率97.0%）**と**うたかたのアリア（みず・79.2%）**。この2枚だけで環境上位の多くに等倍以上が通ります。

- ムーンフォースが×2: ガブリアス（1位）・マスカーニャ（3位）・カイリュー（16位）・ゲッコウガ（28位）
- ムーンフォースが×4: サザンドラ（21位・あく/ドラゴン）
- うたかたのアリアが×2: リザードン（5位）・カバルドン（7位）

うたかたのアリアは**音技なのでみがわりを貫通**し、相手の起点作りを許しません。一致技2枚で広範囲を見られるため、れいとうビーム（4.9%）などのサブ技は薄くても機能します。

### 2. とくこう126・とくぼう116の特殊性能

とくこう種族値**126**は特殊アタッカーとして高水準で、ひかえめ＋C最大振り（C32）でムーンフォースの火力を最大化できます。さらにとくぼう**116**と高く、特殊技に対しては受け出しから切り返せる硬さも兼ねます。

この特殊耐久の高さが、後述の**めいそう（採用率26.2%）型**を成立させています。めいそうでCとDを同時に上げれば、特殊アタッカーとの撃ち合いを優位にしつつ自分の火力も伸ばせます。

### 3. アクアジェットによる先制処理

アシレーヌはすばやさ種族値が**60**と遅く、環境上位の大半に先手を取られます。これを補うのが先制技**アクアジェット（採用率66.6%）**。優先度+1で動くため、**相手のすばやさに関わらず先制**でき、すばやさの遅さを抱えるアシレーヌが「削れた相手を先に倒す」「タスキ・低HPを処理する」動きを取れます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">126</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">116</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

とくこう126・とくぼう116の特殊偏重ステータス。HP80・B74・S60で物理耐久とすばやさは平凡なため、物理アタッカーに上から殴られる展開には弱く、**特殊方向の硬さと先制アクアジェットを軸に立ち回る**のが基本です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="フェアリー" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

フェアリーがドラゴンを無効化し、みず・フェアリー双方の耐性が重なってほのお・みず・こおり・かくとう・むし・あくの6タイプを半減します。**ドラゴン無効＋あく半減**により、ガブリアス・カイリュー・サザンドラのドラゴン技やマスカーニャ・ゲッコウガのあく技を受けにくいのが環境的に大きい点です。一方、弱点はでんき・くさ・どくの3タイプ。とくにウォッシュロトムのでんき技、フシギバナのくさ・どく技は×2で刺さります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力一致技。10%でC1段階ダウン。ドラゴン・あく・かくとうに刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>うたかたのアリア</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致技。音技でみがわり貫通。ほのお・じめん・いわに刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40 先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>66.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手のSに関わらず先制。すばやさの遅さを補う詰め技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>40.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に3ターン固定。積み技・補助技を読んで起点化を防ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代できる。不利な相手に切り返して有利な味方を出す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">CとDを1段階ずつアップ。特殊耐久型で採用。撃ち合いと火力を両立</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致技。うたかたのアリアの代替（命中100・追加効果なし）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">サブ技。くさ・じめん複合へのピンポイント打点</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

型①・型②は性格分布（ひかえめ／ずぶとい）を指標としています。

### 型1: ひかえめ特殊アタッカー型（最多採用）

**性格採用率: ひかえめ 64.9%**（特殊アタッカーの指標。性格分布のうちひかえめが最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ムーンフォース特殊ひかえめ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32 C32（HC振り。残り2はSかDに）<br>
<strong>持ち物:</strong> オボンのみ / しんぴのしずく
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・うたかたのアリア / なみのり<br>
・アクアジェット<br>
・アンコール / めいそう / クイックターン
</div>
</div>
</div>

**強み:**

HC振りでとくこう126を活かしつつ、HP80に振ってオボンのみ（採用率46.6%）の回復量を確保する型です。一致技2枚で広範囲を見つつ、先制アクアジェットですばやさ60の遅さをカバーします。アンコール（40.8%）を採れば、ガブリアスのつるぎのまいやウォッシュロトムのおにびといった補助・積み技を読んで縛り、起点化を防げます。

しんぴのしずく（16.7%）を持てばムーンフォースとみず技の火力が上がり、サザンドラ（あく/ドラゴンにムーンフォース×4）やガブリアス（×2）を一気に削れます。

**弱み:**

すばやさ60で環境上位の大半に先手を取られるため、でんき・くさ・どくの弱点技を持つ相手には上から弱点を突かれて落とされやすいです。オボンのみは1度しか発動せず、ウォッシュロトム・フシギバナのような弱点を連打してくる相手には回復が追いつきません。

### 型2: ずぶとい・めいそう耐久型（2番目に多い構成）

**性格採用率: ずぶとい 13.3%**（物理耐久型の指標。性格分布でひかえめに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">めいそうずぶとい耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（HB振り。物理方向を補強）<br>
<strong>持ち物:</strong> たべのこし / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・うたかたのアリア<br>
・めいそう<br>
・アクアジェット / アンコール
</div>
</div>
</div>

**強み:**

ずぶといでB方向を補強し、平凡なぼうぎょ74を底上げする型です。素のとくぼう116が高いため、めいそう（26.2%）を1積みすればCとDが同時に上がり、特殊アタッカーとの撃ち合いで一方的に有利を取れます。たべのこし（15.2%）と合わせれば、めいそうを積みながら居座って数的有利を作れます。

ひかえめ型がすばやさ・火力で勝負するのに対し、こちらは**物理耐久を補って積みの起点を増やす**型で、対面的な押し付けより居座りでの制圧を狙います。

**弱み:**

ひかえめ型と比べてC無補正のため、めいそうを積むまでの初動火力が低く、削り切れずに居座りを許す相手には手数で押し負けます。また、ぼうぎょを補ってもガブリアスのじしん（採用率99.2%）などは等倍で高威力のため、物理アタッカーの一致弱点技まで受けきれるわけではありません。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、アシレーヌと相性がはっきり出るポケモンを有利・不利の両面から挙げます。アシレーヌはドラゴン無効・あく半減で受けに強い一方、**すばやさ60と遅く先手を取られやすい**ため、でんき・くさ・どくの弱点技を持つ相手には注意が必要です。

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
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 超有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォースが×4（あく2×ドラゴン2）で確定圏。主力のあくのはどう（98.5%）・りゅうせいぐん（90.2%）・かえんほうしゃ（67.0%）はいずれもこちらが半減し、弱点を突く技を持たない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォースが×2。げきりん（47.9%）は無効、じしん（99.2%）も等倍止まり。ただしS102で先手を取られるため、削れた相手をアクアジェットで詰める動きが軸。どくづき（19.4%・どく）を持つ個体には×2で返される点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォースが×2でドラゴン技も無効だが、10まんボルト（47.6%・でんき）が×2弱点。S80で先手を取られるうえ、約半数の個体に上からでんき技で弱点を突かれるため撃ち合いは拮抗。でんき技のない個体には有利</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォースは×2で通るが、主力のトリックフラワー（92.9%・くさ）が×2弱点。S123で先手を取られるため、相手の一撃を受けてから返す展開になり撃ち合いは拮抗</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガY（ほのお/ひこう）にはうたかたのアリアが×2でほのお技も半減できるが、ソーラービーム（61.0%・くさ）が×2弱点でメガ後S実数値167に上から焼かれる。メガX（ほのお/ドラゴン）には一致技がともに等倍で有効打を欠く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技がともに等倍で高耐久を抜けず、はねやすめ（98.1%）で回復される。決定打を欠き、てっぺき（63.5%）の起点にされやすい</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

すばやさ60で先手を取られやすく、でんき・くさ・どくの弱点を突いてくる相手を中心に、使用率上位（TOP30目安）から相性が明確に悪い相手を挙げます。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき/みずでこちらのみず技を半減し、10まんボルト（56.8%）が×2弱点。S86で先手を取られ、おにび（80.6%）でめいそう型の起点化も止められる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんきを無効化するじめんタイプ（ガブリアス・カバルドン）を同伴し、ロトムの前で受けてじめん技で処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・どくの両方が×2弱点で、ギガドレイン（56.9%）・ヘドロばくだん（55.0%）のどちらでも弱点を突かれる。やどりぎのタネ（58.5%）＋こうごうせい（72.7%）で居座られると突破できない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・ひこう・エスパー技を持つポケモン（リザードン等）を同伴し、後出しから弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリアは×2で通るが、S86で先手を取られたうえヘドロウェーブ（69.4%・どく）が×2弱点。受け出しから一撃を受ける展開になり、撃ち合いは不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん技を持つポケモン（ガブリアス・カバルドン）を合わせ、いわ/どくの×4弱点をだいちのちから・じしんで突いて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S110で先手を取られ、ヘドロウェーブ（81.7%・どく）が×2弱点。こちらはうたかたのアリアが等倍・ムーンフォースは×0.5で有効打を欠き、撃ち合いで先に削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく・じめん技を持つポケモン（ドドゲザン・ガブリアス等）でゴースト/どくの弱点を突き、後出しから処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S123の高速くさ枠。アシレーヌが苦手なウォッシュロトムにくさ技で×4打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお火力でフシギバナ等のくさ枠を処理。アシレーヌのくさ弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんでウォッシュロトム・キラフロルのでんき/どく枠を上から処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでくさ・でんきを半減。ステロ展開で交換読みダメージ蓄積</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S110の高速特殊枠。アシレーヌが取りこぼす素早い相手を上から削る</div>
  </div>
</div>

**パーティ構成の基本方針:**

アシレーヌはドラゴン・あくに強くすばやさが遅いため、残り5体で**でんき・くさ・どく枠への対処**と**高速アタッカー**を補います。

1. **でんき・どく対策**: じめんタイプ（ガブリアス・カバルドン）でウォッシュロトム・キラフロルを受ける枠
2. **くさ対策**: ほのお・ひこうタイプ（リザードン）でフシギバナ等のくさ枠を処理する枠
3. **高速アタッカー**: マスカーニャ・ゲンガー等、すばやさ60で取りこぼす相手を上から処理する枠
4. **ステルスロック展開**: ブリジュラス・カバルドン等でステロを撒き、交換読みダメージを蓄積

---

## データ分析①：一致技2枚で完結する攻撃範囲

アシレーヌの技採用は**ムーンフォース97.0%・うたかたのアリア79.2%**の一致技2枚に集約され、サブ技のれいとうビームは4.9%と極端に低くなっています。これは「一致技2枚だけで環境上位への等倍以上が確保できる」ことを数値が示しています。

| 環境上位 | タイプ | ムーンフォース | うたかたのアリア | 最大倍率 |
|---|---|---|---|---|
| サザンドラ（21位） | あく/ドラゴン | **×4** | ×0.5 | ×4 |
| ガブリアス（1位） | ドラゴン/じめん | ×2 | ×1 | ×2 |
| カイリュー（16位） | ドラゴン/ひこう | ×2 | ×0.5 | ×2 |
| マスカーニャ（3位） | くさ/あく | ×2 | ×0.5 | ×2 |
| リザードン（5位） | ほのお/ひこう | ×0.5 | ×2 | ×2 |
| カバルドン（7位） | じめん | ×1 | ×2 | ×2 |

環境TOP10〜上位のうち6体に、一致技のいずれかが×2以上で通ります。これにより**4枠目をアンコール（40.8%）やめいそう（26.2%）といった補助技に割く余裕**が生まれ、単なるアタッカーではなく「起点回避・積み」までこなせる柔軟性が使用率4位を支えています。サブ攻撃技を積まなくても範囲が足りるという点が、アシレーヌが一貫してアンコール採用率4割を維持できる構造的な理由です。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">特殊アタッカー型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ひかえめ 64.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ムーンフォース・うたかたのアリア・アクアジェット・アンコール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">高火力と広範囲。先制と起点回避を両立</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S60で先手を取られ弱点技で落とされやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">めいそう耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい 13.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ムーンフォース・うたかたのアリア・めいそう・アクアジェット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B補強＋めいそうで特殊受けを起点に制圧</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C無補正で初動火力が低く手数で押し負ける</td>
</tr>
</tbody>
</table>
</div>

**総評:**

アシレーヌはムーンフォース＋うたかたのアリアの受けにくい一致技2枚と、とくこう126・とくぼう116の特殊性能を両立した使用率4位のアタッカー兼耐久枠です。ドラゴン無効・あく半減により、ガブリアス・サザンドラといった環境上位のドラゴン勢に強く出られるのが最大の武器です（ただしでんき技を持つカイリューには弱点を突かれるため過信は禁物）。

一方ですばやさ60と遅く、ウォッシュロトム・フシギバナ・キラフロルなどでんき・くさ・どくの弱点を突いてくる相手には上から処理されやすいため、じめん・ほのお枠でこれらをケアするパーティ構成が前提になります。先制アクアジェットと一致技の範囲を活かし、苦手な弱点枠を味方で受け持つ構成が安定します。

---

## 関連記事

- [同居率1位の高速くさ枠 マスカーニャのM-2考察](/blog/meowscarada-analysis-m2/)
- [同じみずタイプ スターミーのM-2考察](/blog/starmie-analysis-m2/)
- [一致技が刺さる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
