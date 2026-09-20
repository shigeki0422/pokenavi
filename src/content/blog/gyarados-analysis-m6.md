---
title: '【ポケモンチャンピオンズ】ギャラドス 考察 M-6 シーズン 使用率15位の非メガいかく型解説'
description: 'M-6シーズン使用率15位のギャラドスを考察。ギャラドスナイト採用率24.1%で非メガ運用が主流に転じた背景、みず/ひこうのタイプ相性、ゴツゴツメット/たべのこし型の型構成・実数値、苦手/得意ポケモンをデータで解説します。'
pubDate: '2026-09-20'
updatedDate: '2026-09-20'
heroImage: '../../assets/hero-gyarados-m6.png'
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
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" />
  <div>
    <h2 style="margin:0 0 8px">ギャラドス</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-10-water.png" alt="みず" style="width:44px;height:44px" />
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">15位</strong>　特性: <strong>いかく 99.8%</strong>
    </div>
  </div>
</div>

※本記事の使用率順位・技/持ち物/性格/EV等の詳細データは2026-09-10時点のスナップショットを使用しています。

M-6シーズンのギャラドスは使用率15位。みず/ひこうの複合タイプにいかくを持ち、りゅうのまいで積みながらパワーウィップ・たきのぼり・じしんで押し切るアタッカーです。持ち物採用率トップはゴツゴツメット（36.9%）とたべのこし（24.4%）で、メガ進化用のギャラドスナイト（24.1%）は3番手にとどまります。つまりM-6の主流は**非メガのいかく型**で、本記事のタイプ相性・耐久・技範囲の分析もこの非メガ形態を基準にします。

---

## ギャラドスの基本スペック

<div style="max-width:560px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:52%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">95</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:69%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">125</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:44%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">79</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:33%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:56%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">100</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:45%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">81</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:700;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">540</span>
  </div>
</div>

Aは125と高水準ですが、Sは81と中速止まりです。HP95・B79・D100とあわせ、耐久寄りのステータス配分に高いAを乗せた構成になっています。

### タイプ・弱点

<div class="type-row"><strong>タイプ：</strong><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:32px;height:32px"></div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px;border:1px solid #cbd5e1">無効</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-12-electric.png" alt="でんき" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:32px;height:32px"><img src="/images/types/type-06-bug.png" alt="むし" style="width:32px;height:32px"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:32px;height:32px"><img src="/images/types/type-10-water.png" alt="みず" style="width:32px;height:32px"><img src="/images/types/type-08-steel.png" alt="はがね" style="width:32px;height:32px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:32px;height:32px"></td>
</tr>
</tbody>
</table>
</div>

でんき×4が最大の弱点です。M-6上位ではパーモット（28位）のでんこうそうげき採用率85.1%、ウォッシュロトム（26位）のボルトチェンジ採用率88.7%が主な脅威になります。一方でじめんタイプの技を無効化できる点は、使用率1位のガブリアスのじしん（採用率67.6%）を受け出せる数少ない相手であることを意味します。ただしガブリアスは種族値S102でギャラドス（S81）より上を取りやすく、がんせきふうじ（採用率21.1%、いわ技でギャラドスに×2）も一定数採用されているほか、りゅうせいぐん・げきりんなどのドラゴン技は等倍で通ります。じしん一辺倒でなければ完全な受け出し先とは言えず、実際の検証でも技の組み合わせ次第で勝敗が分かれる相手です。

### 特性：いかく

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">特性</th>
  <th style="padding:8px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px;border:1px solid #cbd5e1">効果</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">いかく</td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:center">99.8%</td>
  <td style="padding:8px;border:1px solid #cbd5e1">登場した時、相手の攻撃を1段階下げる</td>
</tr>
</tbody>
</table>
</div>

