---
title: '【ポケモンチャンピオンズ】カビゴン考察 M-2 使用率48位 型別採用率と耐久型の立ち回り'
description: 'M-2シングルバトルで使用率48位のカビゴンを徹底分析。HP160・特性あついしぼうでほのお／こおりを半減する高耐久を軸に、AB物理型・HD特殊受け型の構築を解説。じしん64%・あくび39%など実データの技採用率、苦手なかくとう勢への対策まで紹介します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-snorlax-m2.png'
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
  <img src="/images/pokemon/pokemon-0143-00.webp" alt="カビゴン" />
  <div>
    <h2 style="margin:0 0 8px">カビゴン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">48位</strong>　特性: <strong>あついしぼう 93.0%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、カビゴンは**使用率48位**。HP160・とくぼう110という高い耐久と、特性**あついしぼう**（採用率93.0%）でほのお・こおり技を半減する受け性能を軸にした、環境屈指のタフなノーマルアタッカーです。

ノーマル単タイプで弱点は**かくとう**1つのみ。あついしぼうでほのお・こおりも半減するため、環境の特殊アタッカーの多くを後出しから受け止められます。じしん（採用率64.0%）で弱点を突けないはがね・どく・でんきへ打点を持ち、あくび（39.3%）で起点回避と流しを兼ねる立ち回りが基本です。

---

## なぜM-2でカビゴンが採用されるのか

### 1. HP160＋D110で特殊アタッカーを後出しから受ける

カビゴンの最大の強みは桁外れのHP160と、とくぼう110による特殊耐久です。しんちょう（性格採用率30.2%）でHD全振り（H32 D32）にすればHP実数値267・とくぼう実数値178に達し、環境上位の特殊アタッカーの一致技を1発で受けて反撃に回せます。

さらに特性あついしぼうがほのお・こおりを**半減**するため、リザードン（5位）のかえんほうしゃ、ゲッコウガ（28位）のれいとうビーム（採用率89.6%）といったほのお・こおりの特殊打点に対し、無振りでも受け出しが利きます。ノーマル単で弱点がかくとう1つしかない点も後出しの安定性を高めています。ただしかくとう技を持つ相手には弱点を突かれるため、後出しが安定するのは攻撃タイプがかくとう以外の場合に限られます。

### 2. じしん64%で弱点を突けないタイプへ打点を確保する

ノーマル技だけでは、ゴーストに無効・はがねに半減と通らない相手が出ます。これを補うのが採用率64.0%の**じしん**です。はがね・どく・でんき・ほのおへ等倍以上で通り、相性で受けに来るブリジュラス（2位・はがね/ドラゴン）やキラフロル（15位・いわ/どく）に有効打を入れられます。

れいとうパンチ（37.4%）・ヒートスタンプ（24.8%）といったサブウェポンも採用され、じしんと合わせてくさ・ひこう・はがねまで範囲を広げられます。

### 3. あくび39%で起点を作り、積みアタッカーを流す

あくび（採用率39.3%）は相手を眠り状態にして交代を強制する変化技です。高耐久で居座りながらあくびを撒くことで、つるぎのまい・ちょうのまいなどの積みアタッカーに対し**積みの起点を与えず流す**動きが取れます。眠らせた隙に自分の能力を整える・後続に有利な対面を作るといった盤面操作が、低速でも仕事を作れる理由です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:100%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">160</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:68.75%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">110</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.6%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40.6%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:68.75%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">110</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:18.75%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">30</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">540</span>
  </div>
</div>

HP160・とくぼう110で特殊方向は無振りでも厚く、ぼうぎょ65は振り（HB型）で補います。こうげき110はノーマルアタッカーとしては高水準。すばやさ30は環境上位のほとんどに後攻するため、**耐えてから殴る・あくびで流す**という受け攻めの立ち回りが前提になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ノーマル" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">特性による半減</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

