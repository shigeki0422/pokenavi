---
title: '【ポケモンチャンピオンズ】リザードン 考察 M-6 シーズン メガY/メガXの型選択'
description: 'M-6シーズン使用率18位のリザードン考察。メガリザードンYのリザードナイトY採用率60.6%・メガリザードンXのリザードナイトX37.6%のデータから、ひでりソーラービーム型とりゅうのまい物理型の違い、弱点タイプの変化と苦手/得意な相手をデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-charizard-m6.png'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" />
  <div>
    <h2 style="margin:0 0 8px">リザードン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">18位</strong>　持ち物: <strong>リザードナイトY 60.6% / リザードナイトX 37.6%</strong>
    </div>
    <div style="font-size:0.78rem;color:#999;margin-top:4px">データ集計日：2026-09-10</div>
  </div>
</div>

M-6シーズン、リザードンは使用率18位につけています（M-5は11位）。メガ進化することで2つの全く異なるポケモンに変わる特殊なポケモンで、メガリザードンY（メガ石リザードナイトY・採用率60.6%）はほのお/ひこうのまま特殊アタッカーになり、メガリザードンX（メガ石リザードナイトX・採用率37.6%）はほのお/ドラゴンに変化して物理アタッカーになります。どちらのメガ石を選ぶかでタイプ・弱点・技構成が丸ごと変わるため、対戦相手としても味方としても「どちらのメガ石か」の見極めが重要になります。

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

メガリザードンYは特攻159・特防115と特殊方面が伸び、特性が**ひでり**（登場時から5ターン天候をにほんばれにする）に変わります。メガリザードンXは攻撃130・防御111と物理方面が伸び、特性は**かたいツメ**（接触技威力×1.3）です。すばやさはどちらも通常時と同じ100で変化しません。

### タイプ・弱点

メガ進化前とメガYはほのお/ひこう、メガXはほのお/ドラゴンとタイプが変わります。弱点構成が大きく異なるため、それぞれ分けて示します。

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

いわ×4が最大の弱点です。M-6使用率16位のキラフロル（いわ/どく）はパワージェム（いわ）採用率80.8%と高く、控えにいる間・戦っている間ともに大ダメージを受けます。じめんは無効なので、じしんを主力にするガブリアス・カバルドン等の攻撃は通りません。

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

メガXはひこうタイプでなくなるため、じめん技が無効から等倍（×2弱点）に転じます。一方ででんき技への耐性（×0.5）を新たに得るため、環境28位のパーモットが放つでんこうそうげき（でんき・採用率85.1%）はメガXには半減で通ります（メガYはひこう複合のため×2弱点で通ります）。ただしみずタイプは等倍のまま耐性化はしないため、ギャラドス（15位）のたきのぼりはメガXにも等倍で通ります。どちらのメガ石を選ぶかで通る攻撃・通らない攻撃が入れ替わる点が、このポケモンの最大の特徴です。

### 特性

