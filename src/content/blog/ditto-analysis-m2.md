---
title: '【ポケモンチャンピオンズ】メタモン考察 M-2 使用率66位 へんしんコピーの立ち回り'
description: 'M-2シングルバトルで使用率66位のメタモンを徹底分析。特性かわりもの（採用率99.1%）で相手をそのままコピーする特殊なポケモンで、こだわりスカーフ82.3%でコピー後に上を取る運用が主流。種族値オール48・ノーマル単のへんしん前の弱点と、積んだエースを打ち返す立ち回りを実データで解説します。'
pubDate: '2026-06-11'
draft: true
heroImage: '../../assets/hero-ditto-m2.png'
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
  <img src="/images/pokemon/pokemon-0132-00.webp" alt="メタモン" />
  <div>
    <h2 style="margin:0 0 8px">メタモン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">66位</strong>　特性: <strong>かわりもの 99.1%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、メタモンは**使用率66位**を記録。特性は**かわりもの（採用率99.1%）**がほぼ全てで、じゅうなん（0.9%）は誤差です。

メタモンは、通常のアタッカーや耐久型とは構成の考え方が根本から異なる特殊なポケモンです。**かわりもの**は「場に出た瞬間、目の前の相手に変身する」特性で、変身後はHP以外の種族値・能力ランク・技・タイプを相手と同じにします。つまりメタモン自身に攻撃範囲や耐久を求めるのではなく、**相手のエースをそっくりコピーして、そのまま打ち返す**ことが唯一の役割です。持ち物は**こだわりスカーフ 82.3%**が大半を占め、コピーした相手と同じ種族値になった上でスカーフ補正で上を取る運用が標準化しています。

---

## なぜメタモンが使われるのか

### 1. かわりもので相手のエースをそのままコピーする

メタモンの軸は、繰り出した瞬間に発動する特性**かわりもの（99.1%）**です。目の前の相手の種族値（HPを除く）・タイプ・特性・覚えている技・そのときの能力ランクを丸ごとコピーするため、相手が積み技で強化したエースであっても、**積んだ後の能力ランクごと写し取って同じ土俵で殴り返せます**。

通常のアタッカーは「自分の種族値・技で何ができるか」で評価しますが、メタモンは**相手依存**です。相手が強ければ強いほどメタモンも強くなり、環境のエースに対する万能の切り返し役として採用されます。

### 2. こだわりスカーフでコピー後に上を取る

持ち物は**こだわりスカーフ 82.3%**が支配的です。変身でコピーすると相手と同じすばやさ種族値になるため、素のままでは同速で運によるじゃんけんになります。そこにスカーフ補正（×1.5）が乗ることで、**コピー元の相手より確実に先手を取れる**ようになります。

例えばつるぎのまいを積んだガブリアス（使用率1位）に後出しすれば、+2のこうげきランクごとコピーし、スカーフでガブリアスより速く、ガブリアスの技でガブリアスを倒し返せます。「相手の積みエースを、その積み状態のまま追い抜いて処理する」のが最大の採用理由です。

### 3. 変身前に耐えるための耐久振り

メタモンの素の種族値はHP以外すべて48と極端に低く、変身する前に先制技や高速アタッカーで縛られると、コピーする間もなく落ちてしまいます。これを避けるため、EVはHP・ぼうぎょ・とくぼうに振って**変身前に相手の一撃を1回耐える**構成が主流です。耐えてしまえば次の行動でコピーが間に合うため、耐久振りは「変身する隙を作る」ための投資になります。

---

## 基本スペック

### 種族値（へんしん前）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">48</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">288</span>
  </div>
</div>

種族値はHPを含めオール48で、合計288は環境最低クラスです。ただしこの数値は**へんしん前のメタモン自身の値**であり、変身後は相手の種族値（HP以外）に置き換わるため、攻撃・耐久の実質性能は完全に相手依存になります。

唯一コピーされず最後まで自分の値を使うのが**HP**です。H32振りで**HP実数値155**（無振りで123）まで上げられ、これが「変身前に1回耐える」ための数少ない自前のステータスになります。変身後も相手のHPにはならず、このHP実数値155のまま戦う点が、コピー先のエース本体との大きな違いです。

### タイプ・弱点（へんしん前）

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span style="color:#94a3b8">なし</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト
  </td>
</tr>
</tbody>
</table>
</div>

この相性はあくまで**へんしん前のノーマル単**のものです。実戦ではメタモンは場に出た瞬間に変身し、以降は**コピーした相手のタイプ相性**で殴り合うため、この表の弱点・無効が問題になるのは「変身が間に合わなかった例外的な場面」に限られます。なお変身前であってもゴースト技は無効化できるため、初手でゴースト技を撃たれても被弾せずに変身を通せます。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>へんしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">100.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">目の前の相手に変身し、HP以外の能力・技・タイプをコピーする</td>
</tr>
</tbody>
</table>
</div>

