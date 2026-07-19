---
title: '【ポケモンチャンピオンズ】メガカイリュー 考察 M-4 シーズン 特殊型と物理先制型の使い分け'
description: 'M-4シーズン使用率12位のメガカイリュー考察。M-3から続くひかえめ特殊型が59.3%と主流を保ちつつ、ようき・いじっぱりの物理先制型が計23.9%に伸長。カイリュナイト採用率71.8%のデータからマルチスケイル運用と技構成の変化を分析します。'
pubDate: '2026-07-18'
updatedDate: '2026-07-18'
heroImage: '../../assets/hero-dragonite-m4.png'
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
  <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" />
  <div>
    <h2 style="margin:0 0 8px">メガカイリュー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">12位</strong>（M-3: 22位）　持ち物: <strong>カイリュナイト 71.8%</strong>
    </div>
  </div>
</div>

M-4シーズン、カイリューは使用率12位につけています。ドラゴン/ひこうタイプはメガ進化してもタイプが変わらない数少ないメガシンカ枠で、りゅうせいぐん・エアスラッシュを主軸にしたひかえめ特殊型が59.3%と依然主流である一方、M-4ではしんそく・げきりんを軸にした物理先制型（ようき12.7%＋いじっぱり11.2%）が合計23.9%まで伸びています。

---

## メガカイリューの基本スペック

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
      <div style="width:46%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">91</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:67%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">134</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#dc2626">-10</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:58%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">95</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:73%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+45</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+25</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">600</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+100</span>
  </div>
</div>

メガ進化でこうげきが-10される一方、とくこう+45・ぼうぎょ+20・とくぼう+25・すばやさ+20と特殊方面と耐久を厚くする配分です。カイリューは他のメガシンカ種と異なりタイプ変化がなく、ドラゴン/ひこうのまま種族値だけが上昇します。

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

こおり×4が最大の弱点です。M-4上位ではアローラキュウコン（16位）のフリーズドライ84.4%・ふぶき71.5%、ゲッコウガ（15位）のれいとうビーム87.2%が主な脅威です。でんきタイプはひこうの弱点をドラゴンの耐性が打ち消すため等倍で通ります（無効ではありません）。

### 特性

**マルチスケイル（99.2%）**が通常時・メガ進化後を通じて固定です。HPが満タンのときに受けるダメージが半減する特性で、初手の対面や交代直後の1発を大幅に軽減できます。ただしステルスロックや設置技などで一度でもHPが減った状態では効果を失うため、はねやすめでの全回復や無傷での立ち回りが前提になります。せいしんりょく採用は0.8%にとどまります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうせいぐん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">60.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン一致の最大打点。使用後にとくこうが2段階下がる反動あり</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">51.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプへの主力サブウェポン。メタグロス等に確定打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひこう一致で30%ひるみ。かくとうタイプへの打点にもなる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP1/2回復。マルチスケイル維持のため満タンHPを保つ手段</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>しんそく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>42.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+2で必ず先制。物理先制型のフィニッシャー</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>10まんボルト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・ひこうタイプへの選択技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス等ドラゴン耐性を持たないはがね複合への打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こうげき・すばやさを同時に1段階上げる積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理型のドラゴン一致高火力打点。使用後はあばれ状態になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうビーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス等ドラゴン・じめんタイプへの選択技</td>
</tr>
</tbody>
</table>
</div>

---

## M-4の採用型

### 型1：特殊アタッカー型（ひかえめ 59.3%）

**性格採用率: ひかえめ 59.3%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> マルチスケイル（99.2%）<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（最多分布18.4%）<br>
<strong>持ち物:</strong> カイリュナイト（71.8%）
</div>
<div>
<strong>技構成:</strong><br>
・りゅうせいぐん<br>
・エアスラッシュ<br>
・はねやすめ<br>
・かえんほうしゃ（51.3%）または10まんボルト（24.7%）またはれいとうビーム（11.0%）
</div>
</div>
</div>

