---
title: '【ポケモンチャンピオンズ】アシレーヌ 考察 M-5 シーズン めいそう採用率が過去最高に'
description: 'M-5シーズン使用率2位のアシレーヌを考察。めいそう採用率が22.8%から過去最高の38.4%へ急伸し、ひかえめが70.0%まで上昇。ねむる・カゴのみの組み合わせが新たに浮上した実態をデータで解説します。'
pubDate: '2026-08-10'
updatedDate: '2026-08-10'
heroImage: '../../assets/hero-primarina-m5.png'
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
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" />
  <div>
    <h2 style="margin:0 0 8px">アシレーヌ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">2位</strong>（M-4: 6位）　特性: <strong>げきりゅう 96.5%</strong>
    </div>
  </div>
</div>

M-5シーズン、アシレーヌは使用率2位まで浮上しました。みず/フェアリーの複合タイプにムーンフォース・うたかたのアリア・アクアジェットを主軸とする技構成はM-4から継続していますが、めいそうの採用率が大きく伸び、C126という高い特殊火力を積み技で伸ばして押し切る方向性が強まっています。持ち物・性格の分布もM-4から変化しており、後述のデータ分析で詳しく扱います。

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

弱点はどく・くさ・でんきの3タイプ（いずれも×2）。耐性は6タイプに及び、あく・ほのおへの半減とドラゴン無効が持ち味です。M-5使用率4位のマスカーニャ（くさ/あく）はトリックフラワー（くさ・威力70）を96.9%採用しており、くさ×2弱点を突かれやすい相手として上位に存在します。

### 特性

**げきりゅう（96.5%）**がほぼ固定で採用されています。HPが最大の1/3以下になると、みずタイプの技（うたかたのアリア・アクアジェット・クイックターン・なみのり）の威力が1.5倍になる特性です。フェアリータイプのムーンフォースは対象外のため、げきりゅう発動下でもムーンフォースの威力は変わりません。もう一方の**うるおいボイス**（3.5%）は音技をみずタイプに変える特性ですが、採用率は少数にとどまります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ムーンフォース</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー一致のメインウェポン。10%で相手のとくこう低下</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>うたかたのアリア</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致。命中した相手のやけどを治す。げきりゅう発動下で威力1.5倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">71.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。S60の遅さを補い削り合いで先手を確保</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>41.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に固定。積み技・補助技のターンを潰す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>38.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう・とくぼうを1段階ずつ上昇。火力と耐久を同時に強化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。アンコールで縛った後の後続への引き継ぎに使う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねむる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HPと状態異常を全回復し2ターンねむり状態になる。カゴのみとの併用で行動不能ターンを圧縮</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリアと同威力のみず技。やけど回復効果はない代わりの選択肢</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミストフィールド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5ターンの間、場にいる全ポケモンの状態異常を防ぐのが主目的（特にカバルドンのあくび対策）。ドラゴン技半減もおまけで付くが、アシレーヌ自身はドラゴン無効のためこちらの恩恵は薄い。少数派の選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス等のドラゴン/じめん複合への打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-5の採用型

### 型1：アタッカー型（めいそう積み）

**代表的な性格: ひかえめ（全体の性格採用率70.0%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アタッカー型（めいそう積み）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（96.5%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32-C32-S2<br>
<strong>持ち物:</strong> オボンのみ（46.1%）
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

ムーンフォース（フェアリー・威力95）とうたかたのアリア（みず・威力90、命中した相手のやけどを治す効果あり）の2タイプ打点に、めいそう（C・D各1段階上昇）で火力と耐久を同時に伸ばす構成です。アクアジェット（みず・**物理**・威力40・優先度+1）はA無振り・ひかえめ補正でA実数値84にとどまるため大きな打点にはなりませんが、優先度+1できあいのタスキ・瀕死寸前の相手を確実に仕留める役割を持ちます。

**強み:**

ひかえめ・EV H32-C32-S2のC実数値は**195**（HP187・S82）。めいそうを1回でも積めればC・D共に1段階上昇し、以降の打点と受けの両面が型2より高くなります。

**弱み:**

アンコールを持たないため、相手の積み技や補助技を縛れず、めいそうを積む隙を能動的に作れません。

---

