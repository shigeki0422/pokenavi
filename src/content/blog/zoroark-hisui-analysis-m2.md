---
title: '【ポケモンチャンピオンズ】ゾロアーク（ヒスイ）考察 M-2 使用率39位 イリュージョンと崩しの立ち回り'
description: 'M-2シングルバトルで使用率39位のヒスイゾロアーク（ノーマル/ゴースト）を分析。イリュージョン採用率100%、きあいのタスキ70.4%を活かしたおきみやげ・ちょうはつによる崩し型を解説。S110の先手、こごえるかぜ・シャドーボールの技構成、苦手なあくタイプ対策まで実データで紹介します。'
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
  <img src="/images/pokemon/pokemon-0571-01.webp" alt="ヒスイゾロアーク" />
  <div>
    <h2 style="margin:0 0 8px">ゾロアーク（ヒスイ）</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">39位</strong>　特性: <strong>イリュージョン 100%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ヒスイゾロアークは**使用率39位**を記録。特性は**イリュージョン（採用率100%）**で、控えの一番後ろにいるポケモンの見た目で場に出る、相手を欺くことに特化したポケモンです。

ヒスイゾロアークはノーマル/ゴーストという珍しい複合タイプを持ち、ノーマル・かくとう・ゴーストの3タイプを無効化します。きあいのタスキ（採用率70.4%）で1発耐えてから**おきみやげ・ちょうはつ・トリック**で相手の動きを縛る、崩し役としての運用が中心です。

---

## なぜヒスイゾロアークが採用されるのか

### 1. イリュージョンで初手の択を歪める

特性**イリュージョン**は、手持ちの一番後ろのポケモンの姿・名前で場に出る効果です。相手は見えている「別のポケモン」を基準に技選択・交代を決めるため、想定外のヒスイゾロアークの技を通しやすくなります。例えばバンギラスに化けて出せば、相手はバンギラスのいわ・あく技を警戒して動くため、こちらのきあいだま（かくとう）やかえんほうしゃ（ほのお）が刺さりやすくなります。化けの解除は攻撃を受けた瞬間なので、初手の1ターンを能動的に使える点が他の崩し役にない強みです。

### 2. ノーマル・かくとう・ゴーストを無効化する受け出し性能

ノーマル/ゴーストはノーマル技・かくとう技・ゴースト技をすべて無効化します。環境上位ではルカリオ（使用率9位）のインファイト・しんくうは・バレットパンチ以外のかくとう技、ギルガルド（11位）のかげうち（採用率96.2%）・ポルターガイスト（67.6%）といったゴースト技を透かして場に出せます。弱点が**あく1タイプのみ**と少ないため、化けが解けた後も一定の対面なら居座って崩しを進められます。

### 3. S110で環境上位アタッカーの上を取る

すばやさ種族値は**110**。おくびょう＋すばやさ最大振りですばやさ実数値は約167になり、ガブリアス（S102・使用率1位）・サザンドラ（S98・21位）・リザードン（S100・5位）・ブリジュラス（S85・2位）より速く動けます。こごえるかぜ（採用率61.1%）で相手のすばやさを下げる、ちょうはつ（35.0%）で起点作成を阻止する、おきみやげ（51.2%）で後続の起点を作るといった行動を**先手で**通せます。

ただしマスカーニャ（S123・3位）・ゲッコウガ（S122・28位）には先手を取られ、いずれもあく技（マスカーニャのはたきおとす57.6%）でこちらの弱点を突くため、上から縛ることはできません。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:27.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:62.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">125</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">110</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

