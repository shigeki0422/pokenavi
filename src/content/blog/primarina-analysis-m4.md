---
title: '【ポケモンチャンピオンズ】アシレーヌ 考察 M-4 シーズン アンコール軸の採用実態'
description: 'M-4シーズン使用率7位のアシレーヌを考察。M-3の13位から浮上し、たべのこし採用率27.7%・れいせい19.3%と耐久寄りの構築が増加。めいそう積み型22.8%に対しアンコール型46.7%が多数派という採用率の逆説をデータで解説します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
heroImage: '../../assets/hero-primarina-m3.png'
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
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
  <div>
    <h2 style="margin:0 0 8px">アシレーヌ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>（M-3: 13位）　特性: <strong>げきりゅう 95.8%</strong>
    </div>
  </div>
</div>

M-4シーズン、アシレーヌはM-3の13位から使用率7位へ浮上しました。みず/フェアリーの複合タイプにムーンフォース・うたかたのアリア・アクアジェットの3技を軸とする構成はM-3から継続しており、C126という高い特殊火力とアンコールによる相手の行動制限を両立させる汎用アタッカーです。技構成は共通する一方、持ち物・性格の分布はM-3から明確に変化しています。

---

## アシレーヌの基本スペック

### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:53%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:49%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:49%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:84%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">126</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">116</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="min-width:40px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

C126・D116の特殊耐久ラインが高く、A74・B74と物理面は平均的です。S60は環境上位の多くに先手を取られる数値で、耐えてから打ち返す立ち回りが基本になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン
  </td>
</tr>
</tbody>
</table>
</div>

弱点はどく・くさ・でんきの3タイプ（いずれも×2）。耐性は6タイプに及び、あく・ほのおへの半減とドラゴン無効が持ち味です。M-4使用率6位のマスカーニャ（くさ/あく）はトリックフラワー（くさ・威力70）を97.3%採用しており、くさ×2弱点を突かれやすい相手として上位に存在します。

### 特性

**げきりゅう（95.8%）**が固定に近い水準で採用されています。HPが最大の1/3以下になると、みずタイプの技（うたかたのアリア・アクアジェット・なみのり）の威力が1.5倍になる特性です。フェアリータイプのムーンフォースは対象外のため、げきりゅう発動下でもムーンフォースの威力は変わりません。もう一方の**うるおいボイス**（4.2%）は音技をみずタイプに変える特性ですが、採用率は少数にとどまります。

---

## M-4の採用型

### 型1：アタッカー型（めいそう積み）

**代表的な性格: ひかえめ（全体の性格採用率61.3%）**　※この採用率はアシレーヌ全体の性格分布であり、めいそう採用率（22.8%）とは別の指標です

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アタッカー型（めいそう積み）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（95.8%）<br>
<strong>性格:</strong> ひかえめ（C↑ S↓）<br>
<strong>EV:</strong> H32-C32-S2<br>
<strong>持ち物:</strong> オボンのみ（47.0%）
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・うたかたのアリア<br>
・アクアジェット<br>
・めいそう
</div>
</div>
</div>

ムーンフォース（フェアリー・威力95）とうたかたのアリア（みず・威力90、命中した相手のやけどを治す効果あり）の2タイプ打点に、めいそう（C・D各1段階上昇）で火力と耐久を同時に伸ばす構成です。アクアジェット（みず・威力40・優先度+1）は削り合いで先手の一撃を確保する役割を持ちます。

**強み:**

ひかえめ・EV H32-C32-S2のC実数値は**195**（HP187・S73）。めいそうを1回でも積めればC・D共に1段階上昇し、以降の打点と受けの両面が型2より高くなります。

**弱み:**

アンコールを持たないため、相手の積み技や補助技を縛れず、めいそうを積む隙を能動的に作れません。S73は環境上位の多くに先手を取られる数値で、積む前に大きく削られると本来の火力を発揮できません。

**性格の分岐: れいせい（19.3%）**

M-4では、ひかえめに次いで多い性格としてれいせい（C↑S↓）が19.3%採用されています。ひかえめとの違いはA低下かS低下かのみで、技構成・運用方針はどちらも本節のアタッカー型に含まれます。S60・S73は元々環境上位の多くに先手を取られる数値のため、S個体値を切り捨てC・HPに配分を回す考え方がれいせいの増加につながっています。

---

### 型2：耐久型（ずぶとい・B投資）

**代表的な性格: ずぶとい（全体の性格採用率10.9%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久型（ずぶとい・B投資）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（95.8%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B29-C4-D1<br>
<strong>持ち物:</strong> たべのこし（27.7%）
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・うたかたのアリア<br>
・アンコール<br>
・クイックターン
</div>
</div>
</div>

アンコール（相手を直前の技に固定する）で積み技や補助技のターンを潰し、クイックターン（みず・威力60、攻撃後に交代）で後続への引き継ぎを行う型です。めいそうを積まない分、ムーンフォース・うたかたのアリアの一致技をそのまま押し付けます。

アンコール自体の技採用率は46.7%と高いものの、性格別の内訳は公開されていません。ひかえめが性格全体の61.3%を占める以上、アンコールを持つ個体の相当数は型1のひかえめ・れいせい寄りの配分だと考えられ、「アンコール＝ずぶとい耐久型」に限った技ではない点に注意が必要です。ずぶとい・B投資の型はその中でも数値上10.9%の少数派で、めいそうを切ってB実数値を優先した耐久寄りの選択肢にあたります。

**強み:**

B寄りEVでB実数値**135**（型1のB94より+41）。物理技への耐久が上がり、アンコールで相手の行動を縛りながら受け出しやすくなります。クイックターンで後続に負担をかけずに対面を変えられる点も型1にはない選択肢です。

