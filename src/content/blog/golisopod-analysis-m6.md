---
title: '【ポケモンチャンピオンズ】グソクムシャ 考察 M-6 シーズン メガ進化後のかたいツメ型解説'
description: 'M-6シーズン使用率4位のメガグソクムシャ考察。メガ進化でむし/みず→むし/はがねへタイプ変化し弱点はほのお×4のみに。特性かたいツメで接触技が1.3倍、であいがしら・アイアンヘッド等の主要技と苦手/得意な相手を解説。'
pubDate: '2026-09-13'
updatedDate: '2026-09-13'
heroImage: '../../assets/hero-golisopod-m6.png'
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
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" />
  <div>
    <h2 style="margin:0 0 8px">メガグソクムシャ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px" />
      <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">4位</strong>　持ち物: <strong>グソクムシャナイト 98.9%</strong>
    </div>
  </div>
</div>

M-6シーズン、グソクムシャは使用率4位に入っています。通常時はむし/みずタイプですが、メガ進化するとむし/はがねへタイプが変化し、弱点がほのお×4の一点に絞られるのが最大の特徴です。であいがしら（先制技）・とんぼがえり（攻撃後に交代する技）の交代技とアイアンヘッドの一致打点を軸に、特性かたいツメで接触技を底上げする構成が主流です。

---

## メガグソクムシャの基本スペック

### 種族値（通常→メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガ後</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:75%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">125</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:88%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">140</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+35</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:35%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">90</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:20%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">40</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">530</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげき+25・ぼうぎょ+35・とくこう+10・とくぼう+30と、攻守両面が底上げされます。すばやさは40のまま変化せず、環境上位のほとんどのポケモンに先手を取られる遅さが弱点として残ります。主流のEV配分（H32-A32-D2）はすばやさに振らないため、実戦でのすばやさ実数値は60にとどまります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ（メガ進化後）：</strong>
  <img src="/images/types/type-06-bug.png" alt="むし" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-08-steel.png" alt="はがね" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく
  </td>
</tr>
</tbody>
</table>
</div>

弱点はほのお×4の一点のみです。M-6上位ではカイリュー（29位）のかえんほうしゃ66.8%が主な脅威です（サザンドラ〈25位〉も同技を73.3%採用しますが、グソクムシャが登場ターンにであいがしらで先制できれば打点で上回れるため、詳細は後述の得意表を参照）。いずれも本来はほのおタイプではないポケモンがサブウェポンとして採用しています（一致弱点を持つリザードン・エースバーンなど正真正銘のほのおタイプについては後述の苦手表を参照）。一方で通常時のむし/みずタイプが弱点にしていたでんき・ひこう・いわの弱点はメガ進化でいずれも解消されます。

ただしこれはトレードオフでもあります。通常時のむし/みずはほのお技を等倍（1.0）で受けられますが、メガ進化すると同じほのお技が×4に跳ね上がります。でんき・ひこう・いわの3弱点を消す代わりに、ほのお耐性そのものを失って唯一の急所に変えているのがメガ進化の実態です。

### 特性

**ききかいひ（通常時100%）→かたいツメ（メガ進化後）**が組み合わさっています。通常時はHPが1/2以下になると場から退いて手持ちに戻る特性で、メガ進化前の対面で無理に居座らず引く判断がしやすくなります。メガ進化後はかたいツメに切り替わり、接触技の威力が1.3倍になります。であいがしら・アイアンヘッド・とんぼがえり・きゅうけつ・インファイト・アクアジェットなど主要な採用技がいずれも接触技のため、実質的に一致技全般が強化される構成です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>であいがしら</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">83.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+2だが登場して最初に出す技でないと失敗。むし一致＋接触でかたいツメも乗る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">76.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね一致の主力打点。20%でひるみも狙える接触技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>とんぼがえり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃後に交代。すばやさ40の遅さを補い後続へつなぐ</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふいうち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1。相手が攻撃技を選んでいる時のみ成功する先制技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きゅうけつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">与えたダメージの1/2を回復。むし一致の粘り強い打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ドリルライナー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">急所ランク+1。サーフゴー等はがね複合への選択技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の防御・特防が1段階下がる高火力接触技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアジェット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1で先制（同格以上の優先度技には先行できません）。威力は低いが確実に一撃入れられる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきを2段階上げる積み技。積み型でのみ採用</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アクアブレイク</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">20%で相手の防御を下げる。カバルドン等じめんタイプへの打点</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：先制交代型（非積み・いじっぱり主体）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">先制交代型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ききかいひ（100%）→メガ進化後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H32-A32-D2（最多分布22.1%）<br>
<strong>持ち物:</strong> グソクムシャナイト（98.9%）
</div>
<div>
<strong>技構成:</strong><br>
・であいがしら<br>
・アイアンヘッド<br>
・とんぼがえり<br>
・ふいうち または きゅうけつ
</div>
</div>
</div>