とくこう125・すばやさ110の高速特殊アタッカー寄りの配分です。一方でHP55・B60・D60と耐久は全方位に低く、弱点でない技でも上から押されると素受けは難しいため、きあいのタスキで1発耐えてから動く前提の数値です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ゴースト" />
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
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点が**あくの1タイプのみ**で、ノーマル・かくとう・ゴーストの3タイプを無効化するのが最大の特徴です。ノーマル技とゴースト技を同時に透かせる組み合わせは現環境では珍しく、かげうち・ポルターガイストを持つギルガルド（11位）やミミッキュ（19位）のゴースト技、しんそく（ノーマル）などを起点にしやすくなります。一方、弱点のあくを突くマスカーニャ・サザンドラ・ドドゲザン・バンギラスといった上位陣には脆く、これらに崩しの起点を渡さない選出が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こごえるかぜ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">61.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のSを1段階ダウン。ガブリアス・カイリュー等への打点と速度操作を兼ねる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おきみやげ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自身はひんしになるが相手のA・Cを2段階ダウン。後続の起点作成</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">49.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。20%でD1段階ダウン。ゴースト・エスパーへの主打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>うらみつらみ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>46.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。シャドーボールと選択のゴースト特殊技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>41.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・くさ・むしへの打点。ハッサム・キラフロル・ギルガルド対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の変化技を封じる。積み・ステロ・回復の起点阻止</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きあいだま</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中率70。あく・はがね・いわへの大火力。ドドゲザン・バンギラス対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型で採用。受けポケモンに押し付けて機能停止させる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理アタッカーをやけどでAダウンさせ機能停止に追い込む</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40先制</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1のゴースト先制技。A100のため火力は控えめ。タスキ処理用</td>
</tr>
</tbody>
</table>
</div>

特性100%・タイプ一致のメインウェポンであるシャドーボール／うらみつらみより、**こごえるかぜ・おきみやげ**といった補助技の採用率が高いのがこのポケモンの特徴です。純粋な特殊アタッカーではなく、速度操作と能力ダウンで相手の動きを縛る崩し役として運用されていることが採用率に表れています。

---

## 主要型の解説

型①・型②の指標は持ち物分布（きあいのタスキ70.4%／こだわりスカーフ19.4%）を用います。性格はおくびょう75.3%・ひかえめ13.5%でおくびょうが主流です。

### 型1: きあいのタスキ崩し型（最多採用）

**持ち物採用率: きあいのタスキ 70.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0571-01.webp" alt="ヒスイゾロアーク" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ おくびょうCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り。最多型は余りをHBに）<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール / うらみつらみ<br>
・こごえるかぜ<br>
・おきみやげ<br>
・かえんほうしゃ / ちょうはつ
</div>
</div>
</div>

**強み:**

きあいのタスキでどんな高火力でも必ず1発耐え、最低でも**おきみやげ**による相手のA・C2段階ダウン、もしくはちょうはつでの起点阻止という仕事を1つ確実に通せます。イリュージョンで別のポケモンに化けて出れば、相手が誤った技選択・交代をした隙に、こごえるかぜでS操作をしながら殴る／おきみやげで後続の積みの起点を作るといった択を押し付けられます。S110で先手を取れるガブリアス・サザンドラ・ブリジュラスには、行動前にこごえるかぜでSを下げて後続のアタッカーに繋ぐ動きが特に有効です。

**弱み:**

タスキは先制技や定数ダメージで簡単に潰れます。マスカーニャ・ゲッコウガはこちらより速くあく技で弱点を突いてくるため、タスキで耐えても返しで縛りきれません。また、すでにステルスロックやスナアラシなどで削られている状態ではタスキが機能せず、崩しに入る前に落ちます。

---

### 型2: こだわりスカーフ型

**持ち物採用率: こだわりスカーフ 19.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0571-01.webp" alt="ヒスイゾロアーク" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ おくびょうCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り）<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・シャドーボール / うらみつらみ<br>
・かえんほうしゃ<br>
・きあいだま<br>
・トリック / こごえるかぜ
</div>
</div>
</div>

**強み:**

タスキ型がすばやさ実数値約167で止まるのに対し、スカーフで実数値約250相当まで上がり、マスカーニャ（S123）・ゲッコウガ（S122）など素では抜けない高速アタッカーの上を取れます。化けの状態から不意のスカーフ最速で奇襲し、シャドーボールやかえんほうしゃで先に縛る動きが通ります。トリックを採用すれば、行動を縛れない受けポケモンにスカーフを押し付けて変化技を機能停止させられます。

