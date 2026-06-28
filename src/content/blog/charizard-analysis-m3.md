---
title: '【ポケモンチャンピオンズ】リザードン考察 M-3 使用率8〜10位 メガY型とX型の採用率と立ち回り'
description: 'M-3シングルバトルで使用率8〜10位のリザードンを分析。メガY（リザードナイトY 77.5%）とメガX（21.1%）の型別採用率・種族値・技構成・立ち回りを解説。ひでり+ソーラービーム76.5%採用の構造から読み取れる運用思想も考察。'
updatedDate: '2026-06-27'
pubDate: '2026-06-27'
heroImage: '../../assets/hero-charizard-m3.png'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">リザードン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">8〜10位</strong>（M-2は5位）　持ち物: <strong>リザードナイトY 77.5% / リザードナイトX 21.1%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン時点の集計です

M-3のリザードンはリザードナイトY採用率77.5%を中心に、メガリザードンY（ほのお/ひこう）として運用されるケースが多数派です。特性**ひでり**（メガ進化後）でほのお技を1.5倍に強化しつつ、ソーラービームを溜めなしで使えるようにすることで、1ターンで2タイプの攻撃を打ち分ける火力型として機能します。M-2では5位だった使用率が8〜10位に下落しており、環境変化との関係を含めて分析します。

---

## なぜメガリザードンYが採用されるのか

### 1. ひでり+ソーラービームで2タイプ制圧

メガリザードンYは場に出た瞬間に特性ひでりで晴れ状態にします。晴れにより**ほのお技は1.5倍**、**ソーラービームは溜めターンなしで即撃ち**できます。C実数値232（ひかえめ H2 C32 S32）のかえんほうしゃは晴れ補正込みで実質威力202相当となり、ソーラービームの実質威力180（STAB、補正なし）を上回ります。ひでりという1つの特性が「ほのお技強化」と「ソーラービーム即撃ち」の2役を担うため、持ち技2枠でほのお・くさの2タイプをフルパワーで使い分けられます。

ソーラービーム採用率76.5%とかえんほうしゃ採用率47.5%が並立しているのは、この構造の反映です。ソーラービームはみず/じめん複合（×4）やみず単体（×2）など、ほのお技が半減以下になる相手への補完として機能し、かえんほうしゃはひでり補正込みで汎用打点になります。

### 2. メガリザードンXとの役割分担

メガリザードンX（ほのお/ドラゴン、リザードナイトX 21.1%）は物理型で、ニトロチャージ（26.0%）・フレアドライブ（20.8%）・りゅうのはどう（16.0%）を採用します。A実数値200（いじっぱり H2 A32 S32）でニトロチャージ・りゅうのまいを積んで制圧するアタッカーです。一方でメガYは特殊主体でひかえめ42.8%が最多。2つのメガ進化は特殊/物理で役割が完全に分かれており、Yが多数派を占める理由は「ひでり+ソーラービームの汎用性がXのりゅうのまい制圧より構築に組み込みやすい」点にあります。

---

## 基本スペック

### 種族値（通常/メガ後比較）

<div style="max-width:520px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0;font-weight:700;font-size:0.85em;color:#555">
    <span style="width:80px;min-width:80px"></span>
    <span style="flex:1;text-align:center">通常</span>
    <span style="width:72px;text-align:center">メガY</span>
    <span style="width:72px;text-align:center">メガX</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right">78</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">84</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+46</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">111</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+33</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">109</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+50</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+21</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
    <span style="width:32px;text-align:right">85</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right">100</span><span style="width:40px"></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:80px;min-width:80px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">534</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">700</span><span style="width:40px"></span>
  </div>
</div>

メガYは特にCが109→159（+50）と大きく伸び、メガX はAが84→130（+46）・Bが78→111（+33）と上昇します。Sはどちらも100で変わらず、S実数値はひかえめ152・おくびょう167（メガY）、いじっぱり152・ようき167（メガX）です。

### タイプ・弱点

<div class="type-row">
  <strong>メガY タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:8px 0 16px">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2/×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず（×2）</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき（×2）</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ（×4）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう（×0.5）</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.25）</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね（×0.5）</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお（×0.5）</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（×0.25）</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー（×0.5）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
  </td>
</tr>
</tbody>
</table>
</div>

