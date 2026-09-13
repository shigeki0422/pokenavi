---
title: '【ポケモンチャンピオンズ】ボーマンダ 考察 M-6 シーズン 使用率2位のメガ物理/特殊解説'
description: 'M-6シーズン使用率2位のメガボーマンダ考察。特性スカイスキンでノーマル技がひこう技化・威力1.2倍になり、すてみタックル採用率73.4%は実質一致技として機能する。実戦火力と苦手/得意ポケモンをダメージ計算で解説。'
pubDate: '2026-09-13'
updatedDate: '2026-09-13'
heroImage: '../../assets/hero-salamence-m6.png'
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
  <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" />
  <div>
    <h2 style="margin:0 0 8px">メガボーマンダ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">2位</strong>　持ち物: <strong>ボーマンダナイト 98.0%</strong>
    </div>
  </div>
</div>

M-6シーズン、ボーマンダは使用率2位につけています（本記事の使用率・採用率データは2026-09-10時点のもの）。メガ進化で特性がスカイスキンに変わり、ノーマルタイプの技がひこうタイプになった上で威力が1.2倍になる特殊な仕様を持ちます。この効果によりすてみタックル（威力120）が実質ひこう一致の威力144技として機能し、採用率73.4%の主力打点になっている点がこのポケモンの核です。

---

## メガボーマンダの基本スペック

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
      <div style="width:48%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:68%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">135</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+50</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">110</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でぼうぎょが+50と最も大きく伸び、こうげき・とくこう・とくぼう・すばやさも均等に+10〜+20されます（合計+100）。タイプはドラゴン/ひこうのまま変化しません。本記事の苦手/得意判定は、主流のいじっぱりEV32構成（A種族値135→メガ後145、A実数値216／S種族値100→メガ後120、S実数値172）を基準にしています。参考までに、素早さに振るようきEV32構成ならS実数値は通常167→メガ後189になります。素早さはいじっぱりS172基準で統一しますが、一部の対面ではりゅうせいぐんを採用する特殊型（採用率21.2%）の方が確定数で優位になるため、その場合は行ごとに特殊型基準である旨を明記しています。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
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
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

こおり×4が最大の弱点です。M-6上位ではマスカーニャ（13位）のトリプルアクセル、アローラキュウコン（22位）のふぶき・フリーズドライ、ゲッコウガ（20位）のれいとうビームが主な脅威になります。じめんタイプはひこう複合により無効です。

### 特性

通常特性は**いかく（99.4%）**ですが、メガ進化すると特性は固定で**スカイスキン**に切り替わります。スカイスキンは「ノーマルタイプの技がひこうタイプになり、威力が1.2倍になる」特性で、すてみタックル（ノーマル・威力120）がメガ進化後はひこう技としてタイプ一致補正1.5倍が乗り、威力144相当として扱われます。ハイパーボイス（ノーマル・威力90）も同様にひこう技・威力108になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">75.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさを同時に1段階上げる積み技。全採用技の中で最多</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すてみタックル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">73.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">スカイスキンでひこう技化し威力144、さらに一致補正1.5倍が乗る最大打点。命中後に反動ダメージあり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">67.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・でんきタイプへのサブウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP1/2回復。りゅうのまいで積んだ後の耐久維持に使う</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊型のドラゴン一致最大打点。使用後にとくこうが2段階下がる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ハイパーボイス</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊型でもスカイスキンによりひこう技化・威力108相当</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいもんじ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">110</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・むしタイプへのサブウェポン</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">だいもんじより威力を抑えた命中安定型のサブウェポン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のドラゴン一致最大打点。使用後2〜3ターンあばれ状態になる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>やけっぱち</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふうせん持ちのはがねタイプなど、じしんが通らない相手へのサブウェポン</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：物理いじっぱり型（いじっぱり 53.2%）

**性格採用率: いじっぱり 53.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理いじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（通常時99.4%）※メガ後スカイスキン<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H1-A32-B1-S32（最多分布15.0%）<br>
<strong>持ち物:</strong> ボーマンダナイト（98.0%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうのまい<br>
・すてみタックル<br>
・じしん<br>
・はねやすめ
</div>
</div>
</div>