**弱み:**

こだわりで技が固定されるため、タスキ型のおきみやげ・ちょうはつによる柔軟な崩しはできません。崩し技を1回しか選べず、化けが解けた後は実質1回の攻撃で役割を終えやすい、使い切りに近い型です。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ヒスイゾロアークと相性がはっきり出るポケモンを有利・不利の両面から挙げます。弱点はあく1タイプのみですが、HP55・B60・D60と耐久が低く、あく技を持つ相手や先制技持ちにはタスキ込みでも縛りきれない点に注意してください。

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
    <img src="/images/pokemon/pokemon-0681-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド（11位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（96.2%）・ポルターガイスト（67.6%）のゴースト技を無効化。せいなるつるぎ（かくとう）も無効。こちらはかえんほうしゃ（はがね×2）が刺さる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち（93.6%）のゴースト技を無効化、S110＞96で先手。じゃれつく（フェアリー・採用率91.9%）はノーマル/ゴーストに等倍止まり。シャドーボール（ゴースト×2）でばけのかわを剥いでから崩せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃは等倍（はがね2×ドラゴン0.5）だがS110＞85で先手を取れ、あく技を持たないため弱点を突かれず一方的に崩せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分（崩し有効）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S110＞102で先手。こごえるかぜ（こおり×4・ドラゴン2×じめん2）で大きく削りつつS低下、またはおきみやげで起点化できる。ただしA130の高火力で、タスキで耐えた後の2発目では押し負ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分（崩し有効）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・しんくうは・しんそくを無効化し、おきみやげ・おにびで機能停止させやすい。ただしバレットパンチ（はがね・先制）はこちらに等倍で通り、低耐久を削られる</td>
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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちらより速く、はたきおとす（あく×2・採用率57.6%）で弱点を突かれる。とんぼがえり（70.1%）でこちらを見て安全に引かれ、崩しを通させてもらえない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ型なら上を取ってシャドーボールで縛れる。タスキ型ではこごえるかぜでSを下げてから後続のアシレーヌ等みず枠に引いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどう（あく×2・採用率98.5%）で弱点を突かれる。S110＞98で先手は取れるがこちらの一致技ゴースト・補助技では決定力が足りず、撃ち合うと返しで落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいだま（かくとう×2）採用型なら先手で大ダメージを狙える。非採用なら無理せずフェアリー枠（ニンフィア・ピクシー）で後出しして受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（あく・先制・採用率99.0%）でタスキを無視して上から弱点×2を通される。崩し技を撃つ前に縛られやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいだま（かくとう×4）を持てば確定1発を狙えるが命中率70が不安。基本はかくとう・ほのお・じめんの高火力アタッカーを後続に置いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0248-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">バンギラス（同居率1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく×2・採用率75.0%）で弱点を突かれ、すなあらしの定数ダメージでタスキが無効化される。高Dで一致ゴースト技も通りにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいだま（かくとう×4・いわ2×あく2）採用型なら先手で大ダメージ。非採用ならかくとう・むし技を持つアタッカーで弱点を突いて処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト×2・採用率71.1%）で弱点を突かれる。S110同速で運勝負になり、負けると先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ型で確実に上を取り、こちらのシャドーボール（ゴースト×2）で先に縛る。タスキ型なら無理に撃ち合わずあくタイプ等で受ける</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0248-00.webp" alt="バンギラス">
    <div class="name">バンギラス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">化けの偽装役に最適な高耐久枠。すなあらしで相手のタスキを潰し崩しを補助</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア">
    <div class="name">ニンフィア</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">弱点のあくを半減するフェアリー枠。サザンドラ・マスカーニャのあく技を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おきみやげで作った起点から積みやすい高耐久アタッカー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おきみやげのA・Cダウンを押し付けた相手にりゅうのまいから全抜きを狙う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">こちらが苦手なマスカーニャのあく技を受け、りゅうのまいの起点を作れる</div>
  </div>