<div class="type-row">
  <strong>メガX タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:8px 0 16px">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5以下）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし（×0.5）</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね（×0.5）</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお（×0.25）</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ（×0.25）</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき（×0.5）</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なし</td>
</tr>
</tbody>
</table>
</div>

メガYとXではタイプが大きく異なります。YはじめんをS無効化する一方、でんき×2・いわ×4の弱点を持ちます。XはYで弱点だったじめん・でんきをそれぞれ×2・×0.5に変換し、いわ弱点が×4から×2に軽減されます。ただしXはドラゴン弱点が新たに生じ、Y同士の打ち合いと同様に環境上位のドラゴン技が刺さる点には注意が必要です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center;width:40px">順位</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">技名</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">威力</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:center">採用率</th>
  <th style="padding:6px 10px;border:1px solid #cbd5e1;text-align:left">主な型</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">1</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ソーラービーム</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">76.5%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型中心（ひでりで溜めなし即撃ち）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">47.5%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（ひでり補正込み実質202相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">45.5%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（ひこう一致補正、かくとう等に通る）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">30.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（C2段階ダウン、ひでり補正込み実質292相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ニトロチャージ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">26.0%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（S+1。りゅうのまいと合わせて積み型）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ウェザーボール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50（晴れ時100・ほのお）</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">24.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（晴れでほのお100、STAB+ひでりで実質225相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>フレアドライブ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">20.8%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（物理一致打点）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はねやすめ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">18.7%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（HP回復で場持ちを伸ばす）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">16.0%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（特殊ドラゴン打点）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.1%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（A+1 S+1。積み後に制圧）</td>
</tr>
</tbody>
</table>
</div>

Y型はソーラービーム・かえんほうしゃ・エアスラッシュの3枠がほぼ確定枠で、4枠目をオーバーヒート（C2段階ダウン覚悟の最大瞬間火力）・ウェザーボール（晴れでほのお実質威力225）・はねやすめ（回復）から選ぶ構成です。X型はフレアドライブ・ニトロチャージを軸に、りゅうのはどう（16.0%）またはりゅうのまい（15.1%）で打ち分ける構成が読み取れます。

---

## 主要型の解説

### 型1: メガリザードンY 特殊アタッカー型（最多採用）

**持ち物: リザードナイトY 77.5%　性格: ひかえめ 42.8%（最多）/ おくびょう 33.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガリザードンY 特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（84.1%）※メガ後ひでり<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）／おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32（採用率41.9%・最多）<br>
<strong>持ち物:</strong> リザードナイトY（77.5%）
</div>
<div>
<strong>技構成:</strong><br>
・ソーラービーム（76.5%）<br>
・かえんほうしゃ（47.5%）<br>
・エアスラッシュ（45.5%）<br>
・<span style="color:#1d4ed8">オーバーヒート30.9% / ウェザーボール24.8% / はねやすめ18.7%</span>
</div>
</div>
</div>

**実数値（H2 C32 S32）:**
- ひかえめ: HP154 C232 S152
- おくびょう: HP154 C211 S167

**強み（ひかえめ vs おくびょう）:**

ひかえめ型はC232でかえんほうしゃの晴れ込み打点が高く、おくびょう型はC211に落ちる代わりにS167でより多くの相手に先手を取れます。S152（ひかえめ）とS167（おくびょう）の差は、S153〜167帯の相手への先手を確保できるかどうかに影響します。ガブリアス（最速S169）は両型とも後手になるため、S上限で両型の差は消えます。火力か速度かの選択で、多数派はひかえめ（42.8%）です。

**弱み:**

いわ技に×4弱点を持ちます。環境上のいわ技使用ポケモンに対しては選出を控えるか、ほのお技で先に倒す立ち回りが必要です。また、でんき×2弱点があるため、メガライチュウY（S実数値200・ノーガード）に対しては必ず後手となり、でんき技を受けて大ダメージを負います。

---

### 型2: メガリザードンX 物理積み型

**持ち物: リザードナイトX 21.1%　性格: いじっぱり 15.0%（最多）/ ようき 6.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガリザードンX 物理積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（84.1%）※メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）／ようき（S↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率11.8%）<br>
<strong>持ち物:</strong> リザードナイトX（21.1%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ（20.8%）<br>
・ニトロチャージ（26.0%）<br>
・りゅうのはどう（16.0%）<br>
・<span style="color:#1d4ed8">りゅうのまい（15.1%）</span>
</div>
</div>
</div>

