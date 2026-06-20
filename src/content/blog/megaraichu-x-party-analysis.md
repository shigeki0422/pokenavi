---
title: '【ポケモンチャンピオンズ】メガライチュウX 考察 M-3 物理エレキメイカー型のパーティ構築'
description: 'M-3シーズンで使用率3位のライチュウ。だが石の96.6%はメガライチュウY（特殊）で、メガライチュウX（物理）はわずか3.0%。なぜYが主流かをデータで示しつつ、ニッチなメガライチュウXを軸にしたパーティ構成・選出・運用を、対戦シミュレータの実測検証とともに考察します。'
pubDate: '2026-06-19'
draft: false
heroImage: '../../assets/blog-placeholder-1.jpg'
---

<style>
.poke-icon {
  display: inline-block;
  width: 40px;
  height: 40px;
  vertical-align: middle;
  margin-right: 4px;
}
.type-badge-sm {
  display: inline-block;
  width: 32px;
  height: 32px;
  vertical-align: middle;
  margin: 1px 2px;
}
.pokemon-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 20px 0;
}
.pokemon-header img {
  width: 96px;
  height: 96px;
}
.build-card {
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 14px 16px;
  margin: 16px 0;
  background: #fafafa;
}
.build-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}
.build-header img {
  width: 48px;
  height: 48px;
}
.build-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
@media (max-width: 640px) {
  .build-cols { grid-template-columns: 1fr; }
}
.statbar-label { display:inline-block; width:24px; font-weight:bold; }
</style>

<div class="pokemon-header">
  <img src="/images/pokemon/pokemon-0026-00.webp" alt="メガライチュウX（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">メガライチュウX</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-12-electric.png" alt="でんき" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.85rem;color:#555">
      ライチュウ全体 使用率 <strong style="color:#dc2626">3位</strong> ／
      ライチュウナイトX 採用率 <strong style="color:#7c3aed">3.0%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン（2026/06/18集計）のシングルバトルを対象としています。

ライチュウはM-3シーズンで**使用率3位**の人気ポケモンです。しかしその中身を見ると、メガ石の内訳は**ライチュウナイトY 96.6% / ライチュウナイトX 3.0%**。つまり「ライチュウ使い」のほぼ全員がメガライチュウY（特殊）を選び、メガライチュウX（物理）はごく一握りしか使っていません。

この記事では、まずなぜYがこれほど支配的なのかをデータで確認し、その差別化点を踏まえたうえで、あえてメガライチュウXを軸に組んだパーティの狙い・選出・運用を、当サイトの対戦シミュレータによる実測検証とともに考察します。

---

## メガライチュウX と メガライチュウY の違い

両者はでんき単タイプで共通しますが、メガ進化後の種族値・特性・役割はまったく別物です。

| | メガライチュウX | メガライチュウY |
|---|---|---|
| 特性 | <strong>エレキメイカー</strong>（登場時に電気フィールド） | <strong>ノーガード</strong>（自他の技が必中） |
| 種族値(H/A/B/C/D/S) | 60/<strong>135</strong>/95/90/95/110 | 60/100/55/<strong>160</strong>/80/<strong>130</strong> |
| 役割 | 物理アタッカー | 特殊アタッカー |
| 主な実数値 | A187（無補正）／S178（ようきS↑） | C233（ひかえめC↑）／S200（おくびょうS↑） |

実数値はLv50・個体値31・EV最大32で算出（`((種族値×2+31+63)×50÷100+5)×性格補正`）。

### Yが主流である理由はデータに明確に出ている

メガライチュウの「型」はそのまま使用率に出ています。性格は**おくびょう74.1% / ひかえめ20.9%**で特殊型が95%を占め、技は**でんじほう96.5% / きあいだま95.7% / くさむすび75.3%**。EVは**H2-C32-S32が76.9%**。これはすべてメガライチュウY（特殊）の型です。

Yの肝は特性**ノーガード**にあります。本来命中50のでんじほうが必中になり、C233という高火力で「必中の高威力特殊技」を撃ち込めます。さらにくさむすびでくさ・じめんを半減できないみず複合の重量級を狙い、きあいだまであく・はがねを縛る。**ノーガード×でんじほうという1点突破の明快さが、Yを使用率3位の人気に押し上げています**。

### Xが見るべき相手はSライン

一方メガライチュウXは物理型で、その武器はYにないものです。エレキメイカーによる電気フィールド展開と、A187の物理打点。素早さはようきでS178となり、ガブリアス（最速S169）を抜けます。ただしマスカーニャ（最速S192）には抜かれます。