すてみタックル（威力120→スカイスキンでひこう技・威力144相当）を一致最大打点に据え、りゅうのまいで積んでから押し切る型です。じしんははがね・でんきタイプへのサブウェポン、はねやすめは積みに使ったターンの被弾を回復してから再度攻める運用を支えます。

**強み:**

A216（いじっぱり・EV32）はすてみタックルの一撃が非常に重く、りゅうのまいを1回積めばS258まで上昇して環境の大半のポケモンより先に動けるようになります。

**弱み:**

とくこうに寄せていないため特殊打点は持てず、りゅうせいぐんによるドラゴンタイプへの一致技は使えません。積みに1ターンを使う都合上、積む前の1発をどう受けるかが課題になります。

なお性格別では、とくこうを下げずにすばやさを伸ばせるようき（17.7%）も特殊型合計（ひかえめ9.5%+おくびょう7.2%=16.7%）を上回る採用率があります。技構成はいじっぱり型と同じ（すてみタックル軸）ため、本記事では技構成が異なる代表2型（物理いじっぱり型・特殊型）のみを型カードとして掲載しています。ようき型はS実数値が通常167・メガ後189になり、りゅうのまい未使用でもS172基準より速く動ける点に注意してください。

---

### 型2：特殊型（ひかえめ 9.5% / おくびょう 7.2%）

**性格採用率: ひかえめ 9.5% / おくびょう 7.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（通常時99.4%）※メガ後スカイスキン<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）またはおくびょう（S↑ A↓）<br>
<strong>EV:</strong> H1-B1-C32-S32（代表例4.6%）<br>
<strong>持ち物:</strong> ボーマンダナイト（98.0%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうせいぐん<br>
・ハイパーボイス<br>
・だいもんじ<br>
・はねやすめ
</div>
</div>
</div>

りゅうせいぐん（ドラゴン・威力130）を主軸に、ハイパーボイス（スカイスキンでひこう技・威力108相当）とだいもんじ（ほのお・威力110）で打点を散らします。りゅうのまいでは上がらないとくこう方面に依存するため、物理型とは技構成が完全に入れ替わる型です。

**強み:**

C189（ひかえめ・EV32）はりゅうせいぐんの一撃が重く、りゅうのまいで積めない代わりに最初から高火力を発揮できます。

**弱み:**

こうげきに寄せていないため、A216の物理型が持つすてみタックルの一撃は再現できません。りゅうせいぐんは使用後にとくこうが下がるため連発できず、後続の打点が落ちます。

---

## データ分析：りゅうのまいを積むと対面はどう変わるか

このセクションのみ、苦手/得意表（採用率20%以上の技に限定）とは異なり、採用率20%未満の技も含めた全技プールで判定しています。そのためルカリオのように、得意表では多数派技基準で「確定2発を耐えて返り討ちにできる」相手でも、ここでは少数派技を使う型を含めて「無積みでは負けている」と扱っている場合があります。

シミュレーション対象の全81組み合わせのうち、無積みの状態でボーマンダが後手（S172で負けている）だったのは24件です。りゅうのまいを1回積んでS258まで上昇させると、そのうち22件で先に動けるように変わります。積んでも後手のままなのはこだわりスカーフのマスカーニャ（S262）とゲッコウガ（S261）の2件のみですが、それ以外にも先手を取れる（または元から先手を取れている）にもかかわらず倒しきれず負けが残るビルドが11件あります（ガブリアス・セグレイブ・ブリジュラス・マスカーニャ〈きあいのタスキ型〉・ゲッコウガ〈きあいのタスキ型〉・アローラキュウコン・サザンドラ・カイリューの8体）。多くはこちらの確定2発に対し相手の返しが確定1発で打点が届きませんが、セグレイブのいのちのたま型のみ優先度技こおりのつぶてで先制されて落とされます。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">相手</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">主な持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">積み後のS比較</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">積んでも結果</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分S258 &lt; 相手S262</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">後手・敗北のまま</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分S258 &lt; 相手S261</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">後手・敗北のまま</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分S258 &gt; 相手S154（無積み時点でもS172で既に先手）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">先手を取っても1回耐えられ敗北</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こだわりスカーフ / ガブリアスナイトZ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分S258 &gt; 相手S223〜231（無積みではS172で後手）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">先手化してすてみタックル確定1発で勝利</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left"><img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ルカリオナイト / ナイトZ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分S258 &gt; 相手S180〜223</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">ナイトZ型は無積みでも既に勝ち。ナイト型は積むことで先手を取り勝利</td>
</tr>
</tbody>
</table>
</div>

