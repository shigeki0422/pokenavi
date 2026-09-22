---
title: '【ポケモンチャンピオンズ】オオニューラ 考察 M-6シーズン サイコシード×かるわざ'
description: 'ポケモンチャンピオンズM-6シーズン使用率19位のオオニューラを考察。かるわざ(採用率95.0%)とサイコシード(49.1%)が生むS2倍展開、いじっぱりAS型の実数値、M-5からの持ち物採用率の変化、苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-09-22'
draft: false
heroImage: '../../assets/hero-sneasler-m6.png'
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
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" />
  <div>
    <h2 style="margin:0 0 8px">オオニューラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#dc2626">19位</strong>　特性: <strong>かるわざ 95.0%</strong>
    </div>
  </div>
</div>

> データ集計日：2026-09-17（本記事の使用率順位はM-6シーズン期間中の09-17時点の集計基準。ポケモン情報ページの16位は最新の集計基準によるもので、基準日の違いにより順位が異なります）

M-6シーズンのオオニューラは**使用率19位**。種族値S120の高速かくとうアタッカーで、特性かるわざ（採用率95.0%）で持ち物を消費してから加速し、インファイト・フェイタルクローで押し切る型が主流です。直前のM-5シーズンでは使用率48位・しろいハーブ主流（37.9%）でしたが、M-6では使用率が48位→19位へ上昇し、持ち物もサイコシード（採用率49.1%）を使った加速型へ大きく入れ替わりました。

---

## 基本スペック

<div style="max-width:560px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:44%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:72%;background:linear-gradient(90deg,#f97316,#dc2626);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right"><strong style="color:#dc2626">130</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:33%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:22%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">40</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:44%;background:linear-gradient(90deg,#60a5fa,#3b82f6);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:6px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px"><div style="width:66%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div></div>
    <span style="width:32px;text-align:right"><strong style="color:#059669">120</strong></span>
  </div>
  <div style="display:flex;align-items:center;gap:8px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="min-width:40px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>

A130・S120と、物理アタッカーとして高い攻撃・素早さを両立した種族値配分です。一方でH80・B60・D80と耐久は並程度にとどまり、後述のとおり環境上位の一撃で崩されやすい弱点になっています。

---

## タイプ・弱点

<div class="type-row"><strong>タイプ：</strong><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:40px;height:40px"><img src="/images/types/type-03-poison.png" alt="どく" style="width:40px;height:40px"></div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×4）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">弱点（×2）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.5）</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">耐性（×0.25）</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:10px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-13-psychic.png" alt="エスパー" style="width:36px;height:36px"></td>
  <td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px"><img src="/images/types/type-04-ground.png" alt="じめん" style="width:36px;height:36px"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:36px;height:36px"></div></td>
  <td style="padding:10px 12px;border:1px solid #cbd5e1"><div style="display:flex;justify-content:center;gap:4px;flex-wrap:wrap"><img src="/images/types/type-11-grass.png" alt="くさ" style="width:36px;height:36px"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:36px;height:36px"><img src="/images/types/type-03-poison.png" alt="どく" style="width:36px;height:36px"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:36px;height:36px"><img src="/images/types/type-16-dark.png" alt="あく" style="width:36px;height:36px"></div></td>
  <td style="padding:10px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-06-bug.png" alt="むし" style="width:36px;height:36px"></td>
</tr>
</tbody>
</table>
</div>

無効タイプはありません。エスパー×4が最大の弱点で、使用率上位ではイエッサン(オス)のワイドフォース（採用率99.5%）、メタグロスのサイコファング（77.5%）などが該当します。じめん・ひこうは×2弱点で、使用率1位のボーマンダ（ひこう複合）のじしん（71.1%）が×2で通ります。ひこう技ではアーマーガアのブレイブバード（30.5%）が同様に×2で刺さります。

---

## 特性

<strong>かるわざ（採用率95.0%）</strong>：「持っていた道具がなくなると素早さが2倍になる」特性です。持ち物を消費した瞬間に発動するため、オオニューラはこの発動条件を満たす持ち物を意図的に選択して運用します（詳細は下記「主な型」）。他の特性（どくしゅ4.9%、プレッシャー0.2%）は少数派です。

---

