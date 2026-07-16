---
title: 'ブラッキー考察 M-2 使用率31位 イカサマ耐久型の採用率と立ち回り'
description: 'M-2シングルバトルで使用率31位のブラッキーを徹底分析。イカサマ採用率97.2%・たべのこし89.8%・ねがいごと78.7%の耐久サポート型を解説。HB特化での物理受け性能、苦手なかくとう・フェアリーへの対策、同居率上位のパーティ構成まで実データで紹介します。'
updatedDate: '2026-06-11'
pubDate: '2026-06-11'
draft: false
heroImage: '../../assets/hero-umbreon-m2.png'
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
  <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" />
  <div>
    <h2 style="margin:0 0 8px">ブラッキー</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">31位</strong>　持ち物: <strong>たべのこし 89.8%</strong>
    </div>
  </div>
</div>

> ⚠️ 本記事のデータはM-2シーズン（2026/05/30）時点の集計です

シーズンM-2（2026/5/13〜6/17）のシングルバトルで、ブラッキーは**使用率31位**を記録。種族値はHP95・B110・D130に偏った高耐久型で、攻撃面の数値（A65・C60）は低いのが特徴です。

この低い攻撃を補うのが**イカサマ（採用率97.2%）**。イカサマは自分のこうげきではなく**相手のこうげきを参照**してダメージを計算するため、A65という低い攻撃でも、A130のガブリアスのような高火力物理アタッカーに大きなダメージを返せます。さらに**ねがいごと（78.7%）・つきのひかり（19.6%）**で自己回復し、**どくどく（36.5%）**で詰めていく、受け回し主体のポケモンです。

---

## なぜブラッキーが採用されるのか

### 1. イカサマで物理アタッカーを逆手に取る

ブラッキー最大の特徴は**イカサマ（採用率97.2%・ほぼ全個体が採用）**です。イカサマのダメージは自分のA65ではなく相手のこうげきで計算されるため、A130のガブリアス、A134のカイリュー、A125のギャラドスといった、イカサマが等倍で通る環境上位の高A物理アタッカーほど、こちらの返しダメージが大きくなります。あくタイプ一致補正も乗るため、つるぎのまいで積んだ相手には積んだ分だけイカサマの威力も上がります。

低A・低Cのブラッキーが攻撃役として機能するのは、ほぼこのイカサマ1本に依存しています。

### 2. B110・D130の両受けに高HPで物理・特殊両対応

種族値はHP95・ぼうぎょ110・とくぼう130と、物理・特殊の両面で受けに回れる配分です。性格は**ずぶとい（B↑・56.7%）**が最多で、HB特化（採用率上位はHBにD調整を加えた型）により物理アタッカーへの受け出しが安定します。EV振りは**HB（B↑）が約8割**を占め、HD（D↑）型は6.5%にとどまります。

あく単タイプは弱点が**かくとう・むし・フェアリーの3つのみ**と少なく、エスパー技を**無効化**できるのが受け出しの安定性につながっています。

### 3. ねがいごと＋たべのこしで居座りと回復を両立

回復技は**ねがいごと（78.7%）**が主流で、たべのこし（採用率89.8%）の毎ターン回復と合わせて長く場持ちします。**まもる（79.9%）**はねがいごとの回復ターンを稼ぐ・どくどくの定数ダメージを稼ぐために高採用です。天候に依存しない**つきのひかり（19.6%）**を選ぶ個体もいますが、ねがいごとは控えのポケモンにも回復を渡せる点で採用率が上回っています。

---

## 基本スペック

### 種族値