こだわりスカーフのマスカーニャ（S262）・ゲッコウガ（S261）は、りゅうのまいで+1段階してもボーマンダのS258をわずかに上回るため先手を取られ続け、積んでも結果は変わりません。ガブリアスはナイトZ型・こだわりスカーフ型のいずれも、無積みではS172で後手のため負けていますが、りゅうのまいで先手を取り直すとすてみタックル確定1発で勝てるようになります。積んでも勝ちきれないのはきあいのタスキ型のみで、先手を取ってもすてみタックル確定2発に対しタスキで1発を耐えられ、返り討ちに遭います。ルカリオはナイトZ型が無積みのS172の時点で既に勝っている一方、ナイト型は無積みでは後手（S172<S180）で負けており、りゅうのまいで先手を取り直すことで勝利に変わります。りゅうのまいはS172から258まで引き上げる強力な積み技ですが、マスカーニャのきあいのタスキ型・ゲッコウガのきあいのタスキ型・アローラキュウコンのひかりのねんど型・ガブリアスのきあいのタスキ型には積むだけでは解決しない点に注意が必要です。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらの特殊型のりゅうせいぐん（採用率21.2%）は確定2発に対し、ガブリアスの一致技（りゅうせいぐん・げきりん）は確定1発。多くの型で後手に回るうえ、先手を取れる型でも確定数で押し切れず先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取れるものの、りゅうせいぐん（採用率21.2%）は確定2発止まり。セグレイブの一致技きょけんとつげき（採用率79.8%）の確定1発で返り討ちに遭います</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもじしん（採用率67.5%）は確定2〜4発と決め手を欠き、ブリジュラスの主力りゅうせいぐん（採用率65.3%）の確定1発で一撃を許します</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すてみタックル（採用率73.4%）は確定1〜2発を取れるものの、後手に回るためマスカーニャの主力トリプルアクセル（採用率90.1%、こおり×4）の確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもすてみタックル（採用率73.4%）は確定5発、型によっては圏外で決め手を欠き、アーマーガアの主力ブレイブバード（採用率37.6%）の確定4発に先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すてみタックル（採用率73.4%）は確定1〜2発を取れますが、後手に回るためゲッコウガの主力れいとうビーム（採用率92.9%、こおり×4）の確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すてみタックル（採用率73.4%）は確定2発止まりのうえ後手に回り、アローラキュウコンの主力ふぶき（採用率69.1%、こおり×4）の確定1発で先に倒されます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊型同士のミラーで、りゅうせいぐん（採用率21.2%）は確定2発止まり。多くの型で先手を取れてもサザンドラの主力りゅうせいぐん（採用率95.7%）の確定1発には押し切れず先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってもすてみタックル（採用率73.4%）は確定2発止まり。カイリューの主力りゅうせいぐん（採用率50.8%）の確定1発を受け切れず倒されます</td>
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
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定2発。アシレーヌの主力ムーンフォース（採用率99.1%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定2発。グソクムシャの主力アイアンヘッド（採用率76.0%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">すてみタックル（採用率73.4%）で確定2〜3発。カバルドンの主力じしん（採用率99.3%）はひこうタイプに無効のため打点が通りませんが、あくび（採用率96.5%）で機能停止させられるリスクには注意が必要です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りラスターカノン（採用率78.8%）を受けても確定2発なので耐え、じしん（採用率67.5%）の確定1発で返り討ちにできます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定2発。サーフゴーの主力ゴールドラッシュ（採用率94.3%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってじしん（採用率67.5%）で確定2発。ギルガルドの主力ポルターガイスト（採用率54.0%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定2発。ミミッキュの主力じゃれつく（採用率98.1%、フェアリー×2）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定1発。ゴリランダーの主力はたきおとす（採用率66.5%）は確定5発と大きく見劣りします</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってじしん（採用率67.5%）で確定2発。キラフロルの主力パワージェム（採用率80.8%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">多くの型で先手を取ってすてみタックル（採用率73.4%）を確定1発で通せます。イダイトウの主力ウェーブタックル（採用率96.5%）は確定3〜4発に留まり、決まる前に先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらの特殊型のりゅうせいぐん（採用率21.2%）が確定1発。メガリザードンXの物理技げきりん（採用率21.6%）も確定1発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定1発。メガリザードンYの主力オーバーヒート（採用率22.7%）は確定2発に留まり、決まる前に先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回るもののダストシュート（採用率75.8%）は確定3発なので耐え、すてみタックル（採用率73.4%）の確定2発で返り討ちにできます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回るもののフェイタルクロー（採用率94.7%）は確定3発なので耐え、すてみタックル（採用率73.4%）の確定1発で返り討ちにできます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定1発。ウルガモスの主力むしのさざめき（採用率35.4%）は確定4発と大きく見劣りします</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定3発。ラウドボーンの主力シャドーボール（採用率52.9%）は確定4発止まりで、先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0700-00.webp" alt="ニンフィア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ニンフィア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">29位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取ってすてみタックル（採用率73.4%）で確定2発。ニンフィアの主力ハイパーボイス（採用率99.3%）も確定2発ですが、先制で押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0655-00.webp" alt="マフォクシー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マフォクシー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回るもののマジカルシャイン（採用率33.7%）は確定2発なので耐え、すてみタックル（採用率73.4%）の確定1発で返り討ちにできます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-6でボーマンダと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**カバルドン**（1位）はじめん単タイプで、ステルスロックやあくびのサポートを担います。カバルドンの弱点であるみず・くさ・こおりのうち、みず・くさはボーマンダも耐性（×0.5・×0.25）を持ちますが、こおりはボーマンダ自身の弱点（×4）でもあるため補完できません。

