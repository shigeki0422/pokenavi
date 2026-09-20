---
title: '【ポケモンチャンピオンズ】ミミッキュ 考察 M-6 シーズン 使用率12位の解説'
description: 'M-6シーズン使用率12位のミミッキュを考察。ばけのかわを活かしたつるぎのまい型の型構成・実数値、ばけのかわの正確な効果、ガブリアス・セグレイブなど型別の得意/苦手をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-mimikyu-m6.png'
draft: false
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
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" />
  <div>
    <h2 style="margin:0 0 8px">ミミッキュ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">12位</strong>　特性: <strong>ばけのかわ 100%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-10時点、技・性格・持ち物などの詳細データも2026-09-10時点のスナップショットを使用しています。

M-6シーズンのミミッキュは使用率12位。ゴースト/フェアリーの複合タイプに特性ばけのかわを持ち、つるぎのまいで積んでからじゃれつく・かげうち・シャドークローで押し切るアタッカーが主軸です。じゃれつく・かげうち・シャドークローの攻撃技3つとつるぎのまいの計4技でほぼ固定されており、型ごとの違いは主に性格・EV・持ち物に現れます。

---

## ミミッキュの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">55</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">90</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:70%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:64%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">96</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">476</span>
  </div>
</div>

HP55は種族値としては低い部類ですが、後述の特性ばけのかわで1回に限り攻撃技のダメージそのものを無効化できるため、実戦での耐久はこの数値以上に評価されます。A90・S96はいずれも平均以上で、つるぎのまいで積めば高い攻撃力を発揮できます。C50は低く、特殊技を主軸にする運用には向きません。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点はゴースト・はがねの2タイプ（いずれも×2）にとどまり、ノーマル・かくとう・ドラゴンの技を無効化できる点が最大の特長です。特にかくとう・ドラゴンは環境上位に多く採用される攻撃タイプで、これらを主力とする相手には後述のばけのかわと合わせて安全に対面できます。むし技は耐性（×0.25）で軽減できます。

### 特性

<strong>ばけのかわ（100%）</strong>が全個体で採用されています。ばけたすがたの状態で技のダメージを受けると、ダメージの代わりに最大HPの1/8を消費してばれたすがたへ変わる特性です。つまり最初の1発は「ダメージを無効化し、代わりに固定の1/8HPを失う」効果であり、行動不能を防ぐ効果や回避効果ではありません。ばれたすがたに変化した後は通常どおりダメージを受けるため、実戦上の価値は「初手の1発を実質無効化できる」点に集約されます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じゃれつく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー一致のメインウェポン。10%で相手の攻撃を1段階下げる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かげうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1でゴースト一致。威力は低いが確実に先手を取って削れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃を2段階上昇。ばけのかわで1発無効化しつつ積む隙を作るのに使う</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドークロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">急所ランク+1でゴースト一致。かげうちより高火力だが優先度は通常</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のろい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の最大HPの1/2を消費し、相手をのろい状態にする（ゴーストタイプのミミッキュでの効果）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウッドハンマー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・じめん・いわ複合への打点だが与ダメージの1/3を自分も受ける</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドレインパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね複合への打点。与えたダメージの1/2を自分のHPに回復</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>トリックルーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度-7で5ターンの間、場の素早さ順を逆転させる少数派の選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+4で相手の技を1ターン防ぐ。連続使用で成功率が1/3に低下</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">命中85で相手をやけどにする。物理アタッカーの攻撃力を実質半減</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

じゃれつく・かげうち・つるぎのまい・シャドークローの4技はいずれも採用率50%を超えており、型による技構成の差はほとんどありません。性格はいじっぱり（83.0%）とようき（11.2%）に分かれますが、技構成は同一で性格・EVによる実数値の違いにとどまるため、ここでは1つの型（型1）としてまとめて扱います。

### 型1：AS特化型

**代表的な性格: いじっぱり（全体の性格採用率83.0%）／ようき（11.2%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">AS特化型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ばけのかわ（100%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32<br>
<strong>持ち物:</strong> いのちのたま（76.4%）
</div>
<div>
<strong>技構成:</strong><br>
・じゃれつく<br>
・かげうち<br>
・つるぎのまい<br>
・シャドークロー
</div>
</div>
</div>

A実数値156・S実数値148で、いのちのたま込みのじゃれつく・シャドークローで高い打点を出す構成です。つるぎのまいで積んだ後はA2段階上昇でさらに火力が伸びます。

**強み:**

A実数値**156**（いのちのたま込みでさらに上昇）で、無積みのじゃれつくでもガブリアス・セグレイブ・マスカーニャ・オオニューラなど環境上位の多くを2発圏内に収めます。つるぎのまいで積めば、無積みでは2発以上かかる耐久寄りの相手を1発圏内に落とせる場面が広がります。

**弱み:**

S実数値148のため、S149以上の相手には後手に回ります。

**性格による派生（少数派）:**

性格をようきに変えると、A実数値142・S実数値162となり、S149〜161帯の相手に先手を取れる場面が広がる一方、つるぎのまい後の最終打点はいじっぱり型（A156）にやや劣ります。ただし全体の性格採用率は11.2%にとどまり、いじっぱり（83.0%）が明確な主流です。

