---
title: '【ポケモンチャンピオンズ】ガブリアス 考察 M-7 シーズン 使用率1位の型解説'
description: 'M-7シーズン使用率1位のガブリアス考察。メガガブリアスZ（持ち物採用率34.4%）・こだわりスカーフ（持ち物採用率23.8%）型・ステルスロック型・つるぎのまい型・まきびし型の5型を比較し、型別の強み弱みとアシレーヌ・ミミッキュなど苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-25'
updatedDate: '2026-10-14'
heroImage: '../../assets/hero-garchomp-m7.png'
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
      使用率: <strong style="color:#e67e22">1位</strong>　持ち物: <strong>ガブリアスナイトZ 34.4%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-11時点のものです。

M-7シーズン、ガブリアスはM-6シーズン最終に続き使用率1位を維持しました。とくこう種族値141・すばやさ種族値151まで上昇し単一のドラゴンタイプへ変化する「メガガブリアスZ」（持ち物採用率34.4%）と、メガ進化せずこだわりスカーフ（23.8%）・きあいのタスキ（17.8%）を中心にじしんを主力とする物理型が並立しているのが特徴です。

---

## ガブリアスの基本スペック

<!-- gate:rows start id=base_stats facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
### 種族値（通常→メガガブリアスZ）

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
      <div style="width:54%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">108</span><span style="width:32px;text-align:right">108</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span><span style="width:32px;text-align:right">130</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px"></div>
      <div style="width:5%;background:#dc2626;height:12px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:32px;text-align:right">85</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:40%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px"></div>
      <div style="width:30.5%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">141</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+61</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span><span style="width:32px;text-align:right">85</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px;overflow:hidden;display:flex">
      <div style="width:51%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px"></div>
      <div style="width:24.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;opacity:0.35"></div>
    </div>
    <span style="width:32px;text-align:right">102</span><span style="width:32px;text-align:right"><strong style="color:#dc2626">151</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+49</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

メガガブリアスZはぼうぎょ-10と引き換えにとくこう+61・すばやさ+49と特殊アタッカー方向へ大きく変化します。

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

メガガブリアスZに進化すると特性がふゆうに変わり、通常時は等倍で受けていたじめん技が無効になります。こおり×4だった弱点は×2に軽減される一方、でんき無効だった耐性は×0.5に低下します。じめんタイプを失うことで、いわ・どくへの耐性（ともに×0.5）も失います。みず・くさの耐性を新たに獲得するのはメガガブリアスZの利点です。

### 特性

**さめはだ（99.3%）**が通常時の特性です。接触技を受けると相手のHPを1/8削る効果です。メガガブリアスZに進化すると特性は**ふゆう**へ置き換わります（じめん技無効への影響は上記「タイプ・弱点」参照）。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">68.1%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">地中状態の相手には威力が2倍になる。グラスフィールド状態の時、威力が1/2になる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の場をステルスロック状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">30.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をやけど状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">28.0%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分はあばれ状態になる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の特攻を2段階下げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>がんせきふうじ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">25.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の素早さを1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドラゴンテール</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">23.3%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度-6。相手に控えがいる場合、相手をランダムに交代させる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">20.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手の特防を1段階下げる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">スケイルショット</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.5%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">2〜5回連続で攻撃する。自分の防御を1段階下げ、素早さを1段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.4%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">通常の攻撃技。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・性格・EVの組み合わせから、採用割合が高い順に5つの型を紹介します。

### 型1：メガガブリアスZ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="メガガブリアスZ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガガブリアスZ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%、メガ進化後はふゆう）<br>
<strong>性格:</strong> おくびょう<br>
<strong>EV:</strong> H2-C32-S32<br>
<strong>持ち物:</strong> ガブリアスナイトZ
</div>
<div>
<strong>技構成:</strong><br>
・りゅうせいぐん<br>
・かえんほうしゃ<br>
・だいちのちから<br>
・ステルスロック<br>
選択技：パワージェム
</div>
</div>
</div>

H185（EV2）は通常時から変わらず、メガ進化後はC193（EV32）・S223（EV32、おくびょう補正込み）まで伸びる特殊寄りのアタッカーです。多くの個体がステルスロックも採用しており、自力で設置役を兼ねられます。

<!-- gate:rows start id=card:1 facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**他の型との違い:**

- 他の型に無い技：りゅうせいぐん・かえんほうしゃ・だいちのちから
- 持ち物：ガブリアスナイトZ
- 5つの型で最も高い実数値：とくこう193
- 5つの型で最も低い実数値：ぼうぎょ105
<!-- gate:rows end id=card:1 -->

---

### 型2：こだわりスカーフ型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こだわりスカーフ型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> ようき（いじっぱりも同程度）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> こだわりスカーフ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・げきりん<br>
・がんせきふうじ<br>
・ステルスロック<br>
選択技：どくづき・いわなだれ
</div>
</div>
</div>

