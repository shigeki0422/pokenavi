---
title: '【ポケモンチャンピオンズ】メガギャラドス考察 M-2使用率10位 型・タイプ変化・立ち回り'
description: 'M-2シングルバトルで使用率10位のメガギャラドスを徹底分析。メガ進化でみず/ひこう→みず/あくへのタイプ変化、特性かたやぶり、A155+りゅうのまいの全抜き性能、りゅうのまい積み型・ちょうはつ型の3大構築を実データで徹底解説します。'
pubDate: '2026-05-23'
draft: false
heroImage: '../../assets/hero-gyarados-m2.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" />
  <div>
    <h2 style="margin:0 0 8px">メガギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">10位</strong>　メガ石採用率: <strong>ギャラドスナイト 64.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン開始8日目（2026/05/20）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ギャラドスは**使用率10位**を記録。そのうち**64.6%がギャラドスナイトを採用**しており、約3割強は非メガ構成での運用となっています。

メガギャラドスの最大の特徴は**メガ進化によるタイプの変化**です。メガ前はみず/ひこうタイプですが、メガ進化後は**みず/あくタイプに変わります**。これにより弱点・耐性・無効のセットが大きく変化し、使い方と立ち回りも変わります。さらに特性**かたやぶり**（相手の特性を無視して技を使える）により、ふゆう持ちポケモンへのじしんも通ります。A155というトップクラスの攻撃力とりゅうのまいの組み合わせで、積み後の全抜き性能は環境トップクラスです。

---

## 重要：メガ進化でタイプが変わる！

メガギャラドスを使う上で**最も重要な知識**がタイプ変化です。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">状態</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">タイプ</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">じめん技</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">エスパー技</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">でんき技</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">かくとう技</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">フェアリー技</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">いわ技</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガ前（みず/ひこう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">× 無効</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#94a3b8">○ 等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">▲ ×4弱点</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#22c55e;font-weight:bold">◎ 半減</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#94a3b8">○ 等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">▲ ×2弱点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガ後（みず/あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#94a3b8">○ 等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">× 無効</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">▲ ×2弱点</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">▲ ×2弱点</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">▲ ×2弱点</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#94a3b8">○ 等倍</td>
</tr>
</tbody>
</table>
</div>

**特に重要なポイント:**

- **じめんが無効→等倍に悪化** → ひこうタイプを失うため、ガブリアスのじしんが等倍で通るようになる
- **かくとうが半減→×2弱点に悪化** → メガ前は半減で受けられたかくとう技が、メガ後は弱点になる
- **フェアリーが等倍→×2弱点に悪化** → あくタイプの弱点としてフェアリー技が新たに刺さるようになる
- **でんき弱点が×4→×2に軽減** → ひこうタイプとの複合で×4だったでんき弱点がみず単換算の×2に下がり、耐えて反撃できる場面が増える
- **いわ弱点が×2→等倍に軽減** → ひこうのいわ弱点が消え、いわ技を等倍で受けられるようになる
- **エスパーが等倍→無効に改善** → あくタイプによりエスパー技を完全に無効化できる

この変化を理解することが、メガギャラドスの正しい使い方の第一歩です。「ひこうタイプだからじしんが通らない」という読みは**メガ後は通用しません**。

---

## なぜ今メガギャラドスが強いのか

### 1. りゅうのまい後のA155で全抜き性能

メガギャラドスの最大の破壊力は**A155 × りゅうのまい**の組み合わせです。

りゅうのまいはAとSを1段階アップする積み技です。いじっぱりA最大振りのこうげき実数値227が、1積みで1.5倍の約340相当まで跳ね上がります。みず一致のたきのぼり（BP80）やじしん（BP100）と組み合わせれば、積み後は多くの環境ポケモンを確定圏内に収められます。

こおりのキバは採用率45.2%で、環境上位のガブリアス（こおり×4弱点）への確定打点です。りゅうのまいを1積みされたまま処理しきれないと、試合がそのまま終わることもあります。

### 2. 特性かたやぶりの効果

メガ進化後の特性**かたやぶり**は「相手の特性を無視して技を使える」効果です。最も重要な使い道は**ふゆう持ちポケモンへのじしんが通る**点です。通常ふゆうを持つポケモン（ロトム系など）にじしんが無効化されますが、かたやぶりなら関係なく命中します。

ただし、かたやぶりには**火力の補正はありません**。こおりのキバ・かみくだく・たきのぼりはいずれも素の威力そのままです。メガギャラドスの攻撃力の源泉はA155の高い種族値とりゅうのまいの積み技にあります。

### 3. メガ進化前のいかくで物理ダメージを軽減

