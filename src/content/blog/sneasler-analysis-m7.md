---
title: '【ポケモンチャンピオンズ】オオニューラ 考察 M-7 シーズン 使用率25位の型解説'
description: 'ポケモンチャンピオンズM-7シーズン使用率25位（M-6: 16位）のオオニューラを考察。特性かるわざ（採用率91.4%）で加速する4つの型を比較し、ノーマルジュエル+7.5pt・サイコシード-14.0ptというM-6からの持ち物採用率の変化、苦手/得意なポケモンをデータで解説します。'
pubDate: '2026-10-28'
updatedDate: '2026-10-27'
heroImage: '../../assets/hero-sneasler-m7.png'
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
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" />
  <div>
    <h2 style="margin:0 0 8px">オオニューラ</h2>
    <div style="display:flex;align-items:center;gap:6px;margin-top:6px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px" />
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px" />
    </div>
    <div style="margin-top:8px;font-size:0.9em;color:#555">
      使用率: <strong style="color:#e67e22">25位</strong>（M-6: 16位）　持ち物: <strong>ノーマルジュエル 38.2%</strong>
    </div>
  </div>
</div>

※本記事の使用率・採用率データは2026-10-24時点のものです。

M-7シーズンのオオニューラは使用率25位です（M-6: 16位）。特性かるわざ（採用率91.4%）で持ち物を消費して加速する高速アタッカーで、技構成から4つの型に分かれます。持ち物の採用率はM-6から大きく動き、ノーマルジュエルが30.7%から38.2%（+7.5pt）に伸びて最も採用率の高い持ち物になっています。

---

## オオニューラの基本スペック

<!-- gate:rows start id=base_stats facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
### 種族値

