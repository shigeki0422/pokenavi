---
title: '【ポケモンチャンピオンズ】メガフラエッテ徹底考察 M-2シーズン・メガ進化の全て'
description: 'シーズンM-2（5/20時点・使用率11位）でメガ進化率97%を誇るメガフラエッテを徹底分析。めいそう×ドレインキッスの崩し性能、ギャラドスとの6枠構成、パーティ全体の組み方まで実データをもとに解説します。'
pubDate: '2026-05-21'
heroImage: '../../assets/hero-florette-m2.png'
---

<style>
.type-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.85em;
  font-weight: bold;
}
.poke-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0;
  padding: 16px 20px;
  background: linear-gradient(135deg, #fce4f3 0%, #f3e8ff 100%);
  border-radius: 16px;
  border: 1px solid #e9b8d8;
}
.poke-header img.poke-icon {
  width: 80px;
  height: 80px;
}
.poke-header .poke-info h2 {
  margin: 0 0 6px;
  font-size: 1.5rem;
}
.stat-table td, .stat-table th {
  padding: 6px 12px;
  border: 1px solid #e2e8f0;
  text-align: center;
}
.stat-table th {
  background: #f8f0fb;
  font-weight: 600;
}
.bar-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}
.bar {
  height: 10px;
  border-radius: 5px;
  background: linear-gradient(90deg, #c084db, #e879a8);
}
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" class="poke-icon" />
  <div class="poke-info">
    <h2>フラエッテ（永遠の花）</h2>
    <div>
      <img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">
      <strong>フェアリー</strong>タイプ
      &nbsp;｜&nbsp; M-2シングル使用率 <strong>11位</strong>（5/20時点）
      &nbsp;｜&nbsp; メガ進化率 <strong>97.4%</strong>
    </div>
  </div>
</div>

<div style="background:#fff8e1;border-left:4px solid #f59e0b;padding:10px 16px;border-radius:6px;font-size:0.88em;color:#78350f;margin:8px 0 20px">
  ⚠️ 本記事のデータはM-2シーズン開始8日目（2026/05/20）時点の集計です。シーズン終了（06/17）に向けて順位は変動する可能性があります。
</div>

---

## なぜ今、メガフラエッテが強いのか

M-2環境のシングルバトルで注目を集めるメガフラエッテ（5/20時点・使用率11位）。その強さの理由は3つです。

1. **フェアリーオーラ×とくこう155の圧倒的火力** 固有特性フェアリーオーラによりフェアリー技の威力が×1.33倍。とくこう155と合わさることで、ムーンフォース・ドレインキッスが環境上位ポケモンを軒並み確定2発圏内に捉える
2. **めいそう×ドレインキッスの自己完結した崩し** 積みながら回復できるため、先制技・タスキ込みの相手にも崩しが止まりにくい。1体で試合を決められるエース性能を持つ
3. **ドラゴン完全無効でM-2上位に強い** ガブリアス・リザードン・サザンドラなどM-2上位を占めるドラゴン技を完全に無効化。メガギャラドスとも物理×特殊・みず/あく×フェアリーの理想的な補完を形成する

---

## 基本スペック

### 種族値（メガフラエッテ）

<div style="max-width:360px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">74</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:42.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">85</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43.5%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">87</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:77.5%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>155</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:74%;background:linear-gradient(90deg,#9333ea,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right"><strong>148</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #f0e6f8">
    <span style="width:68px;min-width:68px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:51%;background:linear-gradient(90deg,#c084db,#e879a8);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">102</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:68px;min-width:68px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#9333ea">651</span>
  </div>
</div>

メガ進化でとくこう**125→155**、とくぼう**128→148**、すばやさ**92→102**と大幅強化。合計種族値651は環境内でもトップクラスです。

### タイプ相性（メガ進化前）

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">タイプ</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">弱点・耐性</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> はがね</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#e53e3e">×2</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> どく</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#e53e3e">×2</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> ドラゴン</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#2563eb">×0（無効）</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> かくとう</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#60a5fa">×0.5</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-16-dark.png" alt="あく" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> あく</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#60a5fa">×0.5</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-06-bug.png" alt="むし" style="width:24px;height:24px;vertical-align:middle;margin-right:4px"> むし</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong style="color:#60a5fa">×0.5</strong></td></tr>
</tbody></table></div>

ドラゴン無効はM-2環境で極めて価値が高く、使用率上位を占める**ガブリアス・リザードン・サザンドラ・カイリュー**のドラゴン技を完全に無効化できます。弱点ははがねとどくの2タイプのみ。

---

## 採用技の解説

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">技</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">威力</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">命中</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">採用率</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">効果</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">ムーンフォース</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">95</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">100</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">87.1%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">10%でとくこう-1</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">めいそう</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">84.4%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">とくこう・とくぼう+1</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">ドレインキッス</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">50</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">100</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">75.1%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">与ダメの1/2を回復</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">はめつのひかり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">140</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">90</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">46.7%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">与ダメの1/2を自分も受ける</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">サイコキネシス</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">90</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">100</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">38.8%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">10%でとくぼう-1</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">こうごうせい</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">22.4%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">HPを最大値の1/2回復</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">あまえる</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">100</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">12.0%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">相手のこうげき-2</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px;vertical-align:middle;margin-right:6px">みがわり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">9.8%</td><td style="padding:8px 12px;border:1px solid #e2d4f0">HP1/4消費でみがわり生成</td></tr>
</tbody></table></div>

### フェアリーオーラによる実質威力

メガ進化後の特性フェアリーオーラにより、フェアリー技の威力が全て1.33倍になります。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">技</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">表記威力</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">フェアリーオーラ補正後</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">ムーンフォース</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">95</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong>126</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">ドレインキッス</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">50</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong>67</strong></td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">はめつのひかり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">140</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong>186</strong></td></tr>
</tbody></table></div>

はめつのひかりの実質威力186は全技の中でもトップクラスであり、反動を考慮しても破壊力は圧倒的です。

### シングル2大方向性：めいそう型 vs フルアタ型

採用率データが示す**ムーンフォース(87%) + ドレインキッス(75%)** の2技はほぼ全型共通ですが、残り2枠で型の方向性が大きく分かれます。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left"></th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">めいそう積みエース型</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">フルアタ型</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">技構成</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">ムーンフォース / めいそう /<br>ドレインキッス / みがわり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">はめつのひかり / ムーンフォース /<br>ドレインキッス / サイコキネシス</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">めいそう</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">○ 採用</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">✕ 非採用</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">はめつのひかり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">✕ 非採用</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">○ 採用</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">ドレインキッスの役割</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">積んだとくこうで継続回復</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">はめつのひかり反動のHP補填</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">勝ち筋</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">積み上がれば全抜き</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">即時威力186で押し切る</td></tr>
</tbody></table></div>

**はめつのひかりとドレインキッスは同居する**——ただし「積みながら回復する型」ではなく、めいそうなしの純粋なアタッカー型として組み合わせます。めいそう(84.4%)とはめつのひかり(46.7%)がそれぞれ高い採用率を示すのは、この2型が並行して使われているためです。

ダブルではさらに別の型（マジカルシャイン / はめつのひかり / ムーンフォース / まもる）が存在します。

---

## 持ち物・特性

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">項目</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">採用率1位</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">採用率2位</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">持ち物</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">フラエッテナイト 97.4%</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">—</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">特性</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">フラワーベール 97.5%</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">きょうせい 2.5%</td></tr>
</tbody></table></div>

持ち物はフラエッテナイト一択。

**特性の変化に注意**：メガ進化前の特性は「フラワーベール（草タイプの能力低下を防ぐ）」ですが、メガ進化後は**フェアリーオーラ**に変わります。フェアリーオーラは**場に出ている全ポケモンのフェアリー技の威力を1.33倍にする**特性です。

この特性はメガフラエッテ自身のムーンフォース・はめつのひかり・ドレインキッスを強化するだけでなく、**相手のフェアリー技も強化してしまう**点に注意が必要です。ただしシングルバトルでは相手のフェアリーアタッカーと同時に場に立つ機会が限られるため、実質的には自分の火力底上げとして機能します。

---

## 型考察

M-2で確認できる主要な3型を紹介します。型①②はどちらもおくびょうですが、めいそうを積む「制圧型」かはめつのひかりで即攻める「アタッカー型」かで技構成が大きく異なります。

### 型①：おくびょうCS型（先手積みエース）

**採用率トップ（おくびょう52.8%）**

```
性格：おくびょう
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / みがわり
```

**なぜおくびょうが最多か——素早さラインの意味**

メガ進化後のすばやさ種族値は102。ガブリアス（102）と同値で、リザードン（100）・サザンドラ（98）・メガギャラドス（81）より速い位置にあります。ただし**ゲンガー（110）には上から抜かれる**ため、何もしなければゲンガーに先手を渡すことになります。

おくびょうCS全振りにすることで、**無補正ガブリアスへの先手**が取れるようになり、リザードン・サザンドラには確実に先手を取れます。**先に動けるかどうかはめいそうを積めるかどうかを直接決定する**ため、おくびょう採用の優先度が高くなっています。

4枠目のみがわりは積み展開の安定化に貢献します。ゲンガーの催眠・トリックを最も警戒するなら初手みがわりから入るのが安全で、みがわりが維持されている間に積んで制圧します。

---

### 型②：おくびょうCS型（フルアタ即時火力）

```
性格：おくびょう
努力値：CS（とくこう・すばやさ全振り）
持ち物：フラエッテナイト
技構成：はめつのひかり / ムーンフォース / ドレインキッス / サイコキネシス
```

**めいそうを積まず即時火力で押し切る型**

型①との最大の違いは**めいそうを採用しない**点です。実質威力186のはめつのひかりをそのまま打ち込んで相手を削り、ドレインキッスで反動ダメージを部分的に補填しながら戦線を維持します。

**ダメージ計算で検証：はめつのひかりが確定1発を取れるターゲット**

リスクを承知でなぜはめつのひかりを採用するか——答えはダメージ計算に示されます。

Level 50のダメージ計算式（特殊技）：

```
Base     = floor( 22 × 威力 × SpA / SpD ) ÷ 50 + 2
確定ダメージ = Base × STAB(1.5) × フェアリーオーラ(1.33) × タイプ相性 × 乱数(0.85〜1.00)
```

ムーンフォース(95) vs はめつのひかり(140) の威力比 = **1.474倍**。この差から、ムーンフォースがHP残量の **68%以上** を与えている相手に対し、はめつのひかりが確定1発を取れる計算になります（0.68 × 1.474 ≈ 1.00）。

M-2の主要3ターゲット（おくびょうC252、C実数値207）で具体的に検証します。

---

**シナリオ①：アシレーヌ**

アシレーヌ（おくびょうCS：HP155, D135, フェアリー中性×1）

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left"></th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">ダメージ幅</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">HP155比</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">確定数</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">ムーンフォース</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">111〜131</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">72〜85%</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">確定2発</td></tr>
<tr style="background:#fff0f8"><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:700">はめつのひかり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">162〜191</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">105〜123%</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">確定1発</td></tr>
</tbody></table></div>

積みなし・素の状態で確定1発が取れる最も明確なシナリオ。

---

**シナリオ②：カイリュー（マルチスケイル突破）**

カイリュー（HP特化型：HP198, D120、フェアリー技被弱点×2、**マルチスケイル残り**）

マルチスケイルはHP満タン時にダメージを1/2にする特性。フルHPの状態では効果が残る。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left"></th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">通常ダメージ</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">マルチスケイル後（÷2）</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">HP198への確定数</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">ムーンフォース</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">249〜294</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">124〜147（63〜74%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center"><strong>確定2発</strong></td></tr>
<tr style="background:#fff0f8"><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:700">はめつのひかり</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">365〜430</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">182〜215（92〜109%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">乱数8/16（50%）で1発</td></tr>
</tbody></table></div>

HP特化しないアタッカー型（HP=166）に対しては、はめつのひかり最小値182 > HP166 → **確定1発**。

**ムーンフォースはマルチスケイルを一切突破できない**（最大147 < HP166/198）のに対し、はめつのひかりはHP型でも50%・アタッカー型では確定で突破できます。

---

**シナリオ③：ステルスロック展開後のリザードン**

リザードン（おくびょうCS：HP153, D105, ほのお/ひこう×0.5、**ステロ×4弱点**）

リザードン（ほのお/ひこう）はステルスロックに×4弱点（ほのお×2・ひこう×2）→ HP50%削り（76ダメージ、残り77HP）。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left"></th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">ステロ前（HP153残り）</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">ステロ後（HP77残り）</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">ムーンフォース（70〜83）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">確定2発（46〜54%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">乱数7/16（43.75%）で1発</td></tr>
<tr style="background:#fff0f8"><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:700">はめつのひかり（103〜122）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">確定2発（67〜80%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">確定1発（134〜159%）</td></tr>
</tbody></table></div>

ステロ前は両者とも確定2発。ステロ後にはめつのひかりが確定1発、ムーンフォースはランダム43.75%にとどまります。**ガブリアスのステルスロック展開を前提とする構築では、ステロ後リザードンを確実に処理できる**点がフルアタ型固有の優位性です。

---

**C252投資が必須条件**

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left">C努力値</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">実数値</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">アシレーヌ（HP155, D135）への最小ダメージ</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">判定</th>
</tr></thead>
<tbody>
<tr style="background:#fff0f8"><td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:700">252（おくびょう）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">207</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">162（105%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center;font-weight:700">確定1発</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #e2d4f0">0（未投資）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">175</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">136（88%）</td><td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">確定2発</td></tr>
</tbody></table></div>

未投資ではアシレーヌへの確定1発が成立しません。フルアタ型は**C252一択**です。

ムーンフォースを使う場面：HPが減って反動が致命傷になりうる局面、または命中90のリスクを避けたい局面で使い分けます。

サイコキネシスでどくタイプへの打点を確保。フラエッテが弱点を突かれるどく技を持つポケモンを先に処理できます。

**弱点**：積みがないため高耐久ポケモンへの崩しが難しい。はめつのひかりの反動をドレインキッスで完全相殺はできないため、長期戦になるほどHP消耗が進む。

---

### 型③：ひかえめHB型（耐久火力両立）

**ひかえめ42.6%のうち、HB+c等の耐久振りスプレッドが相当数を占める**

```
性格：ひかえめ
努力値：HB+c（HP・ぼうぎょ重点、とくこうに余りを振る）
持ち物：フラエッテナイト
技構成：ムーンフォース / めいそう / ドレインキッス / こうごうせい or みがわり
```

**ひかえめ+耐久振りの意図**

性格ひかえめはとくこうを+10%補正しつつ、こうげき（フラエッテが使わない）を下げます。つまり実質デメリットなしでとくこうを強化できます。これにHB方向の努力値配分を組み合わせることで、**おくびょうCS型より遅いが物理1発耐え性能を持ちながら、ずぶとい型よりとくこうが高い**という中間ポジションを実現します。

物理耐久を確保することでルカリオ・ハッサムなどのはがね物理アタッカーの攻撃を1発耐えてめいそうを積む展開が可能。こうごうせい採用でターンをまたいだ回復を組み合わせれば、削られながらも積み続けられる持久戦型のエースになります。みがわり採用の場合はゲンガーの催眠・トリックへの耐性を確保しつつ積む展開が可能です。

**この型の課題**は速度を大幅に犠牲にすること。おくびょうCS型が先手を取れていた相手（ガブリアス・リザードンなど）に後手に回るため、積むターンを作るには相手の選出や対面操作に依存する部分が増えます。

---

### 型の選択マトリクス

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:left"></th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">型①<br>めいそう積みエース</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">型②<br>フルアタ即時火力</th>
  <th style="padding:8px 12px;background:#f8f0fb;border:1px solid #ddb8ee;text-align:center">型③<br>耐久火力両立</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">性格</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">おくびょう / ひかえめ</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">おくびょう</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">ひかえめ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">努力値</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">CS</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">CS</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">HB+c</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">めいそう</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">○</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">✕</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">○</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">はめつのひかり</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">✕</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">○</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">✕</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">ドレインキッス</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">積み回復</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">反動補填</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">積み回復</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">4枠目</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">みがわり /<br>サイコキネシス</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">サイコキネシス</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">こうごうせい /<br>みがわり</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;font-weight:600;background:#fdf8ff">速度</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">速い（先手優先）</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">速い（先手優先）</td>
  <td style="padding:8px 12px;border:1px solid #e2d4f0;text-align:center">遅い（耐えて積む）</td>
</tr>
</tbody>
</table>
</div>

---

## 相性の良いメガ進化パートナー：メガギャラドス

フラエッテの**同居率1位（ギャラドス）**かつ**ギャラドスのギャラドスナイト採用率76.3%**——データが示す通り、メガフラエッテの最有力パートナーはメガギャラドスです。

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f0f9ff;border:1px solid #bae6fd;text-align:left">項目</th>
  <th style="padding:8px 12px;background:#fce4f3;border:1px solid #f9a8d4;text-align:center"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガフラエッテ</th>
  <th style="padding:8px 12px;background:#eff6ff;border:1px solid #bfdbfe;text-align:center"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">メガギャラドス</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">攻撃軸</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">特殊（とくこう125）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">物理（こうげき高い）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">主な技</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">ムーンフォース・ドレインキッス</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">たきのぼり・りゅうのまい・じしん</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">セットアップ</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">めいそう（特殊耐久↑）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">りゅうのまい（すばやさ・こうげき↑）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">弱点</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">はがね・どく</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">でんき・かくとう・むし・くさ・フェアリー</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #e2e8f0">特性（メガ前）</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">フラワーベール</td>
  <td style="padding:8px 12px;border:1px solid #e2e8f0;text-align:center">いかく（こうげき-1）</td>
</tr>
</tbody>
</table>
</div>

### なぜこの組み合わせが強いか

**フラエッテ選出時の補完（メガギャラドスが苦手な相手をフラエッテがカバー）**

- フラエッテのフェアリー技は、メガギャラドス（みず/あく）が×2弱点を持つ**かくとうタイプ**に対して有効
- 環境上位の**ドラゴンタイプ**全般にもフェアリー技で×2を取れる

**ギャラドス選出時の補完（フラエッテが苦手な相手をメガギャラドスがカバー）**

- ギャラドスのじしんでフラエッテの弱点であるはがね（ブリジュラス・ギルガルドなど）を処理
- フラエッテが苦手などく・はがね主体の相手に対して物理制圧で対応できる

**ギャラドスの主要データ（M-2）**

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead><tr>
  <th style="padding:8px 12px;background:#eff6ff;border:1px solid #bfdbfe;text-align:left">項目</th>
  <th style="padding:8px 12px;background:#eff6ff;border:1px solid #bfdbfe;text-align:left">データ</th>
</tr></thead>
<tbody>
<tr><td style="padding:8px 12px;border:1px solid #dbeafe;font-weight:600;background:#f8fbff">使用率</td><td style="padding:8px 12px;border:1px solid #dbeafe">10位</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #dbeafe;font-weight:600;background:#f8fbff">性格（1位）</td><td style="padding:8px 12px;border:1px solid #dbeafe">いじっぱり 45.1%</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #dbeafe;font-weight:600;background:#f8fbff">努力値（1位）</td><td style="padding:8px 12px;border:1px solid #dbeafe">AS（すばやさ・こうげき全振り）38.1%</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #dbeafe;font-weight:600;background:#f8fbff">技構成</td><td style="padding:8px 12px;border:1px solid #dbeafe">たきのぼり / りゅうのまい / じしん / こおりのキバ</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #dbeafe;font-weight:600;background:#f8fbff">ギャラドスナイト採用率</td><td style="padding:8px 12px;border:1px solid #dbeafe">76.3%</td></tr>
</tbody></table></div>

---

## フラエッテを軸にしたパーティ構成案

1試合にメガ進化できるのは1体のみです。フラエッテ（フラエッテナイト）とギャラドス（ギャラドスナイト）を同じ6枠に入れておき、**フラエッテが有利な対面にはフラエッテ＋サポート2体を選出してメガフラエッテ軸**で戦い、はがね・どくが多い等フラエッテが不利な相手には**ギャラドス＋サポート2体に切り替えてメガギャラドス軸**で戦う、というスイッチ選出が基本思想です。

### パーティ構成案①「ステロ展開型」

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主軸メガ枠</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ（フラエッテナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう積み全抜きエース。基本選出</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">代替メガ枠</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（ギャラドスナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どくが多い相手にフラエッテの代わりに選出しメガ進化</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">展開サポート</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック＋はがね処理（じしん）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">崩し</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">催眠・トリックで相手の積みを崩す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">物理受け・サポート</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0823-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね/ひこうでどく耐性・ちょうはつでフラエッテの積みを守る（使用率6位）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻・先制技</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0448-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マッハパンチ＋はがね技でフラエッテの弱点を補完</td>
</tr>
</tbody>
</table>
</div>

**フラエッテ選出時の流れ：**
1. **ガブリアス**でステルスロック展開・相手のはがねタイプをじしんで処理
2. **メガフラエッテ**が盤面が整った後にめいそう積みから全抜き
3. ゲンガー・ルカリオが詰め・崩し役

**ギャラドス選出時（はがね・どく主体の相手）：**
1. **ガブリアス**でステルスロック・電気対策
2. **メガギャラドス**のいかく＋りゅうのまいで物理制圧
3. ルカリオ・ゲンガーがサポート

### パーティ構成案②「サイクル崩し型」

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">役割</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">ポケモン</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">採用理由</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主軸メガ枠</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0670-05.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ（フラエッテナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">めいそう＋みがわりで安定した積み詰め。基本選出</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">代替メガ枠</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0130-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギャラドス（ギャラドスナイト）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フラエッテ不利時に代わりに選出。いかく＋ちょうはつで相手のサポート封じ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステロ撒き</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0143-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カビゴン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">のろい積み＋どくどく＋ステロで削り</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">電気対策</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ギャラドスの弱点・でんきに強い</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0681-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね耐性でフラエッテの裏から出せる・キングシールド</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">速攻</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;white-space:nowrap"><img src="/images/pokemon/pokemon-0823-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アーマーガア</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね＋ひこうタイプでどくに強く、とんぼがえりでサイクル回し</td>
</tr>
</tbody>
</table>
</div>

---

## フラエッテが苦手なポケモンと対策

<div style="overflow-x:auto;margin:16px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">苦手な相手</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">理由</th>
  <th style="padding:8px 12px;background:#f1f5f9;border:1px solid #cbd5e1;text-align:left">解決策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0681-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:2px">ギルガルド・<img src="/images/pokemon/pokemon-0212-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:2px">ハッサム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">はがね技で弱点</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="" style="width:28px;height:28px;vertical-align:middle;margin-right:4px">ガブリアスのじしんで処理</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0094-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">催眠で積み展開を妨害</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みがわりを張ってから積む・サイコキネシス採用なら先にゲンガーを処理（どくタイプに×2）</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">バレットパンチ（先制はがね技）で上から弱点を突いてくる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アーマーガアのひこう耐性で受けてサイクルを回す</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-03-poison.png" alt="どく" style="width:22px;height:22px;vertical-align:middle;margin-right:4px">どく技（ヘドロばくだん等）で弱点を突く（使用率13位）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ガブリアスのじしんで処理・先にキラフロルを排除してからフラエッテを展開</td>
</tr>
</tbody>
</table>
</div>

---

## まとめ

メガフラエッテはM-2シングルで**「積みエース」「ドラゴン封じ」「耐久回復」を1体で兼ねる**稀有なポケモンです。

- **フラエッテナイト採用率97.4%**——実質メガ進化専用枠として機能
- **めいそう＋ドレインキッスの自己完結**でタスキ・先制技に強く、長期戦でも制圧できる
- **ギャラドスとの同居率1位**——フラエッテが苦手な相手にはギャラドスをメガ進化させる選出に切り替える2択構成として機能

同じ6枠にフラエッテとギャラドスを共存させ、対面に応じてどちらをメガ進化させるか選ぶ構成は、M-2環境の中核的な戦略の一つです。次シーズンでの採用も十分に検討に値します。
