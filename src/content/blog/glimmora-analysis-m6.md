---
title: '【ポケモンチャンピオンズ】キラフロル 考察 M-6 シーズン ステルスロック軸の解説'
description: 'M-6シーズン使用率16位のキラフロルを考察。どくげしょう×ステルスロックのいわ/どく型構成・実数値、メガ進化の採用率低下、ガブリアス・ボーマンダなど苦手なポケモンとメガリザードンYなど得意なポケモンをデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-glimmora-m6.png'
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
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" />
  <div>
    <h2 style="margin:0 0 8px">キラフロル</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">16位</strong>　特性: <strong>どくげしょう 95.2%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも2026-09-10時点のスナップショットを使用しています。

M-6シーズンのキラフロルは使用率16位。いわ/どくの複合タイプに特性どくげしょうを持ち、ステルスロックで設置しつつパワージェム・だいちのちから・ヘドロウェーブの3タイプ複合打点で攻める特殊アタッカーです。持ち物はきあいのタスキが過半数を占め、耐久面の脆さを1回の被弾耐えで補う構成が主流です。

---

## キラフロルの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:41%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">83</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:28%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:41%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">86</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

C130が突出しており、種族値の中では特殊アタッカーとしての適性が最も高い数値です。A55は低く物理技には向きません。HP83・B90・D81は並程度で、後述のきあいのタスキで最初の一撃を耐えることが実戦上の耐久の前提になります。S86は環境上位と比べて高くはなく、素早さで上から動ける相手は限られます。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-05-rock.png" alt="いわ" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
  </td>
</tr>
</tbody>
</table>
</div>

じめん×4が最大の弱点で、環境1位のガブリアスのじしん（採用率67.6%）を筆頭に一致技を持つ相手が多く、実質的な天敵になります。みず・エスパー・はがねの×2弱点も広く、耐性はノーマル・ほのお・ひこう・むし・フェアリーの半減にとどまり、無効タイプはありません。

### 特性

<strong>どくげしょう（95.2%）</strong>がほぼ全個体で採用されています。物理技のダメージを受けるたびに相手の場をどくびし状態にする特性で、接触技限定ではなく「物理技を受けるたび」に発動します。2回受けるとどくびしが2枚になり、相手が交代で場に出すポケモンは「もうどく」状態になります。相手の後続を毒で消耗させる設置効果として機能し、ステルスロックと合わせて相手の交代コストを高める役割を担います。少数派のふしょく（4.8%）は、はがね・どくタイプの相手も毒状態にできる特性です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワージェム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">80.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いわ一致のメインウェポン。追加効果なしの安定打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場に設置。弱点倍率に応じた固定割合を交代のたびに削る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">57.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10%で相手の特防を1段階下降。はがね複合への打点を補う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">56.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どく一致で最高威力。10%で相手を毒状態にする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>キラースピン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力は低いが自陣の設置技を解除しつつ相手を毒にする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エナジーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプへの打点を補う選択技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マッドショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の素早さを1段階下降。だいちのちからより威力は劣る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>マジカルシャイン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン・かくとう複合への打点を補う少数派の選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロばくだん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30%で毒状態。ヘドロウェーブより威力は劣る少数派の選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ニードルガード</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+4で1ターン防御。接触技には最大HPの1/8を反撃</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

パワージェム・ステルスロック・だいちのちから・ヘドロウェーブの4技はいずれも採用率50%を超えており、この4技構成が主流です。持ち物・性格・EVで型を分けます。

### 型1：きあいのタスキ特殊アタッカー型

**性格採用率: おくびょう 45.1% ／ ひかえめ 39.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> どくげしょう（95.2%）<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H1-B1-C32-S32<br>
<strong>持ち物:</strong> きあいのタスキ（56.6%）
</div>
<div>
<strong>技構成:</strong><br>
・パワージェム<br>
・ステルスロック<br>
・だいちのちから<br>
・ヘドロウェーブ
</div>
</div>
</div>

きあいのタスキでHP満タン時の一撃技を1回だけ耐え、その間にステルスロックを設置しつつ攻撃技で打点を出す構成です。おくびょう型はC実数値182・S実数値151、ひかえめ型はC実数値200・S実数値138になります。

**強み:**

