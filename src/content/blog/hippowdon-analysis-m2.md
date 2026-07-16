---
title: 'カバルドン考察 M-2 使用率7位 すなおこし起点作り型の構築と立ち回り'
description: 'M-2シングルバトルで使用率7位のカバルドンを徹底分析。じしん98%・あくび94%・ステルスロック84%という起点作り技構成、すなおこし99.8%、わんぱくHB型としんちょうHD型の使い分け、苦手なみず・くさ・こおり勢への対策を実データで解説します。'
updatedDate: '2026-06-11'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-hippowdon-m2.png'
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
      使用率: <strong style="color:#e67e22">7位</strong>　特性: <strong>すなおこし 99.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、カバルドンは**使用率7位**を記録。攻撃的なアタッカーが上位を占めるなか、耐久・起点作りに特化した受け役としてトップ10に定着しています。

カバルドンの役割は明確で、**あくび（採用率94.2%）で相手を流し、ステルスロック（84.4%）を撒き、なまける（53.2%）で居座る**という起点作りに特化しています。じめん単タイプの素直な耐性とHP108・ぼうぎょ118の高い物理耐久を土台に、後続のアタッカーが通る盤面を整えるのが仕事です。

---

## なぜカバルドンが7位に定着しているのか

### 1. あくび＋ステルスロックの起点作り

カバルドンの技構成は起点作りに振り切っています。**あくび（94.2%）**で相手に交代を強制し、生まれた交代の隙に**ステルスロック（84.4%）**を設置。相手は繰り出すたびに、いわタイプ相性に応じた固定割合（等倍1/8・×2なら1/4・×4なら1/2）を失うため、後続アタッカーの確定数が1つずつ繰り上がります。さらに**ふきとばし（44.5%）**で積みアタッカーの能力上昇をリセットしつつ、ステルスロックのダメージを強制的に蓄積させられます。

あくびは命中するとねむり状態の予約になるため、相手は受けるか交代するかの二択を迫られます。どちらに転んでもカバルドン側が次の行動（ステルスロック・なまける・交代）を選べるのが強みです。

### 2. すなおこし＋高物理耐久で居座る

特性は**すなおこし（99.8%）**がほぼ全個体。場に出た瞬間に5ターンの砂嵐が発生し、いわ・じめん・はがね以外のポケモンに毎ターン最大HPの1/16のスリップダメージを与えます。起点作りで稼いだ交代のたびに砂ダメージも乗るため、ステルスロックと合わせて相手の体力を継続的に削れます。

ぼうぎょ種族値118・HP108に加え、回復技**なまける（53.2%）**で最大HPの半分を回復できるため、物理アタッカーに対しては何度も居座って起点作りを繰り返せます。

### 3. でんき無効・いわ半減で受け出し先を選べる

じめん単タイプはでんき技を無効化し、いわ・どく技を半減します。環境では10まんボルト（ブリジュラス採用率66.9%）など、でんき技を透かして安全に着地できる場面が多く、ステルスロック設置の起点を得やすいのが利点です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
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

HP108・ぼうぎょ118の物理耐久が突出する一方、とくぼう72・すばやさ47は低水準です。素早さが遅いことは起点作りでは欠点になりにくく、むしろあくびを撃った後に交代されてもステルスロックを安全に設置できる利点として働きます。ただしとくぼう72のため、特殊アタッカー相手にはしんちょう＋とくぼう振り（後述のHD型）でなければ受けが安定しません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="じめん" />
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
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
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

弱点はみず・くさ・こおりの3タイプのみとシンプルで、いずれもこの3タイプを一致技で持つ相手（アシレーヌ・マスカーニャ・フシギバナ等）が天敵になります。でんき無効はブリジュラスやウォッシュロトムの10まんボルトを透かせる点で価値が高く、いわ半減はバンギラスのいわ技を受けやすくします。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほぼ唯一の攻撃技。一致技で最低限の打点を確保し、ねむり・交代に対する詰め手にもなる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">94.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次のターン終了時にねむり予約。交代を強制し、その隙に起点作り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">交代のたびに最大HP比のダメージ。後続の確定数を繰り上げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>53.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの半分回復。物理相手に居座って起点作りを繰り返す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>44.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-6。積みアタッカーを流し、ステルスロックのダメージを強制</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">砂・たべのこしのターン稼ぎ、あくびのねむりカウント調整</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほえる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふきとばしと同役割。みがわり貫通が必要な相手向けの選択肢</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス・カイリュー等のドラゴンへの打点を持つ少数派構成</td>
</tr>
</tbody>
</table>
</div>

攻撃技はじしん（98.0%）がほぼ唯一で、残り3枠はあくび・ステルスロック・なまける／ふきとばしという変化技で埋まります。攻撃に枠を割かず、起点作りと耐久に全振りした構成がカバルドンの主流です。

---

## 主要型の解説

EVスプレッドはHB寄り（ぼうぎょ）かHD寄り（とくぼう）かで二分されます。性格はわんぱく（74.2%）としんちょう（16.9%）が両型の指標です。

