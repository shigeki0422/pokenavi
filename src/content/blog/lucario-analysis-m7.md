---
title: '【ポケモンチャンピオンズ】ルカリオ 考察 M-7 シーズン 使用率7位 メガ進化2種の型解説'
description: 'M-7シーズン使用率7位のルカリオ考察。メガルカリオZ（ルカリオナイトZ採用率79.6%）のわるだくみ型・フルアタ型と、メガルカリオ（ルカリオナイト採用率19.4%）のつるぎのまい型を比較し、型別の強み弱みとカバルドン・ガブリアスなど苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-26'
heroImage: '../../assets/hero-lucario-m7.png'
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
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" />
  <div>
    <h2 style="margin:0 0 8px">ルカリオ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>　持ち物: <strong>ルカリオナイトZ 79.6%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズン、ルカリオは使用率7位につけています。メガ進化には**ルカリオナイト**と**ルカリオナイトZ**の2種類のメガストーンがあり、採用率ではルカリオナイトZ（79.6%）が主流です。

---

## ルカリオの基本スペック

<!-- gate:rows start id=base_stats facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
### 種族値（通常→メガルカリオZ／メガルカリオ）

<p style="margin:12px 0 0;font-size:0.85em;font-weight:600;color:#555">通常→メガルカリオZ</p>

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
      <div style="width:35%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:50%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:5%;background:#dc2626;height:12px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:57.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:24.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">115</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">164</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+49</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:45%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:30.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">151</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+61</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">525</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">625</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

<p style="margin:12px 0 0;font-size:0.85em;font-weight:600;color:#555">通常→メガルカリオ</p>

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
      <div style="width:35%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:55%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px"></div>
      <div style="width:17.5%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">145</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:9%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">88</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+18</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:57.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:12.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">115</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">140</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">70</span><span style="width:32px;text-align:right">70</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:45%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:11%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">112</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+22</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">525</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">625</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガルカリオはこうげき+35・ぼうぎょ+18と物理方向、メガルカリオZはとくこう+49・すばやさ+61と特殊方向に伸びる対照的な進化です。EV最多分布H2-C32-S32・おくびょう採用時、メガルカリオZのC実数値は216、S実数値は223になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

メガルカリオ・メガルカリオZもタイプは変わらず、弱点はかくとう・じめん・ほのおです。M-7使用率上位ではガブリアス（1位）・カバルドン（4位）のじしん（採用率それぞれ65.5%・97.3%）、リザードン（6位）のフレアドライブ・かえんほうしゃ（採用率30.5%・43.0%）が主な脅威です。ルカリオナイトZ個体（79.6%）のはどうのぼうごは接触技を半減するため、接触技のフレアドライブは半減できますが、接触技ではないかえんほうしゃはそのまま通ります。

### 特性

通常特性は**せいしんりょく（82.3%）**で、メガ進化前の間は相手の攻撃にひるまず、いかくも効きません。メガ進化後は、ルカリオナイトZ（79.6%）が**はどうのぼうご**（接触技で受けるダメージが半減する）、ルカリオナイト（19.4%）が**てきおうりょく**（自分と同じタイプの技の威力が1.5倍ではなく2倍になる）に替わります。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくのはどう</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で相手をひるませる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>わるだくみ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">59.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻を2段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はどうだん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">55.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手に必ず命中する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ラスターカノン</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんくうは</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">44.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>てっていこうせん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">140</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">32.0%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">攻撃した後自分の最大HPの1/2のダメージを受ける。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.4%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の防御と特防が1段階下がる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃を2段階上げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.6%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+1。優先度0の技より先に出せる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">コメットパンチ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">20%の確率で自分の攻撃を1段階上げる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に3つの型を紹介します。

### 型1：わるだくみ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">わるだくみ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（82.3%、メガ進化後：はどうのぼうご）<br>
<strong>性格:</strong> おくびょう（ひかえめも一定数）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> ルカリオナイトZ
</div>
<div>
<strong>技構成:</strong><br>
・はどうだん<br>
・ラスターカノン<br>
・あくのはどう<br>
・わるだくみ<br>
選択技：しんくうは・てっていこうせん
</div>
</div>
</div>

C216（EV32）のメガルカリオZが、わるだくみでとくこうを2段階上げてから、はどうだん・ラスターカノン・あくのはどうの3タイプで打点を撃ち分ける型です。わるだくみを1回通すとC216からC432まで伸びます。