きあいのタスキにより、じめん×4弱点の一撃を含め、初手の1発をHP1で耐えられます。これによりステルスロックの設置や後続への負荷（どくげしょうのどくびし）を確実に稼げます。

**弱み:**

タスキは1度使うと消えるため、2発目以降はキラフロル種族値どおりの並程度の耐久（H83・D81、前述）で受けることになります。じめん・みず・エスパー・はがねの弱点技を複数回受ける展開には弱く、後続への負担が大きくなります。

**性格による派生（ひかえめ型）:**

ひかえめに変えるとC実数値200・S実数値138となり、だいちのちから・ヘドロウェーブの打点はおくびょう型（C182）より伸びますが、S実数値がおくびょう型（S151）より13低くなり、上から動ける相手の範囲が狭まります。全体の性格採用率はおくびょう45.1%・ひかえめ39.7%とほぼ拮抗しており、打点重視ならひかえめ、先手の範囲重視ならおくびょうという選択になります。

**持ち物の派生（ふうせん型）:**

持ち物2位はふうせん（採用率14.2%）で、メガ進化（キラフロルナイト10.4%）より採用率が高い選択肢です。ふうせんは接地しなくなる効果を持ち、キラフロルの最大の弱点であるじめん×4の技を根本から無効化できます。ただし一度でも攻撃技を受けるとふうせんは割れて接地状態に戻るため、無効化できるのは最初の1回のみです。タスキが「1回だけ耐える」のに対し、ふうせんは「じめん技を1回だけ無効化する」対策になる一方、じめん以外の弱点技や特殊アタッカーの一撃は素で受けることになる点がタスキ型との違いです。

---

### 型2：メガキラフロル型（少数派）

**アイテム採用率: キラフロルナイト 10.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガキラフロル型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> どくげしょう（メガ進化前、採用率95.2%）→ てきおうりょく（メガ進化で固定）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H1-B1-C32-S32<br>
<strong>持ち物:</strong> キラフロルナイト（10.4%）
</div>
<div>
<strong>技構成:</strong><br>
・パワージェム<br>
・ステルスロック<br>
・だいちのちから<br>
・ヘドロウェーブ
</div>
</div>
</div>

メガ進化するとC150・S101まで上昇し、特性もてきおうりょくに変わります。カードの性格（ひかえめ）ではC実数値222・S実数値153です。素早さ上昇を優先しておくびょうを選んだ場合はC実数値202・S実数値168となり、打点と先手のどちらを取るかはこの2択のトレードオフになります。てきおうりょくは一致技の威力を通常の1.5倍ではなく2倍にする効果で、いわ・どく一致のパワージェム・ヘドロウェーブの打点が大きく伸びます。

**強み:**

メガ進化後はC222（ひかえめ）と、型1のきあいのタスキ型（C182〜200）を上回る特殊火力に加え、てきおうりょくで一致技が2倍になるため、パワージェム・ヘドロウェーブの実質威力がさらに高まります。

**弱み:**

きあいのタスキを持てないため初手を耐える手段がなく、じめん×4弱点の一撃技を受けると多くの相手に落とされます。メガ進化枠を消費する点も踏まえ、M-6では採用率10.4%と型1の少数派にとどまっています。

---

## データ分析①：M-5→M-6の技・持ち物採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5（9/9時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6（9/10時点）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">増減</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">+2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステルスロック採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">41.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">59.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">+18.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">だいちのちから採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">67.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">57.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-9.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">キラフロルナイト採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb">-9.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こだわりスカーフ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-5.8pt</td>
</tr>
</tbody>
</table>
</div>

M-6ではステルスロックの採用率が41.3%→59.8%と大きく伸びる一方、メガ進化（キラフロルナイト）は19.7%→10.4%とほぼ半減しました。攻撃技のだいちのちから・こだわりスカーフ型も採用率を落としています。使用率順位は18位→16位に上昇しており、これは打点を伸ばすメガ進化やスカーフより、きあいのタスキで1発耐えて確実にステルスロックを設置する型が支持を広げた結果と読み取れます。

---

## 苦手なポケモン

