---
title: '【ポケモンチャンピオンズ】ギルガルド考察 M-2 使用率11位 バトルスイッチの両刀型と立ち回り'
description: 'M-2シングルバトルで使用率11位のギルガルドを徹底分析。バトルスイッチでシールド/ブレードを切り替える両刀型、かげうち96%・キングシールド84%の技構成、たべのこし採用率59%、HA物理型のEV配分と環境上位への相性を実データで解説します。'
pubDate: '2026-06-04'
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
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" />
  <div>
    <h2 style="margin:0 0 8px">ギルガルド</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">11位</strong>　特性: <strong>バトルスイッチ 100%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ギルガルドは**使用率11位**を記録。特性は**バトルスイッチが100%**で、攻撃技を使うとブレードフォルム（こうげき140・とくこう140）に、まもる系（キングシールド）を使うとシールドフォルム（ぼうぎょ140・とくぼう140）に切り替わります。

この特性により、ギルガルドは「攻めるときは超火力アタッカー、守るときは超耐久」という1体で2役をこなすポケモンです。攻撃時はかげうち（採用率96.2%）の先制技で詰め、キングシールド（84.2%）で受けに回るという独自の立ち回りが最大の特徴です。

---

## なぜ今ギルガルドが強いのか

### 1. バトルスイッチでブレード時はこうげき・とくこう140の高火力

ギルガルドの基本姿はシールドフォルム（こうげき50・とくこう50・ぼうぎょ140・とくぼう140）ですが、攻撃技を選択した瞬間にブレードフォルム（こうげき140・とくこう140・ぼうぎょ50・とくぼう50）へ切り替わり、その技を高火力で放ちます。攻撃種族値が50→140に跳ね上がるため、両刀の攻撃力は環境トップクラスです。

主力のポルターガイスト（採用率67.6%・威力110のゴースト物理技）はタイプ一致補正が乗り、ブレードのこうげき140から繰り出されます。ゴースト技はゴースト・エスパーに×2で通り、環境上位のゲンガー（10位）・ミミッキュ（19位）・スターミー（20位）・マフォクシー（25位）に刺さります。

### 2. かげうちの先制技で低速の不利を補える

ギルガルドのすばやさはシールド・ブレードとも種族値60と低く、環境上位の多くに後手を踏みます。これを補うのが**かげうち**（採用率96.2%・優先度+1のゴースト先制技）です。先制技は優先度で動くため、**相手のすばやさに関わらず先制**でき、高速アタッカーに削られた相手や、きあいのタスキで耐えた相手をブレードのこうげき140で先に倒せます。

採用率96.2%とほぼ全個体が搭載しており、低速ながら詰め性能を持つのがギルガルドの強みです。

### 3. キングシールドで受けと能力低下を両立

**キングシールド**（採用率84.2%）はまもると同様にそのターンの攻撃を防ぎつつ、ギルガルドをシールドフォルム（ぼうぎょ140・とくぼう140）に戻します。さらに、防いだ相手が接触技を使っていた場合は相手のこうげきを2段階下げる追加効果があります。

つるぎのまい（38.0%）で攻撃を積んだ後、キングシールドでシールドに戻って高耐久で耐える、という攻守の切り替えが1体で完結します。接触物理アタッカー（ガブリアス・カイリュー・ルカリオ等）に対しては、キングシールドでこうげきを2段階下げて起点化できます。

---

## 基本スペック

### 種族値（シールドフォルム / ブレードフォルム）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">シールド</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">ブレード</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">140</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#2563eb">140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">140</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#2563eb">140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
</tr>
<tr style="font-weight:700">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb">520</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb">520</td>
</tr>
</tbody>
</table>
</div>

ブレードでは攻撃面が140/140と高いがぼうぎょ・とくぼうが50に下がり、シールドでは逆に防御面が140/140になります。攻撃技を撃ったターンの終了後もブレードのままになるため、**攻撃後の被弾はぼうぎょ50・とくぼう50で受ける**ことになり、相手の高火力技で落とされやすい点が立ち回り上の最大の注意点です。キングシールドで守りながらシールドに戻すタイミングが勝敗を分けます。