なお、上記4技以外では「のろい」が採用率22.0%で続きます。自分の最大HPの1/2を消費して相手をのろい状態にする技で、以後その相手は毎ターン終了時に最大HPの1/4を失い続けます。ばけのかわで初手の1発を無効化できるミミッキュと合わせ、耐久寄りの相手をじわじわ削る用途が考えられますが、シャドークロー・つるぎのまいのどちらと入れ替える構成かは技採用率の集計データからは特定できません。

---

## データ分析：技採用率の逆説

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">役割</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かげうち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">96.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力40と控えめだが優先度+1</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドークロー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">59.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">威力70で優先度は通常</td>
</tr>
</tbody>
</table>
</div>

威力だけで見ればシャドークロー（70）はかげうち（40）の1.75倍の打点があるにもかかわらず、採用率はかげうち96.1%に対してシャドークロー59.2%と大きく下回ります。これは優先度+1の価値を反映した結果です。ばけのかわで無効化できるのは1発だけで（その際に最大HPの1/8を失います）、2発目以降は通常どおりダメージを受けるため、S種族値96の実数値のままでは後手に回って撃墜されるリスクが残ります。かげうちなら素早さに関係なく確実に先手を取れるため、削り合いの終盤で相打ちを避けたり、瀕死の相手にとどめを刺す場面で優先度が威力を上回る価値を持つことが、この採用率の逆転から読み取れます。実戦では高火力が欲しい場面はシャドークロー、先手が欲しい場面はかげうちという使い分けが基本になります。

---

## 苦手なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、いのちのたま・のろいのおふだ・ピントレンズの3構成（いずれもS148のいじっぱり型1前提）で勝敗が一致した相手のみを掲載します。型1のようき派生（S162）やのろい採用構成ではこの検証を行っておらず、素早さ関係が変わる相手（メガリザードンYなど）や技構成が異なる相手では結論が反転する場合があります。

なお、はがね/ゴーストのギルガルド（使用率10位）とはがね/フェアリーのキラフロル（16位）は、ミミッキュの弱点2タイプを一致技で突ける相手ですが、双方とも相手の持ち物（たべのこし/のろいのおふだ、きあいのタスキ/ふうせん）によって検証結果の勝敗が割れたため、苦手・得意のどちらの表にも掲載していません。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（採用率98.1%）は2発圏内までしか落とせず、メガボーマンダ（S172）はミミッキュ（S148）より素早いため、同じ2発圏内のすてみタックル（採用率73.4%）で先に押し切られます。なお特性スカイスキンによりすてみタックルはひこうタイプ技として扱われるため、タイプ相性表の「ノーマル無効」は適用されません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速さではミミッキュ（S148）がメガグソクムシャ（S60）を上回りますが、シャドークロー（採用率59.2%）ではメガグソクムシャを確定数圏内に収められない一方、こちらははがね×2弱点のアイアンヘッド（採用率76.0%）2発で沈められてしまい、先手を取っても確定数で負けます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオZ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（ルカリオナイトZ採用率93.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（採用率98.1%）は2発圏内までしか落とせず、メガルカリオZ（S223）はミミッキュ（S148）より素早いため、同じ2発圏内のラスターカノン（採用率78.8%）で先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（S105〜150）に対し、じゃれつく（採用率98.1%）ではブリジュラスを確定数圏内に収められず、逆にラスターカノン（採用率75.1%）に2〜3発で押し切られます。S150の個体にはミミッキュ（S148）が後手に回ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴリランダーは特性グラスメイカー（採用率99.7%）下でグラススライダー（採用率94.5%）が優先度+1になるため、素早さで勝るミミッキュでも先制されます。じゃれつく（採用率98.1%）ではゴリランダーを倒すのに3発かかる一方、こちらはグラススライダー3発・ドラムアタック（採用率39.1%）なら2発で沈められ、確定数で負けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アーマーガア（S78〜87）にはミミッキュ（S148）が先手を取れますが、シャドークロー（採用率59.2%）ではアーマーガアを確定数圏内に収められず、逆に主力ブレイブバード（採用率37.6%）でこちらが先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ミミッキュがいのちのたま型の場合でもじゃれつくは2発圏内にとどまり、メガリザードンX（S167）はミミッキュ（S148）より素早いため、同じ2発圏内のフレアドライブ（採用率36.5%）で先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドークロー（採用率59.2%）は2発圏内までしか落とせず、メガリザードンY（S152）はミミッキュ（S148）より素早いため、同じ2発圏内のかえんほうしゃ（採用率42.9%）で先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位（メタグロスナイト採用率98.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1のバレットパンチ（採用率90.1%）で素早さに関係なく先手を取られ、2発で押し切られます（メガメタグロスはS162でミミッキュのS148も上回るため、シャドークロー（採用率59.2%）の2発が間に合いません）</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP35を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、いのちのたま・のろいのおふだ・ピントレンズの3構成（いずれもS148のいじっぱり型1前提）で勝敗が一致した相手のみを掲載します（苦手表より母集団を広くTOP35としているのは、得意側に該当する相手がTOP30内に少なく、TOP35まで対象を広げて確認したためです）。型1のようき派生（S162）やのろい採用構成ではこの検証を行っておらず、素早さ関係が変わる相手や技構成が異なる相手では結論が反転する場合があります。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（採用率98.1%）がガブリアスの主力じしん（採用率67.6%）を打点で上回り、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位（セグレイブナイト採用率51.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速さで勝る場面が多く、じゃれつく（採用率98.1%）でセグレイブの技（優先度+1のこおりのつぶて〈採用率82.4%〉を含む、ミミッキュへの最大打点はつららおとし〈採用率43.3%〉）より先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速さで勝り、シャドークロー（採用率59.2%）でサーフゴーの主力シャドーボール（採用率99.9%）より先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャ（S175〜262）はミミッキュ（S148）より素早く後手になりますが、じゃれつく→優先度+1のかげうちの順で決めることで、マスカーニャのトリプルアクセル（採用率90.1%）より先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">イダイトウ(メス)（S130〜195）はミミッキュ（S148）より素早い場合があり後手になりますが、シャドークロー→優先度+1のかげうちの順で決めることで、主力おはかまいり（採用率99.7%）より先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手になりますが、れいとうビーム（採用率92.9%）に3発耐えてじゃれつく（採用率98.1%）2発で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手になりますが、フェイタルクロー（採用率94.7%）に3発耐えてじゃれつく（採用率98.1%）2発で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位（カイリュナイト採用率75.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特性マルチスケイルでHP満タン時の初撃ダメージが半減される点を踏まえても、後手になりますが、かえんほうしゃ（採用率66.8%）に3発耐えてじゃれつく（採用率98.1%）2発で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パーモット（S172〜235）はミミッキュ（S148）より素早く後手になりますが、じゃれつく→優先度+1のかげうちの順で決めることで、主力でんこうそうげき（採用率85.1%、優先度技ではない通常のでんき技）より先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手になりますが、多数派のこだわりスカーフ型（きあいのタスキ非採用）が放つあくのはどう（採用率98.3%、ミミッキュへは等倍）を安全に受けつつ、じゃれつく（採用率98.1%、サザンドラへはフェアリー×4）1発（確定）で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">多数派のこだわりスカーフ型（S220）には後手ですが、ワイドフォース（採用率99.4%）ではミミッキュを3発必要とする一方、こちらはいのちのたま型ならじゃれつく（採用率98.1%）1発で押し切れます（のろいのおふだ・ピントレンズ型は2発）</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でミミッキュと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" loading="lazy">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