使用率TOP30のうち、判定対象データが存在し、かつ複数の代表型で勝敗が一致した相手のみを掲載しています。技名・採用率・確定数はいずれも代表型の判定結果をそのまま転記しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（採用率56.0%）は確定2発。相手の主力じしん（採用率67.6%）は確定2発で、2手に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）は確定2発。相手の主力じしん（採用率67.5%）は確定2発で、2手に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）は確定4発。相手の主力アイアンヘッド（採用率76.0%）は確定2発で、2手に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（採用率57.6%）は確定2発。相手の主力ラスターカノン（採用率78.8%）は確定2発で、2手に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）は確定2発。相手の主力じしん（採用率87.6%）は確定2発で、2手に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（採用率57.6%）は確定3発。相手の主力ポルターガイスト（採用率54.0%）は確定3発で、3手に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）は確定3発。相手の主力アイアンヘッド（採用率22.9%）は確定2発で、2手に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エナジーボール（採用率27.8%）は確定2発。相手の主力ウェーブタックル（採用率96.5%）は確定2発で、2手に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エナジーボール（採用率27.8%）は確定2発。相手の主力なみのり（採用率33.7%）は確定2発で、2手に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいちのちから（採用率57.6%）は確定2発。相手の主力サイコファング（採用率78.2%）は確定2発で、2手に沈められます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP30のうち、判定対象データが存在し、かつ複数の代表型で勝敗が一致した相手のみを掲載しています。技名・採用率・確定数はいずれも代表型の判定結果をそのまま転記しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">有利な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）で確定1発。相手の主力オーバーヒート（採用率22.7%）は確定2発にとどまり、1手で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）で確定1発。相手の主力ギガドレイン（採用率77.6%）は確定3発にとどまり、1手で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（採用率56.0%）で確定2発。相手の主力ふぶき（採用率69.1%）は確定3発にとどまり、2手で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（採用率80.8%）で確定2発。相手の主力シャドーボール（採用率52.9%）は確定3発にとどまり、2手で押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でキラフロルと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

同居率上位10体のうち、キラフロルの最大弱点（じめん×4）を明確に補完できる2体を取り上げます。

**ボーマンダ**（2位）はドラゴン/ひこうタイプで、じめん技を無効化できます。ガブリアスのじしんなどキラフロルを一撃で崩しうるじめん打点に対して、ボーマンダが代わりに受け出せる補完関係です。

**ゴリランダー**（9位）はくさ単タイプで、じめん技を耐性（×0.5）で受けられます。ボーマンダほど確実ではありませんが、じめん打点を受ける役割を分担できます。

その他の上位パートナーにも部分的な補完は見られます。**グソクムシャ**（3位）はじめん・みず・はがねをいずれも半減（×0.5）でき、キラフロルの×2弱点3種を最も広くカバーする補完役です。**アシレーヌ**（4位）・**セグレイブ**（8位）はみずを半減、**ギルガルド**（6位）はエスパー・はがねを半減、**ルカリオ**（7位）ははがねを半減し、それぞれ弱点の一部を分担できます。一方、**ガブリアス**・**カバルドン**・**ミミッキュ**については、キラフロルの弱点タイプに対する明確な耐性・無効を持たず、タイプ面での補完関係は確認できませんでした。

---

## まとめ

M-6のキラフロルは使用率16位で、きあいのタスキで初手を耐えつつステルスロックを設置し、パワージェム・だいちのちから・ヘドロウェーブの3タイプ複合打点で攻める型が主流です。

- **技構成はほぼ固定**：パワージェム80.8%・ステルスロック59.8%・だいちのちから57.6%・ヘドロウェーブ56.0%の4技が主軸です
- **M-5からの変化はステルスロック軸の強化**：ステルスロック採用率が41.3%→59.8%に伸びる一方、メガ進化（キラフロルナイト）は19.7%→10.4%に半減し、攻撃偏重からタスキ+設置技の型へシフトしています
- **どくげしょうは「物理技を受けるたび」発動**：接触限定ではなく、物理技全般で相手の場にどくびしを溜められます

C130の高い特殊火力を持つ一方、A55・S86・耐久並程度という種族値どおりの脆さがあり、じめん×4を筆頭にみず・エスパー・はがねの弱点を突く相手には軒並み後手に回ります。きあいのタスキで初手を耐えてステルスロックを通し、後続で弱点をカバーする構築が前提になります。

<a href="/pokemon/glimmora/">キラフロルの基礎データ・使用率ページはこちら</a>