**実数値（H2 A32 S32）:**
- いじっぱり: HP154 A200 S152
- ようき: HP154 A182 S167

**強み（Y型との差）:**

X型はメガ後特性かたいツメが接触技の威力を1.3倍にするため、フレアドライブ（接触、威力120）の実質打点がY型のかえんほうしゃ（晴れ前提）と異なる条件で発揮されます。Y型は晴れを自分で用意しますが、X型はかたいツメ補正が特性依存で天候に左右されない点が差別点です。りゅうのまい+ニトロチャージで積み切れれば、A・Sともに上昇して物理制圧が狙えます。

**弱み（Y型との差）:**

Yと同じS100でよりSが確保しにくく、じめん×2弱点が増えます。ガブリアス（使用率1位）がじしんを採用する場合はX型にとって刺さる弱点であり、Y型のじめん無効に比べて選出リスクが高まります。積みに複数ターンを要するため、高速アタッカーが多い環境では積みターンを作れないケースがある点も使い勝手に影響します。

---

## 環境ポケモンへの相性分析

下表はメガリザードンY（ひかえめ H2 C32 S32、HP154 C232 S152）を基準とし、各相手のメガ運用が主流の場合はメガ後種族値で比較します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン（環境順位）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">相性</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 条件次第</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのほのお・くさ・ひこう技はいずれも等倍以下。スカーフ採用率26.7%（S約253）では先手を取れず、タスキ採用率38.7%では1発で落とせない。スカーフなし・タスキなしの型（34.6%程度）に対してはS152で後手となりじしん・げきりんを受ける形になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃがはがね/ドラゴンに等倍、かつ晴れ補正込みで打点が高い。ブリジュラス無補正S実数値137はメガYのS152より遅く先手が取れる。スカーフ未採用（オボンのみ29.8%・たべのこし29.4%が主体）。ただしブリジュラスはでんき技を持つ個体が多く、被弾すると×2弱点を突かれる点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃがはがね/エスパーに×2で抜群。メタグロスS70はメガY S152より遅い。晴れ補正込みで高火力の先制打点が入る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガライチュウY（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガライチュウY採用率96.4%。メガ後S130・特性ノーガード（おくびょう実数値200）で必ず先手。でんきタイプのため晴れほのお技が通らず等倍以下。こちらのでんき×2弱点を突かれる。S差が大きく先手を確保できない対面の典型</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（同居率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 条件次第</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリーへのかえんほうしゃは×0.5半減。ソーラービームはみず/フェアリーに×2抜群で打点はある。ただしアシレーヌのみず技がリザードンY（みず×2弱点）に大ダメージを与えるため、先手で動かれると一撃圏に入る可能性がある。S60（最速実数値123）で先手は取れるが、オボン採用率58.0%で回復されると2発必要になる場面がある</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラグラージナイト採用率74.8%。メガ後はみず/じめんでソーラービームが×4で抜群。メガ後S70（最速S134）でメガYのS152（ひかえめ）より遅く先手が取れる。かえんほうしゃはみず半減だが、ソーラービームの×4打点でメインの打点は確保できる</td>
</tr>
</tbody>
</table>
</div>