通常時は**もうか（92.1%）**が主流で、HPが1/3以下になるとほのお技の威力が1.5倍になります。控えは**サンパワー（7.9%）**で、にほんばれ下で特攻1.5倍になる代わり毎ターン最大HPの1/8を失います。ただしメガ進化するとメガYはひでりに、メガXはかたいツメに特性が固定で上書きされるため、通常時の特性はメガ進化前の場に出ているターンにのみ意味を持ちます。もうか・サンパワーいずれの場合も、メガ進化後は特性が入れ替わる点に注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">60.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガY専用の主力技です。ひでりでにほんばれにすれば溜めなしで即撃てます。ガブリアス・カバルドン等じめん複合には等倍以上で通ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かえんほうしゃ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">42.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一致安定打点です。10%でやけどを付与でき、反動なしで運用しやすい技です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>エアスラッシュ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">40.1%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一致技です。30%でひるみを狙えます。かくとう技持ちへの反撃手段にもなります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フレアドライブ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">36.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの一致最大打点です。かたいツメで威力1.3倍になりますが、被ダメージ1/3の反動があります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ニトロチャージ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの技です。反動なしで火力を出しつつ自分のSを1段階上昇できます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>オーバーヒート</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">130</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYの一撃重視の選択技です。使用後は自分のCが2段階downします。連発できないため撃ち切り用です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>げきりん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの一致最大打点候補です。使用後は自分が「あばれ」状態になり技が固定されますが、ガブリアス・ボーマンダ等ドラゴン複合には×2で通ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>かみなりパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXのサブ打点です。みず/ひこう複合のギャラドスには×4で通りますが、ガブリアス等じめん複合には無効です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ウェザーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">50→100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガYのひでり下ではタイプがほのおに変わり威力2倍の100になります。かえんほうしゃと役割が重なるサブ打点です</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>りゅうのまい</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガXの積み技です。自分のA・Sを1段階上昇させ、フレアドライブ・げきりんの威力と行動速度を伸ばします</td>
</tr>
</tbody>
</table>
</div>

---

## M-6の採用型

### 型1：メガY 特殊アタッカー型（ひかえめ 40.1% / おくびょう 20.0%）

**性格採用率: ひかえめ 40.1% / おくびょう 20.0%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガY 特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（92.1%）→メガ後ひでり<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）またはおくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布・21.5%）<br>
<strong>持ち物:</strong> リザードナイトY（60.6%）
</div>
<div>
<strong>技構成:</strong><br>
・ソーラービーム<br>
・かえんほうしゃ<br>
・エアスラッシュ<br>
・オーバーヒート
</div>
</div>
</div>

メガYの特性ひでりで自ら天候をにほんばれにすることで、本来2ターン技のソーラービーム（くさ・威力120）を1ターンで撃てるようにするのが型の骨子です。ソーラービームはくさタイプのため、じめん技を主力にするガブリアス（1位）やカバルドン（5位）に等倍以上で通る貴重な打点になります。かえんほうしゃ（ほのお・威力90）は一致技として安定打点になり、エアスラッシュ（ひこう・威力75）はひるみ30%を狙えます。オーバーヒート（ほのお・威力130、使用後特攻2段階down）は一撃の火力に用いる選択技です。

**性格差：CとSのどちらを取るか**

ひかえめはH155 / A111 / B98 / C232 / D135 / S152、おくびょうはH155 / A111 / B98 / C211 / D135 / S167です（ひかえめはSを補正しないためS152が基礎値のまま、おくびょうはSを1.1倍する補正でS167まで伸びます）。ひかえめは特攻を伸ばして一撃の削り量を優先する型、おくびょうは素早さを伸ばしてスカーフ非採用の相手を上から取れる範囲を広げる型で、どちらを選ぶかはパーティ内の役割分担次第です。

---

### 型2：メガX 物理アタッカー型（いじっぱり 22.7% / ようき 14.4%）

**性格採用率: いじっぱり 22.7% / ようき 14.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガX 物理アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（92.1%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（メガX最多EV分布・19.6%）<br>
<strong>持ち物:</strong> リザードナイトX（37.6%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・ニトロチャージ<br>
・げきりん<br>
・かみなりパンチ
</div>
</div>
</div>

なお、後述の「苦手なポケモン」「得意なポケモン」の対戦検証はようき個体（S167）のビルドで実行しています。型カードが主軸に置くいじっぱり（採用率22.7%）とは前提の性格が異なるため、いじっぱり個体（S152）では素早さ関係が変わり結論が反転する場合がある点に注意してください。

フレアドライブ（ほのお・威力120、被ダメージ1/3の反動）が一致最大打点です。ニトロチャージ（ほのお・威力50、自分のS1段階上昇）は火力を出しながら素早さを補強できます。げきりん（ドラゴン・威力120、使用後は「あばれ」状態で技固定）はガブリアス・ボーマンダ等ドラゴン複合の相手に一致補正込みで×2で通る打点ですが、使用後は連続で同じ技しか出せなくなる制約があります。かみなりパンチ（でんき・威力75）はみず/ひこう複合のギャラドスに×4で刺さる一方、ガブリアス等じめん複合には無効です。

