---
title: '【ポケモンチャンピオンズ】ウツボット考察 M-2 使用率69位 メガ進化とちからをすいとるの粘り型'
description: 'M-2シングルバトルで使用率69位のウツボットを徹底分析。ウツボットナイト採用率98.0%のメガ前提運用、ちからをすいとる97.2%による相手のこうげき低下＋回復、ギガドレイン・ふいうち・アンコールで粘る型を実データで解説。ようりょくそが機能しない理由も検証します。'
pubDate: '2026-06-11'
draft: true
heroImage: '../../assets/hero-victreebel-m2.png'
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
  <img src="/images/pokemon/pokemon-0071-00.webp" alt="ウツボット" />
  <div>
    <h2 style="margin:0 0 8px">ウツボット</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">69位</strong>　持ち物: <strong>ウツボットナイト 98.0%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/24）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ウツボットは**使用率69位**を記録。持ち物は**ウツボットナイト（採用率98.0%）**がほぼ全数で、実態は**メガウツボット前提**のポケモンです。

最大の軸は**ちからをすいとる（採用率97.2%）**。相手のこうげきを下げながらその実数値ぶんHPを回復する変化技で、物理アタッカーと対面して殴り合いを成立させなくする「居座って粘る」動きが本体です。ギガドレイン（55.6%）でHPを取り戻しつつ削り、ふいうち（45.8%）であくの先制を持ち、アンコール（38.2%）で起点を縛ります。火力で押すより、相手の手を鈍らせて長く居座るのがウツボットの戦い方です。

本記事では採用率98.0%のメガウツボットを基準に解説します。

---

## なぜウツボットが使われるのか

### 1. ちからをすいとるで物理アタッカーを機能停止させる

ウツボットの主軸は**ちからをすいとる（採用率97.2%）**です。相手のこうげきを1段階下げ、同時に「下げた相手のこうげき実数値ぶん」のHPを回復します。物理アタッカーと対面すると、相手の打点を削りながらこちらは大きく回復するため、ガブリアス・ドドゲザンのような物理エースを1体で受け止めて機能停止に追い込めます。メガ後はぼうぎょ実数値137・とくぼう実数値147とHP実数値187で、こうげきを下げた相手の物理を継続的に枯らせます。

### 2. ギガドレイン・ふいうちで居座りながら削る

ギガドレイン（採用率55.6%）はくさ一致の吸収技で、ダメージを与えつつHPを回復します。ちからをすいとると合わせ、被弾を回復で取り返しながら盤面に残り続けるのが基本の動きです。さらに**ふいうち（45.8%）**はあくタイプの優先度+1技で、すばやさに関係なく先制でき、ゴースト・エスパーへ刺さります。メガ後のすばやさは実数値134（無補正122）と速くないため、遅さを補う打点としてふいうちが機能します。

### 3. アンコールで相手の行動を縛る

アンコール（採用率38.2%）は相手が直前に使った技を3ターン強制する変化技です。相手の積み技・変化技・撃ち分けを縛り、ちからをすいとるで回復しながら起点化を防げます。ちからをすいとる・ギガドレインの回復で居座れるウツボットは、アンコールで相手を固定して有利な対面を維持しやすい点が採用理由です。

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
      <div style="width:52.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">490</span>
  </div>
</div>

通常時はこうげき105・とくこう100と攻撃寄りの両刀型ですが、すばやさ70・ぼうぎょ65・とくぼう70と中速・低耐久で、素のままでは器用貧乏です。メガ進化で耐久と火力が底上げされ、ちからをすいとるの回復と噛み合います。

### メガ進化（ウツボットナイト採用率98.0%）

ウツボットナイトの採用率は98.0%で、ほぼ全個体がメガ進化前提です。メガ後はぼうぎょ85・とくぼう95・とくこう135まで上がり、特性はようりょくそから**とびだすなかみ**に変わります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">通常</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">105</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">125</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">135</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+35</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+25</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
</tbody>
</table>
</div>

メガ後の特性とびだすなかみは「ひんしになった時、攻撃してきた相手に自分が受けたダメージと同じだけのダメージを与える」効果です。倒され際に相手へ道連れ級の反撃を返せるため、ちからをすいとるで粘ったあと最後に相手を道連れにする動きと噛み合います。