こだわりスカーフ型は、H185（EV2）・A182（EV32）を確保し、ようき個体はこだわりスカーフの1.5倍でS169からS253まですばやさを引き上げます。4つ目の技はステルスロックが主流で、どくづき・いわなだれが選択候補として並びます。

<!-- gate:rows start id=card:2 facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**他の型との違い:**

- げきりん：この型は必ず持ち、つるぎのまい型では選択技
- 持ち物：こだわりスカーフ（素早さが1.5倍になるが、同じ技しか出せなくなる）
- 5つの型で最も高い実数値：すばやさ253（こだわりスカーフ込み）
<!-- gate:rows end id=card:2 -->

---

### 型3：ステルスロック型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ステルスロック型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> ようき／いじっぱり（A・S振り）、わんぱく／しんちょう（H/B振り）<br>
<strong>EV:</strong> A・S振り：H2-A32-S32／H/B振り：H32-B32-D2<br>
<strong>持ち物:</strong> A・S振り：きあいのタスキ／ゴツゴツメット／オボンのみ、H/B振り：ゴツゴツメット／オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ステルスロック<br>
・ドラゴンテール<br>
・がんせきふうじ<br>
選択技：スケイルショット
</div>
</div>
</div>

ステルスロック型は、A・S振りの物理個体（ようきA182・S169、いじっぱりA200・S154）と、H/B振りの耐久個体（わんぱくH215・B161・A150・S122）に分かれます。じしん・ステルスロック・ドラゴンテールの3技は共通し、4つ目の技はがんせきふうじが主流です。

<!-- gate:rows start id=card:3 facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**他の型との違い:**

- こだわりスカーフ型との技の違い：この型はドラゴンテール、こだわりスカーフ型はげきりん
<!-- gate:rows end id=card:3 -->

---

### 型4：つるぎのまい型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> いじっぱり（ようきも一定数）<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・スケイルショット<br>
・つるぎのまい<br>
・ほのおのキバ<br>
選択技：げきりん・いわなだれ・ステルスロック
</div>
</div>
</div>

A200（EV32・いじっぱり補正込み）の物理打点をつるぎのまいでさらに引き上げる積み型です。4つ目の技は、じしんが通らない相手への打点をほのおのキバで補うか、げきりん・いわなだれ・ステルスロックを選ぶかに分かれます。

<!-- gate:rows start id=card:4 facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**他の型との違い:**

- 他の型に無い技：つるぎのまい・ほのおのキバ
- スケイルショット：この型は必ず持ち、ステルスロック型では選択技
- 5つの型で最も高い実数値：こうげき200
<!-- gate:rows end id=card:4 -->

---

### 型5：まきびし型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">まきびし型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> さめはだ（99.3%）<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-B30-S4<br>
<strong>持ち物:</strong> オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・ドラゴンテール<br>
・ステルスロック<br>
・まきびし
</div>
</div>
</div>

H215（EV32）・B159（EV30、わんぱく補正込み）までHP・ぼうぎょを伸ばした耐久型です。H/B振りのステルスロック型に近い耐久振りですが、技構成にまきびしを加える点が異なります。

<!-- gate:rows start id=card:5 facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**他の型との違い:**