りゅうせいぐん（ドラゴン・威力130・採用率60.9%）はタイプ一致の主力打点で、使用後にとくこうが2段階下がる反動があります。エアスラッシュ（ひこう・威力75・採用率50.8%）はタイプ一致でひるみ効果も狙え、はねやすめ（採用率49.2%）でHPを回復してマルチスケイルの発動条件（HP満タン）を維持します。4本目の打点はサブウェポンの選択技で、かえんほうしゃ（ほのお・威力90・採用率51.3%）がはがねタイプへの打点として最多ですが、10まんボルト（でんき・威力90・採用率24.7%）はみず・ひこうタイプへ、れいとうビーム（こおり・威力90・採用率11.0%）はガブリアス等ドラゴン・じめん複合への打点として一定数採用されます。

**強み:**

C216（ひかえめ・EV32）はりゅうせいぐんの一撃が重い一方、ドラゴン技はメタグロス（はがね/エスパー）に半減されるため通りません。メタグロスへの打点はサブウェポンのかえんほうしゃが担っており、メガメタグロス（使用率4位・H157・D実数値130）へ112〜134ダメージ（H157の71.3〜85.4%）で確定2発です。りゅうせいぐんは無振りの相手にも高い打点を出せるドラゴン・ひこうへの一致技として機能します。

**弱み:**

とくこうに寄せた分こうげきが無振りのため、物理方向の打点は持てません。りゅうせいぐんは連続使用でとくこうが下がり続けるため、交代のタイミングを選ぶ必要があります。

---

### 型2：物理先制型（ようき 12.7% / いじっぱり 11.2%）

**性格採用率: ようき 12.7% / いじっぱり 11.2%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">物理先制型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> マルチスケイル（99.2%）<br>
<strong>性格:</strong> ようき（S↑ C↓）またはいじっぱり（A↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（代表例）<br>
<strong>持ち物:</strong> カイリュナイト
</div>
<div>
<strong>技構成:</strong><br>
・しんそく<br>
・げきりん<br>
・じしん<br>
・りゅうのまい
</div>
</div>
</div>

しんそく（ノーマル・威力80・優先度+2・採用率42.4%）は先制技として機能し、げきりん（ドラゴン・威力120・採用率17.8%）はタイプ一致の高火力打点です。じしん（じめん・威力100・採用率22.6%）はブリジュラス（はがね/ドラゴン）への打点として、りゅうのまい（採用率21.4%）はこうげき・すばやさを同時に上げる積み技として採用されます。物理方向の技を並べる関係で、特殊アタッカー型とは技構成が排他的です。

**強み:**

ようきはS167（EV32）で、しんそくは優先度技のため相手のすばやさに関係なく先制できます。りゅうのまいを1回積めば以降のげきりん・じしんの打点が大きく伸びます。

**弱み:**

C148（ようき・とくこう↓・EV0）まで下がるため特殊技はほぼ選択肢に入らず、打点を通せる相手の範囲が物理耐性の高いポケモンに対して狭まります。りゅうのまいで積む1ターンは攻撃行動を消費するため、HPが満タンでマルチスケイルが機能している間は被弾しても軽減されますが、既に削られてマルチスケイルが解除された状態で積みにいくと、軽減なしでこの1ターンを受けきる必要があり隙になります。

---

## データ分析①：M-3→M-4 技・性格・持ち物の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-3</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-4</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">81.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>59.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-22.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>12.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+10.8pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">11.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり（性格）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>11.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+3.4pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんそく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>42.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-18.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はねやすめ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>49.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+23.1pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>51.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+17.6pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>50.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">+17.5pp</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-15.1pp</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">22.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">17.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a">新台頭</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カイリュナイト（持ち物）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">83.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>71.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626">-11.3pp</td>
</tr>
</tbody>
</table>
</div>

M-3で81.7%を占めていたひかえめが59.3%まで減り、ようき・いじっぱりが合計で9.7%から23.9%へ伸びました。特殊型の内訳を見ると、C↑・A↓のひかえめ（59.3%）に加えS↑・A↓の高速特殊型であるおくびょう（11.9%・M-3圏外から新台頭）も一定数存在し、特殊アタッカー全体（ひかえめ＋おくびょう）では71.2%を占めます。これに伴いしんそく（-18.6pp）・れいとうビーム（-15.1pp）が減少する一方、じしん・げきりんが圏外から新たに台頭しており、特殊一辺倒から物理先制型への構成比の変化がデータ上に表れています。はねやすめの採用率は26.1%→49.2%とほぼ倍増しており、マルチスケイルを維持するための回復手段の重要性が両型で共通して高まっています。カイリュナイトの採用率は83.1%→71.8%と低下しましたが、依然7割超が占めておりメガ進化前提の運用が基本線であることに変わりはありません。