ここで重要なのが、**通常特性のようりょくそ（採用率94.2%）はメガ進化すると失われる**点です。ようりょくそは「にほんばれ状態のときすばやさ2倍」ですが、M-2環境で晴れを撒く特性ひでり持ち（キュウコン・コータス）はいずれも使用率TOP50圏外で、にほんばれを採用する環境ポケモンも見当たりません。つまり晴れが用意されない上に、98.0%がメガ進化で特性をとびだすなかみへ上書きするため、**ようりょくそはほぼ機能しません**。メガウツボットはすばやさ実数値134（無補正122）止まりの中速ポケモンとして運用するのが実態です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-11-grass.png" alt="くさ" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="くさ" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="どく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍/0.25倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（0.25）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span style="color:#94a3b8">なし</span>
  </td>
</tr>
</tbody>
</table>
</div>

くさ/どくはみず・でんき・かくとう・くさ・フェアリーを半減でき、特に物理アタッカーのかくとう・みず技を受けやすい点がちからをすいとるでの粘りと噛み合います。一方、弱点は**ほのお・こおり・じめん・ひこう・エスパーの5タイプがいずれも×2**で、ガブリアスのじしん（採用率99.2%）・リザードンのほのお技・マスカーニャのトリプルアクセル（こおり）など、環境上位の主力技が刺さる点に注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちからをすいとる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のこうげきを1段階下げ、その実数値ぶん回復。物理受けの主軸</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガドレイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ一致の吸収技。与ダメージの半分を回復し居座る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">45.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の先制技。ゴースト・エスパーに刺さる。相手が攻撃技なら成功</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">直前の技を3ターン強制。積み技・変化技を縛る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致技。フェアリー・くさへの打点。10%どく</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロばくだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致技。30%どくでヘドロウェーブと選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくづき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく物理一致技。物理寄りの個体が採用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はたきおとす</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の持ち物を落とす。あくでゴースト・エスパーに刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくどく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">もうどくで高耐久を削る。居座り型と相性が良い</td>
</tr>
</tbody>
</table>
</div>

ちからをすいとる（97.2%）がほぼ確定枠で、ギガドレイン・ふいうち・アンコールから2〜3枠を選ぶのが標準です。どく打点はヘドロウェーブ（33.3%）・ヘドロばくだん（18.4%）・どくづき（14.2%）に分散し、特殊寄りか物理寄りかで使い分けられています。

---

## 主要型の解説

性格はひかえめ26.5%・いじっぱり14.1%・れいせい13.5%・わんぱく10.6%と分散し、特殊寄り・物理寄り・耐久寄りが混在します。共通するのはちからをすいとる＋ウツボットナイトで、技構成と性格で役割を寄せる形です。

### 型1: ちからをすいとる物理受け型（最多級）

**指標: ちからをすいとる 97.2%／ひかえめ 26.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0071-00.webp" alt="ウツボット" style="width:48px;height:48px">
  <strong style="font-size:1.05em">すいとる粘り型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ようりょくそ（94.2%）※メガ後とびだすなかみ<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32 C32（HC振り。最多はH+2やC+2）<br>
<strong>持ち物:</strong> ウツボットナイト
</div>
<div>
<strong>技構成:</strong><br>
・ちからをすいとる<br>
・ギガドレイン<br>
・ふいうち / ヘドロウェーブ<br>
・アンコール / どくどく
</div>
</div>
</div>

**強み:**

ちからをすいとる＋ギガドレインの二重回復で物理アタッカーに居座り、こうげきを下げて殴り合いを成立させなくします。ヘドロウェーブ採用でフェアリーへ×2の特殊打点を持ち、アンコールで積み技・変化技を縛れます。とくこう実数値187（メガ後ひかえめ）でギガドレインの回復量・打点を確保できる、特殊寄りの粘り型です。

**弱み:**

ふいうちが特殊型では抜けやすく、あくの先制打点が薄くなります。すばやさ実数値134止まりで、後述の物理寄り型と異なり物理の確定数を詰める速さもないため、弱点技を持つ高速アタッカーには先手で焼かれて回復が間に合わない場面が増えます。

---

### 型2: ふいうち物理寄り型

**指標: いじっぱり 14.1%／どくづき 14.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0071-00.webp" alt="ウツボット" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ふいうち物理型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ようりょくそ（94.2%）※メガ後とびだすなかみ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32 A32（HA振り）<br>
<strong>持ち物:</strong> ウツボットナイト
</div>
<div>
<strong>技構成:</strong><br>
・ちからをすいとる<br>
・ふいうち<br>
・どくづき / ヘドロウェーブ<br>
・アンコール / はたきおとす
</div>
</div>
</div>

**強み:**

