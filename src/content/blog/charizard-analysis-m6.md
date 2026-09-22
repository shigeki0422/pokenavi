---
title: '【ポケモンチャンピオンズ】リザードン 考察 M-6 シーズン メガY/メガXの型選択'
description: 'M-6シーズン使用率17位のリザードン考察。メガリザードンYのリザードナイトY採用率72.8%・メガリザードンXのリザードナイトX25.8%のデータから、ひでりソーラービーム型とりゅうのまい物理型の違い、弱点タイプの変化と苦手/得意な相手をデータで解説します。'
pubDate: '2026-09-22'
updatedDate: '2026-09-22'
heroImage: '../../assets/hero-charizard-m6.png'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" />
  <div>
    <h2 style="margin:0 0 8px">リザードン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">17位</strong>　持ち物: <strong>リザードナイトY 72.8% / リザードナイトX 25.8%</strong>
    </div>
    <div style="font-size:0.78rem;color:#999;margin-top:4px">データ集計日：2026-09-17</div>
  </div>
</div>

※本記事の使用率順位・技/性格/持ち物などの詳細データは2026-09-17時点のクロールを使用しています。

M-6シーズン、リザードンは使用率17位です（M-5は11位）。メガリザードンY（リザードナイトY・採用率72.8%）はほのお/ひこうのまま特殊アタッカーに、メガリザードンX（リザードナイトX・採用率25.8%）はほのお/ドラゴンに変化して物理アタッカーになり、どちらのメガ石かでタイプ・弱点・技構成が丸ごと変わります。

---

## リザードンの基本スペック

### 種族値（通常→メガ後）

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:4px 0;font-size:0.8em;color:#666;border-bottom:2px solid #e2e8f0;margin-bottom:4px">
    <span style="width:72px;min-width:72px"></span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right">通常</span>
    <span style="width:40px;text-align:right">メガY</span>
    <span style="width:40px;text-align:right">メガX</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span><span style="width:40px;text-align:right">78</span><span style="width:40px;text-align:right">78</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">84</span><span style="width:40px;text-align:right;color:#059669">104</span><span style="width:40px;text-align:right;font-weight:700;color:#dc2626">130</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:39%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">78</span><span style="width:40px;text-align:right">78</span><span style="width:40px;text-align:right;font-weight:700;color:#dc2626">111</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">109</span><span style="width:40px;text-align:right;font-weight:700;color:#dc2626">159</span><span style="width:40px;text-align:right">130</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span><span style="width:40px;text-align:right;color:#059669">115</span><span style="width:40px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">100</span><span style="width:40px;text-align:right">100</span><span style="width:40px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">534</span><span style="width:40px;text-align:right;white-space:nowrap">634</span><span style="width:40px;text-align:right;white-space:nowrap">634</span>
  </div>
</div>

メガリザードンYは特攻159・特防115と特殊方面が伸び特性は**ひでり**（5ターン天候をにほんばれにする）、メガリザードンXは攻撃130・防御111と物理方面が伸び特性は**かたいツメ**（接触技威力×1.3）です。すばやさはどちらも通常時と同じ100です。

### タイプ・弱点

メガ進化前とメガYはほのお/ひこう、メガXはほのお/ドラゴンで、弱点構成が大きく異なるため分けて示します。

<div class="type-row">
  <strong>タイプ（通常・メガY）：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
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
    <img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん
  </td>
</tr>
</tbody>
</table>
</div>

いわ×4が最大の弱点です。M-6使用率16位のキラフロル（いわ/どく）はパワージェム（いわ）採用率81.4%と高く大ダメージを受けます。じめんは無効なので、じしんを主力にするガブリアス等の攻撃は通りません。

<div class="type-row">
  <strong>タイプ（メガX）：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ドラゴン</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">でんき</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:6px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

メガXはひこうタイプでなくなるため、じめん技が無効から×2弱点に転じる一方、でんき技には耐性（×0.5）を新たに得ます。例えばパーモット（26位）のでんこうそうげき（でんき93.4%）はメガXには半減、メガYには×2。ギャラドス（14位）のたきのぼり（みず）もメガXには等倍、メガYには×2と、メガ石で通る攻撃が入れ替わります。

