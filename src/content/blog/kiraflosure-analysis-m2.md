---
title: '【ポケモンチャンピオンズ】キラフロル考察 M-2 使用率15位 メガ型とタスキ型の二極構造と対策'
description: 'M-2シングル使用率15位のキラフロルを実データで分析。キラフロルナイト54.2%とタスキ36.0%が併存し、てきおうりょくで実質威力190のメガアタッカー型と、どくげしょうで起点を作る無メガタスキ型では動きと対策が真逆。型読みが分かれにくい構築を採用率と相性で解説します。'
pubDate: '2026-06-05'
draft: false
heroImage: '../../assets/hero-kiraflosure-m2.png'
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
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル（M-2）" />
  <div>
    <h2 style="margin:0 0 6px">キラフロル</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:4px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:40px;height:40px;vertical-align:middle" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:40px;height:40px;vertical-align:middle" />
    </div>
    <div style="margin-top:6px;font-size:0.85rem;color:#555">
      使用率 <strong>15位</strong> ／ キラフロルナイト採用率 <strong>54.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30時点）の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、キラフロルは**使用率15位**を記録しています。持ち物は**キラフロルナイト54.2%（メガアタッカー型）**と**きあいのタスキ36.0%（無メガ起点作り型）**に二極化しており、合計約90%が「攻めるメガ型」「起点を撒くタスキ型」のいずれかとして運用されています。

キラフロルの強みは、この**特性も技構成も対策も真逆な2型が共存している**ことにあります。メガ型は特性**てきおうりょく**で一致技を実質×2.0補正し、タスキ型は特性**どくげしょう**で物理技を受けるたびに相手の場にどくびしを撒き続けます。本記事では両型を並列に扱い、データに基づく型選択と環境相性を整理します。

---

## なぜ今キラフロルが強いのか

### 理由1: メガ型はてきおうりょくで一致技が実質威力190

キラフロルの最大の特徴は、メガ後特性が**てきおうりょく**になることです。てきおうりょくはタイプ一致補正を通常の×1.5から**×2.0**に強化する特性で、いわ・どく一致技の実質威力が以下のように跳ね上がります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">基本威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">通常一致(×1.5)</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">てきおうりょく(×2.0)</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">パワージェム（いわ）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">160</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ヘドロウェーブ（どく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">142.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">190</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">だいちのちから（じめん／非一致）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90</td>
</tr>
</tbody>
</table>
</div>

通常のC150アタッカーが「一致技×1.5で実質180」を打つところ、キラフロルは**一致技だけで実質190**に届きます。C150の数値が高いこと以上に、この×2.0補正が火力の天井を引き上げています。

非一致のだいちのちから（実質威力90）も、はがね・どく・いわなど一致技を半減してくる相手に対し抜群を取る等倍以上の二枚目の選択肢として機能します。

### 理由2: メガ進化で C130→150・S86→101 と火力と速度が同時に伸びる（メガ型）

メガ進化前後の種族値変化は以下の通り。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">通常</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">差</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">HP</td><td style="padding:6px 12px;border:1px solid #cbd5e1">83</td><td style="padding:6px 12px;border:1px solid #cbd5e1">83</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#555">±0</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">こうげき</td><td style="padding:6px 12px;border:1px solid #cbd5e1">55</td><td style="padding:6px 12px;border:1px solid #cbd5e1">90</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+35</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">ぼうぎょ</td><td style="padding:6px 12px;border:1px solid #cbd5e1">90</td><td style="padding:6px 12px;border:1px solid #cbd5e1">105</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+15</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">とくこう</td><td style="padding:6px 12px;border:1px solid #cbd5e1">130</td><td style="padding:6px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">150</strong></td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+20</td></tr>
<tr><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">とくぼう</td><td style="padding:6px 12px;border:1px solid #cbd5e1">81</td><td style="padding:6px 12px;border:1px solid #cbd5e1">96</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+15</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">すばやさ</td><td style="padding:6px 12px;border:1px solid #cbd5e1">86</td><td style="padding:6px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">101</strong></td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+15</td></tr>
<tr style="font-weight:700"><td style="padding:6px 12px;border:1px solid #cbd5e1;text-align:left">合計</td><td style="padding:6px 12px;border:1px solid #cbd5e1">515</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#2563eb">625</td><td style="padding:6px 12px;border:1px solid #cbd5e1;color:#059669">+110</td></tr>
</tbody>
</table>
</div>