## 主要な技と採用率

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">技名</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">タイプ</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">威力</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">備考</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">インファイト</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">120</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">98.4%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技のメインウェポン。使用後は自分のB・Dが1段階下がる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">フェイタルクロー</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><strong style="color:#dc2626">96.2%</strong></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">一致技。30%で相手をどく・まひ・ねむりのいずれかにする</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">-</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">自分の攻撃を2段階上げる積み技</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">じごくづき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">80</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">相手をじごくづき状態にし、相手の音技（ハイパーボイス・フレアソング等）を2ターン封じる補完打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ねこだまし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">40</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">35.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">優先度+3。場に出て最初のターンのみ使用可能で相手をひるませる</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">アクロバット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55（道具無しで110）</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">17.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物を消費し切った後の追加打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">75</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">はがねタイプへの補完打点</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">シャドークロー</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px"></td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">70</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">きゅうしょに当たりやすい技</td>
</tr>
</tbody>
</table>
</div>

インファイト・フェイタルクローの一致2技はほぼ全個体が採用する固定枠です。残る2枠はつるぎのまい・じごくづき・ねこだましの組み合わせで、後述の型によって使い分けます。

---

## 主な型

**性格採用率: いじっぱり 88.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">サイコシード型（AS物理アタッカー）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（95.0%）<br>
<strong>性格:</strong> いじっぱり（88.1%）<br>
<strong>EV:</strong> H2-A32-S32（28.3%）<br>
<strong>持ち物:</strong> サイコシード（49.1%）
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・フェイタルクロー<br>
・つるぎのまい<br>
・じごくづき
</div>
</div>
</div>

A実数値200・S実数値172（いじっぱりのためS無補正）。サイコシードは「サイコフィールド状態の時に特防が1段階上がる。1度使うとその対戦中は無くなる」持ち物で、味方がサイコフィールドを展開した状態で消費されるとD+1段階を得たうえでかるわざが発動し、S172が344相当まで跳ね上がります。

**強み:**

じごくづきは相手を音技封じ状態にできるため、フレアソングを採用率99.1%で使うラウドボーンに対して2ターンの間その技を封じられる点が実戦的な補完打点になります。

**弱み:**

サイコシードはサイコフィールドが展開されていないと消費されず、かるわざも発動しません。イエッサン(オス)などサイコフィールドを展開できる味方がいない編成では、S172のまま加速できずに攻撃を受けることになります。

---

**性格採用率: いじっぱり 88.1%**

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">ノーマルジュエル型（自己完結の初手加速）</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（95.0%）<br>
<strong>性格:</strong> いじっぱり（88.1%）<br>
<strong>EV:</strong> H2-A32-S32（28.3%）<br>
<strong>持ち物:</strong> ノーマルジュエル（28.0%）
</div>
<div>
<strong>技構成:</strong><br>
・インファイト<br>
・フェイタルクロー<br>
・ねこだまし<br>
・つるぎのまい
</div>
</div>
</div>

ノーマルジュエルは「ノーマルタイプの技の威力が1.3倍になる。1度使うとその対戦中は無くなる」持ち物です。場に出た最初のターンにねこだまし（優先度+3、場に出て最初のターンのみ使用可能）を撃つと、威力40が1.3倍に強化されたうえでジュエルが消費され、かるわざが発動して大きく加速します。

**強み:**

サイコシード型と異なりサイコフィールドを展開する味方に依存せず、単独で確実に加速を起動できます。ねこだましの優先度+3でひるみを取りつつ起動するため、初手から相手の行動を1つ潰せる点もサイコシード型にはない利点です。

**弱み:**

ねこだましは場に出て最初のターンしか使えないため、控えに下げて再度出し直すまでは再利用できません。サイコシード型が得るD+1段階の耐久補正はなく、加速後の被弾には弱いままです。

---

## データ分析：M-5からのシーズン変化（使用率・持ち物・技）

M-5シーズン（使用率48位）とM-6シーズン（使用率19位）を比較すると、使用率が29順位上昇すると同時に、加速手段が丸ごと入れ替わっていることがわかります。M-2シーズン（使用率33位）のデータも参考として併記します。

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1">項目</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-2採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-5採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">使用率順位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">33位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">48位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19位</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物：しろいハーブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">37.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.1%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物：サイコシード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">TOP10圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">TOP10圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">49.1%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">持ち物：ノーマルジュエル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">TOP10圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">TOP10圏外</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">28.0%</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">技：つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.8%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">26.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">55.2%</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">技：じごくづき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">52.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32.0%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">50.9%</td>
</tr>
</tbody>
</table>
</div>

