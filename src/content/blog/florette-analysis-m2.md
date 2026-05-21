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
    <span style="width:52px;color:#555;font-weight:600">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:52px;color:#555;font-weight:600">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:52px;color:#555;font-weight:600">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:52px;color:#555;font-weight:600">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77.5%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>155</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:52px;color:#555;font-weight:600">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:74%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>148</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:52px;color:#555;font-weight:600">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">102</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:52px;color:#555">合計</span>
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

### 3枠固定コアと4枠目の二択

採用率を見ると、**ムーンフォース(87%) + めいそう(84%) + ドレインキッス(75%)** の3技が実質的なコアセットです。残り1枠で構築の方向性が分岐します。

**はめつのひかり(46.7%) vs サイコキネシス(38.8%)** の合計は85%——4枠目のほぼすべてがこの二択です。これは単なる好みでなく、**対処したい相手が違う**ことを示しています。

| 4枠目 | 採用率 | 狙い | 向いている環境 |
|:--|:--:|:--|:--|
| はめつのひかり | 46.7% | 耐久が高い相手への一撃突破 | 受けサイクル・高耐久ポケモンが多い |
| サイコキネシス | 38.8% | どくタイプへの確定打点 | どく・はがね複合やどくポケモンが多い |

### はめつのひかり × ドレインキッス のHP管理

はめつのひかり（実質威力186）とドレインキッス（実質威力67）はどちらも与ダメの1/2を自分が受ける・回復するという仕様ですが、**威力が大きく異なるため反動量と回復量は釣り合いません**。

```
同じ相手に対して使った場合の比較（フェアリーオーラ補正後）：

  はめつのひかり：実質威力186 → 与ダメの1/2 を反動として自分が受ける
  ドレインキッス：実質威力 67 → 与ダメの1/2 を回復として自分が得る

  反動：回復 ≈ 186：67 ≈ 2.8倍
```

1回のはめつのひかりの反動を完全に回復するには、ドレインキッスを約3回使う必要がある計算です。

**では、なぜこの2技が同時採用されるのか？**

ドレインキッスは完全相殺こそできないものの、「ダメージを受けながら少しずつ回復できる」ことで戦線を長持ちさせます。正しい使い方は「相殺」ではなく、**HPが多い局面ではめつのひかりで高火力を押し付け、削れたHPをドレインキッスで補填しながら戦線を維持する**という管理型の立ち回りです。

めいそうを積むと両者の効果はとくこうに比例して大きくなりますが、その比率（2.8倍）は変わらないため、**積めば積むほどHP消耗ペースも速くなる**点は意識が必要です。

### ムーンフォース vs はめつのひかりの使い分け基準

```
はめつのひかりを選ぶ場面：
  ・自分のHPが十分あり、反動を受けても問題ない
  ・ムーンフォースでは確定1発を取れないが、はめつのひかりなら取れる
  ・次のターンにドレインキッスで回復できる見通しがある

ムーンフォースを選ぶ場面：
  ・自分のHPが少なく、反動ダメージが致命傷になりうる
  ・10%のとくこう低下を狙いたい（削り＋崩し）
  ・命中90のリスクを避けたい局面
```

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

M-2で確認できる主要な3型を紹介します。性格の二強（おくびょう52.8% / ひかえめ42.6%）が型の方向性を決める大きな分岐点です。

### 型①：おくびょうCS型（先手積みエース）

**採用率トップ（おくびょう52.8%）**

```
性格：おくびょう
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / はめつのひかり
```

**なぜおくびょうが最多か——素早さラインの意味**

すばやさ92というフラエッテの数値は微妙な位置にあります。おくびょうCS振りにすることで環境上位の多くを上から抜ける速度帯に到達します。**先に動けるかどうかはめいそうを積めるかどうかを直接決定する**ため、おくびょう採用の優先度が高くなっています。

はめつのひかりを4枠目に採用するのは、積み上がった後の「削り切れない耐久ポケモンへの突破口」として機能するためです。ドレインキッスで体力を維持しながら、決定打が必要な場面ではめつのひかりを選択します。

**弱点**：はがね・どく技を積む前に受けると何もできない。メガギャラドスのいかくや先発ガブリアスでそれらを排除してから登場させるのが前提。

---

### 型②：ひかえめCS型（確定打点重視）

**採用率2位（ひかえめ42.6%）**

```
性格：ひかえめ
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / サイコキネシス
```

**おくびょうとの使い分けを採用率から読む**

おくびょうとひかえめの採用率が52.8% vs 42.6%とほぼ拮抗しています。この割合はプレイヤーが「素早さ優位」と「火力優位」のどちらを優先するかで判断していることを示しています。

ひかえめ型で4枠目に**サイコキネシス**を採用するケースが多い理由は、どくタイプへの打点確保です。フラエッテはどく技で弱点を突かれる上に、ムーンフォース・はめつのひかりはどくタイプに通りが悪い（フェアリー→どく等倍以下）ため、サイコキネシスで確実に弱点を突けます。

**弱点**：おくびょうより遅いため環境のおくびょう勢（リザードン・アシレーヌなど）に先を取られる場面がある。

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

こうごうせい採用の場合はHP最大値の半分を回復できるため、はめつのひかりの反動すら無視してよい場面が増えます。みがわり採用の場合はゲンガーの催眠・トリックへの耐性を確保しつつ積む展開が可能です。

ずぶとい型が少数派にとどまる理由は、**素早さを捨てることで積む前に倒されるリスクが大幅に上がる**からです。この型を機能させるにはいかくサポートや相手のはがね・どくを事前排除できる構築が必須で、採用コストが高くなります。

---

### 型の選択マトリクス

| | 素早さ重視 | 火力重視 | 耐久重視 |
|:--|:--:|:--:|:--:|
| **性格** | おくびょう | ひかえめ | ずぶとい |
| **採用率** | 52.8% | 42.6% | 4.1% |
| **4枠目** | はめつのひかり | サイコキネシス | こうごうせい/みがわり |
| **いかくサポート必要度** | 中 | 中 | 高 |
| **積み前の生存率** | 高 | 中 | 中（物理のみ） |

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はめつのひかり＋みがわりで詰め</td>
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