であいがしら（採用率83.0%）とアイアンヘッド（76.0%）でタイプ一致の打点を並べ、とんぼがえり（50.9%）ですばやさ40の遅さを補って後続に繋ぎます。4本目はふいうち（49.3%）で相手の攻撃選択を狩るか、きゅうけつ（26.8%）で被弾を回復しながら粘るかで選択が分かれます。

**強み:**

とんぼがえりで後続に負荷を渡しつつ、であいがしらは登場ターンに限り優先度+2で先制打点を出せます（メガ進化は行動前に処理されるため、この時点で既にメガ進化後の攻撃力です）。とんぼがえりによる後続への繋ぎと組み合わせることで、遅いすばやさを実質的にカバーできる構成になっています。

**弱み:**

つるぎのまいを積まないため火力の伸びしろが乏しく、耐久の高い相手を一撃で崩す手段に欠けます。積み技を採用しない分、とんぼがえり後も後続頼みの立ち回りが基本になります。

---

### 型2：つるぎのまい積み型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ききかいひ（100%）→メガ進化後かたいツメ<br>
<strong>性格:</strong> ゆうかん（A↑ S↓。すばやさ実数値がさらに下がる）<br>
<strong>EV:</strong> H31-A32-D3（EV分布3位・8.8%）<br>
<strong>持ち物:</strong> グソクムシャナイト
</div>
<div>
<strong>技構成:</strong><br>
・つるぎのまい<br>
・アイアンヘッド<br>
・インファイト または きゅうけつ<br>
・であいがしら
</div>
</div>
</div>

つるぎのまい（採用率15.1%）でこうげきを2段階上げてからアイアンヘッド・インファイト（採用率24.9%）で押し切る構成です。インファイトは威力120と高火力ですが、使用後に自分の防御・特防が下がるため積んだ後の連打が前提になります。

**強み:**

1回積めばアイアンヘッド・インファイトの打点が大きく伸び、耐久の高い相手も崩しやすくなります。とんぼがえり型とは異なり、積んだ後は後続を頼らず自力で押し切れます。

**弱み:**

積みターンは攻撃できないため、その間に相手から先に攻撃を受けて被弾が嵩みます。インファイト採用時は連続使用で防御・特防が下がり続け、一撃も受けられなくなっていきます。

---

## データ分析：トップメタのほのお技採用状況

メガグソクムシャの唯一の弱点であるほのお×4を突く技は、本来ほのおタイプでないポケモンにも幅広くサブウェポンとして採用されています。M-6使用率TOP30のうち、ダメージを与えるほのお技を採用率5%以上で持つ非ほのおタイプは以下のとおりです（オオニューラ・パーモットのほのおのパンチは1割未満の少数派ですが掲載）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">本来タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">採用ほのお技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">サザンドラ（25位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">あく/ドラゴン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ／だいもんじ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.3%／19.3%</strong></td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">カイリュー（29位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.8%</strong></td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">ギャラドス（15位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">みず/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やけっぱち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.9%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">ガブリアス（2位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/じめん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">ニンフィア（28位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フェアリー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.7%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">ボーマンダ（1位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴン/ひこう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいもんじ／かえんほうしゃ／やけっぱち</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.4%／14.1%／7.6%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">イエッサン(オス)（30位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">エスパー/ノーマル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マジカルフレイム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">オオニューラ（23位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かくとう/どく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.9%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:32px;height:32px;vertical-align:middle;margin-right:6px">パーモット（27位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">でんき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6.4%</td>
</tr>
</tbody>
</table>
</div>

