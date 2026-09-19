---
title: '【ポケモンチャンピオンズ】ガブリアス 考察 M-6 シーズン 使用率1位の解説'
description: 'M-6シーズン使用率1位のガブリアス考察。メガガブリアスZ（採用率35.0%）・こだわりスカーフ（22.9%）・きあいのタスキ（17.0%）の型別の強み弱みと、データで裏付けた苦手/得意なポケモンを解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-garchomp-m6.png'
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
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" />
  <div>
    <h2 style="margin:0 0 8px">ガブリアス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">1位</strong>　持ち物: <strong>ガブリアスナイトZ 35.0%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-09-10時点のものです。

M-6シーズン、ガブリアスは使用率1位につけています。ガブリアスには2種類のメガ進化先があり、C141・S151に特化して単一のドラゴンタイプへ変化する「メガガブリアスZ」（採用率35.0%）と、メガ進化せずこだわりスカーフ・きあいのタスキを持つA重視の物理型（合計39.9%）が並立しているのが最大の特徴です。M-6の環境データからは、通常のガブリアスナイト（A170/B115/C120/D95/S92、特性すなのちから）は採用率上位10持ち物に入らず、実質使われていません。

---

## ガブリアスの基本スペック

### 種族値（通常→メガガブリアスZ）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガZ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">108</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:48%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+61</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:76%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">102</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+49</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガガブリアスZはぼうぎょ-10と引き換えにとくこう+61・すばやさ+49と特殊アタッカー方向へ大きく変化します。こうげきは130のまま据え置きのため、メガZ後も物理技の威力自体は変わりません。参考までに、採用率がほぼゼロの通常のメガガブリアス（ガブリアスナイト）はA170/B115/C120/D95/S92と物理・耐久寄りの配分で、メガZとは逆方向の強化になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ（通常）：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき
  </td>
</tr>
</tbody>
</table>
</div>

<div class="type-row" style="margin-top:20px">
  <strong>タイプ（メガガブリアスZ）：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

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
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">（特性ふゆう）</span>
  </td>
</tr>
</tbody>
</table>
</div>

メガガブリアスZに進化すると、じめんタイプを失い純粋なドラゴンタイプになります。通常時はじめん技を等倍で受けますが、特性がふゆうに変わることで新たにじめん技が無効になります。こおり×4だった弱点が×2に軽減される一方、でんき無効だった耐性は×0.5に低下します。みず・くさの耐性を新たに獲得するのはメガZの利点です（ほのおは通常時から変わらず半減で、新規獲得ではありません）。

### 特性

**さめはだ（99.6%）**が通常時の特性です。接触技を受けると相手のHPを1/8削る効果で、初手の削り合いに寄与します。すながくれ採用は0.4%にとどまります。メガガブリアスZに進化すると特性は自動的に**ふゆう**へ置き換わり、じめん技を無効化します。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型の一致最大打点。はがねタイプに等倍以上で通る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">35.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">設置技。場に出た相手全体に弱点倍率に応じた固定割合ダメージ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">28.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZの一致最大打点。使用後とくこう2段階ダウン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理のドラゴン一致高火力打点。使用後はあばれ状態になる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプへのサブウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手を強制的に交代させる。ステルスロックとの併用でダメージを蓄積</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊のじめん打点。じめんタイプを失うメガガブリアスZでも、技自体は通常どおり使用できる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう・ほのおタイプへの打点。命中時に相手の素早さを1段階下げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2〜5回連続攻撃。使用後、自分のぼうぎょが1段階下がり、すばやさが1段階上がる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>パワージェム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊のひこう・ほのおタイプへの選択技</td>
</tr>
</tbody>
</table>
</div>

---

## 主な型

**性格採用率: おくびょう 19.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="メガガブリアスZ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガガブリアスZ型（採用率35.0%）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.6%、メガ進化後はふゆう）<br>
<strong>性格:</strong> おくびょう（19.5%）<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> ガブリアスナイトZ
</div>
<div>
<strong>技構成:</strong><br>
・りゅうせいぐん<br>
・かえんほうしゃ<br>
・だいちのちから<br>
・パワージェム
</div>
</div>
</div>

H185（EV2）・C193（EV32）・S223（EV32、おくびょう補正込み）まで伸ばした特殊寄りの高速アタッカーです。メガ進化前提のためA135（おくびょう補正でA↓）まで下がり物理技は活かしづらく、りゅうせいぐんの高い一致打点に加え、かえんほうしゃ（はがね）・だいちのちから（でんき・ほのお・どく等）・パワージェム（ひこう・ほのお）で幅広い相手にサブウェポンを撃ち分けられるのが強みです。りゅうせいぐんで一致ドラゴン打点はすでに確保できているため、物理技のげきりんを採用する意味はありません。

**強み:**

