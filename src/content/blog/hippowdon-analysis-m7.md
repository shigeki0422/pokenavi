---
title: '【ポケモンチャンピオンズ】カバルドン 考察 M-7 シーズン 使用率4位の解説'
description: 'M-7シーズン使用率4位のカバルドンを考察。じしん・あくび・なまける・ステルスロックの技構成と、こおりのキバ型の立ち回り、M-6からの技・持ち物採用率の変化、じしんが通る相手・通らない相手を使用率データで解説し、同居率パートナーも紹介します。'
pubDate: '2026-10-25'
updatedDate: '2026-10-14'
heroImage: '../../assets/hero-hippowdon-m7.png'
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
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" />
  <div>
    <h2 style="margin:0 0 8px">カバルドン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">4位</strong>　特性: <strong>すなおこし 99.8%</strong>
    </div>
  </div>
</div>

## カバルドンとは：M-7シーズン使用率4位

カバルドンはM-7シーズンの使用率ランキングで4位につけるじめん単タイプのポケモンです。HP・防御に厚く配分された高耐久型で、特性すなおこしによる天候操作と、あくびによる交代の強要・ステルスロックの設置で相手の選出を圧迫する運用が主流です。M-6からは技構成の重心が変化しています。

※本記事の使用率・採用率データは2026-10-11時点のものです。

---

## 基本スペック

<!-- gate:rows start id=base_stats facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">108</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:56%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">112</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:59%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">118</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">68</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:23.5%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">47</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

HP108・防御118という耐久寄りの配分に加え、こうげき112も高水準で、一致技じしん（威力100）の打点を支えています。一方ですばやさ47は環境上位の中でも下位クラスです。主流EV（H32-B32-D2、わんぱく）の実数値はH215・A132・B187・D94・S67で、苦手・得意表に挙げる相手にはいずれも後手に回ります。

## タイプ・弱点

<div class="type-row"><strong>タイプ：</strong><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></div>

<div style="overflow-x:auto;margin:12px 0"><table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<tr style="background:#f1f5f9">
<th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-10-water.png" alt="みず" style="width:24px;height:24px"><br><img src="/images/types/type-11-grass.png" alt="くさ" style="width:24px;height:24px"><br><img src="/images/types/type-14-ice.png" alt="こおり" style="width:24px;height:24px"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-03-poison.png" alt="どく" style="width:24px;height:24px"><br><img src="/images/types/type-05-rock.png" alt="いわ" style="width:24px;height:24px"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:24px;height:24px"></td>
</tr>
</table></div>

## 特性

<div style="overflow-x:auto;margin:12px 0"><table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<tr style="background:#f1f5f9"><th style="padding:8px 12px;border:1px solid #cbd5e1">特性</th><th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th><th style="padding:8px 12px;border:1px solid #cbd5e1">効果</th></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すなおこし</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">99.8%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">登場した時から5ターンの間、すなあらし状態にする<!-- gate:allow 5ターン reason="ability_master.すなおこし.effect_text" --></td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">すなのちから</td><td style="padding:8px 12px;border:1px solid #cbd5e1">0.2%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">すなあらし状態の時、いわ・じめん・はがねタイプの技の威力が1.3倍になる。すなあらしのダメージを受けない</td></tr>
</table></div>

すなあらし状態では、いわ・じめん・はがねタイプ以外で、かつすなあらしのダメージを受けない特性（すなかき・すながくれ・すなのちから・ぼうじん・マジックガード）を持たない相手は毎ターン最大HPの1/16を失います。きあいのタスキを潰したり、あくび・ステルスロックと合わせて着実に削る運用を支えます。

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em">
<thead>
<tr style="background:#f1f5f9">
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技名</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">タイプ</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">威力</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">採用率</th>
<th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">効果</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.2%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">地中状態の相手には威力が2倍になる。グラスフィールド状態の時、威力が1/2になる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">96.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をねむけ状態にする。相手に必ず命中する。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">66.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分のHPを最大HPの1/2回復する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ステルスロック</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手の場をステルスロック状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ふきとばし</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">31.5%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度-6。相手に控えがいる場合、相手をランダムに交代させる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>こおりのキバ</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">26.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をこおり状態にする。10％の確率で相手をひるませる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.8%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+4。使ったターン中、相手の技から身を守る。連続で使うと成功率が前に使った時の1/3になる。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

