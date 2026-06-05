---
title: '【ポケモンチャンピオンズ】ゲッコウガ考察 M-2 使用率28位 へんげんじざいの型と立ち回り'
description: 'M-2シングルバトルで使用率28位のゲッコウガを徹底分析。S122の高速とへんげんじざい（採用率82.4%）による不意のタイプ変化、れいとうビーム89.6%・あくのはどう75.9%のCS特殊型、タスキ/スカーフ/メガゲッコウガナイト40.8%の持ち物分岐を実データで解説します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-greninja-m2.png'
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
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" />
  <div>
    <h2 style="margin:0 0 8px">ゲッコウガ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">28位</strong>　特性: <strong>へんげんじざい 82.4%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ゲッコウガは**使用率28位**を記録。特性は**へんげんじざい（採用率82.4%）**が主流で、げきりゅう（17.6%）は少数派です。

ゲッコウガの軸は**すばやさ種族値122**という環境屈指の速さと、へんげんじざいによる「繰り出した技のタイプに自分のタイプが変わる」性質です。みず/あくの優秀な攻撃範囲に、れいとうビーム（採用率89.6%）・あくのはどう（75.9%）・ヘドロウェーブ（64.5%）と多彩なサブウェポンを抱え、上から弱点を突き分ける高速特殊アタッカーとして機能します。

持ち物は**ゲッコウガナイト 40.8%・きあいのタスキ 35.2%・こだわりスカーフ 15.5%**と分散しており、メガ進化はあくまで選択肢の1つです。本記事では非メガを基準に、メガゲッコウガ（メガ後S142）の差分も併せて解説します。

---

## なぜゲッコウガが使われるのか

### 1. S122で環境上位のアタッカーを上から叩く

ゲッコウガのすばやさ種族値は**122**。おくびょう＋すばやさ最大振りで、使用率上位の高速アタッカーをほぼ上から叩けます。

- ガブリアス（S102・使用率1位）
- スターミー（S115・20位）
- ゲンガー（S110・10位）
- ミミロップ（S105・13位）
- リザードン（S100・5位）

これらに対し、へんげんじざいで撃つ技のタイプ次第で弱点を突き分けられるのが強みです。例えばガブリアス・カイリュー（ドラゴン/ひこう・16位）にはれいとうビームが×2で通り、上から処理を狙えます。

ただしマスカーニャ（くさ/あく・S123・3位）はわずかに上を取られ、はたきおとす（採用率57.6%）で持ち物を叩き落とされます。トリプルアクセル（72.2%）はみず/あくに×0.5で軽減できますが、先手を取られてタスキを連続技で貫通される点が痛手です。S122は環境トップクラスですが「全てを抜ける」速さではない点に注意してください。

### 2. れいとうビームでドラゴン・じめん勢を上から落とす

ゲッコウガの技で最も採用率が高いのは**れいとうビーム（89.6%）**です。みず/あくのタイプ一致ではないものの、こおり技はドラゴン・じめん・ひこう・くさに刺さり、環境上位のガブリアス（ドラゴン/じめん）・カイリュー（ドラゴン/ひこう）に×2で通ります。S122で上を取れるため、これらの高速ドラゴンを先手で削れるのが大きな採用理由です。

### 3. へんげんじざいで「どの技も一致技」になる

へんげんじざい（採用率82.4%）は、繰り出す技のタイプに自分のタイプが変化する特性です。れいとうビームを撃てばこおり、あくのはどうを撃てばあくと、**選んだ技が常にタイプ一致補正×1.5**になります。サブウェポンを一致火力で撃てるため、相手の弱点に合わせて技を選ぶだけで等倍以上＋一致補正の打点を出せます。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">67</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">103</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">71</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:61%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">122</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

すばやさ122・とくこう103が軸で、攻撃範囲の広さと速さで戦うアタッカーです。HP72・B67・D71と耐久はいずれも低く、弱点技はもちろん等倍でも受からない場面が多いため、**先手で殴るか、タスキで1回耐えて行動する**のが基本になります。

### メガ進化（ゲッコウガナイト採用率40.8%）

ゲッコウガナイトの採用率は40.8%で、半数以上はタスキ・スカーフ等の非メガ構成です。メガ進化するとすばやさ142・とくこう133まで上がり、特性はへんげんじざいのまま据え置かれます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">72</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">72</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">125</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">67</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+10</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">103</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">133</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">71</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+10</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">122</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#059669">142</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+20</td>
</tr>
</tbody>
</table>
</div>

