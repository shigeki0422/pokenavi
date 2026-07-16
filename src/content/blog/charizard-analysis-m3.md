---
title: 'リザードン考察 M-3 メガY型とX型の採用率と立ち回り'
description: 'チャンピオンズM-3使用率7位リザードンを解説。メガY（リザードナイトY 75.9%）とメガX（22.6%）の型別採用率・種族値・技構成・立ち回りを解説。ひでり+ソーラービーム79.0%採用の構造から読み取れる運用思想も考察。'
updatedDate: '2026-07-02'
pubDate: '2026-07-02'
heroImage: '../../assets/hero-charizard-m3.png'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン（M-3）" />
  <div>
    <h2 style="margin:0 0 8px">リザードン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">7位</strong>（M-2は5位）　持ち物: <strong>リザードナイトY 75.9% / リザードナイトX 22.6%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-3シーズン時点の集計です

M-3のリザードンはリザードナイトY採用率75.9%を中心に、メガリザードンY（ほのお/ひこう）として運用されるケースが多数派です。特性**ひでり**（メガ進化後）でほのお技を1.5倍に強化しつつ、ソーラービームを溜めなしで使えるようにすることで、1ターンで2タイプの攻撃を打ち分ける火力型として機能します。M-2では5位だった使用率が7位に下落しており、環境変化との関係を含めて分析します。

---

## なぜメガリザードンが採用されるのか

### Y型（75.9%）: ひでり+ソーラービームで2タイプ制圧

メガリザードンYは場に出た瞬間に特性ひでりで晴れ状態にします。晴れにより**ほのお技は1.5倍**、**ソーラービームは溜めターンなしで即撃ち**できます。C実数値232（ひかえめ H2 C32 S32）のかえんほうしゃは晴れ補正込みで実質威力202相当となり、ソーラービームの実質威力180（STAB、補正なし）を上回ります。ひでりという1つの特性が「ほのお技強化」と「ソーラービーム即撃ち」の2役を担うため、持ち技2枠でほのお・くさの2タイプをフルパワーで使い分けられます。

ソーラービーム採用率79.0%とかえんほうしゃ採用率46.3%が並立しているのは、この構造の反映です。ソーラービームはみず/じめん複合（×4）やみず単体（×2）など、ほのお技が半減以下になる相手への補完として機能し、かえんほうしゃはひでり補正込みで汎用打点になります。

### X型（22.6%）: かたいツメ+積み技で物理制圧

メガリザードンX（ほのお/ドラゴン）はメガ後特性かたいツメにより接触技の威力が1.3倍になる物理型です。A実数値200（いじっぱり H2 A32 S32）でフレアドライブ（20.8%）・ニトロチャージ（26.0%）を主軸とし、りゅうのまい（15.1%）やニトロチャージでA・Sを積んで制圧します。Y型のように晴れ状態に依存せず、かたいツメ補正は天候に左右されない点が差別化点です。積み切れればA・Sが上昇した状態で物理打点を通し続けられます。

Y型との採用率差（75.9% vs 22.6%）の背景は「ひでり+ソーラービームの汎用性がX型のりゅうのまい制圧より構築に組み込みやすい」点にあります。X型は積みターンを確保できないと機能しにくく、高速アタッカーが多い環境ではY型の即時性が優位に働きます。

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
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">104</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+20</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+46</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right">78</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">111</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+33</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">159</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+50</span>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+21</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:80px;min-width:80px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">115</strong></span><span style="width:40px;text-align:right;font-size:0.82em;font-weight:700;color:#059669">+30</span>
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
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">634</span><span style="width:40px"></span>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">634</span><span style="width:40px"></span>
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
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">79.0%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型中心（ひでりで溜めなし即撃ち）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">2</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>かえんほうしゃ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">90</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">46.3%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（ひでり補正込み実質202相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">3</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>エアスラッシュ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">75</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><strong style="color:#dc2626">44.2%</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（ひこう一致補正、かくとう等に通る）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">4</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>オーバーヒート</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">130</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">31.5%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（C2段階ダウン、ひでり補正込み実質292相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">5</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ニトロチャージ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">24.9%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（S+1。りゅうのまいと合わせて積み型）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">6</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>ウェザーボール</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">50（晴れ時100・ほのお）</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">24.6%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（晴れでほのお100、STAB+ひでりで実質225相当）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">7</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>フレアドライブ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">120</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">22.4%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（物理一致打点）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">8</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>はねやすめ</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">19.5%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">Y型（HP回復で場持ちを伸ばす）</td>
</tr>
<tr>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">9</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのはどう</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">85</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.6%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（特殊ドラゴン打点）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">10</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0"><strong>りゅうのまい</strong></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle"></td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">—</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0;text-align:center">15.6%</td>
  <td style="padding:6px 10px;border:1px solid #e2e8f0">X型（A+1 S+1。積み後に制圧）</td>