サザンドラ・カイリューはかえんほうしゃの採用率が7割前後に達していますが、両者の明暗は分かれます。サザンドラに対してはグソクムシャが繰り出したターンに限りであいがしらが優先度+2で先制で通るため、その1手だけを見れば多数派技同士の撃ち合いでグソクムシャ側が勝ち越します（得意なポケモン参照）。一方カイリューはであいがしらでは処理しきれず、アイアンヘッドの確定数もかえんほうしゃに並ばれるため、後手を取るグソクムシャが押し負ける明確な対策必須の相手です（苦手なポケモン参照）。M-5と比べてもかえんほうしゃの採用率はカイリューで59.9%→66.8%（+6.9pp）、サザンドラで66.5%→73.3%（+6.8pp）と両者とも増加しており、グソクムシャの台頭に対する対策としてほのお技採用がシーズンを追うごとに強まっている傾向がうかがえます。

---

## 苦手なポケモン

自分側・相手側とも採用率20%以上の多数派技同士で撃ち合った場合の確定数を全代表型で検証し、型が変わっても一貫して負け越す相手のみを掲載しています（代表型によって勝敗が割れるガブリアス・マフォクシーは除外しています）。グソクムシャはすばやさ実数値60と遅く、以下はいずれも後手に回った上での確定数比較です。なお使用率30位のイエッサン(オス)（マジカルフレイム採用率60.3%）は検証時点の使用率TOP30スナップショットに含まれておらず未検証のため、苦手/得意いずれの表にも掲載していません。また一部の行は採用率25%前後の技（インファイト・ドリルライナー・きゅうけつ等）に依存しており、残り7〜8割の非採用個体には当てはまらない点に注意してください。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのアイアンヘッド（採用率76.0%）と相手のすてみタックル（採用率73.4%）は互いに確定2発で並びますが、後手に回るグソクムシャは先に打点を通されて落とされます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">グソクムシャの主力技（アイアンヘッド・であいがしら・とんぼがえり・インファイト）はいずれもみず/ひこう複合に半減され、等倍で通るのはあくタイプのふいうち（採用率49.3%）のみです。そのふいうちも確定4発にとどまり、相手のやけっぱち（採用率28.9%、残り約7割は非採用）の確定2発に対して打点不足が主因で劣ります。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のかえんほうしゃ（採用率42.9%）は確定1発なのに対し、こちらのドリルライナー（採用率25.6%）は確定2発と打点で大きく劣ります。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のかえんほうしゃ（採用率42.9%）は確定1発なのに対し、こちらのふいうち（採用率49.3%）は確定2発と打点で劣ります。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のかえんボール（採用率98.7%）は確定1発、こちらのドリルライナー（採用率25.6%）も確定1発と互角ですが、後手に回るため先に落とされます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のほのおのまい（採用率70.6%）は確定1発なのに対し、こちらのドリルライナー（採用率25.6%）は確定2発と打点で劣ります。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のフレアソング（採用率99.4%）は確定2発なのに対し、こちらのドリルライナー（採用率25.6%）は確定3発と打点で劣ります。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのアイアンヘッド（採用率76.0%）と相手のかえんほうしゃ（採用率66.8%）は互いに確定2発で並びますが、後手に回るグソクムシャは先に打点を通されます。</td>
</tr>
</tbody>
</table>
</div>

いずれも後手に回ると打点で追いつけない相手のため、居座らずとんぼがえりで後続に引き継ぐか、対面させる前にサイクル戦で相手の耐久を削っておくのが基本の対策になります。

---

## 得意なポケモン