同居率上位10体のうち、明確な耐性・無効によるタイプ補完、または選出構築上の役割分担が確認できる4体を取り上げます（「等倍で受けられる」といった耐性を伴わない相性は補完の根拠にならないため対象外とします）。

**ガブリアス**（1位）はドラゴン/じめんタイプです。ミミッキュはノーマル・かくとう・ドラゴンの技を無効化できるため、ガブリアスを突破しようとするこれらのタイプの攻撃技に対して、ガブリアスに代わって安全に受け出せる役割を担えます。

**ボーマンダ**（2位）はドラゴン/ひこうタイプです。ミミッキュはドラゴン技を無効化できるため、ボーマンダを狙うドラゴン打点の相手に対して受け出し先を分担できます。

**カバルドン**（3位）はじめん単タイプです。タイプ面での明確な耐性補完はありませんが、あくびによる交代誘導とステルスロックの設置役を担い、カバルドンが場を動かしている間にミミッキュを後続として対面に出せる、選出構築上の役割分担があります。

**グソクムシャ**（5位）は通常時むし/みず、グソクムシャナイト採用率98.9%でほぼ全個体がメガ進化し、メガ進化後はむし/はがねタイプになります。メガ進化後のグソクムシャは、はがね技を耐性（×0.25）で受けられます。これはミミッキュの弱点であるはがね技への耐性を持つため、ミミッキュが受けにくいはがね打点をグソクムシャが引き受けられる明確な補完関係です。

---

## まとめ

M-6のミミッキュは使用率12位で、じゃれつく・かげうち・つるぎのまい・シャドークローの4技構成がほぼ固定される、シンプルで完成度の高いアタッカーです。

- **技構成はほぼ固定**：じゃれつく98.1%・かげうち96.1%・つるぎのまい79.8%・シャドークロー59.2%の4技が主軸で、型の違いは性格・EV・持ち物に表れます
- **威力とは逆転する優先度技の価値**：かげうち（威力40）がシャドークロー（威力70）を採用率で大きく上回るのは、優先度+1で確実に先手を取れる価値がHP55の低耐久を補うためです
- **ばけのかわは「無効化して1/8HP消費」**：行動不能を防ぐ効果ではなく、ダメージそのものを1回無効化しつつ固定の割合HPを失う特性です

ノーマル・かくとう・ドラゴンを無効化できる守備範囲を土台に、つるぎのまいで積んでから押し切るか、かげうちで先手を確保して削り切るかの使い分けが基本の立ち回りです。ゴースト・はがねへの弱点は環境上位に存在するため、選出段階でのケアが引き続き求められます。