### 特性

通常時は**もうか（88.0%）**（HP1/3以下でほのお技威力1.5倍）が主流で、控えは**サンパワー（12.0%）**（にほんばれ下で特攻1.5倍、毎ターン最大HPの1/8減少）です。メガ進化後はメガYがひでり、メガXがかたいツメに固定で上書きされます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ソーラービーム</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">71.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガY専用の主力技。ひでりで溜めなしで即撃て、ガブリアス・カバルドン等じめん複合に等倍以上で通ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">50.8%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一致安定打点。10%でやけど付与、反動なし</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">39.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一致技。30%でひるみを狙えます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのはどう</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">27.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの特殊ドラゴン技。ガブリアス・ボーマンダ等ドラゴン複合に×2で通ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>はねやすめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">26.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの回復技。最大HPの1/2を回復します</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フレアドライブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">24.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの一致最大打点。かたいツメで威力1.3倍、被ダメージ1/3の反動あり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ニトロチャージ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの技。反動なしで自分のSを1段階上昇</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウェザーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50→100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYのひでり下ではタイプがほのおに変わり威力2倍の100になる、かえんほうしゃと役割が重なるサブ打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一撃重視の選択技。使用後は自分のCが2段階downし連発不可</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの積み技。自分のA・Sを1段階上昇させフレアドライブを強化</td>
</tr>
</tbody>
</table>
</div>

以前主力候補だったげきりんは9月10日時点の21.6%から20%を割り込み、もともと20%未満だったかみなりパンチとともに上位10技から外れました（詳細はデータ分析③）。

---

## M-6の採用型

### 型1：メガY 特殊アタッカー型（ひかえめ 48.4% / おくびょう 23.2%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガY 特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（88.0%）→メガ後ひでり<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）またはおくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布・30.1%）<br>
<strong>持ち物:</strong> リザードナイトY（72.8%）
</div>
<div>
<strong>技構成:</strong><br>
・ソーラービーム<br>
・かえんほうしゃ<br>
・エアスラッシュ<br>
・りゅうのはどう
</div>
</div>
</div>

特性ひでりで天候をにほんばれにし、本来2ターン技のソーラービームを1ターンで撃つのが型の骨子です。くさ技のため、ガブリアス（じめん/ドラゴン、ほのお×0.5）にもソーラービームなら等倍以上で通ります。第4枠は特殊ドラゴン技のりゅうのはどう（27.9%）が最多で、オーバーヒート（18.4%）・ウェザーボール（19.0%）を上回り、ドラゴン複合への打点を優先する構成が主流です。

**性格差：CとSのどちらを取るか**

ひかえめはH155 / A111 / B98 / C232 / D135 / S152、おくびょうはH155 / A111 / B98 / C211 / D135 / S167です。ひかえめは特攻を伸ばして削り量を優先、おくびょうは素早さを伸ばしてスカーフ非採用の相手を上から取る型です。例えばM-6使用率27位のメタグロスはメガ後、最多性格いじっぱり（58.4%）でS162になるため、おくびょうS167なら先手を取れますが、ひかえめS152では後手になります。パーティ内の役割分担次第で選びます。

---

### 型2：メガX 物理アタッカー型（いじっぱり 16.4% / ようき 9.3%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガX 物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（88.0%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（メガX最多EV分布・13.4%）<br>
<strong>持ち物:</strong> リザードナイトX（25.8%）
</div>
<div>
<strong>技構成:</strong><br>
・はねやすめ<br>
・フレアドライブ<br>
・ニトロチャージ<br>
・りゅうのまい
</div>
</div>
</div>

はねやすめで耐久を補いながらりゅうのまいで積み、フレアドライブを連打する運用が主流です。以前主力だったげきりんは20%を割り込み、もともと20%未満だったかみなりパンチとともに上位10技から外れており、専用打点よりほのお一致技中心の構成になっています。

**性格差：Sの違いが決めるメタグロスとの先手争い**

