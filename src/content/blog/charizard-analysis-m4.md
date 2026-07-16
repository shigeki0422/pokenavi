---
title: '【ポケモンチャンピオンズ】メガリザードン 考察 M-4 シーズン メガY/メガXの型選択'
description: 'M-4シーズン使用率11位のリザードン考察。メガリザードナイトY採用率65.3%・メガリザードナイトX33.5%のデータから、にほんばれソーラービーム型とりゅうのまい物理型の違い、弱点タイプの変化を分析します。'
pubDate: '2026-07-15'
updatedDate: '2026-07-15'
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
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" />
  <div>
    <h2 style="margin:0 0 8px">リザードン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">11位</strong>　持ち物: <strong>リザードナイトY 65.3% / リザードナイトX 33.5%</strong>
    </div>
  </div>
</div>

M-4シーズン、リザードンは使用率11位につけています。メガ進化することで2つの全く異なるポケモンに変わる特殊なポケモンで、メガリザードナイトY（採用率65.3%）はほのお/ひこうのまま特殊アタッカーになり、メガリザードナイトX（採用率33.5%）はほのお/ドラゴンに変化して物理アタッカーになります。どちらのメガ石を選ぶかでタイプ・弱点・技構成が丸ごと変わるため、対戦相手としても味方としても「どちらのメガ石か」の見極めが重要になります。

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

メガリザードナイトYは特攻159・特防115と特殊方面が伸び、特性が**ひでり**（登場時から5ターン天候をにほんばれにする）に変わります。メガリザードナイトXは攻撃130・防御111と物理方面が伸び、特性は**かたいツメ**（接触技威力×1.3）です。すばやさはどちらも通常時と同じ100で変化しません。

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

いわ×4が最大の弱点。M-4使用率1位のガブリアスが採用率49.6%のステルスロック（いわ）を設置するため、控えにいる間に大ダメージを受けます。じめんは無効なので、じしん採用率99.5%のガブリアス・98.4%のカバルドンの主力技は通りません。

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

メガXはひこうタイプでなくなるため、じめん技が無効から等倍（×2弱点）に転じます。一方ででんき技への耐性（×0.5）を新たに得るため、カイリュー（14位）の10まんボルトはメガXには半減で通ります。ただしみずタイプは等倍のまま耐性化はしないため、ギャラドス（8位）のたきのぼりはメガXにも等倍で通ります。どちらのメガ石を選ぶかで通る攻撃・通らない攻撃が入れ替わる点が、このポケモンの最大の特徴です。

### 特性

通常時は**もうか（86.1%）**が主流で、HPが1/3以下になるとほのお技の威力が1.5倍になります。控えは**サンパワー（13.9%）**で、にほんばれ下で特攻1.5倍になる代わり毎ターン最大HPの1/8を失います。ただしメガ進化するとメガYはひでりに、メガXはかたいツメに特性が固定で上書きされるため、通常時の特性はメガ進化前の場に出ているターンにのみ意味を持ちます。もうか・サンパワーいずれの場合も、メガ進化後は特性が入れ替わる点に注意が必要です。

---

## M-4の採用型

### 型1：メガY 特殊アタッカー型（ひかえめ 37.1% / おくびょう 27.4%）

**性格採用率: ひかえめ 37.1% / おくびょう 27.4%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガY 特殊アタッカー型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（86.1%）→メガ後ひでり<br>
<strong>性格:</strong> ひかえめ（C↑ A↓）またはおくびょう（S↑ A↓）<br>
<strong>EV:</strong> H2-C32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> リザードナイトY（65.3%）
</div>
<div>
<strong>技構成:</strong><br>
・ソーラービーム<br>
・かえんほうしゃ<br>
・エアスラッシュ<br>
・オーバーヒート（りゅうのまい）
</div>
</div>
</div>

メガYの特性ひでりで自ら天候をにほんばれにすることで、本来2ターン技のソーラービーム（くさ・威力120）を1ターンで撃てるようにするのが型の骨子です。ソーラービームはくさタイプのため、じめん技を主力にするガブリアス（1位）やカバルドン（3位）に等倍以上で通る貴重な打点になります（対カバルドン：じめん/あく複合に×2）。かえんほうしゃ（ほのお・威力90）は一致技として安定打点になり、エアスラッシュ（ひこう・威力75）はひるみ30%を狙えます。オーバーヒート（ほのお・威力130、使用後特攻2段階down）は一撃の火力に、りゅうのまい（採用率22.2%、A・S1段階上昇）は積み技の選択肢です。