ノーマル単タイプの弱点は**かくとう（×2）のみ**で、ゴースト技を無効化します。さらに特性あついしぼうがほのお・こおりを×0.5に半減するため、実質的に苦手な攻撃タイプはかくとうにほぼ絞られます。タイプ受けの安定性は環境でもトップクラスです。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じしん</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">100</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">64.0%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ノーマル技が通らないはがね・どく・でんきへの打点。最多採用の補完技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">39.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次のターンに相手を眠らせ交代を強制。積みアタッカーの起点回避・流しに</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じばく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">200</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>37.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用後に自分がひんし。役割を終えた後の高火力で道連れ的に1体処理</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>れいとうパンチ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>37.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ドラゴン・ひこう・じめん・くさへの打点。じしんが通らないひこう勢に刺さる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ヒートスタンプ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">可変</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が軽いほど高威力。はがね（ハッサム等）への打点。重さ460kgのカビゴンと相性良</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>すてみタックル</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">高威力の一致技。反動1/3。AB物理型のメインウェポン</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じわれ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">一撃</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一撃必殺（命中30）。耐久型では崩しにくい高耐久・受け対面の打開択</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねむる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">HP全回復＋状態異常回復。カゴのみと合わせて即起き・居座りに</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>のしかかり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">85</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30%でまひ。反動がなく、HD型でも撃てる安定したノーマル一致技</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">攻撃を1ターン防ぐ。たべのこし回復・あくびのターン稼ぎと噛み合う</td>
</tr>
</tbody>
</table>
</div>

---

## 主要型の解説

型①・型②は性格分布（いじっぱり／しんちょう）と振り分布（AB／HD）を指標としています。

### 型1: AB物理アタッカー型（いじっぱり 45.3%）

**性格採用率: いじっぱり 45.3%**（AB物理型の指標。性格分布で最多。振りはAB+D 13.3%が最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0143-00.webp" alt="カビゴン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">AB物理いじっぱり型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> あついしぼう（93.0%）<br>
<strong>性格:</strong> いじっぱり（A↑ C↓）<br>
<strong>EV:</strong> A32 B32（残り2をDかH。AB+D 13.3%が最多）<br>
<strong>持ち物:</strong> たべのこし / ヨプのみ
</div>
<div>
<strong>技構成:</strong><br>
・すてみタックル / のしかかり<br>
・じしん<br>
・れいとうパンチ / ヒートスタンプ<br>
・じばく / あくび
</div>
</div>
</div>

**強み:**

いじっぱりでこうげきを伸ばし、A実数値178からノーマル一致のすてみタックル（威力120）と補完のじしんで広く攻める型です。HD型と違いB方向にも振るため、いかくの入りにくい物理アタッカーとも撃ち合えます。じばくを採用すれば、役割を終えた後に威力200で1体を確実に持っていく詰め筋を持てます。

**弱み:**

HD型に比べて特殊耐久の補強がB方向に分散するぶん、ウォッシュロトム・ゲンガーなど高速特殊アタッカーの連打には居座りにくくなります。すばやさ30で先制を取られる前提のため、あくびを採用しないとつるぎのまい持ちの起点にされやすい点も物理型の弱みです。

---

### 型2: HD特殊受け型（しんちょう 30.2%）

**性格採用率: しんちょう 30.2%**（HD型の指標。性格分布でいじっぱりに次ぐ2番手。振りはHD+B 10.7%が最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0143-00.webp" alt="カビゴン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HD特殊受けしんちょう型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> あついしぼう（93.0%）<br>
<strong>性格:</strong> しんちょう（D↑ C↓）<br>
<strong>EV:</strong> H32 D32（残り2をB。HD+B 10.7%が最多）<br>
<strong>持ち物:</strong> たべのこし / カゴのみ
</div>
<div>
<strong>技構成:</strong><br>
・のしかかり<br>
・じしん<br>
・あくび / まもる<br>
・ねむる / じわれ
</div>
</div>
</div>

**強み:**