あくび・じしんはほぼ共通して採用されており、残りの技スロットをなまける・ステルスロック・こおりのキバ・ふきとばしの中から選ぶことで型が分かれます。

## 主な型

技構成の選択技から、採用割合が高い順に2つの型を紹介します。

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ステルスロック型（H32-B32-D2）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> オボンのみ（39.2%）
</div>
<div>
<strong>技構成:</strong><br>
・あくび<br>
・じしん<br>
・なまける<br>
・ステルスロック
</div>
</div>
</div>

H32-B32-D2（カバルドン全体のEVで最多25.2%）を基本とする型です。持ち物はオボンのみ（39.2%、カバルドン全体の値）が最有力です。

<!-- gate:rows start id=card:1 facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
**他の型との違い:**

- ステルスロック：この型は必ず持ち、こおりのキバ型では選択技
- 持ち物：オボンのみ（HPが最大HPの1/2以下になった時、最大HPの1/4回復する。1度使うと無くなる）
<!-- gate:rows end id=card:1 -->

---

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">こおりのキバ型（H32-B32-D2）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.8%）<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> ゴツゴツメット（32.9%）
</div>
<div>
<strong>技構成:</strong><br>
・あくび<br>
・こおりのキバ<br>
・じしん<br>
・なまける
</div>
</div>
</div>

ステルスロック型と同じH32-B32-D2・わんぱくが基本ですが、持ち物はゴツゴツメット（32.9%、カバルドン全体の値）が中心です。

<!-- gate:rows start id=card:2 facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
**他の型との違い:**

- 他の型に無い技：こおりのキバ
- 持ち物：ゴツゴツメット（接触技を受けると相手に最大HPの1/6のダメージを与える）
<!-- gate:rows end id=card:2 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ステルスロック型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">こおりのキバ型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガガブリアスZ（おくびょう・ガブリアスナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ（いじっぱり・いのちのたま）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（ゆうかん・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（ようき・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（ずぶとい・ふうせん ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（いじっぱり・ボーマンダナイト ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガボーマンダ（むじゃき・ボーマンダナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア（わんぱく・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)（ようき・こだわりスカーフ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガカイリュー（ひかえめ・カイリュナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー（いじっぱり・ゴツゴツメット）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr class="note"><td colspan="3" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。ブリジュラス、セグレイブ、キラフロルは型で判定が変わらない</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

## データ分析：M-6からの技・持ち物構成の変化


<div style="overflow-x:auto;margin:12px 0"><table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<tr style="background:#f1f5f9"><th style="padding:8px 12px;border:1px solid #cbd5e1">項目</th><th style="padding:8px 12px;border:1px solid #cbd5e1">M-6</th><th style="padding:8px 12px;border:1px solid #cbd5e1">M-7</th><th style="padding:8px 12px;border:1px solid #cbd5e1">増減</th></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">90.5%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">64.6%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">-25.9pt</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">ふきとばし採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">61.2%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">31.5%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">-29.7pt</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">なまける採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">38.1%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">66.4%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">+28.3pt</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">5.3%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">26.4%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">+21.1pt</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">オボンのみ採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">64.8%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">39.2%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">-25.6pt</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">ゴツゴツメット採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">18.4%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">32.9%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">+14.5pt</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">15.2%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">26.6%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">+11.4pt</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">わんぱく採用率</td><td style="padding:8px 12px;border:1px solid #cbd5e1">58.9%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">73.8%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">+14.9pt</td></tr>
</table></div>