メガ進化前のギャラドスの特性は**いかく**で、場に出た瞬間に相手のこうげきを1段階下げます。これを活かして「いかくで相手の物理火力を下げてからメガ進化する」という立ち回りが可能です。

いかくで相手のこうげきをあらかじめ下げておくことで、りゅうのまいを積むターンの被ダメージを軽減できます。物理アタッカーが多い相手に対して特に有効で、積み技を通す準備を安全に進められます。

### 4. ちょうはつによる変化技封じ

採用率30.6%のちょうはつは、相手の積み技・回復技・ステルスロックなどを2ターン封じます。積み合いになりやすい環境で、先にちょうはつを打つことで相手のつるぎのまいやてっぺきをシャットアウトできます。

メガギャラドスのS81（いじっぱりでS実数値133、ようきで146）は環境でやや遅めですが、無振りのサポート系ポケモンよりは速いため、ちょうはつを先手で打てるシーンもあります。

---

## 基本スペック

### 種族値（メガ後）

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">155</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">109</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">70</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong>130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:36px;text-align:right;color:#2563eb">640</span>
  </div>
</div>

A155は環境トップクラスの攻撃力です。D130という高い特防とB109で物理・特殊ともに一定の耐久を持っています。さらにいかくで相手のこうげきを下げることで、物理方面では数値以上に硬く立ち回れます。S81はやや遅く、環境の主要アタッカーより遅いため、りゅうのまいでS補強するか後手で受けてから切り返す立ち回りが基本になります。

### メガ前→メガ後ステータス変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステータス</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ前</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">メガ後</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HP</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">こうげき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">125</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">155</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ぼうぎょ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">79</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">109</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+10</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">とくぼう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>130</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+30</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">すばやさ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">81</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#94a3b8">変化なし</td>
</tr>
</tbody>
</table>
</div>

### タイプ・弱点（メガ後: みず/あく）

<div class="type-row">
  <strong>タイプ（メガ後）：</strong>
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
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

**メガ前との弱点比較:**

メガ前はでんき×2・いわ×2・氷×2の弱点を持っていましたが、メガ後は**いわ×2弱点がなくなり、かくとう・むし・くさ・フェアリー弱点が加わります**。また、メガ前はじめんが無効でしたが、**メガ後はじめんが等倍で通ります**。ガブリアスのじしんには特に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たきのぼり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">84.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">安定したみず打点。命中100・ひるみ20%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・S+1。1積みで全抜き射程に入るポケモンが激増</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>65.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・でんきタイプ（ブリジュラス・ハラバリー等）への確定打点。高採用必須技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>45.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスに4倍。りゅうのまい後に確定1発圏内。命中95%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">38.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずタイプに等倍以上。アシレーヌ・カバルドンへの打点。命中85%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2ターン変化技封じ。相手の積み技・回復技・ステロを封じる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60（条件達成時120）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後攻確定。そのターン相手から技ダメージを受けていれば威力2倍（120）。こおりのキバとの選択肢</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やけっぱち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75（条件達成時150）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお打点。前ターンに自分が動けなかった・技を外した・失敗した場合に威力2倍（150）。非メガ採用の可能性も</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみくだく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あく一致打点。Bダウン20%の追加効果あり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼりより威力高いが命中率90。火力重視での採用</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

### 型1: りゅうのまい積み型（メガ・最多採用）

**性格採用率: いじっぱり 45.1%（最多）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">りゅうのまいASいじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（98.8%）※メガ後かたやぶり<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り）<br>
<strong>持ち物:</strong> ギャラドスナイト
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・たきのぼり<br>
・じしん<br>
・こおりのキバ / パワーウィップ
</div>
</div>
</div>

**強み:**

いじっぱりA最大振りでこうげき実数値227を活かします。りゅうのまいを1積みするとAが1.5倍（約340相当）になり、こおりのキバ（BP65）でガブリアスのこおり4倍弱点を突けば**確定1発**圏内に入れられます。

S81はいじっぱりでS実数値133とやや遅いですが、りゅうのまいでS+1になると約199相当まで上がり、環境の多くのポケモンを追い越せます。**いじっぱり**を採用することで、1積み後のA火力を最大化する設計です。

技範囲はたきのぼり（みず）・じしん（じめん）・こおりのキバ（こおり）の組み合わせで、でんきタイプ・ドラゴンタイプ・ほのおタイプなど幅広い相手に打点を持てます。パワーウィップはみず・くさ以外への打点として選択肢になります。

**ようきとの使い分け:**