</tr>
</tbody>
</table>
</div>

Y型はソーラービーム・かえんほうしゃ・エアスラッシュの3枠がほぼ確定枠で、4枠目をオーバーヒート（C2段階ダウン覚悟の最大瞬間火力）・ウェザーボール（晴れでほのお実質威力225）・はねやすめ（回復）から選ぶ構成です。X型はフレアドライブ・ニトロチャージを軸に、りゅうのはどう（15.6%）またはりゅうのまい（15.6%）で打ち分ける構成が読み取れます。

---

## 主要型の解説

### 型1: メガリザードンY 特殊アタッカー型（最多採用）

**持ち物: リザードナイトY 75.9%　性格: ひかえめ 46.6%（最多）/ おくびょう 31.5%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガリザードンY 特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（84.1%）※メガ後ひでり<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）／おくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2 C32 S32（採用率37.7%・最多）<br>
<strong>持ち物:</strong> リザードナイトY（75.9%）
</div>
<div>
<strong>技構成:</strong><br>
・ソーラービーム（79.0%）<br>
・かえんほうしゃ（46.3%）<br>
・エアスラッシュ（44.2%）<br>
・<span style="color:#1d4ed8">オーバーヒート31.5% / ウェザーボール24.6% / はねやすめ19.5%</span>
</div>
</div>
</div>

**実数値（H2 C32 S32）:**
- ひかえめ: HP155 C232 S152
- おくびょう: HP155 C211 S167

**強み（ひかえめ vs おくびょう）:**

ひかえめ型はC232でかえんほうしゃの晴れ込み打点が高く、おくびょう型はC211に落ちる代わりにS167でより多くの相手に先手を取れます。S152（ひかえめ）とS167（おくびょう）の差は、S153〜167帯の相手への先手を確保できるかどうかに影響します。ガブリアス（最速S169）は両型とも後手になるため、S上限で両型の差は消えます。火力か速度かの選択で、多数派はひかえめ（46.6%）です。

**弱み:**

いわ技に×4弱点を持ちます。環境上のいわ技使用ポケモンに対しては選出を控えるか、ほのお技で先に倒す立ち回りが必要です。また、でんき×2弱点があるため、メガライチュウY（S実数値200・ノーガード）に対しては必ず後手となり、でんき技を受けて大ダメージを負います。

---

### 型2: メガリザードンX 物理積み型

**持ち物: リザードナイトX 22.6%　性格: いじっぱり 10.1%（最多）/ ようき 8.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガリザードンX 物理積み型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（84.1%）※メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）／ようき（S↑ C↓）<br>
<strong>EV:</strong> H2 A32 S32（採用率20.4%）<br>
<strong>持ち物:</strong> リザードナイトX（22.6%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ（22.4%）<br>
・ニトロチャージ（24.9%）<br>
・りゅうのはどう（15.6%）<br>
・<span style="color:#1d4ed8">りゅうのまい（15.6%）</span>
</div>
</div>
</div>

**実数値（H2 A32 S32）:**
- いじっぱり: HP155 A200 S152
- ようき: HP155 A182 S167

**強み（Y型との差）:**

X型はメガ後特性かたいツメが接触技の威力を1.3倍にするため、フレアドライブ（接触、威力120）の実質打点がY型のかえんほうしゃ（晴れ前提）と異なる条件で発揮されます。Y型は晴れを自分で用意しますが、X型はかたいツメ補正が特性依存で天候に左右されない点が差別点です。りゅうのまい+ニトロチャージで積み切れれば、A・Sともに上昇して物理制圧が狙えます。

**弱み（Y型との差）:**

Yと同じS100でよりSが確保しにくく、じめん×2弱点が増えます。ガブリアス（使用率1位）がじしんを採用する場合はX型にとって刺さる弱点であり、Y型のじめん無効に比べて選出リスクが高まります。積みに複数ターンを要するため、高速アタッカーが多い環境では積みターンを作れないケースがある点も使い勝手に影響します。

---

## 環境ポケモンへの相性分析