<!-- gate:rows start id=diff_movers facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
- ふきとばし：61.2%→31.5%（-29.7pt）。ステルスロック型の一部の個体が採用しているもので、型の増減とは言えません。
- なまける：38.1%→66.4%（+28.3pt）。記事のすべての型に共通のため、型の増減とは言えません。
- ステルスロック：90.5%→64.6%（-25.9pt）。ステルスロック型が持ち、こおりのキバ型でも選択技のため、型の増減とは言えません。
- オボンのみ：64.8%→39.2%（-25.6pt）。ステルスロック型が持つほか、記事に載せていない型の個体も持つため、型の増減とは言い切れません。
- こおりのキバ：5.3%→26.4%（+21.1pt）。こおりのキバ型だけが持つため、この変化はその型の増減を示します。
- わんぱく：58.9%→73.8%（+14.9pt）。記事のすべての型が選んでいるため、型の増減とは言えません。
- ゴツゴツメット：18.4%→32.9%（+14.5pt）。こおりのキバ型が持つほか、ステルスロック型の一部の個体も持つため、型の増減とは言い切れません。
- しんちょう：31.1%→18.2%（-12.9pt）。ステルスロック型の一部の個体が選んでいるもので、型の増減とは言えません。
<!-- gate:rows end id=diff_movers -->


## 苦手なポケモン

使用率上位のうち、ステルスロック型・こおりのキバ型の両方で結果が一致する相手のみ掲載しています。

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
<!-- gate:rows start id=weak facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定4発。アシレーヌのうたかたのアリア（採用率75.3%）は確定2発で、S67対S80で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトY66.5%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のこおりのキバは確定5発。メガリザードンYのソーラービーム（採用率65.6%）は乱数1発（69%）で、S67対S167で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発。イエッサン(オス)のワイドフォース（採用率99.8%）は確定2発で、S67対S161で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のこおりのキバは乱数3発（62%）。ゴリランダーのドラムアタック（採用率64.7%）は確定2発で、S67対S107で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発。マスカーニャのトリプルアクセル（採用率88.1%）は乱数2発（49%）で、S67対S288（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス<br><span style="font-size:0.8em;color:#64748b">メガギャラドスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定4発。メガギャラドスのパワーウィップ（採用率66.5%）は確定3発で、S67対S146で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発。ゲッコウガのなみのり（採用率36.9%）は確定2発で、S67対S174で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" alt="フラエッテ(永遠)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">フラエッテ(永遠)<br><span style="font-size:0.8em;color:#64748b">メガフラエッテで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">25位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定3発。メガフラエッテのムーンフォース（採用率96.9%）は乱数2発（98%）で、S67対S169で後手のため、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カメックス<br><span style="font-size:0.8em;color:#64748b">メガカメックスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定3発。メガカメックスのはどうだん（採用率92.5%）は確定3発で、S67対S130で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ヒートロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型には有効な攻撃技が無く、倒しきれません。ヒートロトムのイカサマ（採用率15.0%・少数派）は確定10発で、S67対S106で後手になり、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=weak -->
</tbody>
</table>
</div>

## 得意なポケモン