メガ後はすばやさ142でマスカーニャ（S123）も上から叩けるようになり、とくこう133で火力も底上げされます。一方、タスキ・スカーフを持てないため「1回耐える保険」や「相手依存せずスカーフで上を取る」役割は失われます。メガ枠を消費してまで素早さ・火力を伸ばすか、タスキ・スカーフで小回りを利かせるかが構築単位の選択になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="みず" />
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

あくタイプによりエスパー技を無効化できるのが対戦上重要で、スターミー（みず/エスパー）・マフォクシー（ほのお/エスパー）のエスパー打点を透かせます。一方、弱点のでんき・くさ・かくとう・むし・フェアリーは5タイプと多く、低耐久と合わせて等倍でも被弾は痛い点に注意が必要です。なお、へんげんじざいは技を撃った後にそのタイプへ変わるため、初手で撃つ前の被弾はみず/あくのタイプ相性で受けます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">89.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">へんげんじざいで一致補正。ガブリアス・カイリュー等ドラゴンへの主力打点。10%こおり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致技。ゴースト・エスパーに刺さる。20%ひるみ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヘドロウェーブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー（アシレーヌ・フラエッテ）・くさへの打点。10%どく</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なみのり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">44.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致技。リザードン・じめん勢への安定打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>みずしゅりけん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15×2〜5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1の連続技。相手のSに関わらず先制。タスキ・低HP処理に</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイドロポンプ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なみのりより高威力だが命中80。みず最大火力枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>くさむすび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">重さ依存</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン等の重いみず・じめん・いわへの打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくびし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技。初手の高速展開で後続を補助</td>
</tr>
</tbody>
</table>
</div>

れいとうビーム・あくのはどう・ヘドロウェーブの3枠でドラゴン・ゴースト・フェアリーを広くカバーし、4枠目をなみのり（みず一致の安定打点）かみずしゅりけん（先制）で選ぶのが標準的な技構成です。

---

## 主要型の解説

型①・型②は性格分布（ひかえめ／おくびょう）と持ち物分布を指標としています。

### 型1: きあいのタスキ高速アタッカー型（最多級）

**指標: きあいのタスキ 35.2%／ひかえめ 52.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">タスキCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り。最多はH+2）<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・れいとうビーム<br>
・あくのはどう<br>
・ヘドロウェーブ / なみのり<br>
・みずしゅりけん / どくびし
</div>
</div>
</div>

**強み:**

きあいのタスキで弱点技を1回耐え、S122から確実に1手返せます。低耐久のゲッコウガにとって「1回行動を保証する」価値は大きく、初手から相手の弱点をへんげんじざいの一致技で突くか、どくびしを撒いて後続を補助するかを選べます。みずしゅりけんを採用すれば、タスキで耐えた次のターンに先制連続技で削り残しを処理できます。

**弱み:**

タスキは天候ダメージや先制技・設置ダメージで簡単に潰れます。ステルスロックが撒かれた盤面では受け出しが効かず、メガと異なり火力が控えめなため、相手の高耐久（カバルドン・ブリジュラス等）を一撃で抜けない場面が増えます。EVのCS振りでとくこう・すばやさを最大化しているため、被弾には特に脆くなります。

---

### 型2: メガゲッコウガ型（ゲッコウガナイト 40.8%）

**指標: ゲッコウガナイト 40.8%／おくびょう 37.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0658-00.webp" alt="メガゲッコウガ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガCS型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> へんげんじざい<br>
<strong>性格:</strong> おくびょう（S↑ A↓）<br>
<strong>EV:</strong> C32 S32（CS振り）<br>
<strong>持ち物:</strong> ゲッコウガナイト
</div>
<div>
<strong>技構成:</strong><br>
・れいとうビーム<br>
・あくのはどう<br>
・ヘドロウェーブ / なみのり<br>
・ハイドロポンプ / みずしゅりけん
</div>
</div>
</div>

**強み:**

メガ後はすばやさ142で、タスキ型では同速以下になるマスカーニャ（S123）を上から叩けます。とくこう133に上がるため、タスキ型では削り切れない高耐久にも一致技がより通りやすくなります。タスキ型が「1回耐えて返す」のに対し、メガ型は「最初から上を取って押し切る」純粋な火力・速度型です。

