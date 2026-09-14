---
title: '【ポケモンチャンピオンズ】セグレイブ 考察 M-6 シーズン 使用率8位のメガ進化と非メガ型解説'
description: 'M-6シーズン使用率8位のセグレイブ考察。メガ進化でこうげき・ぼうぎょ・とくこう・とくぼうが伸びる一方すばやさは種族値87のまま据え置きで、メガ石採用率51.8%に対し非メガのきあいのタスキ・いのちのたま型も約32%を占める。苦手/得意ポケモンをダメージ計算で解説。'
pubDate: '2026-09-14'
updatedDate: '2026-09-14'
heroImage: '../../assets/hero-baxcalibur-m6.png'
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
  <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" />
  <div>
    <h2 style="margin:0 0 8px">セグレイブ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">8位</strong>　持ち物: <strong>セグレイブナイト 51.8%</strong>
    </div>
  </div>
</div>

M-6シーズン、セグレイブは使用率8位につけています（本記事の使用率・採用率データは2026-09-10時点のものです）。ドラゴン/こおりの複合タイプに、きょけんとつげき（威力120）・こおりのつぶて（優先度+1）・じしんという高火力かつ役割の異なる技を同時に使える攻撃性能が持ち味です。メガ進化ではこうげき・ぼうぎょ・とくこう・とくぼうが伸びる一方すばやさの種族値は87のまま据え置かれますが、非メガ運用でも高い打点を出せるため、メガ石セグレイブナイト（採用率51.8%）を持たない、きあいのタスキ（21.1%）やいのちのたま（10.8%）を持たせた非メガ運用も一定の採用率を保っています。

---

## セグレイブの基本スペック

### 種族値

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
      <div style="width:57%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">115</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:72%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">145</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:46%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">92</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:38%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">75</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">86</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+15</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:44%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#64748b">±0</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげき・ぼうぎょ・とくこう・とくぼうが+15〜+30と大きく伸びる一方、すばやさは87のまま変化しません（S種族値据え置きはメガリザードンX/Yなど他のメガにも見られる仕様です）。タイプはドラゴン/こおりのまま変化しません。本記事の苦手/得意判定は、主流のいじっぱりEV32構成（A実数値216・メガ後249／S実数値139）を基準にしています。参考までに、すばやさに振るようきEV32構成ならS実数値は通常・メガ後とも152になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-14-ice.png" alt="こおり" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

弱点は5タイプすべてが×2止まりで、×4の弱点は持ちません。M-6上位ではミミッキュ（12位）のじゃれつく98.1%、ブリジュラス（7位）のラスターカノン75.1%・りゅうせいぐん65.3%、ガブリアス（1位）のげきりん27.3%・りゅうせいぐん28.6%が主な脅威です。みず・くさ・でんきは半減で受けられます。

### 特性

主流特性は**ねつこうかん（採用率98.9%）**で、ほのおタイプの技を受けると攻撃が1段階上がり、やけど状態にもなりません。ドラゴン/こおり複合へのほのお技は等倍（弱点ではありません）ですが、等倍で受けた1発をこうげき上昇に変えられる点が価値です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">87.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・でんきタイプへのサブウェポン。全採用技の中で最多</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのつぶて</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">82.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+1でSを無視して動ける一致技。すばやさで負ける相手への保険（同格以上の優先度技には先制できない）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>きょけんとつげき</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">79.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン一致の最大打点。使用後は次に行動するまで自分が無防備状態になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">46.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさを同時に1段階上げる積み技。すばやさが上がらないメガ進化の弱点を補う役割</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つららおとし</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">43.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおり一致の高威力技。30%の確率で相手をひるませる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つららばり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2〜5回連続で攻撃するこおり技。きあいのタスキで耐えた相手にも複数回当たる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげきを2段階上げる積み技。りゅうのまいと異なりすばやさは上がらない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>スケイルショット</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">2〜5回連続で攻撃し、自分のぼうぎょを下げてすばやさを上げる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりのキバ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこうタイプへのサブウェポン。10%でまひ・ひるみを狙える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>アイアンヘッド</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリータイプへのサブウェポン</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：メガ進化・物理いじっぱり型（メガ石 51.8%）

**性格採用率: いじっぱり 66.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガ進化・物理いじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ねつこうかん（98.9%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（最多分布23.9%）<br>
<strong>持ち物:</strong> セグレイブナイト（51.8%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・きょけんとつげき<br>
・じしん<br>
・こおりのつぶて
</div>
</div>
</div>

メガ進化でA145→175まで伸びる高火力を、りゅうのまいで積んでからきょけんとつげきで押し切る型です。じしんははがね・でんきタイプへのサブウェポン、こおりのつぶては優先度+1のため積む前や後手を取られた場面での保険になります。