採用率2位のようきAS（41.2%）はS↑補正の型です。S実数値146（いじっぱりは133）で積み前の素早さがやや高く、りゅうのまいを積む前の行動順で有利になる場面が増えます。一方、A実数値はいじっぱり227に対しようき207と約9%低く、積み後の火力はいじっぱりに劣ります。

積み前のS13差で先に動きたいならようき、積み後のA火力で確定数を稼ぎたいならいじっぱりが向きます。

**弱み:**

S81は積み前では環境の主要アタッカーに先手を取られます。りゅうのまいを打つターンが必要なため、対戦相手にちょうはつを打たれると詰み状態になるリスクがあります。

また、メガ進化後はひこうタイプを失うためじめんが等倍で通るようになります。メガ前のじめん無効を前提にした立ち回りは、メガ進化後には通用しない点に注意が必要です。

---

### 型2: ちょうはつ積み型

**性格採用率: ようき 41.2%（積み前の素早さ重視）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ちょうはつ+りゅうのまいようき型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（98.8%）※メガ後かたやぶり<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A32 S32（AS振り）<br>
<strong>持ち物:</strong> ギャラドスナイト
</div>
<div>
<strong>技構成:</strong><br>
・ちょうはつ<br>
・りゅうのまい<br>
・たきのぼり<br>
・じしん / こおりのキバ
</div>
</div>
</div>

**ちょうはつの使い方:**

ちょうはつは相手の変化技を2ターン封じます。主な用途は以下の通りです。

1. **相手のりゅうのまい封じ**: メガギャラドスのミラー対策として、相手のりゅうのまいを先に封じる
2. **カバルドンのステロ封じ**: カバルドン（8位）が初手ステロを打ってくるのをちょうはつで阻止
3. **回復技封じ**: ねむるやアシストパワー準備を封じる
4. **相手の積み技カウンター**: つるぎのまいやりゅうのまい等の積み技をシャットアウト

ようき型でS実数値146を確保することで、いじっぱり（133）より素早さが上がり、ちょうはつを先手で打てる相手が増えます。ちょうはつを打った後、相手の次の行動を読んでりゅうのまいを積むか攻撃するかを判断します。

**弱み:**

技スロットにちょうはつを使うため、技範囲が積み型より狭くなります。こおりのキバかじしんの一方のみ採用になるケースが多く、特定タイプへの打点が欠落します。

---

### 型3: 非メガ耐久型（ギャラドスナイト非採用 35.4%）

**採用持ち物: たべのこし 17.1% / オボンのみ 6.9% / ラムのみ 5.2% / カゴのみ 3.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス（非メガ）" style="width:48px;height:48px">
  <strong style="font-size:1.05em">非メガ耐久型（みず/ひこう）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（98.8%）<br>
<strong>性格:</strong> わんぱく（B↑ C↓）/ いじっぱり<br>
<strong>EV:</strong> HB または AS<br>
<strong>持ち物:</strong> たべのこし / オボンのみ / ラムのみ
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい / ちょうはつ<br>
・たきのぼり<br>
・じしん<br>
・こおりのキバ / ねむる
</div>
</div>
</div>

**非メガの強みと使い方:**

非メガ構成の最大の利点は、**他のメガ進化ポケモンと同じパーティに採用できる**点です（1メガルール）。ギャラドスをあくまでサブアタッカーとして位置づけ、パーティの別ポケモンにメガ進化権を渡せます。

たべのこしを持たせたHB型は、メガ前のみず/ひこうタイプのじめん無効を活かしてガブリアスのじしんを完全シャットアウトしながら回復を積み重ねます。

ラムのみはやけど・麻痺・ねむりへの対策として採用。ちょうはつを使った後にりゅうのまいを積むパターンが安定します。カゴのみはねむる採用型での起き上がりサポートです。

非メガのA125でも、りゅうのまい後の破壊力は十分なレベルにあります。

---

## 環境ポケモンへの相性分析

### 有利なポケモン

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ やや有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうのまい後のこおりのキバで確定1発。ただしメガ後はじしんが通るので注意</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">カバルドン（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップでくさ×2弱点。ちょうはつでステロ封じも可能</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガY（ほのお/ひこう・61.4%）にはたきのぼりがみず×2弱点。ただしメガX（ほのお/ドラゴン・37.2%）には等倍</td>
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
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリー×2弱点。ムーンフォースが痛い</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップで逆に弱点を突ける（くさ×2）。りゅうのまい後なら優位に</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき技（10まんボルト等）でギャラドスのでんき×2弱点を突いてくる。タイプははがね/ドラゴンだがでんき技を使う代表格</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんでブリジュラスのじめん弱点を突く。パーティのじめんタイプで処理</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとう×2弱点。インファイトが刺さる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガルカリオ（S実数値最速180）に先手を取られる。りゅうのまいが通る状況を作る必要あり</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">環境1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき対策。メガギャラドスのでんき弱点をフォロー</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">環境6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">かくとう・むし技を半減で受ける。ギャラドスの弱点補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ">
    <div class="name">ルカリオ</div>
    <div class="rate">環境9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">非メガギャラドスとの組み合わせで同パーティに入れられる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">環境3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ/あく。エスパー・ゴーストへのあく技、みず・じめんへのくさ技で技範囲補完</div>
  </div>