**強み:**

ひかえめはH155 / A111 / B98 / C232 / D135 / S152。C232の高火力でメガメタグロス（はがね/エスパー、ほのお×2弱点）のようなほのお四倍弱点ではない相手にも一致技で大きく削れます。

**弱み:**

おくびょうはH155 / A111 / B98 / C211 / D135 / S167。S167まで伸びる一方、C211とひかえめよりダメージが落ちるため、ソーラービーム・かえんほうしゃの確定数がひかえめより1段階不利になる場面があります。

---

### 型2：メガX りゅうのまい物理型（いじっぱり 20.7% / ようき 12.7%）

**性格採用率: いじっぱり 20.7% / ようき 12.7%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:48px;height:48px">
  <strong style="font-size:1.05em">メガX りゅうのまい物理型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> もうか（86.1%）→メガ後かたいツメ<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）またはようき（S↑ C↓）<br>
<strong>EV:</strong> H2-A32-S32（全体最多EV分布）<br>
<strong>持ち物:</strong> リザードナイトX（33.5%）
</div>
<div>
<strong>技構成:</strong><br>
・フレアドライブ<br>
・ニトロチャージ<br>
・りゅうのまい<br>
・ドラゴンクロー
</div>
</div>
</div>

フレアドライブ（ほのお・威力120、被ダメージ1/3の反動）が一致最大打点。ニトロチャージ（ほのお・威力50、自分のS1段階上昇）は火力を出しながら素早さを補強でき、りゅうのまい（A・S1段階上昇）との相性が良い技です。ドラゴンクロー（ドラゴン・威力80、採用率18.7%）はガブリアス（じめん/ドラゴン）に一致補正なしでも×2で通る数少ない打点ですが、フレアドライブ・ニトロチャージはほのおタイプのためガブリアスには×0.5にとどまります。

**強み:**

いじっぱりはH155 / A200 / B131 / C135 / D105 / S152。A200はかたいツメ込みのフレアドライブで一撃の破壊力が高く、B131によりメガYより打たれ強さがあります。

**弱み:**

ようきはH155 / A182 / B131 / C135 / D105 / S167。S167でメガYと同速から一段先に動ける相手が広がる一方、A182といじっぱりよりフレアドライブの火力が落ちるトレードオフです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ドラゴンクロー（ドラゴン）×2</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">カバルドン（じめん/あく）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ソーラービーム（くさ）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドス（みず/ひこう）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×0.5</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×0.5</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メタグロス（はがね/エスパー）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×2</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×2</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラス（はがね/ドラゴン）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">かえんほうしゃ（ほのお）×1</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">フレアドライブ（ほのお）×1</td>
</tr>
</tbody>
</table>
</div>

表の倍率は`get_type_effectiveness`で全件検算済みです。ソーラービーム（くさ）はガブリアスには等倍止まりですが、じめん複合でも「あく」を挟むカバルドンには×2で通ります。一方メガXのドラゴンクロー（採用率18.7%と低め）はガブリアスに刺さる貴重な打点ですが採用が少数派で、多くのメガX個体はフレアドライブ・ニトロチャージのほのお技のみでガブリアスに対しては×0.5にとどまります。ほのお一致技はギャラドス（みず/ひこう）には×0.5、ブリジュラス（はがね/ドラゴン）には×1と、相手のタイプ次第で通りが大きく変わる点も見落とせません。メガYはくさ技を持つことでメガXにはない地面複合への上積みがある一方、メガXはひこうタイプが外れることでいわ×4のような致命的な四倍弱点を持たないという、攻守で明確なトレードオフになっています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33.5%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">対応する性格合計</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">ひかえめ+おくびょう 64.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">いじっぱり+ようき 33.4%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最多EV分布</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-C32-S32（32.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">H2-A32-S32（16.1%）</td>
</tr>
</tbody>
</table>
</div>