**性格差：Sの違いが決めるメタグロスとの先手争い**

いじっぱりはH155 / A200 / B131 / C135 / D105 / S152、ようきはH155 / A182 / B131 / C135 / D105 / S167です。M-6使用率30位のメタグロスはメガ進化後の最多EV分布（H2-A32-S32）・最多性格（いじっぱり58.4%）でS162になり、いじっぱりS152では上から動けませんがようきS167であれば上から動けます。A200のフレアドライブはA182より一撃の破壊力が高く、りゅうのまいで積んだ後の削り性能はいじっぱりの方が上回ります。メタグロスのような中速帯への先手を優先するかいじっぱりの削り性能を優先するかは、パーティ内の他の高速アタッカーとの役割分担で決まります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアス（じめん/ドラゴン）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ソーラービーム（くさ）×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">げきりん（ドラゴン）×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（じめん）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ソーラービーム（くさ）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（みず/ひこう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かみなりパンチ（でんき）×4</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタグロス（はがね/エスパー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね/ドラゴン）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
</tbody>
</table>
</div>

表の倍率は`get_type_effectiveness`で全件検算済みです。ソーラービーム（くさ）はガブリアスには等倍止まりですが、じめん単タイプのカバルドンには×2で通ります。メガXのかみなりパンチはみず/ひこう複合のギャラドスに×4で刺さる一方、じめん複合のガブリアスには無効になる、相手のタイプ次第で結果が正反対になる技です。ほのお一致技はギャラドス（みず/ひこう）には×0.5、ブリジュラス（はがね/ドラゴン）には×1と、こちらも相手のタイプ次第で通りが変わります。メガYはくさ技を持つことでメガXにはない地面複合への上積みがある一方、メガXはひこうタイプが外れることでいわ×4のような致命的な四倍弱点を持たないという、攻守で明確なトレードオフになっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">対応する性格合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ひかえめ+おくびょう 60.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">いじっぱり+ようき 37.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多EV分布</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-C32-S32（21.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-A32-S32（19.6%）</td>
</tr>
</tbody>
</table>
</div>

メガ石採用率（60.6% / 37.6%）と性格採用率の合計（60.1% / 37.1%）がほぼ一致しており、性格分布がそのままメガYとメガXの採用比率を反映していることがデータから裏付けられます。約6対4でメガYが優勢ですが、メガXも4割近い採用があるため、対戦相手として遭遇した場合はどちらの型かを見て弱点タイプが変わることを踏まえた立ち回りが必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードナイトY採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">61.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.6%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">リザードナイトX採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">37.6%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ひかえめ採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おくびょう採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.0%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22.7%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ようき採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14.4%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ソーラービーム採用率</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">60.1%</td>
</tr>
</tbody>
</table>
</div>

M-5からM-6にかけて使用率は11位から18位に下げましたが、メガY・メガXの採用比率（およそ6対4）とソーラービーム採用率（60%台）はほぼ変化していません。型そのものの構造は固定化されている一方、性格分布には変化が見られます。メガY側ではひかえめが35.0%→40.1%へ伸び、おくびょう（24.9%→20.0%）から乗り換える動きが見られます。これは「メタグロス等への削り量を優先する個体が増え、素早さで上から取る個体が減った」ことを示すデータです。メガX側は逆にようきが11.5%→14.4%へ伸び、いじっぱり（25.5%→22.7%）からの乗り換えが起きています。メガX全体の採用率自体はほぼ横ばい（37.2%→37.6%）のため、X内部では「打点重視」から「速度域拡大」へシフトする動きがあったと読めます。使用率順位の低下は、リザードン自体の型構成の変化ではなく、環境全体の相対的な位置づけの変化によるものと考えられます。