すばやさ種族値60はガブリアス（S102）・リザードン（S100）など環境上位の多くに先手を取られるため、かげうちの先制技と高耐久で受ける運用が前提になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ゴースト" />
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
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし(0.25)</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

はがね/ゴーストはノーマル・かくとう・どくを無効化し、9タイプを半減（むしは×0.25）する優秀な耐性を持ちます。特に**かくとうを無効化**できる点は、環境のかくとう技（ルカリオのインファイト、ハッサムのインファイト等）を完全に受けられることを意味し、防御面でのギルガルドの価値を支えています。シールドフォルムのぼうぎょ140・とくぼう140と組み合わせると、半減・無効タイプの攻撃はほとんど通りません。

ただし弱点のほのお・じめん・あく・ゴーストは×2で通り、これらの技を持つ相手には注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40 先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手のSに関わらず先制。低速の不利を補う詰め技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>キングシールド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃を防ぎシールドに変化。接触技なら相手のAを2段階ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ポルターガイスト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>67.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト物理メインウェポン。相手が道具を持つ時のみ成功</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>38.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A2段階アップ。物理型の積み技。シールドのまま積める</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>せいなるつるぎ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の能力変化を無視。あく・はがね・ノーマルへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タイプ一致はがね物理技。フェアリー・いわ・こおりへの打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊ゴースト技。とくこう型のメインウェポン。D1段階ダウン10%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高威力かくとう技。使用後BとDが1段階ダウン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊はがね技。とくこう型でフェアリー・いわ・こおりへの打点</td>
</tr>
</tbody>
</table>
</div>

ポルターガイストは相手が道具を持っていないと失敗するため、道具のない相手には別の打点が必要です。せいなるつるぎ（採用率31.7%）はギルガルドが等倍以下しか取れないあく・はがねへの打点として機能し、相手の積み（つるぎのまい・りゅうのまい等）を無視してダメージを与えられます。

---

## 主要型の解説

物理型・特殊型の区分は性格分布（いじっぱり／ひかえめ・トリックルーム下のゆうかん等）と攻撃技の採用率を指標としています。

### 型1: つるぎのまい物理型（最多採用）

**性格採用率: いじっぱり 57.1%**（A↑ C↓。物理型の指標で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい物理いじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32 + b/d（最多はHA + BD微調整、採用率13.1%）<br>
<strong>持ち物:</strong> たべのこし / のろいのおふだ
</div>
<div>
<strong>技構成:</strong><br>
・ポルターガイスト<br>
・かげうち<br>
・キングシールド<br>
・つるぎのまい / せいなるつるぎ
</div>
</div>
</div>

**強み:**

EVはHA振り（H32 A32）が主流で、HP・こうげきに厚く振ることでブレード時の火力とシールド時の耐久の両立を狙います。つるぎのまいをシールドフォルムのまま積めるため、ぼうぎょ140・とくぼう140の高耐久で耐えながらこうげきを2段階上げ、次のターンにブレードのこうげき140＋積み2段階でポルターガイストを叩き込めます。

かげうちが先制技として詰めを担うため、低速でも積み後の全抜きを狙いやすいのが特徴です。せいなるつるぎを採用すると、ポルターガイストが半減・無効になるあく・はがね（ドドゲザン・ハッサム等）にも打点を持てます。

**弱み:**

積みターンを通すには相手の弱点技（ほのお・じめん・あく・ゴースト）を耐える必要があり、これらの高火力技を持つ相手には積みを許してもらえません。また、攻撃技を撃った後はブレードのぼうぎょ50・とくぼう50になるため、後続の高速アタッカーから弱点技を受けると一気に崩されます。

---

### 型2: とくこう特殊型

**性格採用率: ひかえめ 1.3%（れいせい10.2%等トリックルーム下の鈍足補正含む）**（C↑。物理型に次ぐ少数派）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">とくこう特殊型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32 C32 + a（HC型、採用率3.2%）<br>
<strong>持ち物:</strong> たべのこし / のろいのおふだ
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール<br>
・ラスターカノン<br>
・かげうち<br>
・キングシールド
</div>
</div>
</div>