メガ石採用率（65.3% / 33.5%）と性格採用率の合計（64.5% / 33.4%）がほぼ一致しており、性格分布がそのままメガYとメガXの採用比率を反映していることがデータから裏付けられます。約2対1でメガYが優勢ですが、メガXも3割を超える採用があるため、対戦相手として遭遇した場合はどちらの型かを見て弱点タイプが変わることを踏まえた立ち回りが必要です。

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
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率99.5%）はメガYには無効ですが、メガXには×2弱点。ステルスロック（いわ・49.6%）はメガYに×4・メガXにも×2で、控えにいる間の被害が大きい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（じめん・採用率98.4%）はメガYには無効ですが、メガXには×2弱点。ステルスロック（いわ・76.2%）採用率が高く、メガYはとりわけ大きなダメージを受けて着地します</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（みず・採用率80.1%）がメガYに×2弱点。じしん（じめん・77.8%）はメガXに×2弱点。フォームに関わらずどちらかの弱点を突かれます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">りゅうせいぐん（ドラゴン・採用率93.3%）がメガXに×2弱点。C高水準のサザンドラの特殊打点は耐久の薄いメガXには大きな負担になります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みずしゅりけん（みず・採用率63.8%）・なみのり（みず・43.3%）がメガYに×2弱点。ゲッコウガのようき最速個体はS191に達し、メガY（S100）・メガX（S100）どちらよりも速く、先手を許しやすい相手です</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率上位の分析

M-4でリザードンと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
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
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" loading="lazy">
    <div class="name">サザンドラ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" loading="lazy">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率9位</div>
  </div>
</div>

**ガブリアス**（同居率1位）はじめん/ドラゴンで、特性はさめはだ（採用率99.4%）が主流です。じしん（じめん）はメガYには無効、メガXには通る技のためリザードンの型に応じて相手の受けを崩す役割を分担できます。ガブリアスのフェアリー弱点はリザードンのタイプ相性からは補完できませんが、両者ともみず技に対する一致以外の打点を持つ点で役割が分担されています。

**ミミッキュ**（同居率2位）はゴースト/フェアリーで、いわ・でんき技を半減する耐性は持ちませんが、ばけのかわで一度は攻撃を受け止められるため、リザードンが弱点を突かれて後退した後の受け直しに使えます。

**アシレーヌ**（同居率3位）はみず/フェアリーで、みず一致技を持つためメガYの弱点であるみずタイプを直接カバーできます。一方でリザードンはくさ技を×0.25で受けられる（両フォーム共通）ため、アシレーヌが苦手とするくさタイプへの耐性面を補います。

**メタグロス**（同居率4位）ははがね/エスパーで、ドラゴン半減・フェアリー半減を持ち、リザードンが処理しにくいフェアリータイプへの牽制役になります。メタグロスのほのお弱点（×2）はリザードン側が対処できませんが、パーティ全体としては役割が分かれています。

**マスカーニャ**（同居率5位）はくさ/あくで、みずタイプへの一致以外の打点を持たない一方、あく技でエスパー・ゴーストタイプを処理でき、リザードンが苦手とするいわ・でんき方面とは別の相手を分担します。

---

## まとめ

M-4のリザードンは使用率11位を維持しつつ、メガリザードナイトY（65.3%）とメガリザードナイトX（33.5%）という2つの全く異なる型がおよそ2対1の比率で併存するシーズンです。

- **メガYはくさ技ソーラービームでじめんタイプに打点を持ち、メガXはひこう解除でじめん・いわ・ドラゴンが新たな弱点になる**：どちらのメガ石かで弱点タイプが入れ替わる特殊な構造
- **性格採用率（ひかえめ+おくびょう64.5% / いじっぱり+ようき33.4%）がメガ石採用率とほぼ一致**：性格分布から型選択の実態が裏付けられる
- **ガブリアス・カバルドンのじしんはメガYには無効、メガXには×2**：対戦相手としても味方としても、どちらの型かの見極めが立ち回りの起点になる

いわ×4（メガY）／じめん・いわ・ドラゴン×2（メガX）という弱点構成の違いを踏まえ、パーティ内の他のポケモンでどちらの弱点を埋めるかが型選択とセットで問われるポケモンです。

---

*関連記事：[メガメタグロス考察 M-4](/blog/metagross-analysis-m4/)*