特に重要なのが**すばやさ86→101**の上昇です。S100ラインを上抜けすることで、リザードン(S100)・ウルガモス(S100)・マフォクシー(S104)直下の中速アタッカーをほぼ捉えられる位置に立てます。

### 理由3: 無メガタスキ型は「どくげしょう＋ステルスロック」で交代を罰する起点役

きあいのタスキ型（採用率36.0%）は、メガ進化せず特性**どくげしょう**を維持します。どくげしょうは「相手から物理技を受けるたびに、相手の場にどくびしを1枚撒く」特性で、2発受けるとどくびしが2枚重なって相手の交代時に「もうどく」状態になります。タスキで一度耐える間に、自然と相手側にどくびしを残せます。

技構成は**ステルスロック36.5%・パワージェム85.3%・だいちのちから66.8%**の組み合わせが中心で、初手の動きは以下のように整理できます：

- 物理アタッカーと対面 → タスキで耐えながら、どくげしょうで相手の場にどくびしを撒く
- 攻撃を受ける前、または2ターン目 → ステルスロックを設置し、いわ4倍・2倍のポケモンへ削りを蓄積
- 残りHP1 → パワージェム・だいちのちから・ヘドロウェーブで一致技を1発

タスキで1発耐えるという保険があるため、無メガでも**初手に出してステルスロックとどくびしを設置する役割を全うできる**のがこの型の本質です。メガ進化を別ポケモン（ガブリアスやハッサム等）に回せる点も、構築全体の柔軟性に直結します。

### 理由4: メガ型とタスキ型で対策が真逆になり、相手は型読みを強いられる

メガ型と無メガタスキ型は、見た目こそ同じキラフロルですが、要求される対策が全く異なります。

| 観点 | メガ型 | 無メガタスキ型 |
|---|---|---|
| 主な脅威 | C150＋てきおうりょくの一致技で確定圏に押し込む | ステルスロック設置＋どくびし設置で長期的に削る |
| 倒し方 | 弱点技（じめん×4・みず×2）で先制 or 後出しから処理 | タスキで1発耐えられる前提で、先制技や2発攻撃で削り切る |
| 受け先 | 高耐久のはがね（ハッサム・ブリジュラス）で受けてC150を凌ぐ | 物理技で殴るとどくげしょうで相手の場にどくびしを撒かれる（2発受けると「もうどく」状態）。特殊技で攻めるのが安全 |

メガ型を想定して「特殊耐久のあるはがね受け」を初手に置くと、タスキ型のステルスロック＋一致技で削られた上にどくびしまで残されます。逆にタスキ型を想定して「特殊技で削り切る」準備をすると、相手がメガ型だった場合はてきおうりょくの一致技を先に受ける可能性があります。

選出段階で**約54:36（持ち物採用率）**の確率分布が読めない以上、相手は対策のリソースを分散させざるを得ません。これがキラフロルが使用率15位を維持している構造的な強みです。

---

## 基本スペック

### タイプ・弱点

<div style="display:flex;align-items:center;gap:6px;margin:10px 0">
  <strong>タイプ：</strong>
  <img src="/images/types/type-05-rock.png" alt="いわ" style="width:40px;height:40px;vertical-align:middle" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:40px;height:40px;vertical-align:middle" />
</div>

いわ/どくの2タイプ倍率を掛け合わせて算出した相性表。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2/×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（½以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:24px;height:24px;vertical-align:middle">じめん<strong style="color:#dc2626">×4</strong></span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px;vertical-align:middle">みず×2</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle">はがね×2</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle">エスパー×2</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">
    <div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle">どく</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle">フェアリー</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle">ノーマル</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle">ひこう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px;vertical-align:middle">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle">むし</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:24px;height:24px;vertical-align:middle">ゴースト</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">—</td>
</tr>
</tbody>
</table>
</div>

耐性の数は多いものの、**じめん×4**は致命的で、環境1位のガブリアス（じしん99.2%）と7位のカバルドン（じしん98.0%）に対し受け出しが一切できません。

---

## 主要型の解説

### 型① キラフロル CS型（持ち物採用率54.2%）

メガ進化前提でC32 S32に振り切る特殊アタッカー型。

