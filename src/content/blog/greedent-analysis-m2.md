---
title: '【ポケモンチャンピオンズ】ホルード考察 M-2 使用率64位 ちからもち・タスキでじしんを上から通す物理アタッカー'
description: 'M-2シングルバトルで使用率64位のホルードを徹底分析。ちからもち（採用率99.8%）で実質A実数値236相当のじしん、れいとうパンチ・かみなりパンチのパンチ範囲、きあいのタスキ79.3%・スカーフ14.5%の持ち物分岐を実データで解説。S130の中速とノーマル単の弱点も両面から検証します。'
pubDate: '2026-06-11'
draft: true
heroImage: '../../assets/hero-greedent-m2.png'
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
  <img src="/images/pokemon/pokemon-0660-00.webp" alt="ホルード" />
  <div>
    <h2 style="margin:0 0 8px">ホルード</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">64位</strong>　特性: <strong>ちからもち 99.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ホルードは**使用率64位**を記録。特性は**ちからもち（採用率99.8%）**でほぼ統一されており、ほおぶくろ・ものひろいは少数派です。

ホルードの軸は**ちからもちでこうげき実数値が2倍になる**点です。こうげき種族値は56と低いものの、いじっぱりAS振りでA実数値118、ちからもち適用後は実質**236相当**となり、A130のブリジュラスやA134のカイリューを上回る火力で物理技を撃てます。じしん（採用率99.7%）を主軸に、れいとうパンチ・かみなりパンチでパンチ範囲を広げる中速物理アタッカーです。

持ち物は**きあいのタスキ 79.3%・こだわりスカーフ 14.5%**に二分されます。本記事ではタスキ型を基準に、スカーフ型の差分も併せて解説します。

---

## なぜホルードが使われるのか

### 1. ちからもちで実質A実数値236相当のじしんを撃つ

ホルードのこうげき種族値は56と低水準ですが、特性**ちからもち（採用率99.8%）はこうげき実数値を2倍にする**ため、火力は種族値の見た目を大きく超えます。いじっぱりAS振りでA実数値118、ちからもち適用後は実質**A実数値236相当**。これはA130のブリジュラス（いじっぱりAS振りでA実数値約200）やA134のカイリューを上回り、A56という低種族値からは想像しにくい高火力を、じしん（採用率99.7%）に乗せられます。

### 2. じしんがはがね・どく・いわ・でんき勢に広く刺さる

ホルードの技で最も採用率が高いのは**じしん（99.7%）**です。じめん技は環境上位のブリジュラス（はがね/ドラゴン・2位）・ルカリオ（かくとう/はがね・9位）・ゲンガー（ゴースト/どく・10位）・ギルガルド（はがね/ゴースト・11位）・ドドゲザン（あく/はがね・24位）にいずれも×2で通り、キラフロル（いわ/どく・15位）には×4で刺さります。ちからもちの2倍火力と合わせ、これらの高耐久はがね・どく勢を上から削れるのが大きな採用理由です。

### 3. れいとうパンチ・かみなりパンチでじしんの通らない相手を補完

じしんが等倍以下になる相手には、れいとうパンチ（採用率82.1%）・かみなりパンチ（47.7%）でパンチ範囲を補完します。れいとうパンチはガブリアス（ドラゴン/じめん・1位）・カイリュー（ドラゴン/ひこう・16位）に×4、かみなりパンチはギャラドス（みず/ひこう・12位）に×4・アシレーヌ（みず/フェアリー・4位）に×2と、じしんが無効（リザードン）または等倍止まりの飛行・水複合に刺さります。じしん一辺倒では不利な相手をパンチ技で拾えるのが、ホルードの技範囲の広さです。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:28%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">56</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">77</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:25%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">77</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">423</span>
  </div>
</div>

合計種族値423と低めですが、ちからもちでこうげきが実質2倍になるため、表示種族値A56からは想像できない火力を出せます。すばやさ種族値78はいじっぱりAS振りで**S実数値130**、ようきなら**S実数値143**で、環境の中速帯に位置します。HP85・B77・D77と耐久は並程度で、きあいのタスキで弱点技を1回耐えてから動くのが基本です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
</div>