**弱み:**

C実数値は**150**（型1のC195より-45）で、めいそうによる火力上昇もないため、後半の打点は型1に劣ります。

---

## データ分析①：M-3→M-4 採用データの変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>7位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>27.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+11.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">58.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">47.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-11.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいせい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">0.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>19.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+18.5pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-9.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>46.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.7pp</td>
</tr>
</tbody>
</table>
</div>

使用率が13位から7位へ上昇した裏で、持ち物・性格の分布は耐久寄りに変化しています。たべのこし（+11.8pp）とオボンのみ（-11.0pp）の入れ替わりは、1発の回復量より毎ターン確実に回復する持続戦を選ぶ構築が増えたことを示します。れいせい（C↑S↓）の急伸（+18.5pp）はS個体値を切り捨ててC・HPを厚くする配分の増加を反映していますが、ひかえめ（61.3%）は依然として過半数を占めており、C重視のアタッカー方向自体は変わっていません。ひかえめ一強かられいせいへの分散が進んだ、と捉えるのが実態に近い変化です。

---

## データ分析②：めいそう採用率とアンコール採用率の逆説

M-4の技採用率で見ると、めいそう（22.8%）はアシレーヌの代名詞のように語られがちですが、実際の技採用率はアンコール（46.7%）を下回っています。ただしこれは性格別の型分布と単純には一致しません。性格採用率ではひかえめ（61.3%）が過半数を占めており、アンコール採用者の相当数はこのひかえめ寄りの配分だと考えられます。つまりアンコールは「ずぶといの耐久型だけの技」ではなく、ひかえめの攻撃型でも幅広く採用されている汎用技であり、めいそうを積む型・積まない型のどちらでも相手の1手を縛る目的で選ばれている実態がうかがえます。

---

## 苦手なポケモン

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
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・威力70・採用率97.3%）がくさ×2弱点。物理技のため型2のB135でも大きく削られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんじほう（でんき・威力120・採用率96.6%）がでんき×2弱点。命中不安はあるものの、通れば型1のD136でも一撃で崩されます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・威力90・採用率55.3%）がでんき×2弱点。ボルトチェンジ（採用率90.6%）で打点を与えつつ後続に交代する構成が多く、対面を長く維持されにくい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・威力95・採用率55.7%）がどく×2弱点。主力のシャドーボール（採用率86.8%）は等倍止まりですが、ヘドロウェーブのほうが実効打点は高くなります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・威力95・採用率55.1%）がどく×2弱点かつ一致技。ステルスロック（採用率49.1%）も並行して展開されるため長期戦で削られやすくなります</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でアシレーヌと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" loading="lazy">
    <div class="name">マフォクシー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**メタグロス**（1位、メガメタグロスの詳細は[メガメタグロスのM-4考察](/blog/metagross-analysis-m4/)を参照）ははがね/エスパーで、アシレーヌの弱点であるどく技を無効化できます。一方でメタグロスの弱点であるほのお・じめん・ゴースト・あくのうち、ほのお・あくはアシレーヌがみずタイプで半減して受けられます。アシレーヌはメタグロスが苦手な2タイプを肩代わりできる組み合わせです。

**ガブリアス**（2位）はドラゴン/じめんで、アシレーヌはドラゴン技を無効で受けられます。逆にアシレーヌの弱点であるでんき技はガブリアスがじめんタイプで無効化でき、こおり技もアシレーヌが半減で受けられるため、でんき・こおりを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**カバルドン**（3位）はじめん/あくで、あくびによる交代誘導とステルスロックの設置役を担います。カバルドンが場を動かしている間にアシレーヌを後続として対面に出せる、選出構築上の役割分担です。

**ミミッキュ**（4位）はゴースト/フェアリーで、アシレーヌの弱点（どく・くさ・でんき）を半減・無効にする耐性は持たず、互いのタイプ相性を補完する関係ではありません。同居の理由はタイプ受けではなく、ばけのかわで一度は攻撃を無効化して起点を作れるミミッキュと、C126の高火力で後続に負担をかけられるアシレーヌを併用し、選出時にどちらかを場に残しやすくする構築上の噛み合わせです。

**マスカーニャ**（6位）はくさ/あくで、アシレーヌの弱点であるくさタイプをマスカーニャ自身も内包するため弱点の分散にはなりませんが、マスカーニャのはたきおとす（あく）でアシレーヌが半減できないどくタイプの持ち物破壊などを分担し、役割を分けて選出できます。

---

## まとめ

M-4のアシレーヌはM-3の13位から7位へ使用率を伸ばし、耐久寄りの構築へシフトしたシーズンです。

- **使用率13位→7位**：技構成（ムーンフォース・うたかたのアリア・アクアジェット）は継続しつつ、持ち物・性格の分布が変化
- **たべのこし+11.8pp・れいせい+18.5pp**：1発回復のオボンのみから持続回復のたべのこしへ、また最速志向のひかえめからS無振りのれいせいへ、耐久寄りの配分が増加（ひかえめ自体は61.3%で依然過半数）
- **めいそう採用率22.8%に対しアンコール採用率46.7%**：ただしアンコールは性格を問わず広く採用されており、「ずぶといの耐久型専用技」ではない点に注意

C126・D116の高い特殊耐久ラインを土台に、めいそうで一気に押し切るか、アンコールで相手の行動を縛りながら立ち回るかは、パーティ内での役割に応じた選択になります。どく・くさ・でんきの3弱点は環境上位に広く存在するため、選出段階でのケアが引き続き求められます。
