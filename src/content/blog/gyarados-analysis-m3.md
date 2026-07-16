---
title: '【ポケモンチャンピオンズ】ギャラドス考察 M-3 使用率15位・型別解説とM-2との変化'
description: 'M-3シングルバトルで使用率15位のメガギャラドスを分析。ギャラドスナイト56.5%・りゅうのまい70.5%・M-2比較でじしん・こおりのキバが消えた理由まで、DBデータから徹底解説します。'
updatedDate: '2026-07-03'
pubDate: '2026-07-03'
heroImage: '../../assets/hero-gyarados-m3.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">ギャラドス / メガギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
      <span style="color:#888;font-size:0.85em">メガ後→</span>
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">15位</strong>（M-2: 12位）　メガ石採用率: <strong>ギャラドスナイト 56.5%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズンの集計です。M-2版は[メガギャラドス考察 M-2](/blog/gyarados-analysis-m2/)をご覧ください。

M-3シングルバトルでギャラドスは**使用率15位**。M-2の12位から3つ順位を下げました。メガ石採用率は62.9%（M-2）→**56.5%**（M-3）に減少しており、非メガ採用者が増加しています。また技構成はM-2から大きく変化しており、M-2で63.7%・45.5%だった**じしん・こおりのキバが共にトップ6から消え**、代わりにパワーウィップとゆきなだれの比重が高まっています。

---

## データ分析①：M-2→M-3の技・持ち物採用率変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たきのぼり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+4.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">73.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>70.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">41.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+6.8pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#94a3b8">変化なし</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+1.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみくだく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.0pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">63.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">圏外</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">大幅減</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">45.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">圏外</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">大幅減</td>
</tr>
</tbody>
</table>
</div>

M-3で最も目を引く変化は**じしんとこおりのキバがトップ6から完全に消えた**点です。M-2ではじしん63.7%・こおりのキバ45.5%が主力打点だったにもかかわらず、M-3ではこれらに代わってパワーウィップが47.8%（+6.8pp）に増加しています。

この変化の背景として、M-2で多かった**ウォッシュロトム（じめん技をふゆうで無効化する相手）への対策としてのじしん**の価値が、M-3環境ではロトムの順位変動により相対的に低下したことが考えられます。またガブリアス（1位）のじしん採用率99.5%というデータから、メガ進化後のじめん弱点（ひこうタイプ喪失）を避けるため、じしんを持たずにメガ前後のリスクを減らす構築が増えた可能性があります。こおりのキバに代わりゆきなだれが21.3%に残っており、先制打よりも受け流し後の反撃を意識した技選択への移行が読み取れます。

持ち物のシーズン比較：

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-2</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギャラドスナイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">62.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>56.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-6.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">23.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">+5.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+2.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-2.0pp</td>
</tr>
</tbody>
</table>
</div>

M-3ではギャラドスナイトが6.4pp減少し、たべのこし（23.2%）が大幅増加しています。M-2では過半数だったメガ石がM-3では56.5%にとどまり、非メガの耐久型（たべのこし・オボンのみ合計33.2%）の選択肢が広がっています。

---

## メガ進化でタイプが変わる

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">状態</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">タイプ</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">じめん</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">でんき</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">かくとう</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">いわ</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">エスパー</th>
  <th style="padding:10px 8px;border:1px solid #cbd5e1">フェアリー</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガ前（みず/ひこう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">無効</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#dc2626;font-weight:bold">×4</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#22c55e;font-weight:bold">半減</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">×2</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1">等倍</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">メガ後（みず/あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin:2px">
    <img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin:2px">
  </td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">×2</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">×2</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1">等倍</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#2563eb;font-weight:bold">無効</td>
  <td style="padding:8px 8px;border:1px solid #cbd5e1;color:#ef4444;font-weight:bold">×2</td>
</tr>
</tbody>
</table>
</div>

メガ進化後の主な耐性変化:

- **じめん無効→等倍**：ひこうタイプを失うため、ガブリアス（1位）のじしん（採用率99.5%）が等倍で通るようになる
- **でんき×4→×2**：最大の弱点が軽減される
- **かくとう半減→×2**：メガ進化でかくとうが弱点に転じる
- **エスパー等倍→無効**：あくタイプ獲得によりエスパー技を完全無効化
- **フェアリー等倍→×2**：ミミッキュ（2位）のじゃれつく（96.4%）、アローラキュウコン（9位）のムーンフォース（49.6%）が弱点に変わる

### タイプ別弱点・耐性（メガ後：みず/あく）

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

---

## 基本スペック

### 種族値（メガ前→メガ後）

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>109</strong></td>
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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:700">合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb;white-space:nowrap">540</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#2563eb;white-space:nowrap">640</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#16a34a">+100</td>
</tr>
</tbody>
</table>
</div>

メガ進化でA・B・D各+30。S81はメガ前後で変わらず、りゅうのまいを積む前の素早さで環境上位の多くに後れを取ります。

---

## なぜM-3でも採用されるのか

### いかく→りゅうのまいのフィニッシャーとしての突破力

