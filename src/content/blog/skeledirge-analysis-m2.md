---
title: '【ポケモンチャンピオンズ】ラウドボーン考察 M-2 使用率29位 てんねん耐久型の採用率と立ち回り'
description: 'M-2シングルバトルで使用率29位のラウドボーンを分析。特性てんねん99.2%で積みアタッカーを無力化し、なまける95.6%・おにび76.4%で居座る耐久型を解説。HB/HD振りの違い、てんねんが刺さるルカリオやミミロップ、苦手なみず・じめんへの対策まで実データで紹介します。'
pubDate: '2026-06-04'
draft: true
heroImage: '../../assets/hero-skeledirge-m2.png'
---

<style>
.poke-header { display:flex; align-items:center; gap:16px; margin:20px 0; }
.poke-header img { width:96px; height:96px; }
.build-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
.item-icon { display:inline-block; width:32px; height:32px; vertical-align:middle; margin-right:4px; object-fit:cover; }
.partner-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(120px,1fr)); gap:12px; margin:16px 0; }
.partner-card { text-align:center; padding:8px; border:1px solid #e2e8f0; border-radius:8px; }
.partner-card img { width:56px; height:56px; display:block; margin:0 auto 4px; }
.partner-card .name { font-size:0.75rem; font-weight:bold; }
.partner-card .rate { font-size:0.7rem; color:#666; }
.type-row { display:flex; align-items:center; gap:8px; margin:8px 0; }
</style>

<div class="poke-header">
  <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" />
  <div>
    <h2 style="margin:0 0 8px">ラウドボーン</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px" />
      <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">29位</strong>　特性: <strong>てんねん 99.2%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ラウドボーンは**使用率29位**。特性は**てんねん（採用率99.2%）**にほぼ統一されており、相手の能力ランク上昇を無視して殴る耐久型として運用されています。

ラウドボーンの核は**てんねん**です。つるぎのまい・りゅうのまい・めいそうといった積み技でランクを上げてくる相手に対し、上昇分を無視してダメージを計算するため、積みアタッカーの居座りを単体で止められます。さらに**なまける（採用率95.6%）**で削られたHPを回復し、**おにび（76.4%）**で物理アタッカーの火力を半減させる、受け回し前提のポケモンです。

---

## なぜ今ラウドボーンが使われるのか

### 1. てんねんで積みアタッカーを単体で止める

ラウドボーンの最大の価値は**特性てんねん**にあります。相手の能力ランク上昇を無視してダメージ計算を行うため、つるぎのまいで全抜きを狙うミミロップ・ハッサム・ルカリオや、りゅうのまいで詰めにくるギャラドスに対し、積みターンを与えても火力が伸びません。

特に**かくとう技を無効化（ゴーストタイプ）**できる点が噛み合っており、つるぎのまい＋インファイトで崩しにくるルカリオ・ミミロップのかくとう技を受け付けません。積みエースを「積ませてから無視して受ける」という、てんねん持ちにしかできない止め方ができます。

### 2. なまける＋おにびで物理アタッカーに居座る

**なまける（採用率95.6%）**は最大HPの1/2を回復する技です。これにより削り合いを長期化させ、相手のPPや交代機会を枯らします。

さらに**おにび（76.4%）**を入れることで、物理アタッカーのこうげきを半減し、やけどの定数ダメージも与えられます。てんねんで積みを無視しつつ、おにびで素の火力まで削るため、つるぎのまいを積んだ物理アタッカーが二重に機能停止します。ぼうぎょ種族値100・HP104の高い物理耐久と合わせ、物理受けとして安定します。

### 3. フレアソング＋たたりめでアタッカーも兼ねる

攻撃面は**フレアソング（採用率99.6%）**がほぼ確定枠です。威力80のほのお一致技で、とくこう1段階上昇の追加効果を持つため、居座りながら自分の火力を上げられます。

サブには**シャドーボール（54.9%）**と**たたりめ（32.4%）**を採用。たたりめは相手が状態異常のとき威力が2倍（65→130相当）になるため、おにびのやけど・あくびのねむりと組み合わせて高火力のゴースト打点になります。とくこう種族値110を活かし、受けるだけでなく削り役も担えるのが他の物理受けとの差別点です。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:52%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">104</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:50%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#2563eb">100</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:55%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#dc2626">110</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:37.5%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">75</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:33%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">66</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">530</span>
  </div>
</div>

HP104・ぼうぎょ100の物理耐久が高く、おにびと合わせて物理アタッカーを強く受けられます。一方とくぼう75はHPの高さで底上げしても物理ほど硬くなく、特殊高火力には押し切られやすいのが弱点です。すばやさ66は環境では低速の部類で、ほぼ後攻前提の立ち回りになります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-09-fire.png" alt="ほのお" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ほのお" />
  <img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="ゴースト" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（2倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（0.5倍）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px">
      <span><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">みず</span>
      <span><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">じめん</span>
      <span><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">いわ</span>
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ほのお</span>
      <span><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">くさ</span>
      <span><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">こおり</span>
      <span><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">どく</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-08-steel.png" alt="はがね" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">はがね</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ノーマル</span>
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
    </div>
  </td>
</tr>
</tbody>
</table>
</div>

ゴーストタイプで**ノーマル・かくとうを無効化**できるのが守りの軸です。これにより、つるぎのまいからインファイト・とびひざげりで崩すルカリオ・ミミロップのかくとう技が一切通りません。一方で弱点はみず・じめん・いわ・ゴースト・あくの5タイプ。環境上位に多いみず（アシレーヌ・ウォッシュロトム・ゲッコウガ）とじめん（ガブリアス・カバルドン）が弱点に並ぶため、これらへの引き先をパーティで用意する前提になります。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フレアソング</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">99.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお一致技。使用後とくこう1段階アップ。居座りながら火力を伸ばせる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>なまける</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">95.6%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの1/2を回復。受け回しの軸。ほぼ確定枠</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>おにび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>76.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をやけど状態に。物理火力半減＋定数ダメージ。たたりめの威力上昇トリガーも兼ねる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>シャドーボール</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>54.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴースト一致技。状態異常に依存せず安定して撃てる。とくぼう低下の追加効果</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>たたりめ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">65（状態異常時130）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">32.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手が状態異常だと威力2倍。おにび・あくびと噛み合うゴースト打点</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次ターンに相手をねむり状態。交代を強要し受け回しを補助</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>だいちのちから</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">90</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお技を半減するはがね・いわへの打点。採用率は低い</td>
</tr>
</tbody>
</table>
</div>

フレアソング・なまけるの2枠はほぼ固定で、残り2枠を「おにび＋シャドーボール」または「おにび＋たたりめ」で埋める構成が主流です。シャドーボールは相手の状態に依存せず安定したゴースト打点になるのに対し、たたりめはおにび・あくびで状態異常を撒く構成と組み合わせて威力2倍を狙う択になります。

---

## 主要型の解説

EV振りはHB型（ずぶとい 67.3%）とHD型（おだやか 21.9%・ひかえめ 8.0%）の2系統が主流です。

### 型1: HB物理受け型（最多採用）

**性格採用率: ずぶとい 67.3%**（ぼうぎょ補正。EVもHB振りが最多で22.5%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">てんねんHBずぶとい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てんねん<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（最多型。余り2はD）<br>
<strong>持ち物:</strong> たべのこし / オボンのみ / カシブのみ
</div>
<div>
<strong>技構成:</strong><br>
・フレアソング<br>
・なまける<br>
・おにび<br>
・シャドーボール / たたりめ
</div>
</div>
</div>

**強み:**

ぼうぎょに振り切り、てんねん＋おにびで物理アタッカーを完全に止める型です。HP104・ぼうぎょ100にずぶとい補正とHB振りを重ねるため、ルカリオ・ミミロップ・ハッサムといったつるぎのまい物理エースを、積みを無視しつつおにびで火力を削って受け切れます。かくとう技を無効化するゴーストタイプも噛み合い、これらの主力かくとう技そのものが通りません。

たべのこし（採用率34.0%）採用ならなまけると合わせて回復量が増し、居座り性能が上がります。オボンのみ（25.8%）は不意の高乱数に対する保険、カシブのみ（13.7%）はゴースト弱点を1回半減してミミッキュのかげうち等を耐える択になります。

**弱み:**

HBに寄せるため特殊耐久が手薄で、ウォッシュロトムのハイドロポンプ（採用率98.5%）やサザンドラのあくのはどう（98.5%）など弱点特殊技で一気に削られます。HD型と異なり特殊アタッカー全般を受けにくいのがこの型固有の弱点です。

---

### 型2: HD特殊受け型（2番目に多い構成）

**性格採用率: おだやか 21.9%**（とくぼう補正。EVはHD振りが計約16%）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:48px;height:48px">
  <strong style="font-size:1.05em">てんねんHDおだやか型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> てんねん<br>
<strong>性格:</strong> おだやか（D↑ C↓）<br>
<strong>EV:</strong> H32 D32（余り2はBまたはS）<br>
<strong>持ち物:</strong> たべのこし / オボンのみ
</div>
<div>
<strong>技構成:</strong><br>
・フレアソング<br>
・なまける<br>
・おにび<br>
・シャドーボール / たたりめ
</div>
</div>
</div>

**強み:**

HB型では受けにくい特殊アタッカーに寄せた型です。とくぼう75はHB型のままだと特殊高火力に押し切られますが、おだやか＋HD振りで底上げすることで、弱点でない特殊技（リザードンのかえんほうしゃ＝ほのお半減、サザンドラのりゅうせいぐん＝等倍など）を受けやすくなります。ただしサザンドラのあくのはどう（採用率98.5%）のような弱点特殊技はHD振りでも×2のため受け切れません。ひかえめ（8.0%）採用個体はとくこう110を伸ばし、フレアソング・たたりめの削り役としての性能を上げています。

**HB型との使い分け:**

HB型がルカリオ・ハッサム等の物理つるぎのまいエースを止める枠なのに対し、HD型は特殊アタッカー側の受けに役割をずらした型です。相手の構築に物理エースが多いか特殊エースが多いかで選び分けます。ただしどちらの型も弱点はみず・じめん・あくで共通するため、引き先の用意は両型に必要です。

**弱み:**

物理方向の耐久がHB型に劣るため、おにびを入れる前のミミロップのインファイト（こちらに無効）以外の物理一致弱点技、たとえばマスカーニャのはたきおとす（あく×2）を受けると、HB型より大きく削られます。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

てんねんで積みを無視し、ゴーストでノーマル・かくとうを無効化する一方、すばやさ66で常に後攻になり、みず・じめん・あく弱点を突かれると受けが成立しません。使用率上位から相性がはっきり出る相手を有利・不利の両面で挙げます。

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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 超有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・しんくうは（かくとう）を無効、コメットパンチ・バレットパンチ（はがね）を半減。てんねんでつるぎのまいも無視。おにびで残る打点も削れる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">バレットパンチ・コメットパンチ（はがね）半減、インファイト（かくとう）無効、てんねんでつるぎのまい無視。ただしはたきおとす（あく・採用率53.6%）は×2弱点で持ち物も落とされる点に注意</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミロップ（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">◎ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト・とびひざげり・マッハパンチ（かくとう）無効、ねこだまし（ノーマル）も無効。てんねんでつるぎのまい無視。トリプルアクセル（こおり）はほのお半減で通らず決定打にならない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">リザードン（5位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かえんほうしゃ等のほのお技もソーラービーム（採用率61.0%）も半減。おにび＋なまけるで居座れる。ただし弱点を突く打点はこちらにない</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ガブリアス（1位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2弱点。S102で先手を取られ、なまけるが追いつかず崩される</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ウォッシュロトム（22位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ハイドロポンプ（みず・採用率98.5%）が×2弱点。相手もおにび（80.6%）持ちでこちらのフレアソングを火傷で削られ、撃ち合いで突破される</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲッコウガ（28位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なみのり（みず）・あくのはどう（あく）がともに×2弱点。S122で先手を取られ、高火力特殊で受けが成立しない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（ゴースト・採用率71.1%）が×2弱点。S110で先手、たたりめ（27.5%）持ちにはやけど自滅も狙われる</td>
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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率99.2%）が×2弱点。S102で先手を取られ、おにびでこうげきを半減してもじしんの一撃が重く押し切られやすい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしんを無効化するひこうタイプ（アーマーガア）や、みず・こおり技でガブリアスに弱点を突けるアシレーヌを同伴し、ガブリアス対面で引いて受ける</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">カバルドン（7位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（98.0%）が×2弱点。なまける（53.2%）持ちで相互に回復し合う消耗戦になるが、フレアソング・ゴースト打点ともにカバルドンに等倍止まりで、高耐久を削りきれない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">くさ・みず技で弱点を突けるアシレーヌ・フシギバナを後投げし、じしんを受けつつ突破する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0658-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲッコウガ（28位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">なみのり（みず）・あくのはどう（あく）がともに×2弱点。S122で先手を取られ、高火力特殊で1〜2発圏内に入れられ受けが成立しない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">みず・あく技を半減するアシレーヌ（みず/フェアリー）で受け、ゲッコウガより速いマスカーニャ（S123）等で上から処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（採用率71.1%）が×2弱点。S110で先手を取られ、こちらのシャドーボールもゲンガーに×2で通る相互×2の撃ち合いだが、先手と火力で押し負ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">あくタイプのドドゲザン（ふいうちでゴーストに×2の先制打点）やサザンドラを後投げし、上から処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0908-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">マスカーニャ（3位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はたきおとす（あく・採用率57.6%）が×2弱点でたべのこし等の持ち物も落とされる。S123で先手を取られ、てんねんはあっても弱点物理で削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">マスカーニャのくさ技（トリックフラワー）を1/4に軽減するブリジュラスや、ほのお技で弱点を突けるリザードンを合わせて処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ">
    <div class="name">ゲッコウガ</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">高速みずアタッカー。ラウドボーンが苦手なじめん・いわ枠に上から打点</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス">
    <div class="name">カメックス</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みずタイプでじめん・いわ・ほのおを受け、弱点を補完</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">じめん枠で電気・岩に打点。ラウドボーンと弱点が分散する</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率4位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンでみずを半減し、ラウドボーンの苦手な特殊みずを受ける</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0003-00.webp" alt="フシギバナ">
    <div class="name">フシギバナ</div>
    <div class="rate">同居率6位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">くさ技でみず・じめん・いわに弱点を突き、ラウドボーンの天敵を逆に狩る</div>
  </div>
</div>

**パーティ構成の基本方針:**

ラウドボーンは物理アタッカーをてんねん＋おにびで止める受け駒です。弱点のみず・じめん・あくを補う引き先を必ず用意します。

1. **みず対策**: ブリジュラス（みず半減）やくさタイプのフシギバナでウォッシュロトムを受ける枠。れいとうビーム（採用率89.6%）持ちのゲッコウガには両者とも弱点を突かれるため、アシレーヌ等みず・あく両方を半減する枠で受ける
2. **じめん対策**: ひこうタイプ（アーマーガア）やくさ・みずタイプでガブリアス・カバルドンのじしんを受ける枠
3. **あく・ゴースト対策**: ゲンガー・マスカーニャに上から打点を持てるあく・ゴーストアタッカーを用意
4. **削り役との連携**: 同居率上位のゲッコウガ・マスカーニャなど高速アタッカーで、ラウドボーンが起点にした相手を上から処理

---

## データ分析①：たたりめは「状態異常前提」でしか採用価値が出ない

ラウドボーンのゴースト打点は**シャドーボール（採用率54.9%）**と**たたりめ（32.4%）**で割れています。両者の威力を、相手の状態で比較します。

| 技 | 相手通常時の威力 | 相手状態異常時の威力 | 一致補正後（×1.5・状態異常時） |
|---|---|---|---|
| シャドーボール | 80 | 80 | 120 |
| たたりめ | 65 | **130** | **195** |

たたりめは相手が状態異常でないと威力65で、一致補正込みでもシャドーボール（120）に大きく劣ります。一方、相手がやけど・ねむり等なら威力130に倍化し、一致補正込み195とシャドーボールの1.6倍に達します。

この差が、技構成の組み合わせを規定しています。たたりめ採用型は**おにび（76.4%）・あくび（13.8%）で状態異常を撒く前提**でなければ機能せず、単体では弱い技です。逆に状態異常を絡める動きが安定している構築なら、たたりめはシャドーボールを上回る決定力を出します。シャドーボール採用率が依然54.9%と過半を占めるのは、「状態異常を撒く前に殴る場面」や「相手が状態異常にならない構築」でも腐らない安定性が評価されているためで、確実性のシャドーボールと爆発力のたたりめという選択になっています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">採用率（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な役割</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HB物理受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ずぶとい 67.3%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ずぶとい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理つるぎのまいエースの止め</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">てんねん＋おにびで物理エースを完封</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊高火力に押し切られやすい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HD特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか 21.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊アタッカーの受け</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">弱点でない特殊技を広く受けられる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理耐久がHB型に劣る</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ラウドボーンは**てんねん**で積みアタッカーを単体で止め、**なまける・おにび**で居座る受け駒です。ゴーストタイプでノーマル・かくとうを無効化するため、つるぎのまい＋かくとう技で崩すルカリオ・ミミロップ・ハッサムに滅法強いのが最大の役割です。

一方、すばやさ66で常に後攻になり、弱点のみず・じめん・あくが環境上位（ガブリアス・カバルドン・ウォッシュロトム・ゲッコウガ・マスカーニャ）に集中するため、単体での受け範囲は限られます。これらへの引き先をパーティで用意できるかが採用の前提で、物理エースの多い構築に強く刺さる対策枠として使用率29位に位置しています。HB型かHD型かは、止めたいエースが物理か特殊かで選び分けるのが基本です。

---

## 関連記事

- [てんねんで止められる側 ルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [天敵となる使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [苦手なみず枠 ウォッシュロトムのM-2考察](/blog/rotom-wash-analysis-m2/)