**強み:**

シャドーボールはポルターガイストと違い相手の道具に依存せず、どの相手にも安定して撃てるのが物理型との差です。ラスターカノンを加えることで、ゴーストを半減するはがね（ブリジュラス・ドドゲザン等）にもはがね打点を通せます。物理受け（カバルドン等の高ぼうぎょ枠）に対しては特殊技の方がダメージが通るため、物理型の苦手枠を崩せます。

**弱み:**

物理型のポルターガイスト（威力110）に対し、シャドーボール（威力80）は単発火力が低く、つるぎのまいによる積みの爆発力も持ちません。かげうちは物理技のためブレードのこうげき140を使いますが、特殊型ではこうげきに振らない分、先制技の打点は物理型より低くなります。採用率も性格・EV分布から物理型が大多数で、特殊型は少数です。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位（TOP30目安）のうち、ギルガルドと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ギルガルドはすばやさ種族値60と低く環境上位の多くに後手を踏むため、かげうちの先制技とシールドフォルムの高耐久を前提に評価しています。相手の主力技は採用率を確認したものです。

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
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ポルターガイスト／かげうちがゴースト×2で刺さる。ゲンガーの主力ヘドロウェーブ（82%）はどく無効、シャドーボール（71%）はゴースト×2だがかげうちで先制を取れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力トリックフラワー（くさ）はこちらに等倍だが、はたきおとす（採用率57.6%）はあく×2弱点でたべのこし等の道具も奪われる。S123で先手を取られる点も重い。キングシールドで接触技のAを下げられるが過信は禁物</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エスパー技はこちらにはがね0.5で半減、みず技も等倍。こちらのゴースト技はエスパーに×2。シールドの高耐久で受けつつ反撃できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率72%）はかくとう無効、コメットパンチ／バレットパンチもはがね0.5で半減。シールドの高耐久でほぼ受けきり、せいなるつるぎ／アイアンヘッドで反撃</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン技は半減、接触物理にはキングシールドでAを下げて対応可。ただしじしん・ほのお技（フレアドライブ等）を持つ個体には弱点を突かれるため型次第</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99%）がじめん×2弱点。S102で先手を取られ、ブレード時のぼうぎょ50では受けきれない。詳細は下表で扱う</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

ギルガルドの弱点（ほのお・じめん・あく・ゴースト）を主力技で突き、かつ高速・高火力で攻撃後のブレード（ぼうぎょ50・とくぼう50）を崩せる相手を、使用率上位から挙げます。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99%）がじめん×2弱点。S102で先手を取られ、ブレードのぼうぎょ50では確定で落ちる。シールド時でもじしんは重い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこうタイプ（アーマーガア等）や、ガブリアスに弱点を突けるこおり・ドラゴン・フェアリータイプを同伴し、ガブリアスの前に引いて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42%）・オーバーヒート（27%）・フレアドライブ（33%）などほのお技がほのお×2弱点。S100で先手を取られ、こちらのはがね技も両形態に半減で打点が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ・でんきタイプを同伴し、リザードンに後出しして弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（採用率99%）があく×2弱点、かえんほうしゃ（67%）はほのお×2弱点。S98で先手を取られ、ブレード時に上から弱点技で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリータイプ（アシレーヌ等）やかくとうタイプを同伴し、サザンドラの弱点を突いて後続から処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0937-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ソウブレイズ（26位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ゴーストでほのお技・ゴースト技ともこちらに×2。かげうちのゴースト先制もこちらにゴースト×2で刺さり、低速の撃ち合いで不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわタイプでほのお技を受けつつ弱点を突く。あくタイプでゴースト技を無効化して後出しする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（採用率99%）・ドゲザン（96%）のあく技があく×2弱点。こちらのゴースト技はあく無効、はがね技も半減で打点が乏しい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">せいなるつるぎ（かくとう×2）を採用した個体なら反撃可。かくとう・じめんタイプを同伴して弱点を突く</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">S110の高速特殊枠。低速のギルガルドが取りこぼす相手に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ひこうでギルガルドの弱点じめんを無効、ほのおも半減</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。ステロ展開でギルガルドの詰めをサポート</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーでほのお・あくを半減し弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">砂嵐+ステロでダメージ蓄積。ギルガルドの詰めを後押し</div>
  </div>