<div style="max-width:380px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:63%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#3b82f6">95</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:73%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">110</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:87%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right"><strong style="color:#059669">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:43%;background:linear-gradient(90deg,#94a3b8,#64748b);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:36px;text-align:right">65</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">525</span>
  </div>
</div>

ぼうぎょ110・とくぼう130の両受け種族値にHP95が乗り、物理・特殊どちらの攻撃も受けられる配分です。一方こうげき65・とくこう60と攻撃面は低く、自前の高威力打点を持ちません。S65も低速のため、受けて回復し、どくどくの定数ダメージで削るという長期戦の立ち回りが基本になります。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-16-dark.png" alt="あく" style="width:44px;height:44px;vertical-align:middle;margin:2px" title="あく" />
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
      <span><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">かくとう</span>
      <span><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">むし</span>
      <span><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">フェアリー</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;font-size:0.85em">
      <span><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">ゴースト</span>
      <span><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">あく</span>
    </div>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:28px;height:28px;vertical-align:middle;margin-right:3px">エスパー
  </td>
</tr>
</tbody>
</table>
</div>

あく単タイプは弱点が**かくとう・むし・フェアリーの3つのみ**と少なく、エスパー技を完全に無効化します。スターミー（20位）・マフォクシー（25位）のエスパー技を受けに行ける点は環境的に有用です。一方、弱点のかくとうは環境上位（ルカリオ・ミミロップ・ハッサム）が高採用、フェアリーもミミッキュ（19位）・フラエッテ:永遠（17位）・アシレーヌ（4位）が広く採用するため、弱点の数は少なくても遭遇頻度は高い点に注意が必要です。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>イカサマ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">95</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">97.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手のこうげきで計算。一致補正あり。高A物理アタッカーほど痛打</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>まもる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>79.9%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねがいごとの着地ターン稼ぎ・どくどくの定数ダメージ稼ぎ</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねがいごと</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>78.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">最大HPの半分を次ターンに回復。控えにも回復を渡せる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>あくび</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong>60.5%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">次ターン終了時に眠らせる。受け出しからの交代強要・積みの牽制</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>どくどく</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">36.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">猛毒の定数ダメージで耐久型・受け回しを崩す</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つきのひかり</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-17-fairy.png" alt="フェアリー" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">19.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">天候非依存の自己回復。ねがいごとと選択</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ちょうはつ</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手の変化技を封じる。ミラーの受け合いで先行する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ほえる</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">積みアタッカーを流す。どくどく蓄積後の交代強要</td>
</tr>
</tbody>
</table>
</div>

技構成は**イカサマ＋まもる＋ねがいごと（またはつきのひかり）＋第4枠（あくび／どくどく）**がテンプレートです。攻撃技はイカサマ1本のみで、残りは回復・状態異常・流し技で固める受け特化型に統一されています。

---

## 主要型の解説

### 型1: HBイカサマ物理受け型（最多採用）

**性格採用率: ずぶとい 56.7%**（HB物理受けの指標。性格分布で最多）

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HBイカサマずぶとい型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> せいしんりょく（68.4%）<br>
<strong>性格:</strong> ずぶとい（B↑ A↓）<br>
<strong>EV:</strong> H32 B32（D方向に余りを2前後）<br>
<strong>持ち物:</strong> たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・イカサマ<br>
・ねがいごと / つきのひかり<br>
・まもる<br>
・あくび / どくどく
</div>
</div>
</div>

**強み:**

EV振りはHB（B↑）型が合計約8割を占め、物理アタッカーへの受け出しに特化します。イカサマが相手のこうげきを参照するため、A130のガブリアスやA134のカイリューなどイカサマが等倍で通る高A物理アタッカーほど大きく削れ、こちらは低い攻撃のまま反撃できます。ねがいごと＋たべのこしで居座りつつ、あくびで積みアタッカーに交代を強要できます。

ずぶといのA↓補正はイカサマのダメージに影響しません（イカサマは相手のAを参照するため）。特性せいしんりょく（68.4%）はミミロップのねこだましやガブリアスのいわなだれ（23.1%）などのひるみを無効化し、受け回し中にひるみで動けなくなる事故を防ぎます。

**弱み:**

D方向の振りが薄いため、フラエッテ:永遠のムーンフォース（特殊フェアリー・採用率87%）やアシレーヌのムーンフォース（97%）など特殊フェアリー技に弱く、弱点×2と相まって受けきれません。また攻撃がイカサマ1本のため、こうげきの低い特殊アタッカーや、つるぎのまいを積まない物理低A個体にはイカサマのダメージが伸びず、決定打を欠きます。

---

### 型2: HDシンクロ特殊受け型（少数）

**EV採用率: HD（D↑）型 6.5%（少数派）**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:48px;height:48px">
  <strong style="font-size:1.05em">HDイカサマ特殊受け型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> シンクロ（31.6%）<br>
<strong>性格:</strong> おだやか（D↑ A↓）など<br>
<strong>EV:</strong> H32 D32（B方向に余りを2前後）<br>
<strong>持ち物:</strong> たべのこし
</div>
<div>
<strong>技構成:</strong><br>
・イカサマ<br>
・ねがいごと<br>
・まもる<br>
・どくどく
</div>
</div>
</div>

**強み:**

HD（D↑）型はEV振りで6.5%と少数ですが、種族値D130をさらに伸ばして特殊アタッカーを受けます。HB型では受けにくいフラエッテ:永遠・アシレーヌのフェアリー技に対しても、弱点等倍化はできないものの被害を抑えられます。特性シンクロ（31.6%）は、相手の技や特性でどく・もうどく・まひ・やけど状態になると相手にも同じ状態異常を返すため、どくどくやおにびでこちらの居座りを崩そうとする受け回し相手を逆に削れます。

**弱み:**

HB型と比べてぼうぎょが下がるため、ガブリアスのじしんなど等倍以上で通る高A物理技を受けたときの被害が増えます。HB型がカバーする物理受けの安定性を犠牲にしている分、相手の攻撃方向を読み違えると回復が間に合わなくなります。

---

## 環境ポケモンへの相性分析

### 主要ポケモンとの相性

使用率上位のうち、ブラッキーと相性がはっきり出るポケモンを有利・不利の両面から挙げます。ブラッキーは攻撃手段がイカサマ1本で、相手のこうげきに依存します。よって**高A物理アタッカーには受けが安定する一方、弱点を突くかくとう・フェアリー、こうげきの低い特殊アタッカーには受けが成立しにくい**点を基準に判定しています。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A130の高A物理。じしん（採用率99.2%）をHBで受け、イカサマが相手のA130参照で大きく返る。げきりん（47.9%）はあく等倍で痛打にならない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0983-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ドドゲザン（24位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ふいうち（99.0%）・ドゲザンはあく0.5、アイアンヘッドははがね等倍で被害は小さい。ただしイカサマはあく/はがね相手に0.5半減、どくどくもはがね複合に無効のため、こちらから崩す手段が乏しく決め手を欠く。けたぐり（17.6%・かくとう）採用個体には×2弱点を突かれる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0094-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ゲンガー（10位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#ca8a04;font-weight:bold">△ 五分</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドーボール（71.1%）はあく半減だが、主力のヘドロウェーブ（どく・81.7%）は等倍で通り、きあいだま（かくとう・37.4%）採用個体には×2弱点を突かれる。D130で耐え一致イカサマで削れるが、どくタイプにどくどくが効かず一方的な受けにはならない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0121-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">スターミー（20位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#16a34a;font-weight:bold">○ 有利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">しねんのずつき等のエスパー技を無効化。みず技も等倍でB110・D130の高耐久で受け、どくどくで削れる。受け出しの定番</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A110＋一致インファイト（71.5%）がかくとう×2弱点。HB振りでも受けきれず、イカサマの返しより先に落とされる</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center;color:#dc2626;font-weight:bold">× 不利</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（91.9%）がフェアリー×2弱点。ばけのかわで1発耐えてつるぎのまいを積まれると、イカサマの返しも追いつかない</td>
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
    <img src="/images/pokemon/pokemon-0448-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ルカリオ（9位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">A110＋一致インファイト（採用率71.5%）がかくとう×2。HB振りでも受け切れず、受け出しが成立しない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうを半減するアーマーガア（はがね/ひこう）・かくとうを無効化するゲンガー（ゴースト/どく）等を後出しして受け、こちらが処理する。ブラッキーは初手から対面させない</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0428-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミロップ（13位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（61.1%）・とびひざげり（33.5%）のかくとう技が×2弱点。ねこだまし＋マッハパンチ（36.8%）で先制を取られ回復の隙も与えられない</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">かくとうを半減するアーマーガアや、ゴースト複合でかくとうを無効化するギルガルド（はがね/ゴースト）を合わせ、後出しから処理する</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">アシレーヌ（4位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（採用率97.0%）がフェアリー×2弱点。特殊アタッカーのためHB型では受けきれず、こうげきが低くイカサマの返しも小さい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フェアリーを半減するハッサム・ギルガルド（はがね複合）・どくタイプを後出しして受ける。HD型なら被害を抑えられるが受け切りは難しい</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0670-05.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">フラエッテ:永遠（17位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ムーンフォース（87.0%）がフェアリー×2弱点。めいそう（85.7%）で積まれ、ドレインキッス（74.6%）で回復しながら殴られると受けが崩壊する</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">どくどくの入る前に積まれると不利。はがね・どくタイプ（ハッサム・ギルガルド等）でフェアリーを半減して受ける。ちょうはつ採用個体でめいそうを止める手もある</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0212-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ハッサム（14位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">インファイト（72.4%）がかくとう×2弱点。つるぎのまい（86.6%）で積まれるとイカサマの返しは増えるが受けは間に合わない。バレットパンチ（99.7%）は先制で削られる</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのお（×4）・じめん（×2）技でハッサムの弱点を突けるポケモン（リザードン・ガブリアス等）を合わせて処理する</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" style="width:32px;height:32px;vertical-align:middle;margin-right:4px">ミミッキュ（19位）
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じゃれつく（91.9%）がフェアリー×2弱点。ばけのかわで攻撃を1回無効化されつるぎのまい（86.7%）を積まれる。かげうち（93.6%）の先制も持つ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがね・どくタイプでフェアリーを半減して受け、ばけのかわを多段技や先制で剥がしてから処理する</td>
</tr>
</tbody>
</table>
</div>

---

## パーティ構成

### 相性の良いポケモン

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス">
    <div class="name">カメックス</div>
    <div class="rate">同居率1位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">みず枠でほのお・いわ・はがねを受け、ブラッキーと攻守の役割を分担</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0939-00.webp" alt="ハラバリー">
    <div class="name">ハラバリー</div>
    <div class="rate">同居率2位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">でんき枠。ブラッキーが受けたみず・ひこうへC103から打点を入れる</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率3位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">ステルスロック展開＋高速地面。ブラッキーの受けで蓄積したダメージを詰める</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがね/ドラゴンの高C特殊受け。ブラッキーが薄い特殊方面を補完する</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0212-00.webp" alt="ハッサム">
    <div class="name">ハッサム</div>
    <div class="rate">同居率7位</div>
    <div style="font-size:0.65rem;color:#888;margin-top:2px">はがねでフェアリーを半減。バレットパンチでフェアリー・こおりを先制処理</div>
  </div>
</div>

**パーティ構成の基本方針:**

ブラッキーは攻撃がイカサマ1本で自前の崩し性能が低く、弱点のかくとう・フェアリーが環境上位に多いため、残り5体で以下の役割を補います。

1. **かくとう対策**: アーマーガア（半減）・ギルガルド（無効化）などかくとうを軽減できる枠で、ルカリオ・ミミロップ・ハッサムを受ける
2. **フェアリー対策**: ハッサム・ギルガルドなどフェアリーを半減するはがね複合で、アシレーヌ・フラエッテ:永遠・ミミッキュを受ける
3. **崩し役**: ガブリアス等のアタッカーで、ブラッキーのどくどく＋受けで蓄積したダメージを詰める
4. **ステルスロック展開**: ガブリアス等でステロを撒き、あくび・ほえるの交代強要と合わせて定数ダメージを稼ぐ

---

## データ分析①：イカサマ97.2%が示す「攻撃を相手に肩代わりさせる」設計

ブラッキーのこうげき種族値は65・とくこうは60と、攻撃面は環境最低クラスです。にもかかわらず攻撃技イカサマの採用率は**97.2%**でほぼ全個体が採用しています。これは自前の攻撃力ではなく、相手のこうげきで殴る設計に振り切っていることを示します。

| 相手 | こうげき種族値 | イカサマが参照する攻撃 | あく一致・タイプ相性 |
|---|---|---|---|
| ガブリアス（1位） | 130 | 相手のA130 | あく等倍・一致補正あり |
| カイリュー（16位） | 134 | 相手のA134 | あく等倍・一致補正あり |
| ギャラドス（12位） | 125 | 相手のA125 | あく等倍・一致補正あり |
| ブラッキー自身のA | 65 | （通常技なら）65 | — |

通常の一致あく技なら自分のA65で計算されますが、イカサマはガブリアス・カイリュー・ギャラドスといったA125超の物理アタッカーのこうげきをそのまま流用します（イカサマがあく等倍で通る相手に限る。あく/はがねのドドゲザンのようにイカサマが半減される相手では返しは伸びません）。さらにこれらがつるぎのまいを積むと、積んだ分だけイカサマの威力も上がるため、**相手が火力を上げるほどこちらの返しも大きくなる**という、受けポケモンとして理にかなった構造です。

逆にこの設計の弱点も明確で、こうげきの低い特殊アタッカー（アシレーヌA74・フラエッテ等）に対してはイカサマの返しが小さく、弱点フェアリーで殴られる側だけが成立します。ブラッキーが「高A物理に強く特殊フェアリーに弱い」のは、種族値の耐久配分だけでなく、イカサマという攻撃手段そのものに起因しています。

---

## まとめ：型別比較

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#1e3a5f;color:#fff">
  <th style="padding:10px 12px;border:1px solid #cbd5e1;text-align:left">型</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">性格（指標）</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">主な技</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">強み</th>
  <th style="padding:10px 12px;border:1px solid #cbd5e1">弱み</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HBイカサマ物理受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">ずぶとい 56.7%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">イカサマ・ねがいごと・まもる・あくび</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">高A物理アタッカーをイカサマで痛打しつつ受ける</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊フェアリーに脆い。D振りが薄い</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-weight:600">HDイカサマ特殊受け型</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">おだやか/しんちょう系 約15%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">イカサマ・ねがいごと・まもる・どくどく</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">特殊アタッカーへの被害を抑える。シンクロで状態異常返し</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left;font-size:0.85em">物理受けが下がり高A物理の被害増</td>
</tr>
</tbody>
</table>
</div>

**総評:**

ブラッキーはB110・D130・HP95の高耐久と、イカサマ（採用率97.2%）による「相手の攻撃力を借りた反撃」を両立した受けポケモンです。あく単タイプはエスパー無効・弱点3つのみで、ガブリアス・カイリューなどイカサマが等倍で通る高A物理アタッカーや、スターミーのエスパー枠を受け出しから処理できます。ねがいごと（78.7%）＋たべのこし（89.8%）で居座り、どくどく・あくびで盤面を整える長期戦が得意です。

一方、弱点のかくとう（ルカリオ・ミミロップ・ハッサム）・フェアリー（アシレーヌ・フラエッテ:永遠・ミミッキュ）は環境上位に高採用で、特に特殊フェアリーにはイカサマの返しも小さく受けが成立しません。これらをはがね・どく・かくとう半減枠でカバーできるかが、ブラッキーを採用したパーティの安定性を左右します。

---

## 関連記事

- [天敵となるかくとうアタッカー ルカリオのM-2考察](/blog/lucario-analysis-m2/)
- [イカサマで受けやすい使用率1位 ガブリアスのM-2考察](/blog/garchomp-analysis-m2/)
- [同居率上位の崩し枠 ハッサムのM-2考察](/blog/scizor-analysis-m2/)
</content>
</invoke>