いじっぱりはH155 / A200 / B131 / C135 / D105 / S152、ようきはH155 / A182 / B131 / C135 / D105 / S167です。M-6使用率27位のメタグロスはメガ後、最多性格いじっぱり（58.4%）でS162、2番手ようき（28.5%）でS178になり、リザードンいじっぱり（S152）はどちらにも後手ですが、ようき（S167）なら多数派のいじっぱりメタグロスには先手を取れます。先手を優先するか、A200の削り性能を優先するかはパーティの役割分担次第です。

---

## データ分析①：メガY・メガXの技カバレッジ比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">環境上位ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガYの主力技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガXの主力技</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ガブリアス（じめん/ドラゴン）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">りゅうのはどう（ドラゴン）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×0.5</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">カバルドン（じめん）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ソーラービーム（くさ）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ギャラドス（みず/ひこう）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ソーラービーム（くさ）×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×0.5</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">メタグロス（はがね/エスパー）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:28px;height:28px;vertical-align:middle;margin-right:6px">ブリジュラス（はがね/ドラゴン）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
</tbody>
</table>
</div>

表の技は採用率20%以上の技の中から最大打点を選んでいます（ギャラドス欄は威力120のソーラービームがりゅうのはどうより上）。メガYは一致技に加えくさ・ドラゴンの補助打点を持ち、ガブリアスにはりゅうのはどう×2、カバルドンにはソーラービーム×2と相手ごとに刺さる技を選べます。一方メガXの採用率20%以上の攻撃技はフレアドライブ・ニトロチャージのほのお2技のみで、ガブリアス・ギャラドスには半減（×0.5）で通りにくく、メタグロスのようなはがね複合には×2で刺さるという、相手依存の構成です。

---

## データ分析②：メガストーン採用率とEV配分

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガY</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">メガX</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">対応する性格合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ひかえめ+おくびょう 71.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">いじっぱり+ようき 25.7%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多EV分布</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-C32-S32（30.1%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-A32-S32（13.4%）</td>
</tr>
</tbody>
</table>
</div>

メガ石採用率（72.8% / 25.8%）と性格採用率の合計（71.6% / 25.7%）はほぼ一致しており、性格分布がそのままメガY/Xの採用比率を反映しています。

---

## データ分析③：M-5からの変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-5</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">M-6</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードナイトY採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">72.8%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードナイトX採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.8%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">48.4%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.4%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9.3%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ソーラービーム採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">71.1%</td>
</tr>
</tbody>
</table>
</div>

M-5からM-6にかけて使用率は11位から17位に下がった一方、メガYの採用比率は約6対4から約7対3へさらに偏りました。ひかえめ採用率（35.0%→48.4%）・ソーラービーム採用率（60.6%→71.1%）がともに伸び、メガYはH2-C32-S32＋ソーラービームへの収束が進んでいます。技構成でも、メガXの主力候補だったげきりんは9月10日時点の21.6%から17日時点で20%を割り込み、もともと20%未満だったかみなりパンチとともに上位10技から外れました。代わりにりゅうのはどう（27.9%）・はねやすめ（26.9%）が新たに上位入りし、メガXはドラゴン・でんきの専用打点よりはねやすめによる耐久を優先する構成にシフトしています。

---

## 苦手なポケモン

環境上位の相手（使用率TOP30の一部、判定が確定したものに限る）について、メガX（ようき個体・S167）・メガY（最多性格ひかえめ・S152）それぞれの多数派技同士の1v1判定を対戦エンジンで一括計算しました。いじっぱり個体（型カード主軸、S152）や相手の性格次第で先手/後手が変わる例（ウルガモス・ミミッキュ）があり、詳細は後述します。