---

## 苦手なポケモン

環境上位の相手（検証対象セットに基づく。使用率TOP30全てを網羅しているわけではありません）について、メガX・メガYそれぞれ持ち物で母集団を絞った上で、多数派技同士の1v1判定をエンジン（`scripts/tests/dump_matchups_majority_item.ts`）で一括計算しました。このうちアシレーヌ・イダイトウ(メス)・メタグロス・ブリジュラスはメガX・メガYで勝敗自体が割れるため（フォーム依存）表から除外し、カバルドン・ギャラドス・キラフロル・ゲッコウガ・エースバーン・ウォッシュロトム・パーモット・セグレイブ・マスカーニャ・サザンドラは相手の代表型（持ち物・技構成）によって勝敗が割れるため判定不能として除外しました。両フォームかつ相手の代表型で結果が一致した相手のみ掲載しています。技名・採用率・確定数・先手後手はエンジン出力をそのまま転記しています。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（21.6%）1発・後手。相手のりゅうせいぐん（28.6%）1発で先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（40.1%）2発・後手。相手のがんせきふうじ（21.1%）2発で先に落とされる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（21.6%）1発・後手。相手のりゅうせいぐん（21.2%）1発で先に落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オーバーヒート（22.7%）2発・後手。相手のすてみタックル（73.4%）1発で先に落とされる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（21.6%）2発・先手だが押し切れず、相手のりゅうせいぐん（50.8%）1発で落とされる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">エアスラッシュ（40.1%）3発・後手。相手のりゅうせいぐん（50.8%）2発で先に落とされる</td>
</tr>
</tbody>
</table>
</div>

メガXはいずれも相手のりゅうせいぐん（ドラゴン技）で落とされ（カイリューには先手を取っても押し切れません）、メガYはがんせきふうじ（ガブリアス）・すてみタックル（ボーマンダ）・りゅうせいぐん（カイリュー）と、相手ごとに決め手が異なります。ドラゴン技（りゅうせいぐん）が3体に共通する主因のため、対策としてはドラゴン技を無効化できるアシレーヌ（みず/フェアリー、ドラゴン技0倍）・ミミッキュ（ゴースト/フェアリー、ドラゴン技0倍）を後出しに使い、これらの相手をリザードン自身で受けずに後続で処理する構築にするのが有効です（ガブリアスはドラゴン技を×2で受けてしまうため、後出し先には不向きです）。すてみタックル（ボーマンダ）・がんせきふうじ（ガブリアス、採用率21.1%で必ずしも主力ではない）はドラゴン技以外の個別対応が必要です。実際にリザードンとの同居率上位にはアシレーヌ・ミミッキュが名を連ねており、パーティ単位でこの弱点を補完する構築が主流になっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・先手。相手のドリルライナー（25.6%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・先手。相手のふいうち（49.3%）は2発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・後手。相手のはどうだん（75.1%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・後手。相手のあくのはどう（59.6%）は4発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・先手。相手のシャドーボール（99.9%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・先手。相手の10まんボルト（20.0%）は2発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・先手。相手のポルターガイスト（54.0%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・先手。相手のポルターガイスト（54.0%）は1発分（互角）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）2発・先手。相手の10まんばりき（50.3%）は2発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・先手。相手のはたきおとす（66.5%）は3発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）2発・先手。相手のじゃれつく（98.1%）は2発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）2発・先手。相手のシャドークロー（59.2%）は2発分（互角）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）2発・先手。相手のブレイブバード（37.6%）は3発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・先手。相手のブレイブバード（37.6%）は3発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）2発・先手。相手のむしのさざめき（35.4%）は5発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オーバーヒート（22.7%）1発・先手。相手のほのおのまい（70.6%）は4発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・後手。相手のふぶき（69.1%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・後手。相手のふぶき（69.1%）は3発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）1発・後手。相手のインファイト（99.4%）は2発分耐える</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）1発・後手。相手のフェイタルクロー（94.7%）は2発分耐える</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">げきりん（21.6%）3発・先手。相手のシャドーボール（52.9%）は3発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">オーバーヒート（22.7%）2発・先手。相手のシャドーボール（52.9%）は4発分耐える</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フレアドライブ（36.5%）2発・先手。相手のワイドフォース（99.4%）は2発分（互角）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ（42.9%）2発・先手。相手のワイドフォース（99.4%）は3発分耐える</td>
</tr>
</tbody>
</table>
</div>