メタモンが覚える技は**へんしん（採用率100%）**の1つだけです。特性かわりもので場に出た時点ですでに変身が済んでいるため、メタモン自身が技として何かを撃つことはなく、変身後は**コピーした相手の技**で戦います。技構成は実質固定で、相手によって戦い方が決まるのがメタモンの最大の特殊性です。

---

## 主要型の解説

持ち物分布（こだわりスカーフ 82.3%／きあいのタスキ 7.6%／せんせいのツメ 6.6%）が型の指標です。技は全型でへんしんに固定されるため、型の差は**持ち物と耐久の振り方**だけで生まれます。性格は能力に影響しないまじめ等を含め分散しますが、上位はのんき（20.5%）・なまいき（17.7%）と**すばやさを下げて耐久に寄せる補正**が選ばれます。これは変身後にスカーフで上を取る前提なら、自分のすばやさを下げてでも変身前の耐久を確保するほうが安定するためです。

### 型1: こだわりスカーフ型（最多）

**指標: こだわりスカーフ 82.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0132-00.webp" alt="メタモン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">スカーフ変身型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かわりもの（99.1%）<br>
<strong>性格:</strong> のんき（S↓ B↑）など能力低下が小さい補正<br>
<strong>EV:</strong> H32 B32（HB耐久。HA+a・HD+b等の派生あり）<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・へんしん<br>
<span style="color:#888">（変身後はコピーした相手の技を使用）</span>
</div>
</div>
</div>

**強み:**

変身でコピーすると相手と同じすばやさになりますが、スカーフ補正（×1.5）が乗ることでコピー元より確実に先手を取れます。積み技を使ったエースをその積みランクごとコピーし、相手の技で相手を上から倒し返せるのがこの型の核です。HB耐久（H32 B32）で物理エースの一撃を耐えてから変身する想定が多く、HP実数値155を活かして1回行動を保証します。

**弱み:**

スカーフで技が固定されるため、変身後は最初に選んだ技を撃ち続けます。コピー元が技を撃ち分けて対応する相手（半減・無効で透かしてくる受け）には、固定された1技では押し切れません。また、相手がメタモンの変身前に交代すると、交代先にとって不利なエースをコピーしてしまう読み合いも発生します。

---

### 補足: きあいのタスキ型（7.6%）／せんせいのツメ型（6.6%）

きあいのタスキ型は、変身前にHP満タンから先制技や高速アタッカーの一撃を受けても1回耐え、確実に変身を通すことを狙います。スカーフのように先手を保証できない代わりに、変身前に縛られて落ちる事故を防ぐ構成です。せんせいのツメ型は20%で先制を取れる持ち物で、同速になりがちな変身後に運で上を取りにいく選択肢ですが、確率依存のためスカーフほど安定しません。いずれも採用率は1割未満で、こだわりスカーフが標準です。

---

## 環境ポケモンへの相性分析

メタモンの相性は「相手をコピーして打ち返せるか」で決まり、通常のタイプ相性とは判断軸が異なります。**積み技で自己強化したエース**には強く、**変身前に縛られる相手**や**コピーしても打開できない受け**には弱い、という整理になります。

### 有利・不利が出る主要ポケモン

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまいを積んだ後出しに、+2のこうげきランクごとコピー。スカーフでガブリアスを上から抜き、相手の技でそのまま落とし返せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうのまいを積んだ後にコピーすれば、上がったランクごと写し取りスカーフで先手。しんそく等の先制技もコピーして撃ち返せる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ea580c;font-weight:bold">△ 高耐久で押し切れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">コピーしても自分のHPは155止まりで相手の高耐久HPにはならず、ミラーでは火力よりHP差で不利。決定打を入れにくく長期戦になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 先制で変身前に縛られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ（先制）でHP155を削られ、変身前に2発で落とされやすい。スカーフで上を取る前に潰される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 持ち物を叩き落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（採用率上位）でこだわりスカーフを落とされると、変身しても同速になり先手保証が消える。先制のトリックフラワーで変身前も削られる</td>
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
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチの先制でHP155を変身前に削られ、コピーが間に合わず縛られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積んでいないハッサムには変身させず、ほのお枠（リザードン等）で先に処理してからメタモンを通す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとすでこだわりスカーフを落とされ、変身しても同速止まりで先手を保証できなくなる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフを残したい相手には変身させず、高速のひこう・ほのお枠を先に当ててマスカーニャを削ってから出す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高耐久ミラーになり、自分のHP155は相手のHPに及ばず削り合いで先に落ちる。決定打を入れにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">コピーで打ち合わず、かくとう枠（ルカリオのインファイト等）ではがね弱点を突いて処理する</td>
</tr>
</tbody>
</table>
</div>