ギャラドスの基本的な採用理由は、場に出た瞬間の特性**いかく**（採用率98.5%）で相手のこうげきを1段階下げ、物理ダメージを軽減しながらりゅうのまいを積んで全抜きを狙える点です。メガ進化後の特性**かたやぶり**は相手の特性を無視して技を発動できるため、ふゆう持ちポケモンへのじめん技も命中します（ただしM-3ではじしん自体の採用率がトップ6外）。

最多EV「A2-B32-S32 ようき」（採用率24.0%）での実数値（Lv50・個体値31）:

- **HP**: 170
- **A（メガ後、EV2）**: 177
- **B（メガ後、EV32）**: 161
- **S（EV32、ようき×1.1）**: 146

りゅうのまい1積み後のA実数値は177×1.5=**265**（端数切り捨て）。いじっぱりA32型（A実数値227）の1積み後は**340**となり、技範囲より火力を優先する場合はいじっぱりの方が突破力で上回ります。

### たきのぼり+パワーウィップが主力打点

M-3の主力2技はたきのぼり（90.7%）とパワーウィップ（47.8%）です。

- **たきのぼり（BP80・みず）**：みず一致打点。カバルドン（じめん）に×2で通る
- **パワーウィップ（BP120・くさ）**：ガブリアス（ドラゴン/じめん）に等倍、カバルドン（じめん）には等倍。みず技が通りにくいみず複合相手へのカバレッジ

M-2にあったじしん（63.7%）とこおりのキバ（45.5%）がM-3では圏外になっており、じめん・こおりのカバレッジより、みず打点の安定性とくさ打点の維持を選ぶ傾向が読み取れます。

---

## 主要な技と採用率（M-3）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たきのぼり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">90.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず一致打点。命中100・ひるみ20%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>70.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A・S+1。全抜き性能の核</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>47.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず複合相手へのカバレッジ。命中85%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2ターン変化技封じ。ミミッキュのつるぎのまい（80.8%）・カバルドンのあくび（93.9%）を先に封じる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">被先制後は威力2倍（120）。ガブリアス（ドラゴン/じめん）に×4</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみくだく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後あく一致打点。Bダウン20%の追加効果</td>
</tr>
</tbody>
</table>
</div>

---

## 型別解説

### 型1：B振り安定型（最多採用）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">B振りりゅうのまい型（ようき）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（98.5%）※メガ後かたやぶり<br>
<strong>性格:</strong> ようき（S↑ C↓）<br>
<strong>EV:</strong> A2 B32 S32<br>
<strong>持ち物:</strong> ギャラドスナイト（56.5%）
</div>
<div>
<strong>技構成:</strong><br>
・たきのぼり<br>
・りゅうのまい<br>
・パワーウィップ<br>
・ちょうはつ / ゆきなだれ
</div>
</div>
</div>

**この型の強み（A32 B0型との比較）:**

B32振りのメガ後B実数値は161。EV全振りとのAとの差はEV2の分（A177）しかなく、積み後の火力はある程度抑えながら物理技を複数受けられる耐久を確保します。ようきS32でS実数値146となり、りゅうのまいを積めばS219相当（1積み）に到達します。

**この型の弱み:**

A2振りのためA実数値177にとどまり、いじっぱりA32型（A実数値227）と比べると50の差があります。りゅうのまい1積み後でもA265に対し相手がA340相当の技を持つ場合に確定数が変わる対象があります。

---

### 型2：A重視型（いじっぱり）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="メガギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">火力重視型（いじっぱり）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（98.5%）※メガ後かたやぶり<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）採用率39.6%<br>
<strong>EV:</strong> A32 S32 など<br>
<strong>持ち物:</strong> ギャラドスナイト / たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・たきのぼり<br>
・りゅうのまい<br>
・パワーウィップ<br>
・ちょうはつ / ゆきなだれ / かみくだく
</div>
</div>
</div>

**この型の強み（ようき型との比較）:**

いじっぱりA32のメガ後A実数値は227（ようきA2の177に対し+50）。りゅうのまい1積み後はA340に達し、ようき型（A265）より75高い火力になります。1積みで確定圏内に入れる相手の範囲が広がります。

**この型の弱み:**

いじっぱりS32のS実数値は133で、ようきS32の146より13低くなります。りゅうのまいを積む前に後れを取る相手が増えるため、積みターンの確保が難しくなります。

---

### 非メガ型（たべのこし・オボンのみ）

M-3ではたべのこし23.2%・オボンのみ10.0%で合計33.2%が非メガ採用です。非メガ時は特性いかくのまま（みず/ひこう）で動き続け、じめん無効・でんき×4という耐性・弱点のままです。わんぱく（14.1%）EV B重視のB振り耐久構成が多く（A1-B32-C1-S32が次点18.6%）、りゅうのまいで積み勝つというよりいかくと耐久でサイクルに参加する運用です。

---

## データ分析②：ゆきなだれがこおりのキバを代替した理由

M-2では**こおりのキバ45.5%・ゆきなだれ19.9%**だったところが、M-3では**こおりのキバ圏外・ゆきなだれ21.3%**に変化しています。