### Y型（ひかえめ HP155 C232 S152）基準

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこうタイプにより無効。ただしほのお・くさ・ひこう技はいずれも等倍以下で高火力の打点がない。スカーフ採用率23.5%（S約253）では先手を取れず、タスキ採用率37.7%では1発で落とせない。スカーフなし・タスキなしの型に対してもS152で後手となり、げきりんを受ける形になる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃがはがね/ドラゴンに等倍、かつ晴れ補正込みで打点が高い。ブリジュラス無補正S実数値137はS152より遅く先手が取れる。スカーフ未採用（オボンのみ29.8%・たべのこし29.4%が主体）。ただしブリジュラスのでんき技を被弾するとでんき×2弱点を突かれる点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃがはがね/エスパーに×2で抜群。メタグロスS70はS152より遅い。晴れ補正込みで高火力の先制打点が入る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガライチュウY（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガライチュウY採用率96.4%。メガ後S130・特性ノーガード（おくびょう実数値200）で必ず先手。でんきタイプのため晴れほのお技が通らず等倍以下。こちらのでんき×2弱点を突かれる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（同居率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 条件次第</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず/フェアリーへのかえんほうしゃは半減。ソーラービームはみず/フェアリーに×2抜群で打点はある。ただしアシレーヌのみず技がみず×2弱点を突くため、オボン採用率58.0%でソーラービーム1発では落とせない場合に反撃を受ける。S60（最速実数値123）で先手は取れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラグラージナイト採用率74.8%。メガ後はみず/じめんでソーラービームが×4で抜群。じしんはひこうタイプにより無効。メガ後S70（最速S134）でS152より遅く先手が取れる</td>
</tr>
</tbody>
</table>
</div>

### X型（いじっぱり HP155 A200 S152）基準

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">X型はじめん×2弱点があるため、ガブリアスのじしん（採用率上位）が直接刺さる。スカーフ採用率23.5%では後手になり先手じしんを受ける。タスキなしのガブリアスは積み前のX型に対してもじしんで大ダメージを与えられる。Y型のじめん無効と比較して対ガブリアスのリスクが大きく異なる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがはがね/ドラゴンに等倍、かつかたいツメ補正込みで打点が高い。ブリジュラス無補正S実数値137はS152より遅く先手が取れる。スカーフ未採用のため先手は安定。ただしでんき技を被弾した場合、X型のでんき×0.5耐性でダメージを半減できる点はY型より優れる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メタグロス（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがはがね/エスパーに×2で抜群。かたいツメ補正込みで高い物理打点が入る。メタグロスS70はS152より遅く先手が取れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガライチュウY（6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">X型もでんき×0.5耐性でY型より軽減できるが、メガ後S130（おくびょう実数値200）で先手を取られる状況は変わらない。でんき技の被ダメージはY型の半分程度になるものの、先手で動かれる点と物理型のA200では特殊技を持たず、でんきタイプへの打点がほのお技のみで等倍止まり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（同居率6位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 条件次第</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブがみず/フェアリーに半減（×0.5）。ソーラービームのような補完技を持ちにくいX型では打点が安定しない。みず技がほのお/ドラゴンに等倍で通るため、オボン採用率58.0%のアシレーヌへの突破は難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0260-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガラグラージ（環境上位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 条件次第</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ラグラージナイト採用率74.8%。メガ後はみず/じめんで、フレアドライブはみず半減（×0.5）。X型はY型のようなソーラービーム（×4）の補完打点がなく、じめん×2弱点によりメガラグラージのじしんが刺さる。積む前に対面すると返しのじしんで大ダメージを受ける</td>
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
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">苦手理由（Y型 / X型）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガライチュウY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Y型: でんき×2弱点を先手で突かれ、ほのお技は等倍以下で返せない。X型: でんき×0.5で被ダメは軽減されるが先手を取られる状況は同じ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラスやガブリアスなど、ライチュウに打点を持つパートナーで対処。直接対面は避ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Y型: かえんほうしゃ半減・ソーラービーム×2はあるがみず技でみず×2弱点を突き返される。X型: フレアドライブが半減でソーラービームの補完もなく打点が安定しない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね技がフェアリー複合に×2で通る）や同居率1位のガブリアスで処理。両型ともリザードン自身での突破は困難</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（X型固有）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">X型固有の問題: じめん×2弱点によりじしんが直接刺さる。Y型はじめん無効のため問題ない。X型選出時はガブリアスの選出動向に注意が必要</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">X型を使う構築では、ガブリアスへの打点を持つパートナー（みず技・こおり技）を用意するか、対ガブリアスはリザードン以外で対応する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（同居率8位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Y型固有の問題: すなおこしでひでり状態が上書きされると、ソーラービームが1ターン溜めに戻り、ほのお技の晴れ補正も消える。X型はひでりに依存しないため天候干渉の影響を受けない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">Y型は天候の打ち消し合いが発生する。カバルドンに先手で動かれないよう先発配置を工夫する</td>
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
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス">
    <div class="name">メタグロス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/エスパーでいわを半減し、リザードンが苦手な岩技持ちへ安定して受け出せる。はがね複合への処理ルートを共有できる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでリザードン弱点のでんき・いわを半減し、耐性補完の中核</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">選出を分散させる役割。リザードンが苦手な相手にアシレーヌで対応する選択肢を用意する</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン">
    <div class="name">カバルドン</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">天候展開が競合するため基本的に非同時選出。じめん打点でリザードンが苦手な相手を処理</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア">
    <div class="name">アーマーガア</div>
    <div class="rate">同居率8位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高耐久ではがね/ひこうの打点を持ち、物理全般の受け出しで盾になれる。ガブリアスのじしんをひこうで無効化する役割</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率9位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">あく/ドラゴンでエスパー・ゴースト複合に打点を持ち、リザードンが対処しにくい耐久型へのサイクル崩しを担う</div>
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