### 苦手なポケモンと対策

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガライチュウY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特性ノーガード・メガ後S130（おくびょう実数値200）でリザードンY（S152）より速い。でんき×2弱点を先手で突かれ、こちらのほのお技は等倍以下で返せない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラスやガブリアスなど、ライチュウに打点を持つパートナーで対処。リザードンでの直接対面は避ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリーでかえんほうしゃは半減。ソーラービームは×2で通るが、みず技でY型のみず×2弱点を突き返される。オボンのみ採用率58.0%で場持ちが高く、ソーラービーム1発では落とせない場合に反撃のみず技を受ける対面になる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね技でフェアリー半減）や同居率1位のガブリアスで処理。リザードン自身での突破は困難</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（同居率8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドンの特性すなおこしによる砂嵐でひでり状態が上書きされると、ソーラービームが1ターン溜めに戻り、ほのお技の晴れ補正も消える。打点自体はソーラービームが×2抜群で入るが、天候を制された後は安定した火力が出せなくなる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">天候の打ち消し合いが発生する。カバルドンに先手で動かれないよう先発配置を工夫する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 同居率上位パートナー（M-3）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じしんでX型の弱点を補完しつつ、リザードンが苦手なライチュウへの打点も持つ</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">リザードンが苦手なみず・ドラゴン勢をじゃれつく・かげうちで牽制。弱点の棲み分けがある</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">とんぼがえりで対面操作し、リザードンを安全に着地させる役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでリザードン弱点のでんき・いわを半減し、耐性補完の中核</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでリザードン弱点のいわ・でんきを半減。リザードンが有利なはがね複合へのルートを共有できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">選出を分散させる役割。リザードンが苦手な相手にアシレーヌで対応する選択肢を用意する</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ひこうでリザードン弱点のいわ・でんきを補完。高耐久で前に出て盾になれる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">天候展開が競合するため基本的に非同時選出。じめん打点でリザードンが苦手な相手を処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)">
    <div class="name">イダイトウ</div>
    <div class="rate">同居率10位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず技を持ちリザードンとタイプ補完が取れる。いわ複合への打点を分担できる</div>
  </div>
</div>

---

## データ分析①：M-2→M-3でのY/X比率シフトと使用率下落

M-3でリザードンの使用率が5位から8〜10位に下落した一方、メガY比率はM-2の63.6%からM-3で77.5%へ上昇しています。

| 項目 | M-2 | M-3 | 変化 |
|---|---|---|---|
| 使用率順位 | 5位 | 8〜10位 | 下落 |
| リザードナイトY | 63.6% | 77.5% | +13.9pt（Y比率上昇） |
| リザードナイトX | 34.9% | 21.1% | −13.8pt（X比率下落） |
| ソーラービーム | 61.0% | 76.5% | +15.5pt |
| フレアドライブ | 33.3% | 20.8% | −12.5pt |
| りゅうのまい | 26.9% | 15.1% | −11.8pt |
| ニトロチャージ | 28.9% | 26.0% | −2.9pt |

Y比率の上昇（+13.9pt）とX比率の低下（−13.8pt）がほぼ鏡写しで、M-3でX型からY型への移行が起きていることが読み取れます。フレアドライブとりゅうのまい（X型の主軸技）の減少が、Xの使用率低下と一致します。

使用率が全体で下落した背景には、M-3環境でメガライチュウY（5位）やアシレーヌ（同居率6位）といったリザードンに対して有利または等倍以上の打点を持つポケモンが上位に増えたことが挙げられます。Y比率の上昇はX型の苦手な環境対処として特殊型（ひでり補正・ソーラービーム即撃ち）へのシフトを示しており、X型を使う前提だったじめん等への裏対応をY型に任せる動きとも解釈できます。

技採用率面では、Y型でのソーラービーム76.5%（M-2: 61.0%）とオーバーヒート30.9%（M-2: 26.6%）の上昇が目立ちます。オーバーヒートはC2段階ダウンのデメリットはあるものの、晴れ補正込みで最大瞬間火力を出せる選択肢として評価が高まっています。ウェザーボール24.8%も晴れ下でほのお100（タイプ一致+ひでりで実質威力225）となり、かえんほうしゃ（実質202）を上回る火力を出せます。「かえんほうしゃ・オーバーヒート・ウェザーボール・ソーラービーム」の4択から3枠を選ぶ構成が生まれ、4枠目の選択肢が多様化しています。

---

**総評:**

リザードンはメガY型（77.5%）を主体に、ひでり+ソーラービームで特殊2タイプを1ターン補完する特殊アタッカーとして環境に存在します。M-2から使用率は下落しましたが、Y比率がさらに高まっており、プレイヤーがY型の汎用性を評価していることが数字に表れています。苦手とする相手（メガライチュウY・アシレーヌ）への対処はパートナーに依存するため、同居率1位ガブリアス・4位ブリジュラスでいわ/でんき弱点をカバーする構成が主流です。

---

## 関連記事

- [使用率2位 ミミッキュのM-3考察](/blog/mimikyu-analysis-m3/)
- [使用率3位 メガライチュウYのM-3考察](/blog/raichu-y-analysis-m3/)
- [使用率6位 メガムクホークのM-3考察](/blog/staraptor-analysis-m3/)