しんちょうHD全振りでHP実数値267・とくぼう実数値178となり、あついしぼうのほのお・こおり半減と合わせて特殊アタッカーをほぼ完封します。あくびで起点回避しつつたべのこしで回復、ねむる＋カゴのみで状態異常を踏み倒して長く居座れるのがこの型の主眼です。物理型では反動を負うすてみタックルの代わりに、反動のないのしかかりで安定してダメージを刻みます。

**弱み:**

物理型と違いB方向が薄いため、ガブリアスのじしん・ドドゲザンのドゲザンなど高火力の物理技で削られやすいです。決定力もこうげき無振り寄りで低く、じわれの一撃必殺に頼らないと高耐久の相手を突破しにくいのも物理型にはない弱みです。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、カビゴンと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ノーマル単で弱点はかくとうのみ、あついしぼうでほのお・こおりも半減するため特殊アタッカーには強い一方、すばやさ30で後攻が確定し、こうげきの高いかくとう勢・物理勢には上から弱点や高火力を押し付けられる点に注意してください。

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
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技はノーマル等倍だがあついしぼうで×0.5に抑え後出しから受ける。すてみタックル等のノーマル一致技で等倍の反撃が入り、ソーラービーム型なら被弾も小さく受け回せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプ（98.5%）はノーマル等倍、10まんボルト（56.8%）も特殊でHD型なら受け切れる。かくとう技を持たず、じしんがでんき/みずに×2（でんき2×みず1）で通り反撃できる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（71.1%）はノーマルに無効、ヘドロウェーブ（81.7%）も等倍でHD型なら受け、じしんがゴースト/どくに×2（ゴースト1×どく2）で通る。ただしS110で上を取られ、きあいだま（採用率37.4%・かくとう×2）採用個体には弱点を突かれるため安定はしない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ブリジュラス（2位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">特殊技はHD型で受け切れるが、じしんは×2（はがね2×ドラゴン1）で通るものの一撃には足りず、相手のラスターカノン等で削り合いになる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">▲ 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99%）がA130から高火力で通り、HD型はB方向が薄く2発圏。れいとうパンチは×4（こおり：ドラゴン2×じめん2）で通るが後攻のため先に大ダメージを受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率72%）が弱点かくとう×2。てきおうりょく補正もあり高耐久でも一撃〜二撃で崩される</td>
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
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">苦手理由</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">対策</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99%）がA130から通り、HD型は防御が薄く2発で落とされる。すばやさ30で先手も取れない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこう・ふゆうのポケモン（アーマーガア等）を同伴し受け先を分ける。れいとうパンチ採用個体で削っておき、後続のこおり・フェアリーで処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（採用率72%）が弱点かくとう×2。てきおうりょくの高火力で高耐久でも崩される</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくびで眠らせて流すか、ひこう・エスパー・フェアリー（ピクシー等）でかくとう半減枠から受ける。じしん採用個体ではがね側に×2で反撃</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0903-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">オオニューラ（33位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（98.6%）が弱点かくとう×2。A130・S120で上から確実に弱点を突かれる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうを半減するひこう・エスパー・フェアリーで受け、どく複合に刺さるじめん技（同伴のガブリアス等）で処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">けたぐり（採用率17.6%）採用個体は弱点かくとう×2。ふいうち（99%）の先制でHD型でも削られ、A135の物理を受け続けにくい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（あく/はがねに等倍×2）で弱点を突けるじめん枠を残す。けたぐり非採用個体は受け切れるため、削れ具合を見て役割を判断する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン（同居率上位）

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0952-00.webp" alt="スコヴィラン">
    <div class="name">スコヴィラン</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ/ほのお。くさ技でじめん・みずへ、ほのお技でカビゴンが等倍のはがね・むしへ打点を広げる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0479-01.webp" alt="ヒートロトム">
    <div class="name">ヒートロトム</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき/ほのお。ふゆうでガブリアスのじしんを無効化し受け先を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴン。フェアリー・ノーマル・ほのお等を半減し特殊耐久を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速地面枠。カビゴンが後攻で取りこぼす相手に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず/フェアリー。かくとうを半減しドラゴン無効。弱点補完に優秀</div>
  </div>
</div>

**パーティ構成の基本方針:**