- 他の型に無い技：まきびし
- 持ち物：オボンのみ（HPが最大HPの1/2以下になった時、最大HPの1/4回復する。1度使うと無くなる）
- 5つの型で最も高い実数値：HP215・ぼうぎょ159
- 5つの型で最も低い実数値：すばやさ126
<!-- gate:rows end id=card:5 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メガガブリアスZ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">こだわりスカーフ型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ステルスロック型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">まきびし型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（おだやか・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン（しんちょう・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンX（ようき・リザードナイトX）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（いじっぱり・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（むじゃき・ボーマンダナイト ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">セグレイブ（いじっぱり・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガセグレイブ（いじっぱり・セグレイブナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガメタグロス（いじっぱり・メタグロスナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)（おくびょう・グランドコート）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr class="note"><td colspan="6" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体11件は除く</td></tr>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ステルスロック</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">39.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+7.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">がんせきふうじ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">25.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+5.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">げきりん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+3.1pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+2.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">だいちのちから</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">25.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-4.4pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ドラゴンテール</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.6pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">りゅうせいぐん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">27.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.4pt</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">23.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+5.9pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+1.7pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ガブリアスナイトZ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">35.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">34.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-1.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ゴツゴツメット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">11.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-5.4pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
- ステルスロック：39.7%→47.6%（+7.9pt）。記事のすべての型に共通のため、型の増減とは言えません。
- いじっぱり：20.0%→26.5%（+6.5pt）。つるぎのまい型が選んでいるほか、こだわりスカーフ型の一部の個体も選んでいるため、型の増減とは言い切れません。
- がんせきふうじ：19.5%→25.4%（+5.9pt）。こだわりスカーフ型・ステルスロック型に共通のため、型の増減とは言えません。
- こだわりスカーフ：17.9%→23.8%（+5.9pt）。こだわりスカーフ型だけが持つため、この変化はその型の増減を示します。
- ひかえめ：11.2%→5.6%（-5.6pt）。メガガブリアスZ型の一部の個体が選んでいるもので、型の増減とは言えません。
- ゴツゴツメット：11.0%→5.6%（-5.4pt）。ステルスロック型の一部の個体が持つもので、型の増減とは言えません。
- だいちのちから：25.2%→20.8%（-4.4pt）。記事の型ではメガガブリアスZ型だけが持ちますが、記事に載せていない型にもあるため、型の増減とは言い切れません。
- わんぱく：16.7%→12.8%（-3.9pt）。まきびし型が選んでいるほか、ステルスロック型の一部の個体も選んでいるため、型の増減とは言い切れません。
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
<!-- gate:rows start id=weak facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ型の選択技どくづきは確定3発。アシレーヌのムーンフォース（採用率98.8%）は確定2発で、最後は優先度+1のアクアジェットで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発（ばけのかわ込み）。ミミッキュのじゃれつく（採用率98.0%）は確定2発で、最後は優先度+1のかげうちで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のりゅうせいぐんは確定2発。カイリューのアイススピナー（採用率15.6%・少数派）は確定2発で、最後は優先度+2のしんそくで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のかえんほうしゃは乱数1発（69%）。マスカーニャのトリプルアクセル（採用率88.1%）は確定1発で、S223対S288（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">フラエッテ(永遠)<br><span style="font-size:0.8em;color:#64748b">メガフラエッテで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発。メガフラエッテのムーンフォース（採用率96.9%）は確定2発（ガブリアスのきあいのタスキ込み）で、同速（S169）のため先後は運次第で、勝ち切れません。</td>
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
<!-- gate:rows start id=strong facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のかえんほうしゃは乱数1発（88%）。メガルカリオのインファイト（採用率19.0%・少数派）は確定1発で、S223対S164で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のりゅうせいぐんは確定2発。イダイトウ(オス)のおはかまいり（採用率99.9%）は乱数3発（98%）で、S223対S214（スカーフ込み）で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のだいちのちからは確定2発（相手のきあいのタスキ込み）。キラフロルのヘドロウェーブ（採用率61.3%）は確定2発で、S223対S151で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガガブリアスZ型のだいちのちからは乱数2発（75%）。メガライチュウYのきあいだま（採用率97.1%）は乱数3発（98%）で、S223対S200で先手を取り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でガブリアスと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" loading="lazy">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アーマーガア<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率4位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率5位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率6位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率7位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メタグロス<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガメタグロスで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率9位・メガルカリオZで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カバルドン<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアスの弱点：こおり技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアスの弱点：ドラゴン技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアスの弱点：フェアリー技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">フラエッテ(永遠)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝ガブリアスの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：アシレーヌ＝ムーンフォース・うたかたのアリア・アクアジェット；ミミッキュ＝じゃれつく・かげうち・シャドークロー；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうのはどう；マスカーニャ＝トリックフラワー・トリプルアクセル・はたきおとす・とんぼがえり；フラエッテ(永遠)＝ムーンフォース・ドレインキッス</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=62a8273879e93047b97a93e70e4821bc7b13f002 -->
**強み**

- 得意な相手は4体です。使用率上位では、ルカリオ（7位）にかえんほうしゃ、イダイトウ(オス)（13位）にりゅうせいぐん、キラフロル（16位）にだいちのちからで勝てます。
- タイプ相性では、ガブリアスはほのお・どく・いわを半減以下、でんきを無効で受けられます。
- タイプ相性では、メガガブリアスZはほのお・みず・でんき・くさを半減以下で受けられます。

**弱み**

- 苦手な相手は5体です。使用率上位では、アシレーヌ（2位）のムーンフォース、ミミッキュ（5位）のじゃれつく、カイリュー（15位）のアイススピナーで先に倒されます。
- ガブリアスの弱点はこおり（×4）・ドラゴン・フェアリーです。
- メガガブリアスZの弱点はこおり・ドラゴン・フェアリーです。

**型の選び分け**

- 「メガガブリアスZ型」：他の型に無い技はりゅうせいぐん・かえんほうしゃ・だいちのちから。
- 「こだわりスカーフ型」：げきりんを必ず持つ（つるぎのまい型では選択技）。
- 「ステルスロック型」：こだわりスカーフ型のげきりんの代わりにドラゴンテールを持つ。
- 「つるぎのまい型」：他の型に無い技はつるぎのまい・ほのおのキバ。
- 「まきびし型」：他の型に無い技はまきびし。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は1位です（M-6: 1位）。
- 採用率の変化が大きいのはステルスロック（+7.9pt）・がんせきふうじ（+5.9pt）・こだわりスカーフ（+5.9pt）です。
<!-- gate:rows end id=summary -->