いかくはほぼ全個体が採用しています。物理アタッカーとして場に出るたびに相手の物理アタッカーの火力を削げるため、りゅうのまいで積み始める前の一手として機能します。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">技名</th>
  <th style="padding:8px;border:1px solid #cbd5e1">タイプ</th>
  <th style="padding:8px;border:1px solid #cbd5e1">威力</th>
  <th style="padding:8px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px;border:1px solid #cbd5e1;text-align:left">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">パワーウィップ</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">120</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">67.3%</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">タイプ一致ではないくさタイプのカバー技。高威力で、カバルドン等のじめんタイプに等倍以上で通せる主力</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1">たきのぼり</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-10-water.png" alt="みず" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">63.1%</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">タイプ一致技。20%でひるみを狙える安定打点</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">じしん</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">100</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">53.4%</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">高火力技。でんきタイプに×2で通り、自分の弱点タイプに逆に打点を返せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1">ゆきなだれ</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">60</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">51.0%</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">優先度-4で後攻専用。そのターンに技ダメージを受けていれば威力2倍</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">ちょうはつ</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px;border:1px solid #cbd5e1">41.3%</td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">相手をちょうはつ状態にし、後続の積み技・回復技を封じる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1">りゅうのまい</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-15-dragon.png" alt="ドラゴン" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">—</td>
  <td style="padding:8px;border:1px solid #cbd5e1">38.8%</td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">自分の攻撃・素早さを1段階上げる積み技</td>
</tr>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">こおりのキバ</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-14-ice.png" alt="こおり" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">65</td>
  <td style="padding:8px;border:1px solid #cbd5e1">31.9%</td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">ドラゴン・じめんタイプへの弱点打点。10%で相手をこおり状態にする</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1">やけっぱち</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px"></td>
  <td style="padding:8px;border:1px solid #cbd5e1">75</td>
  <td style="padding:8px;border:1px solid #cbd5e1">28.9%</td>
  <td style="padding:8px;border:1px solid #cbd5e1;text-align:left">前ターンに動けなかった・技を外した場合威力2倍。くさ・はがねへの打点</td>
</tr>
</tbody>
</table>
</div>

パワーウィップ・たきのぼり・じしんの3つが採用率50%を超える主力技で、これにゆきなだれを加えた4技が実質の標準構成です。ちょうはつ・りゅうのまいは選択技で、積んで押し切る型と、ちょうはつで後続に繋ぐ型に分かれます。ゆきなだれは優先度-4のため素早さに関係なく後攻専用の技で、「先制技」ではなく「後攻から打つと威力が伸びる」打点技として使う点に注意してください。

---

## 主な型

**非メガ代表ビルドの性格採用率: わんぱく 29.4%（非メガ・メガを合わせた全体集計ではいじっぱり49.3%が最多ですが、これはいじっぱりを採用するギャラドスナイト個体を含む数字です。非メガ個体の最多性格はわんぱくと考えられます）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">型1：非メガ いかく型（多数派・持ち物合計61.3%）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（99.8%）<br>
<strong>性格:</strong> わんぱく（非メガ代表ビルド）<br>
<strong>EV:</strong> H32-A2-B32<br>
<strong>持ち物:</strong> ゴツゴツメット（36.9%）／たべのこし（24.4%）
</div>
<div>
<strong>技構成:</strong><br>
・パワーウィップ<br>
・たきのぼり<br>
・じしん<br>
・ゆきなだれ
</div>
</div>
</div>

わんぱくH32・B32でHP実数値202・B実数値144まで底上げしつつ、A実数値は147・S実数値は101にとどまります（本記事の苦手/得意表は、このS101・非メガ耐久寄りビルドを基準に計算しています）。積み技に頼らずいかくで相手の物理アタッカーを弱めながら、パワーウィップ・たきのぼり・じしんで着実にダメージを重ねる型です。ゴツゴツメットは接触技を受けるたびに相手の最大HPの1/6を返すため、物理アタッカーの繰り出しを牽制しながら圧をかけられます。たべのこしは毎ターン最大HPの1/16を回復し、長期戦での居座りに向きます。

**強み:**

ギャラドスナイトを消費しないため、パーティ内の他のポケモンがメガ進化枠を使えます。ゴツゴツメット採用時は接触技を主体とする物理アタッカーへの反撃打点を確保でき、たべのこし採用時はオボンのみ等の消費型きのみより回復量を安定させられます。

**弱み:**

メガ進化によるA125→155・D100→130の種族値上昇が乗らないため、耐久・打点ともにメガギャラドス型より数値は低くなります。

---