つまり**X独自の差別化点は「ガブリアスを上から殴れる物理でんきアタッカー」である点**で、これがそのままパーティ設計の出発点になります。後述するように、現状の環境ではこの差別化点を「勝ち筋」まで昇華させるのは容易ではありませんが、軸を選ぶ思想としては成立します。

---

## メガライチュウXのタイプ相性

でんき単のため、X・Yで防御面は共通です。

| 弱点（×2） | 耐性（½） | 無効 |
|---|---|---|
| <img class="type-badge-sm" src="/images/types/type-04-ground.png" alt="じめん" /> | <img class="type-badge-sm" src="/images/types/type-12-electric.png" alt="でんき" /> <img class="type-badge-sm" src="/images/types/type-02-flying.png" alt="ひこう" /> <img class="type-badge-sm" src="/images/types/type-08-steel.png" alt="はがね" /> | なし |

弱点はじめん×2のみで耐性は3つと、攻撃を受ける面では優秀です。ただしじめん技は環境最上位に多く、ガブリアス（じしん採用率高）・ラグラージ（みず/じめん）・カバルドン（じしん）のじしんは×2で受け出しできません。Xは耐久(H112)も低く、**「殴り合う前提のアタッカー」であり受けには回れない**点を念頭に置く必要があります。

---

## データ分析②：X vs Y 確定数比較（環境上位50体）

X はようき・A32（A187）、Y はひかえめ・C32（C233）。相手のEVはM-3環境最多EV採用時。ミミッキュは**ばけのかわ**により初撃が常に無効化されるため比較対象外。