こうげき実数値194（メガ後いじっぱり）でふいうちの先制打点が重く、特殊型では削り切れないゴースト・エスパーを優先度+1で処理できます。はたきおとす採用でメガ前の相手の持ち物を落とせるのも物理型固有の選択です。ちからをすいとるで自分のこうげきが下がっても、回復目的の技なのでふいうち主体の打点は維持できます。

**弱み:**

ふいうちは相手が攻撃技を選ばないと失敗するため、変化技・交代を読まれると空振りします。ギガドレインを切る構成が多く、特殊型に比べて回復はちからをすいとるのみに依存し、弱点技を連打されると押し切られやすくなります。

---

### 補足: どくどく耐久型（どくどく 13.2%）

どくどくを採用し、ちからをすいとる・ギガドレインの回復で居座りながらもうどくで高耐久を削る型です。アシレーヌ・ブリジュラスのような一撃で落とせない相手を、回復しつつ毒の蓄積で崩します。ふいうち・ヘドロウェーブの即時打点を1枠削るため、短期決戦には向かず、長期戦前提の構築に組み込まれます。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ウツボットと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ちからをすいとるで物理アタッカーに強い一方、すばやさ実数値134（無補正122）と中速で、弱点（ほのお・こおり・じめん・ひこう・エスパー）を突く高速アタッカーには先手で焼かれる点に注意してください。

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
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく/はがねでこちらに弱点を突けず、ふいうち（採用率99.0%）等の物理打点をちからをすいとるで枯らせる。アイアンヘッドは等倍で、回復しながら居座れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプ（98.5%）・10まんボルト（56.8%）ともに×0.5で半減。ギガドレインがでんき/みずに×2で刺さり、おにび（80.6%）を撒かれても物理は使わないので痛手が小さい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（97.0%）が×0.5、うたかたのアリア（みず）も×0.5。ヘドロウェーブがどく×2で刺さり、特殊耐久（D実数値147）で受けつつ削れる。アクアジェットも半減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）が×2弱点。S102でこちらより速く、ちからをすいとるで下げても×2じしんは重い。スケイルショット（34.4%・等倍）を持つ個体は追加で削られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・ひこうともに×2弱点で、S100からこちら（S実数値134）の上を取られる。特殊アタッカーのためちからをすいとるが効かず、回復が間に合わない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（72.2%・こおり）が×2でS123から先制。連続技なのでちからをすいとるの回復より蓄積ダメージが勝ちやすい。はたきおとす（57.6%）でメガ前を狩られる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/ほのおでほのお技が×2弱点。S100でこちらの上を取り、特殊型のためちからをすいとるが無力。ふいうち（あく等倍）では一撃に届かない</td>
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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（99.2%）が×2弱点。S102で先手を取られ、ちからをすいとるで下げても×2の一致じしんは重く居座れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう・ふゆうでじめんを透かせるアーマーガア等を後続に置く。ギガドレイン（じめん/ドラゴンに×2弱点ではないが地面複合に通る）はガブには等倍止まりなので、引いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・ひこう×2弱点をS100の先手で突かれ、特殊アタッカーなのでちからをすいとるが無効。回復で耐えきれない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・いわ枠（ウォッシュロトム・カバルドンのいわ技等）でほのおを半減して受け、上から処理する。ふいうちでは火力不足なので無理に対面しない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリプルアクセル（72.2%・こおり×2）の連続技がちからをすいとるの回復を上回り、S123で先制。はたきおとすでメガ前のウツボットナイトを落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・はがね・どく枠（ハッサム・ドドゲザン等）でこおり技を半減し、あく弱点を突いて処理する後続を用意する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウルガモス（18位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技×2弱点をS100で先制され、特殊型のためちからをすいとるが効かない。ちょうのまいで積まれると一層手がつけられない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ・みず枠（カバルドンのいわ技・ウォッシュロトム）でほのおを半減しつつ、ガブリアス等の高速ドラゴンで上から処理する。アンコールでちょうのまいを縛れる個体なら粘れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">むし/はがねでヘドロウェーブ・ギガドレインともに半減〜等倍。ちからをすいとるで物理は枯らせるが、こちらの打点が乏しく押し込めない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお・じめん枠（リザードン・ガブリアス等）ではがね弱点を突く後続を置く。ヘドロウェーブはむしに半減されるため単体での突破は狙わない</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「ウツボットの弱点（ほのお・こおり・じめん・ひこう・エスパー）を高速で突く特殊アタッカー」と「はがね等でこちらの打点を半減し、撃ち合いで押し込めない相手」に大別されます。ちからをすいとるは特殊アタッカーには無力なため、後続のタイプ補完で受ける構築が前提です。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0302-00.webp" alt="ヤミラミ">
    <div class="name">ヤミラミ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あく/ゴーストでエスパーを透かし、ウツボットの苦手なエスパー打点を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0695-00.webp" alt="エレザード">
    <div class="name">エレザード</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき/ノーマルの高速特殊枠。ウツボットが苦手な高速アタッカーに先手で打点を持つ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめんでウルガモス等のほのお勢を上から削る高速ドラゴン枠</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでこおり・ひこうを半減し、苦手なマスカーニャ等を受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ (オス)">
    <div class="name">イダイトウ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/ゴーストの打点役。エスパーを透かしつつ高火力で崩す</div>
  </div>