<!-- gate:rows start id=card:1 facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
**他の型との違い:**

- 他の型に無い技：わるだくみ
- ラスターカノン：この型は必ず持ち、フルアタ型では選択技
<!-- gate:rows end id=card:1 -->

---

### 型2：フルアタ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（82.3%、メガ進化後：はどうのぼうご）<br>
<strong>性格:</strong> おくびょう（ひかえめも一定数）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> ルカリオナイトZ
</div>
<div>
<strong>技構成:</strong><br>
・はどうだん<br>
・しんくうは<br>
・てっていこうせん<br>
・あくのはどう<br>
選択技：ラスターカノン
</div>
</div>
</div>

積み技を持たず、はどうだん・しんくうは・てっていこうせん・あくのはどうの4つの攻撃技を最初から揃えるアタッカー運用です。

<!-- gate:rows start id=card:2 facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
**他の型との違い:**

- しんくうは：この型は必ず持ち、わるだくみ型では選択技
- てっていこうせん：この型は必ず持ち、わるだくみ型では選択技
<!-- gate:rows end id=card:2 -->

---

### 型3：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（82.3%、メガ進化後：てきおうりょく）<br>
<strong>性格:</strong> ようき（いじっぱりも同程度）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> ルカリオナイト
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・バレットパンチ<br>
・じしん<br>
・つるぎのまい<br>
選択技：コメットパンチ・しんそく
</div>
</div>
</div>

A197（EV32）のメガルカリオが、つるぎのまいでこうげきを2段階上げてから、インファイト・バレットパンチの一致技とじしんで押し切る物理型です。つるぎのまいを1回通すとA197からA394まで伸びます。

<!-- gate:rows start id=card:3 facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
**他の型との違い:**