**性格採用率: いじっぱり49.3%（メガ・非メガを区別しない全体集計）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0130-00.webp" alt="ギャラドス" style="width:48px;height:48px">
  <strong style="font-size:1.05em">型2：メガギャラドス型（少数派・24.1%）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> いかく（メガ進化前）※メガ進化後はかたやぶり<br>
<strong>性格:</strong> いじっぱり（全体集計49.3%）<br>
<strong>EV:</strong> H1-A32-B1-S32（全体集計トップ9.2%。メガ/非メガを分けた個別データはなし）<br>
<strong>持ち物:</strong> ギャラドスナイト（24.1%）
</div>
<div>
<strong>技構成:</strong><br>
・パワーウィップ<br>
・たきのぼり<br>
・じしん<br>
・ゆきなだれ
</div>
</div>
</div>

メガ進化するとタイプがみず/あくに変化し、種族値もA125→155・B79→109・D100→130まで伸びます（Sは81のまま変わりません）。いじっぱりA32でA実数値は227に達し、非メガ型の代表ビルド（わんぱくA147）を大きく上回ります。ただしM-6ではギャラドスナイトの採用率は24.1%にとどまり、ゴツゴツメット・たべのこしを合わせた非メガ運用（61.3%）が主流です。

**強み:**

みず/あく複合になることで、非メガ時に等倍だったゴースト技・こおり技を半減でき、エスパー技を無効化できるようになります。またでんきタイプへの弱点が×4→×2に、いわタイプへの弱点が×2→等倍に軽減されます。A155・B109・D130への上昇でパワーウィップ・たきのぼり・じしんの確定数が縮み、非メガ型より速く相手を落とせる場面が増えます。

**弱み:**

みず/ひこうで無効化できていたじめんタイプの技が等倍で通るようになります（無効→等倍であり弱点化するわけではありませんが、受け出し性能は下がります）。さらにフェアリー・くさ・むし・かくとうタイプは非メガ時には弱点でも無効でもなかった（等倍または半減）のに対し、メガ進化後はこの4タイプすべてが新たに×2弱点として増えます。攻撃面の伸びと引き換えに、受けられる範囲は非メガ時より狭くなる点に注意が必要です。

---

## データ分析：M-5→M-6でメガ運用比率が反転

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px;border:1px solid #cbd5e1">シーズン</th>
  <th style="padding:8px;border:1px solid #cbd5e1">使用率順位</th>
  <th style="padding:8px;border:1px solid #cbd5e1">ギャラドスナイト採用率</th>
  <th style="padding:8px;border:1px solid #cbd5e1">たべのこし採用率</th>
  <th style="padding:8px;border:1px solid #cbd5e1">ゴツゴツメット採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px;border:1px solid #cbd5e1">M-5（2026-08-10時点）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">7位</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">77.8%</strong></td>
  <td style="padding:8px;border:1px solid #cbd5e1">11.4%</td>
  <td style="padding:8px;border:1px solid #cbd5e1">圏外</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px;border:1px solid #cbd5e1">M-6（2026-09-10時点）</td>
  <td style="padding:8px;border:1px solid #cbd5e1">15位</td>
  <td style="padding:8px;border:1px solid #cbd5e1">24.1%</td>
  <td style="padding:8px;border:1px solid #cbd5e1">24.4%</td>
  <td style="padding:8px;border:1px solid #cbd5e1"><strong style="color:#dc2626">36.9%</strong></td>
</tr>
</tbody>
</table>
</div>

M-5時点ではギャラドスナイト採用率77.8%でメガ運用がほぼ標準でしたが、M-6では24.1%まで低下し、代わりにM-5では圏外だったゴツゴツメットが36.9%で最多の持ち物になりました。使用率もM-5の7位からM-6は15位まで下落しており、「メガ進化して打点を伸ばす」運用から「非メガのまま居座って物理アタッカーを牽制する」運用へと環境内での立ち位置が変化したことが、持ち物データの逆転から読み取れます。

---

## 苦手なポケモン