**強み:**

A実数値249（いじっぱり・EV32）から放たれるきょけんとつげきは一撃が非常に重く、ぼうぎょ種族値117・とくぼう種族値101までメガ進化で耐久も強化されるため、非メガ型より積む前の1発を受けやすくなります。

**弱み:**

メガ進化してもすばやさの種族値は変わらないため、りゅうのまいを積むまではS139（EV32・いじっぱり）のままです。りゅうのまいで積む前提の型ゆえに積む1ターンを消費する必要があり、その間はガブリアス・ルカリオ（メガZ後S223、採用率93.7%）・ゲッコウガ・エースバーン・マスカーニャ・キラフロルなど、主流の性格・EVでもセグレイブより速い上位勢にスカーフ無しで上を取られるリスクを抱えます。

---

### 型2：非メガ・きあいのタスキ/いのちのたま型（きあいのタスキ21.1% / いのちのたま10.8%）

**性格採用率: いじっぱり 66.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">非メガ・きあいのタスキ/いのちのたま型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> ねつこうかん（98.9%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（最多分布23.9%）<br>
<strong>持ち物:</strong> きあいのタスキ（21.1%）またはいのちのたま（10.8%）
</div>
<div>
<strong>技構成:</strong><br>
・きょけんとつげき<br>
・じしん<br>
・こおりのつぶて<br>
・つららおとし
</div>
</div>
</div>

メガストーンの枠を持ち物に回し、初手から等倍以上の技を撃ち分ける型です。きあいのタスキは一撃で倒されるダメージを1度だけ耐える保険、いのちのたま（技の威力1.3倍、代わりに攻撃するたびに自分の最大HPの1/10の反動を受ける）は初手から最大火力を出したい場面で選ばれます。

**強み:**

きあいのタスキは、メガ型のぼうぎょ種族値117・とくぼう種族値101をもってしても耐えられない一撃を1度だけ耐えられる点がメガ型にはない強みです。いのちのたま採用時はA実数値216に威力1.3倍が乗り、メガ後のA249相当以上の打点をメガ進化枠を使わずに出せます。

**弱み:**

きあいのタスキ採用時はA実数値216のままでメガ後のA249には届かず、確定数で劣る場面があります。ぼうぎょ種族値92・とくぼう種族値86はメガ進化後のぼうぎょ種族値117・とくぼう種族値101より低く、受け出しでの耐久面もメガ型に劣ります。

---

## データ分析：メガ進化での能力配分とメガ石採用率の関係

メガ進化による能力上昇の配分先はポケモンごとに異なります。セグレイブは合計+100のすべてがこうげき・ぼうぎょ・とくこう・とくぼうに配分され、すばやさへの配分はありません。

セグレイブのメガ石採用率は51.8%で、非メガのきあいのタスキ（21.1%）・いのちのたま（10.8%）を合わせると31.9%が非メガ運用を選んでいます。ただし、S据え置きのメガポケモンが一律に低いメガ石採用率になるわけではありません。同じくS据え置きのメガリザードンY（採用率60.6%）やメガグソクムシャ（採用率98.9%）は高いメガ石採用率を維持しており、セグレイブのメガ石採用率が5割程度に留まる要因は、S据え置き自体よりも非メガ運用（きあいのタスキ・いのちのたま）が高い打点を出せる型として確立している点にあると考えられます。

---

## 苦手なポケモン

自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってじしん（採用率87.6%）を当てても確定3発。アシレーヌの主力ムーンフォース（採用率99.1%）は確定2発で、先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってじしん（採用率87.6%）を当てても確定4発と決め手を欠き、グソクムシャの主力アイアンヘッド（採用率76.0%）の確定2発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってじしん（採用率87.6%）を当てても確定3発。ブリジュラスの主力りゅうせいぐん（採用率65.3%、ドラゴン×2弱点）の確定2発で先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りつららおとし（採用率43.3%）は確定2発止まり。ミミッキュの主力じゃれつく（採用率98.1%、フェアリー×2弱点）も確定2発ですが、先に動かれて沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りじしん（採用率87.6%）は確定3発。アローラキュウコンの主力ムーンフォース（採用率47.1%、フェアリー×2弱点）も確定3発ですが、先に動かれて押し切られます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

