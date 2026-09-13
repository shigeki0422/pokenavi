---
title: '【ポケモンチャンピオンズ】カバルドン 考察 M-6 シーズン 使用率5位の解説'
description: 'M-6シーズン使用率5位のカバルドンを考察。すなおこしと高耐久種族値、あくびで後続に負荷をかける立ち回り、じしんで通る相手・S67の遅さで後手に回る相手をデータで解説。'
pubDate: '2026-09-13'
updatedDate: '2026-09-13'
heroImage: '../../assets/hero-hippowdon-m6.png'
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
      使用率: <strong style="color:#e67e22">5位</strong>　特性: <strong>すなおこし 99.9%</strong>
    </div>
  </div>
</div>

## カバルドンとは：M-6シーズン使用率5位

カバルドンはM-6シーズンの使用率ランキングで5位につけるじめん単タイプのポケモンです。種族値合計525のうちHP・防御・特防に厚く配分された高耐久型で、特性すなおこしによる天候操作とあくび・ステルスロックの設置技で相手の選出を圧迫する運用が主流です。素早さは種族値47と低く、実数値もS67にとどまるため、後手から受けて縛る立ち回りが基本になります。

※本記事の使用率・採用率データは2026-09-10時点のものです。

## 基本スペック

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:54%;background:linear-gradient(90deg,#f87171,#dc2626);height:12px;border-radius:4px"></div>
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
      <div style="width:59%;background:linear-gradient(90deg,#facc15,#ca8a04);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">118</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:34%;background:linear-gradient(90deg,#4ade80,#16a34a);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">68</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:36%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">72</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:24%;background:linear-gradient(90deg,#c084fc,#9333ea);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">47</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

HP108・防御118・特防72という配分に加え、こうげき112も高水準です。一方で素早さ47は環境上位の中でも下位クラスで、主流EV（H32-B2-D32、わんぱく）実数値はH215・B154・D124・A132・S67にとどまります。

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

みず・くさ・こおりが弱点で、でんき無効も持つため被弾面での事故は少なめです。ただし高耐久でも弱点技を継続して受ければ削られるため、苦手なポケモンの節で個別に見ていきます。

## 特性

<div style="overflow-x:auto;margin:12px 0"><table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<tr style="background:#f1f5f9"><th style="padding:8px 12px;border:1px solid #cbd5e1">特性</th><th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th><th style="padding:8px 12px;border:1px solid #cbd5e1">効果</th></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すなおこし</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1">99.9%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">場に出てから5ターンの間、すなあらし状態にする</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">すなのちから</td><td style="padding:8px 12px;border:1px solid #cbd5e1">0.1%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">すなあらし中、いわ・じめん・はがね技の威力が1.3倍になる。すなあらしのダメージを受けない</td></tr>
</table></div>

すなおこしがほぼ全ての個体で採用されています。カバルドン自身はすなあらしのダメージを受けず、いわ・じめん・はがね以外の相手には毎ターン最大HPの1/16のダメージが入るため、きあいのタスキを潰したり、あくび・ステルスロックと合わせて着実に削る運用を支えます。

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0"><table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<tr style="background:#f1f5f9"><th style="padding:8px 12px;border:1px solid #cbd5e1">技名</th><th style="padding:8px 12px;border:1px solid #cbd5e1">タイプ</th><th style="padding:8px 12px;border:1px solid #cbd5e1">威力</th><th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th><th style="padding:8px 12px;border:1px solid #cbd5e1">備考</th></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">じしん</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">100</td><td style="padding:8px 12px;border:1px solid #cbd5e1">99.3%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">一致技で唯一の攻撃打点。ほぼ全個体が採用</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">あくび</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">96.5%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">使用ターンに相手をねむけ状態にし、次のターン終了時に眠る。交代を強要する</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ステルスロック</strong></td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">92.7%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">相手の場全体に設置技。交代のたびに固定割合ダメージ</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">ふきとばし</td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">64.4%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">控えがいる相手をランダムに交代させ、設置ダメージへ繋げる</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">なまける</td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">37.2%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2回復。持久戦の耐久力を底上げ</td></tr>
<tr style="background:#fafafa"><td style="padding:8px 12px;border:1px solid #cbd5e1">まもる</td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">4.0%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">たべのこし等の回復量を稼ぐ補助技</td></tr>
<tr><td style="padding:8px 12px;border:1px solid #cbd5e1">ほえる</td><td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:20px;height:20px"></td><td style="padding:8px 12px;border:1px solid #cbd5e1">-</td><td style="padding:8px 12px;border:1px solid #cbd5e1">2.0%</td><td style="padding:8px 12px;border:1px solid #cbd5e1">ふきとばしと同枠の強制交代技</td></tr>
</table></div>

じしん・あくび・ステルスロックの3技がほぼ固定採用で、残り1枠をふきとばし（採用率64.4%）となまける（37.2%）が分け合う構成が中心です。攻撃技はじしん1本のみで、あくび・ステルスロックで相手の選出とテンポを崩す役割が明確です。

## 主な型

**性格採用率: わんぱく 63.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">型1：ふきとばし型（H32-B2-D32）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.9%）<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-B2-D32<br>
<strong>持ち物:</strong> オボンのみ（72.5%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック<br>
・ふきとばし
</div>
</div>
</div>

EV採用率1位（23.3%）の型です。H215・B154・D124の並びで両耐久をバランスよく確保し、ふきとばしで交代を強制してステルスロックのダメージを稼ぎます。

**強み:**

ふきとばしで相手の選出を乱しながらステルスロックの被害を広げられるため、相手パーティ全体への負荷が大きくなります。D32振りで、後述の型2（D2振り）よりも特殊アタッカーの一致技を受けやすい配分です。

**弱み:**

ふきとばしはランダム交代のため、狙った相手を場に出せません。相手が1体しか残っていない終盤は効果が薄れます。

---

**性格採用率: わんぱく 63.8%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">型2：ぼうぎょ特化型（H32-B32-D2）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> すなおこし（99.9%）<br>
<strong>性格:</strong> わんぱく<br>
<strong>EV:</strong> H32-B32-D2<br>
<strong>持ち物:</strong> オボンのみ（72.5%）
</div>
<div>
<strong>技構成:</strong><br>
・じしん<br>
・あくび<br>
・ステルスロック<br>
・なまける
</div>
</div>
</div>

EV採用率2位（16.3%）の型です。B187まで伸ばして物理アタッカーへの耐性を最大化し、なまけるで回復しながら居座ります。

**強み:**

B187は型1のB154より高く、物理技の確定数を1回分後ろにずらせる場面があります。なまけるを採用することで回復量が上がり、長期戦での居座り性能が高まります。

**弱み:**

D94（型1のD124より低い）で特殊アタッカーへの耐性が下がります。なまけるは回復に専念する分、その1ターンはじしん・あくび・ステルスロックのいずれも使えず相手に自由行動を与えるため、後続への負荷をかけるテンポが型1より遅くなります。

---

## データ分析：技構成の役割分担とEV採用率の分布

カバルドンは攻撃技がじしん1本のみで、残り3枠が「あくび・ステルスロック」固定＋「ふきとばし／なまける」の選択という構成に採用が集中しています。EV採用率でも1位（H32-B2-D32、23.3%）と2位（H32-B32-D2、16.3%）の合計で約4割を占め、両耐久のどちらに厚く振るかで型が分かれる一方、H32は全上位個体で共通しています。

技採用率ではふきとばし（64.4%）となまける（37.2%）が同じ4枠目を争いますが、両者は役割が異なります。ふきとばしは相手を強制的に入れ替えて積み技やステータス変化をリセットしつつステルスロックのダメージを稼ぐ攻めの選択、なまけるは自分のHPを回復して居座り時間を延ばす守りの選択です。採用率がふきとばし側に偏っているのは、カバルドン自体の耐久（H215・B154以上）がすでに高く、回復技より相手の選出テンポを崩す方が対面数を稼ぎやすいと判断されているためと読み取れます。

## 苦手なポケモン

使用率上位のうち、代表的な型が変わっても一貫してカバルドンが不利になる相手を挙げます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ボーマンダナイト採用率98.0%でほぼメガ前提。じしん（採用率99.3%）はひこう複合により無効。メガボーマンダの主力すてみタックル（採用率73.4%）は確定3発で、こちらは攻め手を欠いたまま後手に回ります</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ガブリアス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは等倍で通り確定3発ですが、最大打点となるげきりん（採用率27.3%）も確定3発で、後手に回るため先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは確定3発で並びますが、アシレーヌの主力うたかたのアリア（採用率92.6%、みず×2）も確定3発。後手に回るため先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">グソクムシャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">グソクムシャナイト採用率98.9%でほぼメガ前提。素早さ上はS67がメガグソクムシャのS60（メガ進化後の値）を上回り先手を取れますが、であいがしら（採用率83.0%）で繰り出し直後に先制されるリスクがあり実質先手が確定しません。じしんは確定5発と決め手を欠き、相手の主力アイアンヘッド（採用率76.0%）は確定3発です</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">セグレイブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは確定3発止まりの一方、セグレイブの主力つららおとし（採用率43.3%、こおり×2）は確定2発。後手に回るため先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは確定3発止まりの一方、マスカーニャの主力トリプルアクセル（採用率90.1%、くさ×2）は確定2発。後手に回るため先に押し切られます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大打点となるウッドハンマー（採用率26.7%、くさ×2）が確定1発。後手に回るこちらは反撃する間もなく落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギャラドス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこう複合により無効。ギャラドスの主力パワーウィップ（採用率67.3%、くさ×2）は確定3発ですが、攻め手を持たないこちらは後手に回るしかありません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは確定2発で並びますが、イダイトウの主力ウェーブタックル（採用率96.5%、みず×2）も確定2発。後手に回るため先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこう複合により無効。メガリザードンYの最大打点となるオーバーヒート（採用率22.7%）は確定2発で、攻め手を持たないこちらは後手のまま受け続けることになります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは確定3発で並びますが、アローラキュウコンの主力ふぶき（採用率69.1%、こおり×2）も確定3発。後手に回るため先に押し切られます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは特性ふゆうにより無効。ウォッシュロトムの主力ハイドロポンプ（採用率97.1%、みず×2）は確定3発ですが、攻め手を持たないこちらは後手に回るしかありません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんは特性ふゆう（100%採用）により無効。サザンドラはあくのはどう（採用率98.3%）に加えりゅうせいぐん（採用率95.7%）も併せ持ち、こちらは攻め手を持たないため後手に回るしかありません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんはひこう複合により無効。カイリューの最大打点となるりゅうのはどう（採用率24.9%）は確定5発ですが、攻め手を持たないこちらは後手に回るしかありません</td>
</tr>
</tbody>
</table>
</div>

大半の相手にS67のカバルドンは後手に回ります。みず・くさ・こおりの弱点技を持つアシレーヌ・ゴリランダー・セグレイブ・アローラキュウコン・ウォッシュロトムに加え、じしんが無効になる相手が2系統存在します。メガボーマンダ・ギャラドス・カイリュー・メガリザードンYはひこうタイプを併せ持つため無効、サザンドラ・ウォッシュロトムは特性ふゆう（サザンドラはふゆう100%採用）によりじめん技を受け付けません。一方ガブリアス・マスカーニャは等倍打点は通るものの相手の火力・耐久の方が上回り、後手からのじしんでは確定数負けします。メガグソクムシャは素早さ上はカバルドンが先手を取れますが、であいがしら（採用率83.0%）で繰り出し直後に先制されるリスクがあり、後続のふいうち（採用率49.3%）にも警戒が必要で、実質的に先手が確定しない相手です。

対策としては、じしんが無効になる相手（メガボーマンダ・ギャラドス・カイリュー・メガリザードンY・ひこう複合4体／サザンドラ・ウォッシュロトム・ふゆう2体）にはカバルドン単体で攻め合わず、ステルスロック＋あくびで足止めしてから別の対面処理役に選出を譲るのが基本です。特にひこう複合4体は同時に選出されやすいので、こおり・いわ・でんき技持ちの後続を用意しておくと選出圧を下げられます。

## 得意なポケモン

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ルカリオ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ルカリオナイトZ採用率93.7%でほぼメガ前提。後手に回りますが、メガルカリオの主力ラスターカノン（採用率78.8%）は確定3発なので受け切り、こちらのじしん（はがねタイプへの打点）は確定2発で返り討ちにできます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、ブリジュラスの主力ラスターカノン（採用率75.1%）は確定5発と伸び悩み、こちらのじしんは確定4発で先に押し切れます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、エースバーンの主力とびひざげり（採用率89.0%）は確定2発なので受け切り、こちらのじしん（ほのおタイプへの打点）は確定1発で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、オオニューラの主力インファイト（採用率99.4%）は確定3発なので受け切り、こちらのじしんは確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、ラウドボーンの主力フレアソング（採用率99.4%）は確定4発なので受け切り、こちらのじしんは確定3発で先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、パーモットの主力れいとうパンチ（採用率59.2%）は確定3発なので受け切り、こちらのじしんは確定1発で先に沈められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イエッサン(オス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">35位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">後手に回りますが、イエッサンの主力ワイドフォース（採用率99.4%）は確定3発なので受け切り、こちらのじしんは確定2発で先に沈められます</td>
</tr>
</tbody>
</table>
</div>

得意な相手は全てはがね・かくとう・ほのお・エスパー等じしんが等倍以上の打点になる一方、相手の主力技がカバルドンの高耐久（型1はB154・D124、型2はB187・D94）を上回れない組み合わせに集約されています。いずれも後手からのじしんで確定数を稼ぐ形であり、先手を取って有利になっているわけではない点は苦手な相手と共通しています。

## 同居率・パートナー（TOP10）

M-6でカバルドンと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
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
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ" loading="lazy">
    <div class="name">ルカリオ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" loading="lazy">
    <div class="name">サーフゴー</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" loading="lazy">
    <div class="name">マスカーニャ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

同居率TOP10にはボーマンダ・ガブリアス・セグレイブ・マスカーニャなど環境上位の攻撃的なポケモンが多く並びます。あくび・ステルスロックで相手の選出とテンポを崩すカバルドンの起点作りと、火力で押し切るアタッカーの組み合わせが構築として選ばれやすいことがうかがえます。

## まとめ

カバルドンはM-6シーズン使用率5位です。すなおこし・高耐久・あくび＋ステルスロックの設置コンボで相手の選出とテンポを崩す役割が明確な一方、素早さ実数値67は環境上位の多くに劣るため後手からの立ち回りが前提になります。苦手表に挙がったみず・くさ・こおり技持ちや高火力アタッカーへは後手を強いられるため、対策のうえで選出判断をすることが重要です。

<p style="font-size:0.9em;color:#64748b">関連記事：<a href="/blog/salamence-analysis-m6/">ボーマンダ考察（M-6）</a>、<a href="/blog/golisopod-analysis-m6/">グソクムシャ考察（M-6）</a>、<a href="/blog/garchomp-analysis-m5/">ガブリアス考察（M-5）</a></p>
