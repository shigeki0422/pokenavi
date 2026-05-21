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

### 種族値

<table class="stat-table">
  <thead><tr><th>HP</th><th>こうげき</th><th>ぼうぎょ</th><th>とくこう</th><th>とくぼう</th><th>すばやさ</th><th>合計</th></tr></thead>
  <tbody>
    <tr>
      <td><div class="bar-wrap"><div class="bar" style="width:55px"></div><span>74</span></div></td>
      <td><div class="bar-wrap"><div class="bar" style="width:49px"></div><span>65</span></div></td>
      <td><div class="bar-wrap"><div class="bar" style="width:50px"></div><span>67</span></div></td>
      <td><div class="bar-wrap"><div class="bar" style="width:94px"></div><span><strong>125</strong></span></div></td>
      <td><div class="bar-wrap"><div class="bar" style="width:96px"></div><span><strong>128</strong></span></div></td>
      <td><div class="bar-wrap"><div class="bar" style="width:69px"></div><span>92</span></div></td>
      <td><strong>551</strong></td>
    </tr>
  </tbody>
</table>

とくこう125・とくぼう128は最上位クラス。素早さ92はやや控えめですが、おくびょうCS振りで多くの環境ポケモンを上回れます。

### タイプ相性（メガ進化前）

| タイプ | 弱点・耐性 |
|:--|:--|
| <img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> はがね | <strong style="color:#e53e3e">×2</strong> |
| <img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> どく | <strong style="color:#e53e3e">×2</strong> |
| <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> ドラゴン | <strong style="color:#2563eb">×0（無効）</strong> |
| <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> かくとう | <strong style="color:#60a5fa">×0.5</strong> |
| <img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> あく | <strong style="color:#60a5fa">×0.5</strong> |
| <img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> むし | <strong style="color:#60a5fa">×0.5</strong> |

ドラゴン無効がM-2環境で極めて価値が高く、**ガブリアス・リザードン・サザンドラ・カイリュー**に対して電気タイプポケモンと並ぶ数少ない完全シャットアウト枠。弱点は鋼とどくの2タイプのみ。

---

## 採用技の解説

| 技 | 採用率 |
|:--|:--:|
| <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ムーンフォース | 87.1% |
| <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> めいそう | 84.4% |
| <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> ドレインキッス | 75.1% |
| <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> はめつのひかり | 46.7% |
| <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> サイコキネシス | 38.8% |
| <img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> こうごうせい | 22.4% |
| <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> あまえる | 12.0% |
| <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:24px;height:24px;vertical-align:middle;margin-right:5px"> みがわり | 9.8% |

**ムーンフォース**はフェアリー一致メインウエポン。**めいそう**はとくこう・とくぼうを同時に上昇させる積み技で、1回積めばドレインキッスの回復量も増加。**ドレインキッス**はHP吸収付きフェアリー技——相手のHPの半分を奪いながら自己回復する持続戦闘の要。

**はめつのひかり**は2ターン後に必中で大ダメージを与える遅延攻撃技。みがわりとの組み合わせで後出しから一方的にダメージを与えられます。**サイコキネシス**はどくタイプへの打点（毒タイプに弱点を突ける）として採用されるケースも。

---

## 持ち物・特性・性格・努力値

| 項目 | 採用率1位 | 採用率2位 |
|:--|:--|:--|
| **持ち物** | フラエッテナイト 97.4% | — |
| **特性** | フラワーベール 97.5% | きょうせい 2.5% |
| **性格** | おくびょう 52.8% | ひかえめ 42.6% |
| **努力値** | CS（素早さ・とくこう全振り）22.1% | — |

持ち物はフラエッテナイト一択。特性フラワーベールはくさタイプの能力低下を無効にする。**おくびょうCS**が最多でスピード重視——環境最速クラスに近づける。**ひかえめCS**は火力特化型で特に積み展開前提。

---

## 構築と立ち回り

### 基本の動き

```
1ターン目: 対面の相手に有利なら めいそう → とくこう・とくぼう+1
2ターン目: ドレインキッスで回収しながら削る
3ターン目以降: ムーンフォースで全抜き or はめつのひかりで詰める
```

タスキ消費や状態異常でHPが削られても、**ドレインキッスで回収しながら積み続ける**のが強さの本質。めいそうを1積みした後のドレインキッスは半分以上回復することも多い。

### 主な技構成例

```
技構成①（スタンダード）: ムーンフォース / めいそう / ドレインキッス / はめつのひかり
技構成②（みがわり展開）: ムーンフォース / めいそう / ドレインキッス / みがわり
技構成③（速攻重視）:   ムーンフォース / ドレインキッス / あまえる / サイコキネシス
```

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