こおり×4だった弱点がメガ進化で×2に軽減されつつ、新たに半減耐性を獲得するのはみず・くさのみです（でんきは通常時の無効から半減へ、ほのおは通常時から変わらず半減で、いずれも新規獲得ではありません）。ふゆうでじめん技を無効化するため、じしんを主力に持つ相手の後続としても機能しやすい構成です。

**弱み:**

メガ進化でじめんタイプを失うため、通常時に持っていたいわ・どくタイプへの半減耐性を失い、ぼうぎょも-10されます。また、パーティ内の他のメガ進化候補とメガ進化枠を奪い合うため、ガブリアス以外にもメガ進化を活かしたいポケモンがいる場合は編成の自由度が下がります。

---

**性格採用率: いじっぱり 23.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型（採用率22.9%）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.6%）<br>
<strong>性格:</strong> いじっぱり（23.5%）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・げきりん<br>
・ドラゴンテール<br>
・ステルスロック
</div>
</div>
</div>

メガ進化せず、H185（EV2）・A200（EV32・いじっぱり補正込み）・S154（EV32）にこだわりスカーフの1.5倍でS231まで引き上げる型です。ドラゴン/じめんのタイプを維持したまま最速級の素早さを確保できます。なお性格採用率全体（型を問わず）ではようき（25.6%）がいじっぱり（23.5%）をわずかに上回っており、ようき採用の場合はS169・スカーフ込みでS253とさらに速く仕上がります（Aは低下）。

**強み:**

メガ進化枠を消費しないため、パーティ内の別のポケモンをメガ進化させながらガブリアスを高速アタッカーとして運用できます。じしん・げきりんの2種の一致技に加え、ステルスロックで設置役もこなせます。ドラゴン/じめんのタイプを維持するため、メガガブリアスZ型と異なりでんき技は無効のままです。

**弱み:**

技を1つに固定されるため、後続に読まれた場合は交代でかわされやすくなります。じめん技の効かないひこうタイプに対してはげきりん頼みになります。

---

**性格採用率: いじっぱり 23.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">きあいのタスキ型（採用率17.0%）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.6%）<br>
<strong>性格:</strong> いじっぱり（23.5%）<br>
<strong>EV:</strong> A32-B2-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・げきりん<br>
・ステルスロック<br>
・ドラゴンテール
</div>
</div>
</div>

こだわりスカーフ型と同じA200（EV32・いじっぱり補正込み）の物理打点を持ちつつ、S154のままアイテム補正を受けません。ステルスロックを設置してからドラゴンテールで後続を無理やり呼び込む、設置役としての運用が中心になります。

**強み:**

きあいのタスキにより、HPが満タンの状態なら一撃で倒される技を受けてもHP1で耐えます。技を固定されないため、こだわりスカーフ型と違い相手を見てから技を選べます。

**弱み:**

タスキは1度使うと消滅するため、どくのダメージやステルスロックなどの設置技によるダメージを先に受けているとHP満タンでなくなり機能しません。素早さがS154にとどまり、こだわりスカーフ型のS231には及びません。

---

## データ分析：M-5からの持ち物構成の変化

M-6でメガガブリアスZ（ガブリアスナイトZ）が登場したことで、ガブリアスの持ち物構成はM-5から大きく変わりました。

| 持ち物 | M-5採用率 | M-6採用率 |
| --- | --- | --- |
| きあいのタスキ | 41.4%（1位） | 17.0%（3位） |
| こだわりスカーフ | 19.5%（2位） | 22.9%（2位） |
| ガブリアスナイトZ | なし（未実装） | 35.0%（1位） |
| ガブリアスナイト（非Z） | 2.1% | 上位10位圏外 |

M-5にはガブリアスナイトZという選択肢自体が存在せず、当時のメガ進化枠は非Zのガブリアスナイト（2.1%採用にとどまる不人気型）が担っていました。M-6でメガガブリアスZが追加されたことで一気に採用率1位（35.0%）まで浮上し、M-5で1位だったきあいのタスキは41.4%から17.0%まで半減以下に落ち込んでいます。こだわりスカーフは19.5%から22.9%とほぼ横ばいで、タスキ型の一部がメガガブリアスZ型に流れた構図が見て取れます。

---

## 苦手なポケモン