M-5まではしろいハーブ（インファイトのB・Dダウンを打ち消しつつ消費）による加速が主流で、使用率も48位と低調でした。M-6ではしろいハーブが4.1%まで激減し、代わってサイコシード・ノーマルジュエルという新しい加速手段がTOP10圏外から一気に採用率上位へ浮上しています。じごくづきの採用率はM-2の52.3%からM-5で32.0%へ一度落ち込み、M-6で50.9%まで再上昇するという往復を見せています。つるぎのまいもM-5の26.1%からM-6は55.2%へ倍増しており、加速後に確実に打点を伸ばす構成が支持を広げています。

---

## 苦手なポケモン

使用率TOP30を対象に、自分・相手ともに採用率20%以上の主力技だけで判定し、代表型が変わっても勝敗が一致する相手のみ掲載します。速度はいずれも**かるわざ未発動時点のS172**で比較しています（技・確定数・先手判定は対戦エンジンの判定結果をそのまま転記、代表持ち物は各相手の最多採用型）。

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
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="メガボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガボーマンダ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">1位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力フェイタルクロー（採用率96.2%）は確定3発。相手のすてみタックル（採用率76.2%、ボーマンダナイト採用率97.7%）は確定1発で、S172の同速のため先に動ける場合もありますが、先に動いてもフェイタルクロー3発では勝てず、相手のすてみタックル1発で先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="メガガブリアスZ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガガブリアスZ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。ガブリアスナイトZ型（最多採用率35.6%）のりゅうせいぐん（採用率30.3%）も確定2発と互角ですが、メガ後S223で先手を取るため打ち負けます。なおガブリアス全体ではじしん採用率66.7%が最多で、じしんを持つ個体では確定1発になる可能性があり判定はりゅうせいぐん採用時のものです</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定3発。相手のじしん（採用率97.7%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="メガグソクムシャ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガグソクムシャ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定3発。相手のアイアンヘッド（採用率77.6%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0448-00.webp" alt="メガルカリオZ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガルカリオZ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">6位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定1発。相手のてっていこうせん（採用率20.0%）も確定1発ですが、ルカリオナイトZ型（採用率90.5%）はメガ後S223で先手を取るため打ち負けます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力フェイタルクロー（採用率96.2%）は確定3発。相手のじゃれつく（採用率96.8%）は確定2発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0681-00.webp" alt="ギルガルド" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ギルガルド
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">13位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力じごくづき（採用率50.9%）は確定3発。相手のポルターガイスト（採用率52.7%）はのろいのおふだ型（21.7%）とたべのこし型の大半で確定1発、たべのこし型の一部ビルド（S72）のみ確定2発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定3発。相手のブレイブバード（採用率30.5%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンX" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンX
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。相手のフレアドライブ（採用率24.6%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="メガリザードンY" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガリザードンY
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">17位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力フェイタルクロー（採用率96.2%）は確定2発。相手のかえんほうしゃ（採用率50.8%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">18位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力じごくづき（採用率50.9%）は確定2発。相手のウェーブタックル（採用率96.7%）は確定1発で、こだわりスカーフ型（採用率69.8%）はS214で先手を取られて打ち負けるうえ、オオニューラの方が速いいのちのたま型・しんぴのしずく型でも先に動いてじごくづき2発では相手のウェーブタックル1発に間に合いません</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0815-00.webp" alt="エースバーン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">エースバーン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">20位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。相手のかえんボール（採用率99.2%）も確定2発と互角ですが、こだわりスカーフ型（採用率33.1%）はS256で先手を取るため打ち負けます。さらにいのちのたま型（採用率22.3%）はS171でオオニューラ（S172）より遅く、オオニューラが先手を取れるものの、相手のかえんボールが確定1発（インファイトは確定2発）のため先手を取っても打点で負けます</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0923-00.webp" alt="パーモット" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">パーモット
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">26位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。相手のでんこうそうげき（採用率93.4%）は確定1発で、S172の同速のため先に動ける場合もありますが、先に動いてもインファイト2発では足りず、相手のでんこうそうげき1発で先に落とされます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メガメタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガメタグロス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">27位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。相手のサイコファング（採用率77.5%）は確定1発で、オオニューラが先手を取っても打点で足りません</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="メガカイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メガカイリュー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">30位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力フェイタルクロー（採用率96.2%）は確定4発。相手のりゅうせいぐん（採用率50.1%、カイリュナイト最多採用率69.5%）は確定1発で、オオニューラが先手を取っても大きく打点が足りません</td>
</tr>
</tbody>
</table>
</div>