<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル CS型" style="width:48px;height:48px" />
  <div>
    <strong>キラフロル CS型</strong><br>
    <small style="color:#666">キラフロルナイト 54.2%</small>
  </div>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">内容</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう（57.8%）または ひかえめ（33.0%）</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">C32 S32（余り2はH・B・Dから選択）</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">キラフロルナイト（54.2%）</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>特性</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">どくげしょう（88.5%）※メガ後てきおうりょく（一致技×2.0）</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>必須技</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（85.3%）・ヘドロウェーブ（69.4%）・だいちのちから（66.8%）</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>選択技</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">ニードルガード（27.9%）／ステルスロック（36.5%）／マッドショット（19.1%）／ロックカット（16.1%）</td></tr>
</tbody>
</table>
</div>

**性格の選択（おくびょう vs ひかえめ）:**

C32振り時のS実数値・C実数値は以下の通り。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">S実数値（S101）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">C実数値（C150）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">抜けるライン</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">おくびょう（57.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>S168</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C202</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">最速リザードン・ウルガモス（S実数値167）を1差で上抜き。最速ガブリアス（S169）にはわずかに届かない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ひかえめ（33.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S153</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>C222</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">S100族（リザードン・ウルガモス）には抜かれ、最速マフォクシー（S171）にも届かない。火力に振った代わりに先制を捨てる選択</td>
</tr>
</tbody>
</table>
</div>

**強み（型②との対比）:** ひかえめなら型②の最大C200を上回るC222まで火力を伸ばせ、おくびょうならS実数値168でS100族（リザードン・ウルガモス）を1差で上抜きできる。メガ後のてきおうりょくが乗ることで、型②の通常一致技×1.5に対し×2.0で実質威力が約33%上回る。

**弱み（型②との対比）:** 持ち物がキラフロルナイト固定で、タスキ・たべのこしによる耐久保険が一切ない。メガ進化のターンを使うため初手の起点作りが1テンポ遅れる。

---

### 型② 無メガ タスキ起点作り型（持ち物採用率36.0%）

特性どくげしょう（物理技を受けるたびに相手側にどくびしを1枚展開、2枚重なると交代時に「もうどく」状態）を維持し、きあいのタスキで1発耐えて起点を作る役。

<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="無メガ キラフロル タスキ型" style="width:48px;height:48px" />
  <div>
    <strong>無メガ タスキ起点作り型</strong><br>
    <small style="color:#666">きあいのタスキ 36.0%</small>
  </div>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">内容</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>性格</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう または ひかえめ</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>EV</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">C32 S32</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>持ち物</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ（36.0%）</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>特性</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">どくげしょう（88.5%）</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><strong>技構成例</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック / パワージェム / だいちのちから / ヘドロウェーブ</td></tr>
</tbody>
</table>
</div>

**強み（型①との対比）:** タスキで1発耐えが保証されるため、初手で確実にステルスロック（採用率36.5%）を撒ける。じめん×4・みず×2の弱点を突かれても1発で落ちず、最低限の仕事が約束される。メガ枠を別ポケモンに譲れる。

**弱み（型①との対比）:** 一致技がてきおうりょく×2.0ではなく通常の×1.5止まりで、パワージェム実質威力120／ヘドロウェーブ142.5までしか伸びない（型①と比べ約25%火力ダウン）。S実数値も通常種族値S86止まり（おくびょうC32S32時 S151）で、型①のメガ後S168に届かない。タスキは1試合1回しか機能せず、再登場時には素の耐久で殴り合うことになる。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">解説</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワージェム</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>85.3%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">80</td><td style="padding:8px 12px;border:1px solid #cbd5e1">メインのいわ一致技。メガ後てきおうりょくで実質160</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>69.4%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">95</td><td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致技。メガ後実質190。フェアリー（フラエッテ等）にばつぐん</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>66.8%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">90</td><td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・どく半減のはがね（ブリジュラス・ハッサム）への等倍以上の打点</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>36.5%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td><td style="padding:8px 12px;border:1px solid #cbd5e1">交代時にいわ倍率分のダメージを与える設置技。型②との相性が良い</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ニードルガード</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>27.9%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td><td style="padding:8px 12px;border:1px solid #cbd5e1">守りつつ接触技に反撃ダメージ。メガ進化ターンの隙消しに使える</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>キラースピン</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>20.6%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">30</td><td style="padding:8px 12px;border:1px solid #cbd5e1">自分側の設置技（ステルスロック・どくびし等）を除去＋S1段階アップ。設置依存環境への対抗</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マッドショット</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>19.1%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">55</td><td style="padding:8px 12px;border:1px solid #cbd5e1">相手のS1段階ダウン。S101を補強し中速帯を縛る</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ロックカット</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>16.1%</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td><td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:right">—</td><td style="padding:8px 12px;border:1px solid #cbd5e1">自分のS2段階アップ。おくびょうメガキラフロル（S実数値168）から積めばS336相当となり、最速スカーフ持ちも含めて上から動ける</td></tr>
</tbody>
</table>
</div>

