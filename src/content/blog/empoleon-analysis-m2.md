---
title: 'エンペルト考察 M-2 使用率58位 多耐性の起点作り・サイクル型'
description: 'チャンピオンズM-2使用率58位エンペルトを徹底解説。みず/はがねの多耐性（こおり・はがね×0.25、どく無効、半減以下10タイプ）とかちき（採用率72.9%）を軸に、ステルスロック47.3%・あくび42.8%・クイックターン30.9%の受け回し型を、シュカのみ50.4%の持ち物分布と実データで解説します。'
updatedDate: '2026-07-18'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-empoleon-m2.png'
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
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0395-00.webp" alt="エンペルト" />
  <div>
    <h2 style="margin:0 0 8px">エンペルト</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">58位</strong>　特性: <strong>かちき 72.9%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、エンペルトは**使用率58位**を記録。特性は**かちき（採用率72.9%）**が主流で、げきりゅう（27.1%）は少数派です。

エンペルトの軸は**みず/はがねという多耐性タイプ**です。こおり・はがねを×0.25、どくを無効化し、半減以下に抑えるタイプが10種に及びます。この受け性能を活かし、ステルスロック（採用率47.3%）・あくび（42.8%）・クイックターン（30.9%）で後続の露払いとサイクルを回す、起点作り兼サイクル型のポケモンです。

持ち物は**シュカのみ 50.4%**が最多で、4倍弱点を持たないエンペルトが半数でじめん半減きのみを採用するのは、後述の弱点事情によるものです。本記事では受け出して設置・あくびを撒く型を基準に、HC火力寄りの型も併せて解説します。

---

## なぜエンペルトが使われるのか

### 1. みず/はがねの多耐性で後続の負担を減らす

エンペルトはみず/はがねの複合で、**こおり・はがねを×0.25、どくを無効化**し、ノーマル・みず・ひこう・エスパー・むし・いわ・ドラゴン・フェアリーを×0.5に抑えます。半減以下のタイプは合計10種で、環境の多様な攻撃を1体で受け止められるのが最大の採用理由です。HP191・B140・D168（なまいき）と耐久実数値も高く、半減技なら複数回受けて行動できます。

### 2. ステルスロック・あくびで後続の起点を作る

エンペルトの技で採用率が高いのは**なみのり（75.6%）・れいとうビーム（64.8%）**の攻撃技ですが、ステルスロック（47.3%）・あくび（42.8%）の設置・状態異常技も高採用です。耐性で安全に受け出し、ステルスロックを撒いて後続の削りを補助したり、あくびで相手を交代・眠りに追い込んで隙を作ったりと、低速ながら盤面を整える役割を担えます。

### 3. クイックターンで対面を維持しながら引く

クイックターン（採用率30.9%）はみずタイプの優先度0・威力60の攻撃技で、攻撃後に控えと交代できます。多耐性で受け出し→ステロやあくびを撒く→クイックターンで有利な後続に引く、という一連のサイクルでアドバンテージを取り続けられます。とんぼがえり系の技を持つことで、低速のエンペルトでも対面を一方的に押し付けられるのが強みです。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">84</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">86</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">88</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">111</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">101</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#f87171,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

とくこう111・とくぼう101を軸に、HP84・B88とバランスの取れた耐久を持つ両受け寄りのアタッカーです。すばやさ60は環境では遅く、無振りでもS112にとどまるため、上から殴る役割ではなく「受けてから動く」立ち回りが基本になります。多耐性と高い特殊耐久を活かし、後続の補助に回りやすいステータス配分です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½・¼）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり¼</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね¼</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点はでんき・かくとう・じめんの3タイプのみで、半減以下が10タイプと多いのがみず/はがねの強みです。一方、弱点の3タイプはいずれも環境上位に高威力技の使い手が多く（ウォッシュロトムのでんき、ガブリアスのじめん、ルカリオのかくとう）、低速のエンペルトは先に弱点技を被弾しやすい点が課題です。シュカのみ（採用率50.4%）の高採用は、ガブリアス・カバルドン等のじめん技を1発半減して受けるための択であり、4倍弱点がないにもかかわらず半減きのみが選ばれる理由になっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致の安定打点。リザードン・じめん勢に有効</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン・じめん・ひこうへの打点。ガブリアスに×4。10%こおり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんくうは</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。低速を補い、削れた相手を縛れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技。受け出しの隙に撒いて後続の削りを補助</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">42.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を交代か眠りに追い込む。積みの抑止・対面操作に</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。対面を維持しサイクルを回す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致技。フェアリー・いわへの打点。10%Dダウン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くさむすび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">重さ依存</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン等の重いみず・じめん・いわへの打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP回復技。受け出し回数を増やす</td>
</tr>
</tbody>
</table>
</div>