### 型2：耐久型（ずぶとい・B投資）

**代表的な性格: ずぶとい（全体の性格採用率10.0%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">耐久型（ずぶとい・B投資）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（96.5%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B29-C4-D1<br>
<strong>持ち物:</strong> たべのこし（22.6%）
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

アンコール（相手を直前の技に固定する）で積み技や補助技のターンを潰し、クイックターン（みず・**物理**・威力60、攻撃後に交代）で後続への引き継ぎを行う型です。クイックターンもA無振りで打点は小さく、対面操作が主目的です。めいそうを積まない分、ムーンフォース・うたかたのアリアの一致技をそのまま押し付けます。

このEV配分（H32-B29-C4-D1）の採用率は3.1%で、M-4時点の8.2%から低下しています。アンコール自体の技採用率は41.3%と依然として高く、めいそうを積まずアンコールを軸にするひかえめ個体も一定数存在すると考えられます。

**強み:**

B寄りEVでB実数値**135**（型1のB94より+41）。物理技への耐久が上がり、アンコールで相手の行動を縛りながら受け出しやすくなります。クイックターンで後続に負担をかけずに対面を変えられる点も型1にはない選択肢です。

**弱み:**

C実数値は**150**（型1のC195より-45）で、めいそうによる火力上昇もないため、後半の打点は型1に劣ります。

---

### 型3：回復型（ねむる・カゴのみ）

**代表的な性格: ずぶとい（全体の性格採用率10.0%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">回復型（ねむる・カゴのみ）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（96.5%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B32-C2<br>
<strong>持ち物:</strong> カゴのみ（11.6%）
</div>
<div>
<strong>技構成:</strong><br>
・ムーンフォース<br>
・うたかたのアリア<br>
・アクアジェット<br>
・ねむる
</div>
</div>
</div>

データ分析（後述）で見るように、ねむる（採用率11.9%）とカゴのみ（採用率11.6%）はM-5で新たに浮上し、採用率がほぼ一致していることから連動した運用と推測されます。ねむるはHPと状態異常を全回復して2ターンねむり状態になる技で、カゴのみは自身のねむり状態を回復するきのみです。ねむるを使った直後にカゴのみでねむり状態を解除すれば、本来2ターンかかる行動不能を圧縮しながら全回復できます。この耐久力を活かすため、性格・EVは型2と同じくB寄りの分布と親和的です（H32-B32-C2 ずぶといのB実数値**138**）。

**強み:**

アンコールでの縛りやめいそうでの積みに頼らず、ねむる＋カゴのみの1回に限り、本来2ターンかかる行動不能を1ターンに圧縮しながらHPと状態異常（やけど・まひ・どく・こおり）を全回復できます。起き上がりが即時のため、こおり・まひ等の状態異常を受けても1度は立て直せる構成です。

**弱み:**

カゴのみは1度使うと消費されるため全回復の圧縮効果は1回限りで、2回目以降のねむるは通常どおり2ターンの行動不能になります。またねむるを使うターン自体は攻撃に使えないため、その1回で攻撃機会を失います。ねむるはHPが満タンだと失敗するため、アンコールで縛られると腐りやすい点にも注意が必要です。C実数値は**148**（EV2・ずぶといでC無補正）で型1のC195に劣り、打点は型2のC150とほぼ同水準にとどまります。

---

## データ分析：M-4→M-5 採用データの変化

※M-4列のデータは2026-07-13時点、M-5列のデータは2026-08-10時点（いずれもDBで参照可能な最も完全なスナップショット）を使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>2位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>38.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+15.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>70.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+8.7pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいせい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.7pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">46.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.4pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねむる採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">TOP10圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>11.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新規浮上</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-5.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カゴのみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>11.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+8.4pp</td>
</tr>
</tbody>
</table>
</div>

M-4では、ひかえめかられいせいへS個体値を切り捨てる動きとたべのこしの増加が同時に進み、耐久寄りの分布へ変化していました。M-5ではこの流れが反転し、ひかえめ（+8.7pp）とめいそう（+15.6pp）がともに伸びる一方、れいせい（-5.7pp）・アンコール（-5.4pp）・たべのこし（-5.1pp）は軒並み低下しています。アンコールで縛ってから受け出す立ち回りより、めいそうを積んでC・Dを底上げし押し切る立ち回りへ比重が移ったことが、使用率6位から2位への上昇を支える一因になっています。