**弱み:**

タスキ・スカーフを持てないため、弱点技を耐える保険がなく、低耐久のまま弱点・等倍を被弾します。メガ枠を1体に固定するため、構築全体のメガ選択を縛る点も非メガ型にはない制約です。

---

### 補足: こだわりスカーフ型（15.5%）

スカーフ型はS122にスカーフ補正がかかり、メガゲッコウガ（S142）すら上から叩ける速度を得ます。技を縛られるため、れいとうビーム・あくのはどう・なみのりなど範囲の広い技で固めるのが基本です。最速スカーフ勢（スカーフガブリアス等）に対しても先手を取れる一方、初手から技固定される読み合いが発生します。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ゲッコウガと相性がはっきり出るポケモンを有利・不利の両面から挙げます。S122（おくびょう最大振り）でほぼ上を取れる一方、HP72・B67・D71と耐久は低く、弱点（でんき・くさ・かくとう・むし・フェアリー）はもちろん等倍でも被弾は重い点に注意してください。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビームが×4（ドラゴン2×じめん2）。S122＞102で先手。確定1発圏。ただしスカーフガブリアスのげきりん（採用率47.9%）には先手を取られ等倍で重い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カイリュー（16位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビームが×4（ドラゴン2×ひこう2）。S122＞80で先手。マルチスケイル下でも高乱数。ただししんそく（45.6%）の先制で削り返される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なみのりが×2（ほのお弱点）。S122＞100で先手。低耐久同士の撃ち合いで上から押せる。エアスラッシュ（32.9%）等のひこう技は等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくのはどうが×2（ゴースト弱点）。S122＞110で先手。シャドーボール（71.1%）はあくで×0.5に軽減でき、ヘドロウェーブ（81.7%）はみず/あくに等倍</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">サザンドラ（21位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビームが×2（ドラゴン弱点・あくは等倍）。S122＞98で先手。かえんほうしゃ（67%）はみずで×0.5に軽減でき、撃ち合いで優位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）が×2弱点（でんき）。S122＞86で先手だが一撃で落としにくく、被弾で崩れる。みず技も半減され打点が乏しい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利（メガなら五分）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123でこちらより速い。こおり技のトリプルアクセル（72.2%）はみずで×0.5だが、はたきおとす（57.6%・あく等倍）で持ち物を叩き落とされ、連続技でタスキも貫通される。メガ（S142）なら上を取れる</td>
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
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">S123で非メガゲッコウガより速く、はたきおとす（57.6%）でタスキ・スカーフを叩き落としつつ上から殴られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ進化してS142で上を取り、ヘドロウェーブ（くさ×2で刺さる）で先に削る。または高速のひこう・ほのおタイプを後続に置いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10まんボルト（56.8%）が×2弱点。みず技・れいとうビームともに×0.5で半減され、あくのはどう（等倍）しか通らず打点が薄く、撃ち合いで押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技を半減できるくさ・じめん枠（フシギバナ等）に引いて受ける。じめんタイプならボルトチェンジも透かせる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（97.0%）が×2弱点（フェアリー）。アクアジェット（66.6%）の先制でタスキ後やスカーフ型の隙を突かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブ（どく×2でフェアリーに刺さる）で先制して落とす。落としきれない個体にはどく・はがね・くさタイプを後続に置いてフェアリー技を半減して受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ドラゴンでみず・れいとうビームともに半減〜等倍。高耐久で一撃で抜けず、こちらの低耐久では撃ち合いに時間がかかり不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさむすび（重量級に高威力）かじめん・かくとう枠（ルカリオのインファイト等）を合わせてはがね弱点を突く</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0003-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フシギバナ（27位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ/どくでみず技を半減、こちらはくさ×2弱点を突かれる。れいとうビームは×2で刺さるがD100で一撃には足りず、低耐久のこちらは反撃のくさ技×2で先に落とされやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ヘドロウェーブはくさに半減されるため、ほのお・エスパー・ひこう枠（リザードン等）を合わせてくさ弱点を突く</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は「ゲッコウガの弱点（でんき・くさ・フェアリー）を等倍以上で突き、かつ低耐久のこちらを撃ち合いで倒しきる相手」と「S122を上回る、または先制技で隙を突く相手」に大別されます。いずれも単体での切り返しは難しいため、後続のタイプ補完で受ける構築が前提になります。

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0003-00.webp" alt="フシギバナ">
    <div class="name">フシギバナ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ/どくでゲッコウガの弱点でんき・くさを半減し、苦手なウォッシュロトムを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン">
    <div class="name">ラウドボーン</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのお/ゴーストでくさ・むしを半減。高耐久でゲッコウガの低耐久を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき無効のじめん枠。ウォッシュロトムに上から打点を持つ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでフェアリー・くさ等を半減し、苦手なフェアリーを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ほのおでくさ・むし・はがねを半減。フシギバナ等のくさ受けに打点</div>
  </div>