なみのり・れいとうビームの攻撃2枠に、ステルスロック・あくび・クイックターンから役割に応じて1〜2枠、残りをしんくうはやラスターカノンで埋めるのが標準です。攻撃技を最小限にして設置・あくびを優先する起点作り寄りの構成と、なみのり・れいとうビーム・くさむすび等で打点を確保する火力寄りの構成に分かれます。

---

## 主要型の解説

各型は持ち物分布（シュカのみ50.4%／たべのこし20.5%／オボンのみ15.0%）と性格分布（ひかえめ53.7%／なまいき16.2%／おだやか10.3%）を指標としています。EVはHD振り（特殊受け）とHC振り（特殊アタッカー）に二分しており、役割で性格・持ち物が変わります。

### 型1: HD起点作り・サイクル型（最多）

**指標: シュカのみ 50.4%／HD振り（EV1位 12.1%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0395-00.webp" alt="エンペルト" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HDサイクル型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かちき（72.9%）<br>
<strong>性格:</strong> なまいき（D↑ S↓）<br>
<strong>EV:</strong> H32 D32（HD振り）<br>
<strong>持ち物:</strong> シュカのみ
</div>
<div>
<strong>技構成:</strong><br>
・なみのり<br>
・ステルスロック / あくび<br>
・クイックターン<br>
・れいとうビーム / しんくうは
</div>
</div>
</div>

**強み:**

火力寄りのHC型と異なり、HD振りでD168（なまいき）まで伸ばし、特殊技を半減以下に抑える耐性と合わせて複数回受け出せます。受けた隙にステルスロックやあくびを撒き、クイックターンで有利な後続に引く動きを最も安定して回せるのがこの型です。S下降のなまいきはトリックルーム下で先に動ける利点もあり、低速を逆手に取れます。

**弱み:**

HC型のように一致技で大きく削れず、相手を起点作り中心に動かすため、攻撃的な相手にはステロ・あくびを撒く前に押し切られる場面があります。なまいきはS100まで下がるため、トリックルーム下以外では多くの相手に後手を踏みます。

---

### 型2: HC特殊アタッカー型

**指標: ひかえめ 53.7%／HC振り（EV4位 6.1%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0395-00.webp" alt="エンペルト" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HC特殊型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かちき（72.9%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32 C32（HC振り）<br>
<strong>持ち物:</strong> シュカのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・なみのり<br>
・れいとうビーム<br>
・くさむすび / ラスターカノン<br>
・しんくうは / クイックターン
</div>
</div>
</div>

**強み:**

ひかえめHC振りでC179まで上げ、HD型では削り切れない相手も一致のなみのり・れいとうビームで大きく削れます。多耐性で受け出してから反撃する流れはHD型と同じですが、こちらは設置よりも打点で相手を処理する役割で、ガブリアスにはれいとうビーム×4、カバルドンにはなみのり・くさむすび×2と、受けてから一致打点で返せます。

**弱み:**

HD型に比べDが下がり（ひかえめ無補正でD153）、特殊耐久を割いた分、サザンドラ・ウォッシュロトム等の高火力特殊を複数回は受けにくくなります。あくび・ステロの枠を打点に回すため、後続の起点作りという役割は薄くなります。

---

### 補足: かちき・げきりゅうの特性分担