全代表型で勝敗が一致した相手のみ掲載し、相手の代表型で勝敗が割れるカバルドン・マスカーニャ・カイリュー、両フォームで勝敗が割れるアシレーヌ・ゲッコウガ・カメックス・ブリジュラス・メタグロス・ラウドボーン・ウォッシュロトム・イダイトウ(オス)・ギャラドスは除外しています。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガX</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガY</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）4発・後手。相手のりゅうせいぐん（26.6%）1発で先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうのはどう（27.9%）2発・後手。相手のすてみタックル（76.2%）1発で先に落とされる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）3発・後手。相手のりゅうせいぐん（30.3%）1発で先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうのはどう（27.9%）2発・後手。相手のりゅうせいぐん（30.3%）も2発だが先に動かれるため先に落とされる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手だが押し切れず、相手のきょけんとつげき（77.8%）1発で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）2発。多数派（セグレイブナイト47.9%）は先手を取っても、相手のきょけんとつげき（77.8%）1発で落とされる（ようき個体〈23.4%〉はS152で同速のため、後手になれば2発受けてから落とされる）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）3発・先手だが押し切れず、相手のパワージェム（81.4%）1発で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ソーラービーム（71.1%）2発・先手だが押し切れず、相手のパワージェム（81.4%）1発で落とされる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・後手。相手のとびひざげり（88.9%）も2発だが先に動かれるため先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（39.7%）2発・後手。相手のダストシュート（80.7%）も2発だが先に動かれるため先に落とされる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・後手。相手のインファイト（58.8%）も2発だが先に動かれるため先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）2発・後手。相手のでんこうそうげき（93.4%）1発で先に落とされる</td>
</tr>
</tbody>
</table>
</div>

14位ギャラドス（みず/ひこう）は両フォームで勝敗が割れる代表例で、メガXはじしん（44.8%）で押し切られますが、メガYはソーラービーム（71.1%）が等倍で通り先手を取れます。

メガX・メガYとも表の6匹全てに敗れており、メガXは多数派技がほのお2技に限られたことで打点の幅が狭い点が響いています。またガブリアス・ボーマンダの決定打（りゅうせいぐん）は両者の最多採用技ではなく、最多技はそれぞれじしん（66.7%）・すてみタックル（76.2%）で、こちらへの耐性も別途要注意です。

使用率30位のカイリューはメガYで相手の代表型（カイリュナイトの有無）により勝敗が入れ替わるため除外していますが、最多採用技かえんほうしゃ（62.6%）は決着に関わるりゅうせいぐん（50.1%）より採用率が高い点は押さえておく必要があります。

同居率上位のアシレーヌ・ミミッキュはドラゴン技（りゅうせいぐん・げきりん）を無効化できます。ただしガブリアスの最多技じしん（じめん）はアシレーヌ・ミミッキュどちらにも等倍で通るため根本対策にはなりません。ボーマンダの最多技すてみタックル（ノーマル）は、メガボーマンダの特性スカイスキンでひこうタイプに変化するため、アシレーヌ・ミミッキュどちらにも等倍で通り、パートナーで肩代わりできません。同様に、キラフロル（16位）のパワージェム（いわ81.4%）はルカリオでいわ×0.25に抑えられますが、キラフロルの第3技だいちのちから（じめん61.3%）はルカリオに×2で通り、パーモット（26位）のでんこうそうげき（でんき93.4%）はガブリアス・カバルドンで無効化できても第3技れいとうパンチ（こおり65.6%）がガブリアスに×4・カバルドンに×2で通るため、いずれも安定した処理役にはなりません。

---

## 得意なポケモン

同じ手順で、メガX・メガYどちらの型でも優位に立てる相手を抽出しました。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">使用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガX</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">メガY</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・先手。相手のドリルライナー（29.4%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発。相手のふいうち（58.0%、優先度+1で先に飛ぶ）は2発分耐えるため、こちらが1発で返せます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・後手。相手のはどうだん（75.7%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・後手。相手のてっていこうせん（20.0%）は3発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・先手。相手のシャドーボール（99.0%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・先手。相手の10まんボルト（31.1%）は2発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手。相手の10まんばりき（51.6%）は2発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・先手。相手のはたきおとす（67.5%）は3発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手。相手のじゃれつく（96.8%）は2発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）2発・先手。相手のシャドークロー（64.9%）は2発分（互角）</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・先手。相手のポルターガイスト（52.7%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・先手。相手のポルターガイスト（52.7%）は1発分（互角）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手。相手のブレイブバード（30.5%）は3発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・先手。相手のブレイブバード（30.5%）は3発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・後手。相手のインファイト（98.4%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・後手。相手のフェイタルクロー（96.2%）は2発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手（多数派グランドコート型S147基準）。相手のワイドフォース（99.5%）は2発分（互角）。こだわりスカーフ個体（採用率24.7%、S241）には後手を取られ2発同士で先に落とされます</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）2発・先手（多数派グランドコート型S147基準）。相手のワイドフォース（99.5%）は2発分（互角）。こだわりスカーフ個体（採用率24.7%、S241）には後手を取られ2発同士で先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）1発・後手。相手のふぶき（61.2%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（50.8%）1発・後手。相手のふぶき（61.2%）は3発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（24.6%）2発・先手。相手のむしのさざめき（30.7%）は5発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（39.7%）2発・先手。相手のほのおのまい（80.0%）は4発分耐える</td>
</tr>
</tbody>
</table>
</div>