---

## パーティ構成

この節では使用率TOP30から、キラフロル（メガ後S101・じめん×4／みず×2／はがね×2／エスパー×2）のタイプ相性と相手の主力技採用率を突き合わせ、相性がはっきり出る相手だけを有利・不利の両面で抽出しています。

### 苦手なポケモン

じめん×4・みず×2・はがね×2を採用率20%以上で突いてくる相手、またはお互い有効打が乏しく長期戦で削り負ける相手をリストアップ。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん99.2%が<strong>じめん×4で確定1発</strong>。最速ガブリアスS実数値169はおくびょうメガキラフロルS実数値168を1差で抜き、後出し・対面どちらも勝てない</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん98.0%が<strong>じめん×4で確定1発</strong>。あくび94.2%で起点化もされる。こちらのだいちのちからは入るがS低耐久なので殴り合いも厳しい</td>
</tr>
<tr style="background:#fee2e2">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラスターカノン55.7%が<strong>はがね×2</strong>で重く、10まんボルト66.9%も等倍で通る。こちらのパワージェムははがね/ドラゴンに×0.5×0.5=×0.25で通らず、だいちのちから(×2)で削るしかないが先制を取られて落ちる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり85.9%が<strong>みず×2</strong>、じしん63.7%が<strong>じめん×4</strong>。りゅうのまい73.3%を積まれると追いつけない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0121-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">スターミー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクアブレイク89.2%が<strong>みず×2</strong>、しねんのずつき39.4%が<strong>エスパー×2</strong>。S115でこちらより速くアクアジェット86.9%の先制でも削られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0212-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ハッサム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ99.7%が<strong>はがね×2</strong>で先制圏。こちらのヘドロウェーブははがね/むしに×0.25、パワージェムも×0.5で火力が通らず、だいちのちから×2しか有効打が無い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうにより<strong>だいちのちからが無効化</strong>され、パワージェムは等倍・ヘドロウェーブは×0.5と有効打が乏しい。一方アーマーガアもこちらの弱点を突けないが、てっぺき63.5%＋ボディプレス70.9%＋はねやすめ98.1%で居座られると長期戦で確実に削り負ける</td>
</tr>
</tbody>
</table>
</div>

### 有利なポケモン

相手の主力技でこちらの弱点（じめん・みず・はがね・エスパー）を20%以上突かれない相手のみを抽出。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">リザードン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお/ひこうにパワージェムが<strong>×4で確定1発</strong>。ソーラービーム61.0%はくさ技だが2ターン技で隙が大きい。最速同士でもS実数値168対167で1差先行</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン/ひこうにパワージェムが<strong>×4</strong>。みず・じめん弱点技を突かれない。S80でこちらが先行（しんそく45.6%は先制で通るが等倍止まり）</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ウルガモス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/ほのおにパワージェムが<strong>×4で確定1発</strong>。ほのおのまい79.7%・むしのさざめき33.7%・ギガドレイン59.2%いずれもこちらの弱点ではない。最速同士でもS実数値168対167で1差先行</td>
</tr>
<tr style="background:#dcfce7">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0670-05.webp" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">フラエッテ（永遠）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリーにヘドロウェーブ×2＝実質威力380。ムーンフォースはどく耐性で×0.5</td>
</tr>
</tbody>
</table>
</div>

### 相性の良いパーティパートナー

同居率TOP10から、キラフロルの弱点（じめん×4・みず×2・はがね×2）を補完するパートナーを抜粋。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム">
    <div class="name">ハッサム</div>
    <div class="rate">同居1位／じめん受け（耐性×0.5）</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー">
    <div class="name">カイリュー</div>
    <div class="rate">同居2位／じめん無効</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居3位／高速・はがね対面</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居4位／みず・はがね受け</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居7位／じめん無効・受け</div>
  </div>