ホルードは**ノーマル単タイプ**です。弱点・耐性が少なく、弱点はかくとうのみ、ゴースト技を無効化できるのが対戦上の特徴です。

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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span style="color:#94a3b8">なし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト
  </td>
</tr>
</tbody>
</table>
</div>

ノーマル単は弱点がかくとうの1タイプのみで、ゴースト技を無効化できます。ゲンガー（ゴースト/どく）のシャドーボールやミミッキュ（ゴースト/フェアリー・19位）のゴースト技を透かせる一方、かくとう技は等倍より重い×2で通る点に注意が必要です。ルカリオのインファイト（採用率71.5%）・ばかぢからを持つかくとう勢には、タスキで耐えても返しに落とされやすくなります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力打点。はがね・どく・いわ・でんき・ゴースト勢に広く刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>でんこうせっか</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">83.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。ちからもち補正が乗り低HP・タスキ持ちを処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリューに×4。じしん無効のひこう複合への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスに×4・アシレーヌに×2。みず複合への打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中時に相手のSを1段階下げる。リザードン等ひこうへの打点兼速度操作</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハッサム・アーマーガア等はがね複合への打点。10%やけど</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ばかぢから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドドゲザン等あく・いわへの打点。使用後A・Bが1段階下がる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代できる。対面操作で不利対面を入れ替える</td>
</tr>
</tbody>
</table>
</div>

じしん・れいとうパンチ・でんこうせっかの3枠がほぼ固定で、4枠目をかみなりパンチ（みず複合）・がんせきふうじ（ひこう＋速度操作）・ほのおのパンチ（はがね複合）から相手依存で選ぶのが標準的な技構成です。

---

## 主要型の解説

各型は持ち物分布（きあいのタスキ79.3%／こだわりスカーフ14.5%）を指標としています。性格はいじっぱり80.1%・ようき18.6%が主流で、火力を活かすいじっぱりが多数派です。

### 型1: きあいのタスキ物理アタッカー型（最多）

**指標: きあいのタスキ 79.3%／いじっぱり 80.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0660-00.webp" alt="ホルード" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ちからもち（99.8%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り。余りはH）<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・れいとうパンチ<br>
・でんこうせっか<br>
・かみなりパンチ / がんせきふうじ
</div>
</div>
</div>

**強み:**

きあいのタスキで弱点のかくとう技や、ちからもちを持たないこちらの低耐久でも、一撃を確実に1回耐えて反撃できます。S実数値130から動けない高耐久のブリジュラス・カバルドンには、タスキで耐えてからじしんの2倍火力を通せます。でんこうせっか（採用率83.7%）を採用すれば、タスキで耐えた次のターンに先制技で削り残しやタスキ持ちを処理でき、スカーフ型では持てない「耐えてから先制で詰める」動きが取れます。

**弱み:**

タスキはステルスロックや天候・先制技のダメージで簡単に潰れます。スカーフ型と異なり素早さ補正がかからないため、S実数値130を上回る中速〜高速帯（ガブリアスS実数値169・マスカーニャS実数値192等）には先手を取られ、タスキを貫通する連続技や弱点技で押し切られます。

---

### 型2: こだわりスカーフ型（14.5%）

**指標: こだわりスカーフ 14.5%／ようき 18.6%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0660-00.webp" alt="ホルード" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ちからもち（99.8%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り）<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・れいとうパンチ<br>
・かみなりパンチ<br>
・がんせきふうじ / ばかぢから
</div>
</div>
</div>

**強み:**

ようきAS＋スカーフでS実数値が214まで上がり、タスキ型では先手を取られるガブリアス（S実数値169）・マスカーニャ（S実数値192）・ゲッコウガ（S実数値191）すら上から叩けます。ちからもちの2倍火力をそのままに、タスキ型では返り討ちにされる高速アタッカーへ先制でじしん・れいとうパンチを通せるのが、スカーフ型固有の利点です。

**弱み:**

