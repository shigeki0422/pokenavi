---
title: '【ポケモンチャンピオンズ】ギャラドス 考察 M-7 シーズン メガ運用主流化の型解説'
description: 'M-7シーズン使用率21位（M-6:18位）のギャラドスを考察。ギャラドスナイト採用率46.2%（M-6:22.0%→+24.2pt）でメガ運用が主流化したギャラドスの、みず/ひこうのタイプ相性、3つの型、苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-27'
heroImage: '../../assets/hero-gyarados-m7.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" />
  <div>
    <h2 style="margin:0 0 8px">ギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">21位</strong>（M-6: 18位）　持ち物: <strong>ギャラドスナイト 46.2%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのギャラドスは使用率21位です（M-6: 18位）。みず/ひこうの複合タイプに特性いかくを持つ物理アタッカーで、メガ進化するとみず/あく複合に変わります。技・持ち物・性格・EVの組み合わせから3つの型に分かれます。持ち物はギャラドスナイトが22.0%から46.2%（+24.2pt）に伸び、最も採用率の高い持ち物になっています。

---

## ギャラドスの基本スペック

<!-- gate:rows start id=base_stats facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
### 種族値（通常→メガギャラドス）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:32px;text-align:right">メガ後</span>
    <span style="width:40px;text-align:right">差分</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:47.5%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:32px;text-align:right">95</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:62.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:15%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">125</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">155</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:39.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:15%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">79</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">109</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:30%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">70</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px"></div>
      <div style="width:15%;background:linear-gradient(90deg,#34d399,#059669);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">81</span><span style="width:32px;text-align:right">81</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">540</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">640</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガ進化で種族値はA125→155・B79→109・C60→70・D100→130まで伸びますが、S81は変化しません。型1のメガりゅうのまい型は、りゅうのまいで自分のSを上げてこのすばやさを補います。

### タイプ・弱点

メガ進化前はみず/ひこう、メガ進化後はみず/あくとタイプが変わります。弱点構成が異なるため、それぞれ分けて示します。

<div class="type-row"><strong>タイプ（通常）：</strong><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:32px;height:32px"></div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:32px;height:32px"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:32px;height:32px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:32px;height:32px"><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-06-bug.png" alt="むし" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:32px;height:32px"></td>
</tr>
</tbody>
</table>
</div>

メガ進化前（ちょうはつ型・フルアタ型）はでんき×4が最大の弱点です。M-7上位ではブリジュラス（使用率8位）の10まんボルト（採用率63.9%）やライチュウ（使用率22位）のでんじほう（採用率96.5%）が脅威になります。じめんタイプの技を無効化できるため、使用率1位のガブリアスのじしん（採用率65.5%）は通りませんが、メガガブリアスZとの対戦は型によって判定が異なります（「型による有利不利の違い」の表を参照してください）。

<div class="type-row"><strong>タイプ（メガ後）：</strong><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-16-dark.png" alt="あく" style="width:32px;height:32px"></div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:32px;height:32px"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:32px;height:32px"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:32px;height:32px"><img src="/images/types/type-06-bug.png" alt="むし" style="width:32px;height:32px"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-16-dark.png" alt="あく" style="width:32px;height:32px"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:32px;height:32px"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:32px;height:32px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:32px;height:32px"><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:32px;height:32px"></td>
</tr>
</tbody>
</table>
</div>

メガ進化後はみず/あく複合になり、でんき弱点が×4→×2に軽減される代わりに、かくとう・くさ・むし・フェアリーが新たに弱点に加わります。

### 特性

<strong>いかく（98.7%、M-6: 99.3%→-0.6pt）</strong>が主流です。登場した時、相手の攻撃を1段階下げる特性です。メガ進化後の特性はかたやぶりに固定され、相手の特性に関係なく技を出せます。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">地中状態の相手には威力が2倍になる。グラスフィールド状態の時、威力が1/2になる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワーウィップ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">61.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">52.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃、素早さを1段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たきのぼり</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手をひるませる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">40.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。10％の確率で相手をひるませる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">39.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をちょうはつ状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ゆきなだれ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">37.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度-4。この技を使うターンに相手からの技ダメージを受けていれば、威力が2倍になる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やけっぱち</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">20.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">前のターン自分が動けなかったり技を外したり失敗していた場合、威力が2倍になる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">かみくだく</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.2%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手の防御を1段階下げる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に3つの型を紹介します。

