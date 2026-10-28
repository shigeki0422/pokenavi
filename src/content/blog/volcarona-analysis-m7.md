---
title: '【ポケモンチャンピオンズ】ウルガモス 考察 M-7 シーズン 使用率36位の3型解説'
description: 'M-7シーズン使用率36位（M-6: 29位）のウルガモスを考察。ちょうのまい採用率96.7%を軸に、ずぶとい耐久型・ひかえめ速攻型・おにび型の3型を比較し、ガブリアスなど苦手なポケモン、カバルドンなど得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-27'
heroImage: '../../assets/hero-volcarona-m7.png'
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
  <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" />
  <div>
    <h2 style="margin:0 0 8px">ウルガモス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">36位</strong>（M-6: 29位）　技: <strong>ちょうのまい 96.7%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのウルガモスは使用率36位（M-6: 29位）です。ちょうのまい（採用率96.7%）でとくこう・とくぼう・すばやさを同時に上げる積みアタッカー運用が中心です。ほのおのまい（82.7%）・ギガドレイン（78.8%）の2種を主力技に、あさのひざし・むしのさざめき・おにびなどの選択技を組み合わせます。技・持ち物・性格・EVの組み合わせから3つの型に分かれます。

---

## ウルガモスの基本スペック

<!-- gate:rows start id=base_stats facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:32.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">135</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">105</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">550</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

とくこう135を軸に、とくぼう105と素のすばやさ100を備えた特殊アタッカー型の配分です。HP85・ぼうぎょ65と物理耐久は低く、とくぼうはちょうのまいでさらに上がるため特殊アタッカー相手には積みやすい一方、物理耐久の低さは型（ずぶとい性格・オボンのみ）で補います。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">いわ</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">ひこう</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">みず</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:26px;height:26px;vertical-align:middle;margin-right:3px">くさ</span>
  </td>
</tr>
</tbody>
</table>
</div>

最大の弱点はいわ×4です。

### 特性

特性は<strong>ほのおのからだ</strong>（採用率89.7%）が主流で、接触技を受けると30%の確率で相手をやけど状態にします。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻、特防、素早さを1段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほのおのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">50%の確率で自分の特攻が1段階上がる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ギガドレイン</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">78.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手に与えたダメージの1/2自分のHPを回復する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あさのひざし</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2回復する。にほんばれ状態の場合は2/3回復する。それ以外の天気の場合は1/4回復する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>むしのさざめき</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">36.0%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">おにび</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.1%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をやけど状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">サイコキネシス</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.0%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.0%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の特攻を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をやけど状態にする。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に3つの型を紹介します。

### 型1：ずぶとい耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ずぶとい耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ほのおのからだ<br>
<strong>性格:</strong> ずぶとい<br>
<strong>EV:</strong> H32-B32-S2<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ちょうのまい<br>
・ほのおのまい<br>
・ギガドレイン<br>
選択技：むしのさざめき
・あさのひざし
</div>
</div>
</div>

ぼうぎょに厚く振った耐久積み型です。

<!-- gate:rows start id=card:1 facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
**他の型との違い:**

- おにび型との技の違い：この型はギガドレイン、おにび型はおにび
<!-- gate:rows end id=card:1 -->

---

### 型2：ひかえめ速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ひかえめ速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ほのおのからだ<br>
<strong>性格:</strong> ひかえめ<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・ちょうのまい<br>
・ほのおのまい<br>
・むしのさざめき<br>
選択技：サイコキネシス
・ギガドレイン<br>
選択技：あさのひざし
</div>
</div>
</div>

とくこう・すばやさに全振りし、きあいのタスキで一度だけ耐えてから積みに入る型です。

<!-- gate:rows start id=card:2 facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
**他の型との違い:**

- むしのさざめき：この型は必ず持ち、ずぶとい耐久型では選択技
- 持ち物：きあいのタスキ（HPが満タンの時、一撃でひんしになる技のダメージを受けてもHPを1残して耐える。1度使うと無くなる）
- 3つの型で最も高い実数値：とくこう205・すばやさ152
- 3つの型で最も低い実数値：HP162・ぼうぎょ85
<!-- gate:rows end id=card:2 -->

---

### 型3：おにび型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">おにび型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ほのおのからだ<br>
<strong>性格:</strong> ずぶとい<br>
<strong>EV:</strong> H32-B32-S2<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・ちょうのまい<br>
・ほのおのまい<br>
・おにび<br>
・あさのひざし<br>
選択技：ギガドレイン・サイコキネシス・マジカルフレイム
</div>
</div>
</div>

おにびで相手をやけど状態にし、物理アタッカーの攻撃を弱めながら積みに入る型です。

<!-- gate:rows start id=card:3 facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
**他の型との違い:**