M-3でリザードンの使用率が5位から7位に下落した一方、メガY比率はM-2の63.6%からM-3で75.9%へ上昇しています。

| 項目 | M-2 | M-3 | 変化 |
|---|---|---|---|
| 使用率順位 | 5位 | 7位 | 下落 |
| リザードナイトY | 63.6% | 75.9% | +12.3pt（Y比率上昇） |
| リザードナイトX | 34.9% | 22.6% | −12.3pt（X比率下落） |
| ソーラービーム | 61.0% | 79.0% | +18.0pt |
| フレアドライブ | 33.3% | 22.4% | −10.9pt |
| りゅうのまい | 26.9% | 15.6% | −11.3pt |
| ニトロチャージ | 28.9% | 24.9% | −4.0pt |

Y比率の上昇（+12.3pt）とX比率の低下（−12.3pt）がほぼ鏡写しで、M-3でX型からY型への移行が起きていることが読み取れます。フレアドライブとりゅうのまい（X型の主軸技）の減少が、Xの使用率低下と一致します。

使用率が全体で下落した背景には、M-3環境でメガライチュウY（6位）やアシレーヌ（同居率6位）といったリザードンに対して有利または等倍以上の打点を持つポケモンが上位に増えたことが挙げられます。Y比率の上昇はX型の苦手な環境対処として特殊型（ひでり補正・ソーラービーム即撃ち）へのシフトを示しており、X型を使う前提だったじめん等への裏対応をY型に任せる動きとも解釈できます。

技採用率面では、Y型でのソーラービーム79.0%（M-2: 61.0%）とオーバーヒート31.5%（M-2: 26.6%）の上昇が目立ちます。オーバーヒートはC2段階ダウンのデメリットはあるものの、晴れ補正込みで最大瞬間火力を出せる選択肢として評価が高まっています。ウェザーボール24.6%も晴れ下でほのお100（タイプ一致+ひでりで実質威力225）となり、かえんほうしゃ（実質202）を上回る火力を出せます。「かえんほうしゃ・オーバーヒート・ウェザーボール・ソーラービーム」の4択から3枠を選ぶ構成が生まれ、4枠目の選択肢が多様化しています。

---

**総評:**

リザードンはメガY型（75.9%）を主体に、ひでり+ソーラービームで特殊2タイプを1ターン補完する特殊アタッカーとして環境に存在します。M-2から使用率は下落しましたが、Y比率がさらに高まっており、プレイヤーがY型の汎用性を評価していることが数字に表れています。苦手とする相手（メガライチュウY・アシレーヌ）への対処はパートナーに依存するため、同居率1位ガブリアス・4位メタグロス・5位ブリジュラスでいわ/でんき弱点をカバーする構成が主流です。

---

## 関連記事

- [使用率2位 ミミッキュのM-3考察](/blog/mimikyu-analysis-m3/)
- [使用率3位 メガライチュウYのM-3考察](/blog/raichu-y-analysis-m3/)
- [使用率6位 メガムクホークのM-3考察](/blog/staraptor-analysis-m3/)