同様に自分側・相手側とも採用率20%以上の多数派技同士で撃ち合った場合の確定数を全代表型で検証し、代表的な採用型が変わってもグソクムシャ側が一貫して勝ち越す相手のみを掲載しています（代表型によって勝敗が割れるガブリアス・マフォクシーは除外しています）。使用率30位のイエッサン(オス)は前述の理由により本表でも未検証のため掲載していません。また一部の行（ルカリオ・ブリジュラス・アーマーガア・ギルガルド・パーモット・ウォッシュロトム）は採用率25%前後の技に依存しており、その技を持たない多数派の個体には成立しない場合があります。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">得意な理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のうたかたのアリア（採用率92.6%）は確定4発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定3発と打点で上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のじしん（採用率99.3%）は確定5発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定3発と打点で大きく上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のじしん（採用率87.6%）は確定4発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定2発と打点で大きく上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のはどうだん（採用率75.1%）は確定3発なのに対し、こちらのインファイト（採用率24.9%）は確定2発と打点で上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のシャドーボール（採用率99.9%）は確定3発なのに対し、こちらのふいうち（採用率49.3%）は確定2発と打点で上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の10まんボルト（採用率63.1%）は確定5発なのに対し、こちらのインファイト（採用率24.9%）は確定1発と打点で大きく上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のポルターガイスト（採用率54%）は確定3発なのに対し、こちらのドリルライナー（採用率25.6%）は確定2発と打点で上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のシャドークロー（採用率59.2%）は確定5発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定2発と打点で大きく上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のふいうち（採用率27%）は確定5発なのに対し、こちらのとんぼがえり（採用率50.9%）は確定2発と打点で大きく上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の10まんばりき（採用率50.3%）は確定4発なのに対し、こちらのであいがしら（採用率83%、繰り出したターンに限り優先度+2で成功）は確定1発と打点で大きく上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のブレイブバード（採用率37.6%）は確定5発なのに対し、こちらのインファイト（採用率24.9%）は確定4発と打点で上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のパワージェム（採用率80.8%）は確定4発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定2発と打点で大きく上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のウェーブタックル（採用率96.5%）・こちらのふいうち（採用率49.3%）はともに確定2発ですが、ふいうちの優先度+1により先にトドメを刺せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のなみのり（採用率33.7%）は確定3発なのに対し、こちらのとんぼがえり（採用率50.9%）は確定2発と打点で上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のふぶき（採用率69.1%）では倒しきれないのに対し、こちらのアイアンヘッド（採用率76.0%）は確定1発と打点で大きく上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のハイドロポンプ（採用率97.1%）は確定4発なのに対し、こちらのきゅうけつ（採用率26.8%）は確定3発と打点で上回れます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のインファイト（採用率99.4%）は確定3発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定1発と打点で大きく上回れます。ただしグソクムシャの唯一の弱点を突くほのおのパンチ（採用率6.9%）を持つ少数派もいる点は留意が必要です。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のかえんほうしゃ（採用率73.3%）・こちらのであいがしら（採用率83%）はともに確定1発です。グソクムシャが繰り出したターンに限りであいがしらが優先度+2で先にトドメを刺せますが、これは初手対面限定の話です。サザンドラのかえんほうしゃも確定1発のため、居座り（2ターン目以降）の対面ではこちらが先制権を持たず即座に落とされる点に注意してください。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のインファイト（採用率77.5%）は確定3発なのに対し、こちらのドリルライナー（採用率25.6%）は確定2発と打点で上回れます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のマジカルフレイム（採用率22.7%）は確定2発なのに対し、こちらのアイアンヘッド（採用率76.0%）は確定1発と打点で上回れます。</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-6でグソクムシャと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）はドラゴン/じめんで、グソクムシャの唯一の弱点であるほのおを半減で受けられ、弱点をカバーする組み合わせです。**アシレーヌ**（2位）はみずタイプでほのお技を半減で受けられ、同じくグソクムシャの弱点をカバーする役割を担います（**カバルドン**〈4位〉はじめん単タイプでほのおは等倍のため耐性はありません）。

---

## まとめ

M-6のグソクムシャはメガ進化前提で使用率4位に定着しており、タイプ変化で弱点をほのお×4のみに絞り込んでいる点が最大の特徴です。

- **であいがしら・アイアンヘッド・とんぼがえりの先制交代型が主流**で、特性かたいツメにより接触技全般の打点が底上げされます
- **メガ進化してもすばやさ種族値40は変化しない**ため、環境上位の多くのポケモンに先手を取られる遅さが最大の弱点として残ります
- **多数派技同士の撃ち合いで一貫して負け越す相手は8体**：ボーマンダ・ギャラドス・メガリザードンX・メガリザードンY・エースバーン・ウルガモス・ラウドボーン・カイリュー。いずれも弱点を突く技か、半減でも押し切れる火力を持ち、後手のグソクムシャが打点で追いつけません
- **一方で一貫して勝ち越す相手は20体**：アシレーヌ・カバルドン・セグレイブ・ルカリオ・サーフゴー・ブリジュラス・ギルガルド・ミミッキュ・マスカーニャ・ゴリランダー・アーマーガア・キラフロル・イダイトウ(メス)・ゲッコウガ・アローラキュウコン・ウォッシュロトム・オオニューラ・サザンドラ・パーモット・ニンフィアで、相手の主力技が等倍止まりか、であいがしら・ふいうちの優先度で先手を取れるケースです

弱点タイプが一点に絞られている分、対策すべき相手がはっきりしているのがグソクムシャの特徴です。ほのおを半減で受けられるガブリアスやアシレーヌなど弱点をカバーできるポケモンと組み合わせ、遅さをとんぼがえりでカバーする構築が基本線になります。