代表型データが整備されている環境上位のポケモンのうち、自分・相手ともに複数の代表型（持ち物違いを含む）で判定しても勝敗が一致した相手のみを掲載します（代表型データが未整備、または判定が型によって割れる相手は掲載していません）。技名・採用率・確定数・先手/後手は対戦エンジンの判定をそのまま記載しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ブリジュラスの10まんボルト（採用率63.1%）はでんき×4弱点に刺さり1発で沈められます。こちらのじしん（採用率53.4%）は5発必要で、後攻になるため反撃の機会もありません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0998-00.webp" alt="メガセグレイブ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガセグレイブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位（セグレイブナイト採用率51.8%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガセグレイブのきょけんとつげき（採用率79.8%）は3発で沈める一方、こちらのじしん（採用率53.4%）は5発必要で、後攻の不利以前に確定数で大きく劣ります</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サーフゴー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">9位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのやけっぱち（採用率28.9%）はサーフゴーを2発で沈めますが、サーフゴーの10まんボルト（採用率20.0%）は1発でこちらを落とし、後攻になるため間に合いません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゴリランダー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ゴリランダーのウッドハンマー（採用率26.7%）、こちらのやけっぱち（採用率28.9%）ともに3発で確定数は互角ですが、後攻になるため先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0970-00.webp" alt="キラフロル" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">キラフロル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率53.4%）、キラフロルのパワージェム（採用率80.8%）ともに2発で確定数は互角ですが、後攻になるため先に沈められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトY採用率60.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（採用率63.1%）、メガリザードンYのソーラービーム（採用率60.1%）ともに3発で確定数は互角ですが、後攻になるため先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0038-01.webp" alt="アローラキュウコン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アローラキュウコン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">22位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アローラキュウコンのフリーズドライ（採用率80.3%）、こちらのやけっぱち（採用率28.9%）ともに4発で確定数は互角ですが、後攻になるため先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（採用率67.3%）は2発必要ですが、ウォッシュロトムのボルトチェンジ（採用率88.7%）は1発で沈められ、間に合いません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位（カイリュナイト採用率75.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こちらのこおりのキバ（採用率31.9%）は3発必要ですが、メガカイリューの10まんボルト（採用率39.5%）は1発でこちらを落とし、確定数の差が大きく歯が立ちません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">でんき×4弱点のでんこうそうげき（採用率85.1%）を受けると1発で落とされます。こちらのじしん（採用率53.4%）は2発必要で、後攻になるため反撃できません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位（メタグロスナイト採用率98.2%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">メガメタグロスのかみなりパンチ（採用率31.4%）は2発でこちらを沈める一方、こちらのじしん（採用率53.4%）は3発必要で、確定数の差で押し切られます</td>
</tr>
</tbody>
</table>
</div>

---

## 得意なポケモン

