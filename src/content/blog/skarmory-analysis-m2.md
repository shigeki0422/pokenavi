---
title: 'エアームド考察 M-2 使用率44位 物理受け・ステロ撒きの型別採用率'
description: 'M-2シングルバトルで使用率44位のエアームドを徹底分析。はがね/ひこうでじめん無効・8タイプ耐性を持つ物理受け。メガエアームド(すじがねいり)のつるぎのまい積み型と、がんじょうステロ撒き型の採用率・立ち回り・苦手な相手を実データで解説します。'
updatedDate: '2026-06-11'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-skarmory-m2.png'
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
  <img src="/images/pokemon/pokemon-0227-00.webp" alt="エアームド" />
  <div>
    <h2 style="margin:0 0 8px">エアームド</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">44位</strong>　メガ石採用率: <strong>エアームドナイト 66.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、エアームドは**使用率44位**。はがね/ひこうという複合タイプにより**じめん技を無効化**し、さらに8タイプを半減する屈指の物理受けです。技構成はブレイブバード（採用率67.3%）・つるぎのまい（57.9%）・はねやすめ（56.1%）・ステルスロック（26.7%）・ふきとばし（19.4%）と、起点作りと積みアタッカーの両面を備えています。

注目すべきは**エアームドナイトの採用率66.6%**。メガエアームドは特性が**すじがねいり**（よびみず・サイドチェンジなど技を引き寄せる特性・技を無視して狙った相手に攻撃を通す）に変わり、すばやさ種族値が70→110、こうげき80→140と一気に攻撃寄りへ振れます。素のエアームド（がんじょう／くだけるよろい）が受け、メガが積みアタッカーという二つの顔を使い分けられるのが、この世代のエアームドの軸です。

---

## なぜエアームドが使われるのか

### 1. じめん無効＋8タイプ耐性の物理受け

はがね/ひこうの最大の価値は、環境1位ガブリアスの**じしん（採用率99.2%）を無効化**できる点です。じめんに加え、くさ・むし（各×0.25）、ノーマル・ひこう・エスパー・ドラゴン・はがね・フェアリー（各×0.5）を半減し、どくも無効。ぼうぎょ種族値140（素）と合わせ、物理アタッカーの起点を片端から潰せます。

### 2. はねやすめで居座りながら起点を作る

はねやすめ（採用率56.1%）で最大HPの半分を回復しながら、ステルスロック（26.7%）で交代ダメージを蓄積し、ふきとばし（19.4%）で積みエースを流す——という起点作りが成立します。回復技を持つため、半減タイプの攻撃なら何度も受け出して仕事ができます。

### 3. メガ化でアタッカーへ転身

メガ化でこうげき80→140・すばやさ70→110まで上がるため、つるぎのまい（57.9%）を1積みすればブレイブバードで環境上位の多くを上から叩けます。素のぼうぎょ140で物理を受けてから、終盤に積みアタッカーへ化けられるのが強みです（特性すじがねいりはシングルでは効果がほぼなく、価値は種族値変化にあります）。

---

## 基本スペック

### 種族値（素／メガ後）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">素</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+60</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#2563eb">140</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">110</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+40</td>
</tr>
<tr style="font-weight:700">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="white-space:nowrap">465</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="color:#2563eb;white-space:nowrap">565</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+100</td>
</tr>
</tbody>
</table>
</div>