- 他の型に無い技：おにび
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ずぶとい耐久型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ひかえめ速攻型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">おにび型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（いじっぱり・いのちのたま・H2-A32-S32）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（いじっぱり・いのちのたま・H16-A30-B6-S14）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY（ひかえめ・リザードナイトY）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガセグレイブ（いじっぱり・セグレイブナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロス（いじっぱり・メタグロスナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・グランドコート）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ（ようき・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガキラフロル（おくびょう・キラフロルナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの技・持ち物・性格採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技・持ち物・性格</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+6.3pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">むしのしらせ（特性）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+5.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ほのおのからだ（特性）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">95.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">89.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-5.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">むしのさざめき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">36.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+5.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ずぶとい（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">44.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">39.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-5.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">あさのひざし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">58.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.8pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ひかえめ（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">31.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">35.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+3.8pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ラムのみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">13.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">10.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.5pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
- きあいのタスキ：5.6%→11.9%（+6.3pt）。ひかえめ速攻型だけが持つため、この変化はその型の増減を示します。
- むしのしらせ：4.8%→10.3%（+5.5pt）。この記事の型の特性には含まれません。
- ほのおのからだ：95.2%→89.7%（-5.5pt）。記事のすべての型が持つため、型の増減とは言えません。
- むしのさざめき：30.7%→36.0%（+5.3pt）。ひかえめ速攻型が持ち、ずぶとい耐久型でも選択技のため、型の増減とは言えません。
- ずぶとい：44.8%→39.7%（-5.1pt）。ずぶとい耐久型・おにび型が選んでいるため、型の増減とは言い切れません。
- あさのひざし：58.9%→55.1%（-3.8pt）。記事のすべての型に共通のため、型の増減とは言えません。
- ひかえめ：31.9%→35.7%（+3.8pt）。ひかえめ速攻型が選んでいるほか、ずぶとい耐久型の一部の個体も選んでいるため、型の増減とは言い切れません。
- ラムのみ：13.5%→10.0%（-3.5pt）。ひかえめ速攻型の一部の個体が持つもので、型の増減とは言えません。
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
<!-- gate:rows start id=weak facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のむしのさざめきは確定2発。ガブリアスのじしん（採用率65.5%）は確定2発で、S152対S253（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のギガドレインは確定3発。アシレーヌのうたかたのアリア（採用率75.5%）は確定3発で、最後は優先度+1のアクアジェットで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おにび型の選択技サイコキネシスは乱数2発（>99%）。メガリザードンXのフレアドライブ（採用率30.5%）は確定2発で、S122対S167で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おにび型の選択技サイコキネシスは確定5発。メガカイリューのりゅうせいぐん（採用率35.5%）は乱数4発（97%）（ウルガモスのオボンのみ込み）で、最後は優先度+2のしんそくで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型の選択技サイコキネシスは確定3発。メガボーマンダのじしん（採用率72.0%）は確定2発で、S228（上昇後）対S172で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい耐久型の選択技むしのさざめきは確定3発。メガライチュウYのでんじほう（採用率96.5%）は乱数3発（88%）で、S122対S200で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のギガドレインは確定2発。カバルドンのじしん（採用率97.3%）は確定2発で、S152対S67で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ<br><span style="font-size:0.8em;color:#64748b">メガグソクムシャで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のほのおのまいは確定1発。メガグソクムシャのふいうち（採用率80.3%）は確定2発で、S152対S60で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のほのおのまいは確定1発。メガルカリオZのあくのはどう（採用率73.5%）は乱数3発（96%）で、S152対S223で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おにび型のほのおのまいは乱数4発（>99%）（相手のオボンのみ込み）。ブリジュラスの10まんボルト（採用率63.9%）は確定9発で、S122対S105で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい耐久型のほのおのまいは確定2発。サーフゴーのシャドーボール（採用率97.1%）は乱数4発（85%）で、S122対S114で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい耐久型のほのおのまいは確定2発。アーマーガアのブレイブバード（採用率27.5%）は乱数2発（91%）で、S122対S78で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のむしのさざめきは確定1発。ゴリランダーの10まんばりき（採用率55.1%）は乱数2発（86%）で、S152対S107で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型の選択技サイコキネシスは確定4発（相手のオボンのみ込み）。ヒートロトムの10まんボルト（採用率30.6%）は乱数5発（88%）で、S152対S106で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい耐久型のギガドレインは確定4発（相手のオボンのみ込み）。ウォッシュロトムのハイドロポンプ（採用率97.9%）は確定4発で、S122対S106で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ速攻型のほのおのまいは確定1発。アローラキュウコンのふぶき（採用率66.9%）は確定5発で、S152対S177で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でウルガモスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" loading="lazy">
    <div class="name">ギャラドス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率2位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率6位・メガボーマンダで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イダイトウ(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メタグロス<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガメタグロスで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率9位・メガルカリオZで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ギャラドス<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ウルガモスの弱点：いわ技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ウルガモスの弱点：ひこう技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ウルガモスの弱点：みず技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ボーマンダ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ライチュウ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ウルガモスの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ガブリアス＝じしん・かえんほうしゃ・りゅうせいぐん；アシレーヌ＝ムーンフォース・うたかたのアリア・アクアジェット；メガリザードンX＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；ボーマンダ＝すてみタックル・じしん；ライチュウ＝でんじほう・きあいだま・ねこだまし・ボルトチェンジ</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=d3e94ab338522d01f33ade1d58ea89f9de030488 -->
**強み**

- 得意な相手は10体です。使用率上位では、カバルドン（4位）にギガドレイン、グソクムシャ（5位）・ルカリオ（7位）にほのおのまいで勝てます。
- タイプ相性では、くさ・こおり・かくとう・むし・はがね・フェアリーを半減以下で受けられます。

**弱み**

- 苦手な相手は6体です。使用率上位では、ガブリアス（1位）のじしん、アシレーヌ（2位）のうたかたのアリア、メガリザードンX（6位）のフレアドライブで先に倒されます。
- 弱点はいわ（×4）・みず・ひこうです。

**型の選び分け**

- 「ずぶとい耐久型」：おにび型のおにびの代わりにギガドレインを持つ。
- 「ひかえめ速攻型」：むしのさざめきを必ず持つ（ずぶとい耐久型では選択技）。
- 「おにび型」：他の型に無い技はおにび。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は36位です（M-6: 29位）。
- 採用率の変化が大きいのはきあいのタスキ（+6.3pt）・むしのさざめき（+5.3pt）・あさのひざし（-3.8pt）です。
<!-- gate:rows end id=summary -->

---

*関連記事：[ガブリアス考察 M-7](/blog/garchomp-analysis-m7/)*