カビゴンは特殊方向を1枚で受けられる反面、すばやさ30で後攻が確定し、かくとう・高火力物理が明確な穴になります。残り5体で以下の役割を補います。

1. **かくとう対策**: ひこう・エスパー・フェアリー（アシレーヌ・ピクシー等）でルカリオ・オオニューラを受ける枠
2. **じめん（じしん）対策**: ひこう・ふゆうのポケモン（ヒートロトム等）でガブリアスのじしんを無効化する枠
3. **高速打点**: ガブリアス等の高速アタッカーで、後攻のカビゴンが取りこぼす相手を上から処理
4. **物理受けの分担**: HD型を採用する場合、ブリジュラス等のはがね枠で物理も含めた受けを分散

---

## データ分析①：特性あついしぼうが受け範囲をどう広げるか

あついしぼうが受け範囲をどれだけ広げるかを、環境上位の特殊アタッカーを攻撃タイプ別に並べて定量化します。

| 攻撃タイプ | ノーマルのタイプ相性 | あついしぼう適用後 | 該当する環境上位 |
|---|---|---|---|
| ほのお | ×1（等倍） | **×0.5** | リザードン(5)・ウルガモス(18)・マフォクシー(25)・ラウドボーン(29) |
| こおり | ×1（等倍） | **×0.5** | ゲッコウガ(28)のれいとうビーム・各種こおりサブ |
| エスパー | ×1（等倍） | ×1 | マフォクシー(25)・スターミー(20) |
| かくとう | **×2** | ×2 | ルカリオ(9)・オオニューラ(33) |

数値上のポイントは、**等倍だったほのお・こおりが半減になることで「2発で落とされる」ラインが「3発以上耐える」ラインに動く**ことです。例えばウルガモスのほのお技やゲッコウガのれいとうビームは本来ノーマルに等倍で通りますが、あついしぼうで半減されるとHD型は余裕を持って後出しでき、あくびや反撃に1ターン使える猶予が生まれます。

逆に表が示すのは、弱点のかくとう（×2）は特性でも軽減されないという事実です。採用率93%があついしぼうに集中している以上、ほのお・こおり受けは堅い一方でかくとう打点だけは抜け道がなく、苦手なポケモン対策の優先順位がそのままかくとう対策に直結します。めんえき（6.2%）は状態異常を防ぐ特性ですが、採用率93%のあついしぼうがほのお・こおり半減で受け範囲を広げる以上、受け運用では多数派のあついしぼうが優位です。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">AB物理型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">いじっぱり 45.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">いじっぱり</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">すてみタックル・じしん・れいとうパンチ・じばく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理にも撃ち合える。じばくで詰め筋を持つ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊受けの安定感はHD型に劣る</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう 30.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しんちょう</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">のしかかり・じしん・あくび・ねむる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊アタッカーをほぼ完封。長く居座る</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">B方向が薄く高火力物理に弱い。決定力不足</td>
</tr>
</tbody>
</table>
</div>

**総評:**

カビゴンはHP160・とくぼう110とあついしぼうを軸に、環境の特殊アタッカーを1枚で受け止められる耐久ポケモンです。ノーマル単で弱点はかくとうのみ、ほのお・こおりも特性で半減するため、リザードン・ゲンガー・ウォッシュロトムといった上位特殊勢への後出しが安定します。

一方ですばやさ30で後攻が確定し、ガブリアスのじしんやルカリオ・オオニューラのかくとう技という明確な穴を抱えます。これらはあくびでの流しとパーティ単位のかくとう・じめん受け枠でケアし、じしん・れいとうパンチで弱点を突けるタイプへ打点を通すのが基本戦術です。受けの広さを活かせる構築に組み込めるかどうかが、使用率48位というカビゴンを機能させる鍵になります。

---

## 関連記事

- [天敵となるかくとうアタッカー ルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [同居率上位の高速地面枠 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同じノーマルアタッカー ガルーラのM-2考察](/blog/kangaskhan-analysis-m2/)
</content>
</invoke>