特性はかちき72.9%が主流です。かちきは相手に能力を下げられるととくこうが2段階上がる特性で、いかくや能力低下技に対する切り返しとして機能します。げきりゅう（27.1%）はHP1/3以下でみず技が1.5倍になる特性ですが、受け回し中心のエンペルトでは発動条件を満たしにくく、採用は少数です。どちらの型もかちきが基本となります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、エンペルトと相性がはっきり出るポケモンを有利・不利の両面から挙げます。みず/はがねの多耐性で広く受けられる一方、弱点（でんき・かくとう・じめん）を突く高威力技の使い手が環境上位に多く、S112（無振り）以下と低速で先に被弾しやすい点に注意してください。

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
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ でんき技に注意</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんそく（ノーマル）を×0.5で受け、れいとうビームが×4（ドラゴン2×ひこう2）。ただし10まんボルト（47.6%）がでんき×2で刺さり、こちらが先制で落とせなければ被弾する。じしん（15.2%）もでんき同様の弱点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技は等倍だが高いD耐久で受けられ、なみのりが×2。ソーラービーム（61.0%）はくさ→みず2×はがね0.5で等倍に収まる。かみなりパンチ（18.2%）を持つ個体にはでんき×2で注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ かくとう技に注意</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（こおり）は×0.25、はたきおとす（あく）は等倍で耐久次第。けたぐり（12.5%）等のかくとう技は×2なので、持つ個体には注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ シュカで五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2弱点。シュカのみで1発半減すればれいとうビーム×4で返せるが、シュカ消費後の2発目や、げきりん（あくび誘発を嫌った択）には注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ じめん技に注意</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）が×2だが、なみのり×2・くさむすび×2（重量級で高威力）で返せる。シュカのみで地震を受けつつあくび・ステロを撒ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）が×2弱点。みず技は等倍、ラスターカノンは×0.5と打点が乏しく、ボルトチェンジ（88.7%）で対面を維持されサイクルを崩される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンでみず・はがね技を半減。かくとう技（しんくうは×2）しか弱点を突けず威力40では削り切れず、ラスターカノンも×0.5で押し負ける</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

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
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）が×2弱点。みず技は等倍・はがね技は×0.5で有効打が薄く、ボルトチェンジ（88.7%）でサイクルを回される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき無効のじめん枠（ガブリアス・カバルドン）に引いてボルトチェンジごと透かし、上から打点を入れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンでみず・れいとうビーム・ラスターカノンを半減〜等倍。しんくうは（×2）以外に弱点を突けず、高耐久で撃ち合いに勝てない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめん・かくとう枠（ガブリアスのじしん、ルカリオのインファイト）を合わせてはがね弱点を突く</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）が×2弱点で、S169＞112で先手。シュカ消費後は地震2発で崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム×4で受けてから落とす。シュカ前提の受けになるため、くさ・こおり打点の後続を添えて2体目で詰める</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0530-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドリュウズ（同居率2位帯）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん）が×2弱点。すなかき下では先手を取られ、みず・くさ技がいずれも等倍（じめん2×はがね0.5）でしんくうは以外に有効打がなく、シュカ消費後に押し切られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・こおり・くさ技がすべて等倍でしんくうは（威力40）しか弱点を突けないため単体では止まらない。ほのお・かくとう・じめん枠（リザードン・ルカリオ）を後続に添えて処理する</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「エンペルトの弱点（でんき・じめん）を等倍以上で突き、低速のこちらに先制する相手」と「みず・はがね打点を半減し撃ち合いで上回る高耐久（ブリジュラス）」に大別されます。いずれも単体での切り返しは難しく、でんき・じめんを透かせる後続のタイプ補完が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0282-00.webp" alt="サーナイト">
    <div class="name">サーナイト</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">エスパー/フェアリーでかくとうを半減。エンペルトのステロ・あくびを起点に積みアタッカーとして通す</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0530-00.webp" alt="ドリュウズ">
    <div class="name">ドリュウズ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん/はがねでウォッシュロトムのでんきを無効化。エンペルトが苦手なでんき枠を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき無効のじめん枠。ステロの削りを活かしじしんで制圧する高速アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお/ひこうでかくとう・じめんを半減〜無効。エンペルトの弱点を広く補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき無効のじめん枠。砂で削りつつ高耐久で物理を受け、サイクルを補強</div>
  </div>
</div>

**パーティ構成の基本方針:**

エンペルトは低速で弱点3タイプを先制で突かれやすいため、残り5体で以下の役割を補います。

1. **でんき対策**: じめん（ガブリアス・ドリュウズ・カバルドン）でウォッシュロトムのでんき技・ボルトチェンジを無効化する枠
2. **じめん対策**: ひこう（リザードン）でガブリアス・ドリュウズのじしんを無効化する枠
3. **かくとう対策**: エスパー・フェアリー（サーナイト）でルカリオ等のかくとう技を半減する枠
4. **起点の活用**: エンペルトのステルスロック・あくびで作った隙を、高速アタッカー（ガブリアス・サーナイト）で詰める