素のエアームドはぼうぎょ140・はがね/ひこうで物理受けに特化。メガ化でぼうぎょは30下がるものの、こうげき140・すばやさ110・とくぼう100となり、受けから積みアタッカーへ性質が変わります。とくこう40は据え置きのため、技は物理のみで構築します。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="はがね" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ひこう" />
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
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ(×0.25)</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし(×0.25)</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお・でんきの2タイプのみで、いずれも×2。じめん・どくを無効化し、くさ・むしを×0.25まで激減させます。ガブリアスのじしん・マスカーニャのトリックフラワー（くさ）・キラフロルのヘドロウェーブ（どく無効）など、環境上位の主力物理技を軒並み透かせるのが受けとしての強みです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ブレイブバード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致ひこう技のメイン。1/3反動。メガ後の主打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A2段階アップ。積みアタッカー型の核</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの半分回復。受け型の継戦力の核</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドリルライナー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき・はがね・どく・ほのおへの打点。キラフロル（どく複合）に刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致はがね技。フェアリー・いわ・こおりへの安定打点。30%ひるみ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">交代のたびに最大HP比のダメージ。受け型の起点技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の変化技を封じる。受け合い・起点役対策</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の積みを流す。ステロと合わせ交代ダメージを稼ぐ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ボディプレス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ぼうぎょ依存のかくとう技。素の高Bを攻撃に転用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっぺき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">B2段階アップ。ボディプレスと併せた要塞型</td>
</tr>
</tbody>
</table>
</div>

メイン打点はブレイブバード（67.3%）とつるぎのまい（57.9%）。じめん打点のドリルライナー（45.6%）は、ブレイブバードを半減するはがね・いわや、でんき（ハラバリー等）への相補技として機能します。

---

## 主要型の解説

性格分布はようき49.5%・わんぱく22.4%・いじっぱり17.2%。ようきは積みアタッカー型、わんぱくは物理受け型の指標です。

### 型1: つるぎのまい積みAS型（最多採用）

**性格採用率: ようき 49.5%**（AS型の指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0227-00.webp" alt="エアームド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまいメガAS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> くだけるよろい（37.1%）<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り。最多はAS+H）<br>
<strong>持ち物:</strong> エアームドナイト（採用率66.6%）
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・ブレイブバード<br>
・ドリルライナー / アイアンヘッド<br>
・はねやすめ
</div>
</div>
</div>

**強み:**

メガ化でこうげき140・すばやさ110まで上がり、つるぎのまいを1積みすればブレイブバードで環境上位の多くを上から叩けます。はねやすめで居座って積みターンを作れるため、半減タイプ相手なら起点から積み始められるのが、S70止まりの受け型にない長所です。

ドリルライナーはブレイブバードを半減するはがね・いわ（キラフロル等）や、でんきへの相補打点。アイアンヘッドに替えればフェアリー・こおりへ刺さります。

**弱み:**

メガ化でぼうぎょが140→110に下がり、受け性能が落ちます。弱点のほのお・でんきは×2のまま残るため、リザードンやハラバリーなどほのお・でんきアタッカーに対面すると一方的に削られます。とくこう40のため特殊方向の打点が一切なく、ブレイブバードを半減する高耐久のはがね・いわ（ブリジュラス等）には手数で押し負けます。

---

### 型2: がんじょうステロ撒き物理受け型（2番目に多い構成）

**性格採用率: わんぱく 22.4%**（HB物理受けの指標。ようきに次ぐ2番手）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0227-00.webp" alt="エアームド" style="width:48px;height:48px">
  <strong style="font-size:1.05em">がんじょうHB受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> がんじょう（61.9%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）<br>
<strong>EV:</strong> H32 B32（HB振り）<br>
<strong>持ち物:</strong> オボンのみ(13.2%) / たべのこし(10.4%)
</div>
<div>
<strong>技構成:</strong><br>
・ステルスロック<br>
・はねやすめ<br>
・ふきとばし / ちょうはつ<br>
・ボディプレス / ブレイブバード
</div>
</div>
</div>

**強み:**

メガを別枠に回し、素のぼうぎょ140で物理アタッカーを受け止める型です。特性**がんじょう**（採用率61.9%）はHP満タンなら一撃必殺技や高火力の一撃を必ず1残して耐えるため、不意の致命打にも崩れにくいのが利点です。ステルスロック（26.7%）で交代ダメージを撒き、ふきとばし（19.4%）で相手の積みを流して再びステロダメージを与えられます。はねやすめで延々と居座れるため、ガブリアスのじしんやマスカーニャのトリックフラワーといった物理主体の相手に対し起点を作り続けられます。ボディプレスは素の高いぼうぎょをそのまま火力に変換できるため、HB受け型でも有効打を持てます。