</div>

**パーティ構成のポイント:**
1. **じめん受けが最優先:** じめん×4はガブリアス（1位）・カバルドン（7位）に確定1発で抜かれる致命傷。同居率1位ハッサム（じめん×0.5）、2位カイリュー（じめん無効）、7位アーマーガア（じめん無効）が自然に組み込まれているのは、この受け枠を埋めるための構築選択であることがデータから読み取れる
2. **はがね受け補完:** ブリジュラス（同居4位）はラスターカノン・10まんボルトを半減でき、キラフロルが対面取れないハッサム・ブリジュラス対面を裏から処理できる
3. **タスキ型はステロ起点役:** 型②採用時は同居率2位カイリュー・3位ガブリアスなどの一致技フィニッシャーを後ろに置き、ステロダメージで確定数を1段階繰り上げる役割分担になる

---

## データ分析①：CS振り率95%超の固定化と持ち物の二極化

キラフロルのデータを環境TOP20と並べると、**EV配分と持ち物の構造が他とは違う偏り方**をしていることが見えてきます。

### EVスプレッドの極端な固定化

|順位|EVスプレッド|採用率|
|---|---|---|
|1位|CS+hb|36.7%|
|2位|CS+h|18.5%|
|3位|CS+hd|9.7%|
|4位|CS+b|2.9%|
|5位|CS+d|2.4%|
|6位|CS|1.5%|
|合計（C32 S32 確定）|—|**約72%以上**|

TOP6スプレッド全てが**C32 S32確定**で、違いは余り2の振り先のみです。同居率1位のハッサムがHA軸（H32 A32）で性格・余り振りに分かれるのに対し、キラフロルはCS振り（C32 S32）が全個体で固定化されています。これは「**Cで確定数を作る／Sで先手を取る**」の2つを両立する以外の選択肢が事実上存在しないことを意味します。

### 持ち物の二極化──ハッサムにはない構造

|持ち物|採用率|役割|
|---|---|---|
|キラフロルナイト|54.2%|メガ進化前提アタッカー|
|きあいのタスキ|36.0%|無メガ起点作り|
|たべのこし|5.0%|残飯耐久|
|こだわりスカーフ|1.5%|S補強|

同居率1位のハッサムがハッサムナイト79.1%＋メタルコート9.5%で**バレットパンチ強化アイテムに約89%が集中**しているのに対し、キラフロルは**メガ型54.2%とタスキ型36.0%という二極化**を見せています。これは「特性てきおうりょくのメガ型」と「特性どくげしょうのタスキ型」が**特性ごと異なる役割を担う2軸構造**になっていることを示しており、ハッサムのような単一フィニッシャーへの収束が起きていません。

採用率15位という中位ながら型が二極化するのは、**メガ枠を別ポケモンに譲りつつ起点作りで貢献する用途**と、**メガ枠を確保してC150×てきおうりょくの最大火力を出す用途**が、構築側の役割設計に応じて使い分けられているためと読める。

---

## まとめ：型比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">特性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">EV</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">主な技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">得意場面</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">メガ CS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">てきおうりょく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C32 S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">パワージェム / ヘドロウェーブ / だいちのちから / ステロ or ニードルガード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">54.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">一致技×2.0の最大火力でS100族を上抜き</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:bold">無メガ タスキ起点作り型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どくげしょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">C32 S32</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステロ / パワージェム / だいちのちから / ヘドロウェーブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">タスキ保証でステロ展開＋どくびし展開</td>
</tr>
</tbody>
</table>
</div>

キラフロルはM-2環境において、**特性てきおうりょくによる一致技×2.0補正**でC150以上の火力を引き出し、**メガ後S101でS100族を上抜く**特殊アタッカーです。

CS振り95%超・C32 S32固定という構築の収束が示すように、最もシンプルで強い使い方は「**メガ進化でC150×てきおうりょくの最大火力を確保し、S実数値168（おくびょう最速）から一致技で詰める**」形です。

じめん×4（ガブリアス・カバルドン）・みず×2（スターミー・ギャラドス）・はがね×2（ハッサム・ブリジュラス）への対策枠を用意できれば、フェアリー・ほのお・ひこう・むしタイプを軒並み確定1発圏に捉える強力なメガ進化ポケモンです。

関連記事: [メガハッサム考察 M-2 使用率14位](/blog/scizor-analysis-m2)
