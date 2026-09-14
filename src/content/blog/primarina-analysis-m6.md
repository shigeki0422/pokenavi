---
title: '【ポケモンチャンピオンズ】アシレーヌ 考察 M-6 シーズン 使用率3位の解説'
description: 'M-6シーズン使用率3位のアシレーヌを考察。みず/フェアリーの複合タイプとムーンフォース・うたかたのアリアを軸に、クイックターン採用率がM-5から+5.6ppずぶといが+3.6pp上昇した実態、ガブリアス・カバルドンなど型別の得意/苦手をデータで解説します。'
pubDate: '2026-09-14'
updatedDate: '2026-09-14'
heroImage: '../../assets/hero-primarina-m6.png'
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
      使用率: <strong style="color:#e67e22">3位</strong>（M-5: 2位）　特性: <strong>げきりゅう 97.5%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位は2026-09-14時点、技・性格・持ち物などの詳細データは2026-09-10時点のスナップショットを使用しています。

M-6シーズンのアシレーヌは使用率3位。みず/フェアリーの複合タイプに、ムーンフォース・うたかたのアリア・アクアジェットを主軸とする技構成はM-5から継続していますが、クイックターンとずぶといの採用率が伸びるなど、対面操作・耐久寄りの分布がやや強まっています。この変化は後述のデータ分析で詳しく扱います。

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

弱点はどく・くさ・でんきの3タイプ（いずれも×2）。耐性は6タイプに及び、あく・ほのおへの半減とドラゴン無効が持ち味です。使用率4位のグソクムシャはアイアンヘッド（はがね・威力80、採用率76.0%）を主力にしており等倍止まりですが、後述の苦手表のとおり打点勝負では押し負けており「等倍止まり＝有利」ではありません。こちらの3弱点はいずれも環境上位に存在するため選出段階でのケアが引き続き必要です。

### 特性

**げきりゅう（97.5%）**がほぼ固定で採用されています。HPが最大の1/3以下になると、みずタイプの技（うたかたのアリア・アクアジェット・クイックターン・なみのり）の威力が1.5倍になる特性です。フェアリータイプのムーンフォースは対象外のため、げきりゅう発動下でもムーンフォースの威力は変わりません。もう一方の**うるおいボイス**（2.5%）は音技をみずタイプに変える特性ですが、採用率は少数にとどまります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー一致のメインウェポン。10%で相手のとくこう低下</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>うたかたのアリア</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">92.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致。命中した相手のやけどを治す。げきりゅう発動下で威力1.5倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">71.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。S60の遅さを補い削り合いで先手を確保</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アンコール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>43.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を直前の技に固定。積み技・補助技のターンを潰す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>めいそう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>33.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">とくこう・とくぼうを1段階ずつ上昇。火力と耐久を同時に強化</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>クイックターン</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。アンコールで縛った後の後続への引き継ぎに使う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねむる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HPと状態異常を全回復し2ターンねむり状態になる。カゴのみとの併用で行動不能ターンを圧縮</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリアと同威力のみず技。やけど回復効果はない代わりの選択肢</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ミストフィールド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5ターンの間、地面にいる自陣ポケモンの状態異常・混乱を防ぐのが主目的（特にカバルドンのあくび対策）。ドラゴン技半減もおまけで付くが、アシレーヌ自身はドラゴン無効のためこちらの恩恵は薄い。少数派の選択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス等のドラゴン/じめん複合への打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：アタッカー型（めいそう積み）

**代表的な性格: ひかえめ（全体の性格採用率67.9%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">アタッカー型（めいそう積み）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（97.5%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H32-C32-S2<br>
<strong>持ち物:</strong> オボンのみ（41.2%）
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

ムーンフォース（フェアリー・威力95）とうたかたのアリア（みず・威力90、命中した相手のやけどを治す効果あり）の2タイプ打点に、めいそう（C・D各1段階上昇）で火力と耐久を同時に伸ばす構成です。アクアジェット（みず・**物理**・威力40・優先度+1）はA無振り・ひかえめ補正でA実数値84にとどまるため大きな打点にはなりませんが、優先度+1できあいのタスキで耐えた相手や瀕死寸前の相手に、後手を取らず追撃を入れられる役割を持ちます。

**強み:**

ひかえめ・EV H32-C32-S2のC実数値は**195**（HP187・S82）。めいそうを1回でも積めればC・D共に1段階上昇し、以降の打点と受けの両面が型2より高くなります。

**弱み:**

アンコールを持たないため、相手の積み技や補助技を縛れず、めいそうを積む隙を能動的に作れません。

---

### 型2：対面操作型（アンコール・クイックターン）