</div>

**パーティ構成の基本方針:**

ウツボットは弱点が5タイプと多く、特殊アタッカーには無力なため、残り5体で以下の役割を補います。

1. **エスパー対策**: あく・ゴースト（ヤミラミ・イダイトウ）でエスパー技を透かす枠
2. **ほのお対策**: みず・いわ（ウォッシュロトム・カバルドン等）でリザードン・ウルガモスのほのお技を半減する枠
3. **高速アタッカー処理**: 高速のでんき・じめん（エレザード・ガブリアス）でこちらの上を取る相手に先手で打点を持つ枠
4. **こおり・ひこう対策**: はがね（ブリジュラス）でマスカーニャのトリプルアクセル等を半減し、後続で受ける

---

## データ分析①：採用率に見る「殴る型」ではなく「枯らす型」

ウツボットの技採用率は、攻撃技より**変化技・吸収技の採用率が高い**点に特徴があります。

| 技 | 分類 | 採用率 | 役割 |
|---|---|---|---|
| ちからをすいとる | 変化（回復＋A↓） | 97.2% | 物理受け・回復 |
| ギガドレイン | くさ（吸収） | 55.6% | 回復しつつ削る |
| ふいうち | あく（先制） | 45.8% | 遅さを補う先制打点 |
| アンコール | 変化（行動縛り） | 38.2% | 起点化阻止 |
| ヘドロウェーブ | どく（攻撃） | 33.3% | フェアリーへの打点 |

ほぼ全数が採用するちからをすいとる（97.2%）は攻撃技ではなく、相手のこうげきを下げて回復する変化技です。次点のギガドレイン（55.6%）も吸収技で、純粋な攻撃技で最も高いヘドロウェーブですら33.3%にとどまります。**回復・行動阻害系（ちからをすいとる97.2%＋アンコール38.2%）が攻撃技を上回る**この分布は、ウツボットが「火力で押す」のではなく「相手を枯らして居座る」ことを前提に運用されていることを示します。

さらにこの設計は、メガ後すばやさ実数値134止まりという遅さと噛み合っています。上から殴れない以上、ちからをすいとるで物理を枯らし、ふいうち（優先度+1）で遅さを無視した先制打点を持つのが合理的な選択です。火力を伸ばす持ち物（こだわり系）が実装されていない環境では、ウツボットナイト98.0%・ちからをすいとる97.2%という「メガで耐久を上げて粘る」一択に近い構築思想が読み取れます。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すいとる粘り型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちからをすいとる 97.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">二重回復で物理を枯らす。ヘドロウェーブ×2打点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうちの先制打点が薄い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ふいうち物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり 14.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A194のふいうちでゴースト・エスパーを先制処理</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ふいうちは変化技読みで失敗。回復が薄い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">どくどく耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どくどく 13.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく等</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">高耐久をもうどくで崩す。長期戦に強い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">即時打点が薄く短期決戦に弱い</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ウツボットはウツボットナイト（98.0%）でメガ進化し、ちからをすいとる（97.2%）で物理アタッカーのこうげきを下げて回復しながら居座る粘り型です。ギガドレインの二重回復・ふいうちの先制・アンコールの行動縛りで、火力で押すのではなく相手を枯らして勝つ動きを軸にします。ドドゲザン・ウォッシュロトム・アシレーヌのような弱点を突けない相手には強い一方、すばやさ実数値134止まりで弱点5タイプを高速で突くリザードン・マスカーニャ・ウルガモスには先手で焼かれます。

通常特性ようりょくそは環境に晴れ要員がほぼおらず、98.0%がメガ進化でとびだすなかみへ上書きするため機能しません。中速・低めの素早さを前提に、苦手な高速特殊アタッカーは後続のタイプ補完で受ける構築が必須です。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [弱点ほのお・ひこうで上を取る リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
- [こおり技で上を取るマスカーニャのM-2考察](/blog/meowscarada-analysis-m2/)
</content>
</invoke>