### 型1: わんぱくHB物理受け型（最多採用）

**性格採用率: わんぱく 74.2%**（HB物理受けの指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わんぱくHB型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32 B32（HB振り。HB系で最多の採用率18.1%）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック<br>
・なまける / ふきとばし
</div>
</div>
</div>

**強み:**

わんぱく＋HB振りでぼうぎょを最大化し、物理アタッカーへの受け出しに特化した型です。ガブリアス・マスカーニャといった高速物理アタッカーの一致技を受けつつ、なまけるで回復しながらあくび・ステルスロックを撒き続けられます。HD型より物理方面が硬く、ガブリアスのじしん（カバルドンは等倍）を安定して受けられるのが最大の差です。

**弱み:**

とくぼうに振らないため、アシレーヌのうたかたのアリア（採用率79.2%）やブリジュラスのりゅうせいぐん（64.8%）など特殊弱点技には脆くなります。HD型なら受けられる特殊アタッカーを取りこぼすのがHB型固有の穴です。

---

### 型2: しんちょうHD特殊受け型（2番目に多い構成）

**性格採用率: しんちょう 16.9%**（HD特殊受けの指標。わんぱくに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">しんちょうHD型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> しんちょう（D↑ C↓）<br>
<strong>EV:</strong> H32 D32（HD振り。採用率24.0%の最多スプレッド）<br>
<strong>持ち物:</strong> オボンのみ / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック<br>
・なまける / ふきとばし
</div>
</div>
</div>

**強み:**

しんちょう＋HD振りでとくぼうを補強し、素のとくぼう72では受けきれない特殊アタッカーに対応する型です。サザンドラのあくのはどう・ブリジュラスの10まんボルト（でんきは無効）など、特殊技中心の相手に居座って起点を作れます。EVスプレッド別ではHD型（H32 D32 B余り）が採用率24.0%で全スプレッド中最多であり、特殊環境への意識の高さが表れています。

**弱み:**

ぼうぎょに回す余裕が減るため、ガブリアスのじしん・スケイルショットやマスカーニャの物理一致技を受けたときの消耗がHB型より大きくなります。物理高火力に対してはなまけるの回復が追いつきにくい場面が出ます。

---

## 環境ポケモンへの相性分析

### 起点を作りやすいポケモン

使用率上位のうち、カバルドンが受け出して起点作りを通しやすい相手を挙げます。基準は「カバルドンの弱点（みず・くさ・こおり）を一致技で突かず、カバルドンが流し・設置に動ける相手」です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力の10まんボルト（66.9%）はでんき無効で透かせる。じしんがはがね/ドラゴンに×2で刺さり、起点にしつつ削れる。りゅうせいぐん（64.8%）はHD型で受けやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利（HB型）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）はカバルドンに等倍で、HB型なら受けてなまける回復が間に合う。あくび＋ステルスロックで起点化。ただしスケイルショットの連続ヒットで削りを受ける点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ ソーラービームに注意</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技・ひこう技はカバルドンに等倍で耐久受けが利く。ただしソーラービーム（採用率61.0%）はくさ技でカバルドンに×2弱点。晴れ展開からの一撃には居座れない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ゴーストにじしんが×2。みず・くさ・こおり技を持たず、カバルドンの弱点を突けない。あくびで流して起点化できる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ・インファイト（72.4%）ともカバルドンに等倍以下で、みず・くさ・こおり技を持たず弱点を突けない。つるぎのまい（86.6%）の積みはふきとばしで流せる</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

基準は「カバルドンの弱点（みず・くさ・こおり）を一致技で突き、起点作りの前に高い圧力をかけてくる相手」です。いずれもカバルドンの低いとくぼう72ないし弱点×2を起点に崩しに来ます。

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
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（79.2%）・なみのり（16.8%）のみず技が×2弱点。とくこう126の高火力で、HD型でも連打されると押し切られる。あくびはアンコール（40.8%）で逆用される恐れ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず技を半減できるフシギバナや、特性ちょすい/よびみずを持つ枠を同伴し、アシレーヌの前に引いて受ける。あくびはアンコールを警戒し変化技より交代を選ぶ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致トリックフラワー（92.9%）はくさ技で×2弱点、かつ必中・急所必中。S123で先手を取られ、はたきおとし（57.6%）でオボン・たべのこしを奪われ受けが崩れる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ技を半減するアーマーガア・リザードン等を後出しして処理する。持ち物を狙われる前提でたべのこしよりオボンのみで一度の回復を確保する選択もある</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（12位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致たきのぼり（85.9%）が×2弱点。りゅうのまい（73.3%）でAとSを上げられると、なまける回復を上回る火力で押し切られる。いかくでカバルドンのAも下がる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積み前にふきとばしで流してりゅうのまいをリセットする。でんき・いわ技を持つアタッカー（弱点×2）を合わせて上から処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（88.4%）はじめんで等倍だが、ギガドレイン（56.9%）・やどりぎのタネ（58.5%）のくさ技が×2で刺さり、回復しながらカバルドンを枯らしてくる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさを半減するリザードン・アーマーガア・ハッサム等を同伴し、フシギバナに後出しして弱点（ほのお・ひこう・むし）を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">イダイトウ(オス)（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致ウェーブタックル（96.5%）・アクアジェット（91.1%）のみず技が×2弱点。A種族値の高い物理みずアタッカーで、HD型でも一致みず技の連打は受けきれない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず技を半減・無効化できる枠（フシギバナ、特性ちょすい等）を同伴して受け、後出しで処理する</td>
</tr>
</tbody>
</table>
</div>