**代表的な性格: ずぶとい（全体の性格採用率12.1%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">対面操作型（アンコール・クイックターン）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（97.5%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B20-C14<br>
<strong>持ち物:</strong> たべのこし（20.9%）
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

**強み:**

B寄りEVでB実数値**125**（型1のB94より+31）。物理技への耐久が上がり、アンコールで相手の行動を縛りながら受け出しやすくなります。クイックターンで後続に負担をかけずに対面を変えられる点も型1にはない選択肢です。

**弱み:**

C実数値は**160**（型1のC195より-35）で、めいそうによる火力上昇もないため、後半の打点は型1に劣ります。

---

### 型3：回復型（ねむる・カゴのみ）

**代表的な性格: ずぶとい（全体の性格採用率12.1%）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">回復型（ねむる・カゴのみ）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> げきりゅう（97.5%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32-B32-C2<br>
<strong>持ち物:</strong> カゴのみ（12.7%）
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

ねむる（採用率12.6%）とカゴのみ（採用率12.7%）はほぼ一致する採用率で連動した運用と推測されます。ねむるはHPと状態異常を全回復して2ターンねむり状態になる技で、カゴのみは自身のねむり状態を回復するきのみです。ねむるを使った直後にカゴのみでねむり状態を解除すれば、本来2ターンかかる行動不能を圧縮しながら全回復できます。この耐久力を活かすため、性格・EVは型2と同じくB寄りの分布と親和的です。

**強み:**

アンコールでの縛りやめいそうでの積みに頼らず、ねむる＋カゴのみの1回に限り、本来2ターンかかる行動不能を1ターンに圧縮しながらHPと状態異常（やけど・まひ・どく・こおり）を全回復できます。起き上がりが即時のため、こおり・まひ等の状態異常を受けても1度は立て直せる構成です。B実数値**138**（型1のB94より+44）で受け出しやすさも型1を上回ります。

**弱み:**

カゴのみは1度使うと消費されるため全回復の圧縮効果は1回限りで、2回目以降のねむるは通常どおり2ターンの行動不能になります。またねむるを使うターン自体は攻撃に使えないため、その1回で攻撃機会を失います。ねむるはHPが満タンだと失敗するため、アンコールで縛られると腐りやすい点にも注意が必要です。C実数値は**148**（型1のC195より-47）で、型2のC160よりもさらに打点が下がります。

---

## データ分析：M-5→M-6 採用データの変化

※M-5列のデータはM-5シーズン最終スナップショット（2026-09-09時点）、M-6列のデータは2026-09-10時点を使用しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>3位</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">下降</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.2pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">クイックターン採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>20.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+5.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アンコール採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-1.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">67.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-3.0pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>12.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-4.6pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-0.7pp</td>
</tr>
</tbody>
</table>
</div>

めいそう採用率はM-5の34.3%からM-6で33.1%と-1.2ppの微減にとどまり、「大きく後退した」と言えるほどの変化ではありません。むしろ目立つのはクイックターン（+5.6pp）とずぶとい（+3.6pp）の上昇です。アンコールはM-5の45.3%から43.5%へ-1.8pp減少しており、「アンコールで縛る立ち回りへ戻った」という見立ては数値上は支持されません。実態としては、めいそう・アンコールの主力2技はほぼ横ばいのまま、クイックターンで後続に負担なく対面を渡す選択肢が伸び、それに伴ってずぶといでB方向の耐久を確保する個体が増えたという変化です。オボンのみ（-4.6pp）の低下とたべのこし（-0.7pp）のほぼ横ばいも合わせると、瞬間火力よりも受けて立ち回る個体がやや増加したと読めます。使用率は2位から3位へ後退していますが、上記の分布変化はいずれも数pp規模であり、技構成の骨格自体はM-5から継続しています。

---