**アシレーヌ**（2位）はみず/フェアリーで、ボーマンダの最大弱点であるこおりタイプへの耐性を持ち、被弾を分散できます。

**ギルガルド**（3位）ははがね/ゴーストで、ボーマンダの弱点であるフェアリータイプの技をギルガルドが半減で受けられ、互いの弱点タイプを分散できる組み合わせです。

**サーフゴー**（4位）ははがね/ゴーストで、ボーマンダの弱点であるフェアリー・いわタイプに対する耐性を持ちます。

---

## まとめ

M-6のボーマンダは使用率2位で、スカイスキンによりすてみタックルが実質一致技として機能する点が最大の特徴です。

- **物理いじっぱり型（53.2%）が主流**：すてみタックル（威力144相当）とりゅうのまいを軸に、A216・積み後S258まで到達する高い攻め性能を持ちます
- **りゅうのまいは強力だが万能ではない**：きあいのタスキのガブリアス・マスカーニャ・ゲッコウガ、ひかりのねんどのアローラキュウコンのように、積んでも耐えられて倒しきれない相手には勝ちきれません
- **主流技同士で判定すると得意18体・苦手9体**：アシレーヌ・グソクムシャ・カバルドン・ルカリオ・サーフゴー・ギルガルド・ミミッキュ・ゴリランダー・キラフロル・イダイトウ（メス）・メガリザードンX/Y・エースバーン・ウルガモス・ラウドボーン・オオニューラ・ニンフィア・マフォクシーには先手または打点で優位に立てる一方、ガブリアス・セグレイブ・ブリジュラス・マスカーニャ・アーマーガア・ゲッコウガ・アローラキュウコン・サザンドラ・カイリューには後手を取られる、または打点で届かず不利になります

苦手表の多くはこおり技×4（ゲッコウガ・アローラキュウコン・マスカーニャ）やドラゴン一致技のミラー（ガブリアス・サザンドラ・セグレイブ・ブリジュラス・カイリュー）が原因です。同居率2位のアシレーヌのようなこおり耐性を持つポケモンをパーティに編成しておくと、こおり技持ちへの弱点を補完できます。ガブリアス・マスカーニャ・ゲッコウガのようにりゅうのまいを積んでも勝ちきれない相手については、ボーマンダ単体で解決を狙わず、後続で受け止められるポケモンを編成しておく必要があります。

---

*関連記事：[メガカイリュー考察 M-4](/blog/dragonite-analysis-m4/)*