11体とも一致技（メガXはフレアドライブ、メガYはかえんほうしゃ・エアスラッシュが基本）が相手の主力技より先に、または互角以上のペースで通る相手です。ただし2体は前提が崩れます。ウルガモスはS32振り個体（合計約19.8%）のうち、ひかえめならS152でいじっぱり・メガYひかえめ（ともにS152）と同速になり先手前提が崩れ、おくびょうならS167でさらに上から抜かれます（最多分布のH32-B32-S2型はS122のため、この個体には先手を維持できます）。

ミミッキュはようき個体（15.7%、S162）に対して、メガYひかえめ（S152）・メガXいじっぱり（S152）ともに後手になります（おくびょうS167なら先手を維持）。それでもかえんほうしゃ2発・フレアドライブ2発でミミッキュを先に倒せる（相手のシャドークロー・じゃれつくは3発以上必要）ため、後手でも押し切って勝ちを維持できます。

---

## 同居率上位の分析

M-6でリザードンと同じパーティに入る頻度が高いポケモン（同居率上位10体）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（1位）・**カバルドン**（4位）はともにでんき技無効化・いわ技半減（×0.5）で、メガYのでんき×2弱点と共通のいわ弱点を代わりに受けられます。

**アシレーヌ**（2位）はみず技半減・ドラゴン技無効化で、メガYのみず×2弱点・メガXのドラゴン×2弱点をカバーします。

**ミミッキュ**（3位）はドラゴン技無効化でメガXのドラゴン×2弱点をカバーする一方、リザードンは両フォームともはがね技を半減で受けられ、ミミッキュのはがね弱点を逆に補う関係です。

**セグレイブ**（5位）はみず・でんき技を半減でき、メガYのみず・でんき×2弱点を肩代わりできますが、いわ・ドラゴン技には自身も×2弱点を持ちメガXのいわ・ドラゴン×2弱点とは重複するため対策になりません。

---

## まとめ

M-6のリザードンは使用率17位につけつつ、メガリザードンY（メガ石リザードナイトY・72.8%）とメガリザードンX（メガ石リザードナイトX・25.8%）という2つの全く異なる型が約7対3の比率で併存するシーズンです。

- **メガXはひこう解除でじめん・ドラゴンが新たな弱点になる一方、いわ弱点はメガYの×4から×2に緩和されます**：メガ石で弱点タイプが入れ替わります
- **メガYはくさ技ソーラービームとドラゴン技りゅうのはどうでじめん・ドラゴン複合にも打点を持ち、メガXより技の幅が広い**構成です
- **性格採用率（ひかえめ+おくびょう71.6% / いじっぱり+ようき25.7%）がメガ石採用率とほぼ一致**しています
- **げきりん・かみなりパンチが圏外となり、メガXの攻撃技は実質フレアドライブ・ニトロチャージ（ともにほのお）のみに集約**：ガブリアス・ボーマンダ・セグレイブ・キラフロル・エースバーン・パーモットには両フォームとも苦戦する一方、一致技（メガXはフレアドライブ、メガYはかえんほうしゃ・エアスラッシュが基本）が通る相手（表の11体）には両フォームとも優位を取れます

いわ×4（メガY）／じめん・いわ・ドラゴン×2（メガX）という弱点構成の違いを踏まえ、他のポケモンでどちらの弱点を埋めるかが型選択とセットで問われます。

---

*関連記事：[ガブリアス考察 M-6](/blog/garchomp-analysis-m6/)*