</div>

**パーティ構成の基本方針:**

ヒスイゾロアークは単体で完結せず、おきみやげ・ちょうはつ・こごえるかぜで作った起点を後続が活かす構成が前提です。残り5体で以下を補います。

1. **起点を活かす積みアタッカー**: ガブリアス・ギャラドス・ブリジュラス等。おきみやげで相手の攻撃力を削いだ隙にりゅうのまい・つるぎのまいを積む
2. **あく弱点の受け**: ニンフィア・ピクシー等フェアリー枠でサザンドラ・マスカーニャのあく技を受ける
3. **偽装役**: バンギラス等の高耐久枠を一番後ろに置き、イリュージョンの化け対象にして初手の択を歪める

---

## データ分析①：メイン技より補助技が優先される崩し役の実態

特性イリュージョン採用率100%・一致技シャドーボール（49.6%）／うらみつらみ（46.5%）という構成だけ見れば特殊アタッカーに見えますが、技の採用率を並べるとこのポケモンの本質が見えてきます。

| 技 | 区分 | 採用率 | 役割 |
|---|---|---|---|
| こごえるかぜ | 攻撃＋S操作 | **61.1%** | 速度操作 |
| おきみやげ | 補助（自主退場） | **51.2%** | 起点作成 |
| シャドーボール | 一致攻撃 | 49.6% | 主打点 |
| うらみつらみ | 一致攻撃 | 46.5% | 主打点 |
| ちょうはつ | 補助 | 35.0% | 起点阻止 |

最採用技が一致打点ではなく、相手のSを下げる**こごえるかぜ**である点が特徴的です。続くおきみやげ（51.2%）は自身がひんしになる代わりに相手のA・Cを2段階下げる自主退場技で、シャドーボール・うらみつらみのどちらの一致技よりも採用率が高くなっています。とくこう125を持ちながら、半数以上の個体が「殴る」より「相手を縛って後続の起点を作る」ことを優先しているわけです。

これは持ち物がきあいのタスキ70.4%に偏っていることと整合します。タスキで1発耐える前提なら、その1ターンを攻撃に使うよりおきみやげ・ちょうはつといった「確実に仕事になる崩し」に充てる方が、低耐久・中火力のヒスイゾロアークの仕事を最大化できる——というのが採用者の選択に表れた合理です。崩し役として選出し、後続の積みアタッカーとセットで運用するのが基本になります。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">きあいのタスキ崩し型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">タスキ 70.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">こごえるかぜ・おきみやげ・シャドーボール・かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">1発耐えて崩しを確実に通す。柔軟な択</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">先制技・定数ダメージでタスキが潰れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こだわりスカーフ型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ 19.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">シャドーボール・かえんほうしゃ・きあいだま・トリック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">高速アタッカーの上を奇襲で取る</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技固定で柔軟な崩しができない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ヒスイゾロアークはノーマル・かくとう・ゴーストの3タイプ無効と弱点あく1タイプという優秀な耐性に、イリュージョンの奇襲性とおきみやげ・ちょうはつ・こごえるかぜの崩しを組み合わせた起点作成役です。ギルガルド・ミミッキュのゴースト先制技を透かして起点にできるのが現環境での明確な強みです。

一方でHP55・B60・D60と耐久は低く、弱点を突くあくタイプ（マスカーニャ・サザンドラ・ドドゲザン・バンギラス）には崩しを通す前に縛られます。タスキで1発耐えてから、おきみやげで後続アタッカーの起点を作る——この一連の動きを成立させる選出ができるかどうかが、使用率39位という尖った性能を活かす鍵になります。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [ゴースト先制技を起点にしやすいゲンガーのM-2考察](/blog/gengar-analysis-m2/)
- [同じヒスイのすがた ヒスイダイケンキのM-2考察](/blog/samurott-hisui-analysis-m2/)