12体とも一致技（メガXはフレアドライブ、メガYはかえんほうしゃが基本、一部げきりん・オーバーヒート）が相手の主力技より先に、または互角以上のペースで通る相手です。イエッサン(オス)はTOP30圏外（35位）ですが、両フォームで結果が一致したため参考掲載しています。

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
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

**ガブリアス**（同居率1位）はじめん/ドラゴンで、でんき技を無効化、いわ技を半減（×0.5）で受けられます。メガYのでんき×2弱点、メガY・メガX共通のいわ弱点（メガYは×4、メガXは×2）を代わりに受けられる補完関係です。

**アシレーヌ**（同居率2位）はみず/フェアリーで、みず技を半減（×0.5）、ドラゴン技を無効化できます。メガYのみず×2弱点、メガXのドラゴン×2弱点をそれぞれカバーできる組み合わせです。

**ブリジュラス**（同居率3位）ははがね/ドラゴンで、くさ技を耐性（×0.25）、ノーマル・みず・でんき・むし・いわ・ひこう技を半減（×0.5）で受けられます。リザードンの弱点であるいわ（メガYで×4）・じめん・ドラゴン（メガX）とは異なる耐性軸を持つため、パーティ全体の弱点が重ならないよう分担できる組み合わせです。

**カバルドン**（同居率4位）はじめん単タイプで、でんき技を無効化、いわ技を半減（×0.5）で受けられます。ガブリアスと同様に、メガYのでんき×2弱点とメガY・メガX共通のいわ弱点を代わりに受けられる組み合わせです。

**ミミッキュ**（同居率5位）はゴースト/フェアリーで、ドラゴン技を無効化できます。メガXのドラゴン×2弱点をカバーできる一方、リザードンは両フォームともはがね技を半減（×0.5）で受けられるため、ミミッキュのはがね弱点を逆に補う関係にもなっています。

---

## まとめ

M-6のリザードンは使用率18位につけつつ、メガリザードンY（メガ石リザードナイトY・60.6%）とメガリザードンX（メガ石リザードナイトX・37.6%）という2つの全く異なる型がおよそ6対4の比率で併存するシーズンです。

- **メガYはくさ技ソーラービームでじめんタイプに打点を持ち、メガXはひこう解除でじめん・ドラゴンが新たな弱点になる（いわはメガYの×4からメガXでは×2に緩和）**：どちらのメガ石かで弱点タイプが入れ替わる特殊な構造
- **性格採用率（ひかえめ+おくびょう60.1% / いじっぱり+ようき37.1%）がメガ石採用率とほぼ一致**：性格分布から型選択の実態が裏付けられる
- **ガブリアス・ボーマンダ・カイリューは両フォーム共通で苦戦する一方、グソクムシャ・ルカリオ・サーフゴー・ギルガルド・ゴリランダー・ミミッキュ・アーマーガア・ウルガモス・アローラキュウコン・オオニューラ・ラウドボーン・イエッサン(オス)には両フォームとも優位を取れる**：型ごとの弱点だけでなく、両型に共通する得意・不得意の相手も把握しておく必要がある

いわ×4（メガY）／じめん・いわ・ドラゴン×2（メガX）という弱点構成の違いを踏まえ、パーティ内の他のポケモンでどちらの弱点を埋めるかが型選択とセットで問われるポケモンです。

---

*関連記事：[ガブリアス考察 M-6](/blog/garchomp-analysis-m6/)*