<style>
.ohko-table { width:100%; border-collapse:collapse; font-size:0.88rem; }
.ohko-table th { background:#f1f5f9; padding:8px 10px; text-align:left; border:1px solid #e2e8f0; white-space:nowrap; }
.ohko-table td { padding:7px 10px; border:1px solid #e2e8f0; vertical-align:middle; }
.ohko-table tr:nth-child(even) td { background:#f8fafc; }
.ohko-ok  { color:#16a34a; font-weight:700; }
.ohko-bad { color:#94a3b8; }
.ohko-tag-x { display:inline-block; background:#dbeafe; color:#1d4ed8; font-size:0.78rem; font-weight:700; padding:1px 7px; border-radius:4px; }
.ohko-tag-y { display:inline-block; background:#fce7f3; color:#9d174d; font-size:0.78rem; font-weight:700; padding:1px 7px; border-radius:4px; }
</style>

### X が優位な相手（9体）

X優位の共通パターンは**ドラゴンタイプ**（フェアリー×2）と**フェアリー・こおり複合**（アイアンテール×2）。Y のでんき技がじめんで無効になる相手でもあり、Y にとって最も苦手なゾーンです。

<div style="overflow-x:auto">
<table class="ohko-table">
<thead><tr>
  <th>相手（使用率）</th><th>タイプ</th><th>X ベスト技（確定数）</th><th>Y ベスト技（確定数）</th>
</tr></thead>
<tbody>
<tr>
  <td><strong>ガブリアス（1位）</strong></td>
  <td>ドラゴン/じめん</td>
  <td>じゃれつく：△乱1（7/16）<br><span class="ohko-ok">ねこだまし→じゃれつく：確定</span></td>
  <td><span class="ohko-bad">でんじほう：✕無効</span>　きあいだま：確定2発</td>
</tr>
<tr>
  <td><strong>カイリュー（20位）</strong></td>
  <td>ドラゴン/ひこう</td>
  <td>じゃれつく：乱1（14/16）※マルチスケイル時<br><span class="ohko-ok">ねこだまし→じゃれつく：確定</span></td>
  <td>でんじほう：確定2発</td>
</tr>
<tr>
  <td><strong>ドラパルト（43位）</strong></td>
  <td>ドラゴン/ゴースト</td>
  <td><span class="ohko-ok">じゃれつく：◎確定1発</span></td>
  <td>でんじほう：確定2発</td>
</tr>
<tr>
  <td><strong>ドラミドロ（35位）</strong></td>
  <td>どく/ドラゴン</td>
  <td><span class="ohko-ok">じゃれつく：乱1（14/16）</span></td>
  <td>きあいだま：確定2発</td>
</tr>
<tr>
  <td><strong>アローラキュウコン（18位）</strong></td>
  <td>こおり/フェアリー</td>
  <td><span class="ohko-ok">アイアンテール：◎確定1発</span></td>
  <td>でんじほう：確定2発</td>
</tr>
<tr>
  <td><strong>バイバニラ（30位）</strong></td>
  <td>こおり</td>
  <td><span class="ohko-ok">アイアンテール：◎確定1発</span></td>
  <td>きあいだま：確定2発</td>
</tr>
<tr>
  <td><strong>オーロンゲ（19位）</strong></td>
  <td>あく/フェアリー</td>
  <td><span class="ohko-ok">アイアンテール：乱1（8/16）</span></td>
  <td>きあいだま：確定2発</td>
</tr>
<tr>
  <td><strong>フラエッテ（永遠）（41位）</strong></td>
  <td>フェアリー</td>
  <td><span class="ohko-ok">アイアンテール：◎確定1発</span></td>
  <td>でんじほう：確定2発</td>
</tr>
<tr>
  <td><strong>エルフーン（50位）</strong></td>
  <td>くさ/フェアリー</td>
  <td><span class="ohko-ok">アイアンテール：◎確定1発</span></td>
  <td>きあいだま：確定2発</td>
</tr>
</tbody>
</table>
</div>

### Y が優位な相手（代表例）

Y はきあいだま（かくとう×2 → はがね・ノーマル・あく）・くさむすび（じめん・みず系重量級）・でんじほう（ひこう×2）の3技で環境上位を広くカバー。

<div style="overflow-x:auto">
<table class="ohko-table">
<thead><tr>
  <th>相手（使用率）</th><th>タイプ</th><th>Y ベスト技（確定数）</th><th>X ベスト技（確定数）</th>
</tr></thead>
<tbody>
<tr>
  <td>ブリジュラス（2位）</td><td>はがね/ドラゴン</td>
  <td><span class="ohko-ok">きあいだま：◎確定1発</span></td><td>じゃれつく：確定3発</td>
</tr>
<tr>
  <td>ラグラージ（4位）</td><td>みず/じめん</td>
  <td><span class="ohko-ok">くさむすび：◎確定1発</span></td><td>じゃれつく：確定2発</td>
</tr>
<tr>
  <td>マスカーニャ（5位）</td><td>くさ/あく</td>
  <td><span class="ohko-ok">きあいだま：◎確定1発</span></td><td>アイアンテール：確定2発</td>
</tr>
<tr>
  <td>アーマーガア（9位）</td><td>ひこう/はがね</td>
  <td><span class="ohko-ok">でんじほう：◎確定1発</span></td><td>ワイルドボルト：確定2発</td>
</tr>
<tr>
  <td>バシャーモ（16位）</td><td>ほのお/かくとう</td>
  <td><span class="ohko-ok">きあいだま：◎確定1発</span></td><td>ワイルドボルト：確定2発</td>
</tr>
<tr>
  <td>カバルドン（14位）</td><td>じめん</td>
  <td><span class="ohko-ok">くさむすび：◎確定1発</span></td><td>じゃれつく：確定3発</td>
</tr>
<tr>
  <td>ドドゲザン（24位）</td><td>あく/はがね</td>
  <td><span class="ohko-ok">きあいだま：◎確定1発</span></td><td>ワイルドボルト：確定3発</td>
</tr>
<tr>
  <td>ハッサム（31位）</td><td>むし/はがね</td>
  <td><span class="ohko-ok">きあいだま：◎確定1発</span></td><td>ワイルドボルト：確定2発</td>
</tr>
</tbody>
</table>
</div>

上位50体で**X優位9体・Y優位20体・同等20体**（ばけのかわのミミッキュ除外）。Xが優位を取れるのは環境のドラゴン・氷・フェアリー勢（アイアンテール/じゃれつくが×2弱点）に絞られ、主流帯（2〜5位のはがね・じめん・みず系）はYが確定1発を連発できる領域。これが石採用率の非対称（Y 96.6% vs X 3.0%）をデータとして裏付けています。
---

## メガライチュウX軸パーティの構成

ハンドオフの方針に沿い、**2メガ選出（ライチュウとリザードンの両メガ石を選出に入れ、盤面でどちらをメガ進化させるか選ぶ）**を柱としたチームです。Xだけで勝ちきれない分を、晴れ特殊エースのメガリザードンYと、対メタの物理陣で補います。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" />
    <strong>ライチュウ（→メガライチュウX）</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> せいでんき（11.9%）※メガ後エレキメイカー<br>
      <strong>性格:</strong> ようき<br>
      <strong>EV:</strong> A32 S32<br>
      <strong>持ち物:</strong> ライチュウナイトX（3.0%）
    </div>
    <div>
      <strong>技構成:</strong> ワイルドボルト / じゃれつく / アイアンテール / ねこだまし
    </div>
  </div>
</div>

軸。ようきでS178、ガブリアスの上を取れます。ねこだましの先制でタスキ潰し・削りを入れつつ、ワイルドボルトで地面以外を削り、ガブリアス・マスカーニャにはじゃれつくを通します。せいでんき採用は環境採用率（ひらいしん88.1%／せいでんき11.9%）に基づく選択で、メガ後はエレキメイカーに置き換わるため進化前の特性選択に大きな意味はありません。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" />
    <strong>リザードン（→メガリザードンY）</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> もうか ※メガ後ひでり<br>
      <strong>性格:</strong> ひかえめ<br>
      <strong>EV:</strong> H2 C32 S32<br>
      <strong>持ち物:</strong> リザードナイトY
    </div>
    <div>
      <strong>技構成:</strong> ソーラービーム / かえんほうしゃ / オーバーヒート / エアスラッシュ
    </div>
  </div>
</div>

第2のメガ枠。ひかえめでC232、ひでりの晴れ補正でかえんほうしゃが高火力になります。受けの厚い相手にXが刺さらないとき、こちらをメガ進化させて晴れ特殊で押す選択肢を持てます。ソーラービームでラグラージ（みず/じめん）等のみず複合受けを崩します。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0473-00.webp" alt="マンムー" />
    <strong>マンムー</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> あついしぼう<br>
      <strong>性格:</strong> いじっぱり<br>
      <strong>EV:</strong> H2 A32 S32<br>
      <strong>持ち物:</strong> きあいのタスキ
    </div>
    <div>
      <strong>技構成:</strong> じしん / こおりのつぶて / つららばり / つららおとし
    </div>
  </div>
</div>

対メタの先発。こおり技がガブリアス（ドラゴン/じめん＝こおり×4）に刺さり、Xが苦手とするじめん勢への回答になります。こおりのつぶてで先制を取れるため、Sで負ける相手の削り残しも処理できます。きあいのタスキで一撃を耐え、最低限の仕事を保証します。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0983-00.webp" alt="ドドゲザン" />
    <strong>ドドゲザン</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> そうだいしょう<br>
      <strong>性格:</strong> いじっぱり<br>
      <strong>EV:</strong> H32 A32<br>
      <strong>持ち物:</strong> くろいメガネ
    </div>
    <div>
      <strong>技構成:</strong> ふいうち / ドゲザン / アイアンヘッド / つるぎのまい
    </div>
  </div>
</div>

第2の崩し駒。ふいうちの先制とつるぎのまいの積みで、受け回しを縦に崩します。あく/はがねでフェアリーに弱い点はXのじゃれつくと役割が分かれ、相手の構成に応じてXと併用するか入れ替えるかを選びます。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" />
    <strong>アーマーガア</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> プレッシャー<br>
      <strong>性格:</strong> わんぱく<br>
      <strong>EV:</strong> H32 B32 D2<br>
      <strong>持ち物:</strong> たべのこし
    </div>
    <div>
      <strong>技構成:</strong> はねやすめ / ボディプレス / てっぺき / とんぼがえり
    </div>
  </div>
</div>

唯一の受け駒。物理高速・積み構築に受け出し、とんぼがえりで対面操作してX・リザードンを安全に通します。はがね/ひこうでじめんを無効化でき、Xが投げづらいガブリアスのじしんに後出しできる数少ないコマです。

<div class="build-card">
  <div class="build-header">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" />
    <strong>サザンドラ</strong>
  </div>
  <div class="build-cols">
    <div>
      <strong>特性:</strong> ふゆう<br>
      <strong>性格:</strong> ひかえめ<br>
      <strong>EV:</strong> H2 C32 S32<br>
      <strong>持ち物:</strong> こだわりスカーフ
    </div>
    <div>
      <strong>技構成:</strong> あくのはどう / りゅうせいぐん / かえんほうしゃ / とんぼがえり
    </div>
  </div>
</div>

スカーフによる速度補完。マスカーニャ（S192）のような速い特殊エースを上から処理します。ふゆうでじめんを無効化するため、ここでもチームの対じめん耐性を支えます。なおこだわり系で実装されているのはスカーフのみのため、火力補正の選択肢はスカーフに限られます。

---

## 選出と立ち回り

シミュレータの実測ログ（後述24戦）から、運用パターンは概ね次の通りです。

- **先発はマンムー固定が基本**。環境を埋めるガブリアス・ラグラージにこおり技・じしんが刺さり、こおりのつぶての先制で削りも残せます。
- **メガはXを主軸に（選出20/24でX採用）**。ねこだましの先制とワイルドボルトで対面を削り、地面以外を縦に処理します。
- **2メガ選出（X＋リザードン同居）を約9/24で採用**。盤面を見て、Xを通すかリザードンYを晴れで通すかを選びます。受けが厚い相手にはリザードン主軸へ切り替えます。
- **高速特殊エースが重いときはサザンドラを投入**し、スカーフでマスカーニャ等を上から落とします。
- **物理高速・積み構築にはアーマーガア**で受け、とんぼがえりで対面を作り直します。

ざっくりした指針としては、「ガブ・ラグ重メタ＝マンムー＋X＋（リザ or ドドゲザン）」「高速特殊メタ＝サザンドラ追加」「受け回し＝リザードン主軸へ」と覚えておくと選出に迷いません。

---

## データ分析①：ライチュウ使用率3位の中身はYが96.6%

「メガライチュウ」と聞いて多くの人が想像するのは、実は**メガライチュウY（特殊）**です。下表の通り、ライチュウ採用者の型データはほぼすべてYのものです。

| 項目 | M-3の値 | 示すもの |
|---|---|---|
| ライチュウナイトY | 96.6% | メガ石はほぼY |
| ライチュウナイトX | 3.0% | Xはごく少数 |
| 性格 おくびょう＋ひかえめ | 95.0% | 特殊型が大半 |
| でんじほう採用 | 96.5% | ノーガード前提のY技 |
| きあいだま採用 | 95.7% | Yの特殊サブ |
| くさむすび採用 | 75.3% | Yの特殊サブ |

ここから読み取れる注意点は、**使用率データに出てくる「ライチュウの型」をそのままメガライチュウXに流用してはいけない**ということです。でんじほう・きあいだまはノーガードを前提にしたY（特殊）の技であり、エレキメイカーのX（物理）はワイルドボルト・じゃれつく等の物理技で組む必要があります。X軸を組むということは、使用率上位の型をそのまま真似るのではなく、わずか3.0%の少数派をゼロから設計し直す作業になります。

---

## データ分析②：シミュレータ検証——Xはメタ拮抗、電気フィールドのシナジーは現状不発

当サイトの対戦シミュレータ（MCTS @400手）で、上記の物理メガライチュウX軸チームを、使用率メタ24構築（各2戦・計48戦）と対戦させました。

- **結果：勝率 52.1%（25勝23敗、p=0.77）**。統計的には**メタと拮抗**しており、Xが特別強くも弱くもないことを示します。X選出率は20/24で、物理Xは実戦で機能はします。
- 一方で、**エレキメイカー（電気フィールド）を活かすシナジーは現状不発**でした。電気フィールド下で素早さが2倍になるサーフテール持ちなど、フィールド展開を勝ち筋に変える相方が、M-3の使用率圏に**実質不在**です。電気フィールドで強化されるアローラライチュウやエモンガといった候補は火力が足りず、「Xならではのギミックで勝つ」構図はまだ環境に存在しません。

つまり現時点では、メガライチュウXは「エレキメイカーのギミックで勝つ」ポケモンではなく、「ガブリアスを上から殴れる物理でんきアタッカーを、メタ拮抗ラインのチームに組み込む」という使い方が現実解です。電気フィールドを軸にした先回り戦略は、相方が揃う将来のシーズンを待つ必要があります。Xを救う鍵は、X自身ではなく**フィールドを勝ち筋に変える相方の登場**にあるというのが、データから導かれる結論です。

---

## まとめ

- ライチュウは使用率3位だが、メガ石の96.6%はY。**「メガライチュウ＝実質メガライチュウY（特殊）」**が実態。
- メガライチュウX（物理）の差別化点は、A187・S178でガブリアス（S169）を上から殴れること。ただしでんき技はガブリアスに無効なため、じゃれつく等のサブ技が必須。
- 2メガ選出（X＋メガリザードンY）を柱に、マンムー・ドドゲザン・アーマーガア・サザンドラで対メタを固めた構成は、シミュレータ上で勝率52.1%とメタ拮抗。
- 電気フィールドのシナジーは相方不在で現状不発。Xを勝ち筋に変えるには、フィールドを活かす相方の環境登場が必要。

関連記事：[メガリザードンX 考察 M-2 物理ほのお/ドラゴン型](/blog/charizard-x-analysis-m2/) ／ [ガブリアス 考察 M-2](/blog/garchomp-analysis-m2/)