---

## データ分析①：攻撃技より設置・対面操作技が高採用

エンペルトの技採用率は、純粋なアタッカーと異なり**攻撃技と補助技が拮抗**している点に特徴があります。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| なみのり | 攻撃 | 75.6% | みず一致打点 |
| れいとうビーム | 攻撃 | 64.8% | ドラゴン・じめん |
| しんくうは | 攻撃（先制） | 50.7% | 低速補助 |
| ステルスロック | 設置 | 47.3% | 後続の削り |
| あくび | 対面操作 | 42.8% | 交代・眠り誘発 |
| クイックターン | 攻撃（交代） | 30.9% | サイクル維持 |

攻撃技のなみのり75.6%・れいとうビーム64.8%に対し、ステルスロック47.3%・あくび42.8%・クイックターン30.9%といった補助・対面操作技が軒並み3〜5割で採用されています。攻撃4枠で固める高速アタッカー（同環境のゲッコウガはれいとうビーム89.6%・あくのはどう75.9%と攻撃技が上位を占める）とは対照的に、エンペルトは**攻撃2枠＋補助1〜2枠**という構成が標準化しています。

これは、S112以下と低速で「上から殴る」役割が成立しにくいぶん、多耐性で受け出してから設置・あくびで盤面を整え、クイックターンで有利対面を作る——という起点作り兼サイクルの立ち回りが、エンペルトの種族値構成に合致しているためです。しんくうは（50.7%）も優先度+1で低速を補う先制技であり、技構成全体が「遅さを補い、後続を活かす」設計に寄っているのが採用率から読み取れます。

---

## データ分析②：シュカのみ50.4%が示す「じめん受け」の徹底

エンペルトはじめんに×4の弱点を持たないにもかかわらず、半減きのみのシュカのみが**採用率50.4%**と過半数を占めます。

| 持ち物 | 採用率 | 役割 |
|---|---|---|
| シュカのみ | 50.4% | じめん技を1発半減 |
| たべのこし | 20.5% | 毎ターン回復で受け継続 |
| オボンのみ | 15.0% | HP1/4回復で一度耐える |
| ヨプのみ | 4.6% | かくとう技を1発半減 |

通常、半減きのみは×4弱点を補うために採用されますが、エンペルトのじめん弱点は×2です。それでもシュカのみが過半数なのは、環境1位ガブリアス（じしん99.2%）・カバルドン・ドリュウズといった高威力じめん勢が多く、低速のエンペルトが**先制でじしんを被弾する前提**だからです。シュカのみで地震を1発半減すれば、その隙にあくび・ステロを撒くか、れいとうビーム×4で反撃する余裕が生まれます。

残りはたべのこし20.5%・オボンのみ15.0%と、いずれも受け継続を狙う回復系で固まっており、きあいのタスキ（4.2%）等の攻撃寄りの持ち物は少数です。持ち物分布全体が「受けてサイクルを回す」役割を裏付けており、起点作り型がエンペルトの主流であることが数値からも確認できます。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HDサイクル型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シュカ 50.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シュカのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D168で特殊を複数回受け、設置・あくびを安定して撒く</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">火力が低く、攻撃的な相手に押し切られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HC特殊型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ 53.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シュカのみ / たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">C179で受けてから一致技で大きく削れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">D耐久が下がり、起点作りの役割が薄い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

エンペルトはみず/はがねの多耐性（こおり・はがね×0.25、どく無効、半減以下10タイプ）とかちきを軸に、ステルスロック・あくび・クイックターンで後続の起点を作りサイクルを回す、低速の受け兼サポート枠です。攻撃技と補助技が拮抗する技採用率、シュカのみ50.4%・たべのこし20.5%の受け寄りの持ち物分布が、その役割を裏付けています。

一方、弱点のでんき・かくとう・じめんはいずれも環境上位に高威力技の使い手が多く、S112以下の低速で先制を許しやすいのが課題です。ウォッシュロトム・ブリジュラスのように打点を半減しつつ弱点を突く相手には単体で勝てないため、でんき・じめんを透かせる後続のタイプ補完を前提に組み込むポケモンです。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同じみず複合の高速特殊アタッカー ゲッコウガのM-2考察](/blog/greninja-analysis-m2/)
- [みず・はがね打点を半減する天敵 ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