**弱み:**

とくこう40のため攻撃面はボディプレスかブレイブバード頼みで、ほのお・でんきの特殊アタッカー（リザードン・ハラバリー等）には弱点を突かれて受けが成立しません。AS型と違い高速性能がないため、変化技で起点にされやすく、ちょうはつ持ちには起点作りを止められます。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、エアームドと相性がはっきり出るポケモンを有利・不利の両面から挙げます。じめん無効・8タイプ半減で物理を受けつつ、ほのお・でんきの2弱点が×2で通る点が相性の分かれ目です。相性はメガ前（受け）／メガ後（S110アタッカー）の両面を踏まえて判断しています。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力じしん（採用率99.2%）が無効。げきりん（47.9%）も×0.5。受け出して起点化でき、ドリルライナーで等倍を返せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力トリックフラワー（くさ・92.9%）が×0.25、トリプルアクセル（こおり・72.2%）も等倍止まり。受け出してブレイブバードで反撃できる（かみなりパンチ21.8%採用個体には×2を通される）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・66.9%）がこちらに×2で通る。こちらの一致技は両方半減（ブレイブバード×0.5・アイアンヘッド×0.5）され、削り合いで一方的に不利</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル（15位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・69.4%）無効、だいちのちから（66.8%）も無効。ドリルライナー（いわ/どくに×2）で弱点を突ける。ただしパワージェム（いわ・85.3%）は等倍で通る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.4%）・フレアドライブ（33.3%）がこちらに×2。受けが成立せず、ブレイブバードは等倍止まりで撃ち負ける（後述）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0939-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハラバリー（32位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パラボラチャージ（でんき・98.9%）がこちらに×2。なまける（83.0%）で粘られ、受けあいでも崩しきれない（後述）</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

弱点はほのお・でんきの2タイプ。これらを×2で通す相手と、こちらの一致技を半減して落としきれない高耐久が主な苦手です。

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
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技がこちらに×2。こちらの打点はブレイブバード等倍・アイアンヘッド半減（はがね0.5）で、ほのお/ひこうを一撃で落とせず撃ち合いで負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・でんき・みずタイプ（キラフロル等のいわ枠）を同伴し、リザードンに後出しして弱点を突く</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのまい（79.7%）がこちらに×2。ブレイブバードはむし/ほのおに×2で入るが、ちょうのまい（97.4%）でC・D・Sを積まれると受け型では撃ち負け、あさのひざし（64.4%）で粘られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・でんき・みずタイプで弱点を突く。積む前にちょうはつで補助技を封じる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0939-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハラバリー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パラボラチャージ（98.9%）が×2。なまける（83.0%）で回復され、こちらの打点も乏しく崩せない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめんタイプ（ガブリアス等）を同伴しでんき技を透かして返す。ちょうはつでなまける・どくどくを封じる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・66.9%）が×2で通る一方、こちらの一致技は両方半減され決定打がない。受け合いでも一方的に削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめんタイプ（ガブリアス等）を同伴しでんき技を透かして後出し。ドリルライナー（はがねに×2）採用個体なら自分でも削れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）・ボルトチェンジ（88.7%）のでんき技が×2。おにび（80.6%）でこうげきを下げられ、メガAS型の火力も殺される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じめんタイプを同伴しでんき技を無効化。ちょうはつでおにび・いたみわけを封じてから殴る</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0547-00.webp" alt="エルフーン">
    <div class="name">エルフーン</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">おいかぜ・コットンガードで補助。エアームドの遅さ（メガ前）を速度面で支える</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0473-00.webp" alt="マンムー">
    <div class="name">マンムー</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">こおり/じめんでドラゴン・でんき枠に打点。エアームドが透かすじめん技の撃ち手</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速じめん枠。エアームドが苦手なでんき技を無効化して受け返せる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリーでエアームドの弱点ほのおを半減。リザードン等に後出しできる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめんでんき受け＋ステロ。ハラバリー・ロトムのでんき技を透かす</div>
  </div>