### 型1：メガりゅうのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガりゅうのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（メガ後 かたやぶり）<br>
<strong>性格:</strong> ようき<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> ギャラドスナイト
</div>
<div>
<strong>技構成:</strong><br>
・たきのぼり<br>
・じしん<br>
・こおりのキバ<br>
・りゅうのまい<br>
選択技：パワーウィップ・ちょうはつ
</div>
</div>
</div>

ギャラドスナイトでメガ進化し、りゅうのまいで攻撃とすばやさを同時に上げてから攻め切る積み型です。

<!-- gate:rows start id=card:1 facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
**他の型との違い:**

- 他の型に無い技：りゅうのまい
- こおりのキバ：この型は必ず持ち、フルアタ型では選択技
- 持ち物：ギャラドスナイト
- 3つの型で最も高い実数値：こうげき207・とくぼう150・すばやさ146
- 3つの型で最も低い実数値：HP172・ぼうぎょ129
<!-- gate:rows end id=card:1 -->

---

### 型2：ちょうはつ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ちょうはつ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・パワーウィップ<br>
・ゆきなだれ<br>
・ちょうはつ<br>
選択技：たきのぼり・やけっぱち
</div>
</div>
</div>

H/Bに厚く振り、ゴツゴツメットを持ち、ちょうはつで相手の積み技や回復技を止めながら攻める型です。

<!-- gate:rows start id=card:2 facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
**他の型との違い:**

- ちょうはつ：この型は必ず持ち、メガりゅうのまい型では選択技
<!-- gate:rows end id=card:2 -->

---

### 型3：フルアタ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット
</div>
<div>
<strong>技構成:</strong><br>
・たきのぼり<br>
・じしん<br>
・パワーウィップ<br>
・ゆきなだれ<br>
選択技：やけっぱち・こおりのキバ
</div>
</div>
</div>

ゴツゴツメットで受けに回りながら、状態変化技を採用せず4つの攻撃技だけで攻める型です。

<!-- gate:rows start id=card:3 facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
**他の型との違い:**

- ちょうはつ型との技の違い：この型はたきのぼり、ちょうはつ型はちょうはつ
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガりゅうのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ちょうはつ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガガブリアスZ（おくびょう・ガブリアスナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（いじっぱり・いのちのたま）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX（ようき・リザードナイトX）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・ふうせん）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガカイリュー（ひかえめ・カイリュナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロス（いじっぱり・メタグロスナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（ようき・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガキラフロル（おくびょう・キラフロルナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。セグレイブは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6→M-7でメガ運用が主流に

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">りゅうのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">52.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+21.7pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">45.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">66.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+20.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゆきなだれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">56.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">37.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-19.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">やけっぱち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-18.2pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こおりのキバ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+13.6pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ちょうはつ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">52.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">39.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-12.8pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">パワーウィップ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">67.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">61.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-5.8pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たきのぼり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">56.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">51.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-5.6pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ギャラドスナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">22.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">46.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+24.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゴツゴツメット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">53.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-23.2pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たべのこし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">9.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-4.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">たつじんのおび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+1.6pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
- ギャラドスナイト：22.0%→46.2%（+24.2pt）。メガりゅうのまい型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- ゴツゴツメット：53.9%→30.7%（-23.2pt）。ちょうはつ型・フルアタ型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- りゅうのまい：31.0%→52.7%（+21.7pt）。記事の型ではメガりゅうのまい型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- じしん：45.7%→66.6%（+20.9pt）。記事のすべての型に共通のため、型の増減とは言えません。
- ゆきなだれ：56.2%→37.1%（-19.1pt）。ちょうはつ型・フルアタ型と、記事に載せていない型に共通のため、型の増減とは言えません。
- やけっぱち：38.4%→20.2%（-18.2pt）。ちょうはつ型・フルアタ型の一部の個体が採用しているもので、型の増減とは言えません。
- わんぱく：43.8%→29.6%（-14.2pt）。ちょうはつ型・フルアタ型が選んでいるほか、記事に載せていない型の個体も選んでいるため、型の増減とは言い切れません。
- こおりのキバ：26.6%→40.2%（+13.6pt）。メガりゅうのまい型が持ち、フルアタ型でも選択技のため、型の増減とは言えません。
<!-- gate:rows end id=diff_movers -->

