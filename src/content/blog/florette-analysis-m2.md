---
title: '【ポケモンチャンピオンズ】メガフラエッテ徹底考察 M-2シーズン使用率11位・メガ進化の全て'
description: 'シーズンM-2でメガ進化率97%を誇るメガフラエッテを徹底分析。めいそう×ドレインキッスの崩し性能、相方メガギャラドスとのダブルメガ構築、パーティ全体の組み方まで実データをもとに解説します。'
pubDate: '2026-05-21'
heroImage: '../../assets/hero-florette-m2.png'
---

<style>
.type-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.85em;
  font-weight: bold;
}
.poke-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0;
  padding: 16px 20px;
  background: linear-gradient(135deg, #fce4f3 0%, #f3e8ff 100%);
  border-radius: 16px;
  border: 1px solid #e9b8d8;
}
.poke-header img.poke-icon {
  width: 80px;
  height: 80px;
}
.poke-header .poke-info h2 {
  margin: 0 0 6px;
  font-size: 1.5rem;
}
.stat-table td, .stat-table th {
  padding: 6px 12px;
  border: 1px solid #e2e8f0;
  text-align: center;
}
.stat-table th {
  background: #f8f0fb;
  font-weight: 600;
}
.bar-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}
.bar {
  height: 10px;
  border-radius: 5px;
  background: linear-gradient(90deg, #c084db, #e879a8);
}
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" class="poke-icon" />
  <div class="poke-info">
    <h2>フラエッテ（永遠の花）</h2>
    <div>
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">
      <strong>フェアリー</strong>タイプ
      &nbsp;｜&nbsp; M-2シングル使用率 <strong>11位</strong>
      &nbsp;｜&nbsp; メガ進化率 <strong>97.4%</strong>
    </div>
  </div>
</div>

---

## なぜ今、メガフラエッテが強いのか

M-2環境のシングルバトルで**フラエッテナイト採用率97.4%**——ほぼ全てのフラエッテはメガ進化前提で採用されています。その理由は3つです。

1. **ドラゴン完全無効** ガブリアス・リザードン・サザンドラなどM-2上位を占めるドラゴン技を完全に無効化できる唯一の実用的タイプ
2. **めいそう×ドレインキッスの自己完結した崩し** 積んで回復しながら全抜きを狙える。タスキ+先制技で止まらない
3. **メガギャラドスとの最高の補完** 物理と特殊・水と草の両軸で、互いの弱点をカバーする理想のダブルメガ

---

## 基本スペック

### 種族値（メガフラエッテ）

<div style="max-width:360px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77.5%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>155</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:74%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>148</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">102</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:68px;min-width:68px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#9333ea">651</span>
  </div>
</div>

メガ進化でとくこう**125→155**、とくぼう**128→148**、すばやさ**92→102**と大幅強化。合計種族値651は環境内でもトップクラスです。

### タイプ相性（メガ進化前）

| タイプ | 弱点・耐性 |
|:--|:--|
| <img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> はがね | <strong style="color:#e53e3e">×2</strong> |
| <img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> どく | <strong style="color:#e53e3e">×2</strong> |
| <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> ドラゴン | <strong style="color:#2563eb">×0（無効）</strong> |
| <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> かくとう | <strong style="color:#60a5fa">×0.5</strong> |
| <img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> あく | <strong style="color:#60a5fa">×0.5</strong> |
| <img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> むし | <strong style="color:#60a5fa">×0.5</strong> |

ドラゴン無効はM-2環境で極めて価値が高く、使用率上位を占める**ガブリアス・リザードン・サザンドラ・カイリュー**のドラゴン技を完全に無効化できます。弱点ははがねとどくの2タイプのみ。

---

## 採用技の解説

| 技 | タイプ | 威力 | 命中 | 採用率 | 効果 |
|:--|:--:|:--:|:--:|:--:|:--|
| ムーンフォース | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:22px;height:22px;vertical-align:middle"> | 95 | 100 | 87.1% | 10%でとくこう-1 |
| めいそう | <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:22px;height:22px;vertical-align:middle"> | — | — | 84.4% | とくこう・とくぼう+1 |
| ドレインキッス | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:22px;height:22px;vertical-align:middle"> | 50 | 100 | 75.1% | 与ダメの1/2を回復 |
| はめつのひかり | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:22px;height:22px;vertical-align:middle"> | 140 | 90 | 46.7% | 与ダメの1/2を自分も受ける |
| サイコキネシス | <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:22px;height:22px;vertical-align:middle"> | 90 | 100 | 38.8% | 10%でとくぼう-1 |
| こうごうせい | <img src="/images/types/type-11-grass.png" alt="くさ" style="width:22px;height:22px;vertical-align:middle"> | — | — | 22.4% | HPを最大値の1/2回復 |
| あまえる | <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:22px;height:22px;vertical-align:middle"> | — | 100 | 12.0% | 相手のこうげき-2 |
| みがわり | <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:22px;height:22px;vertical-align:middle"> | — | — | 9.8% | HP1/4消費でみがわり生成 |

### フェアリーオーラによる実質威力

メガ進化後の特性フェアリーオーラにより、フェアリー技の威力が全て1.33倍になります。

| 技 | 表記威力 | フェアリーオーラ補正後 |
|:--|:--:|:--:|
| ムーンフォース | 95 | **126** |
| ドレインキッス | 50 | **67** |
| はめつのひかり | 140 | **186** |

はめつのひかりの実質威力186は全技の中でもトップクラスであり、反動を考慮しても破壊力は圧倒的です。

### シングル2大方向性：めいそう型 vs フルアタ型

採用率データが示す**ムーンフォース(87%) + ドレインキッス(75%)** の2技はほぼ全型共通ですが、残り2枠で型の方向性が大きく分かれます。

| | めいそう積みエース型 | フルアタ型 |
|:--|:--|:--|
| **技構成** | ムーンフォース / めいそう / ドレインキッス / みがわり | はめつのひかり / ムーンフォース / ドレインキッス / サイコキネシス |
| **めいそう** | ○ 採用 | ✕ 非採用 |
| **はめつのひかり** | ✕ 非採用 | ○ 採用 |
| **ドレインキッスの役割** | 積んだとくこうで継続回復 | はめつのひかり反動のHP補填 |
| **勝ち筋** | 積み上がれば全抜き | 即時威力186で押し切る |

**はめつのひかりとドレインキッスは同居する**——ただし「積みながら回復する型」ではなく、めいそうなしの純粋なアタッカー型として組み合わせます。めいそう(84.4%)とはめつのひかり(46.7%)がそれぞれ高い採用率を示すのは、この2型が並行して使われているためです。

ダブルではさらに別の型（マジカルシャイン / はめつのひかり / ムーンフォース / まもる）が存在します。

---

## 持ち物・特性

| 項目 | 採用率1位 | 採用率2位 |
|:--|:--|:--|
| **持ち物** | フラエッテナイト 97.4% | — |
| **特性** | フラワーベール 97.5% | きょうせい 2.5% |

持ち物はフラエッテナイト一択。

**特性の変化に注意**：メガ進化前の特性は「フラワーベール（草タイプの能力低下を防ぐ）」ですが、メガ進化後は**フェアリーオーラ**に変わります。フェアリーオーラは**場に出ている全ポケモンのフェアリー技の威力を1.33倍にする**特性です。

この特性はメガフラエッテ自身のムーンフォース・はめつのひかり・ドレインキッスを強化するだけでなく、**相手のフェアリー技も強化してしまう**点に注意が必要です。ただしシングルバトルでは相手のフェアリーアタッカーと同時に場に立つ機会が限られるため、実質的には自分の火力底上げとして機能します。

---

## 型考察

M-2で確認できる主要な3型を紹介します。型①②はどちらもおくびょうですが、めいそうを積む「制圧型」かはめつのひかりで即攻める「アタッカー型」かで技構成が大きく異なります。

### 型①：おくびょうCS型（先手積みエース）

**採用率トップ（おくびょう52.8%）**

```
性格：おくびょう
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / みがわり
```

**なぜおくびょうが最多か——素早さラインの意味**

すばやさ92というフラエッテの数値は微妙な位置にあります。おくびょうCS振りにすることで環境上位の多くを上から抜ける速度帯に到達します。**先に動けるかどうかはめいそうを積めるかどうかを直接決定する**ため、おくびょう採用の優先度が高くなっています。

4枠目のみがわりは積み展開の安定化に貢献します。ゲンガーの催眠・トリックを最も警戒するなら初手みがわりから入るのが安全で、みがわりが維持されている間に積んで制圧します。

**弱点**：はがね・どく技を積む前に受けると何もできない。メガギャラドスのいかくや先発ガブリアスでそれらを排除してから登場させるのが前提。

---

### 型②：おくびょうCS型（フルアタ即時火力）

```
性格：おくびょう
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：はめつのひかり / ムーンフォース / ドレインキッス / サイコキネシス
```

**めいそうを積まず即時火力で押し切る型**

型①との最大の違いは**めいそうを採用しない**点です。実質威力186のはめつのひかりをそのまま打ち込んで相手を削り、ドレインキッスで反動ダメージを部分的に補填しながら戦線を維持します。

**ダメージ計算で検証：はめつのひかりが1HKOを取れるターゲット**

リスクを承知でなぜはめつのひかりを採用するか——答えはダメージ計算に示されます。

Level 50のダメージ計算式（特殊技）：

```
Base     = floor( 22 × 威力 × SpA / SpD ) ÷ 50 + 2
確定ダメージ = Base × STAB(1.5) × フェアリーオーラ(1.33) × タイプ相性 × 乱数(0.85〜1.00)
```

ムーンフォース(95) vs はめつのひかり(140) の威力比 = **1.474倍**。この差から、ムーンフォースがHP残量の **68%以上** を与えている相手に対し、はめつのひかりが確定1HKOを取れる計算になります（0.68 × 1.474 ≈ 1.00）。

M-2の主要3ターゲット（おくびょう252SpA、SpA実数値207）で具体的に検証します。

---

**シナリオ①：アシレーヌ（SR不要・常時有効）**

アシレーヌ（おくびょうCS：HP155, SpD135, フェアリー中性×1）

| | ダメージ幅 | HP155比 | 確定数 |
|:--|:--:|:--:|:--|
| ムーンフォース | 111〜131 | 72〜85% | 確定2発 |
| **はめつのひかり** | **162〜191** | **105〜123%** | **確定1発** |

SR・積みなし・素の状態で確定1HKOが取れる最も明確なシナリオ。SR受けダメージが×1×1=12.5%（19HP）と小さいため、SR後でもムーンフォースは2HKOのまま変わらない。

---

**シナリオ②：カイリュー（マルチスケイル突破）**

カイリュー（HP特化型：HP198, SpD120, ドラゴン×2、**マルチスケイル残り**）

マルチスケイルはHP満タン時にダメージを1/2にする特性。SR（×2弱点=25%削り）を踏んでいないフルHPの状態では効果が残る。

| | 通常ダメージ | **マルチスケイル後（÷2）** | HP198への確定数 |
|:--|:--:|:--:|:--|
| ムーンフォース | 249〜294 | 124〜147（63〜74%） | **確定2発** |
| **はめつのひかり** | **365〜430** | **182〜215（92〜109%）** | **乱数8/16（50%）で1発** |

HP特化しないアタッカー型（HP=166）に対しては、はめつのひかり最小値182 > HP166 → **確定1HKO**。

SR後（マルチスケイル解除・HP149以下）：ムーンフォース最小値249 > HP149 → **両者とも確定1HKO**（差なし）。

**ムーンフォースはマルチスケイルを一切突破できない**（最大147 < HP166/198）のに対し、はめつのひかりはHP型でも50%・アタッカー型では確定で突破できます。

---

**シナリオ③：ステルスロック展開後のリザードン**

リザードン（おくびょうCS：HP153, SpD105, ほのお/ひこう×0.5、**SR×4弱点**）

リザードン（ほのお/ひこう）はステルスロックに×4弱点（ほのお×2・ひこう×2）→ HP50%削り（76ダメージ、残り77HP）。

| | SR前（HP153残り） | **SR後（HP77残り）** |
|:--|:--|:--|
| ムーンフォース（70〜83） | 確定2発（46〜54%） | **乱数7/16（43.75%）で1発** |
| **はめつのひかり（103〜122）** | 確定2発（67〜80%） | **確定1発（134〜159%）** |

SR前は両者とも2HKO。SR後にはめつのひかりが確定1HKO、ムーンフォースはランダム43.75%にとどまります。**ガブリアスのステルスロック展開を前提とする構築では、SR後リザードンを確実に処理できる**点がフルアタ型固有の優位性です。

---

**（参考）メガギャラドスは差が出ない**

メガギャラドス（いじっぱりAS：HP170, SpD150, あく×2）に対して、ムーンフォースは既に確定1HKOを達成しています（min 198 > HP170）。×2タイプ補正があるため、はめつのひかりを使う必要はありません。

---

**SpA252EVs投資が必須条件**

| SpA設定 | 実数値 | アシレーヌ（HP155, SpD135）への最小ダメージ | 判定 |
|:--|:--:|:--:|:--|
| 252EVs（おくびょう） | 207 | 162（105%） | **確定1HKO** |
| 0EVs（未投資） | 175 | 136（88%） | 確定2HKO |

EVs未投資ではアシレーヌへの確定1HKOが成立しません。フルアタ型は**252SpA一択**です。

ムーンフォースを使う場面：HPが減って反動が致命傷になりうる局面、または命中90のリスクを避けたい局面で使い分けます。

サイコキネシスでどくタイプへの打点を確保。フラエッテが弱点を突かれるどく技を持つポケモンを先に処理できます。

**弱点**：積みがないため高耐久ポケモンへの崩しが難しい。はめつのひかりの反動をドレインキッスで完全相殺はできないため、長期戦になるほどHP消耗が進む。

---

### 型③：ずぶといHB型（耐久積み）

**採用率3位（ずぶとい4.1%）**

```
性格：ずぶとい
努力値：HB+c（HP・ぼうぎょ重点、とくこうに少量振る）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / こうごうせい or みがわり
```

**なぜ耐久型が少数派か——4.1%の意味**

採用率4.1%という数字は「ニッチだが一定の需要がある」ことを示しています。物理耐久を上げることでルカリオ・ハッサムなどのはがね物理アタッカーの攻撃を1発耐えてめいそうを積む、という展開が可能になります。

こうごうせい採用の場合はHP最大値の半分を回復できるため、削られた体力をターンをまたいで補填しながら積む展開が可能です。みがわり採用の場合はゲンガーの催眠・トリックへの耐性を確保しつつ積む展開が可能です。

ずぶとい型が少数派にとどまる理由は、**素早さを捨てることで積む前に倒されるリスクが大幅に上がる**からです。この型を機能させるにはいかくサポートや相手のはがね・どくを事前排除できる構築が必須で、採用コストが高くなります。

---

### 型の選択マトリクス

| | 型①：めいそう積みエース | 型②：フルアタ即時火力 | 型③：耐久積み |
|:--|:--:|:--:|:--:|
| **性格** | おくびょう / ひかえめ | おくびょう | ずぶとい |
| **めいそう** | ○ | ✕ | ○ |
| **はめつのひかり** | ✕ | ○ | ✕ |
| **ドレインキッス** | 積み回復 | 反動補填 | 積み回復 |
| **4枠目** | みがわり / サイコキネシス | サイコキネシス | こうごうせい / みがわり |
| **いかくサポート必要度** | 中 | 低 | 高 |

---

## 相性の良いメガ進化パートナー：メガギャラドス

フラエッテの**同居率1位（ギャラドス）**かつ**ギャラドスのギャラドスナイト採用率76.3%**——データが示す通り、メガフラエッテの最有力パートナーはメガギャラドスです。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f0f9ff;border:1px solid #bae6fd;text-align:left">項目</th>
  <th style="padding:8px 12px;background:#fce4f3;border:1px solid #f9a8d4;text-align:center"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガフラエッテ</th>
  <th style="padding:8px 12px;background:#eff6ff;border:1px solid #bfdbfe;text-align:center"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガギャラドス</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">攻撃軸</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">特殊（とくこう125）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">物理（こうげき高い）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">主な技</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">ムーンフォース・ドレインキッス</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">たきのぼり・りゅうのまい・じしん</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">セットアップ</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">めいそう（特殊耐久↑）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">りゅうのまい（すばやさ・こうげき↑）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">弱点</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">はがね・どく</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">でんき・いわ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">特性（メガ前）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">フラワーベール</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">いかく（こうげき-1）</td>
</tr>
</tbody>
</table>
</div>

### なぜこの組み合わせが強いか

**フラエッテ → ギャラドスへの補完**

- フラエッテのフェアリー技が、ギャラドスが苦手なドラゴン・かくとうタイプに有効
- ギャラドスが弱いでんきタイプに対して、フラエッテは等倍で受けられる

**ギャラドス → フラエッテへの補完**

- いかくで相手の物理こうげきを下げてフラエッテが積みやすい盤面を作る
- ギャラドスのじしんでフラエッテの弱点であるはがね（ブリジュラス・ギルガルドなど）を処理
- ギャラドスが苦手ないわタイプをフラエッテのムーンフォースが中程度に打てる

**ギャラドスの主要データ（M-2）**

| 項目 | データ |
|:--|:--|
| 使用率 | 10位 |
| 性格（1位）| いじっぱり 45.1% |
| 努力値（1位）| AS（すばやさ・こうげき全振り）38.1% |
| 技構成 | たきのぼり / りゅうのまい / じしん / こおりのキバ |
| ギャラドスナイト採用率 | 76.3% |

---

## フラエッテを軸にしたパーティ構成案

構築6枠のうちメガ枠2（フラエッテ＋ギャラドス）を確保した上で、残り4枠に何を入れるかが鍵です。

### パーティ構成案①「ステロ展開型」

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ①（主軸）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガフラエッテ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう積み全抜きエース</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ②（物理エース）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いかく＋りゅうのまいで物理制圧</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">展開サポート</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック＋はがね処理（じしん）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">崩し</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">催眠・トリックで相手の積みを崩す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0472-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">グライオン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスの後に置ける地面耐性</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻・先制技</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0448-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マッハパンチ＋はがね技でフラエッテの弱点を補完</td>
</tr>
</tbody>
</table>
</div>

この構成の流れ：
1. **ガブリアス**でステルスロック展開・相手のはがねタイプをじしんで処理
2. **メガギャラドス**のいかくで相手の物理アタッカーを抑制し、りゅうのまいで加速
3. **メガフラエッテ**が盤面が整った後にめいそう積みから全抜き
4. ゲンガー・ルカリオが詰め・崩し役

### パーティ構成案②「サイクル崩し型」

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ①（主軸）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガフラエッテ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう＋みがわりで安定した積み詰め</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ②（物理エース）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いかく＋ちょうはつで相手のサポート封じ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステロ撒き</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0143-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カビゴン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい積み＋どくどく＋ステロで削り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">電気対策</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスの弱点・でんきに強い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0681-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね耐性でフラエッテの裏から出せる・キングシールド</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0823-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね＋とびタイプでどくに強く、おいかぜサポート</td>
</tr>
</tbody>
</table>
</div>

---

## フラエッテが苦手なポケモンと対策

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">苦手な相手</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">理由</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">解決策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0681-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px">ギルガルド</span>・<span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0212-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px">ハッサム</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="white-space:nowrap"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">はがね技で弱点</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアスのじしんで処理</span></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px">ゲンガー</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">催眠で積み展開を妨害</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みがわりを張ってから積む・先にゲンガーを処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0448-00.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px">ルカリオ</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><span style="white-space:nowrap"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:4px">こうそくいどう＋はがね技で上から処理</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスのいかくで削いでからフラエッテ投入</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><span style="white-space:nowrap"><img src="/images/pokemon/pokemon-0038-01.webp" alt="" style="width:36px;height:36px;vertical-align:middle;margin-right:4px">アローラキュウコン</span></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あられ＋ふぶきの連打でみがわり破壊</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制技で倒すか、ガブリアスで地面技を通す</td>
</tr>
</tbody>
</table>
</div>

---

## まとめ

メガフラエッテはM-2シングルで**「積みエース」「ドラゴン封じ」「耐久回復」を1体で兼ねる**稀有なポケモンです。

- **フラエッテナイト採用率97.4%**——実質メガ進化専用枠として機能
- **めいそう＋ドレインキッスの自己完結**でタスキ・先制技に強く、長期戦でも制圧できる
- **メガギャラドスとのダブルメガ構築**が同居率データで裏付けられた最強コンビ

ガブリアスでステロを撒いてからメガフラエッテ・メガギャラドスの二枚看板で詰める構築は、M-2環境の中核的な戦略の一つです。次シーズンでの採用も十分に検討に値します。