<div style="max-width:480px;margin:16px 0;font-size:0.9em">
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">HP</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#f472b6,#db2777);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">こうげき</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:65%;background:linear-gradient(90deg,#fb923c,#ea580c);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">130</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">ぼうぎょ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:30%;background:linear-gradient(90deg,#60a5fa,#2563eb);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">60</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくこう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:20%;background:linear-gradient(90deg,#c084fc,#7c3aed);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">40</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">とくぼう</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:40%;background:linear-gradient(90deg,#34d399,#059669);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">80</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:5px 0;border-bottom:1px solid #e2e8f0">
    <span style="width:72px;min-width:72px;color:#555;font-weight:600;white-space:nowrap">すばやさ</span>
    <div style="flex:1;background:#eee;border-radius:4px;height:12px">
      <div style="width:60%;background:linear-gradient(90deg,#fbbf24,#d97706);height:12px;border-radius:4px"></div>
    </div>
    <span style="width:32px;text-align:right">120</span>
  </div>
  <div style="display:flex;align-items:center;gap:4px;padding:8px 0;font-weight:700">
    <span style="width:72px;min-width:72px;color:#555;white-space:nowrap">合計</span>
    <div style="flex:1"></div>
    <span style="width:32px;text-align:right;color:#2563eb;white-space:nowrap">510</span>
  </div>
</div>
<!-- gate:rows end id=base_stats -->

A130・S120と攻撃・すばやさが高く、H80・B60・D80という、物理アタッカー向けの種族値配分です。

### タイプ・弱点

<div class="type-row">
  <strong>タイプ：</strong>
  <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
  <img src="/images/types/type-03-poison.png" alt="どく" style="width:44px;height:44px;vertical-align:middle;margin:2px" />
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.92em;text-align:center">
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
  <td style="padding:10px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;justify-content:center;gap:4px">
      <img src="/images/types/type-04-ground.png" alt="じめん" style="width:36px;height:36px">
      <img src="/images/types/type-02-flying.png" alt="ひこう" style="width:36px;height:36px">
    </div>
  </td>
  <td style="padding:10px 12px;border:1px solid #cbd5e1">
    <div style="display:flex;justify-content:center;gap:4px;flex-wrap:wrap">
      <img src="/images/types/type-16-dark.png" alt="あく" style="width:36px;height:36px">
      <img src="/images/types/type-05-rock.png" alt="いわ" style="width:36px;height:36px">
      <img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:36px;height:36px">
      <img src="/images/types/type-11-grass.png" alt="くさ" style="width:36px;height:36px">
      <img src="/images/types/type-03-poison.png" alt="どく" style="width:36px;height:36px">
    </div>
  </td>
  <td style="padding:10px 12px;border:1px solid #cbd5e1"><img src="/images/types/type-06-bug.png" alt="むし" style="width:36px;height:36px"></td>
</tr>
</tbody>
</table>
</div>

無効タイプはありません。エスパー×4が最大の弱点で、使用率上位ではイエッサン(オス)のワイドフォース（採用率99.7%）、メタグロスのサイコファング（73.5%）などが該当します。じめん・ひこうは×2弱点で、使用率1位のガブリアスのじしん（65.5%）、アーマーガアのブレイブバード（27.5%）が通ります。

---

## 特性

<strong>かるわざ（採用率91.4%、M-6: 94.8%）</strong>が主流です。「持っていた道具がなくなるとすばやさが2倍になる」特性で、道具を消費すると速攻型のS実数値は172から344、耐久型は146から292に変化します。他の特性（どくしゅ8.3%、プレッシャー0.3%）は少数派です。

---

## 主要な技と採用率

<!-- gate:rows start id=move_table facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
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
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>インファイト</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-01-fighting.png" alt="かくとう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">120</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">98.4%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の防御と特防が1段階下がる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>フェイタルクロー</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-03-poison.png" alt="どく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">95.8%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">30%の確率で相手をどく状態・まひ状態・ねむり状態のいずれかにする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>ねこだまし</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">40</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">47.7%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">優先度+3。相手をひるませる。登場して最初に出す技でない場合失敗する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>じごくづき</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-16-dark.png" alt="あく" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">80</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">44.9%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">相手をじごくづき状態にする。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1"><strong>つるぎのまい</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-00-normal.png" alt="ノーマル" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">—</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><strong style="color:#dc2626">42.6%</strong></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分の攻撃を2段階上げる。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">アクロバット</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-02-flying.png" alt="ひこう" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">55</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">16.1%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">自分が道具を持っていない場合威力が2倍になる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">ほのおのパンチ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-09-fire.png" alt="ほのお" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12.5%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">10%の確率で相手をやけど状態にする。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">いわなだれ</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-05-rock.png" alt="いわ" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">75</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.7%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">30%の確率で相手をひるませる。</td>
</tr>
<tr>
<td style="padding:8px 12px;border:1px solid #cbd5e1">シャドークロー</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-07-ghost.png" alt="ゴースト" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">7.3%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">きゅうしょアップ+1で攻撃する。</td>
</tr>
<tr style="background:#fafafa">
<td style="padding:8px 12px;border:1px solid #cbd5e1">とんぼがえり</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center"><img src="/images/types/type-06-bug.png" alt="むし" style="width:28px;height:28px;vertical-align:middle"></td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">70</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">5.9%</td>
<td style="padding:8px 12px;border:1px solid #cbd5e1;font-size:0.95em">攻撃した後、手持ちの他のポケモンと交代する。</td>
</tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=move_table -->

---

## 主な型

技・持ち物・EVの組み合わせから、採用割合が高い順に4つの型を紹介します。

### 型1：フルアタ速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（91.4%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> ノーマルジュエル
</div>
<div>
<strong>技構成:</strong><br>
・ねこだまし<br>
・ほのおのパンチ<br>
・インファイト<br>
・フェイタルクロー
</div>
</div>
</div>

ノーマルジュエルを持たせ、ねこだましでジュエルを消費してかるわざを発動させ、次のターンからS344で動く型です。

<!-- gate:rows start id=card:1 facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
**他の型との違い:**

- ほのおのパンチ：この型は必ず持ち、フルアタ耐久型では選択技
<!-- gate:rows end id=card:1 -->

---

### 型2：つるぎのまい速攻型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい速攻型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（91.4%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H2-A32-S32<br>
<strong>持ち物:</strong> きあいのタスキ
</div>
<div>
<strong>技構成:</strong><br>
・じごくづき<br>
・つるぎのまい<br>
・インファイト<br>
・フェイタルクロー
</div>
</div>
</div>

つるぎのまいでAを2段階（A実数値400）上げてから、きあいのタスキで一撃を耐えてかるわざを発動させ、押し切る積み型です。

<!-- gate:rows start id=card:2 facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
**他の型との違い:**

- 持ち物：きあいのタスキ（HPが満タンの時、一撃でひんしになる技のダメージを受けてもHPを1残して耐える。1度使うと無くなる）
<!-- gate:rows end id=card:2 -->

---

### 型3：フルアタ耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">フルアタ耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（91.4%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H28-A32-S6<br>
<strong>持ち物:</strong> ノーマルジュエル
</div>
<div>
<strong>技構成:</strong><br>
・ねこだまし<br>
・アクロバット<br>
・インファイト<br>
・フェイタルクロー
</div>
</div>
</div>

ノーマルジュエル＋ねこだましでかるわざを発動させる点はフルアタ速攻型と同じですが、EVはH28-A32-S6とHに厚く配分し、耐久を補っています。

<!-- gate:rows start id=card:3 facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
**他の型との違い:**

- アクロバット：この型は必ず持ち、フルアタ速攻型では選択技
<!-- gate:rows end id=card:3 -->

---

### 型4：つるぎのまい耐久型

<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:16px;margin:16px 0">
<div class="build-header">
  <img src="/images/pokemon/pokemon-0903-00.webp" alt="オオニューラ" style="width:48px;height:48px">
  <strong style="font-size:1.05em">つるぎのまい耐久型</strong>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:0.92em">
<div>
<strong>特性:</strong> かるわざ（91.4%）<br>
<strong>性格:</strong> いじっぱり<br>
<strong>EV:</strong> H28-A32-S6<br>
<strong>持ち物:</strong> サイコシード
</div>
<div>
<strong>技構成:</strong><br>
・じごくづき<br>
・つるぎのまい<br>
・インファイト<br>
・フェイタルクロー
</div>
</div>
</div>

つるぎのまいでAを2段階上げてから殴る点はつるぎのまい速攻型と同じですが、持ち物はサイコシードで、サイコフィールド状態の時に消費されてかるわざが発動します。ノーマルジュエル型と違って単独では加速できません。

<!-- gate:rows start id=card:4 facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
**他の型との違い:**

- 持ち物：サイコシード（サイコフィールド状態の時に特防が1段階上がる。1度使うとその対戦中は無くなる）
<!-- gate:rows end id=card:4 -->

---

### 型による有利不利の違い

<!-- gate:rows start id=arch_grid facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">相手（性格・持ち物個体）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ速攻型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい速攻型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">フルアタ耐久型</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">つるぎのまい耐久型</th>
</tr>
</thead>
<tbody>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ガブリアス（ようき・こだわりスカーフ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">△</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガガブリアスZ（おくびょう・ガブリアスナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（いじっぱり・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガグソクムシャ（ゆうかん・グソクムシャナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガルカリオZ（おくびょう・ルカリオナイトZ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ブリジュラス（ずぶとい・オボンのみ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">×</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">サーフゴー（おくびょう・ふうせん）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲※</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">キラフロル（おくびょう・きあいのタスキ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メガキラフロル（おくびょう・キラフロルナイト）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ゴリランダー（いじっぱり・きせきのタネ）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">エースバーン（いじっぱり・こうかくレンズ ほか1個体）</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">▲</td></tr>
<tr class="note"><td colspan="5" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎有利 ○やや有利 △五分 ▲やや不利 ×不利。相手の型によって勝敗が割れるため苦手/得意表に載せない相手のうち、自分の型で判定が変わる個体。※＝上の型の技構成に無い選択技での判定。採用率10%未満の技が決め手になる個体10件は除く</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=arch_grid -->

---

## データ分析：M-6からの技・持ち物採用率の変化

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">技</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ねこだまし</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">47.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+9.2pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">つるぎのまい</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">51.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">42.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-9.0pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">いわなだれ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+4.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ほのおのパンチ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.4%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">12.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.9pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">じごくづき</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">48.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">44.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.7pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">アクロバット</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">19.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">16.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.0pt</td>
</tr>
</tbody>
</table>
</div>

<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr style="background:#f1f5f9">
  <th style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">持ち物</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-6採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">M-7採用率</th>
  <th style="padding:8px 12px;border:1px solid #cbd5e1">変化</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">サイコシード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">46.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">32.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-14.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ノーマルジュエル</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">30.7%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">38.2%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+7.5pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">きあいのタスキ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">7.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+3.0pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">グラスシード</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">6.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.3%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#dc2626">-3.3pt</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">ふうせん</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">1.1%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">3.6%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+2.5pt</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:left">しろいハーブ</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">4.5%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">5.9%</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;color:#059669">+1.4pt</td>
</tr>
</tbody>
</table>
</div>

<!-- gate:rows start id=diff_movers facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
- サイコシード：46.7%→32.7%（-14.0pt）。つるぎのまい耐久型が持つほか、つるぎのまい速攻型の一部の個体も持つため、型の増減とは言い切れません。
- ねこだまし：38.5%→47.7%（+9.2pt）。フルアタ耐久型・フルアタ速攻型に共通のため、型の増減とは言えません。
- つるぎのまい：51.6%→42.6%（-9.0pt）。つるぎのまい耐久型・つるぎのまい速攻型に共通のため、型の増減とは言えません。
- ノーマルジュエル：30.7%→38.2%（+7.5pt）。フルアタ速攻型・フルアタ耐久型が持つため、型の増減とは言い切れません。
- いわなだれ：3.7%→7.7%（+4.0pt）。フルアタ速攻型の選択技のため、型の増減とは言えません。
- ほのおのパンチ：16.4%→12.5%（-3.9pt）。フルアタ速攻型が持ち、フルアタ耐久型でも選択技のため、型の増減とは言えません。
- じごくづき：48.6%→44.9%（-3.7pt）。記事のすべての型に共通のため、型の増減とは言えません。
- いじっぱり：86.4%→82.9%（-3.5pt）。記事のすべての型が選んでいるため、型の増減とは言えません。
<!-- gate:rows end id=diff_movers -->

---

## 苦手なポケモン

使用率上位のうち、相手の型が変わっても一貫して不利になる相手のみを掲載します。

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
<!-- gate:rows start id=weak facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ミミッキュ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">3位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型の選択技シャドークローは乱数2発（50%）。ミミッキュのシャドークロー（採用率48.8%）は確定2発で、最後は優先度+1のかげうちで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0450-00.webp" alt="カバルドン" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カバルドン
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">4位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型のインファイトは確定4発。カバルドンのじしん（採用率97.3%）は確定2発で、S172対S67で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0902-00.webp" alt="イダイトウ(オス)" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">イダイトウ(オス)
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">10位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型の選択技じごくづきは確定1発。イダイトウ(オス)のウェーブタックル（採用率89.5%）は確定1発で、S172対S214（スカーフ込み）で後手のため、先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0823-00.webp" alt="アーマーガア" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アーマーガア
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">11位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい速攻型のインファイトは確定2発。アーマーガアのブレイブバード（採用率27.5%）は確定2発で、S172対S78で先手を取りますが、確定数どおりには進まず、先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0149-00.webp" alt="カイリュー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">カイリュー<br><span style="font-size:0.8em;color:#64748b">メガカイリューで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">12位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型のフェイタルクローは乱数3発（>99%）。メガカイリューのりゅうのはどう（採用率32.9%）は確定3発で、最後は優先度+2のしんそくで先に倒されます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0376-00.webp" alt="メタグロス" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">メタグロス<br><span style="font-size:0.8em;color:#64748b">メガメタグロスで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">14位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい速攻型のインファイトは確定2発。メガメタグロスのじしん（採用率68.2%）は確定2発（オオニューラのきあいのタスキ込み）で、最後は優先度+1のバレットパンチで先に倒されます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ボーマンダ<br><span style="font-size:0.8em;color:#64748b">メガボーマンダで判定</span>
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">15位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい速攻型のフェイタルクローは乱数3発（98%）。メガボーマンダのじしん（採用率72.0%）は確定2発で、S344（上昇後）対S172で先手を取れますが確定数で下回り、先に倒されます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。「選択技」は型の4技には無いが、その型で採用されることがある技。</td></tr>
<!-- gate:rows end id=weak -->
</tbody>
</table>
</div>

---

## 得意なポケモン

同じ基準で掲載します。

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
<!-- gate:rows start id=strong facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">アシレーヌ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">2位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">つるぎのまい速攻型のフェイタルクローは確定2発。アシレーヌのムーンフォース（採用率98.3%）は確定2発で、S172対S80で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0197-00.webp" alt="ブラッキー" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ブラッキー
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">24位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型のインファイトは確定2発。ブラッキーのイカサマ（採用率96.0%）は確定2発で、S172対S85で先手を取り、先に倒せます。</td>
</tr>
<tr>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0479-02.webp" alt="ウォッシュロトム" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">ウォッシュロトム
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">28位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型のインファイトは確定2発。ウォッシュロトムのハイドロポンプ（採用率97.9%）は乱数2発（>99%）で、S172対S106で先手を取り、先に倒せます。</td>
</tr>
<tr style="background:#fafafa">
  <td style="padding:8px 12px;border:1px solid #cbd5e1">
    <img src="/images/pokemon/pokemon-0635-00.webp" alt="サザンドラ" style="width:36px;height:36px;vertical-align:middle;margin-right:6px">サザンドラ
  </td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1;text-align:center">31位</td>
  <td style="padding:8px 12px;border:1px solid #cbd5e1">フルアタ速攻型のインファイトは確定2発。サザンドラのりゅうせいぐん（採用率89.3%）は確定2発で、S172対S225（スカーフ込み）で先手を取り、先に倒せます。</td>
</tr>
<tr class="note"><td colspan="3" style="padding:6px 12px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b">※相手は型ごとに判定が最も僅差になる個体。技の採用率は種全体の値（メガ形態も同じ）。自分の技の採用率は「主要な技と採用率」の表を参照。</td></tr>
<!-- gate:rows end id=strong -->
</tbody>
</table>
</div>

---

## 同居率・パートナー

M-7でオオニューラと同じパーティに入る頻度が高いポケモン（同居率1〜10位）は以下のとおりです。

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
    <img src="/images/pokemon/pokemon-0009-00.webp" alt="カメックス" loading="lazy">
    <div class="name">カメックス</div>
    <div class="rate">同居率3位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0730-00.webp" alt="アシレーヌ" loading="lazy">
    <div class="name">アシレーヌ</div>
    <div class="rate">同居率4位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-1018-00.webp" alt="ブリジュラス" loading="lazy">
    <div class="name">ブリジュラス</div>
    <div class="rate">同居率5位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0768-00.webp" alt="グソクムシャ" loading="lazy">
    <div class="name">グソクムシャ</div>
    <div class="rate">同居率6位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0006-00.webp" alt="リザードン" loading="lazy">
    <div class="name">リザードン</div>
    <div class="rate">同居率7位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0373-00.webp" alt="ボーマンダ" loading="lazy">
    <div class="name">ボーマンダ</div>
    <div class="rate">同居率8位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0778-00.webp" alt="ミミッキュ" loading="lazy">
    <div class="name">ミミッキュ</div>
    <div class="rate">同居率9位</div>
  </div>
  <div class="partner-card">
    <img src="/images/pokemon/pokemon-0998-00.webp" alt="セグレイブ" loading="lazy">
    <div class="name">セグレイブ</div>
    <div class="rate">同居率10位</div>
  </div>
</div>

<!-- gate:rows start id=partner_grid facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
<div style="overflow-x:auto;margin:12px 0">
<table style="width:100%;border-collapse:collapse;font-size:0.9em;text-align:center">
<thead>
<tr>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:left">苦手な相手（主力技）</th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">イエッサン(オス)<br><span style="font-weight:normal;font-size:0.85em">同居率1位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ガブリアス<br><span style="font-weight:normal;font-size:0.85em">同居率2位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">カメックス<br><span style="font-weight:normal;font-size:0.85em">同居率3位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">アシレーヌ<br><span style="font-weight:normal;font-size:0.85em">同居率4位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ブリジュラス<br><span style="font-weight:normal;font-size:0.85em">同居率5位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">グソクムシャ<br><span style="font-weight:normal;font-size:0.85em">同居率6位・メガグソクムシャで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">リザードン<br><span style="font-weight:normal;font-size:0.85em">同居率7位・メガリザードンYで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ボーマンダ<br><span style="font-weight:normal;font-size:0.85em">同居率8位・メガボーマンダで判定</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">ミミッキュ<br><span style="font-weight:normal;font-size:0.85em">同居率9位</span></th>
<th style="padding:6px 8px;border:1px solid #cbd5e1;background:#f1f5f9">セグレイブ<br><span style="font-weight:normal;font-size:0.85em">同居率10位</span></th>
</tr>
</thead>
<tbody>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラの弱点：じめん技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1">無効</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラの弱点：ひこう技</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#eff6ff"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">オオニューラの弱点：エスパー技</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ミミッキュ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カバルドン</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">イダイトウ(オス)</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">アーマーガア</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">カイリュー</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr style="background:#fafafa"><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">メタグロス</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left">ボーマンダ</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td><td style="padding:6px 8px;border:1px solid #cbd5e1">—</td><td style="padding:6px 8px;border:1px solid #cbd5e1">○</td><td style="padding:6px 8px;border:1px solid #cbd5e1"></td></tr>
<tr><td style="padding:6px 8px;border:1px solid #cbd5e1;text-align:left"><strong>受けられる相手の数</strong></td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○4</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○5</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎2・○2</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎1・○1</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○3</td><td style="padding:6px 8px;border:1px solid #cbd5e1">◎0・○0</td></tr>
<tr class="note"><td colspan="11" style="padding:6px 8px;border:1px solid #cbd5e1;font-size:0.85em;color:#64748b;text-align:left">◎＝主力技（採用率30%以上の攻撃技）をすべて半減以下で受けられる、○＝最も採用率の高い技を半減以下で受けられる、空欄＝最も採用率の高い技が等倍以上で通る。青い行＝オオニューラの弱点タイプの技を、◎＝半減以下で受けられる／無効＝無効にできる。—＝相手と同じ種族。列はパートナーの同居率順。メガ石の採用率が50%以上の種はメガ形態で判定。主力技：ミミッキュ＝じゃれつく・かげうち・シャドークロー・ウッドハンマー；カバルドン＝じしん；イダイトウ(オス)＝おはかまいり・アクアジェット・ウェーブタックル・クイックターン；アーマーガア＝とんぼがえり・ボディプレス・アイアンヘッド；カイリュー＝しんそく・かえんほうしゃ・10まんボルト・りゅうせいぐん・りゅうのはどう；メタグロス＝バレットパンチ・サイコファング・れいとうパンチ・じしん・かみなりパンチ；ボーマンダ＝すてみタックル・じしん</td></tr>
</tbody>
</table>
</div>
<!-- gate:rows end id=partner_grid -->

---

## まとめ

<!-- gate:rows start id=summary facts=07d0f978a64ee33511009ece2c424cd8477da27b -->
**強み**

- 得意な相手は4体です。使用率上位では、アシレーヌ（2位）にフェイタルクロー、ブラッキー（24位）・ウォッシュロトム（28位）にインファイトで勝てます。
- タイプ相性では、くさ・かくとう・どく・むし・いわ・あくを半減以下で受けられます。

**弱み**

- 苦手な相手は7体です。使用率上位では、ミミッキュ（3位）のシャドークロー、カバルドン（4位）のじしん、イダイトウ(オス)（10位）のウェーブタックルで先に倒されます。
- 弱点はエスパー（×4）・じめん・ひこうです。

**型の選び分け**

- 「フルアタ速攻型」：ほのおのパンチを必ず持つ（フルアタ耐久型では選択技）。
- 「つるぎのまい速攻型」：持ち物はきあいのタスキ（HPが満タンの時、一撃でひんしになる技のダメージを受けてもHPを1残して耐える。1度使うと無くなる）。
- 「フルアタ耐久型」：アクロバットを必ず持つ（フルアタ速攻型では選択技）。
- 「つるぎのまい耐久型」：持ち物はサイコシード（サイコフィールド状態の時に特防が1段階上がる。1度使うとその対戦中は無くなる）。
- 型によって勝敗が変わる相手は「型による有利不利の違い」の表にまとめています。

**M-6からの変化**

- 使用率は25位です（M-6: 16位）。
- 採用率の変化が大きいのはサイコシード（-14.0pt）・ねこだまし（+9.2pt）・つるぎのまい（-9.0pt）です。
<!-- gate:rows end id=summary -->

関連記事：[オオニューラ考察 M-6シーズン サイコシード×かるわざ](/blog/sneasler-analysis-m6/)、[オオニューラ考察 M-2シーズン かるわざ型の採用率と立ち回り](/blog/sneasler-analysis-m2/)