苦手な相手は大きく2パターンに分かれます。カバルドン・メガグソクムシャ・アーマーガア・メガメタグロス・メガリザードンX/Y・メガカイリュー・ミミッキュ・メガボーマンダ・パーモット・イダイトウ(オス)・ギルガルドの12体は確定数そのもので上回られており、先手を取れても打点勝負で負けます。メガガブリアスZ・メガルカリオZは確定数が互角ながら最多採用型の速度（ともにS223）で上回られて先手を取れず、打点負けします。エースバーンはこだわりスカーフ/きあいのタスキ型なら確定数互角の速度負けですが、いのちのたま型（22.3%）はS171で先手を取れても確定数自体で負けます。

かるわざ発動後のS344相当まで加速すれば（優先度技には素早さに関係なく後手のまま）、確定数が互角のメガガブリアスZ（りゅうせいぐん型限定）・メガルカリオZ・エースバーン（こだわりスカーフ/きあいのタスキ型）は先手を取れて勝敗が覆ります。ただしエースバーンのいのちのたま型（22.3%）は加速しても打点不足で覆らず、確定数そのもので負けている残り12体は加速しても不利のままです。

---

## 得意なポケモン

使用率TOP30を対象に、苦手なポケモンと同じ基準（自分・相手ともに採用率20%以上の主力技、代表型が変わっても勝敗が一致する相手のみ）で判定しています。攻撃技のみで判定しているため、採用率1位が積み技のカメックス（からをやぶる90.5%）はエンジン判定上勝てる結果になりますが、実戦では加速・積みが反映されず判定が一致しないため得意表から除外しています。得意な相手は限られます。

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
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力フェイタルクロー（採用率96.2%）は確定2発。相手のムーンフォース（採用率98.0%）も確定2発と互角ですが、S172のオオニューラが先手を取れるため相手の2発目が飛ぶ前に決着を付けられます</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブリジュラス
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">8位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">主力インファイト（採用率98.4%）は確定2発。相手のりゅうせいぐん（採用率69.8%）も確定2発と互角ですが、S172のオオニューラが先手を取れるため相手の2発目が飛ぶ前に決着を付けられます</td>
</tr>
</tbody>
</table>
</div>

---

## 同居率・パートナー

<div class="partner-grid">
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0876-00.webp" alt="イエッサン(オス)" loading="lazy">
    <div class="name">イエッサン(オス)</div>
    <div class="rate">同居率1位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0445-00.webp" alt="ガブリアス" loading="lazy">
    <div class="name">ガブリアス</div>
    <div class="rate">同居率2位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス" loading="lazy">
    <div class="name">カメックス</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0812-00.webp" alt="ゴリランダー" loading="lazy">
    <div class="name">ゴリランダー</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" loading="lazy">
    <div class="name">カバルドン</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

同居率1位のイエッサン(オス)は特性サイコメイカーで、登場した時から5ターンの間、場全体をサイコフィールド状態にします。サイコシード型のオオニューラ（採用率49.1%）はこのフィールド下でサイコシードを消費するとD+1段階を得たうえでかるわざが発動し、大きく加速できます。ただしサイコフィールドは5ターンで切れるため、その間にオオニューラを場に出してサイコシードを消費させる必要があります。サイコシード型はイエッサン(オス)のようなサイコフィールド展開役がいて初めて機能する構成のため、同居率1位という結果と型の設計が対応しています。

同居率8位のブリジュラス（はがね/ドラゴン）は、オオニューラの最大弱点であるエスパー技・第2の弱点であるひこう技をいずれも半減で受けられます。同居率3位のボーマンダ（ドラゴン/ひこう）は、オオニューラのもう一つの弱点であるじめん技を無効化します。オオニューラ自身がタイプで受けきれないエスパー・じめん・ひこうの3方向を、パーティ内の別のタイプで分担できる組み合わせです。

---

## まとめ

M-6シーズンのオオニューラは使用率19位。A130・S120の高いステータスに、かるわざによる持ち物消費後の加速を組み合わせた高速アタッカーです。M-5シーズン（使用率48位・しろいハーブ主流）から大きく順位を上げ、加速手段もサイコシード（イエッサン(オス)などサイコフィールド展開役との併用が前提）とノーマルジュエル（自己完結型の初手加速）へ丸ごと入れ替わったのがM-6の最大の変化点です。H80・B60・D80の耐久は環境上位の一致高火力に対して薄く、先に動けても1発で崩されるケースが目立つため、採用時はサイコフィールドの有無やパーティ全体での弱点カバーを合わせて検討する必要があります。

関連記事：[オオニューラ考察 M-2シーズン かるわざ型の採用率と立ち回り](/blog/sneasler-analysis-m2/)