</div>

**パーティ構成の基本方針:**

以下の役割を補う5体を選ぶのが基本です。

1. **でんき対策**: じめんタイプ（ガブリアス等）やでんき無効・半減のポケモン
2. **フェアリー対策**: はがね・どくタイプでアシレーヌ等に対応
3. **かくとう対策**: ひこうタイプ（アーマーガア等）でメガルカリオのインファイトを半減
4. **先手アタッカー**: S81と遅めのギャラドスの代わりに先制できるポケモン

非メガ型を選択する場合は、別のメガ進化ポケモン（メガルカリオ・メガリザードン等）と組み合わせてメガ進化権を有効活用するパーティ設計が有効です。

---

## データ分析：非メガ35.4%が示すタイプ変化のトレードオフ

ギャラドスナイトの採用率は64.6%で、環境上位10体の中では比較的「メガ進化しない選択肢」が多いポケモンです。

| 選択 | タイプ | A | じめん耐性 | 特徴 |
|---|---|---|---|---|
| 非メガ型（64.6%） | みず/ひこう | A125 | **無効**（ひこう） | でんき×2倍弱点 |
| メガ型（35.4%） | みず/あく | **A155** | **等倍**（じめん） | でんき半減 |

メガ進化するとこうげきが30上昇する一方、**じめん無効が失われじめんが等倍で通るようになる**というタイプ変化が発生します。M-2環境ではガブリアス（使用率1位・じしん採用率99.2%）が最多使用ポケモンであるため、このじめん等倍化は無視できないリスクです。

非メガ型の持ち物採用率を見ると、たべのこし17.1%・オボンのみ6.9%・ラムのみ5.2%・カゴのみ3.8%と、**耐久・状態異常対策アイテムが上位**を占めており、メガ進化権を別のポケモンに譲った上で長期戦を見据えた構成が多いことが分かります。

非メガ型はじめん無効・ひこうタイプを維持したまま強力なアタッカーとして機能し、かつメガ進化権を別のポケモンに回せる点で独自の強みがあります。35.4%という採用率はその実用性を裏付けています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">りゅうのまい積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">りゅうのまい・たきのぼり・じしん・こおりのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積み後の全抜き力最大。A火力を最大化</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">積みターンが必要。ちょうはつで詰み</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">ちょうはつ+積み型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">ちょうはつ・りゅうのまい・たきのぼり・じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">相手の積み技・ステロを封じてから積める</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">技範囲が狭い。A火力がやや低下</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">非メガ耐久型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく/いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">りゅうのまい・たきのぼり・じしん・ちょうはつ/ねむる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">他メガとの共存。じめん無効（ひこう）維持</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">A125でメガ後より火力低下</td>
</tr>
</tbody>
</table>
</div>

**総評:**

メガギャラドスは「メガ進化によるタイプ変化」を理解した上で使うことが最重要です。メガ前のみず/ひこうとメガ後のみず/あくでは、じめん有効・エスパー無効という大きな変化があります。

A155という最高水準の攻撃力とりゅうのまいによる全抜き性能は環境トップクラスで、積み後のこおりのキバでガブリアス（環境1位）のこおり4倍弱点を突いて確定1発圏内に入れられるため、環境適応力が非常に高いポケモンです。

メガリザードンY・カバルドンへの明確な有利と、こおりのキバ採用時のガブリアス処理力を活かしつつ、適切なパーティ構成と「メガ後はじしんが通る」という知識を持って使えば、ランク上位を目指すための強力な駒になります。

非メガ型でも十分な破壊力があるため、別のメガ進化をエースに据えたパーティのサブアタッカーとして使う選択肢も有効です。使用率10位の約35%が非メガを選んでいるという事実が、ギャラドスの非メガでの信頼性を示しています。

---

## 関連する考察記事

- [【ポケモンチャンピオンズ】ガブリアス考察 M-2使用率1位](/blog/garchomp-analysis-m2/)
- [【ポケモンチャンピオンズ】メガルカリオ考察 M-2](/blog/lucario-analysis-m2/)
- [【ポケモンチャンピオンズ】アシレーヌ考察 M-2](/blog/primarina-analysis-m2/)