使用率TOP30のうち、自分側・相手側とも多数派技（採用率20%以上）同士で撃ち合った場合に、ガブリアス側が一貫して負け越す相手は以下の3体です。

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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスの最大打点じしん（採用率67.6%）は確定2〜5発と型によって伸び悩む一方、アシレーヌの一致ムーンフォース（採用率99.1%）はガブリアスの弱点を突いて確定1〜2発で通ります。ガブリアスが先手を取れる対面でも、ムーンフォースの方が確定数で優位に立つため、どの型でも打ち合いに勝てません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスのじしん（採用率67.6%）はばけのかわで1発分が無効化される分、確定3〜4発かかる一方、ミミッキュの一致じゃれつく（採用率98.1%）は確定1〜2発で沈めてきます。先手を取っても打点で押し切れません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ・こだわりスカーフ型は素早さで先手を取れますが、りゅうせいぐん／スケイルショットとも確定2発止まりで、返しのカイリューの一致りゅうせいぐん（採用率50.8%）の確定1発で倒されます。きあいのタスキ型は確定2発同士の撃ち合いになりますが、優先度+2の先制技しんそく（採用率39.6%）を持つ個体には先に動かれてしまいます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

使用率TOP30を中心に、相手の型が変わっても一貫して有利になる相手は以下のとおりです。

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
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率28.6%）はメガボーマンダのりゅうせいぐん（採用率21.2%）より確定数で上回り、1発で沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型（こだわりスカーフ・きあいのタスキ）はげきりん（採用率27.3%）で確定3発。メガガブリアスZ型は特性ふゆうでカバルドンの一致じしん（採用率99.3%）が無効化されて一方的に勝ち、物理型にはじしんが等倍で確定3発通りますが、ガブリアス側が先手で確定3発を先に決めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（×4の弱点）は確定2発、ふうせん持ちにはりゅうせいぐん・げきりん（ドラゴンは等倍）に切り替えても確定2発で安定します。キラフロルの返し技（ヘドロウェーブ採用率56.0%・だいちのちから）は2〜4発とビルドにより差がありますが、ガブリアス側が先に沈めます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率28.6%）とメガリザードンXのげきりん（採用率21.6%）が互いに1発の撃ち合いになりますが、多くの型でガブリアス側が先手を取れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">がんせきふうじ（採用率21.1%）で2発、メガリザードンYのげきりん（採用率21.6%）も2発ですがガブリアス側が先手を取れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">がんせきふうじ（採用率21.1%）で3発、ウルガモスの一致むしのさざめき（採用率35.4%）も3発ですがガブリアス側が先手を取れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率28.6%）は等倍で2発、オオニューラの一致インファイト（採用率99.4%）も2発ですが、多くの型でガブリアス側が先手を取れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん・りゅうせいぐんで確定2発（シュカのみ持ちの個体にはげきりんで確定3発）。ラウドボーンの一致シャドーボール（採用率52.9%）は確定4発止まりで、ガブリアス側が先に沈めます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（採用率27.3%）で3発、ウォッシュロトムの一致ハイドロポンプ（採用率97.1%）も3発ですがガブリアス側が先手を取れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（採用率28.6%）で2発、イエッサンの一致マジカルシャイン（採用率70.2%）も2発ですが、多くの型でガブリアス側が先手を取れます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-6でガブリアスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**アシレーヌ**（1位）はみず/フェアリーで、ガブリアスの弱点であるこおり技を半減・ドラゴン技を無効にできます。

**ボーマンダ**（3位）はドラゴン/ひこうで、ガブリアスと同じドラゴンタイプを共有するため弱点の分散にはなりませんが、じしんが無効なひこう複合の相手にボーマンダのりゅうせいぐん（採用率21.2%）で打点を分担できます。

**ミミッキュ**（8位）はゴースト/フェアリーで、ばけのかわにより初手の1発を無効化できます。ガブリアスが不利になりやすいフェアリー複合の相手（アシレーヌ等）に対しては、ミミッキュの一致じゃれつくで打点を分担できる点が補完になります。

---

## まとめ

M-6のガブリアスは使用率1位を獲得し、メガガブリアスZ型（35.0%）とこだわりスカーフ・きあいのタスキの物理型（合計39.9%）という異なる方向性の型が併存するシーズンです。

- **メガガブリアスZ型（35.0%）**：ふゆうでじめん技を無効化しつつ、C193・S223の特殊高速アタッカーとして運用
- **こだわりスカーフ型（22.9%）**：S231まで伸ばしメガ進化枠を温存したまま最速級の運用が可能
- **きあいのタスキ型（17.0%）**：ステルスロックを絡めた設置役兼、確定耐えによる粘り強さが持ち味
- **通常のガブリアスナイト（非Z）は実質不採用**：M-6環境ではメガガブリアスZが唯一の実戦的なメガ進化先

物理型のじしんは環境上位30体中実質11体に弱点を突ける高いカバー範囲を持つ一方、フェアリー複合のアシレーヌ・ミミッキュには弱点を突かれ、じめん技が無効なひこう複合のボーマンダ・カイリューや特性ふゆうのウォッシュロトムにはドラゴン技での打点が必要になります。どの型を選ぶかは、パーティ内でメガ進化枠をガブリアスに割くか他のポケモンに割くかで判断が分かれます。