---

## 苦手なポケモン

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
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フリーズドライ（こおり・採用率84.4%）・ふぶき（こおり・採用率71.5%）が×4弱点。持ち物はひかりのねんど92.0%でオーロラベール展開が主体のため、被弾機会自体が多い相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">れいとうビーム（こおり・採用率87.2%）が×4弱点。メガゲッコウガ（ゲッコウガナイト採用率49.5%）はおくびょう最速でS実数値約213に達し、メガカイリューのようき型S167より速く、一致弱点技で上から高い打点を持ちます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（フェアリー・採用率98.2%）が×2弱点。ばけのかわで初手の1発を無効化されるため、マルチスケイルとの初動の削り合いで後手に回りやすい相手です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワージェム（いわ・採用率82.1%）が×2弱点。だいちのちから（じめん・採用率62.4%）はひこう複合により無効ですが、パワージェムだけで安定した打点を持たれます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（ドラゴン・採用率93.3%）が×2弱点。こだわりスカーフ採用率84.2%で大多数がスカーフ持ちのため、物理先制型のS167でも上から動けません</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でカイリューと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" loading="lazy">
    <div class="name">ギルガルド</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ" loading="lazy">
    <div class="name">イダイトウ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**カバルドン**（1位）はじめん単タイプで、ステルスロックやあくびのサポートを担います。カイリューはひこう複合でじめん技を無効化できるため、カバルドンの弱点であるみず・くさをカイリューの耐性（みず×0.5・くさ×0.25）で補完できます。ただしカイリューの最大弱点であるこおりはカバルドンも半減できないため、この組み合わせでもこおり対策は別途必要です。

**ミミッキュ**（2位）はゴースト/フェアリーで、かげうち・じゃれつくの一致技によりカイリューが打点を通しにくいドラゴン・あくタイプへ圧力をかけられます。カイリューのエアスラッシュ・かえんほうしゃははがね・むしタイプへの打点になり、ミミッキュが苦手とするはがねタイプをカバーする役割分担です。

**アシレーヌ**（3位）はみず/フェアリーで、カイリューのこおり×4弱点をアシレーヌのオーロラベール（習得時）や高いD種族値でカバーしやすい組み合わせです。アシレーヌのどく弱点はカイリューには影響しないため、互いのタイプ相性が噛み合います。

**メタグロス**（4位）ははがね/エスパーで、カイリューのかえんほうしゃがはがねタイプ全般への打点として機能し、メタグロス自身がドラゴン・フェアリーへの耐性を持つため弱点タイプの分散に寄与します。

**ブリジュラス**（5位）ははがね/ドラゴンで、カイリューと同じドラゴンタイプを共有するため弱点の分散にはなりませんが、ラスターカノン（はがね一致）とカイリューのりゅうせいぐん・エアスラッシュで打点方向が異なる相手を分担できます。

---

## まとめ

M-4のカイリューは使用率12位（M-3: 22位）へ順位を上げ、特殊型と物理先制型の二極化が進んだシーズンです。

- **ひかえめ特殊型が59.3%と依然主流**：りゅうせいぐん・エアスラッシュ・かえんほうしゃの3タイプ攻撃ではがね・むしタイプにも打点を持てる構成
- **ようき・いじっぱりの物理先制型が合計23.9%へ伸長**（M-3合計9.7%から+14.2pp）：しんそく・げきりん・じしんを軸に、りゅうのまいで積む運用
- **カイリュナイト採用率は83.1%→71.8%に低下**しつつも依然7割超が占め、メガ進化前提の運用が基本線

ドラゴン/ひこうタイプが維持されるメガシンカという特性上、マルチスケイルを満タンHPで発動させ続ける立ち回りが両型に共通する軸になります。特殊・物理どちらの型を選ぶかは、パーティ内でメタグロス・ブリジュラスなどのはがねタイプへの打点役をカイリューに担わせるか、しんそくの先制フィニッシャーとして運用するかで判断が分かれます。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*

---

**[この構成を軸にした簡単構築を試す →](/party-suggest/mega-dragonite/)**