</div>

**パーティ構成の基本方針:**

ギルガルドは低速で弱点のほのお・じめん・あくを突く相手が多いため、残り5体で以下の役割を補います。

1. **じめん対策**: ひこうタイプ（ギャラドス等）でガブリアスのじしんを無効化する枠
2. **ほのお・あく対策**: みず・フェアリータイプ（アシレーヌ等）でリザードン・サザンドラの弱点技を受ける枠
3. **高速アタッカー**: ゲンガー等でギルガルドが後手で取りこぼす高速勢に上から打点
4. **ステルスロック展開**: ガブリアス・カバルドン等でステロを撒き、かげうちの先制圏を広げる

---

## データ分析①：たべのこし59%とのろいのおふだ29%が示す立ち回りの二極化

ギルガルドの持ち物は**たべのこし59.1%・のろいのおふだ29.0%**で、この2つで約88%を占めます。きあいのタスキ（4.9%）やオボンのみ（2.3%）は少数で、ギルガルドの運用が大きく2つに分かれていることを示します。

| 持ち物 | 採用率 | 狙い |
|---|---|---|
| たべのこし | 59.1% | 毎ターンHP1/16回復。シールドの高耐久で居座り、つるぎのまい積み・キングシールド受けを継続する持久型 |
| のろいのおふだ | 29.0% | ゴースト技の威力を1.2倍に底上げ。ポルターガイスト・かげうち・シャドーボールの瞬間火力を上げる速攻型 |

たべのこしはシールドフォルム（ぼうぎょ140・とくぼう140）の耐久を活かして長く居座る型で、キングシールドで攻撃を防ぎながら回復し、つるぎのまいを積む立ち回りと噛み合います。一方のろいのおふだは、採用率96.2%のかげうちと67.6%のポルターガイストというギルガルドの主力がどちらもゴースト技である点を活かし、先制技の打点を底上げして低速でも詰めきる速攻寄りの選択です。

持ち物だけで「居座って積む型か、ゴースト火力で押す型か」がある程度読めるため、対戦相手としてはギルガルドの持ち物を観察することで立ち回りを予測しやすくなります。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">つるぎのまい物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 57.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ポルターガイスト・かげうち・キングシールド・つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">シールドで耐えて積み、ブレードで全抜き。先制かげうちで詰め</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積みターンが必要。攻撃後はぼうぎょ50で脆い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう特殊型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ 1.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">シャドーボール・ラスターカノン・かげうち・キングシールド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">道具非依存で安定。物理受けを特殊で崩せる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">単発火力・積み爆発力が物理型より低い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ギルガルドはバトルスイッチによる「攻めはこうげき・とくこう140、守りはぼうぎょ・とくぼう140」という1体2役と、ノーマル・かくとう・どくを無効化する優秀な耐性を両立したポケモンです。すばやさ60と低い弱点を、採用率96.2%のかげうちの先制技と高耐久で補い、使用率11位を維持しています。

立ち回りの鍵は、攻撃技を撃った後のブレード（ぼうぎょ50・とくぼう50）で被弾しないよう、キングシールドでシールドに戻すタイミングです。弱点のじめん・ほのお・あくを突くガブリアス・リザードン・サザンドラはパーティ構成でケアし、かくとうやエスパー、ゴースト技持ちなど受けやすい相手に対してシールドの高耐久で起点を作るのが基本戦術となります。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同居率1位の高速ゴースト ゲンガーのM-2考察](/blog/gengar-analysis-m2/)
- [同じはがねアタッカー ハッサムのM-2考察](/blog/scizor-analysis-m2/)