カバルドン自身はじしん以外に攻撃手段を持たないため、苦手な相手を自力で倒すことは難しいです。上記いずれも「弱点を突く相手の処理役を別途用意し、カバルドンは有利な物理・でんき・はがね方面の受けに専念させる」という役割分担が前提になります。

---

## パーティ構成

### 相性の良いポケモン

カバルドンの同居率上位は、起点作りで整えた盤面を活かす攻撃枠が中心です。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでカバルドンの弱点くさを半減（こおりは等倍）。ちょうはつ持ちの起点作り役と役割分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴースト高速アタッカー。ステルスロック後に弱点を突いて全抜きを狙う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S123の高速くさ/あく。とんぼがえりでカバルドンへ繋ぎ、起点作りと相性が良い</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでカバルドンの弱点くさ・みずを半減（こおりは等倍）。受け回しの相方</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロック後に高火力で全抜きを狙うメガアタッカー。起点作りの受け手</div>
  </div>
</div>

**パーティ構成の基本方針:**

カバルドンは起点作りに特化しているため、残り5体で「整えた盤面を勝ちに変える攻撃役」と「カバルドンの弱点をカバーする受け役」を用意します。

1. **全抜きエース**: ステルスロック＋砂ダメージで確定数を繰り上げた後に通すアタッカー（ルカリオ・イダイトウ等）
2. **みず受け**: アシレーヌ・イダイトウ等のみずアタッカーを止める枠（フシギバナ、特性ちょすい持ち等）
3. **くさ受け**: マスカーニャ・フシギバナのくさ技を半減する枠（アーマーガア・リザードン・ハッサム等）
4. **積みアタッカー流し**: カバルドンのふきとばしと役割が被らないよう、ちょうはつ等でも起点を消せる枠を分担

---

## データ分析①：攻撃技1枠に対する変化技3枠という割り切り

カバルドンの技採用率を見ると、起点作りへの割り切りが数値にはっきり表れています。攻撃技はじしん98.0%の1枠のみで、残りは全て変化技です。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| じしん | 攻撃 | 98.0% | 唯一の打点 |
| あくび | 変化 | 94.2% | 流し（交代強制） |
| ステルスロック | 変化 | 84.4% | 設置（ダメージ蓄積） |
| なまける | 変化 | 53.2% | 回復（居座り） |
| ふきとばし | 変化 | 44.5% | 流し（積みリセット） |

注目すべきは、流し技がふきとばし（44.5%）とあくび（94.2%）で重複採用されている点です。あくびは「交代を誘って起点を作る」攻めの流し、ふきとばしは「積んだ相手を強制交代させてステルスロックを踏ませる」守りの流しと役割が異なり、両採用で積みアタッカーへの対応力を確保しています。一方で4枠目はなまける（53.2%＝居座り重視）とふきとばし（44.5%＝対積み重視）でほぼ二分されており、想定する相手によって「自分が長く残るか／相手の積みを消すか」を選ぶ構築上の分岐点になっています。

攻撃技がじしん1枠に絞られている事実は、カバルドンが「自分で点を取るポケモンではなく、後続が点を取る盤面を作るポケモン」であることをそのまま示しています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主なEV</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">わんぱくHB型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">わんぱく 74.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 B32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理アタッカーを安定受け。ガブリアスのじしんに強い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊技に脆い（アシレーヌ・ブリジュラスの特殊）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">しんちょうHD型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう 16.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">H32 D32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊アタッカーに対応。EVスプレッドは最多採用（24.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理高火力で消耗。ガブリアス等の物理一致技に弱い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

カバルドンはあくび94.2%・ステルスロック84.4%による起点作りと、HP108・ぼうぎょ118の物理耐久、すなおこしによる継続ダメージを兼ね備えた、M-2環境でトップ10入りした受け・サポート役です。攻撃をアタッカー陣に任せ、自分は盤面を整えることに徹する役割分担型のポケモンです。

物理アタッカー・でんきタイプ・はがねタイプに対しては受け出しから起点作りを通せる一方、みず・くさ・こおりを一致技で持つアシレーヌ・マスカーニャ・ギャラドス・フシギバナには弱点を突かれて崩されます。これらの処理役をパーティで明確に用意できるかが、カバルドンを軸にした構築の安定度を左右します。HB型かHD型かは、想定する環境が物理寄りか特殊寄りかで選び分けるのが基本です。

---

## 関連記事

- [起点作りから繋ぐ全抜きエース メガルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [天敵となるみず受けの突破役 ギャラドスのM-2考察](/blog/gyarados-analysis-m2/)
- [同じじめん枠のアタッカー ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