こだわりで技が固定されるため、初手から技選択の読み合いが発生します。タスキを持てないため弱点技を耐える保険がなく、でんこうせっかも採用しにくくなる（こだわり中はスカーフ補正がかかった素早さで上を取れるため先制技の価値が下がる）ため、低耐久のまま被弾すると即座に崩れます。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ホルードと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ちからもちの2倍火力でじしん・パンチ範囲が広く通る一方、S実数値130（いじっぱり）は中速帯のため、ガブリアス・マスカーニャ等の高速勢には先手を許す点、そしてかくとう×2弱点を突かれると低耐久で崩れる点に注意してください。

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
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（はがね弱点）。ちからもちの2倍火力で高耐久でも削れる。S実数値130＞137の相手だが、こちらが速い。ただし10まんボルト（66.9%）は等倍で通り、撃ち合いは油断できない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんが×2（どく弱点）。ノーマル単はシャドーボール（採用率上位のゴースト技）を無効化できる。低耐久のゲンガーをじしんで一撃圏に入れられる。ただしS実数値110＞130でこちらが先手</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ 速度勝負</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうパンチが×4（ドラゴン2×じめん2）。ただしガブS実数値169＞いじっぱりホルードS実数値130で先手を取られ、じしん（99.2%）×2を先に被弾。スカーフ型（S実数値214）なら上から叩ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ じしんが無効</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ひこうでじしんが×0（無効）。れいとうパンチ等倍・かみなりパンチ×2でしか削れず、メガリザードンY（ほのお/ひこう）相手はかみなりパンチ×2が頼り。メガリザードンX（ほのお/ドラゴン・採用率34.9%）にはかみなりパンチが×0.5で半減され打点が薄い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S実数値192＞130でこちらより速い。はたきおとす（57.6%）でタスキ・スカーフを叩き落とされ、トリプルアクセル（72.2%・ノーマル単に等倍）の連続技でタスキを貫通される。じしんはくさ/あくに×0.5で半減され打点が薄い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう/はがねでインファイト（71.5%）がノーマル単に×2弱点。メガルカリオ（S実数値180）はこちらより速く、先制で弱点を突かれる。じしんは×2で通るが、タスキで耐えても返しに落とされやすい</td>
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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（71.5%）がノーマル単に×2弱点。メガルカリオはS実数値180でホルードより速く、先手のかくとう技で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがはがねに×2で通るので、タスキで耐えてから返すか、ひこう・エスパー・フェアリーの後続（リザードン等）でかくとう技を半減して受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ひこうでじしんが無効。S実数値167（メガY）でこちらより速く、かえんほうしゃ（42.4%）等で先に焼かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ（ひこうに×2）を入れた個体で対応するか、いわ・でんき・みずの後続でほのお技を半減して受ける。がんせきふうじでSを下げて後続に繋ぐのも有効</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（99.7%）の先制技でタスキ後の低HPを刈られる。つるぎのまい（86.6%）を積まれるとちからもちの2倍火力でも一撃で落とせず、積み後のバレットパンチで詰められる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんがはがねに×2、ほのおのパンチがむし/はがねに×4で通るので、ほのおのパンチ採用個体で先に削る。ほのお・ひこうの後続でバレットパンチを半減して受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S実数値192で非スカーフのホルードより速く、はたきおとすで持ち物を落とし、トリプルアクセルの連続技でタスキを貫通する。じしんはくさ/あくに×0.5で半減され打点が薄い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ型（S実数値214）なら上から叩ける。タスキ型では、ほのお・ひこう・むしの後続でくさ・あく技を半減して受け、後続から崩す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">イダイトウ オス（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/ゴーストでじしんが等倍。ノーマル単はゴースト技を無効化できるが、こちらの主力じしんが半減されず等倍止まりで一撃に届かず、撃ち合いで押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かみなりパンチ（みずに×2）採用個体で弱点を突く。でんき・くさの後続でみず技を半減して受け回す</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「ホルードの弱点かくとうを×2で突く相手」と「S実数値130を上回り、はたきおとす・先制技で隙を突く相手」に大別されます。いずれも単体での切り返しは難しいため、後続のタイプ補完で受ける構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0478-00.webp" alt="ユキメノコ">
    <div class="name">ユキメノコ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">こおり/ゴーストの高速アタッカー。ホルードが苦手な高速ドラゴンに先制打点を持つ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0900-00.webp" alt="バサギリ">
    <div class="name">バサギリ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">むし/いわの物理アタッカー。ホルードが等倍止まりのひこう・ほのおに弱点を突ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでホルードの弱点かくとうを半減し、苦手なルカリオを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストでかくとう技を無効化し、ルカリオのインファイトを透かす</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお/ひこうでかくとう技を半減。マスカーニャのくさ・あく技も受けられる</div>
  </div>