もう1点、クイックターン（-6.4pp）とほぼ入れ替わる形でねむる（11.9%）とカゴのみ（11.6%）が採用率を伸ばしています。ねむるはHPと状態異常を全回復して2ターンねむり状態になる技で、カゴのみはねむり状態を回復するきのみです。両者の採用率がほぼ一致していることから、ねむるで全回復した直後にカゴのみで自身のねむり状態を解除し、行動不能ターンを圧縮しながら回復する運用が広がっていると考えられます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">トリックフラワー（くさ・威力70・採用率96.9%）がくさ×2弱点。必中・必ず急所の仕様を持つ技で、耐久型（B投資でB135）で受けても弱点補正込みのダメージが重く、こだわりスカーフ55.2%で先手も取られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガライチュウY（ライチュウナイトY採用率97.2%）はノーガードでんじほう（でんき・威力120）が必中。型1のD136に対しても高乱数2発（最大138、HP187の約74%）まで削られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（でんき・威力90・採用率51.9%）がでんき×2弱点の最大打点。ハイドロポンプ（採用率99.1%）はみず半減で受けられますが、おにび（採用率74.3%）も高採用で、こだわりスカーフ26.5%を持たれるとS実数値で上を取られる場合もあります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガゲンガー（ゲンガナイト採用率80.6%）はかげふみで交代を封じてくるため、ヘドロウェーブ（どく・威力95・採用率74.6%、どく×2弱点）を安全に受けられません。主力のシャドーボール（採用率88.3%）は等倍止まりです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく・威力95・採用率61.6%）がどく×2弱点。ステルスロック（採用率36.7%）も並行して展開されるため長期戦で削られやすくなります</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-5でアシレーヌと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" loading="lazy">
    <div class="name">ゲンガー</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、アシレーヌはドラゴン技を無効で受けられます。逆にアシレーヌの弱点であるでんき技はガブリアスがじめんタイプで無効化でき、こおり技もアシレーヌが半減で受けられるため、でんき・こおりを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**メタグロス**（2位、メガメタグロスの詳細は[メガメタグロスのM-4考察](/blog/metagross-analysis-m4/)を参照）ははがね/エスパーで、アシレーヌの弱点であるどく技を無効化できます。一方でメタグロスの弱点であるほのお・じめん・ゴースト・あくのうち、ほのお・あくはアシレーヌがみずタイプで半減して受けられます。アシレーヌはメタグロスが苦手な2タイプを肩代わりできる組み合わせです。

**カバルドン**（3位）はじめん単タイプで、あくびによる交代誘導とステルスロックの設置役を担います。カバルドンが場を動かしている間にアシレーヌを後続として対面に出せる、選出構築上の役割分担です。

**マスカーニャ**（5位）はくさ/あくで、くさタイプの技を自身の耐性（×0.5）で受けられます。アシレーヌの弱点であるくさ技を持つ相手には、マスカーニャに受け出すことで弱点を分散できます。

---

## まとめ

M-5のアシレーヌはM-4の6位から2位へ使用率を伸ばし、めいそう積みを軸とするアタッカー方向へシフトしたシーズンです。

- **使用率6位→2位**：技構成（ムーンフォース・うたかたのアリア・アクアジェット）は継続しつつ、めいそう・性格・持ち物の分布が変化
- **めいそう+15.6pp・ひかえめ+8.7pp**：M-4で進んだ耐久寄りの分布（れいせい・たべのこし・アンコール偏重）から、積み技でC・Dを底上げする方向へ過去最高水準までシフト
- **ねむる11.9%・カゴのみ11.6%が新たに浮上**：ほぼ一致する採用率から、ねむるで全回復した直後にカゴのみで自身のねむり状態を解除する運用が広がったと考えられる

C126・D116の高い特殊耐久ラインを土台に、めいそうで一気に押し切るか、アンコールで相手の行動を縛りながら立ち回るかは、パーティ内での役割に応じた選択になります。どく・くさ・でんきの3弱点は環境上位に広く存在するため、選出段階でのケアが引き続き求められます。

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/primarina/)**