</div>

**パーティ構成の基本方針:**

エアームドの弱点はほのお・でんきの2タイプに集約されるため、残り5体でこの2タイプの処理役を用意するのが基本です。

1. **でんき対策**: じめんタイプ（ガブリアス・カバルドン）でハラバリー・ロトムのでんき技を無効化
2. **ほのお対策**: みずタイプ（アシレーヌ）でリザードン・ウルガモスに後出し
3. **積みエースの確保**: ステロ撒き受け型のエアームドが起点を作り、後続の積みアタッカーに繋ぐ
4. **速度補助**: エルフーンのおいかぜで素のエアームド（S70）の遅さを補う

---

## データ分析①：エアームドの本体はメガ化アタッカーか受けか

エアームドの技採用率を見ると、攻撃技と補助技が混在しています。これを性格分布と突き合わせると、二つの異なる型が見えてきます。

| 指標 | 数値 | 紐づく型 |
|---|---|---|
| ようき（S↑） | 49.5% | メガAS積みアタッカー |
| わんぱく＋いじっぱり（B↑/A↑） | 39.6% | がんじょう受け／物理寄り |
| つるぎのまい | 57.9% | 積みアタッカー |
| ステルスロック | 26.7% | 受け・起点 |
| エアームドナイト | 66.6% | メガ前提 |

**最多はようき49.5%の積みアタッカー型**で、つるぎのまい57.9%・ブレイブバード67.3%という攻撃技の高さと整合します。エアームドナイト66.6%が示す通り、半数以上の個体がメガ化を前提にこうげき140・すばやさ110のアタッカーとして運用されています。

一方でわんぱく＋いじっぱりが約40%を占め、ステルスロック26.7%・ふきとばし19.4%・てっぺき13.2%といった起点・要塞系の技がこの層を支えています。「受けポケモン」という従来の印象に反し、**M-2のエアームドは積みアタッカーが主流**であり、相手は素のぼうぎょ140だけを警戒していると、メガ化後のブレイブバードで上から崩される——という二段構えが採用率に表れています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">つるぎのまいメガAS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ようき 49.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">つるぎのまい・ブレイブバード・ドリルライナー・はねやすめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S110＋A140で積み後に上から制圧</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">メガ後B低下。ほのお・でんき×2が残る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">がんじょうHB受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく 22.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ステルスロック・はねやすめ・ふきとばし・ボディプレス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B140で物理完封。ステロ＋ふきとばしで起点量産</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊耐久が薄い。ほのお・でんき特殊で受け崩壊</td>
</tr>
</tbody>
</table>
</div>

**総評:**

エアームドははがね/ひこうでじめん・どくを無効化し、8タイプを半減する優秀な物理受けです。M-2ではエアームドナイト採用率66.6%・ようき49.5%が示す通り、素のぼうぎょ140で物理を受けてからメガ化（すじがねいり）でこうげき140・すばやさ110の積みアタッカーに転身する運用が主流になっています。

弱点はほのお・でんきの2タイプに集約されるため、対策役（じめん・みず・いわ枠）を後ろに置けばパーティとして穴を塞ぎやすいのも採用しやすさにつながっています。ガブリアス・マスカーニャといった環境上位の物理エースを起点化できる一方、リザードン・ハラバリー・ウルガモスなどほのお・でんき軸には受けが成立しないため、苦手枠の処理役をセットで組むのが構築の前提です。

---

## 関連記事

- [エアームドが苦手なほのお枠 リザードン(Y)のM-2考察](/blog/charizard-y-analysis-m2/)
- [同じはがね/ひこうの物理受け アーマーガアのM-2考察](/blog/corviknight-analysis-m2/)
- [起点化できる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