- 他の型に無い技：インファイト・バレットパンチ・じしん・つるぎのまい
- 持ち物：ルカリオナイト
- 3つの型で最も高い実数値：こうげき197・ぼうぎょ108
- 3つの型で最も低い実数値：すばやさ180
<!-- gate:rows end id=card:3 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">わるだくみ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（のんき・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr class="note"><td colspan="4" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。採用率10%未満の技が決め手になる個体7件は除く。セグレイブ、イエッサン(オス)、キラフロル、ゴリランダーは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの技・持ち物採用率の変化


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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ラスターカノン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">73.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">51.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-22.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">わるだくみ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">77.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">59.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-18.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">はどうだん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">72.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-16.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">インファイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+11.8pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">てっていこうせん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+11.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">14.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.9pt</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ルカリオナイトZ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">90.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">79.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-10.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ルカリオナイト</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">8.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+10.7pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
- ラスターカノン：73.7%→51.3%（-22.4pt）。わるだくみ型が持ち、フルアタ型でも選択技のため、型の増減とは言えません。
- わるだくみ：77.9%→59.6%（-18.3pt）。わるだくみ型だけが持つため、この変化はその型の増減を示します。
- はどうだん：72.8%→55.9%（-16.9pt）。わるだくみ型・フルアタ型に共通のため、型の増減とは言えません。
- インファイト：5.6%→17.4%（+11.8pt）。記事の型ではつるぎのまい型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- おくびょう：66.8%→55.2%（-11.6pt）。わるだくみ型・フルアタ型が選んでいるため、型の増減とは言い切れません。
- てっていこうせん：20.9%→32.0%（+11.1pt）。フルアタ型が持ち、わるだくみ型でも選択技のため、型の増減とは言えません。
- ルカリオナイトZ：90.5%→79.6%（-10.9pt）。わるだくみ型・フルアタ型が持つため、型の増減とは言い切れません。
- ルカリオナイト：8.7%→19.4%（+10.7pt）。つるぎのまい型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
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
<!-- gate:rows start id=weak facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス<br><span style="font-size:0.8em;color:#64748b">メガガブリアスZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のインファイトは乱数1発（50%）。メガガブリアスZのかえんほうしゃ（採用率31.6%）は乱数1発（88%）で、S180対S223で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは乱数2発（89%）。カバルドンのじしん（採用率97.3%）は確定1発で、S223対S67で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ<br><span style="font-size:0.8em;color:#64748b">メガグソクムシャで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは確定2発。メガグソクムシャのインファイト（採用率32.0%）は乱数1発（88%）で、S223対S60で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX31.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじしんは確定1発。メガリザードンXのフレアドライブ（採用率30.5%）は確定1発で、S180対S167で先手を取りますが、確定数どおりには進まず、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のインファイトは確定2発。メガリザードンYのかえんほうしゃ（採用率43.0%）は確定1発で、S180対S167で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型の選択技てっていこうせんは確定2発。メガカイリューのかえんほうしゃ（採用率65.2%）は確定1発で、S223対S152で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のじしんは確定1発。メガライチュウYのきあいだま（採用率96.3%）は確定1発で、S180対S200で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型の選択技てっていこうせんは確定2発。オオニューラのインファイト（採用率98.4%）は確定2発で、S223対S344（上昇後）で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは乱数2発（92%）。ヒートロトムのオーバーヒート（採用率96.3%）は確定1発で、S223対S106で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは確定1発。サザンドラのかえんほうしゃ（採用率74.9%）は乱数1発（94%）で、S223対S225（スカーフ込み）で後手のため、先に倒されます。</td>
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
<!-- gate:rows start id=strong facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のバレットパンチは確定2発。ミミッキュのシャドークロー（採用率48.8%）は確定2発で、優先度+1のバレットパンチで先に動き、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは確定2発。ブリジュラスの10まんボルト（採用率63.9%）は確定3発で、S223対S105で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型の選択技てっていこうせんは確定2発。マスカーニャのトリックフラワー（採用率95.8%）は確定3発で、最後は優先度+1の選択技しんくうはで先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー<br><span style="font-size:0.8em;color:#64748b">メガゲンガーで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型の選択技てっていこうせんは確定1発。メガゲンガーのシャドーボール（採用率82.9%）は確定1発で、S223対S200で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい型のインファイトは確定1発。ブラッキーのイカサマ（採用率96.0%）は確定2発で、S180対S85で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のはどうだんは確定2発（相手のきあいのタスキ込み）。ゲッコウガのなみのり（採用率38.3%）は確定2発で、S223対S174で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">わるだくみ型のラスターカノンは確定1発。アローラキュウコンのムーンフォース（採用率50.7%）は確定2発で、S223対S177で先手を取り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でルカリオと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
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
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" loading="lazy">
    <div class="name">カイリュー</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イダイトウ(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カイリュー<br><span style="font-weight:normal;font-size:0.85em">同居率6位・メガカイリューで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ゴリランダー<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率8位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率10位・メガボーマンダで判定</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZの弱点：かくとう技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZの弱点：じめん技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZの弱点：ほのお技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">グソクムシャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX・メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ライチュウ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サザンドラ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝メガルカリオZの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ガブリアス＝じしん・かえんほうしゃ・りゅうせいぐん；カバルドン＝じしん；グソクムシャ＝ふいうち・きゅうけつ・アイアンヘッド・インファイト；メガリザードンX・メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；ライチュウ＝でんじほう・きあいだま・ねこだまし・ボルトチェンジ；オオニューラ＝インファイト・フェイタルクロー・ねこだまし・じごくづき；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト；サザンドラ＝あくのはどう・りゅうせいぐん・かえんほうしゃ・とんぼがえり</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=a8786b3f8076d6a3d4f3582319a292230289881b -->
**強み**

- 得意な相手は7体です。使用率上位では、ミミッキュ（3位）にバレットパンチ、ブリジュラス（8位）にはどうだん、マスカーニャ（17位）にてっていこうせんで勝てます。
- タイプ相性では、ノーマル・くさ・こおり・むし・いわ・ドラゴン・あく・はがねを半減以下、どくを無効で受けられます。

**弱み**

- 苦手な相手は10体です。使用率上位では、ガブリアス（1位）のかえんほうしゃ、カバルドン（4位）のじしん、グソクムシャ（5位）のインファイトで先に倒されます。
- 弱点はほのお・かくとう・じめんです。

**型の選び分け**

- 「わるだくみ型」：他の型に無い技はわるだくみ。
- 「フルアタ型」：しんくうはを必ず持つ（わるだくみ型では選択技）。
- 「つるぎのまい型」：他の型に無い技はインファイト・バレットパンチ・じしん・つるぎのまい。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は7位です（M-6: 5位）。
- 採用率の変化が大きいのはラスターカノン（-22.4pt）・わるだくみ（-18.3pt）・はどうだん（-16.9pt）です。
<!-- gate:rows end id=summary -->

*関連記事：[ガブリアス考察 M-7](/blog/garchomp-analysis-m7/)、[ルカリオ考察 M-6](/blog/lucario-analysis-m6/)*