自分・相手ともに採用率20%以上の主力技だけを使い、複数の代表的な型を通じて勝敗が一致した相手のみを掲載します（型によって有利・不利が分かれる相手は除外しています）。

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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってつららおとし（採用率43.3%、こおり×2弱点）で確定2発。カバルドンの主力じしん（採用率99.3%）は確定3発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってつららおとし（採用率43.3%、こおり×2弱点）で確定2発。ゴリランダーのウッドハンマー（採用率26.7%）も確定2発ですが、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回るものの、きょけんとつげき（採用率79.8%）は確定1発。マスカーニャの主力トリプルアクセル（採用率90.1%）は確定2発止まりで、返り討ちにできます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってきょけんとつげき（採用率79.8%）で確定4発。ギャラドスの主力じしん（採用率53.4%）も確定4発ですが、先に動いて押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率87.6%）とキラフロルの主力パワージェム（採用率80.8%）はともに確定2発。キラフロル（S151）の方がセグレイブ（S139）より速く、セグレイブは後手に回りますが、優先度+1のこおりのつぶてでとどめを刺せるため決着をつけられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">セグレイブが先手を取ってきょけんとつげき（採用率79.8%）で確定2発。イダイトウの主力ウェーブタックル（採用率96.5%）は確定3発止まりで、先に押し切れます（ただし過半数〈51.1%〉が採用するこだわりスカーフ持ちのイダイトウにはS195まで伸ばされて後手に回りますが、きょけんとつげきは確定1発のため1発耐えれば返り討ちにできます）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回るものの、きょけんとつげき（採用率79.8%）は確定2発。ゲッコウガのヘドロウェーブ（採用率73.5%）は確定3発止まりで、返り討ちにできます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってきょけんとつげき（採用率79.8%）で確定3発。ラウドボーンの主力フレアソング（採用率99.4%）も確定3発ですが、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってきょけんとつげき（採用率79.8%）で確定2発。ウォッシュロトムの主力ハイドロポンプ（採用率97.1%、みず×0.5耐性）は確定4発止まりで、先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">セグレイブが先手を取ってきょけんとつげき（採用率79.8%）で確定2発。イエッサンの主力マジカルシャイン（採用率70.2%、フェアリー×2弱点）も確定2発ですが、先に押し切れます（ただし過半数がこだわりスカーフを採用するイエッサンにはS220まで伸ばされて後手に回りますが、きょけんとつげきは確定1発のため1発耐えれば返り討ちにできます）</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でセグレイブと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
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
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）は素のじめん/ドラゴンであればセグレイブの弱点であるいわタイプの技を半減で受けられますが、ドラゴン・フェアリーはガブリアス自身も弱点として共有します。ただしガブリアスナイトZ（採用率35.0%）を持つメガガブリアスZはドラゴン単タイプになりいわは等倍に戻るため、この耐性は素のガブリアス運用時に限られます。

**グソクムシャ**（2位）は素の状態ではむし/みずですが、グソクムシャナイト（採用率98.9%）でメガ進化すると「むし/はがね」になります。メガグソクムシャはセグレイブの弱点であるはがねタイプの技を半減で受けられますが、いわタイプの技は等倍です（素のむし/みずはいわ×2弱点のため、はがね技を半減できるのはメガ進化後の恩恵です）。

**アシレーヌ**（3位）はみず/フェアリーで、セグレイブの弱点の1つであるドラゴンタイプの技を無効化でき、かくとうタイプも半減で受けられます。

**カバルドン**（4位）はじめん単タイプで、セグレイブの弱点であるいわタイプの技を半減で受けられます。

---

## まとめ

M-6のセグレイブは使用率8位で、メガ進化ではこうげき・ぼうぎょ・とくこう・とくぼうが伸びる一方すばやさは据え置きという能力配分が特徴です。

- **メガ石採用率は51.8%に留まる**：非メガのきあいのタスキ（21.1%）・いのちのたま（10.8%）が高い打点を出せる型として確立しており、両者を合わせた非メガ運用が31.9%を占めます
- **優先度技こおりのつぶてで後手のリスクを補える**：採用率82.4%と高く、すばやさが伸びないメガ型でも後手を取られる場面を補える武器です
- **主流技同士で判定すると得意10体・苦手5体**：カバルドン・ゴリランダー・マスカーニャ・ギャラドス・キラフロル・イダイトウ（メス）・ゲッコウガ・ラウドボーン・ウォッシュロトム・イエッサン（オス）には打点や耐久で優位に立てる一方、アシレーヌ・グソクムシャ・ブリジュラス・ミミッキュ・アローラキュウコンには決め手を欠いて先に押し切られます

苦手表の多くはドラゴン・フェアリー一致技（アシレーヌのムーンフォース、ブリジュラスのりゅうせいぐん、ミミッキュのじゃれつく、アローラキュウコンのムーンフォース）で弱点を突かれるケースで、特にフェアリー技が4件中3件を占めます。同居率7位のサーフゴーや9位のギルガルドのようなはがね複合はフェアリー技を半減できるため、パーティに編成しておくとこの弱点を補完できます。

---

*関連記事：[メガボーマンダ考察 M-6](/blog/salamence-analysis-m6/)*