ステルスロック型・こおりのキバ型の両方でカバルドンが有利になる相手のみ掲載しています。

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
<!-- gate:rows start id=strong facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（リザードナイトX32.3%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定2発。メガリザードンXのフレアドライブ（採用率31.4%）は確定3発で、S67対S167で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ<br><span style="font-size:0.8em;color:#64748b">メガルカリオZで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定1発。メガルカリオZのてっていこうせん（採用率36.3%）は確定2発で、S67対S223で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ステルスロック型のじしんは確定2発。メガメタグロスのれいとうパンチ（採用率73.8%）は乱数3発（98%）で、S67対S162で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定2発。エースバーンのとびひざげり（採用率93.7%）は乱数3発（69%）で、S67対S282（スカーフ込み）で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" alt="ゲンガー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲンガー<br><span style="font-size:0.8em;color:#64748b">メガゲンガーで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定1発。メガゲンガーのシャドーボール（採用率84.5%）は確定2発で、S67対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0026-00.webp" alt="ライチュウ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ライチュウ<br><span style="font-size:0.8em;color:#64748b">メガライチュウYで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定2発。メガライチュウYのきあいだま（採用率97.1%）は乱数3発（84%）で、S67対S200で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定1発。オオニューラのインファイト（採用率99.3%）は確定3発で、S67対S146で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">34位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ型のじしんは確定2発。ギルガルドのポルターガイスト（採用率76.4%）は乱数3発（>99%）で、S67対S112で後手ですが確定数で上回り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

## 同居率・パートナー（TOP10）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" loading="lazy">
    <div class="name">メタグロス</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" loading="lazy">
    <div class="name">イダイトウ(オス)</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">サーフゴー<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率5位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率6位・メガボーマンダで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率7位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ルカリオ<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガルカリオZで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">メタグロス<br><span style="font-weight:normal;font-size:0.85em">同居率9位・メガメタグロスで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イダイトウ(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドンの弱点：くさ技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドンの弱点：こおり技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドンの弱点：みず技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アシレーヌ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガリザードンY</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イエッサン(オス)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">マスカーニャ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ギャラドス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゲッコウガ</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">フラエッテ(永遠)</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カメックス</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ヒートロトム</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○6</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○6</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○6</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○2</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝カバルドンの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：アシレーヌ＝ムーンフォース・うたかたのアリア・アクアジェット；メガリザードンY＝ソーラービーム・りゅうのはどう・かえんほうしゃ・フレアドライブ；イエッサン(オス)＝ワイドフォース・マジカルフレイム・マジカルシャイン；ゴリランダー＝グラススライダー・ドラムアタック・とんぼがえり・10まんばりき・はたきおとす；マスカーニャ＝トリックフラワー・トリプルアクセル・はたきおとす・とんぼがえり；ギャラドス＝じしん・パワーウィップ・たきのぼり・ゆきなだれ・こおりのキバ；ゲッコウガ＝あくのはどう・れいとうビーム・ヘドロウェーブ・みずしゅりけん・なみのり；フラエッテ(永遠)＝ムーンフォース・ドレインキッス；カメックス＝はどうだん・あくのはどう・だいちのはどう；ヒートロトム＝オーバーヒート・ボルトチェンジ・10まんボルト</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

## まとめ

<!-- gate:rows start id=summary facts=a8c887f9b36d9d13c918ebff98b4551411b4cbbb -->
**強み**

- 得意な相手は8体です。使用率上位では、メガリザードンX（6位）・ルカリオ（7位）・メタグロス（14位）にじしんで勝てます。
- タイプ相性では、どく・いわを半減以下、でんきを無効で受けられます。

**弱み**

- 苦手な相手は10体です。使用率上位では、アシレーヌ（2位）のうたかたのアリア、メガリザードンY（6位）のソーラービーム、イエッサン(オス)（17位）のワイドフォースで先に倒されます。
- 弱点はみず・くさ・こおりです。

**型の選び分け**

- 「ステルスロック型」：ステルスロックを必ず持つ（こおりのキバ型では選択技）。
- 「こおりのキバ型」：他の型に無い技はこおりのキバ。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は4位です（M-6: 7位）。
- 採用率の変化が大きいのはふきとばし（-29.7pt）・なまける（+28.3pt）・ステルスロック（-25.9pt）です。
<!-- gate:rows end id=summary -->

<p style="font-size:0.9em;color:#64748b">関連記事：<a href="/blog/hippowdon-analysis-m6/">カバルドン考察（M-6）</a>、<a href="/blog/garchomp-analysis-m6/">ガブリアス考察（M-6）</a></p>