</div>

**パーティ構成の基本方針:**

ホルードは中速で弱点かくとうを×2で突かれるため、残り5体で以下の役割を補います。

1. **かくとう対策**: ひこう・エスパー・フェアリー（リザードン・ブリジュラス）でルカリオのインファイトを半減・無効化する枠
2. **高速アタッカー対策**: ユキメノコ等の高速枠で、ホルードが先手を取られるガブリアス・マスカーニャに先制打点を持つ
3. **じしん無効・等倍対策**: バサギリ等のひこう・ほのおへ弱点を突ける枠で、ホルードのじしんが通らないリザードンを崩す
4. **受け回し**: イダイトウ等でかくとう技を透かし、ホルードが落ちた後の対面を立て直す

---

## データ分析①：ちからもちが変える「種族値A56」の火力評価

ホルードのこうげき種族値は56で、これは環境上位の物理アタッカーと比べても最低クラスです。しかし特性ちからもち（採用率99.8%）でこうげき実数値が2倍になるため、実際の打点は種族値の数字と大きく乖離します。

| ポケモン | A種族値 | A実数値（いじっぱりAS） | ちからもち適用後 |
|---|---|---|---|
| ホルード | 56 | 118 | **236相当** |
| ブリジュラス | 130 | 約200 | — |
| カイリュー | 134 | 約205 | — |
| ガブリアス | 130 | 約200 | — |

A56という種族値だけを見るとアタッカー適性は低く見えますが、ちからもち適用後の**実質A実数値236相当**は、A130級のブリジュラス・ガブリアスのいじっぱりAS振り（A実数値約200）を上回ります。つまりホルードの火力評価は「種族値A56の弱いポケモン」ではなく「環境トップ級のA実数値を持つ物理アタッカー」として行うべきで、これがじしん99.7%という一点突破の技構成が成立する理由です。

一方で、この火力は特性に全面的に依存します。ちからもちを無効化されたり、特性が書き換わると火力が半減するため、ホルードの強さは「特性ありき」である点も同時に読み取れます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">タスキAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>タスキ 79.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">1回耐えて反撃。でんこうせっかで先制処理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">中速のため高速勢に先手を許す。ステロでタスキ消失</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">スカーフAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ 14.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S実数値214で高速勢も上から叩く</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技固定の読み合い。保険なしで低耐久のまま</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ホルードはちからもち（採用率99.8%）で実質A実数値236相当の火力を得る物理アタッカーです。じしん（99.7%）を主軸に、はがね・どく・いわ・でんき・ゴースト勢を上から削り、れいとうパンチ・かみなりパンチでじしんの通らないドラゴン・ひこう・みず複合を補完します。種族値A56からは想像できない火力が、特性によって成立しているのが最大の特徴です。

持ち物はきあいのタスキ79.3%・こだわりスカーフ14.5%に二分され、「1回耐えて先制で詰める」か「最速で上を取る」かで役割が変わります。一方、S実数値130（いじっぱり）は中速帯でガブリアス・マスカーニャ等の高速勢に先手を許し、ノーマル単のかくとう×2弱点を突かれると低耐久で崩れます。これらは構築単位の補完が前提で、苦手なルカリオ・リザードン・ハッサムには後続のタイプ補完で対応する必要があります。

---

## 関連記事

- [れいとうパンチが×4で刺さる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [じしんが無効で苦手 リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
</content>
</invoke>