メタモンが苦手なのは「**変身前に先制技や高速アタッカーで縛られる相手**」と「**コピーしても打開できない高耐久・受け**」、そして「**こだわりスカーフを叩き落として先手保証を奪う相手**」です。いずれもメタモン単体では解決できないため、これらを別のポケモンで処理し、メタモンは「積んだエースを打ち返す」役割に専念させる構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0214-00.webp" alt="ヘラクロス">
    <div class="name">ヘラクロス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">むし/かくとうのアタッカー。積みエースを通す盤面を作り、メタモンの切り返しと噛み合う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0184-00.webp" alt="マリルリ">
    <div class="name">マリルリ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はらだいこで自己強化する積みエース。抜き性能を持ちメタモンの後詰めと相性が良い</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">使用率1位の高速エース。先に攻めて相手の択を絞り、通らなければメタモンで切り返す</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンの高耐久。メタモンが苦手な受け合いを引き受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのおでメタモンが縛られるハッサムを処理。積み展開も狙える</div>
  </div>
</div>

**パーティ構成の基本方針:**

メタモンは単体で完結せず、「相手の積みエースを打ち返す保険」として後ろに置くのが基本です。残り5体で以下を補います。

1. **先制技ケア**: ハッサムのバレットパンチ等でメタモンが変身前に縛られるため、これを先に処理できるほのお・ひこう枠を置く
2. **受け合いの代役**: ブリジュラス等の高耐久を別に用意し、メタモンがコピーで打開できない受け合いを肩代わりさせる
3. **攻めの主軸**: ガブリアス・マリルリ等の積みエースを前に出し、相手に対応を強いてからメタモンを通す

---

## データ分析①：持ち物82.3%が示す「先手で打ち返す」設計

メタモンの持ち物採用率は、**こだわりスカーフ 82.3%**にきわめて偏っています。きあいのタスキ 7.6%・せんせいのツメ 6.6%と続きますが、いずれも1割未満です。

| 持ち物 | 採用率 | 役割 |
|---|---|---|
| こだわりスカーフ | 82.3% | コピー後にスカーフ補正で先手を取る |
| きあいのタスキ | 7.6% | 変身前に1回耐えて変身を通す |
| せんせいのツメ | 6.6% | 20%で先制を取り同速を運で抜く |

この偏りは、メタモンの役割が「相手をコピーするだけ」では完結しないことを示しています。コピーすると相手と**完全に同じすばやさ**になり、そのままでは同速の運勝負になってしまう。スカーフ補正で確実に上を取れて初めて、「積んだエースを追い抜いて倒し返す」という切り返しが成立します。タスキ・せんせいのツメが少数派なのは、これらが「変身前の生存」や「確率的な先手」までしか保証できず、スカーフのような**確定の先手**を生まないためです。

さらに性格でも、上位はのんき（20.5%）・なまいき（17.7%）とすばやさを下げる補正が選ばれます。変身後はスカーフで先手を取る前提なので、自分のすばやさは捨てて変身前の耐久を優先する——持ち物と性格の両面から、メタモンの構築が「変身前に耐え、変身後にスカーフで先手を取る」一点に最適化されていることが読み取れます。

---

## まとめ

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">スカーフ変身型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スカーフ 82.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">コピー後に先手で積みエースを倒し返す</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技が固定。スカーフを叩き落とされると無力化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">タスキ変身型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">タスキ 7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">変身前に1回耐えて変身を確実に通す</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">変身後は同速止まりで先手を保証できない</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メタモンは特性かわりもの（99.1%）で目の前の相手をそのままコピーし、相手のエースをその種族値・能力ランク・技ごと打ち返す、環境でも特殊な役割のポケモンです。技構成はへんしん100%の実質固定で、メタモン自身の性能ではなく「何をコピーするか」で戦い方が決まります。

こだわりスカーフ 82.3%でコピー後に先手を取り、つるぎのまい・りゅうのまいで積んだガブリアス・カイリュー等のエースを追い抜いて倒し返すのが主な仕事です。一方で、種族値オール48の素体は変身前に縛られると脆く、HP実数値155だけが自前の耐久になります。ハッサムの先制技で変身前に落とされる、マスカーニャにスカーフを叩き落とされる、ブリジュラス等の高耐久受けはコピーしても打開できない、といった弱点は単体では解決できず、これらを別のポケモンで処理して「積みエースを打ち返す保険」として運用する構築が前提になります。

---

## 関連記事

- [コピー対象の筆頭 使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [変身前に縛られる先制技 ハッサムのM-2考察](/blog/scizor-analysis-m2/)
- [高耐久で打ち合いに強い ブリジュラスのM-2考察](/blog/archaludon-analysis-m2/)