## 苦手なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）は確定2発ですが後手に回り、メガボーマンダの主力すてみタックル（採用率73.4%）の確定2発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">素早さはアシレーヌが上ですが、うたかたのアリア（採用率92.6%）が確定4発に対し、メガグソクムシャの主力アイアンヘッド（採用率76.0%）は確定3発のため、打点で負けて先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（採用率92.6%）は確定4発止まり。ギルガルドの主力シャドーボール（採用率42.9%）の確定4発と同水準ですが、素早さは同速でこちらの先手が安定せず、先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）が確定2発止まりの一方、ゴリランダーの主力グラススライダー（採用率94.5%、くさ×2弱点）の確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）は確定3発と決め手を欠き、ギャラドスの主力パワーウィップ（採用率67.3%）の確定3発と競り合った末、後手のため先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（採用率92.6%）は確定3発止まり。メガリザードンYの主力ソーラービーム（採用率60.1%）の確定2発に先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）は確定3発止まり。ウォッシュロトムの主力10まんボルト（採用率50.8%、でんき×2弱点）の確定3発と並び、後手のため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）は確定2発ですが、オオニューラの主力フェイタルクロー（採用率94.7%）も確定2発。後手のため先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）が確定1発を取れる場面でも、パーモットの主力でんこうそうげき（採用率85.1%、でんき×2弱点）の確定1発に先手を取られ、先に倒されます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）とガブリアスの主力じしん（採用率67.6%）は共に確定2発。素早さはガブリアスが上ですが、優先度+1のアクアジェットで先に決着をつけられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってうたかたのアリア（採用率92.6%）が確定3発。カバルドンの主力じしん（採用率99.3%）も確定3発で先制で押し切れますが、カバルドンはあくび（採用率96.5%）も高採用のため、じしんではなくあくびで場を流されると押し切りきれず様子見になる点には注意が必要です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）で確定2発。セグレイブの主力じしん（採用率87.6%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）で確定2発。ルカリオの主力ラスターカノン（採用率78.8%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）とゲッコウガの主力ヘドロウェーブ（採用率73.5%、どく×2弱点）は共に確定2発。素早さはゲッコウガが上ですが、優先度+1のアクアジェットで先に決着をつけられます。くさむすび（採用率20.9%）は重量依存で威力60にとどまり、ヘドロウェーブより打点が低いため、この技を持たれても有利は崩れません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）で確定2発。メガリザードンXの主力フレアドライブ（採用率36.5%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）とアローラキュウコンの主力フリーズドライ（採用率80.3%）は共に確定3発。素早さはアローラキュウコンが上ですが、優先度+1のアクアジェットで先に決着をつけられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（採用率92.6%）で確定2発。ウルガモスの主力ギガドレイン（採用率77.6%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）で確定2発。サザンドラの主力あくのはどう（採用率98.3%）は威力不足で決め手を欠き、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">うたかたのアリア（採用率92.6%）で確定2発。ラウドボーンの主力シャドーボール（採用率52.9%）は威力不足で決め手を欠き、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率99.1%）で確定2発。イエッサン(オス)の主力ワイドフォース（採用率99.4%）は確定3発止まりで、先に押し切れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でアシレーヌと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
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
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ボーマンダ**（1位）はドラゴン/ひこうで、アシレーヌはドラゴン技を無効で受けられます。逆にボーマンダの弱点であるこおり技（×4）はアシレーヌが半減で受けられ、くさ技もボーマンダが半減（×0.25）で受けられるため、こおり・くさを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**ガブリアス**（2位）はドラゴン/じめんで、アシレーヌはドラゴン技を無効で受けられます。逆にアシレーヌの弱点であるでんき技はガブリアスがじめんタイプで無効化でき、こおり技もアシレーヌが半減で受けられるため、でんき・こおりを撃ってくる相手への受け出し先をお互いに用意できる組み合わせです。

**カバルドン**（3位）はじめん単タイプで、アシレーヌの弱点であるでんき技を無効化できます。カバルドン自身の弱点であるくさ・こおり技のうち、こおりはアシレーヌが半減で受けられます。あくびによる交代誘導とステルスロックの設置役も担い、カバルドンが場を動かしている間にアシレーヌを後続として対面に出せる選出構築上の役割分担もあります。

**マスカーニャ**（10位）はくさ/あくで、くさタイプの技を自身の耐性（×0.5）で受けられます。アシレーヌの弱点であるくさ技を持つ相手には、マスカーニャに受け出すことで弱点を分散できます。

---

## まとめ

M-6のアシレーヌはM-5の2位から3位へ使用率を落としましたが、主力技構成自体はM-5から大きく変わらず、クイックターンとずぶといの採用がやや伸びた程度の変化にとどまるシーズンです。

- **使用率2位→3位**：技構成（ムーンフォース・うたかたのアリア・アクアジェット）は継続しています。めいそう・アンコールは横ばい〜微減で、「積みから対面操作へ大きく転換した」わけではありません
- **めいそう-1.2pp・アンコール-1.8pp**：いずれも小幅な減少で、主力2型の比率自体は維持されています
- **クイックターン+5.6pp・ずぶとい+3.6pp・オボンのみ-4.6pp**：後続に負担なく対面を渡す選択肢と、B方向へ耐久を配分する個体が増加しています

C126・D116の高い特殊耐久ラインを土台に、めいそうで一気に押し切るか、アンコール・クイックターンで対面を操作するかは、パーティ内での役割に応じた選択になります。どく・くさ・でんきの3弱点は環境上位に広く存在するため、選出段階でのケアが引き続き求められます。

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/primarina/)**