---

## 苦手なポケモン

使用率上位のうち、相手の型が変わっても一貫して不利になる相手のみを掲載します。

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
<!-- gate:rows start id=weak facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ちょうはつ型の選択技たきのぼりは確定3発。メガリザードンYのソーラービーム（採用率65.9%）は確定3発で、S101対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のこおりのキバは確定2発。ゴリランダーのウッドハンマー（採用率12.9%・少数派）は確定2発で、最後はグラスフィールドで優先度+1のグラススライダーで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のじしんは確定1発。メガライチュウYのでんじほう（採用率96.5%）は確定1発で、S146対S200で後手のため、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=weak -->
</tbody>
</table>
</div>

---

## 得意なポケモン

同じ基準で掲載します。

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
<!-- gate:rows start id=strong facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型の選択技パワーウィップは確定2発。アシレーヌのムーンフォース（採用率98.3%）は確定2発で、S146対S80で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のたきのぼりは乱数2発（71%）。カバルドンのじしん（採用率97.3%）は確定3発で、S146対S67で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のじしんは確定1発。メガルカリオZのはどうだん（採用率55.9%）は確定2発で、S146対S223で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型の選択技パワーウィップは確定1発。イダイトウ(オス)のウェーブタックル（採用率89.5%）は確定5発で、S146対S214（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のこおりのキバは確定2発。メガボーマンダのすてみタックル（採用率73.5%）は確定3発で、S146対S172で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のじしんは確定2発。ゲッコウガのヘドロウェーブ（採用率73.3%）は確定3発で、S146対S174で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガりゅうのまい型のこおりのキバは確定2発。サザンドラのりゅうせいぐん（採用率89.3%）は確定3発で、S146対S225（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でギャラドスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" loading="lazy">
    <div class="name">キラフロル</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率2位・メガルカリオZで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">キラフロル<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドスの弱点：いわ技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドスの弱点：でんき技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ライチュウ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ギャラドスの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；ゴリランダー＝グラススライダー・ドラムアタック・とんぼがえり・10まんばりき・はたきおとす；ライチュウ＝でんじほう・きあいだま・ねこだまし・ボルトチェンジ</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=07b774fc6181aa344bb8fe4ca5b905be005d3752 -->
**強み**

- 得意な相手は7体です。使用率上位では、アシレーヌ（2位）にパワーウィップ、カバルドン（4位）にたきのぼり、ルカリオ（7位）にじしんで勝てます。
- タイプ相性では、ギャラドスはほのお・みず・かくとう・むし・はがねを半減以下、じめんを無効で受けられます。
- タイプ相性では、メガギャラドスはほのお・みず・こおり・ゴースト・あく・はがねを半減以下、エスパーを無効で受けられます。

**弱み**

- 苦手な相手は3体です。使用率上位では、メガリザードンY（6位）のソーラービーム、ゴリランダー（19位）のウッドハンマー、ライチュウ（22位）のでんじほうで先に倒されます。
- ギャラドスの弱点はでんき（×4）・いわです。
- メガギャラドスの弱点はでんき・くさ・かくとう・むし・フェアリーです。

**型の選び分け**

- 「メガりゅうのまい型」：他の型に無い技はりゅうのまい。
- 「ちょうはつ型」：ちょうはつを必ず持つ（メガりゅうのまい型では選択技）。
- 「フルアタ型」：ちょうはつ型のちょうはつの代わりにたきのぼりを持つ。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は21位です（M-6: 18位）。
- 採用率の変化が大きいのはギャラドスナイト（+24.2pt）・ゴツゴツメット（-23.2pt）・りゅうのまい（+21.7pt）です。
<!-- gate:rows end id=summary -->

## 関連記事

- [ガブリアス考察記事一覧はこちら](/blog/garchomp-analysis-m7/)
- [アシレーヌ考察記事一覧はこちら](/blog/primarina-analysis-m7/)
- [カバルドン考察記事一覧はこちら](/blog/hippowdon-analysis-m7/)