</div>

**パーティ構成の基本方針:**

ゲッコウガは耐久が低く弱点も5タイプと多いため、残り5体で以下の役割を補います。

1. **でんき対策**: じめん（ガブリアス）やくさ（フシギバナ）でウォッシュロトムのでんき技を受ける枠
2. **フェアリー対策**: はがね・どく（ブリジュラス・フシギバナ）でアシレーヌ等のフェアリー技を半減する枠
3. **くさ対策**: ほのお（リザードン・ラウドボーン）でフシギバナ等のくさ技を半減する枠
4. **先制技ケア**: マルチスケイルカイリューのしんそくやアシレーヌのアクアジェットに削られた後を、高耐久の後続で受け止める

---

## データ分析①：技採用率に見る「弱点を突き分ける」設計

ゲッコウガの技採用率は、みず/あくの一致技より**サブウェポンの採用率が高い**点に特徴があります。

| 技 | タイプ | 採用率 | 主な役割 |
|---|---|---|---|
| れいとうビーム | こおり | 89.6% | ドラゴン・じめん・ひこう・くさ |
| あくのはどう | あく | 75.9% | ゴースト・エスパー |
| ヘドロウェーブ | どく | 64.5% | フェアリー・くさ |
| なみのり | みず | 44.4% | ほのお・じめん・いわ |

最も採用率が高いのは一致技のなみのり（44.4%）ではなく、**非一致のれいとうビーム（89.6%）**です。通常、タイプ一致技は補正×1.5で威力が伸びるため優先されますが、へんげんじざいによって**どの技も一致補正がかかる**ため、ゲッコウガは「火力が出る一致技」ではなく「弱点を突けるタイプの技」を基準に技を選べます。

結果、れいとう・あく・どくの3枠で、環境上位のドラゴン（ガブリアス・カイリュー）・ゴースト（ゲンガー）・フェアリー（アシレーヌ・フラエッテ）を広く弱点圏に収める構成が標準化しています。みず技がなみのり44.4%・みずしゅりけん28.1%・ハイドロポンプ15.1%と分散するのも、「みず打点は4枠目で役割に応じて1つ選べばよい」という、特性が生む技選択の自由度の表れです。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">指標</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">持ち物</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">タスキCS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>タスキ 35.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">1回耐えて確実に1手返す。設置・先制で柔軟</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">天候・ステロでタスキが潰れる。火力控えめ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガCS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガナイト 40.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゲッコウガナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">S142でマスカーニャ抜き。C133で火力増</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">保険なしで低耐久のまま。メガ枠を縛る</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">スカーフCS型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカーフ 15.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">メガS142超えの最速。最速スカーフ勢も抜く</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技固定の読み合い。火力は無補正</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ゲッコウガはS122とへんげんじざいを軸に、れいとうビーム・あくのはどう・ヘドロウェーブで環境上位のドラゴン・ゴースト・フェアリーを上から弱点で叩く高速特殊アタッカーです。特性により非一致技でも一致補正が乗るため、火力ではなく相手の弱点を基準に技を選べる柔軟さが最大の武器です。

持ち物はタスキ35.2%・ゲッコウガナイト40.8%・スカーフ15.5%と分散しており、「1回耐える」「火力と最速を伸ばす」「最速で上を取る」のどれを取るかで役割が変わります。一方、HP72・B67・D71の低耐久と5タイプの弱点は構築単位の補完が前提で、苦手なウォッシュロトム・アシレーヌ・くさ受けには後続のタイプ補完で対応する必要があります。

---

## 関連記事

- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [苦手なくさ受けの天敵 リザードンのM-2考察](/blog/charizard-y-analysis-m2/)
- [弱点フェアリーで上を取られる アシレーヌのM-2考察](/blog/primarina-analysis-m2/)