同じ基準（自分・相手ともに複数の代表型で判定が一致した相手のみ）で有利になる相手です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位（ボーマンダナイト採用率98.0%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">こおりのキバ（採用率31.9%）がドラゴン弱点を突いて2発で沈める一方、メガボーマンダのすてみタックル（採用率73.4%）は3発必要で先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取り、パワーウィップ（採用率67.3%）でアシレーヌを3発で沈めます。アシレーヌのムーンフォース（採用率99.1%）も同じく3発ですが、先手のため先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位（グソクムシャナイト採用率98.9%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取り、やけっぱち（採用率28.9%）でメガグソクムシャを3発で沈めます。メガグソクムシャのふいうち（採用率49.3%）は圏外で、こちらを倒しきれません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取り、パワーウィップ（採用率67.3%）でカバルドンを3発で沈めます。じめん技無効のためカバルドンの主力技はこちらを倒しきれません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオZ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位（ルカリオナイトZ採用率93.7%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率53.4%）はメガルカリオZを2発で沈める一方、メガルカリオZのあくのはどう（採用率59.6%）は4発必要で、後攻でも先に押し切れます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取り、じしん（採用率53.4%）でギルガルドを3発で沈めます。ギルガルドのシャドーボール（採用率42.9%）も同じく3発ですが、先手のため先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（採用率67.3%）は3発でミミッキュを沈める一方、ミミッキュのじゃれつく（採用率98.1%）は圏外で、こちらを倒しきれません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0908-00.webp" alt="マスカーニャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">マスカーニャ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">やけっぱち（採用率28.9%）でマスカーニャを2発で落とせる一方、マスカーニャのトリックフラワー（採用率96.1%）は3発必要で、後攻でも先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0902-01.webp" alt="イダイトウ(メス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(メス)</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（採用率67.3%）が2発で沈める一方、イダイトウのウェーブタックル（採用率96.5%）は圏外で、こちらを倒しきれません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位（リザードナイトX採用率37.6%）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率53.4%）が2発で沈める一方、メガリザードンXのげきりん（採用率21.6%）は3発必要で、後攻でも先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（採用率63.1%）が2発で沈める一方、エースバーンのダストシュート（採用率75.8%）は3発必要で、後攻でも先に決められます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0658-00.webp" alt="ゲッコウガ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ゲッコウガ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">パワーウィップ（採用率67.3%）が2発で沈める一方、ゲッコウガのヘドロウェーブ（採用率73.5%）は3発必要で、後攻でも先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0637-00.webp" alt="ウルガモス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウルガモス</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">21位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">たきのぼり（採用率63.1%）が2発で沈める一方、ウルガモスのギガドレイン（採用率77.6%）は5発必要で全く間に合いません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">オオニューラ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">23位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じしん（採用率53.4%）が2発で沈める一方、オオニューラのフェイタルクロー（採用率94.7%）は5発必要で、後攻でも先に決められます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/pokemon/pokemon-0911-00.webp" alt="ラウドボーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ラウドボーン</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">先手を取り、たきのぼり（採用率63.1%）でラウドボーンを4発で沈めます。ラウドボーンのシャドーボール（採用率52.9%）も同じく4発ですが、先手のため先に決められます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率・パートナー

<div class="partner-grid">
<div class="partner-card"><img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス"><div class="name">ガブリアス</div><div class="rate">同居率1位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0448-00.webp" alt="ルカリオ"><div class="name">ルカリオ</div><div class="rate">同居率2位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ"><div class="name">セグレイブ</div><div class="rate">同居率3位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン"><div class="name">カバルドン</div><div class="rate">同居率4位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ"><div class="name">ボーマンダ</div><div class="rate">同居率5位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ"><div class="name">グソクムシャ</div><div class="rate">同居率6位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ"><div class="name">ミミッキュ</div><div class="rate">同居率7位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-1000-00.webp" alt="サーフゴー"><div class="name">サーフゴー</div><div class="rate">同居率8位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ"><div class="name">アシレーヌ</div><div class="rate">同居率9位</div></div>
<div class="partner-card"><img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス"><div class="name">ブリジュラス</div><div class="rate">同居率10位</div></div>
</div>

※同居率データは2026-09-17時点の最新スナップショットを使用しています。

同居率1位のガブリアスはじめん/ドラゴンタイプで、ギャラドスの弱点であるでんきタイプの技を無効化できます。一方でガブリアスの弱点はこおり・ドラゴン・フェアリーで、ギャラドス自身もこおりタイプへの耐性を持たないため、ガブリアスをこおり技で狙ってくる相手をギャラドスが代わりに受け止めることはできません。この面では互いの弱点を補完し合う組み合わせではなく、それぞれ別の役割（アタッカー・いかく要員）を担う並び方です。同居率2位のルカリオ、4位のカバルドンを含め、物理アタッカー・受けとしての役割分担でパーティに並ぶ構成が多く見られます。

---

## まとめ

M-6のギャラドスは使用率15位で、M-5（7位）から順位を落としました。最大の変化はギャラドスナイトの採用率が77.8%から24.1%へ低下し、代わりにゴツゴツメット（36.9%）を中心とした非メガ運用が主流になった点です。いかく・じめん技無効という素の耐性を活かしつつ、パワーウィップ・たきのぼり・じしんの3タイプ技で押し切る型が現在の標準です。でんき×4弱点は変わらず最大の弱点であり、パーモット・ウォッシュロトム等のでんき技持ちには引き続き注意が必要です。

## 関連記事

- [ガブリアス考察記事一覧はこちら](/blog/garchomp-analysis-m6/)
- [ルカリオ考察記事一覧はこちら](/blog/lucario-analysis-m6/)