どちらもこおりタイプの技でガブリアス（ドラゴン/じめん）に×4で通りますが、用途が異なります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先制可能（S優位時）。ひるみ10%・こおり10%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60（被攻撃後120）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">そのターンに攻撃を受けると威力が2倍になる</td>
</tr>
</tbody>
</table>
</div>

こおりのキバはS優位を前提とした選択です。しかしギャラドスのS実数値146（ようきS32）はメガライチュウX（S178）・メガライチュウY（S200）いずれにも遅れを取ります。またガブリアス（S実数値169・ようき最速）にもりゅうのまいなしでは後れを取るため、「こおりのキバで先制して処理する」という運用が成立しにくい環境になっています。一方ゆきなだれは被攻撃後に威力120で打てるため、相手から攻撃を受けてから反撃する場面で実質的なBP120として機能します。M-3でB振りの最多EVが増えていることと合わせると、先手で仕留めるより受けてから反撃する型が増えた流れと一致しています。

---

## 環境ポケモンへの相性

### 有利に動けるポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼりが×2。カバルドンはあくび（93.9%）で流そうとするが、ちょうはつで封じてからりゅうのまいを積む動線が組みやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼりが半減、くさ技が×0.25なのでパワーウィップは通らないが、ゆきなだれ（こおり等倍）またはかみくだく（あく等倍）での削り役を担える。積み後なら突破可能</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモン

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後フェアリー×2弱点のじゃれつく（96.4%）が直撃する。ギャラドスの全攻撃技はミミッキュ（ゴースト/フェアリー）に等倍以下で、積んでも有効打に乏しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アローラキュウコン（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガ後フェアリー×2弱点のムーンフォース（49.6%）を持つ。あく技は半減で通るためかみくだくでの削りは可能だが、オーロラベール（98.0%）を張られると積み展開を許しやすい</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ライチュウ（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ライチュウナイト採用率96.2%でほぼメガ運用。メガライチュウX（S実数値178・おくびょうS32）・メガライチュウY（S200・おくびょうS32）ともにギャラドス（ようきS32・S実数値146）より速く、でんき×2弱点の技を先に打たれる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん採用率99.5%で、メガ後のじめん等倍をつかれる。ゆきなだれ（×4）で有効打は持てるが、ガブリアスS実数値169（ようき最速）はギャラドスS146より速く、積み前に先手を取られる。積んだ後ならゆきなだれ120倍打で処理圏に入る</td>
</tr>
</tbody>
</table>
</div>

---

## パートナー（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき対策のじめんタイプ。ギャラドスが苦手なでんきに対してじしんで圧をかける役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ばけのかわで場持ちしながら積み、通せない相手をギャラドスに引き継ぐ役割分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン">
    <div class="name">アロキュウ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">オーロラベール（98.0%）で物理・特殊ダメージを半減し、ギャラドスがりゅうのまいを積む場面を安全に作る</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0257-00.webp" alt="バシャーモ">
    <div class="name">バシャーモ</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">かくとう技でギャラドスが有効打を持てないはがね・フェアリーへの打点を補う</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ技でギャラドスと同じみず系への打点を持ち、選出の幅を広げる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロック（84.7%）で場を整え、物理受けの後に交代してギャラドスに繋ぐ</div>
  </div>
</div>

同居率3位のアローラキュウコンはギャラドスの苦手相手でもあります（フェアリー×2弱点のムーンフォース49.6%）。同じパーティに入る理由は、アローラキュウコンの**オーロラベール（採用率98.0%）**がギャラドスのりゅうのまいを積む場面を安全に作れるためです。オーロラベールが展開されている2ターンは物理・特殊問わず受けダメージが半減するため、フェアリー技を受ける際の被害も通常より軽減されます。アローラキュウコンとギャラドスは選出が分かれることが多く、相性の悪さよりオーロラベールのサポートとしての同居価値が上回っています。

---

## まとめ

M-3のギャラドスはM-2と技構成が大きく変化しており、じしん・こおりのキバによる広い技範囲を捨て、たきのぼり+パワーウィップの安定打点とB振りの耐久でサイクルに参加する形が増えています。

採用の判断基準:

- **ギャラドスナイト（56.5%）**：りゅうのまい積み型。いかく+B振りで物理を受けてからりゅうのまいを積む。積み後S219相当（1積み）でほぼ先手を取れる
- **たべのこし（23.2%）・オボンのみ（10.0%）**：非メガ耐久型。いかくのみず/ひこー複合で物理受けを続け、サイクル戦での消耗役
- **フェアリー対策**：メガ後の最大弱点。ミミッキュ・アローラキュウコンへはギャラドス単体では対応しにくく、バシャーモ・マスカーニャ等の選出と組み合わせる必要がある

---

## 関連考察記事

- [【ポケモンチャンピオンズ】メガギャラドス考察 M-2](/blog/gyarados-analysis-m2/)
- [【ポケモンチャンピオンズ】ガブリアス考察 M-3](/blog/garchomp-analysis-m3/)
- [【ポケモンチャンピオンズ】ミミッキュ考察 M-3](/blog/mimikyu-analysis-m3/)
